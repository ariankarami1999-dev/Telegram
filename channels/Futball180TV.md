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
<img src="https://cdn5.telesco.pe/file/KPm2JpNcySCLoD792yKLp5hFKu9bjs53jR6nvetrIXqnvFBi03zUAEYu-HrE9Msxl-bmuepnmKE1W5P-CL_Mg3-L-EqH_O7W-bs2-A4rLf0EKQm3ivnftoDWvurjF80Xu8oGeKfN9z9ktzXilYBJR2QZsllciy3capovzqFXXFsBmdX-ESTQfwpG21nn5QXOIsOZv8jqhc9fWS2BIA2XL0L1Cq2ELmpM_D7MEn9Sl8zRsaQhhOj-WXfoxp4mUx6YVnWSPs7E5aYJRuCu_9PzQKa7vF9S-7YAsBvA73am8GbeqqvAexA8cGGoKvwlultsbwn8DFBi6Pk7BpM1g9v4hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 673K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-94473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea022c974b.mp4?token=JNHwu6G9aCxmHHxJlCu2iU4jNBGlBkvl0Rmou5b8apLuVy46qXqMJY7koJ0Xs1BX6D7z-I_2UdUBq6r1IyxfJKYiRf-NdDoG3OCUA9JeStsQFdUbGkQaKRPc7MzYi71geazSUG78jMNH_3k2Wc-LfZLiSjMB9rCK2PZzbhzAjJ6v6Qwtr50oMkb9OFABwVz2Yjw1JpsFmZ6FtR9SA8n6yA5FK2DqKvF3Y_mZZozsYyoCaJgMhY5pUsW_1iMdZ9AShzvEW69ZeoBPkIndXvtIeFvsbIufGYJJlMuJJHPk1dG0SlnyOyrcgMPakB1DHcu3OMXG92GMnglEQG0E3soG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea022c974b.mp4?token=JNHwu6G9aCxmHHxJlCu2iU4jNBGlBkvl0Rmou5b8apLuVy46qXqMJY7koJ0Xs1BX6D7z-I_2UdUBq6r1IyxfJKYiRf-NdDoG3OCUA9JeStsQFdUbGkQaKRPc7MzYi71geazSUG78jMNH_3k2Wc-LfZLiSjMB9rCK2PZzbhzAjJ6v6Qwtr50oMkb9OFABwVz2Yjw1JpsFmZ6FtR9SA8n6yA5FK2DqKvF3Y_mZZozsYyoCaJgMhY5pUsW_1iMdZ9AShzvEW69ZeoBPkIndXvtIeFvsbIufGYJJlMuJJHPk1dG0SlnyOyrcgMPakB1DHcu3OMXG92GMnglEQG0E3soG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
هوادارای مسی تو بنگلادش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/Futball180TV/94473" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94472" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/Futball180TV/94472" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 313 · <a href="https://t.me/Futball180TV/94471" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHX7aPTWhj7geL42SkyNTVUtQIw7sOlTyhLRFdTe_1843d3kD9pHstf6P6u9uxB0O60ln-D2Kmf0qdFa8IUsdHJ2RI3awL05GAK8QPnUuBdkGPyC0kxk6uSfudO8j-CKNwc86tUabRixjuuxF-DyiFS2KqeaBB35MzkYsfnS3gWPjS1aSCnVS5-NAn2Whiou5Px1MpQagQvuFi3iNdreUK6BsvIfh7X5QMSzl1gqztzItkvyzItPSvBGtvOdlYJ3XpbARRoejk7cfXM-uqOFe5-csiY7ZXH7zQkTWHubilzduWxdBrOiAnyoWaQKCyxHGvin2YSLViE1e5ZrfaJoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ روزنامه SER: قرارداد کریستنسن با باشگاه بارسلونا به مدت یک فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/94470" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVTxGMuqmmBZlhlPCQJ2Ar2aEt7pwUfRJ-Axp9IERHCa2nMzXWDf5_t-poWwgXcyH8T2BKUxuNADnOoPZk1UlkoLZ0JoGOc9DyPe_W0Gvnm302lnkJWauWf4Q2mAl7IKH95qOLRszjeM-gep06i3PK497jldcP5YyjizqpkmNFlVeTdoR3zfmBdCmPmXubeA72E2Zn0fllDBIvrR9G6RiENJ6exe0_h7EQzOrb8cmcAk7pwvIWVhvEh2bzGc-RgeZnW26eeNfPskMbFoQqOlAa5sJ0gKu0UApJCZaQhLPqgrZqdKL1dCRwEeiJHkO9XH-9eI_OaF-SO43QlcIM96fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اکیپ:
بزودی دادگاه اشرف حکیمی به جرم تجاوز قراره تشکیل بشه و وضعیت نهایی اشرف بعد از دادگاه مشخص میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/94469" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f9169375.mp4?token=O-dr-lDu5JzoNE0bo1upXzG5xk3bXGfG9ez4CbXqKRBA32Oua6mGQ70PGk32HLXB26E_p8blx1W0lcdIvTkEnqGixd3Fs0BvULsYlnJtYeIdsldbYe2zb3FR9YAWheeaP4AbIltZOTssR7uzCZlfvaXu6N53KJ21QU7c5FWL4J1mJIWw15OrsuzqhQxdb8Kyq_RZzcrJ0bUxBRn2AF6teKpsEreG3mTUb4CFsA7U8so95vDOzBEd5Eh0VjQFIOiRccgznzkI51z2-jzD-MRAmexcqb2CGRFhI2KLjEDZOMZ8k3jvA-TfowIbxlXtimopLWMqRCUaUfO6GSH65914gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f9169375.mp4?token=O-dr-lDu5JzoNE0bo1upXzG5xk3bXGfG9ez4CbXqKRBA32Oua6mGQ70PGk32HLXB26E_p8blx1W0lcdIvTkEnqGixd3Fs0BvULsYlnJtYeIdsldbYe2zb3FR9YAWheeaP4AbIltZOTssR7uzCZlfvaXu6N53KJ21QU7c5FWL4J1mJIWw15OrsuzqhQxdb8Kyq_RZzcrJ0bUxBRn2AF6teKpsEreG3mTUb4CFsA7U8so95vDOzBEd5Eh0VjQFIOiRccgznzkI51z2-jzD-MRAmexcqb2CGRFhI2KLjEDZOMZ8k3jvA-TfowIbxlXtimopLWMqRCUaUfO6GSH65914gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⭐
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا، در رختکن این تیم پس از پیروزی قاطع 6 بر 0 در برابر قطر و در سایه مصدومیت شدید اسماعیل‌کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94468" target="_blank">📅 19:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d44fd743.mp4?token=j7xdUQTPY6v92lXTxTSfD9phig_ozTzS1izY9DnTgmDQACxZkgm_-oNt8_qmwylutVh56009lb6mVndih5STPBwaF9smOULZH6ty_w7nyVwj9vCV5LAkpImlG8xb0zXnZZo9157RskTiwfQra1_x6BvTOFf0_jaE7Gf_o-gDeL6l-IZxO_lqITcqz4t_glE3ZLM94kn5eMn9wJqfVjL-T2B7RguD0kJ127_Dv63IJ2gpSqmOhnJegmiz3NBfhCqkqt-QcXi9f90Wp9MHmQnQISbKtbR2X66vP5QCgAlqZK9rzN_uAl1ZGWGHnfqFd9E4DKOEoskQHX0rHTWOrIrhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d44fd743.mp4?token=j7xdUQTPY6v92lXTxTSfD9phig_ozTzS1izY9DnTgmDQACxZkgm_-oNt8_qmwylutVh56009lb6mVndih5STPBwaF9smOULZH6ty_w7nyVwj9vCV5LAkpImlG8xb0zXnZZo9157RskTiwfQra1_x6BvTOFf0_jaE7Gf_o-gDeL6l-IZxO_lqITcqz4t_glE3ZLM94kn5eMn9wJqfVjL-T2B7RguD0kJ127_Dv63IJ2gpSqmOhnJegmiz3NBfhCqkqt-QcXi9f90Wp9MHmQnQISbKtbR2X66vP5QCgAlqZK9rzN_uAl1ZGWGHnfqFd9E4DKOEoskQHX0rHTWOrIrhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
آرژانتین امسال از شانس های اصلیه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94467" target="_blank">📅 19:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr6jncnXQSrVJDSMlTQkgbrk2L-7vG2vr31ZWogcOlA3-Lt7Idq_jErMG4dk20uJ1FljSnHSOYxPQtA-dMNaBTGpRKCTWDvy0dXMxYTHxNLthiaxAgN3dxXRzgc_J9AhIA8XhSpXZLLIBxGmhdv1EbWfQoeE21xu0brxluWK8N23NTl22bOcEWTuGiN57uJgGBqsZ1hmIGrut5-kIS1opnM57mM-PNKp1PTrAiv3kPjm6zwIUtaUWxnNUB_K1Y45SP_0p1-rrzy6mreJWO5ClhjcOUGzAQyDx8exQWFaDbOMnAUkAIgghgiDiRHPK2dIkuSk2lyCnHIoIr0kvRnCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
پاسخ تباس به شکایت بارسلونا علیه پرز:
"این اظهارات غیرقابل قبول است زیرا بر اساس شواهد اثبات شده نیست."
"لالیگا قبلاً چندین بار مخالفت خود را با رفتارهای رئال مادرید و عملکردهای معمول آن از طریق رسانه‌های رسمی خود، از جمله کانال تلویزیونی‌اش، اعلام کرده است."
"لالیگا به احترام روندهای قضایی ادامه خواهد داد تا حقایق روشن شود، اما بدون تردید در دستگاه داوری."
"لالیگا علیه هر نهادی که بخواهد به اعتبار مسابقه آسیب برساند، اقدام خواهد کرد."
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/94466" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnI2eLZN3pCmHNi6JE-ILce9h7XzReG2UkBJBxko8Hm8IpnGhRr_r9GU8qU0881kCsjrPSzGGLJhIlkGog3DulXOitj_1Y8afoFAPoB3OjHURVf3oOuCTvQTlNRWdkGSlRkkiZrBNF-Xq8U0cdM0YZAYDp53QbtOj-ys8FaC2_UL47X71YX_QHqibr_NVx5SWPPHJWqpgldGD9lENylLP-e-np5bkTzUW7HCmDmwEG9tGI8k3UhL9cWMlGwhAKko2e5eJMLYL_SWrlHP5jCmo7QJEu6Ro6cAruDRXtjt4hUSSFHzf5_vOjGGw14g9-d0OM4Q0719u8BGa6aOOGvUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از شور فوتبال تا شوق زیارت
با فرارسیدن ماه محرم، حال‌وهوای معنوی این روزها برای بسیاری از مردم با آرزوی زیارت کربلا گره می‌خورد. در همین حال، کمپین پیش‌بینی جام جهانی در اپلیکیشن «
همراه من
» فرصتی فراهم کرده تا این شوق، به سفر عتبات عالیات تبدیل شود.
🎁
بر اساس اعلام این کمپین، در هر مسابقه تیم ملی ایران ۳ نفر به قید قرعه برنده کمک‌هزینه سفر به عتبات عالیات خواهند شد؛ جایزه‌ای متفاوت که در کنار هیجان پیش‌بینی مسابقات در نظر گرفته شده است.
فرصت همچنان باقی است؛ تیم ملی ایران در دور مقدماتی همچنان دو دیدار دیگر برابر بلژیک در ۳۱ خرداد و مصر در ۶ تیر پیش‌رو دارد. در صورت صعود به مراحل بعدی نیز این جایزه ویژه برای هر مسابقه تیم ملی کشورمان ادامه خواهد داشت.
💫
به این ترتیب، حداقل ۶ فرصت برای برنده شدن این سفر وجود دارد؛ فرصتی که شاید برای برخی کاربران، از یک
پیش‌بینی ساده و دقیق
آغاز شود و به مسیر کربلا ختم شود.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/94465" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bd2371280.mp4?token=JtsoYxlzLJ_hUnEHnJHc6TbVM-adt9CJJbKA0wDZnBAMtS0j5mVD-tdyVnGGVwCEOVF-iYfrHzsRMH-L5HqjX-3fuBIGlF3MFiuUFJ6UadXx8TdVh2-Ky3K5tBaThMjeee-XXCboMNgZLIDRrEIfgQlqg-_HJboHfrJYz6XbcvBJ4qHSQfYm0j0lqeAAQXmvaqbJlpRlh7npq20-4klObNkMmNrI7V56g8mpYwfz6Eq1XDbnxHB2AOEpQNmroYYnmx5u7XACnd9waQTEJEwYoxtp2fJidF_g9g8A6tW9B3X-6fsVFn_Cm-STEkuUaW2tsu06aJdasHnsabuUrZn43Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bd2371280.mp4?token=JtsoYxlzLJ_hUnEHnJHc6TbVM-adt9CJJbKA0wDZnBAMtS0j5mVD-tdyVnGGVwCEOVF-iYfrHzsRMH-L5HqjX-3fuBIGlF3MFiuUFJ6UadXx8TdVh2-Ky3K5tBaThMjeee-XXCboMNgZLIDRrEIfgQlqg-_HJboHfrJYz6XbcvBJ4qHSQfYm0j0lqeAAQXmvaqbJlpRlh7npq20-4klObNkMmNrI7V56g8mpYwfz6Eq1XDbnxHB2AOEpQNmroYYnmx5u7XACnd9waQTEJEwYoxtp2fJidF_g9g8A6tW9B3X-6fsVFn_Cm-STEkuUaW2tsu06aJdasHnsabuUrZn43Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که جام‌جهانی داره پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94464" target="_blank">📅 19:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxBlJ80nCjbFig9PRvLMOHucyZOXmcCtSleYKDYzgXRqU7hWcKWY7C3MMzuRGXeD7swXg8PUpWX9p295iwx7E0f0mBoZZVlwNTlZ_bp2cB7DMLZ4N-AFNbN4EJsq3FgADkecKh7sJx2WHS3EQLDAdHaKSTv60uaaxNraFr2PKaURaZNfqK-nAN1kcPLLU7nDHofkJ8BZ46eiL4im-r9FUk6n97VjCm8zObvWNamLbM3hIMmFplvYuYzeECaC2zv7aV6LYEJc9Md0ojEjddMEUQtHxq2lFXk2lRBQiWBeBi16F61mcUip5TEV9LK5-OzF_UQHg7p68ss9mUbVqMR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🗣️
دیس ماتزاری به زلاتان:
🔻
ابراهیموویچ به دلیل عملکرد ریدمانش تو میلان بزرگ‌ترین طرفدار اینتر در تاریخه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/94463" target="_blank">📅 18:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8dggc1NTeQHFUuVjcVRhiIo7eaDFNUu3PIKtyoMDKlCsL595evVCv3yRFAyHgHpc6L0p5KYBC3Eqrar9UhOxbn38JYq9MhvuYxrydMWtvS0VxtkmjWW5S8vN3QnG-iDrJ49TRrz2nJKoFRshbSjwTfoioPJWdzfMR6fFR1sAjfqpBOhjNBpEM2c4cuMIVZQa3_ImQQ58akiMJKwc9SCAzOEIFTqUeBO2MYdmqBEjo9SHeJXrJEkFkdYI1fi7eC9UuZ8C7j0Xo2L5sbF1hQrk_X1AyLpmqOZG6peMamJXdmB-u3OQAf8dHEDAXkJFlhRgS9v46BY2zu9ughafvuVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
رئال بتیس برای گارسیا به رئال مادرید پیشنهاد خود را ارسال کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/94462" target="_blank">📅 18:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxfJ-i11sNYJqSFP0kOYii-rtB0ak2B1Q-iBEVlI--XDT5HtKMavWgsZG48tQdLW_0b_dRPc35DWot6BXg_RWtXEWPpJv6Muvg_IOF1EDP13wUljm_o2gbOgBp_3KJDidi3fs3BdLM-rhMst-yZZdgKFZE_5HRLb6YlV7fjAFoS_EScFoNCfPgX0yc5pbgwb1WqOjxW9FAKCZRk8fSBbFvMJ_lG49xaUeN5K5EuwZDwHu3SvhJ8BbXooQAB5W3w02seKG8dIUF-UC8_V9EnxKRRTHPZhXHUpeRJaqeIUUlefYDM2ngZma8fNO430HsM0svM75cwn4PRnNMBuIlJlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری آاس:
مورینیو به جذب الساندرو باستونی علاقه‌منده اما اینتر برای فروش مدافع ایتالیایی خودش حدود ۷۰ میلیون یورو قیمت گذاشته و کمتر از این عدد وارد مذاکره نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94461" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHq9D3Pp9n15cXdxgiBIE_Tb-RURkRzEvrXJaX_Ifiq-UwvV4OBHJ61G7EDTI1ndjUhyNBy2tGuFcvdunRfbaxSE8_vYdIaFaDeZm2UIZicrYPLDFOh0KG-gE1FbJomanKpOHAbAutum8jE7eM3brUNoCH48Jp17Uj_0kIorvXwq1Cxgp2fzau_Vbq9FObXUX_yxPua5HFpQMFSxUHiavCXtWnWSnTZL8TrS_VR3qGs61xhgRMaybvpRbr8_hiLRDE9mdCJaCZ8QsP3CAeIdA2cYvuus-PJU_oXJ-8r6r4V5Qf3qERJT4aHFimI6owoqIiyjt0cassSxGJee5dYwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پیشبینی‌ هوش مصنوعی از مرحله حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94460" target="_blank">📅 18:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126dd65d76.mp4?token=JTCYX6UsIqSo2imi7VtBIzA3DOH86AaGFJZcvKqIaTb-6OwG4uKpRhx00ujYdERLxhP3Xk5Byzz5cspvfeqgiyZ93oekZlzF7fZfMXLal56NIw3hJ214lQtpjfx_CWWOd2Qb_8v9Fl2DuLfj9Fh5JHD2yJiZqJ467aED70APIEvE-UBXplxQ-k0m_rRum5NPjNuJ9dSL3nUvWILxzyzQs_LU19CxRP0wKGrg02IgavFTAFl8fYem8AqGTlyWgEerPH37zwLB5QgEQMAt-D2pnb4DJIYOmW_TdcfOH8-kAZj3zMXKSLaJJdej60cJI-UvGTRSJBLUPx6AHxr5tsk1nKSIbTUAjfp84UPR1K_iUV1ziLtuw4s-5CijBXJ0dtgH8RJVYjZybGZODoaWqgUnR3C2azH6GYqVkPMq_MN8GJ04anYyauMdNAvH-qS0FqV8bN_tN3HPSAuZKAARVaogOjUFJSOlFJYHrf2Th3QEaauIJ7JbFh4CGLNhCNdj-XFpbh5iLWdrvBlCEOlFwsyGL5HbCi2cbYTdv8AEh_vtXhyIVxB1o5f_ToZAJZY8AMTy7Qz757DBpmODwrcPYFJ3dlPGJo2-0z9WDCywuBaunBexKxYWmSCO8soJ2X2R1FeMzeQ-Ef7I9uFurOx2ZsfC4qp5im58im8m-K58NtcXdzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126dd65d76.mp4?token=JTCYX6UsIqSo2imi7VtBIzA3DOH86AaGFJZcvKqIaTb-6OwG4uKpRhx00ujYdERLxhP3Xk5Byzz5cspvfeqgiyZ93oekZlzF7fZfMXLal56NIw3hJ214lQtpjfx_CWWOd2Qb_8v9Fl2DuLfj9Fh5JHD2yJiZqJ467aED70APIEvE-UBXplxQ-k0m_rRum5NPjNuJ9dSL3nUvWILxzyzQs_LU19CxRP0wKGrg02IgavFTAFl8fYem8AqGTlyWgEerPH37zwLB5QgEQMAt-D2pnb4DJIYOmW_TdcfOH8-kAZj3zMXKSLaJJdej60cJI-UvGTRSJBLUPx6AHxr5tsk1nKSIbTUAjfp84UPR1K_iUV1ziLtuw4s-5CijBXJ0dtgH8RJVYjZybGZODoaWqgUnR3C2azH6GYqVkPMq_MN8GJ04anYyauMdNAvH-qS0FqV8bN_tN3HPSAuZKAARVaogOjUFJSOlFJYHrf2Th3QEaauIJ7JbFh4CGLNhCNdj-XFpbh5iLWdrvBlCEOlFwsyGL5HbCi2cbYTdv8AEh_vtXhyIVxB1o5f_ToZAJZY8AMTy7Qz757DBpmODwrcPYFJ3dlPGJo2-0z9WDCywuBaunBexKxYWmSCO8soJ2X2R1FeMzeQ-Ef7I9uFurOx2ZsfC4qp5im58im8m-K58NtcXdzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏆
صداشو کم‌کنیددددد. ویدیو جنجالی وایرال شده در خارج که قبل بازی ایران رو نشون میده و ایرانیا همو فوش‌کش میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94459" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHhObrxJxVqzhG0pjds9nt6MJuUbEgGxesdjpxjxbbWhFbJrNk9uzBONILES1Zm5suMJcpWCMXJFY5k4O-WUWuOHJDwz1poGjtBB8KOvidrXMwkRdvT-f5saxAA-LNz7KbCsF2C6llgTIO4yBENyqOmJriH7rKWKo2W-VwTbCJp3S12JS07XOQ_5vCOpPCKrOXsibdkgXATpWiniS-VnBxH63IfOqOgrRFJiQaaKF48X4Ib85myGZBb1j9q15V6w-hycQtHvNOcAYGo2j5fmtfbOgBucSk4sbofAmp3ZaR3TAFaOK3KoGn6s6f6nQxhFqBA6QlZ5PYJAq4UfYGyRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرت در مورد هتریک مسی ؟
یامال : مسی هر بازی بیشتر ثابت میکنه که اون بهترین بازیکن تاریخه دیگه حرفی برای گفتن نمیمونه، نیمار الگوی منه، ولی مسی بهترینه تمام دورانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94458" target="_blank">📅 17:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a748cd76e.mp4?token=XOTwxFy_Y6-oeMiHsylfqDN0xLy4HdigfaEbgmZcRxyEfO6ZL8Lm3PPbE-Y9q67ge0BqoSJrl2ySCZpIqOdsRLVTjXR2GKFat1iUDqGzCInqjgZrp6WykTCBxJ4-rBVtcHNC1y2geDKGEmU4YCoX2hy1SZZLi-72vmXI9cFgAlmeYnP5ZTvQZStnKHvkzVyaYWKCBZLxtU5MbgBAG72wrsdfJGf0v-ArcQupWqBuBlGqzrQFIS9azHBCUBxAfIUBCkLjDyJT_wCVIalypvRHfN0K8WEt1WmJuDm46kZdh9wvu5v1X61GC85o-Joe39WVzZHybR5rlOeEbzZDnQM85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a748cd76e.mp4?token=XOTwxFy_Y6-oeMiHsylfqDN0xLy4HdigfaEbgmZcRxyEfO6ZL8Lm3PPbE-Y9q67ge0BqoSJrl2ySCZpIqOdsRLVTjXR2GKFat1iUDqGzCInqjgZrp6WykTCBxJ4-rBVtcHNC1y2geDKGEmU4YCoX2hy1SZZLi-72vmXI9cFgAlmeYnP5ZTvQZStnKHvkzVyaYWKCBZLxtU5MbgBAG72wrsdfJGf0v-ArcQupWqBuBlGqzrQFIS9azHBCUBxAfIUBCkLjDyJT_wCVIalypvRHfN0K8WEt1WmJuDm46kZdh9wvu5v1X61GC85o-Joe39WVzZHybR5rlOeEbzZDnQM85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: خوشحالی من وقتی است که مردم ایران خوشحال شوند/همه تلاش خود را می‌کنیم که در جام‌جهانی اتفاقی را رقم بزنیم که دل مردم ایران شاد شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94457" target="_blank">📅 17:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94456">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001a9bf699.mp4?token=FV_p3hlx8i72mMqxTKq28-BVzmNbEpc-5d_h2wQJAnGBKQRfDzZMCOskbfgiYmVfzOLOuZ6Sofy_kjvC25xSzKQoU_X9Qgop6k4YIkDe-tm39i5hfoq4yFAFtmBMNk4oWbeYZehrx02nTshBlM5zcR0MsxB4TgBzqFmZAsfJ-aVMJSYIAUY3IXpgpM9pczAbDe1b4qDxjAxFVkPV1XhYWsCgUdQ1mKsflMI9DbgNmY86Jnjx0qu1zxlkmcgcsJbxc0SEMs6QuGG0tw1hY55T3OhDIJC6nbRbmkOC7_gKuqHqGLR402BzFY5qWdGVUBzGgM6ZieUhsHe07MELSzlrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001a9bf699.mp4?token=FV_p3hlx8i72mMqxTKq28-BVzmNbEpc-5d_h2wQJAnGBKQRfDzZMCOskbfgiYmVfzOLOuZ6Sofy_kjvC25xSzKQoU_X9Qgop6k4YIkDe-tm39i5hfoq4yFAFtmBMNk4oWbeYZehrx02nTshBlM5zcR0MsxB4TgBzqFmZAsfJ-aVMJSYIAUY3IXpgpM9pczAbDe1b4qDxjAxFVkPV1XhYWsCgUdQ1mKsflMI9DbgNmY86Jnjx0qu1zxlkmcgcsJbxc0SEMs6QuGG0tw1hY55T3OhDIJC6nbRbmkOC7_gKuqHqGLR402BzFY5qWdGVUBzGgM6ZieUhsHe07MELSzlrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇴
🏆
هواداران دوس‌داشتنی کلمبیا کف آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94456" target="_blank">📅 17:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94455">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuF89wA1046k38-CY6dtwjyUXjEeuf1fEAE-nk7mn_T3vF83rgU8R9DL08EWcZ6f-bjd6UQvQ-W9kpkhcoFmWgSFrBJDm1xMejVSbuyFzQAvxcW5MUiqkQ04ZcahlPGygTLKAWxFClvLZBCSN3v8OB4VJ-8MqdTfhp0cUD9_dabcC3uHVTJTezxOhvi_3W1xPPadbOko5tGUNu2_peqBVgSUsH1iWioQotfNqT6DDchOnjZHZFpJI9-Y9X3529nTdTplmL_VRqglAw3Z33S9HL_kiolgnMzFlOmCoTD8NKQYoRkIq8W4rMQDyN9hO5yvQLUl7c4WSlleRe5uU7oYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🚨
دیوید اورنشتین:
منچسترسیتی به‌دنبال یک خرید بزرگ در خط هافبکه و میخواد همزمان برای جذب ساندرو تونالی و الیوت اندرسون اقدام کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94455" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94454">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb9tsiGgNMg5G6F9zDplrYzZd6n_jLPNLXH2dJ7_xI9Hg9mCWQ9L30coI3-MbMExFw9ekdvLYsNieCeDanyjUnSMKyv4cJWRw2bPLpn1Wfl9vlbM9he0fSbGCcNQlQQf5Xt0d8NmwtQmyQkBI9aftJO8Dt59I3yO7YO_nzoRovZisSp4EPlNT0PyjF9lCqzy6VuU5eg9eAb-wbxLMnmx-Z7KyAF9N_PIi_AmFe9nm9O_i9AwDc0DNhxAjheBrAoHeWROJFaEOUk4iYP0BmMDZ74HK3awHlTnhYgWpIGMVkMMP0NjF5lfzga5Z4Ev-BRS2l73gdyzqLWJHcK4wOEuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
اتلتیکو مادرید با الخاندرو گریمالدو به توافق شخصی رسیده است و انتظار می‌رود این قرارداد به زودی تکمیل شود.
🔹
ارزش این قرارداد 12 میلیون یورو است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94454" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94453">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ijJG-TF9TuffLYGGSypPNNHOrN0KAo5dElQ7lBjlhFzNDbPlcEW1YsQOVlaQBXKFRdw46Bbpny09qNGU2znfrIF6C71HAQMYagi0HH72O4cQuPu8bsC5IJZVUB78kHqLY70uDOiyNye-Hq5wtzfa9zN1rLA36Kr5RTcDyCSKed1mZD9_4tL89nkYx9hVBSlSD5vQYx9nii81Wmo4Zjzuim6iy6LjIPqgRR4K5i_ko_wpv9BI-Kxh7uVfE4eFfJroJ-jWPDfvhVCBUMsSUzFnFy7ZJw5700YXf9o6ryUI9nxVr71ViAjXwmvjFuZ_sO54YBhw9i_HbmxXCu90xFEzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۷۰٪ تخفیف ویژه آخر هفته روی کالاهای منتخب
💳
خرید در ۴ قسط و بدون کارمزد با اسنپ‌پی
✨
مشاهده محصولات و خرید با تخفیف ویژه
🔗
https://jwir.ir/ir1</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94453" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94452">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c628dc86c.mp4?token=MVVrAbWPYNHULsWXB7QJOkd_kIbB_vLv5F4mW2Pk9kvHVl1APNKAeljfP0hxibTpRsJj-MqeCrzsrm4wyb5UEdCeCrR3IUbqZbRCbBbtOYEoP2e54Bl3DX3zE1zzOsNtyR_uj_ohhvs1VuGHjle0b58H8PAeRpkwSClPWSnCYvokf-iJV96bokhsiprUXl-iGNWNlq9P6zEwGGShIkTJjAnhAA9BdDYZWDZCvSo9qJjm4oXSao7OJn1mWt5q4OiTcunVHvySoTk_zACfdW2DRyLamaCj4MFvuyIp1CXyEnsiMa5TvZPMIK6QGq1uW20NZDDuSYdn2ZIOkfrqUu4SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c628dc86c.mp4?token=MVVrAbWPYNHULsWXB7QJOkd_kIbB_vLv5F4mW2Pk9kvHVl1APNKAeljfP0hxibTpRsJj-MqeCrzsrm4wyb5UEdCeCrR3IUbqZbRCbBbtOYEoP2e54Bl3DX3zE1zzOsNtyR_uj_ohhvs1VuGHjle0b58H8PAeRpkwSClPWSnCYvokf-iJV96bokhsiprUXl-iGNWNlq9P6zEwGGShIkTJjAnhAA9BdDYZWDZCvSo9qJjm4oXSao7OJn1mWt5q4OiTcunVHvySoTk_zACfdW2DRyLamaCj4MFvuyIp1CXyEnsiMa5TvZPMIK6QGq1uW20NZDDuSYdn2ZIOkfrqUu4SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏆
این ویدیو خود خودشه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94452" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94451">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl_j9jQRjYPf5QnUd3TuaAjtCj5Yv8iP2biB5Rdmk6Cu8hknSCoMtgkQf0JTpZUsM5VaKyd3KkTlLgWUQBK7_O8oXnNPbt79Zt1IlogOUtnnb7Lc2nl8zztdn9wvpMB9rWpOaiAXKN2vo3mGdArcb0lWoHDwLm533PSoKnoO8fHMV6SlhpXgyp6pAH0cPHQyaVotntbQUdzHu0Sv3Df5llb-aZfBngrdVlFgH-T-IA7HsSMChWnKUZTVn7bYCikqsyjeTDbE9TvwXdNX0UiNLa288VjPccA8TrFwtb7to14FiJaaG0v6vGtz74AtokAc3txYqUtlk_L2NT2xwo83dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تعداد کارت های قرمز تو جام جهانی‌ های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94451" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQfu8rb0LkPPVK8KxBjPa0-MlAEiPfa5_1wF6i5niX4tD1TUw5FnVixVbD_1Ly6e4WvbIYFDgWu--d5HepgbPiFUcskB3CZTU6B4EJ0MWxDRTw5xgH1QUo81MzG1JqGV6xjNAPoiO2JeOp3etwRrEeKbR-lWFvf4xLqpoRN2JZzYecssmBzsQ1mpjCcaLzGmX3CxYNowP9lg2Kjg9vU7DtNHSbe3IRSgJ0mqWJDoTT9OS-0K8cCDX6CKFdB6KXD8s47Q9NuakNzZ_QCMF2jnAeUN_bduB1OTFXKOdxdRwXNeiq3_1datEZBoXNzVpnR6au6ufE6KIG0xkxdGlTi8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلافوئنته :
رودری بهترین بازیکن دنیاس، وقتی ازش انتقاد میکنن عصبی میشم، چون اون از تمام هافبک های اروپا بهتره اون حتی اگه 50% آمادگی جسمانی هم داشته باشه بازم جزو بهتریناس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/94450" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d969ad7b3.mp4?token=SJDKfFtB42ASULIdyJ4Xy9NvEuFssx42GZZhR-wFe5wFyIdMX5QJ7J3BeXNVdY2gZlTFALCX8CUkYwUl0s1oZYeU8bnNCs3aQCsVNL9_Zcdq9ovbsAzH_c6fQ9RXm4kfAp5Pkc6fgmhspW6ZszVqSv0kcdvq0VSXk6H3uow7YATBkAT-zXEDNcWh-CiTojWMcyQ_VOa_cTsUgdt4Afu-6OW2uxnMQC_uwFghk7nfI9wkhNmFpOIkjvA5TeafL05fhdPYKUVsYsHqD__diozkLUkF1DRYGh7xVX8M_BBqDSe86fzweyDFWf5sD-qtdlE0pO0cJkltpDiDcOgL3I_QAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d969ad7b3.mp4?token=SJDKfFtB42ASULIdyJ4Xy9NvEuFssx42GZZhR-wFe5wFyIdMX5QJ7J3BeXNVdY2gZlTFALCX8CUkYwUl0s1oZYeU8bnNCs3aQCsVNL9_Zcdq9ovbsAzH_c6fQ9RXm4kfAp5Pkc6fgmhspW6ZszVqSv0kcdvq0VSXk6H3uow7YATBkAT-zXEDNcWh-CiTojWMcyQ_VOa_cTsUgdt4Afu-6OW2uxnMQC_uwFghk7nfI9wkhNmFpOIkjvA5TeafL05fhdPYKUVsYsHqD__diozkLUkF1DRYGh7xVX8M_BBqDSe86fzweyDFWf5sD-qtdlE0pO0cJkltpDiDcOgL3I_QAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهمونای جام‌جهانی ابوطالب‌حسینی عالین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94449" target="_blank">📅 17:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94448" target="_blank">📅 17:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQOJmUN9uWxQpYrYwE0GMvN-EFY6SjSYW07bysfhcOlL77EsOBlhUPdM8-lz5KbAq0HJ0h8PkXSvTvs6dqtRwE1Dwd-ISu2RbWIWTUuJLHEzNU1-KVFk1jCgnnv3chIzAdbsDfq9h-eg7Jw6oX7KYsPZXTpfostnWUYV5YeP1dTSIb257sTiE-chERJnLGWj31vJaMzJy9ufNXOkZoBxeKixGx5tDS35XRCdbNMdhgAFHa453Q4vtvLrDGI1ca18UME2hIJOgj7LoFEXJQshe1vpX6oN0NcuZ5Vi7nh8_ll02kljHbz1iHkHMv1VQtIVa-Vq67GGPbqYYIrlDMSRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر ژائو نوس بعد هجوم هوادارای رونالدو به کامنت هاش، کامنت های پیجشو بست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/94447" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c99fa3193a.mp4?token=SyI-iX3ZzHcSsh6hw4vAFKeKdVeNKBx-xUCcfXmzRmAvsS2Wef-N8qoICB8GEeidPuIs_NdJ1fAULrS9jzx9n000GPdAes_hZ_OmZc1QA4v6q6weNRXwnHYcmpf5s2jbpfygpznlbR1jofeBKUru6umYPPybwz859WvAEC38qn8zCQ9_4DF01cgb9PMn_XH2XFqz3Zu6syBf8iC_N7eZaUFG0vukxbUaGkDVivUu__6gGTLE-Hg7r_f1Yk83AfWEFuIA_Gu9Dsuxe_jGiT6JrW0meoE7rKiNLVXiAtkh_AhOKR4HoPZiAywqjKLVx7hiTiZRbWV8okGWn0nEh8lwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c99fa3193a.mp4?token=SyI-iX3ZzHcSsh6hw4vAFKeKdVeNKBx-xUCcfXmzRmAvsS2Wef-N8qoICB8GEeidPuIs_NdJ1fAULrS9jzx9n000GPdAes_hZ_OmZc1QA4v6q6weNRXwnHYcmpf5s2jbpfygpznlbR1jofeBKUru6umYPPybwz859WvAEC38qn8zCQ9_4DF01cgb9PMn_XH2XFqz3Zu6syBf8iC_N7eZaUFG0vukxbUaGkDVivUu__6gGTLE-Hg7r_f1Yk83AfWEFuIA_Gu9Dsuxe_jGiT6JrW0meoE7rKiNLVXiAtkh_AhOKR4HoPZiAywqjKLVx7hiTiZRbWV8okGWn0nEh8lwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر فوتبالیش خوبه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94446" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcYh4b7wlSakAY8jTxGYtX05HKbXSlyZ-P7UwMjB9kdG0zo0nzxKfBhejRg8eE7XAbQ8JXNmZA5r1GQ9AR554-XG4FCUkIoAKpvub4cuHfdK5c8-RH_M52qA-6S5BcvDnbDiqWA2_NfAwDy4366v40kMB_VCnliNpbiMThGPlH8nCkKAXvj0AQUeek0FfAFw8bMDmy04l6TscTJM0eEpVwAI3x5kiJVO3oDKp2B5PWZRq1N5nYgJDTcDQop0i8rKCj-s_oT_-L-lGCl_Jx6kcwdZag1czWp2aFBP2yvNEG6pcTeHJ76OeLjqcNy9egqCSbk4fbtZSJmJuT6fpGTPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
ما جام جهانی را خواهیم برد [پرتغال]، چون بهترین تیم را داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/94444" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94443">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0dh-bdUHfmkVDoNrsDPx4fIE62GXNbgBl4pV99NJ5DNMFbt1FDKHXjyNTii2_-2w9WHP4wz8yHi_xd89WBmD9oPd3DCxMrXYGjzAxm0RGN4KB55D4gMdE5TznkiEZTanD33AR1Pe89bHZaYDKNsWFR74lSS7qnSqp_P3uAFhd_XkqOMxzNrD9AzPS5r2u09C_217CLGzn3tzM9Lbse3Xn59a-5VKP1s373wzbzaGvwKBm-7TqGnWGp2WPh9UKpDyz-5RWNkhw3tOaMNxIZDUdcLGHSdI-eI8-izYc0j4QCBeANyscFSXUOlFoF_PMZXldijT6p7sDwHE5Pstph5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94443" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94442">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c32ce413.mp4?token=UOMGhcy0SEOMPaKWrdbIauf3A-o5k_HsRwqtOkU9pyCosBujJFtEfjTMEPsLfdlPWAh85scDlbA3hL1LtwtkT6hFmsxOhKSjjwys8JjDmGXEOyatRyOgcb6cMSXZ77Tw0D-y6a9-mV236k9gHrKh6-1qhcmFEyv97n5_5s5GXZOwub1JvPhe3JAS70dHxqln-9m05Fr1bHZ6Y1n_sUhFYslVfTRwCKsAVpo3Z9vpDXl6wEWwabIybcIhM1Zv1HwN-ULWgNOadw-R7EwCJglwRh4y1KYA9xXXZGAkLavyKXdMx_pz0UjjOWe7rGaoKxEVv4C8gNRw2kLjgVhQ30i4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c32ce413.mp4?token=UOMGhcy0SEOMPaKWrdbIauf3A-o5k_HsRwqtOkU9pyCosBujJFtEfjTMEPsLfdlPWAh85scDlbA3hL1LtwtkT6hFmsxOhKSjjwys8JjDmGXEOyatRyOgcb6cMSXZ77Tw0D-y6a9-mV236k9gHrKh6-1qhcmFEyv97n5_5s5GXZOwub1JvPhe3JAS70dHxqln-9m05Fr1bHZ6Y1n_sUhFYslVfTRwCKsAVpo3Z9vpDXl6wEWwabIybcIhM1Zv1HwN-ULWgNOadw-R7EwCJglwRh4y1KYA9xXXZGAkLavyKXdMx_pz0UjjOWe7rGaoKxEVv4C8gNRw2kLjgVhQ30i4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خاطره حنیف عمران‌زاده از هتریک ایمون زاید و شکست مقابل پرسپولیس در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94442" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94441">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e669850176.mp4?token=PTwMJKKoQKnyyb2-ZtyQhZSi8T5chfgESLfQVGuDz3QkTWkdYRs5GJa2MEEAdsSfSk8YkfvdWRkSStw3iuhrIynq0qbLfC-N7XYVylf6kbH2hf9GUNGA_FvzK2cSUS7UkuC9N751AgHQBYTpgE-LdjzLLTSWMWhHqO6rg9_IaXyoWvNynX7_QB1xmoPwRn14cGL9qxWS-OTUbY028qgKRWk1B7SbWTDxGgmr5CSyeHiUR94rA6lj7IMjlwWMpnzOiZSNQGnuJbVapDieuBcUaw5dzVAOQh7H2Lo3CyyqDnLV0Yv9w9a84hSfANnfUPAdwfQrVIxfg-LO-M6xPm9hEbkCzchNyUSSmc4QDhlZhTXwzqNOqNFk86FdyMKAyEWPrmpqDuTgff-ZMDiIKWpB6pBLQ9NjgTV-aK2u8Zq0GbGrzdXEu--BvdEmM3zlLJDomw7KQ5SLsv_KafJm3WzB3_bTR-OKpjsC-rLQ2JBMcXH3d4q7PuFnWddDQrTVXjAyB_pG5VHb_sYF2I1eTnr35kBdpkYbzEaPCqM76JSzWzuCsg_I8BJldJwtUljaKN9jBG1rATnbVEFMKzDnnGaTgoKBZ7w0yiizGBaf-81fYQTf5cstbrlmBpGH_Il4otLMNK1Ci-ZWVQJ9K7nH758Ttw1LZ1Mq2oLVN5m_EnviVqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e669850176.mp4?token=PTwMJKKoQKnyyb2-ZtyQhZSi8T5chfgESLfQVGuDz3QkTWkdYRs5GJa2MEEAdsSfSk8YkfvdWRkSStw3iuhrIynq0qbLfC-N7XYVylf6kbH2hf9GUNGA_FvzK2cSUS7UkuC9N751AgHQBYTpgE-LdjzLLTSWMWhHqO6rg9_IaXyoWvNynX7_QB1xmoPwRn14cGL9qxWS-OTUbY028qgKRWk1B7SbWTDxGgmr5CSyeHiUR94rA6lj7IMjlwWMpnzOiZSNQGnuJbVapDieuBcUaw5dzVAOQh7H2Lo3CyyqDnLV0Yv9w9a84hSfANnfUPAdwfQrVIxfg-LO-M6xPm9hEbkCzchNyUSSmc4QDhlZhTXwzqNOqNFk86FdyMKAyEWPrmpqDuTgff-ZMDiIKWpB6pBLQ9NjgTV-aK2u8Zq0GbGrzdXEu--BvdEmM3zlLJDomw7KQ5SLsv_KafJm3WzB3_bTR-OKpjsC-rLQ2JBMcXH3d4q7PuFnWddDQrTVXjAyB_pG5VHb_sYF2I1eTnr35kBdpkYbzEaPCqM76JSzWzuCsg_I8BJldJwtUljaKN9jBG1rATnbVEFMKzDnnGaTgoKBZ7w0yiizGBaf-81fYQTf5cstbrlmBpGH_Il4otLMNK1Ci-ZWVQJ9K7nH758Ttw1LZ1Mq2oLVN5m_EnviVqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
▶️
پسردکتر حسابی در گفتگو با ابوطالب: منم میتونستم برم دختر بازی ولی ترجیح دادم راه پدرم رو برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94441" target="_blank">📅 16:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94440">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c43B5sVFoEFRmvrOgnlF9QtDIcWzTz6q9TPlC_eaF1jS334FAMSSOyupEGFMrWPFxYNn6oOeqFKdSdamKg5azX9OJd7eoS5k-qQm4pNT7HN5ezUoSlTqXFiiSZRttSqo5A8Dfrnw72iWhZskG5oUz7J26Ge4hWEUHOyzvSpLRB9x0Nku162xtoZEXo6qv9t6YSEYFhc3wFAOldf-F8dGd725NX5jsC-dQoxQqSVYJnnZ74mr_Az4GpaQrp0USIaessGRyvXDpdYyH-Z44Uuz2QBBC6TDH6dH0Dutm_aYmjbL-emIBYDcZBUTN-MVhtgggJWnNJ6fs9PfXL8epcNSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🎙
گاوی درباره انتقال کوکوریا به رئال مادرید:
خب... رئال مادرید اخیراً تغییرات زیادی در دفاع کناری‌هایش داده است! این نتیجه داشتن لامین یامال در بارسلوناست. یامال بهترین است و حالا آن‌ها کوکوریا را برای متوقف کردن لامین جذب کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94440" target="_blank">📅 16:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94439">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f110036c7.mp4?token=cAgpNmfm5A8vv_ku2fEiW5A5fo2bj98AFynts9acf_sk8tjZMgcgs_N2Ipfar8-N7z6CGXdqgwhX9cFID2SvF2ZgHZ5fJwiUzkURKTdERc9alyxfVKzC52REQ1ThYPIhykxDVHllaoVmiENX00I0R18E5ISZxUSoLbygEIaokpYU_pCJmgSEVKUuZ0zis3BI3dgTuJIHN4zbkB7ln15I6IvDWAxHKdV2dj9oXCdvEV6R6HsTCXv-gaIanws-cLdtrcTuLCYoTUK5gm-OIFmWOq861UhXolGhvpUFJM47FnyIFK8_3HzqCBTiET5C3ziYHFzxwmyikJIUZhOR2SLZVjsrKXKhm5FvE4_pmXEJHXZApRqqvErVRAtudSJzSJVCtQzba61u_qD0PumV55LMNEEBCDAx2ruYtxUrD3lgTuF1DLBIvGH-S0Lm2pQEJlJoXzRfw_eDcwMvc8KUjGH0VPWpZR8yUqO6-V78YF1Xn7kgB6H6lQNYUDPOPHkZ-NuS6dKwmXXtaMPEGWYAhFxuXhEgDl67i3fXJiPfMxM834WAezKenAxsY2VYLhJsPt0OAAK6_15kDn1WzieTucBZ0zdIANEJMQ2OSVfhdUG4dVI9Hn__pPZIhLgo7S_MeFRuQVsasU_wNaWK6iWfAtxxPLWV7jSVZOVT1iHEr8iBL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f110036c7.mp4?token=cAgpNmfm5A8vv_ku2fEiW5A5fo2bj98AFynts9acf_sk8tjZMgcgs_N2Ipfar8-N7z6CGXdqgwhX9cFID2SvF2ZgHZ5fJwiUzkURKTdERc9alyxfVKzC52REQ1ThYPIhykxDVHllaoVmiENX00I0R18E5ISZxUSoLbygEIaokpYU_pCJmgSEVKUuZ0zis3BI3dgTuJIHN4zbkB7ln15I6IvDWAxHKdV2dj9oXCdvEV6R6HsTCXv-gaIanws-cLdtrcTuLCYoTUK5gm-OIFmWOq861UhXolGhvpUFJM47FnyIFK8_3HzqCBTiET5C3ziYHFzxwmyikJIUZhOR2SLZVjsrKXKhm5FvE4_pmXEJHXZApRqqvErVRAtudSJzSJVCtQzba61u_qD0PumV55LMNEEBCDAx2ruYtxUrD3lgTuF1DLBIvGH-S0Lm2pQEJlJoXzRfw_eDcwMvc8KUjGH0VPWpZR8yUqO6-V78YF1Xn7kgB6H6lQNYUDPOPHkZ-NuS6dKwmXXtaMPEGWYAhFxuXhEgDl67i3fXJiPfMxM834WAezKenAxsY2VYLhJsPt0OAAK6_15kDn1WzieTucBZ0zdIANEJMQ2OSVfhdUG4dVI9Hn__pPZIhLgo7S_MeFRuQVsasU_wNaWK6iWfAtxxPLWV7jSVZOVT1iHEr8iBL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇦
🤣
این دختر ایرانی وسط بازی دیشب کانادا حوصلش سر رفته اومده رژ لبشو معرفی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94439" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94438">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwjZcQmhOLORFe_4Hngy57Kep_jLKmwiiTnenmtrpiGe9b-uW2m-elMhOdAyA4VAXfFLURI-tv7GSEum8DVcoL2vBxOC0M6DDv7R9qzWm9SboRmgly7sfw1emK1XS_bv_XrBUvLBMYJkudqc5YZN8xD7t9eAP6p2-LIOVP1bJ80THI-F89dWNXLzvVGJL8d9wD6_vRI6YIIzOcQk2ojVieMxF9O1j97RSiFEG8Mv1zQ3yUIQU7OViqZmB3otC-ncfBjvu3JLyngT0Rr4G7YechisltcKSbrHV0XXIFnhDUflvLGr0J-jp9urmAsnHq9lEmPbRY3B4Xqe-Vg0P7qBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دی مارتزیو:
رئال مادرید تصمیم به فروش نیکو پاز گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94438" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8535ae130a.mp4?token=PrMpyWUn9_auJ-up2ioXF3Xjdsi6uQHx5tgAHMXhzPW4_OETj3EAb9IQ0iTunEhXaWl9TfP8masrDjSn4WEU3UcqsoZ_Bh6JVTvyOhfVb-Pix0Ssw6vrOgRA7kzJ7YT9PeWxBU7dHmah4AZyZkCUxQapdyDT2eZLHvHXfNIvGER0FSKYaTt_2o0Y5Ly3uuQ5SnCXnyLQRVQ6yRFqFALcu6_HsWfZ5zqzujL-xDyr1P0b7eNeIJ_HFuiUSsG0jQWMHscXb7KR6qkHST_BHHEtlTlWlxiFOIfVbd15HWLaraBj4Nvtzo6C7TK9to_fw3QNbwuFORcRe4hjTMcjgAEYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8535ae130a.mp4?token=PrMpyWUn9_auJ-up2ioXF3Xjdsi6uQHx5tgAHMXhzPW4_OETj3EAb9IQ0iTunEhXaWl9TfP8masrDjSn4WEU3UcqsoZ_Bh6JVTvyOhfVb-Pix0Ssw6vrOgRA7kzJ7YT9PeWxBU7dHmah4AZyZkCUxQapdyDT2eZLHvHXfNIvGER0FSKYaTt_2o0Y5Ly3uuQ5SnCXnyLQRVQ6yRFqFALcu6_HsWfZ5zqzujL-xDyr1P0b7eNeIJ_HFuiUSsG0jQWMHscXb7KR6qkHST_BHHEtlTlWlxiFOIfVbd15HWLaraBj4Nvtzo6C7TK9to_fw3QNbwuFORcRe4hjTMcjgAEYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
سینه‌رو محکمممممم تر بززززن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94437" target="_blank">📅 16:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94436">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac99529467.mp4?token=FagTE00aFecrtgH4M5AX0m497_F9fTBy4SdnYIaeuZNcZr-vriNmAHVXKQzcmirF83-_1o_KJyqHEyxMdSRQx_k4s06xNOMyiUmJ9Xvwi9tv_5-mzPMGTMc_QgLFyc6lyCNRxzdnNT6hsA9Q9XeOAXnsNApFWAlU9JQR60J4sXPLDLRFzyyQXoUaqV-z2rfmsMwIXxYjq9k2tnGjSHoDhc0KF_jdfEoEBzNNXPmX0ETUi5-a9HvKK8GXpVZ55N43ajdE4k3Uw5qGMgjfyiptIqgvFZ4LUHSTbeSidl-09UZrruqo-gEucdPuli_odedeTBpXsh3uGtjAaCbW9rUk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac99529467.mp4?token=FagTE00aFecrtgH4M5AX0m497_F9fTBy4SdnYIaeuZNcZr-vriNmAHVXKQzcmirF83-_1o_KJyqHEyxMdSRQx_k4s06xNOMyiUmJ9Xvwi9tv_5-mzPMGTMc_QgLFyc6lyCNRxzdnNT6hsA9Q9XeOAXnsNApFWAlU9JQR60J4sXPLDLRFzyyQXoUaqV-z2rfmsMwIXxYjq9k2tnGjSHoDhc0KF_jdfEoEBzNNXPmX0ETUi5-a9HvKK8GXpVZ55N43ajdE4k3Uw5qGMgjfyiptIqgvFZ4LUHSTbeSidl-09UZrruqo-gEucdPuli_odedeTBpXsh3uGtjAaCbW9rUk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی صبرانه منتظر بازی بعدی مکزیک هستم دلیلش هم به خودم مربوطه :
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94436" target="_blank">📅 15:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94435">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stQ_l3kkJj0Y5jcfXObwSWWbQyLuYUr-lP9ug7n1AeUbk1tMXv4hgDVw1L3r2g1wPpEsYFyz-3ckrqmldLpgtWN2DkIlCCi-k4nwAvbZhfTQDulYqirFNgGewhtr8cgrTS71hBYYHmpRLcUp-FPb8E6chP7kj1Ai9b67GSyO5-obVsGpq2NTBeLuH7wtfljPjp0EO_mCRj7iCU9RlrTaesrkE2tvFQVQFF1Gyvtw5hHCHyuIeoAdOnTWY5vb3isjsiWupbt-4zhzl11PekptgDTuPVePC20h8XzZH-si0T6IiwDEv1I3SI4D2hvMK-GgMs0oZiKfHlkbS9qqaC0bOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
جشن صعود مکزیکی ها؛ پشمام از جمعیت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94435" target="_blank">📅 15:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94434">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d371de557.mp4?token=iuE3zFgJhaAVFEEg9_IuMis2zM-uqAjUn6mDBLAyLRkRD4Etkua3z-sfDvDPWigKssFK1SlTfOz2sdV099mZ-t9Hfghv0WXJVeNTV9nLOzq1-WWZub5YEWISJ_7_GRziHjzPN2vYvWO1GPIpbrIJwodM5eYXsexwbQhaH3WQJ03oaZ7k1mWx7nCSvgoi2RJ_CKcXmr3eosQXCJAeHjqTSNHnMOCg8fKJUefM4L4ZJM9qtGBW0CA2cQZQl4SNkh6PBRje8g5D22BUqXOZlXuHQnPrk8ZZhBKKO4iFBOfd_XX3DR9pv-5ec8_pXZ5FCEhVxNAgQ-uyj1HbfMsrbX-SPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d371de557.mp4?token=iuE3zFgJhaAVFEEg9_IuMis2zM-uqAjUn6mDBLAyLRkRD4Etkua3z-sfDvDPWigKssFK1SlTfOz2sdV099mZ-t9Hfghv0WXJVeNTV9nLOzq1-WWZub5YEWISJ_7_GRziHjzPN2vYvWO1GPIpbrIJwodM5eYXsexwbQhaH3WQJ03oaZ7k1mWx7nCSvgoi2RJ_CKcXmr3eosQXCJAeHjqTSNHnMOCg8fKJUefM4L4ZJM9qtGBW0CA2cQZQl4SNkh6PBRje8g5D22BUqXOZlXuHQnPrk8ZZhBKKO4iFBOfd_XX3DR9pv-5ec8_pXZ5FCEhVxNAgQ-uyj1HbfMsrbX-SPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
هوادار آرژانتین بعد درخشش مسی مقابل الجزایر؛ فتبارک الله احسن الخالقین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94434" target="_blank">📅 15:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94433">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaNBJRDgpLoGd_ST3pz_iez3l1ZVzxj5naEixotYv0zEQLL4a2BLEqT2ggegOdhFt1qbbuJfvcs4WjXRHTLhA6TN9hgTf2PymhNb736QAE_-o9On5nfAklhaoBxyZmLdC_sAxzGQU5llXUfeovgUUrHUKTrbKjrTiEEwVPXljcc0dqjG1F6v16Bet7IuD4BCXCmiO24H6Uy4QZQQCOK_7OF_F3t7_vHwatzzc_OIHodfTE4azcKUNc-2QHQqp9FKvjfurBMb7c0BTc7zjZa31zzuUpH5L2YpcIKkWOxE7shS-pHbC5Ek1JOzLoCNx3VfGQYVAlqeXkKLsyz_EwT2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پیرس مورگان:
اگه کریستیانو رونالدو هم همون خطایی رو انجام میداد که مسی انجام داد، قطعا اخراج می‌شد. برای همین میگم توی برخورد با مسی و رونالدو یه جور استاندارد دوگانه وجود داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94433" target="_blank">📅 15:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94432">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu0dAnDbJ6gj0ggslCM52gqi98YdWQJb4HcgQv-uG4wOi_sCDcIu29MAG-3KpeY2-ReWMbUhHWPjqY1voXKyDrFMCEiUeCO-ySno0bLrJWd2rBWqUwIpf6f2UR_0yzHx3PWFvrewh1x1N6HZdgYrMNNs7I-7W8O3B2ZiPeImzaevSPpcceL-7mj4VYdTrDhS4WMYBSvy08VI1kztEsUEwlpoLxuxsMTOH1HnHTmM24U3kq0wLMv4ik2-vDiXUSFHBOajFlRI1fHDLrHnYsUsKEbtuE2XYopdzGBMm47W15yFYKohn56BUQ3rIvGGTOnMsig02uRvEe0SNOHA9hvYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
رومانو:
🔵
🔺
منچستر سیتی رسماً با جرمی دوکو برای تمدید قرارداد پنج ساله‌اش به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94432" target="_blank">📅 15:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94431">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMSoGG7lPgpGun8-54f65CAPFJyQKBKwIVvtoV_X2Qfy4xPLFmaEa7QxDZHx19_9l4H_6XF7Ln6IGvnYr0p8fSTCqszBq2P45epvvkihtnn-3lMrP4xXMO0e5uRsG-qpMYH3A0cnsPyDvtteQ5VIiOQucwb44-GBu_6kyDKehYOfFftKEve8lQEMi6O_pyZ0IpeQOgjPnRNTWt2Aug07HjYGnSqm2L8Cdp7K3jrE8xl4MwIxWfLhCF9Ga6ejKYGzoeyl8v_40IhTLUJbCn62k43a2SCTfjATtpEkE_xxNU2vMClIFPjqmcUZG1tOaVEfjaKX3mWU2PDvpg8Rzq_vjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
#فوریییییی
از فلیکس دیاز:
🔺
پاری سن ژرمن در رقابت با رئال مادرید برای جذب مایکل اولیسه پیشتاز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94431" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94430">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd3fc84dd.mp4?token=Vl1hiwuw1b9DM_N8mFSWys5fsN3mS1yXddvVsvAjN7l1DZm8JmMlYtNhDx5dooE9VXNsI5aotLVSTTsOBd-XG5kJj63SePbXCANOhyFp8em9P5ZXAqfFPaO2_758IiW1uTWg9S2h8T0hSfWAVhgFZbHEScwXxQmd0XCc6G1QoHhiwWqC87uNwhttbVsId1WQqpu4beKSA94DCQJxngGbtn3HzugiDndClLwOlcauhUAiS0klROz91Pue1DLV4Ncf94SLIT76JBMPskZMy2VSQLYSOo8sYQ9MNOBPaNhNmLA6XzrNXdHYm4hTp5jK3uweBCqogvrxCugmAKidnUUdLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd3fc84dd.mp4?token=Vl1hiwuw1b9DM_N8mFSWys5fsN3mS1yXddvVsvAjN7l1DZm8JmMlYtNhDx5dooE9VXNsI5aotLVSTTsOBd-XG5kJj63SePbXCANOhyFp8em9P5ZXAqfFPaO2_758IiW1uTWg9S2h8T0hSfWAVhgFZbHEScwXxQmd0XCc6G1QoHhiwWqC87uNwhttbVsId1WQqpu4beKSA94DCQJxngGbtn3HzugiDndClLwOlcauhUAiS0klROz91Pue1DLV4Ncf94SLIT76JBMPskZMy2VSQLYSOo8sYQ9MNOBPaNhNmLA6XzrNXdHYm4hTp5jK3uweBCqogvrxCugmAKidnUUdLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
پرده‌برداری آتیلا‌حجازی از بازی‌کردن مرحوم ناصر حجازی در لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94430" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2XFLmgiacRviocpPTDJhQiluJATj1Y9ECTnXZW3YsFsYz4eqMEqaevqRFyrlVxGn_dgfmUk5FR0FfthEv6NtbSp3qw2HgGSsofhJGRaBaKNhebHMDrmXy9_AArgd_76hnhmYXmYkYRi3_xQCM2B1zJgj8hjGlmhM7evwL3FdFQWB8F1fiQ39wczXEASRaqbSXaLkGCl5WCHHebe8W8lpOr5D9q2azU-gvZ9aH5YKYddnp1AP7_ywtYLasNqqGcfatX_dWMkQn7wCzp5Evdf-BL2DY5YprEM2lT9IdFA5P_aRkiujN6hAVFY1_5vI-ojYk6F699zcxfcakV9waIieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گاوی: «هتریک مسی؟
چیز جدیدی نیست. مسی بهترین بازیکن تاریخه و من همیشه همینو میگم. واقعیت اینه که برای فهمیدنش اصلا لازم نیست خیلی فوتبال بلد باشی؛ خودش تو کل دورانش ثابت کرده کیه. چه هتریک کنه، چه ببازه چه ببره، همیشه نشون داده واقعا بهترینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94429" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c3b02c2e.mp4?token=Qdui06OW4fbtTZT5gBXxG-xvljxjypnO02Tj5ONeeQ6cRZDUjqLwtCo4cHnd4QkwdNLlJk1brGl8TMOf4wa7mdiDb3Z-FLRPB5mn8fYCId9mtW3KlGrr5XJ1qu1OHillwQtg-VAAd4DqQRfVl0MPyc3tLlpn2dhvTptSYFgYoq49NLoiiu565T4x47d79s23ZFPo24Ll6QjC6FE4XD4hEeAvXpUnzruEwuCHpgmRdN0A2WiZTk4WeJUIjvUOJZiiytvM15LPFhGozteB4x44j2yMaH9IEHU51C0siVcYo-NiE7szddgqacaPlT3POXBoBhj6qHIyKSnleMtNq7OxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c3b02c2e.mp4?token=Qdui06OW4fbtTZT5gBXxG-xvljxjypnO02Tj5ONeeQ6cRZDUjqLwtCo4cHnd4QkwdNLlJk1brGl8TMOf4wa7mdiDb3Z-FLRPB5mn8fYCId9mtW3KlGrr5XJ1qu1OHillwQtg-VAAd4DqQRfVl0MPyc3tLlpn2dhvTptSYFgYoq49NLoiiu565T4x47d79s23ZFPo24Ll6QjC6FE4XD4hEeAvXpUnzruEwuCHpgmRdN0A2WiZTk4WeJUIjvUOJZiiytvM15LPFhGozteB4x44j2yMaH9IEHU51C0siVcYo-NiE7szddgqacaPlT3POXBoBhj6qHIyKSnleMtNq7OxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انتقادات تند مجتبی پوربخش از مهدی‌ طارمی بدلیل مواضعش پس از بازی با نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94428" target="_blank">📅 15:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94426">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEToepy0zFjv1jldJWzR7u2DV3Ggw8PL4L_nbRTNPdyDQviDTzbf_mql4Tl7povuoCead4-abpzT-79MtqKevTqzGm2bDxoFpWSlwiakPbwoEwvye0moRVYFOWGc-E5aQsyHR8558JsHN0eUDwovRMqi3wRTbOP4cqKyCcFPvKBL5u82LVskVDmIQI96zpYFpmHTDm-W-IvLks7PHpFlLeKqFeI9YB8TZOGLmSPJS7YUN65HjTTiO85REFMQL5g3YmoJC7cradpKkcYwNVwJ4rfFDgGrUqejMLy3LHLzboMN_kX2aVRbcERVapTIdnEm-RJLy3usfUoRF2d668woog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7jRJBrTljKq9TKSGXxPioNCjQVK_DS6siwrobK0SJNGppiDkPUGc3eJD89cB7LZxgPyhUO6Ug43bp3-QgBZga7J-LE8Dd2prZejfOS0u3KpSvnvUyup2bACANSnk6zQNpyAx09k4FzjJGaxZ3SXpyR_AGIiGHfj80H1TZMtr8F38I_LjMB6ilwZNRKpgIZP-azRt1u62BlMGIZ7LfOi-c0C8TkgykzERdHsBxTr9u2vApOIkk__4G6IeDZjrRc74jOnXbux09gMTGeRDs50H_JmO7AyZqhTHa3pYKn_m-TdkKmeAbu3zqeYnw8T1WIshn0cpoY7RquDmPjhtK-QRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
خواهر کریستیانو رونالدو با لایک کردن یه پست علیه برونو فرناندز خبرساز شده؛ توی اون پست گفته شده بود برونو با اینکه بازیکن بااستعدادیه، اما توی بازی‌های بزرگ و لحظه‌های حساس اون تأثیری که ازش انتظار میره رو نداره و وقتی تیم به رهبر نیاز داره، کمتر خودش رو…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94426" target="_blank">📅 14:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94425">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiI9RUFFbQskjkcOEUUjjIs5jKvZ5n4CWoREY51xw0a9Of3jEy6m5URSktprJCCmBs315iry7_mF5wzoXfLrMLUEdStIklkkzgF673vysrINdmJV7TwZ4sGJFkJ7tvyAhSmxEgA5lbt6p7A4RpU3di1P98mXqbngCuvZOEHvBvtIArOcxJ6ssQvt-aV9InuXxuExDPS6f0xnOzuZE-qKz5Iw4eaT8dDJZCVmdnu4Ws_fx6UEPfma4T-QsZUW_FB0KvqLlYawvkq7zDCJ9DDKTRTQSb1NKqydgMSCixelLXQr9o_CM1vuZyXZeIzBN_831v6Cuk1GlYlAmQ5Dtu-LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🚨
جنجال تو اردوی اسپانیا
😀
داستان اینجوری شده که بورخا ایگلسیاس میخواسته وارد کمپ تیم ملی بشه ولی مامورای امنیتی آمریکا راهش ندادن! هرچی گفته «من بازیکن تیم ملی‌ام» کسی جدی نگرفته، ازش اسم و کارت خواستن، اسمشو گفته بورخا ایگلسیاس، اونا هم نگاه کردن گفتن «کیه این؟» آخرش هم یکی از کنار خندیده گفته اصلا نشناختنش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94425" target="_blank">📅 14:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94424">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eQXC5o-U2J2gO-fvE8ca3COuKWNh0199cU_mplXT2S14SCiJaMP5JO5YTP4jBQg63FHe3xD-E6RytCr-e_N7MoXp5rv2SGLfXc6PlxIry5ogx14A6u55gQ2h9K-UVAuI8GFX4lBAIHzsZFRaBbWOidc6YjKIveAVMp4D8Aj-WtQliCFq2x7VA7EHKhhYxmAyRCRDwq0qCciU-7nyHUVU43MHWelnUQ81cPkzrkgRKjtdcGG5GEsf4Lye4X3-_9ke8rW2SC7eQmmw9j8JNFoA55KuUJ1GM1hJncv-fb08RkmjtzrKs5YZ1xHXlD5KJjzgjiRNYMb-ebW8LqETCicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
اگه لیونل مسی مقابل اتریش گلزنی کنه، به اولین بازیکن قرن ۲۱ تبدیل میشه که در ۶ بازی پیاپی جام جهانی موفق به گلزنی شده؛ یک رکورد تاریخی دیگه که میتونه به نام اسطوره آرژانتینی ثبت بشه.
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94424" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94423">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94423" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEcFIWGnyAL_aainzETtPcHHjBSCfFgFjJsjgf-NzCP4QOTA1kDuc73mHZxXO_uxcmyxk3xuqNY6reR99WxJR9eAwyAHfEwKj1X766lEjbS5cLj2mQsuKe9CUi4wT_tEnw1SvlFgMc76Mia2JRWKn3JvUaye9jkdBUnn0vQfsmpdb4VP76dScScFOmEJnFosZ0DqYWwRIm1fK3eH9szhgHxKbw23WqWRlHtFlXNF4K-HT8z87-JjhwQomrLy_53knbhSYh4EsWxU3_wEOdsKuCS2_ISjifOuYcrT3OQVGW0JQR8WzdRMC6bMLzraSyLAgiTcRgKwZmU1laoIyo7aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94422" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3d48b39d.mp4?token=qtM-2Fhas587llHFrgT2_p8pA9_tV2iSA6SjrNb1_wMHP9cXRjMPDUfE9IABnkb-pvsndO3HpzCLj-cLMn6-32sWPywstm7OgULjDio7a_X6yribI_fAPtVQ6mdhLdcjHw4w1GGbbskdSK26aFYDHLiwt6Dz-g_uhcpJ9JGrUDulbANbozwpQgUc4XK8vqknBozyTzkh0eevycxC0iITbGCtdmkODq6JGxlBAAJI_gXf1bKEZiHk5NTde3pUVQHOJDisxL1h0CqLwgszwGFYLYK66EbmOZHRASocM056ImBEJc-jilmZN8d458byMVZs1a-ErPdw-JqBv915Lg_2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3d48b39d.mp4?token=qtM-2Fhas587llHFrgT2_p8pA9_tV2iSA6SjrNb1_wMHP9cXRjMPDUfE9IABnkb-pvsndO3HpzCLj-cLMn6-32sWPywstm7OgULjDio7a_X6yribI_fAPtVQ6mdhLdcjHw4w1GGbbskdSK26aFYDHLiwt6Dz-g_uhcpJ9JGrUDulbANbozwpQgUc4XK8vqknBozyTzkh0eevycxC0iITbGCtdmkODq6JGxlBAAJI_gXf1bKEZiHk5NTde3pUVQHOJDisxL1h0CqLwgszwGFYLYK66EbmOZHRASocM056ImBEJc-jilmZN8d458byMVZs1a-ErPdw-JqBv915Lg_2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خارجی اومده موزیک‌های کشور نیوزیلند رو با ایران مقایسه کرده که در آخر ببینید واکنشش چیه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94421" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f31df64f.mp4?token=IBzA8Lr5fBVRVMzAijS8ec-_nTOtecu8yjtu8gxti3MqMW5UhCBQTf0aBEIdI_ikeObbxEfxjaqdjirjO4Q_d5HmZZ8BoTTMep0-3p6FLKHIBLrrb0PlLV6i3_QaRmkkTpRVmQTeOtCQGZgVk6J5oNRUq0Ie5XsKrS7ATK8esV4CWmscZrkJokXD1jdQTc7hc6AID3Jr2GfXOOwFe0IJ_Q34XPYvKVTOEwLrfLrh44RiMuhLuvA3vcwupNBZyZRRw5FxQlcij3LNiQ1TNovqX5J_CYe8zyg8nS3wgzcOUxXyll8UMORPKv7uq819voQ4MgSmxzig3RybjFjxnV1lJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f31df64f.mp4?token=IBzA8Lr5fBVRVMzAijS8ec-_nTOtecu8yjtu8gxti3MqMW5UhCBQTf0aBEIdI_ikeObbxEfxjaqdjirjO4Q_d5HmZZ8BoTTMep0-3p6FLKHIBLrrb0PlLV6i3_QaRmkkTpRVmQTeOtCQGZgVk6J5oNRUq0Ie5XsKrS7ATK8esV4CWmscZrkJokXD1jdQTc7hc6AID3Jr2GfXOOwFe0IJ_Q34XPYvKVTOEwLrfLrh44RiMuhLuvA3vcwupNBZyZRRw5FxQlcij3LNiQ1TNovqX5J_CYe8zyg8nS3wgzcOUxXyll8UMORPKv7uq819voQ4MgSmxzig3RybjFjxnV1lJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن فیل فودن به لیلی فیلیپس (پورن استار) میگه نزدیک شوهرم نیا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94420" target="_blank">📅 14:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1661c1c04c.mp4?token=d5TB7OT2i0uQO_1Zb245dE42EsUJDstro0qd9D5zzVTIQKumMY34xwzWrCVTT_A2r98q6rWB7pWSkuTV_h2g2dBT8LqMwrh_05_ynyfyQUfMVo34pjpLXjm5BjBUVjQH96hiztcGIT-GUFi1R7jIGzDdPZauPckxwHrJNF30z3olCKbCHeRnmrV8gOSTVgwQ1gWut896Q74NyesQl3vZDoIdPKuOqxbDYSdA2mfvySYJ_QgiiD5G2zC3v5RI2qHZNkScEmivorokWMekXnUis9ZZWsABAQ_-lEeCG22xwkrORTqQKaXFM8EueNq0FIxMenIetYkaUH7WKMVtHekM3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1661c1c04c.mp4?token=d5TB7OT2i0uQO_1Zb245dE42EsUJDstro0qd9D5zzVTIQKumMY34xwzWrCVTT_A2r98q6rWB7pWSkuTV_h2g2dBT8LqMwrh_05_ynyfyQUfMVo34pjpLXjm5BjBUVjQH96hiztcGIT-GUFi1R7jIGzDdPZauPckxwHrJNF30z3olCKbCHeRnmrV8gOSTVgwQ1gWut896Q74NyesQl3vZDoIdPKuOqxbDYSdA2mfvySYJ_QgiiD5G2zC3v5RI2qHZNkScEmivorokWMekXnUis9ZZWsABAQ_-lEeCG22xwkrORTqQKaXFM8EueNq0FIxMenIetYkaUH7WKMVtHekM3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این تیکه رو قرار بود پخش نکنن؛ خاطره بامزه حنیف عمران‌زاده از هاشم بیک زاده
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94419" target="_blank">📅 14:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94418">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxZTwjYh6uVPFaqomURBUKsWpKgwUXVnovKNye3HCxqnC_69-E3k7erFSNTnJhjmL6t_OMju9-hLKLssivmDrxUy_JDDzowWrhjnEgN3KkQLakSibQqmMHU9Q-JtzYfbyy2q3_KgHu15tVjU_xGc_95dGgKRAJzpeWnNV-RuG-PodLKVS91-AnfjTgm7hyjzTExOAvzcpU_DWHy4QP09bdV_ThJazbC8eM0rflkoQz3OGdWbW8nuA6bij5vq_I90p-lvHAOrwj-au_N6SkD1OWQCw2D1_3sSEipst_Dg4wB2p9MwmIWEdHC7hOg3AqFOO9WsoqkVDbKMG2g2JZHxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری - اسکای اسپورت:
بارسلونا وضعیت میکی فن د فن را زیر نظر گرفته؛ مدافع تاتنهام هنوز قراردادش را تمدید نکرده و همین موضوع توجه مدیران بارسا را به خودش جلب کرده است.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94418" target="_blank">📅 14:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d15c801ab.mp4?token=WxM_p3OVy2IlUpL8ElwU9LlUToO4oYGHfeIiqdHQ4recdFkdLyTBB3kO34KD551pgT19XUhIdeWWfy8-2bmMU94rEXcf4jJg9VvMj7RjvGvrp7xcfzSXpWQQ6QKqlTaTh71HDbd190wYBnFrdG9vGUpS6VbdOdrgIB8vXgL8MA3yQ5cB-9duv1ofGhK0l09KlmxTOO3DC1qzBR9RyYfMGGiNu6on8Gv1Zouv4pE-CfMD3Q8PuWW9Xiq2EeFf4WRzvROyvK6AjrlqjfYvjRZ6PozPhXsanBKW074El-sbEcW8v2gvVUp4YFHlsSTNPWoJHZYhdGXQR8dTAFMc9kDk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d15c801ab.mp4?token=WxM_p3OVy2IlUpL8ElwU9LlUToO4oYGHfeIiqdHQ4recdFkdLyTBB3kO34KD551pgT19XUhIdeWWfy8-2bmMU94rEXcf4jJg9VvMj7RjvGvrp7xcfzSXpWQQ6QKqlTaTh71HDbd190wYBnFrdG9vGUpS6VbdOdrgIB8vXgL8MA3yQ5cB-9duv1ofGhK0l09KlmxTOO3DC1qzBR9RyYfMGGiNu6on8Gv1Zouv4pE-CfMD3Q8PuWW9Xiq2EeFf4WRzvROyvK6AjrlqjfYvjRZ6PozPhXsanBKW074El-sbEcW8v2gvVUp4YFHlsSTNPWoJHZYhdGXQR8dTAFMc9kDk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
همچنان از کراش‌زدن خارجیا روی تیم‌قلعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94417" target="_blank">📅 14:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcSqtiMxaOJNJw49Znvy0BU7Vb-5ESBVUmrGTRpulbIV21pMoH_5-htxW8zF9xiNvyiyDwiQ-1PfgdR4ZMhLyqsNKMvK0_jrMdpQah_tHL6troMB79VOpqe_iDHEWIxl05aqVO_phME1466hkXtaDJ8r1acxAb2Xi-PPDrmJSwSHx6EzCR0hPsN8M8vB0eZ0v-jMacjfHTYkMpNBP6wbfnHkl1f0Ru8qgvUdkOeQLCDTdJqmW-TB_g-Axz2bsqBGfB3BJFm90jCV7lLPMJWR0MdVdP6S9EYLGVh2dea0PphEIPchzDH4XM_VYQXJTSr-BRJ7_1cSMvdu55a-vMc6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوائو نوس: همه می‌دونیم کریستیانو رونالدو چه کارهای بزرگی برای پرتغال و دنیای فوتبال انجام داده، اما اینجا همه برابرن؛ کریستیانو هم مثل بقیه فقط یه بازیکنه که اومده به تیم کمک کنه و کنار ما برای موفقیت بجنگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94416" target="_blank">📅 13:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94415">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43da0169bd.mp4?token=mzUwWtkGd-bQ7z7MBJKXeRiSzNTPpG8doZr5OOqBplekOnoJx7eHwXf5WhKHGRUmizwi-xZIROrlJKs3EzA33DUQwOCwA79eMeQDladlINkPl9daImXKQf9BjoaCtRz_b6RpiGDJobwn7ITMQZb-k7w1zOQkNODy9s66dJqPF4r6yUp2ZKNBHpawSv_Ui2IhuXwwXIC3USnxr6W66fKGmXYh0GbXosZ8Xg85E_o16Lvqc5QO0jqWGwGqfOwYlFE2KT6puNch266veWwf0Y11HxY3VPwqnBew8tGrlqiVmUom-7_W9tvEs81i41H2GNWAoEyCqGPJkXEtQh9XdkQOI5G3U4ExnpMXQuJHU3bE3NVMyyW8pqJayeupiM0iRX8sBDF1TayAOZQNPNxaC1bFlWUZcBWNzBvsIi6i_anVa7ZvSH4dGkvRUfk_PfZMesJpWjFLR2PHwRsSBuqZnHAYIaxNBpyN0TS-bw3m-DEj2c78F3Z5GwkfpbhtQwyMqZHu4BpqAor1MkhORhPjCL9C6yYM8iWcT6ksx3rBO0GLDUWHw-Q7maVrsBzt2MY-P0_fnsQuDrHo3YGwS9gsmT9Hu9or0VmvpGBSAQLn9S6yOmSs1CFBvkGSnSF8pOXjwfisKdmU1GGQfNSgJxvmorDW3A0JsozDag3v92WhrcHPN6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43da0169bd.mp4?token=mzUwWtkGd-bQ7z7MBJKXeRiSzNTPpG8doZr5OOqBplekOnoJx7eHwXf5WhKHGRUmizwi-xZIROrlJKs3EzA33DUQwOCwA79eMeQDladlINkPl9daImXKQf9BjoaCtRz_b6RpiGDJobwn7ITMQZb-k7w1zOQkNODy9s66dJqPF4r6yUp2ZKNBHpawSv_Ui2IhuXwwXIC3USnxr6W66fKGmXYh0GbXosZ8Xg85E_o16Lvqc5QO0jqWGwGqfOwYlFE2KT6puNch266veWwf0Y11HxY3VPwqnBew8tGrlqiVmUom-7_W9tvEs81i41H2GNWAoEyCqGPJkXEtQh9XdkQOI5G3U4ExnpMXQuJHU3bE3NVMyyW8pqJayeupiM0iRX8sBDF1TayAOZQNPNxaC1bFlWUZcBWNzBvsIi6i_anVa7ZvSH4dGkvRUfk_PfZMesJpWjFLR2PHwRsSBuqZnHAYIaxNBpyN0TS-bw3m-DEj2c78F3Z5GwkfpbhtQwyMqZHu4BpqAor1MkhORhPjCL9C6yYM8iWcT6ksx3rBO0GLDUWHw-Q7maVrsBzt2MY-P0_fnsQuDrHo3YGwS9gsmT9Hu9or0VmvpGBSAQLn9S6yOmSs1CFBvkGSnSF8pOXjwfisKdmU1GGQfNSgJxvmorDW3A0JsozDag3v92WhrcHPN6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه حنیف عمران‌زاده از کتک خوردن مقابل بی‌آزار تهرانی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94415" target="_blank">📅 13:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5j18wQjC5xmg18uGka-I20lsriOWNONM467Au4bEKHHMxSpyaBtBPHj0og1_NupufsPzNxEkcxOoI9rzUd3hm2N-W59jlYu7CYW8Hz_XKHL5TjIVeTWwAbZt85EV4WHGbLO7338RXXvpkSt6j_jZKXVl60UqoBxiLnVNKoVUCKiJ5VXjq6sac9SY8vNqSc8p6XVmjoxjOoPEQnr-paKqvOthfC_5VErWAJL8Bh_MF8MhFH3BZ0XlGc6W0TEstOyh23zM2x_mi-g-I8D06gbMkaDv8BzY5WRDjmyj_25v-zQSj9QFCH0F3BHqw28xafu2BnDw8F5lM8uepKFja1GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سانسورچی از دستش در رفته یا اثرات توافقه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94414" target="_blank">📅 13:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2UbHP35a0l9hUPbsb58t00w1RNIeE-RXCeIaUsBSmxQWtNroCa6Am3Z1HKae2gg_5YRNiRxcVtRorE9eogMIrvlSaCGqTLU6qd1_HeJOssTUh0qxPvcnBLRrfAcC_QiUeGVP3cC8VT3J7leUTmpVDPwGszhcwKSgU0ej1YaxQl9MKTVPjnuu6dZaX9tbV0vMhIlP-2GiwnpH2WI1dUrwz1uvID468TrAwvMG3WyGNnppp9wAkxg0MC9qVUl1hQMe3NQIuYVW1qQ0tJVvzIDuFoWlRFuZr6ST7q1Zp9ijJmxJsHNRgn9Ts8q9_kF8mH9R4ECo8ZUrZwTnAxA91vOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
وضعیت فیلمبردار بازی امروز صبح کلمبیا که بعد تکل خشن خوسانوف اینجوری مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94413" target="_blank">📅 13:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75950a2c2d.mp4?token=IzIEeXlvL_M3u4RImEASH2y5Vb42R5OZS6oS1NDEQP1ivIqBt4F5jp3xJYOSQ2S2wyZ3kp9S1XMZ7Qkw2quWRh05QcvppRVRb-hUyEeVbTtUGddg-65Z3R8rHkeu_3h_IdwjboK5O936JcitZqsCNwhG6w52crFeEsWD_sEEioA3kMHqZx01VKThADfiwoSYbH_vmXcqOCCojsLRrCattpHm3nNJ1dHZjUWbmBNaQeXhiLlYbD4U_E2YgPYTuy4GTnyic4VFZANlZpQC44FwTgsF48jlE3CPOfyybewafYcCDA1F6Co_yAUNpW3YRpfwrg_nn9Wqva46dWDIPcR8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75950a2c2d.mp4?token=IzIEeXlvL_M3u4RImEASH2y5Vb42R5OZS6oS1NDEQP1ivIqBt4F5jp3xJYOSQ2S2wyZ3kp9S1XMZ7Qkw2quWRh05QcvppRVRb-hUyEeVbTtUGddg-65Z3R8rHkeu_3h_IdwjboK5O936JcitZqsCNwhG6w52crFeEsWD_sEEioA3kMHqZx01VKThADfiwoSYbH_vmXcqOCCojsLRrCattpHm3nNJ1dHZjUWbmBNaQeXhiLlYbD4U_E2YgPYTuy4GTnyic4VFZANlZpQC44FwTgsF48jlE3CPOfyybewafYcCDA1F6Co_yAUNpW3YRpfwrg_nn9Wqva46dWDIPcR8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیک نشون داد واقعا شایسته میزبانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94412" target="_blank">📅 13:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7728293bb.mp4?token=hE8rj5LB-6O1mpFXFVfMrku6U7K1cZfo9ksdZeg9lZ2kjq2kaEYwifhZg8L8_3k7x57w8w0JK0rubIOBKn-d0GRaRnH9AOXUywlx9oSdDBcSrwckzd4RK0v_qpOe16BJHEeSJjhd87F_NAOjml38MzLeznEiNlpQbNwbNQvxEJtEp4hhFRZ3gaMVB_KWNkmO52myvbtMTS2MQMUrxVuV9nitWHd1NH2vnwo6XJqrI4cFBVq-magT4__GNoP5t922I1d4xbC7oSaSiNrXZADAw__PyCvIV4DzA4N8d-A0I2Je2dItNDcrb22OGGJ31Gqvd6udqRSijcDuvlwP2EBjAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7728293bb.mp4?token=hE8rj5LB-6O1mpFXFVfMrku6U7K1cZfo9ksdZeg9lZ2kjq2kaEYwifhZg8L8_3k7x57w8w0JK0rubIOBKn-d0GRaRnH9AOXUywlx9oSdDBcSrwckzd4RK0v_qpOe16BJHEeSJjhd87F_NAOjml38MzLeznEiNlpQbNwbNQvxEJtEp4hhFRZ3gaMVB_KWNkmO52myvbtMTS2MQMUrxVuV9nitWHd1NH2vnwo6XJqrI4cFBVq-magT4__GNoP5t922I1d4xbC7oSaSiNrXZADAw__PyCvIV4DzA4N8d-A0I2Je2dItNDcrb22OGGJ31Gqvd6udqRSijcDuvlwP2EBjAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی بعد از اینکه در مقابل الجزایر تعویض شد، روی نیمکت جایی نبود، بنابراین تیاگو آلمادا جای خود را به مسی پیشنهاد داد.
مسی قبول نکرد و روی زمین نشست.
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94411" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04815885a.mp4?token=tj4xoNo9cWQRAd-NVJa0oJkac5AWqZ0JrEzm7NZR5m73yRxnMx_urkiKXHDtfFEpz6qvNbs_82ootCatO44WsPvmlexU-1vAngZ3H-2Nq6-anSsUBOZvbpV1N2TtiJNis5ns3Y0ZRcv7NYMCqEI81wfmWPdHE8-S33eugLbV833KmIMcsi5oqon_d8Pbdgl9GH_VtdMKc_eC4Eobka2dGbLCtIFQodVPEc2GVDSUNtgq3R_dUUjal-WAWBdohYewcups0iQNtVV7oKU1P38X5q425vi07o66H8d-DlSSlrHNbJWZQyFGfDck5EDbY-xw1teAhsSY9zoKGjsQcUJkrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04815885a.mp4?token=tj4xoNo9cWQRAd-NVJa0oJkac5AWqZ0JrEzm7NZR5m73yRxnMx_urkiKXHDtfFEpz6qvNbs_82ootCatO44WsPvmlexU-1vAngZ3H-2Nq6-anSsUBOZvbpV1N2TtiJNis5ns3Y0ZRcv7NYMCqEI81wfmWPdHE8-S33eugLbV833KmIMcsi5oqon_d8Pbdgl9GH_VtdMKc_eC4Eobka2dGbLCtIFQodVPEc2GVDSUNtgq3R_dUUjal-WAWBdohYewcups0iQNtVV7oKU1P38X5q425vi07o66H8d-DlSSlrHNbJWZQyFGfDck5EDbY-xw1teAhsSY9zoKGjsQcUJkrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
مامانا اینقدر سر به سر بچه‌ها نذارید :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94410" target="_blank">📅 13:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94408">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afe9b255b.mp4?token=aWhUVDPB-SuSCgarwJODfu7IODWcF6nIpfr8FdT8VbUUcRpw1flM1SvN9ZACeqTCqzrQIJ4OStuxzmjHjFjOzQ69NBxgt8-moWMNY1hxie40BMFaic__o0FE8YrsrxcTRt7nRrhY_q-qagmAs-jy3ts2AeMaQfDtGwjm66y3GOUjR6tnUxBYJ7Bm1XvrjWhq1G1gKcr2Snbf4xK_RxLjRrzlnNbhBNfDuCNerXdpMhrgIkSwtQU-tQ03KDY_wy2u2MJZjLS5u9h1tftncwAOBHQ02ELLokW0ORB8VEzlBE5aI3rxts2zbCy6oPAAEDwYuSZ-HMGY_yg-gcUFcE_gYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afe9b255b.mp4?token=aWhUVDPB-SuSCgarwJODfu7IODWcF6nIpfr8FdT8VbUUcRpw1flM1SvN9ZACeqTCqzrQIJ4OStuxzmjHjFjOzQ69NBxgt8-moWMNY1hxie40BMFaic__o0FE8YrsrxcTRt7nRrhY_q-qagmAs-jy3ts2AeMaQfDtGwjm66y3GOUjR6tnUxBYJ7Bm1XvrjWhq1G1gKcr2Snbf4xK_RxLjRrzlnNbhBNfDuCNerXdpMhrgIkSwtQU-tQ03KDY_wy2u2MJZjLS5u9h1tftncwAOBHQ02ELLokW0ORB8VEzlBE5aI3rxts2zbCy6oPAAEDwYuSZ-HMGY_yg-gcUFcE_gYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من بعد دیدن 28 بازی جام‌جهانی تو 7 روز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94408" target="_blank">📅 12:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUs1LYJP6janSbng6364oaScfaZ4KVqdEY2gFLcXyr62cKYExdeTJ-gm-1Ese-_bC5C8NpoW7AMMTrR3N9emIq031qpVUXWugTQkvbDOJCsJ2BD0rPcX5iTr5q5klUHS8aTss7QO397DBUByd_7uoxX5Yq7d3TUNtmLTmpMx838S-NX2FO1Hg-Ws3V2iNG7PRDCU0we_oGnyUfVZKLP3H23QuoWXGB5NJ3Xk-nptAg16w6-08PLBq6qnAC3KuAm9GG_V8zOotuiGm8d5FyRffyy5yH6TvGRhbAGCWQAiIgopsbaOf-SR0VW5shI3ukAfYR_kTR4RgXDvqyy8Vm-tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات ۲۰ تیم حاضر در پریمیرلیگ انگلیس فصل ۲۰۲۶/۲۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94407" target="_blank">📅 12:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9590a4f51.mp4?token=bwJtXEHA99tSSJncOMCYd90ggzt1Sn7LKXJTyOcpbHCqjLi_ppubTtzsSAjjRJIod77j-MLpXmFnI52hAyO2MySmZGbupif0X39lrfFh_Pi9m5J1bOe6R1FdsQXhRj7nX1RCcdQQdBHIWCkF4mi-VNUC11m1zLsv-Puc7DXLNBSIa7SjlH5cAJVjbtPefW6ASQJX8l4sn-0j9sW1aI1SK-9PVNapy2N0QieEdso-QxCbcMosCecQCyFJmoKnN8D9yvbYySReihNVdFCxbV6JSLKOBKcjT3Hmu7sYmcBV4ez400F8n-0hs02FWxR_Z1xbu1uyodx9fqzwqy6bbyBkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9590a4f51.mp4?token=bwJtXEHA99tSSJncOMCYd90ggzt1Sn7LKXJTyOcpbHCqjLi_ppubTtzsSAjjRJIod77j-MLpXmFnI52hAyO2MySmZGbupif0X39lrfFh_Pi9m5J1bOe6R1FdsQXhRj7nX1RCcdQQdBHIWCkF4mi-VNUC11m1zLsv-Puc7DXLNBSIa7SjlH5cAJVjbtPefW6ASQJX8l4sn-0j9sW1aI1SK-9PVNapy2N0QieEdso-QxCbcMosCecQCyFJmoKnN8D9yvbYySReihNVdFCxbV6JSLKOBKcjT3Hmu7sYmcBV4ez400F8n-0hs02FWxR_Z1xbu1uyodx9fqzwqy6bbyBkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94406" target="_blank">📅 12:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac52419b4c.mp4?token=qxGuuUrWnfCptnFzedWzM9kEugN8BU2t-eB2FLwwHg2ZXVcc4NnoERRPnChStXee2EpNuQh5P7iZV_ZGVSU5ZyeHTLDjRC7CbGC0k_DqIImdhSe3QsEWjoWHEksNQmGSd2y_fOGyao0jMLJab7Tlh0Hn97t5Oru-gJ5rcDfpu2MtQP3Ah2-6anUjON79UlKDIsSxbENcFpYrRXJSMOnNU8XCvK_oGLVoqhfXJYgILhsLWPyL9gPaiDvLuU4bpoTzB9jfIwQG3IUaraTfXPs_ghUPKRSZOomjMSD3aD0YT1OBcB6XuaA1FqW2IDnHgu1FCJmOwLzm3aTY9Bs9T3VHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac52419b4c.mp4?token=qxGuuUrWnfCptnFzedWzM9kEugN8BU2t-eB2FLwwHg2ZXVcc4NnoERRPnChStXee2EpNuQh5P7iZV_ZGVSU5ZyeHTLDjRC7CbGC0k_DqIImdhSe3QsEWjoWHEksNQmGSd2y_fOGyao0jMLJab7Tlh0Hn97t5Oru-gJ5rcDfpu2MtQP3Ah2-6anUjON79UlKDIsSxbENcFpYrRXJSMOnNU8XCvK_oGLVoqhfXJYgILhsLWPyL9gPaiDvLuU4bpoTzB9jfIwQG3IUaraTfXPs_ghUPKRSZOomjMSD3aD0YT1OBcB6XuaA1FqW2IDnHgu1FCJmOwLzm3aTY9Bs9T3VHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇲🇽
درک نمیکنم چرا خانومای مکزیکی موقع شادی گل ممه‌هاشون میندازن بیرون.‌ نمونش همین بازی دیشب با کره‌جنوبی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94405" target="_blank">📅 12:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94401">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdU8RzHZ5BCiNIFjVmVoGcWwYTQ6Z6f1CmjOxy5aP2nExKJvpgjfE1xt0lgM47vpMBHnvludIrbSYUhsg1hYxTEOJn3jua7n-OaiVkzTj5yleX7G8qUVUguYUuuRhQ7Z5_lQv7Prou9dtDisauX80uumc0I2smVW-6t9GN8XLdyF3SFL_8S_7--UWdVNXKqOGw_Q2hBBEfxvmLcMEsjTlSvz6DLfaVD91oQgjc4Cwtl_tT37Qqsgyaw9VFZgVu9B_CGHv7C6u61fxtFAzc2FwF08uvPIWNJxGQYp1NEhAthXn19TRMyh3AI8InAZ04EcW_VCxVsST0yb6QtKSqZSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBf1qmVKlI2mkC8LABdnzpeA8F1ik27CoFoCj2XAeXK5-t-y6jTzlrMmMynBC98pak5VXTIbC7cTQLi2bshZsRHZWCRZqt5tV8HR80_6A-IpU-OT06Py2ZryJCQ9HV9rsNZ6LQPN7cWQ-eHwFo9PS1GPgbl8ZItfNQvvC3EKyzfd6K45X5CbEk-L4X6vFJyfhaNPGixMIvQZh4tx9wfxQ71DTN4VUaKHQiEpG-8eSzy0GXth79zxReoklKwFxtnMiRg4pV7ca8UwQOP5eYc1YTVsyy8qSijpegKOxeEr8Lod6zxfuBX-87HMGa9ixzTEkgXrRuo0xGIyNCX3tiSuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXQAn-8m9Mq1-e3h83971QGCRHiAS-Gt2jkPWIbNvuVG5tae8503zR_kg_U21sXzeufhD26fCUrU2AlmmTE_8DMAyi3o605nRTNncWwrzyXouxA6uZb52kXXdvwBklM2nlRmYBwlb4k1hilAHyjL1cZP7kiqBToaozH3rLeqgNDMHD9oJtoUX_k88hLArfB2WluqvU_ElLDVL7mFrwjDBKI6lCskGdQRCUhl-MCJMkt8XcTdBXVfxMA8lzqLDLiyq1niHtnZRJb2GEO_ufrW5uaGzlL7wOce5pKNG2_pgOn0fBLKX36Frkp-nZOlu_gdp1QStoqUgXbfInJLFvKh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb7-zawFBnH2kcg-c6xxVbJtfkUEt2pOyvKbjsUfB1rquegDyn0k84392loL2ij85jqAYg77KZEFkmfreWnmXp2WX3n5zeVMtUx0cQOnAsXaa9gENvNNBgRumz-sZHDzEpPpas05AAMZHSq4Md8JwQawwPrk58nh1mkSOBjNW58aecwiIH4DavZqiJ6cXP6jN0-rl13JrYd1ETn41ALjVNZMPc2Paeyz3ZouN-IYYrB5vkSAc9NYbd9tRo8MhDXT5erEf-Y_USfn6fCw63LQD3D1XpbPui11WOjRy5uvyJE4PSx9ucmW215UMY7FD9JaGHIclftJoUpeZcy1Z2J7rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات منچستریونایتد در فصل آینده رقابت‌های لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94401" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94400">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2l6Gl_Y5iiBBfTNaje6FOLudv_7tYCrO4jKaz_8wcJHqPrgfxW3KeFo8cuzeDxvfi0BX8Du1Gr0FZ0ucSRRgSsmJCWQUGOFS91pXVQS_t9d6D0J0M2hXjAb_WCGORZgIck-imJvZ7Mshy3prVTkbxZfyQoB-IzuslXCWlrFGnRl4VzrnD6K_hYYcyMYV8N4rMaNiLxalaPEEMn8eOb4-0NLJ8MVDjcedRoy-HS4ItWhXuSHC8qluLL7HXCmlZgfVX8wNjf51W-l-RdNXzgrJszaj_8suFUwxYi5i4A9rWcYN7DXFYIMFWNZEb79chkjrWVCJ_oaMwdO7bveCHudtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بعد دیدن 28 بازی جام‌جهانی تو 7 روز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94400" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cYKTFbAEehP7xlCUEDt1nLP1USxicnUwpYq8tWBeBZQZ4hGWOLGi9roaiRkcjxAKjgncP6MI-f0G6sputmYp5hOfRgTKtbVoPcDxeBqKXNIcbsAJuUAOCj5uU7to7vH6TzXYpED-8JXNU9_-hYh0nwUIC_pVkFTzBDJuapbYJX19wwowxjuHTaZfsCyuuIV-SJXHYHGFEA6zFstFJIj_eINpBlOFbVeHVNtI-5BCTvjwrKpqfUkoRXM27GrMfC_PT-yYd-pk6kBbN7baGdui8Z59hmgo2G9fjWUXdo2WJ9T50wm6A4WDalgyb-Nx-b8Q7_EHgR3Q-DIKP2KXhektcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bk6tYbQOLdGnRGA91TLFQF9KsHH5a2WRuz9rqxO0T8g-Q5Hs1TvkBQDsnXZIX3SBEiy968E-fUVKsA0kR0PHd8kQcZSn237Yhf5fTiZY6JNIhQ_BCp9F2lDSCOySyCFXR7mkCafSkAqFVmAIb-pU4gbKQ4yTgcY0v6TUDV0dkJ-7re-tYRyFn18xgq9koCTIuntbqWLWJRhpgCwFk-qG0bu5-tRjhn1fFRPJ-VtzN-G1jldEo-TyXBLzsfciLCRJPfZ9iwIU5FZc3IyclBYCcMgWSg6gG2CppkasrsecC7wnsHr7F3WeeceIcZZoSgJdOWaEItWCsmwbIYKxzI8CUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N3mk1Q2eOhl_p3pk2YVhyqsKJ3kqB-vMyQWoYouwvuaRPgDR2JmwxlSJCTps4KTgQ0idtSoccLiDmS8cnT0uIo1t8NwC_5kHKuJTkRgwadekyRWn7LfS7GpoJIkqk_q-i5rHggdrX2jFCXuTiDrayhE2yOaJRTTDtVyoZm8IwCowpGpAynWDq6cBPDRWQA4wonxVIfqPf5O5oYwQg3p8EuB8QwS7HCaaEij9lEE4jRS2w1AFKsRPdAGFNrII_vCzZXGoUCCkF1dXC_x8cWrmZZOA2jdUi83_dD7w3Fl2XMZnJ_veSznFX3RkG6OBY67unk1NQ18BTd3L9_n0CIk25Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
🇺🇸
پولشیچ ستاره آمریکا: برای شادی تک‌تک مردم خصوصا هواداران عزیزمون امشب باید استرالیا رو ببریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94397" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929aa4932e.mp4?token=j1cAGvNzx8WGCP7XnbtIu8YkAZEwgzag6GLd8CR-hcZCz8QYQ6XG8kM56YasByXc-OD_Y9RVhzLQzAf-1F8FPMGUFtFtw3I7yVByPF-guA21Od6y5ajyA5DFNx_lhAkyl0ictYrfSXu52vdiiDOyBLYyQsU91Si2Lf_Doq9kkP9oS_WdfiNVuBLZ5UnimlIiwuUfPTQkqaPil0myr1akiIAO9pz0YOcN3C1_bTV9K4s8_4ksumd3QhtakfIFXCNX-SoSZPsTRcdVTYDAUIN2agQpGfOkLNekUhWRkfrUy2rfqOp2e85nEEAT4y3KeWsi4nZ0qzIjf0uLtms7FU5R4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929aa4932e.mp4?token=j1cAGvNzx8WGCP7XnbtIu8YkAZEwgzag6GLd8CR-hcZCz8QYQ6XG8kM56YasByXc-OD_Y9RVhzLQzAf-1F8FPMGUFtFtw3I7yVByPF-guA21Od6y5ajyA5DFNx_lhAkyl0ictYrfSXu52vdiiDOyBLYyQsU91Si2Lf_Doq9kkP9oS_WdfiNVuBLZ5UnimlIiwuUfPTQkqaPil0myr1akiIAO9pz0YOcN3C1_bTV9K4s8_4ksumd3QhtakfIFXCNX-SoSZPsTRcdVTYDAUIN2agQpGfOkLNekUhWRkfrUy2rfqOp2e85nEEAT4y3KeWsi4nZ0qzIjf0uLtms7FU5R4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تعجب و ترس عادل فردوسی‌پور از تعداد سگ های مازیار: میگه ده تا سگ ژرمن دارم
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94396" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AphDZUzZM05Auivj0XfoDfKMkG8VlWVlDJEFdubIwFOukJGm8fJ_FtpiOK_fs64CTaqffLRGdRkzs_REFeTVykTfE0WIZhQMPN1xgk9uY55sUt1SCDZax1-WEmeVqfnZ7I8eVca3JSBOFqgChXnzx0XexVOA9tbFhfKnmHW6On0WHtjg21shDDFno24fCobp31JVUgSdYbSu6stByPAwNxtS7vM1aAskPQN9LIHV6qUEjvWoU4V5HmV-L1GbiN1H_jtEtCRCpNfzniInETuNdxfzRRkN666JE8FEDtOUMDOJxqk7ZeeGJIilvddHRNyhPHdzsAo3F4Ro3xbkoo4mPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
برنامه مسابقات هفته‌اول پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94395" target="_blank">📅 12:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW-6Lw3P5nNsJWwUWShCQLnI4aV07AgIV6qZcUi8TUWVVs7PP6rJ9B5Y-bblFFRk6m5WCzERJQK997VlSfLfWCclIRgRWKXxf-Tz9vzn2kju-xpIduo9J6cmxEoSipDRGh9RH_ytm1i-xCARfKBL-EAv_mzlii8BmNeRkGnxq7M55Fi2nanbsN_eFcCI5ShF4IZRK3UYgUmNc3Qo-qw-PUKgl5MMqudyFz4NUpqIeFjPsPYQXbPT-huZF4Mkz2_UzXnfYAAByU-jCoHfuNHXmrQPm7gtGX1DELGxK3VWSfkMd08QXp_R2aEAMvMWING1-SPK8JRromRuhsBohIo5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات منچستریونایتد در فصل آینده رقابت‌های لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94394" target="_blank">📅 12:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6e710942b.mp4?token=oywxxA-6dUgj8x6NtrJOejA6cVWME2ysAlICvXfmPltdmGk806px8pWyG7EBd7vl2733LjrcKpB6HJfauxCFu_Qwg1I9HMy3glbN8k5HnKt_0-hj38He0OuVr0BMBKGCG9g87ODwL4Ex463voHgqSR74rN8ufFsQ6ADU2ImyXnyDSS2q92aJ41yBUmElGDaPcyPeMbQuYVAodtfVecm4ZBPQPn68kSq3JrgYCpxPZMt04-xtiHnFClXksqqWQNTILL5dVlTKfa79jB16uPfAvYaI93hQR8tX6aUv63zOOpsA9S6umTEP_3jEdVv4FmYi_cAzOqv4GUB1zMDpaPR5sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6e710942b.mp4?token=oywxxA-6dUgj8x6NtrJOejA6cVWME2ysAlICvXfmPltdmGk806px8pWyG7EBd7vl2733LjrcKpB6HJfauxCFu_Qwg1I9HMy3glbN8k5HnKt_0-hj38He0OuVr0BMBKGCG9g87ODwL4Ex463voHgqSR74rN8ufFsQ6ADU2ImyXnyDSS2q92aJ41yBUmElGDaPcyPeMbQuYVAodtfVecm4ZBPQPn68kSq3JrgYCpxPZMt04-xtiHnFClXksqqWQNTILL5dVlTKfa79jB16uPfAvYaI93hQR8tX6aUv63zOOpsA9S6umTEP_3jEdVv4FmYi_cAzOqv4GUB1zMDpaPR5sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
روایت ابوطالب از ماجرای پیرزن و رونالدو؛ دیدی حتی یک پیرزن هم نیومد ببینه چه رقم آدمی هستی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94393" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14ba09e5b.mp4?token=qDFc9q46Rd91h2gY9Kl7Oo8LAxF8LsxQgua7lm4GFRt1IqL1z9YUpuIPyGxWSQpVimWxDJyTWDA9mUwMDPQLL55Z2PZdHRZ6iwAFrlJMgs9YGkys9oIuVq-kFxep-mBS2rON2Sopg3n6BrfKY0pMq8NQrwKdyqz_B8BYf8TLhSc4iP9bHazwUCTogU-Z9jf5FAS8yhnr2jfH8108th1V16q1ElZ97GeqquKxYRuAVXhK8MHUivwGLAPriZjnmbUsNrERSAmdtSu_K-ReUHZQj8GbmQ7etz3yU6WVWSWAE7fUyZoEmLutNVkqcKd68ZpQ7afr8Nsw4Pf7VTfpP_ytBAED8h-oXqYpVAPDk3tfFpXRmTVFrsdbyoWW-Tof2LeC0iL0B330CajKMDsl9sKKqyvfAo_1TULmEREdr2hi4FnHkrk3l3UqfAp_4NgBgESn4db3lnV2wZwsY45b_yKEazr7pd8U3RWlQQimne2EBsIg2-TCGybXf0U8GVeOFCJi1CCYkcRLF2ChakQN9tIjk0o3dr1M35U3-q8hMGPd9jOw2o13BTOwbSTypqj1r60IW9I4_SA8Tr5X5uhIsLSkmhZ4ev2FHV7k9bP4jiBIy9eyw6URs_koDWq52G4PU3rT3c3R0JqrOxyiG3Kv4DC7yHkm_EXsazbh1Q4-5wPOj10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14ba09e5b.mp4?token=qDFc9q46Rd91h2gY9Kl7Oo8LAxF8LsxQgua7lm4GFRt1IqL1z9YUpuIPyGxWSQpVimWxDJyTWDA9mUwMDPQLL55Z2PZdHRZ6iwAFrlJMgs9YGkys9oIuVq-kFxep-mBS2rON2Sopg3n6BrfKY0pMq8NQrwKdyqz_B8BYf8TLhSc4iP9bHazwUCTogU-Z9jf5FAS8yhnr2jfH8108th1V16q1ElZ97GeqquKxYRuAVXhK8MHUivwGLAPriZjnmbUsNrERSAmdtSu_K-ReUHZQj8GbmQ7etz3yU6WVWSWAE7fUyZoEmLutNVkqcKd68ZpQ7afr8Nsw4Pf7VTfpP_ytBAED8h-oXqYpVAPDk3tfFpXRmTVFrsdbyoWW-Tof2LeC0iL0B330CajKMDsl9sKKqyvfAo_1TULmEREdr2hi4FnHkrk3l3UqfAp_4NgBgESn4db3lnV2wZwsY45b_yKEazr7pd8U3RWlQQimne2EBsIg2-TCGybXf0U8GVeOFCJi1CCYkcRLF2ChakQN9tIjk0o3dr1M35U3-q8hMGPd9jOw2o13BTOwbSTypqj1r60IW9I4_SA8Tr5X5uhIsLSkmhZ4ev2FHV7k9bP4jiBIy9eyw6URs_koDWq52G4PU3rT3c3R0JqrOxyiG3Kv4DC7yHkm_EXsazbh1Q4-5wPOj10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
جوونای آفریقایی برای تیم قلعه‌نویی چالش رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94392" target="_blank">📅 12:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=W2XHC9ewBX4Fqi9haJys56KzeNk_Dq7rBaXDzePR_tRUOImOyeaZuNkxwOj1763G1YhaF_DKiqeAbdoXJGfLAfTn8dN6gL6FDbr4OGt_RsSxClWvsafZpBjyefSuCi-YmzlL8uFJMxYULoVsFo7R1Hxyddfdjs022oJcUK6qrLs0nCeoZov9wbmCx1snTgOlAQa9oU_4-UBK9OWzBep1hUnGyC3P4MiC_w7TSVAFIrMfrUC1fR0dr7abZoUzPckKwn1HuDshABHQI9LHLijQ_5yCSpBIYPbu6ZU0cVQ9rL9sEebeaV2EC_Uj0QFOiH14LTz3OVDX89iBoxpipUt-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=W2XHC9ewBX4Fqi9haJys56KzeNk_Dq7rBaXDzePR_tRUOImOyeaZuNkxwOj1763G1YhaF_DKiqeAbdoXJGfLAfTn8dN6gL6FDbr4OGt_RsSxClWvsafZpBjyefSuCi-YmzlL8uFJMxYULoVsFo7R1Hxyddfdjs022oJcUK6qrLs0nCeoZov9wbmCx1snTgOlAQa9oU_4-UBK9OWzBep1hUnGyC3P4MiC_w7TSVAFIrMfrUC1fR0dr7abZoUzPckKwn1HuDshABHQI9LHLijQ_5yCSpBIYPbu6ZU0cVQ9rL9sEebeaV2EC_Uj0QFOiH14LTz3OVDX89iBoxpipUt-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94391" target="_blank">📅 12:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول لیورپول:  • نیوکاسل یونایتد × لیورپول • لیورپول × ناتینگهام فارست • ایپسویچ تاون × لیورپول • لیورپول × فولهام • بورنموث × لیورپول • لیورپول × منچستر سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94390" target="_blank">📅 11:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۰ بازی اول منچستر یونایتد در لیگ برتر انگلستان فصل ۲۰۲۶/۲۷:  هال سیتی مقابل منچستر یونایتد منچستر یونایتد مقابل ایپسویچ تاون اورتون مقابل منچستر یونایتد منچستر یونایتد مقابل منچستر سیتی فولهام مقابل منچستر یونایتد منچستر یونایتد مقابل تاتنهام…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94389" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول آرسنال‌در فصل جدید پریمیرلیگ:  • کاونتری سیتی × آرسنال • آستون ویلا × آرسنال • آرسنال × چلسی • سندرلند × آرسنال • برایتون × آرسنال • آرسنال × لیدز یونایتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94388" target="_blank">📅 11:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول آرسنال‌در فصل جدید پریمیرلیگ:
• کاونتری سیتی × آرسنال
• آستون ویلا × آرسنال
• آرسنال × چلسی
• سندرلند × آرسنال
• برایتون × آرسنال
• آرسنال × لیدز یونایتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94387" target="_blank">📅 11:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff097f54b6.mp4?token=Js-ZmkNTriaZfnfaYNcxrLzo2aeFo6xYA0CbLscVjLH84GLt3UYArB99NerTQS46WBQffuLydM0_xWJI4uqT-daG3usacVTrfJy7rsbF2iAMaRwMCeL3teJ47_xqt1EV3OYCME8WoOFVTxWZcyWtdyZJZP64q3q4B1UPtg7RWV_s1Q5hcnrmQvnPbE_h1ZBFN4Njg3mJ90pR8Me8e5WcUyUhKChU5fnUDdiOCvfFSE-MC99tdBidvCoiwONZuSI-c8FcoXmCuZeEQAw3LTvEze1Wias-0Zgbu3-XIe25ct3Da2jpTQ-QWciTyqfPWmIRTWzS31RM6qoAL5J_2YjmqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff097f54b6.mp4?token=Js-ZmkNTriaZfnfaYNcxrLzo2aeFo6xYA0CbLscVjLH84GLt3UYArB99NerTQS46WBQffuLydM0_xWJI4uqT-daG3usacVTrfJy7rsbF2iAMaRwMCeL3teJ47_xqt1EV3OYCME8WoOFVTxWZcyWtdyZJZP64q3q4B1UPtg7RWV_s1Q5hcnrmQvnPbE_h1ZBFN4Njg3mJ90pR8Me8e5WcUyUhKChU5fnUDdiOCvfFSE-MC99tdBidvCoiwONZuSI-c8FcoXmCuZeEQAw3LTvEze1Wias-0Zgbu3-XIe25ct3Da2jpTQ-QWciTyqfPWmIRTWzS31RM6qoAL5J_2YjmqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
هوادار ایرانی حاضر در بازی مقابل نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94386" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGua4YJ3PA9ppItsaUM0oFKtFp5EpKelLuuY8kiQW8yCnr8vb49Ww3oVoXpvMN8P2ZVvI2cr1b91A_O1Oo8idvp2dzVFm2xAjN_7B_frZ0uqGgsbKaFkQaMeetv8jZao47SiWhJRYSnVo1QPd1UAvsv_XvZqwYkV-dyeewKO9tmXwMYNLeVGPgraupl59MbfAljAAPRN-IpMv2RhQE-KmEGeQpXiCSy5mR4h5MFZmKgb9o50T2gO9PFJA4LFXOyVFCpuf0eLe7T_PG1adVmRASuBxMGVNQDttRj--6PWj3wJB_jL-20ca_xKmn7ipgQ10zRAmS-oQw8ASUaYc2AP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد بازیکنای رئال تو هفته اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94385" target="_blank">📅 11:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r14hOOo9mJZ2-Kb9duQYRQhvo92V76SqB2GaTZCUe9sidij1dVKNDLNK5JgBaDS_Pov8WJUK1NE7JTEovOQRRLMNY3VXMJrGW4YK-9lVG5jUtkaQC67uSjNqfuAH4zKKufbzjFiLbjPnKjxN2TQyoXQlZhMWVWlIOKcRP5ixEcf22stZf8i38qYzLDxG2UUcXtyRm0enMq7_0P45H36q0YzkYvREeaROng0v_A0OXlfU6eIAd7X1W4RiVminqVdV8bx1_1n3mEEAP7Fjc9_BqJMp179G5zTKxGCy3SQ6JNv1SwauMtlgSmPZjkUCPMSFkTtF_D3bmUTfTf89OMhKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز ایرانی دست به کار شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94384" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94383">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6GXEe0hXGAncsQrakXUl3B4giYQnUNz7bO8XdmovQvP18ELWBAWcFBLg85Gjo7mJosLIshjoMQR_zYnlYA3S-IikPD-UODJCAIoVe10VJl5OV5ov_4ChstvLHyWNOceLUMCi3FSWjO5i_0b49B-QNawUldR3Adt9vks7GY3lG8w3GSQvDfXyn8HRGSBWqnUeVVUgyUYHukcUMAknU_3QyKYpjeyGZXpGwhsd5cRnnSU5kBokjGuzkHKE98FQIb0I0xQF-s0RW57Zai8YjWdAbB5yz9xK90sH-SGGV0hfggvFTze4xgo-uYDDjcvzErumreOESDKIRs3Hz98894ifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خواهر کریستیانو رونالدو با لایک کردن یه پست علیه برونو فرناندز خبرساز شده؛ توی اون پست گفته شده بود برونو با اینکه بازیکن بااستعدادیه، اما توی بازی‌های بزرگ و لحظه‌های حساس اون تأثیری که ازش انتظار میره رو نداره و وقتی تیم به رهبر نیاز داره، کمتر خودش رو نشون میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94383" target="_blank">📅 11:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94382">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366d6a6d70.mp4?token=HgLXAM0PYff6jlhRvYQuvXEldLUSwI0MA7-P2y-hNAYDXmV_NyHDnhBE17fHZWm8_p62VN5BxQiv3tQ4IgnlC7KnEe97xgca4k43ETPPA-5ZZYipPLx9NuXoHiTSZHqPmfZDuRNKlacceoWR05wHwYQpjQE_wyHr7aygXUaY76x17t7_YMvQmnWCj3xOtf7kYwo_F2LYsgZyFQfbPKcYWQTDyUfmP6omZAsFrPNdctAI-6abQbYSDLoKdDoOzMmzlx9AQUfSqQqXeyBn31aVfhy_SqbLVWPe93yTekjk1Oa_W9UJv7VOfOpoEHsmO_h68VIWQS3I31SOrUA0yWhilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366d6a6d70.mp4?token=HgLXAM0PYff6jlhRvYQuvXEldLUSwI0MA7-P2y-hNAYDXmV_NyHDnhBE17fHZWm8_p62VN5BxQiv3tQ4IgnlC7KnEe97xgca4k43ETPPA-5ZZYipPLx9NuXoHiTSZHqPmfZDuRNKlacceoWR05wHwYQpjQE_wyHr7aygXUaY76x17t7_YMvQmnWCj3xOtf7kYwo_F2LYsgZyFQfbPKcYWQTDyUfmP6omZAsFrPNdctAI-6abQbYSDLoKdDoOzMmzlx9AQUfSqQqXeyBn31aVfhy_SqbLVWPe93yTekjk1Oa_W9UJv7VOfOpoEHsmO_h68VIWQS3I31SOrUA0yWhilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحبت‌های بامزه ابوطالب از کراش‌زدن خارجیا روی رامین‌رضاییان و میلاد محمدی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94382" target="_blank">📅 11:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63043e76a0.mp4?token=ScfqQQctmOkZozb33bjXYzVsyKSAMXDZ9HV079LA53i5UOOuPfdGJp7Ls-EQzWvtZcKmc5ntYQhNPU2M9DpSMsdFcBHYRnmqxxBAdcOOyjQw0G8CnUedpvn5GP-2ou87drdcgcH30Ofa5xPFHnIOh_jbyV1Eqj6RQnjNM7503sC-zCv0mKVxcv4pWQSb95pWiysGleVWp1qEfxEBOQ-Se2ILyMTNs61zQYNAgWKQHB310F3Y6gJUcoO-Cyso_vywxekFdFQPLa7loipVbOl7eWtn6xkFNm3F6_wjtOgqittmiCoxyvbvxRL9cYfVx5v7Yjt-wSiEBQk8W4TSpKnNaw0AFrpqYeBX5MwJ4Bwu1WVnH0jtoUhraqCBCacq0bCgo9pH-w_CHheVgi4X_quQYMIsFmg9a86mrclU2P3WthTMCeWIc68RL6AmXHLtY_UMvStxqDCq4Noo3S8YqMXtii2U9oxPFj4y-E3iNoOSCofL-8t-ZnZ6SOiLjxNVvZb6bKhraHeIHnq23tF42gQ7f7xL21EQQ1gygk2ScVEOu8Re_j4e1EsuI9UqZHpogvuE3oDe_dzwjgYiO01yRxfd5avTytDaWCSYC5OLcYbq6arZyRhVnkwqBgUPXdKXIYeRZEYt9f1aq_pudKNOosrtA4dTAslzeAZQnwxX11ni0Bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63043e76a0.mp4?token=ScfqQQctmOkZozb33bjXYzVsyKSAMXDZ9HV079LA53i5UOOuPfdGJp7Ls-EQzWvtZcKmc5ntYQhNPU2M9DpSMsdFcBHYRnmqxxBAdcOOyjQw0G8CnUedpvn5GP-2ou87drdcgcH30Ofa5xPFHnIOh_jbyV1Eqj6RQnjNM7503sC-zCv0mKVxcv4pWQSb95pWiysGleVWp1qEfxEBOQ-Se2ILyMTNs61zQYNAgWKQHB310F3Y6gJUcoO-Cyso_vywxekFdFQPLa7loipVbOl7eWtn6xkFNm3F6_wjtOgqittmiCoxyvbvxRL9cYfVx5v7Yjt-wSiEBQk8W4TSpKnNaw0AFrpqYeBX5MwJ4Bwu1WVnH0jtoUhraqCBCacq0bCgo9pH-w_CHheVgi4X_quQYMIsFmg9a86mrclU2P3WthTMCeWIc68RL6AmXHLtY_UMvStxqDCq4Noo3S8YqMXtii2U9oxPFj4y-E3iNoOSCofL-8t-ZnZ6SOiLjxNVvZb6bKhraHeIHnq23tF42gQ7f7xL21EQQ1gygk2ScVEOu8Re_j4e1EsuI9UqZHpogvuE3oDe_dzwjgYiO01yRxfd5avTytDaWCSYC5OLcYbq6arZyRhVnkwqBgUPXdKXIYeRZEYt9f1aq_pudKNOosrtA4dTAslzeAZQnwxX11ni0Bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇧🇷
طرفدار ایرانی و خوشکل تیم‌‌ملی برزیل که آماده بازی مقابل هائیتی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94381" target="_blank">📅 11:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94380">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58d71cab5.mp4?token=jfdEKa4RmE42TzWPyxyfKKxCB2maHaqsCNTO4I9rSD3pbcQbyUk9-YGbjsV13LrB04eWjsrijxr4XumwEEzuqBrHMThGe5xsnUkBxkCmnLT7vYA8BNuruL0M894qsf3qQppuO7tp_xehKPDPRUUX14QWcFo0LHuAK35cK-1aYv6YVFwvyWIAzf9-3auIPuKGzFEj_o0NSJAQg4yuHEIMC4gI98u8k8s4m3H3vAEQ67wfzKVATYqV8mCtkOt1wzMdJPfwZQguer-bd3NH_K88Q7QKPiVuNTEosXJRAtMuK2h4P0G0aCTr2SRx96boF_GxkKV7kGevBt7IbL3axmFJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58d71cab5.mp4?token=jfdEKa4RmE42TzWPyxyfKKxCB2maHaqsCNTO4I9rSD3pbcQbyUk9-YGbjsV13LrB04eWjsrijxr4XumwEEzuqBrHMThGe5xsnUkBxkCmnLT7vYA8BNuruL0M894qsf3qQppuO7tp_xehKPDPRUUX14QWcFo0LHuAK35cK-1aYv6YVFwvyWIAzf9-3auIPuKGzFEj_o0NSJAQg4yuHEIMC4gI98u8k8s4m3H3vAEQ67wfzKVATYqV8mCtkOt1wzMdJPfwZQguer-bd3NH_K88Q7QKPiVuNTEosXJRAtMuK2h4P0G0aCTr2SRx96boF_GxkKV7kGevBt7IbL3axmFJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
جشن صعود مکزیکی ها؛ پشمام از جمعیت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94380" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08e2881e0.mp4?token=rmTiaSUrBbt6BEoJkcfz3hFYklYJ_h8jzqModPeb92dCRYTypn7DTaQ_dMwvXlQJTJn_-uJkAb28jy6PiHPU6XYTYJny-uADjPGRJf4F0_4uESAES7da1sEBvOX5CwcOX0q3T-eseyQYKKOZUc-pJrcjfygkmCPSECXpmQchuzuHezHVbfMSMl1kyZoUWlYtfiaaxPvLH4_5Y4TT68xNbPTxYHti2LQXcVcuuKj-ORe4gdKztAN_WRwMf6tGGsuCtpAnVxPiuEM-z-tCuFgE35kLZ-tl3H9SWML6dSSh6o8kEP5owK7DjecE2I9ScejFSQcURvqh5R9k81A4WghI_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08e2881e0.mp4?token=rmTiaSUrBbt6BEoJkcfz3hFYklYJ_h8jzqModPeb92dCRYTypn7DTaQ_dMwvXlQJTJn_-uJkAb28jy6PiHPU6XYTYJny-uADjPGRJf4F0_4uESAES7da1sEBvOX5CwcOX0q3T-eseyQYKKOZUc-pJrcjfygkmCPSECXpmQchuzuHezHVbfMSMl1kyZoUWlYtfiaaxPvLH4_5Y4TT68xNbPTxYHti2LQXcVcuuKj-ORe4gdKztAN_WRwMf6tGGsuCtpAnVxPiuEM-z-tCuFgE35kLZ-tl3H9SWML6dSSh6o8kEP5owK7DjecE2I9ScejFSQcURvqh5R9k81A4WghI_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇽
شادی هوادر مکزیکی از گلزنی به کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94378" target="_blank">📅 10:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0828ec8da.mp4?token=nliT8YL8JLsBai5ATK0pSTJtzYpPH2EH3f0Wze4hxKqo1NJt8CHDJjNdCSmMTSrZRybfbCKN9Qua-p_SJ756PtUoe7ZCSFNOVYYNwnq-pcI1hQPlGfjz_fqf6lNM6ArocKmyTDx0oUpkYEhQ57jprQIyQnyOgKEcOkPZDmX2VmHwP8NHf9DTQCFT7FNci_lnQyVqxQZkrxkaNMeq50NX27htoIt1MGG06EV0TRzyPoiehM5_Igt87gAL5zYyP0WChmkdkcdQFUF6hihe-7cZjCR2qZT2TkUYovA5jn4i58QwvMPSIiyv0Z_r6mNy26-J2yf_j3lK-Fvb3qzDXLK64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0828ec8da.mp4?token=nliT8YL8JLsBai5ATK0pSTJtzYpPH2EH3f0Wze4hxKqo1NJt8CHDJjNdCSmMTSrZRybfbCKN9Qua-p_SJ756PtUoe7ZCSFNOVYYNwnq-pcI1hQPlGfjz_fqf6lNM6ArocKmyTDx0oUpkYEhQ57jprQIyQnyOgKEcOkPZDmX2VmHwP8NHf9DTQCFT7FNci_lnQyVqxQZkrxkaNMeq50NX27htoIt1MGG06EV0TRzyPoiehM5_Igt87gAL5zYyP0WChmkdkcdQFUF6hihe-7cZjCR2qZT2TkUYovA5jn4i58QwvMPSIiyv0Z_r6mNy26-J2yf_j3lK-Fvb3qzDXLK64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇵🇹
آقای کریس‌رونالدو واقعا زشته دختران در و داف سرزمینمو ناراحت کنی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94377" target="_blank">📅 10:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7219246c5d.mp4?token=tQ4aJ7T4Osu1sPEj36ziuiISYFK9C9lrTNixwC0hFXPo0gVFVwZlCX15BSP4pbo7gCHfDcK-4HE8q6mdnafCgdMGk3uSS8O2oofAr_QwmHbJDmj1Jk9qQ7PnxPnUNJijE15oANjaDQQJ1ePdNIuAJvV5-JPJ5tz8iG6zMSBY2ASCkAiXCeyUxP6ArtfzPoHO-iE1urpAYDTApPMRkHOuCWGvaRdIxJ3Nx7u0vdwbsWZqubBW1wvqFKr1Jkw_Zvodu_yjk5xi25CP14WQEIQ1kYSDpVuiutLQZf6bu8uQgvntXrY3mwdurOx0TqwHTypQnzlC-AwH5pvB8dBIIjBpKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7219246c5d.mp4?token=tQ4aJ7T4Osu1sPEj36ziuiISYFK9C9lrTNixwC0hFXPo0gVFVwZlCX15BSP4pbo7gCHfDcK-4HE8q6mdnafCgdMGk3uSS8O2oofAr_QwmHbJDmj1Jk9qQ7PnxPnUNJijE15oANjaDQQJ1ePdNIuAJvV5-JPJ5tz8iG6zMSBY2ASCkAiXCeyUxP6ArtfzPoHO-iE1urpAYDTApPMRkHOuCWGvaRdIxJ3Nx7u0vdwbsWZqubBW1wvqFKr1Jkw_Zvodu_yjk5xi25CP14WQEIQ1kYSDpVuiutLQZf6bu8uQgvntXrY3mwdurOx0TqwHTypQnzlC-AwH5pvB8dBIIjBpKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
💥
هوادار ازبک‌که روی رامین‌رضاییان کراش زده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94376" target="_blank">📅 10:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51aa3adb3.mp4?token=ScMcAfVeIE_xAvYYp3oW1vtaKXXCdX4yFfRFhzkg8nSwFCu7Ejcm_AZGEZOmPt-ClBJR2LIKiStROf0Lzc3niDRc4x0mbduB6ClyttWhKUjPlTtcYqP6-_GH34YopZSnPxpCBx2N1-lkkIdfS0ScLLMj87BIWs-BWtreVKt4uyHndtRPKjbmPgRJ7OYn2EpKOMUnoYDvs3KjMiPpdWvTFUBzqfZycRIXIMeBzNsdXsR8R8-iHvS5SuEdWNeXSMcqE4a0KIAJ6nfLnE1NnA4ZrAIAxrNEEWogtEs61LUSM_jG9asbFtYR4rurQ0MRfFr_dihHsiZl8OLIlHZ7VJaTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51aa3adb3.mp4?token=ScMcAfVeIE_xAvYYp3oW1vtaKXXCdX4yFfRFhzkg8nSwFCu7Ejcm_AZGEZOmPt-ClBJR2LIKiStROf0Lzc3niDRc4x0mbduB6ClyttWhKUjPlTtcYqP6-_GH34YopZSnPxpCBx2N1-lkkIdfS0ScLLMj87BIWs-BWtreVKt4uyHndtRPKjbmPgRJ7OYn2EpKOMUnoYDvs3KjMiPpdWvTFUBzqfZycRIXIMeBzNsdXsR8R8-iHvS5SuEdWNeXSMcqE4a0KIAJ6nfLnE1NnA4ZrAIAxrNEEWogtEs61LUSM_jG9asbFtYR4rurQ0MRfFr_dihHsiZl8OLIlHZ7VJaTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
🇦🇷
همه را دیدم و مسی بهترین بود
آرزوی جالب خانمی ۱۰۴ ساله، که تک‌تک جام جهانی‌ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/94375" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9353083f2.mp4?token=VW5NEQPthz9kIV2euOORjqt_KVpvITXKrqrBC1GJpVbUYQ3ebl8xw-exijd-IoyHPTHerXpZpiaHKGNcD0i47nuM9T7zf5QLy3ndmTaocQ59sYESCq_1NV7yyGZE3mPvbV5hPqucP-w4_vOU6Vtdjfww_5udYThmL33Iy2TPZV9Nv03aHuixsmEIOiwtK1JFRkTzwFeTb7kR_S0xs94SN3PA33QLdkxETdxh6BaIS4lFuacxgfuIs-_jZZ8jSzD5w_aoufLBO-RYjQ_11fsgT-D8Yy6hPiAkXJHv6BZC5Jg2HiJeO0udBLq5isN531r3lHuM5oeqvuqZWOQlYCj3RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9353083f2.mp4?token=VW5NEQPthz9kIV2euOORjqt_KVpvITXKrqrBC1GJpVbUYQ3ebl8xw-exijd-IoyHPTHerXpZpiaHKGNcD0i47nuM9T7zf5QLy3ndmTaocQ59sYESCq_1NV7yyGZE3mPvbV5hPqucP-w4_vOU6Vtdjfww_5udYThmL33Iy2TPZV9Nv03aHuixsmEIOiwtK1JFRkTzwFeTb7kR_S0xs94SN3PA33QLdkxETdxh6BaIS4lFuacxgfuIs-_jZZ8jSzD5w_aoufLBO-RYjQ_11fsgT-D8Yy6hPiAkXJHv6BZC5Jg2HiJeO0udBLq5isN531r3lHuM5oeqvuqZWOQlYCj3RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وقتی فوت‌موب آلارم گل میده ولی صداوسیما دو دقیقه بعدش صحنه رو پخش میکنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94374" target="_blank">📅 09:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=Kj8jeyDJwzC5yFdimT9QaBzVh7P2O9vVfj-5A6MWmVZb73pOXP0bBpkSs5sV9UY_iT5CB7cLnHRmlNeHb-Cf9x2WMGEcp34Ud6jjugsLx4CgJM-61udiYbAJbS6D_hvwOUUehZj1A5uzkjbGPd6Yi4NkQXb4LTTPjMLNC8N9AjGWb_-3P7iToT7CCDf0FTyx3MC3YkLvZSHuiGv7TZ9yazuLA-i-nE-mVuurfwshd2il3neaUBpYs290ZgeC5YGITqnij_1M4F2RQlQEm-oLQ0I_f6sgkerakxeGvfriofCDaVai84Vjq0rrQTfUJOsoMhq5iaEAsJ4m7ZUIUywfGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=Kj8jeyDJwzC5yFdimT9QaBzVh7P2O9vVfj-5A6MWmVZb73pOXP0bBpkSs5sV9UY_iT5CB7cLnHRmlNeHb-Cf9x2WMGEcp34Ud6jjugsLx4CgJM-61udiYbAJbS6D_hvwOUUehZj1A5uzkjbGPd6Yi4NkQXb4LTTPjMLNC8N9AjGWb_-3P7iToT7CCDf0FTyx3MC3YkLvZSHuiGv7TZ9yazuLA-i-nE-mVuurfwshd2il3neaUBpYs290ZgeC5YGITqnij_1M4F2RQlQEm-oLQ0I_f6sgkerakxeGvfriofCDaVai84Vjq0rrQTfUJOsoMhq5iaEAsJ4m7ZUIUywfGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇳🇴
پارلمان نروژ تو جلسه دیروزش بابت برد کشورشون در جام‌جهانی اینجوری جشن گرفتن. خداوکیلی کشورو میبینی ارضا میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/94373" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94372">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=raEsuY-OAHxOdFciLL92DCKha-2CsK06_TKy99EIN5yBhGYBCME_FkW6S0Ba-_jYqIquWp5cnA4P3psLqMZvWwG6CcQYLGBRxPdapMKjs3KuFFqocVL_ykKMtzvFMKZWqKFpjLVna_jQESZIY9gpBDLYaVIr_9GTU3LHELSD8tjy4zr8O8demQ_zD-srzdHxm1N3xLiEQDaf_mQGz4-uEYvQDCnaDOQvP4szz1wd8AsBfrwygsbi0Vi68oLnzrOn454yK7IUS11_UKTVRgd7f3xXBrRMnudTkJ_G9ZuxzF8SvzuAmY0nJWY0OpvnUw46vrSdc8GO__WuZ7sDWNuROg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=raEsuY-OAHxOdFciLL92DCKha-2CsK06_TKy99EIN5yBhGYBCME_FkW6S0Ba-_jYqIquWp5cnA4P3psLqMZvWwG6CcQYLGBRxPdapMKjs3KuFFqocVL_ykKMtzvFMKZWqKFpjLVna_jQESZIY9gpBDLYaVIr_9GTU3LHELSD8tjy4zr8O8demQ_zD-srzdHxm1N3xLiEQDaf_mQGz4-uEYvQDCnaDOQvP4szz1wd8AsBfrwygsbi0Vi68oLnzrOn454yK7IUS11_UKTVRgd7f3xXBrRMnudTkJ_G9ZuxzF8SvzuAmY0nJWY0OpvnUw46vrSdc8GO__WuZ7sDWNuROg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
🇫🇷
دیکتاتور امباپه تو تمرین دیروز فرانسه رفته جای دشان نشسته و عملکرد بازیکنا رو میبینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94372" target="_blank">📅 08:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94371">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN8iie3X8phX4vjlEZX9Q5BL5nyy18FBVHPvP4PV0Og0lxgU74cfVrOMIzeoXOD7vZmGzYSBrKT83yRsSc7o57NL-UGTITXgH39dF_yAN_GQvgWP0JccDHCNMxfF2r3FVH0uRrhnutT7CHc5Sddx2AznC0dbX-dJXMol7KUG5NhgDZmGIF9knztS09rdqYNASDQR8xS9NUjFuIKk0qjbXaCoLyL9jx3LR2jthVwJ2QOhp4TWFgZ1J-dK5KiT1IdqfWfIYLoSDriQytOztVN5mv4kvp-ARSaI6lbJHxsJYHFll2rU80pdd7-4BGyfMdiW31ArRyicwKVoxQTnsKyBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇦
#فووووری؛ اسماعیل کونه بازیکن کانادا بدلیل شکستگی استخوان درشت نی و نازک نی حدود ۵ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/94371" target="_blank">📅 08:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94370">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/94370" target="_blank">📅 08:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94369">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8Fa4uIsMvdFHymvwKToRKDqHdWAiQA-JuCUEdQCHezQ5yX6FDHhalfWGP9Zb3BXu2pmJApIvKr58SgCLCkVXbOxLzjcgKlEqEKJkRo45gCgaRQSByCkppSWmy0aA_9C9F_bVTjIQqYD5e1QkC3EKX8mlV84G_S5dkOSf-Ms6iYhFSdwMPYrzQBC892d4Kc-6Ytriz3w92yPz4V6PMDc0lZ9rGN9EpsRGxjwhladPEpIVE-4V2pWRk_fRvCVf2a35zLS-EbnFBgapUJ9eKm-D1xin8Kmw4dgTAjgV05Gc4u0AdllPs831N9K3s9rJCGB9Fs8eevp5iCijYo-qLfM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لوئیز رومو بهترین بازیکن دیدار مکزیک و کره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/94369" target="_blank">📅 06:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDqv9A7TgKiDYhZTbRLsbsQyFTOGIKdCWNuLZvWHgRJTDT4xKDowAmhfn0SOyy-6yFkSSbx1oPgGTRQs9eG05xUuVYZcmDydV4ZkrsaNLcUWhM8IZ9Xmy6eekJIDubDW2ZgHebTE9joxFB_Yo8SRYiLiBVlbsc__J7f0WY8xnxG9V4S_CUxwxci8UBF8y0LROSPlE9dC01IC1eeokhpNtgLO4th4w8tq6Zyx87dgKDNs0BvVuzaoPj3eBf1BcTZa1O3cyvKEtN0j2ytY11MREg94b8S9Ppsa7FTk2wxr8KIbuC_bFpYDxmT8GujaUqjherfkIc3Y3a3O5ONB5lQ-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه A جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/94368" target="_blank">📅 06:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anZ4pNjC2332lKmAeLXQ14R5SsxSrsv-pjjXmgQ6rW6O9PX-KoWlDPfRWEaP7Be4HUBq7XPQMpgbZvIesh56btuQQuby2Xm5-EFHlKpkEZTm3XqbQPtCTvbpjk909lrLkxWZ2_wBbDDjfxbhi9taqyh1lCh-1qYyknUFJnh3nGhvuRrE76AGJvlivtT-NyLM03pH7hvmyJIjnCD612PI59EB455p9Wf5bSfyDASWZoPjdo8IAhd_5K1nLc2eItYQD2ERfVngfZCw0fbIxbk64QEZ9v_sOPLyiCxFNp4VwZeQIswNywy-A4cQ1qDnL9SCzcLYl_q9OXPUMIqwoz7n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94367" target="_blank">📅 06:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10d309995.mp4?token=FnuUhDvSw7yIsDOV-TUoxzUB3tqm-bk0E7TfOsJkum3tjTM5S22mS-xnxI0iZ2N2EL0V3_OD7dcsz9FlfMQlIPNDGzesugVNOJ54fPATYXqdirZBG07lbXiohmLuziPW98767k6oe4nwRzoCB0FkCyIshEomb6FFSpAKzR8pOz-OJOq5rrkEspsyG0vxCMPRcwM1LcFktfjAuq6q0ZTnWLb88b72aBMAdPvtBXYc5v5IGOg-3-w-A2UFbvs26XW-KW7BbnisXt3tZgoHSuUlFHGR93bYtcuyvrcNEyCJlYkxIQmU2o2vx7ANcAANBD8U7a92Q-egDLjput2MQZmFQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10d309995.mp4?token=FnuUhDvSw7yIsDOV-TUoxzUB3tqm-bk0E7TfOsJkum3tjTM5S22mS-xnxI0iZ2N2EL0V3_OD7dcsz9FlfMQlIPNDGzesugVNOJ54fPATYXqdirZBG07lbXiohmLuziPW98767k6oe4nwRzoCB0FkCyIshEomb6FFSpAKzR8pOz-OJOq5rrkEspsyG0vxCMPRcwM1LcFktfjAuq6q0ZTnWLb88b72aBMAdPvtBXYc5v5IGOg-3-w-A2UFbvs26XW-KW7BbnisXt3tZgoHSuUlFHGR93bYtcuyvrcNEyCJlYkxIQmU2o2vx7ANcAANBD8U7a92Q-egDLjput2MQZmFQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل مکزیک به کره‌جنوبی توسط لوئیس رومو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94366" target="_blank">📅 05:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94364">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلر کره رو
😂
😂
😂</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/94364" target="_blank">📅 05:41 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
