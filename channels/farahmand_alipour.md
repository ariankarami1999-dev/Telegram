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
<img src="https://cdn4.telesco.pe/file/HWYsdFxfi_56_sc7WbMUCbGMdc9hAyiS0Zc6Rh8SlhvEwDLi57s6ysXxi-lIvJNqnib3zik4WTo6RskMaRyCWgiSEmGBmM8jferbvsTs9fXktAEu1x7du2YwfHuhrIuYGapIfpO6MCNnLD3aLDxlUKvHbDx9DZm8xMkTuP8y1XPFVFAd_6HIUFIqy8AqZ36KxawuTQBXrioDhF_epjWdC6Op9GLqLBLIcwoaWKNKACRM3q4nL0MbT6224KIMnvlySIcyMi5n0qvloER-tA6zy6sZoY3i240AxblDcSJkLqLQ7vchC_p3-urQkaG7EJbjIJml8C1QRXSH99ML1yUTIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 02:27:07</div>
<hr>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if2isJUAW6XeM3cbi9dgilGPk-cQV5ajf8nvSQoxyk054DNKOsZ-ETQWi1SacNyF3Wafs1JiFI6021VrURAwEMnOnTHBWZ0JEW0ve4GDkGcLqt0yHJg6dpscN1v5pCY1nNRaxdmwwJy3VPzDgUV9pWZ1rPRk2tbFFc7lNi0ILr36rjJl9bvOyuUMPo2s6w8pQGKtaIP9twspAnMhpuFJPexVE8g9VUZ3ERmJnij9dmEY6ql_YnfsrhHsMPreTUzaOQ5l56wHnzA0Bmz5d3GfWzCOjBZBtk1T1V0PkyGbSuqz1sNRftfhA2J1q8Z1rEixOMtMxZd6CRy1XlUlqEDtOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnJoDBqq329PIGb4Afybo7MsPSivmktuG4l4eFtSRCTE8Q_Z9ZbvnQYUDu4AsgkPLCMJzGEZGj85ihCa8zN_IyCEaqmT0NAigLIko1O3wAaFZ138nO31LVr07-TguZaItVw9oioEVtK0RjafdXt021BJ40b-orsFlpyhw0HQN20E9jCNhG0OR9Y1LJOSn6gZmoAjwr1lGCGGEZF8804etaz1i8YjFvbjPZckZwIS5S9hnkPKzdnfnIqHbWhw-ag8u-4ofozs79Bd5n_yEoVMHY27_GWsEA3y8bVGpqz6VXteCdKD2C7-RC9THkauZSjx8bBTEqS1xYsSiELkEzyTPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnJoDBqq329PIGb4Afybo7MsPSivmktuG4l4eFtSRCTE8Q_Z9ZbvnQYUDu4AsgkPLCMJzGEZGj85ihCa8zN_IyCEaqmT0NAigLIko1O3wAaFZ138nO31LVr07-TguZaItVw9oioEVtK0RjafdXt021BJ40b-orsFlpyhw0HQN20E9jCNhG0OR9Y1LJOSn6gZmoAjwr1lGCGGEZF8804etaz1i8YjFvbjPZckZwIS5S9hnkPKzdnfnIqHbWhw-ag8u-4ofozs79Bd5n_yEoVMHY27_GWsEA3y8bVGpqz6VXteCdKD2C7-RC9THkauZSjx8bBTEqS1xYsSiELkEzyTPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spomz7bjOu2I5arbglW-35Spx7_PdN3RWptxCq-doJKbFk-6lWPrCZFJn_pYKqr_7UqjGUnpoHTbhGiH8CvaSORrszeWYO24nk2mbK9LU6fyyT12tzRb0PrRPHZZKTbM2bQdxa6wkUB_mK7zZNRuOc68BTROshOtec272ZdhtlBpQas41pZJYVP1V7ozgWZn9jQGVPum47q58-Ho3QVsLc2sa5mz8g2rfYET_ac3A16C-bVldyCEdgeWAclSuZnTLhg1OegTQh0mz-hYlnyUyeTG1LIJ7TBpGBO_bMnGA3peyXFdhT4tURIHzXlpI89bqRNiKVRNGcmdP0YhKTqSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=OT5qn2kgowITttC6QxBmCYAKTX_-QG1zqPFTWwbBN0nNKTwa3y9XSUQ7yH8zWBkMXFqu5YuAM6DRg4xdmZKyqeoKUh8UtqBeW4w1z0IV-MBUHcHPGbb7q3G1axR9LswZTIokPMmf_kigXdJ6Kwb4fwd0MhuycclUzZTBFlu3sBtYNWsXcG3E8jXQzSAkwWw6gOg8mgXu-YVSDWnd9jG5rdYeMuCbM2FSlgBG4x8gk4AOtzU8vVkSyQnBreG8fr-xdY3ZYVrXngZT1UU5skzAmkRQ2BZfnsDiI8nK4zJ8WM6hNz7aroBpbY3-owRYOnY4tQLejcoKq3WA78RLQqIACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Xc_LHU5kX9qvM-SpQAh2EshjvsMFi7QnIMN1kD9qUR1-jI2-HiOGVpXYO7yxB2RAv7jtczrQ3j-Zr_L_qLJRIFaYWrHBADel4q4X6tGE65a-CT62TF4OkYON0CUmiseLoOdlxaMJ8zTvEvrEFLEqdBZPRZTpk1PxBz4w2L5KmBwNpuJj3GNyVfRZoF_WNoZK0rt03DYOMeZFDRdQDZmGV9HnAh1NK2Nv-4X6c3dCeA-ccM867HTqa7vuK_M3oOWLcfnCaCrVLROCOdKynTBH8xPnuWxBGfCxfKLTx1XRYYRt_Suc9U0Ufncstv4hnR5Y5lYmGPqcc9exnbHDazUydQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Xc_LHU5kX9qvM-SpQAh2EshjvsMFi7QnIMN1kD9qUR1-jI2-HiOGVpXYO7yxB2RAv7jtczrQ3j-Zr_L_qLJRIFaYWrHBADel4q4X6tGE65a-CT62TF4OkYON0CUmiseLoOdlxaMJ8zTvEvrEFLEqdBZPRZTpk1PxBz4w2L5KmBwNpuJj3GNyVfRZoF_WNoZK0rt03DYOMeZFDRdQDZmGV9HnAh1NK2Nv-4X6c3dCeA-ccM867HTqa7vuK_M3oOWLcfnCaCrVLROCOdKynTBH8xPnuWxBGfCxfKLTx1XRYYRt_Suc9U0Ufncstv4hnR5Y5lYmGPqcc9exnbHDazUydQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=CGevgSG5bukOS0klFuX2LuI4cUUSeJ6mYMHmRtW-IVeuKNMqPP8qrwLCJayOrxFSObbP970IlPzbzvAh9vUPKIjU0LcFoFfnp9WhmnDjka9iWuKZuyXCVRYOezuwadR1g_Odye5nCpfEUOuuLoizGA04fPGHwV5pLuVHvb5BqjRrcZFNBmt9e8ep3EtZV7_VUCqElhjFkUld7WBO91JV-Oz6nebuMDKxY7RvMOIjJcNMajdEBdqw48wzxhoI3DELAkSifh81IZ7tIPJ0sSnzLuN1Ed85lSpkiCMzBF3AL3KPCnWPY28ry6SCbX_lHYGq8s5puOvdViDLcJC5C6I8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=CGevgSG5bukOS0klFuX2LuI4cUUSeJ6mYMHmRtW-IVeuKNMqPP8qrwLCJayOrxFSObbP970IlPzbzvAh9vUPKIjU0LcFoFfnp9WhmnDjka9iWuKZuyXCVRYOezuwadR1g_Odye5nCpfEUOuuLoizGA04fPGHwV5pLuVHvb5BqjRrcZFNBmt9e8ep3EtZV7_VUCqElhjFkUld7WBO91JV-Oz6nebuMDKxY7RvMOIjJcNMajdEBdqw48wzxhoI3DELAkSifh81IZ7tIPJ0sSnzLuN1Ed85lSpkiCMzBF3AL3KPCnWPY28ry6SCbX_lHYGq8s5puOvdViDLcJC5C6I8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it-RthdAPGrdl_tGeYR8Zfym_3-z4QI6yUph-PoagL41RKheyzeYATd9rD6O9iu5RQQRFMrUNDTXXg5c97QZ8s9XA_aOCQq9e75Kovdj62pD3vs3-XUQ7m-hHmwz6oCsOLvvuhOqab9b5QXi70rA3_PythfEZUl9QaH_K-uAUH9VzK8lIJKBt5oS3FtJgqaIPsTyWGuxREy-iYePjXMRoufe2Aim_8ssXvCLmY5nW3TeYj22Trq5CdCCD41YDcYl6yFlg_IhoKpPXEHLpghKTwSfgLAkrzhkqPp5qImCDhYFjiL6WM8kgPJLHxU3_0VEk-3rfSXMvbdfH-P6g-ptdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2uB8-PG7PyTsnw4XXYiPgV-ACtszVe1DmuX_ahu1YuXZ1pRZ0GaRTPnZgzLl1PFBHShAuEGxETZNvU6qTh3Ivx2059GkhKNfM0YMJB2ZLBSOZ-4ZHe0kjQovOFv4-zU9eeWrA_1m60g4vXfGYU5f3ZBZsFI4YukKk7LDOQurwEnR03QQVhBfZwDPlJFgivyNHz_VUxPbNZFw_0xQUFfvDPtMBJuKvtpOvisAJ4iThEjzKCehFUZGIPzhFweTif6N6kL0r1644pAKVftCWG0Asyx_waw9ZHtpTQl0G3HuE5NXjD9FTDan0QoF2zO_9uluK8Ytrhl353cyzPjgok8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=AYYjd4k82XZGTkK3MrsGg-lkHdy9hCtog4DYp017IUGcdm8WpFfsGDC4Q187ls-D7Wu7RD5jMr_iRKudmscPS8VMmavMdd1yqxe8JI4YXJscAmlpuuBdpIIvdYbvcuXiNheXPszKGAA4LqE4AsT5VnEZo45qtqol9y7a1d9xr6aHb4JfMKP-ivZurZ_DTXELQRwlZIh3oUpBiNxfqXEceLIF6jcNpydWCAOk816o0Nibu0dXkvMFenF-aOQGDXQhkmG80ui3GHgGAS4nshotRdqX9ywA835puk5M0zO91U0DVAH7q-v6U-BXRW8cVVDADcmCbJ5cEWJqPsc4FBdWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=AYYjd4k82XZGTkK3MrsGg-lkHdy9hCtog4DYp017IUGcdm8WpFfsGDC4Q187ls-D7Wu7RD5jMr_iRKudmscPS8VMmavMdd1yqxe8JI4YXJscAmlpuuBdpIIvdYbvcuXiNheXPszKGAA4LqE4AsT5VnEZo45qtqol9y7a1d9xr6aHb4JfMKP-ivZurZ_DTXELQRwlZIh3oUpBiNxfqXEceLIF6jcNpydWCAOk816o0Nibu0dXkvMFenF-aOQGDXQhkmG80ui3GHgGAS4nshotRdqX9ywA835puk5M0zO91U0DVAH7q-v6U-BXRW8cVVDADcmCbJ5cEWJqPsc4FBdWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugjd5jhK7RwlB1CYo_zEBJAnSyxr5MlV98fRkjSbkZqRFC58zbY36cxBoaGXslVnTG2X5irBJ_Go1CMqwJR50U4_SugaiqaiQbA5gxIg-j9jMj71mDlFa-qm98upE036JCEQL1pScAPuyeaoTsaSCOOORlLfN19e0lNwaawImb-HiD1cgqmS3fBsck7SMRz4kHjZMqOsSmroj3SoZskBSvre5NfCsmwIGrw5pwowMcFnIgRJBZqBqLYLAFja6plo6eFPCsBUPgspZxwM0ZyDreDGDxKfX8dyQotht90hKy2c3FG0GrOqd5yVi2_qKM1akbyqmJOb3T3n0V2LsvNeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsRAIFDKmhhy0ZedggxlxEY-DMwX0QuvVTcNxnx3Dth7pK7eJ5LwAg7T5unqTqtpLQ6hHyd5BnK4FCDPlZejdzn75pufolTkzKZ0IXCG8TXtJe80ovxDfr0IMF18wEFegQp-SuDQD9oD5H9zG_Nz4GrCxz-y-NtF_U69qU10RzX5idADglAN1l4kW1b464gBVhyuDr8u_wAiB8POxbkWi1EJsKEdc-caABHIYPK-8E1doR0gjQoGocdmHTklflIIif2vBoZY-8Aemw8RLbaoVFEaJd9_13s5Q6x3CizELVTFeF-eJ-GsxMnC-wre7qLdl05N57ZuAjweR_39zG9hzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WljizC3DvVzlZll3QR3k5ffVx7JJRKmqSM2ZZQfZmZ_t6PcXxJp_YBjpUKk4M9A7h1lnikPuc4FYnsebmLrCRyjxiAmTo4tErysAXnDhmm-zw7I5EgGQYTtrXLxmyJODwyXp4c6PgOQzfa9gGY6H-OYcBqI51hDLxr-JguZow9BdSj_nc8UDER1KDuBi77iaF_Mtu40hfoL4-o7FO8G9hpKKMcmabDRqbVVHBFNcvfcaAzaDgncJWeeCZQlakaqaPA6OwmXHcD8vMT_KxO0DGA4KgussJV_G-TyiqTTAmtj4WluqnDaxKiR83nZgqO9he6tPAfjSN4DpjOAqdX_Cpgkq66-tlMkyGSSuE6pbTl6D8u5sRgGFsmQvMULDlTzEWFC6w9wikYSF3JJxRBO4Z_n9S-zQYESuHZYM3MI2HyLKPZ-H1yI_qfwHGlgO7SoeFzZMk1-42uKwXSWDZikw5MkQgoDatf9ymWIVeGIuvxwtpCXcRJG1gPsn5LtxJWmCbQOAd7W58eTb2YYC02MBxPEcfzN7rMU37IZrnhMmPd0TDBu8-JgjjvEo6InxhFrTS1rSshLWKiK8oOZS9m0lURRq7JuzzCE8gT8nv8WEm7alkYdkmR2qQv7N79MHDCqprckWXuluCRrE6-iXAPN8qeSt-gchwya2o8QWi0b6_cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9EToCtddJjJMvRaV9CWPmoApWEh1HCadugx3lrAv72Y3RyoPH3Fva1qGapgzh1xGgBRohhtkHcRiHwoXAUMEkdt5C8OJJZ-e-LVQzp67vEYGmrZVz_nSr2syigpJRM4Apu4r10_qk28bdsNsMlZfEzYtzd-SQx4v5o5_4s9e0lPTYCTj-cZQ6PgX4OJRzcVH2RfVwTcXr-jEICTs5sfVJcJnEMARtO5avvXNvIxaKkaBrhJXTbaVpeVisvu0RIku7svraWSlGIEIiZ9Qpiv147IcoNMO_ibkd4TumnBesOe_6Dxlhe1ekSIvkERNi2B8EQmTOmF8OwEFW1HLuLwAKSg30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=QE3LcG46gkw5iKfXlYUvonlh39Uf72dLayJFLh4tzjns5aVJ6Bsii0zH_onTn2NRIepaIC1Y2vVe74h6XQg-pgBNmv3Vz4J7MUnTTqen6VU06liw1y8KSAtWW0ArM3SkutKn5MUAsHBMUz0AWQzXQP9OVjFJkMpukpdr6LfTawfwH6Vc2u7W9XTRWHKnhcVJAtMbl_x5JIUbYtQ6hlajfI7tGHNjqwDbC5i59s6ScXv5HGolHXa1zdD6taJ84q0kexVghi9JzrOVaTTgXGX2FKf0idiDaHPJEZ6RDr9mrPzRgaog9133F_YlSqxkByJaWGHS9gyOl3IcRNAVjfDFHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=D1LvJ96OWDgs6kDzJuSf5fEtxNg_E_9fUjdCwpC7sslmASjIb85r4zagcX_W8WXd2Nh5G_GzrMBf1wil-1SctHERWQ518Q7qHBOSV9jvCTu7Ogpc5dHyrM__QY6xKelg5bD4FLwDMLfNQXDH6D_eWBBlkzjLPS2mGXqzokN7USD-LIb0rZtvwWLWY2wrBG-WQVsLkVk9STejuFkVtGt9TbmR_UY_BtIN3Hces0ob4LRHbi1JpYF6qGmCb2Wwmj2NIjBvaMVUo5rDh0VzWRZ3AHxPZDi6yJg1i-jnYZasQ8A_-twmcKHgYMb_iR28_Fv-M0eRItBaZZOlL8C1tm7kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUtP6oJm-WqVxE0s0OXZPgSdIcvJsr8YhpM1oKp9-s70qZf3W1gPWmCFYRZNu4VksKZTKITYQh_k_9K0G55Ibi4pZyZvZC3DBxzVfuuf0CEFSzoZfMaFXzzSE5IX5hxq6DUfVtZDtfzBUH8W6_jGwkWAhS3rJD7kzZSXEQIQiVALLT6rmmosYjuuV90IgQP8Je-z6jiL3btf-_iocuwAn6K-bdFFngH2vcUCpYII9Zf2Vw2sfFoqeluP-11NVV0cbh2sbtZMjyU89JXll6cna0upyWXKaSlXvEybLk2NpQ6nWrYyFFRfu8zc8shCeaXvp3dzjJ3q1zfUgWfU1dCTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV5mprrmbYv15Q6DaGu_Yg-lIA9MTHIbYh7kY0mMOBZh0LP-OyIC0n2SzULFvnCndgic44Xv8msnr3xM8QYFoHWi7aJqQahgRYzef419H1AH8yQXXdcAumczRsDlZjRKXMS5lNsWoRX8Ne4HGIVmX8p6ZYhFHd0klIT4cFMB5cBMqBhqAzQDCcCvOkn4rLnc1SBQHN33NWJ7-llPWtbPL2tEWSzGrkJS0wSmVQuqLYhKWqegu13DY3TwLo6zqZz3wGo5AhIzOfSvqDKcnF7y0oNG60HrwC4S6upaDrxdf-MVFU2PdTjRUHCA3SlEK10dwgsDffW8IbR5YAsVX7X8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JztU_xTlUVt_fpbRI0-Wog6cPnMHMkPyMPImguY5zl-q_yiPiI_n0P-7n5paCoabOMMXzeSVVYVzFEkuXS64zsL9fLczawMPDRseFsrX3TqfyzC5wl5v2l4xed0em-WGYOfTp53j6aq5VhNsITSzUdo1n-3IwLS65r53S9u_BURLYb6moN8Mks-fR6o1QL7BYioNgwCI7yts4fu7enbQzhHZ35bpVXUDZIrjuCVq9Gctimop7hzZpT812Mhv9eej0QPRBIviIlfXB15vYHTs2Q5NOMrUm1cEMFBkcH6daXzG-XrOM2IlEYP5Z8zkcaUNBS4UBUJF4p3OMG4cyHUTjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrAIuIHJ1rpmgH9nnLV-MWaRY-MF2Tf3tS83a_XR8u8M6ZSRyGf_jCxnd90g2gjJ_KwJ-swnWgsHEawwfSMyWYZKRTy475M4pHYQKLPNkFGb4i7tE1kSgeo1vTcxWr2STDZBy9S_287DNAP1yOE-GQ9hLQ0Iev1X3gvSvSV3pkuDvvuRaXEzULWoB5MbjivoknSoQ5LCGmiz1FOL0VUshMsVpVep4_RWsqmt2bLMYVXsOhk_fvgrwnGBhDDwrd3Hzhl3jr1ZyjayLZu3jQ3Vm7h58TrPwhxeDSiA4BvtmBlWvqE0M0BLS-8rLCsh51WxSNFJOv0v7sgwnqeoUYsEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yoxtfii8wIqr6Mt5hpI-HK63nYZWB0TuBnKiBE2d-c5lx_pP7tFgSY_WY-ipSif2MxgfYGoKF4rv1sSmL-w0ayY3PJO9PduUz3P_vy_FJ6nF0lU1bO_LPcxhVaoriFYkYO6JxYPkzaLa22HgPcosLXcSpJDEYS1Qo9kuJ-TygKA5ByHKTXyvk1caNVxSux-nazU75iUNPMAzYOxAUhifpo0P1iFwfHLjgJFArp5WTqFkq0E8gV6-JkP5fI5tdznj6ej-WQxSlLMG858sxV8XwqfEQbO_IR5sVMusI3Vp7msgySqXQdVVhNCPYH4Fj9676x2XpHHc09buWUATO6bbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=MP3cwR81w0c0JaTxnzWtjwniWvkS5Il-t5vyoMXFOfS_IEtZY8AIVf4YmlVO6ChtvGwsqI5hZeT7qTk4NRXUIi5s_Vr69vltIrXnXOjK5dXgCjUwtKEqQkf1IrRlIcf-Y6ok4pYpqoC5iGSxDOfowfTk7sY9lULhkTiYL7EIrmCMVrLU8ECk4T2o7VgTpf557wq3zoAcAWytG0Tb3WO6wqTFJNRW8jNOqWznpzQcSll8g4v08wP0RjidhJ9puZc_4yTMjX3cUEzWxN3y60qWpiQTsL0vucc-Iscyj2CQriRCbdbpXeIsRp43fImQPiEkGfp6V54vou1yqYk1agr9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=MP3cwR81w0c0JaTxnzWtjwniWvkS5Il-t5vyoMXFOfS_IEtZY8AIVf4YmlVO6ChtvGwsqI5hZeT7qTk4NRXUIi5s_Vr69vltIrXnXOjK5dXgCjUwtKEqQkf1IrRlIcf-Y6ok4pYpqoC5iGSxDOfowfTk7sY9lULhkTiYL7EIrmCMVrLU8ECk4T2o7VgTpf557wq3zoAcAWytG0Tb3WO6wqTFJNRW8jNOqWznpzQcSll8g4v08wP0RjidhJ9puZc_4yTMjX3cUEzWxN3y60qWpiQTsL0vucc-Iscyj2CQriRCbdbpXeIsRp43fImQPiEkGfp6V54vou1yqYk1agr9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=uGX-TpKpse4_-I75uKzNEzBYpH56KYV7nxj51Am7LxIJDEc0hwrwGxcd-ekNoebUeIey5tMDU-5b9xHd2drvKvTmXcp0tZuc6VJySmAh9C98enLdXNEZzOVftnR5RxiMq9KQkSTtTKT3CRvWYdUk41Pfzfne1AtimWef_s7Q6ZYsgvKe3ZpAKR-fBISlJBh1FNU8ykkPL6P5D6RfeeiWHDYGILtVQ-OV3dPNxpJSrFPe6CJ2GmNM4iDwvHPf0wQz-o7Aa33KV06r4NioSi2bFDjAy0ApdWSPn8ilHqGascZdntlYA9OMGZdKl8ReQATu57ufRQ0Lq3-hZmF5OWdcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=uGX-TpKpse4_-I75uKzNEzBYpH56KYV7nxj51Am7LxIJDEc0hwrwGxcd-ekNoebUeIey5tMDU-5b9xHd2drvKvTmXcp0tZuc6VJySmAh9C98enLdXNEZzOVftnR5RxiMq9KQkSTtTKT3CRvWYdUk41Pfzfne1AtimWef_s7Q6ZYsgvKe3ZpAKR-fBISlJBh1FNU8ykkPL6P5D6RfeeiWHDYGILtVQ-OV3dPNxpJSrFPe6CJ2GmNM4iDwvHPf0wQz-o7Aa33KV06r4NioSi2bFDjAy0ApdWSPn8ilHqGascZdntlYA9OMGZdKl8ReQATu57ufRQ0Lq3-hZmF5OWdcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcT1qyqhqSxbwhXMQepLNXkJgqnaj8_nD1IU3LHqfqJmVl-X73WjPYeSxR4MECHKJ89z1tvxd3GUTxrE-kNuFguNOXgqRen9BUvsOwVE6UsAUHw1X3VjF24WrgO5WXBv8tamwcq9AYOV0aj44nNb3M-gsC4v0WEwJjYv59FrAnuEWZ0WPwULsjDx_rz12eOT_UXaJi22uqeJIwcjWrc-5OooYoimFyL6kj8RcY0DFRGWD_xj83TttQ8askqDwySq9Us0vcK0m7FSIBRPPki0rDcCdIicyxLZaR0uQP9j-5Rr2uKErkF7mfxtgr7G3yIf9S_cYrkyG1OSbN13Eu-Smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1jzrhOdwHygO4-5bEpRYio83YPGrNrDzNfZ_RcguQqd88VPB7tVpp1m692RTBbDdiLPBQ_QJL3GjNBERvyeq_Mk76LsR0dC9Z-G37puWnsLDAHTPzdMeVuHYU2M6cIPLMRW2ErLDj6Zgo_iKV7Cf3Ubgt1arAqjxxrgWfESFyJ9rrpB64LSs7yJy5ayalXay76xn3uWNQDCcBQp8Hh1efV0Z70LgxE5CqRyT0PQSRNyR-WwlNrMuVkgzCsYYXSEfBpCGC7xwJw28Jfw1wl1DTw6svcmOK3j6uBKrOI9irN0qwwmX5FovK-4hgH3613zdKAOMld8LJ8BLmOVEil-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=VVOGo2uhEF8OlMCwhdfakOUYRpeAGB46md_J7WXLRG7Xb1iT6Bt0cYicVeqSQjwKfhHybG_NS41i3X7Z6qjhtVQX6_K7-_2gdeS2wK-fMyqvBoCoIw7HyGjpiqtYVtZzffPFw6v9NhExM4zjZJwHEKwSP-U664hjyUc9Q7QCPqEpvTLWA9zP-AJKrLUVcY5cqFNi583FqQoPV-IusjbkUe3eiGtExAoT1DmRLOEAOopoHqyUyIely9-M2cOE097_4ll9QlDgMPBeFHLpvjulZGXZFHTAT4l_xXiYRi9c6TxAXqFO6zFtICyNeTy7xn8uUBVAZ7hOPuewwV31xwuBRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=VVOGo2uhEF8OlMCwhdfakOUYRpeAGB46md_J7WXLRG7Xb1iT6Bt0cYicVeqSQjwKfhHybG_NS41i3X7Z6qjhtVQX6_K7-_2gdeS2wK-fMyqvBoCoIw7HyGjpiqtYVtZzffPFw6v9NhExM4zjZJwHEKwSP-U664hjyUc9Q7QCPqEpvTLWA9zP-AJKrLUVcY5cqFNi583FqQoPV-IusjbkUe3eiGtExAoT1DmRLOEAOopoHqyUyIely9-M2cOE097_4ll9QlDgMPBeFHLpvjulZGXZFHTAT4l_xXiYRi9c6TxAXqFO6zFtICyNeTy7xn8uUBVAZ7hOPuewwV31xwuBRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=TxsAl5_Dx28oWK44noe7XZFF7-lhxCfHxLizxw86hpwjrK5ejMYUz1DcRYp7yWafqijiwq5NCZ587GLgqsgYj8dP1U57wWvz_qCxLxIgJAK-1SwkI2ymvbttW4jrORdHm3HSvf_pPlt7_U7d0r2ASh_HPvbvdvv_rP7AulIJCfM4PP2Q4sFfqMAsT8t_OgCHDg6oiKMfjULQ0Dib1Qgchk0xDhORLtOjVIpOBgtMLk-18NGovp4P2xy6sX57A-bODvB0yYUXDlSdbBDW4qO6OKX6FcG54hf8-kYz7yIG56yGf9PrubYdNbFkHMW9X0r1Xjv0xhx1tn-WqJXprT4JaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=TxsAl5_Dx28oWK44noe7XZFF7-lhxCfHxLizxw86hpwjrK5ejMYUz1DcRYp7yWafqijiwq5NCZ587GLgqsgYj8dP1U57wWvz_qCxLxIgJAK-1SwkI2ymvbttW4jrORdHm3HSvf_pPlt7_U7d0r2ASh_HPvbvdvv_rP7AulIJCfM4PP2Q4sFfqMAsT8t_OgCHDg6oiKMfjULQ0Dib1Qgchk0xDhORLtOjVIpOBgtMLk-18NGovp4P2xy6sX57A-bODvB0yYUXDlSdbBDW4qO6OKX6FcG54hf8-kYz7yIG56yGf9PrubYdNbFkHMW9X0r1Xjv0xhx1tn-WqJXprT4JaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMtBPjcJlyPvzZimVX-3LPg8YZOUVTBUlDq0wiF6SFqqqe2zd7TkncfIv07l51eYvkW4WHwwW0Ag-kpOpjZ761skTDamBU4VU9_fDFji_3LvO9BEfOFHvFae3PvZ4SeN7TKltw21Z7DFvtidomdL8JeDAlwieL21VT5JsGKkTYnoEwb2TDm4WrAGyXwNs1vdV2Tx0i1qXY4Dldkr8rtDF0g8Y30s_N9CLC6dUSYY9zxeiL8XK5b8KC-u_XwzobeDJROqBjbpbnQvLSyCwS64OL8YY9G4kU_pdpGj2QqJK6VR4g4lqTMfIXTJ-5qhZNnUyEQHE0KfvSDXG9hIW6_zcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSXdDArNE2IjXxc8gdzShhu8Xnh3INGU_6czHrrG-FRoX0QF1oToTYW_XAmeN8IG_eHEdyLrr2ezCUPumLONssGMeE3Q3ZUJJhv-Pm8XiaQCS-dQfO9pEeHa1oDAHUzNQg2k7MXSOXj2QiYWzhI5FQBPNItGcmxUfmR1YM4CTywy2jaWSdm1ykeF6K06zPX-oAYPxCO8sgfLbwVOEwmCnkRPmycassdhatcpT8rdIDO7CznxIceYAHoai-po7nf6KFSbTPtO8s52_AHpoRtAdIA00pl8H-9lhblbq0jYWfe12cSCemJNpLTQ5_UYqB0WlY9YPgn1vFYOomH7bsCoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_ClXVgNcUQ2oaOL1aK-2Iy1M15ABfrHFy-yzY2I4NcLkfZGU16tvEDHdgx2hLwBHCQU5v7GhJwvWcy6Yce08pxrdniimqQzaXODE2EQQNfEtn_UxibbDLoGYGkbS8bmg2-krgvFye5_CEN7TgmuRfaHzOxNRVXdrnbML4JGvTheKQ3EZwZZUOAqv1kqciKtFpVaNB1C1gWC24ptAYzI-dYC9s6hTnRa4tPNL3BEYviZAVbpVxyu-2z6H-3EfkGKJysWAk6R9uBibhc1ngCQpPYRXEPiqkRR8DVTX05wBJmcZ6Cz7CJPVhBMxQsa8T_kuwvUehsStCAq-1Ln98yfjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=S4p7jY30HMcSvbs7TqVE2ggdvXuRo3TNjoMvFW4cpsIlz50k1QX--b-z3Rb5dZsXvq-BBie9PFbShCx5XoFNOp9Vqdx5lL1cTVgy2ol8u1VtrX3KMY8uzKoKTZVyq_M-E032yE8Unh1CnQbIwnrvzLEr7wMUxvLluw5EiAhixz1MyFn4q037SD50C3lV7uwxuiYa8pnpKzrDvw6of-ci4p7tSjzXT28SH8xNMrZapdYAxsZIv2HVqn6ZdvxSpJJ8GJEwdAOi6ic_K0zpnu2MiUCrd-ZiSTD-YQ70KT_VR71KPjP3hLNZIrtq47nSjniFhrf7XCD2JkCpBaJdcjut4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=S4p7jY30HMcSvbs7TqVE2ggdvXuRo3TNjoMvFW4cpsIlz50k1QX--b-z3Rb5dZsXvq-BBie9PFbShCx5XoFNOp9Vqdx5lL1cTVgy2ol8u1VtrX3KMY8uzKoKTZVyq_M-E032yE8Unh1CnQbIwnrvzLEr7wMUxvLluw5EiAhixz1MyFn4q037SD50C3lV7uwxuiYa8pnpKzrDvw6of-ci4p7tSjzXT28SH8xNMrZapdYAxsZIv2HVqn6ZdvxSpJJ8GJEwdAOi6ic_K0zpnu2MiUCrd-ZiSTD-YQ70KT_VR71KPjP3hLNZIrtq47nSjniFhrf7XCD2JkCpBaJdcjut4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9cQPmIPRDwFWHa_cshnnj56uNfLLdTubhKWPy3VlZdWvDqn94J0z16klIVzlSGpCm6RbefDWw60l0wEX6PI6IZZREh5Vr5IN0wBOE7N4FGE5757GRlfvpfG1IZEARoXc-t-BtmlrQZhohOBhHFOkWK7_uyqM4S-ZFeP4aA2LIM-COzHevGLWg3Ng3OOpDY7Oo24v0d-S0o9IvUY0BBbt6yvxzHmCw9-LAbVFxAs8aGkjFRKLvWEthPltRhch_KEjO6Z51Jn9hZYU_KMtVE0YmvNoOIbDUZBiq9INGuopmU0Pc48h-TRCfIq7LoSA7jm8Q7SYFe_K1Xq-bD2MMtV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M708bAOoCrS7bSjDkfXPGXPGapQPjAi0HrAxouaMTBNGV1n0tI0M5S941jUEZFYPx7kffmEBLHyHBLcHXHmTR6Vv_7S7ubpFDSM-Q3D3bq_96ynyJ8xPXcnmARWcRRIvVDZ5ojZYNOeyDg-CnTRkEMpt-fj5joDUdMJ_PdZxMXY8XtBqSx6ctETt1bI0V0r1vy8R7DYsLep1NiZmojRsWznKo3W1jYS7gpbpaLji8UFmu8Id6S7kExpaQ384NI6yQuiPi52BT9a6CX6yH4_GaVI52Y9s80SKJu0_UMZZeMNDQMjb8z4f8pac7dqcS0TUEaSfz3sOl3lqWjrcfoXDvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZA5vH4AUymnwl86_nkzm9j_rvl4kjnzexDYCV4KGa3iVdBWxRp3wspdoI_X_B0w8PEaUESCoBj3qIWdYL1fzCHOdLbwj0ertGujziZbCq0wSZlFxrSW3T4t9V0HziU304-CrmDA5jxSV-tEkz5WhT2YMpIcZmJDT-7X6uDYEP52VUFm8UB9X9y6biV4fPwmkY2ggIeFNqU33He4Ht4gDVE7_-96c14kq_0Jz9RodNWNdg_FccfH4kIoyR7rzRgHfhU5AGEW1TKj22D2M_Bfd1F2jA8i-HXQnd28vGjW3I4TGezyMLKQOBZx4EvJ6gZzCCg81JIu04_Uy-EpWhBb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL79RUFNaGl3kS_ImAn3QTWTYJwKwqEz7RVzCreFTKaEah1V3x8Kh2MHnGd6v-oe3qxLluEF2jBA5SZxQsnq8xlUrBESXYE2kUFQNKpZ3v7UIitlI54Okspy8c-fdPBk1ZGXrmFSY4AOTqaWDM6w7rjFM1LU4Pwtewyh3hULd7BJ9VR9t6jVEA6UWOj-coS66vnsRl83BeGev8K6mPaz68PdkEkD9eR5TtaKPRQgJ6vMq9kG-2ao0u_S7Dc_zaWwCxO4h9-opafySuYoMWPl-8QzLPhdyGPEtc-h7DA8mNdCjQjyMUVzYSGEAJ0-jDBybdjW-DK6fhr7_wjwKzOwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=o4KPd_zYq2WawLLgThNDI_9I7bp8K-20HQPZamWR4C0TbSpEjlHpTukiKw1U3jhk9nSDYl9DVN6VoYc4VBilEEvBcmKFpueiffqfZ2KdfzmfR-Pax2GQjtTzLvj76KCvmzYcs9k5lmk9MeUY09FxxjStWFkGm4cosxbyDPQKDlwX6kD4R9Td0urQIKO5QxpAMMUgXrS-MvLUPLTCngNbo96_gH6qaLDBMk7CZC7SHxYOgyQAFS1Jbsm1XzsjFqF1veTPA3f3bWe8zuT70IYHmLqu1vepfNhXv-oLDNB-CxHQ0StpDCZOhKfv3Sf1GCC6NZEIGJ6HKj50qJhRCNshhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=o4KPd_zYq2WawLLgThNDI_9I7bp8K-20HQPZamWR4C0TbSpEjlHpTukiKw1U3jhk9nSDYl9DVN6VoYc4VBilEEvBcmKFpueiffqfZ2KdfzmfR-Pax2GQjtTzLvj76KCvmzYcs9k5lmk9MeUY09FxxjStWFkGm4cosxbyDPQKDlwX6kD4R9Td0urQIKO5QxpAMMUgXrS-MvLUPLTCngNbo96_gH6qaLDBMk7CZC7SHxYOgyQAFS1Jbsm1XzsjFqF1veTPA3f3bWe8zuT70IYHmLqu1vepfNhXv-oLDNB-CxHQ0StpDCZOhKfv3Sf1GCC6NZEIGJ6HKj50qJhRCNshhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De3UzDLBDCk0qn2RnQ22M1KXQkCqU7sawAq0I269GI3KKlK41c0WTiZYAuIE6UPAU4G12x0p2CeUMc0FaOdrK16WJp52ELxPqfr0rpt6AhoQg5MBVCHDlLlow4coI76H8brWsgoB4EiZDmgjydHOlzjF6GuYAKBUzOf8aEnjsQoNmhwyN7_ZDi5p20gCiUibjilkOZl5LHLTdIzN-ork3MGzd7iqax9GJytTMP9qCezhuhpRanqvmvdA0gwsR-9A7cser-iBcifortXwUBrZADssKOn72f_1CBy83kvFwkmNMj56TrA5TLzk9WGqImxGSM3CmCoDCOYctSQ0s9sZ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA83v4Cuuw8poRuSm6783kjsFAcIoKHaKikVBxBziehgwyP2Od7Sgrci9R1vnHYHRgUKMwdlRMAUKxPE6sydPhOFmJ58domGZNLzkRWqglqiPL0UNJQKEmQyXL_TBYrVP4V1mSzDZnPPFfhI6wBvqRNqp7CuxVK99BklsXfn6vhS1cSH7E0GPhAt3w9eULIzeMBi7n604W4i5dCtmYb3YoFUlbWmqxFu9vY8uesv9OPVTHliYp1MdAyjZHYbZnsahPWQ7m-Sddyx6uvhXzeAaHc9t74I5_fbcJie-doKzb6UVb7D9WSwyrCNob1YOTovu3rYqzZp8Yrc9ub65D0aFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNDXoVANFf4J4-GdKollEnIQi60CtsPb5ckkmoBJ6yGTSxgO_7D6hhpAPyVmt-rWnEMT_1FIwdq3iOvxuFiq5sxDnYouBwIf1_MDkrFmL0SDDpl0HBMC8H0kCJfsm_zJqqCHgYvHVwHEQDmgo8y-rnOg7ky_RUJxr6hR3Sz6lOrqgY3OHsWBZs-O5e2MvmhI94H7VhvUxy9xniT1r4iqnQ0n1Ei6jEaIkUbC1EDBAXcl0T-3hJhhQHmO7-FIFUQ_1JRj3dFfksDOka2wAnr3pdE94sofTjRdu5axvz0BwSkjDcG927nuz367nHXaPDX1zEQbsrVueqVR_9z9H2eAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=SdCT2E5i5_Cy8WRXrhiFgZUlFCX_xS-LPVerqHxVXs_KEO1ZIdQoIuWt_5mcWlLmapGCkmUQyHjtbq54F1dWCM8uieJV-hSvWK_GQ9N24ocyIO2Perfuu4ieg4MX4wm7crM8uWTVHi5z_4RdC1xsU3EOGn6hffQSMNb2NswUBmKQZ1p0fSgn8Ev7f_UR5Dm2kHahFTeWbOhLQztu1cTD5sDFCn6ZRjOdmbeJmaDnGI64VPW5YSJohj6U8K8F1slimAIFvekr4SzZlr3SjRwCbQp0X2T6_JhUizGZvPdFTqbEyGLAEG6-V4fHY9p3tqb5uZVJGokZC0AqkMRafSdGlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=SdCT2E5i5_Cy8WRXrhiFgZUlFCX_xS-LPVerqHxVXs_KEO1ZIdQoIuWt_5mcWlLmapGCkmUQyHjtbq54F1dWCM8uieJV-hSvWK_GQ9N24ocyIO2Perfuu4ieg4MX4wm7crM8uWTVHi5z_4RdC1xsU3EOGn6hffQSMNb2NswUBmKQZ1p0fSgn8Ev7f_UR5Dm2kHahFTeWbOhLQztu1cTD5sDFCn6ZRjOdmbeJmaDnGI64VPW5YSJohj6U8K8F1slimAIFvekr4SzZlr3SjRwCbQp0X2T6_JhUizGZvPdFTqbEyGLAEG6-V4fHY9p3tqb5uZVJGokZC0AqkMRafSdGlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Q5RrOB2jjAWe-li0W9pTPAshoHXbawLsnSuQNG5pjhqRq4y85bpQFICSy3NYFVg2E-07dtMQpzp10tb-WRMr4qR4glomSofmQXOVTovcjD-DHwF1VbLXYDLGrC_XZa5_HXe3yWvNsrR6sASmRG9ioE888sljVpkJ2zjww01i4M84oBjCg1iB78JgofEsbZ129gARvmDcOLTso7bqKtuJi5cK-u44Cp9dvSQmg9Cd8SKVFMupwrK7fPLvIh7DRrhQ_sfI8pJZoYYkNANslYiw2FC95OiE9L931cRRLLQVRNMwMRY6B4uoYeowVUuxC2LP93LTkYpg82TyFNw-E3NeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Q5RrOB2jjAWe-li0W9pTPAshoHXbawLsnSuQNG5pjhqRq4y85bpQFICSy3NYFVg2E-07dtMQpzp10tb-WRMr4qR4glomSofmQXOVTovcjD-DHwF1VbLXYDLGrC_XZa5_HXe3yWvNsrR6sASmRG9ioE888sljVpkJ2zjww01i4M84oBjCg1iB78JgofEsbZ129gARvmDcOLTso7bqKtuJi5cK-u44Cp9dvSQmg9Cd8SKVFMupwrK7fPLvIh7DRrhQ_sfI8pJZoYYkNANslYiw2FC95OiE9L931cRRLLQVRNMwMRY6B4uoYeowVUuxC2LP93LTkYpg82TyFNw-E3NeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EmRRxmrg4_A41BEu8GZCwP08YFBBA1HvVMwNN_Y2e2mYefS6M0mo4nDoH6o7BNBOjWRwwwR0xqAsfDdkl6Y5yvBpfahp0FJjLEWQ42o4n9cVZbvBM3uDiZ02RnaIQ9tyFOqZVZ2uzYrF0NT8xfa42JUV1te4hRBQEjLv18d7rPWl9W4-ZPLkvWI5swfwr53zr_MxDw27rxVjFsckZT-A89YMdN9gcPRm6dTa7wj2A26lCi89so0HZ2imW4r90DMtoP3gYp_Q1qv7YWZj7Zse6XSsqHvRIFIavsEHic9fZCB43CKwzQV-awe5WTK-wWhPq2kNhqBoYY9RPMkFJuERfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EmRRxmrg4_A41BEu8GZCwP08YFBBA1HvVMwNN_Y2e2mYefS6M0mo4nDoH6o7BNBOjWRwwwR0xqAsfDdkl6Y5yvBpfahp0FJjLEWQ42o4n9cVZbvBM3uDiZ02RnaIQ9tyFOqZVZ2uzYrF0NT8xfa42JUV1te4hRBQEjLv18d7rPWl9W4-ZPLkvWI5swfwr53zr_MxDw27rxVjFsckZT-A89YMdN9gcPRm6dTa7wj2A26lCi89so0HZ2imW4r90DMtoP3gYp_Q1qv7YWZj7Zse6XSsqHvRIFIavsEHic9fZCB43CKwzQV-awe5WTK-wWhPq2kNhqBoYY9RPMkFJuERfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBnACjdHydEwFnOaqTFoL0-IZNEw5r9JuD-XpHSaeDOxF72qjJmHXnKZEh0LbZh1KQXh2Wqf68fUBEOOhklO-CM63l_fCuKE5eOPi5_VO0VcIA8tNlkDRPDD3bG0ABNtC3lH7AhOeiZko70k-K2E9IB4fFxu1aSqQd5lUoTWe-3U-d11p9qWXrUcbZy73m0MY0sHvUxUex0PsLXpXUNcHWGu-00ch23hyhhts9mMlj5d3oTpH4KDCXhWVlT4OVyLgreatAKcHVJUmDUkZBJnGFCOVfxzva9ji5jB9R2HuBC4WkhGYVvwOwwWXqAysV6eDLIiEJb6Y2LUQg0OzZXh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulkL8A8AEh-niriq41ZR6_5gQDQr1-2vwYcp10nzCEGWMdma1nRRCaFQRNs5YWs8mGqQk1wnnBlBhg7UbUXeBkvS9E3lvmCcmVaKweLmikj0ctUUVAyUcLkCFpmRx9eW_43rMHng1mbEu6NLi_eOO3vql377IokCq5gsRw8CBK02BLEtKzq2V8hy4Pu0SGWqpr_E39W8dVMdxtKfFKt_HTu0m_CtAfI-7DZo0dRHqi7uW94q71l8y5pzPM5JE3UJrwuiZmMHjEwO82-RyxnPz9I1godDYzl911PRIZpOot2-jJSWOusCDmPzp75tmxSMWBWcRG3VRXEeJCZfp-3npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwKZQoecweEmxjFLiygapg4lgUv5mBa_kNkbtudnbS8QkXILUXdtbXASMdKwOS6SmP0ReQaM_CkwMYMd5RbmOxi0SM6T0PKSsqzinCtjjSO8PbQ3OSB4SoFpGz0cjcMtHkGHuODR7oilPsDU99r6jOmIvoDHbqIPUMNAbTJdAlbpnSm5OCyFPVW2It19jM3wn-s5YYGspvSZBi-Wa0xd5MWVEvKqM5J2Sts3S8bkHwuajf5qOxC2IzUkvTJ_fajtAk--nx-FjS5fiaohIrMpYbYPPlA9ZKa0S3RrocmTapSEtXBKz6z3hrPWAEWC5WjQKkderJ6Cbzty56mHy7CgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0Jyd4GX1pjYt75sPYOIXP4un_ZVWyL2cyxl5KUPrz3xWmfuG5J-_6iHkLki6VdBMKzkoB_x53djYoxgCTWVmjHjbHK8k-fLhFBcNIwUeczdOXvWksUGuVRnjhoK204pIV11cwNM-GZ6wu5YJqRWEaOcaHMqZ1alIYmYzObc2S02xW0jUjBVmyxygnkXkr6REtY7xYI_i89AS2jFL9rOTg6Vlcpu6tG4sJdprHQN1qbKEgPV3QslYToMwnSSlqbtBbxoz836YQz2-XMmV3JkcVZN1RRgGH1BCgxyp79GqXCRf35WB8fuCUFkQs5q9UArjy383evFilcRkPmsjdTN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpXmpomrCdW-77y0Y306viuezd71bH1VVGmAdSR_GlsdOVE7rVwVdTFDqPqMOkz8XnL87ZeAmSvqr6RU8QaWbPIX3qdQGjUlLyQJOX6sBC8u6VA6oup57SpNKGmiGLgYxUSEpW_tIeOHK3NNMLkzc9UfEcj27M5N7mSsHw-h0Arqjq3AWsNrPq0c9A5oy1erpgYDZf7m1LyIHDhFiFFrvdJFVptnP5bmchE2uaCQVqS33i7ANp_ydzgjrRhy9OMu2eRVWma89LipTprj2xcPbntYq7cMHJ1o0jf4lzvk89K8l11un-Lv9oEK0NLISgG3p9C9fXd_AiBryPl7kelrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOfj2sdfw49W7IdpIy7bX2tCwT4imJt92Q9g6ehqRZIWGcodXF039BepqNdwCWlAgR55NO19Hh-LUKteYlw-LkyKFgbf9dICme132tGz_BHtkxRir6LikA0spCRBCVKy6uO7yEEMu9a_d-6EutJoE8SDIkpbbQFCIxU4wol72XbAiZ7nHOYveQanCaaeRava76-IInd5KfxroHSk99uX5ReRymaiNSL8kyuIRMJC513oCmgn5K61A7Fg28NK24QVjmgev7JIg7gZYIX--8wLkIspeg8lIE2a_12OAr0CU-kkhOcTe0EfHzPEyZYNKdeL1BP7aoMsA_yXHZaythJBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_jMkeAx6RPw5XUtY2_a-EztL1L9ywHUBFjJP-kqBaUScH32V1x2AB6nS22OY7kdiJzoNg7pKDtO0rgfSmEhSQQ4AYifs_XYRHPJdREO6kaHgiWhdfE65lE5gD22hkicag6pPIHkq81FVMubcLOByqlcflsxs_uX1ZG_G0GkuKu7lma5LTSJLAwJerH-lctXfN9e22Y3ygUlM2w2gGZ1ZO89nZ9jdt-k22Wt5e-3faS-D3PFjlc9pvXeJYzs6mU17lmUAm0NKNcJl5Fu9WYU9k5PgpNb-8Ch4SCpz2brjDLXkuQaa39FS4AP3IiU5IcMj-8l6yWnuCZKoUiFkgmjyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-sORnvu-YYQvdXGlTg5gNeanHKPrZW6X3_15PKM10Qx307r8i3yt_ik6anILBVvhjUenb8-Tjmif7K6HRvXIcmpngaLVRoZ_d0slOiQz1XszhqcF1dzVa3zcJil7SqWMA-BZNwiAQtZYS8GaZ9zqbuSKVOKFhw5mkGrMmt2a0lnbKeU2AO3P2SUFzLfhwb2Mf-NhJoLFjoWJ3NfCkOQGRM2h0SKl23CRwF_haI8jVaPWGo5BJ4iYISbluYi40-UiHFqkTBDffiEJ0UbN4HzJ2cp1pR4RLrRhfPNcXOg371y1DeeoqwpdZojk8JGE6hIYAt4Alv5wvx8aSNUSS043Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dfy882QZwG-RqO-EK1GcgJwCRYKazSulCkQ0_P2ap-fKpFCNP3n3AO1w6nYKcjLqApBbmP1FU6c3f8ukwVBjPYKFiVOvYo9Xs2___c4rmUnmLsQdslbbwBuJpFiix4OIe3rjTCxts_iXdMErDysxeL4Ffs9bEsnt2fYb3_f68pDZcyYOe46lU1azWZHfCwtEl_7kq6bUa1tYvhnAWB5oZW4bczChrdyTHjFpZwDC5j9k2dr1ifaWWOU-itcO7GGsKRCEfLaWKZwRLcuCtf4LU2-z-pMHcNIqWVunjyjH6T1WJwtB105IY50scIhS3HfJKV-CpyB2dHTaVMIWoRftxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PltA8-ZXQV5OH4hv81AMW3XORP9oYtriGNhEfZ5wzDLWmspF2o66N65dVBGNufDWKlMM93zmoAtFZs2-olne7DjOBm17EUkJeg94NZQ3dyFj6clZEv-rPsf93xpzA15l0SlvwSoC3bXc5DRpJzCqLWJ7pbg_UqAs2xXho12jcMYpKHzMtmyqQUhvAMTOEUWRy4OPx9lCC4Ae4StDVG-IpxsKDsGh9oba9ykcedk9Csf9YJmvmJm7Ezg_stY7nI1FmgV4rni7gH3YpNhOOFWtBzAMU35v6W06XX_vf4wUTAU0kHFISZQ_WGbVMko0JPBKOzmyWQJ6Yxrblf2MZjZaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4Lmc_grRIKz2SaVLWPEaKEfkXNNDiS8ztk04kSUIwYYQQdf404qYDMXa33qQgNDm3fNm5fCfwzIkIt95jHA0KdTaU2SrR7fBCvVNQmgaWoulgAg_es0MAPcKmurC0nKVRfEd0fsSrxcW5BCoqVvFh_GhcsG813hWlrFdM0f-o7Zxs4-iY6EFM3ToZmn8mggyUZlUxUzetTg0QsLFy9NEj1R1zcDR4sZLR5dy28d4eX6btpARwnTBEt1c_efE2_h19DpNC7Ixe_sGliBaAxltMuZThTNP2e9NAelYj4O5iU2wYMaKYFJsTmNuiXiqfHx9WzdxQlgXPI544n7Lk4dJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2rOqDfC4-nrnV6W2AQOEpoxn-q-JutO27WPBe89bEBf5HrtqaKp-U6ifox8HJrRY5ahKc17U2k80Z1xVe475N1bwugQBfwBzqrG1Jg18cXf7FyPr_qkpgShDA76e3DUSTWwX_cI-C9ulsa7NbnvGQKsk-KHdWS9P3U2alhZP6Ir-EEccf_anD60kyfrQSLVqe8AgehSiNOWT8j4E6Nz3nxPbpXRtVYCe8SkS1SBB7tXUdWgWx5X_ug1VyOX-_q9ktnPtw461saCT0zGpVLxb-yE35yTGuuxo1QxUYdqwHr-3RHkVOr2D_eaxSB705A_FAQSUajLeO5ILMJXQKlRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyuXtC2fUBcsyaZHaiIzPnRl_3Y-s0Vb2NnqxoP0-YYo4q-d7vll-t2JBHRLHNRMlzpUqVgLd580ULXE8MnSfJOrhOplUbwLwU_3b92KFXq1YWbE1kU40YuqFlCpbT1IW_hXfcpcsFeJ2nUcztb1C7qnDJMg2wEXW3ApZlA6NvE6Ow64IPx9Z_cfu32HpZtSoLma-K7kiu14mWj_prNcFCd8Zp6rjdM67xfZEaqGXOH74t2mdAEhnyIonYCU99w6DTg22-NqSFkCPQXfsDcuSWbi4u7tNBqb94YyjmuIHw5XRnq9i1H_l1_zDhc-hXUfYHXkxBHMrXmd-YU4hgY9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQc6NDE_E5n0ettNPfEeRYEdGA7SsDQNGpd6QhcW5_4n3TN1Cst1kgq8LYdYSQvgrTTtL6LiWuNpBz34eoSA-N68ORHQKN2x_sKgSRazdFgcSnNHikUTTFOrtr9tMYn38LvtL5Cyh3a83T3RsS0KZfZB__GjrKmfpkYflkm9fQMn7i4RtgIlPdAj66cfWKpublNB2C2ptlLrsoW0fd5GZzHLiw8U-eEzBnvxWVFQiJfaFHcSLcsylz8UMdZS3KlS7M9xRfaCHm8WhRJzTQGJ44sIDfs8TtG1IclW5_W1eKkte4g-vUUntvnoZaKXhpZ3gPj719ZNphwawgedl3sVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axshr9V9XYvIpL4r-4RZ_I1WrEbW-cdtZlljsMpWKzUgKCdE_AyyKUWqK6TeYpg5PHZk7RBXX4RWcW7_L0jRvfcOVIYzw8frEbATyQl9F_jX2vEYDRbpQjQPi2iwnXmtPvxd93ni95ppnBndZHiJVAUVXYuOTLC0GAbDSBekBYjZeAO1yH0JtMFxKhVZiFZUu1r_HYlCZs02-vLJNRdSLd2lSbgN2bOorGlOGMA9YyyQfgjtbyWJ7IDliRP6Klt6Cm0w77vY4nRLqX6OfShGwNEECk5UnpVHkVgBa90SzWApt32BpExlv051YS36j5x6s3cQahnVFv2BFLWHFmiGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SN-VSBFxlapK0Sq6Uv6jAFr-lN26suhTVVkYIRSR26itfySQZW_cMBp93UVqj9ONG0L17rqTq5rx26IKvUcCgjThkE4oaO2GrGXouS6GZYIn-SHnY0Rdt0mUrF3QI-Tjfp1Axgp7nrdBlVCTHJHYgV-AOjjGRpyblmNsM9pNY6kHBjPStEbJIeaeyFxbjEgwamBjwr9AjMNSJb8PKGkiI8YXXVthlZC0UwcAUbd7hNsDffqljk7xS4X_b-5o0eND7twpnIYg9GHes3T7I8CfD24hiGCLfHe5faBQsa_AK1KmScKqawE9e8V359e_bxb5VySCvdXv739F8LI8a9Gghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=SN-VSBFxlapK0Sq6Uv6jAFr-lN26suhTVVkYIRSR26itfySQZW_cMBp93UVqj9ONG0L17rqTq5rx26IKvUcCgjThkE4oaO2GrGXouS6GZYIn-SHnY0Rdt0mUrF3QI-Tjfp1Axgp7nrdBlVCTHJHYgV-AOjjGRpyblmNsM9pNY6kHBjPStEbJIeaeyFxbjEgwamBjwr9AjMNSJb8PKGkiI8YXXVthlZC0UwcAUbd7hNsDffqljk7xS4X_b-5o0eND7twpnIYg9GHes3T7I8CfD24hiGCLfHe5faBQsa_AK1KmScKqawE9e8V359e_bxb5VySCvdXv739F8LI8a9Gghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ_J1aNxrxTvcq0q3OotexiVUKTOChbKrFnM_uCGMIeDpEszD8R859FxRdFsyMurQBwYwX_NcUueS-vTWAPmenc7Exe0erq2uXq1TirmgAqvEaBbV_Hik92ioq2KaLSYMKVNhENbb7ypNt7n-bhyKMF1YyTI3CgZ1RWbxMrMwGb_GsmhMyvat6kV3GERpPFznICkCOJdcOpbalxJ-xqGPBHo5O9G5hzGb3oMZHBphkztS2BCHcbpmR5qgHAM3zXBYlt4ZO_xC03CcQzOasBVhd1WnRmZEBNU0yTICUn19dyJrMu3QBcLvV-PfYAdFmr3HeAUWzhlKsNCB3N0MAEKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=lUs83TUs9Cl1FFrsE8BUUeeH7v30xaD_xl_V6tuQF35tnWGSdKX3IWJ6pq6NKEjdxnXlyz0YUR85XXSCgqsqQtz_iJHIZ5l_4NbjrO6yO033z1wj2JlTnyn182FUZqDduTHCFJgMlJgO5MHD26F6EWqRI-MHDXaViSmTHhSO4vh7kE4AiVth7GoqSnOnOKWFuZsrRYwWFw4k_-Snt_ofcykbXk8Q6SsJyfdOIcdY7raQ4_ytCerGmivLSdXUTuKDc5zm8-RkCHIosyv0qaB1Sudn-8mzbKLdzOUTg-ETNZkk7nit2_8VZPHJ1DW0f0Dr8Yhw2bQSjJzFfQ7YYcHUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=lUs83TUs9Cl1FFrsE8BUUeeH7v30xaD_xl_V6tuQF35tnWGSdKX3IWJ6pq6NKEjdxnXlyz0YUR85XXSCgqsqQtz_iJHIZ5l_4NbjrO6yO033z1wj2JlTnyn182FUZqDduTHCFJgMlJgO5MHD26F6EWqRI-MHDXaViSmTHhSO4vh7kE4AiVth7GoqSnOnOKWFuZsrRYwWFw4k_-Snt_ofcykbXk8Q6SsJyfdOIcdY7raQ4_ytCerGmivLSdXUTuKDc5zm8-RkCHIosyv0qaB1Sudn-8mzbKLdzOUTg-ETNZkk7nit2_8VZPHJ1DW0f0Dr8Yhw2bQSjJzFfQ7YYcHUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=NtmylAoa0YUzc3ArHtXnIm-n8CrZg3s0U8QWIK26pvo1GcNSeFq-ljae_eFoZQhqmubutgu0LIMuPmmCd632qXX8bHuSYWtSTAysfjpcFmL7YFiOaRiTt5cLDlkygBxENGTrCij631gc8bW1QDeWbF-ooLNAuivRGRI4LWalQOz89H0U-kBULN4bA72GNfdnOfk232Dmg85tVVxSmB2AfmPLuF8nSXfZwyyvW8VnUtvugF6er1n7eC3v6rEUCUt4n-8PsTr9KbAKNqYKWqVFKKheuRSaw7ydzyknt6MgF9XiggyhCrb4SkdEXX11M0tF3YqOLlCMMS9EYlZaUBYLMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=NtmylAoa0YUzc3ArHtXnIm-n8CrZg3s0U8QWIK26pvo1GcNSeFq-ljae_eFoZQhqmubutgu0LIMuPmmCd632qXX8bHuSYWtSTAysfjpcFmL7YFiOaRiTt5cLDlkygBxENGTrCij631gc8bW1QDeWbF-ooLNAuivRGRI4LWalQOz89H0U-kBULN4bA72GNfdnOfk232Dmg85tVVxSmB2AfmPLuF8nSXfZwyyvW8VnUtvugF6er1n7eC3v6rEUCUt4n-8PsTr9KbAKNqYKWqVFKKheuRSaw7ydzyknt6MgF9XiggyhCrb4SkdEXX11M0tF3YqOLlCMMS9EYlZaUBYLMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/havsQd7fshx1MZO89iSX6xIodVZVVn4q17u7PxGDiFVnU7d7Tz6qNKWIcxhLG6AxE6jHxkxXVOsHRmhdlxFf_3k8EIfEqIelqd5_sxGKD5W0LNidYIwNdPvvd6iRsxjoRdpLMcFDYtxiVJth6e-Z1_DIyHdCadLNA2I4T50JzHVtAbaEuvAxFuuidzJ5QOv1goOHR_T6hG_qWo4gr7w1eKPMEMP9gPmcKhvMuHTcENxMXvbDu8m_j9l0whq9j_CYciMhfW6DRjPU15gMsarB7hK9Vza3zEAzLM-vZypicGE9bhJ1qkKUkm3d7CpWxxlIQod3lDjpY-uEdE8_YpXNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PQWEBB-0GeAgjxJzTV22fAvt5dgTp80bkTP_9OkOJAmTpFfNI7wOkfiNp_22h2wFsUHVVZFu3vGErqNSa5wfGavIIv7KYUoNXU9_64MxwSoXWjypuZ6AwBa5q1sSLfjSrQYINQfbQPUH3fz8He0z9dTXIA9woKsYMj5sRjNGwFY4SzXahzfxfVRmU10dZKzflr6yh-1SeMQhR-a3GsIAKBZW3jwVulRwa9uRAC7t6oujJPc8p3aoswuu0nAffISDdd4eI2C8OVh_cTvOdP813yRL2Da3OOdlET3sd1gkDeuaqg0yEBoFUOd0hpxmXpTpMblWBlsaU4JczpwGu_zMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=PQWEBB-0GeAgjxJzTV22fAvt5dgTp80bkTP_9OkOJAmTpFfNI7wOkfiNp_22h2wFsUHVVZFu3vGErqNSa5wfGavIIv7KYUoNXU9_64MxwSoXWjypuZ6AwBa5q1sSLfjSrQYINQfbQPUH3fz8He0z9dTXIA9woKsYMj5sRjNGwFY4SzXahzfxfVRmU10dZKzflr6yh-1SeMQhR-a3GsIAKBZW3jwVulRwa9uRAC7t6oujJPc8p3aoswuu0nAffISDdd4eI2C8OVh_cTvOdP813yRL2Da3OOdlET3sd1gkDeuaqg0yEBoFUOd0hpxmXpTpMblWBlsaU4JczpwGu_zMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa-1rWKj8LUIjEi_-AOc5bBIYEYIeHFX_EdTBFe1Y16unOEr8cBfl5d4CBF4yJ7pmMwoqpbQVXRxAfXUrHep3IAkHMrREojZjo-1d325BgziCi7ADCkWN1ojauWyXaza2OvsLWTulSnBl5aYPra9m7-FldU9yoidcKidomqk8_tXLz1hMNiLSY9UEETtUhWTKI4X5q9evIAskgHlATyGc0WFUxhFI2fjoRmZVSE1ZOvN6bMGSDK8RAYgV-JPSFxwyBsdSqjmY8snciCD8B4IImklxiNZYSEB_Ke_G-H59n3CNLHpOsgP1TsgF84BTN9198z9QK70e7hDtEafWphB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoeGG8OV__XlsfvhrJYAQwLlH0p0kLNnzcQ87gz_F9y5A9qTVK8BWO1NO7ym7gAjjJl6m9iF52vWkmCpNVanCWjLbWyoOd6FBPyNAYycSzMVrmqPciOUqRUiIXYkYA8M2ExVhdZZ_-iE4WvJ3aRlZ2eJXeHefitRWSJHCHEYDl1GteQb-QnaTdAxGfbDPIVemKTT1y-wzp-0cu3vNT00kob32Th2hW0Y4rWL0G0-BS1-JzIh4OdXd0BaJ68gS4j65TubdJ9XdEhk3kOvqZ7kvHB6otmh5lPDedFF896IzDvaZiIBAQSaeObm5JFgtAlJbXPSai2ABiGF5m7Ih4IFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZSpLtt_-f5XI3emkdyf3lc9_576jhXOtqgE-aiuOsA6yYMEKBeg3GOGgcja6HXFJp901Mwz9AL9S9xh-lsQgQc6_JYRwXStHyx_RPECe7EaPdYh6VLWy9wA7p85NeqkNlD_t-_cHjRtg6X34vKJCwr4Xl4uJPHbBeCz2ZfdewtOwhDd3NaeUS3H3DsFih210x5Jc3Sq0fNHFGxP__6FKWj3FjQwyYWtw-CH0DbMk3Xp_VbDpOdW2FsZNlgsPr8wqbmfdvAg0PFTfG99tmASf1bTv51qdFlEONw50dLARYJ9294AoCKFe1GyAog9vlD_xo2EHxtBgVa5Vt6Ja3SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3uHNM1Xi8TB80MrJlHlSan7M5zAkqAdEH0g2f0EXcev7nHlVnNkh81BayHmFgiNTnXmM6RnxXpPPnqjPGTw_OW-Vd6822B4e4VwhK-h-Q06eiYE642aBNQmp2Up-7ajjhxrGUf26075JJll5pGDDQvgohYLKIHHNL1m5Bgiw0FFt2xjwf9FHHH153Ma5iahfLckM7sCOBTmq7IffAX0XstfIVFJwKdnoUt7BtF-zS9xd1t_NzRk2BIn1l2dNp3EmjvLTK6kuRMA2Rbp8hniFq-njnyTWYjuaW9D4hJiQR1wUJ0x2sf3TcCK50JveJrXVRmDQeEQFBYbU-TAk4y1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vaU8XjyLFLzbdnSeOO5eqlG4moybPsFefANWHg3rerjZucx6_61G_yyovfKgghbkegKEAUIzmmFAyv95mn_wve65VgO0hQ61Cye6ULn0HjZaqZzU1yFiTNDyv_8wCq5_e6RYTcZF5gvx7ZbsRLo8Plv0RMCjZfNIVZW5Dn6ySI8OIbO1tSADBN_kjggtgrB6wGbJCqivPL7iT8opBVO0UiB1AQBVnT7gwpl2h1QYTXfXwLFy9feWwdSLZBFUwgnN8u4SfUm4kxDnNMdtv32IIN4-lS9fjACgL9wdsb58_jKyfp8h5-BFoa02682-zHHuFmvssZVIpYEmpbDQ4urKbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=vaU8XjyLFLzbdnSeOO5eqlG4moybPsFefANWHg3rerjZucx6_61G_yyovfKgghbkegKEAUIzmmFAyv95mn_wve65VgO0hQ61Cye6ULn0HjZaqZzU1yFiTNDyv_8wCq5_e6RYTcZF5gvx7ZbsRLo8Plv0RMCjZfNIVZW5Dn6ySI8OIbO1tSADBN_kjggtgrB6wGbJCqivPL7iT8opBVO0UiB1AQBVnT7gwpl2h1QYTXfXwLFy9feWwdSLZBFUwgnN8u4SfUm4kxDnNMdtv32IIN4-lS9fjACgL9wdsb58_jKyfp8h5-BFoa02682-zHHuFmvssZVIpYEmpbDQ4urKbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=R-voSHV84MK14jx7wk1WxXpDtq7TzCBE_t07e4cqE-gMWe4cYj6dMYzwy103Va4P7hBleDBYiPI3-hCh6uUuWHUNQybydTVkEj0T7a3RbzNHIErCws14P9NxtkCmL7xMfO7QSdC2mqNrlWjfrUNiKKLlOBeKSAQjVUhSvkE8rVB4_kSe0WJYiNfjSyx-7l3GSiSU-vigMEHWoIeSVul7sKLQ4I78TKMmJEIAEgZJq9hZTWtsUZIryduJND6Gc4YU72VcXQGwXQy_0LqLcI_wrf_Z7i7i9oFXN8O_ldEnD_jd-X9CZhINCirOLwg597gkZRAYhVgNRBqq4PiNnR5TOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=R-voSHV84MK14jx7wk1WxXpDtq7TzCBE_t07e4cqE-gMWe4cYj6dMYzwy103Va4P7hBleDBYiPI3-hCh6uUuWHUNQybydTVkEj0T7a3RbzNHIErCws14P9NxtkCmL7xMfO7QSdC2mqNrlWjfrUNiKKLlOBeKSAQjVUhSvkE8rVB4_kSe0WJYiNfjSyx-7l3GSiSU-vigMEHWoIeSVul7sKLQ4I78TKMmJEIAEgZJq9hZTWtsUZIryduJND6Gc4YU72VcXQGwXQy_0LqLcI_wrf_Z7i7i9oFXN8O_ldEnD_jd-X9CZhINCirOLwg597gkZRAYhVgNRBqq4PiNnR5TOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=RCB__fGKjDAny_2it3rPwGjT7ohtfwIJxguOcwzVWqlWySkE-umy1uTGg3RpYbqVV7viuKoSh1pA8Gf77Tz_HTIVR4mOQvNCXgSLRTj6uXASftJniMjuvXX6LwNbTNL1XIM2Juv8wdbP2dPu2ZL_iHpcs8O9hIHupsI1G1JDhqZx3zPv5yRNrWNsv_EfC5ouMuRJoj7lActnK8NKtye6Tav71NjnmSDanxnEB60Zaq7ddX_9XpqWvNcxV9xphgPu3KtisjDNTVVSdidayQKCDtpbpsa7KYWBaFQvcXs24ZPDPgL4t6jwn6Ue4pquR3Oq7Fw8I_BZdkevR-9UJMUp4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=RCB__fGKjDAny_2it3rPwGjT7ohtfwIJxguOcwzVWqlWySkE-umy1uTGg3RpYbqVV7viuKoSh1pA8Gf77Tz_HTIVR4mOQvNCXgSLRTj6uXASftJniMjuvXX6LwNbTNL1XIM2Juv8wdbP2dPu2ZL_iHpcs8O9hIHupsI1G1JDhqZx3zPv5yRNrWNsv_EfC5ouMuRJoj7lActnK8NKtye6Tav71NjnmSDanxnEB60Zaq7ddX_9XpqWvNcxV9xphgPu3KtisjDNTVVSdidayQKCDtpbpsa7KYWBaFQvcXs24ZPDPgL4t6jwn6Ue4pquR3Oq7Fw8I_BZdkevR-9UJMUp4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=TtcGjUIYR2doFab73H9n3Nl5hvgIH14pFuM2xKnVoTJpjBCc9HZRboEwibOCYbaDeVofvzq00KqfjIrlhD0k29nE0VCU_Tj5h_PmpyOEAkZ3Hc_K7ktkNVie8dBTzha4UCEGopQ-i8krWng-kQqw5BYINpZFfDXyjfXn9Be9em7cWhQ1JMFrjWG71hYVdiKM2iN18CJSDf5uOOHo3avdtUujFfsXHJp-WNpN1kIjxswVqtzo_K4xyTxL-ubLGUl6urJHjvsQAH5FtGr89929Ch2x4_sm6VsIU82BKdliKDg4btNPxy4YUsO4Smsqn1IhkN4aNFPGOBZCtelibJmn2ltO4f9AAONLw3D0pd9m-C_BE59UZ21P9AEoKavYHSqRKdm50ApuD-YCRvF6pLpWLubH2XBYy-kSjV6EaJFdHzXr8t1tKI5Kk0QlSba5QLerKNy6EjUuCBkflsfxTiK9WOqElXzZAmfLs8Gw4wlszlqejIdbNqlssf4npl8RGSkMD5e5nKskx9GI1kh_aeAVRKK4SDIstOk0pQPMpuL_s6bf-oh-UY_nJC5qnX8gnKoqp3FUMsmPv83iOv205VHHR8sY7KsigRu-1mD9xQJBhKy5ibvNsLoyIna0AW15nHV_i054vdilCikFW1b5cP_YoQTC0MHBNAZetU27FsfiehA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=TtcGjUIYR2doFab73H9n3Nl5hvgIH14pFuM2xKnVoTJpjBCc9HZRboEwibOCYbaDeVofvzq00KqfjIrlhD0k29nE0VCU_Tj5h_PmpyOEAkZ3Hc_K7ktkNVie8dBTzha4UCEGopQ-i8krWng-kQqw5BYINpZFfDXyjfXn9Be9em7cWhQ1JMFrjWG71hYVdiKM2iN18CJSDf5uOOHo3avdtUujFfsXHJp-WNpN1kIjxswVqtzo_K4xyTxL-ubLGUl6urJHjvsQAH5FtGr89929Ch2x4_sm6VsIU82BKdliKDg4btNPxy4YUsO4Smsqn1IhkN4aNFPGOBZCtelibJmn2ltO4f9AAONLw3D0pd9m-C_BE59UZ21P9AEoKavYHSqRKdm50ApuD-YCRvF6pLpWLubH2XBYy-kSjV6EaJFdHzXr8t1tKI5Kk0QlSba5QLerKNy6EjUuCBkflsfxTiK9WOqElXzZAmfLs8Gw4wlszlqejIdbNqlssf4npl8RGSkMD5e5nKskx9GI1kh_aeAVRKK4SDIstOk0pQPMpuL_s6bf-oh-UY_nJC5qnX8gnKoqp3FUMsmPv83iOv205VHHR8sY7KsigRu-1mD9xQJBhKy5ibvNsLoyIna0AW15nHV_i054vdilCikFW1b5cP_YoQTC0MHBNAZetU27FsfiehA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BpbB2nUNm0WMW4LaAZNxJBpUi3lIEiwGZ2igRHeiHoLWhCt-eOHCx746aGF7PBhVzhnoDzIF4y5KsgPESWYRSsOhlvAX2EYLEh9_cTlXhLfTp8bXnxy7uYhhRSUZBun92PK46iRc-4sG9znfcEFej7OECjRj8p5TAo2NvbZCdd9QIidKnKth_DPINJ7Q06EUdP9CUIEcfdYN-RF4tHuvpY9I-b8CwWIb3_ppcwPWDMHEL8-ZWTZ11q61G7xDdmv6-rnKDxZGg95mHklxQ4YWJ-5L9g5jloqgHXxCPwhkCm3_65av5KUqVnfc-wQ50VYfSHzmpowbD2Z0InAuVQVaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BpbB2nUNm0WMW4LaAZNxJBpUi3lIEiwGZ2igRHeiHoLWhCt-eOHCx746aGF7PBhVzhnoDzIF4y5KsgPESWYRSsOhlvAX2EYLEh9_cTlXhLfTp8bXnxy7uYhhRSUZBun92PK46iRc-4sG9znfcEFej7OECjRj8p5TAo2NvbZCdd9QIidKnKth_DPINJ7Q06EUdP9CUIEcfdYN-RF4tHuvpY9I-b8CwWIb3_ppcwPWDMHEL8-ZWTZ11q61G7xDdmv6-rnKDxZGg95mHklxQ4YWJ-5L9g5jloqgHXxCPwhkCm3_65av5KUqVnfc-wQ50VYfSHzmpowbD2Z0InAuVQVaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=k7iTfPHeAs8Diam7lbFU_9QD8yLt_8FPDekL3MVXtIGpV3BCA_f5Rv21KzqC-UKLknH3HEI74yGzyNF59GB5ktv9za750PiL8jQDtGCUAzfqtWj0STiKU3w8yu46_-Fqyr9uczUg_TKc0A0FeBXjIkJJ2EDpjHBTlOKcTD3eaPwtyPjj1LLHN5lHNi2VSX3ULz0bMQFb9P0f2sw88JDKKtCs5jv2uxEIVisjBAQrFSMucWdXEaSkAaW0o-pvNlPWMqZD7Y-a95Wcm3QTULOiCssmd3fTEloai5M3C9tUudL5bywOrIjShpFyF0TurKKwVqhl3kNlOBe8IOnYMPM7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=k7iTfPHeAs8Diam7lbFU_9QD8yLt_8FPDekL3MVXtIGpV3BCA_f5Rv21KzqC-UKLknH3HEI74yGzyNF59GB5ktv9za750PiL8jQDtGCUAzfqtWj0STiKU3w8yu46_-Fqyr9uczUg_TKc0A0FeBXjIkJJ2EDpjHBTlOKcTD3eaPwtyPjj1LLHN5lHNi2VSX3ULz0bMQFb9P0f2sw88JDKKtCs5jv2uxEIVisjBAQrFSMucWdXEaSkAaW0o-pvNlPWMqZD7Y-a95Wcm3QTULOiCssmd3fTEloai5M3C9tUudL5bywOrIjShpFyF0TurKKwVqhl3kNlOBe8IOnYMPM7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdVHQchzjmFj8qyhpCKWMkVC8Ji0wjweWVqUgX1akvYst2W5ScYkNupttAvsajuk9JVpEDqQ90D58Er8XlMml_Kz8Nzs3BSov7Bt9vTYxo4B8GSeTcY8LEmp1tLtc-j9czhqtODMrd7NgmzOvI-xtT4PJhOS7nc9AzJZj--khFb7B6EuUHPN_lcxFyfafyUO4AVWFB_qAuKokygePe6MDVhVOAEY7RnhAe9ORdny-LHhxRnOGMu5C4Mn4RIhc3PV7wtETfNljahFSFPwZQ2kr4F1Yv0XbywzUThfZg_oE0MIp40PTp1qKqS8MFx9bM22QjfbSkRXxsErC0KcesW6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=scMpsch-SVQ_3cFvVDiro78xmB-0CxOBJpsjxFCmL80LauwxjHidmszx105fsoWSvwKWkrHfB_i7TELvc5buuoAo5Ctfh5CJw1BRvg-toJ5F31o8xAoH7XObVLoz7bfYnmVHbDCO6BQGDKD3JL5LJg6ENOycArTCx69c216oxbYBZbHzgpPM6Tqc1-V47QWTCKkUXtgL_h-f3xnC6LsKIkQqXT2KLGMrQsOIDODTDcgzHXG8dGM6tOgEQ9WZruzig55S7dGTs_EM7TAUXNWtV9mgtA6y790cE2rHeabncJ2Y1A3IcB_bjil6sZ3EVaZsGRSEi9Fb9NGJvLNNwqmk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=scMpsch-SVQ_3cFvVDiro78xmB-0CxOBJpsjxFCmL80LauwxjHidmszx105fsoWSvwKWkrHfB_i7TELvc5buuoAo5Ctfh5CJw1BRvg-toJ5F31o8xAoH7XObVLoz7bfYnmVHbDCO6BQGDKD3JL5LJg6ENOycArTCx69c216oxbYBZbHzgpPM6Tqc1-V47QWTCKkUXtgL_h-f3xnC6LsKIkQqXT2KLGMrQsOIDODTDcgzHXG8dGM6tOgEQ9WZruzig55S7dGTs_EM7TAUXNWtV9mgtA6y790cE2rHeabncJ2Y1A3IcB_bjil6sZ3EVaZsGRSEi9Fb9NGJvLNNwqmk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hje2hDwBwyOrxHMi46_fIrL56s9zQ21oRsvvI_1coN1HqsyfwjP2LvUZZLW033m0MPpejdSpEEC0YQo4ZRRG3sqIoMuQNmZwCWPbrThqnqWs98jX5eGh91dsiR220fLqMzE5cOVPiTD3eC1xId5vc_gVniv_Rbu71wzlGasKhCs00xF5lB3jNRNgITbNeK-QWvZOLTqtRxS0u6IjAohkfIpOPVgUU-tnQC1rbMvrVU87QuqpmtcOkiMyqk-2JXG0RICYVUp2n8BCIpxCIQYka229V8mEdXX-_hC0U06T2HHKIUPxtXpTR9b-RgMj10cJnUIrr0zMlqluF47tGIVoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSrIUiaNAhQYgcJ31e3e6LenUWGR57LjezA1CA383o_ZrONS73QZ-N1-Wk0Q9ePKl-kn7VZQZeMlMI5vjw6r2Iai0DXZALyL1ZFW4PcLwo2G5CIvs_ar5Uhkp1qIdfnXupMlylG9RYKzQFKqX0s97cxqacSxRMKIA4LJGDNFu_e8W05X9PmL03m74CTYuBwTMi6fZhJqlgH5sm_mTlo_0M_5uz5q3bvl_25m9YO1dTRWRjHaFBt527o0VFiT6FQUNl8aBe89_d7wveBgRwvqU9WL2soNxq_GnzBHeua-ePUhS9p8rkHC4L5AmtWTtnNcvwyFuaMX8Elglc92_rzdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=lOM4yoDUP8jXORLuAbMhoVGO779GzUGG58tHeONyKiP-KbXst4EoUmp9uqWUv4etVvWdYV5Bab23UqSScePmmzYG3eZt4UvRyVqlnbc6mwSuE4eOtK9Z5edoRlN_lbo9LvEMbKZqZFZ4fQAWYAW-qYA7DI99llfoE8OF91G8eGmK611eARVudNxmuKumN5TkJilviIPN864UlQQRdUyXlWlmBeVmhwkYXIgw3_cNdqjm3OwxQxKRi30-eCVmHCDbLX9FWYc-wC3HcYrrE4AUPSp39dw6NWA69QQC3rOlIJ8hB6Y0gn46dE1XJjCnXJGYbyAXjxNphZUgv_4q9pzTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=lOM4yoDUP8jXORLuAbMhoVGO779GzUGG58tHeONyKiP-KbXst4EoUmp9uqWUv4etVvWdYV5Bab23UqSScePmmzYG3eZt4UvRyVqlnbc6mwSuE4eOtK9Z5edoRlN_lbo9LvEMbKZqZFZ4fQAWYAW-qYA7DI99llfoE8OF91G8eGmK611eARVudNxmuKumN5TkJilviIPN864UlQQRdUyXlWlmBeVmhwkYXIgw3_cNdqjm3OwxQxKRi30-eCVmHCDbLX9FWYc-wC3HcYrrE4AUPSp39dw6NWA69QQC3rOlIJ8hB6Y0gn46dE1XJjCnXJGYbyAXjxNphZUgv_4q9pzTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=NU33dl4Tu5xkSk3SzaBmtaJ-ajCqod-RaTIglNLbzLOvOyjc9G8VNadkU5_D1FiYPBuVT6AKTURx01-mFMDYKoATfIAkypXbvJuVrTObTTBLKEJa7_yHNuaYjg1v6MtOqYDovY6dy0sGvOWR7dGZOjFKXoF1rwmUQ_RM6CYh-4hj1_JJyrF9BrI6OnAu5Q-iQOWq-SBP_3wJ3UO64oHzSpGfxvIxs7FyK_7OWQMRO24Oey31gydZgKlT-s7bpP_0mhXLOvDeBXBox_Yq6hrRfkcseU0OK00KWIvxJZDJV2CTE1gykllcLCh-4c2Z8s-RykXIQf3lhffK1fzO4-hpFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=NU33dl4Tu5xkSk3SzaBmtaJ-ajCqod-RaTIglNLbzLOvOyjc9G8VNadkU5_D1FiYPBuVT6AKTURx01-mFMDYKoATfIAkypXbvJuVrTObTTBLKEJa7_yHNuaYjg1v6MtOqYDovY6dy0sGvOWR7dGZOjFKXoF1rwmUQ_RM6CYh-4hj1_JJyrF9BrI6OnAu5Q-iQOWq-SBP_3wJ3UO64oHzSpGfxvIxs7FyK_7OWQMRO24Oey31gydZgKlT-s7bpP_0mhXLOvDeBXBox_Yq6hrRfkcseU0OK00KWIvxJZDJV2CTE1gykllcLCh-4c2Z8s-RykXIQf3lhffK1fzO4-hpFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=uB-UxtOCxvEt2KeXKUMDBTsId8dg4vk-wiXfvw8or-Vw7vLfJxHBkTybGY0Jk8FxYap931Daywns1mdi0mgv2JY81KRmVGO0-GIpYYrx_VGZV5gV5tT4TOU5axZXJCCGw2cWRtiDOlLy-Vz7pkRWnzuqkO3fMPAAgfe8ttWmlatDr4vJViKMCiiZTZnT6PSeG8FL7GMEMOebc6AkHfrZVPsqxfGAyLQZtxayNk6Gs-i6l5sLMa1QTi_Jm0zNOsMEDNI2vUWFb0HfQRoFgTiyxRKQx32U1GUpdCZCzhkzonUvYgznLS1pmxbWy-AN0hbq-30L8G9AJJKb7hRC93b8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=uB-UxtOCxvEt2KeXKUMDBTsId8dg4vk-wiXfvw8or-Vw7vLfJxHBkTybGY0Jk8FxYap931Daywns1mdi0mgv2JY81KRmVGO0-GIpYYrx_VGZV5gV5tT4TOU5axZXJCCGw2cWRtiDOlLy-Vz7pkRWnzuqkO3fMPAAgfe8ttWmlatDr4vJViKMCiiZTZnT6PSeG8FL7GMEMOebc6AkHfrZVPsqxfGAyLQZtxayNk6Gs-i6l5sLMa1QTi_Jm0zNOsMEDNI2vUWFb0HfQRoFgTiyxRKQx32U1GUpdCZCzhkzonUvYgznLS1pmxbWy-AN0hbq-30L8G9AJJKb7hRC93b8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW4zzBZcQi9cbegK4SiA9XFVaYh-6fjq0Uqq8odCAuWydiVIf8nziZa_bWC_gWEc1H3at-GU9LWAHL3nMwuJc_u9uSCbNtdy4vCDOUElnf_6Uy3JUmaxoYwHhYTUxayq17Ga4iBzgBxBP0V6B9NSGOkIrEshrX_B6qJCA0lTOdHb0qL2ftG3M5ZReOKgL6Yj8rWqK5evlQlvIITD75TrfPFOV2OWAYrLIpMBJI8DX_rH00WuJkjKxITUVS3o2m7ht3ILaKU0JazTGn0ZF6ZbOCta9B8irW8fBtj1M6BGrYy5IFYQh7atEk7g0F7gW0PasL8XFNkTvG7afhS-1LNkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=fTPclWZfitv7lCXaBznC6MUaYetirFfgn3HeXKBezmnV3B2Kf7HOoBtUEQTm4X_z2dggn-LK1lfn7zZlOy7jXOuTMpBMmL9VG9HwWL2X4LuWLW_mWjtNqYXTZPuIuRr0fkueeUogmq9Z9eykeae0Iw4J7XbGalz8jmD-YG8bQddtsseXw4Sifw2kqAEN4pnXm4asy7IIIAp_U-HysQHpzIfFaX_6CgZC6Xsf3MUwsvfYuGZNksP4WIXjl94jC0NxeMf5Fumjr11cHz5CFGau36bB5n-qo1d2lcy8Ves9HRV7zZoe3zYqa2tUj8pKFbpmS8ANnxY-s_uwChu_C4VkbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=fTPclWZfitv7lCXaBznC6MUaYetirFfgn3HeXKBezmnV3B2Kf7HOoBtUEQTm4X_z2dggn-LK1lfn7zZlOy7jXOuTMpBMmL9VG9HwWL2X4LuWLW_mWjtNqYXTZPuIuRr0fkueeUogmq9Z9eykeae0Iw4J7XbGalz8jmD-YG8bQddtsseXw4Sifw2kqAEN4pnXm4asy7IIIAp_U-HysQHpzIfFaX_6CgZC6Xsf3MUwsvfYuGZNksP4WIXjl94jC0NxeMf5Fumjr11cHz5CFGau36bB5n-qo1d2lcy8Ves9HRV7zZoe3zYqa2tUj8pKFbpmS8ANnxY-s_uwChu_C4VkbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=lT8f6FNPl6vc3dhP8CeNM68BIGTPslKsXOkyWPgvkwB_5JQ3f2hZjFnkTKCGG2K7vLzV504FdBP_huh7w2ducC5vA9-GSXyI7rx373-eTGJX3Ppln3FDlUHbK3mPhzsEW_4QwNTdRUQX2sywIm5qR9KXEOrpW0Bu59z3x48LtsrVYRs9X9VBQzyDmt-3zRZ5ZATZ29UI7RqrLdYHmVL2VWXc84ErKz5tbZvPczPnjGosMfMgutnms65ApyXPHAINhIV9Q_mwyz8-thMsqx5EckLKBXW5Nf7pJkzk4kXNdFvWhrr2It9DwX_FjtmoVwrYCoSok7J6kJis-hWA3Z1AHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=lT8f6FNPl6vc3dhP8CeNM68BIGTPslKsXOkyWPgvkwB_5JQ3f2hZjFnkTKCGG2K7vLzV504FdBP_huh7w2ducC5vA9-GSXyI7rx373-eTGJX3Ppln3FDlUHbK3mPhzsEW_4QwNTdRUQX2sywIm5qR9KXEOrpW0Bu59z3x48LtsrVYRs9X9VBQzyDmt-3zRZ5ZATZ29UI7RqrLdYHmVL2VWXc84ErKz5tbZvPczPnjGosMfMgutnms65ApyXPHAINhIV9Q_mwyz8-thMsqx5EckLKBXW5Nf7pJkzk4kXNdFvWhrr2It9DwX_FjtmoVwrYCoSok7J6kJis-hWA3Z1AHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
