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
<img src="https://cdn4.telesco.pe/file/MQV8QfIv5h66PivvoKpqYQjDY6GLVOW-7vzZtw1jJbhNO-vRydOzyBWbcvoc5hgYMg6La90Ma7JEEraJIP-Cr8dZPxojHIhNoECT_drB5RyR8JtB_g9o8iQkUJN4QYZmyMsECSX-MyRxz6mpPJMRa7M15JV7yTbGpuWMmHmloH4EQfJJT3-qfI6fhrBSeXtgik14VILTlOb5csdoNw9mxqHBAR7-RrtgXSVPEulO-YacPsBvNa4Vj73a7p4LpmQ-AxFpkqXdq_Zm0WtRNrtYsB_nxNhx4EpjfjXqV56snKNg4L2y_H1i6KgmaI3bjWE9FBpwPz_JK-ozEs3QGyplXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2b2TSyixxHrfzK6M2ffLCCBq8v-8Krt2UzLUAa-7RG7qPR7fv-L0rbzBI_3oOUCssICRqr3qMS1FjUtACbuES4OLOA78UpKONMEv0M5-FY5GYwrkN6MzF-5dBx7YmaqeKkgE5wHBYSZpP-TLv-vljNWGL06kF4XwrHAHxNREiDAEt5fQ0KdihD9NMkBxE69E-tM8aKTNFQrpvfxGqqKY4_V5VDcuer9lXlnWwoRDzwBa7tDIXcAQm5LjNNBftUNBuT--seN7CLSGFveoYAG5_vwm10uvvzIX3AziLlgJW21JhtkhQuvn5dh3FTe_Uv3gnNZJKbT4gb9SKD1GoSwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاک کردن واترمارک، افراد، اشیاء مزاحم، متن، برچسب و غیره از تصاویر، با تکمیل خودکار پس‌زمینه توسط AI رایگان
لینک:
https://magicremover.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 569 · <a href="https://t.me/ArchiveTell/6637" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVBM_fNt3NnpPvHNWZ5_Bd4E4TayMbqKmOIGyb7KzOYh7I2DxvLQKb2mhLhoCA9uzSh1G_1wySnkfNYDEk5lgTI7lnKFNtrg_h4q2l0pHqKjhx4TGT7ufibB-svsuwu9MP9BCGbegZYppnT_9sXs3CImuIQt99leCKOgKhhoEUjW04Fs6KrvBCQaZ3pTf4eE8T0t8SHTAd2BkkUJbfSoKmigotN1yBQ5Yotir3-lJYnU1mNkk8r-vP2yWhYAASjA8atf23J9sPW-uKgAJoOgK2or7WS7RXIyL2HA3kgZDF41Ph5KSqZZI2KrlNIjT1PLu-U7sXXBAQFTDl8RjYdvjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 935 · <a href="https://t.me/ArchiveTell/6636" target="_blank">📅 16:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWwCtTz_BVjwwC1yXvHsGkBkYb5HJE0wS1fDmQLK2yW2MVXGzDIxamLQ2oFHBhoPHIeCiV8IFswGLjtwsqDZPt5G-Fs3x9u_GC0HGWIJxhoJh5SUciKK0xBQ8975dafUykNlGAIO5iQ_la6gDIwQ-Vs_YnQlLNnjHCBdfpVJPCftu8fZRDkHSOyY_vR-avC4X7KekpE6SC8DtEXpbbpVGRDVoszrzEp3JMvNkJkPNBV5x5RkjKs0lU3LYLYQIX7Lwl8MeLsOd2rKZmOE1GGzF2NhxAM6rX5kd7N9Hbxu307JDrUEeH83r1VPSMer6GL8Cp2T7yR8wv15CCIYP4VVwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/6635" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=UEMKpkkip-vmWagyJG4Tl4SPOdE-G63cf4zQXR2OO7w60xO6ME1lJPGByvfX-aUrZk0nE-jp7jRnFVCJw-NI4WlGpqOMxjvmz2GSWJC8msIiQ3TbN6aPvax_2WS1GAF6Dc5Mis-5cTGWEcAfsUpfxTQxWXDkagyE1CM_79RGOPSQEi6Aas3DQwcEQB_mqrjP6_cFkhWE0ETqdnTaBB7PXyusYu-Ghvn0Aaadp59kNyUtntCpV2u2D6GoBP0vwG1ITBxC0C44pOss4XnKfEltbnIlojZKFatHi0lKwwO_3s-LwCR7ozOMAmj9K4HSpicp4P1xcyvnp1_RLbP_Zy6Pow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b49cca50b.mp4?token=UEMKpkkip-vmWagyJG4Tl4SPOdE-G63cf4zQXR2OO7w60xO6ME1lJPGByvfX-aUrZk0nE-jp7jRnFVCJw-NI4WlGpqOMxjvmz2GSWJC8msIiQ3TbN6aPvax_2WS1GAF6Dc5Mis-5cTGWEcAfsUpfxTQxWXDkagyE1CM_79RGOPSQEi6Aas3DQwcEQB_mqrjP6_cFkhWE0ETqdnTaBB7PXyusYu-Ghvn0Aaadp59kNyUtntCpV2u2D6GoBP0vwG1ITBxC0C44pOss4XnKfEltbnIlojZKFatHi0lKwwO_3s-LwCR7ozOMAmj9K4HSpicp4P1xcyvnp1_RLbP_Zy6Pow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل تصمیم گرفته که پشتیبانی از API پلتفرم Tenor، بزرگ‌ترین مخزن انیمیشن‌های GIF در جهان را متوقف کند.
دسترسی مستقیم به کتابخانه عظیم Tenor از تلگرام، دیسکورد، توییتر و سایر شبکه‌های اجتماعی غیرقابل دسترس خواهد بود.
اگر بخواهید یک گیف انتخاب کنید، باید خودتان تصویر را جستجو کنید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6634" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIT0mQo1L3r-ChZ70jOFTs0P-odlCb1IwB2iK0R7h7LgLNkfdkjtKQy8YakOX3Eitl3x3dc-l12A2qNwrfvSiBhT-sfPAC6lEPlfD3mGnvWUtMBaOJ3worwuIZqBgohavO59GaBAXxKu-hea6bgEQ17EPMQLRzYOSlXKcMHaNZ5mEo2zT7MfdSmZhhIAxHe2-_aBIbNF7EJo1FlOnw8yLE-KvNOjvOFRRWlma0uNum2JsZ1TOu6bkBJxzjeYHQMlzh39f4bpNn97F24klzfqOTPckfM8gCxUvABAeooazc9gTxBHQ6ayViUN1Zl4jTbMfN19WKKcNOUmxlV8ebssjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/6633" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McTmd6--gk3OSkQlxf-HDnZ8BZohJKguK7xa8x5jdD_BEWogMeycdtcMvRuf45JoiOQHpvAUGnJhqsfa689iFKg-OADxKegEIMGMOUSafSHyKawHTezu0AImwDHXBfHf_0N-210zkZbDF6SKDBS3PsemDxBSMwJfxukb1mVJn9GgGtX_C8L92DAXzUB9ZkHp-VpDA5x2jyaWRd2TaMVnB3wtz77a-GbOtNloHxW24DG2TPwigxlDn_k_L63gmLxxwNLkJa_hOeoJEGUaw8ftCTcHz9-5rqy98QADp4W12z1KxyTo1D74zNFTIbOe0K4c5FdGr7lLt680lBJhXKuhqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6632" target="_blank">📅 11:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این هم آموزش راه اندازی</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6631" target="_blank">📅 05:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/6630" target="_blank">📅 05:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سورپرایز تو راهه...
Ren panel</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6629" target="_blank">📅 04:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px3hG0PNMQdjepNkBAxjA6if9ayTBuK_PKorBMehwUcnK4gvAdzlq9OHI2hXvrMezZY00WQOyTw2JWnoEu3_SpeRXCyeh-HX3Lr0pFnD1jS0-wzTgtrt5J3nigSbeK3tFBWBKowJRjlg0wRBUQzaPHwcgQz9s9yQN2iLR-Wcz0SXdS9giN1AnK3C8ZNi1uP2Wgkk0yeXKoYOzYLfMaq1dQRSKN3b6n41JTXM6KngXOqtRkYWBXm-4qB8fQQGA8gRwZgxp10goulaIaV6rzNEuQiYxLxOfjC3GeAu4yVH2JEy799sbxPUGexYPo6WqdxGh56zMWDkzjyNrVlRyCGXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتس‌اپ پس از تقریباً ۱۷ سال از وجود خود، نام‌های کاربری را معرفی کرد — می‌توان بدون شماره تلفن با کاربر شروع به گفتگو کرد.
تلگرام به انقلاب سال واکنش نشان داده است
😁
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6628" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=onTtqdEacw1W3Gz9LH6SPZrFCSC89X-GOv8zPzPIoya1NC99NiDmhHRHKi5v-Om9kB10kGl9ZeBwNG3NMi5UdhP3JxbJGBimQ0xZ0_V3fywzjOdrbmyFhGc1GZW_Eyasp5cHLck5uNIiefr6u53Op1ZvRTQN50ySGoFt2IO-CSCARYEgLL2BT-XEnQ4EQGp51cf17EVxtPsko_n6MezdvOHyIhNJ9mqFc_EBVl91pdeDTmU9ruk3gH4wWqSTKyjX7biZMy8GuOeEar5zvE5qrR0MbT_pB9OKQzhgeG4fM63V8iM5esMjxMJnHroUqIasnP_t0TfEjBtY2p_0NENVoWlid0w3dS83-M1Fr4HF9-srYqpcgdwRRl0RT-GdxP4u01M9Sf1iby-dAb8mNwP2YjG5JgIeTUmRZflvWyX_Sabo1y-9EUnoLwL34j6ZH-f-02J2fWig92RXH0juGvaE03GSqU2kGjErr-yKDXd45grJwprB0eg4OcwFdUwcYHcU01--E1X1zpBOcdiEqTVpZL3SgdhWTnHB5LqV_rMJJroJC-ztsyqnyc4GqyPayAPgrq6TRsXnQxjXDz0-y7PUuXm0_JqZ85QFTAaWh6n6L_vHPInoU9qthZ3cSdpzpQcchLHjbE9-TDlu4SjCTVE-ktS3LwLAorEJDLzqMgO6BZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c28976b.mp4?token=onTtqdEacw1W3Gz9LH6SPZrFCSC89X-GOv8zPzPIoya1NC99NiDmhHRHKi5v-Om9kB10kGl9ZeBwNG3NMi5UdhP3JxbJGBimQ0xZ0_V3fywzjOdrbmyFhGc1GZW_Eyasp5cHLck5uNIiefr6u53Op1ZvRTQN50ySGoFt2IO-CSCARYEgLL2BT-XEnQ4EQGp51cf17EVxtPsko_n6MezdvOHyIhNJ9mqFc_EBVl91pdeDTmU9ruk3gH4wWqSTKyjX7biZMy8GuOeEar5zvE5qrR0MbT_pB9OKQzhgeG4fM63V8iM5esMjxMJnHroUqIasnP_t0TfEjBtY2p_0NENVoWlid0w3dS83-M1Fr4HF9-srYqpcgdwRRl0RT-GdxP4u01M9Sf1iby-dAb8mNwP2YjG5JgIeTUmRZflvWyX_Sabo1y-9EUnoLwL34j6ZH-f-02J2fWig92RXH0juGvaE03GSqU2kGjErr-yKDXd45grJwprB0eg4OcwFdUwcYHcU01--E1X1zpBOcdiEqTVpZL3SgdhWTnHB5LqV_rMJJroJC-ztsyqnyc4GqyPayAPgrq6TRsXnQxjXDz0-y7PUuXm0_JqZ85QFTAaWh6n6L_vHPInoU9qthZ3cSdpzpQcchLHjbE9-TDlu4SjCTVE-ktS3LwLAorEJDLzqMgO6BZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6627" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اولین تریلر Cyberpunk  Edgerunners 2 منتشر شد!
🔥
انتظار داشته باشید که هر ۱۰ قسمت این فصل جدید،
پاییز امسال
پخش شوند.
آماده‌اید برای بازگشت به نایت‌سیتی؟
🏙️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6626" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حدود 900 تا کانفیگ مختلف
📶
https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Germany.txt
💬
@Archivetell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6625" target="_blank">📅 20:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#اختصاصی
🎧
استودیوی کامل AI: از ایده تا مسترینگ
۱۱ ابزار برای ساخت حرفه‌ای موسیقی:
🎤
تولید: Suno, Udio
🗣️
کلون صدا: Kits AI, Synthesizer V
🎹
سمپل/لوپ: Stable Audio, Splice Create
✂️
جداسازی/ویرایش: LALAL, RipX
🎚️
میکس/مستر: Sonible, iZotope Ozone 11
🔊
پاکسازی: Adobe Enhance
💡
نکته: ترکیب این ابزارها فرآیند تولید را از هفته‌ها به چند ساعت کاهش می‌دهد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6624" target="_blank">📅 17:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmwiptUFhoBdE96jTg_V7sySi-JDGmQEgbXG7EtjRpZG6ryQajfD5BkcTIoeNyJFURza8yGsyel-JAsNGumnSY0bf1PESZ6IloK6uCholbUF1-a4_3d1qzHs9tTA7sMhhnh-Mut7wPdQ80WVi6SswhSwuNyRPSUYaUWox5ExmW39b1nEaphUAn4stFNjE4pvFKDQV3Ig0MXpXBFmHrARIRJqQwIzi0pLYqECZHh88_PgJK19l5Lx_qqxHBcn9kYaF4QMuPBmhlwUxPQ4-RA-hiA2H39V7WbHluxN5aBX12pPzCMrGCD7d7_J9GWEa3Nk2sdcXtz4wPVVjk7y5Cmoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GTweak؛ جعبه‌ابزار همه‌کاره برای شخصی‌سازی و بهینه‌سازی حرفه‌ای ویندوز!
💻
✨
اگر به دنبال یک ابزار پرتابل (بدون نیاز به نصب) هستید که کنترل کامل سیستم‌عامل ویندوز را به شما بدهد، GTweak یکی از قدرتمندترین گزینه‌هاست. این برنامه با رابط کاربری نوشته…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6623" target="_blank">📅 15:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین   بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .   irm https://get.activated.win | iex   اگر کد به مشکل خورد و اجرا نشد دستور زیر…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6622" target="_blank">📅 15:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نحوه اکتیو ویندوز با اسکریپت Microsoft activation
💻
اول تو منو استارت Powershell رو سرچ کنین و باز کنین
بعد از اجرا شدن پاورشل فقط کافیه کد زیر رو وارد کنین و اینتر بزنین .
irm https://get.activated.win | iex
اگر کد به مشکل خورد و اجرا نشد دستور زیر رو بزنین ( نیاز به ویندوز ۱۰ یا ۱۱ به روز داره )‌
iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)
Github
😀
📱
@Archivetell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6621" target="_blank">📅 14:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حجم : نامحدود
زمان : تا ۱۲ شب
vless://63b43d54-3bdc-4d9e-b3f3-10163c892936@64.90.7.102:8443?type=ws&path=%2Fws&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF
وصل شدید بگید</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6620" target="_blank">📅 12:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puPN3hOGgKGOjKOpcGY-CFCHay1aRyGoTH3U9O7yDMbnRzi-Am4LwOSs4fq7V9ofu5fbKr64IFClzgrdAJH_pmxvRH8APyGE_yNZVeVpWQwQPTDh5ypbSNNbahRve9PM_am8nBsExGZNiVV-v39fEXZVHfFapUO1akCZOoIS4v-26e_A56U_oFkJvPMCw_kDGElg3UhCl4Mo1sW8AJWOSrw8wuDwc_jer5d_PIS4GuacAl3rHtje9ev6mze9NnE0CKNKnOkZ87wzVx8Xw62DwG10ZEyrCIQfEatH3B70iSq8rKMgqy22XojhWvOC5l3ZuTlS-4jNkPS9lRc0dXScdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راه جامع علوم کامپیوتر: ۸۰۰+ منبع از دانشگاه‌های برتر جهان
🎓
اگر می‌خواهی به یک توسعه‌دهنده حرفه‌ای تبدیل شوی، این مخزن گنجینه‌ای از دوره‌های دانشگاه‌های هاروارد، استنفورد، MIT و شیکاگو است.
✨
چرا این لیست؟
•
🏛
منابع معتبر:
دسترسی به دوره‌های دانشگاه‌های تاپ جهان.
•
🤖
پوشش کامل:
از الگوریتم‌ها و زبان‌های برنامه‌نویسی تا هوش مصنوعی و رباتیک.
•
📚
دسته‌بندی هوشمند:
گم نمی‌شوی؛ دقیقاً همان چیزی را که نیاز داری پیدا می‌کنی.
•
🔄
همیشه به‌روز:
نویسندگان مخزن را مداوم آپدیت می‌کنند.
مسیر یادگیری‌ات را از اینجا شروع کن!
👇
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6619" target="_blank">📅 11:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVxQN7KtWz8_SIwLxPN-h7xVGj3RMDfOLMP_DzDnZYElffZ5qwSMvtds7tm8X1Y-AkPXe9F5YeR7qthg69gl1mvxDag7emt7PscqVXYihveGv9Kh62xR3GVTJ0HQFzyDLDKnzFIMb42rkdXRZoXJH1VHP-peXvbSwc8fQJiFCwLA2BuumLCgmCH8eg1Nz06RRaO1uvb2FA_ylD20ZNxv8qff_2tBpfdwyqTmmOap5wqLIS7LfUnJ6LDsq11deT1bKVziwiy84mWl2NcFuCsLMwJkBvtaofrw0QnVy6tEsAoSL26unJ7s7Nm2to8JUUripNoZ9koYGcud1_8Wfok4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Anthropic بسیاری از دوره‌های هوش مصنوعی خود را رایگان کرده است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6618" target="_blank">📅 09:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1yiSp1NfqAfq32n1VaApcQQHBbST1au-pbPDWt6-Y-tcyOGX3qNmVHzs3bOSReUQ-iYEPiqHC-UHj3UTDr72QYbypOosXmQFzLrIeRXnysVB6ZQN4nfyVia5-yBYtuIxkel-8llJ0gcU7io8b5H2ptWPHG1pKQA5OQzcYWF_LbewRqRNISAbSs7N0829XFiHcKx5HCSjhEo_jr5Yfc5XPf8PPnk3bpqMjXAzVzsI9GGaGAg7Mw0OKuNz2va2lA6JdGMMjuHyxJWuRy6YBsX8HaY-ab8VitvmLjdatL1D1aGrsaiYMozKf4CqyEVt3qSz68BHAZtsQLTylT7cvozvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">OmniRoute
۱۶۰+ هوش مصنوعی رایگان در یک API!
🤯
دیگر نگران تمام شدن توکن‌ها نباشید. OmniRoute با ارائه
توکن‌های نامحدود رایگان
، تمام مدل‌های برتر جهان را در یک نقطه جمع کرده است.
✨
چرا OmniRoute؟
•
🔄
تغییر خودکار مدل:
اگر توکن یک مدل تمام شد، بلافاصله به مدل بعدی سوئیچ می‌کند.
•
📉
فشرده‌سازی هوشمند:
تا ۹۵٪ کاهش حجم متن برای صرفه‌جویی بیشتر.
•
🌐
دسترسی جامع:
GLM، Grok، Mistral، DeepSeek، Qwen و... همه در دسترس.
•
🛠
پشتیبانی کامل:
سازگار با MCP و مهارت‌های پیشرفته.
یک API، تمام هوش‌های مصنوعی دنیا. رایگان و بی‌نهایت!
🚀
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6617" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">10 میلیون توکن رایگان هوش مصنوعی Mercury 2
🎁
وقتشه ربات تلگرامیت رو با هوش مصنوعی ارتقا بدی!
✨
✅
مناسب برای ساخت چت‌ بات
✅
دسترسی فوری و رایگان
⚡️
همین الان فعال کن:
🔗
platform.inceptionlabs.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/6616" target="_blank">📅 02:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=bH_ATbaiGDwV5iVtY2K_eDtg1Wm7K1yUteyo3PMk6xWJumE3kHHqOFb-WGtpwL2mCa-1jVrsquEOY7QpYYubsMJfMFZh2jrBc2iGiZtIHveehPTgSc7UUjL4VLCGzgxZQLrjvQ46ZLykJYEzAZn-3zxeY958ylLbJo218DO80n0pu0gTnHlsO6-0UPXuGKZVimBIUmqyGppnGNJbzJ1gI3NDdQQISLltOJyLw4d5ZZG6Kff9PBfpTsHzXZMkMhjIe3bP8FLTIM-sglX1fk-V4-0xhYvLQWjkGAT8G8bDrPaBjGfMcSYmn3yAvGo9RyAM_tZWpbUDYFwt7mVPntlhpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a7cbc953.mp4?token=bH_ATbaiGDwV5iVtY2K_eDtg1Wm7K1yUteyo3PMk6xWJumE3kHHqOFb-WGtpwL2mCa-1jVrsquEOY7QpYYubsMJfMFZh2jrBc2iGiZtIHveehPTgSc7UUjL4VLCGzgxZQLrjvQ46ZLykJYEzAZn-3zxeY958ylLbJo218DO80n0pu0gTnHlsO6-0UPXuGKZVimBIUmqyGppnGNJbzJ1gI3NDdQQISLltOJyLw4d5ZZG6Kff9PBfpTsHzXZMkMhjIe3bP8FLTIM-sglX1fk-V4-0xhYvLQWjkGAT8G8bDrPaBjGfMcSYmn3yAvGo9RyAM_tZWpbUDYFwt7mVPntlhpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6615" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#اختصاصی
🚀
معرفی PokieTicker؛ کشف دلیل واقعی پشت هر نوسان قیمت در بازار بورس!
📈
✨
اگر شما هم از دیدن نمودارهای شلوغ و کندل‌استیک‌ها (Candlesticks) خسته شده‌اید و همیشه این سوال برایتان پیش می‌آید که *«چرا قیمت این سهم امروز بالا/پایین رفت؟»*، اپلیکیشن فوق‌العاده و متن‌باز
PokieTicker
دقیقاً برای شما ساخته شده است!
🔥
این ابزار چگونه کار می‌کند و چه امکاناتی دارد؟
1️⃣
تلفیق اخبار و نمودار:
نقاطی روی نمودار کندل‌استیک ظاهر می‌شوند که نشان‌دهنده اخبار منتشر شده در آن روز هستند. با کلیک روی هر نقطه، متوجه می‌شوید چه خبری باعث آن نوسان شده است.
2️⃣
فیلتر هوشمند اخبار:
دسته‌بندی اخبار بر اساس تأثیرات مختلف (گزارش درآمد، تغییرات مدیریتی، محصولات جدید، سیاست‌گذاری و...).
3️⃣
تحلیل و پیش‌بینی با هوش مصنوعی:
با استفاده از مدل‌های قدرتمند
XGBoost
و
Claude
، سنتیمنت (احساسات) اخبار را تحلیل کرده و روند قیمتی سهم را برای روزهای آینده (T+1, T+3, T+5) پیش‌بینی می‌کند!
4️⃣
کشف الگوهای مشابه:
روزهای گذشته که اخبار و شرایط مشابهی داشتند را پیدا می‌کند تا ببینید در آن زمان بازار چه واکنشی نشان داده بود.
5️⃣
رایگان و آماده استفاده:
دیتابیس لوکال (SQLite) از قبل در مخزن گیت‌هاب قرار دارد و برای اجرای اولیه نیازی به خرید API کلیدهای پولی ندارید.
﻿
⚡️
مشخصات فنی:
*
بک‌اند:
Python (FastAPI) + SQLite
*
فرانت‌اند:
React + TypeScript + D3.js
*
مدل‌های AI/ML مورد استفاده:
XGBoost, Claude Haiku / Sonnet
﻿
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/6614" target="_blank">📅 00:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=MfG20tKcV3DujV69UqaUamxPhoQC3EGM2dv4YNHk1QQnB9RatL0NZKyrTyTWMw0-8frLHUX_ltgPaDQfh0rPFKcSo-1Hb-I_QXk8wmAY5jERHFTUpezRoiKI8Muy9ctikpQXxtZanOfwy4XkBO7ZMXYpqWzEzc7Oyz_5aqAF_AKL1ERkjP4rrWRFAXe3XorImSpVFhbbe2b4xVYtE-yUasvo1ocsyeLGQTPqstCc-iwXQ25C7xIXWgpqaWrDDm7PG3Dqec5n-ad84oRBkzWTilbs5gSSRk89JjJ85Xl_RHJfCUMtljZUCrVcM7AbdjSItE6nV4oVWvT2GjkJ4oMngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8393e8cd0f.mp4?token=MfG20tKcV3DujV69UqaUamxPhoQC3EGM2dv4YNHk1QQnB9RatL0NZKyrTyTWMw0-8frLHUX_ltgPaDQfh0rPFKcSo-1Hb-I_QXk8wmAY5jERHFTUpezRoiKI8Muy9ctikpQXxtZanOfwy4XkBO7ZMXYpqWzEzc7Oyz_5aqAF_AKL1ERkjP4rrWRFAXe3XorImSpVFhbbe2b4xVYtE-yUasvo1ocsyeLGQTPqstCc-iwXQ25C7xIXWgpqaWrDDm7PG3Dqec5n-ad84oRBkzWTilbs5gSSRk89JjJ85Xl_RHJfCUMtljZUCrVcM7AbdjSItE6nV4oVWvT2GjkJ4oMngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">DewatermarkAI
حذف واترمارک با هوش مصنوعی در مرورگر
این سرویس رایگان واترمارک‌ها را از عکس‌ها حذف می‌کند و فایل آماده را می‌توان با وضوح اصلی دانلود کرد.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6613" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILoBPfN9xdc2qQFtclYymd-Ub9b_ZNWXPByjVTFxxXjB_8kXyi19tgAWFmhkXNdFtOfbAtsg5oDYFWJLhz_CLdKmUxBBPCUolU78ZLOdW1YJjw8nbfPjXiDgO4Jg9ddC6mhuge3nIiBF6VxJwKu7xQagr0_-7cERc4RmyUY3oOAuv9sClFycmRA3s-b-V9PCgw-LwJEvL9Grl3KyAtDNVD-GwBjiWl9TH3KF648iRWLff0RnVCBistjOzyp6lW9Iq8n5Dgti0tGkdDJQ58qh68Tlo2IoBuivz-D1P9RiSb0PY0hUX8CauSG6QcOjEdk_imm5pmJgOpvWIB0NH8r47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از به‌هم‌ریختگی اسکرین‌شات‌ها خسته شده‌اید؟ Trickle دستیار جدید هوش مصنوعی است که همه اسکرین‌شات‌های شما را به‌طور منظم سازماندهی و خلاصه می‌کند
فقط یک اسکرین‌شات بگیرید و آن را به Trickle ارسال کنید. هوش مصنوعی پیشرفته Trickle یک خلاصه دقیق تولید می‌کند که اطلاعات کلیدی مانند متن، نمودارها و یادداشت‌های دست‌نویس را استخراج می‌کند و سپس می‌توانید این داده‌ها را جستجو و درخواست کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6612" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COJjNZtc-x-EtROcV4iZN_IkrGpBan-quPZ_XauonWjgevFsPb5npl_8P3C9CfXS8vZ6JvLWj0lQMt-COjklA4ytM28E10ZPCuqI0sVArlzzeJ6fUK48ze8_nq26wcJvHMNX_QImMGV2L5HiVQnyPHDl4xwxiijS9Lt2BXdplMRPS2zZaZz-aClfTbov4xX3GsVdmcM_x_abrhgbp9VRWx2kjelcwP3tAMtaScpCDTeAOzfS1xKD5qztildk8lLi84iT2a8tuD7uDgPa_AQm2uxtmKOc5_D1sirjJWVuM1FxP1zOhBMEpofG-laVp5KOb3o1F4p-Zwker3PFE9apsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
شورای خردمندان هوش مصنوعی: تصمیم‌گیری با قدرت ۱۸ متخصص
آیا از پاسخ‌های ساده و تکراری هوش مصنوعی خسته شده‌اید؟ با این ابزار، مسئله خود را به شورای مجازی فیلسوفان، دانشمندان و مهندسان بسپارید و تحلیلی عمیق و چندجانبه دریافت کنید.
➖
مناظره کامل بین ۱۸ کارشناس مجازی (سقراط، ارسطو، سون‌تزو، آندری کارپاتی و...)
➖
بررسی مسئله از زوایای مختلف فکری و تخصصی
➖
ارائه راه‌حل‌ها همراه با نقد و رد استدلال‌های رقیب
➖
دریافت نتیجه‌گیری نهایی بر اساس جمع‌بندی بحث‌ها
➖
تحلیل واقعی به جای پاسخ‌های کلیشه‌ای
این ابزار برای تصمیم‌گیری‌های پیچیده و نیاز به دیدگاه‌های متنوع، گزینه‌ای بی‌نظیر است.
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6611" target="_blank">📅 21:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me-objVy3Mh4pHX5iqH9WvQ0KU1qYIaCBR7YVE-DYcnALaRk1_4PRmR9sbaH_WJzMyjnH0ZowaJIGkX6SpFc89vz_zMyGuJ6BolxVKgL_tJo9hJd9yJ2RQJFBcD3-sf_-lX0wc85QPq1vXg24s6X_U99Z6npJNf_2sTxb6vwMUwpJ64t_tqO6iUmV8c2SmyATNR5clU58tVpeIULxZ5Mn0zjCFbxkDAmMYpEGr35Ds_ptVCCiTJO8VPdenJBKg417neliNnWH1qza71uMcW-luRC1XmrRw9bys9tjS4-yL6LTlFQV3uc0X1hdnR8jkj6WduoQEsYOF90sJg9mb9nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
OFPlayer: پخش‌کننده موسیقی محلی و حرفه‌ای
➖
پشتیبانی کامل از فرمت‌های FLAC و MP3
➖
مدیریت آسان کتابخانه و لیست‌های پخش
➖
نمایش متن ترانه (Lyrics) و کاور آلبوم
➖
تحلیل دقیق فراداده‌های صوتی
➖
اتصال به سرویس‌های WebDAV، Subsonic و Navidrome
➖
رابط کاربری ساده، رایگان و بدون نیاز به ثبت‌نام
این پخش‌کننده برای کاربران NAS و کسانی که مجموعه موسیقی شخصی دارند، بسیار مناسب است.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6610" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PavrCxlRn40aT0lWjqbjacCU3aZ0tOlfwv_OSbqN06f5tuGIsYlw4JVWMbILJpZYbPPW8KN--klNgQPh3VMy0rdS8vWZdLnRU0dJXmPJqBdj13RBdyrv90GwEDYhzov94FPqT-R_EHiCWmH7ofGpa5jNoZ5LUGxs2PfyKr6mxsdlQD3lnYt6uqSwdPciFsJoXZXDaAqIqMMQ4lR72Ks1zjqKGG9FbHEPR5yUp5cskXwKSdu_VJSBPTEDvvCg6UdW01uW0xMdQIyom9wLeevleJAYnADsMdzL1HUIuwTF95-fG9tn3545ZPGs1MkAWJtOUQpIIYW-RkaiSszoQwpJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏋️‍♂️
مخزن کد با ۱۳۲۴ تمرین برای اپلیکیشن فیتنس!
اگه میخوای اپلیکیشن فیتنس خودت رو بسازی، این گنجینه رو از دست نده:
• ۱۳۲۴ تمرین کامل
• انیمیشن‌ها و تصاویر باکیفیت
• جزئیات عضلات درگیر و تجهیزات مورد نیاز
• دستورالعمل‌های گام‌به‌گام حرفه‌ای‌
پروژه خودت رو با این داده‌های غنی شروع کن!
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6609" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب Claude Fable هم استفادش برای مردم عادی کنسل شد
چینیا هم دارن مدرک جعلی میسازن تا بتونن ازش استفاده کنن
😂</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6608" target="_blank">📅 19:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
تبدیل جادویی اسناد پیچیده به Markdown خالص با MinerU!
📄
✨
اگر برای استخراج متن، جداول و فرمول‌ها از فایل‌های درهم‌ریخته و پیچیده مشکل دارید، ابزار متن‌باز
MinerU
دقیقاً همان چیزی است که نیاز دارید! این پروژه فوق‌العاده که با استقبال بی‌نظیری روبرو شده و بیش از ۷۰ هزار ستاره در گیت‌هاب دریافت کرده است، اسناد شما را به راحتی و با بالاترین دقت به فرمت تمیز Markdown تبدیل می‌کند.
🔥
ویژگی‌های برجسته این ابزار:
1️⃣
پشتیبانی از فرمت‌های متنوع:
توانایی پردازش و تبدیل فایل‌های PDF، DOCX، PPTX، XLSX، تصاویر و حتی صفحات وب.
2️⃣
استخراج دقیق جزئیات:
بیرون کشیدن بی‌نقص متن‌ها، جداول و فرمول‌های پیچیده (ریاضی و علمی) از دل اسناد.
3️⃣
پشتیبانی از ۱۰۹ زبان:
قابلیت تشخیص و پردازش بی‌نظیر اسناد در اکثر زبان‌های دنیا.
4️⃣
کاملاً رایگان و متن‌باز:
یک پروژه Open Source قدرتمند و بدون هیچ‌گونه محدودیت پرداخت یا نیاز به سرویس‌های ابری پولی.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6607" target="_blank">📅 18:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrHm7tRuDwUZdUUXFeDRZpK0kuTUbkUSqEOF__FewaLQkOoGaQezvbXjR8_aOzJlhS_tOksXCFPNlRmUPYm-nwYcxnTegUMaqGtN-9Z6AJuWUPT0--4l57iJU-ddGvcGs69RTM9W4ILE_L_Yv97PXH9qI5KmdIus86zsZz02V9_Zds0EF5lNjRzvAQUMagMxULF08QxoFJlE-wzCpNpQvbXxo0-kp31zCJ2kN5A7nCi46RW9zMGKnuOGVd1QwSlyRJ0E3PPugqbLjEYZnKoIVRLzVIaxcHHvgLAvk7QR0z8devwZmTbwY4KCmMwt40eZq6-vVYtkoqdw2O1-b_8B3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها ElevenLabs را کشتند!
💀
توسعه‌دهندگان ByteDance نسخه SeedAudio 1.0 را عرضه کردند که هر نوع گفتار و افکت صوتی را کلون و تولید می‌کند.
1⃣
ایجاد گفتگو با چندین شخصیت: هر شخصیت متمایز است، دارای احساسات، سرعت، تمبر و حتی لهجه منحصر به فرد؛
2⃣
دریافت تا سه منبع برای کپی کامل صدا، احساسات و سبک؛
3⃣
تولید صداها بر اساس پرامپت، مرجع صوتی یا حتی تصویر.
آیا این پایان دوران انحصار ElevenLabs است؟
🤔
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6606" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVZ7_3pwVhG3s77--Lazl3LKw5wSbbeviYfZ3mrfdhHxof2GKsvGErEMj57PJ4sKD4mUJwREIAxuxBO7dql5IF3wlVjGTQaJDaJ8KpNwkInIWfyUKRyNlicQQixk8j3XgvN3By86dC7riQjM6GEk2trbxzd1tMmyXABbvBK26XiY2yyT-p_upw4Uv1tXLMtE_9JQgWR61V_4NMo87BY1lh6gaDFPn9XhG0po-BdpvvfCMBiM0vowZcV65AwXiIJu1tQZWdp78riPWTk5j-9NPBHcg261Ejkn80D8r_OzV9e79eKo7pYr2Hyq2400zD7pWvC2zyneE6ghjDc4IlkdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
تولید رابط‌های کاربری زیبا با پرامپت‌های آماده
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6605" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
معرفی IstanPdf؛ ابزار قدرتمند و آفلاین برای مدیریت فایل‌های PDF و DOCX!
📄
✨
اگر از سایت‌های پولی، تبلیغات آزاردهنده و محدودیت‌های سرویس‌های آنلاین تبدیل فرمت خسته شده‌اید، اپلیکیشن
IstanPdf
دقیقاً همان چیزی است که نیاز دارید. این ابزار کاملاً آفلاین توسعه یافته تا جایگزینی بی‌نقص و رایگان برای سرویس‌های پولی (Freemium) باشد. در این اپلیکیشن حریم خصوصی شما در بالاترین سطح قرار دارد و هیچ فایلی از گوشی شما خارج نمی‌شود!
🔥
امکانات فوق‌العاده IstanPdf (نسخه v1.0):
1️⃣
ابزارهای حرفه‌ای PDF:
*
Merge:
ترکیب و چسباندن چندین فایل PDF به یکدیگر.
*
Split:
استخراج صفحات دلخواه با تعیین محدوده صفحات.
*
Remove & Reorder:
حذف صفحات اضافی و تغییر ترتیب صفحات یک فایل.
2️⃣
تبدیل فرمت (Conversions):
* تبدیل یک یا چند تصویر به یک فایل PDF یکپارچه.
* استخراج صفحات PDF و ذخیره آن‌ها به عنوان عکس.
3️⃣
ابزارهای کاربردی DOCX:
امکان حذف صفحات خاص و تغییر چیدمان و ترتیب صفحات در اسناد ورد.
4️⃣
حریم خصوصی و امنیت مطلق:
کاملاً آفلاین، بدون نیاز به ساخت حساب کاربری، بدون محدودیت حجم و آپلود، و فاقد هرگونه تبلیغات و پرداخت درون‌برنامه‌ای.
🔗
دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6604" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPS0Rdy_p3BNjHVqqOdi6epmsW4l1dFwI_ZxuwMWJkmo-ZhCtnsf0mhtiaqhMZGO4zrEyvZGWmQrw9v7mnsLUpZXIEbmhvO9Dyfy_mpXOi2Z3dI1BuhWpcwpsKLSxCn7JJtN3RQz1Sh4mx1j6mkHeRsg3J8GVbCA5RSIyusiAMNdicFsm5yENrEYIXeQ7PcVuBJuIYcKFPrv51F3i3FXRs8NnW0kEM8qun7gYurY5DeUVAOd0Ycb1iqukhQ8TecKIWE5kDuCcLFVPbsmhY00AtAZDJXKbL78cxiG-0QnpWLAM8P03pk6r1s3FPIk3Fi9OYJEa8uWQa1SKcB0RGSbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
جایگزین رایگان و متن‌باز برای Claude، Cursor، Codex و سایر نمونه‌های مشابه.
✨
ویژگی‌ها:
•
💻
تولید کد برای وب‌سایت، اپلیکیشن و بازی در چند ثانیه
•
🆓
کاملاً رایگان؛ بدون اشتراک یا محدودیت پنهان
•
🌐
اجرای مستقیم در مرورگر؛ بدون نیاز به نصب
•
📝
فقط پرامپت بنویسید و کد آماده دریافت کنید
🌐
Site
#AI
#Coding
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6603" target="_blank">📅 11:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=Kem-kSlGuqLCFWGHtylb1uN16JwYvtIVgNWRh4KD7wrFSf8ZQsWouAgHfWkh2jGGWsE0vHZjQOI2zOjWU1sIVCwLFrzGNBxIRrqd2zCE9LpH43YQrpJ62JChEOUt4Rn3XYh3f3vEnr_XYcj1W59-w2Z5xNS83OLldxaUdxHt4lUZ9QZQhAEGDu55PO22Cx64lcDAWraryf26mcJkfgmNXjJBR4ey4hbI8kgHA1Mxtwh6hUDPy9qft3ARp3DDxCI8ZytMTzbOKO896gWD38E8M1v2m0np_PyCibrd6JrJiH3I0IXbz3i3WScc_chQmBnDaXiI4DUr2MfoUDgZw08tWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7baa23f6.mp4?token=Kem-kSlGuqLCFWGHtylb1uN16JwYvtIVgNWRh4KD7wrFSf8ZQsWouAgHfWkh2jGGWsE0vHZjQOI2zOjWU1sIVCwLFrzGNBxIRrqd2zCE9LpH43YQrpJ62JChEOUt4Rn3XYh3f3vEnr_XYcj1W59-w2Z5xNS83OLldxaUdxHt4lUZ9QZQhAEGDu55PO22Cx64lcDAWraryf26mcJkfgmNXjJBR4ey4hbI8kgHA1Mxtwh6hUDPy9qft3ARp3DDxCI8ZytMTzbOKO896gWD38E8M1v2m0np_PyCibrd6JrJiH3I0IXbz3i3WScc_chQmBnDaXiI4DUr2MfoUDgZw08tWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اختصاصی
🔥
🔥
هر نوع رسانه‌ای را از تلگرام و حتی چت‌های خصوصی دانلود کنید
🤯
• دانلود صوت، پیام‌های صوتی، ویدئو، GIF از چت‌ها، استوری‌ها و حتی چت‌های خصوصی که دانلود در آن‌ها ممنوع است.
• پشتیبانی از دانلودهای چندگانه بدون کاهش سرعت.
• قوانین تلگرام را نقض نمی‌کند، می‌توانید با خیال راحت استفاده کنید.
🌐
GitHub
#Telegram
#Tools
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6600" target="_blank">📅 08:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دریافت 7 میلیون توکن روزانه AI به صورت رایگان!
🎁
🤖
مدل‌های موجود:
• Mimo 2.5 Pro
• Mimo 2.5
• Mistral Large
• Mistral Medium 3.5
💻
کاربرد:
• ساخت وب‌ سایت
🌐
• ساخت ربات تلگرامی
🤖
• کدنویسی در ترمینال
⚙️
🔗
NaraRouter
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/6599" target="_blank">📅 01:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Metapi؛ هاب هوشمند و همه‌کاره برای مدیریت APIهای هوش مصنوعی!
🤖
✨
اگر برای دسترسی به مدل‌های هوش مصنوعی در سایت‌های مختلفی ثبت‌نام کرده‌اید، حتماً می‌دانید مدیریت ده‌ها API Key، چک کردن مداوم موجودی و تغییر دستی تنظیمات هنگام قطعی یک سرور چقدر کلافه‌کننده است. پروژه متن‌باز
Metapi
توسعه یافته تا به عنوان «پروکسیِ پروکسی‌ها» تمام این مشکلات را حل کند!
🔥
امکانات و ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
تجمیع تمام APIها (Aggregation):
شما ده‌ها کلید مختلف را به Metapi می‌دهید و این ابزار به شما
فقط یک API Key و یک Base URL واحد
می‌دهد. حالا می‌توانید این کلید واحد را در تمام برنامه‌های خود (مثل Open WebUI، Claude Code یا Cherry Studio) قرار دهید.
2️⃣
مسیریابی هوشمند (Smart Routing):
اگر سرور یکی از ارائه‌دهنده‌ها قطع شود یا مدل خاصی در آن گران باشد، به صورت خودکار درخواست شما را به یک سرور جایگزین، سالم‌تر و ارزان‌تر می‌فرستد (بدون اینکه شما متوجه قطعی شوید!).
3️⃣
دریافت اعتبار خودکار (Auto Check-in):
به صورت زمان‌بندی‌شده در سایت‌هایی که سهمیه رایگان روزانه می‌دهند لاگین کرده و اعتبار شما را به‌طور خودکار جمع‌آوری می‌کند.
4️⃣
حریم خصوصی ۱۰۰٪ و نصب آسان:
به راحتی با داکر (Docker) روی سرور یا سیستم شخصی شما نصب می‌شود و تمام داده‌ها فقط در دیتابیس محلی (SQLite) خودتان ذخیره می‌مانند.
5️⃣
سیستم هشدار پیشرفته:
در صورت بروز قطعی یا اتمام موجودی، از طریق تلگرام و ایمیل (SMTP) به شما نوتیفیکیشن می‌دهد.
⚡️
برخلاف پروژه‌های مشابه که برای تیم‌ها و فروش API طراحی شده‌اند، Metapi کاملاً برای
استفاده شخصی
بهینه‌سازی شده و رابط کاربری بسیار سبک و تمیزی دارد.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#API
#Metapi
#OpenSource
#Github
#SelfHosted
#Docker
#Tools
#OpenWebUI
#LLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6598" target="_blank">📅 01:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">#اختصاصی
🔥
🚀
معرفی Awesome Android Root؛ گنجینه‌ای بی‌نظیر برای روت و شخصی‌سازی اندروید!
📱
✨
اگر به دنیای روت، کاستوم رام‌ها و دستکاری عمیق سیستم‌عامل اندروید علاقه‌مند هستید، مخزن
Awesome Android Root
یک دایرکتوری جامع و بی‌نظیر است که بیش از ۴۰۰ ابزار، اپلیکیشن و ماژول مخصوص دستگاه‌های روت‌شده را به همراه آموزش‌های دقیق در یک‌جا جمع‌آوری کرده است.
🔥
امکانات و ویژگی‌های کلیدی این لیست:
1️⃣
آموزش‌های قدم‌به‌قدم:
راهنماهای کامل و دقیق برای آنلاک کردن بوت‌لودر (Bootloader Unlocking) و نصب کاستوم ریکاوری‌ها (Custom Recovery).
2️⃣
پشتیبانی از جدیدترین متدهای روت:
پوشش کامل و معرفی ابزارها برای روش‌های مدرن روت سیستم از جمله
Magisk
،
KernelSU
و
APatch
.
3️⃣
کالکشن گلچین‌شده ماژول‌ها:
مجموعه‌ای از بهترین و کاربردی‌ترین ابزارها برای مسدودسازی تبلیغات (Ad-blocking) در سطح سیستم، اتوماسیون وظایف و شخصی‌سازی عمیق رابط کاربری اندروید.
⚡️
مشخصات فنی:
*
زبان:
Python (برای مدیریت و استخراج داده‌های لیست)
*
پلتفرم:
Android
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#Root
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6597" target="_blank">📅 20:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام
دوستان اگر به وایب کدینگ علاقه دارید یه نگاهی به این سایت بندازید:
https://risman.pro
برای ساخت محصولات فنی میتونه خیلی کمکتون کنه. (بدون نیاز به هیچ دانش نرم‌افزاری و برنامه‌نویسی)
امکان انتشار در دامنه خودتون هم بهتون میده.
با اولین لاگین حدود ۱۰۰ هزار تومان توکن هدیه میگیرید و اگر خواستید توکن بیشتری مصرف کنید میتونید از کد تخفیف welcome برای ۵۰% تخفیف تا سقف ۱ میلیون تومان استفاده کنید.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6596" target="_blank">📅 19:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/On3SVOOF6mC2pSyIoklTCISaMHO1vJMY0MHJxtVVmcOJ36D3E3pOl_Uj4rTUtKkkEeTdQFaZ8v1qWcgc_cKbsGU_sdfzziBNAjYAaUOA-DsDsoLp4B-69U4sgb4Z79ZkdGIARM1aQ2KnTFPuGZtGFoJ50z4-vhcAoUSpN8eVHeEenaDM80CmgRTebZCO8MpgXgXlgjB2DitlG2UXxAm-M6-3y9n5f4Okfj1MVX2ieUyt0K7rEALOFxBid39oLcaqhNc4mL-wCneVvITV80Y4I5Iqga7PaCMSi6FBVKmkXPD9e-QmH_KNHQAWmw3v-M2QHBkqzfwfulr4Ux1w7pkt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابلیت ست کردن پراکسی لوکال
خیلیم ساده
مرورگر باحالیه
🔥</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6593" target="_blank">📅 15:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYC_RHE2IDYZCAA-WwONCew6z3LZttXql3HKDEYGXG3HAQHoiPB1_G3FsCCUhZpdVKKFod2dPhm-GI1qHun68Uh2sn3eTuvbYp-fEF8mv5AmP5iYt7JWyX0zKvFF3VZcAkKlfx9tm2fkP3bxSkkCbqTXsGamjBeAsfhTUqste7k4lWe5rYV0TaVinhY7xrUaEOH_DpjEq_pozTmzcKMNJrzuWPh7CQlBy7cZY6nZw9guFX8Xp-tPHPze2twNQucX1314W_7rkh36UJEVTo2vYC-OYbQyrIA3x2E3MmjsivpUveWLHj87VAn3WDvdgsslDsI8kzaAUH2iIoERwvqwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن Solipsism یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی…</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6591" target="_blank">📅 15:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی مرورگر Solipsism؛ وب‌گردی با طراحی منحصربه‌فرد و متمرکز بر حریم خصوصی!
📱
✨
اگر از ظاهر تکراری مرورگرهای موبایل خسته شده‌اید و به دنبال مرورگری خاص، قابل شخصی‌سازی و امن می‌گردید، اپلیکیشن
Solipsism
یک شاهکار در طراحی رابط کاربری است. این مرورگر اندرویدی با ایده خلاقانه "Rail-first" تمام کنترل‌ها و نوار آدرس را به جای بالا یا پایین، در یک نوار کناری (سمت چپ یا راست) قرار می‌دهد تا کار با گوشی‌های بزرگ با یک دست بسیار راحت‌تر شود.
🔥
ویژگی‌های شگفت‌انگیز این مرورگر:
1️⃣
طراحی نوآورانه (Rail-first):
قرارگیری منوها در نوار کناری با قابلیت تنظیم اندازه (از کوچک تا Super Compact) متناسب با اندازه دست و صفحه نمایش شما.
2️⃣
زبان طراحی Material 3:
رابط کاربری بسیار زیبا با گوشه‌های گرد، انیمیشن‌های روان، سایه‌ها و قابلیت هماهنگ‌سازی رنگ‌ها با تم سیستم‌عامل اندروید.
3️⃣
ابزارهای قدرتمند حریم خصوصی:
دارای مسدودکننده تبلیغات (Ad Blocker)، وب‌گردی ناشناس، کنترل کوکی‌ها و WebRTC، پاک کردن خودکار داده‌ها هنگام خروج، و یک قابلیت بی‌نظیر به نام
Decoy Mode
(تولید تاریخچه وب‌گردی جعلی برای محافظت از حریم خصوصی!).
4️⃣
امکانات کاربردی و سریع:
دارای اسکنر QR داخلی، قابلیت نصب مستقیم وب‌سایت‌ها به عنوان اپلیکیشن (PWA)، پخش تمام‌صفحه و بدون مزاحمت ویدیوها و ابزار دانلود حرفه‌ای.
5️⃣
صفحه خانگی شخصی‌سازی‌شده:
امکان تغییر والپیپر هوم‌پیج یا تنظیم آن روی حالت کاملاً تاریک و بی‌صدا.
﻿
⚡️
این مرورگر سبک که بر پایه WebView اندروید ساخته شده، تجربه‌ای کاملاً متفاوت، سریع و مدرن از وب‌گردی را به شما ارائه می‌دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Solipsism
#Android
#Browser
#Privacy
#Material3
#AdBlocker
#WebDevelopment
#MobileApp
#TechTools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6590" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
هوش مصنوعی دیگر کدهای شما را فراموش نمی‌کند؛ دستیار حافظه دائمی برای ایجنت‌های برنامه‌نویسی!
🧠
✨
اگر از پریدن کانتکست (Context) در چت با هوش مصنوعی و توضیح دادن‌های تکراری خسته شده‌اید، این ابزار جدید مشکل شما را حل می‌کند! به تازگی یک دستیار هوشمند برای مدل‌هایی مثل Claude، Codex و Cursor منتشر شده که دانش و اطلاعات پروژه شما را بین سشن‌های (Sessions) کاری مختلف حفظ می‌کند.
🔥
این دستیار چه کارهایی انجام می‌دهد؟
1️⃣
حفظ همیشگی کانتکست:
اطلاعات جلسات کاری شما را ذخیره می‌کند تا با بستن پنجره، کدهای شما فراموش نشوند.
2️⃣
یادگیری ساختار پروژه:
معماری، دایرکتوری‌ها و ویژگی‌های خاص کدبیس (Codebase) شما را کاملاً به خاطر می‌سپارد.
3️⃣
بسته‌بندی خودکار دانش:
اطلاعات جمع‌آوری‌شده را به صورت خودکار و هوشمند بایگانی و بهینه‌سازی می‌کند.
4️⃣
بازخوانی در کسری از ثانیه:
هر زمان که ایجنت به اطلاعات قدیمی نیاز داشته باشد، در کمتر از یک ثانیه آن را فراخوانی می‌کند.
5️⃣
پشتیبانی بسیار گسترده:
سازگاری کامل با
Claude Code
،
Cursor
،
Codex
،
LangGraph
،
CrewAI
و سایر ایجنت‌های هوش مصنوعی.
🔗
لینک دریافت و راه‌اندازی پروژه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#CodingAgents
#Claude
#Cursor
#Codex
#LLM
#Memory
#ProgrammingTools
#DevTools</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6589" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVsNwn8z8ejRJWPfWoVhcyiqatB8TivQYehelqf63TwxHIGlQEdXen8UwTEBHOnCqYbqEZVERY9FVu50lg6CabIJKffdsJu__qBs485rFAdXT7skDw98gJf9o3n4Z2XYqsMnVfjx9raFg8EcAXUYj2bgq2aE2R_7S25Q0fhPJSag3Dlp53EOuE1R49vULrJmf9m5UkZCZXsRroUpZOQluhP-rDipW7CoCw4ddvWOBkzbzJ-Cfj-k5ZEz94GBLuazAyAzPGHkR4Tl8qtRzhNc8cnXkQ1vqtZ68fUPhA9wh_ngdq2uJAMnR9nIByf_ft3W3nAPWcvxIVeRFWWAVMBCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 1T کانفیگ شخصی
🔑
🟢
از لینک زیر میتونین شروع به ساخت اکانت کنید :
➡️
sign up
بعد از ثبت نام وارد اکانت بشید و روی
Quick Subscription
کلیک کنید و داخل اپ هایی مثل :
Nekobox,hiddify,singbox و ...
اکسپورت کنین .
به دلیل نوع پروتکل یعنی AnyTls بودن فقط داخل اپ های ذکر شده میتونین اکسپورت کنین و داخل اپ هایی مثل V2ray کار نمیکنن
😬
خط های تست شده :
🛜
🛜
💬
@Archivetell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6588" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_4HJFEeHZw7Gl6QjX76YvkJ6n4QLiOHwQP5RSdc7iso4XMcw8itR76OIkPOs_U8EWP10b4Bbp24Y4j2Sbl1UAoHn2JWU9bJ3NoFvs97UWQOqCqNkGWXP0F0lFUkDzEtVmGIUSF_dYJE45pH8zHUNunuohVKXDK5qtwivK-8H6bRI6rbWy5q3OYuwJuiZIYnm3aAM36Ds0yrcnyYYfnFYqmuQZY1AuHRedPN4PkvzgGcTfqTe0jn5ewfKxa8jxWjFDZ7YLiARe2RGk0wb67dbKCmN-6dEHhDwTNYQkXTy2O7SC9-csW7MAdBL8ZTGQrt-MllCUzfBqyHkUE6KIZcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHBCxoTnXJQtyQd8ZQMWBa495XENX3yk_XZVIkGGPfZIDrYs-FArWTeXmq4FU67ceq8_SJQB_cFaimwUm51AI9HFGG_OswsEtQW3fFx-RlJBN-g-kew4K_isFwkpWyYjuHjPbF3cRLxN6pQpqSyXEmHmv4aR_fJssm7rbZGyv6V_adU2xZl8HaJDaLZEygYNLgv5DFhUovo4y3xXKefPBJhqYZQYxd1EKA4UlQZ2QsNZrqnVVph__-OqouUfxvPAVYC7hdPXZM1ma3krf7eW-uhskywQEft1HZnzpDys0PoNyJE-ZmrOf1jXKhQqLT7PhHnNh8D5T_E_pFcU5dok3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfT1Uz60v9wH8joSX9nzfOY20j65602fu76K3bjQ1aixQfK9l-EyNyoI9G2yUnqtDw9ZjMpj44MvVzmYF5TQtFjOcZiutXH0jr80h3ANr6N3n6aWgr0YTyIQOFtZf-spaex0aQ3_7pe-5IHtIL2ecPf7fjc2bQUl0TCUSoCORZ4FbwguJY6MLoLX1j10hmC83iVLmvHwGhtSs3tEbnRYlErr68bLMR3d0k-QoFx-KloEjbciH9LfWw-AcRF6G2IkSG38G2DItVpOii3xsWU0F6L4sMSs1m7Cpckn7HcC9UjV0adyAUG7Gnb5Pw0N0fTdfTFj5gKzwnYp3eR9fU5GJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبدیل عکس‌های معمولی به شاهکارهای هنری با هوش مصنوعی
🔥
✨
قابلیت‌ها:
•
🎨
انتقال سبک هنری (مثل ون‌گوگ) به تصاویر شما
•
🪄
انتقال سبک بصری یک عکس به عکس دیگر
•
⚡
مبتنی بر شبکه‌های عصبی کانولوشنی و الگوریتم‌های پیشرفته
•
🛠️
رابط کاربری ساده و سریع برای ویرایش آنلاین
•
📦
بدون نیاز به نصب نرم‌افزار سنگین
🌐
Site
#AI
#Art
#Tech
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6585" target="_blank">📅 11:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_J8uyEjudygjuYeEUgbAl-wBNy0FziqC8y_ucX0hLRsJj971xKLatW-pTiDIoso3uX88Q63B_gIID7-_pjVBUwJ1Cpz2ub4p4tg4UbmchJtRWidYnUUSvbp3A59DGc180l96IZtJAZrah99cgneyilDOZwtU8vl0MVu5PK72ywpHMOBDFeDtFTgnJRWbJTHE0W1Q_AOKxdw9PnR6EMs0VjSoa2LlnPTo2RMcaTNFgSw5VmFVuGJzE9fJpJORriv1U4qzMoevTrqR_1-r3bpw5octCDjX7KTq79LTD6hz6lpHB6-vjvLONnokuf6PVo_tgB_DEuOW7n9CPC47H_Unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه Orcafile دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6584" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ویژه
🔥
🚀
معرفی Orcafile؛ ابزار جستجو و دسته‌بندی سریع فایل‌ها بر اساس پسوند!
📁
✨
اگر از گشتن در میان پوشه‌های درهم‌وبرهم برای پیدا کردن یک فایل خاص خسته شده‌اید، پروژه
Orcafile
دقیقاً برای شماست. این اپلیکیشن دسکتاپ و متن‌باز (Open-Source) به جای اینکه شما را مجبور کند پوشه به پوشه بگردید، کل یک دایرکتوری (یا حتی یک درایو کامل) را اسکن کرده و تمام فایل‌ها را بر اساس پسوندشان (Extension) گروه‌بندی می‌کند.
🔥
ویژگی‌های کلیدی Orcafile:
1️⃣
اسکن فوق‌سریع:
قابلیت اسکن بیش از ۱۰۰ هزار فایل در پس‌زمینه بدون افت عملکرد سیستم.
2️⃣
مشاهده لحظه‌ای پیشرفت (Real-time):
نمایش لحظه به لحظه وضعیت اسکن فایل‌ها.
3️⃣
جستجو و فیلترینگ هوشمند:
جستجوی آنی نام فایل‌ها و فیلتر کردن دقیق بر اساس فرمت و پسوند.
4️⃣
دسترسی سریع:
امکان باز کردن مستقیم فایل‌های پیدا شده در فایل اکسپلورر ویندوز.
⚡️
مشخصات فنی و
پلتفرم:
توسعه‌یافته با ترکیب قدرتمند
Python
و
PyQt6
.
نسخه اجرایی (App) در حال حاضر فقط برای
ویندوز
منتشر شده است، اما از آنجا که پروژه متن‌باز است، با استفاده از سورس‌کد و دستورالعمل‌ها می‌توانید آن را در هر سیستم‌عاملی (مثل لینوکس و مک) اجرا کنید.
🔗
سایت پروژه
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Orcafile
#Python
#PyQt6
#OpenSource
#FileManagement
#WindowsApp
#Github
#Tools
#Productivity
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6583" target="_blank">📅 09:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=GkNNP_tsqAk5-KYMwvIOL2TGbnDZwYqR8NJfwMGtqWm1GlmRw87s467a5CgFLxE1kygZyKiy73JVnXfMWq3RYgXsRsLHHzkK9jK64O1CgCKFGRT9njXQGD3QnvOPxP3glTfMUhJdRwn6hToYPJaJF672dP1upXa-fiEt2HLuiH-pVutF2MQmHn8T6sz7YgJ6aiwQFZh2JvUGLwTKY5PM0NU6FIWMMpVlqCPcBOhDENHmWPZuzlJ4HoZsx9rApe8ox5RGD2eVCbE4t8XAQQ4C0YBfPkbYWtT3uwIOHxW3x7-cdi_W9sie8o09zu6Mn9Yo6NteI2IXNsjBnLCJYC5wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93c42b223.mp4?token=GkNNP_tsqAk5-KYMwvIOL2TGbnDZwYqR8NJfwMGtqWm1GlmRw87s467a5CgFLxE1kygZyKiy73JVnXfMWq3RYgXsRsLHHzkK9jK64O1CgCKFGRT9njXQGD3QnvOPxP3glTfMUhJdRwn6hToYPJaJF672dP1upXa-fiEt2HLuiH-pVutF2MQmHn8T6sz7YgJ6aiwQFZh2JvUGLwTKY5PM0NU6FIWMMpVlqCPcBOhDENHmWPZuzlJ4HoZsx9rApe8ox5RGD2eVCbE4t8XAQQ4C0YBfPkbYWtT3uwIOHxW3x7-cdi_W9sie8o09zu6Mn9Yo6NteI2IXNsjBnLCJYC5wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💻
JanAi
جایگزین محلی ChatGPT
این برنامه مستقیماً روی کامپیوتر اجرا می‌شود و نیازی به اتصال به اینترنت ندارد. می‌توان از مدل‌های زبانی مختلف برای متون، برنامه‌نویسی و سایر وظایف استفاده کرد.
🌐
Site
#AI
#OpenSource
#LocalLLM
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6582" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Awc7ZNdAQxc-bGOa6ApzjxyO7jPGPZ8NVszxpUWvMNqmXENpofm6bVC9gENAhVwi6j2HrAT_W9-YlGAY_TOB0dxKjf12fNt07tRKDtHZSe6wLxIebmj8JPg8kliwTeGWTKDywufuGMPaRtAOKmzH0fQW7S8R-ygrY6_KcQ9R1-e_vq9snC0qaFP3YdlSboED-FlDR52dFVx0HgR3q7rAEFuoaR4PQjtG_ElSWUekF4mQr365kwk4dstrwHPJwAwRBIIGw4aufroiZav53eiVoFyscs7RZL4vCan9QKFs4PCSqV1S2phUqP_Rio3KcC-G8A3vQFwdVq-kcTMB9U4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTNo8X7eZnB6MsmhH6ufTAGuLjx-SZOYcL7ApWtzKEC29_trqa20iYU3deVVUb4VBN06mxVKtAZXWeSrDfOsmz-qzRo2J9Sxcv1ngdnJuqW1inGDFhbDxzbXR5raMohpF4RULGwop0njUaK1ASB95P4GrXzSGOqP5saMbhTrDg468sDYry4rbZ_m-rU-Xi8qlai7qdlHY2aU6Uficwp2_hi95FEs6RsqsdCqcR1a7m_-Sq9dFrt37akWGJs2idJX4SYcMKI3CoUDDUkEvMzgBY1-amyXTdnuNLtoHfEePEqVbrdSee5mC0mizxPJdPn0AtloA4R8a88gGduYDknMxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
«انجمن‌ها» به تلگرام اضافه می‌شوند — در نسخه آزمایشی برنامه چند ویژگی جدید پیدا شده که عملاً پیام‌رسان را به دیسکورد تبدیل می‌کند.
• در انجمن‌ها می‌توان چند گروه را در یک فضا ادغام کرد، چت‌های عمومی و خصوصی اضافه کرد و همچنین دعوت‌نامه‌ها را به آنجا ارسال کرد.
• همچنین می‌توان کانال‌ها را به انجمن‌ها اضافه کرد، اما این ویژگی هنوز فعال نشده است.
تاریخ انتشار به‌روزرسانی بعدی هنوز اعلام نشده است.
#Telegram
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6580" target="_blank">📅 08:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">طراحی وب و اپلیکیشن در یک ثانیه با ابزار جدید GenSpark
🚀
✨
قابلیت‌ها:
•
🔹
تحلیل مستقیم فایل‌های Figma، عکس و کد
•
⚡
تولید طرح نهایی بدون نیاز به کدنویسی دستی
•
🛠️
دسترسی به قالب‌های آماده برای وب و موبایل
•
📦
ساخت رایگان نمونه‌کار برای فریلنسرها
🌐
Site
#AI
#WebDesign
#GenSpark
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6579" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6577">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLgl7p4fGgMFWdIfLRZkedt-BN6FyVnSMxSMjr_ll8_5Zp4lHRdzwQNys4av0DKkZsX0HabMG9OUoGP7YwAJeX1N2dN7IrcmC9Fm2zxCXnfX8WThMpStNoPDfGwyLEjBMiBRHxd16Xfbofe1YjRbN85uRNvnhQIZO0tb_lgjCvnQQy3tFN-jpQwVf-Roaj3racFifS_xymtT_slY6h9B7I_zKNz-iIG8_SJ18Q6FAjRdqVE0rHpyi546XEXBDxZ3h7_BzLHVytsK9zdnB0HAzjgCM6JoZ1MYB3C15KNFyAL5_YTFKyHQsVIbGeD_cEFc9zXewWNC8km42tNPDox-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
انگلیسی رو تو حرکت، باشگاه یا پیاده‌روی تقویت کن!
با این ۵ پادکست، بدون کتاب‌های خسته‌کننده به گفتار زنده عادت می‌کنی:
•
🇺🇸
American English Podcast
: انگلیسی آمریکایی، فرهنگ ایالات متحده و مکالمات واقعی.
•
🧠
English Learning for Curious Minds
: داستان‌های جذاب درباره علم، کسب‌وکار و زندگی.
•
⏰
6 Minute English (BBC)
: قسمت‌های کوتاه با واژگان جدید، اصطلاحات و موضوعات روز.
•
🗣️
The English We Speak
: عبارات مدرن، زبان عامیانه و اصطلاحات مکالمه‌ای.
•
🇬🇧
Luke's English Podcast
: تحلیل زبان و فرهنگ بریتانیایی، یکی از معروف‌ترین‌ها.
#EnglishLearning
#Podcast
#Language
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6577" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKA633fOFPoKv6tAF3XRjaPLLxI_GGb-3GQ5_WZwSpyhwp1xTdxAfqXvc8qgVeJbhWVLy_RRHfBqlbxQyYdlPoz7H2DVjsQ4pv_N_V2pZnKEQVtCC42YyJ_3_CmVQivGgDizwLkMMRXtJjF65cXgzzgtO2OZu6uhq7JdYoQQwywM-YwSNoHYuyl1ZfIQ8wJOC52sQ_rObj2yxPJfnPVhp2aYhbGG1NUDz0c_i_W8J-Y5vsPBWSDyqoThEisYHw0FHQjpmOxziuABEfwbQ2ZhDPtpQZioi-Cr4vS_Aeq6k6HjFM_rpL4ZtBMkaVic9DgptsbyVJON8_ZZETmk3HjXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTK-zKrXI69vYl7n4K_Xdlc4HbbQt6YjII53ngB96ceho5LOzSUSrK9uteeyjd6eNWnOSNlGKJzxjqPiTYKd7WaJOL4I59k0O7U5kAEHZMwim7qQEUDSPL7G_sO72rO7ZdGsGLmVm2_MsVbrdk7DGJwjxRmDEj8kbSXjOi72SUaKJkmKoMrQtJCAWyIL4QJrs6O_w0eAHD2nC4m1g6kMws_P0nL25CMOhhRfrGZxxmCZgiJX0O3CCQWC6xLil9ju1G8IIVQWgX80n8ReqlEMyWVO8-dyH5_YY-CLSqJCTV6jVtUwWP7dReV3BkSn1BLU9oQGkCaM8EBSkWrb13OMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvWHFPv5rIfmH7bCuta1JGPKASnPMXBGHYzfDStKHrTGkkRy0HhqnI8QZy8327IkcSf0eqNmq8XEdEwHc6roJQyz4W-9GSMjmXcqI63-Q2j3JC3bWf0oIknBl3xddFs-BoS2n6K1_2VLdSu2ALqzhMLPGggd_cyBTXeHp7LQRD718i-_4KegLUuQCbns1jRd7UxiILS8DO26e2MFmbwFdod9K8dNjmy63vL94PvhdOGa8zhG1ocLdUcIowZS1ChrCq6nBTZipPaLYkP38PPjDuqjkPM9NPb8fTW_JzYF3YvyD8HMcxr-F5lHKPe9AxTmfhAP_dZSnVYjvOjWSbvhKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
OpenAI
مدل جدید GPT-5.6 Sol را معرفی کرد؛ مدلی که در چند بنچمارک مهم، حتی از رقبای مطرح هم جلو زده و تمرکز اصلی‌اش روی کارهای پیچیده و توسعه نرم‌افزار است.
💻
🧠
•
🔹
عملکرد بهتر در بنچمارک‌هایی مثل Terminal-Bench 2.1
•
⚡
توانایی کار مداوم روی پروژه‌ها برای ساعت‌های طولانی
•
🛠️
مناسب‌ برای توسعه نرم‌افزار با دخالت کمتر انسان
•
📦
معرفی مدل‌های سبک‌تر و ارزان‌تر Terra و Luna در کنار Sol
🌐
Site
#AI
#OpenAI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6574" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الان برای API بهترین
aerolink
هست که بهتون
opus 4.8
میده
خیلی ساده
لینک ثبت نام
نحوه ثبت نامش دقیقا مثل
freemodel
هست طبق این
پست
نحوه اجراش روی
claude code
هم همونه فقط تنظیمات رو این بزنید
هر ورژنی از claude code هم بزنید قبوله
{
"env": {
"ANTHROPIC_API_KEY": "کلید",
"ANTHROPIC_BASE_URL": "https://capi.aerolink.lat/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلید'"
}
لیمیتش هم دقیقا مثل
freemodel
هست
فقط مشکل اینه هر ip ایی تو claude code قبول نمیکنه باید تست کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6573" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=HwmIGIdOxcRdImiWbG6pQE_1JjFaVDl_8P9P7PYK6hnII3Z_OaE13RcWitnrPt8_c4uEtHAfu5B7QGo9iXnPSBK9B17cQQcQ96XWH-MYSa3Omzb6I6-GQmWX-nk35fT7hDeuZ7jthoxD-zRQVWXQBb1rEPVrMOgfsmG55wIoGG_wJhtKJAFYctDi7z4XPM3ZFVHQaHTCIy0DpVdKw_bPm4WB6EBgRnJcNl54i4lqOHN3pJUihV1FdLcBF7fcYahAhVC8pr0ooUgULEA7nRItkcGmTrV3JHQ0GHM1aG9l3IH8xQ1YujmJsVid8Kd52_8wqlEMEcHd6IpWVSmtXEJrD6OwZqeV0Dumul9TYzDatft0PUyD8k_QfnoTVu3MAit5EZtZfrcWhBdTb00nqupz0WZiJ7GzqHYvK_rOiBVqzxxZ3jnzbg1A_myeLRMQzgEiLKlvIS0omHqihksfu3_v1BBPn3UBBYK_-7J9qLixSbpeyFyfvXhT08_n-DWvHSdjK0YDXLGiO-_r_DWLE4ghxltLUV4KXlXetJ-FmNHM-GeJtu4jNvnc3upCN0cZXsolUiwDMJqdq7t5FD3dPC60u6tdiJSBQwAZghhtDRpHeym-5ir3ICbAojHeE2DDq0_o99FLFRps16kZVJTpnesxCVT3fZbqHbEL0PhNXEH0Qm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=HwmIGIdOxcRdImiWbG6pQE_1JjFaVDl_8P9P7PYK6hnII3Z_OaE13RcWitnrPt8_c4uEtHAfu5B7QGo9iXnPSBK9B17cQQcQ96XWH-MYSa3Omzb6I6-GQmWX-nk35fT7hDeuZ7jthoxD-zRQVWXQBb1rEPVrMOgfsmG55wIoGG_wJhtKJAFYctDi7z4XPM3ZFVHQaHTCIy0DpVdKw_bPm4WB6EBgRnJcNl54i4lqOHN3pJUihV1FdLcBF7fcYahAhVC8pr0ooUgULEA7nRItkcGmTrV3JHQ0GHM1aG9l3IH8xQ1YujmJsVid8Kd52_8wqlEMEcHd6IpWVSmtXEJrD6OwZqeV0Dumul9TYzDatft0PUyD8k_QfnoTVu3MAit5EZtZfrcWhBdTb00nqupz0WZiJ7GzqHYvK_rOiBVqzxxZ3jnzbg1A_myeLRMQzgEiLKlvIS0omHqihksfu3_v1BBPn3UBBYK_-7J9qLixSbpeyFyfvXhT08_n-DWvHSdjK0YDXLGiO-_r_DWLE4ghxltLUV4KXlXetJ-FmNHM-GeJtu4jNvnc3upCN0cZXsolUiwDMJqdq7t5FD3dPC60u6tdiJSBQwAZghhtDRpHeym-5ir3ICbAojHeE2DDq0_o99FLFRps16kZVJTpnesxCVT3fZbqHbEL0PhNXEH0Qm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=AharwdXpJxXt-LBr-UwvuJ8ydM9IxseDTIQ8pEWY02oDz_FoP4KIm4sfYWqM0cfMJ5nsvwSa0woKeMenB3-UY3lk5kG85HSNgF2FNTCDv3pILQdmWck9Ley6CdFEh3VuUAyLhhmWa6Q0aqPf4LZ7EAklgLVO77Ozah4Z2GgLTp9otyykFx-FIbJrDIGA67laDv5uit9RMzbtUMdT1Qs_d3VgR2PfIaKHk_sOwfI2hjxbYFWi9Vr4GIBztqHEHYthZkSHe8WFJuoFArru6tBzZPscy2iYhL3eyvx7-b1L1AKovoerMu49Gm0vX79DOlSgEIr7aX3wy2xOjm7Qu3Tk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=AharwdXpJxXt-LBr-UwvuJ8ydM9IxseDTIQ8pEWY02oDz_FoP4KIm4sfYWqM0cfMJ5nsvwSa0woKeMenB3-UY3lk5kG85HSNgF2FNTCDv3pILQdmWck9Ley6CdFEh3VuUAyLhhmWa6Q0aqPf4LZ7EAklgLVO77Ozah4Z2GgLTp9otyykFx-FIbJrDIGA67laDv5uit9RMzbtUMdT1Qs_d3VgR2PfIaKHk_sOwfI2hjxbYFWi9Vr4GIBztqHEHYthZkSHe8WFJuoFArru6tBzZPscy2iYhL3eyvx7-b1L1AKovoerMu49Gm0vX79DOlSgEIr7aX3wy2xOjm7Qu3Tk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYXfhogFdvEbi00kfEKmU2MpFvTqAhgPMgxdnzQwIFmojQ0vAnfTdOSxDwqjpB_mdDFGiC4hGJYEKJg8PSvIFE1P64H7UQuw-43qZ5Xu-7i4pLiZnbY5uClG8aWWZlhzPPnr4eLjLMXPulZs-f8Fpo03CvkkNih6XADkbeyUGLUJmfV7H-QOKLNCEGgJ4B8UAcVKkn9GZhJXCEkd0nzn6N6mXbGmcXTQ1dB8qqUdyrIuxciSypYHNFajdttyHr9zAsgEM05ozl9Evj_RWWL0860jfsj3HnuyPsiNou0VjqAfk8fKc3YQ9uBPRoAOOdMuRCCeGXSKscA9X1qpv8Y8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=TBaMo8QOcQe5dxR-mIFOQvgKuS3J4DqWXbr1c5m8HyuGDkUoVPYbwa_8Ktwz90D_42ihjllLoT8F3drNm_BYSs3uyDdbBQyVN4nO8_o9qmhk4GNg-hYpMvGpJ9Vv0DVSwyvgAk4bxIuXu2UxXERi1uTuBx_dY268mmsvEOLzs8hSkuhOicEsQhYs4b2joOHsUCTuommNfWY5J0nxhWq_AfoEZM4bKwzJCe5bnFaUsQEiyTTiX2m3qiCpA00HoZBSkEUCkHC7n-59LvHJ4vGpbIQfBw0iqj5dM--879dVOAWP5upIS24Vzd7ZI-HHUIQkxydg0RAT1YSWYXTBiBxW0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=TBaMo8QOcQe5dxR-mIFOQvgKuS3J4DqWXbr1c5m8HyuGDkUoVPYbwa_8Ktwz90D_42ihjllLoT8F3drNm_BYSs3uyDdbBQyVN4nO8_o9qmhk4GNg-hYpMvGpJ9Vv0DVSwyvgAk4bxIuXu2UxXERi1uTuBx_dY268mmsvEOLzs8hSkuhOicEsQhYs4b2joOHsUCTuommNfWY5J0nxhWq_AfoEZM4bKwzJCe5bnFaUsQEiyTTiX2m3qiCpA00HoZBSkEUCkHC7n-59LvHJ4vGpbIQfBw0iqj5dM--879dVOAWP5upIS24Vzd7ZI-HHUIQkxydg0RAT1YSWYXTBiBxW0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=NcZKI8sIrEcc2iWVlZAeeadCXqJ9GwOwkIJQqU7thlW4VQnIGcTmABzKrD9UAFNoJO1ZrbYI9JrWghOHSfX6V3VMQWSQ08mJ_OBNjca_qALZmg_pNx5HOo3YXBlF_L4RTXWu0sL_37t_w4pkKXOYn6Fu8ZprN2BGO2lpI7xhxOgsbmUTcGICD919jOJB9rCU8gI5GEBjIG2MiHPTCqHGBzMHBv3nfL2rrzxInVjc62y50xyycL7G7yVOZqYbZ2D34no7BMz15RBcp2jVNp9pbkwtYHfKcbOf1xuCEgzJpCkl_d1AmLLJKj7m1Sr28P2k_Ax6SPk7JDZwlztmZBWWNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=NcZKI8sIrEcc2iWVlZAeeadCXqJ9GwOwkIJQqU7thlW4VQnIGcTmABzKrD9UAFNoJO1ZrbYI9JrWghOHSfX6V3VMQWSQ08mJ_OBNjca_qALZmg_pNx5HOo3YXBlF_L4RTXWu0sL_37t_w4pkKXOYn6Fu8ZprN2BGO2lpI7xhxOgsbmUTcGICD919jOJB9rCU8gI5GEBjIG2MiHPTCqHGBzMHBv3nfL2rrzxInVjc62y50xyycL7G7yVOZqYbZ2D34no7BMz15RBcp2jVNp9pbkwtYHfKcbOf1xuCEgzJpCkl_d1AmLLJKj7m1Sr28P2k_Ax6SPk7JDZwlztmZBWWNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXtHeycMiGp_k1jl3uTh5G5_4UosS0KjcxJt21hq53iSNGPQW3lfZbvR85Uz08fa_Yfyeslk_ra3LqkOLFGfwoGakONYJkj_7yExWZSuxJXoFS0JK6HDwuTmlnNtR0ow4M8XGyfPYbrdGOPKqy5a7ERH3hc-5GFGQSdoyTFUq0VebwLUuQPnKRwuA2AJx41o5zLiiNBklP2MBF4Qbk_KQp2cxPOIVH_-8Kll2SHmq_pTOZWZ1qze3wrrjrVpErGRSLw50VOfQu7Pne7US5kVieDp9SdOlQNt0bYgJQIcUa1rJolwlcR0pnf_UYnu1nxY0kBGkEOEZWaOkS1lh-pEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndQciRwsCRTdqY2kvmeUVRfvGR387nQunpc9TNLDebZmtdRQFlCUho73HNDRBxDRNuwRAHC8YW7pgHuN13QpT3KDFEN6SdFEYGLTIusV5XWXcW_-PZgNyaSBvU3-S8XCpacb_PGdTvd8hemKhm4JO-scNKraUi-PlkA8Y1w1U-5QibHd8gxhzNM1PAfq0dlUeILsAr8XOd4BycVo9f7Bfnck7D3cmsHNZQIocdMVueWyingx4nKWjppz-F87nGdjNqFDRFL48vCzlxpwNpHyzrSwnNiTKkUaHOaewQYJB5DMRxjeFkVMrb0f1REfYC5DxNUJtLbhtY7mjeUXGrID5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVZrsJkTcq30NJvV1ZHCm4XBHXZeCNcNn_4N2GZMaOte9ouTq3EdJBm7lC8eXrYpBr_iUIy8XIITswvG4O9DgGIB2cGHQwppAOBGWUCvbkvNQu3JN7YilBvUqkV6AMZ8LeCoHvC5GqCFY4-hAsccjdApomjr3OyyVsrpV9kLCAaeJ2LRPo-mt57g1YobWBcFOGPF3TNWLPcarKN7SrbKW2cd6PRe8ukIPBPIHrbmkEfQxfXw7j0zaE3NNIgjzoHvcyiREvQQFlO7AUZK_iIKlmzAUwYDVq0NHizOF2TxBt2OKQWtD9udg28kCauouhXec5PS6IK_zMgR4UaFwWFYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=s6qVrKo_ZO9JGc4EDTQ7DHHFMGOHSjDYJ7PNTdhZuUuh8_EyaG1dKM22hJuk2i0ip-e8q668bRU5o6ujFafBeUddUBx0u-Ei2LSnrcGP4xlOGQHX_X_mBRcmZ1NSjdRjxgMtWXx6StHBnDTbfmtx3S7C3w5fQsL8ArydRlN--GxZF-tZNX0rUqxaT1z3PjZdY73D9eiMOdpeQBYAsQbYb0CEmwKn1xCW_WiU1qZJXlk1c6NnUQB05QLom-BAQdG4pUWnBnFnBiw9Blum-9db28P-LgEJI8CwJh5gdU64Pw96bK_3380tW-1BlyaJ1GFcoy-CD7TY5cN14bBoKsaMpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=s6qVrKo_ZO9JGc4EDTQ7DHHFMGOHSjDYJ7PNTdhZuUuh8_EyaG1dKM22hJuk2i0ip-e8q668bRU5o6ujFafBeUddUBx0u-Ei2LSnrcGP4xlOGQHX_X_mBRcmZ1NSjdRjxgMtWXx6StHBnDTbfmtx3S7C3w5fQsL8ArydRlN--GxZF-tZNX0rUqxaT1z3PjZdY73D9eiMOdpeQBYAsQbYb0CEmwKn1xCW_WiU1qZJXlk1c6NnUQB05QLom-BAQdG4pUWnBnFnBiw9Blum-9db28P-LgEJI8CwJh5gdU64Pw96bK_3380tW-1BlyaJ1GFcoy-CD7TY5cN14bBoKsaMpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=Znv0_JTetPAn_KxU8O33JpgENSYN-aLVIcTeKChw1RDG4s2uznKaLzFBa0tCTY2q-bH7GFbP2CTYRbLOrFqsAAMr9KSvSsWiNLGjwqp7BpPlWKrhgLye52Vw13qAMetyzKgIlI2JD8FUZ-b-fFBNTmuK7rXEUwNhLzFLsjW6lpGmQNilkgaCwJ9HIyIw_wOZD4fuGrlk7L9jW0z8j7PE2P5JwlsCd3886gf6KE5MXQwuc6kxz6E8WQhpIzHueEYTtAm5JYQGbLRCnXqOxzeTjAdR2A9vAtUeFmcLIyAzAumkjtNoCyqC5T4K1mMXFLCkhO3pEVczcFmKP0rgvsMEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=Znv0_JTetPAn_KxU8O33JpgENSYN-aLVIcTeKChw1RDG4s2uznKaLzFBa0tCTY2q-bH7GFbP2CTYRbLOrFqsAAMr9KSvSsWiNLGjwqp7BpPlWKrhgLye52Vw13qAMetyzKgIlI2JD8FUZ-b-fFBNTmuK7rXEUwNhLzFLsjW6lpGmQNilkgaCwJ9HIyIw_wOZD4fuGrlk7L9jW0z8j7PE2P5JwlsCd3886gf6KE5MXQwuc6kxz6E8WQhpIzHueEYTtAm5JYQGbLRCnXqOxzeTjAdR2A9vAtUeFmcLIyAzAumkjtNoCyqC5T4K1mMXFLCkhO3pEVczcFmKP0rgvsMEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ough2fhREG-cXVDa1G9nrQ-teNFwhw4YSI5RT-wXjD7X8Q3JFw-VURXh4RpMs3zp_L_PfKA1y6toEWe43x5OJFfTg5seWoRflNOH8OFEvkT2jGM6CKEOCdwrmsONmKkrib_WmUWk93KeCfARQpFAbvmsPJ1wC4WdYHpsy0pSKX_nnXcQGYZJFQ6iD4ynsd-lBj5HJHTSpy0IxmyUtgdCHz1zTvzs3WbtJeDx0It-nRSWEDncBp2i0SVRYgGi3cfVsRLYwTnTZwvT6-NtGxhJRKzV7a1_0pY4kJyBzKiikFDTqbFhyNtuP4KgaWmeKgs3qM830aMM-G2jiY5sxM8UZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
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
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g95b10Hd6Hf-KIIgJhWn20ztJuMK2P_rUuyIMbP_LVnCAmB6kMo26ifX1HhjQflY96ZDeELCxm_Y8LZO2wARZeTNhqq3kFrDT9Xg5DOB696x-CaZIAeKD5aBNvYkweHiFf5O35hlUxp_oH-vBIsq81bOuYgk5xT1i6jLgINHxkIZiAXVgp-0_hhb5bKH2ds4FzhuFucwWH8vClq31FYT6o_7oi27EJJwO5lQF3FnrNoPOla7MmKMd-hOtyJHx152Q8w7n9zs6vZQxODjtFphwiiPJ3eXt1cKWfUaoW9APJVoF_nOh7prA1jqZjA7PEYQthkvb7GQ_onbfiD-s_sHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwqCNFtXg7U-qU1vbgCNbx4EHw313fFr67E_2fSwKN9TWhorU_zFCOX520EnWT2LLPQd4UACw66rjHXvvx2ARzyJfBb_6lbcRVG2RanhDR8zUUVyj0ASucEd6udMESGC2iZTRLPvwUUkcubrqJccwybf25nbBF5hTkjORuHZWC2BX7mdzXynRDbB_Dt475Xj-DxEhCRBmbeHT1cdT61lOEwTZMsS2PihFxxH7ovL5VGCVMpRKkP9evMe0dDQKocrtWZqfhhdyfKb4tbzj3mdS1LDsw_fHQVTXVHCvMAMKj3eISvp8RsH90HJ6pT278RlNff57SiyenexqBd0zwoaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfXIIx3jrduRsRebRYvbrVIKT-hRaeJoxZRWSpPDBn9GrqWy2zA9NXJvR5LXfPj4hZvjB3Y-JgQ0SPQOAqnRvxOTf0WG_0ftvd_jLvsGCK-Q0u12LX037xmkOLXFGYilx3VwYj_ay4sVLZEH_grBPbAiyF6SIAQGmuxCSnAK-DNL908lq_IV82jfCDwjoOvdAZLAtbD8wkqBo0fffbJqfpzQeJjZvBxUgWPjPI3sIh1Cwmo6EZRGk964XEt0X9cQlkmiGPWH7pw1BJ5Pij76gXPgEjkBr3upcZVYQETZPWXIP-R69uUrbhI50pc3qSh35qzYfa3tiEnzmqljf5NHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSokPuEe4LDUdogk3IwKfqCL-fAEUhNUNFGsU5L1fL6aYKH-q-jDpNPuRZ40v6MOAqO3RYWL9CqH_ttiHXP9mqFACfqId4pyez7GEZM3wRcBqSUDXO4mwWuDf-XVuPefd1_hlm6iLnavFo7-jlgskhExFniGwhQo6I9umO8QfaTyJl8Cvx72W9PGddkYQy4T5zn66c79z5acOQFG9jdqi_as3MUv2Cow2MWQBst-n21ujXAHKbFQ4HMsk_QZxdqFVdFZ6994CFkq9p8N6srC4xdmxymYZ-_qRXCsx10Cdjr80phffk7-wY9V72A0_ttMA9hsvQp_kvVWndSWgzcDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwJhn_JNsAzI2ASjGhd2vtKDSbXv2UiXgrxSY0_DCIp_JWCO-tfTp0S5BmU-nSeyS60m50BZkHzcV22uhIqqzEY632tnSIWq_ANJjdb1Gwwnei93SZBP2RJx5-5D8f1mjygdJTaWaJtb7TD3UiUTJ58_tBNeAHJPp9_GFgMtr1aGH088SpLpPMgynHRJ01qj2Mxz0qwoYZSq0ohupx85OepjFCKYospqtpgT9t0nvO6A9rsggIOXwp1E4BJfY312aietFA6ju1koR6L0PKEalM40ksFjPgj_XLwwNowbuWO1fTzxjxY3rghYANYZBdBxm1MhBxcme96SU2sJomgrgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iItGoJ7FI9v_ed0_jwO84h32j6pa9qcbhghFQzapIwlk4j94m7lRoUUV1kPSyAHiEpyDqVejUlyl9IbH_IVkHCzv5Ll03ACMQBBl5tddMP8Dr-z4kAkKQxAISSNgzyVak1ol29MlI9tduOEI3f8Rm9M3L5Rkiw6j6DDWjsbf9jhkqPt-VjUlwPuAkofBxvGiHVve9dFdRehYlivKrey0IQ96GEo-j-KKI1IRL1RxMAqjl9CZ72i8Xf5U8uFgxsIsYwDe3rfko0SXIAj4Kw-4JgnNKXfAQanOfW558FXuwtu-dE_BAZ1CQFkDlidAG6w4o5Q-e0zfIv5UQHhySNmGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qK2uI0PbosA7OfwQeAz0uCXjinxi2JDpVs4NjO3cyztj6z09q7CsQvcy1L9yARqPCeISpYePml_WvdQRRQhTBUfN7HIVVP_D255w_lAs2oi1L8saOCR0VsCgX93Lk0UBIQCbdadyGhK-r5077MWlq6nZbtdBCQaPCWV7fQQspsII379fN7TGgio4hTQKp_sUPekpCOwws9RiziNp7SY8uZy34Hej57qT11hdHMKS_dw7oNu20Q4V2pEGkcAS7YUAyvoXXyq_fsI6eNfwDAeqP1PUmXOSzyfyhnsMFwrEST6Udy8-8zOUs29pR_A-O6dNWkeIMC3HYb-_MZ6bImhtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYaaWDnQrscHfo05EbADYAHCCtYvSE02JlmkstKOsnFIYiLCXZeMTnL88deq8rLd4w7F_4FUWDV4rGbk9ifHrWYXBZHJK1tideXJv_aCNxj0vGaJW214uPcceVHhkx-CHZPLbe6QLNbtKNxUYHs_8uqI838TyyrF5cf3EMSzpTctWkzi98jb-9ahuLPJ4VXEZfGZwtYsZELBOzm82zRSYxqc9IO8Lgakr_tyy57jDVvmTxYVGK3-3vKEOhNole-AnXVwuCRyERpyzXTGK2ke4PTawbs910ABPTB6aDDGJx6wGuy2_v0dZNTE4jzVSgRJeJ9oskInzEOs21KKxDlkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldEm6_FzCWVAMvOkm3YWaolYOIO_NSLyTaKNPssLVMEczGyt6Wfb8JqZCnVFpDNJfvfbuYecGjdmyfL8AF9VvHIF4juHLyMOb_YBzq6WeUFjUac8nZ7ubIxb2Gl5k_RMOPxLMZpx-sqVK0R36aTVYL1fkDwpBH8nTVe6OLQpRh7hWpkeZCQuWU721c_G4-i58Bv3E5QqF4tgJtIeLxb-b7Ojh3-p9EBDFG9y_s_s-wFYJPlr9adZUmJhwfWQXx0Rd0sPyEhfW5JWvmiTi9BPFdR5-qIgllWOxIg5eQuQW_pHT5HgA6itew2t74EbxLWpxJgUNIm1QBcXK2KJBP7uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOZWbVqE-ruIVxrb5JPZdHkypQ_rnZz9QYmGWPZeOxDnGlIdMZLuaYSEp-ogCDQPET5d3WYJRalWZlIQCn5qVRia3OkCo1zIwFl0WmObAoQxyKhfNXrZy0YcQ6kThEr4BCn7RADQSD9sMT1J1qtAB_V1ernRJeNRc-EWM46mZXurS4IdzP6QSwHAXbdc5ObM4XyEjY3KZAKYzgG96NSwDBWixybs8z0jLk7dKLYdSITOkuOTkYGHDt1r9NQCtATKF5-aB0ozjY75tC6qhjhMsreC2c0uKNXANlFwNpqzVNKKrSLmtm-QloAvlRIA5YtJ-pC3-h1JlxxVLgWrBqSh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgVOXZQS5G7n271pps4pSj9VLLp4QHUr1afC3PbbN9SKy_hAU0t01f3JeZsDmyC-GiRwfYd5kRcN5T4nNYtRnxrNBcrqQ3knYyhxDJjPikh4GOOOchvWJveYejVoQoFlzkUOHbP820BuuNZohWnUtdcK2EzJs-lBTsMHmB4IZIpgeUS6YvoPX-cGRhBF_3FL31oi4-DkOnq-RHyXkoHyg7h0U2wzGIUtXoxoJyjAQW340syAuFekEW2XFLGQo5CIEN18Nwo2XsbTEsRdViEFMGBhhZNTZ1kJQQe-_QsFElpnXDeHQM_n8Ps6Tug7kDMLLFT1m8kAQYGUZ3noklZqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIEeQQI1YtSUGuuH0YT2AyG1LHW0CeX3a7GqB_XIlid-Lp7pGmYSAbLsvqUGt3IQc-acZlYZqyEZhhbhKRJ4I0jngVNhl_fiwoZ1FqXH4iQ9R-RDgLusujqiADZtJGx2AxUkKFKAhCrpX1fhXuW_uwUKT09nK62yK9xOItP0f2rfmxdzu65LNtcT-4mw1GgQF8eQwrlX_onDwtCaVsvwm-W-d2ewCpMyWYsefEQdB4zRQDuU0XVWGOX480Ng7Aenp4w0k3mUCiNygrBFVHsIzi2mHiRlnz--xlsHXHGInW0qcutI4qQXf_kFGNrogCTWcO3H8Nks-tf9wJfWCC2T_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAUrKG979nwcsaP12n81T1DfOQelgxpBTky6Kkm9_leipFMh-bXn4dwt0ZvqKGOLbjJvSyejvXhsTDw6oX-B5AvBdbsamSSyFoIurquDJC8Rd-EUNV8gUtYtvZ012uiQFM0u9znu4DTcOTzylz1Kx3JiebRzO6qlg3AgO8Q-ePXB4YTqbdkMKy96VCbfR7RxD0QTvHwxRmtIE6cuF7DAuE8hgkqBpHPHPlrbUMfJrARKHK_G8-SUGs3IIvvWmQ-nrNjFbm_IneuNeN0YaVnoMvUyzct9HsbkNyqXOCRpgB4e2hsDwwkiUEczdYwvbaIXQ8MNwZUBxkbKNpm9gCyyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=sackNvmvjU-D9tvSd-E8Q-7cRtN0wt5oArIb4-PvDWcUWa2onfMmm9urPoe08ifHXRsR7zMQjD9rGSIrsLlj6ZSgaItAl3w49-A5z3tdjiJ_shCHyD39NjJBzIoHlZoYKkKuj5FtjO0tsyqGor_7MoJ2ZYQBUUOVj8Y6sY_A3NQwV1TvHHnGI9kU_rCeHwnN9cA1Kj9lhLE-jBUkD70_LS_nJgYVkh30EBFP3UTiBRaP361UJPU1aVb2Utd8H5EsCW-bofYGyPQgCxyAE0Hz595wuCvG8PUoiq1XiTBPL8AfkNC9V0ZWMQrk8LKJSMLxQxjRFJblN2x8oObxGGCpfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=sackNvmvjU-D9tvSd-E8Q-7cRtN0wt5oArIb4-PvDWcUWa2onfMmm9urPoe08ifHXRsR7zMQjD9rGSIrsLlj6ZSgaItAl3w49-A5z3tdjiJ_shCHyD39NjJBzIoHlZoYKkKuj5FtjO0tsyqGor_7MoJ2ZYQBUUOVj8Y6sY_A3NQwV1TvHHnGI9kU_rCeHwnN9cA1Kj9lhLE-jBUkD70_LS_nJgYVkh30EBFP3UTiBRaP361UJPU1aVb2Utd8H5EsCW-bofYGyPQgCxyAE0Hz595wuCvG8PUoiq1XiTBPL8AfkNC9V0ZWMQrk8LKJSMLxQxjRFJblN2x8oObxGGCpfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAYKcliil9hLrBb_PBr9QyVOqQHCYSqRjvtl_4tDGuwoOzez_51IcS0ISpDw7c0tJL-O4w-5lbZ860iIfdjZ5IlayXBKxpLhcVRheTJaT_iRwLfvvu0v4N7lxWp_9Sj-rC-5nqLGr8hptTx8hHAAyuctG7D6eazu2A1ttV0G4zsXZhvZlXbOx1t1kmhvyppMpn_X3S9MpwyUcSQN9RoFt4gdaBpBUxDBMSiNMeba4IpkWCgx-CrpEc5e-3I_7cNkEHl7uXTAZE8YzqrYamIj9sDApPIJzsSajs_GHtBf6sDCUz4U6Tsfa5xAx_0F_58L6cNVjf3pmeFrPpadzdoeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdMUFvqYoLROritix4_N0ev19ym_3irxhV6kXexgarh9eVjG1Zxox1B-reJ7WXVijX3MRUN0QMRUR6-qS4xUYlseNAO1hO9PWHcMLsytLC5nZEvH_zN5_vnjQ-hdnPM1aJR-F-E_5o4trLV1auYU3__sW0e5SvSIGhiKBgwse46SQnGz6hA5wxAxZz1XtscemC4ooF-Rda2XMuYF2fv2zSttpmVsZdmGqKsmhkE07NX5JTEOW2YG2TVD7HC--ke4zW8NLqj8CQXZBklS9l7Bdk6-XtXm6EEm4binO2TpG57n4zMTPDqHH0rG5Ds5hd6_xsYPh_ti8qMqxGIE5TTAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAdxR3Oq-akgrSgGkHoJzYxFoVsPcLOzycRrSjj-wfgHtMdXZFweJD-e-rRJkCkIm9GQ2hc6Oevc7t1Zq5nts2tol_xMNbu-5CgUDbUpUoyZyFO1wXO4G7Q2pnUuo6UUUvDlXImrfLIKvjGPIUadJyO5Cqg-zTF3N9N1iqFWWhPIlDx7cMbyhtefiEXTH01u-aH2I3whmpdZcaBiyFi1qVg6arnxIthWZra2XS_Fcjd1zlTLIySXZgJRVadOsAuBkqReRtc4YtjuzkuU25nHbZE9u1PAMMMbsVHEN72r-Xh44rDoOPOFUHkcMY-uhy1y5w7Dy2PKJLwjGyvGhJof7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
