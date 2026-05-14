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
<img src="https://cdn4.telesco.pe/file/ZwU5FRkFVVi4W3--nE4ASkrpBRCLK1i59lx9CxsYfdtCr-wEH1ajyW8R6tRxn3j7qiWBjhmBN_w5WmtFmQRyD6rqh3G6ct4JO-RdmKp842Bbr3bBGGNkTwJu5I-QxL--vbdy9qrMrf-288F6hxFf1sslkJICoQHHai72qGQWRDLdlADFtmkmxeTVcqKh2-7W8yQv_qSAUC9vJk3G5BwizMsNbMW9t2q6SHvJzTHKXSNYItYorUc7Aczh5yyeqUPDbDM66P-VGgV_G6ZItsdXWqBrKC4v0KvXKBmVJdMiWRf2f0wvVgP52lyqsjkvRtg0HgA5IhnVmkq0Ryj55sMrrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 07:08:59</div>
<hr>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyFQgGlz8HAw9eu44AC_Qq50Q0uDcOoGNVSjSz-KsH0gm-c2e7ftlKIs6sodfhqv8F0z6PkK3Lmyi1Mn7uu3iaQp9tImrITccN2O1ladJDRKYLLT6yG91YlCuVwrhSODgXgCEDIn5scbXH15bYZb6ouix5XWzJYHdY5sIktY9xHDaFUgB45dCWioWHxx2BNkNtEmoqz0YBKO6BLL9SBQvYEvQXtVNHamCTDIAcpNqh840j18UagAxccU-YnqtLkavAGMh-7mxniUYjGQbDHfB9x9daMORHpchVOud4Fl-0G9Q1orEvfXLe64T_WDEZ4lIRVTAlM4u5g773OPI_3g_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HM3QqjzLuON98Gez4LbFHoDP8tkC_0PG0-VIFqvD8lgVWyicnjJASuERJjlGB7xJU5yNmHrf9Aqf3xQPWxaqGbfM2B_umiIvxlRaYLdZfqnmHgGxf7Xa0MxuUQpTQOz_gYF8dvB_ogcnnGzpNrOeHnZ6JeyenWJ_s3ePjIVeALxPGzBn--07KGtI6lkdEYL9P4jGNoTA5ZTz3qCQMYnBm4cBZV7_ayC88K2eobYC6wNf97CPpBNdrPfa39BYzUGmiYsEo-bihmeVL0hAgnEcVKJAZx3xzmivlWbTkQAGEceFBQQendUTvUe1E8prr2vdrFx741G41h6AI4zFDNwubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY_DF8kBNmLEoLm1H87lUX8Q0rz2xRTJkxTDr7i7JWyF2yetmEbb3eJ4MJU1Alh5rUT3jes2fvBJwQysMenlP8yXqRYak27iYDMhqqDeESk09OxtWnVYYx7bb1riC7CXqFoXfag6tWT-mu3evrg7-IjKWcAAPmyksCY7NxtXOqIHQ8qOgC2Mhs2JE6gDkxjZHDgwEtOv1--7EujiSQ1j3bhrtjGpnJcnBs58U5MXd2guE067H8zfRhGYwGNc2odeqL6ubLLpsvEvarMItrKvlhb3G_ufiPK5abWdd6u3qbC7hbCAKgwpyRfNDiMM9YPSe8djGujGVwbSW5aQfs3kyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYvjgxBBVU5UIQEvzfgTzpcp9gZ3s87Pa0jLKvapvoCq4uA6v66HO8pkpmt6__ThS-wnunfEk4iDO6QqZfDIFBxswvl0QCcZY7_mtJrb3NpkJIl5nPQ06ceYXg7CFjrZXWBOjERa4Rsx94aWvQRv9IV2VFI9jLJuchpyu-3r_XQ3Nc-KMYaHhr8k1TMgwBe90-5wRwKVeNnmrGCOWDkuNKgmQR_XoyNLyDCPDQYWTYa5-zoL_3x_Xe2Puh_m7VS2Lm4QXDtAB5LAGahV-Z0AHeA6jPEg0BlGdfU9FaQNsIROQfln4NEgq2GKdhoiRidlB3HISYF9s-nYJ_PNiErm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K85rxcK9QMsBkSMTLF0tfj3LUuHK4QL3HGyGmRIA3udkytoiPM2-iz_MqqaNm_EYI3PukgPYFdwre-Rg2-ZGOtQYX6On1G52lUiBg1Oa-RaujmUbYZ8IbMmnDQTnbJ63gObNwaHynUIyBAkgsY-MRftKOlxXrHDEWRyALEq5lB2rNKrY7NCvlcZlUAAqlR3lu9EjonlQPrhhTigYdBZ0w9ZIPZQfHGDyqFDZZklqNEKn7CHkU2_vEuPqZ57H8QujOvdKvIG6frbZ9w0s8vnfdAm8V8JH9AfCojo1yZN9XSyV8qtbRuGWe-mUztih6bUQiM0ZdvkcUy3w6jVElSb_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rBQcc17ixm8lKNBUpw0rqN5UKDtQwQ7MruP2LgSd2o3EIcwx7Hgx1aOlsyP9ASTqx7_DrffVmTXW0YTaswgEPN13PmJpibVD2HuTbBVEG_152Xo4hyzvaBojKl8HJBaPfaj1rWR7SH8vKhAEIbwgJb6cSQY3WC_KbkkY1lKFVtkDLmQlRmdCDRg_A-fFgH_5yt_LMk_m0JTS9KIQSuzAKcxsK0SYVqI8tP7O2HrQIViMOb3JYbPPRQ46m-KbyPlJgpMBFTiY3srDB5p9p08VJCzBdLSbP94BpX2T5hiJMQhytkdhL7SbFZwslOcx2GNUcg7YX3ssuZQfWyR7uzG8hSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rBQcc17ixm8lKNBUpw0rqN5UKDtQwQ7MruP2LgSd2o3EIcwx7Hgx1aOlsyP9ASTqx7_DrffVmTXW0YTaswgEPN13PmJpibVD2HuTbBVEG_152Xo4hyzvaBojKl8HJBaPfaj1rWR7SH8vKhAEIbwgJb6cSQY3WC_KbkkY1lKFVtkDLmQlRmdCDRg_A-fFgH_5yt_LMk_m0JTS9KIQSuzAKcxsK0SYVqI8tP7O2HrQIViMOb3JYbPPRQ46m-KbyPlJgpMBFTiY3srDB5p9p08VJCzBdLSbP94BpX2T5hiJMQhytkdhL7SbFZwslOcx2GNUcg7YX3ssuZQfWyR7uzG8hSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=guKqCU3Bfu7OBeYze_khf9foDw3XmK-ATdBktcC2wuoz-p9GrfTSA10KP2xIjkSY84Ld1GAXYFL8tGs-NLmjCoEkuLfAMEFsYGueiGRj_j2sKB1iZQBWWXlIr_n8EwfzpUiwqJvRyU4N8ZvbFsjCsqsHV-4o07fBEl0h680Fay8G3LeGOMy7ru8Ek5ovdRsd9G-A84sbcaamigqiNnMR-rHUqLxeqp8VrcFoZoIWBVY03aOHF0IEclh1SoueqS-IkmpUz3ASErTeN24pXpmXvG7a9kfRPn4UU7FNRCr40BzgpPirPcjozpDwS8i6p__bVCdB-jvEVOqfRHR6gnwPEr_wkHuAHHY5Uyo_HqV7vjuw_pgjqonarNgvDA4qTBZ2Kib1BXbsInGKV-NgxBY0nzueRQZLZ-I5OLHNQE2cPZRfVz2mRUxlF0WxlTCgOVH9RrPmBo7vjG2f8nrOonBx79IpxKvo54StQ1YtP9saP7aEiPNYz924tFYFxjRncFZLEcQfPxJydPUK1CotWAJSAO6xBtx3f-lBJ44pRET4s_8nliSKp5GFL3fUUNUArbFf3JbQ6-is5upGYZdRnEQ2J9ygdzJqJwGLrtTjHyEEawnhph-V6TXNBA5dZxnwAmHKgFLkIsQd60BWF-fFdlieRahQCI2lb-56ChCChuUzA8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=guKqCU3Bfu7OBeYze_khf9foDw3XmK-ATdBktcC2wuoz-p9GrfTSA10KP2xIjkSY84Ld1GAXYFL8tGs-NLmjCoEkuLfAMEFsYGueiGRj_j2sKB1iZQBWWXlIr_n8EwfzpUiwqJvRyU4N8ZvbFsjCsqsHV-4o07fBEl0h680Fay8G3LeGOMy7ru8Ek5ovdRsd9G-A84sbcaamigqiNnMR-rHUqLxeqp8VrcFoZoIWBVY03aOHF0IEclh1SoueqS-IkmpUz3ASErTeN24pXpmXvG7a9kfRPn4UU7FNRCr40BzgpPirPcjozpDwS8i6p__bVCdB-jvEVOqfRHR6gnwPEr_wkHuAHHY5Uyo_HqV7vjuw_pgjqonarNgvDA4qTBZ2Kib1BXbsInGKV-NgxBY0nzueRQZLZ-I5OLHNQE2cPZRfVz2mRUxlF0WxlTCgOVH9RrPmBo7vjG2f8nrOonBx79IpxKvo54StQ1YtP9saP7aEiPNYz924tFYFxjRncFZLEcQfPxJydPUK1CotWAJSAO6xBtx3f-lBJ44pRET4s_8nliSKp5GFL3fUUNUArbFf3JbQ6-is5upGYZdRnEQ2J9ygdzJqJwGLrtTjHyEEawnhph-V6TXNBA5dZxnwAmHKgFLkIsQd60BWF-fFdlieRahQCI2lb-56ChCChuUzA8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWeuhai6qyb3ztOdsnlhpZL-VRGLdLkC-HbxneDRlzwuGy_6B1WaER1kwrLtlkJ8Gz5JmJoDZPBgdY8ROFNSpNKKrWmMn1dxn3plNltoketdr57x3Bfc9m1be3a_3Tkut0VvH4OnRtcB_9B_EWXibJsJzpZtQ8_13bS_XXNvPtbha6R9c_3cKEKV4rb2yfP889lVqtozT0B4zW5JTAZDpqZX1V1FsrJrv-eCzquJmBVVVgRS3E5y5vsSTwLdbfYc3qxw26NWI8SZQbubgfl5ojEjzlfOfOnJ8KBaieo6FRfHkFhzb-MLf5YjHsWzplLvb6vw9dEtLre7Sod6cnLq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF3hyLYJM8fDN08SD90ppmquwu3HOxMmNIroZcO6B4gGQhSkj7lLQ1KBc6ghqWnWJQQqCjxWPU-YgVUrCMWHOBDLY9xMioMry9i2MdxigAulAi8SvrHcm0lokfBgZuIojuSKT-ppoaSmWYQ3z-OHhMl-9D_U9mSY8eCFdV8QWCQB104H4JZ0kMrjnk1qa-FOMQL3Q-xMLmS_UuJYR4o15NfeoNJbb0SQiPQZjtOydm2KNBsOlWuYi1VB4hWIglyT6EkMngpYmgRxmTFed8MHJLE4IUJ_DGQcdJbf_quNpByDNr5K2lT7J86KReys2gLeFGDqP8OX5axmbfePHRBE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVLdMlapE7zhwl8FdbSVHWhhjqJhnLwFS4JRx8e09KG7UZB5vd5QxBBtVOXaBYM7-x8R8iBGu08ttGdTNseSmU8Qg1c6Ettxrc1sLWKvL_cJdShLxcv3hP31WIvls5UQS9hGiCcw1GGldc698zAMXVC8Q2jryEGdMCnRZzv2NtFzsInQC0O_hQ_bcJDyZVc-OQF-fOixGFJbODEDMdA97qJc9uW38onKQ4jNXONQ-04h2FMpfDjHM-sTWg6b5fQBvwPzJpMdhEWt5S2iJZe2wM1atNA5BUi19SFe2Z2-vGstxNYzhe_bHDpFuVYhjpNJBCTLf7vaMMQiQgmLVMhAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN1en62P1Lm7zPO8wrHmbJviZ0QW0SqTb2VYf2g0uSDR4mOwWF2MclXCHz7xEcRL3pgsxWyiiqXH1QHb2ZhhXOcAFQZkx7M2bqfGV4Pllzm5vfvlADyN7qFySjFc35-4zJQWivnR6JIIiCd_XcecNI7GknH_MrvZBXjMUwqLhZsJM08E_czjb8A9YIjiv9ynP1TpQSQQXAZV11jt6AeeuKVfGcgHwsR2o9BETeP1gQI5V5sOkLhuQpaoR-ypMt8IteTWFOvTV8J5y_kRmC8IEQqQ6B5Z6obLNbmB3NTbH0Br26JmOhYAmnX9fXb9Dlvpqaz-luuwupRRd1yIh4SM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDmRlfztw0kQ5HgGG5FZWRbNNkC0djHZ5En6udjbl1dD6g361KVaCK8rGg6BFrt-zrVRZXlUtWW6pvrq_AkSg7ujcyJGrAmMU4ZzOLuhfgmd5r779jiq6-1y3jsLCFh0WQo60OHiGbyWSMQgVHqo_fOBwpDJVzoPapojq_02xJmbCjnGtGSmZIKF3jyg4nPujqmomjgbmilFt8UpdNOq5C20JCJqHWWMs97UNCJEtWDuWIiNDS03eR3gNQeUuqR_3WjJt8Ux856BpQjOmW1xCD94C5cgX_FWakksdG8E5Qy2lr-k1PV51cRIj_g4ZQ5hw-BE71vRZzcIUvtNV7GlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoA0Sgys2pLZVCSCfFfNtpAf1_4VB5-lgK3TywzAsyENgMTnNZnZ4rFaPQbeVU7GwAp87MVy8oKPwdChAhuYmM82pWN8VgnbYI9D1JqyXhauniozG54vmj6aLnAa6zLZ4fpSF7b647a9z-mgB-N1BUgqn5IfP3pwth3hVIekPsoqcsVDa79ULhAEjD4MQc445lqAW-Y-O0oALZThI8BCl3m_P5Zu0KSWqG0Yu_kwS3S3X16JLWUAqC7r68LLEUWDQ2Py3amORqsbQpjsZ1MMV5db5zIoN8MPnOywhg1RZwFRg5-g5cmPp8osmhPCYKChRtxtVOisrN_TLoalSqcU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-ALgJcWioRL8_HdLDOa8fPmOo3fPUbz5gVj8D9yQpQZE1VHp55lshQ3Mr6N4rnc4APSoswtqlyrwcDDCwpJGTrrOlqEB1DnNDlp2qhFAHy4CkT7QPh1wekBZGcIUyitLgd_nJgxZAC3k2WXapKbRfJSdJBIxLkhZf6GWRgLwRYbhBujEktbYYUWuEihP6LdUXOaNwSksClQr59H02FqhUS4Ul3BgB-PoYYy6c5Tli6oLvNKqO5hwy4I68TW9Z6P38w4IaNXFMku9AFa6V0eXN8KRydOdKeyrFya-u-3vs4CRsq_8SOC8rxwSOyDllnTXxcF2SSYNGb4wgV5ePblrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDPWlYMI2lOoi-fPWrCwu1Mr3-titOiXpcHwEQ5uF-9fwtEUPIqHPrBWUllfIQGJ16lddl4IzyQPyqagpTpPX6icslNxnqc1XZSaCsOpj-4HhVu4J9l67b52D2hLpvCB8wLiydbZj_NthbXwsebjiKO3mzXpW-weCuiKm-OUoAS2oC4ou98ZzsaXKu_-dJ4linRXa6KGzHverb2c4xp06WCxLqL5C5En-mzwmBXUBEGYX4J0yAT5s79h2g-W323bQEw1SmYGAbOO0HX3QscUZsHHIzqVuHV09sxpeuli_MInyyWi7KnbPPrrFyGcinnPup_gvNG6oawvbPJuy0bJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNWLRGxmim6RYpoMcFuGWUITggyMEPyDKUj8Ii1d1kG8DVjoGtvwjyuG5fJhCcoHLYuFPEGT7fScXTzjsd3ufzs6lL_p-gT9xaTud_HLdoX0TlP8Ppct8F_pT5_K-df8gQV1tJ1MRW9H5pRdLmTI2O-jI6f7vksKJQwbfm3SB3eh7iZANVg3efX-LESoLorBedpeStblCLIPyk83C82RnG9Shm4kh4ntKtZq-aeFkBGJJpc0Krg9FmfaKCMMl1tZxK-xL9306HXKHCDqfABT9Qd5_BH0uw17bUwlw2QHuV1bS6RE7p4onu79O3Ft4CLtJEYsTiYNL-sS6iwi4Gbcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=LBGNBL-jMbW66wtX3kAUNKnL06hE4uoFnJ05gAAVjHJKD7ZKHObZzpcfCSFq6iAcgD-Esp4jeDeweCXE7vx16tVZr81r8leX1bHLDMnlW5s9hTZFUdPGoLLdSFyFaLQNLCW_9RVLXsLS-ftvlS6wuiL6TfXGKA9BkN5svSYiKCCmFEyetniAEFh7e8l1E1xCM59ecdeD_086-CnYPqrowp2_fxmYhl7CKF1b5UquJz-PD110FMoCFe-sldTxQCyYq2lk-e6enBPSFZdL0nU3zE1qphMYp1dTz8VfmeD0rIcCVId1R3iiIzZ0eaWOK99EQRrT8hcFmy1i2mNA9GJnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=LBGNBL-jMbW66wtX3kAUNKnL06hE4uoFnJ05gAAVjHJKD7ZKHObZzpcfCSFq6iAcgD-Esp4jeDeweCXE7vx16tVZr81r8leX1bHLDMnlW5s9hTZFUdPGoLLdSFyFaLQNLCW_9RVLXsLS-ftvlS6wuiL6TfXGKA9BkN5svSYiKCCmFEyetniAEFh7e8l1E1xCM59ecdeD_086-CnYPqrowp2_fxmYhl7CKF1b5UquJz-PD110FMoCFe-sldTxQCyYq2lk-e6enBPSFZdL0nU3zE1qphMYp1dTz8VfmeD0rIcCVId1R3iiIzZ0eaWOK99EQRrT8hcFmy1i2mNA9GJnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_ceRFb0oCEvmbAAzNK7Ve87V5_oQLkb9oGGETwWkstUdSCirpI0TUQqPeu6tTM0U4uZsGdYNMgyOfgBiD_Xkktndo7pfzJm4pFnDefKGS0UUwckJs5BTxJeLOCobr8cXtTDv-E9POIZxRfG5h51PU9OKj4uBo5Kr7Ls9-woU-mWQV4p7LvdB_fOtn2f03UaT2fgNknMMQQ9nCOvXx2vt0SGR7qowkvyXBQRnKmOYUgxCeMqm0Dyn-LFIt9yuIvFeXgozvDQlN5l6J4dAOWj12qgr6NH6B838gQ4DEfYNdHja1e60E90LMohK4bmRshJV0Jvy4OCxLe2Yfc9dGyrwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQAr1EyZTpfnXr3BCp6znvFJukSsDcGhg7CPK6eTHxR3aE2B-E23y116nUlom34rBe18uNPhaej-xrrnnwFVGCjDOJ2WyMG3eYiOs6fuV0NyPYsKyYBu53bdcc0PJSq6sp6vta6I4o_mzrR7f7wzZmNdaKv_K7UF3XqXs7dKZnbNEA6EaA19odGGRIQGolmwkFClNXalLwYtuy7YQqmFDlMd0FhSrFT9sobRt9XyCvlhPjNDd8C2z3msMCzMCmaltrkcKaTBs8TIC8s2qV9EqM560kZpn-1vL6ADuoPNaUAZe7UMYI07cfakvLzal3MYr6eN-WbNB18oAS07tkXuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMTAtftvf0Z8oxvE4vWLnxG8de6qsfDVTAvnYViZCS7xiivXFa0JaeiIPCPIzSwOC0WZtTrPp4K7iqGneMWjfNdci9gJsbmAuLuwWargzolKOLze2dclhsw0o4mLF6z73ZEZhbQDP_mXei61swU85zlcZResxCOGDuBn4i9rmP2zjx_RZDLodV-udFkrMprzWxF0mWWmRX3Hbdh9KBHRXlAGxtBuIbuwwVd7CaZnwqinbVwqROe5HhAf2R7OvunlltThtcBIQ2SDj47t3PVdGfy0BVcPxZ5a9DtD3Nz0Hp6aI8Whzm1E0-utA7bw9OO-6-280E8sM04DDbDLOjT-CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyuOiwtW1-XLpG_t7VkHY8p_Boo5bexT_DqE2t52sWcF4rK9ik-LhePNJyLU1aBo7MIcu79TILxkEspRs43H2PG5NjQn_2LGC0Q0LKOn1XY9gNh4ofof-rt_0a5FZvXOJsQcwa5598ROBMBY53T7Uq5V6Q5YKB7jpwvPs8XvT-AK1Gs67xRuEQqXtpxVbxfKSDAHQ_jkdt_JILO-In_yeonWvlBWcPAZdicvl-2q2vXqS150a0RIVgP8CoD_7zXc9JDfN-rDgyWTcDO0xx3J19ECwwx-Ei_sgZcWH4I9xvnVeznBRVz1nW1MLYYIWgszoqQowMCmxFKWWbq5WHYvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAZiTYQEyGc8dMHxD6GRIWQR8LbpRu1-4YeB7gU-Xhc977yOqDYoKLfw05yJBN-NcNIKkj6watMaN9aO_MUsKaoNmGJ6io2WShhI-k9lzf7u_lbCsrzTYxf9QC1Axfyopx3cu81bphKzvEqUfTP06bUy_77gTw8FcyQpIz0yYYFoUhPDHMbnsyzSBdaqx3bF3_m2-yjteWQ618mQSQc49Cd6RiOuqeh9Kuj0J1Ozd3QhNG9TktTicvys4P7twsXtDbUVf4-C803qRCR_F9Tnv2DhLLNy8nv2RercTLRYzigqlFMp8NChGX9OqcGss-AHJ2lrjO9XkFzvxqGoZ1PJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcCQfWLEf1s8ghdhQheljKFwAoNwomOGMxwD6Cwcv1TAubP12zoX4CkPI365IeFDAYLqlNiCZqhG0YurG04hok5dOmcvbKAzskX2wINMVU4-zteUCVDrXrgTjO5-TseKl7ynMfG9cnAo8kBAipdD21AINHfAlQHYHTq4JlldiRPFHyQTtkyMt1pDNz8hBLXWBFdgK9r-65GKENcNNAsmvr7acYqtPjd71XjxQWimp6Hi0Y4L_vH1bWnrfYtSt5FqgyfaQkHU58Kg_jOA3if41eV-7VUSe6NnEaKwG0xRxuFLmSLjwuzL3cUSkhd6G4KUyI2eKPlNMtll7XC2s0oF_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbVm4LkrO00oOicZ_-n4iuvWkqDifuV6yDhbqRaI_iWY0Utb26MKtwbS2-5wbpDhJ6SdJ46YbflvrCIdmyzWhK_IyCn1selfUDRO5jHm0jUjchsbNFDZAo08sPE1qYWvSt9ZRb7E_ItgDtfFqbFR9aFeZLm1mr-q7lqEQtVlUhu1Qzn2puPvLfG56KRZ8yUqv1YgQqIR669EXBf1TL5BgvhagDhszXBcc6-Z4L0GuupeZ_zE-Oe0YhEOTOxbP5e-ugbKh4rdr3Rei1Lm-pUkn7t8oqDvYevPfi3EXnIa8SQdGC_rqFF_8z50td2Sd-yuOT-0MJEDbKmywb0CVlbK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asnkVP1OVarNJkLkAJF_ZE-pPtkMDlqVh5cXsFeLWv0IQ9ZFwg4TpCJ2GjImDXB1R-CJHM0XRnCt8gTKCr8rb1iHvoCGU-CUH-42sRqq-1fNd6-c0V7ytBTixP079fx5o02CM1g7egUMkef5jFh8A05iNWQjsWrVMhwuNsd6yBnL3T65pzUrHvj_JnZOWF8tNxpU4niCw2fnDau9tyQf2V94IjHcHQy63LuL8vCuxiv22Hp0KI4CKnyPlMKYy3N0fnI053EqZRtNcnnXxvmsAJKu9h5UjgoXNgbtzj-PI7y4ALlAqLnKKBwQCE5gal2PFxZe6gXD3SQuaK56WoAO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=B2sM-iezGigdrC7eUTPkBQTMGKizFo5y_iT43CUZ4GvTGcmqQ96rvOKgBRsw_jfVuU04bQ9ZCKoehzJnWhnyiaAehfPpmJok7oZBpqgaNF3WenkBIAIwxFTaKkSJHHWTyiVGLS_TxTXtRRv8nP0oIlsWqwnqPZC2_jMp975yXkfqIsA_-Vl_Hd3Mrc8FWxNGJP-Zx719cPReV36pJe2sA0u7gZO9IwE0EEVNIAET8qP49mRNWMxONDgRkp5yXipMKvg3UTFjUzfgEHoIssbyFSV7e_sUo32ATiWaTCeWtQcScMbDjzOxOzed_Jsp10-isLojkulppbKcUxaS7HuwTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=B2sM-iezGigdrC7eUTPkBQTMGKizFo5y_iT43CUZ4GvTGcmqQ96rvOKgBRsw_jfVuU04bQ9ZCKoehzJnWhnyiaAehfPpmJok7oZBpqgaNF3WenkBIAIwxFTaKkSJHHWTyiVGLS_TxTXtRRv8nP0oIlsWqwnqPZC2_jMp975yXkfqIsA_-Vl_Hd3Mrc8FWxNGJP-Zx719cPReV36pJe2sA0u7gZO9IwE0EEVNIAET8qP49mRNWMxONDgRkp5yXipMKvg3UTFjUzfgEHoIssbyFSV7e_sUo32ATiWaTCeWtQcScMbDjzOxOzed_Jsp10-isLojkulppbKcUxaS7HuwTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3KsqvLMy-5h0qtHBivSbvMCjmvptfwmhl10C7M3y2WgaWDtXgQf_zgSrzjaAsD1J_1PGUbr8-CEzLFaCy6gu0AqT_EMvUkcY9Tm_x7AgiFMxgqmWwzHdbg5HZVgzTYcqCitVQ1CpfSBuVSTA80PK5lZY_sUV4Wplvrlq6rWbADDayW5OOgvHJdYU9RFkBT6_GVbu55yJVK92R_PZgHJ_hQ_1DEjHPQgjWB9h3t3R9S621iAj1sU8igbAdOjpoxAd1NlpD-rpxwpATF7aE4l-4HtldYpkVU7QiPPEhw_cochmZdqBChVHkNPkzZNi-Yo9GugayZhhdbXPXMUN9TVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt32Kpn2H3IBhPcdKNFa84VNo6rf5DMXJcJQ9c7jMEGEChi1m652SM9M8pPRAOm5yXyqC13H-k8vRGHDAV18upCXL282o1dgOMs_muTwY_4GFzfcByRjOFlZx2tPEUEPrnuYJQDfl8q8pnOxbns6c2vZ3YdBVFiKDg1dRMweSfeY6F019r2l4SeYn4aXUb_M156iYlrgv984ajtYIyWzyKIao_UGU4Ty4BFzTPYi6riEvrp0sotZqyI368BhFajL2bXi4RtJeUPi4g_UAcVX3WV0mPxvDDpf0ErRHZS3dz9TY0NDEz47F8Bd0SMMvbU7lxTnnvMTRBDDwYqdYPqCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVhn7UH6Hb9SaEfmwdxreNLNOBM5NkQlCQr4Dwt5OJvId4dvayAHiXL-9vbJUev7fJQoRi5--HD5z2pASGw9foxJkqAmL2kUUybcKI0e1d4dD7NGmvqnSxCyV2BTAPMmEJ8y_s61wI35m4ROwrqFRokwvIk2fnj0E6KBWxgMvz3y0Fico4xSdGiFiFqcUbJKM5X8SjfJ77Y24GOwKUXL8dBH3fXDaM9SzGoVYFJzD6Lsl8WTNsRb7wnFH1bpWqdJLxeb0COGXoSLByzkKvyerEtJ-XThAaZV44xO2vTXUQnrTii2LdKMQpJMM-7VMlJ7E1b4WjnDuMjWZKO8MEKegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfxJw-FLnSw4KHkzTOagi4BemIqEU9zpvXVvMZtvVg_fjQ-2xw8VK5iQ3mQ4Cwv-b75iZ8zVP9uNKALK6XT-BgQegWFwYyAJWv_n_DC6-WcRolDKl9HDDCfEQzNeY8mQPgcLX_GCMGWniVl31G6FCKhgj1TqCZzQgEgP5-h699Iqi3VP20mGTu1RD-D8Y8BC_-bEUZOaOVirEbIOUov7dA6NwV5RTVEh3336aQ3yvrcYvMD1h6vYrwgH6n5oeeNUHYsZEvw8r_eF6kgbWMM0Pa5AdphOxrLV0xgW-TI-n2wTuWs9PHp54wobrxohM2lbC0ObzPy8n5bAAZ56ev6zxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7iQVbef6WCO1j5zeJy05jGTFjLOWxZGO0Or9Mlpcm69grU56pPFALe6Merr-ocmwuvRh9LJl5EGrZRpDWo5w2FTejO05VhAeUhYks0d419UrGey3qjxITCGC8SufUvft_fPeVvOF5OtV5kC4dPtHPWe_ObZP8FACtwTdB1wEu1vxFbtAuIy7IlNs8QSKn20Xx8zMBMdb6QxhAXKOJatiyTYWPvxvoFxw-Np6NOfhShw71capIZQOV0kma-gBkuHGpj7Kkb3ebZ1L8Bfn5R-KkF9AapuDlfNwFwT4qra_33AJThJeRtEuH95VIGNjma5GhUWJgxnb7pR00RvYmIuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxRY1nHg1-oUgXjyMIGHft99oCq3v3VrJ60ytC1xGMoOYssgHPkJPv_K25T9q6cWljsuTWJWrUBW04bozrxBpfGInSQIJt70bZZPP3OU4iTkDqGfVW0ZsixF5boy1fdjI_9ODurbAp9yziPnsKdsh9fN1afcV4m8lpEAbLZ7m9axE0z7K7e7Zlm8mFhLJtSM-_1R027gsiJkcurnY_HuiK0GQzaPzmPxc5O3w4Jxrmo8KdqBl13w0LDf_K7v4aMMAl9aFBM-UqjWMMq5LOzOFBRABcN66biRyDfFXpk3W-WWmko_7Y61WhLOfA16-KFQ8cc2wXq91r29XZ-X6QxBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktn9eLQZuUEIMfGi7vOWEzUKFeLfEp3pPU2LcpiohuAlmRUFQAqjaYdhP_V-Vc5wQIThSnlxByOwpQEx6Alr7y0ve692nUa6_9RWSEKc1wrwBB0SDf6sGVyT9k11djCHfz1UDQxtvJuSlwZVaTRHFQaVzaKxyPybXB5IR6BIgr4tXKbrRJSD0DKqXKfOCtgIvrKXtOuEelnPHiY3IOnYet841kUhRYA0V7OMTBObpwLyCKnxMAfcxJq1yEYusjdCjs85dADP28PuLhNnet0v6ee70xuiLKzrFmVk92Sjlvvxu2M9m-v0zL_Tf6PesPJtHLiM0R2xFbuTP3voRxLFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd3j9C0y6WXIZJv3O61gUFLj7NgxIR0vSd4P7_RB1I2AKiJCF3QhYrocCCM9fyCLy0Goxh6pqPMjz2Qpkw_c20W62laXyS5oBHLW_GUwSQ_hhJn1g_LrI3TDg9ee9QCTinUzFTPZLbagiFxnXEf4Ota4pYXC6dpIwoKd75T52qm3fD6dY2WkGAyOqN_1uX5DzVDI0mzU-WE7kApuUq2OWEPZYqfqvu5Q3ZBIzF6y3wim7HnLsZD0lFfyx5_z1Kg7T7XgzTyMuEJ0sHrXPJ-S9rwaOT3evmTIEwdHQbNx61Qnnuu_psh0RpQrF2lJD89EKyiQv3jC52EA3ICqYpPXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در تروث سوشال:
«
ایران ۴۷ سال است که با ایالات متحده و بقیه جهان بازی می‌کند؛ فقط وقت‌کشی، وقت‌کشی، وقت‌کشی!
و در نهایت وقتی به “گنج” رسید که باراک حسین اوباما رئیس‌جمهور شد.
او نه تنها با آنها خوب بود، بلکه فوق‌العاده با آنها رفتار کرد؛ عملاً به سمت ایران رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار پول، و همچنین ۱.۷ میلیارد دلار پول نقد سبز، با هواپیما به تهران فرستاده شد و مثل هدیه‌ای آماده تقدیم آنها شد. تمام بانک‌های واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند!
آن‌قدر پول زیاد بود که وقتی رسید، اراذل و اوباش ایرانی اصلاً نمی‌دانستند با آن چه کار کنند. آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید.
این پول‌ها داخل چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها باورشان نمی‌شد چنین شانسی آورده‌اند. آنها بالاخره بزرگ‌ترین ساده‌لوح ممکن را پیدا کردند؛ در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی.
او برای رهبری کشور ما یک فاجعه بود، البته نه به بدی جو خواب‌آلود بایدن!
ایرانی‌ها ۴۷ سال است که ما را معطل نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً هم ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند، و به کشوری که حالا دوباره عظمتش را به دست آورده می‌خندیدند.
اما دیگر نخواهند خندید!
»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMOOuxyAxK30HIbcTNdUn5gctYpM8J4Ox987qrIIPQ9ParS7yqpneunsWPFCZiHG4mYi2YMxyu5HNtutZVZaV3d3wA5I6Imq225yUb71onqU4_j-6PAQQd8uV7HrKZoanVObFfQP2tQZ0G7t0sTtakg2QjDFAz4jKgS_8T-bECQJB1DdnldYEnIz3jwyusVqKg8wn_X8RqXn8dQQxLQLro9ZLd9kXbSlZIg3CAJ5kpXQjREpoJERgXtFcHAXWV8N8A7ZgUAT-hoLW7CX_ZyCQ4e19XH3ScsSuAXfZ9GdFPMZTjRRmYHSLMgTzYk0vGz_a7JuLZk-MBzDQZ4gTKkiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه چرا کمونیست‌های ایتالیایی نخست وزیر ایتالیا  - الدو مورو - رو در می ۱۹۷۹ کشتن!
چون گفته بود : «باید قدرت رو با چپ‌ها تقسیم کرد!  اونها هم ایتالیایی هستند! نباید مانع شد که وارد دولت بشن!  دولت ائتلافی ایجاد کنیم اونها هم باشن!»  کشتنش!
کمونیست‌های افراطی کشتنش و
گفتن : برنامه داشت تا ما کمونیست‌ها
رو از مسیر اصلی که مبارزه بی‌امان
با لیبرالیسم و سرمایه‌‌‌‌‌‌داری است منحرف کنه و ما رو به فساد بکشونه! در حالی که وظیفه  ما «انقلاب کمونیستی» است !
و نه سازش و شراکت با سرمایه‌دارها!
و‌ همین چپ‌های افراطی (در ایتالیا، آلمان و فرانسه)  که به خاطر مبارزه با سرمایه‌ داری به کشور خودشون رحم نمیکردن و دست به بمب گذاری و قتل و.. میزدن، بزرگ‌ترین حامیان فلسطین شدند (چون اسرائیل طرف آمریکا بود)
چپ‌های افراطی آلمان حتی می‌رفتند اردوگاه‌های فلسطینی
کار با اسلحه و مبارزه رو یاد بگیرن!
کاری که چپ‌های ایرانی هم انجام می‌دادند!
خلاصه ریشه این داستان‌ها و… خیلی طولانیه!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=r2rEu3kxCXW2Q7nX9oQueVEQZTKArVqzwI9ayO7lbp0jD9kvGjlpIdqaN4nVEfmS1IIs1rEVCwdMdWx1D3pJQnlv7d1FpX6vNWZGlBcO_ttw7xBWJZSrdJ75tfFVNEBBuoQL63DJo62d477-smWoL2Ee3uXkQ8_tJK_CidJaZesqOZ-TGqdnUb4nwQbQZUgSuxVM8GOsZBI90FhoQTNp2-OPTpZC_PJwaCKWXwP1YmgyyPYvZldaJb6Txxr7iGNb1lhRRM9YwErwmhjsafxfxrVvi-2h0VKOgGXHVcB_m1vhrkA5pVZptO1BnsY-oRwo31uutMY4Ii-f-WUqbhhf2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=r2rEu3kxCXW2Q7nX9oQueVEQZTKArVqzwI9ayO7lbp0jD9kvGjlpIdqaN4nVEfmS1IIs1rEVCwdMdWx1D3pJQnlv7d1FpX6vNWZGlBcO_ttw7xBWJZSrdJ75tfFVNEBBuoQL63DJo62d477-smWoL2Ee3uXkQ8_tJK_CidJaZesqOZ-TGqdnUb4nwQbQZUgSuxVM8GOsZBI90FhoQTNp2-OPTpZC_PJwaCKWXwP1YmgyyPYvZldaJb6Txxr7iGNb1lhRRM9YwErwmhjsafxfxrVvi-2h0VKOgGXHVcB_m1vhrkA5pVZptO1BnsY-oRwo31uutMY4Ii-f-WUqbhhf2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به مارکو روبیو در وزارت خارجه ایتالیا
سند و شجره نامه خانوادگی‌اش اهدا شد.
خانواده مادری او ایتالیایی است
(از منطقه پیه‌مونته - تورین)
و خانواده پدری او از اسپانیاست (سویل)
او کوبایی است.
در این مراسم گفت : از طریق یک اپلیکیشن ایتالیایی تمرین میکردم. همه رو متوجه میشم! (به خاطر اینکه زبان‌ خودش اسپانیایی است، متوجه میشه
و نه فقط ا‌پلیکیشن و تمرین ایتالیایی)
هر چی وزیر خارجه (ایتالیا ) میگه متوجه میشم.
اصلا نیازی به هدفون و ترجمه نیست.
دفعه بعد که اومدم ایتالیا، سعی میکنم که بتونم
به ایتالیایی هم پاسخ بدم و صحبت کنم.
باید اپلیکیشن زبانم رو هم تمدید کنم.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dS74_Q95cxw3guwzV393JDU7C0J_BdYWrbm16x3XX67dEelomyTxzr9Vvh42qAP_sbEcViO2MhZqgLVlZy14rHSLjZ_dW1qTfSVSf2QpUs84m8D4qQ7D0IRoeA63_6EYqI5pprVIHrX2LaFmzcJC1oSgzMPEhWFWbrxjIViF7MMZxjb6dyxbtU7I1C6133QIDMIJ7jrALXcyw0tiqBMpczFT-G8Th_d0XFf13hWAxzoX27GQ3m-6M5ES8i2uUF-w3PM3euaFFtsvquoX3ayXPR5vrBWcjgEDcpPvfLH4FdYKrhaehXYPermkP99gL9hAbPbwOzg8nDIqFUNrdLNr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u__GXonkzPKI49wJB9cGxpSnH5HbMgp_034gBIDUu7bj1JCF55Nztsd3gU3LJuC6jMWFpUPahoE6ik4gmjJhQ6XOWbVDyxTCE_f7brtlkfPkgUWqyoP5M_gCpNwNJc4J1khOzlfueZTnbVYdCiPUwqvi3a5zHQ3q_Prmr8z9zUTwsMK8m91-UU-JxejwRL6fdzFPhKbe0GpiIgHh6CYMFjApnxF_frDRADJnoiZr_Si4daseBtKuHi3LG_hefzdb3nwXHUxtRf1roHVUnapT49jrGbaLKD83fRy4ts2Mw9wl4lyS3I1NU5Tc76yo0YLLCUyfzzsXvfcb5taVynDz1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=YOC0Zh2-WCieDF93rmAaIJ0aslO-kF1esroZm45U7dbmscHvnqJNzCvpt6xG3JjdGshdcRLp_AXpgrpsA2pu-ntQ9fcZn5tM1v-e4NH30OgohVMXKeGmK5KoRSXuVO4PZwU-S4wSia8JSeXOm_W9QyWSAxTIYbXiihDBeCIR8zdIGJOhiXI1EOH1YrlbkVtG84ULNUyDWbVGnws4Gzno-RKVBktxHzLjd3nPqLQsPvq9g7w9_SEd2ZwgBFjDuD6NR4L7J2x4GljBdxjy4N52pCXc1l6Tsn8cjV6F4UzPXmGtK5IJkVXqLkYmNMdOSx6J83HW_zuCfTQE6mzZYj-M_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=YOC0Zh2-WCieDF93rmAaIJ0aslO-kF1esroZm45U7dbmscHvnqJNzCvpt6xG3JjdGshdcRLp_AXpgrpsA2pu-ntQ9fcZn5tM1v-e4NH30OgohVMXKeGmK5KoRSXuVO4PZwU-S4wSia8JSeXOm_W9QyWSAxTIYbXiihDBeCIR8zdIGJOhiXI1EOH1YrlbkVtG84ULNUyDWbVGnws4Gzno-RKVBktxHzLjd3nPqLQsPvq9g7w9_SEd2ZwgBFjDuD6NR4L7J2x4GljBdxjy4N52pCXc1l6Tsn8cjV6F4UzPXmGtK5IJkVXqLkYmNMdOSx6J83HW_zuCfTQE6mzZYj-M_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ituRTshmXjh7ag2_CG1x8h24CBlK9hjop8QQtFQ4wk26W_3jBHLTLbuwkcHi-X61D4U-HTPL_UILWafowmj2uM_D5Fx47XexdOwFJ26b75Y2GcLzTibZVve4PsufZ5zR-CsJfb5oFnNM3tc-FTEfCwnmwYe4Yr778zfUUDMKh_KummE7yC4fRD4Uhdea-ok75VzxlH_Hv4obWwlDdE8p8h_yLyHe5uh04z-USpH6mS3uuyw61-0GDuvEMQ0K5It4s4rpjQ4ZdEQRiAMMABWCQ8zuE1ql7zc8infdBs7i3HFwZ0901St0yU6QMGIL565Mp6_03rFOeLmZRx_rUhd0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbMinHr6KofTpzn41S-_YaF06F23OV163cbRvFkY8B60IHoO5hK_3xyD4SnYrNdc8Pj2SCBw-oLqMg_1uUazuN9mLSQGCN0UHHoinzJ_ZKHfFvbw9natmMdu1uW3bAHzn7xMyarwc2-4eWfo-WDcQxvRN-9LRzP1aCKjIo3FGU_WyxkFPMes9qK72UdjWH7oPK-rNKi3wZwRjOI_Tqu_3NNMQWuSnfw4l5RR3Cyf6ChOCNECJ-pEzXAGuD1reICDm2dTpRyiPP059_cx25B-olQ3lYIl2vVl35begTidPo0gVheLlqEBCBBaOeBcn5G0HGQdiFvx5aMnetLSMSHvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ سال پیش در ۱۹۳۶و در آستانه برگزاری بازی‌های المپیک برلین در آلمان نازی دستورهای خاصی صادر شد.
مثلا گفتن که دامن زنان در این مدت
می‌تونه ۵ سانتیمتر کوتاه‌تر باشه،
گفتن یهود ستیزی باید کاملا متوقف بشه
که وقتی خارجی‌ها و خبرنگارها میان،
بهشون بگیم این حرف‌ها، فقط تبلیغات
دروغین خارجی علیه آلمانه و واقعیت نداره.
یا مثلا دستور دادن، بخش زیادی از نظامی‌ها و پلیس،
با لباس مردم عادی توی خیابون باشن تا جو پلیسی و نظامی به نظر نیاد و عادی باشه و نشون بدیم آلمان نازی اصلا با تبلیغاتی که بیرون آلمان میگن واقعیت نداره.
حالا توی جمهوری اسلامی این چند روز
زنان بی‌حجاب رو ویترین کردن! و طوری وانمود میکنن انگار ما اینها و سوابق شون و دستهای خو‌نین‌شون
رو نمی‌شناسیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjOLH3K6PBR5E0WNVhpv3aVKIdZn4F_qDzh-SdpB1qmFEloHGEms2Vq4WCCE2yggk-H86_JEjOj9m9Kln6fRZYsoUaFumJZeoCy7vR_FvplhgahM2cPCjxz4xPRFqZo9lqpO1xD_9UDqohqKvAD128QJDWhT68AepVKeGgYgr-yGzMpa5CG7SRWLGIHPGWOZ-niHpmEJuQ3Lcr-I0BXjORJFWnR6pVSyCQykEGlowCej36Xxit2zjj16ppPZjxeFJT3qFl_Wd76gRKZUS7juBcvsFU54kGeBjHsGQ3Y8aDlxd0VWP44tOidiJ9unpWgGEaYjDI-YoJJpR8vQw1EBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOYRD0VhwCDEeGFjnF6Nmk_QRQ3xDup1Roe8MVD2E75Z6FS-35-hynDsGZKUnbKGhjGODQG2sjT3BlXyUd0zQbjD0fuN-Oat6khV-qcd-IqdbsuuAZRFzT3mW_jZfX4Gp-JJ687e1udfojkbokkoXAqX4_BJch2-Gz6kYcxs8itB5Nqzy4WpYsQejQH8Ti4YJPUJWUiAI01UmfOVnFDC5tmV0IcWXE8cyfFtRyrYL85zVPPHTZ6q31L8-qCgT9MZ6kVXp6kFnyQ1yi5wM4WcU8mHSd1TwjaVEczeUiKjHgFsejThLS4RIk3ek2-MQ1aKQ9DodvXpGDIX947eQzUipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTU3_5-gydLJAdhnAHk4SBZEknKkHGUM48qjZdKxk0dSHuA8EuISTLb9nskOIK9OicvKFamGFqkHqVUTKeZ4xiNCpwIHpwqVIEMIcqKNjlg0grOrbqqMkaTx4c_Uzes1O-o57Q-vtf-K5w21e1zUOdlzMA_zd5i6wkNwcV7QshRTnGMnmtH0J-i0FaFcGiQf8nQdFRs-VBI4vySYAAsHPH3FGb9obe_BX8Xu0_A2URCncwi9zUQemC-4xcSshJ8gszVgDQSbm3F3FhszZXJydbGSH8fFEw49XeXy4-0dHvkCnha5iid5yGMMOT2heiyZJz_0bfRHeuXbgnGiXINwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSAfED0ZIdWpkvSFJAufkAws6ud3bxJksJFnisctDj0zA9A9ZyhDOxlrOY3xnRvfkH29fve14bcfxydDnBbkYYj3KgKPbTQOzd5cwMkFJl9zWWQWygMc4FpZCFG3SqRvQNQlOnTdkGZF65Hk9hzBGyXjKp50QdxQzydprte7imudp0vzJmf-_AL_qkRLjd7vyQVv7cYDQLMR2OwVfrKg5cbEER9V0kvorRYcnnOyuF4YssaADB9Jk42STV0j0F4EKuIOcgeuwXZ-THUyASMYsp31oV6cVs4Cp_nnqIGSOQO6WSUAod2DifdeL_KCFDePn1ZKweN_HwbRrAc7Mz9KoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت «مبعوث» شده :))
این هندونه رو  این چند هفته حاکمان
جمهوری اسلامی زیر بغل عمله‌هاشون میگذارن!
که منظورشون چیه؟ مبعوث/ برگزیده شده برای مبارزه با آمریکا و اسرائیل!
«قوم برگزیده» لقب معروف و شاخص قوم یهوده! برگزیدگی هم از سوی خدا بوده!
اینو فقط تورات میگه؟
نه! قرآن هم اشاره داره بهش:
سوره بقره، آیه ۴۷:
يَا بَنِي إِسْرَائِيلَ اذْكُرُوا نِعْمَتِيَ الَّتِي أَنْعَمْتُ عَلَيْكُمْ  وَأَنِّي فَضَّلْتُكُمْ عَلَى الْعَالَمِينَ
«ای بنی‌اسرائیل، نعمت مرا که به شما عطا کردم به یاد آورید، و اینکه شما را بر جهانیان برتری دادم.»  بخش بزرگی از کینه مسلمانان به یهودیان از  شدت «حسادت» میاد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0IdtQc1pIijX4G_O_4vY_guBEX8neC_rhOfgYzYHlwH-I45f0_GiJearn3FzdYmopZQDkOF2cON3nkiX7cw4uMPjSeet1os5o-do1cwfytmltDHY5hfFLco2LpZrzC5uCI5oLZpJFZG-fl_D8WzehVuvDcQOHupKqSVX3V5SqKUXqWUOfoykL81iuRS1MBXagmoqv2ivgH1ubzx3yihKZbVdKVmuh42XtTw1aFIzhmWP2XdKsMkFGTOUpoO08X-tGAPe14Nxf6wbEyeddousoqVE-7AIUhj3mIsChMKGKUQsvL-tJ62WvFd50KGrt63VGxVG3gws3galsPabNVoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط واسه اینکه
روزنه‌ای متفاوت داشته باشید :
در قرآن بیش از ۴۰ بار واژه «اسرائیل» ذکر شده! اما یکبار هم اسم فلسطین نیومده! حتی به روایت صریح قرآن (یعنی
آیه ۲۱ سوره مائده
)
موسی که به‌ دستور خدا رفته بود قوم بنی‌اسرائیل رو از مصر خارج کرده بود و آورده بود تا «سرزمین وعده داده شده» (فلسطین) رو بهشون بده، میگه : « ای قوم من! وارد سرزمین مقدسی شوید که خدا برای شما مقرر کرده است، و به عقب بازنگردید، که زیانکار خواهید شد.» !
يَا قَوْمِ ادْخُلُوا الْأَرْضَ الْمُقَدَّسَةَ الَّتِي كَتَبَ اللَّهُ لَكُمْ وَلَا تَرْتَدُّوا عَلَىٰ أَدْبَارِكُمْ فَتَنقَلِبُوا خَاسِرِينَ
بله! پیامبر خدا، موسی، به روایت صریح قرآن ، به قوم یهود گفته وارد این سرزمین «
مقرر شده
» «
از سوی خدا
» شوید
و خارج هم نشوید
!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkdDSJEvoJ0lzR7yqIfRiyw2pBXgeR9A2ZPjJhXokgla-ACemnOQmy3m3tvlChAeuVgzoBfi0RbXjjBbYJvxqfSp27KlLuSpKGHqRp06fSX4CfgJnOWrcOWAA_4lnz8NRXc_3uBe18GDXO_f2x1ddvDoAR_F0Qy7PEth-9NEOUE0g3auDf6JOUmd7ralxNxV-CDCk-iyLdNF1TjOq-U3tgz_wtcxW20TSTQAz8V5OLTsmtCqm5i6snRKvVI2aUrpRMA7uJxbFfwwChYl2pnGFx1mYBqnfIQytkxaScGq-aqtBxrmGV5EowcNEsyG0a9FoMfOfiEHcQZW8pWcgWClgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OftapvfBefuLiP1tIp79k2mjJ7lUiR1agUpsv_HUKDE0-fNb-WqqvUcAfMwt1IyVB6jsbzKkkzeJ1GPoXtvm0iGLWqaA05YDUXbXSSo9lIJlkb7tdyMGL5UB8sr9fYxuwjkg0Re7_2xObNOz_0Ax4aDWX8FrP3ag3b-MoUQLj_xvIGlXdRhsuFe4S9OZQyNIi2pTSMliOlvAd9vnIeLsHOp2D-bawzRHy_fD33bxdH1-9vZaDoRK7uHhMwcmzFf7zQG-1Kd04Cfulkm-GGXGqGG0cYgRfh51y80HQT_zg6Mi25jI5R_r3C7aaMRQ7vMWIrU92QMW1qOWcIoEgZ-E2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXhmwe4NekKX19H0JZBZJuPFYTo6IeQ8SFXqDpiy-A5PfmbVmk_JyToy86xnIcXyoFaXQQqpZC69RWlKgwVwgaHUkFZJKJ3n7gqnBcXOOMAVGtjLV0QznyxygCCX7MQ8lTt0pgn62BkzPpChnBzv6idmgmxhSFydZQjHRgH4eKsQjP7LfjFSz7VkIcLZgFmuWYCKjbCK-OPDpU6EYIdj9wDMWr6GnlhS7oXDMaaNRZOunOHkNWfOM6H2d4NLquIyqfXq4hxfExzYG9427mj4zL9_l1lwYLkgfdYL3HV2gm7XG4OtU_UUXWP3mdcm8VG6P3IgnBoZ2BLelYD6AVRtcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_0G0cpaiWuaIKHEHAlnh_J18sIxaxLKI6UgwPLEAkO7ogHC2A-f63OBMRRX1qisHfLhZH0Abzcff0ykj5sV1J7WYvj1YVQ9Lrm4FK4r0SJCg4FHrw58QSEVbrRuVz1PscWvY2aof2gS-1In2p95tU8UVUUY4XAKjvjsLl5kJVGFq37iU0X2GYi1JZsH-kDxJnk-dfXOJSj7jj1rIINr4rXiekyyY7eZZRzu7DsFnuuQzkVSVTuFezfcrkCKkVkZ0Tcu-lb3OnEIitiIHdBjYx5-RYO9I44SQJu83ptuA588xQv1XmNMQc9jD5tlgxHXr9JZAOsm8LL8T_YBv0OwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyrLVn-sVTRnN5NxOC7Wo1vf85x0H_fK9bSiFzbkbN3ECoBhgpH-U-lEppnNe5xF9b7nL55wxt6HTfkoNEDvqIncR1Z18kG5hNh_VbuuB7q3Vg48gadlGI0BpDrCqB-qAHHaLMWrTBP5Fzvagqt3YtaOHKti24OyEGVx7H_zvK7HdIyb7weMq8ZDyH9MW8JpjWmDBMQgf6xW_gf3FpjWJ3G8kq6BHlLik4WffSnImFMEd-faI5xGLpnN_U9QPFdpaj1GJAOFVkg4_tt7_-St0_J7p5A4TYKvDOLlJ0JN_kPPtPwT120UQTqXyNQVulFpRyuN6LBL4yRUBbJmpBpkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlZvyAq1BEIHUghmcCVSIqfNO4due6BlEge_HArD9BREERcjl8bMGJR-B5a9-FwNjdM7n_TfW5jW3KUUrMYbCmUXPiOUtz6RkapZW-t761bgUc7bVxxco0PKo8yRM6fQH93IOprPw9Hvu2wWUniRQlKaRgMX6pAOSDj52Rdqmn3f3jGdhRajROTLLUxfHAB-QsUNlbXDM9e6OJht7L1VM74irw2au3KcnyeWvL05nTGmAtiYzTRQYC3sOHQbXqP7fzf3BsfCYhYXLhz3BQ7TN76bPhAzS2yQUZG8SGY-w4kYtcfGqS4gchIqrBt3zoCnQAaebsY0uCl4mYIG92H86w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=PCknKummOWryzG_0yrKjMewTRzD6TwJk_4RiUkyaQbE0knzo3jjwE_V9lVvsl8cXsQ7t5xnI7BLVzZtOsRnS_xfxixTrQSvolgpdVLVfoooWoox1JNv9N14rp5pKda7AK-k1GMDq1Jc4h5N-o7GWdfD_WuSDsWCucZMv7kPx40sKuKkZCW9_6zY3PTgaRlTRm_tD-ygSAyZ9h6NLsQW339ocD09xp0GdKTVHdK__N9n2nGmqjcbqYbi34LsdUO6TaYyuJ60mi-05-wQmVLZaX91UELXtL2guVzOKO59MtB2bKp2to9MupRYcgQMVUTQJi7yM7hhHcodwBUU5CzM-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=PCknKummOWryzG_0yrKjMewTRzD6TwJk_4RiUkyaQbE0knzo3jjwE_V9lVvsl8cXsQ7t5xnI7BLVzZtOsRnS_xfxixTrQSvolgpdVLVfoooWoox1JNv9N14rp5pKda7AK-k1GMDq1Jc4h5N-o7GWdfD_WuSDsWCucZMv7kPx40sKuKkZCW9_6zY3PTgaRlTRm_tD-ygSAyZ9h6NLsQW339ocD09xp0GdKTVHdK__N9n2nGmqjcbqYbi34LsdUO6TaYyuJ60mi-05-wQmVLZaX91UELXtL2guVzOKO59MtB2bKp2to9MupRYcgQMVUTQJi7yM7hhHcodwBUU5CzM-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،
یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت
از امارات در این کشور مستقر کرد
(همراه با خلبانان مصری).
رئیس جمهور مصر گفت :
«هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر قرار می‌دهد.
ما از امنیت و ثبات امارات حمایت می‌کنیم و تجاوزات ایران را رد می‌کنیم.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_5zNGf4cfUFciOWxCPTPnsvDrdfHuJ4JNdwl1rvSzxUXNO8fbnbzZQS9sZVrVTGTq0oLe6hmGCYtVQr7Ie_pYofrxB0sW7KLt9kDNOiFEG4WTUFzWWr3dIfMG4-4tblkYt0Wwm_iZ3COUBWKEUDFKGPBrvrVKRV7lmyq2mGyArp6OXTv5LrrCG_5lFYuY9twg5i2KHwdmLVkg3uSEW45wln_GlJiBtcSuNGjaVxXUvs0718Pq5jLB_1K44WgJCwVfQ6jMSbFvKCikZLdU45BGIy-gb0vJ3t1qXb2f5RGZe1MrOnjI8Yod1lYgXVakpbtmHFIeeM7iUEPlRyOCZTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCDQaZUCX4BQjFfdIReDYTd_HA7DwrxSpuYOYMZMLs6EGe1QMxgHmCnHWD-f8JNrwKvuK-GpQHx_lp3uq2uZRbcgB3NUWn42RTa2Cr04-cKhtwrfgtLPNENIOKEAM4WZshdmSxJMz1W4qGbJavoIEKdR6Osu7rqQGCRuu5pDtzqphpdYRLdT3qZU7D6uQ1LtoVzQtnEJ4My8R7NC6x_V_02cDIEg_TWXjUGNqTAvzbJRdIv-TQR_Pm6bvN1OmQxc8gXnwxgHBHv3b6308KXMu_t4n0iQghkG7R4aPDTRCxbidv6DCOx-0LvkXof9TBrN1JYF04l8hTjrFiDbvx3kBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB13VeeWJAuF0Gp5YL7Koyqfl61_xzvXKgPUCjapGiZ99z-xnVdQokTlLoUujOEsqQKz3p8XZ-XENMTZS4FjOKR3ne7BwfBNm-ykEEEokRF0V_myzwRrAZvHoGg1OODVAdWUpml7JrkPPuAklHA_BTmvIgKFAj89eluUCUUC8RyAJj6czZlQqIj_GHQhJMUOEeUkxjEuu7EoqsgFh9j96zbvqr8DE2tAQ-u9tK4kdH2xPLkGU9JhMsQ57yHbMijgld9Av8rggL49j3lBn6cS_PtDACZ-SrTlVsIczt3lXzz29SSGYkMTI-kmkF1QjJ9kBau1I4BsIuwcShKOuJSIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDSPidBfhDi4qbevGscvOGTlLKLBdH74qpTDrW0yeOMukoYTC3-Ut5mwlWnq-ksSAhQ_wbqQZYkoa_A0hecp13S1-BNiJsDJ8dWhQ--XCImRyJUfEPK9fvrMBS_2NsrHZMLHvRa2fKKxuXvT7Ema7SfvB_YUQLLFjzatsfm7t19jdZGnAl5b0YVcJaDNSy4uEq1JEd8LwF9f6ju2rAn939R7ObSsvp3UQICKP7T9ZfX7CPEMyPMLPvjg_83i1dgR7t22fgxLCrkQ7uDDUcL_HWqJqjgt7H_7eqgDOoR6nJ-93QFFVn7Sf61nuhpju3E1uCKq_jR1cYrB-ohXxWAteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoqkK0xJ7-46nirMZXmG8sVrsThnL_Dm9AnUAKHW8LRKNxqc9t-UjC1_FIO7jjDX6YO1xRlH0vrcbULzt1MllK68Jv0z-i6-51LOr4OoRPe7oy7Te34nzEzzCDxVzK4i6xulyYy52Oi6WGZpdeDVWMQoR6or5AgdfCIx4U0lhVl8zPpbZOoi6KW5IYw7c5BFTZN43yUhjX4iqNwIvy0dIxrWaQu8Y8jwhhreSBdS8gQ8UDbHLZvKlfMXMXm6NjSRlsgALvOsa98EauSwhUB7IzemalOrPeFQWRtb-e0I00p6GpgfRXapijW33T3EpJ2h5Zso0kxq12SOTcDxrb1UuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKEt-Fcx9SMjcvwSc2powtz7jMO_KVAeAI9w5O261fcZqMLKIP0QNqkHbKZQBo4rV6IE9LHkNaiEk3XdqDCtlSbIGHCI4fZBOe3SZeZZaSvCrSZnMUPyZvRqBKODTqZxlyXPRmOQ5i__m98vc0MYdpsMU-i1v00aGTQMawEy8MVnjdobRZ6MILadKqpFBg6Zp0tF7HUwCfObS_Q57FfGDvkrxVQFxRKPcbZvDe_13DNNjRh0COeclIAsRLt4lJPhd_Fk9INVootgxRf5VkN9ifkNduGPfyWTcdhUvzroG4QQ24bvrrS2VNxjWx7dx751EdaRN8NgJhVRnLkJky0L6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li8Bso_FL8GoskOcH4l8_zdNafzKPyTE4ub7h_jvdW4fwB3odY92eipglp_1oOPUROZTaHN3XFpKati--xjinlnS1sxqgSoEBL-8b7Ji24JSZoyNqYXUyAaxlbz73OAPjjVJgMj6JCYjs59rsFq6m7iRgVDYGjQhp6H6-9LejdyQC0putkePXClBZ8cARKJG3ZDr_1eFLiZ2GXsyDZmHYs6JINFL1zbisOijLnw3TlNApsB8du5TRLLjHTGcNkLGZtWhxA5yC7nHIGLgDLjeZb38TcojDjZo5mR8F9qRNJEnoUyXRI4fH5aR9t7va0c_xQ_2nFnCpqIcnZkcHjiU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
🔺
سه ناوشکن آمریکایی درجه یک جهان همین الان با موفقیت زیاد از تنگه هرمز عبور کردند در حالی که زیر آتش بودند. به این سه ناوشکن هیچ آسیبی نرسید،
🔺
اما به مهاجمان ایرانی خسارت عظیمی وارد شد.آنها به طور کامل همراه با قایق‌های کوچک متعدد که برای جایگزینی نیروی دریایی کاملاً سرکوب شده‌شان استفاده می‌شوند، نابود شدند.
🔺
این قایق‌ها به سرعت و به طور مؤثر به ته دریا رفتند. به ناوشکن‌های ما موشک شلیک شد که به راحتی سرنگون شدند. همچنین پهپادهایی آمدند که در هوا سوختند. آنها به زیبایی در اقیانوس سقوط کردند، مثل پروانه‌ای که به قبرش فرود می‌آید!
🔺
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند،
اما ایران کشور عادی نیست. آنها توسط دیوانگان اداره می‌شوند و اگر فرصتی برای استفاده از سلاح هسته‌ای داشتند، بدون تردید این کار را می‌کردند اما هرگز چنین فرصتی نخواهند داشت و همانطور که امروز دوباره آنها را شکست دادیم، در آینده بسیار سخت‌تر و بی‌رحمانه‌تر شکستشان خواهیم داد اگر سریعاً توافق خود را امضا نکنند
!
🔺
سه ناوشکن ما با خدمه‌های شگفت‌انگیزشان اکنون به محاصره دریایی ما می‌پیوندند که واقعاً «دیوار فولادی» است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4859" target="_blank">📅 09:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPZcy9vMABg1LB30K2kmUO5_BLt3K2ferJRS5Pffm7Q6ip-oW8DPd6zKX8brK1DDyRCHeR24PRXmbeoyACp-FvjypIQA3kW3qZ-GRw3pNZs3VpZmXBKAfn52C9myhnjhdeHk4jpn0u6OfE0Az8S9sBBIOLIHccS7pfWB-BBrXdss4lhVnjSnjDzi2pFrnp8ehOm2d-1Ksyr_1MOUcPSQS5d3S1rfS2McR3FsQ0ZwYzEZ7Zjen4Fc-PoRPZ1a_gnxKKZw0n9aKUE8FKFAbsm6vy4Qd_XZWRVUXycLpI7v_jRD1604rLLQG8iHcMxRdUlrQZKUb6bVL6-K0J-bbYzx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-PX0CzXly7x1e7s7l0Dj1k6tYlePOs65iiFWLsdjoLMlBOjlpyYn--z0Y6DVxAFndjmmuXchnxgdPmrH3xbwpeQ827sL5AdMHwOgWJoCaAL5uVL5chHrF6l2yDQ_wqHefIJ67fR0sumD5RtrrZ3LoJdaG-KsIilf7ZUI97GTxClrS66nkgt-EKSBCJnz2732CrYVFpZ00IjhXk5b9ur6Cnbsz8D2V-seFRKA1WzOUXRtk3YyP_6GSrz1FcX9buujTVmRvkW_sMfIhK_X3o2SA6Zz5HKBWuCL4Wedj3wetUBdhXlJ0S4V_98IQzWc7kfhK-l2yXjdlC92P0j9IPRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
تداوم درگیری های نظامی
🔺
گزارش‌هایی از حمله به بوشهر
🔺
گزارش‌هایی از فعال شدن پدافند در شیراز
🚨
حمله آمریکا به میناب</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4856" target="_blank">📅 00:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbFPtwu_JWss1K2eZWMroqtJvW81m0eLI3iw9x_6g9hzJG3ttvesxEfNavRKLiuyPwnOqOHsaBy2pigsmXzLKPKPOYVJ6G4RGVHoSpVh9YlbHmEqzIpUo76xrCcklKJItRR9edJRKzOhl2l_116cT73Pdxe25AG6fpv5i5thbdj-XX472DaVzPb0ZDVRvpeD5QBootspg25w1oCDC2rQh-WBMdFG69155t6Sr9wSR5lX_KUgXkh3YePYuvVyo3_WL9U1pNPF_0iOkNnpmM29sQlVeG5maOvmRFJhnUKyUtwRtVMaCk5QXQkeYkckycygZPn0HgXyhPX5llj4mhWeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی  به نقل از منبع مطلع نظامی: «
حملات نیروی دریایی ایران به ناوشکن‌های آمریکایی در دریای عمان ادامه دارد.
ماجراهای امشب از تعرض ارتش آمریکا به یک نفتکش ایرانی آغاز شد و پس از آن شناورهای نظامی آمریکا هدف حملات موشکی و پهپادی نیروی دریایی قرار گرفتند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4853" target="_blank">📅 00:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
تسنیم: «۳ ناوشکن آمریکایی
در نزدیکی تنگه هرمز هدف حمله نیروی دریایی جمهوری اسلامی قرار گرفت»
🚨
خبرهایی از شنیده شدن صدای انفجار در ابوظبی و‌ دوبی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4852" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
فاکس نیوز:‏ ایالات متحده حملاتی
را به بندر قشم و بندرعباس ایران انجام داده است، اما یک مقام ارشد آمریکایی می‌گوید این به معنای
از سرگیری جنگ نیست.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4851" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در حالی که خبر فعالیت پدافند در تهران منتشر میشه، جمهوری اسلامی هنوز دقیقا نمی‌دونه کی امشب بهش در قشم و بندرعباس و‌ تهران حمله کرده!
فعلا میگه اماراته، اما نمی‌دونه!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4850" target="_blank">📅 00:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=f3XF_chj7HIYOOUkWEzXsjwUp63RAlTNsN126kRNA7wduve-s8cpqVsEswSn5yq7l_eQB3kEckwLhC6bXAyxYIW_kwc8MLsM6W6xQywkRJ1MKyDiWoGxMDZfKM1o-4EjIsrcZ5w3IPwDh2mNzmQzT8DNbq2FO8mViPAHWCB_EnZhzCG7gOb54xTUPopdHX8Vpwe58Vh3urTbtAZwaSHpijtuw2Akz1j2j0GVoPzL9-hFvYljmyviVKFAsjWUjPfsEZqcjs_fVpFHoFiMx67mCk9-T65zDWwPEORuPvB1CJlBLenPduTphlo48ONyHmEOyj5g35gafAYwhIXeWIpg7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=f3XF_chj7HIYOOUkWEzXsjwUp63RAlTNsN126kRNA7wduve-s8cpqVsEswSn5yq7l_eQB3kEckwLhC6bXAyxYIW_kwc8MLsM6W6xQywkRJ1MKyDiWoGxMDZfKM1o-4EjIsrcZ5w3IPwDh2mNzmQzT8DNbq2FO8mViPAHWCB_EnZhzCG7gOb54xTUPopdHX8Vpwe58Vh3urTbtAZwaSHpijtuw2Akz1j2j0GVoPzL9-hFvYljmyviVKFAsjWUjPfsEZqcjs_fVpFHoFiMx67mCk9-T65zDWwPEORuPvB1CJlBLenPduTphlo48ONyHmEOyj5g35gafAYwhIXeWIpg7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش صدا و‌سیما
از درگیری نظامی رخ داده بین ارتش
آمریکا و نیروهای نظامی جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4849" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4848">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4848" target="_blank">📅 23:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4847">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
پایگاه هوایی بندر عباس، کشتی سازی قشم، اسکله بندر قشم و چند ساختمان اداری اسکله قشم ، امشب مورد حمله قرار گرفتند.
🚨
رسانه‌های اسرائیلی به نقل از منابع آگاه وقوع درگیری نظامی امشب میان ارتش آمریکا و جمهوری اسلامی را تایید کردند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4847" target="_blank">📅 23:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏صدا و سیما به نقل از یک مقام آگاه نظامی:  «به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی یگان های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
🔺
برخی رسانه‌ها از شریک  ۷-۸ موشک خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4846" target="_blank">📅 23:22 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
