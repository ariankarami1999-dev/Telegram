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
<img src="https://cdn4.telesco.pe/file/Z4wiiuiVe61UCx3MfhDVZoJfvttJy6ziEJxQM6q0EBAqKuT1xPMaaA5zmyWug2XWvUsibuGr8ZT-vkAtNbtCDDOkDsNMaAsK1PhgWtWmXzXuBZYfzqeC0Q_Ly6YanQnIKTOzLe0ZsznJ1XP-PSmZIr9Jh931rOU7xL6JL53I-8fCFju36Vwh3E5DG6jqMxUYr0nCs_UQf4as2ULk75ITWkRWU4TdaaGXj7h-yS1GZiHvGonYKB5yujj7zYLyizQlRpJv1RjKv_sfxvswYiAB7k5C0N0DSQBsB3I4jpL5atg_ne1sa_DFGQCfJLiq9ZkdTpAasb3MAEBxOi7NIpCzFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWGfMfxSbYpyJ-d3OUimRnWnd5xCyF7vSLyAkM5gSHubV3fBwRjMGliw2xf071tY_mYUzLhO_uXfWol-S-2XvKpEyvw-p1hvnZTlYMRGOBdQCxRlJx2cO5e67YlgQnxVJnH0BVhSBnfP9JheA8lQLZpP7uSgbkO2K8d8zIIRJh21gZjALdf3Wa6hWFkmzbxeIlGr9TVYfoeY7CY5CNxndzC3bydtwaJoVMlWatdyQjEIyaA55MiJc6Lx0PzaksZbY98ZMJ1cskYXUHKTXPVJPuRgqE7T_UT76WiYEIXgsxaxm4ova0STtPevRWZNgw856ngo69cHHII_ZzhFqCmc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYPH6B9NTq2OOGuDuyIp5zKhHRktqySza1PlT_cqg6gOv5mkv9QccFI2O1yNUiQ9R3jBAwjXsPxLEAJAgYN2FhWpgvcu-OG6y5jos1yNk-5ljsvN-ih6TtdCQ95MDPw91AUUohHfEddc13b51Y_-dGtOlSscSUPRSnr2YwSHlZcIar0BUcg3e_vMNlo4gxbzSCwzCqx3dtyW1rbbByTNeN5RUeMVxvoU7HL_jLDL8nv-dLGtLpXeAzRFq9ji75IIv7IxdxftBVKsXIa1cWo1QmFhhE20wVmly2k08ym7IHfqgxNq2hAiRvCLndtnmR2l68Em3JSc7HhDyplQ8Pmhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=GXOjyDTTlKTq1FsI5dFfLjL3HGdzMNkVHR_7VruxDaVCXjnkphDunqSwjcbU1xPnCKMp3LWqxIkYM3xh_QGAQ7Pgq8slLXWyKS0iYWY4EjUfYZ3aQxCZjOWUo2t0ZKOt9Zirjti598Gwi2EcRPYQPRGRRsNhhfJj8wnIPVGLCrfuwJdLSUnSuDpklvMsTT07b4TIbYx7VS4O5xGlE3sNCtUMHER26J-Ddaii6qZtHhmeiG4R7O_Z1S8xSYldP1QD4dppn9Megif-cZQsb6E0ggg0yK-gBi-vZrel5OjSIM4H70cL9cXLcOTP9Rm61c7wLkGbDAmzXSa2n6YKkjmitg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=GXOjyDTTlKTq1FsI5dFfLjL3HGdzMNkVHR_7VruxDaVCXjnkphDunqSwjcbU1xPnCKMp3LWqxIkYM3xh_QGAQ7Pgq8slLXWyKS0iYWY4EjUfYZ3aQxCZjOWUo2t0ZKOt9Zirjti598Gwi2EcRPYQPRGRRsNhhfJj8wnIPVGLCrfuwJdLSUnSuDpklvMsTT07b4TIbYx7VS4O5xGlE3sNCtUMHER26J-Ddaii6qZtHhmeiG4R7O_Z1S8xSYldP1QD4dppn9Megif-cZQsb6E0ggg0yK-gBi-vZrel5OjSIM4H70cL9cXLcOTP9Rm61c7wLkGbDAmzXSa2n6YKkjmitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=RvgOThWCk30BNbhADIwMoqi5QeVsm9vkQKFrxWZUe9M5sV6YjE0OC0z3cl0VNs4qnw6s_J_Kdzl5Qk2H95f9SmQ7txlM0JWoAUiJis1Wv2SXj2daEZUsBu56QvOpymv-C-JU2NPwQc6uaWpRBGw4B12Otv6w04UGc9ggiXsm-GwnGgu4ceU0IX7aoBFNm6URamxC3eDWaCcZCeEXAcljEhXCO_dMnCO58jdWL-zq6Xr_Zw7MHM-OlkoaDGyrhLm0H4O1WdsWZOb8c3zf3BctVqODs6il-ejkPScM8wc1xdAe_3ziwZvik1FKnrUZNbeQFFSdHaFsyhws4pIslm0jPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=RvgOThWCk30BNbhADIwMoqi5QeVsm9vkQKFrxWZUe9M5sV6YjE0OC0z3cl0VNs4qnw6s_J_Kdzl5Qk2H95f9SmQ7txlM0JWoAUiJis1Wv2SXj2daEZUsBu56QvOpymv-C-JU2NPwQc6uaWpRBGw4B12Otv6w04UGc9ggiXsm-GwnGgu4ceU0IX7aoBFNm6URamxC3eDWaCcZCeEXAcljEhXCO_dMnCO58jdWL-zq6Xr_Zw7MHM-OlkoaDGyrhLm0H4O1WdsWZOb8c3zf3BctVqODs6il-ejkPScM8wc1xdAe_3ziwZvik1FKnrUZNbeQFFSdHaFsyhws4pIslm0jPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=PgiT8J66GuhSYCyzzcnzOWQIP--SkJZOgE44OZ5O4J9juGHhrZ4EU-9k787XsKUtc0Fp7NFxBuylVk9d5g2zeHj4ebkKCX4qmcTaMqwdth3PsW9ZgnBIyfXzPJ_CfEmSjGl3BkBXAWuzJN6iPQeV92Zh8wkVUgstRedbU7WX4MFa3Yzn2wMjIgT81MlZrNJ8F0Lli3K0qQ7aXek-QLgObgcafVvoGy1EtpA1j-abwAiII5Yi3zzKf93UYVa77zSV9gbZ2kbSYnfdmO-SuGFN6ePv1HuJasJCpFZbEe9PkIeuApKDcfXk1M3SOeNXOBa0DChqxxd8PKVT2dCQd_2f4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=PgiT8J66GuhSYCyzzcnzOWQIP--SkJZOgE44OZ5O4J9juGHhrZ4EU-9k787XsKUtc0Fp7NFxBuylVk9d5g2zeHj4ebkKCX4qmcTaMqwdth3PsW9ZgnBIyfXzPJ_CfEmSjGl3BkBXAWuzJN6iPQeV92Zh8wkVUgstRedbU7WX4MFa3Yzn2wMjIgT81MlZrNJ8F0Lli3K0qQ7aXek-QLgObgcafVvoGy1EtpA1j-abwAiII5Yi3zzKf93UYVa77zSV9gbZ2kbSYnfdmO-SuGFN6ePv1HuJasJCpFZbEe9PkIeuApKDcfXk1M3SOeNXOBa0DChqxxd8PKVT2dCQd_2f4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=fQhnPMJmzMItG44aVNnVnpqBFGNwJqyJOpgy22Y8h_FGbO54zdhDra5OkaSXESTEpc6uEWPDW5gEIeFkSKDApK-JH3FKsYtzkIamPYbGD7EPhXA5nHAzLweJGlOHrtEK77FfdFWNVcIfNRWu5GVyfHMGfcDR1gH_0gcwM7DDquhLIvRrpm8M4w6U1sOxWv2iSnxKfAl1Wm8fYQyoT0dn-bDNlPn86qqQy3SE_B0cWIk6bne0KVyTeccYVRigKMYL0uW_HgWG06K8IO_JrOgwTAMyOhN9416Q0gdSne7uDhTwpG39puedTkd1MfGGUdW1mD8DKSE1lB4dYJ9mM_xYX5BLXP4NCn67GsVExU-U_jSpsm3BuIt5EtjtiU98-lfkYbnlzgpQW648fBRJQ3Qd6D-I9PsgjUeUk1UpDV31cmxoh2n7xSlEJx7tl_8bgBi4YRpcq0LUnQBivgo_JETyRXFL0LTwvg2iJUoXk4g93heYLmkZUfBpoQtqFE_iirb3zHQEAGR4F5ljo0KVDubsP2SiGHieqLynSl3cMVD09IzfSP0Z_y-KJbaPfRiy0vlN8B50zNAgoUq11CozUys7Q7985sc5lhZGWyBYCc2-FvP42ARZNCRXUy_f3673YPJt2E5lKDGen7KwVkgaQWF1QK-k0f8E7lSh4J2Cdnmz10Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=fQhnPMJmzMItG44aVNnVnpqBFGNwJqyJOpgy22Y8h_FGbO54zdhDra5OkaSXESTEpc6uEWPDW5gEIeFkSKDApK-JH3FKsYtzkIamPYbGD7EPhXA5nHAzLweJGlOHrtEK77FfdFWNVcIfNRWu5GVyfHMGfcDR1gH_0gcwM7DDquhLIvRrpm8M4w6U1sOxWv2iSnxKfAl1Wm8fYQyoT0dn-bDNlPn86qqQy3SE_B0cWIk6bne0KVyTeccYVRigKMYL0uW_HgWG06K8IO_JrOgwTAMyOhN9416Q0gdSne7uDhTwpG39puedTkd1MfGGUdW1mD8DKSE1lB4dYJ9mM_xYX5BLXP4NCn67GsVExU-U_jSpsm3BuIt5EtjtiU98-lfkYbnlzgpQW648fBRJQ3Qd6D-I9PsgjUeUk1UpDV31cmxoh2n7xSlEJx7tl_8bgBi4YRpcq0LUnQBivgo_JETyRXFL0LTwvg2iJUoXk4g93heYLmkZUfBpoQtqFE_iirb3zHQEAGR4F5ljo0KVDubsP2SiGHieqLynSl3cMVD09IzfSP0Z_y-KJbaPfRiy0vlN8B50zNAgoUq11CozUys7Q7985sc5lhZGWyBYCc2-FvP42ARZNCRXUy_f3673YPJt2E5lKDGen7KwVkgaQWF1QK-k0f8E7lSh4J2Cdnmz10Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=neSr7lUO0bss5hqV_mnBkQfdcw3smCYFKqKv10RnqVE3pEW5e3EQu1XteImYOeHjc23xFd5v8dRdFebmwTSkMSJGDMy60QG5kzAqtt0sv8ur0LsVT4cQFpr-83IYGINlCeS6TOSLzyWn3qabLtNAWlfSozYolnrFZE80Rt76l5EFQ9kSkEuFlaMAe4Mwj6jLaTWnIFEMlSIODRog3gZEgK71O8ggT9MXytsvDcLtlhxcbk1WglX3SmRJVuWsqsKRAYZXBteHvLXix0OTmCwrNd-e4aXXAbLYlyigMTmpZzVpSg-xXrcwcGK3w5alBWbnHNPOFp1O5gVmqcSUFFxYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=neSr7lUO0bss5hqV_mnBkQfdcw3smCYFKqKv10RnqVE3pEW5e3EQu1XteImYOeHjc23xFd5v8dRdFebmwTSkMSJGDMy60QG5kzAqtt0sv8ur0LsVT4cQFpr-83IYGINlCeS6TOSLzyWn3qabLtNAWlfSozYolnrFZE80Rt76l5EFQ9kSkEuFlaMAe4Mwj6jLaTWnIFEMlSIODRog3gZEgK71O8ggT9MXytsvDcLtlhxcbk1WglX3SmRJVuWsqsKRAYZXBteHvLXix0OTmCwrNd-e4aXXAbLYlyigMTmpZzVpSg-xXrcwcGK3w5alBWbnHNPOFp1O5gVmqcSUFFxYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=tUMXReSKukfGoFVL21oLNxgP0B1uWW7DBM_jbCehHIRoKl4T1f0SB5N2X9oz8ZCaV-PqUnapyw1AQQnHSuUuTbPx6Bk4whVMvvQWnX4TxCJxT86ZkE97zPnRYHT3PFgsSiaALGGNTvB0-6Gk2HxH8S997JlPs-xRwLAlrcjQ8DPf9vt1fGFqRrGsFSXnrmlZhh42VUP-T3Q1crZkxcTB4K25NrMZh-UMkr2xOWJLCDTIw0CCy1CjXwrrU-SSgbUl8cgDPlQWd9KMBGsfprW6nXr0QNKK0_PFMRPjiekEPkKtLMgYR0SmSwCvwyV0noh4oY7XG18wMIMkzx4_sBnI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=tUMXReSKukfGoFVL21oLNxgP0B1uWW7DBM_jbCehHIRoKl4T1f0SB5N2X9oz8ZCaV-PqUnapyw1AQQnHSuUuTbPx6Bk4whVMvvQWnX4TxCJxT86ZkE97zPnRYHT3PFgsSiaALGGNTvB0-6Gk2HxH8S997JlPs-xRwLAlrcjQ8DPf9vt1fGFqRrGsFSXnrmlZhh42VUP-T3Q1crZkxcTB4K25NrMZh-UMkr2xOWJLCDTIw0CCy1CjXwrrU-SSgbUl8cgDPlQWd9KMBGsfprW6nXr0QNKK0_PFMRPjiekEPkKtLMgYR0SmSwCvwyV0noh4oY7XG18wMIMkzx4_sBnI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSE6IIzfNzfo6leLFDoaUUbKY2phQ6O_zsIZqIQQbugG60XIx2d_fPYxXpO6gXyPJxkeGHDohYcrJJzTAiCMhOrkNiAAtqU3F3QeaX9V3OjL7GjVoDr0mbaJv0vAYaBaVo_itZr0GhscufbX2FCct21lF2iU6xbLgkwqZt6O1VEFbjIcm3CG8cXYLPk1C8fPJClcAd2hKzmOLU3VhRSuUtanNnNRP4xXWlRjSeyUXnzRk5Gw3aHxaXZjhHtoXgwpFEIWrfjw9nxRIwctiDvK06sffGNH8DscvlHR6b8McPL6_0J3ca9LLLS4Rr4xarHuM_i-qUjOF8SLkRCOu8jqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3CYmMUTgLJkeP_Ct9PQcOr6oSE0S7CDBN_oQ8ArlJ8A5YVHbGOIM5okPFtJNdM6Ptyk4grSws4au3hTuZd14NzYB80lj_t6rkXkqTO_XAq2R6Kr3tOmWelv4IQx00jEB-hCh-5RGaj2cL_E4ppFFKLpRNhmiKG8zwKcgdvoRF8hETarS3RANrTVGOqA4hoEwx0jxTLYP4ycSR2kl6WFATl7we3Zgdtw2yn0sT2eH_lDDC2WbMpch-ToFmEznU_txEBhcbiLJVoD2wKASMak3oftEd11gDPztqZ6boE2C-iAV2h_OteJUUorP3IzOyb-J_n8My_0bCYPmWj4obDrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-qPjVziPUQ3lPRnrB_tngLxhtP-gPe-wYf-XEHNeoNgrqVRuhO6yVRDVEQBLhSnQcVUN-B-vssdhbwW8pFQx0pAmFYybBJfZqHutgkQIQ2k6DoJAWve83lmeF_wnl7FJX0VSHj8nuPt8LOa6ZT_80IwHFJdZInxpvrgZmKAS7htDZ4VxvhrelqLrEDhnUBkcB0Fk76KlzsXm5Nz_yqHyNwREzLDOJZv1PGZvqQ-maCxO68rn29NVbFr82XduNc7WexUMMe6YDuZz7uF-YSa2jQ2u91_nBSjN7AmrrJWUpb_xcJ2USPoMlAfHtuCKQxe8_widxe1Iz2roZdiFTfCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkEyefNagd0kJ0n7k02Sp6BFLnowPMduf_pCoUulqhY0YnDsb8xorot4s-Rm1vhw70ARTgWWdAP5gy9isbu7rQsLxJRfskXm9tJTTY08Cx_JODacSldPuRsEQvOjJTsGzTh_DmooGWvgJ9Cut7r3-74CtaaIQfB4VWsf8rFzdHTMYq3y5nB4hnMo9Wm7qHE-8KZti7Ug9JLb3PU9hErYfu2fbEspheZPKiqMRy-Z_RS3dGf5IJMyCrMUpzDMEjV4H_LrmO8EQUxLWdl5poEMx2LSMcOLuRr7YL2VIt51KAPsqQTtjKBuQlZmb2QTeBZx5uzOEqtgHSVnGjVAQfNEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=FTrc_v0tooxTKGeMJU_87uZfdMI2lB_VNdtjbYKB3sgbg3-LInyR6YVLQ_IczlWwUmRYxem-Ku83_GRp5-ZAwq8A-ZyE5ZUhc2zr0A6qiwhmJnM_d_kDTlvTaFEVdNwwULTHFKRSxiU7LK8kcyUXkDDqUPwaZ7NOcKm8f0VyZQC2OgF2pclawcJe0nWqNIxvgjjmTtnjqPYIJ-qpMOecclzLTDxOFy6lSJ-YQH-V9DgpJubM-71fGeV3LA56I7oy3rxJ-FJlMXEGpGf4WHtXsP-1TGz7jkRtfkqMz6-B7YZybrFZCZPuAqU3Vq4chseP5_sF_WRzdYrr_S9-XpbzoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=FTrc_v0tooxTKGeMJU_87uZfdMI2lB_VNdtjbYKB3sgbg3-LInyR6YVLQ_IczlWwUmRYxem-Ku83_GRp5-ZAwq8A-ZyE5ZUhc2zr0A6qiwhmJnM_d_kDTlvTaFEVdNwwULTHFKRSxiU7LK8kcyUXkDDqUPwaZ7NOcKm8f0VyZQC2OgF2pclawcJe0nWqNIxvgjjmTtnjqPYIJ-qpMOecclzLTDxOFy6lSJ-YQH-V9DgpJubM-71fGeV3LA56I7oy3rxJ-FJlMXEGpGf4WHtXsP-1TGz7jkRtfkqMz6-B7YZybrFZCZPuAqU3Vq4chseP5_sF_WRzdYrr_S9-XpbzoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=ERVSWZnS0iCTdi73-UscSWDMPdTL0gcn0-ef1srfJSV7_F8xvVMFnbx1FZzQC1JnUSeUYPQFU12gXw1F1G-QuMgJ8DxN5p4YDiIwOEPdg_AyxW-2ugRkZz-I6k8XLnvgQfBWcLOwDeVSrC3tQlDDJ49sxm-2YUA7BwFf75eK74Q6fdVWoQivPozTTzI5rK8LPXFsrYRZ1G50CW22QgKMpnE_mluDktx_J-IULKZDvVPIzWApoM52xvovSZotFPKLlG7PRyk3od8yKrVLmJcOyBuP3AbsRwOM281Pn3MFxekpNZphW-AFF5RFlxzP9UfbcNgLElySfGkPS6oxNcQrhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=ERVSWZnS0iCTdi73-UscSWDMPdTL0gcn0-ef1srfJSV7_F8xvVMFnbx1FZzQC1JnUSeUYPQFU12gXw1F1G-QuMgJ8DxN5p4YDiIwOEPdg_AyxW-2ugRkZz-I6k8XLnvgQfBWcLOwDeVSrC3tQlDDJ49sxm-2YUA7BwFf75eK74Q6fdVWoQivPozTTzI5rK8LPXFsrYRZ1G50CW22QgKMpnE_mluDktx_J-IULKZDvVPIzWApoM52xvovSZotFPKLlG7PRyk3od8yKrVLmJcOyBuP3AbsRwOM281Pn3MFxekpNZphW-AFF5RFlxzP9UfbcNgLElySfGkPS6oxNcQrhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=dD_JB2TcDp_xKK_Vq2kVhWtKTCM3hl2JT0o41mFseNpyA-AAbqb67aSur2X2nG58A4mlISFVtsswO2TMUUvdi0o4UcCFzsntCz62IBs1V3rrdEMkIuvNGCm_1HIuT7OuzBv0MmTZeJ6XdYUkAKudYrkwPGex_M5_OiTXzBulSTzwru7BR8jgqLZg0Bo0FllEaIVAj6KIftxCIFP2PJgmKbSZhU-7P4zA4YMQrLsGU6eYa1xJWnk-pwVDeZGs672spHvv8KcDQLDSZTEnzVe-d3jbG5wMcChOtcB49dQcCQuIlMW3fgjz22BWsYxyiej6CcpHW6jtB1QJA32R9eWfQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=dD_JB2TcDp_xKK_Vq2kVhWtKTCM3hl2JT0o41mFseNpyA-AAbqb67aSur2X2nG58A4mlISFVtsswO2TMUUvdi0o4UcCFzsntCz62IBs1V3rrdEMkIuvNGCm_1HIuT7OuzBv0MmTZeJ6XdYUkAKudYrkwPGex_M5_OiTXzBulSTzwru7BR8jgqLZg0Bo0FllEaIVAj6KIftxCIFP2PJgmKbSZhU-7P4zA4YMQrLsGU6eYa1xJWnk-pwVDeZGs672spHvv8KcDQLDSZTEnzVe-d3jbG5wMcChOtcB49dQcCQuIlMW3fgjz22BWsYxyiej6CcpHW6jtB1QJA32R9eWfQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se0Jp_BZ9FmpzRP2-D4YiES-Xm4zizUQtZpIMVfByk8J3pj1Cd6RtE8acfl0UKE0C_9uA3XzARGEWmYBWpqESsdE5j_u-z3o_XcorfNoXSj-DZKFBpOK2pAVguVcy9Ayeye1L6Q1xzq5v9uNudyxsy8dR7dtjATj0ohadSyuJVnLhyQTnPmbJIUmDIHo6BpgFmaU-cBVvy9awmTgBLlx7bQPvbkOaMm3M84577d00MpZgnG4NJexJWaiJiHpxA3C996etVEiSL9RkGZJBZMxKAFYUmWHwKavArRkXdkyFu8HE3KF6zJAJgFR1vdBI59AkFKorA45cy1wzQP9i_c40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=LkHnYoyn5QgZcw_-3ovn6GCnq8Ut8Qp8MD83y92biRF4hAZrO8i4DPLsHQ_nzud2ckwrLUgLMfViW8W5w4ynyVhcYQKHXruw7iKcuLp3NXxWyUpLZiWqPpk5BWEDiwT5uIKk0WoqQNEewLRDdNssstdz1l0FmiePWJAJQNVQMhKSlp3OZ3V5LhbYDBZjW1hjVeeZ8kDB69zCqJa_43BLa-vq4jEjvZLx0UF3HVF-fYvF4OKh5v8C8vE9MgfmtGUqu2iTqihQfXpGLKI4Tco-wVRpQ2SltzIntrJ6O0C6Hj_R0THTeavas4F7RcxOh8-aOze4yA1cmTzf2D_3r-6ZXW3YOuz_NfbIPOkoQiLikWmlurUTl9W-Fv302HatI93Yj4L4kGDh-Q22Btg40KMgHCOUaaxd0qOBBXOT9dkGdOXWvGNO4tY2-JNzVW_EE-SE0cimq_JfWy-GBl60nEAX5MziYyogapnY1G5b1i29BFu7RlUqBA58VcchRZq90CJwqjwy60qC66dRO8RuhNBMvxhm5BY8-CSXisrRsL-3vcy_z1T19YZy2Gk7wuy4N2MXQt-nR7KVDhKVd-1ID7m5jhm8ekuAlTZpz3Nw7Gxlsfml0JXKSQa59776bI1itufyS9n30X-dClpCNV2tsbnGp8FEVDwjcBgbhvGMhC2cwpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=LkHnYoyn5QgZcw_-3ovn6GCnq8Ut8Qp8MD83y92biRF4hAZrO8i4DPLsHQ_nzud2ckwrLUgLMfViW8W5w4ynyVhcYQKHXruw7iKcuLp3NXxWyUpLZiWqPpk5BWEDiwT5uIKk0WoqQNEewLRDdNssstdz1l0FmiePWJAJQNVQMhKSlp3OZ3V5LhbYDBZjW1hjVeeZ8kDB69zCqJa_43BLa-vq4jEjvZLx0UF3HVF-fYvF4OKh5v8C8vE9MgfmtGUqu2iTqihQfXpGLKI4Tco-wVRpQ2SltzIntrJ6O0C6Hj_R0THTeavas4F7RcxOh8-aOze4yA1cmTzf2D_3r-6ZXW3YOuz_NfbIPOkoQiLikWmlurUTl9W-Fv302HatI93Yj4L4kGDh-Q22Btg40KMgHCOUaaxd0qOBBXOT9dkGdOXWvGNO4tY2-JNzVW_EE-SE0cimq_JfWy-GBl60nEAX5MziYyogapnY1G5b1i29BFu7RlUqBA58VcchRZq90CJwqjwy60qC66dRO8RuhNBMvxhm5BY8-CSXisrRsL-3vcy_z1T19YZy2Gk7wuy4N2MXQt-nR7KVDhKVd-1ID7m5jhm8ekuAlTZpz3Nw7Gxlsfml0JXKSQa59776bI1itufyS9n30X-dClpCNV2tsbnGp8FEVDwjcBgbhvGMhC2cwpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFz2Dw8LYdzSaDugUlzrDj4aECjNmH4c-781vh3kkMvlqMeS__75oxAVDPcPYWh0N4rBeHywxnL0ofwzESWq6FfckUOXs5w7v1Fv7HuSghz683dMcVEdkZOAdhJCug4plqNqrks-Mnp5yFAC0rs3Tgemwi85QX_4elDOZ0UMx33fmkS93dBT2K23eUvaEmZnX846bPeGDtwRFgejoSMDupFaPasSXzOwasb2Br_55d3UP8yn6EnIW-kXANqPkP0z50D7-e3keq3qJDIb7nZJjUhXXw8ZXuurhvk0NLnsOtiq1VoZymqGZrK1M0ey0NsXfZ91JVJqYDnKPt_8j8NsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=niuQJ7MWmscDFYxohfJnLFpWUkcIiMu16rmHsRnCL10_YnmuFTGSVylWH-vk3XHIMWfMl6tNhDw4NVnFiLebDzgsEI-15uRjEZfVhnEJeECJHzmiUYukvvZ7SZ-bsvNcU-5ueKj0oy9_4ttLAuxQF2cjXjqTdZ3bHrNM2qC1dUTLnyaVnePHC5UyM3Z844ILApa221cn4OvezyvaemL7XzGzw2J_2ARjTX9341gHK8Se7lSr6PHGstsBy5JpYKExnukydKzGDPBb_70T93JiQNJnBcgjFh7GBDfAoOhOldtzfbzqgOUAW43mtl2PNdnI-RLZ1ZA-iYJJ50awHj9Eug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=niuQJ7MWmscDFYxohfJnLFpWUkcIiMu16rmHsRnCL10_YnmuFTGSVylWH-vk3XHIMWfMl6tNhDw4NVnFiLebDzgsEI-15uRjEZfVhnEJeECJHzmiUYukvvZ7SZ-bsvNcU-5ueKj0oy9_4ttLAuxQF2cjXjqTdZ3bHrNM2qC1dUTLnyaVnePHC5UyM3Z844ILApa221cn4OvezyvaemL7XzGzw2J_2ARjTX9341gHK8Se7lSr6PHGstsBy5JpYKExnukydKzGDPBb_70T93JiQNJnBcgjFh7GBDfAoOhOldtzfbzqgOUAW43mtl2PNdnI-RLZ1ZA-iYJJ50awHj9Eug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBBVBr7pehkuHfBntN6Cf3uOa9XmiEBH9gCA7McNOEPU0flqxBR88erj0B0WSuSsiH-MjMCuga8KUxjtN-pD8KO3C8vbxHn4y4a4LI2pVpOounlo-2MzoDbjO_4WttK4gCQw3kL7i4nEo1xDGQKdpHYMmHPHK5eY4I9vSIFKL355gTgFvxCTwi-RvisZUCVlB7D__LwJb9NWWHQx8ZBvxlcUwzE5ZKML-PFJrHzMNFCZeqyVrI3bJ5m4W4wPIqbLfehAxI-l2a0cfngCgyCkYKTJtsABv_FMYTBOvD-nwIWLMaT2cjGqsgRLOgVx7lBGrNLKATBJZjLGuy15RnFCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIcqPGj-aCSTfq7pLBgh5dntKN8sm0jHKlAMjoyGKsAjQhQDoze7QnSUO6TQbaq_Ynunz9EGIhyna0sKpvN9eqRG8bg6ozCzYxDnacn2Z3_WOM654o9NcIoKtkXXlwJq3JrG3lENQajQxNAZrS2s4krzvsoqVmhfjT4zXnUkrhxq6ZMFlPqWh5PwOcqWQwfK3-FN870D-tD660iLmEpa_slvkWhbnI6BA_FUaBjHFiJtZiyDbeqiy3KCLezpmoyYUogiptZIdTSd6D9933Ux_9nvVRt-0dTzi-lcrWU4mPhiTbJZnpOnB5PR3NPb8BnB5fi7T9LpYwzXA8WH6lxAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ridyQfrhsInQTZafCeiOHrLG3H2Oadj7Ql01cK84o1s8fv5ANRyFBAlQYsEaXqMk4dWbV_q--W8BSVjDyDjU3AIdutstHREW1y1pCDMK1bFuz3SrwoTVV_h8VT_D6ufDUSyznLPcj341zgVzbT3SeHfYxaSf0kqw2zZ-gH9S-8RRoobcv2u_6xdQ5POPNZOO7g72kM2m-6TKv53V1GE1o-xwO7POENdrOS8tPLZ5c5c57zjJ7v-BKMMhaWHAmnobhU7nM32FEmgNic3KgHK-9T6Lnwgd5tznGqjD42sg5zPRz1G_a50IZl1aSvF8DENU6XKdFpwtyjr7TyMN14LdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=RFQ7PkzFukVZgOm7iP3bbnT24syThewG4MsuaywxYkF-QBHYHuztNHxjPQAxt3CYnfz0_Z2TnERFiVTXu7MxhfE_3Jt0OhUbpgRMw3kGqB93vCICme2nWjsYoX1WSRbnc_DrX7Lgogt5_6nPzmfDIOoRr0fU6sYFqrD48gbONBgZ2v7h6HBWD-_cPp_qvTJCBYMQOvQo3rT_pnTo8XbhKGf4UQxQyyeHLp8dGoiUq8-QfjYkPuRyyiF1rYwiRoEuXEKGHCrk8jKrFr2SlMYyWRDIBYpuYmiW9hwdjNvumgBLCC1uKooOZxM6OY74pC7_v9bgCbM_RZ0wDx-nDErSdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=RFQ7PkzFukVZgOm7iP3bbnT24syThewG4MsuaywxYkF-QBHYHuztNHxjPQAxt3CYnfz0_Z2TnERFiVTXu7MxhfE_3Jt0OhUbpgRMw3kGqB93vCICme2nWjsYoX1WSRbnc_DrX7Lgogt5_6nPzmfDIOoRr0fU6sYFqrD48gbONBgZ2v7h6HBWD-_cPp_qvTJCBYMQOvQo3rT_pnTo8XbhKGf4UQxQyyeHLp8dGoiUq8-QfjYkPuRyyiF1rYwiRoEuXEKGHCrk8jKrFr2SlMYyWRDIBYpuYmiW9hwdjNvumgBLCC1uKooOZxM6OY74pC7_v9bgCbM_RZ0wDx-nDErSdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2NT3cN782BX-KJfBtIhRIJ9Kb6otm6DfBoUWGARAGQJuAz2huv3eO9Jg0QLEruxZygyhNXr9nCYfct49B20WlVUO5DZLxQqPwK1sBa5lonA38g0UtCCa5Y3pcMKeI41aljWMDdUNOwawWO7gAz0dE8s09S3O8d1p2cZTkDgbfffjimgN8tM357fjbc-ZIiHhXLYqm-0oWaXfdJ7v_Th4a1edjgkIEPQ-Bk6LU56TsT6vlMq9cf9DFPoDPOonvSa6Y6x0dccfAGxZ-oOEuiQT9xT9XvwmfNaKWOmn3aRo_TRijRghmjVPbcfNNSmYPWlcqo3TpuSqR1MRJtYRA571g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y26GZQA57685tGLkQDs4JpU9p45HdSHtPerEeYt0VL5wtmFSIEvaDf7vsjzNETksWIKFLfUBNBG_535MaBFXfNXLkgZUSUHsU4Lo1gBuipWcb5FsoYpnewbP3Dw7gZKzP7XQGdg5IGM0UGVBOBtK8cPZ2bbvP6zM0jBfbtgN-F6yWG6smPbb0FfbwXY400OH00-39uUh3PUbbPYbRDSad48C8fCQLfjlCWwNHCJLyQSny7iV-ULShrSM1tAr022rpPZtLb7dakj_rQVzZlXH7jbnZaCI3bU0rryiIIUBX9ZQiFNPOy6LA2GdD0hFKfYU3AjTolRCoepkipHl0Zme9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFH0KhcWqjT365c3F5xb7HlvlWQoZk1hyoN48wtCRB6LG1wGO90_dEy1KzPbbbPyWH3afpyjFgpSnS936-IUz9MJMQl0rNrNFXx4_Ly-GqB334uCbm6NBrWOso0XZzd3V1O8PE8qPn9oZx1ZDzNI45xAA4d99kH4bV-1kXZKYEHvT7anXHywJ-cxMrb6ourJg3i0XXXAN321OhC7z3S23dRL3WMLOKAdfhWoV42PCkx4QFxBeNhexERRPQrn6KpOAbewKMFi0xyiHULT-Lv6grPa7MwmwwwOvjlskKIDxtERj9d6O4M4lLc3vZkl3_9VhlRIz3TtjKPl1KEdODDskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9mVYMfAF1O-DVSd_DXJoTtlD-7pK9SqCvEoD9tVSyevukt3HInnqFHVgk3MxVJw7EUJeK-xBifRM5a1b-5UdNQOH1bEHwudI3bLaFZSU_kHGL6rj0zlLomXN_xfzTVVjvY02Wt252HFQj5scFx3nG1NSFsKCr2oTI9lZfrRyWVRJ4cHYxOmHCUkTST1EqopuC_V1EmGuevOLIMDvjF0wuhBkqG2GdA6wWWcmp4p1T9fYb3WcJBnlIszNXbA9U_iHEzlQQ-SxyY7TU5Vw8uaAqFes6paSM1WmXUp8f5BDjAXJ_a37AmPx3TIzQTPFuwMBPi_8aJLSeEH90iac2Gcqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=DeGIQ6WBRNt7Kdpoh8DlP2-5SFmM1lA4mZMsm4Pw3yNUnFhYHnFQOl6d83cW1I5IlhuVlqhsTRr28Ru4e502fiPX43uqkQy0ZSgGd7NcaFTx1H33OW7r5rUaY8uOK2elNdElmRoktext4U9My6putJzgkY0EEHEVu3M7Fjexf06DOIzblmECuLnlJR-N2sxO2asPsgHWN4IXWJCaewBtpN6lmATyhD3CmMHuYSX1HPjcpbzwOpURq-ozhjBPc1X44KwePWADOs-2DWha0Ap2rtPbua_f-rHcRBUYlx0NnaJ8YrGYu71RdbzqvPRcbkojUKEcTr3mz_r6uAIyy2IMJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=DeGIQ6WBRNt7Kdpoh8DlP2-5SFmM1lA4mZMsm4Pw3yNUnFhYHnFQOl6d83cW1I5IlhuVlqhsTRr28Ru4e502fiPX43uqkQy0ZSgGd7NcaFTx1H33OW7r5rUaY8uOK2elNdElmRoktext4U9My6putJzgkY0EEHEVu3M7Fjexf06DOIzblmECuLnlJR-N2sxO2asPsgHWN4IXWJCaewBtpN6lmATyhD3CmMHuYSX1HPjcpbzwOpURq-ozhjBPc1X44KwePWADOs-2DWha0Ap2rtPbua_f-rHcRBUYlx0NnaJ8YrGYu71RdbzqvPRcbkojUKEcTr3mz_r6uAIyy2IMJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NobjlXxmj4De6_bECMnWHFvaGlS9_jDRFhBR6U2Z6RGuVFILDeIUqQzWAwaLORF6xdew0-cpj5h9YWesFcRCu2bHbJQEFdhOp1eEaeJxVM7Nop9UANRjJhHThuK-TYene-W1xpOgDzUR2C4389iRqL6hriteVCZTCyDqQba5cJAIFWAIwS8p1-bc6ytfrymjVqFDIcEm9qhjkQyHoiGTDiTUC2l0DQgAY7IKuCJYGjHvuojLVyWS3EDGarKQg3Eo5v8c4mAHd3gATk5JPRS4kDgTUJgTpBMr-ahNsoO5wg4XMQEwcysl__atbF0kom0ddxNJBH_YpXGJYhcQi4sblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=EWfZR95JHDWEjW3aP8imLbRMOW5NWRQgUPohG8SjcfUpFGSvE_Q7h7Ho8FITYHEmOACs0i3LP_xMGvAmUL2mTuLOejvKXeVozkoG26jqU2sydXcdTId7NuuVzh28DzfxGavkKXM3_SvmxR0W3q3JTVrdvnXhHISfqn-9k8Qv9u9Du-WhsJP7Ew7Jug-jhBLUhxef69eqdMK02LWkYMCW9Y9u5_A9j903fjAi3W0k8KODlRaLfiYKY8T23ex9AUnXhN8OkiLQvjF8xh8BjMuO9m5RMgLmL64xl1ELmZlN-he0Z_OcOv2VKiGhaZ9r_n0BWDfL7BMEjW0oKEh-iSRrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=EWfZR95JHDWEjW3aP8imLbRMOW5NWRQgUPohG8SjcfUpFGSvE_Q7h7Ho8FITYHEmOACs0i3LP_xMGvAmUL2mTuLOejvKXeVozkoG26jqU2sydXcdTId7NuuVzh28DzfxGavkKXM3_SvmxR0W3q3JTVrdvnXhHISfqn-9k8Qv9u9Du-WhsJP7Ew7Jug-jhBLUhxef69eqdMK02LWkYMCW9Y9u5_A9j903fjAi3W0k8KODlRaLfiYKY8T23ex9AUnXhN8OkiLQvjF8xh8BjMuO9m5RMgLmL64xl1ELmZlN-he0Z_OcOv2VKiGhaZ9r_n0BWDfL7BMEjW0oKEh-iSRrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTaoWS7kXmm2yLkeXFa7RYDg8aFrkV0eK_IidF4TfKZZJ-J2vSnfmFK5DOe9uAXk4G91f2MuU5y7iw2-r0JyGj4HllcLAF2P1R_Nf0U2LGgt_zrSNiDmUD4Z1bZy-tQWGgyS92ftXpjNGaBm811O6yK8FDzidp3pgYBDeJmvR1mrEavulI1eX8kujTDT6lOTrb6XxsHP4HeRfY22wCJEMu8V-pcZFE8vC-vGwFdCT15RA-3lVyaskosXU2Mm5BXklhsHGzSUa_us-gNrzLVUDwAJTfCUSGW2T6kEEZbKzMoZed8cs5_GdxZcNDFPiQPH4UfjVJF8FWTgBbgQzVYXSfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTaoWS7kXmm2yLkeXFa7RYDg8aFrkV0eK_IidF4TfKZZJ-J2vSnfmFK5DOe9uAXk4G91f2MuU5y7iw2-r0JyGj4HllcLAF2P1R_Nf0U2LGgt_zrSNiDmUD4Z1bZy-tQWGgyS92ftXpjNGaBm811O6yK8FDzidp3pgYBDeJmvR1mrEavulI1eX8kujTDT6lOTrb6XxsHP4HeRfY22wCJEMu8V-pcZFE8vC-vGwFdCT15RA-3lVyaskosXU2Mm5BXklhsHGzSUa_us-gNrzLVUDwAJTfCUSGW2T6kEEZbKzMoZed8cs5_GdxZcNDFPiQPH4UfjVJF8FWTgBbgQzVYXSfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=NKucYI0Ems5K0E69gj8UeiavnQ0t1CtZDKyfC3z04-xVXp8bCkAAjlAdu13IjS5WzlvV2zNIt2VZINGxZMkiJhOSpLkOZ7Y8p2xxAVgGxP_h2GvWw6w5LdG2ScwnX71qguyq66GBlekKFJjLFYdx_3nGzU9ZZNC9dRCQ-2Yj7fmZW1j4-_3qhAlp_nTUM_z6lHhmqrKpEv9hujyWvpe9Gbc5G5NsKB3eVWKkdaHINIa_Ant3OVo5czYd2msfAiH31_fcRyjBGWQfi4BHjz7KEkLU1kVyIFXz0dFa5l3BWdJDTqn9BfFizyiQjNF4aCMbDznyu4z-MpOdYPF1vHGUg1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=NKucYI0Ems5K0E69gj8UeiavnQ0t1CtZDKyfC3z04-xVXp8bCkAAjlAdu13IjS5WzlvV2zNIt2VZINGxZMkiJhOSpLkOZ7Y8p2xxAVgGxP_h2GvWw6w5LdG2ScwnX71qguyq66GBlekKFJjLFYdx_3nGzU9ZZNC9dRCQ-2Yj7fmZW1j4-_3qhAlp_nTUM_z6lHhmqrKpEv9hujyWvpe9Gbc5G5NsKB3eVWKkdaHINIa_Ant3OVo5czYd2msfAiH31_fcRyjBGWQfi4BHjz7KEkLU1kVyIFXz0dFa5l3BWdJDTqn9BfFizyiQjNF4aCMbDznyu4z-MpOdYPF1vHGUg1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=BgYdgBWPTTHPVbrKTQuthVvVkXl44jk2WozBxezEfkKtULxAo5SOkQ8LFW0iTBfNudog94yLU9p1hrwvQLuRxyZ34B1aKRgecT78WJt7byrmgi9yCubHGhUx_pnA6TMohowdMoODaVL3ASzWPPlkTL-OlLojASEHER4xpQqFnnIBKdZ1fD9ABmbWVke5aikMEen5m4ClIwQVeHE_hQ6wukI0k76YQrYDeQ3O7tnVmzyfMSboSxekNPZA5jKsOxCdRWWiJenQ4c-64lkv8WcxhTeHS2miFevSUdSQUS9PW5VwzCuZxVZMRzSBHZC2muWfUj7dCv_wzAbaJ7s-EJ3b7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=BgYdgBWPTTHPVbrKTQuthVvVkXl44jk2WozBxezEfkKtULxAo5SOkQ8LFW0iTBfNudog94yLU9p1hrwvQLuRxyZ34B1aKRgecT78WJt7byrmgi9yCubHGhUx_pnA6TMohowdMoODaVL3ASzWPPlkTL-OlLojASEHER4xpQqFnnIBKdZ1fD9ABmbWVke5aikMEen5m4ClIwQVeHE_hQ6wukI0k76YQrYDeQ3O7tnVmzyfMSboSxekNPZA5jKsOxCdRWWiJenQ4c-64lkv8WcxhTeHS2miFevSUdSQUS9PW5VwzCuZxVZMRzSBHZC2muWfUj7dCv_wzAbaJ7s-EJ3b7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5RjOcgrtPY7zKbTT37lV6QGjM6KLYBdUxcvfuid9IH0sucUtlobOaBefI_fDxyJ_BsyK4X1e4iSBhj-MESfr0XzuJZGup9giBk-_1A3MAq7ES8fhjPfSKVX4QNLInWtrxfnRjwlOR6dcAweTRYiBo08THRDPJuOlrTK_FYVsPZVhVh36QgrIAzamGCJyRMJF5DYpCgREumTBZsf8J6UrYAvV09ebmC4w6j6mvnnLZdEfroC5m4lXOGUBqHFimwtrHdY0OJXyxBdeBQdPXAvLOEVYt6k-BEfnd34BIPylY6V7DSZ1PgbU2ocpYVzKzZ94TTTKUH5XnBxlGbPjrV6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Rb7ChPXs_1yfaykKzBk9yBJe7M6JEs9De9GZdjcaejfEARAqY54eRyoBPn9FqNYIBdiEwdzhd5ZzjP0Hz4d4MNHBidswPgYBR386RqnajPFnwXYU34sHhkLgWaaXhc8x0YSBDh2580hE2SrWOlLemiQcQDpaeldvnr_CEvuexzL2wiah3i_ERQpYK6oROg4dORZ-ZTtsLhns1s-PdbtCZtWNN3Xyk5Sbje-qtIoNIYnicGc5ZdDtGlGKMCygFF3BqNZa3V7xPh3KVx1NUj66F4XcJmNbKA2WeIEJW9lfW7RY4lpyi7Ey7YNPc6NewsUPmTOKCNmJCWS3M1cFamdMAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Rb7ChPXs_1yfaykKzBk9yBJe7M6JEs9De9GZdjcaejfEARAqY54eRyoBPn9FqNYIBdiEwdzhd5ZzjP0Hz4d4MNHBidswPgYBR386RqnajPFnwXYU34sHhkLgWaaXhc8x0YSBDh2580hE2SrWOlLemiQcQDpaeldvnr_CEvuexzL2wiah3i_ERQpYK6oROg4dORZ-ZTtsLhns1s-PdbtCZtWNN3Xyk5Sbje-qtIoNIYnicGc5ZdDtGlGKMCygFF3BqNZa3V7xPh3KVx1NUj66F4XcJmNbKA2WeIEJW9lfW7RY4lpyi7Ey7YNPc6NewsUPmTOKCNmJCWS3M1cFamdMAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=qZQ4XDOaqbo5xQFTEEE6NYmZp7Y17QwBaE4vmILKrNke75AvyHixXyHqtKMiXAwBB4etNLzMRe4QV0oL0N2qPpZsNk4eyDsVMRJItwyIX1C6vH9aQh5vi30S3xi6gJk8xkHryt01ufZw07CeM0D0Yga4P-Y-8is9RCxTfMFqaQZl0dsbIbKVnQqTM6G-O6iMNpD10JRNv46iFQjh4R4XCvg8tUO7nOFOOPCUuSc1YZxBAo6VCJltnhwJr_K1dyiYFT3ZUwj1Wfm9PSRrwWwa3V18f1GilLepF4QSRxwAMJoMeZEaHRBRCXiAhWqvSznV18VRaAwnZBc6W9cg0sv5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=qZQ4XDOaqbo5xQFTEEE6NYmZp7Y17QwBaE4vmILKrNke75AvyHixXyHqtKMiXAwBB4etNLzMRe4QV0oL0N2qPpZsNk4eyDsVMRJItwyIX1C6vH9aQh5vi30S3xi6gJk8xkHryt01ufZw07CeM0D0Yga4P-Y-8is9RCxTfMFqaQZl0dsbIbKVnQqTM6G-O6iMNpD10JRNv46iFQjh4R4XCvg8tUO7nOFOOPCUuSc1YZxBAo6VCJltnhwJr_K1dyiYFT3ZUwj1Wfm9PSRrwWwa3V18f1GilLepF4QSRxwAMJoMeZEaHRBRCXiAhWqvSznV18VRaAwnZBc6W9cg0sv5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=h-4u00pkKAXCsbWImYiJrjQ068Hfwd2jI_UyBNIzG-o0otLPeYXzljQ3dHHkOLzdWjbZbz_2w9btoM3vGUjf3KyRpKAAsr6urijUbq7-wnTTgnaoHKsnvCNT4W7KRP8H0hvIyFDOjF4A1tCxzSc1nv28JICB7py5fUurEyB9hlwkyEVEAEAn-GekzHrFPzniu8N-72k1Jd317SMwDXNRykud5nH0mWEWt_gOBJa3st_BItODvUn1V4PhR9wSVubdplW2qVcD-jWcNSHbBIPpUFoC5Ts8BdWCY9hkvbd1AkKaU6-1rR5x8DlSgwyJtwIWOk03ZT0hWim_J0WAb6T_jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=h-4u00pkKAXCsbWImYiJrjQ068Hfwd2jI_UyBNIzG-o0otLPeYXzljQ3dHHkOLzdWjbZbz_2w9btoM3vGUjf3KyRpKAAsr6urijUbq7-wnTTgnaoHKsnvCNT4W7KRP8H0hvIyFDOjF4A1tCxzSc1nv28JICB7py5fUurEyB9hlwkyEVEAEAn-GekzHrFPzniu8N-72k1Jd317SMwDXNRykud5nH0mWEWt_gOBJa3st_BItODvUn1V4PhR9wSVubdplW2qVcD-jWcNSHbBIPpUFoC5Ts8BdWCY9hkvbd1AkKaU6-1rR5x8DlSgwyJtwIWOk03ZT0hWim_J0WAb6T_jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2DPUsRq71r30mocYne6FCL9ui4k-5jjJ_9-KP7zrr1unGTUsiOqAatkbUDvKCIPStHNIkTVF8ndYZ94jVKtPn-HnJP3R1jT56JzVWe_Emofj-mRFsTJjr2JF3sQ4pDz-A-WoDFcKcjkihCaf5i--kxBprOlK-yU84GC2RFguH6xhwo8b2vw4NSI6-KRztKN81cQ5VaqRg1HyPaKfH5QQQa6fP8HsqDeCe3Nd19mMWdml9HYVE-wSxRxqZmQrFubRWcI0T9yGjvmUr2WtZN5tvJwATKSb_2LXG_Wsq4KUvDuKSAlUQXsrdFSeDrmlZmJWgTOTgZucPAMNRzF5ocvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEmsJhIJmQ19hYeTPQTHZ-X58wGcyM71aOlHPQB-lj9GuaqesIQhkbq_5coDzMAnyal486kCsv3INFPDQPhkBHJX9VzmQFdpJtBytwVGk10ABDrI19Wf2eTFrMHNnVwWM0QvAhbmy7FQPeh1ocnUYVrw8FXYPBz2W7i7UNe4iVBTdDcSGOqahM7AXQoAAMgXllk7_ZAeU-rhRLhAg_W0WdwTtR_IDQFaR8aiKy3CfN_qB49E2fjlBCJmdDnxdJUgFhbQvGcl53ym8ebaxOe5UqJUgliSThYEB2Jqv8fGEgZxS89DJkVmDbBjjC9G8HXF0WAbxRQC8TDaWPX44smKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCxAJUywz6dt7CaLfK9nXIHeyUuRoYXZjowiXQKSaVLMnLDUY9Zd900y0qvIMDE-n-Wf2flboMVK06gGc_rSKKq_Gu-7avwmwHeugig3VFYEpKvPr4Bz0CFd_XSNByZPOdlWgYk0xus8QLaTGbJavTxDcMovUqBQOujGPhdxQK7F9g_wfBDkJz4Zv0H4hdwJJr1Jq6PQ0pKC3lrdd07eSzIY6F1_7TuSOw0oMuhu8A8bw8AHDYC3rp9VQmGrOwErU6PJPPat_heAZkHtj6kantndAhRNgIbk3ki4OsbL1KBWuuHVEhpyfHpKKXGbYdDmTXZt3d8uLF9u4YbtzU3ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hexg6RE15Or6bOEOW7zVO5NBcNKyMp1hzH9f5SNNPhrq7hMJTFrSajG3bC2PwR9LZayhF2tNr2hCbAw7ImX074ZpIMf4ZOWKrOpm2joidsAeQlUeUetdTJ7as1PnK5Hk28vswfn2HFTdDJLvMDG1XwpL1Qmjf2sMVhMou8lPkSPSRXFv5Jx1C3uhn2NztD08FA9yYLsjjgDQj2ifCaJy31Pyh6ywdMa-xFlrT1T3Ul1Q8mBCu7VK5OEDPkpXvsdaJqNTWKke1nqVzjGtA5aieyi7GuvmHCJz-EVIqJYbVL844heCHrcfN_9pSv5FNxM11IpN9FnUtdNTLwAERD5T2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWKnYQU9hiAS7OmkRuV31Da1h6fptgSlG08vZSZDT-mWvpFkQ1RTWYux0nSil_R5MYC_uIfJ8GJwcuHmNZFspwlO2fwakOj1ljomihElaDrf2rj5idkyRLzu0LezXtsBOqnD1CknrgtvrxGC9nJ0NwQ9WVe7L6fHi3ZE-Pee7Gwtj-kG18YYP-2bYnwoUsZk_XAPbERlZr-lNEQW3xPWQJhXzRXVMiV4PTQcvzt_ROmemRdDvxw-nqh8NjgQDWom3P1Ov73-MtcjwcF12foiIc_vZdmJuo_RTSWzS-rKQUxCMT94KSGnB_aJ18sOLJ_CTizlQBGvrZxbVE4M5sgcLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=F3ONQz8ZpteWR9eIC02-99yUmXDeM7QewxI-MZtBms0SPNl-B5I4iHrr449m3fPcx6CjYpsmux0k59b4KGFy9h6upjMCyckhKgwI3MlhYZad1esMUU5ocOW0bdAiZAbOEvKUvJqb4USDNuYtkjQalMsYrPjiYjk14yLcDg1UOeFAPzVviUfC49ciELeQZ19Rao23x-Cerc7VTDBXrZ8xyNY_cm-XLFhJq78puUMoeYg8WoQjNTrfw1M67d3hDiBbS3-Y9YBDc3NML65wAANLn3KVV6WLCrgmoOEOJH5CdVXx9bYl5gq25LodJLGO1rebd3lvAsmadJCotjaOrowvnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=F3ONQz8ZpteWR9eIC02-99yUmXDeM7QewxI-MZtBms0SPNl-B5I4iHrr449m3fPcx6CjYpsmux0k59b4KGFy9h6upjMCyckhKgwI3MlhYZad1esMUU5ocOW0bdAiZAbOEvKUvJqb4USDNuYtkjQalMsYrPjiYjk14yLcDg1UOeFAPzVviUfC49ciELeQZ19Rao23x-Cerc7VTDBXrZ8xyNY_cm-XLFhJq78puUMoeYg8WoQjNTrfw1M67d3hDiBbS3-Y9YBDc3NML65wAANLn3KVV6WLCrgmoOEOJH5CdVXx9bYl5gq25LodJLGO1rebd3lvAsmadJCotjaOrowvnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXP5d5LUEk2vFu_mrrjJNOvy9Jvk0irNCgXMP7ERYQFVurWLsiVwSuNka8FmmbLS03TGv4NyilT4D1DRVnqJZNsTQ_Z9tesny-a5dbZs1nRQMNLJL0UGY1DwnPr9SNyTmt2zi7pK-St2snVVwDmLTLvhHWVdtuZW06t1qQBinTwEPsLQnbDjThCQAfLIn65AVK82Lz-iZq-52qZqQD7BJ8GWRVx3gV_N6iTyYBjjmcl4MJLAN9ckP9r-FxAeJn9g7y6B851vTpezGppWKkjnGYmyr7DtIsmchkesJw3A5WHVu-A1weDbklasqMjVftY8U5PR8GScUUfp0n4P1AL5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-BRJkmjns_xpvO1w48hpt7rMFR9PCE5uq_CXrFcAztZmGJ_jG0vbL3MwSc9uWPF3IDkWBdaLG4xKJjuUK8BJfwD38iI4dz-gJO-XvwKLgA2m9mC27CsKyIGBNDLN4oWHGklqIbFAgXwYAqjx3_iXMvdoxutRsMK3PKlAOOZ7QxKGv8XvQs6FVbx_TP21Bkno2h2X73QGqm6rBIGYXaWv90jqqOJZbk9xk4VpTtqwbnFF_l8rmFjW7q4Q6OV6sLqfHMslntE_B0K9Wte9qvkEdH-kpT2limi6E4bZr4ZqlMzxzTNsbE4fV_9PsHnOCPE2fHXaPupZTRxMHNZYqc0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6B2VJKxTjpQ6COvWDbThYQ-AKqweGKYWgS3MhLMKYYAMHnAP4QHwffKZ5fvxKNTvcp1gGbYm9tSMJozBceoJksPgr4yMgeTvijGZXj-gjmacZmdUKUorJwhT42yP7fgF3GJ1Px6MnEcF9ISILIZN7RBJ84virzQ33Wa99U2CdlF5DoiAoc3nC1641AxJzh_BrvfR-s5BmEiIqd8panGcvjNeTAEMleB7dXjg4lVVopORvbPJMd6hloH2PFhrL0d07D1gdwY-pU-GagE47TXGNI6w42Hbg-KQFgLEUPSS7WIP5GJ-dfuWz2S3-uADfpoX9j940euunNxbiACHN2s9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=GVPC31tjmT1QA11ES_W80M3ypAezOvQfhDA8b2-WR6_JOECPR96jHLgymAnzLtqbivdPbh9l5epjHXw-EHfiyakRv8WLDaTgdaVFBKM-frQGj02K7sRxnL14V6KapnF4-2PkbBJnKk1rDGnmeRdLRWW5yVHraDlKSME4Rr1LHRuTHdcgXL_hX1oCCgctWzQ55H1CzSEs-ssu_VLnE1Shs3qjcjOdls3s7MwHNovfhstInsAdoS-gbwbzJQW2SjAV1Gal4K6WF7fd4HFKoOBELaLvyGgPGsFyj7deBxOVuny_UF2Y6TuRB8gF0lE_JvwSMC-08XPXdTH-c9Zo1amikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=GVPC31tjmT1QA11ES_W80M3ypAezOvQfhDA8b2-WR6_JOECPR96jHLgymAnzLtqbivdPbh9l5epjHXw-EHfiyakRv8WLDaTgdaVFBKM-frQGj02K7sRxnL14V6KapnF4-2PkbBJnKk1rDGnmeRdLRWW5yVHraDlKSME4Rr1LHRuTHdcgXL_hX1oCCgctWzQ55H1CzSEs-ssu_VLnE1Shs3qjcjOdls3s7MwHNovfhstInsAdoS-gbwbzJQW2SjAV1Gal4K6WF7fd4HFKoOBELaLvyGgPGsFyj7deBxOVuny_UF2Y6TuRB8gF0lE_JvwSMC-08XPXdTH-c9Zo1amikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=CEK5UP7gxDk0F2RFRoJxNjTPEoYNWdoZVlmtupZ-t7hCbC7GdALQkKCGj8TpYHdobiJdBPecJqwPPfCnQ77rFK3OgvFnYfFqhJwnkD_AQKYZo0aO8WY-H8hYaDz88Q-K6J7hxAAvuT4lIiTOOWpHayL7Xdcq1LpAMk3CKeaV10DKllJuK8UreZ602OYkO1XCXRS4RmUgwdTaUFC54wKb6cXxWwJ01OrVHNZzXC7OcxAzZTJl4osTpuKuLUHSOvi9SBef9L8vAhgGv800tiT2zVwRpB4MImMmc4EmJNLV-DkGeeDZ6G3UsPMUg4U_W2jrKJW4f_5TC8bvFCkgpBX1ozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=CEK5UP7gxDk0F2RFRoJxNjTPEoYNWdoZVlmtupZ-t7hCbC7GdALQkKCGj8TpYHdobiJdBPecJqwPPfCnQ77rFK3OgvFnYfFqhJwnkD_AQKYZo0aO8WY-H8hYaDz88Q-K6J7hxAAvuT4lIiTOOWpHayL7Xdcq1LpAMk3CKeaV10DKllJuK8UreZ602OYkO1XCXRS4RmUgwdTaUFC54wKb6cXxWwJ01OrVHNZzXC7OcxAzZTJl4osTpuKuLUHSOvi9SBef9L8vAhgGv800tiT2zVwRpB4MImMmc4EmJNLV-DkGeeDZ6G3UsPMUg4U_W2jrKJW4f_5TC8bvFCkgpBX1ozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo43A0l_R4Q8nwz4Ujm0opdG68kjB9BSK8sGDIrbub0885UYtF8oheqn6tccbrxY9OWgd9H6-8mkHju9dyU-Giu_Jobpy1aOjWmBnMfkICsOa78x35R4n4CQ4bE5qaBAWq0S20gqtKsA7LLzZhs39td3GolBB5YQiuCs9lI7rgCRTE5YGRYL9KsA7x7PzYDz0PQn7-VdoOGjjIhcZw_OMGWQJhCBZXSW7JVGID54DMRgBryE-HNWc3bfE7K1IGYrQsspSRtRgaTRSpFdKnHyrIWZygHEjm2BB6LD2Qh2TqL3Bc0F5cENRlptVTDmXEPhy1Vi-0qkXFBjXnCK0STjixfT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo43A0l_R4Q8nwz4Ujm0opdG68kjB9BSK8sGDIrbub0885UYtF8oheqn6tccbrxY9OWgd9H6-8mkHju9dyU-Giu_Jobpy1aOjWmBnMfkICsOa78x35R4n4CQ4bE5qaBAWq0S20gqtKsA7LLzZhs39td3GolBB5YQiuCs9lI7rgCRTE5YGRYL9KsA7x7PzYDz0PQn7-VdoOGjjIhcZw_OMGWQJhCBZXSW7JVGID54DMRgBryE-HNWc3bfE7K1IGYrQsspSRtRgaTRSpFdKnHyrIWZygHEjm2BB6LD2Qh2TqL3Bc0F5cENRlptVTDmXEPhy1Vi-0qkXFBjXnCK0STjixfT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=aksucCcgjxnuj2EHQEicEBfDUzCFpd3t0GQlRpZcrj8IXRCIrIuP3gpaidv1LAetq6GAimxQvMprPacQAgfop8hOGqM51yAzLkIALXIfQkijV4jNqMT0L6YPsaPlRDTuOqtaAFkwqDl3t1PQeN93kijMXoekWwzZW6jVVcbxfYLXewowOkyOZJjR3YM6SVpP4SRrbsff_cM2M3ThOQovds4Hny3FOOSFiKDZPLrsiGj0HM4_3ggXK0w4_0SfheTmc7nvpXXhu8nVYi_8qOd9qOh6st3dFePkUghz_qy6u_35RQOOkUmnMIhRF8fx76h_VraFBZgcykOJAfvfaBj4R361xelX8jHBanwKZy0bxFa-MSWoYXolJOGCHlCMLV9dMGVhpTDBQROmDbBmFYrfPq0GViD4aTMQgkkyWjlgB77TsQQG3FmUIT_VXXIvz-l7ZGUfeji1e6aIU_Z9DZ2PWs1Bxmba3srbq9pi3MDtyS72TCwnuI2Q4qdSZ20xMRPRWiCFIOPSWGXlW2ewl0fqIzzh9v039DqNIwcL65_u3cAJJIvDc57235sHtdo3-8zbpR-MsmXdz8akaGVGD9NAIlSAFa6qiriJWwkAqv75P3N3WXBh9BezcXeh6SWZfwgUiSOG0UwZrXtl4F6GiIzLS0lHZpxOvqPC38rn-IffNy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=aksucCcgjxnuj2EHQEicEBfDUzCFpd3t0GQlRpZcrj8IXRCIrIuP3gpaidv1LAetq6GAimxQvMprPacQAgfop8hOGqM51yAzLkIALXIfQkijV4jNqMT0L6YPsaPlRDTuOqtaAFkwqDl3t1PQeN93kijMXoekWwzZW6jVVcbxfYLXewowOkyOZJjR3YM6SVpP4SRrbsff_cM2M3ThOQovds4Hny3FOOSFiKDZPLrsiGj0HM4_3ggXK0w4_0SfheTmc7nvpXXhu8nVYi_8qOd9qOh6st3dFePkUghz_qy6u_35RQOOkUmnMIhRF8fx76h_VraFBZgcykOJAfvfaBj4R361xelX8jHBanwKZy0bxFa-MSWoYXolJOGCHlCMLV9dMGVhpTDBQROmDbBmFYrfPq0GViD4aTMQgkkyWjlgB77TsQQG3FmUIT_VXXIvz-l7ZGUfeji1e6aIU_Z9DZ2PWs1Bxmba3srbq9pi3MDtyS72TCwnuI2Q4qdSZ20xMRPRWiCFIOPSWGXlW2ewl0fqIzzh9v039DqNIwcL65_u3cAJJIvDc57235sHtdo3-8zbpR-MsmXdz8akaGVGD9NAIlSAFa6qiriJWwkAqv75P3N3WXBh9BezcXeh6SWZfwgUiSOG0UwZrXtl4F6GiIzLS0lHZpxOvqPC38rn-IffNy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owjWa2c621myK9MLtNdmeGupBZFvKk6STRWcGgSgiPk6TAiBKWsA3N6UrQtSzQ-tKw9rcfZ_lAi1tZIkJJD6Rleezbt0KAHI78yB-7Q1V1zNkDjA1Ob9tGQjKBDia3sRAkZgiyo5iPK9RXusBKFGaZBA0bBOUsv312mL7P6diSyn1Gf7z0S2QAdNRoGfvshx9jF9naijZ1iqi2aefIQzFLVa7I8OT9C_QbtcwbH6NhbWptEKiNHhQIS1rQsCZHU0IVQbPyluCuaSlrSn5wIqtEmF5qGO9xgFqjZLSoZmXh88oTSqA5_dXoEX2nb_G6SM2osvmq8bF782m97-nsltQrcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owjWa2c621myK9MLtNdmeGupBZFvKk6STRWcGgSgiPk6TAiBKWsA3N6UrQtSzQ-tKw9rcfZ_lAi1tZIkJJD6Rleezbt0KAHI78yB-7Q1V1zNkDjA1Ob9tGQjKBDia3sRAkZgiyo5iPK9RXusBKFGaZBA0bBOUsv312mL7P6diSyn1Gf7z0S2QAdNRoGfvshx9jF9naijZ1iqi2aefIQzFLVa7I8OT9C_QbtcwbH6NhbWptEKiNHhQIS1rQsCZHU0IVQbPyluCuaSlrSn5wIqtEmF5qGO9xgFqjZLSoZmXh88oTSqA5_dXoEX2nb_G6SM2osvmq8bF782m97-nsltQrcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=JAcXOzm9l6ew2KMfk8R5-jvrEwV_N6N1V3-vrogMsYSV0MQtdq8cZjzBvqhIIZIQbXV4vOXR06MYkJj-Xnf5iPpuNSnU5pZ_si_nBS95or6c__6sRg02wLrJ44AaDPiSgxhE_h1xiV2xwbsps9Q7npCszj32nhIbO7OXhB7SM0B8c-b9-_Dfqi6aVAUgIuCgsbknMaesnx-mZDWguS-cZEnJW-JnwD4Vj-CcnOm4WjeVM3PJ3i5hbfjv97jQcG_aRWiApf7oTXuT_5sZubBZ8VOmMPy3QkzOsXEprokwm_xuxTlmOvdy_UFLCEbkF4dlqqNJrRsb-V0M66xUvsBRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=JAcXOzm9l6ew2KMfk8R5-jvrEwV_N6N1V3-vrogMsYSV0MQtdq8cZjzBvqhIIZIQbXV4vOXR06MYkJj-Xnf5iPpuNSnU5pZ_si_nBS95or6c__6sRg02wLrJ44AaDPiSgxhE_h1xiV2xwbsps9Q7npCszj32nhIbO7OXhB7SM0B8c-b9-_Dfqi6aVAUgIuCgsbknMaesnx-mZDWguS-cZEnJW-JnwD4Vj-CcnOm4WjeVM3PJ3i5hbfjv97jQcG_aRWiApf7oTXuT_5sZubBZ8VOmMPy3QkzOsXEprokwm_xuxTlmOvdy_UFLCEbkF4dlqqNJrRsb-V0M66xUvsBRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=fK3xwuvt4BbjspI1YEiBPlSwNLVYAs4_vi4Vei2v00u2lE9K-geqqFhj-tJbuzmGmoo6N2sxi1gws1yBepPmS6DiaZK_VqZonQVBkezCxY_I52SV4LxylZoSlrJoFcBqwu4sa_SfW1Hc3YNOjVDH8rgJp3yygotOlKf83DmlJvNcwG7hAvvAneqmJ0Nxp_kUuqW7ZG08djb7IZ4OatYoTuFVKXGMECi9dD3r9KEqtCw818OWezgqDs_pRg17VbTSYjQlppXzINbyAfeqaO2tlaOpIIvNjDNcw7K_WNKOglLJLNKg2GwEXs4TBiqV56wWmzT2pkbGsFQ7r8HM5FMUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=fK3xwuvt4BbjspI1YEiBPlSwNLVYAs4_vi4Vei2v00u2lE9K-geqqFhj-tJbuzmGmoo6N2sxi1gws1yBepPmS6DiaZK_VqZonQVBkezCxY_I52SV4LxylZoSlrJoFcBqwu4sa_SfW1Hc3YNOjVDH8rgJp3yygotOlKf83DmlJvNcwG7hAvvAneqmJ0Nxp_kUuqW7ZG08djb7IZ4OatYoTuFVKXGMECi9dD3r9KEqtCw818OWezgqDs_pRg17VbTSYjQlppXzINbyAfeqaO2tlaOpIIvNjDNcw7K_WNKOglLJLNKg2GwEXs4TBiqV56wWmzT2pkbGsFQ7r8HM5FMUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=cZWRJoHSczaHe3vpiYaAzqTMtiTZxkBPFGdM3qO1o-8Q2gEgwVceiOPHPkcOmrcN4bFBvP85SQB3FuNl_jUJx0eVfY-faGqHaKXlq2c-ej4EX8VEMdDAMrxfYo9TgRynA_uxK1WAKYxMhB7GTBaNtcCw_VnFhuSzUpZbU283mBcj03yxPWkbXt3FcU9Hh0ll39uKwXHFF2zl4DTbQ0CPJqKIK-PpBlzj2uZSyL7_v-vNTgyPB_GIQum6oN83kEWXZINq1965gegXbhGpnNPsHLGWkMvArVEAptw0i8pI1IRaC6-p5aIN4-mgzOvH0pLP163Ig427eRYkzszSTcpINA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=cZWRJoHSczaHe3vpiYaAzqTMtiTZxkBPFGdM3qO1o-8Q2gEgwVceiOPHPkcOmrcN4bFBvP85SQB3FuNl_jUJx0eVfY-faGqHaKXlq2c-ej4EX8VEMdDAMrxfYo9TgRynA_uxK1WAKYxMhB7GTBaNtcCw_VnFhuSzUpZbU283mBcj03yxPWkbXt3FcU9Hh0ll39uKwXHFF2zl4DTbQ0CPJqKIK-PpBlzj2uZSyL7_v-vNTgyPB_GIQum6oN83kEWXZINq1965gegXbhGpnNPsHLGWkMvArVEAptw0i8pI1IRaC6-p5aIN4-mgzOvH0pLP163Ig427eRYkzszSTcpINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReJSVM3Aud4qB22zpoyAtKXzQvKIJnnEccFTMQCqJn_aQNRw2o2iRa2lQfSgJ1pc_vQmbnSqfDLHUnxZDzcGcf5FqBcM00nSmS7AtsIBgLNAA7Nhr-2AjK5O5HR2dtqfEHuNvD0Yj5P_ueQIZqJ8lb58VWcUwyS9LQkqksakF_4kABWdUrMFNy9PZDHJxag2HMzQdsBO8-OHo6FhkDbDvMAaHc8EGchliw69uxO-6sz-6gePYiwmSdOcpfcyCQ9gaIlf6nuIYC4jDPUKFa5qMIXn0_6Ewp59pzKs6m03DA3WfzAjVTfkgFCWhnk8WurPZIHYA1806E7iKaxrbmzrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=L9SeQ72uC-YV43DqIgwuegVi5h-YSLki05TgDvXcWmKW30Ahu5V6xr-ywyDW2Rz3TBgsMb1hOQwuVbm0GKtYEKdpLVjk6_Dgc1yxvXgztQ2v4wjeF23Ac_EkAoOka_QYQjAD0w5Dc2RzxoEMtIQj-QCBGqiX90DOaH51OLllzKiG8BuTjG6mC1E_BNkNAz75MMgWK_r3awdapFmRgZ6Mo9_tJo122YEHDr1L7HDdeUcsR4PnHX8TeL81wY7KYsZU8em16zW-e5-xWO22Ua59Z6jlH-fU9JhH-44PCi7IiEE3o3z8l3XLvzZu44zt5upa0kaPtrNMhHQmkL4quaa4gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=L9SeQ72uC-YV43DqIgwuegVi5h-YSLki05TgDvXcWmKW30Ahu5V6xr-ywyDW2Rz3TBgsMb1hOQwuVbm0GKtYEKdpLVjk6_Dgc1yxvXgztQ2v4wjeF23Ac_EkAoOka_QYQjAD0w5Dc2RzxoEMtIQj-QCBGqiX90DOaH51OLllzKiG8BuTjG6mC1E_BNkNAz75MMgWK_r3awdapFmRgZ6Mo9_tJo122YEHDr1L7HDdeUcsR4PnHX8TeL81wY7KYsZU8em16zW-e5-xWO22Ua59Z6jlH-fU9JhH-44PCi7IiEE3o3z8l3XLvzZu44zt5upa0kaPtrNMhHQmkL4quaa4gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkTX9m0CnfyXF8DzH5nyViTUF33xui9MIAR2usI6LfEAWRv16p8ymLDPsrb9oDDpLZxLTPxwglBYU5Jr2-beCg0OX1IzUffet56MbAbPsD8dJ0CmvA6_ksHLsuRZMPLx_VuoYPYCqGWAliYvPlj4DDRpkZAQ1DJJUwd2D2Wq_XUcGudx6bOlfMJ-miWNv0H0k6AQFBTtZxlxKEiiDrHxb84Kzn-PSIWlO7OUK6AN4_YNxDPS_4tRujutNHUR2SJgnL3O-WBvpdQofRBvlrjThS85vKFqJ11tYWqsXkNhGsVDciQku-LZ5IoaEGGqZ_NzNOnCr4QtUPh6PKXevi9jwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=dSdUtlJFbKb_b3MJYZTCZwChvgBeN3702dXjvZ245RKn_EeKzywcb6Ck4pU5bNiKJb1Hvbf2EF9zkQXwTWChgHECo-fVeddM0MEzKkaKP0KzJs9PKynIORzvHaPlAjCN7HnJBy9wPgprbIIy9YnTTx6UAPmVv-9iQHKwE6F4sBrLasp9DOlV2jFOr4vcmoPUeMqmn0j8FK6OHv6lwZCf47NNJ_lAD8odri0nF4-u3J6JWDEQinFy4u9Gua-OwP_sGod2yZa3_Vs9tei7w3cNgdbnKT7LvOWiG-K3F84L8l7j9olEDFeo-rh4D7qXj0InfQhcVegqrf-QfZTycJwiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=dSdUtlJFbKb_b3MJYZTCZwChvgBeN3702dXjvZ245RKn_EeKzywcb6Ck4pU5bNiKJb1Hvbf2EF9zkQXwTWChgHECo-fVeddM0MEzKkaKP0KzJs9PKynIORzvHaPlAjCN7HnJBy9wPgprbIIy9YnTTx6UAPmVv-9iQHKwE6F4sBrLasp9DOlV2jFOr4vcmoPUeMqmn0j8FK6OHv6lwZCf47NNJ_lAD8odri0nF4-u3J6JWDEQinFy4u9Gua-OwP_sGod2yZa3_Vs9tei7w3cNgdbnKT7LvOWiG-K3F84L8l7j9olEDFeo-rh4D7qXj0InfQhcVegqrf-QfZTycJwiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqRgEQSu3f1l6HepJ7uq20dDHoB4BIZB7clf6n8G0tG1Jj3wjgnPxOLufY9_3fOBhTf0U3hGa5JkJ8QDg0xmmSRuAwIpWpoIZ4XW8UIwnDVD7K6TcQ53FMXvK1PyppNmRNCr2C3KXH_ukBSfPCDgnN41w16Rk_ZKqH5zWPj-WuOSkqkRslrs0fwf8lUcAG8AR5pyrR39qeRdvJ01M5XGOPrOLsTFmTgMY2K99E7G1lPqFFGfElqgxIcfEH8SIWt3IYtokXdsvdN6gMv228zZDqUItOPSgwXl8C9Twrb8-E89pD_5bu_4Fn5Qs3K0a6slh-Mt0ff1Pvrnlh66Ey1mKJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqRgEQSu3f1l6HepJ7uq20dDHoB4BIZB7clf6n8G0tG1Jj3wjgnPxOLufY9_3fOBhTf0U3hGa5JkJ8QDg0xmmSRuAwIpWpoIZ4XW8UIwnDVD7K6TcQ53FMXvK1PyppNmRNCr2C3KXH_ukBSfPCDgnN41w16Rk_ZKqH5zWPj-WuOSkqkRslrs0fwf8lUcAG8AR5pyrR39qeRdvJ01M5XGOPrOLsTFmTgMY2K99E7G1lPqFFGfElqgxIcfEH8SIWt3IYtokXdsvdN6gMv228zZDqUItOPSgwXl8C9Twrb8-E89pD_5bu_4Fn5Qs3K0a6slh-Mt0ff1Pvrnlh66Ey1mKJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=dXE6odFJdYUBkSVj9uas1oBfkqZkExFKs_vwYAmfMoECvj8Uj9zfiZkRc8tf-uPxIj-nSdNFwpk7ZOJG7vE88Nv2qZfsVDvxyuS5pB-oTcb6UoDS9BH4PzeVo5PA2y9-Twzvzt2BXJy2gF3wy2rTVTd6OG62wxNZiAQ_cdrQAeIiuf60U3BYubpIZgAcL4menFftIKX8IWzch1YbLZ6RLsodxq1h7K8tlunswpcUpf9jm2NIAnWapHaWR9LuDH-6KC-IeUXV-QgQKN33fRqnvdFdU7E-BLgscg2B3b8V8Fxgk9haQBq5I7dPfkXiSnygCslWv5ZR5aIZK4HsEyYulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=dXE6odFJdYUBkSVj9uas1oBfkqZkExFKs_vwYAmfMoECvj8Uj9zfiZkRc8tf-uPxIj-nSdNFwpk7ZOJG7vE88Nv2qZfsVDvxyuS5pB-oTcb6UoDS9BH4PzeVo5PA2y9-Twzvzt2BXJy2gF3wy2rTVTd6OG62wxNZiAQ_cdrQAeIiuf60U3BYubpIZgAcL4menFftIKX8IWzch1YbLZ6RLsodxq1h7K8tlunswpcUpf9jm2NIAnWapHaWR9LuDH-6KC-IeUXV-QgQKN33fRqnvdFdU7E-BLgscg2B3b8V8Fxgk9haQBq5I7dPfkXiSnygCslWv5ZR5aIZK4HsEyYulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Z0um93OSBikt8Se_5LdHxvY4oVVjNkFsDyg6az0Y3uc2M2JcUQVBj00iKNwnA7Q7sxnqowsWZnXPOXn3Lki2S4kx-wU6hZiEW2d8i8XD0BLGK4DSJyRhEYa85MwnwJRQwQ4YDSt-ElDFkDRQi43XjoNvSZS39bEsntyuY08gMx6bWC4pmGoRi3KS3oXWSGOtT8zH_nppRmHQ4WBOjiAqVEItakM1qQV6rrq0dRJPGTamn5v_buIwJ-fMX4EfiuQ7yYjO0Yu1rR4Aq7Jm3WGO5UswnEU5UAL1jc3teAhK452KOmMv76cywkhOSboZBbsIw8aJdBJQ6K3TtSvpj_OtMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Z0um93OSBikt8Se_5LdHxvY4oVVjNkFsDyg6az0Y3uc2M2JcUQVBj00iKNwnA7Q7sxnqowsWZnXPOXn3Lki2S4kx-wU6hZiEW2d8i8XD0BLGK4DSJyRhEYa85MwnwJRQwQ4YDSt-ElDFkDRQi43XjoNvSZS39bEsntyuY08gMx6bWC4pmGoRi3KS3oXWSGOtT8zH_nppRmHQ4WBOjiAqVEItakM1qQV6rrq0dRJPGTamn5v_buIwJ-fMX4EfiuQ7yYjO0Yu1rR4Aq7Jm3WGO5UswnEU5UAL1jc3teAhK452KOmMv76cywkhOSboZBbsIw8aJdBJQ6K3TtSvpj_OtMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDEVo7J9mMMRmTuZ6ubRUSiZHS9_ClPGO3T_30jsZSDqIcXhIJJ5CGt-eoSrypWlzJXhlRE6_xlx_6BC7DrENqSt1WHcFxLolNnox2eR3xW8CMJVyDj50wnJr4ZKRKB-zIsuLpCy-Cl8SYqH05M8wvlcOOolb9RkurxPBxzGfpsCNNf8tMFh111Pg8Z1WI-y9BkMioVi2lQ4yzJg7EV3dIELVibJl991nBLyUqsYv6N3iQjahtbIn1n6YIc37TOpY9justD1hMWPFC-53qJcjXFivrlNji8N-w6b_Qa3zOC6jbfCfPznUmTquHx2buYmRbu8Xmi8f-LQwUdoNOC_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=dUioJcWZmibA6pnqyV-xuh5xO3U3a7hDIxPwXX1Vz2dMNfLUUfSaH4FYryJVIynT0E89ZE9W46YVW1B3lXXrqCCIMMSO65XvVsdrxpNjyYQNtx9udriojVXgZbfYrw5Pd9vUcA0frarUvY9TBJJGXXFFD0xrnVRxAzDL2hBuDAXtk8BRGJDYx7BIDc4ek18JeV-YouYo9g1PMGTLFq7ww30IxpF2efCixCkTzwyOM-93hlNMNknQe-5ft67I8dJxCRT-x-45HG37xICqjCAvvrokQs5PuXHL9X21jEF92V7Qbjet5UseWc7Z9HRkjxlfXXsz-UinqwSEI-G5lcXoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=dUioJcWZmibA6pnqyV-xuh5xO3U3a7hDIxPwXX1Vz2dMNfLUUfSaH4FYryJVIynT0E89ZE9W46YVW1B3lXXrqCCIMMSO65XvVsdrxpNjyYQNtx9udriojVXgZbfYrw5Pd9vUcA0frarUvY9TBJJGXXFFD0xrnVRxAzDL2hBuDAXtk8BRGJDYx7BIDc4ek18JeV-YouYo9g1PMGTLFq7ww30IxpF2efCixCkTzwyOM-93hlNMNknQe-5ft67I8dJxCRT-x-45HG37xICqjCAvvrokQs5PuXHL9X21jEF92V7Qbjet5UseWc7Z9HRkjxlfXXsz-UinqwSEI-G5lcXoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjosYkH8G1Xq84LUABy2uZCxrrS790dEDhguaAsiRULwC7iOp_7QNMtebxY4IGcFilrt4KSoYBFngHUX38np45Oqtk-Tc6kzSBaIMWJiLolyLOYHUte2AHtXnHZOyzVeUUAo0dPmBgF5qhr-qTm-c0lcCK-qHdHGSt0tSj3_-J63RkBxggjA-m0aVUHFvvnKBQT69pr8MFOCiwn7zra32CQrWi0e1teGIg5jSXBjozDOzaS3BuAY1XZOad-sGjva_G30E1zdXgR8KCzN5Ixt9K8ypETfu7JqMo4eGaGqbFJXo3bZ9L4m2yLbKmHFX5oevIbWZ_X5uAPfQ-zBSjhvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hp8r3Cs0bVxfQhinDCFWB0e63Z-fhniDzotuSW3stViQ_F_esZh4gq6tNWfctFhX7k0gqEuk4cx4GLBai59nVmm_FLVzm0TThWMlL-e2FuXrDl1J2HQmPsA751JCq81abzGAVA-0bh4CrEJX4JKw2bOORmUb4AY0OHMZOMaAeKNObzMF_-Sr1eVKcTN3vqBYgPTWj9PxoRwvzbuEb7SLZIlVyGxuUvfYLadYjGjmDywqrO-vZMJ7MftElebvq21jMTSaOTpnXZ_ToJHKqVVj7icrjio72yJDB3Mkm11uC0ynUam7bUG9dZhUBD5LSkL0G-9avQYHF4g1TBIrtSyndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hp8r3Cs0bVxfQhinDCFWB0e63Z-fhniDzotuSW3stViQ_F_esZh4gq6tNWfctFhX7k0gqEuk4cx4GLBai59nVmm_FLVzm0TThWMlL-e2FuXrDl1J2HQmPsA751JCq81abzGAVA-0bh4CrEJX4JKw2bOORmUb4AY0OHMZOMaAeKNObzMF_-Sr1eVKcTN3vqBYgPTWj9PxoRwvzbuEb7SLZIlVyGxuUvfYLadYjGjmDywqrO-vZMJ7MftElebvq21jMTSaOTpnXZ_ToJHKqVVj7icrjio72yJDB3Mkm11uC0ynUam7bUG9dZhUBD5LSkL0G-9avQYHF4g1TBIrtSyndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=kAeCXQiZ6JEnGXYYoK_mob9G9l1Sat4GNWsOWlCPAh_UU8PswtF4RUpn5jxmYSECpHSZEGD16kVTFbbiqkc9lT6ISJ0dPs2WP9ir3m8TH4mVrp7B-prHLeHA0GAKLUwLd16KaHNQRq6767Q_BUJj6dRRIOYYSWT4Kq3hsu5_dsqAKgDYixbsSnAcno4GKGdjmL_ssJTPGKYKztZXCYPnT_aulfQwHKUmaPbkV88E5mGUuYRoxtM3hRM7m_-KZjsuRdFF0gwddfEmaFRzo3pi8RJqSLqp6UlmydMqi81EawXkSd0hV9Cvb89QHSduPKUKljywN33Rbezvz4h_NNZU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=kAeCXQiZ6JEnGXYYoK_mob9G9l1Sat4GNWsOWlCPAh_UU8PswtF4RUpn5jxmYSECpHSZEGD16kVTFbbiqkc9lT6ISJ0dPs2WP9ir3m8TH4mVrp7B-prHLeHA0GAKLUwLd16KaHNQRq6767Q_BUJj6dRRIOYYSWT4Kq3hsu5_dsqAKgDYixbsSnAcno4GKGdjmL_ssJTPGKYKztZXCYPnT_aulfQwHKUmaPbkV88E5mGUuYRoxtM3hRM7m_-KZjsuRdFF0gwddfEmaFRzo3pi8RJqSLqp6UlmydMqi81EawXkSd0hV9Cvb89QHSduPKUKljywN33Rbezvz4h_NNZU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGfEjDeMjVz3JGJzZUuKSSh6WX4CNfJ-iZn9YQU7atOyHp5VSvmjKhV0mPlFJwNwho0MljbB3gurK01l5p4sW9u0RhxOeKx67HUlZiuDdcOW4xV-ECMf4N8KwtKVUEO0sZjaEWInO7nz4kfCYcu92wWvGOJVndpfbYIs3JWxDZjZwhMFgnOTBMMPXzqrQQcISTGLbRhBOFCfaiazZyn_xYjtRekirSTNhByfLm16G8PSvWkRjua6iB7ApwatiZvXDpQ_1dpa_yhbUWcDpgsPijQaAHM1Rqd11xNrLp1uE5dQk32kOuZi1zbDnXwGxkBoGq0hl4v1rS4BhwBH60RcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=BSLPB4XVXnsTLETi-_y9XV4YhnAKCMyX_uzLsjlDuceLylXu6cZ4XKC0CNn5L8Z5xE5p8wJQS0F3Ih-2-JmkjEDEL7VyJVbf_Mlqx16rbzWjMllN9N-LfVzYNacOcUi_4zJ1g1-l3g0lQ_LwpMUjZs8kQ6q8M32lmKYOUp7lTb9frU8TlDqYJ-75MZvBzkUG5kcgRoCJy0CKge9l8sCQkH1BJBK4cTmj26ru9ScrIRQ0sAXqtgquCTruHFAgnvt_q_8PZZrox80DzmZ7egwszXEdxteVvuWh5zBQ_VEuFIvBuXFgfCzWifESCRvf1v6B9vSgO061anlLPKMnnNuDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=BSLPB4XVXnsTLETi-_y9XV4YhnAKCMyX_uzLsjlDuceLylXu6cZ4XKC0CNn5L8Z5xE5p8wJQS0F3Ih-2-JmkjEDEL7VyJVbf_Mlqx16rbzWjMllN9N-LfVzYNacOcUi_4zJ1g1-l3g0lQ_LwpMUjZs8kQ6q8M32lmKYOUp7lTb9frU8TlDqYJ-75MZvBzkUG5kcgRoCJy0CKge9l8sCQkH1BJBK4cTmj26ru9ScrIRQ0sAXqtgquCTruHFAgnvt_q_8PZZrox80DzmZ7egwszXEdxteVvuWh5zBQ_VEuFIvBuXFgfCzWifESCRvf1v6B9vSgO061anlLPKMnnNuDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rka_vpbUnDngKtSYa41ShCtODap6t-amYxsnQ1Lggzg0RmLdp7lIhNLK9hoWro5MFL2HW8xKhR70QDM6zd29vgK7rqg5kjdDzxp3B3Sx8ACZ_XtxEMkMbNvsIutEexCF9SQlwDm4oOnsKfURjdXfnouFZ6FbLWvR1eWF4EA5mmg_sb7CX614HZ0sdNnomIBPW1pYpG2lIto7Zqt4ORdX1iQW1QdM_mofosCz5MLAtS9g5ql3_J66MsCkrvO-cHF-8efTuSq6sk_4NOi5Fb8vthh89yTJctiI3mLvEhAsDocJmjuMkYB5Mfnwp1oLTnpk9Ny0JTKj-zv3jv_fzgiTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=caetnXLpKzMjBSXMJbJzZyBnqD6RqCmqae7Rf5ocAAES16B5iFtUnRbP7TsbFrZJ5aMkE9mEFsAt8V500iOMcDxPZtJTjZXaIUscCKlvommAvPcY_QPmu2yjrovCglSwykyE5BHNHebv73p3Zy6mY8QR5PaGZpCd_t9auPq5ssIn0pjiKunJCXDF9cJQtFQ3E0oSF_lKe4gmwXGAxLY1FjnDmeAniavhF9gPMTyb_bAFwgwAefwggOFtD29gSeRCec9-DSeCuiIJ_JqhuZqcR_4ezhYQKdRG9eKdHedahmUfdNXckYvHi4XWq1jV7-4so_eB0RDpqVcZltqhldIs3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=caetnXLpKzMjBSXMJbJzZyBnqD6RqCmqae7Rf5ocAAES16B5iFtUnRbP7TsbFrZJ5aMkE9mEFsAt8V500iOMcDxPZtJTjZXaIUscCKlvommAvPcY_QPmu2yjrovCglSwykyE5BHNHebv73p3Zy6mY8QR5PaGZpCd_t9auPq5ssIn0pjiKunJCXDF9cJQtFQ3E0oSF_lKe4gmwXGAxLY1FjnDmeAniavhF9gPMTyb_bAFwgwAefwggOFtD29gSeRCec9-DSeCuiIJ_JqhuZqcR_4ezhYQKdRG9eKdHedahmUfdNXckYvHi4XWq1jV7-4so_eB0RDpqVcZltqhldIs3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re2ogj7luh6f6ps2sdWdk5XxbJLKRa-6cEKL8bGkyUC5Ir1QjcO4glXhMJDKp6b2srQXC7WTlmZVx4wGsxIlS29Yfh126PKEyPf-L4XDY_0h4ujXKocijQIM2JWkWXqurdnoAfa2NSko64qE0ki5XkZMIyQqU4hOhrLFSRisO7Xy_zPz6kiz5Yxm1bbqpEvMpkiEsA0_c56iXb7bJFHPA-wHIa4ENEMfxJfO_AtR4CMb7sCnrgrchDPf2n5n7TKYxdfz7MkSepwBPlfbv0oxgNrlbl9PlqoVYfhYRYdtqEUor4sxVEadGJPkyLdlXgtqD0wt1-ckN56-Ios0b2MG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfAnbPQvU_v6VsoCRWdRsYBaBy5Vkc3IkDvJaCiAf63PPWclLhJayBruD6vBwwdQyijPFaqSYIuXQoJYdFHQR2VumiXLg40H3Zl-CPqPeHShQKqfLfoeOYBDZcw9YQx-uRDo8X8FEt4P-SQdPn4oOIiqv23DmAQVAJEVRP8jnaROoSEGtX-D0_r-FWem6hqskE-y41qfj1m_jnN1_G82-hkmzkufagti6HxJU7l4Skh2zjKXxKXHarr5vfgKHHyX_7P4mQzB6tWNn4Shbei4OyV_-vbNauo0P_6aD8E5VKCu0hB5lTv7elcl5Vv0o0i50d2Afk4pMfRcPBOtCQE2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLiz-nbbFKYjl4-6vitwjOsGC04W8fbM7l1VApmgD1knfqpNHtzYJICiVAXOkld8svbcvg9KyI4PawJXb6E7BKcA7gBZGTaXR61lL5HPe9IyNt6it-SSvggNeWS8TU3FCX0w9OTDiUg7hMr8VXITlAIKeNxmREVpF1-6Xmk9nbzekNnMOkmZAGIhfTzBweg5IP3VJqIEwChWZyRYtHRdl3UOwPFKOh14Wa9SdBIlj8rRfbiSI0fWZioqIfjXxkYdjOxAt2G-UEJZt6ki0oyQ7_CARMj6uLSjzhBeS854BrTGR3sgH5DlwfmRUyyQwsAQVqfYgocpMxbwg2gYYtv37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=GybsYJyN5Fba0__WP5jYamFG-SAOnzcolSIh1-tTOKxUmD-6pFNpoJql6nRZ7_4tlv-pMGmbWTIlvegdcCwCN6JLlPry1YKRhN8X9NC-ZbNQjkXndEvk3noASEo04nvMNIsSZUOZPmrcD-eDTB5zQTUPGRjZPeF8jBxc8jFhGNep4wnYsYS1LwQHgFyPTe6BDXYpNI4xcasGKOHO0siVHEZoVTp633YntabFZDuuHPNMUgiBggOkJox0L1Q-Suyg1iWMhn9SXyPQSLug7H_Jz0tCQPWv3HcLzSTb97vCI-H9g_Z1QudKXO1nzJel7ie_PDJ6QTy7CtW3KcL3SPbxZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=GybsYJyN5Fba0__WP5jYamFG-SAOnzcolSIh1-tTOKxUmD-6pFNpoJql6nRZ7_4tlv-pMGmbWTIlvegdcCwCN6JLlPry1YKRhN8X9NC-ZbNQjkXndEvk3noASEo04nvMNIsSZUOZPmrcD-eDTB5zQTUPGRjZPeF8jBxc8jFhGNep4wnYsYS1LwQHgFyPTe6BDXYpNI4xcasGKOHO0siVHEZoVTp633YntabFZDuuHPNMUgiBggOkJox0L1Q-Suyg1iWMhn9SXyPQSLug7H_Jz0tCQPWv3HcLzSTb97vCI-H9g_Z1QudKXO1nzJel7ie_PDJ6QTy7CtW3KcL3SPbxZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMVDR9hGSO8Bx-_MCGgKOF0oov_KkoXgh5W9oyvB-h_18gqZUFWE333B-QOJmRMO-7bB35Mv2SW_E17wupf-f0EmQ362m3fYJR9N44Xq88iEDeFDMLTIxQNDmfVjp9DpW68Y_LpfNuUz6-20oqlwRH5bGJXo924TwP1Ans3WdTYdAYF8msCGa0xr8zaf4Tvu-ZNmBeKVFajzCh5y6qeI2bglXQXgGBnOofkTXrdTN1KrEw0ChdE411Z9EdEXT0vDWHsJm5OrbihegQSXWu1BqBWF76mJo_9zct0FyCNJ-wk-8Wn3LmR3fBGhtKGEVOCkhkMKf1nH9x4IKploMYQ3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kjn2K5-W_Z20pu262eBkUjDF39u30k_uqiJJrCFUvxbTF7dz4L1nRtg7X9jVgJSYc7AG7Mh05tXza2GQVPvwMOxyjdWLqF0zxmPxmkWY1ZcRAZydUpZ9aciOqIuzOjVMps4Vzx7oVICntGU6xAqwrmTasMqepWJziavHO_sxsr-BbMVuBRR3iG3hEkcaMS0affDlxjQTbt46ALVhzPI3obUNqMbdCJDZhPulCBkaHDoFptrQDEAHeoXhYG3X_YPtpw8esHIygypHfaq5JBfcT43o2WuF2ViyDobAln5CSfyN3ioqmf1zspmonWOsFrTX4k3x1rSZNhZ3nf4B4DW7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbWtk4unUABPti_ngttjnMXB0K_iFjjRbhZuSTMXOoPkuzo6cIdM41YYSHHXe2EAP0YBGDgBoXY6zNzVtBlx9lT2T5hwzYz1Xekb22f_ntqdhaKDIoDdA7gigkoJoHy6WXeTUutJv0DlQjXPBbjUb1QTu1vyMVvpnZssG9xKRzwPmPz2ypPm2l-CH7X-MajSIqE8xbSlutvJAP62QUAJgdYMOGLsVTiLhUjykWauRq2G7beWKBJ3fosK77olFDEXuJv9PMObTFhO68ZW13vIKZKqrpopTLirj5HVE-UeQ6ywdijhs3ohrTtlFnnN6efT74UykdwpFmU6tugkVewqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3h9xvSawY_1yruiIrE-ZChUFprZBxBNYe06F5s6b6yNA8jDem6ci35iLSqY5s6CuO92D5Sr4RnYUKnpLuyF6GnsOB348-4sn7hd5X-9BUtJkuKnuky_tEhcGIzbNyf9SpcVdAyP3ox4U8WYoCRWsfGYJxY7-tvYN3lzlfirc6pAyorsOQb8OCM0XX86rVQgNcQoWfF3m_A9A7yYrct7vnaiBSY9ZYvXm8i7rlbWXDHWs-nkDIKDD5auGbo4LSFi8TjAtipaN7EKb9FD3jHFs_TuF2z_CPAf0VQVILSOCvoEyWmxxnqUGmr7K3hEV1fENHqs_FXAPow7997ErAeKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=EHGGFsp13G0rxPr8JC0Tt-mRWR54lLMY3_1I_NgqeqhIz5k1mAyG6_F62iBGt4sO5dMu09JlgRSdOh3WswCdl6bLPCOuD-_AkPMFg-d4kfzshhnFxbZOzwIiijEF_0xgchC7WhF7No4ghmqwb5rfLLCY9dQPKn1OggkQ2iLtYnPni17atzs4yQUAPwnEoaaCq9DVAx5LlH5AjyzQL2qLlK_Kn9qfXY4cNRbUUlNejvYgIf9PYlx9C8XwiPZi0TrySpYnW8PDIF1QnRsgFlKG794y0INDv6eD7c4ZvSjV7jcmBljk3OF0zSCuCmF_mH7PKukTnAljsQeyMVuaRLMSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=EHGGFsp13G0rxPr8JC0Tt-mRWR54lLMY3_1I_NgqeqhIz5k1mAyG6_F62iBGt4sO5dMu09JlgRSdOh3WswCdl6bLPCOuD-_AkPMFg-d4kfzshhnFxbZOzwIiijEF_0xgchC7WhF7No4ghmqwb5rfLLCY9dQPKn1OggkQ2iLtYnPni17atzs4yQUAPwnEoaaCq9DVAx5LlH5AjyzQL2qLlK_Kn9qfXY4cNRbUUlNejvYgIf9PYlx9C8XwiPZi0TrySpYnW8PDIF1QnRsgFlKG794y0INDv6eD7c4ZvSjV7jcmBljk3OF0zSCuCmF_mH7PKukTnAljsQeyMVuaRLMSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
