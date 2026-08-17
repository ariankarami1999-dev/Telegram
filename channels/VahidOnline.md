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
<img src="https://cdn1.telesco.pe/file/p6_yKBn-t_q5uqppamtugV66bM7AjB-9pgdif_mYpP_Qp82XCC7-Es5lRRcvJrQw0KJ7q0gZQMnNtKFakXSZarCV5uznGeRViG3SnZ2lqawwu1yegTKuFTVEPG9HFqilOvA3Se49PxIZWJUfv9V13ZWWrRWcC3x7juC74Hd8dAqg1ydcfoIu1HOCwJBQzNb9-BnW5wKOfNA3ahLIx9-Eh28-t8kJQ5mPnRbE7sZEqFtfEN7skqXL6EPa6c5NkbVidU4gztRWhNUWEWVqviu21O-uPQ3gpK2SKbUgHKdlE9m9XLND5UIAOj4mlb23Q_pHwxzER1Muk6mNzxYiDDtGvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 05:44:11</div>
<hr>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=GnIiJzkDQTy_4ltSIIsDCllWfXqa21vaIEkGijk6m8UZsvz7801ztrTS2DTEXq8ZHduKXfS4ztPfOKNmCHpgX3bcz8EY_-C9y9KRhF0HB8OxYackJWBRIcYFgA3vl_qMkhz8R-vrQKvwoTLpCUHPBl1G-J2lIGuaFtqMZmhIQusCsheqgDHVwkuh26HCr3pFqV4t4LoNRqaBKLkYq_IIn_Ij0u0_qkTwO708nrLQYttCpARoql0eMKFyfX6WuJpBGC6_aDDfNyJ9luPqjkTnPDoKTDw0jTgR4LXbaUfTwxeZ9UpR9qSEF606165coZm1Y4U6l5fuSvpjYE4AviUKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=GnIiJzkDQTy_4ltSIIsDCllWfXqa21vaIEkGijk6m8UZsvz7801ztrTS2DTEXq8ZHduKXfS4ztPfOKNmCHpgX3bcz8EY_-C9y9KRhF0HB8OxYackJWBRIcYFgA3vl_qMkhz8R-vrQKvwoTLpCUHPBl1G-J2lIGuaFtqMZmhIQusCsheqgDHVwkuh26HCr3pFqV4t4LoNRqaBKLkYq_IIn_Ij0u0_qkTwO708nrLQYttCpARoql0eMKFyfX6WuJpBGC6_aDDfNyJ9luPqjkTnPDoKTDw0jTgR4LXbaUfTwxeZ9UpR9qSEF606165coZm1Y4U6l5fuSvpjYE4AviUKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n6uCtTjX_LvyzhSvGgt3ZV2TRzOj3YIVmFwI92H1ONbA4oL7rFDXyE_ZdFoN1lWhuJ0rlnSLVhVBCKarUhp9GOi4X40L9F-K10VhPhqviGbtJDkjbbGX1VPvzVzwBL7YbwwLRLxQJblrUohU5M9SUtWfOyGIPdUqJKgiHkDNZ-DUuouRiM7mPf8QGtgs_1sqqEYoxzPIA7Mqyv-5ZLY3QQKMDwopBRcY69Zm8H0kWCOKNdu8OMCKkyQeRhLOWeT-wgFaCQQtAyLCEW_m8cEnb0OautfShILalnjo60WvU3_xfoq2mM-UtkWJEQnRSG-BJSikML5bA6Z43gzJPdjpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kBKjISbMLF0BJPE4R3UsK52b8PTFnGL7-JrWdguj_rWC46S20hNM9BWda_CBzKxwQ5-FQlTknxUh9bd3wUsrLHeZyy5qxPOyiQiN_h6CWjnW03lCu6ipHjWQlaXnnlIf2D_Zx3XGSS3s4tP9Obi89R8xNeHvv-L7ktmjHcDItD8ZJ4JeIS-XONoX_0RKc1ASRozv92S3Uo31oumIWg8bG8ieyARDlzk54RXjKmzhmKH1PW6TXkUZEZq6yqCEvSnwMeLeS9cIctEb-9HMLhrTSu2odOJPKiZapyqhlAdPJiadE5ml6XeevVq8x0sIsRasqUOYzSGHFOqvOO1DygQntw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WqyQtIfGmNDGTe75Nbyc2Us35xn5MkGu-Xpianh5bgK1gW8QHNJPZa-rukDVIN6DabfykitLXyHBiuboRLr_fIyHHlngfGHShTDz4Wh2P4JMvquE50oqpIeQdP2oiV--AITMfkzrOruvPjAgsOntoL9C4W3GkmnPrDlTFyJirlFHyeHMSpu3o1RvD3TqhibymdUOPdcd_aikBRm3hVzcHyBr3glIxSludUINmThEWQ-AEeDDxl8CGuZJvpZh1zqnrjiNdOmEGeV8_O4o_mmxFY3KDH7dDJIVtWxj8_EL7L0htPCnw9y8YnfX6I088ndHm5Hwj30caR75Abav_Md9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TZ9PvDtA2gaxKGUFPljUZhF4pHtl9JBFke9Ik4swmGvqQ-pTFs5H5zGB6aywkmG_mrI7neJSVs5qX43xZTKkGKwRUcIdvCCqsTsZWgRBvZBkQwQQQzN2GPZlpxHxXgfVG3TrFMfPaiRWfQnZ7uSZrgXz_He-RNc16C8NwbK4DQ-RAYbVPzrNOKBcwYIJAzaKQTpdfgqCZNDX_xqm1J6Goijxxr97SURZS-VwDnlYPDDd_yGzS5uhznrha1TjQ34kArVLLImQJGPP_SZHXb-SieL64ie__86nxz7ln0jPkBmQRREbC4RMUAkM13NvWX_k6rglm-w2huL5H8Rnx3Bq6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=S_ZTNh36lXbql68Ays7ZXchF0ZFAk4jdx7_jIVv0xxr0m6SNx2bD7-skkCSFVm0lPvPgOeSYNBe4JJO2C_Vh8eaa5xGgdcTWeH56QK8P-8PaI1xM8R3cfcohtV3BOHdq7C6nN4fvsPTW7loQAK2z14JokfE2KFnYk00pLdHXBcVEH0mc-pdDqKEALSfMhEJSN_g6NB0HmW0-Q_KB1EqQKe5zfxPM1NpfhJEBlmWyMUDHgkgWdD_Fd-lQ6Rvaq_sBJVHt0J-3PGjezmeaUUFRdc0ZIFphzoF4BDT-WGrK_Ee-PpTqv3hzg9xdNTFOQRdt65tuKwKl2oAtofLEvz0lUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=S_ZTNh36lXbql68Ays7ZXchF0ZFAk4jdx7_jIVv0xxr0m6SNx2bD7-skkCSFVm0lPvPgOeSYNBe4JJO2C_Vh8eaa5xGgdcTWeH56QK8P-8PaI1xM8R3cfcohtV3BOHdq7C6nN4fvsPTW7loQAK2z14JokfE2KFnYk00pLdHXBcVEH0mc-pdDqKEALSfMhEJSN_g6NB0HmW0-Q_KB1EqQKe5zfxPM1NpfhJEBlmWyMUDHgkgWdD_Fd-lQ6Rvaq_sBJVHt0J-3PGjezmeaUUFRdc0ZIFphzoF4BDT-WGrK_Ee-PpTqv3hzg9xdNTFOQRdt65tuKwKl2oAtofLEvz0lUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XsD0wXUHHnmUjbTcJM0NWPi_p3h-DcXsq1XgkQ2gTIKMHyOtfJMnf4-SKh4HU8l1ivd0Z1msvkQPZYseagJ9fgojCgWaVuYULVqABo1eu-NCCG_3mnZel9T4asjrtiTym49oiEn6Iw3ePgls9Ay_IYTEaSMIpkagBj03rajJdtFd2VWhELy-jZM65-pwDI6UK-n-taG-FVmmZ4BQbnVFoQ1troJcxbkWzgaG_-VLdlZ9mWkQ6iq3wcwzlqNJBy7D-utu9-s4d35ILk_lzkynbbsqgmKDQ01WXGKMRMGlo8BtrkjR6axaZkoTaodF2bmUE0GvAfK4dtKWuBu2TJxMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z8kbbJdhJuZrXRcz3Utx12CNkm4X9U5jfTLLb990fZbWsf7M6hy8aRejFxCaI_8DeUIEsbW0MitUgVzja3McLOlkso2i6aW_ieFgeJ3pi_IN3da3YsLf71D0ZQZzR628mYaIg1qzanuxhK_16aG438fmNrAqEcdXhgArHuVtasue0iQySzi1UoNnb5GDHU8gIkUd1OMIpVg9XG7Fswk37sw97tCMpQAJwgY7y4fsHopTRp5IwNBq-BooB31bD1nHFR_mU-g3pVOfyVlxY76VR8JXDsTGcnZ44-om7aCdhiTsf2G7GohoOXXAxPapLP3P79XL2-Oim044af-CJ2ETYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Eof78lrRBed3rgAKn00cdTAWou7gQG68CZqy9fUqZ0yTLYgRTU_tInBjKi7KHlgRxmIX9l-SoS53Ir65zJU5BNwHBWzRf_UCmKOPCfVCKDuvBctfWmAkW-GLAbyv-yfV6aC_S89l0JBKg58F6QakFKHhtlzSnwOIVGSOXXKCQ32GpksaCa8IzpsL0W-mDCXKVpIBuKzg-48EgaJFMD_il89itQWRwyn-iHMvEPwzQMSKSTQtTUwyYYzdIYxvR4WemQnEGVkUqBvMXyQsrxqTKpb-XE7L7vwehcGOBuKi0JFvQgR0uUWxhcbx6qqLhMIDTzziqoFsnpXuPOkiIlh_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pBsmkNAD308Bd39Z9zzr5N6tfoy8G2F2t3qVAOzud3WX6qctFyzcOaWS-s4tV7JTLHbtbrwjFzOKWQ2YN9FfgZOd3q1q8_MnbW6h8dehXxojEZrmFSEyhFE7XJ-t5vHT6dy1i02pUZfJUlE2MDQz5S7TcXpqS4WMv1q9mEndzl1Q7Akcawi0sTHdHIXzAKxA2yQjIQMwrrY1qG_LIrdO6lRnQbaVj17r2IJzQHsXMbGx8vCvi1M6OQLdMrxv0PVUSaBhlD1r_-kK1Yy6xZQwwU-y4W-c0NKA9GC88u3pZ5N8MkSB8T_POwG0bL9_1O2pzDpXcv5EqXWj4sdlSoGlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbQ3fGNs01BQtduTJcSk-hDP61tkFeekv2lhk4JN4gKCTXJCLefuiZGkXCJmvOkzDMDXClsyGBWjWX7t2ZkAq8eq7KrkOpmuYEFVfd5BRMK0zNszZf9wVUhcQeIQzAEQcJX0WKA2F4jjGgdPlX9LjhNCzRiG5Fw3SDsO4mR2KtPfu-7V8feYcemlUJODpUcCLoPy6Lq3HwJpPID42xmpv9c1EO_RoFcBjiRUzA8kb_CXj20GdZadH1Fq_hr-cxU8Zvmkf7Gk2Z9kMzmqnSIqN8oha9U4uUHEWjsFeh3pGkZ462JUYlly4xVGmD06v2Cd1gPteRu5yb7Tx-byUx4Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/epBVSsOEu1J_TU8K4HvwAF9COKps2Xzdu1fb4CRYo6w84GIHEM4NONCDJfBdelgxEaxwBpp6oaTb5qX57pMkpzivAKg-laT4TSqoc2A9Qo5dBW-ZVqdoxhuPRtnNw68SFtKy5HgC-5C_9mBlSohIDtq38blljjfwqYeeJsYEdUoBqINKO7XUhTB4uW8cxuKn0U0AILXFODiknMx-xoqynot1dvmeqac27Cj6wIHK8YantZoTBtitvdJr9QmC3_GcPR8rrn9YKcLIRH1EV98ycVJSuPdi9zEGkLuwwnGnUgn0K68gkVBfKvWyGah36yCVRU1hLh0jvdz4GIbznEKj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kREVEIKrVLRUYo_3ipDNB9ZVUrwQPylQTTfEb1mT3KdY7PWxqiI_AYJJ_q9kEBYRI74RRBLJnxPJjtDCJ13IHXS3SQFoc4UIOK7CuL1PD8aux_ax4FsWf2KIMvuhTFXHHo7dAZVr03lPm2fcG4nKJ66ZeTThu2tkUMlWLpueTY9MjnZyJ9TZ1fObvT-qAYlJlnMrctT_U2xoPf_U73jo9DIzDPwWH45YzVHB7TV9reaSoInUsfyHpbXT5Q_2GY9b0OVZiW_lR6vQaPdcgSI075p_XkeV3NNw2QyNuBujId6_uz9DH-8I8kp-wgPN1Ivw1e2rFdldGcnXIAh0oHo9oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JUQry_cA4hwwmAN8hxKMDLGX1-YEAiCjRAKr1kK-nLwv0zbpfcDGRirycNl5WkZzlJGcvOLZDsr5IqMKpNomczg1cTJgSx1KLcKkiNhrxvdogeCCRI4wVJIa4O0Aq71Ji8jznVOxbFHH9Im_ewSlJhw2sGniwXBSmzED4oa14fA-6FPoOM6WEUABkR89sCTwY4PFFrxeqk-oxsMf9EvdWeJ6pmWCy9m6IWRRhjEKcw0fbFeM040E3u_eEhTkRKPFMTKNTT1XvMFlOO6vkvGk-Vw5TZ26ZtwP1wqT4zgidpzBGueGXfjcRrSdhIKKe6YSYVXFpl5nHjHqVENfUjasAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X_kqgIUuViyePRPzG80hluYA1k2hzoE_BdlHuTasnkCgdLNGgh8CRfoBQ-KanxBhg9jjLDcOZCgwQ95TsaeISRTW1287k15a-NRM8lprI3cIeIO9JqEXodCHrTtCmNLMi6FFaeDqmlRExi1tjnyzh9nLPXuLkuJrYBfzxsDlkhqWYHeSFy4D-fnpXEgF__Nmm3gBx-JH-34Kxw3VPYyXWElEU5IEeCp_mJM4kCiMgwX3xTgjODQsM7reiDOiVzYKoDCaIQQJWF571Gm2RWWjsJhun9Ms3NMgdBdr529LYG-NI4qpY9jEfIONJ1xYdyncxPiBBNE6h4AdCibwTNjkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CCQiPgrVbcpIQcCwWZsiXt0ApA57E9qW32IbhmApb1428zs0vWEtTT9HOrO9Za2bxvtRAcxsetWb2hX7Y7dT0_Cs54riJ_TUvutL6EnrjiBWO_Wacp518jB7Culs5l5I9M7xm_XfCbSvQGdyJicg5pTsciB9gJ0aMo6qwy61r0AFAWkNRnNgmi0Z3HbGLxV6TA7QSsCA98VrkogcBCsNXVcBY02JEoOfoqed0nD1ZL5adxeWQISNyBy_02WWmVTcCBepMKJYptfGSPTHy0huD-Mzh55Di6xiwWkPTYl5yHH4bpSs6WN7zvpSsPzOxW6-KJexgOR9Pqq3x3jcVF7dOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GTHeD2PMqBtwQvwS-yyOFxicg4RYAVcP67bFhjDQ127RGkj-9cy0g_dEKO4zY2uH4CWE5lUdS-TCT6OAHBGe56cxgZwEgkU4CTCZ8K5yHECG0pn_A1CFFqGidqCFCERTb1SJYD55o4w3EcislyAueKrghCMiabk17U4KOCGQSjD9DW3uutrz81_urjHv8y_gaouVVsAohWuMd2GXWFoEJt6Ry5JCHoL6OaFJfNjthV6RfzuXirWTbNwqZUbec1mkI6MwkKCrqNy8Ze_At-PXMMdUUA8MkV32hl4poTKxUK4MSjJEzmVYNhas4RIhrpd2rf6gqscAVHempBVTYGSWAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=OLqti37YmHEZf5WYnG4Y6LaXIEO_hlq4IYuGv2FT7w0k0a_Lib9hqcZcKtwkZDFvPbRMLhrqCmGTIsjEeGCB4cWJ5R1l56KqS3f47Xy0kObwUU8fYFxcFLABxB8WRpEo_H6hBfAs222IWS3OeeTQBac2zjqlnLJ9aJJh8CRMLVs-H_WyVmvoDb018EMe0oFLNx8ffpfx8SI6_6rLh8pT2f596QddZexXc2CFRtPkXjFI34zBs3BEQmwvPvJPaw5W2NZumjX-sJD78ZKIOzoeJQ9Ek58eZW3Xk_wt_RthQiinp4-e77FLDnWQJ7nYW42Apm0JJ7z7heSIgBXH6c5Z_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=OLqti37YmHEZf5WYnG4Y6LaXIEO_hlq4IYuGv2FT7w0k0a_Lib9hqcZcKtwkZDFvPbRMLhrqCmGTIsjEeGCB4cWJ5R1l56KqS3f47Xy0kObwUU8fYFxcFLABxB8WRpEo_H6hBfAs222IWS3OeeTQBac2zjqlnLJ9aJJh8CRMLVs-H_WyVmvoDb018EMe0oFLNx8ffpfx8SI6_6rLh8pT2f596QddZexXc2CFRtPkXjFI34zBs3BEQmwvPvJPaw5W2NZumjX-sJD78ZKIOzoeJQ9Ek58eZW3Xk_wt_RthQiinp4-e77FLDnWQJ7nYW42Apm0JJ7z7heSIgBXH6c5Z_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R13CIuKk5BksXKSX-cnFTl9dnKJGzWx3TRyZsXLmdUpa_Ep-QdF_OSp1lOYMSFiA7iVAQZOdVxPncdldTScKiurU52DG1xi4avpxPMrWG__kJPEPLF6dNEow_JThfXUWBs4DK7VtZVJ8wnSPeId4xwxm0rCq717z8OaZoCVSCTww8Z_pLCyBfSWOqxSNwzglvKfhjg27SJden62OocfDMR2Xxoai4vFdq8FMAhe5qUxK8G5PuMl_bQbhwtX6vNeG6y-is2So_ugMTKZbzWFLpqfmH2OKYyLmqtvKvkJ6D0Pq2nOTCShJ_t3N1ZAkwo9fWQO3SXSdcZj9r2erW83fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgqW3k4pAiAj_FAbsWjgRP0zEMj_530AbmKmYIzO-iuAqCw-PWsAkez-tFs98vkQ6RqIbnhFiLAWC9fr4lhue2FxCUILeCi4XDbyzwdasnMnAIofmWst18aYi7T2nuNvVKv8V0u_bx86AcC5y-bA09bGZK0ekYq_H2o4atsMGRTmpd6XHGrOyFOtSZt0ZgG0m2zF-ujJ60clIcgbIa5n7T2AGmR1qdkZ7QpGKSJqIUfaP8qH4ToORJ6HTqQHaaedwlEXwdDPdHjx8DbWbVL_gUtJ5-8GiaSD_ITz1JiIs8REvbNjmIHXJToGXWhqarKrqReJOGyofPoKbFK9gBvZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWeukwtV2THckZC4kLgQ1UAWCSP1d9Mm69eIO6TC18eRTimgY95n4fkP3_paXNKZ6ealCYnCqRnR-jESer8SXfxy0Pl5hJsXOAI3-qIhRGaXcPiZ4eUdAGZmBxkCH_dfTfLfrB8QyvknhEUC7dYQJ3SA0C8gJWx7GKv3tIQXsktT5NTzYnbTPKPD1SL91j_SykVaupBdG-gIFLQ_D3CYFRxh4DmtJEsaJDKAo0cVRwFfmNn7e2YlkOwF2HQfxDRiTnh9qka_Hd8upf85l-uIDXTbR2_YIevJspqZBK4bKGvMMNKSKJ4Mr-P08fOojlzQJq7squN2gG32X8wG76Ym7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=AzchETnuOtCdRxtovB5-_ctf2aZ4MoYQ2OIccou0uE5PwdMDbmsZy6QsTNfYvTEO6WfHfHwhuF1mDg6_Bj-8GcRj9B5KgLyUpsWoduymNSrlx0aW6YgIPpKvnDgAq7K-aFUHrfjUsRhUlbCXOIjHGANLrCSlSjtNxv3_Wl7wlTEX1ACW1ywRkKtzHwxDkqrfgXEZaYpQPX5CzPoKt7qj-wxSPyn0-EzLqhF6M-R7unPKslXlt1473Dacjv3-qiaUg7WGrDmbkS7F_9vkqz3H2vmnFshvZJ7UOpiAbXLzVr4zHnbL995rM8XW0cdgwwIQgWg4PWSsFyMIu3B5uTpSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=AzchETnuOtCdRxtovB5-_ctf2aZ4MoYQ2OIccou0uE5PwdMDbmsZy6QsTNfYvTEO6WfHfHwhuF1mDg6_Bj-8GcRj9B5KgLyUpsWoduymNSrlx0aW6YgIPpKvnDgAq7K-aFUHrfjUsRhUlbCXOIjHGANLrCSlSjtNxv3_Wl7wlTEX1ACW1ywRkKtzHwxDkqrfgXEZaYpQPX5CzPoKt7qj-wxSPyn0-EzLqhF6M-R7unPKslXlt1473Dacjv3-qiaUg7WGrDmbkS7F_9vkqz3H2vmnFshvZJ7UOpiAbXLzVr4zHnbL995rM8XW0cdgwwIQgWg4PWSsFyMIu3B5uTpSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=cSF8k-sZbfGu2yKARA0T6hR6vKYB3GrvcLzdUgrQJJdRwbsDmkrrP7OC1exSYOUnfqvFm5zKHm3GljrsNZm91HfB84RJN9XZC_Zml81ATVE64i2GDM1dTwiwdnDZPatfEhuqt6VK7cCi7kBZVJwLfj9HvZtsRYV1laNbTB1gCOfWnJ8zpGMBiigBHPRrE9j8l0lovWJ8QVQKrKnKRjxwG5q87jC9DwVlkR4vrlEq-XKQUg9ta-inel0yBPOg_VLwtRtQE9DL_1ScwjJsoeCzjK3NB4_SwFS7EfcYBrbjAI2-030QTqpj-gpOhUzWT0ec5d52ik3-eBi9f2RckIZWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=cSF8k-sZbfGu2yKARA0T6hR6vKYB3GrvcLzdUgrQJJdRwbsDmkrrP7OC1exSYOUnfqvFm5zKHm3GljrsNZm91HfB84RJN9XZC_Zml81ATVE64i2GDM1dTwiwdnDZPatfEhuqt6VK7cCi7kBZVJwLfj9HvZtsRYV1laNbTB1gCOfWnJ8zpGMBiigBHPRrE9j8l0lovWJ8QVQKrKnKRjxwG5q87jC9DwVlkR4vrlEq-XKQUg9ta-inel0yBPOg_VLwtRtQE9DL_1ScwjJsoeCzjK3NB4_SwFS7EfcYBrbjAI2-030QTqpj-gpOhUzWT0ec5d52ik3-eBi9f2RckIZWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwOzLbgl9sgnUAQ40sPL_YTYsodp7EryHqjc_99xQZx46QwiL-0-4nrEeeDa_qi9rs_1LGPFNkvzZXsJQpKn_th9BB81yQWyVO-DYbxr3q2Go_op2H9SUQ-twCmo9reGqt3Gj42fcPi2anF3fdsEpiOZawNlYpz-J1Cf8Wb66E18XTHBI-ZSrgQuDzeVNv4oqpl8q5XGtyLwKinpzvNrs7hd6Yiettj3mtSM47zM5EAZrw98w_BRNZnRoQtBQZkitMme9h0j-7jeILm82KII3pTaQErtgKP7-7Sxwhkh1vbm1YEiSnRg4ZOJriFJMbLsoqOgFunEbjIsFaoo6vquyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ryx8H-h4pigP5KjVSH5-w2rBtukg33FRnTJhZ2H_j3jjvIfK7rVLDhw7rzY-HN3w0GnR0sRzUbaa_KNWjUmIbfhVQObO0No3tV9LgVyVVAYtuLa7zltVfArHnHmmZffiAXUo5fzx1MDLjqPCkKElsaXOl7Dvfpyfvgo7LTX3O61NrBQ0lZ4c6G0lzHgHoe3i1EQK43ARI5WABWTou6CCzZ-O0TbQSW8p_SH4CZzHq7ZybFsyf894Ndzcj167zY3Do_V0iF_ptzleDUwrGmydqiL6jVDFvqA74wiy2zAnlRITv9wmBbbOK_sQdOkvYJ1nh66aj22zhWtyU6vmvLIr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ روز جمعه در نیویورک با اشاره به حملات آمریکا و اسرائیل به ایران گفت: «آن‌ها دیگر رهبری ندارند. رده اول آن‌ها از بین رفته، رده دوم از بین رفته و نیمی از رده سوم هم از بین رفته است.»
او افزود که این وضعیت، مذاکره با جمهوری اسلامی را نیز دشوار کرده است: «یکی از مشکلات من این است که کسی برای مذاکره وجود ندارد.»
ترامپ سپس با لحنی تمسخرآمیز گفت ایران «تنها کشور جهان است که هیچ‌کس نمی‌خواهد رییس‌جمهوری آن باشد.»
رییس‌جمهوری آمریکا همچنین مدعی شد سامانه‌های راداری و تجهیزات پیشرفته اطلاعاتی جمهوری اسلامی از بین رفته و توان تولید موشک ایران ۸۲ درصد کاهش یافته است.
به گفته او، جمهوری اسلامی همچنان تعدادی موشک و پهپاد در اختیار دارد، اما این تجهیزات تنها بخش کوچکی از توان پیشین ایران را تشکیل می‌دهند و ظرفیت تولید آن‌ها نیز به‌شدت آسیب دیده است.
ترامپ در بخش دیگری از سخنانش، گزارش‌های رسانه‌ای درباره وضعیت ایران را هدف حمله قرار داد و با اشاره به تورم و کاهش ارزش ریال گفت ادعای عملکرد موفق جمهوری اسلامی در جنگ با واقعیت‌های اقتصادی این کشور هم‌خوانی ندارد.
وزیر خارجه جمهوری اسلامی روز شنبه ۲۴ مرداد در گفت‌وگو با «شهرآرانیوز» گفت هیچ مذاکره‌ای میان ایران و آمریکا در جریان نیست و تهران هنوز درباره از سرگیری مذاکرات تصمیم نگرفته است.
عباس عراقچی گفت قطر و پاکستان با تهران و واشنگتن در تماس‌اند و میان دو طرف پیام‌هایی ردوبدل می‌کنند، اما این ارتباطات به معنای آغاز مذاکره نیست.
وزیر خارجه جمهوری اسلامی همچنین گزارش‌ها درباره وجود یک «آتش‌بس ۶۰ روزه» را رد کرد.
به گفته او، در تفاهم‌نامه اسلام‌آباد از «پایان جنگ» و تعیین یک مهلت ۶۰ روزه برای گفت‌وگو درباره توافق نهایی سخن گفته شده بود، نه آتش‌بسی که اکنون نیازمند تمدید باشد.
عراقچی مذاکرات تهران و مسقط را نیز «فنی و تخصصی» خواند و گفت ایران و عمان در حال تعیین مسیرهای دریایی تازه‌ای برای عبور کشتی‌ها از تنگه هرمز هستند.
نیروهای مسلح دو کشور نیز در این گفت‌وگوها مشارکت دارند.
به گفته او، ابتدا یک مسیر موقت برای رفت‌وآمد کشتی‌ها تعیین خواهد شد که ممکن است مبنای مسیر نهایی قرار گیرد.
عراقچی در عین حال تأکید کرد تعیین مسیر کشتیرانی و بازگشایی تنگه هرمز دو موضوع جداگانه‌اند.
او بازگشایی این آبراه را به تحقق شروط جمهوری اسلامی از سوی آمریکا مشروط کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=kC-vOOcAtsYnx_wpOmUf4-3vsj0uB-Moq9A7LjJwL_3gwouuAlX2siyQ5QTDATrUPHv31VmOOwbUVP4cIPkdVaZ5qejP9O56RtIUawQtJxG8yVUJBnUDfuSMXIFz_AbUx6YuJA1JxvzVkd8yuWf5EbO8QZH3G2NYGzZMBnbF9MfpxDsPG9Lids_RkG4VNwM8iJHD6u4KyipNPMQ5Q3klTXbozGE3TX-r8dr-08hHUPQegxZFy5PIFRDV6_2YaxuiskQjWLYmVc4Ww_UJl7JIZLLaDNN_3WibDzKwQqTJYr0qbjjcxlawnAGp-B0aSqT-35ZoQydZE0b-kNhzQbHgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=kC-vOOcAtsYnx_wpOmUf4-3vsj0uB-Moq9A7LjJwL_3gwouuAlX2siyQ5QTDATrUPHv31VmOOwbUVP4cIPkdVaZ5qejP9O56RtIUawQtJxG8yVUJBnUDfuSMXIFz_AbUx6YuJA1JxvzVkd8yuWf5EbO8QZH3G2NYGzZMBnbF9MfpxDsPG9Lids_RkG4VNwM8iJHD6u4KyipNPMQ5Q3klTXbozGE3TX-r8dr-08hHUPQegxZFy5PIFRDV6_2YaxuiskQjWLYmVc4Ww_UJl7JIZLLaDNN_3WibDzKwQqTJYr0qbjjcxlawnAGp-B0aSqT-35ZoQydZE0b-kNhzQbHgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=qCgPJIF1rzObIi6gpmmswUR3RX_oFPLSCYlxN4NojvBQUKDUfmgFrxBVDdMfTGsKR-KfIihNdwlzAsDOXC9xWn6x79aVjjN-lRSjKXuPa9v8dGgHL5FiAps8UN27Yh1yvCgfP7tsu31izOh3CS-m0V4o0hQap7tqWxW7in7YfNBtNiM0hrhMwbV7mY-q6HPQ1WBz7by6fKx0tlKRka2qn-r0Ic9wbcPaKlpw6vWCAvDbnMRg8FU0qVSf0i9CDd5oZ488JhkTypJT2KWlcFIzuXns77XgLKe61wGxlFonW1goS4upfv7C2qGxfIa2sPfYx-g1zBVoevWvjRq2XnOk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=qCgPJIF1rzObIi6gpmmswUR3RX_oFPLSCYlxN4NojvBQUKDUfmgFrxBVDdMfTGsKR-KfIihNdwlzAsDOXC9xWn6x79aVjjN-lRSjKXuPa9v8dGgHL5FiAps8UN27Yh1yvCgfP7tsu31izOh3CS-m0V4o0hQap7tqWxW7in7YfNBtNiM0hrhMwbV7mY-q6HPQ1WBz7by6fKx0tlKRka2qn-r0Ic9wbcPaKlpw6vWCAvDbnMRg8FU0qVSf0i9CDd5oZ488JhkTypJT2KWlcFIzuXns77XgLKe61wGxlFonW1goS4upfv7C2qGxfIa2sPfYx-g1zBVoevWvjRq2XnOk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=u1VaexkOozWgDRRSwpOTYUd9q5a1bBWlAWjNhjuPR0EJ8a3slRDdmxNgzK5RTNDiHtC9sVflNLj18eqbbTn_L9MBBMHSUKsHzXvz2SZN1ICJOvBIrTehmodqvA9APT_1V_fgGeUZcmS-lLF4wrc29J5cxvwsa-jVclb7aF0hiOph4PsoAsUNEMcqvxoeo1ovKU3CuuwxsUj4NwRsZM6qz45Mk2D-8YctIAWSXOfxwZjrTpJFTnDRL7KtfRa1DsvD6KfU0qc4dPgEn8Ywv8qJ8_WhGDEFwg0tzHqhI1hj2pGrCo_EitCYUgt0gv9JPhktdvTVDc-R8Ytx_fu_Q6d1bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=u1VaexkOozWgDRRSwpOTYUd9q5a1bBWlAWjNhjuPR0EJ8a3slRDdmxNgzK5RTNDiHtC9sVflNLj18eqbbTn_L9MBBMHSUKsHzXvz2SZN1ICJOvBIrTehmodqvA9APT_1V_fgGeUZcmS-lLF4wrc29J5cxvwsa-jVclb7aF0hiOph4PsoAsUNEMcqvxoeo1ovKU3CuuwxsUj4NwRsZM6qz45Mk2D-8YctIAWSXOfxwZjrTpJFTnDRL7KtfRa1DsvD6KfU0qc4dPgEn8Ywv8qJ8_WhGDEFwg0tzHqhI1hj2pGrCo_EitCYUgt0gv9JPhktdvTVDc-R8Ytx_fu_Q6d1bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ao0DwutWdaD6MRhSnp6qKa8lGo9BcwzLONBVjcVpd1LnHzPGuYH-_PydpvCtkl8d-kbNmV5gEb8m6hykAo35YrGS9k2gW9aVmt5ZdI3Xf9Bh7L-aWSdYiOWtIYlNyuBk9Z44x4SUYVM-DMPV08bxgp6aam7NYYrOznq4r1i5Q3iDVmSPSjh5w11-PeZ2j1FKiv_ZoJIVS62HaJ8GKBP3EBsM5BtD83ILP2uOLVMiZa7yXWmU7ZcIFSTSb_ESzQf6z3qO5QWvRq-yj_icXj2OwUUFHU5l9GojEYfJIk0iuUH45OYm2g1YkN0A4VNlphcSttyZoV4qJsShBW22n5lkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVpNasuOR8D_tENE6fIavLthDeYna_H76wltRmmfKGv_HvA-aAHOnbbNyc4KwDtMrjlLodRtNXGi7CMBW63CrbtLQvyWIRbBeBeKqV42aBC8F2cXh2kS5w0wOHPkHqVWwQYSOvHm9_agPTLyoMnNaig_uf--p9IaTXoNovcFqmaGkwOMkWttC6amNq0aiSzJZnD8WoEbdkX_R3iGD-UsJtmNg8F6gnd1Rql9X604elQ7VIOxp5ILk1oru7hjburJLQ2td2EfHfG4NV43V80osbkEAzRgHawgo3J9ZOYans2T4BTnhFiPPIeifKLqFEnHdVMeNSzxj_1JzT3m3wwAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=JkdesHolKTql8XlB5by0bbwaXcdwwIw2UXIvREzlukuivr1KwvJdvR3Ki_sLqDSHBXGeS-S-wscF8bXwfIo67UdFILXtU3n0P1IRp0fhGoyWzwKgcUYDuX_KCOEKbzmAXFfYwUfUB-vWnNZezhpAG-kzhZrWDPUUQg3SuLL75gXPTNItP5Uc26BV7aViqg3D8gNUpQ1UkDdw0aGs5F01F9Av1oYBVkNMc51l1ewiQhpukbphXpWDsw0dk7H42fDG4LLawVScC3JBdGhJIGDWGQJwI7jcOvcWSJdSQTWlUYlv2foeigSVo36al-odyzmdOAw6sEprDc-3Lvwh98wqYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=JkdesHolKTql8XlB5by0bbwaXcdwwIw2UXIvREzlukuivr1KwvJdvR3Ki_sLqDSHBXGeS-S-wscF8bXwfIo67UdFILXtU3n0P1IRp0fhGoyWzwKgcUYDuX_KCOEKbzmAXFfYwUfUB-vWnNZezhpAG-kzhZrWDPUUQg3SuLL75gXPTNItP5Uc26BV7aViqg3D8gNUpQ1UkDdw0aGs5F01F9Av1oYBVkNMc51l1ewiQhpukbphXpWDsw0dk7H42fDG4LLawVScC3JBdGhJIGDWGQJwI7jcOvcWSJdSQTWlUYlv2foeigSVo36al-odyzmdOAw6sEprDc-3Lvwh98wqYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UNVqAfDKAT8bBaoctwGzX8EaP03xehfDdU_xWb7OFsL6STSOAoc09dkYF_zqWUapjx6hweVgm28wRNVJUe0n07Oorzk6hMV4f1dhlHgJkWQ-yH5ND422vpEiKx5Qxoraqc7i7auAkideBiezoZYq748Dy2BSv4pz3EApzz2M6nunAX-ul0StGDdmlRQELPCM6d78o0QsMQA1IwpBl70hsdKls2vbdl641JEIpsPbeWWGtTZu89hGV8E_JeXMGzKE2rlbiLCN_SsTIbawnPflsVjInYcL2Zemjp7KHvVdBEVIn_wAeC_Gzj5AKT1eUGTffUcAuIb0-Gj4zmeu4G65YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c5qQABGmBQHVA7ef9wUBf3MfZZ8n4UFJcO_CWfx1punrXJRjaBECzUvJD_fdvgDAe8PrfSneZ2QiWBdhfEXB0f85DqF9V21XGNW9yP_MLRnHXKKVnv0MeNjUYuMsSL14yXFdfR3uL45RMjcORdW2oTKiN_fSqvCIDQLKAjSa9mXTrKBH8-EeqL9Xvqfqs2RJbjd6dQ7PAL4992d2hxWvSe1HekIWO1Jp5rfLKtylEoHdoQYIuWaHI79WxhXCoPoYHohiHX9nLvXzzMkoLPLWd-JMXyfRDkXEblksm63dpZA9RxxV8A7D8loTcZg5PLRg7fOu1OkOaTP4DqGtREpBsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sUVuzAStdB6YEQER63YHpZm-P2HG7rDhw0EScwajqb6NHHZqS7nl4S5lzA6LxO3mp3HDB2OE4sbdP9KtpoBkUZCX7Y8ASown_3oz1DiubTpXUaezIdWPmgrEbu4DTgxYR4yIX_rFEE7oG34fi1rpIm5EGH03jVJve_tT1y5aKuy-oP_sXClbcPnFcmGdqE511Y51GlmXe0MEH-UP7j4c1s0asRvxjY3LGCBG3wR-vZEv5JbtSnZBlK24aXQ8lLJQ1J1oKxHZZBu7BmF3po4vgPAM79Owwcmq5wgRIKEuYvhkVdC9XTDz5Cqlubk1wq766p9Nd2qs8TCwwsYthqbEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0L2JpL58_E8C6dHcwsZhTXyBiYrj9CW3lNHHJEoPSaDayBDqrXaMQGts-Jj_PY2svnHu2jagQFRAlEBLOP0XWyE9h_JPg97sGXViVmtixos3sFkrwk2Y0LvwvmKYGh7P0R2ZxbewHD1Y7yw-9Co4KJ0P9VMKhTpOlJygiEsRdYsI7aKtIuyjX7H78NLs3sNFtP1yUZfbn_PayqMhvr71g2jmNRtHE-v0lg0noVKR1z5CPgTAc86E2E07kfPF4eiDdl5rAETXtjdeQe7Cj4yFjLmFsOwvdtwdh_9Qz1YKN1qCM06gst6IEShHdjR1XzeIpbDHyjrjWhKydIRY0J3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KAjm6MUIakzrInL3hN4quG0qpVf1iPczycP1-kV2b_SWshiFKrrN8DN1X_i5yZJK3fpbV2_CdXNG7PM8HI571xgXgDefR_j95VTxKWEd4zgNTpJeogem2BB9VPNgR3xi0bHviNmNdzV3DKG3YJzBWOJPlK3wqilo4L9GgtWiFfsZqRGb2wCKS1n59YLNhZ6tJibERhENPfh5r-42qOjsBffGXeV9QgR0C0Ssujd8Kei-sKx9sZKlaoLfYQyHUKY8WQzLvS3eqYhVA-puH6cEbbmRv4JGckym4yPpYtahpZqWJlWpegfeFuYaiUbSWQvSz8N6XLHIhN38RwuCvBpxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VocjoPiyQy7iNo67ALwSWKm6qdGEJuvv3biIaupDKcNBBY4A83XpjGBa0T4huUYHA2i7WMwsgLyHDjcn9JbFsEI0rhPBI1kTzPuiau1MtL0PgltL6LT4Zg9eZapn68agB9GASpAkmp9pUsmanWMF_6mdk1Cl93uQpF1cF1cEVw5l0OF2fD6sgf_lXfZGZoPSke1ixWEMkjzVW7PX_RoYIC1dE7MpZ-5n9KJYPoEJJ5Ex3Uf4i7OTVKa1ZwHFkhxQt7x_BrXTlFmWfbo1Pfp0DDHMaXDIy_el_BGzXy8AyZRilaCUhfAmQoW-WGlitKkvjHo4R0EomJe0xBCk5gkqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4vGL2ujvwITCiUhfCsdm-CWPYaG7r7yb8rRuS3UStsmcznZJSWE7sWF1BVb4Daf3Gfakg0LIJHQ_bqHfn_PLvyLuNdtfb1L5KQbYG7_SJbyk6qWi7WYfiBmB3FggYcuo2bj2omeVffinKCR7QknjygC6lyDFSzaVhS7szdFjvEo7xbMRC0Ds_1Be1lYNrG5tQtlbWk98kqtYKAxfkp6L8Wj1t1fZ5LN0C8R8BhvYWdRBwocUxAqQ6eeAEURceLqoFqiAFhhPvbFxvpmsKtJ6-lGcBlTV3V0Y7fmp51gOkFMiyv6IX87RO1txZqeAqq1D6QeCKgaLoNVq2fqY_vGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EMwOmz5gBJbwUoCVtnIHMaMHYaEKptfUQg14bSQo-PGlGklO3cCTiXq9We-vNlZcK5q0QCSly8m7s91Gm7p-Yz35-j-4hwHIbdNHiiOtR1_vgVCH4vQTh82JRDvCNhxh-XgLREuSFsihhB5VWFhpxBgaJI_vrInPXhk8icZYKr7padq3Vlwqf0HIsr3u08ug41wtJAYSp-2vYxMwAER1iAAT2uvrmZsR9w91nutEWAu0f0Cq3LqBZmIKgAhmaV7q2x3XTbbDSk-VXA9snIRHV9ht0y-4Q9u_R3YFFyUr62gQSeXyttXW_URepmGYr1AICGI_kdf2QwACvvrs5N0gLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dsRVwcjRYPnJWaGLJZ0NCRj__YVS-tztNrz7Ss7Wxs_HAzUtmrxZFGORtti0KkhsgcACcVr1-gZYM1WnpCG_NPkLSCF4_rn09lHiQmSdPkoAeE9bBR1g6KMIQmQW_ZIU2Ga16rCjS93Q28otuQUE1NZBSrj9PCpaIIDjWOioVnAkqBWVZwOnQ_REIGdKCdjq9cbPh9hoJLg8jJvQiRilL4uBA0_Q-NkLm2knKmHeE44wacZFgIdRj4BNXJDyiFQbsWxPrw0PCMbh3AbhlrtP4CD20X2kotBIAkzfxnAkZtghMMVfHEt8_4QQEkJ9cZglXxTe4l54nhDybIBGk-jknQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7DtxnV8Kw5Pp6JSYFoD23P4aIZZwFgIxo25JRdrLZimqEHXX3diUvgp7_Wx9_H51IU-e4dI_mqhllQStW-nZnJ1uLb_SYRrJMfQ6S4Bxetra3TWMHzRsHfrIlyRuV2DAkCx2sKx0Q7iJbHRUMc6pUBOYf94MdD7nhIU2FGzjDBy2E-zGEne4gkXLcGwybzs12JM5UTkyEQAJ1954D6IWuhC7hp12k1ZWUxkI2xpVTT5pRD-lZ0L6NePRw1eXNmAcrbaGUXNRV7BOVEWlF27-It6tOSn1paEW_uRkbfe93AifxXpPSiRTySI9EYSAdkwR1DD7kw_pTWHvH_6Hc9KfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=anMqseMHjQWFwnzPv3Xr5nW3R_8d8APNdWAExx8gOaO7V13RF-8HOBKZdaOPN0ZpEooz2AgRQJQkvNXgeUqKUju3pMV1jWgqMeyCzee-n2WRnzO6-1lY7PDmS2Zg-L1EzJCEAVFCa9WwSXRpuvXfNmsEPNlyj8GgVakR4l932kR951umpgkLqO-8l9kr_ZGTETDt2Kgof5rlurtdA2x9GXfoT0Svv1ehkzG-4shYUZ8XcNkd6ax44lY_Jr04Iows04HKvErJ9AG4uuoGUoPqPJLhHV-__L2pq7MLlEAJqvpqZvDd2IvYdrdY3Lw99zqdNWSF1NsU8ZJimNGy4b6Xcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=anMqseMHjQWFwnzPv3Xr5nW3R_8d8APNdWAExx8gOaO7V13RF-8HOBKZdaOPN0ZpEooz2AgRQJQkvNXgeUqKUju3pMV1jWgqMeyCzee-n2WRnzO6-1lY7PDmS2Zg-L1EzJCEAVFCa9WwSXRpuvXfNmsEPNlyj8GgVakR4l932kR951umpgkLqO-8l9kr_ZGTETDt2Kgof5rlurtdA2x9GXfoT0Svv1ehkzG-4shYUZ8XcNkd6ax44lY_Jr04Iows04HKvErJ9AG4uuoGUoPqPJLhHV-__L2pq7MLlEAJqvpqZvDd2IvYdrdY3Lw99zqdNWSF1NsU8ZJimNGy4b6Xcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2ecSoNiyetldZJmbLZQs7Rz4IoS37mgw73QLQox3fk_SenndakwC5fRNNjfsKfyF4-gdZGOAfCKro_Fcb4knsz99Hyt-QPPmtXJMl5LoNdn8P_8SvsJOMs68gdvxKEz2IJLaXMAmuFbHzqWEs9jNazpa-DPPyl0Son1e6oFA7HAMQmVq64KgTSiIG2Nrnf_IHAOrg5j1nw4SG5o91aLUwZbAPhbSp_i277q0aOWUcwABiwwCvIJoV_men1mqONzlyvyGCWJWlLRusl8W9cZjqBvaEjfMcUZ0QpATJE_C5zWlRPAE-h6tgzA5sMK_FOrTaqFr3engyvtJQ0VabHfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kLDGC8J6iamnlEJ_fT-yzOEAQ8GEJyBl2EOPdZ-OkWBzAPsNvlf0yEGCvGl0zqvoejf-jDjrWlcycldZQNJ8_0u0ExDjQdem7q1f6dy4ZJpGZ-s0enmwPU2cU39WFXRpQoEDtHgRbkrtIVLcQCiaObVn1BM7uo_HxVy17b7_jEw2Nn3ouKUC4jypy_MdqAh6z6IcsGTAWiz7XjmmtRle_598334NJHxV_go8GbANiKLJtUFC4vnqCNGlWxxvFOtQ1m57g23CZwlB2YHVWthD6nkIprWWOuC9NyCR6MulR_q-5xS8023GX6JY5xsBBc2vdPo_YwSVtCXDrbQ2AHtrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUzkcEai609TzV7SlPam9redWgDbmhaCWgEHHgvVRUvJVSDvXP7Cv1caGjcSIeV_dlqEwlhf8wNymeXyW1Y8eIft_Ad89PFEhkhIz8KXKIJAf_ZXn3PervyZ3aTtV6hzC6xAaV9gPZHC0J6GhIFBDjjTaewBMaFwAVEDf2aYSHOPUV3Iw4qTYH6EZFHnMOIt1P_oiLLbhbVSVPbZlhbYJgZ16ET15qhfUd7tQv9HbqAHfTJUaH0fV2mNGy9sat6OMThescQzNMyMZVnsxJKN08UMzbtuNmC7-Rh_letmij6lb_po3FAb80JTcM5O_T1A8vr2k-1B3cWF9GLrf1jJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tTLzOX0XV-WswLGdEpPLTs2ODPJSNlaLg8tpXFnY92McLTHckmmVfElkuyBrqsHqDa5dm3xe50ES0zgWVgIIzaqUbNRoYG7BAsM3FP_Ue4KdyRiWKzmYKH90YTW2EudO-zZ4TFP7dFoPK1ictmOkTn_47zYOUk9lorSQz5QLy34Aq6VInAm7FwutW41vnYlSCU1nA18I3_FtxsOg6jBcyNZ763hCvd3accQXKe0qziluEFyjg3he5cK4_xSaTc_638YrXS2biB5iXZH5S5xaq3Bii_J5rTHelkvocRXfUzhd-vIH6APgBkLyd6tfo79mfT5RA0h7NUQUqNbGZbqyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h3bQsys01foLKZ8yLq6DcJ__JROEUKCSSppwnyfAnICYTvtNMco4FwQoVXDELum4Z_ra5N6irXE2zVDbYAut5sB-EezcRR6D0CmQ54-t6YCcCTupRYIn_9r8dM_VeiWL1iABU8HUf4q5cYTGSP8FSt4D_6szkVSAnVBFft7JH2U1dWEnEOhBMvZhHsO0Afuz9ky23pXYUVlrExX8S8nvbFczC-KZIIMvWdygr_0MGkmkq-fcuNndK3b3-8v3m8vU5pNN8EH8kEho51z8DuVXzztt8n7T0kl6ZfsxcmfPEvq4DqmtNQECBX2-oZcA-bHoTSysttZBh-rVuQxjHKFlwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UdzOHfoIz9u1CL1MzC-Mx1wF2ucFUeTJwiI3_MHYBKkABYApztwi-UxDbr3voRpNK_v-3ew1V5COEtmx543DLHom8boTaeYanT-CahexGHdRbqhw2hRcA35tXKqYDPc2rlls4dZa4bxiVGwr6-8wRgGcfFTD1LzpJ_4Rz_EasvOdFknXfI7upzjV9ZxeVCcTP9P9NaQjkyF5vsbmoxmkKmVyK8NGBCBunPc5wwJVu9iNKqqfgxXqXBAu5P17GwXB7Jfn2kExupwvsmkPk3fL-IjXNVG354DFOHf_tdVEtxz-AXg85GRv6fVHDXkEJtvLbjEqPgwxGDU-opHme9CVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQedrI9_8WVlMhcilFRX5iO2M12_KKeYLXaKf2M00GeCxzcinoQ5h7kTVhHBrE3lw-1LSPHiYoE-nuEMl-sq4U6C8jGPp1rufHsb7R3BopPUnpDICxLzTmo32HMGME0aR1yoS5yl4v3KcfwUT3lMdBpfyCvyUPMrbMFSD7gNr_PIJ1yVbKccxUXTkbCU3Eqp5xsVUQL1NgAgLemxaLcRXBuE-so8eiXweC445ipy6gl1HRWHEhzmMTjRXFjSYNXgggn8XGlO83-0ENqrRNbJmXzqdNUt9z4oYUIIxPBQkaMFB6ZhLHrNJRKSd0X7INWHpn-XqYQZpjNC59Zli5tWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwVtIY7BJMAttxrO02dTeNO9ZDrrQPygSDN9LJG3hPmgzyC_dLQLW4AH0_pM87PLEZ5lFBmmiIaawjjeersqyA4g5xPCwdj5yO4HkQ33e3S8_Tl04Y2yZmyGA3Nng76i7QbYlSKk3dtqQHRYFRhGe1K3fVYxqUgqGTfUhRyLpyhzuyiaTOJS8Nkm-3s0cCbRno_dBpn_KN4RCZhJKWup9HrVm4Y8aeQW6gSdRbFbRPfcu0dECYEk-dYu2WexxdFeul34Pvik-mIbT_h_z2pH8SgO81a4FIwv5lbZyfU50tcO29En1G8EtFpmeqPRJMixb6YDgSot4A1RM4L5H2M9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XiIpwcASfodj_yPX7eVlhHEdZ8g7SvxcXNTrD6UpzZpuUT_pwn_SAW1evAJ6YSTdIq8vxkHAX_Zt2fhMbiYf451YbInx4-qjPq_UhWPt63I8NBZMZ6v2T_qJghnwpvPKwIdLrMbm41sl4mV6BNwfsnC_ozqzib56kyQkr6OjiGFi4ivSBuaSPbxPAMOOhNF__9EoPy90bk1-yGMr5ochS2fTX4uiB8p-YASTaXv09ITyz9_e9A-WpZQzwkQB2ba27pgjevm_lQWJ3aIgV-LGJfqYThHuzSHNUBXUTPm8rjm4AifQiAsW2xx5_b36lb5Uzyd7N_Q4xl2YIzYgYWD46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSPByeq4j5q30ru77V6jrma3uN-6vqQQy1d_15Pm-te1PIMNEuDjwsT1KCihRipaL0yoFiWlE1H789G4ZyPilgqEwYDyc0b2XFyrojWFq06xdp3BTKE3wAnF-KYD41XUOlovAr0ZG8GL-HIvJ2CTO4Fxpn2-n8B4wIlmnjNrR2AR-V_ttkY2md6h6k8owYJSKJGmHjLr2kNxX8cSfS5_4tg4elVtz_A_iUbbHWEMu49w-oIIKJhku_2q4kVWWf-aT81mEd4tsMygK9Cly62NAfxerR6y9apB5vRwwsAIhwJ3SIR4fGoFyri92ZKNV2ezvWrsUJlLtgHIipebn3TXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVRy7lInb2dXBRiSHIwgPAravnf12Pn9WokF4UM2cN9lvcZLq8Zqq1UF7tn7qEzmvxaWR4CAx4_iCkcCKQnXG0xiatTy1RDFRNeR4E8Xy5ylzihMUZMs0kMppBkyRcV1nEB3Q5wR-er1wINktG7Hr_hFjTa7zWBf-d_qVcuwNxCksFn72CHTj_hiBSyYN3JIIYxv8I3PGlo0oPxgowKRpgWpw-imitzPv0bFNEier1AMk_mrSIl8me_Cn48H7dyIdksTFeVZjoZTGvsOayHFxWo5ZJGjG3iKdPcaw8AmKV8Hj-CkBkAGMZFyKbw68PHYeU1CgJOxzjEkMaacFQDu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA4R3uj3LX_0KwnQBL_iUWcHkveSG4ltxj8wE8c9MQyFTdQfikhGkbZVcg1lF-AWyX0dZgoWIYiWwNh5qS75TQyK_jgnESlathFpqS7XG7erEFIBhsTrouUSmGGYLUP2TqIqUQ1MfNmJh8tEUPu_xyz_tBFJhdMliqeDkxvqEmoER4nnVFnXCd5m1l_0bxbtGX3sg1yGnK5j923Llm_Rd5cL2_hqHf399lVre65FcQDAMJJcoJUtY5PhqRKhQWAfuQ4eFntzsdMYiiQky4pUUeHWQbK6zQutbUKiHbAIxN7ohNDQ_XbihbXix1N7gp51TLmW3R6VTpNyx5MadbRtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuLjJkNSHU_ZAzLmLZJFK4V_IoCm2vHFQRQZtSG8p35_hLxdkGUHERUxBkcDQbF0mTyfMcZOZuvODqT7OIBRtst0S4DuCmtZa26xeA_1SyqM0I5d_LH5iA-grH0ElMQVbiRnsbQSpBkAKZE3KdjxfYL382Q4LIW9UQTlYLJZQAPvuPVst949ggEqMqYe2JtKNHe9YASnA0SqQ3FmMt-Qmj7z9aPt_ayj2jTK_Bsd3JEnRQ6lFT9dZnbXsNVqAswkAsxi8wiCRdWa35VenaaQTyuZ9pWfmSj6R41t9ElAfN62T42UO1KkljtkxFKLp3wUo5il6_szC6t_C2jhwSa1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBn-SnIE5bhypAfAwMeFsUgOdwfqLAROM5qVAFVYQC5dxNRh_I0MEPvoIFZNZLV8tV0vQZABn-YWlmsXbir7M6lvn6LT5I-722CEctwBUyayrAN5FJCI81V9g0H3ofBro00L06rxRJJpQ0VZ0LLsci9cgVvShpHSzd8uHmHi8bNYfMaFpWq3cRvkr05OI1y5y_SS7jMInOTOc6ETrQ4OjcyUyhKosq1Xx_GR7LJga34cGMz9u6A-FpFgVLsotJEsMHs89Dgs1r-J_bEAGUdEvzI0IaqXeoeU50cVv-2K-q-R19HqJUBaiT94U3EUfSbvysl6HtVxrrBNunE2q49mBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3IPYyLzGYp7OOG4CFzoUg6or99VZC2YRLZgJqy9nlzNIl7TMYX29KOFT_89asDxcc4bxS1Z8PCyNG6kXmLmWPZYjGfMm32wMJCihlF4jv1GNvENtRFh_ia6HYLi01W80o2TJQo8nFi4cKnUDi9kg0FQPNZJZ9WmygmaK8qHbaSqaTRY7m5ckPiOXwuCHBLgS0Rf6KNbelGwebUlqo0jgoCJZCmr_mMPX_xmrGizCA3mwXJo7zpjhirbJ_eJdBeIbEC6hiT6XyB88rgVm7YiGaHPLkAyi5Y5ktqlGrQHQPQ6Yd6O2HihR21a_dQd-t8JNUJ17dbnuIk5H7ITW2G4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJ08iX8HHKBFYUTYR0bd5VC7nSpo4HiWGEoTC1NAmnyc-0sa-BCkvthMLnoEAmNo0Z0nqmDWqNyIckTDCFlE-eehkMmvcmA5XxSn46Rcigpk4m3NyHLM-IP48zg5DVfY0HQjdRwNlmFjk3KUTPvRPY9XzNx1eByMolFbYNpsGTsYBYo5lItMn1yEtv85Qe3eDbXMrsBdpyPsQb-OU3jYyTFTl2Gmdjyy6gga5vW3Uu3FKXi6q3PGfg1snX-aGLPMNM_LZivZ2Zslaok4PkDZBGBUk4yzF7wX1gykJEla4WWwDVS0DyWdPIynJztQZ1QOV9fb7x1MINR_CecZFm5Sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgOvz2bAdOyHdpDYcMFbg_Zyd-z983zAjP1INfYpVJS3GtgNNm7_tD7xj5Oen8ZLulCWNTmoGhV9UzsUr5OXoS2PdoridjELtzbIYmy7Enb0gmldxDNRGlQ6xpmt4JijpArTomk_2pzobV_KvwcSYQ1ZyFdBfNSqeUNTCxbLgCxMNIlrVTyIHWlX9Dx4gFX9CQlcan9-xho1hqVp1t7vMkGLB-HD3eBXjC2NEoGWaGGTKIebrNkehB1-FV0MD9gPuIbLEiDTAxXEWOldw_MT1QKT9yNX-_5Reujyn937NuxPWGEHjCl0GJQ-CjPVfGaFHE7_AJDMKL5j6_kOsolnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z4HwfeG56S5JkaYnGZ_GcqyAKqU0ANMFmqtm1wAPVSknXmtZ4175FTo0c6rTE3dgJDU6QTsIp9nmET3OJAYmHWxozY-1WZYu2rSTXfxt0jO0S-raRb-6hItIvKGiipiX8awlS1bMQdfZzq-6n6vKJeNZvGaWXGjd6Ko7-P_9JurINJciW4k2cxFF7hQD0kbTs2ZQeKccmHLpioKNhFxVe7zzsY8isD-FRo21yrDyHO8K8nXQCLj22bx0c6nvZ-8w8p2WH6QVyF26X9-gpLe0c0GxSQ6A4RPuYIBm5q6v8FIJgf1eGxeEWRSllIuDMNoU7YW5aGgMaDG5zv6g4iM-Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2SRpZpR8X4IEk-JRExzAAsJS69gP1oPxn5dBILLHAz2wkLyuqQpkwXEU4QjcfDq7hGrHQ-E243lIcaucf3P3F7OweeF-YGEXuZyueQpU1MafJjpXZQJsP45K_3Zv7kLg7HCZYvDgYqAnoamU3Kv5-t44KiXq28CFFV3ibRvqWtTuSx70OgatiLrYukSveS3xANVMe_1G9PHnKDOG1I0sNrMuH2m8M_sGqh5WjO_r-HbCSKGrB5bGMpZqv9tm654Wk0D2TCOwchRjg6F_kDxsKQ5JYWL1Xo18rb6x895rcYm79NQj_hFeKx8EKBRBFtP5M1xJoQJepBXREF85C6sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=GW1nQImGhCNdJs5LJLTgKEHW1X-SyKiDnWZ0ybE-rRLqFIbVc6EHdRVVNocoCPk4y5ooKsGsYNGDrNQv45Wr-6jq-uV5a0ujjVNOewBColSYseWNzBFkJAGkXxBLjulkxWE4OPesNMRaGtplioLfmStbJOKjv9LIkdxA2cSsX8YUC9_FYZPUEyA9kL-3pLKEFNUjv9nEMQFjRgLjqKyVhfVsxRd3LInyc0-_0sic7xKndrx4FqVPdpELYgICSnOX3txCwQNkCP9BEOEq-2sHZW3iumYADrIeNwrxCkjzrCHdJtk1AibKK4t3rQQILQ0moEkl07wLmzikDS3ZlD8Vfg1R0cg1Pn6dH5kXEsgi0qijuDlv4pLlCrsCZ_kjZTBD62AP3lUMLAR1f37yM07k0WdgsS4Md4SehuN13EkRlSY0qPROv0raWuiXDg8zTynf5Zgz5o_XWIlHlDtjBAD0HXTvHS8HzJAKT1OrVSUuRuwOB1p0-h5TrD4LEzGHyciQO-ZQuQI1GHsO4tqzX7hQJaxpEily-5tmdv4wisZfZE43LnHpMrBQhCfjASveqpWvRmPENiqx5YUNBKSV5TMpnfXwTzMdTzoiOuWE2uZFN09txQhuo5uZaXpF66JhR75-5J-JF_QeDPGMQcV5td2S3trBfScqb4ELS6zuJx3Uhhk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=GW1nQImGhCNdJs5LJLTgKEHW1X-SyKiDnWZ0ybE-rRLqFIbVc6EHdRVVNocoCPk4y5ooKsGsYNGDrNQv45Wr-6jq-uV5a0ujjVNOewBColSYseWNzBFkJAGkXxBLjulkxWE4OPesNMRaGtplioLfmStbJOKjv9LIkdxA2cSsX8YUC9_FYZPUEyA9kL-3pLKEFNUjv9nEMQFjRgLjqKyVhfVsxRd3LInyc0-_0sic7xKndrx4FqVPdpELYgICSnOX3txCwQNkCP9BEOEq-2sHZW3iumYADrIeNwrxCkjzrCHdJtk1AibKK4t3rQQILQ0moEkl07wLmzikDS3ZlD8Vfg1R0cg1Pn6dH5kXEsgi0qijuDlv4pLlCrsCZ_kjZTBD62AP3lUMLAR1f37yM07k0WdgsS4Md4SehuN13EkRlSY0qPROv0raWuiXDg8zTynf5Zgz5o_XWIlHlDtjBAD0HXTvHS8HzJAKT1OrVSUuRuwOB1p0-h5TrD4LEzGHyciQO-ZQuQI1GHsO4tqzX7hQJaxpEily-5tmdv4wisZfZE43LnHpMrBQhCfjASveqpWvRmPENiqx5YUNBKSV5TMpnfXwTzMdTzoiOuWE2uZFN09txQhuo5uZaXpF66JhR75-5J-JF_QeDPGMQcV5td2S3trBfScqb4ELS6zuJx3Uhhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKEI3oNLonNr1x1LyOiVARJ4w3fEYuzaOCDzPiN8ikKKik7se1ys8BSrm77K_eNsFN1YtYsfDPGPlegJcFuJXhW-CwVcjn5cPISgde4a9aBTKm3v6Zw-vd8z8YBTO56umCcwT9cLQ3v3-8CianAliyoKFm1R3ofp7niW-Pqt8lB5Ga4Cp-EbWe-j_NI4iYjyyd6Y3GCtrdX2cEWB6RScDoZY75OWauzXIMF5qTZqVFFC0BvvYGoizyPXVcBvoczklr9JsKQUOPFtaveicjlgYPobV7h-Xvxl8wum3RvwKb99uksVotvpQhKffKGsvfwAC_akAiC6gsCnNepSlPRhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbXGT1NVNbgumliiRn8bfkyMgTeOWLgRURLCA7vKPkk1UfX4bkwhSBDNMgw8iIrODzHmqqBU_RkKE1E_JizPLS2BmcKkKghygBTba9UWFtqtVfxQkH6bARzTgAIDlTecfqTDaQi6t1Z8tcARVA7Vh8_OgmPbCpDC1b-4lVIGo_fCVmIbLjDzaoPUV5CMhafZU5ucpV_h8DFWDKCDqkzi049zgzusVtvwLJDTeXxosHiyu1XkNvHpERmD_09TTXfoEVKlH5w26RuLi1LAo5Zn4MNl6EBtmoiFPZmFFRfbRvNoSOVh0M-Nkb-9bZHGbSjO5QFPOeLuipk3-SVI-8-ofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sB8SMvMVCyA-epsqli8k5atm-1TkaWVx6qpCX94fj0KpknVDxIoZCdr1LN4BF-dIY8avAvmie08qHHU9H7aTG4I0kXvUJkdRx70MUB1cAl5kvvRK2fX19RUxUnhaqD8kE3hfLPTbaThRuP0auuKEcOTAkPf5IpTzJllulVfD1jM-RO7QPwo5TcCB2fQYDiZjFTJgsqOyRSgMIKZsYkufoC82I0dvcahV-C16rxIulaN4Ei_8LTYzdENNXkP7KCH53MYOCn9s4oDrmbbsip6KLoAfkzvOckFuUR7NLtjpu5s8nbg4w75iqPUi_JOH_FUe3UA4cBki0ZgFGrE2ItCswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f1XiksTJDGP_FMzqiHVupvIv5ULapZNkRCcEG_rRCkxeFOvjzs4Mxuc9f1WQcP7cOAHAahNiG5RQF1G4RDbGrq0T97B3T0-PbIrtK7hHi1yDsZsfa6UOHoTZDR3IRFzPFXPcOalsHnyCPC0300rxYyTj5c2mfDBA9ela0PmlZMgYqyEd81kB0WADnKnSmwXbzZHDVkSsoZBXzOa1-RVIATEHkJQ0nRjsyaKtJnPa_1c4fpmd0jN-tuadiwVpDt9fdr4oVlEzbDhY5KReZyzDrHxMxqaLodzTreI42nHJy-KzuBpdhvUoCxiL_ogHgBOD2ZVkxw8_TXNMEgXcxAPRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DI9vSNKDf1CwZouQMqpRC5JtkZC08ybPcQVYNPrxaFqO-IFFlbZPsmenJOGwpiBkmwxQqDmoXX4O77IU9fTS8FeKNNZKtdW3uRgS4lpmTPDJ6g_LhdVOakDutiWwBh-E9Fs_b-9GufTPngKiIt0MkhkIKrZ4qFuxrg0jSEQWrPpYqxP7nUdIuhdB-pYfiPcQCnTVKpA9IypEN9jR4HaWtsBgdkUD38ghz6FE-J8rrApzglMShJNsQnIajBEoGob2l2gOSLirHl4Er43C5Dxe7UyxUZW9hO2mWg_IST1A0T2AGrG3cjnF7KduVBhl18euhVFcqzu224_UdHezdhah6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KSxa4KlHr3gIeTziRkbpA5itaBxmxySQnAM3dhpilPhoS12OagUAF1oNaJTaMZNisDnl1Hea71yfdnrLfzwJWLFbvnnSIH6HviywyK4W4bhrkmwDqI-C28yWulMm2joy640AnmDPRb4PBQnO2nBIJv2JD5oTUMH3Jteb4uOnSmJk0v3swo5koun-1CkZlJUQ681_dNO0m3TGvarl8Y5VorTws-oSExyo7GUQP5ev8VpZxbqx_khcI8L63bNAnf26gQJlnnvadSqP5vevHoA1EsO0BO9qeXiT41zVei7QH9B3Q7A9Xl2j4uvuX_U0moSkya3ghDiHwbAAHdh-UILQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tag6gxRMUX83aI9RxUHjfyoldc2XlY7q2eqzTBtdO7ziVwmOFWHvuW4CHC9sG-1viRTKUj-FivNrBr9Px2zT6Zl9-fJecmad2V3JiI-N_Nj2SUzRAnFHV66qPygfegArtB5UlOCFUEAADVJqvsT853WI4DkzWqI6IAfpcmcpqFXfp1ri-ne6Tsh4RfniG1-0Xsy-gZzAyyXEQQvfIZpIC9TFqdZUyYaP4i0fORoYk0Jm8RMyaQp66l-RSPCez_9Z2N7MijWGtFu-E0Bb2VTqiXEo2gBRIilCzEWhdTkAfQbl09TOW3z7W8b1srWR5V9KNDkmSHAhBvUMgqwsNJH5qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=LjH6dwxfEtwuggyabFvYprqP2zRlvu1pCFau-a30g3nNou_FFtqbMKiDfK6Vi5LirYNgGim1ddmkuGWp_Dh49WbjWNXz-g96v_to27uJbwUP2QwDYtOzMuj4GBdPOV4L-hcWs_gTf6klQJgoNVfl4I4Wt2mMxWZpJ1EiN52zK4-P6t3J6g5I-VgpCr3o9C7XmcD4m_u_VYqbcMQb_4MTra1r2ebeIlrWR-1HjKWtCWRbq-pQgm1MgI_j_cj_5tfvANcbJQgUqJ166XSP7LOd2cA9eMYoCH1NhMOxVs9-Lf1gCSFfF25NxtOgZE-P9SdfbOuzfbzSZBFa4BHT3Mt0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=LjH6dwxfEtwuggyabFvYprqP2zRlvu1pCFau-a30g3nNou_FFtqbMKiDfK6Vi5LirYNgGim1ddmkuGWp_Dh49WbjWNXz-g96v_to27uJbwUP2QwDYtOzMuj4GBdPOV4L-hcWs_gTf6klQJgoNVfl4I4Wt2mMxWZpJ1EiN52zK4-P6t3J6g5I-VgpCr3o9C7XmcD4m_u_VYqbcMQb_4MTra1r2ebeIlrWR-1HjKWtCWRbq-pQgm1MgI_j_cj_5tfvANcbJQgUqJ166XSP7LOd2cA9eMYoCH1NhMOxVs9-Lf1gCSFfF25NxtOgZE-P9SdfbOuzfbzSZBFa4BHT3Mt0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOvwY8VfAgA4DjcV-tyNOCh11zcZ3m3Wk4QgQHgoNolHWZCkaVOKO-HUFu69PdU2pfVp4soTYZ1lgSgCXiVWsGOUKwmFwmYSsKeKTtBqp1fSqa42e5AhTFIoN4hgNJiSii8gf3LMzBI-8sBq85pbZ6JEOdXCUVTx8v9D6vtizAFXzK2zQhdDzSSeNDljaSi2YsvmIp7gjY8wrGZoT7wAO_fCpYBtvzqn48KvETVoNF5BWtBIOen-al0r-B-pc7qcALlxLrhdg7MAmjgwaLBvsZRP4UlWNAPdLG0n6xBeJURKGaj8LxagkQhfK-DNUMXzo5EEamxaf27VSr0bd9JoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hgBJiVRoCOB4Lnar9CCfuNvuKKiS4mN6v73NeAIhesc_GDkqj9Ak4UbRsH-aL6GZPLu1_4fBKusVhrszH17PYWuCgEq3qIzxhv9oZU9U5knq0bAF6l3m4gBXV5Mt8TpLAn5u8jE70GGdAAaS8LqCtElRCsOS4Qpv-aSgIpRECe7LqkTFqIVVBnxh_6oz4Lk_JqA22dMTSO6_ArGH2KM5JzLSE-qKAnn5OnonAKDrdqrDqtK3qCAr5B69EeGVKNG_OynIbt4fhfmqonwtemmNU3YiQNNn4G8S_l11NlLlmshDKSYG0j9XGlfCpXXIlm-qK2JuxYG8tXTkBtxMIGDQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IRqcYX7khDr4HrgquQDTelRSAaHDktu_JG2g7-3_Sugg1ZJ2-wbn80CbSffxwIp5MLD9HYVL7lwuNNtLqyJnWSeloYCMIbkgs4XwTuFiVnkGOB4NvBh6pyT3DZfgVDvshW2BFHQwFFNh1FoG6zK6y7JbV8EA7KQrFuKJ8dHiAsp4vtjBOdqFuhFhjXM88V8nv9Dnko9Pa1Sp6mb7lfmpjLchxtca3aqqJo4uNvrRK8OoLJsUGrmD6_yG6jNJaZ_4IBtnxoKIMB8fo2c4LqLP_PHKaYZ69DcOJa98o6ZfdAcO0EVmrEOZnihb_0bGfxvw83TnJW8ovAUfLOtmwZeUgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=GjOzSTKkB5iw0_prN4yIKJ9JE55Vws1Z0757v1ncatIvHvqlJWmH0Dydf8-Fzg7T5EcA97xFdLyq-tqfNLEkcEfOy8U5k8o43ac4ZGAL6rYdpvcRwJj8lcboeNnmcUH5X2XwEcoTyUxjRjaRKotSGEXV9TZQ2L-na8LP702ui-cEC-4_VchtNnNiFq2cgpj2mMSJ-GRmcycdDD7qw_grSUfhlH301upVzCqkkvCG8bDYkPJDcscGB4VbUfwkeHGhvi3yxGzNpv6yiCdLWxcds3S8XHb2YUlYsQS0xLuLATrpd66qRYhejLoTC64KawcZFP3vfMzO8EVxOUOnoAcZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=GjOzSTKkB5iw0_prN4yIKJ9JE55Vws1Z0757v1ncatIvHvqlJWmH0Dydf8-Fzg7T5EcA97xFdLyq-tqfNLEkcEfOy8U5k8o43ac4ZGAL6rYdpvcRwJj8lcboeNnmcUH5X2XwEcoTyUxjRjaRKotSGEXV9TZQ2L-na8LP702ui-cEC-4_VchtNnNiFq2cgpj2mMSJ-GRmcycdDD7qw_grSUfhlH301upVzCqkkvCG8bDYkPJDcscGB4VbUfwkeHGhvi3yxGzNpv6yiCdLWxcds3S8XHb2YUlYsQS0xLuLATrpd66qRYhejLoTC64KawcZFP3vfMzO8EVxOUOnoAcZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=DAW-fQt1_-yL0DntbyWk8rwkxatE0-UAriPkwoi95NgMiIL-PFcwqkXZ2ov8sLdCUx0xETs-kGpchH8epqbQJ3utfwjuDrfyWdn2uwZkj_ZJDFnBP56YCXYmM39YqVWLmnU-peSY7qHWlnx-vdTmqfDgELnRmZjnpz7kZ1Vhmn50kmtPjJ_RjAOBa4mPfUY9imYPP0lFvI3BqmfG3elX_fDubxKDHsjRkmAVKDfDFyvT_onYY6VjO8MqoLxpH6hZteYfXyu7D3OcGHDmlP0jLOIhccCh2MhH2emptyuBMuVJ9eRJH2gGWPsdFt8ywDwdqpYBh1fs9ZbwtuUbpobPWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=DAW-fQt1_-yL0DntbyWk8rwkxatE0-UAriPkwoi95NgMiIL-PFcwqkXZ2ov8sLdCUx0xETs-kGpchH8epqbQJ3utfwjuDrfyWdn2uwZkj_ZJDFnBP56YCXYmM39YqVWLmnU-peSY7qHWlnx-vdTmqfDgELnRmZjnpz7kZ1Vhmn50kmtPjJ_RjAOBa4mPfUY9imYPP0lFvI3BqmfG3elX_fDubxKDHsjRkmAVKDfDFyvT_onYY6VjO8MqoLxpH6hZteYfXyu7D3OcGHDmlP0jLOIhccCh2MhH2emptyuBMuVJ9eRJH2gGWPsdFt8ywDwdqpYBh1fs9ZbwtuUbpobPWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8YIEZm2CxyiSnIVEgt8srXae0Od0FYNjrjKriBOe6xOB3sO-ufWrq7yZTyJ4SC_DWmOmS9Yj8eCdRTslIGNKN64fLzTKhmSMjG07g3487FCON8iqYojZ3n4z5Py_ZjrUKnnX0oIJZnqq9SHrCj0zAaf8ZGZZvyChTMnEd9GmFh8Ncksir9zfTVCA7ePaMUKU7CYe81hqPQthRgjkyy6SaDV-1ocj-Ce040-fbqjKlXRUt3jjr-eebBHkPXVUgi7cOsWeedz7o2xqdHbgAmH8EzgrJVURNqDrvZc9U4HTaNEzLhgqzPHgWGmHZWwf1-KLcTZxLtdwV6CY1lMuFRMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vaIuaeQq5hUAyDkDj_RpZPWo_9ctlARu3G8dGihsqurdQ9l7Jak2pckSSL7tIxCjFb0wpHUmzuCqP6aN0928QXAoMr56byG9JW-YgoxYjRxUJBqpNvLaHXxN1QqQTODUdkjwP95SYjrrW11hm_96W9cYkoB3HcOqzTN09mj2AuOYdSTDAf9qJLrl7PFnMG5DA9MUAiJkUbjhjEFG3r3LDqvjy7nLko-UPNAe0Gv_pxUUkIWZx7NbAB_8Bflghc_DZoWBbWaBBQTfoxQehlPF3SWT2KnmWdPbGibnRwQqEpToib7Xs1hbfZay9JywUuFOnx-WmtePYxHOmd_aht920Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQhWn_VdhwPZPOFO_P9ZUT4XMgObXATZh0VtHQhLH0aWP02Gb8ytwiPY3OPzVelUNNSRDxLjhY2K_18GNo6FmwWXNeceg6bvHXVcNGYr0rgL-Pq_f6w81MnkPVwZEZwqqWi39_rsiGtbznPdN6__58bTdViyR_dlbj8eCjFPyRVFIfm-LYrsKisdsTu4F14CB9BO1LfS4YD2axOPXFL0gk1MUowa8kKmvTTdB9RA5wC_LuAGFgOksOpKOA6OQcJ__FDbmhcxDFyZPI5jRBLfXp-DmAtgg37EIvJCKuay4caV8dQn8QES8kxUvr1NYXinBK1dflxl9PBLp8S3U1SsUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OYTZLeyunINhr4Ob8HBfL6tJYgA2dy0R5gs5kgzhvrnuwaLD7X_FEt3yyN-CWrK5p1t6pwbaDe1fPrUd9A6YHINNF7AkMKrqcebQirCbZDaoZY9fUNK-pkMahoHtjuaYqDRdX6IXHH-KmsBnHUfb4_Qfh53QyEtO2a2dC0qyR5TFPOF0UhUkIzRK8ZBYJJ-kRo5PI3y0qXtMzHhQ7lW0bAKA8yfRrmNaNuh86B4i2uxjuQAh_iA3RuUHNKL5jyQuCVvrxqDJri7L70BoVztOF8-o_Cklyaret3BWY59xOunclbTh2_A6_FX9iOcCUg6kgFQ7tSTLuWfs9Q3ZrUU3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpG5NoL1gblO5AzQEhDLqQbhqMlghW7n9belm3zkX6DmSb14rRai3-rC-bdlwPi0_ldxS66uEAOQIwoPSWEeJS7ZnBAGzfSni6Fn43rIhbURf6amdhamOTaIS-_Si-Oit6XW7x0Kz6C8OqO-3Ij4xCAPXdy4Q5x00XFiNXoBabaJNAI_UixZyUtap8UOFQt79EHLgeOyHAD-3bv7wdy17XG31FVNyM2fSasaKEGzEXomZrC8MXG5jfajUw2-R4s_Ys08-Lek94mpgGB82uRrGYxIkuyAn-Mw2hu5LbJtrNp2XVtZ_NDUsUoXkX66F5_uTfhcQYvYkpJrfR3K2imOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J7lVnnvgavG52ucdHKtLasvSTTYrDoz_6ZdCPSLT08NMZXxtgLd7O4E42tFAbnhd3KbKD7TMVnePpHKQGvRrO0aZuYySVZfypoIAYhVi9jGjSEo87qZtP3-7AnAe1sA520V5AbiZTyD5U4LVu4JWnwXcW-DsFhlVDJFXB2oGpbKb5xFc4DiA-ZS4WQXz26IobwTHB2hxmjGPFeTnTzBBIERC7dTYDmcqcMe6MDL5YMGnwQXfldc4BLRAnB6a5OhzCIm316loC2ROXHfXuecxHC9G04GNDtklgVIRekYH38bmdHFCuR8fA7RB_X3h8myIdFnLg2nxqKZboXyI3FwFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nI-2NE5-UBTd7syntMa4RRAEG3FrrPi3nQBRt3LXumt90O11IYL-sJeS9prb57odIu4tZ2T9YLPIRNmSxyRRWn6gkAJYtGge-xRWD_h8BA-JFvv7atPqrqqbPbtZ0z_ASSXMz7fIEsD2oYqVaSF3qMT2oc0VzyEF-B2sgqvlEgAHrDejD4PrYfqU7cz2Zc3DeMEXKYe120I8Rizn2m9QVBmWUFlhPGOr7hstBvz-QIeR2ayf5g8TWMd-1pG5Bwdz7BP3wFYf7pWeUU28SoxE0Xyg3J5Uf0r6QszLB-DfOX-QdyTj9MOPBfWGeDRGiyYhI3VnrYqfQruPbGoTU-QlJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOzJSr9WU1aP9rBJ7vPr1QlziXrCzpn1sohjWfa0Mw6W7J4Qd6O1nu6A0elFb_hrOpJ3KEOqR-JiI_FTeHko4acM-O_jWBLoj_lsvv-v8LB_ICzhS1d7K8O07HPiSp7xpzR6Q1J05E5RA_bMRjDD5ilDXWInG2Fp6INN1BOroc6RB-qO7KE6BDYNN89bCZ445r7VDCtFbp_L6I8jI6ftTM2v1G41FsbzNv4JbTp2Z6kTz_pciCASovEKwi2Wz3wY23qGTJK8LUIKFEZPI_KnXj-L6g3Aeui4D83-90OKovOQ3sem6MDqzMGOKh0suyWUSuXOHigkUAp3wycr2AMpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=PlLVlCKfJPrFOrL78l6Vqa0QZzjVwD57jK9CeSflCYheT2mjM07isbL4wZWKtLvojf-1n4lV7l_mN6e_JWpfUm0OjnxYrs_uOffCRvN8CrPqyeMgM8uWsyxCdJFlb2F8ie2giiP8RgvZfKY-UOWJqiyeMd7uFOlKTSMbpGoicTFmgfuYKBfV3gnSxtEnDulDX7GgMoTuGO6gbVOkknx4YmcL0j3Oyq8vDeUL4AWZyjUVZfgEN7s6YC9RiDA8ZCXEM2IXTDxKe9lCtL73SjSpvAvDp73iwd6MvcuysB57W1kwAHnzWHZB52HRvQaXFs2jSqdYO2TJC44zkG-SSM83oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=PlLVlCKfJPrFOrL78l6Vqa0QZzjVwD57jK9CeSflCYheT2mjM07isbL4wZWKtLvojf-1n4lV7l_mN6e_JWpfUm0OjnxYrs_uOffCRvN8CrPqyeMgM8uWsyxCdJFlb2F8ie2giiP8RgvZfKY-UOWJqiyeMd7uFOlKTSMbpGoicTFmgfuYKBfV3gnSxtEnDulDX7GgMoTuGO6gbVOkknx4YmcL0j3Oyq8vDeUL4AWZyjUVZfgEN7s6YC9RiDA8ZCXEM2IXTDxKe9lCtL73SjSpvAvDp73iwd6MvcuysB57W1kwAHnzWHZB52HRvQaXFs2jSqdYO2TJC44zkG-SSM83oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gt9MMN2IIhB3J3B5qFm_4tSFViduS2HltJblR8Fb63T3Iebo50derm8OIwITjvHTvk3-qWy3uCsSpborPc5hdJ_PoMhwtiEBUdmOoUyO9K656d7rcfS9PNacRo1hpO5vf5FbJQty5AGqxCtMAVfGCQwXeB78LF10aDPMX61EmhHNXe7p-yOmDs5cYSLDHr_ljPm75ZGqylaWizL0I9Tkwp9L_j4OXVHQfpzVmpszn2mol-3XGnQh6spzszLBKnFLsfhfamwbCnKa5aIl7oag0OJ2yrlB-X6ATSZbUq2MkwtjBnMT8Ok-Ty8jWqdSTNs9HJ5_D8Y6jWTcBaUH57eZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jn97BsfcLl5zLp2ViT-m6ovWofStIwcOC86Q-xfixTnXBJcfJo6rKKjWj1hkCtCGFthE89TkbYN0rQH4O2Q-s5o5XPapHOBOtGh7IQGXH542nV3FMGyvIJHQBnjZN5d37e7xpLZil8ghWRobLZSkvuOZzqwh0LnM3S-o8t4Sx7HH8QC7GG5Azevci-lbz77nLecCfW19GbbZiqZoYLFj_UwQccvO0WPqOtC8G5nVKYz8X8PDNl3uLeMkQRZUERg4gFNG1bpMVguUfkO-wxDAJTSNkR3h-6o6NPktvaDuAH8IRalTwv7Dx2vFWgyzVWQOMCJFWtOFFebgp1ox0YSrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPGc-nLXGZ5x3fsOhdohtkSU_nYDJ1Qx8804HnN1g-4g81dqJN7dvOdam8KQW27qmKlUqtihztrkNvRkiskaO80OdeEIYqgXVkHK9-4e8OWHag6D_aHG545Ni6Sbw12Xnn-lfs8pbeNaTmmJTzHRohCi3IxaKEYOROH2DMmk-8okq8wviomAp-rpZMrFrVEk_H6U2GNrOW4ybV4RLQyvN6zjWDSqvOCXKNR06RKcjPIV45HK3tsVwPWD5jJP9blj5EvtK7ubvuPXoSaQhNVwUz0p69bgYgJD6uO5yXzFkiXa55Z9ezQrl24LO7UMYHjzzAzXzHtfXhCmBEV56NSAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=istxwVi69wnTg15Lptpc5XD_fpdt1RUdH1wlOJ3NHgQPPKV04Gvf1OcA1NXoq5buhCqd27HDu2f0z2Bqn9KdQXxdy8LUND9oLvEYSnadkTTh5wRql_NGTsPNns3_I2M2E6y1h6Y1XNvrIiH9SW3IDCeFeBoR6cdWk2ATRT0NxkPumXXFNIxzz_sZlLEQ1SJ08Tx0XB0CQUrCDG9lN8zCVGrd4SaSw8FuhLZUEBhLO2ms-yr8aNCT-EJtE5e1__eIxhIU5iJ2eAJrMxMMq0bWrDadoOjUCvifcXPMLiwWdCNP0u5mP_H16xYVK1InoocKIhku8RozAWkZzQs4mCLf5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=istxwVi69wnTg15Lptpc5XD_fpdt1RUdH1wlOJ3NHgQPPKV04Gvf1OcA1NXoq5buhCqd27HDu2f0z2Bqn9KdQXxdy8LUND9oLvEYSnadkTTh5wRql_NGTsPNns3_I2M2E6y1h6Y1XNvrIiH9SW3IDCeFeBoR6cdWk2ATRT0NxkPumXXFNIxzz_sZlLEQ1SJ08Tx0XB0CQUrCDG9lN8zCVGrd4SaSw8FuhLZUEBhLO2ms-yr8aNCT-EJtE5e1__eIxhIU5iJ2eAJrMxMMq0bWrDadoOjUCvifcXPMLiwWdCNP0u5mP_H16xYVK1InoocKIhku8RozAWkZzQs4mCLf5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nI7dpbfgC_Y2zjgFNoCQ5LEZiNYie77mD8tmUEGa8GxeVZV88YNtiHJXcYXUa_MpjmRweBdoJM6d8cTRvWkmC9XEQXlUkS9vZWichSePa-IuDyLupMuYTJkkrsJ4151JP6AOL60ywx4HItj4FHfFc9glZ8GVqRHBsi6kc2qlQESpxcrDVg63ivx-a3B_aKBFZXzxCJwOfbcKHVePggj9RUd8SjlUou_XZfDAHBDF72DVc_wuAmLzzVe3VM7V6BuCgwQNB673qtPV-5IPbBk0hHhXavAvsS8ZC2NDGq6GcdqSFJiq7D8RTz7_n2_EfG9-zuOkPJJUyQlgzPxqPPyJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X55boiv4rjcgOmRxUQTmXEMX9XkMMCM7pvt28JS2EVWSIs6oE8RrdP1LMWHHumiHozWKxaiuVJqg3hVOGkNs3j6ViUgJp0Dpw4cgIADar_JF8XQNP-QJalkBqs_aMzPNwd2ILQxiNsK4fgk1gITaXPCo_yuXQG9Tz2JZIkwiK6zSO6U4WImzmqjbieojGQlhYqXL_yhDhc3klximE-ZN4oZDky_RaRe4K6yD-VdqnzmH1tDjPPnAdJ6KrKtqfT2Fc0RFmHcDETolc7XfZ7xIqRb8WP7VavTymJlgzOJR3DYXc9wgmZq_y7muzLJ5NKQjOm8dYb3D32gEHzUG9-Dzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=NZBN8Z73vC3K4OJ-4gXZbv_QSRqTFceLHe5AfA4DCCw95Q9wnNS6n8vaecFWqv27sesCj9U2OYzFR_gaK9BxX_P6DfzcRGNNt2qbytzM2rjP6l5VUc52yXLYpvvnJXXIfzGWobZD6RjQKmmPOUdBSFYl7NRmMt5DqWmFHnWpdi535H_MfcFLv_tEerYWKIKAT3z4--xqYhaPOtvVGnsi9TE_Pn-d1PpzU2bJT5mBHU_u9Bji2tehlOX2SG70QLRMeBF1E78fNFyeFio70KRRc32VyoNzPbMn6GfuzPwEgcnQGN4PRu7SXBQtT8LZZCyNQs_M0w4MRneGLAzqXbiPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=NZBN8Z73vC3K4OJ-4gXZbv_QSRqTFceLHe5AfA4DCCw95Q9wnNS6n8vaecFWqv27sesCj9U2OYzFR_gaK9BxX_P6DfzcRGNNt2qbytzM2rjP6l5VUc52yXLYpvvnJXXIfzGWobZD6RjQKmmPOUdBSFYl7NRmMt5DqWmFHnWpdi535H_MfcFLv_tEerYWKIKAT3z4--xqYhaPOtvVGnsi9TE_Pn-d1PpzU2bJT5mBHU_u9Bji2tehlOX2SG70QLRMeBF1E78fNFyeFio70KRRc32VyoNzPbMn6GfuzPwEgcnQGN4PRu7SXBQtT8LZZCyNQs_M0w4MRneGLAzqXbiPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7evXiSNYCRWnQBiEyeltlAEGejIBhSwk988rgQmu13m2cObn5sXIwk3ssA2fLal3SB30AV8OkKmNxTmIHl2Z3rl32COZpHQjeaxtft0-u_yImZla_rdMLYkgHrmBb7bfQCB5mCqYzpJqzK_EY6wFj3mZwx-dyTvtbqqeRjxWoYg8o2DU1J_Ed8H3ICyDUIO-dk9UFah54fwGnBG5HquSTa2uCfhG0H-hMVUGb9K6QI-PYYdgPYekkt-CXaRg5UjJwOkT-FNAWgOSNzpC3tgU5e08Fnmin-faVMVa9Rg7tVlQ15dMHhcwkhBQyFNZGq0uFnSWKNgNHUYqcHdNbUKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/URdoCxOkMMxQS7P85R7xuknQdIhsw54Wq6UZeBOYWAiZP5X6LVbkR71PzdrLC6DTht22AA0hPjhsbL5qX_KnfUUGR-74CwOwBpOn8502gQgqvfTmoa_KC64RLkwCAT3LPME7GYLbcBReouMqPGMDTij411nUsINEoLSbhqbTPnoNyXsGWx9WqWGE8krF829M_66CFYRZD8qARBnRweHRNglLMXRo--akE8kJP84OMTT3mExYbVuprW3Tdx4ZKLLZdON0Lb8RgQ7rtUTGRpCsfBcDEtljEXasr_6jimkH-THvlRrJavpRlh1zXz2gZ9PSwnwXVNShn4mCekEuMrUvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UODYY6vLM_aPeOI8GaafuPmBwELt9LA3n3fvgvce1NR8VOzRJ78o8ivt2fS8GAVT8sBqA4o-Pe3q2egXx7aAt0GhdYPkCPNn-A11NFmwmbNX2eRm_dLzwzi8ocaA38UbDtGsCp_ShDL-o1kxllpnHCGl1EGGD4IumjHO_50Vtbdf8gv-l6nsVk16y5KHuQpXISLwT5265yC2As8qPGx7KT6dGC3ZBrxGDi4uczvPPbFlGlFcmFWXMagD6C9tphkoiv8-KAIX_y2AAnkee21_M6FIzCqdPbCwVMA4AB8fmA5lNiEiOiUM7MrLEOm6wc7zcxTckcW2givq0TFYK5xuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJ_img_fxTFUFtaws6ZF_V85Wv2z0sAww2JRsicSbbzgqpAIW_JYJzomroY-xVoXWw8TWvJdYASMmHrRDRN0MovHv_RezwRLB_dNLxgZ5gRyROn7mFwNx-U6mMC1Hc9QkOviFv-8bfzrMqM7oA2mHL0ncVgn0m0Rh23_htOEMwwLusJFZFs6rNtejtZuPftVSRdoVJMKVJ3lM76b1IhCtjGoQIgJrccqChGlW08-t4hgpJ-vMqecd8TyVWKbQIE5774SniNNQ2CpseSZ9lLXnu2BB1K9giAxcTsRSDm9-r2QeT61SoOmLIZuwCk892EsdjM-I8hcdhxS8LY-KGZK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احکام منسوب به مجتبی خامنه‌ای برای انتصاب شش فرمانده ارشد نظامی؛
بازگشت رسمی حسین طائب به قدرت
دفتر رهبر جمهوری اسلامی روز دوشنبه ۱۹ مرداد خبر داد که مجتبی خامنه‌ای احکام انتصاب شش فرمانده ارشد نیروهای مسلح را صادر کرده و خواستار آمادگی برای «عملیات تهاجمی پرقدرت» علیه آمریکا و اسرائیل شده است.
بر اساس احکام‌ منسوب به مجتبی خامنه‌ای، علی عبداللهی که فرمانده قرارگاه مرکزی خاتم‌الانبیا بود، به عنوان رئیس ستاد کل نیروهای مسلح و کیومرث حیدری به عنوان جانشین رئیس این ستاد معرفی شده است.
رئیس قبلی این ستاد عبدالرحیم موسوی بود که ۹ اسفند سال گذشته در نخستین دقایق حملات آمریکا و اسرائیل کشته شد و ستاد کل نیروهای مسلح ایران در حدود پنج ماه گذشته بدون رئیس به کار خود ادامه می‌داد.
موسوی تابستان سال گذشته جایگزین محمد باقری، رئیس پیشین این ستاد، شده بود؛ باقری خرداد سال گذشته در حملات اسرائیل در ابتدای جنگ ۱۲ روزه همراه با شمار دیگری از فرماندهان ارشد نظامی جمهوری اسلامی کشته شد.
مجتبی خامنه‌ای در حکم صادر شده برای عبداللهی خواستار «تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیا» شده که به گفته او «تدبیر» آن در زمان رهبری پدرش آغاز شده بود.
او همزمان با انتصاب عبداللهی در سمت ستادکل نیروهای مسلح برای فرمانده جدید قرارگاه خاتم‌الانبیا حکمی صادر نکرده است.
احمد وحیدی که از آغاز جنگ و در پی کشته شدن محمد پاکپور، فرمانده‌ کل سپاه پاسداران شده بود، روز دوشنبه بر اساس حکم رهبر جمهوری اسلامی درجهٔ سرلشکری و حکم فرماندهی این نهاد قدرتمند نظامی، امنیتی و اقتصادی را دریافت کرد. او پیش از آغاز جنگ ۴۰ روزه، جانشین فرمانده‌کل سپاه بود.
احمد وحیدی از اعضای ارشد و تندرو سپاه پاسداران سابقه فرماندهی نیروی قدس سپاه پاسداران را دارد و به اتهام دست داشتن در انفجار مرکز یهودیان، آمیا، در آرژانتین از سوی اینترپل تحت تعقیب است.
او به جز مناصب نظامی، در دولت ابراهیم رئیسی، رئیس‌جمهور سابق ایران، به مدت سه سال وزیر کشور بود.
در حکمی که به نام مجتبی خامنه‌ای برای احمد وحیدی صادر شده است، رهبر جمهوری اسلامی خواستار «ارتقاء مستمر و همه‌جانبه‌ توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن» شده است.
بر اساس حکمی جداگانه، مصطفی ایزدی نیز مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفته است.
مجتبی خامنه‌ای در حکم دیگری علی عظمایی را به عنوان فرمانده نیروی دریایی سپاه منصوب کرده و او جانشین علیرضا تنگسیری شده که فروردین ماه در جریان جنگ ۴۰ روزه کشته شد.
مجتبی خامنه‌ای حسین طائب، رئیس پیشین سازمان اطلاعات سپاه، را نیز به عنوان فرمانده سازمان بسیج معرفی کرده است.
از طائب که کار امنیتی را از وزارت اطلاعات آغاز کرد و سپس کنار گذاشته شد و سپس در سپاه پاسداران نهاد اطلاعاتی موازی ایجاد کرد، به عنوان یکی از اعضای حلقهٔ امنیتی و سیاسی قدیمی اطراف مجتبی خامنه‌ای یاد می‌شود؛ حلقه‌ای که سابقهٔ آن به بیش از دو دهه پیش باز می‌گردد.
محمد سرافراز، رئیس اسبق صداوسیما، دربارهٔ نقش پشت‌پردهٔ مجتبی خامنه‌ای در تصمیم‌سازی‌های سیاسیِ مقام‌ها، سخن گفته است. او که خود در مقطعی عضو این حلقه بوده، از ارتباط مستقیم مجتبی خامنه‌ای با حسین طائب یاد کرده و گفته او به گزارش‌های امنیتی طائب علاقه‌مند بود.
او در تیرماه ۱۴۰۱ از سازمان اطلاعات سپاه کنار گذاشته شد، اما بر اساس گزارش‌ها یکی از چهره‌های مهم و نزدیک به مجتبی خامنه‌ای به‌شمار می‌رود.
مجتبی خامنه‌ای در حکم خود برای حسین طائب گفته چند مورد را «مورد انتظار» خود خوانده که یکی از آنها «تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن» شده است.
او همچنین خواستار تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت حامیان جمهوری اسلامی که از ابتدای جنگ ۴۰ روزه در تجمع‌های خیابانی حکومتی شرکت می‌کردند برای «حفاظت از انقلاب اسلامی» شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77802" target="_blank">📅 18:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=rdkDhXtb2Ovts4ZrwmjyJ1dMaeaPzXQgShm5RkMOoNwawyz5LZK06z23I5LcDGufufWX-741TnrHG6Ud-iXiMgtrIr5pRb2ITiyHfNr9_0tI4PAbM5XyinvmC6IkAvjhbDdcukxso9jZZZswGb1Xe0OrFXWHqz0iR28BPm4ET0Hf5KUPdP45ljwSgu-c283miI2ILXLVYvK5jGUIWRGZ8x94fntGefxnbWFcka3rzs6Mf7Mqn39Xamy0Qjzl6wyywdXn88iiZClTNPqLx0kaV5tjYugp0Xo1mwcNQ1uwLEjHFvG9kgN3UtjZcJW7PYCmjv0aFxXDmQ0sLBg2XOXYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=rdkDhXtb2Ovts4ZrwmjyJ1dMaeaPzXQgShm5RkMOoNwawyz5LZK06z23I5LcDGufufWX-741TnrHG6Ud-iXiMgtrIr5pRb2ITiyHfNr9_0tI4PAbM5XyinvmC6IkAvjhbDdcukxso9jZZZswGb1Xe0OrFXWHqz0iR28BPm4ET0Hf5KUPdP45ljwSgu-c283miI2ILXLVYvK5jGUIWRGZ8x94fntGefxnbWFcka3rzs6Mf7Mqn39Xamy0Qjzl6wyywdXn88iiZClTNPqLx0kaV5tjYugp0Xo1mwcNQ1uwLEjHFvG9kgN3UtjZcJW7PYCmjv0aFxXDmQ0sLBg2XOXYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFBOFc4137B9aCnFppJLw4lWUiSZwhTdApYdLXLPWIhmtnYnwf3uBtASYCnRgmCLRcJeBVcZ6K5KeZbSHnwSu59IEDbSIDJwz2150fb22xmMQY5cKDxYF8XlF2DfIp4FzywghK3shJYbQbVoClu09V8cS2nWxd8pR41w76Mmq8QpEVhbJQkwcW9bkM3diboUTJdnxWj6IZmFMZJKHYrnlYIHwBoveq6objupaEXJq6zWtwPrhHbnouypqfbYDOz5SxCdczhyfyLzB3bFPi1At_sXhlwYXnpeZLFW4IqnC650sKFQOUVd8ib2cYPk01xi0O7QfNDQ9geTKBYLHkfbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJbWaOD2PxCjDV-7YPrcT4CYJMS7CbXRY1NwfqnQ5QpZZ_3KIuE4AYOKiqv01OBNF0LjutKrecRIxcRa7W_WykAdjeXF6g7-hyo2bHlDIOYDXmHGnmVUmx6l-r_5HZ3saU5BAfzVuR0h027aRWlj44-dwbfg2kBiAqaWrHgeUD379_rr4AZIxz4KgYuz3uEoUZvwi2MP7x18qbUVAJ38gpKyvAZ8dVuGSKITd5xCgM5UjrLe5U4NiR4W4quiz-3y-cGxzM3k8Hl_MLDw7fFKPJuhQOyem0I7ZvsgSAXmPXRG9JxfiA5s_UrRmJ2TbGm9-E40mZGeo_UJOj8wsVL-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ios4lsBpUcWcYLB8uFE340aR5GmLKXkICbaUVFkXutcDBkomCBFPoTnyz8-cMoO5NNPjxQunKXh1BMSGGzVCTGBJRVCm13fHISC1eVkCjR9oi9ba2Laip0uqK8ofvemfbsV94WDo0ojWTkOMgDldHUvCxQ1yFeJiDqjwbeg_XclmC3KQDVcmU0o89CwYXrGv_oqIvD6G5KyKEcM5QCZFUPc--Z9_5BP_FruaAtTo1PnOgZlWYjbQ_KRqQObGOHYAE1nai-7zKal4ZqZAae_TDX_XG4YP9BZdAO_4dzNmwO-7IJmtej617UgJcJ-orX21hPBEYgTylcSspN_Z8VAYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IoCtuphB--kPIKGresKs1U9sNFIR3VXghzzObuizuP4bFwRpRFkAT-VtDk-7nLxW-JXESjzXJT_YgTgqJtBLKdkKBUiKrhOyvd_Id1-hUV2S-j2gjBb5pxgRwwfrNCWVTTgc19q1Mue05INNtJaqhsAXWa6ixPrxKzLZ5B69_V-trlu-FcO2qtFtbTvpHWzRVZCByvBP8ldmKxb7upKmKxVDDHS5PaIjMxy_KVZptfJ3EOBKV-mMxaxQ8Ee5MqPzEXMPvQnfYmlBR6Q-D7C2-UYh9bltNTINC-JSP8GL19oyvbJoxNndErj-84iXsMjrUKkgeHmxXsZH90Sr-IWcOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بحبوحه گمانه‌زنی‌ها درباره استعفای محمدباقر ذوالقدر از دبیری شورای عالی امنیت ملی، روز یکشنبه ۱۸ مرداد ماه، پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در خبرگزاری حکومتی تسنیم منتشر شد که در آن محسن رضایی به عنوان «نماینده رهبر» در «شعام» (شورای عالی امنیت ملی) معرفی شده است.
در ادامه این پیام مکتوب، بدون اشاره به استعفا، از محمدباقر ذوالقدر «تشکر» شد.
این خبر در حالی منتشر می‌شود که از دو روز پیش اخبار غیررسمی درباره استعفای محمدباقر ذوالقدر از مقام دبیری «شعام» و جانشینی محسن رضایی،‌ منتشر شده بود.
خبر انتصاب رضایی در شعام، صبح یکشنبه در خبرگزاری‌های رسمی ایران منتشر و کمی بعد در بسیاری از آنها
حذف شد
.
آخرین گزارش‌ها از فعالیت ذوالقدر به عنوان دبیر شعام، مربوط به پیامی منتشر شده در روز شنبه است که بازگشایی تنگه هرمز را به پذیرش ۶ شرط جمهوری اسلامی از سوی آمریکا منوط کرده بود. پیامی که بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت و تلاش‌ها برای بازگشایی تنگه هرمز را با ابهام‌هایی مواجه کرده بود.
@
VahidOOnLine
🔥
رجا نیوز نوشته:
در اعلام بدون تاریخ این حکم نشانه‌هایی است برای اهل اندیشه...
🔄
آپدیت:
کانال خامنه‌ای نوشته به ذوالقدر پست مشاور سیاسی  رهبر جمهوری اسلامی داده شده:
📝
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
💬
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔻
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
✏️
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
✍️
سیّدمجتبی خامنه‌ای
🔄
و در نهایت حکم دبیری رضایی صادر شد:
معاون ارتباطات ریاست جمهوری:
محسن رضایی دبیر شورای عالی امنیت ملی شد
🔥
اما بخش جذاب ماجرا
محمدباقر خرازی
است.
او پیشاپیش گفته بود ذوالقدر می‌رود و محسن رضایی جایش را می‌گیرد.
درست درآمدن خبری چنین مشخص، همه ادعاهای خرازی را ثابت نمی‌کند؛ اما حالا دیگر دشوارتر می‌توان گفت او از پشت پرده قدرت هیچ خبری ندارد،حتی اگر خودش مدعی باشد کلیپ‌های جنجالی‌اش را هوش مصنوعی ساخته است.
@
pourostadv
🔥
امیرحسین ثابتی (نماینده انتخاب شده برای مردم تهران در مجلس شورای اسلامی) علیه پزشکیان با عنوان «علی الاصول ۲»:
پزشکیان مقابل خواسته مجتبی (رفتن ذوالقدر و آمدن رضایی) ایستاده بود.
علی الاصول ۲؛ انتشار حکم محسن رضایی توسط رهبرانقلاب
با آشکار شدن حکم نمایندگی رهبرانقلاب برای محسن رضایی در شورای عالی امنیت ملی، یک مساله دیگر آشکار شد و آن اینکه مدتها پزشکیان به عنوان رئیس این شورا در مقابل این خواسته رهبر انقلاب (رفتن ذوالقدر و آمدن رضایی) ایستادگی می‌کرده است.
به لطف خدا، تقریبا همه چیز برای مردم آشکار شده و دیگر کسی فریب "همه امور با رهبری هماهنگ است" را نمی‌خورد و اتفاقا مردم فهمیده‌اند کسانی که تحت پروژه وفاق و با چوب وحدت، میخواهند مردم مطالبه‌گر را سرکوب کنند و مقابل دوربین همه چیز را گردن رهبری بیندازند، در عمل خلاف نظر ایشان را عمل می‌کنند.
آقای پزشکیان! حرکت در مسیر رهبری با حرف زدن نیست، دست فرمان‌تان را تغییر دهید تا مردم تغییرتان نداده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/etvIJAkpGGoLr796uE7WWYis4g-nsOxzHEPW_c2TfOLxpI92YytJdneoTgm0orYM5z_nJWM0vM4_sQ1r3S_R_HYMcPncgzJSPiIglyWxmK9vMDi4oj1eDtKu5uBI1FGjTF8y1ePX4I3QwIg7UsFInxODwtXU8QIMZyLztvNzJDDzC1nALKPveo-XHNelDvhzrK6MTy2Bj8NSEx1Yh3sxfuGy876fSux5Cw89ajhfEu1H4hlaqIwKrR-Lz5lVwCyzpe_dswI7p5Fe6vSDzItTaj9dq4DjV64fdssKi39SojcT-aNbFxUIvoRwySToVWgBJ85fnH-P-kWtQkNQPmEdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس: درباره ایران «داریم قضیه را کم‌سروصدا پیش می‌بریم»
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، روز یکشنبه نشان داد که آماده است اجازه دهد فشار اقتصادی بر ایران افزایش یابد — به‌جای آنکه دستور یک حمله نظامی تازه را صادر کند — حتی در حالی که این کشور همچنان در برابر آمریکا سرپیچی می‌کند.
چرا مهم است:
تنها یک هفته پیش، ترامپ در آستانه صدور دستور بازگشت به عملیات رزمی گسترده بود. اما او در گفت‌وگو با اکسیوس هیچ تهدید نظامی تازه‌ای مطرح نکرد.
▪️
ترامپ همچنین از اینکه ایران اعلام توافق با عمان برای بازگشایی تنگه هرمز را به تأخیر انداخته است، هیچ خشم یا نارضایتی‌ای ابراز نکرد. ایران روز شنبه فهرست تازه‌ای از خواسته‌ها را برای اجازه عبور کشتی‌ها از تنگه مطرح کرد.
ترامپ چه می‌گوید:
ترامپ در یک تماس تلفنی کوتاه گفت: «داریم قضیه را کم‌سروصدا پیش می‌بریم.»
▪️
«ما فقط یک‌جورهایی، نیم‌بند با آنها مذاکره می‌کنیم. فقط داریم ایران را تماشا می‌کنیم، با آن تورم عظیمش و این واقعیت که هیچ پولی ندارد.»
▪️
او تأکید کرد که ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت به نیروهایش ندارد. ترامپ گفت محاصره دریایی آمریکا بحران اقتصادی حکومت ایران را تشدید کرده است.
▪️
در عین حال، ترامپ گفت با کاهش قیمت نفت به اندکی بیش از ۷۵ دلار در هر بشکه، مصرف‌کنندگان آمریکایی فشار کمتری از جنگ احساس می‌کنند.
▪️
ترامپ درباره کش‌وقوس با ایران گفت: «درست می‌شود. همیشه درست می‌شود. مثل یک بازی شطرنج است.»
اصل خبر:
توافقی برای تنظیم تردد در تنگه هرمز میان ایران، عمان و آمریکا مذاکره شده و چند روز است که در انتظار نهایی‌شدن قرار دارد.
▪️
بر اساس توافق جدید، ایران کنترل بخشی از تردد در تنگه را به دست می‌آورد — چیزی که پیش از جنگ در اختیار نداشت.
▪️
میانجی‌های قطری و پاکستانی مطمئن بودند که توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان چشم‌انداز آن رو به افول گذاشته است.
▪️
مقام‌های آمریکایی همچنین می‌گویند اختلافات درون حکومت ایران رو به افزایش است. یک جناح به رهبری مسعود پزشکیان، رئیس‌جمهور، به‌شدت نگران فروپاشی اقتصادی است و معتقد است ایران باید با آمریکا به توافق برسد. جناح دیگری به رهبری احمد وحیدی، فرمانده سپاه پاسداران انقلاب اسلامی، هرگونه امتیازدهی را رد می‌کند.
وضعیت فعلی:
محمدباقر ذوالقدر، رئیس شورای عالی امنیت ملی ایران، روز شنبه شروط تازه‌ای را برای بازگشایی تنگه مطرح کرد — افزون بر شروطی که در توافق عمان درباره آنها مذاکره شده بود.
ذوالقدر در بیانیه‌ای گفت
برای بازگشایی تنگه، آمریکا باید:
▪️
«هرگز با هیچ زبانی ایران را تهدید یا به آن توهین نکند.»
▪️
«جنگ علیه ایران و متحدان ایران در لبنان، غزه، یمن و عراق را برای همیشه پایان دهد.»
▪️
محاصره دریایی را لغو کند و نیروهای نظامی را از اطراف ایران خارج کند.
▪️
او همچنین خواستار پرداخت کامل غرامت خسارات جنگ، لغو همه تحریم‌ها و آزادسازی تمام دارایی‌های مسدودشده ایران شد.
▪️
تا چند هفته پیش، این خواسته‌ها پیش‌شرط دستیابی به یک توافق هسته‌ای بودند. اکنون ایران آنها را صرفاً به‌عنوان شروط بازگشایی تنگه مطرح می‌کند.
▪️
یک دیپلمات از یکی از کشورهای میانجی گفت بیانیه ذوالقدر بازتاب‌دهنده کشمکش سیاسی درون حکومت است.
پشت پرده:
مقام‌های آمریکایی گفتند ترامپ یک هفته پیش متمایل به ازسرگیری عملیات رزمی گسترده علیه ایران بود، اما متقاعد شد که فعلاً تنش را کاهش دهد.
▪️
یکی از این مقام‌ها گفت ادامه درگیری به حکومت ایران اجازه می‌داد از مواجهه با پیامدهای جنگ، خسارت‌های واردشده به زیرساخت‌ها و بحران عمیق اقتصادی ایجادشده اجتناب کند.
▪️
این مقام آمریکایی گفت وقتی ایران درگیر جنگ نیست، ناچار می‌شود با واقعیتی تلخ روبه‌رو شود که هیچ راه‌حل واقعی برای آن در دسترس ندارد.
▪️
در عین حال، این مقام آمریکایی گفت هر شب حدود ۸ میلیون بشکه نفت با هماهنگی ارتش آمریکا از مسیر جنوبی تنگه هرمز از خلیج فارس خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
موضوعی که باید زیر نظر داشت:
جی‌دی ونس، معاون رئیس‌جمهور، روز شنبه به فاکس‌نیوز گفت: «این ماجرا تمام نشده است. واضح است که دیگر در ابتدای آن هم نیستیم. ما وسط بازی هستیم و مجموعه کاملی از ابزارها — ابزارهای دیپلماتیک، اقتصادی و نظامی — را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77793" target="_blank">📅 19:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3_YDSCiFZ7n6_dlg9kxa9hMLUicBTVDcyg647UyIyd1wdJNvm8KnqUyK3YEiXED322M697_2zdmAIeM5YZKOhaoFrQPgMPnTlW1E6__ogHgpxRDySDO6YKMdJVXpDeaA9DFR9H5rCMDiRW2f9m7LkGS-vnmL3h3J0Z0ZC0yZsHwx1ccAUyET-TfK_kpJUhG-fzsS4h7jVya0D6DtEljnoILjihhQ9wkRwiHsfvammDFbzCPlurTKYi6S3O6FJa6ny-azgbr2kF_Vm5R86liBJUJ7a-6J_m8K6VXQQhoSf8Oq-kTUfwnHiv2_ilhxNBrLbjCNSgML9zYec9cEkDDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DMrmfeN_apDJosjcfmouvg9g7UenWGEbtAf1Ub2MkVEwcBaqw9zlX55yM0G1V5v5a-8lwD1k3dKFlgzoE6SAYoSaKN4ktPnxdC1r63a6QDqLNuUM4FClTQD_9n0EHKNkKOGpo57Qa0G6KciMvcjcoeMYmlNFyCkSU7p7Sxv79y1BkWPzQQR8y0N_pMKBpxZv9IPConLcc5KvAKW4MUcuOmeOmvCuOfWifI1OGmVl3Oj3UFp40l-RJtdPFjzWm1UfL-ieK2GJqGc8AJM-BKZ5qFp4lPo2DIflkNBMOsGALNou1F_Ql-8uhu0GmuxGdViAq8BMwY76arTah813SPWRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری از رسانه‌های حکومتی یکشنبه ۱۸ مرداد از انتصاب محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به‌عنوان نماینده او در شورای عالی امنیت ملی خبر دادند، اما دقایقی بعد این خبر را حذف کردند.
خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از «شنیده‌ها» نوشت که با این انتصاب، محسن رضایی و سعید جلیلی دو نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی خواهند بود. تسنیم پس از چند دقیقه این مطلب را از کانال تلگرامی خود حذف کرد.
رسانه‌های مهر، ایسنا و جماران نیز خبر انتصاب رضایی را منتشر کردند و اندکی بعد مطالب خود را برداشتند.
انتشار و حذف این خبر در شرایطی صورت گرفت که در روزهای اخیر اختلاف‌ها در ساختار جمهوری اسلامی بر سر روند گفت‌وگوها با آمریکا، از جمله پرونده هسته‌ای و چشم‌انداز تنگه هرمز، افزایش یافته است.
@
VahidOOnLine
🔄
آپدیت: خبر شش ساعت بعد از حذف دوباره
منتشر شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77791" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=WWIvawlHvp008vbocjWPwAwT5j0-tbTZC1HYdJtp45zbu6iB6RVbQcnVsjdw5ezFzicRvNLUulIvf9mAEnr72fZRKvwTwzXWnACtKBeoZE93oYmRix-xRmg4mi9v442mzioap5hueJyflfnle8GBBbC1O-mDGRBeUQHrYR0j3gO0nOaMSdnX02Cf5Km3mBMoIbguBBHXTeKtf98iQoINzti9APGFn7zcQQ0yv4U4XinkS0PPy-N3hMR_1LurmATJfutS3T3OZA_Lx0e8A_jq44hZSEkBrwzS2ksIwxC8bjIJkWACxLmR6uDJAA9EXRo6U5nfuhuvfx9POJfRtubr8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=WWIvawlHvp008vbocjWPwAwT5j0-tbTZC1HYdJtp45zbu6iB6RVbQcnVsjdw5ezFzicRvNLUulIvf9mAEnr72fZRKvwTwzXWnACtKBeoZE93oYmRix-xRmg4mi9v442mzioap5hueJyflfnle8GBBbC1O-mDGRBeUQHrYR0j3gO0nOaMSdnX02Cf5Km3mBMoIbguBBHXTeKtf98iQoINzti9APGFn7zcQQ0yv4U4XinkS0PPy-N3hMR_1LurmATJfutS3T3OZA_Lx0e8A_jq44hZSEkBrwzS2ksIwxC8bjIJkWACxLmR6uDJAA9EXRo6U5nfuhuvfx9POJfRtubr8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در نشست روز یکشنبه کابینه، با رد صریح طرح ۱۵ ماده‌ای «شورای صلح» دونالد ترامپ برای غزه گفت: «اسرائیل طرح ۱۵ ماده‌ای را رد می‌کند. ارتش اسرائیل تا زمانی که حماس به‌طور کامل خلع سلاح نشود، هیچ‌گونه عقب‌نشینی انجام نخواهد داد.»
او با تاکید بر لزوم خلع سلاح واقعی حماس افزود: «منظور از خلع سلاح، شامل تمام تسلیحات سنگین، نیمه‌سنگین و سبک است؛ ما از یک خلع سلاح واقعی و نه فرضی صحبت می‌کنیم.»
نتانیاهو همچنین با اشاره به رایزنی‌ها با طرف آمریکایی خاطرنشان کرد: «ما در حال گفتگو با آمریکایی‌ها هستیم. آن‌ها ایده‌هایی دارند که برخی از آن‌ها برای ما قابل قبول و برخی غیرقابل قبول است. امنیت اسرائیل قابل مذاکره نیست و ما قاطعانه بر سر منافع خود ایستاده‌ایم.»
نخست‌وزیر اسرائیل در پایان تاکید کرد: «تا زمانی که من نخست‌وزیر هستم، هیچ کشور فلسطینی تشکیل نخواهد شد؛ نه در غزه و نه در کرانه باختری.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77790" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXDVFfKzvq0_JKWqpMgWBDWOhMIOdlSYgbfroia56ZXwgk_q8h-jD9APxR3OUF6c8Jlt4Tu2PSsf2-rN2JkLFWWUiwmPq3AwjT806HV_i2wysrqUy62AknvZj5BroOqkG_YMl7Cn5chY6ZQstdANG2iuHxZajQOTKltZDEwUf1ae19mL-oKqpK6POSSgFX1O4dN901IIzpY3uAlksXh0DYjOJmQkac4N4V03BSTGFTcXntU0TbSGiNTmFOYzt30Dwoo3k7Cvvjn6oSvi6gAd0KCnMiC6dT_OHa_GrfRCQ06ah4k2730wAsHTMK4F9-LrvOAbqDsIgUyIj1NLllfjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان امروز منابع حکومتی درباره قتل مداحی که ۶ ماه به بهانه "دعوت به حجاب" مزاحم یک "دختر بلاگر" شده بود تا رفت سر قرار باهاش:
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴ روز پیش ویدیویی از پیکر آسیب دیدهٔ این فرد در یک کانال ضدانقلاب منتشر و در فضای مجازی دست به دست شد.
مرد گمشده مدتی قبل در فضای مجازی با خانم بلاگر جوانی آشنا شده و به او امر به معروف و نهی از منکر می‌کرده و می خواست حجابش را در پیج اینستاگرامی حفظ کند و به مسائل سیاسی نپردازد که در روز ناپدید شدن نیز این خانم بلاگر از او درخواست ملاقات حضوری داشته است.
تحقیقات کارآگاهان نشان می‌دهد زن جوان با طراحی قبلی و با دعوت از مرد سرشناس به محله خلوتی زمینه حضور وی را فراهم کرده و پس از رسیدن مداح جوان به محل قرار با تعارف خوردنی مسموم ابتدا مقتول را بی هوش کرده سپس با همدستی 5 مرد او را به قتل رسانده اند.
خانم بلاگر در بازجویی ها گفت : من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و... من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند.
...
تحقیقات همچنین نشان داد این افراد پس از قتل، اقدام به فیلمبرداری از صحنه جنایت و جنایت بر میت کرده و فیلم تهیه‌شده را در ازای دریافت پول برای  شبکه‌ معاند منافقین ارسال کرده‌اند چون تصور می کردند برای این فیلم ها که در آن بسیجی ای کشته می شد پول خوبی می توانند دریافت کنند.
بررسی‌های کارآگاهان در این مرحله نشان داد مقتول با ضربات متعدد چاقو به قتل رسیده و پس از مرگ، با آتش زدن جسد جنایت بر میت رخ داده است. متهمان همچنین درباره نحوه انتقال و سوزاندن جسد در بیابان‌های اطراف پرند توضیحاتی را در اختیار تیم تحقیق قرار داده‌اند.
براساس ادعای افراد بازداشتی، یکی از متهمان که به عنوان عامل اصلی جنایت معرفی شده، ضربات اصلی را به مقتول وارد کرده و پس از آن سایر افراد نیز در این جنایت مشارکت داشته‌اند؛ با این حال، متهم اصلی پرونده پس از ارتکاب قتل متواری شده و تلاش‌های پلیس برای دستگیری او ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77789" target="_blank">📅 18:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sWaM6u6upEMIzLsiUWwG56jGecc0z9ec3oKtzviROUH_uBjZQWe9RK6zfmBEpKu_C7hj2UcYQReiL4JWUDtawGQ1I9bKarIWd3q3kuL3AKt-ZxLt-9AvxoQRTzLL3KdoiHN8U5cEbEt5fHmqq6p6ypA9UzBLQPCVHxDCe558juEEP0DqpFjVsGz0mAu5Jku8HATImvdChanxZV3t6wkrrh6mp4FNmcET9D3cUiScM8-to1EPvRTSYQGsepx5dqKcjVZ_Zsl9-N8RZHhyIUkM41fdMJgvMYnoQ5JF1cO-Jm8r8W-axZxU0NcVhj8W6G43DQe7liBx7t3ouqUEt4Ekig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات حکومت ایران در عین اعلام پیشرفت در مذاکرات ایران و عمان درباره تعیین مسیر کشتی‌ها در تنگه هرمز روز شنبه، ۱۷ مردادماه، شرط‌های تازه و گسترده‌ای را برای باز شدن این آبراه مطرح کردند.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه گفت تا زمانی که آمریکا به گفتۀ او «رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد» و تأکید کرد این شورا «چه در جنگ و چه در مذاکره» از این موضع کوتاه نخواهد آمد.
او شش شرط را برای بازگشایی تنگه مطرح کرد که از جمله شامل پایان جنگ و حملات آمریکا به ایران و متحدان جمهوری اسلامی در لبنان، فلسطین، یمن و عراق، رفع محاصره دریایی، خروج نیروهای نظامی آمریکا از پیرامون ایران، پرداخت کامل خسارت‌های جنگ، لغو تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران است. ذوالقدر همچنین خواستار پایان تهدیدهای آمریکا علیه ایران شد.
ساعاتی پیش از آن نیز سخنگوی سپاه پاسداران اعلام کرده بود که بازگشایی تنگه هرمز اساساً «ارتباطی به مذاکرات ایران و عمان ندارد» و تنها در صورتی انجام خواهد شد که آمریکا «شرایط ایران» را به‌طور کامل بپذیرد.
@
VahidHeadline
شرایط شورای امنیت ملی ایران با یادداشت تفاهم با آمریکا چه تفاوتی دارد؟
انتشار شش شرط ایران برای بازگشایی تنگه هرمز، چشم‌انداز بازگشایی این تنگه در کوتاه‌مدت را در ابهام بیشتری فرو برد.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، گفت که این شورا چه در جنگ و چه در مذاکره «هرگز کوتاه نخواهد آمد.»
شورای عالی امنیت ملی ایران زبان صریح‌تری در مقایسه با تفاهمنامه با آمریکا به کار بسته است.
در یک مقایسه سریع با یادداشت تفاهم، ایران این بار به شکلی صریح خواستار پرداخت «بی‌کم و کاست خسارت‌های دو جنگ» شده است، موضوعی که در نص یادداشت تفاهم‌ دیده نمی‌شد.
پذیرش آمریکا تقریبا ناممکن است چرا که آن کشور را در موضع «متجاوز» قرار می‌دهد و به زبان سیاسی هم به «شکست» تعبیر می‌شود. در عین حال، پرداخت غرامت، تبعات حقوقی دیگری هم به‌عنوان آغازگر جنگ و همچنین اقدامات غیرقانونی بین‌المللی دارد.
این در حالی است که دونالد ترامپ گفته بود که خسارات حملات ایران را از پول‌های بلوکه شده ایران می‌گیرد. این موضع آمریکا عملا نفی ششمین شرط ایران برای آزادسازی تمامی‌ دارایی‌هایی‌هایش است.
شرط دوم ایران هم اگرچه به بند نخست یادداشت تفاهم می‌ماند، با یک تفاوت بنیادین. در تفاهمنامه دو کشور تنها از پایان دائمی تخاصم در ایران و لبنان نام برده شده بود. این بار اما جمهوری اسلامی خواستار پایان دائمی جنگ در «فلسطین، یمن و عراق» هم شده است.
به نظر می‌رسد شش شرط ایران نه موضوع مذاکره که موضع این کشور است.
پیش از این، اگرچه مقام‌های ایران اعلام کرده بودند که توافق با عمان به معنای بازگشایی تنگه هرمز نیست اما رئیس‌جمهور و مقام‌های وزارت خارجه تا حدی این موضوع را به بازگشت آمریکا به تفاهمنامه و تعهد عدم نقض آن مشروط کرده بودند.
حالا به نظر می‌رسد شورای عالی امنیت ملی مطالبات را افزایش داده است، اقدامی که حتی اگر با هدف فشار بر آمریکا و امتیازگیری در مذاکرات باشد، مخاطرات خود را دارد و مشخص نیست که واکنش آمریکا چه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77788" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XteXtWHASpCpouwad9uunA65AVqMxLOErKHlIJwVrvEN-tUZwbNSvVdpAxoqRDiY6mBLEVFIis6AQ8lvvUggP6sAAz15b7JLankwRtbSkOEu3UphHFbS1G9VBfMfAGtRKt36HHURCzlMw5_UPGMEusi4VxLm75Lmv_5zYRxN6Po_Z1QLOeZHnujWkNTVei2Suxgunsxw92emIa2FnZ7DoY89j8iW8pyG4hMIoYJd0QX_sjZUCYo7qp72JOuER6qEv5O7Hg8ysjlsr2R5NwhXr4v5CakbxeNwKfxPdT1uOQfbpDE1piYV0PZprUnzrMPzNqOWhfPN34JvvFa28ne7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام رسول رضایی، شهروند ۲۸ ساله اهل فریمان و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در دیوان عالی کشور تایید شده است. او پیش‌تر از سوی دادگاه انقلاب مشهد به اتهام «محاربه» به اعدام محکوم شده بود.
خبرگزاری هرانا، روز یکشنبه ۱۸مرداد ۱۴۰۵، گزارش داد، رسول رضایی که در حال حاضر در زندان وکیل‌آباد مشهد محبوس است، پس از تایید حکم اعدام در دیوان عالی کشور در معرض اجرای این حکم قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77787" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=cfWlajYbGZpBmYp5muxW63i3mm5nrVz8uGEIi6lCeDJ23N9Bk3vW5gEPx7S5wvR1JdQXRNcqw8El_xNg8iKxjzGJdTXa1RqIO9akJHVJML4igbM8MIPxCSA30Zs-YwKiulfp6AsM2zn8b4dqxhMtI8NqkD7YapKXbWgPPRz01JGdFtu-XS5W6nFNGU2go9Id4O7_uq-wxwMr8PhbGgzdfBr9FONK7qE1Go_NUo7mtPl35aZH5W4V5_k1XPVw65EwW-_g5z1tKwYv5-EAUSmWMM6NNy7l24nT5h0YDA40hmbujL2nYCulYxt9bKGifTOtvUEh1xp_y61R7DOAMTz7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=cfWlajYbGZpBmYp5muxW63i3mm5nrVz8uGEIi6lCeDJ23N9Bk3vW5gEPx7S5wvR1JdQXRNcqw8El_xNg8iKxjzGJdTXa1RqIO9akJHVJML4igbM8MIPxCSA30Zs-YwKiulfp6AsM2zn8b4dqxhMtI8NqkD7YapKXbWgPPRz01JGdFtu-XS5W6nFNGU2go9Id4O7_uq-wxwMr8PhbGgzdfBr9FONK7qE1Go_NUo7mtPl35aZH5W4V5_k1XPVw65EwW-_g5z1tKwYv5-EAUSmWMM6NNy7l24nT5h0YDA40hmbujL2nYCulYxt9bKGifTOtvUEh1xp_y61R7DOAMTz7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا با فاکس‌نیوز، بخش مربوط به ایران با تشخیص و ترجمه ماشین:
🔻
ونس: ... ما با ایرانی‌ها در حال گفت‌وگو هستیم.
تلاش می‌کنیم میزان نفت و گازی را که از تنگه هرمز عبور می‌کند به حداکثر برسانیم. در حال حاضر بیش از هر چیز روی همین متمرکز هستیم. فکر می‌کنم می‌بینید که قیمت نفت امروز به حدود ۸۰ دلار در هر بشکه کاهش یافته و گاهی کمی پایین‌تر هم می‌رود.
بنابراین فقط تلاش می‌کنیم مطمئن شویم آنچه را که از این درگیری نیاز داریم به دست می‌آوریم.
اگر به عقب برگردید و به یاد بیاورید که اینجا چه کرده‌ایم، برنامه هسته‌ای آن‌ها را نابود کرده‌ایم، نیروی نظامی متعارفشان را نابود کرده‌ایم و آنچه را می‌توان توانمندی‌های نظامی نامتقارنشان نامید، به‌شدت کاهش داده‌ایم.
و اکنون می‌خواهیم ببینیم آیا حاضرند آن نوع تغییرات بلندمدتی را انجام دهند که برای داشتن رابطه‌ای بهتر با ایالات متحده ضروری است یا نه. اگر هم حاضر نباشند، اشکالی ندارد.
ما همچنان هر فشاری را که بتوانیم وارد می‌کنیم و تلاش می‌کنیم تا جای ممکن نفت و گاز بیشتری از خاورمیانه به جریان بیندازیم تا آمریکایی‌ها بتوانند از قیمت پایین‌تر بنزین و انرژی بهره‌مند شوند.
این همان موازنه ظریفی است که باید برقرار کنیم.
آخرین چیزی که در این باره می‌گویم، کیلی، این است که همیشه سعی می‌کنم به مردم یادآوری کنم که واقعاً هنوز وسط بازی هستیم. این ماجرا تمام نشده است. دیگر در ابتدای کار هم نیستیم؛ وسط بازی هستیم و مجموعه‌ای کامل از ابزارها—دیپلماتیک، اقتصادی و نظامی—را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.
کاملاً مطمئنم که به آن نقطه خواهیم رسید، اما هنوز تا حدی وسط بازی هستیم.
🔺
کیلی مک‌اننی:
ایرانی‌ها هم از راه‌های مختلف این پیام را داده‌اند که می‌خواهند کنترل خود را بر تنگه هرمز محکم‌تر کنند. بنابراین در یک توافق فرضی، وضعیت قابل قبول در تنگه هرمز چه خواهد بود؟
🔻
جی‌دی ونس:
انتظار ما این است که همان میزان نفت و گازی که پیش از آغاز این درگیری از خلیج [فارس] خارج می‌شد، دوباره از آن خارج شود.
ایرانی‌ها به ما گفته‌اند که قرار است همین کار را انجام دهند. کل ائتلاف کشورهای خلیج [فارس] نیز همین را می‌خواهد.
اما می‌دانید، ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف مردم نگاه نمی‌کنیم، به عملشان نگاه می‌کنیم.
می‌بینید که برخی افراد در داخل ساختار ایران درباره گرفتن عوارض صحبت می‌کنند. ایرانی‌ها به ما گفته‌اند هیچ برنامه‌ای برای گرفتن عوارض از عبور و مرور در تنگه هرمز ندارند. اما باز هم خواهیم دید در عمل چه اتفاقی می‌افتد.
آنچه طی حدود یک هفته گذشته در جریان بوده این است که ایرانی‌ها و کشورهای خلیج [فارس]، به‌ویژه عمان، درباره چگونگی تضمین عبور و مرور امن گفت‌وگو کرده‌اند.
البته یک مشکل این است که ایرانی‌ها در آغاز جنگ تعداد زیادی مین کار گذاشتند. بنابراین آنچه اکنون واقعاً داریم روی آن کار می‌کنیم این است که چگونه می‌توان سازوکاری برای تردد ایجاد کرد تا کشتی‌هایی که عبور می‌کنند بتوانند با ایمنی عبور کنند.
این طبعاً شامل مین‌روبی هم می‌شود. همچنین شامل تعهد ایران می‌شود که به کشتی‌های تجاری شلیک نکند.
آن‌ها به‌شدت آسیب دیده‌اند. می‌خواهند این ماجرا تمام شود.
سؤال این است که آیا قادرند—آیا نظامشان قادر است—چیزهایی را که لازم است ارائه کند تا ما راضی باشیم و احساس کنیم آنچه را از این رویارویی نیاز داشتیم به دست آورده‌ایم.
این هنوز مشخص نشده است، اما فکر می‌کنم طی چند روز گذشته مقداری پیشرفت کرده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDsm9oZBobmhusKOvPJippPgmp3NqJ9Q7WWnRkeAfFEFmSphZU-ek-xbk_EpeoEJ-RWV30xy-XG9Rll03zh4ZuMDbfM5zkPX4P4E8vwa-ulzbkVFDyNAhiTlr75U8p0H7ZLwldZX5LaMuimdJNO9o5m1pu6qZAvr0QEV5ltkSv9_nfhKDC3hYoyPcHGuxoYQOxw-WNyo8cnCRjWBpSsSzz4D7sAcTn9s4uB5asud_6uqhc03LvojQsTzwbCWqeD46AdyWfxDQRjqApu7Fdhq9ZdvlpiPmx90wWqLroe9usSyLpotk_ivC9Q7CynhVlq_zdwD0opeKZIccAJTUYgUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UROJFFyig7WDF6vm-4st1EeqS0t5VDLhoG_rBG63d59L_SvfEjrVcqEvfftv0GosH49yb1INoufqRtlxjzyh5tpZsjE0ARzp9VMWSmHC9qkR80HNzascnvhwZNZmKOm8LGc_cquDBMo0MMrpM52J1d0zX_3LWFDisegDMat8FzDFngi1rESF_8XcfPgoxvsTgA_2OS_U06BnTHW6zuwL_GwW7vzhjeLMxlrXLDmg9mmVWCgm54fB_WUj1xxqbzDEvdQvWtn2E28Ev9CvOs0kxmQTdixfFR5jPD0ex8biJR7bXTKxUviVIE2Id4YQ8B1UseutZeCspbWdtodESCJ46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvuJ1Z5pM5cIYegG338CnXnbfk7fziEzCCvUEcvjysdO3WG6zxGDf7SZMzrWSldrqyJPRJSOLsvyJMzECj5GJ-9T_bnpcg1vYEFcs-jgNqq1GPJdSSTTqyafpZKm1bmBVdfAk61_MBgVxmYI0TufgR-JlschTP-EG23cFe76uz89pELcacrzR-Wco1j3nhz1m84EqDPvkINp5KdGpqBQcqAtXFiUn0NVrA0wDK-Z-Tr4vdKpZLQK38WOR-Pctl7I66IOsshGy51wWXQ17GIPB_G_gP9t2pDPyQXHog0zoQUJy6c8lHt3G8HCtNiQMT2r1RoU3OH5E9BlnjbkJElylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که مسعود پزشکیان، رئیس‌جمهور ایران، با استعفای محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdajYU_cCy99m5cdyrXwySrqzfiTBT7Ke2MjLykUU7Ak2Qo61f3udJ1Lc9WfPpH8mycOOSKTSMUyHqCUIFquKTvSgJ4TBDZFkuPG0553jGoL_ErH30nDqjaN1eXa-sypdw7TieqjeLs6QiKSfCG_hAUTP4NIOXcj7dq3WxTWNtd1F4IwXOr0MZO4ARisvowci3-2xxXLqgvRWUT2IF-60X8hgmOLyM4lAD2NP2vh2i7sqOwoo69x_3SwaYUueK2cauDPSxtxoMwKuqqoiRZeQBs85hjs5jmV3fMNYMqj-q-g3xHtCj0Xakl23Us055_XU-3Qy1-7NYuJnxzA29yqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/evtQaSyP5HA5YVUEdk3r8spffvfAy64lCnuJ8Lnv_kyWZXE2j1UBNV0NfhLH1NYyvsjwOZGPO0sgyHhFUWDdVhr57YgsSmH49iIjT0RvxB2WfAOD1qiOBJDif-zsAnY9Byolq6Hbc2kvxpqnnCTuhxv_Xn-qP3kKqA109zEjYrpn0mBiDRsv_p81Rva_a8NfC0Q2ot--qKY0eZDe6ACFaybbKsoIeT_vaEgdd5TJ909zI3DsGxxBZfzOs6dv7QmKyngUbcZ-JlAl-TTiHAflERbko1aMYCyfqITSy-udtfSJ5STFJgNLBeqEwU9i3pEKAAsTgvaIWDonKdwcgcUTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pn9IJdfb_xVyUDjs-RPJ2VYHZzlrjVI8JWiZkrcO9PRahsMBu1uNJxjO0PNUKFN5CgN5CeNFqg-hgWe17o6Bi-R1d34AFgQ8PMrOmqpIM_gFhRWuuIvzGUB7rWsMIwJYqAHDHNgp3Ec7PbMaHxTew7iLO7vhnnoxkS3zmygmjWxy0r2003BiequOITFGr7vUMabJbRe4PaolYHZiAfyZ1pSHKWHyyCj7_-NFzPA5b2amIDpNDyult2xZfrEkPv3Hk8G4MbU2-EORAU77FoauZhJWOPxv_z8LYeKhooYLxm3SZPw9q7VN-L-Ckv1EcKRbrTlkqUP5L7M-ulSYQSHdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBg3wbLQbiFVCVz2Io1WQMgqxgkC_7eTPgwNDGYeNOcSLoXi0KuJZihwdtF5E3RU8eRmt433A8Ye3_x8A3UidfOU6pfSlU7s-95YHZSf-uxdPd5SkJckMAzS9Yp4xuUGid2olTv-GU2r1I2qCPfczJbBC-WzHjnbIl5pCuQX6_ZAus_H-yOiPMGPWLye38Sr5CGONlrNBYzWI7mrqDvDneY2pEeWNIBS85P-xkNI0JbhDTkfVNn7QtqGqZw8e_YPyFsi9OKYQOBWpr9Ae8RtZu8_oa6NNH70ZiwFt2owmJvf3KgNoche4CkvDe21qdp3vDBWnwB4TJLGeJdgPPm-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCSy-RAjmw36uN3lkt7P9ZAB2Gks9A6-ZGWRHQFV6Xe7lyIxq8grTZHLmY1aatRA9R2oqNwbpyxMoAC0gEGp7AUjOPYkpiAHB-0cw3QlcSX31YKHPhkVrk3Vuf7FfFaOrbpg2xToyvgTp_39jchqHHc41wU-QHPOTFrVCwMn2h4f-gzLBwOLfCA8_TskdU_xrLPMf8rZEcW41PIDztOYybLkMCzCdgAZ-Z-cUxXrtp7Hd1Vk26VXKiUqkbtaXxfCjHL4uuK3E1hbg5i6PTstnDxeBJHMyAyRq8vf_2nTUZjYGqoKkEFbs3DcD1DnDf_ymKIoyBl00cULf3_sAfZZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srYYwFW7Es58YY1L5zOeuyuSSgIHK0TRxbT5A2agbLByq3-rtEYgXAIfzHj0ckE913FPS-fZu-MwFjSDpfGW7CZCZh4qE6hQQCmSjuwKSmbyjEFRkFoMXTcZ_khdFHB1LBP0SxuWnTNsvOfG4Zc8KqpckPXKQHYrGvkAqMJkuGiwEcHUdKgOvKTpwyiZJjZ7zWbUyfkfy-iSdKsRhh-3JyMX7Gq44tFdhpiriKaF4TOa-wupZEl7W3dc2CUlZhomuwYPHPbupcrFQWbv9pGUZ3hZuY5LFNDjbrIckWokniZsVoqCLR2XVr_2_x5MVL3ddENTaK4KC3QcD6OqqjTgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueBssJTuOb8mibw9LAi2fVwN3_DGGqZ4yv6jdzs3V6E6dok_85eZ3LnbLRpUegMRECXXZEPFvZO4jUy0DNZ_YZkG_TWqZLdDUAPURAJ8KYIyWPc7xZEksl6XSev7metdWvS_Dl_AiopYz_1HN9v8Dugjse8C4Qx9zp0SgBqHPmXpyr0rb2SS5e8plqmKL2W6cDCliuQy7VI2AWrm2-gcVBzbqAM82w-LVphl6lJLJ7ZaqVJx02YnF-RwBdl90azpmdEV4OQ3wgr8LqMdjENtj6MHdJwUJh3rTSVbZUPU-tDGmQGvLAUH5cgetE0yxUV1TzmA5TX7KMFo4rthMxh65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fa5zhtqytFx0rhMSiLtPOmTabU8ieypNObaN51Ae2zbLcqfqRGrxK_I8gQMJvj5eoLqL4RDavHHgjtZ3q6juQQHxHGZ9jQhPXa44L6yaVtjuIqOugqxsr3wPrmjbA2qDeUFN_I04a7UN5guHHVhmzXwd3anoIm0-rTuYXtFhA1-OCNTw9JU6-jd5yDYHrUi-TNLjOvlvRbUv_uzttEKibhCt6fgtZQ-tWyo2BT-xtKs6R0XTBHYERvOeNOURJmW0Ts2lry6SbaAlohPuS30meClOd9ZpJSJ546xNlxQr8m7oyqF_u-1BD4YbHTnBwtrR-8TLyYV0xgLmeJrVI6KOGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی
قوه قضاییه روز شنبه اعلام کرد محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در پی اظهارات اخیرش به دادگاه ویژه روحانیت احضار شده و تحت تعقیب کیفری قرار گرفته است.
به گفته سخنگوی قوه قضاییه، با توجه به روحانی‌بودن محمدباقر خرازی، رسیدگی به اتهامات احتمالی او در صلاحیت دادگاه ویژه روحانیت است. او همچنین گفت خرازی «می‌تواند اتهامات متعدد امنیتی» داشته باشد و در صورت حاضر نشدن در دادگاه، برای او حکم جلب صادر خواهد شد.
@
VahidHeadline
در حاشیه ساختار قدرت در جمهوری اسلامی، همواره ردی از «خودی‌های دردسرسازی» پیدا می‌شود که مقام و جایگاه رسمی ندارند، اما آن‌قدر به حلقه‌های قدرت نزدیک‌اند که نمی‌توان حرف‌هایشان را نادیده گرفت.
نسبت خانوادگی، لباس روحانیت یا وابستگی به یک تشکل حتی کم‌نام‌ونشان، به آن‌ها امکان می‌دهد از تصمیم‌های پشت پرده خبر بدهند، مقام‌های حکومتی را متهم یا تهدید کنند و سخنانی بگویند که واکنش و تکذیب بالاترین سطوح قدرت را برانگیزد، اما خود در حاشیه امن قدرت باقی بمانند و پس از مدتی با ادعایی تازه برگردند.
محمدباقر خرازی بسیاری از این ویژگی‌ها را دارد.
روحانی بدون منصب حکومتی، دبیرکل تشکلی به نام «حزب‌الله ایران» که وزن و جایگاه واقعی آن در فضای سیاست ایران چندان روشن نیست، و عضوی از خانواده‌ای که با حوزه علمیه، دستگاه دیپلماسی و خاندان خامنه‌ای پیوند دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4tdTkFiN0Y3166glFW9n16ARX2xYHMiFANoIrY8OjA5NswcknU6cnfrDeNaxFCKTTzn1qKr3-QUjtyqAp-qWJTOwFffAqW8_cyng4-67ZC3zMaW48-cJJN50IH4Ji9kDsXPgfkcJmMUYxvRbd5Cdc7Cd1cNksdOqvaNX2xrR7WaX4AWb_iFjavEmB0PC2vBw7e8rpSzJOiZw5lei5TSXJVhQX8eaAF3HLrmMIlt64Bs4o4JBJsBk9inZwuQkmxwLJvN5c5srsuRcoHXvsYxRpxQZWRgp3hQ7UmkLIiBtckjNW9F0wkarfzGDIbO2pjKdJCfhc4ow1mU-QFSrJhtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم روز شنبه ۱۷ مرداد از ربایش و قتل حمیدرضا رجب‌زاده، از مداحان حکومتی، خبر داد.
تسنیم به نقل از یک «منبع آگاه» گزارش داده است که رجب‌زاده چند روز پیش ناپدید شده بود و پس از آن، ویدیویی از لحظه قتل او برای خانواده‌اش ارسال شده است.
بر اساس این گزارش، پس از اطلاع از این حادثه، تحقیقات پلیسی و قضایی برای شناسایی و بازداشت عامل یا عاملان قتل آغاز شده است.
با این حال، تاکنون اطلاعات رسمی و دقیقی درباره نحوه ربایش رجب‌زاده، محل وقوع قتل، انگیزه عاملان، هویت افراد دخیل در این حادثه و جزئیات ویدیویی که برای خانواده او ارسال شده، منتشر نشده است.
@
VahidOOnLine
🔄
ادعای دقایق پیش تسنیم:
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های تجسسی صورت گرفت و نهایتا، خودرویی که رجب‌زاده برای آخرین بار سوار شده بود، شناسایی و مالک آن دستگیر شد.
🔹
این فرد که در ابتدا منکر هرگونه ارتباط با این ماجرا بود، نهایتا اعتراف کرد که با تحریک شبکه‌ای تروریستی در خارج از کشور، به همراه 4نفر دیگر اقدام به ربودن حمیدرضا رجب‌زاده کرده است. آنها در ادامه اقدام به شکنجه و قتل او کرده و تصاویری را هم برای خانواده او ارسال کرده‌اند.
🔹
به گفته این متهم، آن‌ها با وعده دریافت چند هزار دلار، اقدام به ربودن و قتل رجب‌زاده کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پست زلنسکی، ترجمه ماشین:
ما از سنای ایالات متحده و از همه کسانی که از اوکراین حمایت می‌کنند بسیار سپاسگزاریم. تصویب قانون تحریم روسیه و ایران، طرح لیندسی گراهام، قطعاً به افزایش فشار بر متجاوز کمک می‌کند تا این جنگ جنون‌آمیز روسیه علیه استقلال ما و مردم ما پایان یابد.
اوکراین قدردان
تمام
حمایتی است که ایالات متحده از اوکراین به عمل می‌آورد — از سوی هر دو حزب و تمامی مردم آمریکا. و اکنون، زمانی که پوتین آخرین امید خود را به موشک‌های بالستیک بسته تا جنگ را طولانی‌تر کند، و زمانی که ما برای یافتن موشک‌های پاتریوت به‌منظور دفاع از خود، با تمام توان وجب‌به‌وجب همه‌جا را می‌گردیم، هر نشانه‌ای در حمایت از حفاظت از جان انسان‌ها و پایان دادن هرچه سریع‌تر به جنگ، اهمیتی فوق‌العاده دارد.
فشار واقعی و قدرتمند آمریکا و تحریم‌ها علیه روسیه بیش از هر چیز دیگری کمک خواهد کرد. با هر گامی که برای افزایش فشار بر متجاوز برداشته می‌شود، دیپلماسی نزدیک‌تر می‌شود.
از همه کسانی که این را درک می‌کنند و از طریق
قدرت، صلح
را پیش می‌برند، سپاسگزارم.
ZelenskyyUa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 476K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e6agL9TTUWu9nEeFTHFqZ7zcVEbFYzCTGJV8c72Hcx1Hbqvt3XhPtRrTTK9jIW7Mf7IjxT7brwgG0CFPFyTEGIbR4P8ZSa-JFoUtGlGFnf_wH9KWjrgWcyfIdpbmPV4Wsj9yvq_C9yMb2HvrPaMxjNUilIgLAP_lCYBeOZEvv56RWyfMsbejODhN1oOgALd0YoFHns4K1Ioyu76PkyLmqPXS9pPZ8AD2bVX3GkLL0R_AzqptNAg2Uzh-9tfYhJ9Lq0iFM4enVTA4ue3SywVKkv0DM1ROuFe6r0e4sn-r5G52AnrZFiZT25WbpgoIdDjXKDVXULAIKY1c-J6EizrkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده آمریکا در گزارشی که روز جمعه ۱۶مرداد۱۴۰۵ منتشر شد اعلام کرد که «شبکه‌ای از صرافی‌ها و شرکت‌های پوششی مرتبط با جمهوری اسلامی» را هدف قرار داده است.
در بیانیه منتشر شده از سوی این وزارتخانه تاکید شده است که ایالات متحده در حال اخذ تصمیمات قاطع با هدف «قطع شریان‌های مالی» است که حاکمیت جمهوری اسلامی ایران را سر پا نگه می‌دارند.
این وزارتخانه در بیانیه خود نوشته است که این اقدامات با هدف برچیدن شبکه‌ای از صرافی‌ها و شرکت‌های صوری انجام خواهد شد که به ایران کمک می‌کردند صدها میلیون دلار را به‌طور مخفیانه از طریق نظام مالی بین‌المللی جابه‌جا کند.
در بخشی از بیانیه وزارت خارجه ایالات متحده آمده است که «تهران از طریق این شبکه‌ها به درآمدهای نفتی دسترسی پیدا می‌کرد، تحریم‌هایی را که با هدف مهار فعالیت‌های بی‌ثبات‌کننده‌اش وضع شده‌اند دور می‌زد و با استفاده از شرکت‌های پوششی، منابع مالی خود را پول‌شویی می‌کرد.»
هدف قرار دادن بانک‌ها، صرافی‌ها و افرادی که این شبکه غیرقانونی را اداره و تسهیل می‌کنند از سوی آمریکا چنانچه در بیانیه منتشر شده آمده راهی روشن برای اعلام آن است که «هر کس به ایران برای دور زدن تحریم‌ها کمک کند، با پیامدهای جدی روبه‌رو خواهد شد.»
وزارت خارجه آمریکا اقدامات انجام شده از سوی وزارت خزانه‌داری این کشور را نشانی بر تداوم سیاست «فشار حداکثری» دولت «دونالد ترامپ» علیه ایران دانست. سیاستی که بر «قطع منابع مالی مورد استفاده حکومت برای تهدید ثبات منطقه، حمایت از تروریسم و تقویت توانمندی‌های نظامی‌اش» تاکید می‌کند.
@
VahidHeadline
پیش‌تر:
وزیر خرانه‌داری آمریکا روز جمعه گفت که ممکن است «امروز یا فردا» توافقی با ایران برای آتش‌بس و باز شدن تنگه هرمز منعقد شود.
اسکات بسنت در گفت‌وگو با شبکه «۱۲ نیوز» با اشاره به وضعیت وخیم اقتصادی در ایران گفت: «فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد توافقی برای برقراری یک آتش‌بس ۳۰ تا ۶۰ روزه خواهیم بود و تنگه [هرمز] باز خواهد شد. قیمت انرژی هم باید کاهش پیدا کند.»
او با تأکید بر این که ایالات متحده هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست یابد، گفت تحت تاثیر عملیات نظامی آمریکا و اعمال تحریم‌های شدید علیه تهران، «آنها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی مواجه‌اند و دیگر توان پرداخت حقوق نیروهای نظامی‌شان را ندارند».
بسنت همچنین درباره وضعیت زیرساخت‌های نظامی ایران گفت: «نیروی هوایی نابود شد، نیروی دریایی نابود شد و بخش بزرگی از موشک‌ها و مهم‌تر از آن، توان تولید موشک آنها از بین رفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#توافق_مکه
:
وزارت خارجه پاکستان در بیانیه‌ای اعلام کرد جمعه ۱۶ مرداد، پاکستان، ترکیه و عربستان سعودی، توافقنامه مشترک دفاعی امضا کردند.
توافق امضا شده تصریح می‌کند هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله علیه همه آنها تلقی خواهد شد.
در این بیانیه آمده است این امضای این توافق‌نامه «نشان‌دهنده تعهد سه کشور برای تقویت بیشتر امنیت جمعی آنها است.»
وزارت خارجه پاکستان همچنین در این بیانیه نوشت این توافق با هدف تقویت صلح، امنیت و ثبات در منطقه و فراتر از آن و برای دستیابی به آینده‌ای امن و با رفاه بیشتر تنظیم شده است.
همچنین رویترز به نقل از یک مقام ترکیه اعلام کرد «توافق دفاعی میان پاکستان، ترکیه و عربستان سعودی ماهیتی کاملا دفاعی دارد و هدف آن، ایجاد تعهد برای حمایت متقابل در زمینه دفاعی است.
این مقام به رویترز گفت: «این توافق علیه هیچ کشور یا طرف مشخصی تنظیم نشده و کشورهای دیگر منطقه نیز امکان پیوستن به آن را دارند.»
به گفته این مقام، این پیمان جایگزین یا لغوکننده هیچ‌یک از توافق‌های دوجانبه یا چندجانبه موجود میان کشورها نیست.
@
VahidOOnLine
ابراهیم رضایی، عضو كميسيون امنيت ملی و سياست خارجی مجلس شورای اسلامی، عربستان سعودی را به طور غیرمستقیم تهدید کرد که پیمان دفاعی مکه برای آنها امنیت به همراه نخواهد آورد.
رضایی در شبکه ایکس نوشت: «سعودی‌ها باید بدانند که توافق کاغذی با ترکیه و پاکستان برای آنها امنیت‌آور نیست، همان‌طور که سال‌ها شیردهی یکطرفه به آمریکایی‌ها برایشان امنیت نیاورد.»
او عربستان سعودی را به «گدایی امنیت» متهم کرده و به مقامات این کشور توصیه کرده به جای آن، سیاست‌هایشان را «اصلاح» کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=WDNCS73aZcX0g2MAxViJ_32AaP8u0ESfpe_zUt1SdK32kofoRNvtlg1DFNrHYXUKgrpV-I1h5z0VkSai7JW4mr1299YWEAZ73GJyoxg3M6W0xDkfyqSTNAUXUafZM45oL0zk3Fwn3N4PCn7wAj4LxNheIyYcYgYFPDYejvbMcDd5jDBjj9mOSBW8l5-_uKyejfgpcxoREW7VpIqNPsfBZGjfeTgP6cA8rxg_4pwEDpMOjpeLFquVUP2CCr5T7cRx-gUrJlvqvU1wncKjMpmjM4MyeFvk_OPO7xaLg4betqb1FwU_-xy99h1R-fY6HR8cKny1XotNZSk4pOcjkLIUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=WDNCS73aZcX0g2MAxViJ_32AaP8u0ESfpe_zUt1SdK32kofoRNvtlg1DFNrHYXUKgrpV-I1h5z0VkSai7JW4mr1299YWEAZ73GJyoxg3M6W0xDkfyqSTNAUXUafZM45oL0zk3Fwn3N4PCn7wAj4LxNheIyYcYgYFPDYejvbMcDd5jDBjj9mOSBW8l5-_uKyejfgpcxoREW7VpIqNPsfBZGjfeTgP6cA8rxg_4pwEDpMOjpeLFquVUP2CCr5T7cRx-gUrJlvqvU1wncKjMpmjM4MyeFvk_OPO7xaLg4betqb1FwU_-xy99h1R-fY6HR8cKny1XotNZSk4pOcjkLIUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین:
🔺
خبرنگار:
و آقای رئیس‌جمهور، جمهوری‌خواهان اکنون بحث زیادی درباره قدرت خرید و هزینه‌های زندگی دارند. پیام شما درباره این موضوع در آستانه انتخابات میان‌دوره‌ای چیست؟
🔻
ترامپ:
سؤال خوبی است، اما پاسخ آن تا حدی ساده است. من بالاترین قیمت‌های تاریخ را به ارث بردم. بدترین تورم تاریخ کشورمان را به ارث بردم و ما کار فوق‌العاده‌ای انجام داده‌ایم.
قیمت نفت اکنون به‌سرعت در حال کاهش است. اگر به اوضاع نگاه کنید، تا ۷۵ پایین آمده است.
وقتی آن اقدام بسیار مهم را در جمهوری اسلامی ایران آغاز کردم، اقدام بسیار مهمی بود؛ چون آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. در غیر این صورت، تمام جهان منفجر می‌شد. ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. مسئله فقط ما یا خاورمیانه نبود؛ برای تمام جهان فاجعه‌بار می‌شد. چاره دیگری نداشتیم.
قیمت بنزین در بسیاری از نقاط، مانند آیووا، به کمتر از دو دلار رسیده بود؛ قیمت‌هایی که مردم سال‌ها ندیده بودند: یک دلار و ۸۵ سنت، یک دلار و ۹۵ سنت. سه‌شنبه در یکی از توقف‌هایم در آیووا، در یک محل قیمت ۱٫۹۵ دلار و در محل دیگری ۱٫۸۵ دلار برای هر گالن بود.
بر اساس هرچه می‌بینم، به‌محض پایان جنگ، خیلی زود دوباره آن روزها را خواهیم دید. فکر می‌کنم جنگ به‌زودی پایان پیدا کند. تصور نمی‌کنم آن‌ها بتوانند مدت خیلی بیشتری ادامه بدهند. بله، بفرمایید.
🔺
خبرنگار:
آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
🔻
ترامپ:
نمی‌خواهم بگویم که توافق حاصل شده است. تنگه در حال حاضر تا حدودی باز است. می‌دانید، چیزی داریم که «محاصره» نامیده می‌شود و نیروی دریایی آمریکا آن را هدایت می‌کند؛ ما آن را کنترل می‌کنیم.
اکنون کنترل آن با ماست، اما آن‌ها همیشه می‌توانند به چیزی شلیک کنند یا مینی در آب بیندازند. حتی اگر فقط یک مین آن بیرون باشد، اوضاع را به هم می‌ریزد؛ چون مردم نمی‌خواهند کشتی‌های میلیارددلاری خود را وارد منطقه کنند و تصادفاً با مین برخورد کنند.
اما فکر می‌کنم عملکردمان بسیار خوب است. خودم در مذاکرات دخیل هستم و فکر می‌کنم اوضاع خوب پیش می‌رود. ممکن است توافق حاصل شود؛ ممکن است به‌زودی باشد. بله.
🔺
خبرنگار:
آقای رئیس‌جمهور، درباره مهمات؛ شما شب گذشته نوشتید که آمریکا مقدار عظیمی مهمات دارد و وجود هرگونه کمبود را رد کردید. در عین حال، یک درخواست بودجه تکمیلی ۲۱ میلیارد دلاری برای پرکردن مجدد ذخایر وجود دارد. اگر کمبودی نیست، چرا این درخواست همچنان مطرح است؟
🔻
ترامپ:
چون همیشه به مقدار بیشتری نیاز داریم. منظورم این است که مهمات بیشتری لازم داریم.
ببینید، دولت بایدن مقدار بسیار زیادی به اوکراین داد؛ رایگان، بدون دریافت هیچ پولی. میلیاردها و صدها میلیارد دلار.
خوشبختانه من در دوره خودم ذخایر بسیار زیادی ایجاد کرده بودم. نیروهای نظامی را بازسازی کردم و مقدار زیادی تجهیزات و مهمات نیز در اختیارشان گذاشتم.
از بعضی انواع مهمات بسیار قدرتمند، ذخیره‌ای نامحدود یا تقریباً نامحدود داریم. در مورد بعضی انواع دیگر، وضعیت کمی محدودتر است و هر روز محموله‌های تازه دریافت می‌کنیم.
همان‌طور که می‌دانید، شرکت‌های دفاعی ما اکنون بیش از هر زمان دیگری در تاریخ کارخانه می‌سازند. برای موشک‌های پاتریوت، تاماهاوک و همه‌چیز کارخانه می‌سازند.
در عین حال، انواعی از مهمات داریم که ممکن است به آن اندازه دقیق نباشند یا در آن سطح ممتاز قرار نگیرند. نمونه‌های ممتاز را هم داریم و این موضوع را بسیار دقیق زیر نظر گرفته‌ایم. اما بعضی از انواع مهمات ما بسیار قدرتمند و بسیار خوب‌اند و ذخیره‌ای نامحدود از آن‌ها داریم.
بنابراین در وضعیت بسیار خوبی هستیم. بااین‌حال، همیشه مهمات بیشتری می‌خواهیم و باید مقدار بیشتری داشته باشیم. ممکن است مسائل دیگری پیش بیاید و ممکن است هم پیش نیاید. امیدوارم هیچ مسئله دیگری پیش نیاید، اما ما در وضعیت بسیار خوبی قرار داریم. واقعاً مقادیر عظیمی مهمات داریم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 491K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGYFt__RB2zpmrCFSBytySvEkbcfFu7gH0C8FvkzXflFYZkkaGyMshEKyO3eeEe9pSoDbml7n5gaTawZ7jpAx6jvxj4AfyJLxqdOY9PxVE0FDpgRNvwtMRMrLKe-lLqeFPbZehHh1-LTKn7ZPdkWoYqcNFl-0FOnQqwWpQhgfWo2qoDi1GgIM-5GsEco7w3_slcKgl7374UH82cE1K0H8sWIinNF-ISvElqQW7Dy2DPGsU_1tMYWNZ7PfjZF-20QYjCoPlenEURPSy1hRl5Pcyu2Ug35Sv9z0c2QfWHunLBr0MSb_yY9YKvCxXzibEcWD7j5MnfGM1qpGdEFWv4T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 498K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwNWFZuP8PV6b601VUo82asEVkzNyPvI1wPP9H2qvJWDYIWtssE1ldt_x5v_AAr0_wbHHzYMqVifMNCPgwkVlTBR0Y4OQ3NYxk22JDuEKAzskyfnmsbd6lAvNLjHTyCecHdN4oI_PVw1IBJPuxkW9vX6Se-O3IHvRRWCJOCa-qpcefgVrD-DlfeIejycxiDK16bh6szFI-6KR3RPNkn8xVzfWzfD5yaKiqqsmUr4heZE5ZEPfC42qA2LzNLKs5hN5suQSEwzcP_vsjGJbXzWFtExnS83FYCbwg8ktoB1orUVDBqvrX_BbahsYy0e4aBds3EbdOj3zN_7lB7legrh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
همین الان دو صدای بد انفجار شنیده شد قشم
سلام ساعت ۲۱ و ۴۳
قشم دو انفجار نزدیک شهر
سلام وحید جان الان قشم صدای دو انفجار بد اومد
صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن
وحید قشم رو زدنننننننن [لطفا صداها رو تفسیر نکنید]
۴ تا انفجاررررر
قشم هم اکننون سه انفجار
ساعت ۲۱:۴۱ قشم
دوتا انفجار یکیش خیلی قوی تر بود، اسکله بهمن بود یا کشتی‌های نزدیک اسکله
بندرعباس ۲۱:۴۳ دو سه تا صدای انفجار [که لابد همون قشم بوده.]
همین الان صدای ۴ تا انفجار اومد قشم
دوتاش خیلی شدیدو نزدیک بود
دوتاش خیلی دور بود
سلام وحید جان ساعت ۹ و ۴۲ دقیقه قشم دوبار صدای انفجار اومد ،نمی‌دونم چی بود ،خونه لرزید
ساعت ۲۱:۴۰ صدای ۲ انفجار شدید شهر قشم درب و پنجره ها لرزید
سلام وحید جان صدا سه تا انفجار تو قشم اومد دوتا شدید بود یکی انگاری دور بود
🔄
منابع حکومتی:
🔹
معاون امنیتی استانداری هرمزگان،: تاکنون هیچ‌گونه اصابت یا حادثه‌ای در جزیرۀ قشم و شهر بندرعباس گزارش نشده است.
🔹
بررسی‌های لازم توسط دستگاه‌های مسئول برای شناسایی منشأ صدای شنیده‌شده درحال انجام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/77764" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CLF7KE1semUtBkZTTUpnyax2Y9vSnzASW_st9hlyDi7ZEX2t6Xjt3bcNculNknJORG8VZdfDuD0EnxAG4eFzuaV3kE4lHjLcE3RL1AOoDT4V7zfJm-wi_3Y_uu0fgozctzTH1R79Nt-BIY9E08AQv0jAYtPCy2Ok2QHIpsXjRex5dbqxkYNoWMRg0oO4cvjZwlyZSDaViwkiMSbGFXX38macwLIFrw6XTMR9hnR07o7EXnwg30ejFZYtn3_cbls3J0LXen0XlAX3nfGdzsRt6xsMYKul8f0wv9fVf-Atu5IojiiKNtevjudcmS6uUDoftEgisWd5s62Vmb8gGxltuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اخبار جعلی، طبق معمول، در حال انتشار شایعاتی دروغین و کاملاً بی‌اساس است. من از عملکرد پیت هگست به‌شدت راضی هستم. همه‌چیز فوق‌العاده بوده است؛ از جمله حمله ما به ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد نیکلاس مادورو، یکی از بدترین جنایتکاران در سراسر جهان، را به دست عدالت بسپاریم!
همین‌طور اوضاع ایران، که برای هرگز اجازه ندادن به آن برای دستیابی به سلاح هسته‌ای به‌شدت درهم کوبیده شده، بسیار خوب پیش می‌رود! پیت در میان نیروهای نظامی از احترام بسیار بالایی برخوردار است و اصلاحات عظیمی انجام داده؛ از جمله برچیدن سیاست‌های تنوع، برابری و شمول (DEI) و افزایش جذب نیرو به سطوحی تاریخی.
این شایعه را «واشنگتن کام‌پوست» ــ یکی از بدترین رسانه‌های این حرفه ــ به راه انداخت، آن هم با وجود اینکه به آن‌ها گفته بودیم گزارششان کاملاً دروغ است. در واقع، من واقعاً معتقدم این «گزارش‌گری» جعلی آن‌ها خیانت‌آمیز است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 474K · <a href="https://t.me/VahidOnline/77763" target="_blank">📅 20:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fCX_u-v2C_gvc8iFQjDPZYUSS3-puF6RDuLe3bwcjYcKCCnsgpMAjds5SphU9n_qUOr4dSqkruFQjineq-WIDytz6xvZQLb1-alucKDuli4ERsPylqq7jdnmlechFHMkWQxNNUHQuiFnQj2TrubDbCtBLtwVt0GgerGn9ZX_TyoxDm-k6qAmei1gUiCWKIuqQDq8BxD_Zdu_ajqispyHvNg8Hsu9qXQhpbQdH-ib1l5C5_YzJ2ZsUrh7nc5a6icsWO1DCqodYc9KWRg0DBCpKIvq-SxIEal6TJafrDTY-N09IiRYTwdusZ_zZu0jWUjS5hKhIStL_q-9wm6_lqebNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
ایالات متحده مقادیر عظیمی «مهمات»، به‌ویژه از برخی انواع خاص، در اختیار دارد.
افزون بر این، هر مقدار که نیاز باشد، حجم زیادی مهمات تولید و به ایالات متحده ارسال می‌شود.
شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات تولیدی در تاریخ کشور ما هستند.
کسانی که این اظهارات خیانت‌بار را درز داده‌اند، تحت تعقیب قرار دارند.
برای آن‌ها درخواست محکومیت‌های طولانی‌مدت زندان خواهد شد!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/77762" target="_blank">📅 09:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HlKTXPpFCDoqM4EKf7B4lceMx3DFpvksgYG8N9uIuIsDRvuKkQedhzU8F74y-Ffc9yRtywkdXS7hFWU1TQ_Mwi6q41329Qg6rKWCHHNspXNeIaA2RXddwx_yWwGo_d1A5AXK2m_VK9I4iGadZoKVA0e2e9CZTPhxop7Mygh2AmkGscI7fndBgP4C7GFGyL15mtPzunauJo__sqSuOrcbYEqXJvjrCSFoYXmucfx9ujQTTPR71oZJ3mIajvhS80iSWFkhaq01o6UbnbwFM7Qk5j0gUbisYGORDaVmjwssTqDHlrheVIp_6UbjqR8dk8CHpCQ9rdc9JE-7JEZpJlDjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن پست
:
درگیری ترامپ و هگست در کمپ دیوید بر سر نگرانی‌ها از کاهش ذخایر موشکی در جنگ ایران
ترجمه ماشین:
در نشست این آخر هفته در کمپ دیوید، رئیس‌جمهور ترامپ از پیت هگست، وزیر دفاع، درباره کمبود شدید مهمات توضیح خواست.
به گفته دو فرد آگاه از این گفت‌وگو به روزنامه واشنگتن‌پست، سرخوردگی دونالد ترامپ، رئیس‌جمهور آمریکا، از جنگ ایران هفته گذشته در کمپ دیوید فوران کرد؛ جایی که او از پیت هگست، وزیر دفاع، خواست توضیح دهد چرا ظاهراً درباره کمبود شدید مهمات ــ که اکنون گزینه‌های نظامی در برابر ایران را محدود می‌کند ــ گمراه شده است.
این رویارویی روز جمعه و در حاشیه نشست کابینه ترامپ در کمپ دیوید رخ داد. به گفته هر دو فرد آگاه از گفت‌وگو، ترامپ با عصبانیت به هگست گفت تصور می‌کرده مشکل مهمات «حل شده است». این افراد نیز مانند دیگران، به‌دلیل ترس از تلافی‌جویی، به شرط ناشناس‌ماندن صحبت کردند.
به گفته یکی از منابع، کمبودها، به‌ویژه در زمینه موشک‌های هدایت‌شونده دوربرد و موشک‌های رهگیر پدافند هوایی، از دلایلی بوده است که ترامپ در روزهای اخیر از اجرای حملات گسترده‌تر علیه ایران عقب‌نشینی کرده است.
کارولین لیویت، سخنگوی کاخ سفید، در پاسخ به پرسش‌های واشنگتن‌پست گفت: «این خبر صددرصد جعلی است. واقعاً هرگز چنین اتفاقی نیفتاده است. رئیس‌جمهور ترامپ نیز نهایت اعتماد را به وزیر هگست دارد.»
متن کامل فارسی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77761" target="_blank">📅 08:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=KMPAjbnyOefRgZeuIFemHRR-2DjtFebxUkDXnt1FheeDJiQbxWbK6Q3R0LZP_uxU9lFrmvASOdKtGwdW8cwinlEfhsuKSdd_be9MqoW9LikbsLgKrnDxtiXetl5s6c4V7uuJxvC5OD4YZf9gvit2AaoRHjA2L9Zyg_Uxn9a_KZ7XjciEsoXlqh8vQVhpX4exyMY8krxzt54vXGFaVuegydqpO47aEqBLQJwQ4Uqb7HZ-AOPsZPVlivFpb3nihlCgLyNMutG0QLTSW8qGSmwmKKYfAhUuy9WEC-jnqON9gnqYssHMucquo1X-_LwwmkTsuoxizxMM9A1kRzo8X4Jiyg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=KMPAjbnyOefRgZeuIFemHRR-2DjtFebxUkDXnt1FheeDJiQbxWbK6Q3R0LZP_uxU9lFrmvASOdKtGwdW8cwinlEfhsuKSdd_be9MqoW9LikbsLgKrnDxtiXetl5s6c4V7uuJxvC5OD4YZf9gvit2AaoRHjA2L9Zyg_Uxn9a_KZ7XjciEsoXlqh8vQVhpX4exyMY8krxzt54vXGFaVuegydqpO47aEqBLQJwQ4Uqb7HZ-AOPsZPVlivFpb3nihlCgLyNMutG0QLTSW8qGSmwmKKYfAhUuy9WEC-jnqON9gnqYssHMucquo1X-_LwwmkTsuoxizxMM9A1kRzo8X4Jiyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش مربوط به ایران،
تشخیص و ترجمه ماشین:
در ونزوئلا خیلی خوب پیش می‌رویم.
نفت زیادی از ونزوئلا می‌گیریم و رابطه‌مان با آن‌ها هم بسیار خوب است.
میلیاردها و میلیاردها بشکه نفت از ونزوئلا خارج می‌شود. ونزوئلا یکی از غنی‌ترین نقاط جهان از نظر نفت است.
و همان‌طور که می‌دانید، آن یک جنگ ۴۸ دقیقه‌ای بود؛ ۴۸ دقیقه طول کشید.
و هزینه جنگ را با آنچه از آنجا بیرون آورده‌ایم، چندین و چند و چند برابر جبران کرده‌ایم.
قبلاً کجا چنین چیزی شنیده‌اید؟ هیچ‌جا نشنیده‌اید.
همان روش قدیمی است، درست است؟ همان روش قدیمی.
غنائم از آنِ فاتح است، درست است؟
و ضمناً همین کار را در جمهوری اسلامی «دوست‌داشتنی» ایران هم انجام می‌دهیم.
داریم حسابی می‌کوبیم‌شان.
ترجیح می‌دهم توافقی انجام شود، چون نمی‌خواهم مردم را بکشم. نمی‌خواهم مردم را بکشم.
اما بالاخره در مقطعی قرار است... ما... ما برای بزرگ‌ترین حمله در میان همه حملات آماده شده بودیم و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
اما کاملاً آماده بزرگ‌ترین حمله از زمان جنگ جهانی دوم بودیم.
آن‌ها با من تماس گرفتند و گفتند: «لطفاً این کار را نکنید. بیایید گفت‌وگو کنیم.»
بعد می‌گویند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟ رسانه‌های جعلی می‌دانند که آن‌ها چنین چیزی گفتند.
اما در حال گفت‌وگو هستیم. ببینیم چه اتفاقی می‌افتد.
ولی آن‌ها برای ما احترام قائل‌اند. به ما احترام می‌گذارند.
۴۷ سال گذشته است؛ ولی در واقع ۵۰ سال شده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال شده است.
هیچ رئیس‌جمهور دیگری کاری را که باید مدت‌ها پیش انجام می‌شد، انجام نداده است؛ زیرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد. نمی‌تواند داشته باشد.
---
و به‌محض اینکه این وضعیت با ایران پایان یابد، قیمت نفت به‌شدت سقوط خواهد کرد. قیمت بنزین هم پایین خواهد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUhLuzctF5-uPVKKHR472KNCUf2orkbgX3WbTDgprDZj_NEM6EdPpq8IFDUdLmlfpQGTVPrnQDzV1aRvTywHP8X3ir9J6KTlA9GwW6sLMvc3ABrXJLOao5UkD1Cdpu4ZZEX5n9kzw1ywlN7wgIEt-YQeLOrYynsC09NYeOZfj06OUgEojgprrCLjrUCa-FCehjWXSpbyfroJV-m_WLm66MJzfCcMV1u4_MpSiz27Vyhmr-J3ifi78xwftejKG7X788i8w2U38mp2kvmBByt_CTMEsNKdDRXIO9f4IQMGMGMgTlBRCZFmeHvcPuvUfW2RdXauAIPXJgSxdWu-iw6wvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s92sNDEAP1_SkJdVrPryDRjlavdr8_lWO3jg6OF-cGbP2Ct7plCDRxmnFoBguC9lRp9RXbZBaOJ5NLNiwSwjWp2FO3zp76o9WnHr9a79Yc0Zjb6tZK28kpVJNT2IYpxtHxeGpyJiBkVlrD-rsXyOmXEDrxRdw-D8k04chJl-BZxNf17Z5Umg4zWnJojeC7Nn3URwVocGrqTTiTCKZe_nNclqeGoYz7Qkzhs8HIfXxbMCj0jhk5OzZxHUp4UiG37756qSY6KNBvxw0rvKuVeQaMyHjvzGh7lk33Ua8nnSTTBci8l4qCK7uDFNZyPRnaRdfvyjROp-dCajsn-91SsbCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=sO4aeIKaSOc0XePk9wWW0PMTDTyiJyZ5NW74ur1cEhwxAJkLypqO7ofHr2UxV-E9Knvpjb6ZuKCSY1N99DNJW0xD2Ix9zBmRqmD0Fz5uNK5OFHHZqw125fcv4kDwf5e3hOh69qjRelyqShZFx0U_xOVpcdo-dL-g-nfduvbwkuSFo8Dxwd9OwtCsmp1k-5eDSWuBCH-7_csA931VW6CS9VBI8EF5RSYVf14eHYFl8bSkRE45zKMr_on5Id_I_jeb9y7dmoHF6j968lntRyoVL57DavzEmP00L2_gamkeh5TThBDdMv9gnVH7mFhhKZ4A6G7bhffMbx0n2M69ElpEFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=sO4aeIKaSOc0XePk9wWW0PMTDTyiJyZ5NW74ur1cEhwxAJkLypqO7ofHr2UxV-E9Knvpjb6ZuKCSY1N99DNJW0xD2Ix9zBmRqmD0Fz5uNK5OFHHZqw125fcv4kDwf5e3hOh69qjRelyqShZFx0U_xOVpcdo-dL-g-nfduvbwkuSFo8Dxwd9OwtCsmp1k-5eDSWuBCH-7_csA931VW6CS9VBI8EF5RSYVf14eHYFl8bSkRE45zKMr_on5Id_I_jeb9y7dmoHF6j968lntRyoVL57DavzEmP00L2_gamkeh5TThBDdMv9gnVH7mFhhKZ4A6G7bhffMbx0n2M69ElpEFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل روز چهارشنبه ۱۴ مردادماه با انتشار پیامی ویدیویی اعلام کرد این کشور با طرح پیشنهادی آمریکا برای خلع سلاح حماس و مدیریت غزه موافق نیست.
نتانیاهو در این پیام گفت: ««رئیس جمهوری ترامپ و تیمش فکر می‌کنند می‌توانند حماس را به خلع سلاح و غیرنظامی کردن غزه وادار کنند. ما در حال بررسی این موضوع هستیم. آنها پیش‌نویسی برای ما فرستادند، ما موافق نبودیم، این پیش‌نویس ما نیست؛ ما نظرات خود را ارسال کردیم.»
حماس هفته گذشته اعلام کرد به شرط خروج اسرائیل از نوار غزه، خود را خلع سلاح می‌کند. با وجود واکنش مثبت ترامپ، اسرائیل همچنان با این پیشنهاد حماس مخالف است و چند وزیر کابینه ائتلافی، پیشاپیش تاکید کرده‌اند که ارتش این کشور از غزه خارج نخواهد شد.
@
VahidOOnLine
نخست‌وزیر اسرائیل در سخنرانی خود در خاکسپاری رسمی پدربزرگ و مادربزرگ تئودور هرتسل، با اشاره به تحولات جاری تاکید کرد که این کشور در میان رویدادهای حساس نظامی و سیاسی قرار دارد.
بنیامین نتانیاهو با تمجید از رئیس‌جمهوری آمریکا گفت: «می‌خواهم این موضوع را روشن کنم؛ رئیس‌جمهوری ترامپ بزرگ‌ترین دوست ما و بزرگ‌ترین دوستی است که تا کنون در کاخ سفید داشته‌ایم و ایالات متحده نیز بزرگ‌ترین متحد ماست.»
با این حال، نخست‌وزیر اسرائیل با تاکید بر حفظ منافع بنیادین تل‌آویو افزود: «اما موجودیت اسرائیل — چه با توافق و چه بدون توافق — قابل مذاکره نیست. من مصمم هستم که هر آنچه برای تضمین امنیت و آینده‌مان لازم است را انجام دهیم.»
اسرائیل در حال حاضر در میانه گفتگوها برای دو توافق قرار دارد: توافق با لبنان برای خروج تدریجی نیروهایش از جنوب این کشور و توافق صلح غزه برای واگذاری مدیریت این مناطق به هیات صلح مطابق طرح ترامپ.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز چهارشنبه ۱۴ مرداد، در جریان بازدید از مرکز جذب سربازان جدید با تاکید بر اتحاد داخلی این کشور پس از حوادث هفتم اکتبر، تصریح کرد که تل‌آویو اجازه تشکیل کشور مستقل فلسطینی را نخواهد داد.
نتانیاهو با اشاره به این موضوع گفت: «ما در اینجا یک دولت تروریستی فلسطینی تاسیس نخواهیم کرد؛ دولتی که می‌دانیم قصد نابودی کشور-ملت یهود را دارد.»
نخست‌وزیر اسرائیل در ادامه افزود طرف مقابل در پی نابودی اسرائیل است، چرا که این کشور ترویج‌کننده ارزش‌های پیشرفت، دموکراسی و آزادی است؛ ارزش‌هایی که به گفته او، مورد نفرت «دشمنان بربر» قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGnzqo3HAJYaQlQfluAewyMk-rZI1UPM_U7Dw7_VspvMnmfYj4DV0AW0eZvgXiNOgrLJi7Vws-qgp_ND9qy_C1XRlormUrLzdlcgaTiHCOOq3DZiWrtgAXtuIjgSFnVPQfYHlaF_OjT5a4HHrFnTH9BCrBmm687AC8Pcp2f8yWaq9fU4AQsIR7m7opvAeY0qA9T-BWwsadTfJMVsnl2NZYUfZ2xQcASFnjrck8zDY3jbmz4ejeOlLUUb6aMaczoV_B601f12Fp8SA1EJu9VHGhHu4zRGziyfSmR1gNo0k9VkV6KVGWjBOd8vLPTXM8ceRmaFZZVxxaJxzIK28qJ9xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2KXPsZ9OhfxSflp9iuSvodDMMffKhl3lUE3oHzv61dKCysFbufkWbDVPmnNbfCZFdeaWKXdbfrp7wMiBRIPB0ExaRjxHvPpnMv3_bVU8inlqLuxMs50GKgJ9hLQpCaG9B1lV5iu4JgpO5UJuov0NE_l7OLcZ77BlHQKkWtituycW6JCl5MYgdXGURPpbYCo9Wt2jRMksYxMkTQFtkAITX5fDeyKyAyubHvx6TzEfIThCMyBCGBMF0FfN3hwlgw24EFcZT1WRSCW0AwfgtwM6hYPV4MbKNhZW-Uv2BhGFzNFUKqIPLE9Du8lvIJsZow5CgvHg08qM2CBo88WK8HRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در واکنشی دوپهلو به تکذیب دفتر مجتبی خامنه‌ای، اعلام کرد این تکذیبیه را می‌پذیرد، اما ابراز امیدواری کرد پس از «تغییرات مهم آینده» این دفتر نیز همچنان پابرجا بماند.
این واکنش شامگاه سه‌شنبه ۱۳مرداد۱۴۰۵، در صفحه اینستاگرام دفتر خرازی منتشر شد.
در بیانیه دفتر او آمده است: «گرچه به احترام قائد شهید و نیز رهبر معظم حاضر، تکذیبیه روابط عمومی و دفتر نشر آثار را حدوثاً می‌پذیریم، ولی امیدواریم پس از تغییرات مهم آینده در حوزه دفاتر فوق، این تکذیبیه همچنان باقی بماند.»
در ادامه بیانیه آمده است: «خداوند ما را در صورت استقامت و صبر در راه اهل‌بیت و ولایت معظم فقیه یاری خواهد فرمود.»
فرستاده است.
دفتر مجتبی خامنه‌ای ساعاتی پیش از انتشار پاسخ خرازی، ادعای او درباره هشدار رهبر جمهوری اسلامی به مسعود پزشکیان بر سر استعفا را تکذیب کرده بود.
در بیانیه این دفتر، بدون نام‌بردن از خرازی، آمده بود: «مطلب منتشرشده در فضای مجازی که در آن فردی، ادعایی را درباره واکنش رهبر انقلاب اسلامی به نامه رییس‌جمهوری محترم مطرح کرده، از اساس کذب و خلاف واقع است.»
دفتر مجتبی خامنه‌ای انتشار این ادعا را «زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه» توصیف کرده بود.
یک روز پیش از انتشار این تکذیبیه، ویدیویی از سخنان خرازی در شبکه‌های اجتماعی منتشر شده بود. او در این ویدیو مدعی شده بود مسعود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده است.
خرازی همچنین گفته بود مجتبی خامنه‌ای در واکنش به این موضوع نوشته است: «یک بار دیگر پزشکیان استعفا کند، استعفایش را می‌پذیریم.»
او مدعی شده بود پس از این هشدار، پزشکیان و دیگر مقام‌های دولت از مطرح‌کردن دوباره استعفا عقب‌نشینی کرده‌اند.
@
VahidHeadline
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
