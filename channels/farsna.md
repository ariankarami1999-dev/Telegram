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
<img src="https://cdn4.telesco.pe/file/jXZIhH7qH3uKnsPcTr8K5xbUxv2O9ytnNY2ojt7O4qlfN4nqvJTr5-XO1pltpNiufIvzTkD48Cv_EohRfFz_86p_u8vDjM_53ZH_4C-2PhGDdWNHKRlDtxI5Lr5Psc49l5hA9HGPwkFV-KC-Zlw2lyjSaXlWZqE3GEgI200YkKi4rQjHzdK_mrvrdsiSB5dcmhe3yE0Izn-IdXwbXUaWsKXA-jBts3iMHLM_QnAQnqHYnWY2sE96yuFrDe9HUZiCvvwj-KZrvSWVseatDt94yFLdt8irYJ9TjcVUf8UPbHPdSBxMiB9_N-cASpqBtC-xejb41BVqEJcWQ3Rj5_YiRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 03:16:29</div>
<hr>

<div class="tg-post" id="msg-435826">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baab29a915.mp4?token=CMzv4r41SyGU6HQcuLiIwOX39R_0dg2665an2QcVPpLubxY07QCo4R17jkeScdW4uGzSx1O-0KDRg6oxYfHhi8oitG0rhEEQGDH8VCwRKaA0fhIhAC2zjlZgUjaunfUnnxk-Skq3BLNaVyKhNN-2jOm3q3GXHQzkVmUzKi1zsq7cra87BWVlEZ-CPMVFxu_oMXW0liQNLCAG56rUdGzPY8TkeHdtxCXZ8s-L2qKo61Rx6ec_MynbfSY7wdmCvSh_T57Wc3fAufL9j6y70-rb5WUh5nO1yOHxzVSu6GZaSHMDHztd3D1qNqzYFulMV4NECmTXqfnROizc_phkIH3Bbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baab29a915.mp4?token=CMzv4r41SyGU6HQcuLiIwOX39R_0dg2665an2QcVPpLubxY07QCo4R17jkeScdW4uGzSx1O-0KDRg6oxYfHhi8oitG0rhEEQGDH8VCwRKaA0fhIhAC2zjlZgUjaunfUnnxk-Skq3BLNaVyKhNN-2jOm3q3GXHQzkVmUzKi1zsq7cra87BWVlEZ-CPMVFxu_oMXW0liQNLCAG56rUdGzPY8TkeHdtxCXZ8s-L2qKo61Rx6ec_MynbfSY7wdmCvSh_T57Wc3fAufL9j6y70-rb5WUh5nO1yOHxzVSu6GZaSHMDHztd3D1qNqzYFulMV4NECmTXqfnROizc_phkIH3Bbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتادوششمین شب حماسه‌آفرینی قمی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 528 · <a href="https://t.me/farsna/435826" target="_blank">📅 02:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435825">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Fu5Q5NJ0eY4ffM5ZL8QMh2Iwe7qM4FxhFcocYA--hPtqsy4wtzn9KeHDltNzhBLgc6CqhY7AmepT4BJMcQhUHy8XeX_TsmYuNALGbW9qKqbOyAj8yAjKt0-hieYwuLxvVv9AgMNGJnpjh_MtIQ8slfUNkngf5a8CIF7GVtiXCtjICVtsuLlJ9lwj9nsehB31ZjOv9rnXa5WjKbmSAZNnFYmMF0eHCK-XQJlLxhD4ihZMTKPZtaiq_VAael3FEi3ruJ0nGZ4ZQQ6SmYRGwMSujHXRNgTCu_sGJ3HT2yLhitXxDoMrREEuZhm8T__a1zZgf6ALaije2uU4Z7rj7qYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ایلان ماسک مقابل انگلیس
🔹
شبکۀ اجتماعی ایکس متعلق به ایلان ماسک، با انگلیس به توافق رسیده تا نظارت بر محتوای نفرت‌پراکن و مرتبط با گروه‌های افراطی را افزایش دهد.
🔹
ایکس متعهد شده گزارش‌های مربوط به محتوای نفرت‌پراکن یا تروریستی را به‌طور میانگین ظرف ۲۴ ساعت بررسی کند و حداقل ۸۵ درصد محتوای گزارش‌شده را طی ۴۸ ساعت ارزیابی کند.
🔹
این اقدام در حالی انجام می‌شود که دولت انگلیس طی سال‌های اخیر قوانین سخت‌گیرانه‌تری برای کنترل محتوای آنلاین تصویب کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/435825" target="_blank">📅 02:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435824">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9a447c75.mp4?token=EH-51Cg-VWABvf_EC3wWhhSa7hfOVoujDMkaNTOs3fF9yAI2OjO-PVGMbxN6wDJ90mdZZKxWEghVUV2M3eoYDLpDUGVLfy_E7XkW3Bq6L7NvWejYX90iywgwTXBHTXovQCEptS9Q-_7Vu1cViPObOLcQLigSMtGZm7XLWciJfUh3jZ9FmBIbS3d8NDnJBc6VRJGOjBnzQtVX2nKkKagBOOsnkn-CPt6Rj6dq5PpPBtiRTDEDSypKDtj-o8cibeMfgcfoa8jq35Iv9OYV5hqH5wR7SQzVKD7a_n79zYFgwPjum_B3Ftr1ysqgne9kOr1Wdt6syfaiAj_8LZhdQTKjbjL1sh6Xbtkxxcd4_PeGmGp3uAJUUvCao7xw_OS1y0kZRvwAYOf9Rw0TWlK5EVZQmXwGaaxwpzZjzR5TwYWltlcOtjCK9sbVU7fJNQtrCtXHxg8Ula_K-QbVBhXR2T3N3bjmQVCJvPyg_5HLLLxDSJ2Ecu5V0p1z3I5Z7h_C537twLmLNs-xaagS9YwepC4M6Elh5AZ_5xQ26htJy6WpKYdhcxRxeXE1rAg4WEGox_uZpuB0q8FE5sbZKDbvnWQkWn-H1liqhbhjGGHsCfp7Gn3XNZXre08hPr2jnapfwF1198gtINvq9vT2wnmTrKD1B3zAiiKLTFujtZy-CBF60qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9a447c75.mp4?token=EH-51Cg-VWABvf_EC3wWhhSa7hfOVoujDMkaNTOs3fF9yAI2OjO-PVGMbxN6wDJ90mdZZKxWEghVUV2M3eoYDLpDUGVLfy_E7XkW3Bq6L7NvWejYX90iywgwTXBHTXovQCEptS9Q-_7Vu1cViPObOLcQLigSMtGZm7XLWciJfUh3jZ9FmBIbS3d8NDnJBc6VRJGOjBnzQtVX2nKkKagBOOsnkn-CPt6Rj6dq5PpPBtiRTDEDSypKDtj-o8cibeMfgcfoa8jq35Iv9OYV5hqH5wR7SQzVKD7a_n79zYFgwPjum_B3Ftr1ysqgne9kOr1Wdt6syfaiAj_8LZhdQTKjbjL1sh6Xbtkxxcd4_PeGmGp3uAJUUvCao7xw_OS1y0kZRvwAYOf9Rw0TWlK5EVZQmXwGaaxwpzZjzR5TwYWltlcOtjCK9sbVU7fJNQtrCtXHxg8Ula_K-QbVBhXR2T3N3bjmQVCJvPyg_5HLLLxDSJ2Ecu5V0p1z3I5Z7h_C537twLmLNs-xaagS9YwepC4M6Elh5AZ_5xQ26htJy6WpKYdhcxRxeXE1rAg4WEGox_uZpuB0q8FE5sbZKDbvnWQkWn-H1liqhbhjGGHsCfp7Gn3XNZXre08hPr2jnapfwF1198gtINvq9vT2wnmTrKD1B3zAiiKLTFujtZy-CBF60qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج هفتادوششم دفاع ملی در رفسنجان
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/435824" target="_blank">📅 02:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/farsna/435823" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPElXj-inazforfQcM0uyY67zYGSCJapYunhQqyl8R-JJfm9VPIZmmlJ8lJMDlNjIRqg3tkkjLH-O8pz5QUEhChtaaXP8uphmAU3oE5ry9whS-ga_8iDuHZGAHjZbO0kuqGVY3KEIUSAALcavtr6CVrcI16NkAU88JW235pSo216y7nAMEQX04x9FlwybrfTbEDxl6EkkqphjSPPPkeaiL1xYtqxWbSLrfmoV1tp6UqUB8Ivb5BIvytzaRrHJELYGHE85dCoikt7RhRU5KN7tSFmCfedO6x_3gtrPIeKs6N1TqAM-CYjuPTEStSHW4ZgTnrGGmHom-X28cubGb2Kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از قطعنامۀ پیشنهادی آمریکا و بحرین درباره تنگۀ هرمز انتقاد کرد
سفیر چین در سازمان ملل از پیش‌نویس قطعنامۀ پیشنهادی آمریکا و بحرین دربارۀ تنگۀ هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/farsna/435822" target="_blank">📅 01:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8920b53738.mp4?token=A9BojfFmUsLgn0LyxmbgVG35FzO_fnM65EzbVVbRH-4DMl4XWk-Gv2xVGC0MUaCQX8wXPrYL-IePDODx76pwJj_z5VCsTmjXcVEE3r1HsOGk85BksP62EZ8jOFEUrTADAz3UnVFJtEvkuYa_c_LQwVWQjzkH3FYiw08z6WNcNdScls0r5J2OzR5XqLzjJFS3VKg2ORDElMAICEz_9h0gFnWe_saAQmNeqfb3crnXohPoU1xXywWZQJjjuH8Y8sJAcb8FNVjl_sIHy0D3CuDHhpcQ1xHTp0lrewHIW250DMn94nOMaKwWoVi5YsIbjRjrgoj1qWuiZYQJpWTZ7pKKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8920b53738.mp4?token=A9BojfFmUsLgn0LyxmbgVG35FzO_fnM65EzbVVbRH-4DMl4XWk-Gv2xVGC0MUaCQX8wXPrYL-IePDODx76pwJj_z5VCsTmjXcVEE3r1HsOGk85BksP62EZ8jOFEUrTADAz3UnVFJtEvkuYa_c_LQwVWQjzkH3FYiw08z6WNcNdScls0r5J2OzR5XqLzjJFS3VKg2ORDElMAICEz_9h0gFnWe_saAQmNeqfb3crnXohPoU1xXywWZQJjjuH8Y8sJAcb8FNVjl_sIHy0D3CuDHhpcQ1xHTp0lrewHIW250DMn94nOMaKwWoVi5YsIbjRjrgoj1qWuiZYQJpWTZ7pKKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایلام خیابان را به میدان اقتدار تبدیل کردند
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/435821" target="_blank">📅 01:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fin4UTIaEU-hanZG6pvix8IJhoPby7d4-f2Mogp4YzH6Nkzq396z3w_rMic8eDFSOn_ioExrWBobOdAqUGavGoOXE7KWfbZGKurvFSyljz1zDjCJyp3pGIVFt8H1GHWq7MfPZc7V_hecdq_vtP9mM_8tosIsjuhYw-UY-BCEUnIK2KZ9uNXbwXPsaGiA-3ZN0xcUZ_kJ9JbQ9uZqLjSJp41D7hv2xp1qQkNsi8fbdamEYzgiCITSswyGlG7hbuT2l0nAmsRibp04c4SWMxDS5MWNHOtZ4NOxIIXUnG1Pge2xsqjr2qiGeAKaSthAizSso5qSaY6mtHn2tvRWx1vH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته بودن تنگۀ هرمز برق کوبا را قطع کرد
🔹
صدها نفر از مردم کوبا با حضور در خیابان‌ها و روشن کردن آتش نسبت به قطعی گسترده و سراسری برق تجمع اعتراضی برپا کردند.
🔹
کمبود سوخت عامل اصلی قطعی برق در کوباست که به خاطر جنگ آمریکا و اسرائیل علیه ایران تشدید شده است.
🔹
وزیر انرژی کوبا می‌گوید، ذخایر سوختی که روسیه به این کشور اهدا کرده بود تمام شده است. وی آمریکا را به خاطر بسته ماندن تنگۀ هرمز سرزنش و تاکید کرد که قطع جریان نفت ضررهای زیادی به کوبا وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farsna/435820" target="_blank">📅 01:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rktGFbw1C6weWAq3kvvV1Vbq0UwHPFMBoGwQf8f5wHvwd2_lHDTWxzAqiW9YbCFwAT8DYatzmX2tLz7c1H3hpzHM7rr2AYFHB2gBzYXTAxacpKqQtGlefOHPURGAWrobRivPvfiz-s8zyJk_mjzBvvCgNDQTLe_rqihrBHJo0jPWA4yvglBMgk91pxVFJdprXR_hyZhQwBvl86ZsjvAL9XHSfMXTHpUTuSyrrL9KdbRpB57P2RNaGJ3KcYsci75PYej7ec4dvtAzH3XuMB2wI7uRXQmARBeAsnQvYkG9dNSA2iLVR4_RY77peWtNbYOm4O8YVMWjrOElo7CBRxpzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز یک قرار تازه برای تعیین تکلیف امتحانات نهایی!
🔹
سخنگوی آموزش‌وپرورش روز گذشته اعلام کرد که «تا پایان تیرماه صبر می‌کنیم و اگر امکان برگزاری آزمون نهایی فراهم شود، انجام می‌دهیم». تاریخی که تاکنون چندین بار تغییر کرده است.
🔹
اولین‌بار سخنگوی آموزش‌وپرورش دو هفتۀ پیش در حاشیۀ نشست خبری‌اش زمان تعیین تکلیف امتحانات نهایی را نیمۀ مرداد ذکر کرد، اما سه روز پیش وزیر آموزش‌وپرورش، این تاریخ را نیمۀ تیرماه عنوان کرد و حالا سخنگو، پانزده روز به آن اضافه کرده است.
🔸
دانش‌آموزان می‌گویند که در این شرایط بلاتکلیف هستند اما مسئولان آموزش‌وپرورش به جای توضیح دربارۀ تغییر تاریخ‌ها، می‌گویند که دانش‌آموزان به جای نگرانی، درس‌هایشان را مطالعه کنند تا زمان امتحانات اطلاع‌رسانی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farsna/435819" target="_blank">📅 01:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435818">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff319359.mp4?token=XO1OducE_bBz9gme5wOqObEXiYnzaRGSXrtkE8hGteO_FGRcg5jNmrEwYja5MZ-2uT4ZpPPS4-72rgrLUkzTONnUT6IhiRcb9-YNJbOX_BXiT1lZccQLiEO0LThTfBgYnBs607PFKrkNUPn6JXwtd1I4opy7XwuMSjE-ZP81U_9nyW9CaoI9LIxJ55uGMM2AWO19jsHDMRdLyz_1V7XytHUjXZcX2bWlpa8RcBW0bGgJd26heozZ1LEzxE0_eCqYVCNAdN8DnTi0a4HQcKalpsC5DYQzf40c08cHxv6KADShZUPtiaWgryMA-a6sJeyqum9bwi52R2IQeQUV67UZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff319359.mp4?token=XO1OducE_bBz9gme5wOqObEXiYnzaRGSXrtkE8hGteO_FGRcg5jNmrEwYja5MZ-2uT4ZpPPS4-72rgrLUkzTONnUT6IhiRcb9-YNJbOX_BXiT1lZccQLiEO0LThTfBgYnBs607PFKrkNUPn6JXwtd1I4opy7XwuMSjE-ZP81U_9nyW9CaoI9LIxJ55uGMM2AWO19jsHDMRdLyz_1V7XytHUjXZcX2bWlpa8RcBW0bGgJd26heozZ1LEzxE0_eCqYVCNAdN8DnTi0a4HQcKalpsC5DYQzf40c08cHxv6KADShZUPtiaWgryMA-a6sJeyqum9bwi52R2IQeQUV67UZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانم مجری شبکه سه با اسلحه روی آنتن زنده تلویزیون
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/435818" target="_blank">📅 00:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435816">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
پاکدشتی‌ها: حتی در سخت‌ترین شرایط به آمریکا اعتماد نمی‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/435816" target="_blank">📅 00:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435815">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfe7XIzst-eMOjIxY0hz31czPyp3waMMazChk6Bomlr8ug5J0ELQEa1FBgTmRkO2Wylb8FhglMuXZ7B-atD55i0kJypl-u1XZYuGMx9RcKK-LabiVsjPh3j5Drj9DKJfXHAMQELaJxW45IGq0ubRQWnwtTZ8hnKsMwikbRECzYknyMl0L_XjGebHdO3DEd7TXtOQSxtT5vvskkCYN5SylruFN_Y1OGnQs-tnvmJa7nlJFukL89PuGRoXxKnXYosVveu47E8B-ScLUVaMMLDP0KAWiocsEbp4cd-rx9k3QJkh3SGRr7_XlNOJ0kNwJSKUGzR_AKaDXFJu5JTL1XUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به تبعات جنگ ایران بر اقتصاد امریکا
🔹
به آمریکایی‌ها گفته می‌شود که باید هزینه‌های سرسام‌آور جنگِ انتخابی علیه ایران را بپردازند.
🔹
فعلاً افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید.
🔹
درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.
🔹
همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است.
🔸
تمام این‌ها قابل اجتناب بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/435815" target="_blank">📅 00:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435814">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
حزب‌الله: با یک اسکادران پهپاد تهاجمی، تجمع خودروها و سربازان ارتش رژیم صهیونیستی را در نزدیکی شهر ناقوره هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/435814" target="_blank">📅 00:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435809">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pP4c-xSBttTIVk7AAVdmZYB2LQADwaSI2SxMK1XUyJXA68Jk6z0nTJi6HR7J50fhtpOez-jE4-d7bdasOTHV2MS673Rlnfx42dj_IVFbAlT2pa-iuUQ5k9e1STMuaN2taDuvgLzfA6JCg6tfSBQjjbmI5m3oBP5yrcf8AOnMDcRxCExNbPLVsDGNihAlgElWl2DOe_L8t317xNNmQ1w2CZxOcrH2pHC3q_8BKBFioF4WGuG_4lGWM7B3Xnd6gjHT4qkrytzyrCxsy9XDstdydaxCIjr-uI0E-QsQJjVRof4pSxNM_MBCEJfSTeiP-DLJcvecSq9F7ZfOONg1JgDMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiCRHke-4FVeZRsOdhaHVeIAeMhe4Ry63hYPITnhrqL9qYuF4yPvEV0vlM7LG_2ipJdY4PzhkQtvmIabtKs4wCYRP4T8tpRV5MvR7pmfeNg1EAdfIE7Xgr8_-Yy10ULaIoqnCCgA2jpKJSK2Dal02hQ1Yh3HcKwzEyjhQJRP-GEdl0iLIP7cRsnNKUl2aReMw_LMfuwS-rghvAcV70PKA3TmuUQDDl0_Lw5HN0ytKzXrN4d6bckW-kZArSL3N0dr9_ozYA--6rvKsdWvAeKlXPj0dBwJdrQV1PPizzVfOrF4La_br2iu700_D_kTvtsDtw2zIxmVmFAxT3Z_HSfJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8IO1_BXExp4FVK7_a62PiSGvNZt48UmyBwW7-UDpy4W74oB9XFc8CAb7V-csjE1RL-w0L_tw1b1PDtss7dHhOBdngKelAFP3M4KdIXeEqlbCTrcfqbtni7VWgv5u_P9VVmvO-0n0TYpK0419LQazZ8mrC6efkKrjy9VQ34R68gSWbHcjXw15xEwzH-A99OR4ZBhlxnz_DXnxxlEUN75bd9fJ_W1fwn6UwpXvQaqoFrXzJIPT7gqeqaf6e4AubhTbLucJtPooM1gkqsFhRIBWk2_BadSzYtarVwBTDZznFFOpJ0H0Iba04JSa1PYgglTQwiDZrNdSrR59UB1ARZNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXte61syjCbwHBjGRGIs1K95dMXBTA57xhLoIoTPLT5d-bzwTDOG-dGiLCB7_lNob6Q6VUsMoAdFvUpM4BvK-oAHh7rupbPTDv3MN39xQPqJgkTUEbbC2TOuGpPRAdEhS8wSh_PdwJzvKOdV-9jsQxjU4cPuv7imYabPNvhPVPz7_VxI48P_D8Nvy0BixxhgC_9FQLYBxXQFdgKUNS3H2DDxYCG2E_npnfiYgdUcdJ_lUVBC4A74vI6tMboZk8HYolDoP0HIm1TiG3QN9r8OZ7WlstKV2jc64pIe3H4LpiFZQIdJds3uAp_FUXDDlkG_f4DdxNG9-rohbs0A3AbNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yp3Tge9Nbcdim6H7PiKzyUeUBuEm2tk2qbS8dcLxkI2hvX3E4xpU3pVA4OSEGlpZLg_ct5TA4Ihy3CNg50yZLBPqdZu4CWTvnjYzPQCXZ5M7kx4T_M_XXSzPbnn6YM4f46xi9gNW9rhGtwbNZOB3qZuWhRUKRf8o-8fG6Mfz0y-k4E1nWRkvOWLPZxSlyqXpXj9kwqegpj4OoZNqgiz4jJ_xv82GJ7PNMYR65ppIsIlahBy53bfG7_zuGbSgt1jd7a0USgmmSa0WH5sr2FbejSs-L9rZ3133i2hPyahGqmmpp1wlSRR6ElfHI-27_qTqz-lgRn5VO1E9qNzXsShF9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۶ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/435809" target="_blank">📅 00:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rm-8dzJnDu66yHEhyGUMmCmEp-2sqQHDFukHg-YneodEtm3qXnmUlBNO5yBaRrRMnTuOZHtVHfUfyF6GDzKvfaL_i8xKk2qc2-ATQETR3OvnX1E4bM9pPOobMNGosd3KyP4Qkdo9qXeyU794s13lRosTJLlaDXrKSa8HTz3_1mW_NEBlFY_vPgVNVagxX7vBG6TLfwFY9CKd0IS7CES_-Aor-RIhWhsCSY70DU_pLnJVzpTkW8ayXtSkhyohOt1vstyy-Z4jKhcs3gI-5O1lgdqMUXA8lIAXmuqi5yrYah1HsqDLbdTukaEKH75wO2Z1MpidvS2uJ3AzIInWTKXIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOJiim5OfguloUJYzsAq9Mxtgsj10SqqgR6sVMIqpoqsJTpmIB5Ip17h_KQMlUeiE-G8aqPVV8Q6pxiMKE6TkauQUE12NhUxf96as28AUGc1PoEdA3HYGEMicrH0wh5BL_QH7OiyzHrEBn4LnrLR_jRSQcW5Q3xMpL5o4zyulSPAJSXx5MbidHKpEM99PMaJ7_1LoKk7EzSrWZq9oj2eTLg25XKVKDnhmwJcW_kaGWoMnx1xlVCAV7XQRLMMfiXu7iwlDVRVzbvFjPg8w1ZBYqK0j-cGh_xKLI8ZXdpA3v-V3tft_4GvZ8Ngk6jZiAusOJxG4NjSxCkjrVWHomY9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGli6Alkh69xnXZuPlSspmo9eh2cDiNwQYsNnoOiL-Z1d_hGTfWXZIQNimZemmEA6WgXu9r8HHDNVnEalDqX68t_gYz2a-Okxik5h4nQJoGHG_eawdmVqp5hAegm-mZBCm-78d8o7rdJYCv_EMuw93XWYEqMA6i0P_KDbKwPie5blIHnEOm1HZ1fPvplXHUDugnyHLsiBctNiwGwrwO3Zt77ZJ0Eivfk6IrxRB5HJ8_fxq50elyCrv9ypL6cKknadJ0V-yEmwsZ3kj97909Ypd7MO8LVsnZh5YloPAdvpm_kWVcgROCSV17_dpxxe863QO1u1AOP7MVT6xlH4Wk6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzdABEUr1LeRRY0q5rZ_97_oMclNApqtAvRyUVN_34RkpJaQQFgzn-iL7IQcu0nGyx21SyVAWHEU_79ti2Kid7GhY26ToxmN895N7liRnqNgjXYw5Mm1tRRctyf9YbLOiyxfh3w9u9Qj9jkwNVnHx4m_M4KIVs7_XDTdsPeJ8vSoVSB4kpIot2jVerJjPJhGeh6IIK4cVCX0_iwxNqhqvfhahDF2DFkbeNgWuepjZUZ7Op4YVixVU6o7zCXL_SdMaPHLW2HOfETy9k8J9IfKPUWEpaMomcJBRYLn6CmkfLu0jVj9zt2ukwjiJycUkH034y4UMpk2Vo0qT-7fyGcI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmTuFS1W_fUQjxf4OLrPgjV90Qd7WTi2_8u1h0u4-PqKX4iEWZPd52PQDxhk-CkJSrYM-G_BVpnaNRuBOM1aRaj_MnjrI2E99K3l5vHvuB8H_tT0OGRhImeVW0bIy3SDSHuN8VcNy2FMQf-tTumVsI1z5IxS7ihrLC1UIWPPBVynlYvR7nxTAR2Y7pl_S7ptkk4qCTC0PKfwChAKlP-SCPijuLfc8tgYXQhk-XyH488KDILFu-b_aGseOXuJPOQcM1J-xUVYCOErKshWDHffM19_6leNLB6hMhRN4wuHROO1KkofGrLBqCMEsF4tEpFbplygGu5T0qq8Zq8juAv0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAfH5zHJEC0nz_2Gb_KptU1ru14GVxsIG4s5LHeiCMuCEK_NWcshSHX9UhEGLOI5AoF2So29ssSMvTSKBPSFKDBMri1x8VFAhCHh9glsnoti6FqbWIN6ZM3eu8NwbeZcbTFaTcon53qdSWcOOwvblWJCXdk_RDpkzrjBdKrmWTwUF0GVZhmRVnoWZr4SS2N4pCHCSIw6sTYntjlrmUfcnZ3idJ4KjoMUcNXmyF3Z5-uZn5PU_3bhtgYT_yd_b-yxgBQ21IpGEf_9fw6fK-4de9VqUYbFvcZ3F-ZWIaT7oIz2j8BRfNnMxGO9F8odSareUZfMFYBOYUKNaaAkumjG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_Jg6ZjYk2Tw437sLXGfD3DXw5Q5hREm9OiEKE6xqyBoLihAQEm8Nf6qy5tSkReh3BbVRjPoaG4M0-aQRCn-iYdH2oWjrjCKr5yL4RvNQuif5THAzIfnUJBugUPDrFHHeE7JRE1bZiFo0_2e_xc-ndmNNGgaQ_37_h-s3Y-mot3Q8gDk3dqvsXCc7rt7rk8LPp6CGRQr8S4fNSZOAkZChFcJlwCxYCKvSDp_914S2M2AWRGeOPMzeCLaJXWrTGh46GoAA_FlAYoUoWoOpVoLMJsj2vaBOICNpikto8iYqrNs9LtIL8rPoz7AqWWHv8yBe3QKI-L2wB-b2aROp0gr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTD6_u5wnIN1E0stb0i0n6uzWt8xlm1YaazgDECLyhSq5zwl-Nvhjw6fsjvB6jOaYsmXImBbY-FpmSBpJQccvMIDB8jg3RgoeJCAWw5CQCiSxw3l9dHVlPhhLitRVvZtX698FeZcyHXwXN9zHlSzMHK3KQZPUAqDPP7QE5YYDG_-ibm6p5ksQnybkCYKx640VAbwQoKwefXvqRR661nrWC6Mu1kVsHQEjEfh396LhAJcJsQqHk7qBfMcH2ec2f2ZPoUWaiJXNQpfSHzS3R8V-xsIkjmvTXD8Ak_woufJVMrESxF9U57QcEILUBSSe3BUUqpzPt10bLjaTQ3s7wGXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBymO1F5USnVqEi8Sh-BQWpl0a5El4j56yokvSUrIbB6J6j48UiWa2ESRiMJaik0fa87-y41D46j4WrMv2MKBzvTBSoRlcQuZvlm3vX4v3-SXhK2e6JFEntH-Nk3ml3D-arP7aS8Kv-MvN_64GYpeg9CEjSSiqbC4RBOj-auHySYhFnGvExs6trsidED8OFqBvPzkFw-As3uWCMWfU1lQaDRM7t7mZ1rdnouN7r-T_jGhDXHoSOcSbAO69TvzzzLUrfAD3nbjqkSEHpWsnoepF07w4qZaQZlW95oFCP3GKXtEXl3BMFNT0syCOx2cEHSiGfTQ8Xd-HzMsGTNBCELOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mknBmLoZqaC675gUP1_Rw7uRFZpDBZvtIa3iM4oYv4nOjQKAHFF8CpMUN0CPokH9F1OwIy5Zjg0PoiYYQ-AzPhm-mGVw1wU-uocV3AmA4dG92leMuadvZN55jwnol7WJvl2vYIfFr6_zBV8wGGAk5m8kam4dUiahrlUrc0rPB13zs6idGKz4BN8RhzsBcyAeB5jifP3T8l_B3wIL5arUfvDwWddI7jQc-jStEGievtiS4jcUrYSFjhmLzPRLYPiUZBsGOECNI7_IxnpzVlvFNR9d2ZIbFvbuq4BZHRPUzr7_fG6wyXnyPhPAsW1fQeeds6oLM6AN8qPcrCfpVLObIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/435799" target="_blank">📅 00:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دومین جلسۀ مجازی مجلس یکشنبه برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسهٔ مجلس: دومین جلسۀ مجازی صحن مجلس با حضور وزیر رفاه و با محوریت مشکلات معیشتی مردم و پیگیری اقدامات حمایتی از جمله کالابرگ، یکشنبه ۲۷ اردیبهشت ماه برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/435798" target="_blank">📅 00:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4b4be486.mp4?token=eC7PBmMsKnpwb5PJ5QxIUSSsmj-kbNHyMQlx4sWpkW_j1NkDlD2icOaYLCZRjlL8TmeFFfrjRozN425FB0OjI926A38FqAG9ac6hoMDRKloPtkA_iNrNp4cDcHxOxyoSDKg9KKoATYotbk8hPyAjiKxTcsBzVu66ur0G76V7EfU6BR8cnldJKM4Cp3gLpiB48XdSvHHuyLHgoppRKyAxXFQrmiKy5G9fUTbhTK3d-LtyUOTCHkXKY2EtCi3G0JCja_40GzIM4DyoorJANk6cB41nVoT-k9yXF4unDypPwtfGDw1b57qg4_pKQtshf6tQKWJjmNKiG-vZ1ipesFh_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4b4be486.mp4?token=eC7PBmMsKnpwb5PJ5QxIUSSsmj-kbNHyMQlx4sWpkW_j1NkDlD2icOaYLCZRjlL8TmeFFfrjRozN425FB0OjI926A38FqAG9ac6hoMDRKloPtkA_iNrNp4cDcHxOxyoSDKg9KKoATYotbk8hPyAjiKxTcsBzVu66ur0G76V7EfU6BR8cnldJKM4Cp3gLpiB48XdSvHHuyLHgoppRKyAxXFQrmiKy5G9fUTbhTK3d-LtyUOTCHkXKY2EtCi3G0JCja_40GzIM4DyoorJANk6cB41nVoT-k9yXF4unDypPwtfGDw1b57qg4_pKQtshf6tQKWJjmNKiG-vZ1ipesFh_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایلامی‌ها، همچنان در سنگر خیابان
@Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/435797" target="_blank">📅 00:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRIswPBxkyMhNcKilO9JZ2lgAO7rQHAq3g_95w9Ib-00CWnxKmLSsIsk8ZbDYeeg5Cj7OP-tPCmrNiN976LBj6Yg1VytLFGmQiIP8yTslJ1JAzPuUdUG4WIu4FQvy-xB897LwBpb4rjKD1Hyyxu5L4ct29rfYbFQfYbiIQnj0y3F5OxDyWjf7r2O896ivtMsyIToP3GhcNYX6-D2eo-z8WuyfLt3BtvG28SP-a7lfWpFG7Ge2WYdfbKBpNtVoFSAIV2lM_ivBk-6GR4hw26eIygzbScaFi7zxBsktlRs2DNS6s7Mx762prBu8HoNTvQrDClY_nCX87jNVaGbz31LoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاعردزدی
🔹
روزی انوری، شاعر قرن ۶ هجری، در بازار بلخ قدم می‌زد. ناگهان دید معرکه‌ای برپاست و فردی ایستاده و با صدای بلند و شور و حال بسیار، قصایدی را برای مردم می‌خواند.
🔹
انوری نزدیک‌تر رفت و با کمال تعجب شنید که آن شخص دارد قصاید خود انوری را به نام خودش برای مردم می‌خواند و تحسین آن‌ها را برمی‌انگیزد.
🔹
انوری جلو رفت و از مرد پرسید: «ای جوان، این شعرهایی که می‌خوانی از کیست؟»
🔹
مرد با اعتماد‌به‌نفس کامل پاسخ داد: «از دیوان انوری است.»
🔹
انوری لبخندی زد و پرسید: «آیا انوری را می‌شناسی؟»
🔹
مرد گفت: «چه می‌گویی؟ من خودم انوری هستم!»
🔹
انوری که با لحنی طنزآمیز گفت: «عجب! من شنیده بودم که «شعردزدی» وجود دارد، اما «شاعردزدی» ندیده بودم بنده خدا، آن که شعرهایش را می‌خوانی انوری است، اما آن که اکنون در برابر تو ایستاده نیز انوری است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/435796" target="_blank">📅 00:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6e8c5970.mov?token=btgikUhyo3ds6lPnrBAwD7ZUHLSOzoLMNSfZzQ95xylgGyFPUHt1OBQcKNDQvxImIj3Fq6VlKi01WciA1udrYyHK6ueO2CWfBj0CuxbbQtLz5EVfMH5jiq2xpZyc8oZZ5bFgyHuGWEnvZfgt6v0lrhAYTX_of4_jxnxmnvuKIHie1VB9IStuekVLeBhwt23RKO5fkE0UViirClvQF8goZhNfJxbvTYHbrJyLzwG4V0jy7ULOHFwSZvgGBB7rPRiuutgz6w-XAU7znSSsc4zg7RCD9DSvGSkHhneheHGPq7ivr4dPnDeW2bZbtpusZsj-f_pvmJMEYoROlnUJ14taIIOA3jRgfiUVKOPPFJjZuF4skjfQqneX2laa4kWJgxRu-7pdx7nE5e_cTYLu581AMkEVNKZrj-yugEXsAGvWS28qpas2n8CARFqsnZEGTnJR_PMsuLin3M-M1tC28ZJhfUkYrDeYQTgHpqaZRqrxDQpMBW_O8yoOoU04heTYUGzoWRQq-E_P12SEqKNWh-hMouqwgp6sJdIGCx4oLl3uQe_eodVtqOM8NxnGWHwqCzHf3MCv__4TYIgdWUEjYJskJUE7tCvfQEkgXZYJllWNW7d07PdZcMiUR9cS1QchLe_3PkyyWLDPbWlhKquZp0E9WK2tcMcwLgcxSTznpSFLMzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6e8c5970.mov?token=btgikUhyo3ds6lPnrBAwD7ZUHLSOzoLMNSfZzQ95xylgGyFPUHt1OBQcKNDQvxImIj3Fq6VlKi01WciA1udrYyHK6ueO2CWfBj0CuxbbQtLz5EVfMH5jiq2xpZyc8oZZ5bFgyHuGWEnvZfgt6v0lrhAYTX_of4_jxnxmnvuKIHie1VB9IStuekVLeBhwt23RKO5fkE0UViirClvQF8goZhNfJxbvTYHbrJyLzwG4V0jy7ULOHFwSZvgGBB7rPRiuutgz6w-XAU7znSSsc4zg7RCD9DSvGSkHhneheHGPq7ivr4dPnDeW2bZbtpusZsj-f_pvmJMEYoROlnUJ14taIIOA3jRgfiUVKOPPFJjZuF4skjfQqneX2laa4kWJgxRu-7pdx7nE5e_cTYLu581AMkEVNKZrj-yugEXsAGvWS28qpas2n8CARFqsnZEGTnJR_PMsuLin3M-M1tC28ZJhfUkYrDeYQTgHpqaZRqrxDQpMBW_O8yoOoU04heTYUGzoWRQq-E_P12SEqKNWh-hMouqwgp6sJdIGCx4oLl3uQe_eodVtqOM8NxnGWHwqCzHf3MCv__4TYIgdWUEjYJskJUE7tCvfQEkgXZYJllWNW7d07PdZcMiUR9cS1QchLe_3PkyyWLDPbWlhKquZp0E9WK2tcMcwLgcxSTznpSFLMzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با هر حجاب و پوششی که داریم، پرچم رو بر زمین نمی‌گذاریم
🔹
شعار امشب مردم در میدان انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/435795" target="_blank">📅 23:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435794">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
جشن ازدواج متفاوت در شب های ایستادگی مردم مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/435794" target="_blank">📅 23:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">بحث در دولت درباره افزایش کالابرگ
وزارت کار: مبلغ باید افزایش یابد؛ سازمان برنامه: پول نداریم
🔹
کمتر از یک هفته به شروع خردادماه مانده اما هنوز خبری از افزایش رقم کالابرگ نیست.
🔹
نمایندگان مجلس از پیشنهاد افزایش ۵۰۰ هزار تا ۱ میلیون‌تومانی رقم کالابرگ صحبت می‌کنند، برآوردها اما نشان می‌دهد، دولت تنها منابع افزایش ۲۵۰ هزارتومانی رقم کالابرگ را در اختیار دارد.
🔹
سال گذشته بود که سخنگوی دولت وعده داد، خردادماه رقم کالابرگ متناسب با افزایش قیمت‌ها بالا خواهد رفت.
🔹
اخبار رسیده به فارس تأیید می‌کند، وزارت کار در دولت، افزایش رقم کالابرگ را دنبال می‌کند اما سازمان برنامه مصر است که «منابع لازم را نداریم».
https://farsnews.ir/Economy/1778872819925622102</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/435793" target="_blank">📅 23:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gei7SkgW78NVj8aTyF5UhVZzoLzAAKGbb982Ricom3M5jATJG68XPEEY46RLmKHb6zm-zuzrisa2XiqcZ2KHSdXW_yQCtJzk53knhF8n88J8oPtKFaD8oXn45HB4kLbpWENllEsb9tkKzxwRNCpOA8r2aL43fTpAksU_flsVS-7gwhI7Z1C33zHy_T4PuEYcXR36PXJuku2ik0yjeqDW4qJ3jtk6LqyCdqkBCDJmsbwh1sVk0URn2IThK5M9IiUX7_jGpHsff2BWNt7437hWnuZ3EvfnLLr1O6jgDBw0hC7jw_1iYwh8P10-p7utvwDAsoAvJgd9mXtxn4l8-97-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ هکرها به سامانه‌های پمپ‌بنزین‌ها در آمریکا
🔹
سی‌ان‌ان:  سامانه‌های نظارت بر ذخایر سوخت در پمپ‌بنزین‌های چند ایالت آمریکا هدف حملات سایبری قرار گرفته است.
🔹
هکرها با ورود به این سامانه ها ارقام نمایش‌ داده‌‌شده روی نمایش‌گر مخازن را دستکاری کرده‌اند.
🔹
کارشناسان آمریکایی می‌گویند این دسترسی به هکرها این امکان را می‌دهد که یک نشت واقعی گاز یا بنزین را از دید سیستم‌های نظارتی پنهان کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435792" target="_blank">📅 23:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
منابع عراقی از حملۀ پهپادی به مقر گروهک‌های تجزیه‌طلب در کردستان عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435791" target="_blank">📅 23:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435790">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیکر کوهنورد مفقودشده در الوند بعد از ۴ ماه پیدا شد
🔹
بهمن‌ماه سال گذشته ۵ کوه‌نورد در ارتفاعات همدان درگیر بهمن شدند که جسد ۳ کوهنورد در روزهای نخست پیدا شد و یکی از حادثه‌دیدگان هم به سلامت به دامان خانواده بازگشت، اما تلاش‌ها برای یافتن پیکر آخرین مفقودی که در زیر برف مدفون شده بود پس از چندین روز بی‌نتیجه ماند.
🔹
در نهایت برادر این کوهنورد با یافتن پیکر وی به جستجوها پایان داد و با تلاش نیروهای هلال‌احمر و جمعی از کوهنوردان جسد به پایین انتقال یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/435790" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435789">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6IT65qopxy3Geh3ggscYnMR8iOnxAuedi8iT-EE2_2fFl9fkuLC7Q3NPN0x5MyaHvSGnNWtwcYPeaUKK001ZvIcUra8q3HWbE0g3Ebu9wcIp1aaOU0ngTwTcRPPUfjIWtgOnaJKqAmAI12TPytuHFtdsuWj5_qr6PJhiFPDHhaEu53TyltyfNkS4ThZ9lHMRF9NWBZO-nnpXMSyCOHtdTfR-mXcJX8zZDis8-61nJGTr9zSakqAX6z_y4ZSNDAVVXAaEZwAf1DQujdmHHtm4wEjzbQ2AIRIZul7Pl7oa9-Z_nG6LoUUXaCjvkytrWA4u2Mx0w8dZhW2MOJ2mPdVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: قواعد نظم جدید جهان آمریکامحور نیست
🔹
رئیس‌جمهور آمریکا نه از موضع قدرت، بلکه در سایه سنگین ناکامی در جنگ با ایران وارد پکن شد و آنجا را ترک کرد؛ وقتی او برای مهار بحران خودساخته به نفوذ چین چشم می‌دوزد، یعنی نظم جدید به سرعت در حال تنظیم قواعدی است که دیگر آمریکامحور نیست!
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/435789" target="_blank">📅 23:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435788">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3c36794a.mp4?token=cjrKhdHj-s1LSJJY7B-K00LVgIDRGNCPkSPMYcXcadt8n_8knVsUs8SEyv3lw2zBdhuaXiuypCNZb0Xv07bXpGFt8TN09PN7szV_I4W8xBuGlN0r_MdLpTt_4a4ZObdLU_ayx0GZ6rqRYsxXqRLKc-4CNlpVS6dZLdMkRe5EUvwshd2KjkesA_Q50cmDUSyYOvEDBg3RPhb7tYNM_nFXi6PiybXqQdph-I8BwnjfjFphA-w9Qg7k0226Xf7VF3ZY1_y7yq2MRTbuxCZNXQBHZ7eB6Qg8XIc19JEjoI602lloRPg-laoTm4BVREMs9iwc9cXtSyqRXOwnv5lFbl9wUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3c36794a.mp4?token=cjrKhdHj-s1LSJJY7B-K00LVgIDRGNCPkSPMYcXcadt8n_8knVsUs8SEyv3lw2zBdhuaXiuypCNZb0Xv07bXpGFt8TN09PN7szV_I4W8xBuGlN0r_MdLpTt_4a4ZObdLU_ayx0GZ6rqRYsxXqRLKc-4CNlpVS6dZLdMkRe5EUvwshd2KjkesA_Q50cmDUSyYOvEDBg3RPhb7tYNM_nFXi6PiybXqQdph-I8BwnjfjFphA-w9Qg7k0226Xf7VF3ZY1_y7yq2MRTbuxCZNXQBHZ7eB6Qg8XIc19JEjoI602lloRPg-laoTm4BVREMs9iwc9cXtSyqRXOwnv5lFbl9wUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برنامۀ تیم ملی در ترکیه و سفر به آمریکا
🔹
نبی، مدیر تیم ملی: ۸ خرداد در ترکیه با گامبیا بازی داریم و یک دیدار دیگر نیز برای ۱۴ خرداد برنامه‌ریزی کرده‌ایم که تا چند روز دیگر بازی با این تیم خوب هم قطعی می‌شود‌.
🔹
تیم ملی ۱۵ خرداد عازم کمپ خود در آریزونا توسان می‌شود و ۱۹ خرداد هم یک بازی پشت درهای بسته مقابل پورتوریکو انجام می‌دهیم.
🔹
تا  ۱۱ خرداد نیز فهرست ۲۶ نفره و نهایی تیم ملی را به فیفا اعلام می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435788" target="_blank">📅 22:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435787">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
باران شدید هم مانع میدان‌داری زنجانی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435787" target="_blank">📅 22:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435786">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb304da96.mp4?token=TmaxgL3puo8HFZKsTBWvY4DEGhpwkXxdYzlBxl0mxywTeG3H4EygPzmsdWlbIuJI2XP9FNuCSrqZ4BUihZu5V1VStihR-TaV-Wu2BDyZCfuZU8zWZcP0AzWlLBDM-Uv7AFDzPu9Nm06cVUFgIKwIuCsl_npUaxvcfn_1WxIuaDnDW6ivP2s9umJZllE8ego-91RosBMQHwfIo55hkdwRmt4iYiS3PPFVp-vzKAjVA7a5Oyq7zVZJrAJRQNoQWXDr-xhwoK3iD73EGNDXB_cpBAbFULsWu-rilSMM3QHoNy2FX1sgucLxKUUV5gOERy-v0uTwoUROi59hhXNOj3tezReR9zst2sJF4H-aIELeoGuohIpwE6Op7zruj4UE_Hru9cOA-QpioplInv5lQZOA8alfYySVrsiDjnz0Qbq5Lq173x0EVillPC70szWhq5XNKi_unSMYUlGl6SN-hinpeUASOIDt9GLRM_jXxI2PKTq4t0V5R6T6f9hyDjRovkIucoL95VwYjLtLXbkZP9sWpy6Ew0cfz41_b2T6csfjmTVTdyoUER1fF2h1SOu5EAyzLMSx-P4p7_bSV0rdMptqdXXAEpvHr9JzCYihwZZMG3aoa4ni4_9l9aah48OqDy0P54eopCV6GUAlaKDuJgPxV0VipXod-eZiAyel4onlMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb304da96.mp4?token=TmaxgL3puo8HFZKsTBWvY4DEGhpwkXxdYzlBxl0mxywTeG3H4EygPzmsdWlbIuJI2XP9FNuCSrqZ4BUihZu5V1VStihR-TaV-Wu2BDyZCfuZU8zWZcP0AzWlLBDM-Uv7AFDzPu9Nm06cVUFgIKwIuCsl_npUaxvcfn_1WxIuaDnDW6ivP2s9umJZllE8ego-91RosBMQHwfIo55hkdwRmt4iYiS3PPFVp-vzKAjVA7a5Oyq7zVZJrAJRQNoQWXDr-xhwoK3iD73EGNDXB_cpBAbFULsWu-rilSMM3QHoNy2FX1sgucLxKUUV5gOERy-v0uTwoUROi59hhXNOj3tezReR9zst2sJF4H-aIELeoGuohIpwE6Op7zruj4UE_Hru9cOA-QpioplInv5lQZOA8alfYySVrsiDjnz0Qbq5Lq173x0EVillPC70szWhq5XNKi_unSMYUlGl6SN-hinpeUASOIDt9GLRM_jXxI2PKTq4t0V5R6T6f9hyDjRovkIucoL95VwYjLtLXbkZP9sWpy6Ew0cfz41_b2T6csfjmTVTdyoUER1fF2h1SOu5EAyzLMSx-P4p7_bSV0rdMptqdXXAEpvHr9JzCYihwZZMG3aoa4ni4_9l9aah48OqDy0P54eopCV6GUAlaKDuJgPxV0VipXod-eZiAyel4onlMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری خرم‌آبادی‌ها در هفتادوششمین شب حضور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435786" target="_blank">📅 22:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435785">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4b5badbd.mp4?token=izy-dMgV78ph33H9XdzqGsDUq4OzyPrfteoo_NuuaP-zNXmgDrM_qL59LmNc_lJNNXfmwcPVsKaXJVvUgYtC--KsSrm2_bFSrhSleEF9L0t7ZYyDvAz_JeY9v8VJgEJeSphSHwJ9UsppdTtC93WiGJ-ztjXoNKrOB7D8nwhasH3KY8GJszeBO2ccSbR4fPlNkNM3z-lP_pTvFBuuxMxVswvvGhJyGf7LM9Ad9lygtRgkWze7tPsftcMoS1aQkZnDnJbivzvCYIo8IdDp9H2gs7DNX8y5lMRSQ07hyKpBEEltuFlu7f6qStJdrAyzV26r_GWn5dY1vwPdxU5_3Xq-k7ckI8IA3QnThxClQj7alw1NbdwOyttHnmZPhlh7qg6Jr0w5yvognoRAp7rgLBSRqivGmhDnFP4K-iJEsvDmolzJrwmI9v1DXqo0TpJ-YRlqE7sqzIVXhhzjSh5nBr2HJrSrcaEvVxBX60xwJ1_2hKHafbe8mcaUBNmigZtfjnz64RMM7AWtZWLOCxqoNcZocg9IKHt9q0HQ-W4IeNVIe0SUhaEswUKE_lGeTIyppqVGglSwt08oni2jMZT2DsKV0LBWUyA4MMzvThkhKpnUt-DzedK_JgR4UUrmtY3MKy9svB7LZyug0BZtr8I-aFEmBmBARDRx6eoDuHXzcCwC9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4b5badbd.mp4?token=izy-dMgV78ph33H9XdzqGsDUq4OzyPrfteoo_NuuaP-zNXmgDrM_qL59LmNc_lJNNXfmwcPVsKaXJVvUgYtC--KsSrm2_bFSrhSleEF9L0t7ZYyDvAz_JeY9v8VJgEJeSphSHwJ9UsppdTtC93WiGJ-ztjXoNKrOB7D8nwhasH3KY8GJszeBO2ccSbR4fPlNkNM3z-lP_pTvFBuuxMxVswvvGhJyGf7LM9Ad9lygtRgkWze7tPsftcMoS1aQkZnDnJbivzvCYIo8IdDp9H2gs7DNX8y5lMRSQ07hyKpBEEltuFlu7f6qStJdrAyzV26r_GWn5dY1vwPdxU5_3Xq-k7ckI8IA3QnThxClQj7alw1NbdwOyttHnmZPhlh7qg6Jr0w5yvognoRAp7rgLBSRqivGmhDnFP4K-iJEsvDmolzJrwmI9v1DXqo0TpJ-YRlqE7sqzIVXhhzjSh5nBr2HJrSrcaEvVxBX60xwJ1_2hKHafbe8mcaUBNmigZtfjnz64RMM7AWtZWLOCxqoNcZocg9IKHt9q0HQ-W4IeNVIe0SUhaEswUKE_lGeTIyppqVGglSwt08oni2jMZT2DsKV0LBWUyA4MMzvThkhKpnUt-DzedK_JgR4UUrmtY3MKy9svB7LZyug0BZtr8I-aFEmBmBARDRx6eoDuHXzcCwC9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیر تنگه هرمز
🔹
رزمنده‌ای که ۳ جنگ را در تنگه هرمز تجربه کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/435785" target="_blank">📅 22:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435784">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4d62d46f.mp4?token=fdb3pcJDJ0F5fPZe339-wsJir7jMI6bMoeETw3-uDp5v_cjj8CZWSOr3yNpwzmPdrLYk8DT8hSmypjQPjT9pZapnmCqs-SbNCvQvvXjm6rgpTHDNBXWOA9h_8U1dZo392gINaSXVQBLdO3qnuaisnH8AC7ZiNw1MhhKqdThAPK3aa7u5Lg9rgHoDXd_2E6C1MRD96I0T5fpUC4krLy8IAjuv0jaNKF-znnojkb9JSYHnsXLQuXorZx7SFri1i1C8Sx7E79n8LqUcRpebOB3q13qeVVAlkZshJdB2sYu5aN6K8AhkIoJ3ai2xRTg_u0Jtt6L9f1XI5cdfssX0nDo4Ikil2-Pc22po6SdE_f19TvGJqJUsKaF6MZ6NTou-25DcXLtupPNDk5WxabYmw9URJNsGE43KRV-gCd00jCtlCqXw0sLUiFVT_c2SLosL-4FixhBwkFwwEmLtbqwmoQrycJplcQ302Wdk-982cW1O2RlQ8AM8KNvyY1NuUuRUMC-qyJrSymkdlSpsoua61TRIGpbmgfILYWyQPF1c2Z7XPhJKzgBOYQ9Rx_K-2r9Aq0CM-dRYiafa6KBDkuEjT_1nprCtvWzd41Ivcmx32wHoCUBjhUSWG30qf5HaCBQdcLGu8rxWIcjxMwVxtTsn8SytWvlPcR6auiQTQUnNn165b1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4d62d46f.mp4?token=fdb3pcJDJ0F5fPZe339-wsJir7jMI6bMoeETw3-uDp5v_cjj8CZWSOr3yNpwzmPdrLYk8DT8hSmypjQPjT9pZapnmCqs-SbNCvQvvXjm6rgpTHDNBXWOA9h_8U1dZo392gINaSXVQBLdO3qnuaisnH8AC7ZiNw1MhhKqdThAPK3aa7u5Lg9rgHoDXd_2E6C1MRD96I0T5fpUC4krLy8IAjuv0jaNKF-znnojkb9JSYHnsXLQuXorZx7SFri1i1C8Sx7E79n8LqUcRpebOB3q13qeVVAlkZshJdB2sYu5aN6K8AhkIoJ3ai2xRTg_u0Jtt6L9f1XI5cdfssX0nDo4Ikil2-Pc22po6SdE_f19TvGJqJUsKaF6MZ6NTou-25DcXLtupPNDk5WxabYmw9URJNsGE43KRV-gCd00jCtlCqXw0sLUiFVT_c2SLosL-4FixhBwkFwwEmLtbqwmoQrycJplcQ302Wdk-982cW1O2RlQ8AM8KNvyY1NuUuRUMC-qyJrSymkdlSpsoua61TRIGpbmgfILYWyQPF1c2Z7XPhJKzgBOYQ9Rx_K-2r9Aq0CM-dRYiafa6KBDkuEjT_1nprCtvWzd41Ivcmx32wHoCUBjhUSWG30qf5HaCBQdcLGu8rxWIcjxMwVxtTsn8SytWvlPcR6auiQTQUnNn165b1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها با ذکر یاحیدر به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/435784" target="_blank">📅 22:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435783">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a581e71f0c.mp4?token=RBeuLTAXXhd7eNdaXyjXwhZyJfJshRGTc1Dyrv3LS0dqfgM3YCb2nh7x0nRokpJZty7EquavpduejBQElTs-FczuHK9ne8q75Anx3E4fBI1lKsJp-j2Ss7dOTg6w0ojZnbkfIMxFeExPrvWbpL5TobAx5_PDKy48ZU1sNtABzP6BhSsRUfFaajT7bnALXjtAMCf1kq5QePF_oAVu2Ys9OtVwdeCsq5RiTMHQcFKP9d8vsrFbWoI6b3jM9PZEZ-9jnC7OFeJzLlnZ9oFJOtxexauvlgReyKFOsNVpTnpkp9loczlrfwCh0KItmaT9sg2hzP-TK4TlHziNCEz8o4c05w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a581e71f0c.mp4?token=RBeuLTAXXhd7eNdaXyjXwhZyJfJshRGTc1Dyrv3LS0dqfgM3YCb2nh7x0nRokpJZty7EquavpduejBQElTs-FczuHK9ne8q75Anx3E4fBI1lKsJp-j2Ss7dOTg6w0ojZnbkfIMxFeExPrvWbpL5TobAx5_PDKy48ZU1sNtABzP6BhSsRUfFaajT7bnALXjtAMCf1kq5QePF_oAVu2Ys9OtVwdeCsq5RiTMHQcFKP9d8vsrFbWoI6b3jM9PZEZ-9jnC7OFeJzLlnZ9oFJOtxexauvlgReyKFOsNVpTnpkp9loczlrfwCh0KItmaT9sg2hzP-TK4TlHziNCEz8o4c05w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یامال در جشن قهرمانی بارسلونا پرچم فلسطین را برافراشت  @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435783" target="_blank">📅 22:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0dabaf70.mp4?token=WLTV2vSXWS4LF-K7xBVuOndIKuboSreO0ptJuZmYhaYqgGH_gSxhpFP14hKj-r5iRrqrqoInXhP_09LBCjNYEOo_832BH-7wgq7iU_70PYT3xaiPOgsebzgawy_5mauU9zyUhbAPRqunRV9jgh_XOSvjUHg30tDkHydsFw0GLQ4zFgbfjiYCJRbslZn0ojlbm_4pwJnIf-Vl2wcHgzpDVkyvb0TzjSQ0tdR6j2uu6iwyE8giroF-QdIZ4-BBgXbBgP2r2ORWfp-gRCcufAyNufwtyLmeia8HnxbLFUTGx1CfkaL3xWmCnmI1Y_JJcfIxsUPGmZIfEw8kwMaz8VG7BX4PQ3Ee_z5pg0xCSxzgVB_x88K4KW9mkpN5vJyQ-Ibgs-Z7eSaB7avulr6Gk6DessV9ectO6lSywvLIYhkDkuAgf0vI7iA1YUkbBLb5VIY8bLUUGBfyOvZnbKM1iIePIUAeyxtlPY7J7h8qLYdWZlTi6C_q7fluQiCqi8Kzv-BxgfHWveH0WtMPRbjda9M24xwxLG5lEf9cjf1BrVDQTBiaULaw844Uf-55SqE8h1mDbsmYpKow9-fygEx-Eca2wuT50FFiVvAG9j1hyHBcW_91TJTo962kXXFunDvbAJFhPTOwHNEKQWLnXQiDqtGRnRTK2d6veCGhVFnoyaQZTRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0dabaf70.mp4?token=WLTV2vSXWS4LF-K7xBVuOndIKuboSreO0ptJuZmYhaYqgGH_gSxhpFP14hKj-r5iRrqrqoInXhP_09LBCjNYEOo_832BH-7wgq7iU_70PYT3xaiPOgsebzgawy_5mauU9zyUhbAPRqunRV9jgh_XOSvjUHg30tDkHydsFw0GLQ4zFgbfjiYCJRbslZn0ojlbm_4pwJnIf-Vl2wcHgzpDVkyvb0TzjSQ0tdR6j2uu6iwyE8giroF-QdIZ4-BBgXbBgP2r2ORWfp-gRCcufAyNufwtyLmeia8HnxbLFUTGx1CfkaL3xWmCnmI1Y_JJcfIxsUPGmZIfEw8kwMaz8VG7BX4PQ3Ee_z5pg0xCSxzgVB_x88K4KW9mkpN5vJyQ-Ibgs-Z7eSaB7avulr6Gk6DessV9ectO6lSywvLIYhkDkuAgf0vI7iA1YUkbBLb5VIY8bLUUGBfyOvZnbKM1iIePIUAeyxtlPY7J7h8qLYdWZlTi6C_q7fluQiCqi8Kzv-BxgfHWveH0WtMPRbjda9M24xwxLG5lEf9cjf1BrVDQTBiaULaw844Uf-55SqE8h1mDbsmYpKow9-fygEx-Eca2wuT50FFiVvAG9j1hyHBcW_91TJTo962kXXFunDvbAJFhPTOwHNEKQWLnXQiDqtGRnRTK2d6veCGhVFnoyaQZTRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتاد و ششمین اجتماع مردم آبیک قزوین در دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/435782" target="_blank">📅 21:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435781" target="_blank">📅 21:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5d8489d9.mp4?token=Kwf8UDXfI-PvuIhpLoarmBMF_Ls9bBG5ldCXypVDPnYqPbyblEK_aa-ksCsucyYAtDSPQsdtRS5Wn8NrpK87td7ul3ydH1RAwcsqCZf5lfOilsWHhGTpUuqbhkjpf-uyfPJHJ_WnxgsFBgD1HGJ6mol-a90VRx2vxWWwKuA1YdRLDGQIiRR3-wRs_gIwviYrQLg8JLhCaMzXt5xzDCqZlzpE8UZJ7Ubamdz6CA07jQXKIvqV0wXafYSUA5c5zI-Ha9MFZZ82xkSj4Fg3HKxp82aGWMLY8lQ4Qf5__Va7tT4w_gVEJUcH3ZOuzEYQxrfc0DppaNpG6wpd5o6YzzT3FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5d8489d9.mp4?token=Kwf8UDXfI-PvuIhpLoarmBMF_Ls9bBG5ldCXypVDPnYqPbyblEK_aa-ksCsucyYAtDSPQsdtRS5Wn8NrpK87td7ul3ydH1RAwcsqCZf5lfOilsWHhGTpUuqbhkjpf-uyfPJHJ_WnxgsFBgD1HGJ6mol-a90VRx2vxWWwKuA1YdRLDGQIiRR3-wRs_gIwviYrQLg8JLhCaMzXt5xzDCqZlzpE8UZJ7Ubamdz6CA07jQXKIvqV0wXafYSUA5c5zI-Ha9MFZZ82xkSj4Fg3HKxp82aGWMLY8lQ4Qf5__Va7tT4w_gVEJUcH3ZOuzEYQxrfc0DppaNpG6wpd5o6YzzT3FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های در اهتزاز در دل شب
🔹
میدان‌داری شبانۀ مردم ایران به عدد ۷۶ رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/435780" target="_blank">📅 21:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سازمان اداری و استخدامی: ساعت کار اداره‌ها از ۲۶ اردیبهشت تا ۱۵ شهریور ۷ صبح تا ۱۳ خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/435779" target="_blank">📅 21:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435777">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7-qpla8CawM6pWGqWqD_SoI94HQnE_lWiMqQUoMoJOiSNRWh56uPo8vFo1eQN4n_Ux0AhKKnAwq7pFGXcjlnWiqpb_DzkslqP7KAHRLoe_R7xTUdw5kfo_ZqW432YsPtmnFo2T-pO2X95M-h_smZT9d1vFN4VIe_2bLIeQZfi_8LkeM23Qg-ie9f4X7XILGQQe7nVvecfO12ocOXcqB56KIN3n_c6NHvqFmWyjtzaM-S9ZhDOzeBWXD9nKiXhS-O335FzVUkf6nNgW2Bpv8WmoKRUd369oAomOyIVVGRnZfEOzgUUfdhydeYXF3N5tLFASTwzEUn-ohhBoyrAB90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbab850c7b.mp4?token=jSESWvbeMoBW_81Q7KVH7xJKZ-j4PVjITPapukTXv7wELRq_Vnu_WG1M-mvhunAuZTLumitiYbmUtc341V6Dpvq0SqZOX-_np2MueiV5__0RjYJhIL1CastxU0hQ87AUHPiamIokY23vbrj8xSrcYQrWEunqxGxdCxd8NwhY1COD2dByRFcjDBeLlX80rMwszpNJXP7SdVO9zT3H0f38SN8caxPgnEYWN6a-dvYI7cbx3XwTthqRq7_ndpYMWJBqLYFLo2NJjSk1NL8njwjBK842AI5_P8WTdpF-BvcEKtBlwsiw4cufTop1Z-7zp-AwNvp6LdNsW-KphTageXKsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbab850c7b.mp4?token=jSESWvbeMoBW_81Q7KVH7xJKZ-j4PVjITPapukTXv7wELRq_Vnu_WG1M-mvhunAuZTLumitiYbmUtc341V6Dpvq0SqZOX-_np2MueiV5__0RjYJhIL1CastxU0hQ87AUHPiamIokY23vbrj8xSrcYQrWEunqxGxdCxd8NwhY1COD2dByRFcjDBeLlX80rMwszpNJXP7SdVO9zT3H0f38SN8caxPgnEYWN6a-dvYI7cbx3XwTthqRq7_ndpYMWJBqLYFLo2NJjSk1NL8njwjBK842AI5_P8WTdpF-BvcEKtBlwsiw4cufTop1Z-7zp-AwNvp6LdNsW-KphTageXKsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: فرمانده عزالدین قسام را ترور کردیم
🔹
نتانیاهو و کاتس، وزیر جنگ رژیم صهیونیستی مدعی ترور «عزالدین حداد» فرمانده گردان‌‌های عزالدین قسام (شاخه نظامی حماس) در غزه شدند.
🔹
رسانه‌های اسرائیلی مدعی شده‌اند که عزالدین حداد در بمباران آپارتمانی در محله الرمال در غزه به شهادت رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/435777" target="_blank">📅 21:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435776">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de2cca144.mp4?token=vERchvYxqoVkoSj4iyBrUT3EAZt18Otf8bJ5qxQD5y-hZq6HtndzLnN-SpY4LpFP1OOH-_SW4PfQ56MmIurQbp5mqSjty31g3ahdN7U9Xr69wC61ZG6MrPL6j_wZkXlQHq4-xellmmhwWwehj4R1wWUqj8Gh7l02pFvuJVw-tG--ChzzHDKrLJJF7s1G1n6HYCTVSU87ccHjOjvkI15X5-cuOEsXORdOEppPfxUPGSAXUKbrO_bGKCuZbBBNPjcYmPrMNDAl-01Dxzlu4rCXBYXQWUoGaEpr-d0PWDo0hz0msH3i0D5B2g1TFUO3WOuG6PLQO1eFNMI2cDV-hfKy234_ZclvxjoWXNrkC-fuPNtVg09EVp8UFK9U6niaClXjGzz3awquoZB7wofTLU5xj-JknXHRx5i3S7Rd1WOFOoS4W-E8tGr8hdyk9fTyE4Uvb2GrKnpeoDT60mmoGndev4w-t4EvrdgYMErnKEKNhzKCQgApNzpJtRJzjQl8SxEPG1ivyB-Zs2FR0D3kyRHfPsWYhJ3xWpC5MnU1xFrXWlAKr6VChbW2vDwlDYYWzBYTsOElJGx8iqgFCno9kx4TGlX_00bPo_XEGlVWvKo3mOZbMfYX0ed_iwOq5HwJOYmfI_4UOLZUH4yI9RHFV0cah7FAqj3CfY4yxWQcZs6HseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de2cca144.mp4?token=vERchvYxqoVkoSj4iyBrUT3EAZt18Otf8bJ5qxQD5y-hZq6HtndzLnN-SpY4LpFP1OOH-_SW4PfQ56MmIurQbp5mqSjty31g3ahdN7U9Xr69wC61ZG6MrPL6j_wZkXlQHq4-xellmmhwWwehj4R1wWUqj8Gh7l02pFvuJVw-tG--ChzzHDKrLJJF7s1G1n6HYCTVSU87ccHjOjvkI15X5-cuOEsXORdOEppPfxUPGSAXUKbrO_bGKCuZbBBNPjcYmPrMNDAl-01Dxzlu4rCXBYXQWUoGaEpr-d0PWDo0hz0msH3i0D5B2g1TFUO3WOuG6PLQO1eFNMI2cDV-hfKy234_ZclvxjoWXNrkC-fuPNtVg09EVp8UFK9U6niaClXjGzz3awquoZB7wofTLU5xj-JknXHRx5i3S7Rd1WOFOoS4W-E8tGr8hdyk9fTyE4Uvb2GrKnpeoDT60mmoGndev4w-t4EvrdgYMErnKEKNhzKCQgApNzpJtRJzjQl8SxEPG1ivyB-Zs2FR0D3kyRHfPsWYhJ3xWpC5MnU1xFrXWlAKr6VChbW2vDwlDYYWzBYTsOElJGx8iqgFCno9kx4TGlX_00bPo_XEGlVWvKo3mOZbMfYX0ed_iwOq5HwJOYmfI_4UOLZUH4yI9RHFV0cah7FAqj3CfY4yxWQcZs6HseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روستایی‌‌زاده‌ای که آبروی هسته‌ای آذربایجان بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/435776" target="_blank">📅 20:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435775">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUus2BsnrASbevVcwiIc5FIvqsP3raZNf6wLIdz5kA8qZPWygfH9sypkAXWcdGvbBhZ6Qc5DofzNtsUzsO9IcLCgwMzlhY4y32vT6tTRnWIyzgWWGLDAbEhSdDyloDn9PdL8f5mwrfjPRBx0F1Risyd9h-RgL_Q2cDdfbp6j-R1aXIP0LhKfwL3tCYD6RzHd-kz0x6oM46hUITMk8Oix6RGlElisGLQhsqjUM3cMRSROW_qmeIXMPWog8imjpMtxF2Ppdvvnc_PPHUGn97qpgxIoll1XDbIh4ReIgRG0eN90o926e4dE1X0rf1Ew_jpsKDCmQqICflmA4DpJD4ytOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داستان‌های موازی» اصغر فرهادی، ضعیف‌ترین فیلم کن تا روز سوم
🔹
در سومین روز از هفتاد و نهمین دوره فستیوال کن، اصغر فرهادی که در دوره‌های گذشته با آثاری از سینمای ایران حضور موفقی در فستیوال‌های جهانی داشت، آخرین اثرش که فیلمی تماماً اروپایی است به‌عنوان بدترین فیلم جشنواره کن تا پایان روز سوم معرفی شد.
🔹
اکثر منتقدان وب‌سایت مویر امتیاز متوسط را برای «داستان‌های موازی» که دهمین فیلم فرهادی است در نظر گرفتند و اسکرین‌دیلی نیز «داستان‌های موازی» را به عنوان ضعیف‌ترین اثر این دوره از جشنواره تا پایان روز سوم لقب داد.
🔹
منتقدان فرانسوی نیز به هیچ عنوان فیلم فرهادی را نپسندیدند و با نیم ستاره و  یک ‌ستاره از آن استقبال کردند که همین موضوع «داستان‌های موازی» را به بدترین اثر این دوره تاکنون برای آنان تبدیل کرده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/435775" target="_blank">📅 20:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435774">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfZNkTIN0F4gx7hZeDQoim_gR6k2UPeHRBd58KQAIZSryLAvOb-tOxar6bnjPrSPC82X-PZqDqKYzUyiArtzXeLQSLqtd3xY343k2Cm-EMWZWnU8Vu7qVxFqDE0UEwLiS_0CPiMfMnbYEjrdpasEpuQ6O5t988EcWqg0v0kLLYS3CtWcV9hKyfr8Rv-B1t5J8uyi6tSLEGnUS3rxdJ57NYd7kxkb0bJcziZrx_BbR5PXQiAMY9nZP92hu6lB-1GinCLFWR2nm46vURB5OlVGlomMM2IcOgz8XhcU4EL5tnSMdqQycc0DmZiAvF_f6wcs74s6s-FnuDIojvTJFFnxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تصاحب مواد هسته‌ای ایران ضروری نیست
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در مصاحبه شب گذشته با شبکه خبری فاکس‌نیوز از ایده‌های متفاوت و متناقضی درباره تصاحب اورانیوم غنی‌شده ایران که او گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌کند حمایت کرده است.
🔹
متن کامل این بخش از مصاحبه را
در اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/435774" target="_blank">📅 20:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
جنگی بی‌صدا برای خالی کردن خیابان‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/435773" target="_blank">📅 20:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec1b837167.mp4?token=eJ8DCj7R7CHDdvElvvaGYrCmZQ_CSnV0DfctfF_5d3VSwHzzhalDLyAY_SAsmeLocuGEJ0jyskhFVwMRGQ08bEsm8D80w-JU6UmryRaFMoGv2BdBPKuYCsN09PRxWVjzs4KW98NalCDieeOldFTOk6I1D-X5ILLGixyVArP7YuNfhNkeCUP9NcS5AD7XGAXEITzABBeHAYOy5cseXDBSPPr_yMUw5W9oD0aiPJ_QlsGyONAK8YC5LuP0RRkBs8ci1RH83Lj4DwbbOyZzzmWsDbgnRwANHdRrRNz80eIsPOjFRRbo_Ak1w6mNJ8P8-O6J-85qWv-b8JA54d-Efw0lSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec1b837167.mp4?token=eJ8DCj7R7CHDdvElvvaGYrCmZQ_CSnV0DfctfF_5d3VSwHzzhalDLyAY_SAsmeLocuGEJ0jyskhFVwMRGQ08bEsm8D80w-JU6UmryRaFMoGv2BdBPKuYCsN09PRxWVjzs4KW98NalCDieeOldFTOk6I1D-X5ILLGixyVArP7YuNfhNkeCUP9NcS5AD7XGAXEITzABBeHAYOy5cseXDBSPPr_yMUw5W9oD0aiPJ_QlsGyONAK8YC5LuP0RRkBs8ci1RH83Lj4DwbbOyZzzmWsDbgnRwANHdRrRNz80eIsPOjFRRbo_Ak1w6mNJ8P8-O6J-85qWv-b8JA54d-Efw0lSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فردوسی؛ میهن‌‌پرست‌ عاشق امیرالمؤمنین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/435772" target="_blank">📅 19:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d09541d4.mp4?token=WaLY1CbE_oEzt3a9qkdq4yKRVl4yABHiNeah2_gyMcGZVZ9UMKUtP5EagmTPm9U1VLCyHTIsFvIeCeQOQ3_dNbdva31Le_ld_kjThPp4KpxLvzjC7OLA3i1k4NR16PbXAO5-IJwlxcQ9Nlad2_4bOFalbM0_KKeF9rXsaryDt3o8tFCyZ4klmH1Be1FWFj05Qv1jNkftuUgLNv6Scz6thhYUp8YhruawNsIPzEmKriKgKtLV6g7QrBp4RtT5EreNCpMZO7Cl2_3QDGgiwy9b1qD5xchtjOt_L14aO0dId3CtUIn_f41YzYKLnjyhF1KfRJUYQNtWqhVPUZ4_2AJR96LTubAu-detMAIvvoJHJiaXy_hhGW_an9D6xcqZhy9Ca7z8kQWAdQT93qRpibxHaHBtyvmvwEq4d8He3Ep-qWlA_PbI7388wX4ANCZ6FSe1zQr1W5r0Q0knOS9-4Gw6udoPl29p6fdpC6deiNT1D0V2u8jHsmlUR4JOrZVledh3fCeuMM1wvYx2n1K96Nz45QOR5E41K88kdFd119RchRiKS1FL21ZaiEjWBZq4Al9m4v0bdVD5HWn9z8hOx5HJ2PmSAxLZDNT1KVoHdI_6ZdPPIGHoUrr-ZiXEp-vkTRLokJOfBCm7nDChhjZfKRHto8m6AMKppGV93St3HWuXlJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d09541d4.mp4?token=WaLY1CbE_oEzt3a9qkdq4yKRVl4yABHiNeah2_gyMcGZVZ9UMKUtP5EagmTPm9U1VLCyHTIsFvIeCeQOQ3_dNbdva31Le_ld_kjThPp4KpxLvzjC7OLA3i1k4NR16PbXAO5-IJwlxcQ9Nlad2_4bOFalbM0_KKeF9rXsaryDt3o8tFCyZ4klmH1Be1FWFj05Qv1jNkftuUgLNv6Scz6thhYUp8YhruawNsIPzEmKriKgKtLV6g7QrBp4RtT5EreNCpMZO7Cl2_3QDGgiwy9b1qD5xchtjOt_L14aO0dId3CtUIn_f41YzYKLnjyhF1KfRJUYQNtWqhVPUZ4_2AJR96LTubAu-detMAIvvoJHJiaXy_hhGW_an9D6xcqZhy9Ca7z8kQWAdQT93qRpibxHaHBtyvmvwEq4d8He3Ep-qWlA_PbI7388wX4ANCZ6FSe1zQr1W5r0Q0knOS9-4Gw6udoPl29p6fdpC6deiNT1D0V2u8jHsmlUR4JOrZVledh3fCeuMM1wvYx2n1K96Nz45QOR5E41K88kdFd119RchRiKS1FL21ZaiEjWBZq4Al9m4v0bdVD5HWn9z8hOx5HJ2PmSAxLZDNT1KVoHdI_6ZdPPIGHoUrr-ZiXEp-vkTRLokJOfBCm7nDChhjZfKRHto8m6AMKppGV93St3HWuXlJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری شبکۀ مرتبط با موساد در اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/435771" target="_blank">📅 19:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435770">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">فاجعۀ نیم‌همتی در استقلال
کدال پرونده‌های مالی را روی دایره ریخت
🔹
انتشار صورت‌های مالی باشگاه استقلال در سامانه کدال آن هم بعد از وقفه‌ای تقریباً ۸ماهه، نکاتی جنجالی و جالب‌توجه از پرداختی‌ها و شکایات میلیاردی علیه این باشگاه را نشان می‌دهد.
🔹
در بخشی از این اسناد، حسابرس از باشگاه استقلال خواهان اسناد مربوط به پیش‌پرداخت رامین رضائیان شده که مبلغی ۵۷ میلیاردتومانی دارد.
🔹
در بخش خارجی‌ها، منتظر محمد بازیکن عراقی اسبق استقلال شکایتی به مبلغ ۲۸۸ میلیارد تومان علیه این باشگاه طرح کرده که البته رقم دلاری قید شده در گزارش (۵ هزار دلار) با آن تناقض دارد.
🔹
آلمدین زیلیکیچ و وردان کیوسفسکی، دو بازیکن بوسنیایی که در دوران سرمربیگری جواد نکونام به استقلال آمدند، در مجموع شکایتی یک میلیون و ۳۰۰ هزار یورویی را علیه استقلال طرح کرده‌اند.
🔹
کوین یامگا، بازیکن فرانسوی اسبق استقلال به دنبال دریافت ۸۱۵ هزار یورو و فیرمانی، ایجنت این بازیکن هم ۲۸۰ هزار یورو از آبی‌ها هستند.
🔹
پیتسو موسیمانه، سرمربی فصل گذشته استقلال با طرح شکایت در فیفا خواستار دریافت مطالبات خود که شامل (۶۵۶ هزار دلار، تسویه‌حساب مالیاتی، سه بلیت بیزینس کلاس و هشت بلیت رفت‌وبرگشت اکونومی و بیزینس برای خود و دستیارانش به مقصد آفریقا و ۵ درصد سود سالیانه) شده است.
🔹
مبالغی که اگر شکایت منظر محمد عراقی را از آن فاکتور بگیریم، تقریباً به ۳.۵ میلیون دلار می‌رسد که معادل ریالی آن بیش از ۶۰۰ میلیارد تومان است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/435770" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp6PBgTyVTI6V6FJjhTvNHb5xUs1vikCl-l7xMbN3NkdwJHOmnZTcnJ2aogZKTWFV8tMSe6Ax2R8IpFbfEBMEoOPXZH4kM7giJ7xwO2X9KoC_9nyQ7Mdm0-vE8tDPhEjwo6nsu1xHnn_Di7y5Zym-Fpy9F44o3-Zn7DDQq7KafMp2Dz4ifvZeJogATUE-TE1FUJiG2a-4rwO1LwQlR57Rbfj9HFPvV8KlVIwPn0aE_ZqYAUM-KvZ2GAo_NV9zOTeNCfprNm26lFaBibXHr7sPJmCrM4vAUKEUdJHXLodFx61ejQ3x0KnuQVKcVhHwzWxBYazp3dimusq5tDaEBHQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDycP4cNS1CNDSWdrA07HnSx3c7eomfNIJkIdvvS6D1IPfh-nNR8B9LqIb2RUEQOoO5Su1WJB4shnCTX-aw-TCaOAjTVtlwk_3RYPpqcr8tLNFjRp3A3T5mI3b8ucA3L_tVriDg6hq6dkS73JgigLX8GODlqZCXvpWQdoB3FnMcIk_a7LX2JeVCitLTw5oFTxvg_wYIjulEpgNcFAiGoVUVYLubm__rPEY6tEPYiHJrVsAunN6lvK_17r8AJnvEZrCKbhXsRB_xvIGrPch0Zh5hQgzlcBH71pYG_Nl-ovXci8fCa1h0-UOVTa7kgOn_6RajGxgDjdXjeSvKOnxZtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTrfRETxSPExoj-jAVHk3V7H5RmNzPBGpHU_tSOSWUtlwMb9W1XrNDH4udWv4JyX_3H7bwDbq4_iFwZA5B02q42dGhR5I2B8DlDPSxNMaeuRLPsNup4rKK9_uePDbS69YxLyTNei7nf9pzlWabv0RKvSMF1NvWzoPix_lbPmdRBfCwladIUzGw9aEUlu0R_5Wlua_czjqpHnvBPf1aq0QflI9sQ_70CHW0nPuSklCc-031GCOKop3IC-JxmGAJnzWpdSgXGWfE3mpxa_6zDxv6TETKkMY34trifJkimveYUUbVJ0R2fhLx_ajqVJK5GqaccPOSIXXRGKJhHxiLZBiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSp7WY6DyRlguzF7iTb4esa8KfULfckZsg4iK-LV1wBCEAJsamRPio6cH-KPN7D4P5KjGjc-iZPxPbPYGHoJIQzp5zCiApY3pvgYPEC6uOKa3f4uGoYJRGPWfB-1dWlqRe-b8kMFGAWfybLPzhLuj_ofQaP6j7vbQuqWsJx3SGkPE9By7p9i8Q9nt1GBpnoYGt0CITYIi0gtIC03z1H_izMOs-A5m7E78cYio0sr2MirnXb61gEoy58UyquAsEXVFWJ-Le7vbX3ttY4QBTSyvrJpK6lDfK2dJIpKx1JAuaVp2_SJt6Bqu_6YDiMQCcHKPscO0a-GQPsy0_sUdJaoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3fETTCDJ9Ba4pRYCAgdvG3T-rS_ixEoPWXDBWV7yBplBmoQRBgDQLU73unNXxD0-1bpJpu6pCIuZxfHgq98DWoPWw0TnTz9aZq1mA_i3dwAoel5X2GXU0mIuoQxbYbdlqOCLGMGqiWwT0H4-73FOD3dbLj15PHThBm2PFP0DK40PVfp6yzp3YxN7qMLbE1_j3LpdJoqK8Sl0JMkvAHhZFvzhyq2jR-WktRSGzLZ1uesp-hXjJ638mWZgqzIi8KCgpYEGujpZaWtzUlScrlVthDQVJr1-s8TatZAalddlFzvKw6TheVV9dHwK666cjJdWlFFSKf4gTte-teoHaya1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAltGAEKyPmDkQex_nZ5JIMh797vJqtvzfwQFQmw5zQjEvHlM647MsZ6nZo4EB3fs4q3qi-vEEqmJ_0v0Ne9aCmpdYLrCOpiCtMGr_1gzMLDTX3mBQtwRCvs5QESgSM-1_JAw9vClhZu7ssOraRcK2EZEEOlVUVSEdq34h8SjT7dDJr5gGFYWXtqJAYt_Ts578KFsWm-ArtJ4DLiYgrIqMvFW4YFtz72Qyae9bMoTVGbYWTmCSxK82IuOIn18axiXX4_bGsrWEeE3y1o5UE7GUcnA6aa3Xci5TEQifFg4svX8Q8e_BXUt9dt40soJ-oKqVcPIvXm9_DfX_HqfgHAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSnh0-3Bs3NDjXacMGVRWvCHMkoMcuOHeYsXRhkruG7gw_b81dDc5_BbnPm4ITiArCAnLYgTd93U32aIp6HvdUEe7E_IVHthbbcYMPjgm9K08AGIpX-rWA5IlDyIo-w09eInZ1J_0lVUr0YaJSbhFZbMqqS4gGK1ltU85mzVhGKKYueduoK3SGdkd0BDtqkpoNfGUoBwJ-9r2YdXPrSfoCFIAdD1BWjoolJOPq767sYLtOnaMQDwaPKiUbXT8B_EPp48ZeEEe7PrET1xXTZy10e7F79x9BLercxLRyB9cb4FP9MorK6Vfo6CNgwvtlxmcQJJpqAJhzM9NOYmWfftLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهل و نهمین ندبه اجتماع قلوب مردم گرگان
عکس:
علی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/435763" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73dfccfc21.mp4?token=V0_r9zdIsM4k7zPHhqQiNekwz30wOXichbfkrlugR2l5LYU-aGiZPgf4JCgcr8fD77zEAN1-ZJP1I5C0YKWRkIn3kkbDCg6pgiHoNnL0wiCNpz2mkTeif3NZhXi4lo7eb9iRb0SsLkcsNnaHGkRFwxCUxdJOPc1JaxdJzjzvWIZqpGK9HiNEeF9L_enGyENB6W-jTR5k5Nl4sVMHX33sWHIkvy3A45VOWRSJdb8hkjM0LahE7j8O-9-AKx8_ZOenCyaRJ-SUTOD2EBchkbZOtTXbiHOWMN83nfGVxYzrHOa_fOnmysSKdnOr5K74J5Ulz2dJ8VgU-LJKYhk1O-iXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73dfccfc21.mp4?token=V0_r9zdIsM4k7zPHhqQiNekwz30wOXichbfkrlugR2l5LYU-aGiZPgf4JCgcr8fD77zEAN1-ZJP1I5C0YKWRkIn3kkbDCg6pgiHoNnL0wiCNpz2mkTeif3NZhXi4lo7eb9iRb0SsLkcsNnaHGkRFwxCUxdJOPc1JaxdJzjzvWIZqpGK9HiNEeF9L_enGyENB6W-jTR5k5Nl4sVMHX33sWHIkvy3A45VOWRSJdb8hkjM0LahE7j8O-9-AKx8_ZOenCyaRJ-SUTOD2EBchkbZOtTXbiHOWMN83nfGVxYzrHOa_fOnmysSKdnOr5K74J5Ulz2dJ8VgU-LJKYhk1O-iXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع آتش‌‌‌سوزی در پتخ‌تیکوا در شرق تل‌آویو اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435762" target="_blank">📅 19:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b819e8e9.mp4?token=MRPgcwHD5f5Gx2Lt_kqJnctvJHge9D09sLEQl0zQjREz_6tLM93KrVLU6AAvnm9hQwDMwNe89e4AHkedIlHRB6Bj6uDa3ZDoB-yywm7ceiQ8idHASm_cXi86YvjLObAp7fp2Q2IfZz7v272KE7j80M7uBdr1Vrq4S6l6QPesNvjjQA9Tb4aSEvacGeQFlUMvEpK8vbOsJDVjBoiI0gd86qChC0Ek2knKSrTHu_aJxfs5Qrw6wKnFqC8l8Y0tfaxV0OE1nLh9NcDcnpFOkezgHmFl7X0mCOS4Hz0aeD8sGOytK2tlohPhmcKuVj5qqWt6U5NG965nt16DS_mbm-ItUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b819e8e9.mp4?token=MRPgcwHD5f5Gx2Lt_kqJnctvJHge9D09sLEQl0zQjREz_6tLM93KrVLU6AAvnm9hQwDMwNe89e4AHkedIlHRB6Bj6uDa3ZDoB-yywm7ceiQ8idHASm_cXi86YvjLObAp7fp2Q2IfZz7v272KE7j80M7uBdr1Vrq4S6l6QPesNvjjQA9Tb4aSEvacGeQFlUMvEpK8vbOsJDVjBoiI0gd86qChC0Ek2knKSrTHu_aJxfs5Qrw6wKnFqC8l8Y0tfaxV0OE1nLh9NcDcnpFOkezgHmFl7X0mCOS4Hz0aeD8sGOytK2tlohPhmcKuVj5qqWt6U5NG965nt16DS_mbm-ItUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی دختران قزلباش در وصف شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/435761" target="_blank">📅 18:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4907051e.mp4?token=EmyLn_jCTMrLJGc0h3G_w8Cv9UI8iSSEYRoLs9P9Iho3wZ56N9KnHF9S63yJB4IsrU6BHFmiseg_0ioaQBm1hXRQ6IZ_Qm5RPJQ2Uu8Nm7pCBERJvnAKnA-6X1Bv7UoXjSho5oWc7zdv8bldc09TiLy7ebYG81CMdgNoQD288Ad7Bp9qhhIdN4n8gPX3fQfvLVCHCg-bdy8u5wbHNb_Pz-81oEMsFE8Kl2vnVMop3kMWufvHjoVJOoK7MiHDrQvUGjx9qNzjSBW7_mYQLeS1vOpsGgCbAa32iyomzyFvkKlkmfTXQLLneL3AMEy1QZOukFC6QIMnLchakUJn2bWS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4907051e.mp4?token=EmyLn_jCTMrLJGc0h3G_w8Cv9UI8iSSEYRoLs9P9Iho3wZ56N9KnHF9S63yJB4IsrU6BHFmiseg_0ioaQBm1hXRQ6IZ_Qm5RPJQ2Uu8Nm7pCBERJvnAKnA-6X1Bv7UoXjSho5oWc7zdv8bldc09TiLy7ebYG81CMdgNoQD288Ad7Bp9qhhIdN4n8gPX3fQfvLVCHCg-bdy8u5wbHNb_Pz-81oEMsFE8Kl2vnVMop3kMWufvHjoVJOoK7MiHDrQvUGjx9qNzjSBW7_mYQLeS1vOpsGgCbAa32iyomzyFvkKlkmfTXQLLneL3AMEy1QZOukFC6QIMnLchakUJn2bWS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای سربه‌زیر شدن ترامپ در چین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/435760" target="_blank">📅 18:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
همان رستم شاهنامه است او
🔹
نماهنگ داستانی «جهان پهلوان۲» منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435759" target="_blank">📅 18:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435758">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGWO749_SIa8VxFVbymlL0J0UldLM7N4ia5UfGOgUT87TKORP_AOI0HOUSJpvoWs2wmHl9wNf-KUKiAPFg6BJSZWKsPxot6VxTilyobDAChyFFTGkdRwAu5p5aykLIY1Ur8vwUmuwuwyvLnba_Qo6BcsIomWE2GuZKFwcuCi7Qie1LHJipgcC94hGFE8PB40dUWeQBPPL3upi3FIny6nqqGMKs4WNTaQ0F-PBFADKZwS7i415ma0EhZY5NaOcm6UGfkJfBItcuP4kkY4riIw-KqMVT_ZBFd337DLrAjHCN7yJ2yRIoqwovkXWwulArHhiVQ9EJX7cZZ5F57O6p_YdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: فردوسی با شاهنامه هویت ایرانی را جاودانه کرد
🔹
فردوسی با شاهنامه، هویت تاریخی و فرهنگی ایران را جاودانه کرد و پهلوانی را در پیوند با عدالت معنا بخشید. امروز نیز فرزندان ایران، در برابر بیدادگران، پاسدار امنیت و سرافرازی این سرزمین‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/435758" target="_blank">📅 18:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">پاکستان از آزادی ۲۰ خدمه کشتی‌های ایرانی از دست آمریکا خبر داد
🔹
وزیر امور خارجه پاکستان خبر داد: ۱۱ شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا بودند، بازگردانده شدند.
🔹
محمد اسحاق دار افزود: تمامی افراد آزادشده از سنگاپور به بانکوک رسیده‌اند و اکنون با پروازی عازم اسلام‌آباد هستند.
🔹
او همچنین گفت: بازگشت برادران ایرانی ما به کشورشان تسهیل خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/435757" target="_blank">📅 18:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-36.pdf</div>
  <div class="tg-doc-extra">3.2 MB</div>
</div>
<a href="https://t.me/farsna/435755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-35.pdf</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/435755" target="_blank">📅 18:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جام جهانی بالاخره به چین رسید
🔹
تلویزیون چین امروز اعلام کرد که در فاصله کم‌تر از یک ماه به شروع جام جهانی، با فیفا بر سر حق پخش مسابقات به توافق رسیده.
🔹
پیش‌از این چین با فیفا برای مبلغ حق پخش تلویزیونی جام جهانی به توافق نرسیده بود و نمایش این مسابقات در این کشور در هاله‌ای از ابهام قرار داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/435754" target="_blank">📅 17:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axc9OSUf_Scy0l0QZE-4NDOp7Rahd6f2lo8ETCs1_WPmlrn8zegokhpRLvl2Y_aQcNJhQwBRiOqvtcwMr8QxlMZ0ySXcd6NceUgmBTgYKaRts5fkGHcc9YCYAkmmtvNhgn2SiWuWc4OQomWf9BZahtveakBYToYWMDRHjtkJgwhH3VyP0wIsNdyRgeqUJcefPWbKVSe6qBMSjDZw1SoBYVWRxXCkpEW8cKI9AWzbshEvhp056dwIQq9zCZK3JT_-30qVzUpOIqrT5UhbmZLOe-4tInSVbEFyO4wV_y79KHq4i6xP5y3RpSIjK6SNeMJ0eoISDU-bB6w9-ytRb0Yflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری قدیمی از امیر سرلشکر خلبان شهید نصیرزاده در کنار جنگنده F5 نیروی هوایی ارتش
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/435753" target="_blank">📅 17:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
گردشگران، عاشق این دریاچه هستند
🔸
دریاچهٔ سوها از جاهای دیدنی اردبیل بوده و در ۳۵ کیلومتری شرق اردبیل قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/435752" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
حسین ستوده کوتاه نمی‌آییم را خواند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/435751" target="_blank">📅 17:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91c58a6b6.mp4?token=Xe1dml8WqiHSN3C4GorWz-Sjp5U8XwIggTLcKoVsM6EBvaJSJeTOT5-tdqzT9Az0gpyq9ayNNR2as_3V7BVgkRVEp25RSL1udjdsLA4cSzFJpTu2QcLoiZ1u-5sPST1b_gAN8_YSiRQRhSaahZMQJGkqo0rmGnWNwWoGNHNSAuY0UXIAiPiColMoB8GCqZi_CMR0QMbj5NzsNKccFYsZFIunGBpAQS_fvRFsGBpR9CT9u3eXUIlzmb_MOYZW1cKk8D_UBUCBHIZorjdeuu8pXqirzlErgRtkdiSALvrrUQpJ0mdkBikhHfT2wNVj6wWUYdx8hGah6qse0NDZcI5AYLlXlg3AxDRxbhcKU-4bAUzfEqNLXPHRTOFDccmMwQNYeqE9ADIvvpHeYXvGf3J_hFrLBsZKn9ToJCVcV7tbhVglI4eBk-vtbl2R_T6vX1NpVNcfXgkiWspUHdK0wSZ3Ak2jjQcST6iTBbnaYPkYIUuHtgzYvfIpAMslD5wX4ay798u3lfZKXueGF66hqpVK81Oy0nd3FY4kGvzwz4QH0v-3TPPbel_28_qRuTllPUwc9AUd90DlMTI8IibNiZBKLQtKuopgvxzzqg5vQMnf5afBTH5oYeDCHcRuag82bYagi7N129NNIkWkooSlZ7vj9neKg2IMKpK0wm_qdien5hs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91c58a6b6.mp4?token=Xe1dml8WqiHSN3C4GorWz-Sjp5U8XwIggTLcKoVsM6EBvaJSJeTOT5-tdqzT9Az0gpyq9ayNNR2as_3V7BVgkRVEp25RSL1udjdsLA4cSzFJpTu2QcLoiZ1u-5sPST1b_gAN8_YSiRQRhSaahZMQJGkqo0rmGnWNwWoGNHNSAuY0UXIAiPiColMoB8GCqZi_CMR0QMbj5NzsNKccFYsZFIunGBpAQS_fvRFsGBpR9CT9u3eXUIlzmb_MOYZW1cKk8D_UBUCBHIZorjdeuu8pXqirzlErgRtkdiSALvrrUQpJ0mdkBikhHfT2wNVj6wWUYdx8hGah6qse0NDZcI5AYLlXlg3AxDRxbhcKU-4bAUzfEqNLXPHRTOFDccmMwQNYeqE9ADIvvpHeYXvGf3J_hFrLBsZKn9ToJCVcV7tbhVglI4eBk-vtbl2R_T6vX1NpVNcfXgkiWspUHdK0wSZ3Ak2jjQcST6iTBbnaYPkYIUuHtgzYvfIpAMslD5wX4ay798u3lfZKXueGF66hqpVK81Oy0nd3FY4kGvzwz4QH0v-3TPPbel_28_qRuTllPUwc9AUd90DlMTI8IibNiZBKLQtKuopgvxzzqg5vQMnf5afBTH5oYeDCHcRuag82bYagi7N129NNIkWkooSlZ7vj9neKg2IMKpK0wm_qdien5hs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس آمریکایی: ایرانی‌ها درحال تبدیل‌شدن به یک مرکز نوظهور قدرت جهانی هستند
🔹
رابرت پیپ: در نهایت آمریکا باید با این احتمال یا واقعیت کنار بیاید که فقط ۲ سناریو باقی مانده است.
🔹
یا در دام تشدید تنش دوباره به جنگ کشیده شود، یا ایران را به‌عنوان یک هژمون جهانی بپذیرد؛ چیزی که جهان را تغییر خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/435750" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns1EyTtjcVtBgP7iIG3y0BgnPNx6fv1DgQS2T7xEpy5St9cg5rGJOlZ2_RufnsL09CGfK-93f5R4gbByCVlrwHMqK3VzVg3rTwZwwnV_CJRh_SlQPD3BfIkeArv7oeOd-vvQTVx0GVA2CO3BcurfkQ5hdZrIw1leN5HaKyEnwSRwq0bEBSCurgNv5HpU3UptMG_DxiRvON5QbTj9mj73dfJTPpPlrlrYyews4Q7yumoKlT9LMzlizhclV2fxHALhNeHxdBjVm8cd4lND7QdBSJSNaDgWksncBmZM6O80UEFrAPer_s6oy6TXV0SeuN_j04Gv5DqeRWHcsxC_jHoaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکلیف عالیشاه با پرسپولیس برای فصل بعد مشخص شد
🔹
در روزهای اخیر شایعه شد امید عالیشاه کاپیتان پرسپولیس در لیست مازاد این تیم برای فصل آینده قرار دارد.
🔹
این در حالی است که عالیشاه با پرسپولیس قرارداد ۲ساله امضا کرده و فصل آینده هم با این تیم قرارداد دارد.
🔹
پیگیری‌ها از باشگاه نشان می‌دهد که موضوع مازاد بودن عالیشاه برای فصل آینده صحت ندارد و کاپیتان پرسپولیس قرار نیست از این تیم کنار گذاشته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/435749" target="_blank">📅 16:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انهدام مهمات عمل‌ نکرده در قم
🔹
روابط عمومی سپاه امام علی بن ابیطالب: در بازهٔ زمانی ساعت ۱۶:۱۵ تا ۱۷ امروز، عملیات انهدام مهمات جنگ رمضان توسط رزمندگان سپاه استان قم اجرا میشود.
🔹
لذا صدای احتمالی انفجار در این بازهٔ زمانی ناشی از عملیات فنی و کنترل‌شده بوده و جای هیچ‌گونه نگرانی برای شهروندان وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/435748" target="_blank">📅 16:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17331e6499.mp4?token=W3npOKk7T5qA8k_MoiWVJEpZLbRDKk-VRc-YRyguN-CI29kBH172F9_hP4mcaff0MHg2L68lqBeALXkVzhfpylh4epH562Fn5ppxsYsVIGb9IF3hZf12te0w8khuXWg-z3KIDDchwd6HzSI-w-bFOz_GkR_rdx5Y7e7JX3d_V-D_d9ImmvB4XEHzbGUCd93SQ8-oZC_brjcuYDU4DXqwXfS0Mz80jv2ksN0EkKaIw4EW7lGSuqC-mNXL0ZsInuK_ulfND92yd13N08JpFiLnqfM_V4u3CecKcCGS_NHllE8jVkB9VECEp13YH7faM_mhKceIlakhmgz23yn7_Dm0Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17331e6499.mp4?token=W3npOKk7T5qA8k_MoiWVJEpZLbRDKk-VRc-YRyguN-CI29kBH172F9_hP4mcaff0MHg2L68lqBeALXkVzhfpylh4epH562Fn5ppxsYsVIGb9IF3hZf12te0w8khuXWg-z3KIDDchwd6HzSI-w-bFOz_GkR_rdx5Y7e7JX3d_V-D_d9ImmvB4XEHzbGUCd93SQ8-oZC_brjcuYDU4DXqwXfS0Mz80jv2ksN0EkKaIw4EW7lGSuqC-mNXL0ZsInuK_ulfND92yd13N08JpFiLnqfM_V4u3CecKcCGS_NHllE8jVkB9VECEp13YH7faM_mhKceIlakhmgz23yn7_Dm0Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناتوانی فرمانده سنتکام از پاسخ به چرایی بمباران مدارس و بیمارستان‌‌های ایران
🔸
گیلیبراند: ما داده‌ها و اطلاعاتی داریم که نشان می‌دهد که ۲۲ مدرسه و ده‌ها بیمارستان در ایران هدف قرار گرفته‌اند. شما قوانین حقوق بشری جنگ را رعایت کردید؟
🔹
فرمانده سنتکام: بله.…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/435747" target="_blank">📅 16:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086b40b70f.mp4?token=pNf3ChHxwujm0nIZSlv-Zn3tyA4onKhuSDKkk5v63Oxk6PdSo7AgsB8-ojIBZ8eB-yI-AXds9clQhVsOjSPPecKivZA922M41bFRmvmFOKmc8MCd-du9Fi4WNup1Qu12fk-s5ir2SII8ar1-cklNI_ol_GggAgUjmVB1JmurnqKVsP_jAPyd3KhajHjQoeC7_756b0JfLQAyW7S4bYEQrpsSMbzcrBhtpBgO3ujuQOhRtDnkRg0wfmqooNZ4FdbzJc57tq4v_x4k5YHF9od5xYQAySrVZKU3aHYqOYHayU2YjJmTeDojp9Zwvfwjwq53XwXiAiHn4WgmxyAgNGmO1GdLDfi6-UmFVLkjoi0uUL-agpXIHkQDHyDF2DUQkxNSIff984KeEonLszjOL0ZN4IR7Ogt0TxKEtehXo3NT4t5y8-5hobdS9hHVWQZ9taHOVaKnTVL0rC-ypTzlzYpmweZusbjDrU9pnI0IFsfWTlMK5u4a5fb5hly79oKFhCEh7q-NVlOzqIo32fEFVEXLokzlivNAt5dOLvAxUTphArg0Jkn09T9JuDANfluOkf_e2QKblUC_QX9TR7mvB3G9N0c4RSICJVimicTUMGt5_7MzozMupn4SONWx0Bf9aclCZ4yq2kTgmb0xpDBs2Chlu1tTeJ1tO0A-jUFjOpuP2Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086b40b70f.mp4?token=pNf3ChHxwujm0nIZSlv-Zn3tyA4onKhuSDKkk5v63Oxk6PdSo7AgsB8-ojIBZ8eB-yI-AXds9clQhVsOjSPPecKivZA922M41bFRmvmFOKmc8MCd-du9Fi4WNup1Qu12fk-s5ir2SII8ar1-cklNI_ol_GggAgUjmVB1JmurnqKVsP_jAPyd3KhajHjQoeC7_756b0JfLQAyW7S4bYEQrpsSMbzcrBhtpBgO3ujuQOhRtDnkRg0wfmqooNZ4FdbzJc57tq4v_x4k5YHF9od5xYQAySrVZKU3aHYqOYHayU2YjJmTeDojp9Zwvfwjwq53XwXiAiHn4WgmxyAgNGmO1GdLDfi6-UmFVLkjoi0uUL-agpXIHkQDHyDF2DUQkxNSIff984KeEonLszjOL0ZN4IR7Ogt0TxKEtehXo3NT4t5y8-5hobdS9hHVWQZ9taHOVaKnTVL0rC-ypTzlzYpmweZusbjDrU9pnI0IFsfWTlMK5u4a5fb5hly79oKFhCEh7q-NVlOzqIo32fEFVEXLokzlivNAt5dOLvAxUTphArg0Jkn09T9JuDANfluOkf_e2QKblUC_QX9TR7mvB3G9N0c4RSICJVimicTUMGt5_7MzozMupn4SONWx0Bf9aclCZ4yq2kTgmb0xpDBs2Chlu1tTeJ1tO0A-jUFjOpuP2Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشنوارهٔ بازی‌های بومی و محلی در عبدل‌آباد بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/435746" target="_blank">📅 16:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435744">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32f04d19a.mp4?token=Jv8L_qJc6txO0H5zGPBmm7W9ouufTCOvxQ9Sc1BLJDzNZsuRepdO-7NK4jRxgVL64uu30ynOb24brVEAtAmygSs0kIZr6vdqZPNHfQ1yxBz-dZLlkXTnq49GdUbEGDsNnS5CJ3TRIO5NRbfMPEIbPkF3VRwmJ2J9AtmLLy-8Kk5KA_PjnolXXexRphtaauYLpkgqAznnzuohwUEpOY8CFfbATzoR3fjvMI65Nb0eU2aMFiBPbl6XCELkx1PDZ0LuChXaWGpX0fuhrDL2lx66yaD3IZ6kyybdp7XFiz_HTq8fwE7GxJ_lnWl51ie4McRk6itJW85W40U1AzT6eaEqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32f04d19a.mp4?token=Jv8L_qJc6txO0H5zGPBmm7W9ouufTCOvxQ9Sc1BLJDzNZsuRepdO-7NK4jRxgVL64uu30ynOb24brVEAtAmygSs0kIZr6vdqZPNHfQ1yxBz-dZLlkXTnq49GdUbEGDsNnS5CJ3TRIO5NRbfMPEIbPkF3VRwmJ2J9AtmLLy-8Kk5KA_PjnolXXexRphtaauYLpkgqAznnzuohwUEpOY8CFfbATzoR3fjvMI65Nb0eU2aMFiBPbl6XCELkx1PDZ0LuChXaWGpX0fuhrDL2lx66yaD3IZ6kyybdp7XFiz_HTq8fwE7GxJ_lnWl51ie4McRk6itJW85W40U1AzT6eaEqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ ترامپ به خبرنگار آمریکایی: شماها فیک‌نیوز هستید
🔸
خبرنگار: شما ۳۸ روز بمباران کردید اما به تغییرات سیاسی در ایران دست نیافتید.
🔹
ترامپ: «نه، من به یک پیروزی کامل نظامی دست پیداکردم. اما آدم‌های منتشرکنندهٔ «اخبار جعلی» مثل تو، اشتباه می‌نویسند. تو…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435744" target="_blank">📅 16:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435743">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf0f0db1e.mp4?token=PJWkzWOdQfX7dfEzTRUKfwVmy3-f8UvlspwcsGp-dtDkpdVp1B7KsjXwcDBM-rsf-utJEWRWmhFNsPSYjdDIEIpLtdYzdm355uylxxrwoTS4M0y6nkccKp1PPosVHnwMgQR-DYJnc3GrFrIK5_XAoryuIFyZYiy5tneAs2OYTvV2zBuweCblhUHnzWRrW4PZMa7EOQmCPnDV3Aejk3VsOyUyk-EgqSZfv-wTtxLMNZtcstLaXf5dgmS0ot15tgO0kLFBu1EKDOwDfgjRgsbCA7sD0yyjCjadUrnOT6rUwKsKM9BRxx_YfIJXU6u4L_v3cmf_3RbcqcSlodq-A70IYLQRrookAhR00uiJdbHEaRAvmzbFdGUzbK5blRV_l6yHBNxZkEFEIwyHtrwtMFYgXZ6ORWKZDVNRaNBCrpekhW9zU6HmlhydCXFVSKJ9azmXheJ73sLYTeKorr_35x7JXfORxc57wkkhqcPDU103SxYxKLYsYikd5_JRojmXKCv11wnRjjmVAYP_saTRbjK1ZoF3YHSTcD_S1yvEefmbIZnmU83MvkJXZi2ojbXYWuwjahqBMEaPvJCgLPdciSavMfVYvDdxlnYv55IS-wZj_EDY9LPQ8Y2H6uytXgKB1-GtEaSe2n10IwKbAp8mkhrLWwiDilbUJMfa1GPqTyyFmuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf0f0db1e.mp4?token=PJWkzWOdQfX7dfEzTRUKfwVmy3-f8UvlspwcsGp-dtDkpdVp1B7KsjXwcDBM-rsf-utJEWRWmhFNsPSYjdDIEIpLtdYzdm355uylxxrwoTS4M0y6nkccKp1PPosVHnwMgQR-DYJnc3GrFrIK5_XAoryuIFyZYiy5tneAs2OYTvV2zBuweCblhUHnzWRrW4PZMa7EOQmCPnDV3Aejk3VsOyUyk-EgqSZfv-wTtxLMNZtcstLaXf5dgmS0ot15tgO0kLFBu1EKDOwDfgjRgsbCA7sD0yyjCjadUrnOT6rUwKsKM9BRxx_YfIJXU6u4L_v3cmf_3RbcqcSlodq-A70IYLQRrookAhR00uiJdbHEaRAvmzbFdGUzbK5blRV_l6yHBNxZkEFEIwyHtrwtMFYgXZ6ORWKZDVNRaNBCrpekhW9zU6HmlhydCXFVSKJ9azmXheJ73sLYTeKorr_35x7JXfORxc57wkkhqcPDU103SxYxKLYsYikd5_JRojmXKCv11wnRjjmVAYP_saTRbjK1ZoF3YHSTcD_S1yvEefmbIZnmU83MvkJXZi2ojbXYWuwjahqBMEaPvJCgLPdciSavMfVYvDdxlnYv55IS-wZj_EDY9LPQ8Y2H6uytXgKB1-GtEaSe2n10IwKbAp8mkhrLWwiDilbUJMfa1GPqTyyFmuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استپلینگ، تحلیل
‌
گر سیاسی:‌ ایران امروز در قامت کشوری قهرمان و دوراندیش ظاهر شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/435743" target="_blank">📅 16:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435742">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37498dd7b3.mp4?token=RWKVocZdYYuUIdGlI16dPRq2vjVxLECcYEvcYCP3DyslESet7lN8TfQ7gi8urpJduv6ifH7IMyasuHp72DKaXsP6H7FXHYTlNnVEnP4zz-lDWF04jeoy8B-O_yQnPjbmSP47q_9IiZnmngLsNrAN5DI8qQZ_nDgqYoaLZn7OK0BqauLk7g_aqIEj1_38zeKf8EaacYEOlWKBErGKf1fQT-d3ob5bN6wKHxqZ3YCiL0XsLnNz4KLcaMV1-XFH8gAy1NoLXCV4AP7UveR0G7-HkHoOseZf7O1KwKAqJEO4zyGDxHWyiDJ9NMEXvbzFFo7T3i02WcIwTw5dk5v4pkfa3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37498dd7b3.mp4?token=RWKVocZdYYuUIdGlI16dPRq2vjVxLECcYEvcYCP3DyslESet7lN8TfQ7gi8urpJduv6ifH7IMyasuHp72DKaXsP6H7FXHYTlNnVEnP4zz-lDWF04jeoy8B-O_yQnPjbmSP47q_9IiZnmngLsNrAN5DI8qQZ_nDgqYoaLZn7OK0BqauLk7g_aqIEj1_38zeKf8EaacYEOlWKBErGKf1fQT-d3ob5bN6wKHxqZ3YCiL0XsLnNz4KLcaMV1-XFH8gAy1NoLXCV4AP7UveR0G7-HkHoOseZf7O1KwKAqJEO4zyGDxHWyiDJ9NMEXvbzFFo7T3i02WcIwTw5dk5v4pkfa3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر از جملهٔ اول یک پیشنهاد خوشم نیاید، آن را کنار می‌گذارم؛ در مورد پیشنهاد ایران هم همین کار را کردم
🔸
خبرنگار: جملهٔ اول چه بود؟
🔹
ترامپ: یک جملهٔ غیرقابل‌قبول. آن‌ها قبلاً قبول کرده بودند که هیچ فعالیت هسته‌ای نداشته باشند؛ اگر در نامه نشانی از…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/435742" target="_blank">📅 16:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435741">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFvkCno-QOuuas5AQrXsLp4jqvHD74Pir6J171Er08rgfOrkztCTshW6mdy-B7ucE4ajDAeWrmn7x83SdUmny-_esRrfMoaWiHPhZ2Z7s44szs0T_-pMNQ5HPqtwC0Lx4hnfTlFNsd0Hm62j0aniyPnrNK6eh7atZUO4OkpghGfe6VNrAhdIpaQdUAFzPqeRjPIwtxeP7Y2GsCx5zPNak5z_ecYM37ugpa4QrEdfpEzWHd6dCMhUHDu8_X7IIjwqkIN3PAVl7-bXZiJZ3_A8vw-it1rUpGyy9MkC-XqiXsMuvEkuBlRY-NO4jEpYfMvEViNwEuV4cHFBSz2SCiRlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی دختران هندبال ایران در اولین گام آسیایی
🔹
تیم ملی هندبال دختران ایران امروز در اولین مسابقهٔ خود در مسابقات دختران زیر ۱۶ سال آسیا مقابل هنگ‌کنگ با نتیجهٔ ۳۳ بر ۲۹ پیروز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/435741" target="_blank">📅 16:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b16e61a6.mp4?token=IONPudncGtI57n0TXMVTr1p_YdOMiXWY4550NcRnMHem_IVhAtR9P_YTgDN5A7vrIhirNR6xqchsBldSlYqj0HbBzhZzwMPDP-HyYp8p9W4sbC_H2A-pupBOEBHLnC216EHbv7zlmB8cXgbI6QyMsDDVu8JAm00D4B_grSVcwICAX6a_h-ASpnAdAFidMNyP9qaL6rgB-iHnfiyaoM_FSzHq-j3wZH7e7Ka4NpPsCUk9oK3mvkPhLj8ueoEWIQb54AtwHLlvMKWgkAIyauTtFofH06ItILpNQPV_7Izm93d_U3RW9NrwiLcQm3JWWVKqw_aVTxa3JXjZnV4LwW8h3DbLterGeoIx08b7IZk6IuUvhN7Lhmz3f85eA5K9Iu5DcGegZO1Wwpwux6pZvlK7P6h-whYoafg3bZ_MmR9SmkOxDb-2zg55i-You9JiZ6QvuyzcyUwZnw_661LlFeDajfGQGPt8SrJJE12zi0oatTT8iKrRmIqQC7XrHDGHxKzL8oEiaodjnqHFkLWM9QR9-W2i9TYQXBes6bARpfMIwFynqpw429Ij8JybHPZIO6YyfdyhSlNHppZecS0iQPtz-1LSdWv2JABrfd6uOZws-JkxldoO6QmIUECP2Nsvn5J_UPHTqTHweZKo74KZt2VZX6gbpTh67_iijCYMorhcwsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b16e61a6.mp4?token=IONPudncGtI57n0TXMVTr1p_YdOMiXWY4550NcRnMHem_IVhAtR9P_YTgDN5A7vrIhirNR6xqchsBldSlYqj0HbBzhZzwMPDP-HyYp8p9W4sbC_H2A-pupBOEBHLnC216EHbv7zlmB8cXgbI6QyMsDDVu8JAm00D4B_grSVcwICAX6a_h-ASpnAdAFidMNyP9qaL6rgB-iHnfiyaoM_FSzHq-j3wZH7e7Ka4NpPsCUk9oK3mvkPhLj8ueoEWIQb54AtwHLlvMKWgkAIyauTtFofH06ItILpNQPV_7Izm93d_U3RW9NrwiLcQm3JWWVKqw_aVTxa3JXjZnV4LwW8h3DbLterGeoIx08b7IZk6IuUvhN7Lhmz3f85eA5K9Iu5DcGegZO1Wwpwux6pZvlK7P6h-whYoafg3bZ_MmR9SmkOxDb-2zg55i-You9JiZ6QvuyzcyUwZnw_661LlFeDajfGQGPt8SrJJE12zi0oatTT8iKrRmIqQC7XrHDGHxKzL8oEiaodjnqHFkLWM9QR9-W2i9TYQXBes6bARpfMIwFynqpw429Ij8JybHPZIO6YyfdyhSlNHppZecS0iQPtz-1LSdWv2JABrfd6uOZws-JkxldoO6QmIUECP2Nsvn5J_UPHTqTHweZKo74KZt2VZX6gbpTh67_iijCYMorhcwsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر منتشرنشده از دوران جوانی شهید سپهبد موسوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435739" target="_blank">📅 15:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435732">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuRRYBDd3l6IkUu8HH53QzLlwmYtCaPMd7Tjm2cPApQKitiM80pk5JJRDkf6QeK2TfkfqR6HmlTIn_L_LNu2wNBsX5Grft-3JbLu7mv7__9zaxPnXRlLSsDAw07mmXjYY2Rba-6Sh72IT9bvBWgvESlqrKo0zcw6QmNZK6UO5ID0Er5dqSGJZY1gWIa81kAP4NNJFsVNjGyxDCQlmltFz5sgjbAzw33ZF2_a7vxNO9yRRB4-RT1Wgo8ujmG_PbHkVJytXNHQnYrJjwJvmteuX0HkFyRIVhXYgQ7_cB9z4GVYqnFQpvE4HK2h7jXus9HBixW5H03Ny-tzkucJBoVUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaTEx8u2G1SSqY9y7gVf8CJ96zUseNBJ8lktdz9q7Ru0pm3IguXw-lRHZT5pCvYnDSgXsi1Ws-lCKI7CVKR2aU_DMV0XL3Rqf2pSdFqnCcjbRj68jpZ1biHGjh6MBug2dow9ohVEgattCjl5aRLs_9kDMoe8FsaMHN2Rhtkm8zkmMHSuC44pF2wbHrco4nRaw5waYPJnD877CLFZdRYNIVf_pE7yolPxHJmQhRejaScFH_aTS7v7XHyZ5R4NtuStR-rALJMKf51VSC_7-Rb2qacvHR_9OhqBaJK4SU41993NUkqs2411Dm2Kf7Lm0nhnbghSTyVIb2c7scsadZ6Agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DaOKlFqHvKxDbjSNE38P7NP7NkmYarixq8DScsONsQunS1uWN5g7ixfMo33jTdBEauJxtSYSd5OJhMaDKPq7Rc6yIXhXN1la37QKIGWMJWx5yrieybFrrgF0rZp39E5MK4JTZPrzApIy9OFVMI2JzJxR10h1kvE-N_Z1Bp5oHXBJcFsO_O3WKbh5Hi57SA291cCKUvxBgy7HsPe09z_2pRMNUCw9gvJwkDXi_n6--dO6NbcG6NOLkltn2SsFa5hPqjeAlnj__tiTXoR39S4JC_2IjJ5pEIhE-S-Ge2kbdahmO2qo5I3I_H23tet5Io-2iSRoNaCD-GbGLFLjf0ja3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6mF2EErXlUBXcfGDIbUy2q8tpH6eDE7vdc46W-KwjZnC9aLaK6dBcUZVe7APcHLUQAnNQTLmO3oAcjYz8lRf_NSFqBbUF-1kTSiwW6Sl0hhBXjMiLhHzIDV4vyoP4Zohkp6rBAbsRCIArMKStKd7P7owseApuTGFaN1WY2pgHyjsPupT2odfHyFzS-ALvtwuGA79DXwG_UZ5o1mvvqU5aVz2tllJz-rpIx4P8GlTonSqKfpNOvR2bTdgGus8jbAuR7gAmNRg-OddRxmh7LM16DEAT9HKvqQofjcwFnhXYz60zVMp-IJSWn6Nvt6aXu71f4CrQPYgs0xHZQjKnKJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5LP6dkrg_jU4UKuEPiJa_QxiiHE5yRLMuW4UK9ufoba69Gu_Sfzvum_kgq97NSv9tyjO5-y9PwFeuXUo-yoXKl3x_OoXNJM390od_IVXPRewjWW-NUIU7ZRnwS4Rm02yB2L0wpHtqEk7XIQvueq5KVdqvqevTF_e90H295ctTaybrROWrPJTCzCyxK9Y77_uC30JM6Vx2U_U35JroNV0ETmziefiQbVlKZk-xV-W0FjmPI30tgle1vFbQQuN7e77-Insr2NI3N2oqw1LJYqCc-xADEZKB1gGn4mlZHkgewu9LgztgCZgIMYNLzW4yhTh9L7RqLGMSKbnK1hsMfHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AF1b3vQgblA5CGX7I4yC8NzDHJR7hbn6ytxpBC3pVJhZtTfGPKaYdyxNppzWhDuAr_wUSTFHVxoHYYavnZgp_4gLjRCQwQfnxYDWjBDhk1u3sl70pv0jVg6nukEbuzL3rgzQ3joY6QKcspKf_f86eodL4IjvCCfvi0XxHWM_fJfPaBZq9_lZ6NK7yQ4JDvcMcBg8xBvLv0krtOF47taOxKFCoWaeEGLf5HuBkryTgPkzF3D7DACBXpvVyUongIUY2VTinnFRjadfWiQcsTV0rrVLsTn-2oR5CbdEkuwachB7GJ52kHnxS9HjkQy3VX29kY--6484zDGJcCE-4uiVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_iuGTE5KEP_q36EgygIqZh4Lely74pvIuQNW1Na9770QuH8jq265ClIDamACXVswrcitFraKV_Ep8XUbzOkdtkWKa2AgSN-n9LEkiv7Af_1pXzE-LOjDKN-WKYH86_VXYtihVTxhrTP1f4jJxZI2TbgR6jZN8zGYgqQausGhyS_ovQp65O7oT1T3cHLvgWEznrOEwmX-sM85Q_1PIhdlLpx9mHPhs2WhysDqhvHkcIlsothuNTXD73OunzlHoj58dVGh2SB6HJySwYIQyH8AVdMhvWAtmTQifrNGo_1B5F67-fnx67B2ZxW0Hw46NnF_39ni5LkftyGBO-6HFtAmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیاه‌پوشی حرم امام حسین(ع) در آستانهٔ شهادت امام جواد(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/435732" target="_blank">📅 15:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435730">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXPkPm7G4Tg9B4214MIFGuGgqLN-yTl0xKzTc3NYIpg1yJL9mgM4P4pA58YAOIWdEr6WiSvXAZALjObeZ75o7O6UQBntmEHqvrABdtzzut0HjWWqKIWXwGV4TQDzKb6mkgHSzG6xHYf54gpLDmS8DOgpVOyOgliJnje7wwY7RtUggGlGJxa6Yh81hVo_Fa75ei8cArpvS8ueQfLL2xClbEYD05q9WnoPZSS-HayzWUEfzFxs5N5V9WZdELjaNNhOdpq7POEBRJ8QSaXwVHBPkblFmXcTobbPOL8Cj1m60q6Rw8excsJFretaB1JAo31buT2ng4v6NuD5-_gd4pbg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1IvVhaPky2BMhgKJhuDJUVJdXM-Tyv0le8IGSRr7P3DNZD9OQKNd0hfsONE74chlv-sjN1pa0LXlTEkwxZlOuYPbSqBQC0kvVkbhIXbikC5V2bvkZF8wC9nAJFtAmQtgF-_EHfg_1of8usIBjKLeaBt0-D0T_ne1S89D7sUGTcpYEkK0xhU7hsXQR0aUQVnsaDQphu4N2mH6IcbqmixlqQlMRIE1vrh2emesuLCcZusCNwPvXQZHyPHR_KSF6Joe2yNHdsRjimdL7LGJFokrBsE53xHta7dV64_ZfdJ1QRm72inJ79cXydMxzIUFifN5q3cKxmX7_dQJtXYfREXhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۲ مدال طلا و نقره برا نوجوانان بوکسور ایرانی
🔹
متین چمی‌پا بوکسور وزن ۵۷ کیلوگرم تیم ملی نوجوانان پسران ایران در فینال قهرمانی آسیا با شکست بوکسور اردن طلایی شد.
🔹
همچنین فرزان احمدی، در فینال وزن ۷۰ کیلوگرم مقابل حریف ازبکستانی نتیجه را واگذار کرد و به مدال نقره رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/435730" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435729">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJEgN6Csc3Oks0P6KN8tbR17tDgcj8nRGhCAZYSYbIv44XTmGn7yopmd9mNLH69nJE4cg0a-2oakFXXhxTuR_Re8QoWfdThE9lxA2BmnKhVmOK-zzvhaqB1UCdKJMme2CQSfLDBp0a5oaPhLRfi2T_Rmv6ddJTkjSL_vJ3yFd49r80E_Glkn2YU2JcgccKoOSD98KdogoRNyy2JyWO9w5a4lhaq3msl2KgkUm-6WFlnknKVqCLzvwOCgAg2Y2GUZ8FGuOrG_UnlfJ-yfIL9yVemrmfUgrY4gqobTJ51wDqEeTzuxZCWVoD_tGlBCQ8u0tDVyCNrXdxynvaOvbRSlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها باز هم مصوبه دولت را پشت گوش انداختند
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد از بستهٔ ۷۰۰ همتی مصوب وزارت اقتصاد برای تامین سرمایه در گردش صنایع بعد از حذف ارز ۲۸ هزار و ۵۰۰ تومانی تنها ۱۰ درصد تسهیلات پرداخت شده و ۹۰ درصد پرداخت نشده که به توقف تولید، کمبود کالا و گرانی اخیر ختم شده است.
🔹
اواسط دی‌ماه سال گذشته بود که دولت اعلام کرد برای حمایت از تولید و جلوگیری از شوک به تولیدکنندگان درنتیجه تغییر سیاست ارزی، ۷۰۰ همت تسهیلات سرمایه در گردش مصوب کرده و به ۴ گروه از تولیدکنندگان پرداخت می‌شود.
🔹
ابلاغ این بسته به شبکهٔ بانکی اواسط بهمن ماه انجام شده و قرار بود همان زمان به تولیدکنندگان پرداخت شود اما بعد از گذشت ۳ ماه تنها یک دهم تولیدکنندگان موفق به دریافت این تسهیلات شده‌اند.
🔹
مدت اعتبار این مصوبه ۶ ماهه است و بعد از اتمام آن بانک‌ها دیگر الزامی به پرداخت آن ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/435729" target="_blank">📅 15:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435728">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d30b2d935.mp4?token=uuplcM_yRTgMyFAcq-zJTT82BWM8M6Grn5Sl1BRPeMcsU6tOnNZdR7-XwD6AC1-_9G9ffpExLoD2Y4ulhbX0cyS3kGFYt_U4THN8Fdth_T81XPQOVnshN8GyXyj0kgfWESphTe2212eGDH-eLP1JzEXSzfXSfPcs_EFYeOs0tSat1bAOWNStynraHYn0DuSy2yeKZl9wV3mGNaYkip5yeWhLPcgbRNDukTGNttuofVk-9CeRtEpWqN_8PVzu9mxHoMnI4J-S8Yk3iVj09TA1FLAlvLg0r04fx2IRuYKUp7gtZI2d1fq7bS1i_GS6NbHx9etpxL27-wBcVrJT2viMOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d30b2d935.mp4?token=uuplcM_yRTgMyFAcq-zJTT82BWM8M6Grn5Sl1BRPeMcsU6tOnNZdR7-XwD6AC1-_9G9ffpExLoD2Y4ulhbX0cyS3kGFYt_U4THN8Fdth_T81XPQOVnshN8GyXyj0kgfWESphTe2212eGDH-eLP1JzEXSzfXSfPcs_EFYeOs0tSat1bAOWNStynraHYn0DuSy2yeKZl9wV3mGNaYkip5yeWhLPcgbRNDukTGNttuofVk-9CeRtEpWqN_8PVzu9mxHoMnI4J-S8Yk3iVj09TA1FLAlvLg0r04fx2IRuYKUp7gtZI2d1fq7bS1i_GS6NbHx9etpxL27-wBcVrJT2viMOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!  @Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/435728" target="_blank">📅 15:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435727">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EroGAQq9_0k_Q5Z7y5mjC0llJe7pyK-pR7cT75LC5ZvF07EYLNrnNFVAp-0yGBl6xNOOiKK-k2jd6Pu9XK1azj7r74NHCHvdvtu-ZUIKzM4SWNT6nP2TpW5US9Ykt_iaGMhgbwl1xpPeK4Rk2aKhJXYHmnTIVLJhqJ2UOCk_KmxpnMXZgoKdgK5bYZJEDBK6wFvJZdGu-SBlTumcIcvTYu9I2LiQMxJfFKijST5gh_iNyPsuNwAKUSBtmNVIDBv_1oGlwKPFaxHq17ph0NOI58aJKAFXxsn6EFb894pCNd4C6wbDEHbavupC8ngg5p9Hr2XtaaOiyfpKH1WelV0zwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزهٔ ذخیره‌سازی ایران مقابل دسیسهٔ آمریکا
🔹
وزیر خزانه‌داری آمریکا می‌گوید بارگیری نفت در خارگ متوقف شد اما شرکت همراه آمریکا در فشار به ایران می‌گوید، تهران تاکتیک عوض کرده است.
🔹
شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران، تنکرترکرز می‌گوید، اگر ظرفیت ذخیره‌سازی جزیرهٔ خارگ پر شده بود، نزدیک‌ترین نفتکش‌های در دسترس را می‌آوردند و آن‌ها را پر می‌کردند.
🔹
یک ماه پیش ترامپ گفته بود خط لوله‌های ایران منفجر می‌شوند، تنکر ترکرز اعلام کرد، بدون درنظر گرفتن مخازن خشکی، ایران یک ماه و نیم زمان دارد حالا ۲۴ ساعت از ابراز خرسندی وزیر خزانه‌داری آمریکا برای توقف بارگیری نفت در جزیرهٔ خارگ نگذشته است.
🔹
این‌بار هم این شرکت که پیوسته در حال پایش نفتکش‌های خالی ایران است، توضیح می‌دهد، هنوز هم نفتکش‌های زیادی هستند که ایران در آنها بارگیری کند اما تولید را کاهش داده تا با افت بارگیری نفتکش‌ها هماهنگ شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435727" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435726">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b95147575.mp4?token=Q9EK2sAOmsMEtA0swmCbfIim10BGs52OuTFkt_3wYXNBAmNmBQp_eJ43zJL0NTcRgaNqGAP3-ovCqeutz4zMj4ohYN5_QRDORAr52kHmFILBLUM8yq3eVmml8H8MR0xzmTaUHROXDnk2mIR73KLhcCP1WzsMvMoKdag6uRSJFdSoROlTXyDl4NZTYC4BYnfi8EMKRHLbVTu6KvPVJh2La8q0nxaRwtEbco_fyECZqaoM1ypU5P45S7zNLpoyiZ5HXCSnYaKGj9MRtyjnFpmkTRvm8p-NRiY52SNbZssTqIAB5pqao0Q8o6ybrveatnZTj3RZ3rKqJhvyqyj_Ir2JWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b95147575.mp4?token=Q9EK2sAOmsMEtA0swmCbfIim10BGs52OuTFkt_3wYXNBAmNmBQp_eJ43zJL0NTcRgaNqGAP3-ovCqeutz4zMj4ohYN5_QRDORAr52kHmFILBLUM8yq3eVmml8H8MR0xzmTaUHROXDnk2mIR73KLhcCP1WzsMvMoKdag6uRSJFdSoROlTXyDl4NZTYC4BYnfi8EMKRHLbVTu6KvPVJh2La8q0nxaRwtEbco_fyECZqaoM1ypU5P45S7zNLpoyiZ5HXCSnYaKGj9MRtyjnFpmkTRvm8p-NRiY52SNbZssTqIAB5pqao0Q8o6ybrveatnZTj3RZ3rKqJhvyqyj_Ir2JWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: لغو تحریم‌ شرکت‌های چینی خریدار نفت ایران را بررسی می‌کنم
🔹
من هیچ درخواستی از رئیس‌جمهور چین در رابطه با ایران نداشتم و از رئیس‌جمهور چین نخواستم که برای بازگشایی تنگه هرمز بر ایران فشار بیاورد.
🔹
درحال بررسی لغو تحریم‌ها علیه شرکت‌های نفتی چینی که…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435726" target="_blank">📅 15:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435724">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C10lKxALjOCeYxh-AORHqtzEjoJX2RjANiVMAXZyzhXZ0i7amfNbdRbvhndP-XPIKfm0RADvwyizoPKGeW5yaB_sHlQmmcPK9kWHUhG1foq8dbtYEDWInxz4CHX_UmYk0tnHKSZu94eCBRHwzMH5CCapA4p3RdlGbgh5_pVU9R8UIiJ8EbDsYMy3JmGkxp8kIACchep9c1t3BRPYNEsaWaUPevErCQgauGMHXdcTSU82U6y_n__4V6JXwOo94vX3UrxNDIKGvs2zlsZOeV-oEBz-lE2zCv1UmwvzSzi42821en9F9fOEjuiifEPbN0qab8-jMc4m1FGU4I5WpqZ36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریکس خواستار استقلال فلسطین شد
🔹
وزیران خارجه کشورهای عضو بریکس امروز از تلاش فلسطینی‌ها برای تشکیل یک کشور مستقل و رسیدن به آرمان‌های خود اعلام حمایت کردند.
🔹
به نوشته خبرگزاری «اسپوتنیک»، در این بیانیه آمده است: «ما از جامعه بین‌المللی می‌خواهیم تا از فلسطین در انجام اصلاحاتی که با هدف تحقق آرمان‌های مشروع فلسطینیان برای استقلال و تشکیل کشور انجام می‌شود، حمایت کنند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435724" target="_blank">📅 15:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435723">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G71FGtBVippAIZ0Q5amZEDj9F5YeLd5zdBK_Rh7RIDROiAun0cWMjIDY9X2mnYD085mMx6T2psvL9MJZqg6oY5OKITqfYGwJzUdHFAe4TZrjsuRJuzNlYRwy_edS8z3ZDAuEdTJshHI2jTYSpiGKfGIfPe3sx83xC9omSBxwNo4TUdg984wXEYH8Y8jpYKtLzTjXY1xtAM6lGoSs75K7vaudngPudhb9q65MLsCmHHjJUttGowUfitXayPzRe3ogpoXSOwQQth0PwcEiQMkOIVby1BfDZQymQgsekPUKtIkjrHLq8yq7Ykb0qPZdtrPRoK172BKpA87Y_5HFCy8RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: لغو تحریم‌ شرکت‌های چینی خریدار نفت ایران را بررسی می‌کنم
🔹
من هیچ درخواستی از رئیس‌جمهور چین در رابطه با ایران نداشتم و از رئیس‌جمهور چین نخواستم که برای بازگشایی تنگه هرمز بر ایران فشار بیاورد.
🔹
درحال بررسی لغو تحریم‌ها علیه شرکت‌های نفتی چینی که نفت ایران را خریداری می‌کنند هستم و به‌زودی تصمیم خواهم گرفت.
🔹
ترامپ در بخش دیگری از اظهارات خود مدعی شد، من هیچ تعهدی به رئیس‌جمهور چین در مورد تایوان ندادم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435723" target="_blank">📅 15:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435721">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6ee_w0VW-u2UXDe-tRlofcK_Me-9-dnd_DOtEWi3hkq4nmh2jmDJtpNjDsxephd___EccSvJH51IM_gCyfILEPGe26b3k1GtfW5nAIRSVmJI-zHzhjUAxAMmzn0xqioRn2amBMIFZmOiSd2IqsLdnHjEvv0-hneBwp6P5Ga2dneRHmvH99WKPWLc2n-CkUaY67oNDFHg9m7EEtH78YVP2ROU-6qbOat2Tor0xX73lJ_X8sNA75zT-jxIvR0vUOkv48fIdd0WP0CuHyaO14DPjF5XW2iuAH_2sqL5l2syi1C_ImlPaTpveoLzmpTsSTTOpfUoS9isr4fHjEnrMYhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام تبریک پزشکیان به نخست‌وزیر جدید عراق
🔹
جناب آقای علی فالح الزیدی، نخست وزیر محترم عراق، کسب رأی اعتماد پارلمان و آغاز به کار دولت را به شما و مردم برادر عراق تبریک می‌گویم.
🔹
امیدوارم در این مرحله جدید و با تکیه بر پیوندهای عمیق بین دو ملت، شاهد فصل جدیدی از همکاری‌های استراتژیک باشیم.
🔹
ایران در مسیر توسعه و تحکیم امنیت در کنار عراق خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/435721" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435720">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9429126ab3.mp4?token=Cwkr1qZHoRTDNWiZ1Au4Gb0lBcmziHKoB7zBGEjlp0pYcVm3vtGdM24udhE1XEjgLkiX9Qd8ipY1OP_iRZmJJhnZC0SANZq0GSMLmH4YeCg870m0j4fBo_0fiNqgBLfX-QNSTEKlYPPUr7S-3f6ec_gowJyVgRTw3uCWuKAdJNRhpRpLEQ0VeIMZ6FJbPVgKJlxf5jedOQHD4KTkHZ54_LjodvKiDcmLpaH-Am4qSoZRbPmNss27NeDEN9ovFc6ge7S3vEerl0bxGysLBQBvRmJtPvPFy70ZHS4ffuHacAvTdO91O3eT5I_vg9Rcc1mltbMeO9hhKnWjXMMkZ6MUPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9429126ab3.mp4?token=Cwkr1qZHoRTDNWiZ1Au4Gb0lBcmziHKoB7zBGEjlp0pYcVm3vtGdM24udhE1XEjgLkiX9Qd8ipY1OP_iRZmJJhnZC0SANZq0GSMLmH4YeCg870m0j4fBo_0fiNqgBLfX-QNSTEKlYPPUr7S-3f6ec_gowJyVgRTw3uCWuKAdJNRhpRpLEQ0VeIMZ6FJbPVgKJlxf5jedOQHD4KTkHZ54_LjodvKiDcmLpaH-Am4qSoZRbPmNss27NeDEN9ovFc6ge7S3vEerl0bxGysLBQBvRmJtPvPFy70ZHS4ffuHacAvTdO91O3eT5I_vg9Rcc1mltbMeO9hhKnWjXMMkZ6MUPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندهٔ خبرنگار صداوسیما از آب‌های شمالی تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/435720" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435719">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7bd7aa02.mp4?token=S26HMR8hey_MUSOfjyTVtAWDdDakEz8bt3jeWb0XOYhJU77Fq00AhA-55782K7oU1PR7Or2HjhcI8arOlNuDDEM4n2ujRf4-0uQFWCYcjETrX5VCwgjymstnor3rRzWZEHsQfmTd0yRXLNcU9GtNRBQb4nuWgcZsNY4Dd_KBF1rvuqNthx3xor5D3hZ7wrsw4du_toG-8nqe1vY7_Cc89c0fmX5wm1BnguXfPLxysmtge_MCeE0CiKibgytYGsj1jQh90neKU4hnbUTbBOSx_2GRtZXEM-yzubjM_0Mfc-DYFVNkxUJIkqlVsPDJrf64Xz2IqyL3nfi7rnEFWPLDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7bd7aa02.mp4?token=S26HMR8hey_MUSOfjyTVtAWDdDakEz8bt3jeWb0XOYhJU77Fq00AhA-55782K7oU1PR7Or2HjhcI8arOlNuDDEM4n2ujRf4-0uQFWCYcjETrX5VCwgjymstnor3rRzWZEHsQfmTd0yRXLNcU9GtNRBQb4nuWgcZsNY4Dd_KBF1rvuqNthx3xor5D3hZ7wrsw4du_toG-8nqe1vY7_Cc89c0fmX5wm1BnguXfPLxysmtge_MCeE0CiKibgytYGsj1jQh90neKU4hnbUTbBOSx_2GRtZXEM-yzubjM_0Mfc-DYFVNkxUJIkqlVsPDJrf64Xz2IqyL3nfi7rnEFWPLDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/435719" target="_blank">📅 14:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435718">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMHGCppTegNaYob4afUHoK8y39fm7cjBRqfyXcmIIvZKAyaiimCD-oIhWCLC9J0VVnfcCayaaq3w1AwQi1AMvadflt3pvn09ZG9W2HLsJrj1KTLpk7aV3IDLSp3kmHnRJZ0_JuQyTLO-KTTX2Rk6pagLd7S6vs9_1WVCfSqawc9elexgUEk-ua7RnIHTDbDekRuZ8UyYpdTuF36yrycC_YYCFaosWjV22EtmxAgXofSO1nDhBCpAi-wGWTUHvGsSexhry5foLg8Yz0OWk_Sge_v-OaYD7wsf87UVfdJs0aLEVZclf1hrrXcezMwnNVqQiR4FCX4UeLnZ41bx72IfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435718" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435717">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435717" target="_blank">📅 14:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435716">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی: ما هیچ اعتمادی به آمریکا نداریم
🔹
وزیر امور خارجه امروز در نشستی خبری در دهلی‌نو: کشور من تحت تجاوز آمریکا و اسرائیل قرار گرفته است.
🔹
در حین دیپلماسی حمله رخ داد. از کشورهایی که این اقدام تجاوزکارانه را محکوم کردند مخصوصا دولت هند که ابراز همدردی…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/435716" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435715">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی: با پوتین دربارهٔ اورانیوم صحبت کردیم
🔹
مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم.
🔹
با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم؛ از پیشنهاد طرف روسی متشکریم. البته این موضوعی است که باید در جریان مذاکرات دربارهٔ آن تصمیم‌گیری شود.
🔹
موضوع مواد غنی‌‌شدهٔ ما مسئله‌ای بسیار پیچیده است و اکنون با آمریکایی‌ها به این نتیجه رسیده‌ایم که چون در این مورد خاص تقریباً به بن‌بست رسیده‌ایم، بهتر است بررسی آن را به مراحل بعدی مذاکرات موکول کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/435715" target="_blank">📅 14:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435711">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0beUrNOL3ofVdIlioqo47nJUEAqT2b3uZnmEAD0vYgC8nqP25F_iwPgKpxj3EpAeeRpioJrrNYQ-zIHIxl58vKDOKvabKnRv_BMgSWlxL6AmAepOLb9mYECsRZAFhPGrSWhxOKekutu7SZXiuuFHAA0nBUefcMS15qH4FSKcFZCrgFnxym5z3PltccW1A0D18sFgJxqAT7qnLpzr1Flu074myDDJL7TDNbKgbctHrHQicmWw892d3fvo-HxhXi1cIRVHJyVDRqr4-bcZe2IWyjOH7USu_RsF3GjeiUoSrhcpb8dgrMZHpQVF-aEfPavQAumIXaC90-HfLfNkxAcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام رهبر انقلاب به مناسبت روز پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی
بسم‌الله الرّحمن الرّحیم
🔹
زبان فارسی علاوه بر ابزار گفتار و نوشتار، قالب شناخت و رشتهٔ اتّصال اندیشه و مرزهای هویتی ایرانیان را تشکیل می‌دهد. زبان و ادب فارسی یکی از بزرگترین ظرفیت‌ها برای ترویج فرهنگ و تمدّن غنی ایرانِ اسلامی در گسترهٔ جهانی است؛ و توصیهٔ رهبر حکیم و شهیدمان اعلی‌الله مقامه‌الشریف به قدرتمند شدن زبان فارسی، چراغ راه اقتدارِ «تمدن ایرانی-اسلامی» می‌باشد.
🔹
ملت عزیز ایران در دفاع مقدس سوم نیز همچون دو جنگ تحمیلی قبلی ثابت کردند که داستان‌های اسطوره‌ای فردوسی، واقعیت زندگی و شخصیت قهرمانانهٔ آنان بوده و مفاهیم انسان‌ساز، سلحشورانه، و قرآنیِ شاهنامه، همهٔ اقوام و اقشار ایران را در حفظ هویت، اصالت و استقلال خود و مبارزه با «ضحّاک‌وَشانِ» متجاوز، همدل و همراه و همساز می‌کند.
🔹
این حماسهٔ حضور و دفاع و پیروزی، تکلیف بزرگی را بر دوش اهالی فرهنگ و ادب و هنر می‌گذارد تا همچون فردوسی برخیزند و بعثت هنرمندان را در امتداد بعثت مردم رقم زنند؛ فکر و قلم و زبان را با هنر درآمیزند و روایت خیزش عظیم ملت را در تاریخ، ماندگار کنند.
🔹
از سوی دیگر مقاومت غیورانه و پیروزی افتخارآمیز در برابر تهاجم دیوسیرتان و شیاطین جهان، ملت را برای پاسداری از استقلال تمدنی و مقابله با تهاجم زبانی، فرهنگی، و سبک زندگی امریکایی آماده‌تر کرده است تا با ابتکار و نوآوریِ فعالان عرصهٔ فرهنگی در جهت تأمین پدافند زبانی و گفتمانی و رشد و بالندگی کودکان، نوجوانان و جوانان، مراحل باقیمانده تا پیروزی نهایی را با استواری بیشتر بپیماید، بِعَون‌ِ الله تعالی.
سیدمجتبی حسینی خامنه‌ای
۲۵ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/435711" target="_blank">📅 14:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/435709" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عراقچی: آتش‌بس را نمی‌پذیریم، زیرا نمی‌خواهیم سناریوی سال گذشته بار دیگر تکرار شود
🔹
مصاحبۀ وزیر خارجه با کیودو ژاپن: ما از هر ابتکاری که بتواند این جنگ را به‌طور کامل پایان دهد، استقبال می‌کنیم؛ آمادۀ شنیدن و بررسی هستیم.
🔹
در حال حاضر، هرچند برخی کشورها…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/435708" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cafce2fa9e.mp4?token=o0EHBvkdi7zRHPd0m03_iay-yrjb2lv3lHRuT8uhmdy8XBoLNHk57YoAC9IhF9I_cPdWiepvcWgiw6SbKLxB3H8eOhVVHjsxAe6LMuUAF3M8g3vvhcQZUjsC9HA8YvKbQt98j35ADt5MuPX1zcZEgUluq9xhwWsplWg3m2Rc0vO4uzq0IT2M7dRuiY8cEJWx1vbtGaRpGNbclJs5NmuzaX0ntXr-NbOTul2xQuV9iRv43gxIkhjGCCWweE3ylD-plnRDQtO_WRzj_2Nxwf410zjaxa2nxXCAUYs3SJ1FFcre3xgy_LbM8a3j6SApCsCd0aIjP8o9GZ110r_SN-fCDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cafce2fa9e.mp4?token=o0EHBvkdi7zRHPd0m03_iay-yrjb2lv3lHRuT8uhmdy8XBoLNHk57YoAC9IhF9I_cPdWiepvcWgiw6SbKLxB3H8eOhVVHjsxAe6LMuUAF3M8g3vvhcQZUjsC9HA8YvKbQt98j35ADt5MuPX1zcZEgUluq9xhwWsplWg3m2Rc0vO4uzq0IT2M7dRuiY8cEJWx1vbtGaRpGNbclJs5NmuzaX0ntXr-NbOTul2xQuV9iRv43gxIkhjGCCWweE3ylD-plnRDQtO_WRzj_2Nxwf410zjaxa2nxXCAUYs3SJ1FFcre3xgy_LbM8a3j6SApCsCd0aIjP8o9GZ110r_SN-fCDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
او ۳۰ سال برای ایران جنگید
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/435707" target="_blank">📅 13:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fju2jFI6HunZULh4UUdgeerM5Ay4GguQpj8AFsSd1haXWlDcimGo1ubth9GZqmYRs-jScSTKTTxbmm_0vCXG-KEHKvuI81nCCdSwuY1H9hACy9BGGCNURmYv1oH-4XZWRNZ07jxR8p9fSx0fyUQJQcWWwWkMCKM25_maSC5XAQFQAEPqTycHu4YFTZqOw3Hj8eCaRaX1lDkAT6uKZGTtuTErBfzDtLw32oy69mIXyIe3QNDPMWW0BUwA_gAdvvkifkCZ_fvKeSLJqdTE1Vzbqh0MjziV-Lh-g0irnhb4qwgzBgbcL7vdwysS3Ok3iPoGW72AjdsnAyu1UZf8t9cpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که نگذاشت آرامگاه فردوسی ویران شود
🔹
وقتی خبر رسید که عده‌ای با پتک و کلنگ عازم توس شده‌اند، حضرت آیت‌الله خامنه‌ای بی‌درنگ دست به قلم شدند و نوشتند که آرامگاه فردوسی نباید تخریب شود.
🔹
همان چند خط، همچون سپری بر مزار فردوسی نشست و آرامگاه شاعر حماسه ایران را حفظ کرد.
🔸
سال‌ها بعد نیز ایشان آن ماجرا را چنین روایت کردند: «اول انقلاب عده‌‌ای از مردم بااخلاص بی‌اطلاع رفته بودند قبر فردوسی را در توس خراب کنند! وقتی من مطلع شدم، چیزی نوشتم و فوراً به مشهد فرستادم؛ که آن را بردند و بالای قبر فردوسی نصب کردند؛ نمی‌دانم الان هم هست یا نه. بچه‌های حادی که به آن‌جا می‌رفتند، چشمشان که به شهادت بنده می‌افتاد، لطف می‌کردند و می‌پذیرفتند و دیگر کاری به کار فردوسی نداشتند.»
🖼
اما دیدگاه‌ رهبر شهید انقلاب در مورد فردوسی چه بود؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/435706" target="_blank">📅 13:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3sT1iCRt5AH16xXMPJKNRYFsNyov51zs4vXJpue1-HSzBq8I5PqQvjfwAVlEB36c9E4W3Iv6mE9WDstVcFz35wxBUOxccMVKbsWFej93WqZ9YddNflE3ZDvfCYjyalECpKREr_FhXiTKeL9Y6wrb-R6t9lntFORwy-DuMth6rF4NH-pUAerdsULaTXy2eb8Tvin6VlLwLtbLEBmnC_2hUolDqP46ytRaVkyPVNkPUwXSIXBafw7MjVYf_61rXokOId6Q_pQXn7LPSyHrjV_Oer5Dlgt3Yw2hzDPovfBJk-unIc4kEarK1d2oJObPLiUUesAdRjtQzhqmdz5tEe3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: ما هیچ اعتمادی به آمریکا نداریم
🔹
وزیر امور خارجه امروز در نشستی خبری در دهلی‌نو: کشور من تحت تجاوز آمریکا و اسرائیل قرار گرفته است.
🔹
در حین دیپلماسی حمله رخ داد. از کشورهایی که این اقدام تجاوزکارانه را محکوم کردند مخصوصا دولت هند که ابراز همدردی و کمک بشروستانه ارسال کردند.
🔹
ما در وضعیت آتش‌بس هستیم گرچه متزلزل است ولی در تلاشیم به دیپلماسی شانس دیگری بدهیم. هیچ راهکار نظامی برای موضوع ایران نیست. در مقابل هر تجاوزی مقاومت می‌کنیم.
🔹
زمانی وارد مذاکره می‌شویم که طرف مقابل جدی باشد و در مسیر درست قرار بگیرد ما هیچ اعتمادی به آمریکا نداریم.
🔹
پیام‌های متضادی که از آمریکا دریافت می‌کنیم هر روز مواضع متفاوتی می‌گیرند. گاهی اوقات در یک روز دو پیغام متفا‌ت دریافت می‌کنیم.
🔹
برخی طرف‌ها می‌خواهند مذاکرات را به هم بزنند و آمریکا را وارد جنگ کنند و امیدواریم مذاکرات به عقلانیت برگردد و از مسیر مذاکرات به راهکار برسیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/435705" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/435704" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fc71f97d.mp4?token=lYOhyFfkgJx05hoc4H_DW7evyxE0ZSSyWzPdzchySSCZLe6zmznghfOL3AtcMZan6Xcc2gWF-jMk30h8s4kquon4EusGZ_RVylhzBseiNzMgfx-Ed9DSDLYk90ZOmdxiIi0neZCT2D3wTCKkS9JYktc-a-k_840aEzDo788pCMJjbi24zT7XRjm0gDUm8LYfnUKTaQo1vMzGYrk6ew42tx29gyqIJiLxEc8OlXYaoEQOnbLZrw9XNC64mOIevIhYfGTMLwQgShbJ8VMwsbyNvfuLwpg29VqTNRSnbMiP-jKF7_lDGhLrRLRPSz1gbCsV1HlzUR5khyTYKaODeNeoNi2zMkhZ_sI-JSeyaEEUFJQoOtwYDVybZFxZ4ZEbbeA0kkfcQsxi3IHrfDd3wyHacQYHxKXUnWAhW7cfgKEt2cnYVGpmPuYWSHgoKVKQooiCI2eoaQNtiX9y2h-d4ZMZP0QBzqPm4wcyY6O_t-ny_VJTAd6CQgzzV02vQHQZArqotvqziUqf7xNxPT7HNEwYKOktRNWjGxuBmHb6wLWnelLH082ZRHd8mD2CfyrONwtcRwXkcE1GHZGjX7vet3KEG3FapYS6F5naB46IFuSQJXpnu38ntlr1zmSjC_40riridbTVAisTeHURAQyxo8P3vRNoVRRi8R4fYMyV7ebSjm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fc71f97d.mp4?token=lYOhyFfkgJx05hoc4H_DW7evyxE0ZSSyWzPdzchySSCZLe6zmznghfOL3AtcMZan6Xcc2gWF-jMk30h8s4kquon4EusGZ_RVylhzBseiNzMgfx-Ed9DSDLYk90ZOmdxiIi0neZCT2D3wTCKkS9JYktc-a-k_840aEzDo788pCMJjbi24zT7XRjm0gDUm8LYfnUKTaQo1vMzGYrk6ew42tx29gyqIJiLxEc8OlXYaoEQOnbLZrw9XNC64mOIevIhYfGTMLwQgShbJ8VMwsbyNvfuLwpg29VqTNRSnbMiP-jKF7_lDGhLrRLRPSz1gbCsV1HlzUR5khyTYKaODeNeoNi2zMkhZ_sI-JSeyaEEUFJQoOtwYDVybZFxZ4ZEbbeA0kkfcQsxi3IHrfDd3wyHacQYHxKXUnWAhW7cfgKEt2cnYVGpmPuYWSHgoKVKQooiCI2eoaQNtiX9y2h-d4ZMZP0QBzqPm4wcyY6O_t-ny_VJTAd6CQgzzV02vQHQZArqotvqziUqf7xNxPT7HNEwYKOktRNWjGxuBmHb6wLWnelLH082ZRHd8mD2CfyrONwtcRwXkcE1GHZGjX7vet3KEG3FapYS6F5naB46IFuSQJXpnu38ntlr1zmSjC_40riridbTVAisTeHURAQyxo8P3vRNoVRRi8R4fYMyV7ebSjm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برت، تحلیل
‌
گر آمریکایی: هژمونی آمریکا در تنگهٔ هرمز به بن‌بست رسید
🔹
ایران به بمب اتم نیاز ندارد؛ چراکه ثابت کرده که با کنترل تنگهٔ هرمز، همان بازدارندگی و فشاری را ایجاد می‌کند که یک بمب اتم قادر به انجام آن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/435703" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoNAqZqb1kjpNopLu4GlJxPcP5b1wm8vWDSmGj4wjpN2WSv06BiveSreA3wUXMJEKH86IT-xoaK1x4WYcQG_v0sYNy6Zvivh9QCSpRco01l63kYbWkP6ErgrndKODWwuxXWeDpvUNrSKNfpnyNr4YfUgSStmoIZ-KNP_pvcVhp0Obuj5Q39yKgAi3XiGzUBZOjlw92qiU1jarfz6yKL9PJdm79QhAp-kmyPqtxuISfngxTE4lGAx3HEFCTjIiqjF7W9cQ2aXNtTb5NvulMiYBi4Abm5bvObttZ5CIPiiXo-RRsD6nXDWxLhEDEpFc0oaAbY3w5NbrDQVqjKiFRWhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب نماز جمعهٔ تهران: مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است
🔹
حجت‌الاسلام ابوترابی: جنگ فقط میدان احساس نیست میدان تشخیص هم هست، در دوران جنگ جامعه‌ای عقلانی است که به استحکام دورنی قدرت و تحکیم پیوندهای ملی، دینی و افزایش سرمایه اجتماعی می‌اندیشد.
🔹
آنچه در این نبرد مورد تجاوز قرار گرفت بخشی از حافظهٔ تاریخی و تداوم تمدنی ایران بود؛ آمریکا خواست امروز ایران را محو کند ناخواسته دیروز بلند ایران را به یاد جهان آورد.
🔹
این روزها ایران فقط در میدان نبرد و دیپلماسی اقتدار خود را به نمایش نگذارد؛ در میدان زندگی هم ایستاد و حکمرانی جوشیده از درون ملت را عینیت بخشید.
🔹
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است؛ تحلیل‌های سیاسی باید بر پایهٔ عقلانیت، دانش، گزاره‌ها و داده‌های صحیح ارائه گردد.
🔹
ارائه تحلیل‌های نادرست مبتنی‌بر داده‌های غلط و تحریف‌شده زمینه‌ساز تخریب سرمایهٔ اجتماعی و فرسایش اعتماد عمومی است.
🔹
امروز ایرانیان بیش از هر زمان به نگاه منصفانهٔ همراه با عقلانیت و دانش و دور از روایت‌های هیجانی نیاز دارند؛ زیر سؤال قرار دادن بی‌قاعده و بی‌ملاکِ سلامت و وفاداری نهادها، به اعتماد ملت و حاکمیت آسیب زده و زمینه‌ساز بی‌ثباتی ذهنی است.
🔹
جهاد تبیین با تبیین مبتنی‌بر دانش،عقلانیت، گزاره‌های درست، مسئولیت‌پذیری و تحکیم وحدت ملی معنا پیدا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/435702" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliGoLbWZhhLvZvWjXGhcIUFC9o2MQGTXFutKN4T8Bv_z-RboCANjMRgZhVJrSLDBnioI-NQQY6K6Tl0HyihV-vpSx6xOECK_e9IJNM_NWUdNq9kpfgCn0Oui1-ppNHELOzVv2FPyVPcdYmeDam94FfSkHYyZvo5fWCtgDJan3Ia37Ou6rS5hHwmUCt0zMoGL6C6C0D5ursW1Q_a8Wgs1431J_DqV-rBZ5feiF0_UQcsrKQ6E83lN0hkrQFUwH4RAbAuQ99O1dPUQfivlvJJwEBhJEDBPPhBORT8jud5NRNLOPn6853h8G_iEZivHRqaEHxrvVsQuVX-41IDLDVVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: حکیم توس میان پهلوانان ملی و دینی پیوند ماندگار برقرار کرد
🔹
رئیس‌جمهور به‌مناسبت روز بزرگداشت حکیم ابوالقاسم فردوسی: فردوسی با آفرینش شاهنامه، شناسنامهٔ تاریخی و فرهنگی ایران را رقم زد.
🔹
حکیم توس میان پهلوانان ملی و دینی ایران پیوندی ماندگار برقرار کرد.
🔹
پهلوانی در فرهنگ ایرانی و شیعی، در پیوند با عدالت و حمایت از مظلوم معنا می‌یابد.
🔹
امروز نیز ایران، عرصهٔ درخشش پهلوانانی است که در برابر تعدی بیدادگران، امنیت و سرافرازی این ملت را پاس می‌دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/435701" target="_blank">📅 13:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860008d3a5.mp4?token=bsHZf_ZZjDh3f59R7tHwfi_zgWlnbKAAxfjLpviZ-aFvzbz_jMWPT-rae3ipS9SeRHcGXOqz7w5ILjh8bciaztdqFIx3eD7htdPJYtJCWM2_ijdpAB63sYaJEBKSXV4emXy9WBXHebw0d6GIck0oGZTd0xf5WxCY6UifTJMKF4ja9E7YF1lmtibkL9vCVYh1e01ghqWJfZpHm3d98aza06gWZRvcYO3_lhS2w-iMQBBR0gbcJ35tPF_ZvTGRd-xlK3ZNBsuzghLqQd0yGv5BaP1r0UyBbemAliUDF8G1Zbd0wyKj8WDHkS7vjobfak2h2BtsRqmm6XRfjreVNCat6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860008d3a5.mp4?token=bsHZf_ZZjDh3f59R7tHwfi_zgWlnbKAAxfjLpviZ-aFvzbz_jMWPT-rae3ipS9SeRHcGXOqz7w5ILjh8bciaztdqFIx3eD7htdPJYtJCWM2_ijdpAB63sYaJEBKSXV4emXy9WBXHebw0d6GIck0oGZTd0xf5WxCY6UifTJMKF4ja9E7YF1lmtibkL9vCVYh1e01ghqWJfZpHm3d98aza06gWZRvcYO3_lhS2w-iMQBBR0gbcJ35tPF_ZvTGRd-xlK3ZNBsuzghLqQd0yGv5BaP1r0UyBbemAliUDF8G1Zbd0wyKj8WDHkS7vjobfak2h2BtsRqmm6XRfjreVNCat6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر کودکان شهید مدرسهٔ میناب در نشست خبری عراقچی در دهلی‌نو
@Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/435700" target="_blank">📅 13:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkMiFEf3rNLcdTP83rVTy1dYdAlUpp6tys9_2bkPv-PUmbESF5PAGdpi8AscL-MMK0T9AjMR39Vha8EuPmrFBGKu3P6WWRY_sAJ7w7RQQx4W3-yId-4mMqN_Suv-6R6xjgfJtFZLU8eyoEDY850Hglz9f3fFAIzDwO_A5lIj92ZldcWxmymEK5gySragfEFqLXeR8YisROU0L-BsXUyaRGvv55_oo1Sh3UJ9_m0Q3RyXlVFVx4bYJluPxSpI_6EbATPo07JXkTteMdByGJy4bjnx3U9NNwSvyQCm_NvbTo4TpvLo9RVyfP53VQoBx3macZklvv3bq0j5GU4bPbF0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت کشورهای عربی با درخواست امارات برای حمله به ایران
🔹
بلومبرگ: عربستان سعودی و دیگر کشورهای حاشیه خلیج فارس با درخواست امارات برای حمله مشترک به ایران مخالفت کردند.
🔹
امارات تلاش ناموفقی برای متقاعد کردن سعودی‌ها جهت هماهنگی واکنش به حملات ایران انجام داد، اما وقتی درخواستش رد شد، ناامید شد.
🔹
محمد بن زائد، رئیس امارات عربی متحده برای همکاری با آمریکایی‌ها و صهیونیست‌ها علیه ایران عجله داشت اما سران کشورهای خلیج فارس به او گفتند که این جنگِ آنها نیست.
🔹
بن‌زائد، شخصا با محمد بن سلمان، ولی‌عهد سعودی و دیگر سران کشورهای عربی تماس گرفت تا آنها را به حمله به ایران ترغیب کند اما هیچکدام موافقت نکردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/435699" target="_blank">📅 13:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حزب‌الله: درپی پاسخ به نقض آتش‌بس دشمن اسرائیلی، یک تانک مرکاوا در شهر رشاف را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/435698" target="_blank">📅 13:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYZRFpUy8WwormsFXzzUcbT1zFl1C-6SpTbPqljcTzOSoSj6YuXyiLMCCcnpyd1c6S_FHNgf6Ck3lZCG3pxmGO_F0WR29AlvVVPmP2sVEu7_B4XiIkDLkPgI1rfnUxwn5dy1-nznFRH2M_9l9CMfg4xOafHWP0VMvZPn72GoIgqf7TrYMnplGZ_JdpPMI1u33mUwW7PJrOYF2P50w8poEvSJVkDwmIzyTd3gIzK-dbqN40i4WDTcrwiPcBD7SHR-kjBXAlWwGUn3MRqoWvHriTwJAnF_VFfPsP4BEhiU3ymR70KoSd0261J4hroNb6hX8OufH1f1qxaFtoMquuXG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_v8nSHXIPmn09k4Q608zM75g-GUdA6IW77FwAn9JA0GCyYeHErHz5NLAO4Z95lM-kLNEPeQ234GNr2OfbYs0buurQtX8RZmeALS1on2HXsBrx2ZO14bx4waFf3uedZUrrKRBF_cK3KLv0guayrGeYNHMPm3r28ooJGI_v5Cko0FRaj83SNW-dCndGV3dfwy6Tr1eFzaZBRs4Q-SqKSy1HsM4EBfTTc45Yyvanpt5uClgID30-4LbJDrkEs4bnHnpS5hmDDi_6CddKyBiUpsohIMXmtU8XSn6ko0cbhBbgaH0af-MA3-QdHAAJqQIVJmcdGJeySKYzu_tmlT4JcIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IL8boFUUNxYrMwCcSo2x1WdCa4FXBReZeMnyc_QwDZEdbFHZgH0-ZIU3OhcKkzYJ65WpzEOjG8rF6hUaJycKDI_TxyzSyzDs9H29Ty6eX8Uuhy_ahK-0_646nxlE8-7DUyHIZN_9l4N2dKx-xQQP8G0paFKkNejhZQaevf55mY-iMAHe2IQ5aUVU97Gp4m4WYPSQDR3_6L8DbDJ1uTJyOJIx6wx1UJCAN2-VHJIEViqhdjtV-mWPTLGNcTGj6BtMZAhLF4Bk-szNCoe_ghvAa7g8OJoBpwBNcRgEK_yFAfHbgztv8O17JqYdWRMpKIp7q1iU0z9edndWnTuOzbbubw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خنثی‌سازی بمب یک‌تنی در عمق ۱۸ متری زمین
🔹
سپاه لرستان: پس از ۶ روز عملیات گودبرداری توسط مهندسی ناحیه مقاومت بسیج دلفان با بررسی‌های تخصصی، یک بمب ۲۰۰۰ پوندی از نوع mk84 را در عمق ۱۸ متری زمین در شهرستان دلفان شناسایی و خنثی نمایند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/435695" target="_blank">📅 12:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ثبت ۲۵۰ هزار دادخواست و شکایت علیه آمریکا و رژیم صهیونیستی
🔹
معاون قضایی دادستان کل کشور: ۲۵۰ هزار دادخواست حقوقی و شکایت کیفری در رابطه‌ با جنایات جنگی آمریکا و رژیم صهیونیستی ثبت شده و در محاکم و شعب ویژه دادسرا‌ها و دادگاه‌ها درحال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/435694" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8379f709.mp4?token=OJQGRW-mkeHxPCv9uM6aWaQdW564tDjdEUIv8SftTW7dJpIH3M614Ke9bsD2slgF2fKk6FyUH12xe-ETZbSxsXX6QRNMxSAGlWezVJnY9Ra_DEcxORk9-iEkAPZuG4FS9Kzxe5UIDx_VuGpyOdm11FiGKgxTOpOpMxi_h63gtWSALw5PDxLU1PCL16LjEwPpSfGuDC9GYn-ztncR8-CUhlaqszm6gDK78KU7IARLHjvsVT3PnyZ6sMqbopJMg8hDdSTM_haDPSDpF-S8YYqO8MZHx9u6XO7nKF9fj_n0HZh5KUJZO7xBFIH1VAAEeJyhuio8BUJebki5yLe-RvbMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8379f709.mp4?token=OJQGRW-mkeHxPCv9uM6aWaQdW564tDjdEUIv8SftTW7dJpIH3M614Ke9bsD2slgF2fKk6FyUH12xe-ETZbSxsXX6QRNMxSAGlWezVJnY9Ra_DEcxORk9-iEkAPZuG4FS9Kzxe5UIDx_VuGpyOdm11FiGKgxTOpOpMxi_h63gtWSALw5PDxLU1PCL16LjEwPpSfGuDC9GYn-ztncR8-CUhlaqszm6gDK78KU7IARLHjvsVT3PnyZ6sMqbopJMg8hDdSTM_haDPSDpF-S8YYqO8MZHx9u6XO7nKF9fj_n0HZh5KUJZO7xBFIH1VAAEeJyhuio8BUJebki5yLe-RvbMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ موشکی و پهپادی حزب‌الله به تجمعات نظامیان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/435693" target="_blank">📅 12:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2dab68a33.mp4?token=hIhe4zr6LhkoyE8c9bmJn5-TeNMrdB5HxCc-8V70rwIRJin72gPQisHfv7V7pUWZnlv1RQjZl8tzEXeqBZ9-08aNeRwSJycqXm-kuJh7-zlC3lE70kbH79-_WUsf1BAgwUnkSNoDc15y23QAYRUPhU8xp2RH-UzfHztTwKHu2fcB8MjyD0nl8V9GwhvBnptGkYLtlcJnPV7SH5fuDrYdtSWKnW0qEKrXknIB_0xaYSlWFccYep3NBizSdGi808f94xxqqJ6IEUzcrmWvDJEhZIOqDFjGWzuWEO1Vyhf8_8wWKoakQgaApbeqo6IEOnZXyEBHW_wRZZPeM0z-YQUJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2dab68a33.mp4?token=hIhe4zr6LhkoyE8c9bmJn5-TeNMrdB5HxCc-8V70rwIRJin72gPQisHfv7V7pUWZnlv1RQjZl8tzEXeqBZ9-08aNeRwSJycqXm-kuJh7-zlC3lE70kbH79-_WUsf1BAgwUnkSNoDc15y23QAYRUPhU8xp2RH-UzfHztTwKHu2fcB8MjyD0nl8V9GwhvBnptGkYLtlcJnPV7SH5fuDrYdtSWKnW0qEKrXknIB_0xaYSlWFccYep3NBizSdGi808f94xxqqJ6IEUzcrmWvDJEhZIOqDFjGWzuWEO1Vyhf8_8wWKoakQgaApbeqo6IEOnZXyEBHW_wRZZPeM0z-YQUJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتگوی تلفنی مخبر با مادر ۸ شهید جنگ تحمیلی سوم
🔹
مشاور رهبر انقلاب، در تماسی با مادر ۸ شهید «رستمی و کیالها» که در جنگ تحمیلی سوم به مقام رفیع شهادت رسیدند و اخیرا دچار سانحهٔ تصادف شده و در بیمارستان بستری است، به صورت تلفنی گفتگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435692" target="_blank">📅 12:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حملات پهپادی حزب‌الله به شمال اراضی اشغالی
🔹
رسانه‌های اسرائیلی از به‌صدا درآمدن آژیرهای هشدار در شهرک اِون‌‌مناحیم‌ و ۳ شهرک‌‌ دیگر‌ در منطقهٔ الجلیل غربی درپی حمله پهپادی حزب‌الله خبر می‌دهند.
🔹
این رسانه‌ها همچنین خبر دادند که ۲ پهپاد انفجاری حزب‌الله اهدافی را در منطقهٔ شومیراه‌ مورد اصابت قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/435691" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1yNlN5RUudHVlMJr25Fi9pNv21ZYPoIb25SwCYMezSfJz2LNgc64JyAGoPimoOV_A1mabozKDKFE6zuH0ayKrGmBXPe7F_CcQEr9_7BB0379QWV8uN8T0q-Vcz2s6WpUy3A5IgttnGCMmuq36XUJ67xPvaWyJUNezhpHqBhbR0MbEBmoDo8sNOO9V84AImF-ZTLtSWQwvTzAs_qdyjYqw6QnQnAjY9bDUXidiAvzoAQaG8oTkH9s1wsxagi7NX3PgqGQX8Qyt__7Rs4DsUXbigfmsBGMf6k1Rpd7XApf4UPjIk2J5IKkMh0wsBuLsZWV9VnbsWASCz1_2DYAqz4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجع دینی بحرینی: امام خامنه‌ای(ره) امت را به اسلام بازگرداند
🔹
شیخ عیسی قاسم: شهید حضرت آیت‌الله العظمی سیّدعلی خامنه‌ای(ره) چهره‌ای برجسته از چهره‌های انقلابی دارای هوشیاری و عزمی راسخ، و توانا در برنامه‌ریزی، و از آن دسته شخصیت‌هایی برشمرد که جان خود را در راه انقلاب و رهبر عظیمش امام خمینی رحمه‌الله فدا می‌کردند بود.
🔹
رهبر شهید انقلاب مردی کاردان، توانا و کوشا در بازگرداندن واقعی و راستینِ امت به اسلام بود که توانست وحدت امت اسلامی را در خط درست آن مطابق با راه و رسم اسلام، و تربیت شایسته، اهداف سازنده و سیاست موفق این دین مبین حفظ نماید.
🔹
انقلاب بزرگ اسلامی در این عصر برپاکننده حکومتی هدایت‌گر و هدایت‌یافته و عظیم در زمانی است که امّت از نظر علم و عمل از اسلام دور شده بود.
🔹
اسلام تنهاه راه زندگی شرافتمندانه است؛ هیچ سرانجام نیک، باشکوه، امن، پایدار، پاکیزه و اوج‌گیرنده‌ای بدون اسلام در کار نخواهد بود.
🔹
این انقلاب و حکومت اسلامی، آمدند تا امّت اسلامی و تمام بشریّت را از بدبختی حال و آینده‌شان در دنیا و آخرت نجات دهند.
🔹
جنگ امروز، میان اردوگاه جاهلیت و اردوگاه ایمان شعله‌ور است؛ رهبری اردوگاه جاهلیت را طاغوت آمریکایی، صهیونیسم گمراه، و یهودیت سرکش از آیین راستین موسی(ع) به عهده دارند.
🔹
در رأس رهبری آمریکایی «فرعون ترامپ» است و در رأس رهبری صهیونیسم «فرعون نتانیاهو».
🔹
استکبار جهانی بشریت را به سوی دو فاجعه بزرگ رهبری می‌کند؛ یکی فاجعه مادی و دیگری فاجعه معنوی.
🔹
جهان اسلام در برابر این فجایع استکباری، محور مقاومت اسلامی، فریضه جهاد در راه خدا و دفاع از حقوق و مقدّسات را زنده کرد، و بدین وسیله راهی پیمودنی برای نجات بشریت از این دو فاجعه را نشان داد.
🔹
اسلام برای هر انسانی که ذرّه‌ای از حقیقت را درک کند، حجّتی تمام‌عیار است؛ حجّت اسلام بر اعراب را روشنتر است و یاری نکردنش از سوی آنان ظالمانه‌ترین، تأسف‌بارترین، منکرانه‌ترین و عجیب‌ترین رفتار است.
🔹
اعراب پیش از اسلام دوران طولانی‌ای را سپری کردند، اما تنها پس از پیوستن به نور اسلام بود که به شکوفایی رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/435690" target="_blank">📅 12:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
گرامیداشت ۷۲ شهید جنگ رمضان در گلزار شهدای ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/435689" target="_blank">📅 12:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt7kmgTKyQwi9PfGu-sVD2Jnd3oWxjWgN0iUUg_SAxVzFD5dMa3ScXUatyzmmBt5r3wDq9p8k6SDNEwcLhfbVhrQExK0JuKB2MUW-J8PnQYLmeT31PlYIuwUsF-g7IyCKCT7_h4M4RB5zukItWDVQK38_is36KulMbQMfL6JyZBV3A7wu9iEpT2-CpNik5fiwAhupSuXydLTTpTrv0pSQgEauw2mWHM4r3fPdixz4GAC-DpdlfJUVfPvHgerkgji3n_bZe50oLJgjmnJeG02a-BaCopSd4H5qUdfbWm8BIO-QvhB8GgNmXUy4svyzeQLZ1g1xpcljCfm0mQmAtj1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم کشتی روسیه برداشته شد
🔹
اتحادیهٔ جهانی کشتی اعلام کرد که روسیه و بلاروس بدون محدودیت و با پرچم ملی می‌توانند در رقابت‌های پیش رو شرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/435688" target="_blank">📅 12:14 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
