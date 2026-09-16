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
<img src="https://cdn4.telesco.pe/file/XlybhMHHXus_8rIZ9HXFN1RiU_E-J-r8TScup7v0Xgmid0t2eurvIziNoKfToJckJ1dR6FoVdkudzRmJkNpIiH-WE06cSJaoQM4pflNZtC7yL3hUZmoxiDIjoBR7bmyK_vZom8zxz4t6grmO2XcOV-458Oo0t6Npv7hQ_3JiE7M1vtkCdVw0rgO_6ZpSrVLMKxjcK-ARPMVYviZb4s0UZ1lEAeKxGqoalf0HnSN793cOgUnKsYUXm6zQ2aIIx2aC1YCIJdsckVMM0bl6dJFGF7--ldlAPd6lyw2vjXxTodKLAQyQ3Pd85Zkw81bAAv2vy6zq7xxDK0WRTRKMwciY-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-462429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی دولت برای چهارمین‌بار: کالابرگ افزایش می‌یابد
🔹
سخنگوی دولت امروز گفت که «در حتمی‌‎بودن افزایش رقم کالابرگ تردید نداریم و حتما این کار اتفاق می‌افتد.»
🔹
روز گذشته رئیس‌جمهور هم گفته بود که «رقم کالابرگ حتما افزایش پیدا می‌کند.» این درحالی است که قرار…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/462429" target="_blank">📅 13:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS4zxt6Xefi8hYsNk0b9Ldm_0qq01YI_0G1V4e253E2T_w70RMu5XTO-BA5Xy7WnWMt-sBvL5BAdp2UgSMqKHO4Qzd8NkQMQVvOq-KHzucGPHOGpk19zz9Fa8dgpaXyuTjwoLMa_xpngmwZ1DNQz9gjqCxOv9etP73ODqzEJJahTbSjtyVnrdpV9ld6YgvAPih8CzNCcdkEZvgnXJQHs4qkMi5rzljnVnkudlhZBmjv7p5iqOMtddVCmaw6FvBV5XLt3ibSOcWsnjLnBcH_q7MNPxjCMHhNRfvjUcH5y1L7e2Z6xho3ZS3zfGHHd8HWxsCcsNn5GHUdFtp1gmJmEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز اولین تولید آزمایشی گازوئیل یورو۶ در ایران
🔹
پتروشیمی نوری برای نخستین‌بار در ایران تولید آزمایشی گازوئیل یورو۶ با گوگرد کمتر از ۱۰ PPM را آغاز کرد؛ ظرفیت متوسط تولید گازوئیل یورو۶ این واحد حدود ۲ میلیون تُن در سال اعلام شده است.
🔹
برای اجرای پروژه از سال ۱۳۹۹ تاکنون حدود ۶۷ میلیون یورو و ۲.۵ هزار میلیارد تومان سرمایه‌گذاری شده و ۷۰ درصد عملیات آن با توان داخلی انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/462428" target="_blank">📅 13:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diAJtMDfRTIagx6ISkZRL-e55pWuvGpZpkJjVWQAFoG3Od8-0Face0PwGB8QBntai6-iVRJcrBihGdxc7P8x9iKqT-bFeEWaDzwoecn-T9whXRF2m474kEmD5qXwLKXJBC52shQn513QUtmIdBTddUy-ketXYNOsgPfy-uZFUbjRJ5m40-Ppb5EiiTH61jZEgpN5PMSioUuJW4CiXXbC-x8fJkvlICCqzGC7BOKMjOzTF8aGiJkOxQVM2oK4sELtOef7UxgWRMTC8dGaJM85p3H2MTZLlrTEbWJ563TpFnO5lnGqeXj_zSK6HDzwH0xYWtHLSFSYOD5nod-TplHMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر حیدری: اگر آمریکا جنگ را ادامه دهد این‌بار نیروهایش در آب‌های منطقه غرق خواهند شد
🔹
جانشین رئیس ستاد کل نیروهای مسلح: قلۀ توانمندی آمریکا، نیروی دریایی و ناوهای جنگی این کشور است؛ اما چند شب پیش موشک‌های ایران ناوهای سنگین و ناوچه‌های آمریکایی را هدف قرار دادند و آسیب‌های جدی به آن‌ها وارد کردند.
🔹
آمریکایی‌ها در این منطقه دو سرنوشت محتوم دارند. اگر جنگ را ادامه دهند، قطعاً انبوهی از نیرو‌های آن‌ها، همان‌طور که تا امروز به درک واصل شده‌اند، ر عرشۀ همان ناوها به کشورشان بازخواهند گشت و انبوه دیگری از آن‌ها در قعر آب‌های منطقه فرو خواهند رفت.
🔹
امام شهید ما فرمودند که اگر ناو سلاح خطرناکی است، خطرناک‌تر از آن، سلاحی است که ناو را به قعر آب بفرستد و ان‌شاءالله این اتفاق خواهد افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/462427" target="_blank">📅 13:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462426">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی از هفتهٔ آینده
🔹
رئیس‌ بانک مرکزی: ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی با هدف جذب منابع ارزی، تأمین مالی پروژه‌های ارزآور و توسعهٔ ابزارهای مالی ارزی از هفتهٔ آینده آغاز خواهد شد.
🔹
براساس این طرح، دارندگان ارز می‌توانند…</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/462426" target="_blank">📅 13:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462425">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0d_nXiyebxQlIGBX7KRdsFZj6XCWiEy9vUMbQCLq2Gs3lmLcW-7gGtYiXBhhM2WIl0x8KorhZoe_nOAkuPb9PSmSkCkhoO4bDo45rZVhUahsywWeXfegTvtetygbIVQrn9FZDZ7hqC-9foT3H_f4ffHSJJw12-5tvhlk6nGDv4qZLrRkKzFWa5vKBGuftNVT4CExn73-8CCYvL-CkwHsOqs5w9__JFA_pl4ktmDVtM851MOmPg6d5MIaet0tl78LI36l71oLkZBGvsDNymoSwlNl5YlYtm9yqqakX17tNtWp_FcaTh_3YI2OkoM2l3qXQppSzPj-iC0vYeIR7PSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایگان‌ماندن مترو و بی‌آرتی تهران ۲ ماه دیگر تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/462425" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462424">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqBt3vsU_uElTKM8DdShCFtuYibLFOV_IcOyqVQ7-JYcVxgMOwQjHtb3nfXISZStim2CtshzReiZGB9XmyXpzxgOk-nurmbpA3K_jwltwtu_bGK3oqSctS81f6ihYYiO2KpORxYd4003jQYBJ3VNa67n5rDpw7T4FjAmEWpx8XeorT84MOOXPAJyE8CTmWVM1ihFZ4_ra7oTvsd6Jpe3nMonBat_hOUZpfuCDN480PBHhtKaAeBI7w6h1a3afK06D5eX1wLyq78YYfX92MMOYfz1mxla6EopKZdy2Uuab7pwyfJAzDHa9UeOEQt2ROG5aHSayLrjtPo4HY0lrZnZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: ۳۱ اتوبوس دوکابین در دل محاصرهٔ ادعایی آمریکا وارد ایران شد
🔹
محمدخانی: این اتوبوس‌ها دیروز وارد ایران شده و تلاش می‌کنیم با انجام سریع فرایندهای گمرکی، در نخستین هفتهٔ مهر وارد چرخهٔ خدمت‌رسانی در تهران شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/462424" target="_blank">📅 13:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462423">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAYE4g7_grIT9wM6KJ-Sxgl25bQY6KxO48aNDjB_K_ipdiMKUDVrjQNJsSFurQD2cio-xAUU6293qD483S19D9GMV1EMZhJhmhcL_XfRDvBo-a4wInSvbKNVfY9OLorntDtfw4g_DsKe8hxLGARYH68hoq2plpKoTKnyv-6NU_92zoqbt8QJNRlBs5-jGcZBlUUeRPlQs8PDDoUZK_QkEih2lLbF_YpT58j5-hMy5nJAx1FfGhWjX8HBOdVUIU7icYb9xEp9HO70zOmvgP7-jqvBG4h1p89ao3rG6N3cOaTycP9ZCgBIh8UgvwmT-vtxssRWryOh6cUrR6gEedc-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی مصرف CNG پس‌از تغییر نرخ سوم بنزین
🔹
عظیمی‌فر، معاون وزیر نفت: یک هفته پس‌از تغییر نرخ سوم بنزین به ۱۰ هزار تومان میانگین مصرف CNG در کشور نسبت به نیمهٔ نخست شهریور و مرداد، تقریبا ۲ میلیون مترمکعب در روز معادل ۱۱ درصد افزایش یافته است.
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/462423" target="_blank">📅 13:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462422">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tliKV4XL-RQvtAb3_1i8I095pHy-E2fDbPYLz8WVBRy1D7QG0oxNpzyDSkRfJn2bAU_UPYNtnXfexD2Teii1_1v2mshtM60EhLGRXhbMdjo6cfyX0JOAyXBMaSITiReYVZG-CKMHq3kNsAMXpYFNyTr4fw7qsNYZDWhICSQPgxJiESZhvNaE3FuW83yoahuZI9zZ-h5dYh86D_D_CC4CaiyBqjDEauFTT_P2MrkgwvsUZPFreFGk2DoXJGy50yyfi87gia-SbOKvZsGq_IeW9Bxa8e8M_Y4dqLVUi9Nh_SS55p7STrpivmou88ykl-BU090ev3EBEQP_LjR1ezIz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: آماده‌ایم قاطعانه از حقوق ایران دفاع کنیم
🔹
وزیر امور خارجه چین وانگ‌یی امروز در دیدار با عباس عراقچی، همتای ایرانی خود در پکن، با تأکید بر شراکت راهبردی پکن و تهران اعلام کرد که چین آماده است ضمن تقویت گفت‌وگو و همکاری با ایران، از حقوق و منافع مشروع جمهوری اسلامی ایران دفاع کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/462422" target="_blank">📅 13:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQoDhpl1lV3Xh7r9x5hRQeZ2JgWDdF8CydJrSSFihEAOnm-AzYV6uWfpD-_4bbatMIfO3TXk0al9GcPUFMBJobi57ZwjDdXNrc7iuIM_zAMmYByGRbNQOr1Vh1OTndeUjtouyMa2Gj1mdHeDuw46MxG1Fp8lAQwZLFwgj-rS-dnUYua0NXpeASrwm3AQVwSAw2wmt-8IALpgEfz456igUEzgPX2y7j8BhL3YiOK1G3nJTRZzTKTO6eWFpa2YuNW8ZdYnrhnuo4DuCsVUvIyvIXD8SoGoHXIsKCqMfcv-c3_2vNXCe7t4VOA6MhGH5mhuC0jeFImWXY9JCI7ay4ayeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: آمریکا به مونتاژ تصاویر و روایت‌سازی هالیوودی عادت دارد
🔹
سردار محبی در واکنش به روایت رسانه‌های آمریکایی دربارهٔ نجات یکی از خلبانان این کشور در ایران گفت: آمریکا عادت دارد روایت‌های هالیوودی ارائه کند. از ابتدای جنگ تاکنون نیز رئیس‌جمهور آمریکا بارها در خیال خود و در فضای مجازی پیروز شده و ایران را شکست داده است.
🔹
آمریکایی‌ها برای جبران شکست‌های خود، بخش‌هایی از فیلم‌های مربوط به مناطق و حوادث دیگر را کنار یکدیگر قرار می‌دهند تا چنین صحنه‌هایی را خلق کنند.
🔹
هم‌زمان با انتشار این روایت، تصاویری نیز در برخی رسانه‌ها منتشر شد که نشان می‌داد قطعات جنگندهٔ F-15 هدف‌قرارگرفته در همان ایام، در داخل فرغون جمع‌آوری و حمل می‌شد.
🔹
آمریکا باید بداند که این‌گونه روایت‌سازی‌ها دیگر کهنه شده و نمی‌تواند واقعیت‌های میدان را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/462421" target="_blank">📅 12:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امحای مهمات عمل‌نکرده در خارگو
🔹
بخشدار جزیرهٔ خارگ: درپی انهدام مهمات عمل‌نکرده از ساعت ۱۵ تا ۱۸ امروز در جزیرهٔ خارگو، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/462420" target="_blank">📅 12:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGAprHb_xA1UMB-0nJ7DEMwUy48Pjsale6j0PcX3ltbX3MfDmst9HtJyGx0shiFe0c_oXGn1-3akpmuNNFAmu5WdvdE_xQDzyCnfwWdHif05RwvpOWckkbAiAZuMfwcTYdvCSyd20_6DPyil8d2erCzZjHCmZ706yWr90pZ6rRQp2znhMYpa7X1dZmTSbwVmE9rIc3fCS6-ykj5AefmmsVJGvNWg0jkYWXJnY8gI4TgiM8FoWuluEov42ykun6TKztHfazAqvc8oP_ofwqMymhs6fCfcbWcb4r3P3xlISY_uL1eCfj8xHjt49fAw_rxLjh3j8p1_ynfQPPRm8nOqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۳۶ هزار واحدی به ۷ میلیون و ۵۵۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/462419" target="_blank">📅 12:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx69Z9fbhIXB3Eu3CvelOV4KwUvMMYN0OdbQjZT1qE3w_LTuOWu6tsG0orL02Ystqw8Y4Q3Tnih7dfVostJmGoH8S3pejMuZys8VjCyY-npBwxrwco1BEbpraWbK9TaDAeU2wIePQZ5Jic7z19g42A3M21Bdm8iBKMG-sDjKJaaVgFpvRC2zhFULgmdzW_cSGSJhs5Js7xR4ePK0VYmq3pbBLaqKt61vT_FpCZYWOmPVuo9UGNsBVXXmw3y35ICgXMDDEQ4x7wKIHYpecEe7-2xpSnxhbsA8m_ieVExzn3is9c3Q0WqdcuqEOjgndiAe1yLHzNIet8-UaGXY9F0eYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریکس؛ فرصت ایران برای فعال‌سازی دیپلماسی معدنی
🔹
اختصاص یک بند مستقل به «مواد معدنی حیاتی» در بیانیه پایانی اجلاس سران بریکس در دهلی‌نو، در کنار تحولات مشابه در اجلاس گروه۷، از افزایش اهمیت راهبردی این منابع در اقتصاد سیاسی جهان حکایت دارد.
🔹
در این میان، ایران می‌تواند با تکیه بر ظرفیت‌های معدنی و زیرساختی خود، پیشنهاد شکل‌گیری چارچوب همکاری بریکس در حوزه مواد معدنی حیاتی (BRICS-CMCF) را مطرح و همکاری میان اعضا را از سطح گفت‌وگو به پروژه‌های واقعی و مشترک هدایت کند.
🔹
با توجه به ریاست چین بر بریکس در سال ۲۰۲۷ و تأکید این کشور بر تقویت همکاری در حوزه منابع معدنی راهبردی، فرصت مناسبی برای تبدیل بند ۶۷ بیانیه ۲۰۲۶ به یک دستورکار عملیاتی فراهم شده است.
📌
دیپلماسی معدنی می‌تواند یکی از مسیرهای جدید ایران برای نقش‌آفرینی فعال‌تر در بریکس باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/462418" target="_blank">📅 12:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎬
پیشکسوتان سینما‌ از اهمیت حضور بیمه دی در کنار خود می گویند
🎥
گزارش ویدئویی از   دورهمی اهالی سینما در هفته بزرگداشت سینما با حمایت بیمه دی
#رونمایی
از آمفی تئاتر و کتابخانه خانه سینما</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/462417" target="_blank">📅 12:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/462416" target="_blank">📅 12:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محدودیت‌های ترافیکی آخر تابستان در جاده‌های شمال
🔹
تردد موتورسیکلت‌ها از ظهر امروز تا صبح شنبه در جاده‌های چالوس، هراز و سوادکوه ممنوع است.
🔹
در جادهٔ چالوس، محدودیت مسیر تهران و البرز به‌سمت شمال از ساعت ۱۴ جمعه آغاز و از ساعت ۱۵ مسیر پل زنگوله تا تونل البرز بسته می‌شود؛ مسیر مرزن‌آباد به تهران نیز از ساعت ۱۶ یک‌طرفه خواهد شد.
🔹
تردد کامیون و کامیونت در جادهٔ هراز نیز در ساعات ۱۲ تا ۲۴ امروز و ۸ تا ۲۴ پنجشنبه و جمعه ممنوع است و در صورت افزایش ترافیک، این جاده در روزهای جمعه و شنبه به‌صورت مقطعی یک‌طرفه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/462415" target="_blank">📅 12:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462414">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2c10ff6f.mp4?token=XUYJtJtYx3Y0_aYs4lFi6uQ5AJ8fT0hmbnF4iatBxQ9J2xv4LsVySfXpoyraJam3rMHSvaa_3cSGIJMMYgUWZCyKS-YhOkoh8trLFOIvvT-Zn86QrDnU6BL9lc5A0vNTlmWXuqMMwxdpYi5TM3oz-WhUwSKxWbTF_j_8TNot2Pz7LhgQYr7oPRDsxaEyh-k4MxxBqDKLROVEUXokzM7Z9V-j6FZbHyExWUvob1eZgm9WTeR_fPsavj-bcagB1UdaXOvdUZ2RZcL2Cau57njhyoUbSYBSmGP2184duMAr1H39anHaCdXPpND7Iiq0Zs_9RsT3PG30pyvGeosvfpYmEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2c10ff6f.mp4?token=XUYJtJtYx3Y0_aYs4lFi6uQ5AJ8fT0hmbnF4iatBxQ9J2xv4LsVySfXpoyraJam3rMHSvaa_3cSGIJMMYgUWZCyKS-YhOkoh8trLFOIvvT-Zn86QrDnU6BL9lc5A0vNTlmWXuqMMwxdpYi5TM3oz-WhUwSKxWbTF_j_8TNot2Pz7LhgQYr7oPRDsxaEyh-k4MxxBqDKLROVEUXokzM7Z9V-j6FZbHyExWUvob1eZgm9WTeR_fPsavj-bcagB1UdaXOvdUZ2RZcL2Cau57njhyoUbSYBSmGP2184duMAr1H39anHaCdXPpND7Iiq0Zs_9RsT3PG30pyvGeosvfpYmEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسارات جنگی آمریکا «رسمی» شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/462414" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462413">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">استانداری اصفهان: انفجار کنترل‌شده تا ساعت ۱۳ امروز در جنوب استان انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/462413" target="_blank">📅 11:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462412">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7-tHDgkzbbOR5K6BdnNNgV2Bz43LjaTl5k2l5R9XBdT59bLMS9g0PbWWLRzrJgtTVSuWzzW5lsa9vll8wC9xFD2pKPi6oNRnGWuPg2iClnVE4q9gJsnrit52db2by5stTJQKN8kQffsKTQle7AgymCdVrL8TMCyU7gX0Xj5u_ytAw1gtzFyftASN0RcdycLK1I2Mguw0cLiZEgzoVbdpKQp5qFDcdTKIDHggs5ZllA1Xq_e_avbYw4fKOWuPbSo1SWeSXYLU7aea1d4JXloRDn7SqdCw7UpIWjnOAacMcsWZHGIPH9pBhyZlHAW7ITfeHHDzAQ7TFo_LwioxY_enA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ثبت نام بدون کنکور در دانشکده رسانه فارس
رشته سینما و تدوین، ترکیبی از هنر و تکنولوژی است که به شما این امکان را می‌دهد تا داستان‌ها را از ایده تا پرده نهایی خلق کنید.
در این رشته با اصول فیلم‌سازی، فیلم‌برداری، تدوین، صداگذاری و جلوه‌های بصری آشنا می‌شوید و مهارت‌های لازم برای تولید آثار خلاقانه و تاثیرگذار را کسب می‌کنید.
✨
مهارت‌هایی که می‌آموزید:
🔹
فیلمنامه‌نویسی و داستان‌پردازی
🔹
فیلم‌برداری و نورپردازی
🔹
تدوین تصویر و صدا
🔹
جلوه‌های بصری و گرافیک سینمایی
🔹
کارگردانی و تولید محتوا
💼
فرصت‌های شغلی آینده شما:
🔸
تدوینگر فیلم و برنامه‌های تلویزیونی
🔸
کارگردان و دستیار کارگردان
🔸
فیلم‌بردار و مدیر تصویربرداری
🔸
طراح جلوه‌های بصری و موشن گرافیست
🔸
تهیه‌کننده و مدیر تولید
📞
همین امروز قدم اول را بردارید!
⚠️
مهلت ثبت نام تا 26 شهریور ماه می باشد
☎️
تماس: ۰۲۱۴۲۰۸۲۹۴۱ | ۰۲۱۴۲۰۸۲۹۴۲
📱
ارسال
عدد ۱۴
را به شماره
۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/462412" target="_blank">📅 11:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462411">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce0e6f6d6.mp4?token=AHn6-PjgOvhL7v9975-T8yAxdWcui-14HsczNO7ChnkuUWokeSzmZwBnLlCn6KmhamvwjWOKCNhTcIHgntWDzdbqHjWOMxz4epqEHxOSy3TmKAozsxI6pfvKnirrRIBQ_aWKZ_wkvUlwkPi-xMW6Gkl1QB85i4WHstcaJ-eRm7DvB9f8rNID34oPlqzayu4in7q1rVJQVkFrGvZr03BOb2XteXSyqv9d6S76NH1bKzTrH3NITkE7Bu2qdsdO-wIY9GXUcx3XciHV4540j4eouxviMeiPQUxl8L5JAZXaPXRkZpk_zPnLO7kXJ1kazZ1EwztqPghmVbOnWAgEpld4NZC4hE45p3ye8EOMPcTtkQwR20iKjQ3DSRdavkM1QiNcYMpf_srFaUKaFyE8AR7fgitgpkke7rlaErn2uEHaud2paQ42BN1y-v74JB6Fmzj9KClSG0Z0qPRlqBKLDHEl0Zz0zFvbyZfNF1pTg6cr5uTLV7eCkBHqxZem-TiDsUWTNiYjor92xKYLic3hwUWXRQOST5Y-PqVGGWagO3f9iN0oL2pzE589LZhQgQcxxE8r3QPZqZB6eaM2mT5OPS7TGY4_a_aOtPmXus8ETNwL5OQHZuvhCrPaWuFQID3cyN1p_Fu_7qdxMMSYBP8giGdXOd5HJX-Dm4TFQ6J6xSd75tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce0e6f6d6.mp4?token=AHn6-PjgOvhL7v9975-T8yAxdWcui-14HsczNO7ChnkuUWokeSzmZwBnLlCn6KmhamvwjWOKCNhTcIHgntWDzdbqHjWOMxz4epqEHxOSy3TmKAozsxI6pfvKnirrRIBQ_aWKZ_wkvUlwkPi-xMW6Gkl1QB85i4WHstcaJ-eRm7DvB9f8rNID34oPlqzayu4in7q1rVJQVkFrGvZr03BOb2XteXSyqv9d6S76NH1bKzTrH3NITkE7Bu2qdsdO-wIY9GXUcx3XciHV4540j4eouxviMeiPQUxl8L5JAZXaPXRkZpk_zPnLO7kXJ1kazZ1EwztqPghmVbOnWAgEpld4NZC4hE45p3ye8EOMPcTtkQwR20iKjQ3DSRdavkM1QiNcYMpf_srFaUKaFyE8AR7fgitgpkke7rlaErn2uEHaud2paQ42BN1y-v74JB6Fmzj9KClSG0Z0qPRlqBKLDHEl0Zz0zFvbyZfNF1pTg6cr5uTLV7eCkBHqxZem-TiDsUWTNiYjor92xKYLic3hwUWXRQOST5Y-PqVGGWagO3f9iN0oL2pzE589LZhQgQcxxE8r3QPZqZB6eaM2mT5OPS7TGY4_a_aOtPmXus8ETNwL5OQHZuvhCrPaWuFQID3cyN1p_Fu_7qdxMMSYBP8giGdXOd5HJX-Dm4TFQ6J6xSd75tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد «تو جنایتکار جنگی هستی» بر سر وزیر ترامپ در کنگره
🔹
جلسهٔ استماع بسنت، وزیر خزانه‌داری آمریکا در کمیتهٔ خدمات مالی مجلس نمایندگان این کشور با اعتراض‌های پیاپی فعالان ضدجنگ به تحریم‌های غیرانسانی علیه ایران همراه شد.
🔹
طبق گزارش تصویری شبکه ان‌بی‌سی، یکی از معترضان خطاب به بسنت گفت: «تحریم‌های علیه ایران که غیرنظامیان ایرانی را به‌کام مرگ می‌کشاند را متوقف کنید.»
🔹
معترض دیگری گفت: «اسکات بسنت! تو یک جنایتکار جنگی هستی. تحریم‌های علیه ایران را متوقف کنید. شرم بر همهٔ شما که اینجا نشسته‌اید و اجازه می‌دهید مردم به‌خاطر یک جنگ ناعادلانه و غیرقانونی بمیرند.»
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/462411" target="_blank">📅 11:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462410">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qczRWaJeGY1ayVaTkT__ckhtRi2tGUddGbz44qwcUHAYMUXq1ZaarCagROQZpZ3pXaF3LPB9_wXS51ZVCkEkPO4whYsP-efAv7gXY49nDOmtk3ioTAspZW5W3Z4yFPVIu_hkVZDyiZWTVUUe9U6Du8CpynYvTDHk8lQliSiuU_VZbd1QXssjxTYCNeFn__gi66zpO38A8q07lNms2wIOLzNN37TV1iilSoWn_INFLVR0maOu8kvvDEQti0cfxLPmjOoYch1YWdDckQL-XfFcVYZXtSebPl7thvx3FcQKfxnnGXLrbeaRT1LFejL5Ws-BVCgGFR2qc7GO5PA_V1aOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی قیمت گازوئیل در آمریکا
🔹
انجمن اتومبیل آمریکا اعلام کرد میانگین قیمت گازوئیل در آمریکا امروز به رقم بی‌سابقۀ ۶.۲۷ دلار در هر گالن رسید؛ رقمی که حدود ۲.۵۸ دلار بیشتر از قیمت گازوئیل در یک سال گذشته است. @Farsa</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/462410" target="_blank">📅 11:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462409">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDIphS7z8XQDlEC-VB8Lusq8tNEm1aP9UUeUPW9s8eTo6av8_XDdSWByPUV1CKSl_SueTpYTnqrMA1ihLBm91r8vP3Ks3DhTz3by74P-0yLbCW0Q9ukWmWUGaKbKeReoBpgtcU0ifZq2jM1KWWG6Sc5__vbrfiCcbCi5JRVun6EvR24V0PZ07wS44bg7qQVR_9V4Jjb5Ss9jN57_BxRAJZVG8RTkkULFujW9tPBwZ07I2jR_RL01H-BdO0wGuksPOuNRDhwmJNVJ-Clz6LUz1eQu6ZpfZwCVJxquqvevMx5mmP2Lx2NEwbfZ5byY5WqCxNjUeyfdwNYvvJ9IQaHwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: تداوم حضور آگاهانه در تمام عرصه‌های حساس ملی تنها راه پیروزی نهایی در این جنگ تحمیلی پیچیده و مدرن است
🔹
فرمانده‌کل سپاه در پیامی به‌مناسبت دویست شب میدان‌داری و حماسه‌سازی ملت ایران نوشت: دویست شب ایستادگی، دویست شب بصیرت و دویست شب تجلی «بعثت ملی» در میادین و کوی و برزن این سرزمین اسلامی، در حمایت از رزمندگان اسلام و نیروهای مسلح مقتدر کشور، حمایت از ولایت و رهبری معظم انقلاب و خونخواهی امام شهید خامنه‌ای عزیز(قدس سره) برگ زرین دیگری بر تاریخ پرافتخار انقلاب اسلامی افزود. ملت بزرگ و الهی ایران اسلامی در سایهٔ این ایستادگی دویست‌روزه چه از حیث معنوی و عرفانی و چه به لحاظ سیاسی و جایگاه بین‌المللی در افقی بالاتر قرار گرفت و شخصیتی بسیار والاتر یافت.
🔹
در این شرایط خطیر و سرنوشت‌ساز همدل و هم‌صدا با خیل فرماندهان مسئولان و رزمندگان غیور و تاریخ ساز  سپاه پاسداران انقلاب اسلامی، خاضعانه از آحاد ملت مبعوث و هوشیار ایران، از پیر و جوان، زن و مرد و از همهٔ اقشار، اصناف و سلیقه‌های مختلف سیاسی و اجتماعی که در این شب‌های تاریخی، حماسه‌ای ماندگار و بی‌نظیر تاریخی آفریدند، صمیمانه قدردانی و سپاسگزاری می‌کنم. مردم بزرگ با این ایستادگی تراز جدیدی از انسانیت و شرافت را به نمایش گذاشتید و تمدن جدید مبتنی بر کرامت انسانی را پی افکندید.
🔹
ای مردم آگاه و ولایت‌مدار، شما از همان ساعات آغازین جنگ تحمیلی سوم آمریکایی-صهیونیستی و شهادت قائد شهید امت آیت‌الله العظمی امام سیدعلی خامنه‌ای (اعلی‌الله مقامه الشریف)، با حضور اقیانوس‌گونهٔ خود در مساجد، بقاع متبرکه، مصلّی‌ها و خیابان‌ها و میادین سراسر کشور، نه فقط سوگواری کردید، که «نمایشگاه عینی حیات و ارادهٔ ملت» و « نماد وقوع تغییرات بنیادین در معادلات اجتماعی-سیاسی» منطقه و جهان شدید.
🔹
این حضور میلیونی، «بیعتی مجدد با رهبر معظم انقلاب، حضرت آیت‌الله امام سید مجتبی حسینی خامنه‌ای (مدّ ظله العالی)» و «تجدید میثاقی عمیق با آرمان‌های امام کبیر و رهبر شهید» بود که نشان داد پیوند امت و ولایت، نه فقط ارتباط سیاسی بلکه، «پیوندی ایمانی و عاطفی ریشه‌دار در عمق جان‌ها» است.
🔹
این میدان‌داری هدفمند و راهبردی، بزرگ‌ترین پشتوانهٔ معنوی و عملی برای نیروهای مسلح و رزمندگان اسلام در خط مقدم دفاع از حریم امنیت ملی و تمامیت سرزمینی است. دشمنان که گمان می‌کردند با فقدان رهبر و شخصیت‌های کم‌نظیر، ملت از نظام و ارزش‌هایش منفصل می‌شود، در محاسبه خود شکست خوردند و اکنون با تمام قوا برای ایجاد خستگی، یأس، تفرقه و فشار معیشتی متمرکز شده‌اند. اما این «اراده جمعی» و «سرمایه اجتماعی عظیم» که در سایه وحدت و اتحاد مقدس ملی شکل گرفته، اصلی‌ترین سد در برابر توطئه‌های جنگ ترکیبی و شناختی دشمن است و باز هم به شکست بزرگ آنها خواهد انجامید. این استمرار مقاومت در میدان و فوران الفت، معنویت و همدلی بزرگترین قرینه‌ای است که به یقین ما و پیروزی این مردم بی‌نظیر، می‌افزاید.
🔹
ای مردم بصیر! تداوم این حضور آگاهانه در تمام عرصه‌های حساس ملی، از جمله «اقتصاد مقاومتی در سایه وحدت ملی و امنیت ملی»، «تولید علم و فناوری»، «حفظ آمادگی همه‌جانبه دفاعی و تهاجمی » و «افزایش هوشمندی و هوشیاری در برابر جنگ رسانه‌ای و روانی جبهه دشمن»، تنها راه پیروزی نهایی در این جنگ تحمیلی پیچیده و مدرن است. پیروزی‌ای که با الطاف بیکرانه‌ خداوندی و استمرار و تبلور عزم و اراده جمعی ایرانیان، قطعی و حتمی است.
🔹
سپاه پاسداران انقلاب اسلامی مفتخر است که به عنوان سرباز ولایت و مدافع حریم امنیت ملی و منتقمان خون پاک امام شهید و دیگر شهدای اقتدار ایران اسلامی، با تمام توان در کنار شما ملت بزرگ ایستاده است و از هیچ تلاشی برای صیانت از این وحدت الهی و سرمایه راهبردی نظام که تضمین کننده غلبه بر جنگ تحمیلی امریکایی صهیونی است فروگذار نخواهد کرد و به فضل الهی با هرگونه خطای محاسباتی و تهدید تعرض و شرارت دشمن اهریمنی قاطعانه و پشیمان‌کننده برخورد خواهد کرد و یقین دارد این مسیر نورانی و تمدن‌ساز تحت رهبری حکیمانهٔ مقام عظمای ولایت و رهبری و فرماندهی کل قوا (مدّ ظله العالی)، با قدرت، حکمت و بصیرت بیشتری تداوم خواهد یافت و همانگونه که زعیم شهید فرمود؛ این شما ملت نستوه، شجاع و مبعوث هستید که کار را تمام خواهید کرد. انشاالله.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/462409" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYi24Tk6uNZ0fArTpUzkkquoPpo1ggv53WPPRbZS7kUxfhvjUM4iNOXdv4wUGIILS-hozmu4REy_m0n2Kz06vxocffWBOZiM3fcsBb07eG2ZvOnhA_XJnWtWguemioHdcBRhodBPPahJTN_UKtaHzKkAzFEooK-7W5bhCZXRzp6DPtn9EKYvwGyEwmO0flL3c_lr8t4b7YQJLFr1XUEEPHNZisqFHm8gOBT4W5ER1U2L9lnW1Y5qRkdwl6-xgy-x90ITI7S3KkcXK9n1X-UgFJITDx-9JO7yZuZW1JyZMOua2n5y1SP7brBRgDz9GF9wqCDAvZvGDsn9RNsx9Th-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIhIUu2lfMPYLWhUV4fXxbhhDlIunVzhQ7tOeZ7dNW7lM_pX09XPLroSYmXOmTPWzRv6JU6p15GqcN76R6yjbhDNhTOp4RBj63OBfKSXwejhl3gFerfHuyKRyizrlhOk6nCeGn1o6h3fgCV-Y4c_oz7ymqBFWspx-3FOdkbawZYIHXArzwQzZvZSiw8HhNuCs6wRlWUHYqKqZp8rTE4pQ6k22cU0jDl_MGEsTbcfS86irFW1A-ykqVlbB4-34kK9PGkORTGNalTTVS2yVGpOtaV1N_NnQv7-P_NdBG7vU28-qxKQkMBPaa0o9zR_aQIHZqvMvHEgpOL0wJLtnmtknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSttPwDpMKieN2w8AzV8ZrojeWDaI0qYsD5MLPG5-okdfHJ06DA4BPvn54j9xTveEkAfx7IBvDjZFSwNYtPMIqyGqIJ1AMd4iYU7uGyt7zwBW_fu-wffyZyoT2ZvB2IjZYWPBMuRYD6edk2c4aVTxB5nIoJWLzY4hTKZaWtirdxi9idJXi58OY_i5lh9WzILnwkaaGrfcN_c9ypXve51kCC2mD6yKh0_e4uO9_74G1lx7H9gbwnCr-CVhaoYjh7N1HoZNZPxJZkKHZZ7kPYngjBNWJxHmTz7K3rBqRZgx6_fdOvV4WtCCd9XV2YzJiVh_Enw68BU9i22_pCST-AVbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2135f1e48.mp4?token=cAzGkKm38k5b-plZIfbcxHVkUWfW5tHmBTUvfmiYYnFQmyoPmFWyo6wD_o8evjTZfd8o1fbn_izvau3P7P9Lj0oJhK_4srAQt9pWLDDAK_X2i_RxHibSw0se99xrZ98nSOXDMMAsf5__YgbjrPJxXypx4wQ_0Fmy2VDVlReZTLY-ef6lOn9wHFygNfZkcZoOJ9kEip_UwYq2pKvltVdICBR0MnTAZQvpyFFu5FeEQERBjm5OEkV4ONDOZtKH3Z1Ih5dWur2uU0QDJo57WTfh7k6mqp2DDYkrcfaQmAXk66soFJUvVFg2BVA56eBMKc431BfHKw9VsROZKjyxIpxFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2135f1e48.mp4?token=cAzGkKm38k5b-plZIfbcxHVkUWfW5tHmBTUvfmiYYnFQmyoPmFWyo6wD_o8evjTZfd8o1fbn_izvau3P7P9Lj0oJhK_4srAQt9pWLDDAK_X2i_RxHibSw0se99xrZ98nSOXDMMAsf5__YgbjrPJxXypx4wQ_0Fmy2VDVlReZTLY-ef6lOn9wHFygNfZkcZoOJ9kEip_UwYq2pKvltVdICBR0MnTAZQvpyFFu5FeEQERBjm5OEkV4ONDOZtKH3Z1Ih5dWur2uU0QDJo57WTfh7k6mqp2DDYkrcfaQmAXk66soFJUvVFg2BVA56eBMKc431BfHKw9VsROZKjyxIpxFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌ان‌ان: گرانی سرسام‌آور سوخت، اعتراضات جهانی را شعله‌ور کرده است
🔹
به گزارش سی‌ان‌ان، معترضان در نقاط مختلف جهان به خیابان‌ها آمده‌اند تا خشم خود را از جهش سرسام‌آور قیمت سوخت و خاموشی‌های پی‌درپی ابراز کنند؛ چراکه جنگ چندماهه آمریکا با ایران، هزینه انرژی را در سراسر جهان افزایش داده است.
🔹
در سوریه، معترضان در یک بزرگراه پرتردد لاستیک آتش زدند. در گواتمالا، معترضان برای مطالبه اقدام فوری دولت، جاده‌ها را مسدود کردند. در پرتغال هم شماری از صاحبان کسب‌وکارهای محلی و کارگران در مقابل خانه نخست‌وزیر راهپیمایی کردند. فیلیپین هم شاهد اعتراضات گسترده بوده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/462405" target="_blank">📅 11:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462404">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZm00cM2yfzExwCU4DT1Cw-TPYWiIoK0e7OjUIi2nvHcUkxDqmJ-6EqLIAwU62yIW8GDOVusm816Wl66TXHi6QQToZve-TolAy8labch4SfNDM2BtmxIees4DFKvW9E_nIFp0yYKCSJlT6VXh1VbFy9HpcURFs2TG8Xh3Iff_oGoZzzSJS1FFrCguqGzuPlzfW-0A2VKWeejB8usI_K9U9OTDvbFU_setY3SCsvkxvCKXmwoDGvd2n5Fvdx8TfLHC5iAm-OtpBjYu00qGVz-l3S1vORyirs3B2xaw0_08urNq3G9jN6U3Gm7IRP0a13_Hat0BlVyHip1F7BIpos-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه فوری پاکنژاد و شریعتمداری در آستانه مجمع هلدینگ خلیج فارس
🔹
طبق خبر رسیده امروز محسن پاکنژاد وزیر نفت و محمد شریعتمداری، مدیرعامل فعلی هلدینگ خلیج فارس جلسه مشترک برگزار کردند.
🔹
پیش‌تر رئیس‌جمهور دستور داده بود تا مسائل وزارت نفت و هلدینگ خلیج فارس از…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/462404" target="_blank">📅 11:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b7303b54.mp4?token=MUhVOdR9TyAuneLHp-FEF0Y58A1u1SEcKfvk_Ep45JQEkkBa9N0EPdvMcmlXHacMiv0dUw8xTFM54gqUbgqoPGJc-R-Q-EySGq-MjaubZVm22MhgToPgyG3vuvDF0fMBuEuVKKMYQW_vQcIYx0gaIyHghfjBFjqieZ8oOSTEK-Tl-OPXoYT1iKJ0wBr28ueCsYmc1NZNvhRHl6J58a19EN67aZzHgR1FNsrbmhek9NDiXVJPnfGPACL8TjxYXlWq1zcmcn1HyE7QKqGqdyRP9cEKwqgxLDmLMJDB4VC9LEJcRiwG19JasEmYjg_6muOWB4FIQECxeAxMDgjAivW_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b7303b54.mp4?token=MUhVOdR9TyAuneLHp-FEF0Y58A1u1SEcKfvk_Ep45JQEkkBa9N0EPdvMcmlXHacMiv0dUw8xTFM54gqUbgqoPGJc-R-Q-EySGq-MjaubZVm22MhgToPgyG3vuvDF0fMBuEuVKKMYQW_vQcIYx0gaIyHghfjBFjqieZ8oOSTEK-Tl-OPXoYT1iKJ0wBr28ueCsYmc1NZNvhRHl6J58a19EN67aZzHgR1FNsrbmhek9NDiXVJPnfGPACL8TjxYXlWq1zcmcn1HyE7QKqGqdyRP9cEKwqgxLDmLMJDB4VC9LEJcRiwG19JasEmYjg_6muOWB4FIQECxeAxMDgjAivW_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنج‌یابان زیر پای سنگ‌نگارۀ اشکانی را خالی کردند
🔹
چند روز پیش یک کوهنورد در مسیر قلۀ یخچال همدان، متوجه حفاری در پای یک سنگ‌نگاره ثبت‌ملی دوره اشکانی شد؛ حفاری‌ای که احتمالاً با تصور پیدا کردن گنج انجام شده است.
🔹
حالا بررسی کارشناسان نشان داده حدود ۱.۵ تا…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/462403" target="_blank">📅 10:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfewUUwsVSYu6QSxzavsO0cNecd8XHIGf9zZwiOgpTYCxJpZ0Xi38D9iN2E4Y9iJMMJ1FpALhPWbHEOnYFypirOBMrNU20DJksk0W9lswWT8YXEXdkv2qxu8BktcvWcRSFpbP5y8uAOB5VKo7cH-BJmm1l4I0O5e15ILPEQcCAHBB9j8bCCuxuLBPVrmiIQegW5T4BOmgSBBHg3eybzqUq_tJ8wJi918GaaXEDvNB1Yt7gdbYVv7PEeLHIELDnDUfwJgrz4CzNgdGfJO_P1-qUKMfRh6hJM0RVDjdmlq2ct1PIKgrigoUodfqJ8VPXbz1f-jgjNDRs6wglx99-t_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
یوسف مزرعه گل سوم ایران را زد
⚽️
ایران ۳ - ۱ امارات ‌@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/462402" target="_blank">📅 10:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tswhwVKrf7l-Bam9Bbgfm15ZoCHOuo_1FIiJYX7OdoABrVyxGi3oQQbBM5moXnTsoB8wLvd7gwU8It6F4qqFxOKzeK4IIZj1wh2icm3u755uNReW-47T2mGqH-D53i0XVXO62CR2X8NHi8TJieK_l6v5QGT9mfZi8h1cSuBK4P5129dZdNDVN8fPyOohNoun2Qwcve71YXH-co31Q-NAvlpx4coCRigznKz08stIKN7ddcAHi_E3gVM0-AdejmnCT4ZR83Rj1jV4JS1JXe-qpixwHAs8CWgUyFzSi8m69P2hs2YX14SYM01U6BvE2UZh9fHUnBuZQXA9-ZnrO1eEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۷ ریشتر در عمق ۱۰ کیلومتری، کنارتختهٔ فارس را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/462401" target="_blank">📅 10:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec8b30492.mp4?token=kmlIG9lYEqv_bfuK9UAKZf-pOiv__7DaHwL9NE77Uxq6f-REJYp4M-8tcNnyER2SB7Abj8qf1_085z6AF9rdJRjhvL5m-ACACKKppVWLD_ofnrQuR1mZc06dVSg4lDzQQbP7HXyxrKjY5P28bYC8L77C3mCObuqtQhGHbXhF7nsAf_NdYZb0BfTEW0HpwsQ3Bz3lk5Zxb5KRm2FJF-Z2dEzoIlPwizK_l_NXheJJArvF56AI83DB4Gw_PvllP9YjoV37I_3gbwPNKCd3eYo2_qQdsDmPo17seWcG2gchLSpJnUolLsK_cnqPVXDCvM2Pnx7_uT3U7-QOJFROR-A--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec8b30492.mp4?token=kmlIG9lYEqv_bfuK9UAKZf-pOiv__7DaHwL9NE77Uxq6f-REJYp4M-8tcNnyER2SB7Abj8qf1_085z6AF9rdJRjhvL5m-ACACKKppVWLD_ofnrQuR1mZc06dVSg4lDzQQbP7HXyxrKjY5P28bYC8L77C3mCObuqtQhGHbXhF7nsAf_NdYZb0BfTEW0HpwsQ3Bz3lk5Zxb5KRm2FJF-Z2dEzoIlPwizK_l_NXheJJArvF56AI83DB4Gw_PvllP9YjoV37I_3gbwPNKCd3eYo2_qQdsDmPo17seWcG2gchLSpJnUolLsK_cnqPVXDCvM2Pnx7_uT3U7-QOJFROR-A--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات در دقیقهٔ ۵۷ یک گل را جبران کرد
⚽️
ایران ۲ - ۱ امارات @Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/462400" target="_blank">📅 10:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0HOoabQeiCmILnMQOX9qK-4BXxhNCHpqPTpUQ6Mt_1HVXwUDe82H4YUasUs3wzjnt9rocDD1X72exB0ewtujTSLQ8mFPgfS70pmBPL9GPXFubZPHsqOjq9Ebjdbpf_mOfk236cmgn5PxeEOeOKj51gls_umrS4OYOVlWcF5vKRzd56NVDOu61ihigDjadFdrYZ0QpFEqYiQl4V85_zobzmhgu6oYG-_nm_F2-jD4wHCAasNPdx5Ooe4ElkP8Pzb1m7Y6L0FMmifsb7n-NPhWFtXnN_rV01sUQp_8zbFWZHh3siiQT486Dbr0nESwRLShHw_x2okntSkd6vjImMqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به‌دنبال اعمال تحریم‌های جدید بر روسیه و ایران
🔹
مجلس نمایندگان آمریکا قطعنامه‌ای را تصویب کرد که راه را برای رای‌گیری بعدی دربارۀ لایحۀ تحریم‌های جدید علیه روسیه و ایران هموار می‌کند.
🔹
در ماه آگوست بود که مجلس سنای آمریکا با اکثریت قاطع، لایحه‌ای…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/462399" target="_blank">📅 10:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe18d81e4.mp4?token=CrPMeQHIDVTSrRvEtqf3KpO3ATSJf-esN4Ya3zfcg5rbf0-v7ssBnoA8sXtXtDEAL0f-I72J4S-zG2uM_Em0aWbNIuNjAgs3KV7yDiMcq0ZjDeYcrESw4vRIUjZW85maEPjvYN9XexFsIA9u-FVzr1sG7HSuPTdOBSx9VhcAxNzoIR6Mg-Vv8ZFLtdbv2-Bjn5fD_e4hyxJmZdsWW7f-UQGJCTGVz9B7hvfqYPwimZM1oNeSqN8UrivSexo1cWrWj4xld4OIn-SdiwMigCi2YpvTrQpEuy_P9HwtDKMiggXT2prP7NKBPN86-YV6SCLmFGvc3WPQcffIQBlIdoIRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe18d81e4.mp4?token=CrPMeQHIDVTSrRvEtqf3KpO3ATSJf-esN4Ya3zfcg5rbf0-v7ssBnoA8sXtXtDEAL0f-I72J4S-zG2uM_Em0aWbNIuNjAgs3KV7yDiMcq0ZjDeYcrESw4vRIUjZW85maEPjvYN9XexFsIA9u-FVzr1sG7HSuPTdOBSx9VhcAxNzoIR6Mg-Vv8ZFLtdbv2-Bjn5fD_e4hyxJmZdsWW7f-UQGJCTGVz9B7hvfqYPwimZM1oNeSqN8UrivSexo1cWrWj4xld4OIn-SdiwMigCi2YpvTrQpEuy_P9HwtDKMiggXT2prP7NKBPN86-YV6SCLmFGvc3WPQcffIQBlIdoIRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرآبادی دبل کرد
⚽️
ایران ۲ - ۰ امارات @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/462398" target="_blank">📅 09:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462397">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7bf963ea.mp4?token=vYCko5zqXKbnRyFrbT_5hP3Xi5Kla_dWNvQPpP9QfH3EQC3MeiRY4dA65gX4rkur1Z9rctWiR0MVHbyHIyWKmV9LdI8i_4dtGE36kDmhfjbdHHR7zS1XGKgMctJ-C3swagIXivQrufC95IKKSGIewBPMAnvrO-LQLo1rV-byJ-ROj6CqvMga1kHYgOri9tRQFOqE4SIc3Rlyz_NyTy08f7KyOo6RMtnaQdBoNM7BKIddGTNZkimAuK8Blg2iPjzwPuMTxRCcCBUHcPfZiWbtbNHZaSBbqNhNfVD443Rl9QK93-aATYWCK4l9IAoomypzstKbakkhz0R68Nj9cD6rAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7bf963ea.mp4?token=vYCko5zqXKbnRyFrbT_5hP3Xi5Kla_dWNvQPpP9QfH3EQC3MeiRY4dA65gX4rkur1Z9rctWiR0MVHbyHIyWKmV9LdI8i_4dtGE36kDmhfjbdHHR7zS1XGKgMctJ-C3swagIXivQrufC95IKKSGIewBPMAnvrO-LQLo1rV-byJ-ROj6CqvMga1kHYgOri9tRQFOqE4SIc3Rlyz_NyTy08f7KyOo6RMtnaQdBoNM7BKIddGTNZkimAuK8Blg2iPjzwPuMTxRCcCBUHcPfZiWbtbNHZaSBbqNhNfVD443Rl9QK93-aATYWCK4l9IAoomypzstKbakkhz0R68Nj9cD6rAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرآبادی گل اول ایران را به‌ثمر رساند
⚽️
ایران ۱ - ۰ امارات @Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/462397" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfrLq_BknAADjGF0sbLv_PAgz2KR9J1tvxfEBhYKmIkrpKDE7kUUw9ZZvrzjRMajxNJq4IKf1UYJn0Boy0h-Sae153fVFHFspiInWZcpiJDZNkfFlKrvg9LEqhrG8XnBDokfK7Iv_Y7K6queIXg5DGkhuqaSKN5xiRGNjRJv7I_lTqmgmUb6w3b6RNYpiAvC5wgeydJRHT3pUTEXUD1kZsJwCKPry_Od8YHhHx5XYTLBoatlEBEQkxuWGqAUj1z0_6qoHRiT0lZ_oEf2p40yaOOqvaBQdUfAfmblR-xl24dp4jg1n05okqO1hm8meSHLVPi8pARcLXolGC-FC8XQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان ایران وارد فاز تازه شد
🔹
پیش‌بینی وضعیت هوا برای امروز نشان می‌دهد ناپایداری جوی در بخش‌هایی از شمال، شمال‌شرق و جنوب‌شرق کشور ادامه دارد و این مناطق در ساعات بعدازظهر و اوایل شب شاهد رگبار و رعدوبرق‌های محلی خواهند بود.
🔹
آذربایجان‌‌شرقی، آذربایجان‌غربی، اردبیل، گیلان، مازندران، گلستان و ارتفاعات البرز در کنار بخش‌هایی از خراسان‌شمالی و خراسان‌رضوی مستعد بارش‌های پراکنده هستند.
🔹
در جنوب‌شرق نیز جنوب کرمان، شرق هرمزگان و مناطقی از سیستان‌وبلوچستان احتمال رگبار و رعدوبرق دارند.
🔹
در مقابل، مرکز، جنوب و جنوب‌غرب کشور همچنان تحت تأثیر هوای گرم و پایدار قرار دارند و بارش گسترده‌ای برای این مناطق پیش‌بینی نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/462396" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGaidMjhRcQHxyS6dhNBhc1YIl00Ur5Nsuhli8pBLQ7HbVBh3TAxOFFVxTSXIt9Uv0_jR4tvwX6n4rAK6Bk9P-l6KCbEHADCtnkT3JeOWejaCmIt8tBei-AiOfBo8oktkN1zDbi0L1rpzttpR9Bpk96dp0wssuabm_oB3DL7PcVSvmLkk4NMl2Q-ulpw2phZFfRHf8-8BVzdXcLroTgK_YdyFsPrcd7_-yHyaZ24ADOUyqwD218Fts_qxw7Tw5WRUXSEnw16bYODJFX1v5affXg-xsOgLOiTmTee-J5uIVgKatrYSo12axJpbrjNyKe0bf-TGyhenQDXVTY9dJlWKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/462395" target="_blank">📅 09:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
پیکر شهید مولوی گرگیچ در زاهدان تشییع شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/462394" target="_blank">📅 09:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0d2dd5a9.mp4?token=aqCAqyDB1Yll3-wTsKXIUUHc0fwF03o00vto7w76EsDZ9ZYLL9m_oPLQgotMbR_W1XK86TbN8rDKnift20lC54y_kXBwB3vlPcSNJrARDCzkasy-kOoeCm4YQtlKjityHUEeHUnLYIGRTwJEPDRVv8fXIPUuBIHdRj8-a2njgDSpWk74NjhNlhfY5zrqpzLFDDwmyK7Svk3s7pDB1Ngy3nrsE3L7xhK-GiDzaro15Q-3O_0pChoEIu224VS4O0aKBjEHfLF-Fmo12whM0opksJxrV5UNbVVS077JiKrOa5Qe6-_cZGYAaawu1TfTKMbis0Z-Z6ft89qyBgxtywjqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0d2dd5a9.mp4?token=aqCAqyDB1Yll3-wTsKXIUUHc0fwF03o00vto7w76EsDZ9ZYLL9m_oPLQgotMbR_W1XK86TbN8rDKnift20lC54y_kXBwB3vlPcSNJrARDCzkasy-kOoeCm4YQtlKjityHUEeHUnLYIGRTwJEPDRVv8fXIPUuBIHdRj8-a2njgDSpWk74NjhNlhfY5zrqpzLFDDwmyK7Svk3s7pDB1Ngy3nrsE3L7xhK-GiDzaro15Q-3O_0pChoEIu224VS4O0aKBjEHfLF-Fmo12whM0opksJxrV5UNbVVS077JiKrOa5Qe6-_cZGYAaawu1TfTKMbis0Z-Z6ft89qyBgxtywjqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیدهای فوتبال ایران زیر باران شدید ناگویا برای بازی با امارات به ورزشگاه رسیدند  @Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/462393" target="_blank">📅 09:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c265180dd3.mp4?token=X2eLRKXkOo6aHSahn-5r4Wrx05o69VPoPpdzBSxWOzbRNLfftmxJlNFqAmt7W-vzpLPfv5g6eR_XHZ181X4El_7Z0XdxbW9WR9QsPX1aH9ON8gJD-mTEbGGWPFSCob6nTGT8JM5M70Jbftt35T44rZoVn_XoW-XlTCFN6HfQJ-ouCx9wEPxD5-7p97WbG2iUqfPMeyO7JV-6-b1z3Ul-4FoXWncTXwYucnekn0R4cvOrb155j6RTxG71CG1uGOhDhMhoiF90VTRrnzDBWYfrdCKNecRZJCfWziObz9bHXmPbn0Zt2V2YIg2dam8seFBRxqdEdJJQzzb04h7vCYxfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c265180dd3.mp4?token=X2eLRKXkOo6aHSahn-5r4Wrx05o69VPoPpdzBSxWOzbRNLfftmxJlNFqAmt7W-vzpLPfv5g6eR_XHZ181X4El_7Z0XdxbW9WR9QsPX1aH9ON8gJD-mTEbGGWPFSCob6nTGT8JM5M70Jbftt35T44rZoVn_XoW-XlTCFN6HfQJ-ouCx9wEPxD5-7p97WbG2iUqfPMeyO7JV-6-b1z3Ul-4FoXWncTXwYucnekn0R4cvOrb155j6RTxG71CG1uGOhDhMhoiF90VTRrnzDBWYfrdCKNecRZJCfWziObz9bHXmPbn0Zt2V2YIg2dam8seFBRxqdEdJJQzzb04h7vCYxfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
🔹
سردار محبی: ما امروز مصادیق قدرت را یکی پس از دیگری به نمایش می‌گذاریم. نمونه بارز آن، جلوگیری از عبور و مرور هرگونه شناور بدون هماهنگی و نیز ممانعت از ورود جنگ‌افزارهای دشمن است.…</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/462392" target="_blank">📅 09:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVFVfH7zO0aZVyVC2Nq_Yld4-blyiTDQCDeyyCqhgwxCF0u4X9TBFyA9crDq_xSMxX7B-aRtChw9jYO2RmwnD6BFSSe113S8UWsukP2mNEKDYdcHVZjStHa2CgRghmJVM6wd2h1FkXDzxtwTXccKewXiRHN337K3R6bXjVzF8nhfKzt9EkmKMHF_YYm1R78WNy-mG_04MFOW5K0rc3eGPZ-HDbnYREHl-MZXzAWmNnYzEAfX6nli7ordRBRHj4h2mBm4msE-n3wNxQ7xSD-CekWyNH6-qyhdmU3H0kOz3m59695DaE5cPen824QJqqbncaLx90UgQkWmn8FhhBWSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود تیم‌ملی بسکتبال با شکست اردن در ناگویا
🔹
تیم ملی بسکتبال ایران در سومین دیدار خود در مرحلۀ گروهی بازی‌های آسیایی ناگویا، بامداد امروز برابر اردن به میدان رفت و با نتیجۀ ۸۱ بر ۶۸ به پیروزی رسید تا راهی مرحلۀ یک‌چهارم نهایی این رقابت‌ها شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/462391" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae733e101.mp4?token=lhsrHuhFvglmkA_voHxYAisvalzdakxuZrdVi8I-vDKJz7do1CUNpC7tMbWBMj6qRHBrLe2E64Im-RzDP6m7n0vjPpFU-tulkEIKlWOmRS-Cnm6tLEQYeaRklSS-DjfsrV1D5Iknb6hKksCXVOrznq6iOz1addDSWZ_KVR4zNFzDTsVUYBjtQEVR8ZjVOWruyBGGHxzyIu7FuPl6rE2qKB9TIYVa9-2qSLIFbCpDQfKGXr-Ewx5rVoADhazDm8stlJw7LuQYNwTis00s7TJvxCpgNjDut4PiNduSyFilRGxdugC9y-461gQJmte_1z4VHLPUsgQvsF8h24zOBWB0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae733e101.mp4?token=lhsrHuhFvglmkA_voHxYAisvalzdakxuZrdVi8I-vDKJz7do1CUNpC7tMbWBMj6qRHBrLe2E64Im-RzDP6m7n0vjPpFU-tulkEIKlWOmRS-Cnm6tLEQYeaRklSS-DjfsrV1D5Iknb6hKksCXVOrznq6iOz1addDSWZ_KVR4zNFzDTsVUYBjtQEVR8ZjVOWruyBGGHxzyIu7FuPl6rE2qKB9TIYVa9-2qSLIFbCpDQfKGXr-Ewx5rVoADhazDm8stlJw7LuQYNwTis00s7TJvxCpgNjDut4PiNduSyFilRGxdugC9y-461gQJmte_1z4VHLPUsgQvsF8h24zOBWB0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیکر شهید مولوی یوسف گرگیچ فردا در زاهدان تشییع میشود
🔹
پیکر مطهر شهید یوسف گرگیچ فردا صبح از میدان امام حسین تا گلزار شهدای شهرستان زاهدان بر دستان مردم شهید پرور زاهدان تشییع میشود. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/462390" target="_blank">📅 09:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz8yul4YDtXIXvq0JnJSZglDYKn2Cj6xu-H3KCd9jTrsENwMejKV8xyz3OR3U_SWOQsmhT6xu4Vj-aJBpQs-NDApuCUlUE3sRtdBsPO-23ejxOQYn9W1TARib8KzvATZsLv1LpdKgFy3yz12oRR0mGpDnV6He5XKviwt8q7A7zoBffwDnojiq09WUiU-rq9SXvGjmFDOZvNQWubgrICuRHm8NDUxDBoy6OXZW1_BcbyBRByCUlEcNwVN4ILazGd9JBFu4qHBwUK2VZeqTFz66b5d2Ya8ZlD6YRlLeTpXK0JygAracVn33b-GIhj1O2fvl8qN09Gyivtx9wm4xjtptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قالیباف: پاسداری از ایران و وحدت ملت، مرز و مذهب نمی‌شناسد
🔹
رئیس مجلس در پیام تسلیت شهادت مولوی گرگیج: ترور ناجوانمردانه روحانی مجاهدی که عمر خویش را در مسیر دفاع از امنیت مردم، تقویت وحدت و همدلی مسلمانان و صیانت از عزت و تمامیت ارضی ایران اسلامی سپری…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/462389" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🖼
عضو ارشد انصارالله در واکنش به خبر سرنگونی اف-۱۵ سعودی‌ها: دیگر بدبختی‌ها به‌صورت جداگانه بر سر دشمن سعودی نازل نمی‌شوند؛ یکی پس‌از دیگری به‌سراغ او می‌آیند.  @Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/462388" target="_blank">📅 09:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4501b71d6.mp4?token=kiFtLEKZvUmppSC73QQ740kPvFkDDIJzppRE8MN7XUyn3yrB6E5BAb6VoYcpzZZjO8ow7ZjkejBNDPdPpT8uoWEgLiTW6_AS65leYnPkysuw8kdTFzPEWvrTPUAU5LcE-ZosunMas8n8KLJPdcj0W_Om4Fad39HrYmBkBnpz4oMuGZSrmEhbpVkJbsS5fbQm4mvDn2JbVIOtNxIsK5-GZleapcggl_hqutwQFpXbN9byu0d8AQwCVg84wB7A0ToTiriukKfqzGUcklTxbJmkxYJ5tF6MwcZlJJmQ6nRG4_j2kH2ZQuBf1nPFFUdU7nmF83-qk4io1E9-iPrdmxKjYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4501b71d6.mp4?token=kiFtLEKZvUmppSC73QQ740kPvFkDDIJzppRE8MN7XUyn3yrB6E5BAb6VoYcpzZZjO8ow7ZjkejBNDPdPpT8uoWEgLiTW6_AS65leYnPkysuw8kdTFzPEWvrTPUAU5LcE-ZosunMas8n8KLJPdcj0W_Om4Fad39HrYmBkBnpz4oMuGZSrmEhbpVkJbsS5fbQm4mvDn2JbVIOtNxIsK5-GZleapcggl_hqutwQFpXbN9byu0d8AQwCVg84wB7A0ToTiriukKfqzGUcklTxbJmkxYJ5tF6MwcZlJJmQ6nRG4_j2kH2ZQuBf1nPFFUdU7nmF83-qk4io1E9-iPrdmxKjYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت خارجهٔ چین: وزیر امور خارجهٔ ایران فردا به چین سفر خواهد کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/462387" target="_blank">📅 08:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رأی مجلس نمایندگان آمریکا به پایان جنگ علیه ایران
🔹
مجلس نمایندگان آمریکا طرحی که خواستار توقف جنگ علیه ایران بدون مجوز کنگرهٔ این کشور است را با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف تصویب کرد.
🔹
در این رأی‌گیری ۴ نفر از اعضای حزب جمهوری‌خواه با دموکرات‌ها…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/462386" target="_blank">📅 08:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
سپاه: ساعت ۰۲.۲۹ بامداد امروز پنجاه‌ودومین پهپاد MQ-9 ارتش تروریستی امریکا با آتش سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در آسمان جزیرهٔ قشم رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462385" target="_blank">📅 08:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe6080617.mp4?token=lhRpIR2giVZdZGIZG4Hqg2cuQkKh5pswa7oGlR2ds0dNRwZtniyk98TN2gIhlzAl_Xt_TE4Hs_VN3No8T56p9MCvZewOq0OYA-SfSevfBZPn4AKp46XSp3jqyYwyitIcDyE47ULTzce02zQnLsBoh0twt_7pyFHF5B6Jp1829nB09kKRycZP_J9jZsNOQ937LkMnn-uDkZ8SiglDhqfIWYvBLd1JdtaZrgS4smtpBov-wlLEIwKbAPrn1S0BDjvEErNlWtq1ikbFNXTS3lZncPL7gTebsBvTcCjNjTlb4tN9RWqunYbRUtNPw1d9iGygI8QAOsSiFJKEoDGsqfyUPruYtvUK4yJ57iWNeBqJ61QsqbJg-uPLKos3WTSEsB_Zrw-04x9mJHlT_8BOQZ_0eiolC21cxxHJjn2riX-d6N3TY3v3Tlb7lr7UcjhPAoU7OLoFxuQT3q8XLwRBTq8ZEuq07RruU0_kXBKnQVv8xYIb6VMH1yu1A9e5xBi4RNbDl7lr4YFpgqWDpFN-iVF3-wscW6b9XzmAi-wnu3gijhwd93rop8GBltw7Qui-9DsrQLc5AWnzr8h6Vx5nILRVh_a-_-cUxQ_QNrY92oemuta6_QbCSycByKtrLoMbehAGP_l884sBG5t8MxYRoMs1vL2BZA08QYwr7nqEtQZK95Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe6080617.mp4?token=lhRpIR2giVZdZGIZG4Hqg2cuQkKh5pswa7oGlR2ds0dNRwZtniyk98TN2gIhlzAl_Xt_TE4Hs_VN3No8T56p9MCvZewOq0OYA-SfSevfBZPn4AKp46XSp3jqyYwyitIcDyE47ULTzce02zQnLsBoh0twt_7pyFHF5B6Jp1829nB09kKRycZP_J9jZsNOQ937LkMnn-uDkZ8SiglDhqfIWYvBLd1JdtaZrgS4smtpBov-wlLEIwKbAPrn1S0BDjvEErNlWtq1ikbFNXTS3lZncPL7gTebsBvTcCjNjTlb4tN9RWqunYbRUtNPw1d9iGygI8QAOsSiFJKEoDGsqfyUPruYtvUK4yJ57iWNeBqJ61QsqbJg-uPLKos3WTSEsB_Zrw-04x9mJHlT_8BOQZ_0eiolC21cxxHJjn2riX-d6N3TY3v3Tlb7lr7UcjhPAoU7OLoFxuQT3q8XLwRBTq8ZEuq07RruU0_kXBKnQVv8xYIb6VMH1yu1A9e5xBi4RNbDl7lr4YFpgqWDpFN-iVF3-wscW6b9XzmAi-wnu3gijhwd93rop8GBltw7Qui-9DsrQLc5AWnzr8h6Vx5nILRVh_a-_-cUxQ_QNrY92oemuta6_QbCSycByKtrLoMbehAGP_l884sBG5t8MxYRoMs1vL2BZA08QYwr7nqEtQZK95Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیدهای فوتبال ایران زیر باران شدید ناگویا برای بازی با امارات به ورزشگاه رسیدند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462384" target="_blank">📅 08:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPPEGUVFoAOv82FrjVJefDQ9SlNC_W6U3_wK3HgVqa3cFwEY-qIB3U3pkiOWu0y-YeokqXPZk6gPp9c6eGvF2TeBkOilbKdGgSFieMwplWxqMNwrZ6T3FjQw4eICpJMPfs4Yfw0d6Ef_UH2nPg2MpV6quOhuQlNOSjhAawuS6hoHRziM00CtD7wEu2YDK8S2pyMHZAQtQ17go3PrallZBcYmvKVCJ7RDFnQooXsm8A5XavH3LF9cAu-HdSQ4yeA7s6_-kE0gHMfpnaeAbdkxjXLbgNURLnKZ2ZR9S8GTAm1gs2Z-BWr1J_hsQRteucoSga_8JEQ0OV1p4KCCu67oKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌‌های تأییدنشده از سرنگونی اف-۱۵ در یمن
🔹
شبکۀ آی۲۴ رژیم صهیونیستی اعلام کرد که گزارش‌ها حاکی از سرنگونی یک فروند جنگندۀ اف-۱۵ عربستان توسط نیروهای یمن است.
🔸
تا این لحظه، مقامات ارتش یمن و جنبش انصارالله اظهارنظری در این‌باره نکرده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462383" target="_blank">📅 07:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش‌‌های تأییدنشده از سرنگونی اف-۱۵ در یمن
🔹
شبکۀ آی۲۴ رژیم صهیونیستی اعلام کرد که گزارش‌ها حاکی از سرنگونی یک فروند جنگندۀ اف-۱۵ عربستان توسط نیروهای یمن است.
🔸
تا این لحظه، مقامات ارتش یمن و جنبش انصارالله اظهارنظری در این‌باره نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462382" target="_blank">📅 07:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMkBCwxxEXLLdWXGcWLwMjpU66K4ueXODUDPWQsAWGTgeo2X7eZHnmDQSs7d6OMh-971XAlAce9esPMBJ316CLUE2iGS4hge0m6yfUfWww_bN8i41Fgjj_kUKmyxAIAZZsP9nTGONL2iFS_i5JJdjdOV45MxGxAvBv32PW4BT_TTDTdZ4eshUtbz4VhosKalUylr-3fDm3J2ztjh2fgUW5iFPyXw-OE3S98z5r8wTelCM880euoPwkY7eQI5RZwxMj4ql1MSD8j37VYYLTiVLQ9BC4NVLDL9h7uuhHIJCfJKuDIdu6YkVkBV5ZVv6YBdGy_GKDKx51B3oFD9MOv2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mv2nI6Rpb4PHX88ipc9B2mN3ZQ4z2IE_u8mpwe9vrrllHgAyRMP-BhgIX3y0PUhm1zgQWRclf3Fpo0dgjYxebPqhOdGudahKwWbdGdPnfnQ0bu7Z2WJnAfihTm8IKFa_Wunnh0FoTjsb-E5ITNi4SQIIqU8bd4DCX_dyFBK2kaPOoKebcZQKu-U-ZmBvXpf4dddLaOg5WIHPeaMv16tclY2x4VNW-krlYnFXCkIWUqHzt1mopVNlAlxuSSUj-dLyHQwX_Khx79AiHOylT42c6Zzc2fhfWnzIU21FwIiRwlcpsqK-QEkIaPZTzZNMjUqPhnmyAW3nGAmzXAQUxcfPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhqdkKhHBYv5iRa7b3yCAqV_K45wMsM4aOyAerBgzfbrwuoU4nPXFdcS4IxntGTn5vNoMrwJMlQRULMjnlg9ndkDRxRa1MEnsViAq7ewYDVa7pz9G-CfMjdGQR1LPrSo3PSuYgHp-sQP-LiLvgXoRH8UW9o1ab8pRWL6InV87wIzlC7sliHgmDqohG8fosgC5RO02KdlK95pZDMu3VZbinvLJ3jCXCMrIp5mBiPChVki1cQYKNPx3F-CfC7_UvWdPCltsBnI4zYpcH6RoGLhZbrBPFNiqLZ7BFC0fLjm0gPkg87rk-ymGHT-j0b87Gc048OeJ6LUeDDlAbfNkDOVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3W-8ccVF97WAvuA0YHmrSRkSGoB2mj70EeWSx97SixVLhNjpk8-5WvgYxE2ndZ593bben2ELyZkl5Bcfqy_OPZMASr2JXrBLRbSriPxZEZxmwrV9Cg0H5S6Y5Jb9znFovORfhj7hYDibab4sfWjxU6_di05Z-ujMVNByoIR9x0Fe7Iau046oPquGgOle8XHh1PQ69ine9bf1WoOUGnvo7o_XYYQks-rPvGhWf8LwudzSR06v3GihqncZE2L9ObSjLhhxjHZmbjmF0ur0rX744oSs_qgRURI1lOQuZ7nJfzBwAD6y__JI9elZbGx1rrk6SjF_GmCoez61XsoidpN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_j2ScEnieYPFW_Hk3-7lJtFxx-l-LX6-LTsDZ240LR2L0ZtaWJmr2gyJ-JaCp_FvZD0nVQ_WMSgbjkE4uMp1mson2IvbiSdmQSWB-_do6DvNnaZh3R5DTP4F_L8FBsTNVPqOamPyDOxNZQMCZfuQHTBj1G5OuCDwI6KOTGk3zHYVXdiukJCOFtc0za3TCDNhdUXKZygs8PVHGKVUfK2X8N4_4q4IiVQOySI47-enBptQcQSIVIK-BVRw93ISMLqm9MK895mbknG7xAaj73SW7Mbv5lFLNgjsP0IlNJ31-t9SjsVB6u4VNWCXVCiBHgu0fJSVi771P10hH_YnBNKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5zmIsB5bdUbRt48KfhaLHQ_VD20o09vA6UPwbkhyGMi1eVDslJveVL83NJt42AElqPtChPUuwyv_cb72HWVQcBv0AcKao6FH_miA7rvy9FwzSqxvQ0xfYOjasE_jicAjknzh2hi21LfNalNN6jFI1Q6hDSoYXQUXjLpQnGYGs7CTvUqVkUKaH4rhkEl7Nff03Hw50fb6oQDHAK3TvUMyOxlEnQizd78AZdWFQbUWWJv45EiJJ0N8Hz4N_nGwDn2Fa0bvvGZZgHP_26n8MqPEsC-XRdHSK5cj7oxHI7Er-5JVBUxzQEJM6jnF-mQFvU3klx9TNyJSaL2_jssiX35Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRZt0DGsCDe_jqUM1K5xQZ3y9nMsOJewlDvNm91ti0KwSObWQMh_mwg3eHx_VDaPsjrKtjNIeEZQ7U5dPbH96w9m4GTOAG_sod-sSNht2ik9zB8qjkUTk7n511YN60kln6Loh0u86R4JLdn0i4fnVOdDNJ0mSf1rwNBnTZdJeOoUiaV2fJCN3WJ1ZTehai7XdsTBYiZhXkxJo4hYm-QXzxbWoIOs91MojTsbbxuOft_EanIE-wgHsTbELtq0IQ-kwLhohVdxMt5gnX672kAtLi72AFvqfaOWiUseKZ7hgZ21iMHiQAngEEaR1N7_oB8SI48-XInBug7jIBu-6o2hvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پایان دیوارهای بلند زندان رجایی‌شهر
🔹
عملیات تخریب سراسری دیوارهای زندان سابق رجایی‌شهر آغاز شده است؛ مجموعه‌ای که پس از تعطیلی زندان، قرار است بخشی از اراضی آن برای طرح‌های شهری، فضای سبز و کاربری‌های فرهنگی و آموزشی مورد استفاده قرار گیرد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462375" target="_blank">📅 07:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۳، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/462374" target="_blank">📅 07:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0oFo-IOCKBNloMWFIgl0GKp7qqKpXiS3Fb3IiSEQvRlZRy2bHAAy2RQoh67oBOT1LYCSRI80wqQN9cmqPr_MuKJ3QOktPlRkTQ37zM_RoT55s4mNgrBPGJTfV8pYFPBJyIZphOivH9LUXxku9VMuteL_HOzlWSM36VNdg126yzfPJ2UY9CVijYCzuCnc-gdGbRl4TKfQkKeQm8fXTsSDzWx5riabXt1Odh2wW9War7OhDA_JQFFDjERdnuTpx-dkeTsIpj6zENZZnYxBLZxePvpgYG-oI1FVGMnxhrmDheLaATBqv9S43DMEGY2Y5CSsrmaRoLxjhkzKcoq2GUARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: ۲۰۰ روز حضور در خیابان و مجاهدت در تنگۀ هرمز، ضامن امنیت و سربلندی ایران عزیز است.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/462373" target="_blank">📅 07:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462371">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9277a1ee9.mp4?token=FQQO_uPGDCnc5MTSYo1_qEnMYCj5QPK12aQ9v7rYl3TsV5NgVGoRN-ioWXODpfS5WTaY0NTsRjywyWYrSwPJVZhNMrEFEkgeV7bSCScGgC-SU93kYfzznFlXPiTTjmDNDMnRfAYtIKISfmVwMj1dTQ1VA7vj4f0uDMqthFmiuocQRkOH3b8gaTU1vHTOIFNqqs4Bz_ZiJHuBJaH2hfQTj5En8Ub2XXdA20y6MoMdnLPQLoe04KRUFv9CsD5FnJQWUqetayfjHYvb3KmuXIfRtEKjADjZtgtDiJV1ymgxmQGMlNz5CUYcBnMhQgEynnNLwiwqu_o9hqElDEhJYDoksg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9277a1ee9.mp4?token=FQQO_uPGDCnc5MTSYo1_qEnMYCj5QPK12aQ9v7rYl3TsV5NgVGoRN-ioWXODpfS5WTaY0NTsRjywyWYrSwPJVZhNMrEFEkgeV7bSCScGgC-SU93kYfzznFlXPiTTjmDNDMnRfAYtIKISfmVwMj1dTQ1VA7vj4f0uDMqthFmiuocQRkOH3b8gaTU1vHTOIFNqqs4Bz_ZiJHuBJaH2hfQTj5En8Ub2XXdA20y6MoMdnLPQLoe04KRUFv9CsD5FnJQWUqetayfjHYvb3KmuXIfRtEKjADjZtgtDiJV1ymgxmQGMlNz5CUYcBnMhQgEynnNLwiwqu_o9hqElDEhJYDoksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد خبری آمریکا هنگام پوشش تصادف
🔹
در پی سقوط یک بالگرد خبری شبکه «ان‌بی‌سی لس‌آنجلس» هنگام پوشش صحنه یک تصادف مرگبار میان یک خودروی شاسی‌بلند و اتوبوس، ۳ نفر جان خود را از دست دادند و یک نفر دیگر زخمی شد.
🔹
علت سقوط این بالگرد هنوز مشخص نشده است. قرار است هیئت ملی ایمنی حمل‌ونقل آمریکا (NTSB) و اداره هوانوردی فدرال آمریکا (FAA) تحقیقات درباره علت این حادثه را بر عهده بگیرند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/462371" target="_blank">📅 07:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462370">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZdAenUKUNjIzUDgXouN_blIMzKHvnggq6qqwenN0E2dsAg9ogb41ZRS9sPv87RC9Vd8CxVTOU2F_iLcZ8X8QdcORsbwNctM-VGD6yXAxNZZvGDEH3fRv5PeN5MHq6DBNy2jVwSk0h_aaQrqYWG1mdDvZmPIzVAyAckBPYLuyEVlZE_DM4ddRDai_u9_ktBuV6CYb_HgOhvf7T6Fx2qjE-PhpZXidm9yYiJ-r81GcNDOQ6mh6bzdSnVg02BBrcl3NEyd6EkX96KSomIYQOnPIDqSNhUGPchE7DBgITLrBYtW_755clh0N0qhV6yawDZWrvOs-r2HMe-iekjxXOjhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرعت بالای مصرف ذخایر پدافندی آمریکا به دلیل حملات ایران
🔹
وال‌استریت ژورنال به نقل از مقامات آمریکایی و منطقه‌ای نوشت: نیروهای آمریکایی حدود ۷۰ موشک رهگیر پاتریوت و بیش از ۱۲ موشک رهگیر تاد را برای مقابله با حملۀ موشکی ایران به پایگاه‌های اردن در هفتۀ گذشته که شامل حدود ۲۰ موشک بالستیک بود، شلیک کردند.
🔹
استفادۀ گسترده از رهگیرهای دفاع هوایی برای مقابله با یک حملۀ واحد، تقریباً معادل مقداری است که می‌توانست در یک هفتۀ کامل قبل از جنگ استفاده شود.
🔸
پیش از این، شبکۀ سی‌ان‌ان به نقل از مقام‌های آمریکایی گزارش داده بود که حملات ایران به پایگاه‌های آمریکا در منطقه، باعث خالی‌شدن ۸۰ درصد ذخایر رهگیر سامانه‌های پدافندی «تاد» شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/462370" target="_blank">📅 07:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462369">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRS-StmFjv7hEhMUMrNFS11NLfbRTWnj7vtRhV_v8xGg74NC2vOyze77fQMY7q-4X7m3Qefm337zeX-Lk03M7G_WBZ-zACBePCGhjSFK9vl00vuylgOKobUjP7ThcoEw7tDFP-kCfCbUa6X78qdIojnvuW0c1oUT2aEjy82YG1YLxhob-RQ3yJBNxNqgC1WQgv1If5nOOgGP1Nux5YSfAQVCogm2F3NA21MyTEv7PHG8DDU7Ks4m-fMukqJMJ4-LIGICu87MGY7xF9IthYmARC4MUzHnabFvDuhXJ6r6e5qn37wUz5EALfbTzd8L97_la7aSKGn_zkzX7ODW0gFhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد، و تا پایان مهر قابل استفاده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/462369" target="_blank">📅 06:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXR68lkpaAGXhWkvO6UsclHklsYm-o7W16EZLJr_Qdi6mtuXbp8pamDwKlyjJ4DYfYQGpUVBjvxx44rY5pECr0D2zFsYmE0wyJ0cwdIE6K2Bm3JRDTWRQUaGnAUB5gqbGtsd9XY7pu6Z1r_E88ThDnih_lSuiPbDnK-J9Ra9_KnXPksECebhN2v56p5p4xlnD8Scb9_24pbuITThp5_FUqZbDqDl-OYy2oNYlJCtguMCll5DsJB5yOGQLzNi0ReVqrkkxRSv83PzoY8aZcmcVJlyMli8GRsO2kRAU1PvCg77Y2ZggKPQ_vPXhIKxxMcqP6DSQBNwg27fOC28VAtCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ: بحران انرژی جهانی تا زمانی که ایرانی‌ها به شلیک به کشتی‌ها ادامه دهند، وجود خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462368" target="_blank">📅 06:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6uER2Jq9sQ6zm9NWDsyIZqrn5UI31g9gZ3SMbFauXEoahFkSg2NimNawWDRkx3HWIce4rbk-fYl94ozv3TgyCCF-M5XBoPfAUVHSsl2OWC6eizd3nwCHgsFJqBx2CXossO4qytQNb2kLVs1kHEILFdFz9HB4HuOA-DLj8R52W2yWbqDkFns-0Ya-PB_8pWjMD_2jHyFhWWDNcttbqdqWT35eqJAEbUIEYWBWm-DkCUJaVEfGHlgyCiyujFgcCdQxgLnEiUGOcNwxCGCOZ5jibjVDs5IVpgNHPClsdD-3Reb9H5M5ehkFyj8WmKz9gW8uyKLRT3usZIzLoNl8BPYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ: بحران انرژی جهانی تا زمانی که ایرانی‌ها به شلیک به کشتی‌ها ادامه دهند، وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462367" target="_blank">📅 05:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هوش مصنوعی برای اولین‌بار دست به نفوذ زد
🔹
برای نخستین‌بار، یک نهاد ناظر اروپایی از نفوذ واقعی یک عامل هوش مصنوعی به یک سامانه و دسترسی آن به داده‌های شخصی خبر داده است.
🔹
آژانس حفاظت از داده‌های اسپانیا اعلام کرد عامل هوش مصنوعی با استفاده از یک مدل زبانی بزرگ، پس از ورود به سامانۀ هدف به‌صورت خودکار به جست‌وجوی ضعف‌های نرم‌افزاری پرداخته و پس از شناسایی یک آسیب‌پذیری، توانسته اطلاعات شخصی را تغییر دهد و سوابق مربوط به صورت‌حساب‌ها را مشاهده کند.
🔹
این پرونده همچنان در دست بررسی است و جزئیات بیشتری دربارۀ سازمان قربانی یا مدل مورد استفاده اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462366" target="_blank">📅 05:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4149d238d.mp4?token=VnIP7fXTQySqT17HKpV2-6WZ8BsULEudy42BEIEdDUJl06FQhGAAV64C0pWyH4Nm6rP7V2Iq0sM8x_ekp6-CRKaPrvSzijKVHf0JOC-ydb5cqu9WZ_XmbTy5kkPJSadhzFlKsyDD9SsCjzleXZ3OVSxMR3nv57wbye3kam4jAMYtUe61bYpovrQe7ghfEqb-OAqZpFFt_fR-IRWCCnhGDVa0x4uVOoF22WQZ08IjCwU0gpb7ir4qFHOxRYH9SG6H8FfolmsO9Q9Zb493jP4QsTY8Tnz9JGECVui-qbS2NujF1r5Yc6VnkAT4PhEE1GPO-JtIFAQ_kB3i6NurIL02sDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4149d238d.mp4?token=VnIP7fXTQySqT17HKpV2-6WZ8BsULEudy42BEIEdDUJl06FQhGAAV64C0pWyH4Nm6rP7V2Iq0sM8x_ekp6-CRKaPrvSzijKVHf0JOC-ydb5cqu9WZ_XmbTy5kkPJSadhzFlKsyDD9SsCjzleXZ3OVSxMR3nv57wbye3kam4jAMYtUe61bYpovrQe7ghfEqb-OAqZpFFt_fR-IRWCCnhGDVa0x4uVOoF22WQZ08IjCwU0gpb7ir4qFHOxRYH9SG6H8FfolmsO9Q9Zb493jP4QsTY8Tnz9JGECVui-qbS2NujF1r5Yc6VnkAT4PhEE1GPO-JtIFAQ_kB3i6NurIL02sDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر قدر هم را ندانیم ذلیل می‌شویم
🎙
رهبر شهید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462365" target="_blank">📅 04:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok-L1vtsy_aqAs1mk2thxjC2pivrhGKsFqG5H93pDwH7mqekS6PUFY2rqF2aRoCWwU8Bg9d-zEOyiE-d784WjKRx_96uPdulziG-aBFhT84BcSykmnClYCTHyw4AWS0ykRH_-ykDCLLUd4Bx99sdPNqGFiKl4EM1kfEz6KckMM4NmO2Hm5RM5JthGCc7KXzqxIqqz7mbHaKqEsACkwd0zJ9J7aTOL6luqQArrt4QLWEWadScBUXGYsbE9fNGEZA_NJJ_Jo629JvQYD4XT3mDQSEBZ-lpznFEtXXnKIsKOgvcjQShb9iFs_3MK8DXbXwC9CxRZmXVTOI-6bVB1haFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۶۰ درصدی ثروت ترامپ بعد از بازگشت به کاخ سفید
🔹
نشریۀ فوربس: ثروت ترامپ از ابتدای دورۀ دوم ریاست‌جمهوری در آمریکا، به میزان ۲.۷ میلیارد دلار افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462364" target="_blank">📅 04:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462363">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آمریکا به‌دنبال اعمال تحریم‌های جدید بر روسیه و ایران
🔹
مجلس نمایندگان آمریکا قطعنامه‌ای را تصویب کرد که راه را برای رای‌گیری بعدی دربارۀ لایحۀ تحریم‌های جدید علیه روسیه و ایران هموار می‌کند.
🔹
در ماه آگوست بود که مجلس سنای آمریکا با اکثریت قاطع، لایحه‌ای را درمورد تحریم‌های جدید علیه روسیه و ایران تصویب کرد که توسط «لیندسی گراهام» تهیه شده بود.
🔹
طبق این گزارش، این طرح خواستار اعمال تعرفۀ ۱۰۰ درصدی بر پنج خریدار بزرگ محصولات انرژی روسیه و ایران، و تعرفۀ ۵۰۰ درصدی بر تمام واردات روسیه به آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462363" target="_blank">📅 03:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0bDlpwiQKuTN-sihB_i1tsR-RYPU9OGXa-mBpCnXyKTeWB6qrv0e5isYzCHIXG1p2G_pTmT_Lg9bao5dEvXOtcMO7esBlI3N7cYuD__m-nb5KBgQrn0XeIsf-7HN1gicU-yEik_FA2-qzcgjtvMbNr6j1qBQMAL0rTzRx69makk8wuPxULIDikdpLeMuFZQwtYqmc7eY6NmKp_fyQvyYVaQRI7V1bsQyj_efTCInEIUrreocJPIcyIHn5qqljzaGEIww85q9jAGxvtnypVcJ5dHha0HIK1R8uJBN4vQBAkpCpWNeh-fpxrtb9TpN3cxjx0Hs_oLiqa1azlNxILsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbrAnDtxEGuqhezARsgPLKUbN34nezBmPrBg9UwRXiUF8JcJ8b77cwtsdZISvgQIArdSqzHyJpvgH845Gv6hgdkZMsk0jguICIDsJ9HQsG-NEc87Eo046qe8U2-qWKqXtipQ6Zo2o0A12-2MOGanYqedNESkT8SUTHbOw3fv7DjJ24RCCnJMBhdBQ5dtY3quIXDUXFYiZwHJlDNAWqbDTPrnONWqnDpQ6rLH0EM7RuTMPU1vWggUxKwXJoov0cdRd0zv1nVeezYqxdtCTDb7RSdORakp03DbE_G3mrjWXaD6Rlx7Us_FbLAzE5QHs_EWu8PJ42VnR0D_d8k8GcyInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XugT6hWIRF2BS7KMn5TkYC_WbGyCgkoOlpcDcWPO13IX06cUnJdTToYukB0HHn2pTVJm1jfBPdsjTHw3ShRFHdnOM54K2gyQXKmtRISDXpsoyVUogmq1LpoOfQB9IOBW8eP198gk9hUbISsEPeNCGmptUrdyQRj0X5F8dpT3eXTDUEtVgjZc1Y5dxGLLvYrYraUwIE_EJQrWrU9zKOB16gnoMt2jATFAZoCD43rgriL4jwa4IMxy2p9imPrd7UD4PhexPzs6BgLhZ4O5d-xt52QA0jdUdylczMv3QEHbfJHTQNDTfYMboED68EvTOW9kYz6ytEiOm7g25CwEBkBzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfAtA8zdCHkHx85GC2Kol03E05yA2cHHDvThkhBz9TZthpXak24aj-hTvcD4MENh8AG6eAon-AXAGaM5N-MgMF45Yw-ImLs39uMg97LQVHHQ7k1yCGxOMpDt9u-VAOaFQjG0n_vwbO0qbJ7klH_xubw5uIRjxmtSGg4pUtGgFzU7L9ESyCyVOJ3wS-6kUIdRRK-kanJRMhSlksGHUfTgh8iZnZDI_VQWRuiWv60aDMFKcc-LkHs3bgOe2aEeArZfk_ECeL4MknMHwNbIqSwBTfSYS0Qkvtn56OdVE96JLZhTAvE9TXbLGp8v5A6pjBuYjl7Zx5kUWEE6mNpv4JCweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRNkR5kz6VGENYQOHx4U7lQUCx4KlWmBEY0R7yTcaR3_7K6Re62KixraQlqmjzn1WEB08dZTv_35NfBQV0d3HVrDrHwBunITHnAmteHkmPY7xvD-fN_Vomw4hZ-CRHMzFO26QlX8ayYRNuNkwpf5z9mUG7LaYEOzvuo1ICFbllQK6gs7qy1J6NYFgm8_KwARvuBA2Wx-u_wsVObEZCXI_9Zo-CpLTiBVJc6hB8AjeG__Xf6q0lXyBgOvouHfh0i2pQVvR5jMipH8kLelwDHRCbhu8pWPHpjqix_XOpOZy50pEKmjdyr-jjBRPjNjEeM4m-5bbarkqE3MkNmuKrZCRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شب دویستم؛ روایت مردمی که حتی در روزهای سخت، میدانِ خیابان را خالی نکردند
🔹
۲۰۰ شب، روایت تداوم یک حضور است. از روزهای نخست جنگ تا امروز؛ خیابان‌های بسیاری از شهرهای ایران در ساعات شب شاهد مردمی بوده‌اند که با وجود فشارهای ناشی از جنگ و دشواری‌های زندگی، صحنه را ترک نکرده‌اند.
🔹
جواد بخشی‌الموتی استاد دانشگاه در گفت‌وگو با فارس می‌گوید: ما شاهد یک پدیدۀ تاریخی نه تنها در تاریخ ایران بلکه در تاریخ جهان هستیم. هیچگاه در تمامی بخش‌های یک واحد سیاسی، حضور هماهنگ، مستمر و هدفمند با این مختصات را شاهد نبوده‌ایم.
🔹
این حضور مانند یک معجزه، ایران را از نقشۀ وحشتناکی که برای آن طراحی شده بود، نجات داد. نخستین مولفۀ قدرت ایران در این بازه زمانی حساس، مردم بودند که تا پای جان به میدان آمدند.
🔹
اعلام آمادگی و ثبت‌نام ده‌ها میلیونی برای مبارزه و ایستادگی پای ایران و ۲۰۰ شبانه‌روز حضور در میدان تمامی معادلات را تغییر داد و شرایط فقدان رهبری در یک بازۀ کوتاه که مورد طمع متجاوز بود را به حاشیه برد.
🔹
سید محمد مهدوی استاد دانشگاه نیز می‌گوید: این ۲۰۰ شب صرفاً به‌عنوان شمارش شب‌هایی که مردم به خیابان آمده‌اند نیست، بلکه روایتی است از استمرار. روایتی که نشان می‌دهد جامعه تصمیم گرفته حضور خود را حفظ کند و پیام خود به دشمن را از طریق ماندن در صحنه منتقل کند.
🔸
حالا ۲۰۰ شب از اولین شب تجمعات مردم گذشته است؛ قصه این شب‌ها بیش از هر چیز دربارۀ مردمی است که می‌گویند در روزهای سخت، قرار نیست خیابان را خالی کنند، این شب‌ها در خیابان های شهر با هر کدام از این مردم که صحبت می‌کردیم می‌گفتند تا زمانی که لازم باشد و رهبرمان دستور دهند، پای کار خیابان خواهیم بود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462357" target="_blank">📅 03:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7VRO2ILpFhhfFeLN-Wk82pW4mWXiEAYNXOA5D6IqB7swx7oOQYCEiYTwLKUqInMsXBD0Hdhv-LhA82v97-_lAY2-kw24XoH2hB0Robzn1B-ul6ISq3AnJZXMhbquxwuAwAiEwgMmL9fAzxv2CQyvJkuD_6HWsyTc8PbrHKN0NWvBL192g7Un3Jyti9SKaWvAyK3ZoAu8ZTYxyZOt3QkGUYpDCI-xQVgZq8RIdp_uL5uXt6GLqC-Pgmxm-VdWrDSCx617hcf2d3s8SqO1YE7U7qQXWQiq-llU5A7ilW38ne3rrCpp8ImhxmzGdHYpExWAgR4pmDNrptOVEq-auUS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: باید با زبان هنر، مظلومیت مردم ایران و جبهۀ مقاومت را به رخ جهان کشید
🔹
رئیس سازمان بسیج: جامعۀ ایران اسلامی تجربه‌ای عینی از مقاومت و ایستادگی را پشت سر گذاشته است و این تجربه باید به آثار هنری تبدیل شود تا بتواند با مخاطبان منطقه و جهان ارتباط برقرار کند.
🔹
هنرمندان برای رسیدن به سطح حرفه‌ای، به آموزش، فرصت تولید و پشتیبانی اقتصادی نیاز دارند. در همین چارچوب، اقتصاد هنر باید به‌عنوان بخشی جدایی‌ناپذیر از سیاست‌گذاری فرهنگی مورد توجه قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462356" target="_blank">📅 02:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebzNuHohtCB6WhorVFnhEz9xGgFzKOcNAKLH9LHqdrXJO8DutkQk5ZPRMkcYNLO7PgjvSfRak70LP-HmH6VFZgpgn3Nw_NkpdfIjnghtASzFfJrnCCUWBonezNnCxP6ULlXyN1DD0EvZp15iRPdsdENOsFIZRNu3choLWy8VXBUjQY0Zrea5J6AQyOzJ_RbIgmNJF9O9aW62xyNZEJhHbvouX09LKaUKefuAFVBSgmlbpKLDNVXoAit6vP-aWlRkuyly0I3okafoIbrbnSMkhkZUtclLehyHh__VqPyGkTKcK8tjavOvOQJHA-lPlshVVgdYXs9umpJ9i_sPGintkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9psNJICoD7S74sPWhsVfI2rIkITgl_Chj6moL8b3Pejt8U1XbPc4Ob9BEuLR0bN5xUFI7NYSQ9E6_7RshlECbbRZYAbQealqN3XyKMm7zKtUrpqVevehev6XZQLCbixEkCNTLMMJE-zQmATXch0Qk9feyeoY53ROkHqP7a84a50_wT7ig6TsQ2DjwiUuo5GsEFgc6d-mDi60HGHtwUOqFuHQxU7Vh-wKsG4xMm_oJ5jrjJdvQG_TTGO02sDc9-JCYGEbBwKLP696EQHOqQAToLNP-hxZz7t5QDCMPgDykl7ikOdey6WohrZBge9ju8qYIu9NYWQXM4UHmKYXiOKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRgiTOx5MWp80r4jULhqFNf1yrRXgN6M3xtKovgocte02DvyKMukUG9mceD5D0ZKSn9wy_vM84kNY9YGFoXW23t5MbcyQomSDa5BQ5cyAtczqlGga6S3biqRK7zWzFXwN0_nTbLKdwKrhjRUZuHWvDOiXCCBcdgN4WO5Z8tFm4WZ6VPxDQYUxlLU32pmSJG3Nq3Eh6mIhfW_4Es4yJzu03P8lXjBlyF6PqJL8uzPJy4LX9tbPTxOE8HtRUuoq6VFpOfHDF720_mig-0MZ6DmzPovTYzQLBWnHGyOs6IcfWOpGUVBg7n2pgbd7uXLUSrh1QdPFthEwTGY9xSMfAKYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l39KqBGmr75iJtIwTTzTcl2EXpnqLI5k0H5fvw_pZcRsgMrExQV1b4BLdcPSG8fslCHnNhm9qefM_v8UB1vhkz9UD9UvNkdXfUeNqttcadLmaYF40LstJ0v5Q9eTAiXLbJq8aRtRMJOSseP3MsjObT6Ky9BtJVIysMYRN6EhyBtJET5UVwQ4T4Tj6XXy9eKhHjYrNrLBk0wY9TfHGjKAdK4HPVFuldYbKsOVmVWWbwoGjcd15z4wLUVpBfUCAuVgIwSXQmFtXWkliKmlZ3Lmm4qOpdJEFsgE87rGqQtpA8YVWVAdjf_425Lz7-pINSGjdDqQd4FYTBNrdDQWjtV79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slXKXVCycxdad3MborYQZZPLV4_p3QcBppnUekzl4cemNUmIql7076-RE6ve3x_CN4QNovctyksglmd3i_0Gc3rvruOZkRqhE5YDqCfk3nlJcG0CM3mcrx4LVz6LFmOi-_Sx8nZPlAHCKzlXIx1I-lfcj_0Yn9H4htbmeBynaJgrLnQ0IcSLAdR8W0e651gC20PuTZ-ripD6AvFoKzvpY0zYvrgzyYne3jlrgsJjCKV4Iw31ADHe5sPBnLMXgh-5QQ9DZV0B_UdXnNQs-iUoHt1O5Dl-iUsHQLT2yYg19TCKiz-y5PIafmh-MYxXC27tu92mYZpq4wQyTQggmYZstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbvHrhVwH3hlxO3tKsNhMPbvJQ565Y1Hr9wkKsSI0KDyBaBLbYItZo87MGcuXVwnTghnT7dQ7z8al0m-WfEzTDyAHXMEVkNVP0GitaLOZl1V0yWDCPrR3AvbCqnKc7r9YuvckrCS39cPQSmaChV5U06yBkNQrN6RI4hioVabGZQhHlg9nmzjY_7YJC1A61M4vCiyPi1Ntvfu2lIK0F1m643LQvDd8tH7kis50uNvyyyVReTAomL4niaGMntdDwmkijENGPz4IhOZmUsngM7IGkBONGKznANC80jr1YUcMHK0gkgSkbThSv2-g-QB8qw649I_x7RnBxsG8znWdnpwoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر اختصاصی رسانۀ آمریکایی از آسیب ایران به پایگاه‌های آمریکا
🔹
شبکۀ سی‌بی‌اس تصاویری اختصاصی از میزان خسارات گستردۀ وارد شده به پایگاه‌های آمریکا در غرب آسیا در حملات ایران منتشر کرد.
🔹
این تصاویر که توسط اعضای فعال و ناشناس ارتش آمریکا برای سی‌بی‌اس ارسال شده‌اند، ساختمان‌ها، وسایل نقلیه و تجهیزات تخریب‌شده در پایگاه‌های این کشور در عربستان سعودی و کویت را نشان می‌دهند.
🔗
شرح کامل گزارش را
اینجا
بخوانید و ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462350" target="_blank">📅 02:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجار در مقر گروهک‌های تجزیه‌طلب در منطقۀ کردستان عراق
🔹
منابع عراقی: مقر گروهک‌های تروریستی تجزیه‌طلب ضدایرانی در منطقۀ سوران استان اربیل عراق هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462349" target="_blank">📅 01:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwKxgc3iimL4YxpUhSMdQINgD1k6tEhoyUoLYV2IFLFKlg7CZ_Vj1sRiXYBLKn1RXCVecVh49LbxBZ42o3pHmyak4BLF6vGVJitI8-DW23m0gfuuq1uaxCk3dpTEj9mNsxUcVeDDCvOPYhydxRlDOcVgDNfwHViMrrGTIcTESh2wlBnhmEQe57fB8uE4spy3PQUVF09yti72vVZzM82T5GwG-cfnKnYv-lwhrzbGlAyykfXTcX0p8SlchI2_N_YM7kYAYnZJIrF4qnFydHfS4i0DIG4Y7tmR5lRQuHatt3S4DRGy_u4NzIgGkmsf2A1sUremR15m_49gG6EprnqnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جابه‌جایی موقت المان «مشت گره‌کرده» میدان انقلاب برای مقاوم‌سازی
🔹
سازۀ «مشت گره‌کرده» که در آستانۀ مراسم تشییع رهبر شهید انقلاب به‌صورت موقت در میدان انقلاب اسلامی تهران نصب شده بود، برای انجام اصلاحات و بهسازی جمع‌آوری شد.
🔹
این سازه پس از تعمیرات، بار دیگر در میدان انقلاب نصب می‌شود.
🔸
به گفتۀ مدیران شهری، این تصمیم با هدف حفظ این سازه به‌عنوان یکی از نمادهای شهری شکل‌گرفته در جریان مراسم تشییع، و پاسخ به مطالبۀ شهروندان برای تداوم حضور آن در میدان انقلاب گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462348" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462347" target="_blank">📅 01:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b596013a4.mp4?token=ZFD1tgdf66_3C4wOiKjWYjlRGyrmjEbOl_0TIOUC14IdIamLkANQQWLDigC4eIuxmhEB1_E2jEHfXYtTkGJ1oDr1tISLeV2I_yS4lwyUnR87Yv-_0t8zG-bnV2HOyuXSjkiE5hwBWt3gzoyh8mHnjhu9mbAlRLHOoYylAbIgOpfHSwOcLo7-qTLxuQytdiYgHPEXUijJJBGsqL4IwCx_kbluZbyyC9aBrxqigcB8M9oEAgGw_wOCko5TLDrRqJned5eQLkRdcWNXeqO6W-Fd3jCUnpsgzz2Vpy9x3T_fZOF7gDB9a3nTI5ZlbKYqgwvppe7_Q4LiPWF1qeEl0ogzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b596013a4.mp4?token=ZFD1tgdf66_3C4wOiKjWYjlRGyrmjEbOl_0TIOUC14IdIamLkANQQWLDigC4eIuxmhEB1_E2jEHfXYtTkGJ1oDr1tISLeV2I_yS4lwyUnR87Yv-_0t8zG-bnV2HOyuXSjkiE5hwBWt3gzoyh8mHnjhu9mbAlRLHOoYylAbIgOpfHSwOcLo7-qTLxuQytdiYgHPEXUijJJBGsqL4IwCx_kbluZbyyC9aBrxqigcB8M9oEAgGw_wOCko5TLDrRqJned5eQLkRdcWNXeqO6W-Fd3jCUnpsgzz2Vpy9x3T_fZOF7gDB9a3nTI5ZlbKYqgwvppe7_Q4LiPWF1qeEl0ogzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایندگان آمریکا برای سومین‌بار با طرح استیضاح ترامپ مخالفت کردند
🔹
اعضای مجلس نمایندگان آمریکا در رأی‌گیری بامداد چهارشنبه، با آغاز بررسی طرح استیضاح رئیس‌جمهور آمریکا مخالفت کردند.
🔹
این سومین طرح دموکرات‌ها برای استیضاح ترامپ طی دو سال اخیر است که ناکام می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462346" target="_blank">📅 01:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qx2mAXf0vv0xTI_inv9Gywas_Pk19xHvpTqOsH4edB0_WZoW0dYLHOkzPl4sB5T1eZS5zyczfa6ukiFHn3wndfXVb7dYBHNm0apmNquMXlS1VnHUdtJbdm8S377p1xQNU_NMbB7BrFJ4SgrfXffUbjHrl9tNHrwxG0snoi8hjRFCWvltnXQNHrwo-r4H4N1WMgvRq4x4giwqWXgZCuwMW9aZKTtLlznb4ZE5iXPXju2Y0bxU-4Iqi8zvMbUgHvW-4pafb9LqquPD3kUqoy8vNP6T0vRRFejP-eF-3CWRoBa8B6wUqZtyTCI-mhdEcm0nG0YEhxiI0vh3-NEKREUH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsjAWUX6LYUPIPSLt31CN7CY26VpdZVaSlu5iDWLi9zstqLLlH41423I9peKrRJMCFjOOkcr6g0Ew4wheVmUbUqP4zgna9TsZchnKRmTlgC4UCdFOCIRYOPHCceoaiQZAbmUmfFNbAwb7_ePyw5AziGZHp_ORXJt0vsuJSQvOkJZtZ-0dnStfbfk1r5hb_yuB2F2LYKo3t65xElT42Ty4yidil-qwXg1KW0KcIcCUnhTnzZ6Ntp8xpStcEHVxiTS3SSu1JOx9DqCwv8T6nh73I4q5_DNufBTtqYssogmOlUS7JLTCeC5Mb3MSQPzV23jkLZahgq7df3EwUmE-cs47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZsAf6e-C0lnR9neTKzmh8pqSWx824WDxrf5B0oRcEwZ8Wz4qZvzxcJRtj5NzpGaDFIYKZqrCyIQoSTG67FYye4sAeomQKVkFVFFNkf-cfrQi-Nx-mQfv6rOJ0PfQdwggNtq8r-DKPG13tdA3m4cpp59q4vL48QxDCV3IxM2ytdTGQV5TX0jmotBF7JSwnTEdoGvi3BI5CksQiRVoogr_FyNofANYQ3WMr8KPXIWP1raTL8FL9br8HV2ersF1i6Jnr48BO5C1vkFoN7E0UmjphRjx7absBVz_gz8qm9y3Xa4u8PMmAwnsbIp9wjGvISuFs_1_uHWKXk5mGGGuSwTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVRVsJRpRiIbnITggMNbvy4azNB-nsk1-Db-d94KZh4Cp5hHKG8UN_TZ02w0C58m-vms1dLQHZL--MfiweSf0WaN-Si7oYiTQgixZZvQ-k9CrGK2mGm9m70_VcWDQjCuECmdu8M8TWzPFsQtyYXn1vDhIGrEHNzP_OlStIBXciMTK1hB2c_WS4LFA-b-POK7f3twlXIJa17qbcdGt943YZ0-lFl-C_6sbFvN1Yz8aSGNcMdhHlSAwPo-MGw7LASXPGYmuMLWLGXogCGV5zOrUV2NjLQzYxmYH8nA2toAD_xvrcqeSX-A7LNCj1N-R465hFIcM4f2clv-FELEz9kfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GddshuTUlLTwk9h82VgS_xfFSFuH0eaOx5AfvXuOvXDyipknqU7LMYUFxgHYC0gl0sdPiZ5_gb1HNoup8Sy1nE9jVMHEsLMp9332cO5kLjGDkee8_l6MaJibwrNf3BPwW-Fr1jhcO3bNIo2VEQj0naJdGeah-IzbRaShT3Se_3m8rMLnrzdyrsaG_rJFTSTOeqLgNRhEgR-yLJUa_s6nFiMeHKfMuzoAfEpLS_7l-boq4LbYHAWMD4RQ9lGaODNnzpM_CozDq6T4EkwbUi4VsYDTdwefM7HaOWMQYUbPdM1-gbiXkEOnVShp6F4W24TQSqTxr2zlNBOQxMH37q64aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp_2uwn0vgOvKTfWtkg6oMfUd1FP35t20Sknkja_DcCUuYmS7Y2jWu0eYa7TLuZlJQLZMjutW2mrFByoXmexjK0BybhkvC18Rc5ofp73_9WuDdjtEvyVJBfkVp57fzH307fMIzIAYG0N6i31XFrEiUEfd9vyc47Nnd9Ud8q1-E3OeTP1x2Haj0FXl7tyzYP0PRtI1uhb58kUWVGSFKD89w1lE5vE8GWsmNwqNI3yITGBZwq0vvWwwJf4Zzn3EbxljSIxaBKQc44z7UV08OAPM3_V5Ad6_PkQ4QseIclBatu3a4fYm0Y4F9enG9s04RqYUdd9gUeZVNTy5O-83GQ2Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن ازدواج ۱۱۰ زوج تهرانی
🔸
جشن ازدواج ۱۱۰ زوج جوان تهرانی  همزمان با شب ولادت حضرت عبدالعظیم حسنی علیه‌السلام در برج میلاد تهران برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462340" target="_blank">📅 00:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آخرین وضعیت تردد در مرزهای ایران و عراق
🔹
تردد زائران و مسافران از مرز خسروی بدون مشکل ادامه دارد، اما در بخش تجاری، حرکت کامیون‌ها و تریلی‌های صادراتی با کندی انجام می‌شود؛ طبق بررسی‌ها افزایش بازرسی عراق، از عوامل کندی تردد کامیون‌ها است.
🔹
در دیگر مرزهای ایران و عراق نیز روند ازسرگیری فعالیت‌های تجاری در حال انجام است.
🔹
رئیس اتاق بازرگانی اهواز گفت فعالیت تجاری مرز شلمچه نیز از سر گرفته شده، و بخش تجاری مرز چذابه هم از صبح پنجشنبه ۲۶ شهریورماه فعالیت خود را آغاز خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/462339" target="_blank">📅 00:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">منابع عراقی از وقوع انفجارهایی در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/462338" target="_blank">📅 00:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE40mv-vEGEiuQuMDyU_4Hw9_iOyHphVS66Ysl8A-Z5pV7DXCP7v_MXJtr-9Wa8XMNDWYtaiXpOZUVSeHDZZhSBX2XQRkuYQ4CPl681Sl4GasUtyUkTGy7SKdjKNLB-kBtxouF_6DkyI8TwIV6KOe2fg-NF0K4irbR-EPz9zBKDfi4iWsohoS0YBptxAzlBRSvW1B2AfQZGW1SMvs_JFB6oAXil91ukORLdu_YwdHznBCuf0pKRNez6oifxWoNpmkg9QN-OThJvgcOaCK4RRNhAX1p9YK1GZr6SgbHOK-BGPl2cvWFp0R2ibfvMzFWoHzuWrAe5C9gkIK5sBUj0raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یکی از فرماندهان گردان‌های القسام
🔹
حماس در بیانیه‌ای شهادت نائل ابوعبید، فرماندۀ تیپ رفح را طی عملیات ترور رژیم صهیونیستی اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/462337" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff12330ede.mp4?token=J3ntQAGGKqsL3ThFnM-BWRhRs0iP6sr5DXVP-eGvk3b8WWvLmbczXmfP5bmooGimQkmBNe3DBm_UVirKHATpvVqSWlgND2tHa-cteWMn8utPYfuEpX1EAqVJ0WFcIIbreORvZ-a_QoC5RvoMAlpo1aWZb91MgzNH1lwFaQnk9jie2FoHkUC_vc5vZ0xhRAfFUMYouxhE0evSFrumotHg7hIAd5oexlziOgjwmt_9t9rAhvfFt2xjYH76zx4T99KCKAiR1Z7UsF_v5ItDAANeUHZchlgwg5SOPVpdYdmlvwJmQecO0si9zS2hfHbWYRdKC1xHWgWU8lJizQlkJ69ZlbTkBSW26xAqb9uolLTXaPnWq-e_vpR-omGTzLLQB0cqodh63tzMOe7BT_7JIodd978eC9ajjxbPSmbPhNJ53wL8T1v763I6S-mAlkTvGpTfp11Uflc-VP0eJ-FRyr9hDu3QRjmjpRKRP8C4Ab92UAUEq5dV0lBtlKCmKJ38NVx1wOGgrtyFlhHVHiwc05V-GQtvWtt-GGRY8F3BKT59GXpHYyWHJH_2rodngUQ2IkfLSU7hfn7F4y3tGE4Kfg8P-RnKSDi0QhqX3ITXxuYNwlFpCDD2Km5VA6JqBiHA5s1CeB7rjjoNONjzFjiToRpdO5TWHhu7DdImWILOqscaQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff12330ede.mp4?token=J3ntQAGGKqsL3ThFnM-BWRhRs0iP6sr5DXVP-eGvk3b8WWvLmbczXmfP5bmooGimQkmBNe3DBm_UVirKHATpvVqSWlgND2tHa-cteWMn8utPYfuEpX1EAqVJ0WFcIIbreORvZ-a_QoC5RvoMAlpo1aWZb91MgzNH1lwFaQnk9jie2FoHkUC_vc5vZ0xhRAfFUMYouxhE0evSFrumotHg7hIAd5oexlziOgjwmt_9t9rAhvfFt2xjYH76zx4T99KCKAiR1Z7UsF_v5ItDAANeUHZchlgwg5SOPVpdYdmlvwJmQecO0si9zS2hfHbWYRdKC1xHWgWU8lJizQlkJ69ZlbTkBSW26xAqb9uolLTXaPnWq-e_vpR-omGTzLLQB0cqodh63tzMOe7BT_7JIodd978eC9ajjxbPSmbPhNJ53wL8T1v763I6S-mAlkTvGpTfp11Uflc-VP0eJ-FRyr9hDu3QRjmjpRKRP8C4Ab92UAUEq5dV0lBtlKCmKJ38NVx1wOGgrtyFlhHVHiwc05V-GQtvWtt-GGRY8F3BKT59GXpHYyWHJH_2rodngUQ2IkfLSU7hfn7F4y3tGE4Kfg8P-RnKSDi0QhqX3ITXxuYNwlFpCDD2Km5VA6JqBiHA5s1CeB7rjjoNONjzFjiToRpdO5TWHhu7DdImWILOqscaQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۹  شب؛ روایت ایستادگی مراغه برای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/462336" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ce02260f.mp4?token=Bu6fTsNOSIA2OBB3mq4YCd0TMQViejuJ96QAuvl8YTxGomF551eIYRJ3oetsKVvgN0AYOdcCKNs1dvDKG1aeNt2ctEGa7z4-EBqjO4GBxJdN66jExDsVtaBgXPRSGtvPIFvfLSYAkT3UCJnNpdfaLYb4uzgjqzuLvygTmCCc2r0x5lrhNIZgd3KfS_FtozAWdGmb1EWlDXJo0BJ0h0rKQ0kfRuAEr71ullzL89Z-SN9uQzTooRTRhB5VIqWK5sjDhA00_3cCQz5ARNvU6azRXWALAgWeRqkwippsd_yFtv6Ew0gE7OOXX0IlPI2N-ouA5TNczICGapGtw21GdmST_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ce02260f.mp4?token=Bu6fTsNOSIA2OBB3mq4YCd0TMQViejuJ96QAuvl8YTxGomF551eIYRJ3oetsKVvgN0AYOdcCKNs1dvDKG1aeNt2ctEGa7z4-EBqjO4GBxJdN66jExDsVtaBgXPRSGtvPIFvfLSYAkT3UCJnNpdfaLYb4uzgjqzuLvygTmCCc2r0x5lrhNIZgd3KfS_FtozAWdGmb1EWlDXJo0BJ0h0rKQ0kfRuAEr71ullzL89Z-SN9uQzTooRTRhB5VIqWK5sjDhA00_3cCQz5ARNvU6azRXWALAgWeRqkwippsd_yFtv6Ew0gE7OOXX0IlPI2N-ouA5TNczICGapGtw21GdmST_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رفیعی در برنامۀ سمت خدا: انکار خمس، انکار یکی از ضروریات فقه است
🔹
کسانی‌که سال خمسی ندارند، به دفتر مرجع تقلید خود مراجعه و برای تعیین آن اقدام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/462335" target="_blank">📅 23:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
سنگر خیابان میزبان ۱۹۹مین قرار شبانه کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462334" target="_blank">📅 23:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVQ9nckqWgKajip8QNsg6yTkTzQDAwXgRhWfgsMrLEK0-qKs482kJlj1CwUqwmxtcmbrw7gjMwdx7lrxh-_E9GSHcAFrFBm0NtB9XtMidC4nhxNsNux2ifhFvxKgB4kPsHuXpAcnDdehcwX9rq7m189FrrvxBQHp0I_HXawOWOdS1a6MH-XwmgznEX1rkEBVIBHw5J0qGeeDkb7WLIjuFoHsXWBPQUCg0K69oahx-I8dN2-PA8bAQ_N8hB4QHZ5BDamKZ4r3EF9B6m9tY58VZaGkaAnMTEZzLrQLDZjHH3Gp3I2hsD02Xir9_3HWq1Edf177VLZcAkyHU1ZMJYTXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلاک ۱۶۳ خودروی متخلف سوخت‌گیری در رودان منتشر شد
🔹
رئیس دادگستری شهرستان رودان: در ادامه اجرای طرح پایش هوشمند جایگاه‌های سوخت و بر اساس اطلاعات ثبت‌شده توسط سامانه دوربین‌های پلاک‌خوان، ۱۶۳ دستگاه خودرو شناسایی شده‌اند که طی ۴۸ ساعت گذشته بیش از یک‌بار در جایگاه‌های سوخت شهرستان اقدام به سوخت‌گیری کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462333" target="_blank">📅 23:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462331">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cs7ZTH-lfWNGo1JZzWgQQMpalFftpkgKGSjj94LyoPY3eLLnqN71UPoRIbGRF8KIVX3HO4Gbx7VQbi2ljS9YAKi_HZPAR1989P97_yv3RZXwc7PD5lvnWB58tqUE_kFA-OtfQCrDjJz9pUs6O1A2PZgP5bKU32LSBvgLDhqZPoqb8gmuEsL-CPO8g-Z4DrRwj8x1z1chJZtmA2dePocVkR5oMmA9X0UHgGeYDzcSw9yrnTwKCKGHB-Kot28oQgQdhBw6KsgyqdSg5QrkZPDc9-BKRNo7HC6XU3bPVrQ0ZJTaIPJFQ-o7vrZ7syAXDMZOsS7-mHPn7BGCCfp-MvknQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtcRLATV7YNT9FKXQ4rC70zVcJ7y1nCup22XmmKnow6C3S4u8QEuBuU1ai6k-EH264WPv8s-MygsfVG6L1wHoVSobJykvtGGefgSJx-U0Q40dVS97SPpCuylWplrc32rLFFa-iDzTjtyEjGuC9scQhHTK7GE8FLlvHy5gLODjF7YaOxUjZFlF_U4fn5ta1BqQ57WzH5r4cYMvXSZm9PaAzimecmGBkYYa0XgmTzpKo1w7nGIGDXUJjJxMfNugg5c3MdDgvX8K2crfsU_TPRrdU4QB93_6PMDqWnHfRAaGyTHWaUjN5St5RToLhk8jsVJT_0t-492PZrh1FBXnWfYbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار الجولانی و بن‌زاید در امارات
🔹
الجولانی سرکردۀ شورشیان حاکم بر سوریه در سفری به امارات، با بن‌زاید، رئیس این کشور دیدار کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462331" target="_blank">📅 23:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462330">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b19438ce.mp4?token=Jz5tKpXnYQ0yO7O4B7Fz1JBl4RGEvLoVeBLWUWGeiyj_fiOJ1Y7hSFdYc1k07Xrr9W05ghnZrJMBz4YhsSKQE2VGqylQBzGrx6nxqRmAya6m7G5sV-6GBQtCnABk4eLKenInOAjaa5qMMocKXLBiBLUVN1Sip3LpAfmAQVTo0FQXtt492XqalbTwwekjJc1Q8ydaUyWu8icADbzc6LGh7QjObyH_Z8DM_U-Ci2tvs7vpasRX99i7lctBMww0kQSCP-kOq7R1E_IyMTIG5qH-c_fqKcEnh8-a6QIjeiG65r-bCGcGsy920DBYfDCOP-cyPVha3PxQyYO39SI5bVpBUJo0ODdTgtI8Fe013XaLMnVzyv3K4UaEeWDTqGxWh4zWX0g19MGDeuEnrjvkWH4OlZjsTnVSfbDWdqI_0nlz-OF1SV_GSMvdUBqvnmwfreNvT_J87Nkq9c_BUWZtMzRGsCEzuZzRMsqN3HI2FDZc8p9jRAEErsm7fuGWvnn8Ow21xNsNdOF6LmIg5OMRHXC6JzanN3MnOBzTU33TRkD9te3bnDYqmzSVHNyJ6bve6Ja2ZmqnixuXYi52FZJVKVBTcEluwc1ak3dqtyIDstnIs45146ce0q3PK2XxUACvKjCM8I_qBVskQ_r9aY0CWJ_2-AYuGSug4CIG9thZ5oxZ8UI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b19438ce.mp4?token=Jz5tKpXnYQ0yO7O4B7Fz1JBl4RGEvLoVeBLWUWGeiyj_fiOJ1Y7hSFdYc1k07Xrr9W05ghnZrJMBz4YhsSKQE2VGqylQBzGrx6nxqRmAya6m7G5sV-6GBQtCnABk4eLKenInOAjaa5qMMocKXLBiBLUVN1Sip3LpAfmAQVTo0FQXtt492XqalbTwwekjJc1Q8ydaUyWu8icADbzc6LGh7QjObyH_Z8DM_U-Ci2tvs7vpasRX99i7lctBMww0kQSCP-kOq7R1E_IyMTIG5qH-c_fqKcEnh8-a6QIjeiG65r-bCGcGsy920DBYfDCOP-cyPVha3PxQyYO39SI5bVpBUJo0ODdTgtI8Fe013XaLMnVzyv3K4UaEeWDTqGxWh4zWX0g19MGDeuEnrjvkWH4OlZjsTnVSfbDWdqI_0nlz-OF1SV_GSMvdUBqvnmwfreNvT_J87Nkq9c_BUWZtMzRGsCEzuZzRMsqN3HI2FDZc8p9jRAEErsm7fuGWvnn8Ow21xNsNdOF6LmIg5OMRHXC6JzanN3MnOBzTU33TRkD9te3bnDYqmzSVHNyJ6bve6Ja2ZmqnixuXYi52FZJVKVBTcEluwc1ak3dqtyIDstnIs45146ce0q3PK2XxUACvKjCM8I_qBVskQ_r9aY0CWJ_2-AYuGSug4CIG9thZ5oxZ8UI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب تهران به عطر حضرت عبدالعظیم(ع) نفس کشید
🔹
فردا سالروز ولادت حضرت عبدالعظیم(ع) راوی حدیث و مورخ برجستۀ شیعه است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462330" target="_blank">📅 23:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462329">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e625c5de7d.mp4?token=Rwx_jOQuOSdFHF5h3ymNZ2wNgjEhM_rijhW7Fko3dDv0wVmeileNoP4751gZLI6STLBTiapCvf9TISt8xRO1z1Qex81r9_MW5DyI50yW3YJMt-Q15ob3A_81lqB_nWlTW9ZUJLMBlDOgw2IK0kejo_SCPPxttNY0YMK0atOxx8jGY19OWuwwAErmnIl6tMIRPw5Y7AiyqePC_OG-JsUpVkmbrBpvEX1JKvoO1Hj03kTWALKwBLBPKVo_8RLGtR_c_T5cAqFQfxLjvs6kj7EzkOr_MMgiujwOmyp1HMAMA4Vh31B9Da6wywSfnSfF0O8quTuKCnMennNkXtuSaizPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e625c5de7d.mp4?token=Rwx_jOQuOSdFHF5h3ymNZ2wNgjEhM_rijhW7Fko3dDv0wVmeileNoP4751gZLI6STLBTiapCvf9TISt8xRO1z1Qex81r9_MW5DyI50yW3YJMt-Q15ob3A_81lqB_nWlTW9ZUJLMBlDOgw2IK0kejo_SCPPxttNY0YMK0atOxx8jGY19OWuwwAErmnIl6tMIRPw5Y7AiyqePC_OG-JsUpVkmbrBpvEX1JKvoO1Hj03kTWALKwBLBPKVo_8RLGtR_c_T5cAqFQfxLjvs6kj7EzkOr_MMgiujwOmyp1HMAMA4Vh31B9Da6wywSfnSfF0O8quTuKCnMennNkXtuSaizPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد در شب ۱۹۹ بار دیگر به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462329" target="_blank">📅 23:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462328">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVW61vfofsziJVwVCDrz8GQxk9EjqHPDghvW5oj1TaBzWc9YOudM_awSSSzmDBWgFa3d0yohP4Z4UwSvF1zIHvEd7LwHl0kx34neVYmVNii73G5MNL4LJH6b8_bldTP7r3UI5l8HnUORzjso_6iYLGOvY-bT6QONYrqBkCwh9VdYPeFdpwJ62vhAc2jd4YOaBf2q7B9jUl7s6HyUq3-Yxvqnf-ZPBp8mG8C8xL_6hIvURzjas0o3--DV1LOHYHZsEg6byLOhEwJB20aQW-c_NozeAjZ8JJSIT4qAxbcbU_afBvARoJJSDspneamLLDYBgf3HZvG1Xix5fAecewmyqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹ خبر خوب از جای‌جای ایران
🔹
«بستۀ خبر خوب» امروز را از گوشه‌وکنار ایران تقدیم می‌کنیم؛ روایتی از تلاش و امید در سراسر ایران.  تخلیه و بارگیری کالا در بندر سیریک ۴ برابر و تردد شناورها ۲.۵ برابر بیشتر از پارسال شد
🔸
بندر سیریک هرمزگان از ابتدای سال جاری تاکنون…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462328" target="_blank">📅 23:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a5fb9fd1.mp4?token=Q5tpaz3uA7rPvqOwfpAj3l_NK9qjgme3RptnrvRROizakmyOymAoRi9vpdbGC4n_ZG-hZxJVF0tUXKLgHkySI0EjzYsA1ml-7XGbKVAnU_SXaWTHxfTOaaSWvP18gz8sYYGYNVod8NaV6v6amJ-VURuvZMtuSUbm2cH1h9PpwQEtVjcAT4TZ5vBRyM73bfo3o2eo49jnGQR8WnaWy3d9uVGxR6yT4rYWspNT3-Vao3n4ZDvJbnfsRe9RoVppOnk-WpgtrRyZYLrtqrC-CnnvJo_H_flhi30wOt_2F-X-Rxbl-KW3cAbEFJNy94a6DJEb4C9mm17xl6HaNvHdhOfEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a5fb9fd1.mp4?token=Q5tpaz3uA7rPvqOwfpAj3l_NK9qjgme3RptnrvRROizakmyOymAoRi9vpdbGC4n_ZG-hZxJVF0tUXKLgHkySI0EjzYsA1ml-7XGbKVAnU_SXaWTHxfTOaaSWvP18gz8sYYGYNVod8NaV6v6amJ-VURuvZMtuSUbm2cH1h9PpwQEtVjcAT4TZ5vBRyM73bfo3o2eo49jnGQR8WnaWy3d9uVGxR6yT4rYWspNT3-Vao3n4ZDvJbnfsRe9RoVppOnk-WpgtrRyZYLrtqrC-CnnvJo_H_flhi30wOt_2F-X-Rxbl-KW3cAbEFJNy94a6DJEb4C9mm17xl6HaNvHdhOfEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: نحوۀ پخش سریال‌ها را تغییر دادیم
🔹
در این روش سریال‌ها دیگر هر روز پخش نمی‌شوند و در روزهای زوج یا فرد یا آخر هفته‌ها پخش می‌شوند.
🔹
پخش هر روزه باعث می‌شد مخاطب برخی قسمت‌ها را ازدست بدهد و ارتباطش با سریال قطع شود. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462327" target="_blank">📅 23:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3123fc9ea5.mov?token=e75OIi0Ux8i6_G1h-JdBvlBkZQza3oAQS3HzfiUjQiMfYUOe9Cmmg0DNJ2pcJGWTuIVX6A2B1zImKHIIADXnoIwFnc_jwBnwwg2alGyHS7pPaJ74K7IjU54fDeFeDcfb9XQcgFqMdz0x5xOujo4AZ4laAMlCmDoKu8RyR3ArvabCZxw4m3xkya-gAKBoolUOBdvbXLfP5_anK2BxCVcoH8KPr3KOfgHLfQyS1MflgbBHMWEdjoIZ9YruswFOEW-RS1CP36Giq4LIMJTOn19EGRt_Tnq5wECsE7yjgfrBSFz6AgYZxcjh_lCMdQCzjDIIsiklLdIq0OMYbLndEU0UEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3123fc9ea5.mov?token=e75OIi0Ux8i6_G1h-JdBvlBkZQza3oAQS3HzfiUjQiMfYUOe9Cmmg0DNJ2pcJGWTuIVX6A2B1zImKHIIADXnoIwFnc_jwBnwwg2alGyHS7pPaJ74K7IjU54fDeFeDcfb9XQcgFqMdz0x5xOujo4AZ4laAMlCmDoKu8RyR3ArvabCZxw4m3xkya-gAKBoolUOBdvbXLfP5_anK2BxCVcoH8KPr3KOfgHLfQyS1MflgbBHMWEdjoIZ9YruswFOEW-RS1CP36Giq4LIMJTOn19EGRt_Tnq5wECsE7yjgfrBSFz6AgYZxcjh_lCMdQCzjDIIsiklLdIq0OMYbLndEU0UEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی پویش جانفدا: با وجود تکمیل ظرفیت گردان‌ها، سایت برای ثبت‌نام سایر متقاضیان باز است
🔹
افرادی که پس‌از تکمیل ظرفیت ثبت نام می‌کنند در لیست انتظار ذخیره و پس از هماهنگی با نیروهای مسلح سازماندهی خواهند شد.
🔹
در کمتر از ۱۰۰ دقیقه ظرفیت ثبت‌نام برای یک…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462326" target="_blank">📅 23:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dea6cc2c3.mp4?token=hwdmIEgH3yQqbdvAKLBllfY6qbWV-fPELYa3CEFVZ5qi0_J-bdT1YrfPkx7jTdxM11HBwYVWhca6jPLvYZ4Rh-cn-TahclkEhARTv6T4ZaFUTzA3CBgcS6LJgaRWTesaHKS5UztGSnErZR5YPIbsZPdBpinZ1VbGg4qHSSPAC1XKX5Mei7c0wN8BNE42im-gn35iOlhjWGzSLyYZGUZQ0Ua5x4X3oqjFDhlWF9W07VY0oMlKLW6x2Fjwb4cGMNtxmAAjMlmnO3qx-oYhbrA5d1arzMGSq0Q1J2EH5S1hdoyHy7H0s0sBxTP_28o491cuKZkmu8nmj2buPrZCIYBq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dea6cc2c3.mp4?token=hwdmIEgH3yQqbdvAKLBllfY6qbWV-fPELYa3CEFVZ5qi0_J-bdT1YrfPkx7jTdxM11HBwYVWhca6jPLvYZ4Rh-cn-TahclkEhARTv6T4ZaFUTzA3CBgcS6LJgaRWTesaHKS5UztGSnErZR5YPIbsZPdBpinZ1VbGg4qHSSPAC1XKX5Mei7c0wN8BNE42im-gn35iOlhjWGzSLyYZGUZQ0Ua5x4X3oqjFDhlWF9W07VY0oMlKLW6x2Fjwb4cGMNtxmAAjMlmnO3qx-oYhbrA5d1arzMGSq0Q1J2EH5S1hdoyHy7H0s0sBxTP_28o491cuKZkmu8nmj2buPrZCIYBq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: هر پژوهشگری که نسبت به نظرسنجی آمار مخاطبان صداوسیما تردید دارد می‌تواند از نزدیک فرایند این آمارگیری را مشاهده کند  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462325" target="_blank">📅 22:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9ced33d6.mp4?token=N0eGyclVbw3OMk0C3XTDQQ4bFUreXgzvxCd56eihiXrrqyVukCRzi_e67JHtz3_uOfdvhbUb3Q41WJpDolij7h9VKJmIthXUZTrJtt7UJo9sH9T5hjh1r7Rp8nAYraHnBy4sSm6c2KayXo3R3RWWnb7u9d0yE0AGYSXxIHQShR272-jchEWDSXHI57fnuwqmZeoEcCpWVJcZPuD3bIXoHIKWxrc6N5mt60_Y8dh9p3XcIS2FoDCFEGwH7T396MDF4_NZNJiRO2FfznATrbGZiazUIhToWyFfdgIwXXJfW66dfDOmpWHKX6uFRAjrvGB32meqzyHteOda92OAgLegfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9ced33d6.mp4?token=N0eGyclVbw3OMk0C3XTDQQ4bFUreXgzvxCd56eihiXrrqyVukCRzi_e67JHtz3_uOfdvhbUb3Q41WJpDolij7h9VKJmIthXUZTrJtt7UJo9sH9T5hjh1r7Rp8nAYraHnBy4sSm6c2KayXo3R3RWWnb7u9d0yE0AGYSXxIHQShR272-jchEWDSXHI57fnuwqmZeoEcCpWVJcZPuD3bIXoHIKWxrc6N5mt60_Y8dh9p3XcIS2FoDCFEGwH7T396MDF4_NZNJiRO2FfznATrbGZiazUIhToWyFfdgIwXXJfW66dfDOmpWHKX6uFRAjrvGB32meqzyHteOda92OAgLegfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هواداران استقلال در ورزشگاه بصره قبل از شروع دیدار با السد
🔹
نکته جالب حضور برخی شهروندان عراقی با پرچم‌های استقلال است. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462324" target="_blank">📅 22:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fe35fcf7.mp4?token=EU6-yg0sp8nzikkaM0uTHNNCKZ_Kis_YmNZph74jxnCg_tNcyReZ5jVLgKvVPtmNyecYiT5ikFpZJLjAzGcoMLy9eNRsxVr6-crNNq51LDG4uvh5_Ks9U0XBww97pLJ9Gvv49mQMcZHye-yWLS2MWwhNRlPjPCnD8Gtk62WY-pDWh9zHLAFVUjvbPojC5UCsw9VZmkB0cdG7SUSh_ZA3lLY2VAp-e65tEYK4jjN0gPM5VLaeNbdFxAleLiV4sYP4sZIkZdYijqm4UExgcAM3ni44QBgkXNBfGErmro73V0TArZuM8Fjkn3Lu8qKUPDvX07ZMx5UJlgcM5v0CurobSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fe35fcf7.mp4?token=EU6-yg0sp8nzikkaM0uTHNNCKZ_Kis_YmNZph74jxnCg_tNcyReZ5jVLgKvVPtmNyecYiT5ikFpZJLjAzGcoMLy9eNRsxVr6-crNNq51LDG4uvh5_Ks9U0XBww97pLJ9Gvv49mQMcZHye-yWLS2MWwhNRlPjPCnD8Gtk62WY-pDWh9zHLAFVUjvbPojC5UCsw9VZmkB0cdG7SUSh_ZA3lLY2VAp-e65tEYK4jjN0gPM5VLaeNbdFxAleLiV4sYP4sZIkZdYijqm4UExgcAM3ni44QBgkXNBfGErmro73V0TArZuM8Fjkn3Lu8qKUPDvX07ZMx5UJlgcM5v0CurobSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پس‌از دوره‌ای کاهش مخاطب، از سال ۱۴۰۲ به تدریج درحال افزایش مخاطبان رسانۀ ملی بوده‌ایم  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462323" target="_blank">📅 22:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">جلسه فوری پاکنژاد و شریعتمداری در آستانه مجمع هلدینگ خلیج فارس
🔹
طبق خبر رسیده امروز محسن پاکنژاد وزیر نفت و محمد شریعتمداری، مدیرعامل فعلی هلدینگ خلیج فارس جلسه مشترک برگزار کردند.
🔹
پیش‌تر رئیس‌جمهور دستور داده بود تا مسائل وزارت نفت و هلدینگ خلیج فارس از مسیر جلسات مشترک حل و فصل شود.
🔹
جلسه بین پاک‌نژاد و شریعتمداری درحالی برگزار شد که فردا قرار است در جلسه مجمع هلدینگ، ترکیب جدید هیئت مدیره این هلدینگ تعیین تکلیف شود.
@Farseconomy</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462322" target="_blank">📅 22:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b661f8b8bd.mp4?token=VNBk09SJ2UGH30_46XCLQKWnKBflSmquAM1DBpa_U7vgCULQf7cYKdr-4503DtY55Bv6ThXZu1D_ubdXj4gNojwy5TjoeGDfMQ3EP_UA9qAw6sRrp-Ig4S8K-kOfUurDvZ4WPpTAakvwdkYjHoxSu6a_FCXDly72xd9FRSVxhNtIIqWFnpgVPzHX2G_Nyr21RmpUtcyBGPIicDB01HDyYAdjVlKzE9hT7wGyu7N0LcJH1I4JTnt2mSZLoFqGv9AIbaur7XeTDdPaswN7ZkCIk2d7ymeZovfYeIHutWBcwnWpFKDEXj-g3vaTelgJ6iBedCmLgfgPGwg3MC10jUpCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b661f8b8bd.mp4?token=VNBk09SJ2UGH30_46XCLQKWnKBflSmquAM1DBpa_U7vgCULQf7cYKdr-4503DtY55Bv6ThXZu1D_ubdXj4gNojwy5TjoeGDfMQ3EP_UA9qAw6sRrp-Ig4S8K-kOfUurDvZ4WPpTAakvwdkYjHoxSu6a_FCXDly72xd9FRSVxhNtIIqWFnpgVPzHX2G_Nyr21RmpUtcyBGPIicDB01HDyYAdjVlKzE9hT7wGyu7N0LcJH1I4JTnt2mSZLoFqGv9AIbaur7XeTDdPaswN7ZkCIk2d7ymeZovfYeIHutWBcwnWpFKDEXj-g3vaTelgJ6iBedCmLgfgPGwg3MC10jUpCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پس‌از دوره‌ای کاهش مخاطب، از سال ۱۴۰۲ به تدریج درحال افزایش مخاطبان رسانۀ ملی بوده‌ایم  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462321" target="_blank">📅 22:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462319">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462319" target="_blank">📅 22:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462318">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4695adcd.mp4?token=m1LpT1XZaZQAiFEV_Be_B6_dR9zwOsbQl-xWklz3D8NNZRFKAfbLgIeM45CJrzlAeHgVE68KFLkxWRI-B3YaLPSiqgH52FwzBJtTNXlMeeZipv5H1rVq1gX9u2kR59Pecuekmggj_dgrHc--CfzzgiBz6sZEqGdiNoFpsiAinMFU2S0ZTTiNC_TCz5OVOh80FfxcbXuYkjBcNVwXG8WePWnjGiaXSF-WZniLGAUaaL6QHSzoKD26s1-kE9J9AkBx9s9aCL1sU_qRuSjaDyaBHjUfRltEP5DjqqNWa-pRPBznULQ9LtX_X55YqTsSA_VPufxuo86qWQiiZj0_vwKXuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4695adcd.mp4?token=m1LpT1XZaZQAiFEV_Be_B6_dR9zwOsbQl-xWklz3D8NNZRFKAfbLgIeM45CJrzlAeHgVE68KFLkxWRI-B3YaLPSiqgH52FwzBJtTNXlMeeZipv5H1rVq1gX9u2kR59Pecuekmggj_dgrHc--CfzzgiBz6sZEqGdiNoFpsiAinMFU2S0ZTTiNC_TCz5OVOh80FfxcbXuYkjBcNVwXG8WePWnjGiaXSF-WZniLGAUaaL6QHSzoKD26s1-kE9J9AkBx9s9aCL1sU_qRuSjaDyaBHjUfRltEP5DjqqNWa-pRPBznULQ9LtX_X55YqTsSA_VPufxuo86qWQiiZj0_vwKXuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ ترور مولوی یوسف گرگیج در زاهدان  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462318" target="_blank">📅 22:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462317">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
منابع عربی از فعال‌شدن آژیرهای خطر و شنیده‌شدن صدای انفجار در منطقه‌های جیزان و ابها در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462317" target="_blank">📅 22:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462316">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e076801b.mp4?token=HPBBmzTTqC3YcnUoqFihwG3bMk9rK7S90u2u_gFCpolabTYImCIvXg532RuH4SOFb--8BQ5ifSyZpUHHwGRQKbHm3k6zamQSfjbHR4NrdAMLbu-goGQ46Yv0-ESFCVz3ZS_ZWYxTKdFD9LYXrridAqFsPzY99miz6t7PoP2S1eGJa_R3Av_MKJeoy7dIm8NaMVUVeOpBlLj100azwSV0_RPI3ZM8nfEAvPwV0F_AhzeYRaFDT1ELhdlGq6mApWrMuEJlOOAxWJbqnUxM72YYIaTxeJ3dpNG6h4XD0fmS-6Mo9wc1PPqIKcDyMhj7Lym0TDmwfMdM8CPVOT-OGPkuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e076801b.mp4?token=HPBBmzTTqC3YcnUoqFihwG3bMk9rK7S90u2u_gFCpolabTYImCIvXg532RuH4SOFb--8BQ5ifSyZpUHHwGRQKbHm3k6zamQSfjbHR4NrdAMLbu-goGQ46Yv0-ESFCVz3ZS_ZWYxTKdFD9LYXrridAqFsPzY99miz6t7PoP2S1eGJa_R3Av_MKJeoy7dIm8NaMVUVeOpBlLj100azwSV0_RPI3ZM8nfEAvPwV0F_AhzeYRaFDT1ELhdlGq6mApWrMuEJlOOAxWJbqnUxM72YYIaTxeJ3dpNG6h4XD0fmS-6Mo9wc1PPqIKcDyMhj7Lym0TDmwfMdM8CPVOT-OGPkuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پایبندی به هویت اصیل ایرانی-اسلامی می‌تواند مخاطب را جذب کند
🔹
محفل و معلی ثابت کرد می‌توان برنامه‌های معارفی را در فرمی جذاب ارائه کرد که مخاطبان زیادی داشته باشد. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462316" target="_blank">📅 22:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462315">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dealTjrnWbciF1Mqtl-pxaYsRVEUb3LIyyH2IarbYASm8pYx4KqzUibyDFitLQ-IdNFoqTCBrQlUw0sv2RA0mBF0qLUss010PGfKIKC9EF1QlusnJV_qWNvfEKGp-8x5ICanFRzLSRlh-STkcOqU_Q2Sb57gywN2db3Cva2e2GvT1AKzCuUqN1Jyed6sO7_wBRwJ9NLH2GjSyNUP6XojMVW2xC-HM2G_vCFMXgUZJ5N08bWMjVcA4eR4jpFOmXNk2lEXU4cqzn_miDPts3yjLjfRyNtCvnVpXRcLaIsCBCnKaH1OeeWh5Dyboj_mfXYbHRF6P5x2racRDNL39axMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست محرمانه در آلمان؛ همگرایی نادر فرماندهان اسرائیل و کشورهای عربی
🔹
رادیو ارتش اسرائیل به نقل از سخنگوی سنتکام اعلام کرد براد کوپر، فرمانده این نهاد آمریکایی هفتۀ گذشته در آلمان میزبان کنفرانسی با حضور ایال زامیر رئیس ستاد ارتش رژیم صهیونیستی و فرماندهان ارتش‌های عربستان، امارات، قطر، کویت، بحرین، اردن و مصر بوده است.
🔹
سخنگوی سنتکام گفته: کوپر طی این نشست به همتایان خود اعلام کرد که ارتش آمریکا با وجود حملات ایران که پایگاه‌های آمریکایی را هدف قرار داده بود، قصدی برای خروج نیروهای خود از خاورمیانه ندارد.
🔹
به گفتۀ او کوپر در این نشست، گزارشی هم دربارۀ طرح آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز ارائه کرد.
🔹
این نشست نخستین نوع از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران در بیش از شش ماه گذشته بوده است؛ گرچه دیدارهای مشابهی بین فرماندهان نظامی صهیونیست و عرب در گذشته نیز برگزار شده بود.
🔸
رژیم صهیونیستی پیشتر سامانه گنبد آهنین را برای رهگیری موشک‌ها به همراه نظامیان این رژیم در امارات مستقر کرده بود؛ اسرائیل همچنین کمک‌های فوری در زمینه‌های اطلاعاتی، نظارتی و شناسایی از جمله اطلاعات مرتبط با حملات صورت‌ گرفته در ایران، در اختیار ابوظبی قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462315" target="_blank">📅 22:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462313">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808a7154a8.mp4?token=kY4nwtjh7ftYdo8wXxCFGFxlYhJqS6rWTQ-UIiOpbceDD7zt6fKDYX2ZGceF3_ywU5xNrYXC6Zly4jKvJyRtHwOPcFTOBf8tlKUiqoHHkcQ3EDfkhuNMHOeVSOnjQNo3juNxpxxpsuW4hFkLr-VovY99Hu-X7OZuTFnrhB92oyST5JTh9WUtb45tiizqTQRsdCq_4drZR9EM0gA5clpB9pntx-jm3gtIFB6_KUfnJc2ZRNPWjNuxq6vLX5CsLNk3lBIaZyxNEOywgDctU4vOxGNSvpnfhgJT9hq6QKgx95_QaAB-hIykhm0vOYJozoyhe4HlU8koEl5XWo9hbnrjKnZMBfW74PMu0lHC0vlV6mJWPeYRO1eb12LNDCQn4SL-6ZHEzGJKa8qNi_S5R5720hCkml2_qjcLgXk5nAXbt622BxgaAVQZpQq1tDhpJIn9s8uQwtewvTM0tYpN4i7luB9lC9tMff5zHH577wMPZQng5VrX-FVzPNIV66ORmlDXJEJBvrIJD6DPPaatWu0hBUkTxNII_yTUc4MzoLS38Jp_9JQZShpZ8yp2zZzaZUmBkaHIqRdx-osmcpUMsWVdeMQBL21tH0Zf7Iha2713x9sPhY6cfp9FZ6_zkVVmWbIxaCh7IMS0ALPgwPQAKASppVeGGug5HJ5YIrBbbvS_sqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808a7154a8.mp4?token=kY4nwtjh7ftYdo8wXxCFGFxlYhJqS6rWTQ-UIiOpbceDD7zt6fKDYX2ZGceF3_ywU5xNrYXC6Zly4jKvJyRtHwOPcFTOBf8tlKUiqoHHkcQ3EDfkhuNMHOeVSOnjQNo3juNxpxxpsuW4hFkLr-VovY99Hu-X7OZuTFnrhB92oyST5JTh9WUtb45tiizqTQRsdCq_4drZR9EM0gA5clpB9pntx-jm3gtIFB6_KUfnJc2ZRNPWjNuxq6vLX5CsLNk3lBIaZyxNEOywgDctU4vOxGNSvpnfhgJT9hq6QKgx95_QaAB-hIykhm0vOYJozoyhe4HlU8koEl5XWo9hbnrjKnZMBfW74PMu0lHC0vlV6mJWPeYRO1eb12LNDCQn4SL-6ZHEzGJKa8qNi_S5R5720hCkml2_qjcLgXk5nAXbt622BxgaAVQZpQq1tDhpJIn9s8uQwtewvTM0tYpN4i7luB9lC9tMff5zHH577wMPZQng5VrX-FVzPNIV66ORmlDXJEJBvrIJD6DPPaatWu0hBUkTxNII_yTUc4MzoLS38Jp_9JQZShpZ8yp2zZzaZUmBkaHIqRdx-osmcpUMsWVdeMQBL21tH0Zf7Iha2713x9sPhY6cfp9FZ6_zkVVmWbIxaCh7IMS0ALPgwPQAKASppVeGGug5HJ5YIrBbbvS_sqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس صداوسیما: پایبندی به هویت اصیل ایرانی-اسلامی می‌تواند مخاطب را جذب کند
🔹
محفل و معلی ثابت کرد می‌توان برنامه‌های معارفی را در فرمی جذاب ارائه کرد که مخاطبان زیادی داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/462313" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462312">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf0c3c353.mp4?token=XSeDut8uA1sgdMjij0FqX5-jXvNKvFO_TZP0ZydKzkuoiGMcpTVuHWO2GD6q-rm7SVLT-lv6q4gvvcjZpShypiml3TUImuO2hvc3qCeKQg0oZsgB4OJo9nwcxy1VPWepqOVWbu6SYUOcwx1z4Sp5hYgzksmPZkTua8XjjbrjdJ9Ggyuo4Msiu_arH5AH2tqTOEv6wTHPaqXzKewnmUu9RC3DMeUVHGRfn_YBXgPoaJgSyfCodz_9RBjogwGgz0U04SVPi9eiGbPO7WAzie5a_pN7V81YA3eYNlLvWwP13ybXMtpSUhDuk9UBYRbcrMjvABXSWhotJkhH1coS3ANoOSdKcZQeh0D1ibThl-yhyTbZA2HEO1eDGzb_kZ6H_fEsBJkGolWGwAwKRBpJ8nzklkD2ys9g6KwDmI12a-R8inNjKDUdx-GJfarZZCec03zdRRb8bd-I44_Z1G25edgFeBMrSFyEXkfsHZjm5hQa-bC6dgh1RZoYoLz-POnwP34Nu0PnCBXnvBrLbAO4QdenO8Bi2_r8tNzeR7gJhKbUnayr-wc-YNFHY8g_iLYhuIl7whZYOcvPFP0GpYmQC2RZ4QnwSopdOVB41LVMHGn5DJe28m-9iWdaEB49e8UJAjXoK8E9KF8smvL9xxCwcs3IktEfy0kds-g3VOmDuREaIx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf0c3c353.mp4?token=XSeDut8uA1sgdMjij0FqX5-jXvNKvFO_TZP0ZydKzkuoiGMcpTVuHWO2GD6q-rm7SVLT-lv6q4gvvcjZpShypiml3TUImuO2hvc3qCeKQg0oZsgB4OJo9nwcxy1VPWepqOVWbu6SYUOcwx1z4Sp5hYgzksmPZkTua8XjjbrjdJ9Ggyuo4Msiu_arH5AH2tqTOEv6wTHPaqXzKewnmUu9RC3DMeUVHGRfn_YBXgPoaJgSyfCodz_9RBjogwGgz0U04SVPi9eiGbPO7WAzie5a_pN7V81YA3eYNlLvWwP13ybXMtpSUhDuk9UBYRbcrMjvABXSWhotJkhH1coS3ANoOSdKcZQeh0D1ibThl-yhyTbZA2HEO1eDGzb_kZ6H_fEsBJkGolWGwAwKRBpJ8nzklkD2ys9g6KwDmI12a-R8inNjKDUdx-GJfarZZCec03zdRRb8bd-I44_Z1G25edgFeBMrSFyEXkfsHZjm5hQa-bC6dgh1RZoYoLz-POnwP34Nu0PnCBXnvBrLbAO4QdenO8Bi2_r8tNzeR7gJhKbUnayr-wc-YNFHY8g_iLYhuIl7whZYOcvPFP0GpYmQC2RZ4QnwSopdOVB41LVMHGn5DJe28m-9iWdaEB49e8UJAjXoK8E9KF8smvL9xxCwcs3IktEfy0kds-g3VOmDuREaIx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادری که با ۱۴ هزار صلوات برای امام زمان(عج) از شهیدش باخبر شد
🔹
شهید علیرضا رمضانی فرمانده ناوشکن جماران در سومین روز جنگ تحمیلی سوم پس از حمله وحشیانه آمریکایی- اسرائیلی به این ناو، شهید شهد شیرین شهادت نوشید و جاویدالاثر شد.
🔹
در آخرین تفحص از ناو جماران که با سفر خانوادهٔ شهید به کنارک در جنوب کشور انجام شد، بخش هایی از وسایل شخصی این شهید پیدا شده و عملیات تفحص همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462312" target="_blank">📅 22:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb8fa557f.mp4?token=qDVxj8pWM1TMIaP0E351W3smMw8ad2p1oceiSyiSg7lTR8lzJugo5kxhGBRU1eIyQuqZZFiRaGGJDzFcLRJpHGfPbYyjdcWnm5n4M3i3IfHiSamQq7wuiXdoeWyNnCZ70cjpwreZp2BUJfWAjDao6RzOTEjAqGXXUsMBd9HNX83K2BvRpPuotgux6cIcghtYMq_WVkJtV0gLGP5m86pW8zBZS4VRS_w__9arqLo5HEj4Scl4GPRqxwF8ZB5DWip6uuDeCnnGphigSxLyBVqy4QJD-aTrOI-gbVRbopUq70-Q8gwKibnNIYkArY58N9-BzmI6lZRWNXHcH-clNwieeoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb8fa557f.mp4?token=qDVxj8pWM1TMIaP0E351W3smMw8ad2p1oceiSyiSg7lTR8lzJugo5kxhGBRU1eIyQuqZZFiRaGGJDzFcLRJpHGfPbYyjdcWnm5n4M3i3IfHiSamQq7wuiXdoeWyNnCZ70cjpwreZp2BUJfWAjDao6RzOTEjAqGXXUsMBd9HNX83K2BvRpPuotgux6cIcghtYMq_WVkJtV0gLGP5m86pW8zBZS4VRS_w__9arqLo5HEj4Scl4GPRqxwF8ZB5DWip6uuDeCnnGphigSxLyBVqy4QJD-aTrOI-gbVRbopUq70-Q8gwKibnNIYkArY58N9-BzmI6lZRWNXHcH-clNwieeoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقامت بروجردی‌ها در خیابان به شب ۱۹۹ رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/462311" target="_blank">📅 22:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9927c80529.mp4?token=lSPpvTfyTjF4s8N6I9BmaB4TpPmuU9riAWBpZsqgJWfSeyi24XTs4QESf_GD6lwcSr2xt7WV1t4_Wk49ElxgRWwtASepOKEiB6vpYYj1gGzmrhQ0gAAbTwRiW94VxAAdx44gqmrwd3bJTLm7uOJWNUyIW5S-1Gzfs3OMD14Zw6d9_G_e9TBO26Y1M75h5sFmvV-lL3SdE_4y_q8dOMnuu3PLwEdbAbQJkhAvDDz6T6_b_83Qlnu1b6IoragzhHMmvTWVRv8DmkiDoU4vsjQzKaIzABMBJy-vo1qsNYb76qdfsCSnW5pHpyeD1LKz1PKRAvm-5Fe8u-LExncucQoGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9927c80529.mp4?token=lSPpvTfyTjF4s8N6I9BmaB4TpPmuU9riAWBpZsqgJWfSeyi24XTs4QESf_GD6lwcSr2xt7WV1t4_Wk49ElxgRWwtASepOKEiB6vpYYj1gGzmrhQ0gAAbTwRiW94VxAAdx44gqmrwd3bJTLm7uOJWNUyIW5S-1Gzfs3OMD14Zw6d9_G_e9TBO26Y1M75h5sFmvV-lL3SdE_4y_q8dOMnuu3PLwEdbAbQJkhAvDDz6T6_b_83Qlnu1b6IoragzhHMmvTWVRv8DmkiDoU4vsjQzKaIzABMBJy-vo1qsNYb76qdfsCSnW5pHpyeD1LKz1PKRAvm-5Fe8u-LExncucQoGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462310" target="_blank">📅 22:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462309">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673a007c26.mp4?token=oGptYQKgJDGRyH7g12HEyQ_cKMUYVbcgfnadl3ZLPRi6d7OzsDeR29VMg057ZdblgRHuvrh2V1pz3f5xs6R6DmTEhiIzJW-4rUlvELlTEIP0o4UIxAwgYFi7gfBxTMtx78sLnK13A_GHrRxgehP9RKL0wR_xEX9IA6oTwEmyTmPJAIQh8IsPzBxDiW180-gz62LLHFiVs7LBOCuaDRjNvM2kPzU_d8iCYg8tlAMu2GskyzVAoDydR1cpCzbWM4jtLp-bF9EWNZmIKhF6SK2YT5ILxNEXx38CpQje3JnT9Smaje01r4qST2jXHtP46S_KsRPMT7Dxe3x3WremyLakzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673a007c26.mp4?token=oGptYQKgJDGRyH7g12HEyQ_cKMUYVbcgfnadl3ZLPRi6d7OzsDeR29VMg057ZdblgRHuvrh2V1pz3f5xs6R6DmTEhiIzJW-4rUlvELlTEIP0o4UIxAwgYFi7gfBxTMtx78sLnK13A_GHrRxgehP9RKL0wR_xEX9IA6oTwEmyTmPJAIQh8IsPzBxDiW180-gz62LLHFiVs7LBOCuaDRjNvM2kPzU_d8iCYg8tlAMu2GskyzVAoDydR1cpCzbWM4jtLp-bF9EWNZmIKhF6SK2YT5ILxNEXx38CpQje3JnT9Smaje01r4qST2jXHtP46S_KsRPMT7Dxe3x3WremyLakzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امشب تهران به عطر حضرت عبدالعظیم(ع) نفس کشید
🔹
فردا سالروز ولادت حضرت عبدالعظیم(ع) راوی حدیث و مورخ برجستۀ شیعه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/462309" target="_blank">📅 22:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462308">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای
وام ودیعه مسکن
که نیاز ضروری هر مستأجر است، چرا باید دریافت وام به داشتن آشنا در بانک وابسته باشد؟ وقتی به بانک مراجعه می‌کنیم، می‌گویند اگر داخل بانک آشنا داشته باشید وام به شما تعلق می‌گیرد! این چه روالی است؟
🔹
ما در زیباشهر،
منطقه ۱۱ زاهدان
حدود یک سال است پیگیر
برق مجتمع
خود هستیم. اداره برق ابتدا اعلام کرد اگر فاصله شبکه بیش از ۵۰ متر باشد، هزینه ترانس و شبکه بر عهده مردم است. اکنون شبکه در فاصله کمتر از ۳۰ متری ساختمان اجرا شده اما همچنان همان مطالبه را مطرح می‌کنند. لطفا این موضوع را پیگیری و رسانه‌ای کنید.
🔹
از ساعت ۵ بعدازظهر به بعد،
دستفروشان در بازار و به‌ویژه خیابان ۱۵ خرداد تهران
آن‌قدر بساط پهن می‌کنند که
عبور و مرور مردم تقریباً غیرممکن می‌شود
. چندین بار با ۱۳۷ و ۱۱۰ تماس گرفته و موضوع را گزارش کرده‌ایم اما با وجود وعده پیگیری، مشکل همچنان ادامه دارد. مردم واقعاً ناراضی و کلافه شده‌اند.
🔹
چرا
وضعیت حجاب در کشور
به اینجا رسیده است؟ ما این همه شهید دادیم که امروز شاهد چنین وضعی در جامعه باشیم؟ انتظار می‌رود پوشش زنان متناسب با ارزش‌های اسلامی و فرهنگی جامعه باشد، نه اینکه هر روز شاهد گسترش پوشش‌های نامتعارف در خیابان‌ها باشیم. خواهش می‌کنیم مسئولان به این
دغدغه فرهنگی و اجتماعی مردم
توجه کنند.
🔹
بنده سال ۱۳۹۸ از
تعاونی مسکن کارکنان شهرداری شهر جدید مهستان کرج
امتیاز یک واحد آپارتمان ۸۵ متری خریداری کردم. اکنون
پس از گذشت هفت سال
بنده و خریداران امتیاز واحدها که حدود ۴۰۰ واحد هست،
بلاتکلیف هستیم
متاسفانه هیئت‌ مدیره‌ای هم وجود ندارد که به ما پاسخ دقیقی ارائه کند.
🔹
در بحث
سهمیه و افزایش قیمت بنزین
، موضوع
تاکسی‌های شهری
کمتر مورد توجه قرار گرفته است. برخی ون‌ها و تاکسی‌ها عملاً فعالیت مؤثری ندارند و به گفته شهروندان، سهمیه بنزین خود را می‌فروشند. خیابان جیحون نمونه‌ای از این وضعیت است؛ برخی خودروها سال‌ها جابه‌جا نمی‌شوند و با وجود گزارش‌های مردم نظارت کافی صورت نمی‌گیرد.
🔹
لطفاً در برنامه‌ها و گزارش‌ها بیشتر به
معضل ریختن زباله در طبیعت
و مناطق محل زندگی مردم بپردازید.
🔹
سال‌هاست مجتمع‌های آموزشی مدارس روستایی غیرفعال شده‌اند. با توجه به کمبود دانش‌آموز در هر پایه، بسیاری از کودکان روستایی یا مجبور به رفتن به شهر هستند یا در کلاس‌های چندپایه تحصیل می‌کنند که کیفیت آموزش را کاهش می‌دهد. درخواست داریم
مجتمع‌های آموزشی ابتدایی روستاها مجدداً راه‌اندازی شوند
تا دانش‌آموزان چند روستای اطراف در یک مجتمع، به‌صورت تک‌پایه و با معلم جداگانه تحصیل کنند.
🔹
مدتی است به‌عنوان
پیک موتوری اسنپ
فعالیت می‌کنم. امروز در محدوده حرم مطهر، طی دو ساعت سه درخواست «اسنپ‌بایک» از سوی
مسافران خانم
داشتم. راننده پیش از پذیرش امکان اطلاع از جنسیت مسافر را ندارد و با لغو سفر نیز حساب کاربری من به‌دلیل لغوها مدتی مسدود شد. خواهشمندم مسئولان و شرکت اسنپ این موضوع را بررسی کنند و با توجه به اینکه اطلاعات هویتی کاربران بر اساس کد ملی ثبت می‌شود، درباره امکان مدیریت یا حذف این سرویس برای مسافران خانم در محدوده حرم مطهر رضوی تصمیم‌گیری کنند.
🔹
لطفاً موضوع
پرداخت معوقات فروردین و اردیبهشت بازنشستگان
را به مسئولان یادآوری و پیگیری کنید. هرچند این مبالغ در این شش ماه ارزش خود را از دست داده‌اند اما هنوز خانواده‌هایی هستند که چشم‌انتظار دریافت همین معوقات هستند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/462308" target="_blank">📅 22:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جاده چالوس از ساعت ۲۲ دوطرفه می‌شود
🔹
رئیس پلیس راه راهور فراجا: محدودیت تردد در جاده چالوس از ساعت ۲۲:۰۰ امشب رفع می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/462307" target="_blank">📅 21:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQdOw6t25A4BcaYNIIGgPrI-tiTjeFhy591008zALjnKIwfe2-1xJWiW0YTNPHL22PZ3UMI8jeEuS7gBGkRoUPF6A9no7Cp7S4fBNjN9duV9LBNjEoyKHUIbyVynNaooLeisWRtSTcDrfGuFM-wcil_nO5J5L2Xb0az3qfk8SB9czCjMVdPKa7p4NAukMSVMdqhoSdxVDkR-xAME7AdYnka-3mXA-NlB9PAlyosWZpYphaqG8kT1qFLy0jKwzOxiSb_r_7Da9nfu9CdlOYxnLh77WvFkcasO37Aw_Y6_03rF8bUAHfPYSuL9RMENOnsCGzg2XiO4Ta5F79DBq7Xnrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5ZOlpL4RxA8EhGF8yz4eoT4DCENnnQLowKDx2_AbduxeI8ty2_a0tdvN3wlKK2cPHh8tvvrPDo5a4jn8V0s6MQj8BWRXZjVmDiPqcjpvYMsk7eqmOJjRkEm9I3TDbhtBgJ-nFQumE2qMBc0D-97dIg26vX3gB2ug5bbPAosyBRSCFIuwllkb56LJHbsGfxMES1l-vqgXKQl8NUAU2AAEhMXbXHVq21Bu2PBo5zX8HbuAy2A4wPcce1_bD285OOl02_W5ZOALgM2Uvadl3Htp2HpYXM6ffKOTTM5gXwPPvSB8JVHw7Q0ylAaUQc-Qp12aud34DJcH5z6s07o4B-8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmWtbgM0odkqUxGzA624_ksbbxu246vBT3nYs-MHLN_kGJFxceQIdc9J5g9iZ7UeaBFaRtv8hvzyPKTpjq4zfTeLI-S4Frh0qB2BfMQmsgT4bl4oXgSlRi-W8C_epIDyOGteFZ3IFSdFUFyLonY6IxMActEf-cN1CygoD19xD9O5iterYdF9i0jRy7pqdovydT41CUThhEbWr3B1bdEO0iOtqbegSoODqVhlUlvb60dkFVN0bXnNMuW0FY3Vzi733YwR_RxU8A2iOZReOBf623g5eCOrDYbeWrHu-5O9y4g9yOSPjbuJ9fmY8QsotjDZzuXV4NoJvhzLr2YDRHNbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km7necAJdVxYALkXQKzbhhIXiMj4jLOoxxScZRjPPnkOKir6QgK-mEvid6pRnUKsH4xW6JN0fl4p8epPBJpkUjrQeFmIOaske3CA91CmLupaKa7DfwuTxRlgIyTVCs-cL4Z3E4u50PKxiIQMPYyhwZQN_haiaRakayjBWlcAlycEIbVMRh_qxHmnavoO1jhjKzumPrIB0AVx1CkyHoR1kdSgopo9NkN6m9ZyAEgHcPtSKi0XcJ62o_07DjxY4lv60gdKoXlc1SZesHuNhYJAp-S_FVy1Mn3p77QlRRzXg8xHMjAg1mMtkZIp324dhgr6S_MvY9d8osg6fnkJhMeNUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE5y8h32EWqukRjtnzNwYt9G10nCKawb3tck8tQ6jPYaIFKO-w50rGF-k2f5t7yawqF9iWLge1gKhPTyWDnPgszZbsIfdZoTJypbcOaZ-ZoT9B8v52326_PqE8MyIp3rVhZP8wu5nQ992pHuxz7Rtx8xeP-w1oyaERI4f0oJTW4ICWrBtd9ie4EtJf0Kmd7pc8MGynF2BaTCQT1T9EEpVf4t03vpwNf8xWRUQMzyGzdAb6cT-eS-pL54NABTbGDyBLU5KknZ41HDNc58J1-MN11PFac9RQu1tYStySXonS55Y6oxBPvEdpm4xMipW__RtvAqxTgXAXgLRyoOgsfizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5lQjmuPv8aRg7PtgYFBHD_hWuOJNApedd9N_aoYhG22lhuxkLnhTezwLWFEnlTwNG7-o0P5LtR1Bo0rrmmle-FIYRNB3rejkjq-uFZXzGqR_0y7fwJG39SE7ga2dtTV66Bm6B3BvLHnZCHWemHO-qa5tUz2pkDvmdQaiQwqTBKQbf6rkhWvA-Xe4I3PJDs81vmHSNTkjTFwoSgBBoPyO4fmKOJb4HZHv6gGwADAlSdniAC-w3CMEn-hTUNYyGM8l76GCy9MofHwWVDHEsNE1zTqp7r_fNaftG-oBVC2I4iGra7C_ePKv940xkeBHRhzUUpe6pelzlKGxrGv_L-svQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWtuXuO1wApC4EvN9aWXf44ebvAQRQ2pS5FrdESXf1f-R6U_R4VUZFHRxuaMttP1pjeYztCMjpyxzNa7Y8-qC_TVZJ3--bb46u27cNWuytnx-p-XFhIyooFoBkfQEvdPUytn1lM4NngDOZCOGqkUgqFFWh54NfQas4YY5JtUxwVS_oicHzheyrZaYkyMMD1uqdYcHm-RaAp-07h2Yaf7a9XR_ZdURnJJDulpPnkfJbuS_qKC83AlgQx1f7n8ANi31_KN3M_yaQ4CZOldyDYhXADzmuicDb01QLpcs3PKGtkp2Q4C5AIOVvD9OqWYmsD3BpQhHpsQxnSNDG_6wkSBhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هفتمین نمایشگاه بین‌المللی خودرو تهران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462300" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e5ba6a3.mp4?token=KiUSuYzgw69RatUD4AAAf5bcYb_9eO-JUvrRdm3kTUlOC9sax3xVpLtZMFRrS-RJWztmeUcXBaJpxg86F6X523BNBAEd3IevRQfk6tL1LPizuiM-ZZ0QLQNi5Kp19JF1hZxyajN_QDMXg5dxpVJ2xn8QGsmA8ZeGmIdeKuVhlDzLqYWWEVBwpnw5Gep1nROYCMZnHDlD1SUL6AG5QSBFvTEpCVFodtdRF7TvyJIzF5vwU5JKE6w_Tkm3m6ghfzjpqOmcsfYrFCL4Xj34K03wdpxR-9n4cEzdDiEgCWugZcaqgIU86hPhbI-SXt3plDx0qgPRVNFNjw3X7kyD6dhrDQpwl-MMVLV1BlWRyA2TV_PBu6jEhoJ_xwxGxuUHb4G3cz1Ypc79st5pv33l0L15MVteE4uaP2FDqHDnIEJi93FGQqW4a5ytzm-I2R72_g5tW_vWQOC75_7XdxE6SdD0xSSDJhc5NAYHfzX9zJWs3ixIZI94dcnQbU64br31ODzpNhM6KsShOLpfqzdNbk6Kn9FiF9ZlMe8e9_ZHeUdglub1l-AWQdIstGZWKAKlR_ULBy1lJT3cQezjB9YA11Fs2HPdVXS5Q1U1r63AExxf13Rc7-RWLc0vgAsHE0czO1phhkrVU1XYbpSYwUAEtJOBq3A_XZ6TmyOA_3TPJ4cZNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e5ba6a3.mp4?token=KiUSuYzgw69RatUD4AAAf5bcYb_9eO-JUvrRdm3kTUlOC9sax3xVpLtZMFRrS-RJWztmeUcXBaJpxg86F6X523BNBAEd3IevRQfk6tL1LPizuiM-ZZ0QLQNi5Kp19JF1hZxyajN_QDMXg5dxpVJ2xn8QGsmA8ZeGmIdeKuVhlDzLqYWWEVBwpnw5Gep1nROYCMZnHDlD1SUL6AG5QSBFvTEpCVFodtdRF7TvyJIzF5vwU5JKE6w_Tkm3m6ghfzjpqOmcsfYrFCL4Xj34K03wdpxR-9n4cEzdDiEgCWugZcaqgIU86hPhbI-SXt3plDx0qgPRVNFNjw3X7kyD6dhrDQpwl-MMVLV1BlWRyA2TV_PBu6jEhoJ_xwxGxuUHb4G3cz1Ypc79st5pv33l0L15MVteE4uaP2FDqHDnIEJi93FGQqW4a5ytzm-I2R72_g5tW_vWQOC75_7XdxE6SdD0xSSDJhc5NAYHfzX9zJWs3ixIZI94dcnQbU64br31ODzpNhM6KsShOLpfqzdNbk6Kn9FiF9ZlMe8e9_ZHeUdglub1l-AWQdIstGZWKAKlR_ULBy1lJT3cQezjB9YA11Fs2HPdVXS5Q1U1r63AExxf13Rc7-RWLc0vgAsHE0czO1phhkrVU1XYbpSYwUAEtJOBq3A_XZ6TmyOA_3TPJ4cZNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع و تدفین دریانورد شهید جمشید رجبی در بندر امام خمینی(ره)
🔹
دریانورد جمشید رجبی درحملۀ چند روز پیش آمریکا به کشتی کانتینری در حوالی جزیرۀ قشم به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/462292" target="_blank">📅 21:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUcZ13ONuX0_t_Eb9THwP8IBrfjWmvkZ-7pOR0xSYQ1_5equJ8xXXEGVVXOqYlqC9QMiSMf7F8uTI0hvovYFZT1R3pAc9Ws-Nxi_py9-StjVULWaR6vGQe4X9iTwMt8yRojNj_LBSE6-8t6z_4q8oKa1iYONVmncKg0ACu9IVtBZdxI-ddHv6kfSAjnoTdR3NLI4d1XnuNkEIgMCXPWlY3eMrBM0ljxuLA9i7sp7ZpwuPdyRG_oK75EdyeqFYIVXE_yozdmnFde4SawDHn6lvb-s8ZlsMYOoiPHRh71pUlgP3ezjvdq62VeIVGZZBfZWJ2cO71-Qeuh-fH5DlcG7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهام‌های روایت آمریکا از عملیات نجات خلبان F-15E
🔹
خلبان F-15E آمریکایی در مصاحبه خود مدعی شده پس از اصابت موشک ایرانی، با چتری آسیب‌دیده و سرعتی تا حدود ۱۶۰ کیلومتر بر ساعت با زمین برخورد کرده و با وجود شکستگی کمر، بازو و شانه، خود را به ارتفاعات رسانده است.
🔹
امیرسرتیپ دوم خلبان عباس رمضانی، خلبان پیشکسوت نیروی هوایی ارتش، می‌گوید: این روایت از نظر فنی و پزشکی نیازمند مستندات بیشتری است؛ به‌ویژه درباره سرعت واقعی برخورد و میزان آسیب چتر.
🔹
افسر آمریکایی گفته برخورد تقریباً با سقوط آزاد و سرعت ۱۰۰ مایل بر ساعت رخ داده، ولی برخورد با زمین با چنین سرعتی، آن هم در شرایطی که گفته می‌شود چتر نجات پاره یا دچار نقص جدی بوده، موضوع ساده‌ای نیست و زنده ماندن پس از آن بسیار بعید به نظر می‌رسد.
🔹
رمضانی با اشاره به نحوه پوشش رسانه‌ای عملیات نجات، آن را فراتر از یک عملیات نظامی دانسته و می‌گوید به نظر می‌رسد آمریکا تلاش کرده از این حادثه یک روایت تبلیغاتی و روحیه‌بخش برای ارتش خود بسازد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462291" target="_blank">📅 21:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN53aM-4hQ8Rj6cRKDmmxEzGejI4KHA1Jx7IC-cvd79CIo8lrZfhORhDF6jMtbZ7uGt9oBFsgzVGtpi0lVUitrgT-xnGsybVP-4dggqfVVgJCikjRm0bZwYAtGS12EDvgDXunI0lyIEaSCGNgn9avNJS1FCsydi0Kxa3gz9ep5WztSydPSHTt8PnnmH_h9w_C3-06A3vKWLdBLaQz5zZo0A7eyjg1xUJwY_c8yzIQD8o030svp3TymNswZAD-t9RZOoT-bAeZBw2vzvLFa2gk8hyCggtGUD8-LCA_At7WRiTo5M6_b3uJ8TUcrBWMdhL78-FogmClm6xP_5MHy33EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر شهید مولوی یوسف گرگیچ فردا در زاهدان تشییع میشود
🔹
پیکر مطهر شهید یوسف گرگیچ فردا صبح از میدان امام حسین تا گلزار شهدای شهرستان زاهدان بر دستان مردم شهید پرور زاهدان تشییع میشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/462290" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
آغازی بر پایان حبس بدهکاران مهریه
🔹
مصوبات جدید مجلس برای تعیین سقف مهریه و حبس‌زدایی از قانون محکومیت‌های مالی را ببینید.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462289" target="_blank">📅 21:17 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
