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
<img src="https://cdn4.telesco.pe/file/jUs1LVE8IrJ08hliFzORbwkUEW7yzJMtJ5DnHfnOhMJowumlQS_p9Uc4QxDNoCSXAuOkrjXFNP--C0H6keMTcpJExkCFOmxop1iNx8NR4zrfz39Wf8SQITGZk5QOyXmZ3agjfW-z5WkKly8stk9vAeodqgIyDXgjuuJC_Gyb3aZgQhPUHUMjZJPcBiFEIsRfHDtvFvU99cu-Z0aJ0X_hniGXxJxChUvWNQZ9hCVMb0GRqie8iBFUQHPfQb9K3EMSGyynsFFO5W3HWBOIU69AckEKi9GStCyYsqbFskAyLbynPV8WGQo7hD-_yRQLx-xsYcj1SQydfrt9QscliLtuQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
<hr>

<div class="tg-post" id="msg-689971">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/momM9LwnqlM_hQZdZp8alYmL0oW4GQ6bngRCEbZUMSUHvSXjc023mIhuoufhieEbUvkFZ3zs2dZH_32J_51BYPtcWzDM5UrEkxuvakfrSuO3Vh7b-ZX6XUOp98Ccg71TYpZXAPqCk-pZ8EgxPJqnfvriBYAI912WegJRECIb-irHZNaPj8Ofgj0dBDVBXNswT9ioPrG_fnq8pCYabPHesagBAduu1OF7CL_B_OXy9dnY7nbbk-gUfYG0sst57chbOgFjPI9GaorNw2Ej6IwCdcBDTi3IK0gkeOP7irsA0-B8aVTgRW9Yx5Wud9cQLu8xR9k5q83DODvAlHeEmrVF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای یمنی: اگر عربستان سعودی سقوط کند، اسرائیل نیز سقوط خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/689971" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689970">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a82cb8bd.mp4?token=bsVEaDEW3xUUC875hx2AtvLbQ0tSliNxy6A9l47-vn8_6xwqP_ZYzTKm-YQNfgQyIdTxplxbDMSRRliyYHCMq6xH8g1Kc-L6dEVw2czTKgs9ZOZjkN5Atndjk97Jk6V9y7j5huG4iAyiCuhlcET_M56HUZXuo9sI4uZdWFcCbjZCH4cf6zUyvqpqaukUjL5ZwW2lytJFTcyrZrNpmbvKifBO0AL0m4lN0vqZ6e762hk2uL5Zf2RxbKbCiNIFYAt46BUmc9sNSwPwtIUyVyAG891bxNV9AiiCoooX6RVgU6Sh9MsmZ_Jgk0dQvgwikHjYVc01paWNtiwgSGg6YfNHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a82cb8bd.mp4?token=bsVEaDEW3xUUC875hx2AtvLbQ0tSliNxy6A9l47-vn8_6xwqP_ZYzTKm-YQNfgQyIdTxplxbDMSRRliyYHCMq6xH8g1Kc-L6dEVw2czTKgs9ZOZjkN5Atndjk97Jk6V9y7j5huG4iAyiCuhlcET_M56HUZXuo9sI4uZdWFcCbjZCH4cf6zUyvqpqaukUjL5ZwW2lytJFTcyrZrNpmbvKifBO0AL0m4lN0vqZ6e762hk2uL5Zf2RxbKbCiNIFYAt46BUmc9sNSwPwtIUyVyAG891bxNV9AiiCoooX6RVgU6Sh9MsmZ_Jgk0dQvgwikHjYVc01paWNtiwgSGg6YfNHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از بازبینی صحنه؛ گل السد به دلیل خطای هند مردود شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/689970" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689969">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF7BQ4OypPeKy65vJHCsHC53zY9Yb0x_AJCSiSjAy3RVOmSlnAetLv7rqeSDTTRa1esAMcuGTbTxB2_YHWRhjlJF04HU5M3s7tXmtGVv9tl9pgFrCYt3xzlFgwxZQvkjkQ1YHqVXzB4iJzsT6F7Q6OBgZe6PY4pNn-3-f3EYFxlCxGiaX26hIpW5W94zED63_M1TtFM4ZyjAN6zw26CkFIgA3QIoxkvISi8StFx-AoFo0rvsaiu6Dw5itAfk8vedQQfg7RMtkkl7nRFh2x_3qRMGtOzavy1gfSuImyOTmj2XfIPEPIS7U40L_egPpWMu8FirEwm2Lf6qpNW3mqLqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۱ هزار میلیارد تومان پول مردم توسط سازمان بهینه‌سازی قفل شد
🔹
دیوان محاسبات کشور اعلام کرد: حدود ۳۱ هزار میلیارد تومان منابع سازمان بهینه‌سازی، به جای تبدیل شدن به اهرمی برای رفع ناترازی انرژی و حمایت از طرح‌های واقعی صرفه‌جویی، رسوب کرده و موجب بلااثر ماندن ظرفیت‌های قانونی شده است.
🔹
دیوان محاسبات کشور با تأکید بر ضرورت اجرای تکالیف قانونی، وضعیت موجود را از حیث نظارتی، ترک فعل دانسته و موضوع را وفق مقررات، مورد پیگیری و اقدام قانونی قرار می‌دهد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/689969" target="_blank">📅 23:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارت یک ایستگاه پمپاژ دیگر در خط لولۀ نفت شرقی-غربی عربستان سعودی در اثر حملات اخیر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/689968" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689967">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50de393260.mp4?token=RenF57XWPbOsw6G0Q7XcEa_SHPnIFkyictWh_o2vCb66ngNAeDYjbJYRsFEmB_9RUWppH1CNox3agsie40zqKrIdHUwl2X5bdwulZBxW19dmqLthmRV4rYWGaAARxWlAYbSCL2Xz6XMaxNtHHew2T0KT5zWu4JDwy3we91LPGPnLfwU47lX5_OJ6rKHpc4X8-AVz5LZgichzQDTxq3ftJqHv08qV_xmGvvGVpvLlhD87VS8XPMRxlr0GYXwjc5XbatB-u_vHuRhzuGoISXl-mQBDcReOY4hOe5-8orRLhZf7J4v3bjc-hbPWFxbhF1CLHQIGDxzzSrAaPHsvtCsj4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50de393260.mp4?token=RenF57XWPbOsw6G0Q7XcEa_SHPnIFkyictWh_o2vCb66ngNAeDYjbJYRsFEmB_9RUWppH1CNox3agsie40zqKrIdHUwl2X5bdwulZBxW19dmqLthmRV4rYWGaAARxWlAYbSCL2Xz6XMaxNtHHew2T0KT5zWu4JDwy3we91LPGPnLfwU47lX5_OJ6rKHpc4X8-AVz5LZgichzQDTxq3ftJqHv08qV_xmGvvGVpvLlhD87VS8XPMRxlr0GYXwjc5XbatB-u_vHuRhzuGoISXl-mQBDcReOY4hOe5-8orRLhZf7J4v3bjc-hbPWFxbhF1CLHQIGDxzzSrAaPHsvtCsj4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت این روز‌های منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/689967" target="_blank">📅 23:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZVrWCSrYnpsKe-iAgXvKmcxpsBcyPXKsAZgDnRQMsWDDCz-tlw2ItExQJJDnsp5GSyrMjAKhcepWuZFMkJ2zIQf46K4gxGMWVHn6lYsQ3lodyRhND3ZxqYyE7vPfoinEARnjqx_dhC-lv2l6de9FQ7Z_hldy5tdl89mIsPYMwDUBVWUcr3IVt-j3PmhxDt-1QvnjgTVwOOSDbfJEZvzpS6Bwcq_z_9K1sTx-NcP3SDYToISuGjOZotGAc2FuKM6SlxohtagukvUe0DIVDiV6jhY5KRa6yPbGYtl_0AFtDrSzoj0IE3bQgjfTlwRsB9TqgNXMtcssB2bUlV0IrnyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مکس اوته، اقتصاددان آلمانی: جی‌پی مورگان همین الان نموداری ترسناک درباره ذخایر نفت جهان منتشر کرده است
🔹
موجودی ذخایر با سقوطی آزاد در حال کاهش است و اگر این خط به ۶٫۸ برسد، اقتصاد جهان وارد رکود نمی‌شود؛ بلکه فرو می‌پاشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/689966" target="_blank">📅 23:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
روایت مدیرعامل پیشین شرکت ملی صنایع پتروشیمی از وضعیت این روزهای هلدینگ خلیج فارس
🔹
تعطیلی معاونت برنامه‌ریزی در بزرگ‌ترین هلدینگ اقتصادی ایران چه آسیب‌هایی به همراه داشته است؟ عباس زاده مدیرعامل پیشین شرکت ملی صنایع پتروشیمی از وضعیت این روزهای هلدینگ خلیج فارس، از پیشرفت کند پروژه‌های پتروشیمی می‌گوید و تأکید می‌کند که منابع باید در خدمت پروژه‌های اولویت‌دار قرار گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/689965" target="_blank">📅 23:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4fiRzdwOhaeyySsEkgyQ2_Hiwkkwi8v4oFa8pycT-ll16yDphnXGJNRGRQeDlgovm-09wwHcOkPv8uJSh4aFSz9bSpxzSnHk5QbgLhgTroBok_XmJK9Drldw_GkYDWO_rIaqnTYx2G8fzt2SkVrfcUtT3GTt2BecHyh4sOMxb5Q3gV1t0MHT04XC2TIOOkzGCsS7m1SRFJHGuetzfPCK2NcGqzAiIwk4tXfFaeFACliUy4jJ66-JmyLWJOox_ENaVlVFfAifFGipM4skgrBbWRyBDocyogZh41ntdN_vjAFsDbn-tmARLsnj6v9yvG49Z9sHoTxFHw-iucmVhsR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل دوم استقلال به السد توسط سحرخیزان
🔹
استقلال ایران ۲ - ۰ السد قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/689964" target="_blank">📅 23:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پزشکیان: آمریکا ونزوئلا را در ۲۴ ساعت فتح کرد
🔹
آمریکا تصور می‌کرد ایران را مانند ونزوئلا در ۲۴ ساعت فتح می‌کند یا مدلی مثل سوریه را روی ایران پیاده کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/689963" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مسعود پزشکیان: این مردم ایران بودند که مقابل آمریکا ایستادند، نه تکنولوژی و فناوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/689962" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtbIRuqzG6sDpAcJnx0X4wE17l-7IbZUBdaiMNcBLreV93WJ3tZoDusJbxZwS3J-pFfj9wEch3zqfPjmFXojgXOGVXnx30v4z5PIkvxiA5vkJc_x83A9pCbPT3yoiu6VbVHepJW8o5NfQU-CwpugFK_m8hAGSDP8yisXi5KQ1vgEgAaXRWLD5B7fGLVrTsyNuvj48VOKd8XyvrGpNci_T7-LQec0Rw_8BD1mBLSq0g7f-N1CgAFqg9dNypwHE84MyeS4zigSn7DnlXoPnEQIyXZ-PGq8QgDtjUlYKxHO1sa25LRFrZ3yczEzcugc3RhgG71YQgMTYqBIw78c3DI7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده پارلمان کره جنوبی: ترامپ می‌خواهد ما را هم تبدیل به بازنده کند ، در نهایت این ما هستیم که در تقابل مستقیم با ایران تنها می‌مانیم و تاوانش را می‌دهیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/689961" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee0f916eb.mp4?token=IDxnxmkHSAflUjIZT4MY01ryqw-igh-4Uo0-3VpZU0_faGLK6BQSlGrJP_7VBMtimH7jdgo2VT-9eCB148_1-_mOSkOI3sNcJpjE4JyT83KwglW0V9vc9G9F5FnWlhbpgG-rW2OPqCRj6HpgqRz_MBcnBIkYYlc4TS_G4T_mcpOzJNSKry7fGMWM-O_Bp9v2TsVAA3cTNvJxHqkmFaYlhwU6uNzj0z2TH5o2ExFYfcPf2dkadZcLA6NUnlKe2cq9QKQeYAIezVwrq8JnjpDKWjDahPoVzthxYzfGB91xPce-9eiZxdg1jXuasA79dQEpW3K_xvXMwHIqlzqty09k_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee0f916eb.mp4?token=IDxnxmkHSAflUjIZT4MY01ryqw-igh-4Uo0-3VpZU0_faGLK6BQSlGrJP_7VBMtimH7jdgo2VT-9eCB148_1-_mOSkOI3sNcJpjE4JyT83KwglW0V9vc9G9F5FnWlhbpgG-rW2OPqCRj6HpgqRz_MBcnBIkYYlc4TS_G4T_mcpOzJNSKry7fGMWM-O_Bp9v2TsVAA3cTNvJxHqkmFaYlhwU6uNzj0z2TH5o2ExFYfcPf2dkadZcLA6NUnlKe2cq9QKQeYAIezVwrq8JnjpDKWjDahPoVzthxYzfGB91xPce-9eiZxdg1jXuasA79dQEpW3K_xvXMwHIqlzqty09k_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایرانی خارج از کشور: من را هم در پویش جانفدا ثبت‌نام کنید
🔹
همزمان با اعلام خبر فراخوان آموزش نظامی امدادی داوطلبین جانفدا ایرانی‌های در اقصی نقاط جهان خودشان را به این فراخوان رساندند.
🔹
شروع ثبت‌نام فراخوان آموزش نظامی داوطلبین جانفدا سه شنبه ساعت ۱۷ با ارسال شماره ۱ به سرشماره ۳۰۰۰۱۱۵۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/689960" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689959">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7857a3701.mp4?token=I2kGvZMVdfCebvnCC2qPcy8rUT1jF7y7MOhzWBh3u20WPvpM-IaCj5n1tRyp8M6dTUz0UccgHNgiZgcnktDUieFl1b7FTxOWST7AXlakhsdeuUZnCrTHShUP6KL1aZRRDMX7hOjYR9kZRzseX32rirs4DMMzt3tL7IoFPL8Yt__pHKwqJqmvJjL8Slf1fQ-uO8ARwRmwtgW-71NtlRbplIxk-SBA9nJ2BEEKSgojjhJ2VDQvHCWzgAXueYIhlGu85dbmX7LPY2bCLG5aWfu7GUlk5TO0woHJd-4yHiIkakdCpQ74Oi92REJouQXwmh13dA7Cf7YAclR4ICGF8r-Sig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7857a3701.mp4?token=I2kGvZMVdfCebvnCC2qPcy8rUT1jF7y7MOhzWBh3u20WPvpM-IaCj5n1tRyp8M6dTUz0UccgHNgiZgcnktDUieFl1b7FTxOWST7AXlakhsdeuUZnCrTHShUP6KL1aZRRDMX7hOjYR9kZRzseX32rirs4DMMzt3tL7IoFPL8Yt__pHKwqJqmvJjL8Slf1fQ-uO8ARwRmwtgW-71NtlRbplIxk-SBA9nJ2BEEKSgojjhJ2VDQvHCWzgAXueYIhlGu85dbmX7LPY2bCLG5aWfu7GUlk5TO0woHJd-4yHiIkakdCpQ74Oi92REJouQXwmh13dA7Cf7YAclR4ICGF8r-Sig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/689959" target="_blank">📅 22:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689958">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رئیس‌جمهور: دلخوری کشورهای منطقه از حملات ما به آنها غیرمنطقی است
🔹
آن‌ها اجازه دادند دشمن از خاکشان به ما حمله کند و مردم بی‌گناه ما را شهید کند آنوقت توقع دارند ما واکنشی نداشته باشیم؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/689958" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش سخنگوی فراکسیون ورزش به کُری خوانی بیرانوند علیه علی دایی: فوتبالیست‌های ما باید یاد بگیرند به پیشکسوتان احترام بگذارند/ طرف استوری هوایی را در شبکه اجتماعی می‌گذارد و تهمت‌هایی می‌زند که اصلا واقعیت ندارد
روح الله لک علی آبادی عضو کمیسیون بهداشت و سخنگوی فراکسیون ورزش مجلس در
#گفتگو
با خبرفوری:
🔹
بحثی بین بیرانوند و علی دایی پیش آمد که به نظرم این صحبت‌ها پسندیده نیست.
🔹
طرف استوری هوایی را در شبکه اجتماعی می‌گذارد و تهمت‌های می‌زند که اصلا واقعیت ندارد.
🔹
فوتبالیست‌های ما باید یاد بگیرند به پیشکسوتان احترام بگذارند و فضا را دوقطبی نکنند.
🔹
با همه شیطنت‌های که رییس جمهور آمریکا و همه بی‌عرضگی‌هایی که فیفا انجام داد، تیم ملی خوب بازی کرد.
🔹
نهایت بی‌عرضگی فیفا این بود که کارت قرمزی که بازیکن آمریکا گرفته بود با درخواست ترامپ برگشت خورد؛ این فاجعه بود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/689957" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689955">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔵
گل دوم استقلال به السد توسط سحرخیزان
🔹
استقلال ایران ۲ - ۰ السد قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/689955" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689954">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6a359d5e8.mp4?token=YuldiVs5uwakrtua_DJ4uSoq1Rf6njhn5KyH4onNlrQB8RhD4FZJqJUzKpUTe3dSJgCljyGmRxaU63qJrq_yZ3DmytRi6mLg1alfoGe5hWElPzpP6WnQKdGwVAuvW_pTpecsgPOIGlgYe_RcrlX40TDfcWNkq-YJXcGNw70-Rg2i5-Sq2wscAKDvJ2xsV0nI3xK277yuO2-qH9HEW9hxV8xGmZTkBpWwBi3Xe4g1-KbnQ2NT8Z9nlOQm5uFmFOTneViutQxJL3InUTWZP7WDByfKTERO4QrLcXBLTLnk-cq8xoAhhAdZx_F3-Gm_qMWPAraPYF2tmCOsltGc0VxWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6a359d5e8.mp4?token=YuldiVs5uwakrtua_DJ4uSoq1Rf6njhn5KyH4onNlrQB8RhD4FZJqJUzKpUTe3dSJgCljyGmRxaU63qJrq_yZ3DmytRi6mLg1alfoGe5hWElPzpP6WnQKdGwVAuvW_pTpecsgPOIGlgYe_RcrlX40TDfcWNkq-YJXcGNw70-Rg2i5-Sq2wscAKDvJ2xsV0nI3xK277yuO2-qH9HEW9hxV8xGmZTkBpWwBi3Xe4g1-KbnQ2NT8Z9nlOQm5uFmFOTneViutQxJL3InUTWZP7WDByfKTERO4QrLcXBLTLnk-cq8xoAhhAdZx_F3-Gm_qMWPAraPYF2tmCOsltGc0VxWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خوشحالی زمان حمله به ایران تا التماس برای باز کردن تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/689954" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689953">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رئیس‌جمهور: ما با کشورهای منطقه مشکل نداریم بلکه با پایگاه‌های آمریکا مشکل داریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/689953" target="_blank">📅 22:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689952">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a02b5c72.mp4?token=V93BnbWChYRQY-XUcrG7cPb_zbdCoQKs8y-t8pW7YhS6LNOd8q1LqnMchPmYjYMYZr_Zb2lrftf4A5gMSJY6hnNI8w0yZ_lxBmbvhzrLUS0t7jIhXw6HQOg-xOn-G3YavLdbeTO-iUNiobL8Eqru0KVpHSSURy22OgX4ceybAyqY_PTiTdwdvcvRuDtncBXpyxUhvxCcabAnFH3TZDKUPyVIsHcDT4Y3_xbNVquSbTm0aQ-cjJ3KeVeaZ_rkZo0X5CttwaoTAfe5VFEg-ibY2Xdt4Le9j1Apv0jZWGHZCAj1v4cR5l1iKY4DsLwYTXLuhnwmPQMUJCbK97TWFf0Pfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a02b5c72.mp4?token=V93BnbWChYRQY-XUcrG7cPb_zbdCoQKs8y-t8pW7YhS6LNOd8q1LqnMchPmYjYMYZr_Zb2lrftf4A5gMSJY6hnNI8w0yZ_lxBmbvhzrLUS0t7jIhXw6HQOg-xOn-G3YavLdbeTO-iUNiobL8Eqru0KVpHSSURy22OgX4ceybAyqY_PTiTdwdvcvRuDtncBXpyxUhvxCcabAnFH3TZDKUPyVIsHcDT4Y3_xbNVquSbTm0aQ-cjJ3KeVeaZ_rkZo0X5CttwaoTAfe5VFEg-ibY2Xdt4Le9j1Apv0jZWGHZCAj1v4cR5l1iKY4DsLwYTXLuhnwmPQMUJCbK97TWFf0Pfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: آمریکا چون نمی‌تواند رهبر ما را پیدا کند، درباره سلامتی او شایعه می‌سازد
🔹
رهبر انقلاب در سلامت کامل هستند و تصمیم آخر را ایشان می‌گیرند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/689952" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689951">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6e778833.mp4?token=oALSqu00IuSvin5kaEDm0hALjuU0x_ahzDMOOJP6x3ndJqMCQ8jnrD_rdwXty3t6IHOtvlPfnWPAPHtLIR68DLzs_vqSIv2sWDI1jCM2Mi_s5GRBKQDn_32JaSCnOl05W97SPDnCRidYVKkF0jVFf9sawOkhCMHzsqtO01h2exxUZ2f2eB7HXvlr0meuF0_wGdprKc0hXnZSKD6JC2sU3je9RAYn0m3ixfDGBYncOBmkdAahlcw9uZmDtixIfEyHp3jbhKJ4YGs1wYbdllh8y4ti_EsV6a0m2xW090lIE3we1RC3SwaIY81ZRlev8NcDb8FkEwrAK20cJ4MxTViLoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6e778833.mp4?token=oALSqu00IuSvin5kaEDm0hALjuU0x_ahzDMOOJP6x3ndJqMCQ8jnrD_rdwXty3t6IHOtvlPfnWPAPHtLIR68DLzs_vqSIv2sWDI1jCM2Mi_s5GRBKQDn_32JaSCnOl05W97SPDnCRidYVKkF0jVFf9sawOkhCMHzsqtO01h2exxUZ2f2eB7HXvlr0meuF0_wGdprKc0hXnZSKD6JC2sU3je9RAYn0m3ixfDGBYncOBmkdAahlcw9uZmDtixIfEyHp3jbhKJ4YGs1wYbdllh8y4ti_EsV6a0m2xW090lIE3we1RC3SwaIY81ZRlev8NcDb8FkEwrAK20cJ4MxTViLoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمریکا با ادعای حقوق بشر پس از شکست نظامی و زدن زیرساخت‌ها، راه ورود دارو و غذا به ایران را بسته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/689951" target="_blank">📅 22:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689950">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ما با عربستان در جنگ نیستیم و یمنی‌ها نیز مسائل خود را دارند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/689950" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689949">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/943ee9b829.mp4?token=V4_Fe8m0wht1DaRyTmEBRfQPPjZhvNoNmM3bhDR-OZug2gXr1s6zXoPSg7HyUN3KL3yhH0wOmc7380hFCPVtbyjfsHsfDr5TRwBk9hteoQNd6rgL1dLUplPp_nj1TyD0ZjnDSRrCg1efeh5sXeieoX6sxZEy_Xg5rW_YxD9oeTbMRSojcl7GIuU1tTh7npTB2ug3QqGmFkh68a3kImlbkQ6zSue7AiLnMVr0r9uZF4HHqmZR7modnhuysDBDdxPr4fuVdsEc6nstlXHytDWN5vzVbTRwurj0ad6zXFj0h8cG-h-LCmWgSYgJEK5JKZ_FakwI9zisIPLDmTnYgDSuoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/943ee9b829.mp4?token=V4_Fe8m0wht1DaRyTmEBRfQPPjZhvNoNmM3bhDR-OZug2gXr1s6zXoPSg7HyUN3KL3yhH0wOmc7380hFCPVtbyjfsHsfDr5TRwBk9hteoQNd6rgL1dLUplPp_nj1TyD0ZjnDSRrCg1efeh5sXeieoX6sxZEy_Xg5rW_YxD9oeTbMRSojcl7GIuU1tTh7npTB2ug3QqGmFkh68a3kImlbkQ6zSue7AiLnMVr0r9uZF4HHqmZR7modnhuysDBDdxPr4fuVdsEc6nstlXHytDWN5vzVbTRwurj0ad6zXFj0h8cG-h-LCmWgSYgJEK5JKZ_FakwI9zisIPLDmTnYgDSuoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: مردم ما بعد از حملۀ آمریکا به ایران متحدتر شدند
🔹
مردم منطقه از آمریکا متنفرتر شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/689949" target="_blank">📅 22:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689948">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOU9z4qg076Fdujp6nzy1QyX_zTjZ5mrYzOlQXLwIoVDZiGButgCMsnsOL1KaKDH5IdQ6AM4o52o6QocJ1yx4SKVp5V7R2lAlSgTukyyEaJ0ig4OctTun5-e5p_zPw8dmlbuEXc7-JDmBoyyvhWnb9YQqxGEC2GDnkcX26sWSNN-qGou-Qmphmtxqe4DapD9qnkg9C3LomHyK9pXZsaPuYfo-ym1CStona1qlbECGjm1aaVx1wYfV9oZtMyjo10P1RC0Ob1t0oWIPTkkkDGjUtKEBVXnan6fC_Aekf9a2xdWSqiOOBrV7_uXzQOzSawIrPO3RIfDORuKrRb41TBRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران؛ در مسیر آموزش داوطلبان جان‌فدا
🔹
بیلبوردهای جدید شهری با تمرکز بر آموزش‌های نظامی و امدادی داوطلبان «جان‌فدا» در نقاط مختلف تهران اکران شد.
🔹
در یکی از این پیام‌ها آمده است:
«بلدی با دراگانوف‌ شلیک کنی؟»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/689948" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689947">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0bcac33e6.mp4?token=OTTCOzf8U7Pz32rBCGds4zrXCR_dBfXaVcuh0OhtH2LEGyxQ84-Tbp9t0g4cRpYkGR_WkT3vtg2bjz764eKFCjOrUOc2ObBn6ufVFq0BI3RNv72pflycVOFDr0fxNa6eUwirTOE1Pl3oLp2L6YQJxv-x5aSuQXC8Em-yPyY2437fibEq6VdMSEOKzJIhsYyv9lR9AQdhxJSDIgr1MvmBrajUuQjtH2eYfi91rQvWv25W2Ne--eYY2pHcqeG4q2UHb6ubXN6ULxUj6ZY1nxLhKPW7kdDEI8HIMathxyPewgTa-pwYZQxze6YWzx597fIwSbNYXPZ6tDd_pusungQpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0bcac33e6.mp4?token=OTTCOzf8U7Pz32rBCGds4zrXCR_dBfXaVcuh0OhtH2LEGyxQ84-Tbp9t0g4cRpYkGR_WkT3vtg2bjz764eKFCjOrUOc2ObBn6ufVFq0BI3RNv72pflycVOFDr0fxNa6eUwirTOE1Pl3oLp2L6YQJxv-x5aSuQXC8Em-yPyY2437fibEq6VdMSEOKzJIhsYyv9lR9AQdhxJSDIgr1MvmBrajUuQjtH2eYfi91rQvWv25W2Ne--eYY2pHcqeG4q2UHb6ubXN6ULxUj6ZY1nxLhKPW7kdDEI8HIMathxyPewgTa-pwYZQxze6YWzx597fIwSbNYXPZ6tDd_pusungQpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: فعلا نمی‌توانیم تصمیمی درباره مذاکرات مستقیم با آمریکا بگیریم، آن‌ها رهبر ما را شهید کردند، به این راحتی نیست، فقط نوشته‌ای را امضا کرده‌ایم و باید جو اعتماد درست شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/689947" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689946">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
فرود اضطراری بوئینگ ۷۳۷ سپهران در مشهد
🔹
یک فروند بوئینگ ۷۳۷ شرکت سپهران در پرواز مشهد ـ کرمانشاه، پس از برخاستن با مشکل در یکی از لاستیک‌ها و احتمال آسیب به موتور مواجه شد.
🔹
خلبان با اعلام وضعیت اضطراری، هواپیما را به فرودگاه مشهد بازگرداند و هواپیما به سلامت فرود آمد.
🔹
در پی این حادثه ، باند ۳۱ چپ فرودگاه مشهد موقتاً بسته شده و احتمال تأخیر یا تغییر در برنامه برخی پروازهای ورودی و خروجی وجود دارد.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/689946" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689945">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699ab9b780.mp4?token=Xyblxd6OqdggngU-B15fDXG5DO0MdPr4nHMO5cZI8Ny7Zuirl6Gi8gO9dtiHSxnWHijBcTuAX2tg8yn3Sf9IQgJWjdDHTnxZmeNzcVZDw4pp4WzokY9RIq03wCFJKvSRaDjbB_rKv8L0PF17NlkG3PSuKKOPbNCaW4KYHcMinDqy4kdds8laHjVia4Oldjh9AiZJ8xRPJEzK8bYn9EXqHuzh5UCLwtT97FXzx7VmVZDqpXVbZ2jPIz0zFZv6MqgkFufCNxiqVVkjzy4FLQRP5RnpMAx8PTUILfp9lE2fVUiTcvxRLNBgzVpoq0z2k3Ugs8NJzlsvlnhm3nwvYssTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699ab9b780.mp4?token=Xyblxd6OqdggngU-B15fDXG5DO0MdPr4nHMO5cZI8Ny7Zuirl6Gi8gO9dtiHSxnWHijBcTuAX2tg8yn3Sf9IQgJWjdDHTnxZmeNzcVZDw4pp4WzokY9RIq03wCFJKvSRaDjbB_rKv8L0PF17NlkG3PSuKKOPbNCaW4KYHcMinDqy4kdds8laHjVia4Oldjh9AiZJ8xRPJEzK8bYn9EXqHuzh5UCLwtT97FXzx7VmVZDqpXVbZ2jPIz0zFZv6MqgkFufCNxiqVVkjzy4FLQRP5RnpMAx8PTUILfp9lE2fVUiTcvxRLNBgzVpoq0z2k3Ugs8NJzlsvlnhm3nwvYssTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: خواسته‌های ما همان خواسته‌های قبلی است
🔹
رئیس‌جمهور در گفت‌وگو با شبکه خبری ایندیا تودی هند: تفاهم‌نامه ایران و آمریکا چه مشکلی دارد که بخواهیم دوباره مذاکره کنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/689945" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689944">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22081bb80.mp4?token=GJp1vD9YymREZyexzTeK30kh7RxMCfb6Vzbe0MFIMtmB4yXYAxzQIwalpUISLH6FH0kn9aO5Uz_USE5BCo7rShfpDuCWXBkyG6qpnyolN_RaP-NksqLS7scFJ0juN-jV_tyCYb3wVkmCLTDuuW5MvXElCoVxDbBymcdfP4JMP3DSBtnlW4_klkr1kdWlyk_Taz2ALds0HGMuybnRQ02eq_hq6KO1cssjHBcbij0mnpECP3YG03_4JYL7BxAnFBrEnFL-elYKYBmCiVgKV-HZ9mTpcbnPrNr3851G84TXO1NLoyCIOsgtN6A69hEu_ONGAdICTTtkynbLFp0EaUHwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22081bb80.mp4?token=GJp1vD9YymREZyexzTeK30kh7RxMCfb6Vzbe0MFIMtmB4yXYAxzQIwalpUISLH6FH0kn9aO5Uz_USE5BCo7rShfpDuCWXBkyG6qpnyolN_RaP-NksqLS7scFJ0juN-jV_tyCYb3wVkmCLTDuuW5MvXElCoVxDbBymcdfP4JMP3DSBtnlW4_klkr1kdWlyk_Taz2ALds0HGMuybnRQ02eq_hq6KO1cssjHBcbij0mnpECP3YG03_4JYL7BxAnFBrEnFL-elYKYBmCiVgKV-HZ9mTpcbnPrNr3851G84TXO1NLoyCIOsgtN6A69hEu_ONGAdICTTtkynbLFp0EaUHwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ما با کشورهای منطقه مشکل نداریم بلکه با پایگاه‌های آمریکا مشکل داریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/689944" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd6b78ebec.mp4?token=UOUMtUQnxRp4Z8I-cuj_gwQBsWFMEuswuxNA-wUj4eL9ecBS09c4y26M7EhZJ8VSi-Ru1px_jOMFKY2dK_9hCfgFVwMdYc9Vb7mgskss44tEpg2SQhrzDWnbEuytxEcPU2Syo0OUWZQwpNYHXx5fEtNJP-o2DXDV1fMD9IvDoGxLk6DngitIyROTny66fU1S1u6yGKRUJXEpgpNBztcAXbgIBBQVbyAvSt19vVHQPwyiDU_J1m6Hjy5vtAlx-9_TQYCxyfpVLX3a6k32jJb4oWRbWGUsBhoVwV59mrxAU0zMVUcv2YzRwM9piS5cR4LOcbT2966XX5dejarZVcF2Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd6b78ebec.mp4?token=UOUMtUQnxRp4Z8I-cuj_gwQBsWFMEuswuxNA-wUj4eL9ecBS09c4y26M7EhZJ8VSi-Ru1px_jOMFKY2dK_9hCfgFVwMdYc9Vb7mgskss44tEpg2SQhrzDWnbEuytxEcPU2Syo0OUWZQwpNYHXx5fEtNJP-o2DXDV1fMD9IvDoGxLk6DngitIyROTny66fU1S1u6yGKRUJXEpgpNBztcAXbgIBBQVbyAvSt19vVHQPwyiDU_J1m6Hjy5vtAlx-9_TQYCxyfpVLX3a6k32jJb4oWRbWGUsBhoVwV59mrxAU0zMVUcv2YzRwM9piS5cR4LOcbT2966XX5dejarZVcF2Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: رهبر شهید ما که حرف ایشان برای جامعه حجت است، بارها اعلام کردند که ما به هیچ‌وجه بدنبال سلاح هسته‌ای نیستیم، ما با چه زبانی باید بگوییم که دنبال سلاح هسته‌ای نیستیم، کدام مستندی را پیدا کردند که ما بدنبال سلاح هسته‌ای هستیم که به خود اجازه حمله…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689943" target="_blank">📅 22:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689942">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری سخنگوی فراکسیون ورزش از پشت پرده فساد در فوتبال ایران: برخی باشگاه‌ها با زدوبند بازیکن ایرانی را از کشور دیگری خریداری می‌کند و بعد به تیم دیگری در لیگ با قیمت بیشتر می‌فروشند/ برخی ایجنت‌ها برای انتقال یک بازیکن، ۳۰ میلیارد تومان دریافت می‌کنند
روح الله لک علی آبادی عضو کمیسیون بهداشت و سخنگوی فراکسیون ورزش مجلس در گفتگو با
#خبرفوری
:
🔹
مدیر عاملی را برای باشگاهی آوردیم که بعد از ۶ ماه تا یکسال که میماند به باشگاه به خاطر قراردادهای اشتباه، قراردادهایی با زدوبند و یا عدول از سقف قرارداد، هزینه های نجومی را به باشگاه تحمیل می‌کند؛ همه میدانند که از این سقف قراردادها عدول می‌شود.
🔹
به طور صوری با یک بازیکن فوتبال خارجی قرارداد میلیون دلاری می‌بندند که آن بازیکن اصلا وارد زمین نمیشود یا اگر وارد زمین شود عملکردش از ضعیف ترین بازیکن لیگ پایین تر است.
🔹
بازیکن ایرانی از کشور دیگر می آوریم و قرارداد می‌بندیم و به تیم دیگر با سود بیشتر می فروشیم؛ معلوم است که زد و بند وجود دارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689942" target="_blank">📅 22:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پزشکیان: ارتباط ما با نخست‌وزیر هند روزبه‌روز بهتر می‌شود
🔹
در تلاشیم بر پایه فرهنگ و رابطه دیرینۀ ۲ کشور، مقابل تمامیت‌خواهی بایستیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/689941" target="_blank">📅 22:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689940">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان: حتی افرادی که در ایران ناراضی بودند و مشکلات داشتند و حتی اختلافاتی وجود داشت، از تمامیت ایران دفاع کردند و به تجاوز آمریکا اعتراض کردند و حتی تعداد قابل توجهی از ایرانیانی که خارج از کشور بودند، به ایران بازگشتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/689940" target="_blank">📅 22:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689939">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پزشکیان: حتی افرادی که در ایران ناراضی بودند و مشکلات داشتند و حتی اختلافاتی وجود داشت، از تمامیت ایران دفاع کردند و به تجاوز آمریکا اعتراض کردند و حتی تعداد قابل توجهی از ایرانیانی که خارج از کشور بودند، به ایران بازگشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/689939" target="_blank">📅 22:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95be5c545f.mp4?token=HzVesm6LPU1_WCUYOdFPTllp08QmAPGI3agBwEino-jgw26vPQzueqLlTgskjBlP4LzdcIKDKCroQrQajQBRSwX8_beYUNw9ehCuM5E2fuzMTot5KPXimbQYFt4sFqHGi0C7WPUFNcGOwbuEO-OrjkLxY7844Jzug0zPZ8lIyblMKCcm8kX2cOc9u4x3Q3ikeTKQfahvyTC7hik--G6QVAY0fIEhpBz8kAS6n8-rM1-BkmfNEfHGmHm52-cq4Z6LsOrCVhlojJMPNXqWPDwLx7iM2A3-8FMMoaSn3e_vK6CBnGjp4TogVIphm2xvva_98vDUV-e9vqfkSII2V90hrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95be5c545f.mp4?token=HzVesm6LPU1_WCUYOdFPTllp08QmAPGI3agBwEino-jgw26vPQzueqLlTgskjBlP4LzdcIKDKCroQrQajQBRSwX8_beYUNw9ehCuM5E2fuzMTot5KPXimbQYFt4sFqHGi0C7WPUFNcGOwbuEO-OrjkLxY7844Jzug0zPZ8lIyblMKCcm8kX2cOc9u4x3Q3ikeTKQfahvyTC7hik--G6QVAY0fIEhpBz8kAS6n8-rM1-BkmfNEfHGmHm52-cq4Z6LsOrCVhlojJMPNXqWPDwLx7iM2A3-8FMMoaSn3e_vK6CBnGjp4TogVIphm2xvva_98vDUV-e9vqfkSII2V90hrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمادگی کامل داریم که راه ابریشم و سایر کریدورهایی را که از ایران می‌گذرد احیا کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/689938" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK8s02IhGJboBUJ1TKBxJs_IOmjzRIh2EiWtVlPPV0cFnI8IXipofr7_9GmuEvJHO9YJF3LXx7hS39J5I_f4wKekhR6B97CduGvo5e_0GDutI-5NnWnW_Atyr3-kggpuDQYLaNBLzrNB0d8i9pScrU1TTVATLwbDkub9Onwvngz60eYA79GLZyJHGYEi-yhvWpkILZw_JKjUh9mJ7gjaPhwAYP_Lyw0ifrvvB9mIDCG2ZQgyJWuFRO-J4hX7By25Jgcv60DdvPgd9QRBq1u0AGgSChxdUt_ttXEUprbwAop0725Vt6zZAngXBCJZBnc7tffoMfuWcuJmv6P3cFkb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخورد سوپر نفتکش «الگایا» با مین‌های دریایی
فرماندهی نیروی دریایی سپاه:
🔹
سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقهء ممنوعه در جنوب تنگه هرمز را داشت،بر اثر برخورد با مین های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و کل نفتکش در شعله های آتش گرفتار شده است پیش از این نسبت به خطرناک بودن معبر غیر قانونی هشدار داده شده بود، نیروی دریایی سپاه با قاطعیت اعلام می کند تنگه هرمز مسدود و همچنان تحت کنترل هوشمند ما می باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/689937" target="_blank">📅 22:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0cdaddec.mp4?token=knhv5OP20v1rCDo9tvPKJaNeHCpN33jik4GvS2IuIfi4puPxNfpwbvQoPBoI4tbwFKYwmSi0orjAYeSD-4oR9Bn427ncYhz2u3TajPOeVtchBSrQXN9x6GqAcCWI8hSrq8_rF77xEazu7HEid_iyhHXYofvfVhkamWNmSb0YNfPi3i8K9omX08ueCMvz2Zt0jdVB_e071nyyajgeIrHbYqO2gBoODW7DJF1K-raglfl-Dq5W32mAM6YYJhjJ523v2ecxbShcPdWiPnfe-zRBPxq0zQqHNUJ-8GS_mvu2-PelP1uPZElXjUY9fcRN7pv3ugqYgO4mwSfBh_MzgzrmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0cdaddec.mp4?token=knhv5OP20v1rCDo9tvPKJaNeHCpN33jik4GvS2IuIfi4puPxNfpwbvQoPBoI4tbwFKYwmSi0orjAYeSD-4oR9Bn427ncYhz2u3TajPOeVtchBSrQXN9x6GqAcCWI8hSrq8_rF77xEazu7HEid_iyhHXYofvfVhkamWNmSb0YNfPi3i8K9omX08ueCMvz2Zt0jdVB_e071nyyajgeIrHbYqO2gBoODW7DJF1K-raglfl-Dq5W32mAM6YYJhjJ523v2ecxbShcPdWiPnfe-zRBPxq0zQqHNUJ-8GS_mvu2-PelP1uPZElXjUY9fcRN7pv3ugqYgO4mwSfBh_MzgzrmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موضع متفاوت یک ایرانی خارج از کشور نسبت به بیش از ۳۰ میلیون جانفدا: خودم هم ثبت‌نام کردم
🔹
دوره جدید پویش جانفدا با فراخوان آموزش نظامی و امدادی چند روزی است شروع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/689936" target="_blank">📅 22:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689934">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
منابع عربی از فعال‌شدن آژیرهای هشدار در پی حملۀ موشکی انصارالله یمن به منطقۀ نجران در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/689934" target="_blank">📅 22:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkg7dZ4lbAHT83QdxGkBLShkDIczs5V_bwJAbtHfBG7Mq0Vcfux9Rh7g6_t78_BwnZUNdD2afGw_zpvn4ccjnHGObBOsHNdoqNW6HwRMNLdk5tc84cN2Y75TN_o-SvTfplyvePhje3GjtINOn5EczB7JD43a9pYSbFZMKuORzwDIKX6UZcWhUAA0WAl94zR84-qab9TvY6iYIGC8HNjnh-lS2u_5vROAQj43OEgbUg--UkIKTFo_5rccRwoKe18IU2f5C9yVNOlr_gx9hk31mdzJ_pTUsrXJmIBgIt349i9uD2GbNk8fWy9whZ3YbmhRBKJ-UBrynWeuY8r2_KC2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6z5Oh4n7sHo0TuBfLF_GLRktTdRaPMSlbUnultIsG7t4WjdOVBnzzO5tJ5lmInKeCzPtfomWZafcO5ZrUuDpfucRM-CuLFtRsbzIOJ0lrKzPgOtgyQHIOUH41iBSuhZdDBNu1-bVYH8QSkzQjXgKRz4s0uMaMUiLG2DIH9bBIR2aR-WIrxXojre6USRmPWFQjPimNBplA2wd_eeKDS6U9eekuxlrUfeK5HdDeXaE0gEZPR6Pt6u6S2AIziFXipvYGuS4AOx_MCVqjpiC7MdEZtcPbKqww-Dnw2OG39aCv_nDzxqT4wYOZttdsIY1wasH6Fu0nboGspWBHHWG0w-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0581DreM_kX3h_d5NSrV3oNY3IvMOzRjhwZXFQ2lwTL_3YUCkdQc3eprtXFNTUXJItv3PvtxxjJVQVDR9oPR2_NhA8eavP0Lj3Xu1u7vKv_VfnaLu7T0qVvBm5Wt8WHN64Hw39eXBPRGMEt0j1DKIjtKQZy5ap6NgBxbgdWHFywD732-bwEeVPUi4-6uVNrUnBk6REtT7vS8nlblU-ZHU1BczXtnwppkhcrNftSjW1hcI0YSkucXzB3Rrkdu34SkDq7Be9fZQR0uVPb7xnQKynb8LaBskdGtUjLZQecwuw-0YhOqUHj5qHm6-jzI2WsnFMr7LCy030f7t_QFTz7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gm8f9EfR5VTBDLFodNP0NdLvSaUrcXpXJPyBXjcJqkjWTJwqi9qDygksODwY4OQGn8UnqDpuxevMZN_g4PWlEh_mmKuzvPDa5GgFt5JllGUBNSNQ99zM0Kt2dR1PHs4BhwfVnh2DTF-GbwNlhRYVxnIYLojPftU4cRcC51gFqTxJWNgmT-CHQlmP8CTsOo-vLzlNUKqQVRHjoRyDiq7GiWuEkKU_HUBIqjBxzZsaJoOIt8z_fC733jiOfpUevEfgWX-RXTdeEHqGBE6B3eaGn4deAte8afgpPZZcJ41Uoke0XiC4eeSSL5UqhV6_M3SqF4eF8E8fIjkX5aL0uoJmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0a9kIgy17MNd8BuTL3W7Zt_bv2UcVYezIlEtkijM8zvP3t43tf3lWY7Mrdio1-vl7bdrUgneEvG2FsLqojuJ9mhOA0jZPMRNJsuZNMGoE4nhn_5dL31O8tCG02inLWpcC-EktcA9UYdEeWbxqScN4vHumR3zYNpnhher58jboqXn-K8ui67ys7Y7O5hMrSGeGAH9jgzpBj5xhxrZhC2bRQBVE9XPWnKv2b3di6fqiJi54IoW_lgcSI25lPJdoy44rgDvE2JzgOjdo52ivKjaVMTzvPwheMxkQPmrevxl0qB_c3jDc4WBl4WiKH9ZcFpzgn5wuNijmOXbRD3IcXzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLFKQaWoeenlb5VieNy7HjBR6utYENu2N9cP244OpDcXl2lt63GAAVE3LC1ddF0hBtHPy3Uobw_Ema14u9VOaRBp8J-k6Ftwgb5vjaKrm7XpioESeKr-GgnRoFE2vBwuN3aBus33nteiGrDv8GXE6OKIXvkm5hfK351sMDwyNyUVYvKFajJbAgJ-IB_lbrME5E_0Gu37zNEimhjYct216mp01jYSRyHxHpKX3CmdoBscJhZjW64yWbeDwo7fDoaKbKqVTrS5Co5ztiNjvRVkuTlvSUapUXWkZzK-KJBC1-M9Y8Axw3QSuEBKPfOQYHGw3o7Qzh9HzUHZz_Xb0HiQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CeSnKvgTStCD9l-meer4F17LcMq7WU3crVWGVND7OAlobkPCYbmup7wH1BgoLXrkPbe6B7HwVyTOWfHqxgE3oR02R35kSHarhOBJ0IyTDIBNjaB2DTLk01sAUSMEb58xmD1zSJ66m4qravAxhrlFwdiM1BSoV_iWrG4EaiGz-2a0ZL4nQyfpBc19G9cU3VuBkTAZvgBJiE14AFDa70eN9-KmT11L_fKb_QMdjVbXHOaHJydgDOepm-vJn8ez3m8nXzifNB7ps-yDlw-qxyxI-beZrw26KVl01nZcwNexIrrzFy9uJdTnn8ms-sbfxKee65pwhyet5pDQDKOEGLhCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPTlvyZJ-iux0GRWjtepSEuq3aE4JbOFxZu3SXisd6xpphn1gI7Ki0CdkkmLZTbsG9o5WGEmC4FMyVYCl0wne_hE011HL3mvWGEmxH0wusGnf3RYaSQkKy0QvqmYY2eqfKMOu1Pvkm5r4r8ZOMR9vx7Z2DXGvBzPdQ_7gZA_Pamsi3oL0H2B3HzoikqTcOiX263usv3_Ys0pv3CNmOJkG69MBEyxw6TB3ISoI1bZkxoGP1i8DlAgnOqsg0czua_GHLHnzkNiLKUZCHSjFfgoGmj9bJ-j0DAVlLDenmye93VfteTa7YkVhh7CcWhfXAx9hpy1eHgjaGmIjO-uJtuAUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
✨
هیچ قدم خیری کوچک نیست؛ وقتی مقصدش، گره‌گشایی از زندگی دیگری باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم‌برخوردار، قدمی برای همراهی بیشتر برمی‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/689926" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712d597453.mp4?token=JoeSgL7mrlg-TrK06n-4n7oB-5KP1azOxMed-OtcWC6URXM-tEQVMOtze5B50lMtJXA3zw8krtM26o60nD5LYKkCZuw58vOrwlpzvnWc-9niO0ZJr8vniVsLcGYaW6IwD3uWnvYyBH9qdX6mHv1tfnEgl1UU4hT562seIVvf3xNGA02Mr1aEP1OLvvIvtTnX0pycEE_39uv-lkIGt8zy7b-Sp_rh2-HRs0IOEDTtHTGCqLtYf8ql_3mdSlmpsgfkvaQ50bcNZhShRSyJOAYv2-09ir0wpT_kwLxJ_dw-OM3OOYulMWURnlySrsPS7F_yNt3WN8JukS6ZWg4StuKIwQRCiRuhLfZghOh6BzN061K6PqpkZaqHsQgqady7ixhSXTz2INnUc8XLmR503WLgRKmPN7cwcxPRXzzAAqZgh1HGgD5NUHRxWNkLUH7-oun4NV91PYuac0h5GmhuLbSWo66ftV-RWCHU1ZIcb9dVWWllaq6BQKVTUjmZxxiEjamx_ixxT85PdGVlKBFNp51UWfdc_WL-KGDuKQK1KhBlrxYf5liZyA99uo54aVYKWaIvqTYlORhc7t4iS2ZvNHYvXWkSabAgbQ7VRwUT0zAbIvb60NeP6464WWaB3pfhu-hjr6AhQmzxT9umtTUAiLtSbQbM0wwmHBhJrdvv1ilCSlo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712d597453.mp4?token=JoeSgL7mrlg-TrK06n-4n7oB-5KP1azOxMed-OtcWC6URXM-tEQVMOtze5B50lMtJXA3zw8krtM26o60nD5LYKkCZuw58vOrwlpzvnWc-9niO0ZJr8vniVsLcGYaW6IwD3uWnvYyBH9qdX6mHv1tfnEgl1UU4hT562seIVvf3xNGA02Mr1aEP1OLvvIvtTnX0pycEE_39uv-lkIGt8zy7b-Sp_rh2-HRs0IOEDTtHTGCqLtYf8ql_3mdSlmpsgfkvaQ50bcNZhShRSyJOAYv2-09ir0wpT_kwLxJ_dw-OM3OOYulMWURnlySrsPS7F_yNt3WN8JukS6ZWg4StuKIwQRCiRuhLfZghOh6BzN061K6PqpkZaqHsQgqady7ixhSXTz2INnUc8XLmR503WLgRKmPN7cwcxPRXzzAAqZgh1HGgD5NUHRxWNkLUH7-oun4NV91PYuac0h5GmhuLbSWo66ftV-RWCHU1ZIcb9dVWWllaq6BQKVTUjmZxxiEjamx_ixxT85PdGVlKBFNp51UWfdc_WL-KGDuKQK1KhBlrxYf5liZyA99uo54aVYKWaIvqTYlORhc7t4iS2ZvNHYvXWkSabAgbQ7VRwUT0zAbIvb60NeP6464WWaB3pfhu-hjr6AhQmzxT9umtTUAiLtSbQbM0wwmHBhJrdvv1ilCSlo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/689925" target="_blank">📅 22:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وزارت خزانه داری دولت تروریستی آمریکا در تازه‌ترین اقدام علیه ایران و روسیه، از تحریم یک بانک VTB روسیه با اتهام کمک به ایران در دور زدن تحریم‌ها خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/689924" target="_blank">📅 22:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689923">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpznfTHxfMQ37qKADJpmU_JTD4wsbNBkVezGOzvpxIU47gWKBoxLk7GmpTjPuhRUMPXBLAjLppgEVMtLk3r7bgMFRm_cK0B41JjHlj3lbsdnek2GxoqLW2Fo6eXXpoRUdLVwND09NDXEUUKj-jYZR9gcw7XfjjF_NusHwquq2PSDPIqWB-IHmGDPILsiIX5GyaD1TsqGyrVllwyYG8MjBkVoA2x8yiJj88psbsGbcpMI6Zn9CpMbjh0IvdzhEzo769veCJmlV1o4GtARJmLuqpNkcNRyEuMlSAgFl_vneFCcAx-L2hnfJlxIbviAg88LcPsBPnNb5uCZ8QC1e6E5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر یمنی: حج ممکن است به‌زودی رایگان شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/689923" target="_blank">📅 22:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689922">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWhMt3mttmvKhs7pvcOZD9b5drYZ5jdP7qEL2LAlJK1lfmNqcFu7mzUZW9YHO57xu7wUmt8qkhBh0YNwQlIgp64_IXtmWSqUr2t91_8NtUeypreD-LHzuUjkLBo6KyXvTAdFXS790VrkQkw1ZoQ11LLAbDfJe9Gk2v7w0t_WsaM3hQgCZMeP5lCXLsgUN4m8LQslp84HyCI-GLD7jQlK9pEkju0UyXg45-y_6uH18mSXh90tzDPNvquJyBl5lDRkHBLzCWcPG_hdWnAxujh3FNuAhKyWtOGEIEm2f3baHta_FPTnqB-u9pq-ECtOOqoBOSS1ekMRxr3DIi3HWHH0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: دوشنبه ۲۳ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
💳
امکان دریافت اقساطی
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/689922" target="_blank">📅 22:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689921">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنیکان شهد سبلان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903c98b6aa.mp4?token=Tds4UF6K84nIiYC3OH-08TGTVC2aAKe_UCEo7uSl8Vhs3qALrrBFfQWHBAzwxAd28UuaaXYL4diJqe5bhLNNQSkfKjs3_mtpoX3UTReC5-rMUz4OAxJE0llpMGYwKzkaAkJ-xRDalq_ArQjoQpx4Vd-o7GQq9COkJUp0IvNxMyd2SZBAIIAxW0MmXy2oXGj6tQApGp8HaIuYtuuut-B33fhWKtSQr5Qkoa2PjbAiVyKiKm8pj6ogEdX1VMywuDw_xvj0F7EypEKMkxjGEn2xikdLdf4FMxYZuRf1oAGfJJoAdbn3LodYrgvsWvoYc-rzf1ArMtvpSShhd3A8gPIK_UijnWxKqMlg1AMUltRICubnmh-cVx0jP-ZkOIqvHkFUi575xPjd07WdPGa2FtfUumvfqjygbJHncjc0vSS0fodX-zyC5dCrnhYCuNeAcxLUAU-y8r_cKCiNNBlPeAJzGjqQUf3wJKkIiz1cmBnMVco_AQRgaD3V_8UpX9Ogysttw96eY3e6TAyOHcgtQKgt_1r1nPXMN7l0MYX04eC4R1u7PaZNtC0KFK_Tf20tVvGsjZH6Cx1VgTyAWOOt2fOHlgq2_XUvFp7L3P2ZqblsTDCcgIYA4ZWTaFkIoiMJEys0xKauLWrbzmHMJV3d7df5_c5xtu19X1gOpSM2_6y6NYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903c98b6aa.mp4?token=Tds4UF6K84nIiYC3OH-08TGTVC2aAKe_UCEo7uSl8Vhs3qALrrBFfQWHBAzwxAd28UuaaXYL4diJqe5bhLNNQSkfKjs3_mtpoX3UTReC5-rMUz4OAxJE0llpMGYwKzkaAkJ-xRDalq_ArQjoQpx4Vd-o7GQq9COkJUp0IvNxMyd2SZBAIIAxW0MmXy2oXGj6tQApGp8HaIuYtuuut-B33fhWKtSQr5Qkoa2PjbAiVyKiKm8pj6ogEdX1VMywuDw_xvj0F7EypEKMkxjGEn2xikdLdf4FMxYZuRf1oAGfJJoAdbn3LodYrgvsWvoYc-rzf1ArMtvpSShhd3A8gPIK_UijnWxKqMlg1AMUltRICubnmh-cVx0jP-ZkOIqvHkFUi575xPjd07WdPGa2FtfUumvfqjygbJHncjc0vSS0fodX-zyC5dCrnhYCuNeAcxLUAU-y8r_cKCiNNBlPeAJzGjqQUf3wJKkIiz1cmBnMVco_AQRgaD3V_8UpX9Ogysttw96eY3e6TAyOHcgtQKgt_1r1nPXMN7l0MYX04eC4R1u7PaZNtC0KFK_Tf20tVvGsjZH6Cx1VgTyAWOOt2fOHlgq2_XUvFp7L3P2ZqblsTDCcgIYA4ZWTaFkIoiMJEys0xKauLWrbzmHMJV3d7df5_c5xtu19X1gOpSM2_6y6NYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
من یک  زنبوردار ایرانی‌ام که کنار همسرم  در دامنه‌های سبلان، عسل ناب و ارگانیک تهیه می‌کنیم
🐝
⛰
چرا عسل ما اینقدر خاصه؟
⭕️
ارگانیک، سالم، بدون سم و آلودگی
⭕️
قابل مصرف برای دیابتی‌ها
فقط یک قاشقش کافیه تا عاشقش بشی!
✨
عسلی بهت میدم تا آخـــــــــــــــــر عُمرت دعاگوم باشی و پدر مادرم و دعـــــــــــا کنی
🔗
عضویت در کانال:
https://t.me/+ejr3jVZOO2Y2MTM0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/689921" target="_blank">📅 22:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689920">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون بهداشت مجلس: برخی از بیماران به خاطر گرانی دارو در ایران، بلیط هواپیما تهیه می‌کنند و به کشورهای خارجی می‌روند و دارو را با قیمت کمتری تهیه می‌کنند!
روح الله لک علی آبادی، عضو کمیسیون بهداشت و سخنگوی فراکسیون ورزش مجلس در گفتگو با
#خبرفوری
:
🔹
تلاش وزارت بهداشت و کمیسیون بهداشت بر این است که پزشک خانواده احیا شود.
اجرای طرح پزشک خانواده هزینه های درمان را کاهش می‌دهد.
🔹
متاسفانه احساس میکنم در نظام سلامت ما برخی از ظرفیت‌هایی که داریم ، هدر می رود.
🔹
اینکه فردی خودش کشور دیگری برود و دارو بیاورد از ثبت سفارش ارزانتر تمام می شود نیازمند نظارت جدی است ؛ ثبت سفارشی که وقتی از یک داروی خاص مقدار زیادی باشد باید مطمئن تر ارزانتر باشد، اما اینگونه نیست و باید بررسی شود.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/689920" target="_blank">📅 21:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689919">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع عراقی از وقوع دو انفجار در منطقه شمامک استان اربیل و مشاهده آتش‌سوزی در محل انفجار خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/689919" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d904887f17.mp4?token=Ui0LBha8MuYGoYQkChSVMQE7ca8kR6quoyoSS2ZFa_eAdVWXh92pdElGi5tobGa1y4zBvI0_Ag3oS9tI8MJNRPbyGWytt-_i4-8Y-clwlALqwMyM9TzsQXqXtXJd0v1iEKkwXHrin_i5Xp-wqyecY2xmNAHXJW1dE69PCBTlfr-GojRxPq4Co1FazJQ1AdM4U_uTSR4Y4uEULAT9iC3_vaRuHxfKnvS3HoUhphlRXr1-pjaau5zeQ-fi1naPj-0vFMTvKR7rpf_Hr0oY-rb9smfuUh7YqnKogT4uiTAZHyr8ang3Q68Wr3ajFlUFNrzVBiVKMaNsrG6tTXo_OMLR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d904887f17.mp4?token=Ui0LBha8MuYGoYQkChSVMQE7ca8kR6quoyoSS2ZFa_eAdVWXh92pdElGi5tobGa1y4zBvI0_Ag3oS9tI8MJNRPbyGWytt-_i4-8Y-clwlALqwMyM9TzsQXqXtXJd0v1iEKkwXHrin_i5Xp-wqyecY2xmNAHXJW1dE69PCBTlfr-GojRxPq4Co1FazJQ1AdM4U_uTSR4Y4uEULAT9iC3_vaRuHxfKnvS3HoUhphlRXr1-pjaau5zeQ-fi1naPj-0vFMTvKR7rpf_Hr0oY-rb9smfuUh7YqnKogT4uiTAZHyr8ang3Q68Wr3ajFlUFNrzVBiVKMaNsrG6tTXo_OMLR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به السد توسط آسانی
🔹
استقلال ۱ - ۰ السد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/689918" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba5c5864e.mp4?token=dA0LRNcOegDMJkIPexAyaKuPzKpb7EHFAuQgAZda0Y6mLmNh2hR6BWCeQomorhzKSO0L_0K_RyhGcRenS9k_Bp0-izcB6Y_5Ar9Kta9j9oOTDNrZGYDL-ZoPe2iklrJ2-d8fKmR65tOBa7qHkExZELDwD6_MoTqIc49XMQ_heTllIbN68UMoDuRCf8mrgW5Tnd90IOlCYjGuu-zUPgNcdhSvBlz_7L0hwlm2sCMqStXHaYrSZZDiZ4IGpsYoDxhrsQTu51cteucxlcfU2-fHp8inaEYwm8zwAmVJPwrDx9SmeU4DWHA5NO8eL6WbPgwv-wbnJkWTH8xGoRwjn5G7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba5c5864e.mp4?token=dA0LRNcOegDMJkIPexAyaKuPzKpb7EHFAuQgAZda0Y6mLmNh2hR6BWCeQomorhzKSO0L_0K_RyhGcRenS9k_Bp0-izcB6Y_5Ar9Kta9j9oOTDNrZGYDL-ZoPe2iklrJ2-d8fKmR65tOBa7qHkExZELDwD6_MoTqIc49XMQ_heTllIbN68UMoDuRCf8mrgW5Tnd90IOlCYjGuu-zUPgNcdhSvBlz_7L0hwlm2sCMqStXHaYrSZZDiZ4IGpsYoDxhrsQTu51cteucxlcfU2-fHp8inaEYwm8zwAmVJPwrDx9SmeU4DWHA5NO8eL6WbPgwv-wbnJkWTH8xGoRwjn5G7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دومین ایستگاه پمپاژ نفت در خط لوله شرق به غرب ینبع عربستان سعودی مورد اصابت پهپاد و موشک یمن قرار گرفت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/689917" target="_blank">📅 21:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689916">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9280344e02.mp4?token=rJaSOzRDgokoNddRgGiuJ5SzN4S7QYTbMh9XGHXraVAYU8ZHrbOcFZMEz81dSNnaBCsMR4uFF29vRA-IskRqt5EnK6_kMujXyzlqvIg4MfH7Tm5yppWqjxaHN9XNyGxcnInwr-xLOqCaEY-D0tsQcgLMnrJBw_3aPwnm1eoH1PP0nYi3bH28y0GiDhUunNh6wRmI47tQeeHJmwyO_bpXWWh2N-dNabGKoNRYJ4uaUHZVA7qtzMDR1_8EIRP91BIcCqe_FjlXGrpxCcyyjptm87RdC_wl2cI5lYlaIGzKaalJerCTpzwEfR11YwR8x08j7sXIbleyfLiA-x7dKXengqdwXPsNVs9fAub04bG10QGhCIxN1edjAXMDbwKvIFqVE1KbOX8jwS7s03zx9opc8sVa9yFILw8TB-S-g8OhtZWUyK_jebfy_AMwgePscurfJvanG_KUPR8qW_bRJJTCN9XJaMFoY_MCpUq6MrqNtw0pgJ_RLHQbtf39DATnA3kF6r-Vxh5SrdUoODwT6ZZmS-W5uEALOkW5nF08PX5j_ubQpTr6QR8phItA9Deg7T75eVfsMXBjwZQLO8Bp84HBDKiOsxHdshReA1u-7KdCUKOsKl89itRYWY4fqXT_1ttzaiz78sti5x2ogqFU1dfLN8iDH1EY4yFZCXCdGX6TZl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9280344e02.mp4?token=rJaSOzRDgokoNddRgGiuJ5SzN4S7QYTbMh9XGHXraVAYU8ZHrbOcFZMEz81dSNnaBCsMR4uFF29vRA-IskRqt5EnK6_kMujXyzlqvIg4MfH7Tm5yppWqjxaHN9XNyGxcnInwr-xLOqCaEY-D0tsQcgLMnrJBw_3aPwnm1eoH1PP0nYi3bH28y0GiDhUunNh6wRmI47tQeeHJmwyO_bpXWWh2N-dNabGKoNRYJ4uaUHZVA7qtzMDR1_8EIRP91BIcCqe_FjlXGrpxCcyyjptm87RdC_wl2cI5lYlaIGzKaalJerCTpzwEfR11YwR8x08j7sXIbleyfLiA-x7dKXengqdwXPsNVs9fAub04bG10QGhCIxN1edjAXMDbwKvIFqVE1KbOX8jwS7s03zx9opc8sVa9yFILw8TB-S-g8OhtZWUyK_jebfy_AMwgePscurfJvanG_KUPR8qW_bRJJTCN9XJaMFoY_MCpUq6MrqNtw0pgJ_RLHQbtf39DATnA3kF6r-Vxh5SrdUoODwT6ZZmS-W5uEALOkW5nF08PX5j_ubQpTr6QR8phItA9Deg7T75eVfsMXBjwZQLO8Bp84HBDKiOsxHdshReA1u-7KdCUKOsKl89itRYWY4fqXT_1ttzaiz78sti5x2ogqFU1dfLN8iDH1EY4yFZCXCdGX6TZl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترور عالم اهل سنت در زاهدان
🔹
مولوی یوسف گرگیج، از علمای انقلابی اهل سنت و بلوچ زاهدان، توسط مزدوران صهیونیست مقابل درب منزلش، به شهادت رسید.
🔹
اخبار تکمیلی متعاقبا منتشر خواهد شد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/689916" target="_blank">📅 21:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689915">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شبکه عبری کان: جزئیات عملیات ارتش اسرائیل برای انهدام شبکه علی الطاهر فاش شد
🔹
این عملیات سه ماه ادامه داشت و با یک عملیات فریب پس از تصرف شقيف آغاز شد.
🔹
در جریان آن، ۵۰ عضو حزب‌الله که حاضر به تسلیم نشدند و تا پای مرگ جنگیدند، [شهید] شدند. این افراد داخل…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/689915" target="_blank">📅 21:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689914">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
افشاگری وزیر نیروی هوایی آمریکا در خصوص نظامی کردن فضا
🔹
«تروی ماینک» وزیر نیروی هوایی آمریکا فاش کرد که ایالات متحده سلاح‌های کنترل فضایی را در مدار مستقر کرده است .
🔹
ماینک از برنامه‌های ماهواره‌ای نظامی مرتبط با دفاع موشکی و هدف‌گیری دوربرد نیز پرده برداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/689914" target="_blank">📅 21:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689904">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IImgPl0RP6U43xlvP5fvjTF0ZsLUGbQb1nWirpDQ5qnkJ0f0i6Q00E0WtEpjPugfDPYhewcqqS9ZNx2JhWMwVUARv9sgkb8M3rj1jannhqU4-y7vaaOkYNlPLnsqnW-vp7ZJE-1JOonIy79Dwt4QYzfdOUfo0nePZHLBjiRaFa5byE-t3SVdF-CAK_bHAzmE8P9eIivfryFCLyK7kcgraCNSEma0j0g1bgKqGTumJw5Mcm5xNVEfLMyfki0Ssy-xkGTo01kvOAwtKs_IQuwDxfNR-M1Sxlu6_rHdD-khG0CHcO2lOoOHRE9sFRaKJccAvFuMaJw0oXhmJKG5JxEGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZHqtOckg8Vrx6apQMpC4ojpCuVq_Ysac5jlXoVcB-DVIFLMmGVTEgIsYFM-BtUSqUFT1y_9jxl0fLztXKfmStmKcyFf7_ncH0yhaq_cphfmptT8ZJWfO3Pq2G-Aa2PmNDCAG6JVjS5IDQlbT5ZnadD0Pmmu3FTuApWvDH4CpPqHD0KV-3zE6wmhW7h0li6X-cxgYmG_1ulUN4RGChTkNW_1TwVS0okuz-OQ2eWn0dyARXjEmfQZ6cvENeeBSK6h2PEutmWPsJ5IB1uUuQCCXilFovgFJaefpABpzj4ybc53mTDhzKqP5pNxuz1hpL_tn7a2kEfpS29Q_411-gDn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eM-VlfP4-nygCWN04Yl6wVtLFJjgllvVQR-_iAfnDNms53epjeKdACcRyVKir601vamE4jk1HvMAmXXg2yLa6N__Ae-ueD6NIIvJyQ5qpBuct8toUToRAeq3lqz50giuvdZUH67mxpD_DzQlYd16VNNszaMvmD51mQEd0QMPsg9ITFlJwDjMAnWBvqE7sY8hk2fpaXZ6cCLJxK6scxBwwGdj29U2Ya0CqXzpAmZXATkip8ohfCeSfwCqFE4Use6p5UeBzRnW_K855BfcclV0unoH0F8noMbUBtBlSjrv9Jsx4_ahi_zh3DoGUCZVmqwBtJCmbUNTymMSODh23ITwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q24BkJyYdWvjrI371JDGAPmmUwngFO0JIc5F9dSUqebfffxBbBUdJqoDyW3sWtAWWL2_Q2b7kdQxjWwPQxdRM2gla_sG1o4SF4xKfthMagpgZx2ub3JgfBitQvG85hAZUg7nm0fKuVs1P3zWamu7z-83B39-DkPPm9WkSSQtGx4phYyUtzY5Zo1MFOWG3qcXn-orFSEzbiwqMvnRzt0RJ-aKzWNOVJOcWIvFIf8ZDSNFq2Iz8H7pStmJ4a-lunTsoK6sbPPbC6vckhkRBq-KxaU8XJDOiBHmc36hu5JvjTnc_Dk7UJfNc3U1zGtENwqBssqn1lIxs78XmUeri6z2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEazHcFvaS5vL0tO5sCNx07vcAMg6-DdD00Fcx8quwPggXYBxD3XuY2CfPEWdgtTNboW3Adm8_fLpAfhjS57uhIePkTUmplcjkH3mK_NDBQM_GaZKRuJN8HWhZG3mr0I-3bL7LCZN1Hme3Gn64vre6pkPVJ9EKRcVV1V5FksK50DmmlMUfr2w6XyF1ZJpRHoz0YiNiG46ySwhISxdP05oxMWBIDVY8JVgsGFC8Qo-HVPuY7VEuconARmxVyILvcnmeE5wZqt1GHdhB8YscDTMZe1pN_KLkjCOEDYvU2A2vBJBOpwpObJtuGHfflBAzDmc-WsFKSuc7WQYXnZ0K8CDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqzDe5cMTDxQm_fL4CnriNIXsMQ_BD_nyGNd8depV4eRhjqsJ5oZQjT9vTJnrnsGsfp-S7_Fx-cvEUix1khEZSrFN-RBX-rA1pnQ_D2b3PtfvI_MTpJj_PgQyKRI-gvxm4jszjX6UgZbskTVxT9BlbdOVctHuo_PJuAxA1QttAGFB2NrETGk-VJI55xx3hUp1w4KbEGifK_u0Qj72i4XC5F3vcJSfvk25l_a76UQyWa2aILEFhmVPV5Wxl97iHLN5s8ZPruu_nceZk_BRb1qcP3PjqL3MmWr1-7qj_psaathj5Vb2W9BTzE7Fd17-59o75_O8Xd3XNm5IRKELVxMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIJQOfiFP4WruzvPmJ4tnjoAebpVXCsI_5Zt-qxLxaqMlJ71ym9XIs0f5bNhjROMwRFMLbT7BaaAHonMpi1R_IFfOvf56DWZDdAqJDHxRwkKoGzBcb1KIoX4IKFbExZGG8FwhA52VYdAKuFn6gdAwb3fY5RBPLezuzZjM0eW4vMVWnc-z8-H0p5MNLON_Ar3ReXDtK1JJ3M7gPMago-4W81QFppJgY-cUGjP9kIltkCoaPiaYD6Vp0ooxEFhMTrcApeZrczipTluU8E62hD0QRvLA_vfEJldCLbqx1jDggH2c0vgc0VpEqRePAXCJQ26Wlgb3vRW2XiJzOQZkYk8Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c44eP2oq-atuA6z-NiBrKJR9YYMruc_ZwOyxMeCtl942zdaPfHTu2FzEQdbFHZfGdUmkbTXooFWcjoDNlYqMnTCDRr4s7vD6e3g2zWEB4LMAgQY6oi8dG9DRrZD-yORz0b4llGnZKFvoGYW0XzkNr9PVXCQV-lBiOBnFoaqnpE_ao_Q_kByn4-iOUtwnH9tyfiWhJRBb5qc4Va6hEb3BnXAWzZckU5TRJpa55ieZC9dZob7JU6Rhh7lGcnjb6DEw0JqF5KuN0mzedjJr5wsG3r4SXNw_RRNRYLOpvpTVAzUaMaVLBveUrfo1h5bPxPfBcvSzBfP5DnA0u_nHHdUL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nv1ZHMC-ssysvFdFIx1fIa5mIQA8T4DpekV_-4IHzlFhuVvPqilyKNNJo1-qggxrwS4jvNJ6qUMwwBZKghs2huLCmXmNTiPl7lLx67yAUmKLUsjOamZKWYq8ejqzCQzdN5uGl4T7CyvDsgrYFw231mSbnT1_61_Ee3o-4BQwESpkskSwFec5IKA7N-_xgKEAV_0VNrAocM9qQco9twTGZv6_v5a8rH5IM8P4ty9wIDVZ6WAbNz9d76uEYC8rbGlc3KeD-FTNgCXvYhwZclG5l_a1ku4wSTmuIyZkBLgJuJHJfYHvu9Dy8y3nofsz5DwNALluv6gwF46dSMWBvW1prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1CKelDcHv9VMhjsazLVsrQxPhvhqEZwTHRsEus6NWH1cMkey-Yk2OWYZA-qdeEhzuZaAwT2uUClFTBwAVoSp6v4-Tnj0GtRofXLtgOWCi5ZXx9u4QV5HCXZxuzMd4lQxDs0TIXtL7V06fGx0nzBcdXbmK7XSLb3bi_UI-XniXQKb9nkRI12-5HHkOjvizU0PEgxjMOwmtCs1uWPZYZo4AD6_46ggISTiflD0x7Mra3OMVt8bVHTPQDx1FMv9p7vKT3IYrTQupktCgSSRn-t1cJ9ByP2U9icpV8ktiXcXmGkAgygDmC5miYuDkYIYOqo6r6N5L2mssM3djsiRUKd-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
بازتاب مشکلات مردمی در حوزه دسترسی به اقلام دارویی
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/689904" target="_blank">📅 21:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689903">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پزشکیان خطاب به آمریکایی‌ها: حداقل مردانه بجنگید
🔹
مدعیان حقوق بشر و انسانیت، اگر صادق هستید، چرا کودکان، بیمارستان‌ها و زیرساخت‌های مردم را هدف قرار می‌دهید؟
🔹
اگر مرد میدان هستید، بجنگید؛ نه اینکه با ابزار و تکنولوژی، انسان‌های بی‌گناه را محروم و آواره…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/689903" target="_blank">📅 21:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689902">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منابع عبری از وقوع یک انفجار در منطقه الخلیل فلسطین اشغالی خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/689902" target="_blank">📅 21:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689901">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ایرانی‌های خارج از کشور خودشان رو به جانفدایا ایران رساندند
🔹
دوره‌های آموزش
نظامی و امدادی
ویژه داوطلبان پویش مردمی «جان‌فدا» از سه‌شنبه ۲۵ شهریور آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/689901" target="_blank">📅 21:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689900">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fcd96d8c.mp4?token=AZbPwI2HPqnwhDwov9DmThiAg11n4cjUbFbXIGoxWEyFbaBt9gVUfM4HCYSA_gBeXsnUKNSaj7tcSeQdr94nf43gWwP4X-9dfhCkBX4_cvMFSNP6eb9S_OM7TTQo_YMvrcTODuaoo-knAvYfpTUfXcmKWYYo1-u3FgERyQUXU_LPww4EylAnAeXZgZnWVqJmMu7mna8R3Ton1bJJuUnRPLsRHU1grQGxEsFldNdh7hJqb77U8VgjBc4X_s79HsP0-pJSBl7n5sMmi54I48vrJKU9PZ3c0MCK3Tit60K23CSXDsh8bpJ-YvSLlXolVRwmPJcSM5zxNvtZg99P1GKI-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fcd96d8c.mp4?token=AZbPwI2HPqnwhDwov9DmThiAg11n4cjUbFbXIGoxWEyFbaBt9gVUfM4HCYSA_gBeXsnUKNSaj7tcSeQdr94nf43gWwP4X-9dfhCkBX4_cvMFSNP6eb9S_OM7TTQo_YMvrcTODuaoo-knAvYfpTUfXcmKWYYo1-u3FgERyQUXU_LPww4EylAnAeXZgZnWVqJmMu7mna8R3Ton1bJJuUnRPLsRHU1grQGxEsFldNdh7hJqb77U8VgjBc4X_s79HsP0-pJSBl7n5sMmi54I48vrJKU9PZ3c0MCK3Tit60K23CSXDsh8bpJ-YvSLlXolVRwmPJcSM5zxNvtZg99P1GKI-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی کمیسیون سیاست خارجی مجلس: آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/689900" target="_blank">📅 21:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689899">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c9777049.mp4?token=XPTeFGd-qbzCPFeNTEa0ykj1FqEr-jILr42JDeEeFL0gMbbp1Pn15_WMxbGOqq0ajZmrIuGF9TO228VnMQS6okBJAuW3QPIWkadU3XH5pdC8N7fOrXMypJipTZXqWnn6-jsgvFWwRFXoVFtAGysQbXAbl7-OF3Bxn43nqo3qGOYOWh1YEVyqtr86RC4POBrp36YKxuw3BXELCnkamOOgz4FDh49DLC4GeXEUHzf_73zs9LJr-3MYP_WGxNX6M9MXoPd7NWOpzEIP7wCRIKx1K6_YkEnKTwrNFTVCkH2EfwOAuFqgrbDDthHSV86G5hx2ob-lZQ0uEoth8b_EZNPm1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c9777049.mp4?token=XPTeFGd-qbzCPFeNTEa0ykj1FqEr-jILr42JDeEeFL0gMbbp1Pn15_WMxbGOqq0ajZmrIuGF9TO228VnMQS6okBJAuW3QPIWkadU3XH5pdC8N7fOrXMypJipTZXqWnn6-jsgvFWwRFXoVFtAGysQbXAbl7-OF3Bxn43nqo3qGOYOWh1YEVyqtr86RC4POBrp36YKxuw3BXELCnkamOOgz4FDh49DLC4GeXEUHzf_73zs9LJr-3MYP_WGxNX6M9MXoPd7NWOpzEIP7wCRIKx1K6_YkEnKTwrNFTVCkH2EfwOAuFqgrbDDthHSV86G5hx2ob-lZQ0uEoth8b_EZNPm1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏ماجرای شناخت رهبر انقلاب از فیلم‌های کریستوفر نولان  روایت فرید حداد برادر همسر شهید رهبرانقلاب:
🔹
آیت‌الله سیدمجتبی خامنه‌ای با همسرشان برخی سریال‌ها را می‌دیدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/689899" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP09lB-ZilPspsvEQuxKo9I9U4NecJ5bta4LLgG3NoJlePwMVG13S9OZKaFW0NhRhgrUhGdqKv8cG6MaPHCGAuZOQWjAo34RuK3oK7dxDuFy2XSzudvaTkhikPl8UUhHC00sCQAl87RFxj_19UifLuXih0T9wIUysLOyOYbalrcbpH5xFEDN4q_q34bVs20YfssFuoS9W9eQQ7ieIpWDq3FitZI4fpQE99VnnB9x6a-mjUHgeALrKgsKHfdFUfdLr5RJ3mGKOHPpi_OvmzB0FyokvXE2RijYmRS87gwmBSwGw_q86EOV867IhjLi1kRFDCKW2OT_geb2vRdlVXGAGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل صهیونیست‌ها از نبردهای پیش‌روی یمن
پیش‌بینی تحلیلگر یهودی:
🔹
درگیری‌ها در یمن وارد مرحله تازه‌ای خواهد شد؛ از تغییر خطوط درگیری در عدن تا احتمال عملیات‌های همزمان در منطقه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/689896" target="_blank">📅 21:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689895">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkMbi-mNK6sPPAcoPcr_ot4r5S4lqBDPPhtlCpJM9u09XcoK552fr8nSLv6bPDU6MWp-W4-WTJ4zR_2XqWnGKUfQVPYPMfjOupsZYZxDu7AO4HC9IKyjAG7mRfkubAmfhqjJh5vm9bn7HfuOnXCjE2od-Ug10NG52kLbVOboo07e5MU3jONdQgG_1Bl_X1GMx3jBDO0tB-gxEXHyTyNwW680ebWVyfwwkP-FIGtHcV-br_ccAO8HN-8TSrDGizRdIt-6iBT6aklGMPLeZnjpKeEizak6DW06s5_QtOaNYQkmdrxzuP5gfIwynvV6DLYTr16ZZsUqu9NAF5hQ8b4Osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل اول شباب الاهلی به تراکتور در دقیقه ۲۲
🔹
شباب الاهلی ۱ - ۰ تراکتور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/689895" target="_blank">📅 21:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689894">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
پزشکیان: جنگ، تحریم و اختلاف‌افکنی؛ سه رویکرد دشمن برای به زانو درآوردن کشور
🔹
دشمن از یک‌سو جنگ و تحریم را به ایران تحمیل کرده و از سوی دیگر با اختلاف‌افکنی داخلی به‌دنبال تضعیف کشور است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/689894" target="_blank">📅 21:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689893">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e5eddd5e.mp4?token=E3KkomwmiO6CtmmaSlYsGjFwoM3cI-wZ3vii26axdEQC9lduF9sEGMkj6PQ2DpKKZ-iInFZdfPkFCmz2CQlaQWFJ8u3JBBmroO_yc5DRzgEuVwX7-qpvQGLubnXpLiCJAc56EfcoL4aA_IR6oZ1VlQvOrCimJH3daFWtZAEIVaLjPnEWWIPrmheyNEUGO5JwDerLgqMdbj-rfSfv-1XmsHU8u_nNgZ8JZyMKAcuIWGZU5ZScSYMTaaEwfkGXUiLxuUwlkkxJmVqQvKJ7oiVIOAEh-Fik8YmR1eZA89GTnqjjjIO2R9sH9HxDg2Ff_BqZCZSsEo85uqxw5B2kBjwLZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e5eddd5e.mp4?token=E3KkomwmiO6CtmmaSlYsGjFwoM3cI-wZ3vii26axdEQC9lduF9sEGMkj6PQ2DpKKZ-iInFZdfPkFCmz2CQlaQWFJ8u3JBBmroO_yc5DRzgEuVwX7-qpvQGLubnXpLiCJAc56EfcoL4aA_IR6oZ1VlQvOrCimJH3daFWtZAEIVaLjPnEWWIPrmheyNEUGO5JwDerLgqMdbj-rfSfv-1XmsHU8u_nNgZ8JZyMKAcuIWGZU5ZScSYMTaaEwfkGXUiLxuUwlkkxJmVqQvKJ7oiVIOAEh-Fik8YmR1eZA89GTnqjjjIO2R9sH9HxDg2Ff_BqZCZSsEo85uqxw5B2kBjwLZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعاهای برباد رفته ترامپ
🔹
این اتفاقات دو هفته گذشته ایران یک ادعای بزرگ ترامپ را زیر سوال می‌برد.
🔹
اقداماتی که حالا مورد توجه رسانه‌های خارجی قرار گرفته است.
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/689893" target="_blank">📅 21:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689892">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns-wzNX5cx0xNjwwTEUccLzn_f1ncyt0Mp0tv6T4DRECCHOFp5OuRfQmAgMmvoVPZr3M15ZTZeqS9J5ZhY_WatcFnTgvd6Dk0Q-fbWYqzWa1QMvVj3eTMNTZYaD2OiKgdULLC0MXoNynS_lKsh-TAK07iXnrHmB0J7BYsJM0dXxugO6F3CW49cm0DK3yOGzpKMwdqh8Le9MwFcrQOtJ6a4Obh8bDRDRsmy59QmGD_uro-VJLfGGfb51NbxJKu5r3609unxEFA_8ovshq0eSaIoi5q9sWdJr-vW4awnFnGhnDY0zglfw6f0mEQ0d0o0H6vDgv1THO2DUFvLPV48o3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین طرح دیوارنگاره میدان انقلاب با نمایش غرق شدن نفت کش‌ و ناوهای آمریکایی
🔹
همزمان با هدف قرار گرفتن ناوهای متخاصم و زیردریایی پیشرفته آمریکایی در آب‌های خلیج فارس، از جدیدترین طرح دیوارنگاره میدان انقلاب تهران با شعار "لشکر شیطان در خلیج فارس غرق خواهد شد" رونمایی شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/689892" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689891">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشاتوت | نرم افزار حسابداری و CRM</strong></div>
<div class="tg-text">حالا فرصت شروعه!
💜
مدتی بود که
شاتوت
رو مدنظر داشتید؟
از
۱۴
تا
۳۱
شهریور ماه، نرم‌افزار حسابداری و باشگاه مشتریان شاتوت با
۲۰٪
تخفیف
ویژه
ارائه می‌شود.
اگر مدت‌هاست به فکر یک راهکار حرفه‌ای برای مدیریت حساب‌ها و مشتریانتان هستید، این فرصت را از دست ندهید.
⏳
فقط تا ۳۱ شهریور ماه
برای دریافت کد تخفیف فقط کافیه عدد
🤩
رو کامنت کنید.
#شاتوت
#گزارش_مالی
#مدیریت_کسب_و_کار
#حسابداری
#حسابداری_ابری
#جشنواره
#تخفیف
🤝
با ما در ارتباط باشید:
سایت
|
تلگرام
|
اینستاگرام
|
آپارات
|
لینکدین
📞
0513-1237</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/689891" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689890">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
پزشکیان: دولت تروریستی تشکیل داده‌اند و هر کس را بخواهند ترور می‌کنند /با همدلی مردم ایران، مشکلات‌مان را هم با همسایگان حل خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/689890" target="_blank">📅 21:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689889">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رسانه عبری: برگزاری گفتگوها میان عربستان و اسرائیل با میانجی‌گری آمریکا  وب‌سایت صهیونیستی والا:
🔹
برگزاری مذاکراتی میان ریاض و تل‌آویو با هدف مقابله با تهدیدات یمن؛ گفتگوهای میان عربستان سعودی و اسرائیل با میانجی‌گری نهاد تروریستی سنتکام انجام شده است.…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/689889" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689888">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNyUrAvykpCgyV3aK535D2-nnWJ8Y6OUFRgyAgzqRPslzHBsQAdpyj7Adiu7jO--Tgwv7XnizQYK4DeFmeo-pjppSZ-eFOkd65bsyLVGEw5RR_bkDDOIzIS_DJekVfuFxX5yKe1R42YHKSGflicbbYHcjZigqsxsoGnBYAlBMojE7VmtyAm01eLZ0ZMQDa4FKWCTyboeDQ3TfsQJDK1nZE6CkBH7Ou3iUSCApgx6lDcvV-o4oTjPyFsec8pp8TFLuAOw2pL_rmM3KiPraVXBgB4iFOumc8zZbfM_uRkhFQNOgrHvMvqBnBIigd_OzPrbfH9Elh1-jsEYlAHKZDS3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چندتا ترفند ساده که احتمالا هیچوقت نشنیدی
😁
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/689888" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689887">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833d04deeb.mp4?token=NobXDshLofHhqWTAyh6S1WiH87hZRlB9HoWLZ9d8kJFPtz3sUhu7ihOl0BHqGwKT0Ebpy8YcwrN-jpNwQcn4aWtdXHgUbI9CAXeFB_yQufNJ2DkCWQ4vHb2J7OV-0FU7k86RyDt7nZtuqd_4xaMK4P9oEv9emrvAa5ZGLRVjmGqEAdV6w0avwLVA361zlM-icY4naoGZDNsTAe3yDNZOi4G0oz6yvl6LQNZH1NRNve5NnelhEFBWECBJBmQSHqH5HEbgWuwOAcW0fmndO-fG9tULMyiSVsC51qz_0ricGwbicBRSplU-2GRe4iUq9Xm3fN7VxveQjQ3RyscrbsiCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833d04deeb.mp4?token=NobXDshLofHhqWTAyh6S1WiH87hZRlB9HoWLZ9d8kJFPtz3sUhu7ihOl0BHqGwKT0Ebpy8YcwrN-jpNwQcn4aWtdXHgUbI9CAXeFB_yQufNJ2DkCWQ4vHb2J7OV-0FU7k86RyDt7nZtuqd_4xaMK4P9oEv9emrvAa5ZGLRVjmGqEAdV6w0avwLVA361zlM-icY4naoGZDNsTAe3yDNZOi4G0oz6yvl6LQNZH1NRNve5NnelhEFBWECBJBmQSHqH5HEbgWuwOAcW0fmndO-fG9tULMyiSVsC51qz_0ricGwbicBRSplU-2GRe4iUq9Xm3fN7VxveQjQ3RyscrbsiCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: دولت تروریستی تشکیل داده‌اند و هر کس را بخواهند ترور می‌کنند /با همدلی مردم ایران، مشکلات‌مان را هم با همسایگان حل خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/689887" target="_blank">📅 21:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689886">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
هر استان به چه خودرویی علاقه دارد؟
🔹
پژو ۲۰۶ تیپ ۲، پرفروش‌ترین خودرو در کشور و پایتخت است و پژو پارس و ۲۰۷ نیز در ۱۷ استان دیگر صدرنشین معاملات شده‌اند.
🔹
اما همه ایران پژویی نیستند. در فارس، دنا پلاس محبوب‌ترین انتخاب شده، آذربایجان شرقی به سمت ام‌وی‌ام X22 رفته و در گلستان و سیستان‌وبلوچستان، خانواده سمند حرف اول را در بازار می‌زند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/689886" target="_blank">📅 21:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689885">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBniefWUxRD918EayzZyuVkH2kyg222cTAluje3zEXqLn_HI1mBvwG3eLyhANu365VSUc8flhjCT_akzF9W3_0MGHCSrRBwhwd9Kz2W2VUc0LjXyB8IMVMQHCkycs6h6PXKgXG758Kv11RE7avkDsBn-G5mlHGj29-J7bS9MANNGHBnVxbMfl05riZzm_XiK6BAfkF0_NcXJvja1409HDcae8je-4oObTCBulb4j_ScX3F4qvL9QJ4EHDvkeWo-ErbMPPESpiqI9c0apxaBZzmbegx_eH3jqAsjhbtgaYtzRxITLP2h0qFEN8n758DdrYzBtZbGVynaKTB3nvBo46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیان ۱۲۰۰ میلیارد تومانی قشم‌ایر از دولت سیزدهم تاکنون؛ وزیر نفت چرا پاسخگو نیست؟
🔹
بررسی صورت‌های مالی رسمی قشم‌ایر نشان می‌دهد زیان این شرکت در سال ۱۴۰۴ به حدود ۱.۲ هزار میلیارد تومان رسیده؛ رقمی نگران‌کننده برای وضعیت مالی ایرلاین.
🔹
قشم‌ایر که پیش‌تر با مجوزهای استاندارد اروپا به بلژیک و آلمان پرواز داشت، امروز با افت شدید بهره‌وری ناوگان مواجه است؛ از ۲۱ فروند هواپیما، تنها ۵ یا ۶ فروند عملیاتی هستند و احتمال زمین‌گیری ۲ فروند دیگر به‌دلیل نبود موتور پشتیبان وجود دارد.
🔹
کارشناسان، یکی از عوامل این وضعیت را انتصابات غیرتخصصی و حضور مدیرانی می‌دانند که با اقتصاد ایرلاین آشنایی کافی ندارند؛ در حالی که اداره ایرلاین در شرایط تحریم، نیازمند تخصص در اقتصاد هوانوردی، مدیریت درآمد و تأمین قطعات است.
🔹
پرسش از وزارت نفت، به‌عنوان متولی این دارایی ملی، این است که چرا نظارت مؤثری بر عملکرد مدیریتی و انتصابات قشم‌ایر صورت نگرفته و چگونه زیان ۱۲۰۰ میلیارد تومانی به این مجموعه تحمیل شده است؟
🔹
احیای قشم‌ایر نیازمند شایسته‌سالاری و مدیریت تخصصی است؛ نه تداوم روندی که حاصل آن کاهش ناوگان و انباشت زیان بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/689885" target="_blank">📅 20:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689884">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951b617d5f.mp4?token=KisJFRHEO5TitGR3RUnK57Jw8rpsAoYpYJI7P-lOp5TAs9uX3KktA32K9NTyYrDa7QOSJrWIWROa3BRfxzebnI4oX3wXSQ883KAmhAh5_YC9ls6zh3zUEixN_kI0hZOU_6Z_OV3dfIeAO2xvvDi9UmkdvIbHjGs2qD5nli7TsLqlfTOns1bHV29URz0gux0wg4XbznuDjeoIqo7iYyQYuMcVr1LJWb-ddP2T2QmtGxAazoig70mW2Z7knkEchIZzk9JiBIpnUWmTxB1orwOcpYtlT9L4whWHOGJSaxep1Z7Q9f52otN9QYpkO_ZWsRT1Lsqj2FLwnS1d-hmStUWC8nhiocBtmegwu2O_B1aSeo138RZftRsD4Vc8IHk9eYfEl8yhsWA_kwOinqCcnpsYRH1PEKwNcrFmL3t1GdMmUmtx990UF58NZC62vKBRg-zLL_sF42dPqUcAxWbdW-ImJUhiEG0AbaQYMsWSp23V9-N6VoN-zL1Sw_Nsx3lbc6rJGY2uCFwD_zrgEUV4x6yt9kUzQ0ZqdvvRn7Xf9WO9ygGbT_ntHTZ7IB3vQRWLVbnLdmwY8IumFSY9rX4-0w4B9dHejwUhFkDzw47qk9lH_BEv_9nRTJ94I8U6IEXvGhu_oypLEfYOmswtDsdwCTd_9TJzgs09egHCR0vKKosJV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951b617d5f.mp4?token=KisJFRHEO5TitGR3RUnK57Jw8rpsAoYpYJI7P-lOp5TAs9uX3KktA32K9NTyYrDa7QOSJrWIWROa3BRfxzebnI4oX3wXSQ883KAmhAh5_YC9ls6zh3zUEixN_kI0hZOU_6Z_OV3dfIeAO2xvvDi9UmkdvIbHjGs2qD5nli7TsLqlfTOns1bHV29URz0gux0wg4XbznuDjeoIqo7iYyQYuMcVr1LJWb-ddP2T2QmtGxAazoig70mW2Z7knkEchIZzk9JiBIpnUWmTxB1orwOcpYtlT9L4whWHOGJSaxep1Z7Q9f52otN9QYpkO_ZWsRT1Lsqj2FLwnS1d-hmStUWC8nhiocBtmegwu2O_B1aSeo138RZftRsD4Vc8IHk9eYfEl8yhsWA_kwOinqCcnpsYRH1PEKwNcrFmL3t1GdMmUmtx990UF58NZC62vKBRg-zLL_sF42dPqUcAxWbdW-ImJUhiEG0AbaQYMsWSp23V9-N6VoN-zL1Sw_Nsx3lbc6rJGY2uCFwD_zrgEUV4x6yt9kUzQ0ZqdvvRn7Xf9WO9ygGbT_ntHTZ7IB3vQRWLVbnLdmwY8IumFSY9rX4-0w4B9dHejwUhFkDzw47qk9lH_BEv_9nRTJ94I8U6IEXvGhu_oypLEfYOmswtDsdwCTd_9TJzgs09egHCR0vKKosJV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از اجرای یک تئاتر با انتقادهایی در فضای مجازی همراه شده است
🔹
منتقدان به نمایش پای برهنه بازیگر زن و در آغوش گرفتن بازیگر زن و مرد اعتراض کرده‌اند؛ هرچند این دو بازیگر زن و شوهر هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/689884" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689883">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVP07bhDTWMGSlIWC3TKcFYpSEzFvXGmzLJa5oFKsWaJYxmbieXSXkKt8h6NiruUanvIn2kFcheNXuv0Y9e0EjX6WMg7LaneNnY3_jWEDJqWO2twEMPgo0RXUxwJ9VYxqYkW1C72Ti8_rvc5xM9VjrZULQWz9-NSp6vTuznpSgJJh5bgZRlIuWLszensF7eDNDnG6qLBVKQHslRbJw_OwUv7yRBvfPAPj8UVmq9lIfbDdTj-gG-ReQRfTjnJUzaO3z-cywC42_ydDy9WJ7Uhz9mIpq-B819GcRvwlH98lIMZ-xOzjC1wXyOq5GSvwYPPV5ZpRJZCYSer7gimdOsp0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حوثی‌ها به باب‌المندب نزدیک‌تر شدند؛ عربستان در تنگنا | چرا ترامپ برای ورود به جنگ یمن عجله ندارد؟
🔹
پیشروی نیروهای حوثی در سواحل غربی یمن و تصرف شهر المخا و جزیره پریم، معادلات نظامی در اطراف تنگه راهبردی باب‌المندب را پیچیده‌تر کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3245220</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/689883" target="_blank">📅 20:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689882">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رسانه عبری: برگزاری گفتگوها میان عربستان و اسرائیل با میانجی‌گری آمریکا
وب‌سایت صهیونیستی والا:
🔹
برگزاری مذاکراتی میان ریاض و تل‌آویو با هدف مقابله با تهدیدات یمن؛ گفتگوهای میان عربستان سعودی و اسرائیل با میانجی‌گری نهاد تروریستی سنتکام انجام شده است.
🔹
هدف اصلی از این مذاکرات، کمک به عربستان سعودی برای مقابله با یمن از طریق ارائه اطلاعات جاسوسی توسط رژیم صهیونیستی بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/689882" target="_blank">📅 20:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689881">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEpdeH3TwN5YoxwdQhfvpyMHMiiMXbhCZzU_PYaK58Hd-LWIgIw4krRRYn8zYHH5iTNvmM-a99AHeBBzfbjxq9b0wnt-0rrJxeUaovcXgl39z7CDDNsYCKPDGyMpMxdUPguSH1u4aHqPA-7jJ7GprkyUxFJNvsste2UW7dQoPrKGVb51zXt55yGG57rnqvo5LOuqqusyZ1v1mUuP21GufzclD_pOV15-sbw_yaRURrNVegQw_raQ7IM0FgF_KVyDK_RFOpVjZSUp76lGE6c6o9SaQgMixLxd4VKEC_40nb3gn83ZdwLFhShzlDnmwbnKQ-3SaNTirQncOMbaqOWvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز آموزش‌های نظامی و امدادی «جان‌فدا»
🔹
دوره‌های آموزش نظامی و امدادی داوطلبان پویش مردمی «جان‌فدا» از روز سه‌شنبه ۲۵ شهریور آغاز می‌شود.
🔹
علاقه‌مندان می‌توانند با ارسال عدد ۱ به شماره ۳۰۰۰۱۱۵۵ و مراجعه به
JANFADAA.IR
برای شرکت در این دوره‌ها ثبت‌نام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/689881" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689880">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
منبع پاکستانی: آمریکا به‌دنبال توافق «مرحله‌ای» با ایران است
🔹
یک منبع پاکستانی نزدیک به روند رایزنی‌ها مدعی شد واشنگتن در کنار حفظ فشارهای نظامی و اقتصادی، کانال‌های ارتباطی با تهران را باز نگه داشته تا در صورت دشوار بودن توافق جامع، به تفاهم‌های مرحله‌ای روی بیاورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/689880" target="_blank">📅 20:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689879">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">15-2 Ane Manaee (1404-01-31)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/689879" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه پانزدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
درهم‌تنیدگی حق و باطل در دوران معاصر و دشواری تشخیص در دوراهی‌های انتخاب [00:00]
🔹
سنت الهی در فریبندگی ظاهری باطل و سادگی مظاهر حق، آزمونی برای انتخاب بصیرانه [08:11]
🔹
حسینیه ساده جماران و شکوه پوشالی کاخ سفید؛ مصادیق ماندگاری حق در عین سادگی و سقوط باطل در عین اقتدار! [11:24]
🔹
جولان موقت باطل، محکی‌ست برای عیان شدن عیار دل‌ها در فتنه‌ها [19:42]
🔹
هدایت الهی، رسیدن به سعادت حقیقی‌ست نه امکانات ظاهری [21:30]
🔹
تعریف حق و باطل در دایره لذت‌های مادی، محصول تعریف ما از نفع و ضرر است بر اساس ادراکات حسی [23:10]
🔹
حس‌گرایی مردم، چالش اصلی انبیا در انتقال وحی الهی و حقیقت‌های فراحسی  [27:58]
🔹
سعادت و هدایت در افق الهی معنا می‌یابند، نه در جهان مادی و موفقیت‌های دنیوی [37:20]
🔹
درک و حرکت در مسیر حق، تنها با تحمل چالش‌ها و صرف هزینه‌ها ممکن است [43:30]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/689879" target="_blank">📅 20:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689878">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioSKywS8T5OhjChnZhqkbhFCUkLG5dchrl8INg9b_qVlnnbgQ6pMcVb1O2k8RhGGHqdTo729ZScdE8qqZ2CK_jTd7Xi1Krh8Fi3w_OUb2HGQn4aPN3HyAmzfyTf6_dtmikxQIPRJRvlR7hZlX7_-_w-rNW7ncOiZIiXRAIREnXvqc9POT5scycAAvPfLPUDc-NhTEGv7cMnBXq8Qpynf2DgeXptgckjuQ1nkQthlvekAGrGv9nCNm5R7jed_MOVw5Jgn7xyPIhDKi8qNvLBsPrLj7BUWiknAO0Qs1l80E4TrCLLFPRBLndrrConKqeEjcRXwd8r9KefDlmWSX04xNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: امیدوارم همه متوجه باشند که افزایش قیمت‌ها در آمریکا توسط بایدن ایجاد شده نه من!
🔹
قیمت نفت هم در زمان بایدن بالاتر از الان بود، و این ما بودیم که مانع دستیابی ایران به سلاح هسته‌ای شدیم.
🔹
به استثنای نفت، قیمت‌ها با سرعت درحال کاهش هستند و به محض تمام‌شدن درگیری نظامی با ایران، قیمت نفت سقوط خواهد کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/689878" target="_blank">📅 20:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689877">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
عبور ۷۲ کشتی از تنگه باب‌المندب طی دو روز
شبکه المسیره به نقل از وزارت حمل‌ونقل یمن:
🔹
طی روزهای ۱۲ و ۱۳ سپتامبر، در مجموع ۷۲ کشتی از تنگه باب‌المندب عبور کرده‌اند؛ در این مدت، ۲۹ کشتی در روز نخست و ۴۳ کشتی در روز دوم از این مسیر تردد داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/689877" target="_blank">📅 20:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخیرینه</strong></div>
<div class="tg-text">🔴
مشارکت در تأمین آب آشامیدنی مدافعان وطن جنوب کشور
#ویدیوی_بالارو_حتما_ببینید
👆
​
📌
در پی حمله ناجوانمردانه آمریکا به تأسیسات آب‌شیرین‌کن هرمزگان، روند تأمین آب آشامیدنی در این منطقه با اختلال مواجه شده است. برای پشتیبانی از نیروهای مدافع وطن، با هر مبلغی که در توان دارید در این پویش حیاتی مشارکت کنید.
​
👈
حساب رسمی گروه جهادی خیرینه:
💳
5892107050077463
💳
100150050398011502323560
​
👈
مشارکت سریع از طریق سایت:
🔗
https://kheyrine.ir/product/38001
​(خیرینه کلیه مبالغ جمع شده را مطابق شرایط
مندرج در بیوی کانال زیر هزینه خواهد کرد.)
🆔
@kheyrine_ir</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/akhbarefori/689876" target="_blank">📅 20:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d54341283.mp4?token=EkPNUoj-93Ow36GooSMFR8QJ-6FfL-vyiw3Rnkl5ZyhUZDs79gzAe6JlsJKvUUV762hnU4orzwUnkvhP5_SkTWX_NMs9h6seGCEaDAvNmzL4t_5XBQZiGUJ4cS0jfPHDqLnA1s_pX69clXYYDF9Mv64RCobLGrMIXdZ_INB_wmYRD-DS6awHazQbWqHkT3PwgncblcEgWGl7T24aOhXTbse-gZMqHuaN89PjBAd3zZ33bq9sJJgrBq3J-dsRcszAVB2zOPZ4HIEFvJq7VnKmO84zKkB2MApPn93zXnpcYSYqQ7DRikEAh290zHzTqjACqDewZ4_mt6XXMbPxsLVNmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d54341283.mp4?token=EkPNUoj-93Ow36GooSMFR8QJ-6FfL-vyiw3Rnkl5ZyhUZDs79gzAe6JlsJKvUUV762hnU4orzwUnkvhP5_SkTWX_NMs9h6seGCEaDAvNmzL4t_5XBQZiGUJ4cS0jfPHDqLnA1s_pX69clXYYDF9Mv64RCobLGrMIXdZ_INB_wmYRD-DS6awHazQbWqHkT3PwgncblcEgWGl7T24aOhXTbse-gZMqHuaN89PjBAd3zZ33bq9sJJgrBq3J-dsRcszAVB2zOPZ4HIEFvJq7VnKmO84zKkB2MApPn93zXnpcYSYqQ7DRikEAh290zHzTqjACqDewZ4_mt6XXMbPxsLVNmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنج‌یابان زیر پای سنگ‌نگاره اشکانی را خالی کردند
🔹
حفاری دستی در پای یک سنگ‌نگاره ثبت‌ملی دوره اشکانی در مسیر قله یخچال همدان، حدود ۱.۵ تا ۲ متر از پای تخته‌سنگ را تخریب کرده است.
🔹
بررسی کارشناسان نشان می‌دهد خود سنگ‌نگاره آسیبی ندیده؛ این حفاری با تصور یافتن گنج انجام شده است.
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/689875" target="_blank">📅 20:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آمریکا به‌دنبال خبرچین برای شناسایی مسیرهای اقتصادی ایران
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا، از آغاز عملیاتی برای قطع مسیرهای مالی ایران و حامیانش خبر داد.
🔹
او از افشاگران در سراسر جهان خواست اطلاعات مربوط به شبکه‌های مالی ایران را در اختیار واشنگتن قرار دهند و در ازای آن پاداش دریافت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/689874" target="_blank">📅 20:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای تو‌خالی ترامپ: جریان نفت در حال عبور از تنگه هرمز است
🔹
نفت از تنگه هرمز در حال عبور است. کشورهای جهان که هیچ کمکی به ما نکرده‌اند، باید و در نهایت هزینه‌های ایالات متحده آمریکا را پس از پایان این درگیری بازپرداخت کنند.
🔹
ما این کار را بسیار بیشتر…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/689873" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwFHYmvTKqjkmFpg5YJsuaM0EH39bJo3TFKUjt_eiSl8IMBIlva3HRTVyb1ivbb0AAEWboXYntvTb58LHEf8nD8BXKlN-PhKbtAlSZ9LRxjLI5x3rYSoIttVjGNfc9Jt38iWx8_6NGnhA3HI8Zu7qNXM9hDcLOxZeVu_9-v6wL2nP0_IXhDRiGVTg8UzDnw-raIsMvMZz7bVRkVFv5RV5dFOPSn0axAnWyUQ-8rP5fMMi0w-n5jj8rH5vRgHF_5Z1sxFHEF2hUp7T1_qYgEcC51Ry4hjl14HNtiA_URnQ-3WsZzZh3jV_cEPdITuFWET4dWG9zLUFkjxV52rtf6ggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تو‌خالی ترامپ: جریان نفت در حال عبور از تنگه هرمز است
🔹
نفت از تنگه هرمز در حال عبور است. کشورهای جهان که هیچ کمکی به ما نکرده‌اند، باید و در نهایت هزینه‌های ایالات متحده آمریکا را پس از پایان این درگیری بازپرداخت کنند.
🔹
ما این کار را بسیار بیشتر برای دیگران انجام می‌دهیم تا برای خودمان؛ کاری که نسل‌هاست انجام داده‌ایم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/689872" target="_blank">📅 20:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
معاون اول رئیس جمهور: درست است که با ایجاد محاصره اقتصادی مشکلاتی داریم، اما هیچ کالایی نیست که ما قادر نباشیم آن را وارد کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/689871" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7bb74a48.mp4?token=qa3ua0XKyvCXuK8tKb4jMzTl_CGUp6BrDO7SoYuhf0SXPuz9AqbrLdayYlerpDPFLncmTPfMDp1BKbJhsBnUPw67V5xUx760MhzYzdqC9Xkl1ZptpGW0nW4rhBOa31keaHohApvuZdssC6yaHvJYYekl_P6paxF0dOJCLrlMy6QxapYMqR-wJih9JA4HHF5_7-a5sSFZTLnIbq53lC8OD6NuWQEUZm0rwTP5lqCywgd3nJY7yHYlibTI8ZKREoxmz5mGzQghcno0aL_2g0lQN5cO9b7XMZPKvmz0a_a1CaP38OMc-PdVHj-M-y0vuTkBCZrMAGIBAP4ICqMeTpRG_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7bb74a48.mp4?token=qa3ua0XKyvCXuK8tKb4jMzTl_CGUp6BrDO7SoYuhf0SXPuz9AqbrLdayYlerpDPFLncmTPfMDp1BKbJhsBnUPw67V5xUx760MhzYzdqC9Xkl1ZptpGW0nW4rhBOa31keaHohApvuZdssC6yaHvJYYekl_P6paxF0dOJCLrlMy6QxapYMqR-wJih9JA4HHF5_7-a5sSFZTLnIbq53lC8OD6NuWQEUZm0rwTP5lqCywgd3nJY7yHYlibTI8ZKREoxmz5mGzQghcno0aL_2g0lQN5cO9b7XMZPKvmz0a_a1CaP38OMc-PdVHj-M-y0vuTkBCZrMAGIBAP4ICqMeTpRG_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی شبکه دولتی فرانسه از سیل مردمی ثبت‌نام کننده در پویش جان‌فدا
🔹
شبکه دولتی فرانسه اعلام کرد هر روز که می‌گذرد مردم ایران نسبت به آمریکا و اسرائیل بیشتر منزجر و حول حاکمیت بسیج می‌شوند؛ گواه آن آمار بیش از ۱۴ میلیونی پویش «جان‌فدا» است.
🔹
پویش جانفدا در پایان کار خود به بیش از ۳۰ میلیون داوطلب رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/689870" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1686da22.mp4?token=F6MZRDi9oDip0u1HwE-N2K6fgjBX3BHFv-H-XCl-hS_Uuf4QdaHTinre9Fv4P3NJ6YH5wThKXLZY0ARRSxa6OF3iWY1gymJa-EaAS3LAJrl4X2iFAxekm2ePyTSzcR3_AUjFErJPqvz6fvn3S0dhoDFF2DQ0OTbkY5u7Sd9XL2GxOi9ba5iTEFT912yRzRVVSfob64B-L94Xn_07EnJ6L3KBkwa5IyujCBo0b1I_aJOUydkCg1j8Xw2vnRbXZU0cnXpX7Dk2rv6r3bDRNCcMl25iKNAryumphsjh_SN5pykSnuFIv81c_526-JfGJbj8OrkvLBcYsudJq0p1iDKXpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1686da22.mp4?token=F6MZRDi9oDip0u1HwE-N2K6fgjBX3BHFv-H-XCl-hS_Uuf4QdaHTinre9Fv4P3NJ6YH5wThKXLZY0ARRSxa6OF3iWY1gymJa-EaAS3LAJrl4X2iFAxekm2ePyTSzcR3_AUjFErJPqvz6fvn3S0dhoDFF2DQ0OTbkY5u7Sd9XL2GxOi9ba5iTEFT912yRzRVVSfob64B-L94Xn_07EnJ6L3KBkwa5IyujCBo0b1I_aJOUydkCg1j8Xw2vnRbXZU0cnXpX7Dk2rv6r3bDRNCcMl25iKNAryumphsjh_SN5pykSnuFIv81c_526-JfGJbj8OrkvLBcYsudJq0p1iDKXpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سردار آزمون به تراکتور مردود اعلام شد
🔹
شباب‌الاهلی ۰-۰ تراکتور
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/689869" target="_blank">📅 19:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
کاتز علی الطاهر را منطقه امنیتی اسرائیل اعلام کرد   وزیر جنگ اسرائیل:
🔹
ارتفاعات علی الطاهر بخشی از منطقه موسوم به خط زرد و منطقه امنیتی اسرائیل در خاک لبنان است.
🔹
وزیر جنگ اسرائیل در تهدیدی اعلام کرد هر کسی که به این ارتفاعات نزدیک شود، نابود خواهد شد.…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/689868" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادامه دروغ‌های ترامپ درباره ایران
🔹
ایران خواهان برقراری توافقی است.ما تصمیم خواهیم گرفت که آیا در مذاکرات شرکت کنیم یا خیر، و این گزینه‌ای است که ما برای آن آماده‌ایم. #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/689867" target="_blank">📅 19:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5866e96a.mp4?token=Ze9b3wdC9-Ka8VfXdezCBchtCjDj2DyS9YUgf1zK2mawkxBnmKkEHC94cptdnjlEfVsOrrfAjDTHHdejnrvT9X06HT4j74F0cvpKOXu1FbXDVavd2D8zEmlI5Zf4ZXMj0R48_o1qjRa2e5Q9alOhMJpbpv0I6SB42Ytv0lh-xO3s3_zh_9DoAoYJ6TJnchRM2Ybznp-Sk7mtLhjMoCOVt_prbs3dagcoM3RPyeW6QJbeC4lUGWL9ukXEAmOFqPkkM3C-oXKypUqImM-CpTYawukcfgTJG68dDxRyjRT-bo2nXEnuK_gJ9WKB5upnmw39l8fc3aiQC-bGksCX1mtjjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5866e96a.mp4?token=Ze9b3wdC9-Ka8VfXdezCBchtCjDj2DyS9YUgf1zK2mawkxBnmKkEHC94cptdnjlEfVsOrrfAjDTHHdejnrvT9X06HT4j74F0cvpKOXu1FbXDVavd2D8zEmlI5Zf4ZXMj0R48_o1qjRa2e5Q9alOhMJpbpv0I6SB42Ytv0lh-xO3s3_zh_9DoAoYJ6TJnchRM2Ybznp-Sk7mtLhjMoCOVt_prbs3dagcoM3RPyeW6QJbeC4lUGWL9ukXEAmOFqPkkM3C-oXKypUqImM-CpTYawukcfgTJG68dDxRyjRT-bo2nXEnuK_gJ9WKB5upnmw39l8fc3aiQC-bGksCX1mtjjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سردار آزمون به تراکتور مردود اعلام شد
🔹
شباب‌الاهلی ۰-۰ تراکتور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/689866" target="_blank">📅 19:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuiKNSMh5SrKrSew5TXCJBzAD73glTbrBfLkh67FLlZI66cHahw0rLMSGo55Zsl0uKCRi-HJSvygvQVzub10h77-E5zvAQzsmlP4VEyvdYTjrZNAdZP6fXnHQg0cMScCSJzN5HnAbLMeXeFKTFl4YJhzaMiGIADHwoNe5HMIrNbfYCzX8kJBqovoGsoYSleQ_LD5XyHwgQvWtzoJ3qXDxGBnpYuLypGBkg35MDuKKAAS-YO31lEHW_SloYEY1isca54UdhmSug2qJB8oLK6qJVdgtReA3QHm9lYMC2QQvKQaJbSxaxq_mxT0-cz-eVPOfWUIngMWU7zoQ2_DOg5OMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه دروغ‌های ترامپ درباره ایران
🔹
ایران خواهان برقراری توافقی است.ما تصمیم خواهیم گرفت که آیا در مذاکرات شرکت کنیم یا خیر، و این گزینه‌ای است که ما برای آن آماده‌ایم. #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/689865" target="_blank">📅 19:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21be550df.mp4?token=AK7En1kVBI9UoQ3yfHlUSoAIivZ0l43ZgP36KOTqUh0tkNgsEToricCa7V2Jkpus4pndWwjRkoF4-halJfDnUVLCzo8GuO2mDYLSrmTt_7-yhVCRkTo4xcUbSaAWZehsN9y4qiyCyDOkjqLJaSRsrzAediJcEzEws_NRnf9sHcESXUGvQyqYaa6z0iVKSJpXYWz_GleRcS1EzkO9X79XCrGshUq8c-Cfat5bR9Roc7XaWzM35iSTmxsjmE4E8OuyFtzAWQz6vyMy66emzkZgFOptXAfaDZJqySUm6KXEV2ENN9rWbNs4DyS2MfiVjDt8DUKUK7KAubLum_O6LeeLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21be550df.mp4?token=AK7En1kVBI9UoQ3yfHlUSoAIivZ0l43ZgP36KOTqUh0tkNgsEToricCa7V2Jkpus4pndWwjRkoF4-halJfDnUVLCzo8GuO2mDYLSrmTt_7-yhVCRkTo4xcUbSaAWZehsN9y4qiyCyDOkjqLJaSRsrzAediJcEzEws_NRnf9sHcESXUGvQyqYaa6z0iVKSJpXYWz_GleRcS1EzkO9X79XCrGshUq8c-Cfat5bR9Roc7XaWzM35iSTmxsjmE4E8OuyFtzAWQz6vyMy66emzkZgFOptXAfaDZJqySUm6KXEV2ENN9rWbNs4DyS2MfiVjDt8DUKUK7KAubLum_O6LeeLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره پوتین؛ رئیس‌جمهور روسیه به کمپین جانفدا که در یک هفته میلیونی شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/689864" target="_blank">📅 19:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d086fa17.mp4?token=u1bCOKzX04bk8SyMTyWbIbkzTuDZFH9AexZGt0bDIjDMgkm1tgCePGGvS1ZFvjvahoqGLPpKZFLyvKEnvRaI8UsvmQg4aUiWSAM6kXnxi8fupXOqoCgRt87BV01iOJ5Yq-NmkNiTUZL-cSzLMgxTxpSyMs6n9rPsKJnRYBJg-zg04yBCRpJyXAKO9sLltqvGfmcvZVu9_yChNntoXNQbtztM6joSCF5LWlvYo9Zu0gOwZhpSprpuK0KmffrTpI1nMM3LgVwryZrSuy5BP-yulY97GCx23HQU8Yhyh0HsUyXMK0xyEl8ClDFFmmiiQyNSj-kH0fy7vHJ1CrStIVeGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d086fa17.mp4?token=u1bCOKzX04bk8SyMTyWbIbkzTuDZFH9AexZGt0bDIjDMgkm1tgCePGGvS1ZFvjvahoqGLPpKZFLyvKEnvRaI8UsvmQg4aUiWSAM6kXnxi8fupXOqoCgRt87BV01iOJ5Yq-NmkNiTUZL-cSzLMgxTxpSyMs6n9rPsKJnRYBJg-zg04yBCRpJyXAKO9sLltqvGfmcvZVu9_yChNntoXNQbtztM6joSCF5LWlvYo9Zu0gOwZhpSprpuK0KmffrTpI1nMM3LgVwryZrSuy5BP-yulY97GCx23HQU8Yhyh0HsUyXMK0xyEl8ClDFFmmiiQyNSj-kH0fy7vHJ1CrStIVeGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتباط با فرشتگان؛ حقیقتی پنهان یا بازاری برای فریب؟
🔹
پاسخ صریح به مدعیانی که برای اتصال با عالم غیب، قیمت تعیین می‌کنند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689863" target="_blank">📅 19:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ترور عالم اهل سنت در زاهدان
🔹
مولوی یوسف گرگیج، از علمای انقلابی اهل سنت و بلوچ زاهدان، توسط مزدوران صهیونیست مقابل درب منزلش، به شهادت رسید.
🔹
اخبار تکمیلی متعاقبا منتشر خواهد شد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689862" target="_blank">📅 19:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POTs39HfUNXLTCiyXhYDJathsv5jlreC6a1RtdSSFgdrp1_5sCR8bwynBKMOATWn3HE4ocRpzAaLsNL714hpb7Iv2s0bxL5dHalt0Okrf6jiTKzgVn8cSfl669rJDGVq0Xpb7peW3FZUc2HyUB0ma5jQgpMhyg2OdVQ8nnUpZXdIeg3YlwfxnRz_u74Wk4Rcm18-RUCx1gv5titWtzhGS4T0k-e82NLYe7NdxuwNRDMUp4sUOdbUmmrvCjN-gn1EswmkyHW3fozv2JGh2Pj-jEdSsshEd_lTJxjdAxPQ7dHkAgeasjbwvIMJ-vUHS8wWVbJINE3xlTWmXmEVubIhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران یک‌پنجم رأی‌دهندگان به ترامپ را پشیمان کرد
🔹
نتایج یک نظرسنجی تازه از سوی مؤسسه «نویگیتور» نشان می‌دهد حدود ۲۰ درصد از رأی‌دهندگان ترامپ در انتخابات ۲۰۲۴، از رأی خود پشیمان شده‌اند.
🔹
۴۵ درصد از افراد پشیمان، جنگ با ایران را مهم‌ترین علت پشیمانی…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/689861" target="_blank">📅 19:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
خرید اعتباری بدون سود و کارمزد/ ماموریت تارا: هر ایرانی یک اعتبار
تارا
آرین افشار، مدیر ارشد رشد تارا در
#گفتگو
با خبرفوری:
🔹
«تارا به عنوان پلتفرمی که راهکار پرداخت اعتباری است، خدمات متفاوتی به مشتریان خود ارائه می‌دهد؛ یکی از خدمات ما ارائه وام بدون هیچ دردسری، بدون حضور در محل و تنها با انتخاب چند کلیک است.»
🔹
«اعتبار تفاوت عمده‌ای با وام دارد؛ بدون هیچ سود، بدون پرداخت هیچ کارمزدی و بدون هیچ پیش‌پرداختی می‌توانید خرید خود را با دو تا سه قسط انجام دهید.»
🔹
«امیدواریم هر ایرانی یک اعتبار تارا داشته باشد تا به پشتوانه تامین مالی ما، در شرایط مطلوب و شرایط بحرانی امکان خرید داشته باشد.»
🔹
«کمپین «به اعتبار تارا» از یک خرد جمعی شکل گرفت؛ تلاش کردیم مسئله را ساده کنیم؛ زمانی که در محل پرداخت حاضر می‌شوید، اعلام می‌کنید با تارا پرداخت می‌کنم و در واقع با اعتبار تارا پرداخت انجام می‌شود.»
tara360.org/nuk
مشروح خبر
khabarfoori.com/fa/tiny/news-3245179
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/689860" target="_blank">📅 19:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38061763f5.mp4?token=VSCgcva9KUMn2_gGFqCyoVnjSYFTklvv3Lpyqa_WLmvhHuMyzBXL0M3qlGG548UkvuRuOMh-yd4rZju5z0Q-3_u2RCjl9XSKuGnlZbJqqjfgLsnSeCstk8cObmhoF2mXuFiirta65gNces3AVliDVFtEYxW65ffsxJKWjkIHdFajJ_9PP9Px9EpuASHPtKlSYeQn5O1cGyEIKJrE7AgZG4xDRPCENcZRyuCUXYAJvuqg-hmJOKSZZml1wb57zYbZincePg4FpDnVuv5xpzMAN1RC1vNrgm1xe8HhLZx3-gS92EKiI35RDqJ11qJQ9bEwRTGbmJ5FVWapIcY_irsopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38061763f5.mp4?token=VSCgcva9KUMn2_gGFqCyoVnjSYFTklvv3Lpyqa_WLmvhHuMyzBXL0M3qlGG548UkvuRuOMh-yd4rZju5z0Q-3_u2RCjl9XSKuGnlZbJqqjfgLsnSeCstk8cObmhoF2mXuFiirta65gNces3AVliDVFtEYxW65ffsxJKWjkIHdFajJ_9PP9Px9EpuASHPtKlSYeQn5O1cGyEIKJrE7AgZG4xDRPCENcZRyuCUXYAJvuqg-hmJOKSZZml1wb57zYbZincePg4FpDnVuv5xpzMAN1RC1vNrgm1xe8HhLZx3-gS92EKiI35RDqJ11qJQ9bEwRTGbmJ5FVWapIcY_irsopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقت میلی‌متری ربات جراح در عمل مغز
🔹
ربات‌های جراحی باید کنترل بسیار دقیقی روی حرکات خود داشته باشند؛ چراکه یک حرکت کوچک می‌تواند به ساختارهای حساس و حیاتی مغز آسیب بزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/689859" target="_blank">📅 19:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMG1wb20IeguBhoctrSaSFAQR2JCkjJ-ily28xxDzZ8fdr_mCDHrQOIEUR7l--h_F_7EZsj1jR9gH5OLB2zwui1WxCKB_MjCSflnG9RBRq71z4OWTENqIhpXIFQFG8NPdBh3ZKnUkdACtYex1TMYD02z63v8CN6zX0H2KPSKwImLyH5zV-ZNWR8j0SQY5Cxl-hRhRqdZfRipzcS-r0RLnrbdp3ww6l6HI-cv5xO3TuMu7HPm5E8kAiFk_XLaWG6jVhHMN62U3EnYCw6vGoqIOyClFhxGNHggibhpJBoqPFTTszTdVa6jdgkJXMXocd6AVMfvBi78_qQBB3aJopPboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: ترامپ به ولیعهد عربستان سعودی، بن سلمان گفت مسئله شما با ایران به ما ربطی نداره و خودتان باید مشکل را حل کنید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/689858" target="_blank">📅 19:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم/ هر تصمیمی که قانون بگیرد، مطیع آن هستم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/689856" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
الگوگیری عربستان از آمریکا؛ حمله ارتش سعوی به پلی در تعز یمن
🔹
شبکه المسیره یمن از حمله هوایی عربستان سعودی به یک پل در شهرستان مقبنه در استان تعز یمن خبر داد.
🔹
گزارش‌های اولیه از وقوع تلفات و زخمی شدن تعدادی از شهروندان یمنی در پی این حمله خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/689855" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw5-w23it_ppiNz31IsECE_Xqb3vPWwyKFIyaN6xGg8zso_bHKanfall6f1Xhn6N7oRJ1sxW_A2aJy3aZM8XsLebLKlBjArcsWYpx6NC8xKbSFSY38CpvWrCdoOX8vCdaCryOlZrwDU9oirUfzUCdNDnGBVAJxnWtUvl88ZjN9nB0JWCStSqu1WMDDL07QDdHLWrTd6DZE2n1AvbgZ4qEdgLzp5MNDMcOWYTOLEUIY5wqk8mEOxoTPJ8kVO4uSwbZw3inaNCjXo_PGO7LQ-KGcu0uqM88tCj8EWwyBE_Mx8tz3M3I8CoDcBj5otbinGgciS_89yx0V0zl7fwZAO07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه دروغ‌های ترامپ درباره ایران
🔹
ایران خواهان برقراری توافقی است.ما تصمیم خواهیم گرفت که آیا در مذاکرات شرکت کنیم یا خیر، و این گزینه‌ای است که ما برای آن آماده‌ایم.
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/689854" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689853">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fdabcb757.mp4?token=qqVwAEfrzsI6xkYqkQ75QGnMHog6DaszuPZggCMSQ-o9Xfh6Fn13k_SiS20y3058oX0266NILlTaG5gcl4OT52yZF9XvTy4zt4FV5hcolIyg7hRAMncptACtVrME4wmT-P_2u1KDt-R2ZClhqZY3kKDPzHVgNq8sKkUos2ktcf9Wuv4Ae_njFDu-OSurM5MBznnSUMSOxXznxHsQsJvrY7kt8I4l1pqT4gla4JEUokdGsFO6aEuU20wZuWtymRHb6QEjRt3IIjqF8itEVFhQcj7K68GenhOKRO65L-Wui331NZTJi3NWGHKpuj1_JQ9F0flNhIYGgU9zfh87qH3jSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fdabcb757.mp4?token=qqVwAEfrzsI6xkYqkQ75QGnMHog6DaszuPZggCMSQ-o9Xfh6Fn13k_SiS20y3058oX0266NILlTaG5gcl4OT52yZF9XvTy4zt4FV5hcolIyg7hRAMncptACtVrME4wmT-P_2u1KDt-R2ZClhqZY3kKDPzHVgNq8sKkUos2ktcf9Wuv4Ae_njFDu-OSurM5MBznnSUMSOxXznxHsQsJvrY7kt8I4l1pqT4gla4JEUokdGsFO6aEuU20wZuWtymRHb6QEjRt3IIjqF8itEVFhQcj7K68GenhOKRO65L-Wui331NZTJi3NWGHKpuj1_JQ9F0flNhIYGgU9zfh87qH3jSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تام، اسبی که برای فرار از سواری نقش مرده‌ها را بازی می‌کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/689853" target="_blank">📅 19:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689852">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpyntKfrjlVulgF6QJyCABFeBGOxVeAxWOHSJOmwB6wGIOm5Bm5tS42Wep1L-z6I2kWG24Gs0uk6NVXcK-EqdrEsgw5y99DN91vzx_Z2wG8kO5HhvJvsdRKdMZUV2CsFE-LiVau9nf5EFQ01RBw_kADKBxP6T8J9YaoaQFmlYvRBwQj6FG8XcRQT8P_LWQd4QwF1hdapiSJGcw__dmyTTDKTuRMuCL9KYBc6Wu0484CVQigOlnN3FQ_BHU84pC9VMH_fUYgyTc2H2Oc_8Q6PqD6b82earz6hxqzIBe5dP6Gohno-XO3LSrtfcwyCNdu6rSyuoMlBdvFc9qWhfbssIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
می‌خوای فروشگاهت رو به اکوسیستم اسنپ وصل کنی؟
اونم با کمترین هزینه؟
📱
وقت خرید
کارتخوان هوشمند اسنپ در ۴ قسطه
!
🧮
سوپرپوز اسنپ‌بارکد یه کارتخوان اندروید همه‌کاره‌ست که هم مدیریت صندوق و موجودی رو برات انجام می‌ده، هم با گزارش‌ها و تحلیل‌های دقیق، بهت کمک می‌کنه سود مغازه‌ت رو بیشتر کنی.
🛵
جدا از اون، خیلی راحت می‌تونی فروشگاهت رو به سرویس‌هایی مثل اسنپ‌مارکت، اسنپ‌باکس و اسنپ‌پی متصل کنی.
🔻
برای خرید کارتخوان هوشمند اسنپ
در ۴ قسط
،
فرم زیر رو پر کن تا برای مشاوره رایگان، باهات تماس بگیریم
👇
https://forms.gle/Qocxzh4fAUzcwvvw9
📞
تماس با ما: 02196621424
🌐
وبسایت اسنپ بارکد
📤
کانال:
@snappbarcode</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/689852" target="_blank">📅 19:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689851">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PedburwdGE0XjynLHh7xJx8BNh_OTiRmS0iMrcYAWLNw8s6qnTwJqnHrEQ9UMFMLMP4q8pcHa5iKxjUe30xiK_5WbQCilJtp5P3UEgbH0vPkcWdKc9y1oXYI2nCrL0Y9r1wCb8wuvisggNLaUvz1h3EmPsvEIk7axXAMWPZbrIgLORX0ArEFTK6k7rf07mL7rIlvqcSn2f1OfV2gZ3OpQXy8992LsCkLei6cgU6SFnSKV-xKheax06JWlbHU0tHCx5mq5kdgT93WUzgskTAhL74dPAMr33WE0sFpzn6YX-M_AZJyP2uaOo1x0w1bzm2gnKCPNJWm4X6Y_MlIzuPsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
خبر خوب کیش‌ایر برای کیشوندان/ ۲۰ درصد از مبلغ بلیط را میهمان ما باشید
🔹
به گزارش روابط عمومی و امور بین‌الملل هواپیمایی کیش، در پی بازگشایی فرودگاه بین‌المللی کیش و ازسرگیری پروازها، شرکت هواپیمایی کیش، به عنوان ایرلاین سازمان منطقه آزاد کیش و با حمایت این سازمان، در راستای ارائه خدمات و تسهیلات ویژه به کیشوندان گرامی، از تاریخ جمعه ۱۴۰۵/۰۴/۰۵ طرح تخفیف ۲۰ درصدی خرید بلیط در تمامی مسیرهای رفت و برگشت به جزیره کیش را برای دارندگان کارت کیشوندی اجرا می‌کند.
🔹
بر اساس این طرح، کیشوندان محترم می‌توانند از تخفیف ویژه پروازهای کیش ایر در تمامی مسیرهای منتهی به جزیره کیش و بالعکس بهره‌مند شوند.
🔹
استفاده از این تخفیف صرفاً از طریق دفاتر فروش مستقیم هواپیمایی کیش در تهران و جزیره کیش امکان‌پذیر است و خرید از سایر درگاه‌های فروش شامل این طرح نخواهد شد.
📱
@KishAir
🆔
instagram.com/kishairofficial
🌐
www.kishairlines.ir</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/689851" target="_blank">📅 19:00 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
