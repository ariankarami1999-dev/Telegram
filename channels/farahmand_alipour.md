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
<img src="https://cdn4.telesco.pe/file/QpcFfaDThY3BvG0_KwCOuHz9pZtTikXOiYxM-puMw20t6md_vRPfnobrcl-M5z1_MYzllKTKz6sAkzkn9PQ6ORlIaXBxscpZEubJDqiSp_6Q-28PEAzeOoCGpdsL_a4T_uApOu-DOmzXqBOwGck8QtPQ2TSqJHPTKlZ7VaOyskyXZC0KWagLESW5BfOWWC6u1fdoxH9w30jeCFE74CTnuJwPkPmuw6IN4eLCYRwe2EfQOz1sePf-MA000DiQLeJvhg5AwySM0QU1Whoa55pJBKdhemf_u3fkKOBwsi2AinWlw6Kq9zUWOfXW6MbuZgF5UXOAbg3fEomt1ljXgnLaPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 14:56:10</div>
<hr>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_-ck1ufxBY7ZlsBptoEAQUX49M66JszI8t3DtT1bzIEVbwRQ5Ql76ij2tF8Dn09EhtT5s3N6jBEKT-NBzQvAwp8vfbb_o6Z4cSG40EuEZRQuOPItAV2YCx3r3bEYaVQLiNPPJBotwrHZel5t7-G9KeNgYe3LHym4xRfxnwmitdcix3fqoaTHY7eoJNu4E-JGQn6s4OUhx175H9vayJuhPde-cm-pHBw6--jqjGJqu3Vb3nV6sD6_-oFiLSHgC9DLBxE7Zxk5AYDoiB8XVWiFwcguenxEUdeN-_xtKebZNQc2C_HmBzO1tx58_Tr00Bu4evoQEd7qheHWxrqaovEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ANCxAohvnPaLSBu--SUDgSJFGCcEY6nAo-LaLnNQakA9dGoEITbdM7FOmERBBZYH4kZMe-Z0Vg1YsCykQFf9MBnuiEZHX3XzeG4vCpJ4PbU5gUWIFcNAKshBnobAlwsEdxdGXB4ZHKUW2LJFKu63qJXl8KHK9LXL08JmXEoeKDPDJmSY7lPTej9vM0e05RXvE6LKhaDpFFY5nuWAU5h4x0a6yAW_ocMaFna1FY7wZGC6dqMNws9OvtJYiIhLDoIaZQzOXogPdZFPhIgXc1EHGOeVZ8QecY9dCSuHS3rwyB0-NR3A9YkY0Llguc0NflbH83qN1NRG2t7Ti-7PJVqN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ANCxAohvnPaLSBu--SUDgSJFGCcEY6nAo-LaLnNQakA9dGoEITbdM7FOmERBBZYH4kZMe-Z0Vg1YsCykQFf9MBnuiEZHX3XzeG4vCpJ4PbU5gUWIFcNAKshBnobAlwsEdxdGXB4ZHKUW2LJFKu63qJXl8KHK9LXL08JmXEoeKDPDJmSY7lPTej9vM0e05RXvE6LKhaDpFFY5nuWAU5h4x0a6yAW_ocMaFna1FY7wZGC6dqMNws9OvtJYiIhLDoIaZQzOXogPdZFPhIgXc1EHGOeVZ8QecY9dCSuHS3rwyB0-NR3A9YkY0Llguc0NflbH83qN1NRG2t7Ti-7PJVqN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aClTm4qfiUfdz8oh6HdUlAPdggj7VQqZbahR2AYUzf8-JfLcy9zXqhQFIRrGkiNjMPK9Kppw0dplx7K1c_h69ydz9X8Zw6yhL4znt8lzTxNUlX4hgWs_D8gCCgWGW-V8jg5faGZvfh4CaXZD4vnxNc3FnZuCwtoIUQ_1ihg42W57Rj722hZj80iHOTGVfqSJt-PJgguWXqWAFL_Fcy8QLDz5Lc5YAFopH0DsCdcv2DIGRli8HpgU_uTBDMIv8BXZnWOH-3I7jIHXSjorF_d34z5WE45SLe1bykavhmi5MjhjnXWKqnnHAp2B9s6Fmm4zH8w2xhxEKbrbO9sWdiDbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heePX2bwR0h_r8zrwE6nulmAnmsGGXfh3MZ4KaA9wkGRHdK60wfrXdkjnIGIvEuCnURIbSNj-9CFAnzLkyZ7hu7lXi6qkMtZAvkHnXuWZGcYDS6vTEQhzzPFX7p799Rnl36a7xiaj5n7RgxAz-PGPNOhzXjkmTUzF2d88zLzknhZOQTT34zwcvO8Rh1D5vKxi1fzsrwz_hXPFpiNVyQb3Q6uWm5Cc9eq_rRe9B7PLy83C9sCNMkzYs_2k3D59j3VhJQPNWwqbjKqWa8YkPov7eTHQurTVBaD_gBN_11Z9D-OrPKvmkRQP3-i95lOBZfq7c4GQCoAu_D9vYEviMj-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP_0m7zFhXYypUHAx4I2oC-g0r38w0XzsslRtkpO2ABOGe9vMk8AHg-b9EhTTJAZuQak3JDhmNLcbbaGvHs8qRof84OcNDruLIEF7I-N6RdCeoEqnczbU5aMSFB5V3fxdfWK1ZRvi3zr95vIfRbEKk16qU3_hziUuF4TFKeXUEsNzsygeXPAtlYuhSlfY2fSD5kGCeCirg_FlVHPPEmXOpKX_8Akt_rHF44x8EGMvqVqE4I9JOcfgKrcMNqok_9l6lH208bnhDuOtMne6RwNMsIEj7PaWuMProRYgIl7wqK9Vodd2T_o8GGRFo-aYhJ9mR8zZpwNBTVDMXGJlT_UNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Z7z6AO-fsPzxp7YqobRjGDqYtNSwKpuYJcs8KwikUATKM-dRc1rca2T5r9utdK22Hg7riF9rWgYQRzic_lpcL0UKm68d9q9WsV392bB47BkSO7iUvBBMpvhJersmjxkE9JPq6so1hOWX_q9HLTFMT5w469D2Tt_lhRD0QARpnKMZKOvXUMeWlVXLRb6-2mDcQ5Z4IgKg5WB5PxWfMsQq8239W9T2QD8BL1X55qHNqJ1TGyy3J_ONLDUoK3oRWF1GFrq_S9qR6ushAmqrVjG6MGkccMRpnZbzJsMamiObjzBp6j54ilAZ_VRjgJXrodd_tC-Yu9YoiQHPwjMEP2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=BqZpLQSc7RXoRM4UPa37SDwtABfH2g5Yekxii2DTWiUaf8AQy5WNgGE3Ax5dE_GJX-yFBTAhQTQFNwxA1N2adGsPQh1eBkntkH4tX2PcKb0rC1o5eRoHX7-oruPGqtdNjazn8gYzCZ9mWfj8v_x67l0Jk11givUYYG3aqy_LQOXh5L886c56ISOPMI9FnAuvPM-0fRTLVIY65LPQQ6UL0SIXV9akPsQyiNWyckHSDQzsmtK2ZhlJ2UW-mvtWwAdxXZNkKfQx0JSF-agFm5v1jL9MfbZeEgBpsyQeBHVPDmXaCLl9F9j-8yA_2LfzqTC2fUN9zHxPO_6DyFPeDEaxnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=BqZpLQSc7RXoRM4UPa37SDwtABfH2g5Yekxii2DTWiUaf8AQy5WNgGE3Ax5dE_GJX-yFBTAhQTQFNwxA1N2adGsPQh1eBkntkH4tX2PcKb0rC1o5eRoHX7-oruPGqtdNjazn8gYzCZ9mWfj8v_x67l0Jk11givUYYG3aqy_LQOXh5L886c56ISOPMI9FnAuvPM-0fRTLVIY65LPQQ6UL0SIXV9akPsQyiNWyckHSDQzsmtK2ZhlJ2UW-mvtWwAdxXZNkKfQx0JSF-agFm5v1jL9MfbZeEgBpsyQeBHVPDmXaCLl9F9j-8yA_2LfzqTC2fUN9zHxPO_6DyFPeDEaxnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=Mrwaq9NC3oKcfMPDl564BXqM6PL_hzcT0CEsTyASwmQzKIRNjsxJwyI6oTP1K0ul2UJT9JaZ8ZAGiDjA30Uoa_IVH7Rvs1eTJSBKVzzjUe5Qe25g0pSHDHA2T7aE0OOkWBrQjr8swM_6bqjqrCCToV8LtYZOVjwOhP8Htmgu9_M94Ov9zrBZ0GIv80riSNfBhL5A74LLh_At5Qi_iGRaoLSN9kkgbJ_nc8CJbU4y-JYKzQPVulfM0g_8akiYLKtV3umqUSWnyZMkA7Lqbwi9sCjoPszwg-3Aeq7b5fFywpFpaeXL83UOODuJ4rL830DarkNyI6FhENvBSSi756u0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=Mrwaq9NC3oKcfMPDl564BXqM6PL_hzcT0CEsTyASwmQzKIRNjsxJwyI6oTP1K0ul2UJT9JaZ8ZAGiDjA30Uoa_IVH7Rvs1eTJSBKVzzjUe5Qe25g0pSHDHA2T7aE0OOkWBrQjr8swM_6bqjqrCCToV8LtYZOVjwOhP8Htmgu9_M94Ov9zrBZ0GIv80riSNfBhL5A74LLh_At5Qi_iGRaoLSN9kkgbJ_nc8CJbU4y-JYKzQPVulfM0g_8akiYLKtV3umqUSWnyZMkA7Lqbwi9sCjoPszwg-3Aeq7b5fFywpFpaeXL83UOODuJ4rL830DarkNyI6FhENvBSSi756u0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGVoNrcxDxw6T71Flue5sGNepXGRDRDKV3oAPse4YAbdLyHz7WwwZDSIRrEDHgUsg1Us0AHLN5SEz4MW2uxaVPsZuuS3U2JvAWvTbQrHlg1nWRfoLota2fK_DAfUGqf45VAT6_yt9KFb_Pq-VXsEZezut0l389qWGF8XFs2FoOBlKyXNiAEMqrYTxPh6DM9IgRS-PXXWyEaA7ySswZ0_qGJ5RifQOQK5XkI1eL5HW2EDBT2wmhjFggSdgOMAN8iVxuJEO8fDspPt8hDgEAIEseePGqS3p7xJbmU6CMUC-DOxW1pygy2CNxCvMuNJv5gkuCV8jQ8EECYHpopjPakA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBNMHpTtmPxcyXN5Nz_S2zXOEMynSLJcg4Hv4PQuIPUFnRyQ1jp5BpAxiLRo6SZ5fklpUQpINW76oGiLdN-BOjJlAFMPFv7EQoyHbb3xaYYBoJoTbPFhCH_rhyglE5rMihxJDZq7bjc8ESZ0AJf79iNk-8F1rCj4M30lLSkQCFnnxxnScvEGVg4kVXzMt8-rR0LG3iPJ9xayQ8uQcFhEwEzsMvzMHylncHGXcPFN2mIffQXZNqn-CkqhQcsBjmuFFOY6U6taQp0kMQHctgil-K6mEiTDgH9C5gMD7XfDz2nLmD3imyEDWRZ94ycUJNC3hb_Kp4Bdtp2IXp_RsG4tDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqV8OsIUwb1xsmx1KygckpFegsPLV02V6GQyERc2GebHaBNbA2eEzXoHi_V8nBbavIFb5tedvfalmgeIqKmD4aoLVP5JSj3h8ttXUUYXHhc5YoBC-SgOxomDfFEABEjauW6eomkAWCGlIlYKqB9VMw6JLRvMRBgfvyiRxGzE-Cjae_z2pPnLY2ibKqHZCHBQKlnzapxs_cey2ylm0Sdm1BcOqaDcwi3ZZxIwh1Y3jGPw69uY-3kg_rDPmeDxrgWVX5gS0nZlpyHQdvVFcBLCsmTu-wSztkc375EqoCvYEBUy7X7WqjbK49ZDP11CZ76tPpAbe-IWU6WrrQdDqT746w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfP4RuUtDrDKF4oXlsd8XDTo8_lhrJuuMnrw5t4w2OhOrS345vQLqkBhbz27PK_gePrOFoQMW8Su_xRXe7IBon8Sw1LM8nqguBpHOtHMhjvDg5cwO9sBJ6pxQt_9GiJgEXB2LulP9wRjwZG_qoCWWfohEyyhqCD8l1OjBZZTUJVqtsIf6gadkFwIwPAIMmlWfHkXM8XDeibSoVG_ve0LZwayxbBNu9sNzL_OQRcsxnyz7nvpa1FZvU7pVuNSdQJBHTUAFke0dgf69vWxe1bzDcLdwbl5FAPotyZWmtTBB487BIHtkctgYzXrZQyY6wA_OBxnleMIgHPE8mpLeflGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCfuiJmePUqjlo9IUwLGW8tWnxdnrnzENg4oxqEU_Ou4WuKsgA5I34qB_wE5a_d2julzer0lAr-G-87B_CIM9xYWwbTgzEhV0-ltL3vfJxj0M4wazn1UueDZSr7TAFjFE5bqZ7GqmLd6ZIYboghHOZVd1PcWMd6ko0wyWrn0PjxwpFpXVRP4wSZYGtjUfZoztP-T_84c2DPAFzEBpscRTpASPrf-EhEf0OBy3Xwv0KT7Y68xCnNUPRE2TtaU1uySeOovfxqboG4iVHs9sbfNpoxMj5v-Z8pv4eWc6ZktAdcbcb5xqgtt1-g3bL9WomXYWNB01yIbrgqv8VS6_MEG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hD0_8bCAbZX2GvJVJnnE1puqu2w1sbvwsMBssIaHIORxzEKJe1VBCr5Rwq-uy2m9WJThuREiu5KWsyXN_EeB40uP7bmRtMn760YhW099uFvNnpB2IhYaMaEexrOXThSPwRSTXkOlVxAR3TzQAepUfmRRtBH3e0td5w5ER9qj3dK3EhK5v2pdWkCO3GEHmCeD1cZXiXy_J5u01xm2yCuzbQpbFun93SVwUFjxOVfuFPZgjYkouMNQPPAlA-yvmW1GqB2IXsUe0nCy9oPlgoBrqhgePjYFWSC3wwQOEPvwL-HiY1wGv915-0NG9yJx2T8M0-zX8mvEdLFr-67mo14OJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1aOTLoR7aOyFBbHpE8id8IhJt80CHO81_j9vI0n0gFLNrPmi1CXD4PFS0pgzwa7qhyU02bzt_TQXwLLFyA_6-jKbowQfqyiQwo3hYe3eRi_Q7IP2fWKw8JAPDm54e9884xUpU7HyFQsD4ZM6hCdkAwnRKJAjWYOeCj5RPzSI30yPccywwOFm96ROV0lSaDCZNK0YFAt-OXG8HG7Kf2KevfA8F1C4G39pd21jID6SOHCj5hUcetGfE6yG-oQvsgrLrGJmSA0RRB_n3cJ1nKQ3HsZonpSyda3VL2-7LEOySzSejdEYuiGhDWqAcmWd4QW01tyu_cV7Nm5HAztp_Zb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c31slItOx5KAhMCGoI0PM2qbtyqiqgaCPg114osY-JWOinfj1e0WyDiS6N8bwPRk1HVXWWFjT_4QuJBk801NxMZVDYnlLFlGbkaS57mO11RH0kWfAfe2ovi2wwE7Lb4OKKqvJlRyRgealz3fIuTVFvV1ezsMBeepKbuCFUexpohiN_dtff41s6yxoF8GXgeW_xmPnVNJCCnH541fgzx__y1cr5C645X-e5rzxgOirng4A0ATCBRRemKwllD5OObEPpyfVby-B_GxZX8f4rp3i3h3vCjzklbn2Z8v-i8m_d8XXj5Ulk2JdwgdT1_TQeWgRBHAhlomp_AZ2GgqT7DRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwGcAt5d1BnMXBMqSKpWH1niV_xtZHYB1bQIDrUjPEhjfiWZ-sxh391SmZ_AMGcJzs2Dr2By1o1RF0hAlMRj_TltEWYP6BKGOI4xBzVthSbz8de1g69UY-kYOMqhO0f6OslyHtJIqHLPBhfUVYwtJihqP_ti7vdM3JBpPj65jtEAQzB7E0RGFxjHZKeiYfit_Z7bls3jt3O_zmXp8-4qe2fCadB0SCsZ07b-oLg4qFVjNqGSD-J5DfO9qiq_fgev37Ej2JANJMcw4H7ed5OOXsGImk24FkHwc9TAYrd3ELWNDqJJLvmgv47_gmHZhcw2I8uKYbr6oqk2t6rem5G2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=ZibJQGEYJX67aNaB8i_jyJ_cHwkp3p5-QS4qbTF4H2PUUe45OtfKmr2wUQ2Nwl5eTWd1BdjUO6kwi4AW7cHkFGxoGw59bFSL1BGyUxESwNjc4qClUiwipwINJb-V9YKTepWLJYNl1pYxOtRYWEAMT3kQZscFN2w-qw2xKEZ8qiOPh2DGUqwN2XeIhO2VNw_n1IuwTDxQN6tm3kf3U5mSWnh1YpmRsGbf9dO0O9HRaaiD7RFcQvK8u474Accw0dOscmoxpOCyT1mr80ijJBMD34RazGlui0Pafz8ek5YnOBqBBM4iBxSWOfSC6OBlfdwxjG8nQcqMLpZw-Cga-UtZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=ZibJQGEYJX67aNaB8i_jyJ_cHwkp3p5-QS4qbTF4H2PUUe45OtfKmr2wUQ2Nwl5eTWd1BdjUO6kwi4AW7cHkFGxoGw59bFSL1BGyUxESwNjc4qClUiwipwINJb-V9YKTepWLJYNl1pYxOtRYWEAMT3kQZscFN2w-qw2xKEZ8qiOPh2DGUqwN2XeIhO2VNw_n1IuwTDxQN6tm3kf3U5mSWnh1YpmRsGbf9dO0O9HRaaiD7RFcQvK8u474Accw0dOscmoxpOCyT1mr80ijJBMD34RazGlui0Pafz8ek5YnOBqBBM4iBxSWOfSC6OBlfdwxjG8nQcqMLpZw-Cga-UtZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=cw1FwmrsdBLo3moS90EYsyVhs57nOoSh91VGmYbA_RtueVHar9TIsN3AtT3ukp9v-7Cimt-uEbWoYF_gLVBU6LDH0HCyW8M9nDv2dzlutcjANmDAUrKXjKw6sqHGBROAX5c-7uvc4Q8xD1ftiBtg0YTDVNKw8cRT1PrZu1A6BT02sZKVgMXN3asUf83wcyAuUSVujueXqH2nGSlGm7ZOy2wlw4UVwyUrIF9BlYllhitzC0mT7IHyU01fr0nJyvyNu_LYdCgStm_GwTpz_BlszH4uUGehslJvLpE_VYnSECqDKEa96txGlDUDHCx7NXZU76sYOe8e_MA0VfiH5VSE-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=cw1FwmrsdBLo3moS90EYsyVhs57nOoSh91VGmYbA_RtueVHar9TIsN3AtT3ukp9v-7Cimt-uEbWoYF_gLVBU6LDH0HCyW8M9nDv2dzlutcjANmDAUrKXjKw6sqHGBROAX5c-7uvc4Q8xD1ftiBtg0YTDVNKw8cRT1PrZu1A6BT02sZKVgMXN3asUf83wcyAuUSVujueXqH2nGSlGm7ZOy2wlw4UVwyUrIF9BlYllhitzC0mT7IHyU01fr0nJyvyNu_LYdCgStm_GwTpz_BlszH4uUGehslJvLpE_VYnSECqDKEa96txGlDUDHCx7NXZU76sYOe8e_MA0VfiH5VSE-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=mCLumZ9FBhaTXg4EkNFB2Aib8GVWCL-q1j8FXp1OeASVwCLgzxOafLhKaURewhj2gjNLEn_5bDR0EOG06tI98qzs8jdRbj5Qouau6ip0qEIPxLzGRwXZOhmsOQBh0JmrsdDD1nQLpnmlwSEEs12U1wyP5_DuL1gzVvkDPOGjQgo5NS1i4iVFjtryP7tOqGFDyvsPl4R8IAXa-cZKujsOU3NJAtJuP0L01uQ7yQfbFJEuWrynaEBM4c_ph_f6wbzOU9D9quSC2qWgH-xUmUDdzFtOt8QV4WLB8wZ2oiCZiqx4FxxBDEv-7nsUsqzdNHuyirZX5LpyUdNfsuIB4OEgpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=mCLumZ9FBhaTXg4EkNFB2Aib8GVWCL-q1j8FXp1OeASVwCLgzxOafLhKaURewhj2gjNLEn_5bDR0EOG06tI98qzs8jdRbj5Qouau6ip0qEIPxLzGRwXZOhmsOQBh0JmrsdDD1nQLpnmlwSEEs12U1wyP5_DuL1gzVvkDPOGjQgo5NS1i4iVFjtryP7tOqGFDyvsPl4R8IAXa-cZKujsOU3NJAtJuP0L01uQ7yQfbFJEuWrynaEBM4c_ph_f6wbzOU9D9quSC2qWgH-xUmUDdzFtOt8QV4WLB8wZ2oiCZiqx4FxxBDEv-7nsUsqzdNHuyirZX5LpyUdNfsuIB4OEgpTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNO0Q97Nvw6qn_pDN6rinfUafj0N9aQq0LmvqbhbzPR2_grDEuUwNOG-ArDJ7eGJ2218_4uVPGbrwi3sC-ApCX2DObl4PyxTtSIe9hlAzNLqBR7WDhjvpZzRskchIlDH_9h60ZpEpeeHoescWYivcOkWb0_WyhPZWVn56SrRFDjS_3N5LjwjcymoQNKL9iANDuZkfgSQtqLdIM6O--Xr1h2TnLvc93_Jpbwq7-ZJku8KSoZ6LRQoiMS49FpV4Irj3UwsHWAtl5zGxf_fmvqZgcKTqQ93qb134LgU36wHDACUeXvMZphWfQP8FagtH0atHlNSKH-b2sehYzidgLvxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSyAkFn7N7NIjynWyilYPK92tZIVLArCCZ1H018QqTI8T8QhQuqq1hQKXamIDAvXj07nktgcMWxz9JETacucALBJHpzrRXMbMB5NqIYmcQv8Ill8dGy3bn6bqNFTEYXtgqX66Mesup2kDWiKN1gRRI03B9k0gbGJRmzddZTMApptgv-28u2XOOdtl227j4eb3A_CmFh4bnklA268oUWcROmsDBcCdYVj-i4MaImu8Dwbyap_idsIsAyzjtrRU_DsSRCZrJJNrjH3KkiAd-KB_OaeWVwoPZynUEnnN5CEa5_YcCoSV-KjbJ3Adl8md5bvJ8uBwoGYVh73hnI9YbImdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcrN_Z6i2veKDuIRAUidGuED2CI0kQP3mKfD_u24V4XKE1EkXnNQEAMOnexDPrIP4mEx30WeNG9u_XppwIQ2VLd0APxPOJI0fzadLfwFM8Eops4KX77VFPPuE6Syp3QGAYXVqxpuSa2ycZ-evk920BYlESTgnvXrFDry_NoePGIas1m5GbEsT3CRUUdstFH9WEqnhvKrlMOBxf62G7zqFCBKxGp5-avUSsrevZHn3Rbwi3NvEZNkJx0VxJL3Og6VGP7NRy3_zgjtVSzy5c_v7vCEg2xY7HXseHbVBC34ZKfqElh8cWa7o4to3F_jnDfYDHiqndFVnn_xXUSVU9_eoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZwK7Zb63sGx--AjSA8BXq8MWK-E5k4EH0aTuJRbd76AzjODUAsiKFneGsr98KpSxR2MblMbtsQb-u-87ggBQfWJaqboDulOBmLoEqtilj9Oj7SUOi2x_kfsz9BlVuVtlovUfoUZKjPNqpv9RGWoH3OwN_s-eFGg3VXPdwCb1wNIxhbBCTWRIqYzmXfdMPLaaqjIFKzxyjA8RiXxaiPXa3q2kWFc0Crvc_Xfj2x6j6r3qKiXjgSo7XYi_6wGeJg3wIwffhAWLX7jweFG_F-_-X0FhLrQiaM5gmkX83GijkQfV8vYQqG1qTD333HkfRkKhIVTA9Qbz_qZTAR1prRN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyaaSezVcOKRfJOI3ymSNk18YQQMH8iusRGs-Jc274COpwoDgHBt_HU1D8WjteFf6SICRiVCRwYZt-Tts_Gb8N-J6OFhdXcPzTQeV1N4JKJj-TPeR2DCQLsGObCPu4UWamRngrn2va_FUty9jHfFs0hSiZYFnFszrFi45KXJ-aZEJfWL8ARSFzKu3QUXNzXTZAD6vrxfTGSGkw4APTRJFfXB0E0PP4q2h8CiwqPON0PMDucN1eqxKCVhFr6zUDJW2prIsBCqHW_4uGxH0Nqgze11qcXlaau56nThWZ4LxTZsGe7WEWzk0Qawgp1t3nYI4Fc_dnYa58F6VwlSWF17Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_L6xSgKiSJXWCp9cC0Av98fPrqlvlCtC6dozIK5i7AplBYvNPg5u5v_4xQARBMZe1rtZdtbx5ZZfXXxdhKXFV-Uo_ODMs2sdBA4clyTe0b9aONI_Qclc4xoeFfSO_V82K0stZ42iFuBDDwkAXYFM_l7wma8RDMQCSokhj3v_JLuuz9bf2h9XeRgjAVX9UhvXG2kQFimDZJRmp8FLyXPf1ynBcQl-m-elHY0zNg_ZAv8_o3ppMW15ZRxurwkfRA6XNvfpQdMz2edzqRENVqJ9JTbO-xaP2hk4prfLpF8FkIdYKMlCCqc2tvDODgD94p2-yPq_nfeiO3OIGkncrqKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgN7Yr5eiOphDUsWIqULfuTMd5Fv6CPB7z8UyUu5ssvayBIKXpFSjV7LoDDKtSrQFBSVBuAOdZA_o0wVMfq9aoi0MkMMN64UzmnMwO6TJ6xRUEzDz2V2gIHlVScx6oskqSQuHXJQxocsEspy1nsJXerp96wHVXPlovL3gZRoLg58ExQFRhnFdsiqlPxOP2J38PVYjUOA1FMaBvalrvlfrbPkKwqRNGBcrZZXL-tIr38rrr7ymTol9jeThBWyz_R_TUDXsnMt3CpIPwaUKXyB37TfRg4o04ISJXdSqkiu19alwfQlyBri-1B6Zdx-eNP59bkSZqMXy_z0BaO15CzCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuSiKpndCVpHYXGfkeBeWMRge-lK0rXyoAoVlqaeyG8Z3s4TWfPDExDuC96JA1Hd2t4TV5POWvsH_Eh-NSdx3x3uhQtfJewN7MYOk0rm4kkFczXAgRKYIOOaiiI9oDjsGMY9KoW_OznSd-dxulLcYRFTeSOH8qgd9A4BQeLzXV2nm4BLPUG5biPd4nS-yDAwzVB2BruW20x1csIricZ4HVDAPyPCGeskAoYplTw-NTUI2g1JJ1HLZ7a_P1dibrluzJAjdC1lOtRiyZB8Qv8kagOoGlttLxiRY-vV87kjXSx9-gwKW1Z8fwEBPKz45zrwVoh0eKtJW_Flx4cSYtzmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbgJJnXE2P-0umJM5VwJRFofp0KxsF_KRhuihfMHQKGvFzkg4i2zAdvkg9MJYb5HXrBK9gonMNmQxdZFRWM44HrYHqGRjMSzqpoqfwhxh-xCS33oj7dB4FYhXC-4O3NcMTcMFOlLRIvueN6jsoo_OWsTC7dC8j_t5Q86ewakTDsthN_tpsjMbFaE3LWeBY-fO13Rte6TSIliJpphXHQSBOUqBYrKM7oD7Poo2DDzcB9fob97X9O4_jli9G9szl8lKlCsDef3DddppJX0MdHJNFtCowgR1JBEe6VlGtw2XejCRc5rhBD5Ca7pRLb-y4_v_pGWe244CtspMN5jYctjcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=QqTovnM1tEz7fj9KjRfInwvuw21lqu-zCl71Cf6Tw3673sZrCh41TlOUZYpJTnBZm9aanYa8coO8KhTlYdje-ATHQdMwWdwaTaS3RTc9JOI2c_aGXJjBu1yAT4loIOfdQuxCwnRUMIzdjwEiTznV_mN-uEgJgDLv8TsFy8ztpcK7uPBijrEOx3pGaE8hP5zVkXjz_Bk0zH6Yu-k1UfPVKESdB6euH8kXg77gPUX9vYfTtXCQbkqJO1c7AF8ScXRPVajrZ1KXZIO92r9UCBg9VUzBLhBUR3L5uUb1zl70XAuh7UTbzKcNKDnDn2rtuUDMOKVFrLrm1QloLCwMGXRYLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=QqTovnM1tEz7fj9KjRfInwvuw21lqu-zCl71Cf6Tw3673sZrCh41TlOUZYpJTnBZm9aanYa8coO8KhTlYdje-ATHQdMwWdwaTaS3RTc9JOI2c_aGXJjBu1yAT4loIOfdQuxCwnRUMIzdjwEiTznV_mN-uEgJgDLv8TsFy8ztpcK7uPBijrEOx3pGaE8hP5zVkXjz_Bk0zH6Yu-k1UfPVKESdB6euH8kXg77gPUX9vYfTtXCQbkqJO1c7AF8ScXRPVajrZ1KXZIO92r9UCBg9VUzBLhBUR3L5uUb1zl70XAuh7UTbzKcNKDnDn2rtuUDMOKVFrLrm1QloLCwMGXRYLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZKUqhvjvuo6tpPGpWNjcx6Vz45j5f74L_WrpE8OePlfqY5sZE7nt_Edg1kRa1pwFDGo9XtWYWLzLRjVsWPbM0-wvoqn1a9v3UTeEIiQzhge7N-tLsCmjIh0GxENT0j3f54ru_7Xk-TEfJtsIVZO1JJwWsNl3YS3T_-SB3Z8d6dwNKydQMtQFVvBVYYzxp340MIGvgM46Vuffb0rbb9B0IH6g4QA3AiU--2NLalkhQGtwYwaL4y9qDE4MgInNBDuR0n4B4gdVglCZUqQWmP15JD8RVhvtPediitAzmZ__Cc5104CqDUl_j4jy88smQY0c-hHJSTX_5NMQF7RSv9snA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oL5z05JdiNnOqclV1DTYmVMdg8ihPuK0wIzXWad9TGzzRtQq824Rlfim-_OHsRo1YWeP4pw-K7GszeUxhNd8KH9l2NWVpRF80rdK21syBzG4MgueWllzWV4I4XLatktEDBR3cH1QfmoD2BCTcrhyTFuNRjkyrK-3N9UXQsch06EHVAIrJxevjdHH79Mbmwb5dxPpPryCsXaIPdNJdT6F0_TQY1bLxpr63dz9T0SZ8FsOfWysK7TaFIxu3xY21vgzsrvwwLsj1xDQXjynPLjAeYQPlI7be2ONpiAFNmY5ov8pnH6jrut4Py2Pybfhg9IrHPYJ8C3MbGUnxAGGNS93Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNHYAulvkFyYRi6M9jw2_00ZqUOCGLnjDPRwGlus3IljtSrjLGNJEkajr3dx5zlzGcnQ3vbktC0CsBY-SYBQeArIW5oEHwipOwoWvL5LvUQJ9xHN2wN9FLEfEavcMyyrQZ_43ox2aGje_xEEtCMXHlR6iWPb065qM4RK3FrkcbGSnblAzUi22qZCS_zImivLPqk-PnyzU7IdVO4LYTvZi_C140nTAeziXk4PXm3q6puMr6PIE-Pd16MR9ss54eNnjHAppK978gWCKQruYhAT9R1cX3q4VZFQ42W6xyTOEuBhFK9ALfG5x5ybLz_tXyRRxrTyTey2o2EUPbGJeySCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HisbVeSahb70e2ZigYjCr35ZKEh6A9rok1ugcATl5XmD_FvNIF2ABEy8QxL1hIPJbCcb9ppweIXDHbb9C35dyFH0DsEmqVK1KsfRbQp7V_b0k6FOzqG66jauBZw9tnpeyogSdFVDOsHhco34Xf6OOm_CuRmES-_N82nMwbqnfGYblHUw1AykzE3H4YbBCm8zDc4c-LT8oqvIURG6pi-CQr4hLMlMZboC8mIQjubGSn3Axic_fgmpXICipaKZ8gcPwOhZJy5j26LszQyYVXyQRJB1Oyr08aHt31YbJi4kE1xVNHZF2V0oFOyvEzpcoRkARcZ2lM1pvS0tSnMjL3B0Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=BrUEYhhc1iSnnPb8MrIUjE8hP8HiFyZDorUaxlATwQj-jIZWkxEhlPdu1w8JBbymujgPGP14-o9Xve-eEBSCAiyUAbaCHv8_Ffj7bEIqHYb2t06GdqHCce5Zi9xwZLLl7zw6vH0uzXznl6Q0Vgsg-sEZON59JK8WGbonCHByp4bPrNRWPNpKgHkC14h_79efck4HKubX3FRaWGYDJ6bGPI_jCY9oTcO_t0AlBfsvgEpmbfNGoyvWyMK4JD47nUCRUBKBP-ZAQE0b-niCp1aXRVl3Hq9iAB5LWEmIRmiNCh4m_V_ftbPRU0rb0U_qDaJleUwV_9Oi9Iv0QZ0au69vtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=BrUEYhhc1iSnnPb8MrIUjE8hP8HiFyZDorUaxlATwQj-jIZWkxEhlPdu1w8JBbymujgPGP14-o9Xve-eEBSCAiyUAbaCHv8_Ffj7bEIqHYb2t06GdqHCce5Zi9xwZLLl7zw6vH0uzXznl6Q0Vgsg-sEZON59JK8WGbonCHByp4bPrNRWPNpKgHkC14h_79efck4HKubX3FRaWGYDJ6bGPI_jCY9oTcO_t0AlBfsvgEpmbfNGoyvWyMK4JD47nUCRUBKBP-ZAQE0b-niCp1aXRVl3Hq9iAB5LWEmIRmiNCh4m_V_ftbPRU0rb0U_qDaJleUwV_9Oi9Iv0QZ0au69vtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeaVL9-droRpjioIIfEE6viZBtoQJqjzxBlRB1ZhDxSQ7myqVuP7BzkQVPyS-153BGWivvD6FQhS4ipFWsRJy0C47s8Dfi7x2BoS1cCIXeOnQ2eswkfO_4_Yx8pBP-jz-_zpxuATSiyNXkhZ2N09jcGCoAtHU6H6HMkN0565nhaElcLgi6dpe4Cagoos_hmtrLVUsPfLLD2ud0pyLk8AO50XqELymzrciZYtlUE62c72Kp9WjchM2ciL0HAhSYvmOPvp8y49zNmi6VZH33rA-RXbKikzUwcfpPSlEBbhyjZTgCqk_il_Quyaj17B--x8TdYD8W_bRiVeW8kBEw2rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=b1TFbrfeDHPf8duL8DlxLpTvB8NSTfZcnygjBsUzOJ3ztKLRTAj5u8QD5Absd6WMptdV-AkRMRU76FJgp4Hz18XN4EJi_vPaPXLaWcCLHrb913SVwUPRC5jb1I9LDfEpCKlzm8rqKq08g9JL0j2nnfQWarkO23xlkBrJ3-BqOnJiwDj8e1OND8E034kwJErbwJRsT2Ygh5KJrSjQh-CmmC5tyPmNBnLQ1m3cH3iJ2A0kF5dgIBwvtRXbC1aApiwzjGRBu3MhDZou0DYNaA4yGnx-qrGJUcuwEsZutL7_PtWk_PM6Fy3KdeLPpl25iQc3WYjlwVDs4bB4BLC9AVo8Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=b1TFbrfeDHPf8duL8DlxLpTvB8NSTfZcnygjBsUzOJ3ztKLRTAj5u8QD5Absd6WMptdV-AkRMRU76FJgp4Hz18XN4EJi_vPaPXLaWcCLHrb913SVwUPRC5jb1I9LDfEpCKlzm8rqKq08g9JL0j2nnfQWarkO23xlkBrJ3-BqOnJiwDj8e1OND8E034kwJErbwJRsT2Ygh5KJrSjQh-CmmC5tyPmNBnLQ1m3cH3iJ2A0kF5dgIBwvtRXbC1aApiwzjGRBu3MhDZou0DYNaA4yGnx-qrGJUcuwEsZutL7_PtWk_PM6Fy3KdeLPpl25iQc3WYjlwVDs4bB4BLC9AVo8Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOk6HWv5zORJQqY5lWfftaVrvhNtO1DX_up2t13b-_d1JPJnuHX0c8MMpW1o2ncE6saPNrIHhSIaxIAH-Eb9lC6D5-94A3qOa4F0TKIqrcR2HeRaSMVFV8LwNdh8eCmlaba_Oj7a1wolAXQOHjg8Q85MeGUhP60esnCU5lHg8nvBjenXggLJwj329iV5fdmg8zbzdPKgqCq4lOuKw_cQ1QeB6rGBRJUxw4kt_GjdemQC1y0c12qx-J0fFXMz7qIeqL9h9qEXrhfzlO4vBkwrtc-HYX-lbbqZ_YvluEQD6Uuk9YMIY7cFMkmtVU2oE89eNUeROJPTdS0OwzCc7g94Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiVAuHixw7v5oF9HerixyecehH85Ifz14uOtaYdLyJywA2k2V2AApPcXCp5XXkvUD_x9DZcdCI22vIXish7-MlJP2S4rwAbTYrTi9DIgSi7yPTesd9amCbwHkiASsQBbMtMJH4W946j6_os8lKs-265os_RkZq2b0vjyuGdB_r3lEpvgdchQPqp_PNSajMsIkIq6jsnwEsPEkapfqomWilAQT_hUWadGVfs-nQiDy0csCYeo_WQEAmBRQTFBOh5WgHudvTVzOEJt6qc5Onv6HP8ipsrrT1ICXNM-4x1skKwoQypBjgnCZ8uFgyXqaIAWRYfX5LiTqtYf1fYR3wsTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=ermFK39ibV7qR4VfapSdz6Li5VQvCt4Z_mIsnLb1DTam_7n8y3GCd0shQYklsgnumWuDg0UjS1ypriQWn0NBMfuq7vd43tsePHRvS5lVO17GPewpWC9N0BvykJp-WzTb5Z1hb6mMHZ57KR1TE2JJzkihfW-3tf7bjzo4JIOv4Brm2UDmETlfF6J1OZmL9ERUHKSQC6TTxZj0OqaFIiDnILFnbdNpdJ8j_7kHohWTixYp8eTnTbhXvHvYuLCkjDqSJ3SxF51U3SzxTmueDGWzE8ZXb8qPsKTgNBaQTxKjyqvxsRocSDc5dfeD2nCgAdgdNymXxQ9yXnLkN2dGJMHWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=ermFK39ibV7qR4VfapSdz6Li5VQvCt4Z_mIsnLb1DTam_7n8y3GCd0shQYklsgnumWuDg0UjS1ypriQWn0NBMfuq7vd43tsePHRvS5lVO17GPewpWC9N0BvykJp-WzTb5Z1hb6mMHZ57KR1TE2JJzkihfW-3tf7bjzo4JIOv4Brm2UDmETlfF6J1OZmL9ERUHKSQC6TTxZj0OqaFIiDnILFnbdNpdJ8j_7kHohWTixYp8eTnTbhXvHvYuLCkjDqSJ3SxF51U3SzxTmueDGWzE8ZXb8qPsKTgNBaQTxKjyqvxsRocSDc5dfeD2nCgAdgdNymXxQ9yXnLkN2dGJMHWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6pfLQk21xCfKytTjRzDyu7kcz4OURQwIwqYVxoO4B2QgzZ1GTrmKi6t65Y1YSud1ay_c5Om_qzUKy58yeR4xiCYtNwFP_R42d3OYDwI10TKkeC_ZjvovisjQ_2FEI5hrb3yPuid0tzug4pH92ykOgyLesAoe4-pdNvydpqlZL4FywNog5YdM_vI3v20XLb-FUXzeotUxgVcoeaexkb48othDPCi6ogdtHCkaRvzJBujdUsjXQQv2qpCo_Xtq_Ap2jtCX5NbsLsEiPUjtr8luErAZMWInfdT1HNJKhcAyxjU-9P5kGlHUp1Hcv27i_tYt0_tjcoCi8TjlN0SRFmnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=rC0VG5_gpFBXWCtgbDwZDtEyTT9JqfaqP2_WnFr_dJe4NQ41USnBJGYFO2YuUoSRpFsQyr5jGLMPr8SYeHbcaI92rRFd71S9Vkp8gbbugyrXIrOzE3Ppq-CJDgfm-Ea-7Nisne_UXUvUrRWTtP3MDy6hkHZWYcl_wK1HQapFefpfqAXCF1bleLweZbr45rmgbyxvhtuclGGdP5GH6RHCLtC0JTe7I-FLqVO-vjVAaRhrh5q6gyeaobVEm_8j_3c1iSAmF36LYmW3yV3i32wJxz9j-uopbsKBdteP-whWsiJaeBgNyvLfBwQGiPMfDkR8Oirszvsjlko49SBZJOfqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=rC0VG5_gpFBXWCtgbDwZDtEyTT9JqfaqP2_WnFr_dJe4NQ41USnBJGYFO2YuUoSRpFsQyr5jGLMPr8SYeHbcaI92rRFd71S9Vkp8gbbugyrXIrOzE3Ppq-CJDgfm-Ea-7Nisne_UXUvUrRWTtP3MDy6hkHZWYcl_wK1HQapFefpfqAXCF1bleLweZbr45rmgbyxvhtuclGGdP5GH6RHCLtC0JTe7I-FLqVO-vjVAaRhrh5q6gyeaobVEm_8j_3c1iSAmF36LYmW3yV3i32wJxz9j-uopbsKBdteP-whWsiJaeBgNyvLfBwQGiPMfDkR8Oirszvsjlko49SBZJOfqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If6A6Yx_F-_n1PrP-NCpZ3l-pe-64j1UVo03kLh_MvucW2eN5VX89xlNlXMlcnIvn2adSiGD-_itjvRFCkE_7-jwrlaVLoGHMtGUCMex9RBy698veENNP0sj67QbnK2N27Ysyrq02UftAiKHnG-vFJTKe1pMvfgJGAqrYH-wyoI5mcpFZrKL8E-Q0ULWXsETytKFO7VBDcwbsvO6UhC_0a_VudtqGqFIuWVqBXNGOYEUNSYb_vy0xD2WBGasoJsoq1A4qVajdGklhGS-6EAhn84JPIEdrYdIeqWlZu1t6vpfuUuGhb1bRn9Xmq8vzf-TsN62AII6lMWuNL7tJPMYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDD9apN7duR_jBcgL57NkJNMlzMlU8hME88OgoSI-2Pis-lutzPGra0R0tYzxT1oWIXBE2vyz6cCMXCnL4ZP0qKcaWCKRF1gh-Qiv_Hhabw6J6PHfalpjMMSSpqQxVF4MHYrfcYfCqJkJSuDl-346j1baLx28ZFU823o1tPk1hIS9AdR5U26XnvHeJ8FJ-TapiXYUOVtadE4RbkQGmb7Ooxdsy5iEHaH0okTyomC7iRdA5QZsJZ3xf0ekqP2Z2aDP-_uWktFiHCXGfzE-aZ93NErja2_nrFDF5ywJSLbA22CV7LKX4sWvbEgej4ptR1i4zPlyGzGukJ67iUhPGYUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0KOEuB2FwEiRWPB5XbVJBDi8IFrCUlyNNd6DcBdO4QP6XIehgDbfYfSGesqjTw3a9icwWFHriti_icERTdM93THp7oyxwmfJlQ1hXdk6CGzuipxWybscxFfVk4pX5a4Ivp9S3fkO_m8zCEsL6Eg1h4pMw3DC5rRluNy9VUjgGBfyqftOlXoOe23DF7tea1JE6FbeBBgOayYacgdsf8Ui2n7HAxqi8ozyPdTOzfN5uCDH5p3B-aCTFsb2jirTXauDLLFgVep_pS9AWsGgfaKVyH1dHu3NenMY9tf8GMaFj3DtUQXRQbsAYhzz6jqkLCxVGCo5Wfceu-9ulVoR3y46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=pm_malaFfpWJ0wAylAGV_hCOekgVDN2oczYzBlxHk_FnxBHPiAKKFJSwjsIV3pgZr1ogs6htaceVIB8zg4pcIlTcKigBEYM0vMJxXr5P-5uBDwvUUWj3UEldVZ-6V3-6mXTj1KmpeDolndOLkXzfmW6dhWj_PVZVobdYAFEAD_QuZt_nyIIUtOismwEnEgvXryX9K5DPw4-NqSIAVOOIXoTLSwiS86aOF-ILGaLzadB7hfCVyQUnEVZpEXq9whpHLAzV9h-8rSbUWnlWDy_PKHyPKlAjZF-C6t0ii5aB9L-lpk-emZoGrckfORwxCJXI02hzICnELEVCLezjiuXfDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=pm_malaFfpWJ0wAylAGV_hCOekgVDN2oczYzBlxHk_FnxBHPiAKKFJSwjsIV3pgZr1ogs6htaceVIB8zg4pcIlTcKigBEYM0vMJxXr5P-5uBDwvUUWj3UEldVZ-6V3-6mXTj1KmpeDolndOLkXzfmW6dhWj_PVZVobdYAFEAD_QuZt_nyIIUtOismwEnEgvXryX9K5DPw4-NqSIAVOOIXoTLSwiS86aOF-ILGaLzadB7hfCVyQUnEVZpEXq9whpHLAzV9h-8rSbUWnlWDy_PKHyPKlAjZF-C6t0ii5aB9L-lpk-emZoGrckfORwxCJXI02hzICnELEVCLezjiuXfDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=GOiZ_PTsRWTL3iOFDvnImd6wzKgJJf_-6jAf3mMCK0Cx2YbOSwuUPatlgFFifcena1W3Y3pNLJ_EFKH4OYJXRCQKyAh9R4kLFcbqm2ooVyt4WFMsjMlBzLu8-AsrKmdCe79l3hc6VwgrKNhN3WrGQzpe_qGteJ5aRywg40EszRnfVJRYq19zliS4xENZSz_WBMrrVZ-dgBY8TLxPOritpJ8y6bLKHew0wtJa4Q0xgajw5uUHGsSP9E83bckvXAKnwYoAqWBAbV0gojLBLcwkrOmfaj7E7tL4zsJHtdG-gHydO0_YGihGSzTJJAp_NdjaWa9Sgz1zzowOGSBUT3tlbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=GOiZ_PTsRWTL3iOFDvnImd6wzKgJJf_-6jAf3mMCK0Cx2YbOSwuUPatlgFFifcena1W3Y3pNLJ_EFKH4OYJXRCQKyAh9R4kLFcbqm2ooVyt4WFMsjMlBzLu8-AsrKmdCe79l3hc6VwgrKNhN3WrGQzpe_qGteJ5aRywg40EszRnfVJRYq19zliS4xENZSz_WBMrrVZ-dgBY8TLxPOritpJ8y6bLKHew0wtJa4Q0xgajw5uUHGsSP9E83bckvXAKnwYoAqWBAbV0gojLBLcwkrOmfaj7E7tL4zsJHtdG-gHydO0_YGihGSzTJJAp_NdjaWa9Sgz1zzowOGSBUT3tlbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=VlydAEhQBBBh7RsN7Tm0YLaGTNBl2csUf19K82BhDnQH_Mb0KuJUD3Y0aB71rHTr7Dp6rXAR9OEoEmh7l7p9MlOs74Ojn8miMK6vmlAzjuAnDEsw9gx2WUwU9Ubz8371cXyPBM1XEySgXOLT3YrJQ7J2DmOWZk8UGORSqqWT5qMupdYJMNLQDAl9_GhY27wwKpQNXTRjfctoMqbxtI9SufxdKkfdPOXqx94TM7-Zs78Bz3hKtZOhK0tmbLw3AfYgZ0nxhWKdAFy8eFiZiUp6y5ie8nNToAqhlLaUPU3AcdnmCqW_pMOdlAt1y45liNtt1YDO2JaHLh53eaqW2hiqwU58I1wNwHfQf6o59JWbGn0GtAS3iNkjOVWdl56MmMtVvRnGWdZDYOFXbhmH_qBbkbfUqt_sgrgVbHr2FLRmYuEq4R9ukfryiGNDwStrQ_jCNS0uInE9iM4sCQNEHuzDI-BXTAt8FDq40Xn8nEilHyHksnTbYghJ8Y_ZPuRbDsgRCbni6fKFcqF20kLBXwKeAzZgiuLWlKZ_i-K1cWk1A6tPcPBx-47yUgk1i5sk2vK81f2XI6nVGtwqVTiUoIw92uvbdptcTBnyx361-bc1Nr8S0mninc_1HXLjEGyY3mUnqkLLQWVVUzQdhNyAUPgXVd_cXBF9rzD-YKhPUnMEXxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=VlydAEhQBBBh7RsN7Tm0YLaGTNBl2csUf19K82BhDnQH_Mb0KuJUD3Y0aB71rHTr7Dp6rXAR9OEoEmh7l7p9MlOs74Ojn8miMK6vmlAzjuAnDEsw9gx2WUwU9Ubz8371cXyPBM1XEySgXOLT3YrJQ7J2DmOWZk8UGORSqqWT5qMupdYJMNLQDAl9_GhY27wwKpQNXTRjfctoMqbxtI9SufxdKkfdPOXqx94TM7-Zs78Bz3hKtZOhK0tmbLw3AfYgZ0nxhWKdAFy8eFiZiUp6y5ie8nNToAqhlLaUPU3AcdnmCqW_pMOdlAt1y45liNtt1YDO2JaHLh53eaqW2hiqwU58I1wNwHfQf6o59JWbGn0GtAS3iNkjOVWdl56MmMtVvRnGWdZDYOFXbhmH_qBbkbfUqt_sgrgVbHr2FLRmYuEq4R9ukfryiGNDwStrQ_jCNS0uInE9iM4sCQNEHuzDI-BXTAt8FDq40Xn8nEilHyHksnTbYghJ8Y_ZPuRbDsgRCbni6fKFcqF20kLBXwKeAzZgiuLWlKZ_i-K1cWk1A6tPcPBx-47yUgk1i5sk2vK81f2XI6nVGtwqVTiUoIw92uvbdptcTBnyx361-bc1Nr8S0mninc_1HXLjEGyY3mUnqkLLQWVVUzQdhNyAUPgXVd_cXBF9rzD-YKhPUnMEXxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB19MmgsNTogTm86mvKji1R2uW-sIGxAnAwiIo-cYOT1a7-c9z1ljfPlvce7ddjBFXogqCsQ5bEQ_IRqjy5hJ6K59j4xGC3rFFBNcp9lG8oB2zWBUYb3oSDp2DvAO3_eFGf0Ja9ae3ZayP5flXmNygVUKBdhF-t4LHXDoSi_IRfRMtTUa4WanBucGnSWRCyA2-dD006HnkO6nq4sCNPwEE5CUkWOtN1mSOhYgETIYaAcQ0VOOHx8zFhdRDoadtduFGLT6rnDkt4Pf5LnObLXgMXztZGPWORKUh9aRdLcXu5-4Q9E9YJwkME1JhtSB5WQclOLP0-SpPV1iPFiCS0Udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=XGRdn-LiERRjoR-zKk2apk8akgIUef1WGZRccniv_5zzKWLCEsKC0409mAkZxha9ccDB45CdGzFXl_DMAjY-uLg78izlan9VR76wCsKFTGKO76fD5Qzdbp1tL83jZGBJwBdrv66EBN5om43ByIaVHuIzdkNNFzwi6BTP1QG7QyRip4xcOfTZQyTdUNJ73T5iDE3GkFFUxRcYzkxHXQffrQyEz_bKY4l3JaHcH7YVrUfaq46bnJD5g6UVcda8Hwl6i15akY0oQoAOLaec2A9i7HcfA4sTbY0EWakX7Ipyv5dJ99tZxHBdo1_2BGvosy5felu3qMGSOpeuhovcfAB2Gbyaus8Ze0akh7MUm7-IzfW87yNfVbd33kpzSzmUH77Cbwo_imwjjqncWBCbigySC0NDlQxd7L7uaEFJu4A4DdbyJUTCMQaoICvM3cyCzcy95qwL-gKnvNpIuSz_N2RuWHj7EsSCsUIek1SHxrk-4x5B23ju9RaTva1BXQ6N4kfQrLUOryEvdozTtBZzDZ2BC5G3xgqxrMKQqyTRwaTBZBrPwsFuX3jVsEGePzPVAUajnTyshwnmX0X_NHcZiJ8GfaqOkYTP5qt3VpFHlroVICETr4imfsZspLWuH56pZvhPavtrR3BoH7N6l_Bti19gkhJqR6qJwjhFFUcFLtfUEeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=XGRdn-LiERRjoR-zKk2apk8akgIUef1WGZRccniv_5zzKWLCEsKC0409mAkZxha9ccDB45CdGzFXl_DMAjY-uLg78izlan9VR76wCsKFTGKO76fD5Qzdbp1tL83jZGBJwBdrv66EBN5om43ByIaVHuIzdkNNFzwi6BTP1QG7QyRip4xcOfTZQyTdUNJ73T5iDE3GkFFUxRcYzkxHXQffrQyEz_bKY4l3JaHcH7YVrUfaq46bnJD5g6UVcda8Hwl6i15akY0oQoAOLaec2A9i7HcfA4sTbY0EWakX7Ipyv5dJ99tZxHBdo1_2BGvosy5felu3qMGSOpeuhovcfAB2Gbyaus8Ze0akh7MUm7-IzfW87yNfVbd33kpzSzmUH77Cbwo_imwjjqncWBCbigySC0NDlQxd7L7uaEFJu4A4DdbyJUTCMQaoICvM3cyCzcy95qwL-gKnvNpIuSz_N2RuWHj7EsSCsUIek1SHxrk-4x5B23ju9RaTva1BXQ6N4kfQrLUOryEvdozTtBZzDZ2BC5G3xgqxrMKQqyTRwaTBZBrPwsFuX3jVsEGePzPVAUajnTyshwnmX0X_NHcZiJ8GfaqOkYTP5qt3VpFHlroVICETr4imfsZspLWuH56pZvhPavtrR3BoH7N6l_Bti19gkhJqR6qJwjhFFUcFLtfUEeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlOVJ5mKsUV3SlR2KfoXT1Jurv4nO5NtF0bcfwHLdnfppQENoiJYd2oKRnIBCbxuSFW8U0oSNFeEuiAmZa40Miz5MHVtZn7sSHB5442JgpcvkzX5QbOOysptgWbAyirP7H5x2CfYFHt4GBjMRWivi89W1TcVNP3EsRkt0ow6KxWWQc9omfUlQYnzgjYjye1ZeEZktE1GlAJWD8u8X8UvjZqpyWmRiQpFOsdzP3nzMdPeLTXPu4UkQPGjgKFf69mMzKNG19lLntuJJN-LGcinAORSP0dA8zTEqllXh4hgkToHJY5HGSjsUbKh0jmaqQ25YLq_PxdgA4DJDmNxyrrtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
