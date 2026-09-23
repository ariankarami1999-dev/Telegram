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
<img src="https://cdn4.telesco.pe/file/T1l153eRC7HUg4l-nE7IVlI36daV8HIJJOlY5_hlO8aQJs47VmMpbPKt2J0viwLWtRFy5cOe-pGz6zbby0qgiig468RKeNLHjdQc4kI8nQWpPmRMO2wZ6xd2K6dwoRbWuQnIoLtdhrREDrVqz3dP0AKawDnQCtd145smfL632J4ludbtgUrnnQJ3zlxZzfkEtwnGlGBNE35Q615Vp23YVJ8cabR4GSgDdjY_WgOgDY_gx9b0JvAFTZDnBYxK6Sda8bp-_dS0yaEI63A-4KycdYsAgQTcyhk3pO5X4ZUk_gHUfHBbEBusc_uwLe-Jd8qynQLv1viLlPzF5_cvQbU7gA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 455K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 08:53:36</div>
<hr>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392110b2f5.mp4?token=rFT8x3lhmiME-5vfNYpuEnqyZaWj0qGyuG_gMIGVjeOP0GsIqOVA30OxQ9DsE6_S8vfVG29bw5t9u9Hd2z9vVcehUt9ytD8J5Kw3YN3qvm58ELLVrnpZOhVKwkQWaN8wa9W3r0Uhqvi9sl8QJcc_pX14XAFRnWsq2LqD4E0ukr2YqHsb36qcESeHH-3z9Rzk2MoRh3DIs9c4ZySpcpDhpREpKxD6vPM7MvzfaNpBRJukt7GjMyYPZjXdMhOdZU5RtGbaOH1E0tFfDi2ql96vt4XEwYCwJ2Mi2a2gxOlla5jOTKqAO6w3BENHza0Kwe0MwvZfFK5Tpb3uWbisMcqnDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392110b2f5.mp4?token=rFT8x3lhmiME-5vfNYpuEnqyZaWj0qGyuG_gMIGVjeOP0GsIqOVA30OxQ9DsE6_S8vfVG29bw5t9u9Hd2z9vVcehUt9ytD8J5Kw3YN3qvm58ELLVrnpZOhVKwkQWaN8wa9W3r0Uhqvi9sl8QJcc_pX14XAFRnWsq2LqD4E0ukr2YqHsb36qcESeHH-3z9Rzk2MoRh3DIs9c4ZySpcpDhpREpKxD6vPM7MvzfaNpBRJukt7GjMyYPZjXdMhOdZU5RtGbaOH1E0tFfDi2ql96vt4XEwYCwJ2Mi2a2gxOlla5jOTKqAO6w3BENHza0Kwe0MwvZfFK5Tpb3uWbisMcqnDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: «اگر آنها حاضر باشند مردم خودشان را قتل‌عام کنند، فکر می‌کنید با ما چه خواهند کرد؟ با اسرائیل چه خواهند کرد؟ یا با همسایگان سنی خود؟»
روبیو افزود: «همه بر این باورند که ایران نباید سلاح هسته‌ای داشته باشد. تنها چیزی که تغییر کرده این است که ما رئیس‌جمهوری داریم که حاضر است در این زمینه اقدام کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/withyashar/23867" target="_blank">📅 08:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d1e13c3.mp4?token=N8aDHJ-j1xoPPEPSXHkYWPXTHUpgp4mTkBmLDWHt08zYWvyKc0E7i61cASepPA2rvw2rgBuk9Jl1mczYasw9agdjrQCQjDR1bkgtwHwWhAnK-GsHS98p3KZHf2xsjtmQODqZPObD_ub8FFFphwSXIIvMqN4RgRnIQebY9WpSny3y5iYuTrlmrYEgkHg3tzdJ62Wx-3HqcBBEu0Clot7PnPI08VbO69uyuxypEF1dzK9VOsA1krVxQ58GBzPByTbxvYbP7mvomPx1c61q9EZHENhprRpAOqJyueFwIJD7ihgGDWxxEdwkH-jd-V2_AMU2TKEEL1j9MZIWdMJiR5DkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d1e13c3.mp4?token=N8aDHJ-j1xoPPEPSXHkYWPXTHUpgp4mTkBmLDWHt08zYWvyKc0E7i61cASepPA2rvw2rgBuk9Jl1mczYasw9agdjrQCQjDR1bkgtwHwWhAnK-GsHS98p3KZHf2xsjtmQODqZPObD_ub8FFFphwSXIIvMqN4RgRnIQebY9WpSny3y5iYuTrlmrYEgkHg3tzdJ62Wx-3HqcBBEu0Clot7PnPI08VbO69uyuxypEF1dzK9VOsA1krVxQ58GBzPByTbxvYbP7mvomPx1c61q9EZHENhprRpAOqJyueFwIJD7ihgGDWxxEdwkH-jd-V2_AMU2TKEEL1j9MZIWdMJiR5DkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: ناگهان مارکسیست‌ها و اسلام‌گراها با یکدیگر متحد و همکاری کردند و دوران افراط‌گرایی و رادیکالیسم اسلامی را به وجود آوردند.
@WarRoom</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/withyashar/23866" target="_blank">📅 08:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dbeff2ed7.mp4?token=G9_6iCNkLTSLOvgJkOQXg_QfZ0-ci63HdGYGMRMIpVH2ONs9hK6hqmS9_0A2m16T97PGR04EG6t3Mr7uQ49S9rn8uYBQWVTCGHmc7emOcQNGs-7NrU3LkxKqNEBCTM2ahF069B-BaqYoRaG2JoAYcvRMYOkP25uAuNEe_uondL_1I5GRCdu46shz55bdlejDE_VpfGYdPeCLnqmZcteCCjCF5sgK27IN5sTR3qvJG3a22lkGiFXG-G9aTmHNho_doLQCU0ZuA2ZrmBqi5LDWAASXIjCO7AGu17pLleN2oXHUJnyLFGhGX8op5PpxIU26QKmHXTXnHr858Ud-0RhHog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dbeff2ed7.mp4?token=G9_6iCNkLTSLOvgJkOQXg_QfZ0-ci63HdGYGMRMIpVH2ONs9hK6hqmS9_0A2m16T97PGR04EG6t3Mr7uQ49S9rn8uYBQWVTCGHmc7emOcQNGs-7NrU3LkxKqNEBCTM2ahF069B-BaqYoRaG2JoAYcvRMYOkP25uAuNEe_uondL_1I5GRCdu46shz55bdlejDE_VpfGYdPeCLnqmZcteCCjCF5sgK27IN5sTR3qvJG3a22lkGiFXG-G9aTmHNho_doLQCU0ZuA2ZrmBqi5LDWAASXIjCO7AGu17pLleN2oXHUJnyLFGhGX8op5PpxIU26QKmHXTXnHr858Ud-0RhHog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: پیش از انقلاب اسلامی، هر روز پروازهایی از تل‌آویو به تهران داشتیم؛ نه اینکه مانند امروز، هر روز موشک‌هایی به سمت تل‌آویو شلیک شود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/withyashar/23865" target="_blank">📅 08:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اتاق جنگ با یاشار: اجلاس کنکوردیا یک نشست غیردولتی و غیرحزبی است که هم‌زمان با هفته مجمع عمومی سازمان ملل در نیویورک برگزار می‌شود و محل حضور مقام‌های فعلی و سابق، کارشناسان و چهره‌های سیاسی و اقتصادی است. از چهره‌های مطرح حاضر می‌توان به شاهزاده رضا پهلوی ، ژنرال دیوید پترائوس، فرمانده پیشین سنتکام و رئیس پیشین سیا، نیکول پاشینیان، نخست‌وزیر ارمنستان، لیندا توماس-گرینفیلد، سفیر پیشین آمریکا در سازمان ملل، و ترزا می، نخست‌وزیر پیشین بریتانیا، اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/23864" target="_blank">📅 08:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c68d554e9.mp4?token=D245kowp9Fr7NLqwknwD71l7rlSsIkYZw6wK66KuKbKuSGMs4OcQg3UUzNuvSyZlnOCmpjGWvim-w5HetVsBnBkgAlMUyEAS-IC0Tn4Bo2vPJ9ziIQLl9K2H6wp3cVni0ql1Lorg8TFEgfUdXmZk2JLfhwsYIjRlGMOrkq47Zr8LvuAyna8He0_mf0pr9c93waAh7M9-VTwuN1-cq8u9hF5fM7MYTgzNQPqiTKsxZrwZKcYhq7JRyOmmY5cBtPQMw5IJ6Etj25Y-HCRjxZwtbQwrfYq1-XWwKwLKVPd27GWO0cEXQSCnoJcSbAwgjjPfvU87jT8o2w9sSmdNCWa5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c68d554e9.mp4?token=D245kowp9Fr7NLqwknwD71l7rlSsIkYZw6wK66KuKbKuSGMs4OcQg3UUzNuvSyZlnOCmpjGWvim-w5HetVsBnBkgAlMUyEAS-IC0Tn4Bo2vPJ9ziIQLl9K2H6wp3cVni0ql1Lorg8TFEgfUdXmZk2JLfhwsYIjRlGMOrkq47Zr8LvuAyna8He0_mf0pr9c93waAh7M9-VTwuN1-cq8u9hF5fM7MYTgzNQPqiTKsxZrwZKcYhq7JRyOmmY5cBtPQMw5IJ6Etj25Y-HCRjxZwtbQwrfYq1-XWwKwLKVPd27GWO0cEXQSCnoJcSbAwgjjPfvU87jT8o2w9sSmdNCWa5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود؛ امروز تولید ناخالص داخلی کره جنوبی پنج برابر ایران است. وضعیت اقتصاد ایران قابل دوام نیست؛ پایدار نیست و در نهایت منفجر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/withyashar/23863" target="_blank">📅 08:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c403db85.mp4?token=ht-B1u3qORy9pquFU_p5qtUvtBhAYgTjOJOvAzDU6ky-v-fWtfmZ_cZZlt7VRCJfIxKzM8WtbbPg2Tuwtrt473GAUyvFSlopBotaQQzZ8RqQ-G_Dc9ufPf57xXi6-qok-5guyUzcFlqYexZ2Mt79JTxtQvQfAsU6BCzPF9h5IXNXolSxtp39JG7mXDm2uMpC2LsgAfcRUsDClCvr3pr-8vUmQa3rUGtPmpaNoWUQwAtOrEtFxhMm4bdRe4SGiygocoF1FC8h3XNVOvobdTThqaV6e9uNVBeMnNLw5XqmlUEyXG_NLPfOyLmVjF2Npk9RtTK3FOwZ5bxMjmYZDeEZig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c403db85.mp4?token=ht-B1u3qORy9pquFU_p5qtUvtBhAYgTjOJOvAzDU6ky-v-fWtfmZ_cZZlt7VRCJfIxKzM8WtbbPg2Tuwtrt473GAUyvFSlopBotaQQzZ8RqQ-G_Dc9ufPf57xXi6-qok-5guyUzcFlqYexZ2Mt79JTxtQvQfAsU6BCzPF9h5IXNXolSxtp39JG7mXDm2uMpC2LsgAfcRUsDClCvr3pr-8vUmQa3rUGtPmpaNoWUQwAtOrEtFxhMm4bdRe4SGiygocoF1FC8h3XNVOvobdTThqaV6e9uNVBeMnNLw5XqmlUEyXG_NLPfOyLmVjF2Npk9RtTK3FOwZ5bxMjmYZDeEZig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که پروازهای شرکت‌های هواپیمایی ایران در پی «عملیات طرد اقتصادی» در چندین کشور لغو شده‌اند، پزشکیان، رئیس‌جمهور رژیم ایران، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شده و به‌سرعت به حومه شهر منتقل شده است.
سخنرانی او امروز حدود ساعت ۳-۴ به وقت تهران است
@WarRoom</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/23862" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش‌ صدای انفجار‌ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23861" target="_blank">📅 01:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش‌صدای انفجار در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23860" target="_blank">📅 01:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیوی نیویورک فاکس نیوز:
میلیون‌ها ایرانی در ۳۱ استان، در پاسخ به فراخوان من، به خیابان‌ها آمدند و در حمایت از پایان این رژیم شعار دادند.
آنها از اقوام، ادیان و اقشار مختلف جامعه ایران بودند و این نشان‌دهنده وحدت در عین تنوع است. پهلوی گفت
این رژیم عامل ایجاد اختلاف و تفرقه در ایران است
و ایرانیان قرن‌ها فارغ از قومیت و مذهب در کنار یکدیگر در صلح زندگی کرده‌اند و پس از آزادی نیز می‌توانند دوباره متحد شوند. او در پایان گفت:
«انقلاب شیر و خورشید در راه است.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23859" target="_blank">📅 01:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پرتاب موشک از بندر کنگ
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23858" target="_blank">📅 00:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل در واکنش به اظهارات امانوئل مکرون اعلام کرد: «پوچی و تناقض فاحش اظهارات امانوئل مکرون تکان‌دهنده است. تنها دو روز پیش، در آستانه یوم‌کیپور، نتانل شوکرون،
شهروند فرانسوی و پدر شش فرزند
، در خودروی خود در یهودیه و سامریه توسط یک تروریست حماس کشته شد. او در آخرین لحظات زندگی‌اش به پسرش گفت فرار کند. تروریست‌های حماس تقریباً هر روز علیه یهودیان حمله انجام می‌دهند و شمار زیادی از غیرنظامیان اسرائیلی را در یهودیه و سامریه کشته‌اند. ناآگاهی،
هیچ عذری برای نادیده گرفتن خون قربانیان نیست.
»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23857" target="_blank">📅 00:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تتر و دلار دارن میکشن پایین
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23856" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک‌پست:
جمهوری اسلامی ایران در چارچوب یک طرح وابسته به سپاه،
حداقل سن جذب نیرو را به ۱۲ سال کاهش داده است
. یک مقام سپاه در تهران اعلام کرده بود نوجوانان ۱۲ و ۱۳ ساله می‌توانند برای حضور در گشت‌های اطلاعاتی و عملیاتی ثبت‌نام کنند. گزارش‌های بی‌بی‌سی و عفو بین‌الملل نیز از حضور کودکان در ایست‌های بازرسی و مواردی از حمل سلاح توسط آنها خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23855" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
ما به دنبال تغییر رژیم یا جایگزین کردن حکومت ایران نیستیم؛ هدف آمریکا این است که
ایران به سلاح هسته‌ای دست پیدا نکند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23854" target="_blank">📅 00:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فاکس‌نیوز:
دونالد ترامپ اخیراً با امضای حکمی،
مارکو روبیو، وزیر خارجه آمریکا، را به‌طور رسمی و دائمی به‌عنوان مشاور امنیت ملی کاخ سفید منصوب کرد.
روبیو از مه ۲۰۲۵ پس از برکناری مایکل والتز، به‌صورت موقت این سمت را بر عهده داشت و اکنون انتصاب او دائمی شده است. روبیو همچنان وزیر خارجه آمریکا نیز خواهد بود و همزمان مدیریت روند شورای امنیت ملی و نقش مشاور مستقیم رئیس‌جمهور در مسائل امنیتی را بر عهده خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23853" target="_blank">📅 23:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری i24news : ‏اکسپلور گردی« احمد الشرع » وسط سخنرانی اردوغان در سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23852" target="_blank">📅 23:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dcb0a852.mp4?token=OpA75CY7fqIeaA-n6fE5IvmRR2PJafKbNc7cw9rblY3ASSPS4XosO8tR53BUU1zFW5O7xlaMq3xGmNcPRbCDP2AWW9W80doF5DG7_U_k3GHLnHt86znii1UTFJLyg1gF11DFHpsHx-ARDc5RSSKzPKsyygus83PIX8XfxCN7iaxz8j0A46F3qrJIvKFE_0LvB2pMq7D1zj_vlgeDhyasroFYIoEHtXQOylUVCM-KCqFbiYeiTMC4MPCJ9pmKPef_Q4L78GSsf6w-d_N870TP6z2X1HWJ7QQj93Pqqy5thb6p7rL_yJhQeblntCNDIaQuEvwgyd3i6k-iM-RPm6ZSsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dcb0a852.mp4?token=OpA75CY7fqIeaA-n6fE5IvmRR2PJafKbNc7cw9rblY3ASSPS4XosO8tR53BUU1zFW5O7xlaMq3xGmNcPRbCDP2AWW9W80doF5DG7_U_k3GHLnHt86znii1UTFJLyg1gF11DFHpsHx-ARDc5RSSKzPKsyygus83PIX8XfxCN7iaxz8j0A46F3qrJIvKFE_0LvB2pMq7D1zj_vlgeDhyasroFYIoEHtXQOylUVCM-KCqFbiYeiTMC4MPCJ9pmKPef_Q4L78GSsf6w-d_N870TP6z2X1HWJ7QQj93Pqqy5thb6p7rL_yJhQeblntCNDIaQuEvwgyd3i6k-iM-RPm6ZSsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز: «ما هر شب ۲۵ تا ۳۰ کشتی را از بین می‌بریم؛ گاهی هم در طول روز، اما بخش زیادی از آن در شب انجام می‌شود. این محاصره قوی‌ترین چیزی است که تاکنون دیده شده و ما آن را «دیوار فولادی» می‌نامیم. اکنون نسبت به هر زمان دیگری از آغاز درگیری، نفت بسیار بیشتری از طریق تنگه هرمز عبور می‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23850" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb899a45a.mp4?token=WDZext_VAxsGP43ms1YbLYgrk28r6eacA4xt4S3dwurUgn7Jj1POvTZ11GQooE7fYzvHdeXc-Tf6wHFN21j8DGTJDP6QNA3VmrsAPWLKPa6q1Ksjpql5zcIxzbhE9FPMrT8atNPhc3xOCpU-NCOXo4pKZ7PWFcSR8xAGcBaRrbKwarKC9NXjuXBV8IVTEx14-qv1zhlAorqrA6eOdsmqkH54dF_LYDuH7Yhkf6yF_dtx6bl0KFndqVAIYWX0G_GLnnWLGTAqAJYttaQbclymTzO72Z8HMrar34jj8bHlAvhAPXmZ_Bkcol9qD3WdtBhVkaBtiMXLRz6mc39sawv9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb899a45a.mp4?token=WDZext_VAxsGP43ms1YbLYgrk28r6eacA4xt4S3dwurUgn7Jj1POvTZ11GQooE7fYzvHdeXc-Tf6wHFN21j8DGTJDP6QNA3VmrsAPWLKPa6q1Ksjpql5zcIxzbhE9FPMrT8atNPhc3xOCpU-NCOXo4pKZ7PWFcSR8xAGcBaRrbKwarKC9NXjuXBV8IVTEx14-qv1zhlAorqrA6eOdsmqkH54dF_LYDuH7Yhkf6yF_dtx6bl0KFndqVAIYWX0G_GLnnWLGTAqAJYttaQbclymTzO72Z8HMrar34jj8bHlAvhAPXmZ_Bkcol9qD3WdtBhVkaBtiMXLRz6mc39sawv9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بخش بزرگی از اقداماتی که انجام داده‌ایم — شاید ۹۹ درصد آن — برای اطمینان از این بوده است که ایران به سلاح هسته‌ای دست پیدا نکند. آن تأسیسات منهدم شده‌اند. ممکن است مجبور شویم تأسیسات دیگری را هم منهدم کنیم: «کوه کلن گزلا» (Pickaxe Mountain). در حال حاضر فعالیت زیادی در آنجا مشاهده نمی‌کنیم، اما اگر شاهد فعالیتی باشیم، بلافاصله آن را منهدم خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23849" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37263286bc.mp4?token=WQW20szFs5nMGu7XYEL23wPevBe8Mzdnt-4ptWPvMhwAjpbCbqIfsFtEkcnJ-m8Td9EempMD-MvdYSsD7k2CcIZLkETF_G81pDUZ4sEIhIad98J4tIjooAE7BlWy8vNNe6tm9KcAKX4X2F6q108fSeCd-wIjLX44dyAXaGNkBjdQeRZR-mzR6uDrHSDhydjVvNybje3RyLMwEBeqG55FGDAXpPk9UNfzzsG9cm_Gnucp3oGuaKPQfzB3E8PiQBJI2ZcsbjYWgNFYVcBQnkOIYV6VX66vOhBI9aMxIULmPEYWtLviJc4X-PbNx6A19aS6EI3NRdlzrh2cvc-cOeDzmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37263286bc.mp4?token=WQW20szFs5nMGu7XYEL23wPevBe8Mzdnt-4ptWPvMhwAjpbCbqIfsFtEkcnJ-m8Td9EempMD-MvdYSsD7k2CcIZLkETF_G81pDUZ4sEIhIad98J4tIjooAE7BlWy8vNNe6tm9KcAKX4X2F6q108fSeCd-wIjLX44dyAXaGNkBjdQeRZR-mzR6uDrHSDhydjVvNybje3RyLMwEBeqG55FGDAXpPk9UNfzzsG9cm_Gnucp3oGuaKPQfzB3E8PiQBJI2ZcsbjYWgNFYVcBQnkOIYV6VX66vOhBI9aMxIULmPEYWtLviJc4X-PbNx6A19aS6EI3NRdlzrh2cvc-cOeDzmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23848" target="_blank">📅 23:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/540fba7a3f.mp4?token=DMHTWZdwNhni0bHuWPPCk8A87YC7EX80UHMSm0ALrKOyfjHJoW9ya18rwGJZhkVP9amVZz9kxC6EfKC_F_IMkOInhw-IxNKQRSY5AZ45IWBZ4Mspl5vC8g5_AQmp6ebGdeC8QUYLd83VkxX6bHO_ANcGgGxCiBSRIX1ClxRqVVfNPpsnc86KxC4e3QYcw6Ta3-0c1G-0tBTab3g_RyNbHqYeW0QweCG858UkISHj5nZ_bJtnExtqpeiHBNdM7yjMSave2eeZSH6droH9Dy4wDbr5jB5EjLNllfcl7s1dLmH1vzjkvEXnkyN6ox2MvdiAkopyEHU8CJZ0A4iR5HJEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/540fba7a3f.mp4?token=DMHTWZdwNhni0bHuWPPCk8A87YC7EX80UHMSm0ALrKOyfjHJoW9ya18rwGJZhkVP9amVZz9kxC6EfKC_F_IMkOInhw-IxNKQRSY5AZ45IWBZ4Mspl5vC8g5_AQmp6ebGdeC8QUYLd83VkxX6bHO_ANcGgGxCiBSRIX1ClxRqVVfNPpsnc86KxC4e3QYcw6Ta3-0c1G-0tBTab3g_RyNbHqYeW0QweCG858UkISHj5nZ_bJtnExtqpeiHBNdM7yjMSave2eeZSH6droH9Dy4wDbr5jB5EjLNllfcl7s1dLmH1vzjkvEXnkyN6ox2MvdiAkopyEHU8CJZ0A4iR5HJEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما فشار ‌زیادی ‌رویشان قرار‌دادیم ،امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند. می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23847" target="_blank">📅 23:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23846">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a4e00219.mp4?token=r5Bql0JQEnhjHopWgikRcWxWMNBSxEcV1QFavxawQrUd2JXdHzqZ62NaLiPrICrsfo3O7ZZCidZ9pRS4BcUFdDMGRsG8cpR7qGwCGGzdbD_3KqDRCJ3bKRWiKoXfePEePu6swATDskW_IyfbUKhs98b36R_rhorc_dp3S5oFuHe-9H_2onjaoNzfOJcgyB-A0-hLywjVcK00NPJLBCcJZ7bbyYUpSYxunfftzMsW8zlFzXfKn-R3rqEctjlMP839wdjfgyBbjdxksfZ-_0YH2VUEcMIRRtU-tK3Dx569iBJLY6s9er7yrr-2Kvt-Pch322_Qu9bcCYjsQR92aI6krQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a4e00219.mp4?token=r5Bql0JQEnhjHopWgikRcWxWMNBSxEcV1QFavxawQrUd2JXdHzqZ62NaLiPrICrsfo3O7ZZCidZ9pRS4BcUFdDMGRsG8cpR7qGwCGGzdbD_3KqDRCJ3bKRWiKoXfePEePu6swATDskW_IyfbUKhs98b36R_rhorc_dp3S5oFuHe-9H_2onjaoNzfOJcgyB-A0-hLywjVcK00NPJLBCcJZ7bbyYUpSYxunfftzMsW8zlFzXfKn-R3rqEctjlMP839wdjfgyBbjdxksfZ-_0YH2VUEcMIRRtU-tK3Dx569iBJLY6s9er7yrr-2Kvt-Pch322_Qu9bcCYjsQR92aI6krQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: استیو و جارِد امروز جلسه‌ای بسیار سازنده با دو میانجی از ایران داشتند. خواهیم دید که نتیجه این جلسه چه خواهد بود.
به نظر من، یک حرکت قوی برای رسیدن به توافق وجود دارد. این چیزی است که ما از همه می‌شنویم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23846" target="_blank">📅 23:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسرائیل هیوم به نقل از منابع آمریکایی:
یک دیدار از پیش برنامه‌ریزی‌شده میان مقام‌های آمریکایی و هیئت ایرانی به ریاست عباس عراقچی، با حضور نخست‌وزیر قطر، برگزار شد و در آن درباره ازسرگیری مذاکرات میان تهران و واشنگتن و همچنین بازگشایی تنگه هرمز گفت‌وگو شد. با این حال، طرفین درباره مسائل مورد اختلاف به توافقی دست پیدا نکردند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23845" target="_blank">📅 22:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بلومبرگ به نقل از مقام‌های آمریکایی و افراد مطلع گزارش داد آمریکا هوش مصنوعی خود را تغییر داد چون حمله مرگبار به مدرسه میناب نتیجه مجموعه‌ای از خطاهای اطلاعاتی و هدف‌گیری بوده است. بر اساس این گزارش، اطلاعات قدیمی ارتش آمریکا همچنان مدرسه را به‌عنوان یک تأسیسات سپاه ثبت کرده بود، در حالی که تصاویر ماهواره‌ای نشان می‌داد این محل سال‌ها قبل به مدرسه تبدیل شده است. همچنین فشار زمانی برای تعیین بیش از هزار هدف و اتکای برخی نیروهای سنتکام به سامانه هوش مصنوعی «Maven» در روند هدف‌گیری نقش داشت. پس از این حمله، قابلیت‌های جدیدی به Maven اضافه شد تا اطلاعات اهداف، تناقض‌ها و عواملی را که می‌توانند باعث خروج یک هدف از فهرست حمله شوند، دوباره بررسی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23844" target="_blank">📅 22:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">توییت جدید
https://x.com/yasharrapfa</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23843" target="_blank">📅 22:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23842">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آکسیوس:
کشورهای عربی در نیویورک تلاش می‌کنند
دیدار مستقیم ترامپ و مسعود پزشکیان
را در حاشیه مجمع عمومی ترتیب دهند
@WarRolm</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23842" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سازمان هواپیمایی کشوری ایران: از نیمه شب امشب، فرودگاه‌های بغداد و مسقط، پروازهای هواپیمایی ایران را پذیرش نخواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23841" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی سپاه:درحال آماده سازی برای سناریوی حمله پیش‌دستانه به پایگاه های آمریکا در منطقه هستیم،در صورتی که حمله ای از سوی آمریکا به ایران محرز شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23840" target="_blank">📅 22:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویتکاف: دیدار با ایرانی‌ها خوب پیش رفت و در حال حاضر احساس بسیار خوبی دارم
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23839" target="_blank">📅 22:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار i24: استیو ویتکاف و جرد کوشنر، مقام‌های آمریکایی بودند که امروز با هیئت ایرانی دیدار کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23838" target="_blank">📅 22:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">بازنشری دوباره از صحبت های بسیار مهم از صحبت های مانوک درباره مذاکره و آینده ایران
مجری  :  آیا به توافقی میرسند؟
آیا مذاکره می‌کنند؟ یا ایران رد خواهد کرد؟
مانوک خدابخشیان : ایران رد نخواهد کرد، اگر بپذیرند خلع سلاح کامل می‌شوند، و مجبور به پذیرش بقیه شرط ها حقوق بشر دیگر برگ کوبنده ای نیست زیرا صدها برگ دیگر وجود دارد
مجری: ترامپ میگه پیشرفت زیادی در ارتباط با ایران به دست آمده! از این پیشرفت منظورش چیه؟
مانوک خدابخشیان : دونالد زبل بزرگترین خواسته اش اینه با یکی از این ها سلفی بگیره! ایمان داشته باشید«اینها با یک جماعتی در تهران ساخت و پاخت کردن!»نه این که رژیم بمونه!
یادتون نره!
همه ترسشون اینه امروز آمدن مذاکره کردن کار تموم شد ، استمرار پیدا کرد این رژیم ،نه اینچنین نیست.
«این تحلیل های آبکی رو بعد بذارید و بعد بگید »
آمریکا جایی که رفت مذاکره کنه مذاکره نمیکنه ، باز تکرار میکنم « حکم میکنه »
ببینید آیا رژیم جمهوری اسلامی حاضره مثل صدام حسین تحقیر بشه ؟ اینا به نوکر صدام گفتن برید بهش بگید تمام سلاح های اتمی و شیمیایش بده به ما و بعدش میشینیم مذاکره میکنیم و دیدید صدام حسین تو سری رو خورد چرا ؟ چون «بازی تموم شده رژیم کارش تمومه »
اگر یک آلترناتیو الان بود و اطمینان خاطر داشتن اینها در ایران بحران به وجود نمیاد قطعا عمل میکردن و الانم قول هایی گرفتن!
دلیل خوشحالی ترامپ هم همینه
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23837" target="_blank">📅 22:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">@WarRoom
Selfie</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23836" target="_blank">📅 21:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=ARajJ3D2lyH4QR3j8bscXD_MMqYxAYamQcIEwuUVHi1FdRFfOoZhXEw4waHL7Jia_sCkCGVlpc6sQwUzlVbq9pfpRWCb-WyxEv_6u4_J9_8H-CPuDhLFKxf6uwLZrhJcHdp2bho437FTbMCXeJX0sPFYMXp2j8fKeoHQSy8M2wptOqFZAJSdFqLc-OosOwfiv1CtRpHkna1_M-yWW0io1c_Ma7icVF2rPcJEiy6qqc5e-5gf9M77_6ezsFeN2LOgetOCGBiXkrTfk5Xmil1j0z6Np1CPsN79ONtbrF-V-vlMvrLVgqDQGumyto31ZRCp8L66kyRuryj0efq4gm2CQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=ARajJ3D2lyH4QR3j8bscXD_MMqYxAYamQcIEwuUVHi1FdRFfOoZhXEw4waHL7Jia_sCkCGVlpc6sQwUzlVbq9pfpRWCb-WyxEv_6u4_J9_8H-CPuDhLFKxf6uwLZrhJcHdp2bho437FTbMCXeJX0sPFYMXp2j8fKeoHQSy8M2wptOqFZAJSdFqLc-OosOwfiv1CtRpHkna1_M-yWW0io1c_Ma7icVF2rPcJEiy6qqc5e-5gf9M77_6ezsFeN2LOgetOCGBiXkrTfk5Xmil1j0z6Np1CPsN79ONtbrF-V-vlMvrLVgqDQGumyto31ZRCp8L66kyRuryj0efq4gm2CQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23835" target="_blank">📅 21:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23834" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23833" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecad76c05b.mp4?token=uY4movCpo0JC9SHkVhSqVGbzooeeDsOTyY7W2oZ5Id8W_og4SKy2aon5iefHnX5nRyGHyb0f1dff8RABgeKa80Er62ATaKActQKK9RxKV54XqU8bDLx0EQ4fvnUNX2hv_6C0MCgoBkhmC3_qMkCA38R_bu7TK3Jjpu5G-jc-QAhulIQh-JIbFixMSelBh6tSqTP07G_EdbFtrfQaxknKaVr7WJVkqDQKvvkz5hK2uGOEAyYRr5s4MPopTpTyBUjITWw8Him7_hsNl-5qn9Z7zkDZLA3OL50BUHuQJ8IV1UuFCAK1eJy167seYG9l1WjjRkdZaig4aDp7e2ghdNhC-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecad76c05b.mp4?token=uY4movCpo0JC9SHkVhSqVGbzooeeDsOTyY7W2oZ5Id8W_og4SKy2aon5iefHnX5nRyGHyb0f1dff8RABgeKa80Er62ATaKActQKK9RxKV54XqU8bDLx0EQ4fvnUNX2hv_6C0MCgoBkhmC3_qMkCA38R_bu7TK3Jjpu5G-jc-QAhulIQh-JIbFixMSelBh6tSqTP07G_EdbFtrfQaxknKaVr7WJVkqDQKvvkz5hK2uGOEAyYRr5s4MPopTpTyBUjITWw8Him7_hsNl-5qn9Z7zkDZLA3OL50BUHuQJ8IV1UuFCAK1eJy167seYG9l1WjjRkdZaig4aDp7e2ghdNhC-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
امروز، یک ساعت پیش گفتگویی با مقامات ایرانی انجام شد. آن بسیار خوب بود. یک ساعت پیش به پایان رسید.
این یک جلسه‌ای بود که سه ساعت طول کشید.
این یک عظمت، عظمت بالقوه، یا نابودی است.
در یک حالت، نابودی است. و گزینه دیگر، عظمت بالقوه است. می‌تواند کشوری بزرگ باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23832" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خیرگزاری جِی‌فید اسرائیل :
۱۲ فروند جنگنده
F-16C
متعلق به گارد ملی هوایی اوکلاهما از پایگاه اسپانگدالم در آلمان به سمت منطقه عملیاتی
سنتکام در خاورمیانه
حرکت کردند. این جنگنده‌ها که از حدود یک هفته قبل در آلمان مستقر شده بودند، در سه گروه چهار فروندی پرواز کرده و با همراهی
سه فروند سوخت‌رسان KC-135R
به سمت خلیج فارس حرکت کردند. این جابه‌جایی در حالی انجام می‌شود که حضور هوایی آمریکا در منطقه همچنان در حال تقویت است. همزمان، امروز یک فروند
F-16 متعلق به بال ۵۲ جنگنده آمریکا
در نزدیکی پایگاه اسپانگدالم سقوط کرد؛ خلبان با موفقیت ایجکت کرد اما زخمی شد و برای درمان به بیمارستان منتقل شد. علت سقوط در دست بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23830" target="_blank">📅 21:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23829" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نکات مهم و جدید صحبتهای تکراری ترامپ در مجمع عمومی سازمان ملل  : بخش عمده صحبت‌هایش را به
ایران و جنگ
اختصاص داد و گفت اگر تهران به توافق نرسد، آمریکا می‌تواند جمهوری اسلامی را
«نابود کند»
؛ در عین حال تأکید کرد مسیر مذاکره همچنان باز است و ایران باید تنگه هرمز را بازگشایی کند. او از کشورها خواست به
انزوای اقتصادی ایران
بپیوندند. درباره
کوبا
گفت حکومت کمونیستی این کشور شکست‌خورده است و
«آزادی به کوبا خواهد آمد»
. درباره
غزه
از طرح صلح خود و پایان جنگ گفت و درباره
اوکراین
خواستار پایان جنگ روسیه و اوکراین شد. ترامپ درباره
گرینلند
بر گسترش حضور نظامی آمریکا تأکید کرد، از سیاست آمریکا در
ونزوئلا و مقابله با کارتل‌های مواد مخدر
دفاع کرد و به‌شدت از
سازمان ملل و دادگاه کیفری بین‌المللی
انتقاد کرد. او همچنین درباره
هوش مصنوعی
با محدودیت‌های بین‌المللی مخالفت کرد و گفت آمریکا باید در رقابت برای دستیابی به
ابرهوش
پیشتاز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23828" target="_blank">📅 21:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امروز ۳۱ آغاز جنگ ایران و عراق و آغاز هفته دفاع مقدس است. ممکن است صداها برای این هم باشد, همچنین گزارشاتی الان به دستم رسیده که در پارک شمیم تبریز رزمایش است
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23827" target="_blank">📅 21:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تبریز صدای انفجار وحشتناکککک @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23826" target="_blank">📅 21:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تبریز صدای انفجار وحشتناکککک
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23825" target="_blank">📅 21:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رویترز:
عربستان عملیات خط لوله شرق-غرب خود را از سر گرفته؛ این تحول نگرانی درباره اختلال در صادرات نفت منطقه را تا حدی کاهش داده است
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23824" target="_blank">📅 21:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز:
ترامپ‌ در ‌سازمان ملل از کشورهای جهان خواست برای اعمال
انزوای اقتصادی کامل ایران
همکاری کنند و گفت تهران باید تنگه هرمز را کاملاً باز کند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23823" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qme1cai9OLz92nbRI5J0cF2L53xCWhlzdMaDSbmpMFztYMuQUpkPd4SI6X4xkg4SwMOletzSoiZu7UIg38RzMwM8-schKQNBIs2x70oyhJPK_5xUftP62qAp6yWIgo-HR_T6M2E1SBbUXk_9jRnYGFgOVXccFOZoV2jcLESXc9KcP9Ja5jAFSsk1Nz4jRopFODO3XlV1d445wvF90JxjNU5o3XSoojEHZ5UemgSY2cwOsJ3pUwsCXPHKuyz3yZTld3gx-l-yblhR2t9OcnOOYL9uicA1nEmjp8mpOFL20k7JwLKUqF2_d7dOZfXkdC4EO_Yd1YLDnHQTJGhJwPFswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه عالی پودگوریتسا با استرداد امیر براتی، شهروند ایرانی-ترکیه‌ای، به آمریکا موافقت کرد.
مقام‌های مونته‌نگرو او را مرتبط با سپاه پاسداران معرفی کرده‌اند و آمریکا متهمش کرده است که از سال ۲۰۱۳ در حملات سایبری علیه بیش از
۱۵۰ دانشگاه و مؤسسه آمریکایی
مشارکت داشته و این حملات بیش از
۳.۴ میلیارد دلار خسارت
به بار آورده است. براتی در ۲۵ ژوئن در شهر کوتور مونته‌نگرو، به درخواست آمریکا بازداشت شد. او در دنیای هکری با نام
«کینگ‌لِت»
شناخته می‌شد و بعدها با نهادهای اطلاعاتی ایران همکاری داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23822" target="_blank">📅 20:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ درباره ایران: «فکر می‌کنم توافقی حاصل خواهد شد. آن‌ها حتی امروز هم با ما در حال گفت‌وگو بوده‌اند , بگذارید بگوییم که این رابطه در حال شکل‌گیری و پیشرفت است.»
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23821" target="_blank">📅 20:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315709f99a.mp4?token=hAzcNG9kCNoUebqcNcTbuThuFKq9c9PGYoaZdrBqvVZbuEXk3alyC2p7ZrweIbi5slAeq6LmIXwwP850sxT68kjKVUqg25KTmHQtdIxQcxS0IwVnr-gppEFV_GNeAgWbVNCOwa3gy3O5aWXORUqIfUOHh-tzSUX-i9mIL2M08ktg_GAuqTvj07D2BGSM--Uu3O8RWwwMp38ePgcVu62g5T8UbC8lIpxDCb5yVrefIZs9KjB7ra7EvDeDQU7EgpRzcBe5OQ41_zPmqULuEm0Gy755bMiryNJBCKzOvYNV84dk1Zubvieg_yfL4CLS-6BmxR_5MEtuaVTFFwrUyyOv_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315709f99a.mp4?token=hAzcNG9kCNoUebqcNcTbuThuFKq9c9PGYoaZdrBqvVZbuEXk3alyC2p7ZrweIbi5slAeq6LmIXwwP850sxT68kjKVUqg25KTmHQtdIxQcxS0IwVnr-gppEFV_GNeAgWbVNCOwa3gy3O5aWXORUqIfUOHh-tzSUX-i9mIL2M08ktg_GAuqTvj07D2BGSM--Uu3O8RWwwMp38ePgcVu62g5T8UbC8lIpxDCb5yVrefIZs9KjB7ra7EvDeDQU7EgpRzcBe5OQ41_zPmqULuEm0Gy755bMiryNJBCKzOvYNV84dk1Zubvieg_yfL4CLS-6BmxR_5MEtuaVTFFwrUyyOv_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا، جی‌دی ونس:
«رأی‌دهندگان بیشتر روی
مسائل داخلی و محلی که برایشان اهمیت دارد
تمرکز کرده‌اند و نه جنگ با ایران.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23820" target="_blank">📅 19:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815a7ec77d.mp4?token=J3eLkgsYpV1uu1rz_K56x08DFEjNxEai0IbLFKNlSQO8kdBSOeE8TYQccp_OkcouO-CA8een_n28Ofmka-Nb9syJW6moqZmRBUqL1aV957WTeQcwWhDrzwT29N1anqJUlZvAVNobWwfkKHKZo0V4bFj5nsNF01GTdMoNDTDafmiOmhuDJgzH277KZKFVr_x1ajXImPNsOABgCJw1grFRDpekEAgGAJo7gJBBIlNYEy1uPFXxWjXziuKKuefZbWcSMIRoELtwHwSp8jpu8m580HaQaiAOa0A3TEPUUpBQze_yKwMKge-M9YIZ69zcX3vxbS5EHzBb2aW8dbD6OLF5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815a7ec77d.mp4?token=J3eLkgsYpV1uu1rz_K56x08DFEjNxEai0IbLFKNlSQO8kdBSOeE8TYQccp_OkcouO-CA8een_n28Ofmka-Nb9syJW6moqZmRBUqL1aV957WTeQcwWhDrzwT29N1anqJUlZvAVNobWwfkKHKZo0V4bFj5nsNF01GTdMoNDTDafmiOmhuDJgzH277KZKFVr_x1ajXImPNsOABgCJw1grFRDpekEAgGAJo7gJBBIlNYEy1uPFXxWjXziuKKuefZbWcSMIRoELtwHwSp8jpu8m580HaQaiAOa0A3TEPUUpBQze_yKwMKge-M9YIZ69zcX3vxbS5EHzBb2aW8dbD6OLF5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی هنگام سخنرانی رجب طیب اردوغان، رئیس‌جمهور ترکیه، در مجمع عمومی سازمان ملل، سالن را ترک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23819" target="_blank">📅 19:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس:
قرار است تا ساعاتی دیگر در نیویورک،
دونالد ترامپ با رهبران کشورهای عربی خلیج فارس
دیداری مهم داشته باشد و درباره
ادامه جنگ با ایران
گفت‌وگو کند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23818" target="_blank">📅 19:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فرانس‌پرس:
امانوئل مکرون در دیدار با ترامپ چند طرح برای کاهش بحران انرژی پیشنهاد کرده که یکی از آنها تلاش در سازمان ملل برای
باز کردن تنگه هرمز
است. مکرون همچنین پیشنهاد حفاظت از تأسیسات نفتی عربستان در برابر حملات حوثی‌ها را مطرح کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23817" target="_blank">📅 19:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آسوشیتدپرس:
دونالد ترامپ امروز در سخنرانی خود در مجمع عمومی سازمان ملل از تصمیمش برای آغاز جنگ با ایران دفاع کرد و گفت آمریکا در حال «تسویه حساب با مسائل حل‌نشده» است. ترامپ تأکید کرد ایران نباید به سلاح هسته‌ای دست پیدا کند و گفت آمریکا برای پایان جنگ آماده گفت‌وگو است. هیئت ایرانی در جریان سخنرانی ترامپ از سالن خارج شد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23816" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ:
«کارتل‌ها، داعشِ نیمکره غربی هستند؛ افراد خوبی نیستند. همانند داعش، باید
کشته، تبعید یا به‌عنوان نیروهای دشمن بازداشت شوند، بدون امکان آزادی
؛ و ما همین کار را انجام می‌دهیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23815" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce094c02c0.mp4?token=tnmX9MyJRQ_BkzLMsPxfuw8iMd7Qu6roBPkwQeRxL0KDkehuf9L5sIBmDMRqgzDoo6yhc9wqO6bzuHskiKCx-lhudiAJrfACUFzuvWdglas7VrUVRbNdLiiVJqq1mJNL5iFakTGFSMI9GLDAfBBGF5Znse5UScWo_0od9d0BgsfS17zV_4E9Aa5WlWMw29nKDD_Rr8SOVfYnBYcN-qP_rdZ7rgsnhmDdTtJKHEJvrHeN0AbMawPglQAP-OB_dVN1qGgFrQU3boQl73TvaIEpQS11OWuAzqWlK7ZUoyZ2zHpehj1pbAJtyYqsfTS2mnlgJDIdTLQLz1acSyepB3lE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce094c02c0.mp4?token=tnmX9MyJRQ_BkzLMsPxfuw8iMd7Qu6roBPkwQeRxL0KDkehuf9L5sIBmDMRqgzDoo6yhc9wqO6bzuHskiKCx-lhudiAJrfACUFzuvWdglas7VrUVRbNdLiiVJqq1mJNL5iFakTGFSMI9GLDAfBBGF5Znse5UScWo_0od9d0BgsfS17zV_4E9Aa5WlWMw29nKDD_Rr8SOVfYnBYcN-qP_rdZ7rgsnhmDdTtJKHEJvrHeN0AbMawPglQAP-OB_dVN1qGgFrQU3boQl73TvaIEpQS11OWuAzqWlK7ZUoyZ2zHpehj1pbAJtyYqsfTS2mnlgJDIdTLQLz1acSyepB3lE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
دونالد ترامپ درباره ایران گفت: «آمریکا و ایران قطعاً این مسئله را حل خواهند کرد؛ به هر طریقی که باشد، این کار انجام خواهد شد.»
او افزود: «این اتفاق سریع رخ خواهد داد.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23814" target="_blank">📅 18:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: جنگ اوکراین زودتر از آنچه مردم تصور می‌کنند پایان خواهد یافت
دونالد ترامپ درباره جنگ اوکراین گفت: «ما همکاری بسیار نزدیکی با رهبران روسیه و اوکراین داریم و این مسئله را حل خواهیم کرد.»
او افزود: «فکر می‌کنم این اتفاق سریع‌تر از آنچه مردم تصور می‌کنند رخ خواهد داد؛ آن‌ها دیگر از این جنگ خسته شده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23813" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ: بزدلان و خائنان دوست دارند بگویند ایالات متحده با کمبود مهمات مواجه است، اما چنین چیزی درست نیست.
ما بیش از آن مقدار مهماتی داریم که حتی بتوانیم تصور کنیم ممکن است از آن استفاده کنیم و در حال تولید مهمات با سطوحی هستیم که هرگز پیش از این تجربه نکرده‌ایم. ما ذخایر خود را سریع‌تر از هر زمان دیگری افزایش می‌دهیم؛ مهمات و تجهیزات درجه‌یک.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. در حال حاضر ۱۸ کارخانه توسط بزرگ‌ترین شرکت‌های صنایع دفاعی جهان در حال ساخت است؛ ۱۸ کارخانه در دست احداث است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23812" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است @WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/23811" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23810">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc729c6f5e.mp4?token=Ca_upG2AZrh3hT0uk5vrZWMrwAm8RyM1roL5Wv3eTPFY8MeSZahunlzWI-2Bqje-vBdpUXET3r36pAKfAmL_E0bIPvOFzPPqfIapEQayo2LpVKYPXEKQlZ2wncDmDahy9c75qxgmDUwPZIiQ2Ik7v10mkbcnYKYf7AU3BznM0aHK-l8hEJVNkWatAUOkMOrO814b28bafC8gMM-B-n7J0BpTWxYdN44KeaoPwTGWlzgQ7bgoU6ThBvjUiKfhE4RO9y3pxq8bATYBhlgbqB6JN3DvO7cgjWG0EIeWYouU6spHDaKsVOJUwcyVRwmBhVJNc8PuicLRGtZ4yi3I0VErPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc729c6f5e.mp4?token=Ca_upG2AZrh3hT0uk5vrZWMrwAm8RyM1roL5Wv3eTPFY8MeSZahunlzWI-2Bqje-vBdpUXET3r36pAKfAmL_E0bIPvOFzPPqfIapEQayo2LpVKYPXEKQlZ2wncDmDahy9c75qxgmDUwPZIiQ2Ik7v10mkbcnYKYf7AU3BznM0aHK-l8hEJVNkWatAUOkMOrO814b28bafC8gMM-B-n7J0BpTWxYdN44KeaoPwTGWlzgQ7bgoU6ThBvjUiKfhE4RO9y3pxq8bATYBhlgbqB6JN3DvO7cgjWG0EIeWYouU6spHDaKsVOJUwcyVRwmBhVJNc8PuicLRGtZ4yi3I0VErPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/23810" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
دونالد ترامپ درباره ایران گفت: «پس از آغاز به کارم در سال گذشته، مذاکرات با ایران را آغاز کردم و در ازای پایان دادن به برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی را به آن‌ها پیشنهاد دادم.»
او افزود: «اما آن‌ها این پیشنهاد را رد کردند؛ این یک اشتباه بزرگ بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/23809" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.» او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای…</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/23808" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7a774734.mp4?token=LcygkMkjcALHy1x571aXIiX0aouewzryndaDfn3DebYUrbHoJ_pRzhJbCLIXDgQcvNns_CstBLbrdVC2doBC-_ER6LrFqi70o1tJo4QveO_dyoV1pYuwpI_sLlu7Z326DjDxFXVzPNAcjuDor_it_fMizqlRoXI8O4oXOSehNWxKvA4SuMI5VMbg9Eh6pU5tP2VOrB-MCoOQ4tZq6NGj9mlL8J1BZhvvEaQ-F0zZYLgxsmiWxFYgR0HjbhlCcuuG5cD02D8WqXBN5J7QLJwZ3FAuX9HtuyVkPYXNcIRP4w_79Ph88pKPoBZp0I8jv5P5-Gz-vL19-GJ28zq4oylfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7a774734.mp4?token=LcygkMkjcALHy1x571aXIiX0aouewzryndaDfn3DebYUrbHoJ_pRzhJbCLIXDgQcvNns_CstBLbrdVC2doBC-_ER6LrFqi70o1tJo4QveO_dyoV1pYuwpI_sLlu7Z326DjDxFXVzPNAcjuDor_it_fMizqlRoXI8O4oXOSehNWxKvA4SuMI5VMbg9Eh6pU5tP2VOrB-MCoOQ4tZq6NGj9mlL8J1BZhvvEaQ-F0zZYLgxsmiWxFYgR0HjbhlCcuuG5cD02D8WqXBN5J7QLJwZ3FAuX9HtuyVkPYXNcIRP4w_79Ph88pKPoBZp0I8jv5P5-Gz-vL19-GJ28zq4oylfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
«آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/23807" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23806">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac051de59.mp4?token=c_7f-f13H8p5J0zLSoIvfydA3vSsRdfZyb9L9dSWoreW-GHYOpUuH-Qui-nejHlmXk_DFWoGyZdQPZH7JyAxQmtNsvQ9ozppn-ntCNLPGf5mZ4UGZ6L10fpeOy7mqtl1qPEn-HpTQ0e2v111BneGBSrUbsQQKpGEcElqHNn3gU9Gduz-1MEX9GEZ9wFJkHs4hE3XUBm-6ROXCCEC7PfMN403-vU6g3DtdYmk3AiUrnoNwknlCAR6LlW3147AcngQe6lfdbEf8_INcIOH2DdfAybNbTg1PMBsm6SMczAAQTCR59sAWeniBDjX8_Gtgq7GaPNwyoPCyHQa5u_AG0cHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac051de59.mp4?token=c_7f-f13H8p5J0zLSoIvfydA3vSsRdfZyb9L9dSWoreW-GHYOpUuH-Qui-nejHlmXk_DFWoGyZdQPZH7JyAxQmtNsvQ9ozppn-ntCNLPGf5mZ4UGZ6L10fpeOy7mqtl1qPEn-HpTQ0e2v111BneGBSrUbsQQKpGEcElqHNn3gU9Gduz-1MEX9GEZ9wFJkHs4hE3XUBm-6ROXCCEC7PfMN403-vU6g3DtdYmk3AiUrnoNwknlCAR6LlW3147AcngQe6lfdbEf8_INcIOH2DdfAybNbTg1PMBsm6SMczAAQTCR59sAWeniBDjX8_Gtgq7GaPNwyoPCyHQa5u_AG0cHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«با افتخار می‌توانم به شما بگویم که
آمریکا بازگشته است
و کشور ما امروز از همیشه قدرتمندتر است. اقتصاد ما مورد حسادت جهان است.
ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما رقیبی ندارد و ما تقریباً در همه زمینه‌ها
پیشتاز هستیم
.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/23806" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاهزاده رضا پهلوی برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/23805" target="_blank">📅 17:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تلگراف : ترامپ در حال بررسی گزینه‌های مختلف درباره ایرانه؛ از مذاکره و  تشدید حملات و افزایش فشار اقتصادی گرفته تا حتی «منفجر کردن کل حاکمان ایران»!
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/23804" target="_blank">📅 17:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23803">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">با پشتیبانی هواپیماهای سوخت‌رسان BORA74، BORA84 و BORA94، مجموعاً ۱۲ فروند جنگنده F-16C از بال ۱۳۸ جنگنده (138th Fighter Wing) با کد دم «OK»، امروز پایگاه هوایی اشپانگدالم (ETAD) در آلمان را ترک کردند و به سمت خاورمیانه حرکت کردند. @WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/23803" target="_blank">📅 17:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
چند کشور که در تلاش برای میانجی‌گری میان آمریکا و ایران هستند، با هر دو طرف در تماس‌اند تا
یک دیدار در سطح بالا بین آمریکا و ایران
برگزار شود. این کشورها هنوز معرفی نشده‌اند و جزئیات بیشتری درباره این دیدار احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/23802" target="_blank">📅 17:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال ۱۴ اسرائیل : پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کردند که تصویری از نخستین آزمایش بمب هسته‌ای «واقعیه گرم» ایران را به نمایش می‌گذارد. @WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23801" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هم اکنون پس از شرکتهای ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند. @WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/23800" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه های رژیم : «رئیس‌جمهور پزشکیان دقایقی پیش، پس از توقفی کوتاه خود ، الجزایر را به مقصد نیویورک ترک کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/23799" target="_blank">📅 17:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئیس‌جمهور ترامپ هنگام ورود به مقر سازمان ملل:تعجب می‌کنم که سی‌ان‌ان اینجا حضور دارد و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید. شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مشغول پوشش دادن اخبار من باشید. @WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/23798" target="_blank">📅 17:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هم اکنون پس از شرکتهای ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/23797" target="_blank">📅 17:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/066e31f4eb.mp4?token=O9pbvJuUQSnYQ7IA7lsAY0N6XISHA93HSGLaG0aEE-xCLVM1CTHzHx1dxwLWpd6gvsao9ikOo4KngfiksZ68uGxkgPaK0Wvy_SDv6nh9EOZxo3xaBa7A613plcCLnCy-20xtwuHx5tYAPbv4ty2ysC71IGVDDU4X4qA9WwHjcXfsSn5tq9JDr3Bqc_5CY_NHLf4Rj527CODZjPsfLVAv_tcShsOrKBgrC2qHN38EobjYJXEQnX9ko8yk-kLNGSsJhDAOVB75OTIs9Hv9Nhs8wXfe_PAWbjf1LektbpRhud-oIKew7k0_CMgP7HDHjw0rk3NnaaRr-qjD78LcxB716g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/066e31f4eb.mp4?token=O9pbvJuUQSnYQ7IA7lsAY0N6XISHA93HSGLaG0aEE-xCLVM1CTHzHx1dxwLWpd6gvsao9ikOo4KngfiksZ68uGxkgPaK0Wvy_SDv6nh9EOZxo3xaBa7A613plcCLnCy-20xtwuHx5tYAPbv4ty2ysC71IGVDDU4X4qA9WwHjcXfsSn5tq9JDr3Bqc_5CY_NHLf4Rj527CODZjPsfLVAv_tcShsOrKBgrC2qHN38EobjYJXEQnX9ko8yk-kLNGSsJhDAOVB75OTIs9Hv9Nhs8wXfe_PAWbjf1LektbpRhud-oIKew7k0_CMgP7HDHjw0rk3NnaaRr-qjD78LcxB716g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ هنگام ورود به مقر سازمان ملل:تعجب می‌کنم که سی‌ان‌ان اینجا حضور دارد و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مشغول پوشش دادن اخبار من باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/23796" target="_blank">📅 17:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تنگه صدای سلامی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/23795" target="_blank">📅 17:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Z_LPxkANso4L9RxNUGqrVv7SRezbuHt6ECci9fBlWZfwHGAT7DeFM6yhFdL36i4xbL8WoWqTrUCE8f0AgfEoyr4Dpb8hZ0tLUcHTPqVVVSzauZGG09B9ryxw33IdWnce1d3J-utWeTR1Nozk0jqjVBWZKyM33SM94KvZMdjesbG6ND4q1TiNQAh5WE0G5EJJn-CnfZhK4lBfljV4moH1dpoCIYHduFMk7YY7gFVxdNoO6KrCCvU9d_4Nyk0Nd16V99HypWsDDLMEPbVe53rs7alRTUNMVt9bxrB4VAGK9xD_gPySQPMuOkb6G8s5UbDg4LlDRyhXZY0EVJ-5ui8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​ جدول سخنرانیهای سازمان ملل مشخص شد
بر اساس جدول رسمی منتشرشده از سوی مجمع عمومی سازمان ملل متحد (نشست هشتاد و یکم)، دونالد ترامپ امروز به عنوان دومین سخنران در صحن مجمع عمومی حاضر خواهد شد.
پس از گزارش دبیرکل و سخنرانی رئیس مجمع و رئیس‌جمهور برزیل، نوبت به رئیس‌جمهور آمریکا می‌رسد.
زمان تقریبی سخنرانی ترامپ:
به وقت تهران: حدود ساعت ۱۷:۱۵ الی ۱۷:۴۵
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23794" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقچی‌ هم وارد سالن شد تا سخنان ترامپ را بشنود
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/23793" target="_blank">📅 17:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ وارد سازمان ملل شد
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23792" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با پشتیبانی هواپیماهای سوخت‌رسان BORA74، BORA84 و BORA94، مجموعاً ۱۲ فروند جنگنده F-16C از بال ۱۳۸ جنگنده (138th Fighter Wing) با کد دم «OK»، امروز پایگاه هوایی اشپانگدالم (ETAD) در آلمان را ترک کردند و به سمت خاورمیانه حرکت کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23791" target="_blank">📅 16:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تنگه دعوا شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23790" target="_blank">📅 16:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران، از وزارت امور خارجه آمریکا درخواست کرد تا در جریان حضورش در نیویورک برای شرکت در مجمع عمومی سازمان ملل، یک تیم حفاظت امنیتی آمریکایی در اختیار او قرار گیرد. بر اساس گزارش‌های رسیده از آمریکا، پس از بررسی تهدیدهای موجود علیه وی، تیمی از «سرویس امنیت دیپلماتیک» مسئولیت حفاظت از او را بر عهده خواهد گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23789" target="_blank">📅 15:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe43fd0fd0.mp4?token=ZmOwLllFHXq_i9AoUy9uzKRb8WywTcBTF3eyUH8fEaKrY-BOi7FmOzrZNap322ZgVTpcVOYmxApI9-htY5Lfwh3W4yfO5XfzAvb0TU9FXiiw9sGXBoBZyPBUAHoAcCM80G5Zk_hldN8dEvB3KEVg2ze6iLyI2sdD_BmPZ5jklhMvG3gOI_Xnx06ynvGIf9lb5XERRwuUtLdiPznq_klp9EzaRV0MzvjDyv4u88NkC4NB7b-2GQMEgbH9aH_3sIJ6wXOl1ZGTehk6-cCr53Nvt-aWNB9JzCUz5F8y-mN8xIN-4rQVgQZAEil6aSXq-nbPuNTQvPwV287t86774y_ZXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe43fd0fd0.mp4?token=ZmOwLllFHXq_i9AoUy9uzKRb8WywTcBTF3eyUH8fEaKrY-BOi7FmOzrZNap322ZgVTpcVOYmxApI9-htY5Lfwh3W4yfO5XfzAvb0TU9FXiiw9sGXBoBZyPBUAHoAcCM80G5Zk_hldN8dEvB3KEVg2ze6iLyI2sdD_BmPZ5jklhMvG3gOI_Xnx06ynvGIf9lb5XERRwuUtLdiPznq_klp9EzaRV0MzvjDyv4u88NkC4NB7b-2GQMEgbH9aH_3sIJ6wXOl1ZGTehk6-cCr53Nvt-aWNB9JzCUz5F8y-mN8xIN-4rQVgQZAEil6aSXq-nbPuNTQvPwV287t86774y_ZXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، درباره ایران:
«رئیس‌جمهور ترامپ آماده دیدار با
مسعود پزشکیان یا هر فرد دیگری
است. اما اینکه چنین دیداری به نتیجه‌ای سازنده منجر شود، مشخص نیست؛ زیرا
تصمیم‌گیرنده نهایی در ایران رهبر جمهوری اسلامی است
و رهبر جمهوری اسلامی یک روحانی شیعه رادیکال است.»
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23788" target="_blank">📅 15:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb2d25d09.mp4?token=FHDWFIugfK4VSbDXx3IBtW8HhSFm2hqcftNGn8Ekgca3T3F0r7w_YDsPBSB0EJLQr8iWVRQU9Tmy-rjKnDqClRAVGS5oRGTodbTmwNU0nx5CVPFfOOrDogeGg-XvyK0H_od5RYoOfREfwkkJSUbJ-6uHmpMKDdBu9KzWzhlddKsoo_TQO01r6i8h83_0yDsuIg--BVRwpYLnUcWYhGs9-TZYJD6yVINiF2sBN_63qwSekrFAxTSV7c241DVi9zzcYtexzEp8FSWEX2slLlmkQoSJv0LUhTh1NybthhsR_qZmFQ3b38eNTQJryx5m1blAqKviHJGuhkRFsWoW47kY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb2d25d09.mp4?token=FHDWFIugfK4VSbDXx3IBtW8HhSFm2hqcftNGn8Ekgca3T3F0r7w_YDsPBSB0EJLQr8iWVRQU9Tmy-rjKnDqClRAVGS5oRGTodbTmwNU0nx5CVPFfOOrDogeGg-XvyK0H_od5RYoOfREfwkkJSUbJ-6uHmpMKDdBu9KzWzhlddKsoo_TQO01r6i8h83_0yDsuIg--BVRwpYLnUcWYhGs9-TZYJD6yVINiF2sBN_63qwSekrFAxTSV7c241DVi9zzcYtexzEp8FSWEX2slLlmkQoSJv0LUhTh1NybthhsR_qZmFQ3b38eNTQJryx5m1blAqKviHJGuhkRFsWoW47kY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، درباره ایران:
«تصور کنید کره شمالی در خاورمیانه شکل بگیرد؛ این برای جهان فاجعه‌بار خواهد بود. در آن صورت، قیمت گازوئیل که امروز مثلاً ۶ دلار است، ممکن بود
سه برابر
شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23787" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2875ab9dd.mp4?token=IyAU8gO7CfI2ZifjkNw-uKwk3cVe0bikB8OvM8ANlHFxgmuSAXmr6OxV65LxGQEUl7ZBKJQCSc-At484VwX43N4YHwJsxk35coHOR5I0avBOIfLXxNMwd8DfBNHBWVjtpwjveIEcjIwVxfkJ0BxjzwOFNbDMuT5otIUcJE9vt-iNnXn9lgA6FpPP1e1eYwrhYMfhiz_0RMT47CghB8C8StwlP7ySI7fG4Rvnjyjm3JfylO5phA2F1v7sTCD75jC0QOZ8BA6nIQ0Hb2QSIq-AoR1kUjTTuTNmaiphE7Ww9Sa7Ukg0A56Ba9QNmWBKC4lr7m88395gtDe4uCg12wj5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2875ab9dd.mp4?token=IyAU8gO7CfI2ZifjkNw-uKwk3cVe0bikB8OvM8ANlHFxgmuSAXmr6OxV65LxGQEUl7ZBKJQCSc-At484VwX43N4YHwJsxk35coHOR5I0avBOIfLXxNMwd8DfBNHBWVjtpwjveIEcjIwVxfkJ0BxjzwOFNbDMuT5otIUcJE9vt-iNnXn9lgA6FpPP1e1eYwrhYMfhiz_0RMT47CghB8C8StwlP7ySI7fG4Rvnjyjm3JfylO5phA2F1v7sTCD75jC0QOZ8BA6nIQ0Hb2QSIq-AoR1kUjTTuTNmaiphE7Ww9Sa7Ukg0A56Ba9QNmWBKC4lr7m88395gtDe4uCg12wj5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو: ما برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم ولی فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد @WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/23786" target="_blank">📅 15:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ca3ee788.mp4?token=fCRL1OnNjNwpIXAyBrYBLwzzZAuHPR0EV0F5d1Ncp0IciUAFEztiB43Cj1OfNRCb9gY16hw09jtTcuBRqGkRt0FzeNaYf43qXDzQrUnu7uqsJEFtvlkJKmFysLxmCsG9HC5qng45hRWHUpHTD8V1bIRlEOgQK04rMmVIf5lLjVmpOk7qQHakUFfmtKYCYUQqk5QZ4Cbilnh1VQz9A2aTgA2BzCRWo2FP2DK4HxmrbA1V-LOK7d3qvvz43VT_u1xoKBDD9KdRaq4uPpmqjnF8HunySwDhYtDbstXKrP2xYYKpCosXDjfwocmYEFl58OMs6jh6gJBcVgqlZYDgnfVKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ca3ee788.mp4?token=fCRL1OnNjNwpIXAyBrYBLwzzZAuHPR0EV0F5d1Ncp0IciUAFEztiB43Cj1OfNRCb9gY16hw09jtTcuBRqGkRt0FzeNaYf43qXDzQrUnu7uqsJEFtvlkJKmFysLxmCsG9HC5qng45hRWHUpHTD8V1bIRlEOgQK04rMmVIf5lLjVmpOk7qQHakUFfmtKYCYUQqk5QZ4Cbilnh1VQz9A2aTgA2BzCRWo2FP2DK4HxmrbA1V-LOK7d3qvvz43VT_u1xoKBDD9KdRaq4uPpmqjnF8HunySwDhYtDbstXKrP2xYYKpCosXDjfwocmYEFl58OMs6jh6gJBcVgqlZYDgnfVKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل
، در واکنش به اظهارات
زهران ممدانی، شهردار نیویورک
، که او را «
جنایتکار جنگی
» و «معمار
نسل‌کشی هولناک مردم فلسطین
» خوانده و گفته بود حکم بازداشت صادرشده از سوی
دادگاه کیفری بین‌المللی (ICC)
علیه نتانیاهو باید اجرا شود، گفت:«
شرم بر شما، آقای ممدانی.
شرم بر شما که از
هیولاهای تروریست حماس
که مردم ما را قتل‌عام کردند حمایت می‌کنید. شرم بر شما که به
اغتشاشات علیه یهودیان نیویورک
دامن می‌زنید. من به
سازمان ملل
می‌آیم. می‌خواهم درباره
سربازان قهرمان ما
حقیقت را بگویم و درباره
شما
نیز حقیقت را خواهم گفت.»
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23785" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روبیو: ما برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم ولی فکر نمی‌کنم هیچ جلسه‌ای بین ترامپ و رئیس‌جمهور ایران برنامه‌ریزی شده باشد
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/23783" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ در تروث : بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به کاهش است؛ اما این حرف صحت ندارد. ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و هم‌اکنون نیز در حال افزایش تولید آن‌ها به سطوحی بی‌سابقه هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23782" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رویترز:
ایران در صورت
کاهش فشار نظامی آمریکا و رفع محاصره بنادر ایران
، آماده است
تنگه هرمز را ظرف ۷ روز بازگشایی کند.
هیئت ایرانی در نیویورک اختیار دارد از طریق میانجی‌ها مذاکرات دیپلماتیک را از سر بگیرد، اما تهران خواستار تعهد واشنگتن به
تعیین یک جدول زمانی برای پایان درگیری‌ها و حل‌وفصل دیپلماتیک بحران
است. یک مقام ایرانی گفت: «آمریکا باید اعلام و رسماً تأکید کند که می‌خواهد موضوع را از طریق دیپلماسی حل کند و سپس درباره جدول زمانی روند مذاکرات توافق شود. مجمع عمومی سازمان ملل فرصت طلایی برای بازگشت آمریکا به دیپلماسی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23781" target="_blank">📅 14:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی سپاه پاسداران:
اگر آمریکا به
کوه کلنگ یا هر نقطه دیگری از ایران حمله کند، با آن مقابله خواهیم کرد.
ترامپ پیش‌تر نیز تهدیدهایی مطرح کرده، اما نتوانسته آنها را عملی کند. اگر آمریکا حمله کند،
ایران کاملاً آماده پاسخ است
و تجربه پاسخ‌های قبلی ایران که به گفته او مانع تحقق اهداف آمریکا شده، تکرار خواهد شد. او تأکید کرد:
برای هر سناریویی آماده‌ایم و در هر عرصه‌ای که دشمن وارد شود، پاسخ قاطع خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23780" target="_blank">📅 14:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز:
ترافیک کشتی‌ها در
تنگه هرمز به تنها ۲ کشتی تا پایان دیروز دوشنبه
کاهش یافته است؛ این رقم یک روز قبل ۱۰ کشتی بود، در حالی که پیش از جنگ حدود
۱۲۵ کشتی تجاری در روز
از هرمز عبور می‌کردند. رویترز همچنین گزارش داده دو نفتکش در هرمز هدف قرار گرفته‌اند؛ یک نفتکش با پرتابه ناشناس و یک کشتی حامل LPG نیز با بقایای پرتابه ناشناس آسیب دیده‌اند. مسئول حملات هنوز مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23779" target="_blank">📅 13:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d07f32a5.mp4?token=gOG8xxoUgS76GKMj0uP6LZQtoEiXUmntk5QceoSDk_qGnC95k_mvMkdi6agUBjNxLYLq3M_caLvm9Xd3N8TbcQ4fP-wYn_i23pOBq-inipreMd5lMl0UDiAaqmelsoMhMfFw9ggOXyDE2NJ-JDYhn2EF1l1Q9sKliC5u-EIt6j8lQqUCXoDPO-PuV-n1IRFik2mzdig0shQzP4KWIOMlzFJvqSMi78lG7VKWYrxTKp_2fL7UZh18B0Tl9r7kxoELmSxXrIcoVMjKTJlF-4SBcP7lSj4bDNvUwoPBj3KGLKpf7Dbm0_rN5u4FQqGdsc9m5HWHcnB6N3ok869fQ2WURzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d07f32a5.mp4?token=gOG8xxoUgS76GKMj0uP6LZQtoEiXUmntk5QceoSDk_qGnC95k_mvMkdi6agUBjNxLYLq3M_caLvm9Xd3N8TbcQ4fP-wYn_i23pOBq-inipreMd5lMl0UDiAaqmelsoMhMfFw9ggOXyDE2NJ-JDYhn2EF1l1Q9sKliC5u-EIt6j8lQqUCXoDPO-PuV-n1IRFik2mzdig0shQzP4KWIOMlzFJvqSMi78lG7VKWYrxTKp_2fL7UZh18B0Tl9r7kxoELmSxXrIcoVMjKTJlF-4SBcP7lSj4bDNvUwoPBj3KGLKpf7Dbm0_rN5u4FQqGdsc9m5HWHcnB6N3ok869fQ2WURzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل : پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کردند که تصویری از نخستین آزمایش بمب هسته‌ای «واقعیه گرم» ایران را به نمایش می‌گذارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23778" target="_blank">📅 13:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کیودو نیوز ژاپن به نقل از یک مقام ایرانی:
ایران اعلام کرده در صورتی که آمریکا گام‌هایی برای کاهش فشار نظامی بردارد، تهران می‌تواند
تنگه هرمز را ظرف ۷ روز بازگشایی کند
. به گفته این مقام، این پیشنهاد از طریق میانجی‌ها به آمریکا منتقل شده و ایران خواستار ازسرگیری مذاکرات برای دستیابی به پایان دائمی درگیری‌هاست. این گزارش تاکنون به‌طور مستقل از سوی ایران یا آمریکا تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23777" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر دفاع اسرائیل، یسرائیل کاتس:
«با توجه به برخی نیت‌ها و گزارش‌های اطلاعاتی، به سازمان تروریستی حماس و حامیان آن، از ایران گرفته تا اردوغان، هشدار می‌دهم: اگر حتی یک سرباز یا غیرنظامی اسرائیلی ربوده شود، کل شهر غزه، همراه با خانه‌ها و برج‌های آن که محل فعالیت‌های تروریستی هستند، به سمت جنوب تخلیه خواهد شد و بیش از یک میلیون ساکن آن نیز منتقل خواهند شد. با شهر غزه همان‌گونه برخورد خواهد شد که با رفح، بیت‌حانون و ۷۰ درصد از مناطق غزه برخورد شد، تا زمانی که افراد ربوده‌شده بازگردانده شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23776" target="_blank">📅 12:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">@WarRoom
DorDor</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23775" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23774" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23773" target="_blank">📅 12:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st8uf8GJzaFR7u8bNnIYS8YuBKRNIv0wcaVFw_152eFiNNDPob-DwMRLZwyxvcYnglewCNzyJQu9aaCNHvvP7p9xEJNxQAHr3pn3tNryv3SjtVrtFq5jM5uX0dDpZfCfH4fvC8uyrTJC14jY5bteUfvWcHq5Zimwr26QoEptgvKgBZS7ENh2GU8dJwBrU6wCgstRl9h6p8HLLdBDmBiRMgdDOrINIdkG15qmrILlEC7mqWlfFIFWJb6ZxbnuYfD846Pko4eSIhhBQykjnoTpOgJuiS5O6058p_rZVQP6vdE-lW2Lj-ob5t1aX40SWIHIciSzZR_txC1b45qd9pApqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه اخلاقی : تو کار خدا دست نبرید هر چیزی حکمتی دارد
😂
😂
😂
😂
😂
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23772" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">روز گذشته، گوشی یک پاکبان زحمتکش در مشهد به سـرقت رفت و یک هموطن با حضور در منزل این پاکبان، برای او یک گوشی موبایل تهیه کرده و به وی هدیه داد.  @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23771" target="_blank">📅 11:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d0f93a54.mp4?token=g9jjl-prSeEQvyUotG6hr0xFyLHC5qgM-Yl9xTzqOD8WYNhboj3qRdtxzyHKZZkDd1TyFoYSfQS2z7OjYus4E2r7V9DTx_9_kERWfr6F1-09owLru-Rl1G4dAxQeWJaq_2wzwRfda_DDpcRDW-wGxNAIYmMmNaRcJGPw1e8wnqIDeg9dQ9yq_g2opaeVpFaGmGAJKwVTEukwKlyppTukaq0zgmSgUWj55zU2fGwcp0aNpl5yJNU03rZs8ZBupKvQ7DFDpxM3XlFzZYZPcE1Ihq4cd9LOgHjHUNaDIuBF_LqM_TDehR46v2BMQbi5W6-QxdVz_7fu7DQEwPgG1zUFmDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d0f93a54.mp4?token=g9jjl-prSeEQvyUotG6hr0xFyLHC5qgM-Yl9xTzqOD8WYNhboj3qRdtxzyHKZZkDd1TyFoYSfQS2z7OjYus4E2r7V9DTx_9_kERWfr6F1-09owLru-Rl1G4dAxQeWJaq_2wzwRfda_DDpcRDW-wGxNAIYmMmNaRcJGPw1e8wnqIDeg9dQ9yq_g2opaeVpFaGmGAJKwVTEukwKlyppTukaq0zgmSgUWj55zU2fGwcp0aNpl5yJNU03rZs8ZBupKvQ7DFDpxM3XlFzZYZPcE1Ihq4cd9LOgHjHUNaDIuBF_LqM_TDehR46v2BMQbi5W6-QxdVz_7fu7DQEwPgG1zUFmDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز گذشته، گوشی یک پاکبان زحمتکش در مشهد به سـرقت رفت
و یک هموطن با حضور در منزل این پاکبان، برای او یک گوشی موبایل تهیه کرده و به وی هدیه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23770" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آسوشیتدپرس:
شی جین‌پینگ در دیدار با ترامپ تلاش خواهد کرد آمریکا را به
توقف فروش تسلیحات به تایوان
متقاعد کند و به توافق مشترک سال ۱۹۸۲ میان واشنگتن و پکن استناد خواهد کرد
، تایوان و ایران
از موضوعات حساس روابط دو کشور هستند , باید دید آمریکا چه درخواستی دارد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23769" target="_blank">📅 11:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رویترز: ایالات متحده قصد دارد یک پایگاه نظامی متعلق به دوران جنگ سرد را در منطقه نارزارسوآک در جنوب گرینلند مجدداً احیا کند و همچنین در مسترسویک در سواحل شرقی، یک حضور نظامی جدید ایجاد کند؛ این اقدام در چارچوب توافقی میان آمریکا، دانمارک و گرینلند انجام خواهد…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23768" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز:
گروه هفت از ایران خواست
تسلیح و حمایت از حوثی‌ها را متوقف کند
و حملات حوثی‌ها علیه عربستان و کشتی‌های غیرنظامی را محکوم کرد. G7 از حوثی‌ها نیز خواست حملات و تهدیدهای نظامی را متوقف کرده و به روند سیاسی بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23767" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d93d52cd3.mp4?token=MnA_ldUAWrOi2Z1iCpbLaFtTSEh8p7G0JfdTmf9V0aX5OeOyXRJn59iysrHluzh8SyFu1MmNkOtkp-CqsnBKO5B29779KWEUJyRclJrIWCKE4MiTAUydG50mhbZi2rBM8tpb53OSOptSC9IMqmA61YHah9ndidQg9WN2CjuVMOccOSdK2iXbp5wcBIroQ2pfIXAZQhC5BkyGYAJ37iALOOCt_W1k9lOHaswmnVBEPDIhxZSFraBsx3F4UKG7DYgIDIW4QHy986X_yQhEh2pcBzZw67whTp9TBuq-EUksgZQiUnh3b6b3wXVQI8lPYPei3_qbLys1noVO57IfWaCPARjLyodanGRRbXs2N3BN7m1gsuYTpccK82zZDMEtbk_XxfJI12lgZws28yQ9zAB0ysY4VhklY-5IUOAwHW4BnLfdugTTowT7oa20_2HGPK1Tov2RQhmvjG0VhoSqwQMbMUS1fqS9vcn4MRNQdkjLk_4kBbtUhuAcvmL1PToulBcBEAq78ggErFeLbS5g4xUlPhJl16uxej7eX4Aa0_DPkLKUHBYtC8d798l0Kq68EGavlnnbID9lzWGPnIQweVfLKzArdzsG8C5AlrffSbpNHlNTtI3_9A5X8eWbLGwc0ghYBRaM7P079-_bgtkczmOfnFwZ10OEW8kMt0o50910h_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d93d52cd3.mp4?token=MnA_ldUAWrOi2Z1iCpbLaFtTSEh8p7G0JfdTmf9V0aX5OeOyXRJn59iysrHluzh8SyFu1MmNkOtkp-CqsnBKO5B29779KWEUJyRclJrIWCKE4MiTAUydG50mhbZi2rBM8tpb53OSOptSC9IMqmA61YHah9ndidQg9WN2CjuVMOccOSdK2iXbp5wcBIroQ2pfIXAZQhC5BkyGYAJ37iALOOCt_W1k9lOHaswmnVBEPDIhxZSFraBsx3F4UKG7DYgIDIW4QHy986X_yQhEh2pcBzZw67whTp9TBuq-EUksgZQiUnh3b6b3wXVQI8lPYPei3_qbLys1noVO57IfWaCPARjLyodanGRRbXs2N3BN7m1gsuYTpccK82zZDMEtbk_XxfJI12lgZws28yQ9zAB0ysY4VhklY-5IUOAwHW4BnLfdugTTowT7oa20_2HGPK1Tov2RQhmvjG0VhoSqwQMbMUS1fqS9vcn4MRNQdkjLk_4kBbtUhuAcvmL1PToulBcBEAq78ggErFeLbS5g4xUlPhJl16uxej7eX4Aa0_DPkLKUHBYtC8d798l0Kq68EGavlnnbID9lzWGPnIQweVfLKzArdzsG8C5AlrffSbpNHlNTtI3_9A5X8eWbLGwc0ghYBRaM7P079-_bgtkczmOfnFwZ10OEW8kMt0o50910h_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خزعلی: شاه به قم آمد و به همه آخوندها گفت دوره مُفخوری گذشته است. هزار و چهارصد سال است که فکر شما تکان نخورده
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23766" target="_blank">📅 10:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1192bf611.mp4?token=nzp0_J6FMvEOvCd51wyaoiWtNEPJuoJky03KrNQk1DaCb07xx5LehJru-GF0o-MRXYGXtVMlkojGD03iPCvjgpv-AiT5LV-SbG6tz9QvyhTnNXGOcHOLZZ7t16jGVJJ2I5sKiuwMPLX9mUOxYNIo0Ckww1KtinY0z33pJTQoZ8s2Va2q7D0rumV5VlJWAy7QzfsuQD9VkBLiFZAjgpryhRDfmZQ6kK_6HtY3RzovS3QSfXvFWcYfLcqNhQXnXTD4LWcdEUj27s3NXnHIl4TjT2Z6SIbFJ-SqCDb3_yswdjUXlTVl5egVPsLbXCVJTSON2caReCRdgowKN-TKqEg1kVrOR6tIUUbmi_i1Rp4kkYSSLOMyKgb3IDJaMGKmNFEOadgWNYPt04uMH45cTw6sr61xPBPdrvIEjNGmcYuI9i5p6unKB9zn257wu1gBhZRo817sKGE2HeU3NOC4AoNJc5QFRU3gLtZYL-yDzx2HguPEnIDop3hjVhE4mH1ZPXVFluSE8GRz2rwvtTXVU3S95-sD8aluIvK3hBC-BJSGf_UJ3WudrtehVzEGR0aVL8sbHub4w23V3FXtrvu82Ly5gtDD6yvydkn8AogSxrxLLtBmbUnCxLLHoFC-J_TBpVr9J8_fwXPzHk_AwzK9tTv34lGi6tkWmqJ-FvgwANDCSN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1192bf611.mp4?token=nzp0_J6FMvEOvCd51wyaoiWtNEPJuoJky03KrNQk1DaCb07xx5LehJru-GF0o-MRXYGXtVMlkojGD03iPCvjgpv-AiT5LV-SbG6tz9QvyhTnNXGOcHOLZZ7t16jGVJJ2I5sKiuwMPLX9mUOxYNIo0Ckww1KtinY0z33pJTQoZ8s2Va2q7D0rumV5VlJWAy7QzfsuQD9VkBLiFZAjgpryhRDfmZQ6kK_6HtY3RzovS3QSfXvFWcYfLcqNhQXnXTD4LWcdEUj27s3NXnHIl4TjT2Z6SIbFJ-SqCDb3_yswdjUXlTVl5egVPsLbXCVJTSON2caReCRdgowKN-TKqEg1kVrOR6tIUUbmi_i1Rp4kkYSSLOMyKgb3IDJaMGKmNFEOadgWNYPt04uMH45cTw6sr61xPBPdrvIEjNGmcYuI9i5p6unKB9zn257wu1gBhZRo817sKGE2HeU3NOC4AoNJc5QFRU3gLtZYL-yDzx2HguPEnIDop3hjVhE4mH1ZPXVFluSE8GRz2rwvtTXVU3S95-sD8aluIvK3hBC-BJSGf_UJ3WudrtehVzEGR0aVL8sbHub4w23V3FXtrvu82Ly5gtDD6yvydkn8AogSxrxLLtBmbUnCxLLHoFC-J_TBpVr9J8_fwXPzHk_AwzK9tTv34lGi6tkWmqJ-FvgwANDCSN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چک سنگین شاهزاده به صورت موشتبی خامنه‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23765" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
