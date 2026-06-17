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
<img src="https://cdn4.telesco.pe/file/af_kEbLVZVYo8bUQMQglYS4c7L2xGneVevks8XljTBoTCNlUxZPo4Jm7VrlJQCjFG84BUM0rfFtDpeT7nn7-vPL0lBLR7fEj0cJYN3wQtPwByjTL-OlbEZVwJK5xNFkWMrbKSu9Bzx9HVpJGabHDlASEHT6xD-tULj1x6HCdLI8UOz7k0zZXy0JbLrHsto7MGHHZPIK58QT_VeXFiiQ9ysPSnKOaQ0St7c6r1ChQT3_fBqcacT22tKqnfNnrs2SfMgeJz32bgZf36lIfJzKiJlWIoUxSpbAacWFIFHc5fA7dQ91qW8cI-k6m4XTRmk9ifUzUltAj3tLzcSQHZR-LHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-17671">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔵
پاول دوروف ؛ مالک تلگرام
:
دولت بریتانیا می‌خواهد استفاده از شبکه‌های اجتماعی را برای کودکان زیر ۱۶ سال ممنوع کند.
اما ممنوع کردن شبکه‌های اجتماعی برای کودکان فقط آن‌ها را در معرض خطر بیشتری قرار می‌دهد.
آن‌ها مجبور خواهند شد از VPN استفاده کنند و به محتوای غیرقانونی بسیار بدتری دسترسی پیدا کنند.
ما قبلاً این را دیده‌ایم.
وقتی دولت روسیه تلگرام را ممنوع کرد، ۹۵٪ نوجوانان روسی همچنان از آن استفاده کردند. آن‌ها فقط به VPN منتقل شدند. همین‌طور در ایران</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SBoxxx/17671" target="_blank">📅 13:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17670">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfK1dMLWRL0baEjrjb6XtIVoFDkQBxpQm-UFzaNoYVOMvwQfey939xVo7FkBsKsI8LKKTg5xrGSnhTCqqiVgzA-faDGo5R5WlGlTJmxLJGrA7xPH3iHHfAZ6Kvd_ryBQVoQ1W2egfwDAXE03TrRvFjSH9fR9tiWGszFNh4EeFBAgpAxLDkwuFy8M1X8vcQ09vNIv43cbj_6feFH22vyik-nAwqlA1lOHUHTWjAcdUrNi_1fmadaQEg-XqbQqf1bxRnYbWfa3jqxqSKwahjep25n6kf5jR8kUn5yQLcgI42CRZDBkPLnLHMOD7Q-1h6Ey0zA0NvYtWcTGyGf6TDG99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای باری نظامی امارات در پایگاه نواتیم اسرائیل فرود آمد
در ۱۵ ژوئن ۲۰۲۶، یک هواپیمای باری ایلوشین Il-76TD متعلق به امارات از ابوظبی به پایگاه هوایی نواتیم اسرائیل پرواز کرد. این پرواز از حریم هوایی عربستان عبور کرد.
این رویداد، نشانه‌ای از همکاری نظامی رو به گسترش و عمیق‌تر امارات و اسرائیل در برابر تهدید موشکی و پهپادی ایران است. پایگاه نواتیم یکی از مراکز کلیدی نیروی هوایی اسرائیل است.
گزارش‌ها همچنین حاکی از استقرار سیستم
گنبد آهنین
اسرائیل و پرسنل نظامی آن در امارات پس از حملات ایران است. این پرواز احتمالاً برای انتقال تجهیزات، مهمات یا لوازم پشتیبانی دفاع موشکی انجام شده.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/17670" target="_blank">📅 12:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17669">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.   خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SBoxxx/17669" target="_blank">📅 12:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17668">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcVMGZtDn-lMbjIixjOqBhI3rUCoS3BASjtWO0wLr5Nv7kErjW_InzZBCyl0xATHxENtlNUZbhsrISxi2epRPFwi_Vztse5ch8kminXXwoKIyKARhU8V0IiX1WjyflzF_ElU-6_ZI5rW6P9FmQzgtKi2XoZS03onUqPAJT4o0SJU3rItuUeOI4K4kZvlgUmrsw7L9Lj_y25mocJKTkFDLq0rHCgZxakinu5oz6ZN54whLRuGWnR3BGJSPzNAVzoZlIOgsHgUDaqnqvamCWR6XQIGGYPrwSkOX2sRkDAhxtXVSkKr_pM0EnKnyTOMFg7-rh19BpipzFar7nynoWrhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.
خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع یا تشدید درگیری‌های مرتبط با جنگ ایران، به شدت افت کرده و به حدود ۲۵-۳۰٪ در ژوئن رسیده است.
این سقوط با منطقه زمانی خاکستری “جنگ ایران” همخوانی دارد که از اواخر فوریه تا ژوئن را پوشش می‌دهد.
در مقابل، خط آبی نفتالی بنت (حدود ۲۰-۴۰٪) نوسان داشته اما اخیراً پایدارتر است. خط سبز گادی ایزنکوت از نزدیک صفر شروع کرده، به تدریج افزایش یافته و در ژوئن به حدود ۳۵٪ رسیده و حتی از نتانیاهو پیشی گرفته است.
این روند نشان‌دهنده نارضایتی عمومی اسرائیلی‌ها از نتیجه جنگ ایران است؛ افکار عمومی معتقدند اهداف اصلی (مانند نابودی کامل برنامه هسته‌ای و نیابتی هایش) محقق نشده و این امر به ضرر نتانیاهو تمام شده است.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/17668" target="_blank">📅 11:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17667">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بدون تصویب مجلس این توافق اعتبار ندارد  حسینعلی حاجی دلیگانی، نماینده مجلس:  طبق قانون اساسی هر توافق و عهدنامه بین‌المللی باید به تصویب مجلس برسد و بعد در شورای نگهبان تایید شود وگرنه وجه قانونی ندارد و باطل است.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/17667" target="_blank">📅 11:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17666">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بدون تصویب مجلس این توافق اعتبار ندارد
حسینعلی حاجی دلیگانی، نماینده مجلس:
طبق قانون اساسی هر توافق و عهدنامه بین‌المللی باید به تصویب مجلس برسد و بعد در شورای نگهبان تایید شود وگرنه وجه قانونی ندارد و باطل است.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/17666" target="_blank">📅 11:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17665">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgXnGWnOxYDM92-lN9MJzof0VA3Hhac2XHiR_HD0K4KNmHzT2IuBYvt8NzoPx4sB_EULqq1tF5xLYLM2S2ZXT5DoJP--QByC2ZZPrlk4BE5MYu6iDeJW2YPTS0_dhWHjoGaNKNyXmlrjD2fi_SI8A9hfZJZv40d2T5UCnxfbKUtP3JZHfjulP4WkuEUk_kfWdgDpqMQv-J0wmkhhPGM-Ip-MZwz_VoPvZ41kk1aBPezbEJjVoP231wlJY_c8UEVX02Yh_7NmpIHYVV9o_fTeOUQmUrj-mXjEpb8-eWE0PfopQszFMdybqXzsu5jePYmisnl6x6rSUEbFBgfNXaFi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناتو در حال استقرار سامانه دفاع موشکی SAMP-T ایتالیایی در قونیه ترکیه
سامانه SAMP-T که به طور مشترک توسط فرانسه و ایتالیا توسعه یافته است، یک سامانه موشکی زمین به هوای متحرک است که قادر به رهگیری هواپیماهای جنگنده، پهپادها، موشک‌های کروز و برخی موشک‌های بالستیک است.
این استقرار در میان تنش‌های فزاینده منطقه‌ای پس از آغاز جنگ در خاورمیانه رخ می‌دهد، که نیروهای ناتو در ترکیه موشک‌های بالستیک ایرانی را در ۴ مورد جداگانه از فوریه رهگیری کرده‌اند.
یک آتشبار موشکی پاتریوت  اضافی نیز در پایگاه هوایی اینجیرلیک در جنوب ترکیه مستقر شده است.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/17665" target="_blank">📅 10:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17664">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اسموتریچ:
«تا جمعه از جنوب لبنان عقب‌نشینی نخواهیم کرد - و بعد از جمعه هم عقب نشینی نخواهیم کرد.»</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/17664" target="_blank">📅 10:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17663">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ونس ۱۴۰۵ = مرفاوی ۱۳۸۵
سبحان الله!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/17663" target="_blank">📅 10:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17662">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">طبق گزارش NBS؛ از روز یکشنبه که تفاهم‌نامه به‌صورت دیجیتال امضا شده، هر شب ایران چندین پهپاد پرتاب می‌کند.
یک مقام آمریکایی گفته این پهپادها توسط سپاه پاسداران پرتاب می‌شوند و نیروهای آمریکایی آن‌ها را قبل از اینکه تهدیدی برای کشتیرانی تجاری، ناوهای نظامی یا نیروهای منطقه ایجاد کنند، رهگیری و ساقط کرده‌اند.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17662" target="_blank">📅 01:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17661">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جی دی ونس:   تفاهم‌نامه ایران، شامل لبنان هم می‌شود</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17661" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17660">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سفیر آمریکا در اسرائیل، مایک هاکابی، مجدداً تأکید می‌کند که حزب‌الله در توافق بین آمریکا و ایران گنجانده نشده است. این در حالی که تهران همچنان اصرار دارد که بر اساس شرایط این توافق، اسرائیل باید عملیات خود در لبنان را متوقف کند.  در پاسخ به ادعای حزب‌الله…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17660" target="_blank">📅 01:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برخی کانالهای ایرانی خبر داده اند که قطری ها برای راضی کردن ویتکاف و کوشنر جهت فشار بر ترامپ برای پرهیز از جنگ دوباره و امضای توافق، یک هتل نیمه کاره 5-ستاره در دوحه را به این دو نفر هدیه داده اند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17659" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تیم فرانسه به روزی افتاده که بلوندشان شده امباپه!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17658" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش حملات پهپادی سپاه پاسداران به اربیل عراق   سبحان الله !</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17657" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17656" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">— سفیر ایالات متحده در اسرائیل مایک هاکابی:
«بدون اسرائیل، آمریکایی وجود نخواهد داشت.
وجود ما مدیون چیزی است که در این سرزمین رخ داد».</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17655" target="_blank">📅 22:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرد در صورتی که اسرائیل حملات خود به جنوب لبنان را متوقف نکند، باید منتظر پاسخ سختی از سوی نیروهای مسلح ایران باشد</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17654" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17653">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این مسئله لبنان حل نشود کل توافق روی هوا خواهدرفت. مگر اینکه طبق حدس من اساساً از همان آوریل حزب الله را معامله کرده باشند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17653" target="_blank">📅 22:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17652">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzodvcT1v46vf5KoA6OiQSG4RvV09AdRIVIzrjehpTYMbpFplHssjmNSmu1GjIqLT4lxv8HUzBw9NyJRXYACa_N3Tly-FY34QDAVOaKcEmwHzr_80pQjUgbIvyAgvKMiA59aYoZsrfBsbhfXz4O8gkHtG8JdhaokUAQWQQx2jeUZ6YyRhGYFLtH53rKL4vWNOpeYZKyoIGzEpx0QCzoaCQReyu_vcbulPtYit8qFvLwt3O4eM3Z8FJh1oT6jqj10b5mYUIH_qDp-Js6Xbg_tj-coG702xA_sQM7XSCEvyAcrzNpvkoQtMHvsEIgZo0aALrGDxgg3VhnQ-7e5R52tJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نبیه بری و قالیباف در یک تماس تلفنی:   اسرائیل باید ملزم به توقف تخریب روستاهای لبنان و عقب‌نشینی از سرزمین‌های اشغالی شود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17652" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده بلافاصله پس از امضای توافقنامه در این هفته تحریم‌های فروش نفت و سوخت ایران را لغو خواهد کرد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17651" target="_blank">📅 20:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq8_jT7_Gz8bHvkcisd_H6IxTMXDAbXKDAGe3X4pXF7jL7BOGQ3hfO1oQR8p0BtoXD-w8OeQNwyg3Y7EVkYGX0F-hfzDVtZLjeIpdBVbgwTooHTv4_d5YVOTUExf7i9gI9C8I2gpVgXvFKjTEsVQ7iurfbh_UdyNBicvqABS7ODFYDtqL1KnBFGmNkVkye3iODk5OnXpuJwLfw2nEdIQAn3hVo4KkJLFKoHG60hIeQCmNhK-7AeDjU53RR_xJzlkeIRet0t9zjPZ3tlg7_p5sdMCaoBiRNao9wZdiEDe0dKxsW6ghWgf_imGPQUyYHzMtVTZIpYhDLTj_ohgF4nXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17650" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1wF-VNGsX6_645-cl2wYUSXfx00IOSv83-yn5kKF7sHmfmLySfW_jPf6aH1Zow-VEbi4Vg8T2TvGBv6c_-oJ5yGZH00-a-USi7We-7ORD7Ujyiyb4BMo-FRa-fYkmZ3IpDAFrfuszDaI53klLDd4bdN702r78eLoNx3BJgvpuLBbDKRsFQujIX-XukyEby5oSfoVdW1opuEjo4O5v6Jts77QoTW1rfEaBJvMB7lTgCUCHD8bcvq0IW5azlBObL9mdAzKhO1sGT23i22GMvMA_5LaKTu_hZVokbIeWHl85eOLM2777jaD5b1uVmBSKZfDZYm9uOU6uTiSHQkn1UScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL
— H2
در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17649" target="_blank">📅 20:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWEYCRIG7cIA9d2zj9W5-q1wdXuPWzy2hSM1pol2VkwJUy_LeJXh-bbHimZkY4pap4QG443Sd89d-sb_1ipuB7esVbnv8eEngCBTJUjYCH4JpYI4x6heZ3vXDhjeA22iegeAk3bpm0oVJPHR98y2NY7LY_3XM0BaY6vxBXytXKxuMeSiplTLjwZI6TZAxUGe03AlPOclAjmweyLhptMKzxsI1o8BmRibO-jNRKvXIi-00uVWKm5ASSpLiOZNDeYPiw-s_YS-tNzfjxh_-Jxahrtlb7UnxM-YN8OtUydoeTBYYeck2UiGjZgCbrIYzsqN5ttkivotEnS9-2CcYfXo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت جانفدایان</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17648" target="_blank">📅 20:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برآوردهای اطلاعاتی آمریکا: ایران از این پس هر زمان که بخواهد قادر خواهد بود تنگه هرمز را مسدود کند. «این سلاحی قوی‌تر از هسته‌ای است» (سی‌ان‌ان)</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17647" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">العربیه به نقل از منبع آگاه دربارهٔ سند توافق:  سند توافق بر پایان فوری و دائمی جنگ در تمامی جبهه‌ها تأکید دارد.
🔸
سند توافق بر پایان فوری و دائمی جنگ در لبنان تأکید دارد.
🔸
ایالات متحده و ایران بر اساس این توافق متعهد می‌شوند که هیچ‌گونه «اقدام خصمانه‌ای» علیه یکدیگر انجام ندهند.
🔸
ایالات متحده و ایران طبق این توافق از دخالت در امور داخلی یکدیگر خودداری خواهند کرد.
🔸
سند تفاهم میان ایران و آمریکا تأیید می‌کند که مهلت مذاکرات با موافقت دو طرف قابل تمدید است.
🔸
آمریکا بر اساس سند تفاهم، بلافاصله پس از امضای توافق، محاصره دریایی ایران را لغو خواهد کرد.
🔸
آمریکا طبق این تفاهم متعهد می‌شود که ظرف ۳۰ روز پس از توافق نهایی، نیروهای خود را از مناطق پیرامون ایران خارج کند
🔸
ایران بر اساس این تفاهم، اقداماتی را برای تضمین ازسرگیری تردد کشتی‌های تجاری در تنگه هرمز انجام خواهد داد.
🔸
ایران بر اساس این توافق موظف است مین‌های دریایی موجود در تنگه هرمز را پاکسازی و برچیند.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17646" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چین می‌گوید مرحله بعدی مذاکرات آمریکا و ایران «سخت‌تر» خواهد بود
وزیرخارجه چین روز سه‌شنبه به همتای پاکستانی خود گفت که مرحله پیش‌رو از مذاکرات بین آمریکا و ایران انتظار می‌رود «سخت‌تر» باشد.
وزیر امور خارجه چین، وانگ یی در تماس تلفنی با اسحاق دار از پاکستان پیش از امضای برنامه‌ریزی شده یادداشت تفاهم آمریکا و ایران در روز جمعه، ، گفت که «قابل پیش‌بینی است که، در مقایسه با مرحله اول، مرحله دوم مذاکرات سخت‌تر خواهد بود.»
طبق بیانیه وزارت امور خارجه چین، وانگ همچنین گفت که شورای امنیت سازمان ملل «باید نقش بیشتری» در حمایت از مذاکرات ایفا کند.
«اجماع کنونی فاصله زیادی با مقصد نهایی دارد، بلکه یک نقطه شروع جدید است».
«دستیابی به صلح پایدار در خاورمیانه و منطقه خلیج فارس هنوز نیازمند تلاش‌های بی‌وقفه همه طرف‌ها است»، وانگ افزود و گفت که چین آماده همکاری با پاکستان در پیشبرد ابتکارات صلح است.
(خبرگزاری فرانسه)</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17645" target="_blank">📅 18:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2hKxCF01smkSuIsB6wUDyMVH3Bnbu4Yr3QejoSnJ_4I6LyKn-ZHQsLY6n-fzG2TJLbl2QsmXCzam5vap0h6T-QIlhgbkv7FC74yiOkaNb7n2nF0yJbn5yCj5GvXaiBx7XzdDEc7BMc6CzCpmKl6fBrbvTVhmXj9WwKeUok-jTiItEcUym0ykgpHRuwvF5nJ2-R_QR35-f_fb7EapuSlXw8CjqLOEIykX8Yuhp9bBp80e4MYvt0WvBtN3_wwdllq8BC-Xs4_do5eQFeSaZ5dS5UXItWufDOpDS5XhH2lm7X0zA3k3dRgtJCbOEevZEX9ewpfXlkxXbZxCw60MRC-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نشست فدرال رزرو: چرا نخستین حضور کوین وارش از خودِ تصمیم نرخ بهره مهم‌تر است؟
نشست ژوئن فدرال رزرو بیش از آنکه به تصمیم نرخ بهره مربوط باشد، بر نخستین حضور کوین وارش به‌عنوان رئیس جدید متمرکز است؛ فردی که می‌تواند رویکردی متفاوت در سیاست‌گذاری و ارتباطات بانک مرکزی آمریکا ایجاد کند.
سرمایه‌گذاران به دنبال نشانه‌هایی از مسیر آینده سیاست پولی هستند و انتظار دارند اظهارات وارش درباره تورم، نرخ بهره و استقلال فدرال رزرو تأثیر بیشتری از خودِ تصمیم نرخ بهره بر بازارها داشته باشد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17644" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ادامه ترورهای اسراییل ضد حزب الله در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17643" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سوگمندانه جامعه سرمایه گذاری جهانی خیلی به تهدیدات ما اهمیت نداد و فقط شرکت SpaceX ماسک ملعون پس از عرضه اولیه دیروز به ارزش بازار 2.2 هزار میلیارد دلار رسید!  دقت کنید 2200 میلیارد دلار!  ثروت خود ماسک نیز از 1000 میلیارد دلار فراتر رفت.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17642" target="_blank">📅 17:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ونس می‌گوید بازرسان هسته‌ای «قطعاً» بر اساس توافق ایالات متحده به ایران بازخواهند گشت
ونس در مصاحبه‌ای روز دوشنبه با شبکه خبری ان‌بی‌سی اعلام کرد که بازرسان هسته‌ای «قطعاً» اجازه بازگشت به ایران را در چارچوب توافقی با ایالات متحده خواهند داشت.
«در واقع، یکی از بخش‌های اصلی این توافق این است که (آژانس بین‌المللی انرژی اتمی) و ایالات متحده به ایران کمک خواهند کرد تا ذخایر غنی‌سازی شده را نابود کنند و این موضوع به‌طور بسیار شفاف در یادداشت تفاهم قبلاً توافق شده بین واشنگتن و تهران ذکر شده است»،
ونس همچنین اذعان کرد که یادداشت تفاهم مقدماتی مسائل دشوار، به‌ویژه برنامه هسته‌ای ایران را فعلاً حل‌نشده باقی می‌گذارد.
«یادداشت تفاهم حدود یک و نیم صفحه است، بنابراین سند بسیار کلی است»، ونس به سی‌ان‌ان گفت.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17641" target="_blank">📅 17:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17640" target="_blank">📅 17:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وقتی میگوییم ابهام یعنی همین که الان ایران می‌گوید نه تنها باید آتش بس در لبنان برقرار بشود بلکه اسراییل باید از سرزمین های متصرفه عقب نشینی هم بکند اما در سوی مقابل اسراییل دنبال پیشروی بیشتر در خاک لبنان است و ترامپ هم می‌گوید جنگ در لبنان ربطی به توافق با ایران ندارد!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17639" target="_blank">📅 15:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: اگر اسرائیل به لبنان حمله کند، باز هم توافق می‌تواند دوام بیاورد</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17638" target="_blank">📅 14:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17637">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:   قطر و ایران مرز زمینی مشترک دارند و می‌توان از یکی به دیگری پیاده رفت.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17637" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17636">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
قطر و ایران مرز زمینی مشترک دارند و می‌توان از یکی به دیگری پیاده رفت.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17636" target="_blank">📅 13:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17635">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc72PNvfhuwYc-SKnSvwwMr-1Zbaa_zG_smB-RRmTJufnKdQadEsT_vRhYhUjONUPTgMxFQGIpzeC0JFPkRyy3Jce-Uq0EiFAonVYiqxeZUFts_WB9RYnLdidf2Tvyfo4KRqTvWzNKjqBhdtsATvuzQb8_QyyahqBuL4M-faYiB3bycU3GbsO8iVMA40-sb6-vbFgH_UjRnbxk_nYL2c99bs_dEfIQ7XMozjjctCuj6qG5ZxnWMoIBXjd1M3Wn9odaPJ_8DhMXoBz-qW5jHiUxoEoUZAq3ThP8pyAtUQbmam9XNmNWCrJ-TjTbfp37jFVdj06bycTd9z2bB2dB7zyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سطح اطمینان کاربران پیام‌رسان های داخلی از پایداری اتصال:</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17635" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17634">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17634" target="_blank">📅 13:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17633">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این هم سندی که در پست ریپلای شده در Secret Box قرار داده شد:
ترامپ: اگر اسرائیل نتواند کار را بدون این همه کشتار انجام دهد، سوریه باید این کار را انجام دهد|</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17633" target="_blank">📅 13:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17632">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: من از نتانیاهو خشمگین نیستم!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17632" target="_blank">📅 13:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17631">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خود لبنان نادیده گرفته شده بعد اینها دنبال اضافه شدن غزه هستند!  چی در فلافل هایتان میریزید؟</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17631" target="_blank">📅 13:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17630">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17630" target="_blank">📅 13:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17629">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17629" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17628">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تیم پروفسور رولکص آبادی مقابل ضعیف ترین تیم گروه به زور مساوی کرد و از شکست گریخت!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17628" target="_blank">📅 13:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17627">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: توافق ایران یک توافق عادلانه و خوب است</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17627" target="_blank">📅 13:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17626">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: توافق ایران یک توافق عادلانه و خوب است</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17626" target="_blank">📅 13:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17625">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">https://telegra.ph/%D9%85%D8%B1%D8%AD%D9%84%D9%87-%D8%A8%D8%B9%D8%AF%DB%8C-%D8%AC%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%B2%DB%8C%D8%B1%D8%B3%D8%A7%D8%AE%D8%AA%E2%80%8C%D9%87%D8%A7-%D8%A8%D9%87-%D9%85%DB%8C%D8%AF%D8%A7%D9%86-%D9%86%D8%A8%D8%B1%D8%AF…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17625" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17623">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این مسئله لبنان حل نشود کل توافق روی هوا خواهدرفت. مگر اینکه طبق حدس من اساساً از همان آوریل حزب الله را معامله کرده باشند.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17623" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17622">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-text">https://telegra.ph/%D9%85%D8%B1%D8%AD%D9%84%D9%87-%D8%A8%D8%B9%D8%AF%DB%8C-%D8%AC%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%B2%DB%8C%D8%B1%D8%B3%D8%A7%D8%AE%D8%AA%E2%80%8C%D9%87%D8%A7-%D8%A8%D9%87-%D9%85%DB%8C%D8%AF%D8%A7%D9%86-%D9%86%D8%A8%D8%B1%D8%AF-%D8%AA%D8%A8%D8%AF%DB%8C%D9%84-%D9%85%DB%8C%E2%80%8C%D8%B4%D9%88%D9%86%D8%AF-06-16
@Iran_Simorq</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17622" target="_blank">📅 11:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17621">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چگونه روسیه غرب را پشت سر گذاشت و افغانستان را به یک متحد استراتژیک تبدیل کرد
(مقاله یک سایت هوادار بلوک جنوب)
مسکو پس از دهه‌ها از زمانی که نیروهای شوروی ابتدا وارد این منطقه شدند، بار دیگر به ایجاد شراکت‌های پایدار و متقابل در افغانستان بازگشته است، اما این بار بدون به‌کارگیری حتی یک تانک یا شلیک یک گلوله. در حالی که قدرت‌های غربی سال‌ها در تحمیل کنترل مطلق بر این منطقه ناکام ماندند، روسیه از طریق دیپلماسی به یک پیروزی ژئوپلیتیکی عظیم دست یافت، فروپاشی کامل نفوذ غرب را آشکار کرد و یک میدان نبرد سابق را به یک متحد قابل اعتماد تبدیل نمود.
با به رسمیت شناختن رسمی طالبان به عنوان دولت مشروع، کرملین یک تعامل محتاطانه را به یک شراکت استراتژیک کامل و جامع تبدیل کرد. این اتحاد فراتر از سیاست صرف است و رونق اقتصادی عظیمی برای هر دو طرف ایجاد می‌کند. روسیه اکنون میلیون‌ها تن سوخت و گندم با تخفیف سنگین را مستقیماً به این منطقه تأمین می‌کند. در مقابل، شرکت‌های روسی به دسترسی انحصاری به ذخایر گسترده مس، لیتیم و مواد معدنی کمیاب دست یافتند که منابع حیاتی را تأمین کرده و رفاه اقتصادی بلندمدت را تضمین می‌کند.
یک پیمان دفاعی جدید در مسکو کانال‌های رسمی اشتراک اطلاعات برای مقابله با تهدیدات منطقه‌ای مشترک مانند داعش خراسان (IS-K) ایجاد می‌کند. علاوه بر این، این همکاری مستقیم کاملاً پاکستان را دور می‌زند و سرانجام بازی دوگانه دهه‌هاه اسلام‌آباد را که میلیاردها دلار کمک خارجی دریافت می‌کرد و در عین حال نیروهای رادیکال منطقه را پرورش می‌داد، پایان می‌دهد.
برای غرب، این یک شکست ساختاری فاجعه‌بار در صفحه شطرنج جهانی است. اوراسیا اکنون به طور محکم تحت کنترل بازیگرانی است که به طور کامل قواعد به اصطلاح مبتنی بر نظم را که نخبگان جهانی تبلیغ می‌کنند، رد می‌کنند. غرب در این بازی بزرگ جدید به شدت شکست می‌خورد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17621" target="_blank">📅 10:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17620">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جیسون برودسکی:
کوشنر در دیدار آوریل خود در اسلام‌آباد با محمدباقر قالیباف، رئیس مجلس ایران، به او صریحاً گفت: اگر قیمت رولزرویس می‌خواهید، باید محصول رولزرویس ارائه دهید.
به عبارت دیگر، اگر ایران با باز نگه‌داشتن تنگه هرمز، توقف غنی‌سازی اورانیوم به مدت ۲۰ سال و توقف صدور انقلاب خود همکاری کند، می‌تواند صدها میلیارد دلار به دست آورد</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17620" target="_blank">📅 09:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17619">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">— جان راتکلیف، مدیر سیا، به ترامپ هشدار داده که ارزیابی‌های اطلاعاتی ایالات متحده نشان می‌دهد ایران ممکن است مایل به اعطای امتیازات هسته‌ای مورد نیاز برای یک توافق نهایی نباشد.
مارکو روبیو، وزیر امور خارجه، و پییت هگست، وزیر دفاع، نگرانی‌های مشابهی را بیان کردند، در حالی که جی‌دی وانس، معاون رئیس‌جمهور، و نمایندگان ویژه ایالات متحده استیو ویتکوف و جرد کوشنر از این توافق حمایت کردند.
اطلاعاتی که توسط مقامات ارشد ایالات متحده بررسی شد، نشان می‌داد که برخی مقامات ایرانی در مورد این توافق به روش‌هایی در داخل بحث می‌کردند که با پیام‌هایی که به میانجی‌گران و مذاکره‌کنندگان ایالات متحده منتقل می‌شد، ناسازگار به نظر می‌رسید.
— اکسیوس</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17619" target="_blank">📅 08:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17618">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شوخی ایرانی ها با تفاخر متعفن قلعه نوعی با ساعت ۱۰ میلیاردی اش!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17618" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17617">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">— ترامپ:
«ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین، این داستان که ایالات متحده ۳۰۰ میلیون دلار به ایران پرداخت می‌کند، خبر جعلی است که توسط دموکرات‌ها منتشر شده است.»</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17617" target="_blank">📅 08:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17616">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری مهر : شنیده شدن صدای سه انفجار در قشم</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17616" target="_blank">📅 01:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17615">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
ایران باید تأمین مالی سازمان‌ های تروریستی خشونت‌ آمیز و عوامل بی‌ثبات کننده در منطقه را متوقف کند! نمی‌توان با اطمینان ۱۰۰٪ گفت که ایران به تمام تعهدات خود پایبند خواهد ماند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17615" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17614">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تسنیم :
رفع محاصره دریایی عملیاتی شد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17614" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17613">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17613" target="_blank">📅 00:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17612">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4237e85c2.mp4?token=sA8aIy6JBP_6UP8h0jyBiEyJ5gWVeJr0f7ev_q_PYwoS0zIL42DNb5AV4QADQ2-bSvSLJ9OJb0MPXZxH7XrBrmUf63-NZAorg3TK2ISQgpauCW3zguKDRQAs9YMMHMYWV3X2BID2c5pNt9KfauUDPFbwe8sl8eO-i0s26tFo03LRXFAqLyTtZ5QISySMACx_hIybIAJHLgmtWns4UCOrVA_K6LwWSU1e0wdeMIkNb1nFWHnbxyTmO9d--G-XB45WVC9yhIKQHssD2uS7Iw9vD3HZobcaWuadpaX7ZPlJ50OaW_O_FsZJ2DOq2pZzjoaIjBd_WnBouLFafgL6kVIyqYHwO-RMAgCCa5cEiKszz5EyWNrf4DdT3-ODiROAqn_32kzhqdoW05UtnkSRQZLcxWcsMO-8HSUX7xcIdS_iIItZJgbmhYuRFiO5962n_fSNz1HKU4IY2fmTXJg-hW2SgKKm0qF94MGQ9smQYwEPjkU39IIMCh4VegYvsx-4DpkCm6-rLrSWtjEL6vbFiVPP2csRN-oB-PWoG3epFdSg9OsUhicd8HT2JTAINjRzX7YWoixh98tUb794uJyPtFopzfREDNqMshLcgfMOWlR8L_PqFsgV0I5TvA1VX5U1wKbNCXqHafMwd2UW1yRFqETUGwLZ2kMMiKn4tAJR6-IEg3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4237e85c2.mp4?token=sA8aIy6JBP_6UP8h0jyBiEyJ5gWVeJr0f7ev_q_PYwoS0zIL42DNb5AV4QADQ2-bSvSLJ9OJb0MPXZxH7XrBrmUf63-NZAorg3TK2ISQgpauCW3zguKDRQAs9YMMHMYWV3X2BID2c5pNt9KfauUDPFbwe8sl8eO-i0s26tFo03LRXFAqLyTtZ5QISySMACx_hIybIAJHLgmtWns4UCOrVA_K6LwWSU1e0wdeMIkNb1nFWHnbxyTmO9d--G-XB45WVC9yhIKQHssD2uS7Iw9vD3HZobcaWuadpaX7ZPlJ50OaW_O_FsZJ2DOq2pZzjoaIjBd_WnBouLFafgL6kVIyqYHwO-RMAgCCa5cEiKszz5EyWNrf4DdT3-ODiROAqn_32kzhqdoW05UtnkSRQZLcxWcsMO-8HSUX7xcIdS_iIItZJgbmhYuRFiO5962n_fSNz1HKU4IY2fmTXJg-hW2SgKKm0qF94MGQ9smQYwEPjkU39IIMCh4VegYvsx-4DpkCm6-rLrSWtjEL6vbFiVPP2csRN-oB-PWoG3epFdSg9OsUhicd8HT2JTAINjRzX7YWoixh98tUb794uJyPtFopzfREDNqMshLcgfMOWlR8L_PqFsgV0I5TvA1VX5U1wKbNCXqHafMwd2UW1yRFqETUGwLZ2kMMiKn4tAJR6-IEg3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسیب دیدن خبرنگار Press TV هنگام حمله پهپادی اسرائیل در لبنان</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17612" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرمانده نیروی قدس سپاه پاسداران: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و در صورت لزوم، برگ‌های دیگری نیز بازی خواهد شد. - صدا و سیما.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17611" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17610">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآذری‌ها |Azariha</strong></div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است
یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.
ایتان لاسری بر این باور است که اسراییل و ترکیه وارد مرحله‌ای از رقابت استراتژیک فزاینده شده‌اند که ممکن است ویژگی‌های خاورمیانه را در سال‌های آینده شکل دهد. وی اشاره کرد که تنش بین دو طرف به بالاترین سطح خود در دهه‌های اخیر رسیده است، اما هنوز از سطح رویارویی نظامی مستقیم فاصله دارد.
کارشناس اسرائیلی ایتان لاسری به ۸ کانون تنش بین اسرائیل و ترکیه اشاره کرده و معتقد است رقابت استراتژیک آن‌ها ممکن است ویژگی‌های منطقه را تعیین کند. مسائلی مانند غزه، سوریه، لبنان، انرژی در مدیترانه، ناوگان‌های رفع محاصره غزه، تقویت ساختارهای دفاعی ترکیه، و نقش آمریکا در تعادل منطقه از جمله این کانون‌ها هستند. لاسری همچنین احتمال جنگ سرد بین دو کشور را در سال‌های آینده بیشتر از جنگ نظامی می‌داند
https://telegra.ph/%DA%A9%D8%A7%D8%B1%D8%B4%D9%86%D8%A7%D8%B3-%D8%A7%D8%B3%D8%B1%D8%A7%DB%8C%DB%8C%D9%84%DB%8C-%D8%AA%D8%B4%D8%B1%DB%8C%D8%AD-%DA%A9%D8%B1%D8%AF-%DB%B8-%DA%A9%D8%A7%D9%86%D9%88%D9%86-%D8%AA%D9%86%D8%B4-%D8%A8%DB%8C%D9%86-%D8%AA%D8%B1%DA%A9%DB%8C%D9%87-%D9%88-%D8%A7%D8%B3%D8%B1%D8%A7%DB%8C%DB%8C%D9%84-%D8%AA%D8%B1%DA%A9%DB%8C%D9%87-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%AC%D8%AF%DB%8C%D8%AF-%D8%A7%D8%B3%D8%AA-06-15
🆔️
@Ir_Azariha</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17610" target="_blank">📅 23:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17609">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17609" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17608">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فوری | نتانیاهو: ما در حال کار برای حفظ آزادی عمل نظامی و ادامه بهره‌مندی از آن هستیم. توافق با ایران توسط ترامپ انجام شد و این تصمیم او بود. ما منافع خودمان را داریم.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17608" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17607">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو: گاهی اوقات من و ترامپ هم‌نظر نیستیم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17607" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17606">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو: گاهی اوقات من و ترامپ هم‌نظر نیستیم.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17606" target="_blank">📅 21:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17605">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع ایالات متحده نیست و ما کشوری مستقل و دارای حاکمیت هستیم! ما شریک این توافق نیستیم که امنیت ما را تضمین نمی‌کند و به هیچ وجه ما را ملزم نمی‌سازد.  نباید در هیچ چیزی کمتر از انحلال…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17605" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17604">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqyYb3khUT9LnHQEjFcCrhgxk-aNoey1QvohVbu1MvaB2rl6Z-xyuSlEoiV2ygXVVaiNXyvWZGBNgV_jY8wlzS1mwfkmiX6RN1qr3mC8uY5ISG0KVXaIKlWSiqnljPpIA2vstVIhjmyRgsawGuiob9Tmy4ZxGuQwKg4OW6C8gYIcsUAWbsDLC1WwYIbpwKQy2Ndxyq-h3sxFEblbjFMUqaI2au6jAe3iBxClpJpwzpFaWnJXVfO7gn6jECiHVSBYMdVn65v33kmr8fFrlRTQK7mwJ9Ym7uUAR3Tvyc_opUn3cdh-Mtx3pWLknxM9frCqYWQp7RYL869xLhBvV2uqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  به نظر دستکم 30 درصد دیگر ریزش داشته باشد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17604" target="_blank">📅 20:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17603">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHJDe9tYiKBRIQS-EuUosaGUOXp5L_b1-eJHmgU5kmQSnGIUfqal0OvPye9ahvFQzLBLnB99Ys_qLxUs2s180ncOpDPHWPYizxgJvHJLqMtW7u_92hMyZcWlvOYAR1q1mG9h6dUja8SkzE0bHt9UgEx8XdHH7ZPrFPYktOcY0kOYoSfqnUiGpB4J3_LYDwWtduap8QzAGjxvg10P_QPbT4MU-JTu8NmCeB5GJIqARR0GEt0ST3OO-C-3uQPuqQ45Jo3Cbsrog5hT_libJ4AlGm8mFGbR6eIuwxleg-cigIubKYZ0TISRzb7-S9Z_az4xApXZgYpuKprJnvqqRYkWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17603" target="_blank">📅 20:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17602">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک مقام آمریکایی به رویترز می‌گوید که خروج اسرائیل از جنوب لبنان شرط توافق آمریکا و ایران نیست. اسرائیل حق پاسخ به هر حمله‌ای را حفظ می‌کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17602" target="_blank">📅 20:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17601">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرنگار از ترامپ می‌پرسد آیا تحریم‌ها علیه ایران قبل از اجرایی شدن تفاهم‌نامه برداشته می‌شود: آقای رئیس‌جمهور، آیا این توافق شامل رفع زودهنگام تحریم‌ها برای ایران می‌شود؟ این موضوع کی اجرایی خواهد شد؟  ترامپ: خیر، اینطور نیست. این واقعاً یک مسئله رفتاری است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17601" target="_blank">📅 20:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17600">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرنگار از ترامپ می‌پرسد آیا تحریم‌ها علیه ایران قبل از اجرایی شدن تفاهم‌نامه برداشته می‌شود:
آقای رئیس‌جمهور، آیا این توافق شامل رفع زودهنگام تحریم‌ها برای ایران می‌شود؟ این موضوع کی اجرایی خواهد شد؟
ترامپ:
خیر، اینطور نیست. این واقعاً یک مسئله رفتاری است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17600" target="_blank">📅 20:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17599">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17599" target="_blank">📅 18:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17598">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17598" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17597">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لاپید از رهبران اپوزیسیون اسراییل:
هیچ شکست دیپلماتیکی بد‌تری از شکست نتانیاهو در جبهه ایران وجود نداشته است</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17597" target="_blank">📅 18:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17596">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یاد فلیم اخراجی ها افتادم که امین حیایی آن پسره برادر کمند امیرسلیمانی را اسکل کرده بود!  یک تاس به او داده بود میگفت بریز اگر 1 تا 5 آمد بازنده ای و باید پول بدهی و اگر 6 آمد برنده ای. بعد امیرسلیمانی پرسید اگر برنده شدم چی؟!   امین حیایی گفت اگر برنده شدی…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17596" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17595">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، ونس: این توافق به آمریکا قدرت نظارت بر برنامه هسته‌ای ایران را اعطا می‌کند</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17595" target="_blank">📅 16:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17594">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون: بازگشایی هرمز باید بدون عوارض انجام شود</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17594" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17593">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، ونس: انتظار داریم تنگه هرمز در بلندمدت بدون عوارض باز باشد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17593" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17592">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری فارس: در لحظات آخر مذاکرات، متن تفاهم‌نامه تغییراتی داشت که مسئلهٔ اعمال حاکمیت ایران-عمان بر تنگه هرمز را به‌صورت قطعی و مصرح تاکید کرده. طبق متن "آینده اداره خدمات دریانوردی در تنگه هرمز" توسط ایران و عمان تعیین می‌شود و استفاده از اصطلاح "خدمات…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17592" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17591">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گویا لازم است یکی دو فایل اپستین دیگر منتشر بشود.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17591" target="_blank">📅 15:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17590">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDDbTzruxixGph-kMuPjUfbnSnxtNF4BJ1iuxhvsUOC-7aOpMa0imQ16qRU-b_VcQ5k0598Vpz84ruXYGRE9srJyDCpOgCJ385doAlf45iZp8NamkqlimFUdc1Zcnmzoih0AZWpe6XJN6UNS9ZKKvhz2YVOUb6FTa1IoCvlY0VfmIPoaM5_gPF--I7jd6zODfmALgx7Xo4rBAm5utCE3IvlA_gZLOEScTsZcDJJc4aALGrI229r-cAV8Vki1hMvwo6fbwQfWdZOrsA_SI6p0k_yxZJQZudtp2g7UcDk0G_48ez0_MeyebTgmvNLoCF9tT8COuYyY5dNwL5xpG7U67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17590" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17589">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تحلیل خانعلی زاده — از اعضای نزدیک به پایداری — از شرایط توافق  میگوید از 10 شرط رهبری 8 شرط رعایت نشده و 2 شرطی هم که هست به صورت مبهم آمده است.  در ضمن بند مربوط به لبنان (بند اول) هم شدیداً ابهام دارد و بعید است اساساً اجرایی بشود.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17589" target="_blank">📅 14:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17588">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">در حال حاضر تندروها هم در ایران و هم در اسرائیل با این توافق مخالف هستند.
با این تفاوت که در ایران میانه روها با این توافق همراه هستند اما در اسرائیل حتی میانه روها هم با این توافق سر ستیز دارند.
نتیجه:
دست نتانیاهو برای ادامه حملات در لبنان باز باز است و حتی می توان گفت که اساساً چاره ای به جز این نیز ندارد چرا که هم تندروها و هم میانه روها خواهان ادامه جنگ با حزب الله هستند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17588" target="_blank">📅 12:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17587">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع ایالات متحده نیست و ما کشوری مستقل و دارای حاکمیت هستیم! ما شریک این توافق نیستیم که امنیت ما را تضمین نمی‌کند و به هیچ وجه ما را ملزم نمی‌سازد.  نباید در هیچ چیزی کمتر از انحلال…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17587" target="_blank">📅 12:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تقریباً با شما موافقم، فقط اینکه از دید من آمریکا به مراتب دستاورد کمتری نسبت به اسرائیل داشت (و بهتر است بگوییم اساساً دستاوردی نداشت).</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17586" target="_blank">📅 12:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر دفاع اسرائیل:  نخست‌وزیر نتانیاهو و من سیاستی روشن را پیش می‌بریم. ارتش اسرائیل در مناطق امنیتی لبنان، سوریه و غزه باقی می‌ماند. این مناطق از ساکنان محلی پاک‌سازی می‌شوند و تمام زیرساخت‌های «تروریستی»، از جمله خانه‌ها در روستاهای تماس، نابود خواهند شد.…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17585" target="_blank">📅 12:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-poll">
<h4>📊 از دید شما پیروز جنگ:</h4>
<ul>
<li>✓ ایران</li>
<li>✓ آمریکا</li>
<li>✓ اسرائیل</li>
<li>✓ طرف پیروزی وجود نداشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17584" target="_blank">📅 12:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری فارس: در لحظات آخر مذاکرات، متن تفاهم‌نامه تغییراتی داشت که مسئلهٔ اعمال حاکمیت ایران-عمان بر تنگه هرمز را به‌صورت قطعی و مصرح تاکید کرده.
طبق متن "آینده اداره خدمات دریانوردی در تنگه هرمز" توسط ایران و عمان تعیین می‌شود و استفاده از اصطلاح "خدمات دریایی" یعنی تثبیت دریافت هزینه برای ایران توسط آمریکا خواهد بود. این اصل در جای دیگری از متن هم تکرار شده؛ به این شکل که ایران فقط برای ۶۰ روز عبور بدون هزینه کشتی‌ها را خواهد پذیرفت.  اما پس از این ۶۰ روز، جمهوری اسلامی ایران بنا دارد با ارائه خدمات ایمنی، دریانوردی، محیط‌زیست و بیمه از عواید مالی حاصل از تردد کشتی‌های تجاری در این تنگه بهره‌مند شود.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17583" target="_blank">📅 12:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه لبنانی:   امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17582" target="_blank">📅 12:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه لبنانی:
امیدواریم ایران غزه را هم به مفاد آتش‌بس خود اضافه کند!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17581" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=IEAyWsELs_k2Qnku_6LzoiNmpB8NDtTq43uPk1tv9H2hHZ41akuupU0s7h0quB-ZNmDAG7sD-oCLjpsize6ArrKp54MUWEw1t5OmEQK3miaesnNtjsS14mV-Y1iT7rsEKfk7W6YxBGnF_8EnJA4vjX-KAF9qCPKnd2VL5ol9ZNLIVCeebyPCw9eGLV-tDHiSBw949Fd5x5jem5zXlp6gNZypDy-Jim1CIE-qJ__0hC8DzT413NJi9NlsTtZjhfqF_lYM4lm38uqStZUiFB-wyLYBAVDpVZfJ1szNdhs9K6eZijItYxtchtSF0F0UrWqky94WPjYjLDilQ3WdXsuDvqCmtC7XXxAsaR0egHf1vv7vQZyGsrAkJ95dhj0UmCPcIYxX4UX8TuYO-VxUJ0gsLzXLQIgJnU7BBVoWIock1PsXisOQTlvyAX6NZddC7ERgtKtvXj525WmEgdRHpGm4VW5DTTXICfec3ZoyVmghXx1pV8xXbK5E3DcmudOltJJnhMV6RWe6Ts2Gb7WbpMH7pelYeRF4lqrwxGjzNEKuCTrSW3cBXUaPddo04tWEdSDuVLU5mzBK6ucLTTcq6R4BkUv3yok47J-ZnEHXywgBwxqVjhfZPLPKkaPv3Vt1oTH50F4izqN3irH5Gud9K_IFzH2y_XyyThuwI1KjWEZjHGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3472b7e90.mp4?token=IEAyWsELs_k2Qnku_6LzoiNmpB8NDtTq43uPk1tv9H2hHZ41akuupU0s7h0quB-ZNmDAG7sD-oCLjpsize6ArrKp54MUWEw1t5OmEQK3miaesnNtjsS14mV-Y1iT7rsEKfk7W6YxBGnF_8EnJA4vjX-KAF9qCPKnd2VL5ol9ZNLIVCeebyPCw9eGLV-tDHiSBw949Fd5x5jem5zXlp6gNZypDy-Jim1CIE-qJ__0hC8DzT413NJi9NlsTtZjhfqF_lYM4lm38uqStZUiFB-wyLYBAVDpVZfJ1szNdhs9K6eZijItYxtchtSF0F0UrWqky94WPjYjLDilQ3WdXsuDvqCmtC7XXxAsaR0egHf1vv7vQZyGsrAkJ95dhj0UmCPcIYxX4UX8TuYO-VxUJ0gsLzXLQIgJnU7BBVoWIock1PsXisOQTlvyAX6NZddC7ERgtKtvXj525WmEgdRHpGm4VW5DTTXICfec3ZoyVmghXx1pV8xXbK5E3DcmudOltJJnhMV6RWe6Ts2Gb7WbpMH7pelYeRF4lqrwxGjzNEKuCTrSW3cBXUaPddo04tWEdSDuVLU5mzBK6ucLTTcq6R4BkUv3yok47J-ZnEHXywgBwxqVjhfZPLPKkaPv3Vt1oTH50F4izqN3irH5Gud9K_IFzH2y_XyyThuwI1KjWEZjHGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:  توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟  امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17580" target="_blank">📅 12:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تحلیل استاد امیرحسین ثابتی از توافق:
توافق؛ حاصل خطای محاسباتی مسئولان یا رضایت رهبرانقلاب؟
امریکا بالاخره وقتی دید از طریق نظامی نمی‌تواند تنگه هرمز را باز کند، از طریق دیپلماسی و مذاکره به هدف خود رسید و حالا با کاهش قیمت نفت، یکی از مهمترین خواسته‌های دشمن محقق خواهد شد.
تمرکز برای برگزاری آرام جام جهانی نیز هدف دیگر امریکا از این توافق بود که به آن رسید و آنچه قطعی است، سناریوی دشمن برای ادامه ترورها و حملات غافلگیرکننده به ایران خواهد بود، ضمن آنکه رژیم صهیونیستی نه تنها جنگ در لبنان را تمام نکرده بلکه رسما گفته هیچ پایبندی به توقف جنگ ندارد.
در هر حال این توافق عجولانه و ضعیف که ناقض خطوط قرمز رهبرانقلاب است، بیش از هر چیز ریشه در همان موضوعی دارد که ایشان در آخرین پیام‌شان به ملت اعلام کردند؛ "خطای محاسباتی مسئولان". خطاهای محاسباتی عمیقی که پیش از این نیز راه جلوگیری از جنگ را مذاکره میدانست.
واقعیت این است که این توافق حاصل "برآیند توان و فهم مسئولان ارشد کشور" در شرایط فعلی بود نه ناشی از رضایت رهبرانقلاب. وقتی تاب آوری مسئولان از مردم مبعوث شده کمتر باشد، خروجی آن تکرار خطاهای محاسباتی قدیمی و دل بستن به توافق با امریکایی میشود که هدف آن نابودی ایران است.
و اما حرف آخر؛ این توافق نه گشایش اقتصادی خواهد آورد و نه امنیت کشور را تضمین می‌کند. روزهای بسیار پر فراز و نشیبی در راه است...
✍️
امیرحسین ثابتی
‌</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17579" target="_blank">📅 11:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XELRQVqpkk4GTQC2v5wdY5AvXOBsSGqpH7AadFcqeE77YFq6lMv4nnN7eewJZNGoKE8YSq0rj0qT7YmMqDBwGNTYDEZ7Bi9mwozqDgzkv-ipg9pglm9c8hBCi3X8pKQjBbj7QVaYdvrCTgIWsiplEW8-hLv2jN98V6HPqDxMA80-dt2n12lOQ_gaWl5vAO1oZH3vk9gPq-MGBWImA23fiolzMIQ26dVDwoEZSvUMaJIw3Tgwf4jSppDGZhkBYm-VwgE0JIbteA7FFr0ow_nIgBwXloVEy5Qanwl8xDjKLCIRsSFe_KqxN2UAsXwsb8_JAytJNutVtO59VVa5MhGXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفوگرافی تحلیلی توافق بر اساس داده هایی که به هوش مصنوعی دادم</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17578" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هدف حمله، علی موسی دقدوق یکی از چهره‌های کلیدی و تأثیرگذار در حزب الله و مسئول پرونده جولان بوده که کشته شده</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17577" target="_blank">📅 10:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17576" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حالا شما گرامیان گفته اید میزنیم اما به نظر من که اسرائیل را نمیزنیم.  دو مورد که مدنظر من است:  — همون همیشگی (حمله به اربیل)  و|یا  — سپردن کار به بچه های نقطه زن یمن  در صورت تحقق مورد دوم، منتظر اصابت موشک های بالستیک اصحاب یمین به در و دیوار خواهرمیانه…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17575" target="_blank">📅 10:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا  جزییات این پیش‌نویس به شرح ذیل است:  ۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان  ۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.  ۳- رفع کامل محاصره…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17574" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر امنیت اسرائیل، بن گوییر:  توافق ترامپ ما را به هیچ وجه ملزم نمی‌کند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17573" target="_blank">📅 10:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تحلیل همین است.
این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.
پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17572" target="_blank">📅 09:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17571">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">- به گزارش معاریو ، بنیامین نتانیاهو، نخست وزیر اسرائیل، به دونالد ترامپ اطلاع داده است که نیروهای اسرائیلی از لبنان خارج نخواهند شد و اسرائیل خود را ملزم به رعایت بند مربوط به لبنان در تفاهم‌نامه ایالات متحده و ایران نمی‌داند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17571" target="_blank">📅 09:54 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
