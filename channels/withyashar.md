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
<img src="https://cdn4.telesco.pe/file/nf9YSxSbNLBdPe-iswn91_VEdqkZ5EbOZg59p21ymn3w63JluuuUNIui75zALQ9XWa0ljKCom9LMlL6xnmJKeOxOb7sHCmrPGF3kMTO0wd02wKi8qodDNjBf6o8_ANgtHlOrngk7rIW06KdL6Pr_D1ocSJVB4cBzGqVKFtXS-XdiU9zraGgGYs5m-mIaGYYhs-MiieZ-AXL3HUqdqNLHMECdJjE8sbb3bAzDFQ-ERTVBo1h3uPAZQMP2dByaccwy2Jdya9h207-oRiCIzJ2OMnrzONsTFvBPHiKLDBUlJPBbAwjvG3M-hSW1vdzVWJxYx-IQVFJPTX2ZEf-j9dGCzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrHPQIdQW7nLOBQNyGtYyD-YgJ-teCEgPCxAropl6NJQicubFKcx-wn4oyZBZ61D4DvTP3T6rjpWDuU1lGtxiSFzXALXCk5aZqGV--qUtTOxgdbOYE4_tbXmqqHd7aCxzO0_J_o3iYC8DannL70rFydEoMockuEMVj73xILRjvLrJRgrAzlOMhALF7V3yYS0dxnto-DuZ--9fa7apyI8tzH0mGGXtDA2W0g4v5awcBHKfHUgpBCxiS4j6rQajKf_VJ9OLBdgQMs8EXelSWArt5TGxqJs3t-hOFIOycGCzK8Dp124ZvXhhLpb9p0mGF5QjnRlyMsD_HRIAa0CiBX6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y69YhraUlCUVhY89XwXhh0PPvnd6AunIF1sTxcR4-F02sodc5gvvg1_9cNqRiCabbCG3D1iIdILdbxv5ecvkedZrhOx3J9GW_JTeesWFrfRZKu4LTFg4LPFE_fhIpu9sM-6m8ewfRPqg5Gz78yKXMAKf6uhjMGhi-m4CGVu3_BICD60Wrd7FTtd8-JKkJj9UMIvdj3sgYOnsLPhwzH7CPbd81cYc-DzoeSivHzJbbZxvfegK5zWjv0qzzn8rO4KkbsaKA2JV4E-fvEFLWulJr670Ry2x0QZOo5AOZ_uWXBODernBUe4VOAVqyPeYk9uI7M8G1g6T8R9jhiFg-G9nRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16211" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وای نت عبری : یک هواپیمای مسافربری شرکت هواپیمایی الکترا ایرویز که با نام تجاری لات به سمت اسرائیل در حرکت بود، پس از آنکه دو جت جنگنده نیروی هوایی به سمت آن شلیک کردند، در هوا چرخید. طبق گزارش‌ها، خلبان دکمه‌ای را فشار داده که هشدار ربودن هواپیما را می‌داد. این هواپیما از ورشو پرواز کرد و در آسمان ترکیه نسبت به ربودن هواپیما هشدار داد. پس از آن، بر فراز قبرس پرواز کرد و پس از عدم دریافت اجازه فرود در قبرس، برگشت و مسیر خود را تغییر داد. مقامات ارشد صنعت هوانوردی این حادثه را بسیار غیرمعمول و خطرناک می‌دانند و تحقیقات فوری در این زمینه آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTkDVKn-1xC6g4T7sifscyVRZcU4EQtzqxNXEHa0RQkImVffr8Fg-Cku_t_CUz4DmUE3OVHaMe40gFaUDpIkq0EES4V-aJhX_MrJYMwZoYSnQLlPXmkLwYnVLA9M9nr3GWUNGCFgXkIXKqrwcUWATl4nPRDBTPuOsST1uwLlWj7byRiV5SkTgTb34bb0FTduwDLRfZmsCLD2yoQdExEgHbEA_mMQpLkXn-bJ3XmQ84pl0lpCtdunFHWIMOfmZCn-jizuhcXrY8xoATTmUVT7YTTCahQKrBxORJXFNKAIWX4VKpfu5WjwVYbVhOPb6PoJw8m3vVgBj8cpLlCUcWXF0Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTkDVKn-1xC6g4T7sifscyVRZcU4EQtzqxNXEHa0RQkImVffr8Fg-Cku_t_CUz4DmUE3OVHaMe40gFaUDpIkq0EES4V-aJhX_MrJYMwZoYSnQLlPXmkLwYnVLA9M9nr3GWUNGCFgXkIXKqrwcUWATl4nPRDBTPuOsST1uwLlWj7byRiV5SkTgTb34bb0FTduwDLRfZmsCLD2yoQdExEgHbEA_mMQpLkXn-bJ3XmQ84pl0lpCtdunFHWIMOfmZCn-jizuhcXrY8xoATTmUVT7YTTCahQKrBxORJXFNKAIWX4VKpfu5WjwVYbVhOPb6PoJw8m3vVgBj8cpLlCUcWXF0Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXI_QhZsaH59P3WOHEGo3QaoNYPpa3J_pQW-wU4hahwZrtLN1MfoI1rkk_e4fxQ8fg89tTN5kIiGPl0Jh6cb48T3MbpqKCBvtn7CrLE7uco67yt8yjIiNkcLEiTs-nJbhIqNhbsDwMDPreOSUzIVFeBNHNfJG9TEYGKQMX7jValI8c83ToXw7ATw0njpLmQFBtT2OQ_HxTK0gOHF8pTdnzIuU0VWbyNH2YUui1EcNqU9fm-LOYN_iB-bqCzayDfNiqUpFx0RRspmBYGhUoEV5JpC9HK2_u3hNggHeISZEuaOC5GMLmsmgUrUpDOX4nwBAMS9j0xAmB9lXN8stoKfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی :
کیپ‌ورد آرژانتین رو حذف میکنه
،
من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/16202" target="_blank">📅 15:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی وزارت خارجه:  آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند. @withyashar
😂</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/16201" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@withyashar
😂</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/16200" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF5I5J7TyU14oCxQlU9g5O-otpY69PttpCcr7IwnAMWzeiDr2-eX8COKTmL-sc6Oza6cxmux56Lduajlv-oS7BsBGLuveH--gBI2KPeAFqMefAbRH8ImFwGeiXtI4z3IqB0fmTLN-UNTHkWBS6Hzjlm63OGKMXKIii7ARLIlN0o03bbiHiZiuXYu-dsGYKq_mxxWqN-e8mEh4bUR8EmdrjiZQcmMcQIAEp1GbY7ly03HAHASa7kiOvnVz-BltipqXysa8HUZX2D_ktpSOjza9dvgkrwwAXpTbrhDBfHLfpNz0ZQRfcQwqSZ49mjilh1VEfZsUOw-O9aBCZnsHzQ7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر وایرال شده از تعزیه محرم
قیافه بعل یه جوریه که داره میگه خب عاشورا من چه کاره‌ بودم
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/16199" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دبیر ستاد تشییع جنازه خامنه‌ای :
مجتبی بخاطر تهدیدات دشمن نمیتونه تو نماز میت پدرش شرکت بکنه و باید مخفی بمونه
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16198" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند  @withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16197" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر : هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/16196" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR3jcWxYjkvYqdOdEyKIBD19EY6oL50on6bFXLaKjts3GwM-v4IyYIbPR_wtfWpfNmg6Rn8xaZnoHwRDS2BAjkUtm3depkg8oDP60rZJLbZmgA5ZG-p9cfjZrkGMeyMOA47t4zRixNENVqxSe6TBTj-_sbvJiqVKQudPNcqPZNEJUVLXRiPoheaLUjS0TPJHiFVJ-pO2pLm3exifVh7TGMoCYfq5TV1l12B7vqzTAmQ5uQr2BZ9yp3xZ9qEKI4gtLgAhhu5dKFzlYJjyDAsL1gtf4ZYe0lfB8jon96k5ngRVyYxW1lwpdVIBPM4FqdReHVYjzYTwcyNQo09XP01xBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی آمریکا موشک ضدکشتی LRASM را با بمب‌افکن پنهانکار B-2 عملیاتی کرده و در رزمایش Valiant Shield 2026 با آن یک شناور آبی‌خاکی بازنشسته را غرق کرده است.
در حالی که B-1B از قبل این موشک را حمل می‌کرد، تلاش برای افزودن آن به B-52 و P-8 ادامه دارد، اما B-2 فعلاً تنها پلتفرم برد بلند پنهانکار برای شلیک آن محسوب می‌شود.
ترکیب برد بلند LRASM با پنهانکاری و سنسورهای B-2، توان حمله دقیق و دورایستا را افزایش داده و تهدیدی جدی‌تر برای ناوگان‌های دریایی، به‌ویژه در اقیانوس آرام، ایجاد می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16195" target="_blank">📅 12:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر امنیت داخلی آمریکا:
پس از حذف ایران از جام جهانی رقصیدم
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16194" target="_blank">📅 12:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک منبع آگاه غربی:
ممکن است اسرائیل ابتدا در هفته های آینده وارد جنگ با جمهوری اسلامی شود سپس ایالات متحده آمریکا به اسرائیل ملحق خواهد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16193" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد که مارکو روبیو، وزیر امور خارجه ایالات متحده، توانسته است دونالد ترامپ را متقاعد کند که اسرائیل باید حضور خود در لبنان را حفظ کرده و علیه ایران اقدام نظامی انجام دهد.
در همین حال، جی‌دی ونس، معاون رئیس‌جمهور، ناچار به عقب‌نشینی از موضع خود شد و در نهایت اعلام کرد که از توافقی که با محوریت اسرائیل شکل گرفته حمایت می‌کند، نه از ابتکار عمل ایالات متحده.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16192" target="_blank">📅 11:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjNzPb88K0nW8qgT1g9Yaznye5dl4gQJlZimtVH3N8pI6u3DWvK1wL32290vzEwY0NfETG_y3k98R3-NeI9tH4qAb0gA6tW9W12Es8yuMcAdGgwH6BAPbGM90La4Vmuf7hdqUUL7AQy2nmTurBE2_O_6yofAg4cYHmicIxFHANZAB9o1GgBMblC13gRrVF0AJ4ZK_XwmtII5nZSMixWRtXC5B2JmqEx0tgZyU2DCoCPYnc7FzgtG8U9bsgQ6nEgnmFVHHScxlQfEJBNOckMazXs3T1wSfi0IOOzGg2tc5PpT_5YUc-tfSyYPHYRXjKTTWNdLK8gf3gNa_-baeyo3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ثبت شده از محمد اکبرزاده قبل از تصادف و مرگش
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/16191" target="_blank">📅 11:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxPLtOmuXXCdJT-LhhZnmT9ftTRodpb1lqlRPyCe__1RT6AOb7koKTXa3QP2JXvVd-KEPc7_xc8DVHPx_b9vBfnz_XHQ9UgHNSRuJ_9empmXIfyD3xJdLJOXIspjLs2piM2zLKmVrIj192D2NObp8121kzVDeh0UijLoK2BpCaO9Hez-_1B3uGbJo3YPxIebiCsODYZn_-kE9udKcdWZRm6cULzSFYYC0HpDTgIMkRErXYR8eOFmYWl-FFTlnp2BCP6Iq2gj1BG4CrQ79-AFjHZZoJV1Yfxl-JjngNmm-pIoZwVHRSybegO_PJdGsek4dPCXwHNGMtzjHgLBJ6g4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان انفجار مهیب و برخواستن دود از سمت فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16190" target="_blank">📅 11:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اسرائیل در حال آماده شدن برای شروع مجدد جنگ تمام‌عیار علیه ایران
بر اساس اطلاعات موجود، اسرائیل در حال آماده‌سازی یک کمپین مستقل برای آغاز دوباره جنگ تمام‌عیار علیه ایران است. این تحرکات نشان می‌دهد تل‌آویو مسیر جداگانه‌ای از آمریکا در پیش گرفته و انتظار می‌رود در آینده بسیار نزدیک وارد فاز عملیاتی جدیدی شود.
در همین حال، فعالیت موساد در داخل ایران به‌طور محسوسی افزایش یافته و شتاب ناگهانی این تحرکات، از تسریع آماده‌سازی‌ها هم‌زمان با عملیات مستقل اسرائیل حکایت دارد. هم‌زمان، انتظار می‌رود در روزهای آینده موارد بیشتری از انفجارهای مرموز، آتش‌سوزی‌های صنعتی و حوادث مشکوک در داخل ایران رخ دهد؛ رخدادهایی که با الگوهای تاریخی خرابکاری و عملیات پنهانی موساد هم‌خوانی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16189" target="_blank">📅 11:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد !
۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه
یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا نزدیکی سریلانکا به نمایش می‌گذارند
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/16188" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=dGV98CL5XhV468ROz7YdyAZL5RYmusSDK07wXseY0HfRrgKGS28XbGwO9vIkrPZG4P9ZZffXBRF2y6Rgj3pX_vCi5Y93Ilh1mN14cC8_DgOe8iLdcSftKwipj1WGLB4O55B7HCDRjtoGGO7FyyhvixnN-BUUP_XHWLYcS5vpjhYfzZp3tGWpplFMZp2R_WG3YFwJWuMRNyDO305OQ0Qyg8D06Og0RTBvrTh2Wkhmn1y6tKJ5YPEB1JLzdGWndQ2ohwvFUpDNGWP9P2nx7c2v2hKr6WktSYh19ystu5lbAmlQ6M8xYKtRXwXTXrdDMT_O1iR-r0NErXmqNnOYSEWrcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=dGV98CL5XhV468ROz7YdyAZL5RYmusSDK07wXseY0HfRrgKGS28XbGwO9vIkrPZG4P9ZZffXBRF2y6Rgj3pX_vCi5Y93Ilh1mN14cC8_DgOe8iLdcSftKwipj1WGLB4O55B7HCDRjtoGGO7FyyhvixnN-BUUP_XHWLYcS5vpjhYfzZp3tGWpplFMZp2R_WG3YFwJWuMRNyDO305OQ0Qyg8D06Og0RTBvrTh2Wkhmn1y6tKJ5YPEB1JLzdGWndQ2ohwvFUpDNGWP9P2nx7c2v2hKr6WktSYh19ystu5lbAmlQ6M8xYKtRXwXTXrdDMT_O1iR-r0NErXmqNnOYSEWrcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنبریان سخنران صداوسیما: اگر ترامپ را قصاص نکنیم رهبر فعلی باید بدون شک تا ابد در مخفیگاه باشد
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/16186" target="_blank">📅 10:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oulF2vLsEoKBB4IBnnjiXKDzLqe3LyYTF2oTFIkP4fwTrcgncLIJ465BoBkUcISlBwAu0CYjVHg02od0yCdLHygZ7u5Mmmt_UTgOM9e7_5t-evDlZH0s_hoA5bcFZBSyQSFBjqkUlSxv1O_M8ymG_dx9evIvMtmi7gdSylTFqpdXtFcGwcFClpQnNzhEgcgNpDE79xNwvsV24CuA-hpeh9IytNi1CKnA83P0qqR55ehqSBu1ktm-sVBm8jo8FoPSmtRO0KxLVRf-kDQQk-W7-73xVgaezVVZoi6JDhITT-uxPhFBNN2Ay2aHKhaQE7XZDtTtXWqGmPM_L6bj8di4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو نیروی سپاه پاوه ترور شدند
روابط عمومی سپاه استان کرمانشاه:
طی اقدامی، افرادی با تیراندازی درب منزل در شامگاه دوشنبه هشتم تیرماه، «برهان کریسانی» و «خالد خالدی‌نیا» دو تن از نیروهای بومی ما را هدف قرار دادند
در‌این عملیات خالد خالدی نیا بهمراه خواهر و خواهر زاده‌اش کشته شد﻿
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16185" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسناد محرمانه هک شده مادربرد و تراشه جدید آیفون ۱۸ پرو مکس فاش شدند.
بیش از ۶۳۰ گیگابایت اطلاعات از جزئیات کلیدی آیفون ۱۸ پرو و آیفون ۱۸ پرو مکس اپل به سرقت و فاش شد.
رویترز : فایل‌های حساس شامل فهرست قطعات و تأمین‌کنندگان، و حتی عکس‌هایی از مدل‌های در دست‌توسعه آیفون 18 پرو از طریق نشت داده در شرکت هندی Tata Electronics توسط هکر ها روی دارک‌وب منتشر شد.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/16184" target="_blank">📅 10:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حزب‌الله:
قمار سر توافق ننگین بی‌نتیجه است
حسن عزالدین، عضو ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان:
صهیونیست‌ها مکان‌هایی را در به اصطلاح
مناطق آزمایشی
گنجانده‌اند که اصلاً جای پایی در آنجا ندارند مانند شهرک فرون.
دولت لبنان اساساً خودش را فروخته
و به دنبال فروش قدرت لبنان است.
پرونده لبنان همچنان در اولویت ایران قرار دارد
و جمهوری اسلامی ایران این پرونده را به هیچ طرف دیگری واگذار نخواهد کرد. معادله‌ای که تهران ایجاد کرده همچنان پابرجاست و ادامه می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/16183" target="_blank">📅 09:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شروع حذف‌های هدفمند؟
دریادار دوم محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، متولد ۱۳۵۰ بود و در زمان سانحه رانندگی و درگذشت(دیروز)،حدود  ۵۵ سال داشت. او تازه سه هفته پیش، در روز دوشنبه ۱۸ خرداد ۱۴۰۵ معادل ۷ ژوئن ۲۰۲۶، در فهرست تحریم‌های اتحادیه اروپا قرار گرفته بود!
وی در ماه‌های اخیر در سخن‌رانی‌ها و مواضع مرتبط با امنیت خلیج فارس و نظارت بر حضور نیروهای خارجی فعال بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16182" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دیوان عالی آمریکا امروز سه پرونده سرنوشت‌ساز برای دولت ترامپ را تعیین تکلیف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16181" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv-O2nvAbpFKtTC-Uzh-SoSGskVGi_4rscfIKvS1AEzeSVftZru4cIUwZdAu20vYdITSIqd5XvDB5HDEjFMPHFjs1RTdd3-QKwpnswhktTl-MckFcdn2oUByrq3C5Nu5qMxfs_-s2iAFwcINL1ZpcwTflRN17RxtODPiDH0nCDJc4kXjTo1uVZ-1Ap_UKzjW8qSv7jpkOeaHKfnU9kKcfKOzm7idsijVgSh3EW9wg5nuR-A4fvAZYYP6fUvDS2BWBkVPVt0tjTd6HJtKIT6PyrHUSsHh8kq1-CjBMpp-d6khQ7VLm1rGnL8yICfyPhTE4u-5t4KtuOFE9pHa66r2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید روزنامه همشهری :  انتقام قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/16180" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روبیو: احتمال شکست مذاکرات با ایران وجود دارد
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/16179" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ به شرکت‌های نفتی: «قیمت‌ها را کاهش دهید - وگرنه مشکلات بزرگی پیش خواهد آمد!»
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16178" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me1GJsoXbzPAUlZ_Ml8fBA2rYxQ97gudWvOAoyyieApJj3F4tuUwk9IQtDln2IbfNnPuOC-4lPOL56q5PHlb4XpMqep0I-Kvqsz2qJKM14iiGx6aw2FHC9BUYRyokmtCEMOhJn9Q-IQxtSw4jYg0xhF_dIdtnTpjEmuL1Cd0ukrYHLgCE2cmycbjPPEgSwfTbXfD3QJnmSjMk4zuB6tJtfm1rD76T1bxb8b9w3BS_b9fx4Inovwc3ln01nnABv1CEa7m-NTUjd27_faM0eDApkRHAWSU9pmip1E0S48OiPMBlzofxvaJx_TUuRXd3-GawrZPv9mZ-b0BMh45Jk9m-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار هدفمند در موناکو فرانسه
۳ اکراینی نفر زخمی شدند که حال دو نفر از آنها وخیم است.
پلیس در جستجوی مظنون فراری پس از انفجار «هدفمند» در موناکو است که شامل یک وسیله انفجاری جاسازی شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16177" target="_blank">📅 08:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حمله مسلحانه به ایست بازرسی پاوه در کرمانشاه باعث کشته شدن 3 سپاهی شده که یکی از این افراد نقش مهمی در قتل عام مردم در سال 401 داشت که به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16176" target="_blank">📅 08:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو : اگر از غزه خارج میشدیم، خامنه‌ای، نصرالله و اسد الان در قدرت بودن.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16175" target="_blank">📅 00:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj8T26SDxojPQtXjsgEuBgsjnGoylhbla0tYUpK2MwGJw_9zN1GAOjqJiWpf465jZHlwnaMF9dPxnWnvZM9LA3vlAjkADA0XH6Vz9XdP40P7PxEq5a_RkPY26FDgbopiQN1QBO7zuvaGC0Cr1CxJ8hxtxuRCWvL9eqvmv9KYKUuejuczoaMdtvVl4QZpBNw6bj7dvUij5I3E5J28V8j-k2dNzidtlwT_tseC-2o6AhYqa3_tG5x5b_Wu0MIf9Z9GOhY6mBw4qhUrvIMmLr5sFgDMhrxvT6XPrHyi3NRIKgArPrmOux0SdRfywMJol7Sqm6lvZEUClE-nfeXKFjVv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سنگین اسرائیل به مواضع حماس در خان یونس
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/16174" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI0405fFLFpimxpHmkAc3Gz6UQzpKx-1L-rTcpltv3t63otl2IHGTAV4RbOu352TLgocbQYSt6SAE_PZ7Nh0n9SZCwQS9eWXM-j4NElw4QIYB7Fw7NhijqqmmRKRmdm4Yt3SAhwmwrE2yh8cPBKo-HRsJzUaCXj3dwQ5et9Dka2schYxr5tw-0UZb0NtDsjP6z-RMjztu2dOS_-dscZwQXf0d2sWgr2ZWJGkjc0hARiMgwNRPpuhzj6RoylqwxN54W5Wzmcfwy5pMpPIAhFgxDg0bm0r5Z8BizfAGOEsM0l5WRmDmpUo_3E-rL3_zBvY6rNdwiz41vHr1Uc_N8OQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید باور نکنید ولی؛
امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال
۱ میلیون دلار
پاداش طلب کرده بود و فدراسیون پرداخت کرده
۱میلیون دلار هم بازیکنا و سایر اعضا دریافت کردن
اول یک میلیون دلار (۱۷۰ میلیارد تومن) رو گرفت بعد نشست رو نیمکت.
نتیجه: حذف در مرحله گروهی در آسان ترین گروه.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16173" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر دفاع اسرائیل:آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده رخ دهد و ارتش اسرائیل آماده عملیات و هدف قرار دادن اهداف در ایران در صورت شلیک موشک‌های بالستیک در پاسخ به نقض‌ها در لبنان هستند،اسرائیل در حالت هشدار قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/16172" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">موافقت عمان با اخذ هزینه خدمات دریایی
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/16171" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=CCvXEztePbwNJ0jJ4G_tMnESeHlxVchw6YXvzw04bHfMhByO4eYI0XqpxZQ5fWUkcQ3XQJl8pbm9iGpxcShtFH4j_xU5eJLcWVUnexnwL_j6jTwkeW7GLnXdZxa5PjxsmVaWe47S-fPc9CJbBeZDUuxMujWRBTZu47G6JVhRnykyCG7ZNGR-UkBRCPyajJFDjqKe72yB05I3SB2-R3lPmp1ydD17pmUysDgJPc2j9XYwwGrUSqPoEHbqo7DK5dDTI2rjE4fc6KqtuTSriEep6limOHs7Li_Hyk96kVwZdFTvQK-ZWbuIjhUx89ViCRAIoXfrmUeXOLUXmg8oxRhfxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=CCvXEztePbwNJ0jJ4G_tMnESeHlxVchw6YXvzw04bHfMhByO4eYI0XqpxZQ5fWUkcQ3XQJl8pbm9iGpxcShtFH4j_xU5eJLcWVUnexnwL_j6jTwkeW7GLnXdZxa5PjxsmVaWe47S-fPc9CJbBeZDUuxMujWRBTZu47G6JVhRnykyCG7ZNGR-UkBRCPyajJFDjqKe72yB05I3SB2-R3lPmp1ydD17pmUysDgJPc2j9XYwwGrUSqPoEHbqo7DK5dDTI2rjE4fc6KqtuTSriEep6limOHs7Li_Hyk96kVwZdFTvQK-ZWbuIjhUx89ViCRAIoXfrmUeXOLUXmg8oxRhfxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ مورد کمونیست:
آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
این حتی باورکردنی نیست
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16170" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6615611a73.mp4?token=eSfm4EpgpKUzOBPL2AFAjRrX-Keano9gYgKe-4IIgEFkHqrwqQLcinQV_07qQBhxRTCGPm-HWWWplYVIl8QSouEgXyMuk_hychbETSKBjsP2TdHic0vrvdVZByCXPbMmVD_iOGUxaDiAKIIdvxmTuv3XZC4D0MLNerxRhOuUixdjYZmnz30RmSIGyZ2uRt3TU1kDGa30wUos1nRC-MqIDkZBPjbOoz0VFuKS_F4yEP5nNLTn-BQca8DkpIH-khOvW9iEg0DbPPO2AUOTY4TiIvDUBkLBip-2cs9E7bYs4b00hijQm8dKTSPJAtWZKksAVzbfVuEydV1Qr-8xiyocKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6615611a73.mp4?token=eSfm4EpgpKUzOBPL2AFAjRrX-Keano9gYgKe-4IIgEFkHqrwqQLcinQV_07qQBhxRTCGPm-HWWWplYVIl8QSouEgXyMuk_hychbETSKBjsP2TdHic0vrvdVZByCXPbMmVD_iOGUxaDiAKIIdvxmTuv3XZC4D0MLNerxRhOuUixdjYZmnz30RmSIGyZ2uRt3TU1kDGa30wUos1nRC-MqIDkZBPjbOoz0VFuKS_F4yEP5nNLTn-BQca8DkpIH-khOvW9iEg0DbPPO2AUOTY4TiIvDUBkLBip-2cs9E7bYs4b00hijQm8dKTSPJAtWZKksAVzbfVuEydV1Qr-8xiyocKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما از نظر نظامی در حال پیروزی هستیم. به نظر من، تقریباً از نظر نظامی پیروز شده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16169" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=e0haU3LbB_YTknCFzqwi8glXi2oiOcdo1a81K4CVR9hUGdaU2zyQ_eGJVz-MEloi5asBBFrJuVXN72YA8HaclW8EwDQv1YzDYuuOfsP0DuHLcIjrXflaL1BQXBY9R5fYrjlfUkY0M_9hzzQIk43Nv86fxCfD_KJUqIdgDQLDbxhdV-KIoZSXDBLHBZiMr46Z0Np32L8Xyn9NwyWIy5krRFG1mn5IOC4MhtD7IHIeG10Fqrc62hkBrvrFXlV_NzPE6RVQXGtQP7MshO14n2ONoK0-2_zqw_iANk-WlerCg6huqb4BkarWRtmdk7G-9FHdk2Q0a_jC0qPPeYQ8jXNksg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=e0haU3LbB_YTknCFzqwi8glXi2oiOcdo1a81K4CVR9hUGdaU2zyQ_eGJVz-MEloi5asBBFrJuVXN72YA8HaclW8EwDQv1YzDYuuOfsP0DuHLcIjrXflaL1BQXBY9R5fYrjlfUkY0M_9hzzQIk43Nv86fxCfD_KJUqIdgDQLDbxhdV-KIoZSXDBLHBZiMr46Z0Np32L8Xyn9NwyWIy5krRFG1mn5IOC4MhtD7IHIeG10Fqrc62hkBrvrFXlV_NzPE6RVQXGtQP7MshO14n2ONoK0-2_zqw_iANk-WlerCg6huqb4BkarWRtmdk7G-9FHdk2Q0a_jC0qPPeYQ8jXNksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نشست دوحه شاید مهم باشد، شاید هم نه؛ خواهیم دید
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16168" target="_blank">📅 23:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۲ اسرائیل : وزیر دفاع اسرائیل، کاتز، دستورالعملی از ارتش اسرائیل بر آماده‌سازی «عملیات آبی و سفید» برای یک کمپین احتمالی علیه جمهوری اسلامی اعلام کرد و تأیید کرد که اسرائیل تا زمانی که «خلع سلاح سازمان‌های تروریستی» انجام نشود، مناطق امنیتی در غزه، لبنان و سوریه را ترک نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16167" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برخواستن جنگنده از مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16166" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=N4R6Ns787E-kbb_EvLcmDkWZrvaxApFt8A8GqbkV8BrZ5ophfWXMyqHkGIIXNUVwgv5lUCLoCJmnbYVKOpA9u5DPyyxqO3NXYsdlPYIMSIylpe0db48gUkBlPc12-OJ6wA4rQ7m9FgzNMXm_4WuiZhOFO8lTqOG8dnsscoBZvk2dohkOeOUThffXhbj6xwUZDwfgDhhuhLV2HrOdzRqqFuhM2494PVBBBf5aUsgIgu3x8f00cllFi8WYeRD4fmVWrdnJVKdWJSeZcWDSFPIj1AqEWUfsYQHPpyXNusWxNrK845FhUyfL1ShQ5ZeirqdoeL-lRn46I41tNIWqXUS4SapEnGUV0u0PzkAxfiElCE4NMHiE90aaZ_s3TPuGb37qHGPeATf-J3SCfwkjeHPdAZ6Oma-hgshgL0NGikdyt92StkM1RGZve7fZKpHR086hWhhL1Izmd2JzNG64MatHsxXxZxUdQ9BXSTQtYUXS0-iobk637OCr_CvIJXvYGQIu_xh805NRwWOQS-vb69L_lN9goBQ9zU4L1ORwas83gSwU8VonBuj3J3EoXirVj5OsN1s336yX2fBVuJikRVGkenEBCbHXT0DLBtrc2mjbZvTUCGy3S4NJNeFp_HKJtNH2pUyWo2BieD0sNmxGiNiCqz16GMORNJawoBSgftTv_lE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=N4R6Ns787E-kbb_EvLcmDkWZrvaxApFt8A8GqbkV8BrZ5ophfWXMyqHkGIIXNUVwgv5lUCLoCJmnbYVKOpA9u5DPyyxqO3NXYsdlPYIMSIylpe0db48gUkBlPc12-OJ6wA4rQ7m9FgzNMXm_4WuiZhOFO8lTqOG8dnsscoBZvk2dohkOeOUThffXhbj6xwUZDwfgDhhuhLV2HrOdzRqqFuhM2494PVBBBf5aUsgIgu3x8f00cllFi8WYeRD4fmVWrdnJVKdWJSeZcWDSFPIj1AqEWUfsYQHPpyXNusWxNrK845FhUyfL1ShQ5ZeirqdoeL-lRn46I41tNIWqXUS4SapEnGUV0u0PzkAxfiElCE4NMHiE90aaZ_s3TPuGb37qHGPeATf-J3SCfwkjeHPdAZ6Oma-hgshgL0NGikdyt92StkM1RGZve7fZKpHR086hWhhL1Izmd2JzNG64MatHsxXxZxUdQ9BXSTQtYUXS0-iobk637OCr_CvIJXvYGQIu_xh805NRwWOQS-vb69L_lN9goBQ9zU4L1ORwas83gSwU8VonBuj3J3EoXirVj5OsN1s336yX2fBVuJikRVGkenEBCbHXT0DLBtrc2mjbZvTUCGy3S4NJNeFp_HKJtNH2pUyWo2BieD0sNmxGiNiCqz16GMORNJawoBSgftTv_lE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیم
ا
: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16165" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/16164" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBeBJOPSf6H8ZV3_zxex5j27a1VT9F-2idGATr6WIjm33scB33qJ9W79-1ENNgdjlfuW12dHaH0AgdoJPLOkGQS96_g9XRtkunBTegpnpZTxHNxuPRcraYS7oFv0mpjL9Om8AgAu10PK3A7JOjFx4xipJoCCNhmNKJP7kGkZj4_zHijqzwCBNnkOV98NOKEKEbExX1hc0ZtGLBtrBVxfW1Loievv-J2OYVPt1HhJYxSyxjR6MmxBHzHaoQdo6Cp2yxD-Zp8jqmidLP1UjSokjqH_MRz8RPHP7I6Ih_mP3-r-0_x-96Dg0IWXsKuN_x65Y7sB_9FiTjIhAOLYHNsLzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون پیام هشدار سفر از طرف سفارت/کنسولگری چین
🚨
🚨
🚨
🚨
«وزارت امور خارجه چین و سفارت چین در ایران به هم‌وطنان چینی توصیه می‌کنند که در
حال حاضر از سفر به اصفهان ، قم ، مرکزی ، بوشهر و مناطق دیگر خودداری کنند
. لطفاً وضعیت امنیتی محلی را با دقت دنبال کنید، از مناطق با تنش و درگیری بالا دوری کنید، سطح هوشیاری را افزایش دهید و تدابیر امنیتی را تقویت کنید.
رعایت قوانین محلی، خودداری از حمل مشروبات الکلی، گوشت خوک و سایر اقلام ممنوعه در هنگام ورود، و پرهیز از عکس‌برداری در مکان‌هایی غیر از نقاط مجاز ضروری است. اگر امکان استفاده از کارت بانکی، کارت اعتباری یا چک مسافرتی ندارید، از پیش برای آن برنامه‌ریزی کنید. برای اطلاعات بیشتر، اپلیکیشن “China Consular Affairs” را دانلود کنید.
شماره اضطراری در ایران: 110
شماره امداد: 115
خط اضطراری جهانی وزارت امور خارجه چین برای حفاظت کنسولی و خدمات: +86-10-12308 / 65612308
شماره کنسولگری سفارت ایران: +98-9122176035
شماره کنسولگری سفارت ابوظبی: +98-9914240393
اداره فرهنگ و گردشگری چین در بخش گردشگری نیز توصیه می‌کند: “سه رعایت، سه نه” یعنی امنیت را آموزش بدهید، ادب را رعایت کنید، به بهداشت توجه کنید؛ سر و صدا نکنید، بی‌نظمی ایجاد نکنید، و قوانین را نقض نکنید.»
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16163" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16162" target="_blank">📅 20:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معاون وزیر امور خارجه:
ایران به تنهایی عملیات پاکسازی مین‌ها از تنگه هرمز را طبق یادداشت تفاهم بر عهده خواهد داشت.
هیچ کشوری در پاکسازی مین‌های تنگه هرمز با ما مشارکت نخواهد کرد و از نظر اصولی اجازه این کار را نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16161" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک مقام آمریکایی: ما به ایران به‌روشنی توضیح دادیم که تنها در صورت تحقق پیشرفت در پرونده هسته‌ای، دارایی‌های مسدودشده این کشور آزاد خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16160" target="_blank">📅 20:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه با فرمول پس زدن خاک از اجزای خامنه‌ای وضعیت رو نگاه کنیم ، با توجه به اتفاقاتی که داره می‌افته، این فرضیه درمیاد که یه درگیری دوباره پیش میاد تا این تشییع انجام نشه ! و اینا مثل فوتبال در دقیقه ۹۵ ضایع بشن ! و هی زجر بکشن…
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16159" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سفارت ایران در قطر : قصد مذاکره با آمریکا را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16158" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68787096d3.mp4?token=LoDvQE9F0G1Mtiv305oCueBnBqClOD86IR6F3Ij0s0r-iht-g6OuKY-PvMLxfrnGLJOAj0K_jeCa48M75cSLse48bIM9DaQu_qGQVG--JUXMN4XF-EfnWD2udnMx0_81cBFseyClhveuzuG6yZTBjzE-OQTh7nxLlMfMlTWloEDLkKy1RBqb8IUXC3UTlR_c95XvfuwwVwgRCR0bU7n5XjYc8sB9Mk9wfTrboxdKKnoXxN9QH1KcYz48yZdq_b2DuV3sQ2ufVpjEAxr8A9uXSmhL-72X2gE20Eq74UNlASh6So5RfTssTlebLR1FfIcfZ71rOZekK8KL7Pb8BFXeUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68787096d3.mp4?token=LoDvQE9F0G1Mtiv305oCueBnBqClOD86IR6F3Ij0s0r-iht-g6OuKY-PvMLxfrnGLJOAj0K_jeCa48M75cSLse48bIM9DaQu_qGQVG--JUXMN4XF-EfnWD2udnMx0_81cBFseyClhveuzuG6yZTBjzE-OQTh7nxLlMfMlTWloEDLkKy1RBqb8IUXC3UTlR_c95XvfuwwVwgRCR0bU7n5XjYc8sB9Mk9wfTrboxdKKnoXxN9QH1KcYz48yZdq_b2DuV3sQ2ufVpjEAxr8A9uXSmhL-72X2gE20Eq74UNlASh6So5RfTssTlebLR1FfIcfZ71rOZekK8KL7Pb8BFXeUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در جریان سفری مداوم به خاورمیانه، دریاسالار برد کوپر، فرمانده سنتکام، با رهبران ارشد غیرنظامی و نظامی در اسرائیل و لبنان گفتگو کرد. کوپر و کارکنانش در لبنان با رئیس جمهور جوزف عون و فرمانده نیروهای مسلح لبنان، ژنرال رودولف هیکل، دیدار کردند. این رهبران در مورد مسیر پیش رو برای اجرای یک توافق‌نامه تاریخی که روز جمعه در واشنگتن دی سی امضا شد، گفتگو کردند.
سنتکام : بیش از ۵۰ هزار نفر از نیروهای نظامی آمریکایی در حال حاضر در سراسر منطقه در حال فعالیت هستند و هوشیار و آماده باقی مانده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16157" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر جنگ اسرائیل: ما در حال آماده شدن برای نبرد جدیدی با ایران هستیم که هر لحظه ممکن است رخ دهد و ما از لبنان عقب‌نشینی نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16155" target="_blank">📅 18:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔸
قطر فعالیت‌های دریایی خود را تا اطلاع ثانوی متوقف کرد
وزارت راه و ترابری قطر با صدور اطلاعیه‌ای اعلام کرد به‌منظور حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور به‌طور موقت متوقف می‌شود.
این وزارتخانه از تمامی مالکان و استفاده‌کنندگان وسایل دریایی خواست موقتاً از حرکت در دریا خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16154" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
آمریکا و ایران پس از چند روز درگیری و تبادل آتش در نزدیکی تنگه هرمز، فعلا از تشدید تنش خودداری خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16153" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16152" target="_blank">📅 17:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیانیه دولت لبنان پس از دیدار عون با فرمانده سنتکام
ریاست جمهوری لبنان:
رئیس‌جمهور عون با فرمانده فرماندهی مرکزی ایالات متحده درباره آماده‌سازی برای آغاز اجرای توافق چارچوب با اسرائیل گفتگو کرد.
رئیس‌جمهور عون بر مصمم بودن برای اعمال حاکمیت دولت از طریق نیروهای مسلح خود تا مرزهای بین‌المللی جنوبی تأکید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16151" target="_blank">📅 17:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید
هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16150" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=a3kG8B4zfr1Gd2hHnnwWe5hE-rbGOIDADaPNyjOTgmrerVWPQEnHGO8DWNadRQH4Jxm9gSZN88aHoXrn-cxGv3A6jazlYuWnWCA7Xgzlfj2JUGfT6avS5gGQOvtkxkL2CHQJq6BEbMwur2IvSlPqQpqr_KmlfXX9udnIr3p9s4uJxjoBO149v3QekrXs3xL-e3JI0_3OkWcm8v81WQvn7F1zXBnNAY7fEY_lTcmrlcnQNnzcrv_xzABP8z_8ymJJL8RpfL4_E7OdSFHnJCclaR7oET0vfRRQ_xqKwCzZqVs6YXpo5blqRZXA3dlIOKrqE7gJ7lks94KWfUbCWc--Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=a3kG8B4zfr1Gd2hHnnwWe5hE-rbGOIDADaPNyjOTgmrerVWPQEnHGO8DWNadRQH4Jxm9gSZN88aHoXrn-cxGv3A6jazlYuWnWCA7Xgzlfj2JUGfT6avS5gGQOvtkxkL2CHQJq6BEbMwur2IvSlPqQpqr_KmlfXX9udnIr3p9s4uJxjoBO149v3QekrXs3xL-e3JI0_3OkWcm8v81WQvn7F1zXBnNAY7fEY_lTcmrlcnQNnzcrv_xzABP8z_8ymJJL8RpfL4_E7OdSFHnJCclaR7oET0vfRRQ_xqKwCzZqVs6YXpo5blqRZXA3dlIOKrqE7gJ7lks94KWfUbCWc--Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید؛ پاسخ خشونت با خشونت داده خواهد شد،
سخنگوی کاخ سفید اعلام کرد که آمریکا به هرگونه حمله، به‌ویژه حملات اخیر به کشتی‌های تجاری، پاسخ نظامی داده و این روند ادامه خواهد داشت. او تأکید کرد رئیس‌جمهور هم‌زمان به دنبال پیشبرد روند صلح است و از ایران خواست «توافق خوبی» با آمریکا امضا کند، در غیر این صورت واشنگتن آماده استفاده از قدرت نظامی خود است.
وی با اشاره به عملیات‌های «چکش نیمه‌شب» و «خشم حماسی» گفت در هر سناریویی آمریکا برنده خواهد بود: در صورت پیشرفت صلح، توافق‌ها ادامه یافته و کاهش قیمت انرژی تداوم می‌یابد؛ اما اگر ایران نقش «مخرب» داشته باشد، به گفته او با انزوای بیشتر در منطقه مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16149" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16148" target="_blank">📅 15:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS7cHw0nZ9mBLwV8Pzk_ssSPBnl3PTzlMU1bjCCjLFzhS6Ey-djKkD_oBlb9tpZaBjwmG9M-GFc8HpnI8y5BOExRKW2VhBqxcH4UW3agZ9rUfz6RU6cWwK2ahNAOtUipVY1rWbR-cx7X4HPd_Agyt42XDxDL1xsv0I2T8SInIFyC6a3dX4YL4xndZTJhwOVssFoiQ1gjnHJVR_9hADu0y_sOT3Rzifgro507h_NGuy8nEfxM9QrGqM_IFkTjYqpBuuxdwmeWb5UUqRDSDPVNN_AmT1RQET_7cFWgsyTa8LoxX2H70K9btLJwu5Cu5wsoFNK1svInyGfjvIzGiekEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : نفت خام ۶۹ دلار، و در حال کاهش است. این کمتر از مقداری است که پیش از آغاز غیراتمی‌سازی ایران بود
قیمت بنزین به سرعت پایین می‌آید! هرگونه تخلف در سطح خرده‌فروشی را گزارش دهید!!
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16147" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaazaPMiGSaoMUk9D2z5D4ELFdiryp4RPYU_407a7is2PGsa48z-4BMfVcrCfr-F5cge4FRzG7tqyomoJMxYH44ubTdsfDb6OPPL7gzitnCT23hdC9RLu0QdODdZTtBTtrfdaHFTAZeJ0ysOvMSBidLamvCtRaF4JMpvqBl46hDmoakFyDr-FOlRK4uo-jsn_J0i005M7arT8EvQI8bc119aNsqTM_h8iDsMHV5xszaxGoEC0GfXIqSAevoRPNeKHuX1yvtLlqVrOM4vR7nkZ-UU7tzqL-SDHVtKS9YcX2K6J64elPAcddAhNjD8W_FOFzNL0CityrlG17NbhtF64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران درخواست ملاقات کرده است. این ملاقات فردا در دوحه برگزار می‌شود! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16146" target="_blank">📅 15:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16144">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8MIiEAvUIORHT_ljKsm4rN8Zm6-7wbWRlCJRviPaOV0vvAqLon-L-K7fVn0dvmyXjkd2ikS2prJiI-CL2cNDBPPYfE_mZCANf_ZKFm3WiZcLMPe1MLEMGkKGn7xazmdfiiNTbcciJg_NqiONLdjqFqLA2jEz-NW_oIArO_lKT0kOD3UzSLqLletjUTu6v3B_zepKsGtMZVft9sii3gzu_fJwnFrjMfdCdJeThyGKHWStk4TLqJyj4YAHgGRqcTebyk7vJg5fvOjQ2Cuso7swaL944W2B6YgpyO8sqX9qLFsyef3lb74GxU_ee94h4KEIrFf-RqDA1tE2BbOgM3e0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGqu4MVDVRcokKVcsOOiO137iwjbxDXrj4n6FcAn4L2WFfdxJs0JcB36yalTKTCnbLqcetReb2FbWgP-vDZSOgHoVpVPWnqmcMuBcb9YzAhpdGLS2JTLWo_T7GEMNMNl-E1qdpaesOFz5W76WOUHam7dbx3F_bIwHhs3gfp6tWsDv314lSlzIGr3e9qvM9HAB8Pd14QVPXaBmbrwl3_FZGKfT9mb8wyCfpIgTHCJlzmDiBkPu31j6WsyqveoNrTSSvH1xdGozjFi2D-FuLr01Bf-cY9ak0BYQQqviAZQh3BDSBcZ9dMKTSvie9MSaoMLig1Lg1LX-kZxBJ-HgLzqPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نفتکش شرق لیما، المحبوبه (شماره IMO 9340415) با پرچم عربستان سعودی است که از چین حرکت می‌کند با سرپیچی از دستورات سپاه پاسداران عبور فقط از جنوب جزیره لارک از کریدوری تحت حمایت آمریکا و در میان اسکورت سنگین هوایی نیروی هوایی ایالات متحده، از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16144" target="_blank">📅 14:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز: ایران شرکت در مذاکرات فنی را لغو کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16143" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfYBoW9iuXTD83rlbjq0MsKngeI4o29lwp1xZNB7N62pA64taNcoNIiiGe__hq7tfeo0kICMxx_w5hz4LPn7xA1f7UCWSGaNX3JSARJlPgLB7LMuusVfJ13AVjitgPGi5vn3BOUlXDg0Sp8ueYSCKHP77Jd3R6kMGbUL-387PJjxbR4js3Be-Iv0PEHTHp1riiDkJr2IfUUbINYBm3KDnd_8zmPIVM95PHmJEk6QciVNurvZWyRqmsnZ_9tfr9FbocwTXXThZa9tzZFe09LYFQGzMLiab43GSfVUGz9Ltdy5pdpB6CKVwsAfFLCbilKcx0s7IZ5V4xg09fdSlTdeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل اسرائیل، ایال زمیر در‌جلسه به مناسبت ۱۰۰۰ روزه شده مبارزه : الان جنگ به یه مرحله حساس رسیده
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16142" target="_blank">📅 14:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16141">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCWVAsEyF1ekUbzLMGk1nbYicnJbraOcu_aaRhJgMHDs-oqtemoH0tuC43hat1tUvaSFp3IYUCbmQlStrI2SNvzHUtAKCcKcHLEMvb49VurUb9N9qmxtc6wKgrwrZZMxmEIdfkj4xRP1QyNXY0lApMmrP6bGO5k8siOgQ6MjS4PKlnilrGPdkxyrNOGAUij3uYmfsY75AosUDE_EiVxVmRTvN3wRqKs5ZunBMykv8-ukljnZi91AvIUHka62bK6mVHZdWCctScckx83hWZz2Gu0UFFiOUq3O2KIPV9-ams0eDqfz7fKLEnDxBk2_AC_xHi0kNAPQVWaTgS72hIYFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بالاترین آمار نظرسنجی‌ها تا کنون. حتی بالاتر از روز انتخابات، ۵ نوامبر. این علیرغم این واقعیت است که ایران سلاح هسته‌ای نخواهد داشت!
@withyashar
یاشار : نردبون ایران
😂</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16141" target="_blank">📅 14:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16140">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال 12 اسرائیل: جی دی ونس و افرادش کسانی بودند که طرح مخفی موساد برای تغییر حکومت در ایران با کمک کردها را به اردوغان، لو دادن
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16140" target="_blank">📅 13:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16139">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۶ اسرائیل :
«این توافق تنها زمانی محقق می‌شود که مرغ دندان داشته باشد»
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16139" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16138">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جزییات مراسم تشییع خامنه ای درتهران
استاندار تهران: مراسم وداع از ساعت ۶ صبح روز شنبه ۱۳ تیر در مصلای تهران آغاز می‌شود و تا روز بعد ادامه خواهد داشت
پیش‌بینی شده است نماز در ساعات ابتدایی روز دوم اقامه شود و پس از آن، مراسم وداع تا ساعت ۱۴ روز یکشنبه ۱۴ تیر ماه ادامه پیدا می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/16138" target="_blank">📅 12:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16137">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارتش اسرائیل و شاباک: یک تروریست دیگر که در ربودن شهروندان در ۷ اکتبر نقش داشت، از بین رفت
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16137" target="_blank">📅 12:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الان صدای انفجار‌ در شیراز (از قبل اعلام شده بود) مهمات عمل نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16136" target="_blank">📅 11:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF_zHPmHz7-smIt1WZrCe3F_dgwHqtfe7SbhqRqpscbfIg2TnGgstfSkT5tnmU6n_uv2xgzd-iavM6_NraU3FQ3ZpqB9l6o-vqZRXpyC7zERjBsFMWfrfgtZgs64F0GlqrJIh-IDhPlHgJqYuebLtr7vkDuYEvOhpbYha07UnVnngMA6ENCFL2WcZGexSAUVBQWnQv9u1qFdlKGOwNMnlVB-ph05dLteeQSUfOm607IYmx5uWID6drQaPnzn6Qmy99MlpH6AT9Yd727uv_KVFdfESyhYe6V7lKJnwUumtEoWdbCe2QaEvOsto-ORvgY97AXv2MEjo3BY39GsjBF5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود اهواز بعد از شنیده شدن صدای انفجار
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16135" target="_blank">📅 11:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدای انفجار اهواز
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16134" target="_blank">📅 11:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور:
۶ میلیارد دلار از منابع مسدود شده ایران در قطر آزاد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16133" target="_blank">📅 11:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئیس‌جمهور روسیه، پوتین، دیروز برای اولین بار اعتراف کرد که روسیه به دلیل حملات اوکراین در خاک خود با کمبود و مشکلات سوخت مواجه است، اما ادعا کرد که نیروهایش به جنگ ادامه خواهند داد و حتی به تصرفات بیشتر در خاک اوکراین اشاره کرد. «این حملات به تأسیسات زیرساختی ما مشکلاتی ایجاد می‌کند، این واضح است»، او در مصاحبه با رسانه‌های محلی گفت و ادعا کرد که «کمبود بحرانی نیست»
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16132" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر کشاورزی آمریکا: محصولات کشاورزی آماده ارسال به ایران هستند
مجری: محصولاتی که قرار است به ایران بروند، احتمالاً قبلاً کاشته شده‌اند؟"
بروک رولینز: "دقیقاً درست است و آماده ارسال (به ایران) هستند.
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16131" target="_blank">📅 10:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE-yf1jWvjMOs6rFkmzTN3SMPbKDjhal4QRdZnSZM4xM_YX0jog688kfBzvxV0Ginl7q6unD8oUqBzPsJzB1tbwqfM9nNXtchNpbm1jR9Y6nAW3P5sIbxHUlrl63nkVfw1A3gIpsPEFDOTd31kDTDw_9x6fxf4DjQazNI_PJq4ZW3bOOdsoyzID96hijD3svqgEJhO2LhQf3lCfiUcEYWeZVGWcUsCWN7G6h57j0sPRC_pTcSZnNT2o5-GEHyCV19pBufeAoSlew0HEDsPXEO3yNM2VanVenJgXg3mH0V4DpW9fvLCXWhSDN9hmlO69r_KEfGHovdr-E6WQnPwOpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر کاظم
دست کج
به عمان برای برگزاری نخستین نشست کمیته مشترک هرمز
این کمیته قرار است به‌صورت منظم برای هماهنگی‌های منطقه‌ای در حوزه امنیت و مدیریت تنگه فعالیت کند؛ اقدامی که می‌تواند نشانه‌ای از تقویت همکاری‌های تهران–مسقط در یکی از حساس‌ترین گذرگاه‌های انرژی جهان باشد.
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16130" target="_blank">📅 09:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است. هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16129" target="_blank">📅 09:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جاسم البدیوی، دبیرکل شورای همکاری خلیج فارس:
در مورد بسته‌ی ۳۰۰ میلیارد دلاری، من چیزی ندیده‌ام. نه به من و نه به دیگران در کشورهای شورای همکاری مطلبی گفته نشده. ما چیزی در این مورد نمی‌دانیم
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16128" target="_blank">📅 09:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فیلمی از حمله‌های سنگین آمریکا به مناطق جنوب
@withyashar
احتمال زیاد رادار سیریک</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16127" target="_blank">📅 09:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124ea90741.mp4?token=s77GLzi24Bns3IPclQMjsgfx2w-p4SI09E3Y9mxumF2wsew2GoYIWyHKHdP5Jw2kkmn4kOk0eaT-Ygl8ApGK4DaPz6EihEgosR8UeMvuwDeVnvoptteGN-WTgJhiBX2-Py5ycbO0xmS6q8lAyt3Jm2la76yVTDLisGPh0fMx0XgvvTgkVzGg_jo5r12RGnI-M_MfMvIL7SBGqxqNciDpIlecOVXvix_w3hDQ_Xf6TJ7Gg7uJ8TQuTJW3buQUy21GrnT84UeLq0JlxWkuX6MHWhvFhbdWRhS1KwTUJJXSlebwc2PC5xGesjDcngbYcoKHsCtlyeeaRrpGSIorFt6GwB0y-bJdGgBtZGI2bq6lWTefnpUTCkAF1kzwHlfODcgX0q96DXbF3DSiAHw0JUOyUQe3p0qtVYZhF8s5rSz2A4VHX3BLmOIGXRZoEpToo3n9JUom5Jy0MdbOC-svn3PdJzoL6msFbSyJdTwtMqzj6AEDn2k-VFiaZ6ezAqOZq2JbRSDxXt5azML3XTATeezXyXjPeTgPqbLvnIwGYXW6jZPjt4PGAo4qNPeHk-CSK1v0zfX4kjVEwH4keVQkAuAa20prX2NryAkcjlM1MaVt_StwwC1Pl0yOj6AZUH9MoN2kX1WObQZ9J70Fk7RSZ1fPwbcqegvDKDKItwNyAfxQsgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124ea90741.mp4?token=s77GLzi24Bns3IPclQMjsgfx2w-p4SI09E3Y9mxumF2wsew2GoYIWyHKHdP5Jw2kkmn4kOk0eaT-Ygl8ApGK4DaPz6EihEgosR8UeMvuwDeVnvoptteGN-WTgJhiBX2-Py5ycbO0xmS6q8lAyt3Jm2la76yVTDLisGPh0fMx0XgvvTgkVzGg_jo5r12RGnI-M_MfMvIL7SBGqxqNciDpIlecOVXvix_w3hDQ_Xf6TJ7Gg7uJ8TQuTJW3buQUy21GrnT84UeLq0JlxWkuX6MHWhvFhbdWRhS1KwTUJJXSlebwc2PC5xGesjDcngbYcoKHsCtlyeeaRrpGSIorFt6GwB0y-bJdGgBtZGI2bq6lWTefnpUTCkAF1kzwHlfODcgX0q96DXbF3DSiAHw0JUOyUQe3p0qtVYZhF8s5rSz2A4VHX3BLmOIGXRZoEpToo3n9JUom5Jy0MdbOC-svn3PdJzoL6msFbSyJdTwtMqzj6AEDn2k-VFiaZ6ezAqOZq2JbRSDxXt5azML3XTATeezXyXjPeTgPqbLvnIwGYXW6jZPjt4PGAo4qNPeHk-CSK1v0zfX4kjVEwH4keVQkAuAa20prX2NryAkcjlM1MaVt_StwwC1Pl0yOj6AZUH9MoN2kX1WObQZ9J70Fk7RSZ1fPwbcqegvDKDKItwNyAfxQsgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلیل آخرینم باش…
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16126" target="_blank">📅 02:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سناتور جان کندی : ایران الان مثل یک پیرمرد خیلی پیر است که توانایی گرفتن سرماخوردگی را ندارد. ما آنها را به شدت تضعیف کرده‌ایم. نباید تسلیم شویم
برای من عدم توافق قابل قبول است؛ توافق بد قابل قبول نیست.
در پایان یک دوره زمانی معقول، ۶۰ روز یا هر چه که باشد، فکر می‌کنم باید دوباره وارد شویم و دوباره مثل گربه‌زن با آنها برخورد کنیم
باید آنها را بخوریم و استخوان‌ها را روی زمین تف کنیم
@withyashar
آخرش حرف منو میزنه منظورش اینه گربه گیرشون کنیم‌
😂
😂
😂</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16125" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16124" target="_blank">📅 01:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16123" target="_blank">📅 01:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است.
هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16122" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=PrvjVTCcT8vntxEt00XO7oiblkKQ167J7w9Sa7QlmkSQgNq__PpYc__5EcRA-ZCAEV7sIbUtkaWOqlB5wKY2eA2wojwKbfmz10cE__qihbqZU1WcRz-XkZ8_RTsiYHgc0kr7lQ6yPT9ZbjUaCeSo6QOhnkey_rUbbh9YVtYbnOuzTWIdROqmhfVrr_KXxBezNfz1Z36iQZc0gMUAlHslhWKd07T_BYrjFRyBsbsggJcrAxr1xJo8_xxwS8m8ZX3rjZ3XYG0upYv_k99Jl6c4L2ei7MihLWhldcK8RbmtPiVoUkDp6YB69oCu0I6o0SYJE4u_5XwE4ikJFfMJAf5FAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=PrvjVTCcT8vntxEt00XO7oiblkKQ167J7w9Sa7QlmkSQgNq__PpYc__5EcRA-ZCAEV7sIbUtkaWOqlB5wKY2eA2wojwKbfmz10cE__qihbqZU1WcRz-XkZ8_RTsiYHgc0kr7lQ6yPT9ZbjUaCeSo6QOhnkey_rUbbh9YVtYbnOuzTWIdROqmhfVrr_KXxBezNfz1Z36iQZc0gMUAlHslhWKd07T_BYrjFRyBsbsggJcrAxr1xJo8_xxwS8m8ZX3rjZ3XYG0upYv_k99Jl6c4L2ei7MihLWhldcK8RbmtPiVoUkDp6YB69oCu0I6o0SYJE4u_5XwE4ikJFfMJAf5FAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل فیلمی از انفجار تونل در منطقه مجدل، جنوب لبنان، منتشر کرد. ارتش اسرائیل اعلام کرد که این نیروها تونلی را که در واقع یک مجتمع زیرزمینی ساخته شده با استفاده از دانش و فناوری رژیم ایران بود، منهدم کردند. در داخل تونل صدها سلاح و چهار سکوی پرتاب به سمت خاک اسرائیل وجود داشت.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16121" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.       @withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16120" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار شود. تشدید تنش‌ها آنها را به مکان دیگری منتقل کرد و دوباره بر تنگه هرمز متمرکز شد.  به گفته یک مقام آمریکایی و یک منبع آگاه، انتظار می‌رود…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16119" target="_blank">📅 00:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری اردن: سپاه به دنبال ترور یکی از فرماندهان سنتکام بود که موفق نشد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16118" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">من مشکل جدی فیزیکی‌ برام پیش اومده کمک خواستم ! همین ! کلت زیر گلو کسی نزاشتم که ! جم کنید مسخره بازی رو</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/16117" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع @withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16115" target="_blank">📅 00:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16114">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار اسرائیلی: ایران تونل‌های عظیمی در جنوب لبنان ساخته است.
مقادیر مواد منفجره‌ای که ارتش اسرائیل به این منطقه پمپاژ می‌کند، بیشتر از هر چیزی است که در تمام جبهه‌های جنگ وجود داشته است
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16114" target="_blank">📅 23:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16113">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16113" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📩
درخواست همکاری
اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:
نام یا لقب
نوع فعالیت / حوزه کاری:
سابقه کاری:
آدرس لینکدین:
(خیلی خوبه باشه)
آدرس اینستاگرام:
(اختیاری)
آیدی تلگرام:*
(الزامی)
توضیحات:
لطفاً تخصص‌ها، مهارت‌ها، سوابق و توانایی‌های خود را به‌صورت مختصر معرفی کنید.
لطفاً اطلاعات را فقط برای دایرکت همین چنل ارسال کنید
ادمین (خبری، بازار های مالی،گیم،موزیک، ورزشی)
برنامه نویس
و کسی که بتونه ویکیپدیا بیاره بالا
ویدیو ساز فقط با هوش مصنوعی
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16112" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله…</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16111" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
