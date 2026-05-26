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
<img src="https://cdn4.telesco.pe/file/pB7GUftkFk_G_wBDGpfVdKSHlsEWPDUGcabq7pLsMIETbh8laVTg-bH-ks8Us6aC2yJMttJAQKK0JTt_k1O9Qaz7i7CCUsKjfCgcvAYfuz5jO806MjhONBr2PWIMFSxv5vxtbQHwuObgvWPBvZm47ZdOR5c4Qi31j5Jn0hfYtQp9MCUy-VGdQCW8iiqwDhmf6Qj6kts-GSi6qDTFP-r5io7lghWdxR-MVDJuXpwpFjCqWtoDJ9KRzD4FQFLbERvrwkw-1zCDL8M7EoSJ2w9oPgcDi-SiYLpvL3M5467sYHGlLeoLn0hdqtyAcJlytixTOVrX-GmAQqtO0iiFiCEVhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.51K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 23:28:31</div>
<hr>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نت شخمی نشده؟
کانفیگا پولی هم بد وصله
😐
😂</div>
<div class="tg-footer">👁️ 521 · <a href="https://t.me/archivetell/5549" target="_blank">📅 23:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایرانسل پر سرعت وصل
Windscribe UDP 443 Censorship On
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5548" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">همراه اول تست شده
vless://06ef598c-1555-4887-b3f9-08214a2f6792@104.16.7.70:443?encryption=none&host=2026.hhhhh.eu.org&path=%2F222.167.202.31%3A7443&security=tls&sni=2026.hhhhh.eu.org&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/5547" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5546" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5545" target="_blank">📅 22:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-text">پیامهای تشکر و محبت آمیز زیادی دریافت کردم، ظاهرا به خواست خدا وارد قلب هزاران نفر از مردم شدم، فقط میتونم بگم از همگیتون ممنونم.
البته به نظر من کمک اصلی رو "امین محمودی" کرد، پروژه های mhr و masterDNS بینظیر بودن و باعث شد عده ی زیادی متصل بمونن.
واقعا با یک تلاش دسته‌جمعی درصد قابل توجهی از خرید کانفیگهای گران قیمت بی نیاز بودن، افرادی مثل "aleskxyz" ،
"ناکر" ، "samim"، "Sarto" , "shahab", "گروه وایت dns", "مارک پشم‌فروش"  ، "Break_The_Barriers" , "CyberNigga" , "بیا پایین بچه"و ... کمک شایانی در این قضیه انجام دادن.
عده ی زیادی هم تو بحث آموزش این متدها نقش داشتند، عزیرانی مثل "متین سنپای" که آموزشهای روان و ویدیویی در اختیار عموم قرار میدادن که بدون آن قطعا عده‌ی زیادی نمیتونستند از این متدها استفاده کنند.
همچنین جا داره از RPRX بنیان گذار project-X که توجه ویژه ای به ایرانی ها داشت هم تشکر کنم، واقعا v2ray الان به ابزار اصلی ارتباطات اینترنتی تبدیل شده.
از دوست چینیمون "zhc" هم بسیار سپاسگزارم، با دانش بینظیرش کمک قابل توجه ای به مردم ایران کرد.
واقعا یک تلاش بینظیر دسته جمعی صورت گرفت که نمیشه از همه نام برد، من هم خوشحالم که نقشی در این زمینه داشتم، باز هم از همگیتون ممنونم
❤️
///
هنوز نت به طور کامل باز نشده ولی با متدهایی که در حال حاضر وجود داره باز شدن کوچکترین روزنه ای به معنی باز شدن کل اینترنت خواهد بود.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/5544" target="_blank">📅 22:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">همراه اول bdnet وصل</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5543" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHosseini.h</strong></div>
<div class="tg-text">همراه اول bdnet وصل</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5542" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑴𝒓 𝑯𝒂𝒎𝒊𝒅༗</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lI4Btbk4VYr71Z4V03VSH3hrJkoIDi5DaPjlcLzqBOluGZmMU4c5iOGIkLHRm3hxyZ_X6vaYncrwn8JMF6ihybgx3CD4Q79xSde1MmeD-YG8XOfBIxfjvkFlnEkL1AygxZertUOazJeK_pZvcyC8QGGqLXbLcAK5xbyqKER0xeLc_tdmXrJ_2b6vvS0zBpu1kU9JEgAyv2Nt-pDBofdF5ZWJCspAgvnuR1vJ_5tLMk_otMp_FNuhTlqWeI2sRhnWR9W1f4UA2XcY-y7GZFrO7acm9_YjxIZf-z28oVzk3WfJDbfhzwYJqn6Sj-XXzfGYAEHQFtWg0m0dLbBayHOKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZpxHGLnyj1-Z_gaclhxAUXDCLPz5BeyGUnpES_3g50Mqo_g-bEYxSZS3XEPWKqk6EnDIR4gR25AYT1tTqGAzUKMyTdlBTYozYYfZ-v5Bqy-pOLq-Oe_ySppyBzi8kiDligUqdyzog1lW29pjwnjTbEO1ZASHNMAHve_zrCUGrmtjiCMtYEcWXQmsyQwYQKgyCWtDd2dGSp7VGINAKi05ElkX9z5fe2VoBF4kO8zjQwqZCvqmNXsAz_R6Zn3Qv0E8XnRE8-zip6HlSc7QqONmErJXVe5MPdeof7jEoLJIQCcoMLZZapU5K4N98C2QN8jUZVGuYScJZ0C6_Ta3yihng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دوتا وصل شدن همراه اول</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5540" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">vless://IR_NETLIFY@194.59.183.234:42115?type=ws&encryption=none&path=%2F&host=&security=none#IR-NETLIFY
مستقیم وصل</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5538" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">همراه اول کلودفلر وصل
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.18.12.149:40443?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5537" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آیپی تمیز همراه اول
104.18.12.149
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5536" target="_blank">📅 20:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-text">اینم یادتون نره بزارید
شاید بدرد کسی بخوره مستقیم هم سایفون وصله</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5535" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PsiphonProSetup_x64.exe</div>
  <div class="tg-doc-extra">76.1 MB</div>
</div>
<a href="https://t.me/archivetell/5534" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5534" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiliya</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvlcptp3lESSjiRv99CoGFG3iayzBJ8vwxGqjw3Au1i4uyAKhrRq_i_FZA-qFlcapxr-QJ7XFYdfCTvE-9gZJLrNxkRbxmUn8YMMkclsy_NVfloNXZGP3v98GUAUEJIcopnjVchT1Yitux1IAgVqx2qR936Ko3oYfomUbvwJcBpsaYpKlZp-4S4a7aK4tvX4OYCv5ShwPnSJ3mjAvb2LKDALiTLXuluXHFTz-vMRfGPp1w0GYdVeOPK7WrSRG4qu3-chdjaeFmxLV5CuNXrxETuAVpISiA5l_uZhV6qzHnqRoAI6HWNAF0r1ubCy2FoPhZu41Uj-WGP4Nn4aw_M28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0X-2jcDLYhT8QfxVZECp-39Strhrcr6he3G4hfT388kqqPjfqtgjAcz2g4vCXcGN4Qk0AQJY_3x0zQ3gEH9bqnHPSNr15mgcVPUWPwETKaZAhEB4oAenCzaKJcFbbaECxDCfepByFgExB67hAV6pIZ9UESm7oNx8MWJb6LLSojz12t95qM_RZcf2461uQ7_2eXsBZP2ijMe_tJcrB9XuIM5e4EqraZELtUtREq7fz8ZaWh51wsIDWy7qY-3rrCjtnpNtG97GMP803ir07dpdkpidGN0Y-3xinIJ9waxtBCm77Mb1TU6q3nCEnT_ctL66DPptB4nrjMvQVF0cBJR8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنامه ی سری تغییرات دادم و تو خود برنامه میشه کانفیگ زد ترکیبی وصل شد و بین مود های
psiphon
v2ray
v2ray+psiphon
جا ب جا شد</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5532" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آیپی تمیز ایرانسل   27.50.48.49 @ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/5531" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آیپی تمیز ایرانسل   27.50.48.49 @ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5530" target="_blank">📅 20:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://t.me/proxy?server=191.101.113.153&port=443&secret=ee3ef807f06138530624d5631232bfa592636c6f7564666c6172652e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5529" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آیپی تمیز ایرانسل اسکن کردم   واستون میذارم
😁
❤️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5528" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سیمکارت ها هم وصل شدن</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5527" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آیپی تمیز ایرانسل اسکن کردم
واستون میذارم
😁
❤️</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5526" target="_blank">📅 20:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🛡
معرفی ابزار فوق‌العاده Paqctl: عبور از سخت‌ترین فیلترینگ‌ها با دور زدن DPI
---
اگر سرور مجازی (VPS) دارید اما آی‌پی‌تون مدام فیلتر میشه یا سرعتتون به خاطر سیستم‌های تشخیصِ هوشمند (DPI) افت می‌کنه، امروز ابزاری رو بهتون معرفی می‌کنم که قواعد بازی رو عوض کرده:
Paqctl
(بر پایه هسته قدرتمند Paqet).
💡
این ابزار چطور کار می‌کنه؟
روش کار این ابزار با V2ray یا کانفیگ‌های معمولی فرق داره. Paqet ترافیک شما رو از لایه‌های بسیار پایینِ شبکه (Raw Sockets) عبور میده. در واقع پکت‌های اینترنتی رو طوری "دستکاری" می‌کنه (مثلاً فلگ‌های TCP رو تغییر میده یا پکت‌های عمداً خراب می‌سازه) که سیستم فیلترینگ (DPI) گیج میشه، نمی‌تونه تشخیص بده این ترافیکِ پروکسی هست و در نتیجه اجازه عبور میده!
⚙️
دو روش قدرتمند در یک ابزار:
این اسکریپت به شما اجازه میده دو روش مختلف رو روی سرورتون نصب کنید:
۱.
روش Paqet (ساده و پیشنهادی):
از پروتکل KCP روی پکت‌های خام TCP استفاده می‌کنه. شناسایی این روش برای فایروال‌ها بی‌نهایت سخته. خروجی این روش یک پروکسی SOCKS5 روی پورت
1080
سیستم شماست.
۲.
روش GFK (مخصوص سانسور شدید):
از ترکیب پکت‌های "نقض‌شده" (Violated TCP) و تونل QUIC استفاده می‌کنه و در نهایت به یک هسته Xray وصل میشه (پورت
14000
). اگر اینترنتتون به شدت محدوده، این روش معجزه می‌کنه.
---
💻
آموزش نصب سریع (مخصوص لینوکس):
مرحله اول: راه‌اندازی روی سرور (VPS)
وارد سرور لینوکسی خودتون بشید و دستور زیر رو کپی و اجرا کنید (نیاز به دسترسی روت دارید):
curl -fsSL https://raw.githubusercontent.com/SamNet-dev/paqctl/main/paqctl.sh | sudo bash
بعد از نصب، با زدن دستور
sudo paqctl menu
یک منوی جذاب باز میشه که می‌تونید سرویس‌ها رو نصب، استارت یا مدیریت کنید.
برای دریافت اطلاعاتِ اتصال (آی‌پی، پورت و کلیدها) کافیه دستور
sudo paqctl info
رو بزنید.
مرحله دوم: راه‌اندازی روی کلاینت (ویندوز/مک/لینوکس)
ابزار Paqctl فایل‌های کلاینت رو هم در اختیارتون می‌ذاره. کلاینت رو روی سیستم خودتون اجرا می‌کنید و اطلاعاتی که در مرحله قبل گرفتید رو بهش میدید. کلاینت در پس‌زمینه اجرا میشه و به شما یک پورت SOCKS5 میده که می‌تونید اون رو در مرورگر، تلگرام یا برنامه‌هایی مثل v2rayN و NekoBox وارد کنید!
---
🔗
لینک‌های دانلود و گیت‌هاب پروژه:
سورس اصلی پروژه و آموزش‌های دقیق‌تر برای نصب کلاینت ویندوز رو می‌تونید از گیت‌هاب‌های زیر بردارید:
🌐
ابزار مدیریت و نصب آسان (SamNet):
https://github.com/SamNet-dev/paqctl
🌐
هسته اصلی و خام برنامه (hanselime):
https://github.com/hanselime/paqet
⚠️
نکته:
اجرای کلاینت روی ویندوز نیازمند نصب بودن پیش‌نیاز
Npcap
هست که داخل گیت‌هاب کامل توضیح داده شده.
اگر کسی این متدِ Raw Packet رو روی سرورش تست کرد، حتماً از وضعیت پینگ و پایداریش توی کامنت‌ها برامون بنویسه.
👇
📌
#آموزش
#سرور
#فیلترشکن
#VPS
#تونل
#Paqet
#Paqctl
#DPI
#لینوکس
#ویندوز
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5525" target="_blank">📅 20:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همراه اول سورف شارک وصله</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5524" target="_blank">📅 20:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایرانسل cdn شیرو خورشید نسخه جدید وصله سرعت عالی
لینک داخلی شیر و خورشید</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5523" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترکیبی سایفون یا شیر و خورشید با v2ray
ایرانسل و همراه اول
trojan://humanity@193.151.152.206:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5522" target="_blank">📅 20:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلامتی اونی که امروز گیگ بالا اوتباند گرفته
😔
❤️
🍷</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5521" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ی اعلام وضعیت بکنین
با چه اینترنتی و با چ اپی وصلین
👇
:</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5520" target="_blank">📅 19:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)
---
امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.
توی این روش که به کمک پنل
BPB (Bypass Panel)
انجام میشه، شما نیازی به خرید سرور یا دانش برنامه‌نویسی ندارید. پنل شما مستقیماً روی سرورهای قدرتمند کلودفلر (Cloudflare) سوار میشه.
💡
مزایای این روش:
-
رایگان و دائمی:
اکانت رایگان کلودفلر روزانه حدود
۵ تا ۶ گیگابایت
(۱۰۰ هزار ریکوئست) ترافیک به شما میده که برای استفاده معمولِ ۲ تا ۳ نفر (یوتیوب، اینستاگرام و...) کاملاً کافیه.
-
شارژ روزانه:
این حجم هر شب ساعت ۳:۳۰ بامداد (به وقت ایران) دوباره صفر و شارژ میشه!
-
سرعت و پینگ عالی:
به دلیل استفاده از شبکه‌ی کلودفلر.
---
🛠
مراحل راه‌اندازی (قدم‌به‌قدم):
مرحله اول: ساخت اکانت کلودفلر
۱. وارد سایت کلودفلر (
Cloudflare.com
) بشید و ثبت‌نام کنید.
ترفند: برای اینکه ایمیل اصلی‌تون درگیر نشه و بتونید چندین اکانت بسازید، از سایت‌های ایمیل موقت مثل
atomicmail.io
استفاده کنید.
مرحله دوم: نصب اتوماتیک پنل (BPB Wizard)
برای اینکه درگیر کدهای پیچیده نشید، یک ابزار اتوماتیک به اسم BPB Wizard وجود داره که همه کارها رو براتون انجام میده.
⚠️
دو نکته بسیار مهم قبل از اجرا:
- وی‌پی‌ان (VPN) شما باید کاملاً خاموش باشه.
- آنتی‌ویروس (مثل Windows Defender) و فایروال سیستم رو موقتاً خاموش کنید (چون این برنامه کدها رو از گیت‌هاب دانلود می‌کنه، آنتی‌ویروس بهش گیر میده و می‌بندتش).
💻
اگر ویندوز/مک دارید:
ابزار BPB Wizard رو از لینک انتهای پست دانلود کنید، از حالت فشرده خارج کرده و اجرا کنید. مراحل رو با زدن کلید Enter طی کنید تا پنل نصب بشه.
📱
اگر اندروید/لینوکس دارید:
برنامه
Termux
رو باز کنید و کد زیر رو کپی و پیست کنید:
bash <(curl -fsSL https://raw.githubusercontent.com/bia-pain-bache/BPB-Wizard/main/install.sh)
*(نکته: ترموکس رو به هیچ‌وجه از گوگل‌پلی دانلود نکنید، حتماً از سورس اصلی یعنی F-Droid نصب کنید).*
مرحله سوم: تنظیمات داخل پنل BPB
وقتی مراحل بالا تموم شد، ابزار یه لینک به شما میده که تهش
/panel
داره. واردش بشید، یه پسورد قوی بسازید و لاگین کنید.
⚙️
دو تا تنظیم مهم انجام بدید:
۱. تیک IPv6 رو خاموش کنید تا اتصالتون پایدارتر بشه.
۲. تو بخش Routing Rules، تیک Bypass Iran رو بزنید تا وقتی سایت ایرانی باز می‌کنید، ترافیکتون از فیلترشکن رد نشه و سایت‌های بانکی گیر ندن.
---
📲
چگونه به پنل وصل شویم؟
تو پنل خودتون، برید به بخش Subscriptions و لینک بخش
Normal
رو کپی کنید. حالا بسته به دستگاهتون:
🤖
اندروید:
برنامه
MahsaNG
یا Exclave یا V2rayng رو نصب کنید. لینک رو از کلیپ‌بورد Import کنید، از منوی سه‌نقطه Update Subscription رو بزنید و بعد از پینگ گرفتن، متصل بشید.
💻
ویندوز:
برنامه
GUI.for.SingBox
رو دانلود کنید. حتماً روش کلیک راست کرده و Run as Administrator رو بزنید. از داخل پنلِ BPB، فایل
config.json
رو دانلود کنید و تو این برنامه ایمپورت کنید.
🍎
آیفون (iOS):
از اپ استور برنامه
Streisand
رو دانلود کرده و لینک سابسکریپشن رو داخلش وارد کنید.
---
🔗
جعبه ابزار و لینک‌های مورد نیاز:
🌐
سایت کلودفلر:
dash.cloudflare.com
📧
ساخت ایمیل موقت:
atomicmail.io
⚡️
دانلود ابزار نصب BPB Wizard:
🔗
https://github.com/bia-pain-bache/BPB-Wizard
📥
دانلود کلاینت اندروید (MahsaNG):
🔗
[دریافت از گوگل پلی](
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
)
📥
دانلود کلاینت ویندوز (GUI SingBox):
🔗
https://github.com/GUI-for-Cores/GUI.for.SingBox
📌
#آموزش_جامع
#کلودفلر
#فیلترشکن
#Cloudflare
#BPB
#ویندوز
#اندروید
#آیفون
#رایگان
#سرور_رایگان
#VPN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5519" target="_blank">📅 19:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اموزش بچه پایین بیا BPB به زودی گذاشته میشه
راحت شده اسکریپت جدیدش</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5518" target="_blank">📅 19:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از همین تریبون از تمام کسانی که ما رو در این مدت متصل نگهداشتن ممنونم
بخصوص از anonvector گل بابت برنامه خفنش
https://t.me/SlipNet_app
و پترنی‌ها و سایر افرادی که پونز شدن روی صندلی فیلترچی
یادمون نمیره زحماتتون
❤️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5517" target="_blank">📅 19:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مخابرات
trojan://humanity@104.18.32.47:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5516" target="_blank">📅 19:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بمن گفتن زنان قریش رو در اختیارم میذارن
گفتم نه نت پرو؟ ممنون
🙏
👍</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5515" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">https://t.me/proxy?server=51.120.71.120&port=443&secret=c760667d53b6856ca44431fc93b8fe23
https://t.me/proxy?server=95.181.213.248&port=443&secret=ee8a2802995839c6ce8b8f7b0c3bfe44c67777772e617669746f2e7275</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5514" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمهرداد استاپ</strong></div>
<div class="tg-text">من از سازمان بنیاد ملی بازی های رایانه ای باهام تماس گرفتن و قرار بود نت پرو بدن ولی قبول نکردیم و با هزینه شخصی ادامه دادیم</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5513" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLUFFY</strong></div>
<div class="tg-text">شکن عوضی حالا که نتا وا شده چت جی پی تی و اینارو اورده که مردم بخرن که انقدرم خر نیستن مردم</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5512" target="_blank">📅 19:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهاد</strong></div>
<div class="tg-text">اونهایی که پرو نگرفتین دمتون گرم به خودتون افتخار کنید</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5511" target="_blank">📅 19:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهاد</strong></div>
<div class="tg-text">دقیقا و کانال های یوتوبی که اینترنت پرو تبلیغ می کردند</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5510" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiman</strong></div>
<div class="tg-text">ادمین این شکن بیشرف هم که مردمو تهدید میکرد و اکانتاشونو بن میکرد باید توی گروه ها اعلام کنن که هیچکی‌ ازش خرید نکنه. اینارو یادمون نره که کی توی شرایط سخت سنگ مینداخت جلو پای مردم</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5509" target="_blank">📅 19:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه متن کوتاه کامنت کنید در مورد حمید رسایی
😁</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5508" target="_blank">📅 18:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from✨Orchid$✨</strong></div>
<div class="tg-text">لطفا از عبارت "اینترنت داره به حالت عادی برمیگرده" استفاده نکنید.
ما هیچوقت اینترنت عادی نداشتیم.
در بهترین حالت یه فیلترنت بوده با هزاران محدودیت و مشکل...</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5507" target="_blank">📅 18:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝘔 𝘌 𝘕 𝘛 𝘖 𝘙 𝘐 𝘈 𝘟</strong></div>
<div class="tg-text">vless://4115a677-cf46-422f-bc3f-d04352aec2af@104.18.139.67:8443?type=ws&encryption=none&path=%2F&host=ek.cpfreeprize.com&security=tls&fp=chrome&alpn=h2%2Chttp%2F1.1&sni=ek.cpfreeprize.com#Cloud
خواستی اینم بزار واسه مخابرات الان زدم</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5506" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
بچها کسی اگه شکن داره این آیپی و sni بزنه با شیر و خورشید
🚨
⭕️
آیپی :
63.141.252.203
45.89.221.111
142.54.178.211
50.7.5.83
94.130.13.19
204.12.196.34
138.201.54.122
50.7.87.5
94.130.70.160
65.109.34.234
95.216.69.37
85.10.207.48
94.130.33.41
⭕️
Sni :
bbe-getimage.akamaized.net
همراه اول عالی وصله
پرایوت دنس رو ست نکنید ، فقط اعلام آیپی رو بزنید</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5505" target="_blank">📅 18:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lE7dmZQ2Adsu2fXVg0GNqS6iBidUpayGQQI3EPOVjWscV6QWgCbM8Ru2401RRHrMQxBlXIpyGmd_3k0yLS9f31Yxt5Qi5ePtXatUAGzfUNRNbwcZAEj3stzNApGqoJDeSydZ91psScNVAut3B458QBPUMKtnpsZ_4T_kBnktrSOHT3oYCQ6HS4RnemTMGqInDiy6TixCRJaPuAtLH3y7FSndNDbi8sEr_ddr8f6qqqnhH9Uj27XwHqO9BMMTigFWdBrEUNIwg0uKM3LUkQSy9W9KZxpHEjWffOL5x42rigOkvleUad724s8iTLNvmyF__--0j5u2-78SfPtmJZeIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hVG_Q7ECh1_3JaSvxkgg08oiZug2axYZhgLrXD8YuvCzguiCW9xHkrPALwsYHbx-3gkqDPRSKDh00jb1v9hQkmifbo7emGgJTTWxU6F1GQ-iztRtaQ_OeHlhQkPyVXclVzuTdDz4nCIl6hz9HogsUbrsMJ6dI0ZP7ujdX_uU_9SwupJw2weTL5UQeRnJ7reZPEQmJc67iXgVco51iER__Z243kuCrIIUn6CPB-mlZS1q15WO01pDD3bTAwOYvq_LvozblztddSfIRxYdlv4r40htuRbL5OiuE4JxA-gN6pYWpTF_qJizugv6yX-Y0kGCOLsCWCeodVijlnF2ZmU7Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Adsl
سامانتل هم منطقه ای وصله
Express VPN
Houston
Algeria
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5503" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آمار لحظه‌ای اتصال اینترنت کشور:
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5501" target="_blank">📅 18:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مبین نت BOOST VPN وصله
https://play.google.com/store/apps/details?id=com.proxy.fastnode
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5500" target="_blank">📅 18:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad</strong></div>
<div class="tg-text">فعععک نکنم محدودیت روزی دو گیگ چیزی. جالبی باشه</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5499" target="_blank">📅 18:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فشار بخور که خوب فشار میخوری
اونایی که میدونن شبیه چیه
😁</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5498" target="_blank">📅 18:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چه فشاری میخورن اونایی که نت پرو سالانه خریدن ولی الان میبینن بقیه رایگان وصلن
😁</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5497" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTYeCfmgb71gwWTMzmkviR0Kgc0G1VX1lNn51e1iMWUozOUgEreH6XcQ_WtZwzZvWNMVSfSYmgmclBTXCV2DJvYUv9M_bYd669MaXl0mh0YGJJtRBJ06OUqQJohran9yz3Gt4R9X7Ly2d4DzspbgC9LtaVAR7cGMZU7Ep0clNMJDNyKiB6mVBssXUSz1dAyx4dZLgzdjqPw8QjbDrsIEhhQKopkMHcBnOaMuEc5KrjbJHtGIwynpa4oXHPW8ZwoqrbvbcoWrT-Shy0AKxC90vdE83K_WXcFwMh0Yjguft8lSy-rUpnTR_qOATbeHCZXZ_kmDKfvgSSuTpzM1uzv-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبین نت</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5496" target="_blank">📅 17:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFtm</strong></div>
<div class="tg-text">وصل نمی کنند تا همه نت خونگی هاشون رو تمدید کنند</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5495" target="_blank">📅 17:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">نت سیمکارت وصل نمیکنن  یه وقت سیم پرو ها ناراحت نشن</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5494" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">trojan://8r%3C%5B9%27l6hAO%238ZQi@95.38.180.108:40443?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell
مخابرات
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5493" target="_blank">📅 17:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">vless://478cc26d-16b3-4fdd-be64-60d5a58c1622@162.159.36.5:80?encryption=none&host=tt.andishehparenting.com&path=%2F&security=none&type=ws#@ArchiveTell
مخابرات و آسیاتک
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5492" target="_blank">📅 17:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">trojan://8r%3C%5B9%27l6hAO%238ZQi@95.85.28.102:2053?host=Koma-YT.PAGeS.Dev&path=%2FtrTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&sni=Koma-YT.PAGeS.Dev&type=ws#@ArchiveTell%201
trojan://8r%3C%5B9%27l6hAO%238ZQi@57.129.47.56:2053?host=Koma-YT.PAGeS.Dev&path=%2FtrTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&sni=Koma-YT.PAGeS.Dev&type=ws#@ArchiveTell%202
trojan://8r%3C%5B9%27l6hAO%238ZQi@95.85.11.18:2087?host=Koma-YT.PAGeS.Dev&path=%2FtrTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&sni=Koma-YT.PAGeS.Dev&type=ws#@ArchiveTell%203
مخابرات و آسیاتک
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/5491" target="_blank">📅 17:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سامانتل کجایی که ببینی مخابرات و آسیاتک وصل شده
😁</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5490" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دایرکت کانال چند نفر گفتن فیبر نوری ایرانسل هم وصل شده..</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5489" target="_blank">📅 17:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAq5xE7ib_CXvGCqsS3OE2jG_bwWy8SBdHHZdW7igEkguP05dFq4Pv8vKoU-xEWGJI9p-5SocQMJ4jd9xpkwHGAo6vMUUPex8Qoh7HEAHh8pa5-_azkjlQiMSru9TZrZNLK7UNsoWn9rHap3lp-a7szvdoHS1f6BvKF7DhieqDiEvijdnIGAfwyu2TT1uZEY0wluGfXj7anXIUMO5q_pIANFOmPmPJO_oIGSy3KnsjtPJe9-6TqbnDWlVvUE1b189FasqQWtaVC3C3skR6IA5wOpKV9CB3gd99dVXGYQe6Bk-cc8rA9g8SdqSz2EbNpp-dNxzk56Bjs8Wf8P64eXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرات توییتر بدون فیلتر میاره..
آیپی ایران انداخته
😁</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5488" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مخابرات یوتیوب بدون فیلتر میاره..</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5487" target="_blank">📅 16:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آسیاتک و مخابرات
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.21.7.21:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5486" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سایفون رو اینترنت مخابرات وصل شد ...</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/archivetell/5485" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مخابرات و آسیاتک
trojan://8r%3C%5B9%27l6hAO%238ZQi@speedtest.net:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5484" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مخابرات و آسیاتک
trojan://8r%3C%5B9%27l6hAO%238ZQi@172.66.47.69:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5481" target="_blank">📅 16:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انگار آسیاتک و مخابرات وصل شدن بعضی فیلترا..</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5480" target="_blank">📅 16:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدای انفجار در نزدیکی مجتمع Config Sellers
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5479" target="_blank">📅 15:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اپ استور رفع فیلتر شده..
پ.ن: بسته شد</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/5478" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">{
"_comment": {
"remark": "@ArchiveTell"
},
"log": {
"access": "",
"error": "",
"loglevel": "info",
"dnsLog": false
},
"inbounds": [
{
"tag": "in_proxy",
"port": 1080,
"protocol": "socks",
"listen": "0.0.0.0",
"settings": {
"auth": "noauth",
"udp": true,
"userLevel": 8
},
"sniffing": {
"enabled": false
}
},
{
"tag": "http-in",
"port": 10808,
"listen": "::",
"protocol": "http"
}
],
"outbounds": [
{
"tag": "proxy",
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "104.18.20.213",
"method": "chacha20-poly1305",
"ota": false,
"password": "humanity",
"port": 443,
"level": 8,
"flow": ""
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"wsSettings": {
"path": "/assignment",
"headers": {
"Host": "www.calmloud.com"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "www.calmloud.com",
"alpn": [
"http/1.1"
],
"fingerprint": "ios",
"show": false
},
"sockopt": {
"dialerProxy": "fragment",
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
},
"mux": {
"enabled": false,
"concurrency": 8
}
},
{
"tag": "fragment",
"protocol": "freedom",
"settings": {
"domainStrategy": "AsIs",
"fragment": {
"packets": "tlshello",
"length": "100-200",
"interval": "10-20"
}
},
"streamSettings": {
"sockopt": {
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
}
},
{
"tag": "direct",
"protocol": "freedom",
"settings": {
"domainStrategy": "UseIp"
}
},
{
"tag": "blackhole",
"protocol": "blackhole",
"settings": {}
}
],
"dns": {
"servers": [
"8.8.8.8"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5477" target="_blank">📅 15:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc6654627.mp4?token=jP1dj20s9A6ILEON6trJZptUehwPK-0bkjDVsuD_KGlnupMkcjdGctFx81r8og1e4Qk4-PGBrYIkO16icppbEz1vRIcLSPeTWwX3RtVnMOxotjjL4YT4_-1UiN-ecOIhZGtgD5ujSP2wSlbB2K_8dxl7qmDrRTbJYk2Iu4-avEWo1svyrrP-jLHAKG-3nxrvclxk03QD09xyQTd2KlEwM_QfKgDflyVPBQ79WpRcabPlVXB30ShxgBo-SmFc7uKf4XMSbU53_ux5e0wWthFC10vtNiFziNQcELzirs6Rd70Q1nZEmLwfyDxS0-vxjrqx1XuBVwgiNnlxwv80bD5oeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc6654627.mp4?token=jP1dj20s9A6ILEON6trJZptUehwPK-0bkjDVsuD_KGlnupMkcjdGctFx81r8og1e4Qk4-PGBrYIkO16icppbEz1vRIcLSPeTWwX3RtVnMOxotjjL4YT4_-1UiN-ecOIhZGtgD5ujSP2wSlbB2K_8dxl7qmDrRTbJYk2Iu4-avEWo1svyrrP-jLHAKG-3nxrvclxk03QD09xyQTd2KlEwM_QfKgDflyVPBQ79WpRcabPlVXB30ShxgBo-SmFc7uKf4XMSbU53_ux5e0wWthFC10vtNiFziNQcELzirs6Rd70Q1nZEmLwfyDxS0-vxjrqx1XuBVwgiNnlxwv80bD5oeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5476" target="_blank">📅 15:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKMUVJknxq-q-uVUX4Vk4V5uKPOW8Ycd0wT603QvAvPYGcV3epqM52Q9N5j5rlN1HqigDuIRGX-woSrySBy6L4z4_TaFrZE6E81D6EbSVkeHQ3d8EleaL1TPziHNe9W8E1E4M0wYQKcKK_FWquysxOWR0MHp8ixfwCMtYIxVdsJ26HegqYso1wUAP1n-Ef_edxynEA8QG2kI5fsX5ABEDcXuquGZItC3_CBAyyDDvKtMh5_MJjbIpPTYELiUvSgjAs4VMtRoqUdOUnB-0rK7MZRTZMmyp7g1M3HLQ9FoN46Pse6xpVaMk1OTi4bELchUZTUGpIQp4R4NJKYeRXeMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالله
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5475" target="_blank">📅 15:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ی چهارتا سوراخو فقط باز میکنن هیچ چیز به عقب برنمیگرده نظر من</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5474" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">{ "_comment": { "remark": "@ArchiveTell" }, "log": { "access": "", "error": "", "loglevel": "info", "dnsLog": false }, "inbounds": [ { "tag": "in_proxy", "port": 1080, "protocol": "socks", "listen": "0.0.0.0", "settings": { "auth": "noauth", "udp": true, "userLevel":…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5473" target="_blank">📅 15:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">{
"_comment": {
"remark": "
@ArchiveTell
"
},
"log": {
"access": "",
"error": "",
"loglevel": "info",
"dnsLog": false
},
"inbounds": [
{
"tag": "in_proxy",
"port": 1080,
"protocol": "socks",
"listen": "
0.0.0.0
",
"settings": {
"auth": "noauth",
"udp": true,
"userLevel": 8
},
"sniffing": {
"enabled": false
}
},
{
"tag": "http-in",
"port": 10808,
"listen": "::",
"protocol": "http"
}
],
"outbounds": [
{
"tag": "proxy",
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "
104.18.12.149
",
"method": "chacha20-poly1305",
"ota": false,
"password": "humanity",
"port": 443,
"level": 8,
"flow": ""
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"wsSettings": {
"path": "/assignment",
"headers": {
"Host": "
www.calmloud.com
"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "
www.calmloud.com
",
"alpn": [
"http/1.1"
],
"fingerprint": "ios",
"show": false
},
"sockopt": {
"dialerProxy": "fragment",
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
},
"mux": {
"enabled": false,
"concurrency": 8
}
},
{
"tag": "fragment",
"protocol": "freedom",
"settings": {
"domainStrategy": "AsIs",
"fragment": {
"packets": "tlshello",
"length": "100-200",
"interval": "10-20"
}
},
"streamSettings": {
"sockopt": {
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
}
},
{
"tag": "direct",
"protocol": "freedom",
"settings": {
"domainStrategy": "UseIp"
}
},
{
"tag": "blackhole",
"protocol": "blackhole",
"settings": {}
}
],
"dns": {
"servers": [
"
8.8.8.8
"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
این وصله</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5472" target="_blank">📅 15:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">@SHADOW_CONFBOT  کانفیگ رایگان کلادفلر و باقی سی دی ان ها، فایل هارو بگیرید و آیپی تمیز رو جایگزین کنین  برخی کانفیگ ها شاید تموم شده باشن پس تست بزنید و آیپی جایگذاری کنین</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/5471" target="_blank">📅 15:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">@SHADOW_CONFBOT
کانفیگ رایگان کلادفلر و باقی سی دی ان ها، فایل هارو بگیرید و آیپی تمیز رو جایگزین کنین
برخی کانفیگ ها شاید تموم شده باشن پس تست بزنید و آیپی جایگذاری کنین</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5470" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چند دقیقه وصل کردن تا حرف پزشکیان رو هوا نمونه
😁</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5469" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قطع شد..</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5468" target="_blank">📅 15:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">همه نتا وصله
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.16.89.120:2096?host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5467" target="_blank">📅 15:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همه نتا وصله
trojan://humanity@104.16.89.120:443?host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5466" target="_blank">📅 15:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اونایی که ورکر دارن ، این آیپی استفاده کنن
104.16.7.70
اپیوس و ...</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5465" target="_blank">📅 15:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">trojan://humanity@104.16.7.70:443?host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5464" target="_blank">📅 15:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">trojan://8r%3C%5B9%27l6hAO%238ZQi@104.16.7.70:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5463" target="_blank">📅 15:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">vless://388a6c57-87e7-420b-afe2-b3eb670fd7da@104.16.7.70:80?encryption=none&host=vip.yaml7.ggff.net&path=%2F+%40ProxyVPN11&security=none&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5462" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@104.16.7.70:443?encryption=none&host=2026.hhhhh.eu.org&path=%2F222.167.202.31%3A7443&security=tls&sni=2026.hhhhh.eu.org&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5461" target="_blank">📅 15:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:8443?allowInsecure=1&encryption=none&host=sni.111000.dynv6.net&path=%2F%3FTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&security=tls&sni=sni.111000.dynv6.net&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5460" target="_blank">📅 15:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">trojan://humanity@104.18.139.67:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5459" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایرانسل ، رایتل و مخابرات وصله..</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5458" target="_blank">📅 14:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">trojan://humanity@104.18.139.67:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5457" target="_blank">📅 14:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وای فای وصله   trojan://humanity@104.16.7.70:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5456" target="_blank">📅 14:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وای فای وصله
trojan://humanity@104.16.7.70:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5455" target="_blank">📅 14:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانفیگ SNI Spoofing با لوکیشن های مختلف
Finland:
vless://cbf524f0-4d7c-4173-aafb-e9f0608b3192@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1%2Ch3&encryption=none&host=focalin.yhbj.store&mode=auto&path=%2FGoorbeh&security=tls&sni=focalin.yhbj.store&type=xhttp#@ArchiveTell%20Finland
Germany:
vless://a01daac7-1e65-4645-854d-b47d226f6b08@127.0.0.1:40443?encryption=none&host=y6-3cj.PAgES.DEV&path=%2F&security=tls&sni=y6-3cj.PAgES.DEV&type=ws#@ArchiveTell%20Germany%20
France:
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%20France%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5454" target="_blank">📅 13:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">{
"_comment": {
"remark": "@ArchiveTell"
},
"log": {
"access": "",
"error": "",
"loglevel": "info",
"dnsLog": false
},
"inbounds": [
{
"tag": "in_proxy",
"port": 1080,
"protocol": "socks",
"listen": "0.0.0.0",
"settings": {
"auth": "noauth",
"udp": true,
"userLevel": 8
},
"sniffing": {
"enabled": false
}
},
{
"tag": "http-in",
"port": 10808,
"listen": "::",
"protocol": "http"
}
],
"outbounds": [
{
"tag": "proxy",
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "172.64.152.23",
"method": "chacha20-poly1305",
"ota": false,
"password": "humanity",
"port": 443,
"level": 8,
"flow": ""
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"wsSettings": {
"path": "/assignment",
"headers": {
"Host": "www.calmloud.com"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "www.calmloud.com",
"alpn": [
"http/1.1"
],
"fingerprint": "ios",
"show": false
},
"sockopt": {
"dialerProxy": "fragment",
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
},
"mux": {
"enabled": false,
"concurrency": 8
}
},
{
"tag": "fragment",
"protocol": "freedom",
"settings": {
"domainStrategy": "AsIs",
"fragment": {
"packets": "tlshello",
"length": "100-200",
"interval": "10-20"
}
},
"streamSettings": {
"sockopt": {
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
}
},
{
"tag": "direct",
"protocol": "freedom",
"settings": {
"domainStrategy": "UseIp"
}
},
{
"tag": "blackhole",
"protocol": "blackhole",
"settings": {}
}
],
"dns": {
"servers": [
"8.8.8.8"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5453" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ی چهارتا سوراخو فقط باز میکنن
هیچ چیز به عقب برنمیگرده
نظر من</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5452" target="_blank">📅 11:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔥
آموزش اجرای روش جدید SNI-Spoofing (ابزار ZeroDPI) برای ویندوز و اندروید
---
رفقا سلام!
✋
ابزار جدید و فوق‌العاده‌ای به اسم
ZeroDPI
منتشر شده که به زبان قدرتمند Rust نوشته شده و می‌تونه محدودیت‌های فیلترینگ (مثل مسدود بودن کانفیگ‌های مستقیم) رو به زیبایی و شفافیتِ تمام دور بزنه.
این ابزار با روش‌های پیشرفته‌ای مثل (TLS SNI Spoofing) بستهِ فیلترینگ رو فریب میده و اینترنت آزاد رو در اختیارتون می‌ذاره. سرعت بالا و پایداری از مهم‌ترین ویژگی‌های این روشه.
💻
مرحله اول: دانلود و راه‌اندازی ZeroDPI روی ویندوز
۱. کلاینت ZeroDPI (نسخه ویندوز) رو مستقیماً از گیت‌هاب دانلود و اکسترکت کنید:
🔗
https://github.com/nullroute1970/ZeroDPI/releases/download/v0.1.0-20260525T092918Z-bd03a3d79aa4/zerodpi-windows-x86_64.zip
۲. فایل
config.toml
رو باز کنید و مقادیر زیر رو دقیقاً به این شکل تغییر بدید و سیو کنید:
LISTEN_HOST = "0.0.0.0"
LISTEN_PORT = 40443
SCAN_TIMEOUT_SECS = 20
۳. فایل
zerodpi.exe
رو کلیک راست کرده و حتماً با
Run as administrator
اجرا کنید. صبر کنید تا تست اولیه تموم بشه و لیست SNIها بالا بیاد؛ روی همون گزینه اول اِنتر (Enter) بزنید. حالا ZeroDPI آماده‌ست!
---
📥
مرحله دوم: پیدا کردن کانفیگ‌های سالم
۱. وارد این مخزن کالکتور بشید:
🔗
https://github.com/Delta-Kronecker/V2ray-Config
۲. از جدول اول، یکی از گروه‌های ۵۰۰ تایی رو باز کنید. کانفیگ‌ها رو کپی کنید و داخل برنامه
v2rayN
پیست (Paste) کنید.
۳.
تنظیم تست سرعت:
تو v2rayN برید به
Settings ➔ Option Settings ➔ v2rayN settings
و آدرس
Speed test URL
رو برابر مقدار زیر قرار بدید:
https://cachefly.cachefly.net/1mb.test
۴. حالا کانفیگ‌ها رو تو دسته‌های ۱۰۰ تایی انتخاب کنید و کلید
Ctrl+T
(یا کلیک راست و Real ping) رو بزنید. بر اساس پینگ مرتب‌شون کنید.
۵. اونایی که پینگ دادن رو انتخاب کنید و کلید
Ctrl+D
(تست دانلود) رو بزنید. هر کدوم که عددِ دانلود رو نشون داد، یعنی وصل میشه. روش دابل کلیک کنید تا فعال بشه.
⚠️
نکته بسیار مهم:
حتماً روی حالت
System Proxy
بذارید و حالت TUN رو خاموش کنید!
---
📱
مرحله سوم: اشتراک‌گذاری اینترنت آزاد به اندروید (بدون نیاز به کانفیگ روی گوشی)
اگر می‌خواید گوشی‌تون هم بدون دردسر وصل بشه (دقت کنید گوشی و لپ‌تاپ باید به یک وای‌فای وصل باشن):
۱. تو ویندوز،
CMD
رو باز کنید و بنویسید
ipconfig
. عددِ جلوی
IPv4 Address
رو یادداشت کنید.
۲. برگردید تو v2rayN؛ روی همون کانفیگی که الان بهش وصلید، دابل‌کلیک کنید تا ادیت بشه.
۳. مقدارِ
Address
رو از
127.0.0.1
پاک کنید و اون آدرس IPv4 (مرحله ۱) رو جاش بنویسید و ذخیره کنید.
۴. حالا روی همون کانفیگ کلیک راست کنید و گزینه
Share
رو بزنید.
۵. بارکدی (QR Code) که میده رو با برنامه v2rayNG گوشیتون اسکن کنید و بهش وصل بشید!
✅
تمام.
اگه جایی به مشکل خوردید، تو کامنت‌ها بنویسید.
👇
📌
#آموزش
#ویندوز
#اندروید
#SNI_Spoofing
#تونل
#فیلترشکن
#ZeroDPI
#v2rayN
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5451" target="_blank">📅 10:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">trojan://humanity@127.0.0.1:40443?host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%201
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%202
trojan://humanity@127.0.0.1:40443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%203
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%204
trojan://humanity@127.0.0.1:40443?alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell%205
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%206
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.multiplydose.com&type=ws#@ArchiveTell%207
کانفیگ های UDP واسه SNI Spoofing
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5450" target="_blank">📅 09:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">لینک داخلی
سایفون اندروید
سایفون ویندوز
شیر و خورشید
Mahsang
تلگرام ویندوز
تلگرام اندروید نسخه سایت
تلگرام اندروید نسخه گوگل پلی</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5449" target="_blank">📅 08:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">{
"_comment": {
"remark": "@ArchiveTell"
},
"log": {
"access": "",
"error": "",
"loglevel": "info",
"dnsLog": false
},
"inbounds": [
{
"tag": "in_proxy",
"port": 1080,
"protocol": "socks",
"listen": "0.0.0.0",
"settings": {
"auth": "noauth",
"udp": true,
"userLevel": 8
},
"sniffing": {
"enabled": false
}
},
{
"tag": "http-in",
"port": 10808,
"listen": "::",
"protocol": "http"
}
],
"outbounds": [
{
"tag": "proxy",
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "172.64.152.23",
"method": "chacha20-poly1305",
"ota": false,
"password": "humanity",
"port": 443,
"level": 8,
"flow": ""
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"wsSettings": {
"path": "/assignment",
"headers": {
"Host": "www.calmloud.com"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "www.calmloud.com",
"alpn": [
"http/1.1"
],
"fingerprint": "ios",
"show": false
},
"sockopt": {
"dialerProxy": "fragment",
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
},
"mux": {
"enabled": false,
"concurrency": 8
}
},
{
"tag": "fragment",
"protocol": "freedom",
"settings": {
"domainStrategy": "AsIs",
"fragment": {
"packets": "tlshello",
"length": "100-200",
"interval": "10-20"
}
},
"streamSettings": {
"sockopt": {
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
}
},
{
"tag": "direct",
"protocol": "freedom",
"settings": {
"domainStrategy": "UseIp"
}
},
{
"tag": "blackhole",
"protocol": "blackhole",
"settings": {}
}
],
"dns": {
"servers": [
"8.8.8.8"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5448" target="_blank">📅 08:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">{
"_comment": {
"remark": "@ArchiveTell"
},
"log": {
"access": "",
"error": "",
"loglevel": "info",
"dnsLog": false
},
"inbounds": [
{
"tag": "in_proxy",
"port": 1080,
"protocol": "socks",
"listen": "0.0.0.0",
"settings": {
"auth": "noauth",
"udp": true,
"userLevel": 8
},
"sniffing": {
"enabled": false
}
},
{
"tag": "http-in",
"port": 10808,
"listen": "::",
"protocol": "http"
}
],
"outbounds": [
{
"tag": "proxy",
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "104.18.12.149",
"method": "chacha20-poly1305",
"ota": false,
"password": "humanity",
"port": 443,
"level": 8,
"flow": ""
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"wsSettings": {
"path": "/assignment",
"headers": {
"Host": "www.calmloud.com"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "www.calmloud.com",
"alpn": [
"http/1.1"
],
"fingerprint": "ios",
"show": false
},
"sockopt": {
"dialerProxy": "fragment",
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
},
"mux": {
"enabled": false,
"concurrency": 8
}
},
{
"tag": "fragment",
"protocol": "freedom",
"settings": {
"domainStrategy": "AsIs",
"fragment": {
"packets": "tlshello",
"length": "100-200",
"interval": "10-20"
}
},
"streamSettings": {
"sockopt": {
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
}
},
{
"tag": "direct",
"protocol": "freedom",
"settings": {
"domainStrategy": "UseIp"
}
},
{
"tag": "blackhole",
"protocol": "blackhole",
"settings": {}
}
],
"dns": {
"servers": [
"8.8.8.8"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5447" target="_blank">📅 08:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لینک داخلی Mahsang
دانلود</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5446" target="_blank">📅 08:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با سایفون ِ داخلی‌ش سر و کله نزنید. روش سنتی و راحت:
برید داخل Settings مهسا و Mode رو بذارید رو Proxy only،
داخل اپ سایفون / شیر و خورشید اپ مهسا رو اکسکلود کنید (که مشمول وی‌پی‌ان نباشه)،
هاست و پورت رو هم بدید:
127.0.0.1
10809
حالا اول یکی از دو کانفیگ مذکور رو داخل مهسا ران کنید (با دکمه‌ی M پایین برنامه)، و بعدش سایفون / شیر و خورشید رو. والسلام</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/5445" target="_blank">📅 08:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXTp9D6-mCjLhbQs5HBgzYfbShYfpoVjj72u0UvcIhnZHvD0hLULFeT2VtQ3cyB1dRfjg115OYS9oC-XUvVyFlPxA-b9hkAliq3uUVtkG3ULYVri6P6uvJE83GkfYAyA278GyFXu9xvfML9xA0hnCDJc_r7rZvDuu3Mw6zSOXI7aVaUr9Pb4OGqNLoGECm29ZYB7VMyIdhI4WTEsUwSdRpQadOeYJ4sJn22PDi2DaRzbDI_g7M_O4jtKRAoqcuLUlhlOvNyegIxaWJQrjRfFLet4j6L4D3Om9exW4iyNGJiAYS-H1Xu06iRrwg5tSC2oBLdO61yROoNML8zQxfBdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeyL-NQp5a0TusFodU6aCFHZuylZUh9o3R8P-WCT1WXTyDYM_hNvcy0q5qbf-XC93fIlrC8UXZf4TTkvJzUPAUdK5NmMW2sabhdZNj3S_Wv7acN4lrRSG8h_bD6BIn_Mrkd-EjhckrfYaWjMSDtOLLxiJrsQt7OP9ue5ewFWqGt-IY6RsxBCxNtj0KxlCaKE78kZTZOG-u0uEmpaMJDyf3iNgOA-AMj8XjvpUO2VV1tLxQ8RgSLM89DZCwfDMKUIekLVUsFnHSLwStGZSgPHppHaqLbxphZt4x_4_tZyMSEJePY-YBZ9ioDZxRG3KPQd_d8W6QTjQYXSP1WOK6zKew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این روش رو تست کردم فوق العاده است بذارید کانال
اگر کلاینت MahsaNG رو دارید انجام بدید وصل میشه
لینک داخلی
اگر سایت گیتهاب براتون باز هست:
از منوی برنامه مهسا ان جی، اورژانسی EMS، کانفیگ دریافت کنید
دو عدد کانفیگ ترکیبی مشاهده میکنید یکی رو انتخاب کنید
در تنظیمات سایفون Protocol رو روی Auto بذارید و Aggressive رو ON کنید و Save بزنید
دکمه psiphon-after از منوی F رو روشن کنید و Save بزنید
نیازی به روشن کردن فرگمنت از منوی F نیست
دکمه M رو روشن کنید و 30 ثانیه صبر کنید تا سایفون متصل بشه. پینگ بگیرید و از کانفیگ رایگان لذت ببرید
زحمت ایت این آموزش رو این عزیز کشیده
@Khode3ilent</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5443" target="_blank">📅 08:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">داداش درسته که قبلا هم چند جا نوشتن ولی باز بنویسی و یادآوری کنی بد نیست.  اینکه حتما pass key بذارن رو اکانتشون تا اگه تلگرام انداخت بیرون بتونن باهاش دوباره لاگین کنن. چون ممکنه اس ام اسش نیاد و نتونن مجدد وارد اکانتشون بشن.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5442" target="_blank">📅 03:10 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
