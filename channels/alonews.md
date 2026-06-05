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
<img src="https://cdn4.telesco.pe/file/J5JFblfJNQ0YddQag41ngFPQkhZvh2zSv_kGiAH0vfEVFePHuXB8CzSGsoUWq1K4o3DPntHCy4ak969KYBLI5w0fW5qIz6KgeXTpNzkjXRIGpSQBIkyNnlqNPmu264xizUyvl-oyzyXMOMHAZIYEIPoouNlRQ5O1xdVXVbsYlHAkZ6o756hDQpH9xHeZTuIbeHRP613B53TITNdDQJ-F-CGfbSQd3e6fk0Xqxi11-QUKazIxm-djYhopthDO8ECfOefsjT4wQA9shx3ZwVnEzKUP0S1r66WZ2oV_LwcE4BS5AkByp29x4t_uU0R_DbmQhxLHyN1kHh1lmAgq0R_lJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-125286">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
حمله اسرائیل به المجادل، منطقه صیدا، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/125286" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125285">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گروسی: از سرگیری فعالیت‌های ما در ایران برای ارزیابی فنی دقیق وضعیت ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/125285" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
در حال حاضر در مذاکرات جاری بین ایران و آمریکا مشارکتی نداریم، اما می‌دانیم که آنها به دستیابی به توافق نزدیک شده‌اند.
🔴
راه‌حل بحران ایران و آمریکا باید دیپلماتیک باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/125284" target="_blank">📅 15:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125283">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سازمان ملل: در صورت ادامه بسته ماندن تنگه هرمز، ۴۵ میلیون نفر ممکن است با ناامنی حاد غذایی روبه‌رو شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/125283" target="_blank">📅 15:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125282">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کلاس‌های دانشگاه شریف حضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125282" target="_blank">📅 14:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125281">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نبیه‌بری ، رئیس پارلمان لبنان: آتش‌بس باید کامل و بدون شرط باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125281" target="_blank">📅 14:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125280">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecn7a6zqcMxv6UYpcdVlIQzs1FSGcxPbUfE7RqyWBKKUm9-iuDCTW7fDl3WZZPFCyN3oye55Vt6xvPE-VtVhkeBeddCGf8ADEHFQGrpNf6CPBSP9DKoVKf6nNNnA85Qc72IiRd7806wQLTW4L99lNrCU4iaDt5zRP3vI-6tjD676UAOvUhKECNZX8zZNZ8OedBJVCJaH312VYzKsbnX_2aWTKOj_YyBRlNCfY8zjbtlzCsdd1RNRr81q_3SVmG2El03D2NDGUim2PeU_fKwSfvHTbKiHj3w7w34uVnXiV5vBTy-TIQDPJaY9gx_GWVZd8qisNokF_GVEkagMELtKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تا دیروز، تقریباً ۶۳ تانکر نیروی هوایی ایالات متحده (KC-135Rs و KC-46As) در فرودگاه بن گوریون اسرائیل مشاهده شدند
🔴
هواپیماهای نظامی ایالات متحده بیش از نیمی از جایگاه‌های پارکینگ فرودگاه را اشغال کرده‌اند و عملیات تجاری در فرودگاه اصلی غیرنظامی اسرائیل را مختل کرده‌اند
🔴
با وجود گزارش خبری قبلی که ادعا می‌کرد نیروی هوایی ایالات متحده بیشتر هواپیماهای نظامی را از فرودگاه بن گوریون خارج خواهد کرد، چنین اتفاقی نیفتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/125280" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125279">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObSrG6FvIHbNlWMtMftosjnLhbOCEBphb2pA_F2bMYMfBAz-5pFw-8Tnl2eM06usdjdVsYS0pR8QW_iZpL7jSPJ08XCK4n2PxYitgUz0apBJLsjLK-8EwheAO2bSDej9DJf0VrVOMZOncuBC0DbBVGwAPwy1NNvgcCx7LJeBppTlI3Y_tLgU4Aw8cWy_leemaNsSqAhj_hGULs9CyQcCFe7c1T6DlzmagIiDg7bVJElsg8YzaVMj47K2DNsJeNzD2e9OZPayUXrtgTcCM4zWPR9h19slK0peiSJC6_bvvDU5JzH9hvCmZUmwjpXA0v6fAU9ARqoA2OVQaYWmhzzNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125279" target="_blank">📅 14:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125278">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
العربیه: اختلاف اساسی در مذاکرات، آزادسازی دارایی‌های بلوکه‌شده ایران است.
🔴
روش و سازوکار آزادسازی دارایی‌های بلوکه‌شده ایران، یک شکاف (اختلاف نظر) در مذاکرات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125278" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125277">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کرملین: احتمال دیدار پوتین و ترامپ در تابستان ۵۰-۵۰ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125277" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125276">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnt6sGSk7LyHAfT01hcLp0M4mJRHgRAqMK5UGtQfI1MX3sJGMFAUBkciem5iLmnxfxVK4pRut80GQUfSd3FLacYs-M0JyLAR46A11lOX9iA-k_iCUrQ-4sDyBDOE1majjGY1NbXCIKGKqOLAXKV-uFan55xM6sizPDD-zP6b7Q8hpyD0s1oUEnV-DyJujnjtRcYddqLIi-wPFoEqtMXC2vPJASPtX4vzoZJwcU7NoIxbALHYClK2O6d2zyXCUU4-H-32cj6wy771LsHAoIorPHM9It3gw5n4wgt0QdBi3ewXWf6-PdeSSzq2ni8joAoJn9jGNKLKdo19i0I_wJ__EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر سکسقیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125276" target="_blank">📅 14:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125275">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
جمالیان، عضو کمیسیون بهداشت مجلس: میزان کشت خشخاش در استان‌های ایران بسیار بالا رفته!
🔴
در استانی که قبلا برنج می‌کاشتند، امروز به کاشت خشخاش روی آوردند.
🔴
با توجه به اینکه این محصولات خالص‌تر هستند، قطعاً شدت اعتیاد را افزایش می‌دهند.
🔴
خشخاش‌هایی که [غیر قانونی] کاشته می‌شوند، جزو کشفیات است و به کارخانه‌های داروسازی تحویل داده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125275" target="_blank">📅 14:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125274">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت خارجه جمهوری آذربایجان اعلام کرد: در حمله پهپادی شب گذشته به دو کشتی باری خارجی که ۲۵ شهروند آذربایجانی داشتند، پنج نفر کشته و سه نفر مجروح شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125274" target="_blank">📅 14:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
العربیه: ایالات متحده همچنان با درخواست ایران برای آزادسازی دارایی‌های بلوکه‌شده مخالفت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125273" target="_blank">📅 13:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ماکرون، رئیس جمهور فرانسه : جنگ اسرائیل و لبنان هرچه سریع‌تر باید تموم شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125272" target="_blank">📅 13:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125271" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=HHpP4GVX1DZ3jyZyRk01zttcAkAWje7qtc-geiPPSRgZIFPkbPdbTcxtd2q7hk3TVJXdgMhDGZmUSu-qOndeIZqkGDhpVKBLILh8LXvDZT6ub8vZYZqyYOfc40L8wZigTC7cXc0dnOHJB_SnKrBpNWm3-jALxfdIyCmKVvsNC97VfOcYauuw8PimL5khgI3HiWzNG6NM-uIe-CaHU0q45K-WlWmiebOQXUdPVLjZ6FQd9a_bFSX-aPHQJ49wkWPOhzQk0PfPEP4dYSeN7ITQgij2kSUJHO5AAUE4tf_A_RYYjBd7CMFNNIZOLL7NyOSEk1UESLKP-ja5fQfGJJQ5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=HHpP4GVX1DZ3jyZyRk01zttcAkAWje7qtc-geiPPSRgZIFPkbPdbTcxtd2q7hk3TVJXdgMhDGZmUSu-qOndeIZqkGDhpVKBLILh8LXvDZT6ub8vZYZqyYOfc40L8wZigTC7cXc0dnOHJB_SnKrBpNWm3-jALxfdIyCmKVvsNC97VfOcYauuw8PimL5khgI3HiWzNG6NM-uIe-CaHU0q45K-WlWmiebOQXUdPVLjZ6FQd9a_bFSX-aPHQJ49wkWPOhzQk0PfPEP4dYSeN7ITQgij2kSUJHO5AAUE4tf_A_RYYjBd7CMFNNIZOLL7NyOSEk1UESLKP-ja5fQfGJJQ5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیرحسین ثابتی، نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم خواهند کرد.
🔴
باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125270" target="_blank">📅 13:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681a291c50.mp4?token=Bspp7tOM-Y7R3P33TKKc--Yb12_xxoECQH_mxcV2nIi0FOGcwokMXQ-3R4Y7bRVnGMVb7Wz7oqeIzyXGo4QANWKy6wLA-kifkmodtzyGoEyTknBIUh_PiwXgUlhqWWzU09qimPtyG5lYXSBtczIFqpyknTiEmncXlI9a0QmYW2MjSlv6nSg_OvRsDpb72GYRaB_xXu2hW0DiFjkTHNvzHLaOW4ZHEmDHU0DrYgLdxdtN7iUOinQXC2lBkp1EoQ6zpQLHk2RtYjH3HChB3shmJnLueQZuSk41xKIsmHgX-R8NxvlXjq-sT097Wm60kA_jlJIREx4foD2bMU7KoE8IDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681a291c50.mp4?token=Bspp7tOM-Y7R3P33TKKc--Yb12_xxoECQH_mxcV2nIi0FOGcwokMXQ-3R4Y7bRVnGMVb7Wz7oqeIzyXGo4QANWKy6wLA-kifkmodtzyGoEyTknBIUh_PiwXgUlhqWWzU09qimPtyG5lYXSBtczIFqpyknTiEmncXlI9a0QmYW2MjSlv6nSg_OvRsDpb72GYRaB_xXu2hW0DiFjkTHNvzHLaOW4ZHEmDHU0DrYgLdxdtN7iUOinQXC2lBkp1EoQ6zpQLHk2RtYjH3HChB3shmJnLueQZuSk41xKIsmHgX-R8NxvlXjq-sT097Wm60kA_jlJIREx4foD2bMU7KoE8IDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ آمریکا، پیت هگست برای شرکت تو مراسم، رسید به پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125269" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gjvj_YWcPEwC2C6N3wY6IlBOhHbhl_d3DExO-WbUaa6FOCQl_uT3o219TYDjaWxZnpz25fXcJCiDFvVcnBgulMR0Z4fsp_AMsrwF-9EJUzaC0dCYvblyNpFZo1ThXS7EK_tLIi-PnB4x2kDJUQsuyRGMfdBIuO3xLO41YlxkIPOJ_Nq49iUDE03-CB6ylYX7zm82hUhOzCYJm4NaUnlSCapHnqsP1vdeOiKFKIvMxp6EfSqF42z15dmFj2KsothnVIuswbIIj08ckjJVFKOx0JXUz4ea5UHlaVngq3MREspEaUkcyyi79AVnDcH_V3xjdXWl4Z-lb-vJpnUDMalJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJFL9zaTmPT8A6e4n-eAc58hw9f_izrGQDBfPq049I-hYeTEMjzFnNvrv2WeJMPWzKphyoPtIWhxs5LL1pg-1ZJP71mfjg-i3gCJxTOwqNeWZNacJK5hjC_T3mr-GkSx46dzVf0ewJlR5lYmU-p9EQf3yU3gDtChjgTeqimn0kdRch_IFSzwAQzfYUT-ZCGmMeDlY3Lyi9zSc3vMWe7dGac56_Ivc-G_RhAWx8DIIaOQl8vKW2WWAQZeJfNIA6sy7-PzY8fCfHgjYGEd5Sd2gKR3de4dwFakLjvNpT5sVyM56ZDlv25F3IW5xpBvg0d9F-t7YNHXYqWhR7Vdkjz2IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنگین‌ترین موج تورمی در تمام تاریخ ایران!
🔴
۱. نمودار اول: تورم نقطه‌ای و متوسط سالانه
🔴
این نمودار روند تورم نقطه‌ای و تورم متوسط سالانه را از سال ۱۳۸۹ تا ۱۴۰۴ نشان می‌دهد. الان تورم نقطه‌ای روندی صعودی را آغاز کرده و از تورم متوسط سالانه پیشی گرفته. این اتفاق معمولاً نشانه آغاز یک موج جدید تورمی است؛ موجی که انتظار می‌رود در ماه‌های آینده اثر خود را با شدت بیشتری در اقتصاد و زندگی مردم نشان دهد.
🔴
۲. نمودار دوم: تورم انباشته ۸ ساله
نمودار دوم که بر اساس داده‌های بانک مرکزی تهیه شده، تصویری عمیق‌تر و هشداردهنده‌تر از وضعیت اقتصاد ارائه می‌دهد. این نمودار نشان می‌دهد که در ۸ سال گذشته، تورم انباشته با شتابی بی‌سابقه افزایش یافته و از ۲۰۰۰ درصد عبور کرده است.
🔴
بازه ۱۳۲۴ تا ۱۳۹۷: تورم انباشته در محدوده‌ای نسبتاً کنترل‌شده و نوسانی قرار داشت.
بازه ۱۳۹۷ تا ۱۴۰۵: روند تورم انباشته وارد یک مسیر عمودی و انفجاری شده است؛ مسیری که نتیجه آن، کاهش شدید و تاریخی قدرت خرید مردم بوده است.
🔴
به زبان ساده، این یعنی قدرت خرید پول ملی نسبت به ۸ سال پیش، بیش از ۲۰ برابر تضعیف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125267" target="_blank">📅 13:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EYriCkA9gWkbN6MlUY6Sv2LRC5aVIaECqkEF79z-dfXs9-ylmI4FAET7gCWx6iFIDha08_60PUYncqSduWTL0-EqhiKi1tgOC6e5z_55TDxQC3HqELwEGxMZy5-PWpn0XMy5I_NakTQz1YWEYpmYcvMQKgwdqk5iF2VyEztl0tsmMnDo_zZrxyGpFwbBmsHbdVLHs7EPSd88FLf-dQMjrGIUu3Y6QgvijtvjjDXXKgvvBjLwTE34pB4kjCIN18ZiY1KWAtqEUsFFWPP5NRKBMcWvgqbgsqaw7FkR9ptxf262DlHUc9pFqgzbbYi1V4qXYechDbpZh7TxturgN5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار یک پهپاد دریایی «مرتبط با جنگ اوکراین» در بندر رومانی
🔴
به گزارش رسانه‌های محلی، یک پهپاد دریایی مرتبط با جنگ اوکراین صبح روز جمعه در بندر کنستانتا، از مهم‌ترین شهرهای بندری رومانی منفجر شد.
🔴
وزارت دفاع ملی رومانی در بیانیه‌ای اعلام کرد این پهپاد حدود ساعت ۱۰:۳۰ صبح منفجر شده و «احتمالاً از نوع پهپادهایی بوده که در جنگ اوکراین مورد استفاده قرار می‌گیرند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125266" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3719112f5.mp4?token=Zivzj6QyX2TQ5UK27XkO04yfXRkGEXMuK7ptBauzmCcCCeS09k7wRKayKT_idgO98xMHFakGQAW0sgbXaYGRjpt51Mt2bD0q73uELuEKGiA5UQ8bxjR1mVf__J0GgBhCPg0DWk5hkOmxQ7Rqp8wtbjMcQrfDeuQz6IA3tO6vdIeVvo1Ny-3aBLxzGff4GfRPRc_u-PydaZXajzSMppxflhwCKsB6wZN_HHoyRgNaHPwYj1qT_3iFirx-OKQ866-z7_K8EuER7rnvU9X8VY-FanrGkciW3sjhNRw-mqugwvOdxh4TUzh908LyPbWZKrMX9GjclehXXqBGi4RgDKph-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3719112f5.mp4?token=Zivzj6QyX2TQ5UK27XkO04yfXRkGEXMuK7ptBauzmCcCCeS09k7wRKayKT_idgO98xMHFakGQAW0sgbXaYGRjpt51Mt2bD0q73uELuEKGiA5UQ8bxjR1mVf__J0GgBhCPg0DWk5hkOmxQ7Rqp8wtbjMcQrfDeuQz6IA3tO6vdIeVvo1Ny-3aBLxzGff4GfRPRc_u-PydaZXajzSMppxflhwCKsB6wZN_HHoyRgNaHPwYj1qT_3iFirx-OKQ866-z7_K8EuER7rnvU9X8VY-FanrGkciW3sjhNRw-mqugwvOdxh4TUzh908LyPbWZKrMX9GjclehXXqBGi4RgDKph-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاینده‌رود زیبا به اصفهان بازگشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125265" target="_blank">📅 13:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سفیر ایران در مسکو تاکید کرد که ایران با دولت عمان برای مدیریت تنگه هرمز در حال مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125264" target="_blank">📅 13:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7d920c97.mp4?token=uBhFGM9tBPMi8mRfnAGFbw6D_PiDZN11cm8_U4AzPdNhYbFsNbCH8XO0olT0uK1GltGvD9R000ddUrGBaUIHRoGS47B_bm1UyLEbgKxjsnC4_9wxVRW4xfiqaBHTHW5twBt5CNsnYXgqjGNkco29IgnFblBA7p5Qm7DH2adAsByAbYgDXcTZjN1dmYCbsQB-2CSwVhSOifmv5-2ENNaOs20oMeW3vFSwEIu-sQIYWsIPHl3kf_TXUgtlnZW9jyZbr5J45aQ3ojw-ixywm326F3pFH9i4QG7iXy-V72rxSS8gi0lvl5cZt_D4JWAfYC3kSvVH3s1E3BJYxAPaO6bhEwE3GlvSK2LXvSwG4esbNnApuBEdMHfdXs0Og8n1MeWIYyMeTb1gmyFOArAxQOO-QgtBYWSbcwfKy6KoUZU0MRaYYjuM0AvTQMdMdlgITZjrBHYhhRrmeiLvPipLH1zxEp769Q00YV9cc-T_K97LaU-60AccPqb9PJUJ8EJHFmF1cKZ3x57P-E_fHw15KCHtZGAM8PC2M2Qs4lKUFvwY7O4eNe-PrNqHBAMriR846yseFuzkZF5CKAgKWQeaLDtzvSHdE3U7c_C8Dc68fnmfibVbULLzkpwX0nZH5mAEh-wIJCjZVhmibB89bbxH-NDhwT9sRuJd_9G-rgLZrszOnPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7d920c97.mp4?token=uBhFGM9tBPMi8mRfnAGFbw6D_PiDZN11cm8_U4AzPdNhYbFsNbCH8XO0olT0uK1GltGvD9R000ddUrGBaUIHRoGS47B_bm1UyLEbgKxjsnC4_9wxVRW4xfiqaBHTHW5twBt5CNsnYXgqjGNkco29IgnFblBA7p5Qm7DH2adAsByAbYgDXcTZjN1dmYCbsQB-2CSwVhSOifmv5-2ENNaOs20oMeW3vFSwEIu-sQIYWsIPHl3kf_TXUgtlnZW9jyZbr5J45aQ3ojw-ixywm326F3pFH9i4QG7iXy-V72rxSS8gi0lvl5cZt_D4JWAfYC3kSvVH3s1E3BJYxAPaO6bhEwE3GlvSK2LXvSwG4esbNnApuBEdMHfdXs0Og8n1MeWIYyMeTb1gmyFOArAxQOO-QgtBYWSbcwfKy6KoUZU0MRaYYjuM0AvTQMdMdlgITZjrBHYhhRrmeiLvPipLH1zxEp769Q00YV9cc-T_K97LaU-60AccPqb9PJUJ8EJHFmF1cKZ3x57P-E_fHw15KCHtZGAM8PC2M2Qs4lKUFvwY7O4eNe-PrNqHBAMriR846yseFuzkZF5CKAgKWQeaLDtzvSHdE3U7c_C8Dc68fnmfibVbULLzkpwX0nZH5mAEh-wIJCjZVhmibB89bbxH-NDhwT9sRuJd_9G-rgLZrszOnPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس: جنگ ایران در بودجه پنتاگون نبود, حالا ارتش آمریکا به مشکل سوخت و مهمات خورده است
🔴
جنگ ایران در بودجه پنتاگون پیش‌بینی نشده بود و حالا وزارت دفاع آمریکا با فشار جدی در بخش سوخت، مهمات و ساعات آموزشی نیروها روبه‌رو شده است.
🔴
دریادار کادل، فرمانده عملیات نیروی دریایی آمریکا، در کنگره هشدار داده است:
«نگرانم که از بازه زمانی جولای مجبور شوم درباره نحوه آماده‌سازی و تولید نیروی عملیاتی تصمیم‌گیری کنم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125263" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر خارجه روسیه: ترویج گفت‌و‌گو میان پادشاهی‌های عرب و ایران را مهم می‌دانیم
🔴
ترامپ گفته بود که «ایران را به عنوان یک تمدن نابود خواهیم کرد»؛ این یک بلند پروازی گستاخانه و هدفی دست نیافتنی است
🔴
آمریکا به وضوح می‌داند که در موقعیت ناخوشایندی قرار دارد و نمی‌داند چگونه از آن خارج شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125262" target="_blank">📅 13:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرنگار العربیه: آمریکا همچنان درخواست ایران برای آزادسازی دارایی‌های مسدود شده‌اش را رد می‌کند‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125261" target="_blank">📅 13:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125260">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf655e55b0.mp4?token=p0Hg3zO2J31A5HklFLbg1oWGEuMnkBKJXW5SnXvfG5rvjwOuUL0ic2_N9twmwe4-XJgeb8-EHJLyH_790qmrPm_jja9Ehhi8Pvtxh884jUFOurWsbSURzPHQtyL7jfTAtMjTMRyym1l9xH3qK2LjfUK22pW1DFUzQGc5nfS07CcobUbhPihEU4viTD8RoPSJTCM65FFD0POy0fKQFsKuNuk2d8u5YngxLbV2M6dKXGqCE4K1d4XouAZnBk1ZxbOUbROQStey27RXo9qyVgVkWGvEwwCdMO5vJ8xRSA2_nQFWftv2vL20Tjgr-0uWa7OnaH4wTLYZ06Rj7A5Mu7D2bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf655e55b0.mp4?token=p0Hg3zO2J31A5HklFLbg1oWGEuMnkBKJXW5SnXvfG5rvjwOuUL0ic2_N9twmwe4-XJgeb8-EHJLyH_790qmrPm_jja9Ehhi8Pvtxh884jUFOurWsbSURzPHQtyL7jfTAtMjTMRyym1l9xH3qK2LjfUK22pW1DFUzQGc5nfS07CcobUbhPihEU4viTD8RoPSJTCM65FFD0POy0fKQFsKuNuk2d8u5YngxLbV2M6dKXGqCE4K1d4XouAZnBk1ZxbOUbROQStey27RXo9qyVgVkWGvEwwCdMO5vJ8xRSA2_nQFWftv2vL20Tjgr-0uWa7OnaH4wTLYZ06Rj7A5Mu7D2bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جاوید نام ‎سعید تروند ۳۳ ساله اهل ایلام شامگاه پنجشنبه ۱۸ دی در آبادان با شلیک مستقیم گلوله جنگی حرام زاده ها کشته شد.
🔴
او متاهل و دارای فرزندی ۳ ساله بنام آریامهر بود.
🔴
اینجا پدر سعید تروند با فرزند جانفدایش بدرود میگوید.
🤔
عرزشی حرام زاده ، پدر مادرتون باید مورد بررسی قرار بگیره که چه حرومی به خوردتون دادن که اسلحه به سمت مردمتون گرفتین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125260" target="_blank">📅 13:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125259">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مرکز ملی فضای مجازی: بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، قطع اینترنت در هفته‌های اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125259" target="_blank">📅 13:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84ebce81d.mp4?token=quF0nH_--fGXWPEsE1SYx65O3q3vGa-IqtAATvNca4qt7onLFHyzUtiK3BqJdO3hXe8zHgc1-88ZhFCRNQpO167rtEPFIJooJN9Vzc61ukhaOPJ_A8GMCOrPMQD8KIbTosxfVbRie2J3cEY2XDTRIqtnLviJWyi4-lBFR5q_MRudmcxb-RtOiZ-pe0-GKD0xojZGzEo_mNtWWDiGJB--m92WhxaNwbllEJN95sP0Vz7772_4KnbTW7D1SQwnY6jCgsk1KcadJo5nkiywKSehBwWGOnUiW92x7Q3ntoWn_jtzcKKar8VaW1QqTp0jwUdnwueOC9qXUi_InxTQjkFtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84ebce81d.mp4?token=quF0nH_--fGXWPEsE1SYx65O3q3vGa-IqtAATvNca4qt7onLFHyzUtiK3BqJdO3hXe8zHgc1-88ZhFCRNQpO167rtEPFIJooJN9Vzc61ukhaOPJ_A8GMCOrPMQD8KIbTosxfVbRie2J3cEY2XDTRIqtnLviJWyi4-lBFR5q_MRudmcxb-RtOiZ-pe0-GKD0xojZGzEo_mNtWWDiGJB--m92WhxaNwbllEJN95sP0Vz7772_4KnbTW7D1SQwnY6jCgsk1KcadJo5nkiywKSehBwWGOnUiW92x7Q3ntoWn_jtzcKKar8VaW1QqTp0jwUdnwueOC9qXUi_InxTQjkFtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از هشدار ارتش اسرائیل برای تخلیه، مردم جنوب لبنان، و اطراف نبطیه، شروع به ترک منطقه کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125257" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOdo9qymQwxWoOsO3zYO3O39UnxbgYzqTUBFE2p0RA2NIJcol0ahntqpRFJN8GmutSgUD4wEInHfYodI1OVnbJiQVBb610qMFaqeKlra9hbsHBLIcZ1OK9F7Dc2KPmnW2vTkNYhzNcp_zE006Ldr5TdnNU1hn2CcX4wiy4AsI-qlunMJYNptv5C_mgHw-Y8kOsKWpyBmTnHgqsR85Rm8PRwEMNy-ItD8SnC5sT309yk8y16BLANBTprowO5G9DdbscHXFhtPMOBqzuR8BPeQN3GMBKD1TPeYLjSMC7vquRbMiXo89LCewf4bpvYbEckoZIAPyLnG4wyXLE-lSSwlWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125256" target="_blank">📅 13:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asZsbjUC-Ra_yTNP7Ekgwudj08jmnY_j-r9KNtWXBAZGRzqO2AuerxXsBvDSz6jCf0Nbjpea8nhkrhajvbeIsGiw6iakynT87Cuz7ePmfLf9GiCrUd7Vr_xg64dClmvOIYYDr0jYUSAh6T3OWGKtLJA-7eGrsZ8ZsL7TOhvxMnPF6nmxJtfLkWsuBqySU0cJvTRi1ivJN8jtnQBLcl6vKeWNsivIf3hiNxfOU7RRX-PyWM7o5nqHaZfU0Jn79uwb3KqIQ59K6zEIoYEhfB9D-kAXXDbB3gKuSjUJPMxZWBZNEc4McSSmCB6s9-rHYlDg3ItsYZcrTx1sHW0Dpg2KGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه دیتاسنتر ایران با فنلاند
🔴
سمت چپ: دیتاسنتر ایران.
🔴
سمت راست: دیتاسنتر فنلاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125255" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_1s-p_5gONSGHaY_BEIZYHUdEW2PMN7k1RBXLo7B1oijTFivz51hdWZ1tTO8U_tbgmyvKicosJ_FicywTLUKcMfYu_5puPkZwhFf99EA80q6ESCw-_9TWR8FsdyfxnoNf3fkzcEUHx1fizXo6eG_ukYO0ghmd_A8p9EQQK2vW8CQ3I005PWGJT63uWEgNbHkD4P5UYvNU6Q5wo3-V6rOH6_Nbm7YP4wbbvtYiVciFA2WINfphDP03txngbezf6T9f5EJarl60Ju7dRX_XESUqvq6Hvcw65huTAlKFEYqXyEb0uLZnouqpa9x6MDZSFcInEAEU312SLIjo9Fysht1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنا با ۵۲ رأی موافق در برابر ۴۷ رأی مخالف، لایحه ۶۹.۵ میلیارد دلاری برای تأمین بودجه اداره مهاجرت و گمرک آمریکا (ICE) و گشت مرزی تا پایان دوره ریاست جمهوری ترامپ را تصویب کرد.
🔴
سناتور لیزا مورکوفسکی (جمهوری‌خواه از آلاسکا) تنها جمهوری‌خواهی بود که به این بسته رأی منفی داد و هیچ دموکراتی به آن رأی مثبت نداد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125254" target="_blank">📅 12:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea310363a4.mp4?token=FoG432RzKFmvT-LYqKYErtlHjJC3DMQwJMQ1eI92vaQ8KmllXCIrUg__8IAvfO6lZHg_5uU5UXb766rAMp8TZ0ZRySnyo16YIm_25CfgKyjwqf1Fsg3YyrJ92glTnsVXKq1Y6cgcVBZPJftAW0_ryI-ISWtrupiJ8jy5FSW0ufDuBdt0x77QGfZVTFjp-oQVOb4vh8N49v1MVBjGN1O5oN9cI4k05CKnWWPZJYXsHHPFyCm2ESh4ikGmJie2Lq2ycanmqpNncukAbErE6qomnHywqj2dGcwdEJORiAxazqnmPipk3aigO-ODeNlpSFcoHFNK3OGFcdKMUk6x8p0iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea310363a4.mp4?token=FoG432RzKFmvT-LYqKYErtlHjJC3DMQwJMQ1eI92vaQ8KmllXCIrUg__8IAvfO6lZHg_5uU5UXb766rAMp8TZ0ZRySnyo16YIm_25CfgKyjwqf1Fsg3YyrJ92glTnsVXKq1Y6cgcVBZPJftAW0_ryI-ISWtrupiJ8jy5FSW0ufDuBdt0x77QGfZVTFjp-oQVOb4vh8N49v1MVBjGN1O5oN9cI4k05CKnWWPZJYXsHHPFyCm2ESh4ikGmJie2Lq2ycanmqpNncukAbErE6qomnHywqj2dGcwdEJORiAxazqnmPipk3aigO-ODeNlpSFcoHFNK3OGFcdKMUk6x8p0iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جایگزین برنامه 90 بزودی با نام حکمت‌های فوتبالی روی آنتن زنده میرود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125253" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwzeLI2M_nFl8y2-3BzTJpu7g6Yp88XzxGZ7saRKn_U4vKoJncOXqadVRKZqclbgcV1xfDzwWZd4GCDXmk_Ccw5sACbusUPBmWJ1qhWo4Ao0JwNV0YRBRO1JPuW6k4fPoXds2PspmRqJxW58iNVTYeph5ALxf3jR1S0fLMaXrSsVuMdBvhtnSFDz_i7BRQT4OIZ4q9N4I7mSarXVBADVfwS-98jPx9JI_-JhsDGT5BgrjAoqdZASj7DSZj4_V-yhc5AYpapM0yPlUkdtIe1MXy5Mo6_0u_j74gMcXxJyfUWRz-FBcCmB8ayFAXug1tHsv3BLE18nBkOZPD6inI223w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجموعه ای از حملات هوایی اسرائیل شهر عنقون در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125252" target="_blank">📅 12:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa9d58916.mp4?token=keAjNT5EAtbjGCzqR68o7xZiS_4A5pLBtZ92WZurIdaDzNoMfQHreeFeoz6m5hYS8m_i04Nsm25GG1zVZKidlj1lVs1OJnzvsAauB51D7k45ZwZdy7_KjiJU6Bkacb-b5Yk6i2Hw77d5XkJa_WXCLrFXa4XcU7jTUjieM8vispoQ739oJPqRLMCAFDmtR0spypB3GsOoxZ4ngN6lqU-pvTxd3X3pYHsaIMmUCi-NkuIBV9uheqj56PO3i4FOq9ZXFAiAegAvVOPMsSOGlqZhEg8fwa1hQtXir_fnRbEsQUdPsQF3n2pStVv-2j-iG6um0mtb0maH9fWJqO5krnyuZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa9d58916.mp4?token=keAjNT5EAtbjGCzqR68o7xZiS_4A5pLBtZ92WZurIdaDzNoMfQHreeFeoz6m5hYS8m_i04Nsm25GG1zVZKidlj1lVs1OJnzvsAauB51D7k45ZwZdy7_KjiJU6Bkacb-b5Yk6i2Hw77d5XkJa_WXCLrFXa4XcU7jTUjieM8vispoQ739oJPqRLMCAFDmtR0spypB3GsOoxZ4ngN6lqU-pvTxd3X3pYHsaIMmUCi-NkuIBV9uheqj56PO3i4FOq9ZXFAiAegAvVOPMsSOGlqZhEg8fwa1hQtXir_fnRbEsQUdPsQF3n2pStVv-2j-iG6um0mtb0maH9fWJqO5krnyuZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم خشمگین آلبانی در حال برداشتن فنس‌های حفاظتی در جزیره آلبانی که توسط دختر و داماد ترامپ خریداری شده، هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125251" target="_blank">📅 12:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
حملات هوایی گسترده در جنوب لبنان در حال وقوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125250" target="_blank">📅 12:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175f9b173e.mp4?token=E_gvC73UkDDPpwg6HkXF9OPp2rARMfVld0O8a7zw6_A1ILmi_yqntGR-vt2RBFGZE-Oxl2P-n6lh6LmbDEawaBdD838kUIInrbaeJYKtp9m7fU_Aoon9YEjVve9rdyuijPymk9a92by9Sv9oh6SxIqLOjFI0jWmkn_GrN0Wb-FtzXLy8D4R-OkDdq2ji6JdB7cKOz5BTGfPMMp3izxU7SUBs5tLr0sUCnrF5Cm3eWdT4FUwPxvbvVSU_MUtggW3-Xn9rq7VeA6qSzqnd6R6ZOAQilF_rVZAZJrerZDyvHyARY98pkGfLxyaachcogpnC_b2qimr427WMCXmy2w7Sxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175f9b173e.mp4?token=E_gvC73UkDDPpwg6HkXF9OPp2rARMfVld0O8a7zw6_A1ILmi_yqntGR-vt2RBFGZE-Oxl2P-n6lh6LmbDEawaBdD838kUIInrbaeJYKtp9m7fU_Aoon9YEjVve9rdyuijPymk9a92by9Sv9oh6SxIqLOjFI0jWmkn_GrN0Wb-FtzXLy8D4R-OkDdq2ji6JdB7cKOz5BTGfPMMp3izxU7SUBs5tLr0sUCnrF5Cm3eWdT4FUwPxvbvVSU_MUtggW3-Xn9rq7VeA6qSzqnd6R6ZOAQilF_rVZAZJrerZDyvHyARY98pkGfLxyaachcogpnC_b2qimr427WMCXmy2w7Sxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر امور خارجه روسیه:  عملیات‌های آمریکا در ونزوئلا و ایران هر دو مربوط به بازارهای انرژی جهان است.
🔴
در مقطعی، آمریکایی‌ها حتی پیشنهاد دادند که تنگه هرمز به صورت ۵۰-۵۰ توسط آنها و ایران کنترل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125248" target="_blank">📅 12:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a7eb67c92.mp4?token=bX4ueCH2yEsMW2F_Jeay6tzrM216wJkteHpxCOoSnXyRu-lvU8UTU4c0ljeZKjNYv1rkDbCavkX4WlhtHsz0UldRYEMJpF_HevGmCh-5T2jT8FF19nanuVnnartd_CehB_LuS2S0bdRmhfjf5uz1YQgqxz_S-368lGlNJzrb7VwLzV17SU9oXQGl3l2yWKk0fl_g89d4RWeVRsnH_YRpJYtiYGPHwXl89-dSq-BIqf_43P7113vMr6p5egiG-itviWb9hZWG01vwf7MWp-Mbj5b5xpOY0NEmj-J5mJytqQ7oD-2xH8JI8yQPXKquMb2ndWXU-NOs5qLbUhzotza_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a7eb67c92.mp4?token=bX4ueCH2yEsMW2F_Jeay6tzrM216wJkteHpxCOoSnXyRu-lvU8UTU4c0ljeZKjNYv1rkDbCavkX4WlhtHsz0UldRYEMJpF_HevGmCh-5T2jT8FF19nanuVnnartd_CehB_LuS2S0bdRmhfjf5uz1YQgqxz_S-368lGlNJzrb7VwLzV17SU9oXQGl3l2yWKk0fl_g89d4RWeVRsnH_YRpJYtiYGPHwXl89-dSq-BIqf_43P7113vMr6p5egiG-itviWb9hZWG01vwf7MWp-Mbj5b5xpOY0NEmj-J5mJytqQ7oD-2xH8JI8yQPXKquMb2ndWXU-NOs5qLbUhzotza_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از یک زن ایرانی در مکه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125247" target="_blank">📅 12:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-XlmG_hm91p6i--bXw6GyTl5GuSY1MoVSzxeQObbyCRKnIkyWFhA4_5kt98cmeQt0y97RcYqOVu7tuwStLPhpBy5YA4CWevABbeq_3Y7LQr9ZhK87J8zoFxrnrfpJYlOij22f1cQLQcl0Sz_jhTcvbKm7zElQyvxlJCULB2U0QJ3bFjVCVYjDE2zor1VBCZewZMZMRY7VHYh572enGktuHJk0V_t9CsX7OV6hZQszMncTpFYw88plknPEvDtvDtT71bwppW9S-QW3XatrYt5hh9u4bhyilFfL3Xul7KpTbqi2nYYm_ss9uF7CtiOdxwESRWnjCmVR9eWirBKfjM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تیمی نروژی‌ها پیش از جام جهانی به سبک وایکینگ‌ها
@AloSport</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125246" target="_blank">📅 12:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مصاحبه با یک خانم بی حجاب: چرا تو این شبها تیپ های مثل شما کمتر بیرون میان؟
+خرشون از پل گذشته و میان به ما میگن پرچم دستتونه شالم بزنید و تذکر میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125244" target="_blank">📅 12:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دیمیتری پسکوف: برنامه‌ای برای دیدار پوتین و ترامپ تو آینده نزدیک وجود نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125243" target="_blank">📅 12:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125242">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سازمان ملل متحد از اسرائیل خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت ملی این کشور احترام بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125242" target="_blank">📅 12:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125241">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
شی جین پینگ رئیس جمهور چین، در روزهای 18 و 19 خرداد به کره شمالی سفر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125241" target="_blank">📅 12:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125240">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
العربیه:وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125240" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125239">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
خبرنگار : نظرت درباره اتهام نسل‌کشی از سوی وزیر خارجه ایران به آمریکا و اسرائیل چیه؟
🔴
روبیو : ایرانی‌ها خودشون استاد نسل‌کشی‌ان؛ هزاران نفر رو کشتن
🔴
هر مشکلی که تو خاورمیانه می‌بینید، یه ردپایی از ایران توش هست
🔴
حزب‌الله؟ ایران، شبه‌نظامیان شیعه تو عراق؟ ایران، حماس؟ ایران، حوثی‌ها؟ ایران، اسد تو سوریه؟ ایران
🔴
به هر طرف نگاه کنی، از نظر اون پشت همه این ماجراها ایران قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125239" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125238">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ebd4642f.mp4?token=UTbPJZqmu2eUDAjDVfqYqoFURquSTFPSkXvw9s3f49bwUuAZP33Qf2FrIVkzS59pX8K33729NtrQt4T34Z_3qI2adkcb6kJsEGB5c64fAUrh4TTMZOaH9jrk8PnuvMTAWTNHuV-Gin_cy8Vbpw-sV-vd5ROfMV22XrE9IMaTdUOHWfy6HVCU8P0yJd3kM6IdQWDxFjSHS7oRCRR9Ydsb9hnbOCZGcdsPCkzp1WuXhbUXZTLY0wS_hUeQPakqovJayeMwJFFc2reig1b7UdZBy3cQUsTkmeyKHrT7xKvZ58pAYUn_8roefTVuJnVohYYdQFWLgzgoddkJKK8EX93ubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ebd4642f.mp4?token=UTbPJZqmu2eUDAjDVfqYqoFURquSTFPSkXvw9s3f49bwUuAZP33Qf2FrIVkzS59pX8K33729NtrQt4T34Z_3qI2adkcb6kJsEGB5c64fAUrh4TTMZOaH9jrk8PnuvMTAWTNHuV-Gin_cy8Vbpw-sV-vd5ROfMV22XrE9IMaTdUOHWfy6HVCU8P0yJd3kM6IdQWDxFjSHS7oRCRR9Ydsb9hnbOCZGcdsPCkzp1WuXhbUXZTLY0wS_hUeQPakqovJayeMwJFFc2reig1b7UdZBy3cQUsTkmeyKHrT7xKvZ58pAYUn_8roefTVuJnVohYYdQFWLgzgoddkJKK8EX93ubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حرص و ولعی که حرام زاده های حکومتی در کشتن مردم داشتند در هیچ نیروی خارجی که در صد سال اخیر به ایران حمله کرده دیده نشده.
🤔
حرام زاده عرزشی، هرکسی حرام زاده های محله خودشو میشناسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125238" target="_blank">📅 12:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125237">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ارتش اسرائیل در پیامی برای ۶ شهر و روستای دیگر شامل الصرفند، تفاحتا، البابليه، قعقعية الصنوبر، المروانيه و السكسكيه هشدار تخلیه صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125237" target="_blank">📅 12:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125236">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNRv1g6pEb1mI6fdufm2yoKJjZb_nSa1so6y1xh-IU-q2UvhBQZ32sMFnx1pibP0TZm2FzeCPW_Po15t5brx0_JfcPTYQA83pIxT0wl9-o0lZfgOpJb5SkLy_E8rpbUok-ljPhjIH0JFuQyLt1rwklkNnRplksSydhg-E4fPMyCTBOOcz26NBS7lQ3AmgCXeQR-Unl_BZxZ4sVxzy-kmO4wYezQWM3qi6XqeTDyZ51kry14D0Hf75cRCvqxfPoQmWoqlWrdT7-FFv-Y4xd2QrmD33o1eJ3BJEXG3jZPRLJWFkjQvr3qSeIuDkyZdZffeOvICshhgEsGhPBtO4CdGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبری المیادین از حمله پهپادی اسرائیل به شهرک‌های «تول»، «حبوش» و «تبنین» در جنوب لبنان خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125236" target="_blank">📅 12:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125235">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDDouLEqSfyi572cbjenrng4QF8z-RpfY7qoW8v1X9ixsobt0gn7OVXEupohuwzV2JXhBO_SibnnIb20PP5ZRnOZgNwIAr1kmGxThaZvdETSucdv-TM6VFV8lDiYEqLwhg_OCcSaBQjObtsXUrBZ9tVpAPt2TUJai-_JpHhCcJkZNBSp5859Kj98c1RfPNM8FjT9ecLL34dtfZnDp21F4W9AlQWwb7FCJCEomV3D68mVq6xg9qfqKYotPog_MfNAqg7XQWIZOsPdlbzJFS7ZEGntX6BYFHlj4Doh4yETGrsFcL9PO4F1JH4Uz4NQ_ypmtJiUQ_Qm3TlaKOC7KBZIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل: یک فرمانده واحد مهندسی حزب‌الله را ترور کردیم
🔴
رسانه‌های لبنانی از ترور حاج آدم عبد الحلیم حرب، از فرماندهان یگان مرکزی نبطیه حزب‌الله خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125235" target="_blank">📅 12:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125234">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78399abc8d.mp4?token=imnZPKDsSxUaLCtt-x8IS3gV3YVjZoGhk-y6yyQWx-gGRCLPfVfZqXv7XU9chDk6fLH8hIIvcP3nUNW5MRhaXWLLrq33EAjPg-of-_PFHFemgoobwCYOSbQjOHtFLyuHzbTwvkWcaYeagFHfKJrCIpsi0VukUOWSkHm-8zdQyu3bShW7Bml4a20Qb9N5P4xkdFWZPSwvhVeV_An6tGdJ-DEMSmb5LWAWZZSNlMYB0I7RnsbSbw9Vh33NeNxm_lmXdN4u-R4Ydz9Tw9o7h30bosqwmBPQ-hO1jE5V-j32-VMVa5xUpLUbphVdJAeK5Icis5Z0XWFm_5dTEnB4MXhMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78399abc8d.mp4?token=imnZPKDsSxUaLCtt-x8IS3gV3YVjZoGhk-y6yyQWx-gGRCLPfVfZqXv7XU9chDk6fLH8hIIvcP3nUNW5MRhaXWLLrq33EAjPg-of-_PFHFemgoobwCYOSbQjOHtFLyuHzbTwvkWcaYeagFHfKJrCIpsi0VukUOWSkHm-8zdQyu3bShW7Bml4a20Qb9N5P4xkdFWZPSwvhVeV_An6tGdJ-DEMSmb5LWAWZZSNlMYB0I7RnsbSbw9Vh33NeNxm_lmXdN4u-R4Ydz9Tw9o7h30bosqwmBPQ-hO1jE5V-j32-VMVa5xUpLUbphVdJAeK5Icis5Z0XWFm_5dTEnB4MXhMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از ساعتی بعد از آنکه دختر ترامپ از تصمیمش برای ساخت یک جزیره در آلبانی خبر داد این کشور بهم ریخته است
🔴
مردم شعار میدهند کشور را  به اسرائیل نمی‌فروشیم. اینکه مردم اروپا داماد ترامپ را هم معادل اسرائیل می‌ دانند پدیده جدیدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/125234" target="_blank">📅 12:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125233">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بلومبرگ: قیمت قراردادهای آتی استاندارد گاز طبیعی در اروپا از روز جمعه گذشته تاکنون ۷ درصد افزایش یافته است.
🔴
قیمت قراردادهای آتی گاز در روز پنجشنبه به بالاترین سطح خود در ۴ ماه گذشته رسید، همزمان با کاهش بیش از حد انتظار ذخایر داخلی گاز.
🔴
نرخ پرشدگی تأسیسات ذخیره‌سازی گاز طبیعی در اروپا کمی بیش از ۴۱ درصد است که نگرانی‌های اروپایی‌ها را افزایش داده است.
🔴
در صورت ادامه بسته شدن تنگه هرمز، رقابت با آسیا بر سر محموله‌های حمل‌شده از طریق دریا ممکن است در تابستان امسال تشدید شود.
🔴
قیمت گاز طبیعی اروپا در مسیر ثبت رشد هفتگی قرار دارد، زیرا همچنان توافقی میان آمریکا و ایران حاصل نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125233" target="_blank">📅 11:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125232">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی سفارت آذربایجان در ایالات متحده در بیانیه‌ای به سی‌ان‌ان گفت: «ما ادعاهای بی‌اساس مبنی بر استفاده از خاک آذربایجان برای عملیات علیه کشورهای ثالث را قاطعانه رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125232" target="_blank">📅 11:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125231">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سفرا و نمایندگان دائم، ایران، چین و روسیه در نشستی مشترک با رافائل گروسی، مدیرکل آژانس اتمی، موضوعات مربوط به موارد مطرح در نشست بعدی شورای حکام آژانس بین‌المللی انرژی اتمی را مورد بحث و بررسی قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125231" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125230">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7e8e2790.mp4?token=HPmHGiBNZ9caHsqvIa37w1CNyElnBOC0er15zWsieUUVsDyhPaRQKCbIYDfRdacf_aAAMIYetioXbl_drzXX2hxnBhbEWCl6mBmhEIiUVXnQbK5n7AKsB2iihws1LCCn0wbEmsxMsWf8ciEDv5dPkFtRXk7r4eILNDPt8AzfLH5LV--IHf0fgQgYXzePaSk2KHUXio9PSoz5kxT5qfUZ2ru_jQRcEt6m_nFBscu63xx4jtVq7WzPj1wG31TVlclgviFiXo-lrc-oZM7GZQv3GhWQbOBoABy5a2quWCcLUScZSqce2mO6_iLusSkjsjdXFjMnvBgXIg8aHVc0cp5nnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7e8e2790.mp4?token=HPmHGiBNZ9caHsqvIa37w1CNyElnBOC0er15zWsieUUVsDyhPaRQKCbIYDfRdacf_aAAMIYetioXbl_drzXX2hxnBhbEWCl6mBmhEIiUVXnQbK5n7AKsB2iihws1LCCn0wbEmsxMsWf8ciEDv5dPkFtRXk7r4eILNDPt8AzfLH5LV--IHf0fgQgYXzePaSk2KHUXio9PSoz5kxT5qfUZ2ru_jQRcEt6m_nFBscu63xx4jtVq7WzPj1wG31TVlclgviFiXo-lrc-oZM7GZQv3GhWQbOBoABy5a2quWCcLUScZSqce2mO6_iLusSkjsjdXFjMnvBgXIg8aHVc0cp5nnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا، تحلیلگر: در آستانه ابرتورم هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125230" target="_blank">📅 11:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بلومبرگ: مذاکرات ایران و آمریکا همچنان بدون پیشرفت مونده و در حالت توقفه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125229" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=YSxBEPrI1kfjODPGJypo6XebTRUVn9v_Hc87AjYQhFE6tjCCVzpikP6kZ1aEZ1-r3VFtXUc7FN6y6JfZk2Pl06qU2j77HtsaQoJ0_q1cNzqWhQMaNlnBqCJWuxpXqAg67PeoQ5YqeywLZkt4uQ6ehK7kb_9jWhu57FRBntZoF9Pp8Zv7yVdFNyl-ptlzQzSYm4lag15SmlqBlVt_rWFnaSoONKGUwljlZFFyUdmSiIEnrnOeIOozPBdoOco8WLyoyyrjdSEpldpQAAesAWhE2P6HsKad2NvLFPV9flaEvuLmOOnBXXD_pGyIJ6e43CDqa-0bF3WUQQpfyaQhcwP3bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=YSxBEPrI1kfjODPGJypo6XebTRUVn9v_Hc87AjYQhFE6tjCCVzpikP6kZ1aEZ1-r3VFtXUc7FN6y6JfZk2Pl06qU2j77HtsaQoJ0_q1cNzqWhQMaNlnBqCJWuxpXqAg67PeoQ5YqeywLZkt4uQ6ehK7kb_9jWhu57FRBntZoF9Pp8Zv7yVdFNyl-ptlzQzSYm4lag15SmlqBlVt_rWFnaSoONKGUwljlZFFyUdmSiIEnrnOeIOozPBdoOco8WLyoyyrjdSEpldpQAAesAWhE2P6HsKad2NvLFPV9flaEvuLmOOnBXXD_pGyIJ6e43CDqa-0bF3WUQQpfyaQhcwP3bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیک‌ها همه بالا
🍷
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125228" target="_blank">📅 11:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125227" target="_blank">📅 11:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125226">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTKtM8bg3REZ07QEZrfjOLi-JcX04XkFUYWdXS2CtgCAOVdW_UOyNujkRnAQsr-AmLZuXSjh4TUXVK_f--Uxn_gm1v3ytOeW704usRrOIbwr_VKtVUVp038KP7O2HTCq0e-3ZWuUdzo_7k8NbzjXYO-JkCVgtH0Qcjqur2DNQ074QRazprz_H9pIQQhBb6b6gEJO8a4rqmmowefUuPeneU4XQGFDfGujpow55OnUu4JG7CibqVfpEQfA7qoaFEKLM3BC0Mi7aw3jJDeFb9479CqQXYbJt_xOXnElhA6VxGDCNGJ6cSg__HB-QWlFQ1jwM7hHA-fvwvKBPtmdIa7NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آذربایجان چهارمین کشوری است که گزارش شده اجازه داده نیروهای اسرائیلی علیه ایران در قلمرو آن فعالیت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125226" target="_blank">📅 11:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125225">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125225" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125224">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3s8KR6HNBW7unXwOtioDK6WUs3xgDEwfvrIvGkrltLEWkaC9l7L_D9kyjnsorLqLym9UsXYuYG50IRmamspQ_TqY8cju13dQGPSzero-ZbJsbRdOEqBb8LKHJG3CuqvliFdllMFz_vTbTc7NyoU5lbG9lIBzLmBhVyIy1ZpgDWCtEkXT76zx6AqNVOkkuZ4Gn9hyuh3gFWTZAF1vjHVvVmXXZYXEVfp_kDBYaDaaH6B_kBImr2i4QWgx6QTZyPa4S0TvE1zokq3PSab9X7ApZR776ElaOSkZ20vn8yS5QiLfhPdRXz74YjXs3EZWaUatzpyPQNVjUPuWutxyYewvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t
با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه ، سریع اقدام کنید که دیگه قرار نیست هزینه زیاد بابت وی پی ان بدید
👇
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/125224" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125223">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583002539d.mp4?token=dE9X5sXDpqihvbKUIW1mCbRCaDBelSmg8zvGj9tHfJ1tYrNoB0B7w6sFm6InYRxuM4DfHXF_XhfeQ61o8oFcVNDTiT69BK2XKADzijHRv-s-vKGuNdWqtQTnP8w7DUBTDDD0gV32l08U1VfckHpL5QNwYw9QKgzi28E_aD4XaE2JXmvPxBqBhpYq71_66RQFMPplR3hy-hB-__u4DPOefId-f-fOS4uxjNcwHGjNXxJ4JkzbRwmYyEnjPND-bpy8SrLvpoIFmUN3zxtH82FVeTDY4pyCyeipDKI01fANR551JGgnLe9rsHS1Y_OQ5L5-a8OO-saTjMa1UxIQqrd3w3aOwyPzA9TkAd9IrciH-80nAt7S_oKcuqdvLk3Fpa8L2vXaP9n_6VHop4XdAxXZBkMOIFMZ0VTu_opzvFv1L5jjO_bS_vGT7dIe5-1GGA5wPfeaMI70mfavHf151oZ-cCZxn2dCXFnuWG43f9tvAq_XKOdiRdOM1TnQDtrpP4R6LQJR9_5SOc3qrv2f9nB3xlDVJ0MyEfn0UQ0jrsvQB718T3Nmtu5300ZSGlaUZeLq9-ct4bhVTQOI5et_V1-Vn9q17D0NFnXCX-wL72eMPi4nrX64xCve8oqQkg7lW47CvunxitP0Lf3g_k60MPlmxeF_vNSMzZVodIPOysnL8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583002539d.mp4?token=dE9X5sXDpqihvbKUIW1mCbRCaDBelSmg8zvGj9tHfJ1tYrNoB0B7w6sFm6InYRxuM4DfHXF_XhfeQ61o8oFcVNDTiT69BK2XKADzijHRv-s-vKGuNdWqtQTnP8w7DUBTDDD0gV32l08U1VfckHpL5QNwYw9QKgzi28E_aD4XaE2JXmvPxBqBhpYq71_66RQFMPplR3hy-hB-__u4DPOefId-f-fOS4uxjNcwHGjNXxJ4JkzbRwmYyEnjPND-bpy8SrLvpoIFmUN3zxtH82FVeTDY4pyCyeipDKI01fANR551JGgnLe9rsHS1Y_OQ5L5-a8OO-saTjMa1UxIQqrd3w3aOwyPzA9TkAd9IrciH-80nAt7S_oKcuqdvLk3Fpa8L2vXaP9n_6VHop4XdAxXZBkMOIFMZ0VTu_opzvFv1L5jjO_bS_vGT7dIe5-1GGA5wPfeaMI70mfavHf151oZ-cCZxn2dCXFnuWG43f9tvAq_XKOdiRdOM1TnQDtrpP4R6LQJR9_5SOc3qrv2f9nB3xlDVJ0MyEfn0UQ0jrsvQB718T3Nmtu5300ZSGlaUZeLq9-ct4bhVTQOI5et_V1-Vn9q17D0NFnXCX-wL72eMPi4nrX64xCve8oqQkg7lW47CvunxitP0Lf3g_k60MPlmxeF_vNSMzZVodIPOysnL8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خروج اورانیوم از ایران: ایران مثل ونزوئلا نیست که چند دقیقه بمانیم، بعد خارج شویم و آنها برایمان دست تکان بدهند.
🔴
در ایران باید یک تا دو هفته می‌ماندیم، به تجهیزات عظیم نیاز داشتیم و آنجا یک منطقه جنگی واقعی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125223" target="_blank">📅 11:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125222">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHc-AmPBdtPrB_4obTS0WgY2lLkua1fJIOY9g6MlBeuQKmtR6rxaDqhMRgFujfVXbi6u4_UCZfegCRkG9Az0IAePYnKalEbA8JlpR0xrnPCbvjwk_Xr05VWT7genOEmQ0ctMF8K0MA4sHPKopVSiLmy2pl_do4RcCBFU2XMQZj5qJJ5WtwoWlb4Pg4Kh_JYpzQmgeEP_bp1L9SVzCInFlSIWHYIlJr50WhExX7BvpqPZXVeZfMH062GZUlALjGBb2EJPa-Z95Lby7meAiPMDIg3Vdkb4fEzRzBYBn1kWDmtpcbMx61MHCfONIsOgUmc6sX9yujwm-ZTSaWWL-RNxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظرسنجی جدید ماریو نشان داد که ۶۲٪ از اسرائیلی‌ها با «اجازه دادن به ترامپ برای تعیین عملیات نظامی» اسرائیل مخالف هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125222" target="_blank">📅 11:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125221">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رئیس پلیس راهور تهران بزرگ: تردد اسکوتر‌های ایستاده و نشسته بدون پلاک در خیابان‌ها و معابر به جز بوستان‌ها و مسیر‌های ویژه ممنوع است.
🔴
هنوز سازوکار قانونی برای ثبت تخلف یا اعمال قانون برای اسکوتر‌ها وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125221" target="_blank">📅 10:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125220">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سازمان ملل متحد از اسرائیل خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت ملی این کشور احترام بگذارد.
🔴
سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125220" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125219">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
العربیه: وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/125219" target="_blank">📅 10:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125218">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پولیتیکو: احتمال لغو ارسال موشک‌های تاماهاک به آلمان به دلیل کاهش زرادخانه تسلیحاتی آمریکا در درگیری با ایران
🔴
منابع مطلع می‌گویند که آمریکا به دلیل نگرانی از واکنش روسیه، ارسال موشک‌های کروز راهبردی به آلمان را احتمال لغو می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125218" target="_blank">📅 10:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125217">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a6df09fa.mp4?token=unELUu4cSjoD1LZeoTZGFM9jCE_Si1gc-M5c8ebPAiiqxvUaEc5VzARktrKS8tefSzJHk_sy2wn79EN_BW3YxgU46I6_WjzBYTxCyvbMgHk0imbomZfiiq_yMfbx29Iez9PRLRgmoRlAT9Za3sKnIJuLTvrq3HyeZUd3PPqjtdTRI4pHPlnZ9l81E22hEDxOpW5vG8ZzuIAJHZq1RB8c_lR6LhFgn4P7n7dyB_1hHYkNsFaKBvr49Wu-o9wXg3Jzu-gUwQyGQ8Td9_dKmhavqpJW2Fmmts1w3B9SMv_NnlAR4VhhJkvLIyOObNfzJd48Fjgm5CqxPsNqnBOD17r4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a6df09fa.mp4?token=unELUu4cSjoD1LZeoTZGFM9jCE_Si1gc-M5c8ebPAiiqxvUaEc5VzARktrKS8tefSzJHk_sy2wn79EN_BW3YxgU46I6_WjzBYTxCyvbMgHk0imbomZfiiq_yMfbx29Iez9PRLRgmoRlAT9Za3sKnIJuLTvrq3HyeZUd3PPqjtdTRI4pHPlnZ9l81E22hEDxOpW5vG8ZzuIAJHZq1RB8c_lR6LhFgn4P7n7dyB_1hHYkNsFaKBvr49Wu-o9wXg3Jzu-gUwQyGQ8Td9_dKmhavqpJW2Fmmts1w3B9SMv_NnlAR4VhhJkvLIyOObNfzJd48Fjgm5CqxPsNqnBOD17r4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی مربوط به اصابت یک فروند پهپاد انتحاری به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125217" target="_blank">📅 10:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125216">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEx7f-fx3fxnwYpNs36uYIjVnrwC_l5dxJdlx1QaQHiWmhnYD9MUe5QRjmzpk1Eh905LxQ_tfzZ_f6IWK8u-mCg9fY6ac8kfUMl4tYl5SE2op1oFNrc-qPklynwBWtx7r8ZbTuqpH8w9nXfBNBPpPTE_0yNTCHrafxPt-43_hFOA_XPQuYivSddbbFackncdieaL8YWdWxqhtTclbsi83eCPo31rwW1AmLseHCVVZt2_R8rP08Uf_-96z7fMjL_fffaiE7mfcTtIeynjzKVgeJ9ZNo1bdO3F8T6wFzRz7c_TkeEr9ESXpU-I89sSJh4V0EenwrTf5SZmsm1qQx-TVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125216" target="_blank">📅 10:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125215">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmAskKS461WIXZXVH4hL98pqhuJrhJPWOwf-wuztUZr79ORa0KoMPo4gzXHw4jJ0AsQSKwo5v6jwK5zqhymjxVm-mgsyDpCaHVkN4gsypwFbh6IT0RS_mtfqoqzTXyYKZD_G0HjwdcdiDuP61vXqOZ5IDg8q_fQNzPVrmXZEdss-CFjRcY7xZCCv7PYUe1ASeDx6pEI93kYzntAxXoIWNV7aTuHJARdWGzzlBoH2zMGvNQ8-6ZmYyDaIx0YpJ4hgJEx7LjnvXm7mXF4WHV-DZeI96udaPqyXrfNFXO6imk1oDr7DsOF0dV1mxWT9JahKpRcQkbHqpJlaYrhwr2RN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرغون هم رویا شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/125215" target="_blank">📅 10:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125214">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اسلام‌آباد درباره دیدار وزرای کشور پاکستان و ایران: دو طرف در مورد کاهش تنش‌ها و همکاری‌های امنیتی گفت‌وگو کردند
🔴
تلاش‌های دیپلماتیک برای دستیابی به صلح پایدار در منطقه ادامه خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125214" target="_blank">📅 10:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125213">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na-nGMnhaxiAynULBOf9zhrffv8C8wKr6HtfeIXG6zepPThISUJaj6T0AOsC_-4JQf_15YjmO9lBwdLUoTGqBcDtIzGhaTB1l-aDt0D9Hp91qS4ejzVTT4AxeiUl2rUHrdg7EUBVWPt4oDsEoOnS4nfbJUSXHZlrD8xhEykDDXabTWUdWeiLqeEY4JRphefwMaRSEkm155OizoLhu1MbwQtguDKy_F7UZFRm-4VbNp9uAtlSVo7uXrwzxp0ttbvJhg107CqG6deltZVvYzunIqZSUtHBQVSQK-LieLerRkn8Iu-Q-jDZxELOOHCVBK-msvgl9MuVfDDAFdXWCDZKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین رسماً به زیر ۶۲٬۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125213" target="_blank">📅 10:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125212">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo5I7n4CUwBPkdfUnKzl-320BZVkTQYtzJE_ioevafGwbbv1uaMVW3XEqGF7VuunGDizu47bLXEYokZHj0oCKIT7n7AIBE8ToZdmwD5_3dnyd-JYbt0HkRGvVqbsQZxmBssMTK6JCZH0ccyRh2oWkDV6WsopDXVOyc-NZu5Wd8kWaqSyDgYKHTOAHZdLKPjR-u9kFptEEoOxLtYrvymdvLZeMn9EkZObj7mFkGvHn_kEOM1I9Wixt-TEdNBymnaTYkwyL1m9Bh2NXCCabxlid2_sEt-I9SNlEB93JjydxvfbwZWF6AEJwfhR4gHxi6nY_TxJLYacHf7Tt5HIglpVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خیبرشکن صورتی در میدان انقلاب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125212" target="_blank">📅 10:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125211">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
بلومبرگ: ازسرگیری عملیات در بندر فحل عمان برای صادرات نفت خام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125211" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125210">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpkfdJzMXxtyDa_xOO9h1CDV-MkkSfealCuZ_MaWsQArrHq9aW-R90KUkUiv0lslqVxNCaGSRnxao_aHRkwjOm_L0K2XAM1RvYmpgwIDK8fhPn1QmD23a1ovqQ5H4Ht3P_59QhAw6i2HMkQy3uKubaDV_EQ8YN6OuVs00KGRZNkxKTaS_QVh_6wrQRDHSASEfzJeTaCd5SNToMCJ2cr6ew1dAf4cNOjOxv45zLfklfUuJsMVSdeRBL40Azc9vibUVmIwXQOneDG8ZL9YKLNFlkffDPhg3XG-JzgAV6Cbnyy3JVLKFLsqyRsdvc2RNl0VMl8qg-D8VrDthg8MVzci1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: با دیکتاتورهای منطقه به جرم تامین مالی و نظامی آمریکا برخورد کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125210" target="_blank">📅 09:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125209">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آژانس اتمی: هیچ اطلاعاتی درمورد ذخایر اورانیوم نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125209" target="_blank">📅 09:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125208">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرنگار الجزیره: دو حمله هوایی اسرائیل به حومه شهرهای نبطیه الفوقا و میفدون در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125208" target="_blank">📅 09:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125207">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه، پوتین، درباره اینکه آیا روسیه به اروپا حمله خواهد کرد:
چرا؟ چرا روسیه باید این کار را بکند؟
🔴
برای ما چه فایده‌ای دارد؟ دلیل حمله روسیه به اروپا و جنگ با ناتو چیست؟
🔴
این مزخرف است. این یک تحریک عمدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125207" target="_blank">📅 09:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125206">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کابینه امنیتی اسرائیل به پیش‌نویس توافق و آتش‌بس در لبنان رأی نداد
🔴
روزنامه یدیعوت آحارانوت نوشت: کابینه امنیتی دیشب به پیش‌نویس توافق آتش بس در لبنان رأی نداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125206" target="_blank">📅 09:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125205">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f96f6487.mp4?token=sB8ocJXVx3Z9uSMnKINwoQRFtINydKjuGyzyGUa2tSGJCNMUXB2jIivu46EyVIuQjvTEG4QcIiEZvSXmLSDdL2_5qJnjURFvupCo8a7ALYQ7wJpZAjYlZyN9FRgwF5Fe-B6hUTEwQbUEXb7HipTeUR4d1X36p7cJ-wtqGDsLOFnKw3KXg9mQh8b7Gvks0ZyF3WymWzGBgOuKupbbxQrgW-Ibzwu7Uydl8IrfBpqdJjj7gWQzI5jgIzgGAaztYA_4V3S9x-x6wtigUGcQmr1H35SV8Gz5nGW9OeoWqZKuyJLSpUC4JPZiXZnD6G8rXO-SbfZB6IdHmH6-vzFmT9bXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f96f6487.mp4?token=sB8ocJXVx3Z9uSMnKINwoQRFtINydKjuGyzyGUa2tSGJCNMUXB2jIivu46EyVIuQjvTEG4QcIiEZvSXmLSDdL2_5qJnjURFvupCo8a7ALYQ7wJpZAjYlZyN9FRgwF5Fe-B6hUTEwQbUEXb7HipTeUR4d1X36p7cJ-wtqGDsLOFnKw3KXg9mQh8b7Gvks0ZyF3WymWzGBgOuKupbbxQrgW-Ibzwu7Uydl8IrfBpqdJjj7gWQzI5jgIzgGAaztYA_4V3S9x-x6wtigUGcQmr1H35SV8Gz5nGW9OeoWqZKuyJLSpUC4JPZiXZnD6G8rXO-SbfZB6IdHmH6-vzFmT9bXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دیشب هم در کاخ سفید چرت زد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125205" target="_blank">📅 09:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125204">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
با اعلام سفیر ایران در روسیه؛ کار تملک زمین برای احداث راه‌آهن رشت – آستارا به طول ۱۶۲ کیلومتر تمام شده و به زودی برای آغاز پروژه در اختیار روسیه قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125204" target="_blank">📅 09:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125203">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عراقچی: قطر تلاش هایی برای ایفای نقش سازنده در زمینه مسائل مالی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125203" target="_blank">📅 09:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
در تهران سد ماملو کمترین و طالقان بیشترین حجم آب را دارند
🔴
موجودی مخزن سد ماملو ۴۰ میلیون متر مکعب بوده و پر شدگی آن به ۱۶ درصد رسیده
🔴
میزان پر شدگی سد طالقان ۵۰ درصد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125202" target="_blank">📅 08:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125201">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
آژانس اتمی: ایران فقط اجازه دسترسی به نیروگاه بوشهر را داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125201" target="_blank">📅 08:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125200">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhb3xybqBEMuZX43UveUFolT1lviaw2yWwFLr0NG_Eb9abFcVOyBJVTEjPwS-30NesIH7XqS-AAwcu3OIz_FpZvXhedzSl3k6zz0at0I_U9N6axTRmCCnnhanQ7LmW8OSPRy0SWk4fd9oZ95RSbxZ8XYI28ucyINR8i9AYFtz1qDFDIkd11iizWJjEHnqErfnjlm_3WRWNxKoTFwSal8Vh14UeDvDosx6_d2EOki-_Bf1CKCxyT_3biIkwoBChd6iODabpmr6edjArSZBwcrbfsytULDYizTXGgB9upgbawkAQacsk8luHmMUvWBT8CvrFsxW49kMWVtuqX4G42NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه «هیل»: بر پایه یک نظرسنجی تازه، نزدیک به هفت نفر از هر ده آمریکایی می‌خواهند جنگ با ایران «هرچه زودتر» پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125200" target="_blank">📅 08:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125199">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acn-PFUiLkW92nWdfdNKZ5g70PxIhX6H0aFbZ142bX4Z_Jr677LruZlOAqy0DyVB5ebS0VTv5hTWDauLxllFpjTOOZi5Tc_f2EzaJs_ZTTPgSfvMDny_cbMQ_UdgSMcTGlp2HE04AfJ6rF4d1iGeYla7t5LxkODkVAIJ8jnbWEmBwMbDf1VNLpRh5cA3-jD15DFxmoBmqd8yqPDbHP1weh_jSz1apdccTsU_1PPWZDzytsVrJVnf-HrJ3e-JDDezg2pdT8W36jLVWokrR0YgV_mAaD8kGcSrOaj3ZrD-C2QtygiCL5A9qcc87WO3_TNWtUjZvihAc9qUgXnqhi407w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت وحشتناک و باورنکردنی ۴ قلم جهاز منزل
... !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/125199" target="_blank">📅 08:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125198">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رویترز: بر اساس اسناد افشا شده پنتاگون، «استارلینک» با کمک دیش‌های قاچاق شده به ایران، ستون فقرات شبکه نظامی آمریکا برای هدایت پهپادهای انتحاری مانند لوکاس در حمله به ایران بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/125198" target="_blank">📅 08:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125197">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرگزاری دولتی چین: شی جین پینگ، رئیس جمهور چین بین 8 تا 9 ژوئن به کره شمالی سفر خواهد کرد. این اولین سفر او به این کشور در 7 سال اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/125197" target="_blank">📅 08:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125196">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
در تازه‌ترین نشانه از عمق تأثیر جنگ بر اقتصاد منطقه، شرکت هواپیمایی امارات مجبور شده نزدیک به نیم‌میلیون صندلی را از برنامۀ پروازی این ماه خود را حذف کند؛ رقمی که معادل ۱۶ درصد ظرفیت پروازی این شرکت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125196" target="_blank">📅 08:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رویترز: بارگیری نفت خام در بندر مینا الفحل در عمان پس از انفجاری که گمان می‌رود ناشی از حمله پهپادی باشد، متوقف شد
✅
@AloNews
خبر جناب</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/125195" target="_blank">📅 08:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nhYTmpk_fZ7n0MeRHmh3HlynNST4NHPxSbLIoP91yhayE-4KoKkhEzVveg2lL4Nf1nOU_sHJVHqEkpoyk1JtC3R_svw4Er7MJ5rGyhKd_bIlqL8UgDDdmvBytK8YylsnmQqNqlgvS8T3q6l33b2E4mpmUvt068nUwSBxabosUxm-hlLxiYJI38t2VaujfUmvCqoBYPJj7A-We3D0Am6R80p7afc45Lg4alhK6Oyf8YnK8BSUnU8YjRuv41QlX4GxNK72JUohOnoIABRC66TnnwlYNOtMb6N0htgsa0LGBsCs4lwnd2pSDuCoB4ULxVpyY9DxBVr61pvMKjlyI0GiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JT5aSoad0vjWp-vzHVxVb8fkAOmfSb1ZKN_ukpIVddoue1_70K1Wnx1m79vO6i7Cbj6XPWmAiiwD5vysngGokRL1yTVng-8LKquVFe4A32ARdQRiT0URfJ9ppUcJrM8eCwpG7Ujlamd26wfdg2XZsWj2bXN865bHZr7vPzQqtz2Jk_udbJQhSxzOC0YiOM1NBiGwsXypSe2_Sskdny2hQs_A_iNYdBbPwUmoKz93dJ4bAJbjqh6lS_2iiVXxMyg-q-WIsecWR_XiJKwmvz196UvGldYkUgbaNMgCBds_zaNlX1xQ5WiH1jOB3bBx-Bx_N9sL0J7ZL7z2f0zh9oTgmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید و اختصاصی CNN خسارت وارده به ناو هواپیمابر USS Gerald R. Ford (CVN-78) پس از یک «آتش‌سوزی در بخش لباسشویی» روی این کشتی را نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/125193" target="_blank">📅 07:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
«یادداشت تفاهم در مرحله نهایی خود قرار دارد و در انتظار موضع نهایی، چه مثبت و چه منفی، است.
🔴
تا این لحظه هنوز در تهران تصمیم نهایی اتخاذ نشده و واشنگتن در حال انتظار است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/125192" target="_blank">📅 07:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoJF-tSozp0oWP5EIgli1-86jxi-iiMqjXcI5SWLrXSWEPoaUHopHm6Ku8rl7P4OAlMwk4vQUVfh8n2Hfk1J9ZAvdr3nCCrjALBSGgFhocwvBHOPmGuN17NLQcPF6Hv3mOeLfvjQB21J3R4ZIS2XB7SwRXzjMsTYuIG-AEJil1zaNRpWs81m6W5UDptoNKZ5s_A2NIfYcKNxMjXClb479-7XweEMI-fhvUcR-NVDNRrQ1CCPVyD9JhepdbwckeiJONoBVSUeGHy1lZLL5CWpAeVKcrPiD8CtJL0YuKzo7ExoYYDyrKtJwT2xJVOPAlXglOnEo1u8O1ps8bKhpY-KNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/125191" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
محسن رضایی : یک سیلی دیگر ممکن است بیاید تا اسرائیل و آمریکا را سر جای خودشان بنشاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/125190" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39099454ea.mp4?token=Gc-QEw9gkGSF9RO72H1h0G4tFX5ANUXL-W6zaAA-i4VDJpfiYL4cD8uQCpf5RmEVGWr2-BusWPAvG5yNrQDDLmo3RCPwBgfB6N_G1hYU7zIabr-_k8T5gd1FnAd0Imaupl3oJA7DaBn04g2O8tJ4q4iiYRQGnBOgFtKzKn-ICBf07A9qdomTSgc0PRP3EUcKA2Jc_s0Uhw7qxmnuXdUXPEkw7O1loi5dXbF1m1cwCJaS7STesIlq1wBza6Cjx4Sv6-FSUVNRymQF1Ez9u_N0W0Dy8fPLw6pkCTuwQzcO2fqGrJgEScAUdrsTUBAMP5ZiQNVhopMTn_hCztgCM0DvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39099454ea.mp4?token=Gc-QEw9gkGSF9RO72H1h0G4tFX5ANUXL-W6zaAA-i4VDJpfiYL4cD8uQCpf5RmEVGWr2-BusWPAvG5yNrQDDLmo3RCPwBgfB6N_G1hYU7zIabr-_k8T5gd1FnAd0Imaupl3oJA7DaBn04g2O8tJ4q4iiYRQGnBOgFtKzKn-ICBf07A9qdomTSgc0PRP3EUcKA2Jc_s0Uhw7qxmnuXdUXPEkw7O1loi5dXbF1m1cwCJaS7STesIlq1wBza6Cjx4Sv6-FSUVNRymQF1Ez9u_N0W0Dy8fPLw6pkCTuwQzcO2fqGrJgEScAUdrsTUBAMP5ZiQNVhopMTn_hCztgCM0DvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما:
پولی در قطر نداریم، پول ایران در آلمان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/125189" target="_blank">📅 01:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hauNn7vxMNxt7pXSpaaeT_bp-PJ-L7lQnMLGeSa4SRwFzxVC9lCFVNbsi_OscNsWx9eK8382qqahQgnMxrL9Wx7CZtLSfOvJdmFQyVyJV4w14B_FlTaHlmlix5fTid1LSYlxQBidcJ3cj7dLpYjfMSI8H5hDaAlB96TskPNArYNcdmyCJnj1QPTaeXjZI-3sc8XTnf-WJiKzo06WZ6SExOTrbGbIHKT0pctDeRS--SSxC2j0ubCMOPunL-eAtaEPxj3M5WhsNduMUUYTETOSb_lEsOcQLuX54o-pmkGSPq902r4b1aReEeCn3YtXqsedBl0RzJAAEz4OUXk6jiVkNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید اتاق جنگ اسرائیل:
⌛️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/125188" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ ۲۵ بهمن ۱۴۰۴:
میخوام با آیت الله علی خامنه ای دیدار کنم.
🔴
ترامپ ۱۴ خرداد ۱۴۰۵:
میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/125187" target="_blank">📅 00:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374fcdaf63.mp4?token=jiK6hI360X5LOPokPVDj7JVzLSr6R-7nHYuQzTaMxDpcf5RDUe_5z92LyRLXoxLe-Wsclj-HbYhyu-bkW_TAVlJPYfDt16RWpUHuzdOmdUUl4wmeIQkVKFXigRfuAZnK2-pp-8DRE0KlwQuX8b5IIYvkF9OZkkN9YvYELXZIT_tbkZjmrFuNJ6zwPxhgv3_FpfbTdetzvUJX8tT3SD4QSYHJ5Zix-kjbM_eMjZWrBqHqdUXdQr2y2YGwRNXO-1v0-S71uk8BHV7vZexuZFqHXCr_QzwCTmEMCnJN3iqp5Oio0vkmfZkNRKYQxAxg1BZ9e5PHIjJS4F2pVJIm1gj6mwfbJv6m0UGUSdDtymPlwPdfebTY4MylnA4M5TbK8axEQ04d0MdlxjQa7LrWEYc1DXZywdoZTinbQEfhv0TZSkBpXrAb8J83JG6bzAcdj4_sOIS8buDCLRsxK_clGcaXnJq_37T656yOdioXZZNeswh-7VIpW23iNAG6dwfCuv8gF2xgto6q30Kpp2-30sdveANpN8IjMcEZFE11U041VVK-y5-zYvOJA5MI9QqUFUuwmroZrl6EmaC_M5exQrHfGdfLZvF4CQiTcHH71zzgMiYMXmvUfZl4SNqjM-2hZIR-1C9tNIED0fZkD5Th5g0E4EN6Y5Kgw_X49fmZ3BxVro0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374fcdaf63.mp4?token=jiK6hI360X5LOPokPVDj7JVzLSr6R-7nHYuQzTaMxDpcf5RDUe_5z92LyRLXoxLe-Wsclj-HbYhyu-bkW_TAVlJPYfDt16RWpUHuzdOmdUUl4wmeIQkVKFXigRfuAZnK2-pp-8DRE0KlwQuX8b5IIYvkF9OZkkN9YvYELXZIT_tbkZjmrFuNJ6zwPxhgv3_FpfbTdetzvUJX8tT3SD4QSYHJ5Zix-kjbM_eMjZWrBqHqdUXdQr2y2YGwRNXO-1v0-S71uk8BHV7vZexuZFqHXCr_QzwCTmEMCnJN3iqp5Oio0vkmfZkNRKYQxAxg1BZ9e5PHIjJS4F2pVJIm1gj6mwfbJv6m0UGUSdDtymPlwPdfebTY4MylnA4M5TbK8axEQ04d0MdlxjQa7LrWEYc1DXZywdoZTinbQEfhv0TZSkBpXrAb8J83JG6bzAcdj4_sOIS8buDCLRsxK_clGcaXnJq_37T656yOdioXZZNeswh-7VIpW23iNAG6dwfCuv8gF2xgto6q30Kpp2-30sdveANpN8IjMcEZFE11U041VVK-y5-zYvOJA5MI9QqUFUuwmroZrl6EmaC_M5exQrHfGdfLZvF4CQiTcHH71zzgMiYMXmvUfZl4SNqjM-2hZIR-1C9tNIED0fZkD5Th5g0E4EN6Y5Kgw_X49fmZ3BxVro0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی:  اگر اسرائیل به سمت جنوب بیروت می رفت، موشک باران را شروع می کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/125186" target="_blank">📅 00:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ایالات متحده رئیس‌جمهور کوبا، میگل دیاز-کانل و خانواده‌اش را تحریم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/125185" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThbcSuV0YEfBTTURtPDhmghi44y7wJRzYXGvuEYpCToxxUHV8qd9Aykga6FfGLNVWgGKvtbOglZ5c4KaLQBDDM3Uu7bBKUxunRiJEKea1pvjhnTIgIhMORcePSLREsdmirghtzr7XYXg3p6sCYujUd6DVbz8mHit7kh98OqPcLahlwO_1sQndokQZVSRQT6Xrh4FcIYBdIeAjfPkY70qqML_cblUWcSh_Wd0FETxS8gL90_RxdDX2Xis-Kt9f7EDmCrduivv5ppSFBCxj8EVuU5_H2hjloZNzlAsJSVDIVj97h-E22j_mk1-3oAocPasBXchrFv2LlDvO2BLE15xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه منتشر کرد: عکس وزیر کشور پاکستان محسن نقوی در دیدار با وزیر کشور ایران در تهران، در چارچوب تلاش‌های اسلام‌آباد برای پیشبرد مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/125184" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: باعث افتخارمه با آیت الله مجتبی خامنه ای دیدار داشته باشم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/125183" target="_blank">📅 00:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vto8vZMtv6ZCJe--WER-CCOM_sa8aeyu6ClUu6pBBP00XxCgd7ExyvdtJ4B6gyLEmx6sPB5tNcuP_s3wgR3Pe4lH7-eE-lJIsZCxdh9SbO5Sd7HexUkAjctB69OTZQQMPw3iPRCHlx0WjQDVpbtBiYJIl2ks2iFLZLaQ3kLOPpNoP9BORrv_UYIDBXqWmemWPp56lPXBbl3Oplr1wROBg8sY6wZpmBjjsaveqZ1lVH6lS6Mu6hOMqV2_anAS6kU5tJnT0Ifr91b9ukAZXCl0OZSMNnOBLtUCNEF3-mididQujYuNKSchQtHTdMFhXXxYLGZtikaOesJq2b2sSZUtqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم قابل توجهی از ترابری های آمریکا در حال خروج از خاورمیانه و حرکت به سمت اروپا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/125182" target="_blank">📅 00:20 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
