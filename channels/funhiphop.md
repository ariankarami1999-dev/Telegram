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
<img src="https://cdn4.telesco.pe/file/pzGnC89cWHWwgTakiB4-wYMV4MyEG5q8n517ACjJFe8O_y54u4s-Lv2UGk_ADIvsibavbNG2EdUiWb0-0Zd1dA1eSfDWYioGeDqKSi98Xukxr6zrOQA8Q8EnJDc8_I4mj1iUHVgMOrpTkmMGxwel5cEihli0FDNhhuRw3eAeq1aEG-r_SHBX6vMJ7tKWh8SoI3I1BlBM0ShmqhfiX71uSsRpX-eOZF7AtVDjIrcmNHg6mC6N7J5xhg6kHTDmzQ_nchD3aJ3TtkTaksHSjRxKu-5vMY6_D0dcq3h5zqVLUkD0PUZmKKmsmCvH70T6XP--ky0-_gjoj5nb3_rD9t4yyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvzTrinj1cKhMXS69P41LPtTj61n9mCbsBrm11iqVTn_0xPFRXKiDgyHy7jlWE1WhKUQdiPXU172TWXngR4UIbl8CWkKYGxp-lFcafoXc-tIiqhexTcp9kfvO3_O3ywN6KVNvVMta0PusD2Xbx0g3rfNektCfeLGeKRoOFbmmF7xoEG7JcslG8ruYEi2kQDuytQgmgqJUS-mxE1VhyFCa5EMV_cq2qKCL865kIkWjXPiRjaeAa6F2-_svoF1toC7rOz7PARBnjk5I4LywLsPz3d-2I6OppElc-jUNjJuiq4tvwTiWlCLPLkfjbKHqoDPWic4dJWLIQM3kCW3CjTjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromcина</strong></div>
<div class="tg-text">این برای امشبه؟؟؟؟؟</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/77659" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=SqC-i4lOdtN-TTAg9p5XDMZrlagK4CruAVfJvBxd0cgDwbbq6eyT0p21nYTWfoFwXPlKALBvshqzmQLOeIM66M7g7lO9-bLn_0oeakD2CBedQiO-aYlq4c_XVBfCbVI3lFzXGObD9Ed_f0svL2KDCZ5aOR5MeZggo8j3cGTysIXCiVfYfaO6nPiXrfo2p__Xy14Ix-Vac4zISto0Sjsqpkgbtud1kX_1pdn8z8hcoULfyWPiokGlt9PEW9xuJA4obestBJRhkaOOtaif6XsK9ZOxddEAFzmCP67G-AIEsGZlPl4xb6K0ymySqmqzY0f8ZRGOW0Y3tg9S2kkCdy2dnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=SqC-i4lOdtN-TTAg9p5XDMZrlagK4CruAVfJvBxd0cgDwbbq6eyT0p21nYTWfoFwXPlKALBvshqzmQLOeIM66M7g7lO9-bLn_0oeakD2CBedQiO-aYlq4c_XVBfCbVI3lFzXGObD9Ed_f0svL2KDCZ5aOR5MeZggo8j3cGTysIXCiVfYfaO6nPiXrfo2p__Xy14Ix-Vac4zISto0Sjsqpkgbtud1kX_1pdn8z8hcoULfyWPiokGlt9PEW9xuJA4obestBJRhkaOOtaif6XsK9ZOxddEAFzmCP67G-AIEsGZlPl4xb6K0ymySqmqzY0f8ZRGOW0Y3tg9S2kkCdy2dnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته  باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/77658" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته
باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/77657" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">توووی دروازه
مکزیک گل زد
اولین گل جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/77656" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جام جهانی شروع شدددددد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/funhiphop/77655" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqHaj9mjjeZSTeZ53c3nAWpREtY8igG7LReMvl3YiM2IePK0YdoBpW65wQveApjJ_iGwpPeivbvsWNQQBckUKUWWJ6wz978X9PHRs4c_KXeU3EPdNjudc7qMKul3xUpvDqpQ-c4PIUNzs5hWcl_wIZLOSVab4xvpLubTJViMgwvnrefSHS4FEkStiV8hEvQKTHMVe4ApNydXhFTG0JGbE5lQCuLs4lR3-k-qCsaL4caCG_sSwkhwyNsSYuJJZjca0i4vBhOmiokieKdsxnYE_pcFUZ64iOSWvpGwLfKoTRuh76GjJHMYkhxYBp5BcGbATtZ8GJqwp3jGNOaxoCioeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس هنوز نمی‌دونه توافق نهایی شده:
من از نمایندگانی بودم که خلیج خارگ و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پای ناپاک شما به آنجا نخواهد رسید و اگر بیایید، زنده باز نخواهید گشت.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/funhiphop/77654" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/77653" target="_blank">📅 22:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دالگخیز
🔙
عمو ترامپ  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/77652" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک تایمز: امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/77651" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به نیویورک پست:
توافق مورد انتظار برای آغاز مذاکرات هسته‌ای با تهران «تقریباً کاملاً نهایی شده است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/77650" target="_blank">📅 21:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیبالا هم از خودشونه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/77649" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ریدم
عادل فردوسی دیبالا رو بعنوان مهمون اورده برنامش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/77648" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/77647" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/77646" target="_blank">📅 21:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juG2IV81LYT0XvVTW8A7HTUIgupgD-ig63EQm_TqyHkfJdEpNvZ3Ep6FDIoXbEfoKRtXRZpuPlKBFxgbxYgmlxIpVn1F1q4EI4iutqVYZANYIJ41qQb61vbIOeI32fRusDD99cJ8Zn9nOG5ht0s6le9ZljdZjwkWAhS_7ttO-JXNdTCziVr-6lLK0uLUk12ruOFIqkttijQSalBp1pv_5pjaXp3oNsfw0r9wjPVAs7P_Hq0Wb1rGmqYhs1c6nazbSzC1drSxpWdNXyohefmK1bmznEoOCflZfks6TA_94abCjn0vOxoYvqW9jvmm0Sst9XYHFMCmdNdNP8H5Vyx_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل ادامه خواهد داشت — زمان و مکان امضا به زودی اعلام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/77645" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07. Pashmam</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/77644" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06. Adama</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/77643" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05. Khatereh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/77642" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">04. Setareh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/77641" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03. Tehran</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/77640" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02. Beef</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/77639" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">01. Dor Dor</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/funhiphop/77638" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBPIG8t8_6ZtTuNlxoKAeRDHknEg1Gh25z_VsN2Ep01z_KlAplDLNmzou7s2_vrDbV9rjzA4wjUWaWn68Wj9O5NuAXmAdBJZcO6SLPfFX7TgQlAHQUrFKJFVQayaOXGsc_iBwjxfkzfkSf_bUJiBCQji_Ct6g5vbHsvsUlpkMCgGHbhTBFmghsiQQnkIWGod8Vh2EX1zRB_xgNKBXcD8NjKscR0LT9XK_4jc1PIL61eLdCoK7Mj7DFVbINhmg2T5zK9qTCb8hhnt-NMeCnqPuepklcdohtkCnZAWZAjhs4GnCoXfpbtbaWrq_63t1TSRZ03F1lwH1Eh59ZLDX5KpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید مانیاک به نام تیریپ تو تهران منتشر شد
📺
YouTube
🪀
Spotify
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/77637" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بالاخره بعد مددت ها یه ترک خوب از تیجی شنیدم، همونم خودش نداده لیک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/77636" target="_blank">📅 19:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYC3xrw8HVoUKybKUesllK6YATQ-q4_bp8TaZaAEHRQ3Fvie9GjtJEyfMh55dPVqzM9-oDqWuJjXtJUT04A_WGIPJgJlEUljGgPW8Xz_ZnBglnmJbCxE_U2OFa99kghyQ1HRPJ8MPwEI2AeYZ4Bk4-FSz2RaPbQGFzxGSgq7QzcECfOyoS0ts-kA-YsWgc5YjZb3qjlqhs5BkE5HPfdULEcZkq8tPx8pIU1oc7hbjne7RqPbT61ge54_iEaOy59ojmlinP3mmXmeFp3VOXoyOkPQgb3JYb9Bx0f3Gi3IboBF29-0ZIQvC-zZ9Bb1P96tZeBPRydFFuI7tgFcFBSLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندساله که اسم توییتر عوض شده و شده X ولی گوشیه من هنوز توییتر نوشته، حس نوستالژیک و قشنگی داره‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/77635" target="_blank">📅 18:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رامین بچه کونی:
برای اتفاقات روی سکوها آماده هستیم و نمیذاریم بازی با انگلیس تکرار شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/77634" target="_blank">📅 18:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با اکانت توییترم که کنار اسمم
🇮🇱
🎒
🇮🇷
🇺🇸
هست،
توییت زدم وطنم وتنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77633" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLxXmW65FRVFEWs3xDhP_TS9BJzyJIIpPW-5x4VAf0_drpBM5DCoxjb4y6v0aqGJI02SXJqMpNg3yENpfZS7Hf1e7KrdK-T9o4qEDm6CJyrfbaFIoCzH1MhzwJflZxW6V78KLM6UvPLcFPE_HkOR-X9_PLqqBydZ4tbVfGwIGooUjWTw0dQY3dgbwslPtlhb9wPNr_ceHvRXSjBS2WwCBRF7DEnctk97n9d5pg9O9W8zlUpddJ5PDHAr6PaINoJqPTk8t2Y9Gat6bsB1O1RKs2Mk1TnMmSLxxor6-VwdjDkE4YpRbpCnkbkZY-1Jr94oILbR-3LhUcvB5Ul_nX23ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جون عزیزتون این چطور پزشک شده</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77632" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0UJ4N0dTukUJ95ZBzLZXHiB1yh92x0ct50fLCe9mFrH8XqK3X5BUKwfI8HMjMcafsqxWUXVcvrnUzZpjT7oCWzF3ZfDfi59SaPT4i53A8iYxoWlPn-H89moFJGTncO_3f7HrO-GqVj5vTa5lJnVmJhQ8Pm7Wwcm3dhCpn8xYnZaBZvQSHNPDgUI7MugXQEeJhNFn340YCALn6VNnZpQtdseJLihR8PdfTyIbJylIhe2Zu0xq1QFLrvrz5bZX0aJTJYXU3__s0c16ESAx7BpkBKH752eKU1YXBjxFaW1aZcFCyaQCkOcUqMBrgY-WhIpsw9v7EFU43efGYpmrXHHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام اسراییل برای حملات امشب لیست ترور داده !!!!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77631" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6rhph7xNVCLnasprwn-lL25Va6U86OKVXZGajtPe1YegkK0RNtP9Xjd71JOzcQQemIgH3PMnAnLj4vd8KF_sO8CyfzBVZM0i16keDb0PmgA7-WXP1VcC1Gwj6toniw5c9MUiC7ZYrWJ-GUEnJEQT-jG9xFTiagKh-52NKpDT0U_nWt7iDz9nOrMeMKoNuEr7F6BpnvEcxafl9Qaj98ABzptRoFulNs55IKwuAnffvY5kINJWzFWwLw7x4nNHaQofIsviN3f0XeVmHvvbUitgwSTqi5q9Wzs3O-0QyCKVpIf1T9eB4qW5iG9cs17OjtAMdTGJoAXPOxaThqUfGzm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد خیابانی : اسم اصلی من جمشید هستش نه جواد.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77630" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/77629" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3W18AGIg6LQoAtC_SVyCyQJsQ17BPaFHvxMMIB7nJRsraiC9i242mp_iSDon1KFwaM4IYKs5rAtqVtDE4jx-nqGxqWTGmA-OlNeVdJHP3xSKIdPCsZtNMwt7_1B5GxLecwtrkLwjM1zpVcB47-ZsZxSEt9oTXeNidB_OtCjERahlQhPxzRKrQBAgDfwUvMWK-i_45f8-7tZC_rAXc4-5aEmKUmdSGaTrsAknJ5c5bPg_9KC3P-tjdodWu6Bwzf9tl3Q_T47PoYILTPKLkQUagsbzJRhM83yWlITwrQoCTzv_M656PT2iG49dXI17beSANLcrHBz2RihxRx_0NMWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g21
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77628" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=aOBYFjvpB-THWFIAVqXo5nkW07_dlQwLWJugfkxQfUN1RSJylh9hzCMpLzJp4j2jnUbhkw5MlsbOUkvC2Q-T3hrcx7fD-exVNkxe05J6cJSutyWVbiHsdtuXo6tmjUsgZ2CccUuP_oSKdcgfMDbg1RCI-ylOt-o75IHnrcZH_5LhXNZnVuF-eXDOjlZTR3muSAlnSzY09xbvbOBRQPA7oV2tGlNZQtBfdyBiIzzBedyHnsbtwrn3Mr_luhRkGHwS2rYgK9qE8h6zaCfQ7jqSWOXpNZ2bYIdOFXSJ86ZoFjXICQc2enU5HIYyQPipMECFdrNCq9fo1BHEMm8nU96lww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=aOBYFjvpB-THWFIAVqXo5nkW07_dlQwLWJugfkxQfUN1RSJylh9hzCMpLzJp4j2jnUbhkw5MlsbOUkvC2Q-T3hrcx7fD-exVNkxe05J6cJSutyWVbiHsdtuXo6tmjUsgZ2CccUuP_oSKdcgfMDbg1RCI-ylOt-o75IHnrcZH_5LhXNZnVuF-eXDOjlZTR3muSAlnSzY09xbvbOBRQPA7oV2tGlNZQtBfdyBiIzzBedyHnsbtwrn3Mr_luhRkGHwS2rYgK9qE8h6zaCfQ7jqSWOXpNZ2bYIdOFXSJ86ZoFjXICQc2enU5HIYyQPipMECFdrNCq9fo1BHEMm8nU96lww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درباره مدت زمان جنگ با ایران:
من دوست دارم همین حالا یک توافق انجام دهم، کمتر از 3 یا 4 هفته باقی مانده است؛ وقتی این کار را انجام دهید، می‌توانید یک قدم جلوتر بروید.
نمی‌دانم آیا آمریکا تمایل دارد کاری را انجام دهد که من واقعاً ترجیح می‌دهم انجام دهم یا نه (تصرف خارک). ما در دو جنگ 13 سرباز از دست داده‌ایم؛ هیچ‌کدام در ونزوئلا نبود، و ما کشور را تصرف کردیم. در ایران 13 نفر از دست دادیم.
در ویتنام، صدها هزار نفر از دست دادیم. آنها دیوانه می‌شوند چون من سه ماه در ایران بوده‌ام؛ من آن کشور را ویران کرده‌ام.
آنها به من گفتند که شما گفتید سریع‌تر از جنگ با ایران خارج می‌شوید. خوب، الان وضعیت بسیار بزرگ‌تری است چون ما بهتر از هر کسی که انتظار می‌رفت در چنین زمانی آن را انجام دهد، کار کرده‌ایم.
ببینید، ما 19 سال در ویتنام بودیم و کار را انجام ندادیم چون رهبری مناسبی نداشتیم، صادقانه بگویم. اگر من بودم، آن جنگ را ظرف 3 الی 4 ماه تمام می‌کردم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/77626" target="_blank">📅 17:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=ItAQOBqTkvihxaRA3TfQQ496hYTrryT_iiEGp12nrve1V5rKpfK2Q0hNFQoY2eabag_5DUM93zGZXsHJv25PK0NhjH18Sh3Bd7nW_ebYg__fWei8F5GaePCjGOyoh1akmuQ65lnODDrnp40aUdqHh_iu1wInzk1wICA05a94DMntxjwSTXTbLji8L1dhe3HHnBgR38ptW8CIKUpHMMC9LKpmcoJ9xGcpIZdmoW6DAV3d3YoqT4sl7ozMboplXggxNJsl3SO83YSmObxHFojne7Z7OKOTtVKM-KvPWW7VFl-rpeJO1jCog_w1TF10kJ-F_IFvlQpP3ZPzIsZvGXDF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=ItAQOBqTkvihxaRA3TfQQ496hYTrryT_iiEGp12nrve1V5rKpfK2Q0hNFQoY2eabag_5DUM93zGZXsHJv25PK0NhjH18Sh3Bd7nW_ebYg__fWei8F5GaePCjGOyoh1akmuQ65lnODDrnp40aUdqHh_iu1wInzk1wICA05a94DMntxjwSTXTbLji8L1dhe3HHnBgR38ptW8CIKUpHMMC9LKpmcoJ9xGcpIZdmoW6DAV3d3YoqT4sl7ozMboplXggxNJsl3SO83YSmObxHFojne7Z7OKOTtVKM-KvPWW7VFl-rpeJO1jCog_w1TF10kJ-F_IFvlQpP3ZPzIsZvGXDF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درخصوص ارسال سلاح به معترضان ایران از طریق احزاب کرد عراق:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم؛ کردها ما را نا امید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.»
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند و فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد؛ کردها! من این را به یاد خواهم سپرد...
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/77625" target="_blank">📅 17:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee5717647.mp4?token=ZJSlwKjqLjdFEXGffO9y2HzQzU7g5ndSwqaLDbkLmy81jSrEjp9QgH4GmxVfiv4V8-d-F4ADZM_HEQE6VN1px69FkFMKLl8yjY1DkMLlD2j3JCYr4SE6vGWrmKebBXBkzFEYW_3DAFxDamMcV9SokS5uVeEqlsSwTx0jtn2OK5SDxamjuKJF3HI7pbsmsKsPLHyZ6Ya7_MiJDCbmExhmrPiwdnnSjWbWlTqv4hH1Bf3oQCr-LayD0F-VIILjxOMEi1SU1nJRbSQooeEQBst1oP7cmxgKKV1XRJKib7ZOcrYhocpmwH4DcN-lFrZ-SRYPDv5PNlQKU5kCoGmmIORtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee5717647.mp4?token=ZJSlwKjqLjdFEXGffO9y2HzQzU7g5ndSwqaLDbkLmy81jSrEjp9QgH4GmxVfiv4V8-d-F4ADZM_HEQE6VN1px69FkFMKLl8yjY1DkMLlD2j3JCYr4SE6vGWrmKebBXBkzFEYW_3DAFxDamMcV9SokS5uVeEqlsSwTx0jtn2OK5SDxamjuKJF3HI7pbsmsKsPLHyZ6Ya7_MiJDCbmExhmrPiwdnnSjWbWlTqv4hH1Bf3oQCr-LayD0F-VIILjxOMEi1SU1nJRbSQooeEQBst1oP7cmxgKKV1XRJKib7ZOcrYhocpmwH4DcN-lFrZ-SRYPDv5PNlQKU5kCoGmmIORtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز گفت:
امشب بمباران‌های بیشتر و قدرتمندتری (در ایران) خواهد بود. بزرگ‌تر، بزرگ‌تر و قدرتمندتر
فراموش نکنید، ما تمام سامانه‌های پدافند هوایی آن‌ها را از کار انداخته‌ایم و آن‌ها هیچ چیزی برای دفاع از خود ندارند.
منظورم این است که ممکن است سلاح دوش‌پرتاب یا چیز دیگری داشته باشند؛ اما در کل آن‌ها هیچ پدافندی ندارند.
آن‌ها تمام شده‌اند؛ اما روزنامه‌ها و رسانه‌ها از نوشتن آن خودداری می‌کنند. ما می‌توانیم فردا وارد ایران شویم؛ می‌توانیم سرباز بفرستیم. من نمی‌خواهم نیروهای زمینی داشته باشم، اما اگر بخواهم، می‌توانیم گروه کوچکی از سربازان را روی زمین بفرستیم و کل منطقه را تصرف کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/77624" target="_blank">📅 17:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfcc7606c.mp4?token=k-ujZpDVMRgrrzCPNHZ6trdXggeFELVhddQIR16R9len_PYMMZPNobT-zqAXsfh5Qu1BWLp3ECTlGqSSRP8n8If4c2rQXBBUhciyVq3FpRGpcn0XiVC2GfBSZ9E3AuIQTdzhEXn0PclNpIiCjpJaTGYQY_sLjz5BKKSEDr1RHkvjR0GZ0MNim1nVfYvGY2CH9JcfGnCgASGTzka0dXJh5xhTSjMO2_yR5tKo5zzzF7Gnx9WeWbuQthvnTyn_2SHBIXEr9nyMtzTsDjmkDiyAttnKeOrrDHkN-RmhhXj6KZVlZqfLuYcHffyS5dl45J0LRO4Y_FoJwoTjS2h26NMvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfcc7606c.mp4?token=k-ujZpDVMRgrrzCPNHZ6trdXggeFELVhddQIR16R9len_PYMMZPNobT-zqAXsfh5Qu1BWLp3ECTlGqSSRP8n8If4c2rQXBBUhciyVq3FpRGpcn0XiVC2GfBSZ9E3AuIQTdzhEXn0PclNpIiCjpJaTGYQY_sLjz5BKKSEDr1RHkvjR0GZ0MNim1nVfYvGY2CH9JcfGnCgASGTzka0dXJh5xhTSjMO2_yR5tKo5zzzF7Gnx9WeWbuQthvnTyn_2SHBIXEr9nyMtzTsDjmkDiyAttnKeOrrDHkN-RmhhXj6KZVlZqfLuYcHffyS5dl45J0LRO4Y_FoJwoTjS2h26NMvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز:
پیام من به مردم ایران این است: آن‌ها می‌ترسند چون اسلحه ندارند، و طرف مقابل اسلحه دارد، و آن‌ها اعتراض می‌کنند و تیر می‌خورند.
رژیم ایران حداقل 40,000 تا 50,000 نفر را کشته است و مردم می‌ترسند. می‌دانید، وقتی یک مسلسل روبروی صورت شما باشد یا وقتی چهار تک‌تیرانداز در چهار ساختمان مختلف به سر مردم شلیک می‌کنند، برگزاری اعتراض سخت است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/77623" target="_blank">📅 16:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار: یکی از چیزهایی که دیروز مطرح کردید این بود که اهداف بعدی، پل‌ها و نیروگاه‌های برق خواهند بود؛ آیا این مرحله بعدی است  دونالد ترامپ: ترجیح می‌دهم این کار را نکنم چون وقتی این کار را انجام می‌دهی، مردم هم آسیب می‌بینند. مثل اینکه شنیدم شما به آب اشاره…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/77622" target="_blank">📅 16:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4e5f9e8c.mp4?token=tuM72tDjQrqtT-hKD-GV2u1YqmLR2vpCrkb23EwNFsypjZNRRPyq7PGMSdEapsMJMnFrDxCERBAjrDyuQgDYtW2adl4SXfLPGQ_9vIooSwuZdgsS_Sx3AJ7cHH9j5Umr43oMl0bYayOGG8dXPFO2dVhBrUjGIgzBvBQ2aP4ytIWQ56B6NpJCfizFJLqSwcyzeayUTV4mdhUUMJzCbJW2AceSu0iZ8YgUfgaFV2mTN72HieLFLyZ1xkv5_K7qn9-8HvvCwd5qImtSfEVDg0GJ9e1k9OgaXtK2NxKkZy3OPtiKDotzwQdQc03bDGIqYcsT-0m9u8biUj8zuDUf75UeZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4e5f9e8c.mp4?token=tuM72tDjQrqtT-hKD-GV2u1YqmLR2vpCrkb23EwNFsypjZNRRPyq7PGMSdEapsMJMnFrDxCERBAjrDyuQgDYtW2adl4SXfLPGQ_9vIooSwuZdgsS_Sx3AJ7cHH9j5Umr43oMl0bYayOGG8dXPFO2dVhBrUjGIgzBvBQ2aP4ytIWQ56B6NpJCfizFJLqSwcyzeayUTV4mdhUUMJzCbJW2AceSu0iZ8YgUfgaFV2mTN72HieLFLyZ1xkv5_K7qn9-8HvvCwd5qImtSfEVDg0GJ9e1k9OgaXtK2NxKkZy3OPtiKDotzwQdQc03bDGIqYcsT-0m9u8biUj8zuDUf75UeZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: یکی از چیزهایی که دیروز مطرح کردید این بود که اهداف بعدی، پل‌ها و نیروگاه‌های برق خواهند بود؛ آیا این مرحله بعدی است
دونالد ترامپ: ترجیح می‌دهم این کار را نکنم چون وقتی این کار را انجام می‌دهی، مردم هم آسیب می‌بینند. مثل اینکه شنیدم شما به آب اشاره کردید. آب واقعاً برای آنها یک خسارت ویرانگر است. من می‌توانم این کار را در یک دقیقه انجام دهم، اما مشکل این است که مردم قادر به نوشیدن آب نخواهند بود، بنابراین نمی‌خواهم این کار را انجام دهم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77621" target="_blank">📅 16:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ باز از حکومت ناامید شد داره خایمالی مردمو میکنه</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/funhiphop/77620" target="_blank">📅 16:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا فرستادی واسه کردها؟ میفرستادی واسه بلوچ ها</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77619" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: کار برای ایران تمومه. امشب بمباران بزرگی انجام میدیم. اونا میتونن پرچم سفید رو بالا ببرن و بگن ما تسلیم شدیم، آمریکا بزرگترین قدرت دنیاست، الحمداله. واقعاً دوست دارم همین الان با ایران توافق کنم. هدف بعدی ما پل‌های ایرانه. من نمیخوام اینکارو انجام بدم؛…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77618" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: کار برای ایران تمومه. امشب بمباران بزرگی انجام میدیم. اونا میتونن پرچم سفید رو بالا ببرن و بگن ما تسلیم شدیم، آمریکا بزرگترین قدرت دنیاست، الحمداله. واقعاً دوست دارم همین الان با ایران توافق کنم. هدف بعدی ما پل‌های ایرانه. من نمیخوام اینکارو انجام بدم؛ چراکه باعث رنجش مردم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77617" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این ترامپ مادرکونی هروقت تهدید کرده نزده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77616" target="_blank">📅 16:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بنام خدای رنگین کمان، تولدت مبارک کیان.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77615" target="_blank">📅 16:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT1jm4dJ_Y1VAeYwAKLKu7F3WlNClA7D69-hqtCfIJGXH2pheFgxUA_8Qf0VTOYUsvtaBiESQf7xwFgrzwHpoOVD_XAwLul8DTnxeQ_12b7ISQ6CBsliRkYIEhI1HqTfaRPKJFpvBIKsbzcpP-_zqFgEZDagOKI4f4uxYsnG_2JySY57OIwgVaxtr7sO0IP00wfyEaif5qDAIlbLX3fa3qW89jv26f425wb60Fn4S5wleo-UUYMhhb6M7iKHV33fnUBa9R_s_A8DNbLY-ck5EfgjK3COdpjfp8I9tnk40oneRbBmedOCh6BGzijWYrAP-58Phn4ZVrPPTaTQCQQlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنام خدای رنگین کمان، تولدت مبارک کیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77614" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:
ایالات متحده امشب بسیار سخت به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش اعظم توانمندی تهاجمی‌اش از بین رفته است!) ضربه خواهد زد. در زمانی نه چندان دور در آینده، ما جزیره خارگ و سایر نقاط زیرساختی نفت را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت؛ بسیار شبیه به کاری که با ونزوئلا انجام داده‌ایم، که به شکلی عالی هم برای ونزوئلا و هم برای ایالات متحده آمریکا در حال نتیجه دادن است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77613" target="_blank">📅 15:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R93uvSafUarEoPJLEfd-Nd8IoJlwv1tes1L4t2b85lyl30Sz7D-vCGAJkVQg_FB9mTf2kcQ4tNvr3pnceTz2tKj0E_I44imgclqNqvX5DDUURi1eOmagnK8oJt1mUtmnJRJ9-qYDqtI9Twr9hl_EGn_5lvEtN2qGKvLVuO1okkzp_CVHogFRlvycbx4xV56_egeI94oxwNyEzMEGAYWxIU02uiP11yDaE8_iGM2dbAFCTG4Cqx0p2P9QV5SbJYuanI9-MUHsaxsdgHrLTkMv4erDcMOxe8wFyCkzNuiFDT2rIPBPXHIjVUkxz2GWVDqlcKA31Sfn8rAvdU3EcvM6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای جام جهانی آماده اید؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77612" target="_blank">📅 15:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfgvTIb5exvewCp0hEZoQ6NdANpl9HP476xgfkzamccxw8hpV0E-8sgNFoT3e0GQIMSgke5-Z1JGH_cIbSKx403fNf3736Oh8_z9U1Qjr3IFnrvX4msc4cjbC0M5qFLkLScmvigPgZlkOoqtJDac_eSM598k3wQzaSSPgR5wKz39Iy0W_WApW3yzCuoWaOz2uc0U_7VkQr_DfJdK-UibtFgfR2dMLICGHprSu93jmyFwAE8zgDl4LT7u6-F4SOMyeiTr_6z14BKn2--NIR6Y6V6LfMqt0HMOHLHZwKpZpiPYwo6eTTs9kivVIUlJj0Eng7wWS47N8M2NZael6-weuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77611" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YczWgA2KZYSNilyGNB_6TZ0CBXSTv6-dZmxRnHX-yUnTsE11sRluPB_JbqDeQoQrKLmSoki5btzizewoyH5UXemDsRPl9bZPog9UMkdUxd6wt5mnOK1x7bMvBQnd7Rl4paymFspZpz4dg49P69Pq_CflGAHyZajKvhXGWLcubDC5Huw4NnJobeAKhHIKWSEnSZYEaTLdcaD7dJOTkq7epvssjSnPxC4mKli4MfW5InR23Xr3K9DmTHpthgpVQStUkuqdIC7pC2USt3g9BFok9wUbMFIT_BqQQhBmUY1gI7laRW5u5MdF0xOtiGdWRyIM4g6Kvo5rLwVtXmI3SKcb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب داشتم این صحنه رو کابوس میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77610" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfHt1Q19baZo1Vi95MymRsCCNjTrSYl89DCmM7drnh8yefOAPUxmjuHwg6JSaXefHtn1v0Drsap077pO7WN3fS6-TFIElg1EWyDn4QxCGSEDQ8FlSCKAkFuYoSLoq_IAdlRxZLsmcaDJGcrtsC2fp43guwqGPBeB2SL9yPjl8Dnx2SRxP9mFwzWAqvcHkpsNM1QGiLG65u7sEze7x5i73nzYn0sSBs-5FO3BP53SGe9kro_zj4jcHnKzIILQDQn6tJsIK2VT6Oye7wXLiYMcQRs96XfaYUAtiE_ep10mMnexY4GTiMR5hvHu6sosv52q_9ToBNBWTQ0cAhvMEPjdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 گیگ فقط گیگی 2/800 تومان
💥
💥
💥
100 گیگ فقط گیگی 2/990 تومان
💥
💥
💥
50 گیگ فقط گیگی 3/600 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77609" target="_blank">📅 13:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک خبرنگار آمریکایی:
ترامپ از تبدیل رژیم در حال بررسی سوییچ سیاسی به تغییر رژیم کامل است او معتقد است جمهوری اسلامی هیچگاه ممکن است حکومتی اهلی و عاقل نشود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77608" target="_blank">📅 11:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نقض نقض نقض، تا روز آخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77607" target="_blank">📅 11:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دریانوردی هند : سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش نزدیک تنگه هرمز کشته شدند.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77605" target="_blank">📅 10:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi3gPP6BTipbVWrlVc8vXM8Qi0kCE94MQL36fsnqa6oG-uBNN_iE_wNVwdyCgigXkVtxhU-zW9RZtCRNBtWU_1Ol839yT4eTStQ-hpALaj5EEEi6Ckd_mHlA9xhlfz9sllA4PpaO2X5b4gL0ykJvtsUv8w4y7INb03mIAU8fd5EgnV-z65tlYTjf3i-uRIWzVsoIm0v0yuT6JeRLwhY5LUhtvNDeSHutyo9PQcx8AqYZH1C-Wtru1ZtAMkOt0KT6q_sB6oZxeys1eCdumhPHWS4lFb_0xRCXS7qCelCbzd0UGf--QpRAEN6hafIh8tmEzbJfJBf4vKyFchB7EMtWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت یاس از ترک جدید تتلو :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77604" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77603" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNL26qRNu9gQ9QahFy-gqLOLpDE6pUNz2rANGrZi7dXB7b-mziXu0QvB5kI2cE3QjeDwi7aSMf3BuLhaFnCXQghzYVNlONp9cg9_4PZ40K_C2W29lxLx9Z9RHsnGzK4lSlpIt28r5Cr0_X8mWp7XMZY1FQ5EjRDc2kZ8pShfJLLuWyEIu8jhrlNhMvkJ0QvGpfwfvuVJfzfEnsBB9Avo2Ikca3ZpK461AjfPZKfB5s-RzN3Ui5ZI4Dr9uj_JtRVOAkEc6nSpnmxpkDaC0oMssm8MrXeUlw72ukjAeZ9o4RQeXmP4G16SY6QSAD1BycXxKF4wNlwG1s3KPWl55NEL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r21
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77602" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57acb15649.mp4?token=A3OoKA_rkdrQ2zUSRCisl7uRSJ900T4qCoAW4igHh1nnarcMJ3HBgU85HJwJ1Zc7RbeaYu5qORb6Rge9HJzVDS3P4Y1Exo1BZzs9k_W9bvO5ROPHgNu4g833_GchUjhOqXNVgPTVDOlsEfkhMLUa_zaXPrIhah3n3adPRMS0lWRij3TBiwdUJvBcpiFM-ZGToCTj98whu2yJdVRJW3WSKhHe2rzsXG7321Dp6NeQCEZPrFsOd8M8RQx-j_aocQ5XfhXPa8VMoUVlajyM9oe5FwnX7m66hyS0zpg2saEpVT6Y3OUsdYiNh_O9fTVMMtDxBPilyrlKkhEW2u2TLe5h8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57acb15649.mp4?token=A3OoKA_rkdrQ2zUSRCisl7uRSJ900T4qCoAW4igHh1nnarcMJ3HBgU85HJwJ1Zc7RbeaYu5qORb6Rge9HJzVDS3P4Y1Exo1BZzs9k_W9bvO5ROPHgNu4g833_GchUjhOqXNVgPTVDOlsEfkhMLUa_zaXPrIhah3n3adPRMS0lWRij3TBiwdUJvBcpiFM-ZGToCTj98whu2yJdVRJW3WSKhHe2rzsXG7321Dp6NeQCEZPrFsOd8M8RQx-j_aocQ5XfhXPa8VMoUVlajyM9oe5FwnX7m66hyS0zpg2saEpVT6Y3OUsdYiNh_O9fTVMMtDxBPilyrlKkhEW2u2TLe5h8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77601" target="_blank">📅 09:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی: در جواب حملات وحشیانه رژیم جعلی و آدم‌خوار آمریکا و به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، با ۱۲ فروفند موشک محل استقرار جنگنده های F35، F15، F16 آمریکایی و همچنین…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77600" target="_blank">📅 07:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم امشب تغییر رفتاری از سمت ایران رخ دهد.
اگر این باعث نشود آنها پای میز مذاکره بیایند، باید استراتژی خود را تغییر دهید. تمام توان خود را به کار ببرید. آنها را از پا درآورید.
بگذارید مردم ایران به مرور زمان کشورشان را پس بگیرند.
اگر آنها همین الان توافق نکنند، باید اسرائیل را در مسئله ایران آزاد بگذاریم و خودمان هم از نیروی نظامی‌مان استفاده کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77599" target="_blank">📅 07:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75edca7aa.mp4?token=KKqBfwg3XjU_9Fr0Y9-NWshlr9rIY1-uAl9S8QzqshWMrJBWVQPRyE1da-lwV6nJDG9z8JMSFr9Oofr8d5zUJakBfzOB8aLAhOVY3Tq3ohzqSf07g0k0FrNSLfgB1x6KTOetMGpLTO2AyRNftHkNbtTxrObe1_i2N6BWW2g2OxdKSS6gPzb9FhnSPMp60cSzq5nOPaZUY4wXjYpRqDEKAtDspuCz032u_4aoXdNWokjOm0kzoSKFs1O_2RHu-gRxCg_5eBQW09Z1gSpt3ENUDjzQDTkrk-ayEMhJD9j2r7IOoVR7tiYHgSQKIY-5XFvRDmcTUFqTs9xQ7ae-L0cnXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75edca7aa.mp4?token=KKqBfwg3XjU_9Fr0Y9-NWshlr9rIY1-uAl9S8QzqshWMrJBWVQPRyE1da-lwV6nJDG9z8JMSFr9Oofr8d5zUJakBfzOB8aLAhOVY3Tq3ohzqSf07g0k0FrNSLfgB1x6KTOetMGpLTO2AyRNftHkNbtTxrObe1_i2N6BWW2g2OxdKSS6gPzb9FhnSPMp60cSzq5nOPaZUY4wXjYpRqDEKAtDspuCz032u_4aoXdNWokjOm0kzoSKFs1O_2RHu-gRxCg_5eBQW09Z1gSpt3ENUDjzQDTkrk-ayEMhJD9j2r7IOoVR7tiYHgSQKIY-5XFvRDmcTUFqTs9xQ7ae-L0cnXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
در جواب حملات وحشیانه رژیم جعلی و آدم‌خوار آمریکا و به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، با
۱۲ فروفند موشک
محل استقرار
جنگنده های F35، F15، F16 آمریکایی
و همچنین تاسیسات مهم ارتش تروریستی آمریکا را هدف قرار دادیم و آن تاسیسات و مقدار زیادی از
جنگنده‌ها را منهدم کردیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77598" target="_blank">📅 06:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77597">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie6pjcWSJu6v9Rl84E_QWBYejTLYIycdcjEGTfbCz_rThN4wr6VFp5m-kM0PYm5xyHOUpufePPTQdiu-oIE9Tec-S3_BOphjMSrqOHNyc_bQr20CqdAY76YCRwNi-Zb6NYUvST4um-TtlPkLU1FdV1zLjFmD_JjSuIiF4lSpNGzv82ooEzM6b6nKr_2v9hl-PKHIrTEA47BYX5dy6zz8vGxI8r4BzksWOcRuh9bfihy2LtYizsoRWMhdBSrj9fuJaNcIGxpo4gbeT1H88Kwm2DDPjJiDZC83Hh-QNiEGU7DWLF0YSp6GNdKY82_VVV8BNYkyKTtUHJ7gUuub7FQl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل نگارش کپشن
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77597" target="_blank">📅 05:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77596">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77596" target="_blank">📅 04:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=i0jYMnOuUwFLX-UbdKCGr61PCExzkBij2mZrmD5MC17le5e32gy-Bt3lvUwSMmskEn0r8CuZVyIEXRWMJfHjduiH69HsPna0Y5ehO185UlatcOrONAJ6pv8HbW0d3qsDBrSR9PZ-IogrqFxTnt8Z43Fr9iSwskK3Dbc3mt48hRq4f2BgFbP9mxNfOYmeUsKmaIQRRqza4EypVuHyzFbP23IsU2mn_mEzPR_fUDcpCcRPBjSkHVuemPjixngmgK6auCL5WxEmalLDgHqhq2NMD-vgNlOktRFBiQkIQo9_NGRmXE-1VR9SZauLqhQ69G0ZWNX1v_mjERId4-4bhBYOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=i0jYMnOuUwFLX-UbdKCGr61PCExzkBij2mZrmD5MC17le5e32gy-Bt3lvUwSMmskEn0r8CuZVyIEXRWMJfHjduiH69HsPna0Y5ehO185UlatcOrONAJ6pv8HbW0d3qsDBrSR9PZ-IogrqFxTnt8Z43Fr9iSwskK3Dbc3mt48hRq4f2BgFbP9mxNfOYmeUsKmaIQRRqza4EypVuHyzFbP23IsU2mn_mEzPR_fUDcpCcRPBjSkHVuemPjixngmgK6auCL5WxEmalLDgHqhq2NMD-vgNlOktRFBiQkIQo9_NGRmXE-1VR9SZauLqhQ69G0ZWNX1v_mjERId4-4bhBYOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام الان با انتشار این فیلم مثل دیشب اعلام کرد که فعلا حملات «دفاعیش» تکمیل و تموم شده تا ببینیم چه پیش خواهد آمد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77594" target="_blank">📅 04:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77592">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">احتمالا الان آمریکا داره خود زنی می‌کنه که حملات سپاه به کرج فراموش شه ولی نه ما نمی‌ذاریم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77592" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77591">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قزوین و مناطق مختلف جنوب کشور باز صدای توقف حملات اومده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77591" target="_blank">📅 04:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77590">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx6-lMvE9O3MJ2TDaAuwCvtXIPLqywFQJFm_podV4xCotIsemFgtdstEvPipg-3-Ms9fKt81MPIHxRD7Wp-cwEYpfNNlPl-UxJSQYMX9bf-MtiI7-0LM3udfAmgJdNylnAmMmVvNE1Q6izZ7m7vs6x6WGVXVx12udkdWg5_4joQMrsTF6LrTVEXNcYLZ90Gt51pZMd30K1TNUGTO72JWydulJxH0XQcRC7tAqib9lhTxextqutzw_YHXxc1JbFngqGo0IbYae877R-xOm742oIErISpk5GVeqcpTeX9yKEE6Xzoeoitv5Wj1zTzxfUW80b_QPDeMZjs-8rp5b3Fosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید بالاخره بیدار شد:
تنگه مقدس هرمز را ناامن می‌کنید؟ از سراسر ایران منطقه را برای شما جهنم خواهیم کرد.
این پاسخ به جسارت آمریکایی‌ها در منطقه است، ان‌شاءالله.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77590" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77589" target="_blank">📅 04:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77588" target="_blank">📅 04:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اوه اوه  هشدارها و درگیری پدافند در بحرین.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77586" target="_blank">📅 04:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اوه اوه
هشدارها و درگیری پدافند در بحرین.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77585" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77584" target="_blank">📅 03:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77583" target="_blank">📅 03:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صدا سیما به نقل از سپاه پاسداران انقلاب اسلامی: مهر نیوز راست می‌گه، سپاه پایگاه آمریکا تو بحرین رو با پهپاد زده ولی بازی رسانه‌ای دشمن کاری کرد شما نفهمیدید.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77582" target="_blank">📅 03:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946d468c47.mp4?token=EpPgSspgCFQ2ZoXm019_Jk-DBNmFMZlyuaA84yRshs6_TMarjo7O6Oon72ge_nVs-1b9NMvfQY7_qfAzdjvS_mul5XMpVxQcywh1mcdzedrrRC5zClzk1P33JjHiKhBLL36XAkhDO2bDNz6ZMwq2uRZcxeT5Zsi3Ng5VGaSh3lco_6bUsHjkgK3HR0VaQcGJMC2gqcYqmByMgpAtQkACIfVPZ9rDJWqY8jNjSxkdXXC2UbIZxp0NXzOy739M1ZBhXw66CcRdTUX_PI7U2hRXIuNqXM6z-9O170vzzroUDys0akhLKjcvKpQgcXS3Q9Q7LxWEvh2Zm437oqJmOMpW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946d468c47.mp4?token=EpPgSspgCFQ2ZoXm019_Jk-DBNmFMZlyuaA84yRshs6_TMarjo7O6Oon72ge_nVs-1b9NMvfQY7_qfAzdjvS_mul5XMpVxQcywh1mcdzedrrRC5zClzk1P33JjHiKhBLL36XAkhDO2bDNz6ZMwq2uRZcxeT5Zsi3Ng5VGaSh3lco_6bUsHjkgK3HR0VaQcGJMC2gqcYqmByMgpAtQkACIfVPZ9rDJWqY8jNjSxkdXXC2UbIZxp0NXzOy739M1ZBhXw66CcRdTUX_PI7U2hRXIuNqXM6z-9O170vzzroUDys0akhLKjcvKpQgcXS3Q9Q7LxWEvh2Zm437oqJmOMpW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر: سپاه امشب هم اون وسط مسطا پاسخ‌هاش رو داده موشک‌هاش رو زده باز شما عقب مونده‌ها داغ بودید نفهمیدید: مرحله اول عملیات های تهاجمی موشکی و پهپادی هوافضای سپاه انجام شد.  پراکندگی مبدا شلیک ها و فراگیری بانک اهداف، جزو مهمترین ابداعات عملیاتی سپاه…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77581" target="_blank">📅 03:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/77580" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77579">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77579" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کرج زدن؟</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77578" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77577">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید: در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77577" target="_blank">📅 03:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: اگر ایران توافق نکند، فردا شب دوباره آنها را به شدت بمباران خواهیم کرد
(I will bomb the shit out of Iran)
.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77576" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77575">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnXyh81RM9oeTRy0NLCMp9UIAlRKH1tyZ_S35GY7RbrJ8_-zkB6REJmWVoavG9HxwvsxBqZPU2vZXKToTJJ6s-qI1rCAlpW367Vwwc949yndcf7b4VYzPVge3r-9fAkmB-rL2VfnBSleF9IpGvUizRy0reTVOvyGSrheteRswLCMV8rfkoqEjaD6rpAjgDig4fJhmPKQtZ3Yvbi3brW-pj1RccsOCAOaIJjHF9G9elR3Vv0fX43X5QPpDdhCmMmrw7msw_8gyFIbMKSthTXY2Bz5kvU_M7Oaul4QNIcEkayFZgCx7EGhgChffDgtRN3WyN0oH5LtgmbIj1kA_HC1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/77575" target="_blank">📅 03:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77574">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به فاکس نیوز:
این بزرگترین نقض آتش‌بس در تاریخ جهان بود.
(ولی هنوز آتش‌بس سر جاشه حرومز؟)
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/funhiphop/77574" target="_blank">📅 03:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77573">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: من مستقیما با مقامات ایرانی صحبت کردم و آنها از من خواستند که بمباران را متوقف کنم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/77573" target="_blank">📅 03:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77572">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: اسرائیلی‌ها در این بمباران مشارکت ندارند. من درها را برای بمباران بیشتر باز می‌گذارم اگر ایرانی‌ها درست رفتار نکنند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77572" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: من مستقیما با مقامات ایرانی صحبت کردم و آنها از من خواستند که بمباران را متوقف کنم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/77571" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/77570" target="_blank">📅 02:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
بمباران به زودی متوقف می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/77569" target="_blank">📅 02:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یدیعوت آحارونوت: احتمال آسیب به یک ناو نیروی دریایی ایالات متحده پس از درگیری‌های امشب با سپاه در تنگه هرمز وجود دارد.  گزارش‌ها هنوز بسیار تأیید نشده‌ و احتمالی هستند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77568" target="_blank">📅 02:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک مقام آمریکایی به فاکس نیوز:
حملات نظامی آمریکا به ایران همچنان ادامه دارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77567" target="_blank">📅 02:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پاکستان: به آمریکا اعلام کردیم که دست از میانجی‌گری برمیداریم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77566" target="_blank">📅 02:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77565" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77564" target="_blank">📅 02:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77563" target="_blank">📅 02:16 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
