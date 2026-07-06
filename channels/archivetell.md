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
<img src="https://cdn4.telesco.pe/file/HDRSG72O12I6xHl1Mef7-fKApp_n9K77kvVRiOYkY35Cgf3yDIJnMwZzVnJ9IoRQZkvSEAq18a-hLigWSE35kYWoRZOl4Y1xW7RtxNgG1oM4fdwwkKSoyV4mzMM3KWmGLKMCWbLZR3fczn7btYy1X4CJJCJtRi_-UryLV2bOkHMJGn8iDxA7KoiAkYvjuAQkYTSHLQfkaWT3XDnrvUFiBRxuORDaVTCEz1N3-TCj_TutYWl_TXo_RidNjhib9JBLBtlk2ndgX7_z8BGVBir430femxrEj0JG9wQAJD3TkVWlFpmypKU7cXgCABd4jvPvcxL1OB3H7Pe4csxpJO8loA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.7K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llw7vVvym9Lyp2ud9iJX-C0jwdJly9bT0mYmYx76Vf5kvR2kEw4ZCw5hP5WgjJV2NPhR7nTMBntamhh26fj_YrC3JBn6ALojiaejITCJ6amdVG8SmO0x3zosv4Dv1rNIhqhNjsGPP4nT0rX9zjU2BnsonxSoiaiprhdCb7-M6n9k3cTScxS4FUEhaEDvC4RmcX3Mz8Spiialb_7dzKFEZuAiuX2B7a-XY_m6H0ga6al15c_p6Hymi4Aan3EHrOreZ_LLJQmyG_e7C_VlgmYaO1zzqA1BvDfMJUH3IsjM4uuodWm7vt5arN1eco4Zyfc8VkZ3Pgnjb202hxtUgPoJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 374 · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=bUl4xJ056hU95L7E2X50k85NbqtV-GZRjQBNAzAQ63XIO0B6aftPIr6CswUwr3APaP3uDA0_1cFsG1lscFZ7jFUiTVyqgfesz43w3dWCnJywPL6GdOI2EpXyn-UNS3C0gXEHN93mj4p6Ly7PuGVkDpVRq9h5oYR1SCmO3zrbKB0tfXBqJ4qN2dpi5YSBIyl1SfuRydgdRSahNcUefoh6KZTNudMICXZbEHL7anUTgpou-sYQdN3IgC3FSwQsQxHH2AuTDnEonk8s6pEUhBBwjp5KC8FK18VaFw9tctOowGGi1sB5nmWLyNI2jpH8etYSZGxESh--8WLWtC20WKcB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=bUl4xJ056hU95L7E2X50k85NbqtV-GZRjQBNAzAQ63XIO0B6aftPIr6CswUwr3APaP3uDA0_1cFsG1lscFZ7jFUiTVyqgfesz43w3dWCnJywPL6GdOI2EpXyn-UNS3C0gXEHN93mj4p6Ly7PuGVkDpVRq9h5oYR1SCmO3zrbKB0tfXBqJ4qN2dpi5YSBIyl1SfuRydgdRSahNcUefoh6KZTNudMICXZbEHL7anUTgpou-sYQdN3IgC3FSwQsQxHH2AuTDnEonk8s6pEUhBBwjp5KC8FK18VaFw9tctOowGGi1sB5nmWLyNI2jpH8etYSZGxESh--8WLWtC20WKcB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZFY8iI8x-3QmEDR60_o5jm4aMDaW4Hoy6dn95cr8HuTvjxuv1HQqUR1bwuoa93LGeONmfT1bc1vnJXUBqB2ZDQdEapwaeFK35v5W1jWr4xayUoDA519ziqBPptJIB3nZs7pnhuXx_RFR4Bh4IH5AIHm2j19WznGDSdqZ11RP9BP4HPB7nakNiS1dR99oox8TlGi6_2p4vSAlm1G0JKBw-SdFfdCa_kSV70lmAUizfxRZ0jMgBjsaM9Gdtnd2MTdW1NZUt0bWu-3u-UCuvraj2K09V_z2XRyu76By5ekGKsMNyFRT3K6ZWRI-EUxL0aefayWif31ADTNcRaqvo2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai1mvJ22NmSiphUDu1r4YbKx_X8sD-VtHUq83vWw9xC1zS1bFLxwET-me4I1bJoqANyLtgjzPLe4Wo7DFuCUu9QDqvIjhibVYTP9qoDEIPZY5_Sa1CSo0ztLg_nA3qF6EDpqt5S5AQh1ej1Z608cPY3z3iml-eR9JULkBsRlXtZnw_oEP67aaDte0yhuH77midtRvSIS_ok72v4YSuzr-v5qoXKoW9b5_dsjJR5gPa8LRD-6Fom7Lt9KPtkb_fLgiHQzaKJfb1DOyPnERKIH0ql49P16QpIxBmKwy3UaGv-jTVwtxCHFlsA39KYNKbEGYmJoRquYe98CYqatYvVWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQK6OZ6XcbHaTITAEubDkzCD0SML87REEfVlaIFLYLGOOsBOIVPXePd_Zyjx7-w8VYDJTKPkcL7C4rE5utycKN3M4FVgp7GoGm07T4Fl7K3sHfu-8tGT_1Kj40G7e5EirUHfueEjsaJfQGHV7hWIQppbC_bSBbEnczwNXnbz4l5VRN0WzfXQfG3oWTnqFjL1DYW4s1etI84og1fo4vS3xw_W2AerP-QnMh6yXmk9fWGxO7mwYeDwRaIaUEWA0GUqbLNmyLCsudnzxFPKXGB6g2qVwT83YuvdORFGdcB_h3MfopFbKsbnAKL3ux6KlU79Gnm1sKHXZWFNP2Epjp7jtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPmuysZmxH0dzIdUjS3NaTcRGOkIjqhNuCVas_hYgXpsmZhRBFkMgMnqfN17UWmGGmIgMslzRp5AdZpmUMqBStg3Hwyop1Ua3kQ26PQQJN_FQG-KUE7boy9mPCsqE57-JXwh4X9WOpVcoeLMPEpSWhxLrdLPxFv_Ya5dbLBwcQJ_1zrL5OOSvnFJlVtVX4ii5lYxeh6NmT5p62rBxCf_PT1yRdqY1-9zB0e2J1X7HnYYzRziyBjKMckZ_Pp1DrforDFrBH80wIPjPCeF-9QJ8JDZG5zYxHyKbVUC9JjS8xsJjIK37jR_nSMQUsHtSOzcWdi9t75RKGqVbVNlUXoEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFmtmYuY79XrcxpoANbuT6tc0EKVTh8cY6HWmo8VMdAwS39e9iCPynCSG5tzAag27SZPU3J6LeWbMr8U73Aj_d9N2gCFVveVMWSuLVlvfsM02bDJQ_VpTyJwWnSyDwzhtwcZkkDSo-PiYmQgkccP39aC8Amo3OiPqRgDPS5yv_tOTuFvdA-vJSmsqMA5EiSVvDjQNGl61ktral4_sbyoP95RNa9tAldG7tmjYE9YG2Bz7UEUHooDmWV4dR6mqcdHSSaHylLgmq8XEMWSZYDW4MB_S2463Cy8ALaRQFGc9AvFtVcNc1EY3JtyK5tbyf5-fxeSX2QKRhdjj1XzBUhk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6tPY7uK2z9IkzHaIOjg6sYDFhQO38xgP0N7_IQt9y61J8EvrdviM45lV1PpOjHJJHRhiNX4pqQtLa0iNOM4-G-N5E56DE8ZHVRwIHgQPDLAFqMrfULfH3qqBpetyme43JuDhWOnLy9NpKlP8Am3IpKjMxxxm2gWGtg9ZxTIjyRxOsCY7uocUZCkYoHZw7Q3mXlGwy1I90ZsIZblYXwXdpShZnSeaZgKjUpTz4GqTKZU2sfwHBoB9wc2KcZqpk5CYwAdsZ5Ww1faBalhxJsSZ3x7YysMdnK3SMuclSVLFF2Xgnz6WEjsTyi7jyGuHk9vwNkvMCGSY-IZYyMu7JHIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚀
آموزش نصب OpenCode و استفاده رایگان از مدل های هوش مصنوعی زیر :
🔸
Mimo 2.5
🔸
Deepseek 4 flash
🔸
Nemotron 3 Ultra
🔸
Big Pickle
🔸
North Mini Code
🔘
آموزش نصب در موبایل
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب OpenCode
npm i -g opencode-ai
4) اجرای OpenCode
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس‌ :
opencode
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر OpenCode را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
opencode
🔘
داکیومنت رسمی برای نصب در جاهای دیگر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎬
تدوینگر اختصاصی شما داخل ترمینال! معرفی ابزار فوق‌العاده Video-Use
🚀
دوست دارید فقط با چت کردن با عامل‌های هوش مصنوعی (مثل Claude Code یا Codex) ویدیوهاتون رو ادیت کنید؟ پروژه اوپن‌سورس
video-use
دقیقاً همین کار رو می‌کنه. فقط کافیه ویدیوهای خام رو بریزید داخل یک پوشه و با زبان طبیعی بهش بگید چی می‌خواید تا یک فایل نهایی (
final.mp4
) ترتمیز بهتون تحویل بده
.
🔥
چرا این ابزار انقلابی و متفاوته؟
🧠
پردازش هوشمند و ارزان:
به جای اینکه کل ویدیو رو به خورد LLM بده (که به شدت گرون و پرخطاست)، فقط یک فایل متنی سبک از ترانسکریپت با تایم‌استمپ دقیق کلمات و در صورت نیاز اسکرین‌شات‌هایی از تایم‌لاین (شامل فرم تصویر و موج صدا) رو بررسی می‌کنه.
✂️
حذف اتوماتیک اضافات:
تپق‌ها، مکث‌های طولانی و کلمات اضافه رو به صورت خودکار تشخیص میده و هوشمندانه کات می‌زنه.
🎵
تدوین بی‌نقص:
روی تمام کات‌ها ۳۰ میلی‌ثانیه فید (Fade) صوتی میندازه تا هیچ‌وقت صدای پرش کات رو نشنوید.
🎨
زیرنویس و انیمیشن:
می‌تونه زیرنویس‌های کاستوم (مثلاً کلمات دوتایی بزرگ) روی ویدیو بندازه و با ابزارهایی مثل Manim ،Remotion و HyperFrames انیمیشن تولید کنه.
🤖
حلقه خودارزیابی (Self-Eval):
قبل از اینکه خروجی رو به شما نشون بده، خودش ویدیو رو بازبینی می‌کنه تا پرش‌های تصویری یا مشکلات صوتی رو پیدا و برطرف کنه.
این ابزار مثل این می‌مونه که یک کارگردان و یک تدوینگر رو همزمان داخل محیط کدنویسی خودتون داشته باشید که حتی پروژه‌ها رو ذخیره می‌کنه تا روزهای بعد بتونید ادیت رو ادامه بدید!
🔗
لینک گیت‌هاب پروژه برای نصب و راه‌اندازی
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.30.8-universal.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید
#TheFeed
(v.0.30.8)
🔹
بهبود مدیریت لینک ها در برنامه، اگر توی یک پست ای دی یک کانال دیگه و یا لینک یک پست از یک کانال دیگه باشه، وقتی روش بزنید میتونید به اون کانال و پست منتقل بشید، توی قسمت فید باید اون کانال حتما توی اون کانفیگ وجود داشته باشه، توی قسمت میرور خودکار اون کانال به لیستتون اضافه میشه.
📯
من نسخه اندروید
universal
که مناسب همه‌ی گوشی های اندروید هست رو توی این کانال میزارم. ولی اگر نسخه‌های دیگه رو میخواید باید از گیتهاب و یا کانال زیر دانلود کنید (
ویندوز
،
مک
،
لینوکس
،
بی‌اس‌دی
، اندروید‌های
قدیم
و
جدید
،
ترموکس
، و حتی
نسخه ipa
آیفون) و لینک دانلود نسخه آیفون از تست‌فلایت توی کانال پین شده، البته هنوز آپدیت نشده.
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل‌های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ‌های دفید:
@thefeedconfig
🔗
گیتهاب پروژه:
https://github.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
معرفی CdnScanner؛ جامع‌ترین و قدرتمندترین اسکنر IP و CDN
🚀
✨
ویژگی‌های برجسته:
* پشتیبانی کامل از ۱۷ سرویس‌دهنده (CDN): شامل Cloudflare (و WARP/Workers)، AWS CloudFront، Google Cloud، Azure، ArvanCloud، Fastly، Vercel، Akamai، Gcore و...
💪
تست فوق‌دقیق بر اساس کانفیگ شما: در این ابزار IPها فقط زمانی تأیید می‌شوند که با کانفیگ V2Ray واقعی شما (شامل SNI، Host و Path) پاسخگو باشند (پشتیبانی از TCP connect + TLS Handshake + HTTP HEAD).
🫆 اسکنر اختصاصی HTTP: امکان وارد کردن مستقیم IP، دامنه یا رنج CIDR (مانند
1.1.1.0/24
) با قابلیت بازگشایی و اسکن خودکار کل رنج.
* تولید خودکار خروجی V2Ray: ساخت بی‌درنگ لینک‌های VLESS ،VMess و Trojan از IPهای سالم با قابلیت کپی و دانلود یک‌کلیکه!
* پینگ واقعی (ICMP): عملکرد دقیق روی Windows ،Linux و macOS (همراه با سیستم جایگزین TCP در صورت مسدود بودن پینگ).
* اسکن کامل و بدون نقص: بررسی جزء‌به‌جزء تمامی IPهای یک رنج مشخص، به جای اکتفا به نمونه‌های تصادفی.
* رابط کاربری مدرن و فارسی (RTL): داشبورد حرفه‌ای و چشم‌نواز همراه با نوار پیشرفت (Progress bar)، کارت‌های آماری، پیام‌های Toast و طراحی کاملاً راست‌چین.
📥
دریافت و نصب:
همین الان می‌توانید این ابزار قدرتمند و متن‌باز را از گیت‌هاب دریافت کنید. (اگر ابزار برایتان کاربردی بود، دادن ستاره
⭐️
به پروژه در گیت‌هاب فراموش نشود!)
🔗
لینک پروژه در گیت‌هاب:
https://github.com/ScannerVpn/CdnScanner
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSTynsdPDpY2cHkD0NFb98mEO-L0VVKC16mNfz8eP8LSly4TEkB3S9uKI-hP2FvreojbHrwJl5o3AXR7T9l8w3elLmlX6vFV6K4xWGhpdOYnUEbpSHRJxQC4b0Eg1Cz-oIigeK9MOVbQ6RTukuTtEx9lFFqWW69OS2xlSEqRJnXwjRcErmKdpYIpL5xbUHKygwTcqFyhf_0zmtGdaXD31Rmm55YTvQVyweuGHBoz6WZRYMxN3uURO-xZkGPkCY0sY2g6ZDpgyboTCBE0CutAy5Vwc1POxfkk8h0iUib-ryEgp2rubUday08FriCmFIl2vHvOECF-rdLAZ-9--h-3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=S4XugjWIc7OyD_1rz7OB9lmWzJE9nIUPs_7H9lsK0RB85SjuD0Vm0LwzlWRdVm8Itbs4VJp-2JNJezX-4vNdUBkMTVYlSz8PlTCGT0M6uZUl1UVn4iKvvddQJWYsTR7wpRB9qyoXHTojXrpBwrN571y29q9-CiDpRNuGCIB3BG-67nW6RyuK6xU707qr4Rsp2_gVoDoCcShzKrq_6bFiC3vte-I-L3azXPKJf8Zh7AGqWZLvVnZXGnleITeXE5RpSZEJnxnrlR8A1BGEo7I-bLUGc8Z_sJlTe-xhNQgFGSerpA8RtN2L5--0xX2_Zx5_-Iin_vilnOvvRPA-Xr6JtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=S4XugjWIc7OyD_1rz7OB9lmWzJE9nIUPs_7H9lsK0RB85SjuD0Vm0LwzlWRdVm8Itbs4VJp-2JNJezX-4vNdUBkMTVYlSz8PlTCGT0M6uZUl1UVn4iKvvddQJWYsTR7wpRB9qyoXHTojXrpBwrN571y29q9-CiDpRNuGCIB3BG-67nW6RyuK6xU707qr4Rsp2_gVoDoCcShzKrq_6bFiC3vte-I-L3azXPKJf8Zh7AGqWZLvVnZXGnleITeXE5RpSZEJnxnrlR8A1BGEo7I-bLUGc8Z_sJlTe-xhNQgFGSerpA8RtN2L5--0xX2_Zx5_-Iin_vilnOvvRPA-Xr6JtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_GJI2ZdtTHN84dVzY33CsCvYtTUpW_lpj7cuYYi9fe-a7wTrgLcZUFNbZ6jqZSsX2YTsXCC0ydUXRU7VDPzT3zd5cicd-OEYYQcboaaUA-NUWllTskkNpcEsuspUYp2h6Wx2BjFOCybD4LvKx64ni1FUygpip6PctZ8qCoipoXpsFrCBaQecmATB_9CxNa9crCOUsvicQvGBNdaEHjdzxhuFGDVub_Tykw-daibIpaHLu2B0HuFNVFZrUtkeVg0iIo60yM3wv35rwN3MUkFxc_fUBbxllln16LZ7gcj5RyjDOyQ8lZkuMtLz9-1F8iJ4xSCzg5ZKHxKMGBFpYsw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@‌ArchiveTell⁩</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=EbrH-i4qtguDyjMo6SOY_6g5qiJtS_71UCWOG2Xnv1OQdDYFgZuhKTVg3dqV-HHBjRRaZ2nmfCeSFoYrFdc8u3DRYcjLiBT5WOl1HdIHaGgFpkz_0oBb4VAtzbv_eggJ2yYA7jmF4470hDaf1t125EslaNRPosVltZBq5QLxVqy8c3psoHLz--EuVuQ-DsKN_zeMtRy-y8oytUv8xDYLWBg441XBMWtcnkNjf3LwcIpw94qPDcNh6VTIDrz7jdAFSkrBzxe6s0egLliEMQLOPfGjWtjMZ5EBVPiVrn2wBUsycidHm7td9Jx7ILN5Mtip2U-xDkEH-CQ4PQfHCLAKwkHLGVRU33sQZazq3fB9ubrEnIQSe5RMb7siYsbF6-dn661nG2AEM_SMLjCYJFpRT_qj4tjrY0pTsrT_iMoGv-Ftj-ZelrvaC4a7c59i1dQPCCDxqMfBp5s8BydjS2H1wBU_rtBvTfh7_dDY8sEUgwq9Ny6VCX5T7Xzz9Y1MDsq2Q-av5zenjxM_q9EeIXgn9_gtQ1gn3h8An5jWeReQU4hBJBbMkmOdSAU9aGNwOw_TrUcAtMrgP-VMWmhJEnO36dqhJLiVm8Tiw4EoPvOOcR7SRvNLWp2iqyQwu3A2T3jN8mMUiqhWSq-SJJ60-yerpcOn2yncwMdqez-u0GOevD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=EbrH-i4qtguDyjMo6SOY_6g5qiJtS_71UCWOG2Xnv1OQdDYFgZuhKTVg3dqV-HHBjRRaZ2nmfCeSFoYrFdc8u3DRYcjLiBT5WOl1HdIHaGgFpkz_0oBb4VAtzbv_eggJ2yYA7jmF4470hDaf1t125EslaNRPosVltZBq5QLxVqy8c3psoHLz--EuVuQ-DsKN_zeMtRy-y8oytUv8xDYLWBg441XBMWtcnkNjf3LwcIpw94qPDcNh6VTIDrz7jdAFSkrBzxe6s0egLliEMQLOPfGjWtjMZ5EBVPiVrn2wBUsycidHm7td9Jx7ILN5Mtip2U-xDkEH-CQ4PQfHCLAKwkHLGVRU33sQZazq3fB9ubrEnIQSe5RMb7siYsbF6-dn661nG2AEM_SMLjCYJFpRT_qj4tjrY0pTsrT_iMoGv-Ftj-ZelrvaC4a7c59i1dQPCCDxqMfBp5s8BydjS2H1wBU_rtBvTfh7_dDY8sEUgwq9Ny6VCX5T7Xzz9Y1MDsq2Q-av5zenjxM_q9EeIXgn9_gtQ1gn3h8An5jWeReQU4hBJBbMkmOdSAU9aGNwOw_TrUcAtMrgP-VMWmhJEnO36dqhJLiVm8Tiw4EoPvOOcR7SRvNLWp2iqyQwu3A2T3jN8mMUiqhWSq-SJJ60-yerpcOn2yncwMdqez-u0GOevD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=CdhlEa2zYiuyXO6rNSiOe2FCC2fp4STHAcf5uBzhzBgtlxSOzF8QgWCQlE-KkcDd6r1Hjo9XKvHpKWlkfUZffnr_og6ZJBXOwtrEuXNzB2Py2oblQt-SNrZK1EqU1IIKJa12nZPQF285klChjXctnVY6chwahwgPEXccghe4tPs9dK336S6zFYGvL6qkjfwKbtfnxN8Fs3pNF0nH9RSq3R7CqZB63Jxd7-u2wNaNAIHu-UfXeleDGkvTDKw2-IGeW4Z_ewTEIIBErFLJwrHn2yRn2zZDTpPrALVt37prX9Tnb9YB9DH2Ljr6CXxvW_DAFFxnxoZK0NF87F1cNzNWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=CdhlEa2zYiuyXO6rNSiOe2FCC2fp4STHAcf5uBzhzBgtlxSOzF8QgWCQlE-KkcDd6r1Hjo9XKvHpKWlkfUZffnr_og6ZJBXOwtrEuXNzB2Py2oblQt-SNrZK1EqU1IIKJa12nZPQF285klChjXctnVY6chwahwgPEXccghe4tPs9dK336S6zFYGvL6qkjfwKbtfnxN8Fs3pNF0nH9RSq3R7CqZB63Jxd7-u2wNaNAIHu-UfXeleDGkvTDKw2-IGeW4Z_ewTEIIBErFLJwrHn2yRn2zZDTpPrALVt37prX9Tnb9YB9DH2Ljr6CXxvW_DAFFxnxoZK0NF87F1cNzNWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=tfZPfDt9ADDzWdUMWDorJfjsnzLvvDtNY3CWIUufuP_JgnUcbXSczoG0_yC0aaCOiUyBV1hrgNVW_9GOIgxb4Nhi5wsqGBrdcRw9W5neF2REsml8V1pWPwG76EUb69h_vKBJwJp-M-r-LmWddVV4CQ3RTYeQWVN-vmBTYUGi5PCS8usMb8-w-Yg3cz6Png9RE4qdp6sE7IQ_QFxcvUbqipYMk1LLHEMOwdWBH1oKpnkDefEKKzfmubGeXlaDcm5dcuf22Eh8GAmVa652CYJEM0w0KGPOW3wqQeO-e2II7HXWee8VqFe_QWdonom49yP4jwhYQ3ibvLtrGwiSgastVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=tfZPfDt9ADDzWdUMWDorJfjsnzLvvDtNY3CWIUufuP_JgnUcbXSczoG0_yC0aaCOiUyBV1hrgNVW_9GOIgxb4Nhi5wsqGBrdcRw9W5neF2REsml8V1pWPwG76EUb69h_vKBJwJp-M-r-LmWddVV4CQ3RTYeQWVN-vmBTYUGi5PCS8usMb8-w-Yg3cz6Png9RE4qdp6sE7IQ_QFxcvUbqipYMk1LLHEMOwdWBH1oKpnkDefEKKzfmubGeXlaDcm5dcuf22Eh8GAmVa652CYJEM0w0KGPOW3wqQeO-e2II7HXWee8VqFe_QWdonom49yP4jwhYQ3ibvLtrGwiSgastVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCqwvrzarGUryH4lHgIpUN51O5eQkgtXfi5rwG8lOzWCD52V_e5z75Nl_3yuFG2_n8Ufd_utcqiqBKiXsTVnvsHp0jXjB0dQ_CyLvJWWYwUi4nPcSD6B4kXkEEA423U_6o6Aqg8CbdJtA6QJ0iK4ZSbvwNasUxQJcKqzpUxs8pdyrYcXCwPdbZZUPyhB0PfsxCr1ThgJfg64OmDxRy2TUrzeSnKW6Of6mRu7bAUqugA0urDrRdBEBg1MtxnRhQDU5ZkQ7qwerTcB0UjWORaoKOl4-6OMACBWjAcGhrPU3f9QI8IOn9hNVApElvkSq8RWX3pD1l1KJte-Fb43Nmu-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=XOvBg039vi_NQ-2tnFt0niuxFH_0PZViiWVVch6ABBv4nRx-DeD1hRmYc5kXmgNzcPeS2jlaEOky9j7eAOawiB0ardmIgY0gLfg12LXorS_oLe87AhrW10jM8pfGQwX-E0ihfRQ2NO8s9sGPT2LeQpUwRhorPYFF417qqJZ50qxFtlgYtqJhDJK8nOYQVRb4GLPkiycbcGk7CB50UvpwK2271X3sEmFU5dcr1UomymEauI2z2Qk3aJfOjdZ8uaAV0ARma3TIq77dl9mJtsGbxpJx5a66qHKOnN7lC4rAS5H2w0_P6ufuIhyHFZBJCt0IjJOv6pO1-9_RmdUVCMSNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=XOvBg039vi_NQ-2tnFt0niuxFH_0PZViiWVVch6ABBv4nRx-DeD1hRmYc5kXmgNzcPeS2jlaEOky9j7eAOawiB0ardmIgY0gLfg12LXorS_oLe87AhrW10jM8pfGQwX-E0ihfRQ2NO8s9sGPT2LeQpUwRhorPYFF417qqJZ50qxFtlgYtqJhDJK8nOYQVRb4GLPkiycbcGk7CB50UvpwK2271X3sEmFU5dcr1UomymEauI2z2Qk3aJfOjdZ8uaAV0ARma3TIq77dl9mJtsGbxpJx5a66qHKOnN7lC4rAS5H2w0_P6ufuIhyHFZBJCt0IjJOv6pO1-9_RmdUVCMSNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-kze06yKLAZTwhdAx701uY72jySHpLGFuyz7fhx50tI6WBoSNC996MmFubsy0idg5wjNMANwJ5yE_9kRztXz__gdzaWoBkeomjX3LDuCUxE6tKmXFfgQn5hSuxGkGL2-s68jeJzbTbvFXDyapclXFUpqJftXPhaR3miT5ziWBO5YEKutf0PEX2vu23SKiueCvYipuqSZ6Z0rI_wR08cuNxksjZeY2oU3c3ytJc-Upw75pWhCDTVlRKBnILSv4EX0xY0q-O14N9WMqdU1rKfqvnUQ4WWoKEwQRsvQkfmWm7Kuw9DtQLJT65JaIg-Mn62jzTvz3DsUh4znEtm2ya6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8rj8RRTWC2dpY_bDNNBC1xDZquIK1PGjNePkCaml2KD4rqkfQ_cGSvkWUk2mlJHKOnFR9GFUERENEKWrRU8FieCdQIGJMlnXivYN5_Dxsh0-exTFyd74HxSkNWuEW-_tYxyENWyjwFy8_Si-FBOf4ThVfSY5faUPaRvCLg7Gn_iitV3Q7U7vULjiqWaHztisxM-MfJG2W8UrEbZWpaVnAUb1MZdK1S_6JrZC76tx6lxqIf60f9Py_JDef0H7c2hhY-iQMuLQuUaIXOnUvP1q7rFblF7PPqY4VNNQgrBa7hFQihpBHO0Z4Nx-HGxWRZncN7XFjJntty7fxwi1-ct_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک میلیون توکن رایگان Gemini از طرف
گوگل؛ بدون نیاز به کارت بانکی!
🎁
✨
گوگل به تازگی یک فرصت بی‌نظیر فراهم کرده است: دریافت یک میلیون توکن کاملاً رایگان برای استفاده از جدیدترین و قدرتمندترین مدل‌های هوش مصنوعی این شرکت. برای دریافت این توکن‌ها به هیچ‌گونه کارت اعتباری یا خرید اشتراک نیازی ندارید و همه‌چیز با یک کلیک انجام می‌شود!
🔥
چگونه کلید API خود را دریافت کنیم؟
1️⃣
ابتدا وارد پلتفرم Google AI Studio شوید.
2️⃣
روی دکمه Create API key کلیک کنید.
3️⃣
تنظیمات و محدودیت‌های تولید را به دلخواه مشخص کنید؛ کلید شما آماده استفاده است!
🤖
مدل‌هایی که می‌توانید با این کلید استفاده کنید:
Gemini 2.5 Pro (قدرتمندترین و هوشمندترین نسخه)
Gemini 2.5 Flash (سریع، بهینه و همه‌کاره)
Gemini 2.5 Flash-Lite (فوق‌سبک و اقتصادی)
💡
کاربرد: این حجم عظیم از توکن‌ها برای ماه‌ها کار فشرده، از جمله کدنویسی، پردازش و تولید متن، تحلیل داده‌ها و حل مسائل پیچیده کاملاً کافی است.
🔗
لینک دریافت کلید API
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6704" target="_blank">📅 00:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtOTaUO3EcKoqAXFZnMUMu3CLJwvCmxkZBhCTAIc228-fJFAvtiHiFMaUqfbrWpeJsVoHl_eGOPuLv6-rPkgelcwcxpxzVp3ZPeV2hiDedp3EyLbSpLIoUxiHfXsQH2F9H9njoAOgDuSdfOe0oCueX8M33b1a668diyqX483Efe1zXTpeFUhht5ioYLNiYF-NQix6efsyeXEsvQDyPxLrrvxhKaFoo0F9X5xrU7t41sOY7bPgEhfiJc65fEnrHhigA6z4RdOAy97D6pidibaK4RqeqTpIS5QP9X7rqo1H4yyQShKvB5WI5q1DuVhoZ2i-CDGXa-9iOpNsfcedlr0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفسیر خطاهای ویندوز با ابزار داخلی
راهنما:
— کد مورد نظر را کپی کنید، مثلاً 0x80070422.
— ترمینال را باز کنید (با فشردن Win+R و وارد کردن CMD).
— دستور
certutil -error 0x80070422
را وارد کنید.
— توضیحات دقیقی از مشکل را دریافت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6703" target="_blank">📅 22:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWwXsE9TSOEIAgFMKgUMkenZS-ovPKhsscBnV2nbpVy_3SVrbE-eq_yx37cMFpw7iLgoTQHJGWLaFNGsTFYon680-EJVM-Z7wgIZCX_3To2A7lFKN2RuwCObTy-Hg8Hn6D8yMR6m-z0a7T7um308XtWxdpBYsnibCOAmXkiV9nH0-xLnDWUu0waHKtCO6QSJDTNyasniAZtlGOU3Nh9UE6ktyaDYMW3r6MX0ufxsXdGQtdfk0EHH9ZEQ8uvmAZuxPZuJc8JacySTOVE5SMVioTmGgoJ4iaEMSCuFQe0nq6PIyauKaiNR8kKX8ZhLa35aa2lEBGv6UzzIkd4oZ6txeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا پولاتو چیکار می کنی؟
پولام:
به زودی ۱ میلیارد*
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6702" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1d1XISjmklzix0J9-i7hI53oZLh6S4A_igPIqFDFX903TWcXy0urdXfoFXRYcWqsG8o3cZ2ge9uP5rrEg6dMkFdWBK-KYp2dKu7cWUnjpt97Zx6X15SZwK70-CtWpN2-k25yVE-IvgB1kCR_gD2CDPbjUB4tH_V2rixgQTnz9ApExTZtYnqQwGBPkCMXviRyKxrXeEkzmcyATbnDp-fm7-31qr9yz_IEiK8gcy29dJbPvvwnjWUmQM8Za4CzHcySElmNd_5kjMYCYbMV3vsAcSFdWhdthc2xE9tRI_f3_dZAVGuriBYRh9AHKTyghnzrU-eFYwBnFPQndJFERA5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKopogRmqaQExVNGZudakb0SnJSehHxhL-DTbor7ASXGInpU_JsmcSbJDKOS0FyUViDmThm2yVNmnZCQ2tbDS6Zc-Y5f8_a541SUE_iXa6NIHJh90N-aR4Q6R64E-XXdqfbyAre5r7cF4NyHCyvkv9ax-NZudZB19VBQn-EmkJ2cCyk4ImmNoFx9wN_068pqLHbHXJkYXbC6crLwg9S15rX9xCZPfoZjHVtBS4WqmM31sB-RnW72FXJBzhAIZr5fni1eRTgoAArdlYvJ1moZ2XJex_8Z1kb6EKWbwm0eC2-ZBuhcZ6BibSTpy9i8XLYLqzCXjMuVBUsUjI1BJFOADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfJj4eSDfRU8s4birjvyZBsP4hvr1mH9dnA_ZAcsing0v5ILHq_zQp_HkEYnP_efHIIDvPRubzoocA3eybfqmKfXrd3FstPftUYTFViynEPhevPuWDPvxvBDazO9Writeq7GDhUsQfcnrCznJK1re0e2RVa_I-grTqf-EuBZxPyUtBKuVfMVGpg7VxmXD4AfM6qToenXdxdHBln447Q7J27A_gD_8Ta3Rw-Z3nTFkbu3u08bKCGS-89UCtCi2iRZJqkCOSnYkGv6t3EQm8K2l1vLyzO2p8Y9Zn5cYb6Yj0gJdK1NVuAHGYNLWBOE3fKn8avWJ-Fd0ez2-Q-x5fmiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppT_oGeZ220H8RVpBhMomQdIl4J1Ps8I-ED2Z5yARK73QiirSW0Fi2Q4EejSwf9qGP7ZSYSSJVh0ZJZ_GBG4hohbKDHWSt1Qx_Nwcgw8iSj3BTlFe-P_K1ydvKRfRJmGLxTAgFPvKyjtShO36ohm6KaFIZ0ExK5cRUcYItsCge12kly5P6uB8pAXORU-ZEGX3CNMj7RH4tqeG8HqbkjLEF5Ei_ZgLQfwKmFHa48kAauDa5YSUEQA0NJYJTxjjs502YDlSk0okO9MJpXXqsjSsvyQs8POjAyB34HQB57zXl-I6VSXRGQLq8nH9u2X7qUrSQ-DwjFXADsV0E83u-4-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKDhmdpTyDvA-lcMFixBbkgF7c4ZNHQHyf_JCMUsYqjSAjioU5mDF3HZVrjO_tK2cI39IOdEXyjeAf51RpULSt5nD5isTjfzIwCXmCxO5qpCxEAwinm8mx_1nCq9cKj51KrOOCJErFMRojKvVDXBf6oMsQFGRkjdBufvs6TL6Dy9kRw-KFeTElccWwsj_DUTVgD44xL5gFGM_FCBJUAxJEa3bEGUJWOQ1gClS7FmraQgFHOgCTZjuOPO8h90oDqZKaG1FD8XOqvv-9j5cC6u-DU5HWwOC30YD-Cwv5u_j6_sp6RvEo0x1jl7qpeX_bcZQ459xRwvg88D-64W-OZD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDcrYox8JT009LN_MxQbeI29iHm5nZeCRLLNLgw7TFCBOWsE06x11jNAVjk847DzzrdiEDXQK_vrgIWKogedXM3KZOv5BCr3KpvXSTq57joRi5ADIGpLjK43TyRMgq8becK0MIB-no-OsPctYhGWlhHW3XzWZZKTtbu9mc8YBFXz0TFdXCfeApCSI_U51abmwUVbdkZ13C5UhI56uCpIJknY-yCPm6l0_s14rakCzWreqIC1iXQin-GZMB3eYYXMJl_JzXDxKi6oHDaksbIGE8JWWdnlLE1q33bmiU1PrpQxwvP7VvHuoj2VAwpt9lEKYuc3TDmMWz9Vb0eeQhDUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJDTfs7UdXg0N0ECpAL14-chn9cpD-olCZ-Jom66wVeF95EC10GAVFiroVwR93zr2fF_UFUYiknZoQKdpl8sf12A5IZMyrAiKfrb2T5QZN0pWlGiHMAL7NQ5Whsu9RH14U8pk_zwNxEHBhLGw18mNFHsjzl47rtOeI-x-WqvANeUS2Sl2Gv3kTJLdImUtNluaZAaVURczwJItDsb7Gz4KCk0jP1e5gl1UEfUojai8pYpd1ogNI9TF3IlumNMQQLGBAQCHOturP3E2N07b4T0tko1Eub58-RuQd1766SD28rNGagFuIzQYwUUN6jtyC21n-Ysv_cBckw-RXUjzFqd3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج
جایزه عکاسی با آیفون اعلام شد.
در این مسابقه سالانه عکاسان از سراسر جهان بهترین عکس‌های خود را که با آیفون گرفته اند، ارسال می‌کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6695" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJodCITZXu_qtezstlVd3PhialacVktwY-r_UCfyeP2xD7_zcpoUEbLXNVbBg5tugLTe0xnAiXezyZNGX4XMvZN3OfK8dGhre4JudaAPm75_VLjJvkFbYpS6E_28QJ_RM2jCP9RVL8svlyxEa5TEid2xNvf7X5jUPdmt4_n7EE7AOmaf0yNhF4ba421X-sCNS0F56qpIIAFkYYL2HYxlG8QPDbe3voRNu77-AU-vWL0Jr5BCTuJdf7qScbMEdCQqnc1wdOsUvSSVfFe2Xpl7EwoRTTshdcDDUx3R-wkUG7A-VKpBH24q5_8CjJlRQNl0NN7zvBXH4uaBTC0FA1HpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AITwitter Generator
یک افزونه برای تولید توییت است.
این افزونه که بر اساس فناوری پیشرفته هوش مصنوعی ساخته شده، خلاقیت و سرگرمی بی‌حد و حصر را به حساب کاربری توییتر شما اضافه میکند.
https://tweethunter.io/generate-tweets
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6694" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYwKNPydVFxAgebLP7_MpdaxDsLRXkye_KWQ7MhjE_3fz5jqV9r3yzGEKHCewOX6Jowb9qLyfgaYfqwL2_D4Oz1661HIHLxMtoQAYUEDhQM3ljphD7F0xiW3CoJ0yPO0BTP6szhCctmUV1UGSqA0QKoq5atJ6dzWX3FawinE4YJY87cIFcNOzCmrFsC8TUlNbvWVdQ_SwsOBmMHmV8uAT4B7-3iGGZFiMlhTMO25BP_qnHTu9yTJxGrPRgERmhd7xd_mrSXHMT9SlPy3ci8Ca-hBQM4G-iUGEoKEj0ZqkxKc5pwz4KXfE8AsRxKX0ez2T_5z0XYixvSXtFvGHUjvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک مجموعه‌ای رایگان از پرامپت ها برای Claude ارائه می‌دهد
🤩
این مجموعه شامل ده‌ها راهکار آماده برای بررسی امنیت، رفع اشکال و بازبینی کد، خودکارسازی وظایف و موارد دیگر است. برای هر پرامپت، توضیحات مربوط به نحوه عملکرد آن ارائه شده است.
https://code.claude.com/docs/en/prompt-library
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6693" target="_blank">📅 15:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2eHqUEtmFdqr47BPSlMclweMtUR9eazTbbW0pG-6fTwk4v_J91yPK3qNXj9z7fHNVMmULKj0V9Na19Ld5iqO6kj3hzwS0tZPF3ebgRFWXCXMknnbejVpUiYA3UY5wTiZbXeIW2JrOuOuSXdcubVUZplUs_zmqEncoqUakz3BVxQz5onaq2e67uqQLM6eMyzHEx9G4R4r3IrN8RT_G3VdF26eUrdnq9BIJERmgHiTtRaiXSnM3aY4dBAVGMlZswZVsQEHEDPhd8mQ1AEVuvdQUkHrETWknwbb69EQuy8e2t7jGNfw3o77JJ1piVHIHSVRUG-kYPg2CRF3uNCECHTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتوشاپ را فراموش کنید
🤯
یک ابزار مبتنی بر هوش مصنوعی می‌تواند تمام وظایف را با دستورات متنی انجام دهد و برای این کار نیازی به مهارت‌های طراحی یا دانش فنی نیست.
🎨
✨
🔹
همه چیز بسیار ساده است: یک عکس یا تصویر را آپلود می‌کنید، پس‌زمینه را تغییر می‌دهید، اشیاء اضافی را حذف می‌کنید، رتوش انجام می‌دهید، کیفیت را بهبود می‌بخشید و از ده ها امکان دیگر استفاده می‌کنید.
🖼️
🛠️
🔹
بدون ثبت‌نام و مستقیماً در مرورگر
🌐
🔹
کاملاً رایگان
🆓
https://ezmaker.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6692" target="_blank">📅 14:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🎁
500 کریدیت رایگان ‌Opus 4.8⁩ و Fable 5 هدیه بگیرید!
‏دنبال دسترسی رایگان به قدرتمندترین مدل‌های هوش مصنوعی می‌گردید؟ با این روش ساده، ماهانه ۵۰۰ کریدیت رایگان دریافت کنید.
🚀
‏
1⃣
وارد سایت زیر شوید:
🔗
‌www.relay.app
⁩
2⃣
‏ ثبت‌نام کنید:
‏با اکانت
گوگل
یا
مایکروسافت
خود وارد شوید.
3⃣
انتخاب مدل:
اگر روی آیکون پروفایل خود کلیک کنید و وارد تنظیمات شوید
در بخش اکانت ، اولین گزینه را بزنید و select model را انتخاب کنید و مدل مورد نظر خود را انتخاب کنید
4⃣
لذت ببرید:
‏از امکانات پیشرفته و کریدیت‌های رایگان ماهانه استفاده کنید.
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/6691" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🧠
یک سرویس جدید که قادر است مدل‌های سه بعدی را به کتاب‌های آموزشی تعاملی تبدیل کند!
📚
✨
هر مدل سه بعدی را بارگذاری کنید، سیستم به طور دقیق ساختار آن را تجزیه و تحلیل می‌کند: عملکرد هر قطعه را توضیح می‌دهد و نحوه کارکرد آن را نشان می‌دهد. در پایان، یک آزمون کوتاه برای ارزیابی دانش شما ارائه می‌شود.
🧪
🔧
برای آشنایی اولیه با قابلیت‌های این سرویس، مدل‌های آماده‌ای در زمینه‌های پزشکی، مهندسی و علوم طبیعی در دسترس هستند.
🏥
🏗
🌿
https://atlas3d.space/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6690" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=KljMxJQhDe3E9j2W94LNUvqqbRIcxRKUcJS6RVjKli0_WBRkU2JP3x1L5SQp3oKdKNL9fsYPWtOK2pIHjjGc2asNQxWOjizfFx2erJTBtcgIqGUM3yCUyucgAVZnotvJaqJdw1GmXs485_k0y-2ZW7eSFboC_JyIJ0GDuPzV4GDuSUFHe4w-V67DEuOjv8XpdFZKc9FJkJ0oPl0a0uf1NSzgjbd0woH8iYjA7wna3RmxMrcqKNVFQxZo9SeEcLSKCrC2AnPQkhfMywTCa1HPpcZiQQu5R9mp5W9-2MTIQI6F7XEef_SjPFffzEzY1CB7pb75AcT8VH7cJyqYpZ7kPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0677cd71ec.mp4?token=KljMxJQhDe3E9j2W94LNUvqqbRIcxRKUcJS6RVjKli0_WBRkU2JP3x1L5SQp3oKdKNL9fsYPWtOK2pIHjjGc2asNQxWOjizfFx2erJTBtcgIqGUM3yCUyucgAVZnotvJaqJdw1GmXs485_k0y-2ZW7eSFboC_JyIJ0GDuPzV4GDuSUFHe4w-V67DEuOjv8XpdFZKc9FJkJ0oPl0a0uf1NSzgjbd0woH8iYjA7wna3RmxMrcqKNVFQxZo9SeEcLSKCrC2AnPQkhfMywTCa1HPpcZiQQu5R9mp5W9-2MTIQI6F7XEef_SjPFffzEzY1CB7pb75AcT8VH7cJyqYpZ7kPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😂
سووو رونالدو با رینگتون های مختلف
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6689" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آموزش‌ گرفتن Fable 5 به صورت رایگان تا 1 ماه هر هفته 70 دلار
💰
برید توی
Aerolink
و ثبت نام کنید
📝
لینک ثبت نام
🔗
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
📄
نحوه اجراش روی
claude code
هم همونه فقط این تنظیمات رو بزنید جای اون
⚙️
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
هر ورژنی از claude code هم بزنید قبوله
✅
لیمیتش هم دقیقا مثل
freemodel
هست
🔒
موقع اجرای claude code بجای دستور claude این دستور رو بزنید
👇
claude --model claude-fable-5[1m]
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6688" target="_blank">📅 22:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
معرفی Qwen Gate؛ دسترسی رایگان به API مدل قدرتمند Qwen 3.7-Max!
🤖
✨
مدل Qwen 3.7-Max در حال حاضر یکی از بهترین مدل‌های هوش مصنوعی است، اما استفاده از API رسمی آن هزینه دارد. ابزار متن‌باز Qwen Gate نسخه وب (
chat.qwen.ai
) را به یک API کاملاً سازگار با استاندارد OpenAI تبدیل می‌کند تا بتوانید به صورت کاملاً رایگان و لوکال از آن در پروژه‌هایتان استفاده کنید!
🔥
ویژگی‌ها و قابلیت‌های این ابزار:
1️⃣
سازگاری گسترده:
قابلیت اتصال بی‌دردسر به دستیارهای برنامه‌نویسی مثل Cursor, Claude Code, Continue و سایر کلاینت‌های مبتنی بر OpenAI.
2️⃣
چرخش اکانت (Multi-account rotation):
پشتیبانی از مدیریت و چرخش بیش از ۳ حساب کاربری برای جلوگیری از محدودیت‌ها.
3️⃣
امکانات کامل:
پشتیبانی از فراخوانی ابزارها (Tool calling)، استریمینگ سریع و دارای یک داشبورد حرفه‌ای برای گزارش‌گیری.
4️⃣
پشتیبانی از مدل‌های مختلف:
دسترسی به Qwen 3.7-Max, 3-Max, 3-Plus و سایر نسخه‌ها.
💻
نصب و راه‌اندازی سریع:
برای نصب کافیست دستور زیر را در ترمینال اجرا کنید:
Bash
curl -sSL https://raw.githubusercontent.com/youssefvdel/opengate/main/install.sh | bash cd opengate && qg
پس از اجرا، آدرس
http://localhost:26405/dashboard
را در مرورگر باز کرده و اکانت Qwen خود را اضافه کنید. حالا می‌توانید از آدرس http://localhost:26405/v1 به عنوان Endpoint (درگاه API) در نرم‌افزارهای خود استفاده کنید.
⚠️
توجه بسیار مهم:
از آنجا که این ابزار بر پایه اتوماسیونِ رابط کاربری وب کار می‌کند، احتمال مسدود شدن اکانت توسط سیستم‌های امنیتی وجود دارد.
حتماً از اکانت‌های فرعی و تستی استفاده کنید
و به هیچ وجه حساب اصلی خود را متصل نکنید.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6687" target="_blank">📅 21:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
ساخت بی‌نهایت اکانت معتبر با یک Gmail!
📧
✨
سایت‌های حساس (مثل صرافی‌ها، ChatGPT یا AWS) ایمیل‌های فیک را مسدود می‌کنند. اما با ترفند پنهان «پلاس» (+) می‌توانید بدون نیاز به شماره موبایل، بی‌نهایت ایمیل معتبر (برای دریافت اکانت‌های تریال) بسازید!
🔥
این ترفند چطور کار می‌کند؟
قانون جیمیل این است: هر عبارتی که بعد از علامت + (و قبل از @) بیاید، نادیده گرفته می‌شود.
مثلاً اگر ایمیل اصلی شما ArchiveTell@gmail.com باشد، می‌توانید با این آدرس‌ها در سایت‌های مختلف ثبت‌نام کنید:
ArchiveTell+twitter@gmail.com
ArchiveTell+vpn123@gmail.com
از نظر سایت‌ها، این‌ها ایمیل‌هایی کاملاً متفاوت هستند، اما تمام کدهای تایید مستقیماً به
اینباکس همان ایمیل اصلی شما
ارسال می‌شوند!
🛠
ابزار کمکی:
برای ساخت خودکار هزاران آدرس مشابه، می‌توانید از ابزارهای آنلاین
Gmail Generator
استفاده کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#آموزش
#ترفند_جیمیل</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6686" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaWeluEE8-3f3iq6M00Q4dl4Wiv105K09N0hUX4_Ai0ApxvF7LBvtgKJxEkx-_P_0iT6ILjMmgsyE24CKxeC_mWwYtAeDlRrc-FyghHeFBbnjjnz_39qng4wpVh3QBhWSfMvBn8sisvhyEoUei1uQBeK4-SfOaIt09V7WKJQwFZENTF5tpK5_5rtPiezf8pB1MtMfsICDjbHRqd02Xi-IU4pF5ZyMocWHNT0a5kYYxnpqjAMtGYTc7a1lEMy2fr_LgbEWRn8mzeepFuKsLkLX9ixJCbKqNlc2CYGkouVgvtaZ7PyIjQ5dy6QSn5n8B-NFUypp_Ailg-tsZ3LFZ5dCQ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65311253ad.mp4?token=p8vadFK7R14QFQfMqqBKwiF_orRZ-ferjyld56tYmVnVBzhoXnPFTvz2SoSlKfEZnbCofcdp2Q1NakztwVfdp02n-xWdtqvMPPB5QPz4lvydMz9Jj-HomzyFNEnpOx-o7P4xqXGFg0_q_5DhW35tNKUKiSS_eHFHGiNiDrhZ9UeOw0QHY09ZbKSPuD5nLzRDGfPtMd7Aw7jNfvGRNI36SJb3xu2GLLSYODlvbiZqJ_LPuCqYR1a-Ph4XJK7Yd7HpAFc1pfbDjGKuf046tM3DCnw1DcWdU7TrJ792sAXSDLqQXsllGfh7DowEoRev4SGLlNCU-EXvXuvg9O2bhSgMaWeluEE8-3f3iq6M00Q4dl4Wiv105K09N0hUX4_Ai0ApxvF7LBvtgKJxEkx-_P_0iT6ILjMmgsyE24CKxeC_mWwYtAeDlRrc-FyghHeFBbnjjnz_39qng4wpVh3QBhWSfMvBn8sisvhyEoUei1uQBeK4-SfOaIt09V7WKJQwFZENTF5tpK5_5rtPiezf8pB1MtMfsICDjbHRqd02Xi-IU4pF5ZyMocWHNT0a5kYYxnpqjAMtGYTc7a1lEMy2fr_LgbEWRn8mzeepFuKsLkLX9ixJCbKqNlc2CYGkouVgvtaZ7PyIjQ5dy6QSn5n8B-NFUypp_Ailg-tsZ3LFZ5dCQ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیه‌ساز هاگوارتز ( مدرسه جادوگری سری داستان‌های هری پاتر ) از ‌Fable 5⁩
در این قلعه افسانه‌ای می‌توانید درس بخوانید و با جارو پرواز کنید.
🧙‍♂️
‏این شبیه‌ساز مستقیماً در مرورگر اجرا می‌شود.
https://hogwarts-production.up.railway.app/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6685" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ظاهرا کلودفلر اعصابش از ایرانیا **ری شده و از این به بعد دیگه ایمیل فیک قبول نمیکنه اگرم بکنه تایید نمیتونین کنین اگرم بتونین تایید کنین بنتون میکنه
😍
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6684" target="_blank">📅 18:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ArchiveTel
pinned «
دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...  https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6683" target="_blank">📅 18:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🛡
آیا وای‌فایِ شما واقعاً امن است؟ (یک تستِ ساده و حیاتی)
خیلیا فکر می‌کنن چون روی وای‌فای‌شون پسورد گذاشتن، امنیتشون کامله. اما حقیقت اینه که اگر پسورد شما ضعیف باشه، نفوذ به شبکه و شنودِ ترافیکِ شما برای یک فردِ آشنا به تکنیک‌های ساده، کمتر از ۱۰ دقیقه زمان می‌بره.
⚠️
چطور تست کنیم؟
در دنیای امنیت، ما از روشی به اسم «Capture Handshake» استفاده می‌کنیم. وقتی یک دستگاه به مودم وصل می‌شه، یک تبادلِ اطلاعات (Handshake) بین اون دستگاه و مودم انجام می‌شه. اگر کسی این تبادل رو ضبط کنه، می‌تونه آفلاین و بدونِ اتصال به مودمِ شما، اونقدر رمز عبور رو حدس بزنه تا بالاخره یکی درست دربیاد!
💡
چطور نفوذناپذیر شویم؟ (اقدامات فوری)
۱.
پسوردِ قوی انتخاب کنید:
رمز عبور باید حداقل ۱۶ کاراکتر شاملِ (ترکیبِ حروفِ بزرگ/کوچک، اعداد و کاراکترهای خاص) باشه. رمزهای ساده مثل شماره تلفن یا کلماتِ دیکشنری، در لیست‌هایِ هکِ «آفلاین» در عرض چند ثانیه شکسته می‌شن.
۲.
غیرفعال‌سازی WPS:
این قابلیت که اجازه می‌ده با فشار دادنِ یک دکمه روی مودم وصل بشید، یک درِ پشتی (Backdoor) خطرناکه. حتماً وارد تنظیماتِ مودم بشید و
WPS رو کاملاً Disable کنید.
۳.
ارتقا به پروتکل WPA3:
اگر مودمِ شما از WPA3 پشتیبانی می‌کنه، حتماً تنظیماتِ امنیتِ وای‌فای رو روی این گزینه بذارید. WPA3 به شکلی طراحی شده که اصلاً Handshake به روشِ قدیمی تولید نمی‌کنه و عملاً در برابر این حملات ایمنه.
۴.
تغییرِ دوره‌ایِ رمز عبور:
حتی اگر رمزِ پیچیده‌ای دارید، هر چند وقت یک‌بار اون رو تغییر بدید تا اگر کسی قبلاً در حالِ شنودِ ترافیکِ شما بوده، دسترسی‌اش قطع بشه.
این پست رو برای کسانی که هنوز رمزِ وای‌فای‌شون ضعیفه، فوروارد کنید!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/6682" target="_blank">📅 13:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMLEhXjTHEJL_BnD2TsjD2c3fHQj9sB4_F_0H1pLe99hdYfo09pAxMKEJoGM-d7oS8g9egpu32ySYH4r9aaBrUdbDkoHiBn3RJ2aefpRg4RA-rNKpMdDWWJsrnxEsnpfBvlXnj7Fa8zStzRcue9QyXsrX0IuewjwS672KRllFYtBi6jsPxPxipbWxqHyrB17TFmZNnSSnUQ0yjMk8-Bv2PsZBAU9rofjC0HhYmrpwMEGldo4VTMiH0a9cM8lfG9zmP40n6Mr9ZugL8PAE0hz4cQg6dDDa5rfmF9b3vE-XVNOGUpHaL8dxY0ns5Sp5GiaQ5NsW4p8qjP8VMkMdfePPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/6680" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است. با اجرای این ترفند، می‌توانید نسخه گران‌قیمت Ultimate را به راحتی فعال کنید!
🔥
آموزش قدم‌به‌قدم فعال‌سازی:
1️⃣
ثبت‌نام:
به سایت
gitlab.com
مراجعه کنید و با یک حساب گوگل جدید یا یک ایمیل معمولی اکانت بسازید.
2️⃣
تعیین نقش (مرحله حیاتی):
در بخش تنظیمات و شخصی‌سازی پروفایل، نقش خود را حتماً به عنوان
مدیر سیستم (System Administrator)
انتخاب کنید.
3️⃣
انتخاب نوع کاربری:
زمانی که پرسیده شد چه کسی از این فضا استفاده خواهد کرد، به جای گزینه «فقط من»، حتماً
«تیم من» (My team)
را انتخاب کنید.
4️⃣
تکمیل مشخصات:
کادرهای مربوط به نام شرکت، پروژه و گروه را پر کنید. (اگر با خطای «مسیر گرفته شده است / Path taken» مواجه شدید، کافیست چند عدد تصادفی به انتهای نام گروه خود اضافه کنید).
5️⃣
فعال‌سازی نهایی:
روی گزینه «ادامه به GitLab» کلیک کنید تا لایسنس آزمایشی ۳۰ روزه Ultimate شما فوراً فعال شود.
⚠️
نکته بسیار مهم برای جلوگیری از خطای دسترسی (Permissions):
وقتی وارد داشبورد شدید، به هیچ وجه چت هوش مصنوعی را مستقیماً از صفحه اصلی (عمومی) باز
نکنید
. ابتدا وارد داشبورد خود شوید، روی صفحه گروه یا پروژه‌ای که ایجاد کرده‌اید کلیک کنید و سپس از آنجا روی آیکون چت
GitLab Duo
ضربه بزنید.
در نهایت، از منوی کشویی انتخاب مدل،
Claude Fable 5
را انتخاب کنید و از دستیار برنامه‌نویسی حرفه‌ای خود لذت ببرید!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/ArchiveTell/6679" target="_blank">📅 09:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دریافت 2 دامنه رایگان بدون احراز هویت و شماره و ...
https://youtu.be/1yzxi-U_vVo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/6678" target="_blank">📅 02:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K33kqxmpe3tACNRV0YNtGvyRr6HtYMJa2bB5_L0NZsdh4P_lNPEbUwR4JauabmFXvVAfg7shlG2hKNAzBb1p4--RdyH9asCKqL144GOfmsCN4K2Hpb1wxiLTi9HYrYLLZO07aGROk9k7WJqQV67lecPzVLtP46VJ0wD0ON5PjKUpYXLYYwnGChTdwKC97rvWKdgrDcF1lFjajwKmYWFGCC78EFWXiYoK90rN9zuoa9mJWZrt9uK1lEe6guvAKKBLqdRRdcpJdP8uCc9IaQQNbJIP-sP1ig0LOy0k3_-iXn-Ra_S1_yVwLDKkz3nrFM6gZ_3F_NtBc3G0w2GCxT8MyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعه‌دهندگان چینی GLM ابزار قدرتمند ZCode 3.0 را معرفی کردند
😮
این یک ابزار همه‌کاره برای نوشتن کد و تعامل با عوامل هوش مصنوعی است: همه چیز در یک پنجره جمع شده با امکان کنترل از راه دور از طریق تلگرام.
این سرویس به صورت رایگان در دسترس است.
http://zcode.z.ai/en
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6677" target="_blank">📅 01:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GltccIZVbbhUKhML3MdUT-GVadLFkWkflS3W-xzl4FyHuEQv5R3TO09s7Kj__SXvQo4VzuQmkjv0n535GthyDiYHhxjRHQi1ghCGq6E9xwsbFBFZfCEYpIdNV-mYfHi3YsBNPjvllzdbCafQV54C6r-aZlorG-bBw8XMYxZPzlKfc1X7CB78OUmaXJLlU4-P5yZwHKcWKwd3MMgRKdKdbo-xjgBllz4PIHXfeludw_mpLy0AcZ2F9kRx8CIN73tn32sY46Uw28vUx7gtLK-O1wGgafTZEMIiWo9SJeh9XZj-WSkVysArtJlIOnbVlXbBcijjqQFWXW5jUy3RXy9QCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت Fable 5
🔥
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/6676" target="_blank">📅 23:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=tixVLoWnQHyTS8vd2cA1r3eTbu8Uxxqpl-jhCRiVoH3F0w-3AIEvlZCuMxejD3IaPVWwN3A1_B6jGlgMR8UbfB8KeGkQ8xf0Dey6oJGrjx_tGtb-_4KWM-kGHOEf7z9IdnJYmvthIMZVm8ffm7RAh3G3VP-7vVp8yrPfoXkiVW0DNncR5CkOa5DnISVCI34xA339VfwpRD5dweVHxGxeJjHIVau6fHHM4U-5gzjVc1Ronle3C65UqTgnPGgDa6YsdxWC57l2FshhrJrVYCViNUntI8gpYLi3MLPGdXkA11_Tlis5qL68Pt9C49gblHkw6rGA0bR_sWtZGGV3-oyVVn-Cq8nTOqfmzhFgLUm6KQohZwxumxK6TCZRkHkJWvrGUVonjPZBKDuOEDC78vyMGGZZLJrivqn33gJhJ738KSCno-bSp-Idvy6QufIA7MGLjJUgES7wrUzaviHmqLiHb_kAg1_oNOmTN_49Y3MK_iir2MND3qXqcf-Zs7Ez5Q8U0KDkY2PHYsMhTISrhUmcSMPT8s-OPHwfQC6A2yANCIlFa66lPR8yItuWaDTxZFFna2ZTMuQVqhDLUm8QGbFc8wA9HGVsd4U_5DrMABiZLO9X_gdt0k4g_RYCPi0TiVk4176eaIrXDnZ4AvYYYc07Z0wXq6QBaVvgVYedUn-zh9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb8383feb.mp4?token=tixVLoWnQHyTS8vd2cA1r3eTbu8Uxxqpl-jhCRiVoH3F0w-3AIEvlZCuMxejD3IaPVWwN3A1_B6jGlgMR8UbfB8KeGkQ8xf0Dey6oJGrjx_tGtb-_4KWM-kGHOEf7z9IdnJYmvthIMZVm8ffm7RAh3G3VP-7vVp8yrPfoXkiVW0DNncR5CkOa5DnISVCI34xA339VfwpRD5dweVHxGxeJjHIVau6fHHM4U-5gzjVc1Ronle3C65UqTgnPGgDa6YsdxWC57l2FshhrJrVYCViNUntI8gpYLi3MLPGdXkA11_Tlis5qL68Pt9C49gblHkw6rGA0bR_sWtZGGV3-oyVVn-Cq8nTOqfmzhFgLUm6KQohZwxumxK6TCZRkHkJWvrGUVonjPZBKDuOEDC78vyMGGZZLJrivqn33gJhJ738KSCno-bSp-Idvy6QufIA7MGLjJUgES7wrUzaviHmqLiHb_kAg1_oNOmTN_49Y3MK_iir2MND3qXqcf-Zs7Ez5Q8U0KDkY2PHYsMhTISrhUmcSMPT8s-OPHwfQC6A2yANCIlFa66lPR8yItuWaDTxZFFna2ZTMuQVqhDLUm8QGbFc8wA9HGVsd4U_5DrMABiZLO9X_gdt0k4g_RYCPi0TiVk4176eaIrXDnZ4AvYYYc07Z0wXq6QBaVvgVYedUn-zh9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
واقع‌گرایی GTA 6 شگفت‌انگیز است: یک علاقه‌مند صحنه‌هایی از تریلر رسمی بازی را در دنیای واقعی بازسازی کرد.
بعضی از صحنه‌ها عملاً از نسخه‌های اصلی بازی قابل تشخیص نیستند
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/6674" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOqbPH960hkGRoj_I1lyMSXRnJbn8sLVL1gzVChHjUKkKBth3xuwUithyAyCwx6uRQnho-KPwVaF334LNotPO0Ha9wZiMZbN_o6JL1cYJpTqHgI2TXDJUbHGd7FOysZ9kgai61MyWz6DYMfE1oSm4VtEote2-AY2rFrJpQn8TMVHRN96leG8mSNB9lM_akDquXv-_au8v63DCD-0VvLxE9Gv46-Sa4w4m1lW5tMuIMPxspTWEIJt7mCP0tUNLmn4U4TYN9oIRkBtDiNDMr5hVNrGNgs248G3ESTQhrxVa3Qa9XplU9g36mhvThB8Ps9NoWZ1WrO--UjZut8_9tyk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون هوش مصنوعی مهارت خودآموزی (self-learning) را به دست می‌آورد — عامل یک راه‌حل پیدا شده را به خاطر می‌سپارد تا در هر جلسه جدید دوباره آن را جستجو نکند.
🧠
وقتی هوش مصنوعی با یک مسئله مواجه می‌شود، این روش را ثبت می‌کند و علامت می‌زند که دقیقاً چه چیزی کار کرده است. دفعه بعد سیستم مسیر اثبات شده را دنبال می‌کند، به جای اینکه دوباره گزینه‌های ناکارآمد را بررسی کند.
https://github.com/Kulaxyz/self-learning-skills
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6673" target="_blank">📅 18:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6672">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeIAC2uHVseuHJ_cg_MwLudauJmcW4ttJiPFb9SDW00I_3qX02vyl_AnUWooT74_tEglQOvexxWSxb1E14KiDrvBUx8YCAlLiphLf0w5H6mKprXj--PtVzpRFWxOw9RUwxPf6IDq6BagjcJy12dHt1_O3y_3lsOsqWGLOPpsXX5n-ZSgxepL0uhrMYVaOcN9M54NsI2-4jKsj54lRkx0x7JABXcPoQK9qyWrnz_9uT9VXn3yyinYjcvOKxOoNj0O3yQstP0N7z3rI0WlSoQp9R8mTW3BLdqPup_2D1S--6_xiajDpkRRZBxJNQplkNlW9oF9g7pmQKiSgfBgMp3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">RevPDF
ویرایشگر PDF سریع، بومی و متمرکز بر حفظ حریم خصوصی به صورت آفلاین است.
این برنامه امکان ویرایش متن و تصاویر را مستقیماً در سند PDF فراهم می‌کند و همچنین عملیات‌هایی مانند ادغام، تقسیم، فشرده‌سازی و تبدیل فایل‌ها را انجام می‌دهد.
تمامی عملکردها به صورت محلی روی دستگاه اجرا می‌شوند و حریم خصوصی کامل داده‌ها را بدون نیاز به اتصال به اینترنت تضمین می‌کنند.
https://github.com/Pawandeep-prog/revpdf-release
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6672" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6671">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=bZ4yXAMCUDUudDaMTdgesrBEa892JQFOGc02uspJ7itdKY-gdUmydgEpNf9egpy0Yd8NEinUGc4kBbaX18p0fytGSiE2YX8wCH0Mgjl1nGw2fa_EqWyINTVVfMvEtbfzIIOnWBNRIplvMrjGwXuGZnBQngF3dwJoJ8QpmB0Vzi95iw0-mdU9C7COJC5MEVQFQr4lsj_l5uoKy8V-ZWfRjda465o0WmYQ88dd8xmd2JpeImXYWrE8CBjN8K3NsLEKKfeff8zzFXRW_I-VZwdIA8Lhh744uGXUkZCjRVQWf37z_6IXSOJNeRWK4q8dF0nsrHwX522UODnrkhPX8scFKIpjrGaKpvk4Jtgj22j-dmjvNHe4JYJvb-9dZ7htYy0opp00RJQjMX0NQdRNd7HMkQhZAKhnpLhvrFDunyjLuQg-FkBTkp7hiJgiAZIRHZ6xElHPJvDAGta9eJpC8QPM1PJQF8usDLNFfKTk-izlAo0b32cBIvG_zyadPdf4yxJGBtuv7shCqRZVjAl0XuysXNmRileUcT7Jybrhaf4Ak5GqPTFa1TTOL9YnDY7sMc-nJbWz3rNh_nKMGl_zB34I6Gja4lsxtqnZmh7Of___M0JA539DRna0n0_Iw03yJD3oxeBODzTy2dvOxtGHGXkKYrzwxjv5KlBid8flu2mY79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1d8b6548.mp4?token=bZ4yXAMCUDUudDaMTdgesrBEa892JQFOGc02uspJ7itdKY-gdUmydgEpNf9egpy0Yd8NEinUGc4kBbaX18p0fytGSiE2YX8wCH0Mgjl1nGw2fa_EqWyINTVVfMvEtbfzIIOnWBNRIplvMrjGwXuGZnBQngF3dwJoJ8QpmB0Vzi95iw0-mdU9C7COJC5MEVQFQr4lsj_l5uoKy8V-ZWfRjda465o0WmYQ88dd8xmd2JpeImXYWrE8CBjN8K3NsLEKKfeff8zzFXRW_I-VZwdIA8Lhh744uGXUkZCjRVQWf37z_6IXSOJNeRWK4q8dF0nsrHwX522UODnrkhPX8scFKIpjrGaKpvk4Jtgj22j-dmjvNHe4JYJvb-9dZ7htYy0opp00RJQjMX0NQdRNd7HMkQhZAKhnpLhvrFDunyjLuQg-FkBTkp7hiJgiAZIRHZ6xElHPJvDAGta9eJpC8QPM1PJQF8usDLNFfKTk-izlAo0b32cBIvG_zyadPdf4yxJGBtuv7shCqRZVjAl0XuysXNmRileUcT7Jybrhaf4Ak5GqPTFa1TTOL9YnDY7sMc-nJbWz3rNh_nKMGl_zB34I6Gja4lsxtqnZmh7Of___M0JA539DRna0n0_Iw03yJD3oxeBODzTy2dvOxtGHGXkKYrzwxjv5KlBid8flu2mY79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
«اودیسه» نولان - تریلر نهایی. این فیلم یکی از بزرگترین آثار چند سال اخیر خواهد بود.
با بازی ستارگان: مت دیمون، تام هالند، ان هتاوی، رابرت پتینسون، لوپیتا نیونگو، زندایا و شارلیز ترون.
اکران: 17 جولای.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6671" target="_blank">📅 18:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUZm-_LuQs9P9RU6yz_-AMNxhrO3vI7i5MBvYxfC8l_G4xYZ-mu_TKKEp59aC7rbSmQQdwfJUOLY5FrARVNrH1Z-RlAo4RHVACbjLUd4Zhrtq1yOtMgkbnersDCNsU1UXMZKvOnf9AekQEZw-bm0iZbeLP-A-fFrvups7Qgz3eteim5tip9Agm84b1Wl3cG5ndZVCLXp7zY7j46XFGqtGAGzB1K8uMzSepv4IZzdlek-8IYOIwCIc6QpfOMG57wTx1CDluNK9fw3sK1tNfc_19BJ2xwI9evmn4icl1gKqPOPuzlVTsBoKj5vgWqFwxQwIQQamnZNnUayUwUBuJ0tmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض چند ثانیه هر نوع کپچا را در سایت‌ها و منابع دیگر رد می‌کنیم
• به سرعت بیش از ۳۰ نوع کپچا را حل می‌کند، رفتار انسان را تقلید می‌کند تا هر محدودیتی را دور بزند.
• با چند کلیک روی کامپیوتر نصب می‌شود، نیازی به ثبت‌نام و نصب نرم‌افزار اضافی نیست.
• فوری و به صورت محلی کار می‌کند.
https://github.com/clawdbrunner/captcha-solver
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6670" target="_blank">📅 18:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268d269709.mp4?token=e6vK_IphqerOxZYwLSusKdDOPHvQTRLpdFRkNDzygws5ctaLHMFtexQ3BBWbZkT0zpLaNWsogbrhgZBrTaUlrHQdVMpG_99BKBxi4IiXRJ0H3xWQt_KGHd8Htgy2lLpCAj7GOqFhN4mybGuTBqOAdd7f57o2mRgoS6TgojwKxEA43w6rgbcyq4kJEjtI2PPj6puhEm9OnPlqExBQqWCLDXkRlFPqvg38tIMSy2K4aBCfq8KkILciQdvSIN4FMHxeVModVz4qQTJPHYBkAjof5uwlnJNWwG7kwY6UQ9H-1n5TwRzjSa-6n1jQMBJT6xbcnuDtfNlCMG4eZ7DeY9yUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268d269709.mp4?token=e6vK_IphqerOxZYwLSusKdDOPHvQTRLpdFRkNDzygws5ctaLHMFtexQ3BBWbZkT0zpLaNWsogbrhgZBrTaUlrHQdVMpG_99BKBxi4IiXRJ0H3xWQt_KGHd8Htgy2lLpCAj7GOqFhN4mybGuTBqOAdd7f57o2mRgoS6TgojwKxEA43w6rgbcyq4kJEjtI2PPj6puhEm9OnPlqExBQqWCLDXkRlFPqvg38tIMSy2K4aBCfq8KkILciQdvSIN4FMHxeVModVz4qQTJPHYBkAjof5uwlnJNWwG7kwY6UQ9H-1n5TwRzjSa-6n1jQMBJT6xbcnuDtfNlCMG4eZ7DeY9yUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شبکه عصبی Gamma به ChatGPT اضافه شد — حالا می‌توانید پرزنتیشن‌های زیبا را مستقیماً در چت بسازید.
ابزار هوش مصنوعی محبوبی که صدها هزار نفر در سراسر جهان از آن استفاده می‌کنند، در ChatGPT ادغام شده است. حالا کافی است ایده خود را توصیف کنید یا متن را وارد کنید، شبکه عصبی آن را به یک پرزنتیشن آماده با اسلایدهای طراحی شده تبدیل می‌کند.
می‌توانید تا ۱۰ اسلاید را به صورت رایگان تولید کنید.
🔗
لینک
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6669" target="_blank">📅 17:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY84lnIl2ymBD_VMRR3ruHZekA45DDqOTA6UW2hU0gRSqhBXF-ccuW0-usu9U61kPcdvqVtHQDR9ST0vGLV38FidJEQ5RL9dWqsJZ0uKA3gpUOX_rf0HM6JHTpqEs0dKGs6MAdGee9Kg-N9xB0LZzsiu6anEuoPXyA79KVq8fpEgMXIuMtubh8uZ8ZTkkrDDrjrCisb30w4ynhuD3ZEhvqH_wOLhBkOxbXzpTAWKb_RCl6ATaBQwNOSUNbjWQkNCfMvf63MPXb8gUN_daAa20dOFD4qXaXgaR7I_OgR5r26j1yJhxSZTpOmOTmJUVLF_7SR8Fp4JUbX-LEHBTzZcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دیسک‌های بازی پلی‌استیشن سال ۲۰۲۸ ناپدید خواهند شد
بازی‌های جدید فقط به صورت دیجیتال منتشر خواهند شد. همچنین سونی فروشگاه PS Store برای PS3 و PS Vita را خواهد بست.
یک عصر به پایان رسید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6667" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
معرفی Superfile؛ فایل منیجر مدرن و فوق‌سریع برای محیط ترمینال!
📁
✨
اگر از طرفداران محیط خط فرمان (ترمینال) هستید و به یک مدیر فایل قدرتمند، زیبا و سریع نیاز دارید، ابزار
Superfile
دقیقاً برای شما ساخته شده است. این ابزار با رابط کاربری بصری (Intuitive) و کنترل آسان از طریق کلیدهای میانبر، تجربه مدیریت فایل‌ها در ترمینال را به سطح کاملاً جدیدی می‌برد.
🔥
ویژگی‌ها و امکانات برجسته این ابزار:
1️⃣
پشتیبانی کراس‌پلتفرم (Cross-platform):
اجرای بی‌نقص روی تمامی سیستم‌عامل‌های دسکتاپ از جمله لینوکس، ویندوز و macOS.
2️⃣
شخصی‌سازی بی‌نهایت:
دارای سیستم پیشرفته برای نصب پلاگین‌ها و تم‌های متنوع جهت تغییر ظاهر و افزودن قابلیت‌های جدید به محیط برنامه.
3️⃣
نصب سریع و بی‌دردسر:
قابلیت نصب تنها با یک دستور ساده از طریق پکیج‌منیجرهای معروف مانند curl، winget، scoop یا Homebrew.
4️⃣
محبوبیت و پایداری بالا:
توسعه‌یافته با زبان قدرتمند
Go
که توانسته بیش از ۱۷.۷ هزار ستاره (Star) در گیت‌هاب به دست آورد و نشان‌دهنده استقبال بی‌نظیر توسعه‌دهندگان از آن است.
https://github.com/yorukot/superfile</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6665" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk-P1_VcndY8skzhYIvZCxT9ls1BSvSbB7zPyYHCqM4rcaOvnuxvY4hEq1a9Jz8zhBIu0A5-PFyALMF0Zd3iqAv6U4eQ1FMjKZbcmwybnG3Ud0wLxzHgV-nHZR4n_W1e3qmQotza7QvzYFu6Fv_3NhxUZw2EJ_awlDePc7lfgz_vdhtjnmevmyUMtXs1LPcyWjPclLTRLsQGQlVGCuw8rLvGbKtimfwdF0Q58Wmpjj8lKlncUBoifMUMSwZAGbjuid5OY0SvxlvB1JduMY6iKEMDxmDXbdNE66sTSlzLKphI3Mdp358ZsTHNoT3ToqROtfPW546ATkOnZ1frMz3g1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اروین یالوم خودکشی کرده ظاهرا
😐
اروین یالوم نویسنده و تئوریسین روان درمانی اگزیستانسیال</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6664" target="_blank">📅 15:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flfmz6wGUdHqtZK0sFeSk3yLP76qBSlieYtYyS8Kclvbz3YER4jg4UgIr3rkdN98JW5MgcvAn_Tbwk1vsu9zUJsMLcG0imCFnNgLzjOxIJjvUsvE08a88l1BiF8BzFrsZDofn77b2FPm7sNAFSNvMH_Hnk3ewjWq3zb9DK-fXZjIE9X8AIsohBJsIc9OkLmsw1ZpUHTXQteOwowedMmfMN_N4jLAj9-yHLECC01zU0fCTb7mVNmGyg72OhYyrM7No1FritkFbupbObVeDgBpZT6lj2mfle1eFQAKTGSV0kjJi7tleMrots7-OIb54VaWsEwgeLQHKv-_EgEILb77Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر سرویسی راه‌اندازی کرده است که پروژه را از نظر سئو، جستجوی هوش مصنوعی، احراز هویت ربات وب، MCP و پارامترهای دیگر بررسی می‌کند.
سپس به سایت امتیازی از ۰ تا ۱۰۰ داده می‌شود و یک پرامپت با اصلاحات ارائه می‌شود که می‌توان آن را به شبکه عصبی داد و سایت را بهبود داد تا امتیاز خود را افزایش دهد.
https://isitagentready.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/6663" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8WDNeGPkiiariuaglBm-Hw8ha2h_AC8NUEc6tl5xyQ7-urXIhwWlkwJFK5rJmm2Xk13TjhXrdb0s8kymDlJZ0g_xfru4pGAEc6puMxvEwxS4pfbva6a6TU6ZS67dlmp93UnbNKaXh7-JKO0nnKZILGoZEgs80BCAfutF9HAWLY4ROVtsfACLEcVPX_9UeJw6FopGxAErgxo_G1KGpwppMpzFMOX788DT18nEUJ23pJ8-dtNKD7q_hNGFmVMfDQde6KToCjPbMlDRYgBTN7oAvy6kIcq0UVBE8aI5JYH_ekEy8Q4goozxWCsCbagtI_kIhiVn35hPtbFigj_HXtVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع مفید برای توسعه‌دهندگان: در گیت‌هاب یک فهرست عظیم از APIهای رایگان برای همه موارد زندگی جمع‌آوری شده است.
🌐
بیش از ۵۰ دسته‌بندی موجود است: از آب و هوا، ارزهای دیجیتال و مالی گرفته تا یادگیری ماشین، نقشه‌ها، موسیقی، اخبار، انیمه و میم‌های بامزه با حیوانات.
🐱
💻
https://github.com/public-apis/public-apis
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6662" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XlX_3LN5d9BvybRZJtehFrxokQNp28JuIGi8Dfd8-O2YuAu_Ks0IqCMwIPk_vFmzRzX6Ow0WQj4BByye_AwyvML1vh0d2Hi-25YBCp8zuhs-ZwQoX-qwdR6ZjjpWQHaGsJuMJBrkmHojxsLaVHSTxzUVvyH0Zbr24huAwjqix8lj4Pg6ODvUL36CfjKLUuzxhMx5phL7qj1LmRi9i_eFK27o3d23TtrNYxfxC94V3RxmxEZz4qdl8yWcjVDj_LX7rhznRCokIonv_3BEKaZDWFgZKgijj7vu-zQQnWOv-M2W9qvierBPdZv0xYCFDOrV8bDho2TcQw2OV3Kl9NY_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjuKu1GTQyU3OpsgUpBJr5FXeTSCAEnWfsOoHTrB9__9IUTIqn_8_kuYMI6_0p7Tabdb0RwQzhBi4bLH_0fr3X5tvUqjC6S-D_r1LsblsR6Kl0o8nrYch-qco8VuYuXGx3Z_jfSwlOtyZH7hhT4qWByKWUD2SbY24N7xi9W3dfZtTdSVN71cIAM4oqiBG-76UGgE6dok4MriNlhR3Wk2mslPqQjSmIfIUhMNcPjOJpn4s09iKv7jUZOQ65he8O0Pj3jgYjW4PJEcTMWuwkzW2Iiz_F_jAvaES1HGgkhIDwENdLtWYF-zjHddgKgp3TvC_0ToUDWZ0dMkhayvU1SA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l01UJlQ6w6NE2bZSpmg9KGsA0H_bssb_qrFY4pdlIwc_67W9rPvRFxjCYh07oKoZyLn9Ugl5xhRY9L8sbXcZb-4241jI11ZFKNlHF6XW9oG-sH4EadXNw18wzI5DF1Z1t0nHQN82gTYomlThX4JuWx0W1B2Kw4rvM5awzjmQO_D6qppq9hoJjUr1NKgt_ulKB-M3dpxjhtNswHkeM_ECJKeCIiwUVU7gFvKa5U1yiBYcJswrdRaHg3_lmUs6S75Ea_1X_UVnLWBJBoPL_SQWY-XFgJr8FnY7-M-VDsGUAWTaLkICJFqShzFNK-FaUNNpyg1vBQ4owsC5V7frth9mPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAFNd3jhxNvxU__Xhhg_1tdPMbLW6LjQw77n3dWKW09kAZk30P_iFXOf1gK8EYuq5AmmukAd0HiHr9A-Y2omyEVPk8oXMF9SBFLBv7b1Fbr2BVWBT-VO6oxhcuqt2tJabW87Zfn6TmR1RpgKblqG1LtknYqxNqBb8K1rCIiHlWui2XRDI0iGUwueBpF0bMmf1_yaWy-VWfCAyD1K83_2YHXv3zWARG3_pxderIu3lIKud80wZapJs-Bc4MUO6xlAgY31IRBC8u6GPaE6sDpJe4CgR1F4fENMN1A0B3ecb403-bSAKgVmn0MU8t_UMJ-IKILhw2XZt7_aXYtbPYvLaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">PlayTorrio
مگاتورنتی که همه چیز را دانلود می‌کند:  بازی‌ها، موسیقی، فیلم‌ها، کتاب‌ها و هر نوع فایل.
https://playtorrio.pages.dev/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6658" target="_blank">📅 09:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my53F18hmJQZKrHJd5z80Rzx55w-adu-6WeGcHr5zIukALTd6jrx-wXG7nrq7aRlrLZRInB9de6Nzdyv5u_c_TU3nV_-y3tzEgyjFflRsPP_dIuJYQohmmfn29H_kl1FZ59OgAdowwYpHhhU5Udibi43iHti-GRu9uRGa-upyhOdh73bI0AQmcB9o_BUc21z1yKhCGsJVZSVzTgU8i_yaqR-DyBTGuADFXO2UvErd6CVZ3HKISVQzMSPmlwPsZdDwEpZKCxN0z7W3-QegYdIDSPW7W5e1Bgs6Lptvw73xowkGtZpKctXIcQyoB-sjLScDHm9RRS8WL0Xh3PmdzpomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود Mythos و Fable 5 برگشته‌اند! دولت ایالات متحده این دو مدل‌ رو از حالت مسدود خارج کرده است.
امروز Fable 5 برای همه کاربران در دسترس قرار می‌گیرد و تا ۷ جولای می‌توانید تا ۵۰٪ از محدودیت‌های هفتگی خود را روی این مدل استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6657" target="_blank">📅 09:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg8gPUF2YB9HsCbVoLd6lhy3QVdhGVcpxyKesARgaNX0aGtowQ2k63UduxbeiwQlK2g8abNxVp_8i8LTSYNmnRNBbcyRxI4W2PnKYkMll7AWTDQT_yjLy_TLIJmdaP1VoCttu4GpXr7qikqZ6F9iFd-mbVVHIkFAB9eP4c53KZ2_7qR0ZpzouDoT2XDXCh15EM54rmh2YX9SBXNSFFfznvs93HidY9aj7YZTkkT3Trs_RTv3tDkrho5PQbhf9U8s755SnpFVjVTLDRgg3apzmk_n3iGUkaLGdv1k8vOLIKcNQ8NlvFvLkKdtE8hWHKuQKiwl-_hOvNEthpVOwrwpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلود اوپوس بدون سانسور منتشر شد!
توسعه‌دهندگان Qwen 3.5 را با داده‌ها و استدلال‌های Opus 4.6 آموزش دادند و یک نابغه شرور واقعی ساختند.
• محدودیت سوالات فقط تخیل شماست.
• می‌توانید هر چیزی، حتی ترسناک‌ترین‌ها را درخواست کنید، اما مسئولیت آن با خودتان است!
• به صورت محلی اجرا می‌شود و بسیار سبک است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6656" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ArchiveTel
pinned «
🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6655" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">درود دوستان AssA هستم
بابت خرابی ربات
@REN_WZA_BOT
دیروز معذرت می‌خوام
حقیقتا به خاطر شرایط نتونستم سرور تهیه کنم و ربات روی کلودفلر ران شده
فکرش رو نمی‌کردم که قراره انقدر استقبال بشه که سقفش به نصف روز نکشیده پر شه
😄
خبر خوب اینه که یه ربات بک اپ گذاشتم برای وقتی که سقف اولی پر شد بتونید کار هاتون رو راحت روی ربات دوم انجام بدین
جای نگرانی هم نیست تمام اطلاعات دیپلوی ها و کاربر ها انتقال داده میشن پس عملا هیچ فرقی برای شما نداره
مورد دیگه این هستش که خیلی از دوستان بدون اینکه پنل قبلی شون از کار افتاده باشه یا مشکلی پیش اومده باشه ده تا ده تا میسازن که واقعا عجیبه
🤔
خلاصه که دیگه قرار نیست به همچین مشکلی بر بخورید
و نکته سوم هم اینکه ربات دوم کمی با عجله ساخته شد اما از تست های خودم سالم بیرون اومد
اگر باگی یا مشکلی دیدین با تگ کردن آیدی ام توی چت بهم بگین
@Assa_7788
(بابت مشغله های کاری و پی وی شلوغ به احتمال زیاد پاسخ ندم بهتون پس ممنون میشم پیامتون رو با تگ کردن آیدی ام توی گروه بنویسین)
و عذر بنده رو برای طولانی شدن پیام بپذیرید
🌚
❤️</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6654" target="_blank">📅 05:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الیوم اکملت لکم دینکم
🚶‍♂️‍➡️
😂
(حس تکمیل پروژه خوبه)</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6653" target="_blank">📅 23:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6652" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji5QntS8HpvZXrcqh3ZclDhjoEpYaDliwkgW5GNlVDm_EOrBmbdBvEHALuS3ffMtzVaFtqbma7P6i4_BPqF-FmB-CH6mbzEFCCXN2rDOdaSGxKk-u732o-72y9Jg3JV-bcQscmbuY5g20uRN_5S8SjeazdPojqmAb8noM9r31OJofhm0IPnjG1eAv0671ziIJAA7c4p4809_nMLMRfVfwEsguuEzO_R0jO2tXtWGjdcfWrXfjOOoZ8oCfyHjdAj3gSFSaUmIPLsi8CaeFvqrytvUs8fHvi6uuAhzsRFiCth6Q_G-awmuGCFC0we7cynMBSTiHhTFQukoNjroVBMYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=JnpHyg-Vc40</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6651" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFMail@ArchiveTell.zip</div>
  <div class="tg-doc-extra">471.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6650" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام! تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6649" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔥
آموزش ساخت سیستم ایمیل موقت نامحدود و اختصاصی (روی کلودفلر - بدون نیاز به سرور)
🔥
رفقا سلام!
تا حالا شده بخواید تو سایت‌های مختلف ثبت‌نام کنید ولی نخواید ایمیل اصلی‌تون پر از اسپم بشه؟ سایت‌های ایمیل موقت (مثل Temp-Mail) هم که دیگه تو اکثر سرویس‌ها بلاک شدن.
تو این آموزش یک ترفند فوق‌العاده رو پیاده کردیم: ساخت یک سرویس ایمیل موقت اختصاصی روی دامنه شخصی خودتون با استفاده از زیرساخت رایگان کلودفلر!
🚀
این سیستم کاملاً ضدِ بلاک هست و می‌تونید تا بی‌نهایت آدرس ایمیل فیک بسازید و همون لحظه پیام‌هاش رو دریافت کنید.
🎥
آموزش ویدیویی و قدم‌به‌قدم (از صفر تا صد) رو تو یوتیوب آپلود کردم. حتماً ببینید:
🔗
[لینک ویدیوی یوتیوب ]
👇
خلاصه مراحل و کدهای مورد نیاز برای رفقایی که ویدیو رو دیدن:
۱. مخزن اصلی گیت‌هاب (برای فورک کردن فرانت‌اند)
۲. ساخت دیتابیس (D1) و کش (KV):
یک دیتابیس به اسم
mail_db
و یک فضای KV به اسم
mail_kv
تو کلودفلر بسازید. فایل
schema.sql
(موجود در مخزن بالا) رو تو تب Console دیتابیس اجرا کنید.
۳. متغیرهای طلایی (Environment Variables):
موقع ساخت Worker برای بک‌اند، این متغیرها رو دقیقاً با همین نوع و مقادیر اضافه کنید (راحت کپی کنید):
DOMAINS
(نوع JSON)
👈
["yourdomain.com"]
DEFAULT_DOMAINS
(نوع JSON)
👈
[]
DISABLE_ANONYMOUS_USER_CREATE_EMAIL
(نوع Text)
👈
true
JWT_SECRET
(نوع Text)
👈
یک_رمز_طولانی_و_رندوم_انگلیسی
ADMIN_PASSWORDS
(نوع JSON)
👈
["رمز_ورود_شما"]
ENABLE_USER_CREATE_EMAIL
(نوع Text)
👈
true
USER_ROLES
(نوع JSON)
👈
کد زیر رو کپی کنید:
JSON
[
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "vip"
},
{
"domains": ["yourdomain.com"],
"prefix": "",
"role": "admin"
}
]
🚀
مرحله ۵: آپلود کد بک‌اند و هدایت ایمیل‌ها
۱. در منوی
Runtime
ورکر، تو بخش Compatibility flags، کلمه
nodejs_compat
رو اضافه کنید.
۲. روی
Edit code
کلیک کنید و کدهای فایل
worker.js
پروژه رو کپی و پیست کنید. Deploy رو بزنید.
۳. تو تب
Triggers
، یه ساب‌دامین اختصاصی (Custom Domain) برای بک‌اند اضافه کنید (مثلاً
apimail.yourdomain.com
).
۴. حالا به بخش
Email Routing > Routing rules
تو دامنه‌تون برگردید. اون پایین قسمت
Catch-all address
رو ویرایش کنید، Action رو روی
Send to a Worker
بذارید و ورکر پروژه‌تون رو انتخاب کنید.
6. اتصال ظاهر سایت (فرانت‌اند):
مخزن پروژه را در گیت‌هاب شخصی خود
Fork
کنید.
در کلودفلر به
Workers & Pages > Create > Pages > Connect to Git
بروید و مخزن خود را متصل کنید.
تنظیمات Build (دقیقاً این مقادیر را وارد کنید):
Framework preset:
None
Build command:
npm run build:pages
Build output directory:
dist
Root directory:
frontend
تنظیمات محیطی:
یک Environment Variable به نام
VITE_API_BASE
بسازید و آدرس ورکری که در مرحله اول ساختید را در آن قرار دهید (بدون اسلش آخر).
تنظیم SPA:
در مسیر
Settings > General
، مقدار
Not Found behavior
را روی
single-page-application
تنظیم کنید.
روی
Save and Deploy
کلیک کنید.
ارادت، Bachedev
✌️
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6648" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سورپرایز امشب
اختصاصی
🗿
❤️
از یوتیوب
تقدیم به بچه های گل کانال</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6647" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfyLQrOR_-6C5Q-mmQvQt8OjJM7Yj2XhHJvHLjLUDnoQqDQOeUWF9EhSL8NGgNCl2X9TjlSsbSa7DvHBX7-o54_1KQRLa0zrL4D5-ZH1LUT4dE-l1RxzhBjY0mO0wfasHvYJPivfd6hHB7NLfBM2Z5BJF-5_DjcKy-jyBAqAkEZfkw6_DDCT_ZgpTrxiBHhFZcPb5Q0h7lDVaSZk5sWxhCPV0HvziSW3zHaAc98VxbTiIOE6BZxb4mh_GB4knvgsmOvKJrlObc4QH3lPaflpTh-qN0fXyNCA1jfGZLRWkIr7DPIUBZete1QnggB3NpuR2N4CpvxlS_iyLEklSRHY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude Sonnet 5
منتشر شد!
مدل قدرتمندی برای کارهای روزمره اکنون برای تمام کاربران، حتی کاربران رایگان، در دسترس است.
• از نظر عملکرد بسیار به مدل Opus 4.8 نزدیک شده است.
• به مناسبت انتشار، Anthropic همچنین تمام محدودیت‌های مدل‌ها را حذف کرده است.
https://www.anthropic.com/claude/sonnet
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6646" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kp39eZVtpM6p1WVtPD6fuNg7NnHRkQKF5Xlma80ojnlpcJ1sQAxOaV_uKcBEgQ1spLWmn2U9C8w35rRjVCkhntPorLkeI3TjW7cxDMQkLYzWonTs6wmxpDx6E2cf8O1TwagPvcNeHBehTFRvdXbl5IhejFlol72qk9LEnRpxgfUhCTwUB9_Tddl4L8DRme8xREhXZDfU6e6NNepGWCs6JJ4TseLsuvGVYgOP40ZaLiMoNMJCsh0BP2uiLc0WhVsaVERUwOE5M9vyFBKMrplaTKeuga9IpmLlZoqCqCtVIQoSjQSz6uDf1twXfCq_DEM_2cdm89hFE4qW1O3I-i3SRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSvXgH3DrFceLFuMU0MeGwAjsQIxYST7yU4-HJbVi0bFgPVo-mRc23krj5tuz7sofeSUT2HvEb81QR9tJHwQ9V66wEasy25QjdQqjUdxjZovlGkzOYMoJzRRevwyww-C7JGKtPZWYXaB6I6Rfuw-a0tchshdd3dQJGUADa3qlbNbJ_Dy0vjC0jhpa0BbSwVt-KZHtXsmQQL4NSbp6XfzI-HLcYIaFH0i1WHFn2dri17cCc4LuwUKWQmOZAkZ1vw-6CE2WCFGev9I-RmqzC6PC5QMFr6Jkn-ivTpWUmbPeibGOfyTAQCsnG_GCOYtSgr3heFAMFKx0erXUdoHg32vNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXs72PBbPg8wom6YX82W-Ibg0FDXgee6fFctsmGooVfZXqupoYHLkTsdLFHTcsz-NRmujD37D6ihII686cNfNyrbaUe8FlHfedCMW6W50fCC6o48c_QLkZ7c_3pN5up6gk6Mye0xGBfPyAuMtEl4Qs383IClzEi7KY6_rXKN63IBP-7VpVrl2LcaSKypF63l2eZd2PCJ3IQv7Q6heug4_mpE2yHa5ktrTcQY4r6r_HDEPqPfNU1KGoUGGOS_PCDt86XL45QkZ56fydeQROXRLaSJTmtxvRvKlIwi3wftkXZlX2J8KQeoEcduFSNAF3YuaIzik0icHu_ye7mzEQQW8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=B3b6FXHywOU6wEYswSnUhGi-IMxaoPe_QFVSIyO-RKNytejdj4B6k4yZGWfD6XrgBtzqnwjZSc_iy3D7V7KC9jTiLSiuE-lhJBsaa8WSkyV4z37pQ_qY-hvS_Nb8Mqzp2tUo2oR_0_CqSyeAcKLgteOYNt8rrV78XaVEDlso8mPBqUduaNxTpNytlPlxDFSI9Shch6bg1XiEraBeig9gDGQDNKr9HFJebngwgUAymvCFrmqJuy9pKFFz0OipZf3ubwrdkV8zRjWv6ORtrq1qQIQxcpulJHqIQBW0Qj0NHurelGjiARmV820fkwPeT0wkVSVVrBjgxPUIdD-qpXyPWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de073ef68.mp4?token=B3b6FXHywOU6wEYswSnUhGi-IMxaoPe_QFVSIyO-RKNytejdj4B6k4yZGWfD6XrgBtzqnwjZSc_iy3D7V7KC9jTiLSiuE-lhJBsaa8WSkyV4z37pQ_qY-hvS_Nb8Mqzp2tUo2oR_0_CqSyeAcKLgteOYNt8rrV78XaVEDlso8mPBqUduaNxTpNytlPlxDFSI9Shch6bg1XiEraBeig9gDGQDNKr9HFJebngwgUAymvCFrmqJuy9pKFFz0OipZf3ubwrdkV8zRjWv6ORtrq1qQIQxcpulJHqIQBW0Qj0NHurelGjiARmV820fkwPeT0wkVSVVrBjgxPUIdD-qpXyPWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
تولید محتوا ارزان‌تر می‌شود — گوگل مدل‌های Nano Banana 2 Lite و Omni Flash را معرفی کرد، نسخه‌های سبک‌تر از مدل‌های محبوب خود.
نکات مهم:
؛Nano Banana 2 Lite تصاویر را تقریباً در ۴ ثانیه ایجاد می‌کند و هزینه آن حدود ۰.۰۳۴ دلار برای هر ۱۰۰۰ توکن است.
با وجود قیمت پایین‌تر، مدل کارایی خوبی در زمینه متن دارد، متن را به درستی پردازش می‌کند و نتیجه‌ای با کیفیت و بدون آثار قابل توجه ارائه می‌دهد.
؛Omni Flash مسئول ایجاد و ویرایش ویدئو است. هزینه تولید هر ثانیه حدود ۰.۱۰ دلار است.
از نظر هزینه، Omni Flash در سطح Veo 3.1 Fast قرار دارد، اما کیفیت بصری بسیار قابل قبول است.
ویژگی اصلی — می‌توان مدل‌ها را با هم استفاده کرد: ابتدا تصویر را سریع با Nano Banana 2 Lite ایجاد می‌کنیم و سپس آن را به ویدئو با Omni Flash تبدیل می‌کنیم.
https://deepmind.google/models/gemini-image/flash-lite/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6642" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE7v1FLGgZ-yF9njWlDT6kKtrv6i8Bgbx4H3792JNsBEZDB2oS0uMtgkL53yg0FBUE0CR_4dqMsdktmKgkv-5Jm9RwXWDtUMp7VqW9A9ayiBDI4s2O94PWY3ACC751cYigRm6O3x2diKTI6kdZMChjL0B7kPiiCvxO3JR1xF5DqA3G5QflTq6n23pcdOv4Axgq_TfuI32K6MxTPsLonX0NbWNzFGfOexuw33pzIwEmktyyTnhwmeRwJXcLwXoRstUEb29ClAJwcVSq8h3tsA5FZqLP8udcugdNSoxC5qer1eTtE9PrwsoKPhefhM0iPtjtUmoj5n_91YkN9qtoZXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی Opus 4.7
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
http://zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6641" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=O6qC6hbH7ZqtjshHNzYzbJve6ySpWQXYcXlSP9XFmOEONCdKyG80XxwS03_8cnK1QZU6u4pXfwkprlQo8hnZ5rMBiRfnbFDUaupkKIVpFxhekwpJ4MMS5zriyrU6KBlzDwTckp3gEhkknk8ZAvLbuCp2Et2pXRQ_9ZvuhUAAC6K8VRJJUlBMs0WZzcl2VAkSHs2DhGIxAS0vFa8xOJojhxs6dJMYh12j4GzHdbvYk2Od63TBNtd-E_F0abVLjyeCl53ai3zpfDiDenKkFxr5PMW2jqadfVGQioCpFGbxz5WZh5Hv48_vkWYQIKtS5KQuLz42oGdtO9gLiACTA51L8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d39bc32d0.mp4?token=O6qC6hbH7ZqtjshHNzYzbJve6ySpWQXYcXlSP9XFmOEONCdKyG80XxwS03_8cnK1QZU6u4pXfwkprlQo8hnZ5rMBiRfnbFDUaupkKIVpFxhekwpJ4MMS5zriyrU6KBlzDwTckp3gEhkknk8ZAvLbuCp2Et2pXRQ_9ZvuhUAAC6K8VRJJUlBMs0WZzcl2VAkSHs2DhGIxAS0vFa8xOJojhxs6dJMYh12j4GzHdbvYk2Od63TBNtd-E_F0abVLjyeCl53ai3zpfDiDenKkFxr5PMW2jqadfVGQioCpFGbxz5WZh5Hv48_vkWYQIKtS5KQuLz42oGdtO9gLiACTA51L8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا همین‌طور در سال ۲۰۲۷ رم (RAM) خواهیم خرید — یک پروژه با جاسوسان هوش مصنوعی پیدا کردیم که برای شما اینترنت را زیر نظر خواهند داشت
😋
ایده به این صورت است: شما سایت‌ها یا جستجوهای مورد نظر در گوگل را مشخص می‌کنید و «جاسوس‌ها» در فواصل زمانی مشخص اطلاعات را رصد کرده و گزارش را به ایمیل شما ارسال می‌کنند.
https://github.com/firecrawl/open-scouts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6640" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLm7wG-2hzes3AnHKLTKgN_gZVFCR_qFOXAvS8Mh1VLxOdZZNOIxLyZu9TIg4I97oj_ZXhI1uQFdID1wEIbkP1s7evZvbn0SQSChugu-FjNmTxcKCkRdsyQpmJ4QsAlh26gdqUWAUqfIYpzNArzKYRoQU3bsxNbOPg3uXpMNZ0PdKWOUkHR5W0r1tAa4zuHUuyq2-cJ29G7pBezyV_V9VKXpjKskpNdtO9feyxQLyx4-p_5OTNqcXZVo0q_9eEZicminVkyJRRFuVWaZeAhSQw-bWsXrXc37FWD6ejL3MQXCyHWwmxIKw6S3Wf3Acm_8xxEZqP_WYsps9YVa_kM_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DocumindAI
راهکاری برای تحلیل اسناد PDF است.
این ابزار قادر است حجم زیادی از اطلاعات در فایل‌های PDF را تحلیل کند، داده‌های کلیدی را استخراج کرده و رابط کاربری منحصر به فردی برای تعامل با خود سند ارائه دهد. این امکان را فراهم می‌کند تا به صورت تعاملی و مؤثر در سند حرکت کرده، اطلاعات موجود در PDF را درک و استفاده کنید.
https://www.documind.chat/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6639" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQqWrVQbvxM53mmHJ3rDZBNfpV_RG_tefkY0YF-Ho-hv83Ewr_dQIupWDpnhT2zJAZBZ2ffIJPnvdSxmPkYm_lrgdUVeagxcP7e0fl9hwu4qERYbf1v1N5rRhH211M5lv4vSqfF8nvWPw6ZPzHMp_RKuXygpgdmuSJXdI_amsAfwfW5OyxmV71XfkQLWzoucSw-YcTQF6Ldulfzx-JumYhqa395K2TiaO3-2O4V8jYQZeVG2yTB0QhHAwUopxUrAaxtkXjprwsxf0IQaRoBag4k7np2lZMQ49E_lQndeFs_pW_UocrnhzoPmg7HRLeSkNYRg8q3tkp-ckCDqE7vBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
نورون‌ها بالاخره دیگر هیچ چیز را فراموش نمی‌کنند — OpenHuman حالت Super Context را دریافت کرده است که بین جلسات، زمینه را حفظ می‌کند و کار را از جایی که متوقف کرده‌اید ادامه می‌دهد.
🔹
در هر بار باز کردن چت، زمینه را به خاطر می‌سپارد.
🔹
مستندات را مطالعه می‌کند، لاگ‌ها را تحلیل می‌کند، ایمیل‌ها را بررسی می‌کند و می‌تواند آنچه روی صفحه نمایش اتفاق می‌افتد را ببیند.
🔹
به طور مستقل اهداف را تعیین می‌کند.
🔹
به ۱۱۸ برنامه متصل می‌شود.
🔹
با سبک کاری شما سازگار می‌شود و به صرفه‌جویی در توکن‌ها کمک می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6638" target="_blank">📅 20:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozGsrBSBfIJiMqeJp9mF1tkH40BHDDVuVf_PPzKb8QWv7fSCdf7dTrS3zaPkFCt8UQgQaIMfg9-9hGiILHB9_Mb4R5kc2VNg692ZeCh1LpZRH2RvFrZCmtzvtlRpzTAGumtrHQfjDyHwtHiIm8-LeScU2_buF2TN-pUkkz3dwUMU6LBCfa5DtPsyogWAfN_FSQLg7DATeeij1VYOZQEDHdPp0xXzwND4QDKmbINPspmmhmsV0-9BAWCuHiFUYnY403MT5CSJlLBDCiOVdUMXu3tIhY572d6oLqil3Pfbz11pLKiDPnUsL8E3l0I-odK_D-k5hu0Aj3anQzej8s_l4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1gTNAyQI4uRIokgcbcCxMYqUZWsdYLrj6VOyriiOchCRUSyCyyrdzPcAq-hbNheRp7yRhi7hccTusINK29CWda-F0VB_L8AWCpT-_yl9dev8pADT00UO9DkhSbq9_BdmgV2PsJ0ze0RO0qIUkJgoX47wt6KW5GQNHdFC4nGCLGsraJ3V0moPaSTjDcsrWCQbzInAKKDRPiC-bRCm9lKCrWsh4TVKKQD_Dgsn64054WweGc_a79lhvfC6rzco2jKwM86CDH-oSR1H6tI98X20bsvWe5_BLsmeyDxoNTgjvSVy5d6_-0lZGOCGoLfvKOK2fQ16CJlHlQwnGEOSkD6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
گوگل را دور بزنید! ‌NotebookLM⁩ رایگان و لوکال شد
🚫
☁️
‏نسخه متن‌باز و محلی ‌NotebookLM⁩ منتشر شد؛ دقیقاً همان تجربه قدرتمند گوگل، اما روی سخت‌افزار خودتان و بدون ارسال داده به سرورهای خارجی.
💻
🔒
🔹
چت هوشمند: تحلیل عمیق، خلاصه‌سازی و یافتن تناقضات در اسناد
🧠
‏
🔹
ارجاع دقیق: لینک مستقیم به پاراگراف‌های خاص، بدون جستجوی دستی
🔗
‏
🔹
تولید چندرسانه‌ای: ساخت پادکست، نقشه ذهنی و دوره‌های آموزشی از روی ‌PDF⁩ و ویدیو
🎙️
🗺️
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWyM2JHXEiSgtaPx7WqSg44bdF9q8_5WTSb0AA3zalzDUdqng-NPPsN4QLlxmx5sQk12gq4W2Euw5qzackGH929lRAnqbw6MyMHa3B17FMnjW6c9AgwSWTX2e_1H5IZvK2Hvd6ykHgoNhvDDQVlQgKrRCr_uDczCG5s0BpCIDLjPEoAR_FfF44CrWTXwSyVJ514wjsfVvDTf5_Hn6VeexHNkUBmK7Q1EzL5Ee_Wn-3Ll8J5mNlDSAtNPkyvEui2xYPYFe-u9gnKQ-YycVlpFbshaOxvBAQu7BGlZ8wCwrnvm9vJ-ry-T1UEccPhM7ctkpUIDZDC9ZBgV_muDcl5sgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود فایل از اینترنت با ‌Torlink⁩، سریع‌تر از همیشه
🤯
‏این ابزار خط‌فرمانی، جستجوی فایل را برایت خودکار می‌کند تا بدون دردسر به منابع معتبر دسترسی داشته باشی.
‏
✨
قابلیت‌ها:
‏•
🔹
بررسی هوشمند منابع و یافتن فایل‌های سالم
‏•
⚡
نمایش دقیق حجم و تعداد سیدها
‏•
🛠️
دانلود مستقیم از محیط ترمینال
‏•
📦
متن‌باز و بدون نیاز به ثبت‌نام
‏
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=eCWnRLumtqydqFFcWTtxvz6SQTVfIcrtbs61LsmAPF9ehYyJdfa4iG-XjCcb6X4iJKnYdtvF7gexKby9-k5HomWm7zRUmQ357XUDCPwY8GD6efZJlzCJRG5DpU0pZKaAze4Ccy5RH1PO5GMxCAUiVTGZVQ51rreJJOhuR8yL6SSXz9JRHP-k1WrI4EPhAcD2sQMm5Aus0J6jFwnMxlQXZ0HePzJ7zckrhNieGf-Xsmh5RxfYX4MJdXgrHqCoXGiFe_YYy3w2Uvey5EO5zMbjquwPoDxDutu34jmaGFUph47KJ3oBRyIC1mI6_trftXodubI9xPT5h33oVW7qasygJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=eCWnRLumtqydqFFcWTtxvz6SQTVfIcrtbs61LsmAPF9ehYyJdfa4iG-XjCcb6X4iJKnYdtvF7gexKby9-k5HomWm7zRUmQ357XUDCPwY8GD6efZJlzCJRG5DpU0pZKaAze4Ccy5RH1PO5GMxCAUiVTGZVQ51rreJJOhuR8yL6SSXz9JRHP-k1WrI4EPhAcD2sQMm5Aus0J6jFwnMxlQXZ0HePzJ7zckrhNieGf-Xsmh5RxfYX4MJdXgrHqCoXGiFe_YYy3w2Uvey5EO5zMbjquwPoDxDutu34jmaGFUph47KJ3oBRyIC1mI6_trftXodubI9xPT5h33oVW7qasygJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7K6zfJj1g6300qczO4JA2w9-uIBnusOGmxd2zXYg79x0jbe7qQdtrsxBT0yi2gkT-ZRPcUdUXX4CiR6G97mBuFyWPVv0EYXl8nP5ZED6-q4uEpOeLGed62ayuuB0m5uX0psOyuotFnPS_WPoY_lM_jjHbilSxLq1f0COAQXeBUsxCrmnkqjL_ZZ2ISJ97zsW2aih8z181Z2wFloHw0Lg3nHPnFnZ6cVkgOJK6W0aZ27bXI25uBUlEmlzTDnLO58gafAIbjAbQ86W-BBVzwAygdb89dDgvZYGhVessI2dGkGq1KY2qwO40m8Nrgc1pml3TbERGHsu01QI1axt-6D5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
غیرفعال کردن ردیابی در مرورگر — راه‌حل ایده‌آل برای کسانی که از جمع‌آوری گسترده داده‌ها خسته شده‌اند و به دنبال حفظ حریم خصوصی واقعی هستند.
افزونه
Fingerprint Detector
در سه حالت کلیدی کار می‌کند:
🔹
شناسایی — نشان می‌دهد که سایت دقیقاً چه اطلاعاتی را از کاربر استخراج می‌کند.
🔹
شبح — داده‌های واقعی را مخفی می‌کند و آن‌ها را با مقادیر «میانگین» جایگزین می‌کند و دسترسی به canvas، audio و WebGL را مسدود می‌کند.
🔹
جعل — رد دیجیتال شما را به طور کامل با یک رد جعلی تولید شده جایگزین می‌کند.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX4C_QY3xbe86Q42Oi5RaFO5ZMDdzPbQyz9hxL59RV45rex07GHZ2QZvgVW12QEMY2lFUpT4SL9n8aLw4k8ql2ru0DyPInQ7NYk2WYEJgRWOh9H_Ow3oUsSd_d5zBgS2IGVTKr0YspQfRx_Ea4B6xdYYiF6porEdBEE1OW__3PFY-xomyxXR8XMZdwErVifbfb2ohp4RH5WHlkB3_hU4FpyCoTX9A4V4hMRgy6czGiW-d-MuRRQc4uiTHsrR66lr6wJ1nMnnU_07FjR9h7ZPWdayqgdlPeeUOU36fnG_cwVSztNv1HxhGQrSuybreAszPwgQgPzsvy3RTGJFPCiAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🤯
هوش مصنوعی بساز، پول دربیار!
‏فکر می‌کنی ساختن هوش مصنوعی فقط مخصوص نوابغ سیلیکون‌ولی است؟
🤔
اشتباه بزرگی است!
‏تصور کن یک جعبه‌ابزار جادویی داری که از صفر مطلق شروع می‌کنی و تا جایی پیش می‌روی که محصولت را به شرکت‌ها می‌فروشی. این دوره دقیقاً همین مسیر را بدون پیچیدگی‌های خشک دانشگاهی به تو نشان می‌دهد.
🛠️
‏
✨
چرا این دوره خاص است؟
🐍
مبانی:
پایتون و ریاضیات را مثل آب خوردن یاد می‌گیری.
‏
🧠
دانشمند:
مدل‌ها را آموزش می‌دهی و بهینه‌سازی (کوانتیزاسیون) را مسلط می‌شوی.
‏
💼
مهندس:
سرویس‌های واقعی می‌سازی و مشتری پیدا می‌کنی.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
آپدیت جدید بات تلگرام ما منتشر شد!
✨
بخش جدید
Hugging Face
اضافه شد!
از این به بعد می‌تونید خیلی راحت پروژه‌های خودتون رو از طریق تلگرام دیپلوی کنید:
🔹
فقط کافیه در سایت
huggingface.co
ثبت‌نام کنید
🔹
از طریق بات، توکن خودتون رو دریافت کنید
🔹
پروژه به‌صورت خودکار دیپلوی میشه
🚀
⚡
برخلاف خیلی از گزینه‌های دیگه، این بخش فقط از
سرورهای آمریکا
استفاده می‌کنه.
درسته که سرعتش به پای سرویس‌هایی مثل Render نمی‌رسه، اما در عوض:
✅
حجم بسیار بالا
همچنین در بخش
IP تمیز
می‌تونید این IPها رو اضافه کنید:
🇮🇷
Irancel:
52.214.248.106
32.195.122.200
108.133.38.41
🌐
All net:
amazonaws.com
108.133.38.41
34.196.7.222
3.162.112.2
18.185.80.10
23.162.112.25
2.92.189.25
115.185.114.108
18.138.171.15
135.160.210.199
🔥
تجربه دیپلوی راحت‌تر با
@REN_WZA_BOT
💻
توسعه داده شده توسط
AssA
📌
سورس پروژه
⭐
برای حمایت از پروژه، می‌تونید وارد گیت‌هاب بشید و با دادن Star از ادامه توسعه حمایت کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqVVLcQZsQOt4DfzSSNLjs9fEyCq0o3XsHvVcD58LYAs5z15fxwLP-SaN2dLy8WjabMaFa0s04esXUqfqXz506d94eU9AaRjg_L0LeA7rp4V8KSA3QMUgU1gqZ8nNQJNeLIw_PyqHYIN6UaWicIKDKzdfohcs12OBRkfDSdFS_CPykIumg27cL8XfVUHVpFe0C_CNTs_M9Wm6VGBX57bqE416yWvRYS7mdrch-5LPJgNfTtDp8uG53kOL7a_YjYsDHFX_VkVniDc3NK1iUTu7a5_fuRI0YfjDhDpgzOqF7TkjAxYzWeeZiVmtPOWEnzXq4o6f6_GhNcI9P1MMukfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=dIiIf3Newz-mIC-FOstxFDFdzEscxILRqgBDT7FY__YPd6YAtxXpdzAev3n8Zm-2h3ac7UpUWNE1cFZbozAs0uzZUQ6UHhUzl3s7BNe2_3-ZYxduTQuNehpZJUt4lZU87K6FqX1DdDMrlhOsmwdfG6udAcJOuSqMeCKdW25zMd-Bd9mtUtd07ASsnslXe0bfgNEA-fZFtsBzcjFmF4DW4YIiIr0W_liiILC5-EsVG49EfqEviDiFrf6NPtEfBZB2EobTr11evMN4MsRAlXv2b89V2xtjpFkIoAFMsba4ml-Kew4czS5E2HISxA8Ozo8EBeykZ6G2HjzD7AI-PGPTD6KLDXhTUTiODjzAXbNSrPUhqBJuq-EdWVwpBYTRkxr57hc3vP9dGl-OlX0PlqEcohxqEX6oTZpyHs8uxzdmgx-wqs8UKO3V3DdTzsTmW8V8UMf5wfHbkeaHcJMlPWTWn7q1s-DeRlRAVuQy3YaSNeVsVnOLZsphBM5CcX025vDcAbdYt4Gc91T4FYxJBOORwptPmm8TJUIcsxcNyUzBFy7_CEWsrpifB0NEShNNzxGBcfe_66ff6ocnCLQuhYWeHDRyo1U0SMOmH-LDfoTeBZhhSQU3H8R7WQl2TXfxrLNxPPkFVkqajXKhqPze7qTkR7TY-B1RAsxhRM8OcuVJg7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=dIiIf3Newz-mIC-FOstxFDFdzEscxILRqgBDT7FY__YPd6YAtxXpdzAev3n8Zm-2h3ac7UpUWNE1cFZbozAs0uzZUQ6UHhUzl3s7BNe2_3-ZYxduTQuNehpZJUt4lZU87K6FqX1DdDMrlhOsmwdfG6udAcJOuSqMeCKdW25zMd-Bd9mtUtd07ASsnslXe0bfgNEA-fZFtsBzcjFmF4DW4YIiIr0W_liiILC5-EsVG49EfqEviDiFrf6NPtEfBZB2EobTr11evMN4MsRAlXv2b89V2xtjpFkIoAFMsba4ml-Kew4czS5E2HISxA8Ozo8EBeykZ6G2HjzD7AI-PGPTD6KLDXhTUTiODjzAXbNSrPUhqBJuq-EdWVwpBYTRkxr57hc3vP9dGl-OlX0PlqEcohxqEX6oTZpyHs8uxzdmgx-wqs8UKO3V3DdTzsTmW8V8UMf5wfHbkeaHcJMlPWTWn7q1s-DeRlRAVuQy3YaSNeVsVnOLZsphBM5CcX025vDcAbdYt4Gc91T4FYxJBOORwptPmm8TJUIcsxcNyUzBFy7_CEWsrpifB0NEShNNzxGBcfe_66ff6ocnCLQuhYWeHDRyo1U0SMOmH-LDfoTeBZhhSQU3H8R7WQl2TXfxrLNxPPkFVkqajXKhqPze7qTkR7TY-B1RAsxhRM8OcuVJg7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی با چشم‌درد دیجیتال!
👋
👀
تا حالا شده بعد از چند ساعت کار با لپ‌تاپ، چشمانت بسوزد و احساس کنی  به یک لامپ ۱۰۰۰ وات خیره شدی؟
💡
😫
بیایید روراست باشیم: صفحه نمایش‌های امروزی مثل آینه‌های صیقلی هستند که نور را مستقیم به چشم‌هایت پرتاب می‌کنند. اما تصور کن اگر بتوانی یک لایه نامرئی از «کاغذ واقعی» یا «شیشه مات» روی مانیتورت بکشی. جادوی
Paperman
دقیقاً همین است! این ابزار با تغییر بافت پیکسل‌ها، صفحه نمایش را از حالت آزاردهنده به یک سطح نرم و خوانا تبدیل می‌کند، درست مثل ورق زدن یک کتاب قدیمی و دلنشین.
📖
☕
✅
چرا باید همین الان نصبش کنی؟
•
🧊
حذف بازتاب نور:
صفحه مات می‌شود و دیگر نور چراغ سقف روی مانیتورت نمی‌افتد.
•
🎨
تنوع بافت:
از کاغذ کاهی تا E-Ink (مثل کیندل)، هر سلیقه‌ای را پوشش می‌دهد.
•
🎯
هوشمند و انتخابی:
می‌توانی افکت را فقط برای مرورگر فعال کنی و در فتوشاپ یا بازی‌ها خاموشش کنی.
•
🖥️
همه‌کاره:
هم روی ویندوز و هم مک‌او‌اس به زیبایی کار می‌کند.
به نظرت کدام بافت برای کارهای روزمره‌ات مناسب‌تر است؟ کاغذ کاهی یا شیشه مات؟
👇
💬
🔗
دانلود:
Windows
macOS
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
