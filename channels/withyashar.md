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
<img src="https://cdn4.telesco.pe/file/PkUP8fUIlcEM7qBtK9mU5dC-xjhO6RTHt41ea1tuzIKXiqxf1_lE6YKUFoP8bLxoSmcZFg2zh2LLksgEcS3zWPDBb2HKoY9pttZR1SQ1kiR8zwI-LAtpmoESh0lqm9OTj9yPkKK6jERd8EF3p6vKJqBPlxk73mdaZGtpjVZaADsAR-15OMZ_NDRn6xS56XcvnQ0TIjb-EYFthbgHtOxK-bAeWAR3jLh_0NN9ALDHxw0XqWeSk0-74Nqsi1UvGqJqndVyDSTcwmQg4IQMkaw1qTChj92MwITIeNChgUPMeWliK6LkPi7RKDXsYcxQYHCHDRy3_BNYDOIZLmwl5aQdVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دلار ۲۶۸،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚀</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/withyashar/24827" target="_blank">📅 12:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تا آخرین لحظه حیات
از آن چیزی‌که تا به حال‌بودم تغییر نخواهم کرد! و اگر تا به اینجا با حمایت شما رسیده ایم  , مسلما به فروپاشی این رژیم هم خواهیم رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/withyashar/24826" target="_blank">📅 12:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری صداوسیما:
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد تیراندازی رخ داد.
این حادثه پس از مشاجره لفظی میان چند زن و با ورود مردی مسلح به سلاح کمری و شلیک گلوله اتفاق افتاد. مرد مسلح به سمت زنان نزدیک شده و تیراندازی کرده است. تاکنون جزئیاتی درباره
تعداد مصدومان یا تلفات احتمالی، وضعیت افراد حاضر، هویت تیرانداز و انگیزه او
منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/withyashar/24825" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTNiPI57PrSBNfbOH_X84_gQmVvaOlV0zyZOEApdvYoRnLGXb7sPe8TVPF_c3HB_K7CBS-ydKyhis_tdYnCuf_VAO6LLIsd-2ouDna8cth0T8O3CxCfIH4qCyUBG15YVLQ_jx5Ls786ogW-4NxLr2zDEcK75PQA8r2VbNwKpT3wWmdXp_6hJtm750CNyZGh-q3S9ZeAzrmbAURn75CAsYBLfSlHZu7ibQfLm7HhTEk_iS29NOvfsTYBT05Ou6wPCK8weXRspnoa90hO_DxhJWzRhOSH4TqtcKCuxDjlUMH-4p13F54DDyawpnd2A4lhfOSXu4MP4WzdvF8jhbP4ANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابودی پارک جنگلی چیتگر در سه دهه
این پارک در دهه چهل و در دوره پهلوی ساخته شده بود و ۶۰ سال قدمت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/24824" target="_blank">📅 11:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرنگار کانال ۱۲ : گزارشها حاکی از این است که کمک‌خلبان، شهروند عمان، با یک تبر سوار هواپیما شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/24823" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آکسیوس به نقل از سه مقام آمریکایی: مقام‌های ارشد دولت آمریکا در کمپ دیوید برای بررسی اقدامات بعدی درباره ایران و انصارالله تشکیل جلسه دادند. یک مقام آمریکایی گفت در این نشست «تصمیماتی گرفته شد یا دست‌کم موضوعات به‌طور جدی مورد بحث قرار گرفتند». جی‌دی ونس ریاست…</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/24822" target="_blank">📅 10:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRWjbf6LcWz3Z084e-uXGtjoSsixrmw5-L_Y0JtHwIAzEqeOGVmzlX3Nsx76jTaGQmI3J_TmnIbfFdqopWUTKnNZ-YqJa4Isg1rqw_ihroWAq7t4ApxGrhNzyIc1cDDJDi_zr-G39Q0H01xnsQDwCXH9544LX-K5O9C7UUp6RfIFnp7ryNrvR5x6Dggar_rg3AMuWS7kMPz-ndw3sjV9tzSzdMmsew9StXdqeyE9twx6se02P3bVlgvNmtFTxWGOwa1T7NXZBAFlugc-u_vgyYo7IxjIS6VrYoISwLj-544zjyjeca_e5gHQR2tj6KfIxpijKrev6ewpV5rutto8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه افغان نیروی قدس سپاه پاسداران از کشته‌شدن یکی از نیروهای تیپ فاطمیون خبر داد. او در اثر انفجار بمب کنار جاده‌ای که در زاهدان، استان سیستان و بلوچستان، در جنوب‌شرق ایران کار گذاشته شده بود به هلاکت رسید؛ این حمله احتمالاً توسط گروه‌های بلوچ انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/24821" target="_blank">📅 09:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f878b1ca.mp4?token=O-d46NsMAEIZj52b-6v3MUDYJlQmEiPkhkwLZubk4PMUscthgvhdzJih7YoJWhCdzYtOD6zffzOHrc1Hex5wRFtsbQ4bU8OxGCjz1D2AdPik7zxq0_ic2xnqB9jORdiBPls0eLALFNsnKsl7NUXHfsDpC9w4DxbWl_g2in_XRS4cBUEcMeQGLTEXKD_yig-TjQDIKuG873nsGvAPqvIrNjHo1Nd4LX4LJZOl9jX_fffXa72VYJGB1nn7-qxtIMDLxgYj946GPVAyNHY4lJxlMkLdhzBNruhjr9F89oHf2usTGPvdMBSISsCYh7-Fn_J7HCcssMIBn09Uzs48eSI1QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f878b1ca.mp4?token=O-d46NsMAEIZj52b-6v3MUDYJlQmEiPkhkwLZubk4PMUscthgvhdzJih7YoJWhCdzYtOD6zffzOHrc1Hex5wRFtsbQ4bU8OxGCjz1D2AdPik7zxq0_ic2xnqB9jORdiBPls0eLALFNsnKsl7NUXHfsDpC9w4DxbWl_g2in_XRS4cBUEcMeQGLTEXKD_yig-TjQDIKuG873nsGvAPqvIrNjHo1Nd4LX4LJZOl9jX_fffXa72VYJGB1nn7-qxtIMDLxgYj946GPVAyNHY4lJxlMkLdhzBNruhjr9F89oHf2usTGPvdMBSISsCYh7-Fn_J7HCcssMIBn09Uzs48eSI1QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «من گروهی از مردم را دیدم که اسمشان «همجنس‌گرایان برای فلسطین» است. یک روز آنها را بفرستیم تا بروند مذاکره کنند. دیگر هیچ‌وقت آنها را نخواهید دید. آنها کارهایی انجام می‌دهند که باورکردنی نیست.»
@WarRoom
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/24820" target="_blank">📅 09:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Auk-kEcfSVzxh9UXPEJlzKtNdd6F07nGAodzan-lIo_Fl6KhjEfdsIe3FjFZ7gYPmwFMsqrBcRQOFhBk_LGZ-BSw6x1Vf5oZ6XkqIpy1Dg0UxUo4fFS52Hq5PrExGbmho7QcTaxVDLPwps1KhfOcZZPEilSBZKN9CMDNmHb4De6Fi-FzOIVL-yE5-l6lCcdKhKM1i6EdxCw5mG08XA7pao4TaCuuxtKcZqRUfQdFVKU6tI9Rtkz9496DpCj1ghYqLa7q5QVD1PTw77VV6c_3a6OaSqtx9cEVhOkRWDo58kX4y4zYdKPUBAzT7AICWs-nBoW_Gex337Hsmlz0_uxYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم
سیاوش جمشیدی
که در جریان اعتراضات دی ماه ۱۴۰۴ بازداشت شده بود به اتهام استفاده از اسلحه در‌اعتراضات شهرکرد ، بامداد امروز ۱۱ مهر اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/24819" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24818">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس به نقل از سه مقام آمریکایی: مقام‌های ارشد دولت آمریکا در
کمپ دیوید
برای بررسی اقدامات بعدی درباره
ایران و انصارالله
تشکیل جلسه دادند. یک مقام آمریکایی گفت در این نشست «تصمیماتی گرفته شد یا دست‌کم موضوعات به‌طور جدی مورد بحث قرار گرفتند».
جی‌دی ونس
ریاست جلسه را بر عهده داشت و
مارکو روبیو، پیت هگست، ژنرال دن کین، جان رتکلیف و استیو ویتکاف
نیز حضور داشتند.
آخرین بار که چنین نشست مشاوره‌ای برگزار شد، ژوئن ۲۰۲۵ و پیش از آغاز جنگ ۱۲روزه اسرائیل بود.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/24818" target="_blank">📅 09:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پدافند غرب تهران بدجور زد !
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24817" target="_blank">📅 04:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شنیده شدن صدای تیراندازی یا پدافند از شهریار و اندیشه کرج
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24816" target="_blank">📅 04:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24815" target="_blank">📅 04:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241181503.mp4?token=tomB3OwZwtmlMiyWDWsd4pRC498iqjh_vXmuw5KB1VrGbFDkne7mkEq533Dk0Wi55cGVJz56m_tBIgvcUpJ49wmyhH1i21wFSZgxdFQgol-ki5KS-Prm0_pWoz4yTnqO5P0KZOkxriu9rzLmdLaZh910jyk3ntrK4RKmzShVCQAxLAs9xjp62i6cmTYlsvMPEknyw0yY5wxBb994HPiZo9IkJuxHxrwEd-3aUFORIS2M5Z7t7d0GM_Q2IsQY4V2ekdkWwAmlYuqR3V9BIIVR1vUkXYQkDQZn1apH8T-pLIjXZKIepqaZuPEkijXWa91n8w8ejDYuNb5cU2yVZf_lUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241181503.mp4?token=tomB3OwZwtmlMiyWDWsd4pRC498iqjh_vXmuw5KB1VrGbFDkne7mkEq533Dk0Wi55cGVJz56m_tBIgvcUpJ49wmyhH1i21wFSZgxdFQgol-ki5KS-Prm0_pWoz4yTnqO5P0KZOkxriu9rzLmdLaZh910jyk3ntrK4RKmzShVCQAxLAs9xjp62i6cmTYlsvMPEknyw0yY5wxBb994HPiZo9IkJuxHxrwEd-3aUFORIS2M5Z7t7d0GM_Q2IsQY4V2ekdkWwAmlYuqR3V9BIIVR1vUkXYQkDQZn1apH8T-pLIjXZKIepqaZuPEkijXWa91n8w8ejDYuNb5cU2yVZf_lUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «یکی از بدبختی‌هایی که داریم ، کسی نیست که با باهاش مذاکره کنیم. هیچ‌کس نمی‌خواهد رئیس‌جمهور باشه ، جدی‌ میگم : «الان با چه کسی در ایران صحبت کنم؟» تق‌تق! کسی خانه نیست.»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24814" target="_blank">📅 03:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8addbc83.mp4?token=HvnynOH95GF5No8ukTapoDOqWc0mfD2ZxmwaVmdTTv3HdRat4HDWp7o4EgHhNHLoxqhJzdKbCZi3orlpAMNYmP5PtzD7wm2hQOvzyQqonmmE66K329T5vkc89TAhhjd8sGH6-fUwa4uBp7luw6jxkQkdf3nBs0WIpEaKdSCqjrFrFYSiU70ak6t1kWgKI77h8uTGt7kzXgLkeGCt5aXkoIsb7xk1v1lmcSFoPLaRvZGPD7-bm4hK8BWRmgZXGdUkD8PIV7PN90t3XY4URP9c4Y37QmTvjghhRfxFuy3KSUDQ_CJ5HcwpY9aWmi8SNqpGU_YRFxU_KqgcFgF8ZlpTaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8addbc83.mp4?token=HvnynOH95GF5No8ukTapoDOqWc0mfD2ZxmwaVmdTTv3HdRat4HDWp7o4EgHhNHLoxqhJzdKbCZi3orlpAMNYmP5PtzD7wm2hQOvzyQqonmmE66K329T5vkc89TAhhjd8sGH6-fUwa4uBp7luw6jxkQkdf3nBs0WIpEaKdSCqjrFrFYSiU70ak6t1kWgKI77h8uTGt7kzXgLkeGCt5aXkoIsb7xk1v1lmcSFoPLaRvZGPD7-bm4hK8BWRmgZXGdUkD8PIV7PN90t3XY4URP9c4Y37QmTvjghhRfxFuy3KSUDQ_CJ5HcwpY9aWmi8SNqpGU_YRFxU_KqgcFgF8ZlpTaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «ایران برای ریاست‌جمهوری شورا برگزار کرد، اما هیچ‌کس در آن شرکت نکرد. همه می‌گفتند: «ما نمی خواهیم»
@WarRoom
یاشار : فکر میکنم منظورش به همون خبر استعفای پزشکیانه و بعد کسی حاضر نشده کاندید بشه. برای همین با استعفاش موافقت نشد.</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24813" target="_blank">📅 03:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f8e97b36.mp4?token=vC-h8ZnTuBS_bEs-umNf7rtjd9AlHQgtSKQDXo-TWjpitF30164akiALswKjyhooKZefeFfqaPWDKSmcA6-2zGf3iZCG7zQx93n8yJQ8D9PQIroP-2HDbduyrlEFada7opynNZLCvtrjHknfccC5HHKsmh2qtT2CuH3lxLAqHgffod9ZHrriJKhMql90zkGqqyx6Wp5XqgvzhxrKcVV8UCYb15vkfHB9K8pcdH-eYVZbnVTtXWRUG7DiNfnvEyZlK8dW4q2vmfFLpEdboo0wJkdcoDqGZABXgz0ZoWpi3SpB3llR9JiLsGnHlguhf0CJpnOoXSinGInSBVAM1IpPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f8e97b36.mp4?token=vC-h8ZnTuBS_bEs-umNf7rtjd9AlHQgtSKQDXo-TWjpitF30164akiALswKjyhooKZefeFfqaPWDKSmcA6-2zGf3iZCG7zQx93n8yJQ8D9PQIroP-2HDbduyrlEFada7opynNZLCvtrjHknfccC5HHKsmh2qtT2CuH3lxLAqHgffod9ZHrriJKhMql90zkGqqyx6Wp5XqgvzhxrKcVV8UCYb15vkfHB9K8pcdH-eYVZbnVTtXWRUG7DiNfnvEyZlK8dW4q2vmfFLpEdboo0wJkdcoDqGZABXgz0ZoWpi3SpB3llR9JiLsGnHlguhf0CJpnOoXSinGInSBVAM1IpPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «اگر دروغ بگویم، به من پینوکیو می‌گویند. من دروغ نمی‌گویم.»
@WarRoom
یاشار : خیلی خوبه این بشر
😂</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24812" target="_blank">📅 03:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f2bfed07.mp4?token=hbvg30e1KUXYMDCv6KA8j_IUcK9GYZNy9h273MSYTO7UfJ-sza78xjktGVD0cPNnMgLcwXBFT_k0kpMGWlywvEJcBKgcQGAKDgV0SRzsMZoy64l6ozB3fWhMMQSXjlWm1Db1jcdexMdN1_ExB0fRAy_CKpB7U0U8xB1VLQjKqbxnQDC1kWfI4vw_fhb14HPGtvi3STje00uJKRGnxkgzhv8uBDeCJUaM0mb7yxTKI34Rh31XzcFFo_bptyoAi3HkDA5rwgHJV2qJGPUYaqI49L3C9_laz8jk2-mrWLs0P3BqbTLfiQbQKj6BU-T9e_W2rEVoMWh3U1Mp0lOLZYIVAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f2bfed07.mp4?token=hbvg30e1KUXYMDCv6KA8j_IUcK9GYZNy9h273MSYTO7UfJ-sza78xjktGVD0cPNnMgLcwXBFT_k0kpMGWlywvEJcBKgcQGAKDgV0SRzsMZoy64l6ozB3fWhMMQSXjlWm1Db1jcdexMdN1_ExB0fRAy_CKpB7U0U8xB1VLQjKqbxnQDC1kWfI4vw_fhb14HPGtvi3STje00uJKRGnxkgzhv8uBDeCJUaM0mb7yxTKI34Rh31XzcFFo_bptyoAi3HkDA5rwgHJV2qJGPUYaqI49L3C9_laz8jk2-mrWLs0P3BqbTLfiQbQKj6BU-T9e_W2rEVoMWh3U1Mp0lOLZYIVAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «احمق! همه‌شان فکر می‌کنند کلمه Dumb حرف B ندارد.» (ترامپ با بازی زبانی به تلفظ واژه Dumb اشاره می‌کند؛ حرف B در نوشتار وجود دارد، اما در تلفظ خوانده نمی‌شود.)
@WarRoom
یاشار: همون‌جور که می‌بینی ترامپ هم اونور دنیا با این احمق‌ها درگیره. واقعاً احمق زیاده.</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24811" target="_blank">📅 03:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0v-KLPWXXMWJ-g0r8NnGpN5VpcCsHqGSWL932yyWxb6vKc0PIhoetst3OzME2mI3NyZR1_XIndRB3OhgyyLWxf4J6wxM_1k6hygtEXdQoIsbJufzxHODJbg6ZMIKcUysn_Go1wsEqlgB7MCP-FSQ90RzbXMO9vF-q-V2NS9g7PPH7ASWf1tzYPqlEr-NWRHDD7AhxpNJBaQoXX8I3HfDSKpIIOrg1lBIWEaw35blwO9hEwOCduFSG_BT7i5f5bcmPn6V9TPcBr8rsok0DPGzjWjIYg6BEn0-PIR3aFKqEDGPdxMdmBkeivWK0YWFtyZoicBBGuwBB3271duSKySOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش حامل نفت خام در حدود ۴ مایل دریایی شرق عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت.
تمام خدمه در سلامت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24810" target="_blank">📅 03:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24809" target="_blank">📅 03:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24808" target="_blank">📅 03:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الجزیره: حمله هوایی هدفمند اسرائیل به یک آپارتمان مسکونی در غرب شهر غزه.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24807" target="_blank">📅 02:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24806" target="_blank">📅 02:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24805" target="_blank">📅 01:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24804" target="_blank">📅 01:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24803" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24802" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کره شمالی موشک بالستیک پرتاب کرد. پدافند ژاپن در حال رصد تحرکات است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24801" target="_blank">📅 01:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSfpY8wjomeSTZkEghvrSP3OMx3ZPYtCzmP8UHnmyscCPySn0oaBaQM5bivNhIQ_F8e0v4lsjPThKo_h5SPLNrYG-5qRWz3FuBXLiNNQs9bvrvIf2_agBkmJ98pt27jhd63j_ux-BuMjwmRmkA1NSG4DRRWDisxU0IBtNi2Aoh-R2l6ZQJhKoRKWI1lqrPfetBTanQP-Pvsxh_fPffiq2VNhRfTk58YASvA7EeRTj-YbjbwdWIQtzb5e65b799WqFf-gmWUSOidgPw7qW4Ls_oAUNl8u6kUrEnAbuFksj8qUXwbHeG0OvmX1sX1k1gr-MdMfyHUhpm9Ma1DYpnKqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع العربیه: کمک‌خلبان عمانی مرتبط با حادثه پرواز فلای‌دبی «همام الهمامی» نام دارد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24800" target="_blank">📅 01:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع العربیه
: کمک‌خلبان عمانی مرتبط با حادثه پرواز فلای‌دبی «همام الهمامی» نام دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24799" target="_blank">📅 01:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24798">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نظر مارک بر اینه تو این ۲۴ ساعت آینده میزنه انگار</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24798" target="_blank">📅 01:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دلار داره موشکی‌میره بالا
🚀</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24797" target="_blank">📅 01:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چنتا کانفیگ فروش دایرکت دادن برای تبلیغات
😂
😂
میگین به جایی ‌وصلن ؟</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24796" target="_blank">📅 01:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24795">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چنتا کانفیگ فروش دایرکت دادن برای تبلیغات
😂
😂
میگین به جایی ‌وصلن ؟</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24795" target="_blank">📅 00:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وال‌استریت ژورنال:
کمک‌خلبان عمانی پرواز FZ1073 فلای‌دبی که متهم است به خلبان هواپیما چاقو زده و باعث سقوط شدید هواپیما شده،
قبلاً در عمان از پرواز کردن منع شده بود
؛ دلیل این تصمیم، نگرانی‌ها درباره گرایش او به دیدگاه‌های افراطی عنوان شده است. با وجود این ممنوعیت، او بعداً توسط فلای‌دبی استخدام شد و در مسیر حساس
امارات به اسرائیل
پرواز می‌کرد. هنوز مشخص نیست عمان این نگرانی‌ها را با کشورهای دیگر یا شرکت‌های هواپیمایی در میان گذاشته بود یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24794" target="_blank">📅 00:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟ ترامپ: خب، اگر به شما بگویم، یک خبر بزرگ خواهید داشت، درست است؟ اما خودتان خواهید دید؛ همه‌چیز خیلی خوب پیش می‌رود. ایران وضعیت خوبی ندارد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24793" target="_blank">📅 23:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ee0bbd03.mp4?token=cNdFT_nJde8VuHMP6W5aAK3edHil6Yg-5YEsJKAkdH9FVB6jW1UQ-_1UeKUL2ebmi8YKpx8Zt2LM68VQ12IjuFdMKGii0Q1MiHrGTSAh-NfxVAv4qEa1dVAF5JWQG_0MMJJCyglPyxV_2BWkZ3nu8mLl18udcM4_2J_o-H-5xalUNR6BxezISJbsbrFnG-sKQIikR4BD5bfiYa4mVbA7lF41_W5s44N2Vnxbf66GCsGdOY436vrKzQEJ6Hhk4yZghvyZTYw1HWRRXFzg46ETD9L5jf3l5jpUIrZPOSfNxMmBWKOFsB4J_rqNiDsqTo5HKMQh5hmWFtkGXfVgbpzjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ee0bbd03.mp4?token=cNdFT_nJde8VuHMP6W5aAK3edHil6Yg-5YEsJKAkdH9FVB6jW1UQ-_1UeKUL2ebmi8YKpx8Zt2LM68VQ12IjuFdMKGii0Q1MiHrGTSAh-NfxVAv4qEa1dVAF5JWQG_0MMJJCyglPyxV_2BWkZ3nu8mLl18udcM4_2J_o-H-5xalUNR6BxezISJbsbrFnG-sKQIikR4BD5bfiYa4mVbA7lF41_W5s44N2Vnxbf66GCsGdOY436vrKzQEJ6Hhk4yZghvyZTYw1HWRRXFzg46ETD9L5jf3l5jpUIrZPOSfNxMmBWKOFsB4J_rqNiDsqTo5HKMQh5hmWFtkGXfVgbpzjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
گام بعدی شما در قبال ایران چیست؟
ترامپ:
خب، اگر به شما بگویم، یک خبر بزرگ خواهید داشت، درست است؟ اما خودتان خواهید دید؛
همه‌چیز خیلی خوب پیش می‌رود. ایران وضعیت خوبی ندارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24792" target="_blank">📅 23:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا :‌
امروز
دو شهروند ایرانی،
سلام احمدیان ۳۶ ساله و رحمان صالحی ۳۴ ساله
، به اتهام آماده‌سازی برای انجام یک عملیات تروریستی علیه جامعه یهودیان در منچستر متهم شدند. این دو نفر
۲۹ شهریور
در منچستر بازداشت شده بودند. پلیس می‌گوید آنها با یک
طرف امنیتی ثالث خارج از بریتانیا که احتمال می‌رود در ایران باشد
در ارتباط بوده‌اند و تحقیقات درباره این پرونده ادامه دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24791" target="_blank">📅 23:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جروزالم پست: ایهود باراک، نخست‌وزیر پیشین اسرائیل، مدعی شد نتانیاهو ممکن است برای به‌تعویق انداختن انتخابات، زمینه یک جنگ جدید را فراهم کند. باراک گفت اگر شرایط سیاسی برای نتانیاهو نامساعد باشد، آغاز یک درگیری تازه می‌تواند برگزاری انتخابات را به تأخیر بیندازد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24790" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت خارجه آمریکا: در بیانیه‌ای مشترک به مناسبت سالگرد اجرای تحریم‌های «مکانیسم ماشه»، آمریکا و چند کشور دیگر بار دیگر بر تعهد خود برای اجرای محدودیت‌های سازمان ملل که از طریق این سازوکار علیه ایران بازگردانده شده‌اند، تأکید کردند.
این کشورها همچنین از ایران خواستند به تعهدات خود در زمینه منع اشاعه پایبند باشد، با آژانس بین‌المللی انرژی اتمی همکاری کامل داشته باشد و نگرانی‌های بین‌المللی درباره برنامه‌های هسته‌ای و موشک‌های بالستیک خود را برطرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24789" target="_blank">📅 23:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24788" target="_blank">📅 23:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24787" target="_blank">📅 22:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24786" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گویا معین هم اعلام کرد بر میگرده بزودی @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24785" target="_blank">📅 22:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت خارجه بریتانیا: آمریکا، انگلیس، فرانسه و آلمان در بیانیه‌ای مشترک اعلام میکنند که متعهد به جلوگیری از تأمین هرگونه مواد، تجهیزات و فناوری برای ایران هستند که بتواند در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد. این چهار کشور همچنین بر ضرورت همکاری کامل ایران با آژانس بین‌المللی انرژی اتمی و اجرای تعهدات پادمانی تأکید کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24784" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آکسیوس به قلم باراک راوید:
چرا واشنگتن و تهران مدام حرف یکدیگر را نمی‌فهمند؟آمریکا و ایران هر دو می‌گویند راه‌حل دیپلماتیک را به جنگ ترجیح می‌دهند، اما رسیدن به توافق از همیشه دشوارتر شده است. ریشه اختلافات در چهار موضوع است: واشنگتن توافقی سریع و بزرگ می‌خواهد، در حالی که تهران مذاکره طولانی‌تر و توافق‌های محدودتر را ترجیح می‌دهد؛ بی‌اعتمادی عمیقی میان دو طرف وجود دارد و هرکدام نگرانند طرف مقابل از مذاکرات برای آماده‌سازی اقدام بعدی استفاده کند؛ فشارهای سیاسی داخلی در آمریکا و ایران نیز مواضع دو طرف را سخت‌تر کرده است. در ۱۸ ماه گذشته، دو دور مذاکرات شکست خورده و هر دو بار پس از شکست مذاکرات، درگیری نظامی شدت گرفته است. اگر تلاش فعلی هم به بن‌بست برسد، خطر آغاز دور تازه‌ای از جنگ طی چند هفته وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24783" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏امیر قاسمی و رو‌کردن نام کسانی که با سپاه در ارتباط کامل قرار دارند ، آیا نفر بعدی که در ایران خواهید دید معین است؟ گزارشهایی هم هست که در کنسرت اخیر معین اجازه ورود پرچم شیر و خورشید داده نشد و فقط آهنگی برای ایران خوانده شد و در نمایشگر هم پرچمی نمایش داده…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24782" target="_blank">📅 22:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0950d9a5.mp4?token=mM6Lv26VsY7xI4JGiD3Xwj9LoXOTzOlAPOq1uk_In_d8C__OOcvwYGHV-D8ywR1qQcRtj0geP1QOqdRblKZ0pUYkY17wlMS5wNgUQFUz4AADG30FSX6Vx-SvJDUIgNdymnr3xhnThfSHbGdl2dI-YK4ao-_jmrXRI-ZljqCbbINhEBJ4m3JIXlxi4A6PqYOgcAa__tDaZ3RTmN7u4Ml5JTu0LkH6qCtSSTzCnBwVUvqd78fRGFAzUmymDgLQBetINzNn97VSeJeBlkOmmN365OLocSLpW7P_D-ERjEHS59k844C1oSoJStdWKAJUwoQDw7mgY1Bv5P1jZlxgW9sDtF_N4gjo82JyyL7rfcmXoDTFANZQZ6HNjsMPtvOX2qYjX0kY6A37uddIyS3mRPU1UmqQTyK7X475VsNSbafpL_rcw7BI1KcD2fJvRZ0cQKn4Jgi5dofXPBjY81B3HlM5z1rdaAED2x8uRwPs8_lQyT44b6hVqJCSxHA_GNRGuVIAr0LPZinw_8ZQG0ZsNCIF9m-2QbSvlw98CpwAN0p0jP_QMIeQ-PlKt3XXZM2DF7fVBcdRky_pJzR4XDOf_2ltNRwEkSy-W5hpueoSJOdESQ88qx3LP9hqtk0YrDt-j6-0EoaaAF6zOnUfPUCy15Xm2_MN2baDEBl1AH31sd7Q2y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0950d9a5.mp4?token=mM6Lv26VsY7xI4JGiD3Xwj9LoXOTzOlAPOq1uk_In_d8C__OOcvwYGHV-D8ywR1qQcRtj0geP1QOqdRblKZ0pUYkY17wlMS5wNgUQFUz4AADG30FSX6Vx-SvJDUIgNdymnr3xhnThfSHbGdl2dI-YK4ao-_jmrXRI-ZljqCbbINhEBJ4m3JIXlxi4A6PqYOgcAa__tDaZ3RTmN7u4Ml5JTu0LkH6qCtSSTzCnBwVUvqd78fRGFAzUmymDgLQBetINzNn97VSeJeBlkOmmN365OLocSLpW7P_D-ERjEHS59k844C1oSoJStdWKAJUwoQDw7mgY1Bv5P1jZlxgW9sDtF_N4gjo82JyyL7rfcmXoDTFANZQZ6HNjsMPtvOX2qYjX0kY6A37uddIyS3mRPU1UmqQTyK7X475VsNSbafpL_rcw7BI1KcD2fJvRZ0cQKn4Jgi5dofXPBjY81B3HlM5z1rdaAED2x8uRwPs8_lQyT44b6hVqJCSxHA_GNRGuVIAr0LPZinw_8ZQG0ZsNCIF9m-2QbSvlw98CpwAN0p0jP_QMIeQ-PlKt3XXZM2DF7fVBcdRky_pJzR4XDOf_2ltNRwEkSy-W5hpueoSJOdESQ88qx3LP9hqtk0YrDt-j6-0EoaaAF6zOnUfPUCy15Xm2_MN2baDEBl1AH31sd7Q2y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترابری سنگین نظامی آمریکا از ۲۴ ساعت پیش تا دقایقی قبل…
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24781" target="_blank">📅 21:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رئیس انجمن صنفی تولیدکنندگان شیرآلات: اگر محاصره دو ماه دیگر ادامه پیدا کند کل کارخانه‌های شیرآلات تعطیل خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24780" target="_blank">📅 21:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24779" target="_blank">📅 21:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR-cmAABu8RaWzIHDxE6OA37mOSJMTKcE7TlAMJc-WCNkJ3-qWNIAFJsvNUI69d_PAgSo9ltIP-BTL_CosilqNQTj_qXbCUlTv6KO4_GcjH4ypG1PoBL0gRl2BevoTTDfKgGAdFnvis7de_s_x2q-F2n9g-nEvoLWUk9psKS7qAeWj4HgK2A9pOMWFgoBBb_wF2bi1DJprpCzn8CBjI5VrFQSrBtqqrAoZOcxDwZZTB8_8UxswvBuRA9ZSKpCZaxtwpwl2TrLyyPagcGE7MX5JIVGGoY3wIClQHicM27fRV3TLIS7Zoo2Kevhfc4fNDNSC6YM233Y_CWOkWk81yPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ پی-۸ پوسایدون ، ۵ سوخترسان ، ۱ هرکولس و ۳ هواپیمای ترابری سنگین سی۱۷ هم اکنون در محدوده خلیج فارس و همچنین سوخترسانی هم از اسرائیل به سمنت منطقه می آید
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24778" target="_blank">📅 21:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24777" target="_blank">📅 20:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emOWnTM5TBfLLBdL8UIKSQz0MsDZFVKHy0RbkUN6pbq_zExgYGFbdie2Fs4nt5dExQJ9mYY8wN7j23UcNGsAjdRq_OpisKmkqhD_J8-4aSYFORReYfmX15XufYiWFd_ieIJMjPehImffSzH7a6Ec6CApX0Omz45a_qkqigOFBXZ86ExdzDDhr1vYyMdbxuY_4jvRj9fgVYEqBI2aeuoBrQIoX5hjNAxtJU-alvhG5_4UnmNHm66VWCPGljpVO4DkazI8QxLM6ZGJHICm1TmgdDUclR-yCSAKLyXRz8gi10KtLSOFGdWt2Vsk3uTfzCbgaf2FRVdvFjf17GkjbvisfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظارت دریایی بریتانیا اعلام کرد که ناخدای یک تانکر نفتی گزارش داده است که این کشتی در حین عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
یک آتش‌سوزی کوچک و قطعی برق به طور موقت رخ داد، اما آتش‌سوزی خاموش شده و کشتی در حال حرکت است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24776" target="_blank">📅 20:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کوین‌دسک:
سیتی‌گروپ هدف ۱۲ماهه بیت‌کوین را به ۱۱۳ هزار دلار و هدف اتریوم را به ۳٬۰۲۸ دلار افزایش داده است.
این اهداف، پیش‌بینی بانک هستند و قیمت تضمین‌شده محسوب نمی‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24775" target="_blank">📅 18:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=W33kYDgXkyKp9Lbej_L-2g_YnbLraaISU0E8mpQya7kCaAIt_xnICCt9KQXemMIByq1sdevNNoNGKjpKEcmEAjgjrKCbPWE6kTIP7fT50SHnCfM_zxm0HKO3hmlspK-nP5tMJAaev1SSqdw3CJGompD1PKCJc92UIUGvpyxphngUlwdJ0_q4ohzmxPjpgrRBRZsCoKAH9uU5sTuCPgmpHKYzau-vP92L1nSHNmguetid8tbW9O1iiqsMs6O668A6xpLCvg3KVdgnz0lF7qJm8ewOtgg1d9ilTiV6WgILAu_nNlp1zOd8QfA0QX9Gkv_7u6ivGkAHJZecIfOU179o_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=W33kYDgXkyKp9Lbej_L-2g_YnbLraaISU0E8mpQya7kCaAIt_xnICCt9KQXemMIByq1sdevNNoNGKjpKEcmEAjgjrKCbPWE6kTIP7fT50SHnCfM_zxm0HKO3hmlspK-nP5tMJAaev1SSqdw3CJGompD1PKCJc92UIUGvpyxphngUlwdJ0_q4ohzmxPjpgrRBRZsCoKAH9uU5sTuCPgmpHKYzau-vP92L1nSHNmguetid8tbW9O1iiqsMs6O668A6xpLCvg3KVdgnz0lF7qJm8ewOtgg1d9ilTiV6WgILAu_nNlp1zOd8QfA0QX9Gkv_7u6ivGkAHJZecIfOU179o_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الکس پیلیتساس
(
تحلیل‌گر امنیت ملی آمریکا، کارشناس ضدتروریسم و افسر سابق پنتاگون
) در سی‌ان‌ان بخوبی استراتژی جمهوری اسلامی رو توضیح میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24774" target="_blank">📅 18:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye7tUR5RATcocHNlsPPwQohkunab7oQEn5qFUpivxBo57p9pOeiXdHcRkUeymKG39voOksb0CRewuN4dqiq9uUudvlzAavZjsn9fdqkPOQXScx7B0izhhTO1VJ9PEZm1CgzfzeZIzvIhHrhRPtAgFagAFtEpzyNPRxbtYE28ClW3TKfUcj9w7JpFMhOSVdcluifkThuOCoIsyqV7wGPzUAULOuWA9-kKg94ABLuJnIRLEXaHRSqJ5_0_kTdL8_bWl6Ne1wn7uEOylDEGbL3FJZMadpgvkEtStOGHhaT43oTFNsT2liHcDzTNDQ3T45aNm5us4jQsfW6YnIyLQHP1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الناز شاکردوست به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس و دو سال محرومیت محکوم شده است. وکیل او گفته این حکم صرفاً به دلیل انتشار یک استوری پس از حوادث دی‌ماه سال گذشته صادر شده و محتوای آن تنها بیان اندوه بابت جان‌باختن جوانان ایران بوده است. به گفته وکیل شاکردوست، در این نوشته هیچ اشاره‌ای به نظام، حکومت یا مسئولان و همچنین هیچ فراخوانی برای اقدام جمعی، فعالیت سازمان‌یافته یا براندازی وجود نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24773" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=R6u_w6rAPkQoFiXIgFJvLLdJPOf6PATWSZRQ3jkw_qMB2ObFc3Mr-WNWA2egCP0ktFTOcD4eyMR9O02Ztsc1PeAdqrwhGEd6722BhRqH2jYPYVtp_s7veI86obMVPP8-l0CxS8u3USLXvoHKVdzuLjhwRFjTcQUbkIqCVkdzgEnySiGIxrmTQ9FHMcBWaJwlsR5c-L4Gf7cpwuLVvm3pCzSRa3xHFgcLrP_QbdbdUTDC7-99baSI0eHNi2un2MY0vowzeP5LusXYjNGirp941j5ImA5LeInfzEhDhRlUMiZ0IbbbT8t1KOnZJARn8LdaQW9IH-zwShvQneXct04L50VLc3A2sM2x_BlgJLMKg9RsMyKVtQJAXhJA5Rpd_7ScLUMfDh4QQJuk5FlO2nUEfXMBwqOxZ7YXet2wNBohzdx6jWrRcrosgFIvnIK6rI-x3T404AxrqI6O4s2v7XaWgvNayIp4yq5BDl1vsYh2hPVwu16yEK_qDYF64QiXg1oEO_A3treyUcippRAUw-3KCgFx71v9PFih82fvI6T4J3qKNDzx89fmNsnci6u4zvAe0TTiXoIi0D-jAfhuE3-U2jmN585JS7txH5FlYgK398R-tNlj2MNeRVrCw90_OjsjmKWBWqlaq4O-2FCXXS0-4E4eXyssRcGmxOgTlAzebZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=R6u_w6rAPkQoFiXIgFJvLLdJPOf6PATWSZRQ3jkw_qMB2ObFc3Mr-WNWA2egCP0ktFTOcD4eyMR9O02Ztsc1PeAdqrwhGEd6722BhRqH2jYPYVtp_s7veI86obMVPP8-l0CxS8u3USLXvoHKVdzuLjhwRFjTcQUbkIqCVkdzgEnySiGIxrmTQ9FHMcBWaJwlsR5c-L4Gf7cpwuLVvm3pCzSRa3xHFgcLrP_QbdbdUTDC7-99baSI0eHNi2un2MY0vowzeP5LusXYjNGirp941j5ImA5LeInfzEhDhRlUMiZ0IbbbT8t1KOnZJARn8LdaQW9IH-zwShvQneXct04L50VLc3A2sM2x_BlgJLMKg9RsMyKVtQJAXhJA5Rpd_7ScLUMfDh4QQJuk5FlO2nUEfXMBwqOxZ7YXet2wNBohzdx6jWrRcrosgFIvnIK6rI-x3T404AxrqI6O4s2v7XaWgvNayIp4yq5BDl1vsYh2hPVwu16yEK_qDYF64QiXg1oEO_A3treyUcippRAUw-3KCgFx71v9PFih82fvI6T4J3qKNDzx89fmNsnci6u4zvAe0TTiXoIi0D-jAfhuE3-U2jmN585JS7txH5FlYgK398R-tNlj2MNeRVrCw90_OjsjmKWBWqlaq4O-2FCXXS0-4E4eXyssRcGmxOgTlAzebZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مرد فرهیخته ، ژنرال جک کین : مبارزان ایرانی در گروه‌های متعددی سازماندهی شدند و میخواهند مسلح شوند تا کشورشان را پس بگیرند ، هم مسلح کردن ایرانی‌ها لازم هست هم اقدام نظامی شدید در لحظه مناسب بخصوص بعد از فروپاشی اقتصادی
گزینه توافق و دیپلماسی کاملا کنسل است
‏این رژیم باید سرنگون شود..
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24772" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ در‌تروث : «اروپا به‌تازگی با آزادسازی حجم عظیمی از ذخایر بسیار زیاد دیزل خود موافقت کرده است. این روند بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24771" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شبکه 14 اسرائیل: ما رهبر ایران رو وسط تهران کشتیم و هزینه خاصی هم پرداخت نکردیم. اون مرکز رنج ما بود.  ما فکر میکردیم ایران کار دیوانه واری انجام بده ولی فقط 40 روز جنگید و بعدشم به توقف جنگ رضایت داد. دو دهه الکی ترسیده بودیم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24770" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: مأموران سرویس مخفی به من گفتند به‌دلیل بدی آب‌وهوا احتمالاً باید سفر به اوکلاهما را لغو کنیم؛ نه هلیکوپتر می‌توانست پرواز کند و نه هواپیما. گفتند تنها راه، یک رانندگی طولانی است. از آنها پرسیدم «بیست با چه سرعتی می‌تواند حرکت کند؟» گفتند نزدیک به ۱۰۰ مایل بر ساعت.
گفتم: «پس سریع باسن تپلتون رو بزارین تو ماشین و راه بیفتید!»
این سفر آسانی نبود، اما نمی‌خواستم مردمی را که ساعت‌ها برای دیدنم در اوکلاهما منتظر مانده بودند، ناامید کنم.
@WarRoom
👏</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24769" target="_blank">📅 17:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=cXrBIdbRl0gE0fWw-MQEPq763JHFLig-_4I55Qy57AdCLB3aiLOlFhymdSmcezZVmyHHBsefdHEI6lCe2j1Yft8IYRZvs2v3dWhwTzuotWBalkW3ndmjSEemPz4WOvnb9z0RoNZsVbCdym2MhxOCzTzwvvheY-1S8VNlv5DKC0z-KRM8dSvERz48JmyD2S33HS9q32fo9JYIw9zphIMFRZ63STMJr-2d5MTJrVJhE3jWKL6-kXQlLLapi9cXtiAB-B3Ijp6txvXKtWQQ1co2ScJo4ZzZxhODLPpz2Nrzdh69t0JmdkgNH2X5M5brhE2h8TXJpW6xa3YZs8R1jBISPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=cXrBIdbRl0gE0fWw-MQEPq763JHFLig-_4I55Qy57AdCLB3aiLOlFhymdSmcezZVmyHHBsefdHEI6lCe2j1Yft8IYRZvs2v3dWhwTzuotWBalkW3ndmjSEemPz4WOvnb9z0RoNZsVbCdym2MhxOCzTzwvvheY-1S8VNlv5DKC0z-KRM8dSvERz48JmyD2S33HS9q32fo9JYIw9zphIMFRZ63STMJr-2d5MTJrVJhE3jWKL6-kXQlLLapi9cXtiAB-B3Ijp6txvXKtWQQ1co2ScJo4ZzZxhODLPpz2Nrzdh69t0JmdkgNH2X5M5brhE2h8TXJpW6xa3YZs8R1jBISPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
«هر چه زمان می‌گذرد، تصویر واضح‌تر می‌شود. این عمل، نتیجه‌ی افراط‌گرایی اسلامی بود و هدف آن، سرنگون کردن هواپیما به همراه تمام مسافرانش بود.ما در حال بررسی این موضوع هستیم که آیا این فرد برای انجام این کار اعزام شده بود یا خیر، و هر کسی که مسئول این اقدام باشد، باید پاسخگوی عواقب بسیار سنگینی باشد.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24768" target="_blank">📅 17:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرمانده انتظامی رشت اعلام کرد یک روحانی در یکی از محله‌های این شهر توسط فردی ناشناس با سلاح سرد مجروح شده است. به گفته سرهنگ عیسی روشن‌قلب، پلیس در جریان تحقیقات به سرنخ‌های مهمی درباره ضارب دست یافته و تیم‌های تخصصی با هماهنگی مقام قضایی برای دستگیری او تلاش می‌کنند. وضعیت فرد مجروح مساعد اعلام شده و پلیس گفته علت و انگیزه حمله پس از دستگیری متهم و تکمیل تحقیقات مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24767" target="_blank">📅 17:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رعد ‌و برق در تهران ، نترسید
@WarRoom
🫂</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24766" target="_blank">📅 16:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ در ‌تروث: «با خوشحالی اعلام می‌کنم توافق با کره جنوبی هر روز بهتر می‌شود! ۸.۴ میلیارد دلار برای یک پروژه افزایش برداشت نفت اختصاص داده شده است. تولید بیشتر نفت و گاز یعنی تقویت سلطه انرژی آمریکا و تضمین امنیت انرژی در جهان برای آینده.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24765" target="_blank">📅 16:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.» @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24764" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c997284691.mp4?token=fmdhJ9khrdxPjkGp_zg1IRnvziMRtQbQy6-aqmDjftB9sSFIOXXR2XknVOSdkNVzWXF2R4WOT9_tcFt_tPU6-TkQC1hNN3XJ6q15tczOx32H0rQbzJSq_hUFTMyN9ectKmXB3E8N-dQYP7DmSnMKCN3kfXfB7T_OdlJL0MD03gTM64oIlj0FfS97iUnyKSjm8MxvDsR1EQD7Gq51VisKR_5-rDuS29OqpG9vfgFY7WJjckIF5OaIrDD7e9Y5LjOUSRjl37Shd1ZFLxaxskW2nQF27Fys2mxskKfaZrebjvr_2VmNwjT-KdJz8qFQUT1QhIa3H4QlyBRogOgqvEaXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c997284691.mp4?token=fmdhJ9khrdxPjkGp_zg1IRnvziMRtQbQy6-aqmDjftB9sSFIOXXR2XknVOSdkNVzWXF2R4WOT9_tcFt_tPU6-TkQC1hNN3XJ6q15tczOx32H0rQbzJSq_hUFTMyN9ectKmXB3E8N-dQYP7DmSnMKCN3kfXfB7T_OdlJL0MD03gTM64oIlj0FfS97iUnyKSjm8MxvDsR1EQD7Gq51VisKR_5-rDuS29OqpG9vfgFY7WJjckIF5OaIrDD7e9Y5LjOUSRjl37Shd1ZFLxaxskW2nQF27Fys2mxskKfaZrebjvr_2VmNwjT-KdJz8qFQUT1QhIa3H4QlyBRogOgqvEaXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24763" target="_blank">📅 16:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تتر ۲۶۳،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24762" target="_blank">📅 15:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24761" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=DWoyv3zPqeAc6g-bu42Z0E1EwYQHFIaMGVM_w5sajLcvhwV49DnCpgLof1h5nfUX05yX7SQw86xfxLp6SKRxnEbaweK5x2bNtES1HYTdAkFVUmmdx_Nqtxzlxbl6u01D0D6_uujfvi_wWmgOS3nZQMLo_i4BdXvxNS9JA_fFlHgremI1dfIwRsmpmAM0Bxh7qk7UlcPc0tUVU0O2merJF0z3yy6GIrN50Hbi6uzGRwARoQZP7cO6c9MJ7YRixTDWEG8Ws_IhpIkHktaJsvONVIXzQ789DLR_b2gQ7wbY3ucxSLcoLeDXXFZMsa2ckSn6-POB3qnzMiHssRgcRq2AAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=DWoyv3zPqeAc6g-bu42Z0E1EwYQHFIaMGVM_w5sajLcvhwV49DnCpgLof1h5nfUX05yX7SQw86xfxLp6SKRxnEbaweK5x2bNtES1HYTdAkFVUmmdx_Nqtxzlxbl6u01D0D6_uujfvi_wWmgOS3nZQMLo_i4BdXvxNS9JA_fFlHgremI1dfIwRsmpmAM0Bxh7qk7UlcPc0tUVU0O2merJF0z3yy6GIrN50Hbi6uzGRwARoQZP7cO6c9MJ7YRixTDWEG8Ws_IhpIkHktaJsvONVIXzQ789DLR_b2gQ7wbY3ucxSLcoLeDXXFZMsa2ckSn6-POB3qnzMiHssRgcRq2AAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : دیگ به دیگ میگه باسن تو سیاهه
قیصر فرندلی فایر بیژنو میزنه
😂
این قشنگه
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24760" target="_blank">📅 15:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حقیقت یاب
اتاق جنگ:
خبری که با عنوان «ارتش آمریکا رسماً تمرین تصرف و پاکسازی تأسیسات هسته‌ای زیرزمینی را انجام داد» در حال انتشار است،
خبر جدیدی نیست
و مربوط به ژوئن ۲۰۲۴ است. ارتش آمریکا اعلام کرده بود تیم «خنثی‌سازی هسته‌ای ۱» همراه با نیروهای
هنگ ۷۵ رنجر
در یک تمرین نظامی، یک تأسیسات هسته‌ای زیرزمینی شبیه‌سازی‌شده را در شرایط آتش شبیه‌سازی‌شده تصرف و پاکسازی کرده‌اند. این تمرین با هدف افزایش آمادگی برای شناسایی، ایمن‌سازی و خنثی‌سازی تهدیدهای هسته‌ای و پرتوی انجام شده بود. بنابراین انتشار دوباره این گزارش به‌عنوان یک
تحرک یا تمرین جدید آمریکا
نادرست است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24759" target="_blank">📅 15:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مرد خردمند ، مارک لوین : این جنگ هیچ‌وقت درباره تنگه هرمز نبوده؛ اگرچه حفظ جریان نفت دستاورد بزرگی است. فشار اقتصادی علیه جمهوری اسلامی بسیار موفق بوده و همچنین سایت‌های هسته‌ای و اورانیوم غنی‌شده دفن شده اند. اما تنها راه جلوگیری از دستیابی ایران به سلاح هسته‌ای، با داشتن هزاران موشک بالستیک و ادامه حمایتش از تروریسم، نابودی این رژیم است. هیچ راه خروج خوبی وجود ندارد. من همچنان خواستار
مسلح کردن
مردم ایران و
ارائه آموزش، پشتیبانی فنی و پوشش هوایی
مورد نیاز آن هستم. ما پیش از این در کشورهای دیگر چنین کاری کرده‌ایم و با توجه به ضربات واردشده به ایران، به‌ویژه فروپاشی اقتصادی، معتقدم زمان اقدام اکنون است یا دست‌کم به‌زودی فرا می‌رسد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24758" target="_blank">📅 14:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فایننشال تایمز: ترامپ در فکر حمله آخرالزمانی‌به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24756" target="_blank">📅 14:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.      البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است @WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24755" target="_blank">📅 13:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جزئیات جدیدی از دولت
ترامپ
در گزارش مجله تایم :
گروک، چت‌بات هوش مصنوعی شرکت X
، تا حدی در متقاعد کردن ترامپ برای این دیدگاه نقش داشته که
ربودن نیکلاس مادورو، رئیس‌جمهور ونزوئلا، می‌تواند میراث سیاسی او را تثبیت کند
.
در بخشی دیگر تایم گفت ، ترامپ از سوی مقام‌های ارشد مستقیماً در جریان
مشکلات مربوط به ذخایر مهمات آمریکا
قرار نگرفته و این موضوع را از طریق گزارشی در
نیویورک‌تایمز
متوجه شده است. ترامپ سپس با
پیت هگست
، وزیر جنگ آمریکا، درباره این موضوع بحث کرد و هگست او را متقاعد کرد که این گزارش‌ها
«اخبار جعلی»
هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24754" target="_blank">📅 13:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در‌ انتظار تایید : قرائتی ، ورّاج صدا و سیما ، ریق رحمت را سر کشید
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24753" target="_blank">📅 13:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enuluFTOW0vfJAAJy0k-sgcNYfW8SOfu6AxK8G6IN248gIWjBowGV0tfFqHi8lR59z6wl1rUSSEIE2B6GVs7MIX9GwJOZV5A-sgKhNqlmSdyTDwj32VudoQTRXZDNMtjRqzATSwZIBq4tS2DHgaH00Wv8WX85SBOLZ4UwCXLcZerj_hJsKxPfHvq1TGGl-N6hMua6ZUi61iaBJvuuphKmAThIFuL7OXHXzAnWt8_W4Pmf9h894_AUjgjTwnhiIWo5ZgLK2gkODNcWK81QaHzaiK1AhSWrQJ2Olwwg2xbK-4bQX8_vV_Ztm6Bjw41JKZAKdGCKDcbpXhPGZuiJ5tWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلامیه خواهر عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24752" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیژن مرتضوی: در جانفدا ثبت نام کردم
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24751" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ:
اینا آدم‌های دیوانه‌ای هستند، که ۵۰ ساله  است فریاد می‌زنند «مرگ بر آمریکا».
جنگ با جمهوری اسلامی خیلی زود تمام می‌شود. ایران با تورم ۳۱۲ درصدی و سقوط ارزش پول روبه‌رو شده است، بخش بزرگی از رهبرانش هم دیگر نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24750" target="_blank">📅 13:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الجزیره:
مایک والتز، سفیر آمریکا در سازمان ملل، گفت ایران همچنان اورانیوم را تا سطح ۶۰ درصد غنی‌سازی می‌کند
و حاضر نیست از جاه‌طلبی‌های هسته‌ای خود دست بکشد. والتز همچنین ایران را به نقض قوانین بین‌المللی و محدود کردن دسترسی بازرسان آژانس بین‌المللی انرژی اتمی متهم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24749" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پولیتیکو:
فرانسه و ترکیه بر سر توافق‌های جدید همکاری ناتو با آذربایجان و ارمنستان به بن‌بست رسیده‌اند.
فرانسه با توافق همکاری با آذربایجان مخالفت کرده و ترکیه در واکنش خواستار تصویب هم‌زمان توافق همکاری با ارمنستان شده است. این توافق‌ها شامل
رزمایش و آموزش نظامی و تقویت همکاری سیاسی و دفاعی
است و بیش از یک سال در ناتو بلاتکلیف مانده‌اند. دیپلمات‌های ناتو هشدار داده‌اند این بن‌بست می‌تواند روند نزدیک‌شدن ارمنستان و آذربایجان به غرب را دشوارتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24748" target="_blank">📅 13:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.
البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است
@WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24747" target="_blank">📅 12:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز: عبور محموله‌های ال‌ان‌جی از تنگه هرمز در سپتامبر به بالاترین میزان از آغاز جنگ رسید. بر اساس داده‌های S&P Global، ۱۹ محموله شامل ۱۳ محموله از قطر و ۶ محموله از امارات از تنگه عبور کردند؛ داده‌های کپلر این رقم را ۲۱ محموله اعلام کرده است. با این حال،…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24746" target="_blank">📅 12:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رویترز:
عبور محموله‌های ال‌ان‌جی از تنگه هرمز در سپتامبر به بالاترین میزان از آغاز جنگ رسید.
بر اساس داده‌های S&P Global، ۱۹ محموله شامل ۱۳ محموله از قطر و ۶ محموله از امارات از تنگه عبور کردند؛ داده‌های کپلر این رقم را ۲۱ محموله اعلام کرده است. با این حال، برخی کشتی‌های قطری برای عبور از منطقه، سامانه ردیابی خودکار خود را خاموش کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24745" target="_blank">📅 12:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">درگیری مسلحانه میان نیروهای امنیتی رژیم و یک گروه مهاجم در یکی از روستاهای شهرستان راسک در جنوب سیستان‌وبلوچستان رخ داده است. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24744" target="_blank">📅 12:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">درگیری مسلحانه میان نیروهای امنیتی رژیم
و یک گروه مهاجم در یکی از روستاهای شهرستان راسک در جنوب سیستان‌وبلوچستان رخ داده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24743" target="_blank">📅 12:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57b1f32b3.mp4?token=hW_n-Jm-AYWqODrza2f5A3hfH1uAo0Jkae0mx87Jer5Wql2qoN0XHnFxAs0SXB_0hNgU_dSPyt7KImgjrbffi2nHKqDBl1KkKrzm3dm8urFmX_k3tqGKUhpkNVMHXsiPcaSiuyfSPgtkm6d0uEtQnt7DLENA4qsmjJqxlvaSp5tuT8vPm7w7otswWaP_Wt0JIRohjkO3RfVyiJhowrqfc8B1Vic-RRZFdZYNkqLvwqPrQ0z1Fwm_Nw7pibCFLiIcixJVMva0qPvdUYDr5K5ihQm1uH7fZNdNE2Vp4Kd0ifp76SWSBzU7y-2AISXw9QBzPatojR6DeXW6C1orquErdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57b1f32b3.mp4?token=hW_n-Jm-AYWqODrza2f5A3hfH1uAo0Jkae0mx87Jer5Wql2qoN0XHnFxAs0SXB_0hNgU_dSPyt7KImgjrbffi2nHKqDBl1KkKrzm3dm8urFmX_k3tqGKUhpkNVMHXsiPcaSiuyfSPgtkm6d0uEtQnt7DLENA4qsmjJqxlvaSp5tuT8vPm7w7otswWaP_Wt0JIRohjkO3RfVyiJhowrqfc8B1Vic-RRZFdZYNkqLvwqPrQ0z1Fwm_Nw7pibCFLiIcixJVMva0qPvdUYDr5K5ihQm1uH7fZNdNE2Vp4Kd0ifp76SWSBzU7y-2AISXw9QBzPatojR6DeXW6C1orquErdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت‌وگذار یک دانشجوی عراقی با خودروی آمریکایی دوج چارجر در همدان، در حالی که تصویر تروریستها؛ علی خامنه‌ای، قاسم سلیمانی و ابومهدی المهندس (جمال جعفر محمدعلی آل‌ابراهیم، معاون پیشین حشدالشعبی عراق) روی بدنه آن نقش بسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24742" target="_blank">📅 11:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd60bc703d.mp4?token=cgOdAfGqqPZmdxDgiMTt-QtlWuEzupYcxnZJjByBDmyZNcAv7U3VUoy5_iOCRWSmwLT_OOAVak-WGis3NsUQW1cVR9urkQ_ikzLGnB88eo8WflS5JT8ckLGmcL3fGk8EqeWki7Jpwy01FYR9G574K6jlfmkQT91VpjTQsDWz70X5_2nRR-7wHvXawo8poGrdKZMBFL8ciZqP_W-6fNASR3ryOx0EWwywuEu7ZlL0Js1kIBzNNzIOoLgWv1z0Tjrk5eOfuzPUtAlA2XoB817Dg-feHcyKOtD73EWjRwhBynqmQyNhpOibdIPyoNSb9T4QZiFCScugbtwUA7jsy4QrLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd60bc703d.mp4?token=cgOdAfGqqPZmdxDgiMTt-QtlWuEzupYcxnZJjByBDmyZNcAv7U3VUoy5_iOCRWSmwLT_OOAVak-WGis3NsUQW1cVR9urkQ_ikzLGnB88eo8WflS5JT8ckLGmcL3fGk8EqeWki7Jpwy01FYR9G574K6jlfmkQT91VpjTQsDWz70X5_2nRR-7wHvXawo8poGrdKZMBFL8ciZqP_W-6fNASR3ryOx0EWwywuEu7ZlL0Js1kIBzNNzIOoLgWv1z0Tjrk5eOfuzPUtAlA2XoB817Dg-feHcyKOtD73EWjRwhBynqmQyNhpOibdIPyoNSb9T4QZiFCScugbtwUA7jsy4QrLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکسیوس: به نقل از یک مقام آمریکایی گزارش داد که گروه آماده اعزام آبی‌خاکی Makin Island و یگان اعزامی تفنگداران دریایی آمریکا (MEU) سیزدهم، پایگاه دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند و انتظار می‌رود تا پایان نوامبر به منطقه…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24741" target="_blank">📅 11:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: ایران رادارهای پیشرفته‌ای ندارد و گاهی اوقات سعی می‌کند مین‌های دریایی کار بگذارد، اما ما معمولاً آنها را قبل از اینکه بتوانند مستقر شوند، از بین می‌بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24740" target="_blank">📅 10:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رویترز:
نیروهای دولت رسمی یمن اعلام کردند طی حدود سه ساعت،
۲۰ حمله هوایی
علیه مواضع، نیروها، خودروها و تجهیزات نظامی حوثی‌هادر استان تعز انجام داده‌اند. این درگیری‌ها یکی از شدیدترین تشدیدهای نبرد میان نیروهای مورد حمایت عربستان و حوثی‌های مورد حمایت ایران از زمان آتش‌بس ۲۰۲۲ محسوب می‌شود. حدود
۱۹ جاده منتهی به استان تعز
نیز به دلیل درگیری‌ها بسته و مناطق اطراف آنها منطقه عملیاتی نظامی اعلام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24739" target="_blank">📅 10:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیویورک‌تایمز: به نقل از یک مقام امنیتی غربی گزارش داد که ایران حدود
۱۰ موشک کروز ضدکشتی و ۳۰ پهپاد
به سمت تنگه هرمز شلیک کرده است. به گفته این مقام،
۴ نفتکش هدف قرار گرفته‌اند
؛ هرچند آمار فعلی سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
۱۳ مورد
است. جنگنده‌ها و بالگردهای تهاجمی آمریکا برای مقابله با حملات ایران در آسمان تنگه هرمز فعال هستند، با این حال
برخی پرتابه‌ها همچنان به کشتی‌ها اصابت می‌کنند
.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24738" target="_blank">📅 10:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آکسیوس: به نقل از یک مقام آمریکایی گزارش داد که
گروه آماده اعزام آبی‌خاکی Makin Island
و
یگان اعزامی تفنگداران دریایی آمریکا (MEU) سیزدهم
، پایگاه دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند و انتظار می‌رود
تا پایان نوامبر
به منطقه برسند. این گروه شامل ناو تهاجمی آبی‌خاکی
USS Makin Island
از کلاس Wasp، ناو ترابری آبی‌خاکی
USS Anchorage
از کلاس San Antonio و ناو ترابری آبی‌خاکی
USS John P. Murtha
از همین کلاس است. این نیروها
۱۰ فروند جنگنده F-35B Lightning II
و حدود
۲۲۰۰ تفنگدار دریایی آمریکا
را به منطقه خواهند آورد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24737" target="_blank">📅 10:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آکسیوس: به نقل از دو مقام آمریکایی و یک منبع در غرب آسیا گزارش داد که آمریکا برای حفاظت از زیرساخت‌های نفت و گاز،
یک سامانه پدافند هوایی MIM-104 پاتریوت
به قطر و یک سامانه نیز به عربستان سعودی ارسال کرده است. بر اساس این گزارش، یک سامانه پاتریوت در
یک تأسیسات کلیدی نفتی در عربستان سعودی
و یک سامانه دیگر در
یک تأسیسات گاز طبیعی در قطر
مستقر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24736" target="_blank">📅 10:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3218939c94.mp4?token=QXmP98IgcvLm5PYLmdgqo9Exnv3r24gV4-nqaHqiCqCs9H_tQLnpiIryyVCTDMX6BL_XU6qpGhDDkMEvkXm03GBttX19jMhCBDk4nCm_DHclUuXBGfSrCChShtlLaKhbiVk6-S7fFTtCymM0YjHWtJ3-Hb0gY2i9fwLeP1RfyioBv8bIy-nsytqwC627KJ45r37Rry87zsrbaxj8Atx5xPWdVe-iy4-ri5HWzXLqEr-VzAxNgQTznVeWAdJnpV4mfpYkNyCf_a2wZarcsAXH172hs8ZAFMC1mg4fIo_Lou0wadNVHvtYS03gYG84qFvlxcAiv69ozGhppH375NRdvYUDZmu5YmAjKMNsyjP4SxCwTMKM0-TPKOcdRg6OwBPIwvZXd4WM6534QkaFeYAmM6kgSKoiMhfzsWAbjBzASgwYfQcdvBzIdUdKVlt2k1JfsBXd3EgaswijMeJlZC0VkTXfb5tGS56r7jwRla3lZzMB6vLmnf8neVUkxGIfvUg0a6yrtYdE22Q4_A3zjVa-IUm4UIBkMHH5s450LSlbS6fKcGBcFZ8av1qY72h6cacXdkycs_vngRTZ-Dtk9KjuHNQ6QDJYtcPEISGbq4mmSDzw8p-sdZpRwFjaBZSc5ll0H9NxrNy6yVol3fd6rYxl-gWgli2hnRHSQQEVlqu41Lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3218939c94.mp4?token=QXmP98IgcvLm5PYLmdgqo9Exnv3r24gV4-nqaHqiCqCs9H_tQLnpiIryyVCTDMX6BL_XU6qpGhDDkMEvkXm03GBttX19jMhCBDk4nCm_DHclUuXBGfSrCChShtlLaKhbiVk6-S7fFTtCymM0YjHWtJ3-Hb0gY2i9fwLeP1RfyioBv8bIy-nsytqwC627KJ45r37Rry87zsrbaxj8Atx5xPWdVe-iy4-ri5HWzXLqEr-VzAxNgQTznVeWAdJnpV4mfpYkNyCf_a2wZarcsAXH172hs8ZAFMC1mg4fIo_Lou0wadNVHvtYS03gYG84qFvlxcAiv69ozGhppH375NRdvYUDZmu5YmAjKMNsyjP4SxCwTMKM0-TPKOcdRg6OwBPIwvZXd4WM6534QkaFeYAmM6kgSKoiMhfzsWAbjBzASgwYfQcdvBzIdUdKVlt2k1JfsBXd3EgaswijMeJlZC0VkTXfb5tGS56r7jwRla3lZzMB6vLmnf8neVUkxGIfvUg0a6yrtYdE22Q4_A3zjVa-IUm4UIBkMHH5s450LSlbS6fKcGBcFZ8av1qY72h6cacXdkycs_vngRTZ-Dtk9KjuHNQ6QDJYtcPEISGbq4mmSDzw8p-sdZpRwFjaBZSc5ll0H9NxrNy6yVol3fd6rYxl-gWgli2hnRHSQQEVlqu41Lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره عملیات«چکش نیم شب»: بمب‌افکن‌های ما از میزوری پرواز کردند، رفتند و برگشتند؛ ۳۷ ساعت در مسیر بودند و سوخت‌گیری می‌کردند. ساعت یک صبح، وقتی ماه نبود و هوا کاملاً تاریک بود، همه بمب‌ها را رها کردند و مستقیم رفتند پایین، روی این «کارخانه‌های مواد مخدر»… بمب‌ها مستقیماً از مسیرهای هوایی به داخل این، اِمم، کارخانه‌های مواد مخدر رفتند؛ واقعاً همین کاری بود که آنها انجام می‌دادند. آنها هسته‌ای و مواد مخدر بودند. آنها مواد مخدر تولید می‌کردند. این کارخانه‌های مواد مخدر/هسته‌ای به‌شدت هدف قرار گرفتند.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24735" target="_blank">📅 10:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیانیه وزارت امور خارجه ایران: تهران
محدودیت‌های اعمال‌شده بر تردد هوایی میان ایران و عراق
را محکوم کرد و مغایر با منافع و مصالح مشترک دو کشور دانست و اعلام کرد این محدودیت‌ها برای
هزاران مسافر، زائر، بیمار و دانشجو
مشکل ایجاد کرده است. ایران همچنین خواستار
رفع محدودیت‌ها و بازگشت پروازهای دو کشور به شرایط عادی
شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24734" target="_blank">📅 09:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: ما نمی‌خواهیم ایران را در هرج‌ومرج رها کنیم و بعد رئیس‌جمهور دیگری بیاید که شاید کاری را که ما انجام دادیم، انجام ندهد. رئیس‌جمهورهای قبلی باید خیلی وقت پیش به ایران رسیدگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24733" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت دادگستری آمریکا:
اشتون حامد الابودی، مهندس برق ۵۱ ساله و کارمند وزارت انرژی آمریکا، به اتهام تلاش برای ارائه حمایت مادی به
انصارالله یمن
( حوثی‌های تحت حمایت ایران ) بازداشت شد. او متهم است برای ارتقای ارتباطات این گروه، تهیه تجهیزات پهپادی و قطعات ساخت مواد منفجره اقدام کرده است. تحقیقات از دسامبر ۲۰۲۴ آغاز شد و در سپتامبر ۲۰۲۵، الابودی به مناطق تحت کنترل انصارالله در یمن سفر کرد. او همچنین با یک منبع محرمانه FBI که خود را عضو انصارالله معرفی کرده بود، درباره
ادغام سامانه‌های ارتباطی و راه‌اندازی یک مرکز ارتباطات سیار
همکاری و برای تهیه تجهیزات آن کمک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24732" target="_blank">📅 02:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24731" target="_blank">📅 02:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😥</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24730" target="_blank">📅 02:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ درباره جنگ با ایران: شاید پیش از انتخابات پیروز شویم... آن‌ها موشک‌هایی دارند، اما ما می‌توانیم از پسِ آن برآییم. ما می‌توانیم از پسِ آن برآییم. آن‌ها موشک‌هایی دارند، اما تعداد بسیار کمی از آن‌ها باقی مانده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24729" target="_blank">📅 02:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=IeSrniXfv4-kUqUFEWLnvhCPhLhzqTzwrJhDmVw9SGNLXZWj-2JuEOX1oPWka4FbMhgyWDhz6EJMf86e4t1sUY4CNLGC4lCXs9WaIj4DXm0fVJunRr676ZFdZTDUlefWO19yGcRsDCicFwku1k-T5AhIlp13yJdoBCUkBc9lIjHYaNHTqaQ86h6L1wq7OO-DbuCuG9AOgf5cVISM6z7BI9eVcgYcEeABgy04VVNEz_4ODsIFMdxrSYjDClX60FvjZjgEWkEFJd6TqwRQuKtl2prxCtgP_yTrjIJR-GXpcp_g1AucoYN0D_IpV02FRwgwwGVFaGaZjErV3tWnAX8R4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=IeSrniXfv4-kUqUFEWLnvhCPhLhzqTzwrJhDmVw9SGNLXZWj-2JuEOX1oPWka4FbMhgyWDhz6EJMf86e4t1sUY4CNLGC4lCXs9WaIj4DXm0fVJunRr676ZFdZTDUlefWO19yGcRsDCicFwku1k-T5AhIlp13yJdoBCUkBc9lIjHYaNHTqaQ86h6L1wq7OO-DbuCuG9AOgf5cVISM6z7BI9eVcgYcEeABgy04VVNEz_4ODsIFMdxrSYjDClX60FvjZjgEWkEFJd6TqwRQuKtl2prxCtgP_yTrjIJR-GXpcp_g1AucoYN0D_IpV02FRwgwwGVFaGaZjErV3tWnAX8R4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر
»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24728" target="_blank">📅 02:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=E0oQRiIXCXP8OR9f6NC7vjNCumtn6-ljc2S40lf2HcvMRKxcv-ph7uNdVGaPfmWxbN-YYn-MG_VAM6_Wnb6KCYodjaMiH3n7APOCbOSA9C57PUpixh22u-IaAO0A8t2OixDwdKSu3kZALGCSNtOEeJpCuH3U1aT6eVLgv36Qv8_pMxauGxe-GhUdosJhNZT5lTj_wXDgPhHyOEijp0GO5gkxs7tvgWr2R9-zjIPXFnBgSJ5zaJN1mTwQUDyl7brfVcR1bgMWLRGWLgVL88PSuvXqmf80bA52u2OZrW3cKooXAf8wPfPQB2_eukgBh83Uy4zDLLvouHnNRSEX3Q1xPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=E0oQRiIXCXP8OR9f6NC7vjNCumtn6-ljc2S40lf2HcvMRKxcv-ph7uNdVGaPfmWxbN-YYn-MG_VAM6_Wnb6KCYodjaMiH3n7APOCbOSA9C57PUpixh22u-IaAO0A8t2OixDwdKSu3kZALGCSNtOEeJpCuH3U1aT6eVLgv36Qv8_pMxauGxe-GhUdosJhNZT5lTj_wXDgPhHyOEijp0GO5gkxs7tvgWr2R9-zjIPXFnBgSJ5zaJN1mTwQUDyl7brfVcR1bgMWLRGWLgVL88PSuvXqmf80bA52u2OZrW3cKooXAf8wPfPQB2_eukgBh83Uy4zDLLvouHnNRSEX3Q1xPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره اروپا:
«به آنچه برای
اروپا اتفاق افتاده
نگاه کنید. آنها دارند
زنده‌زنده خورده می‌شوند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24727" target="_blank">📅 02:00 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
