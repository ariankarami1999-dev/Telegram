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
<img src="https://cdn4.telesco.pe/file/aaPt-8xAmPi-41IyZ36nIUb1bLBm0GJr7i2RwcFFr8WV4iLHwk9y7kMXH7zlDVSOYXqAH7p5uVW-tbLCjOkhG6-bjK9zpNBaIcd4QNpQRjWWrRJU800VLxwnYflsGT_vWGhAWcKhDo3nj67Xtip7exGJ-19Fie5A4GM3mb1_DvFfnROEB8GoP9TfrOJ0o07V9EGDhvFCnj41C6_fRUFdKaP-c96ze4KzBz0forCA6zxt5eT6h_82Y0bA2Cxyn-rD6AiOD2ZJGDNAHPhZEKPkwYx7598bP1yHi_dS-ETiUfIcUyG4Mb7mzN-YFRGwUrlLGJF4prXh7Wq0zdNwGujO-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
<hr>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HM3QqjzLuON98Gez4LbFHoDP8tkC_0PG0-VIFqvD8lgVWyicnjJASuERJjlGB7xJU5yNmHrf9Aqf3xQPWxaqGbfM2B_umiIvxlRaYLdZfqnmHgGxf7Xa0MxuUQpTQOz_gYF8dvB_ogcnnGzpNrOeHnZ6JeyenWJ_s3ePjIVeALxPGzBn--07KGtI6lkdEYL9P4jGNoTA5ZTz3qCQMYnBm4cBZV7_ayC88K2eobYC6wNf97CPpBNdrPfa39BYzUGmiYsEo-bihmeVL0hAgnEcVKJAZx3xzmivlWbTkQAGEceFBQQendUTvUe1E8prr2vdrFx741G41h6AI4zFDNwubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY_DF8kBNmLEoLm1H87lUX8Q0rz2xRTJkxTDr7i7JWyF2yetmEbb3eJ4MJU1Alh5rUT3jes2fvBJwQysMenlP8yXqRYak27iYDMhqqDeESk09OxtWnVYYx7bb1riC7CXqFoXfag6tWT-mu3evrg7-IjKWcAAPmyksCY7NxtXOqIHQ8qOgC2Mhs2JE6gDkxjZHDgwEtOv1--7EujiSQ1j3bhrtjGpnJcnBs58U5MXd2guE067H8zfRhGYwGNc2odeqL6ubLLpsvEvarMItrKvlhb3G_ufiPK5abWdd6u3qbC7hbCAKgwpyRfNDiMM9YPSe8djGujGVwbSW5aQfs3kyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K85rxcK9QMsBkSMTLF0tfj3LUuHK4QL3HGyGmRIA3udkytoiPM2-iz_MqqaNm_EYI3PukgPYFdwre-Rg2-ZGOtQYX6On1G52lUiBg1Oa-RaujmUbYZ8IbMmnDQTnbJ63gObNwaHynUIyBAkgsY-MRftKOlxXrHDEWRyALEq5lB2rNKrY7NCvlcZlUAAqlR3lu9EjonlQPrhhTigYdBZ0w9ZIPZQfHGDyqFDZZklqNEKn7CHkU2_vEuPqZ57H8QujOvdKvIG6frbZ9w0s8vnfdAm8V8JH9AfCojo1yZN9XSyV8qtbRuGWe-mUztih6bUQiM0ZdvkcUy3w6jVElSb_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWeuhai6qyb3ztOdsnlhpZL-VRGLdLkC-HbxneDRlzwuGy_6B1WaER1kwrLtlkJ8Gz5JmJoDZPBgdY8ROFNSpNKKrWmMn1dxn3plNltoketdr57x3Bfc9m1be3a_3Tkut0VvH4OnRtcB_9B_EWXibJsJzpZtQ8_13bS_XXNvPtbha6R9c_3cKEKV4rb2yfP889lVqtozT0B4zW5JTAZDpqZX1V1FsrJrv-eCzquJmBVVVgRS3E5y5vsSTwLdbfYc3qxw26NWI8SZQbubgfl5ojEjzlfOfOnJ8KBaieo6FRfHkFhzb-MLf5YjHsWzplLvb6vw9dEtLre7Sod6cnLq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF3hyLYJM8fDN08SD90ppmquwu3HOxMmNIroZcO6B4gGQhSkj7lLQ1KBc6ghqWnWJQQqCjxWPU-YgVUrCMWHOBDLY9xMioMry9i2MdxigAulAi8SvrHcm0lokfBgZuIojuSKT-ppoaSmWYQ3z-OHhMl-9D_U9mSY8eCFdV8QWCQB104H4JZ0kMrjnk1qa-FOMQL3Q-xMLmS_UuJYR4o15NfeoNJbb0SQiPQZjtOydm2KNBsOlWuYi1VB4hWIglyT6EkMngpYmgRxmTFed8MHJLE4IUJ_DGQcdJbf_quNpByDNr5K2lT7J86KReys2gLeFGDqP8OX5axmbfePHRBE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVLdMlapE7zhwl8FdbSVHWhhjqJhnLwFS4JRx8e09KG7UZB5vd5QxBBtVOXaBYM7-x8R8iBGu08ttGdTNseSmU8Qg1c6Ettxrc1sLWKvL_cJdShLxcv3hP31WIvls5UQS9hGiCcw1GGldc698zAMXVC8Q2jryEGdMCnRZzv2NtFzsInQC0O_hQ_bcJDyZVc-OQF-fOixGFJbODEDMdA97qJc9uW38onKQ4jNXONQ-04h2FMpfDjHM-sTWg6b5fQBvwPzJpMdhEWt5S2iJZe2wM1atNA5BUi19SFe2Z2-vGstxNYzhe_bHDpFuVYhjpNJBCTLf7vaMMQiQgmLVMhAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN1en62P1Lm7zPO8wrHmbJviZ0QW0SqTb2VYf2g0uSDR4mOwWF2MclXCHz7xEcRL3pgsxWyiiqXH1QHb2ZhhXOcAFQZkx7M2bqfGV4Pllzm5vfvlADyN7qFySjFc35-4zJQWivnR6JIIiCd_XcecNI7GknH_MrvZBXjMUwqLhZsJM08E_czjb8A9YIjiv9ynP1TpQSQQXAZV11jt6AeeuKVfGcgHwsR2o9BETeP1gQI5V5sOkLhuQpaoR-ypMt8IteTWFOvTV8J5y_kRmC8IEQqQ6B5Z6obLNbmB3NTbH0Br26JmOhYAmnX9fXb9Dlvpqaz-luuwupRRd1yIh4SM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwRqMTYb_KXOG-0cHGdtcTq-WKxzgDNRVxhK5GRMeUGNsicWW0Y2thprOfz6hB_ljpH-o84LYy_btaKHey22uriiKVxksAxyVti3qvhhSEROlUBs2RrQPpz40GZnYMwdM65PeWIyslhgPA0Uv1_6wV2AqUibnJO0PgMFg0FVl0VZNJxOZlnIZ-MYzN5CxbwcVqNVGbUSES5_QL5TEMKqm3eCfpLOKesrkmkU787A3a60rDpSiRjZ3BAblsCLHRzuIztWtSj3lNGh5r6Fs69iBzRPdV-0-5AAXCa4XsXRaEIukVTsWevl6QxTpa1dDLiAXXxCLVofZ9GEZwx6YeBsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY3WRKHzG0hrN59VXw7vzHz-VTkOi02VsVAwWm5hUsviPpe3dB44aof3gKoDbiG_aZkoEtLZw8_fSlLI8J2gwtR16O9yDjGuQt9G3yJjfO4mx-8jDB7yvUdYUk_ZKyUneHrlqyfHrOQn_9_4AxruRNJ_dWqAO4dfssvvHHKdponmuGIAHk0ZuJmrUkrLLO55_GSPigDQZuYns4JfpKdnR26ulOWLB23ioD7wFzicph-5Ixk6xyoZLjviSewkA2Mltq2RKMz9x3_e7DuArLZhReEoPvilDHGas41UKpTLOfE9oDDPanIQiDphS7d7XruHJOaA4LZxYeukMzTAp412Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI9q5rdwcJUeO1q4OPP2R46cq6VyDuMvBoZBg95KumGBqnn0aamz_dxIEw1NiKZaY_BmSkd4dwtpxLcyPZLMZ81nkBDipxTReMBaXusFhbjK8PTitbM2YIQBGx3dyrp857hyqwr99fVIoBPNCGUpGlITL0ZBgfe4txLSXrD3Djxefy80PgZpj67X5sN7285UoSYu1hW8c4wJ-g9_JT804h78u370KVNTWTdGNOjONgWP-Wnq7y-xXq7WQot0OyS1mQ_sH11CQjiayi6BvDfC-wVU8f2pb3qPg1jsquXZuTzNuXReaUqzn09VSxea6cO5RaysobI-pw6rqlsWUX4RNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc_a65LkOJR7lrJVRY4DzO1FEFZVG4sHtfcK3Ewar0WesqGFXbbbkWnPKoG0WXR45sXbuTozFYE0gbjqRaDUErogDY_qyobSmxVukfOUDMavVm0UAa5i-8a5sozZpwfgF6B4qXIkcFV6xGKFtKBYhpYWzUOGEdVQ0S1lswoH68T95m4EhYrzYIcYNQBywWXpqM_8atlJd3t7UIjSIO3q2detmum16YmaC2_OZQnA90l9Lr0MDwYkGqpobip_vZk08UP13bxAe-HkGlabhTwDcIVl_zQkumNCQjWTsMqujwV3YNm-87zZ43ySLK4HGm9vo5ReGBHKPYN3jqTWi7Iutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrlZWmRaI4F2W325Uo61AjrX6nL8gJ6TX6FKHArpmlK0ME6pXajdwzhsn44Fwp0vdz_vUPiS65xxHmgt1L-nXH03DvSfaKi1invsD3g16S9jLdpJZK0NsatmDqG9nDsXBCYs7hcLZgIqLRXL-yYyLHS8UuguKURhYiqA9k41hEaYxvq9n2BrR2GzcUf6SbRz72nLHyimjgLLR8OYBc-pKHUEaZZlOrntznBGXtn3uKedNm09pcUGfAmDb3TLCxkJFNVvlpqDpQTq2oUrQ8RKryguVmY_nKhbHn8HVyj5CyypjM5Gq1uq_xDYoimSMK5iSmw7Mbs3fo_EuGFISq9S7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=h4c6SAkl1hrBw3hYEWtFetVv2kObGPwREl6Ybuwh_Ijv0WBcgvsDoiXzwEsGhoIiOQlx-16Mw5PYcsYqPO9_RyBGWGpSaL5ahqDp05e38GRIRTczsDI_HYkIQRfO2ZX5PHZ0mzmG0SMQ0tCFidApQfeRSu0QS_lZuthPuzdo2EPiW5eiG9eDh9pJsW4kJjalZnBMriX7Zc4nLky12CSWXaXH0Ath2QAUa_SdXzt23muNOF-SWS_53GQOF4mdxURUuQ7CyB8S6E_1zPg1tloTF_2rlcpCQbyv7vPpwobhtrodc1k1uVYHZXVFcIRhaxNFmWF4s8NaLweEpIynwrj_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=h4c6SAkl1hrBw3hYEWtFetVv2kObGPwREl6Ybuwh_Ijv0WBcgvsDoiXzwEsGhoIiOQlx-16Mw5PYcsYqPO9_RyBGWGpSaL5ahqDp05e38GRIRTczsDI_HYkIQRfO2ZX5PHZ0mzmG0SMQ0tCFidApQfeRSu0QS_lZuthPuzdo2EPiW5eiG9eDh9pJsW4kJjalZnBMriX7Zc4nLky12CSWXaXH0Ath2QAUa_SdXzt23muNOF-SWS_53GQOF4mdxURUuQ7CyB8S6E_1zPg1tloTF_2rlcpCQbyv7vPpwobhtrodc1k1uVYHZXVFcIRhaxNFmWF4s8NaLweEpIynwrj_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUEvpQkdJQ1kko-eAX3nh3iRDmB_W9gYl8lmG6ckSFAHY-_iwXN_NAtMYf_oWAj4uF7ZMtsXzUJKo-gPvjDnYT9kIZkh1hRHmt5d8iCe9SRhbH2oRG4CqkgdJXnztDhyPLxQsnCBSC9T0VXJAmIE1Eos_RHSjIBVWPq2-fRqzgh5I99cgyzv1qUda8wk54c_KKJS0M26KFmIZyIlET6u3uP5VoCJ3irSUhmr9HK0xWusKuwzZSz3TPje6W2qs-TOW6dEYJigNN6hATvY20PLSt1_MTBf-xTFm4Vd3X3UTMGLJJJD7qcxqeJD6S6vv-pbgCOKUF2iFGZP3EU9fIG_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naLyGTWo-DjfWr34efmCVnzNOXGaETxgfOq9m3BFVGli7RwH-ph4kCT9vxAv0h3SZj-Byu1HAOCn43SsTiqTRnlA-UhEbOOSf7d01TJ4XPgDDfbC1sgbHygvNrZNqAbI67VjKZ163RQGIuh_cCGyM8QjzDCsfrlrQ1g7fvCC-a0cMNUpMjtCG0vIhg4WYOlUPSEmbv_iR-D6Twb7LEe0LqUxsYG3yERan6ESkERRM4QGZZ2VDndXABVz5NaWmayJaPYqlR8yQZ-4vQOirn9UNUF12U2ZgNddVetA198dL8XKVQRnhqS4DKFeFm5Pp9aDfiUPLUlY_j8MPVaikK5D6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPdRdTqdKMJVwUTDtAwTfJtGtNeZuiPK5TNhHG_NObaWZ11gn0MC7BS1vJaqyE68ywJ_Dbpaxt2svsiFP3mZwWEXtQPRgSq79w7EvuRDJQ47G18wyEqvdrVvWLP58w3jWBhLlJLZ_xlEgtyUFGSaMycsnS1M6UeHZI6AQ2n9VbR02pX88Ura4okK7UYYF6fo9ETz8k21yndccWCPTpEh0Sno7ijYmM2FgDycxOtPWNvxUkWbiMdPqgqps8z2MQEc-UtwRaueLsf9Q3AJr5s5aO7qdkYPN0AAy-lqRP_TknN1dVEpkglyrLq7d6wJVoT75DayjiqzOJumZpJPvkucfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-YI17qibGupoAmWmJgbCv2lvDR2yxsKNeITXmoyV6ldokWF08k_3bk_KBSVZ0ksRA831RUYl_6WMnlTKTnTddEi3k-Afc5JebiyGUP5gbxeU993FbQT7DEiqyBH-8cyJ2IbOl7uwC_DjS-EnqblXE_goCgDEz-4zdgcphdn9H9X2QyPOxkYW7nZEG12-g0T9sPZMKEpG9856-UxlBF7WX75LjSprVUXtdl_zu9s5QO-K87cb2Gqu00Q1jkulQ9U08Qyr1sIeKBIfs-il24XyQUC2XTu5dYvpoL5P7Jt_bLBukqe9Lfm7gvUBjDW21aJeu1i-GlA6ZPsgnk6VT1wZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSnGiVVT_TSvVKpIGYFwzSDK5vZgv0G2X-vD8_vKOD3RgG8Ux3N8XrMslwat0seYBfWy2IGROVfmVjTeeysctenjZneLnoC8ybGJ_CcoKB6T9g54Ad9Zek__x9IyqZ6drlsAQ_HOODlhglFiUjLYyYKSsDs4FgS4tr7bXfjAjR3FSB-8ayvXe8H_YbtXrltsRd6dHvqIHZ2t-xmxYYCkB5QeBqeP0ISGhwhRYaPWt-vqXjDnPhRProbXt55zCBdqSJnNs9BFx6nCZkZXgjx9Ur_wrjgZHMzyPzD_hfZez7TwtEWThYu6bqOvqt_gBy1or5mjZb7mZORhU-g9Lk1HiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbVm4LkrO00oOicZ_-n4iuvWkqDifuV6yDhbqRaI_iWY0Utb26MKtwbS2-5wbpDhJ6SdJ46YbflvrCIdmyzWhK_IyCn1selfUDRO5jHm0jUjchsbNFDZAo08sPE1qYWvSt9ZRb7E_ItgDtfFqbFR9aFeZLm1mr-q7lqEQtVlUhu1Qzn2puPvLfG56KRZ8yUqv1YgQqIR669EXBf1TL5BgvhagDhszXBcc6-Z4L0GuupeZ_zE-Oe0YhEOTOxbP5e-ugbKh4rdr3Rei1Lm-pUkn7t8oqDvYevPfi3EXnIa8SQdGC_rqFF_8z50td2Sd-yuOT-0MJEDbKmywb0CVlbK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asnkVP1OVarNJkLkAJF_ZE-pPtkMDlqVh5cXsFeLWv0IQ9ZFwg4TpCJ2GjImDXB1R-CJHM0XRnCt8gTKCr8rb1iHvoCGU-CUH-42sRqq-1fNd6-c0V7ytBTixP079fx5o02CM1g7egUMkef5jFh8A05iNWQjsWrVMhwuNsd6yBnL3T65pzUrHvj_JnZOWF8tNxpU4niCw2fnDau9tyQf2V94IjHcHQy63LuL8vCuxiv22Hp0KI4CKnyPlMKYy3N0fnI053EqZRtNcnnXxvmsAJKu9h5UjgoXNgbtzj-PI7y4ALlAqLnKKBwQCE5gal2PFxZe6gXD3SQuaK56WoAO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=XIFU0PuofKBdcQ2Up3xmAzjCuKCby8BBqCovpEEzIH_pRTo-jfDuadU5Go6pLmH3J-nY5pDQYwnxN6KhbbzmsDA0b0WC7suTDdr2f-FMWyIrWNQhNXeYepw6Q_22eVRmD6btKmp5xyY1QVS_BVbLmRw0oJSEcaY5DKKorQa_g94WPctmwVkhhyFBZIyrDstZtGM4Cct0UQUDeuuB9xdk1gk7iUNbaREHx41Fo75CUILQk-ijeyd4unG_H2g6DXSWumRNA4Vl6vPaehnbZgQHMHRP7fj_ZA-lJzDhkjxuSJ4XAmFL5kfORDiazM2yumQhl05vsSv2TrKxOO7EXc2xNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=XIFU0PuofKBdcQ2Up3xmAzjCuKCby8BBqCovpEEzIH_pRTo-jfDuadU5Go6pLmH3J-nY5pDQYwnxN6KhbbzmsDA0b0WC7suTDdr2f-FMWyIrWNQhNXeYepw6Q_22eVRmD6btKmp5xyY1QVS_BVbLmRw0oJSEcaY5DKKorQa_g94WPctmwVkhhyFBZIyrDstZtGM4Cct0UQUDeuuB9xdk1gk7iUNbaREHx41Fo75CUILQk-ijeyd4unG_H2g6DXSWumRNA4Vl6vPaehnbZgQHMHRP7fj_ZA-lJzDhkjxuSJ4XAmFL5kfORDiazM2yumQhl05vsSv2TrKxOO7EXc2xNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3KsqvLMy-5h0qtHBivSbvMCjmvptfwmhl10C7M3y2WgaWDtXgQf_zgSrzjaAsD1J_1PGUbr8-CEzLFaCy6gu0AqT_EMvUkcY9Tm_x7AgiFMxgqmWwzHdbg5HZVgzTYcqCitVQ1CpfSBuVSTA80PK5lZY_sUV4Wplvrlq6rWbADDayW5OOgvHJdYU9RFkBT6_GVbu55yJVK92R_PZgHJ_hQ_1DEjHPQgjWB9h3t3R9S621iAj1sU8igbAdOjpoxAd1NlpD-rpxwpATF7aE4l-4HtldYpkVU7QiPPEhw_cochmZdqBChVHkNPkzZNi-Yo9GugayZhhdbXPXMUN9TVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnyrYTbuQUed2TTi8GYzSjFrfyYzkLqZhA9TAd36yEq3GbG8vv0VjV8wP9JnzJnSqcglohh0qXoqYTHpvhaQLpPiNzBcc6GEAeA2_DUf4Ww_5gDecJLun1M7Wqu6kXUvO5e6bHVG2JwQXVDkGRDF-rwDk5t76KlJOAkRGfpuQRsnyT9vQJeL-9VDrxpxaq7FF2xSlBpXxcz1fiEpnIKDajuhGTIfEpw1aU0erJiDgqgNM028Be9WboVtrDZLKQN11cQm4qNIhc3T622xkj_o4EQLwFD2BHEw4bNVEEtASBnBQXfAZXicxqpIXsiuAM1FfEdLLsMA8bjzGT5F-WlVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJl-md3A7dsGdbN10575WX0VDVFzh3Gs18oJJyKsPHHmiPIdeX1O0Aq7z2aToBXU7uRIPbtVfSHAHAjAiTPlpPSgUyE9VHTtGqlaMLGBec4kgctnenNdsYym2N4b-Q16e7ddESxB-_fZQacg6LVQLIWE8iWYXmgDV81lAi4L6uPr900UGmiJCP5F1b9sUNYGTrp7WYw868bHF4fhd0sGXPYNIs9viGmllr-39VGbOqiPDYZ6ld9p0dl6g7ZeMJTFcFv9NaLY6cjovHxE-Prk5bHfi_8xIMKEIJWuHNG7kwTXQr2s1XNiG6kvkf4FsnfVDvU95jU5aalWPEg2ljxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_JfenSXwcqdSdB6b1d5ClBCStukjBrlg06BRp2R2r7x4w_yRbVNs54LETRU_ZwGggCBL5OrZeappwlCgEh8OVurgFRvPMXJWBcf5iiseQ-gt9R8l3mdmBhglQjBZ2kvLtCcA_p4XpmoF8A50COjCVgdm2-p5v9oSTSKhFoeutqDeua_CCRdf6Vo-K4tlft5mn3l1Fk1edWWCFZ9STeXYoWqJI9NQabC7ZL5ZRrYk1wr5MOMKn-Y9pUdykvs9K-7NLTdwCF2662Myav3eoWjR5eGewFDkQfnvF79LWhOqPfMKj9LV3hlgW12PcGpG4v2Qu_LuXVA1Qel52MUTOaKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUInY4DRIdUVBNAhNRKED3tfcg6fQ2GdSAYqrOOI5O_Wn7dS2HNQdeKHP7AZ5zkKxfuVGSIE-GSkl9YZORek_4ixQ7q0ipwEL3ZZzo3vzSwbTK8z8BTBdbOTPcoErKRhpKZjrfFWNk8n4RM69Q0Am5NSLQmft6i9B-YUaPet08Dphr64HRZFHiPUZpebW7xP_7H0Tlzna6L5sXdjqDZsIGmKGEHcpkkPG0RW2d13kYMmxs0tIHdrZzPL9BkvMQQQbqVL53yAXbv17xuskLR5afp2qabW0QEwIhPrdEZylcE9CHbPAx1glBeA1Vh9VcRpEz_t8rCdrwPvj4dlmhH-kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsNr56xyzZsDaPUOCVMN403ECk4hTzePq8ifBiVO470A2fgRIdBV2wTse53aEd8WtZMWoOS72lEY_LzQy0fSMmdrbVWIG61v4QExaw-Ap9-o8uU8lEDlwLoluR6Umae-AFBUvwPLlbAMKUYZZwSbU0lydBP4ewXYoa4q352AFO3affhytUXum0VWkTVoD9ez-v8pGj9FB9xTJvwszni_SUZSZZ8UJEWct_6b3SduorABOtuf19qGj2n7YlNo0PtsxsP8lL5drrs858KNjeiXsGlCaZ8MF-THAWALg625o9FkHNAwDjybYJswmfFjIWQEs5Xxg9VvxbPR2JxKGdpHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpWlqSZQz04Adi6325bYd4Ql7pAfBCZx5rM1Phct-JAdfVhzus8-VdZLpJi7XLzM8MqzzSesCHlxKUYyA2sd-YM-kADLjsjYaw8vFsiJ2dZD9JYDBvcSj9Gp5Ed9fcTrUjKogyZQp_R4vhrJwVpF0XJccwOYtDru5iBiIpQYa452EKkywldBi4VLHPN_-UBNVIOnyQzTkBKqhUM1xTGH9S2RIdjJ7dNVPCoauhNd089j9ckTRJdn7u9_h6zC4wPJ-wYMeDvm-RuxKEtetwsdpeDRs7H0ggFrJ4VMbpAzwKm5UQnO9Pq6LvPvbjHIaEYLa_xZzUiUSmPybNZ4JufduA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTZO7XIJliSl9D4scpKRAXwN4xlq4qLzt05nAWQvMnKN69YnMpz-O6GlCuwjpc3I2IsUsmlbVxD90v0ci2z5ODRfV1V_pXwQIEmMm3_3mMZjk2GQQ5va4DpnNmcMMtsnR1HUy0bxGjPhioUctvUp6LsMfVt2aOIFhMJjKq4Zd1QPjA8Qp1BNbVPCzN_m4t61WC5lz3zQBGi0vI4jxOvmlRITkcE2jaT6m6KPzuYw56iIwDKR0EUTrW4Fqt7QMTp8q6aTJNoL3g3LPDXzyrsDcyYkq_pPXx8M65k75G565r9j41aROa1z4sq8piQ-btDa8TL4kpglI2iIeUIBhHEtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fi4QTYhdutaSqvyvNSvLh1Rv6vKtequvQyPh-jX3yx6cUbyzKS6bKJh3Ou2KHnIlDY2ylQ0nHL9GHeUU-siNRrico6GVMqpw43_U7hB24sX-4PaIu_vH2ASb57HXvECRSrKvtPfTPwwMrRiyiVj6ub2tCG1lF9C7m1Wxjg_nGBwbEEqTt6-8yeg3maFumhhy2Fzj07Rqsqcg6B7Akpp0ArQYWBZMmHu7AJgd-G731yI-TRePoolu2jk7uPlNj4fR_oCYGw9v5sh0cJl8hqvmKy5eiRvqvyuhiUwdlAThW34m_dugynuUm05HhQM2_t6tbtfG9LXntA_L5129YTGQ4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=Kg0_hk1dfgVt1EQNeZLxTBvrBn2y696xL5uSSuVZDzWMWiWaI5C1n4r5hdihg80XPlvUGIh7bISdefQIGLr-VGIHpr04MPGFfEaRXNDBtags31AE1W59yxa7EDEqOCNPTUkIrliWUayAXgQU-LBJO7Usp27bRKMtrKZNQ5Bis_ZxdLTpDHytIBadc9MEc8jSt6Z21D_hiXrC2zYWxJfvgOL09mLJKvrGwC3VY7LArPdjt1coU_rwLxBa6Nl7THa0wsNYfUigPByuXUXrmvOO2KelejL9-3dKE6UstepEKCoFQkhgRvXytm24YX-bD5STa23ImuaflbUfDkXJr5lcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=Kg0_hk1dfgVt1EQNeZLxTBvrBn2y696xL5uSSuVZDzWMWiWaI5C1n4r5hdihg80XPlvUGIh7bISdefQIGLr-VGIHpr04MPGFfEaRXNDBtags31AE1W59yxa7EDEqOCNPTUkIrliWUayAXgQU-LBJO7Usp27bRKMtrKZNQ5Bis_ZxdLTpDHytIBadc9MEc8jSt6Z21D_hiXrC2zYWxJfvgOL09mLJKvrGwC3VY7LArPdjt1coU_rwLxBa6Nl7THa0wsNYfUigPByuXUXrmvOO2KelejL9-3dKE6UstepEKCoFQkhgRvXytm24YX-bD5STa23ImuaflbUfDkXJr5lcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbiSHyDIZC5l-vZNBoRHmxOdu59Lshws3VNUCYqZ15HNR11H1oIqYnmS1xIDjEyMbcmdQCb3Pp-t7kxrBj5F-4HQy3349i_3G1VMaxjHffu3vzKNUGfcL3laYpSzMJh5gOxw6FkGjJ4YibY3DsRnoQe12bXDWpnasZZyAjQaNfi0k27vDsdM8RnSPsQtcyjG-Z_A-LD2-_RMkmD1QyDw8PTtddaJIE0lmnyWsLSxfRm4nJuYsbJzM93S98v1tHOxVI0gbJDW64fq4EXBfypHvNAt2aPKOIIUVKmytF7V0tMj7Zu5IJAB00yYZNBcsp_om5ZIvTs_BLcvxzhoP5SmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3s8L9vmOuNKArFRt7ey6Oidjs1V-Rr9cLvTjxW0pFOwzn_uZtY7ul3-BzAOQ5nEpcBD_SsG2S9VPYeEeRDuBWv83p1x_oyiiAk75GnLG35Z0mKTZvkvA4BLsnOVLO202OOBDeOQ3fNVxmEV0vUTH3DBYtBsEvP17u-jGTdkMdxelB4RuiRbqBUEDNsaqlAwctmjr0k3dTBQbdzO6LYfL6z1eIHL6QM2ibTOJp8UfusssmdM_UIEdKdZUl8v3tQ2uSnh24BUxWRK3dpqCHGn2io8St87XX3m_PjcFmcaHxFrd8FQU0R2vc-zSDocsv-cd5w0UNH9uhW6EETwn5DHbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=p4ljMuSK4cfpjxHAqgxqtWcSOu_ArvSgQzzlzJtkFq30fFyWsoVpeIPrCSrqET2tHeHyBEbDioIr3LPq66m1kQ1nicWsFYmtWGzf3SxUyMSJDqe38EcFw_jlif2x0l6RDz3Dlkgd3nVZEasd0FlMJp7BUprVGHM-YKFl4yr2QEZiGVYOnBUVRAsigfop6Jg4kBKkBeHZbjqrisuNF94Wv55nzfQ4Eadw_QXLIgGC6WbSoESF3MVDcAVN5q2zegltlFpqUtC24gGu5X7i4FcQ0T-VqwsA5TogySY2yagSJ1tsoM60Z_FGFjIz-ELs4Sjw9g0cF3NXShFJQ6JLOV7a3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=p4ljMuSK4cfpjxHAqgxqtWcSOu_ArvSgQzzlzJtkFq30fFyWsoVpeIPrCSrqET2tHeHyBEbDioIr3LPq66m1kQ1nicWsFYmtWGzf3SxUyMSJDqe38EcFw_jlif2x0l6RDz3Dlkgd3nVZEasd0FlMJp7BUprVGHM-YKFl4yr2QEZiGVYOnBUVRAsigfop6Jg4kBKkBeHZbjqrisuNF94Wv55nzfQ4Eadw_QXLIgGC6WbSoESF3MVDcAVN5q2zegltlFpqUtC24gGu5X7i4FcQ0T-VqwsA5TogySY2yagSJ1tsoM60Z_FGFjIz-ELs4Sjw9g0cF3NXShFJQ6JLOV7a3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEtjoKj5LUaj8sEbLBiRqbqsIcZpSZozwXoZDDIypnECb5wBGQQKVqCRRgEBt5dxvCbxxvFT8GCjimX0v8MHL3nA4N1A8q6U8KflYQJAl4qCmx8LIRFEOqW45QibsJQsqOV5jQsF_pEgXQFwpCgKzNgoU0Z9b_6szMckM_4o8nKUkco5EfIHNUgOdD1Dn9CEQWKhlPGAZ7OMGxhLn8EGwFHR7WsTOXf3eArJNuDMWr2X-c2_Cdy5Q77e-2YPQq738fz6jFao7QrZ8ZvqMOYVf5EKYKfF6yEPqtdYMFle-cHYqBTuXfSbHxVZCJhGZVq-a7LaHRr4h6o-0_XmNymgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgCN0IaMiwgRAyOR3ZdKowyolIEyCORfx2L-Sy05zrcmNU6vy1U4LJ9jigTiu7AsIOmRIFITgx07qP1yLYL1heFBHzzEzKXurdqMQPniVabMCUuUx90hBvK2PFze454Cke_Iq8GYQRoPbN_fv6YHdGKLa_DvnNjk1hjaWx-gKGOdO6z8mDgIMZ5lMgIiCyQ5LPXTToaZZguXd_39huSQHHQ8jlUBIvDwC6ExiDiNdMmmAn8xljb-7vhQXuuI0Zc2HBoxRMgw4Gpv5XdJS_ATX6p2q_FK9ynjjrU5HQa7ob9yToaXR_EbefP0wvOHMKcPOK0ACB54mNPfW9iW4WAnQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C72th75_o3uuyf9neE3eAqdHY6GVwz7gWlVGQnhlWz3uq3rRG_qtDWUn_QrmbGRYTNyZT89JDYPbDPu2fzkuSfLyn7fBSC0HzQag-bqKIAh26qKOEPh-e8gPJCwJY6W9O-3eTA1S7gFSZMsYW-hPlfuIu4X_Twr6okDsQvtRVUrBVtD36IwDDNOx9phfSI8J1ayN9OEGEoxWQF4o6LGYUDltvdcqiqveLLb0VPj9uUZXJN6EJUkv4_Uyfm-hKX0wQamPihqglIlPdVacLIsDcx_Q60SXhoMCES2bmbPvbhT3cRoWexsHh6DLa2AJ-Bv7hrEEKly7ikbW03EuHtWmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gccfieh2Z95MBXm0oPL0M1J-orIUfg4Fr3YU4q1S9VfOK5WaXpwBB77fCuGBojIYjeJssVHVY9INXVzzvYhrDpyf4WPT0cs91mZGbQ69WKWZQvo6vPgpdhznWVN_GFWmSHg8AaoTBUbK45HWm_UxUYC8ybboX6kRVD2YH-JJokWnaruYK0mBeOx3ouaJRDLyPjG6n7I2k7woMmY24HjgJAuclQk7pbVAippL_4BdXe-lCHkCnAFw7MnNk87VFyFN5qcjaQhuKjlSqvjZ5_jxn48U_il2Q3tAEAi9u5D9zXKqy3esRqYnSczR49iTHl8i6ljHIdNKEhcBlsRE28GOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p81y9vmvTFtgoQGxN940FnwpXtuFn0RYBtB7bGe-bkoXKEGeNIZu3CSCzqcJ2LCE38PTPpa1KY9UQ-4XMpydMpUQYXNS4iKjeYyJprPVsFFLPteloDsMHNKigB0bSrkaAaNxUukFImrqXpY6KzyVEnaKI_S72FNpRt9Do3cJFVt8_yZmUvbq-3uBELJaTmOsmowWJlLkTP-I6uMi_6N1kMv-bon6G1QLtnQFbNn4axl3Q5yENSiw0NIhr8M8npD5ah6E22pAFNJWHY6VKvshr1z32NioB_HRDVt7g8wTyTuvZ3_l4yfvIR8_oZVnWky91jkd5mBBZoAP1mmF3-425g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw8VotpPkppM7k0QU7d2Cf_LJMV614CbBq95H6cOSd3yNP_yGToEQT1Htl9BERQ12GFLGThRdV8T9i4BqqpSBhSWobuBnhKdqqvukXqa5yAYeRcR-BK69zVmrDhkJtXAiWHmr2sVV5Y7VZ41bryk5HuSjbeRGVGADfjXsygYFcNWrUGKpze1Qo8tT_3xEE1lqm7QCMadcupMGCRSchbWJ8COvK2FxChKNofDaBSnqFYjj2XcuOkU-5ogROTcHnqOSj4MYiJqZkCzDij_XOUz1OD5s2WTBRnO_nPBKwq-5Yuyz6jyPS0aGXoFRn0dWNVb555D-jQIC4RaXwtGU9MeKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4vpZS2ayVXET2GzJLITZtEnzYT-7CmebSjIPi4-jlxjqNzVSTEvRyTOgmvyIVaByOWrXv1Nv5-iTvD7Cjnuhueel9KUTZw1HiYfrjI66WuqPrV60wQonmkXDjXiG-dYE1PKvNdZPQDwiogNxYUN8cNNA1zfOA1lb0TBJ-35Lv9rrWTwiJh86S98PINR382iCqvGTQAUTl1t1oDUugomgBys2Buz3KT_THB8VIp6tjaN402Ges9aAZY_fKP9neTjGAOvQ-1Eq6Qx7JohmdJkJU1KtlmA78XJ8xGqrgGxz273Nz73MrvG4c7cov0-kRn5tPe1VX7AwphXrxBB2X8IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWs4uFbfhd8lc5qAq57BKFPc3WshvMxMhO_J8owZmrddBV2sOG6q7cmBWZk9LL_HdOZDVsiPSQbMTbv2UnV8K1ZVjttSalLGrKv518b6aGFUrLan1mX0fr3fTujywJazpW890ipxWPYyUXmqj9X8F-mA-BvfHfF5XLmqFzf222k1DkzfbPEUO4rBz2Z4wv-WCJKB-qkhwu4TRnCmr2wxF9Wv-4-J7q1L0eCh_I2fMJ-X01F1NX3utnDekof6WLCxLpo9cYDrJMY_Mo5B-07U2rFh472U6bI7GkzzIxtH_zbJOtI1BUSU_HEjC8h8tigHiIda8y5U8fJzrZjAsb_evA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4SYADTESqUFM3UGd-22B8a7riOvPsibYHGc308evpx9Rz9j1bePfRPuoAbVorNecfega4QC9kT128_87pi4-G8sP9ycWs9lj3sYklP_72ytZHcj1lxY-255o_6UMpoIbEQpso-EO5dYZS_mFiL-eOugp1SLCHLpBAehA0WvJE3QpuIcBT5lqg_spTjrYZCW2aTqW-0xxB8aL9LD7Vwjnqw47psIQR7FUDBYOCEzpFVj0hQn_jSELS-FKl6d0ls-xwby8W2uckj1rS5sbIGj68BbI7o08RDDP_U9MN8nAdS4k9ZxJUTb88OiPn8S7jEfPKOHLczxtZ0_Oyu_yksXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1CMSAWFiP54aJ8qTyoo_KSPdAQOS7CdaK_dv_eHS5mPW28AIlnE8Y1b-UMgPZyE1i0CxTJurKpMghNYzHPSzky5Hc__--2gSMUshhiVeVSE6gaI-AyY7eryk2xW73ZfzsUSZzVEX5AaZt4rO_tjCHo62f9l48QVkOAsAn3zgYReRfkvXbGfmHrsjoxshcbB1tfblwBn-VvKgAb6n5Dulbn3KRK2Q1Vj9xJ45MAmUSJ2j5grugvNTA1c1ao1puHwaH9XUkWRv9LfBWMPdkpibd2VnuI4YNz0-F15FupIcfVAR8LnnpaUXQcTBjTXRB8z15p4OCVccgq09mGHH07HAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2_jR43kD8Gpr7lsvoWfOFMKol_k40WkMhu5cTo1-jBAwZficSo6WD64wel4iSKltD-aGmE0gWwhc2mnJQ58KpsP8FjreHB7U753EcFpFgINZ_gP32xqDDzjMe8xQ_VaBp2oUMKey3-Mv8mEJEkMaSoRYkv_vU7yjEIDAP03wi9r3BvDKNCijC1zLG_rhtMc-caphA1ZuOw_JCcL_KarRTvdJkM_jnz6M_7gH3G415sMjFC-aZKfWCu1S_dmtRavAHKx08bnjMUVM6tBHJoQLQd4eda_8Gf7S1O7mpJApllAz6NThogbWWNdtJJdE6W-oIQdPeFs_IFbO5SuMqblpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBlWBEetat2E2HpDNCvftN2UhZzICQX8S9rkCHnB4ysbifA7y1dXAQaRXxaksp6HhInUQH8MitRH9dbfsY-3oPSgBu19nr0Ta-6BipYZMc36HUYusw7TrI1ESsC1fBkCokjO3UIu53cIcjep4A3fyhMxOlZCqs2-fpC3g4i7oAU81EdcLnxEk8S-erA8xBZf0jI-Bj5mavexxPUniZLH0btw-SNZXjTuT0mtncJrJCK_LFCmz4RHNGT7oL7cNPOM8uEmUdh9578NppwVcLIoD27c9zz6TEzrk9-1jGdsmDOCOP9G8m3ZatmHbfG0qofR79_exm53sAGbIVXqbxzmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZCwK6jvZ51u0_apIemFLDB_JdDcBCAKUhDWwmqLpYWcMtXHIo2xpyJ7dvrWN99HBsi0pUCXbvxEnPfq2BV4_458nhFbzyQ50snYrG2DX5tvfXouIqXF6kmvowa8ua6MOMawIgxwBo_ZedrWP-ObtZzKJSNA3EnVFHo6BPuTY7mcxGhTZDooVa21GgJqA5OkpaBrBbJpGjlZwuOglWiS6awHwjKFkCaa4mXlzoEY3hcaOqVsQpTeip2g0SBSSu7x2KZa1JpiM8fiCAPd2HFQpS96vlLiP5Dyp-ysNPnF7XlCq0b9miKbZuONUBZJ1od787c2ZVFVUsO2pE5IgNwUYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=bVDSQ9sM5iyk0Jom4f5qkMHw4lt3LOffHR8Iyxl17lcynMfNQmsegKTUfFgemPvCyYkSBpbpwHOWDp2MmdyHDaiRA76qLIvjB_UmTnxfYSq7B30p00RMHucIlUv2HFR_mksmtoth6YMNRne9VxqXmvW7L4IsivJC8cXgPJOSeiqK6vJZdHQSHTF8BenuxHGQIAJB4ja9-8DkI3-0jHPyeCFix9eCQ57I782Nc4Fh6wD6s1hwHvNGlBafqAqGs6UY_zI8NgKSz8Ih8ultMy7OYZMDSiaOg_guM6J65VjEVLiHGuRyYHL7vZCKyenV-X0dxpvWZDL1cvzPgee84WfMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=bVDSQ9sM5iyk0Jom4f5qkMHw4lt3LOffHR8Iyxl17lcynMfNQmsegKTUfFgemPvCyYkSBpbpwHOWDp2MmdyHDaiRA76qLIvjB_UmTnxfYSq7B30p00RMHucIlUv2HFR_mksmtoth6YMNRne9VxqXmvW7L4IsivJC8cXgPJOSeiqK6vJZdHQSHTF8BenuxHGQIAJB4ja9-8DkI3-0jHPyeCFix9eCQ57I782Nc4Fh6wD6s1hwHvNGlBafqAqGs6UY_zI8NgKSz8Ih8ultMy7OYZMDSiaOg_guM6J65VjEVLiHGuRyYHL7vZCKyenV-X0dxpvWZDL1cvzPgee84WfMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PpFHpQGQRJxhTofWIpdcSm70M-UeLdXw2lCUU_gW_PlY-55c9Vie00v41_npapJYV5vjyjTZ2n03YNbcWyLukpjobTMV7--SSRRwUAf9dJXqD6mJnxmEWwmBgcEYprdp1wXqD8piy9xJTj385feErXoGfYtORiyzoZIknaeIE0eGTfqYlRUHDWxE0QfvAx_l8VYhneR2XDabejNvQZlM9AyVJn3W-R2lCSMKLXxP36sD4zVJT6YmhnNBAmSpm-3jfxM38KWjBCT7PtNsJgG88ZQlYvGyvS9kq899IUUPbHY0pUlvYU1rSICvuENA8Ofqwcq05kZgd4X2T4ql8m5GPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omPm5wDEkFrN01HZ4CPrAlSqQNbjOlEmuOHtlAlwoXrD9UmAUKlt0VhRWeggy58N1-S7NXOFKJbNY8Fk9pD7X9w024M2ND00mLUTvXGyqFWqFtp57lzXGV6KXhEywWI7HBjJmOgmZEgiNFBc3deZwO01vZtPvhyWw7dcajw0ot3QmyxEfcIH6ewy9ro3maBLEIyxOAk1efyNXvgx17rUB7FL_yH1FfLV1ABJFGMi7oo8b40wi314yY2giSEYJD1g5AfHE_gQ55BZH1njf6Gfs2zJ4Rf4tuzzEgSJHCULyNA7ClfvdDXD1r7FG0HsS-3QRMJfmLGBF52MYQHMDlkETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeTBztIAbkHVcORyMJ6L2mgxtKJzPtw31-0tImAoI3E9jCJd3yW8VdEdPj08KVQxaG2bW2RZkdNnvn2AyDc3Rq-k3lVwWXhYbBTsV_xluwCEABwE1LkVhjmSedOI7yczPMCrrq29023V2bfLCC4YNKqw3GnFzN5E8WEuWy4Mf0nSFDcJTSdcdktuOSa4efpr8697Ra_aefqf0fC8owT-pYicaTZe7Ep5gDLuOP6PNTHknxHSWIHPnmLYiy0oolVD5ddC3EIo8C9EX1NiQLx3xWi75ennbgDtZ05fFgZud0qOfjc9sY7rjRzXVh5-Y1LGkJ_dFNVp1cNCt6OZUd_TnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5EKdjepC_3ZsI40hhF5HwI_B4ck4nvTck25auzgAnB4AYfcj_3OWSIX2j1chWZU82wvSmIEIrZBd0GdPcP-FfPuL7GuX-vT2E4DL1hCFuTZygjA6kSiVXAy5WC8bTP_dfPslx7E7TDbFOOPYKsR0C7STPiLWfi3p-Wo5QOo9AwopfHQ7xuOn6v0JvWCAKNCnbj3rBEjmzbFndGKHnWfpiyR2ON6-q7vC_NvEIb36Oc-8o8MRbSxlrlHBytrm6pMu2jXmpa5dX9qtAtXadzeV2IiMD50T0va-TadI2QMidpSDA7jk__jhVrzsU5dJywR1pGqnDu0iLiW-okundfEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVwgOZXrYDITpZ4WGKiEnlmKuDxeISrGXzFxZGltVd4SVv1Jm2dgKE9DMy2nFyaZ1s7qcOyVHenyDHAzM4DJ27BG0o8GU-yaO16mXkdJY8Jsfb9cE_8bz79R5GXeFYXP5MiyEjTNFhyR5fbA9-GooqXoGfedR0q7qETrPj8fbzjEgAeaTbUXmkUZj6kqasufnDRNl11vxvWjB3AO-FBs42ggLFl5mJyta2kbIGUg2kyznV7XbuC4CmUsrBOQ3uYhCMqrwgiCMlgL6iZeUtwzmRACvfHxVpVuOCOWvrx2FT16qLCTlGIAIoJDMo-lRJGdSIpcsAilQ1gGvdINqEfwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMuxDPRnzL8w8JKr3i6wUUKieGW6UYiMO8Yb4o2n5rbdpPZ7oU6iRMAivHsqusCj8aDsDOtPf1qbQpPZWOQqWyWtCGfBUu2oka-KlAVYaoWg4hAkhqkGmEXodsWSQYNj-tZponq-tPG8sDgcAtl1WBIE0ARVWLNWMjfT0LCAEMExzfFLf1DkloX0QV5mSfbtW8xNCK0oNwRIlKkQzTdKFMGKKTytZDM8IV3KUllC3eRqSxAkkKK8PN4WdSmwRy0Ip4NqO7ZG_TtRi3gRJjEB5D3pdiScXuNHOHlIfApLLdWpGGBjhsevV37uB0yP9HlX5VSYHQqceh2L3SXzXpGkNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erHWnRFKFXKO140ljCF5uS1dICABYzafj2og4eKsyu5vK8LfQzhsbcLdeVgGxCbF0iBohRuGx2OQbvizHX8HGo1R91xQ6dYTZxlRtn8kGJYSUZ7-WceCFLa4gLtDgZv0Bl3RGbmvkialFii1588nOrQoWGgkpwxmSuBdKPgufYtnjYwIvcL_VSs5r68d1yIEnlVI9Wj1VAMXg2ihKPHFV35o5u07m7Hsk_O4o5KM1SOWHvz9RZN8mYOdIaRn1ZPVQV25YToqrqvB1crSRow-EiqLYUNVcX5LkwTXZjpGhbmKy06ghzkucUQ2tYMZ0FRP-CyOHqHI3Y42PNa9xLt2Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9oYCJW2DHAksPqy9iHH6F2a7uGyPggCwMA1iuhEK871D10f4GpjNDaDtltJ92MmHEX2JXGLqfIO2TPElR5PEjnyU8MbeOpNFn5hxTMTvFMba8R9AZ_B6jKstmZweZSSitqBGkSki5MoQvspLo9uLIYonrEw_BOGDkby2r9jghvLZ1dWVDrwOlu4ANFJiGfSC62sRXnDSX6hXUs9S-ygDldgXvwDC2SOnBO-3gq2pPey1k7CEyxrJEPBLswkkoy8Ey6vwVgf-MhINaFDoIMOdJM2omvOqK2NKOeoFH1Z-7C_XppVPxiY-ab5Wp49uKr7Hhr4wWcHbTvxKzEOgFl4Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBdVSme0aTigCgCqdhLp-79e0282mjdQ0YqtBDDl_0dYuvv0fQtDIinKrGUf-rdGgRmSkEcvTjLmQyebNngeLO7q0zdk6MlOdeozIrrtExkpOz65I2TTe1fe862WJqtUdFVdmJC8EptWuA1OlpW9FMsqbORzqNX5aH-NgiU9peJ47lNFDZmdIVf7PXLvaHYnxI4SsFVXRtwDUWkf-4d9h1AwV33onLj--Sho9Y7WI7MSnEcIlafCuLyd1oZE9NTCLKd52ayhHQEi8X0bJRqh4LDPNG15wUaVzP89GsNn0fJFhJripG8svxxx3Xr0n5NqSdZ8dPWpt8k2pPIMmcHz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSkNICOGZux9trCTOf5X2O4KIcZU5zg6J8JBpRYsSlN7rG5AannYtVlR5Ail8XyU_NzB20O0niS1B4TklHN6Riqn-M1mouESIvbQw-WPal4MlAtO5b30fXGY7spNyyCHHMAXsDWqOOZC_jOjk_Jwo8ZTuAd6n5JuA7VPY47R3tlRSH7847qDuRqd4Hvn7TEfZIWdajPUV7DRcT5HQ5LH6D5VEgFUQJDokstS8a0biq1JUwyKlNc_rxNG1qfPAI_ONXSN_eEFigkMwmxIAlH4ZPoJEmlYN3BmI9iTpE0ZP9c0NsrKvDzIhvW97qn3GjkiVspYj8SV-DVtYkD_PCc8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی  به نقل از منبع مطلع نظامی: «
حملات نیروی دریایی ایران به ناوشکن‌های آمریکایی در دریای عمان ادامه دارد.
ماجراهای امشب از تعرض ارتش آمریکا به یک نفتکش ایرانی آغاز شد و پس از آن شناورهای نظامی آمریکا هدف حملات موشکی و پهپادی نیروی دریایی قرار گرفتند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4853" target="_blank">📅 00:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
تسنیم: «۳ ناوشکن آمریکایی
در نزدیکی تنگه هرمز هدف حمله نیروی دریایی جمهوری اسلامی قرار گرفت»
🚨
خبرهایی از شنیده شدن صدای انفجار در ابوظبی و‌ دوبی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4852" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
فاکس نیوز:‏ ایالات متحده حملاتی
را به بندر قشم و بندرعباس ایران انجام داده است، اما یک مقام ارشد آمریکایی می‌گوید این به معنای
از سرگیری جنگ نیست.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4851" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در حالی که خبر فعالیت پدافند در تهران منتشر میشه، جمهوری اسلامی هنوز دقیقا نمی‌دونه کی امشب بهش در قشم و بندرعباس و‌ تهران حمله کرده!
فعلا میگه اماراته، اما نمی‌دونه!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4850" target="_blank">📅 00:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=pbR6H5_kswqDb3SbH6KGUdcUkjgp4dTHqf4Wsd22rsA5gOOvMXTWpMsscVhju6f9OcqdU2ODXMgp3PWbU5iBhE4CyfyiaMSaMLsxah6-B5qn5e7Bo2rABOp3Q79SN8mDGjDp1cTzCltxlNRjilEF5VLy6zbWZZprepbgiy7BGy0xRmmwJjsfEO50XOhvma2npQXN8UCpW4BLkKYGBI5QDO7FNoSDXbgOzdT6FK4hAhG429U2BQFUAQ3eQFrY4CI7lqvIgnZvNAseB3iTwxckc5bc-lBMzH_NDSo3ZKbriPrALuEl3oB8vcbbEeitiLcczLa8FbQ14X9O1qpPztCMiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=pbR6H5_kswqDb3SbH6KGUdcUkjgp4dTHqf4Wsd22rsA5gOOvMXTWpMsscVhju6f9OcqdU2ODXMgp3PWbU5iBhE4CyfyiaMSaMLsxah6-B5qn5e7Bo2rABOp3Q79SN8mDGjDp1cTzCltxlNRjilEF5VLy6zbWZZprepbgiy7BGy0xRmmwJjsfEO50XOhvma2npQXN8UCpW4BLkKYGBI5QDO7FNoSDXbgOzdT6FK4hAhG429U2BQFUAQ3eQFrY4CI7lqvIgnZvNAseB3iTwxckc5bc-lBMzH_NDSo3ZKbriPrALuEl3oB8vcbbEeitiLcczLa8FbQ14X9O1qpPztCMiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش صدا و‌سیما
از درگیری نظامی رخ داده بین ارتش
آمریکا و نیروهای نظامی جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4849" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4848" target="_blank">📅 23:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4847">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
پایگاه هوایی بندر عباس، کشتی سازی قشم، اسکله بندر قشم و چند ساختمان اداری اسکله قشم ، امشب مورد حمله قرار گرفتند.
🚨
رسانه‌های اسرائیلی به نقل از منابع آگاه وقوع درگیری نظامی امشب میان ارتش آمریکا و جمهوری اسلامی را تایید کردند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4847" target="_blank">📅 23:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏صدا و سیما به نقل از یک مقام آگاه نظامی:  «به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی یگان های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
🔺
برخی رسانه‌ها از شریک  ۷-۸ موشک خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4846" target="_blank">📅 23:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
منابع اسرائیلی : در حملات امشب به جنوب ایران، اسرائیل نقشی نداشت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4845" target="_blank">📅 23:05 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های تایید شده از انفجار  در بندرعباس و قشم خبر می‌دهند،  و گزارش‌های هنوز تایید نشده  از شنیده شدن صدای انفجارها  در میناب،  بندر خمیر و سیریک خبر می‌دهند.
🚨
برخی رسانه‌ها از احتمال  حمله امارات به بنادر جنوبی خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4844" target="_blank">📅 23:03 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری‌های داخلی از حمله «دشمن» خبر داده‌اند، اما مشخص نیست منظور کدوم کشوره، آمریکا؟ امارات؟؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4843" target="_blank">📅 23:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4842" target="_blank">📅 22:51 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
