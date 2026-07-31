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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 984K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت خارجه چین کشته شدن یک شهروند چینی در کویت را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/138833" target="_blank">📅 12:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بی‌بی‌سی: در ۲۴ ساعت گذشته ۴۹ هزار نفر از مهاجرین مراکشی از طریق دریا وارد شهر سئوتا اسپانیا شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/138832" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgL-dGtmiSAveieYngbyiBwgZ-b-_-1gQlcZRWdQp6uMB6IHwMp3I7GwHFbKMArSQrlCFLBU88bsXglFtSn2skx9DF_HoEhjLQCygzbe-s5GVG6-5-EqXYF5kpfPFKG4taD4vPPk2dAzxkaKEBMGExutnwKfE8VYLvdfcU01cUo5Ilm0o8Ss23_SjjjEMS2uq_6c3iUe6sGM6owUterm6fPaDS513uVXdVdAE9PXfcYV3eX496JiXVKrWCJ8mFrw4aoVcL2ANgdzMPkiFbay4NJgUsJwpulZOq3HmhBjiy_N0JEInPkRZLcPxtRjGYTIN--MKpDwEXak_dA_Q8XOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووری/زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138831" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=vUGvwX3Ck7R7daZ6SPMaJslk4YcYa3CqSDhxFjpDBtK7QwEY82HfMEI3g_BbnQxbFSeHI0hycjDFCHFtBZzO6_CSk0eJI2ACpGIljLzZitx19YtXKJNyiWdR6-FzoA4VJzHePGcNLIKIV5vWz0aGpd-xU-xkcw17_MVrA5zNEl1TBUEvVkf6YA-XxTXBwL2Y28cTJ5UrIJ2Qkjw8V8uaxm3WpD0vmtFyCUx-7Ft38ycPTBFEwCXOuXWwF5aCeAfwoVNAlESH3PBraZQxZNm1v6njT67XUEpVI5t3a00gbDy45on9QcTioLD1pP9nc_uDivgx8x6GDtPzlLFgbScKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=vUGvwX3Ck7R7daZ6SPMaJslk4YcYa3CqSDhxFjpDBtK7QwEY82HfMEI3g_BbnQxbFSeHI0hycjDFCHFtBZzO6_CSk0eJI2ACpGIljLzZitx19YtXKJNyiWdR6-FzoA4VJzHePGcNLIKIV5vWz0aGpd-xU-xkcw17_MVrA5zNEl1TBUEvVkf6YA-XxTXBwL2Y28cTJ5UrIJ2Qkjw8V8uaxm3WpD0vmtFyCUx-7Ft38ycPTBFEwCXOuXWwF5aCeAfwoVNAlESH3PBraZQxZNm1v6njT67XUEpVI5t3a00gbDy45on9QcTioLD1pP9nc_uDivgx8x6GDtPzlLFgbScKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی هجوم مهاجران غیرقانونی که حصار مرزی را در ملیلیا  شکسته و وارد خاک اسپانیا می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138830" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138829" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا در حال بازنگری در حضور نظامی خود در کویت است
🔴
ایالات متحده در حال بازنگری در سطح حضور نظامی خود در کویت است. واشنگتن روابط مستحکمی با کویت دارد و این کشور را شریکی مهم در حفظ ثبات منطقه می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138828" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9Xq11_J_6S9-CkbaV3Y-QZ7yZPUrasBFWwV06vJIQz78AkjLbLHx2sQjfiATG_YqAiZJ8XLLmft-aaYVlHplxaXzD3WJ3fgua9QNOzrfeuyjI1_ACmxAug0jyrA67y7qHA9-_AqCUfPDYxyYaFuPahAO3KqGE1_1gL2U0klt3MQsJTHl9jQl8KoFH8_LjRz4EDwhh57PmGeDh5rd0PZYgzZuQHAd7flThq37hp2oT2euKub0A6Aw3C1JZfHHN2-TUzqUQFBtf3i5fC1M2tsUJBoKvaqNZ_hrVKhEXM6GDnkLz_m5In7adicSooJtCOzuTM0DhAAqU11XlOBJ5-IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
🔴
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138827" target="_blank">📅 11:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یک مسئول حماس به خبرگزاری رویترز گفت: توافق غزه باید به صورت مرحله‌ای اجرا شود، اما اسرائیل باید نیروهای خود را از این منطقه خارج کند.
🔴
پس از توافق طرفین بر سر متن این توافق، اسرائیل باید اجرای مرحله اول را آغاز کند.
🔴
همچنین، گروه‌های مسلح مورد حمایت اسرائیل باید منحل شوند. اگر اسرائیل با این توافق موافقت نکند، ما آن را اجرا نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138826" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=D7_as1YvZTPge_pNCbrbQraNyxt6YzRcxYDcpf97fp3PHj63eKWjdSqaVGvPKv60eVTfqDcWf-FS36rYbuUDbke55eDirUEYe_9FMiZUn8K4h15vzRAHRnIOAWmVxnjGnngMcd8BqOfhkleyIurtvokG-46UQlnX3KBwx6aajBA7-sC7q_bxWcoSnmqeg0WcfkquOhSU44lKCo9sJPvvrffjsFgJpncmAsbwcPJOy15Lv98tB_nwIA6k-SiIzrSB-6vzmRAF-teTJkzc6uPz_eC61-gumNzSrJA0hX63sGstTc5e5U0XUjmxHpkOh0pESNzXnX_TSMgyw4bZh5SRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=D7_as1YvZTPge_pNCbrbQraNyxt6YzRcxYDcpf97fp3PHj63eKWjdSqaVGvPKv60eVTfqDcWf-FS36rYbuUDbke55eDirUEYe_9FMiZUn8K4h15vzRAHRnIOAWmVxnjGnngMcd8BqOfhkleyIurtvokG-46UQlnX3KBwx6aajBA7-sC7q_bxWcoSnmqeg0WcfkquOhSU44lKCo9sJPvvrffjsFgJpncmAsbwcPJOy15Lv98tB_nwIA6k-SiIzrSB-6vzmRAF-teTJkzc6uPz_eC61-gumNzSrJA0hX63sGstTc5e5U0XUjmxHpkOh0pESNzXnX_TSMgyw4bZh5SRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد موگویی جای همه رو لو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/138825" target="_blank">📅 11:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rctaq5prVhaeaPR7tuj_AWk9Cwm-uFc3OrGrI_gEtZ_7QytZEDSu6mxB2BSOT80lFFHTGxDiRHCsxICCIKSnxz3UO2IJtvkpLyupKLoOo2pZS9NONPXXc_mYnp8GwAUH3uUAuisnZ52qH4QKowclydysULTA3cSGlqH3XFKyirx4iofmJ5slHPPTMF9gb88Mxoq_t503jJCMZkNYJGo1m8bLq9RxOEeiy670cXnTVzFziVTDAczAdf5HGL3WpEIQAFDztSsv6Yhg5cr1SRaw0LpfZ1zh1P060l_ivMLddOgvBI6LWXC0FsEp9apKjk8PnVYzNRPVS3QFWXM36sRtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فک نکنم‌ جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138824" target="_blank">📅 11:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ارتش روسیه به وسیله کوادکوپترهای انتحاری، تعدادی از پمپ بنزین های اوکراین را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/138823" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsnf-MACyQJoRr0xPnE28rgxuFHvZfg5iDblUEVwp4iN7CP1L4Sd-Xreb-vGL-5eR3Mrj3mFQfZilQsVjORbGY5TthfsOE-c4QKg1R6paKy1fTdxnYWwgL-oyC_yOQQ9zhoZC-fonNNzn9rZTtklXmzaTOEuLhxqb1_4rc0UJLFRcyQD-wCQfnJyn9UK2nQhhlHS05UPM7ld5bQvV3pzL_LBlcu_UzkoaQXnEGDyz7z0hxftsfdmJ3La7bRjT8bnyZhOjhYeznfszKoyuHJS2cNwaYFGe-JFBiDTHK88a2nV3dWn1jn3yCmSFX3H2V-EsD1dWJe28PVGULS6sq6rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر دهه هشتادی رئیس بانک سپه، معاون بانک دی شد
🔴
پ.ن: لابد اینم امام زمان انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138822" target="_blank">📅 11:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
روزنامه «الاخبار» نوشته اردوغان در گفتگو با عون، رئیس‌جمهور لبنان، به او توصیه کرده در توافق با اسرائیل شتاب نکند زیرا اسرائیل هدفش صلح با هیچ‌کسی نیست.
🔴
اردوغان به عون توصیه کرده که سعی کند با سفر به دمشق و دیدار با الجولانی،  روابط خود با سوریه را تقویت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138821" target="_blank">📅 11:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/138820" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=XFoNXzT3NUdHgrxEd4ZXDAIWnTYieVLcE-4CZ6U6MGG56jLlJLonVBghfFWUkPIIoFD18kil7HLmfsnrKq7XKW_Z8f5Ho9Abz1BNOaII0aaTnH1f0V35JDAbqqEt6ZzhkF-A0I5zYY-DGfUuwALPlLNUdui22U58QKVkO7PzctXh9SsRd4BbxUHGoaBY1oG9BBnr0uytHc5Bv57j82i65x0jWK51J3kI_9gSW534TlFTx8LkQx_g8DVKW0VVU9fFubsnft5UFJtdZQiPJeZFOxl9SNRJ72KftxV3zH5LJ6HDABwCARLJg9CEiCOkZjwAXSyMB6zv81e9B01-5-0oVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=XFoNXzT3NUdHgrxEd4ZXDAIWnTYieVLcE-4CZ6U6MGG56jLlJLonVBghfFWUkPIIoFD18kil7HLmfsnrKq7XKW_Z8f5Ho9Abz1BNOaII0aaTnH1f0V35JDAbqqEt6ZzhkF-A0I5zYY-DGfUuwALPlLNUdui22U58QKVkO7PzctXh9SsRd4BbxUHGoaBY1oG9BBnr0uytHc5Bv57j82i65x0jWK51J3kI_9gSW534TlFTx8LkQx_g8DVKW0VVU9fFubsnft5UFJtdZQiPJeZFOxl9SNRJ72KftxV3zH5LJ6HDABwCARLJg9CEiCOkZjwAXSyMB6zv81e9B01-5-0oVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/138819" target="_blank">📅 10:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
الجزیره: قیمت نفت کاهش یافت، اما در مسیر ثبت رشد ماهانه ۲۰ درصدی قرار دارد
🔴
قیمت نفت روز جمعه کاهش یافت، اما همچنان در مسیر ثبت رشد ماهانه نزدیک به ۲۰ درصد قرار دارد. نفت برنت با کاهش ۱٫۰۳ دلار (۱٫۲ درصد) به ۸۸ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138817" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt-lpZpjBJIvLmsOW6IDTVWLyBL5sd1m8Ehp5KLHlKA1kqYjhFxRuogY_R47HF6hf_hq85R15aBRQMdWNk4CiF0zw7Q6u113FtgkjjrXlwhIJ8zkZhJLbXjNysm-kn6Jxl0RYO8biaNJAdZTGScHHpok1TZ3VX-1FJYG5TJmtxB5JqejQGCDEHm1MK--vf3w5YcZ3TrpWkpf4Fj1Vo6rZuNcduoJCPb8Ydw4OY-FaBWzVnRg4cCGZcduztbYFRTfPhJS3XE3zze22h27spWcmXykZBO7jjvb8AngGjLb3Er_7yDItWXHEjNk7khCg-iYBSoVIRUMUuNdEdMc8uk_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138816" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmrWlHz_r4ldo_GuuoJ6gwa1xrX9eCWwhv6AawzfHoRBzJTUhQ-_mO3JCksTQoJHFdMHExhCqYm_M1i49lJT4oXX30SZkiL29sfJwPsTZkhLpL8mAJrL7R1fe5B7UwROU-Gje_ohFZhtixQOQp6qR_6ABIowXUb4CsFj4oXOSXbfgIE-NfY1_Kwk9p55kBurt0FA-jYxccqDNO8nwQ3s1cJWDHyZ0hthf0IMG_Y2po4lyIL-7i_n9dQcBfkydRNbYG1oBmW44FVsPnI9BeWFhAc2mzcdkwc0XIpl__1dQfy5SEWA5o6d3XEZ2TVNmSU9lfSMUDM1v9SlaE6qW-aIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهری: ممکن است یک آمریکایی انتقام خون رهبر را بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138815" target="_blank">📅 10:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138814">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شورای صلح غزه: حماس به‌طور رسمی متعهد شده است یک برنامه اجرایی برای واگذاری همه سلاح‌های خود را اجرا کند.
🔴
اقدامی که در ادامه آن، خروج نیروهای اسرائیلی از غزه انجام خواهد شد.
🔴
این طرح همچنین «نویدبخش مزایای قابل‌توجهی برای مردم غزه است؛ مردمی که مدت‌هاست در انتظار آینده‌ای بهتر هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138814" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138813">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4lugapgqTliluPWjyNq6pCcBX-nYYJRvAYlnsXcrTMges7mh4lqBsElqZVJmLS1e2pWqfVvgCq8p6NmUZrI86TobSOsEUnMjjFLMgFrBOBVxptZTPFSAPtl3bfH5xhRZm75xTE41NpK-nHjEiutXa6526ldsIRGQ48vmqn8rtsANcyz3Gu4RBUaNT5flDateznYF2BFOGayGKTB9rzRtVMJgFaTULZhbRWxbnyEBoTgv-nBoVjzn6j8_Il7OnxZT_fR5lIpCwIhJKlngZrPv7xNZ-1xJMQim8MI5ILbr836chRcVW4WzlKzYNgps2sA9Z5UNK8OsvSjt0QeF9WP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آپدیت بازار کریپتو ۹مرداد ماه
🔴
مارکت کپ: ۲.۲  تریلیون دلار
🔴
شاخص ترس/طمع: ۳۷%
🔴
قیمت تتر: ۱۹۳,۱۴۷ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138813" target="_blank">📅 10:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138812">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1510e3d07f.mp4?token=NYr5IcJFXQnph69WeSmLRYkpN1BvvJz9iUNJ0qIFsRXu7zsCxxwHauV3slFLHV0CI4qpFFsoiGSRT9otrf8kMw6ZTdnKniXl1ShfvKphHtfxGJ8W4EKWl-ecF-dsPyLiChw7lCjHgbfYi4op4LffuuAKL_IUR8-BIhWOi70zTJMK9QP9z7aIsAJ2C7xORXvc9ZSGcoG1phUZ2IGCE3FvoGmvgnCaN8bowkbAOA9P_e3mRoSvMEI0nKxutUP6KgZvshU5xIKR_dlxQtelz1bB_8DvtG2soT9pLDnUZHfaOBPJBwqTO-EoI4HmV_g6kWPyRUBmn7L-ywFg5sCPXwAhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1510e3d07f.mp4?token=NYr5IcJFXQnph69WeSmLRYkpN1BvvJz9iUNJ0qIFsRXu7zsCxxwHauV3slFLHV0CI4qpFFsoiGSRT9otrf8kMw6ZTdnKniXl1ShfvKphHtfxGJ8W4EKWl-ecF-dsPyLiChw7lCjHgbfYi4op4LffuuAKL_IUR8-BIhWOi70zTJMK9QP9z7aIsAJ2C7xORXvc9ZSGcoG1phUZ2IGCE3FvoGmvgnCaN8bowkbAOA9P_e3mRoSvMEI0nKxutUP6KgZvshU5xIKR_dlxQtelz1bB_8DvtG2soT9pLDnUZHfaOBPJBwqTO-EoI4HmV_g6kWPyRUBmn7L-ywFg5sCPXwAhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: در نیمه شمالی کشور دمای هوا روند کاهشی خواهد داشت
🔴
برخی مناطق جنوب کشور و سواحل دریای خزر با رگبار و رعد و برق همراه خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138812" target="_blank">📅 10:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138811">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7007c9b457.mp4?token=p98TOAQB7ws-MqP7ulsRZLEW2mZ0kHqxCdkCS0xwGXX70BTtKvNNSkfJjolgN_-fyVNBQ2tMhzfc8_RLlYGv7ua21oGSNwp_bRoQQ1OdwaNH_Vi0YgycOyI7CZJIuF3hL8VoK_KNBLfmVVHmhF1Hpqc4ZjX7EcTbMTumeeR2KhR8qn2i5KrTOVvWeA7ECIXWnCz1fREp9VNuSj_0wv678pEYQSli__tLDsHwLNUPjilYcfpRP5ZTrUdm2tTsLd53Hg-b-N9BlSJV4Fv7t1Aku1yMuf6qVuy1y-iAAa_MsI3dg--biFUCQewcIyt1WR1O9wutPNLpWLQhQ-D0t1gaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7007c9b457.mp4?token=p98TOAQB7ws-MqP7ulsRZLEW2mZ0kHqxCdkCS0xwGXX70BTtKvNNSkfJjolgN_-fyVNBQ2tMhzfc8_RLlYGv7ua21oGSNwp_bRoQQ1OdwaNH_Vi0YgycOyI7CZJIuF3hL8VoK_KNBLfmVVHmhF1Hpqc4ZjX7EcTbMTumeeR2KhR8qn2i5KrTOVvWeA7ECIXWnCz1fREp9VNuSj_0wv678pEYQSli__tLDsHwLNUPjilYcfpRP5ZTrUdm2tTsLd53Hg-b-N9BlSJV4Fv7t1Aku1yMuf6qVuy1y-iAAa_MsI3dg--biFUCQewcIyt1WR1O9wutPNLpWLQhQ-D0t1gaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 نشان می‌دهد که پس از حملات اخیر موشک‌های بالستیک ایران، آسیب‌های جدیدی در پایگاه هوایی علی السالم کویت ایجاد شده است.
🔴
در این تصاویر، یک اثر سوختگی در یک سوله انبار که توسط نیروهای آمریکایی استفاده می‌شود، مشاهده می‌شود؛ اثری که با اصابت مستقیم یک پرتابه مطابقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138811" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138810">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da03a51b1.mp4?token=aEbkDhvQyLhFHL9gQ2UC3gLYQlrhy7gT2X6M0nUCMAT9r3icsjg0Svwp9uMIbGOxr1Qb4Wx_8GRVlFgQJ6J2U3acIXb0KKB-D0s92FIqa2it3Vf5RkhsXhcBatlGYDluNDbr2Z_3Mhqqhjn2LB9k_ul2blua4n1r7TlCTM5c7n0VsWH3XR5wxV6sdXXJwUEntjAvY114qhTF7qFyZwKZjDV3nKNvNTRUKxOdKVfcyrjukASTd5VnyPNRGY81-pVxGEe_jihANIVrW6Nos1exiG7nFIULKQMCLiVAYjKKAPbFFXvKUsrdp_smuF3Ci11ws94Lm7XRsW11cbwIPijgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da03a51b1.mp4?token=aEbkDhvQyLhFHL9gQ2UC3gLYQlrhy7gT2X6M0nUCMAT9r3icsjg0Svwp9uMIbGOxr1Qb4Wx_8GRVlFgQJ6J2U3acIXb0KKB-D0s92FIqa2it3Vf5RkhsXhcBatlGYDluNDbr2Z_3Mhqqhjn2LB9k_ul2blua4n1r7TlCTM5c7n0VsWH3XR5wxV6sdXXJwUEntjAvY114qhTF7qFyZwKZjDV3nKNvNTRUKxOdKVfcyrjukASTd5VnyPNRGY81-pVxGEe_jihANIVrW6Nos1exiG7nFIULKQMCLiVAYjKKAPbFFXvKUsrdp_smuF3Ci11ws94Lm7XRsW11cbwIPijgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش، یک اردوگاه متعلق به گروه‌های تجزیه طلب کرد، در اربیل مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138810" target="_blank">📅 10:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138809">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نخست وزیر و وزیر جنگ اسرائیل با صدور بیانیه مشترک گفتند که ارتش اسرائیل در حملات شب گذشته خود علیه جنوب لبنان از ۷۰۰ تن مواد منفجره استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138809" target="_blank">📅 10:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138808">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پاکستان: مذاکرات میان تهران و واشنگتن ادامه دارد
🔴
سخنگوی وزارت امور خارجه پاکستان:
اسلام‌آباد نهایت تلاش خود را برای بازگرداندن ایران و آمریکا به اجرای تعهدات‌شان در یادداشت تفاهم پایان جنگ به کار می‌گیرد.
🔴
مذاکرات میان طرفین با وجود درگیری‌های اخیر ادامه دارد.
🔴
پاکستان از طرفین می‌خواهد که حداکثر خویشتنداری را به کار گیرند.
🔴
گفت‌وگو و دیپلماسی همچنان تنها مسیر ممکن در میان تنش‌ها و خصومت‌های جاری در غرب آسیا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138808" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138807">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مدودف: روسیه در مرحله‌ای مهم از پایان جنگ قرار دارد
🔴
مقام روس گفت: مناقشه اوکراین بدون تردید با پیروزی روسیه پایان خواهد یافت و اکنون مرحله کلیدی از پایان آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138807" target="_blank">📅 09:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138806">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
واژگونی یک دستگاه خودرو سواری پژوپارس در مسیر دهلران به اندیمشک، به جان باختن چهار مسافر و آسیب‌دیدگی یک نفر دیگر انجامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138806" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBBCppgzG4B5pcKwRBHYay_Vjuy4z5Q0xdRnACn7Qqje0KUBJ8iSEmqnCFZ_cmCMCAnkY6P-QHBiRErHaqpKENRogwWy5D85WQHCHt4fAhdWQaBdM1YNIN5He9z_obOKEar2o64zqaMEE7z8L_b66fNsZCClARWOoLT_GO3S0x2Hxi1FzeDscUaUE168I_2FyqCHcZxVP4Nps-K7vhx0CxQY6oFAAzTmYyp6LnjVp3Xgj9Y1HPw7Wgj8HeVWFQo0mEaJPfi_uwNE6Zg3HwjxmDk5ONPcuHgHsZEJpATokMLjEg7l6AKdJxWk7TtLURtNPDM3s95uVgblTfnsZ2eg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین رای‌گیری غیررسمی شورای امنیت سازمان ملل متحد درباره هفت نامزد دبیرکلی سازمان ملل برای جانشینی «آنتونیو گوترش» دبیر کل کنونی این نهاد بین المللی، روز پنجشنبه به وقت محلی در حالی برگزار شد که خانم «ربکا گرینسپن» معاون پیشین رئیس جمهوری کاستاریکا پیشتاز این رقابت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138805" target="_blank">📅 09:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=h9RQ5N7LheGzYvxg9mS_2XmUoUBagG7r0C6ChDMm4yNOIapCFB8yfqmX62pYzQtAErVQG6MJCr2R500dlux9nqF04oGU5VithCThrT5yVRiszdow3bSwpjFlbzkATk6MR3EnrsG6meogonPOfUmJx8BQPzBOyyGOrmNgR6AV7STxVXLLtgbgBsNRDSUHLT1U0f6bjWeFmUz8XbhXqDfi916JnT41aKtyxAu8Q4PpecuxzP6vxpb3pABn0LjFob5QODpAEfF41GJowZWfwIWMadYLroVM23JcwZwL5yzPF5YZwdeDbYy2LIFOQV9lWVwYBaDMo01YL_OKkRpzC2ORSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=h9RQ5N7LheGzYvxg9mS_2XmUoUBagG7r0C6ChDMm4yNOIapCFB8yfqmX62pYzQtAErVQG6MJCr2R500dlux9nqF04oGU5VithCThrT5yVRiszdow3bSwpjFlbzkATk6MR3EnrsG6meogonPOfUmJx8BQPzBOyyGOrmNgR6AV7STxVXLLtgbgBsNRDSUHLT1U0f6bjWeFmUz8XbhXqDfi916JnT41aKtyxAu8Q4PpecuxzP6vxpb3pABn0LjFob5QODpAEfF41GJowZWfwIWMadYLroVM23JcwZwL5yzPF5YZwdeDbYy2LIFOQV9lWVwYBaDMo01YL_OKkRpzC2ORSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش : پهپادهای نظامی، مراکز استراتژیک آمریکایی را در کویت مورد هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138804" target="_blank">📅 09:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138803">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCtfy6_iWdWlLKnsSPX3BpUBR007AEzokEJkO4hA0AW8p2Dr42BeiZ_zviv-7Y5HnGhgorCnc5CjdBFv3jvR5P1YjbsjeB2vH0DXGlLW6553jV_cPMFuKp9SvBnCpohIWKShwvk7lQFcfKF8g2T66VVw_gKb7ZzReactw3-STqd_gCht6tIveZkWvpwsdI_p8AgS0MY580pQbyWHM6YBaectmzOCrklrqxL3VmcMvS3gM3xsTjN_shu3R-MwYUHho6K1bySE0LTzOqfIVxvwScpVxaWIw7h5wedYLR_gOKyAg3Jg85xoj4OoCcOzZvMxJ2ThxiTJwqKuk_7hz9qU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ از ایران «خشمگین» شده است، زیرا مقامات ارشد نمی‌توانند بر سر یک استراتژی مشخص، به توافق برسند
🔴
رئیس‌جمهور در جلسه اخیر خود با برخی از مقامات ارشد امنیت ملی خود به شدت برخورد کرده است.
🔴
او از عدم پیشرفت در زمینه پایان‌دادن به جنگ با ایران و همچنین اختلاف نظرهایی که در داخل دولت خود در مورد استراتژی وجود دارد، ناراضی است.
🔴
برخی از مقامات از ادامه عملیات نظامی حمایت می‌کنند، در حالی که برخی دیگر هشدار می‌دهند که حملات طولانی‌مدت می‌تواند ذخایر تسلیحاتی ایالات متحده را کاهش داده و اوضاع را وخیم‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138803" target="_blank">📅 09:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138802">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W32ajk3Lh9E0ldRNBD2Mp2F1ZWW_I9CyV7iv0GXMeGUYuNJWtk1nVlE-dLEVzAvz-2bYmc2XPKHJLecGfQrgtUGeGSHuzT3T3DCABJUQ3w1t9nOeEQQZIhfDUKUdHHbcS89cyxPLOjhWgrd9vGUuEJ1bAbIduBTxm_LEdNr1Q5OPrnLul2--JF0-BT6zGw5rX-KSEi1PhLsJtN0bol18NgNMgCEypqFdp0W626_GgyekxTYoWGyv-WQgnIe9AN1Al1mlckYLvRfH05_ceYqwtNoePBq7TI3nWMEj3Ge9EOAJvPfB88QdKN6sWATVd30GJdAMMnE4MPRmmy1bZMMBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
@AloSport</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138802" target="_blank">📅 09:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138801">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مقامات آمریکایی به وال استریت ژورنال:
«پنتاگون در واکنش به حملات ایران به پایگاه‌های ایالات متحده، حضور خود در کویت را کاهش داده است تا خطرات را به حداقل برساند.
🔴
پنتاگون پیش از شروع جنگ با ایران، در حال بررسی امکان کاهش نیروهای خود بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138801" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=oF-YIWqIxoN5e3_G6-LqTN_IZNtiuU097GYda19E89H2ye7u4ImhHngKUVw4EaDdt7_X3kjQdUqnCi4_y55D1woLQszprQysA8V34YqqSloRGB_L7a4x89wQeDFhoRnmZHQ2AejkKTxwVNMjaXEGpGpItk2fCbGEK0xUCKkLLdyp6T8lsn-6R8BFyJxpePyZH98wMK36YQFr_dnQkyjvMQmHza-DjVr23hhwouhW-aS0hZP1bec-WmQRPzO4hxk250sR8Wh0QFcUAgHctr2M1Jq9g4cjktF2zicbkM5j1d5OkL-ifOm6peCfKJfrDhsSYIvrkw_dKVaRb53vUNc6JwSBM_niMTq_R5DpEaFPQbZckn90mq-vSpU3x1eLLzs3ZkcLDb6DBhCTdGLIwuHCRUu21QyqAJJ-uLh1KtQXMmylNdiCn_XBKO65zgF5IuRsaFhO9wQiewoMDWg1XJvnPulipWPwWPcYnEbVaDJe9qejQrl7I7TyD6B5mWnsflTafkHwLWn94dgsBLe0udppaxRgxywweVJVneeR_HsHvmwFlw8XykVxSApsENMDfyTTeOzArB94eXbobzfsCLW5sLLLcoKrFzWbMJwVbo28jlsTri3QjK98jWFf-wtOwI9DoMFyKJjjQVNYpdseVTdq07zxVaBfrAUeLwHuTDh1Bao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=oF-YIWqIxoN5e3_G6-LqTN_IZNtiuU097GYda19E89H2ye7u4ImhHngKUVw4EaDdt7_X3kjQdUqnCi4_y55D1woLQszprQysA8V34YqqSloRGB_L7a4x89wQeDFhoRnmZHQ2AejkKTxwVNMjaXEGpGpItk2fCbGEK0xUCKkLLdyp6T8lsn-6R8BFyJxpePyZH98wMK36YQFr_dnQkyjvMQmHza-DjVr23hhwouhW-aS0hZP1bec-WmQRPzO4hxk250sR8Wh0QFcUAgHctr2M1Jq9g4cjktF2zicbkM5j1d5OkL-ifOm6peCfKJfrDhsSYIvrkw_dKVaRb53vUNc6JwSBM_niMTq_R5DpEaFPQbZckn90mq-vSpU3x1eLLzs3ZkcLDb6DBhCTdGLIwuHCRUu21QyqAJJ-uLh1KtQXMmylNdiCn_XBKO65zgF5IuRsaFhO9wQiewoMDWg1XJvnPulipWPwWPcYnEbVaDJe9qejQrl7I7TyD6B5mWnsflTafkHwLWn94dgsBLe0udppaxRgxywweVJVneeR_HsHvmwFlw8XykVxSApsENMDfyTTeOzArB94eXbobzfsCLW5sLLLcoKrFzWbMJwVbo28jlsTri3QjK98jWFf-wtOwI9DoMFyKJjjQVNYpdseVTdq07zxVaBfrAUeLwHuTDh1Bao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت حمله به خوابگاه دانشجویی اهواز از زبان یکی از دانشجویان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138800" target="_blank">📅 09:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عبور ۲۵ کشتی تجاری از باب‌المندب
🔴
بر اساس داده‌های شرکت ردیابی دریایی Kpler که خبرگزاری رویترز به آن استناد کرده است، روز پنج‌شنبه ۲۵ کشتی تجاری از تنگه باب‌المندب عبور کردند، در حالی که تردد در تنگه هرمز همچنان بسیار محدود بود و تنها دو نفتکش از آن عبور کردند.
🔴
از میان این ۲۵ کشتی:
۱۸ فروند وارد آبراه شدند.
۷ فروند از آن خارج شدند.
🔴
این کشتی‌ها شامل چندین نفتکش، از جمله: دو نفتکش بسیار بزرگ (VLCC)،
یک نفتکش سوئزمکس،
و پنج نفتکش آفرامکس بودند.
🔴
در همین حال، هیچ‌یک از دو کشتی عبوری از تنگه هرمز حامل محموله نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138799" target="_blank">📅 09:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام آمریکایی گزارش داد که واشنگتن از اسرائیل فقط می‌خواهد که با طرح ۲۰ ماده‌ای که قبلاً به‌طور اصولی با آن موافقت کرده بود، کنار بیاید. این مقام افزود که دولت آمریکا اطمینان دارد اسرائیل به این طرح پایبند خواهد بود و اشاره کرد که اگر چنین نکند، دونالد ترامپ، رئیس‌جمهور، «به‌شدت ناامید خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138798" target="_blank">📅 09:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یک منبع اطلاعاتی آمریکایی به شبکه نیوزماکس گفت:ایران از داده‌های مربوط به فناوری تبلیغات برای ردیابی نیروهای آمریکایی و هدف قرار دادن آن‌ها استفاده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138797" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=GwzdLQYz2HkBQo0VpGCVyR6kk7XTryzSzfe8z5xpHWlu39oy8JEg6RU_3msH2OEKFggVQfkIckMHIaA-6lPAV49y0whhHQxgGanhuC3oSgnPL9i2NSX78xe_aPr9yrHz65vj3tukbvcU8EiZIbe0Y24ReoomhogKdURafgutz7IsZ4L8abbBGon40iVbeWwDmCHFVL_g90TT8YZ_r7oEo0uQFXX1EwI27cN6arJPqAdls82nkhV78GUIahqfu7DinHEqwVw7Pe3vWVZj3pfh-qlxWiR6OsXtAthJ3CEQcJG2UDCIK5477XEUvcF4ku-NWkyzlf_y8CTOa7jNZk80Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=GwzdLQYz2HkBQo0VpGCVyR6kk7XTryzSzfe8z5xpHWlu39oy8JEg6RU_3msH2OEKFggVQfkIckMHIaA-6lPAV49y0whhHQxgGanhuC3oSgnPL9i2NSX78xe_aPr9yrHz65vj3tukbvcU8EiZIbe0Y24ReoomhogKdURafgutz7IsZ4L8abbBGon40iVbeWwDmCHFVL_g90TT8YZ_r7oEo0uQFXX1EwI27cN6arJPqAdls82nkhV78GUIahqfu7DinHEqwVw7Pe3vWVZj3pfh-qlxWiR6OsXtAthJ3CEQcJG2UDCIK5477XEUvcF4ku-NWkyzlf_y8CTOa7jNZk80Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ایران به کُردهای تجزیه طلب در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138795" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شمار قربانیان زلزله ژاپن به ۳۴ نفر رسید/ ۳۵۰۰ خانه هنوز برق ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138794" target="_blank">📅 08:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اکسیوس به نقل از مقامات اسرائیلی و آمریکایی: ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
🔴
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
دو طرف توافق کردند که به دنبال فرصت‌هایی برای همکاری اسرائیل و ایالات متحده در حوزه‌های دارای منافع مشترک و اهداف مورد توافق باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138793" target="_blank">📅 08:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزارت جنگ آمریکا در به‌روزرسانی آمار تلفات اعلام کرد شمار نظامیان زخمی این کشور در جنگ با ایران به ۶۵۳ نفر رسیده است. بر اساس این گزارش، ۱۱ نظامی دیگر مجروح شده‌اند و تاکنون ۱۸ نظامی آمریکایی نیز در جریان درگیری‌ها کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138792" target="_blank">📅 08:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
🔴
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
🔴
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/138791" target="_blank">📅 08:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4HjegrVMafhGPBKSal5IQyggi6H34plkNOZyfuagTpPtyFmUnyscJN0rVq7I-3szKXM9K1VgnAHsJLYNpI8X9aXmcwbIxXCQjhdQkWXaYAnYbOUiHanwpZDHDvY2k4bSaMYVRUu6YwIbEJrTicUtB3ZhUNKMxm9sk-EayBQyrFbybZTuWV-jZxbuB-c-WFEedOkk7WtcH5gc8ULcs3hN8BseVhr4r3vyu134QWoANG8BhfZqbyng6JOPhRrGFlu9GVvicjiYfMEk7qf0ys-Bfr3K5VAOfIisph9Pfb4LmE6CsZ23eAVjJsKQuVF4lD8pwYfPWuARnL5Y6xMEgTetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اینترنت استارلینک در عراق چقدر است؟
🔴
یک ماهه سرعت ۱۰۰ مگابیتی؛ حجم نامحدود: ۹ میلیون تومان.
🔴
یک ماهه سرعت ۴۰۰ مگابیتی؛ حجم نامحدود: ۱۵ میلیون تومان.
🔴
میانگین درآمد مردم عراق: ماهی ۱۰۰ میلیون تومان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/138790" target="_blank">📅 08:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZtQSu4TNL-AhKf0tisfBcWhWlFiwWj4eE3YcLGFGJHU2EYWkqaUic1Rcc91n3B-nCdENVw03C3Gla2Z2GQEhIKoPhW0f1DwOEEy0nLrc_k8iiWR8fUVZ0KLjL0E_vMQMWIQRnKy6v9hIz7ZAjljlACG3ytyDvpeUQ19vLZ7xIJgKLmC05bYvlNc3pe7Bv4AxCjasVbVNwQL0j7AwOSYtyJDrq88KTtpYQt_4O3p7ZAKD_cYQNwJb-n8Jga0r50LUiy0RPQJkWCdNE-NN8VyTWe7CJ4_rFekW1sFEySelrWsTSqTU44v_NVXg7nu_B98N7Ll2PdIbzONLnXxUz_oXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: حماس خلع سلاح شد
ترامپ:
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این یک نقطه عطف مهم در اجرای طرح 20 ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
تهدیدی که از غزه در 7 اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت.
در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/138789" target="_blank">📅 02:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCr3j0tZP6G6zshzRt9ErmlS4yWqE3aESY7Ap8T8O5zaFo4gv-yRQEgM8Qq83l4olbvvM6UwRGh4YQRDmNbjwPYW_GJvNZ1W1g8z56WjfnNnT_8ddimSnVUk5ZD8Rn88EIWVNZdXaWddUxTEl_B12mdTtMzJ9nbVrN8cJyZUO5Ji5tsA8ppEcXAY7whwf8ilf4uWF02H2ycYF_FxczMvb8v2DK5ZkZbNtsMR3ktnpT3-CUqHbNqIuolNY5QMbsJzySf8J9_7jIxHvf_OLweE4YTAGrMghn5ZhXBA3kPkJtxIxkfAn0fEy1ztOo9CM8QDXw2J48ijyhGPmFqe8O-0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عجیب نتانیاهو با یک سناتور!
🔴
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/138787" target="_blank">📅 01:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد در آسمان اربیل، واقع در کردستان، مورد رهگیری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/138786" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=hdFzeIjcUZoxcgMQzh8cCS-vtpSHTUHM33KOPMfjZ025ESVfcljrA_znjaY4QL5PEql0MCsiqwBHdTbC5ZHjQWvkhuxYGTq6tc9IVxCs7CB7SmrZYSBVtqYnBNl4Ym7uQrvFagC1O8C244Yh4FNQTxnrdhoXLEBXi5X9IKz53eOXRNwhrmaUQChuonzDjC1wqgD4gkKrSHFtyX0d07lDLw6I6TdGpHMAkDPHnQQxQsbIrYffuXR-QASh4v0y8aK6P884pVjAM-CnzQmJ9VlXjpsBpD2JeKD-wFeovMp2Np9NDZ_8e8OCGcL2GnRxokXf-ROPQF4e9ogyxE9h_MVuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=hdFzeIjcUZoxcgMQzh8cCS-vtpSHTUHM33KOPMfjZ025ESVfcljrA_znjaY4QL5PEql0MCsiqwBHdTbC5ZHjQWvkhuxYGTq6tc9IVxCs7CB7SmrZYSBVtqYnBNl4Ym7uQrvFagC1O8C244Yh4FNQTxnrdhoXLEBXi5X9IKz53eOXRNwhrmaUQChuonzDjC1wqgD4gkKrSHFtyX0d07lDLw6I6TdGpHMAkDPHnQQxQsbIrYffuXR-QASh4v0y8aK6P884pVjAM-CnzQmJ9VlXjpsBpD2JeKD-wFeovMp2Np9NDZ_8e8OCGcL2GnRxokXf-ROPQF4e9ogyxE9h_MVuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: تونل‌های حزب‌الله تو منطقه بوفور جنوب لبنان رو با حدود ۷۰۰ تُن مواد منفجره منهدم کردیم
🔴
این عملیات در واکنش به نقض آتش‌بس از سوی حزب‌الله انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/138785" target="_blank">📅 01:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دادگاه دختری که از پسرها سواستفاده جنسی میکرد و فیلمش پخش میکرد بزودی برگزار میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/138784" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/138783" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=LTfJJ02ABsVxDGCBpEdoq6lDPznQjCdn5mTKmaUjmEP58m42KAFn360-2Fht7Up7T8mm6ySMaKQ4RJNia74IiqclH07oOcbp7jhVBjaKLQqQt3thC2yIzHaL-GsTbpAAhz_M8B0JFVkQ22PZhnCbVlgk3mLPFn2Lmt949SurUoMIhc89qBS-3o-YDjzpkJS4Ra8Auxtxn-z5TWh_v35H1Q0Ve4-9odp7xFAtQt2wyc1rmsIEy8kMkG-xfiHFcOAa0GsGMkIVwlbCw8pgE6hio_Cu-EW8oodpIKjG7pjEBSa-b7Tb6pcUvacNvNVWjKzbfs6_iCviHPRfZallLG5icYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=LTfJJ02ABsVxDGCBpEdoq6lDPznQjCdn5mTKmaUjmEP58m42KAFn360-2Fht7Up7T8mm6ySMaKQ4RJNia74IiqclH07oOcbp7jhVBjaKLQqQt3thC2yIzHaL-GsTbpAAhz_M8B0JFVkQ22PZhnCbVlgk3mLPFn2Lmt949SurUoMIhc89qBS-3o-YDjzpkJS4Ra8Auxtxn-z5TWh_v35H1Q0Ve4-9odp7xFAtQt2wyc1rmsIEy8kMkG-xfiHFcOAa0GsGMkIVwlbCw8pgE6hio_Cu-EW8oodpIKjG7pjEBSa-b7Tb6pcUvacNvNVWjKzbfs6_iCviHPRfZallLG5icYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین جنتی شاعر: سال ۸۹ تو بیت رهبری شعر خوندم و کمی نقد کردم. آقای خامنه‌ای علنا تهدیدم کرد و فردا صبح مامورا ریختن تو خونه‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/138782" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دادستان تهران:هر کسی از اعدامی‌ها، چه به صورت مستقیم یا غیر مستقیم حمایت کنه جرمه و براش پرونده قضایی تشکیل میدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/138781" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIFxAjynHEYVzSX_ihYba3Rk-lAKLi9FPXsJXHOjqC0r_gPE5Y_K6s2bEE573XiA2iZMdUsHvnh1JmktCy1h-CR9F49UWue8z_pVdZRaR-VR06AUNLe1eTAcEGwED7U8z4r7joZ29KiUCzIShxGgqW7oRTmGczI2t94cjp_5GNxksz43UH0wFjEBAzWTURsBSMKz0_v-zrEhaNqP_GL-JughZYk2dlMxAOvGGMZ4a2vUggbATiejFGkvvnyqqAbtlLc5cCuaYPIP9wUELpgkH958mlL4bLCp1CgNoN1OMQIL_OeHzhd1KxOQ11kMO9K0gXTYKGOcoZbY8VyNir3xtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور رسما تریاک کشید
‼️
🔴
‏استراتژی جنگی عوستاد رائفی‌پور:
حمله زمینی عراق از شمال و یمن از جنوب کار عربستان را یکسره می کند
🔴
‏عربستان بجز توان هوایی که با هدف قرار گرفتن فرودگاه ها و پایگاه های هوایی اش در همان ابتدا فلج خواهد شد هیچ چیز دیگری ندارد
🔴
‏پاکستان هم به دلیل نداشتن مرز زمینی با عربستان کمک خاصی نمی تواند بکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/138780" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟…</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/138779" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟ چرا اصلا چنین چیزی رو باید باور کنید؟ دست هیچکس رو نمیبوسم. هجمه عجیبی علیه من اومده. همیشه کنار مردم هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/138778" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAazcBfjS7i5c3aDpMFbDwJHineDTDXs55T8OqxnBqYUd-cw40Ja8jEEjR0i-c1HGBdAjEX3bfMq9v-1z8d8tk7BE4PsMu5wYY8eDLAlltQtbTTPJQNVaLI2ORC6YT-XK4dn37ztcbvx_0BdPFKku9_MblWQwOz2s5nwmkG3ZbdU0jJX5c3gRdi_dDSULlEOFSvWumMfoG556DLFyaFTLYrAnrvexk-rQGQzKqKmMXQ4YOlG5Ytjv2X8rXWLihWhnS_hyH1EwEw2FmPW7q8Tu0pSvH5Hs9FVJvBRrZea5RSXxLvZo-QeZTl5XZJGY67Rn1MI_gYclqjKw31t3jC1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جایزه بزرگ شهر هوشمند
🥇
نفر اول 500 دلار
🥈
نفر دوم 250 دلار
🥈
نفر سوم 200 دلار نفر چهارم وپنجم هم 100 دلار جایزه
به هم پوک بزنید فالو کنید
پوینت کسب کنید
🎮
لینک مستقیم بات
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/138777" target="_blank">📅 00:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
فایننشال تایمز: حملات پهپادی اوکراین ۴۵ درصد ظرفیت پالایشگاههای روسیه را از بین برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/138776" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubn6zMpn-DMRszUO7Y_-jcIGWUBzJXTPiom2s6fpKGuApeylO_9L0_FNwQxre1p4I_h-Lf85CNZHYh8Rj6zSKm9M4Rq6k_roLZM_GAZlMFjreIZ_dl0Fxz9bC1sewAI2VODtQdPLP25VszuZcXhGADa3PsAqpraGgfoaR2Wkk0ajgCt6eKx8YmwhMlR_xEE3kOD9UKdxFlSGmNKIKHTYyIEMPyHmGSnr6S4GkCuaLW2o8IfUyWEMcY_GrTyoaZo1VOe6mr1fLfqCqzq1j4o9KmAihsNIsf3s9dLsg_uHmua8j2sqmmXMux1ILIZf5vLyWeozehuLuBfDw-iZWhR90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : مصر برای ما یه دوست و شریک مهم توی منطقه‌ست و امنیتش اولویت داره
🔴
همه باید حواسمون به نقشه‌های اسرائیل و عملیات‌های «پرچم دروغین» که هدفشون به‌هم زدن صلح منطقه‌ست، باشه
🔴
تهدید مشترکه و از اتحاد مسلمان‌ها می‌ترسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/138775" target="_blank">📅 23:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhJxFaKXESIMgNpgHz499_A0Fir1--fnjAyM-GZMMAC7YCWZIUt4QByNO8yKbRpCe2JhQyGxcVS0M3vayPk1dtsusWTymB-Wq4feaigw4fT4PCr5C0ZedOrz7PtdRJXxv7UyPrvne7xc1CMFU8uD-Fc0eOPbTA-z6iLNNIsyEmj3c-g56P4XvlShWNRtRMQGDVypBeQJusPArnubpsqxkq_5ppUfAsYDb36whd8UC6xRBjkKEONIWAqWXPxXmdpeZqsq1iVb6oyshYYBQuj4m4SjlBA0DErupsmYn0K5nWgZcA5z524WqsWDozPPTsgPe-qDsflLdJCSLA0m-l8Ffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابطحی: احتمالاً احمدی‌نژاد جاسوس دوطرفه بوده است که کاری با او ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/138774" target="_blank">📅 23:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9bkAgF-duUKPS2aS0LBTuLglRXARJOypEke6tCKzXL5mflXYAGDbBULypDLJINX-Z616ioF5pBaAxmjj-glvbNv94bN3t3WrCuP1KuqNBbrYuGQf50UcPUrKs0cYlx0cniP_5zTosKe1qP3sIgRCLO2IlTKk03MQwHwG9w5mwa0Cv6TUOIbANdEhuDYWy7riFQPggfe4aUY2yJwVcRbZefPFPWqkafbgfmY47rKjh2YB2LKWu70k60-H_Nrj8FYkkjCCUxq_LD7UaVzxZxmMuHxGhYi42YaQrd9YZitLLoAuBmxF_VtVgq42ZODMNNxZExeoZT913M8l6OL2sL0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ماه از غیبت صغری گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/138773" target="_blank">📅 23:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
آی۲۴ گزارش داد یسرائیل کاتز، وزیر دفاع اسرائیل، به همراه ایال زمیر، رییس ستاد ارتش اسرائیل، نشست ارزیابی امنیتی برگزار کرد. در این نشست، آخرین وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای مختلف بررسی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/138772" target="_blank">📅 23:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
اسرائیل منطقه المنصوری در جنوب لبنان را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/138771" target="_blank">📅 23:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرمانده قرارگاه مرکزی خاتم الانبیا:
آمریکایی ها متوجه شدند تابوت هایشان بخشی از تجهیزاتشان در منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/138770" target="_blank">📅 23:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwuiLwAav9qsSEJGuywz632qWP9mfOgXonV6vF-ogRi_SsYzdleOL6nBzW6VupyzIDLU7WRh5VCgZdfSIrd3LcI_rGzwy7G-Jcnlto833-pwJ1FrFjk-bGPlC2LUKoQWlzE_N5KZQya6pTlk_-Y6943a_YQEjscpQC_4X0d4Y2KgvuUuahT3v4VZPX93FPa3Hs9uClopdt2GSQj7XBSPdE2IXyizNzvTnyLkSKiqt5wH8bpV8I76MNtkLYkMTmKAd7Sj8fjIvD8tcFTjyHoUpHF3-LHlyhB_XL1m6YYEAeTqY30f60JbNNpduJHJulIHFhlTN5oFaTyrDJdR_cf5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: تنش‌های آمریکا و ایران ممکن است همچنان مهار شده و بخشی از یک استراتژی مذاکره باشد.
🔴
مذاکرات با مسقط در مورد تنگه هرمز متوقف نشده است؛ نتایج آنها آینده تنگه را برای سال‌های آینده، فراتر از مدت زمان تفاهم‌نامه، شکل خواهد داد.
🔴
هرگونه توافقی در مورد تنگه می‌تواند راه را برای لغو محاصره دریایی و تحریم‌های نفتی هموار کند.
🔴
خوش‌بینی محتاطانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/138769" target="_blank">📅 23:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سیتنا: طبق گزارشات دو روزه سرعت اینترنت سراسر کشور کاهش پیدا کرده و اینترنت دچار اختلال شده،پروکسیا اکثرا مواقع قطع میشن و یا به زور کار میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/138768" target="_blank">📅 23:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138767">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حیدر العبودی، سخنگوی دولت عراق، اعلام کرد دولت این کشور هیچ‌گونه اطلاع قبلی از حملات انجام‌شده به خاک عراق نداشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/138767" target="_blank">📅 23:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
👈
وزارت امور خارجه قطر: هدف قرار دادن دو کشتی در بندر دمیاط تهدیدی مستقیم برای تامین انرژی جهانی و رویکردی غیرمسئولانه است که امنیت منطقه را تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/138766" target="_blank">📅 23:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ناتو: ایتالیا، اسپانیا و ترکیه جنگنده‌های خود را برای تقویت گشت‌های هوایی، به جناح شرقی ناتو اعزام می‌کنند
🔴
این اقدام با هدف تضمین بازدارندگی انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/138765" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f455635e8.mp4?token=RuuAs91IJxt2It7SLkzWPip4RXS6W081Vdv5kWGPAjep6JhP6JaI7SpgIxKh58RsFbLGaVBDipFL8x1QUKoWHDqA_4OC4QLkcMHeuOtyUVwbLuZKRw3wBU6hQFBdhGEWK92kQmNoMRPEj7O0MXWySlF5YJqx3gGuUFt164vLUnlhYwzQb7N1sJ_QB_x0LWUCJDSL4fG1wdJhBLmdu3fp5vRc9fzaOV9DY4ywICkEyGWvMZXbBJY0L_h74peNHgeOT4R7lTeQozSHDwfWxpgk1ORtYRJWwttD4kvOvP7hN7QmzHuUSERRvlxdn29FUSh-DSJ9uEBb81MB0azC_XSgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f455635e8.mp4?token=RuuAs91IJxt2It7SLkzWPip4RXS6W081Vdv5kWGPAjep6JhP6JaI7SpgIxKh58RsFbLGaVBDipFL8x1QUKoWHDqA_4OC4QLkcMHeuOtyUVwbLuZKRw3wBU6hQFBdhGEWK92kQmNoMRPEj7O0MXWySlF5YJqx3gGuUFt164vLUnlhYwzQb7N1sJ_QB_x0LWUCJDSL4fG1wdJhBLmdu3fp5vRc9fzaOV9DY4ywICkEyGWvMZXbBJY0L_h74peNHgeOT4R7lTeQozSHDwfWxpgk1ORtYRJWwttD4kvOvP7hN7QmzHuUSERRvlxdn29FUSh-DSJ9uEBb81MB0azC_XSgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نوید کلهرودی: ایران با جمهوری اسلامی هیچ آینده‌ای نداره و مردم روز به روز بدبخت‌تر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/138764" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/شبکه 13عبری: ارزیابی‌ها حاکی از آن است که ترامپ دستور گسترش دامنه حملات علیه ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/138763" target="_blank">📅 22:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8kPhayuWKvk_ioP8nFoPZnAM0YyNiwE9FJXuP9IbP6UpxGAyhCJVjoLg_qPyfMxLen-Cl4gzdItwVPe2q50QKD6nKo5UlrN4kpBXPw1uXuLtWh8wtkQ3I3loViw8gEB_6NdRIyjIdM4Uo6azJyV4WRBxmOpxyWUaIqKLY49Se93-TcUgt_ItYftORZg60WeJ6rAWvlfaMA1-3ckaRujbJe9XgfSft9vUEyWCWKtw8FziNxplcaxe3h1Q6JZ6SXe2X9gbbTupEAlV_LD8Pzx1b62lDJPWWPjocRjMIfaiumnvDL05w_5Unm5ZC6f4YBylqIXiUrxcU2w-HwecB5SUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تایمز : سیا و موساد در جست‌وجوی آیه الله مجتبی خامنه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/138762" target="_blank">📅 22:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/138761" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
جای اشتباه دلار بخری ضرر میکنی، جای اشتباه هم بفروشی سودتو از دست میدی !   قبلا بهتون گفتم روی ۱۵۵ خرید بزنید حالا خیلیا جا موندن!  ببینید فرق داره شما روی ۱۵۵ خریده باشی یا روی ۱۸۰ خرید بزنی، سود بهینه تر توی نقطه ورود دقیق تر و خروج بهتر هست ( کاری که…</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/138760" target="_blank">📅 22:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مصر: عامل حمله به بندر «دمیاط»‌ هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/138759" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOqPiPwQaSRaI8-rnUqMNxOGjHxs6ilPPWHQSizxqFYt1GEDmy6KtsfpXLqMcUWbqUzQMrJFz2OHcR6UAs7cOqgx2CJC0ZQE4ahdDXAUHSCDXEcT19ygnK19HRCgRGF_nEAvkYF67E9g4cf6wkezup7gCZXH5UK354j7wS9Pv95yXMLZyte-Ol1ELKPNQ7dzwrpw5vUowyWPZfJ7xGoPZUfUu33Q42ANg3_ibgiUQYWhGM65W9VidLSyIrSoFnap-Nt2g0wEKsmZZSCzy-iLVmYstaS7qzHwBtw9hQmXHmJcXhZnfSiSr3FG0RtZK5gMDMXeijTpZ4_rBZQkfa60LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: ائتلاف تحت رهبری عربستان حتی حاضر نیست کوچکترین اقدامی علیه اسرائیل انجام دهد؛ اما در عوض تلاش خواهد کرد مردم یمن را که از غزه حمایت کرده‌ اند، هدف قرار دهد؛ همه چیز اکنون برملا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/138758" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سنتکام :  کشتی تجاری رو تغییر مسیر دادیم  ۲ شناور را از کار انداختیم و ۲ کشتی رو بازرسی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/138757" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138756">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گزارش کانال ۱۲: جلسه هفتگی کابینه اسرائیل که قرار بود یکشنبه برگزار شود، لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138756" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
گویا رژیم جمهوری اسلامی خیلی احساس خطر کرده و داره از همه ظرفیت‌هاش استفاده میکنه.
🔴
دومرتبه مجتبی شکوری و ژست‌های فرهیختگی‌ش رو از توی صندوقچه درآوردن!
🔴
باز هم ظاهراً قرار نبوده چیزی بگه، ولی یهو بار امانت روی دوشش سنگینی کرده، گفته بذار یه ویدیو از کربلا ضبط کنم.
🔴
یه‌سری کتاب جدید خونده، اسطوره‌های ایران رو با عرب تازی درآمیخته و به این نتیجه رسیده که اهریمن خواب‌های بدی برای ایران دیده.
🔴
حالا اومده می‌گه بیاید همه احساس وظیفه کنیم؛ به‌خاطر ایران، چشم‌مون رو روی همه بدبختی‌هایی که توی زندگی‌مون کشیدیم ببندیم و پشت جمهوری آخوندی بایستیم.
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/138755" target="_blank">📅 22:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkUCBJC_nL5tbFrDlOceCRI0q0niAIc-5xsWF_P3ggR0p9x-n20YxQyPYq_3KTkqoxZy_2f62UDgBljOMltgouAfhQuTlcG3zwXX8ySMGpyq2Ea-M5nb3oXIj8KYqRIF738g1Rb9opJxZ2MPXquzcORhUNkb4w8utjCpkYftUowa7R36BEtbR7rudiZx2XodK0VvpDm8XrqURRgn6tekXsUEOgtOIrIR3BdHgZXYgqDpiEdZ5ktmhFUN5UZaGWOliizZ4ezyikXj81NHlot7YUiwasgaxnAQ_HvORIzMM73Tbt7kymtsxzFGadq9ZBSPKTpsC4Cp9mIclRIJ1mNH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااااااااام
😂
خانما تو فرانسه
🇫🇷
کامل لخت شدن رفتن زیر برج ایفل که اینجوری از
ایران
حمایت کنن، ولی همه جمع شدن دورشون و به جای حمایت از ایران زل زدن به بدن لخت زن‌ها و این کلیپشون نزدیک 15 میلیون بار تو جهان شیر شده...
+مشاهده تصاویر بدون سانسور
‌
‌*_*</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138754" target="_blank">📅 22:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
زلنسکی: روسیه در حمله موشکی که منجر به کشته شدن یک خانواده اوکراینی شد، از موشک های کره شمالی استفاده کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/138753" target="_blank">📅 22:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات ایران و عمان ادامه دارد ، تنگه هرمز همچنان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138752" target="_blank">📅 22:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
منابع العربیه: سفارتخانه‌های غربی در بغداد ترددهای خارجی کارمندان خود را محدود کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/138751" target="_blank">📅 22:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: چرا سازمان ملل اسرائیل و آمریکا را محکوم نمیکنه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/138750" target="_blank">📅 22:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
به نقل از یک مقام ایران: ایران هرگز آتش‌بس به سبک آمریکایی را نخواهد پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/138749" target="_blank">📅 22:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_ELIweAhqYJyKzTa7_9oJXtJbLf4POhHLC7EvCd_ZPfDeuIY1EXWPc0pbBIBxeUtgHLtnScDS7SURHXnFZa6B74pmDc58a8ZkhrOC6r-O1KsjxN-a-Sb6soW5qi7zlTxLnpmeUu33gXId3flNkHPUt7AIx1vpqY4TCb3fReeq1vSJ8LHnCk-V5Xw9sjsu-RGTZerw6ek_zyq1qLCWk_tWlr2Kmd6w2vL2p7UCW2WlcBHDv1R1n_1lGM6R4FyCvRBlRS_oDG7GpWPb9RwNjeuwigrb-uIoc2bOAxsByyvjAop1qmL4kiuZbPCdG9S-e-5N7LRP9HqSzDhlt6JkF9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سعودی در نزدیکی مرز با شمال یمن ماموریت جاسوسی انجام می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/138748" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کمیسیون اروپا: هفت کارخانه بزرگ هوش مصنوعی را در سراسر این بلوک با ۱۰ میلیارد یورو تأمین مالی خواهد کرد، تا تلاش‌های خود را برای کاهش شکاف فناوری با آمریکا و چین افزایش دهد.
🔴
در پی استقبال شدید کشورهای اتحادیه اروپا، تعداد کل کارخانه‌های بزرگ از پنج کارخانه برنامه‌ریزی شده به هفت کارخانه افزایش یافت.
🔴
این کارخانه‌ها علاوه بر ۱۹ کارخانه هوش مصنوعی موجود در کشورهای مختلف اتحادیه اروپا، به بهره‌برداری خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/138747" target="_blank">📅 22:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=jF7OU9jzjIZRIw9SU7teW-JyHZfn0C1xoaLBSK_Th0UemsNRovGKx0EaQ9WWrXgqrlpXDR5dW0GB9KZfEywMC54J-fnRtYYNXsaoyrRf21RtflRQQMzj6DaWIzrnRybtq0O5yyvoH3I1b3FDd9VVPK_h_mR0W2vxncvGU-8zAjrAYMNWe0uKW-gJ_ktc_q641lsD7DtVGseFnw5Nbav-PnjNx4Z-KA-Nq6xvzmUtOl2oMcoHrdaIzJ8-f8SOw_z-4sq2heYqMHd4_wouzwegCJLRTaYB6C97ivChp3Yc8lv-qhDs2f6vJX09tb-TrOh2F1MZ_dx1MI10-Xv-ZqVOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=jF7OU9jzjIZRIw9SU7teW-JyHZfn0C1xoaLBSK_Th0UemsNRovGKx0EaQ9WWrXgqrlpXDR5dW0GB9KZfEywMC54J-fnRtYYNXsaoyrRf21RtflRQQMzj6DaWIzrnRybtq0O5yyvoH3I1b3FDd9VVPK_h_mR0W2vxncvGU-8zAjrAYMNWe0uKW-gJ_ktc_q641lsD7DtVGseFnw5Nbav-PnjNx4Z-KA-Nq6xvzmUtOl2oMcoHrdaIzJ8-f8SOw_z-4sq2heYqMHd4_wouzwegCJLRTaYB6C97ivChp3Yc8lv-qhDs2f6vJX09tb-TrOh2F1MZ_dx1MI10-Xv-ZqVOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش ایران اعلام کرده است که مرحله بیست و ششم عملیات «ساعقه» را با هدف قرار دادن تاسیسات آمریکایی در بحرین با استفاده از پهپادهای «اراش» انجام داده است.
🔴
به گزارش‌ها، این حملات به ژنراتورهای برق، سیستم‌های ناوبری و ساختمان‌های اداری و پشتیبانی در پایگاه شیخ عیسی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/138746" target="_blank">📅 21:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد:  بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138745" target="_blank">📅 21:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/138744" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=fm4Ym7j_6IjCHaicX3dP9ZIDSi4NmeJ-K81EwzDDnh4uDeV_Mo_lWi2-Y7a41pW-8wN0Wtc82BLrxGZgdeUKngsf43UUVF6eDOu6CUtFcdTcFEYRPIenCzJMSLATuOQaFvA-8KDHnMUxEsrm5At8SMrQCbBJL_rvPCBApOcIE6qRQwKzBkNaJrdaatIJLTwLzx3yqbZFilyfbsuijE5w7f3YxxGohR-XYXfi4hbe4NJCC016-f6JeSBbKYQXWbWBqgxUSAaNxN-QfQb9N8ezfKpl0nrWnXW8CrEvp1TQpHKONf8vH3ftj4_Xu9udbpgtopP9psetKibfwk5zKHO_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=fm4Ym7j_6IjCHaicX3dP9ZIDSi4NmeJ-K81EwzDDnh4uDeV_Mo_lWi2-Y7a41pW-8wN0Wtc82BLrxGZgdeUKngsf43UUVF6eDOu6CUtFcdTcFEYRPIenCzJMSLATuOQaFvA-8KDHnMUxEsrm5At8SMrQCbBJL_rvPCBApOcIE6qRQwKzBkNaJrdaatIJLTwLzx3yqbZFilyfbsuijE5w7f3YxxGohR-XYXfi4hbe4NJCC016-f6JeSBbKYQXWbWBqgxUSAaNxN-QfQb9N8ezfKpl0nrWnXW8CrEvp1TQpHKONf8vH3ftj4_Xu9udbpgtopP9psetKibfwk5zKHO_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: انتظار دارید جنگ با ایران چقدر طول بکشد؟
🔴
ترامپ پاسخ نداد و رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/138743" target="_blank">📅 21:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
گاردین: عربستان سعودی در حال آماده شدن برای حمله‌ای بزرگ زمینی و دریایی به حوثی های یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/138742" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n05Gur96KF79ydLwO0oLXhwWPI1hERLVOHcESH7nMnqaCqTqzNe0OMl5OEMaHO3RrhZvWCX8mn0tNkahoM1hUtsbTUCB18P_GXf9S2dT4xMi5blS_cQxIhhr_UmoVkK2MEF6LxkVp-iIdWGjgRU459BRsVBTVN82m6dXXN4kFxzY4U_bPDF9cCgrpHlkBi_gAkoYbHAxH9FGn04ZxbXsInSs5AHWSUli30dj_7LW99jlYPmzJJCvt4B3K4mVCpOk4KXK5F-cKLjCxVd5Lz3wZQf-45qpRYZ-gdX9K1IxvKrd28KYdmXwZPcDWei4hcTObCIQOYNYbKa3V-midmqbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گلایه کاربران از زود تمام شدن بسته‌های اینترنت
‏
🔴
بر اساس گزارش‌های غیررسمی، ضریب مصرف اینترنت بین الملل به ۲.۷ افزایش یافته. یعنی هر گیگ مصرف ، ۲.۷ گیگ حساب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/138741" target="_blank">📅 21:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMfIKK7eka77BhE8PwaN-XwBpmVOHuRilHz3JSVDzq3t3PDn1V4_B1NhNwuNF0D7aNCHFhLpSjYrshcZX9eX3Pgli6jw19O9r2SSFZTwwcAraj0ROxc9QhSByxHYcD6Zb_rSluQ6ePYj2PTFyCgG-VkzCs2lziM3W9twoFD7jdCFjH4w0i2t7K2R33sRFLhTphm0t0mfn7RL8MH5EgWzVLQEQr1HpaQVCBHqES__afAyOOE0EV6rwXQLxc14c5KQjDBUzqV1f3-DinWaC6K1lftyQTNo9pxM7kOcVlfwRCsYFcU5oWRfVPT40YoaJYtvxMCZlxj3Kck5IX-9-3DbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خارجی بستنی شکل باب اسفنجی خریده و از انباکس کردنش پست گذاشته؛
🔴
و اما کامنت یه ایرانی زیر پستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138740" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
گاردین:
نیروهای سعودی در حال برنامه‌ریزی برای یک حمله بزرگ علیه حوثی‌ها در مرکز یمن هستند.
عربستان سعودی در حال آماده شدن برای یک حمله احتمالی زمینی و دریایی برای شکستن محاصره صادرات نفت از طریق دریای سرخ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138739" target="_blank">📅 21:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
اگه فیلترشکنتون اذیت میکنه پیشنهاد میکنیم یکبار امتحان کنید
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید (برای شرایط اینترنت ملی هم اوکیه)
(همراه با تست رایگان‌)
خرید وتحویل فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/138738" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XethutjjmaEjvCYRVXEDeGYmfbnE_2ZHY48yxb1bS0E9sy4_35RlDC2I2A0qgm2-p40ThKaCSPci5KTiAD6caszlfjVlQxZhQKuWscH2vvOsnxjY0nJMZHO_A0isMvrAlGBTpTu_9wS99LqUTn_Cdpy398nzBouMXMnrG_097m3W-TBpwdTNpfMbcOX3IwuEGKxqsA5p7em1JLn7-wwThg6zQ7jreHTWDJvt6Wre1QoUIValocjFx1r_cpnJzVmUKPRZX4tDklBrOvPCP3Y_aua6nPM1UBSq1LbGOmmYkgJur6uzRLABWew_ADK-kf9QER3HakQyMHlCvGTDPl5ZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
تعرفه سرویس‌های مولتی و تک لوکیشن SafeVPN
📆
پلن های یک‌ماهه
📍
10 گیگ
➡️
35,000   T
📍
‌‌20 گیگ
➡️
50,000   T
📍
30 گیگ
➡️
75,000    T
📍
40 گیگ
➡️
100,000  T
📍
50 گیگ
➡️
125,000  T
📍
100گیگ
➡️
250,000  T
📍
نامحدود
➡️
400,000  T
📆
پلن های دوماهه
📍
10 گیگ
➡️
75,000    T
📍
20 گیگ
➡️
110,000  T
📍
30 گیگ
➡️
145,000   T
📍
40 گیگ
➡️
180,000   T
📍
50 گیگ
➡️
215,000   T
📍
100گیگ
➡️
390,000   T
📍
نامحدود
➡️
550,000   T
﻿
✨
ویژگی‌ها
✅
اتصال پایدار روی تمامی اپراتورها
✅
مناسب استفاده روزمره و شبکه‌های اجتماعی
✅
دارای ساب‌لینک جهت مشاهده حجم و تاریخ انقضا
✅
تک لینک اختصاصی بدون نیاز به بروزرسانی
✅
حجم واقعی بدون ضریب مصرف
━━━━━━━━━━━━━━
مشاوره و خرید
🏪
@safevpn_secureSupport
✅</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/138737" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ارتش ایران: پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/138736" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sip9qZe4QdbVtsc2_jjrCqol9_hhhMVAuxjIV-a3KRFSPlL1YtA_cu8Q7Lp-MAbJZ7PN-AFJHgLOSE5km24lpmtPKsNfHXVnryNwyk4zFmte-W1h0STTedZg5CFP_POI40g9i2jgQ7uIrRsYgfs1qjLMF4wQRyw0MA6DbmcxdAcMp_Gs2UUm5q-QNF9xpMwq_QT7E2K0TZ_B4MMvXf7W1bZY4IXm5ueYsm1UWc1may1LPmfb9u9f_hkxixXzHIVIp0Q9IFa5M-IqMCYM0fS6xhuVKsumjN4_kRftNFapk7b6LtEv39PDCtHaogZU5E6pjznX5ofBqHyMfKrayFeLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله تایم
:
حجم فزاینده‌ای از اطلاعات جمع‌آوری‌شده توسط سازمان‌های اطلاعاتی آمریکا نشان می‌دهد که روسیه، حمایت‌های حیاتی مالی، اطلاعاتی و نظامی از ایران ارائه می‌دهد.
🔴
این کشور از افزایش قیمت‌های جهانی انرژی و کاهش تحریم‌ها برای تثبیت اقتصاد جنگی خود استفاده می‌کند، در حالی که درگیری‌ها را هم در خاورمیانه و هم در اوکراین طولانی‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/138735" target="_blank">📅 21:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نتانیاهو پس از بازگشت از آمریکا، مستقیم در پایگاه هوایی نواتیم اسرائیل فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138734" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=ZlmF92wLqS9KOcc8rH7enobM6dE3Osy7JLrQY62876Yc4S2_rxnr9ZlcagCgA6Abb6NFoP1Bn1hIBspSZZ8OvazM6wl_m86EbBK285NqfddvvDfS7b1gTLcujCh8Ei_Xxip7jtr2Cki9CeC_bHTTIrhd9nxoIO-mjFujljACnyecXqystvNZLzibS-4aASyTT_oXu-KCPVjR97WaAaX6TVq5bepNkDXexB4HV6OnEhIdbXpLKZIj2Ys4vK2mQV6EyLh0YiJSnFls-ErWP2TAxDdof15Wh-MfG9EEZQW8R0fi3BnrFw9qngEjorqkVbhbMxloM9xyA9uyJ_-R1VNzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=ZlmF92wLqS9KOcc8rH7enobM6dE3Osy7JLrQY62876Yc4S2_rxnr9ZlcagCgA6Abb6NFoP1Bn1hIBspSZZ8OvazM6wl_m86EbBK285NqfddvvDfS7b1gTLcujCh8Ei_Xxip7jtr2Cki9CeC_bHTTIrhd9nxoIO-mjFujljACnyecXqystvNZLzibS-4aASyTT_oXu-KCPVjR97WaAaX6TVq5bepNkDXexB4HV6OnEhIdbXpLKZIj2Ys4vK2mQV6EyLh0YiJSnFls-ErWP2TAxDdof15Wh-MfG9EEZQW8R0fi3BnrFw9qngEjorqkVbhbMxloM9xyA9uyJ_-R1VNzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق
🔴
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/138733" target="_blank">📅 20:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/138732" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=eDl6hxzzHyjerinR7H3lLfxOkbzFlYQgk8R64CA74gq43Bjz03zzJ9D9-8q7dWQm6LGMy75-MTeI1syyCILmHw090-j9hMTPQ7tH_E_zoovLPoXszi_1quYUaaVbJdZZprnAMfeGI8g8tl_4mOwER7m9AffsWCROITrQpGgO1p2N08b7e4vdC7MwN1ci87TqLY0oWNWqT1jId_X8bFLTiSxlCQwWd4wWBNxhEiwHYg-oxQWoOTDzttLX0qXyzQpo06sjgyw7ft0BprQDqN2WqSHWdL9mdUo_6AwPRd13iAg94LUktkxys0k6eBJEzP3Ic2zQ3m565DKgGYRmg0GAxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=eDl6hxzzHyjerinR7H3lLfxOkbzFlYQgk8R64CA74gq43Bjz03zzJ9D9-8q7dWQm6LGMy75-MTeI1syyCILmHw090-j9hMTPQ7tH_E_zoovLPoXszi_1quYUaaVbJdZZprnAMfeGI8g8tl_4mOwER7m9AffsWCROITrQpGgO1p2N08b7e4vdC7MwN1ci87TqLY0oWNWqT1jId_X8bFLTiSxlCQwWd4wWBNxhEiwHYg-oxQWoOTDzttLX0qXyzQpo06sjgyw7ft0BprQDqN2WqSHWdL9mdUo_6AwPRd13iAg94LUktkxys0k6eBJEzP3Ic2zQ3m565DKgGYRmg0GAxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
المیادین: اوکراین از طریق میانجی‌ها در تکاپوی کاهش تنش با ایران است
🔴
ویدیو منتسب به تهدید ایران توسط نیروهای اوکراینی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/138731" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
