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
<img src="https://cdn4.telesco.pe/file/kUdLRRA6BX2O9K-cNlg-dmJk73Nl2ngt6TrYLOVa1ZYGwsfIuTnYY4-08r-rjFm4vv_qCNB_Zr3GUTJ5vKaQEfGIoOm4ngpHij53D696xEN6fJNNM4C4fed4ht_3W25XMHvJvh0fU11tPgAtp2daich10HVH6zbLmOBqfCZGJkKS9UyOB97Tj5tu_YhMqsWUxDE6cA6-a8LPOqeBsPLRyxDifeZf7jab8fDYiOS-g4QKK5UXxqoa-pRt4-kme8glM3tNV3ocS_ni8goYh-kuPHeH7_kXceZ8RJsOScnuHJ5Z4px41GtgBJWVfBt7SMGZ77ElykMVyyVzf8-g9vk3uA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 12:02:23</div>
<hr>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNS8Gsot92uRlwDDEmaaC-aBITySaIgoI18JowbZIIns49XomhBye2iYoxdRmfJOkWw871twQHWJ--s9QS_BkxKNi9jeTa3Ys8vmaF1IrPehlF0AZUSF_EFMED38W3WU4qx60dJsKicCZzdFSSOe79pb-UeZzZgKGH9Ve4dlb_FrbVqiQoJJK5pdwn-V7JgGZI52lN4RUesp_pVKCvq74tmifDzg2T5FInT982nJjr5nEWEKcnTeYIR_P_P5ZmleUbEHBCRGScg3uSMA_O5AFEadYfcPEJcYkMFmPuRFOYy6Y3i6VRx6eitZLLooMYEj1LuHWTF7nYWMSkGQgIoVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhfACF52uauy_6kl2UAp3gbPVGqz3xiPKLnEwpV5wFf9gR9Zk9LMlRk64j4Y0GxLiaYp7KwCSdzxG8KplPeSi4ZSexAcXLDopBC9ZpQcTsIyDqdNffYlGsXIg9xbvnAWntWxvyKPgLmZAbS_yf4p8Rf2Lv9-RY64bXCiRUJ4phA_CjZrv_aftejYkMUFIbkUHgU62GJccrYKF3JinNIc7ABYfsFlAuu6wlaxpJRcfVU0HKjz6J79rysqQSKJ9SQBkQ3o3zabcUq14r5yQV8S8C1fMmby6gk2cZ5mgmw_7wiHEtJZoNfYLBMlsmZkPzAHo_LJle6jg5bPa8e8S0p3KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fperqOWlMGj9CiCNFqCHpAKcOi3D0xt5RuXnuO_lzyZ0o9lbQhLVg2l5mUwkA2JMUrigDBZ_9R0o7BUWQt2-p9lAL2yvWVCpdvlWLw1TGWGlFabpkfIvK6U_SVNgU_HExuTcLDQY8PpOvV-RuT8zV792GtgvJb06AdUlcZKY2HQZVz9-uXNFfr7XoWwSuvKzPf3u2ZYd8XOoFsfoRZtZ7xMPAM8_mpt0SiALV5fMtVX4rczQ1Uqx-6ILSvAK6Iv_Gph7jMYQL9ooQzKzpQ_kh7ZZ-j-GPH5moErI0EZM8r93T-lO3lmvI8QERQkIBHQIO36Yt1044pS3BiXADbakmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5WHSpRJgOYXflWfq1Td7gJsuCiuuqSBXWq3myQn2kY-h-eNDvJYmrAGdSofx77Gx6aJQjanOS6mPZHX7yF_ekig8bGVejf-0Zq0qIWORnejBPBnoQ8847AFsOH4VZ09DysXIlsm5UDz6aAhed4Wc8TUCeK7rHViKf45ffSJ1NBPaDNlrq6fG-tkJE-CRc6jtPTgbhZVzTFrt30HXwha-ioBh0ZfYQlURY5T6tyx0qWWr3Ihue47Nt-TS-tjiogeZ_64yFkEOaU0bmuyuIoY4tp6_LNgJ1dM4lU0WzZ9gR5INFd58TUK_CoXs-n0glWW4V2k9RmUYtECd_zKz5P1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZk7xLJ7ZacDq6DUwkyoq36-tH3tyKZ39uuXv-MKPSGYThpLyYmobCXTiQCxIbaPeQueohJSi8m8iKutSN_6pLNbVTIMnZNVjuqCKciiE78iNrMpdsZre8gCsM4tM7idJii9zSN6wrnzK83fbD-NKQhimUcOl6otOij3mVy-6Yt0Izn-ZSgLa3EfNn54Ll5ywsWyAP5wIK3n7HQw2NDy-Sy82yv-PK6NrfjsQ_bGeI82CHdjdEmnTmoHzsLNZT62SC5OJzHB1iloctuCjvxlhPMrGuKJaNuw4uaCMOAzoStNw_pvk1ArQr7idh0KtBKF-T5irB_QCxIfqIG3LHsggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=Gvd75Ho5YZDS0Wa2w4Hfr9lT58PwZSFN6F5F73V-IPsTzv36RyoxR8ic_jZDmjGB_63pfSdnIg-oEleeKnF0jieWXqWIMiYW6DyEkhppXY2A5E8rmUCbuWgAckCtIcMB7vt15GDLN9l5J670T3FpR0dtiRSL1fuZ0evK2mPcWSsqOopimEOh60aYHAzWOedKStsPLmDcvFo8L6PquEhVM_lmBOp_4TE-TM9aRsZO2fuUyyj8uEWTtjp1UMNK3pnh5QlZ1Lp4zNOZlf3NRQcFNxrXHj6KqD5CDOiYKl1vkWY9E5FUU4K4LNh1iab2AVLDUjj-Dl83v0DhCYcV3BDooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=Gvd75Ho5YZDS0Wa2w4Hfr9lT58PwZSFN6F5F73V-IPsTzv36RyoxR8ic_jZDmjGB_63pfSdnIg-oEleeKnF0jieWXqWIMiYW6DyEkhppXY2A5E8rmUCbuWgAckCtIcMB7vt15GDLN9l5J670T3FpR0dtiRSL1fuZ0evK2mPcWSsqOopimEOh60aYHAzWOedKStsPLmDcvFo8L6PquEhVM_lmBOp_4TE-TM9aRsZO2fuUyyj8uEWTtjp1UMNK3pnh5QlZ1Lp4zNOZlf3NRQcFNxrXHj6KqD5CDOiYKl1vkWY9E5FUU4K4LNh1iab2AVLDUjj-Dl83v0DhCYcV3BDooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxqHojIre8Y-wuWvxpxHFpz3N00etSKqb_4M7qY9kj2kY_hcfjoIJVALosA1nKo9jKqUMJ2T19GGKZtpXgXNFgiyeBEGI-ClMomgXInMjtg1up1xUPgO3R6O1Bn1EvwQjbH03nPY5vt3FpryT93jT1JnRAj2DN_EsFmadJbrlFpl9K4kMHJ5luOLdRUbXARHBtFoHks-3Esyo6f0DyOKq0Rqpj3JK-3gKLvysAy1_vC-1d3T14C1SyTPimKQkIqgAcUyRRXQEnF17VygVAKKK-neolBSwSXsS44qRz-MfeVX_Wwp5eQG-AkrIxaIU5d3CtKXvpSGsnymAd9d_mgiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CThM0CosDaJ9mwiUCYwwhShyp9txusioEPbsmRLWF3VJJshppD_Gd7qhtqwrz1bN5KennqwcVyqp3p5hSwYf8lwNsRBjsCVpR9xXkh39D93BN1UWTrtj3xXvCdTofxjKVNIJJ-U8ukDjBOp_LdJtTMYGCyDU9enQ7qZdDUYgBTx_aW7E6fd1fiaY2-zE-XY9AJhKIk8KxuYUyxXKZcpH6AmeOYPiSVDiHVrx56FPe6LM4HsR2Xny9RQXzKEYdZWgbWhcYaWnqwh5EvCqqs7P6ubOQrsseED5auRl_YXiCERdbZkCCTscn72kRVot3XY8TENcA3K8d9DlLNGQoDpoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI6gFDpX1aYBBCpqh1WA5cDbdEE5AbPM1-vTy7MLAlHLiz-kaUfJ86CgffsRTr6xO5FaMTdZD8pYzuig3UVpR6q3QWVDmzFReNxkIdXerqsGYsmrrp_PvxgWUyjKQTWy7vnmHlQYfhZfhPB1weSCZGT12goieBATBBPCDL8SS8TIUCBYEpl0Q2XIgVrQ6dm06ida9tmh4PsA8HJpdDwswkN8KBCeiErRkEOU0ejGPLoYVXvbYNa7NIGJY2zFnKFekmM1vNHOTLMS8NWoIEbWng314RHtiP7TOV6hQR6VR55a8pct23IxLwI2-FQmLUF5YfTGH4PMWjhOOJ9OBRcW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFgL3fTv_LyCjUrMK5SPlVZn0wN7ev6tz_1LSrCG-PtyVXTbhAVm4b3ABhbn9_EV0kgxKgr09p_T5fbafczY8Aujqh8SJRjD7EG63BrA0UT6Gbqt8_ObePxm1bNSdB0uezms9ulDLylKHcAHFLMrCrLVQ0MqfBoM2p7M6DhIludl2ZLca7RDj3z_dN2oEDWYJzZalf6AFyLDMSb3DzKBPv4VRDFnoONR9CrnNyIfvfYo3ZChVP1EC-D44kl44_hPLBBIGVPO8SK1tgPZxiVqtUknkd3WUZBSZvdaEjG8KoFABX9Sf9d88KlAvKUhJ9UyOp-J6JmgBjJzlD67NOgUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZgviVzSrxQVS3BoLagE25UE8SXUFCfq3Xq_Rd9ZRcnDjRq9nfkRyCOMJy3KCqRiHW0fiJ9rvpRhBWn-9Bs9_5oXGK2A7nMzY7zMnv-1mDgQqyH66PUi23IHJM2hOZGIjo6XVXk_B6SYF4iEMLEfD4uxBR27pDbeYRC-cEPzddz2oBAHjygEqEsqrR_PPuZoEKSU85lt0K_2h72-Dkn8K2Z88ZNN_2yhytaCr7AnxYoC-Ent2in_RoPdhB9193NtwWIWz8c4a8SZTCbMA_Ikx6357EPcp75J-0GK2yUmgWuLt4V-Id2htjHmOvm6SsXQVOsGa6RAcOaOUShIuYgLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHGalfjYFCGDaacrLCNGRz9Heg4erIed0-4ahOBA66NKwlyZm8axMI3NdivP-DarsL-OpAZ634-t4uiKSItwDpXdUYwfUjmM9rm_zc0e3Mufq-ySANoOJEOPhNrXX5PXq5DzVxvwCHi9nL7FYH7jADjCfZ6OxYzZbZEmWIs7Vc9J4z42AD-3Lmen_d2ve4FzMuwdGouf3SbeO25Dccc0h1jkTDlglgx1dbDbbrMgrKL8K1JHzLM__dekHJPrEvV6_X9LQbUZ7e2X2oArUvY2A7Hy8BN2Wdh77b8kvG32Y6krJPoEPONpnKWX32ICBrgkWrmXV29aUAXYB5sMp6NPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwvALGhZzTkJ92jevSSrV__ubptniQY15ZqwtF6CGlOnNIUS4grACjKMcjdN3JtOWM5ql9zUvgaWof2mDodmJ4tvJHX6YK3vqBH3xel-SZl29igLqmfvxn-EKrJtq_v43I2z-kHpgTlBEmzYH59OMscPNcMVSIIFnbc-1GcdJQmcY96KzEik-WwOUMAkKM8Dlenwv8PKizSz7epWfCSIZxZNyrJ0uCb-vBlSYpaf5A9ks-PLH_kvAyTn4IlCUK7TUm8VLUKVxxXlp-qe0nKUq55au-vyIRAn2nt__7kV1t67Z4Sbse8IpdEyL2-yA0qDgTmfGsWavfHY3dEyITZhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhTEREfjYHTfTxhaIB9Xnrdi-BRyZDVyX605H12km3DWAFn3oFRWYcsFPNQ7f1N6OyySLMxVyMY0T9nxy02C9c0PoIW7jjfcg6g4DpZaDtQrhWbTZQW5kgkBG77pvH4HqtcT85yHxFFqHhq964gPbbS00VUePMsNhegMT2WE1b77vuTntSVdYG_xB654-3K3AdLGNOLRObj9_PYg0aqA3ZepVJDOnRd-zr_9QhX-Fwv2mWJIgd1Ma09A0DXs5TgWUjPOns4skuxIfF4X_pkc7VT4uwWAqQYMbe0OrTuI5EyDHQTgAAMmjeUkSVrWEaOBIFH57cAPAw1gOn0t2HbqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJebvRgehbxDftk9_4PtHWri_T2by8x978d7N8J85Wrq5cDzqBdxMXmHd8eMaJsoEwydlWjjwpErsIHoR9KWNRvC0H3FlM6Z7fDJ-nwVgc4sbyCpQ_UyVNrqJSiAJwOrsW6ZEOlhQswUQgSGBJbCQcNim4HlLkfE6gVBQD_7ObkDhBPc5SjuUpJeXMTT3r8q4_6aVTei15sOXowvgzI0u96gQFDLxVMb6QkAVHWpduaCCaDD9lWpPBa1n3VdT5Sxmxb3b965_IDBK5k3_4_edod02q_2gPm8KsrGuDMdvfaFakTo5DOB2tsWQqzagS5YgCag4uaA3sp5tOm_cHcVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODTHWDL3Dp8LifRoVbDBhtMkAJywutRBERD4ynYeQneIA_t7KJdPi67M-fhg798MK2h365yfgfyOynOJeril6HiKHsrLCEg4Dt8DVPTHakuCIChQXm4FCNDH23gPUoLkjO6u0Avlw5Q2C92XzAcpR-1TA-7Nmib0ECzHI3mj1IEAybyi13OvXDZ_FF6iWDOjrxqwrCo3u-CqF2rksTtI0sEBCYNckXTlyDaqnraCHBg1zhfmTm7iRWCyRJSN_debF1EeyMwczEHDauGO6O5uTj8nv6rEZygu1sGBJByk1R20ReGHON5DOjf1IhBM-o4HyG5MPPevkxri3y5eSc3xIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJ5cd-fZtFG6Ka2oJwrqAWbit2FLKgm0tugsVjlIOL-JyRdgytvBB7MwECSBXXsyE9GOa9bOH3k0AFKmMPp7py1lJsUF-JRa5OuisqKkPSHXAyAvOm5hNhPFM4BLiG5gX0XbDIrIzJDPmuLSF-7byB6aw6gg0IabdgsJz1BDk5oTVwLMyo4srX67FOMCsbGBuvoywdUHVaRMmMKOAa3W2OTntceVgUIGofASgY94krjB1YfIOz0CurpVUxZs5_jiB1xY_yVgSbZsdKDHHRBMct_hIYpdbH8GdBKxi7YQT1An3o1SYca5qmhn1VhR40gEi0Gj7fZBgdIti281gn2zFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benlTJIG7UdAqF_ygVktlP48oU3UNkkjxlduyLfcInah7-OIm9woWrEL3SzctcOLuuymUQOJN0ja44nJSOhnbP73OXCF5b4iTQp9TaOmLUoQx3EusZdzldEAAXjofvCp4uNaN6cn0Rtv7IpUh2d2bD341Kz89zF2GPbbILOEQqveryafzFgOaharwfRfRUFuwmaQaQKG95vT51OEJqag2JO0CuMHDAvsbzsJygrbQ0eTvQrvNYUfNyJwl-vepXrpCP_-wl-pUuB9wvh-gNOgW6UAmysEqmqmLEKajqmB8ZeveNGGhds9BQoWWXSMQa4fTR83ffhMsFixsK7rZslGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=o_o10JLpEg72SUghf2WLw7Rr9OHCTSLXksQVWGj9NzOgt2bL3YBysho7Bw5TgXZRdKxekpg2ODuSQ9AabFz-68LsjvTcrSy3KgH90Wz942tn5OUo8cBZe2mcl9BawN9nJxQgEnjYWSwBoZPR4foHyt9Z2Epn-UGKOIoSbh9Ab5z1wFbTK18jKyVBlJ8wdWJsg1v10bgtyTEeuivdPNBDSHwv588l6YYMQbMFjOzFLHdN6xq6ZBNyIaOvtwRdR6YqJRnvfWZdH4qFcs5Oe9HseYx6SYkp4YQcQvjJ-hdxDCpcShOruM-YFjytDdL_-IYmxPCVYUzNI1vvPvYJZQxInw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=o_o10JLpEg72SUghf2WLw7Rr9OHCTSLXksQVWGj9NzOgt2bL3YBysho7Bw5TgXZRdKxekpg2ODuSQ9AabFz-68LsjvTcrSy3KgH90Wz942tn5OUo8cBZe2mcl9BawN9nJxQgEnjYWSwBoZPR4foHyt9Z2Epn-UGKOIoSbh9Ab5z1wFbTK18jKyVBlJ8wdWJsg1v10bgtyTEeuivdPNBDSHwv588l6YYMQbMFjOzFLHdN6xq6ZBNyIaOvtwRdR6YqJRnvfWZdH4qFcs5Oe9HseYx6SYkp4YQcQvjJ-hdxDCpcShOruM-YFjytDdL_-IYmxPCVYUzNI1vvPvYJZQxInw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9fjsb4RTbkqEQFjvPaDKOi6yRj8YGSr4IVu8WaZSNfDipEtOh7FJmXsrpmsfOGMzBv_t2UtShKhJoywRerF3L-y7O0i-w67xDNhUS6mrharYpsFibf0z9QwAW9dIXHAShQDee0KYUL2bx8jQiUQG52DkYeU59sqqRUAy7icownlNIUVvNHOe4sEIiCPv-mTkt4-od79VGg8TNZCrghHu3IUf5VBsk626Uuhyxlr7qMKsxqEVGL3IeMA67uwazB0EaNaARHQYnWcmw-BsyN6z4ikbsFlAkL4Ek9ZMtSOVAg3SSN4QSwHdUNFwRSBzfcIs5FkiJh4YrD7E7J_1yVj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUE0M_MB0LoYgkdE3CvBjRmyZLWnF0Mt3G_MPkej9CbgZZiMH4ak-PWMeEtBSo2ET51-4C4qM6wv7I2ghA0wGEdkIJL9VCOXVUv4Z5Cl4EMMsozAWN5ka0igSfxPvNfTle_3Te-90mOMyvORhSePcDoIAe1xjL9xNCFL7JYER7CUZY2fW6GYWRO-wUFSaO5SifV3amqoWHR11Ulumau2kcofZ3RBxuh-6ZkhR4cxZB9Rp0fmEG-HoDRD8hNx-kAHLpz8u5rgx1UgDCb_wLpwlkUhJFhxz3_inZ-1QD8_8bZb68StgZsx3trcc7v7qKGRBIX43QqfwyCP-JUuZHno3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiHEyKosmRWH4SsbptkpzQpHXsBQUjG--JU3M2cpGF-cWtNc6by18wmwYctQ3gbt8J0HALLetBQgCHe8BBSR50XXjJh6Ft-wVB2qKLrQ23o23xqViuI0u-8f2TN_5fCoyeN7HqmbEgKp6PGsG4FnPkeWu33V_XLb0t1KTYoMOr9bJtnADXxQYeF8YAoKAvNfCh4W7u-PwdiY8oTZC6yHpfafJtAMVH5pfYvOR6QWwiZ0lG3A60W_QBG8cIxemDURlUIPaLaa75YwArVbYZdJfSI8vgK_1dWqtRCuJkBGjGwpR1aJ5xwCQ3PoaMenykeaer1Du6ZtW-kNS4AYH3VEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=UVVOiHZOuLuek3evnFgJ1qT30M5hL72kAO-ivhu-gipJGYngZW9WLYEXRl-tKQbjq5t3ctd_Zz_Ucj5OVX4vTlBHA13DKdyFog10bB3BEbZTxQbdRhj1dmEbSKycIez4rXiIucCLCLapw2V76iTzLVQ3fBKNKSlKASbgDCP-wF7J216ETsKw6n0WGVM7imql33sJ4ApU-Q0s5ulcwh3LqxvJdW2vkLw-21da-V4Nn3L6bLCmIi84Js-lSj7QOz1ltNWuU-jfBRhL_x_4JpCZwaFuP5C3HiU9gqkhojo5zpRCYF3egoYAtqhWqtrDU8Zbn4-00Kjbw-Hh23omraI0pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=UVVOiHZOuLuek3evnFgJ1qT30M5hL72kAO-ivhu-gipJGYngZW9WLYEXRl-tKQbjq5t3ctd_Zz_Ucj5OVX4vTlBHA13DKdyFog10bB3BEbZTxQbdRhj1dmEbSKycIez4rXiIucCLCLapw2V76iTzLVQ3fBKNKSlKASbgDCP-wF7J216ETsKw6n0WGVM7imql33sJ4ApU-Q0s5ulcwh3LqxvJdW2vkLw-21da-V4Nn3L6bLCmIi84Js-lSj7QOz1ltNWuU-jfBRhL_x_4JpCZwaFuP5C3HiU9gqkhojo5zpRCYF3egoYAtqhWqtrDU8Zbn4-00Kjbw-Hh23omraI0pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdi8XKBP5vpUvOh-lhKd0JFLKVh1r_U1WGk8gjsqMngT5_c6UP14aFa7egs5HVEBEFYsPKu9Ioa02Z-Iio2u3ZhFZl1XfU8KZHFfDexJf53SUxbq6qVyh9tMlcMI_LI-G2FjbWpMQapeHbSGwsmb96zyAXHW-YhzLHLOz4jSKO9Odv1yQB-UDwozvcawBHUZol3s6bldKsc7HWoLsgUk8IeVA_1PrNIQET_Rx7M96QY50590IcoSHJu4EgLhtml4AS6FaoXnnV4IRi7gdtDkZdmRnzUMa9TsMP6hYyMuhHyAlXnHF-0lj0cRAAtrUMbvKlwDVK30izI8UcrE5Ljk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9HAM8uNYiEYBUxq1V3bFh_kKA88EgZ5DQn8ywWbzcR2xOno7WemDyftxNRV-ZQVPW2hUA5AV1K3lp0Py0yuWlt6l1cjzODcHQDo-9vygW_mJCgy24NhFcKqDvLUdgvfs5w8FTAkpfmOdTdarWQsAW1WjZM5aDsKt0Weh5Uz5tDeKDsxpK8jG1_fRBFOhu4IjJMvqCjQ7sVEGBLVx1voEr1D8O4R8CbNsHnIkYjpzPVDfXfX0X3xDjzGf_Bt017xzZmGD_PmaEG-vT_zlPFprNfIi3fg9uuxOBgMjpqD3EGQv1BMWiPs-CR17P7KZttQPBAiqLKStfkURXtO-jD97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dojdpAWeGgsOMtTc49wdlkbYMHUy_Hx8FeoDSYN1WT9ELOYknc-7ZkcRP5hD3CPbSUvlj7zxpt_Ax1liZsn04qlwWn0b50WirAo0nOY0rhPr6_Wge3SHlvAGdlZjYGLOhsXvzzWx8AJ6L4rNLPJ_lf1VUbWoPg8Fz2rZeQziAe1IUG5RypRF-a89ruA7-dFmrjQXxK2RwJ0ROgu9p5IdxCwywIxOSrZbeNw5ZBCa9M2uwUipoAcEgElsk1TQV0lMU7txlJcNAntcf4Rolx1yOQQS2i0wUwfFcSsm3enfsqbZ3lW0Uscr1t9dvZ1-KVr1ya2yu8G9pPhs1YVRgUb9QxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dojdpAWeGgsOMtTc49wdlkbYMHUy_Hx8FeoDSYN1WT9ELOYknc-7ZkcRP5hD3CPbSUvlj7zxpt_Ax1liZsn04qlwWn0b50WirAo0nOY0rhPr6_Wge3SHlvAGdlZjYGLOhsXvzzWx8AJ6L4rNLPJ_lf1VUbWoPg8Fz2rZeQziAe1IUG5RypRF-a89ruA7-dFmrjQXxK2RwJ0ROgu9p5IdxCwywIxOSrZbeNw5ZBCa9M2uwUipoAcEgElsk1TQV0lMU7txlJcNAntcf4Rolx1yOQQS2i0wUwfFcSsm3enfsqbZ3lW0Uscr1t9dvZ1-KVr1ya2yu8G9pPhs1YVRgUb9QxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic7QItOoW92afJz5Bq4AWE_UTT1ccFr88AvZNSa-fzXUMBOwDCiNsHTMiMs641OvEn0X2QiHdwjxZ_IB2hPSnnW-j5E8BOGqRRFkldlFu0nqq_NSKUwROPM_lsHDqkhNW96lW6tscI9j5KMepVzMpyCbOfsLTJcuuYWzUaEvp4VQnc9EKIbnWdEyrnpI_JSOMtprYPRuKfBySsd9XCBmYbCfbaEdysWoPdyc5_lPwpFvA2oR13iQ1UCQvLmr3O5Ay4gMtFVVe6t0cA0HULbs5G1IuXSrOO1M8-9karvG-_aE5k7pzZaEXIy3wgDp_Q1hKQkTbLm5vNbT-t5eYI4n5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=fIop_gzlHOo2yFukFJRsErRD2u7Z853RnRp_InpQDQKyfadS50N7n6ayn3Omjovg-ODmS_Flyyc6ZjzT0gr1-D6djYIfDHULyGRTsfr0o1HVMNKx6SZwA0SrBDuF0s5DhJ-I08v6ie2t4IGBmzOyhQCOlvtGIHnfcUiJlgfm-O46_MR8SJVfgR_sKf2aIFEg9kiOT9RzORofBq9UyC8H4y13QDHfvQQ68YMa46RDFM8Bv3AO0dvKIu4HKvxiETERyNuPXMARHQ4XLU5SqMg_7PdUJXfaGGiRseuW-1aFZkCBTrfZwcHVJevoGAPCDY0WRvnwODvBTlzhb0bRjChotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=fIop_gzlHOo2yFukFJRsErRD2u7Z853RnRp_InpQDQKyfadS50N7n6ayn3Omjovg-ODmS_Flyyc6ZjzT0gr1-D6djYIfDHULyGRTsfr0o1HVMNKx6SZwA0SrBDuF0s5DhJ-I08v6ie2t4IGBmzOyhQCOlvtGIHnfcUiJlgfm-O46_MR8SJVfgR_sKf2aIFEg9kiOT9RzORofBq9UyC8H4y13QDHfvQQ68YMa46RDFM8Bv3AO0dvKIu4HKvxiETERyNuPXMARHQ4XLU5SqMg_7PdUJXfaGGiRseuW-1aFZkCBTrfZwcHVJevoGAPCDY0WRvnwODvBTlzhb0bRjChotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGxRyubXpcdpRXUGWf-qkGHeOMJfiyOfB2ZZo_m_TqD3xH3_ZUpQmVBgSlPzCv5Y5-zkfX9sLyr2ZB-SyJnKIhQo44PbsEDsAwpmpBVKC_Km4-x49nGJxYyn_XBrxA52-78aEzw8ny0XqCJRGeb2j9KCqAmEKKmNRNn-bOcfZIywtUGlyjWNKMBBBUDVtqPVdq5KlnTp9ur4IUkFQQT5aej7QR4cfI58oaRgIDeuWF-zYeVf_hG2DE5VfrMRwTVCl_gszqp4VpLOcVkoxmLzr7L4Rzs-HyFbnXT8NnkE5uJGdZ_UMwQQwyXbAlPDDo2XiKvLmG1HoiS7QCxY3O_kAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH1M7cYDcEee61CCnlO4df95W5keM01ihYPmle7qZzAu3gdZbgVx2bIViQLnvVIGF4lbQzaSB7YmqVDHGT_f4Z_vSoi6ZUQoJaRwFlVhUdRl3j2FAhTEIMH2kSOw9mexyTrXalbMVU0LnYRW2GMWo8WliQF_KSBf8hLPtssR1Ac5iaF43bC1WItqzSu1TV4N5qzAGTCb_MwlDat9hfSyZwNwEABHL8NE1w4v86kzlQgOQ-t9YOw2Wmz-KJ_ajjey0lb44P77vY6s6BlCFvjJINGQkEsD48KT9CGKJP_6iSVBZnR2EAWZF7bYKgb3z_S91QyZHsRiqy8TY_4HavrkRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRuz2OPkK5UaW_PmFV6oZvtsJUzyt7zO55O_lGEHyR1T2p5f29rrea8RHCNmWgjurt40PPR5Yz4esXDHh6EiTknFQMuIM_iDpj_eSnzcNB9dtb8gSQX3gwOuo_kR96esGqULNzmhZIABXVQQlDNDB_TxLrs4BP9me2Mp3WRHkU6TZW784kHEKl3oKBckwvzf32BCkhr9vMr6ylL-3NHsI5K0LycHTUqcQ9M_BjQ0ZxifTEkDxsrsNHKKCA7sefHaEjjxBuVqBuP-_duZqYBzoOa3R-rO7H7axGyBI011qQh9NjbedycgfCoG3L2Uohbwj3ex44QgT1krB356Zih9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUBn_ff7I0S1npfnrx6ZptXqmHrfbEsZrPDejBBTJuzx-OEgQkbokOAyyGiGYuxPfJ0rrHFg62HgWyBQNmQqZUryYaq2xNEUd4Q5XCLvXjQdvcqMkb03R5EZeew-Ee-umF-WirP8VSAXGhcfFPbT4ti6MtxOPNac67XCURZHbb_tQIwUtdLjw92fNbYC9YJvR02fLYElmbUwS41BlV9h6BfjzoPvGcVYgtdbDVbp_UKip_f4DVXfOD4ZrRb8nvZGA9Tjsdspjg7NJO1vIaYmnfmBRyP59BOR2Is2UCiqYlc5i_VBQvXfc1b5rbhixLky1mcPLV0KIhjp_F1a3p3YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=mmcChpn6oNCa3Dr2xBCMLs-lXRg4FVeahqNLTIdzVPQr0NFWUmXBJtkcT8YRVVcMLGXsBtU8EobV_8JrMNvap3CFIwMzwnUajqJCE3R2TZJQ0_9CPRM_4ZWbmC2cM_5zw8Dpm2loBS-MC6TOaNLnkuxKaR9Zv8QcZvbBnjIK5HAjUEH_kf0bs8tgyzB-K-Etap9HxetC6epAweueLo80VPfMDEsaOCweyjmadH_krWcp9DaXAlLWoQEhED0CWwuM7-DrAh_pPSFmUFKU_CjKA8WcpnxdztOtWli3PMat0y1hakrbBBfImWHdM07nB33j8ciaLP5jBtj1bBUunAn9NTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=mmcChpn6oNCa3Dr2xBCMLs-lXRg4FVeahqNLTIdzVPQr0NFWUmXBJtkcT8YRVVcMLGXsBtU8EobV_8JrMNvap3CFIwMzwnUajqJCE3R2TZJQ0_9CPRM_4ZWbmC2cM_5zw8Dpm2loBS-MC6TOaNLnkuxKaR9Zv8QcZvbBnjIK5HAjUEH_kf0bs8tgyzB-K-Etap9HxetC6epAweueLo80VPfMDEsaOCweyjmadH_krWcp9DaXAlLWoQEhED0CWwuM7-DrAh_pPSFmUFKU_CjKA8WcpnxdztOtWli3PMat0y1hakrbBBfImWHdM07nB33j8ciaLP5jBtj1bBUunAn9NTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlrhcJZs3j8CTRaVAr6I52XVsRBJ0bAo11k5IGHh1l-emLKLlyV_8o2Gou5amtEkK3BlTdvz3KQsTAv93IYSyj4Db3J_EHWeabQznnSXoAj98EBEdscyeVti4z3n7WeKvoBun-3CEOlEtEhymFgWxhR8AqH62OnVOgBY3wVEDW7SCcs1wIEC8ngKtNORkMK2iDrI2pjsWJPwkA1C_gBkvfvncP2jJtCepHIJsqNev6rroIutb6fahzLiewR6NCU4flNm6ffNHEmYoKGTycWz86HN9dYno-TcNAQxdgjbo9XauzRc2w4Rgeum8YxQzH9PAiFcYBJGq_cLJQsc6vwfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین
پس از آغاز نخستین محاصره بنادر ایران در
۱۳ آوریل
، حمل‌ونقل ریلی کالا از
شی‌آن چین به تهران
افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر
سه تا چهار روز
رسیده است.
این مسیر ریلی پیش از آغاز بحران نیز فعال بود.
نخستین قطار باری مستقیم از شی‌آن در
۲۵ مه ۲۰۲۵
در بندر خشک
آپِرین (Aprin)
در نزدیکی تهران تخلیه بار کرد. بنابراین، مسیر مذکور پیش از اعمال فشارهای دریایی ایجاد شده بود.
مسیر قطار از
قزاقستان و ترکمنستان
عبور می‌کند و سپس وارد ایران می‌شود و به آپرین می‌رسد. در این مرکز، محموله‌ها ترخیص شده و برای توزیع در سراسر کشور ارسال می‌شوند. حمل بار از این مسیر ریلی حدود
۱۳ تا ۱۶ روز
زمان می‌برد، در حالی که حمل دریایی در شرایط عادی حدود
۳۰ تا ۴۵ روز
طول می‌کشد.
افزایش تقاضا برای این مسیر هزینه حمل را نیز بالا برده است. قیمت حمل یک کانتینر ۴۰ فوتی در ماه مه به حدود
۷ هزار دلار
رسید که تقریباً ۴۰ درصد بیشتر از سطح معمول بود.
هر قطار حدود
۵۰ کانتینر
حمل می‌کند. محموله‌ها عمدتاً شامل قطعات خودرو، ژنراتورها، تجهیزات الکترونیکی و سایر کالاهای صنعتی و مصرفی هستند. قطارهای برگشتی که با ظرفیت پایین حرکت می‌کنند نیز هزینه حمل در مسیر غرب را افزایش می‌دهند.
بااین‌حال، ظرفیت ریلی قابل مقایسه با تجارت دریایی نیست. یک کشتی کانتینری بزرگ می‌تواند هزاران کانتینر حمل کند و انتقال نفت خام یا سایر محموله‌های فله‌ای در مسافت حدود
۱۰٬۴۰۰ کیلومتر
از طریق راه‌آهن از نظر اقتصادی مقرون‌به‌صرفه نیست.
در نتیجه، این کریدور ریلی نمی‌تواند تجارت نفت ایران پیش از محاصره را احیا کند یا جایگزین دسترسی آزاد به بنادر شود.
پس از آنکه آمریکا نخستین محاصره را در
۱۸ ژوئن
لغو کرد، این محاصره در
۱۴ ژوئیه
دوباره برقرار شد و اهمیت مسیر ریلی به‌عنوان یک کانال جایگزین افزایش یافت.
ایران همچنین از مسیرهای زمینی و ریلی دیگری استفاده می‌کند. خطوط ریلی در شمال به سمت
روسیه
امتداد دارند و گذرگاه‌های زمینی در شرق نیز امکان ارتباط با
پاکستان
را فراهم می‌کنند.
هیچ‌یک از این مسیرها از نظر حجم قابل مقایسه با حمل‌ونقل دریایی از طریق خلیج فارس نیستند، اما امکان انتقال بخشی از کالاهای مورد نیاز ایران از طریق مسیرهای زمینی و ریلی را فراهم می‌کنند
.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20142" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برخی اخبار تاییدنشده خبر از سفر عاصم منیر به تهران می دهند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20141" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انسان‌ها_بحث_درباره_خودآگاهی_هوش_مصنوعی_را_برعکس_در_نظر_می‌گیرند.pdf</div>
  <div class="tg-doc-extra">328.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/20137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک بحثی که وجود دارد اینکه یک مدل «رایانش قهری زیستی» هم مدنظر ممکن است قرار بگیرد. (Forceful Biological Computing) که در آن مغز یک انسان بدون رضایت خودش از طریق کاشت ابزارهای خاصی (نانورباتها یا ....) در اختیار یک شرکت پردازشگر هوش مصنوعی قرار بگیرد.  در…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20137" target="_blank">📅 15:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترکیه، فاکستان، عربستان، ایران، بنگلادش!  به نظرم اسمش را پیمان «جده» بگذارند بهتر است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20136" target="_blank">📅 15:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20135" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:
از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20134" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtH9B2oRS12E2iPEAYRBaTo6EeR-OpILbd0PU0HlkKMzjGnOQ5m6V_ZcekcbPijfllj8SVGr-Bnd79dA_eDcHBx5Oqy4jRoytgJXUlHaegr7x90iKyYNkSRpAsHeSf9myHL1CVWTPP9kEMmvvRZrqAwFOnUj44ZJT0ihDoYpoIWHRmxQf7jwntsCNObkr-_eLOjCokIV7uakQXUfOf3E4dO7peox6osoy67pRWIRbsDZtsUqUVAu3YovAbYXqOQ5h4mBG0yldNRBToCEpNwn-NBpwP9sRbrdmNDQFwhjdvfO3rsf-MA9T4sH3wxMpsJG680ugELI_xA97R1BxIOzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=ur19B98ibdZ7dwIOfHXGWhS-BWC9aBEXllnWk898Y-dtsv_QUVC5MeudPGuK6XEXPCC_8v1W6lx2iBWkNjnKU0GrEOiVWGae693UkNARGIkVq0Ucof9EA917cmTZcCU2bfpEtRnhJ6WWTCAsJPqo8Q88lZ2aQm7gdAPmwx1JKDmjmvNejIlNce7ff7UQn965xmWCJoZevW144S0mU-nrah9h_eRXNUC32WvhZFvvSwSSDvSeI_vh-NnoOHdm7wSdK10FNtMDrzGlACwV00WP5Wv9pvxfJhZYBGUdqrOVSDU5oj971z8rGO4-bSnlHrP2UdIOxXyff8HJwXv2iWpZcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=ur19B98ibdZ7dwIOfHXGWhS-BWC9aBEXllnWk898Y-dtsv_QUVC5MeudPGuK6XEXPCC_8v1W6lx2iBWkNjnKU0GrEOiVWGae693UkNARGIkVq0Ucof9EA917cmTZcCU2bfpEtRnhJ6WWTCAsJPqo8Q88lZ2aQm7gdAPmwx1JKDmjmvNejIlNce7ff7UQn965xmWCJoZevW144S0mU-nrah9h_eRXNUC32WvhZFvvSwSSDvSeI_vh-NnoOHdm7wSdK10FNtMDrzGlACwV00WP5Wv9pvxfJhZYBGUdqrOVSDU5oj971z8rGO4-bSnlHrP2UdIOxXyff8HJwXv2iWpZcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاریکاتور اکونومیست با عنوان «کمبود رهگیرها» تصویری طنزآمیز اما هشداردهنده از یکی از مهم‌ترین آسیب‌پذیری‌های جنگ‌های مدرن ارائه می‌کند یعنی محدود بودن ذخایر موشک‌های پدافندی در برابر حجم بالای حملات موشکی و پهپادی.
در تصویر، سربازانی که ظاهراً نماینده آمریکاییها و متحدانشان هستند، در حالی که تعداد زیادی تیر دشمن ایرانی در سپرهایشان فرو رفته، زیر بارانی از تیرهای دیگر گرفتار شده‌اند.
دیالوگ بالای تصویر نیز به‌صراحت می‌گوید که جهان به رهگیرهای بیشتری نیاز دارد، اما بخش بزرگی از ذخایر موجود برای دفاع از آسمان خاورمیانه مصرف شده است.
نکته جالب‌تر، شباهت بسیار آشکار ترکیب‌بندی تصویر به صحنه معروف فیلم
300
است؛ جایی که سربازان اسپارتی در برابر سپاه عظیم ایران هخامنشی، زیر باران تیرهای پرشمار، سپرهای خود را بالا می‌برند. این ارجاع تاریخی، پیام کاریکاتور را تقویت می‌کند: مدافعان امروزی نیز با وجود فناوری پیشرفته، در برابر «اشباع» شدن سامانه‌های دفاعی با همان مسئله‌ای روبه‌رو هستند که سربازان اسپارتی به‌صورت نمادین با آن مواجه بودند.
طنز پایانی تصویر نیز تلخ است: سرباز سمت راست می‌گوید «امیدوارم دیگر چنین اشتباهی نکنیم»؛ اشاره‌ای به این واقعیت که مصرف سریع رهگیرها می‌تواند در جنگی طولانی، خود به یک بحران راهبردی تبدیل شود.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20132" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خب دیگر بس است بخوابیم.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20131" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هر ایرانی در سال یک بار معتاد بشود و 2 بار ترک کند تا اینطوری تعداد معتادان کشور کاهش یابد و وابستگی کشور به تریاک وارداتی کاهش یافته و صرفه جویی ارزی کنیم.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20130" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هر خانواده ایرانی در خانه اش یک نفر را به عنوان سرباز آمریکایی اعلام کند تا ما دستگیرش کنیم و به آن خانواده 30 هزار دلار بدهیم.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20129" target="_blank">📅 01:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مردم در خانه شان تنگه های هرمز پرورش بدهند تا ببندیم و از کشتی های عبوری عوارض بگیریم!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20128" target="_blank">📅 01:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAzqEhrwGAuXb5X9je8fXfD00eOYQ7VeT_xROR4ueUMPcCz7tzG14wqMmov8nnkkw48pI3E5cZEuL45F7bHR7HY66Y90_s_dMpWiJXdkQ5C6HIfM8YEHrimCsvOAXXnZHpIhUSV5H6WxqSjUJq4bF0wRW5BRUtyoVGHlk6DEJViPbkS2Wn6HAYXwQCRzXln2OODq5hOblTmDUZwXgk__FZ16ydiqlA7ExzzyOKbU71Pz7t7c6G-iZP0uH0BHGXbpWTsgtCBO28JKdf1MMtg9SeiobiuNRYi_xJz75UuU_eU254XwvclxSEKkyGUe_lR6MTWTyMbmIEmJ6MA5nvqDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20127" target="_blank">📅 01:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTA6b1p8K-6FP7f4Wklz56oixaXEMOWG5OEnfnPs9jG9nlj0_Bz93d3qfYT9MNdUfN7nnd4lrB0mXManZdB2mZNi3-MkKpoe2HqIZc0JvH7ccgSsWGzV7SwkCi6dalTFIb-MZcCVWSsWvXQay7lB7xKTD3zApPApFuHgrU64tFeBYpBUaIm6nyAnHW5gnVr0KNeAShSZP3msG5_HAMcst5rRam0XnkiTeEDgrKKbP-J7wehfGKZpI-W7WgEsPTe4UwErASjArJsymRDBLBcitVuQoknAmyObnBeJyeqUVVCm0wU6k2tuM4P90sdbUeDtgxiEjJw33tYXPwq0ngNi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.  جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20126" target="_blank">📅 00:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ektmn7pjMvDW7zWPaNdbluaZ0EcArjqUKw-ilI493Kss2G30O1GIJmA5XXu8gPl-_4x-6pRMMOBY6Nl6G1q7Zj7jrgjPCFrnJ3uGPYCTiBpyrCsk5Fmd9MsOioV4FJZtM8ZPD248LYm5h4kYtEZIemf3Wo6ck8ykOwVr_NX00lBGotzpEJvsqDNqIh9_V53vVHuyNisicdI2VoYjE7urNJ0CHFo1FiyBRNf06OJrBBCbYcOFd8HMo8hq4nz73I0hkQc1PuGrTS9s1-LXDRrARkSrDlEGK8c_N6QDF951QGsOxcfD8NCw4WoAlXLVNdH9cK8GUh6ltBVXH7GA6V3HQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.
جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20125" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20124" target="_blank">📅 00:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20123" target="_blank">📅 00:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مردم فلافل بخورند و در خانه شان نیروگاه بادی راه بیاندازند</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20122" target="_blank">📅 00:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4MTLxxfMTvy9GymDR2WTiqOQcgR7_Dp8YJO4jhHx8wGcERMbJY0xqwBBBn4d_o9D6Yaoo0doCwZ4I0yhZAXsykY9C7X366fL38rNUUeSLyvNiOgFg77Xd8gnVoMhc8pGoEG2qvru0YhHcGlRtlU2V3eeChqdmgL5puF0UtLNQUwPKGX6MEw0-rCzk9gr_98ORZZqFtiXNjwaZdFIpqCdpIdivcqvga1si0OdpyW3g5LnjlWjeB2obZBdNBhz5Ui-5bgmzYwOqe8cZjg2-qb6wLQXwMFZYmKKuTbzrRUzGQ902N4hUjv1zrjAwSLJYxL9gStmk6hweafKTzPXgqMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!
ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20121" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHcVfEVxQUUEkfrq01I5clOZLD76TLcF4JcVKdkDzpdQFTlp9P6cRbdjWtSaoH1bOwBj-u2m3WBaS_I7ksxxzHOug8ytcirAFW38ODPnPyEkx4Az6k9vK_MTlXcv9A9mZTaeu00xALbC0EpnOYXx9qwVtRmUqjBo5czWZaevc3s3kwhuZHm1WbdgF6IV4nIsCOBCOhdFVRYR3WvSEuJowY5NgXsyg8j5e2pdoSfNAT4WmZ79-pctfPOXIcMEGAYmWVysK6_ocSbOTCY7BMTVWCqJgJ1VnkqRaNigfVD0S099001fgkp5th5SKJZ0eP8NH4UMfhR3Cj3CH6J28rJZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید یادتان نباشد ولی این نخبه نابغه کشورمان — دکتر حجت عبدالملکی — که حتی رییسی او را از کابینه اش اخراج کرد یک بار گفته بود با 1 میلیون تومان میشود کار ایجاد کرد!
یک نفر خوش ذوق هم زیر پستش کامنت کرده بود بله 700 هزار تومان دستگاه تقطیر با 300 هزار تومان کشمش!
البته الان با 1 میلیون تومان نهایتاً یک پیتزا با یک دوغ به شما می دهند و آبش را هم میدهند Meساکی بخورد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20120" target="_blank">📅 00:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">باید در هر کوچه یک شیره کش خانه باشد و بعد کنارش یک کمپ ترک اعتیاد بزنیم تا مردم هر کوچه از هم پول بگیرند و گردش مالی ایجاد بشود و مالیاتش را هم بدهند به ما.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20119" target="_blank">📅 00:28 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
