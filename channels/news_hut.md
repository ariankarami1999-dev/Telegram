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
<img src="https://cdn4.telesco.pe/file/puVy353vPb7d6UE4Gagx_fYfykHBsEkUqxeYAxpYXLs243-rOQSgE-wioe724d4EHr1uHyCnXaHVC0GBlUj2UEfKHZJPMi6qSMDFkYT1qvxbIZiIFct2pR1bKZYxB4FQYKFhCsHhch2xIc-H9-gX0sq4ItrSWywfIHgQXI5L5Wd7iXf6GbbdXaC8eqv8pnqz_PeGj4ht8v3labKRbIdtZUIUjLNu3I7wm7fF1RPcmy1NsFiDRHcuGaQRJuoCkPAcnTAiQ16QjuHcY-fHA_9updrAW63PsugthGpRpkyGy48KYAf70-HAtSdFtuqyPL8ATWsOguX1957MytrI_eFdfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-66093">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
زیرنویس شبکه خبر:
پاسخ به حمله اسرائیل قطعی است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/news_hut/66093" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhRwEQ4K0SH8mwiHVeURiAm_b-cHjLi4KGqmxjuq5nzU3gmQ-6pxEF-Q3IP9wc6AdXzLFtaqiheV0xcayMiLB4NaM0OUAXzVjfTZMrE6d3w9IEvdQnPiWL_Hnw35foKGRphI4YioV6LhsqP-Xx3rKo59A8avIVh-Te18_fQCxIFlP1iikpGuv4q-3u7n42TNlXY08E9IUu92wvOEWjnZQroENLTAYs0itLIx8__yra14taOUVogHeuhj0zONgQRPiGur98pXIJmQ-yj2pKGOJT7tEOeL-aN3JXUk4TB4xuUCiUWhITJGTcbPm8HnoPRDsilMOJeGmWMIhH_Mp7_12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدباقر ذوالقدر دبیر شورای عالی امنیت ملی:
‏
پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/news_hut/66092" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه
#hjAly‌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66091" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66090">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOnZxYsNcbowskh25nP8sQUPWot1XNnwIPHTCdbp7b2grziEOmh9oyq7xSHUCBrlKuNXMOLNqQsFMibT97bMegzNbS12N5IG6nt-YbDSZ6PpKum13kdfGkT2qH58NsQPcSsOnWguBjVvfdHLqxUVd2mnsXei2pXf18TbdDK9LFBNa7uoAVa_axzMF_cBhVs7v654xpuVNuyhksDspfOTSXbcTQzEitgeChsh4bnTW76uNIh9o4ICwP9g0rhioeEQU1_U3MeZH1k9CZV6Y3rIAaQIVVVXJ6GR15Yr9gWcgQtO4c5kgqHywBV6GlS-ZK0fE2eJoIKHbwx-m18z7b7azA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66090" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66089">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66089" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66088">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0qkbhLZQzCl31ZbEcC2d5udGeNhgg8XJ4et9l3XushVPXop5sDmqQC7DjII51TkpKhHtC1As3nvc8FKnP41TKO866b50cAXasoqIxpr188JK3LZ43anla4Sco86ulLSlH2ZTKmJnfh_hlOpOLkFhk8eNfYwYvPL7NF-0Q2sECgRbkoSGjSzSdbM0hC5-wesvrnsXGUO3kHjIRpF74glW05ogspTbVkRVzeb1RLWSFcuHmft5craQS9iSBuZ-2fGCEUuopfiIrmRJpys52J6CInMfa0qVumsbtaKsSJyjRmCQqG8MQ64CgEGvsFQrpjFq_i6jUvt22OMjiTnQBWw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/66088" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66087">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ به خبرنگار فاکس‌نیوز گفت انتظار می‌رود ظرف چند ساعت آینده توافق  با ایران حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66087" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66086">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0IgXfVQgwV5Bfefk-f6JLZYS8qh3NVPoF6ImJ6LxO1EA1zzSdjyo8_6W3V5vCZo4hnUgRRKcyASJD-qU5st-YlIi_1drOzR38vsfzmPKQL0IngJTJDFpMt_OoJrTyzL20f625DzAexTQ3AnftBu8OMjQEthZCIdoyQ5uso1OLbnKW1rXm2GzVaelF-1onEDSFpcxTuY6eud2uUZ8jC7PdINCd1SUYNcAYSzi7KGsYtsagmW6YTnGTxsB4Eat9JEU0j8xXNt942ZlJodLGXAK5elS3HbpII45AqryPOGzytZ5ZDiHwfCdgG29NcqvCJbpA-8lQeGg26EiVL7QUXIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید: رئیس جمهور ترامپ در یک مصاحبه تلفنی به من گفت که معتقد است علیرغم حمله اسرائیل به بیروت، توافق با ایران امروز امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66086" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پزشکیان:
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
رسانه ملی در حالی بیانات رهبری در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی "نه جنگ، نه صلح" گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66085" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0x_nxc__lmvKZJMpgWhXZ97WgHuZcHfLu6Nj2I5CyTRkFtO2g2WRRQJ94gBlUhKZRRmce7U1WjKrIeUygBHegDsgMrK5SRnby1Caq9YF3Cwcd-JAlzzvdi7vEw3Z01059wyZYmCQf1bJRR5iUB6YEQmOM5fav7GcBlK9bLuu_-lDIiIPDPsW94nBzfn3fdRZ1pqURHFVm9PsG1tBtWYYZFsrwAot5ZT8g_dYjK8xMrPyNtmPihqvEmVDtOkT8BbzlQs_n82adJn4PFRo_16yBjiXGIQSm8s3vvO7Fdr2TVitA25dZOtasb1q6vIM3DJot6CirFoVL2ytiW3L8uXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ در مورد حمله به بیروت:
«این نباید اتفاق می‌افتاد، ما به توافقی که صلح را به منطقه می‌آورد بسیار نزدیک هستیم. بیایید آن را خراب نکنیم.» او از همه طرف‌ها می‌خواهد که عقب‌نشینی کنند و حملات را متوقف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66084" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
وزیر جنگ آمریکا به سی بی اس:
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت توافق با ایران را مختل کند.
ما در مسیر امضای توافق با ایران هستیم و مسئله این نیست که آیا این توافق را امضا خواهیم کرد بلکه مسئله زمان امضای توافق است.
اگر ایران میخواهد این موضوع دوام بیاورد باید افسار حزب‌الله را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66083" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66082" target="_blank">📅 18:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66081" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
احتمالا طی ساعات آینده ایران به خاک ما حمله کند
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66080" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5H5jA9VDGtBNEsbtswQ6loF8cm1jElc6yhSqvyTH18y-LKo3c8rD-uFUMHQS7ugpbpdsYB43YZABoq9KmLi1CJ-jI1IHEkY565tflngS6bkZc5HvCnL9ZuoNzrf04s3nsUwzTqvKk5UdlJk7-SpV86fBFbDrOOUXFlKs8P2J60F3akBFhlkLsThJ2ZttQwQYciZ6TFPFrbAjJVsbOGuWE8XGuYxHICtPsBipDMPS4Ixm82PZfEjOcLrjvhD2t51dLSiqBglI1SeRsdUnfBIwcvDfH8rMTjzcOcnTyS13m7NgK9M8HNup3QO_tvT9lOZJ4GRpvll3h7bhtqMlnMj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی:
حتی اگه توافقم بخوایم بکنیم باید اسرائیل رو بزنیم تا ادب شه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66079" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXE9j7TV7p3hR-vXlvNbHVhMe_IEZCgRwJ5Sa0Ex7qtPBsAJrAEF3RKBBsblp7q3mk-g9kht-9KKoFrzU4_ypZqn6n_KMdP_XEbM0gQcS7mVFo4yPKIHzaw__yomgrCvP7DVZv85xCCfxcckjMHKwKCJAzirXAJmfaQz3ECVWIMxVKlKNSzyv0aFr4d0RwaWKfYn7eKTsPp3uzs9H2WKBi_MhedndwDtVekawdBwsG49ty76SsMJVHuVDzdustCNtvrxjP9O7LLBRT1P6JoEMCwdUK2c7ldBapeHlbZdYT_u_oS4BAKEYNcXuD4Ufi7y5S8BDkmd9A7e4Ze6i4NHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66078" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت اعراب حاشیه خلیج‌فارس توی این جنگ
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66077" target="_blank">📅 17:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66076" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه!
#hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66075" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a237733a.mp4?token=BU46FiS7NG0c89kpZ85fSJjj2M2JtrN7ZO99pCOydA0IIhTSmtcejf6jIgDs4ZRQh04SaW0GsWIZLxyD2lYAoZEoq83pHBNUA_VogVVbKHbu_mkcnS7IooIwwqTtpevWgqkk8hp0QMm1hfVmJxROmow6gqdTkCI7KUZC8fkOCj8I5ynylFxRWbhRviWFReU_Wax12EUitFjrXqXjFpUexj4blJYWsRzKzgNwTnTKm-fcxfzh9i2kUWoVGzTQdE4JP8Ww-6xCeF3Tbahz5Afob_BF6hNnZw4O6b6lQj3Fz3OagA1IXfEJYmVUn34k2uqy2BBzpzRLMbQ_nYqf8lZzeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a237733a.mp4?token=BU46FiS7NG0c89kpZ85fSJjj2M2JtrN7ZO99pCOydA0IIhTSmtcejf6jIgDs4ZRQh04SaW0GsWIZLxyD2lYAoZEoq83pHBNUA_VogVVbKHbu_mkcnS7IooIwwqTtpevWgqkk8hp0QMm1hfVmJxROmow6gqdTkCI7KUZC8fkOCj8I5ynylFxRWbhRviWFReU_Wax12EUitFjrXqXjFpUexj4blJYWsRzKzgNwTnTKm-fcxfzh9i2kUWoVGzTQdE4JP8Ww-6xCeF3Tbahz5Afob_BF6hNnZw4O6b6lQj3Fz3OagA1IXfEJYmVUn34k2uqy2BBzpzRLMbQ_nYqf8lZzeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی نماینده مجلس:
اگه میخواید این تجمعات شبانه تموم بشه باید انتقام خون نائب امام زمان رو بگیریم و این انتقام تنها با محو کردن اسرائیل از کره زمین به دست خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66074" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyM8K7LK7oveGtSlA-TQaZE8QRPZRpcwLv2s8Bs2p91Ei038XMAVbYvvQFa_6isgTYMrrEi2cB4ejLNNzC7m3u337F7RhJihR1JVBlWKC9vL358nCwrOX3V_u5ARt_U0tVRaoDq5E6InhN6WKZJyJsTM6sTfaoute4z-5fADBjHIEHmpsmMcjfHbxdkXgZIBkojdrYA7AGVRzd-wI-uoUYHBblpamMtigiOEoGNXXr96-wKvS9hm7OkDnnkDGXIw9FiIjO183vAhWH1V5FjBp2CTE-Ms8PQPIW3XZORSYC-3G1yFGXmkyHIFHTJpF9ABDM5ByJCcgaa-espLq7iw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
تجاوز صهیونیست‌ها به ضاحیه باردیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.
اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66073" target="_blank">📅 16:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی:
ارتش اسرائیل،فرماندهی مرکزی ایالات متحده (سنتکام)را اندکی پیش از حمله به بیروت مطلع کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66072" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66067">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: رسول خدا و همراهانش در جنگ لت و پار شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66067" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66064">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که ارتش اسرائیل از حمله به ساختمان حزب‌الله در ضاحیه بیروت منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66064" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66063">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
کانال 12 اسرائیل به نقل از یک مقام امنیتی:
این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66063" target="_blank">📅 14:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66062">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
کانال ۱۲ اسرائیل:
هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66062" target="_blank">📅 14:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66061">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66061" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66060">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چندساعت قبل، اصابت پهباد حزب‌الله به منطقه ای در شمال اسرائیل.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66060" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66059">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66059" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66058">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=c0oxsHxqTajFRcppAuaA2oCBo0NT85HO1Xz8J7d7NCB3NF_aUcO1bdLx0LrBfAxyGG9fbvh0B21nthgNpjN7_uIs_tZV4xAxHul8Y0rjB5kYLuy4ZULkGG6cQx8EiSW4ZHODto6UeCigjh30CYfoo5T-zCXyHBtXs5H90waEG8CW6AlYSu22BV4IDuT7axDrfaFY5zPyEnK9CxGubd0w3hfU44RMkiHTWehvIK5JVoLJkCguhOWwSyiWRwfyjctjHZ4YqykqOhHDmfqvx7beFcB6h4iLj6T9EceYyRQMJJbSAA0nMjj5lBk8HfQAS5EIrNX8U0DoYn3ykHtKSi-u1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=c0oxsHxqTajFRcppAuaA2oCBo0NT85HO1Xz8J7d7NCB3NF_aUcO1bdLx0LrBfAxyGG9fbvh0B21nthgNpjN7_uIs_tZV4xAxHul8Y0rjB5kYLuy4ZULkGG6cQx8EiSW4ZHODto6UeCigjh30CYfoo5T-zCXyHBtXs5H90waEG8CW6AlYSu22BV4IDuT7axDrfaFY5zPyEnK9CxGubd0w3hfU44RMkiHTWehvIK5JVoLJkCguhOWwSyiWRwfyjctjHZ4YqykqOhHDmfqvx7beFcB6h4iLj6T9EceYyRQMJJbSAA0nMjj5lBk8HfQAS5EIrNX8U0DoYn3ykHtKSi-u1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66058" target="_blank">📅 14:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66057">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل:
حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66057" target="_blank">📅 14:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66056">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoFHTXa9IiBAWWN6AfrEO0eB3DuHCzy4w0q0WslERl4osyxSKcQjv36K3JT4Blr7NwEPWq-VrZ6AsuwxlmmK6C-IXRXM1EGoSxIC0ax2YwK9cewt7hLaui9XNhrXKlZRShJCvnGMiDLxEZ6hxzOUyQ59bt41Sk8CCLhmyolCqzoEwPpCaC-G22i4k-8FxvR2sS00Nl3lSzKi7L81_1XqI2cwlgINRYe3njFQNqoTs-hoZYoh9Vkqj5LQC3T0AMU1wMxPnChFSJRDFRySP-z9MJ5O-Tbn7eMjJvAu0AwGs6HYdWNZxE6SIyOcou9CTT5cVwGA_Bb9AzBItORz7qrzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه نتانیاهو و کاتس:
ارتش اسرائیل اهدافی متعلق به سازمان تروریستی حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66056" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVBQekkR2H0dRgTfELLj-XOzcrQgjbIlqd6PhZ47f_hIcnRSGFto_-EZdMpaJ61F9gSWC7Jr887U2FLxre_cu6VVMUqW_sKnJVyT-zC3ha7G5nUT8CvP99cnD1195QnBq7QunqXYkE71UGik1sICpV7UHIzPItDBjHAv8N5CU8vM2etc-j9FnUxTPgKZOD38JNL-r_tbIqQ-diAHw0WZMz6AGBBeBtgExNsg-JdlYx5AmqVO8977McMwekIxTmPO7aXAZGmK6UhUIr2rek2F0osfsWwqx772GpnOwQBuXvCdTaRd0Rfl8IxjgltOQb382ftFPRPwcaItOeswqCte-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها ازحملات اسرائیل به ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66054" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66053">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=olyAvi7fREZlyu9k__ZSjlMWhTfI2FJDjXnfh21U3XOPyqi9Fw09vIM-5LLJ8GPrjNLaHKitJar68zVpkanZ6HFHBi0rbwoHTdaFNRTR-fUnLhKkTiIdtNtIZOlwg5jm4Xd1HCPnif8-xx2UsbjB_nq_mtYmXv0PYR9YLk2_PlbtbAVpWiiVDxmpjtrAYtRCBdC2foutFeOe78ZCkPeovnoP2clQo5DIc0FwOmvog2NiW3UDDM7pqyEEkX19Y12QcUNUkgsmrLKeDUKjqEYI5-D9Q7ictjGyejee9xl3O1On1gHutEVvdZRi4dkxPABYSdaD5qX7HGryvXjwn7bngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=olyAvi7fREZlyu9k__ZSjlMWhTfI2FJDjXnfh21U3XOPyqi9Fw09vIM-5LLJ8GPrjNLaHKitJar68zVpkanZ6HFHBi0rbwoHTdaFNRTR-fUnLhKkTiIdtNtIZOlwg5jm4Xd1HCPnif8-xx2UsbjB_nq_mtYmXv0PYR9YLk2_PlbtbAVpWiiVDxmpjtrAYtRCBdC2foutFeOe78ZCkPeovnoP2clQo5DIc0FwOmvog2NiW3UDDM7pqyEEkX19Y12QcUNUkgsmrLKeDUKjqEYI5-D9Q7ictjGyejee9xl3O1On1gHutEVvdZRi4dkxPABYSdaD5qX7HGryvXjwn7bngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66053" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=NXvAYgIzrwiYDeiz7yATBYuQJ7_Wjp5ulJwqr7x-1NIOHQR5ungE7J_RAB8Wr_KYupLjcV5kqZi3G_4Mb_yLgbESDLzLj5W_T6qWiG38_Q4RKrU4A6SaqEymLFarmManYlrdyRHTw3MEuTIrSGuW9ox1k7dnpRCPhOAKCIhNA0GZDYhiWKrIodoG56ZWeLQNmoEZ9BRPpgtf1MbFMD1qjYS4Ao8GocnZcmxHa3RwCSaDJce9_6jzYtmOXGOlHAa4T3rsrbYkAaqxeGk1lM1IcbBgzff_Wznocs1yRz8fGmPOb_HukZqnq6NTTNLSqBJkDcOl5LZnK5B2jP7BzWzm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=NXvAYgIzrwiYDeiz7yATBYuQJ7_Wjp5ulJwqr7x-1NIOHQR5ungE7J_RAB8Wr_KYupLjcV5kqZi3G_4Mb_yLgbESDLzLj5W_T6qWiG38_Q4RKrU4A6SaqEymLFarmManYlrdyRHTw3MEuTIrSGuW9ox1k7dnpRCPhOAKCIhNA0GZDYhiWKrIodoG56ZWeLQNmoEZ9BRPpgtf1MbFMD1qjYS4Ao8GocnZcmxHa3RwCSaDJce9_6jzYtmOXGOlHAa4T3rsrbYkAaqxeGk1lM1IcbBgzff_Wznocs1yRz8fGmPOb_HukZqnq6NTTNLSqBJkDcOl5LZnK5B2jP7BzWzm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو برزیل یه دختر 21 ساله رفته بانجی جامپینگ یادشون رفته براش طناب ببندن و انداختنش دختره هم فوت شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66052" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66051" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3rnOzZ-6IAHWTYVOQ8PpsPGqx7lrhgVSzOqjLm4ekVzyPEgp2FBIIjtnO_2HD_8PJOlTokhBzt_dvV2oCCfeCxThP8kpMt9NB97C6hyRFMY1NQChHUSwpCMOcJm7tS3B6TYmT6CpoDFDQ_Bzgg5gM2YpnWYZrISaerwqH-mhTg_Ger02EWuJ-KQaGR398vq8ZqxOcv11CUDSH0tFIi_USZaRFVxlQWq4p98yR0wqIGUCBuVtvxBNALUP7e0fx9jPFWIR3aYIf19uiwCzKkR_s6ZCa0jeCzNTyIAyhXLyWNTDvKodEYOSoOlu_UXd4RKqynH5Y62w6LHSQulY50PDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66050" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36249809.mp4?token=mfnaEVMbY8F9s4m0vunzbeFOi5hcXU9ZBvqD2TGoW-AkPuSPFjVW4-x-iUO0BpgMJ_MtA-I2tJoJydOBE9VHtzwkuSdVA-Qj1G_n4lq6ce1hFR71mLc6pAqDSJySW-fjBjpP5RS_QcoUUuamTf2DWwQk86wGmFD_46LBacP-D3JjUpOrcIuIyQQ3KdxEEKNrYH4i-4SANgQPpsks2H0r5qXDzVyleUGu2dxsZMqXApPRuwdiBRBzD-DzfQHKs1gl4_nnEmfJ7IGkbb2Trkvko-ifbiRlYqZatKsr91mka38RguE6qP-E-7_Y2c0bHcXKkokJK83gF7erqcmY_mSSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36249809.mp4?token=mfnaEVMbY8F9s4m0vunzbeFOi5hcXU9ZBvqD2TGoW-AkPuSPFjVW4-x-iUO0BpgMJ_MtA-I2tJoJydOBE9VHtzwkuSdVA-Qj1G_n4lq6ce1hFR71mLc6pAqDSJySW-fjBjpP5RS_QcoUUuamTf2DWwQk86wGmFD_46LBacP-D3JjUpOrcIuIyQQ3KdxEEKNrYH4i-4SANgQPpsks2H0r5qXDzVyleUGu2dxsZMqXApPRuwdiBRBzD-DzfQHKs1gl4_nnEmfJ7IGkbb2Trkvko-ifbiRlYqZatKsr91mka38RguE6qP-E-7_Y2c0bHcXKkokJK83gF7erqcmY_mSSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۱۵ سال پیش زنده‌یاد مانوک خدابخشیان جنگ میان جمهوری اسلامی و آمریکا رو اینجوری پیش بینی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66049" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
امتحانات نهایی پایه‌های یازدهم و دوازدهم به دلیل مراسم تشییع علی خامنه ای، یک هفته به تعویق افتاد.
پایه یازدهم: شروع از ۲۰ تیر ۱۴۰۵
پایه دوازدهم: شروع از ۲۱ تیر ۱۴۰۵
جدول زمان‌بندی دقیق به‌زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66048" target="_blank">📅 12:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28745391f.mp4?token=ftVH9lmfyib7gtYmnxt14ofchq7QGrZGTmcHiNtZ3rwB8i9PIk-TeQPZQKzTO16CIQi1JmRa7tg08rCQ0-8pDW1igXv5jfaixVRopoxVescZoBjCaNgAZN85k-ZA0UAt4e47xq8rhyrYLi6lNXrN7xy0h3bGR_Kh9nDL5PaAUA-pPdRfb7EbSOSIFj0MyQhUtCqnQlpWkydvEuQUBufz2hTGlElSm9FoFcA8uN82-tsNaI_issC0443QTGjUd7vei2-1xgavu4B-PLzAE8yF8nrbzrlaQj9EmzUc49S1JvjJXl6582GFWf05G3jo0nFZFdNbhaKAMuwsuS3p37iKvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28745391f.mp4?token=ftVH9lmfyib7gtYmnxt14ofchq7QGrZGTmcHiNtZ3rwB8i9PIk-TeQPZQKzTO16CIQi1JmRa7tg08rCQ0-8pDW1igXv5jfaixVRopoxVescZoBjCaNgAZN85k-ZA0UAt4e47xq8rhyrYLi6lNXrN7xy0h3bGR_Kh9nDL5PaAUA-pPdRfb7EbSOSIFj0MyQhUtCqnQlpWkydvEuQUBufz2hTGlElSm9FoFcA8uN82-tsNaI_issC0443QTGjUd7vei2-1xgavu4B-PLzAE8yF8nrbzrlaQj9EmzUc49S1JvjJXl6582GFWf05G3jo0nFZFdNbhaKAMuwsuS3p37iKvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صحبت‌های حمید رسایی علیه مذاکرات نمایندگان جمهوری اسلامی با آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66047" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
ثابتی دیشب تو تجمعات بسیجیا: عراقچی خائنه و من طرح استیضاح رو به مجلس ارائه میدم
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66046" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vchcdRY-zXlAc8y0wKfULFOg6d_ZKynquzuTxEV7XZ9QoQg2MpLfetD17-ejbU2WQlHQQbQr3nV6zB1wopqu2qHLsxkneVSvdQuGXwIzWh3AJEPRE4UV2uSPO_ypX9sX99_ZTzmumMA3BybluIqCzUlU_rJEol2gM-7I6NW22l7lAFiBLjqmqzrILLb6f5T1YJTKwwruMxlRJ42GE_hekp0zRVdt2iB0rnXRP8othxAQSap1Yn05SxVIHTKAX1WsVIHsBvbnJyZZ4QFTJvJ8Ina8vbB4pjWuYq3WCb_oxG9PqiBUwrDlEIhzXwnuTKyaRnIKSnT2pZt7ni70Myl-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی والا مام خوبیم
بابامو کشتن
زنمو کشتن
بچمو کشتن
«ولی رفتم باهاشون توافق کردم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66045" target="_blank">📅 10:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66044">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375671acc0.mp4?token=PiH8-uqbeN8ZxzYxhOI32ut6leRP3o7aJT4SHZOXldH1SdQBogxxts72BZyRWtNMERWKTH7YlKatF-bLiEWwWiXvi_h5VoKR07GVRKWIxMovF4KnVj3ayARVNjMPFTqjFaI0RGWucY6LEtoiRAzf60BQiCX8ukFSr_yJ6RAoP29rsEUg5M52sqyjcgxrqiHJgP9jnBEpvRLIkA4UZNDwtJqnF4yVTYGov-WXvTVygjvTz1aLjGcVNzYZHB8u2mYL2AbOMo5XESTCxhW7IibbXvQkAWZFYMi3-ZhSfrfnRSsZxvxew9UENETdNIruiiJZQYVoYVMaVRPUUp20-N5PrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375671acc0.mp4?token=PiH8-uqbeN8ZxzYxhOI32ut6leRP3o7aJT4SHZOXldH1SdQBogxxts72BZyRWtNMERWKTH7YlKatF-bLiEWwWiXvi_h5VoKR07GVRKWIxMovF4KnVj3ayARVNjMPFTqjFaI0RGWucY6LEtoiRAzf60BQiCX8ukFSr_yJ6RAoP29rsEUg5M52sqyjcgxrqiHJgP9jnBEpvRLIkA4UZNDwtJqnF4yVTYGov-WXvTVygjvTz1aLjGcVNzYZHB8u2mYL2AbOMo5XESTCxhW7IibbXvQkAWZFYMi3-ZhSfrfnRSsZxvxew9UENETdNIruiiJZQYVoYVMaVRPUUp20-N5PrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ١ دقیقه رو گوش بدید
زنده یاد مانوک خدابخشیان میگه :
رژیم اگر توافق رو بپذیره به جاکشی می افته !
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66044" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66043">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWM6bgtrOu0fBYlb_IIra_KpBj6lsjE3WhJ1-HXgm2FBVRy096IpDve2LWagCUEgX6L37tHvVIewT5ofu-ZwVATb2LDt9a3KWjKQK27ctevs1jDb0ep3E4laaAva1GybBxBByInr1d57bEdNE74MorFZYJ5ipXh4V-CFDtvl3ghwy6YEnub4LJ8y5dFRDVlWv1ynRfQsOC92csHL3vVF8Jux7yz-VlLbmbRCwhd0qo8g2uodVbr3LLYQpoJsRlI1UHwaTNgTNqAW6D5EnfCQBLHVzH-Wdg6ZnHSgqnhxhmCStge5Kg8BiG2YnfBy5yOVJRnB1-iaas1UHKQtVRcqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66043" target="_blank">📅 09:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518512af42.mp4?token=CRNESOeaUWy87vXCc04DyBtyTqdVt_cgNBzm4PXEPLnvMl7Np0l3AnJJglfm_o_6EO4HWxqr5-nBg1BAKQpphEq2-j8H00SasnpCLjd9yczBXGyD9KF6x6_wTwMn05kr4dD2wTP47GFLgb72GJdAYABb8Xkvs1J6bLKMn1mMz7Dt3c_HUmAyeMseRhNmrx8f8jD_UTwHN7_PMUa2W83i59CYYvg4soKUqVtzYFV-sDVyBzflweVs0-5uGu5OYtb8jVifThThj7RYJJqz3wLpjO8Rho2yfv9IHTOCuIVRrACKKYaKbrCkXupezxcVSFFDOxXI6SYEWh56iijLRyybNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518512af42.mp4?token=CRNESOeaUWy87vXCc04DyBtyTqdVt_cgNBzm4PXEPLnvMl7Np0l3AnJJglfm_o_6EO4HWxqr5-nBg1BAKQpphEq2-j8H00SasnpCLjd9yczBXGyD9KF6x6_wTwMn05kr4dD2wTP47GFLgb72GJdAYABb8Xkvs1J6bLKMn1mMz7Dt3c_HUmAyeMseRhNmrx8f8jD_UTwHN7_PMUa2W83i59CYYvg4soKUqVtzYFV-sDVyBzflweVs0-5uGu5OYtb8jVifThThj7RYJJqz3wLpjO8Rho2yfv9IHTOCuIVRrACKKYaKbrCkXupezxcVSFFDOxXI6SYEWh56iijLRyybNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه آخوند آوردن صداوسیما داره میگه به پیر به پیغمبر اماما همشون با دشمناشون صلح کردن شما هم شل کنید دیگه.
«
واقعا بی شرف تر از آخوند هیچ جای دنیا پیدا نمیشه»
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66042" target="_blank">📅 09:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkVIXh-7MqBoe2lSTmgrLcJbKpzFndHp5JIkz3yezQrPpi_VRMv8Rl3tUbq5jxjR-0oJTFM-MpNOcFkUE-qzLyP6MPA7uSB2zz0LC5gNIS_5Or8woLE5ENPwSPXEQNE0NT3br8LNDeP6sZWVqH3ytLsZTnkRsADG8ektcxGR0MSsPpUu3ToO-Blh7xNd-0vXF8Mr3tZ_Lb0CIPkOsYYiBhoVx7Ecq2WRS9aLY4dZTgVq1Q-S1OW9u0cA-9OEchkzMS5KCYnR-mzMyV7hW8uZBZFWDFTER23aZtVN-VZEs04nIaOMOp2MInDcAmSSDWwHqlRptMLxIPaxGc7XGA0Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBSojXyyvjQrs5HUKKZKRWDbMHXz8wpCi9xVwyqY56c6MrCBwEgzFIYvUJggmAUDIsN0dDwSvSijV5w9xDd0alYLzc0QKBKyPektQxifntGVZE7JYh0qXe61GO2CWHFLUxeSjNpxkq6MTgkhSAv_hYbpXnVP1nPpSOcxycYOt8CM09vEG_Y55XtU0sxG8OZhHiEl4RrInJavAHHL4E-Gw2zRqgGtlGEutuGD0Q3qatgZZMxbQ8FPJQWMfskIdYnRLVP-39Stxqx6vbT_W2hFs7ByZBwbsIkkIOjM5p7mYzjTVDek31smBgEc4Mo02WRQEjZFHuTHEtBMDGr5aEFvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66038">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
شعارهای معترضین به مذاکرات با آمریکا
اگر چیزی امضا شه، مسعود باید کشته شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66038" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66037">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
⭕️
شعارهایی که در تجمعات امشب حامیان حکومت سر داده شد:
۱_ تا باقر کفن نشود، این وطن وطن نشود.
۲_ مرگ بر سه لاشی، قالی مسعود عراقچی.
۳_ این توافق خونیه، باقر خودش کونیه.
۴_ خایه بخور با سینی، عباس بچه قینی.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/66037" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66036">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEF0rYhniRnh5j_duF7GMDZub4eDV28z6tsfS8t2K5E3JTaVJp81v-JVjnVz0hcsfurC59c0a3VwczDoQuy7NV_qITOUTTGB4xKtiLVw_e4PyKj7ce9Sddjy2LULuTWeFvlf_o3hSXxCOwqqkjXY_tojvyIAkNhDvUAkiPWOAMl7Vt04g9F49BVeoKIS_axGxSWpRruukEqGNKCyZpiuyZM3JeBaAn7rw3UXYLVf28YpferqpbGX0rS-BsTkk16wDnCTN7dmN7o81Xx4j6oekUMc0Ji6mWH8MgG11QFhDpwJtjDQBv2Eck2jB8O19FgoILxkg-4mHuCACNDAvsi94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ و پیت هگست در موکب هیئت محبان امام صادق (ع) کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66036" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66035">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaR1zTC0D3suLUWEO7PPV4AwWxAbok-a15e6_r4Wy5JgHxH2Y7VhzX-FwziEdh3yhu4ARftgpoMF6hDjLlTIDIb3_uWmfUGsub3r17VBNyhm5fIVPl8xTaUKT0KxlqPdMdojLvgTWJnd0z19WhgfHyvuNWhZQRLIgw-PG9toJH0GDlxBNBI3RcpDyZLm21iUFXk8scsZ_EG5pMYubXZvuclkdU__DZmwDxgC9C7tZm7Xzrvb6JSsValVFcAlW1mszfMwtZNrbAbWYfqY-zyD7IEVgtF-bJI8E2whlob34ZUHKCQnwekTGB0xHFBsQUjlu05H6JoLHzeNZlMIrjF9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
توهین و کنایه بسیجی‌ها به آقا مژتبی
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/66035" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66034">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
نبویان :
امریکا اومده به اینا گفته 300 میلیارد دلار بودجه بازسازی مملکت رو از عربستان و امارات میگیریم تامین میکنیم که خب مشخصه نمیده
اگه آمریکا بعداً بگه ما از عربستان خواستیم پول بده ولی نداد، شما می‌خواید چیکار کنید؟
«وقتی توی متن نوشته شده هزینه‌ها باید با توافق دو طرف انجام بشه، یعنی آمریکا هم باید درباره محل خرج شدن پول نظر بده. حالا اگه آمریکا بگه این پول نباید فلان جا خرج بشه چون ممکنه به دست سپاه برسه، اون وقت می‌خواید چیکار کنید؟
من بهتون قول میدم نه پولی واقعاً وارد کشور میشه و نه اختیار کامل دارید که خودتون تصمیم بگیرید این پول‌ها کجا خرج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66034" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66033">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKnBCzDhmWQM5cQPmC6eUdqjmLPu918y6oO1iTQDu8Ow9DsxDBOEiiOiRes9xxqQnOFxKGLql-YhxN5I4UtKrt6_093pwOqXWEe7Rn2lz6Waz1mIQfw7ZLoOgXcfEIEqYlSHcQtKyuhWV19fivjiWe9Cb7GQ--ObwXUREGlIzSAhDKv-5kfM-KvmJZOugULvyas6tz6bnPwyc0bu8Q-GTrY96nJ84CPI-9mV1ju-1BCnPr-AF4D07GxGbXeq3OgDV12lWcMaMe0Qaf73FwiEjfP75ncXZkNBF2onioiesAxWCUpHlsgpz0onpX2KjzOQPB3z5-rL4gHkDiUIXdkrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز دفنت نکردن فردا هم قراره با قاتلانت توافق نامه رو امضا کنن
😂
...
«چقد تو مظلومی»
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66033" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66032">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:  طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است. نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66032" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66031">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077634d539.mp4?token=N0wTELg2bu16teNwxuZ-gpfoPkluYvwUwGpNvzAUPBQZJ0SRMw3f5sHnFK6dV-f46Rt4AHr9rYCBdPBTBgkk6wk1G1MORw_uzOVRqRuF2fDMxvpaK1FZ_Hhki1hEUE6LcKt0k6R5dudgecPi93ddNhhzGneG_F1ohQi7pTfB0iCSHVAdaimAq9jOtd2oW_7CDVeD8IgBqmLSV2pcOos6ZyfFPJ3HJiLk8MFXpVTOQ_3A_G6y0pEzM0CkubBYH1inuMNBEwlCfni7Z8pWhVmKa4CA9S26rD6lZ4CHN6Kq7rT-C3TabLPQicTZqgI0EhbuxpKBNSyn2qi_6JLfOhX7lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077634d539.mp4?token=N0wTELg2bu16teNwxuZ-gpfoPkluYvwUwGpNvzAUPBQZJ0SRMw3f5sHnFK6dV-f46Rt4AHr9rYCBdPBTBgkk6wk1G1MORw_uzOVRqRuF2fDMxvpaK1FZ_Hhki1hEUE6LcKt0k6R5dudgecPi93ddNhhzGneG_F1ohQi7pTfB0iCSHVAdaimAq9jOtd2oW_7CDVeD8IgBqmLSV2pcOos6ZyfFPJ3HJiLk8MFXpVTOQ_3A_G6y0pEzM0CkubBYH1inuMNBEwlCfni7Z8pWhVmKa4CA9S26rD6lZ4CHN6Kq7rT-C3TabLPQicTZqgI0EhbuxpKBNSyn2qi_6JLfOhX7lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرفداران رژیم دارن شعار مرگ بر سازشگر رو سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66031" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66030">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=vAoP5Te_UidunWIJe5wkFMp7YT8zadD2eJHxBWCknv7-yGfGk2hyH3P59Swt3THk8G_nJhX3VJNOiOI22sQcHbf80rP1bw-fhru5sshqlyDtY0t2H0C-bv0BrbPSGoaM_JYwP2vrXfQesQNA7XlNgDGpu3JCYfeWeKmWOR2YKIYzuMENMX3C9QNYnmfWSvIJrSRD5TKqy2QEof_LiKNo99BjNGVMCXr59OteXYVxXherZq4nanN8JATch3pxMx-9OX5UlZs0lVHUS2J-2VG9OCKzPv4WAP4NtGbm1SOPG-3zPW_1Rv-7SqEnDRgjFgzrVACfGRHq3A5Tbg9PawTMy34lJPrOSV0KRGMs9kp9OxBgD2CAJvBBwDruPlA13f0OCCBAy-_xbOLG1XJIaICttefpvTJEBqzt8ytktAnMufacleOsrmantEPN0kt86BzaZkaW1BFv5xXGf-ggA9Cm9nNf6Gm32nnsoqJvPrF_3pDxY631r8oAcMr0wJKgHBN_X8wpJbmo1vn1xok5uXpoy8As0Z1rThpLD_HKfiTjHb1HcCtBiUO_Ou4fC3QuYvBvqSwf_oo8U3aNU744H-dQR5PTFnZMdpXBNStWvQhO8DITszHuMdBPOVnRfJ0y8sXptFG7JjDXI-GiCK_ffd7VUICAZJhOXxQibfJTBrasv-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=vAoP5Te_UidunWIJe5wkFMp7YT8zadD2eJHxBWCknv7-yGfGk2hyH3P59Swt3THk8G_nJhX3VJNOiOI22sQcHbf80rP1bw-fhru5sshqlyDtY0t2H0C-bv0BrbPSGoaM_JYwP2vrXfQesQNA7XlNgDGpu3JCYfeWeKmWOR2YKIYzuMENMX3C9QNYnmfWSvIJrSRD5TKqy2QEof_LiKNo99BjNGVMCXr59OteXYVxXherZq4nanN8JATch3pxMx-9OX5UlZs0lVHUS2J-2VG9OCKzPv4WAP4NtGbm1SOPG-3zPW_1Rv-7SqEnDRgjFgzrVACfGRHq3A5Tbg9PawTMy34lJPrOSV0KRGMs9kp9OxBgD2CAJvBBwDruPlA13f0OCCBAy-_xbOLG1XJIaICttefpvTJEBqzt8ytktAnMufacleOsrmantEPN0kt86BzaZkaW1BFv5xXGf-ggA9Cm9nNf6Gm32nnsoqJvPrF_3pDxY631r8oAcMr0wJKgHBN_X8wpJbmo1vn1xok5uXpoy8As0Z1rThpLD_HKfiTjHb1HcCtBiUO_Ou4fC3QuYvBvqSwf_oo8U3aNU744H-dQR5PTFnZMdpXBNStWvQhO8DITszHuMdBPOVnRfJ0y8sXptFG7JjDXI-GiCK_ffd7VUICAZJhOXxQibfJTBrasv-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
نبویان: من خیلی ناراحتم این چیزی نبود که آقا گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66030" target="_blank">📅 22:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66029">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=gfk2YZLNMAnV7FUPOT-dtZhGsC-zg2xwv-BAAKoLvWC0Umz2qxctCvGlW1TpEtPk1BO_6F1Q3kfRD1kEwYHMrWXf-UKlVeA6Tl4vXGChjHg0pl6TD08dvSyvTM-7lM4FbB8QbVFru6OMObovLLDDsoc79m_ISfFL5U9rjnEWQeLwOjUOi6-2D8_Jq2hsNtcOwXlrN4ZqzMX6aUJ2jw3OV-P5Ip2Mq2qukxi0G2kkXHof7--A1J6HFayIM3A0cWbb_joI4YOZM9reA0bPSqYaMCCkHzMMid8w9k3eYSG73wENkz32Op_j-HwlhBJF6kzJQ1eAA9w08zpoNNW5DfMXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=gfk2YZLNMAnV7FUPOT-dtZhGsC-zg2xwv-BAAKoLvWC0Umz2qxctCvGlW1TpEtPk1BO_6F1Q3kfRD1kEwYHMrWXf-UKlVeA6Tl4vXGChjHg0pl6TD08dvSyvTM-7lM4FbB8QbVFru6OMObovLLDDsoc79m_ISfFL5U9rjnEWQeLwOjUOi6-2D8_Jq2hsNtcOwXlrN4ZqzMX6aUJ2jw3OV-P5Ip2Mq2qukxi0G2kkXHof7--A1J6HFayIM3A0cWbb_joI4YOZM9reA0bPSqYaMCCkHzMMid8w9k3eYSG73wENkz32Op_j-HwlhBJF6kzJQ1eAA9w08zpoNNW5DfMXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشایی تنگه‌ی هرمز که قبل جنگ باز بود الان شده‌ی آرزوی ترامپ، آدم می‌مونه چی بگه، دهن تحلیلگری که بگه آخوند تسلیم شد رو باید گِل گرفت، می‌دونیم که این تفاهمه و توافق نیست و توافق اصلی در طی دو ماه آینده مورد بحث قرار می گیره ولی همین تفاهم هم فقط و فقط به بقای جمهوری اسلامی کمک می‌کنه نه تضعیفش دقیقا به مانند برجام.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66029" target="_blank">📅 22:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66028">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGWnkXB-Mr5EYx7heQhzY0cnmW62VcR4RAvBdFBnVDvvLWJ3uDMdocfQypMDfHiX_sHTz_Fsoz7PhAgP77KUGrYiM8664URTUaYWsZPq8aX0j4HfI_WiFq7machV5Gp5No386DHqjHQlDMGwFereXoXWr9eUbYMkwQN7HMemetTLnaEHFW9szUjHhWlHd3Z8Y8AO3TrLQWg58aYBPBmwzdJh6ncxZ9Dlv6kJBcLEZtrlWRPIkSZcRc1C9AIyxAtEPqfKrJKVhIyxXdeDLCW6HJFNpSh0V_aD7w8hsSdvQwjobnZ7FVXVdMhjt9i6t-1OwpIlclOmk-hDuh8Sfdac6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان اعتراضی نمایندگان مجلس علیه مذاکرات و توافق
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66028" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66027">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
رادان: هر فردی که در تجمعات شبانه برعلیه تصمیمات حکومت حرفی بزند یا شعاری دهد به عنوان تفرقه افکن با او برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66027" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66026">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=eTbtGUo2z7iBsvBgfA_pn2E1kUiuI1Nre_YTOJqopsun42UuoKMppXopCjfzduYVnx8u3D-czruiDucJ_y8KCGXjFJL2BaupXn7-sXSte-LpEmwukzgeobOA25MmBGArQkZ_pznE3gqJ1f2BbM1WqcAvcRVOTj0FeupAojY9U2lNQdT1rgKm4tlJw3oFh9VyGosS4Kg_XX8ACKdSirYYvgKw2xZpojeHdTysOoxi_2Kn4eod1uoJ6KEsuWmoBSpB5E-8CR1emtd5I7J2krha7IqJhjYZqUxD0djaiEHBV1E_1VWEcTs6Fym8xCc0bxX-CwhBdRO51dN-Y5d3OXtxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=eTbtGUo2z7iBsvBgfA_pn2E1kUiuI1Nre_YTOJqopsun42UuoKMppXopCjfzduYVnx8u3D-czruiDucJ_y8KCGXjFJL2BaupXn7-sXSte-LpEmwukzgeobOA25MmBGArQkZ_pznE3gqJ1f2BbM1WqcAvcRVOTj0FeupAojY9U2lNQdT1rgKm4tlJw3oFh9VyGosS4Kg_XX8ACKdSirYYvgKw2xZpojeHdTysOoxi_2Kn4eod1uoJ6KEsuWmoBSpB5E-8CR1emtd5I7J2krha7IqJhjYZqUxD0djaiEHBV1E_1VWEcTs6Fym8xCc0bxX-CwhBdRO51dN-Y5d3OXtxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
در تجمعات شبانه:
عراقچی حیا کن
امریکارو رها کن
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66026" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66025">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
⭕️
🚬
🚬
فرهنگستان زبان فارسی: از این به بعد بجای کلمه هدفون باید بگید گوشینه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66025" target="_blank">📅 21:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66024">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSjdbppbmQvVzJ3FH910SI2ebYPPs3XYNvkY5Vg27cR1-_vAvLLfatf_Lwn-cTve20gUilAVz0jI_-9BL6AFetimU9WWKCaYxypgVMkmE0IxIeYtreORERyi7hA-8LmnHw_G4ETPxuJcRCXzjxUmTkpthrmDOlicJL-6Pcnka0u5z5XEgA9rgc9DiYcIS_RIjLy9EYBLBmKsN7Q4sAdjFC-c-25gEA-BABK4JFRf6YlNoWgaBTY8IqkVY7tlUGcHP5jR5N1XAN1PEk6BPQLt4qAEGB8BbXAfd7eobr3zMi9cUBaC301zZ0zDRqgZYVoYNiOhwiocCCkMbhaRJfiBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
⚠️
سردبیر مشرق: رهبری در کدام پیام ده شرط را اعلام کردند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66024" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=OhvctrxzCzcpLQZ8Tq3fTUfd42ZTvIVhVC4OCFRn0gR3USxg-q-scNSWEi2QXFkS-t3p53td48tVhk8kiCMftE0j1S8JCzsRGVMRca98gqKFhkdh4_6hmc_FY5DOdDFQhM8necNaUqUdOraHYfTom9Jqm9oUwFeuI6IxuDobGbu4KbalkxgKiPeEaK0A5mgAgOgz5bsABBEFT1mIa0y3qpGaq-MG3qTYXAE3rw_4UgSAbypRevkGUULIpdgeJcToy2ptwI_kiPvicDkaQRWURM5KYbrmu5wFUmdDu_y0dus9y0JSaKJFBlEHGEb6hGrtyi-TeA-jh3UqGxFkc1sZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=OhvctrxzCzcpLQZ8Tq3fTUfd42ZTvIVhVC4OCFRn0gR3USxg-q-scNSWEi2QXFkS-t3p53td48tVhk8kiCMftE0j1S8JCzsRGVMRca98gqKFhkdh4_6hmc_FY5DOdDFQhM8necNaUqUdOraHYfTom9Jqm9oUwFeuI6IxuDobGbu4KbalkxgKiPeEaK0A5mgAgOgz5bsABBEFT1mIa0y3qpGaq-MG3qTYXAE3rw_4UgSAbypRevkGUULIpdgeJcToy2ptwI_kiPvicDkaQRWURM5KYbrmu5wFUmdDu_y0dus9y0JSaKJFBlEHGEb6hGrtyi-TeA-jh3UqGxFkc1sZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربا با ماشینایی که تو ایران شده هرکدوم۱۵/۱۰میلیارد و شده حسرت برا مردم از این کارا میکنن واسه سرگرمی...
💔
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66021" target="_blank">📅 21:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66020" target="_blank">📅 20:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری؛ ترامپ: فردا توافق با ایران امضا می‌شود  توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد. توافق من با ایران دقیقاً برعکس…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66019" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl4ulxcCDskYWNkvu3tvSnD5LJ5MJziBCs6aSzveS3KYN5jfkSqpBT_7dN_klgxZY3wzfoB00ahLa_k03SkFoNzIE8zt5CuQ7H535GBe3JHbPtXVzDqSg8Vtn2Z4-Ka6GZ_jF78OShtUWsJ2QYVO3jQUKOGJTWhl0H889b59-sGHc3HbQClQ2RYx-w3zBr8WwKh5XMfQoAxS-Rwl93J99WchrPpt3xgwVTGfaLIDAsAVooVsei8GgP5LBwdsAwYwrG7_urFaR44gDm5LbTu5b5fizJb8vYOB9TaOYwAhUz9HcGRjafUz13FIZCVl_SspRsogdQp_nhCC_P4UICgx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: فردا توافق با ایران امضا می‌شود
توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد.
توافق من با ایران دقیقاً برعکس است، دیواری برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر سلاح هسته‌ای نمی‌خواهند و نخواهند داشت، چه از طریق خرید، توسعه یا هر نوع دیگری از تدارکات. قرار است این توافق فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز خواهد بود. رابطه ما با ایران بسیار متفاوت و بهتر از روابط دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداخت اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد. در زمان مناسب، وقتی همه چیز آرام است، ما به لطف بمب‌افکن‌های زیبای B-2 و خلبانان درخشان آنها، وارد عمل می‌شویم و گرد و غبار هسته‌ای را که در اعماق کوه‌های گرانیتی قدرتمند و غرق شده دفن شده است، جمع‌آوری و نابود می‌کنیم، چه در ایران و چه در ایالات متحده.  ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای طولانی هستیم. امیدواریم که این روند به سرعت، به راحتی و به راحتی پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مورد استفاده قرار نگیرد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66018" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=rddDP5RwB6mlsw7W1ciPMtdem0XJ6w7Pin0d03AB_QPXi_EIAaWuqRBUfxiklN4AH8Lv14zRHq806NgNicNfr1YkCcVh_JxmAjwv_Z6Y87hHVYEDXdJUxgVgLpABEhk2dIk_XFbsYc4FA1Vz7FjFkgMt8CJIC2t2inUGTqSLaAT9z7bk7mEqMx4QJ4_UQN-ESFmgMTWAWnomhpuS0RR5po_LkHcAllHz_q8_DqEOnCfjt-HDwTzzb5yATRJmz6EJ_TKR65zbWGDw4PzMPzvOw2dqtS_LrfzyVX-Sm_GVV6C7q5ckj8b_GVRgn4p-Zzk1rL_YY0glIawdK_dp38VShA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=rddDP5RwB6mlsw7W1ciPMtdem0XJ6w7Pin0d03AB_QPXi_EIAaWuqRBUfxiklN4AH8Lv14zRHq806NgNicNfr1YkCcVh_JxmAjwv_Z6Y87hHVYEDXdJUxgVgLpABEhk2dIk_XFbsYc4FA1Vz7FjFkgMt8CJIC2t2inUGTqSLaAT9z7bk7mEqMx4QJ4_UQN-ESFmgMTWAWnomhpuS0RR5po_LkHcAllHz_q8_DqEOnCfjt-HDwTzzb5yATRJmz6EJ_TKR65zbWGDw4PzMPzvOw2dqtS_LrfzyVX-Sm_GVV6C7q5ckj8b_GVRgn4p-Zzk1rL_YY0glIawdK_dp38VShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
تجمع هواداران جمهوری اسلامی مقابل وزارت امور خارجه: مرگ بر عراقچی بیشرف نفوذی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66017" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=uA7b8y00P17EiY8EMRRkdjut41WjlRIsPuvFV3cBSR3pULynWRon1YlY3FpfK-CNMjJDI-9hWnQe9L98tC5ivZbLXZlixbl57oqsh234FQM2gd9iXeuy4xXlxecxd8IoQkqvd7gibN9dSiiFku99pKCBX6PUVcAW27WV8Xs7q2s9f9l3FniOkRUaSmGjiBrlq9_p4M3u8peTVISOF6sYdg1DYPFn9_Uq6TneSpfh9BI0cnP-BDkqpbvknvnRXyOAH_GFwaVbVsaIpJnneCSFsXrfYGW1DZkSpEWwd84hTwcMFJO6fh3fPJp7JmyzNdPPDVB1APn2Ca9yiJzhdS3JbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=uA7b8y00P17EiY8EMRRkdjut41WjlRIsPuvFV3cBSR3pULynWRon1YlY3FpfK-CNMjJDI-9hWnQe9L98tC5ivZbLXZlixbl57oqsh234FQM2gd9iXeuy4xXlxecxd8IoQkqvd7gibN9dSiiFku99pKCBX6PUVcAW27WV8Xs7q2s9f9l3FniOkRUaSmGjiBrlq9_p4M3u8peTVISOF6sYdg1DYPFn9_Uq6TneSpfh9BI0cnP-BDkqpbvknvnRXyOAH_GFwaVbVsaIpJnneCSFsXrfYGW1DZkSpEWwd84hTwcMFJO6fh3fPJp7JmyzNdPPDVB1APn2Ca9yiJzhdS3JbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی وایرال شده از کیوماسا، گوریل باغ‌وحش ژاپن بعد از دعوا با دوس‌دخترش
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66014" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcO9U_C1n232NM1FpdaWura_sSsfF0qNSZkDsovTqZJOh6oZCL6jn0nQJPCRk6yDIyuvRC87CazF_9amq74fZ23-PvTxL6fsZLJH2d5tUyJLIh6-DK5m2RKm8AiIaK1Ab_wX5fhn4-OcwhyrYxRZtSKqjQ-4n9Rll1QA8bn6zIQYL1lM3bSbH12IDmjAaGYPQsTz_H1gJm7XfjeNUFV_dT4TFTyMWBv_0SCaQ6FTkhpmhJrqDwWfkBR9zkQBIf5dOb_Q5QFOSR0h5eTw1e-UPDirvmYcUHmmUM7cvq6si8ULR8iRhCu9gl6B0MEvjDw-MTwo-Lg7iF9q-c-EwyNBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید به نقل از یک مقام آمریکایی:
پرزیدنت ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت، دیدارهای دوجانبه جداگانه‌ای با رهبران قطر، امارات و مصر خواهد داشت. نتانیاهو در این نشست شرکت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66013" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m48fsGxmO2-JxqdzLzx8jLSuk_JDJAEd-cT-E5g487VnIqb9gY20akp9D8T4jAAA7B4ASGwNq3PRiabW4cjyizYmx_-BU7mbt-heG38wX2Ytz5jkfOe3847ZmJ0ANZpNcCBWbmlL5Gczok_juxEftRRseJYCpdCe-NEHH9qoS844qznfe7YQOyf_6_jDn6Lp539TlLP5eNnpbo9X1jpRUu6o78S9QuqUO05hJC6PFoVFYHtt3K-JPt9Uy6okP7q5alJONgZxQF5f1yrXmOFP2vs0g5ZPtK_sp9q2cWrhlPd3U4doah4UIlNsZtbB1l_N0SQR_0U5Y0d4xji8SzlMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تجمع اعتراضی مردم تبریز به دلیل توافق با قاتل خامنه ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66012" target="_blank">📅 18:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
#فوری
؛پاکستان:
توافق آمریکا و ایران فردا بصورت الکترونیکی امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66011" target="_blank">📅 18:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9kUykFcpkJuGXYvl24P9tRojG_o-nqOwivPVdILuI0s0QkpZLFi2trug1lAq2LBivmIws_66ufi9zbgPLO7zunyfISjHGTzi4cr4VOmdLXWBe4zgH-kONhyidcs4ai8x06hu423rGgkSR6fgTD6JlS_if4XlPmfkYxFriiC3Sp49HRkzkRVsBeDoSQWQ0SG-AdNPwiNb1weVFaki07lmHMWFaFkF_3VE3Xd8eq3aazBPZRjClFF91R59MA4SgT-_8UhZxdV8kOx0DJr2b7JyhmwYPNf704QRtdMr9BY-Ux1o5JQmuXkloKKomRfhGICyPb50BnNIP_ElOZ_PIT23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlYO7ifUjBZNqs-9ZUjKPRiP9oAZAnLkUpxeLIXrvc62ivwRJWT6EzMQ4WYmmsuSKQdvilg3oZgy1rIXWEMYffwuFBGb9XLoUiYOST36Ty5UbbltlK2RxTl5HM_5mmSHyZEBvetV3cJJQyS5HgajzAXDF8VDZs2mkxoKtjN_Rb24oHzv834exvt1UOEnvU-UN9vAW08rLRJrlFU5yvz9bRFOIao4TFVAYHiJ8eXgVPd14mP9RqEO2dstBh1Go65qUsK5ofY3GYJRGzTghBM-hdysMRp5RxVU3CLj3Op-uLqiiIBlPDIWWeDdtp-agtrVWe7y2h5ZwYVAdGBkBkDGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgVatG9vJwtWABdilxqT8QPT8Dl9scdyTk8qRSM6l3fYz_YeNotgueJS-dhV2C6fsjqosBANwS1PPYEBmHRgghk1zUL7N_RcsQLI33I5D7vgUDoGtqP-Xs0WSIXI2ujdM4XCKmcz3RcUpKJSKfwotvrw7tDfjQXZPBH5HLA2jMhPZ7Y5Uj4y1xCWI6gvfFargDJ1AqtoDyptrfEmxmvmkReGM2V1uHKAvuKOP0BO5E1dCv80S9jOf1yVRKs4_5E5GmK5J7rub-cZuQOIyQeJYHSl3gDBr_YOq9NUv_8iNsC8unHFwON6ClbVV9IsZbk8H8IAVlN_ydCiCox6lSII_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4xV_6rCUlfiL_ED_J2PgPOqjjEk9V792de9LUG6a-Gb9razmZPpWqqt5GNCmapmJDoKeQ3XS0ihG5Aa9875dqT_3V-wrWmDQkbHBYknxstN_R4GQ_GdsJUSZy5GQenibDQqjKRFft1cVXl0mXLcNCiQmwBJV-0poXIDHi8LcWmeI4ny8J5UwAvC0TYF5X2-AZCSQH-TPcCdebZOhgMqGjsXYBLkjKVgn5fX8HFN9IsPgIL_SuOu0tAErpTN_DlNttkwzPc7RC7Gq2RcVr7etso7kMi5UjbnMKu429JgjP5ZG8gZMhkICKBEPjmXG0NbQlyZIGmFaKB7kmqI3alC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsCBfSK0cNn3GQPjKxgzo4c57lPh1YOR7zyPBpdkVNTcjwv716nseRAoj2joUpqyj-Wx5eL3COjZ3rEAiZXuMl-8uySnvKYGknIhUIPaqDvXAIdV7cX7dOj19nQaguvG9xMta9zMwVnur5_YWDLUCSjlBB10umc18v8Brp2JJGnP9PIrNNSry5nsBX1nvQy6kv4uPrIIHHFjLmgBPFMgLSNpM2g4FO7_R_kG5o4OJQaN_9vwgSk9N6ZAMR3W_AJNqYxSlRqhSFbkGAg6jKBiMYIoPihx7VDHlsb08n2vbb6iMF-cmn-mEBvoRFKBVHVY4ZEjtoP42dG2LNv_y1DrPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxr013b-llC-mVTs-6R4UWMzcBWIx69YXymoVXB17oL-qcjGrohiXs_XEARv8Jd9NTXDLBnHXG5LqNom5d2E6MBec4y7cUlUajKuKKIMqZtRyBOE52RwSm277G9MOKZiRB0_bNXe3OCV38pKtRMsp2-CKGZ14oldiMlBC3_aiYE-DnN94HX4CPOlX5eUGeD5aAo7GiE02QIsxOZhiBa-5mruv55xoXL0KlO2GT1OCSzX77p_Jw8DNQf-ZvdBo2IpebIOM8mTNVfLuDkoL2NG1v73DLxaquwuK0-sD4pvJJrpSKMehOmWoqjkDgDRWzqwNMmrbXyyI94LnZkth1sfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6ym0RhqJ7LokaQd5TiDHqnqWvTYdbxV63xFR_6olj8e_n9o7_g8KmGcYDPnVQArP7GuEfAHq9yM0n52BzIG-A0i8lH4U_q2VhyNlelmymyW6kB1puZU9Aude6gdthsOA8y30wNgxGv-gdbnu4RyiAVkcmPyPZaSA66ge_-J9RNGOsXutFg20znaYCexqUfAGORlS8lJWI4xXyngEb2ARtSArevU3Da0ZROVsdE665BeGpR1lIsYWnoB7qVNFLxEDHadu2BLRML8hWQ8sXP2ioXZ-XH69zMELUJDFG2r3nqnAlSd64sZYoLpvnO6qJtonmaIV9drTxTS9bygj93eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=CiCwfBPTjDd8i028Mrsu68N3PH-TYwvG-UWyc2T1oo91mo9boiYOnlu-ng6GA0-MEjMJuYtvd_hPbOWc6mxnMpU_KQkhEJ5ofAvrFjoYjjIeeNpIw8d85i_D7-iYApOs5nDDgcsFnnrd0nmN5wLMpzhHUyvjOPsjt3DsSJf7JoQd_nQjKKUaGsfse8xUzt_Qo5MbHNsy_sRvw0b_rt_BKcks-mMGqWadCDz73oaHw8_a8z3YdroKllDS7MXOoZrg0k5TSi2opDpM-PQBcpptjbg_4swLv5dC91GKf7R6zSYHALQG1CcZ1uF9nVIP4FBx6HhupK6lytfcHNmN6Orq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=CiCwfBPTjDd8i028Mrsu68N3PH-TYwvG-UWyc2T1oo91mo9boiYOnlu-ng6GA0-MEjMJuYtvd_hPbOWc6mxnMpU_KQkhEJ5ofAvrFjoYjjIeeNpIw8d85i_D7-iYApOs5nDDgcsFnnrd0nmN5wLMpzhHUyvjOPsjt3DsSJf7JoQd_nQjKKUaGsfse8xUzt_Qo5MbHNsy_sRvw0b_rt_BKcks-mMGqWadCDz73oaHw8_a8z3YdroKllDS7MXOoZrg0k5TSi2opDpM-PQBcpptjbg_4swLv5dC91GKf7R6zSYHALQG1CcZ1uF9nVIP4FBx6HhupK6lytfcHNmN6Orq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-87NTbezQ5VLq7hZoLLymw1z-DGJJHnIq2TDeYQAIhv2HV_1Kxn3HyiVca5wGGf_zetNQJz7dBFnVxtvmdZcD3RbPg3k9b2FelVWY5Jr55k1dN14vPJ0iJ2sVdMliE8J6M71HVzkupqXy-R0lLiGToK8mwCFPnM7ZyFbLkAgUBtoJ5s2e72bKpwkcMPB21acBVHQAJOjdcc7OycRh3cj61BW_JWcqU9He5x6uti_gOPDnYMQ7faQ_L-U-Gv7HJUqxo-Mu-iyRBpmt0le57PFDlkzCGDpUCKEnez7RM2C9LxXKxcGqOFmUnUOPUlO2NmZ17nZsEVX93I8Nmo1shWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65995">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
؛نخست وزیر پاکستان:
ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65995" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65994">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شهر عجیبیه! تریسام بروبچ دهه نودی  @sammfoott</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65994" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
⭕️
مراسم خاکسپاری علی‌خامنه‌ای روز ۱۸ تیرماه در مشهد برگزار خواهد شد. از روزهای ۱۳ تا ۱۷ تیر هم مراسم‌هایی برای رهبر دوم جمهوری اسلامی در تهران و قم برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65993" target="_blank">📅 14:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
از امروز صبح خدمات الکترونیکی برخی بانک های کشور از جمله ،تجارت،ملی،صادرات و توسعه صادرات با اختلال مواجه شده است.
خبرگزاری فارس اعلام کرد برخی منابع از احتمال وقوع حمله سایبری خبر داده اند اماهنوز منابع رسمی این موضوع را تایید یا رد نکرده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65992" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65989">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNbZ90_DeqWU9Ng57IIYoX47hBLE0lS5FDbidMz1JGwe603flHTNqEaCjXNW8ktb3sb5uj8zE0EAR_9HQdWhF4EbVMP72RKlpLEU62JiUeFmVJ0i_Qy7xc9ZRxx1VKEo0Y65F_HS-7MrWF5G6WKYFhtdc5ZPtWOb-_02pd1c2zBq1ENZXrxDN_NlHAAQjUnIS1yKltGUGC7dDI2RI1fqN9izwtrDk72sNDbrKyyg6t7ElO5nb3T4wi4h4rQmRiLNMW0NWt1ykrb_6mH-GpYeYYbv8AHPA17U6fpU2HsfZD9KXhCw2RamVszBFTca0zWmtm77zesDeCJBAZP5S1rUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جنوب لبنان؛ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه یا حسین نصب کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65989" target="_blank">📅 13:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65988">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roLSi9dOCUKCjQLslG8LTj35FbHOlWCjY7VJGUIvxObcrWAChyqLdR9LhV_mN4IbPIbYZS0pkVUZHLZdZ7Rfw0rGQH7_tND4KqqVGdV3YUO3QysbTSBfB3WSsoP2h_oH4FxwY8jlbUNLRX3ZQOAaA0BNXouEFk13JFXN-s63HmpWLsZTty1txqI5h1sNtWPRjeQN3MKNOt7IuiQkzRTj4vg9w6PEt3p_iGm7dqsxyxmslA3BEkHstWf7qDlXLlmYPTW2pVsst_frXwc00WaLBtRr8FUWW4_NUy_ZSwzyxcAajW0pYBISamXrH_SPiFk1VLOSZ8lZlbP-8FuZZDEmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران تو هفته‌های اخیر حسابی دسترسی به انبارهای اورانیوم غنی‌شده رو سخت‌تر کرده
- طبق گفته چند منبع اطلاعاتی آمریکا؛
- ایران بعضی از تونل‌ها رو عمداً ریزش داده و ورودی‌هاشون رو با مواد منفجره مین‌گذاری کرده
به گفته این منابع؛
- الان رسیدن به این انبارها نسبت به یک ماه پیش خیلی سخت‌تر، خطرناک‌تر و زمان‌برتر شده -
CNN
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65988" target="_blank">📅 12:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65987">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=pLz_1jIEapgecMoFhrVHod5PdgJB20ii_UJxB1W2DwtvK8OgPWLz4MnjaANyny88hJ0qgJiLtKTIydWVaUJN6YDFR5tQQY8PU5MpD6FLx9dbUxxeWUTiFaLrxG1E6FdVlB7SOQRmS5vHo4SeIkgXTP1AeWEXoqFBOkkVrzdPIDosdlEPE3lj3Z_X-muqjRLagshOuiG4wJjZLx9DIM5ZB0NDSyGVZpStW6HwFfxz2la6fTiuO441KUfynwNzDZONWo4P04F8SLOh6fazquO-gUggl4OGh1XQplvQiteuBf6c_WEXxtb6MTIWuqNwdW9h9G-M4KQyHX9enGSsSXoojQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=pLz_1jIEapgecMoFhrVHod5PdgJB20ii_UJxB1W2DwtvK8OgPWLz4MnjaANyny88hJ0qgJiLtKTIydWVaUJN6YDFR5tQQY8PU5MpD6FLx9dbUxxeWUTiFaLrxG1E6FdVlB7SOQRmS5vHo4SeIkgXTP1AeWEXoqFBOkkVrzdPIDosdlEPE3lj3Z_X-muqjRLagshOuiG4wJjZLx9DIM5ZB0NDSyGVZpStW6HwFfxz2la6fTiuO441KUfynwNzDZONWo4P04F8SLOh6fazquO-gUggl4OGh1XQplvQiteuBf6c_WEXxtb6MTIWuqNwdW9h9G-M4KQyHX9enGSsSXoojQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انفجار شدید تانکر حامل سوخت در مکزیک
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65987" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEqmUman0C9-hN4dcddfN798yVqfg6txXCZLPLQf9JeNRyJo98I4uwvaVDcXd3s4Nh9xuN3rqdSDa_YYG49DXAb7T1QZtsIcycilXzls8ICxNoADYe_Cj5Twco_WKChAt13JGUiz9seCkgOyzMv-R9JQ8cfSvhTaPc2fvLJ9lsAvk_DEVeDLYj5Aj7iNALqknyx9Cyq-2OBdvbDZSTqjdK2P95U9NBE13_EQZNjY1JWGV1nN7_LBg9SbaxW2SSjKiTW8_QfGgvbMHWfLQXlMwTimfczsJuA-xBJfMFOAtcv10THi2jBTkilLA8hhi9TQfADLPZuHAeY2wCT59CXb6R9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEqmUman0C9-hN4dcddfN798yVqfg6txXCZLPLQf9JeNRyJo98I4uwvaVDcXd3s4Nh9xuN3rqdSDa_YYG49DXAb7T1QZtsIcycilXzls8ICxNoADYe_Cj5Twco_WKChAt13JGUiz9seCkgOyzMv-R9JQ8cfSvhTaPc2fvLJ9lsAvk_DEVeDLYj5Aj7iNALqknyx9Cyq-2OBdvbDZSTqjdK2P95U9NBE13_EQZNjY1JWGV1nN7_LBg9SbaxW2SSjKiTW8_QfGgvbMHWfLQXlMwTimfczsJuA-xBJfMFOAtcv10THi2jBTkilLA8hhi9TQfADLPZuHAeY2wCT59CXb6R9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=CJFRfYkUu-K9BEVWRne-paovOD_eltnaV9wdaw5V7nyOs7xsGmctwV4ECQ8_C8ZGaQeb_cheiRBrCIX1vKtIA-hUObQnPcjucJQYnzQq83TFOgzV0fBbsn503oisltK4SNbg3aO31pO-j1oDiTUmL2Nj2YGWJxO8H565QPQk8wHxPGHzbVJPGdE9b0nQlTBSMOIkiPUufTyDCfJ2ag0yERYerPkhmsfg8TWmghC7hDTz4LyM47Qug6BJ8lLBnMNUF4A7hT9xzeHG_3AXAGPL_IVgCVvfFA3-FsCNBdULrQO5LxMnhHggidrOgjTpFhLT_VS1JMhhJfoSrPdtxkjrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=CJFRfYkUu-K9BEVWRne-paovOD_eltnaV9wdaw5V7nyOs7xsGmctwV4ECQ8_C8ZGaQeb_cheiRBrCIX1vKtIA-hUObQnPcjucJQYnzQq83TFOgzV0fBbsn503oisltK4SNbg3aO31pO-j1oDiTUmL2Nj2YGWJxO8H565QPQk8wHxPGHzbVJPGdE9b0nQlTBSMOIkiPUufTyDCfJ2ag0yERYerPkhmsfg8TWmghC7hDTz4LyM47Qug6BJ8lLBnMNUF4A7hT9xzeHG_3AXAGPL_IVgCVvfFA3-FsCNBdULrQO5LxMnhHggidrOgjTpFhLT_VS1JMhhJfoSrPdtxkjrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=V6rJevDD64JbV0lGqJ0E3B3ntDLKXFscFN18W2H3G0MV2Iuo0vZnSEcHHWwpVVoNgC29dt6gMQSmQF8EjP5pbgHtbFT4zvIuPjGBKr54KBD_bBz_7KoVCPpA9iMZRPMmyZv5ALEfwatPaSQJSKsGhs4y9X6ofCLxPhExcJeP8L372OcZzBhiy-Cf6yFctdo8G3nDBYnoAfNNJFtqngY9I9XhCRurF-vLF9T-zr11IF-Rin3kzoVPAFxLqGPpRpveqgdy3sIq0ME5XwDQmLbXCxszJhz_EGEHqJhgHJXQmEJsihgelSF07aAJolwVgjIDutkcI5Z7HhVmmAdcG3saSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=V6rJevDD64JbV0lGqJ0E3B3ntDLKXFscFN18W2H3G0MV2Iuo0vZnSEcHHWwpVVoNgC29dt6gMQSmQF8EjP5pbgHtbFT4zvIuPjGBKr54KBD_bBz_7KoVCPpA9iMZRPMmyZv5ALEfwatPaSQJSKsGhs4y9X6ofCLxPhExcJeP8L372OcZzBhiy-Cf6yFctdo8G3nDBYnoAfNNJFtqngY9I9XhCRurF-vLF9T-zr11IF-Rin3kzoVPAFxLqGPpRpveqgdy3sIq0ME5XwDQmLbXCxszJhz_EGEHqJhgHJXQmEJsihgelSF07aAJolwVgjIDutkcI5Z7HhVmmAdcG3saSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=aVN-BwA2lGRASBDfMyzRCnFDemrKB_azWBJWgw8Gsg0mQZok2pTHRvEK_fqNa-8Zrw3atvseOclq_u5CdY8HB4lcjOH9u8HBIRu9-CpxHFC7khLoq-9ydCv5Fs5pqHlyAdX07DQEcK67vgVOi7Bs5Ra4yuH45cPV00xrBGz8mpyBxsRZF4PALWgpR0n-AnzGxfrAWd_L1YCOwU-SOWeV1mvmqHdR5rb7laPMXdj9JYugm8WO7fttux8KcpIq7BO6SdHhr7uyX1IYAZEI1CMinkmRrTUJD0uHqR215E-GyYIGMJPui1m-UO4jZcKzPrVtn0W3rnLNGXtS3eE6rffZiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=aVN-BwA2lGRASBDfMyzRCnFDemrKB_azWBJWgw8Gsg0mQZok2pTHRvEK_fqNa-8Zrw3atvseOclq_u5CdY8HB4lcjOH9u8HBIRu9-CpxHFC7khLoq-9ydCv5Fs5pqHlyAdX07DQEcK67vgVOi7Bs5Ra4yuH45cPV00xrBGz8mpyBxsRZF4PALWgpR0n-AnzGxfrAWd_L1YCOwU-SOWeV1mvmqHdR5rb7laPMXdj9JYugm8WO7fttux8KcpIq7BO6SdHhr7uyX1IYAZEI1CMinkmRrTUJD0uHqR215E-GyYIGMJPui1m-UO4jZcKzPrVtn0W3rnLNGXtS3eE6rffZiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRNl2VrtLHZXFAuuzcc0hMcsrYPab8hNO_wN0KSj7TYYcrAsvqq1PyrwgBuVeOjA_etnPC8G9tS7gtOELTln_7BuIYxHtKh1bvIiWARnryqpOfDFWS_C68vUyRxmMATeN7LfoFOBfwU3Bew4XGDnTPDJ9Ld_ag5Fd1nOf2BKa0q5Jaim3S22CHASdJ6zJ3f6D2lxRX1VPK4_u3xyVn8JxLbRahQ1GqT3pqon_Phr4ftaZskLnSzt0z6iulRiElIFCgQtxrNPz8y-rdZxU3_4FGBaN0c38D987F324aE8_PJVuw8nCL1SyCZ-SlR5dF8X-J-xXQcvkbaKBnLVs3P1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfdIZdhiBovIdGrjPbfNVX1psfBuQVQNXNrISPjGr9T1wLRfTVdqeVR-kHm9YDpjPI233bIuhUFESkgtUuMVxQIEwFxsAMmzLgBRTkkLO0CimQ4wXhMK-MIm7-hZK44JPmd8XhSj1JbYo50pK5ryaL6ILqFw7AUZrAhfmh-kIqlr6rL-lU_uw0H_5WAg5-Q0AUrIjDk1gpuqpXgolh_d32rvKE4hF3rXzYfjwEPfCFuRd-EAykTKSobZxnVvrsiZXAZxPjYwjwArLIE3qBaQa58jJFY2q5qIGj-mZIZXC4h2kouA560X3vuoOmzUW1xcHOsklLrfMpsvt821g32WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=E4ug3O1eeWeK9d77g6Hu_OTvCckUxBAyzUJFleaWCrLS5Ox87r2QsCB-1QvLpO-CsfDrYyp_v1hoXrUPdf-Ghhc0fIy9vGssIUYWISTXIZNy3opgLsYlBvUdtNNUDD9i7K8SLErJvflHtpnJA9Uy1-MMPqad6UChw8zDzksH88SReDIkdEu6cSLNcLxlKD19edmVq5URSAhxVdiIMqjaKS4gPzL7hGfnI01qUbf5botgqBC9F5-Xklhc1S4Z0KTq5hm10LhBRHzw4pb9h9CeuCb_9Mf42V2zMMKQqnYdeqTS4jHPdHC5K_rwe2mZyD6nJfT46QUndrJUaBykXPhFrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=E4ug3O1eeWeK9d77g6Hu_OTvCckUxBAyzUJFleaWCrLS5Ox87r2QsCB-1QvLpO-CsfDrYyp_v1hoXrUPdf-Ghhc0fIy9vGssIUYWISTXIZNy3opgLsYlBvUdtNNUDD9i7K8SLErJvflHtpnJA9Uy1-MMPqad6UChw8zDzksH88SReDIkdEu6cSLNcLxlKD19edmVq5URSAhxVdiIMqjaKS4gPzL7hGfnI01qUbf5botgqBC9F5-Xklhc1S4Z0KTq5hm10LhBRHzw4pb9h9CeuCb_9Mf42V2zMMKQqnYdeqTS4jHPdHC5K_rwe2mZyD6nJfT46QUndrJUaBykXPhFrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odfXtVM1cNtCGOEoHkh6FqM64SL2tMXs8qQqKREKs_m_8b4jLJZAHelcv7SaaEB_dOkEe-1aoojXGQyd0oJncp0Qb3YZlX28zSdo4KUjIGGufwyoHTBYERBdQOaOeWZs7KMyTYFvOTko9YYFkhhWSEHi0x2ax7VXPMTF9J1KqwhTWJ7p63gK3SsWJxYMjUqo_xVsYrOZ3KS4PrJRfNK-Vc6FjL0PmrWbL7QRUb9JcpTa9zZmXuKX4X7dPZMn5FgA7KjBHNyNAN0ssIU8hffBLrP9XBBhLlDYyJWZjnb3h48uoRUPH_y-pqx4sXdTBgDna66XrzLCs1HGXBGUqBkqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
