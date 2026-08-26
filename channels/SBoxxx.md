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
<img src="https://cdn4.telesco.pe/file/oM3OYesLYChUAW9yhB0NnUYbO_xUb7shassAGw-aDk6HFYg3suvijLAInyUKIh_zU6ndy7n1xO3FfBJYI4666xNsXzJ1yB_sMmdw9-p_NMzhmo_GrUSoy380j5PfEjibUAq8Gvws6yp9mNlTwLviKy1mA1KUrZF6pRR94kHdGuvuD_AIfCY1tJKhrcDIxwOmfZ4oFASLESVDKVxZVYkiDJjT_FtyASmrTflzhIdzr9U_SaXFmGo37qFv2LxBxodjw6w0IJb7yXSauqh8zCIXOCg4Wx_d4UHDLTkLxyO9ExJP2jx-fj7SIg4IMyRlT78jDVO7QIdFH1y_mhEcbcEr9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 03:22:42</div>
<hr>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=A9Lq0TSFztcQHnGBSvv-2L-7A7lKM50Wr9_AGlfceuboJSC9ioeikpuFuNRrkKp5Hwh0pJuo_bR9_JSXLz8YD3ylGHoHRJ-1FFtwnGKOM458r8SrWRlaozh3NZkbqcwWhjPsRo_xDT0bcBMzaFS_qvhdHccgCIjD1S4UclwK0EOlXq6t3wfsthhpu2LmTVALx-WlhoJlG8aUSK836pP6tbQJMcQkXlJt9DVSkuHBmR1Uiez_05xPvLnJWskYxouwXc7GVmKZXG2VU7Pul3dZADVX_a6ibZot_7hLowHs-FMxNur8MBhoJ9_7V4LpD9oi7vhthxaJXz1Yfl1aXz44LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=A9Lq0TSFztcQHnGBSvv-2L-7A7lKM50Wr9_AGlfceuboJSC9ioeikpuFuNRrkKp5Hwh0pJuo_bR9_JSXLz8YD3ylGHoHRJ-1FFtwnGKOM458r8SrWRlaozh3NZkbqcwWhjPsRo_xDT0bcBMzaFS_qvhdHccgCIjD1S4UclwK0EOlXq6t3wfsthhpu2LmTVALx-WlhoJlG8aUSK836pP6tbQJMcQkXlJt9DVSkuHBmR1Uiez_05xPvLnJWskYxouwXc7GVmKZXG2VU7Pul3dZADVX_a6ibZot_7hLowHs-FMxNur8MBhoJ9_7V4LpD9oi7vhthxaJXz1Yfl1aXz44LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgVp8oS6lo6s_Na4kwE6Ec9Vc1FET4u8DMRnHv2DORFEGQZwNSkCh7W5nEQII5W5wGsO06nHTsoTxbNaCgOKZ16EhOEgRpQdiLh0ba5f0WF6mwbNb6BulFbZZPwi23NGemUr_nvxkFmhyLcZxG9nqGbDsQvdUHi8cdaAAoz1BYXLzVInCFd3il9yfp3V77B57CQsV_24o4KTdDxdEY-UV1jy7ozfTZ9HVuNdIvjKhnNoOwZ8eWs5EmdsCoCHtDMpqAh5DSV1JUHzWM_isHJnzY8jnf7Jz38qsky-yPN4TCDMxal-lr2nuwc78OV2yrQvisBXFMvtfTxuKNpklBKHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXec92vnkhy3bhoxt3tmxs5ZAhYZYNL609O4dRrHarKwyLdxXdtYvihqK06xnJP1nemJ0L4PxQ8qlb_QCTOcg6WM3uCjQMtQbcitxbBQ0myCow29g0JhOLKXkJvSPv9mtfez5LksgcNV6B1c_GOoraR1SqFHrbzqIyXrXSGjPVVtR4VgpE01iLBak_ixVZl07Bmq53DmTPX2AA3IKRifkPlaiDBI70M4zzJP5APRW4t5-AawAnbx1a62KJ7nT-hRKZ1LONNrzexcZ4pgfRe-R90UR2vRoUHduD_unI9gIbec_XxFsB9yqNHZSlHpfxbE6OarnQHSMk8tJg8e4MTViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQLx8iSxwDe-pxoXIKF0oohRRPcakYlkuYPLDNrttmdlJRcJP6IjsRGNbIKcLoJY6tY5NsmU17i60RhH4h8tHd-LspdPCcdhCUezH-JzKLFT51sNh1TjdjCT5w8D542fl-y1PysUOVvU0kXfAv97J9V55D-IPBQf4m6G4M7JLJik8KWrrRLEhQUtyLWlbup4_OYvwXTXAE_tsbqhHODzElOmO50U9-UBCcVi-eZ4hpHh0uS2n4_wCcA7eSvj1mrM8qqddsEIY5XU6M6NZ-PHC82yraYKelx0PB0010lMJqvwjp-kVoqCJihADkojC2Cdhnmvd2KvTUFCtc9MSJoo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S83jB46GDI0Fo9gsuFkDF7sgMTBBfxrbMJSsM_VK9Kg9cQIs-Eq8XBKjtr-uXxoxi6Xq1JcBQnwKTG7QsoZ2klT-XYZDKm641CayvVeUaOlj65uyLZNFoH25DDrdvFAQK9U5_5llYtM3knyrd75qaQtb7GY1SCTUJgELYOsLAGFz7DD_hMQOfvPUw1Uu1dYzerUN3LRtigbgeI0bStzOAs-5qFoKLJhGDGk5Uj0GKytYbdxrxkAzN8wPsc3qh20CJymVh-6ZNT6nM80urO7vS2rVGeEcu2iP3H7reJYR0wW3cfUAJ2Fmgk2kxIC0-B5QqCVR5XW9ObJErWkfRKnjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qwy4MwPBj0CV0ArKtWoDVrqjrE04A_VZ8dVZO-VD-ZW2lFKTu6cjJJl9He-wcXezfWQmul37ITr5KUeyxEcHaFsFXEWwKPWeX257koIFpMhYK7U8cb_oBN_h5AB-3rIt6H4YzSODJVrHQg-80xnFBB8umW4k_kGFuitM4fhi-YVrg91H4Nx9gtzJnwP_mvUuJCNi_aHGUZ32mtS5lbUkYElQL6kYIRDd6n03dMVN85DFwU8atzLfKWVsMf5F5yHRkNROAQ9EEXfskRsYnVMnDb2Ne4fchTac9BjUoA32c7UPhkt-gUczz4Rc-yrjEL5rMxZBU9Zqkoo3z5u4cq61gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNS8Gsot92uRlwDDEmaaC-aBITySaIgoI18JowbZIIns49XomhBye2iYoxdRmfJOkWw871twQHWJ--s9QS_BkxKNi9jeTa3Ys8vmaF1IrPehlF0AZUSF_EFMED38W3WU4qx60dJsKicCZzdFSSOe79pb-UeZzZgKGH9Ve4dlb_FrbVqiQoJJK5pdwn-V7JgGZI52lN4RUesp_pVKCvq74tmifDzg2T5FInT982nJjr5nEWEKcnTeYIR_P_P5ZmleUbEHBCRGScg3uSMA_O5AFEadYfcPEJcYkMFmPuRFOYy6Y3i6VRx6eitZLLooMYEj1LuHWTF7nYWMSkGQgIoVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhfACF52uauy_6kl2UAp3gbPVGqz3xiPKLnEwpV5wFf9gR9Zk9LMlRk64j4Y0GxLiaYp7KwCSdzxG8KplPeSi4ZSexAcXLDopBC9ZpQcTsIyDqdNffYlGsXIg9xbvnAWntWxvyKPgLmZAbS_yf4p8Rf2Lv9-RY64bXCiRUJ4phA_CjZrv_aftejYkMUFIbkUHgU62GJccrYKF3JinNIc7ABYfsFlAuu6wlaxpJRcfVU0HKjz6J79rysqQSKJ9SQBkQ3o3zabcUq14r5yQV8S8C1fMmby6gk2cZ5mgmw_7wiHEtJZoNfYLBMlsmZkPzAHo_LJle6jg5bPa8e8S0p3KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbSN5AHoDrp583EiVrIca83wPcEZrRWD35me8KMx6EFnz0dOYbfpZEIc9aiX_Uc1eoIOIA6eOGVYy78DgKu70PNbvtojo4pLbfXoG6Wyd3Gr-eqO7vwShTC7oYIhD6ICQiuqPqGJDX2ZMdU77ffcaklfZpxUvgaZihVu4xthAazOCiVADsJmSOUQFP4MZyxJ86kvbuKfNjJ0gHK4AO3XWPnm1wqy5KMjY3CBMrkFtQxTP5Z_ui3I5tet8c5sYdUCaOEmgoN6mI8Ndp8rcueZ1B3JDWnHAXpBnx-cs08uLobnkFJDoC2rbd2B_cH4kdF9OcPwdIyK7Zw04EBKroGjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5WHSpRJgOYXflWfq1Td7gJsuCiuuqSBXWq3myQn2kY-h-eNDvJYmrAGdSofx77Gx6aJQjanOS6mPZHX7yF_ekig8bGVejf-0Zq0qIWORnejBPBnoQ8847AFsOH4VZ09DysXIlsm5UDz6aAhed4Wc8TUCeK7rHViKf45ffSJ1NBPaDNlrq6fG-tkJE-CRc6jtPTgbhZVzTFrt30HXwha-ioBh0ZfYQlURY5T6tyx0qWWr3Ihue47Nt-TS-tjiogeZ_64yFkEOaU0bmuyuIoY4tp6_LNgJ1dM4lU0WzZ9gR5INFd58TUK_CoXs-n0glWW4V2k9RmUYtECd_zKz5P1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZk7xLJ7ZacDq6DUwkyoq36-tH3tyKZ39uuXv-MKPSGYThpLyYmobCXTiQCxIbaPeQueohJSi8m8iKutSN_6pLNbVTIMnZNVjuqCKciiE78iNrMpdsZre8gCsM4tM7idJii9zSN6wrnzK83fbD-NKQhimUcOl6otOij3mVy-6Yt0Izn-ZSgLa3EfNn54Ll5ywsWyAP5wIK3n7HQw2NDy-Sy82yv-PK6NrfjsQ_bGeI82CHdjdEmnTmoHzsLNZT62SC5OJzHB1iloctuCjvxlhPMrGuKJaNuw4uaCMOAzoStNw_pvk1ArQr7idh0KtBKF-T5irB_QCxIfqIG3LHsggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=JSd5YBvCxklqeQ4d-Iap2jkyWZksVPPYyTDNQueC75i7uc0cxkZ3YlgxYAYSFZil8DxTuZifTD026Dzavt7kkGAp1JYgDtJ3jbPDZSFLtYBOAR1wQJnctlLyiSQ7ChAOHTILNO0kRnii0zQEKf_SyCaDNQs8cXZQBODIt6X93EdWP2bM-thm655TAQBZcyXzTdc0FO0nF5CfDE0egaXzY5RYYXFcV_uLXnlgy_BLWr8vQ9czbR_uCOgvFmDUb4SaO2niRSzpzxVCN7zZTdfNb74L3X1fElNkpVY6hiyQz0qVnOmZCETYH4Jxtq3gbMRrnidmeNULv4RZTJb1UxYwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=JSd5YBvCxklqeQ4d-Iap2jkyWZksVPPYyTDNQueC75i7uc0cxkZ3YlgxYAYSFZil8DxTuZifTD026Dzavt7kkGAp1JYgDtJ3jbPDZSFLtYBOAR1wQJnctlLyiSQ7ChAOHTILNO0kRnii0zQEKf_SyCaDNQs8cXZQBODIt6X93EdWP2bM-thm655TAQBZcyXzTdc0FO0nF5CfDE0egaXzY5RYYXFcV_uLXnlgy_BLWr8vQ9czbR_uCOgvFmDUb4SaO2niRSzpzxVCN7zZTdfNb74L3X1fElNkpVY6hiyQz0qVnOmZCETYH4Jxtq3gbMRrnidmeNULv4RZTJb1UxYwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=SV9JJJlrSTShUES930CJ27lTtU2gZTXkkX8w3bRQgYsTisUikOQ_a6LFiC20q57RLopPw_8e9-53rlqAn7vVkg1wmWpsSQUZiCIBtlRdfkpXyrDS3iyqgyUVeq8vSlR4NMre3OuveJo_Yu2J0FGoGpQmkZ1EXmX5Z05BLsDNwFj1qaCHsUdfb6P6tqEQZSHcrgNk3FE7PJPlK3nE3AXEHwIvL7tufl1Zr4-nvECu-KOzNZMa2n60wyYggcbr-H0widhaPU6KnJ9GP4RIzLWYS3wyhhj5TbBLWFiSxVnLeRuHxTZNd5Ct5FTQY-lMgYt5p-CqJXEzYpkPEFG6DFWXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=SV9JJJlrSTShUES930CJ27lTtU2gZTXkkX8w3bRQgYsTisUikOQ_a6LFiC20q57RLopPw_8e9-53rlqAn7vVkg1wmWpsSQUZiCIBtlRdfkpXyrDS3iyqgyUVeq8vSlR4NMre3OuveJo_Yu2J0FGoGpQmkZ1EXmX5Z05BLsDNwFj1qaCHsUdfb6P6tqEQZSHcrgNk3FE7PJPlK3nE3AXEHwIvL7tufl1Zr4-nvECu-KOzNZMa2n60wyYggcbr-H0widhaPU6KnJ9GP4RIzLWYS3wyhhj5TbBLWFiSxVnLeRuHxTZNd5Ct5FTQY-lMgYt5p-CqJXEzYpkPEFG6DFWXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw2scvlgZS0sDNibtLC-vceRgQ2zQFfKnwFdR6G70BmxFJPkOqoM5mLdxF_NVJ8CT93Ik1t4TdnjSPNud3UNbWnBE7hPg0ACGsr3Z0vBJCSFZhFeuzY1J45olqmkK3zJ8Vi4O8k4JcNp45thWUzo2d9HDtmkHsWCTxK59EUYrvkQ4p0eRrLvGAkiSrhmi5yGXjFhZqFvEAV66jcjnI74G_B_Umuh95dJYkPgQMCy7nbFoqeVCf5tfa68RHovxTKzZz-Z6Zz4pjxmJQ7Nj0GnQbuRUn77HZ-xNRIPDpesCoBkGh5hC79mE7-RqCgMDO_o9J1p3SLOUKjz-2Kyj4Kl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqIO7njdBD-LTa-Na9sY4dBW3gGcAvVHaHvBxp1oKLT-XxRBG1mmfgs1k5sa_R6H4Fb7mbexiD54pUH_JkDVGkCjtpRucDW9liJlf8A6lNfLFv5pq3HL1vfQTrlndTq_znqzC6lmrmp1NUiPTjJbDt_ISSRm-pn1oCUXK7PsOKTupfZ3PZQTbB2u6LJ5-RXOm6fLmEIp4-HIT6zbKVgNGYwqaCJLiQsrfsZkW4vl9rplM1fn8QPCwAsTO8NurA9sN80mbjBVl6ll--gpery3IxI3cq2Rve4I1Wk1OSGBDVZQbjw8FuSUuASAU7iXWQjw7YcxWHHvEQ2UDnFGaM8B8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-GUz954HGHP7nRIoyA9-aKjG338neC7V1Kq39xlDXuvUU5vuToOg92U9uB-W3SPGp2YVbON50hczgcF1oqL79J2kApvnElkv-ElnSB3hBtlZBDyWddoEeXrg9mD-suoqXcT10eUm0_GnESro5E2ZSWLDAFLNGYhv1YaLMFBMxqM-ldj7b8ZX1QZ_-o-vGDk4io6ttpo685QUpKYNKueyj0avc3UJInPn7y4-_MZRL0TehaiC8nrLodDAHqhDJj9XFe245AHUQ5nK_FsFNdebluqravE0ZlGJXrm6Glfad0UQmHd0PbwzhKShZTE29Pi3tHK7y9J0bUcKYmZKIHH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFfJNBIhmnr1_YZRi72OjHeae77eYL0j6_4T5Ed5dwEMio4JUH3OLIDb2lGBqT_bi2zmdgqgEias25SPGkrtVJipQ-Vc1Kce91gjXfF2FyGNJENzMXWQ65ntrQeWrYhOELiu5CE8XAiD2Jx5Bf7APkhDiHCg6J5HLI1PVpof267rQEAyI9pe3BTRQdfHCoVyi9ARZhpg1J0P7ePne_K62Y3bi4MUlUXfSv6T-cHhBgkzy8HzG1PqkheyfQan74GEg5WM4XbePUt1UUtHhgiDdTI7t6jZ67nDA-7i2kG2b_hOOLJzdXmKlBmEE8vJZvuc0-GZXh2T0aVmCC9ZaT2xmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRL9uHcpfEHt6xEvqkPd3PhcNrWLXWdGyplCsCObgkOFcxMQYJNa_KCBBy0JMpM-ZfoNtIhhH_fXisb4al-TeW3nVbPWjgGeOMsYI66zDQfQIiSBEO4sMm640zdS2fMbb5FCWBvZly8y16RNnPw1Wzp3zbRBstsEPTfHmPyK6Jv0G-GcC0nB0-hY2gHorMCSit0dbWVUFMpxJKLOmqcBSU5hwE4tyQrrsOZwWmZP1hI8W8GoXsag4ND5cu6PFfewlTY7V3uzNG0t6178pahSMoId4MY-81olmJjyQCHCQQjd5C7tSE3LgTKADobKr5iBFfDT4LtoFwnk3aVMOTpk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxWjucvqin_iVGrYetqgd_qsKudlNHxB5dPYk-XGVhtqVOqDETNUO3dBHvV4rNz_R9pPEUJpOI-_QVd9mwUc518qeXXsqf9B6FBeaBYcEf7cwgNIEUy_SdcY2RhiSj6ZVuOTxmf9Anvm3hCRnNVjZagcK132cMQvOxJITzrHh7OoCDWVlY4ea8f8ECg0Img0bykdw3X2TMoIk_w1i2d-wO3kubHAs0d-2xopzyq6UN-7aM-NtW3SJrESzUHbgOVHYRZH7DoD7MNAkgU0wp_A_1rv0FPTekzqJ316i2UcxiSi9J9pu0fOApaL7AvEOsL_-54FGLyD-wuLmFm3PdBafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X09gWzstQHE13HJeJT7K_UFfEL5G-aWtiKYOisRATXo47GuV8x7jQTJ5ULe7T1OC09OMYgbhr34WmWFhQCaF-yrlXVbYBPovIrKGQTSx9XbN5xzJK3Xtiz3O3bQ1TkltFdkxFP24_YS2vXq0f5srAE81S9Np3axLtzvVvJ_UqaGHudXUY-ePvvdIVyo4-jMo_Q5Fbq_FDvYNtmzfZIkH7xkUkwxuA3dHIa7EJnZPbWVhnaVYAwY5-xCZnGwCZMvWvG2pZnXzcfIOT7AlsXI2kRtdNy56g1D5JNXQAsi1sz9RYX3St6sKc-LqLOvQac3VDRzksrmqLf2UFbm1hD_8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXXqnko3m9u1tbvKWIQR7KJ326gEPIYerMWCupSGl_wl9D1Dbkj8QMRxHcZXBEt6kc1iaoqc1S_xfIKhuugnV0qjrdqlwS-BSj0xRSwznCAY17qSE1MF84ulW8Ol5NZDuevvZGkuJIosNGL2NjY0dby36qHkLb21mkBJXB4bhWK3Nlh8BLL8GfCiZg8c9lcg1PvHtl8DXMcVqsR_BFZq8J8TlfTHk-739dAMp_ibutS3KK74f2gJI3QrD1_AIMHgSTqSo454oYi8xi8zkdFdl31zjSXAVQxiNjp3lMievoLg906HI6w0SqTaZTJWYw6pPkNe5HevpjGIq0gCLhVK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deChXJvxHblMkcVhe8pAfuZX0dI-ThdukQWW_pCxbiwEUW-yJPR1xBudV4AtjMGv_Z4bsk4kmW5MpH2VAgsOtv1yA-WjLSLDpGr4a-CQI_QsuL9_EdawjlR3b3H3oiDevbDsGD7Og924vioW7k5b-ya5WDuHBET9cv0b_PwHoWRaraPBluMOrXL1Ik2c7wrcZru4hybG7zLiQM8ANFozS9AMWcBnsBgJKLQyXgUF2W8ZI2KSlu1jj1kHDR-SAcB4xcBQ3GrX5ZErlEQGqE5TZaD7wq61SDT18Zb4PCbVAgstSy-H2oAVVEdSrApAdf9yvL-mGqoKl6nyZtUEPqTtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOlmbv_U6aLRtgTbnjj-YqTscsYNFY7AwJoOSWipAGBcfXCQbAtdJ6ZYhmAU8x-5Ur2wVIX53pnGkd5AAP0FQOaiGGRic-Eb9sQeEGXKBIOo3_CgMitooHgT28RwlvDMKFLMSTVA6nA22wgfdoYo_y3h_jO-8k2Cg9r_3NoTC_kPiX_MpVTYx83j9uZ1TDEIzF6fjApg5u7Xc-JK3c3ZnJGmsSJrhBhFmCCrEGFpgpNBhUpAeEiYiHHhXdPp0_XJkY6ASwcdQyX7lnS-VlRHF8KYS2Unzl10KOdiKebeejhTcILbPpxCFa0QR9qEmdlNVpT5V5wzaAsNoMwHaRlcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzgw8n4zWylopSL0C-ZL2hqGusODjys-MhEKZYVPiX1QgrfkmrEHma3K57Sp28-RcH-QIzsxMqWwv_wls6hIvDBrsSuso1mzBIO8A85NibnhggjikZJoSfrqMno_mwAwzHNqK3udXWvYvXwSp1rKzhx2rfIyEHs5wicQ9HHMdXve3a2kqlzdvNMOwSqbR0KOSouSJtIykwbaat030l4__JHYjqRLrRCLSa7YLEx1fw_2EC8PNcxTCcPl-BtPa03jOulPx-i2wr8YE3xJBJSBPY_ayuQL1_lhmeIykcimzyOLvUEeurBZeYqWxcV32kR0UQFz31f6LK8Gz3FHE1znIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc4ckFBoUHPBgoppgCYmo5i065zHVuhgn3dpep5_k041drYxJ-_DkbuuqB92qGFN88-ebf2YZwai8dLcjZw8NNuwPgrp5bBByH08gCpbMXY0s9daKGDwvmPxRKi2eWtW8gf2-sW2WK67KruJMRi9-DIfLAUN4cqSehDKTWoxlIIQ1zCMJZJgtqScYEQDGeV9LYp0o7NU72pdJamYWb6abbWK9QrmGYfa-hPhad0OaEzdzeYjbNdvlzNR1eaHa8tg38qKiY3GA4eujVZ88j2-Trf01IrOGQ4MlyDkvQ9XoEj4O2cbfLx395u1dt8luq2pTAL5iNC_b6731MApGLGwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=J00yFM6mRRdMswWGsgcXgNlRKo9wgRM4FwP4Mk1LbIOFvaisEk56c7qiBZAyVU6RFPMokdQMVm3OdxvKw530qftrYYa8MeqWW_JokcVuTPPF0PrItOv_d94QzAew8t4nlMfXtQ082F7gZEMOGLhNqKUAfnUk0J4F-PlADNd5RChzSlaSngDGq6xq-wVXHOLZaL57tWwSRtuil8q2fbJCVvjNBAl2adSJ-Ns53HURCoLlrDHwqkeRCnv5YZ4Wa5mL1EadYjsSf6c7Sfri3z0PXCUWoPa6Oqj5S6fvFtHJMvGs_9H4YTU3g0qpBQI9TTw1qwukPhqRwWM8aT35o06EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=J00yFM6mRRdMswWGsgcXgNlRKo9wgRM4FwP4Mk1LbIOFvaisEk56c7qiBZAyVU6RFPMokdQMVm3OdxvKw530qftrYYa8MeqWW_JokcVuTPPF0PrItOv_d94QzAew8t4nlMfXtQ082F7gZEMOGLhNqKUAfnUk0J4F-PlADNd5RChzSlaSngDGq6xq-wVXHOLZaL57tWwSRtuil8q2fbJCVvjNBAl2adSJ-Ns53HURCoLlrDHwqkeRCnv5YZ4Wa5mL1EadYjsSf6c7Sfri3z0PXCUWoPa6Oqj5S6fvFtHJMvGs_9H4YTU3g0qpBQI9TTw1qwukPhqRwWM8aT35o06EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc0RmRusCtCQfLuzeoF2XmYGrJ3zcMGL-OIN_Y-5fngjNfbspaODZwhXb4oCkIiFc54lRV2CSLW7PYCAWiw79q8-CA7bG1DwMGC4n_DFZGarY1apRPWv0OftrmZEBUFgWJXkKagbv9fI7OydRA9_qb9lAeb8a6hmaelpKpx6MnmA-5biKgcG-uXqjUtam-ZJYe7t_MNSte_I3L9nj94zEk8tfrCXKinkz68sMoyMck-zSRf6uwYObZMD6PoVT2MzUW7KoTcQJyHLrS-UjbGJwwN9F2kPdyIXQM6666YbyrzfpXA-Kjw4hFpllvs--HmcP5Sz5takIbfFnfQfn9sZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrX5bMxwfmzBcEa1yogy99pFiPOUipLP9cksb3qBO1rT41Izcxz-fOu8URXT9FXHnMPSEDJ3zZ-tRbXxQ3hB5T-LyDKerBwyZvZhBPYS9jcq4RlUvLaOHOaJXbY6B28W8PAXoZAPEs8HW4L3IO8j-OTET5mGL8VnSbjZ2RYlyVABMuQFuSHYkKw09_KOTSrRXBFNNI7PRfwlPC4yWVy84WGpOP9QG50wu_0E4CKe6WsWaQvokdSISzJ1BzRFU8aQM6byYvXSkYG4vSw690BsroF7Jte6SE3p5z8YfvBSw_s7Rc2rr0EN6M0x7q0PgTuXJCBr6cWpxgSpJ-p-ye8WNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLOuLT-vG_0HYSkJriNJwcAhTgf5n5dzMxwsYEzD9AROrKIFMlmsZpX6rMTqTF4fbW6yL0EJb3AMS7IcWqvbfHqyuStgdJIiiXJ-bR0UmzRISv_8pRLqBv8Jym0TQa3XHTh7iBSvABgCEeSo9dgN5q5Ps0R3PgJMU6JZJsqPcwDK5c9ZwiuC1NO8a8hbfJH_xoieuLRNWzPln7wHJpyhRDMCbd10qf2yzHbw_ariQWWj9AU-8Sgm767HhXWstdX7SWioojfLveBl2P9jwXs6J-cffjV91a7qG6Gy2c6m6EXnbSPfYT13qaMhXfOUcK-ChBuXLWiS6zE4HOZrC_0Vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=bfNdx6nR-iCueffgjkcIX_OM2aDxcnzRkJ8nghmdheKcPCee7mPcsc56_LIgbjOfu2EkdDjSrUqL9CzZ1AaISPrAd92oL4q1v4dNYKquo226PdX8WuHD4TXAwqoH7yhBU4vT3VFDYSeLjO_sk_b-0OCChhUrntKeR27bP_1i3Go_MFgG9pnyVSZdd1WsbsIqOnqydbdE-cWtQW1eVKiKhfM6mh2ZMjEGOLmME3L1W2aLTno6sQrx6ZfwSUyfoidrRxoMYDR3sk7LCdJ4LagIK3hHHPYQCEh12JJOHJfazx36wD9D5rgGl-osZx60HoKgAf1TNJzl0kIFr_cmCrDoxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=bfNdx6nR-iCueffgjkcIX_OM2aDxcnzRkJ8nghmdheKcPCee7mPcsc56_LIgbjOfu2EkdDjSrUqL9CzZ1AaISPrAd92oL4q1v4dNYKquo226PdX8WuHD4TXAwqoH7yhBU4vT3VFDYSeLjO_sk_b-0OCChhUrntKeR27bP_1i3Go_MFgG9pnyVSZdd1WsbsIqOnqydbdE-cWtQW1eVKiKhfM6mh2ZMjEGOLmME3L1W2aLTno6sQrx6ZfwSUyfoidrRxoMYDR3sk7LCdJ4LagIK3hHHPYQCEh12JJOHJfazx36wD9D5rgGl-osZx60HoKgAf1TNJzl0kIFr_cmCrDoxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJl9EXtjfvOLuactwoWkQlpxa5ztwD5R3T7oVDviL-Zo76qFpDK5rB98pplRaAtqvN9PrmOGyRvcW1IIShqEO9mcYuKA7NNaUPI__TV5wqhe9FgLG7BqQ6Ic59vXwXpw6IzY_rPNs610KqXKFmt7sCWnz8INsaSoAJ7MDZThPscrTdkJf-4eH-rKoQBNHLd442_Ts1Jggj3z6LrchElI7oZSr7dXeabjRXGBRXYzUamlVJehd0iwqUTT-AZk2WJ3c2GXjSszy4W3tjsbGWZNiFn6tY9bDC6Ot2g7W_PhEB89OpOPEM4EMU4Yivm0LY9_sUa1BTPUa13i0sb-XGno2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_DIpk5DYirT_NQcZ9K9nDoip3hKlBxV1_SEUcbA6PLieo50xN-hYNwZMEaKN98yVFkS5OG9D0V9jgKT_K6VYX2xxURkFoyFvMMz2yJLUpag2Kdu-ueWc0l68nDt7TJYZcNuf5dm4336yBdjbUYAe-71cD7zh4P7IHEWZOuZ5agkO-1OLSqOq72TkqQwjU1NFm_96Z5L1aj3BRwg_otsE73V6t3ggR7ITNev0epk1LxrQMu4zATcIYhc8mbZbT4j-F_WHLkDbFnh_pYAsW-gQkqOsjKCGFZGgh6P0QKH8y-CmINCnGq55KStKds0ZGQkEo98HXhOTYJumP6lBET8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=ohitIbk_GjnXbZ6dMUoabE24IwEIOMM9WrlGvtG70_5Uc3dmMR8QKfvaj_2sstTkb2ZFr0BtHWOA88D742_IKgjUTHoq02payAknn7Zv3gtDYbQ_WVfZAx8MDUHG_IyRQhDxM22sLBHdes4EP7toeQXr6c8S9b1Zi9M_pZRGWLqG9srwRoGbSjgmP7-ZwLjDmgZ1SQuMhwPXO_clCEckd8b1e7ddxr2qic1euPTdh5hEhnEd8n91f_Et4s-lRA82QCIw13ThVm0BLVvFYuJZaD6J5gu4w1dREGc9L7KKqAo5hs4cu1S069J10QWJFBMJ6OiwtLPt4YWw47Jxj4lGbwPEZR8FgVmn0k4Hn2NXUF5WOLR-rgntdjW2CLQIpC7l_iK7XHM68H-B7B9VcWB95z4BQhJ19FA6fizCXsa3JfeYMBTtFYQd6UuIAeSD3hCz7aAX9s1SB0b49v4RnP5BSl3JWJsfnWDkv-2uZ80rNzkrXYsMM2pX9JcF0qwYajeFDGI8z0HeDbRtrtzVQ7pMKJ374CoWY2NFpHu8KjhqBhtHfdu9mBIZIc3bF1_5mXm4yLKYk7jspvOVf0prsJZHedMGjUrQ2bNRUAIrmgMemVfQUVtNlQf09htvmE7xn3g5Mx5IAf7TPoigFXavr4hR35Cb9L5inYvOYNFTSokMoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=ohitIbk_GjnXbZ6dMUoabE24IwEIOMM9WrlGvtG70_5Uc3dmMR8QKfvaj_2sstTkb2ZFr0BtHWOA88D742_IKgjUTHoq02payAknn7Zv3gtDYbQ_WVfZAx8MDUHG_IyRQhDxM22sLBHdes4EP7toeQXr6c8S9b1Zi9M_pZRGWLqG9srwRoGbSjgmP7-ZwLjDmgZ1SQuMhwPXO_clCEckd8b1e7ddxr2qic1euPTdh5hEhnEd8n91f_Et4s-lRA82QCIw13ThVm0BLVvFYuJZaD6J5gu4w1dREGc9L7KKqAo5hs4cu1S069J10QWJFBMJ6OiwtLPt4YWw47Jxj4lGbwPEZR8FgVmn0k4Hn2NXUF5WOLR-rgntdjW2CLQIpC7l_iK7XHM68H-B7B9VcWB95z4BQhJ19FA6fizCXsa3JfeYMBTtFYQd6UuIAeSD3hCz7aAX9s1SB0b49v4RnP5BSl3JWJsfnWDkv-2uZ80rNzkrXYsMM2pX9JcF0qwYajeFDGI8z0HeDbRtrtzVQ7pMKJ374CoWY2NFpHu8KjhqBhtHfdu9mBIZIc3bF1_5mXm4yLKYk7jspvOVf0prsJZHedMGjUrQ2bNRUAIrmgMemVfQUVtNlQf09htvmE7xn3g5Mx5IAf7TPoigFXavr4hR35Cb9L5inYvOYNFTSokMoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1cMolijdWmfg3AD3_hWQhehIfuNdTas4m38ZWBEZiT7lnj71gWAGiO-oz6G6zjMWWxvaEwYVYBM-Mi9pvtkulT5nMK13QJ1Bu5vXodbODSc_sjBdy16Qj8IzmVkdc4jykAvkFKtepkLiLXAdttf-LeYmVjGPYQrXCx8mtfBHXepDK5PPc1wXiF1AdMcZ2uv1cWNYbM0cJZHARp8cS-KLRUmES1h_-13DGtd08U22jiTKdtvZm8HASQnlt6gdda_JDxvi5_HrkrCqx4EE5rCSkwnAkFQvF0PewTul8-VNZiXe4m7I7kEBJK2iob5vsgKZ0QMRykGyq5uyCha3LzJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=rjo-yeNRwJw8XL3bYXwlvGP2FuBqaWNDF_nctmNcsl1iWVJqe6wHAF9mytA9CtFkKo4fQ3uqoxGVPDp2AUgkht9jvBnRgHXYQSGGWjZnG4l213E9a1sQNRzoG0NAVnaR_SKMqHx0YcdDzf6bxgp4jrHjnoPpf5TZC6zi-aDCd9zOH2yfgiF-MelS_zHaf-YNaTTePTINajbDD0PiMXY_aMVCwYMaYYljo4aevydHvllWMT2CFb8KZa2q4hzljkwy7o0HaILfPig_o9vsAz-9lnQTutJvYGT1s-jfd6BAV0Yg4TJAJI7-Hip6VWL82ORE74k1RRsXMiO2d4o5Gr2MfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=rjo-yeNRwJw8XL3bYXwlvGP2FuBqaWNDF_nctmNcsl1iWVJqe6wHAF9mytA9CtFkKo4fQ3uqoxGVPDp2AUgkht9jvBnRgHXYQSGGWjZnG4l213E9a1sQNRzoG0NAVnaR_SKMqHx0YcdDzf6bxgp4jrHjnoPpf5TZC6zi-aDCd9zOH2yfgiF-MelS_zHaf-YNaTTePTINajbDD0PiMXY_aMVCwYMaYYljo4aevydHvllWMT2CFb8KZa2q4hzljkwy7o0HaILfPig_o9vsAz-9lnQTutJvYGT1s-jfd6BAV0Yg4TJAJI7-Hip6VWL82ORE74k1RRsXMiO2d4o5Gr2MfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEb8UFJnms2gDfrEMHax82ZTfu08mwX4GzvmUbUoosBuNBuptXc6kyl-FikfTjI3-3sgEiYCZxujc__LfoOnr-YzdCqMjarqAshWemt6I42tM5a-YpGrTGfMdXHUrZamumgMfvEn2q03mmD2S63wlO8NFzgjxLqMmxXZn53OrUh4mKwquaKIOiGPGmyw4fjQbOdlByk7wcTkkqJ8zotiEbY7fycsK75god4sWDj7jSNxKeFK5TiPW10EphTU-1AInKU1h6g0wcgvoMwdvDzHcnN9b9Js53K_Scazdj8cXuKRN-McfKLiPtujmhfusTbyEo0OBzB8mQ-0hl-HA8f_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smdxDNkBjue6QUWzbgcGx-xKdkew9DHbWZkqS0tgARU4FO-kib3rb12jCImoSz96-FukbO6osvw4ZLR1uFoDxBS0OkpnGcYmS_ELDy1xGV2ukXEzzxqSu6q9aKIkOVbTet_Mn3wgdkoLejVJHtHTozdOUWkqWbzJxj-RPT_fp6Qpl2XWQV3M61DAc9j59Lu8byuiRCQvPPRZv75bAwtEZwOBG3kcEmJzrA0ZOdZPJAy_NQFLSvR8mHqZTkLumtSKSnay5CQuHdfjNlE3_B234KUeWJRWCLH6BF4Luk1UfAqR6vd3HkPDmBmRAPEHMDwg86wqSZT94q1Qk0M1R-0i5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofePGT_XcK6mxfeSChlSbK1pmt64_7L15h_DkxG93yPj_HBZAAjQ0K6Ku7y7PAVE7V7EgrmmxsOLgJyprlCD5nSIT9mp8RitP63DK8TbsEx1WD1ugl8iibgaGSpEWFtn9kJsmG4W0LpakVxyh-ptAJSuFmy2Q689doKvs2xYwMjrj6v5nctemM914CCZ6E6URsSJqAUJVgbultgFBwEDdmfYai9Wb88OtsSpQ52Gc2h7SofMsytHUSJL0hZdzHKoemvwP2bJXMMXCY0qtrpgp_rGkPLdMebwuMyTUs_nGvhI5lVNkmZ81Ln17utcmHlfkrdgb8cKd_6tHfRRK4gNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-azDiD1hhoAyrdlCRkjdQWogw04u7MCOWSQP7CKGyNkXL9Fq70oICIdK0GCpBIwCaqI7nGr-_Ul1UAfzRDjdVagYjo1aue1st4vym_Pys8ah3Luh3K6P32DveGF12fHt118Joj2t8IlsxyE6uQPQ5LdTh2KSB41ZOKCDCU5739IjKhFOEo1BsKt7kUADUzegiM1iiHYWQBJVSrId17JUVFzA3XEFC9IoDdEArKtnjFCm_mX2aXkt2m-qZNgoPYdG0TUXbMDN7mmYk23GfRoQTseIV1LkuqxBnS1FVTnhjZ9ChbLGtR09qxYxK3GZt0ASvVWSEiZyap0M5GUk09Anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=aKNz9tLn7XM8bf2z9O51125xpO1g1zJVjesHAV8oB8jBVCjFkNr_lf55nFJ08zwbziZH7LsCtHxkHsNGE2A5hzloSSUa9QS1EjTPXj-RppUbsD5vs-H0gENdJeQCLzrpyfAw4kjvqzSTKjWg0h5giL088tv04nSpPQWzXBzjUs4F5G6bgLYc-EcbCrVQAC0fixzxdTue8BEOGL1FmHEL98j4H45kZmn22nCBw7kKnKejL_F9tpMZ5amHy-ltEJmNj5uuKNeX0sWbSsFBkpGqiPPWLHn6NKbJaLKkdfOT-EUixAk_op8SbSO2oHaGHQDoC0Ldwe3hfpqsbVWatfNR54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=aKNz9tLn7XM8bf2z9O51125xpO1g1zJVjesHAV8oB8jBVCjFkNr_lf55nFJ08zwbziZH7LsCtHxkHsNGE2A5hzloSSUa9QS1EjTPXj-RppUbsD5vs-H0gENdJeQCLzrpyfAw4kjvqzSTKjWg0h5giL088tv04nSpPQWzXBzjUs4F5G6bgLYc-EcbCrVQAC0fixzxdTue8BEOGL1FmHEL98j4H45kZmn22nCBw7kKnKejL_F9tpMZ5amHy-ltEJmNj5uuKNeX0sWbSsFBkpGqiPPWLHn6NKbJaLKkdfOT-EUixAk_op8SbSO2oHaGHQDoC0Ldwe3hfpqsbVWatfNR54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
