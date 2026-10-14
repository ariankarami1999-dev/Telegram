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
<img src="https://cdn4.telesco.pe/file/OYaIccYs0HSHe5SSD53UpqP8HJRc9wkRTxmLFn31LydC5j1VwvIeP5G5DrhN50cI8hv2L6jHcTlA4DpS3uxodHj6Nx-m-7jMup7LxaIO470jiSnfdovbP5rfU5cYQ437IocM66Fk1_URFO_qsufMJ7mozGS5i429LWL8CfuTC91uSQuDlbPicOZd6uaRef5KDaJN-eP9U820uKsPXBcAu6WIq7sWlSBGPJQa2GGS3Kt0H-dOWhd7vgrJwlaBMQJDxJ5IRqlkKJHsnFzN75HgORBcmpNSJXsWnTezQKIoDNrXnIscWn4uHW-225dTeiY4zAM9gLdtKICGM-a4ZMHwvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-152568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس ابری ProNet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzkwUNNo8MzFDPNpQGvUKzegIfGh-r8pX6pFKsAchOPl3xpKfBcVvRbjeFr7P3rz2cOTKY7O5NBNSFMm6lroIjYxSDODhly6rORvGRpGNZkN_WsLGuAfDLTOYE51qqln8OvBrGPTxxOXyAMyZAJ9GmExE3wDvEHEuSWwH4tUvkUVLi4sSSZ55jYfs_uHqhGkns4ZwNiuKs0-Z4_6NYUkXztKPa8AjYEtYpeLLr-EYrFPcX7gyBYFNsJUa-turRLAC-J5U9cOWmgyY1yCJcZKh66THZyeVv5sh5V2IuSpo4yvk_TO7cQr-IG9jr4yLhdWhtBnHmsIf998yA65H6i7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین فیلترشکن پرداخت به ازای مصرف ایران
🌎
پرلوکیشن‌ترین سرویس ایران
🌎
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🔴
دسترسی 75 سرور با خرید یک اشتراک
🔵
قوی‌ترین تیم پشتیبانی 24 ساعته
🔴
مناسب برای تمامی اپراتورها
🔵
سرورهای ترافیک نیم‌بها
🔴
سرورهای ویژه زمان اختلال و محدودیت
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دریافت مستقیم اکانت تست
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🟢
مینی اپ حرفه‌ای مدیریت اکانت‌ها
🟢
اشتراک فیلیمو فیلم‌نت رایگان
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/152568" target="_blank">📅 01:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گویا بخاطر تسویه دیر به دیر دولت با فروشندگان، خیلی از فروشگاه‌ها دیگه کالابرگ ارائه نمیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/152567" target="_blank">📅 01:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e211b84.mp4?token=S09s7F-LjFKlzNRqN8kswAKcCHZqL4lq-UHhWIj20gl0RJTPcsem-i0woOK4yW5pmXscVL5U53q5Fvsx3LDc77MfkLS31jTknYqYnAOC3BzqYQfZhnYH2QS-Wd9iLuhjqVlJsNjOYzESYHnlub28edC7OTrI3SS2lvi58U6HlDR86CPayYKgU1gWz-JiOpNRxKP4BXl-hBrzZnAPvZITNeR3YiVB3nyAtmseLHxRF0oafoBM1wPjssNQuiv3eB8NjAJRdp9hjhyL_lRU4fSLSJfMHWMvyNUm_ly5yCLyXMb2xhAWDBo2vx1_Di9_kxr5LfFOwLLdlTFN6sfMvnLL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e211b84.mp4?token=S09s7F-LjFKlzNRqN8kswAKcCHZqL4lq-UHhWIj20gl0RJTPcsem-i0woOK4yW5pmXscVL5U53q5Fvsx3LDc77MfkLS31jTknYqYnAOC3BzqYQfZhnYH2QS-Wd9iLuhjqVlJsNjOYzESYHnlub28edC7OTrI3SS2lvi58U6HlDR86CPayYKgU1gWz-JiOpNRxKP4BXl-hBrzZnAPvZITNeR3YiVB3nyAtmseLHxRF0oafoBM1wPjssNQuiv3eB8NjAJRdp9hjhyL_lRU4fSLSJfMHWMvyNUm_ly5yCLyXMb2xhAWDBo2vx1_Di9_kxr5LfFOwLLdlTFN6sfMvnLL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی بالأخره دادگاهی شد
🔴
امشب تو یکی از تجمعات شبانه، سه نفر از حاضرین نقشِ "قاضی، دادستان و حسن روحانی" رو بازی کردن و اینجوری حسن روحانیِ الکی رو وسط خیابون محاکمه کردن.
#توهم
#تریاک
#کصخول
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/152566" target="_blank">📅 01:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZyc2EHQCs8VDRfCwF368V2T8P6R8OacdILVAJ_QHNFAlxCDTKfajosisOyyup_kDYGRb76s2lJnWIi_s9Ts78qvKqY09ncitRYHKOhVWnI3CRYUwRPjWf1Q0-b3TuQFsHLRf_QkiAqCHwt_9jOpyfm9A0wn0gFdwk8yz6npOvCF8Q3yLJCQPtPv1SeW3hG70_OQW0z8PZep8BVBJwybcAfSMAwTQ-hT0AbEp2EwgO716kOZjFUcmVk-PaMJB6Wn6Y1tr5S5rTCjL7vtFdM-vwH33x_GKlpjU7j2hidQn34_36GaQDUWGQDG16lkzinvwfd8QjnRIIttwEICl8d08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:حاضرم تمام افتخاراتم رو بدم اما ۱دقیقه جای ملت مبعوث شده تو خیابون باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/alonews/152564" target="_blank">📅 01:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/152563" target="_blank">📅 01:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش‌ها از افزایش پروازهای ترابری به اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/152562" target="_blank">📅 01:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-X6akOu5V3uBMDEZObfBgoW_0aPgUB-ZxGaw0eDfC42U4YysPthTvM1AahaUsUiThjfzhVR-jfH9KAL-2oLbVFhmlGi4YWnH5Uo7YITaLX8hZWY5OrJ0xJA83HmgvWO8b5zz7wSaVXqST5UrZAzUvWsEibcB4ybX1PgT3dlePgrHSDLd5PVFMojZ9bt9wt_eaeytAU9fl3l-jbOJoLyeDmo0NXyIo-rOt-qmncXyiLIMTGeVccDS34ja5xB4PNRkI_vs6HiGZ15LOTLWkdLBQIKTCs7rQVRNiNZjVoj971GwuxSMv4m9m5XQdGX7rbpEkKuEu-tMRR4Eyrb_KAG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازگشت ناوگروه ضربت جرج بوش به دریای عرب
🔴
بر اساس گزارش منتشرشده از سوی USNI News، ناوگروه ضربت شماره ۱۰ نیروی دریایی آمریکا، به فرماندهی ناو هواپیمابر «یو‌اس‌اس جرج بوش» (CVN-77)، پس از توقف در تایلند به دریای عرب بازگشته است.
🔴
این تحولات در حالی گزارش می‌شود که پیش‌تر نیز خبرهایی درباره حضور ناو هواپیمابر جرج واشینگتن و حرکت احتمالی ناو تئودور روزولت به سمت منطقه منتشر شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/alonews/152561" target="_blank">📅 01:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q80XWH4sVChrVF7kHGbVK9s4IYc7XQY43FEMs3S8fsHn775KI3W3AheFl9hcfhJe333hMFQZgUxXqXPXzIdgv99kp9kxuYvz591R5fnJF9JlRDDeoP6gEM8eEelWgjEJwehTS1-0NnlnhwZjMvjO_GPVq4EjRNUyNe0lUyCHKTfL3CwUD5yGKqpaMNbhKxVX9DfNIZaGmEYKpGVQEj9wmgzvnZug0AZVVaS7H8ANoQaPg2RNYaXTwYArCxdjZPETXhi5zIBPjI_U4Dgp6PU1gf9FsYFFWF3i4kCOAlq4hfxp8I2s5WzXD47L9-TxlPBtP431jZWCiulS39FK9NrJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۲۲ مهرماه تولد ۸۸سالگی فرح پهلوی، همسر محمدرضا شاه و ملکه اسبق ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/152560" target="_blank">📅 00:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-plMo4uXJJpdZmGhIcdv-xb80z-HILxkvoaAxUrZN2uJkr_VAsIc6fCt86J8q7zv9tJ91WTMbGpRhy9s-g9uuYfAwewDGQ68AVx43C3ZjsAk4zBBGaWGYsfUKLNEdhM12RE8AUqVVHjf8H8vfOEOV2RCck8om3YLddG03kW-k00GHHjaZA9JpuHkD4oYsX9zpGL6td7dTQICioOSpiUlmvF985RCT46pKhjw9xNcKDbrdUk7Q65m6g1Z-WXGL_DgpLi_vwx22yBNlUSO_crTDQRiJb8WYPoVCB753rWWliPslOxqxPcdqmOc3g-HYl2xgTLkKOTnXIs1nqMt9NA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید:
در جلسات اخیر با سران امنیتی و اطلاعاتی، نتانیاهو ادعا کرد که این ترامپ بود، نه او، که بحث درباره احتمال حمله به ایران پیش از انتخابات را آغاز کرد
بر اساس این روایت، ترامپ از نتانیاهو پرسید که آیا اسرائیل به آن ملحق خواهد شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/152559" target="_blank">📅 00:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfzEGEXiOH-he1s4Q_TQIOyJqeNOCAC52WT_vXqqaZOCxtv4UDM0wa9p3q9Rao4LpmLnhBBUIwmpkt8304r2P76BXEULwKAaEigdTrZBbQ6Z-eGCKwbo27B5JD-GNnQBaVpCV3kcL5Iu6gJKbSUh6yL_SpsXYXc823DvIXwdPKwU7VFTjjwtJyHznVV-RfeYWxqXZ0SW0xgoushtmqWCnLf93MINmUnRMGK-DzE25j4-FwgcDRg1AadIuHYg2egCPhcOHfUv9TqHm77qn0-uMZeMZ7RJaam_BlQKOxbPiUwPkmKI5snx4uiDOg-gDLJ9lYerlgu197aLv1dEaUE3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع آمریکایی:
هگست شدیدا به دنبال حمله به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/152558" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fT3I-KgVyvr9LaO2eGBRBiFGe5KleoCHT2q58857D9BI9_6dhtuiR_ucQD6C2eyDyvyve10QIu6qR3WyMNsjDD_e82VcCve75VFYbmkQITtB9A7gL9IFHNeeNK376lQ8CUu4AuY0dzP5-hQ0okKIHrg1KOt_VeLo6RS8tJuubqjkgBem8qZ61GoXgMJ_CZy5fSPABZTBCEUUloSzknJNKDQd6JpXQUqZaSBUuKAHOcYY8gd7NBOiFH-axKRlueykdHGFJlzCXC1wtgyV4XYhLeoYdXSuslXxHrtzAMfHyGDIpBuGH3AKFGlVlnZl6q1rf89wbxvfXSLF_SAnhXd8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در روزهای اخیر، شاهد فعالیت‌های نظامی غیرمعمولی از سوی نیروی هوایی اسرائیل بر فراز سوریه و عراق هستیم که یادآورِ وقایعِ پیش از ۹ اسفند ۱۴۰۴ و حمله مشترک آمریکا/اسرائیل است؛ امشب هم دقایقی پیش و برای سومین روز متوالی ساکنان کرانه باختری و منطقه گلیل/الجلیل از فعالیت شدید جنگنده‌ها اسرائیلی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/152557" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل:
فعالیت‌های اتمی در ایران رصد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/152556" target="_blank">📅 00:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
فوووووووری/لیبرمن: جنگ ویرانگر طی ۷۲ساعت آتی آغاز خواهد شد
🌎
@ForioNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/152555" target="_blank">📅 00:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=FXVw_xmnXDVzI21axvgPTKuDZFwKTyer-w5fCqg9kPrSCu35ZQ8UXQ0IPEY2f1dOu7BC9NL1lLwGvHzA_ciKKmXn_QA-B7FsTCdIiLrph4t7-f-BVHaLx3uxsA1sd27ybH0X9w3McEHM9BsXQC9HVvozhYsQNVIDRFehhQ9JDdA9MzfmQ260CI-_-J6ad1UI79LzFtWsqIeloUt2kS4HAdJRypUpmVudvDfWVbppViooDavMDZ0P_BefnQUvs2KHlAOclB9vWLtmz9RbenHfeiRC2T_cHVEZZokAvTc8NMDa5i_VzYsj0SHVXKeb_xD6oL0Gcen-AvWr9G5P2XsvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=FXVw_xmnXDVzI21axvgPTKuDZFwKTyer-w5fCqg9kPrSCu35ZQ8UXQ0IPEY2f1dOu7BC9NL1lLwGvHzA_ciKKmXn_QA-B7FsTCdIiLrph4t7-f-BVHaLx3uxsA1sd27ybH0X9w3McEHM9BsXQC9HVvozhYsQNVIDRFehhQ9JDdA9MzfmQ260CI-_-J6ad1UI79LzFtWsqIeloUt2kS4HAdJRypUpmVudvDfWVbppViooDavMDZ0P_BefnQUvs2KHlAOclB9vWLtmz9RbenHfeiRC2T_cHVEZZokAvTc8NMDa5i_VzYsj0SHVXKeb_xD6oL0Gcen-AvWr9G5P2XsvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود
🔴
نتانیاهو بدون جنگ باید به زندان برود، برای همین چه با ترامپ و چه بدون ترامپ، جنگ را شروع میکند!
🔴
برای زدن زیرساخت‌های ایران ۳ روز برنامه ریختن، با این‌کار نتانیاهو انتخابات را به تأخیر میندازه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/152554" target="_blank">📅 00:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITOQ--UnimtIWuUF5fQVUaSsyxkVjuLZs-tKpDkyr2lELX6RieQRNr1Ry02g6P_AAKS8zAsZNHpa4y1PLAe09rlMnVmmZX_LSQL6Nmw5gyFvR_hJV_ICaQ0gwTmbT8BCMRYRangyt52AK6JmxcoqCEmo4PqZksvn60BcuLEc1LOeKz79KtJYoy5DMtnWn1OzyQM9cq2XVtV5GFZYAkFT259bElCqZQMvFuYWKB1p0pOQMGzccWozEOqr6ysA5Qwh_iiGERKeAN2p0usXKwscsNoG6Ku0I9gCOwT9FBwO9Lcq_ZN53qu-RgpkrWI6CPO4vzOeeQmhZZ945ZT0YYFrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آغاز استفاده صداوسیما از نام «دریای کاسپین» برای دریای خزر
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/152553" target="_blank">📅 00:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / گاردین: گزارش هایی وجود دارد مبنی بر اینکه ایران فعالیت‌های غنی‌سازی اورانیوم را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/152552" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
یک مقام کاخ سفید به الجزیره: اطلاعات مربوط به احتمال حمله آمریکا به ایران پیش از انتخابات میان‌دوره‌ای صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/152551" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqVocZK8HaxU8BXBFqccCCKsV7d5-JgZWfTdnbYxrS6yU0RimHoRNUmteNp0idKjF_KUi2cuks7rsHL5z3tFoXHrHvvZCzoENErEQll_W_jKXEnZ6cy5IuPr89lKLQg_z7IeTJN6a7jiMyqEGW0lwscnjqtDTQi7VJKY1t07rCvmX_uZnBN-ZgKxNDWCm2i8fWaZUa8z_Z09H03WVYTI7JJpBbIf1WgC20-er8NsspIW2dqeJMRH6iTO4k87ROHIifMAWDxD8BNq_Cl5t5IMCjL1JV10EH3WMg0zTDFWGppolj8Az-wHRPk8FWvo22YgMtsU0Wc3G6JWUiUnc_iTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی دزفول چند تا دزد 6 تا بز اصیل افسانه‌ای ایرانی رو از باغ وحش دزدیدن. این بزها خیلی نادر هستن و قیمت بسیار بالایی دارن دزدا‌ رو دستگیر کردن گفتن یکیش نیست دزدا هم اعتراف کردن و گفتن یکیشو کباب کردیم و خوردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/152550" target="_blank">📅 23:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری رویترز، به نقل از یک منبع آگاه، گزارش داد که ساختمان مرکزی شرکت نفتی سعودی آرامکو در شهر ذهران، امشب مورد اصابت قرار گرفته است. این منبع افزود که هنوز مشخص نیست آیا ساختمان مستقیماً مورد اصابت قرار گرفته است یا اینکه خسارت ناشی از سقوط آوار بوده است.
🔴
به کارمندان شرکت آرامکو دستور داده شده بود که روز چهارشنبه از خانه کار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/152549" target="_blank">📅 23:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
لحظاتی پیش سازمان عملیات تجارت دریایی بریتانیا از حمله موشکی ایران به یک کشتی باری در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/152548" target="_blank">📅 23:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxCUWUuc5xBhgjn2BBQNUDHV3hcPqgykdEgwiS_lqD4zCcAjlEdBBETLfAYF-xaDMoSe42sGDfXRJ6ICwmpPXjXg3NieBopAkWgq-gGzGrimPdUC_477psXGotS-ilEwL8iNV7Qptyon9ttAAdTmTajJFDbMibvzV8ypVUDQaEsXDilO3ZdJ5bJ0YpCOvJhYmE3I6bIrF_sZg3EhR1SyFUA-w_BR7ZZHa_oNKVSZfKZVLiDsk0yQNJKx61u1t-rZmpA60U5jrazJi2tcPKk6a7L_P-F1goJ0VyE6nVf98Y79FUp3NUnm2CteoXH217xeRcLDOQpTCSa-aMREDPaxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی مدعی شدند دفتر مرکزی آرامکو در ظهران در آتش سوخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/152547" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
👈
دفتر نتانیاهو، اخباری را که نتانیاهو ترامپ را برای حمله به ایران قبل از انتخابات تحت فشار قرار داده، تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/152546" target="_blank">📅 23:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVlqcf45Cd52ljXQfWovxp8D5x2KiMWbrPNw_dv6XzVYKwxaPGuqCSXgbjs7IRXigOJhtR6qJQYiI0q9a3a2nMwztGhRcdiTlgw2dkmYXJWDSUytt0XQL9ssQX2z4aATNj5aMGMdev3KQ0zq0EEXvHZq3eO3iahGquPntMkOPT42mD63q8KB8OW_NOh4gsB-z8gjScRCYBUCLLHiQBKp63O35ObxFt2F0ic5dU9NzVEooOp9QIhmLH6TMXTqjpMYqkRDRdL3ZoIRh54SE8rAplHrJB89QwYmrBt5e6YbUsJ8StOeBvfpvMV3CUar3sa8yAKiAmkAwmgcbtrWo049cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات دولت آذربایجان بعد از ممنوعیت حجاب تو مدارس، این بار تصمیم به بستن فوری مساجد در سراسر کشور گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152545" target="_blank">📅 23:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wpxvrss6n7hoO1AvOonRdvNs1wiPPumJ87_w2FpC2-fbkI9Z9ykCT-FepLwEM_MBQ6fw9bpIeNBN9JnRsYQ_C5-ypZOyglbokRzndW4hdnMhU97oaIuZecik0Gen9gGYKM_w-FMxKfa6cCC_u8Ex9nRDCDG06QhDCfWBsh58phCVoKYonlGSljyyIpxSyNqgdOq1-OsZVcsAI9IxYr9NQO8Q9MSUIu13dNT4JclqaHhTzxYVxx7Ik8FEkMYmn4I3iZ3CTEefiK1BIp7jCiiwUQybdkmHor33lpeCgioydoFRd3ENBK5v3eSmg4bZgVWKU3yy3Q7-RstmFTyFfgFFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در یک حادثه غمناک، امروز یه کارگر ۲۲ ساله مشهدی داخل یک میکسر بزرگ سوسیس کالباس افتاد و در جا فوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/152544" target="_blank">📅 22:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgt5nKHhrUm55AH8HRFGb5klSilX4a9vE9joc-iuYX4flDSKnSiMij0m6ulfxlwPdigjfANW0eBN49DwT8H94LHg7A0sHWgg0126-88pdTbn6JaUXc22fb0Um7xUOVSKfiTdx4JpJFzMDpT3sXAPpcHDVAPeSg8UrlOXEIq4nJkBejHjsg-yIp1mKhDfY3m4nY0RTpNlOHHDnugbVWmZ61dZqnE9QpKZDcbvaOdfQbqHXg3sWXIWcXi7HqP7E_G5ezZl68pi5ZNGzxO5zS49nwujCduD-hTua9yrL8vG0XcgttaeWaCQjaGauZNS1qlPE_VAV2Uedwr5cRMbdp0dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان نظارت دریایی جنوب شرق آسیا (UKMTO) گزارش داد که امروز صبح یک کشتی تانکر در تنگه هرمز به وسیله یک پرتابه هدف قرار گرفت.
🔴
مسئولان در حال حاضر در حال بررسی این حادثه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/152543" target="_blank">📅 22:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
هر لحظه احتمال وقوع جنگ و قطعی اینترنت وجود داره
🔴
اگه سرویس متصل و پایدار حتی تو قطعی میخواهید سریع تهیه کنید
👇
https://t.me/voxnet_bot
https://t.me/voxnet_bot</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/152542" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
👈
آکسیوس:
مقامات اسرائیلی متوجه شده‌اند که نتانیاهو تمایل دارد قبل از انتخابات در 5 آبان حملات به ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/152541" target="_blank">📅 22:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4bIIXEIGuN8l9MsEcepldqn2JDCts1SA5A0ZW1gFewxDmQ7hQ9VaWe9fUvYbd1Q_wuu1vhc_Cwa4-ZYgdQxREQEITEmnqoafkgbjpl_AqFgq5Qd3MpWzwrF4kJIImbnkMHIm4Xc6y-KTMph0txIUGFI0lXLo8-0lHpJ8DFAhJML0yeTKNzQ45bVFeSMS6va4KJ5WmtLlnyamfN6UnNf6t-BNMjXre-TE4-4RuNfw186xow0x0IqB3xLYCrg9zDeZ2_Lx2SpPjwQyvXbHD87w4M7jTwgR_E8XfU5wDyRZKhmkgjO80ycDe_dIWw10y_H9BwJw985gzXNUmc4Q0eGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم:
دفاع مهم نیست فقط حمله مهمه
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/152540" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8337fa213b.mp4?token=Z6CWSed7wNUwOel0u2SEnOphoauqSBGe6TGfaO3ayl4UQ109tNgtwa159JoglBuCQuWKIq-YcOMphIsOHq83U_TyvCLkNPmPeazVOnENfpdye1YAhn15S8OM3M1sFgfkYun57fvCCPNHzURzOla1RG4gJ9TYMrNBQLIIM3APEH3fqO7Bs6QMSZKXZRty35ejYwUSUyIxpbJjmwY4dlyDWtZ2-Lp00xYYB8CKJyVcZ3moWVR1nZNq_umW3RM89fhujF3xvvKJl04xaWi7NHznla86omPDTrxhN8KKB8uasoF1nH1IbjfHmlHaKaoBG4sn_DgOvBDqmVYxeawQ9QFotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8337fa213b.mp4?token=Z6CWSed7wNUwOel0u2SEnOphoauqSBGe6TGfaO3ayl4UQ109tNgtwa159JoglBuCQuWKIq-YcOMphIsOHq83U_TyvCLkNPmPeazVOnENfpdye1YAhn15S8OM3M1sFgfkYun57fvCCPNHzURzOla1RG4gJ9TYMrNBQLIIM3APEH3fqO7Bs6QMSZKXZRty35ejYwUSUyIxpbJjmwY4dlyDWtZ2-Lp00xYYB8CKJyVcZ3moWVR1nZNq_umW3RM89fhujF3xvvKJl04xaWi7NHznla86omPDTrxhN8KKB8uasoF1nH1IbjfHmlHaKaoBG4sn_DgOvBDqmVYxeawQ9QFotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر مطهرنیا: آمریکا فعلی جنگی نکرده که!
🔴
بازو یعنی حزب الله رو زد
🔴
ستون فقرات یعنی سوریه رو زد
🔴
قلب یعنی عراق رو زد
🔴
گردن یعنی حوثی‌ها رو هم میزنه
🔴
الانم اسلحه گذاشته رو سر ایران که یا تسلیم شو یا میکشمت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/152539" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGpWfzHaj_PyJwAi4pIB1uqQ-Wt9U6W4qMeygjF3tMsrTmb0kI3uUVF0O8B7qvd4Os9sTdSoJiervP4JtbPAkYHCzZv9v0K-1KNUebxGumtRtdu4Oc8tsV8cvWcsWmJBfWIEf4IHib3o1Kf-CTIuNclx8XMiilxg7Vv1REVD6hirjLwN2wb9nrwKWAoYsLj1kTWWOKW2tjzW6eWJMO6Ifm3we-JgeE09cOM1_XU9g4CMp5SGX-s8QeyctAHnyDuwfCHHh8K2uzClRGzckVPErEAaw5s7alk9EK4vmeub0p5NaaEm_CzUFUlILN1iullG7w2lam766eAY4jZuvArWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: آقا مجتبی رو تو بیمارستان وقتی میخواستن بخیه بزنن، دائما میگفت نمازم دیر نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/152538" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کانال 15 عبری:ایران برنامه‌های نظامی خود را به نمایش گذاشت، به منظور آمادگی برای هرگونه تشدید احتمالی در منطقه. این کشور تمام گزینه‌ها را در نظر دارد، از جمله احتمال ورود نیروهای زمینی به خاک امارات متحده عربی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/152537" target="_blank">📅 21:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هم اکنون حملات حوثی‌ها به آرامکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/152536" target="_blank">📅 21:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نقدی: اردن به ما گفت با یه موشک شما ۲۰۰ تا آمریکایی اینجا مردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/152535" target="_blank">📅 21:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy1k1HVXGq3t_ieDuv3Cm9WM-CmojxUzCC67S007F-Dzspl5PCOwNgnxXy08w3xOsB8qoW6sI9DK9NlBGiJUXyvVPhjrKhr2lMqJH7Q261s_Lr9CmdCxtCRlepMw9LVVeWnpuqkghVHoyFujjwOIOtmq7IAPMSljLOR3CnP51dhe5MBmW0pixfl3QDgG36OQEXUZW_6d7muongMc-DRWXxnow5ofWvJfBCgAuqGADolo1Djkh__AbGzVmYyJ5-8mzSzUyh7G3m7VOWmDekY13FDFmzv9Pmda13ajfAPbZ-L5opJbxKSXTW8JkJWSOq-SEKzBWUHKdLTe20MDlIDIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقدی: اردن به ما گفت با یه موشک شما ۲۰۰ تا آمریکایی اینجا مردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/152534" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مقام ارشد آمریکایی: ترامپ به نخست‌وزیر گفت برای اقدام علیه ایران آماده باشد
🔴
یک مقام ارشد آمریکایی اعلام کرد که دونالد ترامپ در تماس تلفنی به نخست‌وزیر گفت:
«می‌دانید، برای اقدام علیه ایران در هر لحظه آماده باشید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/152533" target="_blank">📅 21:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYdM2BZRgKxt8f1JMqlVqwtL-8wgomaSazyI3GwX5Pu1-FCLVnYTlGTcZ9QL36pHo0wKAe-k4AvXJwlJ9S81ZiRmSTEALtOay3rOwFee6gvcXdjEY0B4gS6kKdUZ8Ddz2B80LG2cZy19xNYvLEwtBJQMCJu-fgsO-VAS5vuHRwkRuftQvFwhi7wyCC7p5DHF2wTSxylNGKE2R3Szc7IxK4PChraVFL3k0Uflfu6loRGNbAVRYduvyKaj2PACt3_1nrlYgfWC0UWuKY8Y3sGEwLzuuASxBt-vCS06g3jR3pZiEpO62zjt-0Pebw9RfkH-fnV_MC9Wckfpe3RVdobIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): هرکسی با جمهوری اسلامی مشکل داره، پست و بی ارزشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/152532" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/152531" target="_blank">📅 20:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/152530" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
حوثی های یمن:
شرکت آرامکو هدف مشروع ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/152529" target="_blank">📅 20:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فعالیت شدید هواپیماهای نظامی اسرائیل بر فراز حریم هوایی ام الفهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/152526" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/باراک راوید:
امروز نتانیاهو و ترامپ درباره یک حمله احتمالی به ایران قبل از انتخابات دو هفته آینده گفتگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/152525" target="_blank">📅 20:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
لیبرمن: نتانیاهو پیش از انتخابات کنست به‌دنبال آغاز جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/152524" target="_blank">📅 20:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152522">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSHu085oze3xYyaMdpgqGiaBD_Apgh7j242XDRNejeRnFA9jBN5IV8LiQM5hn_SamWjAI0aAs2leiZ9ns6OboUm12DvXUKoIEBm2BHxzmSHpv_c7eYAESLsiZLDTx0nZ7QWf_JmUlzETupWlRn1pZc7QCmckzJITjpaVMZaGYGvlQVWQ2DXdexJUHA_wYPQyBnWhCqCmgEZmjEL737prRI3OmGAvApyKvTgBS7V2bv2liO5l1E5Uy0ZExWC30ZBVrr9ZGraz61bYpBzZfwRjoo-2CwEKdoED83q-f4t1lMbpXXLtAkX6IJlX-GIzFjMu9sWlPaUKTjtkZWbQw1nG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A76yXA2NNjl4dQmD7Z9NrnJNgJTAZPKpH1aG8SzokYo7vADvbJIWPH3R5VBiozaIkPD_NW88WS1XSleeaLZkWKAQIM2XoijOOEqfDKlENEION1UBigmRW7EiRX_CmwuZmtFgTHbpisDgyXijnRim2hGUszd_fc-J_jxGw4HtI2-tRkBl85A0qhOgg7NF5s2_X7FEEYNwckukoAIH-Q8l4cw57mu0my4Qs1iGiZge6cj54EkRGIivZbR_49HX-TYCm6v9sKy4tPfOcwpITzJ3vFNxyHJgrryuPGbL73ZRgDrfl8shuhSN_6ap_3kHvbJRMzjCT5X0Oe2HbT_L0x2hnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کمک‌های نظامی اروپا به عربستان رسید
🔴
یک هواپیمای باری مدل A400M متعلق به فرانسه، هم اکنون در فرودگاه بین‌المللی جده فرود آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/152522" target="_blank">📅 20:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152521">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHLo2ZtqOjetPCg55Yobr3SNYDXqFAw5Ga9gh8JiLbaq-ITrAcn7frh0m0Q_ztUjmMTT0j7yEOW20xxGuJo1N5eVOgd45luIQrO_G8eS3GyKTUCCxEZGq3joGWU18PZDbubza8ugc_BDo9taf_D9e0UEL1czlDjP8Wj5bsxEriMCQ2VkB9HRMkEyFAbttTfff7siUTkxNpMC8IyPIVNHiv8-uUS14tm9Z284FtZay_7c54WgLd2ULsJcVkOyz7-GoQ84V8Xyffqq3erweEHaSySfa-gbyh3ak6t8Iz56Ys3Nmbm7XlYxMNviiT1O2q-ekczgCRyjW6Et29Z_iIUhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در مورد حوثی ها:
رفتار حوثی‌ها بسیار نامناسب است. من تصور می‌کردم آن‌ها یک سال پیش، زمانی که ما به‌شدت مواضع آن‌ها را بمباران کردیم و به درخواست خودِ آن‌ها عملیات را متوقف نمودیم، درس عبرت گرفته‌اند
🔴
آن‌ها مدت طولانی در سکوت بودند، اما اکنون دوباره ظاهر شده‌اند؛ احتمالاً به دستور ایران که کشوری شکست‌خورده با نیروی دریایی صفر، نیروی هوایی صفر، بدترین اقتصاد جهان و تورم ۳۰۱ درصدی است. آن‌ها به شکلی بسیار زننده عربستان سعودی را هدف قرار می‌دهند و عمدا تلاش می‌کنند تا احتمالاً پیش از انتخابات ایالات متحده، قیمت نفت را بالا ببرند؛ این به‌هیچ‌وجه خوب نیست.
🔴
کسی باید به آن‌ها توضیح دهد که من در انتخابات نامزد نیستم، من از قبل با یک پیروزی قاطع بزرگ برنده شده‌ام، اما من پس از انتخابات نیز اینجا خواهم بود و هرگز فراموش نخواهم کرد!
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/152521" target="_blank">📅 20:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152520">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفتگو با الجزیره:
حملات ایران به کشتیرانی در تنگه هرمز را از نزدیک زیر نظر داریم
🔴
به مقابله با اقدامات خصمانه ایران از طریق رهگیری و مقابله با حملات و تضمین تداوم جریان کشتیرانی دریایی ادامه می‌دهیم
🔴
به ایران درباره حمله به کشتی‌های نظامی‌مان هشدار داده‌ایم و در واکنش به حمله به یکی از کشتی‌هایمان، کشتی‌های ایرانی را هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/152520" target="_blank">📅 19:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1KyUaG1hJT0ELrgCt2H8-vzBqrt4SOxbPhlThfznQ4ncsfaoVKTmMPBL2Tizg2YJonoIbrVaSy7nmdbh8skL3_g5fD8TChu2vc_C7VQjNdruvuMC6-X4Q6qRyiSk08ZZsVqwWF2LmM3QTF_TsIZgn8Eicj_7wJb-oIJYuDd8LVUNJiAX3gyT2dpdG7RPRHDyXCG-kQGFCV5YMRiqEuvvohzlnyy3LP-JkiEW26493VQCrezVA5PRKv8zarFt9OJfhWVu62H69CAH_3iw1B8zOXS1OzgIvmA959sj_VfEvb7BavVKQwt1LFzPNCIXHgfo7SjxfzK_rFfV1e69npC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی ها به قبرستان "الجبلیین" در تعز رسیده‌اند و برای حمله به کوه "هان" در غرب تعز، از سه محور آماده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152519" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cF_TX50POUlGdLclrMIetYmn5-t26RA-e98QX2AQbD_SZO0qHbL1ma0Bd6T2xoVDzxJ9uBfwAq_76YCNysQzFwsZDoMiBOWlS4x0i_ay7owYD4IWqukrsRgRXe4EiUTQDXlm3YbNaFApRkXb_QB0rVdbOZ2GnWK3xW0J9mvXIlBFPeKSMPygxr8P9y-AhRiFaOp8nRB39CpOe1yLVDMtWzZYW-ms6zdj3bB5Ar52Zu_Bo55CMY5pgOlx08wZsmuveSjqVzweZET-bI1WwPFLd4D94ezCqAfSCOlMes3sDjV8ROeYlRMMK_w7350l5uYOcMJy7ebDXpkTKv2Ze9RbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به مناسبت دویست و پنجاه و یکمین سالگرد نیروی دریایی ایالات متحده و محاصره ایران، پیام خود را منتشر کرد:
تولدت مبارک، نیروی دریایی ایالات متحده! اکنون ۲۵۱ سال از پیروزی‌های شما، هم قدیمی و هم جدید، می‌گذرد
🔴
آنچه که نیروی دریایی شما با ایجاد یک "دیوار فولادی غیرقابل نفوذ" (که گاهی اوقات به آن "محاصره" گفته می‌شود) در تنگه هرمز انجام داده است، یک دستاورد تاریخی دیگر است، از میان دستاوردهای بسیار. تولدت مبارک، نیروی دریایی ایالات متحده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/152518" target="_blank">📅 19:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef3983c18b.mp4?token=qM1i3s7E6N1IXHp80RbmPjy-X_quR47nTHubOIno36m31zzUP_3jmaVXePlS3yk8QN1aiiLHtzxhxH4yKSZnkmenywKoMOLjs5vSYZyNs4UXPZmLRRRJVkZxGAPUHRoWP3k3gZOi-lEwH-lF5RxEyVKgPPmA8Y-Xh1BuX2Wvm7WQ8klejhQg2bFTmZKBoWMgfB2cvZlwWvHs9WjhlcL4pzmLXaI8JIOw0gghO4LxH4x9gWPgx_qNH36HaJZgrku6-87vX517JizfLiLpNlkGC_SjjH6yOxbaQleaAp6nU5dH6TSYkklp1sd2kqWexYlEkkWciGirIi5ouhprJlsDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef3983c18b.mp4?token=qM1i3s7E6N1IXHp80RbmPjy-X_quR47nTHubOIno36m31zzUP_3jmaVXePlS3yk8QN1aiiLHtzxhxH4yKSZnkmenywKoMOLjs5vSYZyNs4UXPZmLRRRJVkZxGAPUHRoWP3k3gZOi-lEwH-lF5RxEyVKgPPmA8Y-Xh1BuX2Wvm7WQ8klejhQg2bFTmZKBoWMgfB2cvZlwWvHs9WjhlcL4pzmLXaI8JIOw0gghO4LxH4x9gWPgx_qNH36HaJZgrku6-87vX517JizfLiLpNlkGC_SjjH6yOxbaQleaAp6nU5dH6TSYkklp1sd2kqWexYlEkkWciGirIi5ouhprJlsDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: دیروز، روسیه شش تاسیسات انرژی را مورد هدف قرار داد
🔴
دونالد ترامپ: خب، اوکراین روز قبل از آن، بسیاری از تاسیسات را مورد هدف قرار داد
🔴
خبرنگار: اما به نظر شما، روسیه آتش‌بس را نقض نکرده است
🔴
دونالد ترامپ: در این مورد، بعداً به شما اطلاع خواهم داد؛ آن‌ها به یکدیگر حمله می‌کنند، اما همه این‌ها بالاخره به پایان خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/152517" target="_blank">📅 19:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ درباره ایران:  "ایران یک کشور شکست‌خورده است. ما به زودی در مورد آن‌ها تصمیم خواهیم گرفت. ما کنترل تنگه هرمز را در دست داریم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/152516" target="_blank">📅 19:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152515" target="_blank">📅 19:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / ترامپ : به‌زودی درباره ایران تصمیمی خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/152514" target="_blank">📅 19:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سوال خبرنگار از ترامپ: چرا در انتخابات اسرائیل از هیچ نامزدی حمایت نکرده‌اید؟
🔴
ترامپ: ما هنوز حتی به این موضوع فکر هم نکرده‌ایم. شاید کاری در این زمینه انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/152513" target="_blank">📅 19:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: روسیه در حال حاضر گازوئیل به ما عرضه نمی‌کند. آن‌ها این محصول را به کل جهان عرضه می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/152512" target="_blank">📅 19:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86e6e5a41.mp4?token=JrZu0vm2WX1AtjTbdtpELFuJZux7Ay8Jj7TAYoDB2cifhmmQxaWoT8VHSKhEvcWoCdiCGGzYBlWRGh9qfv2Tc8i0_4iThuQsNLHEfbPor6okVHjRzZBsXWRl4UEgWLBITsKIBBHX-zjl2T5d3_DsMM3ORkmULoXavF40muHXe2MuoYaVFr69W6Rk8Vs-LIwsMgKPr9n6LwDLORiTQYWdg0LE6w_k3WMIXL-vUyluhH9uEf5Dl1pljfVAKQpEeDGX4w63WZchVU2MuryH9ox_yYP3jwRyWTqj9F0eirP4jnztP04i_luACMH2YCR3BX5JMhRuTV77YfSJ7Hx_AkUPsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86e6e5a41.mp4?token=JrZu0vm2WX1AtjTbdtpELFuJZux7Ay8Jj7TAYoDB2cifhmmQxaWoT8VHSKhEvcWoCdiCGGzYBlWRGh9qfv2Tc8i0_4iThuQsNLHEfbPor6okVHjRzZBsXWRl4UEgWLBITsKIBBHX-zjl2T5d3_DsMM3ORkmULoXavF40muHXe2MuoYaVFr69W6Rk8Vs-LIwsMgKPr9n6LwDLORiTQYWdg0LE6w_k3WMIXL-vUyluhH9uEf5Dl1pljfVAKQpEeDGX4w63WZchVU2MuryH9ox_yYP3jwRyWTqj9F0eirP4jnztP04i_luACMH2YCR3BX5JMhRuTV77YfSJ7Hx_AkUPsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره روسیه و اوکراین:
هم زلنسکی و هم پوتین می‌خواهند جنگ به پایان برسد، اما نمی‌دانند چگونه این کار را انجام دهند. ما به آن‌ها کمک خواهیم کرد تا به این هدف برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/152511" target="_blank">📅 19:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / ترامپ: حوثی‌ها خیلی بد رفتار می‌کنند و ممکن است از ترکیه بخواهم در یمن مداخله کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152510" target="_blank">📅 19:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
گزارشگر: آیا توقف کرده‌ایم که اطلاعات را با اوکراین به اشتراک بگذاریم؟
🔴
ترامپ: خیر، ما این کار را نکرده‌ایم. ما به آن‌ها کمک می‌کنیم. ما می‌خواهیم جنگ به پایان برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/152509" target="_blank">📅 19:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152507">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlh-QkRUrjeoV3g9HrK6lVHiQXYHlrRVYz9DiyRFSNefKt5ChSRv7dZ3tbxsFVzyVLvuj4qxqNwGryM2o6MVxmYQ_h2qUmcICn1iQRtz60YvnxLgeryh6Ixrpt0ZfyZiNr9oPtc50pETOG_M8_Er5zTAhF20xVOgNfEGfoVHBS35zfn7X0kSVhgnTPeQHJWeGSo9nhirI7G5tr1EulXI4kdNpc9b7EJvpyMZDYMULLC5w_HH6ShbbQ79fkltoqrGsOUh02LbXx_hOgEYNmogE_UMQx4bIY87S6OKZSBsz1JwBByL1uspbtazET5bJj9yXw_15M6vHE1Q-icncslAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40aca6cd2b.mp4?token=JKQDi6kDADShYOaRs9y_BdMTTXXmmmtw94llXoiR1kZJNTWTtI3gViegF1BF4bB2CBdbPywCDr9nT5dbECVK7B0WP0_vANbOpSrBWcKshYY2W6VUDSubpCqvDdHPwzildZo7SvMmCHrfM7_mbn_bTtCxffpD0QvpQLYarl7G0qlNWXjWzyTk8Ru9c9JyPDn50ez2zO7pV2i64KKW5DUUkGE0GKQ_udB17RsgCyZCOb3GLiIyezN5VJ3iq3CNe5j-Pl2ojMUe3DXrrAlzJ-6qOx6HkXSxQjTcNipDSddb6iCA6rXqF-p0qpL5A_WO0yo4DwA1qST_i0CG6QMZRFo4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40aca6cd2b.mp4?token=JKQDi6kDADShYOaRs9y_BdMTTXXmmmtw94llXoiR1kZJNTWTtI3gViegF1BF4bB2CBdbPywCDr9nT5dbECVK7B0WP0_vANbOpSrBWcKshYY2W6VUDSubpCqvDdHPwzildZo7SvMmCHrfM7_mbn_bTtCxffpD0QvpQLYarl7G0qlNWXjWzyTk8Ru9c9JyPDn50ez2zO7pV2i64KKW5DUUkGE0GKQ_udB17RsgCyZCOb3GLiIyezN5VJ3iq3CNe5j-Pl2ojMUe3DXrrAlzJ-6qOx6HkXSxQjTcNipDSddb6iCA6rXqF-p0qpL5A_WO0yo4DwA1qST_i0CG6QMZRFo4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری منتشر شده از حملات عربستان سعودی به شهر حدیده در یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/152507" target="_blank">📅 19:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84fea900d6.mp4?token=bJypf4bOZx8kO4tUEEGPrhYY6MWDm3fSCWitLaypOEkKba13rHmdiTtMUpwM4Gk1OWmNWTAgtgupdqzWc5Iz7uli7vNnnOsGOqXn6etGLMdztDWqrbdoUk9jyDTChqquBm2cKDM4GmdzdZ7AO8VHOmXRd69AUTeE5YO8G-LCXiJVZVyScjS0G6ar49kkc1l9VA4_od1VXs8dRfvpfmvPFP-VP6kgk0BFY7Nrk7UjZtuJexty4uvQ1PIQmi0e1977W4dIB0oltlz_Swuk_6cwnSvX1Yaeqxt64Ga296XB9so2oYE416nMca0QYtEySwh6EJgmgQ6mGp2nqQ6zjihZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84fea900d6.mp4?token=bJypf4bOZx8kO4tUEEGPrhYY6MWDm3fSCWitLaypOEkKba13rHmdiTtMUpwM4Gk1OWmNWTAgtgupdqzWc5Iz7uli7vNnnOsGOqXn6etGLMdztDWqrbdoUk9jyDTChqquBm2cKDM4GmdzdZ7AO8VHOmXRd69AUTeE5YO8G-LCXiJVZVyScjS0G6ar49kkc1l9VA4_od1VXs8dRfvpfmvPFP-VP6kgk0BFY7Nrk7UjZtuJexty4uvQ1PIQmi0e1977W4dIB0oltlz_Swuk_6cwnSvX1Yaeqxt64Ga296XB9so2oYE416nMca0QYtEySwh6EJgmgQ6mGp2nqQ6zjihZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدیری ابیانه: حسن روحانی می‌خواست اروند رو به صدام بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/152506" target="_blank">📅 18:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عراق سطح آماده‌باش رزمی نیروهای مسلح را به بالاترین حد رساند
🔴
علی فالح الزیدی، فرماندهی کل نیروهای مسلح عراق در واکنش به تحولات جاری و تهدیدات منطقه‌ای، دستور ارتقای فوری وضعیت دفاعی کشور را صادر کرد.
🔴
ارتش و نیروهای مسلح عراق موظف به افزایش سطح آماده‌باش رزمی به بالاترین درجه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152505" target="_blank">📅 18:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عربستان: دوران خویشتن‌داری عربستان سعودی در قبال حوثی‌های مورد حمایت ایران به پایان رسیده است، به زودی ضربات بسیار بزرگی به حوثی ها وارد خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/152504" target="_blank">📅 18:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عوستاد رائفی‌پور: ۵.۶ سال آینده بسیار شدید پر باران و سیل خیزه برای ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/152503" target="_blank">📅 18:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucoTfP-XPjhMscgzc-wORkCsp3x4mozBovbeNGiNZhwrN9zzOKIE_NDo9nWMh0Og6j1WduACUOQy0RCawy1-yB7r7AIZ9Ole5u9BByGJ6XuHWVCLOW3LbmE-97c6vsxghmQ-Em5Z1EmvbG2gud0OJyF0cACtaBu3MkPgAyfQGbeuWCahnlwIeH01UT_sHK_Y9VMWma6EEOzKMH5zEsQEavOe_KQoTSUBQotJ-ZveZPmi6M6o5o45hza2wGbRPzgYgKLF04FrTBMa2haO5om1Gi_1RFmyLw8wkk3iHlHayWAm_qtchA-baqBkSLPvFrqHU2utUh7VyC6wjhszmOTBeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه گاردین: دست‌کم هفت کابل مهم داده و اینترنت زیردریایی از تنگه هرمز عبور می‌کنند.
🔴
یکی از مهم‌ترین آن‌ها کابل AAE-۱ است؛ سامانه‌ای حدود ۲۵ هزار کیلومتری که جنوب‌شرق آسیا را از مسیر خاورمیانه و آفریقا به اروپا متصل می‌کند.
🔴
همین موقعیت باعث شده هرمز، علاوه بر گلوگاه انرژی، به یکی از گلوگاه‌های حساس ارتباطات دیجیتال جهان نیز تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/152502" target="_blank">📅 18:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3234a3eb6.mp4?token=R9DDgkf2JaCNmrwbA4nAR3NEWHK8eNpXDNdxKsNiobEqcIRczIHLKtS0EjuoHmpmLfKufFkFhvgMAXmoKEdhYcJXLBwzg6bUrLPKaB-CKsdh8RFlYCdgDkxs_sFC6_CPo1ybmOFZ1aGQ2zEi2S1tWeOyXLYn5kJ2DApJwma5PV1DsF8OgxtvbKtZnb3LNIp9UxTZ2TWlhRJg3CO3KvEP00YI8DbzAujmckP87IcsEUFL6FbwigDhYJDfyRG70pQIeJRg4e_aD9P2lwsvrIRVHqD73q64uZF0acXYKErnybyXxrWocAJiy2Uim-ujhoW4Y3jQN6IP_oaWit9wgXgZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3234a3eb6.mp4?token=R9DDgkf2JaCNmrwbA4nAR3NEWHK8eNpXDNdxKsNiobEqcIRczIHLKtS0EjuoHmpmLfKufFkFhvgMAXmoKEdhYcJXLBwzg6bUrLPKaB-CKsdh8RFlYCdgDkxs_sFC6_CPo1ybmOFZ1aGQ2zEi2S1tWeOyXLYn5kJ2DApJwma5PV1DsF8OgxtvbKtZnb3LNIp9UxTZ2TWlhRJg3CO3KvEP00YI8DbzAujmckP87IcsEUFL6FbwigDhYJDfyRG70pQIeJRg4e_aD9P2lwsvrIRVHqD73q64uZF0acXYKErnybyXxrWocAJiy2Uim-ujhoW4Y3jQN6IP_oaWit9wgXgZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتی زخاریا، سخنگوی کاخ سفید:
رئیس‌جمهور من—ببخشید، همسرم. این یک شوخی خوب بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152501" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxbDV5tWe6xsO8sPbXSnaixo_sQwKT7cTl3ymBIAUcvoKiqi55dcB71nLJ-s3uGh8bRlgBMQhS0uQtuWliyhiQNbq0FsBd3VA3KB21xoT1WvTlwKG1YFoTM0VtyDT5Tv6yAHSFcnXklv9gDLUU4GDYLsoGs8aXHIx4RGk7WmdRBicCzigBQJ5XvCNzeciCMt-T3mFndk7rwVkZUYi4K_MTvqAjhkbzTenR_yK0VVvAeT_2055irNW4Y65dlaelfCl8UAmVPU5m7q92YhmEWR4dFRWkWIwIiNE92ZMeFfOJ0c8GAC651CmrjmaqYkld1iH6HFcU8ij6hE_cwJuQdZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5yZIwXQbgxQPexYZkj3IjiXvl9debOQsnC2bscjKdYlhaI9zJ4TPChakze1vDC0AxBkr05PEHLWq53LEvTN8MuV1qzTsc4-hor_5hKPgCkJGwHBB_697kF8PMncQOsXlG8hP_BYBnsuI-fuATN-kwEfK4QzdCC1_PR7_ISkA1N2kyeKgYabU6yESVEpkIS1CWVAiwNQQaIE0G4L0ijbzMmVt-s40VyUM5jVyJ9_DRRJnr5b0urzZ1gGE80QkBrlBmpe8WVoVdi7Pyvenz3LrYUYpfB1Nrs9IbnrT2pH_uXG3QFEqtZSOB0TL1zbUEV79gnYdSN2uGaN8xsh6P6-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_eHqOhm9U2fNj1aFQYhnj9uN96oGvdlae-cgybOHetzkYKJHMfT_OAuKZ_8g1LX8gsou3mUWgCl5Uvu7qJi0wafslVU1HPRv7l7cNOOItnR2D_0GCJJwDSsVEZCVq4_W5y1Vg8KAgRGk5RwYOmCHG1ltCq3jMjknLJOPISVFV0oCCY5w9hOiOL04u2J7_QUgOD5vwrVOx1FqEg2ScjgA_rbapcWTtqM7l2gvo7cZGycHDZb9JOjtkPhw-V_oNtp2CHU8irr5Xz_5A9iK_S05MkXAfnx6NrqhytlfbjT2FJxwsV1jQgOa_VkCiWPaXbF_zc7XNtsdtNFC8A7H8DE8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هشدارهای تخلیه صادر شده از سوی حوثی ها برای برای تاسیسات ظهران و ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/152498" target="_blank">📅 18:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802b135f8d.mp4?token=u-gUX-7QstoOeuOquj19Hmdno1gB1Uu1GFgpt6hDsx5MWaBTiHFCyI4-l3YRnVTENPFBxjprqZUtmPbMRk476fBKLtZ4bQBlNGvmC7g9eAVkPzqS-xpGp8A81VsqSedm-_a20ZWqR7CnoeTakfJ9TwctzGP1VSyHrStYS5cOo4q26ENffIvRsIRT25WfwTczmNJ9tFswhreabBZ8zciFajopP_Wi7_YhPwZOpdalxAoXP8NBmCHHbvoLPDvKSMFvkLNxC0lLt-H8S04n4zia6ng1fD-yeAneKYUDSqePx3VBK484iJSJjjfjrB82SiXCfb1SIf8pcm0tI0CobmY5BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802b135f8d.mp4?token=u-gUX-7QstoOeuOquj19Hmdno1gB1Uu1GFgpt6hDsx5MWaBTiHFCyI4-l3YRnVTENPFBxjprqZUtmPbMRk476fBKLtZ4bQBlNGvmC7g9eAVkPzqS-xpGp8A81VsqSedm-_a20ZWqR7CnoeTakfJ9TwctzGP1VSyHrStYS5cOo4q26ENffIvRsIRT25WfwTczmNJ9tFswhreabBZ8zciFajopP_Wi7_YhPwZOpdalxAoXP8NBmCHHbvoLPDvKSMFvkLNxC0lLt-H8S04n4zia6ng1fD-yeAneKYUDSqePx3VBK484iJSJjjfjrB82SiXCfb1SIf8pcm0tI0CobmY5BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتی زاخاریا، سخنگوی کاخ سفید:
دونالد ترامپ در حال عمل به تمام وعده‌های خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/152497" target="_blank">📅 17:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
چندین حمله هوایی نیروی هوایی سلطنتی عربستان سعودی، پایانه نفتی الرضا در بندر الرضا، شهر الحدیده، واقع در یمن تحت کنترل انصارالله را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/152496" target="_blank">📅 17:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نیروی هوایی سلطنتی عربستان سعودی نیز در همین بازه زمانی، حملات هوایی را علیه شهر الحدیده در یمن، که تحت کنترل جنبش انصارالله قرار دارد، انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/152495" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نیروی هوایی سلطنتی عربستان سعودی نیز در همین بازه زمانی، حملات هوایی را علیه شهر الحدیده در یمن، که تحت کنترل جنبش انصارالله قرار دارد، انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/152494" target="_blank">📅 17:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
عربستان تأسیسات شرکت نفت در غرب صنعا را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/152493" target="_blank">📅 17:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هزینه ۳۶۶ میلیون دلاری ایلان ماسک برای انتخابات میان‌دوره‌ای آمریکا
🔴
رویترز گزارش داده است ایلان ماسک تاکنون ۳۶۶ میلیون دلار در انتخابات میان‌دوره‌ای آمریکا هزینه کرده است
🔴
به نوشته رویترز، هدف این هزینه‌های سیاسی حمایت از جمهوری‌خواهان و کمک به حفظ قدرت آن‌ها در کنگره آمریکا بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/152492" target="_blank">📅 17:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c888b31cc8.mp4?token=dSlEPw_wqLKpYK936K6orVfL4-DhDm00Rg2r8gWKCDkgwWFDCWFATObG8QpB5I4wuM7f9VVeUQ0u4X8Tq2txOeknsSlanLcy1VZge35cychiH7LRIzCHaN_rRxEk59IKjm2KITKfGdGtiKDpcceknCGw_XfX7S1myhkew2uiABY5VQZFyyRXRVHGsh-RlcVJm9XEZYxPPWRRZ-k8JAoWQvADAFabO-eN72zxy1V65lOuaRDZyqljlatOg6TdpysjqcBvtZsOykFEyBwBsCMVVPYyGtNmhwhDxM8WCBUoKL2YdJbt-sw59HUyB5MFkyin1jR9hBm9dSzDojw2SG1AHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c888b31cc8.mp4?token=dSlEPw_wqLKpYK936K6orVfL4-DhDm00Rg2r8gWKCDkgwWFDCWFATObG8QpB5I4wuM7f9VVeUQ0u4X8Tq2txOeknsSlanLcy1VZge35cychiH7LRIzCHaN_rRxEk59IKjm2KITKfGdGtiKDpcceknCGw_XfX7S1myhkew2uiABY5VQZFyyRXRVHGsh-RlcVJm9XEZYxPPWRRZ-k8JAoWQvADAFabO-eN72zxy1V65lOuaRDZyqljlatOg6TdpysjqcBvtZsOykFEyBwBsCMVVPYyGtNmhwhDxM8WCBUoKL2YdJbt-sw59HUyB5MFkyin1jR9hBm9dSzDojw2SG1AHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوکی از شبکه فاکس: آیا ایالات متحده از به اشتراک گذاشتن اطلاعات با اوکراین خودداری کرده است؟
🔴
کتی زاکاریا: من باید در این مورد بررسی کنم و به شما پاسخ خواهم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/152491" target="_blank">📅 17:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152490">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الجزیره: صدای انفجار در صنعا شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/152490" target="_blank">📅 17:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152489">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: صدای انفجار در صنعا شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/152489" target="_blank">📅 17:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152488">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
۱۱۵ اورژانس قطع شد/ اعلام شماره‌های جایگزین
🔴
روابط عمومی سازمان اورژانس استان تهران:از دقایقی پیش شماره ۱۱۵ قطع شده و شهروندان برای دریافت خدمات اورژانس می‌توانند از شماره‌های جایگزین استفاده کنند.
🔴
لیست شماره‌های جایگزین
🔴
۴۶۰۱۵۹۸۱
🔴
۴۶۰۱۵۶۱۹
🔴
۴۶۰۱۵۹۴۸…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/152488" target="_blank">📅 17:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152487">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNCIU5t5ipa95T2vLNtPM2uNEm0wMwLZ3MpJTm9Jj1IlUH_jBv6kO-XFSeE3Dzq_SVy804E7rSoddy6fUjStVz-nUTlw4KYioew3d7NUXamZA80807SgfqttDtH6y48UEfq06tMnUMlbchDsd6ATYCjoxaXaIJnF2ibO-kSccZ3t04fukPFlRMHryZB1lxa0q4KSZXA79nlgVJx3zI2hViUmtyUDtlNmVNwlfvhg4-ncYvuoAWajIaRg-4SC-r1FhzkF5zhPknrLThXZfYeEINxWfKq4gEAuxjSIFijqbha_RuBMOieJC-vLKl1wWJ8iFYxxp6AoY1SK6I23S6cRoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده آمریکا، هشدار سفر خود به عربستان سعودی را تشدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/152487" target="_blank">📅 17:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ایرنا: بیش از ۶۰ دانشجوی دانشگاه بوعلی همدان با علائم مسمومیت به بیمارستان مراجعه کردن و داریم بررسی میکنیم دلیلش چی بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/152485" target="_blank">📅 16:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حوثی های یمن: شرکت آرامکو هدف مشروع ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152484" target="_blank">📅 16:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آقامیری، دبیر مرکز ملی فضای مجازی:
اینترنت فرانسه به دلیل اعتراضات قطعی داره. ما چون شبکه ملی اطلاعات داریم هیچ دستگاه پوزی از کار نمیوفته برعکس فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/152483" target="_blank">📅 16:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
آتلانتیک: اقدامات اخیر ترامپ تلاشی برای وادار کردن اوکراین به تسلیم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/152482" target="_blank">📅 16:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
حوثی های یمن: شرکت آرامکو هدف مشروع ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/152481" target="_blank">📅 16:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE1gHKu0cvmXA2W58uQK19_s1jY2QKtMZWLyrEJlpNB86iHzyNAd2QzexCXCUTI-uimy5apiW0P41-o_vZ0nE9H1ZRCHV8dVL4wVmxJ837ZZNSagr6YLQ-f6GiiPQH6rh-uFNEDB05UnxvppOWGgjc0kBRoy3D6jQbQndJ8-i95GJdF9LHDihKcFYV5y9uZp-YRw4PH6g5oFROHtpmTm7o3qzATY43AGbX2Gio3Ef3E4K3ExP2VF0GexiZFJbmZRz6cLh-XkN0y6OflF9zozikMZ0O3UP9i5RgC3LOFaTEGsY8e7LiFmuUKuQfDORoaGrHkummIQbkW1ksSYixlf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتی، نماینده تهران: ۲۰۰ هزار تومن رشوه دادم و محدودیت ۲۵ لیتری جایگاه بنزین را دور زدم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/152480" target="_blank">📅 16:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مسئولان طالبان در افغانستان پخش رادیویی بی‌بی‌سی اف‌ام را در سراسر کشور متوقف کرده‌اند و به «تخلفات مکرر» نامشخص اشاره کرده‌اند
🔴
بی‌بی‌سی اعلام کرد که میلیون‌ها افغان به گزارش‌های آن تکیه دارند و در حال همکاری با مقامات برای حل این مسئله است
🔴
دولت طالبان گفت که این ممنوعیت فعلاً برقرار خواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/152479" target="_blank">📅 16:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دولت: اگه خونه یا ماشین یا حقوق بالای ۲۰ تومن دارید، کالابرگتون نمیره بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/152478" target="_blank">📅 16:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_O2aOgSrZ70uBunYSfeRdmseeiKNrnyUnAkaj-O_JCS_8fdfUr1DZ_1vEXarxxkGKbwTEGN5sUXY5SUU27l7huBTwkeL0_eUINhP0aeNui3RjRgh3oa_EgMpLN95GwHPwVKLivXvHarMf_pSKzDke78nlSQx7HXNrisVXgQ2R8u_xqUlAOPvctaZPRff-skuMPJSNVlN4Jd9SdU4IDBDIsVPdHNvYd9Pun3sI6NXHNajJ1S8HUilFwCVixxvkFSecOrxVwjM8FpIjLz84DCcFSfljCAo94ZUHrieZcIPJPs3Oascb5cEUlM7O4XpXyf_pEis1y5GoxBwq_ePdJzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان خواستار تخلیه شرکت نفت یمن در صنعا شد
🔴
عربستان سعودی خواستار تخلیه فوری محوطه شرکت نفت یمن و ایستگاه مرکزی «الصباحه» در صنعا بر اساس نقشه اعلام‌شده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/152477" target="_blank">📅 15:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اکونومیست: خطر وقوع یک «چرنوبیل هوش مصنوعی» در حال افزایش است
🔴
اکونومیست در تحلیلی نوشته است جهان تاکنون از وقوع یک فاجعه بزرگ ناشی از هوش مصنوعی، آنچه این نشریه از آن با تعبیر «چرنوبیل هوش مصنوعی» یاد کرده، در امان مانده است؛ اما به ارزیابی این رسانه، احتمال چنین فاجعه‌ای رو به افزایش است.
🔴
این نشریه رویکرد «رها کردن هوش مصنوعی بدون قواعد و محدودیت» را سیاستی نادرست و یک بن‌بست توصیف کرده و بر ضرورت تدوین چارچوب‌هایی برای کنترل خطرات این فناوری تأکید دارد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152476" target="_blank">📅 15:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
۱۱۵ اورژانس قطع شد/ اعلام شماره‌های جایگزین
🔴
روابط عمومی سازمان اورژانس استان تهران:از دقایقی پیش شماره ۱۱۵ قطع شده و شهروندان برای دریافت خدمات اورژانس می‌توانند از شماره‌های جایگزین استفاده کنند.
🔴
لیست شماره‌های جایگزین
🔴
۴۶۰۱۵۹۸۱
🔴
۴۶۰۱۵۶۱۹
🔴
۴۶۰۱۵۹۴۸
🔴
۴۶۰۱۵۷۳۴
🔴
۴۶۰۱۵۷۳۲
🔴
۴۶۰۱۵۸۷۳
🔴
۴۶۰۱۵۶۱۳
🔴
‌۴۶۰۱۵۷۰۳
🔴
۴۶۰۱۵۶۴۸
🔴
۴۴۸۹۶۳۹۱
🔴
۴۴۸۹۱۳۹۹
🔴
۴۴۸۹۱۵۲۵
🔴
۴۴۸۹۶۳۴۵
🔴
۴۴۸۹۶۳۷۶
🔴
۴۴۸۹۶۳۸۹
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/152475" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4501f8d0c.mp4?token=NetFdR9KRL9l2gbXVy8Pn-7CTjUQvmOSrndjDo4xL8Wf4NDwUtfJeQmYVoX8AJ-a-e3ZCE_PQ6CXVTty9hd-pWTmcBNvdCSEipFpCKZr5o_QuhBWwiXi8ufR8XZQGEPG2Smet-ON1vy2slHIp4NAayGFSw_BWG4JbCV-O1Ba_hnt6G68IXl_gMLsydzwNCJcrz-oGqrzeQ7c0rU0KIaRDVSAGjZMEK9L1SVR09s0DZ7WkegZUVpgHC-8eAr8VH1gkAotTSf0Q_Y8p9Pc8sSNy5MeXJCrQLqU0lubNnJpL5xgoDs957yZPFSgYTs2QiZW_u4ePdmUDLX9XBzjQjhuAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4501f8d0c.mp4?token=NetFdR9KRL9l2gbXVy8Pn-7CTjUQvmOSrndjDo4xL8Wf4NDwUtfJeQmYVoX8AJ-a-e3ZCE_PQ6CXVTty9hd-pWTmcBNvdCSEipFpCKZr5o_QuhBWwiXi8ufR8XZQGEPG2Smet-ON1vy2slHIp4NAayGFSw_BWG4JbCV-O1Ba_hnt6G68IXl_gMLsydzwNCJcrz-oGqrzeQ7c0rU0KIaRDVSAGjZMEK9L1SVR09s0DZ7WkegZUVpgHC-8eAr8VH1gkAotTSf0Q_Y8p9Pc8sSNy5MeXJCrQLqU0lubNnJpL5xgoDs957yZPFSgYTs2QiZW_u4ePdmUDLX9XBzjQjhuAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمعیت هلال احمر: برای هر سناریو از جمله حملات هسته‌ای و شیمیایی آماده‌ایم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/152474" target="_blank">📅 15:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
شنیده‌شدن صدای ۳ انفجار در پی حمله پهپادی به پایتخت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/152473" target="_blank">📅 15:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بریتانیا قصد دارد نقش روسیه در کارزارهای «اطلاعات نادرست» را علنی‌تر کند
🔴
لوک پولارد، یکی از وزیران دفاع بریتانیا، گفته است دولت قصد دارد با شفافیت بیشتری درباره آنچه نقش روسیه در کارزارهای «اطلاعات نادرست و ایجاد تفرقه» در میان افکار عمومی می‌خواند، اطلاع‌رسانی کند.
🔴
به نوشته تلگراف، دولت کارگر بریتانیا این رویکرد را بخشی از برنامه خود برای مقابله با فعالیت‌های اطلاعاتی و تبلیغاتی منتسب به روسیه در این کشور می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/152472" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab51fa2077.mp4?token=RyoL4HPL93-PzCqmxviiZAwMdSSrcvtZ8zb6xP-npFdjTchpPY7aAXa9yJy61yhptleWZNiedVcR9vwbRe3jyMpp1t6yxWxYphSsBA-UY5cPoLxV1baqYfxlv30Ce-9Fn2LuUrYpsleVh4Ki3T1sKLFYWhK1OtJ10KgU_4rvVqPruBPhzWGG3XXQcGiYee0y2ioMncK6lWyvN0gwL90ViTmygoD5pnmztEYS51r6FrsRNrZin-GydNty7XMOK0u5SjmHJ2kGdh-B7jBOAsn7QPxSNCia22TZJAjrDWw_SUHZ7qXG15Kq1C4NtbM3fDLX8nnMcx-5r95698E1uc9ppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab51fa2077.mp4?token=RyoL4HPL93-PzCqmxviiZAwMdSSrcvtZ8zb6xP-npFdjTchpPY7aAXa9yJy61yhptleWZNiedVcR9vwbRe3jyMpp1t6yxWxYphSsBA-UY5cPoLxV1baqYfxlv30Ce-9Fn2LuUrYpsleVh4Ki3T1sKLFYWhK1OtJ10KgU_4rvVqPruBPhzWGG3XXQcGiYee0y2ioMncK6lWyvN0gwL90ViTmygoD5pnmztEYS51r6FrsRNrZin-GydNty7XMOK0u5SjmHJ2kGdh-B7jBOAsn7QPxSNCia22TZJAjrDWw_SUHZ7qXG15Kq1C4NtbM3fDLX8nnMcx-5r95698E1uc9ppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجمع عمومی سازمان ملل متحد در ۱۲ اکتبر، اعلامیه‌ای غیر الزام‌آور برای آمادگی در برابر همه‌گیری را با ۱۵۳ رأی موافق، ۳ رأی مخالف (آمریکا، اسرائیل و آرژانتین) و ۲ رأی ممتنع تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/152471" target="_blank">📅 15:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس:
آمریکا رمزارزهای دولت را در جاهای مختلف ورود کرده و مقادیری را برداشت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/152470" target="_blank">📅 15:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: دوست دارم برای سومین دوره رئیس‌جمهور آمریکا شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152469" target="_blank">📅 15:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZaSGzaP3nYV4jMmZwyhas92WBu5DwizD6TpX2lJLL3mmtIvJDACClu117NfOwXnZT8WYzemibL1ZizVBkYnSGhkiAYmcDXOpJ2P5qOpT5XL7q75adK82hkdJuJ4svDKh_RMIEamRtS6aR1jeS_p64gwYISjxTh7_dOeiU3riB4XcrTuLQe4CIoNsH6lj9h9L-LydzrGqfNnZn0nMx-5XJ6PbnYz7Btm0jVmvd5rSkGdTHj4eVP_A1dTLOR8xsJfpg_-Yjktt7xqbvFe62vQxwlRoKuWyZene3fAyIdHDv6HWZPY3MOIy3RPxPnjTuYwpLim3tyFPKwxJ_cum-K8e3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WQnzynYjplxJQ9g9vsnY_-jWP5mu1Wx_CpUAUxeNdngfYSCvewQ6OkuEnjAANoNFbz1O9rMOG7y1jg1ugNzFz8kr3CiGexJRR1z1A4c9sMTTdSlsfawf8OII7o-03ETwQoUaHEQEFkUVV5vswh0npHWrZ9gp1-pKHLZWMn2GaQ3Nn07U5Pc-IXsGWiu4qIKUuK-JvZtlcghPc003WAI1Ew_3vfeOIR8wZ15-qKmCeTNb3hUpe28uJdszkB-WHJ2IXnCQOu6JvQtCAa212iqxsXlkjMB5Egg7mtlm2VwSnBKx5oVUI6B4h-I8VjfnrYiAZtJHwW3PMjt-dAEBSTsDhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بوسه کریستیانو رونالدو رو شمشیر و درخت نخل نماد عربستان سعودی در بحبوحه حمله حوثی های یمن به این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152467" target="_blank">📅 14:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=YzVqlMFunQQr6j3j-AzB9AnPX-1_p39OU_LvebNF2K2lZzGPmUnRCdaxyc6-lbOC_iiwU0uZAiPIo2bKh6RteeSVuhYVhNmHQKEmghKWRVi2b0LqmyPX-nbNbT4lyCtY8sVz4U83_ZHdakBdg_RxjgBnxcuvMa0S-9hxM6CoQj-Z5yxRDp6hSzCHFgzQPyIlYp-0PoJ3bqEIP9Kh3I9X35MSUUjMqCSgoKP8vDuYN2Uefgw7-RhD15yEXU-5WgN3ijwj09S9Js180nWCpBUjXrmig64k9Lm1xUI8oLMM4CvFF3tP-V5RGQLCS3p_g25UjIPYF4hqkV81SJdlCi-mHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=YzVqlMFunQQr6j3j-AzB9AnPX-1_p39OU_LvebNF2K2lZzGPmUnRCdaxyc6-lbOC_iiwU0uZAiPIo2bKh6RteeSVuhYVhNmHQKEmghKWRVi2b0LqmyPX-nbNbT4lyCtY8sVz4U83_ZHdakBdg_RxjgBnxcuvMa0S-9hxM6CoQj-Z5yxRDp6hSzCHFgzQPyIlYp-0PoJ3bqEIP9Kh3I9X35MSUUjMqCSgoKP8vDuYN2Uefgw7-RhD15yEXU-5WgN3ijwj09S9Js180nWCpBUjXrmig64k9Lm1xUI8oLMM4CvFF3tP-V5RGQLCS3p_g25UjIPYF4hqkV81SJdlCi-mHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهردار کرج: همه شهروندان ایران کرجی هستند اما خودشان نمی‌دانند!
🔴
آغوش کرج به روی همه باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152466" target="_blank">📅 14:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152462">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyxqZSKpfNRf3n3ejJy9OEXXj_xGJjsNAV4Z4P8T1GOC06OFEtDeNYJ4DjDPusQbOrvgh61jHDxGVHXuzS1RQUh14OjfAVkL50JcbEsJRtQRCwc8Pu4IKNkJRxvQRdq7z_g62JUeGsPmsiMJnKcRBh7ylh-krgncu0jL-B2pb6IL7QZArrnMAo8KZOslAWAqXBbW1j2exm4kdEXUeCO3za9hvlzdi5GVTw5QXyiCpr5fs2CBm20W_azwN0-d0H0DVGZvzacO5RWctNjsvJejxXAEE38ZgrRW8iQKQWC3z5NiCcmiCDRe6ZgFAho17mNbFQvcKdKSQwwwMT7MG1xnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huRMwoyTJ2Xe5RKXRzq3tsq0MZg5adxBi6GfeKwnwGHfKR8Nm6FbGcY23GMZpZ4CjH9Idr4FVUZS5kLoNm56OatMe4D3CH14j3U4W2kIRTUT7IfSYRfWP6hAO2tuBJS_DV86BcFdx0QxvGhEXTirnpT7EBts_pELX3SZR9-fMtskPcmyEa72ZbMcSu-mywHAOkKurWQAXliBFz4Q3I8Te4HCHulPG4g4tckEfH0z5nnLt1h6Z5lyPomS3b5CkJ7AbSdrohSkSbX8_u7opbIs6gMp_Rhn-5mpJihCyGPUxMp2OoMWKXz7gLI9OZeLo1MoXd1pCcmQ1KuextLyxTDU4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXU66E5RDRksyfspwii3axDFQ5f7lCeoe1PHIEwz1vWspPXqU5NQCJ-NzDZH4wkBfeFLNrwd4QGYASYuXyk9veG06niOEJykDaWnalZI1E3oHZkuj5zoSZLEQRTz9yv7I7viEDD2Rhzhd2f1i5ilepFL0PhgbiiAhOySlWdzbSrraKYv6qwUpmaKBTd66GlpkBNkjVf-AJkGzTkNBtBcbBgQ8f5BXS_KOKqeZi4uJAaO8L5V3M9hiJDvbnjcFltKjUas4IdoNyLaTmfWqjDMU_MpL5p0sSO4xUmp28P0SIQHcTC1C-9y9TUYOGimmrYBNl7sO_vGh24CTzqYLOzBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SL9gSQ_skYLj6G77k1kKSUArv0v1ExKRXJ4BPqItz-aHPRNeVrwTDen4HzMuhvCFlNjTBh5tBBjSaPbzPo0FNnoKHLJDUY0_lot99uKbu2ipwqkjpguvs5rFKPXPJ2bm1YHs2l45JmvJXYWAFzKc2W5emSnWxNhgczj-hPEXATQmz-UPOnDPooEq8WKdpgr5qFDIBP8wTtjbIXaWXsKPL7-hvyFCAHXzkKvMChqc2-RBDcXSSUh8OnCzdIQOrNuTobJ4ztUVwPWeomb4WSamUPxPw8LisuZNo7x8_nyOjNJbwAbc_bbvHovgkKWdviWelVJSROh-3wYwkYMyjl1ZvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه
🔴
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
🔴
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152462" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152461">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر بهداشت: در ایران سالانه حدود ۲۰ هزار جوان در جاده‌ها بر اثر تصادفات جان خود را از دست می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152461" target="_blank">📅 14:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152460">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حسام الدین آشنا: برخی امور مستند‌تر از آن است که بتوان با جابه‌جایی نقش‌ها گاندومالش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/152460" target="_blank">📅 14:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مفقودی ۱۱ ملوان در دریای سیاه
🔴
در پی غرق شدن یک کشتی بر اثر حمله پهپادی در نزدیکی سواحل بلغارستان در دریای سیاه، یازده ملوان مفقود شدند.
🔴
این حادثه که احتمالاً دومین مورد غرق شدن یک کشتی باری در این منطقه طی یک هفته اخیر است، منجر به احضار سفیر روسیه توسط بلغارستان شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/152459" target="_blank">📅 14:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zpwyo-d1JT1BfQMOUnfeEB3QD0k0MQOMxMBr5qLQueZBaVgUI4148k8A92DNEMT-9zD_D0oSrLQnUN0kwDzrfwMNO7P43fHq4t96oe_nzFLNJUkD-9ugYYQq_rsq3y70crf8FAQ-BXpc5r6ehTrjUmvc2iy-7meRBdXEBspCmXmN-pXYWwkfyHiwlJsIoph32hQSsQRqjT_vyfxww_o6oVv2YfK9Wp_p_e20qigu4DZP7iucaYUXcOgs0SI2WqqeqJRNJcvC81R0sh46d8TiEzc6aA7ga7ajuqePmnjo4WNg3Gk2eoV8Gl2RHyxTETDP3lWBdd2wEzBWJopAxcbv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسما اعلام شد که ‏برداشت ریالی از ۵صرافی نوبیتکس، رمزینکس، بیت پین، تترلند، ارزینجا تا پنجشنبه ساعت ۱۶ متوقف شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/152458" target="_blank">📅 14:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز: سامانه هشدار عربستان پیش از حملات به فرودگاه ریاض از کار افتاده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/152457" target="_blank">📅 13:51 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
