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
<img src="https://cdn5.telesco.pe/file/Yaaioy3-UDqBCk7s4tO3E9ewiMdgWfCc9iQxWU9z7MHKIUiN-AVimL0JU4zJQqxw2yzYACJUeucjostgr_PkYt-zmzoJxbP9pIDFtVtNp7Dotzl4TiCCbaxpY_HSEKfbeB7zu0WO5u0DKTZGc9tD65EWBXepATbPcvtMmIjAsYPolVHa0eCn7XH_DyxPkl_UAgwEHRU1JlKD9GGOLqUTYYF3qgUBoSKIHGVUEVkv0cbX_Db6TF7UanQEN46O6haNaAbteKs5AOjA9sU7deAehfR4LJNvZSehtvGRfXo8QMKXEbRQoA6DxkjCrJWhPuPbSZVlVR0VBQT-lEaUlZqxXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 422K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-105879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqmicQoVY0T6peVmCCFjRe_h7I-e9Zab4WDjQ2aZwd3T8Qvof8ytLjtpDRpaG9j8D8R_fAaiC0sfDVnGBP7Nc_AL2xzWnHxs3TCY6oEJ_FBpHO3cDWqEvcY_kiT7f2Ia7Z_IWXdoA7FP-aS5m49TBbMxa6KjIXEULxmy8hdYOlUb2dAqCIgszNOr3UI3H3RWv9BEfunCVngC6GEzhBS2-DI82o3SNzBMC0nmVhkdN5ff4OyC4CANO75eQJc5C2R967E5d6LgM-vZZDeAeQ0Vjcw1kHTIappWXQVE-ir6yB1vaREIahKmnJo3-UTMmtmRh4knDE8MR_OutECb3es6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
نامزدهای توپ‌طلا ۲۰۲۶ زنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/105879" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTNMoZMJ1yvPvdN8hDOncoDrnqkBvKJ1UeTCXBRKrTSapt7vbLu-Rf1XMxYb6zSQDucKfG8MaDnmvwbgB4blER5kDPDEgB-SbZI3dmcLyPNR0S8wpVKPtmqTcLg2MekWOMM1yqSnkAYmkfaH8W88IvgJwdNyNbZRgalIaG0OTuR1-RUYxA4akKegPGiiQtScH0hRiJ24DG2Rj0JtDEc1Xakx7wyMLOm-phYZetff9x0mhwbUPxiiUUv39oJnUYoLPttJe1AdHiPd-zV6MtXgVt7aaQNkfAvR63fE2gJgMmV3i05SWj5iMpO3ywE_dn75f9DUXtKkWV3GUL5EaQeIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
پیراهن اصلی تیم‌های حاضر در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/105878" target="_blank">📅 16:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8991c045e3.mp4?token=ZBUYtAsJCFFsseT9XCzERDnWcnNh3wimjrNER7lPR3gv6JRDIVtGG4mHsn-vG2XV3DCxMzTywbBXIM59JyaWz9qZ6PdV-SdeODJOAb7y6PR100WGkZ5J0eyoDU9vW2jrJspy3ye3T6urCwCLCp9myeB7ROgEGThEdsSJAq2Bbs5uanEop39PLNMEn5WwVomQD9gbIeN8MuYHNq1nq3d8oPwoF_PXz4iM23wddY2dw4Ir0FY1d7YW9f-R69fbiMHPef4_dOit4EZlAkFOWdv_7ddUFE2uR7vEzvNIgQp9mnbg61TlvohfhbPfTXLCtRSmrXLBnmehbK3_2pDjSUDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پیش‌بینی یک سال پیش خانعلی: تنگه هرمز و باب المندب را ببندیم نفت ۴۰۰ دلار می‌شود
پ‌ن: قیمت فعلی نفت ۹۷ دلاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/105877" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEoGK3PJBa08ScyTsLQu3EHWtQk5vIZqcpbSXjckvYAg9LdjtxrS7m0tWYcd83KUOqHy8RylpNduRpNLe-U4xlhZuRrWinLlPISp0O0Uo-hUADxK3oFxyqDPlpG-uMtFCWtbZ8yfsQsY5bK3xeheB5iyhqc73aJmyMnj7dSyc22oVpJ6JSV6UK_X54X-RzT8he4XaUEApSiC3sb1-Ia5o6_Jw4di7GxYJjeAjRPyCKCoRfk4mIHXsh6JlU9SQItkJbdf2u1rBRyk83Rolrnxe46lqeYpt9DM_XrNdKBlELZh4pQGWTxZodriFvSQbopgRmIG-SB3UehIcrH4lzacGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mbiu_fzaRTNDVNonC2uPOQoCNa1OiIPsAMWbjG1R1kCPElyYNOptbMCkT4bvB8Ec2bDGc4tqoKSUNUFBD0OSz4BYjmSxlmUbtWPPovqtUo94QwpNpAWHWN56UXFtxjDlSWdb3sFBMRknG2Ginq7g_6FPey7q60DmrYAIXs3iLjSlAgFbVsLv_fNO3UCzqrg9VF-fdKmx7P75MoQGQTMDhEuGAWRZTdlSWswUx2mzPkRzNSWkOsWMJgC9aNmlRDWOOnkYjSQ-qPNe_vy7d9V3t3HONdPqUtX3gqd7FxSo2PyEPrsvA_IHHXwE6rFK3rHC5VDdgs7yf6MeAQvm0gWtiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
نامزدهای جایزه بهترین بازیکن جوان سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/105875" target="_blank">📅 16:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325df9d92d.mp4?token=uO5jShSX66XSKdrhDgVsute7PyJb0T1MvaZPhbXEkYHX1elQVwBKOYG8SkwDh-PxwPSmAj8DBi2C99NONcSByOyVZoMdDH03GXU9g2LtE_0SlbaZJ2ktW2PhMthczLtoTQUTjTUmtzLSQiZVlNrWEpz3EGngBct1r08phxwogjdCViIXSEkHiEops0jMSGi1L1yoSmdhEd0BfOg_LjSJN-DkCiAwUV4Opyty_EWU1JARyn4vIEUx1zSg7N5pNVbljyUOxcdsyi7C30z1ng4ljaYjLg9tJb5S8Ii5JEtjjDV1xZdJPss89N2uFMqiqPoh6CWKsehKY_EANm1xN_eDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابوطالب یک‌سال پیش خیلی قشنگ کفت؛ تا سال‌ها مغزمون راحت بود اگه علی دایی اون پاس رو نمی‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/105874" target="_blank">📅 16:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105873">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
❌
🎙
مجری شبکه‌دو خطاب به خداداد عزیزی: فحش دادن شجاعت نیست؛ و خطرناک‌تر از خودِ توهین، زمانیه که به اون افتخار کنیم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/105873" target="_blank">📅 15:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105872">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218de47812.mp4?token=WR1YyFOhXEAzWAsu1p5-72OqkLyiqXmPL9xcKqOSZnssoF89k411vImpcOx94gB2d56WmsMq2wdboVGfffx4ZaxH69cmWVUcFRSgsAGOOor8krY5ja1yFyyB6-OE95efDSB2mzObdILyPDI_3LvmM_slQSq2IR98o-NSzu2UpWsOONFAJs9IvVFshplRbUnDYGWKQBSZySgN6KFWa_vpiw8N8wO1nIa6AuMigV974dK9kGSP0MI23Jq7xiL9HUEc2yGUBsC-3TIoQp9yvXrHf9tULzjQwktM6QzdrXvxBytw0sWA5VjdHe705b2SJeYHzYlEk7xV5FFW9RrYkJWaQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
یادی‌کنیم از روزی که کل‌ایران به هیبت و بزرگی اسطوره علی‌دایی در جام‌جهانی افتخار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/105872" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105871">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ8-3wD_xHaaosK1tNIdzUGea9iRnN3qEiPQGI3gkQ5ujXhIbLNrRzeG7Irj-kHTs2GOv85vS69Dks6hT2Nu6k6ikRyEFGQAILyR3NWfIHTMhht2NvBfCJZWxdIVw6GhNk4RpuuffLvKtO_8oixcU_gexcKp3GKlYjsppVJ-OGMhdcl2PlUYCvnpwbRNdhKEkUrHFIS-pKS76LwdzTdHXNUo7LXcHlWzhlUzXtNrr4pgiqvon9_55o4IMzxN3BfMur3vcFAUAvt4yld0f9dgSIN8eSX7GzSFczA7eXaqQPTDmQYbmm-lCV8w0w7bBQpBgxfWT66WKZLJhuKaNKUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
🇮🇹
نتایج ۱۱ تقابل اخیر میلان و یووه در سری‌آ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105871" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUwfIwJeLpVK54YvwFA8HKwvWgBWay7ClP80c9F306Gk3DrODfR3RO7Q1pw5wBra7GwUQJfYjAxoSKHmql5Z1ls3ydh7zwb6pPchkhEqzIpE1nFNmMdboScJC9ZGjFcA-KRLGzCz2goQ0U1bbPpv__zEOnRbgaujdnzm8aIGQr6g20h1M1M5d7tAFOLI4SE1wqdt54WPBvj2HH2Y92tJYJnI5hu53m9xp_BjX88Fwx4gkA2c-mCkqTCMj12tByqNKlix30EWKvBm77bHHaCgpPk0mUoELPXXS9Nbsv7goDZPKxukKlr5DfCywBZx_GeV5ZMwLyaN_0JJ9B9s6s0SBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست نامزهای بهترین سرمربی سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105870" target="_blank">📅 14:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSgm37HzCULf-HXApIb_HCU3-sEFrsWjGW1MMixXDU2zosXSpdaVwU6e6QOVd4FC1UCEAtf7MkV3DRs-HMTIfNpDIOZ5AjcnJXfnMER97F9fmWNfrFjwnicdD5nYWQr9Iyh6qSb_akzOQPC9ihfSoxrL_5A7cHEKCH769QfqQxcu3C_d7JqAEkADra1GG_x-u4kkqpTgu5W_lOm9uGS2o5Z5L-48eJE1nwtQZPwBuRpkuA2Dg4Pt1072sfe7v26ikW0v1SxqE0lqEm-bRAGZkwPgNiU3aex713pifWu79nkT5E5BVfER7ZThNudX6ST2NSNXzEXezgtDsd5bzn6s6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج سه‌سرمربی اخیر رئال‌مادرید مقابل بتیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105869" target="_blank">📅 14:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeAICC2sSnv2NKeJIYswwyCR5HmidkpxkJwDL9W6MR6ucpt-X-Jc4DIkdSwjS__H8doKMRbbUzhh80J43LCc5-ePejp3VMihx9pSdQoC6c2OohjF00bZrkm-MGcRZIX8l8uWXczEeoRgz5fUIfoG6Rp4QkrIMVb4Wxx6btAx1e3m-8yLsGciCrAPf_oSBYCjRz4LI3R6axoAaO6RGkx4M8tFYXNlkRxu6xkyrTLlqf77cbmKL_6mAZDaxpDajdElAjkyMKzmScqGMXPYGX4LtG-uJ6rpLyCnSPy_vH9hXgvxT52-lfc025vJLKJ6ebVqJ_1XP17_bWYTASmmX8RoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد خط هجوم بارسلونا در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105868" target="_blank">📅 14:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKukd3IZGCzEUUN6daKkMM8L8MeUNCUR5DQKoctlv_IvdCcwtzKq8ExTuPFZd7pAc3XqZcS3JRYZioEdd76iDrhkc6Z9eQ6mY_N04vkHhl2gHBEyrCkM8lhl838GBBCPld4tzqK0TKpyrRT23CmqcXJ0rcb6JW1U5rDXRYkdujQuulWxYUeuPZLhKm7q4FqYLZSk8RO-8VZLPKU91Hq3uwi3DY5OLLiScj0zm7-Qmdya8y6EnEI7Ky5SN6kEQuL7kBxvldngRJ3LphXahZi6zSTRr0kpnETRbB-Jdhu-eFtx4P89mVEwParGAEcttzEBjXfWZ_VPyoOXxiKvAUm5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
🇪🇺
لیست رئال‌مادرید برای بازی با اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105867" target="_blank">📅 13:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105866">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoQWVDJSUp2nEp9RogVnVnJEYK9sHaucgT0BAFaCUb3-ZF20bXYCuXP-r98fhp1Ja1s6pmr0eH3AoyWmD9akPoLcRO1deCHfduY7GHes9hyJa60pOYFEf05K4h_5_AMExmVxdgI9LmDhz-lt3nTqK6pHEzeDDLR0U2yuvoG148hVUhBqiFWGZrdntexzejzAx_3jZBaUQ7spy9kG7gl5ysZLiSZabxf6Ag2sIbjfF2vXxeAyZiuhhsNE_Jq0aznwgb6M5mmC2lkJV1PKqw71tQK0rLg9TeAaRtWuWfPLe0tdDz3JkcgynvQRLKuMOkPUsCp2GyhLtC8rwjV8Cq8HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🇪🇺
در آستانه آغاز لیگ‌قهرمانان اروپا؛ نگاهی بر بهترین ترکیب تاریخ این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105866" target="_blank">📅 13:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105865">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRsr1NDlP1MkOizfQCkQZzEwLcAtaAZLn13Is_2D3X1KpwejI_C0gvO6EzRDclHcv-17zxzVD4gbxXjMO-5hZuf3lLDLWbLTpmTc2PrpQR-JBdQVNgf8TiOARgPeriWsikksBhgD17Dqb_aigMG043PjzjbotZb2hJWVKKozihSmslWkUrm6bYrGBaXGvlgPO27irP6WqL5DGFMj2OLDs7S5oIlLHEwqtz7XygV9Ov9ohqyZnCVMFTsoxfotcqoFA1xkmbeAexnIw48klMD7kNWWZ1JK3exR-3WdQGVvnj3PQgQ8Etl6j5tsnHMm0994nOcYzi5h-fQv4MRsBedAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
نامزدهای بهترین تیم‌مردان فصل‌گذشته:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇳🇴
بودگلیمت نروژ
🇧🇷
فلامینگو برزیل
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105865" target="_blank">📅 12:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105864">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
جلسه کمیته‌انضباطی باشگاه استقلال برای رسیدگی به تخلفات صالح‌حردانی فردا برگزار می‌شود. حردانی در بازی مقابل پیکان غایب بوده و احتمالا مقابل السد هم شانسی برای بازگشت به تمرینات استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105864" target="_blank">📅 12:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubyFpayDrNhtS1Hl1Ht2xaZUtyOIqN_KZFoOGzwf0v5upUFxnX_VaPfgizStmctKg6BmPEdQMy_Q_mwyyuMwekGa4o7f6bBXkg4eYYgHNlALv8MXY6s87MNu_42v20oeu57-VfFjg6a_MonE7heQkMPxWOX_Q7-s-Ie4WZ1Xmf9QjSTc1xLl5OUXCWz-Fg-5AXWX72KPT-0Isj2jGmRLgBOtu7arXsfCPUovjTy6G79LuAoIPJiA0jKAF3ZeDb-uANH-nx3qxf6DlJRwE7If1qR3CwKTwYSg9pK2xEtAX6JOHfndPT5lS2V6yXCA2oULuVjTs7JfrfuYTqU47saWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نامزهای کسب‌عنوان بهترین تیم زنان فصل‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105863" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🏆
آغاز اعلام اسامی نامزدهای نهایی جایزه توپ‌طلا؛ ابتدا بخش زنان معرفی میشه بعدش مردان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105862" target="_blank">📅 12:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hfeoz0AJJqB0UP4JP7-p7bJUBZ0H508xaw7lggg4WX60pXDk-0x9RJet7vbfzpeVz6a5-diQV3e86LODykX-gSBmkAQv22gf3PdqBMuluWe-ooDveKlTqSF8CetfAPIpKwtSHL0UKXk7UjAcdHSJxrfM9WR6LDZem4mMq1O3gnc0mDsC79p-W8u0UXqfyQVgQ0cL-rA7vFXhrMKfaL_FrJkheznidnGz7XczsCAHEFGCmIupLlKjzervbzC64B2OH-wqP6f_MOwTxDs2UbVioDtbTMHo9P-1A7CSfcHKSTm3HW-CltOFdFYvn9kg1OQT0Mu3OVl86e87njT0TWG_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
آرش قادری مدافع ذوب‌آهن ۶ زندانی جرائم مالی و غیرعمد رو با پرداخت بدهیشون آزاد کرد. با این ۶ نفر تعداد نفراتی که این بازیکن طی دو سال اخیر آزاد کرده به ۲۰ نفر رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105861" target="_blank">📅 12:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105860">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=rYCi6ZbZ3saB3iULPWufC-J77YCcM9U68x2DmUpRiDXVdRu5m9wIDsM4EEZ8OTXCLMON95Qu5HhAbk_Bn1eqZ9HbATAqcFwqojWoUAw31DBZYB9JfAPCHNDMA8ZOoL3zd_IYjK1Yc6_7TuWHCRwC0kxdM7bPZDTqsq1ZRvswMzOhbK2NGXp3441mowUBD1i8mwI_nlDRrTwZmIBUQQvpJL-_Acob8Wl_UIc0tobDZ4Knyb9q2YPpCTZXGWs0NwZ8FdLWW558zy88WqoAAByKNrcgvfz_uovrSKkbkmKZreYjY1ByTCn2p0OchwfXbfW9JNXDuSKwSYJiZEREKT3nFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3601cd12ba.mp4?token=rYCi6ZbZ3saB3iULPWufC-J77YCcM9U68x2DmUpRiDXVdRu5m9wIDsM4EEZ8OTXCLMON95Qu5HhAbk_Bn1eqZ9HbATAqcFwqojWoUAw31DBZYB9JfAPCHNDMA8ZOoL3zd_IYjK1Yc6_7TuWHCRwC0kxdM7bPZDTqsq1ZRvswMzOhbK2NGXp3441mowUBD1i8mwI_nlDRrTwZmIBUQQvpJL-_Acob8Wl_UIc0tobDZ4Knyb9q2YPpCTZXGWs0NwZ8FdLWW558zy88WqoAAByKNrcgvfz_uovrSKkbkmKZreYjY1ByTCn2p0OchwfXbfW9JNXDuSKwSYJiZEREKT3nFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سون هیونگ مین در مقایسه مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105860" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105859" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHPiucW3hqXUFEwQ2SkrHOS7003hKm2MlCpGG5Oo3YAdO4MpqJpTf6yACf5aaONrcTHZMt2fxurGZNojN0WaJI9tnxJdevlJwac7zDmO2P8KZRsRwb3ksrzXzCjIcSscLvE9xu8sMzExU0ylmqmPahqjOb0Pj_NrJUA2cfI7Hd0Hy1ZIrT7vON9URVAdCLPKxSPlnwjNnlrsL9kG1sQCBply890G-drBOmU-n52tSaKxTwivB6DlPyjKrCOsGd6hG8io24Q5GBZ80e6u4BlCvMqtQohnXJJ5kGGKuz1YgvODgPEuH-aXY83kMT9E8fW_2Y_yTyfw8A2V_gIy9af5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105858" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105857">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hae78R3ZA1CPU0wRfWW_DZ1FUndFxqQaBxewGLquVD4pFETibnpY5H5izmy5IYHogI02KWVuweG4lYT7mC1IPvYlXt5NcdZ2_8KJ0YXUXEdz4TW0V47-vzYQh6Ul93SbW6pX2BX1qPSIAYmTbsB36T0_6OvzEe4vybTBjfQm8pcJvdnOmkEtRQFWMAkqzfFUn6RoWK3_-jzz5aOAqvbH4S2dd-MX4JKlHtoxNgUvz7tTSoSWIMFDh-mxK6EWs3ACg8eEL3QYcg5VRxthg9Wz5WPvxor1s3G_Qp6gfk8Emdy84fBJZ7NhQXW7FJMuy3HiSOEbw80wba_BVeZtI6O96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🇶🇦
🇮🇷
نتایج بازی‌های اخیر السد حریف هفته‌بعدی استقلال در لیگ‌نخبگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105857" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105856">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSIVCqwi-hqYt-1cjuJmIKVvZTpWe0T3qfoYwiV5iTVgf10TvDdHPFce7e5N_DXKeH7PBUdSYghhz-bQn104ohucIhdUoAftPLYvNLG7A3-xu7Be-nz9oqXcbiHD9hTRw4w7aIHOmI9TwO-6sMpjiZrGnpedRV5rAsI_jViQ8Fm6X7zY4nLbTVrC--CwAdcxCYVCdlDtiXdzvnvaBMzcJ90NrFZ6fLXGNGTftoAUr3vgD0rzBDoswN-OM3_zISz4xHbKqmyBkqZfLBcusdi531t9S_3oZLOmZUJCFc-ifQnBAb2mi1E1BegbaJGTkD6Z36cwVt2chuqkgcT4LZSIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
لیست اتلتیکومادرید مقابل لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105856" target="_blank">📅 11:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105855">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=uM9kPeooTBell81V5zaYKCpumBD_6HBHcklt2qM1UumFdA4qwU7fhCnfG_OC9XKrb957T3lqj_vrIKSTQPvJpibCp_JQuFdENLv3d3ELy7AnFDzfPtfYYDXjs474IYxdzTBfj033Lpf99f7quiTgASBmHR4F5XuqkggIoo3X5ierQDk7ic274huBy-kyZZuAMRFs7R7Yc5sOGn2gVF9xm071hd5IyYQnw1oEUOcqCluZ0_B0NSn31pyb5cHOJzwCFaycP5JbkCFUzl_duz8Zojw7t00brJjtO9mWLkcc3EBKnlN89suSF0zdhKMy97t88FnPSavMgaalENjlJkpGjpmZVB-dDWt2UQu5t5UGWf9_SBEqjmasfRyAb6i2TTXyGfGyiLwOIuMckOvt8lqOl7hDCjvNbOAsmu50mZltIF74GqW3YEOJLBv4m6plZd9jEABIYd0zIZXxPSne6udGTAQT_boVVkp7KqxyHAqm1O-RyGdRkhxgfMXMe3ealP3iIW_DlTVkzH5NBjnPx1NIR8dvL64tSl7JF1MP465JXyCz7Nd7RWnjAgnaG1XHdyE0u6Cmwan_Gt-L1hwvXQCXIgDDK-pcooATvb93refBG1YtrBMqb3ATG_RzDPcP1Xsi4TMlD_N-l2r39o0mTrPZRf0xDcHb9lpXLz7pM4jvE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5465076b4d.mp4?token=uM9kPeooTBell81V5zaYKCpumBD_6HBHcklt2qM1UumFdA4qwU7fhCnfG_OC9XKrb957T3lqj_vrIKSTQPvJpibCp_JQuFdENLv3d3ELy7AnFDzfPtfYYDXjs474IYxdzTBfj033Lpf99f7quiTgASBmHR4F5XuqkggIoo3X5ierQDk7ic274huBy-kyZZuAMRFs7R7Yc5sOGn2gVF9xm071hd5IyYQnw1oEUOcqCluZ0_B0NSn31pyb5cHOJzwCFaycP5JbkCFUzl_duz8Zojw7t00brJjtO9mWLkcc3EBKnlN89suSF0zdhKMy97t88FnPSavMgaalENjlJkpGjpmZVB-dDWt2UQu5t5UGWf9_SBEqjmasfRyAb6i2TTXyGfGyiLwOIuMckOvt8lqOl7hDCjvNbOAsmu50mZltIF74GqW3YEOJLBv4m6plZd9jEABIYd0zIZXxPSne6udGTAQT_boVVkp7KqxyHAqm1O-RyGdRkhxgfMXMe3ealP3iIW_DlTVkzH5NBjnPx1NIR8dvL64tSl7JF1MP465JXyCz7Nd7RWnjAgnaG1XHdyE0u6Cmwan_Gt-L1hwvXQCXIgDDK-pcooATvb93refBG1YtrBMqb3ATG_RzDPcP1Xsi4TMlD_N-l2r39o0mTrPZRf0xDcHb9lpXLz7pM4jvE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید اسماعیلی: داور باید شهامت داشته باشد و از هواداران ذوب آهن عذرخواهی کند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105855" target="_blank">📅 11:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105854">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97326bc667.mp4?token=INDgq7TXn3EM6nDt7UW1QUX3FplQ3AdV9G4ws3n8CPJwavxEo-DkCn47eoIRAg1vwKI3byV3UckLywiJzLfBteLOvD6gSHqniGL0x84MHi7kKWpSYB4ZAvY2pcLHx7UIZaaK1M-q3-jK8Zpwg3dNze42j7clbLL1pDO4pSQRPmOojbSydTb4LnnX3H5NWcp_YOFSYoua6WgIbrkfJnmqEU01UxWQK5CyBWZH9Iap1qZ4zwH_f3R7y-EpN6C9Wh7lq1AB6skonR2CQAdPly2ybWwSYLIAHU7d97YXKFd4NalbTfdSV_EX4jEHHgBKdEBZEymqdwuzZaJUfMP9HU6MKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97326bc667.mp4?token=INDgq7TXn3EM6nDt7UW1QUX3FplQ3AdV9G4ws3n8CPJwavxEo-DkCn47eoIRAg1vwKI3byV3UckLywiJzLfBteLOvD6gSHqniGL0x84MHi7kKWpSYB4ZAvY2pcLHx7UIZaaK1M-q3-jK8Zpwg3dNze42j7clbLL1pDO4pSQRPmOojbSydTb4LnnX3H5NWcp_YOFSYoua6WgIbrkfJnmqEU01UxWQK5CyBWZH9Iap1qZ4zwH_f3R7y-EpN6C9Wh7lq1AB6skonR2CQAdPly2ybWwSYLIAHU7d97YXKFd4NalbTfdSV_EX4jEHHgBKdEBZEymqdwuzZaJUfMP9HU6MKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🧕
مارک‌کلاتنبرگ: گل‌اول پرسپولیس مقابل ذوب‌آهن باید آفساید گرفته می‌شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105854" target="_blank">📅 11:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105853">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
واکنش اینستاگرامی خداداد عزیزی به محرومیت ۴ماهه از حضور در ورزشگاه‌ها
:
چهار ماه محروم شدم و الان دارم میرم مشهد به یه زمین چمن سر بزنم. خواستم اطلاع بدم فردا کسی ویس صدای قدم‌های من در چمن را نگیرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105853" target="_blank">📅 10:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105852">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688084072.mp4?token=S_SP7uzGrGcezSsxDt6v2XqUWzy4nWJG3n2pETfdiWrbj6PKE6c1jvQjTivDA7HSNzBemL6bLQ3gchMWBc7hqI4sfALIY026O_PZ8gyOrVjuBjgY4taieH_ntLvXU183_tlPpQQu0KFuFhbJdGvKimzX-keR0wgOY8xKttzyWWfAUX3jTcruUyK2RFmxgq-DtChtqdxKhsmPEotT7JXLIJc01034bNftWYzrRWXiNdGYEHtZVuHw86yIqTAMF-Do2a2aniyCBoKrCIYR2LAvqrkI9DUvFtdRL9baVYVyMzy16ngDu0Xd_6lA62wBe2v3l-p3JGlDIpHQLf0v8z5uBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
پست باشگاه بدبخت و خار آلاوس بعد دوم شدن در لالیگا پس از هفته‌چهارم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105852" target="_blank">📅 10:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105851">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc1-PlnUL3ANpS8t9Qxdm7NZE9UktnWdWc2-cnn3_4Q35qVnvK_GpC2hjCEF_F5VOO3tPYMUxyNCLsBNVpqJqYVWzNioG-IMKHcXVCu6f4snFzCLvq59OJzVJo9xDEpTgXEpwYZi4aFaX3IsenetGZJ_fGlU_djFXfu6ZKbWcwkpMRrP57OPvAfymNM1m_UxeartfpHvFAS1kfsByu9j9PCk8xRpkkTNXZernIyY9YNvHq4OuD5Zf0kvfxduHeS0zy3N7O5mieGbMkr-5jbF6HIzO6nN07-XdWVQ32_OpMHGG3D8iddwvMby4Q9EY7hOzH5gwmUGXXzHumzGfsmyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز برومند پیشکسوت شریف فوتبال ایران و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105851" target="_blank">📅 10:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105850">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=n7a2gKmHR6EU42SDBpgaBswYnDxRGN83SeqsQQx_bzDAUl4YeNgukO3woYoggscFs3YwEd9FXM340YlqGFVXntb1hN5A5gA8VqDsOrQxNkeeH6MnAqV_75x04XkIu7WGyNVAcATUCaRwLSU-j9s_UW31G3rBk6i28vcisXaac4M7OqmnenJv4rjcEkEDmX6gg3Q9B1Jp01SFCHNI8sd4PBucJuRnoAN8LYjGjqdO8Jc-iYrYie9h1LZzffvna8ms3O2w7ZN01YTqsdvwPQG7WuZ1xwAeaHGqHjCs7zKmIQE0MSPaw8iWgJ5OT_fWEuln-_HYsn7RlJb92vzNllTcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dffcc1103.mp4?token=n7a2gKmHR6EU42SDBpgaBswYnDxRGN83SeqsQQx_bzDAUl4YeNgukO3woYoggscFs3YwEd9FXM340YlqGFVXntb1hN5A5gA8VqDsOrQxNkeeH6MnAqV_75x04XkIu7WGyNVAcATUCaRwLSU-j9s_UW31G3rBk6i28vcisXaac4M7OqmnenJv4rjcEkEDmX6gg3Q9B1Jp01SFCHNI8sd4PBucJuRnoAN8LYjGjqdO8Jc-iYrYie9h1LZzffvna8ms3O2w7ZN01YTqsdvwPQG7WuZ1xwAeaHGqHjCs7zKmIQE0MSPaw8iWgJ5OT_fWEuln-_HYsn7RlJb92vzNllTcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنایه تندادموند اختر بازیکن سابق استقلال به رامین‌رضاییان: فاميل‌هاى ما سه تا جت دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105850" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105849">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=EO-U_LR_aABUbpSL0rg57HXVP8mqA0P4bgCRNwElVJz_IjXD5LC9_N4F_oM-jMWQiAL9MK-gQR8u_oQCJvPwKxKJ49uuCcAe3NsB5v4Tm3__sej-YIN0xyURH-_lEVV-0ILp8jaq4dCRzR2wLmBdYW7kUGh9oxz9u_2fr4ekNDHKiphx4l7vkh3fbSAXfUJgQJTTmtm-KeF85WuU7_oOIQeEWGiBmaeyU8YPPWyVfjsG5x7vML4SPxMkB6ugKLwH0E1ASn0w7dL9_PAwykydzKttJUkDfI2aYVA9uWDqCwWZ1GnpDhDKSl9KocXCPNhTbW3gLymmf2Xrfew13Ksusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7e0021bd.mp4?token=EO-U_LR_aABUbpSL0rg57HXVP8mqA0P4bgCRNwElVJz_IjXD5LC9_N4F_oM-jMWQiAL9MK-gQR8u_oQCJvPwKxKJ49uuCcAe3NsB5v4Tm3__sej-YIN0xyURH-_lEVV-0ILp8jaq4dCRzR2wLmBdYW7kUGh9oxz9u_2fr4ekNDHKiphx4l7vkh3fbSAXfUJgQJTTmtm-KeF85WuU7_oOIQeEWGiBmaeyU8YPPWyVfjsG5x7vML4SPxMkB6ugKLwH0E1ASn0w7dL9_PAwykydzKttJUkDfI2aYVA9uWDqCwWZ1GnpDhDKSl9KocXCPNhTbW3gLymmf2Xrfew13Ksusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ماندگاری مدیر رسانه‌ای استقلال: اگه کنعانی بتونه با شستش گیتار بزنه، واقعاً از نوادر موسیقیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105849" target="_blank">📅 09:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105848">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=pqZwN06nzHVq70wUwgB6gE1nuxy2r7dtE1FwotjT-X-Sd1IHQHSr-6Tpi2p1dSQT6_XZ3hV8GFK4cSPN5Wt0e-jzTLKFLlQN4hDQ_0pcudfmuXuvIi7EFLipDaUA1O5G4pQl9m9gOVxiw_LI7SlA-F6MdPIEg0w6D7pVXr7zlA4NMhbUxNBzXeEW9hjvlsWbyRHzFQpAHQob4PoXtpCfP-UciDYlGVwPn2tmCxG7PC3HHvpXYStxe6nCJX_QkaERZwPf2tXkYfjIsyoVEfd0PglI1uaZoTko9NQzUF_gzIseHgRItiTkIaYIaJyVfXONdSNCg_W15O67LEzwuRw7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a78b6b32.mp4?token=pqZwN06nzHVq70wUwgB6gE1nuxy2r7dtE1FwotjT-X-Sd1IHQHSr-6Tpi2p1dSQT6_XZ3hV8GFK4cSPN5Wt0e-jzTLKFLlQN4hDQ_0pcudfmuXuvIi7EFLipDaUA1O5G4pQl9m9gOVxiw_LI7SlA-F6MdPIEg0w6D7pVXr7zlA4NMhbUxNBzXeEW9hjvlsWbyRHzFQpAHQob4PoXtpCfP-UciDYlGVwPn2tmCxG7PC3HHvpXYStxe6nCJX_QkaERZwPf2tXkYfjIsyoVEfd0PglI1uaZoTko9NQzUF_gzIseHgRItiTkIaYIaJyVfXONdSNCg_W15O67LEzwuRw7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تصویری از کنایه امید عالیشاه به داور دیدار تراکتور و گل‌گهر: میخوای بهشون جام بدی
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105848" target="_blank">📅 09:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105847">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پیام جدید وحید قلیچ به خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105847" target="_blank">📅 08:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105846">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105846" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105845">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRkW8NH3gEwvPPnN-y0oifw07R2GMwa0rWLEX2HcNFletbrxtFP_q_DaZ9vh0hXaptSNN2dDiD18qfxofLrhNbpkGiPd7TKiejIHB0O2g3XfLgUF_3tmG5pCl87JrvIu7qo0-je7wCC2SOSng6fqlS3oSuf5d_K597KvNdqKyiRHC4SMnRokOLoco762M7nTVDAvIakys_VahocAmGWKCZwz45iNcFj8sksJeMMGoutouEiti-73QkjpMOOoYz3c7XTwrMmC8V1lMQ6X765RS6hPGrv-VGealY1zJWzQRt1bC-6nsy_7npUQkR7Ts7W3rbW5mI6m86vYMmvxDaiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105845" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105844">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105844" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105843">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=h7XnrwFM5AVDbHF1-KDJpeeuIyVt_rJNez7hzsVWZPwXq-piBap6BJNjxQFH1EYZG_eU-0vhgX1_ZpkEjUtdhVy2CM7gsA1TiY5o-mX7n_m9vHeDGYjFcANZXwqvI-Y6lGZOMyNiXfOtb6V9BekfLFxZRL1ohNLDkvstcPZ7KDcm7JJG4q4Ga4C27xaevOqPIURP6D0C9FgJj5mynzwvDyxqua-qopf4rubCPXTUbUBw_qepx9ejsD-LtQ7VEh0v-xW_hv5nAdaGwdAHyc3r14DahLlF7_y1rmbpWabuJEKvghQr4NBpdSStKdHFJn0f-OGJnG-OOfSglpx62ElNzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=h7XnrwFM5AVDbHF1-KDJpeeuIyVt_rJNez7hzsVWZPwXq-piBap6BJNjxQFH1EYZG_eU-0vhgX1_ZpkEjUtdhVy2CM7gsA1TiY5o-mX7n_m9vHeDGYjFcANZXwqvI-Y6lGZOMyNiXfOtb6V9BekfLFxZRL1ohNLDkvstcPZ7KDcm7JJG4q4Ga4C27xaevOqPIURP6D0C9FgJj5mynzwvDyxqua-qopf4rubCPXTUbUBw_qepx9ejsD-LtQ7VEh0v-xW_hv5nAdaGwdAHyc3r14DahLlF7_y1rmbpWabuJEKvghQr4NBpdSStKdHFJn0f-OGJnG-OOfSglpx62ElNzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💙
میثاقی: با صالح حردانی صحبت کردم او توضیح داد که اصلا قصد حاشیه سازی نداشتم و هیچ قصدی هم برای حاشیه سازی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105843" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105842">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=tLz-u9q4hGUcG2XtbRA0Mel2c19nhw0XYRydJyjsIUGAujwVscAYrp__Zf18nNqcOyP4dLFwmuRPA73o2_AuTESCKF4AWqg_QNEGsCZOgt-CfGNesiUMXrOEwBcILX8cKq2PVnmDbVKe-l3xYSIHq5KVTdMBvxzwaRUkRccJB5MPI8Z1YgXQKv_NiQ9aYXVGwt-dV4-LesQ0o-6sDxwnfjEiRkB3CgNNnjm31ncELuZqdVvhVXgWRGmRdCr5-H5-0m1M7dItaI90PStCU3ASezZF_ClcZRdJzte8o9D6BP3Kp2lgF6LrFY6CLAugvRXgPKfQvgiBjCt4QNr73H803A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=tLz-u9q4hGUcG2XtbRA0Mel2c19nhw0XYRydJyjsIUGAujwVscAYrp__Zf18nNqcOyP4dLFwmuRPA73o2_AuTESCKF4AWqg_QNEGsCZOgt-CfGNesiUMXrOEwBcILX8cKq2PVnmDbVKe-l3xYSIHq5KVTdMBvxzwaRUkRccJB5MPI8Z1YgXQKv_NiQ9aYXVGwt-dV4-LesQ0o-6sDxwnfjEiRkB3CgNNnjm31ncELuZqdVvhVXgWRGmRdCr5-H5-0m1M7dItaI90PStCU3ASezZF_ClcZRdJzte8o9D6BP3Kp2lgF6LrFY6CLAugvRXgPKfQvgiBjCt4QNr73H803A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💙
اسفندیارپور مدیرعامل گل‌گهر: سندی بیرون آمده که یک نفر از آن طرف فحش داده ولی از طرف ما اتفاقی نیفتاده است!
💙
میثاقی: پس چطور عالیشاه 4 جلسه محروم شده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105842" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105841">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=eVFXHbDBYexT-LLu9Lp_dWODt0qhAB1vrfMd8Lg-PSjZhfCJLHEUpi2s7M7icl6hBvRGrhXquP27_b0NlU9T-XXFhmgaYxvkvW06ocLDVbnd1iwGPm7MyLj7mA4YXE_RpaG9Me2VHloRzHDykRgGyW_Ct1YR0mIBO49U-HsdF-LCkj_QkkJKVzGAOo0IhVQ5HzeXdxNLhB_PuLpVSKM1AvUEFzDf-_0igyQW40mBqLxNl8oFa5eufYNsRtLE0rpLrdsyZPr3rCH45dYltj4NoCkwPhMRbCDXy1VzWgW3jZydYqNtcegSea600bxToLefsjrki55DTVIJfHbWJPao8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=eVFXHbDBYexT-LLu9Lp_dWODt0qhAB1vrfMd8Lg-PSjZhfCJLHEUpi2s7M7icl6hBvRGrhXquP27_b0NlU9T-XXFhmgaYxvkvW06ocLDVbnd1iwGPm7MyLj7mA4YXE_RpaG9Me2VHloRzHDykRgGyW_Ct1YR0mIBO49U-HsdF-LCkj_QkkJKVzGAOo0IhVQ5HzeXdxNLhB_PuLpVSKM1AvUEFzDf-_0igyQW40mBqLxNl8oFa5eufYNsRtLE0rpLrdsyZPr3rCH45dYltj4NoCkwPhMRbCDXy1VzWgW3jZydYqNtcegSea600bxToLefsjrki55DTVIJfHbWJPao8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
❤️
حجت کریمی مدیرعامل تراکتور: حالا حکم کمیته انضباطی آمده است آیا واقعا باید خداداد عزیزی را در استادیوم‌ها راه ندهیم؟ آیا این درست است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105841" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105840">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=AH997B_BMIDYc7vbfa_VCVxphXiJbRuq6cknSXY1Gne5W7oTdZVyk5RxW3rZs2rUB9YcwWErQnHP8IJAgVRkcCj2lNT1h4qKrO4g_EkGTUCF77nBGI453aT_4sU6UUT4Q-KVW2W25CK-cdGIOMMs8gP1yy4dMR97JIFointerJaOYK-PTyP8GWCIAeECTNIF07evO7N-spKfC_V1TCfsY_N35Z-kIDGtRZjvNaL11-T_O9VK5xLbm7k3PSQHigCcxDuvH_JiuvFRpjlWesF3HWLjC7uIbqoyzBBg1-ScEk0Y6mjFAxq-L3vmbJVGEGhM2t8OrGtqCSL9h1S8TXLKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=AH997B_BMIDYc7vbfa_VCVxphXiJbRuq6cknSXY1Gne5W7oTdZVyk5RxW3rZs2rUB9YcwWErQnHP8IJAgVRkcCj2lNT1h4qKrO4g_EkGTUCF77nBGI453aT_4sU6UUT4Q-KVW2W25CK-cdGIOMMs8gP1yy4dMR97JIFointerJaOYK-PTyP8GWCIAeECTNIF07evO7N-spKfC_V1TCfsY_N35Z-kIDGtRZjvNaL11-T_O9VK5xLbm7k3PSQHigCcxDuvH_JiuvFRpjlWesF3HWLjC7uIbqoyzBBg1-ScEk0Y6mjFAxq-L3vmbJVGEGhM2t8OrGtqCSL9h1S8TXLKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
گلایه عجیب خلیل‌زاده از حجت کریمی؛
🚨
‼️
چرا به تماشاگرانمان گفتی فحش ندهند!
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105840" target="_blank">📅 00:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105839">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=b4X2GyS0ZN_al94AlQYHCHMpkbHcFiMukKmhwMnJvWSEAsSRH8iRhCv2RHzS3LxHrzawp_BeUNKNPkR64sd3fFauBeHdxfzoUI8rk3QzcDapkeR8CBMDFmSR-3sVcZeCpteD_FZNyvra5B4QB4ae8Nk3C-oAl7UxxxzCOfa2mj5aUOFSIbv8bYis4Rm8LW02QlqxALTVmkGZNoqqFyfmUzbKfpfWP1QCU7Ywm3IkCFWtNyN8YeGDjRXIkNJxIcFAr8kt1Kc31rSL-y4LYpag7sZ3cYayH01ZglHhVKZzdFofMlyxMXsM4Fk7aDG6qrn7x8Sz9_LJbrwflT9XTuCq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=b4X2GyS0ZN_al94AlQYHCHMpkbHcFiMukKmhwMnJvWSEAsSRH8iRhCv2RHzS3LxHrzawp_BeUNKNPkR64sd3fFauBeHdxfzoUI8rk3QzcDapkeR8CBMDFmSR-3sVcZeCpteD_FZNyvra5B4QB4ae8Nk3C-oAl7UxxxzCOfa2mj5aUOFSIbv8bYis4Rm8LW02QlqxALTVmkGZNoqqFyfmUzbKfpfWP1QCU7Ywm3IkCFWtNyN8YeGDjRXIkNJxIcFAr8kt1Kc31rSL-y4LYpag7sZ3cYayH01ZglHhVKZzdFofMlyxMXsM4Fk7aDG6qrn7x8Sz9_LJbrwflT9XTuCq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
به‌به آقا مبارک باشه. اولین لحظات بنزین ۱۰ هزار تومانی در ساحت مقدس جمهوری اسلامی
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105839" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105838">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: آن کسی که ویس را ضبط کرده است چرا به آبروی طرف مقابل( خداداد) فکر نکرده است؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105838" target="_blank">📅 00:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105837">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=CLelqLTzDvWNK31M4bvD4KRKuvgz9lVxohasxSShEz-PcJtNK2PI3pp3y8NRv8d7kh1HNqr7GwaWlQJ_-YBFs3YnYPOcb6iAjQj0BrY8FIqjAXgzIxKdt-vWSxluNl1k1hGxdHOY-JtyOP2JXX0sUk6oGFEjuWR2lzsfmNT6VusjjdrWhbhTfedp1Pa7mtrKfSDG3TOeck_YVmo0STqfm6IwrfXyhgfZytjJrtZgIRBSmo5omnS2RyHGF7SpN186EfAo1PB_9OIBWS6cpvHlZ3KRvgrNPI80M9LtMyBNc2-E5I4ocTlR654XiI-ELmrcY_lzGyaiSJjXdzLDRsoogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=CLelqLTzDvWNK31M4bvD4KRKuvgz9lVxohasxSShEz-PcJtNK2PI3pp3y8NRv8d7kh1HNqr7GwaWlQJ_-YBFs3YnYPOcb6iAjQj0BrY8FIqjAXgzIxKdt-vWSxluNl1k1hGxdHOY-JtyOP2JXX0sUk6oGFEjuWR2lzsfmNT6VusjjdrWhbhTfedp1Pa7mtrKfSDG3TOeck_YVmo0STqfm6IwrfXyhgfZytjJrtZgIRBSmo5omnS2RyHGF7SpN186EfAo1PB_9OIBWS6cpvHlZ3KRvgrNPI80M9LtMyBNc2-E5I4ocTlR654XiI-ELmrcY_lzGyaiSJjXdzLDRsoogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
حجت کریمی مدیرعامل تراکتور:  دیشب بچه ام از من می پرسید بابا قضیه خداداد چیه؟ من نتوانستم جوابش را بدهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105837" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105836">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❤️
حجت کریمی مدیرعامل تراکتور: حق نداشتند که آن ویس (فحش های خداداد عزیزی) را پخش و جامعه را ناراحت کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105836" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105835">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=cTp1T_7qbKpFCX11F9DSSe8UVb1qGz8QGqrGrlZAiZ-YLbE-QA9z8nIAYrqN0_nWsdBQ6KCd3m_9JHDbont5ZEjxeiv1lsV_BzwExM9qqn8nJT3sCDqbXHf12UG3UEVfuzW7uIDgTuHPihYiq8KcGO52SirjvPI6dLVArB7UcIHeQ-fd9fN3Ii3tn7nwzYD_uqN3uHninq25XiurfDkFJCGXdmzfKepkoP92U_hkVVkQB-XqwxXtZHT4CyxL-rJX1ZlezNERHzxLNmONnF4TH36MxsXSfb4GcUxZsAsiFgDx0vOvqBM7mJIjA-z8wz9vYhRDhZvyVU8JTSLh3dUCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=cTp1T_7qbKpFCX11F9DSSe8UVb1qGz8QGqrGrlZAiZ-YLbE-QA9z8nIAYrqN0_nWsdBQ6KCd3m_9JHDbont5ZEjxeiv1lsV_BzwExM9qqn8nJT3sCDqbXHf12UG3UEVfuzW7uIDgTuHPihYiq8KcGO52SirjvPI6dLVArB7UcIHeQ-fd9fN3Ii3tn7nwzYD_uqN3uHninq25XiurfDkFJCGXdmzfKepkoP92U_hkVVkQB-XqwxXtZHT4CyxL-rJX1ZlezNERHzxLNmONnF4TH36MxsXSfb4GcUxZsAsiFgDx0vOvqBM7mJIjA-z8wz9vYhRDhZvyVU8JTSLh3dUCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
😆
😆
عادل خودشو جر که فحاشی خداداد رو تکرار نکنه بعد همون لحظه واکنش سخنگوی گلگهر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105835" target="_blank">📅 00:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105834">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=fLtyj0-A6qLMNE_bqt-_BdUayH8Az49hrztSjuX6gRTc0eEArcvXTp9RtjJHhRbRLlNzFXvEKqyyLTfIpoiM4pfP0CIcmMomNt5Q2NCllN90ifiUhAgGxzCG-aj3XbxNkVXgxL2yjQWgmDALdZR-TbzCeXJT_NeBPTVkBHxTFtTq18TcGiDal0OwI278H_tw4RIsRg8B6vfbd7zG6htx2J5noWmMiNdM50ultSBM1Ed8y3ZqVQfDIK0yjzcch8S1peHADFArdqa1NsqzG1Yg9lWnSHWZP9OPkOyyjALWKJuAfFHBGQ-vue668FnQjqvV2NcwtY-Gf1e2eFDhu5WBfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=fLtyj0-A6qLMNE_bqt-_BdUayH8Az49hrztSjuX6gRTc0eEArcvXTp9RtjJHhRbRLlNzFXvEKqyyLTfIpoiM4pfP0CIcmMomNt5Q2NCllN90ifiUhAgGxzCG-aj3XbxNkVXgxL2yjQWgmDALdZR-TbzCeXJT_NeBPTVkBHxTFtTq18TcGiDal0OwI278H_tw4RIsRg8B6vfbd7zG6htx2J5noWmMiNdM50ultSBM1Ed8y3ZqVQfDIK0yjzcch8S1peHADFArdqa1NsqzG1Yg9lWnSHWZP9OPkOyyjALWKJuAfFHBGQ-vue668FnQjqvV2NcwtY-Gf1e2eFDhu5WBfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
❤️
حجت کریمی: اگر خداداد عزیزی فحش داده است حتما یک نفر یک کاری کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105834" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105833">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=mJZ5qnUu4pCqXQOOUAQVpVNvRiF4KQMsYBH59et2RZK7NQvApOGjMkx5lh-YqKgjvy_4VIIGSN8f-W-TluLqKDCI62-nRO7opQmqMdb2arcYifeHI6gT5ud5vQflXR0Yvyslbsshj-2iRicgtWbiF9aOQg0jrO8_DYUjK456PITdfZ_nYivr9zXdTvK6Fkhz6NgNub4AOiGmMcP5WqYFD-hHgAbGgXL-Zuvb_kYllkmLCVCAywgPJijvH9warMTaY_Qp8S49WfI73eiS8K5cAp7e54WjkBTehhVGhg6orREHZ93uXcRs9GZTGh2D7-Nlxodq7DGi_eCJXt_Zg5EcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=mJZ5qnUu4pCqXQOOUAQVpVNvRiF4KQMsYBH59et2RZK7NQvApOGjMkx5lh-YqKgjvy_4VIIGSN8f-W-TluLqKDCI62-nRO7opQmqMdb2arcYifeHI6gT5ud5vQflXR0Yvyslbsshj-2iRicgtWbiF9aOQg0jrO8_DYUjK456PITdfZ_nYivr9zXdTvK6Fkhz6NgNub4AOiGmMcP5WqYFD-hHgAbGgXL-Zuvb_kYllkmLCVCAywgPJijvH9warMTaY_Qp8S49WfI73eiS8K5cAp7e54WjkBTehhVGhg6orREHZ93uXcRs9GZTGh2D7-Nlxodq7DGi_eCJXt_Zg5EcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: به دلیل اتفاقاتی که در تبریز و در بازی با گل گهر افتاد از تمام مردم ایران عذرخواهی می کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105833" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105832">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
با استقلال تفاهم‌نامه امضا کرده‌ایم
🇮🇷
چیزی ۱۰۰ درصدی نیست!/ توضیح محمد خلیفه درباره جزئیات تفاهم آلومینیوم با استقلال؛ که حتی خود از بندهایش خبر ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105832" target="_blank">📅 23:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105831">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های سخنگوی باشگاه گل‌گهر در خصوص فایل صوتی جنجالی خداداد عزیزی؛ با صدای بلند فحش می‌داد اما کسی از رختکن گل‌گهر بیرون نیامد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105831" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105830">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‼️
آدم عارش میاد بگه به فوتبال علاقه‌منده!
مقدمه عادل فردوسی‌پور قبل از مرور پرونده بازی جنجالی ترا‌کتور - گل‌گهر؛ این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105830" target="_blank">📅 23:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105829">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=N486B8v-zGbssnnM6UiJ1H5iKThHy1FhXnMW5BgZinhwsYbFGFauHq10hh1I525RlOtNxisuqE4W1Boi7A25ZOCjJYYu6Kq7HfY_drvqVOvC1vJ45tQqb7nTpqZXZsDWkGFRtef58UeWYkuDMsiH9qatq3N3o62M0_ORpopBUEN0_irkWfZkDytvTLXV2hZ_FtpxaroktaxqfCbo4eUg2Qo5l-XoNKoxbk4oj9wc_4m_9ZiiSSqapC9-6y77l-1ryQUU52_sHuuEO5FYIfv_AOt0iyW0yAAX0LUIX4S3K8f3oliqFdTh2l7Yg--dD7O0sP8P1zJrqsNaQ-Y-iXSCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=N486B8v-zGbssnnM6UiJ1H5iKThHy1FhXnMW5BgZinhwsYbFGFauHq10hh1I525RlOtNxisuqE4W1Boi7A25ZOCjJYYu6Kq7HfY_drvqVOvC1vJ45tQqb7nTpqZXZsDWkGFRtef58UeWYkuDMsiH9qatq3N3o62M0_ORpopBUEN0_irkWfZkDytvTLXV2hZ_FtpxaroktaxqfCbo4eUg2Qo5l-XoNKoxbk4oj9wc_4m_9ZiiSSqapC9-6y77l-1ryQUU52_sHuuEO5FYIfv_AOt0iyW0yAAX0LUIX4S3K8f3oliqFdTh2l7Yg--dD7O0sP8P1zJrqsNaQ-Y-iXSCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
فولاد خوزستان با گل دقیقه ۹۲ احسان محروقی مقابل فجرسپاسی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105829" target="_blank">📅 22:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105828">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=rqfnnWRPXlSv4Hf41T3xZLgXItACLSCQ_IFRKKzzwqicQFxjLEEuNnkufKn8x4jflQBfgQc4vE_ZOtw7RfaU8af91A5VNHc1tqX9QOdJs-7Sd1uOl1Xgq_bVCqATWxVFQ9XmTTjVqN_CuPoMtJJUvrAXhWINQ_Sg8K4RxuxLowVMg-7i6omvdpdlsAa07BxxTYLCjea0LZJAioeiPSebxJdAoP-RPzsUKVWObJdHUEMFDL0t49zZfr5c3zhdWYILa5rGHudZnwexs-tOl8uRLYIUtKKma-jCvz2HFQDr-cVnCdg8mq-BTZV348RXHeBMZRdEA03NhXWOldU_dga33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=rqfnnWRPXlSv4Hf41T3xZLgXItACLSCQ_IFRKKzzwqicQFxjLEEuNnkufKn8x4jflQBfgQc4vE_ZOtw7RfaU8af91A5VNHc1tqX9QOdJs-7Sd1uOl1Xgq_bVCqATWxVFQ9XmTTjVqN_CuPoMtJJUvrAXhWINQ_Sg8K4RxuxLowVMg-7i6omvdpdlsAa07BxxTYLCjea0LZJAioeiPSebxJdAoP-RPzsUKVWObJdHUEMFDL0t49zZfr5c3zhdWYILa5rGHudZnwexs-tOl8uRLYIUtKKma-jCvz2HFQDr-cVnCdg8mq-BTZV348RXHeBMZRdEA03NhXWOldU_dga33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
واکنش کنعانی زادگان، بازیکن پرسپولیس در مورد حواشی دربی و ضربه اش به عارف آقاسی:
در فوتبال اتفاقات زیاد می افتد/ نمی خواهم به کسی توهین کنم و یا ضربه بزنم/ شما دنبال این هستید که حرفی زده شود/ هیچ کسی مشکلی ندارد و همه را دوست داریم و به همه احترام می گذاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105828" target="_blank">📅 21:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105827">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82451c129.mp4?token=C8-mBXoZhpXE6D50-_Glb_-iFPCLA3wO1b3Gv1aZFZctL324W51jKCwoJ4D7D3R8M-T-hK_is1wstHpE3lZCGV5qc53j9G7fOkARazMjm9LNL_HcJ_jK9ODMA7NCp8qOlKE5K03deT4CWr0-J1N7UXO6Jjt0ioFXbcFewGBP9sGyle01nC4QA99Z5JCw9-jl-rW9EluKdNdD_1yIoxmlCrUNl4r8KHPpuiXDrBUWvsj0pB0iZ1QStSgfDzrveIG8CUBGeroXMXCB__Lbe3nSB9cn9INhy0_Uv2-3LGezb2LdT_tmCKGPs52IYnkxWcTM_V6g8h0lfCUxre-E29URNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82451c129.mp4?token=C8-mBXoZhpXE6D50-_Glb_-iFPCLA3wO1b3Gv1aZFZctL324W51jKCwoJ4D7D3R8M-T-hK_is1wstHpE3lZCGV5qc53j9G7fOkARazMjm9LNL_HcJ_jK9ODMA7NCp8qOlKE5K03deT4CWr0-J1N7UXO6Jjt0ioFXbcFewGBP9sGyle01nC4QA99Z5JCw9-jl-rW9EluKdNdD_1yIoxmlCrUNl4r8KHPpuiXDrBUWvsj0pB0iZ1QStSgfDzrveIG8CUBGeroXMXCB__Lbe3nSB9cn9INhy0_Uv2-3LGezb2LdT_tmCKGPs52IYnkxWcTM_V6g8h0lfCUxre-E29URNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
❤️
کنعانی زادگان: بازی امروز خیلی سخت تر از بازی با استقلال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105827" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105826">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=vFZQpt_pC30gj4TzOQoi_02kyK905r7R-xPdBy0LyYwrOl-Hfup7PW079FRCG1A8qRiT_cr727E_c2maed9wf3ZJCaLdDI5KiUWrYgwzITVT2ta-H1Okl0ek7C3d4RtncimnIDIuPjSFCQpG14c5qb0hcVqzh7dUhTmmXVv4X-9yZc2ReOtQNbszSoP_kYMP5vEMMWfTyMndiqvUN2a78XJpBmt-pL9QC4B1yV030jP0xLSqo_9MJsSdzpNTqpsvJk-FMTJNyXFC47PCsPBGxbFF8lLfY96joJ2GIUv7xvJKxe2Qdz1X7MZkDhmqUdL7z1bitw2982HdLYSJT8jQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=vFZQpt_pC30gj4TzOQoi_02kyK905r7R-xPdBy0LyYwrOl-Hfup7PW079FRCG1A8qRiT_cr727E_c2maed9wf3ZJCaLdDI5KiUWrYgwzITVT2ta-H1Okl0ek7C3d4RtncimnIDIuPjSFCQpG14c5qb0hcVqzh7dUhTmmXVv4X-9yZc2ReOtQNbszSoP_kYMP5vEMMWfTyMndiqvUN2a78XJpBmt-pL9QC4B1yV030jP0xLSqo_9MJsSdzpNTqpsvJk-FMTJNyXFC47PCsPBGxbFF8lLfY96joJ2GIUv7xvJKxe2Qdz1X7MZkDhmqUdL7z1bitw2982HdLYSJT8jQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😢
🇮🇷
واکنش جالب هوادار پرسپولیس به عملکرد تیم
:
بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل می زنیم 3 تا به رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105826" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105825">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پیمان حدادی، مدیرعامل پرسپولیس:
🔴
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105825" target="_blank">📅 21:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105824">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr8YHhPrI7fBVBS75SKOvmaeVhXnD1ZMvERNm8Fzp000k0a3gf9ZMXk8eGze0CTKGq8WLlTO_gT6TM0BkuxbQwRdE9cn3o8B-JVr9O9uidqUDxYdEpjyiSahceh7KVJlVC8gAbXcVGAli0Ufp8W5d-9Ue29__BU5tKqz8eu2YbDnAl5_Ii3U7DM6GI8L4oiYTPz1nt581hJ8yPKvWQWL8EkStJS7LgvzgFIyZuP5dAE_Z4p9nO5TJ95mbDnMLlijivdJLaU3zsdZOpqIHjbuUmBfhemTy318D-haI62SF-yuEs1MFe18J5G6uvSAgbKYiqfxb7TX4SAhYTKhhrejEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
عبدالله ویسی، سرمربی ذوب‌آهن پس از دیدار امروز مقابل پرسپولیس از سمت خود استعفا کرد. ذوب‌آهن با کسب ۶ امتیاز از ۶ بازی در رده سیزدهم جدول لیگ برتر قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105824" target="_blank">📅 21:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105823">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtvTnmwRNmyF797dIwujCkef3W3lNsjDfeEq517tqkw8LGMWZ5qFKfKVI8RwS3sJjxyoq90LDJ8ofVdj5uRnKJqGvlkf1aBjWQE1EeFGUwf3BEmzHG_-MOVGalp5ywSV-rlNEgwiJoVlRPdweS3FSdgNaU3nv5KGeiZ8M2wnUW3Gr0pJkGKJncSYtkcLsQJXieVGly9lCoaEs9xh8dolBels_0ezWrBOrul7xsHwoPyRAuBlyushDgFhGUpYSNMQsxWsyufXik9ukbRy3f7nS1jp_QKeYDUuTESHTyYV-_oRhIBFnhYrrUMkoiNsWpydJSlehkMW7tvzj8cgnJCtOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105823" target="_blank">📅 21:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105822">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr_DJNBdWz8A4rCYO16AgUW9hiNJSzlG8kI0cFtCzCcJEHdbmfGypr7SLXwwGHVuf-rbMHD2O5dXkx4IAWmeJUQNy17CwETz_N4hPwzFdEhSfmX2ZeIxds5f1zsPiwK5O5HP_MC91QK6JHn0o6VEu3tm04d7ULb0usmE8E-ncGjDPsst5qWS9ughevqc5Dbg4OAeOGeQ0Cg4tpK2zGNw7R-fz1pdI9ypUU7YyxUi-kCQ8F3o-7wQZQqzmpGdS0wgwxmjc16da5D1pvpaRapPiN6ue4FYG1s7qwZYAqBcbq425jCU9rY30cRcihMVq6rEDN6bum0inxduVxTz4TlNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105822" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105821">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=DQRyAPqLkOGzFsWhbT8LSjaAIGDp4hcd2e6BoQY4-zNxB-RqMlz36Nl2E9iHjEsTuSP-wUv60MEFlpJzpfhKeNjH-CHULh9DurMl1E4RvYaWimYWy-Qrde-O2H3JyETSz0Y5z34Q9MbON_fupMvMWNNzsk_fqtBn7Jb2XVJOOHCQVquCwKti29DAAjAcAvFt90T-CS6POQ1c5hRwCjzQTIUW9kB_XEB9mQ1RTGMSzqUSTk7uOs4SbPScWkgfm0LY3dgqXzDvzbDKROYTEzT9cxIRVrXUQMGv9GuUFjgWCj7dVHB290OykI57ueJH8mHGl0tMWaKPRyT4lmRjk6Qf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=DQRyAPqLkOGzFsWhbT8LSjaAIGDp4hcd2e6BoQY4-zNxB-RqMlz36Nl2E9iHjEsTuSP-wUv60MEFlpJzpfhKeNjH-CHULh9DurMl1E4RvYaWimYWy-Qrde-O2H3JyETSz0Y5z34Q9MbON_fupMvMWNNzsk_fqtBn7Jb2XVJOOHCQVquCwKti29DAAjAcAvFt90T-CS6POQ1c5hRwCjzQTIUW9kB_XEB9mQ1RTGMSzqUSTk7uOs4SbPScWkgfm0LY3dgqXzDvzbDKROYTEzT9cxIRVrXUQMGv9GuUFjgWCj7dVHB290OykI57ueJH8mHGl0tMWaKPRyT4lmRjk6Qf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از مشخص شدن محرومیت 4 ماهه خداداد عزیزی، پرسپولیسیا این شکلی عالیشاه رو تشویق کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105821" target="_blank">📅 20:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105820">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=LiMzzHM0t90NpstCj668gseFuiTADckZZMZksYF6H4NpkncdABJIgD-M6XM342W_H48nL-ti5NEOIe6LSkL3OfA3bLdVgSqFHZSzGsZwA_Ri6wRZHYalucFMi7-JBsTWgU4GXeWA830UX4ikWylD90fWsyBOyfi8CAO2Y-4Tr0g-inirzfAGvwY-7xB0RtbSR_Nru3xYOTqlKyfuqmQYTivy8-LOof_7STOo67-lEYDFfX7mJZnSLvN7roVpD6Q5VdWqrZvrLswA7hJkm3k8c2bqqcHj_DJUntEhr3C_MKFYyriJPIFo_Yiec5_z9oeEcgt5wdJ__LM7IXegdh9P-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=LiMzzHM0t90NpstCj668gseFuiTADckZZMZksYF6H4NpkncdABJIgD-M6XM342W_H48nL-ti5NEOIe6LSkL3OfA3bLdVgSqFHZSzGsZwA_Ri6wRZHYalucFMi7-JBsTWgU4GXeWA830UX4ikWylD90fWsyBOyfi8CAO2Y-4Tr0g-inirzfAGvwY-7xB0RtbSR_Nru3xYOTqlKyfuqmQYTivy8-LOof_7STOo67-lEYDFfX7mJZnSLvN7roVpD6Q5VdWqrZvrLswA7hJkm3k8c2bqqcHj_DJUntEhr3C_MKFYyriJPIFo_Yiec5_z9oeEcgt5wdJ__LM7IXegdh9P-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی
64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105820" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105819">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105819" target="_blank">📅 20:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105818">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4eCFHFkc0ydDoxPMHoM1mwsBvzjjzE-6LxoAUiaGvUphLbqL0AIiQV9gikApCY1rIQq-418oIBMaWz8HieFaihEi_9sYwq5Dw1yMXVx7KWF0XnBsKzXr6FZyGUpJ0llJpAtHQdMmt-n-mW-zo-8dPZ-IckV55ixl9Ggs_WsXlDd3A2_Q5diAI_fwos1U915A8M9hMFavoh95WeYf432t1PX5CzGBjh_iXQ5HlX8gmclp5k6-zAq1gZck8JMIF32b6FKGnFAuQc3G5K-43ZIov6tgYaYUM0CIw_Exq4-jDsdh6EulKzTWKXJ4PDdH2Klyxv6HeFZ1mZ-gZ3GjAHHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105818" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105817">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1X5iE3pL-1V3foakFpqql0IhfZeOPGD7afNuJhstuxZ--qwFA376jKHY0tLRa3QZtbrSYjfnehXDuwsTw24em37Z1-pMQogqBMogD3Gv9_R3Dv8t-7GpFLrE3aOAEkDcigjH52mjrifJpX_XBg73f_2GSXh_s7e_LrmEtxd3kIVH9MaOMRgT8p4t8W7BI9owN30bcEBolwaNndwBDiRzTFfKAxgU-yVp9g-W_T3FpZo9X6fwLIOyfZfH4RKmxozjN181kZqyoPBkTO_atwoZrNjG0DUfjw7kDIWYdurQZnQp72vNFPy15J9fCcEMSSXCnEHayo-57hXW0JzJJ_MzHoEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1X5iE3pL-1V3foakFpqql0IhfZeOPGD7afNuJhstuxZ--qwFA376jKHY0tLRa3QZtbrSYjfnehXDuwsTw24em37Z1-pMQogqBMogD3Gv9_R3Dv8t-7GpFLrE3aOAEkDcigjH52mjrifJpX_XBg73f_2GSXh_s7e_LrmEtxd3kIVH9MaOMRgT8p4t8W7BI9owN30bcEBolwaNndwBDiRzTFfKAxgU-yVp9g-W_T3FpZo9X6fwLIOyfZfH4RKmxozjN181kZqyoPBkTO_atwoZrNjG0DUfjw7kDIWYdurQZnQp72vNFPy15J9fCcEMSSXCnEHayo-57hXW0JzJJ_MzHoEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به ذوب آهن توسط علیپور(43)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105817" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105816">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بالاخره پرسپولیس زدددددددد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105816" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105815">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">علیپووووووووور</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105815" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105814">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105814" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105813">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=OWMigy3_P3juxGcwD7GOOc2aSpnd_YYje1ALWZuXZuPhCqX8INpzCMOCx8ItWpCHC1734ZD2glbn73dTuJgVAQDuqCD4JHFOM1wL4YQ9JMgFBX-nmBrYgF6WVd8wItO_CkN62nf5gQjbiH8G_oNbaQR7Y76NIsrzUw4YUEvMRlbdEQvS3Z7Syy3_15CSk3uJ3DSSDWNNfJe9zRpBVTG2BGan6oUA5wRtGa4tthMlEZpqvNa8O-Fb1wj5mH1ThNJD6K17ws_ipj0u1GADykw3CXSARE6GemV7gMPGwq90Zs-X_HPyxapex3TehxlI-cHhvofPwj-9qI5Kl3hf3BNFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=OWMigy3_P3juxGcwD7GOOc2aSpnd_YYje1ALWZuXZuPhCqX8INpzCMOCx8ItWpCHC1734ZD2glbn73dTuJgVAQDuqCD4JHFOM1wL4YQ9JMgFBX-nmBrYgF6WVd8wItO_CkN62nf5gQjbiH8G_oNbaQR7Y76NIsrzUw4YUEvMRlbdEQvS3Z7Syy3_15CSk3uJ3DSSDWNNfJe9zRpBVTG2BGan6oUA5wRtGa4tthMlEZpqvNa8O-Fb1wj5mH1ThNJD6K17ws_ipj0u1GADykw3CXSARE6GemV7gMPGwq90Zs-X_HPyxapex3TehxlI-cHhvofPwj-9qI5Kl3hf3BNFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جالب عبدالله ویسی به خراب شدن موقعیت گلزنی تیمش مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105813" target="_blank">📅 19:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105812">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=sykWKo_KNCKXKvmOELdMBBSo64IGQHVniWCA-GBxoK5LhFpnWR9XVyd8W0F3QMwlAF-QzVzfO5_dKmfw4uDXCfBdCkXps0QJXlFRj85JXG1DsvujRrcKUXof9BPCXLqp7nzPY-vBK5LpevuJyyb10Fqkv5i8WJMI6E4OuHcG-jC5GPPZcmQ2Y1XquYcQA_lScebR2HkHT0gY7vgUx21AXBsuQ8tBe3BMiXlXv9Lokr4-SgYfHP_M8WJDdGECxVDswIIYB2znS0H04JZYelv8JZGTWI4U8CGbdPUZJvuU2rnZm-Lzeiai5nf0fyidAhmSxMW7_HbE-gIod_yoisFv0XVmmZCEQ_496rt2HuD5necFqUFJViNw1-Tp1cstUYPOkmUglBuSa_FJ9Da_1SGU5qUIjoII6-r5lg2z8oq529OxdNRr0ujKnUtVJGi_6NSFhf1YCZ11FRdH0B0xoJ3n95qkIOQCJaFuh-w72Sya-o2wnqyimrLSQCFczTc0xJGcdjA_vSwFPu8mcCi7Jjc6eb1CN4mKWLwDGjN1lK78MFsWRW7v1DXSWOhSyBs3_EIgKNj5LtKlkSUl739Kq05QXCPXq-2-cWRMyaCDe9bhni6uzkHs21a4OKscutojXTjdwEBj8sMAYGDrv1z0EHvTziMPCVrVAkzOVdapHxcy8Fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=sykWKo_KNCKXKvmOELdMBBSo64IGQHVniWCA-GBxoK5LhFpnWR9XVyd8W0F3QMwlAF-QzVzfO5_dKmfw4uDXCfBdCkXps0QJXlFRj85JXG1DsvujRrcKUXof9BPCXLqp7nzPY-vBK5LpevuJyyb10Fqkv5i8WJMI6E4OuHcG-jC5GPPZcmQ2Y1XquYcQA_lScebR2HkHT0gY7vgUx21AXBsuQ8tBe3BMiXlXv9Lokr4-SgYfHP_M8WJDdGECxVDswIIYB2znS0H04JZYelv8JZGTWI4U8CGbdPUZJvuU2rnZm-Lzeiai5nf0fyidAhmSxMW7_HbE-gIod_yoisFv0XVmmZCEQ_496rt2HuD5necFqUFJViNw1-Tp1cstUYPOkmUglBuSa_FJ9Da_1SGU5qUIjoII6-r5lg2z8oq529OxdNRr0ujKnUtVJGi_6NSFhf1YCZ11FRdH0B0xoJ3n95qkIOQCJaFuh-w72Sya-o2wnqyimrLSQCFczTc0xJGcdjA_vSwFPu8mcCi7Jjc6eb1CN4mKWLwDGjN1lK78MFsWRW7v1DXSWOhSyBs3_EIgKNj5LtKlkSUl739Kq05QXCPXq-2-cWRMyaCDe9bhni6uzkHs21a4OKscutojXTjdwEBj8sMAYGDrv1z0EHvTziMPCVrVAkzOVdapHxcy8Fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب رحمان جعفری مقابل دروازه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105812" target="_blank">📅 19:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105811">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=u4xycr05jETrfnFxfWZ-8RKDs3IsPYZ8kCC1L21peVcrLbyUs_WBMJBDM26KWEeHu8HfjAD3dCPOyfXCjfSCnHcduxs--5XUjtWlVvBmQAHheanmOjpsvtWlYmlF_HaZvKzFp8d63Jb4sArTwHLoGbF7hksWoEMGxs5rttd2L9sSI1lhXlwcMTcMhWd94dDWQOTXCS_31ABNYP3W1y5cOgIOjvd4HgNVjzOi2xKopQ8oaGmK_X6G7U1rtznWATn3YCJp4q85gYhDYg9jvH4zzeQV39oZkwnS9Axcm14iNzShSw2kgn64X-94G7q_WVZoAZi-4bHhVXOR8zZM3ltOhz5DABGicqEMyr19lK7o9tv6y0V9Z6CcBhG0LqesHnqZdddiVfKB7KpaPd1VDKGSzbn6XEd6Lt7JdudLeg8BNsjC5rTUWgfANmaJ5JiylKVkl5gyGwPrfHrNx9iTpmAz-aXirFeuz5sl7iQlSWQAwd_755n-Kn39JLvUKjCD5wwX_4gD_cjNwqrU61wbosszTv0PaOhzU9-KLdn7e7Gjr9GfgcMQJJJn_wwxQu5l8kMRXbb-dQ35_Nz2PMe-GNBAEdP7MiaCPT_SjBU0JrkkKOM3gkSFxIwwLgnB2OMu0e24NR54lW7dBdcC7KAi4o0Si_7DrYndO-yUUKchADmIp_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=u4xycr05jETrfnFxfWZ-8RKDs3IsPYZ8kCC1L21peVcrLbyUs_WBMJBDM26KWEeHu8HfjAD3dCPOyfXCjfSCnHcduxs--5XUjtWlVvBmQAHheanmOjpsvtWlYmlF_HaZvKzFp8d63Jb4sArTwHLoGbF7hksWoEMGxs5rttd2L9sSI1lhXlwcMTcMhWd94dDWQOTXCS_31ABNYP3W1y5cOgIOjvd4HgNVjzOi2xKopQ8oaGmK_X6G7U1rtznWATn3YCJp4q85gYhDYg9jvH4zzeQV39oZkwnS9Axcm14iNzShSw2kgn64X-94G7q_WVZoAZi-4bHhVXOR8zZM3ltOhz5DABGicqEMyr19lK7o9tv6y0V9Z6CcBhG0LqesHnqZdddiVfKB7KpaPd1VDKGSzbn6XEd6Lt7JdudLeg8BNsjC5rTUWgfANmaJ5JiylKVkl5gyGwPrfHrNx9iTpmAz-aXirFeuz5sl7iQlSWQAwd_755n-Kn39JLvUKjCD5wwX_4gD_cjNwqrU61wbosszTv0PaOhzU9-KLdn7e7Gjr9GfgcMQJJJn_wwxQu5l8kMRXbb-dQ35_Nz2PMe-GNBAEdP7MiaCPT_SjBU0JrkkKOM3gkSFxIwwLgnB2OMu0e24NR54lW7dBdcC7KAi4o0Si_7DrYndO-yUUKchADmIp_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
عایشه‌گل جوشکن، بازیگر و خواننده ترک، در گفت‌وگو با مجید واشقانی در برنامه «رُک» از ماجرای آشنایی و ازدواجش با همسر ایرانی‌اش گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105811" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105810">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoclFuNI991p2U4frBQByIFASk2r1d4MsASmsMVUiPI71r3JWLOgqRitZk7DTHfn7tygQ8DoFo6yc1cXDTowLxuK4dR1s5gEPwbzkyjXTVEZ8ZkS1NOKQaq2XfXlUD9srIHVdxVkb7IJCH9LCn2fH_RBJhhSSKcZVfXlmmxSImiryReQwdeY7SdaUiEaJ6K4HgqgLnstAOMe0iG8s1kuyIPkS-U4ENTCJgbpXLUDZicoYhjCczwnbTU_krJxGVLh8odpuYbwxSyyo8DS61Ae-_2TV4ZugjwS5eYIwEvhRrlBT5WpnnyqzyX7sQ7at75qppbaZuwyCWV2Df6TQ36E6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105810" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105809">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkGJ9BniSYEe94loRmaLmInJiU-a3bZ2Eo9uO-iCzXghizqDXffPQSwMtTLLzzXMp3JTswEJx2cRvHwqbAjVJ9TYqubOiMkuaYMabhIj-I4IhQJsfLidZeie-uN4C2ayIBScTbQdFVYE_9-DIkf6fr8nlQWQJ2IonurCEyF_k5ERg5Vx6vOA2-wfeFvtZLwGeWo1WbDfrmvMKjOdRILT21SfLqwP6AK0NSgPNJVwtdM8OXauDRiyVB2rDTZN7cXixYIiy9luyb6nkLai_iJkCzPPiFmsjMs0SWRO6FhmfmqNxrg9dLlExq2zGTN8Ca8u_XUT3zgLShQa-nnO6x6gJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
اگر حق رای دادن را داشتید، به چه کسی برای جایزه توپ طلایی رای می‌دادید؟
🎙
کیلیان امباپه:
🔴
من برای خودم برای جایزه توپ طلایی رای می‌دهم. این یک جایزه فردی است و باید دید که بازیکن در سطح فردی چه دستاوردهایی داشته است.
🔴
برخی می‌گویند که من یک فصل بی‌نتیجه داشتم، اما من هرگز برنده توپ طلایی را ندیده‌ام که تمام معیارها را داشته باشد. آیا بازیکنی وجود داشته که به طور یکپارچه توپ طلایی را برنده شده باشد؟ نه. این بدان معناست که همیشه کسانی هستند که فکر می‌کنند بازیکن شایسته آن نیست.
🔴
اینکه من بهترین گلزن تاریخ جام جهانی هستم، چیزی است که در ذهن مردم باقی می‌ماند. اینکه من بهترین گلزن تمام تورنمنت‌های بزرگ هستم، جایی که بهترین بازیکنان بازی می‌کنند، لیگ قهرمانان اروپا، جام جهانی، نمی‌دانم آیا کسی قبلاً این کار را انجام داده است یا خیر.
🔴
من کسانی را که با من مخالف هستند درک می‌کنم، زیرا این یک دیکتاتوری نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105809" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105808">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=dCp-kLcLGTvOXv5ba8qm0HguR63ludOiews0UlPCXBqmy_QRJcMCY-PZ0S_QWJPzIKvqvyEsEbFkBtDAr9kxP_68JXWmbFTOhxXMAChT_pSSBQ2Q-WscwISewHeAThyBDcM2oSRxIlzQ56zkvC9kM36c9TFtvNSwff9bEWDZg05DONOLDSEXRXC3X_jF4My1zD94dhuU-FQdTH3NcRbs7fF5A1SEkA-NGBMQSd4G_Vg9Z0jfopflDRdeRtm1cmb1FF0QFapr0erJJaW0D8BOOPxnzKEtpSJtvxE49i8wa-WCaGUY8sJ94A7Aocglsqdlak-_viYO2JAdhVoeZYOX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=dCp-kLcLGTvOXv5ba8qm0HguR63ludOiews0UlPCXBqmy_QRJcMCY-PZ0S_QWJPzIKvqvyEsEbFkBtDAr9kxP_68JXWmbFTOhxXMAChT_pSSBQ2Q-WscwISewHeAThyBDcM2oSRxIlzQ56zkvC9kM36c9TFtvNSwff9bEWDZg05DONOLDSEXRXC3X_jF4My1zD94dhuU-FQdTH3NcRbs7fF5A1SEkA-NGBMQSd4G_Vg9Z0jfopflDRdeRtm1cmb1FF0QFapr0erJJaW0D8BOOPxnzKEtpSJtvxE49i8wa-WCaGUY8sJ94A7Aocglsqdlak-_viYO2JAdhVoeZYOX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
بازشدن پرچم 6 از سوی هواداران پرسپولیس و کری برای استقلالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105808" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105807">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=CRnWLrQVydy_jU_pvDbzLacBoiKK8Vcd384dXHa2re7wv4cFBMqrLcGKzVSPhKViiTEUa4fq6zaiQVYnm85ZJ3JDl5oOXU-uI_aaSa9MQZPPCTq5gGSDDmZvD90zS0AOqUesWZeCO1rGY7yXe_d9AiNt37NvoLTIvEb6I0qcgq4r5t6HbJeiEY-uVDGaSDMVaSI2K2HGmTstoUXhp4OTnDbS2o6HhH3IMnRPdQVdhjEryvA2jAkytIl2tjIg3shH5F8W8Dkm1JXzVQ-ADDLso8VnT3V_V4b9-nqinbCaQZWGSj5XYeWPvvPsafu5usR28p-vBUMoXvAr6ricpPFaig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=CRnWLrQVydy_jU_pvDbzLacBoiKK8Vcd384dXHa2re7wv4cFBMqrLcGKzVSPhKViiTEUa4fq6zaiQVYnm85ZJ3JDl5oOXU-uI_aaSa9MQZPPCTq5gGSDDmZvD90zS0AOqUesWZeCO1rGY7yXe_d9AiNt37NvoLTIvEb6I0qcgq4r5t6HbJeiEY-uVDGaSDMVaSI2K2HGmTstoUXhp4OTnDbS2o6HhH3IMnRPdQVdhjEryvA2jAkytIl2tjIg3shH5F8W8Dkm1JXzVQ-ADDLso8VnT3V_V4b9-nqinbCaQZWGSj5XYeWPvvPsafu5usR28p-vBUMoXvAr6ricpPFaig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105807" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105806">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105806" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105805">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ianA4f-eFRbAV0143FJUVyKpseVAhcXtcxNTUu3BqKMNP4ysnP9p0_-B1aX97P3LrwLTTfFNd0_AQh2dbfUgZo141DvfYq4Fu7mTbfN15q8fXZNC-IibROCYngKrpMtGB1Ud59hHAGyvnh3ru55AZtgvKC9rhc9QQCeizLqBn95-XQ7M4RCuXAlPZdsC6tuPNtTVPUs3CwPeMrPlqw893Ovz6U7cBkAbqQ-ocTAi0u0XWHOaK4qPvfnlxmv6GD-XCX0hA_E5MJwwriR3BobEqta_rkbXVIt7KNogUpzNq8xCSl8FuuOHtjtcm0eLm0h3aZOQSHQz3k78S4o6xH1lPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105805" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKuXGYCxoF29JUru21Am_sIBSUlk_QL4ZazOPRgsgSprcPijJNZ7TcWo03EkkERtpPWXokzLPsdynzI585CTokwJoDGZ1GhBZw_MTqAo_ooaIv91Lv9S_e82l464_13oCqLh6xjwDGZpGqdHLxbAN6hvQX182m-zdU-rhqgQ2iTWJkf6tEPI69rNu8PXPHgT7b9pE_aGFa_49Pqoiwr_Ch8gySmVPi-OU92IhMMC6iBad0hrbJW8iFETgE8fLNvojqkqwGsGhzGONxgri_RrhgjLgWsbksYKE6GEGXU1xWyyYSWc6woSWg_ltLq7-kjMgEhjAa4VGXBrY5lXcu-ZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
شماتیک ترکیب پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105804" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66914acac.mp4?token=RRJU2vR5xF9FpmUj_l-q555Yz1jPo0NQYSXVx_MXUZRPK7SZXKRC502lHoQ26gxKAI6BsitTgrHvmm_3Jb5ABEvsabBerFlNWg3AqUTSfsaG1vcdzmZU-aCXVazwWRZFPzEc1xUZcX1q4TW2hFhbYz4nNwByLONlG-xJcoZ9kaZdMXH8SsvtObiYh1UYfc32rZ8J27zN99bAPtU07od_NGWq9YJzy20ZqNyyKdPby9C7RuqSRNSI7rz8k6ZEW62w9ZuYvhlZMlxy-0qnhewC8d7BopiLG5A1j0NnH2153_XHZ0YW_EHPv36V7aBZn_JVl202teFUyo0rgCEMsUepFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66914acac.mp4?token=RRJU2vR5xF9FpmUj_l-q555Yz1jPo0NQYSXVx_MXUZRPK7SZXKRC502lHoQ26gxKAI6BsitTgrHvmm_3Jb5ABEvsabBerFlNWg3AqUTSfsaG1vcdzmZU-aCXVazwWRZFPzEc1xUZcX1q4TW2hFhbYz4nNwByLONlG-xJcoZ9kaZdMXH8SsvtObiYh1UYfc32rZ8J27zN99bAPtU07od_NGWq9YJzy20ZqNyyKdPby9C7RuqSRNSI7rz8k6ZEW62w9ZuYvhlZMlxy-0qnhewC8d7BopiLG5A1j0NnH2153_XHZ0YW_EHPv36V7aBZn_JVl202teFUyo0rgCEMsUepFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇺
🇪🇸
خولیان آلوارز در مراسم عکاسی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105803" target="_blank">📅 17:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105802">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=GhA2wKw_cqw5Zy5H2-SaCZ6dhu6TK6Mb4yzfhC1XwgJIRfx2XvOaIM2JP2Skk9A_lYXLcH98q6EY3DoQoSK3hqAC6QitADH7Uz1a9gfLBLS_npkwOc1XfvtMFUe3zGhAtM_xh_fLyGHuDCJgJsVJm6VQSLisiVqfBfhQaamXYH7eofBCLZ3-zgffSufWu_JcUAXtSK3n0AwpoeqNkkZ-kDJM03gkPdPKR3ob_o2Zyd1nfLDTarxAMXPpHVEbMA55snCIoJ7FdQ3W-6g2eq-VYrSrfFW3ClYxVLmIXko24MsIPRMAFyhaOEe10kuovP-yK-4q5wcWMZfRmqG_cEzSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=GhA2wKw_cqw5Zy5H2-SaCZ6dhu6TK6Mb4yzfhC1XwgJIRfx2XvOaIM2JP2Skk9A_lYXLcH98q6EY3DoQoSK3hqAC6QitADH7Uz1a9gfLBLS_npkwOc1XfvtMFUe3zGhAtM_xh_fLyGHuDCJgJsVJm6VQSLisiVqfBfhQaamXYH7eofBCLZ3-zgffSufWu_JcUAXtSK3n0AwpoeqNkkZ-kDJM03gkPdPKR3ob_o2Zyd1nfLDTarxAMXPpHVEbMA55snCIoJ7FdQ3W-6g2eq-VYrSrfFW3ClYxVLmIXko24MsIPRMAFyhaOEe10kuovP-yK-4q5wcWMZfRmqG_cEzSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
پژمان ماندگاری مدیر رسانه ای استقلال: با صالح حردانی در ارتباط هستیم هم من هم باشگاه، ولی باید زمان بگذرد تا اتفاقی که بین باشگاه و حردانی افتاده است حل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105802" target="_blank">📅 17:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105801">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=c0UMbUWEsEyIbi0fw0RJVwmO05A18OzEaZfMbX0Y-SxnVjYOHF-RTshxKQLybp-7ciKiZ1DKBa7JUO9aOkmI0NtMqn38LhHelAtWeAlmb4YLam_nTn7BlBFGqe2nNjffeoRfz-oRXdFKxH7wtyH9oViPwMi1SujPifjX6rJAPonW-Twwm7jy7qCPI3iz1N9DUtZRADSrJtXOQu_8xHaG6txbqhwblVMw34i54STPGjBp-XiUiP940AxTNMT2Y3mD1QZPqdNH7iH3qCc9_zwhPoO46clZEIK9JP3cih83tc7108__tQXB-PBY6FA7Yyw_H6_tS2CSDwxN5KyK0uEdnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=c0UMbUWEsEyIbi0fw0RJVwmO05A18OzEaZfMbX0Y-SxnVjYOHF-RTshxKQLybp-7ciKiZ1DKBa7JUO9aOkmI0NtMqn38LhHelAtWeAlmb4YLam_nTn7BlBFGqe2nNjffeoRfz-oRXdFKxH7wtyH9oViPwMi1SujPifjX6rJAPonW-Twwm7jy7qCPI3iz1N9DUtZRADSrJtXOQu_8xHaG6txbqhwblVMw34i54STPGjBp-XiUiP940AxTNMT2Y3mD1QZPqdNH7iH3qCc9_zwhPoO46clZEIK9JP3cih83tc7108__tQXB-PBY6FA7Yyw_H6_tS2CSDwxN5KyK0uEdnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
پژمان ماندگاری مدیر رسانه ای استقلال: در خصوص ماندن یا بازگشت صالح حردانی جلساتی در حال برگزاری است اجازه دهید خود سهراب بختیاری زاده در این خصوص تصمیم نهایی را بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105801" target="_blank">📅 17:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=aM4VwkdUWQ2g0V3d4DjGTxqMfAEYBkPWBfMYQvtsiThKvZjVYDwr2MaPJ0mI_3GL33cVzrRKR8g-fxRDCCBc0PVeN0BOGJGsbWIXHA6_gUeEB64X6nCeofzbpWJOTzS2zch3rNs52hxc1km42SJgadktZaPxKsAwhJX6csHIgtMR1niaD1F_EndYlAW4KfGamEdSTHVirrB65d-kCa7JZl_ah4Dm2S5R2_ioddSQYYWxZa-4_n_kSmJYMd3YxmXEUhetL-q1ve5fj7vB4OfYlZt1Sj5kMSNOrC46b4BiwW-uQoR00sExWGGTygQRzXLZ6lXCa6Bntg85d-JG1JVQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=aM4VwkdUWQ2g0V3d4DjGTxqMfAEYBkPWBfMYQvtsiThKvZjVYDwr2MaPJ0mI_3GL33cVzrRKR8g-fxRDCCBc0PVeN0BOGJGsbWIXHA6_gUeEB64X6nCeofzbpWJOTzS2zch3rNs52hxc1km42SJgadktZaPxKsAwhJX6csHIgtMR1niaD1F_EndYlAW4KfGamEdSTHVirrB65d-kCa7JZl_ah4Dm2S5R2_ioddSQYYWxZa-4_n_kSmJYMd3YxmXEUhetL-q1ve5fj7vB4OfYlZt1Sj5kMSNOrC46b4BiwW-uQoR00sExWGGTygQRzXLZ6lXCa6Bntg85d-JG1JVQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پژمان ماندگاری مدیر رسانه ای استقلال:
🔺
مصاحبه پخش شده از بهاروند در خصوص قهرمان لیگ تقطیع شده بود/ آخر مصاحبه می گوید که هیئت رئیسه فدراسیون فوتبال می تواند دوباره در خصوص موضوع قهرمانی لیگ بررسی های لازم را به عمل آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105800" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105799">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=KXLPLTPbY_RN2ht-jxq6AUnBvcKJsCtAKet3m2hGXL3UlwX-VhpzdFu-TH3Acm7IjDZ_A-SkHsc1oxKp38lj7x6GyLGeLNYpKGiBEzquZMnIGEIHYfszptnBxJiVutrfzvO4TRpFb5NoHs95-NktVDNTbmsV2EbtNi3z6A0VUl05R1xR5prtYs2UMBI1xzxnKQfAiz_cVlYtMjGu4gO_2bDPNun0iaS1SB4Zg1NxKDdyAWKdQmYBa-PNS04GXXp28oWZyCeLB3SaOjlx21ZRvviMxbx2bSoATcV46xapFxS55T1RuSckWsT9CdtvUYAq5vkI3cKO_PWaKzn7u2EKLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=KXLPLTPbY_RN2ht-jxq6AUnBvcKJsCtAKet3m2hGXL3UlwX-VhpzdFu-TH3Acm7IjDZ_A-SkHsc1oxKp38lj7x6GyLGeLNYpKGiBEzquZMnIGEIHYfszptnBxJiVutrfzvO4TRpFb5NoHs95-NktVDNTbmsV2EbtNi3z6A0VUl05R1xR5prtYs2UMBI1xzxnKQfAiz_cVlYtMjGu4gO_2bDPNun0iaS1SB4Zg1NxKDdyAWKdQmYBa-PNS04GXXp28oWZyCeLB3SaOjlx21ZRvviMxbx2bSoATcV46xapFxS55T1RuSckWsT9CdtvUYAq5vkI3cKO_PWaKzn7u2EKLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس
: ای کاش خداداد عزیزی سُر می‌خورد و آن گل را نمی‌زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105799" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105798">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=ZxYKVEPH0B0QsEHpC5T3_LbQDBQ4T5hvG8OW8s6BXv0Goa_AxNGoZXIX286c7IbPodAejIpujeYL4AOCYP7YwN2u4O64FlSv4VppvosquyH-yiBW0hC2sXxHike_raDr6lkwjhORqA9abG3lEI_fM_OhdgXw-KQUQvVJ27RKBoSHiT5woXGEct4cc3Dg0oAJkJYZ_YbpcT-ZjcrGI7Ozl5Eh5qYjyQh29_aJyuyL3NsS3whEmHbMWkmUTDmdGu1_4d7ED1YGpVtK9nqPVHNSVScHlaUWT_RFMzYG_jPEVXktFDSCXsMf7Tj0jApbnZIZsnWrnpdrFEN_5AlWYleS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=ZxYKVEPH0B0QsEHpC5T3_LbQDBQ4T5hvG8OW8s6BXv0Goa_AxNGoZXIX286c7IbPodAejIpujeYL4AOCYP7YwN2u4O64FlSv4VppvosquyH-yiBW0hC2sXxHike_raDr6lkwjhORqA9abG3lEI_fM_OhdgXw-KQUQvVJ27RKBoSHiT5woXGEct4cc3Dg0oAJkJYZ_YbpcT-ZjcrGI7Ozl5Eh5qYjyQh29_aJyuyL3NsS3whEmHbMWkmUTDmdGu1_4d7ED1YGpVtK9nqPVHNSVScHlaUWT_RFMzYG_jPEVXktFDSCXsMf7Tj0jApbnZIZsnWrnpdrFEN_5AlWYleS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون‌شرح :)))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105798" target="_blank">📅 17:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=RhVyehFahG2DWekHI18H0OVUXhUT48c03aur_jPy_fQYfKeIEbsxmuAMMZVHM1rGfp277cOUCI65gI-FHfaCqR8Yt_S9NEwTyJEOLxFgfUqx3GiP84bnBkPARhSLITMfSvuSHXSDQznZO205MIGDIp54irF4zmybFiia30EZae_PCKaoCxmQd_6ij_ycc4WjS073309dwGdlC3bLGSv6MQFF2HLYwWCbSnfaBFX04n5rd72vIirFgqyBmEtUX32AoYKBZT0KRgWkA3fA9TmZc2afbd2s_SQMGaTW0hMk6UhlHzhy9VtWX-wdTbqHclEUmbRks9J7DWwfzXVnaF033g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=RhVyehFahG2DWekHI18H0OVUXhUT48c03aur_jPy_fQYfKeIEbsxmuAMMZVHM1rGfp277cOUCI65gI-FHfaCqR8Yt_S9NEwTyJEOLxFgfUqx3GiP84bnBkPARhSLITMfSvuSHXSDQznZO205MIGDIp54irF4zmybFiia30EZae_PCKaoCxmQd_6ij_ycc4WjS073309dwGdlC3bLGSv6MQFF2HLYwWCbSnfaBFX04n5rd72vIirFgqyBmEtUX32AoYKBZT0KRgWkA3fA9TmZc2afbd2s_SQMGaTW0hMk6UhlHzhy9VtWX-wdTbqHclEUmbRks9J7DWwfzXVnaF033g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعد از دعوای خداداد عزیزی و عالیشاه آدم ناخودآگاه یاد این صحبت‌های اسطوره علی‌دایی میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105797" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=pbKrsuppIZ6UKNJMG03hgKjivjce2A0_GDX1zfFFy8vwzMZBOYGHaZVkvWTCPU3Arwv18JkbK5KGmIDfEfNKTThxpr2AkxX4ktckMbgkB_LfaS86d9ncN-VRjzBNtWIJyB-GfiPNg9iBFedV9oqJpgKxMaZ_73D9NxiO-i15uNdNytnv8_EMt3s88o1fhXQTcuetlx40Ncwhzs-uqCkh9nvlCnrW93LojdcKuOlVoEnjJTxWyq4th904GLfa6NwoGqdDfdGcxhDP7ttboAYVUVUdT4h-7XSy8AshK3MN291Gs_of6CTcjb3b6herjLrc47JlsVzNLWs9w2HvT8OQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=pbKrsuppIZ6UKNJMG03hgKjivjce2A0_GDX1zfFFy8vwzMZBOYGHaZVkvWTCPU3Arwv18JkbK5KGmIDfEfNKTThxpr2AkxX4ktckMbgkB_LfaS86d9ncN-VRjzBNtWIJyB-GfiPNg9iBFedV9oqJpgKxMaZ_73D9NxiO-i15uNdNytnv8_EMt3s88o1fhXQTcuetlx40Ncwhzs-uqCkh9nvlCnrW93LojdcKuOlVoEnjJTxWyq4th904GLfa6NwoGqdDfdGcxhDP7ttboAYVUVUdT4h-7XSy8AshK3MN291Gs_of6CTcjb3b6herjLrc47JlsVzNLWs9w2HvT8OQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بزرگی و مردانگی یک بزرگ‌مرد، با حرف‌های پوچ و توهین‌آمیز یک آدم بی‌سواد زیر سؤال نمی‌رود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105796" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=BWEPw6-wyHpkMsPMOyrYdVn5WxFcQcplTcwKPHrVtgf8QEm84xtYcDiVI3Pi-93FII1bS8Ab_6F0zKaScFJAF3aYwhnJNQ7tL25C9-Qdv_Yw9nQ6vg1QQMKxG4K0k9M4DWqaUGrZlLPr1wnaUBYYTFZCHz_4_QdmWRJZ6bsvJz9m77UTssUkNf3y2c0mQ4Y6G7HNasDlKoQwaS2regfPMdFOskRu5cWQZi2r_iM_txujk3Pd8MbazJ33fvaGGncznMUZljDGd42Wn-UIkMyxWwV3QpNdIRn04z6zkTo5TKEgm124jZXwM7pCYsK9efAGZIIl8EQqwgNKnrZ0AHI2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=BWEPw6-wyHpkMsPMOyrYdVn5WxFcQcplTcwKPHrVtgf8QEm84xtYcDiVI3Pi-93FII1bS8Ab_6F0zKaScFJAF3aYwhnJNQ7tL25C9-Qdv_Yw9nQ6vg1QQMKxG4K0k9M4DWqaUGrZlLPr1wnaUBYYTFZCHz_4_QdmWRJZ6bsvJz9m77UTssUkNf3y2c0mQ4Y6G7HNasDlKoQwaS2regfPMdFOskRu5cWQZi2r_iM_txujk3Pd8MbazJ33fvaGGncznMUZljDGd42Wn-UIkMyxWwV3QpNdIRn04z6zkTo5TKEgm124jZXwM7pCYsK9efAGZIIl8EQqwgNKnrZ0AHI2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای خداداد عزیزی و امید عالیشاه از این زاویه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105795" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCLpJ1Bo0_gdDRvp_nhJhRZa4ik5zi0FadlLe2JhW-5V0r3_32WukpkFqb-wjlg-oSeimD2tUOFtNDfDs9q9KV9FH6Sxwu1XYI0PiqrAcu5EYWMeoWTlmD9K70RaTaZ5OZCUpmnrnw58KdRymYQOEtW_S5AdZUgKdQO7iWxsagVKRCoF_piCGOC-HP2ceVJlkfn7LNYcybHc90EQ1kfOcF2WAXB2ciWNmsujCXE1g_J3CxuEFP9wgLcGsVWHnWTk-0S8igmOlFAuV7nr3qRFRdA2PPMRgenNWklzPbwVxDrNBcDQsBgq4nqgjGIZp4zkk1I41S23K3wy8twxxdpL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
هوادار جذاب و شیک تیم‌الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105794" target="_blank">📅 15:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72559f2230.mp4?token=RNcI7GqFoEAHd1BpaRQsO3SMoTm4u9Wu7_g4yu9gNoxZz1eKCrP17JIRMF14x1st3vvHcl4hJCAjeKyTA5gI_yP8KejEJA2NM0m4gi_IPb0h_YdKW5Xi2V_gZf4tQPRFu12tiUr9FZY2j0tdNvE5YCyjr46rmr8LXsGrxdVRTN6cM9ZlbK8zzQ2eGUZHN5J-9NUZtuCZbvfxpu_f_-Z6mlcwl1sr_IptZUw_1aM0zlMk-Q5C4eci7Pl_Z5coFUVRSlwpcdtFABq4TWT9u8kgbMHnAHoI5yGQwVVbPkGsBu8_cD5RW_iAUXbaNVFUoKZDmGxi78ItUY8pQJ2wuYvNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72559f2230.mp4?token=RNcI7GqFoEAHd1BpaRQsO3SMoTm4u9Wu7_g4yu9gNoxZz1eKCrP17JIRMF14x1st3vvHcl4hJCAjeKyTA5gI_yP8KejEJA2NM0m4gi_IPb0h_YdKW5Xi2V_gZf4tQPRFu12tiUr9FZY2j0tdNvE5YCyjr46rmr8LXsGrxdVRTN6cM9ZlbK8zzQ2eGUZHN5J-9NUZtuCZbvfxpu_f_-Z6mlcwl1sr_IptZUw_1aM0zlMk-Q5C4eci7Pl_Z5coFUVRSlwpcdtFABq4TWT9u8kgbMHnAHoI5yGQwVVbPkGsBu8_cD5RW_iAUXbaNVFUoKZDmGxi78ItUY8pQJ2wuYvNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
جوری که دیشب هواداران والنسیا هنگام تعویض شدن پدری ستاره بارسلونا تشویقش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105793" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=QGRMNnA0UoZgUrGfecWQOZt6hor3AqMHihi6XDcDD153Bfi_rUwR6SaPEGADid48VNUyQnUXncwWbqY166o0EK_pBfxuMY8cHsm4tAReMgOvvp5sg624pMI95jaQtHLB6uEyf_pV2meWdykYOP5oLt0PD0qLmI6kK3bQrwuVHkcW0noN7xovZ60drAyFvwspxACPPGZ60F72XHdYHUtdj2M3ATsO58yeX9MPTRMaw_oB5AIt1gJb45uXNIZsE8logRCtM6Zw4NB71Us1PCZM1Vk7KwWHuwJXb0oprSG8MNMD8Ot4wQSgGCKa5SEP2WEwnYWFIYdBZCmMd2IrnKIygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=QGRMNnA0UoZgUrGfecWQOZt6hor3AqMHihi6XDcDD153Bfi_rUwR6SaPEGADid48VNUyQnUXncwWbqY166o0EK_pBfxuMY8cHsm4tAReMgOvvp5sg624pMI95jaQtHLB6uEyf_pV2meWdykYOP5oLt0PD0qLmI6kK3bQrwuVHkcW0noN7xovZ60drAyFvwspxACPPGZ60F72XHdYHUtdj2M3ATsO58yeX9MPTRMaw_oB5AIt1gJb45uXNIZsE8logRCtM6Zw4NB71Us1PCZM1Vk7KwWHuwJXb0oprSG8MNMD8Ot4wQSgGCKa5SEP2WEwnYWFIYdBZCmMd2IrnKIygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
وضعیت شاهکار این‌هفته بارساییا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105792" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miGeGHKDoMXRwcODz4Bgco0sruJOrEN-ROuDoL5rsAOA3qwe5UWpwHoyjsshuueXW1KwJqB54tfQwSTdTA5ZXPszaYEH29bxFc32tEt2f-1Uue1Ur68piXgftLjrt5ueloN1etd0kWkDSnx0x9AF_YlHDtlOwvVVBBJW88h9jAA63ZvkTUxujr-wFqA-MxhvTuoxN65uBF-vpNHJp9mStggmzg7LgFXJf4DFSSWc6TZxOOlQMcewDyWMcBspdcKU1MZjB1yTvnEOexzLLiI1yFaVXYQyWYUmE2LoVskJC2Qo32TZmvlKVArmXae8zl3ScDc4jdhOnrinO6Qf6gec7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد بازی‌های لازم برای رسیدن به 300 گل
:
🇦🇷
مسی: 365 بازی، 300 گل
🇳🇴
هالاند: 384 بازی، 300 گل
🇫🇷
امباپه: 398 بازی، 300 گل
🇵🇹
رونالدو: 499 بازی، 300 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105791" target="_blank">📅 14:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105790">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2kKcBFGafJuwc5f5g3g-EkaU0rSbUIrcapts8l8Wn_X0lf0F0xs5gY0_aVkg6W99TOgxdxOZu_WJ6kXpsWEuwWA89eXBDOUU5Z8KfmXC_GXjSVr75c_gJNTFWXrA7wokhoL1y2Wc9o4QOoj0xserwhyITXunvLEISfiaTG7vkTLsGmlUC3vagpem9txdcADaWSf4cwKcWz1ZRn5CfCX2qVYroW88KiKhKog9XdIVYBjyK9jC7T3hBfXqppghXJpaNUtvPs2u75Hk2GKMFOWqq6vkDaQEPvbelYRY32GnmT4nY3ex_HcA1Sx3ssUjs_O_vWU6Qn8_1fC5wP4awP15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇭🇷
🎼
لیست تیم‌ملی کرواسی برای فیفادی با حضور لوکا مودریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105790" target="_blank">📅 14:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105789">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBvS0OWY-E_XxiatnGG5ALJTOzu-LlLo7IvyDxlPilftGurSocYeFnv9wyJN1s4AXUU5UjCSwZF0d5tK1Y95md2uoPnaj4a30697xlU9FWpgExMMasxGt7NhOg1lAW6ujWsxKnfqVrlCfVtIHkl7CwMiAN_e72m4KxOJJewbSF7jd78fslbs3pkiZQxouAxpkjhA5NHplZNLejSbuDbP_GLOmhc0jCkjsJp-p1omHKup5HfC4nP4DZBxPoN1_0Eba6ttAEtiQoy59Cj_lxvXSZ0uw7iSNpyo9cJI2GDGSatcUhLGUdRkv56v9EnoxcX2uDt44rNRWnAMXkPSv8hnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
این تنها سومین بار در دوران حرفه‌ای امباپه است که این بازیکن هم موفق‌به گلزنی نمی‌شود  و هم چهار موقعیت گلزنی بزرگ را در یک بازی از دست می‌دهد.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105789" target="_blank">📅 13:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105788">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2063588.mp4?token=nZsKSVdutbWy4799aUmGiFxDZH34UvkuAo4DXLxFZNMgMZ3Msd2QaQ_Inu6qIJzF10KBSJ1hJeU2GlMtouhm5VA_vke1menq8dl3DjLIbrTrlV3pMMdB1aULTJCWhvD1Ylq_2dQYRiQmVMu2RhborO_gjG-2RH4zZUqT0YqTix-V8LKsjsx1xc62gtZn-UMPWMVqzIwO1-vGGEkg3i6sVlyGMo8vBhcaC0ZTQGhkM5Ou-whWU-RlJAcuTcjOr-sSWpuR-1XBcvWIEWwbC9tLFM6yehe0-oTGBPi1FOvSVHSkRcepCqdEO3fYTTXm8r1g-uEc2M4Epc0ux_bkXTCeNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2063588.mp4?token=nZsKSVdutbWy4799aUmGiFxDZH34UvkuAo4DXLxFZNMgMZ3Msd2QaQ_Inu6qIJzF10KBSJ1hJeU2GlMtouhm5VA_vke1menq8dl3DjLIbrTrlV3pMMdB1aULTJCWhvD1Ylq_2dQYRiQmVMu2RhborO_gjG-2RH4zZUqT0YqTix-V8LKsjsx1xc62gtZn-UMPWMVqzIwO1-vGGEkg3i6sVlyGMo8vBhcaC0ZTQGhkM5Ou-whWU-RlJAcuTcjOr-sSWpuR-1XBcvWIEWwbC9tLFM6yehe0-oTGBPi1FOvSVHSkRcepCqdEO3fYTTXm8r1g-uEc2M4Epc0ux_bkXTCeNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
امین‌رضایی یکی از اساطیر سندروم‌داون در دیدار با علیرضا منصوریان در بغداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105788" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105787">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=C91fCgjwOIDcNQvtVcIgqM7l7JJitdoHHskjV2FHsGNUyu2unzScOSPr07wwdI3PYDdNwFrY4QZ-WB1k0uKp7Si7khaT1GxjKNtWAU-mgBn3A02dM1u5QmW5zLjYkmWjnC3vVKdZW9RLIF1q3slx6CQ39SujeaoHa4dxhixwD3MWNzyMM5LvOrekEKjrogiz41PaEHwk0kGrTv2RFK1MOOIcP84cCF0YM9qnsPTpiVqGqzZEb8tpYx41HRWMdMxJW0iCIpl-dldhXLfvl_Bmq9CEwIIdlBpIjJVRd9nyxZJKCCyClyGrdjuJElH2tPmHLvHMHlSV0hfwEEwHI4xWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=C91fCgjwOIDcNQvtVcIgqM7l7JJitdoHHskjV2FHsGNUyu2unzScOSPr07wwdI3PYDdNwFrY4QZ-WB1k0uKp7Si7khaT1GxjKNtWAU-mgBn3A02dM1u5QmW5zLjYkmWjnC3vVKdZW9RLIF1q3slx6CQ39SujeaoHa4dxhixwD3MWNzyMM5LvOrekEKjrogiz41PaEHwk0kGrTv2RFK1MOOIcP84cCF0YM9qnsPTpiVqGqzZEb8tpYx41HRWMdMxJW0iCIpl-dldhXLfvl_Bmq9CEwIIdlBpIjJVRd9nyxZJKCCyClyGrdjuJElH2tPmHLvHMHlSV0hfwEEwHI4xWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
حمایت جالب هوادار استقلال از امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105787" target="_blank">📅 13:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105786">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=DEnxK1k6I8mVwRlMlHh__7Hc6x_HbeXWG2WMwR7UffDGZkIFjDsnugM4SAbDNRE1VqiUco8g39SxCn_2T93c3fCLx6Jo8RQtO_Y-RENyVkpG5GPeOsw4CYd064VUj6UF1T_SMvvPmILqTCZoZQoFUdNWP17Wqi3XsUMENC3Tra6ePiW1dpS9Ovc4Dz4nyB0UsYK_sfeVMw6VR6QZfqSfGEcLSIb3BGlWFvB-CthJsnjmG2_NbvFbfsHkUXhd98SFtCGIzcl5zcVw57X_E6Ur7AWBYYMCeDUhma1Hd6QWuV5pMBRSI-qqumskuBBz7__BYRfy36EKCwygC8fAx6Pjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=DEnxK1k6I8mVwRlMlHh__7Hc6x_HbeXWG2WMwR7UffDGZkIFjDsnugM4SAbDNRE1VqiUco8g39SxCn_2T93c3fCLx6Jo8RQtO_Y-RENyVkpG5GPeOsw4CYd064VUj6UF1T_SMvvPmILqTCZoZQoFUdNWP17Wqi3XsUMENC3Tra6ePiW1dpS9Ovc4Dz4nyB0UsYK_sfeVMw6VR6QZfqSfGEcLSIb3BGlWFvB-CthJsnjmG2_NbvFbfsHkUXhd98SFtCGIzcl5zcVw57X_E6Ur7AWBYYMCeDUhma1Hd6QWuV5pMBRSI-qqumskuBBz7__BYRfy36EKCwygC8fAx6Pjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی سمی همسر دیوید بکام با ظاهر عجیب محصول کشاورزی شوهرش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105786" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105785">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=v_p3uhT1VJRAVc4nMFEmhft3PeFyPK1qZssCxDYsIycrd7G2tUQN62J-j7PUvcL4glwq7SICB8oaNmJSRIjeZ1k2HY84G52LOsn_yL1NzOI2ovjVn7B8n28lvICKdGLkKJg0mxfcxCndisyy3JGIvujuOylBqAADA_6Gn8RM0Q2K6ZCW60L4fEm-wpicT46Vh-pSvcpLqZ9sQjDhfueDmEuQmb-KWu4SrDI_bNdm39SdgtLWv4FSR3_FpJEeETOJdre0hOCCbN-6VjQOQjZuu2QCqxb_qs7iU9A-jlbOjwCqxSUi9_Z-umeaT1aCP6QakzJdfcyuTn_-VWAc9d0tQkufM54kfdN9jLq5IFTKpZ624bkhwkaIptTdpFrSsyJAujBCbZ_wxbneEwT211W2b3Ukrd-7KXqD5Qt9mqglg_4SVsG87zlp1ztgL_QsQtv8KRDIh_FkSHpz017-A9SriaN27OhjKFx_tCZyRY-wFAgXGnfaz1RR8utT6pzy7XO-BvNpVQpFMkbnI__JBxu_vd_y_n4EjGtQNbiBhXJGQHVhxJW3zfcMPgO-FQeW9y-P2QvFrIob2D8KyB3V0qzq42EKtSQLN_JdlWfge1QfsDod63XEO4NLABUN2PYbXbou7u4Uh3Zyx0KaPQjX8GbkjHMxcUs6iNcYXKwuEeyrLpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=v_p3uhT1VJRAVc4nMFEmhft3PeFyPK1qZssCxDYsIycrd7G2tUQN62J-j7PUvcL4glwq7SICB8oaNmJSRIjeZ1k2HY84G52LOsn_yL1NzOI2ovjVn7B8n28lvICKdGLkKJg0mxfcxCndisyy3JGIvujuOylBqAADA_6Gn8RM0Q2K6ZCW60L4fEm-wpicT46Vh-pSvcpLqZ9sQjDhfueDmEuQmb-KWu4SrDI_bNdm39SdgtLWv4FSR3_FpJEeETOJdre0hOCCbN-6VjQOQjZuu2QCqxb_qs7iU9A-jlbOjwCqxSUi9_Z-umeaT1aCP6QakzJdfcyuTn_-VWAc9d0tQkufM54kfdN9jLq5IFTKpZ624bkhwkaIptTdpFrSsyJAujBCbZ_wxbneEwT211W2b3Ukrd-7KXqD5Qt9mqglg_4SVsG87zlp1ztgL_QsQtv8KRDIh_FkSHpz017-A9SriaN27OhjKFx_tCZyRY-wFAgXGnfaz1RR8utT6pzy7XO-BvNpVQpFMkbnI__JBxu_vd_y_n4EjGtQNbiBhXJGQHVhxJW3zfcMPgO-FQeW9y-P2QvFrIob2D8KyB3V0qzq42EKtSQLN_JdlWfge1QfsDod63XEO4NLABUN2PYbXbou7u4Uh3Zyx0KaPQjX8GbkjHMxcUs6iNcYXKwuEeyrLpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید باقری، بازیکن پیکان: خوشحالم در پرسپولیس شاگرد گل‌محمدی و مطهری نشدم. اینکه بعد از جدایی به همه جا زنگ بزنند و من را خراب کنند، حرکت درستی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105785" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105784">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjRH_sM3D04zKzd_7cqIsde7r155vwUDFQ8ItYAozCW8uibivxhRXk6j3vvXL8jcKuTUYBODPjsnj8STUdrGJFK7y7su0IfxwdIGlRKZP-NeVYgRWP7sjveHicSASha4kOUmyFcbI6jeqtAC9TMVAjfAB-wmsWNzLARtVgS-TSBNCZ-TYj_zFqr14j1bwVfRT27-Vy72_X3NoULlIEyWZTHXFpaonkbF6lqaAksefnGAwQ1i2VDA-KjbOI9kAN7vD1wMIGtkS_F-QleL-zwG6aYmNDWmgFX4pjZQOBx7II3aiBlgtTUpLURvL9UmiAKn9mqbm81FKDMz99yBHbYWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
👩‍💻
💡
یه راهنمای فوق‌العاده کاربردی برای دوستانی که با برنامه‌های آفیس سروکار دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105784" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105783">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=XAoFuyB3WI-_OZiC69u_SQhvs5OTirvge576c8lJVFnQ58U3SlQ69FRSHCfQY9cgCA8hbPThC3LuvfXm-7viLkkSI1mirBXUObawCHiOmS4rZ32rLV5Z4gVYTgAi7S5vdHkWRQgsCINa6qOGVDHEpcq3qVufzcszzaV_nOuuHulzcq4ZqILM4dDvxWXF2-7Do2euh8BE1hVj6JvHxUZ_eiXVypsvo2r4Vwbg86hakZ-jWU1CJQwF4JiCeI1LI_1izrYDhqv2vxguX1OyynG-K0XLY_UqYKoftpCPi6B3xq4bKHuLhJ7jp73kFMJw2Y69BqTlEyvJD33mcuwST1m1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=XAoFuyB3WI-_OZiC69u_SQhvs5OTirvge576c8lJVFnQ58U3SlQ69FRSHCfQY9cgCA8hbPThC3LuvfXm-7viLkkSI1mirBXUObawCHiOmS4rZ32rLV5Z4gVYTgAi7S5vdHkWRQgsCINa6qOGVDHEpcq3qVufzcszzaV_nOuuHulzcq4ZqILM4dDvxWXF2-7Do2euh8BE1hVj6JvHxUZ_eiXVypsvo2r4Vwbg86hakZ-jWU1CJQwF4JiCeI1LI_1izrYDhqv2vxguX1OyynG-K0XLY_UqYKoftpCPi6B3xq4bKHuLhJ7jp73kFMJw2Y69BqTlEyvJD33mcuwST1m1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد آلمانی بعد از شروع فوق‌العاده در لالیگا و ۴ برد متوالی و ۱۷ گل زده: تقرببا بی‌نقص بود، چون هیچی بی‌نقص نیست و همیشه جا برای بهبود هست!
بارسای تقریبا بی‌نقص هانسی فلیک در صدر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105783" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105782">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105782" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105781">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrBeYSiS-wXBbrKsg48xsFC4GpjrS9NubJ8wpbg_gJrqx2MHcGf37QEv6ajEsn6bP9BS4saTjDnnCHNZxZdmjmLcPWfUTnBBFo-D1SrC14ZVBqjQRtDe8u0AtaBLHfIIMxVgD3sapiUJ5l0XHI6v---m2rU0y8goJL79f2wjFZ7p2x4ICt2kjEztB9kVHFA3Vb2ou1TAZiF-rEjBNsEnN6OondHll0dXmibNlqXcxrXRNVpFA1LolfbT6fzSNcGM90yL3RfYP-f0AnG0ZwedfYDPmh_8Xwuf98BbYfKcFpeslUjva1Nvk56IFSkC2KidbUJVzb-o5vD8CuRBOZv4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105781" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105780">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=AYuDZMnWOexL3o--gumBD0cZUbOMgrwlBCEB09PwkKr5igCk84c6i_NfTbKJfFAX6hxU-u3vYeAJ7KZnOu_3x2L0_knjMkmmzmkjsTdyzBMHEEu4WwPZTj0D6GagM5LDMdpXVUiMPCRFvU_WNU0tUN2Yq_p7su0vCDyDxFgABAc3lwUdOYqRPjW7TvDUBQHmqxG18fNz1FTP077r-x2IGFlyAQbJYoZlpwYOx0iKWh5iUzjZXogVo1n9PV45_ZqQL43dWryBB7FAzOzklqmrfcobDtZh5ijdVdKlHHh2PVH9supblxzdHP-Q-nOZF_2z9_mlbVF_HUHyIFyd3-Ocvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=AYuDZMnWOexL3o--gumBD0cZUbOMgrwlBCEB09PwkKr5igCk84c6i_NfTbKJfFAX6hxU-u3vYeAJ7KZnOu_3x2L0_knjMkmmzmkjsTdyzBMHEEu4WwPZTj0D6GagM5LDMdpXVUiMPCRFvU_WNU0tUN2Yq_p7su0vCDyDxFgABAc3lwUdOYqRPjW7TvDUBQHmqxG18fNz1FTP077r-x2IGFlyAQbJYoZlpwYOx0iKWh5iUzjZXogVo1n9PV45_ZqQL43dWryBB7FAzOzklqmrfcobDtZh5ijdVdKlHHh2PVH9supblxzdHP-Q-nOZF_2z9_mlbVF_HUHyIFyd3-Ocvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لندن مطابق سالیان اخیر قرمزه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105780" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105779">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VCyHblb517oxQv31s3BAIrC0eDNhfh02lm173COXsWkRXHf4imMLjCYPfm_5b7AE53yDR6uGFVCVEpfFWoqozR1gp66EZMGN8-O9BMQA1HOq-7PP8R_y_atrae1uVPEcT8B1nO47qDpPhSQbiHXggir1_rpHdMWLGc3IoaX2jVzvT7v-yOwBQVUaY1SPnF4c7u-WQtjeDuIJwUH3VGzO4x0VeWLfPeo05ta8KxJ3tG8WHPQlwzHH6N1Kxfw5Lt83Ka85NZWLStty_5JLBVcXpV4gBYtNyg85mLOKxCMuJb8JfsQ30lZ_yRMXlGfoMmCYjCF1zmemgrvYficdGqYXlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VCyHblb517oxQv31s3BAIrC0eDNhfh02lm173COXsWkRXHf4imMLjCYPfm_5b7AE53yDR6uGFVCVEpfFWoqozR1gp66EZMGN8-O9BMQA1HOq-7PP8R_y_atrae1uVPEcT8B1nO47qDpPhSQbiHXggir1_rpHdMWLGc3IoaX2jVzvT7v-yOwBQVUaY1SPnF4c7u-WQtjeDuIJwUH3VGzO4x0VeWLfPeo05ta8KxJ3tG8WHPQlwzHH6N1Kxfw5Lt83Ka85NZWLStty_5JLBVcXpV4gBYtNyg85mLOKxCMuJb8JfsQ30lZ_yRMXlGfoMmCYjCF1zmemgrvYficdGqYXlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
⚡️
ویدیو بسیار‌کاربردی از بات‌های جذاب تلگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105779" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
