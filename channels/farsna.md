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
<img src="https://cdn4.telesco.pe/file/uh8VAOUqO5UZccEO-9qIfZHYBoTPfMYHN9NcoKX-gFSrGEYth1etg3a9Nldcg90u9Br0I3Suq_SCFeSONIgt7P6_QaVdP0JBKvN_iqjHRaA2Z6Wmo7tBlLAFWzn1F78cifs7UHCD_A74viOZeXKZZIuBxgbulqEhqlW_qpzUgJse9gyfckVmdMRpVSiZ8-7ubVhznpN0apkU7MNX483kRXnV2hbJzTd2sK-6637IA5GOn6wbpCCbGsV47ZzcZ6cZseONfOStlfTabdBdYG-k2J55qM7jw9L9tGtRZhHyKdLKL-ejCdLE-_UHHttJGySuaoE0FbDmHIy8Mp4GO6o_rQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-460143">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمنان با جنگ، محاصره و تحریم به‌دنبال ایجاد اختلاف، شکاف و آشوب در داخل کشور هستند و ما نیز با تکیه بر وحدت، هم‌افزایی و انسجام ملی، این نقشه‌ها را خنثی خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 44 · <a href="https://t.me/farsna/460143" target="_blank">📅 20:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twlI9ipuQ0Q8kUAEX3FUEAQrb8tLl3ndowuh4tE8W3DuoHMOqff7wAPYQnnKBBtiql6ILJo_kOXW9dDvoiXxP1Qkuji5L6SBqlrb-UV2g0zD99TyioNVSyWrzXiPLhpIitT5ONSd4gOyi9W5p-gRQmQgg5M7hcPcIJnULBmbmAFu5gGDnFjMnxN9KNAvUskQPymu1EBWLd8eZygJbc46ztcyzBilvs3T_lvNqo0aaj9-5MC91DtSjeWU02DnUR9i1SaOFUccWp7nqYphxOLXC29fXW3bW-tDSj_81fpPc1YAkr3vyj_OuzjVTTzv2PYpr84rFyCeJiR5JgcMzXARjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل عاشقی مرال‌ها؛ جنگل، مهمان اضافه نمی‌پذیرد
🔹
همزمان با نزدیک شدن فصل گاوبانگی، تبلیغ تورهای طبیعت‌گردی برای تماشای مرال‌ها در فضای مجازی افزایش یافته است اما معاون محیط زیست طبیعی و تنوع زیستی سازمان حفاظت محیط زیست، امروز اعلام کرد برگزاری هرگونه تور گاوبانگی ممنوع است.
🔹
فصل گاوبانگی یکی از حساس‌ترین دوره‌های زیستی مرال‌هاست که از اواسط شهریور تا اواخر مهر، همزمان با فصل جفت‌گیری این گوزن‌ها، ادامه دارد. در این دوره، گوزن‌های نر برای تعیین قلمرو با یکدیگر رقابت می‌کنند و با سر دادن بانگی شبیه صدای گاو، ماده‌ها را به قلمرو خود فرا می‌خوانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/farsna/460142" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460141">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQzn3bJfwEGK0VqewjNlwL405gCKtxHsGJ8Mbk2YHanDW_-e2mET7gBGvF_NxbvUjLq8FfHh1k26SGRlRkcIQsPGUFcT8joCLuUYyTKAZ81zwXNBHw30xtulgQ0K-Lgl-5g3c1UP-NKrCH5B__HMLYtJ13zKApCJyNQUdfUmRtRQvKV2ABCJvK52CwBQo92QziH819eUonrWRQ_HuzXaz5TjY7N0kI-rTkNe1eJx1V9J1HeYvQpEeB6su9CX-T7iFUlLRTbskzxf0E-GbnnrogF7jLiwGtuax2bIcUEPACC9B_fd61zwfTaE2R7EV883ZXJb_ivZTfBAA0jibRAInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ایران از ایدهٔ چین برای ایجاد یک معماری امنیتی جدید در منطقه استقبال می‌کند
🔹
نمایندهٔ ویژهٔ جمهوری اسلامی ایران در امور چین: تأکید چین بر تقویت امنیت مشترک، بازتاب‌دهنده اصلی است که ایران نیز سال‌هاست بر آن تأکید داشته است.
🔹
کشورهای منطقه باید آیندهٔ خود را با دستان خود رقم بزنند و ثبات واقعی تنها از طریق ایجاد یک معماری امنیتی جدید و بومی در منطقه امکان‌پذیر است. ایران آماده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/460141" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460140">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/460140" target="_blank">📅 20:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460138">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh53ER9YxqL75lBr7k_CSagnCLZ_52GaXB31fyb87oEhwZTH21qgV52OJMu22NYkEHJWtnbhN3NrWKSmZZXD1k4dePjGmCentvlfAyMCkQP9zlqAZoeRs5FkAkxlFXE_bIRRAE5xQiwV6CDr59FwuFws-wXl62AtnjH1jjcnkFAG9ItF8rHHZXzyP7tSvLtB39WzvByg0J8ARoS3VJjZwoHZrXZro6FyamU_UDZw4bryOkc-JOWTSwgXo27w77RyEjmVf5KFRozlXqDkZUjp3_gKUN-Jlgv0jB2Y3o5gb_6RWP9T_QNCzNeyD06_viPuCEhlYZ-PUgH5KeIecoBevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت ترامپ از شدت گرفتن انتقادها از او بابت جنگ علیه ایران
ترامپ در شبکه اجتماعی تروث سوشال نوشت:
«دیوانه‌های افراطیِ چپ‌گرا، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ با ایران
شکست بخوریم
تا اینکه رئیس‌جمهور دونالد جی. ترامپ این جنگ را برای آمریکا به پیروزی برساند.
به عبارت دیگر، آنها ترجیح می‌دهند ما ببازیم تا اینکه ما برنده شویم! اینها آدم‌های واقعاً بیماری هستند که به نوع شدیدی از
سندرم
TDS مبتلا هستند؛ چیزی که گاهی از آن با عنوان سندروم جنون ترامپ یاد می‌شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/460138" target="_blank">📅 20:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460137">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
منابع عربی از حملهٔ موشکی به اهداف آمریکایی در شمال اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/460137" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460130">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_9GJIhheXr9gLpFITpOC7IiAjBgo9SDMyCIDrI2jWzgLdJGF3oUWsdpx_v4cRPLP3zwzQbOlHSrlbAGuRczKEdrfw23LxE2xToeJGF0n9yo_YjCs_CKU-8c60ZU2tuZFUwRubMHAuRRLrapQKhmw5sLOYsIj948D1USZ4W6YrOD_Wcf0AHgmHQPOEdpaYgA6iQDZ4LIiaeWXr4zWOtYw50De5hYgmz8QDwMGBrOIthoyD5uY6kXpsf92j3ldia16qNEpMjhRqJzGdWAVct9lYCDQS38ngvWhNct0_ySXmflfXKgkaHXCef6tj9PRKfsD7rD4-Xviao3WCKv1fvXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTedLZqt1czJ5uTBRBUdohzKqldjECxBa3NSJC8WzhKJxFccn6vC9xCezUsqCDXLTDT1QcoVZOGHM4q1eAce2H--MwlyxNJpKphqNOLtVx19wWpNySbuXtMSD2dIGIYaLxcwngz7-lbzUegWuhfd_HXkU6gwYBcvyCcQek9OPdP_ZF8fYiLuGT06uH_ponWT1kS7JSjDxR8gpqYacjlht2eJ3N6LCS7sTcv3tH3rPnrnJ2h3g0zhpJU6v6GXLxaHqPvV85Flp9Ty5iw0rZZj-PtibsNXmVbSoBN5hJnsVPwvr9-B_ziHtjm0Vk2LlStuFCJICnoHX7U0-6hkcoJKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6BE9oBjzwCU1XwO2829_tVhahzyqCUayy5Lt7Ch-Az769gb4dbtObNwuEDc8OkI1kdDg04XnHo_HPXtugrrF1qC2tGxYipZ1MKccl496gV9-nnDORDBDLgk6C7_wwqasdOgPdgYvDl1MtFcDEw1MMBGGGOFzQAWh2aYfimqzmwhEdmd-gJW-hRLS-azXTdK_Uqy4JhayEX034Pvpf-26n9dUSMgNjk6zIu5aw59x1V5vr3Yon9r24SLs3HUIhdrCSlS-zl_eg2w3a5zO0VQRVqr-gMb2SfGIOMmPmG4kZQme7v1Y22BsZKPQU_s8PktDsQR3OX6GODOGD8BAu4H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4UpnRdmMdrtdR2Dr0Noj02jm82Rcbyyyx9TaPWwPjtQunHTcndE3VdmQ3ds4n76fyhf47yxPzpzAisNTlbPfxO8e9-m_dvT5_D2T3L4-flZYrubo0gsNDl4a2dnsEef-573JCoFaTFjqVDCKE7Fz7kqgWPK8BSo12dZy6Z-cxRt6zXKlsnUUwHXJy5Pv7SJjkiMVLfzRKzZa-UMVancsh8yvHPG29qMjFL0fC2ZRZ4Yt1wLAboERvwcLT9pNMVQX8AXsgoyUefzhMBNcpGeS5a0ajnK5b8FdYHWZBzU0WRRnyU4AgD_POdrFlYyDLvwjsjfM0VSFgNQOE8NeAPsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rM0nU0yarh8pl1xG-v8AECKK0HJQaZxDRWNJcEYNeg74sqWqGnc7dyybQsk2u0OHwhlyJuNvGbMzDti0PuwtDOwqNZoplwtaRzyeVF6ubAxix-AHNvp-cola_fBdE0ScuYv54-oA_Aw5MLuqc2JXzSCOYD6x0pEKbphei_DuNyPaneDjqBg1mqSwMnvL0ASJlEDyBZTNI-uY6bbBmrFpwD9WZLsAjKpBUxvBCcxjRniqGNx_DKKKeQyYM_Vnk6i6gTg87KboZum5Ycm4p_iokFBd2WRXdwP7E-dSeUKFxBiq8GfTBRaevci_Uq_sEjURr39KCeuvtz7DCIhfzE9EGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMTgrRkh0GEdcq_g35z2Kebk8cvIcKfXsKpwqQF6nWOEN_pU7fGvA-LVLcJoc9Q60nSZby4baJQ9afN7MwG22BP-unetABFM5XhmsUqRzFaJV2piT-2U5WxndWfONEYB4JwLkXTN4wcedZ2PDg-1CUw74PEr1DVsqPzZCdpxA5jS7ztFQ6Y7irsPcSY2PuWI9uDCNWA-rnLvYt4Zf03PQMfyfpoIgTlEbtvWFjxrwjXd6VPkjS04RdVxdoObnC5ynLYcRZoGH3lCTT4wIgB29VY_v8JVxr4OHP_jczf98YPCsGXcxjokGnm_C7VCJNX2C4hr_4sW1GCTF5ueO-x6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cib0uowCP8mvdqYhvqvhr95h_R4h6T_uUm64uICtbxn7cqeCbLDbr8_daiN9NsrljN9B0u2k9uTbqFNwZt50CjV9SUuAQ7DqipjBB0InUuit_kl80FlZ0OjaQszKH3sOoRSDAXXNFgg57TIVvdLkG5NgkqFCbnCXE-PwC4FQb2zN8LNp47PXPadCjHLNqtF3Xv_qPl6GVXgYO_TbPYyKjgMTNupNz9JTY6kA03xw5JjrE1OF1j83AW124K-sDszF9HmzMBvitfscLPBFgaxllCld068Sgx786CQyOs92sbPSBaHpoTL7fqnRz6Pny3u7XcCvEVhm8n0bOV6SBld8fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت رزمی در «میدان‌یار» کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/460130" target="_blank">📅 20:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdW2mm1KKcCExXMbViptcGHT_w0xHpIOQ3Y5HhdR6457tjejAhv48DH_3z37HLvGXCXm6Ymd-D1JQzfMWU9RPN-pxaXTzMDtSY_1k-7lNmzZggn85yev3gCxAoqQJs89hh7SyC22b2BeX1Y6tnlZJS7LuUD0Z67VQ-dvTPv5onrMw5DbYDeySNQ1s3LI7LPFuRO69pNUHa9AC6JXg4TEOuxuzkJdfUU3GxsTojjBbfoma9MxGgf8ENlqusE5WiboaYAuBDT4KsyKYJ_qFWJwuNiupmu1olT_gCsslmyyfatnc1m-cwv976SZI3fQ-bhkobeMBoo6bazpSeTxKmCq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1ozs6afKjepdSYc1IdyaqH4ZUXJNjsiMQXjJVgwoNaGWJODQsJzkPVh0L6PKZWdHd8butONRm9b_Lynw5l84OK1fuk_JCK3P3tsvh9S_JZlnuGU1cfsp3nOVW1vQ2_jGX6JIJp5olRiR7ss8ta_MwjN8ZOUZvZdQf8HKkOYm12rlmgfURW3UsWG0ZiKuX9ZWh1OK_PnNLSWAX4cumpuWsTtbTOg4Qs5Hkljl4FW76P0BFrQcW8Fr8ZkIVuE6-tPICZ64DTLTm5V902W_iWV_OzdRDaj5ooLMdvmfrpPSCcPb3J7nvPF9aKxHZ0ZpLjdmk8dRSUmXEhafEDUx9eCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU2SCSeSGJ9Ff-MHW8wZW67B4YZLjDfA6J7DlwmHQxBAXL5rqMKHY2eGrgQqbbgdsV8sFLNrte36ayAmBh4CunvG0D-KNrkKZQi23M36mXUNxomBRhOW8ENyMqPwWTG10woDKxfyKZ9rylqLKBwuiZ0mZqHfn9--KccISqjklm-Yhkz1ADzq8qPBdtwLWvnUiILKE0D41cL6aEi5br4Hs7H0tTBQuAQ5SxxKHOKN_t5pZfHGv5Pkg_wsbVU9SAyphkFG2qgsRmOs92WlpwvadbF9XcA27OVMMGsVptjVreWOCFoPia8hJ4i95tNG5sDPfBXEPIx5k2Dtd2VRjfRAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gskPBEfYzOBp25Ma5WPcQMHEygxhafDjwecilBUp_GySb2vNqHv78b5dugTwZtinGj6OsTYHXxiYc3t2b5FtDW926yz17YM3xWh7jPN-qd8BKE5pXOm8IkSjG3Vr7THNKJ1x-7RqLFoMRuFaK92CoTae-AJCl9O89Iu_QO0UgcLPiN4dkhZ-Yf7DnDaToh1WTG7EDDUOS5iaCIXH2BDoSkvCULJ2uQskgNOUZ7ZvotVvrVCLStuYTaFWlH7e9nQeGrgwYBp-bSPkaeV0nFDWxynLZcobeeUd49x46eWmFLhQxGv0jUiddmZkNB7pVwaguHSpg95h6tXD3lJJTiP1fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تمدید بسته‌های ایرانسل اجباری شد؟
🔹
اگر در روزهای اخیر بستهٔ اینترنت ایرانسل‌تان بدون اقدام شما تمدید شده، دلیلش رویهٔ جدید ایرانسل در فعال‌کردن تمدید خودکار بسته‌هاست؛ رویه‌ای که باعث شده کاربر برای جلوگیری از تمدید، خودش دست به کار شود.
🔹
پیش از این، هنگام خرید بسته، گزینهٔ «تمدید خودکار» به‌صورت پیش‌فرض فعال نبود؛ اما حالا در اغلب بسته‌های اینترنتی، این گزینه هنگام خرید به‌طور پیش‌فرض فعال است و اگر دقت نکنید تمدید خودکار آن را هم انتخاب خواهید کرد.
🔹
در سیم‌کارت‌های دائمی، ماجرا حتی متفاوت‌تر است؛ هنگام خرید برخی بسته‌ها اساساً گزینه‌ای برای برداشتن تیک تمدید خودکار وجود ندارد و بسته با قابلیت تمدید خودکار ارائه می‌شود.
🔹
ایرانسل در پیامک‌های مربوط به حجم باقی‌ماندهٔ بسته نیز اعلام کرده بسته‌های ۵۰۰ مگابایت و بیشتر، با رسیدن حجم باقی‌مانده به ۵۰ مگابایت یا رسیدن تاریخ انقضا، به‌طور خودکار تمدید می‌شود.
🔹
در نتیجه، اگر حواستان به غیرفعال‌کردن تمدید خودکار نباشد، بسته می‌تواند دوباره و حتی چندباره تمدید شود؛ هزینهٔ آن نیز بسته به نوع سیم‌کارت، از شارژ کسر یا در قبض شما محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/460126" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1869c43e13.mp4?token=Wy5H8O9Udi1idl8PnNbacI7NTI07BRyKtmyLNNrGjjsCLkalUT7SmUDMeSoGhh6CP7Imki-Ji2zB89Qd6t-TETYHBAMOYsXKElyLjtzjaHOupHnkIzRMt9EU8g47iNXsO92MXSE2LVjSqGiWJAU_Gox1T4hAaDg4t5PC8yQBhbm8veDXA7xFEQSv_an7dMVcaykUTznX-5iMwun-aDQtkiHQIubuxsarRl1iBcFC5j2hRKieKZXw_JCaX7lSKh5icdXwpYobeCpQbtAShPPdbgb9g5siOmUmKi07nmHM7kJGymCscwIGqixd1hX5UO9Sjy4Dpdr2RdXw7NDB07vEQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1869c43e13.mp4?token=Wy5H8O9Udi1idl8PnNbacI7NTI07BRyKtmyLNNrGjjsCLkalUT7SmUDMeSoGhh6CP7Imki-Ji2zB89Qd6t-TETYHBAMOYsXKElyLjtzjaHOupHnkIzRMt9EU8g47iNXsO92MXSE2LVjSqGiWJAU_Gox1T4hAaDg4t5PC8yQBhbm8veDXA7xFEQSv_an7dMVcaykUTznX-5iMwun-aDQtkiHQIubuxsarRl1iBcFC5j2hRKieKZXw_JCaX7lSKh5icdXwpYobeCpQbtAShPPdbgb9g5siOmUmKi07nmHM7kJGymCscwIGqixd1hX5UO9Sjy4Dpdr2RdXw7NDB07vEQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رئیس‌جمهور در حوادث دی‌ماه گفت اجازه نمی‌دهم اعتراضات به حق مردم توسط بیگانگان مصادره شود  @Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/460125" target="_blank">📅 20:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d9f21b8c.mp4?token=eQHcDocq-LgpvA2FcOGbQsRGCCq8EmqTG1Ip0DIlGvuijaVhJ9JRoRK1W7uEp8CsawpMxdQNp5bOtzN4YmlIAHLyWbE8NOQPESInAKjsvazEAhz8Ni1KlDQhlpqz1wTuyWJrudRUO072vl7FD5xzvvnsnBJzo3ICg8ndLjIbCOPfAzSwAphtmHE9CSATbGTYS_4ykrAad5ckpCE4HGbkifiyUpDI26yc0lYJ_IJ8w3AnaDFvetgDkntLJA1u1T-oucowFKwiXcj2O5OG9_yRlUXUZc5MMblEmKJytMJIgNw5Oun741-UukhAh0DJKLSGSzrPVQDiyrvPs9tk5XpZ5QRS76wGEOEBAcU833NrtS3bBDrXNJqjvjSvnR6AdYA6rZSHdACDB9WdNqBTqd6gcMyYFkF8ITPQfjFs0R5yCbUXQp-VCiEA3-er7wvtiPGj8Q16R8wt-6iFnyoMqY9CjCGi4EP5njODOtfMxUDZ64mO-DUPJG2ruNBvT8aimD2_GzjNJhkMX7b8g_S80zUHlG7yY6t-tU0BfQx4-gIYXjDTnMBJq9unQMi_pehId9vD6g5Q8DxosLrqotwTePhvkc5s_6KDUJEJsKz3E-edFFpuScxyzwLnVpdKvLXHBscOwXpfWqTy2lKa0dq-_NGu_OueC8wDwT8SfFQ9sEJvKwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d9f21b8c.mp4?token=eQHcDocq-LgpvA2FcOGbQsRGCCq8EmqTG1Ip0DIlGvuijaVhJ9JRoRK1W7uEp8CsawpMxdQNp5bOtzN4YmlIAHLyWbE8NOQPESInAKjsvazEAhz8Ni1KlDQhlpqz1wTuyWJrudRUO072vl7FD5xzvvnsnBJzo3ICg8ndLjIbCOPfAzSwAphtmHE9CSATbGTYS_4ykrAad5ckpCE4HGbkifiyUpDI26yc0lYJ_IJ8w3AnaDFvetgDkntLJA1u1T-oucowFKwiXcj2O5OG9_yRlUXUZc5MMblEmKJytMJIgNw5Oun741-UukhAh0DJKLSGSzrPVQDiyrvPs9tk5XpZ5QRS76wGEOEBAcU833NrtS3bBDrXNJqjvjSvnR6AdYA6rZSHdACDB9WdNqBTqd6gcMyYFkF8ITPQfjFs0R5yCbUXQp-VCiEA3-er7wvtiPGj8Q16R8wt-6iFnyoMqY9CjCGi4EP5njODOtfMxUDZ64mO-DUPJG2ruNBvT8aimD2_GzjNJhkMX7b8g_S80zUHlG7yY6t-tU0BfQx4-gIYXjDTnMBJq9unQMi_pehId9vD6g5Q8DxosLrqotwTePhvkc5s_6KDUJEJsKz3E-edFFpuScxyzwLnVpdKvLXHBscOwXpfWqTy2lKa0dq-_NGu_OueC8wDwT8SfFQ9sEJvKwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع باشکوه مردم دیّر با ۳ شهید حملۀ آمریکای جنایتکار
🔹
پیکر ۳ شهید بسیجی شهرستان دیّر که در حملۀ تروریستی آمریکا به جزیرۀ لاوان به شهادت رسیدند، عصر امروز تشییع و به خاک سپرده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/460120" target="_blank">📅 19:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460119">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfc862078.mp4?token=ntvxe8EC5N-4mrWRbNWrpdVxu48Gthv3lE0p2sdGz3PxiR3lZQxaj8sYN0j2o7hChXyDH3VP4gzuYpab7ZivJQtlrXk8RimLtnxitEvpwVXePOEsZjepwfTGb6VTyb7rh6u2hZIQs6wjnCrqckRQbn3tlUSCr7TWwN43j9wKGypb7EnYfnQNszutjrW5EZP6xUAp-OEQxV7id1KVwkaD2eKn9bZyGRLgsPf2Shfuwddk3eO7_hkIkOUvBXTR40JGC0iM6nGfz9LSQWm-VlSgYFZLtWNvNhfxbyGO4qz6grItjM61bUuO7KdcOEYowx8nQoZh9wQn3zEuBv6-eTTjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfc862078.mp4?token=ntvxe8EC5N-4mrWRbNWrpdVxu48Gthv3lE0p2sdGz3PxiR3lZQxaj8sYN0j2o7hChXyDH3VP4gzuYpab7ZivJQtlrXk8RimLtnxitEvpwVXePOEsZjepwfTGb6VTyb7rh6u2hZIQs6wjnCrqckRQbn3tlUSCr7TWwN43j9wKGypb7EnYfnQNszutjrW5EZP6xUAp-OEQxV7id1KVwkaD2eKn9bZyGRLgsPf2Shfuwddk3eO7_hkIkOUvBXTR40JGC0iM6nGfz9LSQWm-VlSgYFZLtWNvNhfxbyGO4qz6grItjM61bUuO7KdcOEYowx8nQoZh9wQn3zEuBv6-eTTjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رئیس‌جمهور در حوادث دی‌ماه گفت اجازه نمی‌دهم اعتراضات به حق مردم توسط بیگانگان مصادره شود
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/460119" target="_blank">📅 19:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460118">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-text">سهمی در لبخند دانش‌آموزان نیازمند داشته باشیم
🔹
مخاطبان «فارس من» با نزدیک شدن به آغاز سال تحصیلی، خواستار برپایی ایستگاه‌های جمع‌آوری کمک‌های مردمی در میادین، تجمعات شبانه و نقاط پرتردد شهرها شدند تا خیرین و مردم بتوانند در تأمین لوازم‌التحریر دانش‌آموزان کم‌برخوردار مشارکت کنند.
🔹
ثبت‌کنندگان این پویش تأکید دارند با همکاری دستگاه‌های مسئول و گروه‌های مردمی، زمینه مشارکت عمومی فراهم شود تا هیچ دانش‌آموزی به دلیل مشکلات مالی، آغاز سال تحصیلی را با کمبود لوازم ضروری آموزشی تجربه نکند.
🎉
برای حمایت از این پویش
اینجا
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/460118" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460117">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ec2c47be.mp4?token=KWo73aes9XBRp2f5YJhLzlfxSzXXBS50xrbqLn5mt5SmGmixS3XJFdukOcF3CGbF8oX5nWenp3o1BDZ0dPvQuLVo7rk9qg297TSPBcnFnrJGhJjb3mYii3gctUKU59K8pBYkvvdBgfyEmMfc0bkcO8yK94GmNYhVNzL0GXfkFIAbrqrUq2whccDmFN-MEjLQ_tM34LPoFgcEZtVFjoeK5Yc6NM8qJCgLhp_D7bwXneCBwClMxdwyHyLRmmo8lOAYISwq0ip2KxVpLs5cS7KXCdrkBRKNlCn0TlLTt42x8vl4ATmgiT1YhjUSM3rq6JqBEDdMg6zPhBOJdmFqhiszDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ec2c47be.mp4?token=KWo73aes9XBRp2f5YJhLzlfxSzXXBS50xrbqLn5mt5SmGmixS3XJFdukOcF3CGbF8oX5nWenp3o1BDZ0dPvQuLVo7rk9qg297TSPBcnFnrJGhJjb3mYii3gctUKU59K8pBYkvvdBgfyEmMfc0bkcO8yK94GmNYhVNzL0GXfkFIAbrqrUq2whccDmFN-MEjLQ_tM34LPoFgcEZtVFjoeK5Yc6NM8qJCgLhp_D7bwXneCBwClMxdwyHyLRmmo8lOAYISwq0ip2KxVpLs5cS7KXCdrkBRKNlCn0TlLTt42x8vl4ATmgiT1YhjUSM3rq6JqBEDdMg6zPhBOJdmFqhiszDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین نقاره‌ها به‌مناسبت سالروز ورود حضرت معصومه(س) به قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/460117" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460116">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آتش‌سوزی دو کارگاه بافندگی در تهران
🔹
سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان مرکز پایتخت مربوط به حریق دو کارگاه بافندگی در کوچه برلن است.
🔹
آتش‌نشانان در محل حضور دارند و در حال اطفای حریق هستند.
🔹
تاکنون مصدومی در این حادثه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/460116" target="_blank">📅 19:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460115">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbaf95122.mp4?token=sLnPOFCDTz4IyHfb8nOxuRODyA1bE4k2HMTRxRMKvVKQzIvVDYrsvDw6eP1kQrWsuTfU0vOOVDcK6ftsXrmmAxXPSeIGyyYkfP7iDP_g3upgzitCFEkyq1igFan6NKDEXfgDGmiP3rm9sfV9hCe2uF6KE1FiRVQzX2VoqRYQfvexUlMde1374BwjdV0Lr1PQNLdW_y84RXn_3QtnVU5UypgqXsr5gearQfN_tblR5YD2u8ELJy9ZH9eo4Kz8b3BpjSaBBCKrqtvE4AdGmBw0BvwWUPdyY5oBhaQuN2v3GJ3aI4HySJkUur7n1ngg5XFVi_cQ2JRJaT7mRgFwOZX0qTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbaf95122.mp4?token=sLnPOFCDTz4IyHfb8nOxuRODyA1bE4k2HMTRxRMKvVKQzIvVDYrsvDw6eP1kQrWsuTfU0vOOVDcK6ftsXrmmAxXPSeIGyyYkfP7iDP_g3upgzitCFEkyq1igFan6NKDEXfgDGmiP3rm9sfV9hCe2uF6KE1FiRVQzX2VoqRYQfvexUlMde1374BwjdV0Lr1PQNLdW_y84RXn_3QtnVU5UypgqXsr5gearQfN_tblR5YD2u8ELJy9ZH9eo4Kz8b3BpjSaBBCKrqtvE4AdGmBw0BvwWUPdyY5oBhaQuN2v3GJ3aI4HySJkUur7n1ngg5XFVi_cQ2JRJaT7mRgFwOZX0qTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع ۲ شهید حملۀ تروریستی آمریکا در کرمانشاه
🔹
پیکر مطهر شهیدان رضا محمدی و شهرام جعفری که در پی حمله هوایی تروریست‌های آمریکایی در شامگاه ۱۰ شهریورماه به درجه رفیع شهادت نائل آمده بودند در کرمانشاه تشییع و دفن شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/460115" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460114">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F428kHqpTJgjWQVR5H0KRdUouZ6jZPjk3Y8Mx3rIrhlzQZiPsNO34XU0OBafYn2NZ3Y8og2ybtYX0Brjeypkv38AKOFUFTVKxxZ94oYbBnBD1TMigQ12sWetD-2BQKTX3Lt5J-qtAkXSbsKxvLDGuTelZC7cGZQANOljmf11sVRPp6jDoGcjKyKEyO-tEW9xyQ79hQYnbycPvRc3NHgCivh_5ZAie9lAPBKnIQDdurdHNjPPmDZdAUZh_OlxWmdICNiXPKDlTnIeU9maqHmu4ccsiBz3Ef_KWRL1kkb0cc6XUtA9w10kLiSt9xV29Anpi0WS4j0ydB7HnMlBShQRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های لبنان: ارتش اشغالگر اسرائیل به یک نقطه در شهرک المنصوری در جنوب لبنان حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/460114" target="_blank">📅 18:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460113">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eee7887d1.mp4?token=TBznAoYcuOfL-RnB3Uc0XnaWzCfRn1pFN6zg4m_RpUyjTZsViS9Ft5Kc9VeW1Th6V3i6do4lICLsqIezwEGmcozTTYHFrr3q3qw5qnxuP4le6SQm3_BiR2YWj3BO2S_Gy2M5U9etnVnuFLqIbBumcsVpyLC2OWNqivBpG8JgJ4mFD7dZNkNpBJL-5ejOP4WI8ohPluu7Mg6E6t1eJ9jWZ6UIS8NG5wlhDce_WoHQ_2wywulJmRXDSUav0ym9J63g7e8hJxsFHrGMMOtKlFxl61S1agDvbZhzkfvefaw-fzvnQ2muWkfacI8gvP6NG9sXl7YkcyeD__hqRqgGLB200A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eee7887d1.mp4?token=TBznAoYcuOfL-RnB3Uc0XnaWzCfRn1pFN6zg4m_RpUyjTZsViS9Ft5Kc9VeW1Th6V3i6do4lICLsqIezwEGmcozTTYHFrr3q3qw5qnxuP4le6SQm3_BiR2YWj3BO2S_Gy2M5U9etnVnuFLqIbBumcsVpyLC2OWNqivBpG8JgJ4mFD7dZNkNpBJL-5ejOP4WI8ohPluu7Mg6E6t1eJ9jWZ6UIS8NG5wlhDce_WoHQ_2wywulJmRXDSUav0ym9J63g7e8hJxsFHrGMMOtKlFxl61S1agDvbZhzkfvefaw-fzvnQ2muWkfacI8gvP6NG9sXl7YkcyeD__hqRqgGLB200A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قیمت نفت از ۹۴ دلار عبور کرد  @Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/460113" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBaz9A-S3eLXxb1GZfUGvO_4FMoHqh84In9O2E36WNVgsFswbRZEwIhcBrpsnAYYy9kIaigGLp0odp-JYGZ63zSE5Ad5EYEBJYh63g0JLI1WKvqSqRuIo0skBAD1bIuu0mghr7gASgLQGv-HffJao-vdYzdbv45bLzeV4b_8pczpwZdOJEFuIx2OSpIHUVY379JtNr5YxoEqU3YrElCuCZrBP2R1OJZw9WkpKaYhw8eKqqTuQk5ZNebpl7_12hk3jZd4xMABkHMxNVR2119LvIkBVRD43Rr1KFvA7-42o4JCIP0S70rb_aSlEF8bpMsi0g4varrW4go8xECquyTdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7Ufa0Ps_VtE3e5Xya04svDqlBFoMtw9y9qbZbTDw7dqsedTXECJlvF8KkCYFkUWi16SnMlVAt8vrnKFHsSu0HUM-bqUZ00bslVJRjD_fuK3h6rYVc7Rr4Tfm2OCtGZ4_GfgyAtmZ6NM2iJKWre_R9ibNPzsY9eilOFqIfaO3iG8OT7qiwndjpQQYLAyN4eHTs-UxDessntUUQozZxJzNXgfJehsoTEet6NxVzWX0Gr0SKWL1dnvzcp3wqe6d66YZY1k2L8psk3rI-ZFRgWoK7nTPTFfI5KBGVle8NPCnpLCmUMR5H0CXSXj0aZLheGq_b2DDQArToKSM8woZNTMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gO4n8Zb7mzw6fanQHjd-AT7BAIPYb2yrO8Xo6dCdjGFxjJDy3ji98ElGJpGPVJCwAKfRQycgIATCJ9ebAITCYUCX_oZzJFcnyNYOl6AE5WDhlc4jyIJwAvu68ckCl-xn5ZjlPRCVwYxSWKJQe48YIpTFodniI7khHMOo3BSEjB5YPt9mUEjMy6OM5FAHY4zIdDMzzs75MjlA818jgnQTAXRUNkErTl0t_sob_Ctd0PnucjtbinsIyUU6yE03l4PZY89gR5sM20K7YcKA7Oky6tj3jGKU1qZ5F5Fo7SnWQ4Gn6ozCGjinlIIwfgNo02ZD560n7tJGFrAgR7htNnpkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbBXyYieGIpqTuQ--bH8dSNJdOa_f0FfmiTxFRUIBRebCfwhECo9OljdUd_aeN_DCM4oUEnQ81L3A_pY6MssX9FwPJP-0zvG4C5mDIW9J6owPNMaZkDiEZWL4VbcdhLLlz2YvscI1B7FBRlHvRagZD176snTqUqqLbioRF0oHggqYNduaR-JCxZMHPhiGF6J2ycHXpxUNChkaDph9QukvKyGRwCoqngMaiDcsrmrrhFg-XXBv0-LpH7lUFXH-X26Pua_hNdzKFdZ2mzsLEQQSzow6HRFpJgegl3Vsf8V0g7A-WK9JTUFm3okvJVHOZLgQ95ZQ5KS8pz8PJBuuNSVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHF3N030Dkel17hyBQ0BVHFiytsiZ3REBzn7m_iEfzcNzOJXw4thh-sqWGwIU1Qos2PhttXkHRl7vbJhWGgzGaRSHu33EeM1d2SSWCTEZWsLhITesHhsH4D0jDXM3tauDk9BSpWBvhV9yQ4P_brglOtgaZ3kmT9JlxGAj9KvVR_eWl3rkemJvzLGmbUhgUbL47oaxHl3od2w9bYsOS9VN6pqnSv5Y9nyHT-d2WuAAdOE0Wf9jN4wITIH3M_aEPX-Yr0wCQ8Ea4ERYgG4gIalX_YnmAmk9C9_I92LZOwKewqJ3E-aMYu5mMroK4a6buN3SrHeEvymiwlsoyhhiN5fjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
از یاد نمی‌روی که نامت زنده‌ است، ای پیکر آرمیده در دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/460108" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ad405b00.mp4?token=tcca7OSG1Vcl3XFEt9yk2orY6kw7FkgkKhXhGMk6jnj1bFvcB7D4-KGKS27kgGQ_8Qq_ClwOaayTOu1YTutyIyXHM3crZRfhkPr9QMoxXXQcnpun0ODYKrPy_yzu-g3pN_yeAikbp4WaljMr9HKxZBoSnmTXJaSQvMnnUMK2op7oFaNMddzkC5ywOVtT07V6JA9xx6oseePsLRNBgcV6ERr3yMGm_Jzpi-r2m5E1CATEcD_8UeYrd6Weu5ufOlFL-WYI2M8DGvHl8KuQENt1mc2v53y-1gTmy3JaXjoHsX4BVA_dxH4QUd8tLACLmR42THSjSi_WXhLKIqCOfiK9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ad405b00.mp4?token=tcca7OSG1Vcl3XFEt9yk2orY6kw7FkgkKhXhGMk6jnj1bFvcB7D4-KGKS27kgGQ_8Qq_ClwOaayTOu1YTutyIyXHM3crZRfhkPr9QMoxXXQcnpun0ODYKrPy_yzu-g3pN_yeAikbp4WaljMr9HKxZBoSnmTXJaSQvMnnUMK2op7oFaNMddzkC5ywOVtT07V6JA9xx6oseePsLRNBgcV6ERr3yMGm_Jzpi-r2m5E1CATEcD_8UeYrd6Weu5ufOlFL-WYI2M8DGvHl8KuQENt1mc2v53y-1gTmy3JaXjoHsX4BVA_dxH4QUd8tLACLmR42THSjSi_WXhLKIqCOfiK9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای:‌ آمریکا دنبال چاره برای خارج شدن از باتلاقی است که خودش برای خودش ساخته است
🔹
آمریکا و اسرائیل در سال گذشته و امسال همه توان و امکانشان را گذاشتند تا جنگ ظالمانه و غیرقانونی را بر ایران تحمیل کنند.
🔹
ایران پایداری و استقامت کرده است و آمریکا به هیچ یک از اهداف خود نرسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/460107" target="_blank">📅 18:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فردا احتمال شنیده‌شدن صدای انفجار در قشم وجود دارد
🔹
فرماندار قشم از عملیات انهدام کنترل‌شده مهمات عمل‌نکرده دشمن در برخی نقاط این شهرستان در روز شنبه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/460106" target="_blank">📅 18:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVVD1UThQ9HhHBfg4kYBaqZ-KdoTB7gST19CWuW_FnHOHmSDywWmeT_zYu2ZECRPJLDk50H65AWlrDSaRttcFg0_SFcAniK1n0ytG8vDHg6YehX50pT_J5nIc7oBYXCr3NROQhAoDB70iPCJnaO9JWSdxeAvHmW_XeNNS87gcotgqcGnIQ4wGzQu0oUtwcE4G8D1XNifu5suBFpU72blgd0qvlwBQsLRuvFDnQ_bZWsGmDbl55gUdLqmqmIFzx7wYSda1rUdABPPvb_kBaAO6O6E-Y95lyBxgwnamtEdwq02Kum1blHKliikhY5y-071NV-sUYko5Ykc9rmWV6s40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: تلاش آمریکا و اروپا برای ارجاع پرونده هسته‌ای ایران به شورای امنیت
🔹
خبرگزاری رویترز امروز به نقل از دیپلمات‌ها گزارش داد که آمریکا به همراه سه کشور اروپایی موسوم به تروئیکا شامل انگلیس، فرانسه و آلمان در تلاش‌ هستند شورای حکام آژانس را در نشست هفتۀ آینده تحت فشار قرار دهند تا قطعنامه‌ای را تصویب کند که بر اساس آن، این نهاد آنچه «نقض تعهدات ایران در زمینه منع اشاعه هسته‌ای» ادعا شده را به شورای امنیت سازمان ملل گزارش دهد.
@ Farsna -
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/460105" target="_blank">📅 18:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آمریکا ۳ نهاد مالی را به بهانه ارتباط با ایران تحریم کرد
🔹
وزارت خزانه‌داری آمریکا سه نهاد فعال در زمینه مسائل مالی و بیمه مستقر در ترکیه را به بهانه ارتباط با ایران در فهرست تحریم‌ها قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/460104" target="_blank">📅 17:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
وداع مردم بهمئی با پیکر تکاور شهید در زادگاهش
🔹
ناوسروان سید مالک موسوی‌تبار در جریان حملۀ اخیر دشمن آمریکایی، در حین انجام وظیفه در خوزستان به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460103" target="_blank">📅 17:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhtZEwNLVUh274EBN-NwfPkhk_lug9L-ruzAQwtXI3duSSCwKQ57i0AmXKN8yYlK5pMRlskE-JnvY4H1TlulKW6M8E-CW_qAFjUC5U2Av6A_U62mhG7vQsO0N-UV90Ha96DN_W4-cB2lR_zTEmktEVtQd6mMPheUPqsRNnsixfIdAN6YAxA18hicx2KTDAQ-xxYBC_UrHP1p5q2gL59lUOnvnb0i_yL90AFn6XYIOw4e1B1ACLzn0Oy-ddHb-NI41tH4yCkTBHr6URVuJsGoRgS8iUn5_bjkqGQmOA3ysQ96jmbEQdLXBTWdAedKQLds4Mu6ozJSK-Xeeuv--ghXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: اقتصاد کشور را نمی‌شود در اتاق بسته اداره کرد
🔹
حدود ۲۲ هزار همت نقدینگی در جامعه سرگردان است و باید این منابع به سمت تولید هدایت شود؛ اقتصاد کشور را نمی‌توان در اتاق بسته اداره کرد و باید از تمرکز خارج و به مردم واگذار شود.
🔹
دشمن به دنبال شکستن تاب‌آوری مردم و ایجاد اختلال محاسباتی است، اما بیداری و حضور مردم در صحنه، محاسبات دشمن را بر هم زده و نشان داده است که سرمایه اجتماعی و حضور مردم، از عوامل مهم عبور از شرایط بحرانی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460102" target="_blank">📅 17:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtJpHUMWopzN_KEocT18TsGeeCVLqEExuBs-P71NG-5plyfez8GnymmcOIVSVDQ_tBf-GGlHmOfS2e_mIv5sDqdA2udD6pp8dN-CQmwRs_HI5loG7g_DWs6uxYtVHROtvDQVPF11okq-lY1khblbebxRCINAr5fgvXp1o3BID0Vgv-vU7ahORW0fGDV7pK_tm_00bAfAy4zIt6NUe5V52qOXWHM3Bo6JeAvhbcjJLNpkBShx50howKOS5Z1vEbvzoOrNjEliaP9WutblqBdQGvT-qyAeblwitOR3KRg1NZ9RuQ-H_-TnFTlbwzmxKHADt83awNth1ioIvFCgVjzvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ اولیانوف به آمریکا: واشنگتن حق تعیین‌تکلیف برای روابط روسیه را ندارد
🔹
نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین اتریش امروز در پیامی در ایکس به درخواست آمریکا از مسکو برای دور ماندن از تهران، واکنش نشان داد و تاکید کرد «بدیهی است که واشنگتن نمی‌تواند به مسکو دیکته کند که با کدام کشورها روابط داشته باشد یا نداشته باشد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/460101" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOnBkKnzRDPYN9BEVnwdBILC1TeYPAcPR5wx8xWO_TuuqWneehX6k-CdiFo5oSdKqPMt2W5Oz7H3QCvhPoHVz4NsSNc_FhxKKLWuAW-KXI6UiUmtjQKHd5XD4cx0cYHYkLprLTYQ1flCnd172ahoWyl0-eloLnlHcHIROmPSSQMN0GRbbN3GBZ-V1D6LyX4QOBirTcxDn91uTja7HI8BxBM87td5V5ylaekqqxBWb3O5Dg0znSOL7c46zg0fdq8SH1fwZqINoWfHbn-AFR_Ck-BuGNhcmahCXvzx6V17sgCzfEkU-A-Onvr0quqxERG0zymIDmPDqdelSKSrBgNd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: متروی تهران تا پایان جنگ رایگان است
🔹
متروی تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/460100" target="_blank">📅 17:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXMae0CTLzxQguQzslQvX0W2_MbRwELPLgoiFaVftB7cZ_0Fr4NwqIgDtMDhX6-YvGWe7HAWNlD8R-DctykP5okFLrpq5JITRD5memsVPklOk02KhcwbEhiiE7WGuG5mNbQM8tN6jlfUre8O4NbbPpDwQaNLcD_EqPpNBQnzJFj6VasT9DjCtIhr0y9H5svXOhMM-8F1zxSDfkJveVinqHom45RFsbXsPM2pG3cVurLnTlBzx-LPyKdk_Z1xj3G3d9zfBbOe7Bwd0M8OcDHdSCcv5a5TTH6Z2qoV4KFf2S_hdIi3JTy9IHT62RM8jMOJk2TjD8XIz99oZHLOO-fNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار عفو بین‌الملل دربارهٔ خیز اسرائیل برای اشغال کرانهٔ باختری
🔹
سازمان عفو بین‌الملل: رژیم صهیونیستی با صدور دستورات غیرقانونی برای مصادرهٔ اراضی کرانهٔ باختری، سیاست تشدید اشغالگری را در دستور کار خود قرار داده است.
🔹
اسرائیل از طریق مصادرهٔ اراضی کرانهٔ باختری، در حال گسترش شهرک‌سازی‌های غیرقانونی است.
🔹
صدور دستور صریح برای مصادره زمین‌های منطقهٔ (الف) که تحت کنترل دولت فلسطین قرار دارد، شامل این اقدامات است که بسیار نگران کننده است.
🔹
اقدام مذکور شهرک‌سازی غیرقانونی اسرائیل را بیشتر تثبیت کرده و باعث تضییع حقوق مردم فلسطین شده است؛ فقط در ماه ژوئیهٔ ۲۰۲۶، ارتش اسرائیل حداقل ۱۵ دستور برای مصادرهٔ زمین‌هایی به مساحت تقریبی ۲۰ هکتار صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/460099" target="_blank">📅 17:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf864b3c6.mp4?token=q8Bfkr7sFmAZHMNyMUO9zpmYw3qSIQnYCwrcfQ97tQXjkQwb_fkfMRkAY6RKGwhkzpk0Sf1Zg8JgbZgZTPAEaSKJaZEBlXxjyO0NTJ-j1TQzgvL8-ln8qmvL_QbNf6y7wGuPbM3hy5kIKEDDwdQtTEit5P8RaNFeLtv1a02cSvJrA7zrPV5qEd4q4ksZ44nMhhb4gGmg9gwVm59MmONdt5tjF2mDaSBj9RVjdIuKgFNgp-NwV4N5Bal-XfHBdiQcoU9XQvLJQdENh3A8Z2PruOsAaZ363Q2nGiB3y1mMY2SMQrV4puycheVzlEYVWaeLTAxIpc7YW9yfaDYUQpOzs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf864b3c6.mp4?token=q8Bfkr7sFmAZHMNyMUO9zpmYw3qSIQnYCwrcfQ97tQXjkQwb_fkfMRkAY6RKGwhkzpk0Sf1Zg8JgbZgZTPAEaSKJaZEBlXxjyO0NTJ-j1TQzgvL8-ln8qmvL_QbNf6y7wGuPbM3hy5kIKEDDwdQtTEit5P8RaNFeLtv1a02cSvJrA7zrPV5qEd4q4ksZ44nMhhb4gGmg9gwVm59MmONdt5tjF2mDaSBj9RVjdIuKgFNgp-NwV4N5Bal-XfHBdiQcoU9XQvLJQdENh3A8Z2PruOsAaZ363Q2nGiB3y1mMY2SMQrV4puycheVzlEYVWaeLTAxIpc7YW9yfaDYUQpOzs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌دست کردن رانندهٔ کامیون در لهستان منجربه تصادف وحشتناک با قطار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/460097" target="_blank">📅 16:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxCAZQSwk_V0WFmacSJWXElkkCL7GuSrMiGKjp4tck9EKPbjk57vqyQ5a1AisDAluA0ZZSG8xPESbXy1F67H6kYjtYmN0LLbWi-azjmqNjcP_SFMkxOyMDLcXc3NfgEklNywLfrOrplsZgkjnja48pHWp7hIouFAtDRlq8KlSWnCKgxjiwFcTeoBndoZpsN6cKmws06XnVx8pyONsGOLIoSk7il2j7YBi4kGp6OABVoNiGb-VqrKWhvJ_H0QOGzqUjEvtm20_An2kU0QeRw1T9pJ-CGocrWkvQhlPvUnPedG2fbDuaH1LZoLz5358JSUKO10HSlkQg8loKGfiLRolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرستادگان ترامپ عازم مسکو و کی‌یف می‌شوند
🔹
استیو ویتکاف و جرد کوشنر در حالی قرار است فردا و پس‌فردا ابتدا به مسکو و سپس به کی‌یف سفر کنند که واشنگتن مدعی است برای ازسرگیری مذاکرات ۳ ‌جانبه میان روسیه، اوکراین و آمریکا تلاش می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/460096" target="_blank">📅 16:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460093">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a6c9629a.mp4?token=PkAtGOYGHXJidoWaA9UAaCijOL5ynNdNilQfzSi9v5CRuhJKWp2sG6kpNv1UMTp_bLXiwX7ztpeXK4gNnZimNIDspiovsfJxkzU44O_lS5TxlovzTbk83GdmuztNTQ41kyYEuPFKGHYe9D2JT3zGvjqf5X4H_W71RmPYJYtzcfOBJ8g07UXSaK8fKUb89ciDrtGLE1HZg8BZ9cyLaxLp0BVazPAg3ERPVeSBBYj31XLUj-JJYlleKdo8EqL7YguUeIA-2crUBXfE3o8p9P1oUnpHKnaDT2wftFTa1btZ6pnhdC6yY9qYjHcYjr5rTsWsn77vWFlsbYr4bXBHEsFilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a6c9629a.mp4?token=PkAtGOYGHXJidoWaA9UAaCijOL5ynNdNilQfzSi9v5CRuhJKWp2sG6kpNv1UMTp_bLXiwX7ztpeXK4gNnZimNIDspiovsfJxkzU44O_lS5TxlovzTbk83GdmuztNTQ41kyYEuPFKGHYe9D2JT3zGvjqf5X4H_W71RmPYJYtzcfOBJ8g07UXSaK8fKUb89ciDrtGLE1HZg8BZ9cyLaxLp0BVazPAg3ERPVeSBBYj31XLUj-JJYlleKdo8EqL7YguUeIA-2crUBXfE3o8p9P1oUnpHKnaDT2wftFTa1btZ6pnhdC6yY9qYjHcYjr5rTsWsn77vWFlsbYr4bXBHEsFilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند،…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/460093" target="_blank">📅 16:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460092">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176b4afb7.mp4?token=pdY3DLd1S7egaPaKayQOKu6JZIMbylvD3JCv6hh_-DRWosWKHZ9NA2iLCMfk0PCMLfGK-Mll-_iUKuXqs03LSvmxSrsqbb__7Fv9v5qMq08cpcrZuZ0_ZcBS4v7nIDrHYjdU9OpToJPRAt0itrSZo1MkQab3LhAhjhA6DWI3IuOVd8Keu3xAuBT_NoGz9xKn6nEvUt73a8XnzvHd50THfQyFWAiRU9pGnhRxdaA7veFainy0m34YV1mj6q-Iv2K2zgn5RmnQsVdPfC2Af4V5Xgm_JEf6mIM1RlDE8hhN0NGJjKZWeBjoVkV2EzN3WO1Mzhsn0ok5JR6gT49qrM_dEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176b4afb7.mp4?token=pdY3DLd1S7egaPaKayQOKu6JZIMbylvD3JCv6hh_-DRWosWKHZ9NA2iLCMfk0PCMLfGK-Mll-_iUKuXqs03LSvmxSrsqbb__7Fv9v5qMq08cpcrZuZ0_ZcBS4v7nIDrHYjdU9OpToJPRAt0itrSZo1MkQab3LhAhjhA6DWI3IuOVd8Keu3xAuBT_NoGz9xKn6nEvUt73a8XnzvHd50THfQyFWAiRU9pGnhRxdaA7veFainy0m34YV1mj6q-Iv2K2zgn5RmnQsVdPfC2Af4V5Xgm_JEf6mIM1RlDE8hhN0NGJjKZWeBjoVkV2EzN3WO1Mzhsn0ok5JR6gT49qrM_dEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: هرجا احساس تهدید کنیم عملیات پیش‌دستانه انجام خواهیم داد.
🔹
دکترین نظامی ما پس‌از جنگ ۱۲ روزه به‌تدریج به این سمت حرکت کرده است که مطابق منشور ملل متحد باید از جنگ پیش‌دستانه استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/460092" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460091">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9986a958.mp4?token=orx1vw2s03yHYWM0F1cikakgfYf8_TEKtqwajDt4cGyco9qnXGKTJBIIOfSnEXGMahSlJ2f0Kj9-lcHbuel1K6Dox4TZeO8EaDxfDxZzCC5nLVh3ri4G-smPqevwVg8vRBF544RWJAwkp2NdE6qGSNPFz7Ci2B4QO-gddq8e3WFGv2tsT4qI4ffTDxFq-2iUobKebSm3ksfW2ffIZxmvomyrc0yE8IQmkJp6_F3JWrp15SB0B3JV_BitUe9fegBcG6GsfrxZUz9wtGcfchtLlSgQLevjbl36mqbjAYQQ90rYlcySQxk7cGsU6jcKP8pWdQ8f7BCWAS2uBlfVIOXV9oPUhNQ31bGFBU_UnhpQp34z7LkRwXq0ef8amjt8iVg3__IKRKxPxmRtOYLdtdfKADXvQZSB3l4VgbNthUqdhseCKsRx2FUjPn6vXxLP6qEJ4oBW5VlmA99ZQNGjc3Ti7qWDayolcFMT-un3El3AaF-6zuOI55pXHK7_ovO0HMi8RdK-VyQS4KT36kaknX0LOCi9v_PVJBObq12cUZlF1Sqvue-oIl9_Sw8OfM7cm57SdoPQNlIrNp3pVicUHV1F4XLPX-AQ754Yz_ILlE3fRIRS-nXzq64cd7YT9QphwltONedOiFF6MkEFZ3EuUY__rE6yHJuSQFduJWDRxPPEJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9986a958.mp4?token=orx1vw2s03yHYWM0F1cikakgfYf8_TEKtqwajDt4cGyco9qnXGKTJBIIOfSnEXGMahSlJ2f0Kj9-lcHbuel1K6Dox4TZeO8EaDxfDxZzCC5nLVh3ri4G-smPqevwVg8vRBF544RWJAwkp2NdE6qGSNPFz7Ci2B4QO-gddq8e3WFGv2tsT4qI4ffTDxFq-2iUobKebSm3ksfW2ffIZxmvomyrc0yE8IQmkJp6_F3JWrp15SB0B3JV_BitUe9fegBcG6GsfrxZUz9wtGcfchtLlSgQLevjbl36mqbjAYQQ90rYlcySQxk7cGsU6jcKP8pWdQ8f7BCWAS2uBlfVIOXV9oPUhNQ31bGFBU_UnhpQp34z7LkRwXq0ef8amjt8iVg3__IKRKxPxmRtOYLdtdfKADXvQZSB3l4VgbNthUqdhseCKsRx2FUjPn6vXxLP6qEJ4oBW5VlmA99ZQNGjc3Ti7qWDayolcFMT-un3El3AaF-6zuOI55pXHK7_ovO0HMi8RdK-VyQS4KT36kaknX0LOCi9v_PVJBObq12cUZlF1Sqvue-oIl9_Sw8OfM7cm57SdoPQNlIrNp3pVicUHV1F4XLPX-AQ754Yz_ILlE3fRIRS-nXzq64cd7YT9QphwltONedOiFF6MkEFZ3EuUY__rE6yHJuSQFduJWDRxPPEJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در عملیات‌های اخیر علیه دشمن از موشک‌های زمین‌به‌زمین فتح و پهپادهای آرش ۲ استفاده کردیم که مجهز به هوش مصنوعی بودند.
🔹
درحال‌حاضر عملیا‌ت‌ها را به‌صورت ترکیبی و نامتقارن انجام می‌دهیم که آثار بسیار مثبتی داشته و توانستیم به‌راحتی اهداف را مورد…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/460091" target="_blank">📅 16:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460090">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ddce6d63.mp4?token=f_0derLBxDud0fLOx6VCY5592_OXg5D-NsvJvxZdXxk6DlmB6_VZyeh8VJx_YuyvoDS6Wk3NhWekylqYEXiCvED58EGLvA1rQ71DrAdB2CjRbuSdjb3lOArm7yrYLBibc5h96j5Zq1aW06xhpduMmGEk_TlJCu9PO282JEjy2kvZU3b_W1CFZAyepxnx8qQsKciKZjc8ZB2jVZ8MrqEmDVxqvzX_HphL74uwgbojfm9ao3vvoLcdrxYpDAiS4WqZ_o_RwjrlgXPRP0kvs0qPw-Qpny14azv_bMel-l5H3nhbw6_PXyK2qe2PKjUKwJ4tAgzOrluysW1ppZV6_kWx3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ddce6d63.mp4?token=f_0derLBxDud0fLOx6VCY5592_OXg5D-NsvJvxZdXxk6DlmB6_VZyeh8VJx_YuyvoDS6Wk3NhWekylqYEXiCvED58EGLvA1rQ71DrAdB2CjRbuSdjb3lOArm7yrYLBibc5h96j5Zq1aW06xhpduMmGEk_TlJCu9PO282JEjy2kvZU3b_W1CFZAyepxnx8qQsKciKZjc8ZB2jVZ8MrqEmDVxqvzX_HphL74uwgbojfm9ao3vvoLcdrxYpDAiS4WqZ_o_RwjrlgXPRP0kvs0qPw-Qpny14azv_bMel-l5H3nhbw6_PXyK2qe2PKjUKwJ4tAgzOrluysW1ppZV6_kWx3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در کمتر از ۱۵ دقیقه به حملات اخیر دشمن در جنوب کشور پاسخ دادیم
🔹
آمریکایی‌ها سعی کردند کنترل نیروهای مسلح ایران بر تنگهٔ هرمز را تضعیف کنند که با پاسخ قاطع و کوبنده مواجه شدند.
🔹
در این عملیات‌ها پایگاه‌های آمریکا در سراسر منطقهٔ عربی، از اردن…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/460090" target="_blank">📅 15:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7c7a6a7b.mp4?token=QuevQJczxhrlQqF04kkoZzWTFB-DUqXeHxflM6VtPQ6vOPPqXaJGrJBsVjOJl5dUsn1bvonESLWrHbJkUoUqeeH9EX4_np-lxgvNILCBAExLGNzhF9t8G3OPl6t2j5EDmxjLHZwoKd_iTzJAWHWvyFRI35pZWh-wcmWgrgVTQ1m6ep1nOHmHWYjEznj1AHFW_7YNh-iYl2tCUFNAE60OweNKPHAOMXsasf56KGljbSRERVVlnDM2OAgVsq4KV-tvsYs7NajT_4cNyIbZhHXYu_huPrPHIHAdinAFTzTp5zGC2d5atrceImss7B-QfMi4Ud2OaHAokTbp96uQj_LWGKUFXC3uB5rELRSXoUbYjEPrP80rDC7mXttRZYle17N36RwkuFdJlOfFVR6EbhAR38Ym9fQJYdwmUK0QJPmOHZsURvvgTuLZHJFDfzxdt51puX-mDeGx84y0LL9t4IMuNxWAfWvghStBNa7ru31dagGDyawQg6o5Fwd18jE5v63i_k4UFlJx3KkxprlnN6cYTLa-ER8DkweUteG4Q1V6eOfrbp-1i6WsmyE1lNt1EJRipA4rEViMEgTQBs3pGPJcRfq2jtbU_ZkKjJ1VIQnVt6RzTSv41sSDzNQXVq5iH0dKEBVE0PI_4nGR2sLQpcnSymPmmaTC9q-N0lX-rH1yv-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7c7a6a7b.mp4?token=QuevQJczxhrlQqF04kkoZzWTFB-DUqXeHxflM6VtPQ6vOPPqXaJGrJBsVjOJl5dUsn1bvonESLWrHbJkUoUqeeH9EX4_np-lxgvNILCBAExLGNzhF9t8G3OPl6t2j5EDmxjLHZwoKd_iTzJAWHWvyFRI35pZWh-wcmWgrgVTQ1m6ep1nOHmHWYjEznj1AHFW_7YNh-iYl2tCUFNAE60OweNKPHAOMXsasf56KGljbSRERVVlnDM2OAgVsq4KV-tvsYs7NajT_4cNyIbZhHXYu_huPrPHIHAdinAFTzTp5zGC2d5atrceImss7B-QfMi4Ud2OaHAokTbp96uQj_LWGKUFXC3uB5rELRSXoUbYjEPrP80rDC7mXttRZYle17N36RwkuFdJlOfFVR6EbhAR38Ym9fQJYdwmUK0QJPmOHZsURvvgTuLZHJFDfzxdt51puX-mDeGx84y0LL9t4IMuNxWAfWvghStBNa7ru31dagGDyawQg6o5Fwd18jE5v63i_k4UFlJx3KkxprlnN6cYTLa-ER8DkweUteG4Q1V6eOfrbp-1i6WsmyE1lNt1EJRipA4rEViMEgTQBs3pGPJcRfq2jtbU_ZkKjJ1VIQnVt6RzTSv41sSDzNQXVq5iH0dKEBVE0PI_4nGR2sLQpcnSymPmmaTC9q-N0lX-rH1yv-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در کمتر از ۱۵ دقیقه به حملات اخیر دشمن در جنوب کشور پاسخ دادیم
🔹
آمریکایی‌ها سعی کردند کنترل نیروهای مسلح ایران بر تنگهٔ هرمز را تضعیف کنند که با پاسخ قاطع و کوبنده مواجه شدند.
🔹
در این عملیات‌ها پایگاه‌های آمریکا در سراسر منطقهٔ عربی، از اردن تا امارات، مورد هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460088" target="_blank">📅 15:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a03d5c8d.mp4?token=Y5ZdS_rbrbVQdtij44w310tV0NbbogFUt8U5WAAPVuKSnzs0ph7u-HN2KBIRcV5v0kHh_W1PR7A4y4gYOfrZzOEx-_v2rAwYZ638OnbCSUnk8z8OIRVGXtbVGUSN0hE65Az1cqn53eT7P4dFdBM1ki3e1980_zX-7oOIEIOZ3rQbiZou8ZCLObgaw8zKTttwbOc8-zrOSeoEz3XiuelwyUVPB1A9c2mCDEiEPPOVv5Ka2HtyYFpTGoMSDWyN_EAF0mDB-HPGP3jFQXaV52MVnyli1bczOoGQq5BslcTKASM_r5iAXIOD6haQ4n2BJZwqK8BJZ9zRhLRRMy1vabvgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a03d5c8d.mp4?token=Y5ZdS_rbrbVQdtij44w310tV0NbbogFUt8U5WAAPVuKSnzs0ph7u-HN2KBIRcV5v0kHh_W1PR7A4y4gYOfrZzOEx-_v2rAwYZ638OnbCSUnk8z8OIRVGXtbVGUSN0hE65Az1cqn53eT7P4dFdBM1ki3e1980_zX-7oOIEIOZ3rQbiZou8ZCLObgaw8zKTttwbOc8-zrOSeoEz3XiuelwyUVPB1A9c2mCDEiEPPOVv5Ka2HtyYFpTGoMSDWyN_EAF0mDB-HPGP3jFQXaV52MVnyli1bczOoGQq5BslcTKASM_r5iAXIOD6haQ4n2BJZwqK8BJZ9zRhLRRMy1vabvgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل نپال و چین از هزار نفر فراتر رفت
🔹
تعداد تلفات سیل مرز چین و نپال به ۱۰۰۳ نفر رسید و ۴۴۶۲ نفر از جمله ۸۴۴ تبعهٔ خارجی همچنان مفقود هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460087" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn5AlHGhYchdv6rnEa6IIU9IwaMiZg2ST8wxvS1kgoO6RkdBYMKJkTEvjyD6mDhmi7ue1dpkNXGG_EZ-wMj1rI2NdDR1Jfd0CJVoGVh0WTMyRzm4CzMpy_LzW28P30VDzSdd8WJwfUIJO8cWN-ZRiWAbOWq4cyPp8ys0EBWoOW081qoG3vu-Ws92k6MkyyOyA75PElwU-lZfn2NK4PZApSKynK629-U9_LN2jSWWfi0ZrvSGbEYgpIIAVtxYAUaA4PFo3_Rhv59_UgwS6Ng0WQ8QXB3qmFvoVe4FkzHizuBdC3128D3QUukGMcoiYM4iwK35-QqEnKcI3CwkoSygKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/460086" target="_blank">📅 15:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuxAnRUrDndgISjXaoEMKc8Mx1JtT6a1cb4ewESUBV1U3EhCu1tKxarnlj6K2aw-dNiqVbQyxjw_z4L5lPwIUTkLoTHLBu2LWEL8IQNLGpTbtBw9_Jg5qvKWexZf5DiDnqRbbNAOz7kTlfHCPJx0JDOeE7BWKrAM8xcdN6WdA8F16URZgGWjDaVbp8m_OfkrYZiATfVB0E0eJP6LVCAgRUYxf49oOjpKFl-69HWAmnrFGaS0mCdVHquePr14gmYJFC0sQIbyK3ssUvps76ydI6dsqnGX9ADxVFQ8b3qSr-JiFhxhwYIjJzS0aGwDZ17qMKqfTCcUoh4469Vejf6S_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽
رشد ۶۰ درصدی ارزش سهام پارس خودرو در یک ماه گذشته
◽
حرکت پرشتاب به سمت افزایش تولید و ارزش آفرینی
🔻
سهام پارس‌خودرو در معاملات یک ماه گذشته با رشد ۶۰ درصدی قیمت همراه شد و در این مدت مورد توجه معامله‌گران بازار سرمایه قرار گرفت.
مشروح خبر:
🔗
saipanews.com/news/id/24634
🆔
@parskhodro_pk</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/460085" target="_blank">📅 15:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/460084" target="_blank">📅 15:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYfK88viWClHnvFTpJ7IU-gHjsysOtpSJOuVuK2pWsMeEKvSJ8fnFGb8-ah5Lh6zredQ3rzKwWk8qoLOPhOCmeXNFwbq3oomCVXXloZ_jFyavIWYEoo0PBM1zNdA53ovMsRp99JjlHk3MnE4VvnbldTAQRoDAEz127DQJZ-xwR0E78cUPvEln5EcDCNeJbcZ_tUkMkIhUnqfEImQp1_WEIJ0mrggKl_Ru4tbi7akWF0AFGCfzLGhvwYcBDgp9DzsFS-TGzgBlRR4rAw1A4MDjj4d1gp4IPApeAeLv-Gr7zEHmEcNeh2CNBnUvWY2JdeThCJ5ErU3mUSK6GkFUWqAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ارتش: راهکار مناسب برای آمریکا پرداخت هزینه‌ها و خروج از منطقه است
🔹
امیر اکرمی‌نیا: معضلات ارتش ایالات متحده در منطقه و مشکلات مردم این کشور، ناشی از اشتباهات مسئولان آمریکا در تجاوز به یک کشور مستقل و متمدن است.
🔹
راهکار مناسب برای آمریکا پذیرش واقعیات، پرداخت هزینه‌ها و خروج از منطقه است. این کار منطقه را امن و مردم آمریکا را به رفاه نزدیک‌تر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/460083" target="_blank">📅 15:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa_Y7Wa9w0c2OsBVjTHD4KU6fnmFzXl1icpxBJ6fYEFdV5dxWPH5sRyeF-YcTnkQmK-AwZHVORrzd0cyQ38XTsl3DblPKGmdXykqeHNLyV4Bue0SmjguanT-Gke1DhdOlJb04equUyT_ioSOcnKnLSXKzRaqLkNntTbwxQ6xshgBIt5Cosn6cjMmc4P9XYGauVKLVBx5MGSvQk49tBqfnQ-1kUVgYD7dNn2N8utZ_I3fItaMutG1BNdQS1aM-wgVbj9l1foHtu5nQYxZqhIEfEwn3PtJCpPe1QDSfPfRKjinEsLjmltZVgQtTS1t-QxqaTuEz3zMydqljMdbr9PhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور آمریکایی: وزیر جنگ دربارهٔ حمله به جشن عروسی پاسخگو باشد
🔹
کریس ون هولن: هگزث تلفات غیرنظامیان را موضوعی فرعی تلقی می‌کند؛ نیروهای مسئول جلوگیری از این تلفات را کاهش می‌دهد و به نبودِ قواعد احمقانهٔ درگیری افتخار می‌کند.
🔹
باید دربارهٔ حمله به شهر سیریک تحقیقات کاملی انجام شود و مسئولان آن پاسخگو شوند؛ همچنین باید همین حالا به این جنگ فاجعه‌بار پایان دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/460082" target="_blank">📅 14:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32f681c97.mp4?token=fXr0xx7JEuviM0s0lN7da2SCAfsiKDv84RuHJFuuhknfFTbsjZJ6W-OpzZ5G5jQQXhkKysesbXxDplgdsViMXkbh6MzseDekfWlSe8jCIxSu9mpwpsja_A7cVlVrc5_1gcrROMQQTgEzYnOe1U5SbeU3bHwfbXlgDIlwKizf8RWqKTouNOuomNwBlJvoLTs2TgFCb-_PLzUKRUpevZ2c43VZb2bC0wZm9MJyDOn9947x5R6RP6NPsbI8Fnw7gd2mYRlF8WQcGoxj4MNRiKHJSkK1qkdnPNf2qfWGrT8A19JhROzI4gORlxL2U0kaCPMKSVqMrdlk-uUMUjrcoKlMzTMKOhuZWl9JE4aNyzjnXyyIWEH75bVKL-bTYGl5XTevfDZtx_Rzr05kpjlummPReXCJmodFIP8fWiqLtzy4q9CueAsSMwGtiv12rcbV9sNLHwLTUQoCXYpRE0DPDDvvE3FqfganvPGidUISZysOEUMcH_f_SecwImffusIoDFjqP8f8fVHVVwBJoglqK0J2R1ovrL6U6r9MVoaC2WRh09T9uoqL55DH-ORTzds_KuiDlV1fIG1-wXFrlKg1yH8xHEKyqv6xAJId1w2y1mwPD3McKjFNptPFsL-fLqneR5e8ISKekAt8o15q093zN1-MlEgTOPJpLD45Gqmq13mYcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32f681c97.mp4?token=fXr0xx7JEuviM0s0lN7da2SCAfsiKDv84RuHJFuuhknfFTbsjZJ6W-OpzZ5G5jQQXhkKysesbXxDplgdsViMXkbh6MzseDekfWlSe8jCIxSu9mpwpsja_A7cVlVrc5_1gcrROMQQTgEzYnOe1U5SbeU3bHwfbXlgDIlwKizf8RWqKTouNOuomNwBlJvoLTs2TgFCb-_PLzUKRUpevZ2c43VZb2bC0wZm9MJyDOn9947x5R6RP6NPsbI8Fnw7gd2mYRlF8WQcGoxj4MNRiKHJSkK1qkdnPNf2qfWGrT8A19JhROzI4gORlxL2U0kaCPMKSVqMrdlk-uUMUjrcoKlMzTMKOhuZWl9JE4aNyzjnXyyIWEH75bVKL-bTYGl5XTevfDZtx_Rzr05kpjlummPReXCJmodFIP8fWiqLtzy4q9CueAsSMwGtiv12rcbV9sNLHwLTUQoCXYpRE0DPDDvvE3FqfganvPGidUISZysOEUMcH_f_SecwImffusIoDFjqP8f8fVHVVwBJoglqK0J2R1ovrL6U6r9MVoaC2WRh09T9uoqL55DH-ORTzds_KuiDlV1fIG1-wXFrlKg1yH8xHEKyqv6xAJId1w2y1mwPD3McKjFNptPFsL-fLqneR5e8ISKekAt8o15q093zN1-MlEgTOPJpLD45Gqmq13mYcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: برای اولین‌بار به صادرکنندهٔ گازوئیل تبدیل شدیم  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460081" target="_blank">📅 14:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzxzIYWYu1JaEVRcwaZ_AKN6uXTImtbRI_Lg4bZnstjvJP0n3mxkHj2duG6hUngS0H7_gtHYZpzhv2mYZmh7iP1NiiRbumC1-xMPeiJ82UAHNPBleEd_iHXsNqb_xU8Zvyn6882dGW9-f_0QzGz4uj0RloH-QdGpGtmrPX85lLYZMFRndLHRCvYWt4YcTxLTD_iX6OeGXDKMRv8Bkw6AQqFuwUO7qErLbFmbwmo6Jv6XzubVpCplvMebbCI5aAGHGDFeSAkz6IQet8cCc83IbZbuKun7KE5wmTotZsPC7o4qp-RD-lLMs4PafkBPSV7CtpfPBqiXTm5JPFt6fPbIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک ضدانقلاب
🔹
فرمانده مرزبانی کرمانشاه: گروهبان‌یکم مرزبانی «رضا دارایی عمارتی» در جریان درگیری بامداد امروز مرزبانان هنگ مرزی پاوه با گروهک معاند و ضدانقلاب به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460080" target="_blank">📅 14:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جاده‌های مازندران یک‌طرفه می‌شوند
🔹
پلیس‌راه مازندران: از ساعت ۱۴  مسیر جنوب به شمال آزادراه تهران-شمال و جادهٔ کندوان مسدود شده و از ساعت ۱۷:۳۰ تردد از خروجی مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد.
🔹
در جادهٔ هراز نیز تردد به‌صورت مقطعی به صورت یک‌طرفه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460079" target="_blank">📅 14:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04dc114a09.mp4?token=nOh3Nh4IHklKWPdiGZXyn2rjCcNpZ4e2128cvrfrUZvdI8IHQWSg-9jubzUplUlg584ECUIXkJmcw8AWNVhPv35IdtIpMFcZPQKyrG5VhLThFmFFW-YG0CcNLOuxnw3MkLcJPa5_2ISGiq0OY6uJD6zj4E1Y1NV3_cfbQ7xKTiVq4gqFrRozNByQG9oMSrLHi9AcIU8w1ak0K33tFjY_s5kCEvsYGfmHQWt2iluAcKBQMx31365VPO-zBdg_U9PYTLHUjySeIA4gNZ5N7zS0W86u8S4311VM9_utQFrZfMMnrWRQ20qoZKxhx6tlS9CsEsWKVdyLzdkrJNsVoWNVkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04dc114a09.mp4?token=nOh3Nh4IHklKWPdiGZXyn2rjCcNpZ4e2128cvrfrUZvdI8IHQWSg-9jubzUplUlg584ECUIXkJmcw8AWNVhPv35IdtIpMFcZPQKyrG5VhLThFmFFW-YG0CcNLOuxnw3MkLcJPa5_2ISGiq0OY6uJD6zj4E1Y1NV3_cfbQ7xKTiVq4gqFrRozNByQG9oMSrLHi9AcIU8w1ak0K33tFjY_s5kCEvsYGfmHQWt2iluAcKBQMx31365VPO-zBdg_U9PYTLHUjySeIA4gNZ5N7zS0W86u8S4311VM9_utQFrZfMMnrWRQ20qoZKxhx6tlS9CsEsWKVdyLzdkrJNsVoWNVkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: صادرات نفت در زمان یک ساعت هم قطع نشد
🔹
بیش‌از ۵۵۰ اصابت به جزیرهٔ خارک داشتیم؛ همکاران صنعت نفت زیر بمباران بارگیری می‌کردند. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460078" target="_blank">📅 14:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiyJ29QZyFvCcHdbfqrR9Q_ZtX6DFpHoPSdlWvLJpJypzAZcaFU1gUSI01ZPUkcm1InDSv63QiD9x2MZEyR_8Rhyfd3tH2BABJ2xyRAvqs5mnZMmNIqsr6lTiDkwuO8mr_Pr5JvP1X2wH-53qWQnNtXYiJYo_1iyjmBVrA9Eu1yuLOWQRGQZyuaXqDW2dML7UV2RKtubwQyyhsJxH0nrsn3z1G8qh78tfgHNZvSm2QaUOY3GQCV7oqBjgYLeSSH6Bq-XQpHrAYuHZ0w_C9uMv7eHz2-zbmbwCSEiVXjvI4526eX3Jf1URNhyeUW_U-vewyFMlhPBaAmR809uX3RAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: منابع حاصل از کاهش مصرف بنزین صرف تقویت کالابرگ خواهد شد
🔹
رئیس‌جمهور در جلسهٔ هماهنگی مدیریت ناترازی انرژی: سیاست دولت، مدیریت و کنترل مصرف با استفاده از ابزارها و سیاست‌های عمدتا غیرقیمتی است و به‌هیچ‌عنوان نباید تصمیمات این حوزه به‌گونه‌ای اتخاذ شود که جامعه با رفتارهای ناگهانی و شوک‌آور مواجه شود.
🔹
اطلاع‌رسانی شفاف، دقیق و به‌موقع به مردم پیش از اجرای هر تصمیم نیز باید به‌طور جدی در دستور کار قرار داشته باشد تا ضمن افزایش آگاهی عمومی، زمینهٔ اقناع و مشارکت مردم در اجرای برنامه‌ها فراهم شود.
🔹
هر میزان صرفه‌جویی و درآمد حاصل از کاهش مصرف بنزین، صرف تقویت طرح کالابرگ خواهد شد و محل مصرف دیگری برای این منابع در نظر گرفته نخواهد شد.
🔹
مهم‌ترین دغدغهٔ ما، دغدغهٔ مردم است و در تمامی مراحل اجرای برنامه‌ها و تصمیمات، از جمله موضوع سهمیه‌ها و مدیریت استفاده از کارت‌های سوخت جایگاه‌ها، باید به‌گونه‌ای عمل شود که نارضایتی و فشار مضاعف بر مردم ایجاد نشود.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460077" target="_blank">📅 14:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b853d23c51.mp4?token=Z6kpkb8SfH6Yji3DE8Vj6vVlm5M1wohaOJyVMzBoRqWEfG7iaIdb0dWVdKubQ9G8mK8a8XI4cnGwh35EH-oAJO4IRPcMJ7RkskjKpC28skzVXtuuNUYg08C6GEyVTq09h_g8txRGtwoYxMTu3S21FgiGEBtBAgjNmJ7QePBV0jkz1OWKeMNynJp08lhTT8fC6jIClB0kvAsWQ67yrCSfP0Xt3b8okesXy9VepLI90U6QAWalgF9cFWdZqqewfCK0uIxG6VKyHmglTm_K8tzBMg77pN3Gq_mGkMhJIUyAfNMFYXbrBQazPPmsl-Czw_UIiJXKnRjMFFV_weUukvSExYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b853d23c51.mp4?token=Z6kpkb8SfH6Yji3DE8Vj6vVlm5M1wohaOJyVMzBoRqWEfG7iaIdb0dWVdKubQ9G8mK8a8XI4cnGwh35EH-oAJO4IRPcMJ7RkskjKpC28skzVXtuuNUYg08C6GEyVTq09h_g8txRGtwoYxMTu3S21FgiGEBtBAgjNmJ7QePBV0jkz1OWKeMNynJp08lhTT8fC6jIClB0kvAsWQ67yrCSfP0Xt3b8okesXy9VepLI90U6QAWalgF9cFWdZqqewfCK0uIxG6VKyHmglTm_K8tzBMg77pN3Gq_mGkMhJIUyAfNMFYXbrBQazPPmsl-Czw_UIiJXKnRjMFFV_weUukvSExYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: در تلاشیم تا محاصره را به‌طور کامل دور بزنیم
🔹
در زمان رفع محاصره، نفت را به آن طرف دریای عمان منتقل کردیم. @Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/460076" target="_blank">📅 13:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697c3ea5cd.mp4?token=NY-lfqulfL1I_3sQNfD_kaP5X-djAUyN-9LnPz7HoyXTk2yvEYteLkxZfRlenzyFHlGtm3W_6hraAQ5COgzOqpI1x9HN6W-6Fwh2j2ZUKMRFjB1W_9l44NL9MV-YLsrvahLE-DYKIPhux8Yt7ftqQs9bBkN31M_s7sHH33tcsn-PFg-Y4AMYs-PL5v_LyK0X-jNHQnshKhqKN8fGVnJoTXXqEHZFueSL7FNs7ScX-GwBvU02nHfM84geJQHyGrKKE6M9RguZwqpLuKMZQJJ1bqLuLnOphIQ8ymIoDx8xHI_MjvbYC_JBq7JOFBy_zs255c_4WYniJguIImLHlVLWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697c3ea5cd.mp4?token=NY-lfqulfL1I_3sQNfD_kaP5X-djAUyN-9LnPz7HoyXTk2yvEYteLkxZfRlenzyFHlGtm3W_6hraAQ5COgzOqpI1x9HN6W-6Fwh2j2ZUKMRFjB1W_9l44NL9MV-YLsrvahLE-DYKIPhux8Yt7ftqQs9bBkN31M_s7sHH33tcsn-PFg-Y4AMYs-PL5v_LyK0X-jNHQnshKhqKN8fGVnJoTXXqEHZFueSL7FNs7ScX-GwBvU02nHfM84geJQHyGrKKE6M9RguZwqpLuKMZQJJ1bqLuLnOphIQ8ymIoDx8xHI_MjvbYC_JBq7JOFBy_zs255c_4WYniJguIImLHlVLWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت وزیر نفت از شب حمله به انبارهای سوخت در جنگ رمضان و نحوهٔ مدیریت پیامدهای آن  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460075" target="_blank">📅 13:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6058e3237.mp4?token=NlaXj3eSfyIDtUDr12RkugtoZci1AJF27tFIBB55Qwuap3ARTOdBSLBaIx2IkC1vOl2o65QN1wRPzaSb42lbSh6BNPN6DwOiPbuCwardBtA2VYyN_tvEB3ikASkiE675-XLjGN1zr4MH6NPXXfiVLqOt000AlLQ1qHr5vScF298UinxycN4xmr5mOsavz8If-7CRI48hGkPsk4QbNtsaAF0QgBA4Km_lqsIlXrhY5oRJLJp8B1Leh6Ae59JyqmephH_xs4YAYfELJWgOR9blq0JYUx2CitQHiQ1qM6hss95HCdGxeIPlfpWnUjbk-dyLBhhktR6zAYC-ksmlTa4rZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6058e3237.mp4?token=NlaXj3eSfyIDtUDr12RkugtoZci1AJF27tFIBB55Qwuap3ARTOdBSLBaIx2IkC1vOl2o65QN1wRPzaSb42lbSh6BNPN6DwOiPbuCwardBtA2VYyN_tvEB3ikASkiE675-XLjGN1zr4MH6NPXXfiVLqOt000AlLQ1qHr5vScF298UinxycN4xmr5mOsavz8If-7CRI48hGkPsk4QbNtsaAF0QgBA4Km_lqsIlXrhY5oRJLJp8B1Leh6Ae59JyqmephH_xs4YAYfELJWgOR9blq0JYUx2CitQHiQ1qM6hss95HCdGxeIPlfpWnUjbk-dyLBhhktR6zAYC-ksmlTa4rZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460074" target="_blank">📅 13:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4303f11b4.mp4?token=f0N2If2qUfX5Ns6O3CeKjMgXoOLCvT5nijz3cDVD0XEkf_tyaXNkIVDxWCrDMiK5NjRjGWn9JSMTSZLyXIPjtujmliyjR27Zq1yG9nUuFUmWX-31Xyr20SKpioqa7V-i61c1kIGI2oQjxqf_9lXyFVOn4tDlMiTu7aih9PZCvIuNT5zAZDVrLTn2HUFkOjjZwAbkcZ3-ErliVXWEwOt42soDzE5KNqdKH6ViTSMEQFIbY1vRhpd883LCBY1x5cpSTHhXNtcqTQy3TOBTVs_quoPD1qxrSixwDte4zGywCvah4d2IXtqNSwG1Dgo1dmbKFFsTM0jOgCl_Yv45J8u75zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4303f11b4.mp4?token=f0N2If2qUfX5Ns6O3CeKjMgXoOLCvT5nijz3cDVD0XEkf_tyaXNkIVDxWCrDMiK5NjRjGWn9JSMTSZLyXIPjtujmliyjR27Zq1yG9nUuFUmWX-31Xyr20SKpioqa7V-i61c1kIGI2oQjxqf_9lXyFVOn4tDlMiTu7aih9PZCvIuNT5zAZDVrLTn2HUFkOjjZwAbkcZ3-ErliVXWEwOt42soDzE5KNqdKH6ViTSMEQFIbY1vRhpd883LCBY1x5cpSTHhXNtcqTQy3TOBTVs_quoPD1qxrSixwDte4zGywCvah4d2IXtqNSwG1Dgo1dmbKFFsTM0jOgCl_Yv45J8u75zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی و توپخانه‌ای صهیونیست‌ها به جنوب لبنان
🔹
منابع لبنانی از ۳ حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در جنوب لبنان خبر می‌دهند.
🔹
توپخانه ارتش رژیم صهیونیستی هم اطراف شهرک النبطیه الفوقا‌ و کفررمان را مورد هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460073" target="_blank">📅 13:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK-HS5awr-F8iViZrU_FaInX5X54xZn5-FSYkbVCsF8_Godr7SnLaW7q45Fhk3fFtybJLXt4HzyWae76e0-F5heUkNVBQqXP5IXZXpW242lFYlTjE8T3dbD9ZMVKICax04yMlU6ZwklyzUWaS5sFWLn_nvJrdVLEyzAczl_4t6-x_8-MpVNmSaBbnJt_rKftfQk_jODgrwPLcFBRNGFkI7tuq7kQOuDc-_05KaeChdE_0X91CdG34rz7tvVG4hoXA5pULLNFYPTlP_c7GvIO6eNWAsOTJp0Uc9YGjhjgCn-HNN-SwhEIstXF8E_W_mNRyJ9RAv5Tgwh-KRlPe36E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعهٔ تهران: فشار اقتصادی علیه ایران شکست خواهد خورد
🔹
آیت‌الله خاتمی: از قرآن استفاده می‌شود که فشار اقتصادی موضوع تازه‌ای نیست که ترامپ به اصطلاح خودش آن را آورده باشد؛ بلکه از آغاز اسلام این فشار وجود داشته است.
🔹
همان‌گونه که دشمنان صدر اسلام شکست خوردند، تحقیقاً این‌ها نیز شکست خواهند خورد.
🔹
مسئولان نظام باید با کار جهادی بکوشند مشکلات اقتصادی مردم را حل کنند یا دست‌کم کاهش دهند.
🔹
هیچ‌کس در این نظام حق ندارد سخنی بر زبان بیاورد که بوی ضعف و ناتوانی از آن استشمام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460072" target="_blank">📅 13:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhZCkeF_fU_QkzPirZ0bZsYVYvTc6hXHXHvX5PEtV7iAk61Gl5lKbiEnYIKEcn2X8no_7QQ0m9S-CEEGhHdSb4RallpZ-EKtAhItVauML7ybqYBUMvMRR8otne8C3sKQE4M5VaDDXFkVqYaFWQOAZLKoNN-C5kZhO_tcthyvVdU61GlzoIEYZiDz5hYm3CV23EHAJPzPE-JX4CqG3x4B2YZD7uUlZuHVsCW92-QX9qgfUIxqqeQFqo0frlAhXRuEYinoWkdPcMwq7Mj5LpQ6XN6ZUre6nYxCYRHlwqjcmQwBnMUpFUqE346Fy6nDBEAZdrmRLb62V8ez85hfh-0PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵۰ کیلو مخدر شیشه در آذربایجان‌غربی
🔹
فرمانده انتظامی آذربایجان‌غربی: در بازرسی از یک خودرو، ۵۰ کیلوگرم مواد مخدر شیشه کشف شد؛ در این راستا یک نفر دستگیر و خودروی حامل مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460071" target="_blank">📅 12:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyYenCqZguxfYMd095j5LDWwTAgFiqP13wSELLNEiM2snMrat-pR418V9SY211ZQ-j2TnB_CSssQSok0c7LtOhOnmLubz0T8G3pRX_fJEJtIFHlxGbTYf4-fD4xzcekwTIHjiL9GyNBfkYQ4O1P5VccCdQDzU5ZoRMMEKE-tcNAQK1Cv1gLUylHbEglYIDtLRG0H4etLjX5ufKjo6IPjhgGXHRjzk_UdnIYk2pniihIzBhLSLvpNUyRfTfJP2AcagQQddMGTwHYwmOK15mLGhf5j8-PgLOj72fNZTHr_4Xq16Dq4xS6CtLgRAjlvM2RMLi8_c_iB-bki4bXK5TFz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: برای هر نوع تقابل آماده‌ایم
🔹
فرمانده قرارگاه مشترک پدافند هوایی خاتم‌الانبیا(ص): ایران با آنچه در جنگ‌های اخیر از خود به‌نمایش گذاشت، تعریف جدیدی از قدرت ملی به‌دنیا عرضه کرد.
🔹
نیروهای پدافند هوایی ارتش و سپاه در جنگ اخیر سامانهٔ پدافند هوایی تولید کردند، آن را توسعه دادند، در میدان مستقر کردند، از آن بهره‌برداری کردند و هواپیماهای دشمن متخاصم را نابود کردند.
🔹
پدافند هوایی کشور با تکیه بر توان داخلی، دانشمندان جوان، شرکت‌های دانش‌بنیان، دانشگاه‌ها و تجربیات میدانی نیروهای مسلح، در تأمین تجهیزات و سامانه‌های مورد نیاز خود به خودکفایی کامل رسیده و جنگ را اداره می‌کند.
🔹
خود را برای هر نوع تقابل در امروز و آینده آماده کرده‌ایم و آماده خواهیم کرد؛ زیرا می‌دانیم تهدید تمام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460070" target="_blank">📅 12:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPDdjE--GSs6eccXKRF-bi9U38YVmZXHd05_5rVIC0pydH0eXG2MNClOuvzqyzIki87UVNPFqimR5ihWWsUyhrzyXjZxoupZaiS5fhPGJ8zbCKBPPG8afJ5EaKJp6Jea3adlVQ45taJeI-B-VTNK600YClo2d9H-58a4U8PNt4LIIiiuvJUvn0CI-EAfGG4gS_OOH81xL8GFXCQP4l1Xc7dkTnc9E82IzehKYP1MSPjucaG8AeHax1YhkUYlk4893DpXBKdDCmUoKug-AefklZUpj9ZQ_g2A93OHsWd2tj0aXAOWR7Wn79FiUdrfaMAAG-CNK4NJ2Sl59ZeEeUZ38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فرهنگی سازمان بسیج: ۲۹ هزار گروه مردمی، پای‌کار میدان‌اند‌
🔹
سردار مقواساز: استقبال مردم از «میدان‌یار» بیش از پیش‌بینی اولیه بوده و مردم با خلاقیت خود به گسترش آن کمک کرده‌اند.
🔹
تاکنون نزدیک به ۲۹ هزار گروه در این طرح ثبت‌نام کرده‌اند و پیش‌بینی می‌شود این رقم به ۱۰۰ هزار گروه برسد.
🔹
هدف اصلی این طرح آموزش و آمادگی عمومی مردم است؛ میدان‌یار صرفا مسابقه نیست، بلکه یک حرکت عمومی برای آموزش مردم و افزایش نقش‌آفرینی آنها در میدان‌های پیش‌روست.
🔹
این طرح در ۴ محور آموزش‌های نظامی، امدادی و خودامدادی و دگرامدادی، فرهنگی و هنری و رسانه و روایتگری اجرا می‌شود.
🔹
حضور بانوان، خانواده‌ها، نوجوانان و اقشار مختلف در این طرح چشمگیر بوده؛ قرار است گروه‌های تشکیل‌شده پس‌از پایان مسابقات نیز در محله‌ها و محیط‌های اجتماعی به فعالیت خود ادامه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460069" target="_blank">📅 12:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7xsdmUAA0hVjSX0NmNekjWy9Nec03icJOXZaLQHdxui1APBIHeNLuIayL3MP2EdsjqHIHIpst9z7obxRg011fg9uMySjvwlbs18GWohz6s4FTS3_LsUpm8e7JWeJBnRs2FogI-wRrmURGbbK2ZARK2_jM6qdXT1Q-G6SVUI9PyPN3KKQQqG-zey_NEqzwl94rqaQ5-2kacBCwpGfvAeTJLbkpU-0mTeukC0aXfB5ODQQiICJQqr9EyifRGLA0Zabih7qqlnJKTkkT78E512HELfadQMYWYAneA8UKLDQgUaqn808moqIgFmb_mV5jh3kvPNbwOsyovjEHIflljvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای حملهٔ آمریکا به مراسم عروسی در سیریک به ۵ نفر رسید
🔹
رئیس دانشگاه علوم پزشکی هرمزگان: آسیه مولایی‌نژاد، ۲۲ ساله، بعدازظهر امروز بر اثر شدت جراحات وارده به شهادت رسید و به این ترتیب شمار شهدای این حمله به ۵ نفر افزایش یافت.
🔹
در حملهٔ ۲ شب پیش آمریکا…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460068" target="_blank">📅 12:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JprWMmjZoxYAC6y2NnjabVHSh53IDz33GbRCmKm1e0C2oVbinzZuXkUVj3pVPDcCcYEaX4Qyt73N8HNh-78ykLb2OGlaJohSScX2kwN2bBWv1uQ4jaVAv7RY5xHOy-NCSjH64QU03QXbd4IfbLHE-fxmMxxdOTVkLFI4PVESPFHqbrImHv--0oLRGljt-Iruwl4e-l9TsJDOB9psE0nT0Bv23oknPF5iP-Dyo44zVQ3XaXsMdgPJPcuDMV0goA-foquSP2iFqXOhIqHfHlQT9Uc1ordjOnSDkjViBPLDc0xPDbHihx0XpUlLA_O664qYCQg2BGMqkyfqf8ncUdB9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت
🔹
وزیر بهداشت فرانسه: تا پایان ژوئیه، حدود ۷ هزار مرگ اضافی در جریان موج‌های گرمای شدید که تابستان امسال کشور را فراگرفت، ثبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460067" target="_blank">📅 11:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXBnp1IquPJ5mgWnprkODE6YBWr0mJfbzHe9cHSpi3VN44OqVtBKANhqveKyPm2CU8xBw6dSV3XhD2HwTffL9WdnJhXqiNJS_U3mWVRZ6Mb3X_wS5FfdoRVHxLUv2GMyyH3fVJdSRqVTYSZSFkPLk_bP5vEo7S3YUyd2PrkECzD8VtHIJ97oAHpsAAed0s20dSMjapk1JyoE_Z7KAvan8YCYuk7cyegngMxpZ5GR3Alyn1Kykb1_ulFB7xM785QBWQc-_XM-Bm6hjF7GQIaaZRyWZ9Ri5Oj6ZAZqj84josWcR7fXBzoKApilJY7Ivv-Kg14gg6jGLgrqdgXUhHEQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی پاسخ وزیر خارجهٔ اردن را داد
🔹
وزیر خارجهٔ اردن گفته: «ایران ۲ ساعت پس از آغاز جنگ، اردن و دیگر کشورهای منطقه را هدف قرار داد و این یعنی حملهٔ ایران پاسخ دفاعی نبوده است.»
🔹
عراقچی در پاسخ به او نوشت: به نظر وزیر خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔸
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته‌شدن ایرانیان بی‌گناه انجامید؟
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460066" target="_blank">📅 11:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmKsbLB8AgeddfVN2XkWvBztzHbuCtboM5fP-F561fB4NRtFkg0a5uLMNiat3MLP75EDJRpBians--JnFj9ixq-GoAMpzrFbQkWkwBMlEX5z11Vw-7WWbdtHDU2ClXewLoItrybpy6B_KJ5Y2trQS99dO-C6N9CjC-M0c1XAijcOGYaQbwWXk-VUWv968XxPkttC5HSWmHVmjFY2JCB2kAsvIcVVY2PIo5x_3vkAJ3mAEQCdO2QG_ynNR2Em4r97_WGl4BFADN55CImSpkVUQGcJuOFerGzVFNPneZp9jjtj8TuZPRtzwUwaT0XD31KIAhpBGyoiVwxGCP-cUXEUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ عبری: نتانیاهو و ترامپ زمین سوخته برجای می‌گذارند
🔹
معاریو: نخست‌وزیر رژیم اشغالگر و رئیس جمهور آمریکا زمین‌سوخته‌ای پشت سرشان در اراضی اشغالی و آمریکا برجای می‌گذارند.
🔹
به‌دلیل نحوهٔ رهبری ترامپ و نتانیاهو، اسرائیل و آمریکا دچار نزاع بر سر هویت و فرسایش نهادها شده‌اند.
🔹
رامپ و نتانیاهو در یک دستورکار شخصی، قومیتی و اجتماعی اشتراک دارند که به‌هیچ‌وجه دموکراتیک نیست.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460065" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJydh2IOJrZJqhyjCCZXuhRdmgGrvQR-jXxAaPnJhwpX94_IVNqScg3Kx4dfRtsDYb-Bz0cZ1S46ApmvvEFcph5qEEAiUVqsZ_Y-kYOLAKcffe5W1zZf7HMgpK4T_5fuTNOHuOTLmtqjSfSKRtP7A8kK2EQNHp5V4WBYq9Nn8N0bhMwUh_xXyCeobN4ocMpwazWlpBDy5WxzSGIL0x9XxnAE4gS9bauY6wibjzg_B62n1MpZ7S_13FsKI20h88FwxDD4N5hnT4jJXFeLjIHGWHiPZOic3rYMZqQYaKMhdth89_0r-1BG9FUXmzALTQhSRjMIpBNX_WgGAR13mGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye-pJ5-2klJBhdU3vSvkuPYiRaoONgsRqOuS5wyc3cy-mBNJzbKFLIq1TwKcyAoUqH7xToU1e8aPUMPBZT2fBy4RsvaPbSZsgmMYRKygTbAaUnpw0mUc3fOzCe4k2X3fbhrSXA_B7UNnDLwQtN_KIYT8p7_BwWNDP7EmKnDdWEp-1JLAwsZZgR7xj8EV6w7lqVZMWT5KbDo9D-zTZCLj3LM9p9DjLnlJygLVIV4h7iPrgexdr0iaiy_9QgAoa9np2odWazg9ayla5uUowwaA1hxZpAL8gd92v-RBxU8dKblJffCKm0Am-jhfd4yVGiytOymZtewuSp1FyUUy16GOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A70Qv5XjPz0rifnTJmBIYYGwwojFUB9ZuwIoDic6b2PCB_M5XhNtyta2ryk0cfm7peoQTTtp2vIhizpA6319Wv5kEUY7G2t14EBtA3XZxrsfBv7CJfiYwNCXMw16KxTjUci_IM5aAM_yxu4hBllHus4O2Ni8RSP9VVcTjcBXbfB6uzxkkztsMdeWPkD3_xnIPKWH02xYHWK3oxlkEV_pXfuzvTyyX75O0yUifh1g69-nvZ6Ae83sDKcy0SFuGeNd1xA_vfqCw0ixK_aNpU0nlrak8egzRGKNlR0VknOtd_3zf8jqxCCV0fL3WMftEoMFzH4azhIdPcT4wVeCJs8UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQC5hJPJD9Wx_aIUzCIFJo0TrGTwQAMeK2rNiJM8mQOL4e-tragWoTxmdTnUazTTC7hTMpJ81C0MufDjo0Wu0OtrFuZu4P-UWLnpstuO3Fbq6O0tCwUVi3WnvosUy7dWCFm2m_e0eD6Z1WXY2Irswjsjnmt0z6mLJ6cwWqHcmAr77yrrOp-SvGgUwye8kRC42-MaRhULZBBPYb_wKfNUNaZKyGckXe_n-lJcw0GasYkFTVEjLfFYPhqRggHwboW737P56I9uV6k9zzCrrKFfOYOZANDdPGSI6U7y3uHx2FkrrfvQ0Hv_BZzDSNqUtZeJM-llU__doc1H6m5xjCOaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuuxsWgCOPaLG1iLND4__k6-VTh3D-BfBdWtIv7Wk-atIrthCA9_WncsQLtOWp6b7dwtRjHG2RdwVNrxJGJqs93jR1DJLwv0lofHkuunUsrRk-3IL-eos4nXO_tVJ4mRmDArrXnLxe-ICLL56a-GZpN39VHRC6yTCFwUloUgmbw7OnFJEBLXZHPl8Y6ngYTbnzgluxYdhzPGFroOcVZagv6YP0-Rinx5-8DTc1FRKpFzM9IeIBKc0MFnxJmboGR41ZbIxfgOFK74eQkeKdDrUoAsdbnV5C14pGoVuUZN-23tDLaIxLSzrEKmFrwTiyN9MhRuNX1vY3qcgqUs3TV2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N15MKBp0oPbHwFKW6qtiX9sMhwIC2jDdtBHSRbH3XDy-xH30J1ok3hKD-2sRklmK_XBiJAEmEe79A5h7XwhaMYz2XEwQ4iThoL03QNpxHiIdwsiLkOanlRFZBNsIaVUJ0b7KdFMZU5YVxUth2INrkesXQlc6lUZnnA-yjEGbJBINqatlDvzDjJbhBNnF9oDqt-6zsnS1C9f4BZmF1s4i_0nRQRRCCX2ccBhK0pOznLQgFD7fpGdrCdicTJZl2kLUatoAdvkILx80XhewQUPGRpXpAe8j_hTLv338eoMg00tdzt3yWm3SJnxzrpBuNGoBceJ5N1CbXyHa3GMN-iHzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJCpk4sALVdTG3ZlrUYVfQdgG7Wt_B4mqguvukntoc9ICB7yf0SPupBWhCE5zdve8oablvp6hTFK8-J9kY5_K5VDCXA_gNuDL2IAAspwnbqYV1-imwPwhcirW1nHRh63vOkhPoXxdAP6htQOx3iVIg6PTMv9UJ7j2f3yLEAMp4RgBrHXxhL3eCI7so8sDiXPkMLjOpv8YHa9dAWtkKOl2NSQA0txutn3NvDgVeCMnpgc78wyvodaH3-TF0YD06rIjdxgUaXJH2T6p9n7puQBMgg8JMN2daICNgCuZux3JBmfAuzMHgVKdYQVo-ErEJNqB6Zi87Y3nl8L1caXJVyl6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460058" target="_blank">📅 10:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRIxl4BKuXDqPptmWvb5b8VSEffvvrbgX3qBZGozUYz91rjsjd7NN1Vfyhcqt0e4ZBmSTxN31-aOGBgEQQNmzoMFO19ozRmw0YHp4FW0FJ4Wf_4JgyKwxU13RxnGJqIZ273P8SG2dNfVQ4fCHQH3GOxmX-fpCqQje3QOQEN7xK88j6oNT3iLmoi91QXB-29ObTCufxtXaPPpzoWAT6I4z9szzrDj_KgANuncfri04vbCanuxVzY7rvjV6huJgXoiexy77-2_4vZpJPLFqcEGYgOF0e3cjPdppWdctV1kiXmRYDtNDt8oTIpa9u_DEGQBA4Xp53TvcmM3ZMoGqenfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه شوم بن‌گویر برای آواره‌کردن ۲ میلیون فلسطینی
🔹
ایتامار بن گویر، طرحی را برای آواره‌کردن ۱.۸۶ میلیون فلسطینی از غزه طی هفت سال رونمایی کرده است؛ طرحی که بن‌گویر آن را «مهاجرت داوطلبانه» می‌نامد، اما هدف آن آواره‌ کردن بخش عمده جمعیت فلسطینی نوار غزه است.
🔹
وبگاه «کریدل» (The Cradle)، بر اساس این طرح که «جدایی ۷/۱۰» نام گرفته، قرار است در سال نخست حدود ۲۵۰ هزار فلسطینی غزه را ترک کنند و شمار آوارگان طی سه سال به حدود ۱.۱۱ میلیون نفر و طی هفت سال به ۱.۸۶ میلیون نفر برسد.
🔹
بن‌گویر اعلام کرده است این طرح یکی از مطالبات اصلی حزب «قدرت یهود» در مذاکرات برای پیوستن به دولت آینده رژیم صهیونیستی خواهد بود و این حزب اجرای آن را به‌عنوان یکی از شروط خود برای ورود به ائتلاف حاکم مطرح خواهد کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460057" target="_blank">📅 10:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn-7nDhFSsQxQCsuIBCfKUuv5BvlqN5TfxysNU57QivdWQ5OyC1F7nawbc2tfp26HFkvsTVz22sEoJ16F1hSIzbLvGuZljZh7KZdA7IYj7RsWvOmY4PRCWKgv0GO0JJ7wIf0VyJK4IT1e7j-dbHASB5SXbdtO244fvJduWbNzafAmib_rtUiT2CzAnDv0LInSDDGjkxaKmr6PhflUaeGsX4nzovpa7XAVHfXo-TRmTMg4PN9J7oUhgXzxCEeXCqDlAAjtoc84idLfX65gduJs3cdhW6wgfTZR6z-DPAMQ8DW-T7TIPpQ7CGXPYfSTIhPdEUj_PceOjdVgEoNP8Kbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: ارادهٔ ایران برای گسترش روابط با چین قطعی است
🔹
‌اژه‌ای در دیدار با رئیس دیوان عالی چین: جهان درحال گذار به نظم نوین جهانی است و چین نقش مؤثری در این فرآیند ایفا می‌کند.
🔹
ظرفیت‌های علمی و فناورانهٔ چین در کنار توانمندی‌های بومی ایران، می‌تواند…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460056" target="_blank">📅 10:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6u-oxiXBkzRJ1JmOjwXGDvku6ZYQwKJmudUG0D9BosnWFFxbvV25V1JtnJxZdxyFt_lroCA4IESYMWx4eAJWUrQuBiHJXSmbMlFT14G-bcAAOc091nY19HJnl24Q4CKPOi8nJUbLxFgiO5-eIt2sUP3GAWYk2veaeQQXQMFZ9sVevDe0z4ZxxRko2k7v8yGdthrt0xDLWjEUpd19vjPSjfrbOJ6ubetZQEQkPKKcnm99nrRkvTYPt4tXUjjucj8w8MN8Pl7TYD0jTR8Rh5Thro67fuG8FVxLfBo8ulvUcCXn_85lsNGaw5EM5CwLPna8tjMVI4GNEb_MsKrMjXbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: ارادهٔ ایران برای گسترش روابط با چین قطعی است
🔹
‌اژه‌ای در دیدار با رئیس دیوان عالی چین: جهان درحال گذار به نظم نوین جهانی است و چین نقش مؤثری در این فرآیند ایفا می‌کند.
🔹
ظرفیت‌های علمی و فناورانهٔ چین در کنار توانمندی‌های بومی ایران، می‌تواند زمینه‌ساز جهشی نوین در همکاری‌های دوجانبه و تقویت اقتدار مشترک باشد.
🔹
همچنین ایجاد و گسترش بسترهای ارتباطی در حوزه‌های قضایی می‌تواند به‌عنوان یک بازوی پشتیبان، تقویت‌کنندهٔ روابط در سایر عرصه‌های راهبردی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460055" target="_blank">📅 09:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دستگیری ۴ پیمانکار و ۲ کارمند شهرداری پرند
🔹
۴ پیمانکاران و ۲ نفر کارمند شهرداری پرند به‌دلیل تخلفات مالی و اداری بازداشت شدند؛ به گفتهٔ یک منبع این دستگیری‌ها بخشی از یک زنجیرهٔ تخلفات مالی در شهرداری پرند است و تحقیقات برای شناسایی سایر عوامل در جریان است.
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/460054" target="_blank">📅 09:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee9832f4f5.mp4?token=u9mZgmJJX-RYPuI9vQKGYXFpvFvOC4mPVX4VyEzjDB8ZXIon_C5g_xZSzNZ06UBNC9NJ50w_ygpf_acQlE-b15VRg1z3TTyuI1H3ZpvdnBznEr-6voQVmVtRzSd-_-m765APqVYkMJ-A79R0H8kTuyW6X222YxEE8upqfZtB6tNiZnOt2F7kRkeiTzpK-siefUZACosNlyENgFZS8YPGOzmb8gwrjlFpfG97_Rtrq4bEUU4uGrrxgJKE6J8NgYqySI18hyeeBgJcWZc6nPiwSwFNAOdu_gI4dOrXZm8MojQ07ccCfzgL87BkT0B0O5QNJzmDmhUJKpIAdbgMrWtDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee9832f4f5.mp4?token=u9mZgmJJX-RYPuI9vQKGYXFpvFvOC4mPVX4VyEzjDB8ZXIon_C5g_xZSzNZ06UBNC9NJ50w_ygpf_acQlE-b15VRg1z3TTyuI1H3ZpvdnBznEr-6voQVmVtRzSd-_-m765APqVYkMJ-A79R0H8kTuyW6X222YxEE8upqfZtB6tNiZnOt2F7kRkeiTzpK-siefUZACosNlyENgFZS8YPGOzmb8gwrjlFpfG97_Rtrq4bEUU4uGrrxgJKE6J8NgYqySI18hyeeBgJcWZc6nPiwSwFNAOdu_gI4dOrXZm8MojQ07ccCfzgL87BkT0B0O5QNJzmDmhUJKpIAdbgMrWtDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: امروز تمام اقدامات ضدبشری علیه ایران انجام شده و دشمنان به آن افتخار می‌کنند.
🔹
اگر روزی که تروریست‌های آدمکش بیش‌از ۷۰ هزار زن و کودک را در غزه به خاک و خون کشیدند، در مقابل آن می‌ایستادند امروز آن‌ها تجاوز و حملهٔ غیرقانونی علیه کشور دیگری…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/460053" target="_blank">📅 09:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI2t_u3trXaVbuFpVt_zuRUsvrpE6Cd7qvGyN4uXVOrJAt7NG41eMdsnrN9gZFUQmy4yWZXPI0H-fprAebQLn5nOEydOXzLiY_YQo9h3mx6EADVKSclzDytmYZRqiW3fj3rXDxEXueZfrFG3KVNGNyTcFiohRPGevetWDl9hXtcyeJGlnjXj55A3C-tnTXfvKe4WcWU1saocDokvrzjrNL8Hp3LwrqmTIga-XO4xDjSgAvpofstpW9ZMbRU5W4bckorL2NSce3Qok97i5elcreSw7tXI3wl90P7Ph56VBzJUMncAG4KnY-Way58x1wo8Ct3NuwJV3rA9cb8l7VmxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460052" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea54ba0c3.mp4?token=MGQbzL8rIK8qyC__BI8VZy5RNSt5lixx1xHYNHIQ0Uv7buHWt8kYohfFqlIdqNjL5q5bIfd1IYYxXkBOTGbISYjQW7Y7fyHA8DeB9yo-UPtZ8vK7sJbbOj-waT8R9oPTLDReVtOVt8zptRfjomd8ezmvuaCWLB_Olk7ygmwO9T-1UlTLrUt6G-tRe3O6CJFJYj_sqVA1osp6C2u5GGI2Esz8p_Z5hXHpENYYd0Td5iT4LZCeBJFeqbI9LUhtxUGFxyrtqfgJ6wDzeJ4SP4tYggcqLh4t9sZd-hoSdQDMPQJCrJsqVbJ2HHxBKmYZtirO9eeu_yS15iY-WUgwGIG2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea54ba0c3.mp4?token=MGQbzL8rIK8qyC__BI8VZy5RNSt5lixx1xHYNHIQ0Uv7buHWt8kYohfFqlIdqNjL5q5bIfd1IYYxXkBOTGbISYjQW7Y7fyHA8DeB9yo-UPtZ8vK7sJbbOj-waT8R9oPTLDReVtOVt8zptRfjomd8ezmvuaCWLB_Olk7ygmwO9T-1UlTLrUt6G-tRe3O6CJFJYj_sqVA1osp6C2u5GGI2Esz8p_Z5hXHpENYYd0Td5iT4LZCeBJFeqbI9LUhtxUGFxyrtqfgJ6wDzeJ4SP4tYggcqLh4t9sZd-hoSdQDMPQJCrJsqVbJ2HHxBKmYZtirO9eeu_yS15iY-WUgwGIG2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: ایران به‌هیچ‌وجه زیر بار ظلم و زور نرفته و نخواهد رفت  @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460051" target="_blank">📅 09:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_lOHiz2hsi74qYiLahiEbe4ogRFYxhqvp6Sz3H5jy_LyTelP3NdAEdk76EMG2KXaAvihqZyq_5nNFcJBEBl0fIYsbS4m2_am0wn8YuNajw1mFovPUCLfeBuhFySkIS4JGq-5Th7jdo0-beCoSR109oAffXQsOxBpy7c5n5gkp33pd3t2Ta6AbZLE5TmctE7aUPxs7pRNBf3sqtK_5NLH46jiv0QTjRMXxWc9oyFt-lqYax6e7iA2CX8Pg556GJB5M_65lPp54oMoVM4JC43oSPyR7INT3sqnEXRXT-Q1ktke-Ax0KTVe6dynA7iqfpAB_l1Cd4XkfzLgBNMC9SSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت تولید برق کشور از ۱۰۲ هزار مگاوات عبور کرد
🔹
معاون برق وزارت نیرو: درحال‌حاضر ظرفیت تولید برق کشور از ۱۰۲ هزار مگاوات عبور کرده و اجرای طرح «۱۴ مگاپروژه ۳» با هدف توسعهٔ نیروگاه‌های تولید برق آغاز شده است،
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/460050" target="_blank">📅 09:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4a32b4e7.mp4?token=sDMw55ffKoxYzBiHlmfB6pUxg4TrUdzgcAx6v4j36Oosp-OHX9CnZm4atcYHHjeU0YztHhSsRjbj9xhV32jWnq7aXrRDFDYos3r2tkMAxQBa4wzqSF3iFT9g3zBK5Xf9xoMqhD6nJ8mx8uUQjE9Gfi_CQyryPBo9b_-9cU9Z6FU9zQdEGWgq3xPc8cFnuphgbXkDtYnnd38TEVPGnuh3OmIPvv_m0UUiA5Az7xB2JMqFl_gOIC7BhyIi9xqhLqOYQtnNX-CFKfdSV8NDkaJ6ffrayBZ2z-bO3qM7XQ9OR1L5xFT8bBCWpQow5osamoseJ5CxQYeZBI6-pIYamM20Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4a32b4e7.mp4?token=sDMw55ffKoxYzBiHlmfB6pUxg4TrUdzgcAx6v4j36Oosp-OHX9CnZm4atcYHHjeU0YztHhSsRjbj9xhV32jWnq7aXrRDFDYos3r2tkMAxQBa4wzqSF3iFT9g3zBK5Xf9xoMqhD6nJ8mx8uUQjE9Gfi_CQyryPBo9b_-9cU9Z6FU9zQdEGWgq3xPc8cFnuphgbXkDtYnnd38TEVPGnuh3OmIPvv_m0UUiA5Az7xB2JMqFl_gOIC7BhyIi9xqhLqOYQtnNX-CFKfdSV8NDkaJ6ffrayBZ2z-bO3qM7XQ9OR1L5xFT8bBCWpQow5osamoseJ5CxQYeZBI6-pIYamM20Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ایران برای استقلال خود شهدای بزرگی تقدیم کرده است
🔹
رئیس‌ قوه‌قضائیه در دیدار با علمای اسلامی و بزرگان ادیان کشور هند: ما از خون شهدا، زحمت و تلاش خود نتیجه گرفته‌ایم و سرافراز و سربلندیم.
🔹
امروز ایران تنها کشوری است که به مستکبرترین عالم یعنی آمریکا…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/460049" target="_blank">📅 09:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e1abe06.mp4?token=PxZJkbvRZTYf8RYvThzRiB-y2enu9ibipu3q9ViZtZwZOefnfh_pZdvoAc-Rk1mDcIqRWkCaGZ5Q_Z2dpc5VFrjKUe6A-SDcdIeX5j0Rgl2Y7ebnGEqVFDvfVZVEVAFUWFvDgQ1r8EqAsu6Ilkouy1Gc4oRiBTSvUhoL9SDP7Y3qWAaV0dmdxWK-GsfFgLQC4446_mE6pL5yvNlJ4FvZd1F7t0YZqYiAZNnKNXex755rUtNsMBpbDL2HTkAVckWpQ2s9e4bjddV_kkqjQiJ5PUBFe2NhtB811VUhNIVnIR3S0nUB91f_4GI2uftDJfcVeUA6sLNMGwHNJqAHxV0Hfa-D3Efz0jk2BQx3rMMNl4IZFHziNf0L1jwrR08lMAzhzWAd_LiP7hOYx6C46XZz7gJyhceqPwwFkeDu1M897PBdgfMi-EB5jJrZ_SYMdN9ZDD06oflLe_pLCreJcvrFTZXKJXf_KzhT9qMSSWH9SxVf8gq0bLpFyRWBYZt_ND7xcwX8HR_n62M27ogVz53NE1BE68yZ_ngSH4sn3C2uQ2dzLcnrZ8KE8qTPUUqC_peTkQweoFHWEExGjUPysxjwIJGVOTbOM5rTt5lzEGbpKvZmwatksxHyBlRTnFoiki-E0_AwvZZml2BIgwFoIrLYDj_QaO_UkvY7Lk81gBkSobI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e1abe06.mp4?token=PxZJkbvRZTYf8RYvThzRiB-y2enu9ibipu3q9ViZtZwZOefnfh_pZdvoAc-Rk1mDcIqRWkCaGZ5Q_Z2dpc5VFrjKUe6A-SDcdIeX5j0Rgl2Y7ebnGEqVFDvfVZVEVAFUWFvDgQ1r8EqAsu6Ilkouy1Gc4oRiBTSvUhoL9SDP7Y3qWAaV0dmdxWK-GsfFgLQC4446_mE6pL5yvNlJ4FvZd1F7t0YZqYiAZNnKNXex755rUtNsMBpbDL2HTkAVckWpQ2s9e4bjddV_kkqjQiJ5PUBFe2NhtB811VUhNIVnIR3S0nUB91f_4GI2uftDJfcVeUA6sLNMGwHNJqAHxV0Hfa-D3Efz0jk2BQx3rMMNl4IZFHziNf0L1jwrR08lMAzhzWAd_LiP7hOYx6C46XZz7gJyhceqPwwFkeDu1M897PBdgfMi-EB5jJrZ_SYMdN9ZDD06oflLe_pLCreJcvrFTZXKJXf_KzhT9qMSSWH9SxVf8gq0bLpFyRWBYZt_ND7xcwX8HR_n62M27ogVz53NE1BE68yZ_ngSH4sn3C2uQ2dzLcnrZ8KE8qTPUUqC_peTkQweoFHWEExGjUPysxjwIJGVOTbOM5rTt5lzEGbpKvZmwatksxHyBlRTnFoiki-E0_AwvZZml2BIgwFoIrLYDj_QaO_UkvY7Lk81gBkSobI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ایران برای استقلال خود شهدای بزرگی تقدیم کرده است
🔹
رئیس‌ قوه‌قضائیه در دیدار با علمای اسلامی و بزرگان ادیان کشور هند: ما از خون شهدا، زحمت و تلاش خود نتیجه گرفته‌ایم و سرافراز و سربلندیم.
🔹
امروز ایران تنها کشوری است که به مستکبرترین عالم یعنی آمریکا نه گفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460048" target="_blank">📅 09:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
هواشناسی: سامانهٔ بارشی جدید از یکشنبه وارد کشور می‌شود
🔹
با ورود این سامانه در روزهای یکشنبه و دوشنبه در اکثر مناطق شمالی کشور شاهد بارش خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/460047" target="_blank">📅 09:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6761000c20.mp4?token=X24CrN3oSiJda6uurrS5ZJkGTHe_UBT59sU_7rpUn0hMMTkdwlP15S-BHlS_d4d4Q3zO7B_u0yCfz7_JfcQOUN5Xd7oZO5tM5GT5Iv8zmaS8PXhD2Hd8Q9OKeHngyNM7sEwHzc-wGeKxzKRMmNxMdSqcs-zCZkyyQ--6eKfC0fExaOwDPWrkzepxVhYYyr5tcd7JdohWQWRgptfktlTTWIo4WD5qJFi7td5uEtHD1UJ6Bq-coOWIXxfLc_vNzDH6au2Qj8XiLyEbBLi2fUozCNqcG0gGpHeW68JVszY3PRpQ9lq3sn4a1km5LZ6OuF9nhrAd451uHP29tGkT7qv0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6761000c20.mp4?token=X24CrN3oSiJda6uurrS5ZJkGTHe_UBT59sU_7rpUn0hMMTkdwlP15S-BHlS_d4d4Q3zO7B_u0yCfz7_JfcQOUN5Xd7oZO5tM5GT5Iv8zmaS8PXhD2Hd8Q9OKeHngyNM7sEwHzc-wGeKxzKRMmNxMdSqcs-zCZkyyQ--6eKfC0fExaOwDPWrkzepxVhYYyr5tcd7JdohWQWRgptfktlTTWIo4WD5qJFi7td5uEtHD1UJ6Bq-coOWIXxfLc_vNzDH6au2Qj8XiLyEbBLi2fUozCNqcG0gGpHeW68JVszY3PRpQ9lq3sn4a1km5LZ6OuF9nhrAd451uHP29tGkT7qv0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوچ وحشی بر فراز کوه‌های بافق خودنمایی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460046" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhF9u6jf0-8kWRjcemAtmtvDCo5IdBSDHNLm64l4pUUXtM5hlZIVl1uL_wYjrU5a90qEmXUWbdJh0eEBNMXWRTKKNsi46IQPLwxBwySdMDC9ch4aACCexdiYlu83pbUxKCG_Rpwjr6ddtdlsX2EWEaY9NPLd7HUiFJqDzgEEKAxErQlFEXcefk3PIoSxmFrbouzcmyUJ9yVPWMc4qpz4-tcUEUf-7zIUn-XTGvhqrSuH0yCZtrUkxl8-51IFxJVVfjjupPhEV38NWUf7Acp4dQIEUekoxgZ8xt-Z2QMcz3r1cfjNQuLPyqUg_EjJVW6VK_39g7nGsbTgSdPcN2Su6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی شاگردان پیاتزا در اولین گام قهرمانی آسیا
🔹
تیم ملی والیبال کشورمان در اولین بازی خود در مسابقات قهرمانی مردان آسیا  ۲۰۲۶ در ۳ ست متوالی با امتیازهای ۲۵ بر ۱۵، ۲۵ بر ۱۲ و ۲۵ بر ۲۲ مقابل نیوزیلند به پیروزی رسید و در صدر جدول گروه دوم این رقابت‌ها قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460045" target="_blank">📅 08:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460040">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rysv5UArE1VDqNDfZVtqFpMpSvd44A0OQyvJjanxwhyt7LZENO3vl3DL_fy96stnVQHzETSY1wKBgd7L42Lo_zBM5ZZdpHk30kEOkMhMW9n8_FuEVJpjpu2o96JeuMKBLgSE71g77TTt4JwU0nW-c62yQ-bos4fakcJgSRQNYmb9R3a-7E-_ztIHm_FNmjHmxtabTFurfchylecV51bQfDwGWNk6NNyC4QiR9MgahjOONe8V_F-OtLBDaB1KizsDXtnHq8oIB-sFG7bNufNXBfRBab07RBnswTVeuGheo6lN2O6Q9gWm5-kxh9xaAa3JjBc49cwIwB0uNHEsW74zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBSRn9hlIpSaL0FUEkSMju9YHcu-rmrr53e6Tv_jJ3eKKzxZyp4b5cBJDiwK2BhcWwBxWy2dxZKluUFQry-nF_QuBxWWO-ntXAukYYiWTnqqROeBCcEIUIjLsPcPxk0i80YsBXYXTlRaJyQ4YpK-To_2ZPtUzY5ovLAb_EsLI-9GLwEOkx2CV8-n4gGoLwCGgb5fJxiF8-UH5_HckYYtRHniyYbeqb78xBoi8XIeQ4r9dyk7Lsb6vsRKzcxCKGUgsmwnQ0T39lNa8_rs6Ud958ryfYdV1fTW9Af2RF_rwX6mdugvSBB7VvIdIGf6OyA50FT0bB1ZfK6Vsbz3ByFs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvIRkaxcv8xb6N2xa1ZR7Km4PmHKS0GFdHPcxAmsdgE1WaQqm4yebFGMfqc0k1QlN1a73a-ggjSAJqmwGA-AaX7ukXyXYQnzji5s7Ag3qdY9-sZO6ConXfQpybYG_lTiiac9ip7Fhyd-pc7Ivzr0PizYsgwVGRU5Ve0-zHRHxitqh8IsEp8YiGaazQmK8D12sJSf9BbgZwam2CvUO2tbHTEPlAkgTUIOOSBYDWInOuXKw4uugiQ2MJ_nCGmamxDpzet6T2MsjUmrJ7kWHg8LsMiSDUJMb2PSoKymdQ7wKkv8NBTLuI18HFRV4N3KcPevb1kqdfuMy8XtdDTEjCkSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvWrrKCvPwEYwF_6hDbdxwDpt0nt3krlnrc_rqa7Spgwy91YqJU9kFUpdk-RFzI1tLFKPxholHwK1S-NO33cPUCkda8Yk3HslmCfr1LoI_fWE6Idx7w8SlvBMdIoHVgAHRFrN2PfrhX8Dm7X010Myr3gwBIOM7Pd8sAqJMG-TlFayVreI8zOnQhHPoPVOq2hr5DyRC4SGXT9zHZV3aV9WZgLzjXmEKLk_o1CkS8lQxaZZydMb2razgcYGgeGy8ukJgCyOhIjNtcX-g4ZTKYm3gsE3oRffEDps3LsBaxDymQgdrGWyRBCJE3Lepdgf0UaKung3dC_SAd1SYAMk8_Rmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzFDKuOnvPogfBs_BEr7hh16ghVUx2zjp5VL4kgn2-Wa6HIqSAD0ln4am9fvHktYRm6WGwZOvVwsIu8ZCbHLUEGJ-eS6GaVXy-KDo1J1pJAu1MVqTZNiOmvttJ2ahnpE7v8pvBD_dbc-Do0MskvhJjzhYyPvdqwYo7_DTBwVEWUyCMXtQQoBRzxn5Xqb1GxsLmfsMRQzyR26bzoeXC0_0ZEDMQ6N5GFqc7G7p4s9W7jjT2KMcvGbZxGQZpXqGL9mzjhG13k6TU2hTgQV8bK3Q16afcnkpE5CF-U6gPSMTbNSw05KJBVPmWwxkcVp6wpZ9hJ-RAdy3DwtC5MhbvUJ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین تجلیل از خانواده‌های شهدای جنگ رمضان شهرستان لامـِرد
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460040" target="_blank">📅 08:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460039">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZsFIYd0SHSWXnlvQA3ovjZrq2thMv7_3x9OaVO0XYiPCkDRqedAk3E9uAFNrNtUPUiiWNRVvvI4rGt2vMGMst8M1fC5YgfbF6RUui6TZpjDnqgKKeVkmFbSBykXqQaJ36N-IsnGxF1wTyDrMtmHg7UG1JKj4arbHvXD8v1xK29TSRPRJl4EWiF-KXq-JeNmQIBbWNt3PhlKdSPzp3C8IknpAS6xAazTNuaN6du1Fww0lEbeh5S98QleVD1guuYhh-8akf1GIns7UaecuUEYpfuBe-eHsBbLmmvG8e_qQtsUowIHrAOh8f7_ebkaW9IV2V_1fYELOjZ08ObQf9lMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: ترامپ توافقی شامل برنامۀ هسته‌ای و تنگه هرمز می‌خواهد
🔹
یک نشریۀ انگلیسی گزارش داد که میانجی‌گران در تلاشند تا چارچوبی برای مذاکرات بین تهران و واشنگتن درمورد یک توافق جدید احتمالی ایجاد کنند.
🔹
همچنین این نشریه از تصمیم ترامپ، رئیس‌جمهور آمریکا برای گنجاندن تنگۀ هرمز در هرگونه توافقی با جمهوری اسلامی ایران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460039" target="_blank">📅 08:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocu0jFWiP9-LK1JE-AFxVLF3nzeLaO00hF6SlX95vGIxsruA_Qpxpwk8Y-e2UVaBssq2FLd4pcCJdBAhV9r_tj3o5xeGsZDllX9ktjxUnm6kRGxPDmkLSsqiM_6ziy4v7rV4ld84yXKB61FuL3x4esKzsTvRvCG9x2r2zGNjXeWkDAcMaMXYoDKvMqoD7zV1zFK3O97IZBPTC3OCz-qw3wDp5rbObsVlmykQHJ1c8ElM_NpO1034RTkTTwjSS02M6dUlHt_Wm9px0YN74lum0O1kGX9bLfww3ZPb03z_OeIWDD9KcX5BF2tKdi6kyBAcu_0P1lG-HcGjPyQyRZ2f0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس از مهر حضوری هستند
🔹
وزیر آموزش‌وپرورش: تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/460038" target="_blank">📅 06:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اعتماد به هوش مصنوعی کار دست کوهنوردان داد
🔹
اعتماد گروهی از کوهنوردان کالیفرنیایی به اطلاعات نادرست هوش مصنوعی جمنای دربارۀ زمان و تجهیزات لازم برای صعود به کوه، منجر به خطری جدی و عملیات امدادونجات چندساعته شد.
🔹
کوهنوردان با اتکا به هوش مصنوعی که زمان صعود را تنها ۸ ساعت تخمین زده بود، آب و غذای بسیار کمی برداشته و از همراه داشتن لباس گرم و تجهیزات مخصوص شب خودداری کرده بودند.
🔹
اما این مسیر در واقعیت ۱۶ ساعت طول کشید و پس از تاریک شدن هوا در مسیر بازگشت، کوهنوردان از مسیر اصلی منحرف شدند.
🔹
پس از تماس با نیروهای امدادی نیز به‌دلیل شرایط نامساعد جوی امکان اعزام هلیکوپتر فراهم نشد. کوهنوردان پس از طی ۹ ساعت پیاده‌روی موفق شدند خود را به منطقۀ دارای شرایط حضور امدادگران برسانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460037" target="_blank">📅 05:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24f550794.mp4?token=q2MZWHLXxK52rl8-oxIbxC4pU5vlWz6wn91JgPeyHjJcVl2tRbWOAT7fdCZNJgQT6hdnapFZGEb0zp8cTGCvXkNtImGIt_pgkKzpfFKMod35NcWVzkXJsvFdJmWRegA4dbNLA-OMLlVY-JEPWMyhXcTdyHDjyjnYE0LjOaXR6vMNn27gQNiChbXNhi8szwauOgYsZU2tTNOCdfq9-NZxNxLIGBvwp6TVrjcgUmGrypz57LkkxYhAFQfPTFdxLbG7ID8ZNkT2apLPJTG5sKoLVDojMo_0ZEkiQWH8k8ZtcEiFO05UvXTA5KeqA0sTaeIomzd1793LhXvwuXI_JgQlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24f550794.mp4?token=q2MZWHLXxK52rl8-oxIbxC4pU5vlWz6wn91JgPeyHjJcVl2tRbWOAT7fdCZNJgQT6hdnapFZGEb0zp8cTGCvXkNtImGIt_pgkKzpfFKMod35NcWVzkXJsvFdJmWRegA4dbNLA-OMLlVY-JEPWMyhXcTdyHDjyjnYE0LjOaXR6vMNn27gQNiChbXNhi8szwauOgYsZU2tTNOCdfq9-NZxNxLIGBvwp6TVrjcgUmGrypz57LkkxYhAFQfPTFdxLbG7ID8ZNkT2apLPJTG5sKoLVDojMo_0ZEkiQWH8k8ZtcEiFO05UvXTA5KeqA0sTaeIomzd1793LhXvwuXI_JgQlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزندت گوشی نمی‌خواهد بازی می‌خواهد
🎙
هادی زینالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/460036" target="_blank">📅 04:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba6YJVcLJYGUANdNbjJ_iRE8d8yeE6pLyXZ-TJitxbmvaRmdg1EVLR6nFg5zg1B1ui5gtMbhDXH9vR7JeEJyU7nl8Om3rw3p-5648qG2DRvE0gg13gctUBgWK54P1AZh6gSUOBGRKYD5ss3tjx6CRJ9XZaqZh_c_mB4bpTSBtP2hT0Q--6kg3JO17Nty3wxbQRUkuU4hsR0G3TGH3bW1rdgAE2B7BfMqTHtqNtiNPzzZCpcgJcXwMHbMHEMgf4fZGH9krutqlry1h86ncLEobThDJLweOYTbKs_LWDB6eEClvJRZlZgB4NTVsoKx7WmSuNROzzBUWEYczwf9ZmpL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ متهم آدم‌ربایی مسلحانه در مریوان بازداشت شدند
🔹
رئیس‌کل دادگستری استان کردستان از بازداشت ۴ متهم آدم‌ربایی مسلحانه در شهرستان مریوان، در کمتر از ۲۴ ساعت خبر داد.
🔹
این متهمین چهارشنبه ۱۱ شهریور اقدام به آدم‌ربایی مسلحانه، و ضرب‌وجرح تعدادی از کارکنان ادارۀ گمرک مریوان کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/460035" target="_blank">📅 04:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma2BWuK-9S4Ach9NPo2aue6PUdJ7cB8kJQjhGN3JigygFqUYYRoScMmZb0oQDx0jfpGp1TL60H54NjeKNbXBDzcUZwz5BBSaNp0qOppobpAmjj6cXzkO8Z9zVDW8AU7BY4G0BHJlMpaguGEsYvrfV0TaWq7q17zM6LO4C_tAyPEnm3fiAX2oPGwDidSVy3P_PQIaUD_PO8SDBorcBnzxrYM35g-1FQlTAjYCsTiv3YE4mDbkvqdno7oUWvpdWuD8ABeVqwBel72Wqj5sDSDGxTWYDqVx5SWj4U7_g4EXwQxcTHZhJn3ZpJ4bGyDqS3Yik9dYuMlaaGGyLecprzFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین مدل چت‌جی‌پی‌تی رونمایی شد
🔹
اپن‌ای‌آی از مدل جدید خود با نام جی‌پی‌تی-۶ آسترا رونمایی کرد و آن را بهترین مدل خود تاکنون دانست، اما هم‌زمان هشدار داد که این مدل گاهی تلاش می‌کند از نظارت انسان‌ها دور بماند.
🔹
جی‌پی‌تی-۶ آسترا سریع‌تر و توانمندتر از مدل‌های قبلی است و می‌تواند کارهایی مانند آماده‌سازی مالیات، ساخت بازی، رندر معماری، قالب‌بندی یادداشت‌های حقوقی و جست‌وجوی آپارتمان را انجام دهد.
🔹
اما اپن‌ای‌آی می‌گوید این مدل بیشتر از نسل‌های قبلی احتمال دارد روش گام‌به‌گام حل مسائل خود را مخفی یا مبهم کند و همین موضوع ارزیابی عملکرد آن را برای انسان‌ها دشوارتر می‌کند. آسترا هنوز در مسائل پیچیده نمی‌تواند همیشه این کار را انجام دهد، اما توانایی آن برای پنهان کردن ردپای فعالیت‌هایش در حال افزایش است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460034" target="_blank">📅 03:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هیاهوی تبلیغاتی جدید وزیر خزانه‌داری آمریکا دربارۀ تحریم‌ها علیه ایران
🔹
وزیر خزانه‌داری آمریکا مدعی شد که اتحادیۀ اروپا رسما به روند «انزوای اقتصادی» علیه ایران پیوسته است.
🔹
اسکات بسنت بدون ارائه جزئیات بیشتری از این «موضع قوی و زودهنگام» قدردانی کرده است.
🔸
پیش از این رسانه‌های آمریکا گزارش داده بودند که جنگ اقتصادی دولت ترامپ علیه ایران، تاکنون ادامۀ همان سیاست فشار حداکثری با دوز بیشتری از هیاهو و جنجال‌های رسانه‌ای بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460033" target="_blank">📅 03:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko1N2-V-4fIn8yWjd5J7Ozv9KbycXT4fxAs1EcB1wxS9DWhEfjcepnUu9wF3GvuEplUEf-xwTPqtnKfKzrJE5vN_OvZT16F_QmYpO-KuOt383B6bIgQ6zoZ7y29THJEj-EXP-3k8NpH8qv1FWCyDpjjcTRvOKiRNu_5p-p8-VrMUfYUkcUfENoHlksDawZ1sPi7Uwimjl0letUSlvxvLPZP9A7ZcT5pETLUV441nBfzTxeueWUuh9MzLx5BmXzDhfHt34zsL6SdoEaH1zugElGveWQFquqTduhI0sCeVFruk147TURQv_02OoQqRCMjI9p0qAENAmlg2DcKCc8RZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حمله به عروسی در ایران ناشی از اصابت مستقیم مهمات آمریکایی بود
🔹
تحلیل کارشناسان تسلیحاتی از تصاویر و ویدئوهایی که رویترز صحت آنها را تأیید کرده، نشان می‌دهد انفجاری که روز سه‌شنبه یک مراسم عروسی را در جنوب ایران به خاک‌وخون کشید احتمالاً ناشی از اصابت مستقیم یک مهمات آمریکایی بوده است.
🔸
رویترز نوشته که این حملۀ مرگبار ناشی از برخورد یا انحراف بمب‌ها پس از اصابت به هدفی دیگر نبوده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/460032" target="_blank">📅 02:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM2BEr0bBpGXkTuv2MluOZW09uv0GDIjE954lwB--1rp5OM8aBozUqroB8H-VCB73kLLwD4YwMf4t9j1MhMTrmRf6N_nPPKR8c8ZnVsSXJ0Au6gDuHPEEIEDZ46kAVVNmxvgM4EHGdF5Y5EnELw_v3kucsB-90WA1GbUVMHiOJLBocHD9O0R60D5CLZoKxQu5hXNynEK0SCF_FPGQtYJ5A_2SeWmNYjLBZgrooNNYO4p2zdEP0jSdvfZ4DQBzAF-KQIkcYito4XkQo2pCOZik-RYCTrrA2Z_uKWqJ0mEwhiVyt_nb-WcgDy0TS4q-TPCutWX7a1pkPbKrHeNoqlqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ جایگزین معاون مستعفی وزیر جنگ آمریکا را معرفی کرد
🔹
رئیس‌جمهور تروریست آمریکا اعلام کرد که آدام تل را به‌عنوان معاون وزیر جنگ این کشور منصوب کرده است.
🔹
او جانشین دن دریسکول می‌شود که پس از ماه‌ها تنش و اختلاف با وزیر جنگ آمریکا استعفای خود را به کاخ سفید ارائه کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460031" target="_blank">📅 02:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460026">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpRXGz707nS30DTZ8LNH1ymZDoUUf9sy6mWHocKk4I4Gri6lJdJPdpeUT8m8cNOqCQAjVsguQGoNLRsF12QE0IzRZ7ChHZA_RFZT1t7_jiis2y3granoRMuK7tSU48LlsQHTVq-B3eLZac_H1OdtnZNnoNDgmjTC4w8MwPCr9faKWPOe6rO6qHxV9m2lfESRuNObz-NoHya_wCZCtTdKy_8oIKb5xs6jymEJuRuNMPmaAKf0CZVenCepx1yZQwwO-r0BvFueqkZzCkoBmJhhm9wDGYzokcpzkhhQu1petcoYcAvEmzLxkDcQPGiaf1Pyoa8_rjht9LxeP-BWrDXYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjRDRZU--pMwhd4zzVnePYldjiaKE3-ZEe3Hxc_3dtXDJHd0xd3xjKfASZ2mbDtBld9Ahe4xCfWB2ifIegZ9v0_hRKo9glClgHYdo8dfpWVJF4pgBZH_QY0RM0DSLCtSsxfCZ1x0BDc7bzv50P-D5t3pBwYjonYOi5edVU4fVAMukRlvzi1TTWloFFcuTVXlFayrV2pMA2PMRC01SaAVVjsTH5pvFwTeAJne5civAKdIE2WFOMhCOuuCnfPk7yTlK7Y-iU3B6k-Rmn4-0HMUDADoxtzIlxJCYxsUK25cN9h3j85EIu1bBm2sL_ozbrD0HErAAhqVHPkUju7ZHV8svw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEQOXFKHSzKJDdE7O_ks5ZINYExx5BPQTj2FS9CHKp1qc2L_Sh6JGBBkjyYLcWDJP9ATFPcZe72ldbjxdxFYPkdhavyXLs3IDjNjPNDvsKgiaaSXLs58FsRl9W0yeaDl-aduh27oEwshmx0DP-cgV0uRTuYy3XJ6bUr4jfPmTm016IqAmM7MPPZkgY_wvzB8ltbTu2b5RZZTFDQzvmD_JNKRLQQ9VOun_JBWsh0vGhcV4ppPx_Isw6boRXGB7jTvcE9OGel3BzjAjxgXTUdqs75bChjQPkNbWoaWrZXKCAOHdxde3Y9S7u-WVB98LUjpeIr0C0Sb9RcsiQXF6fMSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqN2GUsHnlHkNZoEnGGHEL7wDn_oLFtv0IqbhRGSkXQW_rArGdOH6b8vmNlpcZoD51F_PaQ76C9bPtO0Gkmh1ea-4H8rbogcMkyV9Y7_5xl1S1xHgXpbvd9Ae812C_GN9vDGUFIJIPEjj-ZUzMsBzOHK9C-WezFLrWKBql8OBrtLjhohMt8tg99CDXKN2Y1VWJ4YwbZKeRCitiQKL0lVN84Cd3OIIIOFCJ1cso30S1cJBXFJOOf8_C9-qsu3EFygLNc4IdOnc5Hug5D9-gVGiUQz_5r9cGGJ0LdIKZPADNuIKV9o0dYYXXu9BfPL6Wk4Tqh5HbIcJKxkcuVzDY-qcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع اهالی بندر دیّر با پیکر ۳ شهید بسیجی حملۀ آمریکا به جزیرۀ لاوان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/460026" target="_blank">📅 01:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9a5461d9.mp4?token=Y_qls0o9hHuH-UDF5T9fdRc3rnFlzkS7QjMbVAVCkz5n1EEHA7pEeHcHQk3PMZiydoP2-Sqj9MM2nRbk8HVviqu4-d_Yzz6r3qud95IOlVfr6N29aC0z1enpsEm2J3ZKZBUuXNgCETdJoQQLfOL0Zb2ZJ8FseOKUKJoZmG9NT-ZHdUPG-YH4lalf3ZE4huZCNa4jIc7ISneEotY9vFCcWBHLbSLkJOmovffMQBIxVoZGnGNfE2GBkuGxXE6d1Po0GbfP9O1SAfKUc_QdihUv_0pjADTQEMgr7Jrxek2U-HEjSLJ3URFGlXAoNI9DLPswoZEjxolNUoMeH8KXFgKpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9a5461d9.mp4?token=Y_qls0o9hHuH-UDF5T9fdRc3rnFlzkS7QjMbVAVCkz5n1EEHA7pEeHcHQk3PMZiydoP2-Sqj9MM2nRbk8HVviqu4-d_Yzz6r3qud95IOlVfr6N29aC0z1enpsEm2J3ZKZBUuXNgCETdJoQQLfOL0Zb2ZJ8FseOKUKJoZmG9NT-ZHdUPG-YH4lalf3ZE4huZCNa4jIc7ISneEotY9vFCcWBHLbSLkJOmovffMQBIxVoZGnGNfE2GBkuGxXE6d1Po0GbfP9O1SAfKUc_QdihUv_0pjADTQEMgr7Jrxek2U-HEjSLJ3URFGlXAoNI9DLPswoZEjxolNUoMeH8KXFgKpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تکثیر شهید سلیمانی وحشت دارند!
🔸
رهبر شهید انقلاب: امروز مستکبران از نام شهید سلیمانی وحشت دارند، ببینید در فضای مجازی با اسم او چه برخوردی دارند میکنند؛ از اسمش هم میترسند و از تکثیر او وحشت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460025" target="_blank">📅 01:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlDoWsP8HzB3lshrSQnHYj0yoT9nRIeXdU_4S2Kt45YRJBGm8Ni6mLk2iOVGVmJo1xrfD-3qCmXzABk4_ijLY-7VYRbtqwagbAKHVPec1Amf9wp4Yw0F-uD216pVM8P63nm36GInU1YQ5x3q05YMvB9huUMCp82x-0ffpokBcLU0hXBuGu3uwjC-Ox8mrMIwD2F_FB8YlIqv5HpxponHIZpcULJoxAc4OpCJAPJAmQZps5UG6SNqiS1-ujiXbOl73muz9XLMEg6eFaax83oYy2ink2ckoDH-4-fTDPWoXfE6db37E6gDAsaFTd5zXo74-d_yps47I-g562KuVLYCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف مهمات جنگی سنگین در مرزهای سیستان‌و‌بلوچستان
🔹
جانشین فرماندهی مرزبانی سیستان‌وبلوچستان: در درگیری با قاچاقچیان مسلح، ۴ قبضه سلاح آرپی‌جی۷، ۶ گلوله آرپی‌جی ضدزره، ۶ خرج گلوله آرپی‌جی، ۲ هزار و ۳۸۲ فشنگ جنگی کلاش و ۷۹۶ فشنگ ام۴ کشف شد.
🔸
قاچاقچیان قصد داشتند این سلاح‌ها و مهمات را برای انجام اقدامات خرابکارانه و ایجاد ناامنی وارد کشور کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460024" target="_blank">📅 01:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4a30d19.mp4?token=gjdOCXwSQlQg4MadEu-oJzBZ5GYZFJvyZlw9FU2Fp3O3KH5ocHMvl3oqWMPKh1moLxpecYe5zI4lOS9gUKDI700pCmWMgjVLQ3Vdoli_F-wO_taaKzFu_rRlZziKzmj0RWFMpTYU9nAsukqtSt7wlYDO81ttbnijMPr5R91fYaQtA9mCUZpJM6bmOGjPHxaIrq3EBVEsh5iiWMW47T3vLzk7L66XIQmqiYdFJG_D50X8CFOZTnrTqxYzbPFIaiKWVq3weF4zTKn7r5sXOcwoZgDl9QelCaBu_N9YLhPVGVxyCwh0Htc68z_bA4rXhICWkCJxvqVru5vk0_o4p9gGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4a30d19.mp4?token=gjdOCXwSQlQg4MadEu-oJzBZ5GYZFJvyZlw9FU2Fp3O3KH5ocHMvl3oqWMPKh1moLxpecYe5zI4lOS9gUKDI700pCmWMgjVLQ3Vdoli_F-wO_taaKzFu_rRlZziKzmj0RWFMpTYU9nAsukqtSt7wlYDO81ttbnijMPr5R91fYaQtA9mCUZpJM6bmOGjPHxaIrq3EBVEsh5iiWMW47T3vLzk7L66XIQmqiYdFJG_D50X8CFOZTnrTqxYzbPFIaiKWVq3weF4zTKn7r5sXOcwoZgDl9QelCaBu_N9YLhPVGVxyCwh0Htc68z_bA4rXhICWkCJxvqVru5vk0_o4p9gGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف ناخواستۀ ترامپ به عدم پیروزی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا در ماه‌های گذشته بارها مدعی شد که در جنگ علیه ایران به پیروزی رسیده است.
🔹
با وجود این او در یک لغزش زبانی جمله‌ای بر سر زبان آورد که نشان می‌دهد که حتی خودش هم به ادعاهایش در این زمینه باور ندارد.
🔹
او در سخنانی دربارۀ جنگ علیه ایران ابتدا گفت «به محض اینکه به پیروزی برسیم» اما بلافاصله سخنش را عوض کرد و گفت: «همین الان پیروز شده‌ایم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460023" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b56d43c04.mp4?token=WvNFrbiVXwIN3RrkyKIM45VneVtFNmWHkvKvneWhT9N_nT7rNCTb0Sqibcjq9FmYBMNbdy0rf_rPocN31TrLUs49wWu3UM50kZU5K6bayc_zZEQJV5RzdhJD6ACazKmdv-SmRWsLTbegxRlQpow-2C9LZDqDO8JvYvVFE4jWVwYsJEysCWA2d_XyCo75nJJl2a9VzaaC16nsdUU3dyrUVKs7VoexHa2gIpAKQKbt2LEpEKJm1BdyFw3imojra9qTqbng2zsrzhuLiD94FnaoW_qqrOp3zwt7gj03etukAEomYKlZnQFsPAyTfpZxvrE0J1UBs4RjzCjpcmxB8brFOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b56d43c04.mp4?token=WvNFrbiVXwIN3RrkyKIM45VneVtFNmWHkvKvneWhT9N_nT7rNCTb0Sqibcjq9FmYBMNbdy0rf_rPocN31TrLUs49wWu3UM50kZU5K6bayc_zZEQJV5RzdhJD6ACazKmdv-SmRWsLTbegxRlQpow-2C9LZDqDO8JvYvVFE4jWVwYsJEysCWA2d_XyCo75nJJl2a9VzaaC16nsdUU3dyrUVKs7VoexHa2gIpAKQKbt2LEpEKJm1BdyFw3imojra9qTqbng2zsrzhuLiD94FnaoW_qqrOp3zwt7gj03etukAEomYKlZnQFsPAyTfpZxvrE0J1UBs4RjzCjpcmxB8brFOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم دزفول با خلبان شهید نیروی دریایی ارتش
◾️
شهید مجتبی باقری در حملات دوشب گذشتۀ دشمن آمریکایی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460022" target="_blank">📅 00:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYTWK2pYm2Sl2yaGaNYkXZRmj3ay0BxwGtsJWTJ4Q3lnQzkwJ_eXbuOOrgzyH1Xb5nlVZdNCfHFofzCfN47QuAn3hwfngdyKtMfVrfXqOOb95PHBJHi-2tCaCPBAbUwfMBJd61-_g0fYVqSClNdoLoB_FnQKoBVh34EDgbb3EEl3zmYn9PYQrchJ3c_eTzDbP-Tcx6XGHxER9Us0RjZhUruxb_5X5zqp0PSpDTgqx52M-c4jWoZMJgrmC42e5XRLXYsPFV6Kn7euVrTcx0vXBLee5miKC_2PQNINj8tAgCV0e-U6U123U3JEUvGTEDgZSWflh-UD6uGIzl0vn9bHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن‌پالیسی: چین با ابزارهای قدرتمند خود، از فشار ترامپ علیه ایران هراسی ندارد
🔹
رسانۀ آمریکایی فارن‌پالیسی: چین با در اختیار داشتن ابزارهایی مانند امکان محدود کردن صادرات عناصر نادر خاکی به آمریکا، از فشار اقتصادی دولت ترامپ علیه تهران هراسی ندارد.
🔹
چین حتی می‌تواند در صورت هدف قرار گرفتن شرکت‌های چینی، واشنگتن را با اقدامات تلافی‌جویانه روبه‌رو کند.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/460021" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8334da6f.mp4?token=HCuWUvZs-8dLQ9HV9YSJWKnpMNB11-YwW50JBher1nL4_RtVpA_OIcHgjQY-O2t41MzVreRxQzOoADctf14mVtpe6Vf29yr5TGOYFeQOlQRdjduBYfP0r3oy7zon0wN3jZ8kXwpcYDGMHUnEXQ8U4MHkT36HAmBdoWeleQhtckyEAcmn5CTqwmc7x-XwVwNtsqzrgrlHlZhtdQ_c8Sd-zmlFn3GqqNsI0vorhF0PwRLCU98auCN4g6ZlTgWBHvqGXqjHnuWkULKKp1MXC-UdZO2riELJWC2kESrqenTg8fHzKBqamm_N2nbiOuPATIzIFzlXg4ltvK0QEW7aXkv6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8334da6f.mp4?token=HCuWUvZs-8dLQ9HV9YSJWKnpMNB11-YwW50JBher1nL4_RtVpA_OIcHgjQY-O2t41MzVreRxQzOoADctf14mVtpe6Vf29yr5TGOYFeQOlQRdjduBYfP0r3oy7zon0wN3jZ8kXwpcYDGMHUnEXQ8U4MHkT36HAmBdoWeleQhtckyEAcmn5CTqwmc7x-XwVwNtsqzrgrlHlZhtdQ_c8Sd-zmlFn3GqqNsI0vorhF0PwRLCU98auCN4g6ZlTgWBHvqGXqjHnuWkULKKp1MXC-UdZO2riELJWC2kESrqenTg8fHzKBqamm_N2nbiOuPATIzIFzlXg4ltvK0QEW7aXkv6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نیشابور در قرار ۱۸۷ خیابان را ترک نکردند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460020" target="_blank">📅 00:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حملات هوایی و توپخانه‌ای صهیونیست‌ها به جنوب لبنان
🔹
منابع لبنانی از ۳ حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در جنوب لبنان خبر می‌دهند.
🔹
توپخانه ارتش رژیم صهیونیستی هم اطراف شهرک النبطیه الفوقا‌ و کفررمان را مورد هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460019" target="_blank">📅 23:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cbc03b8f.mp4?token=qqtXrs4rZYIz9MPe0VvlpL5rONg4mBCLFWV7j_ibtzkDkYiKCBIz8hzWTdib_iXePkRIH4ncKo7PPLUgULBp1e1GCRAiwmfNcYV957_xbA8_1Gl9WzJye43Gq6YNWxz7U7e2z7AtHhzXGTeY1-nx1V153wnHTOzGwsCJR5FIv2Y36TO39_1ArXtBdKdADEtHAAt8BceZPRs5me3TG06yUbE9XFc27N4_124EjopFSkfKFXpgz_WtAo2p2fv-Ne3H9zPcvrT6jSbgeFdPmW5i89U_PZ-xg5sUQEfzjbW72GidkLJ4ts8YhCAi5W5AaNNIHNYJIMg4ZHr3nZNukXOD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cbc03b8f.mp4?token=qqtXrs4rZYIz9MPe0VvlpL5rONg4mBCLFWV7j_ibtzkDkYiKCBIz8hzWTdib_iXePkRIH4ncKo7PPLUgULBp1e1GCRAiwmfNcYV957_xbA8_1Gl9WzJye43Gq6YNWxz7U7e2z7AtHhzXGTeY1-nx1V153wnHTOzGwsCJR5FIv2Y36TO39_1ArXtBdKdADEtHAAt8BceZPRs5me3TG06yUbE9XFc27N4_124EjopFSkfKFXpgz_WtAo2p2fv-Ne3H9zPcvrT6jSbgeFdPmW5i89U_PZ-xg5sUQEfzjbW72GidkLJ4ts8YhCAi5W5AaNNIHNYJIMg4ZHr3nZNukXOD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرایان خراسان‌جنوبی؛ ۱۸۷ شب، یک قرار و روایت ماندگار همدلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460018" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
بروجردی‌ها در شب ۱۸۷ همچنان باقوت در میدان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/460017" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le78mLpPwiU8_FeTjb8jb7c5440wUvNoPix5kTw3sZyrLZX3eTxQ7Le1BWCdUN-MnVS6rmkjFxS1_dotQiyO_DtBHFwbWDXB2erNCjq7RylYCH5TgRPCftTMNQgCY40m0wpKgG7Iq_Tje7igEiKORM6UTdgNT_Igmk95K1pdIh-yUZkOaq83hYfCiwbE9vMon10-wtDSNnD5FQYWyAj52w9jsqJdHUn5d84mEod5V0qHINam7wGtn24P0SSog5q0P7nkawwE5AvF7tUR9LTiaiyyXhIQN7PEkQlQPFrmxXmO1LCcmkKDt41Al_zwiV2dsfvwyKCmcBSPX0g0K4fR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: برخلاف آمریکا، ضربات دفاعی ایران منحصرا علیه اهداف نظامی بوده است؛ گزارش رسمی قطر نیز اثبات‌کنندهٔ این واقعیت است..
🔹
سخنگوی وزارت امورخارجه، با اشاره به سند ثبت‌شده توسط قطر در اتحادیهٔ بین‌المللی ارتباطات راه دور (ITU) که در آن تاکید شده ضربات دفاعی ایران، فقط متوجه پایگاه‌های نظامی آمریکا بوده است، نوشت:
🔹
دولت قطر در سندی رسمی که به اتحادیه بین‌المللی ارتباطات (ITU) ارائه کرده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر منحصرا «متوجه تأسیسات نظامی آمریکا بوده است و هیچ منطقه غیرنظامی هدف قرار نگرفته است.
🔹
تنها استثنایی مورد ادعای قطر، حمله به یک تأسیسات گازی در ۱۸ مارس بوده است. اما در این مورد هم باید در نظر داسته باشیم که آن تأسیسات در آن زمان در خدمت عملیات‌های تجاوزکارانه آمریکا علیه ایران بود.
🔹
این واقعیت، یعنی دقت و مراقبت ایران در تعیین اهداف مورد حمله، را مقایسه کنید با عملکرد آمریکا در حملات مکرر به غیرنظامیان و اهداف غیرنظامی: مدارس، بیمارستان‌ها، مناطق مسکونی، مراسم عروسی، پل‌ها و موارد دیگر.
🔹
تفاوت عظیمی وجود دارد میان ملتی متمدن که اهمیت پایبندی به اصول اخلاقی و انسانی - حتی در دشوارترین شرایط - را آموخته است، و حاکمان جنگ‌طلبی که در قدرت‌نمایی‌های خود، هیچ اصل قانونی یا قاعده‌ اخلاقی را رعایت نمی‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460016" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pea59xaaP8HDmQ-YpEB1YZQCsaQPNO2NzLlNDq00oLBciA7DVxDizr9yMTJyAp53Qjg-r00LFo58sDwMSxKJtastNJlmeHz7jlyGUd0IKwrOk87XlVxrhff6jwu0PqAyrbCVROSBAn9fJxYVOgesQA0_PxIQ9sOT7WjNiTnh9jFywi01m-oXT5TRYeKec2BdbzyBdje1n5z8gah-zVTIRXCDIaPUJ7uopx2HKPp7z8gJe_og__Ak9Qfg2QvL9fYyIxi6hZodJlKyLWum56eiTZReZ0fc-7Ut2JY4acY4TPGbu2OgKk8quWURryHk94HbT87rKu8dykJMVLoszCRQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقدام جدید آمریکا علیه دانشگاه‌هایی که اسرائیل را تحریم کردند
🔹
گاردین: مجلس نمایندگان آمریکا روز پنج‌شنبه لایحه‌ای را علیه جنبش دانشگاهی بایکوت اسرائیل تصویب کرد.
🔹
براساس این لایحهٔ دانشگاه‌های شرکت‌کننده در بایکوت اسرائیل یا دانشگاه‌هایی که برای جلوگیری از شرکت دانشجویان در برنامه‌های تبادل دانشجو با رژیم صهیونیستی شرکت کرده‌اند، جریمه می‌شوند.
🔹
لایحه‌ی «حمایت از آزادی اقتصادی و دانشگاهی» با رأی ۲۳۷ بر ۱۶۹ به تصویب رسید، به‌طوری که ۳۳ دموکرات برخلاف هم‌حزبی‌هایشان به آن رأی مثبت دادند و تنها ۲ جمهوری‌خواه با آن مخالفت کردند.
🔹
در پی تجاوز نظامی رژیم صهیونیستی به نوار غزه، اعتراضات دانشجویی گسترده‌ای در آمریکا در محکومیت جنایات اسرائیل آغاز شد و دانشجویان تلاش کردند تا روابط دانشگاه‌های خود با اسرائیل را به حداقل برسانند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460015" target="_blank">📅 23:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43137cc482.mp4?token=iXJDP4E_3M9k-mg2J0Uh624ULiu7PQYdCXw-DKP3mguaZHkr5VQ4-YsY7vMqLCnnRH2-wC5UJF_EAiFcqDSTRvbq22hhFdwqZcq5HO_MoUUvbsVmkFrtPTI7mWCyVx5SAoBhhNwutyN4_DWvwGOYfh3AjWB-IgDy_9-FNdNQ36EmKdGZjwyY-BN6HOxMbmjT1dz4JvogTGNBn3-QeRUEInSnNnDK4jC0oV5RDn2ocSMwRSPAQQCx5jB8JqHIwRQGtPE_Ep4Np0uF3IwN-OfEiPlFgt74K7AfAmJpIPhL4rQ__QZqfn3X6KCQo7sPh126fb7QazQ53KCfz8rPJdlz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43137cc482.mp4?token=iXJDP4E_3M9k-mg2J0Uh624ULiu7PQYdCXw-DKP3mguaZHkr5VQ4-YsY7vMqLCnnRH2-wC5UJF_EAiFcqDSTRvbq22hhFdwqZcq5HO_MoUUvbsVmkFrtPTI7mWCyVx5SAoBhhNwutyN4_DWvwGOYfh3AjWB-IgDy_9-FNdNQ36EmKdGZjwyY-BN6HOxMbmjT1dz4JvogTGNBn3-QeRUEInSnNnDK4jC0oV5RDn2ocSMwRSPAQQCx5jB8JqHIwRQGtPE_Ep4Np0uF3IwN-OfEiPlFgt74K7AfAmJpIPhL4rQ__QZqfn3X6KCQo7sPh126fb7QazQ53KCfz8rPJdlz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تشییع پیکر شهید حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460014" target="_blank">📅 23:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNAdmc6FoTmXePnpTwOEOHu4dtXWaQ5aTVpe0sVfth-pNBU7WtDcr-bZq9HxMeIkhWtiygBZ8vuoPbrQ3oi0QDKLdmj8pTbXlOj4ohYSbQG_zGT366FqgVLh6p95l1SRP6h9yIdcnOqSo2O2lN97VGhznP_SQ2u-sDIcXSirDPiLxMkG-gmntpe56eIMnFSgR0zdyGkFejRg46jkA-4GBi6BJrTcytDZvZxwSbDN7Z4jgCEwvuPF99VUhOCytY_NRwOVyWSYYCJqcIVhBLXzII-cxvKrjqgjq9uoemafLBz5iA2u1H-o28RynbuMYqOS64YcJR2WO325OaL3jXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشروی انصارالله در جبههٔ تعز و فرار مزدوران سعودی
🔹
منابع یمنی از وقوع درگیری‌های شدید میان نیروهای انصارالله و مزدوران وابسته به عربستان در محور تعز و در جبهه مقبته و ساحل غربی خبر می‌دهند.
🔹
براساس گزارش‌ها، نیروهای مسلح یمن(صنعاء) موفق به سیطره بر «مناطق راهبردی جدید» در استان تعز شده و به سمت بندر المخا در حال پیشروی هستند.
🔹
بر این اساس، ده‌ها مزدور سعودی از جمله فرماندهان رده‌ اول کشته و شماری نیز به همراه خانواده‌های خود پا به فرار گذاشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460013" target="_blank">📅 23:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460008">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dmz7v6-mvmmgF1QPZ5Lo42Zt2Oic6eevSStoYWNYstDUWA0KUp4gN0hQFWeF9ffRJjQBwWIjIoo84pDrD_vIIKdlwe_03Q9osiMuKiW4Lv9Tr8HIwH1wrYwLL6NeuQhIikD4a4tAE5Si5Msn8Bv3NBlp66LgU7d0wwrVkWTdEZlRpPyi7CscyYucJ_zTdsk0Ucs-gs-ymAPjNqLjiOS68fGlGCoqXXqDMBE-LIN7vX-oZKcFfdJgRPgW9LIrv6FGcp2gSsuv4sMz3BmD0pj5ZUlZip6wXiUl9FLapYxOa1klkjMz_TxdqpHitJ_de6uYI6JeH_FArWqQOMDw9KAMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhZEML7rS8JcRDpnz_hQiNNH3upzElBKFf9JJiGPxmJIITEt_8XA98ce-CCfIXTln0yrsfidIjmyHMAqLzJb2amRyZg-QZNAH-sn7UPLyut7TEC6lZLpMuLvKE75WD60kLv5KwmUyza_RrpjAK4GfCOsf_fNLQIeota9o4XBdFay6iM2CsJCh7a2R3RF05PrHTnHmpaZ8QCad1CazRbwY5ivvywyrQ0JPf35u9jrQFbePQ2BtwLYfKhX4Jxahk9k2N8r59GTbXaHTMSpLEwgP1E8u3jQUE17TxdmE2Ucl2U5dTO-U3SmFm6A426NVIPrNVpfHALp6rvHIUXtxuvnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cyj_VAX-khfuKk0JHhLLuHfNhh3MMfl1jsK0rucAnichUEWiP80ebAaT5tAh25WqO-k1hNI4_D87zx7X93il3h6fUcrdFrHtFIKBw9g8IC_Rqydet3kJfwLIKswvMEwsaUUhzoXWHnLOejfVu3bvICJcbrUTiC2-2XKxjOsdpuQFsrNBz3bc8hvWEOIFe7ffSePWBj-epYVILY7i9TZ3UFJt2bBB_bl5N9iBMWHZrIc6_B5t3MOhqpeTsyMGwaLhZxjYE5TZ_bbo38QCTyODgYS8bGWSnozH1JxQec0rpT7UuA39JDqI_NPD10-9rviafhWvW1Gd7K6dwqyCTMEc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrT8gurI9dEePkE8BCvhF2p2I-TwBgmtuk5oo4030aZ-A3UIgzgHtqcWuR_0VWu4Vd_kZNYT93iC8zEoghciiOh2Tnnfbcj8APIQg-iiuRAAWvbsMGXvZ_fDsrXD1CGyeySjCBmV1fr58J3h2lFAFfFISkqS9rjTetPS9tdigZ3zUZu1aEd3NgIrpoaXhQd8KtC166t4T_8EcwpJJ22TCz3kZE1myrzRliIQJRDJY8h5DQnZt5G5T65RToK7Na8dqoi_Su4zmMD16g2m_N_B3uk_0Uei4wMAOYWvvHu3PbDDLyVviuqnG6ESTgbgN7xvp3RNSf34HlwhnjSogPqBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcUKvg9ONVX428L1nG-mM5-0gnMVq0wZ5gZMDS10Bq1ZQFHxjwdo0D59sLH5Nv8mUbAjmmwc3HEfSvOF3CcicnN18A5TKxiMFhHWA4J6Eir-S0VnSaRVuya9pYrb5_4ZhDd_9Hah7blMCWnRk57p9UqSozk9Ziut9A8Fs64eP-Exk7LU8akw6H7lpWN2TrvLgnKURLxG5PD1RDD08580pNGueSWoubkSuDchUqYDXBapKxpc6loaPk179Yon9ddBK0ZyN2eCtQjVg7SBu0h3PPUtCiDgjszQT5haOnc9CcLVBHHalXYt--hK04EWMW8tXXAvNJXOnPfefk373EzTjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ سردار شهید جعفر کهریزی تا زادگاهش
🔸
پیکر مطهر سردار شهید جعفر کهریزی که در حملهٔ دشمن آمریکایی به شهادت رسیده بود با حضور مردم در روستای کهریز کرمانشاه به خاک سپرده شد.  عکاس: بهروز احمدی  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460008" target="_blank">📅 23:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460007">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb0-Au2rHkvapJR_-Cpgp8wlxHVmiNm2BcnL4A520JTqoAVU0tQlpbHY1w1kKhPxGjVsVNiesRaYJoPNw4hMILYGo9-U7EO7J49X93mNnqYEHLKfuoaGN-eDDism5JJAvS69KwEV3IJFEVtHBHxlEX-0aFveKx1VPlC94aY17GjYgohcmJBPVKeD3nLnZM9PZIfpeKAlABiSwhjJ-1u8LomyM-LtGo9YOwBEq4wcXlV376B7v5CkHLbwUFQcvNrgyYuzqR8MolJY2YrlAkDmGZr6PKOew9j3WkERd1bs9AgK08iLNwsp7TVL1KfAsV9SdZdenxprG5DSaY6Ucyw_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس صهیونیست‌ها از احتمال حملهٔ موشکی ایران
🔹
شبکهٔ ۱۲ اسرائیل از نگرانی‌های این رژیم مبنی بر احتمال تلاش‌های ایران به ویژه در ایام اعیاد یهودی و هم‌زمان با سومین سالگرد ۷ اکتبر برای ضربه زدن به صهیونیست‌ها در خارج از فلسطین اشغالی خبر داد.
🔹
این شبکهٔ عبری افرود که ارزیابی‌ها در این رژیم حکایت از آن دارد که هدف حملهٔ موشکی ایران به بندر عقبه اردن، ارسال پیام هشدار به اسرائیل بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460007" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460006">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e1734fc33.mp4?token=Fqvh9XpTk7ePMszyCWS5c08wSR8QMV32GrO4Lv4RiWRQ8qcOwEs_cWz8Hu7Zbd2m_LC6GWFASguDW_2HnOc0fntOQPWPL88-kHBQoQUg1e3_ZdC3UZ7KRxFdmE_VqRdjoCieyTCc7rO1D1fs12orzS6t1anulFomqo1EwefXeYXe4kwSkNPXl0vSAaN_la3_1LZ62CHRuBrgxyxf8qtHtLf0cuh-ZWWzI9btx8aePUuXFWuJnm3xiH7PQT1TujPOuO_LvfktLfodj0Q79NX_Y70wTtC70wVggF9OSmE2cfr_LARSRCPhVnazHhP5dmwyYiFtGfu_gkxi_RE18iqqcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e1734fc33.mp4?token=Fqvh9XpTk7ePMszyCWS5c08wSR8QMV32GrO4Lv4RiWRQ8qcOwEs_cWz8Hu7Zbd2m_LC6GWFASguDW_2HnOc0fntOQPWPL88-kHBQoQUg1e3_ZdC3UZ7KRxFdmE_VqRdjoCieyTCc7rO1D1fs12orzS6t1anulFomqo1EwefXeYXe4kwSkNPXl0vSAaN_la3_1LZ62CHRuBrgxyxf8qtHtLf0cuh-ZWWzI9btx8aePUuXFWuJnm3xiH7PQT1TujPOuO_LvfktLfodj0Q79NX_Y70wTtC70wVggF9OSmE2cfr_LARSRCPhVnazHhP5dmwyYiFtGfu_gkxi_RE18iqqcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: حفاری بیش از ۳۰ حلقه چاه را در پارس جنوبی شروع کردیم که برخی از آن‌ها به نتیجه رسیده است   @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460006" target="_blank">📅 23:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460005">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53969dced.mp4?token=bomvEbBSJrPgtHX5Dd-bIDyD8f9Z7aKV-ZFP2vA_ICsy6F_5XHbHQzkRYYCxlMpTTwB6q1h0bLgX0md9T1zBOmerQxAAau3lIWQy7pfXW9opRlFJnOgZrwuHVeLc9Gvw4fgq0q7TkUfqOP-dUTobAChmbmAqap8HeJZxlCxc1TOP9iHANrj2j8MkjWhDEgLtXmNaPSDeFm70HhTEqpw_N9UVkqZ1Vwrbz7vLVptt1Iz_MSt6ays3TmT9yrMhtWmbEXfR-Zf7TQIKNSSZxRC8vdnkJM6R9RWIt6H7eRiLhmN-fmkNUAVVLiL9PTfIAbJUwF_X1Qr4LimCGgVD5N9FMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53969dced.mp4?token=bomvEbBSJrPgtHX5Dd-bIDyD8f9Z7aKV-ZFP2vA_ICsy6F_5XHbHQzkRYYCxlMpTTwB6q1h0bLgX0md9T1zBOmerQxAAau3lIWQy7pfXW9opRlFJnOgZrwuHVeLc9Gvw4fgq0q7TkUfqOP-dUTobAChmbmAqap8HeJZxlCxc1TOP9iHANrj2j8MkjWhDEgLtXmNaPSDeFm70HhTEqpw_N9UVkqZ1Vwrbz7vLVptt1Iz_MSt6ays3TmT9yrMhtWmbEXfR-Zf7TQIKNSSZxRC8vdnkJM6R9RWIt6H7eRiLhmN-fmkNUAVVLiL9PTfIAbJUwF_X1Qr4LimCGgVD5N9FMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست مردم شهرکرد از نیروهای مسلح؛ «بزن، الان که وقت انتقامه»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460005" target="_blank">📅 23:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823b00509b.mp4?token=oVJsOMwIEt6_Wah6zRjwhVYPpYK1wNGAxUqFvAwj8wDzT-qTVzjWYjbj97n5Z_VQpXeqAXaKY9BJFl_gPTzZCXAjzWNseRbL86HpoFAhPXz8URQepUZtKq-DbZVfGNDuAAh6-tkUAgp4Xi9mZeHBOYismldlBIHtzBJcD7dEJ4mxfTpqS0fQNAKls8IghsaYfLz1bAVnC9Ou9WzF5N0UOukE2wbokeHPrLvis1BK715m60ULPXSg8e_9KChXUKn9TPn-JlyqP0ipRV7u0vUWUg5b8yojaVszpi7xAx1vP3rB0_wUzq7G1T74MDa2u-Nu4O6W4fvHFHhbwJ7uffIVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823b00509b.mp4?token=oVJsOMwIEt6_Wah6zRjwhVYPpYK1wNGAxUqFvAwj8wDzT-qTVzjWYjbj97n5Z_VQpXeqAXaKY9BJFl_gPTzZCXAjzWNseRbL86HpoFAhPXz8URQepUZtKq-DbZVfGNDuAAh6-tkUAgp4Xi9mZeHBOYismldlBIHtzBJcD7dEJ4mxfTpqS0fQNAKls8IghsaYfLz1bAVnC9Ou9WzF5N0UOukE2wbokeHPrLvis1BK715m60ULPXSg8e_9KChXUKn9TPn-JlyqP0ipRV7u0vUWUg5b8yojaVszpi7xAx1vP3rB0_wUzq7G1T74MDa2u-Nu4O6W4fvHFHhbwJ7uffIVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: علت گرانی فعلی بنزین در آمریکا، حملهٔ ایرانی‌ها به کشتی‌ها [در تنگهٔ هرمز] است.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460003" target="_blank">📅 22:54 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
