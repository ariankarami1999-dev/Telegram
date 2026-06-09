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
<img src="https://cdn4.telesco.pe/file/fHPZHJZtUXiINapr0PgZLJZIbrSzzD-MoaifJm43THw8FArR_M5Qyl_ud3JLhGyoGRnJEEZqnYuYcjomCESd-HE8MlE_gz_F_LupMoq2exmF85qflGwbIyBGKlDVM3GF7Jt9PRthbiMs_V-tWA_AZcz0w9iabsvPmKs1TX6KaY4dcSFYn8lZJCBC9B3Fp8YocUP_HfpOMsshc4GDmu2KPunbNsXXJCeAgsWz_--tEhOiRHpupkenLXoJXIxf_VpZGM2GUuXObAXtQS4nVHRHiSxgJq4h4Sy4XYPs1VlBmc6ulghQ8K0ba0C-UGotMfVRM_T-Fp9I5AEUBE4LdqtvwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 307K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-14175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc82e1504.mp4?token=H5efP7NjDe5KjnwKaGtPxJlWclvcXIAvjiifznXs2UNHLLgz_WGwNEBN1B7citUPbXHY4hJmHqo0PxqzWHmVbXMfriUAgDboPo8Su78kzCqdCvEccRWt--sAmbTZd-9QRmaB8ufysyb8o3YmtN3AOVpK8LDzBziFhmf8MVHua80IK6GsieJ-ykQl0U7RKYKI-oUyIHPuerrQVqGUzzDrTzcaZpU_pDT8Rq3hhaXsCPen9qFs8VEOLT3FV_6rMrILynu-YKsHTVth4CTpsIPYsPMLv9pSR8ulW4XmOtgXi6xbF7CLCalHI1FqrBmrwyg_zh0WvBx8qTHq4u4CyK-HCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc82e1504.mp4?token=H5efP7NjDe5KjnwKaGtPxJlWclvcXIAvjiifznXs2UNHLLgz_WGwNEBN1B7citUPbXHY4hJmHqo0PxqzWHmVbXMfriUAgDboPo8Su78kzCqdCvEccRWt--sAmbTZd-9QRmaB8ufysyb8o3YmtN3AOVpK8LDzBziFhmf8MVHua80IK6GsieJ-ykQl0U7RKYKI-oUyIHPuerrQVqGUzzDrTzcaZpU_pDT8Rq3hhaXsCPen9qFs8VEOLT3FV_6rMrILynu-YKsHTVth4CTpsIPYsPMLv9pSR8ulW4XmOtgXi6xbF7CLCalHI1FqrBmrwyg_zh0WvBx8qTHq4u4CyK-HCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/withyashar/14175" target="_blank">📅 23:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس تروریستی ج.ا :
دست آن رزمنده‌ای که در تنگه هرمز با سرنگونی هلیکوپتر آمریکایی (همچون شهید نادر مهدوی) سیلی دیگری به شیطان زد را می‌بوسیم، از او به عنوان یک قهرمان تجلیل خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/14174" target="_blank">📅 23:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1747743dd.mp4?token=GKOj7x4evP5xoOTd5L04mYGJnv3RcdJdnURUkmbGd49PO8PBWuDV-xChg-bqqvRq140B39UumbUPJC8nsDrWIUEuQiUZ29EC0nCb4Z7tDVWRuIKzXrazfM5ezK2na2SM8s2yGqLrqEEc8wm7ksI6qDPUFgXPVB3YBZwydNOKJIdOlQENwyXIvlcW9KhwHkRsE0VwfMCAL66lRtAej8hcb61ngxrVt_IZYPYvjl2Qkx5A8mwwF2btEMMRd7RsgqDEKKm07r4SmslhXCmOcy_smbfnwcrljvz1YUEHnYSDg4cEpE9a48FBuitlkXjvxzW_iKuKslbSP-MAH4dWVtpz8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1747743dd.mp4?token=GKOj7x4evP5xoOTd5L04mYGJnv3RcdJdnURUkmbGd49PO8PBWuDV-xChg-bqqvRq140B39UumbUPJC8nsDrWIUEuQiUZ29EC0nCb4Z7tDVWRuIKzXrazfM5ezK2na2SM8s2yGqLrqEEc8wm7ksI6qDPUFgXPVB3YBZwydNOKJIdOlQENwyXIvlcW9KhwHkRsE0VwfMCAL66lRtAej8hcb61ngxrVt_IZYPYvjl2Qkx5A8mwwF2btEMMRd7RsgqDEKKm07r4SmslhXCmOcy_smbfnwcrljvz1YUEHnYSDg4cEpE9a48FBuitlkXjvxzW_iKuKslbSP-MAH4dWVtpz8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد واشنگتن به دستیابی به توافق با ایران نزدیک شده است.
ونس گفت:
«ممکن است این توافق هفته آینده حاصل شود، یا شاید چند ماه دیگر.»
@withyashar</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/14173" target="_blank">📅 23:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ به وال استریت ژورنال: حادثه هلیکوپتر آپاچی موضوع جدی نیست و خلبان حالش خوب است!
ترامپ: به زودی پایان جنگ و پیروزی آمریکا بر ایران را اعلام میکنم امسال جام جهانی خوبی خواهیم داشت.
ترامپ: محاصره ایران رو به شدت فقیر میکنه و تا زمانی که نیاز باشه ادامه داره.
@withyashar
🚨
«این خبر ‌وال استریت ژورنال مال قبل از پست  تهدید ترامپ در تروث است»</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/14172" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار: شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
ترامپ: من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/14171" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ درباره ایران به ABC:
یک نفر باید همه آن زیرساخت‌ها را بسازد، پل‌های جدید، فلان چیز جدید، نیروگاه‌های جدید... آنها از یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر...
@withyashar</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/14170" target="_blank">📅 23:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع آمریکایی و اسرائیلی ادعا می‌کنند که اقدام نظامی قریب‌الوقوع آمریکا علیه ایران ظرف چند ساعت آینده انجام خواهد شد و آن را حرکتی بزرگ با دامنه نامحدود می‌نامند.
@withyashar</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/14169" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/14168" target="_blank">📅 23:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معاون وزیر امور خارجه رژیم جمهوری اسلامی با ترس به الجزیره گفت: ایران پشت حمله به یک هلیکوپتر آپاچی آمریکایی در تنگه هرمز نیست.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/14167" target="_blank">📅 23:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پست جدید از آخرین وضعیت و اتفاقات پیش رو کارهای اداریش را انجام بدید. کلیک کنید.
💥
💥
😁
https://www.instagram.com/reel/DZYFeVJS_V2/?igsh=MWNobm81Z282cWtmZQ==</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/14166" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b5cbaa3c.mp4?token=PlqMqEiXu_hXud2qK29QxbSsYyIzO0GjSllVVYTQUqtvejk3HatwkmUMkzG1wNt6cPMpJIBL4R7pcZKzrRy9BEGDB6eb-H4bmHG4fumTWhkD-EvOsf-LOnQ-Ax3eVDkXskMmv-BrZfjBkHIwDysAEFINWJ_jEMpRCkx83Y1ojq4WL7TfY1MGkIVX5oMVios-Z_PYrWkwMB0BzebqonQgCionC4I-GJy4VWMeG0-hfonRK5nbikPoZ4SHjHCyaIUFNipvG9eAzPSfOPagGAKwY4wg65Ue_1zBDP8uX_8lq0hJnV0OY3YbVSzlE1On4gD2-rbwe1dsNl2o9a7xji3LblNHRDFhTCLJymT6sKbARysKJRSnVy6PMoFMMGH1o7X7n_Xki1mKKoZCllda3RGpSmkYCygT1Znx2Yt0ZoUCLfbxESvc5LkKD9VzMQYaEjoyLRzrCqsC9qRES6ojvZ_AO13l3DYpfAXgOopLxasU6K9hwkhwzGqWmPQ2E9-hJyvOsk97lDZSgCj5aUYjCCif3_86yhrOii--wbTOvWLxea7Ag8CsKIjvQZFdbv06HuT_KX8VMTjJaqxCPsgyH6RKTkit9aCQZiuCukxZlDwUphVKBpzKADM0Q7A2nhtKB01Tx5A1e2coI5makn-pCEvHcrhYaYCwhbCBASDHf_bJIm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b5cbaa3c.mp4?token=PlqMqEiXu_hXud2qK29QxbSsYyIzO0GjSllVVYTQUqtvejk3HatwkmUMkzG1wNt6cPMpJIBL4R7pcZKzrRy9BEGDB6eb-H4bmHG4fumTWhkD-EvOsf-LOnQ-Ax3eVDkXskMmv-BrZfjBkHIwDysAEFINWJ_jEMpRCkx83Y1ojq4WL7TfY1MGkIVX5oMVios-Z_PYrWkwMB0BzebqonQgCionC4I-GJy4VWMeG0-hfonRK5nbikPoZ4SHjHCyaIUFNipvG9eAzPSfOPagGAKwY4wg65Ue_1zBDP8uX_8lq0hJnV0OY3YbVSzlE1On4gD2-rbwe1dsNl2o9a7xji3LblNHRDFhTCLJymT6sKbARysKJRSnVy6PMoFMMGH1o7X7n_Xki1mKKoZCllda3RGpSmkYCygT1Znx2Yt0ZoUCLfbxESvc5LkKD9VzMQYaEjoyLRzrCqsC9qRES6ojvZ_AO13l3DYpfAXgOopLxasU6K9hwkhwzGqWmPQ2E9-hJyvOsk97lDZSgCj5aUYjCCif3_86yhrOii--wbTOvWLxea7Ag8CsKIjvQZFdbv06HuT_KX8VMTjJaqxCPsgyH6RKTkit9aCQZiuCukxZlDwUphVKBpzKADM0Q7A2nhtKB01Tx5A1e2coI5makn-pCEvHcrhYaYCwhbCBASDHf_bJIm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : اختلال GPS
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/14165" target="_blank">📅 23:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شورای امنیت رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ها علیه جمهوری اسلامی ایران را تصویب کرد.
بریتانیا از فعال شدن تمام تحریم علیه  ایران استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/14164" target="_blank">📅 23:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پست جدید از آخرین وضعیت و اتفاقات پیش رو کارهای اداریش را انجام بدید. کلیک کنید.
💥
💥
😁
https://www.instagram.com/reel/DZYFeVJS_V2/?igsh=MWNobm81Z282cWtmZQ==</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/14163" target="_blank">📅 23:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرنگار یدیعوت آحارونوت: حملات آمریکا جوری خواهد بود هیچکس حتی فکرشو نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/14162" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/14161" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/14160" target="_blank">📅 22:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14159" target="_blank">📅 22:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پست جدید از آخرین وضعیت و اتفاقات پیش رو کارهای اداریش را انجام بدید. کلیک کنید.
💥
💥
😁
https://www.instagram.com/reel/DZYFeVJS_V2/?igsh=MWNobm81Z282cWtmZQ==</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/14158" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14157">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فرودگاه های تهران رو دارن تخلیه می کنند.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/14157" target="_blank">📅 22:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14156">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAN6MsfjlUENaJV__npoQ61BFnx0wEjkjaJxEwicZItA1FFmItkP4eDr0usx4HeZNffrphUR_RSXIY93XiSBrLiCTZddimnpDc_n7gBcg6he1kRvPK0l-0Lo8eivK33QxQHCW0eXQzYrx-7smhjh-PQUThjXBQIrA0EW2Ce5JZ7oy8FUFqtdFq4ACqXkSuFObNMiS2lsaVm3e5n4UJMVqg31JKlbY1mzYZQoP6iKuhT4OLp07SInS-qupxrzYRyzPhHOFBWSfT9oMAejMphlVVbVIybC7Nln5EDrya8N_hLyl0yvSugs0lCqUAlPzrXJT_91_gkpm_tWSROQlVug5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/14156" target="_blank">📅 22:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14155">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14155" target="_blank">📅 22:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14154">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آمادگی نیروهای مسلح برای پاسخ به هرگونه شرارت و تجاوزی
سخنگوی کمیسیون امنیت ملی:
نیروهای مسلح در اوج آمادگی‌های رزمی و دفاعی قرار دارند و الحمدالله آسیب‌ها رفع شده است.
نیروهای مسلح آماده‌اند تا در بالاترین سطح به هرگونه شرارت و تجاوزی پاسخ دهند.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/14154" target="_blank">📅 22:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14153">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ‌با کت باز گفت :  در واقع خیلی ساده است. برنده کسی است که قدرت دارد. ما تمام قدرت را داریم. @withyashar
😁</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14153" target="_blank">📅 22:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14152">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با شما :صدای مهیب اومد بعدم آمبولانس  پشت بندشم پدافند کار میکنه منطقه۶
@withyashar
یاشار : امشب هوای تهران طوفانی‌هم هست</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14152" target="_blank">📅 22:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ‌با کت باز گفت :  در واقع خیلی ساده است. برنده کسی است که قدرت دارد. ما تمام قدرت را داریم.
@withyashar
😁</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/14151" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14150">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش پرواز جنگنده های نیروی هوایی ارتش در جنوب غرب کشور
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14150" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرنگار العربیه: اسرائیل با انجام 4 حمله هوایی مناطقی را در جنوب لبنان بمباران کرد.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14149" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۴ اسرائیل: گزارش‌هایی از چندین انفجار در منطقه امیرآباد تهران منتشر شده است. این منطقه محل استقرار ستاد سازمان انرژی اتمی ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14148" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس:
نتانیاهو گزارش من درمورد احتمال از سرگیری جنگ توسط اسرائیل بدون آمریکا رو تایید کرد
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/14147" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14146">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار اسرائیلی:
من گیج شدم. دو روز پیش ایران به اسرائیل حمله کرد و ترامپ خواست ما جواب ندیم ولی الان خودش میگه باید بخاطر شلیک به هلیکوتر آمریکایی جواب بدیم.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/14146" target="_blank">📅 21:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14145" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14144">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نجات ۲ خلبان بالگرد آپاچی ۶۴ توسط قایق بدون سرنشین آمریکایی
سخنگوی فرماندهی مرکزی ایالات متحده(سنتکام) به رادیو ارتش اسرائیل تأیید کرده است که کشتی‌ای که دیشب خدمه هلیکوپتر آپاچی را در سواحل عمان نجات داد، یک کشتی بدون سرنشین نیروی دریایی ایالات متحده بوده است.
نیروهای عملیاتی از اواخر مارس شروع به استقرار چنین کشتی‌های بدون سرنشین در این منطقه کرده‌اند.
لشکر ۸۲ هوابرد معروف به شیطان نیز در این عملیات نجات مشارکت داشتند
.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14144" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14143">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اتاق جنگ با یاشار : خبر ۳ میلیارد دلار خبر فیک با منبع رسانه داخلیه
خودش هم گفته باز به نقل از یک مقام سپاهی!!!!
@withyashar
اون پرواز هم چک کردم رفته پرسنل رو تخلیه کنه !</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14143" target="_blank">📅 21:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14142">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرنگار فاکس‌نیوز در کاخ سفید:
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
«رئیس جمهور ترامپ احتمالاً در شرف دستور دادن به یک انفجار بزرگ در ایران است...
هیچ سرباز آمریکایی در اینجا کشته نشد، اما به نظر می‌رسد که ایران واقعاً، واقعاً سخت تلاش می‌کرد تا سربازان آمریکایی را بکشد، زیرا آنها یک هلیکوپتر آپاچی را سرنگون کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/14142" target="_blank">📅 21:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سی ان ان :  یک پهپاد شاهد ایران  یک بالگرد آپاچی ۶۴ آمریکا را سرنگون کرده است.
قیمت پهپاد شاهد بدون رنگ : ۲۰،۰۰۰دلار
قیمت هلیکوپتر آپاچی ای اچ -۶۴ مدل سال : ۳۱ میلیون دلار
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/14141" target="_blank">📅 20:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">منبع عراقی  : یک موشک روسی اوگلا-اس به یک هدف هوایی که قصد عبور از تنگه هرمز را داشت، اصابت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/14140" target="_blank">📅 20:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیویورک تایمز: ترامپ از اینکه نمی‌تونه مستقیم با آیت‌الله خامنه‌ای صحبت کنه خیلی ناراحته و حسابی ناامید شده
این خبر فیکه  داره پخش میشه !حتی ترجمه عنوان هم چیز دیگست
خبر اصلی :
https://www.nytimes.com/2026/06/09/world/middleeast/us-iran-talks-war.html?utm_source=perplexity
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/14139" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی مدعی شد:
تحقیقات به این نتیجه رسید که یک پهپاد ایرانی با یک بالگرد آمریکایی برخورد کرده و موجب سقوط آن شده است.
این مقام آمریکایی مدعی شد هنوز مشخص نشده است که این ساقط کردن هلیکوپتر با پهپاد، تعمدی بوده یا خیر.
@withyashar
با این حال، کمی پیش ترامپ در شبکه تروث اعلام کرد که انتقام این کار ایران را میگیرد.</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/14138" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قالیباف: ما زبان دیپلماسی را ترجیح می‌دهیم، ولی زبان‌ غیردیپلماسی را روان‌تر صحبت می‌کنیم / شما سوار همان اسبی می‌شوید که زین کرده‌اید
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم.
اگر تعهدات خود را بشکنید، ما به همان زبان که خودمان بهتر بلدیم، روی می‌آوریم. شما سوار همان اسبی می‌شوید که زین کرده‌اید!
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/14137" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14136">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/14136" target="_blank">📅 20:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14135">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694d9db426.mp4?token=t0K0ZlE8XtwBVL4dNkNo6mzH1MAO-DR7iffdS8l1vAYXTFMveGIdkncQ8vb-YtO5gHmxV_wBZRXnHBR8X8-9hGeIzAFBU7hfKecE08IEWsivZmVm06MWJbC6fcp2UELCtmUvN73kfCoD70GvKskK_6n9pSVJzC0EPKvOfOiKd4LrSlZxD6_x7qSLzcugugrdR9xh6B_EW68ImGolbTilaUBuAvuLrqslazbhEo9DvWpxpoI_PCY30x6iHmf-blcyTWMFaN5KrNHFK7bGih2fZARTpyHHM0Y7me764EnCHS6sHTT0omAX9NL8y3dS2Gs5iYPZ3H1DGtqQQn1r4IP5kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694d9db426.mp4?token=t0K0ZlE8XtwBVL4dNkNo6mzH1MAO-DR7iffdS8l1vAYXTFMveGIdkncQ8vb-YtO5gHmxV_wBZRXnHBR8X8-9hGeIzAFBU7hfKecE08IEWsivZmVm06MWJbC6fcp2UELCtmUvN73kfCoD70GvKskK_6n9pSVJzC0EPKvOfOiKd4LrSlZxD6_x7qSLzcugugrdR9xh6B_EW68ImGolbTilaUBuAvuLrqslazbhEo9DvWpxpoI_PCY30x6iHmf-blcyTWMFaN5KrNHFK7bGih2fZARTpyHHM0Y7me764EnCHS6sHTT0omAX9NL8y3dS2Gs5iYPZ3H1DGtqQQn1r4IP5kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/14135" target="_blank">📅 20:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14134">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ در تروث : «به من همین حالا توسط ارتش بزرگ‌مان اطلاع داده شده است که دیشب ایرانی‌ها یکی از بالگردهای بسیار پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه حضور داشتند و هر دو سالم و بدون جراحت هستند. با این حال،…</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/14134" target="_blank">📅 20:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14133">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLqaZnCBB_KZ_a1IguAC4Igbrp1gJHjVHnRILgi-3kWBqn1a9sVwN5_Lwds_3Q8C30Iq0Wlsyg7xsNqljC_9ee3rpFvyUm6eZbNgJtxIjF5C2NWZ6KNSAI-5zB_VAXJ0zxQGsNZ1uTAmPaOcV38FfcGL4Kt2GhX3aRd7nm-ThmMK9IxLraFvDw__km5h-YAYW0i-_SejAZR3IvsUcZoDASinpefSRL3d9DWhaHqgqsk4MYtv4rPFbbrV1wUuZBv6IEaPMGSNu8RpcgXBIn_8qRy8tkSQzwu4s_clNuVJIavJieiho534Ha3vsW3PDapvFyWc4LsHMgX_XZmnDptUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «به من همین حالا توسط ارتش بزرگ‌مان اطلاع داده شده است که دیشب ایرانی‌ها یکی از بالگردهای بسیار پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان در این حادثه حضور داشتند و هر دو سالم و بدون جراحت هستند. با این حال، ایالات متحده ناگزیر است به این حمله پاسخ دهد. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14133" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14132">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/14132" target="_blank">📅 20:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر انرژی آمریکا: بازگشت جریان انرژی به حالت عادی ماه‌ها طول خواهد کشید
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/14130" target="_blank">📅 20:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQkNBxiF_YMDdGgO3QdIUhP6wjvgb4QE62OTEj7LubLLE1r2qHCyyylvIG041EptpOMcWNO2JWKgQ2WfY0iE6UvQOOCNTiODMpoal55TK9GkBHkqZiUUiSFvyYLY8ahhJa3NKZxX3wVOEWaHyuTPOq2LKkIPslZRRUW0hOnqc8yvb1VoHFIJxJZAJQwg1gS4eNQ7o3PO_LwiNRXJZXi1iVxsmXy5_El3cFKYSQMVbH_6HLS92qk_mJyTGe_SuNkQb1vHxCYcrCunFXjCZ_cuLBetrHos71bB0XANhtk8o5TLbm3mR6EQq2ZbZ4XT9qC_82WIHP32gFgcD0ou9DgE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود همین الان تهران محدوده ولنجک @withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/14129" target="_blank">📅 19:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آغاز حملات جدید اسرائیل به صور در‌جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/14128" target="_blank">📅 19:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9WdoCnCQxDfpbLgtKfpp6Id-6muez1rNe02JcUy4TiMIt5Kss6Kz9-BQMj2-xj-hnCvo0u-8TDsAZ_8xiriSXRnIbti2hVVrKTtqb54FXs4GIuD5h0xp_yCA8Qr6ligNZh9w4LaOSq5iyj99cO_IXKaxPrsanCsLefC8ea1Y5MoxOFCynkhcO34CUI5qe46QxvEKI6A-jiz-V2nGQNZkYhLTkZIQnDj97zr-enLqR7yp_AgLTWzcj_Duo8lr-Qx5w0PzJ1fJoDVJKVDsLifvNz48ZNYESdP7OJS3Pw_E9nXecOZs11FGI3VbqtWGphVax2jteb7wZl5DFxFiuZHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیراز  یک ربع پیش
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/14127" target="_blank">📅 19:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برنامه حضور تیم‌ملی در آمریکا مشخص شد
سخنگوی فدراسیون فوتبال:
کاروان تیم براساس برنامه فیفا، با پرواز چارتر به آمریکا می‌رود؛ یک روز قبل بازی مقابل نیوزیلند تیم به محل می‌رود و در دو بازی بعد، دو روز قبل مسابقه در محل میزبانی حضور پیدا خواهیم کرد.
بجای بازی با گرنادا، مسئولان فدراسیون در تلاش هستند تا یک دیدار هماهنگ کنند که این بازی پشت درهای بسته برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/14126" target="_blank">📅 19:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شبکه الحدث:  نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌‌اند
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14125" target="_blank">📅 18:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه العربیه، به نقل از یک مقام کاخ سفید: مذاکرات درباره توافقی برای جلوگیری از دستیابی ایران به سلاح هسته‌ای نتایج مثبتی به همراه دارد
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/14124" target="_blank">📅 18:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اکسیوس به نقل یک منبع آگاه:
عملیات جستجوی فشرده ساعت‌ها طول کشید تا خدمه بالگرد آپاچی پیدا بشن.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14123" target="_blank">📅 17:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش های محلی در لبنان،از آغاز پیشروی نیروی زمینی ارتش اسرائیل به سمت بندر صور، بزرگ ترین شهر جنوب لبنان گزارش می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/14122" target="_blank">📅 17:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آکسیوس به نقل از مقامات آمریکایی: ما در حال بررسی این موضوع هستیم که آیا شلیک گلوله از سوی ایران باعث سقوط بالگرد آپاچی در نزدیکی تنگه هرمز در روز دوشنبه شده است یا خیر.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/14121" target="_blank">📅 17:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسکای نیوز عربی:
ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون میده دولت ترامپ اون رو تا حدودی قابل قبول میدونه.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/14120" target="_blank">📅 17:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیروهای رضوان حزب الله اعلام کردند بصورت زمینی وارد شهرک های اسرائیلی شدن
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14119" target="_blank">📅 16:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ستون دود همین الان تهران محدوده ولنجک @withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/14118" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: تنگه هرمز بلافاصله پس از امضا باز خواهد شد، که ممکن است در دو یا سه روز آینده باشد
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/14117" target="_blank">📅 15:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT2eLPspFoHHPhNX-UbB9T_cL64kZzQ6P4Q0XviqZZfIwrkO-pn2XdsZLAumo7jq39cMOBDp5TGv9Dw3u_YWRH-F1jYi90HmcYHIUqUNgDJV_muWORH5B3q6aBoEwIvb6YzJB4hW6mKlHUADGEGplfWe0NFod1nG-sUkTPsJva7DGd4T99Zpop8ldNIahtqG_XkprQLJrYE1Z6IAF-NkbjP_LLSYbtaPnSLL0Ydy0a9W85d-KiSzAZhB9WanLr1gPsNU34YQmg78PsZVC0d_1JURBFQ_oCb3zZqTNVEe4ineoMfeQlaA2f9R3BCVG3WGwZD5cgpyBz6z-5QmhkVwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود همین الان تهران محدوده ولنجک
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/14116" target="_blank">📅 15:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شبکه 14 اسرائیل
«کابینه اسرائیل تصمیم گرفته است در پاسخ  موشک‌ها یا پهپادهای حزب‌الله که شمال اسرائیل را هدف قرار دهند حمله متقابل به بیروت را در دستور کار قرار دهد.»
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14115" target="_blank">📅 15:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال ۱۲ عبری، به نقل از یک منبع امنیتی:
ما وارد مرحله «دورهای مکرر» با ایران شده‌ایم. ارزیابی‌ها حاکی از آن است که تشدید اخیر، رویارویی نهایی با ایران نیست
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/14114" target="_blank">📅 14:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14113">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee75a2eed.mp4?token=pdDPivPmhQf-b_PclPy-87DcoVSfrRwBHoN5ZiJgVQVdb4nwkWg2rWU2ZoCdHj5aJL2e9SaOZAE66kr4X5soHyCYoPV_RxzXfhmz0BO-5iIgycrLcRIUqVjRQZFynlbyJ2Xv8fjIryDDyJEvjQqBhyQRCRCHsjvi97MChhr3HQPvyHafVk-It0PA6kSh6pQsaEZ6BLm-dcfgdwHguQtAgdL0s5JwPHaLo3Bkfy5iSy8MFqQ1a8GCL-lFpHxdEoVAkjKa9K72fUIJno0TzYZAAD6Zk7mnAK2uIfjH8JPJf40ytJPpWoJx3XLU1QKN8WBAxDsohRNc0t5zGsWra9yeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee75a2eed.mp4?token=pdDPivPmhQf-b_PclPy-87DcoVSfrRwBHoN5ZiJgVQVdb4nwkWg2rWU2ZoCdHj5aJL2e9SaOZAE66kr4X5soHyCYoPV_RxzXfhmz0BO-5iIgycrLcRIUqVjRQZFynlbyJ2Xv8fjIryDDyJEvjQqBhyQRCRCHsjvi97MChhr3HQPvyHafVk-It0PA6kSh6pQsaEZ6BLm-dcfgdwHguQtAgdL0s5JwPHaLo3Bkfy5iSy8MFqQ1a8GCL-lFpHxdEoVAkjKa9K72fUIJno0TzYZAAD6Zk7mnAK2uIfjH8JPJf40ytJPpWoJx3XLU1QKN8WBAxDsohRNc0t5zGsWra9yeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین اسرائیل به جنوب لبنان شهر صور
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14113" target="_blank">📅 14:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14112">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به گزارش اکونومیست، ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14112" target="_blank">📅 14:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14111">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای ترامپ درباره ایران:
اگر برویم و بمباران کنیم، که اگر بخواهیم خیلی آسان می‌توانیم این کار را انجام دهیم.
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را بکند؟ من نمی‌خواهم.
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14111" target="_blank">📅 13:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14110">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 آیا شما از تیم ملی جمهوری اسلامی در جام جهانی ۲۰۲۶ حمایت می‌کنید؟</h4>
<ul>
<li>✓ خیر ، بر زدشونم هر کاری باشه میکنم</li>
<li>✓ خنثی ، فقط دنبال میکنم و میبینم</li>
<li>✓ بله ، تمام قد پشت تیم ملی هستم</li>
</ul>
</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14110" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14109">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه‌های ایران می‌گویند دو تن از اعضای «نیروی پدافند هوایی ارتش» در حمله دیروز اسرائیل کشته شدند و امروز تشییع می‌شوند.
تاکنون در حملات دوشنبه و سه‌شنبه اسرائیل کشته‌ای گزارش نشده بود و ۱۵ زخمی اعلام شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/14109" target="_blank">📅 13:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14108">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7566ed8ca7.mp4?token=kOkf5h6bPAs_YqrDKkDIdc9v1opDhUzGDIvZaUrklDUyiOfltrQehtYV5LL0Gf_5Gs-XDksb-PZtCjQ259ol2ja1RIkJ8cjujIfrQKZEdt_hEHcrm_PI3toTF1yJrr4HriEE5DLGxYEI-U-QhaCi1rI9JNoLy0E-Q8xyUIk4E1Yu-Qseht0QP13mdY7PuNP7hAeGRrrr3ghCR0LliRAZIhR9Xp5fwfkRRCWNgjHDh4XCFplWcM_ZvabhxzFPNCTLeNH2FoGsYaIkOqKTUjD-SSRvCzUoFVhtZoMlcNL3JvOJMvghXz9iGijgnj8__-x6AAE5AJN23xJv0-ET1LOHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7566ed8ca7.mp4?token=kOkf5h6bPAs_YqrDKkDIdc9v1opDhUzGDIvZaUrklDUyiOfltrQehtYV5LL0Gf_5Gs-XDksb-PZtCjQ259ol2ja1RIkJ8cjujIfrQKZEdt_hEHcrm_PI3toTF1yJrr4HriEE5DLGxYEI-U-QhaCi1rI9JNoLy0E-Q8xyUIk4E1Yu-Qseht0QP13mdY7PuNP7hAeGRrrr3ghCR0LliRAZIhR9Xp5fwfkRRCWNgjHDh4XCFplWcM_ZvabhxzFPNCTLeNH2FoGsYaIkOqKTUjD-SSRvCzUoFVhtZoMlcNL3JvOJMvghXz9iGijgnj8__-x6AAE5AJN23xJv0-ET1LOHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار و آتش سوزی پادگان سپاه کنار کوه صفه اصفهان
پیشتر رژیم اعلام کرده بود امروز اصفهان خنثی سازی مهمات عمل نکرده انجام میشود
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14108" target="_blank">📅 13:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یوتیوب رفع فیلتر می‌شود
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14107" target="_blank">📅 12:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/14106" target="_blank">📅 12:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سهمیه بلیت تماشاگران ایران در جام جهانی حذف شد
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14105" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14104">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3559129ca.mp4?token=Kf8V7GKQbgVfxDWwc-8FQKOOFDxIVyDrr6YRsKas_g3zjeWkK_ijWiV96k7MQxp8sj3ycFzpEEyx8m9v8wNOe2sFkkoBDGcYKj8DYwioy9RXuWPg7roJlPeFyBhx1r6oQ8RwqFxIy1oWomYtwnbcDojg2eSccYlnkoDsUZXzHo9nsP6zFSXnewTpUikJ4JF_cNObbytd7_v2wOSw8WM24D5HNz1y_zIGa6MOc-80irlVwoWE3iPv44AQ_kciW3Zo4hLR6xm_l1PZFvNWoVfId-uTJyuIPxflWxibB24EKBLWNc8euVWmm3xAT3uRp4p_0XzBTeWDl_lmS7RtLe01GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3559129ca.mp4?token=Kf8V7GKQbgVfxDWwc-8FQKOOFDxIVyDrr6YRsKas_g3zjeWkK_ijWiV96k7MQxp8sj3ycFzpEEyx8m9v8wNOe2sFkkoBDGcYKj8DYwioy9RXuWPg7roJlPeFyBhx1r6oQ8RwqFxIy1oWomYtwnbcDojg2eSccYlnkoDsUZXzHo9nsP6zFSXnewTpUikJ4JF_cNObbytd7_v2wOSw8WM24D5HNz1y_zIGa6MOc-80irlVwoWE3iPv44AQ_kciW3Zo4hLR6xm_l1PZFvNWoVfId-uTJyuIPxflWxibB24EKBLWNc8euVWmm3xAT3uRp4p_0XzBTeWDl_lmS7RtLe01GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور اتباع کشورهای مختلف در تجمعات شبانه حکومتی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14104" target="_blank">📅 11:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14103">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه cnn: ترامپ ۳۷ بار توافق با ایران را «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده!
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14103" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14102">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر ارتباطات: ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/14102" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14101">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه های رژیم :
هلیکوپتر تهاجمی آپاچی AH-64، بعد از عدم توجه به هشدارها توسط نیروی دریایی سپاه پاسداران و بوسیله شلیک یکی از قایق های بسیج، ساقط شده است.
این در حالیست که با توجه به قریب‌الوقوع بودن اعلام متن تفاهم مشترک، اسقاط این هلیکوپتر به نقص فنی مرتبط شده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14101" target="_blank">📅 10:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14100">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14100" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14099">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ گفت خلبانان بالگرد آپاچی که در تنگه هرمز سقوط کرد، سالم هستند. او گفت آمریکا امروز گزارشی درباره این حادثه منتشر خواهد کرد.
@withyashar
این حادثه در دست بررسی است و هنوز مشخص نیست که آیا این بالگرد با شلیک نیروهای جمهوری اسلامی سرنگون شده، دچار نقص فنی شده یا با مشکل دیگری مواجه شده است.</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/14099" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14098">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حملات سنگین اسراییل به صور لبنان
رادیو ارتش اسرائیل: ما محدودیت‌هایی برای حمله به بیروت داریم اما برای عملیات در جنوب لبنان محدودیتی نداریم
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/14098" target="_blank">📅 10:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14097">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فارس: تجهیزات هدایت و پشتیبانی جنگنده‌های اسرائیلی در جنگل‌های تنکابن(شهسوار) کشف شد
خبرگزاری فارس گزارش داد مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایه که گفته می‌شود برای پشتیبانی و هدایت جنگنده‌های مهاجم مورد استفاده قرار می‌گرفته، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شده است.
بر اساس این گزارش، این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌ها به حریم هوایی تهران مستقر بوده‌اند.
فارس مدعی شده منطقه مورد نظر در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شده است.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/14097" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14096">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حزب دمکرات کردستان ایران کمی پیش  امروز سشنبه در شبکه ایکس خبر داد یکی از کمپ‌های این حزب بار دیگر هدف حمله پهپادی جمهوری اسلامی قرار گرفت.
بر اساس این گزارش در این حمله دو فروند پهپاد به سمت "کمپ آزادی" شلیک شده‌اند.
کمپ آزادی محل اسکان خانواده‌های اعضای حزب دمکرات است و از آغاز درگیری‌های اخیر تا کنون بارها هدف حملات جمهوری اسلامی قرار گرفت. این حزب تا کنون گزارشی درباره تلفات جانی یا زخمی‌ها ارائه نکرده است.
بر اساس این گزارش، جمهوری اسلامی ایران از زمان آغاز درگیری‌ها با آمریکا و اسرائیل تا کنون با شلیک بیش از ۱۳۴ فروند موشک و پهپاد، کمپ‌های حزب دمکرات کردستان ایران و همچنین مراکز درمانی و آموزشی این حزب را هدف قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14096" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14095">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af93d53bde.mp4?token=DYaSGmbRi6nXlwTyQ5n_LszwKygtLaFfUrypwxTyutfl3LSEVYPpbipcBQUDpsLCojWpannBqp9aPb1hZuH5yAyBGvBwY5mjlv9eUAeqQ-6ZlvQHs62X5ctUV08FMOp6q-ERiy_FyENMXKb4q0OJFg3CP1MAFoKWzbdOTdEl_stl8iKT7C995JngdnqolBOUb7DRQyCSK2ZgRgazSa0jXDzy3FPsMA7ZdE_Bt8RDEqEf7M2o5yOkGS5ZShs6pDM6FQuWSOQt5Fjgg9vC_-W3cempI0Wq9nl6Et8Bv4wzqL6-Iy1knrK9tIV_Kj2RxnRU-kuYudny9zS6ehYaHWy10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af93d53bde.mp4?token=DYaSGmbRi6nXlwTyQ5n_LszwKygtLaFfUrypwxTyutfl3LSEVYPpbipcBQUDpsLCojWpannBqp9aPb1hZuH5yAyBGvBwY5mjlv9eUAeqQ-6ZlvQHs62X5ctUV08FMOp6q-ERiy_FyENMXKb4q0OJFg3CP1MAFoKWzbdOTdEl_stl8iKT7C995JngdnqolBOUb7DRQyCSK2ZgRgazSa0jXDzy3FPsMA7ZdE_Bt8RDEqEf7M2o5yOkGS5ZShs6pDM6FQuWSOQt5Fjgg9vC_-W3cempI0Wq9nl6Et8Bv4wzqL6-Iy1knrK9tIV_Kj2RxnRU-kuYudny9zS6ehYaHWy10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز همین الان
@withyashar
گویا دود فلر ‌نفتیه</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/14095" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14094">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ec6b7e1.mp4?token=KMYiQF46dhpZzgtt1XUm3zJDUlUv0NCj7H5MMPmsdWp4YUnm3abPoO-j7Ohc38nWioybYuIUXudAGRAWt-_FREMdUbL5Hi_PQ80lXqWfqQfGJ9MOlxF1mrpUiob3KsnbIXgsf05uzvvILQP1rTOEZJPLAPfAY4crVI6_6iMJoJeM0cbDak1VZ1NZiYZQi1QaVedhya1ADkX9ihzPzozZetEVEtx-VL3Dkl6Z-lVRfOlCHFSDdZXgptmqc2l4n8WJHS_qCvU2xroWzFrZ2eN0mk8_DkidYa0iLDS_1UQqoLUULdYXocbU06dIHU87Sq53DQq77WvdEQOs0FqOsBrX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ec6b7e1.mp4?token=KMYiQF46dhpZzgtt1XUm3zJDUlUv0NCj7H5MMPmsdWp4YUnm3abPoO-j7Ohc38nWioybYuIUXudAGRAWt-_FREMdUbL5Hi_PQ80lXqWfqQfGJ9MOlxF1mrpUiob3KsnbIXgsf05uzvvILQP1rTOEZJPLAPfAY4crVI6_6iMJoJeM0cbDak1VZ1NZiYZQi1QaVedhya1ADkX9ihzPzozZetEVEtx-VL3Dkl6Z-lVRfOlCHFSDdZXgptmqc2l4n8WJHS_qCvU2xroWzFrZ2eN0mk8_DkidYa0iLDS_1UQqoLUULdYXocbU06dIHU87Sq53DQq77WvdEQOs0FqOsBrX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ان‌بی‌سی نیوز : وقتی رئیس جمهور ترامپ در بازی سوم فینال NBA هنگام پخش سرود ملی روی جایگاه تماشاگران در مدیسون اسکوئر گاردن ظاهر شد، توسط جمعیت (BOOE) هو شد.
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/14094" target="_blank">📅 09:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14093">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پنتاگون شرکت‌های BYD، Alibaba و Baidu را به فهرست شرکت‌های متهم به همکاری با ارتش چین اضافه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14093" target="_blank">📅 09:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14092">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویورک تایمز:  یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
هنوز مشخص نیست که آیا این بالگرد توسط آتش‌ ایران سرنگون شده یا دچار نقص فنی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14092" target="_blank">📅 09:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14091">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره لیندزی گراهام:
او برجسته است. مدت‌ها در کنار من بوده است.
ما ابتدا مدت‌ها پیش بر سر موضوع کاندیداتوری با هم مبارزه کردیم. او کاندیدا بود و من هم کاندیدا بودم، و ما مبارزه کردیم، و من شروع کردم به این که بفهمم او فردی بسیار بااستعداد است.
بعد از آن مبارزه، ما بهترین دوستان شدیم و او به من به اندازه هر کسی در سنا کمک کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14091" target="_blank">📅 02:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهم کردم!
رئیس جمهور ایالات متحده: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14090" target="_blank">📅 01:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کن کلیپنشتاین، روزنامه‌نگار آمریکایی، مدعی شده اسناد محرمانه‌ای را دیده که نشان می‌دهد بخشی از نیروهای لشکر ۸۲ هوابرد آمریکا در آوریل ۲۰۲۶ به‌طور مخفیانه به اسرائیل اعزام شده‌اند. به ادعای او، این نیروها در چارچوب برنامه‌ریزی مشترک آمریکا و اسرائیل برای سناریوهایی از جمله تصرف جزیره خارگ ایران و ایجاد یک منطقه ساحلی در داخل خاک ایران آماده شده بودند. این ادعا تاکنون از سوی پنتاگون یا دولت آمریکا به‌صورت رسمی تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14089" target="_blank">📅 01:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ به اسکای نیوز:
من فکر نمی کنم اسرائیل به جنگ با ایران بازگردد. همه چیز خیلی خوب پیش می رود.
ایران کاری را که باید انجام دهد انجام می دهد. من فکر نمی کنم این اتفاق بیفتد، اوکی؟
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14088" target="_blank">📅 01:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">زلزله شدید بندرعباس الان @withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14087" target="_blank">📅 01:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک منبع جمهوری اسلامی به الجزیره: آمریکا تغییرات غیرقابل قبولی در پیش‌نویس یادداشت تفاهم ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14086" target="_blank">📅 00:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جنگنده غرب تهران
قشنگ دیده میشد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14085" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">زلزله شدید بندرعباس الان
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14084" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدا جنگنده در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14083" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حمله پهپادی حزب‌الله به اسرائیل
🚨
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14082" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش صدای انفجار از‌ دروازه دولت
🚨
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14081" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش از وقوع انفجار مهیب در محدوده گیشا تهران؛ لرزش شدید ساختمان‌ها و شیشه‌ها.
هجوم شهروندان به خیابان‌ها در پی شنیده شدن صدای انفجار و ایجاد رعب و وحشت.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14080" target="_blank">📅 00:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک پهپاد از لبنان به شمال اسرائیل نفوذ کرد و آژیرها به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14079" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جروزالم پست :  هشدار نفوذ پهپادها گالیلای علیا و جولان (1 مکان). در حال به‌روزرسانی...
وارد اتاق امن شوید و تا اطلاع ثانوی در آن بمانید
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14078" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArad</strong></div>
<div class="tg-text">گیشا یک صدایی شد پنجره لرزید و مردم چند نفر ریختند بیرون</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14077" target="_blank">📅 00:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمکران</strong></div>
<div class="tg-text">صدای انفجار اومد سیریک ولی دور بود</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14076" target="_blank">📅 00:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">فکر کنم گیشا رو زدن</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14075" target="_blank">📅 00:23 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
