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
<img src="https://cdn4.telesco.pe/file/s8k8TQdC7E1PGSvXDGszNjLKZulW6a2xpR0ZuMASembELxw1Wj6VXDNQXEguzdXDgGIQwZ1oG_AS-dkCnLsE4LSdP-Wvo3nz6s-LpYYlv2aIi7lljvK9S9vwsBFPe8ezsNxZlWNAHQTRa9DLhG-usJ6ukAtOxcIL5B0pTsvceC2VTgENuTFJUZ7ZaHhkZCJOAXw30UljmZ4A_iILcxLclvRa0_9-niUam54TF_an2Vpoj53UitWcR7CVU2HObrIQuAcpw3A2qmNDwmb-ApAp6S1xI5r4wNTHZZJ_DoGuezBwPDB5qarONtCb7P5PD_8JEUQcqJan6lkL_qpG1TOjIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-466358">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLQlOxve9NwAwX4adVpiW3-Rif8JVVR9Wx91hF_Fh9GnSuP_9JKB1CVpS8mFZsCI0RoiKu53U22IgBtTKWLxKP2QNyqqDd8XAsHpT9lOxW1X3gMZtDepM9BE3S-_a5r0j4plJzVOjRCSXzXDIySMhZ_-1cJ3Uw_HzsJGCX-ZY5inf1kiFdFAWsq8o_myQ1Hv6CmdXjwi61rjzEkaZEwtaR5w4JaGRIA6SAhq0O2BA1wKS-3bAdlNCY3xABqt3xD9CSR-msbva3o4PLIZC3jYwTX2HGTKSngkHKZZUpBTa1ubDM_ulkMyDU05O3HDvwhz2fm_qqgFyfFUlwCtcwiOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۷۹ مصدوم و ۴ فوتی بر اثر طوفان و سیلاب‌های اخیر کشور
🔹
سازمان اورژانس کشور: در پی حوادث جوی از ابتدا تا ۱۱ مهرماه، ۵۷۹ نفر مصدوم شدند که ۵۷۶ نفر از این تعداد در حوادث ناشی از طوفان، و سه نفر بر اثر صاعقه و رعدوبرق آسیب دیدند.
🔹
در این بازهٔ زمانی، ۴ نفر جان خود را از دست دادند که دو مورد به‌دلیل وقوع سیلاب و دو مورد در پی رعدوبرق بوده است؛ یک نفر نیز در حادثهٔ مرتبط با سیلاب مفقود شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 699 · <a href="https://t.me/farsna/466358" target="_blank">📅 05:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuUTgG09CGgjunk-6nUHFJpAE4IN0XMD_v9mvrRrCE9G5BR3N3HwPCeb4y0nQudckPYbcftoDRk9h1AJKWxMPiW9KpBSTfWn0vIn1YwxapwOd7ta4W6sOyY9eQP9ckEQq7_SMf43xpHBX5cC3sFCkxivdMKw4h6T3mbaX8Cl3emrd1KGZv1FvQvUI-aql0Vwe80951o_j-MjoBUW7M5WRXFcJyw1HYEAAvfhHnJ8fDZ-OBARK_XubLAkmqdXoppK7bAFLAPBMMJPzvxC071PUFS04SGhYCDADz3pAQ49FPLY7WRVyFMMD7ANLTalg_K0B29FxEBKZGxqFEUe5KIQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ مشهد: شهرداری‌ها به طرح «تورم صفر» بپيوندند
🔹
حسنعلی اخلاقی امیری: همهٔ شهرها به‌ویژه کلان‌شهرها باید با ایجاد چرخهٔ صحیح توزیع و حذف واسطه‌های غیرضروری، به کاهش فشار تورمی بر مردم کمک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/farsna/466357" target="_blank">📅 04:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znuk3gFFNwgnhVTZO57fBtLfNVYgGKaWJ_YPqeU_-uCMvN6TCZOeVygf8I5ihEcGo4q2pCzLMJQNrH1ZPagborn_oyatFHUJDET3hbj2bAAIKsc6CoyHQUcCaeMamX_Dz4fwvxhW3KVUBSVDyVrcwfuCdL7-pbBrCGLV7VDAIJF-_6JHlaC1yBBQ7LlreI2m4Z7GwbxWFNXP79QReVtjTu21drt3XXYZjhhpt7H_9V8QHqlux_aOR7m6HI5wXSyiiP91I8Li8VjMFts9u0OYmYPGKFioHqaFc9pTTrb6Dyh6rfgOz6W3ztqHLjTfwzfebfp4nWJnrx3bP23pMz1KKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعیین رئیس‌جمهور برزیل به دور دوم کشیده شد
🔹
انتخابات ریاست‌جمهوری برزیل پس از آن‌که هیچ‌یک از نامزدها نتوانست بیش از ۵۰ درصد آرای معتبر را به‌دست آورد، به دور دوم کشیده شد و «لوئیز ایناسیو لولا داسیلوا»، رئیس‌جمهور کنونی، و «فلاویو بولسونارو»، سناتور و پسر رئیس‌جمهور پیشین برزیل، برای رقابت نهایی راهی دور دوم شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/466356" target="_blank">📅 04:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTzu5gG-TL3glUOYzdEuMa6AsMEF9uHX67ZYratG-upLP7-NL9uoA6ycbkB_8LrryAXifpncvTj78M32enVSbXYvSVSpjnbiknjbiBLvOU8_5mSRZlvTCOazhckTTgiMt13FdpPskPHfnGelKlSDLsuL4e9IfsoaCE38yME7pxnh_Y2d12yHK8Gcdc50qH03zdD-onMucMOUglKglkPK6s7roXWi0MmIrJFIDMhtFzY7LU-_VGS62GhIlnIiK9I3oEcRhrD7g-OXL4xuY4ye3augyryI3aSQyHN_rxASa7-xd2v1kI7loqUo3ZqiY6XTPQD7vfHa63BUMoJgMIxb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل با خبرنگاران جعلی برخورد می‌کند
🔹
گوگل دستورالعمل‌های ارزیابی کیفیت محتوا را به‌روزرسانی کرده و ساخت هویت جعلی برای نویسندگان، ازجمله استفاده از نام، سوابق حرفه‌ای و تصاویر تولیدشده با هوش مصنوعی، را مصداق فریب دانسته است.
🔹
براساس این دستورالعمل، سایت‌هایی که با جعل هویت نویسندگان وانمود می‌کنند مطالبشان را متخصصان واقعی نوشته‌اند، ممکن است اعتبار و رتبهٔ خود را در نتایج جست‌وجوی گوگل از دست بدهند.
🔹
این تصمیم در پی گسترش رسانه‌هایی اتخاذ شده که با تولید انبوه محتوای هوش مصنوعی و ساخت خبرنگاران غیرواقعی، به‌دنبال جذب بازدیدکننده هستند.
🔹
گوگل تأکید دارد مسئله، استفاده از هوش مصنوعی نیست، بلکه جعل هویت انسانی برای فریب مخاطبان و القای اعتبار کاذب به محتواست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farsna/466355" target="_blank">📅 04:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">منابع عربی از توقف پروازها در دو فرودگاه ریاض و جدهٔ عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/farsna/466354" target="_blank">📅 03:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf7r1zXnRDf6EJm7kD4ee8ojBM8rgIHi3UV9vV7PX8JXXuog36qHbiA9vNnkncU2ja7LkEAHYsc-nocjqx3L3AQgkehcbl-v-xco8W9wQkVJHNmpv2lJE0v2GyuesOTJWdmDFUBYZdMPH8E0uclPnTmUYjoUV2LnQetzg7S10pc6ilhDwFWJKQt9DSR-bxHJJ4eEkeJ_hYExgXedic2-woAGFhecNw0u2aQ0m3uEsxJpanpvxBwag5g5fkVXYvGJ50JNgDb9WWfraoBZLUyF7iY8yG8K5cU1NzsVqx29l-x-EOL-18158vYhhKomDdFtDQurV99TQZIf-Ez4M72JPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش آمریکا برای تشکیل ائتلاف سعودی-اماراتی علیه یمن
🔹
گاردین: کاخ سفید از عربستان و امارات خواسته اختلافات خود را کنار بگذارند و برای مقابله با نیروهای مسلح یمن، فرماندهی نظامی مشترک تشکیل دهند.
🔹
همچنین نتانیاهو در ابوظبی، پیشنهاد کمک به عربستان را به نمایندگان…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farsna/466353" target="_blank">📅 03:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52295b88bf.mp4?token=SxlotsjqCAtQu-N25FtSYnpMfsk2AWEPDWBbZxQfk4bvaUs5n2PvrI7qPwvTVHUoZoK3IIT9Q_UijWRm57PtDhcEjPii6uwkfmsN0Hfx4DzSl3aDCQcuqIQTPRZ_zpB0UUxiQGFtR1O-fhnjuP-wbERTKxNoKRqUwODhat4ym5CaTzAsHGRCgLCJCrXIJYmhHkpbjEy7_qJKxVoR4lv4zNQ2Nap0uZ0cNNc8RHyOD5K6uvklmYNSo_vlLoZmxlGHfMh6hsGrl-urFa_ECoTrOutiRpO7pGGq9toH4IO89kudQNwLQmBH67rr2YNiScXcFe5rabp9bVZbG__ct6M1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52295b88bf.mp4?token=SxlotsjqCAtQu-N25FtSYnpMfsk2AWEPDWBbZxQfk4bvaUs5n2PvrI7qPwvTVHUoZoK3IIT9Q_UijWRm57PtDhcEjPii6uwkfmsN0Hfx4DzSl3aDCQcuqIQTPRZ_zpB0UUxiQGFtR1O-fhnjuP-wbERTKxNoKRqUwODhat4ym5CaTzAsHGRCgLCJCrXIJYmhHkpbjEy7_qJKxVoR4lv4zNQ2Nap0uZ0cNNc8RHyOD5K6uvklmYNSo_vlLoZmxlGHfMh6hsGrl-urFa_ECoTrOutiRpO7pGGq9toH4IO89kudQNwLQmBH67rr2YNiScXcFe5rabp9bVZbG__ct6M1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جسم نماز را خالی از روح نکنید
🎙
رهبر شهید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/466352" target="_blank">📅 03:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/466351" target="_blank">📅 02:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT9yUaI3JkGdw7YOk8okP11InikiiRFR3tyoMwZEtkXOqZvRDc4gjTfwwmtfDzGNLwHMb-DhK-W9HBOeU4gzm4c3WnRnZS9h19cZpnZ0Ywg5Wb80hKfZqul6XqYWiUArmCYf_mgHIow7faGFCi03LvpNIrMtOKBvek_HAZ2BuE_L5lwc5uUM01ZQ9NlotsceorPMSUhJRaNRsebvp__sAeppnFFQ0SUhn1h_VNC7825RiozIJudDHa-FNccmujtHeWSmx7uen4YB5s7ZJ-bXfgBcDzxbYTf5og88-0PVc4ERdyy9nlqwX4hy3phCDBVPG1hQ7ieoJfCbuP3hYkGq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر تیم‌های دوم برای استقلال و پرسپولیس
🔹
طبق قوانین جدید کنفدراسیون فوتبال آسیا، باشگاه‌هایی که دو تیم دارند مجاز به حضور در برخی از مسابقات (مانند جام حذفی) نیستند و در صورتی که چنین اقدامی انجام دهند دیگر حتی حق حضور در رقابت‌های لیگ نخبگان و لیگ قهرمانان سطح دو آسیا را نخواهند داشت.
🔹
به‌عبارت‌دیگر باشگاه استقلال که استقلال ب سیستان را به‌عنوان تیم دوم در اختیار دارد اگر بخواهد همراه با این تیم در جام حذفی شرکت کند اجازهٔ حضور در آسیا را پیدا نخواهد کرد مگر اینکه باشگاه استقلال مانع حضور تیم استقلال ب سیستان در جام حذفی شود.
🔹
تیم پرسپولیس هم که به‌دنبال خرید تیم دوم از یکی از باشگاه‌های لیگ‌هایی پایین‌تر است همین شرایط برایش پیش خواهد آمد. مگر اینکه تیم دوم خریداری شده برای باشگاه‌ها در سراسر آسیا اساسنامه‌های جداگانه‌ای داشته، و کلاً از تیم اول مجزا باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/farsna/466350" target="_blank">📅 02:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9UPDABRlsYt22sWrpT_U4P364hBJqY15-KFoJi4eh6-l58pN0KiX2bm0kzEvZ0fPVlKt8Bz7KcTpNtj03usDjgwAakG1faXI71VsgwTkHgEiKihsW0mvVLdUaB2qSweTDRRHl6GoXERuOyzvFX0q396AB7VqqeggShapUVZsAMEimg-W4GBflvSSmJpI-O7Kt8TifsAK4hz9xFo35voCoohU6P8YD-Fh8SkLuufCrh5Oze1yWW1HOqVIDi3PUS6QBNe6cNZQHTlweDyKW_nEPZOQqsuLrwcbEK9axSEy8y3MKdF_RzA5bJ6te8a8C1SdWzCzeuSXcaf8wDqfoxdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سیاه اقتصاد آمریکا پنهان زیر سایهٔ افزایش دلار در ایران
🔹
اگرچه اخبار نرخ دلار در ایران، فرصت پرداخت به وضعیت اقتصاد در آمریکا پس از شوک نفتی تنگهٔ هرمز را کاسته اما افزایش تورم و نرخ بهره اتفاقی است که فضای رسانه‌های غربی مستقل را به خود اختصاص داده است.
🔹
دولت آمریکا در تنگنای تازه‌ای گرفتار شده و برای آنکه اوراق قرضههٔ آمریکایی خریدار پیدا کند، باید بازده پرداختی اوراق ۱۰ ساله را به بالای ۵.۲ درصد برساند؛ رقمی که بی‌سابقه‌ترین سطح از زمان بحران مالی سال ۲۰۰۸ تاکنون است.
🔹
بازده ۵.۲ درصدی، بازار اوراق را به رقیبی جدی برای بازار سهام تبدیل کرده است؛ سرمایه‌گذاری که تا دیروز بازار جذابی جز بورس نداشت، اکنون در اوراق قرضه پناهگاه کم‌ریسک‌تری می‌بیند.
🔹
نتیجهٔ این جابه‌جایی، خود را در سقوط سهام نشان داده است به نحوی که در یک ماه اخیر، ۷۰ درصد شرکت‌های شاخص بورس آمریکا، افت قیمت را تجربه کرده‌اند.
🔹
تحلیل‌گران معتقدند تثبیت این نرخ ظرف چند هفته منجر به ریزش گستردهٔ بازار بورس خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/466349" target="_blank">📅 02:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466346">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگالری عکس ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcaj59MT8mkipPtnJFaaARwDJM_us8o0mG2T_HtjrhIz1iwvQK9_sZGhpTlBoz1NFVI45N3EWrUnPxAaGOb8Gjph-iA3ogbUeIczmfis06pvPDvs4pdAF23l0Zd6mkn7uEg5IYY_fL6lrBoBl92vff_k5x8HMm3rbKpdtZqH2yJft4Ry5yg8N1kz5-iltus3dCHsFLV00PKYuIrq82hQT2g4KOwiV_A2rilHfZ50LAKnF8rYPiWXK95sRGN9mFbI0BjUO1wnRjd9a6HtsjuuObnSwPkS8yF-jO7PshBoaG_AaHNybEE9kXGsjdAKBf2zsw985XLKnUKdeNqjAtoH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A90CBN4e564a0dZECHBlT72yrEsmxZY6mOaHnY7zRFT5ve7ZbCNUOTP2VeDXrCOpY59Tw6kaQPvtLyrSIh2kP6M5hdOhp6Ccp1Vgpn39l3KXfB11j61rpGVCHSGuszwd2ah0rNqdMw9KxfWxLudVVltMVa8CGiYY-gnFNTFZpk9DO03Frdh4Wv0X7D9tvSrOBiISH94jpDaKTewQWAhp30H5GX1U8EaPzX_88T5VgCTdn3Uy5sPqrmo_G3Ouog07a5kBKOZcKenT-CXRrOTk9FcBDmc7j-Owyq1UnW9WqLFoq3c69tlXXfiUSRALzIpUlNvunAZLeJ4ePdn51pUXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGO_EZQNEnnBkJAcP0sUTFjccIuh3H3PLwjmNmZ9GEiGECdcfVY-Ka771iSF6d0AFIxhoW48dqSVVK653P1zKOWc8rNqOSAM00P9tdZDMSkuxTUFNjFP7ugf_rd5c4Xa4sYSFYef4iwccbq22RiJAjhD6q3FiC2aVSyJiaQd4gYWiwKVCyipWp-fkiSX4gtq7LxyS0yfr0B3LJlhIhtreyZKM7N4DiX8O9N4vuCEc8qiLucRCtbPm5tgJ2RznG6paBge22_63lCwGSircgvyfw8IvnTn3Uf2DnEIvOjV_U2CiSL69jSBBgp3aiJh9t3IP0s5-SP4C3nIEI0SPlXVuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ماه و خواجو
عکس: محمد سلطانی
@GalleryAksIran</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/466346" target="_blank">📅 02:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466345">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای شبکهٔ اسرائیلی: کمک‌خلبان فلای‌دبی قصد داشت آن را به فرودگاه بن‌گوریون بکوبد
🔹
کانال ۱۲ تلویزیون اسرائیل مدعی شد کمک‌خلبان قصد داشته ابتدا هواپیما را به‌صورت عادی به سمت اسرائیل هدایت کند و برای فرود به فرودگاه بن‌گوریون نزدیک شود.
🔹
او برنامه داشته در آخرین لحظه، زمانی که امکان رهگیری هواپیما وجود نداشته باشد، مسیر آن را تغییر داده و هواپیما را به ساختمان ترمینال فرودگاه بکوبد.
🔹
این شبکهٔ صهیونیستی جزئیات بیشتری دربارهٔ هویت، انگیزه و نحوهٔ اقدام کمک‌خلبان ارائه نکرده و این ادعاها را از منابع ناشناس نقل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/466345" target="_blank">📅 01:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466344">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اعتراض ایران به نروژ درباره فعالیت‌های غیرمجاز استارلینک
🔹
مدیرکل صلح و امنیت بین‌المللی وزارت خارجه، سفیر نروژ در تهران را احضار و به استمرار بی‌عملی این کشور در قبال فعالیت‌های غیرمجاز استارلینک در ایران اعتراض کرد.
🔹
او در این دیدار با اشاره سوءاستفاده آمریکا و رژیم صهیونیستی از اینترنت ماهواره‌ای استارلینک برای اقدامات مداخله‌جویانه علیه ایران، تأکید کرد نروژ به‌عنوان کشور ثبت‌کننده شبکهٔ استارلینک در اتحادیهٔ بین‌المللی مخابرات، موظف به جلوگیری از ارسال‌های غیرمجاز این سامانه در قلمرو ایران است.
🔹
او با انتقاد از بی‌نتیجه‌ماندن پیگیری‌های مکرر ایران، خواستار اقدام فوری و مؤثر دولت نروژ برای توقف فعالیت‌های ناقض حاکمیت و امنیت ملی ایران شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/466344" target="_blank">📅 01:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466343">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7e3aed45.mp4?token=pQsz22mrASM9463csyL5y6cyMo0rOqKemWIBsEJqywd_5eKuR8uvHecznG7qw--JtNqlKRXl-zRuW-BeBZwxtbvaTfqSZuUinslK09Y3ueNP1fHj6qlsaYqKtl0BYaMK9XCsUHFsi4DWc-NOoX6SKd1qnA35HrfqJHDejHWK6wUlhSeKYs-0zZywWxJ8nLwOQTd-4NxPTN0MKB3Xm9JJWmjPgQ6FaW1blkT-ExVtzV7D1Vfi3C4Jy9_0vrhlEfkogj1n7hh7YSQmP7iVsfbIxUSVqTJiEKxPytXHnEN-8P2onVz3wRs6MMvG4APUnFw7i3typpDdzKiXoiw3f6WduIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7e3aed45.mp4?token=pQsz22mrASM9463csyL5y6cyMo0rOqKemWIBsEJqywd_5eKuR8uvHecznG7qw--JtNqlKRXl-zRuW-BeBZwxtbvaTfqSZuUinslK09Y3ueNP1fHj6qlsaYqKtl0BYaMK9XCsUHFsi4DWc-NOoX6SKd1qnA35HrfqJHDejHWK6wUlhSeKYs-0zZywWxJ8nLwOQTd-4NxPTN0MKB3Xm9JJWmjPgQ6FaW1blkT-ExVtzV7D1Vfi3C4Jy9_0vrhlEfkogj1n7hh7YSQmP7iVsfbIxUSVqTJiEKxPytXHnEN-8P2onVz3wRs6MMvG4APUnFw7i3typpDdzKiXoiw3f6WduIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدارس فرانسه به دلایل امنیتی تعطیل شد
به دنبال اعتراضات دانش‌آموزان دبیرستانی در فرانسه شمار زیادی از مدارس این کشور که در کانون بحران قرار دارند تعطیل شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/466343" target="_blank">📅 01:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت آخر</div>
</div>
<a href="https://t.me/farsna/466342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۶ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/466342" target="_blank">📅 00:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3skRVBLMvYc6HCI7_0441W_mABGbHQ0jPB6Lu_eCYXhsgRlVSGnSjMGYySPSFgtCL7P0CZMHFL83vlpGY1sDP1jU6ZWHgcPOWyob049s4pVUX_XWUtVqAGVLDHNWVRKU6TNnJAJ3oA8dAAKvqk5n-9piiBF2LaBKglFJzbSHeJpJtQZNlzIZpuq3KF98skwJBsVK801SxGgcRTPBWHDl9vAPCXhU3xIH68YjvN6zp9OMGDVBkRTTHDHOSycAivUVVXYBgCgyA6Z_UzkH8_slyaRy7ct5_TYRaF4g0dD1KNx3Puh0QIv2K599PZ0dDak3oJlnXW6yIAgd03_MEL84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت رفاقت با فریبکاران
🔹
کلاغ، گرگ و شغالی در بیشه‌ای همراه شیری زندگی می‌کردند و روزگارشان از پس‌ماندهٔ شکار او می‌گذشت.
🔹
روزی شتری که از کاروانی جا مانده بود، برای علف‌چرانی به آن بیشه آمد. شتر چون با شیر روبه‌رو شد، کرنش کرد و شیر نیز به او امان داد و گفت می‌تواند در پناهش آسوده زندگی کند.
🔹
چندی بعد، شیر در نبرد با فیلی به سختی زخمی شد، در غار افتاد و توان شکار را از دست داد. حیواناتِ دوره‌اش نیز از گرسنگی درمانده شدند. کلاغ که درپی چاره بود، به یارانش پیشنهاد داد کاری کنند تا شیر شتر را بخورد.
🔹
شغال گفت: «شیر به او امان داده و پیمان‌شکنی زشت است.» کلاغ پاسخ داد: «چاره‌اش با من؛ حیله‌ای می‌سازم که شتر خودش به استقبال قربانی‌شدن برود.»
🔹
کلاغ نزد شیر رفت و با چرب‌زبانی او را راضی کرد و قول داد کار را چنان پیش ببرد که نیازی به شکستن پیمان نباشد.
🔹
سپس سراغ گرگ، شغال و شتر رفت و گفت: «جان سلطان در خطر است؛ بیایید وفاداری نشان دهیم و خود را پیشکش کنیم. شیر از گوشت ما نمی‌خورد، ولی رسم خدمت ادا می‌شود.»
🔹
همگی نزد شیر رفتند. نخست کلاغ پیش‌‌قدم شد و خود را پیشکش کرد، اما گرگ و شغال فریاد زدند: «تو جثه‌ای نداری و گوشتت بدمزه است!» سپس شغال داوطلب شد و دیگران گوشت او را بدبو خواندند. نوبت به گرگ رسید و آن‌ها گوشتش را زیان‌آور دانستند.
🔹
شترِ ساده‌دل که این صحنه‌سازی را دید، با خود پنداشت اگر او هم پیشنهاد دهد، همراهان به رسم پیشین عذری می‌آورند و امان شیر پایدار می‌ماند. پس پیش آمد و گفت: «تنم فدای سلطان؛ گوشتم پاکیزه است و همگان را سیر می‌کند.» سخنش تمام نشده بود که هر سه حیوان یک‌صدا گفتند: «راست می‌گوید!» و بی‌درنگ بر سرش ریختند و او را طعمۀ خود کردند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/466341" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466340">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFLuBI8fqZCW1pRwwmjAOlkaRdD7IVNByWsSwj9kQ2zEQzUHGEytvKjaOX7XRCpXhW9cWIWYKk7OrlurGdJ2F7M6YAaSvdJbVv_S6osqQogbBpVIYg0AyYwWAp6FslKUveYdHklswZ-OVPF0XBrQJj1C8L94I_5HBmnJ9XEeEFF8R0Ka07tPkscqwl-kkVTm6WgpiuoCrMvygsCnN7hkmDzY1vvvPzaMqAktROEwvxrQnsf-7ldvlBvQzxrTSLxAd_EKZ0ApgewSu4gaSAGHaaE-PEUZG-uqNejNsEw1m60mSOmBjz-e1YDy-n11QUcyKBC_mvBNFF59oZF2AcvYsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/466340" target="_blank">📅 00:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466335">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6ZQf2eMUgoJW1PT7Pe6tsNT9OtjH0KWVrzdGUN0ojk3mmgMXoN_-ga35uHRA9TlRh2bVFRKg5HACttlaVwzsvTsDy25__8HoQio8cKTfQiIdYchQztrVcCmzrAyuxPPfZ5xvU6Ska99ELgn7ghiZy-wiUQBoV_skUX0PWIRk0H0HVU-ycDmkTFoCIEFHKAcANjSqYBDGdC3G-zJ8fcWgldc74cNmW_BDNjRdlv7baXOQV9Cg_Meftv_EWYtemfjqnRZ2zVJ5TUZYt-621gOTHr_Mr5B-nlO_1xywz4cUUcuqvv0UTXuJp404z05PwiofcGIsHp-HZ8I6pPQzJhvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-OLlsX4iROs0jQ0dcfDm9nabkS4gtksNHwJveoJAlxo4fTmeMfac4BC2fsiC0G9JwfwFDI6uWZV3-MU8GEc5_CDo6pXVK0xflNb3dMk3IehPwUOk9RJw8hqK1YL2xeIJs_iZd2l4u-R65iW4EgcWpVxekmIlJQYJSIjzfUWRYuKR-8Ubv4QnazfQswXjf416Wbxf4VKVmRgz6rbY45H2SdHDIxBeVc66hn3nvcDp18OIBmREnxr3kB3MwBn_xUazS6huKR7msBpcM-yJfvhnxCS99-mWGmHweT6raDUAlTWFkZG_qaWTP-6f-Osi3_5FW4APy19-eOkUxDt0RhoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoglK_Lki2w2CeDoc5JRkVJ_Crf8k30S9i_jomLrWXIy1pmMBg48Tk1z-vfrNQiVWouB4WO8KkDVS4464vDitqY7N9Xp0IR8PMQl029x4B6q0QFsA1MDItH_FUPhDDfRWO_j9SXQbC5a19jW6Wkyf3GZcV_OL8bEDSawjtgssuXbIdwvupkS4B16nrgqKj91_V6ZVMndXpiLhIEbaRxf27Z2vGFbKdKCSkz3XUEfSZKuzHMNS97cCS8AUngbOrSpPBmE424mj0ydrnOt-YuMABqaOoFl9sOpL887a2zwqMksXP-XVGno4gCuB1dCaap4PwnATKW15C1t05L81NEriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHDN9q-G8b4-hnSncsR4NF7cojEB_D7uaX8O0JPOQYqSs7dKgTznwBM8WuXn1JjjwMP_Q2y97L6Cv42qmoLDKarX7-l8pSmozlUK_VdNG0QEllf2gluQo11Nmq6p7DgdrryhGgz1S9jF-88aKW2KPzVYYbRvH1lXLU6Xx-ybJG0PfnyCuDkk1M-tkim4Sgs2DM5VNt24ywB4NZDkbHQF7ARVqf-38cd87CVwdv12BomtqH3XboATWljhIMtQuPrsGtj30HkY2BCCEwM06k-etLFVh-omSZYp6imcVQvWuTxzcV05zv1uSgnSL7_kBzwnqN-4OXico77_RjsYEjdDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOP7516v2iHh2A__JrRToI8NnLC8ckvhELZ-NK0MEAJRbgZ4kX-ajKPOnxHXVD4SMtkIWbCMGN25jeysl41MH666zZeMuLRP6349As88HFWTErIOZcIU7b0GyBSaW2JAIdqDCL_p0nyKLMrfony79YzViUYlKkQA1t2KOTn0su8zIl_SUOu3qmC_RpNeU12YD-QBf6ahOLr_bmDiqZLAh77h9v9aZHm14KLF3P-BFzQRpOFlE59sAoOH7y1Z3UGUOStt5jS37Hc-Gkeljne50ngHNficxU0z77LvonRgZBQ-P7ZNDP7HVZucqFrQ5uc_sQLz85zTjrjo8h7ghet9JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادوارهٔ شهدای عملیات رمضان در اهواز
عکس :
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/466335" target="_blank">📅 23:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466334">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79723a5117.mp4?token=vGmmLrwEJmOOkPbJMt_RUmlLpRRkckkL-NiOsMhSzR6M_Ndh3czsPrb9EBMMPFVv0xd4omdnYODPcwuJkh6LBf1bANccY7xG3f8njFHJzFJCg8FLSTTFL0ckV3uvHi0zjGcOZSNUp64vugmUtpB8Fk6MOFFx_j80w-v7rwzs1ZB-l1ZBePY2fY-8HQyn0ReCYhzmT1p1UsicAJYwK8BU_VTnAtNfSDk9I2MJ6diwt1pnDC1JfhxxGcw724xSUx4WY3DFfZRk2ZoJ5-qDhkCF7xVqe-n3AlRA5LmOlhENBXLAEp3TMxsU-n9hiq8mjun0QZoFzOeLv9l639d_g63SGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79723a5117.mp4?token=vGmmLrwEJmOOkPbJMt_RUmlLpRRkckkL-NiOsMhSzR6M_Ndh3czsPrb9EBMMPFVv0xd4omdnYODPcwuJkh6LBf1bANccY7xG3f8njFHJzFJCg8FLSTTFL0ckV3uvHi0zjGcOZSNUp64vugmUtpB8Fk6MOFFx_j80w-v7rwzs1ZB-l1ZBePY2fY-8HQyn0ReCYhzmT1p1UsicAJYwK8BU_VTnAtNfSDk9I2MJ6diwt1pnDC1JfhxxGcw724xSUx4WY3DFfZRk2ZoJ5-qDhkCF7xVqe-n3AlRA5LmOlhENBXLAEp3TMxsU-n9hiq8mjun0QZoFzOeLv9l639d_g63SGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال مردم شهر آسترخان روسیه از اجرای گروه موسیقی سنتی ایرانی
🔹
هفتهٔ فرهنگی ایران در روسیه بعد از سن‌پترزبورگ، مسکو و کازان به جنوب روسیه رفته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/466334" target="_blank">📅 23:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
آقاسیدعلی مارو ببخش...
🔹
صحبت‌های تکان‌دهندهٔ یک جوان در رواق دارالذکر در کنار مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/466332" target="_blank">📅 23:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bf0750c6.mp4?token=hwIulhWYaxxej5TEcNLtd-BsOql4O7HpdrsvV13bMVynQCxgxY2hiCT-oVrjWmA7BagJLCudeif4SkKLLLNwAo1Xpw7MHer6Y8e4yo6c4cledkI5jLQXIGqLTJoIQk4XCbbz73Octy_KhdWoy4XnIeZWwiO59gp_Eq3UPGuOdX1UKpvJveFUISVJElnbbTPcGfbrAqvD89H02oUSGc3YSObrPUGGvfkjYjGpf4K4ydLCsmn4LTofLHrpy-6FhpsK7k7O7_6X72sVvZE5Xx5Vf2s5aO32UiGmScKybh-U62RiV9mOibAtDUeKHdwsVAx3PIwp_TBWGuXI7CEEpQLSxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bf0750c6.mp4?token=hwIulhWYaxxej5TEcNLtd-BsOql4O7HpdrsvV13bMVynQCxgxY2hiCT-oVrjWmA7BagJLCudeif4SkKLLLNwAo1Xpw7MHer6Y8e4yo6c4cledkI5jLQXIGqLTJoIQk4XCbbz73Octy_KhdWoy4XnIeZWwiO59gp_Eq3UPGuOdX1UKpvJveFUISVJElnbbTPcGfbrAqvD89H02oUSGc3YSObrPUGGvfkjYjGpf4K4ydLCsmn4LTofLHrpy-6FhpsK7k7O7_6X72sVvZE5Xx5Vf2s5aO32UiGmScKybh-U62RiV9mOibAtDUeKHdwsVAx3PIwp_TBWGuXI7CEEpQLSxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها یک صدا برای ایران خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/466331" target="_blank">📅 23:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9f90a9a7.mp4?token=IOfVpVnZPPZ8NMOAi_J0Od0khCJ66EDTMoVzr5-lhCF7ZzpV7hhDbmxeVCURaz91gnAnyQ90CHauRq0mxKNltYrPrmrWmW0WRrLRKJjeq5t_qHWfvloElqpQ5pb5lFQmDsdwzvPxfTjkT7v9OR9cJilk10ys6p84iTT69CznCf13XG4OYnh5UuUIwY9FwrjEh50J6kek0FfEnyDB-hSpnDvVHxlewtLkwdTB3tI-ieBXsS9OpMUHldCZ5HtGXWlPgBE8AlPtgds3ZHkRN64WWNo8kdrPikPg2rraHW-t-uDRw_DdJ5rnAUjJS0P1E3hO-WD2yvFFXZl-XrAxOFQI8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9f90a9a7.mp4?token=IOfVpVnZPPZ8NMOAi_J0Od0khCJ66EDTMoVzr5-lhCF7ZzpV7hhDbmxeVCURaz91gnAnyQ90CHauRq0mxKNltYrPrmrWmW0WRrLRKJjeq5t_qHWfvloElqpQ5pb5lFQmDsdwzvPxfTjkT7v9OR9cJilk10ys6p84iTT69CznCf13XG4OYnh5UuUIwY9FwrjEh50J6kek0FfEnyDB-hSpnDvVHxlewtLkwdTB3tI-ieBXsS9OpMUHldCZ5HtGXWlPgBE8AlPtgds3ZHkRN64WWNo8kdrPikPg2rraHW-t-uDRw_DdJ5rnAUjJS0P1E3hO-WD2yvFFXZl-XrAxOFQI8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: آمریکایی‌ها می‌فهمند که هیچ منفعتی نمی‌برند و باید هزینه‌های زیادی بپردازند
🔹
آمریکایی‌ها در منطقه که آمدند، تمام خباثت‌هایی که داشتند و تمام اهدافشان، ما بودیم و در تمام مقدماتشان شکست خوردند. مگر در افغانستان و عراق و قصهٔ داعش پیروز شدند؟ در همه‌جا شکست خوردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/466330" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044e50cd6f.mp4?token=a1WlmgJJIMUvgfNDWRIR-oa9sOtdjcYWDa-qh2hXPWVyzLsq2hHKoySiCgjEUtiBQUXvstTop8fJigKhnF85LTKC1OWwiQYmNPfYcvDHJGaCZGO6Si2oHpPGWOUkwZvqBji6mjvoJVOT-kdSmc9VcvKDzKt3gHdRs_BGU6zntpqz_DggOEHGXGeVmJD-n2GTseg3LqaoJXfL3vPkVfKDAlMWvHf5Z9wLDoP7HrE_gMSnmv6755iCT0qeswgxl38DABBNmGpcopwx4-5ePnu7yPDzuT96DfEEi9lcilYg32Uk_A_IOiK_UmNeygFekulPZHYBBQUx7yIReqin2ZWAUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044e50cd6f.mp4?token=a1WlmgJJIMUvgfNDWRIR-oa9sOtdjcYWDa-qh2hXPWVyzLsq2hHKoySiCgjEUtiBQUXvstTop8fJigKhnF85LTKC1OWwiQYmNPfYcvDHJGaCZGO6Si2oHpPGWOUkwZvqBji6mjvoJVOT-kdSmc9VcvKDzKt3gHdRs_BGU6zntpqz_DggOEHGXGeVmJD-n2GTseg3LqaoJXfL3vPkVfKDAlMWvHf5Z9wLDoP7HrE_gMSnmv6755iCT0qeswgxl38DABBNmGpcopwx4-5ePnu7yPDzuT96DfEEi9lcilYg32Uk_A_IOiK_UmNeygFekulPZHYBBQUx7yIReqin2ZWAUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: کشورهای منطقه اگر بخواهند می‌توانند در برابر آمریکا ایستادگی کنند.  @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/466329" target="_blank">📅 23:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a74e8ba96.mp4?token=v_gUBNwB1YffKMm1o8fQDCZz9_xU8NQDCTvyxRMQDGlHs6VVe0XSHPtxnXGmoU-lDvOhox40RkIqwoT7z6kc-dKDtJgYjDRLWfuLvviN8FXOiH6JsXlCJy13nZQhJj0PsL9Q9CQu_pSWNCZBf80uHQrO_H88146xKe9ZreOA6i73pZYLP8kQAPHQmH33f0W13dbM-z4U7uyDKtXKu9JEtgZ0GcCDN6EEwq6XKlBSWLL8h7u7wGOXNnuLJStsZ4QMBnqy3-0QKkHfUB8--a5O4p9QSrI92_UJeNqv8wE4q7axuz_V2Wl0KtHAfLuynx9MmHyvYhcqscnLDYY4-g7kdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a74e8ba96.mp4?token=v_gUBNwB1YffKMm1o8fQDCZz9_xU8NQDCTvyxRMQDGlHs6VVe0XSHPtxnXGmoU-lDvOhox40RkIqwoT7z6kc-dKDtJgYjDRLWfuLvviN8FXOiH6JsXlCJy13nZQhJj0PsL9Q9CQu_pSWNCZBf80uHQrO_H88146xKe9ZreOA6i73pZYLP8kQAPHQmH33f0W13dbM-z4U7uyDKtXKu9JEtgZ0GcCDN6EEwq6XKlBSWLL8h7u7wGOXNnuLJStsZ4QMBnqy3-0QKkHfUB8--a5O4p9QSrI92_UJeNqv8wE4q7axuz_V2Wl0KtHAfLuynx9MmHyvYhcqscnLDYY4-g7kdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: قیمت گازوئیل در اروپا ۲ یورو شده که یعنی ۷۰۰ هزار تومان
🔹
ما اینجا ۱۰ هزار تومان پول بنزین می‌دهیم که حتی یک دلار هم نمی‌شود و اصلا متوجه نمی‌شویم گازوئیل لیتری ۲ یورویی یعنی چه.  @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/466328" target="_blank">📅 23:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f77840eb.mp4?token=nclkqHw5XlVjTKZ50wR8HPlWe7XEny6TnXG4DU1tVwK8Abap-jcXWZLtkv-x_Xe2H3ZHP_EJUQY3cK1wQkA_9step4TkRi6u0Q80g3dXvaLyJcbWm1m3m8_YHKrFj55g9OMEIz2tkcLH1m0bRtn5Yaq67mxCifizPbj83HQ6vsXGZkznBYR3uruW_PBH-po3wqKcv73Yu4lJp9ybOA67fqhvBVWSq4fQTRuc8HrTb6GmYWFuRAlLwB6iBX1n0__944SCw1svtAPhYqE7MFfBTeLd_FFgcWQdor5IGOTFJ1ib3TDgpaw8WrBcdnq70v1R55XfutyyEy6MRfdWbKuSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f77840eb.mp4?token=nclkqHw5XlVjTKZ50wR8HPlWe7XEny6TnXG4DU1tVwK8Abap-jcXWZLtkv-x_Xe2H3ZHP_EJUQY3cK1wQkA_9step4TkRi6u0Q80g3dXvaLyJcbWm1m3m8_YHKrFj55g9OMEIz2tkcLH1m0bRtn5Yaq67mxCifizPbj83HQ6vsXGZkznBYR3uruW_PBH-po3wqKcv73Yu4lJp9ybOA67fqhvBVWSq4fQTRuc8HrTb6GmYWFuRAlLwB6iBX1n0__944SCw1svtAPhYqE7MFfBTeLd_FFgcWQdor5IGOTFJ1ib3TDgpaw8WrBcdnq70v1R55XfutyyEy6MRfdWbKuSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: ملوانان کشتی‌ها به ما می‌گویند نمی‌خواهند از مسیر جنوبی تنگه حرکت کنند اما آمریکا آن‌ها را مجبور کرده  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466327" target="_blank">📅 23:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3315a230c.mp4?token=VujIw_cNqyC6iPlY9h7yB__nUdxJPSA_WkTIRWiZRuS3nBHgjUO0FodcBINxmE9H3r_oa_qWk6sX-86jmdMDyouxU3Vh2FZgTjMinsEvJmrA1N5LaEBaaLa4hZj1i04mZwPq7I0HT5uLo2YkudYgkUDc83mH6--tBtA3M8HTNbb7bGs4LIHWaDy6ED6J0LhXPBw1kUXveUc_NrijQRXNzrbJx9ISYvIqR3r65O8LTL9Poxss-ExLfZ4MK5haonvThWDW2M12n0AHtGQwaTrHUwyUrPHFyWJvfiuHGQ_Otlc5UhfOihF3VlgMqcMHrMfjNsIaUQjflq6tGMP3ez2k2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3315a230c.mp4?token=VujIw_cNqyC6iPlY9h7yB__nUdxJPSA_WkTIRWiZRuS3nBHgjUO0FodcBINxmE9H3r_oa_qWk6sX-86jmdMDyouxU3Vh2FZgTjMinsEvJmrA1N5LaEBaaLa4hZj1i04mZwPq7I0HT5uLo2YkudYgkUDc83mH6--tBtA3M8HTNbb7bGs4LIHWaDy6ED6J0LhXPBw1kUXveUc_NrijQRXNzrbJx9ISYvIqR3r65O8LTL9Poxss-ExLfZ4MK5haonvThWDW2M12n0AHtGQwaTrHUwyUrPHFyWJvfiuHGQ_Otlc5UhfOihF3VlgMqcMHrMfjNsIaUQjflq6tGMP3ez2k2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: هیچ شناور آمریکایی و هم‌پیمانانش در خلیج‌فارس نیست
🔹
آمریکایی‌ها از سال ۱۸۵۳ در خلیج فارس حضور داشتند، اما اکنون برای نخستین‌بار هیچ شناور آمریکایی نه‌تنها در خلیج فارس، بلکه حتی در شمال اقیانوس هند نیز حضور ندارد.
🔹
آمریکایی‌ها فرار کرده‌اند…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/466326" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمله به یک نفتکش در سواحل یمن
🔹
سازمان عملیات تجارت دریایی انگلیس خبر داد، گزارشی از یک حادثه در ۶۰ مایلی دریایی جنوب المخا در یمن دریافت کرده است.
🔹
به گفتهٔ این سازمان، یک نفت‌کش از وقوع چند انفجار در نزدیکی خود در جنوب المخا در یمن خبر داد، ولی خدمه در سلامت هستند.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466325" target="_blank">📅 22:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c36029544.mp4?token=Ce5c2yRtSvpJuSDA0pyPIXXKJ_y5MXyuWMFjThqLoPdFFtwRXB_6kltb3fEAKyh2nruT9wQax7eptwMei0CJnrMXLDUrqzw_3O--xlfXQc0NrmialFjVFopyiVxmWp4Zl1Otz9HbPDGLRfX70LyFKTrQnaMRB39eRrjxPs84VO7fCL2LM6XvlYbJuHPRnCeXGkzML2UxCLbNqwBIadzqvoiehdBIycog_wTYPh_5cgSRUzhiCPnIlKhDUO8__hOZZHfnt4zpAMg4JdbeXap9RK13drAOgZpyXOZaVPmmDPnuNlWumS85vYtZzehSu5WPpExD1fpkjg4YWeiE8fxNeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c36029544.mp4?token=Ce5c2yRtSvpJuSDA0pyPIXXKJ_y5MXyuWMFjThqLoPdFFtwRXB_6kltb3fEAKyh2nruT9wQax7eptwMei0CJnrMXLDUrqzw_3O--xlfXQc0NrmialFjVFopyiVxmWp4Zl1Otz9HbPDGLRfX70LyFKTrQnaMRB39eRrjxPs84VO7fCL2LM6XvlYbJuHPRnCeXGkzML2UxCLbNqwBIadzqvoiehdBIycog_wTYPh_5cgSRUzhiCPnIlKhDUO8__hOZZHfnt4zpAMg4JdbeXap9RK13drAOgZpyXOZaVPmmDPnuNlWumS85vYtZzehSu5WPpExD1fpkjg4YWeiE8fxNeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: هیچ شناور آمریکایی و هم‌پیمانانش در خلیج‌فارس نیست
🔹
آمریکایی‌ها از سال ۱۸۵۳ در خلیج فارس حضور داشتند، اما اکنون برای نخستین‌بار هیچ شناور آمریکایی نه‌تنها در خلیج فارس، بلکه حتی در شمال اقیانوس هند نیز حضور ندارد.
🔹
آمریکایی‌ها فرار کرده‌اند و بیش از هزار کیلومتر از مرزهای ما دور شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466324" target="_blank">📅 22:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466323">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fefadf12c.mp4?token=bCOSOj4aQnFRAcOt05z1EEblgNhNoGQyKkK1hvEAEXZu20RghMb_3niOTNfuSCShWlp0fe3_AIEi4IwmwsfAa-ykUpa9clW_qu60U-pOfY8w2WnjsuOeoHLlocp-fRd2qz34CsKgU_qJLjFARh_JUStSchmvKQuB3zT3NpnyCmqakPKcs7ZGPm2Hl2qStiYPl8X5AVgml4N2YerUQ0nXp-LAV6O44K8fHZQOSuoSVV3G2NntQ0sEC9uSN6O7Z8LeOqVaKd7zklIehpmgLeJWhB-n_aCCol3d-CpQU9tiCBx5rUsYGt-Ey3WNCmgzciZRW34wWd34GsRdDSbWPX21KlJ45vNes4-Kphrnk7wocUT0IS2Y6WO4aGs1J8fPP3zfb_4ptSgOGqfysJ9YXKsn8RQfrO6TwP6_yPrcSR-QBahsRc_IDrfunGN_zvmhVQTyTcbQFZG0CE6nHphsYmy-o8EufaSsz0BQOlFZFdDsSG7tHi4y7G7XSsCC6L2RRV3E1tATTD5OlGdoESolYP2pOhG7nF0K51-_8LSeYOUNm0NoFQ9PuqiRvVZI_v-uFkd_y_6bzXWglZR-bYhe45qjBNzIrW_egAWaJiqXa8CVISZhBcJUIn_W_yLwGoPay0zLwqwelQsgsAMJ_PNz4gbBsLyaU0yxlb-f_o4ktR-alyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fefadf12c.mp4?token=bCOSOj4aQnFRAcOt05z1EEblgNhNoGQyKkK1hvEAEXZu20RghMb_3niOTNfuSCShWlp0fe3_AIEi4IwmwsfAa-ykUpa9clW_qu60U-pOfY8w2WnjsuOeoHLlocp-fRd2qz34CsKgU_qJLjFARh_JUStSchmvKQuB3zT3NpnyCmqakPKcs7ZGPm2Hl2qStiYPl8X5AVgml4N2YerUQ0nXp-LAV6O44K8fHZQOSuoSVV3G2NntQ0sEC9uSN6O7Z8LeOqVaKd7zklIehpmgLeJWhB-n_aCCol3d-CpQU9tiCBx5rUsYGt-Ey3WNCmgzciZRW34wWd34GsRdDSbWPX21KlJ45vNes4-Kphrnk7wocUT0IS2Y6WO4aGs1J8fPP3zfb_4ptSgOGqfysJ9YXKsn8RQfrO6TwP6_yPrcSR-QBahsRc_IDrfunGN_zvmhVQTyTcbQFZG0CE6nHphsYmy-o8EufaSsz0BQOlFZFdDsSG7tHi4y7G7XSsCC6L2RRV3E1tATTD5OlGdoESolYP2pOhG7nF0K51-_8LSeYOUNm0NoFQ9PuqiRvVZI_v-uFkd_y_6bzXWglZR-bYhe45qjBNzIrW_egAWaJiqXa8CVISZhBcJUIn_W_yLwGoPay0zLwqwelQsgsAMJ_PNz4gbBsLyaU0yxlb-f_o4ktR-alyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه قبول دارند جنایت مدرسهٔ میناب کار آمریکاست، به‌جز پهلوی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466323" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec5950702.mp4?token=Hl4fuhnTUSX8W0_R4m473AYB5OgAc_QlG5A22vZQ8peMboTpdA6HqN_fBmsIH1bXIt66tDg2xCinn15XJl_lPzs6dkSR_6iQT3NfSwiuuZS5jKObob3DbJEMhcqloghF7GPi7HZX1wDdg9yP73f7Ioajq3-NdGPo2m6kdPae0CXMe-yq7z4Ww0tccykLJSyI3vxpfk7WyPN5yFW-Ofku2sjkt00YufyEcK7N5kzg9OrBr3TyJ-144UBwDceda83V0sFkyzV0-sjF4tBNN1fMYTkXly7S_g3KTaLbhYBXSqWZPNiXa-rVlDEprH25MZZS3B2ytQDCdqfVasClw5B0ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec5950702.mp4?token=Hl4fuhnTUSX8W0_R4m473AYB5OgAc_QlG5A22vZQ8peMboTpdA6HqN_fBmsIH1bXIt66tDg2xCinn15XJl_lPzs6dkSR_6iQT3NfSwiuuZS5jKObob3DbJEMhcqloghF7GPi7HZX1wDdg9yP73f7Ioajq3-NdGPo2m6kdPae0CXMe-yq7z4Ww0tccykLJSyI3vxpfk7WyPN5yFW-Ofku2sjkt00YufyEcK7N5kzg9OrBr3TyJ-144UBwDceda83V0sFkyzV0-sjF4tBNN1fMYTkXly7S_g3KTaLbhYBXSqWZPNiXa-rVlDEprH25MZZS3B2ytQDCdqfVasClw5B0ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۸شب از همبستگی و ایستادگی مردم کاشمر تا مقاومت و خون‌خواهی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466322" target="_blank">📅 22:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c72b757f9.mp4?token=Zqydxp14NLDA-r6qDxTTW_MjWOd74sNkk5j7Y9Rw0KnSp_GauKRr8NfioP6x5MSW_Q8bABXcgWdR2M6Ty4Jyv4aKOe1B6Z9r36lHU9IzcQreUOjibuXsmrKbzYoHhayBP-_SSqIawUQDM1J8cuz97kD05neNC-YuNgxm9Wl4SJEhXmZUURY81P5AE6znQm3n3y4rZayrFHWtbsaGPxHxRhBPZE3ysr9sgvVBecEWhvmmumRjTEH-l_ngrNgz7QLDuGTFel0dRocqv3Pl4Vb0-HjoVDsfObtGwlNo3LvR8kqIDqNvcd5lheNKZiMPeGGbKtKKJ8cMLRCSsGsYJohMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c72b757f9.mp4?token=Zqydxp14NLDA-r6qDxTTW_MjWOd74sNkk5j7Y9Rw0KnSp_GauKRr8NfioP6x5MSW_Q8bABXcgWdR2M6Ty4Jyv4aKOe1B6Z9r36lHU9IzcQreUOjibuXsmrKbzYoHhayBP-_SSqIawUQDM1J8cuz97kD05neNC-YuNgxm9Wl4SJEhXmZUURY81P5AE6znQm3n3y4rZayrFHWtbsaGPxHxRhBPZE3ysr9sgvVBecEWhvmmumRjTEH-l_ngrNgz7QLDuGTFel0dRocqv3Pl4Vb0-HjoVDsfObtGwlNo3LvR8kqIDqNvcd5lheNKZiMPeGGbKtKKJ8cMLRCSsGsYJohMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلیمی، عضو هیئت‌رئیسۀ مجلس: در طول جنگ مجلس تعطیل نبوده
🔹
از ابتدای سال، مجلس ۴۵۲ جلسۀ نظارتی داشته و تذکر، سوال و تحقیق از وزرا جریان داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466321" target="_blank">📅 22:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466320">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5769ab9e.mp4?token=LvwNZ0gDsuq7oHWWoVEhAPmqm_0K-kKqdBZMgP23bn_j7bWF_eyL-9r8bK-cdMGJi-_ZUWLD86S7JVFLRnJZI-H60s0LnE5VFyqG_EFlzUA90mKQ-yBSYI3eMYzlcAVycaoWAyVEAgDAX4PHBdBBYfAGc6fTKpNv7VRK16V88gTS-8tu7GgH9Cb64g7orKf-LQJrSxlJGz9kSsgcOqXxobhlMnwso-UqkYbLRRLYedRDjTKWALn-rBLa8J0AvBgERO174jIqjACNZclKthTntIhWMIwOIeu3x-M9AA0Bd4-FeD_7StDW6XwxDKCYTlLeuPo8SEnoLXUCMq9yhYSLWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5769ab9e.mp4?token=LvwNZ0gDsuq7oHWWoVEhAPmqm_0K-kKqdBZMgP23bn_j7bWF_eyL-9r8bK-cdMGJi-_ZUWLD86S7JVFLRnJZI-H60s0LnE5VFyqG_EFlzUA90mKQ-yBSYI3eMYzlcAVycaoWAyVEAgDAX4PHBdBBYfAGc6fTKpNv7VRK16V88gTS-8tu7GgH9Cb64g7orKf-LQJrSxlJGz9kSsgcOqXxobhlMnwso-UqkYbLRRLYedRDjTKWALn-rBLa8J0AvBgERO174jIqjACNZclKthTntIhWMIwOIeu3x-M9AA0Bd4-FeD_7StDW6XwxDKCYTlLeuPo8SEnoLXUCMq9yhYSLWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما چه چیزی باید بدهیم تا آمریکا راضی شود؟
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466320" target="_blank">📅 22:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466318">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa71ac9306.mp4?token=c4U7kuT1Lv-2TLHgDMzrgj6CoNd5gMasekudgiB_ofbdSLdKcLxsHCp6KDfdSxK5J-iPL7aGfrQxrupTDUkwVKTsZafiqFGoIgwSUBnd8Cr8himRyjyrAvqL6M_sNKfPHMx3ZNJAl0IriJnQoxd-BwR39aXRNDhpjKvxYhQ5R_z-7-fUDu7i8buUQDX8rtIuHSnJouShIJJk12cp6D0lyPKcfw7ungFBqGkm_4565IAHSIs2NnibXsJdDqwMVM-CcCc2tMDY8nJ_SbIWJC8KX3y_8fAzhgqkfNg7tn15ptqu958DL1UVhcG2kaaASlVtDO1JOF9tNIGNs5bWen9aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa71ac9306.mp4?token=c4U7kuT1Lv-2TLHgDMzrgj6CoNd5gMasekudgiB_ofbdSLdKcLxsHCp6KDfdSxK5J-iPL7aGfrQxrupTDUkwVKTsZafiqFGoIgwSUBnd8Cr8himRyjyrAvqL6M_sNKfPHMx3ZNJAl0IriJnQoxd-BwR39aXRNDhpjKvxYhQ5R_z-7-fUDu7i8buUQDX8rtIuHSnJouShIJJk12cp6D0lyPKcfw7ungFBqGkm_4565IAHSIs2NnibXsJdDqwMVM-CcCc2tMDY8nJ_SbIWJC8KX3y_8fAzhgqkfNg7tn15ptqu958DL1UVhcG2kaaASlVtDO1JOF9tNIGNs5bWen9aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۲۱۸، هم‌چنان پای عهدشان هستند
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466318" target="_blank">📅 22:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466317">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jph6VnKqGarAuDJH1YRCs6d77n2t4qeXoQkgr8G94-hGIZ9LiLONIthwzuTmq4LwQejpNh7BKWFjLgkX0KaA82JE035u0U8QmsfoMyAthcbk5oZEIq3QKEY3JDF7LRZOC-hDBM0f4_cSWwa_5YWgddrAV3wnoshnz9_ZgyfZjPXcYFEE0I9uytD6cFmkIyCw32_J2Sm-a9rgjpEHhMtd87srrNcanrOrWyzHuc7nFO2WWGQcTvQ8XZ-JaRukGk4iqPrmd5lWtj3aLWvZpBUuMJd0i-Ju4_D-z8qC9Iy3DT-4VPukIJuX7RdDo2SEFkoZjrDLrHvKtFWKy92cqcRUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کمیسیون انرژی: قیمت نفت باید از ۱۱۰ دلار عبور کند
🔹
عبدالحسین همتی: ما تمام تلاشمان را می‌کنیم که قیمت جهانی نفت از آستانه ۱۱۰ دلار عبور کند، با توجه به شرایط منطقه، ظرفیت افزایش قیمت نفت همچنان وجود دارد.
🔹
بازار جهانی نفت به‌شدت از تحولات سیاسی و امنیتی منطقه تأثیر می‌پذیرد و هرگونه اختلال در مسیر انتقال انرژی می‌تواند قیمت نفت را افزایش دهد.
🔹
اگر ایران امکان صادرات نفت و فرآورده‌های نفتی خود را از منطقه نداشته باشد، هیچ کشور دیگری نیز اجازه صادرات از این مسیر را نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/466317" target="_blank">📅 22:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466315">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaqFixI6u20T9GQ-G7VkiuVJ89N6jfH475ZUXgifJM-KurXLSk_XyW2WTUYjp4PmUALQSFZrhS0phurZB8WThmfvOEWkkTGeeGSUKQW9WJXWTHHRf_8HrHbs-I_HYcBt39yAQB79oTbcMlolL_jDSW2KDpM816bfMHv2Oev4t78PPvHc3tRv0gZcu183Xcecn5TcxLhaTkiNpjXGqwXwxf0gbJdo8LqIQSxbTfEzlHfxYABQzjUaBNL88CIb8sVtBpXDrAaMIMGxsoj9Vw-G2qx3YrGdBQs5Yn1gZXyOcv5CBALJY5zO6mqskN0s5PFZk_oHWBryv5Rlch_Ze87dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uej63rHEfdxzV8zbxM71KCzukxAxhZ-_R89YMvvniM_KCgfiw96R9Cquyc4ovdDOVbE8A7Kx7oJ2o6Df09oWfUAltPcKyPC_FOQslsGvkBkpp28I2l5ouaFWqERm-7i9Sh7vksyO3boUIWbhrXK57lsxUCBHJOoq0UMp066hqhHOLGqJO8g5WN5bYJatdgFWF7p0do-l-b4j6pa6foNg6wEFo69eanaa9npEkn9bv0alkI0jSFXqLaYFk0h6n5JkYXvxSWvV3tia8SymCVmW8AUnFyPpyqphFTY1Q0ra02kIJffjiZAPhCglmfJAMax1ud5oD8YtXLA8-RYP59Tcaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پترولاین عربستان دوباره تیر غیب خورد
🔹
براساس تصاویر ماهواره‌ای سنتینل-۳، امروز ستونی از دود سیاه به طول حدود ۵۰ کیلومتر بر فراز این سایت دیده می‌شود. داده‌های سامانهٔ FIRMS ناسا نیز ۴ ناهنجاری حرارتی در این ایستگاه ثبت کرده است.
🔹
خط لوله شرق–غرب عربستان تنها مسیر صادرات نفت این کشور است که از تنگهٔ هرمز عبور نمی‌کند. این خط لوله در ۱۱ سپتامبر پس از اولین موج حملات بسته شد و در ۲۲ سپتامبر فقط به‌طور جزئی فعالیت خود را از سر گرفت.
🔹
تا این لحظه جزئیات رسمی بیشتری دربارهٔ عامل حمله یا میزان خسارات واردشده منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466315" target="_blank">📅 21:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466314">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVFoDRomn1bGIgw15LVonY6unBl6Xz1VjRNkYYCoinexFILqGEZXe5_rPEDH7_IXoFEGYgnJTJ8XuJSGiLNAXy21TjhyFXDv2RJ4-jJAPbddW6-OKXKEUZqASIP3vWEGv6A9RHqzlHU0hd5du8QAhjBVQgac8XKsMAUIi8RADQjr7nXymlGQGPqV1IwVJ_eZmuiW-WxfEMICIU-09dwPIRnyOoJHcKLGkVP4QiuGY-_J_JXnAtMSrixvHtaVpIhqkNQDzSR1GmbSHExOa5g1R6E5b7CFrNHe2-90KN_-59RdeZGM3p6-NuYXYjtQd45FigS1xim4ClDgpU7738qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس علیه استقلال تا دادگاه عالی ورزش CAS می‌رود
🔹
پس از هفتمین دربی پایتخت که با تساوی استقلال و پرسپولیس به پایان رسید، باشگاه پرسپولیس به دلیل آنچه حضور غیرقانونی یاسر آسانی در ترکیب استقلال می‌داند، از این بازیکن شکایت کرده است.
🔹
مسئولان باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466314" target="_blank">📅 21:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466313">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک نفتکش در تنگهٔ هرمز هدف قرار گرفت
🔹
به‌گزارش سازمات تجارت دریایی انگلیس، یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفته است.
🔹
ناخدای این کشتی می‌گوید که بر اثر این اصابت به موتورخانه این نفتکش آسیب وارد شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/466313" target="_blank">📅 21:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466312">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9314b8a6.mp4?token=eGfuUz-9ZFDxb4YeuTbxZ5ejGS2Ig2_MueL88jIjDwXrIuOMdN693L5hdozsiC8kgdeuFAn8Jwe1rBvcFDubaO2Lg7UacslnTlIjEO6BeDEUMlqHz3DXTYvg3XTZQaLXVrKi4qL0ueS4cv37smtG1lObcqTxGKtNrBD58KydqFYbBzZooT0NzRLO6PZ-I_l9T-1Th8fKYbBTONRZmLaugZFgmZIgG7J1dgmchvO9Coj3Yx-Fhryi8TpJ_fzc-vIG6AlQPTfry25uByuvHbI87phhDPY3VdNF7kFsw7B60xWZEfPtiiyCY5RDyjEcBetIzOJ-lgohvqnaQLqcF5jnrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9314b8a6.mp4?token=eGfuUz-9ZFDxb4YeuTbxZ5ejGS2Ig2_MueL88jIjDwXrIuOMdN693L5hdozsiC8kgdeuFAn8Jwe1rBvcFDubaO2Lg7UacslnTlIjEO6BeDEUMlqHz3DXTYvg3XTZQaLXVrKi4qL0ueS4cv37smtG1lObcqTxGKtNrBD58KydqFYbBzZooT0NzRLO6PZ-I_l9T-1Th8fKYbBTONRZmLaugZFgmZIgG7J1dgmchvO9Coj3Yx-Fhryi8TpJ_fzc-vIG6AlQPTfry25uByuvHbI87phhDPY3VdNF7kFsw7B60xWZEfPtiiyCY5RDyjEcBetIzOJ-lgohvqnaQLqcF5jnrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466312" target="_blank">📅 21:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466311">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6b828b64.mp4?token=ESmokFBluyJm0DrqQ9W0ObeZbK71hFSaWS1UmswqlbqPULkZHla_AOeJKDQsX7h1i7t7MMdCeA1Sd6UgK67BgemofiqcHZ7zfaRGKAn0sSRsIOlmpcTbW9vXODvA2OVKP_UdUahUS9losmtIo5qckJHZ5avUySZAFkyvHW9UO3DZo3b2BcyJQTBpFFJA-mo7f4IevjjeEFw_ktz1rjZx5SKGaoECSlEE4dLOdpTF2mTDjnXnA92icr86x3Da46r7tAwSZ5Eywa6ZbDTER5nTZOGRYQ7dl5XR7ILaCbULpM5w5O9crC-zByLf14tDopt3RtrXK524d_SJGkYQ_cwXEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6b828b64.mp4?token=ESmokFBluyJm0DrqQ9W0ObeZbK71hFSaWS1UmswqlbqPULkZHla_AOeJKDQsX7h1i7t7MMdCeA1Sd6UgK67BgemofiqcHZ7zfaRGKAn0sSRsIOlmpcTbW9vXODvA2OVKP_UdUahUS9losmtIo5qckJHZ5avUySZAFkyvHW9UO3DZo3b2BcyJQTBpFFJA-mo7f4IevjjeEFw_ktz1rjZx5SKGaoECSlEE4dLOdpTF2mTDjnXnA92icr86x3Da46r7tAwSZ5Eywa6ZbDTER5nTZOGRYQ7dl5XR7ILaCbULpM5w5O9crC-zByLf14tDopt3RtrXK524d_SJGkYQ_cwXEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ هربار با توهمی عجیب‌تر دربارهٔ ایران برمی‌گردد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/466311" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466310">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca6430549.mp4?token=c5LKOdpipJGczP_BnTYWTrejhZAry-KeRNlaQl4kqQr0tFWjeHEN-syuovJ2TIumoLuJkPmF_WtRgGqibm3SaIUSCcTEBiFOCzFMXJvHMLmXnyfd0V2rkxJzuWI1WjMX_6o9B3nDO5A3JC0lvWZwAzpae_7FebXVWCcevVSsOzU-suYwttVXp3jUdN4bHOWg3bdeg34_sfVmS4W6Kp3tgK4eX6kcozByM7za-hF8VC1KQQUBzMPuukOVKQPWr1MnUboD1p57zzj1YY7i9zJCK6lWVUbJ-s9xXkTTj7jyIIt-YwkHl7dVlRxTdnu62x4wMLz5cMafC1UtCnl4TyFseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca6430549.mp4?token=c5LKOdpipJGczP_BnTYWTrejhZAry-KeRNlaQl4kqQr0tFWjeHEN-syuovJ2TIumoLuJkPmF_WtRgGqibm3SaIUSCcTEBiFOCzFMXJvHMLmXnyfd0V2rkxJzuWI1WjMX_6o9B3nDO5A3JC0lvWZwAzpae_7FebXVWCcevVSsOzU-suYwttVXp3jUdN4bHOWg3bdeg34_sfVmS4W6Kp3tgK4eX6kcozByM7za-hF8VC1KQQUBzMPuukOVKQPWr1MnUboD1p57zzj1YY7i9zJCK6lWVUbJ-s9xXkTTj7jyIIt-YwkHl7dVlRxTdnu62x4wMLz5cMafC1UtCnl4TyFseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعزیرات اصفهان این‌گونه مچ طلافروشان متخلف را گرفت
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466310" target="_blank">📅 21:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466309">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe94c4a5.mp4?token=HLdkfN2lM_PXa1SJLm8gPOA_b2BCSfejM3449LUGuCnln-j5Spi0XrcCi7WPic7vg7M_PT93fUa1s_shVP89oeAtMCDnZW1O7vu9hh0hTpVJokfFV8AQEkP3mri9GC6BElQyWDT06YD938gXwai62OjYf9A0onJoPhentZi7-HcGkMNSTquKlC_mbHfJBvHT8Kka6CQ0FjsnbFfp-jaWTPAhPW2b104uAkoLqFdRDn06w69cQ1Bz9sdb8hXZW71oD6E_OruoBprpQdfHAW18pATkWf2ikNXeJDHtALfifuisBzoLpshXxFrUWOUWckNIZy_uEXy4Ua7iQ5N1a6jKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe94c4a5.mp4?token=HLdkfN2lM_PXa1SJLm8gPOA_b2BCSfejM3449LUGuCnln-j5Spi0XrcCi7WPic7vg7M_PT93fUa1s_shVP89oeAtMCDnZW1O7vu9hh0hTpVJokfFV8AQEkP3mri9GC6BElQyWDT06YD938gXwai62OjYf9A0onJoPhentZi7-HcGkMNSTquKlC_mbHfJBvHT8Kka6CQ0FjsnbFfp-jaWTPAhPW2b104uAkoLqFdRDn06w69cQ1Bz9sdb8hXZW71oD6E_OruoBprpQdfHAW18pATkWf2ikNXeJDHtALfifuisBzoLpshXxFrUWOUWckNIZy_uEXy4Ua7iQ5N1a6jKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: مردم به‌زودی می‌توانند با اسکن کدهای نصب‌شده روی خودروهای پلیس، انتقادات و پیشنهادهای خود دربارهٔ عملکرد پلیس را ثبت و ارسال کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/466309" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bf1ad55b.mp4?token=m8-i56jLV3in1wLRz6jeV_KUbaFllnLmsp6AG53DbE9HjLn6PELnOQlV7ZP-4vcZwAS1ZVw-fUW3_FNxJn2ZxUet0-Kqlv9cY-8Q4AK1esJ-8asvb6ArLuAak-0Ml62xjOXo9mKNdp4M2RT8MJiU3MQKCkFbOZHzey80vMDX7K2gUQiAToIvccrJzxUflpv_7S5I-PKnD1wh2LEyNm8sRKLpAuDAlJJCdbSzBj2n-ZkOQCAC6kW88Uu8QKtXGdBZ4srGx6d6koFLOg-v3Izhj9oAABYkpSENL_NmyTcZDZUcDk2N19EaATcQWMYsviETes_3-xGCZIo3INZgr68nDQDq-g1hWjWFsDjhG7U3bCzbFK_JRWZ91fRBe8oqaqyT3RrBdUa4Rm8agAWnZOCrfVb1jaJCSAhtPSIcp85fKpRKTtXnC6CsswjCoseZeSffXjYH1ujB10AJRz-xZke6msukJxH8cTXBdxWqv8oE3eeomW1jOMwH0zGYHdpuET-7zV6S3b10Xt45jEryk0qog1HD7qZJUn8BnRWkAzNBQW27HjOFs9Hu5lFckXHMVJnNdOF7fng8NAztiQtJghZadOaoXjLwFvoKh9UA0GSSdnbLBn8JXReGvjZbrD11RRK9DEes1MU5JHNGBRv_0RWAxCXzzFLzzl6p3lUvS57ROL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bf1ad55b.mp4?token=m8-i56jLV3in1wLRz6jeV_KUbaFllnLmsp6AG53DbE9HjLn6PELnOQlV7ZP-4vcZwAS1ZVw-fUW3_FNxJn2ZxUet0-Kqlv9cY-8Q4AK1esJ-8asvb6ArLuAak-0Ml62xjOXo9mKNdp4M2RT8MJiU3MQKCkFbOZHzey80vMDX7K2gUQiAToIvccrJzxUflpv_7S5I-PKnD1wh2LEyNm8sRKLpAuDAlJJCdbSzBj2n-ZkOQCAC6kW88Uu8QKtXGdBZ4srGx6d6koFLOg-v3Izhj9oAABYkpSENL_NmyTcZDZUcDk2N19EaATcQWMYsviETes_3-xGCZIo3INZgr68nDQDq-g1hWjWFsDjhG7U3bCzbFK_JRWZ91fRBe8oqaqyT3RrBdUa4Rm8agAWnZOCrfVb1jaJCSAhtPSIcp85fKpRKTtXnC6CsswjCoseZeSffXjYH1ujB10AJRz-xZke6msukJxH8cTXBdxWqv8oE3eeomW1jOMwH0zGYHdpuET-7zV6S3b10Xt45jEryk0qog1HD7qZJUn8BnRWkAzNBQW27HjOFs9Hu5lFckXHMVJnNdOF7fng8NAztiQtJghZadOaoXjLwFvoKh9UA0GSSdnbLBn8JXReGvjZbrD11RRK9DEes1MU5JHNGBRv_0RWAxCXzzFLzzl6p3lUvS57ROL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دربارهٔ کسانی گفتند که در میدان ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/466308" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVUTH_yfkfuh7P0LNl7Gl5mZW6xMBEr8bNqb_rwju-u8mbxwTjvw42NH0EzrR3QNIfECGYAfGsIq43cl4VObenWksj1SsGDao0hX9anyIodUYXJXetsMoDHvGije8OO1j0haUFpbMs5lHXjgW_w2ZYJFTGB7_IklFT_iQ03XZ9oJb1e0cxd8Ev1I7q4gTloSfBitC-idsT__ar2l3pGb8wUC2KIalK_F9z_CELgVSReB70IkGwXFVaI63e1jfeDgjRN4hBxnbuv6EMNLcera5xcDMCUVeBaZtJ9MokdHsyXIhK_IvCB_tODKU6hcbTI3Dw7pp9OxNp9ylOWJoLxo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۸ فروشگاه شهروند به طرح «تورم صفر» اضافه شد
🔹
از هفتۀ گذشته طرح «تورم صفر» برای ثابت‌ماندن قیمت ۱۲ قلم کالای اساسی در ۱۰۸ میدان میوه و تره‌بار تهران کلید خورد.
🔸
امروز نیز ۱۸ فروشگاه شهروند به این طرح اضافه شده‌اند و قیمت این ۱۲ قلم کالا در این فروشگاه‌ها…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466307" target="_blank">📅 20:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466306">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621b24ff29.mp4?token=WD7s1irNiaEJ-ZzS-aYX7sAL4owxJJfkGWu1abSLubpnLKTi5_5VvWKBknmq1OexmXCS7dIDaR1ZZBNH4zmyuTiDSSTe5mL0FlDQrWc_8keAtLq0cPnH8QEgHtYhMuOceBw8wmPH1i-EAqR3tVRu7BZrPdyOvmzpLKHDZnhEKekAbC5jL04fSyqqLiZLztgj04ngnPLwG9l4hFv87u2gCFd6RkYNJwTlxMSM5MQM0h9OXlz3gFkQ33w8JWyBNuF0t5AGL_1HR0phm8tCEtRDj4HliHVikbHts5LPDVy1y5x9jsWRtPjWrfEIZ2VYVqJ5R8yNpwAWmRdMgJ6UFvwHjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621b24ff29.mp4?token=WD7s1irNiaEJ-ZzS-aYX7sAL4owxJJfkGWu1abSLubpnLKTi5_5VvWKBknmq1OexmXCS7dIDaR1ZZBNH4zmyuTiDSSTe5mL0FlDQrWc_8keAtLq0cPnH8QEgHtYhMuOceBw8wmPH1i-EAqR3tVRu7BZrPdyOvmzpLKHDZnhEKekAbC5jL04fSyqqLiZLztgj04ngnPLwG9l4hFv87u2gCFd6RkYNJwTlxMSM5MQM0h9OXlz3gFkQ33w8JWyBNuF0t5AGL_1HR0phm8tCEtRDj4HliHVikbHts5LPDVy1y5x9jsWRtPjWrfEIZ2VYVqJ5R8yNpwAWmRdMgJ6UFvwHjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخشش ایران در المپیاد جهانی نجوم
🔹
تیم ملی المپیاد نجوم و اخترفیزیک ایران در نوزدهمین المپیاد جهانی این رشته در ویتنام، با کسب ۵ مدال طلا در میان بیش از ۶۶ کشور و ۳۲۰ دانش‌آموز درخشید.  اسامی مدال‌آوران ایران:
🔸
سارینا علم‌پور
🔸
محمدحسین حسینی
🔸
هیربد فودازی…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466306" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466305">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh-Wxr_9x_pCtCVQazJ2ayShOp_xyfyb9QHms1c-gb16krJRwzn--kT9eYzrPrcNyMdSs4vLcaY_bXo_fSG1tcpDyGtO9DKgKNPd7gklKqXDH0-QmQM7HD_8PXd75nWTwobGZn5prGeNOVOf6Bv7o7oNfG1jHw8cRv3WScd5N4FwWkVU7ze9b9qAyKBcfMQdSJEnarU9GIJ163BsZyE7H2hpN6_LC2ZzVHchNvBkYHoQpSpai215y3kOXsQuocxHjg8uvhJy0CtCH6L0AzaQxjx6Ew1SGjMfGHrbihHQKVuN4UEsMONsiJRl5JF-VLb69NJEJS1qWVGlEhiW0ilZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/466305" target="_blank">📅 20:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466304">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/466304" target="_blank">📅 20:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466303">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2372ddac.mp4?token=suGd1cDAKLaCmTrvKo20flPnfiBt8JBNROx0GwBf-OcTo8HvBHQvanlKGxb9W2rft_J9OOcicuZuz2XDpwDQPo3HQU6SEZA9LDaxdL0cDl_QHIRpAzbjBmfsFhJauXD5VVbaCY66OtBx5WujqtNtpGEUEvojW-L1nw6KxLNuZel9DimgK84fCLOF9Q3wp16xZj7wGxENjHc0C5OiClYOBoX-OFhSGxXYopGcAAS29huRZSQZ-h-MTTkiKDqGb-MZpxjV968SVBmZm9YKYG6LJDeYox-ukVlEZtouEYZE7-OavF38F3RUvDxDtSTwf4QPX7DG5FmXO-DhgnmCQAmR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2372ddac.mp4?token=suGd1cDAKLaCmTrvKo20flPnfiBt8JBNROx0GwBf-OcTo8HvBHQvanlKGxb9W2rft_J9OOcicuZuz2XDpwDQPo3HQU6SEZA9LDaxdL0cDl_QHIRpAzbjBmfsFhJauXD5VVbaCY66OtBx5WujqtNtpGEUEvojW-L1nw6KxLNuZel9DimgK84fCLOF9Q3wp16xZj7wGxENjHc0C5OiClYOBoX-OFhSGxXYopGcAAS29huRZSQZ-h-MTTkiKDqGb-MZpxjV968SVBmZm9YKYG6LJDeYox-ukVlEZtouEYZE7-OavF38F3RUvDxDtSTwf4QPX7DG5FmXO-DhgnmCQAmR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: طرح تثبیت قیمت ۱۲ کالا در سراسر کشور اجرا می‌شود
🔹
طرح «تثبیت ۶ ماهۀ قیمت ۱۲ قلم کالای اساسی در تهران»  مورد توجه دولت قرار گرفته و قرار است این طرح در سراسر کشور اجرا شود.
🔹
قرار شده کمیته‌ای ۶-۷ نفره تشکیل شود تا تجربیات و زیرساخت‌های ایجادشده را…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/466303" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466302">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIxYe0AiOs7LF5YCNFNxbOZi9jCdMQs8X7d7PShkyJXhC0K4-KKGgvvf8QDkv6ClzjRjlfF3mBwgZa_Xj7o3tR6fvg63S1ze3i7GyMBXr1fZjX4hIDrX32S4hmu6w74N2DmJ67dD2nMbBcYQHFHGlMuT_Cy19rIyF9uKLqhcQohNCGTiXRifRCjI0OivA-XKPmZBh24eiqX5BJq653sFzomlnOojWK6PvA_ON_LeMBH9M3o0up5Qu3mhFhu-JB_pTaL43M8z6g6-DL-dUK_M3cAy1ClJxhO512WyZZ7H2Vo4BSF4ONe6WGmf9CS6qQ9TXo9khtjI9B4DIvE0hAAcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح تثبیت قیمت ۱۲ کالا در سراسر کشور اجرا می‌شود
🔹
طرح «تثبیت ۶ ماهۀ قیمت ۱۲ قلم کالای اساسی در تهران»  مورد توجه دولت قرار گرفته و قرار است این طرح در سراسر کشور اجرا شود.
🔹
قرار شده کمیته‌ای ۶-۷ نفره تشکیل شود تا تجربیات و زیرساخت‌های ایجادشده را بررسی و به کل کشور منتقل کند تا با همکاری دولت و شهرداری‌ها، این مدل در سایر شهرها نیز قابل اجرا باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466302" target="_blank">📅 20:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwIcNLUW3aBL1DQbj56pOXN63_VW-e20MREbKp12OZvVkdzyfmFTsSDUj2kvZKpdPVHn9gZ1odMHrR2CcrhOA101vU7j0fc5h0FvzCFjErbJA7LaZjK8HuXUx5TlidvAHEv6RqrixFx-yku0T0KnK10d1Bv9SKPzXXWbmhXDlgCuNnK-sLWtSL6DLBckEsYHMeXYV2cBqqfZl985djtUJQE5TkefWKmudKhoi6wKlkc7fnq9lKCKC1GDYSjNrmEc4DPhwZW6tndTWlFzHAUoJH4AD2uQS4LGZ9W3OnHicc2qu3KdwmZPQIuVVORZvXpxPNyIea6WcoNSud1qIk9G7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
محل‌های استفاده از طرح «تورم صفر» شهرداری تهران را بشناسید  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466301" target="_blank">📅 19:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466296">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دفترچۀ زبان.pdf</div>
  <div class="tg-doc-extra">17.7 MB</div>
</div>
<a href="https://t.me/farsna/466296" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
‌
🖼
دفترچۀ انتخاب رشتۀ کنکور ۱۴۰۵ منتشر شد
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/466296" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fcd4c336.mp4?token=UWepxLzA_coLq5LGXCZhC-SnoKNdmqKo4LtHYp7RzD7A52Qt6Jf0x_luW0vE4S8Vq8p6V1zgQ5Pl4ewlRiL3rJ1krymy_rDsYe1ICr400JPPyCkWm4lZ_KfGK8bODLA0zV8A28vQ0SdXh6GnUDXaFhEoFUaKRUArB14j2FlQPesVjFl18bvgNAYE_dO9eRbfhmhsU3U_W5PGdFr7QttM0Jm1UlFWJiBGi1kk56iaoSsVJ1XktnJXtiQ-zOkAglGJ0Dr7Kp9lM5FbKz2JUce2BguRkKECVQqcycZpkXtxM9qpciO_643OsDwqJJQGhWcjnji83_szRMapBUgKJ5yJPIOYJdhjQ-ODgyLZkJw2_VqGb5vUkquacqcE89GWQir0oeM-XbZ76dXeHCbNnUUl0SD3mBwCtCwt5Ruh7aC5TgmGWTMORdt8-TPxUqbZA2kBxEWdR3AmkvIaq1mGL6SS4CtFh83pgvYbzXdOzJEcFrZUyFRU3lTbgwQDwWAjCouk9th_0-hc8YBDlgmHDlIdmb0hIA1zGozQVUAQKxTQy6eu0N9bJHrs9c7qmeRH_MjJHJZw3xYqOaEBco6BLTRBQAFLLVRywZM8D1MXQ00RZHYuc-zGPd8G4c7uy_MI9xsDVB7crn9iGiUh-DoldRX8MXTAhfJXOmhsIs2xM52tcYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fcd4c336.mp4?token=UWepxLzA_coLq5LGXCZhC-SnoKNdmqKo4LtHYp7RzD7A52Qt6Jf0x_luW0vE4S8Vq8p6V1zgQ5Pl4ewlRiL3rJ1krymy_rDsYe1ICr400JPPyCkWm4lZ_KfGK8bODLA0zV8A28vQ0SdXh6GnUDXaFhEoFUaKRUArB14j2FlQPesVjFl18bvgNAYE_dO9eRbfhmhsU3U_W5PGdFr7QttM0Jm1UlFWJiBGi1kk56iaoSsVJ1XktnJXtiQ-zOkAglGJ0Dr7Kp9lM5FbKz2JUce2BguRkKECVQqcycZpkXtxM9qpciO_643OsDwqJJQGhWcjnji83_szRMapBUgKJ5yJPIOYJdhjQ-ODgyLZkJw2_VqGb5vUkquacqcE89GWQir0oeM-XbZ76dXeHCbNnUUl0SD3mBwCtCwt5Ruh7aC5TgmGWTMORdt8-TPxUqbZA2kBxEWdR3AmkvIaq1mGL6SS4CtFh83pgvYbzXdOzJEcFrZUyFRU3lTbgwQDwWAjCouk9th_0-hc8YBDlgmHDlIdmb0hIA1zGozQVUAQKxTQy6eu0N9bJHrs9c7qmeRH_MjJHJZw3xYqOaEBco6BLTRBQAFLLVRywZM8D1MXQ00RZHYuc-zGPd8G4c7uy_MI9xsDVB7crn9iGiUh-DoldRX8MXTAhfJXOmhsIs2xM52tcYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبر انقلاب شبیه‌ترین فرد به امام شهید است
صادق محصولی:
بنده توفیق داشتم چندین جلسه خدمت رهبر انقلاب قبل از دفاع مقدس سوم، باشم؛ جلسات دونفره و در موضوعاتی که مورد بحث بود، خدمتشان باشم و از نظراتشان استفاده کنم. به‌طور کلی، برداشت من این است که اگر بخواهیم در یک جمله بگوییم، شاید ایشان شبیه‌ترین فرد به امام شهید، باشند.
🔹
یک بار خدمت اخوی بزرگ‌تر ایشان، حضرت آیت‌الله مصطفی بودیم. بحث رهبر انقلاب پیش آمد. آقا مصطفی، علاوه بر توانایی‌های علمی ایشان، در مورد زهد و تقوای ایشان مطالبی گفت که برای من خیلی جالب بود. ایشان با عبارات والا و شایسته، در مورد ایشان تعریف ‌کردند که الحمدلله به لحاظ تهجد، زهد و تقوا، درجات عالی دارند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466295" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbewat2DgO3hMiRwKPhKRuliDtMTyDw2LqL9XplAENIoPbQ9P7TeF2gs4rB6itibgMLyCG1OnYj_tud7KeBYJtjGcL1OIaRTS9AHLYWP_VZFnSoRGxh4XUEGgN0Q1Tf5Bi1LzSX365TkbhWeGpSX15T36EU-ioxLvPwYhkiEYBQm96jwI03sFLlWVqFkerApYbXe3b2fW1sccGkIXcXX-qYZnUt8A907NUZmfJ0XKXqSwlV1rUQCkeehMUYaqVMK024zGod3q5AHVy9aIYdP0GfOnQm8QBWzGSwQR2VaSA0SApnLFi6hegrk8CY9JhCfkPXHkOBROMUXh9p32H6eaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فرار نیروهای سعودی از چند منطقه در تعز
🔹
خبرگزاری سبأ یمن: نیروهای وابسته به سعودی از منطقه التُربه و ۲ منطقۀ الشمایتین و سامع در استان تعز بیرون رانده شدند. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466294" target="_blank">📅 19:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGMGQNlGW2ePYEzTzDFL9vfpqRWoarL8LSNo5NrVB9LqD3ZixvaNQC8rcxb7whGrc5xipd1CPKqTvRrUhA7f41cnDdSHnBKqBV-F63Mw0RRUmRdi_tNkJ9UTii-44XJ4iMeMRFu6HccEClISyl19S-mTJ5gpdCKSnJRgZ7rE1l5_RPnXJsiGlMRiy4r7U2IT5BgWGivLpuKQZv28x1US803CjzDP01C-HCFH_TQPNENrrNjXLClxfHpsnkzPz4nD1x5lMuJjXmvJF_MWfipRV2tMueJn8h6vsWrGtp4v53DFtk6EQ0HH_Wg0q3xa-M0OHi2qQZGoVBsW-PJdDWxvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قیمت هر قلم کالا و نحوۀ ثبت‌نام در طرح «تورم صفر» چگونه است؟  @Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/466293" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5w3apwYkZW2OodK77wWzhp8K_EaJTPrSNO6XjxVjAZVyfFq4cNOsIA49WfX8GD6mYxXF7o7baaRT7WYaVaCdN3RyDjqetXP627T7GPgRTaeTdvKjmYXtzT8_epg3WBUeWGcj7hG1Zgjq5RnkPsGDekGeYFcZakXu5A_hNi-0CVduddkCwergSRuNdm51vL5XLVBUKZXOss560n_bG-Sf8SoyGpeqbxFmP7ko2F-2-juEsHVcUw6tSCvWVHU9FnYDeEaVeDE6Ik9sB_vDDsZhYTmOWHezYsAHavVEpzE2Lyv-XuhvqDvEG586ivIVuIEO5nJQlYVfXFv2TgKCdlihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برف پاییزی بر دماوند نشست
🔹
با ورود سامانه بارشی و افت محسوس دما قله دماوند برای نخستین‌بار در پاییز امسال چهره‌ای زمستانی به خود گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466292" target="_blank">📅 19:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c31larpnYS91ESl9QYNAWTofjGPRqDVy8YFc5uGc7vjTleBNK95Mk1Mbs06OqISffeXfg5EfREFmMxnUi5ptbAXCawBbtaQaqQnFNKG7o7yiPta437KkLgwkh9_gQFNWF6lXEY9LqPYGyl-giAMS6RuM8cfIUVTA2lG5Du0qetyUyNL1R-0YCcyeXT9ZYv28GYuZl7FzW3X5jaaTe3I9r1jC-dExF85JO-SN4TxtLf6mrgW8hgl1dsvuRKNa5J0YEk2nnp0Sparxfl-Ntlah-cNxCtURonk_zNxuC7Nz0WlRXZSD6U4rh8IKHpmRqYau6PBgtEsU6BBUeCLYhKUK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5rJ-cGYsw7FJYKizACLHk1L5nUuAY020ZTzlfjxm-BUoxgJWICTBFOTS9hktxJ73KKJtgcaLK40gekGettoaHH2IU2eZMKGaPZdEoaeqPUuIJEF-DBngMWxBTQfSIyUTSgD7_0yopV-FJrzVH_vuMYIO-pWAEy79juYLw1ad7yldBh2OR85saByJUF5PMjdimRz5hO1usQQ0ffDsOCxLu6e4XSE65TtS6XikKRPynOhCAqi9XdOdvHetvaJ4Hr9S6JCX09XAeGGPuPn9PHyV7YmYMaAdhGwRgyqo1jqRfo3dvu8OT70rKt4L-GMgL400OFldr_sP2HPnLt-Xz4G3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaAunHJhaVv2fofzha5GkG0oKTvxMOD1Hjv1ESCiS5HiLD1tyQrP54AXWbqW7Wf98cRCpVdkl6CnP-Bwfm5cU-L_FMuMaOfIutrVEF4WWSuCOdQQKEwmLoVeL3ci1W4IFAFVDPyr5-U2r2qAnvGUn1fvXApzLB2kN2zDaFlytS7EaDqCA7T4MOfevvopTODIOErBYrTcCqAqHv4XIliOCPu4ydurNsA01DBMph27ChQDLVY3dVfodcc107LdMuwtsMjdupGxxeM60ECqRMBc4TXilhb7vf3fh4iQMJkSf0mNwkbkMkx8jYg9cph3HtrdzPIPwjFfbjFKkRyqLyudRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2bzZYTNuUlLq8tf1RrrSZ0DE1vqq31Bsb0mcSGc7YxODcr2pp28LvRUuYE1rsNqGsVsIg1VOdqamBszx-VmPo6iDRzw0kA0UIco6gZOcN3JhmogE4rWK0AnkcIdoRN_Pl5dzVtMUFztcHa5zEQqwM-e7IUfGuneDIAKO4nUp1narlGUjWcjGH7Aw3eQBTMA5wWbEidmjdE8D5kkg40U3OCXwnj_NDfwllHIC9jUVxEcHXqymn2ZnfqCum9My73XMYii8JoIoYxraNk04KvEK3WL3WX0dwWUXkZmvKwb6v8kIYpSPZ0FRhEjz6NDw3rQMGHm8jzHHg43aNNw-GW_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H29RxrYnhVsrxUvvs7Fhjruc2KY2pzIFIMYrHyTC6ahuabV-1p0vAdPPwHm3zBm9AOV8kEwexuf68uAICi3zrKJdx6ILne3txH9hLL17AerkNqppg8zPqFORZ4lt-42TJEcsX3m8j4G-vw9O2_HpMWwpSCJ17sMC-kCfEFoCtwhhnsjrxWEJH1OMNTe9jtThStwJqg2utP-hr8XdrKjhG83MOXRtn4szk5FQGTBJDcO5_Psi7FTuCjwiUf1RnCWzwpY3Qi4bQa9C7gadLxykZgLrOHCvVoVixcsuw-eiq4HCWN89-yS-WPq77l-Jq9KzOaHuDDa0OmZwutwEj-ZPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq6Gk4IEk32tgcWiqorOESdq6615OWYwG1mCnwA9J7hx0Q_4lr507qAtgc0N3rFrAndDzcYf9AW48Euu-Ge-oJoQ-ek0PxfoSykpuoYI8e4o0ecvWtFPiFncdP-tSCXx5OVKleBcygxYo13lWDt8vm4du-FqxV6VIpLZqByftLNOCF8HTQKDouUb79BmSnBrMsuFnDSec3MHS47jqs5cePEYmUEY0jTaEecIubWFi_7bEloyN-UiOs8Pom4hGo_I-HQ6cFFiiTbIKcu0zbJd00elDkidVh6Z1tPJXM4-aL0D3fyvZKxno5nN_CSyFVxjZ_vyj-vmBGv5mwemiFQmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ly9IsHOXdRhMraaV76Ww1Jb5FBs9QqEVHSDL8WuVYIBgQb7kpD9oWX9CC73JT7gndWxDE81WL8vOvkly2GE1S9st9FUeoSN_QLtoHx64X44-qPKlvIeVDj1lZx5-qQSz1l9zC5VFHttJ0hdRnmslOHuuQTewp2u4P9yTfF76j0s5-R5HqTntskX-RdQ3LaqPEK0KbNbI0-7vLQDZTIgkhOkDm9tnB2z-r6WF9I6AEpW5PggT85rGAlXSKjStss5S15RXzv_PRk1oy-8BHA9UQfZU4W1spVJ-9lSzIcob2MrtQgvQpPVEqIq44kkyCBrOXPG-sPuab4-v5hNBW6wucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHhV6qWa7fXNEX4yNXU9i37K2AuIoXoXMnXYt0dI8qfNaR30_rRuIxXqWqMmP-FnQMzLGTIJ07EAyZ1iOC03Jecopmc6ZNFg69DiM9gYslC9WqZSFiCX4KdEOlfuXrIuQGKEu35vSyX2nnaNNkcEuVdjM4E-5gFSds2QPmJMc7Lkwgr-ttkyTrNnsjHq07fhuUJz31WoZOoxqHB0zmZFgJvsxfx33nDsj6vafAxle2XVW02wnvx3uM4VdGjnFW0EaXatWTHS472qY8IwEOMc8EgsRb7ICrn7OXI53_M1gCwjkuF_NbrZmZveY5046QH1FwJv7Ou50VZqtX8sJUa2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVGa9ZXi-R3nTXWSru8BFySn5gws1VnytLUZ8O4YfLnbCwh5AwTejyRp87zLN68kbPWn7WLtB1nP0OhUcgVOVg181JBLmykRIL8Fueps9xFTSQjgnUPJtSe77i_gpXUwQqZQ2-eI_Wdw7aCF0XBhnNGqYWTLiWo_5RrKkO-uQeJVF1MJlWOg71aHzQpjIRJl7hPeALuoIBDRgAWnwO4kZgB7xtepksniMRW1two64K-FPETj5Cc-arKCvVEfCk8pUeXTt6d_FG39AMpJ6vMNMNz6YCowmpV4KD1srV4OZgcqnqa74nRYQ-egtQG3FE0qv-DFgUFlfRFC3zFwN7oOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGulOsEZUDTI8NQGyTXW1rQfJ54Qr6UDZ1zGYgUFTTz8IiavsGKQXzfALQ6C0Yjobu5b0rTaLvJvWPewjrbzOCt6aAB4I8GmKJwbcFDqpJfWQycl0RTtXu8NpnEDDxG6o8xWntA-f56PdRGL4xAD5BC7I4iOSWgtwHyUkNwKoGaqjO3bK9WKA73xzRVSm_wrEqj2QgXa19KgTVMobB2wyAk07KuzmR06FXWuwccHsB_5P7yjaOH5tEuRZudL5tD-FUPN4ZR87djr_1BnpAAvsr2doHlYlAv8rfF_kIVe4Oh2FtvR5KAzARPbv9cSdwQIxJYmRFthVbkpLC9OUv26Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏋‍♀
استقبال بانک صادرات ایران از قهرمانان وزنه‌برداری
🔹
قهرمانان تیم ملی وزنه‌برداری در بازگشت از مسابقات آسیایی ناگویا ژاپن، مورد استقبال مدیران ارشد بانک صادرات ایران قرار گرفتند.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#وزنه_برداری
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/466282" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAy5B7Ot68AgVrkgEiCIEf-f6kv7zQ48tMk84nCTyhc9XSpm7XM2HTSJf-kjLrIlZQopcG-PU0V3AStIP3XIk6apYbJr8FuJ3HhBpshWjN_0JClIakvXIe45VeLHHvf0VJcUWLN5Tukb63TwseL01ye8Tm7fhd8prrn6upUhRo6KkkPjSaIJKsM_11jJlCgZBvTwE-8hGTAz1sl9U41XHJ1Shec_B3e6L1aBiJ7jiV0VVEv0-GTeL815_2mlz-kblySSj3JMKOiCh71ctOS5W8h48Bc2LUK08bPySd5AQumsQNuxcZOj2TY9ZmI-wFqn_yAh1R8knVhIM2xFw1dkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای بازی‌های آسیایی ۲۰۲۶ ناگویا در دستان همکار
#بيمه_البرز
علیرضا عبدولی، فرنگی‌کار شایسته کشورمان و همکار
#بيمه_البرز
، در جریان رقابت‌های کشتی فرنگی بازی‌های آسیایی ۲۰۲۶ ناگویا  به مدال ارزشمند طلا دست یافت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5106</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/466281" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/466280" target="_blank">📅 19:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2014acdb2c.mp4?token=kG-dLnXYnrljLqMMB4vZAF1VYZuW-sOPv0FLqBvBhGd83JsU5YR-qo12KQqO7TtW7zORcdu6O_grm-uIwSN6DdsuDaPBHmzTebqyY0e57dBxOOyJSIxfs8PHcgKaeC6N2tZKdcHnORn92b7ej4owO1FxscdahWFBM1NVBxAL3C2pVhZf5-XIlv8yhy3D54tZ-77UbJTs0cE09r70JiNw1wR4HarzmO8D9u69gEEY2kyA_VNzw1wonyR4rCi9xhnvrhqffTctq9FPZOiewgMqxW2pMIMW3M-5JOzeQ1KVspR5QeP-YTfAExlME4q6AXMxRmGF3wQTebg7veuH1nnDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2014acdb2c.mp4?token=kG-dLnXYnrljLqMMB4vZAF1VYZuW-sOPv0FLqBvBhGd83JsU5YR-qo12KQqO7TtW7zORcdu6O_grm-uIwSN6DdsuDaPBHmzTebqyY0e57dBxOOyJSIxfs8PHcgKaeC6N2tZKdcHnORn92b7ej4owO1FxscdahWFBM1NVBxAL3C2pVhZf5-XIlv8yhy3D54tZ-77UbJTs0cE09r70JiNw1wR4HarzmO8D9u69gEEY2kyA_VNzw1wonyR4rCi9xhnvrhqffTctq9FPZOiewgMqxW2pMIMW3M-5JOzeQ1KVspR5QeP-YTfAExlME4q6AXMxRmGF3wQTebg7veuH1nnDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتوش چهره تروریست‌ها در ۵ دقیقه!
❌
رسانه‌های ضدایرانی سیاوش جمشیدی را با دستکاری و حذف سلاح از عکسش با فتوشاپ «معترض» جا زدند.
✅
اما سرقت، کلاهبرداری، حمل و نگهداری سلاح غیرمجاز جنگی، مشارکت در آدم‌ربایی، تهدید با سلاح گرم، شلیک با سلاح کمری و اجتماع و تبانی…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466279" target="_blank">📅 18:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJXPsy0YB6nksIZMa_fXOpcz_qIxnGJ-SSE_PGS-u138aXIwA5mM63J-2zu6iak38c6jYQMLX74hniPtMbwmlGBzht07Zl_7d9wen6e9sZPVRPdrphA_T4y0OChTh-IC5yg3KP35_V3eV5A0wyLxRuCugjjVKcdLHSurh958RlOqkmsUzTPyR_kcaK4gGbB0o8b73XmP_a2F5WsfrGisg-oLxFW0PpfTQXM-1adxdp75x0HD-lhDmwn5ZUi_YHb07Msqp6K8I7gYhbh4-XngePV7bivcpPFgZ5jaeT8Ti8p9ZNQvSW90l1xPPL1Fc8PgoMI2Pg8wYOJTbf5kw0ZJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت: عمر نیمی از بیمارستان‌ها بیش از ۳۰ سال است
🔹
مدیرکل دفتر فنی وزارت بهداشت: بخشی از زیرساخت‌های بیمارستانی فرسوده است و برای افزایش آمادگی در بحران، تأمین اعتبار و تدوین استاندارد ملی ایمنی مراکز درمانی ضروری است.
🔹
درحال حاضر بیش از نیمی از بیمارستان‌های کشور بیشتر از ۳۰ سال قدمت دارند و ۴۱ درصد بیمارستان‌ها از نظر ایمنی سازه‌ای باید در اولویت رسیدگی و مقاوم سازی قرار گیرند.
🔹
۴۰ هزار تخت بیمارستانی در دست ساخت است و برای ارتقاء ایمنی اطفای حریق، آسانسورها و اجزای غیر سازه ای بیمارستانها حدود ۲۵۰ همت مورد نیاز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466278" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تداوم پیشروی‌های ارتش یمن؛ تعز در آستانۀ آزادسازی
🔹
به‌گفتۀ مدیر دفتر المیادین در یمن، نیروهای مسلح یمن در آستانۀ به‌دست‌گرفتن کنترل منطقۀ راهبردی تربه در استان تعز قرار دارند.
🔹
کنترل تربه می‌تواند برتری آتش نیروهای یمنی و امکان محاصرۀ بخش‌های باقی‌ماندۀ…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/466277" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBrkdz1poOvlcfMOJoVESyB3b9Ad2LudcIIcY_adHFEze_4BIOZrookb_TPEOFLdT2DomSk2e5i9pP5COJMrXyalUHk5Y8-LWjH4ulYIpImtlOpDvl2IvbuRLv7oWMOpQsGjFFuA7aITZ9TLclvo4K463fqBdeZwUYmVerw3Hzv7IM9vBe7dWn8X5Nh5UNr1619d0srZbXZ4WCiEBCv3jBIdk6uGYH98QbgMnafscOJnlw2vv6gzmONhsFd05mll1-AxAZEKoytuy7hDzry2SPbU2qQj8yR5084KH1ZXw8_IrBd5V9ucy6diZqFfnkEI_4gq4ZivwQxAmy4LpfJQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه ماندن خودروهای گذر موقت در کشور هموار شد
🔹
براساس ابلاغ گمرک، مدیران گمرک در مرزها و استان‌ها اجازه پیدا کرده‌اند بدون نامه‌نگاری با پایتخت، مهلت پلاک گذر موقت خودروها را به مدت ۲ ماه تمدید کنند.
🔹
این اقدام هم شامل مسافرانی می‌شود که دفترچهٔ بین‌المللی تردد دارند و هم سرمایه‌گذاران خارجی را در بر می‌گیرد.
🔸
پیش از این تصمیم، رانندگان پس از پایان مهلت اولیهٔ خودروهایشان گرفتار یک بروکراسی طولانی می‌شدند؛ پرونده‌ها باید حتماً به تهران فرستاده می‌شد و پاسخ آن هفته‌ها طول می‌کشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466276" target="_blank">📅 18:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqvm3Vji9ndERgNaK4RR24F6A0z_OfIeQlbypJGSiGTe45ExHZ42up0blORAV6fKstKJq-M5wgeXPos42M0D0wPJ8QK-8880mKnemuX9E1lw2RovmnOqneuFjwwPKdA-EngqELqG8Q3Dc7oRqML8bCRbPWNjjN1-OvGSmREzLgqX6Dry131B_PHaLW-eua65LgXfQ7DbKwFit27C7fceIpgZMMmKdsBXJCcWocA5esBOTDAkRI2i5P9eDpyOh5pidKUVOmoo6ahRqgx6rZHMC3fZFNgjl_KNnusIpb-zH5LQgczGKGMbaN6U2h6H768RExJGvLiLagYYvOE4QdznRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر رسیدن آسیایی‌ها به جام‌جهانی فوتبال تغییر می‌کند
⚽️
کنفدراسیون فوتبال آسیا درحال بررسی راه‌اندازی لیگ ملت‌های آسیا از سال ۲۰۳۰ است. این رقابت دوسالانه قرار است با انتخابی جام‌جهانی و جام ملت‌های آسیا ادغام شود.
⚽️
در طرح پیشنهادی، تیم‌های آسیایی در ۳ سطح قرار می‌گیرند. در دوره‌های هم‌زمان با انتخابی جام‌جهانی، ۶ تیم برتر سطح اول مستقیما به جام‌جهانی صعود می‌کنند و تیم‌های هفتم تا دهم برای ۳ سهمیۀ دیگر به پلی‌آف می‌روند.
🔸
لیگ ملت‌های آسیا علاوه بر مسیر انتخابی، قهرمان هم خواهد داشت و ۸ تیم برتر سطح اول وارد مرحلۀ حذفی می‌شوند.
🔹
این طرح همچنین شامل سیستم صعود و سقوط میان سه سطح و حذف تقسیم‌بندی منطقه‌ای تیم‌هاست.
🔹
ای‌اف‌سی برگزاری یک دورۀ آزمایشی در سال‌های ۲۰۲۸ و ۲۰۲۹ را پیشنهاد کرده و قرار است نخستین دورۀ رسمی لیگ ملت‌های آسیا از ۲۰۳۰ آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466275" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۲.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/466274" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۱.pdf</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/466274" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466270">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHoO6cLiIheZk7HBTE7PoBWgxAd-HjUWQ9PfFARj4_MRwkprIiR2wDFSzUWlr3eiq0BoDiQsAOUvjkQh3cjoeqNu8WJWENA38_v4lG7uK4H6IGUu0DoVWfT9YSEott0JTJlVxWjqfnJYmjHgWoik5SphyNZJE3jQ8yWthC5TuonfrgzyD7PUOWdxC_WLqp4U4zACLUZYOSCQh1b39AWQySwJNc0VihHpIIPQOwax9e9bpI5bJAWDIHFGMPtp6Slh-fkMfts8nLjblxlECzZftpSg9sltw4_p33RumXNxADD9X5_vM5Ybh8qNF8leSWk-GTXOT513Pk9DsrZH8SG4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcihaVWjfiNWkd7qICzJfmtwNT0vrRzgY0yd_20Y9OK8QlgInB4eKQSOSEYk-6wc9REdfXegsm9g8ZtahSiTUSTFGtJ_gOR0EmUwmC9HgGeSu9sH5ctec7wAvhk0LgSsscmNBe6fjtE3XUp_ubsscF_TOT6y-slEGIKDfeMkf__8EJTzOMlz-LO-PchSyFH-wG7K1NRYENlrc5-QoTm5AYbsrSTdZlN-q333Dl_ikyiBgTo_qB_rAECW8EG7lkuBNLCb4I75W0ccoxnuJ33Cet7d46TmJZKbua-l77SZeVnlGKaU_0GbtdlJlDQ9cvyffzOntwA9zEk5Q-61nasU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ifg7XdEqGe-kNv_Bu-SoLe7Yw8glDok1XhpIZPu4vfBuHT39hoQsw4Ty5hEC_8MKQ8Z-FfjJJsyNfMfIMuptPMar0G-PsEinbR3KEDD7-d9ZWjG0hj2WTfihnn-OwBeyoKff1TRaiebU8TQPijqZg6O-a-Q1WSjvgs3rdQHv3ufgtLEpWZDGMDH9koU_hVacf9fJANjJxLeDGAviZTdrXH6BkBauIwWw58CBVXKyiDptgBZKl4SPEP3qTTce_Em5M2MFZFnLwvmZ91KeZziCK9QGZZL0lXedOXQPbTd2pd3WRnfersj0rljhtgBTkWCc9LxjeRNdO5PEmgZ38XdV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yea1T4ERDZ6p3kfL6Xkgsa1hXR9lJh_9mcvHmml1BGirccqqli4zhksJGB5jQ21rzeFod1sVWd0Wog1jmHf7oqSETkGYhKY80C67Rj_MPAJyf1xZiFvrFRhf6hP6nlID-W8Ngu58zS0rbM_jX6A0BzprZwXWxyYcZl0VpoZlXeieYjsTyqLVpD8_7ZgzBSEs5tyU1-kLRiwq1ylyn38RgSL6Cylvjud7psH7zUzFV06d6Sq_r7hrUatAmLN3evOYBFiyLCMZ6OPzZ1-yAdF-yfqIc-vqFzWKq01RBfcgADL1DQqYt8gXEndJrDctwOBZ2JqAV23EFVuxJ_DN6DLa8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رتوش چهره تروریست‌ها در ۵ دقیقه!
❌
رسانه‌های ضدایرانی سیاوش جمشیدی را با دستکاری و حذف سلاح از عکسش با فتوشاپ «معترض» جا زدند.
✅
اما سرقت، کلاهبرداری، حمل و نگهداری سلاح غیرمجاز جنگی، مشارکت در آدم‌ربایی، تهدید با سلاح گرم، شلیک با سلاح کمری و اجتماع و تبانی علیه امنیت کشور؛ بخشی از کارنامه سیاوش جمشیدی که روز گذشته به سزای اعمالش رسید.
🔎
این اولین بار نیست که رسانه‌هایی مثل اینترنشنال، BBC فارسی و منوتو با انتخاب گزینشی یا دستکاری تصاویر تلاش می‌کنند تصویری متفاوت از اشرار و اقدامات مجرمانه ارائه دهند. زینب جلالیان، پخشان عزیزی، وریشه مرادی، رامین حسین‌پناهی، شتاو ساعدپناه، نوید افکاری و... نمونه‌هایی از تبدیل «تروریست» به «معترض» با فتوشاپ هستند.
⚠️
اما رسانه‌های ضدایرانی در این کار سابقۀ طولانی دارند.
نمونه‌های پیشین را
اینجا
ببینید.
@Fals_News</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466270" target="_blank">📅 17:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nt_amRuiTk3GpIaSkkTFJC0bJeRSt_QwtUnegV07v1CofEyF9dW8sDtphHI2Ib-_HbFt7PHl1HcF_nPNs3FxP6_T45fQN8QmRlrR4Em-_eboxJS7i68u0-3WzfBi5rQF1Vwo3AXiSecdSYioZM4yhW087tMArp8nsJF1vbz5HhQoNIH8Wf_KwsEX1RzgtugiMV24SSJyn_FfWabWE1mvSb6AsAsecZ0U4S5ASRVr0IlQ8rvxsdBhGJbNfh1Nww8lmVN_wPWoC8RG6AU4o9aGCvd_Ll5NacKz9WgMA78ZLu1x0zxZeynbL89k8nGNZuvnlezD993whRVETrGp0pMd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn8R67gKNCe1Ts_9271w1PL-Aryde-2yT7Lv7FI5tAs_6GQ-Bg9vEhxLN0I8jGF4oY4jZ8LoguNE4sM9aGPKK1-yOCkNvlNPEbw25o3L_irXzTzXMvnQsYQ-INExlw42yF7tR2SvhIroMNIkgRWFeGQlYnopJC-GT9E28ARubbI1LEAbQGdM4Pk12CyOgZPGUUBhB0hYA2tRYGYuAgK_OzLDOhTMf9NQxWYlVhXsrXIQg6eyEZiA03Cw9cTOCf6dPpZ3GLVX3mYK7opfQ47ybhSUbZqtEUYq34YfXLTFloA63LkWFtqF8Mdhf2BM62Poris_Z0PguvzYai007X9HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHF3M7mC-8y1WSCihe2OEzo2CtfGBhbIMvU0zI2uj89im5VUEVYTVkYbXzhJ1ofg5EmYDxEzwUEEQkvb8erb8TSHoeeXha7JxPT8glBvCpzF7C5OznO3rTjKfVna5fCurYxpfX0_jTWyThYB98I3U9BJW_p9aKNw3ip2zHuo2frRIxDvpEKKvGW8CWg1gZZUCl49AGUpIITUS3HCskNQq0rKgqsu-R5gVmSlfmOH5RBRNN76WdwppCOIEAEbA8pt7qT9owOTYqZExt4r2ter7-G7ThwfpOj8xXuyTa17yyZpCJYvdNPOtT5ABl7U5CdTVo-1JWDZhBmJagKl1by89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsSgxaiKswnY_xlODJQ8zRl2Amu7HLmeZZ0GkpQVL9uQwIFHW7gAq3HkpB9L7gnIQIB4KXyHCzfiF43dTzXnfJrHYiHySjMDUDk0DBo8rL3XrUCPs707ICMIr-e2oyzlMzeRnMEauj87I5hOndyX6EliQzaJpnwqq7wySzVuBiKPBPcitQyCIJFPZtbVQxwxY_duNQ-bPXDWPaa__wmk7M21zUBh2mlncnPTim85Kmq8mIj0_QVziGEa8eQfrJprHMJ91Kk9G_atY_qBtOgoQHEtcqOFVjufSCupLO37e4EV4sG2iiqATvh9v4hQ7OrBa2hlQD2LnFfqvCwXku10sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2cI-QK9-5OUJZduL6Q0Ihqix2O8-kqkLHbgHDeP8CwqI6tWdv9pjaVERecw0NK27hrl2UeSkf4qSXeF6lHZa2Tj6177qCv80fEcXpGjvLp6vKT_2fQF0qBhp92aIGJyUqQEUUqlsVtE9Y68AO9wGG2qFR79gKh24LHgyYatEcSy1l6p41RbK3QUkhfz-OjoCaja782sp35rmffSW6a8ssJh2psP_WGLYISaYLU2SGuMtc_orpCdS6Qlv3Qz0tdWwtDylBKloXtApgWZmJ-YpASF1F8ZN5eLd2J6pgTSt3zbjuF3r4lSZa6NUNxyfm0kkq2WbUqTrr4A3TTGWTQ5gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
افتتاحیهٔ هفتهٔ جهانی فضا
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/466265" target="_blank">📅 17:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K37NL6M8B_2pDYUy6Mi-8HZyywo-oQFpnKU7OMOU_Q8pJEAy8z7PaXDAwvU3o6RInq8eK0bMAr0wvugj_ncrsGfKFoOgXq4d7x7h6tvpFEiFhNHv6o_EuCEOF4h2lFGka2dMUe4HtXNDkT18REeIl_bbnXVzb3qGniq3qD8IORb12u3_-Njo0JEf4LDcJvb0pZ7N34fVBtfIMuJcdSfwc1EIn6h2SKUfFVEn7pAtvKFrlRWN2LR7ncnTOrYmoONFIf8MV0xs1rMK7emHq4H-u7asHvPBbWeBLBfhV4-8GiLLsyl8Z01x6-Z28qtOp5cnL3jqHddG0c9q1ufn3o04vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پایان کار کاروان ایران در بازی‌های آسیایی با رتبۀ ۶
🔹
کاروان ورزشی کشورمان با کسب ۱۹ مدال طلا، ۱۸ نقره و ۱۵ برنز در جایگاه ششم جدول توزیع مدال‌های بازی ‌های آسیایی ایستاد و به کار خود پایان داد.
🔸
در دورۀ  قبلی بازی‌های آسیایی یعنی ۲۰۲۲ هانگژو، کاروان ایران…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/466263" target="_blank">📅 17:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol9G8QEAZmUJtgWRAYjk9UCEKi3qqxeX_mZmk_Fw5Cz1tTGYTarYcajHbJXAyaQ-pS026GiXoOErqajrYl3UA7Rqpf7-HD54lBH5BWAvAxSJR5WG0I_nHxfPp_-J6rs-XQeQCCxyngSm6ut8VQQFobuLZyvSvPZi6h3sIyAsQD5mvcQFpYmrtpc3KHpKQUDgCEod3_YxrYEvR6whW7qkjbfQOIXneMNyC9PdJBIv70Wh3NdvnI3msjHNHdXEbuyTEMnfPP-oZNfVndTLRR2qHLggLX89_IMcmIFuC9bK2PrwJ3qQs5tM0vl1KlksQoS3abmsTOyR4G7GZkaFZci_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار روسیه به آمریکا دربارۀ «جنگ تمام‌عیار در فضا»
🔹
مدودف، معاون شورای امنیت روسیه، در واکنش به درخواست اوکراین برای اعمال فشار علیه منظومۀ ماهواره‌ای «راسوت» روسیه گفت: «هرگونه تلاش برای از کار انداختن این منظومه می‌تواند به «جنگ تمام‌عیار در فضا» منجر شود.
🔹
در صورت نابودی «راسوت»، ماهواره‌های آمریکایی از جمله استارلینک نیز ممکن است هدف قرار بگیرند و آمریکا باید پیامدهای چنین اقدامی را در نظر بگیرد.»
🔸
«راسوت» یک منظومۀ ارتباطی ماهواره‌ای روسیه در مدار پایین زمین است که مسکو می‌خواهد آن را رقیبی برای استارلینک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/466262" target="_blank">📅 17:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC01Yv4Y4ep4PD8CBBesn2j_3YsNASYFW6UMkJWeh9H8UUCOOrHEB88FwecjuRLHqOUxUKJL0i8doWJJ8YKPeM8geIMVbtQbOYmuWy2awdPT-gkOV2hTPo2u6UtpZxM80ZQw9Fr3xHC6BbEftTi4SiywzTZmrbaMqZgdjDx8NYQN-GIWhHef0L-8FZJlaavwHddISWYrtodXDlJBsRIQRYb8Ru_uwuQ2NdxURibUIa3taAAW-Yi2xk9SLJc98xVS9awr5MtzV2TraUkZ9WAzNb-j-_KmiyDVTanH9nUfrv9v-YvRXIMm2IAtkH8WgehHwHtb0CsLx39clz5QwRAQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست شرکت نفت ایرانول اعلام کرد:
✅
برنامه ایرانول برای فعال‌سازی ظرفیت‌های تولید و توسعه محصولات پیشرفته
🔶
سرپرست شرکت نفت ایرانول، توسعه ظرفیت‌های تولید، افزایش بهره‌وری، گسترش بازار محصولات صنعتی و حرکت به سمت محصولات با ارزش افزوده بالاتر را از محورهای اصلی برنامه‌های این شرکت عنوان کرد و گفت: فعال‌سازی ظرفیت‌های سایت آبادان، تقویت تولید محصولات مبتنی بر روغن‌های پایه گروه ۲ و ۳ و توسعه همکاری‌های درون‌گروهی، از محورهای توسعه آتی ایرانول خواهد بود.
🔶
به گزارش مدیریت روابط عمومی، برند و مسئولیت اجتماعی تاپیکو، اکبر میرزاپور سرپرست شرکت نفت ایرانول، در حاشیه بازدید از پالایشگاه تهران در گفتگو با خبرنگار ایلنا اظهار کرد: ایرانول از ظرفیت‌های تولیدی، فنی و انسانی قابل توجهی برخوردار است و تمرکز ما بر این است که با برنامه‌ریزی و سرمایه‌گذاری هدفمند، از این ظرفیت‌ها برای توسعه تولید و بازار استفاده کنیم.
🔶
وی افزود: در کنار تقویت فعالیت‌های جاری، شناسایی ظرفیت‌هایی که امکان بهره‌برداری بیشتری از آنها وجود دارد نیز در دستور کار قرار گرفته و سایت آبادان یکی از مهم‌ترین این ظرفیت‌هاست.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/466261" target="_blank">📅 17:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466257">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2JPEP44DZq0TywxVfZ6j4e09ldTMXKTgd0zALK2j0MLTTYg2R_rXyAHZMOPBVR85tQYMmZ4b7YvW8OzdofBkdxK1ZVv-ayXQEYXrL1b0mTQ5QBDs4OeemSTlD-9Q-U4MUSlnb_F3d-vAghIkDhehM3HQmFjEXjbxRy2aKSZnD1p5sY_kW_G456qK1ftkmFHQcx2j-0_uMmtBdbdZCCuHpI9eglTEpqdrWLxLr2hrVseXUWO-sUbU6mxri7idF0shNn7hJDokjk3Oby3O1zORFaQHy8_4Xrbars67ACmdor7pygKqwVBJy9Q0R4qe26hrH9eLtGFlg8k5oeAxbiaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr-UrnfTrMialemdLISYnxHio40NE04bkJhov_Sh8e7SKoYUqcadhrkY98-tZTYj2BZYDEa5k67ty9jpDULtfwPF9MEwRwj4EN9DORadkYTQzLllyJ9r0fAvi4t8dyesSZ-JnCWjoDWh_cIMu-fGqTsyK8u5sEACfuviU2jf5gz3vpgUFPHfEjGudjQeDzcHZTi6D2f0D5_E6E_dHnHVpCAu6zr-3z4AEMlsZHXEhoMZVDGGa18_Vv_0pJ60U5YhT9YGo0pzKO5eN87JnoQ9zSOUg4aTkT5Q0i6oJLJEAEiYsP0jB0zXoIjGuRv0m2qogE-u1T1vEkqlu6HtCcusmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOWRihWWxPImW9buYGKKvaFyJJYcHvIMBWoIwimJr-FfwSGFg-Tp3ROd1-zad6-6k2iLq4RyQP1lwNJWzsoteqqw9ptWq3gw1HYLiTkOQkuolXuw6odTgCkrYyRdXVDS3wvbSdv2_zFnjvVq7U9kc9YIJal6it2zMKH01fMW5GQRwd96uu-yXtG1Bl2QbhOHvC54ASFmcTkXLHRQHZdi8RA05Xcg5SX5_XXHTd7cLkBczwZNMFad63lTkvaRVcHNiOTd17jcEPluOiTp75LWt4-1rptYtB1gchx5s5SK4iNUuRTwAvOXAjStZ1rGrLdiW4jSvc7_KSGcXYZ59-2uag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptEWBDs2BLpcCwRPcni3BFy0dNQhjC2qWZGm-4UkjeSUNVXACJOzJttkjetfKl1xnAqmCg5IMb7swB2VwACwKJZUBVKAJcW8BCWtGittvcji_91UkCxfQdk8eJsckP8Nw4SwsIFFWFhnMrkVjKHpsxK8gzedoHnCBOVUqMeK1N9QlqQFo2vYGkkrXWVFBxfELt8zdN4ck1kjA6vR9anYbfmKZeHt-TEnH_s7eQKVYYSxsM6NswPokJ8VhHzYUMgaX6c6stH3QYgZDcj0Cjz5M1OolmP-zWoNliwOe-XCI1ABhmhbkouiSNHD9X2jgRyPN_TyFuLJFRnTDGz-5lAhTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔰
بازدید مدیرعامل شرکت ملی مس از کارخانه تغلیظ مجتمع مس سرچشمه
🔻
مدیرعامل شرکت ملی صنایع مس ایران، شنبه ۱۱ مهرماه، با حضور در مجتمع مس سرچشمه، از کارخانه تغلیظ بازدید و آخرین وضعیت تولید و فعالیت این واحد را بررسی کرد.
🔹
دکتر سیدمصطفی فیض در این بازدید که با همراهی محمود خدادادی، مدیر مجتمع مس سرچشمه انجام شد، ضمن حضور در بخش‌های مختلف کارخانه تغلیظ، با مدیران، مهندسان و کارشناسان این مجموعه گفت‌وگو کرد و در جریان شرایط تولید و مهم‌ترین مسائل عملیاتی کارخانه قرار گرفت.
🔹
مدیرعامل شرکت ملی مس در جریان این بازدید، حفظ پایداری تولید را ضروری برشمرد و آمادگی تجهیزات را از الزامات اصلی فعالیت در مجتمع دانست.
🔹
وی همچنین بر هماهنگی میان بخش‌های عملیاتی و فنی و پایش مستمر فرآیند تولید تأکید کرد.
لینک خبر در مس‌پرس:
https://mespress.ir/x6TP
@mespress_ir</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/466257" target="_blank">📅 17:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/466256" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaO3VpCM6oKt6wclNIkigEoi9xKWf9MZeZIMzU2RR1jvZv6Khgft-8VUrx0qkJeKQauvvg34QBXUpjFI7amOH3J6Y5LO2UfrC9g82BcR8cFWtiss6eQoinVgWfL73G2Zs4qalMaRrl8jQGPByeXBgXUv-BRCmjjgJ6404hbEXPqblrPo7aIKiwPvfsuyrKQzd5GLYXjDM9NHdj8LZS8LA7yo4VYJHVaXikHTWRbOVT6rkpqdwiCvqVosbpS2LhfAHzZMBWUSbdU4uFQQXAeXLoJxZVR_ro0Ion7Z-EouKp7fV8YFJQB6GPEGktaaxvaheR-WlrcCaAf_K6YQsVSnrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی کودکان پیش‌دبستانی هم متوجه شده‌اند که ماجرای پایگاه هوایی «فیرفورد» یا پرواز فلای‌دبی خیلی ناشیانه برای اتهام‌زنی به ایران طراحی شده است.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/466255" target="_blank">📅 16:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc1j-X_FfdPNopOEBbnLD1jaHo0TXNSa_CkhjDsT7x0KGCwy-w74gH_W6PbAT5i7oIdxd7o723zjbCuxvXdpYoLaD_obGdXaDgHM3VFEdd9LP2hlZuioaveeNjzXIPcL4KhbBIapVmQovuIz0yqzrr1rqX2d5_2_xFfyJ793ww8asFkgeLXT1Yhcazl0ntUDX12njdj8Omeh71dER5AwT0ViT2sl2xYHTvxMDLGLA7Q94WJERjcf_DPSoeyIZJzaett2JQWrw3y_SwttJWYhhnStit9mjMX8C5YuUFXA3f6QmX4HDH9asVJMa-hVxDIg9Bx_vuyw4PiRwwAdV7r9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرامکو زیر حملات موشکی یمن رفت
🔹
سخنگوی نیروهای مسلح یمن: ۲ شرکت آرامکو در ریاض و خریص عربستان هدف حملات موشکی و پهپهادی قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/466254" target="_blank">📅 16:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXBcDp227dKPnHCrpwi_3m9_9sQ_Ty0_mk4pkBjFQnoYWE-fT2FX5N0esX78zf2ky0AGsU5-b90D8C5ve-N8GJ8lTc-7fDr1laihPS33qCtegV57sGUIJ5U7HDHyWk-wdJLGyOQYx33B6AoVQzoqJaRqXXvChVpCx4_b4g8XEj1ohJJMH26tmFftrVSGAkDGl3j2Hm1eOY6N5X6WD0hpdCIeXniWGLPVm-0aRt0_GhSLTmsiiJAySg8y79TXL3evMi86-9b5xd4dioju-4aNViZI8TNK95ggELn11_lmmZ2_bTiLJNO8-WesUffEWt7MLc-a-UUV7CWo_qZr_gNh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی دولت: آیین‌نامۀ حمایت از بازگشت نخبگان خارج از کشور با ۳ محور در هیئت دولت تصویب شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/466253" target="_blank">📅 16:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0Qa9tzchjrcvakqwhh6U03q9b2f8laH7mGMEy6MpwjtjEZ7dKjFK8wkSeWaLWZLtotxqyE6lmcAbgfxdmePqG-H3i49UNHwL_U34RcKKaZm6PkAPONnMPpRnqvYanQM5EU-4SNPkjYmJsT5cKoH6hNI6TkBk6Mu-Ik-WTEwRREhoXN_s1SNmizguP4QCEDx7EZHVt_ZPBrlbdD9Yqir5XRBbAEkPyFMu11HOytFjrIen1C3talbyHM_-thPobxXaO2ZeUo-KEYgdIpuAWGbep6Neo35abCMVCLgxSNQXhw2vca1f0sWgzUId-WCZ9KIjkuulfTRdhH0s2CqE8cNbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبرد ایران و آمریکا در میدان نفت و دلار
🔹
جنگ ایران و آمریکا فقط در میدان نظامی و تحریم‌ها دنبال نمی‌شود؛ قیمت نفت در آمریکا و نرخ دلار در ایران به ۲ شاخص برای سنجش اثرگذاری سیاست‌های دو طرف تبدیل شده‌اند.
🔹
دولت ترامپ با آزادسازی ذخایر راهبردی و افزایش عرضه تلاش می‌کند قیمت انرژی را کنترل کند؛ در مقابل، واشنگتن نوسانات ریال را نیز به‌عنوان نشانهٔ اثرگذاری فشارهای اقتصادی خود برجسته می‌کند.
🔹
در ایران، دلار به یکی از ملموس‌ترین شاخص‌های وضعیت اقتصادی تبدیل شده و افزایش آن می‌تواند به تابلوی نمایش موفقیت فشارهای آمریکا تبدیل شود.
🔹
بنابراین ثبات بازار ارز بخشی از مدیریت جنگ اقتصادی و روانی است و تقویت عرضهٔ ارز، کاهش نااطمینانی و هماهنگی سیاست‌های اقتصادی می‌تواند به تعدیل انتظارات و ثبات بازار کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/466252" target="_blank">📅 16:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cebc383706.mp4?token=rxTTxDIuuMlF0WhWOCb1FH0fDcKqlOHiNFUlDTUaFpVUH01Z-RTjolY9kV3eHPaaloqH1VkjJrDh7MG2lpziFZGIF5xaX5ncZ8DFEPDxSLyyQb-jrKj_gOXFBYPrXEagZ2uZsMmVnwbqSV8lAsnrPwAXTjuVGSd4PYnJxmPbMwwpisfxj2gyWiHTUOJ2W8pJLOfpWh66fI027JepRJVUnecDlnmjERtstCRc3qwi_WYqy3DEIS_nSxLpnr1ElYeBhgU1JYU7k9UgsO4q1YtXAADyDpU7u42R-o5P9nHClICvoSycaKOCLwnxe0FngfVXtvHRDNmaqJbphYEwonlfNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cebc383706.mp4?token=rxTTxDIuuMlF0WhWOCb1FH0fDcKqlOHiNFUlDTUaFpVUH01Z-RTjolY9kV3eHPaaloqH1VkjJrDh7MG2lpziFZGIF5xaX5ncZ8DFEPDxSLyyQb-jrKj_gOXFBYPrXEagZ2uZsMmVnwbqSV8lAsnrPwAXTjuVGSd4PYnJxmPbMwwpisfxj2gyWiHTUOJ2W8pJLOfpWh66fI027JepRJVUnecDlnmjERtstCRc3qwi_WYqy3DEIS_nSxLpnr1ElYeBhgU1JYU7k9UgsO4q1YtXAADyDpU7u42R-o5P9nHClICvoSycaKOCLwnxe0FngfVXtvHRDNmaqJbphYEwonlfNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطری که سازمان ملی هوش مصنوعی را تهدید می‌کند
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/466251" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdKKBZnWe807XnqttjXYujstYip1l8qbSfga4gB4wsFsZnUwehl54CDHqMyvuGrKluyuSRTRQ5dM5t_5A0w0lX8e1djWqcCRVe3ePrSOp-xvpOz5nvEfZM6zMtza9IzFzasrxWJwjqLEG8ZsQWkd0hWnLhJ8D5vQ7ziMn6_pac6q6p0ZLQ37YKB1atCTjaGAs5NeS9hM_ODn3t-0aaOxD5P_9tiz_NerQPM5cBFmf96cwu_LCZChSvTpEpTmhPf4Lk1ak8GDzWFsM5kOnbqVE-I1FtV4Iw9keG353vqyGzkzIo0lpOVHLlOEMAkq6MuTN3m6bb3zG1rLE4aMN-UQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگین‌ترین ماهوارهٔ ایرانی ۶ هزار کیلومتر تصویربرداری کرد
🔹
رئیس گروه فضایی صاایران: پس از تزریق ماهوارهٔ پایا یا طلوع ۳ به مدار، تیم متخصصان به‌صورت شبانه‌روزی روی تثبیت آن کار کردند و پس از ۱۰ روز، همزمان با روز ۱۳ رجب و ولادت حضرت امیرالمؤمنین(ع)، ماهواره تثبیت شد و توانست به سمت زمین نشانه‌روی کند.
🔹
پس از تثبیت ماهواره، اولین تصاویر توسط پایا دریافت شد؛ این درحالی بود که حتی مطمئن نبودیم دوربین ماهواره پس از اتفاقات رخ‌داده بتواند به‌درستی کار کند.
🔹
اکنون حدود ۱۰ ماه از این مأموریت گذشته و ماهواره پایا تاکنون حدود ۶ هزار کیلومتر مربع تصویربرداری کرده است.
🔹
گام بعدی ما برای دستیابی به فاز صنعتی، «منظومه‌سازی ماهواره‌ای» در سال‌های آینده خواهد بود و امیدوارم به‌زودی شاهد فرود ماه‌نورد ایرانی بر سطح ماه باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/466250" target="_blank">📅 16:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فردا زمان برگزاری انتخابات شوراها مشخص می‌شود؟
🔹
جوکار، رئیس هیئت مرکزی نظارت بر انتخابات شوراها: زمان برگزاری انتخابات هنوز نهایی نشده و فردا در جلسه مشترک با ستاد انتخابات کشور دربارهٔ آن تصمیم‌گیری خواهد شد.
🔹
احتمال دارد انتخابات در برخی شهرها به تعویق…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/466249" target="_blank">📅 16:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad175c275.mp4?token=ql8vR8qQlGbnrMeNAUYuuBeZZws-OA0X5hg8wpKVAzB4XM1RwnZUc48rYD1VkjNpUC7Hxc0giZrnaTKNLmDLO_F1alhym2r9uNm6780hwFE60Q033VczT4VjBnihT1BZxH0EQyBSX_SLuMw7gO4PRnUFMvSBztxuSEg0e-yUa5WyuSzLIHgBQRnBvFO3L71_pHT-ZD6spo-9iJlfiKNqmT7OMtSeNxQxvl_PD2NJe7AlfMZzjclOLulmSeHvpEvhdsGCBI-5x1jSy7Px60OMX5fAQ3E7qwtfK0tvDXbVDtd2yLnngUTq_cJmMYHAdO8geTFHVm07yazSjkUtxbPzUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad175c275.mp4?token=ql8vR8qQlGbnrMeNAUYuuBeZZws-OA0X5hg8wpKVAzB4XM1RwnZUc48rYD1VkjNpUC7Hxc0giZrnaTKNLmDLO_F1alhym2r9uNm6780hwFE60Q033VczT4VjBnihT1BZxH0EQyBSX_SLuMw7gO4PRnUFMvSBztxuSEg0e-yUa5WyuSzLIHgBQRnBvFO3L71_pHT-ZD6spo-9iJlfiKNqmT7OMtSeNxQxvl_PD2NJe7AlfMZzjclOLulmSeHvpEvhdsGCBI-5x1jSy7Px60OMX5fAQ3E7qwtfK0tvDXbVDtd2yLnngUTq_cJmMYHAdO8geTFHVm07yazSjkUtxbPzUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دارندۀ مدال برنز المپیاد اقتصاد: اصلاً نمی‌دانستم المپیاد یعنی چه!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/466248" target="_blank">📅 16:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466247">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملات موشکی یمن به تجمع نیروهای مزدور سعودی
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای سعودی در شرق استان الجوف پس‌از ناکامی آن‌ها در پیشروی به‌سمت مواضع نیروهای یمنی هدف قرار گرفتند؛ این تجمعات با چندین فروند موشک بالستیک و پهپاد هدف قرار گرفته‌ شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/466247" target="_blank">📅 15:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466246">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIT0C4MzG6_5odRUHKysdB64X3hbTxsxNqOCdqbhux3tzNLE9GwGyStMeuW1PGQj_l7soWubx8vHQA-gI4nXWJj2x_MmriUO3ZiEWLP7NmJumrE03Az2DJ_yYLOU_zN6NbPKSL1hvVXEF9Bcm6xoyA1vSxnByZhCq5C0DuMaBvSF8uPL6SiM29y3i_63CwA0lnWhtHmdj-MII5nsSRoDFDRl1N4T3dpo1qynegFqx1b9Fw7Dzp_namqdcdsmu6Tvm7egeaNpp53jX4eJ292NzW9p2WRlp7JpqE7SA-wp2wtq1uww9fKw0VGKkQldC1xOE5sS71ALE860ASMG-VzNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه جایگزینی تراستی‌ها آزمایش شد
🔹
بانک مرکزی تاکنون بیش‌از ۱.۵ میلیارد دلار از منابع ارزی خود را از طریق شبکهٔ بانکی روسیه منتقل کرده است؛ مسیری که طبق اطلاعات فارس ظرفیت جابه‌جایی میلیاردها دلار دیگر از منابع ایران را نیز دارد.
🔹
بیش‌از ۳ میلیارد دلار از منابع ارزی بانک مرکزی در بانک‌های روسی نگهداری می‌شود و این بانک‌ها بابت آن ۱۶ درصد سود پرداخت می‌کنند.
🔹
این ظرفیت درحالی وجود دارد که حدود ۸ میلیارد دلار ارز صادراتی در حساب‌های تراستی ۱۸ بانک باقی مانده و به‌گفتهٔ دیوان محاسبات، موجب تأخیر در ۸۵ درصد معاملات مرکز مبادله شده است.
🔹
شبکهٔ بانکی روسیه می‌تواند علاوه‌بر چین، برای تسویهٔ تجارت ایران با هند، برزیل و کشورهای آسه‌آن نیز مورد استفاده قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466246" target="_blank">📅 15:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466245">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ67gAjLoXXxayRAmki1yQs4rWDL08W9hMU-M9QD9tC6HTmEe9MkRBxuyPv1Ognu0I9YOGNywKB5G8oWC1fsfzU9G-4YpkfThdjQ3YT1kA1W2B53veAxSpI0-54vy7z5jf2c5ZSzQ-c2huzdxWLM_vTDnKf21lFl4OZ-omMuyp4xfQ7ydgk7M-fM9Jt89r7UOav-R-YqL_jwzAC7O2QH6e2sVSYGggNcDn5AFAOS-k05KhtSH9olBCIWhJBAqCCZos7O32Q6o9lSST2I64JgrOiwjp01d63b4oc4dRNSSoIw8BzninShBTbAD3xxGpozUzFAOPHUwhCV0DQhrfrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
در میانه سال دوم اجرای برنامه جامع راهبردی و فراتر از اهداف تعیین شده
🔰
منابع بانک مهر ایران از ۱۰۰۰ همت عبور کرد...
🔸
بانک مهر ایران به‌عنوان اصلی‌ترین متولی بانکداری قرض‌الحسنه در کشور، موفق شد با گذشت تقریباً نیمی از سال، رشد قابل توجه بیش از ۴۲ درصد را در شاخص مانده منابع تجربه کند و در باشگاه بانک‌هایی با بیش از ۱۰۰۰ همت قرار گیرد.
🔸
بانک مهر ایران به‌عنوان نخستین و بزرگ‌ترین بانک قرض‌الحسنه کشور، در دومین سال اجرای برنامه جامع راهبردی و به‌رغم ریسک‌های متعددی مانند بروز دو جنگ تحمیلی به کشور که شرایط کلان اقتصادی و فعالیت شبکه بانکی از آن متأثر شده، توانست منابع خود را به یک میلیون میلیارد تومان ارتقا دهد.
🔸
بر اساس برنامه جامع راهبردی، خطوط کسب‌وکار بانک تعیین شده و به تبع آن سبد محصولات متنوعی در اختیار مشتریان هر یک از گروه‌های خرد و اجتماعی، اصناف و کسب‌وکارها و همچنین سازمان‌ها و شرکت‌ها قرار گرفته است.
🔸
این موضوع در کنار تأمین مالی ارزان‌قیمت، سرعت بالا و فرآیند آسان پرداخت تسهیلات، ارائه خدمات متنوع بانکی و مالی به مشتریان و پایداری سامانه‌ها موجب افزایش تعداد مشتریان این بانک به بیش از ۲۴ میلیون نفر و به تبع آن رسیدن منابع به عدد ۱۰۰۰ همت شده است.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/466245" target="_blank">📅 15:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466244">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_2TtTq-3OmSJFmfrMixrR_OUsO9oGA53SmIfy7dP-QzZjv3Ho6yWBzOx3Vo-NlPvQ_G0iD4PBztaxZEJ9PGqC4yg_n4pKhfeePasAlvBaGz8ODhC1nnEcQ_FDk2jDWbVnBBjueF9A2SayaC6lozPq3mpbHtOPATtOLeGs9ASS7HFlEY_EXBu-kWoK2o0M6U8yorG_wqAOUdQXcVQdTK8RSla6-YD6YPoYhFGSktjP5EKePCMPyQ6ttjazxxC3lS2rYDtn6BzIDfTiLjnkvvFbEd0Y8YZOaXHGq4IAd83GLO1g1uVFB4B-T28KOZE7ZYqKUPvuHRFyxRvBOkP7F_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/466244" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466243">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/466243" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466242">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqiR1C8GcxOV3087YGv88Ek-bRPrTSS0bCbCGFU0mP11SG1D0pSpHWF7605ANBIovWDf6YUiPq-yeia6FqlseY7UdNB-QGFdy4B9Nr5RNJyMsX39vfrl-VU2zPNRFe0m0ta1QazD1p7Mj52tL4tmxjilmqQPod6K8wpICKlQrp6qApTDS25lKf11q-iX0KlJO-x3hz452R_6njtorF8CJnIuhKeNIrPxE8xgAU09RHIN-oXx7TtO1qE6F4F23M1nn6c4yv8hXfP2L2dFseIFkwxaEpeTJfzP-WnrBEDaML7uNKGL-fq5Hxm20vkcjMJJaU407bmHYqMrKla-px4mpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سرگیری پروازهای نجف از فرودگاه مشهد
🔹
مدیر روابط‌عمومی فرودگاه شهیدهاشمی‌نژاد: اولین پرواز در مسیر مشهد - نجف پس از اعمال محدودیت‌های دولت عراق، امروز ساعت ۱۸:۴۰ انجام می‌شود.
🔹
دومین پرواز نیز یک ساعت بعد از آن به انجام خواهد رسید و تعیین قیمت بلیت در اختیار سازمان هواپیمایی کشوری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/466242" target="_blank">📅 15:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzuXRlfCF_RPGOhcy1FyW_b44B-RKDWAWWcolO2IcrBT7sBQTlkOfjKt3HQy-mS69ogWMXRjlR_sIH-pdz2NyAiPnkL8UyRCj_8J2G5Z9oymb8IV1kbuR3tJUb4QfQ4zjAyvuvgWrIehTgtfzmv09nAIE45ItnQrrlq99rW-yGrSKD9jFZtcW8RUH6Y8_glL4ka4sxwD6qmrS2uhY8gd5Pmuei2gl_sqYfq8lanbal97QEu7ni2qgUC5kIaeXCks00RXn1_UUj-0tdeez88KTYH5ivo4aE6rL8n-1re-0suvxpn1khmIToc8s81uAclxZLMcomXcW0lEg3nZM7hQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال صهیونیست: شاید اسرائیل چند سال آینده دیگر وجود نداشته باشد
🔹
ژنرال بازنشسته ارتش اشغالگر با هشدار درباره آینده این رژیم گفت اگر مجموعه‌ای از بحران‌های داخلی، اقتصادی، امنیتی و بین‌المللی حل نشود، ممکن است اسرائیل چند سال آینده دیگر وجود نداشته باشد.
🔹
اسحاق بریک در مقاله‌ای در روزنامه «معاریو» تأکید کرد نخستین گام، خروج جامعه اسرائیل از وضعیت «انکار و سرکوب» و پذیرش واقعیت‌های موجود است. او جامعه اسرائیل را دچار شکاف‌های عمیق میان راست و چپ، مذهبی و سکولار و عرب و یهودی دانست و گفت غلبه منافع گروهی بر منافع داخلی، توان جامعه برای مقابله با چالش‌های مشترک در حوزه‌های امنیت، اقتصاد، آموزش و زیرساخت را تضعیف کرده است.
🔹
وی همچنین درباره انزوای بین‌المللی و تضعیف روابط خارجی رژیم صهیونیستی هشدار داد و گفت این رژیم طی سه سال جنگ بخش مهمی از روابط خود با جهان را از دست داده است. به گفته بریک، اسرائیل در حال از دست دادن حمایت آمریکا و کشورهای اروپایی است و ادامه این روند می‌تواند توانایی آن برای ادامه حیات را با مشکل مواجه کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466241" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کشوری که ۱۵۰۰ برابر ایران هزینه کرد اما چهاردهم شد
🔹
قطر با صرف میلیاردها دلار برای ورزش و جذب ورزشکاران خارجی، ویترینی پرزرق‌وبرق از قدرت ورزشی ساخت، اما نگاهی به نتایج این کشور نشان می‌دهد پول، به‌تنهایی اصالت و قهرمان‌سازی نمی‌خرد.
🔹
این در شرایطی است که کمک مستقیم به تمام فدراسیون‌های ایران در سال ۱۴۰۴، فقط حدود ۱.۲ میلیون دلار برآورد شده بود.
🔹
ایران در بازی‌های آسیایی ناگویا ۲۰۲۶، ۵۲ مدال گرفت و رتبه ششم آسیا را به دست آورد؛ در مقابل، قطر با هزینهٔ ۱.۸ میلیارد دلاری برای ورزش در سال ۱۴۰۴، تنها ۱۶ مدال گرفت و چهاردهم آسیا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/466240" target="_blank">📅 15:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXuqCAKvD25F6kCIouvbi01-O3INloNGpF3xUERGhdzRErnEiGXOJdemW5v9SS1wWeTJfVwzRqvAZE9fjbBDff0eA3kXBsYEAigB_YLhaglpSV7rHsSslpgxOKtzQ6lcTlr1Y9EFEeunDS7d9MB1vs6e3CTRnJ-irVct384vPrnOzfWnJKNmGbyLWpGfGl35nPgaxc15LgAHal8-ZjsWEA46Ajn54nzsGK4eD-PKE5Gid6v6vK86RL4Ih7iypJeZFlx1IXVeVW6rJzZ_FdWxCWnTvWQTvxiAbm_7W1OJvwBqCnKsFDIIvMvf-c2CwNZFs3laBoiSgKtse6C7xIYWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل دسترسی کاربران رایگان جمنای را محدود کرد
🔹
از ۹ اکتبر (۱۷ مهر) کاربران رایگان جمنای فقط به مدل Flash-Lite دسترسی خواهند داشت و مدل‌های Flash و Pro برای آن‌‎ها حذف می‌شوند.
🔹
مدل فلش‌لایت برای پاسخ‌های سریع، کارهای روزمره و گفت‌وگوهای معمول طراحی شده، درحالی‌که مدل‌های فلش و پرو برای وظایف پیچیده‌تر و استدلال عمیق‌تر کاربرد دارند.
🔹
مشترکان AI Plus نیز دیگر به مدل Pro دسترسی نخواهند داشت اما کاربران AI Pro و Ultra همچنان به هر سه مدل دسترسی دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/466239" target="_blank">📅 15:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgyQd3I4PS_N5tKwON_V5gBakmn-9128A_fUyUVHdpgBipdamLYJgzReI7Te2nWg8Y8gQ1WTYgx2k05bM1RB0m4kh8VqTlAlEIUz1eH7h4MancF-dyfk0WEiALcgMsrsZ4nDpLM9QOo4yaGFdyKtBkr3BNhwLSaSd24_mUDiaAFP1ich3w9vOmYlf9G-t8MEL11hUEl-i1nqw6icwwTE43xDJF0xn7HvivorGniy8vhBWZZIc46BchyHodOtegDx3bCE0hxQZcjI5qLKnQYCLtUoLYiqKB3buft-9drN1Rgxr4cCjRuvyPVOele6x3rhNuhIe2Imz63d4BPjRxB9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رئیس سازمان حج و زیارت: اگر کسی از حج امسال انصراف دهد عین پولش برگشت داده می‌شود و سال آینده می‌تواند ثبت‌نام کند و اعزام شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/466238" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2f2cb823.mp4?token=Dx6AqoNgqTbEw3iOQ9IN1Ptz6ILVi1pU2qEAb1qtlB1T5aJvxR_OieEUFBpBw0eH7N1CbCzEUnG34R9wOWXPQDEE7A1ItiqHFu9skGKLlwhv-9vmQSZZHgP1bD6ZSHQ3jWD1OZewaK4f76BeFpxExBPMOfF7AriBUh3yfQxyz6050sd6rPNrCKvWUss8pLqTCrb29ylgv46YARccnpp-8b-5mYMZB_yafZiqU1tUtH5sjQ-PYnFaRGSdQR0CKHt5IDA4M_TQRFO4WRqMlTIQhRebb6Z2HcAuhACzef31BfieCGIePcPiDqAWBmUthxpuf3oQ-i-bxjnFGnnUlxBj0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2f2cb823.mp4?token=Dx6AqoNgqTbEw3iOQ9IN1Ptz6ILVi1pU2qEAb1qtlB1T5aJvxR_OieEUFBpBw0eH7N1CbCzEUnG34R9wOWXPQDEE7A1ItiqHFu9skGKLlwhv-9vmQSZZHgP1bD6ZSHQ3jWD1OZewaK4f76BeFpxExBPMOfF7AriBUh3yfQxyz6050sd6rPNrCKvWUss8pLqTCrb29ylgv46YARccnpp-8b-5mYMZB_yafZiqU1tUtH5sjQ-PYnFaRGSdQR0CKHt5IDA4M_TQRFO4WRqMlTIQhRebb6Z2HcAuhACzef31BfieCGIePcPiDqAWBmUthxpuf3oQ-i-bxjnFGnnUlxBj0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف کارگاهی که بسته‌بندی برندهای معتبر را جعل می‌کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/466237" target="_blank">📅 14:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f6940786.mp4?token=YbujUF9V6DNDbV_eggZhmYdKAd3FraaJO8q_DQRXx9mQHmnD8gkWN5VhJVOtM7d0k7VOLZAGuonx5_5rsy0Tw_D5OStJAVApOx9AOPYyBCEZ0SKgPy0GyaIoFJCkYGBgM-0_xvSiaOJLS1dr4L-fTKItNMHEX-CXLIUIcgtzitNpjgZs6ByEniM31Rzf6I0yDpTs6TpfHwUcMGnhBmLcgTGMcyVF8DJftGbOCQMiV2t1uvpHyQANN2IZsJcilxNztAZIIiyhsamJ5A1ar9zYUTL5zagC9VpqBKgD04YnWwG-S326by5laaNIRDSDILydSZgM2KR7FtnFR9FULby4Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f6940786.mp4?token=YbujUF9V6DNDbV_eggZhmYdKAd3FraaJO8q_DQRXx9mQHmnD8gkWN5VhJVOtM7d0k7VOLZAGuonx5_5rsy0Tw_D5OStJAVApOx9AOPYyBCEZ0SKgPy0GyaIoFJCkYGBgM-0_xvSiaOJLS1dr4L-fTKItNMHEX-CXLIUIcgtzitNpjgZs6ByEniM31Rzf6I0yDpTs6TpfHwUcMGnhBmLcgTGMcyVF8DJftGbOCQMiV2t1uvpHyQANN2IZsJcilxNztAZIIiyhsamJ5A1ar9zYUTL5zagC9VpqBKgD04YnWwG-S326by5laaNIRDSDILydSZgM2KR7FtnFR9FULby4Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: استان‌های شمالی و برخی استان‌های شمال‌غرب، غرب و جنوب امروز هم شاهد بارش خواهند بود.
🔹
همچنین فردا در بخش‌هایی از استان‌های گیلان، مازندران، کرمانشاه، ایلام، اصفهان، استان مرکزی و لرستان باران می‌بارد؛ موج جدیدی از بارش‌ها پس‌فردا وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/466236" target="_blank">📅 14:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466235">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3aa391a2.mp4?token=ETEkFy04liWeKFRbHFEssDPNvppwSi31TLFaWjBDqiseRo_S8ObREHKjTcNRyGizgy5T5uHzIE2M_CdHGat7Rk7FF1ThyRWxpGObY_fqZh-XcG9hZzb-9XabxSXzGiHegwSsrCunTI5oOiCrL9WCZPZtcLKcfLHwxhX1ATYI-5JPHkbicmEyJxvyIbe2eVmpn0oarCWBUMosN6fIKwI5WkCRRnj61MoTp8U7ldmTLUbI7-87Jeu67QB3HVYfHFUD9GsqoBKcmDCg6CQOOG9t9F6_I7DBloTTZQ0ce-WEiRI_0dy-4rsIbR_pGI5xjxPiTp010iqnKHdOeO1bXuOw11qjgEO6LjuAXo_ktn9IkiXRhAd5h47RQdtwmdrvxlCiwbw0xWTgvo6PjrioALILz1pV_QZThS_D2MslZFvxlXTmZBxAD_RE0mLdopCa5hMteFsQ4f7Qpr4lU3zrOMepp851swvtaNCAFMywWztGibtggBO-Fv3SiguvMP3eA9ho8uxMQa0iv_4WZL9CNqykD1w94f1OFRnvsz08JlTq-yEoy6DM5oLSfouObqEh2ySAROMtxTdyhxbe7HaXRMWxWmwmZkT9-u83nm9Ds-HLnU2svFiQ-STtjGoSGz_LBRYFNJ0ZPggCEyFzwdtZZi62bEuWZHvfPxltZHVGcnhyRpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3aa391a2.mp4?token=ETEkFy04liWeKFRbHFEssDPNvppwSi31TLFaWjBDqiseRo_S8ObREHKjTcNRyGizgy5T5uHzIE2M_CdHGat7Rk7FF1ThyRWxpGObY_fqZh-XcG9hZzb-9XabxSXzGiHegwSsrCunTI5oOiCrL9WCZPZtcLKcfLHwxhX1ATYI-5JPHkbicmEyJxvyIbe2eVmpn0oarCWBUMosN6fIKwI5WkCRRnj61MoTp8U7ldmTLUbI7-87Jeu67QB3HVYfHFUD9GsqoBKcmDCg6CQOOG9t9F6_I7DBloTTZQ0ce-WEiRI_0dy-4rsIbR_pGI5xjxPiTp010iqnKHdOeO1bXuOw11qjgEO6LjuAXo_ktn9IkiXRhAd5h47RQdtwmdrvxlCiwbw0xWTgvo6PjrioALILz1pV_QZThS_D2MslZFvxlXTmZBxAD_RE0mLdopCa5hMteFsQ4f7Qpr4lU3zrOMepp851swvtaNCAFMywWztGibtggBO-Fv3SiguvMP3eA9ho8uxMQa0iv_4WZL9CNqykD1w94f1OFRnvsz08JlTq-yEoy6DM5oLSfouObqEh2ySAROMtxTdyhxbe7HaXRMWxWmwmZkT9-u83nm9Ds-HLnU2svFiQ-STtjGoSGz_LBRYFNJ0ZPggCEyFzwdtZZi62bEuWZHvfPxltZHVGcnhyRpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخشش ایران در المپیاد جهانی نجوم
🔹
تیم ملی المپیاد نجوم و اخترفیزیک ایران در نوزدهمین المپیاد جهانی این رشته در ویتنام، با کسب ۵ مدال طلا در میان بیش از ۶۶ کشور و ۳۲۰ دانش‌آموز درخشید.
اسامی مدال‌آوران ایران
:
🔸
سارینا علم‌پور
🔸
محمدحسین حسینی
🔸
هیربد فودازی
🔸
حسین معصومی
🔸
ارشیا میرشمسی کاخکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466235" target="_blank">📅 14:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466234">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدای شنیده‌شده در بندرخمیر مربوط به فعالیت شرکت گچ بود
🔹
فرمانداری بندرخمیر هرمزگان: صدای انفجاری که در محدودۀ شهر بندرخمیر شنیده شد، مربوط به عملیات معمول و قانونی شرکت گچ خمیر بوده و حادثه یا شرایط غیرعادی گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/466234" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466233">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5756415753.mp4?token=NsmDmx_UUY75MoVk6mhhx-bC-bFLgiW7fpPDGfReJ3wDv1lbdgC4BSvKI-O8JMh3PLKiTStXz_MEmLzNLEfdjkzmrrClNMmZNPKS1bMKkLso-Uc1x_MA7j4cl_xZ4CI35BDOgRnnwqHeOetGXrtMPBp1Wzd-tqCikpfiaLsJuPVzblUO5bZAJGQ-Z44xopYUu-gU5btYJ42PqFrKSTFlRB9wBKZhJC6pYMD6IjL1lt7NRAeSvo4cmxzvFsgcrOY3iTqGFQjgE8u0rqB7OMOcxFe8zs9pAUXMcoe66iq_YOAUv4_AiHKtBY_z454NTJ3i9xH1NgRlyrgcEu7IGJFVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5756415753.mp4?token=NsmDmx_UUY75MoVk6mhhx-bC-bFLgiW7fpPDGfReJ3wDv1lbdgC4BSvKI-O8JMh3PLKiTStXz_MEmLzNLEfdjkzmrrClNMmZNPKS1bMKkLso-Uc1x_MA7j4cl_xZ4CI35BDOgRnnwqHeOetGXrtMPBp1Wzd-tqCikpfiaLsJuPVzblUO5bZAJGQ-Z44xopYUu-gU5btYJ42PqFrKSTFlRB9wBKZhJC6pYMD6IjL1lt7NRAeSvo4cmxzvFsgcrOY3iTqGFQjgE8u0rqB7OMOcxFe8zs9pAUXMcoe66iq_YOAUv4_AiHKtBY_z454NTJ3i9xH1NgRlyrgcEu7IGJFVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ کابوس جمهوری‌خواهان شد
🔹
وزیر خزانه‌داری آمریکا: مردم آمریکا زیر چرخ‌های کامیون تورم له می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466233" target="_blank">📅 14:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38fd43416c.mp4?token=Q3gTJomXlNBjmekyXf8bLnhpN7628tbwX0eaUb1CXGRiXLLmSIi-2Tx5imD3ZzUg1MVYidMvsbw5EpR-9BN6iy6hXU58DmVgnOXFtHng3BvMfdspDofhqb-jXG_r-tN0hvQKXCmyat9lg_i9anxP7jWK4O5CVgff6G0tvWSCK-W8_UiTm-cgG5R8AsqvoUz2M6lSNleyrgqSoDS0ZrrfUecAvbKUciqU7yxO4w_49dk9XjeH59GDrIOVNNaieZql7c9PiPVcS0hYW-VD_BWS0W6C_jIndIhKd3cfaHrtsDKop_MrgHM3Nh-oLGnqwl7ivb2kYCuL6goS__1yQ-wnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38fd43416c.mp4?token=Q3gTJomXlNBjmekyXf8bLnhpN7628tbwX0eaUb1CXGRiXLLmSIi-2Tx5imD3ZzUg1MVYidMvsbw5EpR-9BN6iy6hXU58DmVgnOXFtHng3BvMfdspDofhqb-jXG_r-tN0hvQKXCmyat9lg_i9anxP7jWK4O5CVgff6G0tvWSCK-W8_UiTm-cgG5R8AsqvoUz2M6lSNleyrgqSoDS0ZrrfUecAvbKUciqU7yxO4w_49dk9XjeH59GDrIOVNNaieZql7c9PiPVcS0hYW-VD_BWS0W6C_jIndIhKd3cfaHrtsDKop_MrgHM3Nh-oLGnqwl7ivb2kYCuL6goS__1yQ-wnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برجک زندان رجایی‌شهر فروریخت
🔹
در ادامۀ تخریب دیوارهای زندان رجایی‌شهر البرز، برجک این زندان نیز تخریب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466232" target="_blank">📅 14:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88addec6bc.mp4?token=h7bpzjzEke6qT6kjrGMQJuHaYNGKkoIglnCvQ6oSve-uUQjwISHScWZPPHoYPtu6iS54sAYznS4zMYNXTRptUk0jT1s2-KFAj7haC4J86j-rXrL-Y3TXjBKHXrkO5u5kaliBQVys3nD4vbYBfIAAf-fSziUQmHe9tYSrsbode_KGmQAoU_W_QtW8qSB_nBdA64rc4RCT3bYR9RBK7YOSSnZs7c4ObfcVp6M6A8O5JdLsmJEwaBJKO7h0HMxeMCSduQdbtdjWcaopfFB7TPo9y_9VNE4g_iu5f7q74EcS1CSupcUWKsJ38rseAiMt9PBr9Fg-MYEa4deHdocc3wDb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88addec6bc.mp4?token=h7bpzjzEke6qT6kjrGMQJuHaYNGKkoIglnCvQ6oSve-uUQjwISHScWZPPHoYPtu6iS54sAYznS4zMYNXTRptUk0jT1s2-KFAj7haC4J86j-rXrL-Y3TXjBKHXrkO5u5kaliBQVys3nD4vbYBfIAAf-fSziUQmHe9tYSrsbode_KGmQAoU_W_QtW8qSB_nBdA64rc4RCT3bYR9RBK7YOSSnZs7c4ObfcVp6M6A8O5JdLsmJEwaBJKO7h0HMxeMCSduQdbtdjWcaopfFB7TPo9y_9VNE4g_iu5f7q74EcS1CSupcUWKsJ38rseAiMt9PBr9Fg-MYEa4deHdocc3wDb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
۱. آرش محمدی</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466231" target="_blank">📅 14:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86022fba13.mp4?token=kF1BbXQ8_Pd6g_qwYKoS64LMlOvovt5SILAGo8FAviw-uLcIb36DbdSZO9uQ4EGUOYAiVfST9Zxg5djqO0gtVcJm3VvHaZrvAikGh1FWlFMEoutSkAogltKp4hKH91_YlES0_RS_6X1DjJo-rg3Dvvw2Ouncc7djsceCXzoPH85baPkq53yDnzX-By-qFYXbND7z4lGBKWG-pvoq6U__UWxZ9tpCuXttC8yN2WEZYQOdoKVE-fDr7VV6c5Oni8ZOUe1AD9-rdYZieR0Z1BH1NV1LAuIXcCNnFBajXW2y9rE5SxkIVb6soAeNVjZ-DDDKLf8vknLJgLGBSVwWslzOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86022fba13.mp4?token=kF1BbXQ8_Pd6g_qwYKoS64LMlOvovt5SILAGo8FAviw-uLcIb36DbdSZO9uQ4EGUOYAiVfST9Zxg5djqO0gtVcJm3VvHaZrvAikGh1FWlFMEoutSkAogltKp4hKH91_YlES0_RS_6X1DjJo-rg3Dvvw2Ouncc7djsceCXzoPH85baPkq53yDnzX-By-qFYXbND7z4lGBKWG-pvoq6U__UWxZ9tpCuXttC8yN2WEZYQOdoKVE-fDr7VV6c5Oni8ZOUe1AD9-rdYZieR0Z1BH1NV1LAuIXcCNnFBajXW2y9rE5SxkIVb6soAeNVjZ-DDDKLf8vknLJgLGBSVwWslzOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: ۳ ماهوارهٔ جدید از منظومهٔ شهید سلیمانی در دههٔ فجر رونمایی می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466230" target="_blank">📅 14:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGlZpm1ZTH0HM-i8b4VTTLSljO4cKa3CDvqvenSVCJylX946vTO1ySkZVZWXa-5V4Nli97DpJdsEv5uKIBChZXu5Ys8kuwEm2Ju9SGoL4qZ8_wPB0RlLrCTrzfbe3NYoVqnr2f5YhEwOuAdKwgoOmNBeqkAuijdrdreQIDGcmRtsbfFzFtaTN2b-h7jlJ0nOn-tCqz--uKE3c0H294yrS3sW8GXd-ckgvQ3SJybzhQru6SuHWUuEgWzY2CGwAH-TiyoG3H_uAKwKP0-sgUIoLCTvo6h3tu1R81Tsu3BGWpiknCg3xk3FSv1ik0CpXKnFauSM14vU4rLimMf-2Sr_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگهٔ هرمز هدف قرار گرفت
🔹
به‌گزارش سازمات تجارت دریایی انگلیس، یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفته است.
🔹
ناخدای این کشتی می‌گوید که بر اثر این اصابت به موتورخانه این نفتکش آسیب وارد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466229" target="_blank">📅 14:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b68653419.mp4?token=OL3eib1OUheByO0p57fr6G0mHVCfEvQq_iVlk7uRsdC-374324i0j3Rmg911eb6zb-FPZKX7pkWxebEz2KKc8MbKgvDi0roc0IHsIa_vBK70MyZ5OI8RvyDONxabQ0zuHrWO6w8Yut_MUiMTwy7JglzabmAlHfBw_wGfOcxNNXwvt9vEQUQQZ8eSpA_JdisrJGVgMRHhEtv1FO_D6lkRBbpf-G9saXapqWHzSJVvzsbgyOJeQJFRuXyyQIp_E-nsaCzWHfKO9A5nMqL_bwlBp6xsQtpR7s1IIOYGfnos5lHMPh2avoZPpP-ynCO7ELUI8bmGPk9a_8SNqtXfkYUfz4OvE7hdt3WZY4OPrKm8-QiWYXs76K4x7et4biNKq8GiJa00LUUMjRWN9uJ7HitQ0NugYk_ynT2FQBuCbZzZfRZUH3cbPEhLr3hyEbpIYzXi9AGkoTwGQR7ay6Jlo0PnaKDVLJnvPhts1a-PWHKa2sgZTc9nWqXzQPWWVoGwk1Yr1mrtrJczG8INwg56JCeF10XqRae3NiOE_dUV-OxUcMv4zbwr-fy3zJfqeoMK985ArdzjsAUn4K2bkJaC3wTOr8pURJ2XSPg73KYiV7Ms79gEFkgQuHX-VW2Tw5jp7C04vMiwvVOMwWk0OcM5vgkHx1og6i_s5HIYKEJ3Sy-6Gto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b68653419.mp4?token=OL3eib1OUheByO0p57fr6G0mHVCfEvQq_iVlk7uRsdC-374324i0j3Rmg911eb6zb-FPZKX7pkWxebEz2KKc8MbKgvDi0roc0IHsIa_vBK70MyZ5OI8RvyDONxabQ0zuHrWO6w8Yut_MUiMTwy7JglzabmAlHfBw_wGfOcxNNXwvt9vEQUQQZ8eSpA_JdisrJGVgMRHhEtv1FO_D6lkRBbpf-G9saXapqWHzSJVvzsbgyOJeQJFRuXyyQIp_E-nsaCzWHfKO9A5nMqL_bwlBp6xsQtpR7s1IIOYGfnos5lHMPh2avoZPpP-ynCO7ELUI8bmGPk9a_8SNqtXfkYUfz4OvE7hdt3WZY4OPrKm8-QiWYXs76K4x7et4biNKq8GiJa00LUUMjRWN9uJ7HitQ0NugYk_ynT2FQBuCbZzZfRZUH3cbPEhLr3hyEbpIYzXi9AGkoTwGQR7ay6Jlo0PnaKDVLJnvPhts1a-PWHKa2sgZTc9nWqXzQPWWVoGwk1Yr1mrtrJczG8INwg56JCeF10XqRae3NiOE_dUV-OxUcMv4zbwr-fy3zJfqeoMK985ArdzjsAUn4K2bkJaC3wTOr8pURJ2XSPg73KYiV7Ms79gEFkgQuHX-VW2Tw5jp7C04vMiwvVOMwWk0OcM5vgkHx1og6i_s5HIYKEJ3Sy-6Gto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلاتکلیفی ۲۳ سالهٔ زمین ۴۲ هکتاریِ قزوین که قرار بود گلخانه شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466228" target="_blank">📅 14:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db14e940f.mp4?token=VuHEmxpjoMr7Pgd604xGDx58ZyF4i87DMmaMYVEYStFhkO7Y1ij2jgocGRhYv7SslZ6NlZd03eN2NhmNhiSYrgFXEnvk4Xx0TPZTXP4S8xFTnlHIWpZJL5lC_rRTk67QCGjhzW-EGGIeUAh8H--E1IEAzWshNttxvkLbPR8mmGVmn7Ao_S4h_PRyPLqvpLFv6NXeCOWzRJJ2l7li9l2ARP-8dxSLIZjKPIO0mwpNCHg6j1158HcItEgmeAFeLdWb7XRfxU7fyYaZoP92IxGmb9flODOAnTdXyAb_znswpfBuXijLGQsGPkIgZwL23AZSHcNeA-NngCbcnKmeYeaZYbrpCPXI-vPS5WjWATRdLma_ifzXVdyWHQNqJT7xKL-e0MeB17OhgtlJy2whDjKx7_fKUeDZsOfEBfh5Oa_G1pFDGnucWGjksaiw54yXHb1LKdr-vUUybSjhnZZpuqhKln84MawdbRhleSvQUbUmdx42BHzfS6nLc62Dcff99oTJrtRnLiGyxNIvW7Edj5Lj40CTBdqSDa4L--KHoSFoZhH3Rek2jsJ7dBYEccvSXKpzZuMXjbD3YQS4cunrIm2l2Tm0HqS4sUo_bF8618ZFKs-tifcQkdj6AdmuuqP7da5t_hnIVxC95LWD2kW_sRHhRYlm-vZInCn_xYMqx8jRCiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db14e940f.mp4?token=VuHEmxpjoMr7Pgd604xGDx58ZyF4i87DMmaMYVEYStFhkO7Y1ij2jgocGRhYv7SslZ6NlZd03eN2NhmNhiSYrgFXEnvk4Xx0TPZTXP4S8xFTnlHIWpZJL5lC_rRTk67QCGjhzW-EGGIeUAh8H--E1IEAzWshNttxvkLbPR8mmGVmn7Ao_S4h_PRyPLqvpLFv6NXeCOWzRJJ2l7li9l2ARP-8dxSLIZjKPIO0mwpNCHg6j1158HcItEgmeAFeLdWb7XRfxU7fyYaZoP92IxGmb9flODOAnTdXyAb_znswpfBuXijLGQsGPkIgZwL23AZSHcNeA-NngCbcnKmeYeaZYbrpCPXI-vPS5WjWATRdLma_ifzXVdyWHQNqJT7xKL-e0MeB17OhgtlJy2whDjKx7_fKUeDZsOfEBfh5Oa_G1pFDGnucWGjksaiw54yXHb1LKdr-vUUybSjhnZZpuqhKln84MawdbRhleSvQUbUmdx42BHzfS6nLc62Dcff99oTJrtRnLiGyxNIvW7Edj5Lj40CTBdqSDa4L--KHoSFoZhH3Rek2jsJ7dBYEccvSXKpzZuMXjbD3YQS4cunrIm2l2Tm0HqS4sUo_bF8618ZFKs-tifcQkdj6AdmuuqP7da5t_hnIVxC95LWD2kW_sRHhRYlm-vZInCn_xYMqx8jRCiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در این جنگ به این نتیجه رسیدیم که حتما باید برد موشک‌هایمان‌ را ارتقا دهیم و الان به این سمت رفته‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466227" target="_blank">📅 13:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r50GDXim11TiI3OxnPOT3deHopxueCznwpnMDDNfh2ES_sKKIIh7sYBT7iSkDHB2btg4Erq1CmcU-Vck6SVZReEYH_i68dXqdzzXiy2Ejr80G1VT_BfEwco_LioCOktSFDrYCdIa0nAnsO0wjWTVGYujRNpDxF3BSGqXn-n4hTq0dHKMhxIWbWhgfqHfZX4pclgVmfAkXKkjl3PWi0T7EY429G3yZlliX-8nQa6Qm93SJWgF580dy2vlRoh7KBc3vDBFmiXVt0j_gqKhQatUZrpihRxlYWfepMdKIxa7pnspLyo6DRJWBqbE3-AaP1dmj7U-zYt4u-JkioTglWg_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس کمی ریزش کرد
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۵ هزار واحدی به ۷ میلیون ۷۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466226" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
