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
<img src="https://cdn5.telesco.pe/file/llK7IPcic6konEPbVGFxlEjg5XxBRTDtANNjc6nAKnpw1qBD3rJLmwSkSzBL2Fimt7EzXMHkFsnJXfZ1HBDDHHTT_vo6S8de0DXo0RpXETArp5Viz_5_Sbjmn41zy4rUV5-BdG73iXAjDIOI8paJvoEyvbqtGbjNVOZ4KiqKGsz_RGS0XZCuTyjTG-2oyiGkoBtApPEygPkYLwDfEzNhtHDxKbzyktig0B8iE8Xd-JbxkKcscWo4U9Ueua8d0-fZhzW65gIBxZ9vLu7w30nf6YeaWXAuechbYkDyqPwU1Itk-NdvvBLuhBhBsVrwp8QXgzrVbg21dIu4Cw7K0PqPYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 278K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYQMxBzbQhchUlubgl7TyeZGHpHgs1t-O5pcDVEIuzbJ1uP0ti6iQvX2HprcTztTNaarvkq836rfRhASB0TS-ZMViKUBtYs8y-16uRj15bKHeSIAZwCXYwX9Q4zgD82v19a0khzgZ1WdoGaVi5lI4iOL86FxM7ubEwCDs6nTNyTEOHOlRbEBTTwNeg2ZUPH_6TYqsg4TD4XbxmmUsVOWEhT_1C89l3Kj1J2fHdxoVTu2Ql9f2E0cFD_o1a6BHn7VYkWAarJVZjmRffdbR0fWphTAHf9bSBqoC2vwBlbl_PMdqkWd6t_JBSN4OVDKpHBqHHnzbHi4pP7EwRymt-l4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
تیمبر به دلیل مصدومیت از لیست تیم ملی هلند برای حضور در جام جهانی خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/91588" target="_blank">📅 21:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🏅
تاجرنیا و جویباری بزودی برای کسری طاهری و محمد جواد حسین نژاد اقدام میکنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/91587" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQAzSAoqKyxJYwKwrhR_D9jDEH8reY1z7mlRsw7b5fYyjn3HcVsMHJAn2xKVoyNmNIea2mLyF4z7a7fC6OXMd6Qv650G1IaLHbUmL3ZzrvqneK8wgCPZwJH_D6SX9PIM9CO4tVjjPR-4LZXdreg9NVZyilas-w8vmWKHOpg4PvGikJLcjxGL5p4542PjAwT5gHgg8gWRno7PW6xAthVa8PRpt_ZKY-5zmZYiELUFJ4SeocRYqaSXBsWCQBjKYaYTNC1zE-y0TJFqsAI43EHRTt-ivo4EW-_4K_Gh9nIlXqSDcjzhi5Q6XgiE9iKHXEPL-vw_dIpX8_rqcZY9lrqX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب ازبکستان مقابل هلند با حضور فیکس آشورماتوف و اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/91586" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2mM-Y22TbCMpG_sWrKYdoE_8nB9dRAWSthMPg6u-PRtjoQWfedUzgSOVx2VK3uq0uthCIph2XAR479O60g0oa1tv9Q7vGvvGpW8YsRuvLgH-Lc-j9e3o8QjMmBX-EXF8j7lag0anpB4_6GuWKlHVPgYap7csRwop_M7NXw9oUyG1gf6emOYSGPtuP7c_1pn-RlutcB_XU_Slr5tC7-XGIrJhdFqpEPxmbc4E3xVcuEomosFS6c-7OVxWn0YjUHvI04eugUa9asVgsug5RBuVIOfkdUatNpAnqwwp_CVUgx7niVMB7TmJIeBK_imb62CucfGihLwe4EDSndA-ShIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/91585" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlnJrrhLIgfDAE3vxRxn_iPBa2SY0QC0KpQmV7llyLo92AHEIPQ58QcBlBocNraCfWu_BdYeviBDNG590LTpOmfaHh05R8se1glRT8sdDZWUlRePMW1f6Z_wRohIA1RwPKVjFMrHoE-nre4HRfYehU2vrXxS7HUQ8vscqnINQsFEE_JqpovDW63eplHYR12C6UOTxVQdY-eCxq53sgqhyf2YOcFuBir7-0yMP1RHLKHrCEC-02HCDVHacuAqgrP8MDB5L4gJ_bKVrBbTmw1IAj0Zg-9e708wouT-5K8e68GtKFFQiVCdEnTYO3sscYZ-Hqj58nIw6VEM-iCkEq6yJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنایی که بیشترین دقایق بازی رو در جام جهانی داشتن؛
لیونل مسی قلب‌ها در صدر
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/Futball180TV/91584" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jos7uu4iLiL1ZCVPpb0w5OhzM23JG8NvrYMhOIlRU5UB6Zdua7V67Y-KZD9Gtfs_PnQs1zopE7EAayL9qANBmpDIwPbOU3ZGvVmAAVWT9j7sb6VedzU9pAIcRT_SqIX-1uAMVybdlNhX9XUf0ErgYTR-kUqt0NURDuILlMl7cVZA9vAcocgsnXKJbmP9bIWTzSGtM27GCasWRzns_lMwnDPqZT7p8EEU_XNy6LPspipjTLWe539LDSY52g8NuJk3xZriHSvAorJb9sdxIjXw4ENOU9z0dh_IQ9NCfOl0rLv3Pu7B2ogDAlhFqOVFX6ko5RSkUHkoqdImdFvN9TaarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر سپهر حیدری هم پرقدرت فعالیتشو شروع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/Futball180TV/91583" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXsO1rG4LM5H7WnvNJ6LQPHzy-tmMp3eQpzg6loO4asvSn5F0BBXfFraI4jnxOJBeA7Ls6AAI4kdkczjeKc7sDUGafwdLbtjtRVtxvtGBNcQTsSQnacnYtyn-1ivInmVV8609SYpHmONiRB5cohaoeUlDoQpQ6noxLwA7hPP4dBiYk-Bl_UY4LYv12xM6tdNmuCXs0JWB5a418AsKLVL9XpYEFjRqnlwLiojfflXzdSZe9jcLBFRSPkSFlFemE9gnDcLLVZIGnRosmjF7-Xjyx2Rwg5n1ovUF-7QZRmhnWFjgZFIfyFWnx8ACDjqsXuKYMc40g8hOe39H6GdU-q_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpsV37sbgyS7WkTqFSV_aTAfNZL1kqjHm-2msQB9NAMiO2rB0teGXwPXthvhUoz0zPYS8dv5kkzGHKETtFhnyaPPOtVHwSAKcui41JmG2jiq5gHd3D7wE9fzBZ8Y5PRooez7kbvw8LGLudTTzfnnPHBq67aQDRRMq_X81j2z7rZlnq6ipy7REuv__SHArBtsMyvkl78uK4er0WhfBX2m8XGBArb4l9GBQFJ6_ro6K5r2NFzmLeotBrM0i4RIR8ZS6k13W1UtUOHH8tPv7f-hRC0YUkum2G7WFMGjvh0mXpkxM3vZ7jrHf0gAxDXgtjET3JCf_RpeVIwS6xO9FycTEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه. واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/91581" target="_blank">📅 19:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cO_GwGAaZtPbkQ_WUY5WKyOMjkWDfnxLnocuVVrn1hEbYoEcwR6e76eVitvU8aNYUxfRSBHXsPK5TRrOlg6aQ_Pp_SlAW16AAU5r3rHjKTwqZ6tQzZlVss1ArL6hxEMieyW9_JupzclNlZWyKENwb-OQWuOREArjvathyPqVkOfHTKGeDCfSTDjrVeVU_9kjmwBoEaJEGVSFvm6sBFemdyJsghKMRgNg1COToC5jvw7i2SK9edICAJz_C4P6oEJw6CMssmcrH9psxd1FzlwHQGBOMRznpFdF-i78bwYp10jDEzbstZesyYMLRZ9GqRdf2pVB98rYh9XoZf7eo9T80g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cO_GwGAaZtPbkQ_WUY5WKyOMjkWDfnxLnocuVVrn1hEbYoEcwR6e76eVitvU8aNYUxfRSBHXsPK5TRrOlg6aQ_Pp_SlAW16AAU5r3rHjKTwqZ6tQzZlVss1ArL6hxEMieyW9_JupzclNlZWyKENwb-OQWuOREArjvathyPqVkOfHTKGeDCfSTDjrVeVU_9kjmwBoEaJEGVSFvm6sBFemdyJsghKMRgNg1COToC5jvw7i2SK9edICAJz_C4P6oEJw6CMssmcrH9psxd1FzlwHQGBOMRznpFdF-i78bwYp10jDEzbstZesyYMLRZ9GqRdf2pVB98rYh9XoZf7eo9T80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد مقامات آمریکایی با بازیکنان تیم ملی سنگال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/91580" target="_blank">📅 19:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjwDKJUF0tvvR3R1Vb8cYTzTtldQyvfNYqVzx6bk6wF42O0rEzOY7rHfhXIk_HAfrqjXHf9OLjC8eiUUN1njqvnas169B8CAbZfOBjstKCDXme11r_D8uagq_gI2vpEBdcIEjl1QgmwiX4lWAnQpkekF6sHg7qdDZWAGlESJbjdMX5avFXRzGYmK0-lLDLCPMXVkTYSpFMx_hoMxgZL5St8sasRzRTiDrp4FIEGhNqB_y6NGvJKo6ms3Xzi49ZkAra3VEWTzRSn0FQkwEIrsGpCA8AyYzii_BxO4ZoH0YoHKJT2Oy31nJr9W8w6HAtay9RiENxJ1DQYgLFNIj18wlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
کادنا سر:
رئال مادرید پرقدرت وارد رقابت برای جذب برناردو سیلوا شد. مورینیو این بازیکن رو میخواد و اکنون این احتمال واقعی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91579" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGEcqCqxGB4ekNg0ICYXXntf2EScRInG-IyVMYrjhs-FIacaHGdER8Oisnsa337orcllwIYpBWNukZj9Mclt-Aj8OCOLI8ClENW74pX_ceqoyhzEtA2KxygqGpyhhP3SNZtscJ-AoN45hCEsDOpKkYI7aCaLspnQ3Fgg5LLsJCFPYA7fyL-nJVLMrJ3T8StqaY4oL6TvamXPcYMM52lCf9jXk8wY92tTr10efCL-ovAaf2NvBAze7UuP0eJ6OABV2nP61Zv8EroV2OZMsLWlWz3DuLTBbxysNzSWz5nTtUBeMgXwoKEZVbLI6EGuWO_1vJAH6LSJmTZClvjifsficQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYvDDgtU0yS5S1vw7p56w3t-UP-4O0sd3nPD-QHtH605DpTC9vsKSy05pTroaB9iYW-jSRyzniaN8lDDoKcohUQmk4A1sHPIxRTuIkkwXeFDHn1Pd4x2ynkuERHQzn_YXl8zqXZtfB4ALxveZQazbHL8D52r7ccpJ13ENRwAO-OX3JGXdiPQky_IcVSkKEiID08vPIVOPrner9HQq6RBT63fu14nfGxm5J95tpajGZtALXT1hzOumPg9IjuhPdrldBfz9bB5SGrD9BI3peRHTua9hXQJpCM_2oevSZhwebqMrqqmyaFRwE47JaLCRlQUH400P45kUoA2u86M7LFk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXQJL7ObyAVoRJNIoi_wkvROh6cZY_f11TJSL2NIYvO9haWXXsuoyvi2ctmZzSa8YmvY_ebxSKiSo0sl0Hu-aIGTd6gBAX0WLJXsF354cGp14cfHxQuDxBeLZX-VTinD-ujxtmrMgzrAjzL3I7PMPxAbxa4iUO-IMBIVoBh3U9Ywn4CRVAPj4dWE0ZXhb_8F9vXxq1loZ1Lp2XLE25wwn9QXEaLvo43tF7okyHT12XQOTEMGlZNDRNH1PMHQdjciKvFSEBS6G7g0J2F5tB13UF8AfKeaFHeASahPYPuMRoryMPPlRoGXW7-8o9p_miyNshaTAqcE-lcSataBkuLlfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله دلیتای عزیز هم که معرف حضورتون هست تو جام جهانی مجری خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/91576" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=BnFS13c4xBKmxxav-4UqU2eJY-_K5Wh7maCr8VASIwB7dk45wSlTjl8scEIVhRUhwOB3MJyqwBr-1MHqkWbaPSzx-eK4gxqCv4lL3-5pkVnkZwWlBQsAlDOMv-5TJL6MpoX2DufZEgSXN2OrGW0QxzeLo1XTCR6AFGjAI9cNGsu1AmmaY4MLQ00DvuvLEOE9EeMWO4OzOBh78_fqWjzwGE8mBwVQSTAd4MjsDDJMRkb7JCaeBlwDQlmMTrEg2nSl9BAwJg7UkOg7-XPje1FxYH4_pwu1IQHQ7u8P5AfbY3x4lEF2BeMnn4FQ5Fb9YZm-bO0Dm4QHmCL0iCO8nJNVw1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=BnFS13c4xBKmxxav-4UqU2eJY-_K5Wh7maCr8VASIwB7dk45wSlTjl8scEIVhRUhwOB3MJyqwBr-1MHqkWbaPSzx-eK4gxqCv4lL3-5pkVnkZwWlBQsAlDOMv-5TJL6MpoX2DufZEgSXN2OrGW0QxzeLo1XTCR6AFGjAI9cNGsu1AmmaY4MLQ00DvuvLEOE9EeMWO4OzOBh78_fqWjzwGE8mBwVQSTAd4MjsDDJMRkb7JCaeBlwDQlmMTrEg2nSl9BAwJg7UkOg7-XPje1FxYH4_pwu1IQHQ7u8P5AfbY3x4lEF2BeMnn4FQ5Fb9YZm-bO0Dm4QHmCL0iCO8nJNVw1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمار؛
بزرگترین «چی میشد اگه..» در دنیای فوتبال..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/91575" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=Fz7sKZ_3xv7uvncvBJDE1KV4e3YBQJ2MylE9zR4C7QK4jQXUBWJsEneOZRvI6AEWovw269lHAgw-4oOLqU_B_bcvn0lmObim478qcsLU2PT1yx03PuT8dB64ZgRIB_NuigwtjyLkXlpHRhqhn99gW1QQC7_ojAoLsWtUUpwRPqJClggE3v8d3lcqxK8PlL1VLDbS5nn4v5bkV1VAN3r9xlWkUOtMG_R7OoEIjP0Jn8Jvw6wkTeyZQFBEkU_i_gzn6jij5Z3FbF2GLtfnXDodWHsMrAGrSe5lLEf8Wj0mkZbZDvyV0xydjUP9mJ8P1yKkaqycfVPjjmm9ewAT9UkPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=Fz7sKZ_3xv7uvncvBJDE1KV4e3YBQJ2MylE9zR4C7QK4jQXUBWJsEneOZRvI6AEWovw269lHAgw-4oOLqU_B_bcvn0lmObim478qcsLU2PT1yx03PuT8dB64ZgRIB_NuigwtjyLkXlpHRhqhn99gW1QQC7_ojAoLsWtUUpwRPqJClggE3v8d3lcqxK8PlL1VLDbS5nn4v5bkV1VAN3r9xlWkUOtMG_R7OoEIjP0Jn8Jvw6wkTeyZQFBEkU_i_gzn6jij5Z3FbF2GLtfnXDodWHsMrAGrSe5lLEf8Wj0mkZbZDvyV0xydjUP9mJ8P1yKkaqycfVPjjmm9ewAT9UkPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91574" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ear-qgAES02i-wi8gGd-5ijWE6Wv4nTeuGnP5lxth-yVO2RvqC4ghkP8c4VubGb0uueyVLreyD3sfP6OdHTqUibrQ85xrWEnXtRvSBOvPn48hovjqW1o86j15_RCWpq0EaDkwJMCNR4Ohk7DAXL-dDB2XUjaDpwbcVqUNPwA5-JMnPIkN6TnkuKyWIR7wyTXtHq_r6fcdWd6sKL6reLk_pdW2J3FE_ZW_7U8Is8OiZcyOL2juRmbmcupwfdKsCarVdTMVJ_cCpoFNosNkf5ZcTRsw2OqfKydM7x0grNlJkE14nerVOhiRq3J72URH6QTO1egiSRhAIIYSQ6tvb_CPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBGz5zG4cirmzdko-GyhA2z-QUwjjzalDyt2Z6xpPobtrPCcYXrKDhhGa_dVN17DGpX1kDk0RJyNjgd8upbcIXADLY9ywdXPI-A2ip8ZOQGNYAJaJ2HiGWjF8xqUUUw8dScqZYSZAFKqVNiyfjSQwlVJHrbpWuB8BRxSWcbjNN6nD79yDQYrK5aGr_gMu5zKuklFEOr7212m5hL15KZS5xbnUolThiFyW9y0qmmCM5MSN0_h0AwzvhMVu4ipwQznFSX3Hh6JANPxg3bddHdEKnqfN-YxuZyFJYREGvJqlKYjtd2XDWk6e7SUbaWKHOsTliU0vaVEikyIQNSaoUfibw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91572" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwtohqQxgKI5V1yiEnEIpUf3zFfFJxfWt4zTaTCy_uuwaMM01j-Cc7vWsF_fL1VEewi-pBkUyGLPvbjZm_NqLLjb95Lv7FexVr7tIOBqZDnpRwGq1V3sutX_C0c-bXuKxC-i9z_9VrU92v6iQEpzRN1k-jCYIBcRNE4tdLkrI0JtrLXjkVVNZEd9MDXHU19-k9-P-5afLJlc1-MEhUCj4L_QzHY5quku46wi9KILDbvzrrSX8jSvY7dE-TjLC4txXw-173R3zfMsNXTEqJjpUTtoj-vDszQQqffQSTg6cbu7Gwn_vfsqPrGPOvd8RyUv7qGSkmT97a_gPuhbqvHlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کروس : بهترین بازیکنی که در دوران حرفه‌ایم باهاش بازی کردم بدون شک کریستیانو رونالدوی افسانه‌ای بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91571" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Reigdnfjltl9JOSMn04Pc7fgzNrZcqKojtCkedpaJ-_JKqssxjIDipBs5B1QTNbEwKjWrQXtChH6uzJ96QOo41ogTKda4Z7gba5Im278EWqaPPmh5fBLvIjBK8NF7157veT447S36VTFw-SndvE-wGAYJ71wCY1-N1-GrUVHFOhZgRJYEMaKSW3hH4-LElCnYZxAVEusKMOlG1nZCBugAndcgPna-myqDAlHQL_NbTtnd3fecwi9Qw2LQmZu3k4SezZzI7rPeHbKUYruxmYK6aq5dUh7W249hmK5b62xl7GlM6rc148PDDePRbJex7aleLLITZiCKl3a3-2T2pxFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
دیلی میل: چلسی ۱۳۹ میلیون یورو برای انزو فرناندز میخواد
🔵
مسئولان چلسی
میدونن که رئال مادرید به این بازیکن علاقه‌مند است.
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/91570" target="_blank">📅 18:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=mlEtnGSB-UosBdDcNQhNr-WqIjpmuzLyAhFY-ufZjgM-QCQiaydv6wawWTj4-1qYzYzASSRYt66-FddO1T7mCgdUOJA7r3Uz8BoLbbqo7mRpYL7C1CgD_5prtx10NsWCS9aAN8ewzVY3kzPisnkKhbUIv8VP7nXeLnYhJHf3beUgPiKc0X9vFwCt82T90u-rRqcIcd5ls1CQdcoBK9DGnk35vsFpr7fIEYP25oYuI3fULh5CWksy_5yi03d2OuHmWn-6NPhx7M4PU3X2hCF1nSqJI-GGvgvtQlqfX07wv21nwZWRPpJOTnlKK7nMkBZRgwAfwT9d2ewBi6jVsLKqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=mlEtnGSB-UosBdDcNQhNr-WqIjpmuzLyAhFY-ufZjgM-QCQiaydv6wawWTj4-1qYzYzASSRYt66-FddO1T7mCgdUOJA7r3Uz8BoLbbqo7mRpYL7C1CgD_5prtx10NsWCS9aAN8ewzVY3kzPisnkKhbUIv8VP7nXeLnYhJHf3beUgPiKc0X9vFwCt82T90u-rRqcIcd5ls1CQdcoBK9DGnk35vsFpr7fIEYP25oYuI3fULh5CWksy_5yi03d2OuHmWn-6NPhx7M4PU3X2hCF1nSqJI-GGvgvtQlqfX07wv21nwZWRPpJOTnlKK7nMkBZRgwAfwT9d2ewBi6jVsLKqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
هیچوقت این‌صحنه تاریخی از لیگ‌رومانی فراموش نمیشه که وسط صحبت سرمربی یه توله شیر میارن رو گردن مربی و همه خایه‌چسپون میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/91568" target="_blank">📅 18:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LVv3mYnZM0pTV8eLFkpZJDdFu5MKVXpA4gNRs4TogdqAfoR7OaeBujKiuO0ud4CLprZwBEXGLCHqjA-bO8IHbp81JExn3acEIgrO_-cjyDSpv3Tk5HpbC3wxuqy2eATdVlYEDrLRrnADXKR2zTpL8C7X54iDnHR35UEKwytbk4NQ2-9HwegbUfSB-c5QZKPdhLUylIUSH-ZcTQ0uBKfClH3VvHy7Mkl9flen1CBKLo_clUDHcf7sQV0IyXmSsdtvc_Qf7HKvxtQnU-53wgZVBiqzbUKKNzrZXc2fM2SeYW9uepjQZ-MeHAsW6hnG3NUBImbBNQE8oIGfWIIReO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه قاب تر و تمیزی حاجی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/91567" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=Aha_zYRDQzqfsGCoqZRHNNDyCcffW4nintzNHIu5VQBpUEXuArOaZ-m9UWvzGrCPFMoBteKN8FoY6zrKA-4NCRi2_fD912HqBqmepFIHbDbnAo1GwlYYqxiFEVHxXkudCzgaQjHcB5MC7DkfXqrdBHdo-gfvgSKTL0reTiBL1OZprkVhQKwRXH4IUBFPiExV_fakb8JYldKQsIOyEA-IEYkraSUWiGWKwHCr_XrqO6S7Yi1gq8paUdtYduePbis3r7MAtVRp87R6L5hIA_ctblZKOXSSVHLdbDNxADnzAJdGo_1F8dwlikxDHFVczQwRxdeo5FZz4YNeJWUh8ayXvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=Aha_zYRDQzqfsGCoqZRHNNDyCcffW4nintzNHIu5VQBpUEXuArOaZ-m9UWvzGrCPFMoBteKN8FoY6zrKA-4NCRi2_fD912HqBqmepFIHbDbnAo1GwlYYqxiFEVHxXkudCzgaQjHcB5MC7DkfXqrdBHdo-gfvgSKTL0reTiBL1OZprkVhQKwRXH4IUBFPiExV_fakb8JYldKQsIOyEA-IEYkraSUWiGWKwHCr_XrqO6S7Yi1gq8paUdtYduePbis3r7MAtVRp87R6L5hIA_ctblZKOXSSVHLdbDNxADnzAJdGo_1F8dwlikxDHFVczQwRxdeo5FZz4YNeJWUh8ayXvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نیمار جونیور ورژن برزیل در کوپا آمریکا 2021
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91566" target="_blank">📅 18:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=TwZb7Zpnn547rFMq0tKCjB300WCfAitQ4uh5D23eAu25GOwfWUyQRYRXK_QmVVe2QVOJ9wndcGdXxfj2z9JBVW-d448CVROugfvgBu0Au8Vc8Pcg0MmQUTc68rlf2V_yjAhiORcjX_7Z4RCo7dv7v9_xk2aY_hmoX0TugQkwH7quFNZvnCYLT8DHdjUfA8CtSCjStKRRzWBPHKb2kFIBbAHEKVeb-iWOy7FlXB-uGOo4btdijNrxqfd5_TMyMphlEomOao9lyC9FeZZALOoh8h7-QHn-nrpNk3QLeyyr4zSQ2rT6jjWUUvgX26n3qNt8KYxlPwlKgrO3Mye87-2yCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=TwZb7Zpnn547rFMq0tKCjB300WCfAitQ4uh5D23eAu25GOwfWUyQRYRXK_QmVVe2QVOJ9wndcGdXxfj2z9JBVW-d448CVROugfvgBu0Au8Vc8Pcg0MmQUTc68rlf2V_yjAhiORcjX_7Z4RCo7dv7v9_xk2aY_hmoX0TugQkwH7quFNZvnCYLT8DHdjUfA8CtSCjStKRRzWBPHKb2kFIBbAHEKVeb-iWOy7FlXB-uGOo4btdijNrxqfd5_TMyMphlEomOao9lyC9FeZZALOoh8h7-QHn-nrpNk3QLeyyr4zSQ2rT6jjWUUvgX26n3qNt8KYxlPwlKgrO3Mye87-2yCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۶ سال از این ویدیو سمی بازیکنان تیم فوتبال منچستریونایتد گذشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91565" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq8p3xDUbgaj_TMLSckfm9NMci0DsJtMNI2V0rYYPeRxquWh25koQLbitltmkRe3r1bahQFFnB1CGDKwZ5uZD-YlMt7gqRDe-yljRWCe4kZxXB1KOWRDZqMEqgR9x0x37YFeJxlJtDnorEtYXAPC_yYpyq9D7QkHVayTuvC5E5BWKaHeifClJGqNJohOOX9NG4sEC5LDOsMO8u4chfgAhv6GBG54LGAkAYTkaaD0EfjYK2NFof3coxcDC-q0P25lip1009o5JuPlfs0jWFLjj2pc21vkb9pK98hhD3PNpwBdctE-JF0qeV5hD0zk7s5jDqVZCz9SCruODJ9D8NOtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
متئو مورتو:
روبرتو مانچینی در آستانه کامبک به نیمکت تیم ملی ایتالیا قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91564" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=WDATRp-kJCHgcUiD_ZlCH36fq3UNbz6GXrQwrSJ0ufYCZqnd41QQJ2qnp4dvxHnQP5_MOahVxja0-9gPtQfxU8dJ7K93J6tbho-xv_1RQq6kTUSeAaQAZR_M4XmLpS70Vdxvnezmu5qZ8yLfDxEnsKI2h5P9mQmA10kUoPUhVSmScXrS34lP6WIKgOBjPwBbPdWrYZbsYmijL2Do9bpksECP2vMriuEdObuu473jI8vk-_2fTU8qIKNk3kUUeRBK8WwAYnbrAh54MFJuLdXFh2tNsFfCPmid8TN708sRPp573c99d3yAN0xen1s5IxyfB7UaI6pIMzw8MQdvvtTtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=WDATRp-kJCHgcUiD_ZlCH36fq3UNbz6GXrQwrSJ0ufYCZqnd41QQJ2qnp4dvxHnQP5_MOahVxja0-9gPtQfxU8dJ7K93J6tbho-xv_1RQq6kTUSeAaQAZR_M4XmLpS70Vdxvnezmu5qZ8yLfDxEnsKI2h5P9mQmA10kUoPUhVSmScXrS34lP6WIKgOBjPwBbPdWrYZbsYmijL2Do9bpksECP2vMriuEdObuu473jI8vk-_2fTU8qIKNk3kUUeRBK8WwAYnbrAh54MFJuLdXFh2tNsFfCPmid8TN708sRPp573c99d3yAN0xen1s5IxyfB7UaI6pIMzw8MQdvvtTtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اتحاد و همدلی بازیکنان اوکراین و دانمارک در صحنه بازی دیشب و سکته اریکسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91563" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKb23j63PJx5Ci6MlRQC1YjWAd4D2E2bWKu7R8fB_3i_2wdL8eOdCqBXLZpMZAmXPxGhCbpMohOa26cslrw9mg-ytbcovntmCeEj3yuSzFNCZoPkPo5NGT_vUsY-NCRbGUgfTcERYOtbtFH-FsjjguhDcPo3vniocmLaHEhi6A-AhZMqZyS-WURnpADuAufzutDWBq2xab2EEGYa3FiWs2x1sRf97CYzQrHtJAHpG8VCvLiHAojN13Ah0G7HvGS55kwbYVxW_UImvbmzCNiCgOGK4SABok_HK_HTp_3ZOFYiRE6CTmeTOFi36pcxgG4jeLVHbFyrwty3XCrPSw8rzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۱۰۰ میلیونی، از اینجا ارزون‌تر درمیاد!
😎
💸
وام بانکی از اسنپ‌پی
با ۲۰% تخفیف
خرید اشتراک
📱
💙
✅
تا ۲۴ماه
مهلت پرداخت اقساط
✅
بدون ضامن!
ارزون‌تر از همه‌جا، آنلاین وام بگیر
👇
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/91562" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=Awstvrz43FosqCqgjWkxbHKs4cv-r4UgRtilmqI1cgRnEA8QeU8hJZgKd69RrPcKDaB7-_ZQzLMWLkIqYz1JVAVJzLbiW0LJhXH8GxCkrJ-UNeXkrRtm40fcC-IB6-FQ5yS_oR9wkMzUif_tZjaHuXFqixlI3wpZ92kFPG00Vns-hZ03A2sXzdFoUzUb8_MfmrWXjeSBy_uCd2GiBmYKfp_W-3KTn6OUuuouKBnhjqTSqQ85Av5MsarjPm_UHkkay_6ztOSdp6XxopSXdxiNpdiKjpIYWlsgtH5biMcrryfERknqmWsVd5euxcXvrvwX6gmm17Kscrg8vTt9fHl4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=Awstvrz43FosqCqgjWkxbHKs4cv-r4UgRtilmqI1cgRnEA8QeU8hJZgKd69RrPcKDaB7-_ZQzLMWLkIqYz1JVAVJzLbiW0LJhXH8GxCkrJ-UNeXkrRtm40fcC-IB6-FQ5yS_oR9wkMzUif_tZjaHuXFqixlI3wpZ92kFPG00Vns-hZ03A2sXzdFoUzUb8_MfmrWXjeSBy_uCd2GiBmYKfp_W-3KTn6OUuuouKBnhjqTSqQ85Av5MsarjPm_UHkkay_6ztOSdp6XxopSXdxiNpdiKjpIYWlsgtH5biMcrryfERknqmWsVd5euxcXvrvwX6gmm17Kscrg8vTt9fHl4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ناصر الخلیفی در شبکه الکاس قطر : لوئیس انریکه به مدت ۸ ماه پیاپی از مرکز تمرینات باشگاه خارج نشد او هر روز از ساعت ۸ صبح تا ۹ شب کار می‌کرد؛ تا جایی که نگران شده بودیم مبادا از شدت فشار کار دچار مشکل روحی شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91561" target="_blank">📅 17:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkrYJoGhQgJIfdIBTvSMJ_ScVjl6WNXfH54FoAIUi-uQftd9Wjp9YAgX-_8cQJboxTNNcEiGjT5RJQs9I4coSKJgFUDgZMrIOxxv1o5qK3-JT8ZbpLpsnlCXVM4MH0uI90qqhqqwf1ocEZLsUB4KVkXnDsgt9GhNHMLr34e7rGwy2J0zjx7sS7TxR8JDx-0d_4aylV3YbtQm8aXKlBe1kWqnqg1nLIWKPNW2DWtaD1WmbJUOQDdyGSpa8gejEv4yyYrdFKLCz84jXM4XaZzcXrDXBlsZXu1o-59nYT5si5-tJTkGNZxFozz8cPrHQtsasPYJHsPPNsD5Q0dMVcX_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUI4ZBOBCZOXpTSJ8-8dDr6apt2aYkqNO-JIadxfYaYbuF0kGZJ6-NNRkzrsxTveHp_l9XCoATPEyJ4TvvgeLzKiSVrZg5j3cCNqmL2EKzB7I5_m7e7Z7LSsCwC4Y3eO1ddcvsjY8OEewqbvHXwD2R-bDRc_v2aRrmLWCU8x2cpB7QK5tvnzfPmvpdaW8COOJ1z1eoUHI6IWe6YarjQyepobwrtZDH8F-0YFnLoWJKbviy53YXhYVMtp4HBKl5dS6a4hGb50pqlZFaR9Gu141df7D0rPg5z9JwRwTDMpyilaBo6Qqtq8grsxG7niG2EzTYq1_fR1aS4_RmFSvh2TfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله وندا بهتون سلام میرسونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91559" target="_blank">📅 17:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw__kxP61KTNedmFCbsIkbWwzc1-UbgmM7l7ZY5mbRkmnvJuCmAF9fAS6tlJAFskLod3Au4Ma1LmAugoMB56DVbdGO0sAgJ7Lp_JYMt4wf6FoOzuoPdgNWn3kkWYkzB2LqVRB7T0v_V2ZmKwWSaj5OsYVkYbu1z8AqpidiByB6i2HXev-TWjFJw5-4_L_tBJu2UYNJZ8PABWL7UiTWWatIdAq8f57xF65E6Q_SX6XH_nGis9bMIRGAcNo_kzqsle8qvvvpSLkOy9F7kHG6BZYHj43gggLTCVj7O_yr66ymMf7r2B5iGqvMBRhmoWePoE4-rHwyApcHDEUDyxmgowBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91558" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2681453adb.mp4?token=k3PnP8l9tVuZHGFAJZkb5AuaWGbxuWByW37mBlwdJaJyQkFcASD9hjOD6AoYchUQb10k9vr_pvGAsY386LsiIYNMhjonMvLaFIsAwAWQVbLFkTbp70kbdWVBSJlIzIP2wsvru6pnOmETVHml29B89zh4h57k3G2h07yTnVlWs-kDaN-qiCs80wJxJ2oksqPgIpyuDgMfO-ki0VkOBYkNuMLr92X22YMHK6mJ3fuLYhaWKd-RbSQjowgZU59CoHoFTJvZCyhSqPu7d1KaRjASxCdfD2PZvrr5X2Y0KK2xjVwkN5zID2RVyBgk-fI2UMXx0C9Gfr7QjmIDIqlRUYmY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2681453adb.mp4?token=k3PnP8l9tVuZHGFAJZkb5AuaWGbxuWByW37mBlwdJaJyQkFcASD9hjOD6AoYchUQb10k9vr_pvGAsY386LsiIYNMhjonMvLaFIsAwAWQVbLFkTbp70kbdWVBSJlIzIP2wsvru6pnOmETVHml29B89zh4h57k3G2h07yTnVlWs-kDaN-qiCs80wJxJ2oksqPgIpyuDgMfO-ki0VkOBYkNuMLr92X22YMHK6mJ3fuLYhaWKd-RbSQjowgZU59CoHoFTJvZCyhSqPu7d1KaRjASxCdfD2PZvrr5X2Y0KK2xjVwkN5zID2RVyBgk-fI2UMXx0C9Gfr7QjmIDIqlRUYmY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧑‍🎨
اثر هنری جدید حمید سحری: تاریخ دوباره برای اسپانیا تکرار میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91557" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOadxMn50vXILKq6GsyqErupQFnyA0BwQEvoAE9ZjJDE1OZ2YhD4Nfhc68z0grLEYoV2TQqznDZ_aZrbc_InZbUWKcSccDUHjANpbSIXLhXpy7ajjHueW6GdyPQ0siTyqcJiYYajo42FTW67bQLrGj3EAaV1cCzlRSHGec0azLikJZ2poEmOLQ7pJHNjrhSd-0stijxLJ5d6i5qy9gkh60lHqLQ6V3O0ureuCAPizGhxc-kv-9_kW5Kskn7J9ZWW50mFaqI31TF3WU9yVP2Eb3CdhTJM18_Zepj7jJiefdZ5fzZhyF69-HGfiYCfNjLw_ivxv3XZLfrVn7t4Jcl-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زین‌الدین زیدان:
🔸
قبلاً بازیکنان آزاد شماره ده بازیکنان باهوشی بودند که بازی را به شکل دیگری درک می‌کردند. حالا همه چیز فیزیکی‌تر، منظم‌تر و کنترل‌شده‌تر شده است اما فوتبال بدون شماره ده شعر و شاعری‌اش را از دست می‌دهد. فوتبال بیش از حد فیزیکی و تاکتیکی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91556" target="_blank">📅 16:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اسرائیل دقایقی پیش جنوب لبنان رو زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91555" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.  امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91554" target="_blank">📅 15:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlULk1PK9N_QQCqJyTgSmJY7hHLHZ2WGCwnxPRR9JETMVwCcRFdHgSHx89cRuoWb6HeUzElnnfINhNi_WNvm5nLMWFKSNyR0A4fyFWOVneawUsItrUx1e-Gxg8eWYHshYm52QASNJw-CdUkegpCPyHkmIx9uAKOVJ-VfdC0G1ds0GxaoQROYf4U4ys-xT0QFwiVxiV8VXso_zNJ_hxV7TOLZmEPRZM2XfbNCpybH_jAEbb7lJSxtXh3LOl7dxuHA4DqMmBx2priK-nr4hqVmJViK0kdz0evx1RRZ1TrGgYoHYpr69aGETtk3Sg3TGpUDd4HL51grdsEACZ1EhYpaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91553" target="_blank">📅 15:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91552">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcj9yscWLAwU716KdxbS-5171aMX6u3F-BfEDJ8v6vHN77paqqdQOEcoSicM5er2d6MSdaL4kR9TnKrS-mPR1_cZV2gCNsvEMsW7X3N8DrqVPaED3h9tFvhg5o9K6VwwW3bxRYxfcwQnnwiYAW0XeTJTJhO5xh72Nkf63V0iicK-qFPYrXAFxSmJ7t0loAYnfBxcFqpEXG2GEiykMIdEc6PtSi4AqbGVLmmnug-SlGKSftb8wqyBBclsLrl1G_IOigJEcr2nPBhE_DxU80ffjsQC7lQ-9rolXzbtthRjvs39mVug3ued5O-Ny-cmaxJ0nkQUbv0w11l2UB0ifkzEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.
امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91552" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvEZy-ltG23Qf_MWrT9Qn_yM0QCLhTrJHxyawqJQuk3kBOgFzBlZVAvUmhdJGZzF7goVEBDaIWXhoOZ9pPph72tcc3wjMidvcGIsRVFs11pesK6UjY0o3fHZi5gI1QATKwKWCtxDmIwZtuBmFnf3oPnZThrVzVkQpp3QFeZfutGyv2Eeu9Aj_PLf53r9_lRq5PE5RYCSDAh0O3Y-CnQg_AgHMDKBsRBYJqQLZ2cxUici662E7vWH3ofJn22RqXXu4tVzd3frhWpbKnkypxpk4fa5qJ9FjZgIeHeoAqL7fW68-f85DFvsHHSesvq2DbNWl1VCXdC5M0xBx-seCOHnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خوزه لوئیز سانچز:
به شما می‌گویم بازیکنی که ارزشش ۱۵۰ میلیون یورو است و پرز زیر نظر دارد بمب است بمب
‼️
کاملاً باور نکردنیه و وقتی اسمش رو شنیدم بدنم یخ زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91551" target="_blank">📅 15:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTBgBVmyPvEdZYhRecbiaFkxSdcjEHIgDQI6bC6L5cyJDKhVTIl9nsBYDc1NlpkhmACNenCILfGLKmjZVX8JK6uMYo3ZPGFoX8trDRhb1AmHoVjGE9FoYsZPiRxbFhy1C8qYFZfAPpSNdoifnyM3btovCKuIcEHiMnR6WdE6qC6WksRGoGqdXK8rPOzeD6ndBD1Y-arhMwJ0RQ7zh3Jvo8UgyhkqfNrj2mg2rP4syccVM0_ExlMaRB9CvG_t2ZAwodAe-YJxmg0EynZvDF9VuHcoX1mQtfsKq-L5Fz9KW_hU8SS9rUF0Hhkj6V6h0XjOdvfP9E6mW9fRgBRjMxqQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا
:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91550" target="_blank">📅 15:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91549">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AEo9K4DIqYMD0TN6NJxrWsgOyoKlEaZJ74sMtfZ08CSHtwQURMByuSw6D7ZzEDCG9UqMEsNIwJ7LvO6fcygopjFFWFy_CT6X7A410ymAmc36WpW7vfWHrzrKNvOePYrQfh1hwwQkA-bpM24cHUQQtmApLALI5bUgXhdYOLHivBHQ-LSIPQzKjLtrFqh3MfUeZG8b9fkYyA-0FSYjl80yCHhKjCMU-bzuVJEfrrxM0AVMyJQLmabJYr15j3kdr6FZ2l6qYdAAve0UTzgTw1hNolaXto62nINPQ64bOJxhMzaNkaM9NCfQ5r36IiO_c77iN-OQpCQWjQmc75y55KUoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرارد رومرو:
🔺
پیشنهاد آخر لاپورتا برای جذب آلوارز: 120 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91549" target="_blank">📅 15:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91548">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91548" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f300aGaXW6oZ9sJM-g7oQFQuT_8kndp5fpE-BML9U-Dbe97CN7lD7Nn9_CI4QS0RNuzE7G9N4hzwIfj41jwr6Ffz7ODL3vZROiwriQigqHvgwLbE5knxALGMkko6DIw9N5jsWibEs5li3VDRSEll91Sl98flRhubmP6KlKV2NST6ANYeeUbcWl3gOSvyjNVTa9IbVK9SL-gJJubU-_GGN_4yDBvRyg9QhZX3yxXwi0QQ_oaspixIKlZJievQh_zphJbepkABcpiAE5Jy8w6rkwb2sZCM-8ZgS47VrA42DraOp2vSAnqadvK2dqTvOaebypk79UUTm_yR3SsKGVQoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBU1qkIRZaXABtSnN-39Yjyp3kCO7sMXhtwiVQl0dCci-ON5YBse4Ge5nKNLzcAIkFS6xKrVx9wt4Ju5rY-HllISl3HU_LeFHaxPEKsVgV22OIR2b3EQOw8I0jKs4zFKl0ud5I3IEDjn5UezVtGZiL4C5AXWNYU4dV8_KuftSJBbH-WZTvex5Wu2XZ_LNIWz_2I5X04uh1dotAfSCP52-8P-S1WpqSTAGPC7UuHWlg6ovZuAAG-WykRugweSiLfTcOuNp0IvEV2WPdeVuyhasB0RmlK9_SpntiLHJ1kPA5gbd5UT1pP2Sl8c9ZkeRk-Kbbk8L0fvcEamZo4YowSwag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
#فورییییی از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91546" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wcx5X_6mLmziZSloz9eOLnvcCPZTRhEOsr1M_LZVt7H_pL-Hwtkkey2AIBi_MR0frSYEHFdb8NU2PDC8rjpytd5U4PRZuHcW_DQ2R5XALAPQMl2RILi8Li_eplDYzPVbiUsd1teEHedrmc4JIt2kHEI75sinpHsaZOE0jGCm3RTjoISWPNGsTD_dmkYWDFAlGsdLcbuDu05epdWQwiieo2zk4hikuBf_zcAsI1VAObv-Sq0fXSJzb7MUvttR5IMv4MitEynlYFoClRTlZkdhw_lyHruwPAUZiuocpJdJ_XguNCe3qBzqAr2FN0PddzudlF2px7Cth4-nW_vHRBptXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فورییییی
از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91545" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91544">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ9ijXbn5FNgZ9oyffqJkIy2F8gJBfT97TpH52LqMG1cRpEklvqzM3qvnnBQWD3kojOvhpQMvPuPC68J1l8TmlqYwW8WzGLsVAvKr0xcSP3k2QB7QtHEzhT1h3zp3NPenePifsTF0_PYaEbwDSdMb0CgcKJvJMF3FwfIr30HJ2J9jfVxtxdoHj9ItQdXOBhphGZKUpYuz15gK5Luthe_UMAk07gcAvNV4f3dEYbqjmE8SnDqwP6pQREBcG6HnjGvtNUCDbiD09pOabuWkSRTDoNd9iUtBmyCVaSUaj84Gz5C0TLQ4b1ueK9sB3mG6ij-eizv20rfjyEVctNRlLJhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
من درباره شایعاتی که آلوارز را به باشگاه رئال مادرید لینک میکنند پرس‌وجو کردم.
پاسخ رئال مادرید: هیچ نظری نداریم.
نزدیکان خولیان آلوارز: هیچ نظری نداریم.
باید صبور باشیم و ببینیم چه اتفاقی خواهد افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91544" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/leqVUUCUophs2wgprOo-b0ZdP1xmMJg0bxaq4Ggi1s3J_IZXqwSkYWS0TCAdjxwJ9ObA41jSx4V6d8xSu_kyky695-NDAclTHchTsit9a0HbECa61xwI7mHSC7BiXxNeIeNJdMYm4s10lPzX9zQ0u6wu2JdJk4UnGQzo3ZX8Lf1E4QzxjzLzFu1FBSTFKS6s8M_3Yahd5Wr9jkcxrTNnuNTugRxaLky8gY9aW23LDnRjeFt8M4AT9Mvg96fxHbToHxDDYU76gOEb9RMjRo_xk9G9tX9zW_u6P7adlmAbA-xhgCeV5hr_UZkLuymn0GCd_v3w4TDUNOfx2KXsG7A53A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
رومانو:
🔵
منچستر سیتی آماده ارائه پیشنهاد جدیدی برای الیوت اندرسون است. باشگاه به نهایی شدن این قرارداد اطمینان دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91543" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRpyvj1kXCWTG4MdODJJvligwIHR4yGHQLLonNk0YpZMvNq1AnpIHRFhnwyNGOm0RTMk-Lj5pGksoCYjElP9jcgLgf56SRX_xEu91Z6XwuKCQdshUhjjth4YN6RC4Ud2Yr5mdzXxlW1StyLKvIp4WruL-AxqH1W38mtXynZR1IVL_eg9InWZ1AirbfMLGeu4FN98JMeaCHglBgjBNCgQkAmpSIAi3PWU158JSztgksN-vGjwxJyG94vcM0sxcF3UNkVoFq4pw-52MOJ7qFXN2ahL7yYB31JFpFbM-XxpzPxBHttNyE5QQJNUd_Y0hx6VxLL1WExngRq2V9hLi-aC0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYuASHZi-LFcmO99MhbMZSKUCf0aiey-r9dZumzKBxt9C3I8clxf7tPqGbO1QECh6rfYJaVv20LfY0yonp-o8peyrOHugZWQBI2yHiP79LBMrhFSubpJfSnnDARCiB_qWojOMQZVfJTHfuFDmftdOwuZMlIgSxZbNii77f3fSDkAnoK5VvrnY8FA4QRLUt-dpO6cmJjha3sAM1jFq5P-cwyW7G7IYJaHhEfgOpfmg1WzBRsYogk5XronO-ulIWlvj6h3YMFP2oP6hmVSqscyWR_syeZrtbO-4cxYRBhmKpHR1E7pdleOC1lXZG5GQaFHAwxVnXVwq0yAD44abi6lLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
#فوری
؛ قرارگاه خاتم‌الانبیا: پاسخ دردناک داده شد و پایان عملیات اعلام می‌شود
.
🚨
🇮🇱
#مهم
؛ اسرائیل هیوم: اگر ایران حمله نکند، اسرائیل هم حمله دیگری نخواهد کرد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91541" target="_blank">📅 14:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
فوری | قرارگاه خاتم الانبیاء:
ما توقف عملیات نظامی را اعلام می‌کنیم و تأکید می‌کنیم که اگر حملات، به ویژه در جنوب لبنان، ادامه یابد، پاسخ ما بسیار قوی‌تر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91539" target="_blank">📅 14:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8izGRc71ElDMNJ-742HnlcG8w6WzrQac1sz60vwVHGnXWvr22-53A1pba69bB67RTIXmMTl875B0d5ETaUQvqGOV4IF0fkTF8o_hL0Vj-hhcylYscMNrX48Lll3g5StQ8-OqG1blFt9HCA7ancZpBUvP4d1zOU_BFPGx8AorjSqCJTx0-JTWdfTFkYpI414uOVuhv1d_59F6H1nAUZTMKXu_Sy8nqPG5jbWWa5ajJ8_uL4cFtTvQWPIyG1qu3cA1hl-ddv0hnInX4xZTT9JzA1uXYbKVkQeT8Rqpy6A2OqH5NwcmUiYj0RbeSTVuOarMh7Qk4r0Wy8bbYnw595Nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف تو من هستم نتانیاهوی قمارباز
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91538" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ept49uU7irlAUr62H55EyLfxKs52W8X0UcclxIRKMbmgO5s_XwRa-Nk5bv0y-UD9Rc01ClS8Rc0QF0elAFK70IyQ7gn-Ic4jaxoMLGBrrwaXTNW84CN-c5ZLVKVBtfDhpNWCFBUgYm6pK8_si9XxxQiDV_KCrXyiYlq2gjg0_ANu8SYPJys_2AJRZmTHTT1uyzmZWZj3R0C5jc9z0zFeL7R3oP3sO5_9-4JR7slY7Hd6bc656bzJSCYSAa3K3b_uMm1-yuPEkIquvgdT-xejSwZtm4RRxnkx38yn9CqXDyo5WDLrSxSJg-OiieJqEF2hL3WAX5rG9ccPF4ZgmSELXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفده‌سال پیش در چنین‌روزی کاکا با رقم 68 میلیون یورو به رئال‌مادرید اومد و‌ در 129 بازی با ثبت 29 گل، 39 پاس گل و 2 جام این تیم‌رو‌ ترک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91537" target="_blank">📅 14:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=J0H3mvDkVUljiMKqNdeBU7KzRiQWd6oIlqd58ZmZKKTlmtlyUUSvMuk5_9I6Z5BIGFYRha_dPYXfnpGkEN5Mtw_z3JDqd6zbCAqFOISRUZ1P1fyMQ1JvA0lANoRmE04pRFx7trRrbzhmmYYzABn37ky1vN-Wop5fDEz1ORK0K_Lpi7LdK2UUNe_Ti3PIFuBny9aUFC7C9UJOLHSN6ynTwU6308p-eL2tZBJttUwa8r5pIcACD5ToZhSLHy9wd2jUr1DPuRONLS33lev_Zr6Cs3sJKoURO4Oty0Tfo2u7evJ8iayjAa6uIJBuRUjdsYSqa-jtjkEFAc2Y5tCVSo_PGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=J0H3mvDkVUljiMKqNdeBU7KzRiQWd6oIlqd58ZmZKKTlmtlyUUSvMuk5_9I6Z5BIGFYRha_dPYXfnpGkEN5Mtw_z3JDqd6zbCAqFOISRUZ1P1fyMQ1JvA0lANoRmE04pRFx7trRrbzhmmYYzABn37ky1vN-Wop5fDEz1ORK0K_Lpi7LdK2UUNe_Ti3PIFuBny9aUFC7C9UJOLHSN6ynTwU6308p-eL2tZBJttUwa8r5pIcACD5ToZhSLHy9wd2jUr1DPuRONLS33lev_Zr6Cs3sJKoURO4Oty0Tfo2u7evJ8iayjAa6uIJBuRUjdsYSqa-jtjkEFAc2Y5tCVSo_PGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد باقری هم سایدشو برای جام جهانی مشخص کرد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91536" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_3vq2JN_0hkXlTlrNFTHDkh-Y1ygZuxcsPOuvVyE5lFpxK4hCoNd5TVo8iTmB6K9zMz4qZ3te8BSGfd6O-zFwOSyLsuHvRrnlIh-1FlLTe_XK3ZN68rMRwVZgR23HH5u0nfm1_tLf9hCcwuWDTVKxxHno4AN2WLdbi3SlhzAu4WrN_wIJMHO7Fc1ahRkM9VhNaTN4PDWPUgLLudW8DjeYKaco6-W2xkdkINfEKkSZkc5uu4pd4TbhM2R86U8qXI0j8wLLeTcJSdqP2f61ZGTKlzrzM4gQNB9JUhzwCk90xfL_l0X-e68rZvoc5h3vbLWE_mNm1tDIcAh4FN7Kz7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه.
واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91534" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91532">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE1tNJwOGVUW38aMxPNRt8xqk7gBTbAI02DgYkLNRMyCJjiGiphmM6xRT-O6-0JfXaeGsAHMwsEk7gEd0uffpU42yYWPVzlbuzH7svR5vAGg9sxSDnF351ZueyOjcdcNqtFT4gLKwGkEzMM2J7hd1H30lCxsOAtH4ioRG1fl0_zv2lrGsgoSkJJz9ZRqRuXbaMycJHaVk1mM-cgXiuL51xVyneT9n48kJUDOSupb2gmLL70nHUgGwU3MdpRpeUCS_MZw98DABs1yFpQwGSCfQFuK3OARyeLeEfQfUCGwmdoDe96eeJDRRavshT9CDCnZGTU8Sa5_4oyGi-FsOCSyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⭕️
🚨
تنها 3 روز تا شروع جام جهانی
تلویزیون دولتی ترکیه مسابقات جام جهانی فوتبال را به صورت زنده و با کیفیت 4K و Super HD در ماهواره ترکست پخش خواهد کرد.
TRT 4K
TURKSAT 42°E
11767 V 15000
TRT SPOR HD
TRT 1 HD
TURKSAT 42°E
11054 V 30000
11794 V 30000
تلویزیون دولتی ترکیه با بهره‌گیری از تجهیزات مدرن پخش، استانداردهای فنی بالا و جلوگیری از فشرده‌سازی‌های مکرر به‌واسطه دسترسی به پهنای باند مناسب، تصاویری با کیفیت بسیار بالا ارائه می‌دهد. به همین دلیل، حتی در مواردی که بیت‌ریت برخی شبکه‌ها تقریباً برابر است، کیفیت تصویر TRT بالاتر به نظر می‌رسد. برای نمونه، شبکه TRT 1 HD با وجود بیت‌ریت نسبتاً مشابه با بین اسپورت، در بسیاری از برنامه‌ها تصویری شفاف‌تر، رنگ‌هایی طبیعی‌تر و جزئیات بیشتری را به بیننده ارائه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91532" target="_blank">📅 13:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ملی شکن⚡🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/Futball180TV/91529" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
✅
به اشتراک بذارید دوستاتون وصل‌شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91529" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He9bubXp7zgxR-KQV-vogmxX-cF6HU2zmSPxXqQBGuDaXNrYcoizroo11kF1pif4d_L-64iO_AaNdgtXB9tOMwuAvEsDqF41a7WqT2OaQnyb9ep-k1cCnk9FR9atD_0F7-XyaMOWR9TMim3ssaJ1VKuKEjZtQOZkTwq1DxJvuvAoqdd3W-64gGKArL3pLeA4SjzZ7Nz-_wTP7wIMMRg1AQ0sRP8-u-L18wnTBPmtmMlmQsElccY4UDzoyUX42LGHfD3547blrGp1kwIjsQAYcWuhjJF_8Srp-o9j4Z_3g_IYTmpuPki7ArmqVLMNicLAitutKU3VRASJTCm_E1Gwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91528" target="_blank">📅 13:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:   اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91527" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:
اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91525" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان ملل باز هم ابراز نگرانی کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91524" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91523" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXXZ8kWmqK1QCIK99h0lFIYICm95u1la8Vdo0wQ0nzPhUfOLK146U9FZ6pL_qi0ezzj4NWKJ_LgZtV_6nSPbpw_rFFSN7EyIkISUI8NT1yqd6N6SO9Uw2KJGwqFGaLzFfboKGwCIdaxNWzg_GSDQdAIhpVQW_yfu-s4I-tjJheaVvpk7IRin0gO773Z_qoQUpqtzNT4iXO60ttE84E2s_NLnCXf7WfHiWgS8orkWxlcthEb63arn3N3ED6weNI4Xs0km2ga0aRnsF31CpYk3ZWEJ2Z26rLHk7bFkAclrU_uq7xFwBBp0c1gX6JrolUp2Zyz6-mpUHe0Ea2D2Gp-z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی ترامپ الانا زیر پتو کنار یا روی زنش خوابیده. تا بیدار بشه یه حرکتی بزنه یکی دو ساعت دیگه زمان میبره. احتمالا این سری علاوه بر ایران، کیرشو سفت حواله نتانیاهو هم بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/91522" target="_blank">📅 12:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/91521" target="_blank">📅 12:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_8oFd8X4ODCaA7z1Mbre-k7vNLJWgv66-Su7Yw0bB1IhY7KK3y1XgYcbGSV_gQ6i1pWn3QfE4LF39ygpHO3xpmRspB5MqLJ1-9SDSbmk5gCe6Zz4vDJXm_CNMofjRXN5lYF4Ykp7GH4YX03qN4rcAxznV2XbELReWfQ1U3eY_qscuLGY0osamh-eTVbJ_FzNbXXpbWsxWRBhcyJ-NM5KJEwsuejEMngGhWaiNER5b_hiN5aS47DGpRjAoVhtx53KVLRWH3prCQSQUDKB_Ow50rLOLb6oRFcU35kLv92f3E6onlOajvRcvvIos8gKcwR5yrdSjMTXX2vmibYua3gJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
#فووووری
؛ عبدالصمد الزلزولی ستاره مراکش بدلیل مصدومیت از ناحیه رباط جانبی جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/Futball180TV/91518" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKpq4gfO7zz-DbPznYozI06Pf6FCAbQzgH6kAhkEbK5Earray8OsGM-067nMwMo-THoo8z-jBh5NY2N79BM001EzEIrAk-inadPqfmoKDfKWgOt-TjhAPt3Hdfdavt-Tyb0IopkQipdtWnc9reLYN2Q1vwY4BBwhUTW0SXXxaKMvBWGcTv3Px8nfx3gtewdWBH5p0jU-8Mg8m6uPCDH78j9yUE4QqG6HsRQCWVIuDpZ2maCJcHmQAWVX0MVxl57GUP4ingy9md_lTXSNUhKYq1-HoIQHnoCuYwskdDorVTwSu_m26DIRVAe7Nr_BGrjUMn_36XZI85MnOGWs6KqLECyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKpq4gfO7zz-DbPznYozI06Pf6FCAbQzgH6kAhkEbK5Earray8OsGM-067nMwMo-THoo8z-jBh5NY2N79BM001EzEIrAk-inadPqfmoKDfKWgOt-TjhAPt3Hdfdavt-Tyb0IopkQipdtWnc9reLYN2Q1vwY4BBwhUTW0SXXxaKMvBWGcTv3Px8nfx3gtewdWBH5p0jU-8Mg8m6uPCDH78j9yUE4QqG6HsRQCWVIuDpZ2maCJcHmQAWVX0MVxl57GUP4ingy9md_lTXSNUhKYq1-HoIQHnoCuYwskdDorVTwSu_m26DIRVAe7Nr_BGrjUMn_36XZI85MnOGWs6KqLECyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/91517" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/Futball180TV/91516" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کاش یکی به این کصمشنگا بگه اگه با قطع اینترنت فکر می‌کنید اسرائیل حمله نمیکنه و فیلمی منتشر نمیشه از خر، خرترید  اونی که بخواد فیلم بفرسته نیاز به نت کسشر بین‌المللی که به خرد مردم میدید نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/91515" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/91514" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!
+منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/91513" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/91512" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJ0Gd4WADta3Wu7Bq8bT5SYT3xikLzpzTV5EWqjq60M8wdB1nZZOtZyHAjpEKbLVUWA0ufI-Jm5ij0Z3ZEza8H0Nn8-DHih0d6UcItNukksj_STSoVBIVfS2qCgg-45lFmV5pbhixBeWsEzeLlVJkb3Epjuw2z0EWirs0WLFq07sP9dKe_q2H01qjhe7Z947KTJ9-QixEx7uUUdOVcTvDlzCnOuNLCvRj1TIYskWZR57pctoBVAeqxdQlpawvOOBCGRqz14FKK3A5qrPXB2f-WC4T3zKU8oZaRQiZaKhLiltqfsctf4GGi5491lKSOqVgwdSIGWptIJ2FqtybmpM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب ایتالیا در آخرین جام جهانی که حضور داشتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/91511" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/91510" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هنوز آتش بس نقض نشده!
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/91509" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3bvSpiZ10ADenBoJV-33CUsMSdyo37EbWD8htFo9W2o922rMoaAhrddLl0XRc7q3sfztZ20wuyLmjk47tGlBmTQl-kFwGWkUC4g1j0vrpPXOOiTrc6CW7UH3oMFMvW6MYv6T6GAoIkRMQoIceWgXUHdRIsUkcEqwIeDazPO9uAsRB8pxyPNwFWymIhtj_LTAvuglxX25z-JNVYFYfhoAeNgdIFuC1PwjXrB8V0f4wzvSJP2i1Aq3lxGIPC8yfFKcOqSfV7Iv64ciSb9CaDk4KvHThJKtaS84s5-a82-YEAWFnnjB-BrXb4ZbJRGPZZDAq2zOvo8XNFCWduv-KltRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibGMJ3yiXHN6SxI0SyhhukbSfNDJ9v5N6gxpQwaJ9Z5neJuou9TBlfUuLUS-N1EhA4RuqUaKTb9KT7PzYIRnYhlGpkkc6GKbhqfaE22xc2vPtpxmqix_2SKcI_yJq02klxfzAHenSlpdD5wyb3wQaaG1-sBcP2fYKqWC1B208TISZ8lqMWivKijqRc8yiedbL_Q_2NpYFJwksSoPsRl9O7Lt-y8P9lk8qhsqwn6OeHY2QOrYXRM0L_5bjzXdMcs1UieFHY61WqKD4Jl-cj78PhPHnuExYlXcMmDDBFG2XPVqCNsCLxxH_yy15k2OJnzSVBb0VhHB4-pTBU1GkknPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqay6inXCCuO5kjOrA8LPY4PJ-zhXg3Bdxoh8b4BzklEY0NSGC8HplkrBScA9wRxYlrJ1KHb_kH8wpZBZOuk5n3H9K5yMtuOzXI4TQy-oYxDmCcKwKEQpwrbgD9ensbFG3Nzcg2PkK-PrIf-R2sBF_8HhidGlbJmq766y5Gj7ZmRtnBKW3N-G2AywE0lVltUYL_kdKEDLB5kDYr3-MgRNp_-Zp-pT8gem9Lq0gjCpmzPi8t8rXg7dvuFybJ8ZM58fB4faLVpMBKgZs0FxUA-iFSatthuWHOkuYxoZEfcqrQT3Gg5AO4BW3IV9R3CJi6oEeq7UjZxAsW1iDKMbHar1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFhPiEg2w_nleEUF4H9gMMi-kGjh9IJm0foD2z_zwgu9VWN0CPHY_sY3ioMg3EMB-ypeuL7hGT4R3u6E8Y5ZauBSD9GrvWad71QAW9e5oII-UhAYC4gDWMEZa_Xie86UkS5PAu61W7027fkgKa55ZKy23BEJb1oilQ721RBIDJxKL2A5Ln_2QLlaUJnDGZqVMe2SyduAqXG7YvjLs4zWYosQbkVhIC63kyxT0I7t9_mA_ClBzFXzKNZy9rj_k6VlaeHC4z2s4P5BexQMG0n6Lo96Bx7zaio-WnlPHdvC4Fux9LIdoaB8MjOxSCaXp7RxyO1zRlTi2LFrYaQemC78DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMqWzDEX5FznqmrK0zxqBxN7PebgBMQbZ8NbPBcPCtT81cqZCT2jG7V3PeS8Xlp0_NYDGIH0jOkiV2t8kwiNFBOpXdL_Rrtha5qkjpHv3keLpqWMQOsbmLeEuLu6kL3seD9Gj49cUts4hZkPx9NQ0E3r72ojaGblEiEZu_92PA356vxJbJQU5X9sgbbu_x80Qrp0QPu-Y5Zbqh0rlgJ5MIG7JsCMWno8-vObAjn18Z9MHinoEbAmY13kRUSK82wbMiHDOVWG-mV5Il_JxolNlSw4YvSx63ewg0ISdNM5NMrhL7Hk9aXiklv2PG6k6xElEmqEAvoreXiZAcRHkQXcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_ntS94tEl2E2EMXWnxvjz7PS7Rfa5t3V7oiB0vh2DEMHlQ05L4tzGbjWB3Dh0kJMv8VVv3XaFhO6x3kupjqDv66CQ2cWCRXG4TvPwbpEbEzD1VBWXaNrSTrjxGT7R2wDxxhz1RnNOKpDif_ENrj0Hg2j8MGd_Nqc0aFU5gccmVz-WhpBleaxeoFFekDHFdwIVDuBGghiERItXUYBMPXoI4TC6r9_VAWG40IGdnF2B4KzCoy5OE-LC7TnLreGDXazLlzsHncWsRxKjGVygY7XN9M1tHzgdPt4hv6xG8lrt1_J7nZZ5QEPsOltMMOmrnqC8H7IXAlDfUfwbFIp0uynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hld5C9dpgH26EEy70lWSSL5kT2hvwItVCY1FyH_DwHwT4KTE2ARE30WJJQutsf08xzPC3zDn4BhiFfr7xRCzbq18AMdwHsPomnwaJ5_TWsOW8B2gzD7yVOm3SBDxPbqbRsu-I10dAnSeruiLGFc0H6kPVrRs7jGcMqtcMShyszT_l3jCQddJDzIGp2oCrBDBlaF1vnXLRU425th-U6Txc26BdPo9Vwb-Kwl_xXYfI0duEzL1_6EXpuYc2XqE0J4WsTSM-dcXVoHKf9x49np8lTwkm1-rf3IkGk0SlYWIeYdNI6Etft5eCzG1xKQ2IMU5wNtL__df1ZiaNXyg960TfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
تیم افسانه‌ای رئال مادرید 2010/11 و وضعیت فعلی آن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/91502" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91501" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی
صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91500" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkG27t0CCWarozJOnF_SZ8h5NmTAITiNsCUvq2z8ZgjtjWngIwalWs2WxxLQV1mDISDR-D8gjsyo068MWsvWR7nEhK1PPedx38yXG7Uj9u9F50hxU30XcNevZom4WPpFUsukkdHDHK_fJj1mQAjRXCYp5ib3qu398kHRoJplk0g69MF4Tel9C6CLHcG-xkI-RP9PZM-qAbR2L8oIAYJfldOE756x4kURWZFQVJLgn7J5e8Kp6zo_c7Oy4HOHyHs2pbPvPIVwLVTsWIAl1GLiHG9-NO75d2t0bzf-T_z6zzSJG0fzcoPKDQHWONKbo5IHYVG7cv3pil-LxrzxbyqLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91499" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvCEvJ-HCiHIxKmMVLIEgZdESkE-zRjjmojn-8EZxYLCu1Gclv7u_2PLd78vGWdv8o-8jqpCfxGyR7P7ySjldURHTC012pHn4yoEtY-BaIKWo7XsgvQANLrKHe2qkDn6EHjXbCFcUGaEVrksI1w83kSjnxWYn3Oqt43YQ99edWPjA9MMMJFHM0BoUbawCOc7h7GBYsIfV27s9pupF0SeidzfPOSmt5JlBWyYNgAhHYGUHcmM9U2Kuqisvpqdxx3TvJaIr1qJ649GTny7q9mi_5Jyg6sCFtcKlK5XDe5hwccmiH_jqtk21kti5DOibAdlBx3RKghNoUyXGE4-ALzOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
پوستر رسمی باشگاه استقلال پس از دریافت مجوز حرفه‌ای AFC و قطعی شدن حضورشان در فصل آینده لیگ نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91498" target="_blank">📅 11:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
موج بعدی حملات‌ اسرائیل شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91497" target="_blank">📅 11:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2ZSe2A8UPnfXRzILXiuhEGrpLO5cfPq-qCoVfGsWkzWdl2dWmB_iksX6lL6gS3zZdgC36wDFCILGQM31ka06IdIMFIS3jjLegPgbOZuhU6TmdXvzbeAv5Fa9KkDtskrVIs_13vI2LCut1LP2121VM43IS4BLGHHyUKs--Dtv-iF0uvmbjZCMpdzFPbKtHrNnWyZVWRzgkhq0fhccWGFB1tABgFMNOJJ2_v9nu3nt-NL10qo0m_3ShqEa17z2o7rZrAcPMW9VJtuUf4kw1Zya5w71WM2Nu51IqrPFllMiLvwTDrHQa7uLWMaR8wBMf1ybYNvlGNjed5dIsmXxGvbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایلان ماسک: تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91496" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚬
بیانیه اتحادیه اروپا: جنگ خوب نیست. متوقف بشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91495" target="_blank">📅 10:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی ایران به مرکز انرژی اسرائیل در حیفا و ناصره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91494" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anH9NkTuz1SwSX32kqw-rt2y-ff_TBMZlkGYLAuaxZ2aPbATDxS-dYTkSsUM7XYYgmUmyL4Q00zhXzcOlsrNl6TqWOORcoQnr6vFatfAffA7cX9pXSbxFsLfiX-HDaD9agm1YLGQfOhx41ATnD1U86QKDfjvGTs1A4qr64Xxs92g5pwF2AZCozlf-u0Qbod-9ndupoX8sM1uMV2H4Pafoia1MVT8By1IZ-KqQ8aTcnPMC3jXJBoqvkKWceDAg8a8vjDPJ_y9mhTAC265PNh50a1m2ypalRFxzjsLz3Gkt6Lou2CQhOP8G7BrFNNI1CAnTzDPIoZ7mcaIA--vPisQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مرکز اسرائیل هم اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91493" target="_blank">📅 10:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری؛ موج جدید حملات سپاه به اسرائیل هم‌اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91492" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUC7Pe-5N-v0sHjLboKaZqFKr1uoXoD4dtTNSLnHAu6Yv3zEE8J_LqjkLrHpP69KhzMa46FQ8YIweub_UUTwy_dh0tLREY_n0ZPg6un4IxdrGrZjiM4BXv_RFVT__k4ZACCzwdWikpLBjzkhgJRxL8hJZBr_F7xvh6zudCa_noyWIbdUSw4cDgovGX0gQUNzp49dA3tfwx4U4iowlYfhbz5t-R25znZcMepc2dstdtXYoGeljn32l1tdD2NQZQkP0RYahGxmi-S1feUwrrTXCj7uAsr_PLZZI8VkoyKNafjDe6qLqAWIXEDR5A-rY2bbeCtJ2Oqqbx7bCotxyLIwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تفاوت‌قدی عجیب هافبک و دروازه‌بان پاناما که در فضای‌مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91491" target="_blank">📅 10:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران: ثابت کردیم آسمان اسرائیل در اختیار ماست و هر جا رو که اراده کنیم میزنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91490" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
فوووووری از رویترز: با اعلام انصارالله یمن، یکی از مهمترین تنگه های جهانی باب‌المندب برای آمریکا و اسرائیل و متحدانش بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91489" target="_blank">📅 09:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=NSsvY-wYUEidtvzC1g6T8SvGXQ_dK0lBS8o6JcV5A6d-cfMCsg7Fij3S6oXcg2BDoviD_iBIYece6krtlN-ZW5il_cZeEJo3K36ldkDelb2dg2PjHWT27F-8N9ABZFf2tOU53OVpjv7HVClAYkMepzlbKSUVPytbLq8NoWEZqxVKhqoKIaze_WCsLmsESxibnSCJs5EPWTG1F1xYRH4XxdvC7xIpHn5bTI2HDaXVa62iXKOehlsF2_959QvMlrJGChsv9l9BMnn64Yihb-dqZdl2tNHJa44KPaqA6t5SwfDTgPCdE1LiKi5ODiTqn5vdF3vpfszKy4xfHFF_-xJBzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=NSsvY-wYUEidtvzC1g6T8SvGXQ_dK0lBS8o6JcV5A6d-cfMCsg7Fij3S6oXcg2BDoviD_iBIYece6krtlN-ZW5il_cZeEJo3K36ldkDelb2dg2PjHWT27F-8N9ABZFf2tOU53OVpjv7HVClAYkMepzlbKSUVPytbLq8NoWEZqxVKhqoKIaze_WCsLmsESxibnSCJs5EPWTG1F1xYRH4XxdvC7xIpHn5bTI2HDaXVa62iXKOehlsF2_959QvMlrJGChsv9l9BMnn64Yihb-dqZdl2tNHJa44KPaqA6t5SwfDTgPCdE1LiKi5ODiTqn5vdF3vpfszKy4xfHFF_-xJBzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ورزش عجيب و غريب تو اروپا اختراع شده به اسم اسب چوبی که هرچی از سم بودنش بگم کمه و تازه براش مسابقات قهرمانی اروپا هم گذاشتن. فقط این ویدیو رو ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91488" target="_blank">📅 09:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل:
تبادل آتش میان ایران و اسرائیل احتمالا چند روز ادامه خواهد داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91487" target="_blank">📅 09:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88d8579a12.mp4?token=ZD-f6KYFSlTkWTB3RP1kFelxLTC2Wx1-aiWeIVzdeauQdPUSISpsBtVPmrb3kqFIydTApmBO_p6Bs5zM6ZJSxiimYFu4SMLCT3DGkKb_4U4sV2EmEMxo5vc09YWD1MPelWeShOvo_8lSqgHEa538-bj0cmV19UxG-X7i39iv3lh0E_G4OsqwlUudQZUHOLXQmLKzYZTzRva-HJ7SiqX0xRBq3ELabCSz3Gk5V1DTN5W3fobd2Fi8TwPows3gUXWHYVH6nnucbiCRLSR-qDORmMjkOCdPk15V68d6c8_ejW36EgKdIgPly8IV0QsnDViDRYBCsGKwc9sESl5568Y7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88d8579a12.mp4?token=ZD-f6KYFSlTkWTB3RP1kFelxLTC2Wx1-aiWeIVzdeauQdPUSISpsBtVPmrb3kqFIydTApmBO_p6Bs5zM6ZJSxiimYFu4SMLCT3DGkKb_4U4sV2EmEMxo5vc09YWD1MPelWeShOvo_8lSqgHEa538-bj0cmV19UxG-X7i39iv3lh0E_G4OsqwlUudQZUHOLXQmLKzYZTzRva-HJ7SiqX0xRBq3ELabCSz3Gk5V1DTN5W3fobd2Fi8TwPows3gUXWHYVH6nnucbiCRLSR-qDORmMjkOCdPk15V68d6c8_ejW36EgKdIgPly8IV0QsnDViDRYBCsGKwc9sESl5568Y7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
خانم جورجینا درحال ترتیب دادن موهاش قبل سفر به آمریکا برای دیدن جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91486" target="_blank">📅 09:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران:
دقایقی پیش، عملیات نصر را با هدف قرار دادن مراکز مهم پایگاه های هوایی راهبردی نواتیم و تلنوف آغاز کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91485" target="_blank">📅 09:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a069e77f.mp4?token=EQKP1yfRF26Q6U3w5SNaNEfOEDr06K7vb2nnbH4sIU6082bpVzBxt4arMX1fMgyDCtxLIqaYqbOalgFdgpzPAxlYKlXnh_4UJIpD0VUevNzgai1ET8ufQJSxPZDVeMOW7h4OeQyR_IGhtQ_5zUH4CyqIB6wr_lqyteKWQM3Iln7WZQ6W8ET2cDeyhet0Xsp7TA7oETsrWbN3ZN503CFAzwQba9d6ISBrR7w8nHv9lILe3ArJwOIcMLT3QJRz9CqVqu1GEI_K6uQtUYaeqjtC2_FtqpD1w3qtUMSOQs3cv23xXc99noDHKrfsc9S6NGgpTGf56_DnH2htSV1fLv2whg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a069e77f.mp4?token=EQKP1yfRF26Q6U3w5SNaNEfOEDr06K7vb2nnbH4sIU6082bpVzBxt4arMX1fMgyDCtxLIqaYqbOalgFdgpzPAxlYKlXnh_4UJIpD0VUevNzgai1ET8ufQJSxPZDVeMOW7h4OeQyR_IGhtQ_5zUH4CyqIB6wr_lqyteKWQM3Iln7WZQ6W8ET2cDeyhet0Xsp7TA7oETsrWbN3ZN503CFAzwQba9d6ISBrR7w8nHv9lILe3ArJwOIcMLT3QJRz9CqVqu1GEI_K6uQtUYaeqjtC2_FtqpD1w3qtUMSOQs3cv23xXc99noDHKrfsc9S6NGgpTGf56_DnH2htSV1fLv2whg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صبح‌دوشنبه و پارت پنجم ورزش در خانه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91484" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
احتمالا با دخالت ترامپ وضعیت جنگی ایران و اسرائیل موقتا تا بعد جام‌جهانی متوقف بشه. البته اگه ترامپ این‌سری واقعا بتونه خایه‌های نتانیاهو رو بکشه و مثل دیشب کیر نخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91483" target="_blank">📅 08:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91482" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91481" target="_blank">📅 08:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=TmmAovYZBMdpDte-1xN8_8L3CrCOZf5Dz5A1ZDwGKlHbaz2Wki2s7jBDQ-pet8n0QrkQH0z5LhN86OCSzIkNvEGUVnRKkxdjNnNOFYHmj7WY2C2YjJsz9SFtHGHofLDFK39ahYpIUfs7ZmhW1GF0NpDdUkjEEvJFRyF5bP1-QNAWollzgKFrTWiJq8TOcJge1BvUjwi9pk0g44vZ_kn2JcWK9GqL6WJc-kb8A0NSRivAG-KD_KDuAYn_nxePI8OEynSV6eaxqEsq5nIE5p1c93V-vJ9mMsbDAB2jm-LGb4YiSfRzjVn8mURpVd1_KiBAJu8xTaoVVnGWPS8-xKYhnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=TmmAovYZBMdpDte-1xN8_8L3CrCOZf5Dz5A1ZDwGKlHbaz2Wki2s7jBDQ-pet8n0QrkQH0z5LhN86OCSzIkNvEGUVnRKkxdjNnNOFYHmj7WY2C2YjJsz9SFtHGHofLDFK39ahYpIUfs7ZmhW1GF0NpDdUkjEEvJFRyF5bP1-QNAWollzgKFrTWiJq8TOcJge1BvUjwi9pk0g44vZ_kn2JcWK9GqL6WJc-kb8A0NSRivAG-KD_KDuAYn_nxePI8OEynSV6eaxqEsq5nIE5p1c93V-vJ9mMsbDAB2jm-LGb4YiSfRzjVn8mURpVd1_KiBAJu8xTaoVVnGWPS8-xKYhnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91480" target="_blank">📅 08:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از یک انفجار مهیب در پتروشیمی کارون ماهشهر حکایت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91479" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇱
گزارش‌ها از شلیک موشک از مبدا یمن به اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91478" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
آژیرهای هشدار در سراسر نقاط اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91477" target="_blank">📅 06:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG1zZbPruN2kkrS5mo4bQwCplptI7l7Hn7sNvG6V1Y9xFViQBheloc0CF44TpRzkBXp8wbHlJzaEZqkxZ8PpUIhVdJoB3vABCuNDLCtERIVVDrdiMvfcSv7CdgFsa1gBO1bI1wxPZAGXoJiG4C8fU9o3E8P49B8DQZA5_NPTwrlVHYXEkQOWZVLyxQg0xbRheo-johAlFtYPCO74QCJAJm7RTu_uO5hNqXBSbr7lVFpl5E8IpXQQ7i-s8BJXC3wT-wZo1i99ToRiZZETHYmuSKyYj7eZNKmQ93JK3RBQvJBOj4YOUay1VauwhSpwt8Xqm_UC1Eaj5R0Blmg3S4R6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
آژیرهای هشدار در سراسر نقاط اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91476" target="_blank">📅 06:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c5f07bd9.mp4?token=fgmWMVwRfWx-9IR7r-xti9Ld8QG16MMNSNHnZMGtagCXiOY6fx_4rTO8AvKa78Mx4fkOrMHlCunyVuxHGPbTcmcGlz5UGVkrBZ9lp_xS_6VE9t4Rrv7trUVnY8l4oOIs0VUDjuV1IE7d0dnrH0d7docTUIy8gnpBqagQ8RO0rugsQEgNvhgzlcvxB6T23kAVqLpO7cGxZnPVjUMZzAGlU2bO8T4XnvVq1ySQlGjWeWXBkhYT6OmsU6JNXYC4WXoWJW7XUF-5KyNN_1kYkKjKkObIVPh7oL0_qC5oSX90NVn38OvkMiZ6Nw9jT02mIlqPs-uL4LUCr0c7_9GNrGdVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c5f07bd9.mp4?token=fgmWMVwRfWx-9IR7r-xti9Ld8QG16MMNSNHnZMGtagCXiOY6fx_4rTO8AvKa78Mx4fkOrMHlCunyVuxHGPbTcmcGlz5UGVkrBZ9lp_xS_6VE9t4Rrv7trUVnY8l4oOIs0VUDjuV1IE7d0dnrH0d7docTUIy8gnpBqagQ8RO0rugsQEgNvhgzlcvxB6T23kAVqLpO7cGxZnPVjUMZzAGlU2bO8T4XnvVq1ySQlGjWeWXBkhYT6OmsU6JNXYC4WXoWJW7XUF-5KyNN_1kYkKjKkObIVPh7oL0_qC5oSX90NVn38OvkMiZ6Nw9jT02mIlqPs-uL4LUCr0c7_9GNrGdVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار و آتش سوزی در غرب تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91474" target="_blank">📅 05:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
⭕️
چند نکته ضروری هنگام وقوع انفجار
در این ویدیوی آموزشی، جمعیت هلال احمر چند نکته مهم برای جلوگیری از آسیب در زمان حمله هوایی و انفجار ارائه می دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91473" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJdQmZtcty4MMdltII69GH_Enb2_pQRhnaHf4_LLsVC7tfvhTQotG60zgLGu6SLGlxMqoxGT3Smz5SPuqhbEGA2CK2_1jjxZywjYmlnvs5Bns6nzZtFcgeK_6eNst0f_bwbSY5Ehc6JoYtpR1SmLSXq9UJiYmHqyZzOyxJCupRSfiiP2kQZFh_iNdYQFJJxgRCtOgQPL-uJfam6or3KOKjiB62ydKlEUjhnThG7j3obTqFO9TX4NpnFAi0xq6dNHsN22E9dQxKuGpQNKfdcMuQ98eE3pJxPAImadwsqxS2ovTPv5XO-BszCNfr_n6Z53s8DNxRsPs7e4KkMTtq4S3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
♨️
انفجارهای شدید در نجف‌آباد اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91472" target="_blank">📅 05:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
💪
#فووووووری
؛ فرودگاه مهرآباد تهران مورد حمله قرار گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91470" target="_blank">📅 05:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کانال ۱۲ اسرائیل: پدافند اسرائیل در آمادگی کامل برای مقابله با حملات موشکی ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91469" target="_blank">📅 05:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e78148f7.mp4?token=SYM_rhUSIEAm0O0n_-MUA-Jz9UUB8JX_nTb0LsfZgSCCHkeHdhZrW_t2oi1sxOR1qiCOg0PC5WoQdwDVt6gGrltaNNdGQmYSDE1KRdK3Nlqlm6iM7oetUwQ1wth68fhp2kllcAQ5wYH4n-oGrsuR9cxRsjJlnCR4RwuY3n_6HnuCwyFha7mJ0oDgJsRjRU3l7d4mjz7HENhz0L73a6wVcIIX9VfSKymonMOvcZt3IVSKP_N0xHY90Tnrjn-6u78pfwrxYEKHvIwSP4zuKoQnMroF48ERhGgUXe5YZhJjgUCRzFQV04SZqVFMzKjZRbAuPy0WCo_NzBTl8A0q2WYZNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e78148f7.mp4?token=SYM_rhUSIEAm0O0n_-MUA-Jz9UUB8JX_nTb0LsfZgSCCHkeHdhZrW_t2oi1sxOR1qiCOg0PC5WoQdwDVt6gGrltaNNdGQmYSDE1KRdK3Nlqlm6iM7oetUwQ1wth68fhp2kllcAQ5wYH4n-oGrsuR9cxRsjJlnCR4RwuY3n_6HnuCwyFha7mJ0oDgJsRjRU3l7d4mjz7HENhz0L73a6wVcIIX9VfSKymonMOvcZt3IVSKP_N0xHY90Tnrjn-6u78pfwrxYEKHvIwSP4zuKoQnMroF48ERhGgUXe5YZhJjgUCRzFQV04SZqVFMzKjZRbAuPy0WCo_NzBTl8A0q2WYZNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇱
تصاویری از اصفهان، ایران، دود را نشان می‌دهد که از یک انبار تولید پهپاد پس از یک حمله اسرائیلی بلند می‌شود
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91468" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm0o1ACd93fwMH0yYzVggfuMPBy11tY_Jgj2m1NjS10CSXklnutftSkpUN6SskSetWjWaHPkYf69QLlNF5ef6S7XicOQUY4tYQwcQhjY6RK6MtPTVA0jYAuLwMSzgNWbNSl5mGakOgwDo2P6gwYaCLs-yNKKs0pnt2C-qkYrekoPR5rmtkFMPTXt1nwWmzOACJZdhj0ZPpe0McTkYY6eaSgN2FgGqc30jqS6rUnmyUV2OfHSZ_zJjag2mMB-NZlGj8cWQddlkCOhaka0Za58QS-mCuzu4jJ4_KH3dVLgMCrhC9qFAIFc519cogjKVbuBqCkdk08-YXT6SLFOoqxnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویری از انفجار در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91467" target="_blank">📅 05:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
شنیده شدن صدای انفجار از سه شهر تبریز، اصفهان و تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91466" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91464">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1uG_cHbap0TZaypLtQvlUS7K9nAHLuXFUqQPaGElBt7MhhIE4gEqlGBJ8X_Wh-FpSFrttMyodMnNDpxkuNBbF_H8M644E2mTvWhNagXASOu5Cht03mS1bwnHNBQg-w8gFmZQqCr65hIu42MUmU2TmvPSYkHVXMYp4VvTk3FunqcBgPXvKaXiQf82-5A7dINvShVLgKt3fB3RRFwsv3cI_bsRV_6d3tLs5C2BVD60_hru1jx-mcypgx-UTzKrZUctnM8OOUIE5OHL_wlsgOC5zGV90XCzD4_H7zP6p_0Jv0wtIMT4d8wHq1NEUTE0hcgecCEJRKGC1OuOYflopYdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aK34cF-HIDopBjp4TqHONRjTx8Uy4yh-GojKFdquKu2QDCWMqdUNT3E57d_3bEEp7XGiPQZ99NZSHP-F-iHokN5HLXYDQH2mWY629D6CKJ6ZDHqWtcqkYy98r8G8p4EaOrD1poMNHzuA35eDiT_jvQk_HAXEwhCcivViU0UBy1TuYq3uq6s-zyZZyInvtrFsazcHJN7Q92ll5nPPnrRMJ5WZYaTu6P7gCSU8xHTF2gOAFLItsb3_5PAxQWqCbuIXxLa_KRp5p1IbrTKBDrdONXTKM6kk15IeOw221oYnqEdoqkSfGvgQS8QqPKdPoGZm1F-sqZjD0YjIgt9RvVr5OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین‌تصاویر از انفجارهای شدید در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91464" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
