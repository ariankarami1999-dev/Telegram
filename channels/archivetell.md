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
<img src="https://cdn4.telesco.pe/file/k-P3zXKSBrz3fvYUYiwk41sscodIkxh6enp20PhOCODZZ0QQ87Qu2ASJT_jYET1Gc9jMBsxjSfoe1U-pnRcgVLwWaYTM_bGxMKya3HGuP1lNjq2PNbL-JnQ6xtIx-rLWSGqUrUj64QgRiHOkWrxV8Kbsg1c3Tr4VgJleQzxzava8NWTvW09Pr_ageMvT3x6jKwSyTuLnZYnT5uOto4_4YjGk1hvsjRev4NGhI1ghySPpOq3ch-BZsqWsRIDdxjP6djzFu0SlLE8dsQ51MxtZmC8YuK1j8epWYt2-n1Px-rTmeb073q7uKhSChb5t05jLDCqnvNeJHvsEE8_gr-4UPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYN5NLq1Y9I-cRl7ziELdZOO0LxGcGpxU25xEpkSwn5b882mpoO34Tx-wfSys3PYLq-e0T9zrx-OZF4rjmhc2uIOoukLXJo6xZ00b7bGR_e-h8QAfoH2XUQnrAcjEPc3dDTE_xzRutlZL9_hVpTwgBERgC3ncEM1llzvVplzCqirM37EA43OwVXtEO_mC0kcWudNBFSm71lBuY1aq27bXSsHeYOVfJ9LwxTJhCHjBggbUf5ThKBo4VY9p2USLUDAiO70P-6dO1SxVRkeReqfDnpYewaCQEj06S73nJCWPB0t568D_Eq0ZzhxoESQM-slkwmmw0EuLYymYBZx9yRwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA7mkVRUXCBhmH-HPpBXoZdC0Ch5Z88KvxFgCtfPzdk13XqfzboRCEDiPE5hSOMlFHzJK8hbokxtXxzcS8i-y86QSnRUXe_t_SfOVrs5nl6nJivR5uNE3XMOMV1ICHgBeoBJAjgMoUrp7KGq_WrH0nEf6tD67zoWvkUgK89NupzRacr7ornv1x_QEi0l2Gu5oylatXLyY5LpWQtz8NgibR_qqudAPeMH__fK1ZiP2CRBnxGk4E0JTAcFMz65J1RXe1tPI5uW5Ld0hLGPGZTJq6W8SFu6AfL4i-KhCx_OKXtpHWXrAShir1D4am5mRe0jH0_Wl653jCtVskCTMJV_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxMyhglNPmIkexwto2DBhgG3BDZbL-y8hKPmTpC9SlsWfn1hZcsVT69v2eHhEVlPYD7AWBgCJyLDgDpORiqerohbDJEsu6g7zSrjnTz7XOsimGYPPS9fVJ0sIQHIBN-cOY_sGZzYS4DxkA918MBwv37r-b1XN2zQsZY4yRdgkgNgYxErTSr5FU0bKAGNCxR0O74BF4SPiz37nait28oq5aWUdrXI88vnWXjk9yLdwaeJoVTE_0e6rWzCsNrMJt8nkgvw3PQQykYhnmZqQ6WRiqe70F4UiOfXL3Je6jCYFBpKTkp4dOriY9Oi_zfSNvLSB9eOW46fMMeeBlT7DTV0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7li7HQstMhALObMV62z5ey2GP-XVadNhXh1KbWpohjsO6Mevf9dx-xEaBcismOI0m5Vh8g6S_Z5KxOIA48zyEnX7XRRVKAd7FBe772dwkvxD5yJQCkWfMe-mpxcRRrldkN7ryv1VLuGcxObouRokUnNwyLn7PUJ7nbLLXfEw-yy_ONayDmLJSm4ygqp9vYfRMH9yzT4jSxFKtepx2W7C-PinXtaQQ0ZgAHygQLIRlYs14R-U-1PG6vHZHn5xkhRXa_shFUfjuGbJlgX8f4zp5I_ZbkKNnaSfdJnGbWMj_Xv7cCNsBwMSAa98BYBLd1Ngq-ZcesVwfgZStCAMXSOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeWFAHUglFCvskVMZ17DrPBhmwMgn4ra1dXkC3wlWdVfuuJWoqNYx7lIuWWOHAuDHfWPOfwbTdt-UbJPV0JiKr3CFy-cwG_ZQI-y0uS0ZTE_3e8tALobt4SoEXhb7HoZxut3xMpRWh0Y-FF3e2DrOOpVSZ4MzX3infAAI6RL0HFdQ4y-3QqP1A9udFm7iS9aOIzV5DwaYJ-kHDsL6ZAq1bI0-nfCDlA1QvxQQAlwsFStTsH1T71e-A2Tm9ccCT56p-c6MlHSBo6kDyRwT28VNTEvKGrMMlbvp7rn9wB7-MsstZ9N5ZDd_vGIR83AKlOy0iqbaMJLwFhbuYbcWTvo3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 64 · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXtjgG7malE0R-qQtFIG57sYQIP8obyfINFjDOwWFQH31y4B4tZ7Ll7A7lXyjMlWXr9yjiJhO8ACGF47ER-E64S9R953jIoKwqmLn_Nif6fSDGaMVWOgrVfhH4zSOVHyf7gG1lCgRrCDHBFrSTqfTq96dSqWgaWYGNQanHV3epS40sfOJulGcByakmQIrutZ8vu3EEW4uA6qZRf_rpi3kiffNptej_Zac0PuBOqtKo-BonF15RyI3LGQJpdm-lgwg2WqFziLLldqVrkiz6G7GIt0q30weVTt5UffNs7Uwkah3k9qdCBlMiGjB5ycKGKDAUVTrURs8zd_hUJMVNCuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqLYX1zTZQ52pkDJyLpwfox42taHu5gNa1s9zWrpAJ8L8yINyx0tSyzQy_OHgLYaVIbYC0AEIwztmQ5C2J613Cqgx9TfVecyhTewrAbhweLDQJkvSLI9bXl5CbTPXHA4w6biB8Vtpnj6n6sQMizsgmdA82ZgxD-ZXTJvEEErrRsuzPPBSjLEx21VYcoKk2dsX1Fq0RtGgDIBIdvzrAM2smhEpJqBVOF2IMDDMFg5p7Hc1SRR3Tp6r-bwWN7ffmIdGu_y7GWyC3k-1njX-p1GSc9gjvIa-w2zN3h54BXPKMvXhL9jKpZj47QRRbLB6CDemqSPPCe_p_J51t4il92MPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILwcAEZHPZEziBBCY6HIBlZ4054LnAZDGMVroliZ5ltLl-tf2zMK1d7Qk7T3CHZJPmtjkzjDz7BoOtMzPRwEHP_TBoNMpyMHUyARg87EFc8YaGM_uZ-_8sIkoFAwwIqTJwlAcMFFDnzkAKpyScMB22wDG-DSQdH1cvI2yk9KoSPTXnHNoTo19VV9o5j8a9xWzSgZWFARqXtY9GBfNWdPdAvyL3R_cBKQv1UsUIIDRABMsM3zsvq_kSL0DPdu5f-F2q_EtkXetpSrimCRzLMVcu0bmr1A7vhS7gsDqDd3lxTHNsnl8O9GK4-o_RxpFJMHbqRmQMM70f2oF0dDdTo6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LY_YRI3QFt1vRNXs-U11LVtirv_L1zps99_JnRVyZJeEiz5PhwkEvwunUt4_ewMcc1WozXTcLk5Iw1ZaqVJr6bMiEd8Dnu66GAtZV03D8ZxdArvlW2b26jHQf-i8YTWT90fBUHs4yYf6qjxHHQiCkDz9RapTSk-rcWCjnHAzK57BgpQ1oZxKv_rfz-uNbEjR0nBeJyfIXkv1HEzfLJElwFlL4Y1GgO_hPlrOGMEbw_E7chNlCXBPKzJSkW6YnXfOPswInPNg8owc9cMJ1IxB_dYWqd2fYcGqCFff5lSMGrz9L4ry2vRE0XBzuq3NXmxMDBdsIrBgLJ_wqHQgKqXjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsgW4-aQ79e6_3fIrL6dRaaWSRES_mVJhcYLPHyHclDnQQXx6VJYf8Z3jRKZlFgmeAg36_-7Ah7gZdS16guOSd0RS6dHKBf9i7Z99Uod0hBYDRVyRcL5rJ18Wj4vsf-IhxHBei1iYv5DtXSBegEvJ7y34aAwHo2Urr--Osa_tY6s5EagAJLK69jU99eeTlgO5uW4SFpzUvdkd0L38D7Tdkfa8WZffaGZLmhqV0agunR5Zy9tgQNZVr9_Qqv53_egTorQxeb_9lRYyH9-QgGh-XzXjRmQbpZYu2IS4buxxSRJu0IoBVOemfHbbPaJ0UxszDlbhAFzv0RGgjCUJyLOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBmpqXnzzM7iuJnMxrf3R9R_L0VDVhVdXoM5W9JK8oxjCKTx4ByIqpDAbrwJS8XwnkFEOVnLFtQqgOFQLeH_FPqgliSIa7DVNAQoBSr8pGRxeyGd3WyzQxEv6RyZONEauC1ks0Ax-ciu4BCjtvSfWHR_IaFOL8qyPEMMma991PxQjBLdSWoh-kRaowFsfBazaPG6xZfKZpIt4sfxwnsCispqnOJofk7y6jrT9G53IIzSUkVCNOTUnlrRZa4P2TrDOtrcV44FOO-gsNvoNfOk3S1BPt7qW48f_wbJI633Gcj2CvkobBp777x4XvyWStM5qSH7rodFJGgKJqa6bfEenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJrE-O5WiVHF5wYfY08j7Y5AW51QUE0OmkAa3T2sZ9hX-vZXh1u-T41k_IshFDWnlvwTlSnKYq4al79LRl3DQQA0-ACz43HUD-73QsTQ0rdSb_X2DHHmZWHxhjrJ7isGOzW-Sm2wRAPtcEAwkYw0445N0FKBrViAyT7xSZfx0hqNm3WwdQfuPK1hDVcKUUH_1r4sD-I7u6wg9SwCwe1ef73bNnkLTbHxayPYteb0xqB7sZJhuq84rKJqWzMYLrPM8bE2PIKjBBuxo-JvUDBeHQwB4PEgrnMIff6s27YYH1UVyAFZ6uqIcSV_LgZ9YSTKlRWD27rOvSGq1llWoTa_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao27NdUXi1Tp-e-q8xXPxZ5vSZ4cHtTay_TxLDvEn_AZ5Fg5kvjGsK22E4VgaB2qefRq0DJ7ifXf-HLw3VFWkiW4SZRxUCulE4sODHm6vDmVuPx0GL2g3styB2A-48GRB5ugz4PX1mlKYnLnnmg1cy76_rAOi-f49tOhv5s7kXQj7FKFkXuACazwm7HRn2GZSOOF3ANXZramMq4gFSePTwC5mLxr1JeGlbQTH-IIGqyENN3ouqkk7hdOV7sObvSGEw_ZYXxl2YxGUgfiv7Jp92_H7XpBHsSuNUWMiBJtRlvw3wjM0l_K_UcDHe8YId75GsqBQTv6qYQTBZeGgVWuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAz3x6KvITayRPAOwwzEZdS5RKZ9muKNRP4za7PNYid9ZpEUwKoAq0VZNNru-oxBCmpM4RKiBHJyWFazqQqmdIm09sWx0bQSTUqXPgnfaEh7I5NNsOgfYwHnYQUZ7I-X8MvKXQt-pYexzbVVsajNNw4AzJtr38FL2qZuK-Befw03ERP0o6Zhb_nerO8PY5rCt2y3xbC9ceb4cQeOHRlGSF93w460iB86ybhWeLFvb1pnn2IMyhADnX_WDty3XnhBfsGVOKGI3dQHGfxBT6RF8vPvp_UgQ2-_fTPXLNNh65K43sL0ft99RFN_66yKGW_Vo2Kjwh3LXZdBw5K9wATRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ0BAW8uyt33wqFj10OjHqmni10dpTldgf1XyFlF_HSWdJu9bFz0GdNXSIs3NASg2IBznBisbiJ3999_ICUjd1TfnL_-xwkWddNAYgiQ3luF1MPdm6A1T4kQ2FOqBGPttUGSCkaGz7PcE5rcDw9G0gKHcOfAztsM0p_GtBsbw4l98QId5umKmwA8o1u61UGIdojFpLIio9s4dgCU5h19dxt4Eg2x3E2UyMiwT9c4h-yVlYYdEZSfVkN-zc6D-KJM0B2mIr6tZ9rlQn1A10fJnsCJvcCunewA2lsbkWEHZupZYwRQWW4h3UrvjxsuAuu6MqaCArh1w1YPd0cH3hAzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A967wCzO6dQW8kiWpP0XnDdODAT_31A-_eTg5BKHf0cOUDGHfPmk6MGKiWkTGH1ZFwqMKwY9RYjAiVsIwLOHsAcTnxmuzlNUbkb9R_HdqooWTAPa-14poywtcr7krWlU3toAURfSGQoywhJLqiMZABMh7MoD3atJw7PpYpJpy8HUlMCgVCFEIFY3g2MG3kfYM0OKXZbBrR5HKTYD-LjBDaRQQ_oPXcayGGgO5wa-pE_C8mcmhXhuzPz7RK946O7hBa5w3QFWrvMMjVeM8SDp2YS6RWaVDv6gvZo4zNmVCEVOUUgw1EieRXLBQQ-ThgZalPfxovBHWyrusPqJ_yOaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtLG1zr1fYzN-AVUwFg2G7FahNAOB6_OyFjo2D3KtE_A21NBqfy7TsXAVyG3ybsUzfDMsco0ljK3N8drKz06YDuMW76EOqk5mgyxpAPhw_g4Z3RIivDKNFkYMcoH9C_4Rhn53bs9GYB0IkR5O6qaA5ReEQQgKgrPyYGAURwcuXb-AVS1KwXG1ZvUip21cq-ZyP_kDT7omPAFp3odYyjSuOzwa7ssc8LMnsqHiGl4QRR6nE34wtVIUpR-wYiYRNwtmr-MI39NvD4Qs0pjHFy9dBWrNWoYrVC5ErGPhcEd1oMO27T9zigriFH3d3dYGGFonS-LcC5BdoFclHOJzCWtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbZUMgDm1CKkBiK9cVv9t-dtHfWi5hIoR1_BFyOcke5CXQ5bvGoFEl01H9qvyTTH47AonYZx9r0RBxaZgtrO-iLI4L14kEC4M9Xe0YnurTIxs4uJ_nf4dtBDoSPHRuiR8MT5i524ETr-lVwRstSmPMP34H5MOeuZTNNoNCP9r-U2_WczMYLU4NsjiqZFEeoVg0PmDG0kDuT1TRTo55DznEB73DWypFvxLTdXLlwjj1bt2F6K0esDA7bgWMnQWGEY-ocI1U6L0JMTkKc3Nx1wnf7f1hBOs52Ps39eeGotqFWR5dyJxrFhpcLB9qOI3odG_EK9QCJc1_RTQBtTV7UsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIhGPrb7_MvDEVXOkCsX2zKh5BVYpm4EJJRzXJigygFVqVTMRslskK3ql5I_vF9Qfi_85CMsSz7PlhYceAI-wbBLZAkeXOyeVe_z6iZkG9GCKzTYMw4pyY7unUvnMRdWH7MmYKNuOlB77m1IRqsC0Epb8ttYbxIAJNTSJ69wsSBYMsyfQjvjR967WNO2cVFDO1D1lUVJ4q8w1LyoBPj8s_b_nIU6eKn0175cXIjRhiZ_DdNnFQypT8Ax32roPrXVKal0gWOiEV8wKe29zsbu_xN3Sr9YwyBkwmBCKJriT4ziq37l8Ofeqfp_qYkQIfyGn62JUaJXIQzeBYNs8ZITIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQ_6HEIm6C4OKmjgOfT_OQPA_EB_yKCvzjhjYtyuI9WiWcmhJgBqOfN81avNtKXb9VwDZIpVW4ea_wSS_07RqkKbteqQmMN14jGWaPjSvXx0SWB72DlXuz2XA4TaXyzQP9kzD--vBA7rOOOdtqQ0Sm2eVh3qhcR9mboH4vg0yL-w2WyRFDLdeV2R1Dojp-D176D1mGxPVuORzxHbHMCyKrNYdDB539Yn1vvAcN1zn3smHRB51UBmXEfMLzgED6qCnnJpQSAdSS9QhD1cQrUbidgJ66OqMF9NBpkFALnECpUorINsmo1RkiAujiojkbvi8Z2MQ2t6VH0JxyrlZYzLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cLR4ZywMfCAK3I5mcghhRkBxYBUxdUR3z4OJnZNRckbZoo3GScIjSUELod4Pz6WGVIkcweb1mXJ9bXgti2zxXRAx1FQodMOq3Nuf5zj18sUJKA_WOy9wleYv9JOgF4Zbcmn9saPASsvs-CTgSZWqRvNbNwcrI_zgnN5g0bm3pa-riqepo5_CNRB4IoOaxlsOopWDhGyVAh0uW3ymx9RY2t3DHh_WCzU0YC0K25WNiynlY8H3-LhXm2vSEd8tIJEdkGFeRb8GxH5htX6QeBu2QX_92UUCTWQ8HyTnmNCaGt_GMLBRB-fRigK7zd8uyLMwehJYR6jDalErd_iTChT00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6l3HsLX1QTlSP59IFUlVxM5kTeYsMUHYhLrbYzlja6Y9JordCJgmN5E8QpRl0Yr1_9zWh9vvpLoJWn2j35VIPX9HWL_JEH43FaOBFK51a6V2WsE_G8qIqHDIRjswmVCegyccApv7a3t0aCWCOt1l1-81qYY64RFvsh-xrz65z0CqgbDlI5-X-pUmJ5PizqTfIlVqBcxGv1fczM6U82X6crUxltoFgMEQKcdna09prEyJL_VgnyVEuRf8l_zA1fD2blAO7byFeeUdwKJNXFvGt-fG_ntHtvzr1t75ULkqSGLUZzIrbtej7qz3BW5S8RNk__iwkl-5z99KsMjIJg2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfU_Js1TwynotXF7qDUpa-PWHNB1ZZTg9wjutmxS1GccALimmGj2pp_9Qeojz_UgLADv06xfuUlwQ3s3DknxExKqA9F4yLCSVGbv2NYQpoF-kvzjRj-Mq9m8G74i9l9RpqrI34zKnl7hU3IljWzKO5zcSwpYgTLpuhq4bvyETdqm6TM6i5fofy63G3T2_GSFtK9Ut8RMtPN3dqGcF8Jc0-NssiE6EhDMeCiNuRuHinHaZC9p637QeLUM7TDpF1dss4zb-E1V7K8NANJmomneYERYLATZtuy3ubVa6Jz98OwmHMlVk9wxDHvUn3OXIKzt2NMl_6NdG8RtL0mYvPRCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH9bqEZcZ5oeRLN-wQdOY-NYa72zS8WtPNzM5JdBtLIVkxdvk3ydV0DXrTjFy7yJ5RJO1U7rvjgenwA0-FRTJB9fDxOwbTuV9Om5E15zgIGtr0BMYBgRGdLSVoLcLncbj4cnKjGwTx_fr0suSYp2eNLbv274YwYD_Epdi0ahFe7cZWM_Mh5iMzooTJ8a_AI7eGNixlnpXM20rGdR0MUX0mmpoxBd95f9JimSWp1_GlLjAsXWUqnY-Lltx9RBV15J_KayT-fC80P5o2AU7gHWUC0v30q9OodKDwrhZXTVytIzND3HbsfjLGdVqlB48GhPxJ4vsK5kafGypgPQYMMWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbEuNY2PDAEMWf0M_oJwHQpd1SxeoA7-dwS2pufa4HBHvpo1OaxKrM81HGamW0n4fqs94pnG5c2aqJBh6rC2AHilz25INb9FwACQDPjl3OKcQVoGZR2k5pwdwVVjd3C0tZCOc1de6n-zzYjJgU3562P_R7FvG7loKY1qaPpEA4t2TWUklU-D6D8bvZhtavY8C_hYe9I69eWfoJl3Oq5Q8SMhMabIVHHoR4S5eChYl6Qxn5FnMkFbSecUl85AfmYIkVJ7VZz8_4nW9PfrsaFyxGjFJf5VDyiQR57hCYTcmZnR_ryxTgE3wZj-48FnAM_HDHz9zQdFW6XLbwMZ-NO1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIoDlvy0eaHKW3lFU8ZuM9WpxZfdYJSVGuyHI2MAtLOtGwrX6UX-fELLFLE8hFwjThkCCuip2_3W30FuQCfFqQoZ4BC8jOP0uKIUOWG_alveeVGyt7i4eKbvn0qaiQChj6x4lqcoHO5fsTH60-8ZRvTMKYTafSEHjcRghYAVLkfW_NuEtkJpFZTyoQ59BiuWdyqckYUAepPRZ-F40xetLQgrVcukZyKVxjfM4edaoFSo-DaQ18OdLH1FnSxWt1vQbiD6lUKM740eEtLmoAUxIWgVTiM0KrgBXrICJCl-EQhLzkdzIUKiA0h5b16pOp1JNGgSgtAJJeqJcn-6DXVPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkmtZUaWndITMyicuhHLn6cu-KWK34FzeWcZw1pkcgRs6rft4OD3pR5V1XQ-1uwcYql6EWpawMHoWTVr_CDrZLLLYmRdBoIaUplXJgeZKdKnelqKnP6WfHOwHyupqZe9eJJU73ND74hMEz8NDK5VuBHsngGzv3HL5P3AcCF__g5Vubb7da1Pb3D-pzoVYLoHN3_9Dnh9gyBB9YyilEotLsCJQA3UsViDHbsdux_P7_ly-VK9Da3j3fd8EyUKJ-9SIo9uml_G97qU8Tm2-Rfy2brIbUe0Q5NPQkBJfJiShq6tx-9UZ5yZOkv5m-pyI95bROHQCl2vocM-RU9fRKxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ5K6kyiOzvqq-EOKXalkbVeZRJKLTA7x26eWYoI0TuBnrYEPtNvfL6ErUiXuKUUHNlSWU3cJlnpzHVQFkivK9NYcpM-38jzdo_Cv1eOm3zBf5YB3azYitjl95AXcfUhqLIPftb-olJlx5QoWXBDwjgvhu9YHgxV7-EZl3C9z2XrvXaDe3wMFxDGjMbTCwXTE45WAJe9V7022QxG_rNwaA4Krj9ezYMTaykZRz4ZzR5-T5i55ycyCuKEvHQtUorXVu23Bth7Dfb5NkyXyBcF6K3kmZCAExLRH5vxqR7PX6zbSzztOV7PGAKiyE-GyNXWLb-xjECdC6tNqNOICVge-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgV8e1sylHvGUKcB4cG_f6EP2C2tYXFmQhxBk7psbPuyvMcPDNnfzVDnKdIRrzLJbGvD4Yi31HEmAz3HjoD7vCeT3KUXCZiR_6wsesU2-lThdXnNvlS2TazFMyzzYAE_YW2MeP-oeCK7vIx9-I6nEM9k5qw_vPX5WqkLE7tOWne1rJ8KXyHyo96_sWp6UEN0zCXuhYYa6dNKNxUDdnjFtDz_aEQ0ddgp5uCBLWZYWF5QMutPNhJUkvPY7P6yPoNQYk_AnbiugTRONFIgk5Qrl2JBAfqVMMlL4vw98Bl2JUjAPAX52eIp696PLXsnLHNalBLLmC7w_mWISx3sGvMW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYSuT7HYnRsPcUae2Jsh4xSNL-jFw0dREQFMmCkTqCDhCB3CE_88pwPfw5PeHvnd_hHB4cjE58b9qYhKZFLIcgAWbm2-hPM4BWkawnt5b5kqblZSLzjGrfhdd5-A9JKHVqKyy0DM-yMa3Xe7wzqNWIqPl6dLVKrunygXq9CCn4wPMrkqsn62RLKNsVhuCbTC0bLurocKZGTnJYYWomgeyQjNITNIXCOftTEHaAxSiYMgcRKN6-hzoPMsbP7DJDCxwc4g_uCcSGwHvVQdVrBICVPS_GfOL0WFMvzMtsz8nfuB5NRKH6K86ox7tgwWV1KiOrafjrJClaKF0vSawfDMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTI4lVWLwQSXltnAFxyhmlv-SQpF0ir15wT5N4WdKaSSQJx0qkEqwTkNbXhaziP4xNZ5yGylCNZ4FmOHNmeRNA8tJyMlDEDFOITjvbmTKGs0ETn3jt4idjDfCnvqNAhfCqpHYRAWtgozLMWsZxo7uQ_1KN55yWFNOMBaqcCq02uTO8WLUZdxT1R-LniGa1xCHWjeZdBsPBWq8hV2A_TAip5_eznIfAzN8s-kbnInfsa2bJxA5BRzvWYO7gdRTOGIxnViHfVvwDgM10rwdiHsjKo8yZ_aoSp-LacsCAhB6JzmLbuZHJ7WxaUWhw2Bcxco1CBKKOzXszsy4tCqpHuL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKt105gPXehwfkhhiVy98H5sLySZwkeWMW3Ni2iBM51dPQVWQrMWgNuScd3iwau13ujGk3lYBs6JoDLoiCgilyJOzTMw4no0oULJmzhADdC2ctn5OjkcoUt6NCWYZfcZ1ZBL_1ycxYdBWsvCDVpFHBKUQMaEvOJWEWOTHQyYrpKor2mdyPK5dPM781mJlfBT8ln_P0x43vACBbKSxNiFZZnuwM1mmg4sAiZkgGcsQqEK8zpC4723SGQ9czVNfx411UjS5l8pg0f2zgWtCgSXhWpKmzc98qWI5wWEXwAJ9xhlMiPwCT5U0TgGJ_zcd96cqK7rLz2c7583VIPgaV8YtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfMLjVO_T0BdPOQX8lHjAGOaNyiv5E60HdrgSfZDxF9-ZvTsiPuHka-OZ2t_k7aQ7_zZNDlvQt9uMRkv6xdixcA6KxLoabmDrN9MkAFlKSUpEOt4ATHoGWuuun8g3nNzDLA2e32nKVQ9LHX8T9RIgTGDYsuAgOMQxvhfli4HAP-uV859emngL9MbY8BI29n8Lvn_58x9o3CIbHFef2aCHveBvRhmVIuL5pSCGZZccun6hTATnk1mKZCHEMWsAh9_h7EkiGrCmwvYVtM4GEGpgIf20T6GqvVlGy8CwwRdLTE74QSutjuBfhFJrNhkiBH1r7VLAsy4qUviOiHjBEY8Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUDbjk5B1H81tUIljPaTC2xdGNz2Q9ZsE2Qa0Ny9NZIeoW1NX9dFTwYYhsjLYKgRQHmAP5OJghlw9h0ozcBV9lKjAMLIRf1r5ApNkCh2UJKpSAocT4nliXndFLok1E3u2IjHxCFsjJSCzbNIu004jW9Fe3WiyrIl_-Y9rOJ61qRVf03oXq3-uMsL4M5PffphKTJt1Dr3kZQDmRyZt14qUdAIdwVZqcyV0YYjFik25EWw3buOog9YW-P0T322nwdUkf5DcUg3YvbQBleYkhkOLPy-Z29j-tkxxF6sX9MQ31TAwmsxJrU-7t_hBKmTEz2QbaWARbBwoOMqU0iaADy36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if8uQfmrMRg7SAA9L1tsPzOrXFLq3hQQpoexbQKN64RFwNQxDyvlHaQ4P6ZsSkUlCGoP88dikeuyahBdKOEX7e-_bB5gjClfDNirwVCOLxsj-Eklhp9MGvzbqhTxnRI928YRCMc22P2SAa5qjxKSzrlzOFdlcCbmLNgc9dVsQ289oV_Pu78uwocovFONsU8TYcTVsPNuiyYPB5Zwv8wVjrVRplSxbyV6FQqTeFzY33Q3s4w3ZxXTW8UAarDV4ZG_rxpmLES2kQeD3s5agDMQjfhkaopAnte5-1pHiYlM2mF7iY5PjViXYNmx-s2er_rjLyNWDLf9XAO6a1DUMYnTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_V2IxQ1YHGWRhrQcCUX7idKM2PzNDzDn5svbxSbze8AEHVdWMqCFnro7Y9Cj7wdMYogHgL2sm8VK14h4DwXbYju1yIGzGsoj4B3GcHMOVMcS-Ov6Z9SpiYO7uGE4xk5nJcadPUNcu2efr_jJjDsBCPq2g5PkscGsVG15kPn7-VQUlW-sx9XLZ2fe9qfgYa6AQ0ybJ1WHXoFaZmidnPMGXjXaPLaiQ3brvV2feFUobdD0WLsc1wVdpyGfE77j_pXj6evJCLd68OHA6Vy4taLQA7dkM5ekv1gpKX9Cx_8VRAtx2PDFmzjgbdU_c68EJ5ahzS-1nXzVuoiCBXjhPeg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl-NfplF5d_Kcbj5ItJhUs8Fs11YNM7OAVSVpPmOAQZ3CC8zCqSoj4kW3ZxFLgdrJo3RALd6A3wBXcbQJ7dD7UEIU5AVCy9VOQkb4P8htxeRhqWdEWXZlHAQmdqgp3zmXz2i5-50sEXYAv2tjiMujquMs1_CzHuUQ1AMF5agFMoPyh0HRVCy9fNR_RGReBl5jSq-SspJhONphX0lWdfV8i4p6KOJZDCM1cekJdiO491itGY0afNxLip9_6-zBGRsQqzzh6MU3LIcULR3vLfvQRSaJiFsRSlRv83b8G3-vH3i3RICH8o-baMPQ9vAf9IlRFp0eA8LKBBryQvgbefUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUtAWLq3p2XSdPYecE1CHIYlPeWF7Yxpbn4eJsLX3knoqmAFBnE51Q-Z-Oa7-cIJO9HUrloOAI87H5DrUd_-NCgug5La1P369AKHzJ4CU0LnwVuN0tk2nBmt6uCi5SHUUJL0W193_l-mJ72JYml4EpSJwiEvJvJbWCXVru8lk8apHkO8P_Qw8C_-5GmSS5WA7JGcAhoaNCvtoQF9K7yd30g5tgArmhVOPluvnNnokkgIMMWJFyCDpPnlEixWoFqcFgd9vUASrnj9pNPi9oAmFSmn-eNy_4Q3k54jLNS3WaODTGegWAKRo56PM-NMJpA0rH8AiWURxvrSqvD6f1pnzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lE1ny2Rpw9vQxlrsQi6WM01c_Vod91IJzt-GJQfWnshA2fjlke8S_PA6oRLiPTfFkF3XJjsPbZtdzIWkz9yGQEX6vcmIZYrfEqAx003kajVGOXC67ONQ8zg9yGDGcpPd8scXQV_joqxtoB56QUm_Btp778NJ71jzp3VWF_x9VrY5lLtZaJh21NggkmEg21M47S0yGxb5EiqXjR_9Fj-DqsN3a0z06VoqTsOzQzifrf8wuwFp8dYmL5ixy4fkTkygB2o73ZFBxnWD0FsFIi4B2QmBZe8K9stulN-bLwWTy7-wBJFqJ36zQ90JC954t7N1S1Xyj6462xXRKmXnbECguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDl3-tmVAhFtJHbkglmX9KZysdIthNhrGMBkMFFiiM3dq6RvlMpSimFlY4NThm8YLOis74D6gXetT9OILDSAV7WxTHgh5ArMcrnL9zsSZvLD4716f1fkpHzDa71Pbw2ueKPtux0HKS90ycfUzecvUxgytQhfe0AjZHHFqCsMf5cIpZfASzRxJC18q_iOwYwfBrzxYFMgjtOPjC_IpAKNaah0147D65_hb5iGTAX0zNtSZqRF1BQIWQurQ5nUtrPeun8l3r_hoxCrBVB06HHf9Ee75nfki9nuogCKdLfs6xpk414biHnkT9pxh9rfkotKXgKNhiVgGuUMt2U179zY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoKZqVhQRylI0KaLydzVeoO-eMNdl79RcJNkDqfQIBVTbJwTqrs7TRz7aFu--_DeKj-9Y4XvxmtAuK0ccke_Of03U6If1te9nIJbk3UxkkNZK5FF6tWIddinw4BH-ocDawKCZDRbeYpqsVvs3dCgvfQtASF5MWWUr600b9sB9tgu3i3jWA900Df8iLDTU0PYtcuXRt01qsXdd-zsjaiIE4ZOSog4EaFgKmy5x3KFnMEh6Sr9QSsurU6syDzZnNhf2WunP6Ze5ukez0c-Ds4TSR5FLIwxOkHONccqbHHjP33jFmiPVip-JaDglsdavG0hX1pVH6vLAxcUsU1OU-mDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2I8izio0PqseLqmsyehEYEKKoGQ3GccCfngKBbQHKiX_jH2jg0TSingThHc63ZXMoNeOGNQ40UjsuooxkanhInTjLtf7KBkK74Sl1nGNWgvSyYmb-9gLpMyuuvgmyM-JDoF3IzAx-ilkhr5JdjAB56JylWzo94bRh1p6b6h-OYsi8CQZbQ5sWdGhFqk7pL4Ut8JP0M73POcuP64S-IM5OFHtgOeak7PXMm_NIbigNZssGdG3eI-LLgbMk6Z_oTd23mU1mmb2brl76gTVW7pp3v-TdifgLqU4IA6Tz9QK5SWe06NVExYj4JVFcsGz6w8-o3jPrqv65pcDh4WGVTvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o947mpS71qvmBDhueyZrs_3bYiMtvqdB1vfkjLyxS4S-EumqmsrdEExvkig9mmw_SQTU6-SN1F89EPOel8dMpprHG0jXIf1pgj5etTesRNitWhT2LKLOdPiLHOp2sN0MXKjevpamUuC6y2iFwPYZfKmQvSJONgLTss0NS1Wnvw-96B82rpSDcq1_OqECvzRj3i5JuCN7fWteIEg2LO0QuH29vLbwlljq9nhdNdQbnDZdVlGFTfiqjGD4sswXnk8iBf14VDM1xdgYHljfF-Pqn2x777i-_31z0A4Gmbsq9tKTQKjozw2QVMu0tQsSydmSM7Qmd50XUSeiPqNaSBBtQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5u88wxR61jIEp-esXg95dmYIrZNKyKJAeTy40rifAZFEWI4kXUCGtKvamF_7PmP8LDciwPQuk1I4EuEMxaDE-mT_DVMsU7kC1nOsGrAhLJYqmG89mw0Pvs42Jk22JcHOsi-E9B5tRsQZngdbibmngoXeGUAlVnqoCnieZ7JzdnTYpcnGUtLCsJj_pDZlTc58BQz_rVhLH82MXG_HuOjnHKyIQMC22_FCDDDZIe9kOhLY4-e9J3yfXMb6kN1UTA5Y7BJuVEvt469UgvXNApAaX_OtR4UbskbWKAYuMM3w6QXVPZoe1sMnfmGYVpFkHUC-4NQPlQFJj63MlrBDAxTbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBqPMJqRoOhhuB5UcqvLrDYw27OHZbBn9f695wQyLeVTT8AIaSRSxs_gW6WMwnaVt12aMLlROOFoL8sjzO0lrTcVtNuV3TIIZ5LChvJPqsvvOYerACm2DO4aFOUcmurVyqzERc7WxSqwLTc1ecdlUO95tC-pGiSWOWf2fx3nlnKH--qzJ7WfERLzCQXMgaSRqcDf8fOnS_hiOYHZeW8qPHq6ycKdE5jwKI_h7bgppIm_VMDYxsunZ8N_ZKkctab_gNOSNLgr1vgQ4ovDE-5kPErktwWnQRTqICVFUyoYv5iE39cvlHHzAAR4u3_hzqLYC38i6KYn5srHDKCvheBC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN8vP_m-E9Woc26VxGpd10ZR4W1ncdVCLgKFgH4AaPVIHvG_-hVOVlRNYnbFjsfoHaTmk_v7GDl7aJYRa-1KCXMINRWeyW_Z90coN97Imm6xSicrUbz3XsxV6R0lTsJqlhSm8W5wYtQ8I4AXKX35H-KoILUCno0GX66AKvv5rqshew21xW6b0FATJ3o02gaPdxbs13T3AMvJ6gdXkcvcpDQBvSwuGpUz0y9YbcPWJI8Fq89lpCj29W85tAJlTMnsm5kC63Onl2cfbEXmShLJbkVpAFQJKFAbhN22cDmFGbWMscF4ALOpa-pe_jiTYNI98GNXlZxS1RHCgk43H1Hgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1wzyBvO1doxGzZwgDur7fUkASSBlFx-1e5W7WNJOdd8qzUOIm2dfNExtw-7KshdpTDN4FHmdPtBdQYxzqM5GBQCoxEbmMrYJ5fV32RCNxBMQglFahfqMp4p-T0GpxUQ_rQ1vfhqGBLhZVmB2Sq9qYVHaQYh_v3kGIhIYze0vKPwSrCgANpFftSV9OdwfbrBpEj0TUSh2CgAqBlzcANARRKv8EdP_Ypknp30I8iyCUqOtWLINc2kjkA53v0QUgw_w_jTm9dRC_pQfq8xquBaWqxtlLhFKv2OdJZiJraMgxbS1A9_sMeVAVIjzMlkm01lpknNJmHeu4t4_iR1HKM3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xj9vI3tH0M-lQ89-DfjPj8NEbp17Dx3f-gEVE-hxcnPQcMJYBC9VOeoZPd4KCoIw2ToLe6KRgTJtZMLSYb_fRCZWDMAZIyqdOH67xnBJnAlkNlXV41fEuVtG_bF2W9PEFNOwAk-0iUUrTOyGvJQb5uWspnrKivgNZDJcPXalWhqzHojoKZr6BiinhiK7AqeTDx-68PE5HqvbayIj1CDaSB-dcRJTPlNw4CzK683t7USKBYJWqpYIJexNWelfX5sqiQmEt5HAugB-sNd-waTrPKYvFKxisd_lDc--s401cm7K5t8GdLD4ewaMABHf2Oth7289JNAkVxjRdbxGHYXHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_llwdv8wNCnI1SKfMVn5qLXOCWW8IhNfD1RBNxrRWvh25a8dW2n12tI2QfshSdysjQwQwdo6YCzxm1LoYt3qLHCFUrmxVWNdWf746YVbQQJjf8JkZ61DkThlAk4DpBsbohwwae_twOXpE7EC-0twy4vHDz4bNAg7EXHTxLbE7HHKchzWd-hRK5UgxSk2ZmHHgnc_LQ9pIOItopa-Mc42_aC1sY6YwtjsPgkCBLEM4zL3WGwxO_QYEuAPa2GBBAZMYqFeLYBjlPiXLjr00Q7YdVVDNM2MmIbSlAgV2nmVn8a6ZVJqvOEG9iLkvIW8EZAK2SkiJy-h1k708QN46e__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcuZAN5IFg4xcqZPJqVquaOnu72RKspL7M2fjexqzl_8dlX1jbyO9hrMzks_P-7GoxNw6vdI12htXAVqaAPLn36dXHq_Cw-YSfezqmwqu6KZvW-utOKkbVQQM5ffgMeySj1Is9YfF8NgJDt_-ZYvLVWqRC9iJx-eMRS3yHVPKr2mTTPyK2maRo4MTrkTs93IeoFCv3kfcyemwUplVUUYXc55GACTeGXUIh-Jk1EYXCBBaNAnYf0-JYg7JhHRgHSAXSXMtjmSdJr7j9Rd1uP3emcTEKa9BNP8AXphmfNv5e0YeB1z4kY1YO09da7OhvNGzHxXGuqIg1fmzpiPX_pu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPQUHoQHGCsekeVPrrSNJCFTw5Io2yeWXNu0xZvEFOuC4FeEXsciXUiDULF5wzGp_paxEmdkE64L9UBJVDxf-IyjOlnOdJu8XdKZcW0ErkXWBf352O3BAgEAEBaPqqsDwcXJHqJZtQFJFdEZtXkYO_3suy75rvnH9oi3gk2MIwg4nHZNeYy__s1HDW-akEahXNfm_onanmzljhNXSYzi0Q1gPnw5vepx83lk6633nQ37hIdL10T2tPodOx36y5_qAeQH7O-RCJF5cto_ok9xxOduwlOFXI8gbP5-ryIyK1T3598ol9vOSKVVvIJlvgmVxTENQ2hAk0XnYAP0QbD0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3ZTjOyKXICvkoaV2sT8PRNldB-ZVEqnk6XUwe78FM4E43UyM7zwjLlbkWVM90kZ8JlxPg-LqyTqoqmVqtHyeIUd_BhJJAnyKl5gHuTTx8tX3_3YcYRvUY7RN5poCt8LBBtlfU4xItv6vgHsDdU64Uhk43YGHAC7ltm842bqgQNjCSamKHgaWymbFWlOvoy07d9dYF1aPyicdk3HypC7KPGmasYj3Gr5esyHu-2toi1Wg8jFCFYehN_C8E519_g_SdscSco0xvIghrfql_cucEzu2xbSQWiHZzYY4hAh4hDD9-xT0C0n4iQ9Ti-HYzcs6YFccgpnNqbbIPQelV3oxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O60dNSsIT4UnLcJcPAGd5oX7x3SVjbm7JhxzXKSIeEUswCBI0iRMMw0LByb8y2F4lDwCE8rjHct5ewpeGn7-JVbLFZjreAi8ARgy9WH2KkHemn-KE42TDvrm_O2AAa4XpgLQbD5uq-OVadhXQuvUYMVGuWvZXC-lS_Z7CQA7D-RuF64f4Vjm-7Ndw6JwYpKlz-Pcfv1Ct37grvnd97yLLQx79EKmXlR4x0xjbd6Ee6so0xGv3SmGqGT3UvFT7TinH06sCXLD4Mv8B9Ovoq-KM4rDHXsFs1bhzDMPi5Ll1OvUZnTgMroWtmvKcst0vLbvP11DwEE5JMPhsI3F_opRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhAINgBSul_1QQ7D9T-11BhtaUtqKr_-8DWdS9ZzHRzY6wZJwBHbcqazqJQS866K3tFHN-ZJEBWzin78ENS-UTuRrc5Lv_UPgrdCPNtSsYjEt2lYWfrMFSq9pxTIs-lCMw8l8e3Y8TVXznx1BBAYIIbxsriDVNkgb1BLxGAVwpr3BpAXsVk8k5ZbACCyG0B7Fe3bL-AZmaC6Au1znoVtGFjbz-zo4CMCC3OZIS3xnvoVIY3LeymrhUx8u0L1H1DCGVWL516wsuxGCpjXQSitQrZubHVH419NrsB_3BNr3zVSsvB774OSOU8RTLaCXWtpXNr28Yfrr_Lr_b84AenV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcziuDGklAjK1gN90bWZF4_3CSGtDvL36jMcgJTDr1EFwdM945IMvcwkE00Caw63OXznmY7qebPVfFCkkkP7ZV8eZRZpKXPRe_c-ISzTeZMc7Mz8X7Wfx3Eb8RlYr_jZPEgNJGDr2vRSe3mx2MSQcqhg9tzx-TMDdjcydVh82tNqhfgsZnjfd5qVDJdUPuS9g4K701nEcG4bLjuUbQVfnnY8upA1UiZPlJXGkICJXnJWQkQjNwQpuSpy8Y7a2FEJuBAln7LKtU2-o4t2X6rYsb9srhlpkEiigu6kN6Qi_3qbaAQKKlQZUAOk87fArjKMokLrrPkLEP20bMmpgau2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7PyV1mSl7v5U_Tp4bW4CT4xK25dbAHhs16TEXEzmUKKVernJu1sXJymyhx2fLGSfbg_dUQARwueRf6rz9Opwmx3yz27CYNhsfZbWBcCSwoVv-KwGC2LZ6Xe0tVz3XSjoL0phehArvRCsQRWdYV-ILm52dPshePy3gnRS5HSHfGiXQnoP6admdZpjjE8yK99rjww_4ZwCgq8SG4yd2mcKvbtRa_7HMbatgTh9rpyZCXOm3yoHedNA5oKJ7QHHozCmexm0S3epwQjVjxD6x4MtRGXBxfF-YW9LtwNDPw_F0F4skZg2mrfwAOm8q0JlWuvAtBEMstPzBBFoj9mAx1wvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kToMmVhjUQn_SnWnonAbSph1ihgtB_j4ENwEFVe_i-apHlUTNrkCcmu5sSwAaJUVz6Kn0pg-n8z0C5t--n2GzGhnq3oSuD1ZGIZRzfHBRXOnPoZGRFwM5VdTdVJwHsZWxSWRv7YoO-pOR_azv8dpFVCmHH7sRbTo-oJCvuUJQnvrnrIBhPeuuBATfPzDGy6mrshujyIRZ2n7sZ4GW6bXgFhtwu-ycezhEvWHn3vNhqJnR5iIBRRXLq2AzqhHK57y8wGOilXcqNZRtUJhTMVViM1let5mfwnINvL9jGQ64WJ4znlkGbZgmycgcGPFbzXfHa_gB0qnDbyLF3CWHFUmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdQpXxjFhhc9vSAwBvP48M6UrBG8nYr4pz6kU5L2oqtgrfdficbMYzLH4T01ev2jCsy7RjSsyIuM7eSD08GItPqBNMqNM9tm0dvTxiihpMLOT9roIraYYJymgt_M5qHAj31oFNwRhhXok7AAM__pqHxfqZiRQflumkNjQIhlwJX_tYIxH46W_-VsILF3EDHKyHf6kA1GDfJGuHwOWZJ1fZ5q8iaEPv1_ZEktfUvFqPZK_LSacGvognvCQMsSmnj3X_3YQr3zLKvL_ywRo_kH2pGR-ROtcL-_7c0C-TBI4aXKpiI2ODwNIl0uFyP3nkRzPsG8QrjfVNIP1UGUssS4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=nRYhuByT96SwswQ25AGJQc1jQHnAZh177wFLqQdjSGjHJ4Boi7mVLVOPqzKCUreXcg8gNz2TUz-MOAshSwAI3M3wdczAkA7ddFsXz5Wpugz-6dNgLj2c5E7j86-cJ5aeJ3QqTbn0nqVWk5-tY83bz7CcKMQD8i96QqjVS7aKaLCQv9WwbTvATVP865hLwmp3TbYfSmpXGf8B56-v2rrODfYv4L76zzFvy7Rj_C3Q5EmAEFfdtrkkfqFlHTcHLoR3QU--hUQKCl-dagFhrj6_NSxgc0i81VOrixpbmkiXhgkPa5ibLpR-75hwIGmBTfOF8Xb5wJ6-YhC1Kb6JF7bjjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=nRYhuByT96SwswQ25AGJQc1jQHnAZh177wFLqQdjSGjHJ4Boi7mVLVOPqzKCUreXcg8gNz2TUz-MOAshSwAI3M3wdczAkA7ddFsXz5Wpugz-6dNgLj2c5E7j86-cJ5aeJ3QqTbn0nqVWk5-tY83bz7CcKMQD8i96QqjVS7aKaLCQv9WwbTvATVP865hLwmp3TbYfSmpXGf8B56-v2rrODfYv4L76zzFvy7Rj_C3Q5EmAEFfdtrkkfqFlHTcHLoR3QU--hUQKCl-dagFhrj6_NSxgc0i81VOrixpbmkiXhgkPa5ibLpR-75hwIGmBTfOF8Xb5wJ6-YhC1Kb6JF7bjjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhUf1RpSBeU0MGRLxAldu5Zxsu05rqPFBJijbNK4rTERSp_qXe2iIIplaj4cUpY8yISegHPDnU3KUtYUnarfsC2A7xzFUb9wReKR4Y7wPjiuY-Xccgb0blOJ4hnpE98QkVMGh-Ktv5WhVBq4b4Zo5v8rnjjgENRMstrX3lJtXoElS04PSH_vlZzrUFPui4QcICoCG9duhAYhdTyrAuECoKvzscUk9qUDv8VX7-j9fjdJax1hp2DopkAnoiIy8pJMS2RQCnzk2O4MNX7XNsqynaOs_mDnrIQuezz_DvvaujrCHs4uXfhrRs18Oz2u7k97jSEv2bprtvqjqvbPjQFOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3XAZ98vGvDvl445r4a92_dyWUG1BvNeZGGlWycCsp65Lwg0EWY2kHCOITLsdcKBfnOUldqkX_3F7PA4WI9KIjNzGr0FjWMHNG7D5Forz073RTy0p4wq6-IumdPe2yiXxVClFvQa7ChRdhQAZCzlmcjxCltOGRHBYB7uiCGrL4O5Hm-v5Gc41bVUZfm-vsDiy5h1NpRWGOYwMsxzGViXJMQQepPkX7eSHielYTNzWtnX0EGcsw_xh7jrtyceYdGNHsoT0Vda97ABGAznwOCqRqmKenNDVj1uyvCbNOHfhyi2YtG48pHTvjDpnA6MPu4k1DBAu_RDIE9yhCDUXdRAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NssM6eWRNcc6F0d2_tNB9Kmc3JJZhKsCRvxBJF50nonUVQgoD-0RTy3VQzU8rqkzkxic-MA5MJcMcuhH8WXrE_M-a3eDQiMqMKI5V8gtyUIQqkoRu8AXfnR1-4bc3ysFR62aD8eKwSgqbzuzMlzQUXAKb7Urf3jHLYjI09H9KtqB2a48w87CfKDTgsuYdUT4B19lu9XkmrSwA1cIrMZ7TXfx-VF_MI88IS4t7J540ismO0cr7vPcetOjbxUcyc_Ff8BB4iimtt-mAynjek-U-IcwQmPSZ1QBDoV1iTh6LDlTQwWE0XsTFdVevOwQ0w-44gTQh3KuVi_klGM8N8wYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bbm3k1WnrTEmxyArVR_RI82G3F1rwCmHS-CqLN2I7QNugOciMpOn5aDOVuVo_7CoOmn9oJQ2B-G-GS9nUdI5xLMAyU_zPoQ7iizzhsZts-pt39srn2XcFY1tgmrpDnel6_qE8SMoJ3aKVDdYVX9jomsElNLvhO8ZreLN9iM8OiRsmBhMbmMvtrBbx0dayyOMTI6Ej7ZByeWo6o_qGM2pxC7dTQJqAtB9HK4sa0rc8-UR12r6ExzsuZtaYUFLuTV4YvmWp7rhrKTn2imT0yQIO_XATKTTj7w3Wl2kuUp5XAQ0onienu30Eszro0Sfu8g1exrMItlcb9HFU4bz8ige0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehf-i7UeexJL9HCpM8pO0dYGHQvlEdIC-r0JcwIxE5aDN21zfKFpSiLgXrmr6j2-CVi56LIU8uovHgbc_9UD1JIR2mJD2RFAPewNcDRC6CXvWeBbKTVMUA8fzwm6wI7Nqw-rWCs5fnjElnLyfkM2KLLgeT8g47sGfTpmbklBFGVLn_uWokNND2bciog-U3Q-KlDCs3mhSKaZi8Dp8_XA44xz36oV45VjDeT-sRPnGpZKqVE4IQFKUubcsHvii_jNo3antUsgxS-lvklytZpNU31MNfDKz0GKbn671GRla-wGNuAZssgD_kLQWy5kuCpBAcZx9Nez2DYkp23nsZPZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZei5nWhZl3kEGXIJkaVKs0OnMGNOEe7X5WXAhXWOHjUDDjzuqoKGlBTqn5JUSYywTy6T-WSjoTVqRd2nnQbeqmJjfD5mkH44PJ2haEzxe7usn12LrLfWkkDE6JaQnyyHjl-uc8gGYMnQHG54x82tFRNn-ulEQKz2D3IH5Uj974MfVYVWy9Nv6TjcZ8ggvxMdhA82-y3L6NFgQCREOaavKpzWQfD2goWzT2AfwkeTz6aamXbUde4A_x9NGiNNBKLiXLb4bMHn1iLlMJAWxfZD6ELsZ1nl7AS2gt6ZVTe6FPSbyJv4b6tO8kJgRQHnL54o44bzdhysOgfKcF1SIZ2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU8g8b56gxxsUFP9D3ZGEHfVulK1kwEQIDQENZxPpv7MRQXbY6MGiqOrBEGlfKoyljB9whRfn6DcjTc3ll9zPo2Qq9yMp8SkVjqsZFf-mu4OXrh66bcKR7h7F_LELs6nPCo2NV0m1z7MKVgWj8jGgrdlmbcIweGKSqnCyOJCBVXiWkvezUqULZeQ-RMiTbmhhdruF5Ql7eScxZVaRE6QjpMdppcDwP4WUAxQrm6pKFrlC1OMKmVQNM4v6xithPMVWTRmD_b0L3azP92TyAxJ3nnLjMTeltfFCSJi8AYowLFO2vUTJHOxDdijthIopiIn8xKd4fjXo-AGOarkVG3o9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inQxVcTG5tO8BwIo3P0ck-lYPitkwu0Hyorntzah8MvceJXhlPw-xbBGn34j_IxK8veFfQli8_Uar9LA0QVLCmhozfMJL4dEewmD1Emx-d3g8W8faZ9fWOvd0n4OW7H6d4Ct_F7d5fiib6BWjV4sAeOLGSC5jJZ2lahiGO3pnZCkPjIyOxf-LqkUordiCIhAFw5LLI3HGrAP58-ClX4f-IP543f5ZfyoxBT6ZCDuJVB-EjgKonrgNOPIQxZQ2JnWxmwTCfTBUnEGUUUMyiLasfCD2-Sq7FUpR0UU7tNL5ZTBSkkT-GQX1XUjrImzzS83pougUf97vS71aj69uH1WZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaTymwun4IaJJFCqm3gr5s4QTpie-fvjcmBHENbk3O2TE6yNi8y7gUh5HpNVdlH2xeMQHvXdVa_EFIhG6IqWtjaK6Cnl4CmoFcFk-vAxHcLDYLj40ufmGxbS9wauxfeYvlnHwt4kc52XM1M5094oT0YjH-wUy4o8Ehap7qNWdwdYYgrGkiDAFXVK8fZh9bW7XynNn3aq_0lMzOyA_Ss1PYBhftG7AK7wWr4Zlozzmp1qi3DTVO3M5CR6bfTzE0PtS_B_AA2zYNXfhRuyeMlbihYUXPmf9svwKyvLqS68d_dLmO1-3vdAWQFVQyTOBUtmkqAH1-qoD2Ka_vm6px8-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgmr8f6pIxo-1JtND1hd5OmF_NXCIGUokusaLnBMQVmZ1gGKjUyezmJPGwc6wUsGw99U7MDqXYv8UiSqNMWVpGs-2ff8IH2bzBMZc9wO4rkTe7CiAiWYj1MRUZQwgKBgKPGl4L6o84BM-iZmLRtsl8RpyHUUOb43vxAIKZ6Cr0YvS8QcKvlMQGNlr_eI1zQ9bRNiMen1dGaWOo4o5UGUN0S990aWulPLeZJaldgpzdVXnmFgs-J2b3VWhA8_WqORxjuFIhXiNEfI7cNGY0hjFLI1dAyBrlrFeVrejx9s0wB_LwPIn6aiinZHPdAAzRKatroBECuQD2ll4z5FzoMAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaGpN807iijTm3WQGol5F_S9Y8dTx50EvRGRH2vb2z3U7VhyIq5MM7cFdMSYwxGSIuzop_pt85uVfzIHn5DCZXjYl3AqDHZy_t-imteS9HNj0Fw3bU5xOmje_BLb0WGSgeD9msWz9qzUTnNyQ6S7pE6-bZIbubGqsTqGPMERm3NmTNvSy5qN_JhuSOcHTRQaQ7d6ES2ce82B0VeW59hpy9sIfwTG3nxEFPhKOMq8NtR0tGiTL1GNq_ydY52wv33Aev53rFPd4Byqa4m0pXdcBfyHrT7key5jMQfkzqjqc5ON8ZC791fu-MnGBDZnP7vRX3-544Dgd5Lhs3mrpZCzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp5idXqKTEbtMftOiEnnYrkK5EVujhqjxK9UiLklzz3rf7QORMeIEK475p1zaqBb6ZX26BIzfV7l6o9-eJ3xgonTyK9T6MNElbzNQ1XcS7TvKF8e-Z780cEL1We701KONFN9d5xrfOGXPD0iteAnhqWzKWfy2LXfgzpX109qxKmWWieBwsXPk3kuPAC_-cx3dnzXxoWTaaniat-k3Gb-xJj32FV6SlGH6nxB_3bdDPtFpGfmZDT1l7XcqhRoke494p5SdH3f_WDleMju6bu8WN-7MJFPDqxlrlUF03zflf__B1zPVr6vIM7Xi2bjWS1aHd6cifO6JdyGybzA2eBLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZPvzj-4oQLIJjQEmyqAWi5TkXDouRdI-UnmRt0IsJ285VaKznqdWLpoDRXk5iX1J6w9v7bw7K9gTAuUd1t7ki2F2FMkBBfIrpaovvsWFBpxFKzusEjyzcYzQ72q78sq0A2xnoZ-eRrERgB5b0KnsE21rQmL7kekXb4aHNK0vJJRbCap_dTwjxnniLO-_gIafZ-X-2RC4iXgbdNJgLbGmWJhaKN0rna1NNuPzLmMpHF6HxrOEUz0ylnDAKc1DGrGUqgSey6mPYsWcPNEBXIyRSUeHmXOLTs9tNWncE45YJ81vJbXFcEigZPsf4Q-XWUDdDEeQL7ULSIOhxzMIkO3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3xRhsbogXwpjnLl0L8bPMBhib2imBsyLsjx3OGCq7baSz284Lpha1REN0e8e3RahGvtQ4dbIIEsPn-Y3DW05ToSVlB4vMRLB15CYc8ydt2UU4fm-XdaAX0ju_XgwxUpIkXDgLynoErsQQvdz9U6HIOYVQnIA7gVtyOlK5DKelMwx3H6Rde4feG9ZQG6Kv9MS7fLB0v42QtBc6s9s9JK2kTlZx0bIkw6TCyw6xnMbH2m1G_gXkwpHeFdcE3xchHCZBv7mLJ8KbM_yR4I8sDsygnCry6kLoVQGOo8DMKWNIqsezlxCjBlRRVziBr64l8votBcaUW2tohGDRqnLidsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5P6f3kJDguIjs9gQqofzoOpi1Pf7so20RSmQrBtyJxVBALpBk5N9W6Y31uXF6sGCOD2KkayN1PurkyerJIP8nDzytLGERYHRhJA6O6u1gtfup-Rp5m8VATx7gIV5TZhMLysRPcFvnwkOfi0jYGFyfEQJOu2qR8bL1jETa2UpMByCFM6hUsd9pQfU6eYg6rRwmPz7LoFAd5Z7o472MzK2TF85IHMS2RNYk1lq4WN4y6X6a1mezx7jT9v2fTVujM0cfF351bP3DnnzJg0LX1b2c6KwMqUvIdQTHPOZh6cCffduGwIZI2RwdVPZ-sA2sw3a3aXktzZDUdlDAahLB6Yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3sLNRH-YFANdXCCsOUmQ1K4-RdP5dEUg4EecCTqyEZvzR-SqYf_f8N2cQtKcEvskienvotpPcQTtJ9XlyDmhOaK8MOSJjh4smdkAfa0KkhWNbEH3kxeC6KBEpqerWv9U2Phvw5wn9ZOqhqfLXMNep8JV5ECCBiWDC51wUW8ASxx122rWMeqOwRoETC0EsctvwDSl0y81UoyRb9uozGin-nXUFy3H3TFTNnBXTmt84Id6MLfvmkq9_uhTXOlxgXmDvhN-kX4LQ2BYgwnN0ZRwddP-RG_RXYjSyw0AQUCi0Uzz-kP5UupIu7YnVARXgW-_6TdzZaDGapvBzVf6BcsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjV_NiZKwKAmUj21FT-xxZFD69XYKyrU8eCI6WNsbUAfHm6aMEGrPobUkPzFPAjCmXqk632bikQTReIes6_tvQ2sjekDnkWLZA6SVJaM5EPfUofH1I20bj3HV-UV-mos-AlL33MBnuwXYH8yQ8Odui4xA2FfJyv8f8wdiDQhLQ2YFTnzpMubH1YZQOocwuFQDlAffYDK8auCPwuldzGkvfOLT25if6tUvCpkk50C4s45JY8KyhPct66vMqOAKgLv3oSsApxM6aaH4LUYOvQFDuwwTC13wEP2gho39g2G4nj5uTed82aYM8HP_nJVHoI_pdD6jaiF6lZbqf0zRBiZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBUuLTRjBnme9N4dBzBbUmfA8YfH-YhOzoNo9NWnfaQBvZ_LwBzNa19KKfh9xU2wy-cFjYEOVLIrfikvv6XGKcdezNTNlbqpijKIQKx0TAsm8Vc7qOXsHEUD_zUmMuX-ND-MVCqEGk264YkYtXxUiZkE3Rz8hOqvYwjo7woNr7sjkR1LJ47qWaBWp1tKwRZdYgC487wNmnMQwlIcQQmEbcvKuCXs9NavzhT4EMTEst7gAaeRN7l3jSpmeu4_ll4Sul2knPG50fdk9cpM34roRz4o5tSeu2D2M7vrwIzzbQFN9HYuefI0bKCCiJDuZA9SctxhXfK9Ogks8eqlA2f1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8QxfTQjDLXOexI8fClwQjlRC5RQl7DVBwMbjHCIEOZI3IBY3GV6vJZjxbCnvZD3G4W_0yU0vQP7W-1V3_rbpa2EOPZ-bYIrMsnC7ebxvOm5oADWomssDHfE7ScEzWkTzW582B2tN1-dOgndYvQUXRy35nXNN6QUBD8BpMUWoY66LF4pkh9X85Yltcgt4KkZKDrhivrZ8uYBv0zIuY5MALLLvGUyC7IWjKPTc0DJf1DQHqXEwtsJMfhBhUrx8i5Kfcq7Q1MrlCFVh0MNDgcS7tycZB1EiVpXki7cIc6M3rCQv06a9UldwhJ_ysOf3yGPkf-bQWt3aIaPVajXr33KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVwbgKWSeJqQGXxCRrSe3iVLojFoieDmYm2TbtTQLea9IW5_E-ZbFbTpOEQUSqeIhzVoGYmt2bPSY8XcABIrES1KHbylHp0NKmUrzr4V06XjqAI2S1nuBe1iDqu8zobt8EXZ2hj08m0M0ZWbiut_iCKcMPXTG5B4WdlYTsVIQIJqBb-3NpXcYz6XO3UwqIIBLBguS-_2UGETyPyLbdCGeH9c1SwLlmhfs9SQ3ayky_LDTAwClOO9MYWIgg8rS_M7QMaulATeRIUt2oLkx43BS3GYm0-TaegdofP_r5_Q6k1c3ll1oJ7fH6UsZ92XhTY1cwewMS0nODkuXl9LpNdB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoMBMsFxAh0jGPrFfYF5ak1dNVAL4MCezV2buZETxWY3fr8umzgf8PQchkxsMVtGcA-d_CojSUlSCfcByBP335kuYFPVGWqn42sElKRGDFSRbGIzulySMx5BrOo_nf3CiIy5DvpzDANsfBZ4hGq2KshHGaluIkztmW-ewRzrgJvm8XecEAq3lJdCv7Tclkxh1qeHQzYD54MWtuPT5Fy5Suvc3DdTj_P_zKRH1BDmJ66cov5aK5sCVGz9wJGMkfPyxc4pdvoKrNDh7enVENSIaLuCiCATNKmuGrYog7QCrvhCMAnO0jlvVaqvyJqLSconPEqdEMhl76Mj7NvmzNeHvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=pLcsSn9k4dDb5JrCMF_3uwOJYp_aNEPA8IlFqmO0YlpVxNo03zwi35kISo0Fq4CCvxe4h0lZGsGymGKMN0SOq8xE4zdiVcwbpoqL7GaMD_R6nEMx0kv_1Wl6y5FGFCWDidTcPCWIYH88ZEXuU4WY8r9p0NIIP-RPlI_co45IcE81BVdTzNWD8lG7AR8nJEt15Zwe9vBbvlKkJR4OgnPiBfmwGoVcdLV8mpzLLUPCjlUGVTq9Z-SZEwWfSNL0Jv1eyj8HNUVteKm-OHmOyxeb6HibzC-6gIMre2k4H_UcvBhM6Ux5l763YLoRaO-6OwwIERLN6wkEu1wMZ035WfMsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=pLcsSn9k4dDb5JrCMF_3uwOJYp_aNEPA8IlFqmO0YlpVxNo03zwi35kISo0Fq4CCvxe4h0lZGsGymGKMN0SOq8xE4zdiVcwbpoqL7GaMD_R6nEMx0kv_1Wl6y5FGFCWDidTcPCWIYH88ZEXuU4WY8r9p0NIIP-RPlI_co45IcE81BVdTzNWD8lG7AR8nJEt15Zwe9vBbvlKkJR4OgnPiBfmwGoVcdLV8mpzLLUPCjlUGVTq9Z-SZEwWfSNL0Jv1eyj8HNUVteKm-OHmOyxeb6HibzC-6gIMre2k4H_UcvBhM6Ux5l763YLoRaO-6OwwIERLN6wkEu1wMZ035WfMsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMYKA4tb0s3kwsqB9JnVQ6mfNt15eG0uyCOAFpljfbtyp0D_1bPZW8Uqp8hpNqTjrKTaTRx5H23cykvmUnCKUIj5JnxaltMXq4PtbLDMGK35h0No37K33cTytdZ4BuD1vnudmJIvjrZqYN4D_EgoUIYFz62Jg7fkQvvqifFaQLJCf85K79d7T7JwuvFNBXTh3sXLycIpWccpzpakFmZdOBmGFhbvDLtf37RuDj3hLZg42XwErXB5AZIMjJgOxVLeU65JaW5ZlGRsemL_hQYKd3xjQUirb_VnyMLrAfTuRmrLD3XEOMkIjs1skQ1Pa-a2K5d7R-zuqkbepiloq_gNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1Oz8wtvnefUv6u_BuRIIlRL_HSYtu2MyNL7njwqulYiF-zPNLGvLqeTSd9ODkUh4BIC0GAEX1xdF1zl5ZCthUgvhCLzXEpAtJxOis7xTM-G3-Q4La504lwQZZEcyXpjOdDfzRM6qeXyzxJ3V0iGyUVdEQ9M83pQKm-l5K1dHWEllvS85cxAe44ukcbNg4Fif3W2q1RKA4bcYb5d8GykrwHiZq11Nd-3ysAmbjJTjR1bNWgPNFPHMur_4LxAE00qi3GW6UT_SDTTE14g4mp-vfDRU2Wu4jdPgNY3wW_elisM7AAPEl4ID0CTA53_w-yo-VXptmNcPUaLRGdKu13qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJYTHr57oO2-R9xGxhoJZ1hFFD8MVZlMT3Ko8ktCej6b6Iu0h0iGtyKD06xR0pu0my6fZXZLzn-Vjg-tfydgm9T1lykjFWhkdbeklmy3xevN0qiIboD7UGs5Szm77NIve25NUjqnyi9iP2_tbufwORwD12Hh_MiA4W7p5UtMIGYL1F9rFFtOf8uWqa57-L-ake83LUloHOvOcSJ-Uu5skkYPm1MqOqYTnsLWbfMZRlQh3p3N3eDG1PbwmD99q5P8HAgZuqCjIdWR9oaQ3kTltYrwUc8uVE6JeBY16frdGrkyIX_1CbVjuoRFmwwWnxFOhXzSqrb-DEXHMKuXMevmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=t01w1B2bNXTUTSRzItlA2jxNIjVmnd2nZMJaVeHu7pCOe27q44QGh8V7AtYV6Gh-PFD6mxNZ4nqW4lp7hhfmUQ1XDEPFhwi90lb_YAf0nbbWR1ulbCC90XzyWDAyMZX3LkiqSy8SXW0VPTm1kFzES3PkzXdymkVuwS98h04QllOta24j1beQ2N8q_S1F7iWt--97nzXlXaHgdZSRXM4F_kE6NLRmJtJK2GSHLPVCn-jTF_FJ7WgQCruEpHcbzq-OJsub3AOP4bPvWo4tQAhNjhKyqDpImbew1UhZTQS3VsNbEmsvSzDwDPzyYdSHs0jxd7M8PKQw0749d8pSXKor9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=t01w1B2bNXTUTSRzItlA2jxNIjVmnd2nZMJaVeHu7pCOe27q44QGh8V7AtYV6Gh-PFD6mxNZ4nqW4lp7hhfmUQ1XDEPFhwi90lb_YAf0nbbWR1ulbCC90XzyWDAyMZX3LkiqSy8SXW0VPTm1kFzES3PkzXdymkVuwS98h04QllOta24j1beQ2N8q_S1F7iWt--97nzXlXaHgdZSRXM4F_kE6NLRmJtJK2GSHLPVCn-jTF_FJ7WgQCruEpHcbzq-OJsub3AOP4bPvWo4tQAhNjhKyqDpImbew1UhZTQS3VsNbEmsvSzDwDPzyYdSHs0jxd7M8PKQw0749d8pSXKor9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
