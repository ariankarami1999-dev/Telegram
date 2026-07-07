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
<img src="https://cdn1.telesco.pe/file/Lk14xDE_mG5B31rut5w2PAVhJMMtqMJaanGw-KDZJVCLfYv6oMVp7ZmgA5zLMZNbRP7qCbve8GAUpIF1ob8vSupGmBezlK4Cw3dGdxjIFJDBUPzQ_bDWd_X2ob6ou3OUNfAWcebQn04Zz-1gIzdPU4fxILrNeD6qQymSnl5irHAzUMrNz3wH1oywSg3bfd3DV-DOTtesFzqyCyBbbo1LZ19ePni1pdNmZQOJKAOF1rnGzM7IAVKvVH-MMK9UyRteTEgA1CdGDTaYOxsyN31r-6xJ1iSvcbe5HSVw5goik7sgTEo2sUFzlOi3Heimf80ZOJ1TA-BPdTVDt1ITMCyhHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rH-PJqWq_2BodoCNiI8_yXiNnJxvQteUTuaJ5HAC2kwX74V80vM4qIhRjNAJFV0Ms8CQb0g8NG9CzZfIWH-ykSjkhyM7To3oRoeIWQ8G5zyoDBZ2ukrL_GGMP5CoN4B49DdQ-oIv_CLdmbZJsYB0r6G0W1Kor-926DPGdGfyt-cfNny-F9qRTaFbCsMQ7qTG1-t4Eotbx-985oJ-sPQQWkrb1tLLI5BBqNeRMdzlI987MzRWaj6-NYiZBtHaeHI8LQxwpr9eEJZgZ-cxuZNn5TDPiK81rfpuolFsARuxjLQ3TlACXey9vVBfrxemZTGfT53s072mrPi0xuQbuKsQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vJv2b_4YQs6xUfyEGTRMv6D0Q9toxRaZ8gDNzGNOjEmWGGAM-LvrgS0zSwGBakU-8zr6TaFbeFT8HNUQOt_c8LVhbmANLi2-Uw58FIOv8RbC9Vzp5YVfsnMgdMB2Z-qvVOXA0zVNbPUQBOshonsppQktmyaCmW1BBiuqJia6DKdXFy90QHxjCPWgojvbiOdYXHgPfVHKMht-SYVM2gXL0LGYqUcHjVODHsvCEYV-rTXUz47rhOs519LSiEqjaJM8eGDP73_qURNQ4yS1yf6YtNiYVIs2yQ-cFKyQbRxwyPpP_LDh_jnYSHtZfuYQTrlMyMDNxC5q2eKuOUdDurN_WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OB9a3abgJ1XByMPCWnv8H-PcBFTdLvCpS4_XvVCi-Pz-oF37I8TrOczwigDpXlDYw7EoRFMmZ95G7ibGEKSuu3Mc3oxfEIwQJKuVDCZ6D5VPbu8aiKXxf7QnHx6ECuUaBfkkr6z6i0fpfY0qVjMxKQ5S6seGiVmERe2FM4Pwk74PFmmzbVmUTV6Nt-nTy3bn6VVumrSf_H8tHQg2dkPZkHcpn9iOU6ItBrcoxlYL4_2XcSHPivrSS1n56qRfTekNsePFwkYZCJ5JwEFRMRWy_8CHC-UIoePYOd6cyhYwlwWQueH8knuVpz9xvaFytX3K9rFsCDXQXlYZeaGi5zw3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GaM937gzOlMixdOTm-9aypNdNi9sARbhRAxbCGTUcbIh9OxYzSK2_DNz8Pdwpj6U1Jjrz26_B8aSAsEUpU4q9fnedckozhJtjW1udNc2KPUTXL8qpJIpU5ofwO2pe5KMRfCJLzZ6SH2VBzyfJVTNnuGqRoC2sjco5LIl5fBdoOs6FF9_llxLcLRBYKpbPp8aBqmmmNow1-DkMLTsN9iTkDkBI0A1FmHfNqLvbeH3DOkGIyLfsyiahW6m5gka3pzCJnZGP2qQN1k47WVxiXNIE5emokdp4tsgVp7vWwaA9XrAU-UDjv9gmHlBeGw3eytLuPnyTt4eLTEFAQZpu1U2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cLNmMuOycOp1NNs3bu_HZ6jtMSVsYeYHcuVEIWf0BepR1ZPXRPN8XiOoTJyOHuv0zb2ClNPCtWIbuqcuQ9jH9j0C8khBFVugXHvxwogR50l1Ko_TuWMywVGVfyKp1ATuRkCVobQxXhTK7BWdR5jCiF0C0y72lW33VDLpTfFPvFUFtPIV3QmTjQqdlsCnPD7ZLI4xailaGrB4XeE4dZbNRvf3E__vC6sRCl4goSu7Pb7Pk_JqW1MtUzPQrU0V8zMGIsnAIC289j0hlIDjFtdSOc0sM-D2zBxBwyaKNeambk1ez9G9PxjVBBsA3QUamS7OpjmNq7e8VMDZd2gWrDgpuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=fWf6Do5bCg2tKYrkndeUWjJ9vhoNdPvgVVIAyKARUJ4Ut6kdvVf2h4TLT31CcDcR9mt_7y5Ng-Huedvwj7WR09_Cdd1MXu_YegtWE9LrNWu7XP-bW4PW6puYae8lAbVSedzrjHYCqENfjfZBTIVFzFH3IP_KhJvJhyR1K7qU032Jufk7_wERW16k4Q1vjdvXVoK_bxZ0enVEohbr1aAFV_V63qi5HbKPD97IJyaHarpSnkNjmS3MtPXlnALyxjnPLhCCKu3kPaAVqmPm2qn2RasNhVPhaoEltAiiR1Tax6cBlDIcOc98YA8PZGuS8cPESw8NGWanXDVtdhZhdzqMTViA5s277PiN-kr1Z9fY185XdS_rtbacbxbrkeSVuy1agBp9wCqAyjCR-we-ZqqM9Nw0cQxHTGB76jxM5FCP0E4wdFu64djJvSudmpWyn6QclvxaoPLrAOTYpplIJyh63aeF6w0vJL_mOo9ZDblrE_hKE0X1nlzJ37KXJoS9geKXtG1kd-0YXf1FS-J1mIH3mIaseToyk4k0K97wvQz2yvM5eRoEqmN4lQslyXZ4NubZl3oAEnmoNXuU0Ke-qs_VF7KMsThSHwBlxu7n9nmzsLqA3T482_YXd7ghCBnN6LnxW1Yk6Ht_-qYJdM1uDMHtUN1z9xDuQ-yRLAQc22_tf7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=fWf6Do5bCg2tKYrkndeUWjJ9vhoNdPvgVVIAyKARUJ4Ut6kdvVf2h4TLT31CcDcR9mt_7y5Ng-Huedvwj7WR09_Cdd1MXu_YegtWE9LrNWu7XP-bW4PW6puYae8lAbVSedzrjHYCqENfjfZBTIVFzFH3IP_KhJvJhyR1K7qU032Jufk7_wERW16k4Q1vjdvXVoK_bxZ0enVEohbr1aAFV_V63qi5HbKPD97IJyaHarpSnkNjmS3MtPXlnALyxjnPLhCCKu3kPaAVqmPm2qn2RasNhVPhaoEltAiiR1Tax6cBlDIcOc98YA8PZGuS8cPESw8NGWanXDVtdhZhdzqMTViA5s277PiN-kr1Z9fY185XdS_rtbacbxbrkeSVuy1agBp9wCqAyjCR-we-ZqqM9Nw0cQxHTGB76jxM5FCP0E4wdFu64djJvSudmpWyn6QclvxaoPLrAOTYpplIJyh63aeF6w0vJL_mOo9ZDblrE_hKE0X1nlzJ37KXJoS9geKXtG1kd-0YXf1FS-J1mIH3mIaseToyk4k0K97wvQz2yvM5eRoEqmN4lQslyXZ4NubZl3oAEnmoNXuU0Ke-qs_VF7KMsThSHwBlxu7n9nmzsLqA3T482_YXd7ghCBnN6LnxW1Yk6Ht_-qYJdM1uDMHtUN1z9xDuQ-yRLAQc22_tf7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SQGTluMGxkYSbpqPCsFabXHK4Vgd7a7pbx_-n4YuNyMuvrYFiyZJx8BQr7WGWc5F-F5TqE8LhVHznXQf3RC7zMnXnl7jOXZRpK46wgqZBVFVPKWTB7IS_-Qmc50CoWhnz9lAhRNAC6L27tmvJexm7Xl4JlpP5x_bV_vqtojy9R0gNxd-V7wdraSLjOz_10qdAkZ2F_rd8Ud4NnLlFl_QfNkfznzfZ9gC_w23RL-pH4TaKRx0FXXtW30POSaZcYyJYSZTR5G-kI1qea9TnmdniNlvyyaAH2WivNn4FoxUqogi_UB8XKWenvlrVBwget8lMxlYGI_uvZGviHoZqx5U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAO54C-yQ278Uwc8CkgT5J9XyNKIdC9NtWPziziRdxCt83F_xgONtG7v6XTTOfuiEa5Z3bn22j60myHAw51WneNX71MKbU8ddNrk3yG_lt3xgoeL3Z88PHSPjwXUXxVqg0Yn66ArNC8t2rBqxAUPnueomo1l7RcnvSK_bHD6pLH0m7glYYov7qe2ncla-3qbXg90wK9M2F5lIkP0wobmsYympI6iDtC2qD4ze7LIrQfimN9i56LPciPN6Oyq2r1RoawmRhfIvB-_6E_fh6-zCXAebWzHXOtLC9W5Aa2qlnts0WH9qFWg7Kpe5MEBWgOu6uolxJNV7XzikTzqrZPPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NKdC-BFaw8oxOkN-2-nVyCnWve0epuTuUmXKpR_KO52VEpRfCr_BSstJF8ZmT5DbpMlehGzlUGoxkVVsJky5_z0uSZCRiJC9Df8gRz5_TxSKQdI15Unu38bBR5q5kGsPQOWJ4PkB-r_YM-gdVrVgWUo-7v9QbBBmvo5YBLn3bxRTdlNyJTTRvozB8hayZw_ZwvAajol8v-4LS2BsMy4c_CkctQontvdL9LTsU2xnpCw1vbfjU59MncB42MoMfhRdnQ8y8unCUc_WzPkTQ1l9zgzKRWG1noP2cEy08RV5J2TwjdgcVK4_EtiHHu7BgzSc9ynIoU_UGJtAzkmYcaFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GXAcxdJc6f6efVAK1r2LyiNABWRIaQpzKVF-QqWzlnUQnnyxLY41mv5puB2AMGRS0Ro1InNG1co2zbcTnCTozxugijrvRUI899Z1XIM8FqdYBynkvy315a3BWkQdHYHwek42TREuVms7bhQnK4I5EQ7U3GU_GYipClhcKmOlqqi0TywXRGerD7YcvqNJlEtJY9pa6VuK-vwp2BGXgQhYdIduMs2ggXZkxlJmtrkSxffuaobwVKPgK4qzjhp-DsMg1RnkMEAEUm5izhzo2Y1O80vu05OqPHRVeg9TKDxt_N-fcG5gGpX1RZTYYBxJeQKydWnjYj4Y__nCMXtCQvjcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4eKLe6ZArp2wIDXfxWwuWXrGgjrVKxsDHxIVW0ydy4tFjo3dln-eKC8Z6vCwJeCkzZ8J3x941b316VcqKrn6FjZWN3_QJoe37BDbxWVdcyvTQQlkJdqO9jGzM2iw30wWhvLwNQErAjZWbWmNE0K7clRm6bj2oDhozQWVZ7RLQ6Trrc8HjVajkZ_yUsADsW7pbja94m7VinPzI-tUq_HaTwFuW_cxZFWfDl_M4pfWjKyryDI88d5-ErGRBsDtgXd-X_bvnBG42ouVy3ZdUj9BsQFxV9z2CpX83Q2eXkq3DULF0wbVM8o-FzcVyg1jS4PkfoQs0LPFl6t13asZnueeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=Hvyjp_vbjge2msV-lsl7zctRpBzLE30ZsMik5BlUS5bJiJ-rUizY_7qpMlfpbKKBRbLvejWwsbYBgZARA8dz3kgXj3A7iOd3ZjzZHky7ZGlMR8jVZgLxXxKoOX5WW9N-WknHqtpL2LFGBneHuuHhC-rpg6f1Mfvp79wDhdGYEX7Z-IwgfpECVUS_l4oo9YM91l0ByCPeVcNBExA1aULLmWymfwwGhmY-DtpwrdTLrZ6fYeFJ3nhZGH20MTHvZLGNJkbId01OmLJP7LTumu4NFZX9QKiTjd9W7MDSh1MmNpZHZZ6oA6KyveMl01rNW-7WWN7ZyhF-uDJBcplx6_JTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=Hvyjp_vbjge2msV-lsl7zctRpBzLE30ZsMik5BlUS5bJiJ-rUizY_7qpMlfpbKKBRbLvejWwsbYBgZARA8dz3kgXj3A7iOd3ZjzZHky7ZGlMR8jVZgLxXxKoOX5WW9N-WknHqtpL2LFGBneHuuHhC-rpg6f1Mfvp79wDhdGYEX7Z-IwgfpECVUS_l4oo9YM91l0ByCPeVcNBExA1aULLmWymfwwGhmY-DtpwrdTLrZ6fYeFJ3nhZGH20MTHvZLGNJkbId01OmLJP7LTumu4NFZX9QKiTjd9W7MDSh1MmNpZHZZ6oA6KyveMl01rNW-7WWN7ZyhF-uDJBcplx6_JTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r0-HuRKvISl_13GjRPc0aHNP3WLbOvEA8HFIrWUiUYxbqSi-4q7uf2eof2Plx-X7lkNyWVHxLkk6hhj5_Sbln1dfPN4uWJ_2BzgXxxAqZ-R5xfvleOgdy-80Bcvr-Of9nAbSr2P955WT_UThjg9ECbjDxoiiFhC6iKyeV5XFG_z8f2qy0LtaXNz8-j6sKQiqmQNDnIfnyTfOyoD_FsC9-vQ-c_Pype5x2f7Dbw3qh_Uju8IKxFJwx2PtZq0X3eln7ayzCfWhn61whHRtnScAf5nGItUxnP3SfptRZQY9Jzsx498eCgBa8RShWgF1aT6mIzyflgtjzrGaqeAaS91aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J7VkRcrPqNduoaDD2U0fwmggVesYDXZRo1RRZY4KneJgsUyYApvz1XmhN6M52yxhmV5ZLYjsdyl8VOUwNBO-Mnr6r78ZnZkWAm7kRT2_sy0KScJHt7-w1VPEIBtneM_W5iTf0gwocfOgNd-vK9yiZJo_Iv5eq-AGkrBjDcqkvXCaRuwUQN_JbPUgmTwnBp0NRBOzTFB1ntmFhveQDW0FxZQ5ZYwayv1PGSW8gAqfBQM7V-zVA4j7T35xwuVmLslvmz0OgAfY1UoFHouaeVZtBWcijDdtaJVSvOjjyMNUyK-xOIsVshvPUpCjGuLUBEGzEcq3p_rbwjz4vmbwwkC_gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJRp8I2KNwS-lTIn10-thzs3uZESqVXQjvSbxMxVe_j9hR_7pqxColK0W_zO-hCwO_Z0sSJcr3_9UTs0QV7W4NvNQg4It4j8391DANH9PEPDYSeyoBalVJpT2eeTg641I2mRE6T4S4YRGhmF-RTb_Qx5BLbw-7z73FTCIqA-M0U0A_x0GRGF5Fq2e0cQjc3QOcNa_2ikDxPOwezS7_PJ0EAoBBoe7HZ0kzPAgjJaIjjTYkjWbwEAoPMbwRmky6vuz9Fw95gEcDU0EYuUMl_qSBj9ts9hc81_amrFYyVcTfX1LS-TnOrh3lxjAExAuHKX2SAcxeF0PohKM2pX-NjyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k5V61N_If3MTaw3RajnexI38KUWQxochuDoQXEld0wwuyje38Ts5aqyZ6ytpanJPInwwAFBIP6JenpoVV4nEhJDHjuaFf2kHdHq7DvjwsAfeKWcRUBVLdc7NzRzKVTs8neN84uGlFQpJhQUftHvBdd0LxxTufROeiGV6cpNO4kOR7cHUMh8TB5fK5HYU7sPSNT9Omt8IO38_m12-V3UDtOTeSoh9Z1QAS-cnaB8jcMn9UKK7UZNEekBZEipbK4NDLMTCn9ZttrehWGOWJl_5JS7INGKuLoaqEA0NOm8sXA97qxJ3O4vesU-JJclM6FrEdi6_oB3su5zBYF9iM0P4xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RqXv4briiPQXyoqqownbZwLhAGls8HlSiPiJJ995PXguIFQq3b4TMzC8OmZFEsbRNxC1cPakRzkIuGRoZJxkIJxpcSMujJi5vh0wnYUheNPSHtqOVPCthwkwiJKDerTVMfGkNVBlR0XwmmjOWQlkRkYJ8VxdxVniKAIFF1AvRHgY3QFoQd_pMLxOitJGFBvJWFrPDR--Po1cGr8hxkwMp0Y6UMT2J4yNg0JWx2_pbsFWgR9OqAH4B-e1xwA7ZTs77W224H-JAIRFaYSqqtBKzJyL96OF8BFn_vKRA4oiW-Vkx9Mp8PN9bIn7ALr6zjswvc06Ss6pYYWAD8uviNN1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sFf5euDQVyAv4uMJtF-6UTWtqNXl_DFRcHKlnQFCyRfMyh9N3TVmjvhkvGjO9X9ppiYClKwiAbxqAONRHym6ULNBcPbsQgVjt1q4G3vUT2agxJmBqKqixSwz86q5cfBEqGJVGt830LrCvEowN3DvJmR_L6YEItBgSsD5w4DcubpGuSqkO0AhOM8dkEjxxI9be3KiqR0zXgJBV1ko7fFqSw9J5CYuuBQN9n--haw8dittUkRMzNzFfuOjHAN7krkpnAzgLBBrE3TBD_s3TgWd9aifveaNodOQFijfWCsi_G9-GtYR7wSupW2KmPEcw63ZdWp8K_dY-GqX0yERjBUdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XgNOwrVomkwu8NfaW150w27iv2sDqFxAxE6igThpOcLw2mPuueQtxvVSyZjKLEtOLzhhIfkKXH7Mx2WwjKv_vw5JcxtNwfIib2NUKyUbGOEUmJvw9xe0dfeeZLd_C9-U-8lk4_9UF9IG2FmKo_atrRs0dukQl5LHEcLiyM1i31ZW3E66Y15esnnBoWphizqUOKGr4I9pNtyMQ88cDhpXwdnQeeRQVv54RcpJ9aB1XuF-3drk4PmgNyrX5nm1BmtxR4M8Qu8wm8SozdFK2hcHneE0qbBWvZlcnQRrAE27_ByfbLQWHcUMB7GZl4zxq9DcTYASsH0xalw1hMtUsnEIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YKJE6bgOspc7U3zsbAQiybmbYBk0DNtLSATsnb91UQZTEFDC6-3i3xZYX052KbtLp5aE8VKh_TDq01QUwI_NL1YfVi6HshYbxCxQ4k5bMRx5pb_UhRayMkL2CZbdq_ZxIFncN3KXpsm_I87cfaZx6lLVxKGBjLrVH2G7yujcrRH8tOlXqzKkKwdJ6lhZrpjueDzMlk3zg1o8zMvHE-wnIbYEcf22SWT61hOMzHJa-RdPYTgaA5tJrzbl--trmgIihsEhG8psYyBg0fDiK5FsREvmgPbiXblMeNSaH56jPK_nm7Zas6ctCU7nN8CRBklmz44VnXCrTmleOFDZO_u42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t5-PCQc_aMOYVGzY_fpL1L_zVrNLJo4f-bUW4YC8sDznGfmA__t4YtRKMWNkjUD9-CeY0PFSnqDb8iw7rEsIlpCBEq8wNCLnvVWb-IqNkM1oy5I1NTnG82I_ENS7LdTmgnpr5q5iE54z6_uF0H3EteY4Om_CgnVj0BA5yM4xzgbabouA28NwupmG8aR3sPrR3lT_CzARTFANdTk14f_qKERqcmS-SVKgvYtHBYv1EH324presgS_lV2QA_FGc2d6KwQ1pemrUXIDoc2vtqpOKVOML1vMJqKyUUaMntvKyxEbe7ecugapitnc8rkN7UZPOJm8AF_zDDnInujnYksUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IDSE8S_2LDtUIMSahMvj6KNXS3YvB21Fyoq7MmK6mAa7zbZeID70TTOIvdN2Jf43mx-bn8N1SVVYEwvaCNkVy9FQyPnwPVaIYU22nNvhV3OdoyO2SoghOy6yKH0GR2JIfYkAgz_C6xbJfWf_JmsY2T1V4vvutdRD21CuG7IFUqLRW9lgUx78XZxJojiHwoZLCZ5doHsroDbo01gTEnn97Qoy7Nt2oylZG0eC_DnTSxzO15mNzMsApQKJZ96Lf9yaNcG-EnBfvNJtpfyXdZYtNGfoG0uaymcs-WOyf1VWxH1KhBlFASnVS3BhzIZ4Bhmn1KbhJTSvkAQk1VC3IxiQ7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzlYtr0kEXTYcKrxXKjW64-CWe0n8NN-2-qijrERzqnpHpp5lFmFP3wB_FlSocl69CMm4LnTp32vqU-lybllM2yegea0T0BypxiavzQJKJbNYUuCn6u1jZ_-hTmVJxQl-cpt1-FNMQJeXwXf9REdupL3U19S4E6DhHZGJ7ghmHSzfoTcGzM5Vmmb2AoWiWWb2DYRc5KAfKxu0jmj-nlI6ALVrbFTedw44QRVdQ70__VTmNR0vcyMfxRBxzN0ky4oHT8ddQwvlOe4-3Eh1qS0KPCO1ttkBJXXfeeLiZTZur_RGclnHPrQYxgyJvhWKkgqjR2AHDjYqGH5Srql0BHKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pdu8F2qolz3cLrLG1Rz8U16AR_wtyIjWGvWQww0pNoGFWE_aOQ8Y0VGyzybjZ_Myxre3qgXzXD6d8m9Fy6yh6aFEItFN6nsrUWPp4j_IhAmMBxKYSQmQ3Z4Flx2mrfj9Y1qfgSklA0WlsgrZXg5ly2DQgn0Ab7BqXxMZa7KNaB0PBCWp6L4ZyAH2ptQZ2bp5D5S613If1s1ps-zwnj7r79SPEojeGFN4KUa6N7l7f33x-lhX5OJM9Rl0r-taNqyO_aDbTDr1lRH50bcy7R1-QTBUxY1jMW0dENKHUvR64NGRwwytiKYZG3p56XrkCIrljSCityCL4w1wJWxWsb6jBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZMyFDf3WX_AAYKMo5W3BRKrz8vJEV-ohHs9ZcV1zTgD11x9oJ4VMQisMNAst9x49gxx5RnC9P2YvhKhkbNOImtzR5WN4O_Hyrs5ueLm8uvXsQvlfA4lXu8PDLm-xn07niQ5Xs24XMP798OyukFD0WRMiOy2BZ-qxJecc6E1XvecPZD2ZB3IcWxdNjJfn9Kz3JHHCt3YOlIc9PsIRLHt8MVgqWjArZY5Qs_0-NORbihrxx4xe8ybOrimEm95FSsyI-NVcIY7X1KFbWd9qIxnQ6Dz2Z5jYeHzlbCI9XQ9MdMgy7UOWSh9F185jseWxzdIaBof_6sEukceN4aGNboJ1tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EEzFE-gQGvNGZ4uVGCN9Zm5HOpmt1oqcLi_ey8BnxwSzNnmgO4QgTWg6V8ix0yzr18eafATleDitfLlGG8jIeNFAlIRsPU7VU_hulTTXCHkglQFus2SskATGEQpRk2rVgPPLE-vigHY3CJxi4wJz63BHbeRu9lgA9TRpfJDdrjA0PqxRZ9IWD9Knrn8xJCswTKySQiiA-uTTjgkTTM17OWMRpTbzcDGZrztHFpQCS5wMC7xn8yWmy-WnPrhlM-Qsqif6C4k3SSDzrbn8G0XmRAoWVbeoH5kw40ImLG-R3cYWpUVXwyE9EwnnTJrd8BdhkGBB9ksOBuW3wvYu9gSPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=SpAjPOqY-t3IvZxXQ7kGVukmazj6Lm8kjgYgQQcMTQ1Uzg11CQNwUwS46Pa_cACMJ7torG4d7uJUsLvFW4qDFA5vt4PFs4SHHQh0FdyUatYbfI-9N8jcNfZ_EmnV4LfHQmIUZKL_9Mfh5jWqRqJAFALG2d6zHp1BS65Lsso0fTLP-KO_2zdIBm-HF09bIyv7Wp7TFBl9xXKV_i8kuBbEWD9UQ30U4uDyv3JJmDHw_bbIpCpxAwHtDAw3ShBFIodZqf6aHVlbQGx4T_DQIEAOyTCgy4MrXiY7dKOvyfKVMHyqEVAcFrwRvV-kypvkY0_mqeZq5ivMVlZR9xZ0fk9Qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=SpAjPOqY-t3IvZxXQ7kGVukmazj6Lm8kjgYgQQcMTQ1Uzg11CQNwUwS46Pa_cACMJ7torG4d7uJUsLvFW4qDFA5vt4PFs4SHHQh0FdyUatYbfI-9N8jcNfZ_EmnV4LfHQmIUZKL_9Mfh5jWqRqJAFALG2d6zHp1BS65Lsso0fTLP-KO_2zdIBm-HF09bIyv7Wp7TFBl9xXKV_i8kuBbEWD9UQ30U4uDyv3JJmDHw_bbIpCpxAwHtDAw3ShBFIodZqf6aHVlbQGx4T_DQIEAOyTCgy4MrXiY7dKOvyfKVMHyqEVAcFrwRvV-kypvkY0_mqeZq5ivMVlZR9xZ0fk9Qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W1Vj8Ce0BxBsYAithAk_oqOLZ-hX9qI65rM2iYYs_Q6jHYBk2xQeAwx_JNBHvq8tuS0YHBeXXZNVhuFReVQzzk4N2K1Jcsp2OCOIf5UZH_S5wqbIJXGXmD3MBfnrhuxrwRRZnK0wGJc3Dq7UVqp4Z0IFoD_rlGw90jNflhQvoBGHn4lOD8VbegJI3ibauPQht64C0fNa9X6Gdzii7rv2tfB8sqeWng5V6DRRG8SdG2lULppEdy0zp-yEcM8H2-5n5KC6L8iy9N5e7ZVGX1yv_tk9IKh1zuhi41OonpSrBih4HHd_SDmmBf-iYGfCefZBfNIXx4JfjdRBamgCpE0K1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVcLO6Cbyi5yWBItbNmJvrZNWshEBTR54uka6ect1VhV94_1mYiXjkz1dzTQUjIn-3PkTlFL7ZnUMtOa_BJCWc7cdVdpxRrFj8M7JfzMfxTrD3YCk0DoFpwVbDDXzzNQz3BdkeFcMr1OWG4qQ3fLUPmG-ffsmOyv9Iqak2Za4t8nwBTnFhq5PiBKOss4s6vqTTUzkDF52KKjuloYVt1vSxAWKKwHsL7hcqI8qiY9XRuyU16wpfk6Ff4eppQhU4I9s3sfm3Qq0UGM_XMn8C0GRj1KUyoyQXeL9X2T8NW7HmplRQVhdLTcWyQWGCpT6dkKYjTigQ0fspWQzybA9VtDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sa13IZK1GybCuicmsXCli2mrDwfJoSeYuFb634dkiOaEjeMDxMrMcpJyL88mMImvAPqxysAK1WSxF30UEwfEw6-HebxZZ3fdAbgasZAGdWNby18RqkMUoqKq6N2h3eKO1uf3oITKORUmKObeTMPCA5rUqXfp33eBnez1llEAJN_ihX6T4_2v56lM2uBHQQokYf8G5iv0SC2PI14opbKRDsoojZmR6x7IudE5Go76ScsbqKhv66CgrI5X--7AsmzUpL-7MSq4CGXnzKOBWteIjKdPmIHhEBMDXQduloOxxsEcPCHn3cp2ATNboyZkfpgRGXvajkEf2DI9_9nZW9XNJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ne6TVcpDHHL51L_mewbFZw19GZ46VXSpN1dBVOir-Z11U5nudrUAwZusddBYHVkQbwg039L9tsk_5kn_t3JqU1UMNGn2sziyzmWSNQ6ua3Oa62KQGY7aN6WbrtMYKlatLA-DtRLMpV3A5Haq9h66z5g_50ihM4JytybGMI4NvNtd8znu7PZxgsCH142HvWeABObUGQ0dOPz_XKxWv1O92wbnMdJYF0rI12HfuK2-CEaAc5PhSN85DYYEWGaKaoFw_sS-9ds2HMTPKNkg-lkpdlPBAXneVwkPibS0QWRnIhOv_7Q0ie17Daj9K-2c30KRU6SclTbnJaNS4HWDhwpuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bAwkjryqw5EnUSm8OwG4z32bLjEsyQVFiJAyqA_g_xisiHiX98cmXntJWjZAoKLCOW-eXpIhXaQt6468zwpHS7kSVSdSu2aQ0seRCM5UCYpRF331bBu4VHLNO-pjurhIAPP6cA2Xqt8fNU2V6nvm99vZDk9AtAafHaAer9EvEmGWEjgu16insG3pI3Ylblvs--Qd-MrFmJYUf2_9HTvMEYqSaOuh-LDLaOJ15bhFqtZcHX-LCiI4Kqc6CrdGpElnbT87Xo30MD8kiJBl9vwkCOZIAlctd_XkkUcLTLHxKbWfXzMpMPISnp2Oqd-58OxzvB1Ddl61Emc5tSBErlaDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RdzS1TUgio1sRV43uhQP6kXGitJBxLVEE-djzjccsUIsq0AbRjnNhRJ4lB62Ts4qlIV-0zpbQQQYI2MRjnCKh0rokz5s8CBNmsi1OFLZdkUNMsQcwm2Ynl330NwfNjVWTOwaHpnFGb4ommUdsuaM9s4xuM6lG72SQ2kSxBCDtyf2zGu8CnitBgBTacNbsqglm6ozkcXl94uwXOgPka7fTuVl5DnnPO9Cvs5tJSknMBg6BDPBZ6p1PIigB308KKCWzl0QWC8Ndeh47vvxaLK8g1ukkkt9il3jp3i9gnCAO9f_WDUUG7iEvUJ3BCtHX2XCj-Ao4pjt1p0fvEfibD8PWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pGfXVc8TyGnDMNMoI-5TjjQuTSnGxynuKtCeuWVfhXTQ3wOA2x5D3YysmTUydJaQbiuLCUqmB6IGnNruV_SwaD-iDBiAH10ujwlAXArzLm7IPrdh0pAOhIbxL0SFDvF_kAw5gNYZfuQ5NXEbrizLs6ROP-js4zUGtwBk_p1jKo1-6Q4ob8O2y8_hyaha-WjF1AFZKoGLuAlAQagLTSOFcTKCgMAgLGKfOo5qoUubRqbnMkNZT8Dcc1Ral_mBXnXvaZOMoiSgaFDpuS0CmEZQbzhn929XsUMGGJCWgs0Grvl3uUvbj-UwbMqDSJZBpPjFwT6KZsl-9BYhKI-3TnhQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CoQzBTxwyKW84bm1A9Z3LcGEs5nb2agQt6IVWteVX3aj6eEYzo2N1y2TlzQb5AEKYmrIciFNrj6UCHTWFpabu8opylGZO36E0QEFNzyPcWqqznL1VWMDuwgGminh8nEGJgPjUwvXVZb-S8vR0ZM7O6fbtN8pbcT7lmknT7kFiqxLKoa1WuITQK6xdzsdbHjoUfsTC2UjtQCV6UiXctI3iVGZFNAgDeHfLytTidnyroS9tx8Vgfl4MLT9o5K6LIBR-6Hnnf--D-s-9JqD3VoUdC5HnWxLyHLln-bV6PJvWZHdLJ11WL8CA6Jy_KhW7VUCNVzcOBEE0ubhOQlUUnZE-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/djJ06NjEER0iZqi3v3vNRsANDMzOWWeZ46hwIWqWrM3Bukb5RGf9SAaGxYPdbQrgj6V_bULhkX1RN4gCnh4tzeRSza5hkf0OdR2R2pEhEBOQFaOwY796qjWdL2ny0i6EF3-FHl33GctvD17TJ-QuHeyKfG9jhZZIY_5BNPNDlpsJa1PWtpG_n4ayaV2Ug0BPYR1ad_aN6RppwVMOITIqm7tIYFPtCNlnCKaHUtvaROIR7T0SUzo0s-qw-nbUW0Y54IpnxTE0XnNE_2sGtXjlB2cFrGRjJJCC87gJPFICh0jugz4LRtOYaXKbBeoGJ1-S8ShKWl_EU4iVqEj1UNr1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FL-qxuXwzVvdSyMVgtg-1Qd-CdSROW4G5FcI_7CYPWkwf9QrWiB1iHV2_H7zqFS1A8uwf9JHfHdkiqcKxLtOXeriK8t7ggRyRcthBTe3JJ_dzNFhVlHoyzW0Qfpw_SNHLd8eUIUw9fvuFngysJ7N9Ao4XF5n7ngREXd_DEqxIjdIKGG3H2mXctlZATwlS-PZq-efVCxwU9HQzeFB2ojL9jKzhOrMLmg01QzHo6bW34SgTcCYHSkPNxATAW-xsQllfM3Xmy7GzeBGIqX2bS-4bAZojSOP6fcR0wV08DpUf0oxX9jX8iuIpm18MfWa4aFO16CXDQWA5PC-RKXARjBBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGweuoAMgLFGkkpWZ-Yfpn2WK6jSDJdzwEqAAfnBy4toI327IlNRMx3ukZhKTwulH9IlRom1BRpbTBYrYzbmhEWWOpYxNsVc5Lw5vHCgZ2Ugysk09q8UTmay7M955sshc3LWAhFuM-F3TleR0I-drdLVkwRm4xn7ygGnalJZp7oyqblqRSNc0xkhvl7ZIz4zQUpIx7j2ota-X5JKHsa5VHt-IE6SJmJ33PJzLDga772rTmVzTNxFsW7CJYedbht7bzCl0omgIWQiLIJMAD-BRxjPqUIvkPNbaGn4FFLvryLTUYbYZkBlRT_NgPGG3luxCS_CQrsRC5u5MqD9Qq4JvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YMFYtZl-tXiu7EtcEnCtgnaDnfIP_6R0fmM8byCMynYsQyedMPvTTO-vN087YGdPUR7EBlsipCXMa2nNggGwrdTZ2sARbbZA039ik1dkNfbz7RhNFYjyFBvZrJsOSFJIqfTTfg_g3_3umUkSzh8doYBChPBgtfBY1PqGXlZmqYnV6rMB4DoPFRXWtTkxWoeRrZp9aTImYIM1hxBMGQPCZtbBPRh_kO1RvwJKWdqPZfgCUfdbBM0uE-okxwkfj-ix8z_44rv9lQ2Xq9hfZnWu-t7Z08VNKOzQ4mwRZCjEGeirT-kVUc94W4hWkPyFjV5MN31zpZSc3oLYeF1Id5NnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E3m9KDEBlswFWGCb-OB4VRRTqms2T2QdFBshM0OGxgiqs4nVfKUApkWnSQkZVskKHDDxHId5me__y_3j85MaHZI0pir8OTxyxIIR37eYu9cmN07LMXUvSdfvXGNtBkCj9yq_QJ915CB0k2BNRpEwuQ5VPfYzbplElijFGhU-p9lG6_3ovFpRISfSwS5lb8k3n4_yxQk56ncotCG0cgufecLrsOHQwn6JPG2nRBzyqoKORsjqH4B7qwCks1BnJ2FHeNkjj6IAkV8BL5JlfMcITc-zzRAyrAGrtLth3mlKG7LUXyTWetgZnC58gfrdEJk4HANKlgOlLxJrNI6Wjdz5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PmF7yXdbXVrFKjFEEd5ixMjANpHIrxA1hfhexYHofcQ-XnAYpgdTAQ14OWQtyoYNqQvjIEpXQazUHCZzTDwPQUKLKbU2O49MX2nq3PgVSmCxpmEycrdKaXG3b4C97vTv-pkrvkKhT5CJCAOvuFQkFnSNnuPZXIBR1GYpt_jgDkU4r0HAYj5EtjHxfZpHzOFq1aGDqJDdMxH9IxvR5WUnn5kli5hZnPTP3w8EJEkO5ye0hSa17kdE-NROtMl3PFAjxbROCdY4AXr74DqHjNjoQB0BrVLu31gaF2k-7G5NXP9J9zfn-uFwFyJ2A-dcQw0AXN2lKUbcckuxxL6qBtdceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XyKBcaWxvClWVn_-aCPE3ARyDUNNfGc4rxQd3b_Johjai2-ZbjKoCVvH2cklkFKy68r1MVqr1pveB5cH-OqgOPWBULRaPZ2OsftISYouzVjai0DlETQzvTJtT5jmBWsnaSjGG_G3p33Lwx_fn3dKbNajRymGhc-QOg42GVtFvHEBF063l1rhhLTqCivOiKGScu-s71lYqc86fWpYvnSETVTuoKj99PNx3aqNhMIK-f6yupquVPtMH3xojWvJaoxkSZGglQU_yWmFiqoUvpdIX7nQ3eSELM2-Bb4SKrcXymBLx8iGAyjN-ATpu2bbD3k-VPwJ7yurUYl63gHh1XuvwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی Hermes اگر از دستور Compress استفاده کنید، به صورت دستی زمینه گفتگو رو فشرده می‌کنه و چیزهای به درد نخور رو حذف می‌کنه. هرچند خودش وقتی توی هر Session به 50 درصد ظرفیت برسه این کار رو انجام میده، ولی تأثیرش روی توکن مصرفی خیلی زیاده! همونطور که توی عکس دوم می‌بینید
💪
/compress
—> فشرده‌سازی معمولی کل تاریخچه.
/compress here
[N] —> فقط تا قبل از N پیام اخیر رو فشرده می‌کنه (N پیش‌فرض ۲). پیام‌های اخیر کاملاً دست‌نخورده می‌مونن (وقتی می‌خواید مرز فشرده‌سازی رو خودتون کنترل کنید).
/compress [موضوع خاص]
—> مثلاً /compress database schema — خلاصه‌کننده اولویت رو می‌ده به موضوع خاص (مثل schema دیتابیس) و بقیه چیزها رو یه خورده شدیدتر خلاصه می‌کنه. و محوریت حافظه‌ی Session حول همون موضوعی که گفتید می‌چرخه.
حالا شاید سؤال پیش بیاد، که متین آیا این قضیه، کاری به اون حافظه‌ی بلند مدت و حلقه‌ی یادگیری خود هرمس نداره؟
✉️
باید بگم که اتفاقا چرا. هرمس قبل از فشرده‌سازی، memory flush انجام می‌ده تا اطلاعات مهم از دست نره و توی حافظه‌ی بلند مدتش ذخیره می‌کنه. و این شکلیه که چیزی از قلم نمیفته!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=d0e9ZrDgmaF8JpiL0RRb-QjrL_VTMOSOsZSZn4munsV0taRNhNaC4h3rwjvGM-6n6IXFdP5w7D1kIYYAu69rkPdp9BzgP7Gdi3K6mstbhnHtjnRVzok8fx6qdjlh6TqKT-Yt0mdSeG0B2GzRfsd1vxJv_7iSLCc5-Uq9VFrcgs6l_f49U53o_ynEPi3XtEzC8uB9sA9JG3vofI2KxlLhEXxZPgqFZoOrNcP_yfRStzWE5buLnSPibRS0V05_XwcYTH7tv8_7E5DqJXtm0I1V1YFbCfRwdgRoyU4-x9OL5akeTUj0w1aHXerL6A3ghqsVKP2MVFwi_l3xLyepHCwApjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=d0e9ZrDgmaF8JpiL0RRb-QjrL_VTMOSOsZSZn4munsV0taRNhNaC4h3rwjvGM-6n6IXFdP5w7D1kIYYAu69rkPdp9BzgP7Gdi3K6mstbhnHtjnRVzok8fx6qdjlh6TqKT-Yt0mdSeG0B2GzRfsd1vxJv_7iSLCc5-Uq9VFrcgs6l_f49U53o_ynEPi3XtEzC8uB9sA9JG3vofI2KxlLhEXxZPgqFZoOrNcP_yfRStzWE5buLnSPibRS0V05_XwcYTH7tv8_7E5DqJXtm0I1V1YFbCfRwdgRoyU4-x9OL5akeTUj0w1aHXerL6A3ghqsVKP2MVFwi_l3xLyepHCwApjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pJhLIz8V9w15EX2szH88BxY__CztZxserAHr5FKg-6PcRuZAgEwKU5dbYOgXJnMLBSFd_cHARcKW7CuZlfK7fPUp46yB4J7Fj2LxgSd-dJeNFMaUex029Itel5PI6mg0E93H6SarA_IRONNuwhjSCXNP8PcE63dnZx9fzMtTv42MggAdnPNqTAdZ_EEd8Oa_xPTvpnbZJY3-AJkBuM71o0Hq9QcdDwl00vJenUPFDJNqYYLZquMuR0lwYVnP8t6ON9mOPlQ336r-OwAi_iWxo7mZfKrMalkifYEdv5z0o5E0TSDpv-xS7bHcaTFATeP4RqxSXPQhxf5j1h2uQJeqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R3UXgNjPiWrQEjIaHrqDC1T5zMOv0ACh2QjcHAJEXhrxunAoxnSE-BUyG8ahL3UKjjCVdkmQtlh4N3F2G1uXL8EbNpvboxYFiHzQwjH_uGGmpStdbA4kEsGE3FS68R_IIPvWkO_kGtXYO275pNm3lIy-VKclYMXdPanPT20iMnyQh8NTogV1B37puIHLn-lSgCBy4H3ZCsssD3vbj63rD9agWabOVoSkdX06Dh0vyWv1zD_JDUHQHoE-0Oabx79It7A7xHifGPwcEAajjfFtZU3cGHkIhQyXS8m8KFRclc9xT9wvghbL-jId3FyyIcGMl4uMtX_Xeut8h4lyMx3Vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qV6iskBbXWObi0WUNBZc18P3KlSZNl75HPnDXNK0x7UN0TSj32PGBQpmHd0M23sX-Ep2wXIIqzHZ0clxm-l0da8P7hggG86NpwTmufY9RtVPKUuTg9uU5mKpFifq1vXo0eDy-0VXed48Y1R9x5_TQ5jZ9Otqbz2-j3PYhPKz7O7Fnnfn-Zs1m_91FufFFdalNPob-tG9Y4OEbQkU_2Q1kCdWAOv1bzllvXI7KS0XjjEOstlgd59pz8f4UfL2WkuHDDogdqLAnKlXVNiy_d8qmsprxT4etEn5qLn5cmG7OMyUaUpPct1PDmb0Hxya26cqKnju90Sl03kMgVbcBt701A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CZkzwTJMA2-z739fFe7iwA-SwAxIlF3CViQ8h7NiKxmM8uLDCm7b-DeH0uPUISnLaFUC77B57sBfDdOjI4rzNpN3GLbsDD2lT-N7cAm0gOACamGAZyyXWAhcxJdccpzqXEhm2ZTFkwLE5CfRLwkxyGmBvGCpWEJJHwdmCjA98XmVtf7uP0e9Kn_GUVmasYCYwNkjskz6mUYjJi_iN5HFXwZuktHBHKbC7cDyTTyUbDRhgbLso03tMxzSGWtEipNOSW67ieKAp2QKRVVZsqKnaQSDzMxfgJbI09ZurESPbwloSHxMBiWQJCaAuLBaxne9RmSHqM_V7t6bGfLmnrkZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O6SSwgQkISXPBdk3iWeuasVWIjQmrRZaNGj36Iyg3zTFlK8EodL13fnATX_ZhOMy749xztZTEdEhjIm8AKJooph4cDDKpNJbtxHgO5HMpT1pGvgdVFxS9nK8gORJr9eTX5QX1L3l559qenmZPAMyEwHCsQiG203XSVM-G588co5SOelMZG_uChj_jgl7qF2WFLyhqqOGjlxXuYY_XKzICzFvaZH_GHQdaiYb9uI2R6Mdo7r6nRIU3F0_LYNfc_sm6lK9CM3dHmLKvqjmQu_jpT5nXstQje8TE_6Qe0zxYy_JAkg_f6ur8PKlTXqRY77H5AdG29WSeyKbZEb-EmdD8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jspp2PFp-jcZCL-GlHc9nLUwt9DLQ54naB5IRFUzITB6AgpZfWX1PKuUiXsKqdFln8mCVKBgq5q0e__6HSBZsoQQTl1ARYWe4szhSmg2r6Obs6ZlcCTZpGcHJ2wmUpgF-MZaFQXhwrh5zFa_n3erqO5FVYOR42Fq3UMJMhF1VLJti6lOD4_cPObcq09g8JthRgrNGr5zR2zqFpDqmGBHIBA6vKzUSckiwjHaXmXwCNvL5UxVCHuoiwsYayWpbZ3Jji6E5lYKJjbLfg1VO_6Aaj70iFMgHOMVty3JLizd8bbsXHqPKDwm3t6B1PeiKC7VAiT5KqFO3iRzMRyYtWmhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PbaD90eurM8pG7uw2f2fvd_f8rf8_3rqB-YcXKdsuJnLT2BG3NHJEw13gF16u4fxdPZU8ScQzYRKCWk9OvQjJe7NZmNapzW2RgtnBoAMPF0fbsEyV0nvWmjb__jdj4wUvzxIxoqkoo3-iBigeq9xAADOTVH8aHW8RVNF22xEwGxAvL8IDn4jkk3j_P3GHjuEG7VG6OH0EDGghu_cFbGxFJdxU0807tew7VBtzg8uXeNhg9AvbKbV573lmugBMroO64-qy-1Y-o_c28-gph5mQK9CPXdGJJGxG_T6rwtlNkfyCHpAl28mThZUIYvIPnqJ8JSK25uPD50voUok8uwJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVHlC0M9_WKkG1RBtWM-M2XaxR4LkVr2Jx4g9A_CPX0NuCCItGFF7GHpGnNmRGGF-Rj0W02jM5V10DfutxWa9EwTzhpYGnBuA26M5wYpLhR8MIFplOii9KXsB45QmMnlRvkUsTq8xhQPCEvadiZjU24BPdNNDfkXrnb8w2txHwBDTm8oxCOH2h7xs3to3vcfx-ABjk6HGoQ6Rfhlw6RCGKSvVnm7s2GMPhe8Tmca80ZPj3Oowi9Kvp_gczBuqGFGdWcw2l7d1b1HAMETSGmxtjj0Y1rofHX51jmrgM9lluKyHSfXvdqOzLKfU1lmAFhcgVAV8SpwRab0HTU38cJlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtDzlsnVlVvheRL8ymsBiipI8I7jWhrcZklVFBjCLl_SMwSIKO-1tbk0VYoJI10jaAPXE0EWR0fWqYkzFT9l-M07lWQbRlTWIvRQbVXnLjIMzbVla3tkejNmFJDYfya7HvAGDejD5H9J54YmNVJlpsNRZeVrMYz_96QtK7Q22C2dgh1vTFyPiB9ydJ8Q2vxpXHOxEu2HIbpeqXlaii5Nw-uiRMNGAHmLA5frCvhpcuwWs_pHdyxBQwQHT7dXEpfUmO8055sTgrQkUpBB51K1lu0uCZHIraECKukcTls1tI8vXJKAWj-gPt1VPRI_xYYLAx8wQHExt7R5d6JHDGUEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evnH91BfCiQOMHsWaC_lfcqTFHvtJSJv-VDuRs9yNQ3yFrrMXfdB6MMtoyWz14s7CHpajgTCqS-JdM-a6D2U6UpvTmxHv3MSE_zZQXzBnWubQlQU_ZaCibni7qs84Ou2iDBShIX2hYEkx6xjN8yjOWAqZe3km7hYb6qXPRTmtvRdJvn1JsZnSfxoM7dcrdq97Qtz6h02mjTpTwAPlqKDAEdkZ-M1uq-mLf2V4MSE9dlM7oTlbqQl-UiZqyeicRxlHR0ObzQG6ZKmUDPjCtmQ6Mzt6nJnlCTamrvfNTIwEgNCbrDui7tUsR2mlptopyR9Z8REJy825u9aVxERFH70Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sk-JgCiruZhHUvOVRmmbc-ExHGvYPLExgGVMiDJz_dUxwSiJcqEUBWb9SOfwqWxKKgDKJ8HfIqps8nbhN0jjfKV8rqGqNZJ1gTV6Lj7IpitkQhvHG4QuExzT42Dz4J7IjYj02tsnTKNItDgV8JRWxmheim80_ksXlBAy0aDT7RXka-3KukgA3vN0elsNuUirRsXd4yRfpSNf-aKAg8nRdnhj_maF1KXKkmH4YCK_sl4KTxM5cJHKgf2SxPgAal9UUkhfIcasvT8hbDZLeo9b1mE6VuQE6pdxA3L26wqDA4dZMbByHgbGkpAYN_taLtArq5sw6nRfMv_0OJMvvAaSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ikdoxihqWCQILarCafVNc1s7XZ9Tzcs3BocTl8DarbjF4BVfQm_AmruG97LEBPdEq8CPraQblRKd3EWBWwUJHMv4oRGF8uXK54kn2oHdJ4ekrCsmeHkQISjfNUDH0mQcjuIDTipBMSBQzZ_-46-5AScuE-dif_ujH7Y0OtfEr_0jo9EELZK7yjxNQADYjQOiYHEimcTGcWVGNupP87HZCYZ40i33bGxQ3-0xP-6ZQ6FRNf1spIk8eX7Yxdwh84cXr4kV-_Yn_Cra9N05lODMSF7zBJHMxYV53Cf9uydLMGo1siE_FxEkBmEVxj_NgBuaR7hfxhCryRsL7fF6YeVo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TLo5bYLjwOeCjmaAgGBwkSly7v-oTfuxTif38QsMdFI6nxsevPaEtmzCqkuCRRGTJnSetjBk__TR9haURU9g5tptN6ipegYDLV183f9dHMVNYu-kAUc9Ec2cpkNif0SyikIi4yDa7WxqTDpKOJmkQ-w_cmdHRS2MaA8uAyzIh2eBSVK0UzU6wbTPygW4R5Au-0Ov9kGRZOF-nKWU_Y-ewPNP6V8Kona0cymHo9wyF9EBAOuf3XSHbHAILxoWViakSU3yNNWBqGcAu_pCQ-YLbacBWXyVrTNKf-4w5dypV5ea2FMNv0BVZGFdtiPATCVjmIXnt6lR_riTOI8C6UJofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vxNUoiw_ZmrJl3SSCrM1EeSqSa8b5_lRxh4nNsQPMnWmMh9LCigNQUc4x3PVYHcr2sjdbgJezD20b3gBZZqZ2pAdV_PgISPfrAVYf2wnEs61glmMS_nRD9NT9IThM0P-ydZw9LhjYuJevQ-Kk_F9YWziPDbi72MkVAT2vVAQjPbuMAv788Hr-4xfccGV_Cs90wf3IQjN6djeEap7IZFDZXPIHxY--ShtPig-PTLORmotxTGZy0U0OytY4hTiI4tNM2xKbekMhcTS-kax2O40HlopfLcbdG6323_SrxUGenzi0E1fA5umQ2ryMw9BrHL3zdQTNhOpIMo9tNudKLoKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PwNbeMC7EUdnsJ7z0mpdPAoGHGwFc0Kkp9nXQxFBkbSxiOZHmUYlU4phu2MB4nz73yoTP05AqCSie4MX_vRpCrZljcPwTXOLaZFeSPnG0zyMMVIdZol0-TDrXEGpxhRmSiL-8Am3_Rt_sMbrYg5_FFobxB7TZbqAQIh2a8miV2uT4P82wSrt3GbaldF_0bvvPGmy3gYV2zDGGeQyLVXG1lfmCgG4a0oDVnV21W5ZqnqlzL9ITIyqd8nXQHXAjh4SyMom12OGKfZPsQmspOoTSF2r2voiIZNJ5rOkxuJric_uxJbmmvkm3C5lFKhLSbapLvR_cWKpAiH1nAKFhnS5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsPhFvW5NSNP4dbXdStV7WmkOAWR9M5COMv8u2a-25_0IElFaK0aokD3DfQjk7c4rcaoIXjQ052m004-737pXzqmCbpsm6sa8l7UR9sPCeXDXOqhb7Jo26LJhkN5UQX9BXWGRvgteLPx_7vVs8qfzzfK9_djX3Rc6_lqCIUIgIDUO6j0eD4P6HdQNrDRay1_HTaR3nM6VkjJMtDhC1u80pcmnuq6RTLkMVuj0N-4YkopXCB_KhtcvbH7G6IurUvsyCOB0Z83iFdDyrYZ4N67Eqx9W3N3J_XTI0fQtawjHLm86IGqr5IVXA7QVREC5gAGFZ-tIGv6zeKengfhR1YJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KOPUPmTnRNgcGiHfT-9Qyfg641ArAf849NvQHZs0Bwpg30RlpT6Q0O7bAECCbS6LE884rVRBHaCWY3RowJmKg7_9o_WoPbIZBg2jK7sRe6zoOGCSV6oESNVstlSoB2Tn_gXEcLxP2EGS-lfSLpIEUSLHi9i5ScEUBWcO0yWyJRvMy00GTJV6OrvnlpkABg-OoqUX_oYOTIBuc5reEOstiGHFrH3nnp9L_HEITNzeGgDkaUWQHYT4ydbM11cp0_MaR6QgM8dnFUQuO7M5KXFI2rItCm-36n_DS-8yJI-TkL-7aaBC7DMu5A9Od0auO3CeDNHMuG4kdIbg6yvq-FnEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWbxIkkZEgCbZ2-T3tmDLt-XRxfX31CgLZ3MAPMrLLDTdXCw7_dhyUCfln3oi-wZpqrioQ3RMF-3-0_GX9WugwDl7gsfdC6KEe978WpR2vF3NqZrVHrz806QrY58iPhY33I90Cp_GoF3A8guLUGWCiAo9DujRcnSnPncX7k1rInjyKUxaLOxUmMnAZoDwGqDzjKEPZoMmI9v-2iCCvWTUTNfaPktLk5Cxdd6e7-ZLzHqPCHbAC-aVPanNVWvF37vddxW4qHmJzhnbYBCYuVeYjLIHmh0B1iIqmpV4YSZ6iEw6gdurKEsEY8BD7ixjDuLrz7H2Lro870S9iR4b1MCcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QwGI0ASHTN_AimM08kEk_W-pi-1tjgcfu93fTwsqS3lmbpv1A5e-yongAOTDE7tulYxIFXlKtfVrvsK5vj7K6ZGIKBfDV-j2jwOQFN7AJlrlANWB3vI-gemd0YStj6_Q5xZOa9E83rTfUxjoJ8bjbvzG7IgRqs6e3q1HIYZdbEbtdVBqC_OuQtG03z3ZbR2pwGcPPAYGWsvRZqHleVUjVfE-pLLyxAPkmxnMm4KJfHtUTCz0f_5GwkGuWRD5DHdQ4oSKZsW5Ae-H26EEAupxNaFuRyzHXd9UwSyTWs8VA3FdsDzmNeNHqQ_-7PnCbijdYn7-9Uk8iV6NVYMp9Rd3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
