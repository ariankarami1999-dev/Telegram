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
<img src="https://cdn4.telesco.pe/file/J8vVpPyR41eYPnO-i8wts9AEHrQLWq7a9SYaqqNuprZnaFUiMrBFuZS0Qx9UHVuYumyMJuKMYO6QUqvEfKjJnwDCNrqi6V2g0AgC7rlyCpbsWTjSssnLCj6Ch8Dj2-gm96ZO7gBqDnOVX9QmBpd961EKqsdkSzXU7bmYnl6b0_DBC3PC7SZY_MflMkTondqF_YEUXRTNS95LuezNZaIoH9zJ9xv7z5fBU3S3QcbNdnL4o4GZikRd-u__VFJ7lEzYxLBIxJnW_PEvrRihBQB19HVC6QJ8wJ3Oc7MOI0EH9P3fk_bRZ6ChAAe8r3nNNbrFl43qMQsn6kjQJ-fIEr51dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 516K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yrBAVebsO32ndMFe80tCYWXCGPc2U6BC0kChJD6QTCqcYEByJs4uni5BocKZ8pO6Vk0kzoMuOhRCabeBB5YmwJ5AenqsjceTZQJ5wsRNh_98ueT8wqguYfLO1VIhFDoaVQocuHZ1UJHQkUhw2PgaD02j8kLxcHgGgJ60ij6xtLK6qYkTJNoTiUfLe66m0j863ChnMyEcOzEvDHyOzOOP360Ui21oFsBYQKMa5UB5pJm0bFCW5K3W8P5ViKGiZun_2OHoiKMDGlfZfPnrPXf39pychnQQf6ecgan-ZDuO5as7NWs8bNe-WpO8N7l7rRrGOlx9H2JmtJvlaHKKMclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yc6dRh31Y3krsF5MQO-9Mgfch0JJYNxbciCeyKW8m-HsqLDDOWULOSaGQupA0PikmhwDw6aSInTSQfNwThQRlfdX2npgVmqIEaUHosDDZYp-xsha3hj-LXY3KEEpq56bG3xPbjNrWMFEjW47xPb5ifqbGwC8rBI3EjG2WVF1QxbNp7f1IerfdKth1dcZS6KW6UhykdCvLgzt6-492y_XThik3ORee8lQwTwkM5QyL3DUCcA5IqEctgpiHv3InzdxJcjZif7OsUyX-KtoD-XVMxhx9Qc0PQiF8KBvnVnW96NFQqtoGH6uzXjJMKu2hE6PhbdOnl4-q27UpY17RLPkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTh_WuCPbBU31XY9iu0FGbTlZa0as6fxKELsH637mYlrSciXBgtDyaBJFdSlAoMmDq5MzMvMdNGjzLaLdVELepFfwtYjMqbMrKSlvEyL_VhJfkG4E-cJavHiFD_dwZUcm-PSCT5W9Ae3N56VnyrOkL8081ZNaFisZCaY3N36zd6g5kTybRoSunDjlBSYxrWxFballURpiSsoHqc9UTX3ipmYNbqxwKOF-SOm9ib6rg-UZ5qCzhjXz99l7NBd-S2RTEmHiInO_OfekugGcdc7A1lQbXOCcnbXrx9lmCRWWvPS5oRsN2fDV45pfrcThOD3fcX0Ejj5ZZtq0AejBL8mdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab3DKu2_WuxLe5wPgjZrDDuWemer4Xn2J96xdfAqwgyFdUxowpXd_IRFCDtAfM2wMnKZiUbHmQA98GFDJKugAoxXkb6lsJelQG8OlxTJZICJJXY0aqR8pNhPnTYY2ZhwW7i_D-m_aa-nHgzOy9__KyCFo5RVoB85EmMGUa_nrVwObUjP1Z_agIuRoqj69pvDwvSeYmWm5gSg0Il3fC4bwQ57cdBqjtSM-SHsmyV4F7kw5kYsYCDMyIj0dnU1wg65ZqORg8pjf3UNUkQb4rGsVGrpaHzQ6UDlLLb7g6hKZyzD_twNibq0lYgFjOyZTO7aZtbZGQqks7iugW1I8Z-7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=JojwUJWAM3snKmSJ-N-uGw2zideIY_y7bxaqSIHxzZ8dLaHGON0s_jnXa0vhacj8uVMYYRrDWsypCnQl8s3BJVLF4LmnpXBCoruGUr98-Lgu8wBXsRW3husGzW-7BJPXa6vAHPuHb3aRofmZZN58SgD1bYU4OUvmrI75xaIOCLmQACaB1JmcMXI2UckAYcVe7CpQaz6AroBqaYfXw7zTbCGDcmVwexNTOto4l-uLhjq6s0eFAmzG58Lle8FkYG6gEBfdvTmEtcd3x9e9XNybvPHjHlNiA8z5jKB4VEBeh9aZOfY8G6qyhZNwfUhOwlSWQqIKDdXyZU3Q8x4aOMrduQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=JojwUJWAM3snKmSJ-N-uGw2zideIY_y7bxaqSIHxzZ8dLaHGON0s_jnXa0vhacj8uVMYYRrDWsypCnQl8s3BJVLF4LmnpXBCoruGUr98-Lgu8wBXsRW3husGzW-7BJPXa6vAHPuHb3aRofmZZN58SgD1bYU4OUvmrI75xaIOCLmQACaB1JmcMXI2UckAYcVe7CpQaz6AroBqaYfXw7zTbCGDcmVwexNTOto4l-uLhjq6s0eFAmzG58Lle8FkYG6gEBfdvTmEtcd3x9e9XNybvPHjHlNiA8z5jKB4VEBeh9aZOfY8G6qyhZNwfUhOwlSWQqIKDdXyZU3Q8x4aOMrduQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtBsziVIpbddCG-RhIikNfKTNoG7Ss9qi3txe_CheoMefJ234vzPIzoQUzN4KYVJ0cR8T-3ldBNT7EqYGwxp52v--cbVl_QuK7zmP41AnrVQl8aqexv2v6x9DZ4cvJX3rC9MFSF6Qim8rbKHVCHU5U-0LcYh0O00NRRZjBhM_0x9yF-j3sG90ncnhVeBo9vzmZAvjkg6z7GT6JczpMMnkY4T_heD2f-QZf2WPCH9DF3iL8ukncYgWZHfe-XujSWGEHf9m0AE2wAcWZDUjOMVzzTI5tCN32exGEz_tIpUIrZTE-yMhVEj4fGxyicNffKque-HD0iO8euFv5G2UcG1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuaJNy3nGi_5sfJV5IJs1Rop-PHj00GgDIjf3PoAlZS8gSO3-1VXMIb96TlrApv70D9keJPeODDf5EjfcwpRyGhvZBFJ1qRZ9wmM1-vQw_wWYlXQXgiL3djJf_xbnpYpFljCrf4fgWl0V7Nrb5ck06Rn6Aq_MNK8Tg2hcxjXRFMVLaBnj1zJstdgyROX5MO8YGYlvfxsP6CcWCmAt8k4n6hBjSOg97YHASopfJ00KigQjtlrBDjb5rb78-OsuebT2hS1MS_Hoq6c1Qerp1DC8l8g7eWttHOCF5Y9muFpNzOfCQL5GHslQu6vEhs5HjXk6-BXzyjqeghHNV7TcTKnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگارباشگاه فنرباغچه هستن که معتقده کارتال باید درفنرباغچه‌بمونه و باید به او فرصت داد. باشگاه اون‌فردیکه بطری زده بود تو سر کارتال شناسایی کرد و از حضور در استادیوم در فصل جاری محروم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/29742" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2qRnSYRxSVZXFQMzVQHxdeYmq142mnRZZq1CRnMmDFAi14qBp0FM2f6J304ub6S6Jm8b4g_3yk4nVC_cjeEAnzf6-sBiMVqNJqE1iai31ENEQlJ4UptKKxPCrIrtziONYoRuyuFT7NOivrMYwfW3yF6zZKS1U5EjMzz1Bb3KVP5scYIVpcDtrPwQs8Hr3yF_xJFAR_L4thFed2x0kjI8-d2ktQ2au9B9EgDUkySqe1lew21dJC0e6ujcZQybskUzQsA59qvELENRJfpE8NJQZgJEPyCCxZz94csaMvlV6B0XXxPujahrRZpeHMWE7qjt6_8eL1rkhpSTUnzYYzBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/29741" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyrB8gMmetn_ee61WmZgv_AnyRnb4oEbDLEoRRJBc7vE0V4dCUYziyV6SyYvfmdNRMo8uDeGKpvyrE8YBnFJJ_kOlVtYIrrsHsrG7vDAD6Akrt-5edzDsSKgQXXYQM8PmtV4YpNuum-2IkCEGmULoAwsfpm9XB-MKNgNj6tRs3mxzbr2r3e9Dm9WmH1ZvHheb4GbVJo77syT9renT-3X5kktdCoC8SyYWi2-rWENhjiJhXzEsoAiU7PEBr6EbzAePNHOEvp7aRC1HscuTgNkhFFhcGFPxvQMVZBiP5O_uPxLwbzefOjHWnqQZ-n7WEAUwY_qJM3Mu4LpYscH50f_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29740" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAhuIENG1ln2aMFbKP319l6tnPUl66_bTY54U9oitt9Bx1B66F-sGnpxAWmcssLnMatp0DBocMLg2Htbta6gWucoMietW-cg91tBBO5MlrQ_tThjbmNrIgQCDP29VBYGAwevbLLxER7q9ZtmNzaL-PajQAXyRQKG6K8DX2KOFRb93-DG9dl-Oihw76xs_OgCwPNEu39iW4zs0VhDN1fYoLabYTxDYWz9xcuDtZYpIitPDRu4MatJ0-eFuT_HTbrdhnXKZsSfEX43XB-aIqgeQOJZ_tCDBTdzc4wfIDBvuCGjU_ddXnL3sjFKDwa_BLBAJ7u4wYWKW7nZZ30Tu7bpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/29739" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU2esBlBTIHKXpzCv9hBnIYa8Z54PND27oYwI8_ZE18_5FjCKJxur9scZRo0P7IA8EaEXG64vq-tW3CJuykPhFPtO5SlPaoFCLVv3N1JFtGsYPAwbEL9PqpCemW7J04SDq9kOqpX06rd-Zv-D0g1krXuea4vTMeW3ZIwYQ0mtgm1jqrRxPu1l4AJqN-qkZy6Ux-jdwwiqppUai-G9_RJxDr6YsQDS7p9sP1Wa6KJwz384cJoXqBbUJ4LyfOVCmef0PUrDCMaCT9e7PfOX7fVH77qEmj5NhXTL8TNjjDZGFSvr5jmJR4vZ8agYGU1vUBMpzPxHBDAN05DySpYWXaofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردلامین‌یامال و رافینیادیاز باعملکرد کیلیان امباپه و وینیسوس جونیور در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/29738" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vwOV3nnG8mguZWqhPBahLA-JltydjmLxaH1fC4XfmvoE6pNvgTGJDCDzH-lJVGY_Q1yZJL8Y4f0LjVgZl25E7UWxCyZ_EiPFZ5NCzF-HYd1S7eZ_12I20LCiQpjviaM2uj4Hx51kfAwVFQsVtvEVLDhOzWVbqcqnoe9MgB7mzvwcMcAu_ZY_t2WnHochz-r8V2vxc5qODOK9KEYTJLzJ8RMJG8a2aeFlqsU9cfBln4DPNH0qREebPvCL-Rhsq5iSDDubkfPEI7MpDn8EC6OUB7Wc5q_R3WxH5jAC_AX_J5lV-u1wTkUq69H45JVyB42yTxL8iFaDcCYMykOqj9wyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vwOV3nnG8mguZWqhPBahLA-JltydjmLxaH1fC4XfmvoE6pNvgTGJDCDzH-lJVGY_Q1yZJL8Y4f0LjVgZl25E7UWxCyZ_EiPFZ5NCzF-HYd1S7eZ_12I20LCiQpjviaM2uj4Hx51kfAwVFQsVtvEVLDhOzWVbqcqnoe9MgB7mzvwcMcAu_ZY_t2WnHochz-r8V2vxc5qODOK9KEYTJLzJ8RMJG8a2aeFlqsU9cfBln4DPNH0qREebPvCL-Rhsq5iSDDubkfPEI7MpDn8EC6OUB7Wc5q_R3WxH5jAC_AX_J5lV-u1wTkUq69H45JVyB42yTxL8iFaDcCYMykOqj9wyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛ تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/29737" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcVTwp-QvkooRv_qRz_c75xohHt89mrWNZxp6D6uzY3mqetFJzGJ-xXuNIn21Pn9rLja451TYkiBEWfe8f3ydi0l7VKqB9NET2oFMuux5xph6XbV31if7-eZYULpkn2Hrts9J_9X_orcdbUxCI2gWuS5KDjVJR93qz0IA25a8vj09RZ4A18xlajo_aUhSASfM4YGtCfZreZwP99F-gQAAVcnMFKn5aXMyCGqLwjtGXbVnTZ054eG7QU0d_sZWiQwvQeX6neQ8I3ITNVeSDYwSi_LwQ12sR18OHZtGaJiSX91fsSvFVHCS4NFt_Yf08AEBPwMPLuYAT0udtCxQI0hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان نیم فصل و قهرمانان فصل لیگ برتر خلیج‌فارس در 10 دوره گذشته این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29736" target="_blank">📅 14:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29735">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHttzSDEhM_UTtP03Af9pIjN3uUuGe6s2gBKHjgfOedbv96woZO0oaCw2sOWYdEUAoj4tcHO0MPp8hiERFHaBdElw4C1yi3d5GFYGdCIWAc7NSYGhyZBpZDM7zY1Qkv1qlORZptpd93os3cgWTS0Sfc5733nmsFqSu7aoeIMTEQ5dyZ7ksTqj9e8wq6_WKE6pO07jxAm4ZphBf3IrCewm_XebRCgV1SG9q77T4QIkytlScFugV7Pd8_LkcaO1DDuJo6vtTRC1wdZEm2qVI8uVWYVQtSPhPLXqvugn7QLm1fCPbIQdKOBP8wo2eV6BrnqGxhNBQ2WGuf3PAZC-3ag4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/29735" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29734">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2SzVBp9PY3BESHMenSn54dma39fxnIXG2bdDHDsVk2Rv0wLhSmPQSMazS2MXr9B_MNeb1FFnlvJQws8jvGPADmf4ALaOD6Wmtz7Lc--yK39FXig_c65e2rvBUJYe3DLOsLMKnYaaSPzidgzSAl1anQiO99pmDdxIBct7zE4j6jdehZo7wmo4ZZZbWHCaJJygfu_3KqeidXbinbx0TXs-x8Z8aSY5KnOenKtAkN_wbI6DU6LHuBgFzN95-eaIKbfswMQ9DAUZ5ve2nN9mVOHB_8fEFZSy15v6awxcAk9peHURc1TTUcepRlLPJcNrvISrTaCtuEGG9FQFt3TQP7aisYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2SzVBp9PY3BESHMenSn54dma39fxnIXG2bdDHDsVk2Rv0wLhSmPQSMazS2MXr9B_MNeb1FFnlvJQws8jvGPADmf4ALaOD6Wmtz7Lc--yK39FXig_c65e2rvBUJYe3DLOsLMKnYaaSPzidgzSAl1anQiO99pmDdxIBct7zE4j6jdehZo7wmo4ZZZbWHCaJJygfu_3KqeidXbinbx0TXs-x8Z8aSY5KnOenKtAkN_wbI6DU6LHuBgFzN95-eaIKbfswMQ9DAUZ5ve2nN9mVOHB_8fEFZSy15v6awxcAk9peHURc1TTUcepRlLPJcNrvISrTaCtuEGG9FQFt3TQP7aisYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایوان تونی مهاجم انگلیسی الاهلی عربستان:
من‌ عاشق این هستم که موقع پنالتی زدن دروازه‌بان حریف رو تحقیر کنم برای همینه اکثرا چیپ میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29734" target="_blank">📅 13:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29733">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0PkYjjsHHtQDGv2xiqr2XFYvwvUe7E2umcCPqa9GzX0mW7pmR4GT7qjWPVKVQ_TfSmeJKdjfkAgPkS56shZKVLWQw8dRpWI4O_SWQUJwGAeF-DVW_F5HydMC-g13YGWfuUz3tBOdWJbYoZcLybM68vBm0awP_YNAfjLGiVocDArDarxh2a0H1QODeonu6VqJHs3_1M89Z1knXA0i0vqTJysCLg-U9rMBoOl7u19oXKo0ufSRnc5De0JXeChwSbd4O-grEDnzrX6EVIGNI0wGXoKMKxBpR7CR7EjQ-Xs3C6K5P5ClRR3Z5g6fLv0iIO2XMKPm4WlQFZYVCXrs0dlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خوزه مورینیو خطاب به‌خبرنگاران در نشست خبری پیش‌از دیدار فرداشب با الچه: در فاصله 3 روز من باید 6  بار بیام جلوی شما بشینم، خدایی خودتون خسته‌نشدین؟ اصلا سوالی مونده ازم بپرسین؟ واقعا خسته‌کننده‌ست. بلند شیم همگی بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/29733" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQ3m4kLsBNyuNFocs5tBATjmEBQMzd3xmMike1uSL3TOEeX1910ExIODGPMFB5JfxtPTrK7Mf3wY0eKjdDoQaI24Ddmws1VC0tq3KaxFSwcYXjr8YOvROYd_5Qe0mvXTFIBuIRJRHPoyrLOJ2x-YyWlf8bUYlJNVoihPaFHubYsFGgyYRdii-tBSJlGO7UvgwJ74sEt-x9aiwnnAJ48eEADbr5ZVery7ofRUdBfvkberH2SpZ-qioEKefNxNDv0u1HI7Z3N15-yC2Vrz9wD9TlnMqziAIGM3qAicrhSQSbA-iiOh6vHAMMD8RvR-5-Zfkcck-tkejgdTJgNYBUs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیره‌کننده رافینیا و لامین یامال زیر نظر هانسی فلیک دربارسا؛ یادتون باشه قبل اومدن فلیک سران‌بارساداشتن‌رافینیا رو میفروختن‌که فلیک اومد و با رفتن رافینیا مخالفت‌کرد و گفت احیاش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29732" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak69mADGr9jUnbJXx0LuO1m-WUA55ieYiyuyeHqlx2keExqRx-RKIRPuHeK5TefTUrBXG0aUWNFO4GMJ5GQxet1ffEI1WjASIyU-0ybNvbfxo29VqnLlJiPG365Ibzr0_CXxD2NTcVhgPyJMimcWF5RT83UxXKxtvOq0ecVhIyenjTZkSDFeCwGJMMBXvG1vBL1I6fKosneoiYYWBl_bw9G10xNBw8nPB-ZWKuTTdGq0QS7yOeWG0gjY8Etvhk30qmi7Fbsnf8Oxq67-9J84FY7vh3bW3OS6bytpJSYWGDmhlx6U4SsTcQBb8GUipZ5nXGg7oIn8Osfgnntul0UD-qPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak69mADGr9jUnbJXx0LuO1m-WUA55ieYiyuyeHqlx2keExqRx-RKIRPuHeK5TefTUrBXG0aUWNFO4GMJ5GQxet1ffEI1WjASIyU-0ybNvbfxo29VqnLlJiPG365Ibzr0_CXxD2NTcVhgPyJMimcWF5RT83UxXKxtvOq0ecVhIyenjTZkSDFeCwGJMMBXvG1vBL1I6fKosneoiYYWBl_bw9G10xNBw8nPB-ZWKuTTdGq0QS7yOeWG0gjY8Etvhk30qmi7Fbsnf8Oxq67-9J84FY7vh3bW3OS6bytpJSYWGDmhlx6U4SsTcQBb8GUipZ5nXGg7oIn8Osfgnntul0UD-qPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ بااعلام‌مدیرعامل‌فجرسپاسی؛ علیرضا بیرانوند دروازه‌‌بان‌تراکتور درنیم‌فصل‌با عقد قراردادی تاپایان‌خدمت‌سربازی به این‌تیم خواهد پیوست. بدین ترتیب بیرو تا نیم‌فصل بدون تیم خواهندماند و راهی لیگ آزادگان نخواهدشد. بااین‌شرایط باید ببینیم بیرو درجام ملت…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29731" target="_blank">📅 12:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsB9zN_5jt9nfSTRUhMFuLploxZ7XMIRO3ypYAYNrgweY2xA1QomzNdd4wGo1T_97YWUkKmI1SO0jcy12Re2u24lA3GvlaC2pDk57svU-83Ctqd3gujkA5QD0Cxr5uITQic3lMAmqFBU6nw8VgHJjHdB-jCowNOHV3pWtZAHbFcS4qtWMOatEb73wpqqco998ZWNT2Uk8RcA4ddroByAvrFJGB-QkTn8VPUaZUqg6-DUD5kTAe-cYs78ARelm3oL1CS5XQMfXCEoMq5QonuPl45ehcItLEmTId7IzG7jMBQIm0RgIIxt9Hh9fe7YAx8wjldceIkE-87z_efJrkN6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده یاسر آسانی ستاره آلبانیایی استقلال در لیگ‌قهرمانان آسیا: 10 مسابقه، 9 گل زده، 1 پاس گل، کسب میانگین نمره 9.1 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29730" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=LPXDFCmhWGD8g3S3YFfM9CTR2lcdcti9rEpMlefy4NBQCp1jaHDF4OSsmNrj3GGOtbhsX8EiGc_QHiAEuA0yRz988YViXtgzI505ldlvrNCN-10tJI_ZlTh-5YiYxrjJKifZXVMEgIPMbK4mU2jUmc-ENUt9jNNtm3GeyYftT9a_qlyuQaMJQaaQyjSAuMJX1QfDGPFz1y6qgNAgl_7grP5a-q6p_IBWpAdpoTIJ5HHg-jNy5kHLfzWz6dkf4o1sQ5LRXP0shb9NjHIMgMJTKh2foc9u-lQT_4AzNy2dgb0G7Vf7m_wd5wrVhfBhJ9ebkLLu_2tmmKsgPGpq4rsQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=LPXDFCmhWGD8g3S3YFfM9CTR2lcdcti9rEpMlefy4NBQCp1jaHDF4OSsmNrj3GGOtbhsX8EiGc_QHiAEuA0yRz988YViXtgzI505ldlvrNCN-10tJI_ZlTh-5YiYxrjJKifZXVMEgIPMbK4mU2jUmc-ENUt9jNNtm3GeyYftT9a_qlyuQaMJQaaQyjSAuMJX1QfDGPFz1y6qgNAgl_7grP5a-q6p_IBWpAdpoTIJ5HHg-jNy5kHLfzWz6dkf4o1sQ5LRXP0shb9NjHIMgMJTKh2foc9u-lQT_4AzNy2dgb0G7Vf7m_wd5wrVhfBhJ9ebkLLu_2tmmKsgPGpq4rsQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛
تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29729" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdnldCEQknoU2SJxor5HRL0ebrC-m4n9aywmQsPAngHeXmSiG572mojjHMP-syMOx_sZe-xz3Z71wZSDdgS795XzBzWBghE5XMn5CdqkdrzRNs8tgeBiBY-i837JyjsEDLbe-ivi05AFVcfSnCZzWsxipGrL0ioBJDe24p7ZnZ2l-JjTDIjXNwXLAvjBZ4ubjcz1JZOApHNRk-lH73SwOJFJPx1K97u3eLOa57kPfVkwcECh-gBatE527YarGVvmYMTnz1n7qWklOYYDznKmj_lqGK_84UZs371qhI0sI078bPV2pvYuzTRm5tJAzj9cg3oaJmqgBFMLM5t9WFtDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29728" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnr9-O2hlSsSWfdroKoD3_mvuJF0TO-S0VqE2i78gLggUd83FICp0mIKWtZb-XHZGmWgKP5I6AfHscYUfFKSqDvhLqBbdxn8nN-T3f5IADIVKIACqVBf4cMnjgx_akE3F85TPLUWSbuNl8lkSCZl0IbndTKo8LcWA4kBEmBqvYjYHkMll_gJwII4siqTJ4AEk4WCEPzu1iggLWks6SmUp7J82rb_4WUGL9iU8ONZozTI6YSxj36zGxxE1rYi5lSySmMXwLb015UxUQRZFH-CubPBAXIXWQu7o7AXJiPzhHS2oX3V_kocDG6Nqs-JNgQwpJ7qg4ZMCCLht5aJh1SjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29727" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29726" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfmp-eI2vnHbc2jdeHTI9_5pGOyC2yg7hHZa11i8aRoP8n2YtZ2WFCod_1NGdH8QbtwiA1htoksNFc4tXkrZtodp49B7AwS8SZ3EgVL-l4rjFUHQjY9nlo2CeM7vvKYBu3UTPqdem457u3td6rpKnoDmDzZdDglCSSuEPl1tAweVVrAiwPXmmY5O8-zZcBgnRrE9QaAuFhYXE8FZsdMJCRsV4UYq3i9Als0J3xi2Ub4pmxEGFfjDr38_JxYtZy9sabMVlninxBYsnKjIKnrH7tnAMfjsLbu5kAsqv4rJPIGgiTq0zNebueJwOdN5Bi7kGrPlVQE5QVdSwLp-Mv1F-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤩
🤩
🤩
هدیه ی نقدی برای تمام واریزها
⚠️
چه برنده باشید چه بازنده فرقی نمیکنه بعد از‌ هر واریزی هدیه بگیرید
⚡️
🔔
سریع عضو بشین‌و ثبت نام کنید و برای تمامی واریزیها
🤩
🤩
🤩
هدیه ی نقدی به صورت‌ووچر دریافت‌کنید
💵
💎
سریع جوین بشین چون عضوگیری محدود میباشد
⬇️
⬇️
⬇️
⬇️
r23
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/29725" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29724">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdAPVHFYmTqqVwa8dCQuFSFl-qgJdBCM8wqd1JuF9WDZ936QDBoVPCZD49H0i7ZRG1gnd5A613lqm9JKwjbC7StD68pVSIsL26tJ43pFJg-e0fe6-G_kAAIpi3vdZEPzduWegUeKzsm8ONZL9lUkitd0MZ1V9YVHPyhe6wXFCmlWdlqh2IiYN_rXLjJ8HVjAqGKjndSVmrSdYoecVY4ThEwgumP6M6NPLKyx08-OMhx15X2h4iDvm8-Ob5L1AnUNUtTxqkYCckFi6dNcK-LHJFAoKqejo1-5wQUWjENPQAt-0z42mFHaq_STzUz44J0q48zbxgPrh3CxfpugSCUWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29724" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کل‌کل‌های وحید هاشمیان سرمربی سابق تیم پرسپولیس با پیمان حدادی مدیر عاملی این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29723" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29722">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp0GuB8DOseBnZjSHRxjyzz4h620WH1ZyQzxjzRH6vt9efQ1sAhHj9dodEt4L2cwnH05Ku9mg88nIcxzo-1wfaGSCW7FE_HjmUz0a05ACVT3Ah3OV7LxWKb6mW755ncpqX31UhpDNlr-gr2S_aclidbIfSlO4EXhMyOmVY3HT2qK0QwfucZkAyf3gemN9TnzpbSmzptMgm49baoBa_va8ZrWG8GSuA_b7C5OACU4jqT66hyLaq-L9LQDZ4cocZYOcRjul1HpHXfOJk8gfDZHsSI2NHLi0Z3wxOuvDDgt8-xhtmcE3yhABH8bcpYld9JpgqG3Xcy90_tKW0cULG5Ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند دفترچه خدمت سربازی را ارسال کرد. دروازه بان تراکتور از اول آبان‌ماه ۱۴۰۵ دوران خدمت سربازی خود را به‌صورت رسمی آغاز خواهد کرد و به مدت ۱۸ ماه در یکی از تیم‌های نظامی خدمت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29722" target="_blank">📅 10:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29721">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddUjMhPzed8H-nlDq117CNn6xV_FwUgieTKhqETYT3P40nx9h0uwDmdqifakS591leYWHLfj62zWWj4PSBTFkJ8G2JRIyuTZJGGSbwkGU9YLzseW_lxBHrkOLgCd-0M54QCODfwWUTuvC9QeYw0VEXpE2fDB_Db2Ivt2KK7PFvOI-tasfoAwySVKGzNQ0c350GTkDcSBJwbC8Oc16SxEYUwCshDzSuROy4n20dM0IAT4iqYCmjhFpYpHA2-FOYr4MvqfP1q11rQ99eGX4KnbyBfjvVMCWomZrSsR7SgmNOICwac03Hy0Nxjn8i66OoztHg1iGQZ1cZzluhLXMDjibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کمک‌ داور رقابت‌های این‌ فصل‌ سری‌آ هستن که در بازی اخیر فروزینونه
🆚
فیورنتینا حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29721" target="_blank">📅 10:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29720">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IND0oQoFKC_sWzlvc_yN5Xl4M8DQ1nzCpeQK39nYvPnoE_eifpu-huc8PvAY3jgfmR-cWx8yeublGSRwDlxJfHjJWZQHCbyZQXeMFX9BZV9TuZrgJ3qsxA4-aueWVBM-J03SBqe7X-SwtX0wTnR7XfPqn__URr-eTt-ya6U7OfxZDHkhvUxsgAC2K7Ls-XK5JAf5zPe6GYEft6WjXw7GuL7Ue2_XulJ0YuXS9RPbjRefeJcQ8QHegacT10dCHTN1hAeI7rEgOj7rcRSazXZ0pKl0ptYFLOs63L71ibWfj9KPwmDCCDGCvadaB1ZR44CpCEbW39LMMX9k14QuKBK5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29720" target="_blank">📅 10:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29719">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrE0DvxbwIHsazUfmrk2mqkWA0VpksrCM83GvkY4K5dD6et2T-EsEHw_QGJHAVZ5QU1Q1WTfLFfayvEh8IAUCozDjcJa4UdrdSXddKsBsamamnIWBg-wpto0sYxzdE-7kA0eBrbY_hSDpyCNhIcsqQlnYZ-0-x_i2wcVoPSkdiJR7zG-xjbIsiTginjUrYVj_xLXBcVWZAI5dyj6E2G9SqPm17Pmwh-afXmTpvQYuUbZjAxw_lKyhcgAnVHhPu7fXwECzNdfQh7XY0-c_NDBiXlhN1Bl1vBkVGufPhmOtaMfPoT7S84szF404H46tSwvpXHUUCn53CjsJjpJq_uHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌لالیگا درپایان‌دیدارهای‌هفته‌پنجم؛ عملکرد خیره کننده بارسلونا هانسی فلیک درفصل جدید: پنج مسابقه، پنج پیروزی، 27 گل زده. 5 گل خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29719" target="_blank">📅 09:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCHlKcEsqvb4YCL25BdxdcT50Ka1Wes48iiCX3QdJi4gx8lpt-tZwNAOSXKDn2W6HjTUpG0FiYPoKeYWeW56HSij6cj2nvpBZYkyeR5dgQ7neg5au3YrY6IBm2Dn5PaCPBM_E_cuzNFaOmDr-ftUu0T7dGEkzXvSHkCYtUIGjjR0Ik06E_LkJOIuzYv9fzCotuWfJmP1Q4QdEQXcO6JV2Mil9G52hO959UlztZCCJmNPN7mSUglKiXuhv5HZqNrVSvEUE_ifts7mgbNIlCTPm-kVId4kOWD96J9gxBKnOZohqO1rOAqVH48HmnFZo6GRMvlPcLc1ibYDHBJwVgJDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
۱۰ سال‌از شبی که قلب پرسپولیس ایستاد، گذشت؛ واکنش امید عالیشاه به سال‌روز فوت هادی نوروزی کاپیتان‌ابدی‌ سرخ‌ها: از آن روز تاکنون هربار دقیقه ۲۴ نامت از سکوها بلند می‌شود، انگار دوباره برمی‌گردی به زمین، به قلب‌ها، به جان هوادار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29718" target="_blank">📅 01:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4pVT3k190rqFhf6DyrnjcCci429V-2rBkhpUDl5T27NlUPgkcLQ5KXz19PdiNW5-rxCdHEzbQJAXSVrgKx3AKIGKIoXfCc3i8SKOAnI87Z1v1gf0r-WD3Pu3XuQkTvtaiKoaLxUCl40ScPCXCDYJk9dcPBQS2lg64gZFDfI-bAAaWPA4c3o-3G4lPNkqhFK3c5FDMXxVoxxbrpC74iKvwemuR9YA9eLUhhSTGIWVmqlXRCcMNk9T5_S2-e8W5uNfToHOQSsnDAahhsaCW28JXrarpQNcDu0BLB71BGPXFcWzo6xIPDGrUygkjJdSFHU29S19cLWolVBbHrJ7qmJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ا ازآغاز فصل جدید رقابت های لیگ‌نخبگان‌آسیا با جدال مجدد یاران آزمون برابر تراکتور تا تقابل استقلال
🆚
السد قطر در عراق!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29716" target="_blank">📅 01:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONGrwZ7p5dmzGUEr6h6bnAc9DRsNY2OIUNGn8GWBIXMCOAsuVZ1nUuy2GraJ2gNIJYJuS8H_FvZsbl1tH4qQMPI3hJPnwXI5_zfcWYRhmE0UDRrREn5uNQ8bl1sns9nt0pw_TlsudOXSmJR_aarMVZ28UqEVhLUK_XmbvC7eDRxiDi4hEqJHpps2r1djT9RCjyg9v4VDqBtT9trZFSZpbh-k1EEEyb4NXe3iLCerQlidWvZOYSEJtcnxDPfLpbVFTJ2hNf3phVG6bCCngoK1rBcUm8wUDYnr5aI2202VzJy5lK6K1As4y4czu0-LFg-7dVqG9hdBIZ7hwM0ABkT90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌سخت و پر حرف و حدیث سیتیزن‌ها در دربی شهر منچستر تا پیروزی بارسلونا در ادامه درخشش‌ های یامال و رافینیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29715" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSAWtDhh4x8nX8zVmsYAio952kNg3EPNuJ-wKlWW-aG3m-fa45V5tvlysxms9B8Xm5GExqQ9klPT0H9jBt1qDlpm8bI2j05vsuIxEz42ySz5ep9cSV3-dZ-t7r7BZmZMn6c96YPUyOnR6C9gb36BYI4D9kZEnCUkRFfJKp5FfSahkigFiEdVvaNB1CAHhboa1J1w4P5gQ7IdFDsM8KK1jGUlqZhLjgppqn8f3v6Zk0MICKu36SB4mMnWXd1ZVDBelibvSDEVvk70bFJavhS6GpDFAiVNCxU07isbRb6_zcUB2EvYqucOERsNla3rRwV0V3FSfdoRvMXYEe5iZvh49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل تقابل‌های استقلال
🆚
السد در رقابت های آسیایی به‌مناسبت‌بازی‌فرداشب دو تیم در ACL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29714" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE5dOmrggkgiktf9CHYWKPRQmX4Mq4X0iLE13EODiKCjx5n4Pr-1yw4nY5emmyHyT6tdWa7-AP9xlvwBEeayF4nIFZH6htei3lepdhr-bN0tXJCT__NJn01YyqWvbHOSlS5V9Hjs1fIKI3VjfA4SKNCMTOnJtw3AqBQzkqFCtqovgSYoCXoIq4wfX3zi4q4A4uD7hf9jj7h26AXsbjWxYTlstFHoKRZOA4IvGmlM6GtEeHrNfTBKT9pwh4uVhBsgSJUbAQGEL1YWwizDmoN00EkswUjmv-5XeEXPB-C4GC1mJVA8a8uVEpQVRj_dCSjWZwMkY1NhtC3sRdTS6MidhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام مدیرسامانه هوشمند سوخت؛ خودروهای صفر "نو" بالای یه‌میلیاردتومان فقط میتونن از بنزین 10 هزارتومانی‌استفاده‌کنند و سهمیه بنزین 1500 و 3000 تومانی براشون حذف شده. حالا سوال اینجا ماشین صفر زیر یک تومن چی مونده اصلا؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29713" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdw-XvfHdxHhABv20xr-V3YdgvhrrHwQkhXyNsArGUVGU6Q23Js3dY7GALlzkk4v-JH76CGdqbcE0WDKwk5w0_4koxCmgB2qJEYwUjnBqPWg2Jgy5kSJH_iMSXFMO1f_YNMc1N_ZuTWUGAb-UUANVe6C1LYs5OjJ27akVm7a2c5jgUY1oHdeEYtQZ7lisGt9bGl76rLqu6lvvk9M9AeRaNT4PXiXfR67W82LW5HRL8sU39zXIvuub9QaIs6AtaTgUnsuuX27vPUGtj2_BhD5a2ep1IXp_EVww8U9zFwtE9wPyf9c18q9xILJP2PMWyWNa3MqQN2Fk6su8Fi8GrWwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_mMWe8Br3VA_eU-BkxhyvSqUBm3gPHpw5o9tXxoPhhrNXXy2FiX2yRPIaRKI6GjIXr4MtgIgoDCmMsJvf4bku0k-xYaK_gqtHYIK-xG19TZ1lI3XHtkC8zInDOMaununHNlqu3NB2WcpCXzVCrxlQ4YGsRUOrtV1GuDu6xyzarVKSY4kQ0fndybSnGxockcLvkMl-JN3SD6zj70EuRC563NUFVL2vjId-fS5PZINaOkzt_Rf2noTSZhuUldUlfVtJ9d4libQ4moi0yIuPrJlv5IkrvbPTukELIaOavMdsXsW5wRQBt-peFoE4HLcLlD_ls5VmFhTbuE8wdibS28uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko0-x5Oc3XZF2f8CxTPocqrZlA6eQQjBJEvm_s3kxvnGuu2gG-63IHWZ_eTuHMFMjlzcMkBtERvRrB2sDDlsBiYdoCPAiUHylGdSwzVxlkNoJvKywWehWFBgBgpQSRCJ9mo6DZ_Ri0QjzfcRmckMDUhEOeWNFhVZRZPPkg0cLRIUyOokB_k3dMdJDygn_7wAkjF1gykKhIKSJT1jQ7znsb67U7wta-NNQ6Cm43nQwLPRiV05LQVC748WI3neXavvTZxM8qLBx35Qu5l8N8VUcGlvy6ReriorLLabUwcj3Z5vj_uidGNmsELLIuCh2ejUs4WKnQkhTh92ECb0mzEKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29707">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWOrnu-p812CL3XkQUGFly589-2L9k7kEELi1DR29QCPFUqFMKT4V6WcqcSD74kgdo9_Kvso2IXQzeoLvgeP-nzik62exiaLcVsUuB3xQZV4XFB5mBHfxQoFPnbRd0p3mIvuaqHte4gPq_onyAStT8v4fewjl3cDAMJ9mVK4P3VzRgk4isCmVl31tnloniV0ke-EoFinTMHe7ROYfoutxaKPWP97NEoJC8p6dU4Xzh9GVP96XpJlPqcbBjhtfLSRrZ3PqpWkwyVqVQzu85FaO1VHwqIKEQFGP55iljF1A3lK0zySeS30OUetrPhN8JfOgFCouRdoCF4kpdnN-1TlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق
؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29707" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29705">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3yfAcU5yrSrL88bwASaWQUHUyjUHueWqzYB5yK3ZGII2CV2mMomzEhPBCeTL8x8ZiY17thKXdov9SdncHzRAHCFINU1qJzys2NE4Lso_IQXUWAnkmg4QlPeEe2SUtm-Yl9DXxxy6zh7G_DU5ukiRkflBIEsnWa-TgiNgGS_oaJoTVa7hqsesAe_d8eao_wEYursQMlqn0NeVVghWqqcfr8U30beW3zH2t7J7NfU5FMpr-cxQF5-p9wBxNE_JbUZX8nLekj2mI1YRAh6bb3bsEzNg3dHKwjzb9QHlqIoTTRo3L302lk7kYOgDPYC5QyV6FwEq74s2BvSuMY1XfmNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0jojF_Ta-HZcbeK-fBI31jQAU5TqvZnYvICT0StYf0Cbr7YRH31pm6gyFDyDh-2al6T5BCzXPTYRCb-bE71CN5-4jF4oSyaZbS2birWvHMpmzy1-g3kS2zDeiYkyYBR8ODLK3UKzA42y16mMBqGP0o2Gt6J0ue1TC8r6kgyvXZBxe0zMZZF3Q70X_bYOSskIyW6A4MnAicx-pNcZ_BzmP2gQuV0MBWtZhGTGWhbpbxVQ3jQInTuNaomGY7vi_bcX8vQ1f9JktG2QW2-Wu7dW3vvGL5N4nGFj36FRg0uwNd7KB7gqAshtATk8kIWdCyYMK0thzS43M4GzAKqdXRWsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29705" target="_blank">📅 23:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29704">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh3i1yDhRuY_pPF_JuHv4pQ4b52DHjbGrJrOd0uPe4kWGY8Z29oJ8YMH1PrpfaHprWY_IgQ5d7_F4HPl_aS5pOEKN5prxEUkdh23AiFGqLrGjS5Dz-4w9GRGICIkWTTCdGrE_JSUiAgQCqgxyX3_vxTJSN4ciJYh6v4uVgmzbtKlm9WpUJyHHBGGAc_kGQkvYU0HzjzHlWVLl_uyA6jd3uDL7e6z3uWFMwcpgtYuW5paN8gYRA1FskYKXmKu00oL4kSI5uw3O9sCIqinAcEBfqiaXq5rNVONvnqj_i34TsiW0OyWwKhFjxyFpRN76fkLrI7U17KGAjFjzH-nVQKFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌ چهارم لیگ جزیزه؛ آرسنال میکل آرتتا با دوگل دیدنی گیمارش و ساکاساندرلند رو شکست داد و باچهارپیروزی‌پیاپی صدرنشینی‌اش رو تثبیت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29704" target="_blank">📅 23:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_jUgMhGMZyAS_RDuwvhlLPFyMjzn6auadaGCafLCXF_EkxJ0yNjNeYgCozcfuWt6ejzLM5dW0OIRMn2Jp6zcIcOKWW3-Oy7dOlSS77d-VwyDVQw31bd6Ou4nLe4_G7FQ77rjGxIE-WhL1Yzak9lDMdbRvxmajdoq7Ze42tC07RJwx9ubsq7WhC_m7qgS09BICpT9VDF53h3JkUV2pn57I99_FLcvtmG7mm8On_UjNYY0yvpvLaYfBprFDiEZeoFoAJjet5HiA3-g8FxvMyyO2j6bSrmc8jO7ehvQaigU_kLQNopcSLi0WGl2_QCDoQl2OgTpjk1Ss4vR3FCjPnj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29703" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DaIjm1l_KMrBUB_6_EVVDj7gkiELlPslaLfxG8VJGKl1sUvLkRDXh2qFV2hAFEsPdFynEsEt7TKgoQLjagF-7vopu0RSQUIFXpyA49E2Dgn6_8ZVcp4SfMtjCB8HQ5mbK7ZLSgw3Bi06aiu20auuPCVPQpYfk7P2UXz2PiTQxDZaoiR06za1JLg2YUk_RKvKXWFgwhNwvp-k7DXPQ-TBCJep43j3RsrElT4UeEDjBfjRd0hE8uNtM0HxEJHOwlohDmW9lS-PRIzb8EhUzbT7kqffEWLDXrz4HwD1A2qoSFqd_rMa0JwQtmCqgPPcqt74grI4oe4pn_x33IqhrxSgfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DaIjm1l_KMrBUB_6_EVVDj7gkiELlPslaLfxG8VJGKl1sUvLkRDXh2qFV2hAFEsPdFynEsEt7TKgoQLjagF-7vopu0RSQUIFXpyA49E2Dgn6_8ZVcp4SfMtjCB8HQ5mbK7ZLSgw3Bi06aiu20auuPCVPQpYfk7P2UXz2PiTQxDZaoiR06za1JLg2YUk_RKvKXWFgwhNwvp-k7DXPQ-TBCJep43j3RsrElT4UeEDjBfjRd0hE8uNtM0HxEJHOwlohDmW9lS-PRIzb8EhUzbT7kqffEWLDXrz4HwD1A2qoSFqd_rMa0JwQtmCqgPPcqt74grI4oe4pn_x33IqhrxSgfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29702" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqlx8WEzMrxAl3cwk5pzxsDI9J88JaznMhnr5YqcQsfmVc4OvYjehRouqxe5V5tKIPqTW5_Ek1fjKxw36oOVxZw4iVUgffANYNGj60rVH58AlUIYnShyH0KT4J-sZaWl_HumuzU_qa0ZgHK7rZJ-ud_OYSYto5U5tCcy3K4mD-d6hSQrWBBVB0sN1nLTAv_vpVzgWL7V9gMXqHlW_GcavwjiHj_TwGPFF8dK-JKyc099p4G-HboVIkIN8W7PJOuonC4wu8rPw514QQsAAYlzoD-lT7OfP9rEabflAgwuSXBya5wUiZ7raz8jvoUz8HAef_WJFIBjIXO-ODgw6XGTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKAFajkbwLw15KmioZJMysYoPIcMgTODvQSWaTdJ1z_2N9s3TwR6lXZhEBo-XnSbV0HcyvUdjjGZQMaeg0UTn2K_gWjwtMH71iv0gaxjlCFh15da0rUIUh1Lyyf7ZzJJi9q-cSj5BpluAAkeNftWRMslWi7nnUACmGPAbzyjGMgOBSYvergVB964wAmUawKhCGUdyARySJHgIFP6PrdyF7FFojkjImlxOGs4K7xj6RdQ8LFUfNwt081l_sn3omJYyXIimWpZQDk8VEXROBCVDHukLWTXl8cMya-0oWq9PJr_W-fGP3n9KmM9WEVc1kJ2GdrUYhcTF2ZaAqjtkPHL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZsZBZKAttdQBtOxZDzcEMtv1CiMNvG8iBG6U9AiuPiqI0Q8I6x2pXIIRkqd4BPybzh2zSoO17CjGvccrQwuksOqRl2wc2ZhChEuwfORtjcHFrlq8_pWhRCj0atYL_BCwjeiNWtcCxb5rHn-sMfPR-nebPSA_k3eN8F8OFiCbSq2-wUjyO_dMb0Ck5vUEiwvuiE9Fr2MstNsKGzFzf7BzZLdO-HNaBLH1isQbklIKY0o0JUcpzSCFHwTzkYd6Mo-MXihCHAYnF69silueciam4heaL0wTSkET53OkMHQ8IcjHxZFH_MJ4DAm5aJNH5Vv0BeHsjHVOC9zeeSDk-kwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrvYLYGZicYmBODzD-XRCvPZb_Ek2vO5Nns_nJv8K0l2B_DPL9kCo43h-gumixdPnaH3COgRtsNvgbZP1_CXt4vESeZchidRlYn6yNzhaKhlD_5Z3tTd9SXh284GS0dnF0Myf3ysYx4SpqTPvWg4PPAI1f55bwxRxlsnzSanDg5H23p20MbtwN9q3XSkjbnCf3XxJq3J-SicAc_81Q04AcDY3cIoMJ-GyWJ3eMC7ZhUg_XAPqe_FOzInW8MRAlOIiTs0s2vU37pT-2zg5aDh-dOk0if_S0iWFPgGo3PWTw8kt9GVsya4LCngv5S3CZZV6d5g7BewDive0FKIL76P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=PRXrqfFfc9zu78KPs0xevAKFLQuEfHBy_vK-fm8mh1borIUI0AeUjI1K0kQNrdcJ9B_rAZqX0eK5CqQ6H-62JjjS1MUdQ0LinrDm5Eo0246oMnxXQsY9Y8FGtDEHUEoNQEdFxP-IRe7iJ0na1UIek8fkTDAD-BU-gYG7mFCUzarOKMQ4cJK00pWusj80FO7nUuAZxkhlPstk2-zvv3UH9vFL1pz81Mu07JKHj-Ns5K3VnBoeRHjc8l-7ooorQ_uZtQ9L6wegVPSPIsw-_EPO1rlf3cgNvzonhGPP3BVM3gLsahiO9GesmcHUNo8LmnTDWR20_lEN9gAWM1xbwnRaaYyBS0zNZVBHTjkxZrVXRoHq-IBrUfFW_T2qoAGwr1GNdVzYoRQ1s4mvodn8wSiQ6NBtSJxhwV2TTzBmgM0toUuBa2bKhljlDpG-w5GORgFbKsgSgK8AQJapYUaiGaFB474Jfb2qG00er6Y6eMqbsGBk-dOilp_h0Gzv83LqnYW-3_e8YCzr3rZ5m_LLSVRXRDirgvcHbpiNVwjqtS4e1_MJpsRVD7sOxwcafMXHySG7rfQF4awU_Htv_5fyv6BxjDng6g93k3qh6qSclJI_R1sUYxlz0PbH7qNuoz3qTP8ERdSHj74vGDH4ZGtdPr6DkJT0BijiW3B1IXcGGyYMzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=PRXrqfFfc9zu78KPs0xevAKFLQuEfHBy_vK-fm8mh1borIUI0AeUjI1K0kQNrdcJ9B_rAZqX0eK5CqQ6H-62JjjS1MUdQ0LinrDm5Eo0246oMnxXQsY9Y8FGtDEHUEoNQEdFxP-IRe7iJ0na1UIek8fkTDAD-BU-gYG7mFCUzarOKMQ4cJK00pWusj80FO7nUuAZxkhlPstk2-zvv3UH9vFL1pz81Mu07JKHj-Ns5K3VnBoeRHjc8l-7ooorQ_uZtQ9L6wegVPSPIsw-_EPO1rlf3cgNvzonhGPP3BVM3gLsahiO9GesmcHUNo8LmnTDWR20_lEN9gAWM1xbwnRaaYyBS0zNZVBHTjkxZrVXRoHq-IBrUfFW_T2qoAGwr1GNdVzYoRQ1s4mvodn8wSiQ6NBtSJxhwV2TTzBmgM0toUuBa2bKhljlDpG-w5GORgFbKsgSgK8AQJapYUaiGaFB474Jfb2qG00er6Y6eMqbsGBk-dOilp_h0Gzv83LqnYW-3_e8YCzr3rZ5m_LLSVRXRDirgvcHbpiNVwjqtS4e1_MJpsRVD7sOxwcafMXHySG7rfQF4awU_Htv_5fyv6BxjDng6g93k3qh6qSclJI_R1sUYxlz0PbH7qNuoz3qTP8ERdSHj74vGDH4ZGtdPr6DkJT0BijiW3B1IXcGGyYMzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29695" target="_blank">📅 20:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFyWN9YK_hMZtGmwNgmZbFyelEX5x-ghkImmZvHCNJbirEuOKsrjA8Bb-s4QhVBtuwko7B1ekMSxv5a2IIuj3rA2SKJtZY4h-c2KXrttQyrGb4_qiaQAKuz_TdgHBsGCAZkqG_ydBW9kwG23UThtdlWQAHICW4rDVnIFj8t__CrBVmA3rvkzGH_ytBOHAtF581QZUR6WqZaIri2HdFYCg5eAzT8A3AtR1yTfl1UonpN1s79QAV3hcLIoYP8KXIbJOneqHayTvIgx5evyimPEUYm8QZd7ODR-ZL-s8v1Ngdc1RzC6XJkRpFgzzg22RRr61X5FYohcq8hLiv0g5lCD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29694" target="_blank">📅 20:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5X8vphW6cwTHTfj-DlLlz1Gb9EJ1uoUhUWdAFofFnwwuTdLthcqKCS3R1FVtDdMNF5n9yP4xUlOYnqxghNzYMxV9ineN4KryixINLoaSvMtt0i16Sv-0q79Dj-LcsruQty5-GiglRGmFa-BFiZz-SySOK7_NLMybwIQjPDjRp2h-xZ4IOZRWdJseMsZMbX5A8qdA0De7aK1znWs_5oxs21D1iciKty9hGHmYJYTqzY8rkCwxaLhZ0TmcEKvnXu993IK0DV5Udrv1LRswD5KO_EIbLx8qxJI7D8F3h6rpH47ww_w4ANCgulhWpQjoZRy1fYhi0z27GJISd6iX3QTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی و عجیب اتحادیه موبایل ایران: مردم به‌هیچ‌عنوان‌برای‌خریدموبایل عجله نکنن چون قراره خیلی قیمت موبایل بیاد پایین. صبوری کنید!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29693" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29692">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=nyLNvhFYYCrUa-pr-viX9T44xlgYNKB_TT9Hy3QL9xAnWn1ZEpdlR5D_bke-jzKnjgWndNDA1dofIAS3nU_WgJbok5EhHFupHk_J-9916-yFFbZiSsnsy4-h1zU2kfkQMYMpJ-ItVfc5COWYWw4wheMG_1wyzfWoI9MwDNe2EUOmZPK35YPbApR6uN9InRz1rHGLEAMdh62_tH5x23c2eDGkyBcSsI_mk1YobtjyWtQJAiERL2S1Sz6E4DyHWPCQu2P5qurEaayu0T2TYQ_3l__6BSL3tokpbRuonqcEhHtRTxvcGTw-s7BX1nyfC9nbqR_tNlNwSzJMuk6bbraz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=nyLNvhFYYCrUa-pr-viX9T44xlgYNKB_TT9Hy3QL9xAnWn1ZEpdlR5D_bke-jzKnjgWndNDA1dofIAS3nU_WgJbok5EhHFupHk_J-9916-yFFbZiSsnsy4-h1zU2kfkQMYMpJ-ItVfc5COWYWw4wheMG_1wyzfWoI9MwDNe2EUOmZPK35YPbApR6uN9InRz1rHGLEAMdh62_tH5x23c2eDGkyBcSsI_mk1YobtjyWtQJAiERL2S1Sz6E4DyHWPCQu2P5qurEaayu0T2TYQ_3l__6BSL3tokpbRuonqcEhHtRTxvcGTw-s7BX1nyfC9nbqR_tNlNwSzJMuk6bbraz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29692" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwmTWrFhk2xqem0xwMasBHQueI7RMsK73fI35AVz2h57AYELVGHNWxT3XmsixNVgaC2-aBf6KWGBYdw1WpkA_pRTpvzOTY_R6EccZ_RqP-2xaS51y1xGYK8Fk9bmswdPGiTkwT32xEKe7HynxZEfKoiBjNk3hnNeCkxdlk1tdX1hccr0zth4dGmHZ049OsVLLecvapUVHEkw9OoEUmX4XmRGcqbp6sEMkKI8oK5JB9DIA1VJfmANhcCb91-V1mrP3qk3j4LA4yFsF7Yics51jT93icAHiCrN_AoCc7mZINhqvz8QfxbX3IBTeBXm6c_GQ68HdM1VAO7Squ_XIfhUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🇪🇸
نشریه ال‌ناسیونال:
فابیان رویز ستاره اسپانیایی30ساله پاریسن‌ژرمن درخط هافبک تبدیل به اصلی ترین و مهم ترین هدف سران تیم بارسلونا در پنجره بعدی‌شده. رویز از یونایتد و چلسی‌نیز افر دریافت‌کرده اماباتوجه به‌رفاقت‌نزدیکی‌که با پدری و رودری داره به احتمال زیاد بارسا رو انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29690" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J96raAIyyfkIHLiF3ubpcTGJpW62YMp2mlzeo12tGj-3oR6cWDV4oDo_HtXhfzgv2Fp6mr4DpaUMydMbUrB2MMDTZcOIpH4RkyHy9dApSN-IVhzOGRvizMCpw_bO8z01OmP0I4O0Yw2X8nU7tfpyjXwrinL2BF3A4V9BpDsGb4YtPdVG3OyZ8ha3YvwmxCurvzK5GDoGTpK4Nsb_SpiVRm9kR-9QhxTJuct9qwDl1yQ8eSRLCYDm5sDx9EQ9QmXwbn5JC1kBpD-id3tNN7NPF4VCj7Rm-pe8iUfci5vuXiieVS2w2mB4L6tMrBkgM7M8iIZu5ODh0QqynoO76dMXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0sMx9Svj14pS459iZOLnTiKk2wbuQAzF0B1vLgVYQtRfdDs1nGLNzQl8rEygP_SnwVJK1mjDklKqtnvlVqcRAA8-Tgrzpi8zkza-dFsEfBHrFDrfmj1G1GReKWKhuNZdIb7qmzK27NmHaskkef64ZyTA-dNrYJFWexhTRWNtGbwYMmm9SyUJLe-pmN6pYmI_dzkroa0XPJdBqtbCa_2P9jOaqCnRF4J8fPqKwp6N8qsCe_STwTIBFz97V0RzQMULpO2hdAFyevUOOW79U4xsdQcPxaB5_AlvWIOpGptYmrwAEGg4K1WSfAnftgogsxZwzmBP6B2O1DzRVeTWD5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlq72vvNkthDxCTHSAJcbXquessaRpvKPFOwdqe8k-UiYJPA-KZub2R7rFZiclU2dcWy0105RiFcJ6FdGr8e6RZoyBftq-JsGaJZfZznvzSg37xApgXvMmH-yrxP56ckzfVaiwDf_vP4amzUAPqpaw8iALOKlhF1M9ITFE-u34NGJgHqvRPY8vskOEDPwn4OxBafFQuuor07zHNUDBSVrg8e4MwbQxL62QTp41sFQYrC4ACKvuZKufwdco_CHu0n0_gcQr8bXOE0tYj9kreXvSqJbi7Sk2JXvaV1jD1Tg7jmYsGzFnkIX1ZEpPjUQIB-6o80R6x3R2ONnEfsp1Svcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc5QDwVfVv7RYSfGkWtdj5PS98fL_Z5bNm9B7rTrWJjUstr23Ofq2EqBdvn8ePWTRWxxjC8gQCgwreT44Vv_u44wepqhdPj70_bQno8qgWW9cjMCCGJVnZFn127HYzZmz-ZbkuHPowcMPwR0VkCILfVcbEdLRx08lGdxrmJjb5CN5pKxv78Ic-o3o1mLY2SYkymFVD5ECa3h9q-UelSmxeJ3QEOXyLGp4k7zDO74loijHdJsMujq4guoqjRXXUB00Or_xEYxo4gvT2jIriPp6yOeRzaBFL165XGyDM2ivMeU5R8kKQtwU3yL5LPZ2N3Cb6SBO06XczVASpRz3TLbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dboCmhuqoOdl4Us3fFYJLGRLngFtCHUKyDnjy3dbzvAMf91YZkTzREBmbUGUyEq0AZ-jmg53UWjvgBUG_RZeb2PWVTq142PNEpZ--Pl5qbYk-1_uuKmrxzFpMBdoKzOoZ7ZryZqm40wpHkDw3zPVWXCWGeJvURv-9HNLpJyn8UmfmPz7Lp_eFNWZpoGYIrNwEl_GMV51UUmqfJaI5G8O72Sf3SYZFNZDDkzxfgJOGJIEB45L8uxFud-JITJtL5SSTaI1OkpfzrfqZNpjJyI98_FoSGo7MKDzwl5BYesp72Kc9Fm9RGmg9xvINMEj2cxJXBzpOsISGGF6oj0ohkgIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2gv2OhhHHJvn66e1tO4jKvaDxucFnVwzFD-e_jFjSnuFya2BhhCfw42mCAx7aolAb0wNLoWH3xHP6cYRW93UAKqbJYuw08OB0PeXUHSeTwSIc94SqkYWskQOe7UdP539MiwJVn51PVpiGOC9h6Lq2R8nU1hgBYL97bvers481C7eBrOuFNj-xvFrXkVmZfvCXrwHR2_9i5V8_03S_X0W-DXV9jF_Xm-HRTRLiRo-Tx0c6NvNrmT8lcmM0aJLt8hD1WDRFNp8Cdl4O_MtKEUEv1fsuGmbcEYwnogb-JuWrfKDJOWslSPHaedWQBka9ZG6UJPbASI6ZdpteSROFtYLLYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2gv2OhhHHJvn66e1tO4jKvaDxucFnVwzFD-e_jFjSnuFya2BhhCfw42mCAx7aolAb0wNLoWH3xHP6cYRW93UAKqbJYuw08OB0PeXUHSeTwSIc94SqkYWskQOe7UdP539MiwJVn51PVpiGOC9h6Lq2R8nU1hgBYL97bvers481C7eBrOuFNj-xvFrXkVmZfvCXrwHR2_9i5V8_03S_X0W-DXV9jF_Xm-HRTRLiRo-Tx0c6NvNrmT8lcmM0aJLt8hD1WDRFNp8Cdl4O_MtKEUEv1fsuGmbcEYwnogb-JuWrfKDJOWslSPHaedWQBka9ZG6UJPbASI6ZdpteSROFtYLLYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=Ni_hsMbH6KGQgDbun5iSSr7H43ADm_o2XCYXOBG3kueU1DqZtTRC0iI5ee9mN399PZLh2QPoImdgxc9OSbV0iOTCU5rHVZikGIXIE15noZ-TsXYpz4KhkDYMKd9ZtgR1E5e5XbDwCA1vV23U2nuXDlObGk9qXu6oHljEAQra3tHvBrVhHXMqMI4eXTbSLvNjC_AV7hvFP0wCAwf-EYyGM1Exva3-EQGu3r8WaFN6wur4EkcDBEfg2Wg2QXWdWKEygZ0El6w9SFU18PXb8aCCyAvEgOe-AmpfosKf8yIxIyRocZmmfWKSJ-tJ_4bgW0T4NC-zsPgVfslJ2PKZhgfpfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=Ni_hsMbH6KGQgDbun5iSSr7H43ADm_o2XCYXOBG3kueU1DqZtTRC0iI5ee9mN399PZLh2QPoImdgxc9OSbV0iOTCU5rHVZikGIXIE15noZ-TsXYpz4KhkDYMKd9ZtgR1E5e5XbDwCA1vV23U2nuXDlObGk9qXu6oHljEAQra3tHvBrVhHXMqMI4eXTbSLvNjC_AV7hvFP0wCAwf-EYyGM1Exva3-EQGu3r8WaFN6wur4EkcDBEfg2Wg2QXWdWKEygZ0El6w9SFU18PXb8aCCyAvEgOe-AmpfosKf8yIxIyRocZmmfWKSJ-tJ_4bgW0T4NC-zsPgVfslJ2PKZhgfpfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPT39jguo8XnLZEV8dXu2RCmLiH1PB1-HN2uKxTOyluPGauy8Nwd3Nzpu9ywppj-bPpwRbmQWSUSA4OteJi_d4lcdZvn5EEISZnHGCRHMLHyluudhueTqMlW5HAUm-PF9wldE2avz-FneCvbJric6NM_zRJ20BfLykDz3Vxciv3s9ZopvLQSJsp6TAsNQPeaYVA6j-89vGkeDvewd1bhHW4xdbPvpcr-hD9ouxKwjG-fVXMhRMB1GazvpAkLMGB_LtTTH7mqnlqNRio6rxuoZ1VQzLw-NcnalvPfH9I9DzsekpTDi4ikvOF7KabV9z2sDzM0WTfUSHeD_qx_YPeuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLGGlFq4fgxqhbWY0mNgiTS3syPInRfemwnUIIxo1OMdnCiWijFFFL16sV3_E0NAsteyOyAbeimwD_TXctt2L2IVt5riFLQg0D7hrFNGPR6-vsxV1qllCDVZgQ49bW5e-fKBOirVQwA7RczvN88BRfzVvF1wfa0CfpDnlrIBq4PTAhKLHW2k-pB8ibezvYtWjESRLtqWrlFLmrGdwpkiSD7DwG3lP-cwCBEAacGi2S4mnO1yg9b4T_bikCZ4KV1SofCmAePcWU0uK-R9PTfZ4yjBEW7xWhlYDKXYjLhhlxEa160xxJPDp7k1gnZ8R-Yl-NmekyubX1VUoO1ONkinbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqGdw6bjYRONg7tbaSUNqpTM2MVrxzr922ne8mxxoVBb7M37Hkqd1CAWB0eBahFKVI40FbQ-rUSpb-ueNUgK3meUTUIjTvTbt51hGEpQVVFbHWxUQUXQXt1L2Gmt8qDFs8zyz224wO_lO5HcnPFhS9ilzKoxpYJsPDTi06cCWGApy9Sye0NiU5Ze4_j2-drHK4Ni4tLW7QQ9sV0Q52qutW2QzL4q8Eu3BaXOSjdrIutOeIU58_LIiX51RuaEmg9l886xLpJLFB-alFYs3RSpO0tANoBXHNcf-5t4tL85TCisxIY9WADI-FJUAtY485hNj7_a-ZROnkZ_Zak1ywQnNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbzMGsWrCsd1MmorsKuJoHdT7dZ95VwAF7E3OrZ0rRAqIEtOSLPGT79_lNgoYct23tyGe7EJTUQI2xCKpH7apLlBqJn8QLqPiM3wPFV2I_T_XByiuv3pWDXWP7N4td8e2ut5sse6R-ggrm9AK1isqv7Ddh3vYa4yE_xGZabypox22PORAUlXAKLFOZxXyf_h3cPA5dk-ajoe71dXr174_QDOAipEcrCDFrGWan7-H3njtH5tTZQD1TvtgTjrgiaoXYqvBxKFFVhHcuTmfV7EdcGua5epsCSPbtjqPh3J_ht3O7kewA2EvlI2ViO6dnKQzmmdJIZYItG8PjSzfjkohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=tw7HefRG8HZu2-qHHa2OtPprjnocIaDLm6499obfKZyQF8Abp-iw3vtQR2Rt7KwAzJQNYftSGJl3kKU0o_rjAMj90bd_3WZPmPIwbCZ-XGA2ALMDrgfhf-DG-yMU3VltI1-DnIkmEHH8w25rrUdl-1NQEu_FgoD6SQGzKuRhjLNEMv0DMbS9T30HuPZ5N2X775PtKcvldAiSLQNASbc2NYGJw9_sGoHC24LkR0QkHjSehNddk9EFyCwRt7jQGt3mIjW4X20QtDBDNL6YlsMLR3mFhzQhybcnuddlc_Zdk_dZz1UioD6dZh7aclNzjrrK-7uy-Z5EeY1CC-J2VSoMVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=tw7HefRG8HZu2-qHHa2OtPprjnocIaDLm6499obfKZyQF8Abp-iw3vtQR2Rt7KwAzJQNYftSGJl3kKU0o_rjAMj90bd_3WZPmPIwbCZ-XGA2ALMDrgfhf-DG-yMU3VltI1-DnIkmEHH8w25rrUdl-1NQEu_FgoD6SQGzKuRhjLNEMv0DMbS9T30HuPZ5N2X775PtKcvldAiSLQNASbc2NYGJw9_sGoHC24LkR0QkHjSehNddk9EFyCwRt7jQGt3mIjW4X20QtDBDNL6YlsMLR3mFhzQhybcnuddlc_Zdk_dZz1UioD6dZh7aclNzjrrK-7uy-Z5EeY1CC-J2VSoMVIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=JsSGRewGeLTpI4ICecAEL_Nez3Uh5ZsUeItR5dCItgfGPOrT8cJqlTF03qcvmARavTqLffZl5iJXtdhp_novqgFs7jT0SosyrbvCBslc3YFEUwa2JaJOuu5GkUtZTGYp91sz2gQWM4q5sXOto_EVBvzQ-QC9wXWtA6WMUPl5fdGZKmPgGluiOYKuoDKE9F-ypcIxEWzd2rEwY6EbSW_UGyOrtb6nIMYB6axMyNyLN4ffI-ZpCyhOeSDYFLWFk9C8CjwMZXktn7Z4xPMvEMShIo2EqsJAKvL68jqDVLTF6FRUk6URSvLPUrxZpv0Thr0ybWMJlPOmD5Ujx8UK-Fr1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=JsSGRewGeLTpI4ICecAEL_Nez3Uh5ZsUeItR5dCItgfGPOrT8cJqlTF03qcvmARavTqLffZl5iJXtdhp_novqgFs7jT0SosyrbvCBslc3YFEUwa2JaJOuu5GkUtZTGYp91sz2gQWM4q5sXOto_EVBvzQ-QC9wXWtA6WMUPl5fdGZKmPgGluiOYKuoDKE9F-ypcIxEWzd2rEwY6EbSW_UGyOrtb6nIMYB6axMyNyLN4ffI-ZpCyhOeSDYFLWFk9C8CjwMZXktn7Z4xPMvEMShIo2EqsJAKvL68jqDVLTF6FRUk6URSvLPUrxZpv0Thr0ybWMJlPOmD5Ujx8UK-Fr1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl8nwiapQ3WuGApZxKi_oJTubTsstP4HZAisAYcPx8MUhl4144htoY7expub-VG40vGDd5Y-eL2Ca0BENcyZtTcEDuZvK8-c0Qi8aWbXA_6AvEJU-shRlOX2_To2jqOimNHeG-nwz-cNVC41Pl4PakCJEE_CO4cE1vCdyKg_4qhvL0CCtlnEX4vsUzgUuYmBEgCkkKXWiQHr37KTHT5eVodZApZqMJcPSBv8k4My-MiC_hLJprq3-heVmCS0Gnl7VyJaEqh5N9OPaU8KQtTi48QgsEs-iauSjkhMZrolQa-m2cJLbi4vxVATWrpmPYdieQ8B0dzaQw-7qt4DA2CwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29673">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMbsVjEsa4fpqMfe0MXKQFPzywNFC3fPUNMII5KBvMiHrtZN-1sMnZmIQjqZG11vnKmQVJcghH8FnOCK0aGUvlCGd2yjPWCrCac9P9OkcUAIKWcM9fLVr3sIndtltHVvmBA5galQOej6XYBrXU7sRnE263JuKdF3FFJ6PTjo3V6Z31X6RCG7_9yrevX-xUfilhik96s8aUG8rcdiEvoQUGti5zgZubrDFolHIFiQ1Z_iXB6Uuj4VoTj6tAqXP3ersVtmsNM1tlr02CZv9C0nwzq9uU1_M_gCuuo4IHUFH5ckmtRKiaJw_rRKkQLyObQykkcj6M3pgbK_yGqAdguIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29673" target="_blank">📅 16:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29672">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrY4EzXxO41gk7bgm_uoGbYtAY4jNrbxXQkfuEnpv3u5rm95NcVbXaiYWAsTsjvzCexvYxrHKTWqyLXoGuzDGDuAYoF_Tzdw5iyr_iiFifMulEB2o-OHQAGLjHYDx-DsBgCZ6YRnz3RSNvos2PDLwgRLzXqv7jyGTqrg8rGkdX91AsH9mIuu0dWjSTO2R6pt0ZkGGWypMF5FVaaO-JCoI4xJn1QuIYAWFZQyzRYXFiSbUmxeLd44CK_F2LPRP7FT5oJHjXk_05F5Re8Mk3B1OzQou5JJ299gL1iEVrrmt7oKhG19lz8SmssgeJZzNWXxdoayIpAKq5IjaqavUlcAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29672" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=AAAI5gcidReiDwW9qxRpKMy_3w9HwudmyhHWbb3roADefNLjMxv2gmuSr93BUlOrfO6Thi71oaR9nbn0EUjwAClWyRgv-CEtNYiv7vaT2cGuIxy32uoPGcJve3bpeYZonuoRMjbytounbuBOB5eJaUiqBuNYmE7Rl-SOZXjOTf8SjhtUZpHSwdVXaETroG6yrn-SF6zD79iteFRmoUz2qDR5ViO9kXL4zCM2MthZrMMUZrFGsw9o-9i_nwK7YcC093miQ_29aClHNRf5ESpF5iVrCUIATZ2A9lTKorToKJDcBlC2_2zK3CmOowGow_FUjUDNJYwa4vanU3M_1RgxdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=AAAI5gcidReiDwW9qxRpKMy_3w9HwudmyhHWbb3roADefNLjMxv2gmuSr93BUlOrfO6Thi71oaR9nbn0EUjwAClWyRgv-CEtNYiv7vaT2cGuIxy32uoPGcJve3bpeYZonuoRMjbytounbuBOB5eJaUiqBuNYmE7Rl-SOZXjOTf8SjhtUZpHSwdVXaETroG6yrn-SF6zD79iteFRmoUz2qDR5ViO9kXL4zCM2MthZrMMUZrFGsw9o-9i_nwK7YcC093miQ_29aClHNRf5ESpF5iVrCUIATZ2A9lTKorToKJDcBlC2_2zK3CmOowGow_FUjUDNJYwa4vanU3M_1RgxdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETSmCVRB7EHofBt4wALdu0MhRL3ehTnVTYPnE36hUvNUT8Vsm6rAYh7_I1PR55GJFMxHiGg_qvvJqcjoVSCK0w-jrcwFhxq9kS61dQu8EJroY7ZKQFqydL69wInWCX7vUMJT3X8Ubj8qwfeVDMAcDSOY91E7n7roAtc6cyG5wRa-pIlLtjNP1km2mhfAOLSgz3jKiEEJZdYmSuAMl2RIN7iPuqSGmQxYl5o5DFXzdgyHaUIaP4ccLLWSLe3F6hTyW34o7Q_fknQrOghh5svTpgXkRlCNbSa1TCoFlcl1zTJ4V-APubIDfILyqD8i_isR4ed4LJ-fIgc8T9n4MdXQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFQSlNUre3Z5Gyf2Nxg5MDYXqtmuqJeHC3Xne6iOsZffQO1i3RyeV6FcZBUNJyyFIQ-KyP4I2dAcmlVu2kLL3bCtqsbryw1JpA3rjHF6oSND4hj3NfNnjrxrhz-QUkYSCEWUAk2S6z2M1s97a_3mU-WPxTnWEyIOOwj86U1BIHGU8CG6GDkVSi-QXTuPL7LFIaV6aA9APSxsqtNIVim7gKPq04WDBMQE8HgM-Fy0Le7xdDyTVPadmjdHA6iZuRTshW7FIsAmwb9gcCQ-CS-F8M2DtRn8Ai4Y94JjEnYlg6Mls16-ln8ZrEtZ6YfVLA-DH9LbFP7bWJi1bu7gnyLUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg2mJIj8u5dcwh0D8_TfpWEXzKKMcgwwCoy6up8jTxjj66wv5S2IhsiwRYCISNJAnthwoptuiUzWMdqjMNB4qLD3iX9aB2xk3oRkvden0fMxgLLdMUqZOEbdeQHo3sXMdVRYrQE7s8iw_MkB9Y-096oX7mdTqz-b4UB52VZRpCQHV9rDONJuuthXxXKQGgYaYza7JBq_222THCdYfahqcpJVt8SjX5oAK47Xn2Lik-etcbuBrmUojxIU05yA1vUKWexZLmPXxtcRd8Wcetzn_FrxDUaZ3fVeo3DBjhKwPiULWqSW4aD8uulUsRqu-iX4ifvSIg_UtNP0CAHjcI5ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=RMKhgJxBv4oTEN0rzMxcoYhjnShsFzUwbHyrnrTwhWXthp57ExFDFBgZCXIqZCSWelsiSyjO1iALAFXH1IaieTcq74fzAEF3_NwpHEqh6tbjTvysxeZZVNeDsk4JB08SnbF9S5WufVv1L-rdn4fBem18U8vQv9RAet4oXnRkaMiQjkLyjK2tZJM_NkB5cnSCWA6OKJuQAfwCekbxKzxhP7m2zpiiE8kSA-6OSXm0PbfvtmfJk4F0ngrHAuIU39QIaMmWEelrrDS0PlH5Zs-wweHcs6WNRXMvkZ9_DVIUQVpuWADgLvaDT5hmvt7tWxO-Gl_Vs7dge17YgIN2TqF7hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=RMKhgJxBv4oTEN0rzMxcoYhjnShsFzUwbHyrnrTwhWXthp57ExFDFBgZCXIqZCSWelsiSyjO1iALAFXH1IaieTcq74fzAEF3_NwpHEqh6tbjTvysxeZZVNeDsk4JB08SnbF9S5WufVv1L-rdn4fBem18U8vQv9RAet4oXnRkaMiQjkLyjK2tZJM_NkB5cnSCWA6OKJuQAfwCekbxKzxhP7m2zpiiE8kSA-6OSXm0PbfvtmfJk4F0ngrHAuIU39QIaMmWEelrrDS0PlH5Zs-wweHcs6WNRXMvkZ9_DVIUQVpuWADgLvaDT5hmvt7tWxO-Gl_Vs7dge17YgIN2TqF7hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=RrWYMJEXcNB8d1D8JbqSCd86UPpnvbuUFIkpQGc0ZDcpLLh_D_YDFXmdspN8WhcEzyExEYLjBwLXpaLTpUZ8dSwo98FV69dBpBktVZ53R2yVqR3bJFhSu7aPNuxf9kRjL8yS7OWZ6a33y2ax6LimxX_HCg3zkKG3A5oglQxgpUPrtoczby0B3P_ij6RSBs4_YnX7xXRd68LSIUoCPSKsP4v_DzA4-V4sgvFmORsbjj4izMMJ8VJUwneRAHPxDlyas_GtdoFkPbMhCcbDjCQB5epWRlLLVoE3bNTUkO1lH7jIgjLjwt_BZqFx5UQCMa5XB18WulBTu0IvpcMVBvz4ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=RrWYMJEXcNB8d1D8JbqSCd86UPpnvbuUFIkpQGc0ZDcpLLh_D_YDFXmdspN8WhcEzyExEYLjBwLXpaLTpUZ8dSwo98FV69dBpBktVZ53R2yVqR3bJFhSu7aPNuxf9kRjL8yS7OWZ6a33y2ax6LimxX_HCg3zkKG3A5oglQxgpUPrtoczby0B3P_ij6RSBs4_YnX7xXRd68LSIUoCPSKsP4v_DzA4-V4sgvFmORsbjj4izMMJ8VJUwneRAHPxDlyas_GtdoFkPbMhCcbDjCQB5epWRlLLVoE3bNTUkO1lH7jIgjLjwt_BZqFx5UQCMa5XB18WulBTu0IvpcMVBvz4ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGO3IgPeVFJjLje9UDVCwPmgLlWoDhrG4pFFeKyeuGwRJgZWGsE0gNNIIHSFbuQFKAXyx3_vaIYfBU2UlmpSKmRmYSGalmSC7-F4AASrDih5CXaWsIB8I7dU0tTJ3wxTyljazX6p4OIXE9EbNFPrxkcbRrJNgMyGQ_x8Y2gwJ0IoLvcqLFmFP9dSFJ6XOeRwBdTdB-HynISlycsYZyWxFD-1wPjlwW4BfsfrH8ng2NgFdt8Kw8hJrnI5qmKBSBkDtzawi_dbgl_wNJcstKNolzEn6phjLXYJyfUJ_vEB1I9Ht_F7G1--L_4vT7lt1LbAOOl4e1T4bi9Z_og3TqaAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG6-Rc2EujXzjfYTk259m3-ekew_BpOa4xwuK8ESXoOOmXVFQHGFa0jPG7EJOsvSsNaJRtvgNBYm0WYWCXt3uqMD7xXsRkYOpwhioAFFN0Yng5ACWg3cpj5eh3WwdfCNu6WqvQwpYrKnJlXawPmp7D1ihmz9McoLpqyhG4EynBEgCYonHkj8ynKVCh3dSGHR3I4w0HeBp3tTKExiuvBVPYR98Jec95egZjVSJthC3INBH1ItV1VROPRV9sj7J2yKVGMs6MhogDjRYel9hI5RQwpLAxZeYrdrrIr0yb_B4QnuXe9TiHgcCPp6iE7qaNrjcNRhZa2Ru48OzqyI70DlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXfBEzxNnr05LYD0sgVuCQ-GY5W7VqVCkPiA3LgeYJil1wCn-pxgX4RiO45PKK9CbNBTVhDpw5_Do5axDaR-NJH_v7pXz5eBQJ24w8C2IkE8CfinDmrBuG4kvIyL8ORp1PAe9hBcE3dXdRv5yiqC2ZfsdZUP-Ti3bScEDa_d5ce7nQSm0hemFel60N-LUWYG6XZWufbNBDuHkbu6L8ToOYx8nYXfDZNTRZe3bA-xdUPpG0EsEbqAemHRg-MtzfQ8Tw5aTMb9m77Ii0z_f_w9tTXrw358qCF7t-4r07FyH2lDDSVZ_xJs6LBbwcNrDaDf8toOnntLA2QSheHyGvKdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmmZUAOCbvA7MewvXEoYoC7j2Ke86taQIU6zXBbXZ0Zq5v-2pwlNRODeprxhYwgZrTZjTk0564XMW6-zRTqmWTDDlI4sBB7o6p3kr1xcKInsVjjXxRLYQzozx0FRE_OfnwYNK__LoEWB5G1y8sk-gBhylwBlg-wNHANkAQ_IUqUMaEilnARRVADZEA5XQlU7lx8G7KhVI_WoWh_OOB_5vzrBXg8KsxAoVameM5pQuYHtCMgnCmWgBTCPJDKEurgqFR_MafDHPDZpIZQ4ug3BrYDt13aItjAK1N-VtIoanfOfIuKvv5I4pL1TpRrHcVS4kzCtAC3PU7pkLhd3cWOXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BItISS2hqRiccSuQl5NC1CYCh-GtKBM52mneYAv8GnZJhzjNnop0oEnvVn2OMt1sMu5Fuo-_hm0XhWHDF3QjUdy-KEp-eoBi-vDGndxO_dN7cWl2qjg7mH_yhdHJHp37Jqbx8X3dsYTl-jUP8gyVZmEZNXkMT1UCkZwRi4yLjFmlbT23jxuF8rjYBgZ4d_lOI6KG6JAF151O-BH5rEWcon7Y9Rxv7ewyoid9GPHMDXU1cHCaTtEgSSgDy33IJPSq3_oK9ERHwGtnZGhxpcWmeTnGWci8U95rODTsmNyOw6X_O1ixxKo484fSsMzTV5QRdS4i1FXoNhpSll5h68VLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=HXYrVj4tjE_6EL51RMoa4u-98eKlTJPxvnC-3yjvaiXpMF9oXw2oGe9Nmx3W6mbSQbPaSalLBHuXZDqHdIcOZxscaRp3G6mj71E_gkTsBt-g6jikreBCzajsIVt68bqYFp7A1TD4vgy56wey6wKHgbLgwvCcThjV6gjH8cqNHIbQfWsvNB8YJ5yznMBv9vOm5l44l56J1lVwOFJjFcX6O7LMwytPX4QSdTeMcxlV8iQcBQ9d9If2m6FZL0H4EdpvDhHRVZMechhQAqLmOQ66GZ3eMECdI72CCCkXOgwZwWKXUe8GSrKzK_tkUBGejZptOmf45ZKJzD3POvkBQRE08g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=HXYrVj4tjE_6EL51RMoa4u-98eKlTJPxvnC-3yjvaiXpMF9oXw2oGe9Nmx3W6mbSQbPaSalLBHuXZDqHdIcOZxscaRp3G6mj71E_gkTsBt-g6jikreBCzajsIVt68bqYFp7A1TD4vgy56wey6wKHgbLgwvCcThjV6gjH8cqNHIbQfWsvNB8YJ5yznMBv9vOm5l44l56J1lVwOFJjFcX6O7LMwytPX4QSdTeMcxlV8iQcBQ9d9If2m6FZL0H4EdpvDhHRVZMechhQAqLmOQ66GZ3eMECdI72CCCkXOgwZwWKXUe8GSrKzK_tkUBGejZptOmf45ZKJzD3POvkBQRE08g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8iyhbeOphnqgsSZQ_FIvKCYbWemRxW0U9klLcebHfk7yMVNGBvT_g23bZGTk19OjKzAxJ5wYb9JXpNxeeONN_Dr_TJN77oxHFMvHyGbASV79NIUGIAkPtMbM9fmYcx2jSpajslHwY6JHr1JBHnPOCNUJpX7DJhi41c4ulNkamBvyd0s5xWEl4PA8WSlaLetnNgF3x2JQ_C4SZBIZxNScAJJJ9BK1S-yq2ivJrkjw1wqSztyz4Qid5xSmcjjg3SiXuYiibo97mH2G98SGnZ9EEYQCYeEe-YKEecs5xF_IDtYVe5GsGWqyOdAl6DGpi2FClWXDAsCzdAuB3zDhVSFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=hzBPuv0FkgH4lu7D1AR1xfTWlHqboluoh9XMiiw9btZBhuaNUDVeaNkWhJ2VBGCSL_vFkkYN9znOcbMSmDP2a7D1uSU2Lb9-IWJ1wSzMHjh21M6nck3eDGh2kQwIdmXiAR5-zzvN7_-glPxlr_ly1eFJurRcbYF7tF7CBKz7oxGYzxi1ZlD8Dh9pLPzY6y19fMulEtB7xM1txdbxyE1YjbD5L_-gfstXVqwcr5apgCe7s3-rRuQ1vU6GeAIVM3Yj35epHfGNy3Fr7bYDt-Eywpoj_v7QjTQAZXIdjyPWoqn6fcQ1ZiqgnpeSmif3VNducRVWVMmh4xRyV0GodPT9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=hzBPuv0FkgH4lu7D1AR1xfTWlHqboluoh9XMiiw9btZBhuaNUDVeaNkWhJ2VBGCSL_vFkkYN9znOcbMSmDP2a7D1uSU2Lb9-IWJ1wSzMHjh21M6nck3eDGh2kQwIdmXiAR5-zzvN7_-glPxlr_ly1eFJurRcbYF7tF7CBKz7oxGYzxi1ZlD8Dh9pLPzY6y19fMulEtB7xM1txdbxyE1YjbD5L_-gfstXVqwcr5apgCe7s3-rRuQ1vU6GeAIVM3Yj35epHfGNy3Fr7bYDt-Eywpoj_v7QjTQAZXIdjyPWoqn6fcQ1ZiqgnpeSmif3VNducRVWVMmh4xRyV0GodPT9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkPwA5nwqSoJx2mUI0wK6BDStIS57800mm9wlmu0YnOYpd6jIIi_Elna6EQtqDHbj_U17VqtwypXoTw7JfaeCmEFjvph70CGaX_S2xLhejWqTB0ERzEI6jQhPgOAEusGhI-e91hDw7OA1C6jiH7ftFHBxQhijtof-wziH6FDbRnd5wwpE3yLvEb803Ds16SmIrCYMmKCLtSk566UHFfJjD5b-Owk1LytExRBoGld1cKeMO5TWuwBSRGdZjp4BO05setwcJ6y9k4T4PLRBk_IuHZ9l1bpZw_HNMZQWJFv5LUUo4UYxVuoDafxGzzyeHPHwfGg4-SeIC68U4kCYYFHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRBpDIYfFmsgXzsxDHJav4psiAgdNmj64I83YRKZ7W9qGpk3mmYRyH11jRv6vLndNWPjKq3C0d6Y7CK188T_UBvGfdVyPHHDiDUVjXIDxpDPxdg9YeNldjBMpsURnGkTz43Ul-K4wfIXRSAWSN6QYt-uYRSvfLW3rM7MdV4dKyo9BNEZ_GtZKQzAMpXdh5grGFE6cFej-u4mxpMQRiF4Vo7e0PZlXIhth0EwKOJHbDuAPo5R2-5BIet1f_mPU5mZmZoU08WJ1bz75PYRlRX_tmtHJ7iKuD3tii_IhsFNg3eG4pb3vryrMDdsxOnMckcFob-IZgO-b-4Npqalv6BdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29654" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCXF30W8ZbLiVFDvaCngWCM0au3vOFCot2fd9eGgZ4DPtxQ5dKaB9EGFlwC9wQVT2XfHY8vS7VWhH9-3iR2QIREg3BX9HPVQJhOWC-P69j7JFHPVfKJp0okU48SSIz5qYgeCw9qa0nWpYdFhhcumGtmsswFTV_R3zQ2p_ukEFf2CtnIkFFlddpb552KecxJejQEf2XZ9WetnvRYNu7nPzDoahwji12pJEgRqY0bn1-EiDBKIHNkeoj6rDOorlgHTQbFOXCE1LivAnVVdhSvizL5ucEYtgt2_zBJo7uZ6IbfpuPmpInCyAhAivfHAk_PhvUrTAFG7tyzolmAzZnf-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
#تقویم
؛ 138 سال پیش همچین روزایی اولین فصل لیگ فوتبال انگلیسی شروع شد که به عنوان اولین لیگ فوتبال در جهان شناخته می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29653" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhKKmdnwL9mliIWqhmrW1APJV0K478HgQnV2sxAly4if-mxwG15rG_w9-4AoM_sBhc3q713WlcLbGfbHN7BBrXlH3DOGl-OYivqU1zN_I8_2S_GNdZEQTtVo0eTsPs5ueXr70JaheKAz41DVyShBLqWjZFruPPS4HGaD_TCxMQzlEzqjORJXpCESXDaMgzDls04KOfkSjissTNH03LKMOpFqqEB8OHi0Zk7e8EjWySgemy0_IB7MoxBSudjVGBL2mZE2qqqi_NlWNGdIS5i9RiBCTCy5LYE006MO3YTQRkXCxyvYXpSm1UfmPDYUSKHYK1iJC9ZcBAX0WbGNlsvUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=dYjRaiQnFsLsXYdR6VX8xlfSgFKvRa8v-yymq0haRWdwIXauc-3XEvjPj1nYnF65nXPLbFLd69i_LxXeoH3aD_glQyG2Y5oy-7sWvc08iQtqWJCaGI5_qkLVTjiyfJrgT3yP6XNd0sq1Q1-5rOzTN7e9DuM7vSzfKjrSfHbT9DSvUa9UuSI4YMOPaiUZEYKELv2ceUlTfRYv93cB2rqAL2HFzjE0bwVW_2SDdCDuOf48Zu1xCUxM2rOoC3WmSCH_hYWljOgNpiJpJ9rkj23JsI_tyKgwd-uxmDk53xb9v5frdbN4bTaBJBSZ-2_QKdBSwEgMt62qWl3VWFpdgfUtdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=dYjRaiQnFsLsXYdR6VX8xlfSgFKvRa8v-yymq0haRWdwIXauc-3XEvjPj1nYnF65nXPLbFLd69i_LxXeoH3aD_glQyG2Y5oy-7sWvc08iQtqWJCaGI5_qkLVTjiyfJrgT3yP6XNd0sq1Q1-5rOzTN7e9DuM7vSzfKjrSfHbT9DSvUa9UuSI4YMOPaiUZEYKELv2ceUlTfRYv93cB2rqAL2HFzjE0bwVW_2SDdCDuOf48Zu1xCUxM2rOoC3WmSCH_hYWljOgNpiJpJ9rkj23JsI_tyKgwd-uxmDk53xb9v5frdbN4bTaBJBSZ-2_QKdBSwEgMt62qWl3VWFpdgfUtdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=DVIwSgoj9sgzoeeqCHEXZihOdRWN-TWOD_OnsA1brNVuKG0xls5NDc6yMShe3421njTcHJoh04naBpf31cCXzvWbNI8sEAsBJgcsZ6IHp5cDQgFlAqIGQcVAxB8ifq26nobT8ptaf4bYzSq8duR7JkMJ-hkcormPf7WrWHbhxtWwoa3mSsEyxtCXmTbZGJxz03scwfNr8XDw7KuDHagqZRzeEkms_B-oZVmdEq83SrhSR83y2pbv2gfskJpHCM1hKsafsIgysLZ8T9uos1Vpc2Tn0Ue2M1nCFWi75IL17lG5eSfXEyxN6vrS2fTnyD6t5hFkKlHlLPk2bad6a1av5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=DVIwSgoj9sgzoeeqCHEXZihOdRWN-TWOD_OnsA1brNVuKG0xls5NDc6yMShe3421njTcHJoh04naBpf31cCXzvWbNI8sEAsBJgcsZ6IHp5cDQgFlAqIGQcVAxB8ifq26nobT8ptaf4bYzSq8duR7JkMJ-hkcormPf7WrWHbhxtWwoa3mSsEyxtCXmTbZGJxz03scwfNr8XDw7KuDHagqZRzeEkms_B-oZVmdEq83SrhSR83y2pbv2gfskJpHCM1hKsafsIgysLZ8T9uos1Vpc2Tn0Ue2M1nCFWi75IL17lG5eSfXEyxN6vrS2fTnyD6t5hFkKlHlLPk2bad6a1av5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgHPM7zMsuEhbRhoKX936QVsb8sqj-AtX0cYsRvEuD_O9CPaCio89F61qNzTI9xK7aVWbsZ_KMmlhpuRSqe6s1aFXld5G8VcoOiVJiAfxtfX6Fx4ZRe0fg_-WQAzkKfQHB3ZktqAgFMgGVk_8vFxZ-RS0pYagcB_exTOEzzFDjHpjAEgKBugOLSOAKE1MD5Z8WsNilQpMhfu-GNkMD99cGC_ghFviIZG9rcWd5X56tg1_4Fqh-_adJ5hYf6DlCwrBAYSpttyFGyLSOmx4Pdegj9tiqwRy9qUYbNE6BognhwFHwD2s8KSXgSaD5Ph6jjD28GK8mWSy3nafBX_vQWQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGYtCe3CfGLHZ-YRzBksb5Miilt6VDo3wcMznKqM-irOVlbH0KrLFwJjoXEoMBgOIvZFgYpFMefCkXCH-rCjm-RjcAFJ5eAOChx0O9DNz2Rc9x8MTF7NXJJNIX_3IZXZTKk-rYGAHsTM4ui-ts7rabt78Gjib4jsjejuzM5WcXKPXy4225Cxw5CizliUqv7eaeGmPdXxO9K1hlT2wchEvn0WZuhQYVTqzBPuV6TsrArM3ukqi42XZsxjY204ww9sv92iANJsDXG7b4FAzxbmOxwULx-kfCBBUEhKX31ONXhQ1Fht7HF658QBVxxyZk8MSXFEa8J3mQ8PWmXTZ8MQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzwmOsnxUq24eCZs-nH2mqi1S4jqoY3PE-ivc0zYcH8jWf5ulYh8d3UaKKR84IIMS4ulzv76i3pX8R8WBgz_G_2x8lxPtQjZ6jreHY9WhR9Gx8efGmJWi1GbyOU1zu1JupfFkVdg7JOREcgJnoCPu7C_2aFvrwifF5KlLytLuwcusAW2Ey4-Zphu4iBTd90wqqeoGA_9-SixmBigLIaDoc1XmQ6eeTezyVpwlYhrBu-7w6qRbmUYbKwRnSwNN3KJnIaMOdo8c_c9z1-LM1nAbHZ9_VPNboImHVqmJD_fyEInUOmiQnUuwCh1tL9JlXCrpjVLsCneirz7c64EcvY0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmlat0y17DJbN552Pm9X2StDlPvQnbWnxr2a3L9Ya6ZjWZsNqrsKxVqVZcY84SAcF3u63Vw_QEqSIKiH_8N1HMc3mDPe3RMO-f8w3bqCyy0hrTL0Newg4H_wjxz4bNSHgFDZ0OX7hqTdjxuXuCEg9sm1LujRgZQdQv4vfElWsmOuQHxx88Mim3nwQE_utkZyCRn06vd4vaRptCq9VE9uSq_hrUgWGlgOCKMFL6r3fpNMSy2-EFlwHLo2eI8r3ka5DaiZ4ASLDNVNVU5Ll_5aRts-YQGOHIzypqF6WGYXGnxhF_5mmyWFhP9jZ_cadUs-2u3PC8meARusMCHVJLm4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=jtjNrtMKoEhNLEq3yk0ChorMAKv0cboQyjMPozBzNNlnNZhYZSsdQZzOptKAnPMsYkTWnPOWMkVXNcewnUmOgaa7y2sry8-EoI-xKQNNHODP2bk4dx8ftSzTCKYYsCqRcoHowb-10l8YB_y8daTeRUkQ5k-BL48FjhfIgxlj4GbgTzimyJA7vuzNDGqE5xYF-id-RqsGCO9yDwPBAWNP37nwKiX7scqP10xORePPQLMjhAaeerEFmW47vTTmhYimsDmcMgwQVj0lpP79xZe8C87z55f6hMPxzr0kYLOa6fStXTnL0WdE2HQ0U0_sL9Up2DS-jKCpRcOS-MC1KKnb5UNPRHEHXiYg99TF0SsUwfkI21_EVDMue7n2doJlaClGy8Ijd2owfd0iyzEv1Jks_wOgbF92VeClCx7k7gaAGn9hqKadlGxrOm5Dv5E0uiCIO8dAqARnClhNzo76OITXBh-RmRTVMbiF3HuJIeu5TUYE_-3sVN98necPkF9Q1pKAzrhmuZ5K1X4fkAre3k1FwY0AKZ11TaH_uQICmi48U9DpqUsoMRkOWJ-kPmh1ervLh9HWDW3mKJNfzEt0nN9PH7xh1cT-kF8ddxJhdGclj_P42Sqrbz_ZW96ly3tOoH1ktgWfo7vmOdtII6OW_Zu2g3AHbmHbzD4xDxLF1BjhKF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=jtjNrtMKoEhNLEq3yk0ChorMAKv0cboQyjMPozBzNNlnNZhYZSsdQZzOptKAnPMsYkTWnPOWMkVXNcewnUmOgaa7y2sry8-EoI-xKQNNHODP2bk4dx8ftSzTCKYYsCqRcoHowb-10l8YB_y8daTeRUkQ5k-BL48FjhfIgxlj4GbgTzimyJA7vuzNDGqE5xYF-id-RqsGCO9yDwPBAWNP37nwKiX7scqP10xORePPQLMjhAaeerEFmW47vTTmhYimsDmcMgwQVj0lpP79xZe8C87z55f6hMPxzr0kYLOa6fStXTnL0WdE2HQ0U0_sL9Up2DS-jKCpRcOS-MC1KKnb5UNPRHEHXiYg99TF0SsUwfkI21_EVDMue7n2doJlaClGy8Ijd2owfd0iyzEv1Jks_wOgbF92VeClCx7k7gaAGn9hqKadlGxrOm5Dv5E0uiCIO8dAqARnClhNzo76OITXBh-RmRTVMbiF3HuJIeu5TUYE_-3sVN98necPkF9Q1pKAzrhmuZ5K1X4fkAre3k1FwY0AKZ11TaH_uQICmi48U9DpqUsoMRkOWJ-kPmh1ervLh9HWDW3mKJNfzEt0nN9PH7xh1cT-kF8ddxJhdGclj_P42Sqrbz_ZW96ly3tOoH1ktgWfo7vmOdtII6OW_Zu2g3AHbmHbzD4xDxLF1BjhKF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdPg-OulVNJiZZ2K8299S0rCKwCjR96fTspWQ7W-hxxlaEl30IrLK_9SVmo-8na8tKoZxXPiRbc0S2MY3BqpWSsuSSk5VvmyCFqQoKN6LV0D2rncw6YC7M5lnm8rPxmgk3IQjKwuQxN35WYNpxpSM4k0-Kizc5Fr3w5RpslLj8SeBEBFUZ9r3gwzHgFqTO6yfZRpwvtix5JkQkil-FgvWjEzhqo6AdJcH6d5UegKC5cYJj9FF0ryj4pF7o1G6mLQLVJ0PN5WJF8oMX9-vZp5O-K1jTkEF88XGktHCAmtK9wacZ5FwPztklXTge9yf9Z8auA4i3Frf9OAZ217Uyuhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhS8fkqlaqEln8vAkMHkhKGS_yTVUHkk1pxlXX1dblljCnK1VsTFe_TzeNaRXak--VkudDvjfQAM5v09sZI2hXwZfv1cc78EvzpQE3gQ0Cs178KtMFQZjk_KnVstt1dBD7IDDW_OF-xcH1IGitkdUg_WCBeHWFRZv3rx0IxcPennjy_YI1YKI_gkPkho9jLn6Dkwl_gDXVodmfCQ1H-7g78ZqTkz7RneOKKEmU7XWacb_DPdQDMU0LOT81ZozmbJPds7Wp0igFPLN2FShKszrMTQFwKIacefw35HEkqNbxnoaNfYXdsfqENo-tDFj2UEsTxUWUyzSQHqHd9JnIzcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No-3u_hldEB1GSA8eay6fFYdWOqAps2W_C0mL0lV4kOeznVBD7EHUo1UWaKtyT9s4jP4QnE6iUgsSyFg4W70W6_0JtyFU_bE6O5MmHxFoo3vyLCDv6UpYHL3B5q3X3FTULDDeFaS-rBPBYhjhe2496nYNFcesdeT9pbDMedvm1hiI5LsmY3pLKPXB9zX4xU6wN1yyiMHOjrQm9a5TIX3g2uTOxPbSLbXssFmtX26Yo7yopi9u0QacFFFAqy35MLRHEbvh5lk_Q0MFi9ymxkdzYICX34UsGrODgonAcf46QBT4BIoWLwEQkOMGzK7ov0oRlosCDhT2uPIOMJ2_o6okw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
