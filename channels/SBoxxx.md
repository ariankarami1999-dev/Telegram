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
<img src="https://cdn4.telesco.pe/file/K67_04omHfMzs0BKCtyh2ovMRvouwJRdcb03isYY8eISwCUh3NmOcgkJ-JzV0xE_4I4_zDWSxImkhnL2qZm5tbES85MDOvTXUQN_tfcYGiFey0Md33ePNm3kxdZoIRmIJOHk0aOPxA7pKXKgxe183BQPuiVc9TMhJ24ckWkW6U5mciSz-r4CQ002o4ghJ5NhfadHsbTQoUn5cf0HTTf9ME6A0iduRCtnTNMFzRq_4_TQ1S-6FtxwF3GYIktp4XOepv516dMA_F9-rqV7sC1At4JUNttavkF78bpNarhPXbHQWJ5tLp4S4oOs9Nr57pVvkaNoMtCITiXABZVB_GJyzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.87K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 22:24:34</div>
<hr>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 221 · <a href="https://t.me/SBoxxx/16462" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/SBoxxx/16461" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/SBoxxx/16460" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ونس به جای ترامپ!   ای کاش ترامپ صفر تا صدِ پروندهٔ مربوط به مذاکره با ایران را به جی.دی ونس معاون خود می‌سپرد و خودش بخصوص از اظهارنظر در این زمینه خودداری می‌کرد! ونس حداقل گویا و آرام و قابل فهم سخن می‌گوید، اما ترامپ با زبان تحریک‌آمیز و شلخته‌اش فقط شرایط…</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/SBoxxx/16459" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/SBoxxx/16458" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
ترامپ می‌گوید جدول زمانی برای ایران ۲-۳ روز است، شاید تا اوایل هفته آینده.</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/SBoxxx/16457" target="_blank">📅 21:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SBoxxx/16456" target="_blank">📅 21:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران:
من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.
رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه است. ما توافقی نخواهیم داشت که به ایرانی‌ها اجازه دهد سلاح هسته‌ای داشته باشند.
پس، همانطور که رئیس‌جمهور همین الان به من گفت، ما آماده و مسلح هستیم. ما نمی‌خواهیم به آن مسیر برویم، اما رئیس‌جمهور آماده و قادر است اگر لازم باشد به آن مسیر برود.</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SBoxxx/16455" target="_blank">📅 21:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/16454" target="_blank">📅 20:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔘
اقدام نمادین دولت تاجیکستان در انتقال خاک مزار «قهرمانان تاجیک»
⬅️
با پیگیری
دولت تاجیکستان
بخشی خاک از مزار «قهرمانان تاجیک» که عموما چهره های نخبه و بنیانگذاران تاجیکستان مدرن در دوره شوروی بودند در اقدامی نمادین به این کشور منتقل شد. از جمله این افراد شیرین شاه شاه تیمور، نصرت‌الله مخصوم و نثار محمد از بنیانگذاران تاجیکستان بودند.
🔹
صبح روز ۱۹ مه، امامعلی رحمان، رئیس جمهور تاجیکستان، با ادای احترام به یاد و خاطره آنها، جعبه‌های حاوی خاک مزار این چهره‌های برجسته تاریخ معاصر تاجیکستان را دریافت کرد.
🔹
نماز میت این چهره‌ها در مسجد جامع مرکزی دوشنبه به نام امام اعظم برگزار شد که در آن رستم امامعلی، شهردار دوشنبه، شرکت کرد. پس از آن، خاک نمادین در گورستان لوچوب به خاک سپرده شد.
🔹
شیرین شاه تیمور، نصرت‌الله مخسوم و نثار محمد در سال ۱۹۳۷ در جریان سرکوب‌های استالینیستی به اتهامات سیاسی در مسکو اعدام شدند. آنها در گورهای دسته جمعی در نزدیکی مسکو دفن شدند. پس از مرگ استالین، در دهه‌های ۱۹۵۰ و ۱۹۶۰ پرونده‌های این چهره‌ها بررسی و از آنها اعاده حیثیت کامل شد.
آمو | مطالعات تخصصی آسیای مرکزی
@C5_Amu</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/16453" target="_blank">📅 20:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/16452" target="_blank">📅 20:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت :  برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SBoxxx/16451" target="_blank">📅 20:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQIqtRHSOB4PInkulq77dbMzD4uRjWVY4HM4GE2D8tAvyUcS0vfNXMRhIM_D-0PK4mgCd7hfZZXM8rrUGN5YSMjchVl4P-SHpdblClYJiowJXVPFuF4HLSU5LK23juDstHqeWl4uw6HIOMK6YzgE9REMGiM5v29RpybYJGxB7FgX6UthBIMxjydOdBFd-duzybMHX1KjcGc12jk6uZhopyrC5XnLd_7VLCLUh_Io406SyXAHwtCKDl5T_L2OAQjPh7Eta0yge5VK7Myur4tSj48MO_-U_SQ1jXKo6LWT8nSjxcpDdPcu-Z1M7k4I-bWOeesZOIe-kn51os2xc-djug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت
:
برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/16450" target="_blank">📅 19:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1oEhlLp1lnsYVTWdpUzhFXrjOwNmelTSmbRYZDjtTCh3qgoRX5uTgS7QgdIvj-v4_7ZO0XP3Fg543c-UjrJp6RioaJ4ThjVLto9EGlDTmVDQQ6HsNAQ62mu-B0a3k0xtzRxsN5fGRY0mhB52vWanY3EEl5-IN-VPew2rcW5nAL0dBipwZXv2jSPxdJfLAJ7OWN_3SyCo3ByM_mLxSH9lxNnolwKIHbIhRUlfkkzNI_S_Z4BSeHGdzlBQHhxrlUVV4nvAOhFbfjZ78nKZGfnvWi0WBxhdFKIzAioyjAhNNm3izheyr53rNO0OkmL-FbSwGMLkQ2OZU8XgQjq6GbCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه اسراییل بزرگ روی بازوی برخی نیروهای نظامی این کشور  با این تیمی که ترامپ چیده بعید نیست به این سمت حرکت کنند. بیخود نیست وزیر دفاع ترکیه هم نگران شده است.  برخی اطرافیان ترامپ رسما باور ایدئولوژیک به اسراییل بزرگ دارند.</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/16449" target="_blank">📅 15:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16448" target="_blank">📅 15:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/16447" target="_blank">📅 15:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پدرسگ های کافر هر 5 ماه یک بار دچار خطای محاسباتی می شوند حرامزاده ها</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/16446" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فوری | فرمانده نیروی زمینی ارتش ایران: دشمنان نباید در محاسبات خود در مورد توانایی‌های نیروهای ما اشتباه کنند.</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/16445" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
معاون امنیتی خوزستان
:
امروز  براثر تست پدافند و برخورد پرتابه های آن به یک منزل مسکونی ، متاسفانه ۴ نفر از شهروندان عزیزمان مجروح شدند</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16444" target="_blank">📅 15:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هاکان فیدان:   اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16443" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هاکان فیدان:
اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16441" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرگزاری تسنیم:   فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16440" target="_blank">📅 14:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">در بازگشایی باشکوه بورص، این نمادها کماکان بسته خواهندماند:  #مبین • #نوری • #پارس • #آریا • #جم • #جم‌پیلن • #شپدیس • #زاگرس • #بفجر • #مارون • #شکبیر • #شگویا • #اروند • #بوعلی • #شفن • #شغدیر • #شجم • #شفارا • #شیراز • #شاوان • #فخوز • #فاهواز • #فولاد…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16439" target="_blank">📅 14:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG3rpjBkEibS5pgIMdQhOACXvJCm-nYr0aTYmlXZ-DXO-5Jwlt1wHjMwd9axrBMhR80PakQ5c8U8FcamdP71VRlk8RzUWiooJ2AIG_N4pxFbKvymQ60gvCMCD6OiOwDyaPzjp5x_mxFqKCybPiUBcjFQgwa3SX0pUHcxd4nK8MfEhw-bEPomR-OxoDUS_5R03xnosT4TSNdJFEtAF7AZOotJ_w1n0V2A_w4A9GFmLn4bZssRy6NNpUpzxCnj29K3d5NqomFcl4QvAmVPPR7dzGo7UOsUHNWp-wIXRMaxNrulo399k-gSTYE3cwTGTae8zATQnaZTyFQid-uFzMrBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای دارای بیشترین نرخ زادورود!
هند زیبا در صدر!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16438" target="_blank">📅 10:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چرا میخند؟!</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16437" target="_blank">📅 10:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=TIo7Pna6LJ49TBIIG92Q6eNVbYRv2K_bcvJ-K7OlFNK9eTlqjybDEAX0m9Bze3WzM2DiBf2Vt9A9bvl8FFKcNJfjYUiOgCUJjNcZtUFQHNMyo-8ZqVMDwWn8sksjg3LtJgN3pDOSspZwcxbAZxcC_wX9h4dEbLXn7oxzFdlqgQ3vqGoews_c8vUrLO_1m94KbQa6VK3GQ_w1U9WqtmapiE9dw4Ud2YZbl0FmkLglOYND7wIak7j8ZXmx69UfQBwGNJoFRUKAJV-Sbz21XyrGlavj0_gBQR5879CA6RQbKXytCVpjujfE9wywbovaTQdI427f8ZimTvFcWi1U5MaN61YPtHRMJcUvHbeOlE21R2rX_fDIzt_msrSSYWsNVgWY2IMbJGo246FvZcYug017Mg3idornTSv7aLuGUVDpSdVtouj3SXvG_CJofZOyr7afQvgELI3XCY2xwrsj4iY6r3u1-_j5yCdz2mkOaa2gv4Qkp9IUquK-7eW6ZOotJ0se0TNyEYVowv_AYVooRYjrPe0CFhLjoykgCKhncsdeUOvLBK3e7K9WtB7bPgVY8zKekMxMSLDuwER0Rr2RYuMGPVzeq79ib6MxBwEEp8UyBOz4NlEMmvbP1V3H0OcLfrXxt2eKidGKmRjD1So4WYPi6mSsw7UK3RkvfxzcdbiZ2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=TIo7Pna6LJ49TBIIG92Q6eNVbYRv2K_bcvJ-K7OlFNK9eTlqjybDEAX0m9Bze3WzM2DiBf2Vt9A9bvl8FFKcNJfjYUiOgCUJjNcZtUFQHNMyo-8ZqVMDwWn8sksjg3LtJgN3pDOSspZwcxbAZxcC_wX9h4dEbLXn7oxzFdlqgQ3vqGoews_c8vUrLO_1m94KbQa6VK3GQ_w1U9WqtmapiE9dw4Ud2YZbl0FmkLglOYND7wIak7j8ZXmx69UfQBwGNJoFRUKAJV-Sbz21XyrGlavj0_gBQR5879CA6RQbKXytCVpjujfE9wywbovaTQdI427f8ZimTvFcWi1U5MaN61YPtHRMJcUvHbeOlE21R2rX_fDIzt_msrSSYWsNVgWY2IMbJGo246FvZcYug017Mg3idornTSv7aLuGUVDpSdVtouj3SXvG_CJofZOyr7afQvgELI3XCY2xwrsj4iY6r3u1-_j5yCdz2mkOaa2gv4Qkp9IUquK-7eW6ZOotJ0se0TNyEYVowv_AYVooRYjrPe0CFhLjoykgCKhncsdeUOvLBK3e7K9WtB7bPgVY8zKekMxMSLDuwER0Rr2RYuMGPVzeq79ib6MxBwEEp8UyBOz4NlEMmvbP1V3H0OcLfrXxt2eKidGKmRjD1So4WYPi6mSsw7UK3RkvfxzcdbiZ2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داماد شهید رئیسی: شهید رئیسی اثبات کارآمدی نظام ولایی را رسالت خود می‌دانست
صادق توسلی، داماد شهید رئیسی:
🔹
جوهر اصلی شخصیت شهید آیت‌الله رئیسی را می‌توان در دو واژه «تعبد» و «ولایت‌مداری» خلاصه کرد.
🔹
آنچه در سلوک ایشان به وضوح لمس می‌شد، احساس رسالت عمیق برای اثبات کارآمدی و موفقیت «الگوی نظام ولایی» در هر جایگاه و مسئولیتی بود.
🔹
تمام اهتمام و مجاهدت ایشان بر این اصل استوار بود که مردم برکاتِ ملموس این نسخه یگانه و نجات‌بخش را در زندگی خود احساس کنند.
🔹
رابطه عمیق، عاطفی و سرشار از محبت میان ایشان و امام شهید، صرفاً یک دلبستگی فردی یا عاطفه شخصی نبود؛ بلکه ریشه در یک پیوند تشکیلاتی و ولایی داشت.
🔹
این ارتباط ساختاری با ولی‌فقیه به عنوان عمود خیمه نظام، با این هدف تعریف شده بود که خروجی کارآمدیِ حاکمیت دینی را در عرصه اجرایی به ثمر بنشاند و حقانیت این الگو را در عمل پایدار سازد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16436" target="_blank">📅 10:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:   رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است   پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16435" target="_blank">📅 09:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:
رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است
پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16434" target="_blank">📅 09:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5dFOnxGbf4ufRK0-P0upgjY4VH6jTt-1rVcRE9cYLIbet2RBLEn3g9k44X8AqUzlEGn4bEHrw6B6LQE_BCYJrriCffbcWrFk54dnh4foucKNNttRcD-3RcECvdbkyGFwq_rAVxW5Up6hoIuxQuBpzWoROd-gRuCKdRK-GFojHHgd_c9XFX3ykIzzFB2D-PEUGZQrzfQLbDl_5ZM6nftnKl6dkuLMwzoqYwTDI9G_C7QNAWyWj2eSAETSRrooKD8eMNXzzq6H6OGJjY5ZbZj_tMC42OZS-LLpCXR9nc6RCLx1UgN8ytZMrE7V4eNZXu0UGe7tOY6ml7aP9BMo47Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ نیابتی آمریکا با بلوک چین در شاخ آفریقا هم نمود پیدا کرده و دیشب نتانیاهو اعلام کرد که اسراییل، استقلال سومالیلند را از سومالی به رسمیت میشناسد.  جالب است بدانید که سومالیلند از ۱۹۹۱ دارای دولت و ساختارهای حکومتی خودش است و اتفاقا از دید قوام نهادهای مدنی…</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16433" target="_blank">📅 05:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار:
«آیا گزارش‌هایی را شنیده‌اید که می‌گوید ایران دیگر درباره تعهدات هسته‌ای صحبت نمی‌کند؟»
ترامپ:
«چه سوال احمقانه‌ای. من چیزی نمی‌شنوم، ما در حال حاضر در حال مذاکره هستیم، تو چه آدم احمقی هستی. من در این مورد با تو صحبت نخواهم کرد.»</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16432" target="_blank">📅 05:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7YVyeQjXZyaaUUbrATDEqd6CsUbHpr5BIz8dI5bPsWIRjd4ewHadiYAnnRnxXuZI8zAIEomNNvbbmLMBumOD2f0sysNIvjSdCw7sIJZxiHwaqLGsLftSytvG8ChrThzRFqF8QVm0I8P9kPSVG51uycLz336pq0NOyQ8oXhF6Zd3R9B1ockeWCguWyK-AYmkXJgCroX5lgWwB0p21ByK6qvTm41za939yvGRwKmPoELJcKOq97Ee79WYFgKPG1WfIIzgsiY_JHCPceLJgCq3z9E-G0CjLSQlx3d-Y8TU6ecAQcOwfDliZHz-MSF1GeGrOstgA4DvOdVV0YzSrbYzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!  سبحان الله !</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16431" target="_blank">📅 00:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تقریباً ۹۰٪ از کشورها اکنون شاهد روند افزایش بازده‌ها هستند و نرخ جهانی ۱۰ ساله به بالاترین حد پس از سال ۲۰۰۸ رسیده است.</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16430" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16429" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkLhziZIoLTvFRzl6zG-8W2mmqDpm4hn5LfRihTvbGQaKXGTd0qCRm0s0X7S6TnG3IY5kDXvC_-VtsPtdl-smWjN_pzaALhZYFHnFqejgI9yZZbp-iZu6KGpODtEuqw20s9x0-jPu3W50MLh9q87or3Nx0EckSbkKUzSSHjdCkeNHNlpkuyDXftb_v4OSIOTY2PMZoa67vRxKEEd-UJaeF3QSBLHcc8P2HXk0W_BptGfeP00tXD2PvyUpRrrRF3apLHatfH8LOLVFVACfWFnt3WNnwmZ2yu_U-s5isAc4kxRRU6tOG-BAYKxGFbE8BfY2cKhSyCA0yZVuBm3aUCx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16428" target="_blank">📅 23:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرگزاری تسنیم:
فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16427" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16426" target="_blank">📅 22:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16425" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic Republic of Iran, which was scheduled for tomorrow, in that serious negotiations are now taking place, and that, in their opinion, as Great Leaders and Allies, a Deal will be made, which will be very acceptable to the United States of America, as well as all Countries in the Middle East, and beyond. This Deal will include, importantly, NO NUCLEAR WEAPONS FOR IRAN! Based on my respect for the above mentioned Leaders, I have instructed Secretary of War, Pete Hegseth, The Chairman of The Joint Chiefs of Staff, General Daniel Caine, and The United States Military, that we will NOT be doing the scheduled attack of Iran tomorrow, but have further instructed them to be prepared to go forward with a full, large scale assault of Iran, on a moment’s notice, in the event that an acceptable Deal is not reached. Thank you for your attention to this matter! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16424" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voMepy8bMec7MeM_K7aLWhdNTcbcYSROR8fSF78SndOyKFTprnv6uS48ToBOJX4krL7-Z9NEV7dik3BgEi8aVeYlbj9_DFEpydRnts2nga6bYztthjNZH6YdIkLBi0y28Esw3Hoh8zps8n0j9rTXmfa23HlbXQmyPD0FyHjColrNqeUv-c0JILojISwG-ExNTQjg-28PhEAImYdwKJrG6aCNK1AKx9XPTJ3IKk1r86GAXNkQSx0xY4xrSEIH8Hbjzy0apKxjdnAsVxYDh_LY1UkidacwiR-YOs__zDKe9dGWS0_9XlRr9YL3fJpGsoZLcLCdTzC41UpuTkem1HfIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16423" target="_blank">📅 21:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:
«رژیم ایران می‌داند بزودی چه اتفاق وحشتناکی برایش می‌افتد»</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16422" target="_blank">📅 21:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16421">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♨️
پس از رد پیشنهاد جمهوری اسلامی ایران توسط کاخ سفید ، وزیر پاکستان ، خاک کشور را ترک کرد</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16421" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16420">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuVmbuegyC2bd-ORSHc8peURpm9Zf__krtwehqrrDbZ2kZJWfZRZzZz4aCrRg8swyhGepOs56XYpH9FbvWBxCTDRCnFCgpcDjb90H6j4ZhrsQrNMX9M_I5alT4b_W_MY4_IRpnDm-I-gN5DgaIkU9sjf2V7oHI3-eWfDOlMPzOzY2iu5BTQi65LJKtJCe6UrhZf7ka8XCMFJw_pgLVReNE9iltIoNS43v1mf7uAvC5AewUNWg6lUW6-jWLj705jDja68pOUxsN44MXR-1CjOyA8b81eQwEmw6G7Kr2g1Ab8DvMJD3odoxPzemuUUGpSNrrWjRsUUW_2Y3WWL3SjYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16420" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قلعه‌نویی، سرمربی تیم ملی:   40 درصد عقب‌ماندگی بدنی و فنی داشتیم که 25 درصد آن را جبران کردیم، شرایط سخت است ولی نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16419" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16418" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16417" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16416" target="_blank">📅 14:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمالاً زمان بازگشایی بازار بورص هفته آینده اعلام شود</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16415" target="_blank">📅 13:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16414" target="_blank">📅 13:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16413" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxB2xRcK5dh5PBysojY1HEEeAkdTjZ6llH_mUJfudPLiGlV3dIUDQjdoELJoJp6uPyu4OTquZVl6Op8klWA2qrLaxOr-isjscqd-clTbi30OR1ypG4isGYHiD00I8YwQV5pJEMn6qkB5MKMTmp_2FgEfNtbXsbrBiQAMdWAVIXCzd5t6tuhWxndXMZDH-xXClufA-P4o3NguHkLf-ZfJJaE6i4RyVNO4WKrVPHKWObOyKLu0HrwTkGG8qYqFE_Gd4lbIvnSuY49qJtvnLk4SpXPbAPLl3-_JlM7mwINl1aocXiXF4Kv1IvRt_ZmCNYb7rHcG-GcqwCWy2QA-w_L9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16412" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16411" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-H-ySwvF8fKYebeFsdvtZxsGOHAHb6Oet1rzw4Kgk3JVSZgnxGH0qbFlvkpu17hOxV1r3bAgLPJ8_vKbwUandlzz03nw_AQhVOGiToO5aUwl4nRTKY7LC3Mpug6zDPF8yq2pJOXjeluNGvpgidh-8WPqBThijmxetGa9CzjefXWqYrFUMKOMVihML9WRLRJWYQiibAcTF92XDejvoIbizhSboZt4-hl4RxNZealpSzY45EYtbA-H1cmNK1TDf_1O6HvT52YLJhsqVGsL-FPflh2VjNHZ4Y2JqNNQj_vB5cMYimS0552-NaQeHsLOtvQHclcGkG5HyMNY40fMXSjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL -- H4
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16410" target="_blank">📅 09:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg0iQlm4zoG2PDg10MXIBSaSlfjblCyM0Fg995l_mz5IMw9KYmiCMQvsFD-PPHYFOkdo0pFZb9JohtdMS213dBwmkEv-Wj6vNpT8-zbzGua7Q920Lahw4-D6aWqqTLEa9h_-kniT8wsi9ECgeNqTc77fhoVuiKMSe1FNzdKFHbd3WZmK5IoD4pE8SW1CxtenhgVdaKDUUZ9w3oPSX76o7RMBt3kAXSfNK602zjRsbrdo5jidwPHUtDc-X_vniLRgq_0ZU5nDCCEe9pq5hEK_qNa0tl1OQA4wY0NJSz7w1RmLjnOTNaYd1ETwKfnBwY-piBcyDHiu-kfPt3azfyKEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین که ترامپ مردد است بین کوین هست یا کوین وارش کدام را انتخاب کند نشان می‌دهد یا دنبال دستکاری بازارها است یا اساسا نمیداند این دو در دو سوی طیف سیاست پولی هستند؛ یکی بشدت هوادار تسهیل پولی (هست) و دیگر طرفدار متعصب محافظه کاری و انضباط مالی (وارش)</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16409" target="_blank">📅 09:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16408" target="_blank">📅 09:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تأثیر جنگ ایران بر بحران انرژی اروپا
جنگ ۲۰۲۶ ایران با بستن تنگه هرمز و حمله به زیرساخت‌های انرژی، شوک شدیدی به بازار جهانی انرژی وارد کرد. اروپا، که به شدت به واردات گاز طبیعی مایع (LNG) و نفت از طریق این تنگه وابسته است، اکنون با چالشی بزرگ روبرو است. بر اساس گزارش‌های اخیر،
آلمان و ایتالیا
آسیب‌پذیرترین کشورها هستند. بانک مرکزی اروپا هشدار داده که این اقتصادهای وابسته به انرژی ممکن است تا پایان ۲۰۲۶ وارد رکود شوند. افزایش شدید قیمت‌ها، تورم را در بریتانیا به بیش از ۵ درصد رسانده و تولید صنعتی در بخش‌های شیمیایی و فولاد را با چالش‌های جدی مواجه کرده است.
کشورهای بالکان مانند
یونان، قبرس و ترکیه
نیز به دلیل میزبانی از پایگاه‌های حیاتی ناتو و آمریکا، نه تنها با بحران انرژی، بلکه با تهدیدات امنیتی روبرو هستند. حملات پهپادی به اکروتیری و دکلیا در مارس ۲۰۲۶، منطقه مدیترانه شرقی را به منطقه‌ای ناپایدار تبدیل کرده و صنعت گردشگری این کشورها را نیز تحت تأثیر قرار داده است.
در مقابل،
فرانسه
به دلیل داشتن سیستم انرژی کم‌کربن و مازاد برق، کمترین آسیب‌پذیری را دارد. این کشور با تکیه بر انرژی هسته‌ای و منابع داخلی، توانسته است از شوک‌های خارجی در امان بماند و حتی بر افزایش تقاضا متمرکز شود.
به طور خلاصه، کشورهایی مانند آلمان، ایتالیا، بریتانیا، یونان، قبرس و ترکیه بیشترین آسیب را متحمل می‌شوند، در حالی که فرانسه به دلیل استراتژی انرژی مستقل خود، در موقعیت بهتری قرار دارد. این بحران بار دیگر اهمیت تنوع‌بخشی به منابع انرژی و کاهش وابستگی به واردات را برای اروپا برجسته می‌کند.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16407" target="_blank">📅 09:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">تلویزیون دولتی آموزش زنده‌ای درباره نحوه استفاده از
مسلسل پی‌کا
پخش کرد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16406" target="_blank">📅 07:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMoqCu6_TtAO4--FPhdNVYHth6PEV_FoBSgKgkCgY8CmfJ5qvd6yDEuUj4x1GUjxeOzw3PctdaKLst-Nl31Vd5YyNCrIUt1lYCHy26RJZlyjgLeSrUyUiAU2neEAiMHUbABq0CBMz6xVi2Ch5NpKraXwERVgfv_NpKQanO5ash5Zw1KHPEZlCt79568rRzroJvZtpeD5fcU_eHWb0cVDTtNN4XOUJ9L6_gThPQbjjjQRmYoMQyka1KUM7vAgze3Vh8hSRD0hEUqH6HXSR5MiGscUDd7BZTb3hvy3P1Um-fWD6-zWPDiSQPBJmVIHICqemyPO-a0a_pG2a1tUs6BZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  افت 45 درصدی نسبت طلا به نفت پس از ارائه تحلیل.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16405" target="_blank">📅 06:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdGSuKhqHZdSr-E6g2jkGfvT04e4BbXS1UuxG567nk5izVXxp19Mz4MIja-gR9ePX6GOsuWr7ReHrcx-G9RgszjNNKb_en_YPJ1AaZpZG-Otze9NZT2JwHzsu9NwLpUnKvnB1caAR1S-Z_Hzwq-gDu4E4XIZkxAWlzFYMRqqytnT638-wOUvK_cd1hZsqeeueoFJB4XTQyXN8p8DeOqWkbLkPImZkS7Njdp5xuW6ym5Z-Eb5g4lNKNEIbx4-TZ8-P0su73rtFkkkRbXcAHAk-GQdE8eINfbS938ZKIR-42k0g_CNpS8nzyeQzJ_I-0ii7L0C5__6tm8dB_Gw5f-3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشخص است کله زرد خسیس رفته نسخه رایگان هوش مصنوعی کذایی را که با آن کار می کند خریده و گرنه این همه اسم شهرهای ما را اشتباه نمی نوشت.  رشت = Majd? تبریز = Toha?</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16404" target="_blank">📅 06:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16403" target="_blank">📅 06:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش عراق:   اجازه نمی‌دهیم عراق سکوی پرتابی برای تعرض به سایر کشورها باشد</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16402" target="_blank">📅 05:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16401" target="_blank">📅 05:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBlQ7OqDQewGFCLppShKQ_8A_VwqJnYwyGFQP2aFetEKIk2rZVcXTIm40HQN-aznHmdy51wARdYIdrmcAv7TUnukXyzwKm2zqhPhluzo78khj6Mss7_6WgST6GTvoJLcPSjUVm6q9QWGQNeBc1Gdmb7ZT9QROHkUnCIf4CZI7pqXoaGMUZQq-WoFY4ZyeBSmC3OD7qgpokt-KB5_by5M5sl5StcgHQvP8cWp8eiWmYLL2eUn2dD1PwoD2SdlByWku_vfo8AqafHw6VAMZxf4Y4QSdG99-apfGVm469F3dODs6BPNjilJXgjKzInqzh87JjySq5VEmKsbH_bAtfg6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16400" target="_blank">📅 05:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2JJssb-hLKbd_Q8mZLCecvnL8WMEOdjzkhrr94mZhLNfMAw5vxLfKkGPib7D6wp0RbO-FDX1y3T6f9KgOGC01NgqBdtD7hXwn3Vo0Je43LNE5tWCba39PZQZWWF_J2sZlYsqNWcNLJUdRSbNuZ12kR44D2O1G0enIrr0ICCjp9xAel7KhZ1UxNnbr6EgUty-Saszmbzg9Y0gCIX0kgouIUjA4uwgrWQrSfSW2ed6gg8STlglyksLI_PVG4dZ2nD0CVlno9MOW2Sp6nmfatvI6pCXIN3MHZ5zo5bLthwHjfof0HvLR23b9piMvTQtMM1iAa9_z4537MQ9AKcZFsUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16399" target="_blank">📅 05:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b124790efc.mp4?token=r6hYhDU-2GKfYgCU6LVO5TDZnGfVOBF2Yf1A4eoxj776km_CTxRv9UBDpRoCIsZDbX-D8URCPRRbL7X63-8OyjVPl-HnDhbjWRSym9hUMRWDbHak8MoXVsbSJVNkbGkjV-8LjB8TYqln5SBgrgOytYCB2kBU03KlKUX2euo1DAq50B2BG0isyL4LR103qb6q0ztpGt56vz79hxBhDgQWZvMkpFtfoJaUuqT_0LLkBF-TcabqNpVDqgrT7nbTKv_YHN2fXyXLdib40eToVQchIlDmp7Dze2ofLXecaKobsNnfg0YUX1M0gYC0SHAbaO7GtzajaX4MM9YLMxaCUeo3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b124790efc.mp4?token=r6hYhDU-2GKfYgCU6LVO5TDZnGfVOBF2Yf1A4eoxj776km_CTxRv9UBDpRoCIsZDbX-D8URCPRRbL7X63-8OyjVPl-HnDhbjWRSym9hUMRWDbHak8MoXVsbSJVNkbGkjV-8LjB8TYqln5SBgrgOytYCB2kBU03KlKUX2euo1DAq50B2BG0isyL4LR103qb6q0ztpGt56vz79hxBhDgQWZvMkpFtfoJaUuqT_0LLkBF-TcabqNpVDqgrT7nbTKv_YHN2fXyXLdib40eToVQchIlDmp7Dze2ofLXecaKobsNnfg0YUX1M0gYC0SHAbaO7GtzajaX4MM9YLMxaCUeo3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
در ادامه تمرینات آمادگی دفاعی شبکه افق ، پس از شلیک های موفق به پرچم امارات در روز گذشته ، امشب ، نتانیاهو و دونالد ترامپ بدون استفاده از گلوله ،  بصورت نمادین هدشات شدند</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16398" target="_blank">📅 00:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است! رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16397" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxJ6phUI422ybuMRK1csaKYgbahEa8aF9gM7ZEXpdytlcGoMgBl8KzKul1GYL6sYaz-nH7soU8rzq-4wH8aFHymFIujWu1G9rQOXGKuRXjNH3odJS1CeYcO458Tb_j52DJCas4zpcCfk_Iq_xwIB2Cj8zGjHZBryoGwK-53DQRum6YLPyCVMNk_XxJD-A8BCOxE8uwjgaydpyH4ArQ2h-IW__vUW5ZewuzjZVFlcqFwaF460InbsUiiRM3lZ0LM1Qpc2_JVauQ3uM5A7nGBzTEN4m9ZHk04Kit5Kk7f1dzVWBfKUMiVfE0DAUTRpHZxWSYW7TbjcwV5xlNbcHEQcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووال اشتاینیتز، رئیس شرکت دفاعی دولتی رافائل اسرائیل، اعلام کرد که اسرائیل با کمبود رهگیرهای موشکی مواجه نیست.
این اظهارات در حالی مطرح می‌شود که گزارش‌هایی درباره فشار بر ذخایر دفاع هوایی (به‌ویژه رهگیرهای Arrow) به دلیل درگیری با ایران وجود دارد. اسرائیل همواره این ادعاهای کمبود را رد کرده است.
رافائل تولیدکننده اصلی سیستم گنبد آهنین است و برخی اجزای Arrow را می‌سازد.
اشتاینیتز در یک کنفرانس گفت که گنبد آهنین حدود ۹۸-۹۹٪ موفقیت در رهگیری راکت‌های حماس و حزب‌الله داشته و از ۷ اکتبر ۲۰۲۳ تاکنون، این دو گروه حدود ۴۰٬۰۰۰ راکت به سمت اسرائیل شلیک کرده‌اند.
همچنین ایران از سال ۲۰۲۴ حدود ۱٬۵۰۰ موشک بالستیک شلیک کرده که به گفته او تنها چند ده تای آن رهگیری نشده‌اند.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16396" target="_blank">📅 19:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارت اطلاعات کوبا تایید کرد که رییس سازمان CIA به این کشور سفر خواهدکرد.  به نظر می رسد اینها هم بزودی پرچم سپید را بالا ببرند.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16395" target="_blank">📅 19:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔘
پافشاری ترکیه برای تغییر نام «آسیای مرکزی» به «ترکستان»در کتب درسی
یوسف تکین، وزیر آموزش ملی ترکیه، در مراسم «رمضان در قلب آموزش» در استانبول، از تغییرات در برنامه درسی مدارس به عنوان بخشی از «الگوی آموزشی قرن ترکیه» خبر داد. به نقل از رسانه‌های ترکیه، طبق این برنامه درسی به‌روز شده، اصطلاح «آسیای مرکزی» با «ترکستان» جایگزین خواهد شد.
🔹
همچنین این مقام توضیح داد که مفهوم «آسیای مرکزی» محصول اوضاع سیاسی پس از جنگ جهانی دوم است، در حالی که «ترکستان» (ترکستان) با ادبیات علمی مطابقت دارد.
🔹
این تغییرات بخشی از مدل آموزشی جدید وزارت آموزش ملی ترکیه است. جایگزینی برنامه‌ریزی‌شده اصطلاح «آسیای مرکزی» با «ترکستان» در برنامه‌های درسی تاریخ مدارس در اکتبر ۲۰۲۴ اعلام شد.
آمو | مطالعات تخصصی آسیای مرکزی</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16394" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16393" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItpVsPlxSUkLWkuO8Y-zH_q7rPrKXC38LkhfMa3xfSPVk2ObmRqqxEqrI_UUtqGJrj8ruq4k33TWBoqi0I-YTDSfeXQJjZqxULr__7LWDReDTGaQIrIgEcHQTj82_FLHv4vlDUlLzpqpocluiY_WueglFFIZoyhLOrvIE3_202YSsLDCGmjvXUBDOB29nmZAONKMn-7Vri5O6JN1cooSw8rUAaCjMu_Ke5C-Ark0LCv7qbas7fb1YEM8z1h0YNfhVwT1nkAnrDuTvH_FzLFrBuRbpPSzqu19O2v3HJp_fR7I0CNNd_PUop7LsK9K1dv_oEoNdgll_MlZpM_ZsHZQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بدون اینکه خنده اش بگیرد روز جهانی «ارتباطات» را تبریک گفت!</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16392" target="_blank">📅 15:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام: دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .   پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات،…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16391" target="_blank">📅 15:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVlrXJCfuoHOrvLunKvb3ZEJYh4mxr1TFUCarytlCj2LkO1rWDsURMCU97NIaiykjVfxMV1109J7JyV57osM6X9vk0nzlh-MB810gMnaTLb2Pyvziqd0Nch2Ofkqv4iL3IlJNq3Vm9fr79t3e1Cze0dkdkMYcpONiVoa0cVxJ_ARmPU2vRTJqAUhqwkx0bLnobRlp8ecuX5WLYCa-ekz3QYczCIuJ1vDwHeMaxiyry-Loq_5cZoYgj_1z6EZQeaaYYbpBkPKHMgzHbRxc1uY_06-0Z-We4fGzHm1gMCzZnVFBpzng1rGIabBhJ4WUO2u5PJG6muaydIL0Eiguhziyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔑
حضرتی، رئیس‌شورای اطلاع‌ رسانی دولت
:
حرف‌های پزشکیان در مورد اینترنت «وعده» نبوده، شائبه وعده بوده</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16390" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btafa1DpIcqqRWQHQj4iioO4tbiS_C0UWF10Qzk9_3tQydzle73dybZqYUvWj5FbybuFeTRXHTm-u_U6SrGDxFUSj08uuRhCFt_MJplD4i__bF3DMPeO0XL4JXZA2YstBT2LS5MHnbInhjjdGcZXOkONaTkJKqpOFgtYqxlLzJh0JMUVe-YJ67QokJa8L6Wc9hqYcgl88IHTBL098J1vj334OL_hHvM1l59y5FAAxI5beEtjoaHW1LWoYK0uuqg1GxdJKDeE1Nayx-GFVv4tsXLQ4oy6qp3ai7A-i93PVga1FrO7Z4lIU30giMfHTUdd3hqFdhvqla4DmIsx-bU8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#EURNZD
-- H4
کانال نزولی در حال شکسته شدن است و انتظار رشد مناسب داریم.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16389" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی: اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16388" target="_blank">📅 13:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🟣
خبرگزاری CNN :
کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16387" target="_blank">📅 12:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
رسول جلیلی ؛ عضو حقیقی شورای عالی فضای مجازی
:
اینستاگرام مثل F35، F22 و A10 آمریکا است، مثل آن اژدری است که به ناو دنا شلیک شد</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16385" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بحران انرژی در حال تبدیل به بحران ارزی در بازارهای نوظهور آسیا است
نگاهی به لیست بدترین عملکرد ارزها از آغاز جنگ آمریکا و اسرائیل با ایران بیندازید: الگوی جالب ولی غیرمنتظره‌ای آشکار می‌شود. تقریباً تمام آن‌ها واردکنندگان انرژی هستند. بزرگ‌ترین بازندگان شامل پوند مصر، پزو فیلیپین، وون کره جنوبی و بات تایلند می‌شوند. در میان ارزهای اندکی که صعود کرده‌اند، ریال برزیل، تنگ قزاقستان و نایرا نیجریه دیده می‌شوند — همه آن‌ها
صادرات‌کنندگان عمده نفت
هستند.
آسیا با چالشی فراتر از یک بحران انرژی روبرو است. اقتصادهای نوظهور این منطقه نه‌تنها با افزایش هزینه‌های سوخت و برق دست‌و‌پنجه نرم می‌کنند، بلکه با
فشارهای تراز پرداخت‌ها
نیز مواجه هستند که به نوبه خود بر ارزهای ملی آن‌ها تأثیر می‌گذارند. در کشورهای آسیایی که به سوخت‌های فسیلی وابستگی بالایی دارند، افزایش قیمت‌ها باعث بالا رفتن هزینه‌های تولید و کاهش قدرت خرید مردم شده است. این وضعیت، در برخی موارد، منجر به تضعیف ارزهای ملی و افزایش کسری تراز تجاری شده است.
در حال حاضر، کشورهایی که قادر به تامین انرژی خود نیستند، بیش از همه آسیب می‌بینند. برای مثال، اندونزی به دلیل بازار داخلی کوچک و وابستگی شدید به واردات انرژی، با چالش‌های مالی فزاینده‌ای روبرو است. افزایش یارانه‌ها ممکن است باعث تاخیر در تثبیت مالی شود و کسری بودجه اندونزی در سال ۲۰۲۶ می‌تواند از آستانه ۳ درصدی تولید ناخالص داخلی فراتر رود — موضوعی که نگرانی سرمایه‌گذاران خارجی را برانگیخته است.
در این میان، کشورهایی که صادرکننده نفت هستند، مانند برزیل، قزاقستان و نیجریه، از افزایش قیمت‌ها سود می‌برند و ارزهای آن‌ها تقویت می‌شود. این تضاد روشن نشان می‌دهد که
بحران انرژی اکنون به بحران ارزی تبدیل شده است
— پدیده‌ای که اقتصادهای نوظهور آسیا را در موقعیت دشواری قرار داده است.
بلومبرگ</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16384" target="_blank">📅 10:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyHnKwHk2uSPPZgjj_mBKD-ZRNLfdV3-FeQu6m3yD81JDGzofZFzAZ1spWCfmJO8wYGKpZpA7oS8iPjiLnOPq-h2GXC-l4NT-dAsYJDxIrANViwd9ehJENzFkE-rxtl19Nbh_qYt42a9uVPTAPdv3curliQiavRectHdjmnoS6ONjxwblbVt3_1HvWovLLxnp8bp88Qf6IbMtbBHNRW5bVUSWIYNekB2YCO48GMCPULBsxsLMfyGzA2lieycbPl0ikDZ4gvNFB0qjy0C1LVGX-vNNxn9xnYVMr6vS9g0ypdb9Vr_5_dLvvbutDwB1i2LggJwoPkmDEd0iVg24QTMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUicHZ4OmzMs4KEb0qALQRHyDjLIaYwNFhRl2_bf4s05Be6g5n9d1EX6WIuczCmIVYWJHz0bmJkwHXG-eTcwQKbTCUKIbgA4pnsCWJq1OvNN-RNXrfm0V38Vc77OrRJJvA50uLmrxgVsQVHut2MjXWYTc_bGXYQZ5uQZAJWAWXEWztN0mNmQatn7AlY5kPFc-YA9Y0vOeI-RhsCs04_RVWYi_Nr3bTS9zhXbonj0cK_1BrNdBz9SVeRIx8PwNiiWlniEwjoeUsT5wlqm7fjjWHqxNmCgjLHdVTpYos9XvWxL9cROPbWZW2oBlePJAK0K0_2MmeZOJKM2WMkKt9QbFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیروهای نظامی جمهوری اسلامی اواخر سال ۲۰۲۵ قراردادی برای خرید ۵۰۰ دستگاه پرتابگر موشکهای دوش پرتاب زمین به هوای  Verba (تصویر پایین) به همراه ۲۵۰۰ موشک مربوطه امضا کرده بودند که بخشی تحویل شد و بخشی در جریان حملات اسراییل به تاسیسات نیروی دریایی در انزلی از میان رفت.
همچنین سامانه مشابه میثاق ساخت داخل نیز در اختیار نیروهای مسلح ایران است.(تصویر بالا)</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16382" target="_blank">📅 09:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16381" target="_blank">📅 09:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_wZNs8O2pIvdK2bmEi9heZWeQ5GH-7MTTd_Au39LCi5a-0gt_WPTOQDT15JJ8sJrJJhVd0ufyI_tsEIP-r_SY0V-ueOVE8mQ37lkIjmBt36Tn7l0Iz5DtdpkFLajiL86Trx23BxGm050WTekiyGH_CwfAPi6epp8F6JiS3Dzk5C8HaJp3zwXHU6iAyLcppbq9QHpQDs5wGk8_j2KKdF7GAI79-5UqAt_op6i-X-V0x4KbJdB01026-RZUx1FyGGXNSb_vwTcY2ZojBYysrvcPdgAcsxcAlgTb30kpSKamHwsDDTmP0XxozAn6EFXike6lqjdVqVungwjLisDiOe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج ۵ نبرد ایران و آمریکا همراه با هلی برن گسترده با حمایت هوایی سنگین خواهدبود و تسلیح یگانهای ویژه نظامی در ایران به تفنگ‌های دورزن و موشکهای پدافندی دوش پرتاب و نیز موج آموزش عمومی کار با اسلحه در صداوسیما و مساجد و … در راستای مقابله با این تهاجم است.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16380" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvLa0G3ctmikjaoZLwtmBhBP_s0YW1EkSxS48ZTU6Inx1MNxdUEwnAqk4y65fW3l85cpWb1ojtOhTYHO9SLahR0Ow0b0Ld-XJ7N8HYmxwe0gOkZdKKrww1n5w8I3XzjKp2nwQBzVy6n5BjEtsHjEhh_YdPobHa-23g9UtArQwKtHXJ16-AarD6x-HErudoTDb1b3gEkHZCgQXl4UMb4gA7L-oUJabjoF9774JP8aGSfD_Okdpj-YREC1Z2dXtVZEGwPcyYtvemVF3WzBgFI8-SL_ftNwln8rcdn2Q5S1n5i_mlXvPh81YbyaXAuHYkdTiNSsNpEGdy5vJeh94i9INA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16379" target="_blank">📅 08:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617dc4e3f8.mp4?token=n7Im-yVldC8U6xwajevw41iDYUhcsPmsdO3uXpASFHoCWIh9Cu1QCCtLohSfPJeKPwZf1ZLS2yBeNJsl-RjxXtROBMtbPNulfGZ3MdRq3QMQ3niEn53dJuuTUmnV4y6hwRCbvoLVVGPcrhASdt-puZYMpgXbU2-dhdMX_jEtP1OQpZFfuIbdTLgVtus1dd10AcyvrfrCF5L9FNAfGfe4T6rlGtSIBUGB_MSwjV3gcNym_nI2mVZSNMrL9nBjIlo0k7-rkkztRZTsSxy06eGv-0FYX4iXngA8Gq9uQjEcC5D5DIRVjBTHExm-sIU8n2MOkzDFVFtgv2tuIVxHbDnttr1MlxT_Vg26A7Q4YUZOe1Htn8YKcvPEReSexAl3TTLftLbykhqFDFVzHzN10YlfCMKpujZY3sN5Sv90nOh47bhA5i6rAi6Kh6-XVnrc9UIPW0rmX0hVnIT_64RCxZW618RRiO3LqmfeEx7-JY101md__mqmjhtBb-cmbvutJn-Q5mRnSCDkOJzwYPVxZd5Mu5iaeE0pcbGtkBKEYiJTCOI1VbMKJx2YRZUklcK6_lqvhqM0i8QAszux7EeN56OT7kPlziM2VtkQ3bnnv56MMJ8JsXfLRlgMDddQsZtMfZDdUrYl94IhrpUIscVLCqSePTgKNqM_L2JIQq4M_j6HV3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617dc4e3f8.mp4?token=n7Im-yVldC8U6xwajevw41iDYUhcsPmsdO3uXpASFHoCWIh9Cu1QCCtLohSfPJeKPwZf1ZLS2yBeNJsl-RjxXtROBMtbPNulfGZ3MdRq3QMQ3niEn53dJuuTUmnV4y6hwRCbvoLVVGPcrhASdt-puZYMpgXbU2-dhdMX_jEtP1OQpZFfuIbdTLgVtus1dd10AcyvrfrCF5L9FNAfGfe4T6rlGtSIBUGB_MSwjV3gcNym_nI2mVZSNMrL9nBjIlo0k7-rkkztRZTsSxy06eGv-0FYX4iXngA8Gq9uQjEcC5D5DIRVjBTHExm-sIU8n2MOkzDFVFtgv2tuIVxHbDnttr1MlxT_Vg26A7Q4YUZOe1Htn8YKcvPEReSexAl3TTLftLbykhqFDFVzHzN10YlfCMKpujZY3sN5Sv90nOh47bhA5i6rAi6Kh6-XVnrc9UIPW0rmX0hVnIT_64RCxZW618RRiO3LqmfeEx7-JY101md__mqmjhtBb-cmbvutJn-Q5mRnSCDkOJzwYPVxZd5Mu5iaeE0pcbGtkBKEYiJTCOI1VbMKJx2YRZUklcK6_lqvhqM0i8QAszux7EeN56OT7kPlziM2VtkQ3bnnv56MMJ8JsXfLRlgMDddQsZtMfZDdUrYl94IhrpUIscVLCqSePTgKNqM_L2JIQq4M_j6HV3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این هندی ها همه چیزشان کمدی درام است؛  مقامات هندی در حال بررسی طرحی برای رهاسازی مارهای سمی و تمساح‌ها در نواحی رودخانه‌ای مرز با بنگلادش به منظور جلوگیری از نفوذ و فعالیت‌های مجرمانه هستند</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16378" target="_blank">📅 08:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">معاون وزیر خارجه روسیه دقایقی پیش از قریب‌الوقوع بودن حمله آمریکا و اسرائیل به ایران خبر داد.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16377" target="_blank">📅 02:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔹
رسانه های اسرائیلی از وقوع انفجاری عظیم در بیت شمش خبر دادند
🔴
گفته می شود ، انفجار مربوط به کارخانه بزرگ " تومر " که فعال در حوزه تولید و توسعه موتورهای موشکی و موتورهای پیشران است ، بوده است
🔹
هنوز اطلاعات دقیقی از خسارات و تلفات این حادثه منتشر نشده…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16376" target="_blank">📅 00:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
رسانه های اسرائیلی از وقوع انفجاری عظیم در بیت شمش خبر دادند
🔴
گفته می شود ، انفجار مربوط به کارخانه بزرگ " تومر " که فعال در حوزه تولید و توسعه موتورهای موشکی و موتورهای پیشران است ، بوده است
🔹
هنوز اطلاعات دقیقی از خسارات و تلفات این حادثه منتشر نشده است</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16375" target="_blank">📅 00:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzZWX2y9tE_CsUwII9b949T-JXjgXCh_3KIL-t3uUBwworc4XUjzJfF9qBsIb0LDxJ8PGXR7ZSQxHVMpj3A32sMGqnMoeYZSkPWRqM6pZIItWIqA9Nfb2dMFJp9KFMzpMjOQquEt3WYc0Ol_h8nG__A0TwxQHP6n2OWhCiY7NyK4jctK1DOpivmnA6ygeKq8iKzkRR-_Vycbqk3c3a2ljA9qEqmFCzwwkFe8D5-xqV9k0AWme9dav_NfbPnMzumUcIwkqEuagTzJr12XCE0j1kdLVRjgqpYrv0vX3V9HlJpUkgGRwO3MNjwayCMi4B1VfTdIDBB90dyoaOdOQd9ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مرغ طوفانم نیندیشم ز طوفان | موجم نه آن موجی که از دریا گریزد</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16374" target="_blank">📅 00:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16373" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16372" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhiXM4bV3CnVDIJLPjiMf6xGtG4RKEFubUEYVWz_wZym9EKZ3Oq3gSwSFP7_XQalehZY2Qb3L-9XYQ61Q5VV0Hb7iGbq2Z2qu2uC8641hrotJE_PX6pnSxdRypGKRRv-8JDqk53qbIV-RmwZkZW-TIUK1RCwYIaN2e4AuQRWRxOluVQ-C-NUORzogk5xKy5KsR3_sSSI1XEK4UlJ4hg-ocs7FnNFnv_gPxhtdBzrClLUwi4nl-3pUeH1OfUvlA_o7LBGOA8kCcfGn_Z_YeU5g-r1rQBZMCn5MxM1XbcDjWUxT_SpvSpfU7xh2Tx9OLmR6nhHqSp6gQYkvuFad1o-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کله زرد ول کن این هوش مصنوعی کذایی نیست.  چه گناهی کرده ایم که این ور با هوش مصنوعی هر شب فرعون و ناوهای آنها را غرق می کنند و آن ور هم آنها قایقهای کوچک مان را اینطوری پرپر می کنند.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16371" target="_blank">📅 23:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
تاثیرات اختلال سوپراپلیکیشن "شاد" و اخلال در بستر دیجیتال آموزش کشور</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16370" target="_blank">📅 22:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEdnV0PsA6PfYhC0Hvmz542oR374Hj9cKJSU2rp2GkK8aeM2UriF2uV1DDDOAEGxSHOTGsq62UUJHBDA0e7TKL6C7O5j2VS6HSaF9QJCJx3VgB36E0HDPhk_0yHAe0rR9j53QtXJnNu6KSg4d3yje2EPbmF4E_0j-cKmWUJhqvM55eyfpbMQIFF0Exr897nvZuobCgM9RL4yGUfqdSHbclXFDs3kM0IQy2AcNsSthr0eWWb2MDjHPwIugux0EFIru0lqArPjlAqoUku83nLLUQIdoaRbSrAaGLRy1tdLROCepoFiPVoFuwcGnBNOkDMWRiRlzmFG_hrL48Iw1FL7yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر داگلاس مک گرگور از میلیتاری نویس های برجسته X دال بر نزدیک بودن دور بعدی جنگ</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16369" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بازگشایی بازار سهام از روز سه‌شنبه
‌
معاون نظارت بر بورس‌ها و ناشران سازمان بورس و اوراق بهادار:
برنامه‌ریزی لازم برای آغاز معاملات سهام و ابزارهای مربوط به آن از روز سه‌شنبه ۲۹ اردیبهشت ۱۴۰۵ انجام شده است.
‌
بر اساس هماهنگی‌های صورت‌گرفته و پس از اخذ مجوزهای لازم، مقرر شد بازگشایی بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها از روز سه‌شنبه هفته جاری صورت پذیرد.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16368" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور:
دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16367" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام
:
دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .
پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات، حفاظت بهتری نسبت به اروپایی‌هایی دریافت می‌کنیم که ۵۰٪ مالیات می‌دهند.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16366" target="_blank">📅 21:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حالا امارات را مسخره کنید اما اساسا یکی از مشوق های اسراییل برای پیوستن کشورها به یک پیمان راهبردی با تل آویو «تصرف خاک» است.  نمونه اش پیمان با باکو که منجر به تصرف قراباغ شد و از دید اماراتی ها، وضعیت جزایر سه گانه برای آنها معادل وضعیت قراباغ برای باکویی…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16365" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16364" target="_blank">📅 19:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlbOgbkpXLpMn_AtE2Vl1KjLzSAAUPwUFEOdaqwZnWpCnNJa7VENVjM46RC3Ko_oqHIQ_-BiEnRTnaNYP8lDUIg0JkC_K7ydmrbTjfvPT1fhrA9MIR0DFKpcHZ04TxLBKOPBzIjgJoGZ3oUnHorXjeMeOb7qfxuFUgNSM1QOodJ8fsXqg1SsHYjM_RisgVfehy697w_ZGtILUmMyyXwIZutq68G6pRCzgYyR3DXw4m3u67bd6ShgT_P07HmpOx0XgIgC9QPE5Ct4XSxX5Pb54q-6rgwn5488tLiccnl8O80GzuylcZtVZtAOfzYMM2JP_9VNhEs7pqTfLji2315EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد از تعمیر سوپراپلیکیشن "بله" ، سوپراپلیکیشن "شاد" دچار اختلال شدید شده است</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16363" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16362" target="_blank">📅 17:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16361" target="_blank">📅 15:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1x2d_QooJt2iSf_k8cA1a5YRd71ZeNFTi7d7R6Yp4BF1bf8WcPzqKKu36lMkH8WwoZ0MTK9S9fzIqgFeEWFVZ4y_jsSWiru-7QldWSUw7AHRd86oK31MO-XIqxOj6M1xOnf-GxX9zeWB7LPcg_QywgPqkK8k5tik3ArgzNYvKUKESQqTXnK3APwrkxoL4R07WjdVEfm54_EJWlm1t3Fz8RNuW2btn3XhBhLY_O2m7SA8m7Le9lNJnHb49atfdbPA2u4hIoXF7hScZ06JSn-3YMPSBs_Ac0vrnVxIEor3JtYBXlcZam2veZ9ggI1JSta9ryDNZy5QUqLQz3m-NX0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحولات رفتار بانک‌های مرکزی درباره طلا
بانک‌های مرکزی در سال ۲۰۲۶ رویکردهای متفاوتی نسبت به طلا اتخاذ کرده‌اند؛ برخی مانند ترکیه فروش را افزایش داده و برخی دیگر همچنان خریدار هستند.
ادامه خرید طلا توسط کشورهایی مانند چین و لهستان نشان می‌دهد طلا همچنان جایگاه مهمی در تنوع‌بخشی ذخایر و مدیریت ریسک بانک‌های مرکزی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16360" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
