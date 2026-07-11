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
<img src="https://cdn4.telesco.pe/file/tg0MAjgGs4mlescbrKN-mtaa_NO9Pzt2woI6bSaS3DgCfLVP2bWkmjmyfHVIU39-p81wl-vbLx7UTxLVXlCySS0LIkGzE7ECkNnF9OcJrbH4NQNik2Ur2m-9n2dNBrUG0O4PFVuNHJ8NIe52t-XE1KOgpEpfgKR714Hun1Eck0LSpRIbASQlSd0hXwhHv8B3cGW8-4s7ds3GoNMxsM5mqeVcSQCByd2PA5_V1p1MTlc2DJAHB-PUgdtzrqfp9IC9kSKh7k-oldDz0AD-rMtnRCPxH700GwcI4qa_iBJdvdtdBZWrZbMjdcRLha_ibUMyoF_gNGFVZZPlTG3BBiQ0Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.82K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 19:54:28</div>
<hr>

<div class="tg-post" id="msg-6871">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtl_VLNjDtgUlWMzYXX37Z0GAbJa3yfFAFjLvF5gF4ir9qCf6XOg3V75K1DrKWwKWTX0jzsl4NRPdwDJBciAkcZuHNzGwmfrcK9uje91qLR7Edt5yUgW8sPWCMKnzw8rz4Iv3PnsE4Tub7xDAh5vr0aJaDWoBc3XVxMSLHd06lKTi-FFh4Ay5I5fXWOuOXRqHsyBo4FoyYjpU2ClSL8gF1oDzNYgko4hkqzSelRQQ9H3UHRxLx9ioFgp_nMbmYB_rFoYiqT-GNpBDKWiRe01-5GUJ7nndOj2r4neoK8UwUQ6LwIlraP24r28kHs883gHkSU3bPOWjLqfrEtHwxYrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📚
معرفی ‌CheatReader⁩؛ دستیار مطالعه در محیط کار!
🤫
📖
‏‌CheatReader⁩ یک ابزار عالی برای مطالعه در محیط کار است. با استفاده از این ابزار، می‌توانید کتاب یا رمان مورد علاقه‌تان را در یک پنجره شناور در گوشه دسکتاپ پین کنید و همزمان به کارهای اصلی‌تان برسید.
‏
🔥
ویژگی‌ها:
‏‌1⁩️⃣ پنجره شناور برای مطالعه در محیط کار
‏‌2⁩️⃣ حالت‌های متنوع مطالعه، از جمله حالت شفاف و نمایش تک‌خطی
‏‌3⁩️⃣ پشتیبانی از فرمت‌های مختلف، از جمله ‌TXT⁩، ‌EPUB⁩، ‌PDF⁩، ‌DOCX⁩ و غیره
‏‌4⁩️⃣ شخصی‌سازی، از جمله تنظیم فونت و جستجوی متن
‏
⚙️
مشخصات:
‏• پلتفرم: ویندوز، مک، لینوکس
‏• منبع: رایگان و متن‌باز
‏
🔗
لینک پروژه: ‌
http://github.com/yaoyao2mm/cheatreader
⁩
──────────────────────────────
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 730 · <a href="https://t.me/ArchiveTell/6871" target="_blank">📅 17:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6870">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxWlGYFJ-NC0rJBtvXJ0E1BF_Va9JXLBGOwkKEENtyo-hctAW2MbG2kzNz2kjVxB5CbMu4uiUuFdxcduzIXUNJN5BIWGrOvshrVmK2mfMNaq_Px5tDD9Tkkdaq1Dl2OvsGkgW2plkdf4C3LT65L-KUST-tvOedx-z2vEbB0Qhs0W52U_v3ilh6xjzafZho7e7X5RsZtdTEdVOAZ3npr6MhxaPBrXmFqHii1f5wcPN65l5_aMpNa9ZBkaXuUVEXWzSGWv7FKuoKEYRHDzmOTV_gXecsR6vo8Y-8i8rGdAh1SaY4AA7NGgHgQInsVM6KNOs9C8hpEPdKsd8FA7Yg4mBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡️
فورت (Fort)
🔥
یک فایروال (Firewall) قدرتمند و متن‌باز برای سیستم‌عامل ویندوز است که با کنترل ترافیک ورودی و خروجی شبکه، امنیت سیستم را افزایش می‌دهد.
✨
امکانات کلیدی:
🔹
کنترل و فیلتر کردن ترافیک شبکه برای برنامه‌ها و سرویس‌های مختلف
🔹
ایجاد و مدیریت قوانین اختصاصی برای دسترسی برنامه‌ها به اینترنت
🔹
مانیتورینگ لحظه‌ای فعالیت‌های شبکه و نمایش جزئیات اتصالات
🔹
سبک، رایگان و دارای رابط کاربری ساده
🔗
https://github.com/tnodir/fort
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/ArchiveTell/6870" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎬
آرشیو رایگان فیلم و سریال بدون سانسور
اگر دنبال یک مرجع برای تماشا و دانلود فیلم و سریال هستید،
PunkMovie
یکی از گزینه‌های خوب است.
✅
ویژگی‌ها: • آرشیو بزرگ از فیلم و سریال‌های خارجی • نسخه‌های
بدون سانسور
• به‌روزرسانی سریع با انتشار قسمت‌ها و فیلم‌های جدید • امکان تماشای آنلاین و دانلود • اپلیکیشن اختصاصی اندروید
🔗
لینک:
https://punkmovie.top
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/ArchiveTell/6868" target="_blank">📅 15:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
آپدیت Archive Scanner v1.0.1
🔧
تست سرعت دانلود درست شد (حل مشکل فیلترینگ SNI) — برای همه، بدون تنظیمات
📤
تست سرعت آپلود اضافه شد
🤖
ساخت خودکار Worker آپلود با یک کلیک (بدون نیاز به خروج از اپ)
🚀
سریع‌تر و کم‌مصرف‌تر  https://github.com/ArchiveTell/archive…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/6867" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SW2E2_wt3ayhLCJko8yqc3djSxXbqC6d_9TavLqGMeNDdaV_619gtUEI2lBtOM4MPGFAN-r5edM00eG9-6yyDpOzIfvQNjyV3VhmhGWT1cbc1SxPwYyVv5rLZacF3GtnjiYT1luD86YM0bVbJc5hcdewrZZHH3q_lWjI85hJXUG3TZMJpJl6vhp3k0tMjfvKqZKZvRPq0PHKm9cwih_sgnQ3q-jVIyNFoevebSHorJrJEkDFk97lxM7a_b3eTxPMAc06yZIW1TMZBd1aLFtxoZNIsuA5Jg7m2SaS_kT2bbVEA8d9xaE2DESwu8AaOUIMi_RwEWYIrB2sSxXZ-6-jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ryq_meGqihXwVwezrAJQxYzgRugpJ080pHXzllsAv08BqUwXQ7DRbBe4Z1dhA-y0cMOKvNKTnE38cFBGuUiSeKvB3I-kx2Wp7QkmhEtis6qVoLNaOPT-x1dYSjS72gMluuMh8NivMrz6EJx_w8-s8kZfHWePUaPYmDbKNRISpQo57ykL0uNzkuMQm8I2LzWnfO134eEMhP4vBmWjVCBJsbe2C4qvFyd2PBIoWa9w0bRZhVgyQCM8EFV3iJtZFgrs72kblgAKKLtJyxTeWD-tPhY36650Trngpjl1dpiQ5jXAUKPE-2j3xVVj1utrLiM3yg1XcA2nw65V__1TGrrL5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
آپدیت Archive Scanner v1.0.1
🔧
تست سرعت دانلود درست شد (حل مشکل فیلترینگ SNI) — برای همه، بدون تنظیمات
📤
تست سرعت آپلود اضافه شد
🤖
ساخت خودکار Worker آپلود با یک کلیک (بدون نیاز به خروج از اپ)
🚀
سریع‌تر و کم‌مصرف‌تر  https://github.com/ArchiveTell/archive…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6865" target="_blank">📅 13:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/ArchiveTell/6864" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📡
وای‌فای؛ دوربین نامرئی آینده؟
محققان نشان داده‌اند روترهای جدید Wi-Fi با کمک هوش مصنوعی می‌توانند تغییرات امواج را تحلیل کنند و بدون نیاز به گوشی یا وسیله همراه، حضور و حتی هویت افراد را تشخیص دهند.
🧠
این فناوری برای خانه‌های هوشمند و امنیت کاربرد دارد، اما می‌تواند نگرانی‌های جدی درباره حریم خصوصی و ردیابی افراد ایجاد کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/ArchiveTell/6863" target="_blank">📅 13:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8AVsgd_ORIcGqpojE3N05TYk_ozy2eY9IG3g6iHCJcBdbCj5aRSKleKYYPouY40RaDySxMlBRUe3Z67Sx6cUIQ8Gn-leDhzBsn7Vx4K-PYFcgibtobaxsD_07L5ee-o_POL9MONKaHI8IvKM7_f8O2c0BAgRlt6FafGpV3xVtMczo_YSeUL3uJS-7fgMvNuYkNeRs5ampIi3cAphZaiu0kbryTynTz3HMBWiQV-65WFXr_C2cCx12zjmzb6X1224aJKnxyWBwk4T26sdr2k-wYsHVc4Jb9-sVS370cFnEDjJMXkKBTSb2orzVjYk3TgvY0yfA7-5qMaHUxiB1o0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📦
‌RepoStore⁩: فروشگاه اپلیکیشن‌های گیت‌هاب از راه رسید!
🚀
‏دیگه نیازی نیست برای پیدا کردن پروژه‌های جذاب در گیت‌هاب، ساعت‌ها در مخازن مختلف جستجو کنید.
‌RepoStore⁩
دقیقاً مثل یک پلی‌استور اختصاصی برای گیت‌هاب عمل می‌کند.
‏
🌟
چرا باید از آن استفاده کنید؟
‏•
تجربه کاربری آشنا:
محیطی مشابه فروشگاه‌های رسمی که کار با آن بسیار ساده است.
‏•
مدیریت هوشمند:
نصب و آپدیت مستقیم اپلیکیشن‌ها بدون درگیری با فایل‌های ‌APK⁩ پراکنده.
‏•
شفافیت کامل:
امتیازها و تعداد ستاره‌های گیت‌هاب مستقیماً نمایش داده می‌شوند تا بهترین ابزارها را بشناسید.
‏•
دسترسی آزاد:
کاملاً رایگان و متمرکز بر پروژه‌های متن‌باز.
🔗
https://github.com/samyak2403/RepoStore
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6862" target="_blank">📅 13:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/ArchiveTell/6861" target="_blank">📅 13:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ArchiveTel
pinned «
🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…
»</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6860" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Tr - infinity.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">روز خوبیو توی این دوران سخت براتون ارزو میکنم
😜
🥰
Password :
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6859" target="_blank">📅 05:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام! اگر برای پروژه‌ها یا ربات‌های خود به یک API رایگان نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.  ؛Dahl Inference بدون نیاز به ثبت‌نام، تنها با چند کلیک یک API Key در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6858" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔥
دریافت API رایگان بدون ثبت‌نام!
اگر برای پروژه‌ها یا ربات‌های خود به یک
API رایگان
نیاز دارید، این سایت می‌تواند گزینه جالبی باشد.
؛
Dahl Inference
بدون نیاز به ثبت‌نام، تنها با چند کلیک یک
API Key
در اختیارتان قرار می‌دهد که می‌توانید از آن برای استفاده از مدل‌های مختلف هوش مصنوعی استفاده کنید.
ویژگی‌ها:
• بدون نیاز به ساخت حساب • دریافت فوری API Key • دسترسی به مدل‌های مختلف • مناسب برای تست، توسعه و پروژه‌های شخصی
هر کلید 100 میلیون توکن رایگان میده
😁
🔗
دریافت API:
https://inference.dahl.global/chatKeys#models
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6857" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">؛
🎨
Lake: اپلیکیشن آرامش‌بخش رنگ‌آمیزی برای بزرگسالان
اگر بعد از یک روز پرمشغله دنبال راهی برای استراحت و دور شدن از استرس هستید،
Lake
یکی از بهترین گزینه‌هاست.
این اپلیکیشن مجموعه بزرگی از طرح‌های رنگ‌آمیزی را که توسط هنرمندان واقعی طراحی شده‌اند در اختیارتان قرار می‌دهد. از
مناظر و طبیعت
گرفته تا
معماری، دکوراسیون، حیوانات و پرتره
، برای هر سلیقه‌ای طرحی پیدا می‌شود.
✨
امکانات: •
🖌️
صدها طرح باکیفیت •
🎯
حالت هوشمند برای جلوگیری از خروج رنگ از خطوط •
🎨
ابزارها و پالت‌های رنگ متنوع
🆓
کلی طرح رایگان برای شروع
اگر به دنبال یک سرگرمی ساده و آرامش‌بخش هستید، Lake ارزش امتحان کردن را دارد.
نکته: فعلا فقط برای آیفون در دسترسه
🔗
سایت:
https://lakecoloring.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6856" target="_blank">📅 01:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6854">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_mZQ9ppRJX1CF9OJsa_MOqDVphag-LlofFhLTZDUNOSm1zfVEbDBceV2UFimaDQQofdyFQxQElYLCtnwRb2ZtVPuPGghaLPhrLODz7ABmt8CHzJpSoIBrSkyexhbpHOLZpJTI8E-oFjkS08V16l533T4hfn7ZrYO4lL1VhUVo2ATYJa4qsgtc6tyiiYj_hstQA_7x-gnxCqvKR4tpllif29vRi0j-t7dLSN9u5C4ktNBVvUnbcOLaFem3qv-BXWOU-lg0mKulLu6muF5fl39Cy6W15jF7iqwFaU-kOA8XkFJiHQzD0NDTSHOmGnTwgnGiHG3xd2vucu6u-MZmkbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SerbABpcPQcG9VshN5Emu-XIm1OS4XsULWCSd6-MPt6S8iYD0u6v_gg-yLmlaYZbSkGcCEuwKWistmAf24o1mcaZh4hHP6TA4WljLGK6l2ZLDqQ6v4WjEcz9BP8rrSF2Gxx5JhECbNog-UG3JPsMamR8_qX7d4smVZPpLToogtnOZWTqhS9XwdJmphj7ZLoUYBXW-qPq0ffFz2iuG21pPxck7HTt_de9G90oZkh0BUYRydms-OU_wMyQt-iQMHJcVN8Wtdzkn4MhItydjChnL72Nd2eC3Ed5bkS9NWCvYmzNJzGVYts2g5wL9n3gYvaOtKFShXxmEABcNChP-H1BJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0  (اسکنر آیپی تمیز کلودفلر) به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6854" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6853">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
انتشار رسمی Archive Scanner v1.0.0
(اسکنر آیپی تمیز کلودفلر)
به عنوان عضوی از کامیونیتی، همیشه جای خالی یک اسکنرِ دقیق، سریع و پایدار را حس می‌کردم. ابزارهای موجود یا بسیار کند بودند، یا با باگ‌های عجیب همراه بودند. تصمیم گرفتم این خلاء را شاید خودم پر کنم. امروز با افتخار نسخه اول
Archive Scanner
را به شما تقدیم می‌کنم.
🔥
قابلیت‌های فنی و تخصصی:
✅
اسکن پیشرفته SNI + TLS:
ما به پینگ ساده اکتفا نکردیم! با شبیه‌سازی کامل TLS Handshake، آی‌پی‌هایی را پیدا می‌کنیم که "واقعاً" کار می‌کنند.
⚡️
سرعتِ خیره‌کننده:
طراحی‌شده برای اسکن‌های فوق‌سریع که زمان شما را هدر نمی‌دهد.
🎯
حذف هوشمندِ آی‌پی‌های مرده (Dead-End Elimination):
فیلتر کردنِ آی‌پی‌هایی که پورتشان باز است اما عملاً ترافیک را رد نمی‌کنند.
✨
طراحی مهندسی‌شده:
طراحی و توسعه کامل توسط
Bachelor
⚡️
با تمرکز بر UI/UX مدرن (Material Design 3).
🛠
شفافیت و آینده پروژه:
من تمام تلاشم را کرده‌ام تا این نسخه در پایدارترین حالت ممکن باشد، اما چون در ابتدای مسیر هستیم (v1.0.0)، ممکن است باگ‌های جزئی وجود داشته باشد. من متعهد هستم که در آپدیت‌های بعدی این موارد را سریعاً برطرف کنم.
💡
خبر خوب:
این نسخه از
آپدیت درون‌برنامه‌ای (In-App Update)
پشتیبانی می‌کند؛ بنابراین به محض انتشار نسخه جدید، شما باخبر خواهید شد و نیاز به دانلودِ دستیِ مجدد نخواهید داشت.
📥
لینک دانلود مستقیم (گیت‌هاب)
این اپلیکیشن حاصل روزها تلاش مستمر من برای ارتقای استانداردهای جامعه شبکه است. اگر باگی دیدید، حتماً اطلاع دهید تا در آپدیت‌های آینده برطرف شود.</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6853" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVr18DkdbZW74GLK5RxXU2lZh2Sp5igzLvr0aWcOSkPXpFIDMOJp1FMDKsa_2WXn86qLFuAZDKUZLroEysj4vH-Qz1FubSiAJC7nvK8zESLzbX7vDb2wjaZfz0MznDrqerUhOx6Xa9MfSUJ0a6HL2bwph_knHyAfaBi3LhjGFKwdTGFUpsNYmvxAJOo0VkQUiYK1cbq14Z_442lLljo6LOKhX_N3zTJBn9pOWLitz-UR3o0Ka_HnvRwbKpEUSloRoIDCwFILADkxyTjgUTTvL6b0TAP9ptkH9fJHB-CYIpFVR7iMi8Ibu4DKaEYQs9wMJ7ehKdUAWAAGVDyw6eQH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
‏
🎮
آیا ‌GTA 6⁩ زودتر از موعد به کامپیوترها می‌آید؟**
🖥️
🔥
‏شاید غیرممکن به نظر برسد، اما توسعه‌دهندگان امولاتور ‌SharpEmu⁩ در حال برداشتن قدم‌های بزرگی برای اجرای بازی‌های ‌PS5⁩ روی ویندوز هستند!
🛠️
‏
✅
چه اتفاقی افتاده؟
‏تیم سازنده موفق شده بازی سنگین ‌Demon's Souls⁩ را تا مرحله لودینگ و صفحه اصلی روی کامپیوتر اجرا کند. این یعنی معماری ‌PS5⁩ در حال رمزگشایی است.
‏اگر این روند با همین سرعت پیش برود، برخی امیدوارند که بتوانند ‌GTA 6⁩ را قبل از انتشار رسمی نسخه ‌PC⁩، از طریق این شبیه‌ساز روی سیستم‌های قدرتمند تجربه کنند.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6847" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚀
۱۰۰۰ اعتبار رایگان در Flashloop برای ساخت ویدیوهای هوش مصنوعی!
🎥
اگر به ساخت ویدیو با هوش مصنوعی علاقه دارید، می‌توانید با ثبت‌نام در Flashloop، ۱۰۰۰ اعتبار رایگان دریافت کنید.
مراحل دریافت اعتبار:
1️⃣
وارد سایت شوید:
https://www.flashloop.app
2️⃣
با حساب گوگل (یا سایر روش‌ها) ثبت‌نام کنید.
3️⃣
هنگام ثبت‌نام یا در بخش مربوطه، کد زیر را وارد کنید:
Z36ZT9
🎉
با وارد کردن این کد، ۱۰۰۰ اعتبار رایگان به حساب شما اضافه می‌شود.
با Flashloop می‌توانید انواع ویدیوهای AI در سبک‌های مختلف تولید کنید و از ابزارهای ویرایش و افکت‌های متنوع آن استفاده کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6846" target="_blank">📅 20:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6845">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQiG9_Nha8zqB7lnle2J1V_hYPV4Kk0Xe1Nx5Jz59vCDIlI8yx4GK1bJqoSytrmT5KY3xpl-1cgwZrR0HmGUs9kHPa92fTDWjWRYu6eqF02bKhbLVVxZnhKaw3YZXMD1t-1zQt-14RQ9tXLrf-MMtRtMZ8qiH9sMQFwJSknjBXgnAlQf_tB6nDdWYB9UDroWlfc8meRpJo54HAcGh-OjhPacwkMBuFy-3i5d26C6DO4Sr8GILt9F6K0XzrP0IVrdLqWW1DhRD0j0i5GuDFxqMkAgIwOeD__2edht29EIRxUu0W7RlHCMQ2zzBr5KIMjqA8ZAab2wQ9LZWYGqheedHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐧
GameShell
GameShell
یک پروژه
متن‌باز
برای یادگیری دستورات لینوکس و
Bash
است که به‌جای آموزش سنتی، مفاهیم را در قالب مراحل و مأموریت‌های تعاملی آموزش می‌دهد
🔹
اگر قصد دارید کار با ترمینال و دستورات لینوکس را به‌صورت عملی و سرگرم‌کننده یاد بگیرید،
GameShell
می‌تواند نقطه شروع مناسبی باشد
◾️
🔺
GitHub
✔️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6845" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نامحدود
🫡
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.189:8080#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6844" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نامحدود
🔥
vmess://771a590c-5eac-5732-b796-17251132f8d2@47.83.221.185:80?encryption=auto&security=none&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6843" target="_blank">📅 18:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
💎
گنجینه‌ای از ۱۰,۰۰۰ پرامپت طلایی!
🍌
✨
‏اگر به دنبال خلق تصاویر خیره‌کننده با هوش مصنوعی هستید، این مخزن دقیقاً همان چیزی است که نیاز دارید!
🎨
🚀
‏
✅
ویژگی‌های این مجموعه:
🔹
بیش از ۱۰ هزار پرامپت منتخب و تست‌شده
‏
🔹
بهینه‌شده برای
‌Nano Banana Pro (Google Gemini)⁩
‏
🔹
سازگاری کامل با ۸ مدل برتر دنیا (از جمله ‌Midjourney⁩، ‌DALL-E⁩ و ‌Flux)⁩
‏
🔹
همراه با پیش‌نمایش تصاویر برای درک بهتر خروجی
‏
🔹
کاملاً متن‌باز (‌Open Source)⁩ و رایگان
‏
🔗
https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6842" target="_blank">📅 16:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416755798a.mp4?token=n-C3JFP03QCKXAvcRyf2fEYypD9zh7m1Nu_ztwxQTsQOEg3lcf648pSHu9Q4DJxNEyZuj0A6gQkdDMhssEA8Mo1a2ueHb5dU2qbTDBN3peLVbkdvjfahj1sx_SAmN3Adf29yZQAkLUlmQxuZoE9yUF_HvWDR7Qgye5ht5tbMFkTq6VvVU24QxKcFtMxgUc9RmtQQagptaK1bLkSDC3Xwhm02ol0LSJdYw0ZaISZWOROsZdPe12yRCXnVDcnj9ycNsAxQz8OAcwh0J30SfhStk223YGPbuSdixb1IwjGFuKQkaYVJo-cZ6BlBtqNdLGcXiP2yzH_u0hYQiWsrd-Pdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416755798a.mp4?token=n-C3JFP03QCKXAvcRyf2fEYypD9zh7m1Nu_ztwxQTsQOEg3lcf648pSHu9Q4DJxNEyZuj0A6gQkdDMhssEA8Mo1a2ueHb5dU2qbTDBN3peLVbkdvjfahj1sx_SAmN3Adf29yZQAkLUlmQxuZoE9yUF_HvWDR7Qgye5ht5tbMFkTq6VvVU24QxKcFtMxgUc9RmtQQagptaK1bLkSDC3Xwhm02ol0LSJdYw0ZaISZWOROsZdPe12yRCXnVDcnj9ycNsAxQz8OAcwh0J30SfhStk223YGPbuSdixb1IwjGFuKQkaYVJo-cZ6BlBtqNdLGcXiP2yzH_u0hYQiWsrd-Pdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
؛Traycer Desktop App منتشر شد!
رایگان، متن‌باز و ساخته‌شده برای AI Orchestration.
✨
قابلیت‌های جدید:
• استفاده از اشتراک‌های فعلی مثل Claude، Codex، Opencode و...
• ارتباط Agent-to-Agent و Loops
• ؛Workspaceهای دائمی با Tab و Sub-tab
• اشتراک‌گذاری Taskها و همکاری با اعضای تیم
امروز دیگر توانایی مدل‌های هوش مصنوعی چالش اصلی نیست.
چالش واقعی، ساخت محیطی است که Agentها بتوانند به‌صورت هماهنگ با هم کار کنند، حافظه مشترک داشته باشند و از هر جایی ادامه‌ی کار را از سر بگیرند.
؛Traycer دقیقاً برای حل همین مسئله ساخته شده است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6841" target="_blank">📅 15:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6839">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚀
تبدیل Qwen Chat به API رایگان!
اگر همیشه دوست داشتید از
Qwen
داخل پروژه‌ها، ربات‌ها یا برنامه‌های خود استفاده کنید، این پروژه دقیقاً برای همین ساخته شده است.
؛
FreeQwenApi
سایت
Qwen Chat
را به یک
API رایگان و سازگار با OpenAI
تبدیل می‌کند؛ یعنی می‌توانید بدون تغییر زیاد در کد، از مدل‌های Qwen داخل پروژه‌های خود استفاده کنید.
✨
قابلیت‌ها
✅
تبدیل Qwen Chat به API
✅
سازگار با OpenAI API
✅
پشتیبانی از Streaming
✅
پشتیبانی از فایل، تصویر و Web Search (در مدل‌های پشتیبانی‌شده)
✅
قابل استفاده در Open WebUI، LobeChat، Dify، Claude Code و...
🛠️
آموزش راه‌اندازی
1️⃣
پروژه را دانلود کنید
git clone https://github.com/y13sint/FreeQwenApi cd FreeQwenApi
2️⃣
وابستگی‌ها را نصب کنید
npm install
3️⃣
پروژه را اجرا کنید
npm start
4️⃣
وارد حساب Qwen شوید
توکن (Session Token) اکانت Qwen خود را داخل پروژه قرار دهید؛ از این به بعد می‌توانید از Qwen مثل یک API معمولی استفاده کنید.
⚠️
این پروژه API جدیدی ایجاد نمی‌کند؛ بلکه از دسترسی رایگان حساب Qwen شما استفاده کرده و آن را به یک API سازگار با OpenAI تبدیل می‌کند.
🔗
GitHub:
https://github.com/y13sint/FreeQwenApi
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6839" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6838">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">vless://c44c7433-5460-4269-a7de-0af05e27a48f@64.90.7.33:8080?type=kcp&headerType=none&seed=SwbMceiT2H&security=none#%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86
نامحدود
اگه دیدید قطع شد ip فیلتر شده
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6838" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ-I2_zaI7SrVVLVFcdY9MaH2H5KlVv-dvNbGHiZxuwBPnyL7QWUEKCRDmq88QW93nYCcDf_3sOPnLqjTRwtYMAYIi2h90SlXZlgsNe9vJr_jp448k_Lkn41_1Np8t4IiZrceOAeIsThJcHBT0k91E9RQIhwjVNiy_1NY8m33R7zoRglwwNviGGwMfSQTREbFBuGj9UEz_TUZ21DlUU6rLqqqt7HC0zoqtKJPJyVql4ebkJ5bS8oSbGPFgseUX0H7eS-5sErX2NnyWXeEsdPxGLcZOWB7D8Hm1meIFruFcubltISQ51F_fPSAkhR-XJJUGTCm7sNSbhgo-SkLJ4JMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
یک ابزار جذاب برای کار با ویدیو!
معرفی Frame؛ رابط گرافیکی بومی برای FFmpeg ساخته‌شده با Rust
🦀
؛FFmpeg فوق‌العاده قدرتمنده، اما کار با خط فرمانش برای خیلی‌ها سخت است. Frame همان قدرت را با یک رابط ساده و زیبا در اختیار می‌گذارد.
🔥
امکانات:
⚡
ارتقای کیفیت تصویر با AI (Real-ESRGAN)
🚀
شتاب‌دهی سخت‌افزاری (Apple Silicon و NVIDIA)
📦
مدیریت چند پردازش همزمان
🔒
کاملاً لوکال؛ بدون تله‌متری و بدون نیاز به حساب کاربری
💻
پشتیبانی از macOS، Windows و Linux
﻿
یک انتخاب عالی برای کسانی که با تبدیل، فشرده‌سازی و پردازش ویدیو سروکار دارند.
🎥
github.com/66HEX/frame
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6837" target="_blank">📅 04:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚀
؛Grok 4.5 رایگان شد!
مدل جدید کدنویسی Grok 4.5 از xAI برای مدت محدودی به‌صورت رایگان در ابزارهای Agent قابل استفاده است.
✨
ویژگی‌ها:
🧠
پنجره متنی 500K برای پروژه‌های بزرگ
⚡️
مناسب برای Agentهای کدنویسی و جلسات طولانی
🔌
سازگار با Hermes، Aider، OpenCode، Cline، Claude Code و تمام ابزارهای سازگار با OpenAI API
⚙️
راه‌اندازی در کمتر از ۲ دقیقه:
curl -fsSL https://x.ai/cli/install.sh | bash
سپس:
• آدرس
localhost:8000/v1
را به ابزار خود معرفی کنید.
• مدل grok-4.5 را انتخاب کنید.
• یا از API Key در کنسول xAI با آدرس پایه
https://api.x.ai/v1
استفاده کنید.
⚠️
این دسترسی محدود و موقتی است و شامل Rate Limit می‌شود. (شاید ۱۲ ساعت مونده باشه ازش) (تست نشده)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6836" target="_blank">📅 04:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmw3KWIgc7fGKpJ75QfQC8oiHNfX_LVjmsnklnM9cIn-zjTN9D1NIkDh4JAckZgpU_M-Qeq5OzuGqCF7T4dRKriDUgXaH5aizyckwwg0l77gUy6mwD0sNA8CSWhR3jmBEKizlaqq8nJDumDBXmOuY3DHT1EZa8-fV3Vs3EnHFlSb4Iq-mXNbP9KrMWwgxhA-Nh504o292lejuwtOJDqZTWBgeKsvKD1hV_e5Bki9zpg8Q4KYOta8HrV9vJIL7aXn0FcDfESM-whmNnrMOPLwaG4_iOZCT2b5rcGYhHSielxM_wNMFtN3G5Kk9UWE6QJPGifr82Up8dHatUN8oKmYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧭
؛MBCompass؛ قطب‌نما و مسیریاب متن‌باز برای اندروید
یک اپلیکیشن سبک و رایگان برای طبیعت‌گردی، کوهنوردی و استفاده روزمره؛ بدون تبلیغات، بدون ردیابی و بدون وابستگی به سرویس‌های گوگل.
✨
امکانات:
🧭
قطب‌نمای دقیق (شمال مغناطیسی و واقعی)
📍
نمایش موقعیت لحظه‌ای روی OpenStreetMap
🗺️
پشتیبانی از نقشه‌های آفلاین و آنلاین
🥾
ضبط مسیر و خروجی GPX
🔋
حجم کم (~۲ مگابایت) و مصرف باتری پایین
🔒
بدون تبلیغات، بدون جمع‌آوری داده‌های شخصی
یک گزینه عالی برای علاقه‌مندان به سفر، طبیعت‌گردی و مسیر‌یابی.
🌿
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6835" target="_blank">📅 03:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter وارد سایت Agentrouter شوید با حساب Github ثبت‌نام کنید بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key وارد سایت شوید…</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6833" target="_blank">📅 00:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6831">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS1SL8rOVk078ByCBB3-rSrcagbH1lexCv-cBV-TvS2gAdXJoadbjt0q5kuBGXXHZ52qEWsoCkGTlsMTYUiaFQQ-n3COtH27cNf7TfpagSPBVVn6SE-MiSzXS-167MQJJ0Av10XJkKmge7ffLQ7AfzExckZiMXDQxaiMHycdrXY5C3aKEH98EgeszBwyHL-DBSO4pY8mnN8UmnjN1082mKtpx0SaAQHoNx2mbhNvjE5GZ7bguHUqmgZWvsHO3rQFT2MKbHvJDI23DZoHkkznHSr0ZMeykFoL-4ckY3jvMN8fti6NEb3Q5TJfh1O2a83QRHlvk964NeKQKQYP6-XRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☁️
🚀
؛Cloudflare Drop؛ انتشار سایت در چند ثانیه!
کافی است پوشه پروژه‌تان را داخل مرورگر Drag & Drop کنید تا سایت فوراً روی شبکه Cloudflare منتشر شود.
✨
ویژگی‌ها:
⚡
بدون نیاز به ثبت‌نام
🌍
دسترسی جهانی با تأخیر بسیار کم
📁
مناسب برای دمو، نمونه‌کار و پروژه‌های آزمایشی
⏳
نسخه‌های بدون حساب تا ۶۰ دقیقه فعال می‌مانند و سپس حذف می‌شوند؛ با ثبت‌نام می‌توانید آن‌ها را دائمی کنید.
https://cloudflare.com/drop/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6831" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGbKlL0a4Op1DrgL7kBPyaRp_65jf5k4Y2M1eHzmnzHQpzE8-oeB1MT_7K5j6l9-BldbXMHSO-u_rkS4hpx6zbVORgxX8LBuekc5k0Hj92sHAX6jC-xourT0wBc6cROkiahibWlmppgzjZ4FUkmsR2q-jqOc_xwFBCGowzvv0HxIWaiD3Vn2wjdSyFWExLjgIgVEDBqQgpcqUfCMvA-yVtLk6fSrkUAeoN8WLabWkYrrlxnl3PSxlRHL1IK0XayiCBe9lMVU8-4Ctl6CgkaALY30kq1QYj0-5gPNZ1SuOlBuYYCpKDY4bnpf_mg811cGF8mxW-5IbDRgc5qY_q-I_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6829" target="_blank">📅 23:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🧩
؛CanvasMind | ساخت و استقرار ورک‌فلوهای AI با بوم بصری
✨
یه ابزار متن‌باز و Low-Code برای طراحی و اجرای ورک‌فلوهای هوش مصنوعی! دیگه فقط دمو نیست، مستقیم به پروژه قابل استقرار تبدیلش کن
🚀
⚡
ویژگی‌ها:
🎨
بوم گرافیکی با Drag & Drop
🔀
شرط، حلقه و منطق کنترلی
💻
اجرا محلی یا از راه دور via SSH
🤖
دستیار هوشمند داخلی
🚀
خروجی CLI، API، Docker و Server
🔗
https://github.com/buyaka/canvasmind
#هوش_مصنوعی
#LowCode
#ورک‌فلو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6828" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📱
💿
؛EtchDroid؛ ساخت فلش بوتیبل با گوشی اندروید
اگر کامپیوتر در دسترس ندارید، EtchDroid به شما اجازه می‌دهد فایل‌های ISO سیستم‌عامل‌های لینوکسی را مستقیماً از طریق گوشی روی فلش USB رایت کنید و یک فلش بوتیبل بسازید.
✨
ویژگی‌ها:
🔹
متن‌باز و رایگان
🔹
پشتیبانی از اکثر توزیع‌های لینوکس و Raspberry Pi
🔹
مناسب برای مواقعی که سیستم بالا نمی‌آید و فقط گوشی در دسترس است
⚠️
این برنامه از ISO رسمی ویندوز و فایل‌های DMG مک پشتیبانی نمی‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6827" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤖
؛Cogny | دستیار هوش مصنوعی بازاریابی
✨
یه ابزار فوق‌العاده که بازاریابی رو با هوش مصنوعی انجام میده! سئو، تبلیغات، تحلیل رقبا و کلی کار دیگه
🚀
⚡
ویژگی‌ها:
🎯
سئو و بهینه‌سازی محتوا
📊
تحلیل کمپین‌های تبلیغاتی
🔍
آنالیز رقبا و بازار
✍️
تولید متن تبلیغاتی
📈
اتصال به ۱۳ کانال بازاریابی
💻
کار با Claude، Cursor و Codex
💰
رایگان برای شروع · ۹ دلار برای استفاده نامحدود
🔗
https://cogny.com
#هوش_مصنوعی
#بازاریابی
#سئو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6826" target="_blank">📅 21:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8iBH4l-xBly0PaOdcj5jWxut7MLcOefbtZL7fLRyyCiY8be4oRXoOMQhWetSZ_qHhBshuU8bb0ymJbvHiowe_z3aqUANFYLfs-1LbtP9OtLdirVRFnmpr26ECYvZTZcQjcuZiK1PAFzVc4B-quym3IHa_GBL3y_oUuKD97x6a1PDm7Rkmm0RqWOBAcfaDRd7CB1aHtKVghAqFYZcemRXv_g6WMGudBOA091mo4kfdMVFZ9L-anNoHOAMBX2kyQoNbp6A_4WcniKiTyMHbJcW3HwZNlUWj0qVDo5pFH4JABGrhUUzQQl35C7OX0Vb3MhuHIPcLfqV30ftt8woEgKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6825" target="_blank">📅 20:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">104.17.14.0
104.25.49.102
ایپی تمیز کلودفلر
تست کنین
❤️
با لایک و دیسلایک و کامنت اعلام کنین
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6824" target="_blank">📅 20:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6821">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEnMxvtHeVxdze_sV2j8wTba9_NOT5P4MhY5BhwiBOy4s28-HE3jqoyI6velyZhaiFdEVem7CoHqMetRs9r10Awl32FzZdDOV7YoD2pZ_GMHMU4-LGM7fC_NY8tJRlJ_y3XpGyGiWhTI6okOQk4AqhQCO58gGW28ihVTxkRcOgBF3mJAr6kIMultDKrq_37K7aFeO9G8UkUHy2RUj7NmFGHWBbVeJW29t7O-DN6CC8r_v288HE3i4Bbfjyle_xxsax7IT_ORi1AJ-SCi5LaPcoP8SLw4WKkBH8QkI1WSNT0-O1rCkugdAAkxhAjAuQa7jA8J6WvxcSjVjZZcgkiRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_5JtRWZRbIN5JRH4Bgq-ebyrs6h7ERtxepImwsUsuJ534s07PeKidqeI2iNKK3juqd8-dvqccmJT2RmgWezZNPjHpN7ISt11QJ8pLPC4o4AjXwxiJipCnQCecejalEJdYZG2zXVxy6Hi0Qd4VugFOvSk--1qFdD8PthZEYpFF8sTYYEXTLDmLv-z0akR7b837lrH3-dpPlOGjzYSxvYG_0yu4GEckfaiua5PUTo4sKGWeUKcMdTXpwklraDpa0JO4crVeYXSzA8gO2lcL821IihY5nhbuiP0Ki22gPKpWV3JKnUY42RpkAZgvR_kk9mHcB3m-Hbs_olmsVDzvkJTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏‌
Imgfree⁩: ابزار رایگان تولید تصویر و ویدیو با هوش مصنوعی
🤖
‏
🌐
پلتفرمی که مدل‌های پیشرفته هوش مصنوعی مانند ‌‌Midjourney⁩، ‌GPT-Image⁩ ، ‌Kling⁩ ، Nano Banana و Flux را گرد هم آورده است
📈
‏
✨
تولید تصویر و ویدیو بدون نیاز به تنظیمات پیچیده
📺
‏
🔗
لینک: ‌
https://www.imgfree.co
⁩
‏
💻
دسترسی رایگان و نامحدود برای تولید محتوای با کیفیت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6821" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6820">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB27B3iSGNc4_9sjazh-RjEzr1d73irsv-Ml6SCF-OuCcJiZGOD5EkdRYHk3_nO5CKnxkzzrMkGLpu--NQ9J0VPAzSveayZDudk3tS_J9mMndw7vQAfMkOBJu7Bgkxp4V1kgMzh310qPU6Y-M1tXrzQgVfGpSxvp-3JR2Sj-U9Us2lRi8YIsg4ZNd0HffJpN59C-_DpAVdWsL5CAdWXbatBammX_bF7F1xX_jm5uZt8T4yPV5IoliijDFkbVxVYn_g5IBIQ72_6dn9uVri9iMFZeWeFwORBn8X-FMPh83l6DlNYQzCHqWZW95O3ue5GjyBj9TSdqb6umDuWzCqe_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛
🎬
CapCut Web؛ ادیت ویدیو با هوش مصنوعی
اگر تولید محتوا می‌کنید یا برای شبکه‌های اجتماعی ویدیو می‌سازید،
CapCut Web
یکی از کامل‌ترین ابزارهای آنلاین برای تدوین سریع و حرفه‌ای است.
با قابلیت‌های هوش مصنوعی این پلتفرم می‌توانید:
•
🪄
حذف خودکار پس‌زمینه و نویز صدا
•
📝
ساخت زیرنویس خودکار (حتی برای فارسی)
•
✂️
تبدیل ویدیوهای طولانی به کلیپ‌های کوتاه مناسب ریلز و شورتز
•
🎨
استفاده از افکت‌ها، قالب‌ها و ابزارهای هوشمند ادیت
🔗
سایت:
https://www.capcut.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6820" target="_blank">📅 18:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6819">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌐
دانلود کامل هر وب‌سایت با Website Downloader
اگر می‌خواهید یک وب‌سایت را برای استفاده آفلاین یا بررسی کدهای آن دانلود کنید(فرانت اند)،
Website Downloader
ابزار مناسبی است.
✨
قابلیت‌ها: •
📥
دانلود کامل
HTML، CSS، JavaScript، تصاویر و فونت‌ها
•
🔗
بازنویسی لینک‌ها برای اجرای آفلاین •
📦
خروجی به‌صورت فایل ZIP •
⚡
متن‌باز با لایسنس MIT
این ابزار برای
کلون کردن سایت‌ها، تهیه نسخه آفلاین و یادگیری ساختار پروژه‌های وب
بسیار کاربردی است.
🔗
GitHub
:
https://github.com/AhmadIbrahiim/Website-downloader
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6819" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6818">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=LJxCRUn6DtV_-_CNag4cH9IZWJFHsmNKV_K5HH1l8wcVQI5Dz_Wr9Cy34AO2vQO2iBVtoqGfhOiQfjePCAlvpbLuKqO3vYBhTRkCOi-HacqwRGJY3hXtvbjMEcR7cMYNaOWx0WyG3H7m_0okAGIDSUHSl_YDGRr-fsVSxTXO1h__6qElED7-J_hLu070Ii13WNmh_OLtLmxpLA2WF8hv5nexOBEIbxQ6ZzYVmKfpcAZu-ajdRG9kZg7Qi90BO7ztqNuIFOurCw1dzqSC1MFIyuqw-II-FMAPlJXJPcPnpTJ43-g4GtGz5ZERK_tyDeXibI3AfLUgL0sb2iCqUjxiQZiIRHxKIRMt62lGhTTF_TrqOYxnc9Eh7GcFnNovWYuQkBXq8G_dzJ_WmfKfBS-NgkE8n8kank12mIAdEG2avDaP2MEc7BSI94_VUvUnqSQ4zq4fI1CgdsLo7ilx9zsCnsfCw_p6-KEIAAMru36lUZVhdCyFlkO7XQ3E37MlCt8vy4tlCYKx6bBX3LAesoFN-8t951YAqAERmfpYI7JXaCew9l-RuYVQPyfZNT8d6L0udQa4gjnIaVqWxP9qLl52rFOVeaxYUlO55nzp_-YdlOmrGY-X9hQLrEjWKU-Rs9DAhsP2pbkaaFdYqqQrI8jJCTNPvlfu4eVKMIKNPrK0Up4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=LJxCRUn6DtV_-_CNag4cH9IZWJFHsmNKV_K5HH1l8wcVQI5Dz_Wr9Cy34AO2vQO2iBVtoqGfhOiQfjePCAlvpbLuKqO3vYBhTRkCOi-HacqwRGJY3hXtvbjMEcR7cMYNaOWx0WyG3H7m_0okAGIDSUHSl_YDGRr-fsVSxTXO1h__6qElED7-J_hLu070Ii13WNmh_OLtLmxpLA2WF8hv5nexOBEIbxQ6ZzYVmKfpcAZu-ajdRG9kZg7Qi90BO7ztqNuIFOurCw1dzqSC1MFIyuqw-II-FMAPlJXJPcPnpTJ43-g4GtGz5ZERK_tyDeXibI3AfLUgL0sb2iCqUjxiQZiIRHxKIRMt62lGhTTF_TrqOYxnc9Eh7GcFnNovWYuQkBXq8G_dzJ_WmfKfBS-NgkE8n8kank12mIAdEG2avDaP2MEc7BSI94_VUvUnqSQ4zq4fI1CgdsLo7ilx9zsCnsfCw_p6-KEIAAMru36lUZVhdCyFlkO7XQ3E37MlCt8vy4tlCYKx6bBX3LAesoFN-8t951YAqAERmfpYI7JXaCew9l-RuYVQPyfZNT8d6L0udQa4gjnIaVqWxP9qLl52rFOVeaxYUlO55nzp_-YdlOmrGY-X9hQLrEjWKU-Rs9DAhsP2pbkaaFdYqqQrI8jJCTNPvlfu4eVKMIKNPrK0Up4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌎
نقشه آینده زمین برای زندگی!
‏این پروژه خیلی جالب و مهمه! یه نقشه تعاملی به نام ‌Farmland Atlas⁩ ساخته شده که پیش‌بینی می‌کنه مناطق مختلف زمین چقدر برای زندگی مناسب خواهند بود تا سال ‌2100⁩.
🤔
‏این پلتفرم با تحلیل بیش از ‌5⁩ میلیون نقطه، چندین سناریو رو بررسی می‌کنه، از خوش‌بینانه تا بدبینانه. برای هر مکان، پیش‌بینی آب و هوا، ارزیابی کیفیت منابع آب، وضعیت خاک و خطرات اجتماعی رو هم در نظر می‌گیره.
🌟
🔗
https://farmlandatlas.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6818" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6817">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📊
معرفی ابزار CodexBar
اگر از
Claude Code، OpenAI Codex، Cursor، Gemini، OpenRouter، GitHub Copilot
یا سایر ابزارهای AI استفاده می‌کنید، احتمالاً بارها با محدودیت استفاده یا تمام شدن سهمیه مواجه شده‌اید.
؛
CodexBar
یک ابزار متن‌باز برای macOS است که تمام این اطلاعات را مستقیماً در نوار منو نمایش می‌دهد تا همیشه بدانید چقدر از سهمیه‌تان باقی مانده است.
ویژگی‌ها:
• نمایش میزان استفاده و سهمیه باقی‌مانده
• نمایش زمان دقیق ریست شدن محدودیت‌ها
• پشتیبانی از Claude، Codex، Cursor، Gemini، OpenRouter، GitHub Copilot، Groq، Deepgram، MiniMax،
z.ai
و ده‌ها سرویس دیگر
• نمایش هزینه، اعتبار و میزان مصرف API در سرویس‌های پشتیبانی‌شده
• نمایش وضعیت آنلاین سرویس‌ها و اختلالات احتمالی
• حالت تجمیعی برای مدیریت چندین سرویس از یک پنل
• بدون ذخیره رمز عبور؛ از نشست‌ها و لاگین‌های موجود شما استفاده می‌کند.
🔗
GitHub:
https://github.com/steipete/CodexBar
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6817" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6816">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚀
چند ابزار متن‌باز و رایگان برای برنامه‌نویس‌ها و سازنده‌ها:
🎨
Text Effects
افکت‌های جذاب CSS برای طراحی متن و رابط وب.
📧
SESPulse
داشبورد متن‌باز برای مدیریت و بررسی ایمیل‌های Amazon SES.
🔎
API Finder
مخزن APIهای عمومی برای پیدا کردن سرویس‌های آماده.
🛡
Tirreno
فریم‌ورک امنیتی متن‌باز برای شناسایی رفتارهای مشکوک کاربران.
💻
OpenTUI
کتابخانه ساخت رابط‌های کاربری زیبا در ترمینال.
✨
ابزارهای کوچک، کاربردهای بزرگ برای ساخت سریع‌تر پروژه‌ها.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6816" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6815">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://ac7e7b41-0dc0-4bec-a285-3266ecbb87c8@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6815" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6814">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📸
ساخت عکس پرسنلی ۳×۴ با هوش مصنوعی
اگر یک عکس معمولی از خودتان دارید، می‌توانید با پرامپت زیر آن را به یک
عکس پرسنلی رسمی
تبدیل کنید.
✨
ویژگی‌ها:
✅
پس‌زمینه سفید یا خاکستری ساده
✅
نورپردازی طبیعی و یکنواخت
✅
حذف اشیای اضافی و اکسسوری‌ها
✅
افزایش کیفیت و وضوح تصویر
✅
مناسب برای عکس پرسنلی و پاسپورت
📝
Prompt:
Convert this photo into a professional ID/passport photo.
- Neutral plain background (light gray or white, evenly lit, no texture).
- Centered face and shoulders visible, crop from top of head to chest.
- Natural skin tone, balanced lighting, no shadows.
- Neutral facial expression (slight smile allowed).
- Professional look, no accessories (remove hats, sunglasses, background objects).
- Enhance sharpness and clarity.
- High resolution, suitable for official use.
💡
برای بهترین نتیجه، یک عکس با نور مناسب و کیفیت خوب به مدل بدهید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6814" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6813">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📄
olmOCR | تبدیل هوشمند PDF به Markdown با هوش مصنوعی
یک ابزار متن‌باز برای تبدیل فایل‌های PDF، PNG و JPEG به متن و Markdown تمیز با حفظ ساختار اسناد؛ مناسب برای مقالات، کتاب‌ها و فایل‌های اسکن‌شده.
🚀
⚡
ویژگی‌ها:
📝
تبدیل PDF و تصاویر به Markdown خوانا
📊
پشتیبانی از جدول‌ها، فرمول‌ها، دست‌خط و قالب‌بندی‌های پیچیده
🧹
حذف خودکار هدر و فوتر صفحات
📚
حفظ ترتیب طبیعی متن حتی در اسناد چندستونه و دارای شکل
⚡
دقت بالا با پشتیبانی از پردازش محلی یا سرورهای vLLM
🔓
متن‌باز با لایسنس Apache 2.0
🔗
https://github.com/allenai/olmocr
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6813" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6812">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">؛
🛠️
OfficeCLI؛ هوش مصنوعی برای Word، Excel و PowerPoint
؛
OfficeCLI
یک ابزار متن‌باز جدید است که به دستیارهای هوش مصنوعی امکان کار مستقیم با فایل‌های
Word، Excel و PowerPoint
را می‌دهد.
✨
قابلیت‌ها: •
📄
ساخت و ویرایش اسناد Word •
📊
ایجاد و تحلیل فایل‌های Excel •
📽️
ساخت و ویرایش ارائه‌های PowerPoint •
✅
بررسی و اصلاح خودکار خروجی‌ها
نکته جالب اینکه
بدون نیاز به نصب Microsoft Office
کار می‌کند و از محیط‌هایی مثل
Claude Code، Cursor و Codex
نیز پشتیبانی می‌کند.
🔗
GitHub:
https://github.com/iOfficeAI/OfficeCLI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6812" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=V0gJjkacoe3WO3oZ8QtM7SqcWdG5rmxS0GKK4g3Jy2ug15HGVVrd_SFJZTsX8Agok5ah-PUQQZSPMpBFvLxjn9LdHonnvP7-RtWUp818KrmjMyMmOPJCfC5T6yNiMRTZUvVkCaqHf3PSkiZWkIejgheEYxwP2Uv33WzlpCqXHNyPgzFFjT9fwZWmNzo60rtgkXEQ9THZeK1cCjJThSV1eIr-Q_9PgRvIN43frCM58Nk0-J0SG0ugPEg4k8V1fkLgL6WtqmoG7zuNVipzo4JyHNOOo7o59nNpEVxAdw822IQeDzndeCPhgUC-jiJFihS6VNK9AF_jpHb4wIZz5oT4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=V0gJjkacoe3WO3oZ8QtM7SqcWdG5rmxS0GKK4g3Jy2ug15HGVVrd_SFJZTsX8Agok5ah-PUQQZSPMpBFvLxjn9LdHonnvP7-RtWUp818KrmjMyMmOPJCfC5T6yNiMRTZUvVkCaqHf3PSkiZWkIejgheEYxwP2Uv33WzlpCqXHNyPgzFFjT9fwZWmNzo60rtgkXEQ9THZeK1cCjJThSV1eIr-Q_9PgRvIN43frCM58Nk0-J0SG0ugPEg4k8V1fkLgL6WtqmoG7zuNVipzo4JyHNOOo7o59nNpEVxAdw822IQeDzndeCPhgUC-jiJFihS6VNK9AF_jpHb4wIZz5oT4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛‌OpenAI⁩ مدل جدید ‌GPT-Live-1⁩ رو معرفی کرده که مکالمات صوتی با هوش مصنوعی رو به سطح جدیدی می‌بره!
🎙️
‏این مدل میتونه تغییر لحن بده، بخنده و حتی وقتی که کاربر ناگهان حرفش رو قطع می‌کنه، طبیعی‌تر واکنش نشون بده
🗣️
‏و اما یه قابلیت خیلی جالب دیگه: میتونه به صورت آنی به حرف‌های کاربر واکنش نشون بده و حتی به عنوان مترجم همزمان کار کنه!
🌎
‏همین حالا از طریق ‌
ChatGPT Voice⁩
قابل دسترسه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6809" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎯
RankGrow | دستیار هوش مصنوعی برای سئو
ابزاری هوشمند که با اتصال به Google Search Console، مشکلات سئوی سایت را شناسایی کرده و لیستی از مهم‌ترین کارهایی که باید انجام دهید را ارائه می‌دهد.
🚀
⚡
ویژگی‌ها:
📊
اتصال مستقیم به Google Search Console
🤖
۷ دستیار تخصصی هوش مصنوعی برای سئو
📝
پیشنهاد بهبود محتوا، لینک‌سازی و سئوی فنی
🎯
لیست اولویت‌بندی‌شده از کارهای ضروری SEO
📈
تحلیل رقبا و کشف فرصت‌های رشد
🎁
۵ اعتبار رایگان برای شروع (بدون نیاز به کارت بانکی)
🔗
https://rankgrow.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6808" target="_blank">📅 07:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کد نویسی رایگان با ابزار هوش مصنوعی FREEBUFF
💻
ابتدا به
سایت
بروید و اکانت بسازید سپس ابزار را اجرا کنید
🚀
— نصب آسان با دستور npm install -g freebuff
🛠️
— بدون نیاز به کلید، کارت یا اشتراک ماهانه
🆓
— مدل‌های پیشرفته از جمله DeepSeek V4 pro و Mimo 2.5 pro و Minimax M3
🧠
— دارای یک وب سایت برای تولید و استقرار برنامه‌ها به صورت رایگان
🌐
کد نویسی خود را با هوش مصنوعی و به صورت رایگان انجام دهید!
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6807" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6806">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎉
Claude Opus 4.8 رایگان در
Supercode (فقط یک روز)
به مناسبت لانچ Supercode در Product Hunt، این ابزار دسترسی رایگان یک‌روزه به مدل Claude Opus 4.8 را برای همه کاربران فراهم کرده است.
🚀
⚡
جزئیات:
🆓
دسترسی رایگان به Claude Opus 4.8 برای یک روز
🤖
استفاده از AI Agent در ترمینال
💻
مناسب برای کدنویسی، توسعه و مدیریت پروژه‌ها
📈
؛Supercode
تاکنون به بیش از ۹,۵۰۰ دانلود، ۸۲ ستاره GitHub و ۲۲۰ کاربر رسیده است.
اگر قصد دارید Supercode را امتحان کنید، امروز بهترین فرصت است.
🔗
https://supercode.sh
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6806" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromlocalhost(Yousef Taheri)</strong></div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6794" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QleP6mR0yVz6feReZwnBhTfnfaKXAifMvJwkoJ7rbKhtjN-E5qfuv8dfLWzQGUEa-to_goAgfZHrgc6n_HgQFFaU5iC8CLmKvD4fvSiGblL1rF77sU1F5Wg5nWNrLOFdB8gv5IAn3amkU5vXlM1ehz23lPGAespWQ4wt3WNMbUXfB-P7lifMy-WxBO78BvIdzBKIgR7zGFyZhup5XNZxRp8rHTQJNFuxYLBiUvU_1lXLW9oCUVEDzNheXtxFDZFo7GZP5w-VQI-yogBU9hS2Cm8DjNumahK5lJtag0ncda-HxP2fuCLUe22A78qnhu_Z6wmCQfB_xsnH2lU1mCD0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Grok 4.5 منتشر شد
⚡️
این نسخه محصولی ویژه از ایلان ماسک است که به‌طور خاص برای برنامه‌نویسی و توسعه‌ی ربات‌ها طراحی شده است.
نکات مهم:
• این مدل به طور مشترک با شرکت Cursor توسعه داده شده و با استفاده از داده‌های واقعی میلیون‌ها برنامه‌نویس آموزش داده شده است.
• سرعت بسیار بالا: 80 توکن در ثانیه.
• قیمت بسیار مناسب: 4 برابر ارزان‌تر از Opus 4.8.
در حال حاضر، به صورت
رایگان
در Cursor و Grok Build در دسترس است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6793" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">#اختصاصی
شبیه‌سازهای پلی‌استیشن
🎮
PS1:
duckstation.org
PS2:
pcsx2.net
PS3:
rpcs3.net
PS4:
shadps4.net
PSP:
ppsspp.org
PSV:
vita3k.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=L1SR2PDlcxXdpzwwMnwyrEdhjD6dx4SpI1l3stf68U3OeTMkIKJalRHH7HMWYLqlCWWuYu20HWB4spGzLLvsqzwh8qJ3ouT4F8bQm9dc4w_HyqVTVFaLgntmWdO66GiNHvGvMFCZ-2eFIJHIR110Aq2KU4pgI2XBB7-itNyKfFhbjIInxibDlvj1KcFY76syrW5ipgMk_nHl1b1xmYlpaGu0zQ6a0voSE1AMYD3l7osFKQGDJIqGn9CXwB6pieex7gCTOhdONaR1wB-UvCUv-dBVe15EmqQC_da69Bfm3fg5XuoW8mSsOwlmhC_X_scAlXUBV0IEKU-eFW24wWIdWlCGRwCkwSsGWkfIy9COu8dW3k_0ABHjXBu4YhMHrq_nhBH5a3telMIdvBHZr3r-XiOu0OY8BjSSS0StJho3o71-nBwml52a1UnzHbToXMfpYMHSKpAuhUCUJYcD4Oa1lLgP1rxhNqsrzb-zvar-Ol9-O-_AlDI8FniCF0Uk1onZTRNWRfPqQGMVo79kuf-P0otT35YdDSi6050KYwOgWNh1o7ESF8e2fWe4OPZ9txQy25LOX2sPbNBIPMwDpCQtAJTv_l5d1D_SeQaAa8betzfZcZRJGdFCrVSgMRy-phIeEtle1Mnd5BrQSKNfCyexHC8ERYl0OiP_TgqvR8uyiMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=L1SR2PDlcxXdpzwwMnwyrEdhjD6dx4SpI1l3stf68U3OeTMkIKJalRHH7HMWYLqlCWWuYu20HWB4spGzLLvsqzwh8qJ3ouT4F8bQm9dc4w_HyqVTVFaLgntmWdO66GiNHvGvMFCZ-2eFIJHIR110Aq2KU4pgI2XBB7-itNyKfFhbjIInxibDlvj1KcFY76syrW5ipgMk_nHl1b1xmYlpaGu0zQ6a0voSE1AMYD3l7osFKQGDJIqGn9CXwB6pieex7gCTOhdONaR1wB-UvCUv-dBVe15EmqQC_da69Bfm3fg5XuoW8mSsOwlmhC_X_scAlXUBV0IEKU-eFW24wWIdWlCGRwCkwSsGWkfIy9COu8dW3k_0ABHjXBu4YhMHrq_nhBH5a3telMIdvBHZr3r-XiOu0OY8BjSSS0StJho3o71-nBwml52a1UnzHbToXMfpYMHSKpAuhUCUJYcD4Oa1lLgP1rxhNqsrzb-zvar-Ol9-O-_AlDI8FniCF0Uk1onZTRNWRfPqQGMVo79kuf-P0otT35YdDSi6050KYwOgWNh1o7ESF8e2fWe4OPZ9txQy25LOX2sPbNBIPMwDpCQtAJTv_l5d1D_SeQaAa8betzfZcZRJGdFCrVSgMRy-phIeEtle1Mnd5BrQSKNfCyexHC8ERYl0OiP_TgqvR8uyiMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چینی‌ها یک "غول" جدید برای تولید تصاویر معرفی کردند: Seedream 5.0 Pro.
ویژگی‌های این ابزار:
🔹
ویرایش لایه‌ای تصاویر
📦
‏
🔹
ترکیب چندین تصویر در یک طرح کلی
📚
‏
🔹
تنظیمات جداگانه برای سبک هر شیء
🎨
‏
🔹
ویرایش محلی مناطق انتخابی
🔍
‏
🔹
تغییر تصاویر بر اساس دستورات متنی
📝
‏
🔹
تطابق دقیق‌تر خروجی با درخواست
📊
‏
🔹
بهبود عملکرد در کار با متن داخل تصاویر
📚
‏
🔹
تولید اینفوگرافیک، نمودارها و سایر مواد بصری
📊
‏
نسخه ‌Lite⁩ رایگان در ‌
Higgsfield⁩
و ‌
Dreamina⁩
قابل آزمایشه
📦
👀
‏نسخه ‌Pro⁩ از طریق ‌API⁩ در دسترسه
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6hBrnyqcmAFQS3ileBhxvg46XkYz9TMb1liIY4WjWlS3XGR2wrtK53oVdZKHMzM4aNOlol1Z6ObMpLe3kxvlA34tUXGeOdkbxfqzfyFh2MJgjrFkiBFNscNtb_IMM8xd6MtWAzNnsPmeuRwRHyIfiZdpXcyPg4mNNUlLcsLfJ1F9fQ_lYentXd8hvw2Q9HhKYfp7fMhF7PJqRxFmjwnhaaP3-yNhxu-WgFkAN607HoXuQDdR1QBLvsgPtYoKryOe9i7q47nd7_GgKlHEjfcx8oKeBYsFCqc6hVzta8hxcIWdKLptPPxnIDwkJv-DIZLjKonO5vmMeZbd2LDaE10IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر
DuckDuckGo
در جدیدترین به‌روزرسانی خود قابلیتی اضافه کرده که امکان
حذف تبلیغات ویدیوهای یوتیوب
را فراهم می‌کند
🌐
این ویژگی با استفاده از فیلترهای
uBlock Origin
کار می‌کند. هرچند ممکن است در برخی مواقع
زمان بارگذاری
یا
بافر شدن
ویدیوها کمی بیشتر شود، اما در عوض می‌تواند تجربه‌ای بدون
تبلیغات
و روان‌تر هنگام تماشای ویدیوهای یوتیوب ارائه د
هد
😎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuYVUb-wxixIru7qJwzeOGM4bluf5Q7IiwJKKkDC4Q3e7LrEyabjl0gFOKSpq1B9EV9BMMzdlRcp4Cb0HtxXwag2__7ceB7E00SrfrzcazQExqFtMutiSFBtUCe1oIogYYv2eCPE9PKGuCTRsDL3BLhJJ-ieuBINBrYE07IEEOPVx1m4wbAHGTekInjup_Rlh4t2UPpBQ6-snzqIMR0TyIW3S0-jxrtaWzfgHAEVcdg4u6bVSpFltXUVG-FDoK27PDSm57XQDVcor7C-r2NuYLsWZLCxG1_Th6iPHFVj8T9tMpfT0nh0c4_PmouvAOC6QfhLBh96EPF2kE9qrOufsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdaKahOwWD3da0JKDn1VQx2bvWR1A278V7lHOndS2Cpbqd_O0UvDABfDT8pmRmbdtzkh4Ha_khru0XAkEvrUR5xGI1-2kL_d_GDhXw2daaMTByHzNblS4XGLzFQ6u5v0hchsPvxCVGcIBsE5oVRuxc_Y-ICcNlPGAKdulBu9AZY4qkDaWBpePN9tqmFerDbhYy3ZykWeLGinlP3QugJor6T9jr689qAvBDJ5nkRbuiODuuFUC-7LbvIerRj44X98dVFFilSEjzdPW-VRnbDO1Mgdp2IdXavav1jgqj4cqTYwqsK8NIq3yGC0rsuTuVNqmXaXo-YVMyIOErc8HPutLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8dOumigYfPz0IIIYA72g61LwysRu8hmS3sujLtBq5Jf4djtFhp-AOzEV3WQxSkk4QCw6yZxt4JhO7_ssp5RyZWoQoVI0UpDWlMYDML_HrEES4QXz9cImGtzh4EXfR3Y6L0yHt_bIvz4SqBkGCMbokMAEWlMkNgCsG8uMtCOggiX32-w8VNobf-EEIYZz6RNncikoCRBxSyCofITT_PQio_7FD3VAnZGtICrZLA-yddTuwsDM2_DOTjwyaPuCvKG4cT3t2JwlP50WK0enZPdTyJkVnPxTlnm_H-aTOuUZ2G7e26irUUnmRLdlsdJsV22vYsJXHB_uf2C-WJdz7Egzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpYxtFGztQV11IhT_ZUEnyStKTjWI_fFqhJJQPwoZNjOTYV197Cg6y-6a-LLAlViBuSXbxe6Hcdnm0nPcVSTwtwWu8fPqD8U6z4doeeqsK27tmEqfxlyV5uJ-4spaHCcbqDWNRDD3KRj2YktezN9HJerFJgF9kEbPFJZQxiXXsrrnaqLcZNDOKPMrQQSCz5EBDsS-SPOPzAxdEECPKIUCakvxzC4PWvLJV5ofoPf4hEv7-VhwHnNKbkyTGvvLlvE8YKlcjYKNRYahCbIgK_V-AXEscBVyBWWNieKfscAU1htJw7Xswh73GyBo9yhbWsy256XK_gaJMCSJeR3GperSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_c-_okct3rYmA-Py7fDyNFvKJxnblhB0DLTim3Wsl4-fCdn99YZwh4Nz0Bq5mA08fF4uhu5KnW6dfqBWXqIrnmg1oS3BM2Xrer5trMbw49AFWGBF_EHvw-8Hdo4KgaJn1ZyAH8_YsOCcvK9laprcQhR73yni-eYihZOeKffDh8ora_EzBk--hyBZj8Qjt8X8jIYHkTba3Wbe2hB2SD5JR9AKgXLHv1VrXwZpvBK9YkjqFeED32hopPhOum84gS6op-VFsHw_eqqumAbHBJeNj7BRabiryQyYeKVrEMytPqZUmrwywvRPByxOnxZayJXhcD2lIih0CyKkHhdNqUOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3zkiyE-K0GzNWhDHUMavanLt6kgA2gbaUW_F7LZYaF3-oemEvVhyVRmIjtQ45xeEXX0VcKPRTJO2wh7GcVI7IAh6kmVShL_4bVWh8o2aWslTCy7AIZjG9zpJ-illZ0iTotqNSm4NJBMSz8GuatN0DfPdSzaEQp4ynfXga7PmtsUgDjFrZF_Bmivyg7IQZHbaxKOpALmdpZKyxnaaAnjleJDRSD9nyrLGgk1PDF9LBEbv13dreafnY4TUj5XG-HXylx0QnGKQ6sVWNVdBmeclB1JQc15FssAWIaPqW4pjisYsSLdFFgRIsp5hJBH8cWyTrA6Qy77Y-yQVURsUE8sfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnXaHWi6AMrB0nPOA8jkGxPsDAF54TctcgVigVZpVakkp9Xd5tDqME2-oMfHx2SSI9Sz4w0btNahpGdtKnkbit9IRzYcp6amuQUZyHmjcJ8sd_V98hVsDb2-udCD2dFTMe6EWbUYMKPBGpsEffLycXOb2VJ3MkbUIFQDkd2E-LAyjR0A81JLRxptaYgerpY98hmbarTaRTVSixWemxBjRBNVJZkoD6mu_ZBTHgJsvBPfqFbvR7hSe_Is5wshWWt7tNmGHV-GtXBsM0Rrc3ywqEyUJuH5QQJR1E9HSrK-any1lvyOATgCmxsBIu6MMViG3nuHB9wcGLxcJ0pE51Yw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3rLQ-ahcs4_6djRO_XMJnZPZ-OGe14d425n7dkQtcY5j9ZoIuSRODXHVdLrhNYY-oIjyMTjineh2hjaTjDT_T5Z-hrb_Rg__VoD09lIr7ieu4rQPA9n_cMOEH6iHlFICedtIxnhqJkhmGfDwDjeuvTXYFXmBH7smSH9ytczkUJdB4eWtJgPsjTtO1-1ry61zwfMyVaVdi5L0OpjyRJr39KP0Wd451QGuplT2rsHyiTRrKtE_hHAzw2bbC9AQrlvUCtDI42-kakw4dfjGj0IPf4hV0xuhW5N2FyOGlx-kydxjO6WwnNkVv4riQvSNNVaiBppWNmaLM1M10Ewsmoyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqqwbh1JMCmD8lTqfjeK2NrPsbZef33lWF_27KdIG2JS9wzONjNKBSA4-O3YYsb5Rhg2KWMSRpT6g5Nl11bjK21lebhXSQOwrmzv63E-fNcEEpp8rvBf-rmxEZZgssv1habq6bJ8MkRmJLSLYYw8-zckCa4VOlrMrtgRv8HGTyQagYz4qu1UYkgPELwhdYjknswx-JdQ8v0xuTBpT--9Fq8Jt9w_DfVSdDJJMhIi5dMy7m1ZtBH5fgyHE0PnEbxHHc6GwxWzMqL03ztP9MoeeoAXDlrZUQwFlFu_tlbc4T90u0AWZAI8fa_Tpw-0azPXOiWG9rCoG2O0QPPmmO-q8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9gLsm4fsdEp0657JwmVRBbiONxjAce0XTYISs25HZephUqO4gCdj3S7RKnLHX1dzTHD8W4obz2ZNiOwdgn1QcR4bmQo1EEvMQGMYJjjOrmthFRwAjrys1oynmwP80-DIGEORAMXyoRwEq6sdM7aHAWPHHs3qlyD6cDPhgE9xKFOoSjcMsbXNlvSENtzGxRKxTnqdK5uLZ4zFQtPH6t9esb5Qp4CkYBwVd1losyh_5zPOrisOGgRsIF8KApbpfyHUe43xXp96GJVmSBFcBUuPqYQYfg-pWQx1Fhfo7Ajd5HPbycGDYnaPwjMk0gjZlLE2uzsCb_RzjXLT-vV7jvHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBOhFXQtVkljl4apzRGJfIGu6ykzgLzeNbnW1jcrEg2JjOEzKLPo7_4oiZYa_euSEw1pLTEeA-D8HAAzgYF0SfICMer_QU-T9A_wlDngL_MA9o8BJcg7GpraJ2wChCZnNoPJqii_-2tkcWLxsBwHP3HBA4CO0ONdWruGgxDUcOAzIyUGKqqp9uUYEYHe29ZcmDUX3FpxP7YWz1oCYXt74jeyV4-zG67qxwv-B3r0BHDUWbAxWCIPLyQz6tCgZSdiNkRcf9jdxnvUSqk6o_SvzkFOT3avUEu3AmTNA_AqY3T8wXy4kFBLxc7nyUlDZaxwjc2zhxQLzynLi5gjOL51TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srpp5VQkCgWHM2OLnlaody68BnUMaQVfuwWUgDMQbD_C3oqQElQk9GlGvdx0diSwWCAYGSiw3SyD4DgK99YLF9TlHVyLRj9NpcQUkZoodIA2twKYQCa89-Q62RH-JcNZZRhMHmlwXP3E_v-zN_U40DYR-Q-cjj3q8aDLSg3R-nXHkbhwRMYNLrrv_JuHO6wXHTPJGMV98ESYO-eQkBjyfCj5diTSOSLrqT5A1bTAmz0rEz2GU4WXm0-K5RJj3ky6UZBjYrniNFOOg8INkxTR85mo9UE86Skui7Q2p2sEQu0CfW25GIZ1mO-zMXeHc23AZaBC6l5cbhv9HXvzedPn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsPqYmGPYj-yHUMYYTlUxJ1YX1yjOPYNQ3ZbpOF5JTofCUoYPFuQQ8LTg7AHnlWVmBleNYeuQZJI20TgBJBK4LVTHGjccyYhxt9Rn0Yo2_m3C2W2IddX6EwIhdaoxA21RaFTFkgjgM-TIUEsoU58sPabfOzPNrhX2Hd_OFmQGMKrBnhfwzz2x9jLxk7shg1UZluZ1OGWNHuxPvCAqPaW5VGh2UBXyFaYFIkrgFcMH6q982DMVE5fccX614Ni2tndrDsPkcifHGIIQBvFkS7XIooSKS5Yi75hMYMW6UG0jU-V-B9k5V026nuCUYzmi7SmG45ggk7jFR9MB8DwoM2iPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=ss0ziuENGjtuWdLNYnX9txQuacDPtoTLOpyVJrQmWHDTN_z3WW914S-f-pqt28BrOXxH8HXhg09Acx1xuX88BvD_29q9CK2qsdJjjOv8h3xa4JzJKkd67PE86JHYhgRaplDXgoDq4OfECOzfvHIhINj-snQqqEIXvSALlWTumWhoj4ZmsqztUGgkLQz-s9Mnxcx8yzDcIm4qYewyFm8j45pdjeu57okF4NQKGuGxNch0XxbXIJ72eklycDfZgb8sctGw-HccxXH3iU-MhXmAgIzRM2q4vtG9mZiahgcwnItm3qKWYLbMCp-h75mZy9a08HYJiRQofk-2PPEG6XKtsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=ss0ziuENGjtuWdLNYnX9txQuacDPtoTLOpyVJrQmWHDTN_z3WW914S-f-pqt28BrOXxH8HXhg09Acx1xuX88BvD_29q9CK2qsdJjjOv8h3xa4JzJKkd67PE86JHYhgRaplDXgoDq4OfECOzfvHIhINj-snQqqEIXvSALlWTumWhoj4ZmsqztUGgkLQz-s9Mnxcx8yzDcIm4qYewyFm8j45pdjeu57okF4NQKGuGxNch0XxbXIJ72eklycDfZgb8sctGw-HccxXH3iU-MhXmAgIzRM2q4vtG9mZiahgcwnItm3qKWYLbMCp-h75mZy9a08HYJiRQofk-2PPEG6XKtsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrbdxFhK1bpYZUDkf16uKSVDw3QtLe_7LA61mWmjtAV3qklK8I0H2w4A2aXrubgQq2zpjDVS2MLbqaGCMgtpY4zGp5QyKvRhIfVFylrRnXj9_DF14lIbfMmMreH0W-Tncayt86kFIZF57ncr8pVpfOsE_pNpwq1rKSt-D7nbrmkTAQCvPFuZoVFWROvxdGHuUIPOkOa2-PU8euCR0tqnuOtw-ppUaZ8yVc5V7Tbj39pU29EMeUc7Y-agteyl43NhD6j7DDDeXTpalaDD3MR0P_OIhVF74DIIXjTK5HFT_rYPgAQV-xog7HtRacpSHHxi7qexC3Kelr7udlWs1AYyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-eE5OI4RYcfOUBaOi1DGAdCSB69xwqi0eRME26QBBhD9bqx1ucEayqk3w0HwVmuoIMQnKzD70yn5DgBeYqUIeMQEpUWVGa0szT9iv8Gp4YnGAqcCYkkk33qxj__xSOgWoCbgtONZpNoAwFcyB9NNaHMHCs4RC7hMNtPToM5YYHBbHEgtCed8scjKn1mG8znvn3AqO71Sb_B-KCuYBkwO-ULhN0w6HYkcyit6Gq_4Qu9UgjrX4oXPoEkqGbM98kigxfiSe9g1RmJJPHd-C7rculTej9HvwQxXpQhQIa_r-aoyCPIqZd5cH_6zVyOc4RWA6hQrCoBSt8gxttfiYTtxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvXAof3984NF3km2Lv4OMWj3lRrD1-9vkP4TttotNPmyNBnha_S5JaorEzBkyRhULLi2FSCMkfn4017DwOFpSneqKX9bhZbouxrK04-1oiYnlF_wUrLnNU3fmwNPujhNJrl-pT31W95tqPGxAYqxxP0C0qdT-LyxVGys3TvCY4LcxcB7zlXSou64WSDlfp_56JRikOvfkC3xaRtNh__VW0Zv-TjAH3tX7ILgDf9R9mFgAFZ7vPYDE7OdARhAmB9z2C_dycpDhjYejQpJqN1uz4qc-bwEWZ9s8VMqTPWCCVk7BYBFlXtp9HWURmZDuF-x8Y5twi8_8RjbTsPgZe43aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYSoDHgs_9nQE_IekyXRMxI2nYXTx-iqowppJNP3viQYfOl04D2tIJWo_2yMyHMjlPzCgaOudvJS3CBVy25PsPh8ouVqNU_ZYyarMaQY4UZj0lS4suP1zOVP-XKctUSFS22vyaxGrpiEB47tXkwsBHKu1BBFeAnt6iAgdq9gZHAJtQdOogY3UvFROdns0ugVdz2W5zxaYPOTt-o-LPq6yNNlOCFo5fAR0M3uXix6OmNUU4lWy3AP85H3K3qAUR3_Z1sypsf75xgD0upBpKH8LIH1RJ1KEoUnrHyBNOgD4JAkj7eQaYoD-TUFCbrqiIVmjjyBVjPetd-WuP3s5L1JJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlQg5E-ASmnq2sYG_OE3NShnE_TCcTPqZ7hELTaJ0KfhUEoCRLfuMz9y32AIY8sxGhQ2I1wlzdCoVaGQPiTBkZ1VQ6sWGkpSAFLjhsvmlckwkpmdgy51QYc_WBF3vtu1s9dyY33kHnpo-bi-LKpgVU-S-5SNxCvZB56rzpe-o3bmN6NZdkk8WkqGYNeVCCRW4_lvT4fNYrKbiTbWHFVBtE4x1L3QiWglmDI8Ydeap0FBQBN4cAUfe8YSlj5gXTHquVYKApic6z51S6yvFpCvf0f3cZxZndu5ez40H_gnxaTrnWJDbH4O0M7F9EQfDl2fknbaaHQ_IETLETnGcingnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=ISWQvc9Rg7NXeRw9CAjM7J4NrqTQYJIp0PDjeFHMVZDDc82uIb4LyXCrNig7vqkdlvA96o1uwUK0TC6LRQok51Hf4fZm5Rcbw7yHJj-mtV59PaSUgS92FAbTHriNuw8tQqx8BrXG3EPoxmskyFiKf3LIgxek7tkZrAfVGnpkOSSmG6tkqj1pPBk2yPciaV8RF9hekWOWcap6Bpv_hPCsIOml8yyY_QBl_aFJJBs0u8Gd-sjDej4d6Bj1NxtuVYKfE8NG2pWZp_Ef3VVq9qp-LHj48W2J1Ls1NVKOcjHnWHegLf2k_t_fHlq7G0HnaHCdiDPlGXukzlATRGs_eLXHfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=ISWQvc9Rg7NXeRw9CAjM7J4NrqTQYJIp0PDjeFHMVZDDc82uIb4LyXCrNig7vqkdlvA96o1uwUK0TC6LRQok51Hf4fZm5Rcbw7yHJj-mtV59PaSUgS92FAbTHriNuw8tQqx8BrXG3EPoxmskyFiKf3LIgxek7tkZrAfVGnpkOSSmG6tkqj1pPBk2yPciaV8RF9hekWOWcap6Bpv_hPCsIOml8yyY_QBl_aFJJBs0u8Gd-sjDej4d6Bj1NxtuVYKfE8NG2pWZp_Ef3VVq9qp-LHj48W2J1Ls1NVKOcjHnWHegLf2k_t_fHlq7G0HnaHCdiDPlGXukzlATRGs_eLXHfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPuShLgl6D9s1eml4y3wN_a2SViI8gjExUGvfCi8V3HLUomgD74mKxSQd_wMOzPWDiZrgupA4Z0Q0Y9JNXlcFvbsoFUN770P_Qw6QbqBqepe74hhzryKP4969ll63nqaW9Vk9DLakgsboF1R-oCsvlQrOE1QD4-ae4ce7vhM9-oIvmFIEzk04GXYG6b09Kao9sadY3Tu51vCh_eoH6eklwUOhvqjXE2TqPp6_zxGeiKtZES8X2G-i6VDNUfwZk43J5WD2dx565pUCxXFplT77CYUXfIA793AD1EIPxAXlOTfli5ZsbXx_awrBCxG1OsjURodFG9-m2sUgITxDi8Waw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
