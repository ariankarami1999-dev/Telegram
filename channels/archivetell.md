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
<img src="https://cdn4.telesco.pe/file/jjBIOKkKZ_tWstndsHwXoc5rrIpbWh_0m3CNxxCzHlqFFNERDdgOHFbESvZsGV2uj_vYtIKI8PHYBOvt125hBpme6LIWMr5VogtImecK3m6Hz07gHVebh1iEUQ_3YyyIJOTq8oRQbP6rFxipK4QK_qlPsEkhqqy6qXkz-cMzFFUspw0QHkd-XZ7NZxZ-8AJ74ejWjhOZ67ntuzKu0ZX2mEIKSgnN1HSiINffhDW5JuVDNfnMUF8rE2fyB9Hpzy4E8MSoxuHkCqu4jCnMq_7eqAieItX7tgLh9u9vJGslejN0UhhOY_i5YXYc15ZbYrRYNcvHjhwa0phVbj5oDdqK7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io26Ha5xayvtkr-MPvPcMJXzitsQEbcq-TIDoxfa9V5eT_YEz_P7pFwW0OjWpFxNKUPyp6bHTJURJqwr50S95Fj6A0z_VkyuNxOmlny0sBNjTX8JaJPev9EA1QrRdVAacjGlyyFiNsKhW9xJOWFwuHEnfSx526wcOKwb-v0zUV0HqpsY9-baS_1lw_AbIII_qquzZbFXr8LbFleRkZ1G_epmI5KGYBCLGoCAHT0SyWXbGUd-w50vk-g-xUUCMess7hafVGKFMaVGjSgR0o_-H1IV8QzQzYEqZgDXOFuG58ZODKJwclT-4wXHlffvSlnL9sp5400TYsSwTXfLR0wKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=GV5gmtsqjcBJJumkP4R13yggK-7IAKFv9HYzAiIB0EItlqkByFNYPGruzGJvkL2pCsJBi26rRUZo-QxVx5vjd8WisHxiwEf-HDLyHn1hqCKqh2-Yp_efyhWNuW9Mb0W-JlT0GaIgnT6ee3RcQ-9z3Vn4DLQZX3E3wqcypMeecU_-7Q0yJKXHFwUSieuJgKcq55JTTgzKHiSQFPxVa70Et1xkmKVesJAF7TNZe0mX1Q52weIGaY4Ze7_AuKqQPHBTJQjT9FGnqFh7LLF_xh5wPeFHKGL5B7iv4c2t6YKzfKvtFZqM_Jh791CCW4qU2QSwQcEIaEk34ilZCTgRroApMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=GV5gmtsqjcBJJumkP4R13yggK-7IAKFv9HYzAiIB0EItlqkByFNYPGruzGJvkL2pCsJBi26rRUZo-QxVx5vjd8WisHxiwEf-HDLyHn1hqCKqh2-Yp_efyhWNuW9Mb0W-JlT0GaIgnT6ee3RcQ-9z3Vn4DLQZX3E3wqcypMeecU_-7Q0yJKXHFwUSieuJgKcq55JTTgzKHiSQFPxVa70Et1xkmKVesJAF7TNZe0mX1Q52weIGaY4Ze7_AuKqQPHBTJQjT9FGnqFh7LLF_xh5wPeFHKGL5B7iv4c2t6YKzfKvtFZqM_Jh791CCW4qU2QSwQcEIaEk34ilZCTgRroApMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXtjgG7malE0R-qQtFIG57sYQIP8obyfINFjDOwWFQH31y4B4tZ7Ll7A7lXyjMlWXr9yjiJhO8ACGF47ER-E64S9R953jIoKwqmLn_Nif6fSDGaMVWOgrVfhH4zSOVHyf7gG1lCgRrCDHBFrSTqfTq96dSqWgaWYGNQanHV3epS40sfOJulGcByakmQIrutZ8vu3EEW4uA6qZRf_rpi3kiffNptej_Zac0PuBOqtKo-BonF15RyI3LGQJpdm-lgwg2WqFziLLldqVrkiz6G7GIt0q30weVTt5UffNs7Uwkah3k9qdCBlMiGjB5ycKGKDAUVTrURs8zd_hUJMVNCuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cta41Ia6KBKMB08CruqUD3SUgO9bVMHsDpMnUnls2vmSidS4WUiyjYhxXN9XYSKItNZtAvC2bsFZdQ72T09D_IofOBRodHbx1xd-g66Q7s6v9KHSC8fsCYawzR79HItw_ialMAYVgyTLTkE0hDJGj9rTL9hYV-_UgiHPC7b61ZAQz2XTGCywGP7xC9bLqbQJUFtaPKtaskEpvxuNkq0emnLg-M646zgcO88fAEbER-UH2RTtL7sQcJtqzhEUbglT6hvFpV25B8KEntBJtZ5_gTeHjrMKvatEkAJLm7hPtG9EMs_lHwdKqPtz3oTyMM0pnees8Pa_rsuDEvGy5EOabA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlBqCinLqQx2p44lA7-MDW0HUUHemmnpuic9yxTNeBQ8PARJY67ydfdbENZM3ED_xDIpw54ozOlVtA2M6ZutZsju519ruNmwCtGbV73T68Mhm8OTkWnqTN9yDxAmicQDT-QmKkQxPL7ptFpoKIEFt4UlyDY7a2a9E03ED0VYwo1Jk6GFQXPisSHgW0J6unnpFsxe1zurvsXUO5r1joZIiRlpCqfzpBA6l_CGhcaGHu-x6OQNqCtjBY2YAKI2a9F_7WkwGpJ6vRLNmuswpOL1bC6kmgQi5C0WLwl0PR3jigIm2DpFpMZcOl7-N_P7MqpuqMpRgiqaG82MxfqlvmN36A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHAo8we43TYYstSOI-1F7F9_-0-BgFk0QHTs1nezHxjpOf75x_R8ikajsOIm4CJc4DOwGk5AVe0-zlwaXMCUj8nlekxpYTEP9jjQqwOsGIbUNi3TIdQf7hi16He0mMHoinScJauivbAJKi5otUIAuui5DYbAme_aEJ57Kw7o82ndQL_PYRxItQ80cEIQY8UxoBioy4R0PkbiA4aEQiHohVItPdNlvcqTXXweZyMqu92E92QL7B3hHi1hMT9GfYkxFX_I3B3S290wGUu3S1OUOodH1HMUMB8MTamc48Cb_WsjKHsekEGXcbkj032fv0YudzkwFjxp2-GO6RL8s9drNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jO7dHEYuMOIjsywKFO8EK1Tllu7iOf6-1pqBJloN89bdU_TN9kp8JwiGJ3-wMlz8oYhcoX01wDG_9gN2wcaXK0EtbFmgPnvNhHWD7ba5bZTDlB2kteSY0NbwgvOHK__XpIQGWk0I6YWGg-cecyfuxfv69EeH2qn5YDKjM-3RJbbqushxGsKPoibbDOJsT8juPz1ZFnPCsPz-2WZLjjp2tiL8RxUOmd7q_T5aMKPf34VL-YPD3MdGLk6O-gYP7QpD4E2B4cVhrw95AM659h3RwL5tTE7kEeg9rJvdw22ySYe7lM1BTIl60zlHqqtzGEIqR9P4IwZSMDbYho9HOzZFrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1krit2447YlDMpiZ467WkfdOQpl8srQAuxZD8WnPxoHkVvOTVA-W3pKL8OwYeqblKrC5urNEWAmlBin812be-iaQUUJTEDelrfq8XM7N5QATQ3rPR9AiA-4CJgTcVYhGS7seFVGKvdqBoZFH2KGbGUyQUuZTE1zswS2FKTTY5xKxPsu-1loNUsMfMSxWOd72qNKxce-yIftw-ib_qWQGu-QORBTmgxPG-gIjmAIgY5QoIOil5hAEBdXN7DkAGyhr9HcvarbOi8PYO3k6xcUMbpf48SKB4ndxG-sSwNlexS67HdpobjxrY4_I-9oBAbtR5IBJp3TTuohwW4MiAxRjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuc6iE1RD1xgSs2-V54s6PKwk8aM3M6ut8w6J0v31gRcoGB8JBn9Sjr463hwija4BBd0g2rDVnMydXdMqNWirD4T71-RaJYSk87UayzdS1TxyYHn8xg8EVAOOaqqznNL1iw6AKeXYVGbsruP00P3WyQunfXGbMC4Hsx-HdsjKeu3iRHY6kik4G3n1QtQUVSwLA5CGTEzZx4PvMKeapN51ASPqAY4XZBVU_qO6fjDvhUp2UhljkHj9_R1yykmpioO0W8gOhjHj7qdzSWtEy3Omc6mls6CrRZVBjDY1lycVs9L6xeSHNtfs9qOC8Hte6aLXcy3LGS2KHycpXQs9kxgqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp6nd-_npaLsD2kjC0YtyPpTfb_kIQviXbFYvAMpOoiYPYc3rsrmFyiwdJYSQEc4keTXuGIcKstXXoiOB_dCo_ovAtKhg1pgxuHSGv4aYuuanzECB9TQyeQPraxopA3jLftrCy8ShNDfehj0n6Pdw1EF7crjAIndoFr78vjXRPHvVMyMqMWc99g20bxd1HXVr2mvze_gNJ6tXaW3y7ki3XX_0PHWPDwySaSThSlUjhKq6uwQ_7vravDnxBYjDJacoZcE_2FL_9c71xQ8-EZLih9NrzdqsIhY3elggD2v3Yypv6d-pJ-gKOcBKCSYtaY3wyfZss9P2Ofw5-R9nqgmKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeKF9zt9S9zx15y6zg6UZOq8KG5kh3fyHqwHGYTjkI8Y6JTg4oszfLx6-uDeJ5NZbkzMoWuy0_poGnZ6gXYSrr4kzfxog6iNG_mxicHsEOaBgFdFgciT8aCXwxrO4uB_IpHwF7K7BYNwZTed8sVhY3HlE-VuIuh3mHx2qLZSz-g_ujk3vmxo_NOqJRH-m5aggTqi1geOKwqVomAD3sP65E4xQb2e7oY6v3o9kOLS8w7zLhY2urLEEZloZaO8l98AmvpPSmh0Dac7nqirKA7dbNhw7MehGlU1x1IQWh8urSRk35qbD1VH6ucYiWQq6a5VI9fES74iSCQZ8XDRUbmZIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxZPLIXyf9mkLTUYFmwHBiD7wdsndF7fjcqTpd4QehKPyeQG4Ouu6lRXj_Dc1W-6SSDeoAoTnDUf9f90BwT8sxjaDRj_iYZfb-XIds4F65NCfSsPfeBCObKvsOeojah8zpQ-RP0KMxTmQzeDsoskx5BW4yMQEWmEVlL9i2i8HTIcY6QqmYYbfl6yrDaZcJtCInFR-enEyad6nSVqjN6ECa_ZkJIOTA8BL-5Hdt6FB4cVKAKxIGVWjmoWTVdBnPhjMwS0QfdGElyFXSrXBU407KRd_iET1ibU7YF0lqUSumnxLzbOedKj0l2seI-VyIa1XHU0W6FKT3nfI67_Zdgu1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rXVNQLFw4t8kqAF6cN0ZtdnKOKI2oF6NEjdbQZjIbGFk4ZAdk9pFDyUg-6zb47fMh11zAN2vs3ChJJxt4r-cOb6g_5R38zWogbKRcmKEc4C_H2YrEcOrsprnL2VnS-xGMVk31QJ9DMsD5EwY5_WznlFfXXJeu9mEV2WWTSV61yEk9f-IZKW_usZwHi-U9dLB6iyeEZ6mfb1EDMY0nu3PL3FeybmpoEh-XpGPxZr49plW_OZMYpdv_oiY8htkhvBSMycfV6cYhNPMCOiovv28AEV9u-ZbR7wXkhnsU7hOPpC0k7CLDlZ_y9XWkuPlgcyDyk3pbNN-NKazAgOdfA340A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tODUfXEe6K4J1q9wi6GA4U0oC_tyrZ8Q1fN1ujOd02Q2wKOSDEi3GL1W1ySZUmaTvh40Y4yywr2_GtV7jKGVgoSSGpjYqIVv01tOK0bB8CU_VdrN8VWAfeLLdftUB2Bbhp8i0A8d7HI1FF1DpfowfLllBA6hkO6dBehxr8TR7KhWaDz0k6KNYXpKiF7aLnPw6DCq1ZcsMfVeLu9u50pXW5aYkBex7N6N8hd-0AQTcXrKirMH7qMKSzldMoEiNwTpz4l4t2TfzSuoRTb02tuHMTn52f6S3_n8kbuOEAfhGu-F7bQvTgbkmDxMx4UyoUTevey1DRiMsxUUjTbnKil6mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilPXB8fOvqVMgpeSqhsOViq8dKvHCnGp7Ffns2eu_i4Z4CQ_gNXkJjgv6KokQNvmOSnemj2dCYbGjR5C9j9CKAicYs_6YqKCfRJAxTJ0zdTPyo5EBofjPmXVlzvvgYA4hIH4PeWIPXA1arqmrX6uItokFTQZ0H4Bw6PI35Md3o7uAjMhL2-u_mCrH-fbPVHMgQ_HMIZseBDs7rIWuhFCa-A6tLjA_1VxLqKR7eEREYK-R-FmVDPX5IDcEWFzVHABkdBtlsE4-x6SZTKoVImZ1x5Q-qIKFVcZc3FTvFRxNh06nKsWaUBYDcUHpFgE_5Wp8d8sD003j0qHWw1NX721gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piW5mZ1Yzggt9dXd_qCqoTCD6M8YnwP0TjHvPYrqvP4kIjQsaFGBm-KAfAif6zhVClnh6F24eI21vpysU3QDiQaGxbqeQoV0z7vsZgXl10xjhld2MB-Gi96bkrt-9FAgo_rICQuZo3AKsfj2S8JGRnYHOXU1oJvZP1IElWOCnW7Paqg_9AjMHMcElOVGU_td3BMFiWfH6AZ3b7E5WIKvun6Oqkl_QKxQpeDkDVdFr2MvgyU2-X3RR-NcP_jykZ1ARZyPX_zZHQx5SkSWfIOwCkqL1hOsgY8AEI8PtiDdA2UMMFDBrhBsM2kS8PybZCBNeie2fd3v6WwvUzrdfsxzRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOzmO6oEPiDwnlIWK6ax7VBKbirnLVplWuZOw5MjRQ7pojxoMfT2UuMSGh_hhqw17mqhPA4U_eBBogeogXVubsJXyxjeOFeTs39Fo4s24oQ4JwweQz0R50UxyC0ioUjjRaHbNlyroJBFiSxDUUwUDtzN7zGvealc7iisuIzZ3e_NelYyhzBmSm9mKvGVRkNre60OVXPCvTewe6I_MVa0ETh6qbZA_wXmcEK1RRFc_ak5aU5IAZlRZlsV17IcFJp2_vHEInqjgcQhVMQKxS6jwPvCWcxCS8qYmDXgClxzyo7E3fc3R0I20kiRDAhojBNvEPffZiXMTjdn10XjxQJg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beqAijhVg4RaGGnTkiIi1Hb4iwwuxWrWOBgUdFZxBw1iDut9CwBMXjacXx3tUqkI7dcHYe6t_5XWl10Vcg8wY4Lb3Pgo81ul4AaHdZD2fKMIE1JyG8P8_zNjyP7mwqYy9eoYkYlI4I4O7v68ve0MTYOCXXh2SeBMBjib7poxRnNXjmwUldmRp023UdUNjkGrma108v9NOalNZ7wqlvsEcIxHCtNEgYn-ng9110R1Hv_a0baDFIRumRktK7vvKxQ4tsX97QdEQFgsDmdFk4Vyml9bnoFU8u1S3r30knv4dRgRmoi37zIkOWXNB45m2Jr9UogiDCc4NOZlW06wFGQgJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC9UeyyTSwas3OPwn88jioD8kHaPsEVY4vx_wo8cNMSxdA3snJ0fZmkyG7hQBIVCPb4xGCIy6IO0khW6NyiO-gWWceq9VP0S4TT_dgm1Nb0gPYKErLIXyqvMZsiexTOpWzWy-M23pYdlQY1zpISlqzkFURrrj81QXHGTWl8tgVfGgCuUICueyTeDEkk1WBnJFkR1au5UO-uNLBOUfRWXApW_144uzNeKKLaFpLU5CcNCfJut_5C9gRgk-KIQ7SklP1wphE63j4PlGsu8J9ZTHpSXbSPMJV6NNcTwV9jZ76Dwtl7NJ3DpHHcksc05ZGzqRzS7oTlvCqSsrfNDelUjVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrxoPbSPAEduiUDa9I4gDkA6a4ff_ElQpquvuiacvSLqqiZTQZT8nEgtgBHDUUSorVhMdoX31Gia3bka9UN_k56NdFyMhP6fVLWf7GZDsAgwatKFh5ma_qyCDl9JjaE3Iu2hDeawxBOjy3j0ze0hohuxqiEAnWfRB4nYnACgtpvOVcP1WpYdkfTCEYPlGwUp0R-JoHxVoNF9NwGNiKAd-pNM0fynd75MuMnY47Flr2GdQ9EZUz_LmiQ2zdHn_OCIt_31DI03BPJRMY-HcJlE88ThCNNjGpbXvqDUA2kJLqcaqve69zWeylhRBEnt1Ugu8eVLonj238fS4kNjorcx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb-tPGcURoSAsOCMehTRVX3DJ5ru4zRc75ShbkPKBZ6j9f8dg2YEplwrCfMej7J3zCGRKJxXWXy17OHoJ-RqBfFz2tOIbw4brGRmvuemfVDC1dkT-1K2kcYlbZyj1QnFOJOjvTGYJ2KOxMSLNvBy-JMm-y8a2MQyjb79IMKa1VXPqXhaY5lANXvthY4tiF9OGkI3bEBOqJ9x4XU8iH_BcOleNZZInnMAhPc8oJmnHbsXgfFM48kM6kGwIWZNnf8XxjI5fvfShbRnTfYwAUWY-AfabHovhNMcmSmCpQeEAkWN86EREbDihcU20cj2nMaMQGSstT7BTIzADAp5uigg-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZpMpxOauus6zT4VNmTX22iS4rwATCrpfO1z-IyAvxU5-TLaj5uITz-WWZc4LPMcvZQLrA9j0b5HTs3gnIX8W3XT2q71-bEs_yTZaanUTK3KX7nvBSiCSOwsOYS9BJnrfU6FrycySSpSUKe9AOGk8236a3pEJat2N2Zxc3XmliNcavloVT1-AG_oSt5JLqbpmKDpr-wmPWquib2x8mtAjyBQnBUrlgBVYvoV7rAsT77j-9-rjnODaHEpEYp9h98UJrLb0ewBlH9E4YqdldnIzDXeGMpoBW_04yWpHt_RTGyFx0BzzHWKZUDvNsH7hD4kZYHj08SookHjSqEdxmFt5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK4BputqT-t3A70jDHHgYltIogsHBW_2v_H-TUVGLh1T07F9bugAm8C-BzSONddXT4ElsE0YiDOP79qQSdJCYE8ZaOmL5KXHyu8WI3BKE6vidCU_ulFbIJWDPXWREpKoBeh6jw7DonjNjLpA894yaQFjLV2QYPdd6hKqFXVFNH7iwlJXnDzU0fKOANusDn2VrlucyleeUBvVGiLBw7Z5lVIv4jC7zGtpe1sitNktOgacwewO3EQutlUdc7Ko-KvXvcWGVc7cLAUpWn5Sq1d1OMEsm83yFVFB6XEs0RjuKuM9eObigx_jIzP6cSApD-eKLePDPd1kGfJ7cCtB0Sfn9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY0qW4JQXMVWXO8XjTlhrDcuWwWvJKsvcUnl20YeubN-OM4tzXrIELYWN65hW_hR6fnYAM0E-1aRKGtM9kc__aU9dO1bp9LHIJUxPwDpQ3M48gaSxe6PhJtSncEMwac_gViCdN1Umm_6iOXtPHOrd9w1ztXLG7NacvZ9_7hO56BPAlzyQZe-LY4fVEmJCMpZnBXNjBUU0sdZ88BQy27aYNS_yMSAQ_TQ8KP7AAsW2go0EiI4yF9QnWdjVxGRYHmsJpJuXVp16IYA68GaZ0nEfi4MjAry0IkMDZ2N26POZW7tph7OhKTOJ6JZvi9OPTy9lT-ZHpbFqPFluijckKZXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq23B6gVa6vuv9WlJsKC_Z6ODna-VfLrNMm7fWn0cdBFwm2BXBrwYFBHbsBjDbWp5SfYGDCwmnSnzax3V7HbahW9LtNUjg5m4lWZ4pN97yYXq-0DSqMYfbAjMGijtWcvnufnMJEqoReLR2I7V-MRvupEctMVSFKwDXXlrbnmSwY0BwVC0PiUrSUYEcssCQn-MNQF_Md4VUspLKml17jlk3y7LuJ5LS4bTMB4byAHksJ2ZIZXLv9cuQ9XfVsH91JtAiMti2wP5an-S6IQMmJHfSdkjKAO4NpXEZSRrjwn78jPAV5OaJrQ-QkhFOe7dFIqzlGZSxa5EtVX_KA7SVREgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiEvytGpAyOP3DG44apGmKU4EN48nP-4XSBWg7qKufMA7ZNzonGhVDksPx3_ErYfCzAmS24ZvsCo-OtQtkF3XZ3ZeuN4xdvbsm09naJiSLSx6i5Jp2o7VcKgigQpvpQhd65n2GNTpsTJiU6yVKID1nqc8LDLkIrJgWSzL0ZU758qNXIOWqtbtFrX5knbfn4Xlzk_A9R_ahq1ZvhJ2n9_SPfcyCdjeqXG165ln1EZ642TLycL3mvmkZyzWXchwbbCHMfqCLrO6FxPUFnRSNR4yU2mq6Vps08Ol4Gksyb3IEXd7GVDqx5myD1Iw1XRouyTo64Cly2d0rl5JKx9BDD4ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWgjquZKc1hSgSv5FNMGFsISmAfvPwu3ZZpvos-THyQ-CWGcl27oP-hRVLIZCOmC0P_QgjZ5fRijfUoFSxVQveaDf8klMw7TNKw57_2VTJudqo039rZP24CgHyEThQ9qGmlvwBko4PmC6ri-dkmeidyIUpQDzrTq4exa280DdspgaPWvDy2U4J87Wr-2jQBD8EaQVIxuFratgMr4pSOGKBNxm-3ItiUaEJ5OXH5JByt5OYQlNQJBU38QcFRdn627lpvOTjt7CfAaLIvQRNQtt1ug_vIW662dLOs_dZ_GH80r8cHd_Pc-9QuV2dPT5gZP6K3R7YQM1AfXXruAAWMN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKX1dvuzJRqJNML2JBwCCNQSfjo2p59qpDctcyAs52oXPT_EzEKoHWN5-LaVlTXvE-seh0K02aCugyjW5O3hYmB8HBlvMPb3jPAbbdxWEv5fVwkapRlKeKTqxse19LWdiFvrnvpr0jIbd6XFZ69URGuh9eEj_UuKRIQEmhbHns1x6qNxWe8qAWlyQhj1oZ7tM0wTTHEX_uSpjtviQukcwt7pnWUuTxbue8uiErZDMWWSfYmbSAHmKQUSK9TAFi_24g3eahtCssHEey5PkpbkKu-kkTALoLJP7mnKgjnpNK1SI4i8pnbkMXqAiikUvCfhPHYTnlFVV1zpcdi85Kuf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vKf3fT9YWdmV7Hhi2dIcsc54XN9BIRnsACW7T2V6nvIyxAvlg5VPUmol0UOUrgK-bQFBBjA5T3AKnR2HMmE9AHyhj29Alt6GptRwabbctuayFFXKgttjlulu5tWkLbB5z3fsEbcDMyowU_wKm6DL8iVm3Z3uoRSkfxwBLsTz1GK_g4exOA2kstfDrwQLrfKBimJ9ev1hyJgpyXsywkBYqa_UgOeJ4ceGXlH2yNOEytsi3CSiwj7w-hhQxSfYE0GGRPfbuOMOC9QVwRo2DhPB4NJFxVPg-yweCOPzQWoUnV2qq6lshNIUBETWCpQusw1LCQApsRpSDVSr4DsfEhXJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeaY9hdChFiz67cOaCx3NRCzloYWxARtX5zJ7o7rgqIZhWwF_kZpS4Jw2PJst2YMdlODTydj4bdwQhnW4htUdyFkcLVwci0DJ2_A_Y111L-K5Zd5gMT4Ik8fUNQTilAZnSfnaj8UDGRaMy54CCKqeLQX2SaclaRvahMd3CJKrNM1dbLLEbpl1HYLRJOXQR3YA6EXrR6TioSs-HNgdpRKtfoweouENlH0-p3VzFgaoRIwqX94zC_M4nkgrJdcCxNa_7pAshLmg0PePr0-gZg2gZOkN7N1jkz4g5oaje-brAkCvJBlqKHQYS7x5LbDkF-zXwqkww7hYiglLccWwegjeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-5d14nUanMm7lhR_EWsf-W1lzQs6CLb9v7hrFnwTzjLLpxqMEMDewtoyCd9ZGw0ZA3zwW55OgvaAwU5-VCey24D3rUAzSQhymNliUhUE2xjxmwYwVe4wllVvmUnDKTNoAp_FjJkS0wdCZkwn0VS0Da9kB_zYN7ThH9OCLQObKH4-8KD_wKjYeSfGT5rr78b4by9Jrqx2_UUWdSVTO2T_mlyQEiy6jqmaFs1ao3s6RZRX660nqbvR0T02qbAQAuzBqF4FBmxztmUYilqMbXwJYdYFrm7SYCgvmYceHB4oJd5h2LKgheRpC8SHabDvgL9oV8c1VKwbfqYhY2MrlpZBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcKiBk_lIfC-dNSUl7idaz_UuODPElD6cNp3p4UHMQt6DJ-gIIYlW4TZHPejwReilfOm4_Pziq8IHo0hLcOzgEGGX2AwYZ_eee_CrQKtGtEuvz-eM6MU6m2fMXq1mNLrfZjlsomkKclWPEEXaRpmnId5hYO8QbNVDxyO1CItUqoGLdfWa-FzeKMXnfoq2MUa8WQjVOlI7AEOkNGtxes83_OSahKDA9_PkdHpP0uQUu_ScNUx_lDRqBlIJWhV2Sr4GPxJpgBrszTjmyPlPZem06iMxNs3V6ozI8-kOh4N6SwHB_psExfI5Bbs7nxz_zVfnpi55skgc34QXDwGCMg0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uA6UZ4uB4HqpBx_P2nFkgt2USeIcQM9W5GTVYl50YrExdYkAoF_ug34l4jeRBecF3rICTn5bbkhLgWw0_fMjIwpFZ0V_X9YtjpemFIIwi5w7SfY3tPaWEe7S9VfmjsNZtBTCKxBspC-Rdydzm7aAN7USVrFWVkPRGBN2JCQWudXcsiW13xCYkI6ejDVGwLzprDcwSzC33CiC4x86RgO-38-IVxJUvaaF6MC0YvLexEyW_a5j-WahLs0yGroWL8NfILJQziax1jVgjeuLtTJvpBpscK42cmz3aZ-XR_ZsOGSdTzKC3odEtvSoAbriA7mPGU_DbA7rEcxlhyL13ApqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJvTuGJytuRd5eAUJCIk8NQLmEJOQmKsGkcWKBn6SzhnpTdbQj5zgf0zuTymKlXcvHR26dWZRX736BWzQDqShsTOmsW2x1yZ_81iXMCa6NNEYK912GneD0iy0LdZVHr9Cn01vRk3dfVjR4w5O_cPl4OvDwaLDX6k1CfAfYYJmPIvm1l1lQg-PJJWdDldrMVYiwEPe0KMBYGCAK9IM5LsDfppTsMADNfF-pmA9FxFhavegInlesVsBAXEJrhHF-AiEdJ0iZnq6REtgaWjhJPGur9afjcMzIeazOJQkVwkY_Ln6mTaPTXRHjg1S_rGnPLQTQmIlJInIMKMAPZ00cfsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOIlCk6oPqhHN-JG8hCgLYVA5lpEFqcMSYCKAF-d3rj5tvbyWv-9dfMY86xpRgU0lWJntj7DPsip48eDzG1wXpRmRpoIq9cB_j68hhZivdN0Wcn-x4LulpPhI3t4iDp_ZtOty61vx4-maKUlUZiwPaI_gj5W9YkToIENbeHR0wwDdL9bci7QAkTPeghyMPbQt4zajw20Z7RQVr1ULTZ_JV-k_WtwCzF3XIiS9yamQsn2O_Yy5aku3Pd8iGPpDtEVH9LFZuMBIY_El8ELquKlvDsHhxzhZZgZHBq8PV8GDURsXGDIXfcht0aQPMjRRXEypswsbtbSCKQgPuF9U-DqAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdZDQDExK0EogDS5fLNpX80ZIU1C5ZhmmVJCFr5cx08RG21JPc17MRNLxZAFBuG9TEt4l5JimLBXQC07S54DeIoag97Rl-x_kbManVUSP0ATqlU3BLkLCeJiGgioMsc8t3wDlfXYMzzDVtg6l1OgJNjWPHGNp-0tHGZ9dFdLwkLBw2qblYsKTkIBJERhNWlXIC6SV_OTyFigjc8H7Lhazjbj6OpwKxjeshV3GkI_8thZE5-N7No1z5XtcX9mPpxIe4mI8xZQYeUhoVyNjXp332S88pQd2H4e_MN8G9Iop93UOsU2xGn4K1J3aP7f3DTZ_GMfEutpmG4TOBt_Oz6jng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8kfGHfYYi6oq5DHpoBj2waNe-BzMKyqbMXjcx99N2bB7YjphIIyMYTuooTNyiIbm7HH0GVSRpVQt8Fyjb9qI20UZ5l5ee-XD9zGD3lweoZvXereQRSF3XpmMmODhbhRXBA2WbvEZICoIjJOSmmccaKLesVYCh9tRO-GAUkAZkYpoEQtCWi3xa4rQG59cM-HpXtRxN2LpcJpbKO_r0reUadylaks9F5Wnpuj9Cy99Eqe9QntimjJ2_UJ_yNkK83wE9s6klaxLL18CeHEpVz9eTD5gQyFMxtnluvXCv7GfjNCBuEYY8nIyjUaDQoclD4FSYakkyR6qWudJGjNxPbnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlFmT9y7iWmKw12jnnCNYtonuephIOA1YJVpF0JtUsoHfjS0YH_s04T2pBZgGbijUkCDb2PIxXIlHSnRvxIIsEqb9aEkhZGCNycDCziHPwYEOSzGTH6wFwTBSYEyEvdI2fOQetsqqNclWptptHUgkjLTc61CEPukvmzepGQdve5AfPYYZ_L8L-YRLtUrnhK97EcUWWFA3-OYT7UNSzitoXxVwEUq-AJ4BxX8FVVy034dGFYmYmQGe7_HIg8uLKJDDmgKrsNd70MSHyEUohVwbOtrsGE3H8bwuOvRLHj0YBGpnnpl9dQapazR0MMii104bvq78aYgBv-XZpyBYXHa3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrxfuDoijZMh-sCUCcL9PLdQ6YBXPn-cUCBn3oSD5jXuJpA98b4EXigBKshhGcHSDJmlklLvJWP7knZX_KFCXmdOakF3gjdh3fDDkoSgcZqdo2w0oeG6oxVKIHYXVP6jlG7zvN_akugALACXwg1s7FSbICJi4Q0NyeNoNrNU_hIxYgLqksmNgYq5cZhf4NbHLhbnj8HtvET0aKD0Pn77AhPDfhtIFPh4rcxmNDGod4LGB1vT_42Hc0jRd6d-vzpMute9Qfa_178QX9_1PU4qIK_6VXZ8BRKB1UiXZHkJKo3FZu9fD-QAQfIBu7EBvR8cdjC5ZqDQ9GFhXwa0fKwXpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUzqhTbPahZVE1-AcnBGYYLCgsQ61P2bwJ15Lzc5IecGLPfyvYJETKgKunF2GPNu6bEgEbNrjUoNeG7yLgPQIdi_m3YFy9ejlgsZqie8KuUlemdh2hzNuKeoClfPzqrCJTFS8vyeavEt_D4lzlay7qjQeibi1YRDxZT37O97SJBYyM_kf-810VWaYNbJ_6IpHBjHEqv3TNf5wLyqDziVdfcikpzGdX1Dg7qiOXK8CqrDCKzncspXfPlCoMvXfFcXc1jWobijInQXMlZrVKSdRo0grLqisxLSONlx1QVHGxEib-K2y26Vb-G3ed3k05It3g6j6fyFhZBHo-zlcSeORw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6aDEShiFPFZmq6lwguQ5b8U7hJBW9MaflUBd8iOuFwIR3cXpt-eUQ49gbJ3Vf84HIiYAg-5aBvVm2a0gPdjvVsx7xQ5hymECVH37b1PwqbaTuBsnUvC-SZUIGPnBFpBW3YBl2S0ZaNrIIDQxfkFt4k5JBvAC5Ui93v3AO3zYOvQ6RVRHsr88T2lQEiU85rwdMNWHGBgCWa5qzYyMa3cFUd4kT56x-KGa7B_hhulNpinh_AtIeE8zck4PL5_tzyH4JnCysjOl7Rxz32Vdr3DzQIDBlPlLK9DF_eN8WtVtZ9cMkI0HaBoNH7sJqq0eM1OWpAjYaKS7zJfaqQ1K3BAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7W30hkDVsTgGHkOlBgKxuJ79SJ3Hu2d-rW5pAaTtRr_3W08c2FfVUKLCjnnashDPkPhwRp8hoGu_yl3Hw9gKnKo-lF0FR76aqUKfCAZ2bgX3N4ShKBJIsn9r4RUupghZkQ9JvLqhXO3etQI71YfArdQ0VYelLMXeamir9HQlLHWVtFu6I0qwxRw8jpEwskHdP-5BlPRgPknznzsbDBevlB3bY7qylIFW0x6wQSKdAZ0IVr23fcrhnSgTdzCpHw_aOCVR0bKPZlQ1yaAqnLuCvqK8S1KNA68bi5nwtTETsaRP-vaiBohHrdIwCcLZiOtM6mFckRPqC7NYVPDQcKb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfRJ5BN21KyTfYj6RFhunbGjNqFzTQUi6t-jL_fZtC36E_gi1fQGm41xChvYw7BTwkEFeDxMjyBmeeNfNHrnk2R_pfAjRArsoEpjJjIUD1BfOdS9hK-XQsVkk2R-VG9FIf1d0O3GdPvovuNo5vqhkpEDhOK3M7d7S3zhXtXdh9d17obivOB-wajqflPH5gEISO-KLcq4N09jckfRREJbZi6D-yCDdb5NCFDI1jpCfGrqtfEgqI3B6XXvwglsXMzkXHwUDupdVHrTtyfoK6BcUxvpOxtaS2SY_yaOQxTTBT4_JmogbpkKSgg4-Qx3Tq76CIGCFkfHamGpulbgoeKSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXbPXB6rb64EM-NxTOC1kYEbWBRcORmI94cOzrdQAbz78_e1ckjnOp6mcJ3tfpSbb-kCYEHn_ao5hGjCfKd8vAoMU5WCHO-KM0cCzYm7W3-7AyIgT1076a48OTqRxeXwKeGHVC6lv769PrN2i3JBuxKbn8VIDbQON3bVCNRyC3SatCzUIiVI24qn_piW-9ZWCtvAiS-IQdvnelhooWqGbisL1rI4TQ7ZB9Zkxr6NyOQ3NK_Hp3pA11YfcVaYtHA2ixTyvkWFTElN9sLSc5RN9N6VKsTVWAfBZd_SWFNEh42FdbmsE029Zhvy7TLDaq-bTZ2H_pZjenk7gZiViZWxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bN6rv_59_oFRH0FfavqUXla2s3mRYO9nXe1vPqcjmMgqKKAVB6F9fqs84xkJCod7i6vqvialprYmB8IGLZmNuD_b61FCX9q9LbeeM2PcEfK0VxoQ2GwPzKo_hOBQGHC-eMAb2yAYOG1jWZ9JB4A_pP1GgsIZuupsOhjBjPvR-OU5UITVTf_6xalzXEp3TzkF6_RB9JnZZJEIkDhY6bQ3rwIj5Gu3fHoHBV4kFbUTSepDgtJtemkVAY8CGJAQKJJYsmZy4Rnpk9yL5uzbmYPCRLikkSdByTOvvdoPRVOxSuse2UQnzTFK3t-KuI3FF_sxZwZhriCbGkkpSV0OaSwpAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE672uE_vyRLekS7LotlKCxWZaMFms3H7epjBj-aLG-nlQqVurvpj2ncCkFppkCM0woWFxANKijHEsTKAULrELoxf8YgMaLBDWH-bI3ow9rThu6TlQBA2K_kDlCRaHrnnOoyTm4JsALwfx0Imjkkzq1yEyJ_X06x5owLCEj_JZAg19CfhxfnlEwqbNTBtNE2am2GiZ_7UdQ9vKTw_4obHx5ui8dUipkj3eAPnLxIlTLFT-vNzEpygenx_iBdCEHxJtyOcF73UVb-HYz_S-zKuvL5jYr47c39IhgE1cTFbQJ-tEWDaaZetal599S6MmZ7FS_1672yLayzterBTRsL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9xX5InZIKbWOgRnUPcuLC-eCEH871OZ0_kiMvqUGu2-rrDv-h7KbbKA0yWpHSCMEk6Fl6HqdxkkrnpB4EgozwOtJ8enQRZJB_vKE7pbBdYqGXa-WrPENopg0nAwSHgjju5gXN2tZpYBv06w6qQfmYgMwvzRAEMmbtOUwkxDgofavqUYb7WblRaxgVqG1ZdiiSp0TWsx2lZSrjwIgJAdrqx6qd66iOkh38J74cMVlj1GxnFlt4zygU8Lw4M7OFDF7zuRBXpUTbaVLTavc1If7F-lTfZQc51Ipa3mTl849-ShhtXcfttK4K0kYUFAn2yPGQTMiKUvsXq0YTY6KZvs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyMyt3X9l15ijenUsEgW9CLx4o58aoQJroF0I9yW7XTKvnT3-kdjdw0vyy2r59PpyQMQeMOvsLYOeXUx-t-Jp-Bk3bPCShvJPtpGH-1Cwoj61_zbsolUVhChi9DdrhsofWP30-v51EHV2oxmMfePF-tKMTmhIcVZW8BnwEAlbWUMEg7J2cwtd78GC188ZvfKbFiuW02Gb6sSkXVAuPY0Vs3bEDa8WdnJCCb4m__hc3PHeFn22EbktWzW4CFAJcPmXybXvR37K8AKR194KfrX8SMgRn4HNbeRpdtwuoFcUEgksjCMmgHaNwIraX1SzEXLGU9yU4fqgQeHLlGV0XjrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWqAs5X6EP4YbYEKgAgNjSToRMV3FVtgu1sK-dwlAyB3wVB06nCYRnpgq5A8VjfP8mft8GDL_2tFsnhj3Qy9han0Io5F4Zl2c8J3_uDxFCrXeOG8NHsUQNOf5bHy9OgcT71pJnOXfmu3bQX-U9r4Dy2NJa4aRztncfhnRhpPl8yO2ccov-msp7XsRRE8efkIuC4351uLdx947YeDrLPwwZrTXwyj36iTuIUKMR2x97swJes4Bz9J4jiwHIZCXCBtabFErmoS7mumiqBDHyza0IpLBatd-4VYG3UqCmWZ-ylX7psERWQ7W7U3n7VRGKtLR_H4MY8Gm5Uu8jYj8jfXjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-gG5DaFUmI3DYZ8JfO1UC-acv-2G55WVQqQcorqvwe210IgPSSZTMUpAUsZqvQ0RuUlsaD8nCvQGB2fILCsWWdpiGZk1riLoS_cpmoFVSEGWQCymjHhfDM-u21_9_AHEimISzVsGK_FwmJRr1y6PmSKAhy84dh_yzo_AocQvHmXAtHA1Ka6oKNrSFiYobOJKX1Cx2Pd4Ndn40u0p7gmzHtRvFknWgwp7koE8KwTDPcg7R2c1_BN7xQ4SCuA_EnuZSfeGaguViIDL9mYULWlwUWMQGZhm_X2HjfbF7u5c4PIvVXb73-XFCs5JZI9yuKhfD70hmK6yNELZ3QnorTSeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeeBFr93HtSvQknvejsqFW6MSH8yqRXUFZg1vWTqyW1ojy-9Hf1YExuB1oMcLh0CxloAFzQPChJB8ZzkS9pKhjOW9ofZCimOiJ3bb1tYwG5u_psrMJ4krZNqN_sS08Q1wJdF4qEconFO8fI1nL4jgvnuD3ZnzxZjNg36muVhR97u9bCNxs_oiX6_7_MmWTiIHEFiwrSmdT3dQEhYahEAz6FMDscuZ9zTXfLKjrMdyGjG_iwGp1KYaXdl1Wr6Z_ZT4eEL3JZf_iP0w59Q8zbYNC6Hmzrzn41uKpDQXRl9g3_nsVQzKdZbGVdzUEWarXfeSB0UHYRnxw5AJIvOiztdlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=W_1PiSqwPGgNBmlk2hEb3qyOWmjFsG3-6IXV_-Q7MIIlWQeJiDnzHTOT0SO_hwBB6clpaUp0ON-2So0kCpm6Lns3Z34c4Vsx4ShwP-2ZFKOACqp1U5s5FJ3577Sc-hHdN3WlBq9YyogCul8rbu7FtupQ37yFsVVTcVb7NYXGLoyOI_oqHOn0OmG2A7LJCEBhWfqyVkzefe5yx6lgeWSuntf_jTXVay8nYBc-iKcvtSzIG5SjuGa0ngNtvPpZP84ulSkbf-MZXoDcMIV8qzX8x3YM1fIc6i5uPy1LZUxqbk2q5knPiGhCryqrCyTAHxMUQzwfI9i8TbAsASWnxR_mRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=W_1PiSqwPGgNBmlk2hEb3qyOWmjFsG3-6IXV_-Q7MIIlWQeJiDnzHTOT0SO_hwBB6clpaUp0ON-2So0kCpm6Lns3Z34c4Vsx4ShwP-2ZFKOACqp1U5s5FJ3577Sc-hHdN3WlBq9YyogCul8rbu7FtupQ37yFsVVTcVb7NYXGLoyOI_oqHOn0OmG2A7LJCEBhWfqyVkzefe5yx6lgeWSuntf_jTXVay8nYBc-iKcvtSzIG5SjuGa0ngNtvPpZP84ulSkbf-MZXoDcMIV8qzX8x3YM1fIc6i5uPy1LZUxqbk2q5knPiGhCryqrCyTAHxMUQzwfI9i8TbAsASWnxR_mRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNroKNM-xRgIwRC5PRp81idfdqT-Vz2KAuRWalaEvnJRHuuGhaAV0FOymr3Aq0gnJjP5_xdjMAKzrB68HhStvrcZQZ79sVxUsvbteF_mH9mr3-dKog8xvO3NRTidMd9nzzvN-p8rxoxjtgL02N7D8-8qa91Sc1VQ5ASlrh5zftUDU9Tv5HRO6LT5BMdPufQfOF0vpDF9-mv-lTI9BS9gE6rJEoL8EFiWdjdF48AGp2C6NWO1JZ3Vk0x7qPxUot406QK3FHtSvYtcV5iQAf3tNTLuIg20ZwHTth8aa_073AyXFzW5CtxcPo1z1ZvkCedteC9Rkh_ktYGmg4MLeu_NkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mymDhcGb0CAgV5eKv9B03DXI9ShfazZCq7f7vFo15JkxL76N4B22vPchKr_QIjIyz17WGnU9-RBWOnbpaqCo045J7ZxV2tCrjQGxPOQl-wAt8DOoldcD4zRrcHgwFUZRPSFkhWlckSMDsNMSPexEGW2gMYVbFa4H9FWpeKnT_m4jYq1MRXSRFeYg4I6iC9Y2C_78WyS1cIBgayMK1rEp1dIATAKnDHP2ZcAzb_a48III6nJ9ImkfNvU7hojY6O9OaPyAlmpo9uV8G2HfYVYy0rJC5iB2ST-H2yXazGS0XuFax0BuKpomP8iPm8qox7rqzNrjOszJEsfJbEY6C_eUQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSELdcQU8KBpQTJQNmtzzDEu3_ApT2duEYY57VRHtQuAfWEAWfPhUOtRE78N04rZunIVdJ4WDc2wqCpC2iyR5LP5gJXsr9GnRwZBfZABBd6cvuwgAmWESZoefiG7EFqZAqVxQQuHeBZG5lKMjZrBWHcR8kvbG88oSECGSmIyaGwX6pu9BSx7w7NK4x7pKg604tYvGNPEnCUWKxbpsvJfOaZK9NiOQkpej5DFZjus4rAvPWe3P4xbC8-wEY81X-xNMFlQOa0KQIuFSo-rEGwZZHYtRSMhfdjjBr7k80KKbApXHRx71N9nyDIUj2q4p-jCO9iSxwGIHstRPSIuh8fmnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GExJN_3AtwhiVeyZQmhGZ24rWgsR-exJGi4ov8zHZW-VBOu8S0M8mYTZ1E1Fo-4OZ8vRIPlFHSBeJb4vXVQ4vnUgtx-mwRpeLTNGKND_mzS15s-u8Tayf7_fL83kbBPzZiylUqmvG53X2DepEnE3gIUKBq9h_qIWuEIFbiJgwukJdd47f8WBW1gwkJVYhpCSVQbdq7L_e1oTmplomiy5dH-wpBhtjIej7sxKfCnaX4f3zSZkVXBW4QNr-HTj5-0bE3SE1oxpxOtuRHgEzzrpRcUYhO10xU-p8flH4r7v4FxwMEJ9LFHMFzfzuGAf4YvBBssZzjaoNBB0yhITvaq5bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACTaMJyO1xQUoZK7fH7_Xhfkfro2QRIkPAq2BMl2scryvef1o-Xmymg9A6tMIef7spSAqwLu_NsdwO-7HQJf6InpGNQTGqQZqQ6SPeainh7jBLKRw1FVE2ABONmMjuiruJ9TUPxmU43LQQEXIy11DzXcx-gVXJ9yYEDrz07KmUh_psRfH0S3nBX08eptIhgtn4MlomrP0WfVTb0DiO-SoSizpcgR4dTxFGn2XG5rRfEY_TyhE1OzIynD2XCD9X4KjGcrpJ_55qezn086cn1RbHw4DrOyr7MGHSB4_W0cYCudrzn7H6gGpcAdRaFmd_vqPiCb3XlOHlVINn5R8iErOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXnu5HeKBlq4-wNbsApri3_OKHrjIWQl3550z3SHB96GWNv-Vsog-Czp_77S3Akq5TT6OTqjoB-Bj0Dot3ZDJD7bBgGTomq9U5tSfFFzZg4tFNJCb7tdOHUyC2YaqkpPfsJMH_C2mK2Werg5_dWcr1C8rncHa6c2WltEwStF2iGxeTAnow5XWzBTDlKz2G3tQq0CHOofLT0f9x7Ce7VGgubpupKAzMgw4HTv22vCoz8nsBJQppPbRFy-tqxvdep7tjODvDFjV8oeXcWTD1qSueEPhNuuRmLMz2wQP1_7aQmqZ2MeEKvXnupfik_fpQha_yLsNYLXuoYFu1s4FI20fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEGztTyZDriSHw-jCgsP-mMye3ZQoqGjs6ESuP6sCguDaBR4x84XqvpRWkox7DsSjT5MroivIUH61OIgQmsT9FGHj8jAIElAN20Uvnf1GaVGEapTw27tLesmL396vty-y7xJFHKhmI4ZAR94NTP_oqNPvBCtPbQlXLEFCdFbkBgx1xasMoDrEsIXipOOwWCsVjmmR0brFuidvhVTDEsT4OEK3riFyPy1P-t2qG_SWNQ-bgBv00M3xwsux_AOXSJe659z4zhPQS6oTa4xD0DpUloueWvAg5useH8fqK1_ROQjCThHBKBXFU9q-PdBPIimO52j2vIkOw1lCnNjwsPsYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMmPTWoACAZ7T5OTqtesXHUWAcqpWLlp5JM0YKbsJWJ3L1t-cZHw_vTTeoc2hreU6DpmsVmRu82c73PgRYPBKrYYH7AYa1c2no6EW2qumvJs94ohsYr_pXEKNYN_uI_izijmSysm7rrcFyHVaQUkq6xrMUygK8OC0K-CYcJnfEg3TY7lthdEMBpq7JAkZxVcbaKg_pJujT38jXSpRg5xO2NXSCPnO2P47GwqtDJZbrqNpC_06RSmvcoyNN-nf3DOH_lY5JG3YJtDrRRvvgJckZEYUz1PQkgU599fsogv9R2VNSyre6EtcwM1AMQo01Hu9J8w-iWTfQcyACnlTjwwTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au8h7OrjB8iWUyRnysRW9llVNzUZ-G8YvZB--scZ7rOqT5lgWsI7Lvum757DxWg3xIWjtV7w_iep7HkqlzHZZLrNXQ_GmBsF2KEceVOjQy8VGgCjBI_O5fYPtxAvONnj_Aw0bmAzj_bwzBrFgZ0ps2U90Ai-uvdSts9_y0D3KmWnBV-3eUzG_npz7JvwbJhzfplPEl4pdvFjob-b_HXm5cbBqL4kQ2nNOo3uGKCIqwLv66CaHbE3n9b9oVbu_Rv3xFMiD4CR4H1vuNYyUY74w8P6AExy4sbNqteL9h3Or9aEtq98ErnkFpQmhlZISFYZPgOFIjCU8ttoeTwNk2wRww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APYNOKEpNJ2BHdAtee3vgwfBrf73NjZJiC2s0ujYdjUayWd7BjU7OdDpGz6qoUl1HRyKglwquHCw85SQl0L4MSCz0s8GMfUsjWnwNq08RatoSKG4voGkVfE9FN3riKQxe-WO71YajjX-PqKATCWFp5Wm-f469OTXp91o49ucacIq-UIX0hMtf6_76i2c88UKvWh4vyFDqwYQbptkloIpOkoGiRpAnXZS51njAmvMx5Niebu7yFCXYvWwGQFUTsFtTfg8grN51-E4EErVJgVNY_ZuGuu3z3RZVi6s5a6plMnRbwQJnFYn32orxdIs-dsuq-7_XSz4TEiCtaDqy41ebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqiUJBh81t8wMKphq0Co89IP0wmKtJc1slsCrwwGm_7bTtnUeKrunn2wJ_LqK3AHKekJ6ch9aJcDkbXu6tP-aaobMMtNxMC6IQrAQQ02micPDmBI-KwisCEFX8dy2ioSF3i7nD3bfP37c8XQ_Gy3XOjyqQFbgJIMmk5iE_W_laBX18u_R0X-0_UVmyITITjR6OjlcRclP_9oZNp0nlE1zMcrg9HtlX_zxpmQ3yGGXPbbzpN6LJ64-DQmyHaiSSGiyVQOrm9XepB8Q0Q689UxjNpO8SpYD3gU6k7pKDl9-kCpQSPz5cVmw-fbLletoHYGCSUhET2dHQQLnJFwM8w9Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9O1MBA2KYTIoDtQXgqr5OFKCQrdcT6bzKo-9uxpXmTh975BaCR7-qgpEk1pn_y1tVfO2IMQtpmPDxFeqQUl-6QKNOJY3BoLPpTfkgrcd0HW1rmARh0dr6OXK5ze7GbZdeaTEZ-XjNWWdWm1fRTAOVoeYgK13GpCEcg2U3NgGWXhQLDseqtXNyP_S4Ck5fFjXRKPS2aXiyHV3AB5l-3I4BaQkj8j3kcFN9ZPTbezzFk3K1XG7BFAkNBTVGHGQvc5mo5qtGaU2Evb4oT8m1RpEznKfLNJdNkvqSP7Z7bdvSWUQGpMaUAbbID2gPz37aTWEzCQy6ABYQgY2vQJ9M7Y6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFLcH1bBy3n-_IO1M4p7ePm9WvMG6UCmFwoODwjrh7-xRENpP4qz7uKD0cR3Al_ZGUmzuxrLANin163CYX8U0VTAWf3ze4rauVgfKpyeC9opPDTlwjkQp98tmqT_DrJcEMiszuZ3minQtq64YyJvNiG7-7_gru-E8QnxSgjIP0KRuFXWUl1D6-OWlKUnNEe90BwRJb2VLpv0N39vFgh5CnHMOIw9IBOQbUpNrN28oERNmxY3YgleelfFeogu72nI6rqG_BPXcbFId3NXTUdX9bMGRQIfhD0KmzURVA2uG9_Hnp9a1cY-M6vUmVYYS2oQoBJFgPEfLKbXGOYNqFNbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWI9tN99Rmkr01PkAXniwH65Nbs5VM8CJB-YCf8ZH89OBdvFWlL9d2jOqD91gYcEv3Ns6aVpG91-pqMd6lTVMynUgDzfGQkLQKShRnAoVFtAFup1K7xh_S0HckLgiUYQLmGr0SnzyG29hrCa-n95X2M1fmmuktg6K-ZMEP5uqjMuLWZXUpSsiRhfrYUt5-mRX1k23NlJ0dazJObLUmGRwo0aMkkSw3CPpZ3RIA_G29PSyEY_qOE0fUOurS71LJJas-w6q5xOIFozpbgb8FeGw0GaVOedKRhkrZufzfuPF98lxYp6OSPxmw9yAS9bmI1z0o5rnbJht2dN40vkdSN50Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTizTrBwNWhs-v4o9zcncEDCxTSFn6OrfizA2kL2MGhePbJrsqzYPzVvq5u6JBj8QRO6c95eGFcJFcepln7ggCNRO5LHU9Uq20Xq13K-0Xg1XfeXPWjl09EpsG7gXCYb35PaY83VzRhP0AeYW_tvY0slx0QT0JV5Rbpl-RYg13Ee7hFG7cJDnpYeQ8BnCXqzEVr4KIuvdYBSnChgZh9oDZsNU96GnCVHn037uEjwP7HwFSujP1_qT-SHWsZN5QjGGlG8GdBxHfc2W3uGlZ5jOMuTXAdO9IXPqSteBzMxD4RlVGwzyoWH5TwWjiVdl7Ks2NPtJyK8K7u7ukWGiwsYwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erJJQZc7T6nkimxvcb9USTjHgoBPEZtx6q9ASJnAiKTeWRzDNGpgG9a9QPZKq78O3MMnodIJwNNkHA7oaqUPv9-lmkJTJWYAnm54oaGC8HceQYn_cBeBPIZ75kwCNUl3maw1FBjz_TmsdWR5tIqkrgLvv1np1XZ3ECgU96oRKfyi2vvHhPDBqFqm0dWY8pE34fiCT0CKTb1_8e2S4oSgeR7a3HVxzFm_wE4c6mBkI5zQrdCZeOmfc-1B6EBr46AiM6yk1EtLf0XYNpcJFl0jAFA3Hst3nI-gvxhThbo6T0Lea5DKIqxjcQPc9FxJX_IQfJeea5vrbosy-N63i-0T8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCCp6n6lcAVY9OkJCJAmurhwfvHQkk9M7uyJU7RmF1qd-bZikeFPXZ0d8cnmbk7hcLSZxMv8ApIBjGXzG4mHv-pdN-OUj0-urDPNegyqQ4fRN8D6HuGrmSei310jEk4fucG_QsvodPyzvLmWVorYznopcycigPANNePv7U0Pw8FAIqslvVxw4YrZgbQ2o0KjDMfhrtK4Kee6RRr-3kd2044DPXe1Og7Jg8qAHNBVKTHledpHdfLh0Mm0OkhfH9ZzxF76jcKHmnyoPa12uAyTLwBIvazfhPraVuEzl07RxzfLq_uhQaeQjdKknTxLEJHs7Mm2-BRAcRZHGWqFNWchng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAv5yehUCUboI5nWLr5dtI4214CHh-CHsMfKVHtQphZSj-L22S2-XJmJz9HmAKA0tAPlY5RSntE47gqZ8l_mYARaNuh4vZOSuKQmUrY04xXz6sffzat24OFD-7wwVMwfX3PHOsuDIRdlPPkHGXQTm3E7Yy8AD5qfYnFLxQ-6ZFBN8iRTANMUzzX6r9g40Xkomjie9MKqSp9zOHX2gVBXgLWZba6Wa9L_JV2P68T2sXvL4pH-bnYLBJ3EgdWxkQe_cSLcCLsd1_MM1vRwaZF7DhtPEaID-WXYiiuy7UHUbLMNoLAeIh-cG3v2eONTkXBC60DDVYt_AtzLoG7rnIACJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGUIVDT29ZYTF5Yv1L64fl3lWx2GTczG9lkDIE60hlPvuTpUqca-SkeIKsaT7OsFABvxQPX1A5LyYBH2lylu911wVQtNCUnRbwAZEwLkZ8lzGu0_Il0gRH0dsR4xKzE0KmqzOYaB0MKEyx9ES3vTRR7Ziu_smjI-XyzFAFzK7XnklENP7ptk9SRNI1Tqj2daqBUKu2f7DWZrTUNMIftbV3fnFo-PVeKdPxdEIguo0gJNKWSrFAzlrjXzvyCOGLgS3T4YFWTNoffx3FIcx8J0VlsMh08KJCPxqn4iGHxHNnymKPBGGEnip-qf0kYq3VDl4H1iw-YVXNwTfX3dHtrURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJdYF7Eunix0pppBDVKAeEzAwK423JvA0F5RwYGy1UcoeNdRMugKuvAFB8m9cCBpd7qZ2_OgRe9sPLdZ_0uoVuD5zmw4utuBl9z6diEim189yan-sydAahkyalqmcqhTdxMZfZfpiNP3zkhkxz8EsGde1INHSlFbO8mHZaQ_7f2N0QYDbDoD-l6cFTS7YqM_fKREoYwHD1r5c28_C0N_FsphkKzIkdOYQrdZeKyI8FrG8z_HfpcOEBky5gEh21uDyIahgpjpL_LFMKwD0TJlj7hL1LioZV4W_5tLkPWee_CL_YzmU2SQqvIUb4IYXGxLzhd3fTVmq52MwRsvMosoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJzt7NCaicu2lWt3iSvobTl-xt5EOCqaLrBrWhgkmqYqWK0Al_UgEwAY5VnvYggrmb3HZtqptHx3Tbi2GcFEFanYcMgIh6jAjQcLqiTw0cTI3RD78H1ICu3q8uOUBZGcL7OQ0SYCSCugv9UbOwiWp714GkGbiFX89wQA-_UYsL9sP1Om8BOgKFhsJhv2SVsVXPldNFCftT6Jv3e0iDKMPHFjfrL0IgeQWE9UpVYdz59zkbIinbAbsntqDK6YukoA477Xoc1BknuFlz10sO_9K_gPyueqFOXb-J_At9HWTCFymeLhl3Vmqh3QQWANRnYbdpSBkMxT60aaA_irc2WWBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=lqURSP1HpUsWFWuHwaDnWJXj-cmaFHjnybuXAqeMPqSgy8qZCwxv98d9MaunTqH609zSzdPQR_jhss-VZMxiINfu2AIMaKwusy-4XAvfg6CxLVhX2v4s-7ZKgdUAO_VTFbAIh0jVUrAfH5u7-0ilSnvWjJ4Kyd99adFIWdvfhbww9x_CG1hXnbkHratD71h8i4iBoNCwEaB4-8P7R7qMZqFolRX4loQtegjKkrU90xw9NtoT8A3xP8fi5Fqqd2m1Ybt4r-S_fdUqWGoOb5Grfryj_HK-tLFK8ye2IfwNjqN9uea9NF_hFgaB3eRaxJoxqzJ88JjZWD00R0ViUEQJcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=lqURSP1HpUsWFWuHwaDnWJXj-cmaFHjnybuXAqeMPqSgy8qZCwxv98d9MaunTqH609zSzdPQR_jhss-VZMxiINfu2AIMaKwusy-4XAvfg6CxLVhX2v4s-7ZKgdUAO_VTFbAIh0jVUrAfH5u7-0ilSnvWjJ4Kyd99adFIWdvfhbww9x_CG1hXnbkHratD71h8i4iBoNCwEaB4-8P7R7qMZqFolRX4loQtegjKkrU90xw9NtoT8A3xP8fi5Fqqd2m1Ybt4r-S_fdUqWGoOb5Grfryj_HK-tLFK8ye2IfwNjqN9uea9NF_hFgaB3eRaxJoxqzJ88JjZWD00R0ViUEQJcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsIbf6l1ZFDQuL-iCR8TbTOLQnD5CwzOriRpSgu-ddmL70ow3Jz4ToYili4JQdTfJxW0Lv3QPZT0axfStL4-3m6CkrbdKeD_siEw1mEYs2Nux8S6SFJNJjfEWvf1-ccUMYOkEWEF60_1eldN5XQQS4_7hQQk_uwrYnZXAHbAArp4bNSz15k2z5Odpb7rI5eM0YLOew5hBzuG_qpEsyiLDHulqzrxrmMaO2BaDa-Y0dt0uPZMeFNS1UF-AdpGrjuy0chps-q_sw09sa7qGQ5BQtMRJYYvCEM32Quz5pNyez1lC-DjqZrhBX8ntMGBpf62MbO1veyrDodOkhDQtsEztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpJTuuDH0yKvzbLE-2YV3KY_8UeChnSSVZi2u9J2aYvas4cxTkWWgnR68V8kn-S64-SOIWm8Qe8ASKsaGaADt50Rx7W_xDwxx2I5MuWtkneb_EALEI4fqVURTRiZM5mfz3fGdCHrzn99T2wQpLC1mqxO1Leo2d9HkM71RM44pRXzO9kzk2MiKug3D0rnIHcrhJdQU9gjynxH1-mqCkSAOETLPHIoh7tDcZfip6QLQGl0NUKDjiLafqhuGy-IizVurq4cSJBdRSWfSts3IAA8zZy4Xrfoga05RA0L7OoMlogtlEN3KkWQaZXu0kpzXMVoVST7uo6rgkmj_LlD4rHwUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Uscr43DJfgODr0tbtsVjK9RCu5b7qArTHpDUg_FSXprGLj50qGP9nUVeSglMfBE053F5mQY3SaeBUpKVnmFN99JEbv2_kTu_kNzPkmbK9eYCIifNS1fcFx3V3SA7tUxcMy7rkaP05D-Q2P45OKvLcZUrr7XvOOylUTCXXualCxmKolNU8uB3Lp3nXqa0E2PEnsPC0cHT4sEl10ToWM-W5PhYNBhz_dF1NXnNsVOccLZlceJAByZE4hRxXB-ruk0CAxIu-SF9Qid0XwI8dmJfQqERg3rych_cTiobl7MmpV0sUF6mxsUQX1PS9P5SC9w8ZAXm5c55UkG7zcQTrDqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
