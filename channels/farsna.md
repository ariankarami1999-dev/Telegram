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
<img src="https://cdn4.telesco.pe/file/ZgSC30HvIyvhDsv_lxGrRByua-BXWfGCrtKuD57wpkjCE0prJdpLMEW1c740U9e4yjNvMQwhDoIYxp6cHznwaINshV1gXDJ01OEGlEKG-0ggBkSAaqZ_hPZ2lpFMp3yg1qOltv8DS-5EE3hRAL-6iDhTmnFD6-K3Gs2EB4RsDXdlqU_ZPw-fFUASlAlvTIzx305BLOyayU71Sz4qdxD39hr9maGzthtZzbq0wJptxmTFdAaL7P2-cn0c-99TKyAe3zEAr8lG2bwaJ14zgIQuuAY5N6WesAlYlygW_hEOJDihzc36WOTZNBJFLpjxa4cReyqtz0wZF2_1xvss9Tz6Bg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.86M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-466888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8da12bc4ba.mp4?token=JBbPLz8KpqTDaQksiIKcszf_wbRVM82xGDph8SSE4zZZuGBcYiWn6OSZz3qgXqm43z5jcZZheded2S-QrwUCdvmU9YMG3E37-zZ7LrMudPFFXBJJz79v34s_3sTzCXrUse49kiANQehlJBDKX-S2jUmQAPWZB1DVJCW813fzdBQGKIeir2TVg6yz_YVRgBSMydR7tciOFirgOJPKKYibZDxuMOU3zhqv1nKcEX9ZbDmnZJaolMX_q4IXs9Hx9g42V9cLqzSXNqFSHV6F0XSCCbaGRLT8jXHPaIfaVIZ89dQtTRa-ndCG4ISQSJDykAcZyz_Um7zYUrhelR1f9bGYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8da12bc4ba.mp4?token=JBbPLz8KpqTDaQksiIKcszf_wbRVM82xGDph8SSE4zZZuGBcYiWn6OSZz3qgXqm43z5jcZZheded2S-QrwUCdvmU9YMG3E37-zZ7LrMudPFFXBJJz79v34s_3sTzCXrUse49kiANQehlJBDKX-S2jUmQAPWZB1DVJCW813fzdBQGKIeir2TVg6yz_YVRgBSMydR7tciOFirgOJPKKYibZDxuMOU3zhqv1nKcEX9ZbDmnZJaolMX_q4IXs9Hx9g42V9cLqzSXNqFSHV6F0XSCCbaGRLT8jXHPaIfaVIZ89dQtTRa-ndCG4ISQSJDykAcZyz_Um7zYUrhelR1f9bGYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس شمس تبریزی در خوی
🔹
در سفر وزیر گردشگری به آذربایجان‌غربی سازۀ جدید مقبرۀ شمس تبریزی افتتاح و از تندیس این شاعر نامور ایرانی رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 338 · <a href="https://t.me/farsna/466888" target="_blank">📅 20:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cc8074b1.mp4?token=RU5csO7YMuNW66U-2_RYBUtS_RnHWALGvYSzaZ-NU5-z30JiBh9dof8aNzefeNS9vgYGvM2X77f4M60ATImpWrF7RfUXnHhmQzd2JY9jkICv6kQE3cE3nik7bSQb0Ff2TyMZmKkCx9wCmZLymQMg8MVNr8ExL2P39C8n8wrMKWpvU067ALVpLFhCLKV20ebYNci3gBfKwR6Ubtq9WAGO9wXLEm5uLHb-s3scqXnnUbiiRkE5M5fn0XaU1TfesMs0Y-akNtSGiJ_BC2EOQacYJqKN5R3iJRNZT7LH0IDWziqTxWZSm4_6XNiJp8zYfFwAlYmh_0n_fZvujGEBPsyoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cc8074b1.mp4?token=RU5csO7YMuNW66U-2_RYBUtS_RnHWALGvYSzaZ-NU5-z30JiBh9dof8aNzefeNS9vgYGvM2X77f4M60ATImpWrF7RfUXnHhmQzd2JY9jkICv6kQE3cE3nik7bSQb0Ff2TyMZmKkCx9wCmZLymQMg8MVNr8ExL2P39C8n8wrMKWpvU067ALVpLFhCLKV20ebYNci3gBfKwR6Ubtq9WAGO9wXLEm5uLHb-s3scqXnnUbiiRkE5M5fn0XaU1TfesMs0Y-akNtSGiJ_BC2EOQacYJqKN5R3iJRNZT7LH0IDWziqTxWZSm4_6XNiJp8zYfFwAlYmh_0n_fZvujGEBPsyoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دریاچهٔ گازوئیل در جاده آبادان-اهواز چه قرار بود؟
🔹
انتشار تصاویری از تجمع حجم زیادی گازوئیل در جاده آبادان-اهواز و شکل‌گیری ترافیک، در روزهای گذشته در فضای مجازی خبرساز شد.
🖼
اما ماجرا چه بود؟
مدیر شرکت خطوط لوله و مخابرات نفت منطقه خوزستان اعلام کرد که این حادثه شامگاه سه‌شنبه ۱۴ مهر به‌دلیل ایجاد انشعاب غیرمجاز توسط سارقان مواد نفتی رخ داده است.
🔹
عملیات ایمن‌سازی، مهار نشت، ترمیم خط و پاکسازی کامل محل در کوتاه‌ترین زمان ممکن انجام گرفت و در حال حاضر این خط لوله در مدار بهره‌برداری قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/466887" target="_blank">📅 20:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRCP62M594kJgBxRbkObyrnhO8DAaZs0Axe8jqItVzzvpkviwj-gRAhEaWEjOZxsEnXmBViXU9Q_hUVvSXOhRBe_co1ArIbwwrtaGZoglifT1RXcooI-U-8noBBubmnAdJUDQfshJKDvIECHg0EkPg3QRmIrljGJ3TzRRKsPoZ-XlvlOq0aVeO5TXBWWXfefVhf5PLoIr4h9MiseTZK_CAvcI0HfBK1SMEzdylveuazadt1YwGewlLZZWuMCt4C2FSMdS25g8Yn36l_1-BqhIk2930ELI81JJZDoiaCPI9xLxKkFmE1K1IvHhQZ3GaZk32j2Vn45o7sECe50Ojl1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلای دبی پروازها به تل‌آویو را تا اطلاع ثانوی متوقف کرد
🔹
فلای‌دبی که روزانه ۱۰ پرواز رفت‌وبرگشت بین دبی و تل‌آویو داشت، به‌دنبال حادثه پرواز جنجالی چهارشنبه گذشته پروازهایش را تا اطلاع ثانوی تعلیق کرد.
🔸
روز چهارشنبه ۳۰ سپتامبر، هواپیمای فلای‌دبی از دبی به…</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/466886" target="_blank">📅 20:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
رهبر انصارالله:  سعودی زیر چتر آمریکا قرار دارد و تحت پوشش آمریکا به یمن حمله می‌کند. خواسته اصلی سعودی نیز ورود مستقیم و همه‌جانبه آمریکا به این جنگ بوده است. @Farsna</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/466885" target="_blank">📅 20:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466884">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
بانوان شهرکردی جان‌فدای ایران شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/466884" target="_blank">📅 20:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466883">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601ed69b31.mp4?token=ATblpaQUToRgWVKAPjT5BrvqtLI5hWo1URq0IkjVP_ZltWBZ_Mbf7uEUT8Atthh1pGWdX8G6L0m8U6S7pn9vlAf7XTZm7SCWOkwPOX7vQej8r5Lxj-8uWgVecZxZQb4kgm20GFZJ0JV65rqpnnWbGXVRz0tzOfRLIEfSAEgS12kI9FvX3a0H3W4pFtIO-tVa-nPNZxyyLaQp34prm10GnlDn1X4qjYX68d3rUPUeaNn8ftWpvXgnGms52ts-mJL_GYj8GCosnMWVYRPu5-u5cBf8zAAhhxECODjoagtDIL7xH1KZDhkh9Knzf6hyBnJJxPOKRV3XEVu5sub2y6rCEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601ed69b31.mp4?token=ATblpaQUToRgWVKAPjT5BrvqtLI5hWo1URq0IkjVP_ZltWBZ_Mbf7uEUT8Atthh1pGWdX8G6L0m8U6S7pn9vlAf7XTZm7SCWOkwPOX7vQej8r5Lxj-8uWgVecZxZQb4kgm20GFZJ0JV65rqpnnWbGXVRz0tzOfRLIEfSAEgS12kI9FvX3a0H3W4pFtIO-tVa-nPNZxyyLaQp34prm10GnlDn1X4qjYX68d3rUPUeaNn8ftWpvXgnGms52ts-mJL_GYj8GCosnMWVYRPu5-u5cBf8zAAhhxECODjoagtDIL7xH1KZDhkh9Knzf6hyBnJJxPOKRV3XEVu5sub2y6rCEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقائی: عملیات‌های پرچم دروغین جنایت‌های آمریکا و اسرائیل را نمی‌پوشاند
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی درباره تاریخچه عملیات‌های پرچم دروغین آمریکا و رژیم صهیونیستی در ۷ دهۀ گذشته نوشت: پرچم‌ دروغین، شگردی دیرینه‌ است: اول صحنه‌سازی کن، سپس انگشت اتهام را به سمت دیگری دراز کن، و در آخر از نتایجش بهره‌مند شو.
🔹
در وضعیتی که افکار عمومی آمریکا و جهان از جنگ غیرقانونی و تجاوزکارانه علیه ایران به ستوه آمده‌اند و متجاوزان هیچ راهی برای توجیه تجاوز نظامی خود ندارند، آنها مانند کسی که در حال غرق‌شدن است برای نجات خود به هر تخته‌پاره‌ای از جنس دروغ آویزان می‌شوند.
🔹
بقائی پیش ازاین با اشاره به اتهام‌زنی‌ها به ایران در ماجراهای پایگاه فرفرود انگلیس و پرواز فلای‌دبی به گفته بود: گویا رژیم صهیونیستی و مدافعانش در اروپا و آمریکا به دنبال این هستند که هم موضوع فلسطین و غزه را به حاشیه برانند و هم تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران را و این‌گونه القا کنند که گویا تهدید جدیدی از جانب ایران متوجه منطقه یا جامعه جهانی است.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/466883" target="_blank">📅 20:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466882">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bilv1Z69WG5qpyeqgBc0edgQPELv0ydoeCOXNMF4perP2CUyvWj2gnUiTz2Xdug-5SNnQSgsyvhy_kS9hSHHdikz-JCyQ8M91JMh5D1iDUG_mQ4qD0gABYAI7jGFM7KOAV3h9LqArpFmGtK8HI3uMDeRDzt6NX224owDY_U5k7QbsDgMaQFrDB4Qj5R67BrrdEgPktPx3X7vijDU6Ho0xjW2kfVW1VnfFw6etcm1ExnLUonNjZGuc3EEbPphxfA3VTvD4jaAlwvoiLQJNNN4KQ3KlbOUK1vJJbU7NiYwJg4GQ0TB70RvBRhEyLNahC7wovV2Vgo_3lwj2Ss3R9EUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار تهران: اولین محمولۀ متروباس‌های ۲۶ متری با عبور از محاصره وارد ایران شد
🔹
زاکانی: امروز ثابت کردیم محاصرۀ آمریکایی ناتوان‌تر از آن است که بتواند جلوی ارادۀ ایرانی‌ها بايستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/466882" target="_blank">📅 19:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466881">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162720c36d.mp4?token=CtL4uj8ZYUH6twMprgvdgvbdyHFn9K-EezibKQZ0VyMG_qmnPLMcM850tN7tWy5sbOi3kvZSLZ1EHWyasFLQTnwYIttvIOzqKEEr1o5mlwbZf5VsrMKR62tpYz1pLjdTZCYpHYu2Z0oaL25en1lbL7PkROmmank8YfrC8lepHEa4d1gwOKQXTo5VwxSn671RsjPaNx9PZOEMK4tsNxt2Q40xBFUAgCLWh9H4jvwqAa3QWUDITIa_-KSso9M-HJhGLwQCeIBRJamt8l09iM6n4bTTYyXQUm62TJHJ743S9eCX0Zf7y55iWcrxk_g59dapwqg6BNICOWeIlh4QTjIhPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162720c36d.mp4?token=CtL4uj8ZYUH6twMprgvdgvbdyHFn9K-EezibKQZ0VyMG_qmnPLMcM850tN7tWy5sbOi3kvZSLZ1EHWyasFLQTnwYIttvIOzqKEEr1o5mlwbZf5VsrMKR62tpYz1pLjdTZCYpHYu2Z0oaL25en1lbL7PkROmmank8YfrC8lepHEa4d1gwOKQXTo5VwxSn671RsjPaNx9PZOEMK4tsNxt2Q40xBFUAgCLWh9H4jvwqAa3QWUDITIa_-KSso9M-HJhGLwQCeIBRJamt8l09iM6n4bTTYyXQUm62TJHJ743S9eCX0Zf7y55iWcrxk_g59dapwqg6BNICOWeIlh4QTjIhPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اکتشافات نوین، مطالبه‌ای برای شناسایی دقیق‌تر منابع شد
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/466881" target="_blank">📅 19:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466880">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKEJ7Ehh2oAhrWBRXQsPyn26iYNK-7aPqbn-sDcY6XmmTTkH2PTT4vJdw-3EYorXd0QkWM3qoUmtyPeemTqPo0vze0aqaI3SG18Jb-xE2kHV8d5znfPB703xBHnPkMPJMQ4_GgSM1HLLZHniIfTBetSRvgNSXrFUage0Kh0I9_u6yg6uasFOSAuLsyGjZzStE6vwJ6xP6Ks2e8gXuTSeZNhNcL1W_vjZd7fTlHZOE3cw1PGHevktjsA1m2JMZiYxhkR2EXCHwrbMQw-4VFrusae6TKoIwrLkWdPrHKExpVV-LDiZKYmdqYEBP57pH5x8nlt4Q043NAs0YR8vgXZj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد نفتکش‌زنی در تنگهٔ هرمز شکست
🔹
رویترز: طبق اعلام منابع رصد حوادث دریایی، تنها در یک هفته اخیر ۱۳ نفتکش در تنگهٔ هرمز هدف حمله قرار گرفته و ۷ نفتکش هم پس از هشدار از ادامه تردد در هرمز منصرف شده‌اند.
🔹
قیمت نفت امروز از ۱۰۲ دلار گذشت و پیش‌بینی بانک‌های بین‌المللی افزایش شدید قیمت نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/466880" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466879">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌ احضار سفیر فرانسه به وزارت خارجه ایران
🔹
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گستردۀ حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد.
🔸
اداره کل حقوق بشر وزارت امور خارجه با یادآوری تعهدات…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/466879" target="_blank">📅 19:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466878">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c87c2307.mp4?token=W_MK_ea4ZF-GHZ7njL87rQ3ltMN1tV_ZJEojLe8ZI1B1xljF1MzA6eMC2z8qG0THOG2eWGG8H9TAvgXmMiLntsOJag871XDU5coQ4T1L_W-SKfYrvi1b3gQWMtvLWpeNhU1i9kd0gdYDhTxiq2h3cS1P3J5KKnD9ox8mQ3yHPTW9zp6axdoDc2peMrfzJurumnm8MUvFIQGTPRlR02FZxB9R-Yod5dH4gT6-SlWPqjfDzVmhGT3nK85nUGlZTimh9peJ3lk9d4e7NkBa4A0XuJAa7cezQof8CheZ1xyxymoEn0kJvq12FqCMkt8TjFyYmSwvVPO3_iiv1Ohr2ag1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c87c2307.mp4?token=W_MK_ea4ZF-GHZ7njL87rQ3ltMN1tV_ZJEojLe8ZI1B1xljF1MzA6eMC2z8qG0THOG2eWGG8H9TAvgXmMiLntsOJag871XDU5coQ4T1L_W-SKfYrvi1b3gQWMtvLWpeNhU1i9kd0gdYDhTxiq2h3cS1P3J5KKnD9ox8mQ3yHPTW9zp6axdoDc2peMrfzJurumnm8MUvFIQGTPRlR02FZxB9R-Yod5dH4gT6-SlWPqjfDzVmhGT3nK85nUGlZTimh9peJ3lk9d4e7NkBa4A0XuJAa7cezQof8CheZ1xyxymoEn0kJvq12FqCMkt8TjFyYmSwvVPO3_iiv1Ohr2ag1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز آمار: سرشماری غیرحضوری نفوس و مسکن از ۲۵ مهرماه آغاز می‌شود
🔹
۳ گروه هدف ما خواهند بود که برای آن‌ها پیامک ارسال خواهد شد. پیامک‌ها حتماً با سرشماره مشخص ارسال می‌شود و لینکی نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/466878" target="_blank">📅 19:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466876">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uo39bRHe0ykJBiUqwyin8IvNNE8BqJH7z1VQbqlTWDz_hWqgQm-veE0dTBovNTCp3go1cxvIVCxqbYqrNrNJ3XUX-NkaaBhgm-AMcNEzHUWDvVatrAN07Pa_sWjbTQLg4evFtpoKUOlMqXKITG_d06oQQ51dWKd4mF6Mq11CbDPfx5N9I0sZk4Af0Qsh61mLRMn8swYf6mz1Sr8MJeikww9mC0astiJs1IS7XoTDXoNokniv-fbRj3e_rXbgJ43cHkhNC-73VUgeOQtR4vTHTMj7oHlT7EZmhPNwpK5AlxqLagn9Ig0FLO_VEjA81PL9qJHfHWBOcedQEebRgbq8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVGn_fMTn_gLxtTVTzrDY14umVCTG4dctfj8nrVfHmg0imMe9C17MMbUKjfcQU0utF_mQYoWUwAsJcV78E81HiazguEk6MX1GBKguEJfwnxxuF7zN5soAZVEdNioxRbaBPkdgr2GtKZ2QmkZgXY84NmOL6FkPbJ2_0JBxG6fJNSdWfzp6ZiV1dX_yDWZI4balzWdYr87RgjIu2V3uRJOkUj9vLHc8EGz4PplnU-8G-aDhp48C0MfpNr3UV_XlU9lzpMGiIEqOcgz--Tme6GjT6gwckH74tuB0PdP7TWj-0j3sgQY0AwwaF81FOhNiScx3Yz_D_eHYpzFUAM5r85FXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو بحران‌زده آمریکا با کارنامه‌ای پرحاشیه به خانه بازگشت
🔹
ناو هواپیمابر «یواس‌اس آبراهام لینکلن» روز چهارشنبه با ورود به بندر خانگی خود در شهر «سن‌دیگو» واقع در جنوب ایالت کالیفرنیا به مأموریت پرحاشیه‌اش در جنگ با ایران خاتمه می‌دهد.
🔹
وزیر جنگ آمریکا پیت هگزث که به دلیل مشکلات و بحران‌های ایجاد‌شده در این ناو به شدت مورد انتقاد قرار گرفت، به شهر سن‌دیگو سفر کرده تا از خدمه این ناو استقبال کند.
🔸
رسانه‌های آمریکایی ماه پیش گزارش‌های متعددی از شرایط دشوار زندگی بر روی این ناو اعم از کمبود مواد غذایی و محصولات بهداشتی و همچنین مشکلات مربوط به وضعیت روانی برخی از ملوانان منتشر کرده بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/466876" target="_blank">📅 19:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466875">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: آمریکا و عناصر صهیونیست و بعضی از دولتها برای غرب آسیا نقشه طراحی کرده بودند که عملیات طوفان‌الاقصی آن را باطل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/466875" target="_blank">📅 19:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466874">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c86a2176.mp4?token=SL0614sf8EUNfYRwKK5dO-6k9HPzXlWTLSHFKrc6FRQ5j1dsdDhcHpS_n-DtuFSnMOOd_CQlg3EkY2RzBbqfDZ9tfGy3--430nZqMNMnEUMgqTOlhJeA5zpibr4SNJST70Y3aWOjm8Yba7VHk9IZ9ZXgJ_9VMdZm9m5fT-Dvw9JRoWYhW2nRLW6nJ8YiWClMG5TLarBwrmQtNxMAGMDQr-7ukCIo7_diqXiQ_JefHa-7AQrgBD9w4Bh1BqCtPfXGR4AJO-9Y12-b-x5U4S5fwOqey5QPaSu33X9_crEpUjPg1zv447mHsDfIEXr6gllJHyIsLPptnqCLSP6O6-5_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c86a2176.mp4?token=SL0614sf8EUNfYRwKK5dO-6k9HPzXlWTLSHFKrc6FRQ5j1dsdDhcHpS_n-DtuFSnMOOd_CQlg3EkY2RzBbqfDZ9tfGy3--430nZqMNMnEUMgqTOlhJeA5zpibr4SNJST70Y3aWOjm8Yba7VHk9IZ9ZXgJ_9VMdZm9m5fT-Dvw9JRoWYhW2nRLW6nJ8YiWClMG5TLarBwrmQtNxMAGMDQr-7ukCIo7_diqXiQ_JefHa-7AQrgBD9w4Bh1BqCtPfXGR4AJO-9Y12-b-x5U4S5fwOqey5QPaSu33X9_crEpUjPg1zv447mHsDfIEXr6gllJHyIsLPptnqCLSP6O6-5_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: ۳.۲ میلیارد لیتر سوخت برای عبور از زمستان ذخیره شده است
@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/466874" target="_blank">📅 19:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466873">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: ادعای سعودی‌ها دربارۀ قصد یمن برای هدف قرار دادن مکه و مدینه، افترا و دروغی با منشأ صهیونیستی است. @Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/466873" target="_blank">📅 19:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466872">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
رهبر انصارالله:  سعودی زیر چتر آمریکا قرار دارد و تحت پوشش آمریکا به یمن حمله می‌کند. خواسته اصلی سعودی نیز ورود مستقیم و همه‌جانبه آمریکا به این جنگ بوده است. @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/466872" target="_blank">📅 19:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466871">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: هواپیماها و تسلیحاتی که بارها و بارها به‌وسیلۀ آن به یمن حملۀ هوایی شده آمریکایی هستند و استفاده و به‌کارگیری آن‌ها به آمریکا وابسته است. @Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/466871" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466870">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: اگر کشورهای عربی همان کاری را با مردم فلسطین انجام می‌دادند که غرب با رژیم صهیونیستی انجام می‌دهد، وضعیت کاملاً متفاوت بود. @Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/466870" target="_blank">📅 18:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466869">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b32e36c8.mp4?token=AJ9l-gD7gomVIxnrvfSWIhJfJczJWvk095csTmlHhaBAGCl-HSY1uOX1FC8EIq85AOyLJWnhnnCEMbJim0eSuHUjthn6F1hOr0BQH3XM8xbwmy91by9WEOdWOCAJZhXsqX2v1orgeO1MNTOus8E6XH7pqIVQoejQRBSrzd4bFiC6-d-fxaMba_-1A7HiMlhKav3g6gxF4ybM4GnnPdvlxCOS8zKf8hVAnOOtVhABmTFsugZTlOgwp8BFcZgesRgEBXEeCMPbFXkFmdqHJ7dZiQkovQLQJ1-F8-aI3Ie9VqD73DSbhVPbfyiTt7t7uJuNo54LWltraZcyHzbZN2y4Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b32e36c8.mp4?token=AJ9l-gD7gomVIxnrvfSWIhJfJczJWvk095csTmlHhaBAGCl-HSY1uOX1FC8EIq85AOyLJWnhnnCEMbJim0eSuHUjthn6F1hOr0BQH3XM8xbwmy91by9WEOdWOCAJZhXsqX2v1orgeO1MNTOus8E6XH7pqIVQoejQRBSrzd4bFiC6-d-fxaMba_-1A7HiMlhKav3g6gxF4ybM4GnnPdvlxCOS8zKf8hVAnOOtVhABmTFsugZTlOgwp8BFcZgesRgEBXEeCMPbFXkFmdqHJ7dZiQkovQLQJ1-F8-aI3Ie9VqD73DSbhVPbfyiTt7t7uJuNo54LWltraZcyHzbZN2y4Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسخهٔ بانک مرکزی برای مدیریت بازار ارز چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/466869" target="_blank">📅 18:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: جمهوری اسلامی ایران در راه مقابله با رژیم سرکش صهیونیستی فداکاری‌های بزرگی انجام داده که در رأس این فداکاری‌ها، تقدیم رهبر و امام شهید انقلاب اسلامی ایران، سید علی حسینی خامنه‌ای (رضوان‌الله علیه)، قرار دارد. @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/466868" target="_blank">📅 18:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: نقشی که جمهوری اسلامی ایران در قبال فلسطین و منطقه ایفا کرده و ایستادگی آن در برابر استکبار صهیونیستی، به نفع همه امت اسلامی است.
🔹
صهیونیسم و بازوهای آن، جمهوری اسلامی ایران را بزرگ‌ترین مانع در مسیر حمایت از مردم فلسطین و مقابله با طرح…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/466867" target="_blank">📅 18:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466866">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: بزرگ‌ترین خدمت به رژیم صهیونیستی در لبنان، پایان‌دادن به مقاومت اسلامی است؛ مقاومتی که در برابر طرح صهیونیستی برای منطقه ایستاده است. @Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/466866" target="_blank">📅 18:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466865">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: رژیم سعودی در ترور شهید عماد مغنیه نقش داشت و از همان ابتدا از تلاش‌ها برای ترور دبیرکل حزب‌الله نیز حمایت می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/466865" target="_blank">📅 18:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
رهبر انصارالله: تروریستی اعلام‌کردن گروه‌های فلسطینی یکی از مواردی است که حقیقت موضع سعودی در قبال مسئله فلسطین را آشکار می‌کند
🔹
رژیم سعودی در محافل رسمی لبنان برای خرید مواضع فشار می‌آورد و همه را علیه حزب‌الله در یک جبهه مشترک با رژیم صهیونیستی و آمریکا…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/466864" target="_blank">📅 18:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
رهبر انصارالله: سعودی‌ها از مسائل دینی علیه امت اسلامی استفاده می‌کنند
🔹
بن‌سلمان اعتراف کرد که رژیم سعودی از تکفیری‌ها حمایت کرده و دوستان سعودی در این زمینه آمریکا، انگلیس و اسرائیل بودند.
🔹
سعودی‌ها از عنوان «جهاد در راه خدا» استفاده می‌کنند و امت اسلامی…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/466863" target="_blank">📅 18:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44953e3252.mp4?token=ObDFPDevIzlz_rVfD7ZSKpJbmcqJof9wwiIP0WrSj0w48FGOxbL8gsMTQSPSLB1zsPxc-X7h15z8Lld1GSxnIZgcttSoQ1DUF-TNtEcS6WFElGGCMLXmgJaoUxI1Vv8NMowIJq4OY9QKtax0l_KcXPBL77Yxq6BiqcpD5kVEhz_jnDaVIePTbMP5SIdNwu--esstsPKKSZ2H8CrMgFnA1Npk6nNf_wnN0WpIJYPKskN8z0TKF-3LxfdQOuMrl7kCp6pAO4fKQVxv2DaW0zQmNnnD5Fu9Eq08tLgKF25-9zphzG-Eucqr_Qpd0ZBqx1Y-hahSfiCxlok14-3E3eyTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44953e3252.mp4?token=ObDFPDevIzlz_rVfD7ZSKpJbmcqJof9wwiIP0WrSj0w48FGOxbL8gsMTQSPSLB1zsPxc-X7h15z8Lld1GSxnIZgcttSoQ1DUF-TNtEcS6WFElGGCMLXmgJaoUxI1Vv8NMowIJq4OY9QKtax0l_KcXPBL77Yxq6BiqcpD5kVEhz_jnDaVIePTbMP5SIdNwu--esstsPKKSZ2H8CrMgFnA1Npk6nNf_wnN0WpIJYPKskN8z0TKF-3LxfdQOuMrl7kCp6pAO4fKQVxv2DaW0zQmNnnD5Fu9Eq08tLgKF25-9zphzG-Eucqr_Qpd0ZBqx1Y-hahSfiCxlok14-3E3eyTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رهبر انصارالله: انگلیس رژیم سعودی را ایجاد کرده است
🔹
انگلیس رژیم سعودی را ایجاد کرد و نقش مشخص و نامطلوبی را در جهان اسلام به آن سپرد. @Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/466862" target="_blank">📅 18:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
رهبر انصارالله: انگلیس رژیم سعودی را ایجاد کرده است
🔹
انگلیس رژیم سعودی را ایجاد کرد و نقش مشخص و نامطلوبی را در جهان اسلام به آن سپرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/466861" target="_blank">📅 18:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466860">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدای انفجار در بانه ناشی از عملیات انفجار کنترل‌شده ارتش بود
🔹
فرماندار بانه: صدای شنیده شده در منطقه، ناشی از عملیات انهدام و خنثی‌سازی مهمات عمل‌نکرده باقی‌مانده از دوران جنگ بود که توسط نیروهای ارتش و به صورت کاملاً کنترل‌شده صورت گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/466860" target="_blank">📅 17:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qkg4yzbl0ohO57E6IP1tjIChgfp0TYRIbZn6wzDj_NVMpDRArWxAlCCMObsk8lG5oxlOk3MNKGYwzdk2AKkhx1LnlihNam6wyRMr-E0v4REhCT7G-LIniWu9ziROjlNSRCXoztDQ7QYryPn0aogADiO-N3XCmSmH0ZLJhjrksilzNvphEYOH9Sm3tBdoAx6nVkIYiIuyoa3glUhpP_YDWTvCmQOsWPw_IEdyE8EM6u8L4VW2Kr9Gy_1E3NHqViVdrZ-yq2Qecfhh6u0q4-ctbrH15np5j8THeNmdbXhd2ilONvwfrQBVbVHolyc-DMl6XN5BiL15q6mpyg7S73PUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtxueVoItqfZnAZgDLCb3Se2ussMGSL_Xd8JlWokBl233H5lvpsruW6-7D-PpkFdJkLiGE_5SjggHpzYiYe0zL3cNdZs6FwrjxkVCloRSHBn02IuBbYsMsAWbOcOiz3Krtr7wwyySMvyhDvWg6Qp7K2E2pGXA8Ez9xAAyZqen2MO3dz25CRXtziPXJrYx8GnHEoy88x4DVCDcvzQPPI9xVcoCVpwqRKImBZoXGx14qnokC0o7NemQLtOEVpxK8RRs_sr8EjWn4pMi9lpb2b_gfbHfMSb9E3tyaoPBvmP3PqVn_8gLsewh_598aC2jEnRYJNgpUjt5G8On0LxMzGltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcTy5TFRs5HOAoeVq3-M7l3IBhvls5ZW8Lqx3RxykDY9S07SsMc83TQuMLaCUfwu4xr0vReHiFkQCpW8b36tFcN1cdxXlF6tnpseKsh_1TvHo3yHQ8nPO09zdtY6rpHVAgP9bfgoCA_eoPZq0yV45qv-8sZkH7U8UOp3qLNlKuulQqS_T9bg5B8x_Z51gOgbf_PqLWiA0HU__L9pfDZ3nUAZhTVslDTCL-4mZCAiX5dqQHOHeA2a4ylSHH0EELvdO9BLRcCDV5JBBA5ptMpr0_Bz6wC8Uo7TZoO58YMzg-9jilegwaWz_VUJtT8Snh-h3nSqvXP9KWCfIUX1FpvyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okxOTBpjTLYT97PZlfKQIxhPskPNenPcL05hIchD_wOockrvsWMNxD0WAgM9TtcwGfGI-tDPtAJMTGsCgKYkiTc37mP6uIN1PYpNTe9-RZtCjzWgiWkumZhkMxm3uSadLSSqm0fHSZMc0EcSm7ksZf6tM37gy8QsmYYW0NIe3dGPSPd5BAXMqiok2FYatvYMZf8PIrk3-ldCaAyZiAd6SzzzvQyN1DPmZjq9q3ysNfIpkURCjMZr6srsjzPGL-lAwxgJG3Yy5I_4aHXEHuiv2i_wkJuhTHFV87zLeICouJeWB9ip2NU8xu8HicKxoMqLvogrjCi3MLB01aDFYsyn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3SJmNQDYSJVe1CjrNH20sbbfoBXuI8-0Ivpoz7fqOzdyIUNJ-uPxLP-9_p6O9Hsx3bJPwEI3t8Yc7rU5OFeS-LoRUIhWMOlWsSNZM4ZaCssJNF6f09cWJ0NEsd0MOtNrowhF-AN2e7GXwRV6ScaFjFzIufS4niZsy3vlz6VfX376vTIv_XkKd8TuPl95cHp0XSjVzOh23UJJ5ifEpo8IwjeOQ4XooDvSr_8WgROTVQQc0BDahSy8VB9CdfmiqTVrfbmUW8X--s7eEphWQwLkcdpy93FoO0NhN_QWyB7-3TTqDsjI3Vr8dxTgEOSGXGsxnpE9NIX6bSPS3sT0YQm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJYyOhnT_zpB8HpQkczJj49X7QJkbvcrGdc1pto4moCoisoQ1jDAOnfm04gvzDi8aMLkz_UVG_DFVvxRO79Up8mqB6KD2_ytKbRtS8ORNf_ULzuIkVwRsU8nJ6INzvqkeeLNXD8nyfeJO5JVuTLWXV-q1AnkC6EgzbwFD92wDzDG2W5u0GHmLD2c2ZvXKfusBRg71kP0I-pgt3WJrezcctvjzPy_exP7ihpWvyp3ZJXZb0E7Qq4eOG0ZsOMlNdEbPc2zuS4Bvjso7SX_cdUhG1JlV0Yy6PEg7CEI47uKRrydHfBeA9Q7Ua4csx0bhGKHYHr8FLyd3ZeQipB149KN4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مشارکت بانک صادرات ایران در بازسازی قطب علمی دانشگاه شهید بهشتی
🔹
بانک صادرات ایران با هدف توسعه زیرساخت‌های علمی و تأمین مالی بازسازی پژوهشکده لیزر و پلاسمای دانشگاه شهید بهشتی را از محل اعتبار مالیاتی بر عهده گرفت. این اقدام که با همراهی وزارت امور اقتصادی و دارایی انجام می‌شود، گامی راهبردی برای تقویت سرمایه‌های انسانی و «ساختن آینده» کشور است.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#بانک_صادرات
#گزارش_تصویری
#بانک_صادرات_ایران
#دانشگاه_شهید_بهشتی</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/466854" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyBQWrx-xwn5gae4TwLrmZbHN5Lqz78Icn9w37Mk9EUg1QC9mI_FXI0zASBpfzHO_177vLfbX242N5hezYRaJp829oisY21nBUWSsomj3SEPh8Wzj41ZRX2AP_gatcaciOkR4gLY0dRHLUlZYbGi1eBM_k2qqnfA3ocMqQHAjEDKCqolefgC9kYmtupJ6jivb6TBgaItWuTTtcpTnvYZ0Eky8KteVYU-9pN8SPHsGjv1kZd-2ZEW-EeMzwjPmH3Ya3JERou-Cdnf9MGtKBgvCC9K84y1I9M4hmD8ilYWZszmwEWt04GK-MOKYP5kODFoYV9VCiXXIJnDtTVckCTVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید اعضای کمیسیون اقتصادی مجلس بر نقش‌آفرینی موثر
#بيمه_البرز
در چرخه اقتصادی کشور
در نشستی به میزبانی بیمه البرز و با حضور جمعی از اعضای کمیسیون اقتصادی مجلس شورای اسلامی، نقش کلیدی این شرکت ۶۸ ساله در تقویت اقتصاد ملی، حمایت از بنگاه‌های تولیدی و مدیریت ریسک‌های کشور مورد بررسی و تقدیر قرار گرفت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5108</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/466853" target="_blank">📅 17:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/466852" target="_blank">📅 17:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1e3f4f16.mp4?token=Dep9FpUxlvBpu7cq2qjvYLoHShdZNtjt2wxnfm9mh-xXF7q6ZpVqp7dOvdGo4yPOIMZRCtgL_lrGVik-jTmtouFv-I24SwIlU26bNIY6e88R6m7Ygu-wAOXdME6UQNFMKVL2JzFF7IL52h8XzTbyh9aglYDN0LcuuHHkwlStrSnDG_XKAE42zp2NgpXrL_SUMCAanbD6bHA_2kwX0eXMAJwuaOUODhPJtIrYaKheyKUHt5nYV9l76PoJmZTicY11O06NSVSpKixb-hlb-dgp3Oud4dfDq4OM-Z5x1V9NL48RvH_EHZv7mpklakPV-UEkDg3tELCaT3uAlTKkSeNOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1e3f4f16.mp4?token=Dep9FpUxlvBpu7cq2qjvYLoHShdZNtjt2wxnfm9mh-xXF7q6ZpVqp7dOvdGo4yPOIMZRCtgL_lrGVik-jTmtouFv-I24SwIlU26bNIY6e88R6m7Ygu-wAOXdME6UQNFMKVL2JzFF7IL52h8XzTbyh9aglYDN0LcuuHHkwlStrSnDG_XKAE42zp2NgpXrL_SUMCAanbD6bHA_2kwX0eXMAJwuaOUODhPJtIrYaKheyKUHt5nYV9l76PoJmZTicY11O06NSVSpKixb-hlb-dgp3Oud4dfDq4OM-Z5x1V9NL48RvH_EHZv7mpklakPV-UEkDg3tELCaT3uAlTKkSeNOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدال‌آورترین کشور عربی با صفر مدال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/466851" target="_blank">📅 17:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGE1EOrJQ51TIxifZt6bS1eCU_g_t42vUmWynsKi6UjndWsYpSYoc-VDuPhF2B8wwcQ_1V5rzUHbNwi-RwZQryecVdOBUj-n2oaNs_JW_yjF5HBdeSI7uzV_Ke5HSpfiUX2IdPfv1iOzMm_vrbOwTlsdtHKvVFUZvJ6GVb1umnum47WU1QU18LKOkWVMl6yMEV6mIk-UvB8w2um_AaZ1a6fBpXMLJaSoDj-As0A5N96bkMesQm_MBCNb2fS5ggXQtXQTVRFUIJxMDp2yu31UOWm61L40EC4JApPuFDa0EssU8KCkMmAVFBo4anrkXFcwXWtxiJ2c7unqxGm_5nFyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج : هلال‌احمر در جنگ ۱۲ روزه کنار مردم قرار داشت
🔹
حجت‌الاسلام والمسلمین طائب: براساس تفاهم‌نامه میان سازمان بسیج و هلال احمر، مسیر گسترش همکاری‌های ۲ مجموعه از امروز وارد مرحله اجرایی می‌شود.
🔹
تلاش خواهیم کرد ظرفیت‌های مردمی بسیج و جمعیت هلال‌احمر بیش از گذشته در خدمت امدادرسانی، مدیریت بحران، مقاوم‌سازی و افزایش تاب‌آوری مردم و کشور قرار گیرد.
🔹
مقاوم‌سازی جامعه تنها به حوزه دفاعی و نظامی محدود نمی‌شود، بلکه باید همه ظرفیت‌های مردمی برای مواجهه با بحران‌ها فعال شوند و جمعیت هلال‌احمر در این زمینه یکی از مجموعه‌های مؤثر و برخوردار از ظرفیت گسترده مردمی است.
🔹
در جریان‌های جنگ‌های تحمیلی اخیر، ۵۶ مرکز هلال‌احمر هدف حمله قرار گرفت و شماری از بیمارستان‌ها و آمبولانس‌های امدادی نیز آسیب دیدند.
🔹
هدف قرار گرفتن آمبولانس هلال‌احمر به جای یک هدف نظامی، نشان‌دهندهٔ ماهیت حملات دشمن و بی‌توجهی او به اصول انسانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/466850" target="_blank">📅 17:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساقدوشی سلبریتی‌ها برای یک قاتل وحشی
🔹
برخی سلبریتی‌ها با انتشار مطالبی در صفحات خود، به حمایت از علیرضا سپاهی، قاتل جنایتکار میدان علیخانی اصفهان پرداختند.
🔹
«مهشاد و علیرضای عزیز پیوندتان مبارک.» این متنی است که حامد بهداد به تازگی در صفحه شخصی خود منتشر…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/466849" target="_blank">📅 16:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThPrxFRh-9pe3Jwf5wC5jPwK0RCSQwlShw9Gr5pjy05VJmxTqfVlFo6WLJpds1EWXYFGfixJOExd-_aeg4zSK1-chX7F5LIO2sVts_q3HVUk_AdI2Gh2eosK8KC9lUHoY70q6IDeuuRA07A-5nBnrfSytFKEgLvRkY6cniEE1i-xM16TqOYjOKIXAlNuCzJyX5K6aQreYv_IN8p9EUM8N3ToDiiOAS3PcE9by_pfUWy-ef7PA8jlNB7wkN8vv9hMkRjri1q7K35XxD_20i7MZTBgIYckd15qShTscU9a2c76dxStB25NB7vsCXIZlkSAyBqVk33ycH4Sro4mr-FSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdr7T9nzez_1mXm_PdvVL-UTLWbTmku6pKqcDoTB3hvZEJYSWqlIZorS7Vzt2a3xSNoF9-A1hZWfFPbsSd5yQnGd-pNRZFC4mL2P2yHYMwYGP2HCkyX1_P8FRt02IvQlCAvboNjjM9Kup__9GmaWoark44su4uXqKvuYanlubxdBA_xs-HSZU9yF4AaIadny9S1wRd0VbE1qI2LPQSzkhxMinUc0CKm-vjR9cxtoxY7aZiggIbGfLVwBqBvF2e2QSbfaO-iUkdd8LP4V0n1LUV1FR_chUF0pc4sLYFYiY1MrfnjOmUdQWG7VTGnjSpeLCmw-bzEDNIGVk0TEdDRrzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عیادت نمایندگان رهبر انقلاب از آیت‌الله نوری همدانی
🔹
حجج‌اسلام والمسلمین رحیمیان، محمدی عراقی، محمدیان و حاج علی‌اکبری، بعدازظهر امروز با حضور در یکی از بیمارستان‌های تهران، ضمن ابلاغ سلام رهبر انقلاب به آیت‌الله نوری همدانی، از مراجع عظام تقلید، در جریان آخرین روند درمانی ایشان قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/466847" target="_blank">📅 16:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466846">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تجمع مزدوران سعودی هدف موشک‌های یمن شد
🔹
سخنگوی نیروهای مسلح یمن: تجمع نیروهای متجاوز سعودی که قصد پیشروی به‌سمت مواضع نیروهای ما در شرق استان الجوف داشتند را با موشک و پهپاد هدف قرار دادیم.
🔹
در این حمله ده‌ها نفر از آن‌ها کشته، زخمی یا به‌اسارت درآمدند و تعدادی از تجهیزاتشان نیز نابود شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/466846" target="_blank">📅 16:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWuzFew6gVBeT-x5Fwf_pLjYreLYpPH6bAzpp-XObjIapllwy8Ypv2-6q15Rmb25zULde2a9jUc2-v-mDaHuLQD5mWUtCZJL1uMyWDu4R1AW2lWPcfxsShlT7P57bVlbQX68jKS8nJfO7CwlG5y2pL5QMzOS3rwn-b5EiyYVoyCKuwwBN0Tld7M-BaNqlqb61exhSs2sBDd_8eXOV2mUKyU14nuTrTJre-ZjUuUDgnO1ij_GJkBt_m-RyzyMGmon5GGLFZmpHKEl66MBjaBIeyRq_w1MU2Ivp2erEGbLflqmRPiMTaPrdf3FJiGj3Q6pCgX6V0XFLwmIYbyjiOeAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dF2X-g5FfQfFvvSehcCShwSK90Hv7Yj9IPMq-W097n8h3pNoZRS8VJu_K6ytfixbQmW3oaHzPRnH5WwUR7-1-882h3e0wAe9pd-rJYLgadxEMeGpb1uxkz6FH1TRQNh6LD_sOWLeS8WwrqfC5ls1ZcAIQS6R_bCx85yvJ3EMTRcQ3Ld1hfNYMSV_aPtRR1PEDbhurq0LCCQF4BSWfSaVPjm4mDuAbjEWjvmTLM5fSOqC9Ke-U1VRP30Qz1k97sNPVWHDBRtHUT2gVqVlpxBOm31TCbEF3NgXuveOTCJDSn7WR6-I9OI8W_D_KFcmAPKmfsGFGBosRr4TRxaHxaib2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همواره گفته‌ام که بعد از دوران دفاع مقدس ۸ ساله، دوران حضورم در نیروی انتظامی را بهترین دوران زندگی‌ام می‌دانم.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/466844" target="_blank">📅 15:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کالابرگ دهک‌های پایین اضافه نشد
🔹
بنابود رقم کالابرگ دهک‌های پایین از امروز اضافه شود؛ اما پیگیری فارس از وزارت کار مشخص کرد، رقم اضافه‌شده تا لحظهٔ انتشار خبر واریز نشده است؛ علت این مسئله به نتیجه‌نرسیدن این مسئله در دولت است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/466843" target="_blank">📅 15:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4khqLUMITWVowJctxuSoJBUsCGe5QvQa5qLhLVsHMUww3_la8rCCA7jDVUJPSfhvtUQE1KzN70Q1F-SQOy-bFHf5YlUN--TnH_PZWdOPGlKmv09bzBRtNqfn9RBqG-aJ8LTVB3ZPQ9vaHz9a0qYlcLbhWxNO3GpCcFwgoMWM_PviE-Z1CPKf7NxcX7Ndh9GC5l-YINnCeC4m9hNuZth_JYRcN7ewbFgEh4ZU3ZkR4_49s-hzwFu5JN_39ng52Deb-pYCQLeKmj8uRaBW9SQ73bWJ_mjkZwMSBe5fWKCX7bN_6gKVI9GwaEztqg5b_XQoTx0D-qa22tTiLR6XanbHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برندهٔ نوبل فیزیک اعلام شد
🔹
جایزهٔ نوبل فیزیک ۲۰۲۶ به فرانسیس هالزن برای مشارکت در رصدخانه آیس‌کیوب و کشف نوترینوهای پرانرژی کیهانی اعطا شد.
🔹
این دستاورد راه را برای نوع تازه‌ای از اخترشناسی بر پایهٔ مطالعه نوترینوهای کیهانی باز کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/466842" target="_blank">📅 15:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419ab3f210.mp4?token=UiEnWtAoJnNnjQy6MyHy0Bvz-TjH3Nnz8LxSKx7fvphT9j4VbCX-D7I5pwamLcloiT95fFqY3DAsJAbyo2kzewlGa2BYMS-F2cuFjJH6WS_yz3Dwwn_t-y39W85EMy4puI8_6VjfM4WkdX6PPz2aQQ2kbXtwfieMWi-22GmVwwh6Lnizx2SLgfG5z-nSQOeC79mMuWXVP4XxQXq1HL8bng0_K4fGkrSBrPXyThLf1t5svr-feICwh_6nmP0w2s6Ff33Z-4t4FcgI58iFHltgMbTpAtwN2jiGGPLc4lCzPI5pflEKNMucEweJ8wUrePucxz57wvSGqQ-FxzRrCJ6qJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419ab3f210.mp4?token=UiEnWtAoJnNnjQy6MyHy0Bvz-TjH3Nnz8LxSKx7fvphT9j4VbCX-D7I5pwamLcloiT95fFqY3DAsJAbyo2kzewlGa2BYMS-F2cuFjJH6WS_yz3Dwwn_t-y39W85EMy4puI8_6VjfM4WkdX6PPz2aQQ2kbXtwfieMWi-22GmVwwh6Lnizx2SLgfG5z-nSQOeC79mMuWXVP4XxQXq1HL8bng0_K4fGkrSBrPXyThLf1t5svr-feICwh_6nmP0w2s6Ff33Z-4t4FcgI58iFHltgMbTpAtwN2jiGGPLc4lCzPI5pflEKNMucEweJ8wUrePucxz57wvSGqQ-FxzRrCJ6qJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: نتایج نهایی کنکور نیمهٔ دوم آبان اعلام می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/466841" target="_blank">📅 15:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پزشکیان فردا به ترکمنستان می‌رود
🔹
رئیس‌جمهور، فردا به‌منظور شرکت در هفدهمین کنفرانس دولت‌های عضو کنوانسیون تنوع زیستی، عازم ترکمنستان می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/466840" target="_blank">📅 15:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ielfZSzrGDGj40bW67Tfd9FZT4no_6cuFOAyptrmNvJHO_svY0rFCXHmnA0mDvfoGSvkrwVS41M8UcDGbhMbklSUJ8P3aC51yEFVpV_r16sj8kwtT5hdOWLnSpEakkBRCObufM88F84NkIVcni38KE2AtmApq8uOcu0bPJRNg35ur2Gm0JIEHxGelVYs0Fhgu1xcPz-gxDeli_N2XtMOfx59n5Qqem0TMZ25YJvM2M3OpHZX24CuThnra_x1UWEONnM7yYwh0TlNNAOqfSRbVPV8u7l04vwGdQ5G93y-HNmCiF61MaKSodGb08T3AXRJLfyyY518G2Sw8bQ35dGEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قریشی: بسیج عشایری باید ظرفیت‌های گستردۀ جامعه عشایری را در خدمت انقلاب و کشور فعال کند
🔹
جانشین سازمان بسیج: حمایت از جامعه عشایری یکی از مأموریت‌های اصلی بسیج عشایری است.
🔹
عشایر را نباید صرفاً یک «قشر» در کنار سایر اقشار جامعه تلقی کرد؛ چرا که جامعۀ عشایری مجموعه‌ای متنوع از اقشار و گروه‌های اجتماعی را دربرمی‌گیرد و از ظرفیت‌های گسترده‌ای در عرصه‌های مختلف برخوردار است.
🔹
بسیج جامعه عشایری باید علاوه‌بر فعالیت‌های فرهنگی و اجتماعی، مسائل و نیازهای واقعی عشایر را نیز دنبال کند و در مواردی که امکان حل مشکلات از طریق ظرفیت‌های موجود در کشور وجود دارد، مطالبه‌گر و پیگیر باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/466839" target="_blank">📅 15:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bff72e06.mp4?token=fGJ6VgqIieTod46m4D2wjtM-Q204VfDZv-4gcrKG5xEu3lKVXe7CvmoE_zM2NFut1X8zcQuwjO11rF95hDHzXFwTlcQNILabmfpUleSiqWohYRGUC89prMfo6_O_d1nEC75Ix0DBeO6NSSxYFebK2ZPfYJnUCEHVdBO4VbCmvNowqbtEhxvZXY2yqdprwbqfpma1jnQCm4g2YhHbFNNmrb_IYaDzHbMGpnx6PmqW_4sA4xsu53KRbPeOS_R8LOR_RQyOOcE0xM3wrazLogjg2fTcP5nHcikKjssk1VS4aqDAnEZwfaNcJJRV_L98kKRZAoerrDKhr1bldPjgEZWKNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bff72e06.mp4?token=fGJ6VgqIieTod46m4D2wjtM-Q204VfDZv-4gcrKG5xEu3lKVXe7CvmoE_zM2NFut1X8zcQuwjO11rF95hDHzXFwTlcQNILabmfpUleSiqWohYRGUC89prMfo6_O_d1nEC75Ix0DBeO6NSSxYFebK2ZPfYJnUCEHVdBO4VbCmvNowqbtEhxvZXY2yqdprwbqfpma1jnQCm4g2YhHbFNNmrb_IYaDzHbMGpnx6PmqW_4sA4xsu53KRbPeOS_R8LOR_RQyOOcE0xM3wrazLogjg2fTcP5nHcikKjssk1VS4aqDAnEZwfaNcJJRV_L98kKRZAoerrDKhr1bldPjgEZWKNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از دیدار سردار رادان با قالیباف @Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/466838" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8U8p7see-iaFIxJkyR74KtqVc2vg8QWWH_hnoky__02TKBj1syY7aknHBZNmMGas06JAWpaMTu7X5Ff3v7Pwyotu5zvaigv1bkNpxE6jM3CSIxb8r73S9V-4pv0cWQ9RBBC2__oqBa22SYX7FqZ1MbtJe_Yy7hZKQf_ILHpbeOl3gMTUnxK-7YuUWTah34NFD43zImd_bMN3MJda_ncPSPF_ndwE7C8aMch_VOWm-7Mnk5HQJW9a4MCnn2EUTILZ_Og79MaHdHXQJDM6hGIedsbfufNvozqY63ZJtX0srDCrVrJEJxGZARc6piK_KYx4j60ralRS841vDLrohHvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TA_ce-qZTZfBJDFYwPW87ioap_e3V8-isrqX-dHYzgi25Ql_dK87lut30CShgnxXArk1ATqmufQWbhyS2sgYWYDdFNlgRN7NE62fZ1BYerwPcL4CzebzPAWuTMuLPqn2tVx1-Q5tdPsC0BCB0ciNFdvEwLl96YYFqDPzlaHLV3wpQh2pKHjvBcOhjSEOsr5pBmbiplkZUcFXpQqVAF7ktwBH-kYYuRxvG5ZdCMFNUOs-RZ5UKU28baynOJLkqCt9rWd5EmDD_owYoIAYStGiwrMBlCcefoEFfVcAb5UT7PFKGpN0lUQ3rQr3vZhmEKU0yw4WAe7OBsEPsQSGf2lFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3P02hsCtNFuxqOeG_AXv6yRt8yFE3sje7FY9kFfxYQXFES_gsclyCbJeFcgQCRU8BQyk4Q3t1tkGI6jFf8kVENVyI_HfvNMRjAuOYI88Ybwvz60zSIoSvwxjVBiGOMaD3vAFTJINBmnZgEEnKMC5sUFFmGxT1KEFNxnB0yh9B8Z7oYAhzRbJOBq0Qiltdc4mPjen6SL6YX6GUAK6qU11iLJKnuts14h_rlMeSjTfuAY8mXM_3U_2q5vlttJrhhvJM4tiW46kOLm1E5T8ljVusdnCBW5zbCj-Of98sabQkmR9T64ZLrpYvhIRi2Z3BLw_r6GKCaD3bHjx69SuJ87Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5RPbRWY55Rs3XE1fmb2sb2IH4IAapYnLpvY27kF56bq7IonwgJp3Jae40kcD6--U4ok_pf_PC3uPVlPSeGUsTHstZmcyUn52MpZW_SY51G4wKGb-UoXmCuLuVN-edCvjVkFLQyWr6Id-lYaNwTOndbGkEKvwd0v5UzCG2WO8NxCmE3wMJdZTykox3dj-aMPVVdGdJeXVRCCgdLcRjo-gh9nTe7WgcjpTeJj9tq0tXPM_FnlrX0a3-K-xzZaN1AyU3YAR1nwcNgmgqmKFQde-tR90xjDJaP5_c7ZUzXrAn1ayzTB639dChWr3LRTzIoFdPF9Ydvc6k3-wUqZQ6LVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhVPIZDr-XD2wdLK_Z95kp5IzcgE9vD_8l9q7Y219AFK8UMJLj6XD1vNm42FMl9gFnd3dQyT0dDrXa0EBPcTssSVDV8_QtKAtD-n50RNhEje93qj8ee0Qsj3a6kUpjtwIDj5J9JoHJJtcFYUj5yX20jxVRB_JByjXF1izuRUXl_oN5WxeuFAyref9ufeJkG9IYe1o4luz2G1-FEOcS_8PuqQiPyvO9MAoJydxW60MVwaMuqgxA5_cBmfqRh5nWWlTprhAtyzpDN6JOsDr_Z0hRKABXh6YfK1h7g12NHWccfyiJCCLw7uCoZzGaB8YaB8yFsDid6FPvTEKkq5mwnmhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفت‌وگوی بی‌سیمی قالیباف با پرسنل فراجا
🔹
رئیس‌مجلس در دیدار با سردار رادان در پیامی صوتی از طریق شبکۀ بی‌سیم سراسری فرماندهی انتظامی کشور، هفتۀ انتظامی را به فرماندهان و پرسنل فراجا تبریک گفت و از تلاش و مجاهدت‌های آن در نقاط مختلف کشور تشکر کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/466833" target="_blank">📅 15:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گفت‌وگوی تلفنی پزشکیان و پوتین
🔹
رئیس‌جمهور ایران و روسیه، در گفت‌وگویی تلفنی درخصوص تحولات منطقه متعاقب تجاوز آمریکا و رژیم صهیونیستی علیه ایران، اعلام آتش‌بس جاری و برگزاری مذاکرات ایران-آمریکا در اسلام‌آباد پاکستان به تبادل نظر پرداختند.
🔹
پزشکیان: ایران برای رسیدن به یک توافق متوازن و منصفانه که متضمن صلح و امنیت پایدار در منطقه باشد، آمادگی کامل دارد.
🔹
خط قرمز ما منافع ملی و حقوق ملت ایران است. اگر آمریکا به چارچوب‌های حقوقی بین‌المللی پایبند باشد، رسیدن به توافق دور از دسترس نیست.
🔹
ایران آماده است تا با همسایگان خود، در جهت دستیابی به صلح و امنیت درون‌زای منطقه، بدون حضور و دخالت کشورهای فرامنطقه‌ای مشارکت و همکاری کند.
🔸
پوتین با انتقاد جدی از مواضع و استانداردهای دوگانه طرف‌های غربی، بر لزوم احترام به حق حاکمیت ملی و تمامیت سرزمینی ایران تأکید کرد و مواضع به‌حق طرف ایرانی از جمله در زمینۀ جبران خسارت‌های وارد شده در تجاوز نظامی علیه ایران و دریافت تضمین‌های امنیتی درازمدت برای عدم تکرار تجاوز را مورد تأکید قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/466832" target="_blank">📅 15:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466831">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d623562a1c.mp4?token=HywcRk4x-v2RAgi1VbB6Xqi5P8jQXgyDtMK5g2mhsAmjfMFJqksESWxTANCDAkWT2oL53RzPAEUDxVaJEPcjmFbw5ekyNqrlQwfbodIM8PwT2yzYlTtYwCGKCl1DIPZ1B1WHSxqcXCiiyd_pTwEEao-K9gDEOZWKVGt77p_tpb0kFtX8sdGxOlkSkZ-xDHO_ar0u2YBqj9-VHoI2XNAkyiRsbYHnysTkQHQYbounYQxfnAateQCOOn86DLwCCJYR1Ukp59-wudNw5oXZgYyc0wXZL2Ss_Fy7lxWSL4pGWBXRwIgfRED9mMAgT3W3TdqYLkOO6b1JJe8srIeR-w-DEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d623562a1c.mp4?token=HywcRk4x-v2RAgi1VbB6Xqi5P8jQXgyDtMK5g2mhsAmjfMFJqksESWxTANCDAkWT2oL53RzPAEUDxVaJEPcjmFbw5ekyNqrlQwfbodIM8PwT2yzYlTtYwCGKCl1DIPZ1B1WHSxqcXCiiyd_pTwEEao-K9gDEOZWKVGt77p_tpb0kFtX8sdGxOlkSkZ-xDHO_ar0u2YBqj9-VHoI2XNAkyiRsbYHnysTkQHQYbounYQxfnAateQCOOn86DLwCCJYR1Ukp59-wudNw5oXZgYyc0wXZL2Ss_Fy7lxWSL4pGWBXRwIgfRED9mMAgT3W3TdqYLkOO6b1JJe8srIeR-w-DEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرخ تولید تایر به‌تندی می‌چرخد
🔹
تولید ۷۵ درصد نیاز تایر کشور در داخل کشور انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/466831" target="_blank">📅 15:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5951552a87.mp4?token=CjlbtERLsMdiaME2sxiRlQ0Hx6MRA_zSFzbABE9kmG-kK-n33cCxoSz9YovBRAbIlCcEfvBYwbeGvh8gsZtghyBA25oL_GTXsGbxbwcRo9OuAC9mgdVmKloMVzZK4a2nogmi40CsfkkX3hk2yL1D4ia4brrO_UHmGgEsSouIUn2tpwZiHnFXBF9hpvkn0VWnLrquaNE8Qf6cLpu_AGIgPWZsAH_XRfpeyWskmuBXkDr8ANEscPCmETIkqjkBOOe1o5khFvX8lHnKa4KHn3ZjJSRaNwD5vTdjJI-59Zyy7BT2gZg5OdjNE6vEtVNvOWcyz48adYEyUcI1IFCqLp1DXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5951552a87.mp4?token=CjlbtERLsMdiaME2sxiRlQ0Hx6MRA_zSFzbABE9kmG-kK-n33cCxoSz9YovBRAbIlCcEfvBYwbeGvh8gsZtghyBA25oL_GTXsGbxbwcRo9OuAC9mgdVmKloMVzZK4a2nogmi40CsfkkX3hk2yL1D4ia4brrO_UHmGgEsSouIUn2tpwZiHnFXBF9hpvkn0VWnLrquaNE8Qf6cLpu_AGIgPWZsAH_XRfpeyWskmuBXkDr8ANEscPCmETIkqjkBOOe1o5khFvX8lHnKa4KHn3ZjJSRaNwD5vTdjJI-59Zyy7BT2gZg5OdjNE6vEtVNvOWcyz48adYEyUcI1IFCqLp1DXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزینهٔ تجاوز آمریکا همچنان روی میز کشاورزان اروپایی نقد می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/466830" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70cb544ed1.mp4?token=RsdeeDXgIGB25Z9vr50Hqtg4n-SKx8G-O7y8c1bKAyKQi7CmtgjbaQQn8cg7Pf9nkLl9MJlb4EHxi72yFzgFVb73VJ5aTI5hgNRMJvtFb9Ao9HBO17DVPBQig4TgQ_QBxPymt5uK3oPMPQeS0-7cBs64rQwl5lecE-W3WHuzl2qsWzK2O1H87GLzKbnmYfQAwgyYDz-_O3IEr1UBbMVFZwdygqkj6c34O_mPM676B6uHc68OIxmnoHcNOsRNGxIO0dOUAsx1EMfLEWyxj8LAj-gcAW_6qIQYvn1G73cbUa975iiDT9ekG86rO77VX7jbM-qI5Kf0jQPnmmqBMB8cEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70cb544ed1.mp4?token=RsdeeDXgIGB25Z9vr50Hqtg4n-SKx8G-O7y8c1bKAyKQi7CmtgjbaQQn8cg7Pf9nkLl9MJlb4EHxi72yFzgFVb73VJ5aTI5hgNRMJvtFb9Ao9HBO17DVPBQig4TgQ_QBxPymt5uK3oPMPQeS0-7cBs64rQwl5lecE-W3WHuzl2qsWzK2O1H87GLzKbnmYfQAwgyYDz-_O3IEr1UBbMVFZwdygqkj6c34O_mPM676B6uHc68OIxmnoHcNOsRNGxIO0dOUAsx1EMfLEWyxj8LAj-gcAW_6qIQYvn1G73cbUa975iiDT9ekG86rO77VX7jbM-qI5Kf0jQPnmmqBMB8cEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزی که طوفان خشم فلسطینی‌ها به جان صهیونیست‌ها افتاد
🗓
امروز ۷ اکتبر، روز عملیات تاریخی طوفان‌الاقصی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/466829" target="_blank">📅 14:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466828">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee8e50e3d.mp4?token=g9gA9-Kgp5CViT5yWhygNcxnE5NgUjEptJVFsyw3g22e8aEZJowOWIjNV5S85LShFZsAvRU7EphK85MxmtYrXWn5YD0hhbHneb55RlGgyJPKouTLYJTQc4qtqEAkdPOBzvT0NFk4HUPoXaa-_UQNv35twZcdwDxWPXeOllyZeY2vU73Z5Om3IssaHjwuua-hwYMBOjXkg8bq0L0lbZpq0msnPn8YRwG9AyUOQRNvoRGB6kY7ICszzeoLcCXqoQLgV0UpBtBoRZ9p3sR_K3sPEM1DwLhVbWdL_EwlUr7ygAz5MUkhPHRGbgSCEGYuatexX0pXFUNuSeh2f3aozY2zng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee8e50e3d.mp4?token=g9gA9-Kgp5CViT5yWhygNcxnE5NgUjEptJVFsyw3g22e8aEZJowOWIjNV5S85LShFZsAvRU7EphK85MxmtYrXWn5YD0hhbHneb55RlGgyJPKouTLYJTQc4qtqEAkdPOBzvT0NFk4HUPoXaa-_UQNv35twZcdwDxWPXeOllyZeY2vU73Z5Om3IssaHjwuua-hwYMBOjXkg8bq0L0lbZpq0msnPn8YRwG9AyUOQRNvoRGB6kY7ICszzeoLcCXqoQLgV0UpBtBoRZ9p3sR_K3sPEM1DwLhVbWdL_EwlUr7ygAz5MUkhPHRGbgSCEGYuatexX0pXFUNuSeh2f3aozY2zng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصرف CNG افزایش یافت
🔹
مدیرعامل شرکت ملی پخش فرآورده‌ای نفتی: با اجرای نرخ سوم بنزین، مصرف سی‌ان‌جی ۱۲ درصد افزایش یافته و مصرف بنزین ۳ درصد کاهش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/466828" target="_blank">📅 14:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466827">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a7905108.mp4?token=fKrTDzMV6Mz2Rxi4TljBgpzMYGaPp6bEDTU9m5gnn7VYa9VHnT7XNX2nJgaqx5cvbYhoaBgHeu9ku9bweROK1s2Viuz8Na8box__iemXbl2efk4oh6Gz7rI8-G5Qohr4vRjy-gdn2tQBY1ECWdgpU6ZfavKFsyM9KLH2ZX1rt684rBR53wGprojkdEWaEhEGtYeH1yAyMxMDrmOtWWhilTu2AMaWM5EBX-2lhNTiIeWaVZvtBfjZIoGpw6Tw-eiCScRWSmwXd5E9YEC3DVGtNO_EQBZZcs-XlcX9dtcGxJLZva39d2fk7Wx9xqVY_Nu_MAdyBQcqaMBCjMgFaB6buQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a7905108.mp4?token=fKrTDzMV6Mz2Rxi4TljBgpzMYGaPp6bEDTU9m5gnn7VYa9VHnT7XNX2nJgaqx5cvbYhoaBgHeu9ku9bweROK1s2Viuz8Na8box__iemXbl2efk4oh6Gz7rI8-G5Qohr4vRjy-gdn2tQBY1ECWdgpU6ZfavKFsyM9KLH2ZX1rt684rBR53wGprojkdEWaEhEGtYeH1yAyMxMDrmOtWWhilTu2AMaWM5EBX-2lhNTiIeWaVZvtBfjZIoGpw6Tw-eiCScRWSmwXd5E9YEC3DVGtNO_EQBZZcs-XlcX9dtcGxJLZva39d2fk7Wx9xqVY_Nu_MAdyBQcqaMBCjMgFaB6buQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقشهٔ فرانسه برای مداخله در ایران که نقش‌ بر آب شد
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/466827" target="_blank">📅 14:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466826">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c37d1fb097.mp4?token=EMizuBdf9mwXeVjqNfLrQ1Ru0PvBVBLgO0gJYOBiDAcY02R6z3YTIXRd9Dq__6nfzWUblS-YS26qWhJfkKk-60ByrhvwdhVablcDO-oqED02eOoB7AqW3y4jT1yJZQkJfwuAJaQLFz-4HSuNMaSS2aoztQyiti_-tlcK2gAmQOhSjJyV7TmvmEp0j59sBwdKqKKjGJIkpeR9Z93AE0veAWwvqkjLPCi_5oYyGGxj6KAUZQGb0pDRPqQGeI9r5_37_axN6yLBbGnk8ETy1AtQFrq11OJDc3X2JsABnlohNwWpjFimIrqnJwn8d2-gi0Hh6Rl_Eh5FHaYmdVQ77gw-hjWtw_PQsKSUGk3RDH0ZGXpmKAt_CiK1kQe0a1Aijelz11ot2B5OfxNKw1VYmSyHFmJ_daGKpEol5LyG7llGZ6AlmKJWlQfFkDJwgM63awbkK_MAOKGR9I5rufcR1ySltz60liDMbGY7Q4TbdsGVObitD589i8Ju4wJd_G_0J1TJswvm4O4fybhKKQaV5eUrCDdtZs1Su4VZg9Kgp9-u2uJpr-Y7C-Dn8XfwpnU-Q7W1pKojD9Gk29NfIrUF5UKoi0StahgvD_hx6AmhmbinixfW6pdfeqUgbbLwPjXSxpAwxRieFKQrEFMhClXwR75ejsHEmQw8IjfRGGs7Ww-6lBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c37d1fb097.mp4?token=EMizuBdf9mwXeVjqNfLrQ1Ru0PvBVBLgO0gJYOBiDAcY02R6z3YTIXRd9Dq__6nfzWUblS-YS26qWhJfkKk-60ByrhvwdhVablcDO-oqED02eOoB7AqW3y4jT1yJZQkJfwuAJaQLFz-4HSuNMaSS2aoztQyiti_-tlcK2gAmQOhSjJyV7TmvmEp0j59sBwdKqKKjGJIkpeR9Z93AE0veAWwvqkjLPCi_5oYyGGxj6KAUZQGb0pDRPqQGeI9r5_37_axN6yLBbGnk8ETy1AtQFrq11OJDc3X2JsABnlohNwWpjFimIrqnJwn8d2-gi0Hh6Rl_Eh5FHaYmdVQ77gw-hjWtw_PQsKSUGk3RDH0ZGXpmKAt_CiK1kQe0a1Aijelz11ot2B5OfxNKw1VYmSyHFmJ_daGKpEol5LyG7llGZ6AlmKJWlQfFkDJwgM63awbkK_MAOKGR9I5rufcR1ySltz60liDMbGY7Q4TbdsGVObitD589i8Ju4wJd_G_0J1TJswvm4O4fybhKKQaV5eUrCDdtZs1Su4VZg9Kgp9-u2uJpr-Y7C-Dn8XfwpnU-Q7W1pKojD9Gk29NfIrUF5UKoi0StahgvD_hx6AmhmbinixfW6pdfeqUgbbLwPjXSxpAwxRieFKQrEFMhClXwR75ejsHEmQw8IjfRGGs7Ww-6lBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۲۰ تجمعات شبانه حال‌وهوای متفاوتی داشت
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/466826" target="_blank">📅 14:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466825">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20587ffb2.mp4?token=HzUO32thaqIyDzKXFjDlSj7TYJzeYBx005aXgy6vjB04hv3ZWbOw1DYcrc3GuCbHRK2ljr0XxUEkWWuzLeXS-FDRApCGxXTXQsuHobovE91RFCnfVePx_wlxWW7-TRuIB_xXWjS-wK5B4ms_x3zBC626xNupkQ7xS6kPpXZQWTz7_YIcVi6di2tFxOqLZi9qseyntMqfIdb41xiHwjtvsuEH4NDRyNRj5qcQi8HwdfqXLEQ3i4eUcpTkIrfWMojhIw2vMc5B0Y9rlNhPq5uDMDUoTmoHQJYF8t5A0EZPXgspvw5HYrJd6NVqCOZjjFcMd5kRWY8l4uP228XAHoRX_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20587ffb2.mp4?token=HzUO32thaqIyDzKXFjDlSj7TYJzeYBx005aXgy6vjB04hv3ZWbOw1DYcrc3GuCbHRK2ljr0XxUEkWWuzLeXS-FDRApCGxXTXQsuHobovE91RFCnfVePx_wlxWW7-TRuIB_xXWjS-wK5B4ms_x3zBC626xNupkQ7xS6kPpXZQWTz7_YIcVi6di2tFxOqLZi9qseyntMqfIdb41xiHwjtvsuEH4NDRyNRj5qcQi8HwdfqXLEQ3i4eUcpTkIrfWMojhIw2vMc5B0Y9rlNhPq5uDMDUoTmoHQJYF8t5A0EZPXgspvw5HYrJd6NVqCOZjjFcMd5kRWY8l4uP228XAHoRX_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران سالانه میزبان یک میلیون و ۷۰۰ هزار گردشگر سلامت است
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/466825" target="_blank">📅 14:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466824">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMySwLh9UfGQD8nOZWfQQD2HLOGT_DZ_fwv4XNP4joi4lRwz8PZvR44EVuefASPIH4SwCU_ZakNtCfmrzYHKPzXtlp2asIDwhgK_LZ1ITyJwEaUA8MvrOcc-wveQVP858fYyXpwmmniPM5S2UCZXr61iBf43fiCwhVOmVe69dvwAOUFWpkkOGkvKbG5gf_C_IP4PkFzwbwwzwGt3sbyDBAN-XltOHuUK1RPQmBWTbEea1j9_7rxcwx-79ZITM1FviNjry2fW0PPQPTJdf8xRDD9x_bnpDiBNRtcrmOFFX59XwKG9pDhFuFR9ihQtW63hwNBDpqfc9eP3jN3vfG5pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: در یک جنگ تمام‌عیار قرار داریم
🔹
در شرایط جنگ تمام‌عیار، دولت ضمن ادامۀ گفت‌وگو برای احقاق حقوق ملت ایران، برنامۀ مقاومت را با قدرت دنبال می‌کند و نباید اجازه داد مشکلات موجود به معیشت مردم و چرخۀ تولید آسیب وارد کند.
🔹
قطعاً بدون شک مقاومت خواهیم…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/466824" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466823">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
سردار نقدی: هر زمان که رهبر انقلاب مجوز بدهند، برد سلاح‌های خود را متناسب با نیاز میدان نبرد افزایش خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/466823" target="_blank">📅 14:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466822">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
سردار نقدی: برد محدود تسلیحات ما ناشی از دلایل فنی نیست، بلکه برخاسته از سیاست ماست
🔹
برد تسلیحاتی ایران با تصمیم مسئولان، رهبر انقلاب و متناسب با نیازهای ما تعیین می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/466822" target="_blank">📅 14:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466821">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
🔹
مشاور فرمانده کل سپاه: تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
🔹
حجم نفت قاچاق‌شده بسیارناچیز است…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/466821" target="_blank">📅 14:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466820">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
سردار نقدی: مسیرهای غیرقانونی را در تنگۀ هرمز مسدود می‌کنیم
🔹
مشاور فرمانده کل سپاه: تنگۀ هرمز بسته است و نیروهای مسلح بر آن تسلط کامل دارند و این وضعیت تا زمانی که خواسته‌های مشروع ایران برآورده نشود، ادامه خواهد داشت.
🔹
حجم نفت قاچاق‌شده بسیارناچیز است و نمی‌توان گفت که تنگۀ هرمز برای چنین فعالیت‌هایی باز است اما برخی با شناورهای کوچک اقدام به قاچاق نفت و انتقال آن به نفتکش‌ها می‌کنند.
🔹
به‌زودی، تعداد کمی از مسیرهایی که افراد متخلف از طریق انفجار و تخریب برخی از مسیرهای صخره‌ای موجود در تنگه هرمز ایجاد کرده‌اند، مسدود خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/466820" target="_blank">📅 14:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466819">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سرلشکر عبداللهی: دفاع از جبهه مقاومت تا آزادی قدس ادامه خواهد داشت
🔹
رئیس ستادکل نیروهای مسلح: عملیات طوفان‌الاقصی فراتر از تصور رژیم صهیونیستی بود و محاسبات دشمنان جبهۀ مقاومت را به هم ریخت.
🔹
۷ اکتبر، راهبرد جبهه مقاومت را از دفاعی به تهاجمی برای دفاع از مردم و سرزمین فلسطین تبدیل کرد و به گفته وی، روند افول رژیم صهیونیستی را سرعت بخشید.
🔹
حماسه‌آفرینی‌های حاج قاسم سلیمانی، سید حسن نصرالله، اسماعیل هنیه و یحیی سنوار تداوم خواهد داشت و پایان رژیم اشغالگر قدس را رقم خواهد زد.
🔹
دفاع از آرمان فلسطین و جبهه مقاومت تا آزادی قدس شریف ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/466819" target="_blank">📅 13:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466817">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScMzOxpf5LCiyGWbiSqVcW2j6wc3YuEFPZl2gQ-1avrYldqmGUmWV9nSxQ08MTPY3A3Y98p2QOd1b00nCTvxBYPFunixk8SnzT2OiMxN-GjdzaVivrO3kVPXAEV_CBOTohwrdeDlnus4NptQSSajxMBr4aNAjXXb6qwQch71m4FHARLALpXGMof2zl9KLgwtKThaWxQJdSKvExXt3zmE-Z4JySoxkONWxAbFaMlb50EqxbBFq7jE7vn6hkw6Y2-8Pj8ye518FlngC5U1bgAQYnC8nuaiA4RXm3cL-XpbT1tqs3I9jIFER047O_WXb9lsZPsuntFm5FhXoh0IiOcJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
قالیباف: طراحی دشمن بر اقدامات خشونت‌آمیز در داخل کشور تمرکز دارد
🔹
این طراحی و نقشۀ دشمن نشان می‌دهد که که اولویت اصلی ما نیز باید تلاش برای ارتقای تاب‌آوری اقتصادی و تامین امنیت داخلی باشد. @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/466817" target="_blank">📅 13:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466816">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
قالیباف: آمریکایی‌ها در جنگ ۴۰ روزه فهمیدند که با این اقدامات نظامی نمی‌توانند به ایران آسیب بزنند و از این بابت بازدارندگی ایجاد شده است
🔹
به‌همین دلیل فشار جدی و اساسی علیه ایران را به موضوعات اقتصادی و برهم زدن امنیت داخلی کشور متمرکز کرده‌اند.   @Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/466816" target="_blank">📅 13:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466815">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قالیباف: دشمن به‌دنبال ایجاد ناامنی در داخل کشور است
🔹
رئیس‌مجلس در دیدار فرمانده و اعضای ستاد فرماندهی انتظامی کشور: همۀ تلاش ما این است که به‌صورت ویژه در حوزۀ زیرساختی و معیشت کارکنان فراجا اقدامات جدی انجام دهیم.
🔹
همواره گفته‌ام که بعد از دوران دفاع…</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466815" target="_blank">📅 13:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466814">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbo24Uig6K1VbCRGPygQ1EcJL7GciIw0cxITXwWV6IRvsxsEuAGFPiEza9sw2vHHPcI1FcbMF8lW_3JeEn0mansNmP0Mq8ZKMcD-uzGlgLDLr825J_RN-tPat0nUXJqtrWRo_VaFsEUsND1I8b0GczV3mcO8Q4m821XLytNyng0nSU2ij-LpvgDfQQx3J3ALanx_onHb41z-Jp8QzX-pW2q2f0Pvjuid2joy53RKz7afhY9N-K0I4eHdBdjLlGaxNBEUawDufHhnboQtvkgVx3I5j4yN2z5Rily6oINHittmaNKxf31RO1deSym2MSRP7H8bI6snO3WfGASJJRbwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دشمن به‌دنبال ایجاد ناامنی در داخل کشور است
🔹
رئیس‌مجلس در دیدار فرمانده و اعضای ستاد فرماندهی انتظامی کشور: همۀ تلاش ما این است که به‌صورت ویژه در حوزۀ زیرساختی و معیشت کارکنان فراجا اقدامات جدی انجام دهیم.
🔹
همواره گفته‌ام که بعد از دوران دفاع مقدس ۸ ساله، دوران حضورم در نیروی انتظامی را بهترین دوران زندگی‌ام می‌دانم.
🔹
فشارهایی که نیروهای فراجا تحمل می‌کنند در همۀ شرایط جنگ و صلح وجود دارد و پرسنل این نیرو حتی در شرایط عادی نیز به‌صورت ۲۴ ساعته درحال انجام وظیفه و عملیات هستند و این جزو ویژگی‌های کارکنان فرماندهی انتظامی کشور است.
🔹
قوای سه‌گانه وظیفه خود می‌دانند که برای تامین نیازهای همۀ نیروهای مسلح به‌خصوص فراجا در حوزه‌های مختلف زیرساختی، اقتصادی و معیشتی اقدامات جدی و فوری انجام دهند و این موضوع با جدیت در بخش‌های مختلف دنبال می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/466814" target="_blank">📅 13:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466813">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOJt2YISyf_TR1zOuomoqBMycKBqPCjz7Rps-PXOnOeYTTeaga3fimTLpfjQlx8vnKXMo86VuDyd_iKC_PvG831hAlPzi4WMS5nAxlIPCTh_jgC11U-IhPr3Lw5JPxMl7k6iyXv8b6m4g_9paVgywdeBJ-Soqy3sZWKvB_60Cv9gudWeT8fto11AMOcV6Oug-mkYR_uZy0Jml_I48g06z2RIYnlesVUgwWVX9ief3b6bguYMj4iC53Tma9rE4k_qVGtsRJIHB0OtdMtRo2vIjLLS1f7ASWlH6kfD_5uDGuhGw3p-Zm54EsLDk_oiZNVqSba9Ac_ZXvvJWWp-V5O7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از جلسۀ امروز کابینۀ دولت @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/466813" target="_blank">📅 13:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466810">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jv-5tibfWSXlsxsdN3TmDhLHOWrg8DKms04Qur61aJxOayj5pacdnZG4pT8FLhOlbSElDnmZDVaAFXo7clLvKw2SvNTHZhX2YUN4ogD6ibEAo57DlLb_VlVNuOzxnlBsZFfWbSBey5qhl56K9FVrSgVn-6c6EVNUJnJLzi83DH-B7gu0DCT8VefdRclKWoLbgm1CnVQpaGcw-D7xWvSfgde9tuSOQYwkgxvSQAKUY1NJ8fdIEZ49iAWFMG_MYeOPiZrWuPyeFDYFhKuDU_JGVl3RKt0AHEBwu6T_tq2KU0-c7hjnNxxSsKWoKiUbaRrkyiW5B_mUgBSfQXuBTcSEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBgIV9kbQPJITOjZ_X4NRIcq-4no0wXwBSQQ5CPJxRw0l3WAxfqMSQoyQI1AAZAiXhu3hJtaeDdB196sYIzHAdBL0y3JUyzr5zkzTYAGd9fmYC8tPDvA1gPIpBxJS3mQwvIXucEoyKjHw3svbiPknN2T_t_uft1xKaMgWanx-LouTyx0LZ6CSQr8x0XAN-_s0i_C6ZKVqxe305ojlOv8bA3gholX4TIyH3TbcnX4SLsxdih83XcI9PfOR0mlBnC4H-SqZ0CXl2rdyvIJ6sXJXMRr35l-yNKN24ffa3IU8IVMffzV_zISwbyd4V47RTdbCBkKR0w6uz0aLwJkzqithA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kvb5jZ_G-vR3ijJoOH2FcmzgXeX7DJ5OczVajRyNwbbvCWAYob2vxh-kcgFoCR3RTHDrufDq6zGJSr-Mn-tJnvKSL4qOjlIzBmsr9cEpfhGwIdz8Ceb7NijGMRmiVyrr1pDjHHkh9YIhAAoGDcF0anzxIzbvABx4hwRfOqsZnubR3xnSr_kQgaebsLFZXkuhoR14t0K-P8jv1tZDHbKztKJ52hzm3wMUfAWEo9GXqx4__JCl3030wXR6ldzJbTUHJrNuF2kx8NrlPAjIHPgwam3rT3x92KAiRk7xFkIY8DKJBaCGOwu3LZk82J4LDFzo204bCajh_82p_GCaKMYhWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از جلسۀ امروز کابینۀ دولت
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466810" target="_blank">📅 13:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bjgyc2IP34_CIyRlvnI-Us33By-X9nj6fy7KltAbU9uVp-yQPnHMZV0wkS-C4pa-tOkxJH9QU-Mx3XGeak5uBI4hnEmgBhb-blGBfa-ye0LSkzX1_ZoYnB6hy4kPvz4Xzozi36zWNbHVCYYZ3QM5h3GxUHySYQ1qVh-M_zDwAk767TLvLspPknCocCiY6H4ZPZME2L4H4pYbEPTTQ2z7aUSXBBf-Bga_BG2nP4abEP_OVv8qq-mXc4uSM_lqFGm1DlM1bTOUw7IPIK2ypuUvX3IWgC8QGKOVhW-xgIU_qA8Pp2aqwx3dvwXWYNJKDJRuEoyVqWDrdgN0RgZiJrH1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: انقلاب اسلامی روزهای تیره سلطه مستکبرین را به روزهای پرنورِ جمهوری اسلامی تبدیل کرد
🔹
آغازین روزهای ماه مهر، یادآور ایّام الله و پدیده عظیم و ماندگار دفاع هشت ساله جانانه ملّت ایران در جنگ تحمیلی اوّل است.  در آن روزها تابش گرم خورشید انقلاب…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/466809" target="_blank">📅 13:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e96ac0df.mp4?token=VUNWiHVKV6obmG2LFXA2goM4uHbgW36uS3KxfubbGmbct-k61QjKutuDqAdE8WhZoquZvac2hcO_gptj4JQlWav7dMvmrSDDAfLM9zsEe3GZPvJRDf7Pkvk4lSVnXoWO1HKk9M2Rj16EpZpVYgZ_GkYfVKGKLSsJfGgFMw13T1geZyvFoIkljs2jRVcdalgi_TkZNKdcN7AjzRU28ncddyOBGO5ViyWq3Uk0vPjQs3_p6aWbaNnjkT_9y0QrV2APnUZd0igpFTHQCNmegue6fTUrdiH5oCfXPYHEZah0n-qiMFrDBwI8xNABbPS8ONPt0zpvCp-ZYOeUdxqPg7N6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e96ac0df.mp4?token=VUNWiHVKV6obmG2LFXA2goM4uHbgW36uS3KxfubbGmbct-k61QjKutuDqAdE8WhZoquZvac2hcO_gptj4JQlWav7dMvmrSDDAfLM9zsEe3GZPvJRDf7Pkvk4lSVnXoWO1HKk9M2Rj16EpZpVYgZ_GkYfVKGKLSsJfGgFMw13T1geZyvFoIkljs2jRVcdalgi_TkZNKdcN7AjzRU28ncddyOBGO5ViyWq3Uk0vPjQs3_p6aWbaNnjkT_9y0QrV2APnUZd0igpFTHQCNmegue6fTUrdiH5oCfXPYHEZah0n-qiMFrDBwI8xNABbPS8ONPt0zpvCp-ZYOeUdxqPg7N6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش: تجهیزات جدید پدافندی و آفندی در زمان مناسب معرفی خواهند شد
🔹
در طول جنگ تحمیلی ۴۰ روزه از تجهیزات جدیدی نیز استفاده کردیم که در صورت لزوم، رسانه‌ای خواهند شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/466808" target="_blank">📅 13:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFDtK9kxuFRMB-oQgqlVIhe7CrwN4WjNBjdVDJ1Z-e2vrOFJRyGXPHxnnUAcSdbGY2QQ-EzfaHK1-tgWItsmSvvahU5csBuknFWuAe5dQHWBNJ4rdtiBPk7MnDJSuFreH4IlJnHZgnEyPaJz9MtHPwREWIl_G100iR1hDnWfm2sKGYmRL6SGzAiXRFqb6jVPNnX1AoiFx9FaYLguMbxwp68AqAwc-wYGf7Zfr5d9AdYBS0B0oevxNaHMn5s21yef9rIqNuJDl1NNgpidNwjkKG8Wq60lO-Gr_08o3sIItjHxOP448fk8jLY7TA1TOocib-fJnuFaGcPWvQg8gfqj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوترها به خیابان‌های تهران می‌آیند
🔹
همزمان با آغاز طرح «اسکوتر کن» در تهران، شهرداری از برنامه‌ریزی برای توسعۀ استفاده از اسکوتر به‌عنوان یکی از شیوه‌های حمل‌ونقل پاک و مناسب سفرهای کوتاه‌مسافت خبر داد.
🔹
برنامه‌ای که تشکیل ناوگان ۳۰۰ دستگاهی اسکوتر برای پلیس، ایجاد مسیرهای ایمن برای تردد و اختصاص تسهیلات ۱۵۰ میلیون تومانی برای خرید اسکوتر را شامل می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/466807" target="_blank">📅 13:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtKL0_5ZF8xo1aCc0sG5xmaeFNa6StRHJ4b73A9_X7kySlvqFyj-WIvAvyZ_XTu_dwl4qpWwUtHsNPXYXOA_nv7BMa2MdIhEsjZNPxanWjeSNZ46RlI6zXNavlOKLrvlN_LPt0mOPikqf0XgTJvdbS295S00JRVQL7_D9NFNTExp-hqEw-gbem3MHXVBS-2t_cbjfyykvfkOUxmT0_GYy94he3VSNWB0IxsZ8dbhHZWenTF0PJ5fELNbMMeYpOYB5DcTM1IYq7kXSotewbEcuNB6RVHPH0xL8OaLlhLCGEThveND6bIGKtHyqmXg4BY5N5YImLLHvrXpCeT0lV_xbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم نیروهای ویژۀ نیروی زمینی سپاه برای شرکت در رزمایش ضدتروریستی شانگهای وارد بلاروس شد
🔹
روابط‌عمومی نیروی زمینی سپاه: تیم نیروی زمینی سپاه پاسداران، به نمایندگی از نیروهای مسلح کشورمان، برای شرکت در رزمایش مشترک ضدتروریستی کشورهای عضو سازمان همکاری شانگهای،…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/466806" target="_blank">📅 13:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8KH7bwTpPsCIIKyAo63jdAgCVWPKkAl4bR8226m_sRa_arXDgU8IFl64ChuOyqID1Yx1wqVm0i5MEhKQrhltJqSggw8I5tA6aSov4epJKwmP4IyoJV71VCNUXE8O-gSj5q_rSn7wLM_4jLkeFVFsHJL9eQZ_SBVWQfMnsA3l5YMYD-eY7MeK-nmWiRrUuZOq74cHZAKX3OgBd6DcZsifKU1moSAfcuWVsJG2vZJqn3pxh-rghKLUIrEkjrwr3noM7hzD57Eu4tv0HxWOl5w_zU7h6D7XXHi-sW0wxAHD2eVQ-xFmH9b8j4Dc6bbC60JrNera9HJzxgIPiYXLclQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حکم ۱۰ ماه حبس برای رسایی چه بود؟
🔹
حمید رسایی، نماینده تهران در مجلس، در پروندۀ شکایت محمدباقر قالیباف، رئیس مجلس، به ۱۰ ماه حبس محکوم شده است.
🔹
موضوع اصلی این محکومیت، مطلب منتشرشده در نشریۀ «۹ دی» در دی‌ماه ۱۴۰۲ با تیتر «دستکاری قالیباف در اسناد…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/466805" target="_blank">📅 12:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwcdvuWz7M0vbX1LQXctenqwSEJn3hKmUmTAl0dSY-8jJL_NsIr3cBsSMc2eay4Ql_HG5ergEeZiyK-t3me0F5EASxXI8IKgCL9Ld1EGDSlVDby8aBu5jWIp7AfDjGKe7sETGBzxW0Pje1MfJYiG6tmU6II9wauyZhj_6mPqoeOEqpcQmW-wrqHKYvTAX0RHfMK_Al0NV6R359ym1REbt5OAdRwQceZXwVd9kjnoAz1-P5fRp1YaVR8qhuSM4mh0orI5G-WzgcyQsl86rkWv22l5xKEF_zaf0gI8yl4kz0lljp38m7lZYYg5bBI4H3zbU4yeBFtu5C2hPKLs56blzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف ۱۵ شوتی سوختی در میناب
🔹
فرمانده انتظامی مینابِ هرمزگان: درپی توقیف ۱۵ خودروی شوتی، بیش‌از ۳ هزار لیتر بنزین کشف و ۱۵ متهم دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/466804" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b9357478.mp4?token=YpTjeq3RbrtTXbgv8mw_1ryyjfJnUC8lpXKDEBE1djbvhmV2JoMx1cAy51YecS5InG4VSRM3qVKsI-bn98a-PRnV5Qv1ReevNcJGgp2qeYYZNRdQa_RktHzMu-sLP4y6J3q92KU6AL2FS--obrRjpkh264QtdWWul_OZw0aQTfA4I3KwXWxIC9Y0UzWtCqJ5OYTtVIc0fdDJaIsmLKhMYbIr7p4FgWMeSnQrdse48hypaIgg0tklSWkZksnUCUHFxWDPi6g12Oj4vhfK6mduT-SNJXXb0Yqe9CD0EbtI0c0gkx7WVdWAgsBcKVzkLvp3slmTh40VVHqcEa_mcG7u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b9357478.mp4?token=YpTjeq3RbrtTXbgv8mw_1ryyjfJnUC8lpXKDEBE1djbvhmV2JoMx1cAy51YecS5InG4VSRM3qVKsI-bn98a-PRnV5Qv1ReevNcJGgp2qeYYZNRdQa_RktHzMu-sLP4y6J3q92KU6AL2FS--obrRjpkh264QtdWWul_OZw0aQTfA4I3KwXWxIC9Y0UzWtCqJ5OYTtVIc0fdDJaIsmLKhMYbIr7p4FgWMeSnQrdse48hypaIgg0tklSWkZksnUCUHFxWDPi6g12Oj4vhfK6mduT-SNJXXb0Yqe9CD0EbtI0c0gkx7WVdWAgsBcKVzkLvp3slmTh40VVHqcEa_mcG7u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: ۸۰ میلیون دلار برای پوشش خسارات واردشده به کشتی‌ها و هواپیماها توسط صنعت بیمه پرداخت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/466803" target="_blank">📅 12:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پلمب تالار متخلف در قم به‌خاطر هنجارشکنی همسر علی دایی
🔹
پس‌از حضور علی دایی پیشکوست فوتبال و همسر وی بدون رعایت حجاب در همایش مرتبط با یک شرکت خصوصی در تالار کهکشان غدیر قم، با درخواست مردم و دستور دادستان قم، صنف برگزارکننده پلمب و برای عوامل برگزارکننده پروندهٔ قضایی تشکیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466802" target="_blank">📅 12:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkVyclI9CnvQ5XdFeVOKWwbbrS7QaDmumkYBRlzqgOEyRAR7Ew-Y09IaOs7Syly2vHETvt8cFwV05egRTamvmJFCkrUnvbsUjzHF0ZyyAmeY1zwXHF1pahjiqVBaWT17mmb-4mgsHdKH38ueJv2QuTT0lMCELVWhSR6hLiazS0GHZONUSRdolyrYcz9jPevWYGjtCRn0_knxe0iR4cMYk-SJJptHP-nWGLA7wFUmOTdAMOL8joctS6WoDjO2cNU5fghJx21poA_skPr-W4sGSDzi97_5E5FUtQR2CKSAlRsB3QSDn7i__ZR9WAj1QzaWdNKuL8IRWoLs9WRe2qfxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ ۳ گروه شارژ شد
🔸
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔸
خانوارهای تحت پوشش نهادهای حمایتی
🔸
خانواده‌های نیروهای مسلح
🔹
طبق اظهارات وزیر رفاه و رئیس سازمان برنامه‌وبودجه، قرار بوده اعتبار برخی دهک‌های درآمدی از این ماه بین ۳۰۰ تا ۵۰۰ هزار تومان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466801" target="_blank">📅 12:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دستگیری شرور گروهک تجزیه‌طلب در ترکیه
🔹
یکی از اعضای گروهک تروریستی تجزیه‌طلب که قصد پناهندگی به اروپا را داشته، در کشور ترکیه توسط نیروهای امنیتی دستگیر شده و به ایران بازگردانده خواهد شد.
🔹
فرد دستگیرشده سالهاست به گروهک تجزیه‌طلب کردی پیوسته و فعالیت زیاد و تبلیغات گسترده‌ای علیه جمهوری اسلامی داشته.
🔹
خط‌دهی به عوامل داخلی جهت آتش‌زدن و پرتاب کوکتل‌مولوتف و مواد محترقه، شعارنویسی و سنگ‌پراکنی به مغازه و منازل از دیگر اقدامات مخرب این عنصر گروهک تروریستی است.
🔹
همچنین گفته شده او از عوامل اصلی آموزش و سازماندهی و هدایت اغتشاشگران به‌ویژه در فتنۀ ۱۴۰۱ بوده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/466800" target="_blank">📅 12:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH-pJqMdDfau1HOHC_qYSS4ta_WwEsRZfN5PFrcB-E0Nb8elQPDCB5Uo2Hf-lAlKE1IUCoIMS0J1Ws_Qxh0qpQoeJv4sf8obfKFa-7_0w6SrgBfwvoqTcWjUkEWnrlFB7ej0raLT7VjxJytyh_yfoCS8QkshuqFti6DzV_RRiPBPRpzMySH8qJmZxLahdOLQoACQagH_aIN1hSI7PP7T1JZ0DvRuCZ-qnSb3Pq7Zg_h2CMLqHeCjpkAi7UsDtdvufkMDFb2uASRb4s6CoJJlsDLcFKAhzs4AyMYJfbE_w7hB2ErziMfFqhz3_lKOMdrWiQQ43PwgTuxCc-1--ddGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادری که قدس را حمل می‌کند
🔹
طرحی هنری با موضوع فلسطین و قدس، با عنوان «مادری که قدس را حمل می‌کند»، در تهران اجرا شد.
🔹
این اثر با اجرای نقاشی بهزاد حق‌گویی، نقاش برجسته با الهام از شهادت مادر فلسطینی باردار در جریان جنگ طراحی شده است.
🔹
قدومی، نمایندۀ حماس در ایران: پیام این اثر و ایده‌ای که در تهران اجرا شده، قابلیت آن را دارد که در شهرهای کشورهای عربی و دیگر کشورها نیز اجرا شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/466799" target="_blank">📅 11:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در خمین
🔹
به‌دنبال اجرای عملیات کنترل‌شده، احتمال شنیده‌شدن صدای انفجار طی فردا در خمینِ استان مرکزی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/466798" target="_blank">📅 11:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466797">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzJIi8R1PTTy3sMzSzkyPTL42M_sl6-YFBgZdcrWwNfLKren-MwJapT_Q66-QPizW6o3xfnkIpCRZgtH2N7EEJwi51Z83NEj2z_Jic8PBAZUJ4So7TQA5DCp138_YtMw0r1UVB5BSrwt64QX8nHfNuPpkabDdzzykRVu2CGy_XbHt1fsNhxlz53MdQ5MlTuDsk_IDJ9KDgQ9xkUxEbEQDtRdJbVta2MP280Z_sms02Trv1eHeghXunreCD8Om_vHDo4-Z-hPoyZE8-ban_Q1bfqNwaRIlDamOjdUtIkBoi6MBPyWRVkqe3y2VI5HgYGr236LPAqNsC81C67tJcIr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: مقاومت همچنان می‌تازد
🔹
حزب‌الله لبنان در بیانیه‌ای به‌مناسبت سالروز طوفان‌الاقصی: ۳ سال پس‌از عملیات طوفان‌الاقصی، جدل دربارهٔ روایت‌های آن همچنان پایان نیافته است؛ اما آنچه بر همگان محرز شده، این است که دشمن صهیونیستی نتوانست به اهدافش برسد.
🔹
در…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/466797" target="_blank">📅 11:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466796">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69090f317.mp4?token=Rj71Tszbc_OQYrqYxFm-47ou7Sb4gJZ1SIvoJhmaB5OBu9fN9nthoVEUOOvD7gtIHXA0ajQK-gATPRf4wXBwFCa6_957BY-TqAqkUfu1-mdtAEmG8WGxG7wdyzD659ESpRxhSf9WWbmmDwVL0TqbPX_o9Xxs0CKM6qVqK1YMlq2KHkwjYskEkVsHJ5wZLr9Inq3e_cB2Va3vjsSMzRNAz5j_CG75bP7RpAPVBVFr36nOUe92_oPQJe8Af4qz7WlHVHZ1P-12hMXvfwFwXtse32pxOYGD4KFP_BBGdMpI8b8AAo8GGlBRaF3ASi9V-07yOuDGBtsW6LgMRv9B4cMvWbZWBtMO8xFkZ7169CC_5FPcREP6joSoIW5FMkTHjiDtbXofva-ehm052Gim_Y_CbYgFIVV-BITS-0QrdcaNBE-egqSKRW1tHOgAIzd0IyEo-ZWLgN3dZOkz-APkWJbG_0fYFxoNPfEMw930cALfJGwnZYhQsLPG4NGtrdNKuZZ838b6-bTNqQ2LmBqmNsN2wQXYR74i81l2aSyFcDrpgQgheq5ZDt6NfRe1-FbJSELRlZRrdq9oJWFZqPQgiaff0_AAc62qvIOA0VzoA0EU7X9Bn_o2Ef7FeSZw_JL0Z4_hwK6fqh2INEP0jZ7RhfSO7DqLO2Gzr7BdP4s3x5grOr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69090f317.mp4?token=Rj71Tszbc_OQYrqYxFm-47ou7Sb4gJZ1SIvoJhmaB5OBu9fN9nthoVEUOOvD7gtIHXA0ajQK-gATPRf4wXBwFCa6_957BY-TqAqkUfu1-mdtAEmG8WGxG7wdyzD659ESpRxhSf9WWbmmDwVL0TqbPX_o9Xxs0CKM6qVqK1YMlq2KHkwjYskEkVsHJ5wZLr9Inq3e_cB2Va3vjsSMzRNAz5j_CG75bP7RpAPVBVFr36nOUe92_oPQJe8Af4qz7WlHVHZ1P-12hMXvfwFwXtse32pxOYGD4KFP_BBGdMpI8b8AAo8GGlBRaF3ASi9V-07yOuDGBtsW6LgMRv9B4cMvWbZWBtMO8xFkZ7169CC_5FPcREP6joSoIW5FMkTHjiDtbXofva-ehm052Gim_Y_CbYgFIVV-BITS-0QrdcaNBE-egqSKRW1tHOgAIzd0IyEo-ZWLgN3dZOkz-APkWJbG_0fYFxoNPfEMw930cALfJGwnZYhQsLPG4NGtrdNKuZZ838b6-bTNqQ2LmBqmNsN2wQXYR74i81l2aSyFcDrpgQgheq5ZDt6NfRe1-FbJSELRlZRrdq9oJWFZqPQgiaff0_AAc62qvIOA0VzoA0EU7X9Bn_o2Ef7FeSZw_JL0Z4_hwK6fqh2INEP0jZ7RhfSO7DqLO2Gzr7BdP4s3x5grOr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بسیج اساتید: شرط التزام به ولایت فقیه را از آیین‌نامۀ جذب اساتید حذف کرده‌اند
🔹
پیشوایی: شرط التزام به ولایت فقیه، شرط مربوط به حضور در اغتشاشات و ملاحظات اخلاقی درباره اشتغال افراد دارای فساد، از آیین‌نامه جدید حذف شده است.
🔹
آیین‌نامۀ جدید هنوز به…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/466796" target="_blank">📅 11:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxzN4FShU69mmZyTS6Q3tSO_eWBHrsK3lS9l9JyUnjKiUajN1jI2Z_xq7BzMfBt8nf6BtjfrFNTeuEyPSiOwW58AJ4Tali-bwJg8dFDlys6-gF9V2i6G8pkFWapdoSDunjlERFkBJGSyTcRrXyc71RjuL3pplVoRxUSkl_k-2Wx6G6i1-OM3YO7Ff0bzMCD-rHmYY1v0KVbis6MGiJO8RJOyiN2CVHpX4AkHgPaKqBmTFUhVVwRg4JPSf9WNV9OpvMkkTl0LBB4ngWJM-8ZIZX2xkqLqNwWycnoOKaG4-4hwH06PzLT5WpOS4Jq654ka7RFbeCUa49sR8S3UskMRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: مقاومت همچنان می‌تازد
🔹
حزب‌الله لبنان در بیانیه‌ای به‌مناسبت سالروز طوفان‌الاقصی: ۳ سال پس‌از عملیات طوفان‌الاقصی، جدل دربارهٔ روایت‌های آن همچنان پایان نیافته است؛ اما آنچه بر همگان محرز شده، این است که دشمن صهیونیستی نتوانست به اهدافش برسد.
🔹
در حمایت از ملت مظلوم و مقاومت‌کننده تردیدی نداریم و محکومیت شدید خود را نسبت به نسل‌کشی صهیونیستی تجدید می‌کنیم.
🔹
سکوت و چاپلوسی برای دشمن، چیزی جز تضعیف حاکمیت آن‌ها و توانمندسازی دشمن برای تصمیم‌گیری درباره آیندهٔ کشورها و ملت‌هایشان نخواهد داشت.
🔹
دشمن صهیونیستی با وجود تمام موفقیت‌های تاکتیکی، در باتلاق شکست گرفتار است و مقاومت همچنان به مسیر خود ادامه می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466795" target="_blank">📅 11:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JooX7BHRyh_tLA0UO4dFYnNlFwGpLYdH1GTJrFwBb2JV3NPPbgXh9LULVsDS8HH-W3PCoHGgHEXNsLPEsZjkoHLhwQzLM6NfKREbm6oIis-_KpK_Zv3nV_4nd08HRgqyRvuwGDiakbGpfRtdICWEZA6P_YXlgOn7WviObDYuRSp7oCrY78MpY-jC2MhWUmIGHNNshS_lweS5rwg-WuOMldl50FQmpXfArEymMWalj4xbFRZBrfabRYIIDIGdehnqbIgoTZKMvs7TCTVDW_qSGdeyM2noqK28pFNnqAVjezM1IB3YBxlBd_QpD1aPkuoRmiGYzRK-cRjdgKORSVYxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGki_eLItaR8icVShA4-Qh_h2OjCg6J4YLdLNPtMYzfl0heuy16z09cMee48uJOVlYB2FE0eg7ufsFI3wUSFrsC5i4Zh99zoySAjL8OkMRFgX8c0_b2RJs1_RxrFsaPnBbN6MGJrGbUsfFZu6rKZ8-VTT4ni787Qk6zGSKo_YnIyO_l7le4AGr794Ultneo8_iCWZ6cl-nS--XmC4U6_4RcWIR2qZhcYbS2zh8cP-CO9zyMdg8N1bKi04MK5sl6rLIQwsCltU6Md02XouxLBo8JbXCiAyLTsQkzFUs9Lm0isYlZc9Hc6KoGVU314LVv_tVuXL4DY4GnRLIlCyDeAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3Ruy6TiLEvb6q01jgfbaHYFkWnRHbVNGs8XMgYRqQsVCikJS_bJKAdGyufY1YSdtFoYFKVUMEvHYs_2bZQ6vrtK9IkodUY0jOjrJKmxPAoF_j5XT2OZ8s4NCZNGtYhdivdrwrFPPQJPLzYcSUc6QCvXNTGP_idcdckwtkmzQ_uv6q7Z69YuSGv-sn6Dy-J1XdwrvYanmDd4mVC0zTbHKISP0XXWO5eNH2pl-QfIChru53nKFuA0MVUK0OizaSs-_sIsK6UZLUIpxKFe7TyAdjC3jSUAZxIYxU-sT8zDYNFC7wJyyz-rqsaE7udTyJH7-3j5rHOkrfab3iNaeTE_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/my_jFa5CgLO1g-NR2on3_ncKsdBBWwz58zf8KXdBw4PF2B2Kp2jH_qtMt8x8gb_Nd-Z9PXuZLmZyQwkanmSnB-YQmY3hCJJbxjtcRQxYA-_SEXFGPN3nc9aVvfzppV49X46IVqNprJ9ByeTfddgfH9_Ay_XNn1b2XSB25uEaM36HCH0olG0KT72WhegaGQp2vucxuhmJPortjddgLG_EFE4ze27I3LVZGeAqRPNfXjBVB6wafM3f5XpMy5Jy3jYqcpdcJmyKZ_Ri-OMujl_0OI1f1R-18Lt7L7HUfhd-eOAn7cBfx3aQXdn0lSF2c0PqeoOKhSbCAt-tdfRbxM8xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_8SdUcft7uHG0m8AG4t8T_nuhB6dROVnG7YD5zI-Jfa9zixy1ZWI9aVEGzKxbAFcbX600xHwO0EvDI9ryVa0fc9VYizxAoZMOwjfbC8lBTFEOIb8movyEJd5M_h6ev42hooO-JosHTJnxjOMD1qGsO6De7XECxzPnh2uxMWCgqbcOZuLeBVd4sL5LXeBQ1OR86W2hPYIWiE2aArC0fHxVajSInBsZIWgS3731oRAJELUo9k2W231QcJTf-4mZCSJG26h7VDF6aT3H7raEM-d3RbdyCEo8ocqRPGSI1S6JCco1IgVgCLVaT2nt09NDliTATAPl5W8IJ3lo0pGkAW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvYNrwsNfD2HOCZioCmlpxTJnMq1ZbElYbVB_aOg_e81M_XHXb1RxnDPw7LfAVbwcygLMaLZoZdGC2K9gQpx9mB8AABkTZBXCCYLadDkbjE20YhiGcxwb32-LcsZslMX5Z5O_GoRXVNLeqXG4dED-oUA4yQj0-KKyEmaF_h7BlO2U8zt36bMnNWt1xL_WH_Pwaymt4Cj_za2gQooUyjBLuuYRl6Yn4IKOBJEYtBKRmpI4toRhrCPD0eqpcYldp7KOdFcZF-Uj4UX5gPynALwDJmAjyAeKy5TZyTr_giOMspqiYBCI5bWgVaujf4fo349DyExsHBS7LYQNIg7P7vUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-yAmE0YLNS1NpoBJnb1wY8ycxsJZrRi46WQFMuLNo_ywdv8OGynjp9i8h7k12OO1mjcHN0MeiQrfQrPlVkxUoJP4E74ZcABN-9v26LGQaowV_7HlmuF_1UBjWSL90707616PKSzcRFIYTI7GsRSkXss8UY464qni5Q6bf6ygwgaovFnHnSSK1MHYShrHr2KxdW2kvSGYczuj37h1WcAL3dDUUblRee9-qX2CchH54H_weiqLFek03wEUDV0aHsDNou6SZ1cjV1nnj8r5xY4nMj0Locx2_IoULlPTm9bquoCADTRSvdPd1sgcWRk-ZtCgo24YQQuz7e-XZHsiAUaug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کردستان را از دریچهٔ روستاهایش ببیینید
🗓
۱۵ مهر روز بزرگداشت روستا است.
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/466788" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d43d555f7.mp4?token=GpQsBCI6Zgvg0KoFa1ChguvMzITWapdubpuqElR8vUIXWVLu4UCq7X0ubKPMEg6B6q2PCO8pOPyd0SzTj1dPlbMiSeYJX422OZPuxz2tdWh53I8Fiq_UlfmI1LGMHhMBNDnUREoJz-_lZ_NFhMbOkpZkS56m342qBQhuQ_7u2hHk3WdEhs0hb7W4Q6oa94_vS6kZBqvgAfnqI5GpxnCM02JtjIbgfhvCjGcxW3KhMsXTzLdL0GfLjuNKMpYdXdkEUGGfFQ4ElEVKoPz4o_3GjV64JkTo-Wcee6zzpunXxY9SbH0TiL9A2gMnZ5GrHMByLnoxq-sFUIBD7IRXh7dJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d43d555f7.mp4?token=GpQsBCI6Zgvg0KoFa1ChguvMzITWapdubpuqElR8vUIXWVLu4UCq7X0ubKPMEg6B6q2PCO8pOPyd0SzTj1dPlbMiSeYJX422OZPuxz2tdWh53I8Fiq_UlfmI1LGMHhMBNDnUREoJz-_lZ_NFhMbOkpZkS56m342qBQhuQ_7u2hHk3WdEhs0hb7W4Q6oa94_vS6kZBqvgAfnqI5GpxnCM02JtjIbgfhvCjGcxW3KhMsXTzLdL0GfLjuNKMpYdXdkEUGGfFQ4ElEVKoPz4o_3GjV64JkTo-Wcee6zzpunXxY9SbH0TiL9A2gMnZ5GrHMByLnoxq-sFUIBD7IRXh7dJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور از مسیر غیرمجاز تنگۀ هرمز، به روایت ملوان هندی
🔹
یک ملوان هندی با نام مستعار «سینگ» با فارس گفت‌وگو کرده و روایت خود از عبور کشتی GFS Galaxy از تنگه هرمز و هدف‌قرار‌گرفتن آن را بازگو کرده است.
🔹
او علت اعلام نام مستعار در گفت‌وگو را ترس از پیگیری حقوقی…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/466787" target="_blank">📅 11:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بازداشت یکی از مدیران نفتی خوزستان
🔹
یکی از مدیران صنعت نفت در خوزستان به‌اتهام ارتشا و تخلفات مالی بازداشت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/466786" target="_blank">📅 11:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کشف محمولۀ مواد منفجره قبل از ورود به مشهد
🔹
فرمانده انتظامی خراسان‌رضوی: یک خودروی حامل مواد منفجره قبل‌از ورود به مشهد توقیف و رانندهٔ خودرو دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/466785" target="_blank">📅 11:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پزشکان خواستار رعایت پوشش حرفه‌ای در کنگره‌ها شدند
🔹
انتشار تصاویری از برخی کنگره‌ها و همایش‌های پزشکی که به گفتۀ جمعی از استادان، پزشکان و کادر درمان با شأن محافل علمی و حرفه پزشکی هم‌خوانی ندارد، مطالبه رعایت جدی‌تر قوانین و پوشش حرفه‌ای در محیط‌های آموزشی، درمانی و علمی را به‌دنبال داشته است.
🔹
جمعی از استادان علوم پزشکی، پزشکان و کادر درمان با اشاره به انتشار برخی تصاویر از کنگره‌ها و همایش‌های پزشکی، خواستار رعایت قوانین کشور و پوشش حرفه‌ای در مراکز درمانی، دانشگاه‌ها، کنگره‌ها و سایر محافل علمی و صنفی شدند.
🔗
متن نامه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/466784" target="_blank">📅 10:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d99b27551.mp4?token=PP6alEozESVsnOx3QOT3hLvx2MNrWgqoV7fI3W_1wV-2ME-hlnYRRkOeiATZxdWY8VsWHxSSCeKx89ZpNlcVkQucb6M-HlmMmizjx_0a6L2GxPWa4iO-K5vtNZh1y7d1v7uLTEQ02HMUX67-eaLuyTv1_-RGdXunjNM54QZjSoM83wgif55A7NLjwsNwOo2yQ_Q3H7YsyYTtu6PBGqdT-NUX5r8k3XMgfsHABtHLpLLPadxcaCBtRmcRMLTfluLQj9y_vZXVyEwySr-0O8MehBYGQjrW6fQNT8eAp2iMyYFikuEkAKtKeTdiDogsraoinz8oPjDsxQcj8fkpWUTU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d99b27551.mp4?token=PP6alEozESVsnOx3QOT3hLvx2MNrWgqoV7fI3W_1wV-2ME-hlnYRRkOeiATZxdWY8VsWHxSSCeKx89ZpNlcVkQucb6M-HlmMmizjx_0a6L2GxPWa4iO-K5vtNZh1y7d1v7uLTEQ02HMUX67-eaLuyTv1_-RGdXunjNM54QZjSoM83wgif55A7NLjwsNwOo2yQ_Q3H7YsyYTtu6PBGqdT-NUX5r8k3XMgfsHABtHLpLLPadxcaCBtRmcRMLTfluLQj9y_vZXVyEwySr-0O8MehBYGQjrW6fQNT8eAp2iMyYFikuEkAKtKeTdiDogsraoinz8oPjDsxQcj8fkpWUTU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از روزی می‌ترسم که خدا از من سوال کند که چه‌ کار کردی
؟
🔹
همۀ کارها را برای خدا می‌کنم و دنبال پاداش نیستم؛ از روزی می‌ترسم که خدا از من سوال کند که چه‌ کار کردی.
🔹
اگر کسی که ادعای مسلمانی کند ولی دروغ بگوید و به داد مردم نرسد، مسلمان نیست.
🔹
از خدا می‌خواهیم کمک کند تا به‌جای اینکه بیگانگان را ببینیم، مردم‌مان را ببینیم؛ متاسفانه در خیلی جاها قصور داریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/466783" target="_blank">📅 10:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7JRlpyf_Odyf8cBBTiN5yZ_LlTbW_fOWi3HB9PXOcCM9iVkBia1DzpEcPgJphGalNQB3ZeRMDQ5qd-0GXTeADXnbIjCH7FSXLyGn5vdiwCBJ-fRfMyatuPMHNtnk4k7oPhimor-IWIx4EbX2_gA8kUpMrj13B5Y3aiQdaqvsUhfpvPpH99XHFy-3n9OMpYAtbUInA626QFlwSIKT-SV1zxpSmgbp8Een97SAPn9gzypVSHy5UW7ThvEAOkzqs96MIW55z-eIVGDBNqbehv8F8O0xcCi77dyp_7w39fQwspuRkodZXc4Ef2PmQt6GzjrQoOq2Tr3CfnCd4ctGRogzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/466782" target="_blank">📅 10:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6144b045a6.mp4?token=C76hujmq-jopSEccGnEY6ECFbJCLMwbHGGET78z7Prxbfi46DPrPJh3leYRiYoEixieVcBL4Tas-eQ9ECAfSdMKE3luTvx8GUWGNbRgYhC3O3MHhrPCSucq9v8eSaUI6d3IuVsEZ4fSMYr6cWc1gQ1NY299pGlR8znNK3lhB5mfYBsoflQ7VMprXYgEsgM9EUh9jhvheU9SaG26CeN8k5oIHHtk0CCjzYt-jJLug2UzvPjWNNXCzoYAOhDXUnw6iSVhjJDol98SN7CdB4WwUURfunbAwYUFXKxPdXLrLE1Yw3PSM8ediw17_-aSB4Avbr_NlwNrd8vsK-W0GuZjOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6144b045a6.mp4?token=C76hujmq-jopSEccGnEY6ECFbJCLMwbHGGET78z7Prxbfi46DPrPJh3leYRiYoEixieVcBL4Tas-eQ9ECAfSdMKE3luTvx8GUWGNbRgYhC3O3MHhrPCSucq9v8eSaUI6d3IuVsEZ4fSMYr6cWc1gQ1NY299pGlR8znNK3lhB5mfYBsoflQ7VMprXYgEsgM9EUh9jhvheU9SaG26CeN8k5oIHHtk0CCjzYt-jJLug2UzvPjWNNXCzoYAOhDXUnw6iSVhjJDol98SN7CdB4WwUURfunbAwYUFXKxPdXLrLE1Yw3PSM8ediw17_-aSB4Avbr_NlwNrd8vsK-W0GuZjOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دستگاه قضا: در کشور سند کم نداریم اما درصد قابل توجهی از این اسناد محقق نمی‌شوند.  @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/466781" target="_blank">📅 10:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466780">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b6d54fd.mp4?token=TPl9sKflgYrPNnO2Lse1ZViY7sYOZR8FmKXLe8z7a5tN3RIT0C0bsxJdKLaAmfIM3E9Q3LvtcCRWaTuc7tEUdVCP50L6yWSWu6ayiaBf71YB54G2XkaI4pVJbLt9koFVGPt5HxgePuCz9W7SwFnHIijuhY-h1za7kHQQBEQ-aitIYCy8eSIPW1QdCF_dq-RVaWTsX03xqLLNBbDCcbBQhmS3_pMmEQK4nsDJjtn2Yz_Op1BAtUh_E2My2VODg_21Q_BmHFiNp7bVYW5mYorMtuUKdIpKag28qJM77W_sUaiKguOtNMxROoNeXwGpBtzN2ZkBRiw-t6FnuhgngikfNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b6d54fd.mp4?token=TPl9sKflgYrPNnO2Lse1ZViY7sYOZR8FmKXLe8z7a5tN3RIT0C0bsxJdKLaAmfIM3E9Q3LvtcCRWaTuc7tEUdVCP50L6yWSWu6ayiaBf71YB54G2XkaI4pVJbLt9koFVGPt5HxgePuCz9W7SwFnHIijuhY-h1za7kHQQBEQ-aitIYCy8eSIPW1QdCF_dq-RVaWTsX03xqLLNBbDCcbBQhmS3_pMmEQK4nsDJjtn2Yz_Op1BAtUh_E2My2VODg_21Q_BmHFiNp7bVYW5mYorMtuUKdIpKag28qJM77W_sUaiKguOtNMxROoNeXwGpBtzN2ZkBRiw-t6FnuhgngikfNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دستگاه قضا: در کشور سند کم نداریم اما درصد قابل توجهی از این اسناد محقق نمی‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/466780" target="_blank">📅 10:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466779">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2722ca14de.mp4?token=Kgla3Y84p57ghXokBEkXYQ64z9qqD0pu6Zh-Ns7Lszsf33jrjRXQhJNvqiPP_CSaQZ4VTXLtJdnANfXiiLZiy2JGSq4eoCro8lXW7hK4FfKLdpVHcXDdnHsML3UkIfyrdxMI1ZQXrU41HELhoWR7CZltse_R2tU_rTobOqk4IWCvZ3DQir8sNzNzZtt3btlc5yRRPPx4tH-JanIjoh6jQd-DmPzNY4slufwDaiLHmiP9XQEW_OOkyZfci1aF8ogAyQRCkt5O0pOIbihQtl-l6fWBSijC2xEd-5gNG97NJGFWhrFN5YtTI-Y52Pdu8O0W4NQdYiS6epGumjNFP97nkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2722ca14de.mp4?token=Kgla3Y84p57ghXokBEkXYQ64z9qqD0pu6Zh-Ns7Lszsf33jrjRXQhJNvqiPP_CSaQZ4VTXLtJdnANfXiiLZiy2JGSq4eoCro8lXW7hK4FfKLdpVHcXDdnHsML3UkIfyrdxMI1ZQXrU41HELhoWR7CZltse_R2tU_rTobOqk4IWCvZ3DQir8sNzNzZtt3btlc5yRRPPx4tH-JanIjoh6jQd-DmPzNY4slufwDaiLHmiP9XQEW_OOkyZfci1aF8ogAyQRCkt5O0pOIbihQtl-l6fWBSijC2xEd-5gNG97NJGFWhrFN5YtTI-Y52Pdu8O0W4NQdYiS6epGumjNFP97nkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت ۲ نفر از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
ساعتی قبل، تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو فرماندهی انتظامی شهرستان بمپور که در حال گشت‌زنی و تأمین امنیت مردم بودند، حمله و به‌سمت کارکنان انتظامی تیراندازی کردند.
🔹
پلیس سیستان‌وبلوچستان:…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/466779" target="_blank">📅 10:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466778">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d81db205b.mp4?token=ODZnWjx1Uo7HlaYeZ-Lz4Xk5nmKJU_aoItm4DMKbHsy3gZzarNo_HpbW86OBKklRpVrsFs-f4do7EIzVgz4K1Z_xsyfalFTjieMGcHVJbcPeoiz3m8PZYv0Uq3B8yBlyBqUJlm1GS8Zb9EGoyg2_pjMY98LSlCPu_g7XPFN10ESCx-HZAgea1_3hKUfnS8e2bh294aouX2Krr3gyoDYrGYwggyGxwhK1ySN4MXuHZRPwXm6V4HZcTU-0lKcZgIatlSxPI5TRk1wpE09NWcXY1zDCmY-oiu8f-mMNa9z7zWHO1lqH81LVkC_TxyrSXSuAeIfFV873GCKzq7KdvWlRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d81db205b.mp4?token=ODZnWjx1Uo7HlaYeZ-Lz4Xk5nmKJU_aoItm4DMKbHsy3gZzarNo_HpbW86OBKklRpVrsFs-f4do7EIzVgz4K1Z_xsyfalFTjieMGcHVJbcPeoiz3m8PZYv0Uq3B8yBlyBqUJlm1GS8Zb9EGoyg2_pjMY98LSlCPu_g7XPFN10ESCx-HZAgea1_3hKUfnS8e2bh294aouX2Krr3gyoDYrGYwggyGxwhK1ySN4MXuHZRPwXm6V4HZcTU-0lKcZgIatlSxPI5TRk1wpE09NWcXY1zDCmY-oiu8f-mMNa9z7zWHO1lqH81LVkC_TxyrSXSuAeIfFV873GCKzq7KdvWlRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازداشت ۴۸۸ نفر در اعتراضات دانش‌آموزی فرانسه
🔹
وزارت کشور فرانسه از بازداشت ۴۸۸ نفر در چهاردهمین روز اعتراضات خبر داد. شمار بازداشت‌شدگان از آغاز اعتراضات نیز به بیش از ۵ هزار نفر رسیده است.
🔹
در جریان این اعتراضات، شماری از معترضان نیز مجروح شده‌اند؛ از…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/466778" target="_blank">📅 10:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466777">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGqgE2HUNilhP3d0An-_uBtpCkwoqiDk99PMU7FmH3aGOquFIGCJFC5SvCduoI5bcOz-j-Sd-T-SZ8DGFM94sSE5-DrUvznmAXXaODLOR4jRP7ZQArIZ8ZI0LCklL_w15JX5PZxEMWKjRIEJQL5hKp3IraUCvQYmFoGspJf0GlSkCuI2q-FhFnjLwoTE2ArtpUEIkRSi1Ebp5eHVGkLjaFSaI7Z-xbLR_whYjH3PUSuTa7uZHXTIOS69Ju0YG5kmaekayRqLZAuB1W-9KYxmkisTvor2TxbG_50AgmG-GB5aBNYtNT0W4WhJUVQh-PSa_XwuUuuBpWA4btVW6iJz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ طلا برای دوومیدانی‌کاران ناشنوای ایران در آسیا
🔹
در مسابقات دوومیدانی ناشنوایان قهرمانی آسیا در مالزی، امیرحسین زارع در پرتاب دیسک به مدال طلا دست ‌یافت.
🔹
علی علیزاده هم در دوی ۸۰۰ متر صاحب مدال طلا شد. علیزاده دیروز هم مدال نقره دوی ۱۵۰۰ را نیز کسب کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/466777" target="_blank">📅 09:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466776">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S70CBMSKp0DUzqqRPIqakHl495iQ_zWeCJ27mFsMzGxgUNGCuCPWxWl9NNog8SMcqub06OOxsLTh8yS3qOYX7H3_tlpGcE4KcOoSVT_WE67aFT13TAXCRFJKw48TnoqfWYZQeOjZQ5lSUSIY1eUNeIABRn422qyHJ430cvAbvgpQWTvq98dODDgyERO2mLKAwDkAqRnw8402BnmLvp7FqveuB_VrF9JEZp2IG4irNW5yJqNqL9QDf4EUBb_nq83nAFinWzoQHM9jnPpSUlR2Hkkw2jLNShSmPIlL_tWyi3syeZWh9TWC9_V8gledTGP-NxUXsZzYZg4vSePPAUlSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی: دوست داشتم تا آخر عمرم کنار آرژانتین باشم
مسی در آخرین بازی ملی:
🎙
دوست داشتم برای همیشه، تا آخر عمرم، کنار آرژانتین باشم اما وقت خداحافظی و بازنشستگی فرا رسیده است.
🎙
بعد از آخرین جام جهانی، زمان آن رسیده که خداحافظی کنم. ممنونم از همه، چون بازی کردن برای آرژانتین، بهترین چیزی بود که می‌توانستم تجربه کنم.
🎙
هیچ‌وقت برای این پیراهن تسلیم نشدم. همیشه جنگیدم، ادامه دادم و تمام توانم را گذاشتم. برای ۲۰ سال، تمام تلاشم را برای آرژانتین کردم.
🎙
دیگر کاری جز تشکر از این پیراهن برایم باقی نمانده. من همه وجودم را برای آرژانتین گذاشتم.
🎙
احساساتی که امشب دارم، باورنکردنی است. از همه شما ممنونم و اولین کسی که همین حالا به او فکر می‌کنم، پدرم است.
@Sportfars</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/466776" target="_blank">📅 09:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466774">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCztQD41ivqYyHYnJ-YnGk1wOc9VvWuPe2xKCtP8s5v8tr7aj5IdaCJhaULn1wmode3yL9VhAuoETwzkW7WWT2Qt1Zp5ehwzAdT7gz_mG9u63WI37OQoSkVKTsxk7-OzZTT63inlh89buLZnbCBcF991qhOuYspNByYFYhTRy6u4U9uGTvg3MRXEtPuL75inMItvxpl2o61zQU8AZ2Fs7zxVQYlYwltxV_kVWvdt7FQCZSDmnPsoAIgkEHANfAzCnSAzevkbWdONnlSCY_C6Ovfq3-nShMNg10K560XL8NLshLcSDo-yxScPy37Ri1k86ZqF7lSmQw3CxXj3gPCEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به رکورد ۸ میلیون رسید
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۴۱ هزار واحدی با ثبت رکورد جدید، به ۸ میلیون و ۱۱۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/466774" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466773">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moDuBhySQtnBURFYGFcfD_IoZHLUkEhaqSz2Vl8OMgfS_GebvCGhKoX2Km64GBvCm77uYi2kgJ8AyF6vskpZHNSmtt0LFqY_zeMQqfeKhle7NTINF4DZYvRU0MEkJNd1lVeSHunbmTxVg7yeWi7KtwZFqBzzdx8BtgEIiZ8lgIS8lsaK0vpLF0UTfAeV48kQlnuxZsJ5UHqHew6ABai6vz_m59vCjE-J82XrmkYiSVfO5dixaklrMEq65fg4qcmN9RuI_bM0Vg8qHSvVh4lw7J53bOfzzxbD8jXtAg7gBToFslnqlGkdJ3VsmBqFQZ1y31FndofdlkJ8nhAKcseeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/466773" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b443b53971.mp4?token=ESzb1ajJuDaZgxnwSAXcz8UmyJpX3947ZWbNSXU3VDInEiBSrDf8StTG3Fi841rOKh1R9nINArHE4Rp3c_Rg182xeLvCbdg_GEXZw1VLlct4VPzBU6gV0XxGWiMUu5Cec2aydY6aOPZrJPHJCQXSsVWmrbz407PeWHdoCk74Vs3ppbl7Ooi0NbLViDbS4uzkdV9Rb8NEOO4iohs-0Aiv7TS3j6eaVBYwzLYcLIdVwiQQbLVCfnhEGRiKs2nHnXvuItSpiS-GioLb_d1leYbJKBrzLrrff4jO2Ih6eQaT6PIzymbGwocjymNZd4zH7g-vjCyK86xg4ganlRHL8lj5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b443b53971.mp4?token=ESzb1ajJuDaZgxnwSAXcz8UmyJpX3947ZWbNSXU3VDInEiBSrDf8StTG3Fi841rOKh1R9nINArHE4Rp3c_Rg182xeLvCbdg_GEXZw1VLlct4VPzBU6gV0XxGWiMUu5Cec2aydY6aOPZrJPHJCQXSsVWmrbz407PeWHdoCk74Vs3ppbl7Ooi0NbLViDbS4uzkdV9Rb8NEOO4iohs-0Aiv7TS3j6eaVBYwzLYcLIdVwiQQbLVCfnhEGRiKs2nHnXvuItSpiS-GioLb_d1leYbJKBrzLrrff4jO2Ih6eQaT6PIzymbGwocjymNZd4zH7g-vjCyK86xg4ganlRHL8lj5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ثبت احوال: نسل جدید کارت ملی با قابلیت احراز هویت برخط بهار ۱۴۰۶ رونمایی می‌شود
🔹
کارت ملی بیش‌از ۴۰ میلیون نفر منقضی شده اما نیاز به تعویض ندارند و معتبر هستند. برای این افراد کارت ملی نسل جدید صادر می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/466772" target="_blank">📅 09:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11569a18b.mp4?token=T7LQ_mm0WoDpflhRogHK2QW7fSVe9bRbOaeuvFWP7KKR_bBECr7Ts_rMaiDx0qnZD4UMaKWMCLRWcUeqMrt9XxMTiGzZ4XLyjReIbiwVblnBhnoM5MLjQYFyorCA8mkDOg82Dx8vPFqo6Dqv6MXmhP1QJGX5wfNRgLolRyb5PWO3Z7BnpJwO3fGg-tPwDYmX-Bste8vinvOldBEdG1I8t0oCTLWBCl4qb68gac4d07iOpQWygDDc393wpwXnQ-8p9xcaRNf79fLhzpXBdB3AdiDlA1EvhlOAb7X_Z5FtAGdzkuMlMLxX2ZHVU57WZjMlO0DY0GKAMjM_JzISmLY8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11569a18b.mp4?token=T7LQ_mm0WoDpflhRogHK2QW7fSVe9bRbOaeuvFWP7KKR_bBECr7Ts_rMaiDx0qnZD4UMaKWMCLRWcUeqMrt9XxMTiGzZ4XLyjReIbiwVblnBhnoM5MLjQYFyorCA8mkDOg82Dx8vPFqo6Dqv6MXmhP1QJGX5wfNRgLolRyb5PWO3Z7BnpJwO3fGg-tPwDYmX-Bste8vinvOldBEdG1I8t0oCTLWBCl4qb68gac4d07iOpQWygDDc393wpwXnQ-8p9xcaRNf79fLhzpXBdB3AdiDlA1EvhlOAb7X_Z5FtAGdzkuMlMLxX2ZHVU57WZjMlO0DY0GKAMjM_JzISmLY8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ثبت احوال: نسل جدید کارت ملی با قابلیت احراز هویت برخط بهار ۱۴۰۶ رونمایی می‌شود
🔹
کارت ملی بیش‌از ۴۰ میلیون نفر منقضی شده اما نیاز به تعویض ندارند و معتبر هستند. برای این افراد کارت ملی نسل جدید صادر می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/466771" target="_blank">📅 09:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466770">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd10a25b4.mp4?token=Y7lg4hEBVVoUn14A6WTjJ5S5YEn4Nu3yaRidghjZpnaMQFXTrtqJjUrUB4IPhnIRLENyR631UHszdC6_F7OW4iHm5jyWiyS_TgSTF4nAdaibYtlm-vyiG3N_p2hHdeXaceY0Fbb5I5Se-J-D5NaQwJJANeEajDwAjQFNeVGPrGFsFMCVKjHKANf-zLlN3Ab4DggmP9CFbzlxdGDpVnqUKyYgsfff_rOjtRKCtcPzfwCKu6DJe44IvFxLfrwkn2qKQVuOz0z3VvsiG62Mo8J5SIdsGwk8-htCwFiH8Bs-U-FJvEbuu1v-86VgjHojjLUm34HDbtc9InpJ-4KcCLUyhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd10a25b4.mp4?token=Y7lg4hEBVVoUn14A6WTjJ5S5YEn4Nu3yaRidghjZpnaMQFXTrtqJjUrUB4IPhnIRLENyR631UHszdC6_F7OW4iHm5jyWiyS_TgSTF4nAdaibYtlm-vyiG3N_p2hHdeXaceY0Fbb5I5Se-J-D5NaQwJJANeEajDwAjQFNeVGPrGFsFMCVKjHKANf-zLlN3Ab4DggmP9CFbzlxdGDpVnqUKyYgsfff_rOjtRKCtcPzfwCKu6DJe44IvFxLfrwkn2qKQVuOz0z3VvsiG62Mo8J5SIdsGwk8-htCwFiH8Bs-U-FJvEbuu1v-86VgjHojjLUm34HDbtc9InpJ-4KcCLUyhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ثبت احوال: نسل جدید کارت ملی با قابلیت احراز هویت برخط بهار ۱۴۰۶ رونمایی می‌شود
🔹
کارت ملی بیش‌از ۴۰ میلیون نفر منقضی شده اما نیاز به تعویض ندارند و معتبر هستند. برای این افراد کارت ملی نسل جدید صادر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466770" target="_blank">📅 09:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466769">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc2m4H7DFVCUR03KwSW2IGg_yPxfTvcw2VKNnWBiAIuCuBJWVdl-EFzogYh_NvaFu_HUq7xXlJrvt77sRPkLOh738cfSq3Atg0DJK_wu7I6Q6cU6bBdZYJz8oBVD7CTYpFrwtYtjJmeymeYuf6lwZYePJmGmWhCkXdF_g9znHCSBFVVV-yEA6i2pABxnbaB5mUdQ7qpORjY5J1RRnIJI7LTmJ8lRFUsPenOuEjovvoe8xI-zir-eHCmn1-ZDwvmmk48X1Wuj3Hz5sM4HMsaysbmIhrQCG6MT7YlEhXqYQf0gJW1gURmlpZ3MDi_qZ3ZA82q5C8fhwQstHsJ4w1QXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سدهای تهران ۱۵۵ میلیون مترمکعب پُرآب‌تر از پارسال
🔹
مدیرعامل آبفای تهران: ذخایر سدهای تهران نسبت به سال گذشته ۱۵۵ میلیون مترمکعب افزایش داشته است.
🔹
این افزایش درحالی رقم خورده که برای عبور از یک سال آبی نرمال، ذخیره ۸۰۰ تا ۸۵۰ میلیون مترمکعبی در ۵ سد تأمین‌کنندهٔ آب تهران مورد نیاز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466769" target="_blank">📅 09:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466768">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4096a7c0d.mp4?token=jtWM22kOMSS2xkOQ4jKkaZY9o7cPYcPc2XpTpDxEapT8MOzOUmDLfxH0AhqZ5iU4FAyXEr-rWvC5C4KZ40Gt-LVDj7EB59NNCi1Uamo_4zf7rFwromW--uptzO7NYjDb5kIDFTtmXsN2ni3cLrXTy0Yk3ItKWeThCvUOO7jC_rul433hSRfYawqHUzhIYFzV-qu5WJ9CP-xttMn0mhwW33iStTyJc3k4HmBB42dTxX0aKWVSQc0Z4BPpAH6NbzigeDgte2Rb2qw_AlIeC0gT9_FvoFFQybaTu0KyQckHVCBTfL0IevSdm4zM02cpxEjaf3GC0V2uPypwUU_oBDMyLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4096a7c0d.mp4?token=jtWM22kOMSS2xkOQ4jKkaZY9o7cPYcPc2XpTpDxEapT8MOzOUmDLfxH0AhqZ5iU4FAyXEr-rWvC5C4KZ40Gt-LVDj7EB59NNCi1Uamo_4zf7rFwromW--uptzO7NYjDb5kIDFTtmXsN2ni3cLrXTy0Yk3ItKWeThCvUOO7jC_rul433hSRfYawqHUzhIYFzV-qu5WJ9CP-xttMn0mhwW33iStTyJc3k4HmBB42dTxX0aKWVSQc0Z4BPpAH6NbzigeDgte2Rb2qw_AlIeC0gT9_FvoFFQybaTu0KyQckHVCBTfL0IevSdm4zM02cpxEjaf3GC0V2uPypwUU_oBDMyLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌ها به‌صورت پراکنده در بخش‌هایی از کشور طی ساعت‌های آینده اتفاق می‌افتد
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466768" target="_blank">📅 08:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466767">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ7SYK8S8lYjH2yVRywInIgmXiImyl7vzxgu42aTmyVhAzP_gtZrgZY8ODCuwkjUtz7z8cs78FrmgfKnHDkvgEJvLnAsjfhlNC7WU8J9edpVS8wduEQ6z69FqJsAG1JWShgGbDLl4Jhl3pxHjTjGe0tcBLlfPcvJuExDW99KqZfm84nq2T-CZ3ej8ilgNVUHCcAimQAnKWAXHdrGq7-kOiDzVF83FlLxY6AldiblwoODBrwwpj3IMbsAnM3sr1Z_BdAmYoJhAMQdN42-lYCFeqNxcnZX8fABzT2Bzr-Ugmx1820j8TXraWb9CECe9rd9LF5b-zz_Z4ZolqybN_MZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ ۳ گروه شارژ شد
🔸
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔸
خانوارهای تحت پوشش نهادهای حمایتی
🔸
خانواده‌های نیروهای مسلح
🔹
طبق اظهارات وزیر رفاه و رئیس سازمان برنامه‌وبودجه، قرار بوده اعتبار برخی دهک‌های درآمدی از این ماه بین ۳۰۰ تا ۵۰۰ هزار تومان افزایش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466767" target="_blank">📅 08:01 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
