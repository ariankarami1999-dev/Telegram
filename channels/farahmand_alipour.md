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
<img src="https://cdn4.telesco.pe/file/T65xj10RbAQWdGrKZtScce2_0HoEKzNJfFbY22UMBvYAKNUb1IQaoH5zbAeUcof8Vbm1qG39ybgZxjM3dgxsMNhLwCayynaz88KrL8TUTFox-QhPyLGG1Z_FhpCa1LjZPeSoSvyIApm2k2vtOjprXeWlvdlv8xSdXl7EM_Es1OLGlU_IwKIBAyaKnriPJsvbx4T3P0uMBAvUX4_nlAS-o5BVx4h6z7PlS5z13kP97g2xRGnrUqIYF0X_EAKqEWxO3zmjgb9HXpi6y5vqB8lGtSIrFZiooMRgh0_m9l38yliZgVZYIsRAkRoVcYdHVNuNM09CcibSXEmlCrmAwxgQFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMeB-HsSjq2YMMHj5WyeZ6XnGy7ZmrVuSAOhAM4FBXmvPJ31JMCmlFSo_g-xT84MunDxCSgvEi0Xap3R8kzA1GscHwstWvFVfvFgdrp0tgI04lYEakY9Hyx78YJPAYOMAtRKl6740QQPJIbCHi_3D6-INOrirnBbbikTBWOW7Ygu2jqD8uVCp_tvljvTIAXdzYjpDjhgQp4GPvpKkx6d9PA5tdSRMb34ORI9dSHZWiu6e2aFEOElHp9tyON6o3YdabSABBgZNIbOFa2r0GRWTmD-NoUpWekg3GRcHIOGcZ9LYo_kBLuaNJadHtOVjSHSr5Ozh6ytlBufI3SM-gNK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=j4zXSEvR05j0TPU7puX0Vh9G_hHEgehH_HrluI4sCIgo6YynJhmQzYDbH57mUN4FaymZu4OrXNIjFh1rCDLMxYCefmZRSRg2LNQY-HcGarcgRYLJNp-RiEkeb9q4AN5NT05vNlT4bAlk5I2mghbPqZqpD_6vCyfOY-hVZWBmK5736xALM1zwiKj8mtRtzVgUr9yaA6w_r7V3csVbSHt0yiobVGRK5o5KJr8e8tjCkyLq6Sv_O2hWUM9hedHzYs-H7wj0ZNUHmLzAT3M8-BoOxU2SbZWnzz1zY96BYcfJ42BHSiCQwo3yv1Vwi8miyyhQddfdQLTGpPfFg3mPuK8XFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=j4zXSEvR05j0TPU7puX0Vh9G_hHEgehH_HrluI4sCIgo6YynJhmQzYDbH57mUN4FaymZu4OrXNIjFh1rCDLMxYCefmZRSRg2LNQY-HcGarcgRYLJNp-RiEkeb9q4AN5NT05vNlT4bAlk5I2mghbPqZqpD_6vCyfOY-hVZWBmK5736xALM1zwiKj8mtRtzVgUr9yaA6w_r7V3csVbSHt0yiobVGRK5o5KJr8e8tjCkyLq6Sv_O2hWUM9hedHzYs-H7wj0ZNUHmLzAT3M8-BoOxU2SbZWnzz1zY96BYcfJ42BHSiCQwo3yv1Vwi8miyyhQddfdQLTGpPfFg3mPuK8XFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkJ8CHRFBAWvEd2TAQAYZNpShabxRdJcaVbVVKakRuLNuHK2DedtIWLLwmYCixnkjt4-jSUWhFY2j9vPWKqWrK5Pvy46abVT16XsIYLcftttkK9SVPywPUeWvYSxvqatp8PmsXt6BDnj3mZIOe7iDjS0onR30hQ_0HAgDS2DHkoFI2JwWhUcvbPI6Q11MP2A9aUbWERdSbwd6P_m-h_nofwmtf8OA_rBFy-zIB_5YaRTOQO1NRkzogoCQ_Atc9CFk9RU5hbvZaPFYcwOVYJ2XdCypTFmLHRzXaaQuZYbnHDUSLvVSt0Ge5GwK1epHs-08HWUw690B0tBmBBkK7K5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTX7abO_HBWQHB5OHCn8fQ0fVF5Qt47vGKBs4RZ-ymc9Xv0K0QuIbbghgvxfHtzGWNJuRXDgQ3AFpJ_uZVZMndKziOMAWkDrw6vEBI83EWi9vH0nPHW5V2lhwLkbB82jiV0SZKtiw-R7ycJCQRGKa2Y1qFfJHmh7oFsqvks_oAwQE-U8LcZRohEvA32P6e_79MdC48q0pVHlklseHPmR6qN-anF14e5SCY9kmxxE2hUsjNcaLUbta1w4JWIcjw2LrPWombTlfStTNIndvcpF5_Ce2ZDzAA1eozhEg51-9exRYnkrkmWC-SbC4eLXDQY28whBgv0FcbmdkOhb-0ukWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8omnbdlXorNlxVYpRAuo6P7rfCZcbQPZEHGoSaLRJyF2ozz9KVqz81ERap1vzQBCNbgalcoj-SExDRR5549WKas3P4RArERIjYTC_u_DFcyu8jZDGyZOPtiuKDuDzzO0JyJrqPHIAGO7nrog8ak614KlurVqZV7fNgfPR__MlYjCdxMe-LoP4U1Gv-3q4HanIe0LbLsBnHtcw82KMIDop7Y2qgGiFBIicGrjWyJjSEZCVsqGiheHY5WQRvd4BTFlBE7g_RzkKIlCBawDF4FlXGbxToD6oXfW5n3t-I9IamhRrhRQw8RtM8EufMYhg8s1aMOkRPn2dqYFypSidPIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijEOeEETvZ-GNeuJElr77oI-Lwvk3-SY9nS83vxHkdCfr2BRgTQudXsrfPxneQhZwvKyROyidOnBgdyZ1n4FmC8k7rUK-jceWdiASxp5rq_MQa6BvwZIrezlZnPVJmjDuUgffd8QJOBrEL13k0d2OmPibQEOIK5kYWcpe0Qmj6TTFpZt5Rh_gFr18ZCByLffJ_O1KuMPvycWm0OmO0ayLdKjI3s8xf0yJCwE6uvESsy_43fHu0Zad72LQlgsZGFggPMOa-4A_2L8Q1-DOPi8yQSpX24_7yWf8bc501UKCh9UZy9DgkyT7COxgiYvj99Hcep8WvZ-IUMXa_UUeUyU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vknurSUj5MKClQsp4e9AqoBwUsqXu8sqRxI85EzmfpvHX0nkezi34cfC99d7CUYTRCL2nhK9xgmnSedZI6qPPqqbBUDfOBthbiHKjLlW2Kf-HjLXVTughig2xolNUhOiB2riv1H2jcmGRWg7sy_sFDC4exoPFmlpEz3IlCgpcYMk9ZAhEUBHb3DlJoV2W5YPC19FyvURheZy3rp3q8c2RJDBHzd7jPw6KBrVkx_bEL430DHCXg3pnd03thWphZo6qyDG3yZ6SBCPi-42sS6J8cfOFGTAgv_hn2AmlGh7EB6Rz_srLI2JMVwwhjbe8UqwpcM7djQvbde5Oh1nAjM1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIDPvvCBsjwjzytJq0K8TavZNpU8bC1pt0knmRzaJGx7dng290phOpqudGh8jeYaNsrY8qqjdBQGTNjott-pzjtcOJt2a4zJN1M8zZCTnrja3992PgC04oqkVZJ8XDqihSzAurqnfetKG_asgPPIn1v8b9ZxYr-DefXv7LZGtr4z9Kr_E5hLB7TtvYkqURaKSOn1Ye4Alf4ToYCO9EIlBhpB2iypOGOPNcSbDDv3xMAEvWfre64Md1ONOiftIr9ynFJvQrWy-5JNxPhF9JtZxbbxWOlHSE5wl44KC7bwd8iIF6YuN-AA-GNeOEj0UCseGU9s7kkHo0KGe3vGFfY9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quASYbv6tYX18IfIEwbFxG_cGUqpAF7cDfcAE9rpWj7yUNXQa1UlkeaaZM8FoqoiZmIGbx__swPb_zNHIQ_MxcZBPE_SbS5IZDH1kHTAHo60uNi6o9WxB1j71E_UkT1r2eDFpBP9jqY5eGoS5VVbHVzihmzJMe_2fsSMh5UDgwYqNusC4fdJqWSZWtvDg6VMLGhifUSphxGT3hAjNUHstBTSIdF0l_X1TJa9fOaJ688XnwjDvljrK7AL8aNAnx0D_eN35JK4hNRrAnzf93ON4w-toi4X7q3Qtb3BJnnz-KOO_y88JpYMQ3avxJT-McRggZoJR9w5eDAiehYZGhrquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7HI9uK1YjtkrwjXjriEZ9Mf78i3aug9DRxVxLzsw-GFEL8uVNypFJB_g2SAbbxkXEqA3ltCh5ztafiTIdX4ErvFUOGshSYDwwxgQ6jDk-iVK9qjq0xg0f-eeP9lC6WR_Sh_VgtP-9COjyi0vBh6bp7rur4eZSmvMJY1g7fiW0D51UDHAtWBC2E8yv-zdkOY55DPlv0vsV1VFHTfxnwMmJpTt1eF1mzEzt0A7Fs5S2ijC2eY5ZL1YHwkTEiXpEJqwU6mFwiOFVtLjOzjT9iwi-CFKi2mVRTAP5hr--TGIrXkaCsfPvJEk61Scut339kWtnmWcQ6qB9XQA6wmOTksSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=aaGoHH6Rq2v3CWph9pim5DplYvOSyEjVwU9rLxpwMl2oIMU6omO1cE5iGTyvEXyUP34hxSFjRQAHNdChW-Lunhcb-URw6d2-BeohWvJS9dQNtd8KCB7CqTaDhmtFa3_4z1TPKCZubdp-LOVQfgb_7ySMif0VQiWPWt3oY6FNZNgl2XmPAppVKY6stRVGHZ6C9B4ORgqA6u8pDw1V8Dr45chsSluIv8Fpezw-qTxNoF2hme36PpPjKyKnRu2YKH6vkG6LyFHiiJpaWHY1Hb0q64aqO_G75rFfcBNGfZyzo9El5KD17BbPFxaip9m3puP6zNRIDEM8MmqCSGDPQM4RwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=aaGoHH6Rq2v3CWph9pim5DplYvOSyEjVwU9rLxpwMl2oIMU6omO1cE5iGTyvEXyUP34hxSFjRQAHNdChW-Lunhcb-URw6d2-BeohWvJS9dQNtd8KCB7CqTaDhmtFa3_4z1TPKCZubdp-LOVQfgb_7ySMif0VQiWPWt3oY6FNZNgl2XmPAppVKY6stRVGHZ6C9B4ORgqA6u8pDw1V8Dr45chsSluIv8Fpezw-qTxNoF2hme36PpPjKyKnRu2YKH6vkG6LyFHiiJpaWHY1Hb0q64aqO_G75rFfcBNGfZyzo9El5KD17BbPFxaip9m3puP6zNRIDEM8MmqCSGDPQM4RwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfOhJJ3L64WqMYmjhcQ9Lg0jQaK5euGx3R2zeEOQPM2d5HCip8AAvEoHntjMy8C5EhNUWrjdCM-H4RZIsdRYjNdGAH4AKNuxxEm5qvOQcrFx00hexwYDjREajjfZByuvGMZD7lmWwx3n3hmjR3OdVqwv3blKDTZ_H5VD0mCmy_hLv4hdR2ZeGx_gE1l-iyXZxcFrsXTjzIvoHY8xXfM8xyqaGFOKGnZGjpBcMuAqXrU8M_PtEJnTHKC04tUrHsOxYoozvmh2NFuyVnQDcz8TMBk1TAyNmy47BMhHuVplKJ-bQ-keLWP57J1Mj99Y1DVh1EeF28Oz8w8xe2lZAHLpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOgnwp9-y6QfwIcnG5ruu3oz4_V3oRNC3otKb5Cn74U7Cu2j6HEC40soU4G7DjjqOPyvXhdRcbKA6vPznshqtsq8kgRpVcaY5iBKoYv0kUXrvMg_EoJzdYfL5QORBvaxMTYla4pkcUr_HB4u1597CZIdzn7IBOfGCHGBvTE1Q85iGEgUCaPdQbshrZRBBoV20ZRdqfS8KwREBRJuaK2RJmgtOLQqNI_dE4tCo76R3efUDv87xvqYdw2yG_1BxVN3w7hSqzV8I53sI33kuulB6N5VWVsyLB_MbBvsmu3PX831nAEdi7ydLoterNxUnrJ-6esuqY9cBKGOcXQTwP15pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGZ97tYdgD99wlPwnkHb-Hc2eSY92VKF3bpYJHjiDJ2SJ7ZxSRVmPJRDZ7jMtkt58sqgwxRT3iMRPICiyHt8mNmVD7BL2wjvEfvYcEwJ-pt5VEtomE6UGTIF8Uwt9Za1fpraLbq7dxNc3EqojY2KOHzniFWq0Hf08qgPvnjNF0pP-IxO_D-er492Ma7KtAF8XctEMtHq5Si5JQ6TPhJz3hKo7WmegMjWg7MLIop6zI-WclU9yd2HA_-thbXZbDm_ABAekNe4mJGN8PuOY6os1mPhtkTAIZ0TrqSIblhWc6RqipUsfmztk9yUFdOBzjvEQHC5MfsdBEjmg7T1dDTLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbqmuRfN1Hhxku8H9K1weFnOFU7nc4lH6BodDFmFbAudX5vxqmbrUJfTp5w_rhvvJATdZ4wq_Vf3tEdnlI15J7lycehDJNObCYLnWT82k2L7VgqT6Z_G_X7BB0L2dyjUEWt2XdMpWHjBf6s5KpcNdu-cIWLXrXlG3dfeW0bEGgmB3rPKljUdzj3YfA03-dNmTUCBAv_5EgdePa17T5NRB-mNwIcqF2FC46f82GRyI2437YaxeWqqmRCCZoeaYuRjxlnAGeYhMF-yvPJ6MUrf_0XdAeS5bswE5KRmpKjrg5VXPc5bjhZS5PNJHn_aKzpTA-U3avTUS4Spll6q7507Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLI3jp9QmoQAwaIiumv3kLADlTLaPN84fQHauJyzUPKUbPpGO5zEy_5Sn-72xHHeeJfKrJQ9XuGfb8_asocLjlwZwg5cgYv3FTjX8kOkKLwOdm_uMjZyWpcS8CFOrnk2hfdUkPfsJ8ADQaQv7nYBFCyU2g3vCqVmjsbTbrSfiKyQpVJzgfTEZUEEfwmRdZe9XoNfTpfujD278JDP7Pptv8YOVnhS7278bS9ViUkdbN-fDnjMi3UAby20qsulUMDAwpVFg67B_viMzfVAfGM6CtlmT52ZV4XoSAWIeqoD14mZwVVf4nUPQENQOXTJbBH2Kj2JstSb6NqVf_aJpaui0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=ip-Bvmsj_870dfbMJOo99zX8h4bv7USQ0NqAJ_fJ_gPh4xZmZ5mZF7m7DWBL2d09gTwppvedmfX4vIV7rI6aQkUT8uA2kUfaI-ngTIHO9SgUGuFmF1AdtpzstjFzaDqzrQ1oyVuJlzxF7rc-T8qL0d7YM13OodmGjYNcwicz-J2gFTnbCdRMn_RqGtfLIlKS0OPRcCcQ9EV8USBzNgr--bW4tGwGHXNt4z8P1yo_-CNv5mdoxcgA6lph9s8-eg4WHiNUW5CWVbmFYXPBC_pGt_BZF86cWdk5yuB0I0Yza3Kxzc1c5ub6tfvfg_A0z4TCXJFiYQjikH5C0S-w_JnPsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=ip-Bvmsj_870dfbMJOo99zX8h4bv7USQ0NqAJ_fJ_gPh4xZmZ5mZF7m7DWBL2d09gTwppvedmfX4vIV7rI6aQkUT8uA2kUfaI-ngTIHO9SgUGuFmF1AdtpzstjFzaDqzrQ1oyVuJlzxF7rc-T8qL0d7YM13OodmGjYNcwicz-J2gFTnbCdRMn_RqGtfLIlKS0OPRcCcQ9EV8USBzNgr--bW4tGwGHXNt4z8P1yo_-CNv5mdoxcgA6lph9s8-eg4WHiNUW5CWVbmFYXPBC_pGt_BZF86cWdk5yuB0I0Yza3Kxzc1c5ub6tfvfg_A0z4TCXJFiYQjikH5C0S-w_JnPsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb6j7852hn-PF_A_zjI0fUWAEYAsIb36VZUDkfOLzYrDWR2Zu5ceASdeTyQNBlmbdX_W1-gGaGLFb9ReueaBt2qqAp1puByLXa_Rm5F4OS3bkB88RGCJZ1xj9wHw-_Fg5rBg6q-S0wP3njMYDv1GMgsJjytYtRrVm39crVkefWxY_bxfMQiE5F3e_BP2Fg1-JKHUcvcxdlkvV5Abn5adY7PRf1rqBmdOeJIVz7zUBk4cXfVWw9-HglICVZ36XFiPy41GeKvajc6tHpdVtv4uHyH4lWRJkwPLLKsprYd0v-xEKgApK5xhaWCt7AseymNIbt1dZVtBaH2hSQi2jzSLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=pTMxMq8hkLfaJNYPts4oxxD2RcaiKrsTrpraWPdNqSjjcCF9jhZEjKxgIfb1Z49mkKEKsm2O5WLtPOwo5iJOI6JL30HTSNNu29FLSBd0BPon4MCkllvgOjZzEJ6OXlVsskDySfWdb80Z45T9MLtfY7EgJkafiA5RqSEJam-fk4Zj44ZVFGf4IsRXQ-8t5iDpc0NKiLSKDVMsi-LubYrIl68wN0YYGirkVqIYMDI9IEOcWOC3H6BJn8UJJNkhq9EHcXvnuici2L56FO_SAXeAEYfxQKFCzTPvSmUydHQxnXO2d2RGT536QJIZG_T-Hj-ogSBymFm5NX2Gd6ZRsp5x_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=pTMxMq8hkLfaJNYPts4oxxD2RcaiKrsTrpraWPdNqSjjcCF9jhZEjKxgIfb1Z49mkKEKsm2O5WLtPOwo5iJOI6JL30HTSNNu29FLSBd0BPon4MCkllvgOjZzEJ6OXlVsskDySfWdb80Z45T9MLtfY7EgJkafiA5RqSEJam-fk4Zj44ZVFGf4IsRXQ-8t5iDpc0NKiLSKDVMsi-LubYrIl68wN0YYGirkVqIYMDI9IEOcWOC3H6BJn8UJJNkhq9EHcXvnuici2L56FO_SAXeAEYfxQKFCzTPvSmUydHQxnXO2d2RGT536QJIZG_T-Hj-ogSBymFm5NX2Gd6ZRsp5x_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=Wj0PEcLKe1xnS8Er6NXgim4L1S354_V5_A72D8zOicKi8lvFOV7Ktj_Ffuns-RLPu1Js1-EwXHI0rqo7U2zmW-CH0N8J9oAtiGeNj6ok-7ALsu7PzeE6F26uJOy4EdM5TmN_LOZnuulFgqqJE02WDbsvXEd8yK-F4_UXiFzg4hgMQbs0JKw0I_poRlbrteirJA4JU5O18GS9P-Gycl1bGLe6hHQy4KXK1RJJ3LeNGISGtdbe-IChg12NeKkj7nmj5EJARofCc83d54f1mZqFZFBnVLpNCHsgpWwpxEnzZXc0CwLaV_0yJrHS5ELci73rQDwPVozuFPY-ZPrzVgM8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=Wj0PEcLKe1xnS8Er6NXgim4L1S354_V5_A72D8zOicKi8lvFOV7Ktj_Ffuns-RLPu1Js1-EwXHI0rqo7U2zmW-CH0N8J9oAtiGeNj6ok-7ALsu7PzeE6F26uJOy4EdM5TmN_LOZnuulFgqqJE02WDbsvXEd8yK-F4_UXiFzg4hgMQbs0JKw0I_poRlbrteirJA4JU5O18GS9P-Gycl1bGLe6hHQy4KXK1RJJ3LeNGISGtdbe-IChg12NeKkj7nmj5EJARofCc83d54f1mZqFZFBnVLpNCHsgpWwpxEnzZXc0CwLaV_0yJrHS5ELci73rQDwPVozuFPY-ZPrzVgM8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCo95hGeeBPG8ARYZXPyM0CVo7_o7IohbyJVQCfBr8ALY-F64Jkv3sNXNrLqOkajmKJ-htF0DjTWJSrWoqN15dtCO2lHQPyzf10C7BymzrlYNbSMKkxrTvehBxrMQ0WCsjW21E9woyr9ozggx0WLYtmT4C_A90Zfz3oEjcmXAcBwKNTWHF5pTGUuvZndbokaUXiSDGRV2HomyFCBTXbWC6f4nUn1PZpMGhykSsWYFibBHT-AjkGA-_3ch3FNqqljFtNiRkwbVfwgE3hkWjN4XbLRLqCWJYdG-ldYQsvh42QgoGFAYHVy45VfCRUW0TO_kcnjq0nIA_QPoHLGEKbx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VimpCClj_UP4oZ22EbqQATUqqYJmhxq0QjiVfGwFUPEWaBL1rT8ByUEzy3Joe5xqffShMc38cxHD_VpkjXg7O8vmYHKco9F1YCSLhV_6JUVV_11bZm8ltXh7e8gzFTZTxNowYZb0Otdh12fpd96m7OvwY0zefpne5kACYr7KvED1iY4l0206Sh6WBny4_TLEMt4zNRTN8L-DZYFSOD4YY5cUpnxhIkECR0iisNbvTsHENo3icQq7XOm7EDffRXy5946FEuwBDnZ41lyUEiB9E1kT_y77Uih6aXXqd7pnf4ZWgzRvGidHIim91DqyEoPukiVWAqcY2caNpNIFIhodqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=RRpSwAFWtwqvxSff8JHxsRQxdLZG2wuBvcDwgn_38wifh2cnSnh0KZfVA2IN8VN_4vtcHkXj6fflyovtK73yOSzvXvvX57NuRWOY92-RI-KZ6QuB7yIXehTM6IKV5DGJtiad_4WNdGLB-1IOJJ0rgY5CzoH-Fex2LKozQ7fyx0Usjm2ABiCFDwiCTAvyAru-S-Gfqqwq_5yLv7779xUqQ5dlcANriI9yXO2vuocRCUML2CAbdHby-fCgTAxC1k4Aj2sZ_rlmlQcTFSW45l6Ou9UQrjsrws65oUvPqqtKMsDJWODovBTw02qSLUDGARs-Mh_t1_RLDDrVwXdMCdY_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=RRpSwAFWtwqvxSff8JHxsRQxdLZG2wuBvcDwgn_38wifh2cnSnh0KZfVA2IN8VN_4vtcHkXj6fflyovtK73yOSzvXvvX57NuRWOY92-RI-KZ6QuB7yIXehTM6IKV5DGJtiad_4WNdGLB-1IOJJ0rgY5CzoH-Fex2LKozQ7fyx0Usjm2ABiCFDwiCTAvyAru-S-Gfqqwq_5yLv7779xUqQ5dlcANriI9yXO2vuocRCUML2CAbdHby-fCgTAxC1k4Aj2sZ_rlmlQcTFSW45l6Ou9UQrjsrws65oUvPqqtKMsDJWODovBTw02qSLUDGARs-Mh_t1_RLDDrVwXdMCdY_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6yd4VbOE6ZrsLlCxkyXSkbeyXr0MoTn3bstEY8QVXCitSiHS2S_JYmp5ytmm0lK8K4WmBw_YO7-jEHCMR0tCtB1MhBTUWlzzmG8LN_HN-3MOD8jveDfcslzcIGaba91S_-WZKyj4tYYgjzN7V02elnG9dTWkj-x_3a3z9_Jl_U_CqzdvrblnMbWW6EyQX2H28ddgH60btzIOJHyggj6B27zjXZxzPP0F35F7UeDk8NUYk8BIC1o1bJQfkph5DGdX7JWE1oiFiViDRoLAQrLOfpXkQ443GtcdIR8WncrrLrL1EYkHg8Vm2ZUESAXpylndI842XGijRmDffDdDGgRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPbPKSpvenBXw8st6roIbOaO8jAphbhM543mPGeXCBDLjNmHAKyO6ftWqW50TqKqGoShbOReK1Hym0CqVWwxRwe0I2ZP9dmrBgwUTHPNmO-VaZDQf9_MN_YnJIcJprdcQbbH0XWERDwXHBQkIouV3Uieba40NJl9G8Wn4zvQ7aCZZjiUN9oVgRspxxrC9lelH9xY3vMziefX1wzN_0h5UySccMhhtc8UTs4A5q8mZxdkseNrHJHuoOjqzaiGkUcp3MTYyt1ImXSTc08chGrA34HAUEf_od581O6Uj5xgjMQrJyBtC_0kL8qffZuobAdiVkYP7rNdWd_R6FoXU1M2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9ImDGpwIBMX59RG6k7EvNSLXwKGDduiyutkt_m2JTpO9FcJXBDKHkMpQvLaOPt3iVYAs1HAvsKBueHIUzUC2HkGrNN2NMMem0d24V2SB21dkg09I334LjayeBgeDM-sFgqbGthuaxtWpVGCd2Bsrd57y12Dnm4Jhg8MjZMiY6XAjVH4_ZkoW3XhAzKCnCT9FFSeP7Fldaq9B8NJUblDjV7FF7O7LKAuuseIte1MODO4nJSB6yDIu3aeErY0A3pmkuFm3F73jY0KAJDwUSQUyPa7Kv-7DwMDLn77XDDMTimMNul0-d5pD6M9RIN16TjrM4f-xFVO8-fcXnJghIcr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_clbzVg3k8qRYKXLDZ_-u7Ux3itTjsp1BV00zf0_JQt1SmBfat-udCnTzHt4WMdZ96UrNoGbKGyVmmyqrTUa1Raq1iYyUeuzbC8wqvyOlXirsBn6X0NocJUB7q5W1cClqghEDmrl-f_D4intx9y5OeSGdT2qi0uv47NLl-rkW6kxtWXKcyRGGeAN6AHXx6z7On2c0J5gNkWZnbHA98ptMrkKMDS0VALfpFrKEsYXZJEehzArGhY7DtDoBya5UeIf1RZJ9wKOUvQat844Dk0I1K5xDrcNxBzQ5iQ3CbNnYxe9ANx2U6ewpFy5YmqlEpSkuSy8tNzl1tbd_Z2vLLVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs91J4664jVDlbmMYp720HubUkbONF3cxl2XWM-0kHIPZvCuizoelgh7mx_luaGuTXU-h6o83UdWYbm7p_4huIyO8PZ94HB1A9C8mRBh-ampWhjsWchVaIKqsuZM4CT5y8xMNrLasLVQHdcZqeYtDOzUfm02QyeTQK4xTQMznKVmIfcMWWhN583NhHP7TDKP7myQwl-0_R8S4_HXsdPuMPdbWkMV_1mYFM9ZLPy8hAisqhBBtkO0d4Q6BbEZ-5DV1vbITNFlbzxDFM1bbyu08n3ZpUZwIYasl4gLFLUb1AJJDHTzWHnFJIcl6Al1w9JG8r2XGtxHPItX_KYncFKkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHJHpGfwdMPcF2SS77r9ZAJbwMa28YhONpoOaGiN1vcyrKhsyjL5e6XGfTNVzCerTqNa_Bh4ScsZC73gVdraawWNHVZh7nNp-Xg9MqkBO3K872nhl4iQlhmcoEKPzcmalhlOddSzRsPUixIQn4Qo2kaTmVnHTfBRFjLWm3uRvX-cscqHUx6SkXjgejElyDttSh5GrQZfm9sObsQu-qHk4BNOWXFOfnQGL6E9dwlwE4GWOAKStQVFRQjr4v5QLm1Ge9R33rW5MyJcaeW_x7YGRBvY2VDtFHp3Gv4tFU8VHqMQOyWM39Q5JGeXqnF2GhprgzZcjAM2RtXTtdrGzRMghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZldON3uZHu2RE7BuCFG5kZOhMlRniW3yLqozpNFPpUoo8x4tdVFeHVCPWMbEBhWYIrhE06-sOqgssvUMNkgcAdHX4dLIUagazTcVeoOgpiHsXfsTEkb5hep8glj317TmEFA-A0eADW1YFfKzikfCXHB9hU2wGYLVVz20EWHcIBynNd2gTqZa279jA-krD24qd4ckZTejOSwrW6W8167gUsW9M6MhgS8l3eBAB-8Eae2lcxUH0eX1QdamIcKpLMOZagOqAXEeodq8QliVrBodWqTWIWolYweksrxumtWxvvsG8XVkutA77A7NNwe7MWr63NsZNLDF_8GWzGkLj0wq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWpVWd8k8Q6kP9kUFd74FK25A8bSENpH_RdQOaa8rKGsERi6zKoIh1PxUEEoE0u-Q0HmbV1w-E-VuiZ5praPxfcYlngCjgp4jfIQxtXWRRU3bbKikJK89WD2OQwPwa73d-FRfx8NnskKQMOml0uwjtiS5QWJJ9A-fqlyOgm2z8bpmsCcEFC6oTnWz1lfEUu89s8fqXh0DWk_XOqQiCLMBMq5k4JRw4jdYnz_qBcU9HtxD2l33ZiUuReE0KaM2N9MGwZurMiuf_lMe8_0fsJ7_Nb8IGbn_v096J-0bgKV0aSy0VMrkqSv5_xeMUqzuhiD90_DyEvC7Nda074KdMYkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD6Q6IqiBQqr-IiERk-wNAmve1I35x6vdHsNAeDtBi5-Qt_Y_yGpgW-7kaHFoy_1KQpJwd7HC65fCPsYsNoYRPz7-7eZ-Q-drEUM-N0vuVhKBjwE0Nasv44wn0_-rig8AXk1CUqOx14NXN1k0dq0KKBY2tObbUpJgiR51VGNZNryrtfrdlr0L7RRrru863MMNqy4TucATMWo7glJp1BUew1TXWalG2CUHt-bMixrM_HbKmV_bCweJS-73ELJnFh2X-pLY5_7Err3mDDaeKcomBBtEDcaywT6bXnQUDzLgKHAw8uVeUTGNmZJvNuKuxR8zZNQmYhK24-CbiFNtA5pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7nguR2DjGtLFW9IpowNBd35Ywc9yW3nJaO2Qw4kTaadbMCJedJ2wpzVaOSp6zvqjgSUGgbPCDcd_8E_Ta498Aqk68uw9DrjNsU5TOkDDOUHRVJPzu5ZQlVbW44K-tZbsB-VF2gjauleRYfVlVw70htrJmoxOkAQTXdp5ErWrythfPoLJtQQA9Ie3V_YI2DcNKul8JeMC9ZGsJBAl2OOmfvRoGmHZul9R00l14tM9IBbUCfIcy0AupQZsBFbUVA0evxLYndmCU9642IliHgN_-9HmJ9tZVy-egg4kbhSTZD-7QPgoHgT5vd3wUqmD7yFBpwI6zsK9bZzDWWfyeSPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLpGEPvoGNO9BV_l7tywxWkDZvmeMgP6Z-FGKAuxWAk1LakcZJkgMFAJG0Qh5jOIgqQzYqAFjNnu4tAqfW1EELLFMHiPDWX7Sx8avlXuqeZz44p4Q6MEhNK0GkwA4ChouSRnKfk_qFH2s-47Y5jiGS1X5H6mkt9MwTuzH_SV6UFBsGOwnSLQYVszzJbeG8kqhhafx-jPmxmOMLfNAbqtEwfGvMnddwpwYLHWr5cgCi5sOg7iwnT4nqK5jF5qQQCYza51Yj74o0bzgrcUJk4EgqaY6RDIazNougq4buuJ54Ynx3FUlw1LwdrOHk9c7fOKL4xYsjl3fRghqheQjQ8JBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=t2MgOagMGpFj-6SxCsbBSeN2IdQEYThwjPsRnADr1br6gVxK6zsl4K2XqlS_e5ePca0ZmSprHHa3GgtIqghqvqGLxqzo0it1t-bPO4MBiA8MY3oKZPUN9DbGBhAmIfM687gxVxCv-Ck6X3nhinLNs-m2hEnpe1BQjxGfL7FtScikFD24j9e-DW1BdI6BeUJgv5NGtdWEWvPW2hhJ1Q62uNX-ifSwNuP-w6-zsXxePMPs3wPVGD0JMKHuefkIh_2t3NWbd5fNPCxR7ktTSz3xD2fAhnjliHfP7FlLFtHGLXaMe4kpbR9y99lS_6itmUFati-M0OEtcYDPTKtyilvkmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=t2MgOagMGpFj-6SxCsbBSeN2IdQEYThwjPsRnADr1br6gVxK6zsl4K2XqlS_e5ePca0ZmSprHHa3GgtIqghqvqGLxqzo0it1t-bPO4MBiA8MY3oKZPUN9DbGBhAmIfM687gxVxCv-Ck6X3nhinLNs-m2hEnpe1BQjxGfL7FtScikFD24j9e-DW1BdI6BeUJgv5NGtdWEWvPW2hhJ1Q62uNX-ifSwNuP-w6-zsXxePMPs3wPVGD0JMKHuefkIh_2t3NWbd5fNPCxR7ktTSz3xD2fAhnjliHfP7FlLFtHGLXaMe4kpbR9y99lS_6itmUFati-M0OEtcYDPTKtyilvkmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=aiBkV_cfOb-kiuAeBmVqBcbekZTK3_c_a6Y31JRz6yaZHBp27GMEsJXCnjmcR88egCl9iW26F4kYuSCxqjNWmmtTvjpPNDMjvlKYcxk9K1D0esl9rvnUMk34GKCb3szV-cIUk1JsEv-F0SfMP45DIa_5uP2IsTyCl3r6Rsd7_nBe41Rz5eD9wJltRuf2Tfwj2a7rWUbpgQZtIPSbOkwOBWPzNvxjqeQY3BRi4aV1C5Mh2u9HU1OEzhRngJ4TiAIdmbV1V_Ad38VCGqarYMT4cXO1QegVKbYysGxOcpbtXBm-sfC2_GrfTCdU03qdZDBD4ylU46a84bDFfBpFFgs0LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=aiBkV_cfOb-kiuAeBmVqBcbekZTK3_c_a6Y31JRz6yaZHBp27GMEsJXCnjmcR88egCl9iW26F4kYuSCxqjNWmmtTvjpPNDMjvlKYcxk9K1D0esl9rvnUMk34GKCb3szV-cIUk1JsEv-F0SfMP45DIa_5uP2IsTyCl3r6Rsd7_nBe41Rz5eD9wJltRuf2Tfwj2a7rWUbpgQZtIPSbOkwOBWPzNvxjqeQY3BRi4aV1C5Mh2u9HU1OEzhRngJ4TiAIdmbV1V_Ad38VCGqarYMT4cXO1QegVKbYysGxOcpbtXBm-sfC2_GrfTCdU03qdZDBD4ylU46a84bDFfBpFFgs0LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SntpxW3CClDDRvD1SvDECvp0iGbolZFJuX7_YlWqARJloj3zNDB6I-hJzJEjBMf5wWZnJuPGaho3tllh-kWOv9ui_Cg-CzEDG7vaLt2eCiznPPepMefmc6u4N-9IIh9o2UIg5b8r87WMHlU8hwtDhQgeueVEMTfb72OeyIQgaf5EL-lKj1601z8i1PMKi8uRO1Rvb1HFYVBhD-_Y7KHLn-vWEvKDHfaA0gnTnXKwk-AOOAWl-AryfVJLGm-IhL1Wa_r1qXhBTATVfUKfVHmrP7ZemrdZ1U_avykGQ0gVFjU8psmseHlCRiBOqIQ-T-4HXrAbC0nV8p8RnV5iHkS36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUDKCg3gaI46FYQFNpKx84b2I31n3kvywwA_9aICGvFgjg1w5u7BGGXAd19INKPkLuLDJEi-1D6oKgXoFHiGD-zOGmSRkJ4Gdjr-Cvrh-j-K19Lkaij1rFv6s-XxbWGDXkLZpQ7w3nwqXBb_22RR55I5YNg6oITcb8o0YU4TG2-9D4ssv5QJ3WMTCawdu0-YcNZzmepE1FjzzsVrFoObFPfwkCl4kxSoja3HPyljCY910lAz_fWjIRxm6bPb7yMupVGC84eE-y1n27Y6zdzlOQswW5TSIPklCr_Xae0R4XO2vP5oqpoL3cspCH3lEayr92EDkquBHHT8IeCfa64wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-dtu9Tj9-NhekCgZmyVGPC5kmggFuJe67R29nkZfzdGCzP42lnIfj19KXjstyQTPQPqXdWWUt1_XJccA8wVC7v6V9wI3-X5V1XiJihWfMRk7yTjNpsfQ5T2XHxvz84_dSkJ4boMSKWSEecYNyijV0tU3n3AH4MA6a9hhCeWL4jJn-bdxvhebkUD7A4ZIxxdKrQrn6yx_aeLoBmQwacM9YwWgbM3dCN-rt99j0z2mAYGXMx7QC5G1YOK-v33fxzbGL57Av0x2pt_pPO1tN_L5pTP64NbRFO0q10PZKYzKEBsw2On37GfhMvXC4FQpq0g2NKCjY36qi--bMuBEzOkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=IybgNMApXk_LFx74Jyz-xMF0FYmKY8RMVXFp104Q7gmMo79oQIwM9f84WNlFIz84zFBMjED_iTBLqX1pIx9CEXg8HGeeAan2vCJbRtwHwGMnosrZ9CRAU-5R59ngJXb66KfJR--uTG3yke310fNVTbvteDn8RkNXmgdYiLlN2P_CfUvP-_2sYAxkh281q6HDMUyyPmfHe1UoJJdkpMmSxeke4nQlcQUjAwyzNbC-0XRtmpJpiM5sDkU2zcyyboSR27Y1YbcLu_dgWjw6QJKZQB_2Z6127X0_-Z4H0wXii5-0PIXLqQ2ItziiasgbtubGkAsCJJXzRx0kNcrxm1UdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=IybgNMApXk_LFx74Jyz-xMF0FYmKY8RMVXFp104Q7gmMo79oQIwM9f84WNlFIz84zFBMjED_iTBLqX1pIx9CEXg8HGeeAan2vCJbRtwHwGMnosrZ9CRAU-5R59ngJXb66KfJR--uTG3yke310fNVTbvteDn8RkNXmgdYiLlN2P_CfUvP-_2sYAxkh281q6HDMUyyPmfHe1UoJJdkpMmSxeke4nQlcQUjAwyzNbC-0XRtmpJpiM5sDkU2zcyyboSR27Y1YbcLu_dgWjw6QJKZQB_2Z6127X0_-Z4H0wXii5-0PIXLqQ2ItziiasgbtubGkAsCJJXzRx0kNcrxm1UdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohaWSmqQDmfCYN6BhKv2iwFQbXu_cWP_tFqF42qwHS6kc0w28LDIKqxM_rETAfsFGfmsSD5BmCErp6W6cR7Ft_1gmn7CJYjVuL-3z8aTVeSa4qWL97Bz42ojLJ5J6b7JHcjQ7jQmGwjblkYXwrl-sCUL0ORfkA9r8uuKpqEwsWVQMl8-Lgab_2UpzOhqI_zjm26UnGxITpvlteei6K9S2CuBWpAjkNGv2NrmN80KcWvs-epgRQOtN6X3ZC_YzBO-qRO21ebxmlBejl-n92nDjXHDU5yJRyMFtP0DDVRaMDTs7AJsZXa7Zih7fV6zHZa2k1FqEnA7FCDAqvG4xHWrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY8G-jkkr-X0qrsnfPiqscYB5ibYJ0TyznYHSb4zHapAO7oNZJbLJY2RC4-R4ib67hOKl45sg18ovhU0sUSTpvgV4kbBtfnG-g5i9EnzoBHlIpeKibHWCFhymWAfQpF_qUqHaQIYvGGCoatIZ8660_Mzh9aMz76SmZ7vUSoB6VCbh2WokgU23ka1PWyAMkgVU9CpoE7PG4olvBJ66p21ornVWKki_RtNCAC7IT85Iiq5wX2k87VFCkAilYKoqb0jczI9fyLDX8aAtwEQ2ehQCcnIE1NeTT1ibAFB_R1AqIYeJE43S0slkiJrv8dTVuniBieGUfOE8oDW4bcZ2-Cqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd4hsRqPw0rzsWpZTUcC0CA3oI81GiYlwztzm9VfI8ttkram70GS-SjMNdw7l3BYQPCPlTcXbHzKjOZRx-rYp-x5nh8qgzS6-sW05M3GyPnpoWdyBBa8yDgQA2HgIR61I5naF0uFsU4GNGYsKHJTXdpAJzyDFrEYZQ99OPSvQUePzMqraiwpJFohKCujyrdB0wv6NTqmfHERjzc3SGiRINA0uSmSkersl1vwB1pko4_OEC9sojh-aW2k3BtugYG3NuTpv4GfUiJmb5NATGFUtbzpMSyjuCaUDHIGIkTjB_-JfKafp1knW26Sr7MhlK-B2bkTPXULaqzn3rb_ZsHjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJQJOGtXvZSJXPXxHge31dHv6I7r8AY12QzT7_GsMe5bWsB1GQnvI4vrYkq6NVy3Bf7sYLQGDWzYNaylsJAUVPbc2q1j-4Cx_IMAAzCeduoa-NutkkRpHBvlAd4DKMe5Jx0-4M4KjibrcKe4vyGJPOZfuLG8MnhernZuEP8tW02e3lyxZDj9ApH5IsGyGCJJjuEemS-EcziOaKeq-mUb7naCVolKrNWa1S8GtWWtb3Nz9g8LCrbGaXSGJqYy4L3IIwjKQlmUU-hgHC46vnV-e3bOfFCKuAZ3PB_BFQayC-KYAzkQQDEqycdzsHiLa198D2heN0Csv67S_3soRcTBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiNnkiGVlx94GpoRetsGKxlnRfecVsodPcWErZjk9cC0G387xRWuyPUEMRaAM3OSiAq3FW1PzalEnqQlhoZ2ssoLnI29zsnYns3XAQiV_2V-IFYrOUN10PWqOq5_5TR3QXRrnsWrST5kpoaZo0UQhHj8w0aHLMeCcnX2sBfBhR49cLx2txaWD1ybfMT9BgezDUJTRB4sF8gE2pI1-G1tFqqOYsXjJl-bK5xb2nyr6ULo5FgRcCP94-stxsQonqBmzuvJJfXEIcEzaIBQjbpOB42Q3y4nLpxQ3HsO_Xz1vAszwjBKKBsYedtXK5xWOJgCAEwqWf67oTsYEFjb9za9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuqXK7dzJGYfgT_6sT6n4xvCeEXboeUy1-DisPATmyiEOgpTigIkmBt9009ulfWnOxQiOYM2DEHRZaElkqv9nsJpHlN2VC3RGFj-74NJYfjwAljufUKkNkydfIdn37TNbC23-if5hgUvy4bUWBbkaUCds48Anr8hSdWeaoVceKY8EOF3kxVCXoQRj32T3V_0ei7NnJqjErLKrMiEumdjYMcYDyJtm_PLb7woWPHqJwRHZQoOu3eyXhIPtfEAf1LcMJSsi8Mu429g42OS_H3r9uw9lITauPRPhV0N_5f9BB8Hg5SH8_spbOzIzxiGzayiCKFkADz5i9Web5gyJisBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9JRNAksTjmlIF4elDOOfod5oQJsdN8RtogHu2cyBmsdIErSrg7Z8HroUeSJMz56_EHXk3CTVFIH063PW3eTnQMBvC22Veua1X1Y2vSd7qWztvc08vncR2JfNsMT9MOLft5esRJeX4079M5Hg-BjFpwHHajEBKzHKTS_R24Lm859Ivyrs3N3njGyJwWyc_v89K_6k77yWYxTpkWwoxMd2GpRHeUoCejj_KXph1bI0_0sCqAmgKr-l58z-VMFiBkf9Bo1OwUluCyshWBCLuLUUoEtiB3Ah06XSiEnXuCEH9AUXxIbQbjsqKEj4ykhWISoyex3M4OX1iO99g_1TLG9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxvjCj_dmK7evTlA9biLelWykr-W5eCA3GODa2rWaOQ3aM_3YMmdYVsy03s6Od4g8rWYZoLOY2yL1T61oRng8s2z8XKmIiVNEtS8ueQsKeqHScU4oefmX3oX8HPWETjdlz8gnX7zpx2nasVc3EoNvVCns1i7nsJ1uEq931dY_tLC9ofjjuAay1dC0QC-iLFZAbEItWYLROlGfPHJNETftC5bqrxjQYkbAo_FcL9lO3PC5iWsunxCdL4sDVwBurxGt8dqUqqGA2W9qKuajazEBolPsYfgBqLOH_cTvCxHcUxMh9aK2bqMs_BonX9n1yDHlHMEQKycxuEJXGFkgmtk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuPjD_JYSpIjYZAPbJt4nrq1DwcTGCZvehEpsbRJk9etd3JlMKdZYwm3lLn8MTwJwv8VAcL26e7rqYhC67mRdfUw6RWcosAhG9XKTLUHsB4jWuegz_skty6IrOGiKLVypQEI_KxZBG0HiRGf0rHPuaiZxr0WVCJ4C9K5zt6gmhiSHbMteGV-mZYPagHj_gNPfBmvq5vtTN2CIifoGVV1yYkjcnG0X-GYky3BBLvDC5acaX9hBboE-nNQUveRN5Hl8JOxcKXm1o4GdrXVZjXrV-wwE5FceZOBwrLpk02IwY-RjiQI8myLey9LAGCeC_QizLPoGHBCc1k6F_WIOGUAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vB4Ci7nZ7Am5OTbRQipsXkgHt6FfQuPH4Q9tFLHnN8fi5p3IK96NUn_4syECKtXWi5yaGLN33I5bvFPofVFAnPJ7jlnQaqGM40pZLN84j0-Yw5bTLijuowY4cENa13TkKjCzZ6MUmim0vcAliK8am9A-l6YNwErSuv2cLm6FGdyVZ84VReVBO1TUMiXVoldx9weDQbCKLUzQvWwQicUMzHbo05EufWumMJdhVqAPe27UZI6dYpa-wiVuRA3jYYBbwSyLY4VDNbbWKa0kqwXwdwGrMdn9E-lcBcHhDFlwCPXO29Rg-nhvwdZWoT4EAiCvtMXKKR75d7nFhAfcaY503Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NahMJc1NsQXThfWoLO2Jn0L-Xo4Z5dihMYTlVnGI5pJB6Nei_EhfTcuW1in2FbxTYXw_7_5kA2ED9y0lYf0BbjaI7Z3LHu2N5FHDNBI6tsxnya41ohyuH5vAPMI3JcFNfxwjBZQ5rYH3XLcCW6HGrVWnbuPIx-6DAAPvG5XRhIwRsd4J1phR0uL6YUKtXRHqeWcOsUQV4ljGeQhGVJTJj4QGAPvMUfojPIUyYZGro74DQMhGkz2dyFp5jG3pxkFpjUMKYinMCvjufR-Bg-F4FmjCfGyAYwsmoR41mwxzE72r8CwygsPPhTjPQfdHkEN3Yl_ttUymHaSOtOsC90A9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=NnAEsQtkuA6kRI6uj7MKePNeHxiE8VBXMhWF3Y6KvN8sWyxkRQFG5OdyfBD5MTi4n7PFV0p8TuZYvD_YRMciPCPZsUGSQkkU2c0fovNnpcQM6Nk62A7mDM7K_AMaNeSfyyBYVaLBYmLqdZYYLXK_stuauBv-w9zeHwMIJwgchCTEt3dK216pGxJ2bt4BsfTGV-vS2VZ4xQRgdfVupmTgH97pHHcgkbwU0dApSbPvxXFzjePbkE_vuqAvshVMVo4byUEQB1-PbnocFWqKx1OBUSdJW3LYwSnk3f0it4I8Et3LgfgCxuO9WjqaICymInMjvU0LYdvXhykpV50RQyhqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=NnAEsQtkuA6kRI6uj7MKePNeHxiE8VBXMhWF3Y6KvN8sWyxkRQFG5OdyfBD5MTi4n7PFV0p8TuZYvD_YRMciPCPZsUGSQkkU2c0fovNnpcQM6Nk62A7mDM7K_AMaNeSfyyBYVaLBYmLqdZYYLXK_stuauBv-w9zeHwMIJwgchCTEt3dK216pGxJ2bt4BsfTGV-vS2VZ4xQRgdfVupmTgH97pHHcgkbwU0dApSbPvxXFzjePbkE_vuqAvshVMVo4byUEQB1-PbnocFWqKx1OBUSdJW3LYwSnk3f0it4I8Et3LgfgCxuO9WjqaICymInMjvU0LYdvXhykpV50RQyhqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=izhtjAunXr4xEwWtdOIj9xi-tsxHP4qKvGkciv8rc5Zd-YFTbl50ZAGKxN9Ap1GWwDN5IszEtQ_w8OKV472dGYmJTdoWYbORpEwqZFeNMQ8iYOJsms4aPslBN1FPOiFuG_2k9KnzmRiyfbVt0QughpCFV2Ee74aerMTJtDZa6Vxvz5c1Um2r-AaLr1GPQMGE8SjbNhuxPvdByox69-05VhMSOEaNSDQ0f9yWyLflebHw0zdyWcTWqipKONZiYhik1iEAaDAudH_umtjbeiKX6nW-rtVOPdFFkapOS4Nn0-ALRaO9UDV_awWNCAPUE_xVnuuuFIjoDkti4IowIvJJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=izhtjAunXr4xEwWtdOIj9xi-tsxHP4qKvGkciv8rc5Zd-YFTbl50ZAGKxN9Ap1GWwDN5IszEtQ_w8OKV472dGYmJTdoWYbORpEwqZFeNMQ8iYOJsms4aPslBN1FPOiFuG_2k9KnzmRiyfbVt0QughpCFV2Ee74aerMTJtDZa6Vxvz5c1Um2r-AaLr1GPQMGE8SjbNhuxPvdByox69-05VhMSOEaNSDQ0f9yWyLflebHw0zdyWcTWqipKONZiYhik1iEAaDAudH_umtjbeiKX6nW-rtVOPdFFkapOS4Nn0-ALRaO9UDV_awWNCAPUE_xVnuuuFIjoDkti4IowIvJJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=afaAJxS0ZMPKTHHxGXHV2swZ0I9Zu1BjQs3-ErVFxSODbrIBDcrPcq8PDPFcFDqjWOIM29bs9KlqffD6hgA9OYwOfTJgaDKzxVcrr0Ajo93_zmSxVXuvqdgKcs_m9FQWEnm_yCJlxhpDcFS0tBRlpVknkLH1wkQhhJKskIQIwWhv70gIzviUsmS5IeEa_dJCPklmknbGfuHrWiyZnu3JHlrW72ZHprsIu9iwYlT7gFk2uSfQCib-Z4qtGJ2T9msCuRxERUK5YdFzmuz1u_7G2JmK1EZ8OEot1DEbKcFT4JT24KYutTOrYdWRDaX3FSPmvFQqEIt-UpI9U_Glp9nEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=afaAJxS0ZMPKTHHxGXHV2swZ0I9Zu1BjQs3-ErVFxSODbrIBDcrPcq8PDPFcFDqjWOIM29bs9KlqffD6hgA9OYwOfTJgaDKzxVcrr0Ajo93_zmSxVXuvqdgKcs_m9FQWEnm_yCJlxhpDcFS0tBRlpVknkLH1wkQhhJKskIQIwWhv70gIzviUsmS5IeEa_dJCPklmknbGfuHrWiyZnu3JHlrW72ZHprsIu9iwYlT7gFk2uSfQCib-Z4qtGJ2T9msCuRxERUK5YdFzmuz1u_7G2JmK1EZ8OEot1DEbKcFT4JT24KYutTOrYdWRDaX3FSPmvFQqEIt-UpI9U_Glp9nEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltum_AwR-OGLOmwdpkKX9KbEdV-8e8foEPTMLzi_QN7PTv4hZ_sT27WHbQQHR9RMsTwMQfPE8n1Q3CzkfLgR3iWuTFhklhQElbZSZujdgQBRcseUSRp56tVC8ugruW6XZWMiXpjp8Yx-mo1aWE26RGLVcHN4M_1czBPyjQ6ts8uy47jDhj-iFTlPKeKhNx9aGWV7RiY1wZGmBUo4uVOJD4DYPrcCu-DsNsUJEYx1HaEpget4W-7eTAJuIT5U0mOGTQ4mgIZ9HAhiFiB69tZCNZQp_61JAdRy57nHEsE4IkIfCdqwKhWC0zYpa507IoTwikKLtDBgncCmrutppqHjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=WJBCV3bHveUnFaExbuGZukFs6ITlAhVGEuGjX4K_trx5duga8tvtZWGG0iZD0CRIvbmhw0YT2w1sIgO2cLIcfAMsgPumGLYfUOo33BTQhUdW1RgeK12yxE78MPZClJAjct_r7kvW2ZGv9r6WKkm4YImXTP4aglwtP2r840aGE0nE0ATF_eUWASmjI1P93Tv-Nl0Q0TbQ2XN_0P7ZKTy8FCi7ll00MQzRSOEEGP2ZWJxsNUXFVH39t5xUMe68cXAujN6OJHuKxnJWdhOQHb3PS_K16oSrSj6MDPq94krrAyjSsGGotYH_riatLw_2WIjL50R-aBxXPqv1Q8elUNzZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=WJBCV3bHveUnFaExbuGZukFs6ITlAhVGEuGjX4K_trx5duga8tvtZWGG0iZD0CRIvbmhw0YT2w1sIgO2cLIcfAMsgPumGLYfUOo33BTQhUdW1RgeK12yxE78MPZClJAjct_r7kvW2ZGv9r6WKkm4YImXTP4aglwtP2r840aGE0nE0ATF_eUWASmjI1P93Tv-Nl0Q0TbQ2XN_0P7ZKTy8FCi7ll00MQzRSOEEGP2ZWJxsNUXFVH39t5xUMe68cXAujN6OJHuKxnJWdhOQHb3PS_K16oSrSj6MDPq94krrAyjSsGGotYH_riatLw_2WIjL50R-aBxXPqv1Q8elUNzZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=hnwr-NZhvLfYRW7Z7vEavnEZ0c6cJQXTMGrt4V4UpncSQROVul2NoucS7ycGtt2I-VH9AxoNWHsJd63-QmxEIlYB3jv9JKlgv3D2g--JD4AGF3-nrmtjap6WN05vagPZhq-y7K3MGUqRDTI7B4dWPm7TCzREK59SVWPCM2VLjogQCdLsQKvpHYWaO8EqKXISXmAt4gmrkJrMP9D6nQpxb8UxB9XeHY7wowpzW5-sfoEHQ2ToNSoql5I3pjMZukXGOrhSe6YfFyxM2fKkvI4f-hRUqX3mQOxhZkOmCrl2tBWYg5C9OMZNQYHDYCHIIPXEd4YJgfeRR6MaFe7PehFoWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=hnwr-NZhvLfYRW7Z7vEavnEZ0c6cJQXTMGrt4V4UpncSQROVul2NoucS7ycGtt2I-VH9AxoNWHsJd63-QmxEIlYB3jv9JKlgv3D2g--JD4AGF3-nrmtjap6WN05vagPZhq-y7K3MGUqRDTI7B4dWPm7TCzREK59SVWPCM2VLjogQCdLsQKvpHYWaO8EqKXISXmAt4gmrkJrMP9D6nQpxb8UxB9XeHY7wowpzW5-sfoEHQ2ToNSoql5I3pjMZukXGOrhSe6YfFyxM2fKkvI4f-hRUqX3mQOxhZkOmCrl2tBWYg5C9OMZNQYHDYCHIIPXEd4YJgfeRR6MaFe7PehFoWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tL7KW7IpDfV-NrLBStZ7C-McaJks18VBh0Ak4P7-uCtHj-2gqZUAB-Xxj911tEfcAiqPe8qRV_1IUpC4oFGg-NSt3PaxvSq3MCBz44FWMNFS7s2MtKg4QEMa27YJkj1xcUgC4_-KBp_lGIY7nIJ8OWNdYwljg-epxW64es1lCAx_PXyRWGYTuS0nVAp1tuskg4LcLFGZqAOUeV69jLjrUvKa1TFzIc5rp8eOQvCiG1xbYXNiLjYbDWgKTjmL-3jJYqOqz1-6io5BFJ2V_FPLybMZOEoGdaPFodEu_bif_21QcUtmUKuhTwKiDVA95d-Ena1jqVnR0TFJFtKtGRDDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUdhaKLlQ7NTZISCijTbIruaSD5gpQEuwkAb22qvr0P825g87fmti941vRsjkxYW8ItJK5wWeQKWGYm0y3CAbovH-G2wWHi3HQvZSIo00jH4n5zstI6I0gklBlEebpJTqcs2j9yHjyLSx9IN47aKheVeCVo4AlqEr2_JjSZQINfz4R8t5LGpy8RasPKJwpvp0HZSxDGUIMQhmvKwEVUWuF1TcCRzA2unIkxzii-6uebixi3R5WeOP2edQH-C-6rY-RJUqCl2DKSP4si-VS8xZWZ7YopV9EaBRFBBdmNbXt-tNjLsuFX8G-X3MFM0ogBxSQC_4PuROB1EHL3hlt9ibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTEJWjueDkg14vHSRbLqloFMHNjdPEvg938DSd3dLttkFOuWOi6Ox9EfFMIDZDIeDaidOcC8gVnClUg-3iy9VynLfg8In0qc9E1GmOukY6XuwgTbLdF5pn_3u-Q42ZI2gnHshys0DzGHvxQBEoGwMFA6O_HyWazvYcz6cVlXcUPaTrQSEjhueh_QSPsUM9_0oWOI9gYR0bWikb2KuSTqXa88rPFypA3OHzYephKoKZX88sJVyPvLGbDxIpP4unFl7aUy9JWNJuWralb0yPcRjmxl2DUONZFXcv3hBzaAcVBZidmE7Bxu-ekKnkeTX54WaH_dSU3R-PbUmbr7J9yhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twaOK5SIs_4t1KN1GSqW8gfDMekSTES9iUUKzjwp4yWeCK_vipazPzIMv8hUKvth22JsgoCavvU6MvmfCVi5x9nTB_a_uAfpQV69Z6l_KkvJrlmkOk4HnUdf2AAy6F_iychDFAdit4QtORN98TQEj2ZVRfHkag3-xtD6YJlmr2OXzUjuYcnnBvpf9tZIz2gY-szqGVctt5r7SF4b0ZVr3ghgh6eQrCgwo46vj5-61e1zvielD2jQUgmjSbE0-8YB307TIcNgCEl6uG5Nd3pFTAHARWj4bJSOXSheBMoKEf8oITghdaQk3X_IFnEZys9aufQaN2_SzEswABX8qOa1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7a_BWTPa4rCqfZp1w8TtZ9UEzLq925717KPx0cdIvCsVkgqAYwxlQYmg2Y5FMRwtXCjUoBqxluA3jIHadCwJyZtgt1_tH1zK-0C8cyNm21dBD5yToKCOYJOsDgx3ZYbjLPq5NxhbOlqFCMp-OFF8K3utAPQANS6kH7THPduVfF2-bCca3PvtX5di932TVZv6Tvd_vp8fKeD73-lYwmRKI9lq3ompsmTmimtpZydjbYp2cjcxkLi1xzl3KRQBfA2X40FiXS_TpjeX68nhfsRtno6NTYe2dyhf83svYoec6oYncOSGyjHG8acuMThsXnsybaTEdIZT27Fgr0hSTFubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeoDHlMT_yME69tXjyYHbbn52aoJCtGNy_TPJ9nlVguI-5rN_46huBEKyC5wmr4NUzS3tkMPqNXzRyoPXDXlo-nscO8fssuv1DwM_z3WrEpCR_Zm3QUtQ6Asr3CFcXPbR6-OkGGbf-seU4J-YZq9oNBUyfcM1nlnmU8pkY5NkhGU9jeqXeS-2gsDOMHdUNFlQq-HyTsCYIgrFmGONNPil65pafQ92eURolDgDk2HnCb1xdXr5ZDbB7s2vayX-joIGDu2oJSlYggiFgv9mBDZMN3gzaEFTgaDU870SOwclOcaAkHNOPRdXE0yljhRKa-I_8WQpOsu8-TUU3HnUMFphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukByoOSV0RoNKgSeIDVo1m2txmTnz3lR_fVU-YcEJnnq1mEqszuOlBPVEqVxVygeMM43YpnBeGDHJtZdVGNmjyH-EGdYkEscH1_xj7YA66Qu4q3P77_pvOhyhCet8dWun6eeR_rILhSoyyD7bW8uscE8I7MggC01sTw-Nru9IMaowCOgHYmffBOOvgFZhTC-vfwDA0y86HTQZb4s1hK-E7TI-OKB9JME2piegdh0wQJc18NL2ddm6PAmz-IaedBES2cpF6e5f5yTVe_vf36ai8WsyqoRIQ6tSVkDUNly_1TuNeE82Dor-bGaW90UR9IueMx2vsfzyzEBGQgHAjr0NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=PAVMFRJrncHy4wXt_SEEaikNHsd0mvXTK8S_Fm3Krt9dNp0T9KHABOHkIE8Z9PLh2_3BFVofC1nDaf6JkrNkgDQltDx2OoUzE_nTbCSMu5y8-Vp9iFI6R2F6w6Ep8EWBnOy8VZB13sW8AWgG673qDjrEVWUDAVySseB0B3w1dkxaf8uH-qlD7g4zUVzO7znn2IN2WVcF3zC6sdUVA77qPqDJgkkpJr8Zf9dgbOCZN8hAM-0lv8iuMjdlraxisqZKAuiCQTWKwbbRgfxP1jxV35LTR7bJkn28KkvI2SkAeej8roGj1IM_3lGnMw2hLmpqH144auAs1Ymk_UYOz_XIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=PAVMFRJrncHy4wXt_SEEaikNHsd0mvXTK8S_Fm3Krt9dNp0T9KHABOHkIE8Z9PLh2_3BFVofC1nDaf6JkrNkgDQltDx2OoUzE_nTbCSMu5y8-Vp9iFI6R2F6w6Ep8EWBnOy8VZB13sW8AWgG673qDjrEVWUDAVySseB0B3w1dkxaf8uH-qlD7g4zUVzO7znn2IN2WVcF3zC6sdUVA77qPqDJgkkpJr8Zf9dgbOCZN8hAM-0lv8iuMjdlraxisqZKAuiCQTWKwbbRgfxP1jxV35LTR7bJkn28KkvI2SkAeej8roGj1IM_3lGnMw2hLmpqH144auAs1Ymk_UYOz_XIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oClyja_c1h42jOO2a-ziYBj-Z_OdOenGSFDqTbrasf8eOjWQ-3zxD0hKZC14HWo0Rc_xT9szZm99FXtQcWaiNy4AwxQXkC_KYX2YVqdGnuFixgRZonMNz6EhAdT-OC6EoQr-CUyYWeIX7qAGAz4u0t3RR_rAh7onMuB8kw6tGg8tK_YyJn7hM4s3JVEMt0Ex4zzl_vaHz1nLqq-5q_SHHOo_hzNrZ4YxFMMe88WgzPVdKBMnwg4-qLCmPtXHATyJb_hE90GuBaET6rVKQSEvuB9a3jZr8Y5RilqMYy7GYZo3ytkyTi0Kxk_v5S6IrHjEwZ1SLrWzZ9GF2Gb6ufiYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhg1cM38QE8xWI3zW86RBl_R8YVVeQpL4vLbLjkSvQm5Jvz9TgrENy18ybE3U24p4-mFEXnVutQt2Wb5q70SNJ1TwzLoj7kReaMNHB-hmFT2aGG-E1ICVd0SmFzUIophqflIqKUAHr1CO-Ekc75M1djt_VtT76U8VB7VRFMlHRF9RwcNc45YxpYaKhdWMt3S5J181wQDVcZZY9keaiLYLWd6E3YP8k73m-cuA31UPvfuhB_flH3UhLMMTpi5hyfOZylcfKXS5kPlNaGUcXbbgRo50Zv1OqYHWXIbG7x_V7YJ7irJl62vbDdHktv-sLt5vUbH1rrammMMIHehvsR_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhuFKIJTv90UvHnXbZAV26bvDSC8maeX2VHK8F_LeNN_wJWWv7KYhvYOHbmILc8W1dpEURqEIvv9uhvpQFYEZp-hSptgZPmxokzFPtsKNVlnH2qpzlm_mm8GtwPcedlLrZ9CcSiQ8FVLA11f9BZqTLk9PGtJl0YBLK5XAjie1LvX38B2IH7F8J8uW2M7NTTlQgUhdqG01AlY6OGLqNEr1RrAjVgQh30MgNZ5LgsoQvNwVdjD7i1ICoNoWewwwio3psY9ALR81ku571kFBtznVs7zJInd9QMvUo4r_-rdxyiKbquir-OD2y_gc6A_yboMiCE2Muf0et59jGCf0DuCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
