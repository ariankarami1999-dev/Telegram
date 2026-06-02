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
<img src="https://cdn4.telesco.pe/file/gu3ReaQ210xuXWBZ65JMG5L_UroZ2TFDjTLLnKhhmpiPvIhQz-KbFtg36yWhT6mkFSxKdrLsQysiXaINAukkcVmuhMdkuTIGWMg4DXwYAuhrT8lgaE2EW1i4aPcvCz069Cz9w8Er5h95hzvrpKHazTEM_Nq9dr3LsPT2sGDdlu2yEh7iHzZnw-fzY7Mc6PGJ7kVAAqsFcZjQB0fr3h9j74Fg0zycHqcC_Rbc8dRjOTjmP2l7ZZolDMiS5D8EO1Sjo6ut57EDT1MTN2_inl0vCiBGwEGLul-VwqoHtNuaFSoVUWnRUhGnTIHxEQAFw09rmGywmnLweQXLUI3MpC37jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 00:57:54</div>
<hr>

<div class="tg-post" id="msg-124611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ادعای رسانه بریتانیایی امواج:
یک منبع ارشد سیاسی گفت که هیچ گونه قطعی در ارتباط ایران با آمریکا از طریق واسطه‌ها صورت نگرفته است.
🔴
همزمان، قطر در کنار سایر واسطه‌های منطقه‌ای، به طور فشرده در پشت صحنه کار می‌کند تا از شعله‌ور شدن دوباره جنگ بر سر لبنان جلوگیری کند.
🔴
منابع آگاه عرب و ایرانی گفته‌اند که یکی از نزدیکان نبیه بری، رئیس پارلمان لبنان، به همین منظور در دوحه به سر می‌برد.
🔴
نخست‌وزیر قطر نیز امروز با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، دیدار کرد.
🔴
این تحرکات در مسیرهای موازی اما به هم پیوسته نشان می‌دهد که ممکن است در آستانه یک تحول مهم قرار داشته باشیم.
🔴
با این حال، آنچه بیش از هر اعلامیه‌ای اهمیت خواهد داشت، اجرا و عمل به توافقات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/124611" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=ikbFpJc5Ro3neyelKaVD_Snjwy305MrtzgjkeZmfv9FVm7mSlz01wBJEIRObnIF_Klzo2aC2DL8Bzoq2OOMUEgQ7vUdvXdBJzRKrA_jz9QVHFd5kmQuajmDEN0SYwEhSMr4klqgGdo-BvaHb4hZFor-DT6nDws64mb7QzTKhydxVnfdQ7fYXyyx_9P9wP9bjIag6IKwuHWBcioYwlnhVoYeq0TLwNpEhMp1bbsfIRW8-EpKc-CBSGIaFrFm5kZPTE3zzwgPclAlip1R8ztc8rw42n-DuBMwCsuHLAqhjwxSgdPnakb4yflumc4jw_ubRxlveb29Mw-YmfQ6V5_ppQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=ikbFpJc5Ro3neyelKaVD_Snjwy305MrtzgjkeZmfv9FVm7mSlz01wBJEIRObnIF_Klzo2aC2DL8Bzoq2OOMUEgQ7vUdvXdBJzRKrA_jz9QVHFd5kmQuajmDEN0SYwEhSMr4klqgGdo-BvaHb4hZFor-DT6nDws64mb7QzTKhydxVnfdQ7fYXyyx_9P9wP9bjIag6IKwuHWBcioYwlnhVoYeq0TLwNpEhMp1bbsfIRW8-EpKc-CBSGIaFrFm5kZPTE3zzwgPclAlip1R8ztc8rw42n-DuBMwCsuHLAqhjwxSgdPnakb4yflumc4jw_ubRxlveb29Mw-YmfQ6V5_ppQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا به یک کشتی دیگر شلیک کرد.
🔴
بیانه سنتکام : تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/124610" target="_blank">📅 00:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
توماس میسی نماینده کنگره: فقط کافی است کمک‌های خارجی به اسرائیل را به مدت یک ماه قطع کنید، آن وقت آنها بمباران همسایگانشان را متوقف می‌کنند - صلح فوری برقرار می‌شود، تنگه هرمز باز می‌شود، و قیمت بنزین در هر گالن دو دلار پایین می‌آید. اسرائیل بزرگترین دریافت‌کننده کمک‌های مالی از جیب مالیات‌دهندگان آمریکایی بوده و همچنان هم هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/124609" target="_blank">📅 00:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b65xi_UwdTOgZfd7K4Jf6Ob4H3pycymK4ND-vtKziodR18i75D__lwiYlx14-4Wn2WHSoumti9Mbk5I7sGBbaLxH47yJmH60GaXfyHyUCG7zNsdjK_5hQYUYzl2bvyGo7GCgiZ57pkVcxrWfO9TaZzJh1DPhnSY5y7RcqgT76aYj1MqJOBp1er9TfdVuZUF2dSGgBcop-0EF7XrDM_llIO1pin72Hl6mOFkGZ6NkSoXnCS_O5NSWzjm5FTvDdtwVPj_lYLudm7kyWJzKSyAR7Nwz1MPDM0BUvnENi-5gbqG_oWUq7gB7_ba54JFI6345bPGX0BIua4MtS37apqLONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد!
🔴
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/124608" target="_blank">📅 00:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124607">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : تیم مذاکره کننده با قدرت ایستاده تا آمریکا به خواسته هایش نرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/124607" target="_blank">📅 00:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124606">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r93Pp1rHO0Pdo2NmgV1jXH8nTylESfjQlLjtxeNQGfdn0frbOxPDgzf_qeZL-c8_AyAiKSsMRGld_8TkJL9m9cHv_L3GM-HJWGZAhi0qeNs3TpyGQPEnz4PuumNxT44zMfEhiw0z6vqFSBvvAdFiB5KUu4J5RDLeDKTZN8DPuAxI94l1-gTImdrDEPXZON2Dkw0rnNaDEjjx3lACoYKI9watnOruWYTCFKxg0QMUnkgxC4FfRGEmUEhwnNAnXU0e_cypaFWg2lHF5oF1Q-7Tv6qjWEzxjeWCRb5zsomMNeMFwhLKTpE-KEAuQuNQ56IlFhbO0KXhdRQ0STT1MRfqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/124606" target="_blank">📅 00:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124605">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
الحدث: وزارت خزانه‌داری آمریکا اعلام کرد واشنگتن تحریم‌های جدیدی مرتبط با ایران را وضع کرده است که افراد و پلتفرم‌های تبادل ارز دیجیتال را هدف قرار می‌دهد.
✅
@AloNews
خبر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124605" target="_blank">📅 00:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124604">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رکورد تورم در ایران از زمان جنگ جهانی دوم تاکنون شکسته شد.
🔴
بر اساس داده‌های بانک مرکزی، نرخ تورم نقطه‌به‌نقطه در اردیبهشت ۱۴۰۵ به ۷۷.۲ درصد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124604" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124603">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHuGkvh33nqmG5tKBDT4kRfgez2oye91NUTi3YQUBPnKlw6kVn9kCOCmf1a5jp8ijiqM1PmGw8MMY2w4HSqty6oRS7Ifh7hJFeUXbeNNXywsTCNe6rfdW_Tiiux5cWlaG-i_d9seB444byZ3UaYVxx784LOVPlH39ArmJGveIeXDCS8frqSnsP-3woWJUAfKwRC-TkNPuY3l9LgEwlq2oZFGlmG9KOihQU9bn4mmNPpLXoxP8kE-V7xjMmf2Pl0vDOEQcILGBG5KDHo9tYxrBjduTE_AeIBOFfWWUBdc6uIiPyQTlAZIvU_LCoDXWEukwmvsC7xJi1O5rW4OTm89OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بررسی ورود سرمایه‌گذاری خصوصی به بخش برق ونزوئلا در مجلس ملی
🔴
مجلس ملی ونزوئلا قرار است اصلاحاتی را مورد بحث و بررسی قرار دهد که در صورت تصویب، مسیر را برای ورود سرمایه‌گذاری خصوصی به بخش برق این کشور هموار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124603" target="_blank">📅 23:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124602">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/124602" target="_blank">📅 23:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124601">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ریزش 2 هزار تومانی تتر در پی خبر تحریم نوبیتکس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124601" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124600">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a44b2aef3.mp4?token=NESBo-exC6naaufoYpw_EByKNWaAB9V_CDKSI12oTyHxnGzF0cwgEwONpJgQqV0XaxjWAE-NDwXueyCkDeMKSM8i5VGcnFHYQgfd6RPQ8wyTtyscKjGhlFrushBxpl6YbnXiLWhqvHGqf2lZGfeuBo769W08aIugEA1F-fYFwJpJzukHukNKSjDPG5g4kIJm_N829SJ_EHqPEHPW8H1qzCBA-wo05-k2NX1gOfYcdJLdj_UcfOhLxftM_x3IbtEVz3Hu1yF1q7eYy7bhd2lVxcaAp26jR-7UrTUGFwK9bm4ZsVLkJ8obj-GBaBG3pUHe8STXBdq14T-2_kqTUDA8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a44b2aef3.mp4?token=NESBo-exC6naaufoYpw_EByKNWaAB9V_CDKSI12oTyHxnGzF0cwgEwONpJgQqV0XaxjWAE-NDwXueyCkDeMKSM8i5VGcnFHYQgfd6RPQ8wyTtyscKjGhlFrushBxpl6YbnXiLWhqvHGqf2lZGfeuBo769W08aIugEA1F-fYFwJpJzukHukNKSjDPG5g4kIJm_N829SJ_EHqPEHPW8H1qzCBA-wo05-k2NX1gOfYcdJLdj_UcfOhLxftM_x3IbtEVz3Hu1yF1q7eYy7bhd2lVxcaAp26jR-7UrTUGFwK9bm4ZsVLkJ8obj-GBaBG3pUHe8STXBdq14T-2_kqTUDA8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : تیم مذاکره کننده با قدرت ایستاده تا آمریکا به خواسته هایش نرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124600" target="_blank">📅 23:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124599">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فیلترشکن گیگی
8️⃣
هزار تومان
😂
❌
فیلترشکن گیگی 20 تومان دیگه نخر
کف قیمت فیلترشکن
👇
3️⃣
0️⃣
💿
2️⃣
8️⃣
5️⃣
💸
5️⃣
0️⃣
💿
4️⃣
5️⃣
0️⃣
💸
7️⃣
0️⃣
💿
5️⃣
9️⃣
5️⃣
💸
1️⃣
0️⃣
0️⃣
💿
8️⃣
0️⃣
0️⃣
💸
برای خرید پیام بدین
👇
🔤
@MrTh_Vpn
🔤
@MrTh_Vpn
🔤
@MrTh_Vpn</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124599" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124598">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
میدل ایست آی: مالک برجسته کشتی‌های یونانی حاضر به پرداخت عوارض عبور از تنگه هرمز به ایران است
🔴
غول کشتیرانی یونان و مالک بیش از ۱۵۰ فروند کشتی: این عوارض می‌تواند «خسارات» وارد شده به ایران در اثر جنگ آمریکا و اسرائیل را جبران کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/124598" target="_blank">📅 23:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124597">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941e46de05.mp4?token=ajufrXcLXMwn9mMGyVw6vCVXWXj4-8mAAy10PnebiUg48LBOW95VKwI02kd_nalilAWxPVOw1EdGgeys-8vLIEdvO026LDGLtywp9ZqSjMGaJk0DM2JRp2CYE9tfKxh669c2MwuLuLM4E0o_Hf0BdKJK9czb_d5npsG0c8F1WK8LqwvrZPZKWVEfETdW5Lz7oV3xzel_o6g2F7B7idKMWri1gBbn7F8MW_exgtI2AxuLqB1UsAts3ke2ngnAro_H9Q2BO_7ZZVQRsNBnK703JSjzM7KAkqIug4rMjoGAeybiNlipgHk1wFgNA1LPpMiBJNImFKUJGvBR54bQ80QH7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941e46de05.mp4?token=ajufrXcLXMwn9mMGyVw6vCVXWXj4-8mAAy10PnebiUg48LBOW95VKwI02kd_nalilAWxPVOw1EdGgeys-8vLIEdvO026LDGLtywp9ZqSjMGaJk0DM2JRp2CYE9tfKxh669c2MwuLuLM4E0o_Hf0BdKJK9czb_d5npsG0c8F1WK8LqwvrZPZKWVEfETdW5Lz7oV3xzel_o6g2F7B7idKMWri1gBbn7F8MW_exgtI2AxuLqB1UsAts3ke2ngnAro_H9Q2BO_7ZZVQRsNBnK703JSjzM7KAkqIug4rMjoGAeybiNlipgHk1wFgNA1LPpMiBJNImFKUJGvBR54bQ80QH7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمود قیم، مداح: کوروش اگه سگِ آستان اهل بیت نیست،‌ پس خاک بر تمدن ایران باستان
‼️
🔴
پ.ن: محمود کاش اون شب بابات میرفت داروخونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124597" target="_blank">📅 23:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124596">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvUmp0mUz4NE5cGJICEFjjKYwlotF9YRoNxPOLYZ4SDSMbZVylbkdITyDnROEDGe55A07HGshevJQ372-JY2YETHhVbsoMX6PRbmBX4OWWOa7eoLOoO7tAqB3Er21SGvfDYpqnlqQZcb2MLm9gW-Y1k3LSwqRouZieCNuKVJXov68DEHDvUOgOhFKp1xdgZCn9Yl54HNwTQJVAE2KnIu4IvCsj9E9uuGn2y4gIJEaPxYPQChPGO4gI43Ua-6QxYosBDdf4bPQ7s1RS0t7XGJOI37UR37Qo3MtrNgPP2h6HEIB-lf8mN6fgCtW_iZHEDysN9dmrnAb9_C0ZbP4RfHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تسلیحات و پیمان ابراهیم؛ پیشی گرفتن فروش سلاح اسرائیل به اعراب نسبت به آمریکا
🔴
آمارهای جدید نشان می‌دهد تحت تأثیر پیمان ابراهیم، میزان فروش تسلیحات اسرائیل به متحدان عرب خود از میزان صادرات نظامی آن به ایالات متحده فراتر رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/124596" target="_blank">📅 23:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
یک سرباز ذخیره ارتش دفاعی اسرائیل (IDF) امروز صبح در جنوب لبنان توسط یک پهپاد انفجاری حزب‌الله به طور متوسط زخمی شد و سه سرباز دیگر نیز به طور سطحی آسیب دیدند، طبق گزارش ارتش دفاعی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/124595" target="_blank">📅 23:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آمریکا چهار صرافی ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس و 6 فرد مرتبط با اونا رو تحریم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/124594" target="_blank">📅 23:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
معاون قرارگاه مرکزی خاتم‌الانبیا :
اگه هیچ چیز هم نداشته باشیم، با سنگ به جنگ با آمریکا میریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/124593" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53317d490.mp4?token=H_1te19m6mWr5pz3P09HlXyJt7N83xpyUdNrB4cKp9ruGZ_RsXd2y9fXZ4qFOe-X2wi36fEMnXwY_cCFDq6c9NG-wNVJpXGTh1Zp0zCHFP1kO8DRi6euub0WZ7q-P70P2rbNk0_0WlwWNRpiQqzoWpn3ejWK2dxwGsRrSaJiUckZMDxrMo8nyQKF1p34GW9iEQTv4UlYhBV8jmuTfa0KfH-PGHztMIBNaBWPK040k5KnclgkHRl8A7Enx4NhXpvik6EWAXmKMawW5YEmvGUj2eH-OVtedDppQ1j3I4_2ZLyTWPAvzvTZk3Xy3P_i0Udd2ubHpkCH1b38CbPm1lG3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53317d490.mp4?token=H_1te19m6mWr5pz3P09HlXyJt7N83xpyUdNrB4cKp9ruGZ_RsXd2y9fXZ4qFOe-X2wi36fEMnXwY_cCFDq6c9NG-wNVJpXGTh1Zp0zCHFP1kO8DRi6euub0WZ7q-P70P2rbNk0_0WlwWNRpiQqzoWpn3ejWK2dxwGsRrSaJiUckZMDxrMo8nyQKF1p34GW9iEQTv4UlYhBV8jmuTfa0KfH-PGHztMIBNaBWPK040k5KnclgkHRl8A7Enx4NhXpvik6EWAXmKMawW5YEmvGUj2eH-OVtedDppQ1j3I4_2ZLyTWPAvzvTZk3Xy3P_i0Udd2ubHpkCH1b38CbPm1lG3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز شبانه جنگنده‌های ارتش روی کرج، استان البرز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/124592" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
طبق گزارشات منتشر شده،مصرف دخانیات تو دخترای ۱۳ تا ۱۵ ساله ایران نسبت به سال ۱۳۹۵ حدود ۱۳۵ درصد افزایش پیدا کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124591" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مدارک_مالیاتی_موسسه_محسن_سازگارا_۲۰۰۶_تا_۲۰۲۴_.pdf</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/alonews/124588" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/124588" target="_blank">📅 23:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124587">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
در تاریخ ۹ خرداد ۱۴۰۵ (۳۰ می ۲۰۲۶)، محسن سازگارا در اتاق «طرح نو» کلاب‌هاوس حضور داشت. او در پاسخ به یک نقد بی‌پرده، مطالب و ادعاهایی را مطرح کرد. او در صحبت‌هایش صراحتاً ادعا کرد که در تمام طول عمرش، از هیچ فرد، سازمان یا دولتی فاند دریافت نکرده است.
🔴
اما با بررسی هایی که در رسمی‌ترین اسناد مالیاتی ثبت‌شده در ایالات متحده، واقعیت دیگری را نشان می‌دهد که با این ادعای کلاب‌هاوسی در تضاد است:
بر اساس فرم اظهارنامه مالیاتی ۹۹۰ مربوط به «موسسه تحقیقاتی ایران معاصر» (موسسه‌ای که سازگارا خود از سال ۲۰۰۶ رئیس و امضاکننده قانونی آن است)، این سازمان در سال ۲۰۲۴ مبلغ ۲۰۰,۰۰۰ دلار فاند مستقیم از دولت آمریکا دریافت کرده است.
🔴
طبق اطلاعات درج‌شده در صفحه ۹، بخش ۸، خط 1e این سند، این مبلغ ۲۰۰ هزار دلاری به طور رسمی و قانونی تحت عنوان «فاند دولتی» ثبت شده است.
🔴
این سند رسمی که تحت جریمه شهادت دروغ به مراجع قانونی آمریکا تحویل داده شده، ثابت می‌کند که موسسه و فعالیت‌های محسن سازگارابه طور مستقیم از فاند دولتی تأمین مالی شده است. این پست با مرور اسناد رسمی، نقض آشکار ادعای اخیر او در کلاب‌هاوس را اثبات می‌کند.
🤔
محسن سازگار تاسیس کننده سپاه پاسداران و از همراهان اصلی خمینی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124587" target="_blank">📅 23:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124586">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تحریم‌های جدید آمریکا علیه ایران
🔴
وزارت خزانه‌داری آمریکا روز سه‌شنبه اعلام کرد که تحریم‌های جدیدی علیه ایران اعمال کرده است.
🔴
طبق بیانیه دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک)، چهار فرد و چهار نهاد مرتبط با ایران، به فهرست تحریمی آمریکا افزوده شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124586" target="_blank">📅 23:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گزارشاتی از فعالیت جنگنده های ارتش بر فراز کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124585" target="_blank">📅 23:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh8FVKXAXUqaPPqVJveQ8BKDZuCOHe-IsSmtsf4MnLo_aoAkuvbAW1p1qkwLB4lkKtnVgvkZj1a-S99KBewaDbGErcQAP4cacWByVXrD7Tru23cBtzrob7v0_d9Kdz3JFIKLLFBG92F8wE1p9BBQ2jsPT8esNQEAOQObc-HoL9lGXjwaece4aUtER0KFJnkW4zbrYLSJMikSX0_9ju4jN8iX5E2VEz1jQAPi2HzASa85f8msTNPNG4tGqFnwVILJfxziHBmx8Y8KQMjO89bMKvCvy9k8zHMgE2FYeEzvIVWZeQwRuHFocEpxeQVZDrt1fmennqSxOcOuv8iG-7C6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه توسط تلگرامه و دست ما نیست و  کلاهبرداری هست و فریب نخورید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124584" target="_blank">📅 23:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/124583" target="_blank">📅 23:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124582">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c91c418d.mp4?token=BwaEsOBnnIQZFAnNZq9d9GqLOThPnhjbUaBPaIOZaEI0rp9OaFC0g2FzSISi77b3MOhjy_QZ3GDHfY1ssaeCYMMyZj3mINzdh9XTybZDcF0emKpCDRdiGDhu6mPz9zl2F9aVp6BS7d3R4G7BUcz3ludfmuMvSNuzXKuVtFnIqg8mL_N-yqFFtbq7nSEGDeoqm9lTK2-uL60BT3vI3qVl3b9QJvdgXMaYJ3BrRYtBlVs8vxYkcNxlQcoqT9MhAHcIbD89kRN8ejdLTYmVXyVxE7HVPNTExGPc4xuAQX2U748AD84abUPkecR7C3c7ZIrV6aIRhIwRy1z35tcXsUO3eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c91c418d.mp4?token=BwaEsOBnnIQZFAnNZq9d9GqLOThPnhjbUaBPaIOZaEI0rp9OaFC0g2FzSISi77b3MOhjy_QZ3GDHfY1ssaeCYMMyZj3mINzdh9XTybZDcF0emKpCDRdiGDhu6mPz9zl2F9aVp6BS7d3R4G7BUcz3ludfmuMvSNuzXKuVtFnIqg8mL_N-yqFFtbq7nSEGDeoqm9lTK2-uL60BT3vI3qVl3b9QJvdgXMaYJ3BrRYtBlVs8vxYkcNxlQcoqT9MhAHcIbD89kRN8ejdLTYmVXyVxE7HVPNTExGPc4xuAQX2U748AD84abUPkecR7C3c7ZIrV6aIRhIwRy1z35tcXsUO3eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: بگذارید بگویم ونزوئلا امروز آن جایی نیست که ما برای مردم ونزوئلا آرزو داریم.
🔴
اما در مسیری قرار دارد که فکر می‌کنم اگر ادامه یابد، بسیار مثبت است و باید ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124582" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124581">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بانک مرکزی اروپا اعلام کرده است که طلا جایگزین اوراق قرضه خزانه‌داری آمریکا به عنوان برترین دارایی ذخیره‌ای جهان شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124581" target="_blank">📅 23:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
الجزیره: ترامپ ترمز نتانیاهو را کشید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124580" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هم اکنون پرواز گسترده پهپاد های اسرائیلی بر فراز بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124579" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7472ed86c9.mp4?token=J8Proaoay-2GMSpeE6_mryo29NbPEdW9Ies-SmTiEgJfxPFwXRBUSr4JPo9JUL3mPAEVvBvuifmIIi8Y7-cNWwcT-MEGCUTWcZJt4J08thX8oAGmWP2DVtB4mKr7L_Dt1RWetKyXR0TSM4Bf-j-lqCdYTFxmT0yqZhVTgjj_I_JvwCmJkxGqCrd-Vkr3ElEY9U2vfsRHC7ZI88Yk2VO1yz0ZnQ63IPe4WR-UWD5hYd89cx4pO8q7rWWvWjf5Kpe_oex9ZMrch7Tx7uxIqeFPp-iLiDV4uHtihxzQ6LHt4mmnjvR0TSN-vSisu6U5oqJolMJs2V9DK0w8hTWWspv2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7472ed86c9.mp4?token=J8Proaoay-2GMSpeE6_mryo29NbPEdW9Ies-SmTiEgJfxPFwXRBUSr4JPo9JUL3mPAEVvBvuifmIIi8Y7-cNWwcT-MEGCUTWcZJt4J08thX8oAGmWP2DVtB4mKr7L_Dt1RWetKyXR0TSM4Bf-j-lqCdYTFxmT0yqZhVTgjj_I_JvwCmJkxGqCrd-Vkr3ElEY9U2vfsRHC7ZI88Yk2VO1yz0ZnQ63IPe4WR-UWD5hYd89cx4pO8q7rWWvWjf5Kpe_oex9ZMrch7Tx7uxIqeFPp-iLiDV4uHtihxzQ6LHt4mmnjvR0TSN-vSisu6U5oqJolMJs2V9DK0w8hTWWspv2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلی اتفاقی علی جوانمردی معروف به علی تجزیه که مدعی آزادی برای مردم ایران هستن، بصورت کاملا خواسته در راستای جمهوری اسلامی که بیش از 47 ساله مردم ایران رو به گروگان گرفته صحبت میکنن.
🤔
حرام زاده های کراواتی رو بهتر بشناسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/124578" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=Am6JZrTNsjLxdvJXqwqoNGuqCqCjzw0HHFKw9J2ltiXQEKRjrYHHTfKauNpr6xi9JtA_dAQGY3RtYJUZkBm3AibPqcHRrGm_yW8w9eNHJbVjyCDZbOj930ZZnLbsWWwYccPEVdItQXjrnj5Zj7AYKTIKt9V5w3DB2MuIP4RyoAzs6wr4q9IVq93Ejec3-QF7bfZINLVbUdq4FAv1i3atmhdwrqM3pbFisZXeSYMboLfK6QN4ZVJ_2Z5udt5HbpyA9QVD7TyU-yzXfn1nJJTYMme4weaKdZWgLOb9CUVMWhCLCkxP3kvvSOML8RRMiy3M4Fe8b_V50SciGYz_6hDGIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=Am6JZrTNsjLxdvJXqwqoNGuqCqCjzw0HHFKw9J2ltiXQEKRjrYHHTfKauNpr6xi9JtA_dAQGY3RtYJUZkBm3AibPqcHRrGm_yW8w9eNHJbVjyCDZbOj930ZZnLbsWWwYccPEVdItQXjrnj5Zj7AYKTIKt9V5w3DB2MuIP4RyoAzs6wr4q9IVq93Ejec3-QF7bfZINLVbUdq4FAv1i3atmhdwrqM3pbFisZXeSYMboLfK6QN4ZVJ_2Z5udt5HbpyA9QVD7TyU-yzXfn1nJJTYMme4weaKdZWgLOb9CUVMWhCLCkxP3kvvSOML8RRMiy3M4Fe8b_V50SciGYz_6hDGIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو در جلسه استماع کنگره مدعی شد: اکنون ما افرادی را داریم که در آمریکا به‌جرم تلاش برای ترور محکوم شده‌اند و یک نفر هم دیروز دستگیر شد؛ از مأموران ایرانی که درحال توطئه برای ترور رهبران سیاسی، از جمله رئیس‌جمهور آمریکا بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124577" target="_blank">📅 23:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / روبیو در کنگره مدعی شد یک ایرانی دیروز به اتهام تلاش برای ترور رئیس‌جمهور آمریکا دستگیر شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124576" target="_blank">📅 22:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا از اعمال تحریم‌های علیه ایران خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124575" target="_blank">📅 22:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjHdVFuxu2S7EI6U6lVw9-gWMm00Jy8BHAlIsJSw55Ti-_7zworU4-KTRfUliKAyAtYzvONHfFfEGeAjkPuFU057J0eRCEx6nuU2RCKNJwhTMaMhY6_IqBpThSB4Nk6TPVRebig3gUA_yWjQCoLhHKIK3_lZW27O63OiOAzgYB6_k46ZqWY3defQlYvGiTZHQO9uhGG2WmXCUAwCJ4s8DzPYX_vUCchRyo3x0FXx20V0p8wUel7yVTTsF_LV_MOXp6j0mHScspG9qXDM2WMPokDjihdLIkB2NlE5QVkvnWybSKQxS3QvFRzSHW1e4OPhsigD0rLwZMt8LlaWIT2Hxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/124574" target="_blank">📅 22:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db5c6e8c5.mp4?token=qvtAWRCO3vIi8QdOWBr3fgd73Y9w_vHIBrqhrpcYLhJ-609NpKLU9qMq-9vnpeNqlPY9vFQZSl6iKe3gNbhHzqFDBRQZYmLTF9df4Vm9K7O6bZojSqZeZJpTIphVKjFHGlI-achUriNHBazV92EgaDv28NaxcL0V7ufNyb_NJIIwaa8F2zf03HxaeCQ5YHwsdtk-CfpTv7qBnkoxcdf-NdhF7lwHVUGibDFzmbPEnIqrTN6NOjoQBUS7vbbFlgacloP42TNvIs7E15fnWnT12MnNVv-0RXySDdZQ-d0x1BpGiLrYz23bwfDKXAEWZK-1rrnSupg40NdVA8Ht7ahx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db5c6e8c5.mp4?token=qvtAWRCO3vIi8QdOWBr3fgd73Y9w_vHIBrqhrpcYLhJ-609NpKLU9qMq-9vnpeNqlPY9vFQZSl6iKe3gNbhHzqFDBRQZYmLTF9df4Vm9K7O6bZojSqZeZJpTIphVKjFHGlI-achUriNHBazV92EgaDv28NaxcL0V7ufNyb_NJIIwaa8F2zf03HxaeCQ5YHwsdtk-CfpTv7qBnkoxcdf-NdhF7lwHVUGibDFzmbPEnIqrTN6NOjoQBUS7vbbFlgacloP42TNvIs7E15fnWnT12MnNVv-0RXySDdZQ-d0x1BpGiLrYz23bwfDKXAEWZK-1rrnSupg40NdVA8Ht7ahx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: این گروه‌های تروریستی خشونت‌طلب، مارکسیست، چپ‌گرا و رادیکال که در بسیاری از کشورها فعالیت می‌کنند، برای مثال سال‌ها کلمبیا را بی‌ثبات کرده‌اند و دیگران نیز سرمایه اولیه خود را از کوبا دریافت کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124573" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124572">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9227ec9400.mp4?token=TKCPr7qybuaoUTL4aQEi0QcIP04UIjdjy5rDg4T2rU6p2xBPl3d7l9uknJXwbdvLZwDZCQu0N85Ey19d3knXRj226r2zEptMqsS7ACkJ6gw_-BdFSvv2TblaesJyZvEAmbRo_TiRkTxwT7kT7QigGkXx63Up4Ug5P56uXPqFXudKkDiD4LoZFWkHFtyRy0V4H_INeTraQkxrdTPJHR2YVNIAnnNz3FT55rMmZ-6tESRIrBT2LtVbfUCgSnRkpw6PeV5zHSTN67BQ_hYZhrr6M_Ab-PiYXNjcZS0I9g8UiH0QEfLqIAxG5bJPf3qrP7jyw7dxePVwX8uXhYwEGG4gxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9227ec9400.mp4?token=TKCPr7qybuaoUTL4aQEi0QcIP04UIjdjy5rDg4T2rU6p2xBPl3d7l9uknJXwbdvLZwDZCQu0N85Ey19d3knXRj226r2zEptMqsS7ACkJ6gw_-BdFSvv2TblaesJyZvEAmbRo_TiRkTxwT7kT7QigGkXx63Up4Ug5P56uXPqFXudKkDiD4LoZFWkHFtyRy0V4H_INeTraQkxrdTPJHR2YVNIAnnNz3FT55rMmZ-6tESRIrBT2LtVbfUCgSnRkpw6PeV5zHSTN67BQ_hYZhrr6M_Ab-PiYXNjcZS0I9g8UiH0QEfLqIAxG5bJPf3qrP7jyw7dxePVwX8uXhYwEGG4gxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: ما پیشرفت‌های چشمگیری در نحوه ارائه کمک‌های خارجی آمریکا در سراسر جهان داشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124572" target="_blank">📅 22:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گزارش فایننشال تایمز حاکی از آن است که ایالات متحده در نظر دارد دارایی‌های هسته‌ای بیشتری را به کشورهای بیشتری از ناتو در اروپا مستقر کند.
🔴
گفته می‌شود لهستان و چند کشور بالتیک علاقه‌مند به میزبانی پایگاه‌هایی برای هواپیماهای دو منظوره‌ای هستند که قادر به حمل سلاح‌های هسته‌ای هستند.
🔴
انتظار نمی‌رود به زودی توافقی حاصل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124571" target="_blank">📅 22:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/de870dace2.mp4?token=ZSYmid2yR_cLTBqbo_Ji6jrBmTFYZfD8aqps5bzyhCR2H8XVnhJAJdBHu43u9T0EhdrDGtx27HtgEiqD05Y2I8-L_edUHj8i1HSKQfpwINK_LMBCG1VniMKx3E0S8pNdDcWw3cJysI3uYDrZ9Lltvx_zFytcX01ebJF3aD2UYtXZxEiOaGsZx3Jgpj6BAkvnbdl_G-y9X5mZTZ5PWh-R4OUUDWWsXeuXwTYYc2iz-iCHzrb_ET5ZHD0_qUbE_7wneQnMGQqBOirya9OrLXXbimjYM0ykalxBdAsWsl9Uh5GdJvxW1_REjOPCFZDkaUw_G6qOdwZ7mwIttbD3LxUEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/de870dace2.mp4?token=ZSYmid2yR_cLTBqbo_Ji6jrBmTFYZfD8aqps5bzyhCR2H8XVnhJAJdBHu43u9T0EhdrDGtx27HtgEiqD05Y2I8-L_edUHj8i1HSKQfpwINK_LMBCG1VniMKx3E0S8pNdDcWw3cJysI3uYDrZ9Lltvx_zFytcX01ebJF3aD2UYtXZxEiOaGsZx3Jgpj6BAkvnbdl_G-y9X5mZTZ5PWh-R4OUUDWWsXeuXwTYYc2iz-iCHzrb_ET5ZHD0_qUbE_7wneQnMGQqBOirya9OrLXXbimjYM0ykalxBdAsWsl9Uh5GdJvxW1_REjOPCFZDkaUw_G6qOdwZ7mwIttbD3LxUEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی سازنده جم تیوی و فیلمای ترکی پشماشون از این کلیپ ریخته:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/124570" target="_blank">📅 22:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33ad08024.mp4?token=doBonkx45Wea7SYjkuc58RtYsK2k8dj0rw_XOzKevE3PKJvmMIEuRJHb7N1mfM4aireBklWwlRSbYftjOn8ICgCVRqhli7dzNQEycKDbQ68aOEPBCmyZdohW_FjGzdiZb32SLRHNjyKzYMfuYTKa3F6XvJwKRZzKK02UAeZl48kVyS8B6ETve4ffPUdypZyZqm69spROYcGaGKKgU5boOEvuyEKhOhaXCXSJ-VF6SFJ8u9IctuwfDDgnuF09aI5mkuDJkR816mW-Fn22YeWtq-pV_bsOcy_E21tODBmtnQzVhuUXw-WCeSjaCYjLUC6ZGOBuQTPzrCKTBo4a24c3ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33ad08024.mp4?token=doBonkx45Wea7SYjkuc58RtYsK2k8dj0rw_XOzKevE3PKJvmMIEuRJHb7N1mfM4aireBklWwlRSbYftjOn8ICgCVRqhli7dzNQEycKDbQ68aOEPBCmyZdohW_FjGzdiZb32SLRHNjyKzYMfuYTKa3F6XvJwKRZzKK02UAeZl48kVyS8B6ETve4ffPUdypZyZqm69spROYcGaGKKgU5boOEvuyEKhOhaXCXSJ-VF6SFJ8u9IctuwfDDgnuF09aI5mkuDJkR816mW-Fn22YeWtq-pV_bsOcy_E21tODBmtnQzVhuUXw-WCeSjaCYjLUC6ZGOBuQTPzrCKTBo4a24c3ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در یکی دو روز گذشته کمپین «ایران ارث پدری ماست» رو همگی دیدیم.
🔴
حالا بشنوید از پادشاه بریتانیا در سال ۱۹۹۳: «اسلام میراث ماست!»
🤔
آخوند انگلیسی که میگن همینه که ما تو ایران داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124569" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eeaf331dd.mp4?token=fk9YItFgGtf_cQKZFpY8HSCR3fKYbFSM1vBzckICpCSjnpv0uXKxKClUZZHA3tfob3xE_91H2PBbqbwOJ4De6gzfFyquPyx5mJ3bNeu9kAz2OQrkCR511L0aJXQYNF8UWFn2oGFrTeyba5j4xXoyVQ-DxH9KmB5MpDCukj5gdXqN58ZcQi8jAhHXv-lUjDAlksO5JpXnt8tke0VblCqWCx-S5DHj_i8ljp70_djFxf5QlWRYHw-waLaDO0xF_VKdOPIB-gU2hEhsfefA6XWTn0kA5JEUAwgrbKhGmyWroOwchn91PzrOB2wVg4vXO6jj2DGiwxCuKeiNDRTTNsfpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eeaf331dd.mp4?token=fk9YItFgGtf_cQKZFpY8HSCR3fKYbFSM1vBzckICpCSjnpv0uXKxKClUZZHA3tfob3xE_91H2PBbqbwOJ4De6gzfFyquPyx5mJ3bNeu9kAz2OQrkCR511L0aJXQYNF8UWFn2oGFrTeyba5j4xXoyVQ-DxH9KmB5MpDCukj5gdXqN58ZcQi8jAhHXv-lUjDAlksO5JpXnt8tke0VblCqWCx-S5DHj_i8ljp70_djFxf5QlWRYHw-waLaDO0xF_VKdOPIB-gU2hEhsfefA6XWTn0kA5JEUAwgrbKhGmyWroOwchn91PzrOB2wVg4vXO6jj2DGiwxCuKeiNDRTTNsfpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تئوری‌پردازی فاکس نیوز برای شروع مجدد حملات اسرائیل به لبنان با چراغ سبز ترامپ/ جک کین، ژنرال بازنشسته ارتش آمریکا: دونالد ترامپ هر دو طرف را متوقف کرده است. حداقل به یک توافق شفاهی رسیده‌ایم.
🔴
می‌دانم که اسرائیل به آن توافق پایبند خواهد ماند.
🔴
از ۱۷ آوریل به بعد شواهد زیادی داریم که نشان می‌دهد حزب‌الله چنین نخواهد کرد. و فرض من این است که اگر حزب‌الله مثل گذشته این توافق را نقض کند، رئیس‌جمهور به اسرائیل چراغ سبز نشان می‌دهد تا هر کاری برای دفاع کافی از خود و همچنین انجام عملیات تهاجمی برای از بین بردن این توانایی لازم است، انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124568" target="_blank">📅 22:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نتانیاهو تا چند دقیقه دیگه یه جلسه امنیتی برگزار میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124567" target="_blank">📅 22:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گروسی: به دلیل جنگ و هدف قرار گرفتن برنامه هسته‌ای ایران، ارزیابی آژانس تغییر اساسی کرده و بسیاری از فعالیت‌های هسته‌ای ایران اکنون متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124566" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrhYKEip1k1BUGWTsGfJ9nvW5KdXshBClUEIosZJk4Sxtj2p6pFUQvE6l35a3jdE6J6-PPYr8ktRWADGiAYZWDHaKtyuLnXrGFDG3WQ3Zo0FMwiWvoVEXaR5lIyWleijZKv0FGH9oQbIWFg42ltIE945SK9deOsu0Buj-29Mnz4ZjEP0E08Z8oJL7m1kVxXYiHTsfeGGg178I78gLr_88ngRGCMRkswKwLbaFqWsrtakvkeB9w4E7iguscHl5nIADrWBRkBPeTAWn9gtY1vwgqnrv79lN1urIsjUEyJ-hhi4joKfxekfVi_wy2paCMaav9AXYsyGBC2P4HlyYmC3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشت نفر کشته و ۴۲ نفر دیگر در مالی روز دوشنبه پس از برخورد یک اتوبوس با مین زمینی در جاده بین باماکو و کایس زخمی شدند، به گزارش رویترز و به نقل از یک مقام اتحادیه حمل و نقل
🔴
انفجار در منطقه‌ای رخ داد که جبهه نجات ملی برای تغییر و اصلاح (JNIM) همراه با جبهه آزادی مالی (FLA) فعالیت می‌کنند.
🔴
هیچ‌کس مسئولیت گذاشتن مین زمینی را بر عهده نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124565" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHB3ipnsPrBg1AjIk5bzMxgn1FA-oZ8zSoe2wJPnnESeQZH8LSFhA0exF0pGJZTu1YlL2dYCPpEnteLgy0WLikCPgViH1juA7p2oSjLAGplx1M7fudarwK8yzC9ol4esVMVm8lIN9I0Y06KqXlS_t3sie7YJY3uOLX6SD56G3-GFsWfdG6-HCLKlmHrbScaxW3b8gO1Cosu3ya43cDI36K82RXqbXtgL5z0s0Nhdtrsim_JtFfeC2hBMgEEe6rV0zS59iq7TDUDmCviKKCD-GNFCfuQf8OD7qgrRzHVdXGoBlYoMar_9WA61zU9t8O9H2-kOqBI87kxRQHyNcdzHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
داشتن فلاویو بولسونارو در دفتر بیضی کاخ سفید بسیار خوشایند بود — جوانی باهوش که کشورش، برزیل، را بسیار دوست دارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124564" target="_blank">📅 22:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر امور اقتصادی و دارایی: تعیین مالیات مقطوع صفر برای بیش از ۹۰ درصد صاحبان مشاغل که در سال گذشته با موفقیت اجرا شد، امسال نیز تداوم خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124563" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روبیو: امارات و کویت در جنگ علیه ایران فعالانه و جدی با آمریکا همکاری می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124562" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124560">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdEzjdlWDZY22lGqgPk4VWRrELa2NvbO96N13g1VNQ3X4t5p6S9E0VN5JLcmFiFFrIkKYQbrKGyiG6w5ozjluV6zHdBY4gzyk3jOxX_y2z_-UEZV5hc22PRjmBB9B69sRGlVeSR89a-_TqR083PRnzVFMFrGCswrn36iof8WQ14Np0DysSfU8x6PRtgM9Us8l4JvBZqvI12EJuGKM3TZwZ-rcYBEkuS4QUtvOvqQc7dbBI6LjdlENsqcn_QU7yi9Rcs2dJP-0HC4vqZuvIeRzgtIm9Xe-ZJmBILJomaqLKhZNZ_oni1LcFYuGVff78eMiXLueYwR2Ll3iJyZ8vHzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو «یو‌اس‌اس باکسر» (USS Boxer) که مدتها قبل به منظور عملیات آبی-خاکی در ایران اعزام شده بود، علی‌رغم انتظارات به دریای جنوبی چین رفت و از منطقه دورتر شد
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124560" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124556">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up-M2F9o3WKWKhGh2Dk7LZdV7OGY4PmxJOdu0-I5WAppSemfnfCEfZwO3Q3edeIl37ybzPTt72plnGgZ6pBIJFZdJVnMghAktEljKZd2-XWedeBnYQg3eEydwPaoJvlel7e6lGsbSzmGIJVLFodRKrWi0ZdOF0Ler_zxc9xUgoTHSjglMivm8Ebfpe3NRP9QCIyhuM_oknnQFrZaHxJ9RmVqAsHd-RGJhuqfv4ottSUpOOHIulnZD7wXFLsi7weI3gu2jpa6ibwabE54xCL9lVI-AzfrI-QkXprdwCx5ovs915P-ssSbrAVmNaNjdgfVsu0OMfk_38--O5gCBDl2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSqPun52NOc90GqkZ4R9ADVIAoaUa3HpfU5JaK2zZbA_YcpA7v1rFAfVANDKJIFfPpu4exw_esfUALBhKLW_f_GIzf6aBAh1pgdl6N36TuxfoPtG1I_8YN_XKQoQtutJb56j7RIPjeHD1LKib2_xX6CFlW_Lz51WYqsCUUEELF1ZjY2t0MCH3aqPCDcv9zs2JrsdehZQqTFJNi6XRlPxpr3yVcUbjEWqPtbwY8Gs3IpHaxOYwdZ32qvoMvlnV4dd_BElDwXjp-A5gmUfMdH_UyCshAd67p3I-LDzn2NX_EU64SEC9EmGnky1eEe8hmaEAA9z5LFFC2ECIghL2GEN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5IJspip1DiQ25nmgPHvK0nU98E_8QqLaoKfUk9n9rjbo51PHB_k2KseHcVrLGPnWsiqilAn9ndRYXgjALu-_ffpPWs37MlhDfeukAx21bpp_QxhgKZBYohTTgKDqvE3uWdC5QYI2WF2lUSDRMFztVJh5gfb4rinVgbjKBIHuh5cZcN3Tiv0eCOVxjCNCoqjO46UCIGYJvgdmjSIhqnqjPUqFtW7PRkFaR2Zn5pGjrxWLRHVgE8a_OaiChBr781IICthYgFkkVrby15-rFxySyg_h-CbgzAYOAolZFVYx7_28NI97ELLVdlpfuNgu9Co6PLTWNEJxpAJa3BFytcRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgYya8dmwNVbynCiRwgmqak-QLcGfN7emjHBfggC3yAF5Pz9rrPXRVbfIhLbOyxcQ82BoDvGXnVil-27yY9Djv0lYohc8qgDTWKLGjoJM0afSd7h-jtAzjdvA6MRIloNSCr2THzlLRp0OiPVLcYl2RZm3DRt4DYeamKsNWORAamK2vMfgOfZT204P7XXwlRRFtNh6f358A5K4ZPABTbs82e3mfwEG-CdxSqFXSsRLu6_wcOaPiVNwKCq6iH06kqERtof2SuuswCttxReekQ787Gk-4MCV6b27vyoT3s7LIEocE-4eqJnHfCkNqy8xdI82ExlYpw7FSy9Rj-HV06Pbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
🔴
تمرین همکاری منطقه‌ای ۲۶ دیروز در قلعه هریسون، مونتانا، با مراسم افتتاحیه و یک دوره موانع آغاز شد.
🔴
همکاری منطقه‌ای بزرگ‌ترین تمرین آموزشی فرماندهی مرکزی با کشورهای آسیای مرکزی و جنوبی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124556" target="_blank">📅 22:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124553">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zi9-dRzN2YONANQK4o2XlfQUQU-_gawiozOuzJxJ1n3aCYqOTi_2OD8xpuDJWKn3nRY0KR2DHJsYJVYrKIUDNYt8kMyiu9TTok5EJMNMJJ2s7M0Vm2F5SJVNabvoZdrsw6Ifl2u0Plm3FT71IBu1N6jsWgYgt5fjIhm8F1yv9QzDUlHBYU_7C0Z1NjSn08EvYk66V_wmKv-DzMI2W2z96bK5YwJInzudW1-hxYHDYcSyeqwZejGVrc7R9PrHDEpHApuMSbI4ujGIF5_tlIMJ21v6z9PtDea86ol6z_tOj0rzNpeuuCofhX3PF7l8msVifwG5Sfr_QcGM58MvzVj1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miTlXui8kusGjDwpLwAUZMmnH9Jxfl2mDUs2UA52lr1hEmwBuRSh9doQ49F648VDC-KDnQlr1qrH-cs5mRQttz7btR_2V8c6cI-wUYtQA_Uk3Std0Dg3t-sqBl5hnjekBuamww0azc5VacnkjbbN6wp9PjzpQilEUqF2aT4aqTgB0zDBkwBOiFQpa185IAYVkU9SvZ5JTmbTZNMkEERyi4Vf1KVx-x6qcm0ofdWRuGNwcObNHNkWQZTVQ3UrApTlBxPEezPprBHD_XdMDP01mcTyjTceCGKL9hgOo68MfNbmeqhEhk3aWrRHg-LeLo_W53X00lWcujD46HbwIvQOfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823f2337f3.mp4?token=eLr4cLJ69CZYGwP_vKD1xU95t9RfW5FB3DNjdGcd92wlCtud9J7yM3jzrS8BMjd-AuWvsP0QqpZM7VtYazxDkbh6Ff9LACh3_rY2XjkPK1YCeFWf5Pqa71S6YwTTZgwVCJkjVhPWcw1CuKsk6mDaqhU7CsPLok2ygWq5_6-FJciy32tHsg_6H-KBVOWYLcxfHwC_UPAM4KbA_z_8RLT2_f2V97mLuMv7tARs6xOyi-esn1a7EGHnKKPGKaUkxl8yhlkG9Or2eBOnA4oOiQx0dNsPNb-32apRBdpqoant1nNGV9DYH7Sw_Nuz2eJZiajzRa-Zzn2hSzzVDjxQbP9SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823f2337f3.mp4?token=eLr4cLJ69CZYGwP_vKD1xU95t9RfW5FB3DNjdGcd92wlCtud9J7yM3jzrS8BMjd-AuWvsP0QqpZM7VtYazxDkbh6Ff9LACh3_rY2XjkPK1YCeFWf5Pqa71S6YwTTZgwVCJkjVhPWcw1CuKsk6mDaqhU7CsPLok2ygWq5_6-FJciy32tHsg_6H-KBVOWYLcxfHwC_UPAM4KbA_z_8RLT2_f2V97mLuMv7tARs6xOyi-esn1a7EGHnKKPGKaUkxl8yhlkG9Or2eBOnA4oOiQx0dNsPNb-32apRBdpqoant1nNGV9DYH7Sw_Nuz2eJZiajzRa-Zzn2hSzzVDjxQbP9SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
عرزشی‌ها ،عرزشی‌ها را پاره کردند!
🔴
عرزشی ها، عرزشی‌های مخالف مذاکره را کتک زدند و پلاکارد گفته خامنه‌ای را هم پاره کردند.
🔴
چند عرزشی در تجمع شبانه مشهد از لباس شخصی ها کتک خوردن و حالا قرار شده موافق و محالف در میدانهای مختلف جنع بشوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124553" target="_blank">📅 22:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
احتمال وقوع سیلاب در ۱۱ استان کشور
🔴
سازمان مدیریت بحران: احتمال وقوع بارش شدید، سیلاب، تگرگ و صاعقه در ۳ روز آینده در استان‌های آذربایجان شرقی، گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی، سمنان، ارتفاعات تهران، البرز و نیمه شمالی آذربایجان غربی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124552" target="_blank">📅 22:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124551">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فرهنگستان زبان فارسی: واژه مصوب قدیمی «دوگوشی» برای هدفون دیگر کاربردی نیست؛ پیشنهادهای جدید مانند «نیوشه»، «شنوه» و «آوایار» را بررسی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124551" target="_blank">📅 22:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124550">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/گزارش ها از درگیری شدید مرزی میان هند و پاکستان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124550" target="_blank">📅 22:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124549">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124549" target="_blank">📅 21:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی دولت : امتحانات نهایی دانش آموزان و داوطلبان آزاد ۱۳ تا ۲۳ تیرماه آغاز می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124548" target="_blank">📅 21:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124547">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFMSNrSVTEILvQVqJwT5YdM8Tsb-kCXv9GrLSIvVW9-twx2eM3rG-r0hpfSdb0Vi-AvNKJa76pu021xU1e6ql2gGf1_osN7JPfsRgVYeISihZ25Ws13A4etp74aQZ39ouQfeqZNEMRqVWM4VN4A0eRFXW6FcT8aNRI3xeTxt0WcrhMgPKKi7kzZcLIaUtf4AyUZo1purdL1buPpdSrfNuyFcbJUul9I1s8kGhgG6Od9eK-i3Zqyzuz3eeWSXUb1e_0tjmRf2qk7pFotuf-EPbI5vA1AHvqlclsvNVaYeuJPxOWEjNll-Mn8ujgyGlQetT9KTCtu7PDbVPiS1M_wRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک املاکی دیگر جایگزین تولسی گابارد شد !
🔴
پس از استعفای تولسی گابارد مدیر اطلاعات ملی امریکا ، بیل پالت مدیر آژانس فدرال تامین مالی مسکن (FHFA) از سوی ترامپ به عنوان سرپرست اداره اطلاعات ملی امریکا انتخاب شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124547" target="_blank">📅 21:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124546">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COxXAiH7hnbE6i4gELu7wnboJQOsjkuY1DAKNUphu5Nk49TtdfV-RaTxke4VrEIy8U4zXfVet8q-5nTC9jYDSe9VdUGq7OhwWOuVsk0QYUKCOkF8mZU44A3VkUTVN-YQHS2ecFl2Bddq6N-6Zd7-KgQuY9aolCfsFGmS27ePRdrj5_B-iumqnbPmPn9u2CVvZqJcGXGF5cLKaXodjF3XYu11wG-ES_wvc-hsmDgANqB3KhADMeY_OGLDlmuQar-nTGgEMuKx_3wwW2kkPmBJHLaNjxUIeJ0dPI7PUYEsjtt89XhamuX6KmX5SR5bQpBp7LsxnL8FnVsy8vL34LcCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده مختاری، خبرنگار:  قدرت خرید مردم با سرعتی بی‌سابقه در حال سوختن است و مقامات با بهانه جویی درباره فقط جنگ ۱۴۰۴، واقعیت ۸ سال سیاست‌گذاری غلط را سانسور می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124546" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی (IAEA) اعلام کرد که انعقاد هرگونه توافق با ایران بدون سازوکارهای دقیق راستی‌آزمایی و نظارت سخت‌گیرانه بر تأسیسات هسته‌ای، غیرمنطقی  است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124544" target="_blank">📅 21:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhYclBXMwAJYhZU2Qts0tu2NfBT5ekUgVqUx1DIC-419aKIzIBmY14_0L1oNzP7xmgrYYV1PLPOq62Ipk2gTdbGPZ5EFK51NHr00jWhl5lFAAk3uj8Vij_dbyru1lTkcnDC2IhuF3hc-0VNhoUYIHtAhH4y_8MelyGO6UolbD0PJYg8x0mWk122PRqQ8EzJy6XgW-riZ491H5q0ojFceQCymQhwyl-JF7TJTwbK6UG0I0kBzgf7sgKHgl0Oh27raYISJj_Z8cSPvWWQglm6gSuNtov7McoKSTxqphmX0M-9Y8XogEidRkJsJ3XaV2ZN0qxWhKTWFgG8GiuhqDPfE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در نشانه‌ای از قدرت و استقامت، به تازگی اعلام شده است که شام خبرنگاران کاخ سفید که به طور ناگهانی و خشونت‌آمیز در ۲۵ آوریل به پایان رسید، به تاریخ ۲۴ ژوئیه موکول شده است.
🔴
این اعلامیه خبر بسیار خوبی است زیرا نمی‌توانیم اجازه دهیم دیوانگان سبک زندگی ما یا حتی زمان‌بندی آن را تغییر دهند. از من خواسته شده بود که در آنجا حضور داشته باشم و سخنرانی کنم، توسط ویجیا جیانگ، رئیس انجمن خبرنگاران کاخ سفید، و من پذیرفته‌ام.
🔴
نمی‌دانم آیا همان اظهارات نسبتاً تند را خواهم داشت، حداقل در مورد برخی افراد، اما به زودی خواهیم فهمید. به هر حال، این یک بلیت "داغ" خواهد بود!
🔴
جالب است که مکان برگزاری، والدورف آستوریا در خیابان پنسیلوانیا خواهد بود، ساختمانی و سالن رقصی که من ساخته‌ام.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124543" target="_blank">📅 21:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53317d490.mp4?token=bFls0z5R6AhrGnfJpNjMJpQ3XIhpo9eItnMaUq9PuIhPJ_eTPYYePsd02xqhGm5jUbUc_IfdoqZxXCpjpVs7vCCeiC30jYKrvTgd6ctHyQqcTxJ3q9fo4lF0geMtLQaFSopu9dvKbbFrD1p_H3DQI86IYpa3kNXIE6Sx0tfDkemTOYLKEA1nJLWSubgnQ7gkTbq_l5dYJ2INfLISEAw_OR3YmHBmFZKm8u9-t33Y0Sf7pHpya4qAomBKc4FSRDvZ_WgYKJT-MaYz2mYBeEfH2p9Tyu3LJ2OehbZobgliLYy-tdD-RkI01LKfVI60Ygziy8aHLMOKYkXMGXZLkC3VBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53317d490.mp4?token=bFls0z5R6AhrGnfJpNjMJpQ3XIhpo9eItnMaUq9PuIhPJ_eTPYYePsd02xqhGm5jUbUc_IfdoqZxXCpjpVs7vCCeiC30jYKrvTgd6ctHyQqcTxJ3q9fo4lF0geMtLQaFSopu9dvKbbFrD1p_H3DQI86IYpa3kNXIE6Sx0tfDkemTOYLKEA1nJLWSubgnQ7gkTbq_l5dYJ2INfLISEAw_OR3YmHBmFZKm8u9-t33Y0Sf7pHpya4qAomBKc4FSRDvZ_WgYKJT-MaYz2mYBeEfH2p9Tyu3LJ2OehbZobgliLYy-tdD-RkI01LKfVI60Ygziy8aHLMOKYkXMGXZLkC3VBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز شبانه جنگنده‌های ارتش روی کرج، استان البرز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124542" target="_blank">📅 21:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل:
آمریکا با ادامه حضور نظامی اسرائیل در جنوب لبنان موافقت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124541" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKABQhKse8zJpCoure1yU8uOapwVo8wXvY_5tU1xZbvMoi1xTuqC6C4XIoZGCgkkygsyj10g90WIIoZ5GIayBWtUXkxgLLccCAhFrMizBGOTnG50ceAWJnWtJWkt8rToCUdu8_JQrxj6_9YwBITkY29ez41uc08qK9AYsi5YJl0pClYJuHmXVpihU-xr8F4ySS_y_ZbcKBrVat-watnqOXM5frf7a-dsvpYRg1vpfxsXcmmU5RyzyRNFj1OcUpXXejyTdskVXIPQh8yx8ZiLxxt2_zxACcg1GWDdz68IB6jc_XY6hfMgh_aVtQl0aeJBJZwyMA6Y2xyfKCKSP3n6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: چیزی که ایرانی‌ها گفتند این بود که دیگر پیشنهاد رد و بدل نمی‌کنند. کاملاً مشخص بود که میانجیگری ادامه دارد. بنابراین اینجا تناقض مستقیمی وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124540" target="_blank">📅 21:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
شبکه کان به نقل از یک مقام اسرائیلی:
تل‌آویو به دلیل فشار آمریکا انتظار حمله به بیروت را ندارد، با این حال تأکید کرد که ارتش اسرائیل از "منطقه امنیتی" که اسرائیل در داخل مرزهای لبنان در آن نفوذ کرده، خارج نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124539" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
المیادین به نقل از منابع آگاه: هیئت لبنانی جلسه را با تأکید بر لزوم دستیابی به آتش‌بس جامع آغاز کرد.
🔴
مذاکرات شامل پرونده‌های مختلف و مفاهیم مرجع مرتبط با سازوکار آتش‌بس و تثبیت آن می‌شود.
🔴
تخمین ما این است که مذاکرات امروز به نتیجه قطعی منجر نخواهد شد و احتمالاً مذاکرات فردا ادامه می‌یابد.
🔴
در طول جلسه، ایده‌ها و راهکارهای عملی از سوی طرف لبنانی و «اسرائیلی» و همچنین پیشنهادهایی از میانجی آمریکایی درباره آتش‌بس مطرح شد.
🔴
یک جدیت آشکار و یک تلاش واقعی آمریکایی برای دستیابی به تثبیت کامل و پایدار آتش‌بس وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124538" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
بی‌بی‌سی‌ : ترامپ به پایان جنگ ایران نیاز دارد، اما تهران عقب‌نشینی نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124537" target="_blank">📅 21:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
ترامپ احساس می‌کند نتانیاهو کنترل خود را از دست داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124536" target="_blank">📅 21:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رئیس جمهور اوکراین ولادیمیر زلنسکی:
ما از طریق اطلاعات می‌دانیم که یک حمله عظیم روسی ممکن است در زودترین وقت امشب رخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124535" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ناو هواپیمابر آبراهام لینکلن به حمایت از محاصره دریایی اعمال‌شده علیه ایران ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124534" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23fb8dd41.mp4?token=mII68-f-D9rJ7eY0OFf4EDBTWlCQgEN5QFbBTG7fXOpG33p3DWnUd-EOgx7G5KFulf3tTjQBF2PnM6Jdkp_e0rIIbEyowoCbXbPoiSG6cHF5W5Ce9kHwWSUWo8GZ5UoHeksVB0lCKqXR0_3vR201xt-VvszHvosVmkP0yaoms78IKQwILZ2jZCALkv9lfnJOXc6aAePyjiKX5YRvZtvxcafNMAizyouNDYskeqokBH5hH7efQP2StHBJ24L4X4wqsyvF8Ift5vJljAT_EhoofdWTM-5pNe6LoZ_HC0vw4dMdMN3uPvmq2DBKFf8vj22nRCocoWZvnPV3dVCQsoY13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23fb8dd41.mp4?token=mII68-f-D9rJ7eY0OFf4EDBTWlCQgEN5QFbBTG7fXOpG33p3DWnUd-EOgx7G5KFulf3tTjQBF2PnM6Jdkp_e0rIIbEyowoCbXbPoiSG6cHF5W5Ce9kHwWSUWo8GZ5UoHeksVB0lCKqXR0_3vR201xt-VvszHvosVmkP0yaoms78IKQwILZ2jZCALkv9lfnJOXc6aAePyjiKX5YRvZtvxcafNMAizyouNDYskeqokBH5hH7efQP2StHBJ24L4X4wqsyvF8Ift5vJljAT_EhoofdWTM-5pNe6LoZ_HC0vw4dMdMN3uPvmq2DBKFf8vj22nRCocoWZvnPV3dVCQsoY13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماریا کورینا ماچادو رهبر اوپوزیسیون ونزوئلا می گوید به زودی به ونزوئلا بازخواهد گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124533" target="_blank">📅 20:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada3d308cc.mp4?token=tjlMfBWA_lTRW8vsp96Vk5C849QNnhZlmF-YuL3GpoC1_538ARlaRaDDpeDBvqLeyMJFIZOR2rb_6wfOVCOu5FXz-TvdcIeBJASa5ZAuHyGK36OJdOhkdxEvf7Ub5RC4u_dwR_ib8Ugxz2LB-1wXjkiRNWpDTcG9owkk86ofOh9k2Owm3Rxk0yjEs5nP65prfTgI26-tR3VHMRK1qRO194ATPhcxvEfqU-S2pXq17C06ttCDqBIgHoxFkYhLfawWtZqiW951xWf3SgBThwBqVoJfL0McugMRIqwIWz6-gGif2RvYjDy3RwXbCcFLJTv2W-yNUizaUEbsNppGTXMNnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada3d308cc.mp4?token=tjlMfBWA_lTRW8vsp96Vk5C849QNnhZlmF-YuL3GpoC1_538ARlaRaDDpeDBvqLeyMJFIZOR2rb_6wfOVCOu5FXz-TvdcIeBJASa5ZAuHyGK36OJdOhkdxEvf7Ub5RC4u_dwR_ib8Ugxz2LB-1wXjkiRNWpDTcG9owkk86ofOh9k2Owm3Rxk0yjEs5nP65prfTgI26-tR3VHMRK1qRO194ATPhcxvEfqU-S2pXq17C06ttCDqBIgHoxFkYhLfawWtZqiW951xWf3SgBThwBqVoJfL0McugMRIqwIWz6-gGif2RvYjDy3RwXbCcFLJTv2W-yNUizaUEbsNppGTXMNnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: حزب‌الله نه تنها دشمن اسرائیل و دشمن آمریکا است؛ حزب‌الله دشمن لبنان و مردم لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124532" target="_blank">📅 20:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فرستاده اسرائیل در سازمان ملل، درباره پهپادهای حزب‌الله: این پهپادها کمتر از ۲ کیلوگرم وزن دارند. می‌توانید آنها را به صورت آنلاین تهیه کنید. بسیار آسان است. می‌توانند آن را از میان یک پنجره به داخل یک خودرو هدایت کنند.
🔴
پرواز آن پایین است. شناسایی آن بسیار دشوار است. و تا وقتی صدای آن را بالای سرتان بشنوید، دیگر دیر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124531" target="_blank">📅 20:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124530">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ادعای شبکه ۱۲ اسرائیل : دستور تخلیه ضاحیه جنوبی بخشی از هماهنگی نتانیاهو و ترامپ برای فشار به ایران تو مذاکرات بوده و نه برای حمله مستقیم به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124530" target="_blank">📅 20:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124529">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: گزارش‌های جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش از صحبت کردن دست کشیده‌اند، نادرست و اشتباه است.
🔴
گفتگوهای ما به طور مداوم ادامه داشته است، از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش و امروز.
🔴
اینکه این گفتگوها به کجا منتهی می‌شود، هیچ‌کس نمی‌داند، اما همانطور که به ایران گفتم، «زمان آن رسیده است که به هر نحوی یک توافق انجام دهید. شما ۴۷ سال است که این کار را انجام می‌دهید و دیگر نمی‌توان اجازه داد که ادامه یابد!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124529" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124528">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نخست‌وزیر مجارستان، پتر ماگار:
مجارستان سرباز یا سلاحی به اوکراین ارسال نخواهد کرد.
🔴
نه حتی تحت دولت جدید مجارستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124528" target="_blank">📅 20:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124527">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad80e601a.mp4?token=eiV9xJjtNU5sre47R4yhiK3xap3VtwWEvPeBCZF8DuK2uYlsQjSxieyJHkMS1mnokEzI1fxwZzCOfJsF_VTdwPYU-CLPp6x9YfEF0xVR0k9mphCqfN4XS1OysTzD6TSslg7bX6nbJFe9Kan_gaza0HeolSKynQiBWOWMOJHcPUxhujw2gKg-1AAXZec3hxqWhmR7ly9_K6MNcrq88OtGYMoGWpBfLcuxNNE9fpgPKOjK_wCxssYhUwlQWoQYw1IaJH_BCqZgnUtkP773tbP9_ZUG4T44OjixTAPMVsM1q8BBOZn0KYATn99Z33t2mIyrjf1JXat5zITq8iEnQNHAOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad80e601a.mp4?token=eiV9xJjtNU5sre47R4yhiK3xap3VtwWEvPeBCZF8DuK2uYlsQjSxieyJHkMS1mnokEzI1fxwZzCOfJsF_VTdwPYU-CLPp6x9YfEF0xVR0k9mphCqfN4XS1OysTzD6TSslg7bX6nbJFe9Kan_gaza0HeolSKynQiBWOWMOJHcPUxhujw2gKg-1AAXZec3hxqWhmR7ly9_K6MNcrq88OtGYMoGWpBfLcuxNNE9fpgPKOjK_wCxssYhUwlQWoQYw1IaJH_BCqZgnUtkP773tbP9_ZUG4T44OjixTAPMVsM1q8BBOZn0KYATn99Z33t2mIyrjf1JXat5zITq8iEnQNHAOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از لحظه برخورد موشک به کیف در شب گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124527" target="_blank">📅 20:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124526">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روبیو: اگر ایران سلاح‌های هسته‌ای به دست آورد، مانند کره شمالی اما بدتر خواهد بود.
🔴
آن‌ها کشور اسرائیل را نابود خواهند کرد و شما قادر به انجام کاری در این مورد نخواهید بود زیرا آن‌ها یک سلاح هسته‌ای دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124526" target="_blank">📅 20:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124525">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
روبیو: در مورد هند و پاکستان، ما آن جنگ را به پایان رساندیم؛ ما در کمک به میانجی‌گری آن نقش داشتیم.
🔴
مارکو روبیو می‌گوید سودان به یک درگیری نیابتی تبدیل شده است زیرا «امارات و سعودی‌ها در دو طرف مخالف آن قرار دارند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124525" target="_blank">📅 20:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124524">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5843d7de41.mp4?token=qaVVTli7kKbYxzdMGGIEE9NFHE7G2rx-uAvZwtBq2xQ3wrvHB2WsXJwlj_a6vP1EzBNBkkACmrb5abWjgb35DM2F4HN0vC4o0ZkNpuv_mFHtr0lyhefeWzJyhJHusL9DYFhSgD7Hrx_hssf_kvRtM6Xq26E-Y6AMhk01eNtyYLHLWZexbgyCFsW8rbjtomaBdqkK84Jkc5jsmbpmjAmyosLRQJcYT9dYZB7iTCNfxSuZPM63p2AD6fiCKLlOINJ0O10QRzs0vJ7heWenzAZiJujT2vL8JvAy7RQZeZUDuuKCR5nhruAYgv5QIk8RPuOdy7ekhCeGXEVluCfE8w5-sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5843d7de41.mp4?token=qaVVTli7kKbYxzdMGGIEE9NFHE7G2rx-uAvZwtBq2xQ3wrvHB2WsXJwlj_a6vP1EzBNBkkACmrb5abWjgb35DM2F4HN0vC4o0ZkNpuv_mFHtr0lyhefeWzJyhJHusL9DYFhSgD7Hrx_hssf_kvRtM6Xq26E-Y6AMhk01eNtyYLHLWZexbgyCFsW8rbjtomaBdqkK84Jkc5jsmbpmjAmyosLRQJcYT9dYZB7iTCNfxSuZPM63p2AD6fiCKLlOINJ0O10QRzs0vJ7heWenzAZiJujT2vL8JvAy7RQZeZUDuuKCR5nhruAYgv5QIk8RPuOdy7ekhCeGXEVluCfE8w5-sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو
:
برخی از متحدان ما در منطقه بسیار به صورت تهاجمی همکاری کرده‌اند، مانند امارات متحده عربی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124524" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124523">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روبیو: اگر مردم ایران اختیار داشتند، فردا توافق می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124523" target="_blank">📅 19:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124522">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کرملین: در صورت عقب‌نشینی اوکراین، جنگ امشب پایان می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124522" target="_blank">📅 19:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124521">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حزب‌الله: در صورت بمباران ضاحیه، تل‌آویو را هدف قرار خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124521" target="_blank">📅 19:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124520">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روبیو: جنگ در ایران به پایان رسیده است.  ایران به صدها میلیارد دلار برای بازسازی نگاه می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124520" target="_blank">📅 19:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مارکو روبیو: ما از تهران برای هیچ چیز التماس نمی‌کنیم.
🔴
اونا ممکن است التماس کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124519" target="_blank">📅 19:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9z02i9B9Lu9SZU6jHz6fnp6hcQDjbU4ZNdokrt5QDTDTeEkX2cXS-Jc0lBrctSR7ApHdLhYc6TbhUTPBtr9IQny0cQLOrbIGr5XZXzKZOF0qbYjqPsd7nmHKpoNZZjvvxonpPZM9I0JRrA6KBmVZzmUWiV3C7QQJ04R2Ax6VR9LkEV9YF2j0oweOxpMNRhlCN8FWfGWih3evdJJtUBr40tgHS04PJ02R2gMiHa8kZyn7dGAyWJDqU4ZFjzFvvzaoyJlGPfeBKOK_YV0FTedfd8I2erYVgeolulDcWBvEhTf-duBraq8D2i1cVi6IB1sE-Cu1F5il6_AEHJqzAu5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط بیت کوین به زیر ۶۷۰۰۰ دلار
🔴
۷۰۰ میلیون دلار از بازار ارزهای دیجیتال در ۲ ساعت گذشته نقد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124518" target="_blank">📅 19:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
روبیو درباره ارمنستان: روس‌ها از درگیری ما در ارمنستان کمتر از خوشحالی هستند.
🔴
به نظر من شواهدی وجود دارد که نشان می‌دهد آن‌ها دوست دارند رئیس‌جمهور فعلی به دلیل این رابطه رو به رشد با ایالات متحده، انتخابات خود را ببازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124517" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
روبیو : در نهایت ما هنوز با چالش‌های دیگه‌ای درباره ایران روبه‌رو هستیم
🔴
جدا از برنامه هسته‌ای؛ مثل این‌که پولشون رو صرف حمایت از حزب‌الله، حماس و گروه های دیگر در نقاط مختلف دنیا می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124516" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
روبیو : چین این موضوع (فروش سلاح به تایوان) رو همیشه به‌عنوان یک فشار در مذاکرات مطرح می‌کنه؛
🔴
ولی این موضوع تصمیم‌گیری ما رو متوقف نکرده، در نهایت، زمان و نحوه انجامش با رئیس‌جمهوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124515" target="_blank">📅 19:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">یه افسانه ژاپنی هست که میگه:
"اگر به اتوبوس نرسیدی، شاید از یک تصادف جا موندی
اگر پذیرفته نشدی، شاید از جایی اشتباه نجات پیدا کردی
اگر کسی ترکت کرد، شاید داره جا رو برای کسی که قراره وارد زندگیت بشه باز میکنه."
گاهی جهان پشت چیزی که اول شبیه بدشانسیه داره ازت محافظت میکنه
به مسیرهای غیر منتظره اعتماد کن.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124514" target="_blank">📅 19:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید 90 گیگ 100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/124513" target="_blank">📅 19:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECzMvjOedYT15wfaW0jjS0LihQ2bsR7LG-uS4FWNTkAgNlHLUrSDJh_lVsAwdbLRgc7klo2WjvBFzkPZ34ex6TAtiZv2c9jOme-PGamXeGyEs2zCzVeKsMR-vknrJfvqCPt9NTCA88bqW1SM381xQ_V1fcj-ec-phStJY3vxxUAxAC1sPEjTgcIv-c6-9Ja6mp9KyFPEUT-k-9dKSIBXYq9uCyRTHa_NvDWRitGBuoqnsaQVjQelPj_oSYL8WrDazHmwTax1_mWxhLApxiqrowHPivGynLrsptBhXmyfQBLwioyoS4U4Iejud9jpGn2ZpBdYj_riZvr6KodJq4mHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/124512" target="_blank">📅 19:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW9Au7xWWqiGRam4Gxg8vRoA863M-WwVBEzhc-7mnVMm8veq0_TyoWAvDYNlymgUQ7nsD4Yon3_Bwv9f_36ng79E0E0GEoeF-1-Qcz4n26UETOqVrXZjLcCofdKPU4ckWTn_qw0I6ZWfdi2VR5JyEl4Fo-CmMt3ll6VPCAnRzZI-KsE8GtvTkBjKu4Y0MM3eN8KGkqn-YbZqrvvwhWgiQqtvsNp0wqMC-5K2BzMDjMBpi4MiPNqyV3jKUEIjxJeBvEJtgh72zsjwzL33d78F7psv67L92H9Pjt-lzulASmkI84kW3qFQrs95oOJ-8AL0fwxGTWi2H6Xx7L-BgJxI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت متروی کی‌یف پایتخت اوکراین در بحبوحه حملات سنگین روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124511" target="_blank">📅 19:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، امارات متحده عربی در حال بررسی طرحی برای ساخت یک خط لوله اضافی انتقال محصولات پالایش‌شده است. این خط لوله با هدف دور زدن تنگه هرمز و انتقال مستقیم سوخت به سواحل شرقی این کشور در نظر گرفته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124510" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
جبهه داخلی اسرائیل: محدودیت‌ها در شهرک‌های مرزی با لبنان کاهش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124509" target="_blank">📅 18:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c945a1dc.mp4?token=oGCL56XL9loiBbcTu9OUxTSUFIHW1PEs8ZvEC2JeGJlcsf5LRhwymXPNebgmeX3jZUgPON62XXJzooSQctv55rvSpEYiLC1R-GAmvTegMLqBJPoRjGlTJlOp1ybYi6xMV_I2cMSRzE1E2VZMeQDzuUMaIDPt2SNdqllty-v8GGOPnRoWJ0lz6YI3XTloJlDBUiocUiF8ZvpeE-1ZuOnVAFliP315OMiZJHnL06hnEYXNGxoTrwusIwPfPZd5NXlGyyl2-La1aTObJnpn7LPf3dkS1EVy0SF3Tfqq1W8RuNJT7b5IVRXzsLc60ckZeVgIknv7DN1pb4I3Qcq4d-IDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c945a1dc.mp4?token=oGCL56XL9loiBbcTu9OUxTSUFIHW1PEs8ZvEC2JeGJlcsf5LRhwymXPNebgmeX3jZUgPON62XXJzooSQctv55rvSpEYiLC1R-GAmvTegMLqBJPoRjGlTJlOp1ybYi6xMV_I2cMSRzE1E2VZMeQDzuUMaIDPt2SNdqllty-v8GGOPnRoWJ0lz6YI3XTloJlDBUiocUiF8ZvpeE-1ZuOnVAFliP315OMiZJHnL06hnEYXNGxoTrwusIwPfPZd5NXlGyyl2-La1aTObJnpn7LPf3dkS1EVy0SF3Tfqq1W8RuNJT7b5IVRXzsLc60ckZeVgIknv7DN1pb4I3Qcq4d-IDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: ناتو یک جلسه سرگرم‌کننده خواهد بود...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124508" target="_blank">📅 18:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124507">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
روبیو: هیچ تغییری در سیاست ایالات متحده نسبت به تایوان ایجاد نشده است.
🔴
به نظر من، به وضوح، طرف چینی دوست دارد تغییری را ببیند، اما در این زمینه هیچ تغییری ایجاد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124507" target="_blank">📅 18:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124506">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fdfdb0cf.mp4?token=ct1uO4LR-0hP0HmSAyfRg7W80r9tWindm3rYFTpKIChrW2GA1mmDJlIEj-_SLeq5xgsFc-t4zZBJrLzOh13NiatB4ONWevNOAO3jLsNfBDKK3H_nlSng2nTmh0BIE2nD7l9AQ5CXLXpZXk8rVLkY4wBigs4YVShEQAdc4J8tRpFvvIc8NOihakEs_Tt72n03ZioAUFIGG1aWfqGIU0e2Y3OCullj1RY8lcCEo5WtCD2I4UbBvzuAaaZMlX_PhdbCNYVqdyMuysGtG-obSZCEKdVsMlEdoAsFfeOaFGd5AeTWLPCvkOupnkVR8tv-HggzErLfqv3aHGvMshTOhKzYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fdfdb0cf.mp4?token=ct1uO4LR-0hP0HmSAyfRg7W80r9tWindm3rYFTpKIChrW2GA1mmDJlIEj-_SLeq5xgsFc-t4zZBJrLzOh13NiatB4ONWevNOAO3jLsNfBDKK3H_nlSng2nTmh0BIE2nD7l9AQ5CXLXpZXk8rVLkY4wBigs4YVShEQAdc4J8tRpFvvIc8NOihakEs_Tt72n03ZioAUFIGG1aWfqGIU0e2Y3OCullj1RY8lcCEo5WtCD2I4UbBvzuAaaZMlX_PhdbCNYVqdyMuysGtG-obSZCEKdVsMlEdoAsFfeOaFGd5AeTWLPCvkOupnkVR8tv-HggzErLfqv3aHGvMshTOhKzYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه مارکو روبیو می‌گوید نشانه‌هایی وجود دارد که نشان می‌دهد رهبر جمهوری اسلامی ایران، مجتبی خامنه‌ای، زنده است و «در سطحی» در تصمیم‌گیری‌ها مشارکت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124506" target="_blank">📅 18:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124504">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: اگر مذاکرات به نتیجه نرسد، به وضوح همچنان مشکلی در مورد جاه‌طلبی‌های هسته‌ای آن‌ها وجود خواهد داشت.
🔴
اما چیزی که دیگر به عنوان سپر متعارفی برای پنهان شدن پشت آن است، ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124504" target="_blank">📅 18:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124503">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه آمریکا در مورد ایران: اگر ایران می‌خواهد بتواند دوباره نفت خود را از طریق تنگه عبور دهد، باید تنگه‌ها را باز کند.
🔴
اگر از انجام این کار خودداری کنند، گزینه‌های دیگری نیز در اختیار ما قرار دارد، اما ترجیح می‌دهیم برای باز شدن این تنگه مذاکره کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124503" target="_blank">📅 18:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124502">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روبیو : شاید چند روز آینده خبری از توافق بشه
🔴
مشکل اینه که جواب‌هاشون دیر می‌رسه و همین باعث شده بیرون هم گزارش‌هایی بیاد که شاید چند روز دیگه یه توافقی بشه.
🔴
چون داخل سیستم خودشون هم طول می‌کشه پاسخ بدن، بعضی وقت‌ها حتی ۵ یا ۶ روز طول می‌کشه تا جواب‌ها و تصمیم‌هاشون رد و بدل بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124502" target="_blank">📅 18:44 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
