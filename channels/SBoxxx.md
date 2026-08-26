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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgVp8oS6lo6s_Na4kwE6Ec9Vc1FET4u8DMRnHv2DORFEGQZwNSkCh7W5nEQII5W5wGsO06nHTsoTxbNaCgOKZ16EhOEgRpQdiLh0ba5f0WF6mwbNb6BulFbZZPwi23NGemUr_nvxkFmhyLcZxG9nqGbDsQvdUHi8cdaAAoz1BYXLzVInCFd3il9yfp3V77B57CQsV_24o4KTdDxdEY-UV1jy7ozfTZ9HVuNdIvjKhnNoOwZ8eWs5EmdsCoCHtDMpqAh5DSV1JUHzWM_isHJnzY8jnf7Jz38qsky-yPN4TCDMxal-lr2nuwc78OV2yrQvisBXFMvtfTxuKNpklBKHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQLx8iSxwDe-pxoXIKF0oohRRPcakYlkuYPLDNrttmdlJRcJP6IjsRGNbIKcLoJY6tY5NsmU17i60RhH4h8tHd-LspdPCcdhCUezH-JzKLFT51sNh1TjdjCT5w8D542fl-y1PysUOVvU0kXfAv97J9V55D-IPBQf4m6G4M7JLJik8KWrrRLEhQUtyLWlbup4_OYvwXTXAE_tsbqhHODzElOmO50U9-UBCcVi-eZ4hpHh0uS2n4_wCcA7eSvj1mrM8qqddsEIY5XU6M6NZ-PHC82yraYKelx0PB0010lMJqvwjp-kVoqCJihADkojC2Cdhnmvd2KvTUFCtc9MSJoo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=uFZ4lmT5waVr_cYAdntloTldDAlUKpxV5Bu9qUN1wWmApC63OCySX-iFuAgQ9jOVar50pa49vXA1QwxeYnsDVGoBEjtobybGVAZuDBt2uO1TVd1L7NB94N-e0P9yGPW1R2ng-wTjbe3ClqMNgMzAMY7owl48u2NigVLFlprTEH79Y0ckxeBpcC69_GtIlDBDpT11QuKHJ5ZvYvathBipgObYNTG0nCh8YQXJL6wPfT9qLDPKZNR0lxPwq7zrADAAmCAD31G4tXrtrEUkOI7-vwIIsedabsfHcR0cqXy-foq1mLqtvvvB0GpjJYsTMzpNTDAvxQ1a6rOZmuMBSsAzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S83jB46GDI0Fo9gsuFkDF7sgMTBBfxrbMJSsM_VK9Kg9cQIs-Eq8XBKjtr-uXxoxi6Xq1JcBQnwKTG7QsoZ2klT-XYZDKm641CayvVeUaOlj65uyLZNFoH25DDrdvFAQK9U5_5llYtM3knyrd75qaQtb7GY1SCTUJgELYOsLAGFz7DD_hMQOfvPUw1Uu1dYzerUN3LRtigbgeI0bStzOAs-5qFoKLJhGDGk5Uj0GKytYbdxrxkAzN8wPsc3qh20CJymVh-6ZNT6nM80urO7vS2rVGeEcu2iP3H7reJYR0wW3cfUAJ2Fmgk2kxIC0-B5QqCVR5XW9ObJErWkfRKnjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qwy4MwPBj0CV0ArKtWoDVrqjrE04A_VZ8dVZO-VD-ZW2lFKTu6cjJJl9He-wcXezfWQmul37ITr5KUeyxEcHaFsFXEWwKPWeX257koIFpMhYK7U8cb_oBN_h5AB-3rIt6H4YzSODJVrHQg-80xnFBB8umW4k_kGFuitM4fhi-YVrg91H4Nx9gtzJnwP_mvUuJCNi_aHGUZ32mtS5lbUkYElQL6kYIRDd6n03dMVN85DFwU8atzLfKWVsMf5F5yHRkNROAQ9EEXfskRsYnVMnDb2Ne4fchTac9BjUoA32c7UPhkt-gUczz4Rc-yrjEL5rMxZBU9Zqkoo3z5u4cq61gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNS8Gsot92uRlwDDEmaaC-aBITySaIgoI18JowbZIIns49XomhBye2iYoxdRmfJOkWw871twQHWJ--s9QS_BkxKNi9jeTa3Ys8vmaF1IrPehlF0AZUSF_EFMED38W3WU4qx60dJsKicCZzdFSSOe79pb-UeZzZgKGH9Ve4dlb_FrbVqiQoJJK5pdwn-V7JgGZI52lN4RUesp_pVKCvq74tmifDzg2T5FInT982nJjr5nEWEKcnTeYIR_P_P5ZmleUbEHBCRGScg3uSMA_O5AFEadYfcPEJcYkMFmPuRFOYy6Y3i6VRx6eitZLLooMYEj1LuHWTF7nYWMSkGQgIoVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhfACF52uauy_6kl2UAp3gbPVGqz3xiPKLnEwpV5wFf9gR9Zk9LMlRk64j4Y0GxLiaYp7KwCSdzxG8KplPeSi4ZSexAcXLDopBC9ZpQcTsIyDqdNffYlGsXIg9xbvnAWntWxvyKPgLmZAbS_yf4p8Rf2Lv9-RY64bXCiRUJ4phA_CjZrv_aftejYkMUFIbkUHgU62GJccrYKF3JinNIc7ABYfsFlAuu6wlaxpJRcfVU0HKjz6J79rysqQSKJ9SQBkQ3o3zabcUq14r5yQV8S8C1fMmby6gk2cZ5mgmw_7wiHEtJZoNfYLBMlsmZkPzAHo_LJle6jg5bPa8e8S0p3KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbSN5AHoDrp583EiVrIca83wPcEZrRWD35me8KMx6EFnz0dOYbfpZEIc9aiX_Uc1eoIOIA6eOGVYy78DgKu70PNbvtojo4pLbfXoG6Wyd3Gr-eqO7vwShTC7oYIhD6ICQiuqPqGJDX2ZMdU77ffcaklfZpxUvgaZihVu4xthAazOCiVADsJmSOUQFP4MZyxJ86kvbuKfNjJ0gHK4AO3XWPnm1wqy5KMjY3CBMrkFtQxTP5Z_ui3I5tet8c5sYdUCaOEmgoN6mI8Ndp8rcueZ1B3JDWnHAXpBnx-cs08uLobnkFJDoC2rbd2B_cH4kdF9OcPwdIyK7Zw04EBKroGjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5WHSpRJgOYXflWfq1Td7gJsuCiuuqSBXWq3myQn2kY-h-eNDvJYmrAGdSofx77Gx6aJQjanOS6mPZHX7yF_ekig8bGVejf-0Zq0qIWORnejBPBnoQ8847AFsOH4VZ09DysXIlsm5UDz6aAhed4Wc8TUCeK7rHViKf45ffSJ1NBPaDNlrq6fG-tkJE-CRc6jtPTgbhZVzTFrt30HXwha-ioBh0ZfYQlURY5T6tyx0qWWr3Ihue47Nt-TS-tjiogeZ_64yFkEOaU0bmuyuIoY4tp6_LNgJ1dM4lU0WzZ9gR5INFd58TUK_CoXs-n0glWW4V2k9RmUYtECd_zKz5P1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=eQB95hxstEGBmKT6j0vIa16aob2T2-kUMi8785jp2uzc4RksN_w4m_e59azgmsahzLkXlqVYOte7-Xvzade2NeNHHZ0trBk3dBk5VK7l8hLNb7kIO8ds0YnL3IBEvJNvKU5BPbYzYEuyzHqMH-uXm0LtqAf09GCVzn5p-N0mYt9Cdnv6S35iIBOmelK2zsba35sch1xuiqOYcEfWxFY9IGUup_06PRJ-D2gQorUygCxh0H7dz2prYhq8mnFsxAjrXttE5Ax_B7UunBX_yJ2RXdsVhXKRU9QZ9loriZKUOgVEY1_z1StCFlv7QT25DoB_VcKQCsFU1DmNildG6hHa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw2scvlgZS0sDNibtLC-vceRgQ2zQFfKnwFdR6G70BmxFJPkOqoM5mLdxF_NVJ8CT93Ik1t4TdnjSPNud3UNbWnBE7hPg0ACGsr3Z0vBJCSFZhFeuzY1J45olqmkK3zJ8Vi4O8k4JcNp45thWUzo2d9HDtmkHsWCTxK59EUYrvkQ4p0eRrLvGAkiSrhmi5yGXjFhZqFvEAV66jcjnI74G_B_Umuh95dJYkPgQMCy7nbFoqeVCf5tfa68RHovxTKzZz-Z6Zz4pjxmJQ7Nj0GnQbuRUn77HZ-xNRIPDpesCoBkGh5hC79mE7-RqCgMDO_o9J1p3SLOUKjz-2Kyj4Kl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqIO7njdBD-LTa-Na9sY4dBW3gGcAvVHaHvBxp1oKLT-XxRBG1mmfgs1k5sa_R6H4Fb7mbexiD54pUH_JkDVGkCjtpRucDW9liJlf8A6lNfLFv5pq3HL1vfQTrlndTq_znqzC6lmrmp1NUiPTjJbDt_ISSRm-pn1oCUXK7PsOKTupfZ3PZQTbB2u6LJ5-RXOm6fLmEIp4-HIT6zbKVgNGYwqaCJLiQsrfsZkW4vl9rplM1fn8QPCwAsTO8NurA9sN80mbjBVl6ll--gpery3IxI3cq2Rve4I1Wk1OSGBDVZQbjw8FuSUuASAU7iXWQjw7YcxWHHvEQ2UDnFGaM8B8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-GUz954HGHP7nRIoyA9-aKjG338neC7V1Kq39xlDXuvUU5vuToOg92U9uB-W3SPGp2YVbON50hczgcF1oqL79J2kApvnElkv-ElnSB3hBtlZBDyWddoEeXrg9mD-suoqXcT10eUm0_GnESro5E2ZSWLDAFLNGYhv1YaLMFBMxqM-ldj7b8ZX1QZ_-o-vGDk4io6ttpo685QUpKYNKueyj0avc3UJInPn7y4-_MZRL0TehaiC8nrLodDAHqhDJj9XFe245AHUQ5nK_FsFNdebluqravE0ZlGJXrm6Glfad0UQmHd0PbwzhKShZTE29Pi3tHK7y9J0bUcKYmZKIHH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFfJNBIhmnr1_YZRi72OjHeae77eYL0j6_4T5Ed5dwEMio4JUH3OLIDb2lGBqT_bi2zmdgqgEias25SPGkrtVJipQ-Vc1Kce91gjXfF2FyGNJENzMXWQ65ntrQeWrYhOELiu5CE8XAiD2Jx5Bf7APkhDiHCg6J5HLI1PVpof267rQEAyI9pe3BTRQdfHCoVyi9ARZhpg1J0P7ePne_K62Y3bi4MUlUXfSv6T-cHhBgkzy8HzG1PqkheyfQan74GEg5WM4XbePUt1UUtHhgiDdTI7t6jZ67nDA-7i2kG2b_hOOLJzdXmKlBmEE8vJZvuc0-GZXh2T0aVmCC9ZaT2xmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZgP3ZgF0bJUOGQUaXf-d_0NBkuuESiBg-AiRU6PcAs4Rgv8AuGEkaadS77dg7bQmtOhlXEuMo1iBBzwUECiVCCX6tv_uaKvwHMz8yc56iB9UbN6zFkS_DTtmbHo-YTiNi7yoB2_ScymU-9N_f0JkdBK7-6AjM4yVHIXPDngyZJ0jhEMoAqMaN55dinDpbw_U2HFkYGKG6U15qh12Zz8PKxBm-uHlOSPZ7EYJPAT0v5_a-lUBLRN6ELxcabwgBGZNgqE7Z1ftBMsck6hOAxgICtn8Yu_Qu0K0MtsiJWKPGCrMFUZ5IqsRW_r3Zbs-lGTfY9cHSZwKkFzia7603YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxWjucvqin_iVGrYetqgd_qsKudlNHxB5dPYk-XGVhtqVOqDETNUO3dBHvV4rNz_R9pPEUJpOI-_QVd9mwUc518qeXXsqf9B6FBeaBYcEf7cwgNIEUy_SdcY2RhiSj6ZVuOTxmf9Anvm3hCRnNVjZagcK132cMQvOxJITzrHh7OoCDWVlY4ea8f8ECg0Img0bykdw3X2TMoIk_w1i2d-wO3kubHAs0d-2xopzyq6UN-7aM-NtW3SJrESzUHbgOVHYRZH7DoD7MNAkgU0wp_A_1rv0FPTekzqJ316i2UcxiSi9J9pu0fOApaL7AvEOsL_-54FGLyD-wuLmFm3PdBafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X09gWzstQHE13HJeJT7K_UFfEL5G-aWtiKYOisRATXo47GuV8x7jQTJ5ULe7T1OC09OMYgbhr34WmWFhQCaF-yrlXVbYBPovIrKGQTSx9XbN5xzJK3Xtiz3O3bQ1TkltFdkxFP24_YS2vXq0f5srAE81S9Np3axLtzvVvJ_UqaGHudXUY-ePvvdIVyo4-jMo_Q5Fbq_FDvYNtmzfZIkH7xkUkwxuA3dHIa7EJnZPbWVhnaVYAwY5-xCZnGwCZMvWvG2pZnXzcfIOT7AlsXI2kRtdNy56g1D5JNXQAsi1sz9RYX3St6sKc-LqLOvQac3VDRzksrmqLf2UFbm1hD_8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXXqnko3m9u1tbvKWIQR7KJ326gEPIYerMWCupSGl_wl9D1Dbkj8QMRxHcZXBEt6kc1iaoqc1S_xfIKhuugnV0qjrdqlwS-BSj0xRSwznCAY17qSE1MF84ulW8Ol5NZDuevvZGkuJIosNGL2NjY0dby36qHkLb21mkBJXB4bhWK3Nlh8BLL8GfCiZg8c9lcg1PvHtl8DXMcVqsR_BFZq8J8TlfTHk-739dAMp_ibutS3KK74f2gJI3QrD1_AIMHgSTqSo454oYi8xi8zkdFdl31zjSXAVQxiNjp3lMievoLg906HI6w0SqTaZTJWYw6pPkNe5HevpjGIq0gCLhVK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtXsda68iX0dAP4EVohYlO_RVIyi2RvVdeIL-pxcJj08NuDarRF91n5VqvDKJqevY4GcpKoa8oE_UJlrBEOo3LIX9OASESh4TMR44s1soP8ehfnXv1B9OR5L2AHlNjYv8DzNF3JEQXj79JodiL7UA5GqzubVvbRApNDgPKRQQm73Il7oxXyeMWuInN6jediyhseZSaqO7gp9jUlUZUxeIy_1DZAWWjr-N4kgyDXjGj--8VVhsOkkVUrlaRKUV0pBG9ojDirqhXVwkhEELVFJexNsSeXaHoCwgreS3U0X82iTSHPg_aWGoK4v0dU8-F61GS4dsKrSy3mndUb6x3t2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOlmbv_U6aLRtgTbnjj-YqTscsYNFY7AwJoOSWipAGBcfXCQbAtdJ6ZYhmAU8x-5Ur2wVIX53pnGkd5AAP0FQOaiGGRic-Eb9sQeEGXKBIOo3_CgMitooHgT28RwlvDMKFLMSTVA6nA22wgfdoYo_y3h_jO-8k2Cg9r_3NoTC_kPiX_MpVTYx83j9uZ1TDEIzF6fjApg5u7Xc-JK3c3ZnJGmsSJrhBhFmCCrEGFpgpNBhUpAeEiYiHHhXdPp0_XJkY6ASwcdQyX7lnS-VlRHF8KYS2Unzl10KOdiKebeejhTcILbPpxCFa0QR9qEmdlNVpT5V5wzaAsNoMwHaRlcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcj8scUpAi9utBd0RYkN02gYIewGeZemPQJZTeN57dxvUHLCCUJSg8fYiN_XoCyEs5n47aPqZrZCnTrr6qKGL_Pzc8tHx243RKQbMP2z2rEPOvkar_ovKItmgjS3RLN8IQkwCXqeo51DhR9OHvpeHW8EIHksVzpelz6Y7d5R1Om9rqFZnubQpOlnNEsYF0Ox_FwQaMCd1f2U9VKnPQkK2qcT_K1jM_kdEd_Uq8lWLeTXt55vhfQKNjRIMKB6ZCNFuVde2Ez7HfXCaKw3Af7X9gHXixra9mJPUm9GiQfwGbwseLGCDni2uqfEl6qhzaFpq1auqrO3sucxhPJcksqU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benlTJIG7UdAqF_ygVktlP48oU3UNkkjxlduyLfcInah7-OIm9woWrEL3SzctcOLuuymUQOJN0ja44nJSOhnbP73OXCF5b4iTQp9TaOmLUoQx3EusZdzldEAAXjofvCp4uNaN6cn0Rtv7IpUh2d2bD341Kz89zF2GPbbILOEQqveryafzFgOaharwfRfRUFuwmaQaQKG95vT51OEJqag2JO0CuMHDAvsbzsJygrbQ0eTvQrvNYUfNyJwl-vepXrpCP_-wl-pUuB9wvh-gNOgW6UAmysEqmqmLEKajqmB8ZeveNGGhds9BQoWWXSMQa4fTR83ffhMsFixsK7rZslGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=uIpJjyrXccwisr8UvOm20cZJGzwiezqCsT8yqzUyELKILg8Tj4SKkUVotvpfpyVQCYTAcFVBfhlTsrfPA3qIahrutdt3_bYOhhjZC5FL8Tpva3Ws15EvpNg2-mG0vbMsmYH61OopmsVuS5h5lVS0E8i5ZMASH3MlOkkzMf2WndsFBxJVZSd4bhaSQQLaBxce0g3xUvkNmuqt2SGMDUSF9_ilDnZ7NR_m1ccUdbTT3UcISwzZ9O0w6h0yMLJIIeC1Fluz9xOCAH8hbyEGZ5Mh7e83GYRpBT5ZnxzIrZ9Q3LWnlC7MHSQrUX0PFDIWvemozcBOqACx1PrKbHN7qMkt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=uIpJjyrXccwisr8UvOm20cZJGzwiezqCsT8yqzUyELKILg8Tj4SKkUVotvpfpyVQCYTAcFVBfhlTsrfPA3qIahrutdt3_bYOhhjZC5FL8Tpva3Ws15EvpNg2-mG0vbMsmYH61OopmsVuS5h5lVS0E8i5ZMASH3MlOkkzMf2WndsFBxJVZSd4bhaSQQLaBxce0g3xUvkNmuqt2SGMDUSF9_ilDnZ7NR_m1ccUdbTT3UcISwzZ9O0w6h0yMLJIIeC1Fluz9xOCAH8hbyEGZ5Mh7e83GYRpBT5ZnxzIrZ9Q3LWnlC7MHSQrUX0PFDIWvemozcBOqACx1PrKbHN7qMkt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoNA6G1en2aKZXvm683guqWLlZIkZhJQ9cgnyhcriKDds5mkag2JrdGNh4jabzRHArFZEUOLVU1lVPozVtiw3AXfOrdbkDbwXzpqvd8d_R8pRIXJc5u8wt9Or48fDePzqx_Kj4_qTfjm82r9Zxynr6614e5bEKNLkbkuFjp1Cz-5Nxa1jpHuDTocCGD4G0wS1brXZZ2-czXrA1hK57JOHqBEuE-Yd0YZsuMDTieii0EGas5bNpitrOYxBtb5XDoe_PY4d0OPd4YZ2Z1yzauQIcl5bMjgIDz0KR9p2cxhpM7Fk1eoRpHbj1U7RT_-atWsd9Q9WBGFvuGFXtlU7woClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmM4JJ92PEaSTQuvluD-OlkNYfYxcfR8PjpfL4vdlCy29fUMDf6f1uMAV8FfLWruNZ10J3QCswv7qI540-yLoGc1jhTeiVXEnOkqRzUx3dYXxRNJfpWdP7YhPRUMaCZOj2uZeu6MQ8fFKy6m_gxRDHkEEiBFv7GgEDtNtCQL1oK044ftRypATsDOK6lV3-WnwPB1b3M-KIehIRVXP7U8_8v2xREdEFPJ0kbrR7n1ftdVq8o9_pYo9PBb8ReDDS1CUMCAM7NiEx9qmuNVHnaNXrXXv1uq86OAVM-rHAze1efSxb0BBowo549SHU8jRxHankc0h7GHLWStg-nTU6rJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7vZBnXKja3Eun2qKU9N_kjXVt1l6hCk6QKu-M_SAeKzMjrhyJIuzXGMuzACO5tFAVyQOpdx-ody1BRQAsU9YGINjuTKVFU9wCqaiBZVIfV8Nc7gb-SHUjsZgqZwi7mBG1VAXyrTDRBZZS_9pujRZAQXMi7WA4d8Zk6D1c_pSM2YInpTAay_0MfAQE-KFlulT2N4PazHkqO9D3Y4v03i7MegVzrdCm3TnVHbFhqwWgObcnpa17znz7VrRhcg7_A6X4YnBA7r9MuSxoEKK-p5Br4HEF-QMJeIJYFxDNFQxEStxo8cM3zrZMwC5sLvwP5sibGw5sDkk-Sd7Ikq6cRYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=aBQtS12krerRgiXDHUWlWiU2BkXM-ONADJrUIcfQzWQc6249T4O9nLZl5hsXffsVkos7pd_mbjNvPdqgV3g0SqZuiETmK-gRt0YxJRy_YK4ShuY0i-o-LVgbwhecV-OVsM32JhK6sA0s5gGDPwVFU6Ec9fngakiUhDtPyp5GdvZIy_Mkgrt4rb3WApcd_N3_7JQ0WpJS1qtL2d6_DiNcCyZn4Qlu0MaZx6YnSlcGhIbHpP47BJsVXYQYh-Z8Io1awvcEx4JQw8wLGzgKh2Y2ojvTeneu8NLenuJD0dXpCe-cJXBXIxPkAkRkDGT3s_r8JFH8tNsQQWmPEMIlGFo9aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=aBQtS12krerRgiXDHUWlWiU2BkXM-ONADJrUIcfQzWQc6249T4O9nLZl5hsXffsVkos7pd_mbjNvPdqgV3g0SqZuiETmK-gRt0YxJRy_YK4ShuY0i-o-LVgbwhecV-OVsM32JhK6sA0s5gGDPwVFU6Ec9fngakiUhDtPyp5GdvZIy_Mkgrt4rb3WApcd_N3_7JQ0WpJS1qtL2d6_DiNcCyZn4Qlu0MaZx6YnSlcGhIbHpP47BJsVXYQYh-Z8Io1awvcEx4JQw8wLGzgKh2Y2ojvTeneu8NLenuJD0dXpCe-cJXBXIxPkAkRkDGT3s_r8JFH8tNsQQWmPEMIlGFo9aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJL-ldMSbd6oazRLDlAXCs3Vav0Q23-pFVGQ8CWeTc-r-o5rFdvt2KgyjdLtxQYi6c5ZSi6yyNY6_jFZfl1L6Log35C7fwDNWXcHhVXwyOPLk8a8YtmILqfSN3mmWNXB73mWw3i4Q0LWL9sdildvYabGSmHpYvCa6W6euEURbzO1Mynt5GK_F53g9Lg2yhfgF3-OWoVkfGdM0r2ugU-0InFGzo2v2uATmbTku4gRDD2cJhI57ifwm9mbktnaHhMTsirX5usH6eOVcjCUsDGmrNfI86USnhYLQa0q0wUtEII55-jJW9znmN7ryJY0Om-NMAmOi5KiwbNb_mLmcIVm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNyhHtLvNgvRs39oCgrmH-wdfE0npSYXYGTI6aohfzZ86qqXFLi2ADUKF-uTS2MAm8cCpHj6L0rz9sI2QEuTOuvbwd7CgquDymUYaUZztMbPjWbxTmo9MnGmESMbUWvNalH5CXJ2lrsyEwttjYL5Q-VveKdCQpjXfPQOtNmrav6N0l6r_V5ZIgkrhJQsFWN-G7FkIae7ziD2W30l9t7Mqly9-AhiTpUPRKXEHNkfnLlxmekaTCBepbveqnFtkmtok-Cy2ftGCkkBPFR19S9dSURdZ3IB556C7CIvtoTDvEPPyO7C06gXCRLu58vo3pF32vhVC3SibGHwFIMlonbghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dpOd59pW_PD4gUi59dRdSdO0W8zUSqy1N8t2SWl78YbANkiuT2e6RvqkZs--zxzfAs6voi98RDwrJU5Bvo4UAXvBbqD3JRLVwx747Jo9BDd8UPTOF3i7_Wrh6_A9lV8k1x_rM3MFsdf01-VIizEJKvcbqKHTlioTW32WrRyg1xClORDtPARgm_C_mbABjF0bL3WSInKeGTTp4oXSCCNYv9hCVGePc6ANn5qPesPb_Bm5rKjKuljEAyekZXzSyiJUgD-NrKII8KtZT5ASqP3I5xm1rpGLF3W_9Euad5TrtU2tsZX-kJOmewVvZL9s09wypkwF2UkcFfHGQwPtmlIN9ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dpOd59pW_PD4gUi59dRdSdO0W8zUSqy1N8t2SWl78YbANkiuT2e6RvqkZs--zxzfAs6voi98RDwrJU5Bvo4UAXvBbqD3JRLVwx747Jo9BDd8UPTOF3i7_Wrh6_A9lV8k1x_rM3MFsdf01-VIizEJKvcbqKHTlioTW32WrRyg1xClORDtPARgm_C_mbABjF0bL3WSInKeGTTp4oXSCCNYv9hCVGePc6ANn5qPesPb_Bm5rKjKuljEAyekZXzSyiJUgD-NrKII8KtZT5ASqP3I5xm1rpGLF3W_9Euad5TrtU2tsZX-kJOmewVvZL9s09wypkwF2UkcFfHGQwPtmlIN9ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaolMRirgKFjkk18GtZWHbZoM9RVGTlvgyeyyUjjdqlw1IgRmg9Ry8s-_3REXqtjhS0SzZr4BNF-ziNhX-C5uw_EQ9s2C6v-2dkViMIpKLffS4XYn6aYcciNJlyMjKFYANMnkhu8wUTcdTv8h5FLhfAhekt03qFb3F6RfgXhKNR-g5meMK59teYKRGAK60LeIcLp55Eg25NBGcO_XyckWWrTCt9uKa6cD0r3Lca-LWnZ9Mjz3obEebE_vVI5IeHoCuh2lfrRJJPbBKEcQ3v_pCe-TeG4FHkzvKwFDEIzf1R5Rta7_ZAH8w7h8DOojIhS_M8uye75Bp_dbcvgEm6n6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=RQ65g2ZAp_LeGoFZeBgtpv9SKCjDOX9JfoJBtV1oiNQtJd6Clw4lQtjd70AQbWcrlNZpdCt6nCCloQiIPIttUlVAtcAcKPWCtpgujL4DfXPoJbk68UzZdMUp6f8-N0mQHOaRdbWr9ZFxV_fiBBgMaKOb-ZeGpaAtwJBS3_2I5qE-8XY2xqXX6GkkylimwMuYAVtGxGRMmYK5PULiA5wA1N1yLjf9ylZp4yiOzYmzFuBRGkcY0IqPR11pN3rLddM_6nmbMOdaMI51ATWjHr-ahGKaCMLDFYDEcnmgGoggBdhMR03A9ODSvc4_DHN8cLQKLiZaefeh-eiTzdiEr8xZ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=RQ65g2ZAp_LeGoFZeBgtpv9SKCjDOX9JfoJBtV1oiNQtJd6Clw4lQtjd70AQbWcrlNZpdCt6nCCloQiIPIttUlVAtcAcKPWCtpgujL4DfXPoJbk68UzZdMUp6f8-N0mQHOaRdbWr9ZFxV_fiBBgMaKOb-ZeGpaAtwJBS3_2I5qE-8XY2xqXX6GkkylimwMuYAVtGxGRMmYK5PULiA5wA1N1yLjf9ylZp4yiOzYmzFuBRGkcY0IqPR11pN3rLddM_6nmbMOdaMI51ATWjHr-ahGKaCMLDFYDEcnmgGoggBdhMR03A9ODSvc4_DHN8cLQKLiZaefeh-eiTzdiEr8xZ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heRYHkRnFc15lo6DwNMFOAl52uHTthd_Zl6lIRyV4O-l1rAhTCWQDVfec4zx_cLtKlQ5hLwdxzV_2oufX5tlKGocd17oKFDg-HuABdjaSI-tobqB7-LqmKWZn237vcTF3Szz4X7RuiR35YuLmo9QlzTy1dIlDY72GOSpWFn2fyrgCFVvjjSpbMS_agPBU0x5qEn7T72hk9Up1BO1BUBZ8wvvUHaIGIWuwkAMscmsuU5F363M4ZYubliIx4njZHCfoWjmU7LVqqitpmpVGxTTkUv5z-rmJgkrrbslWXzaYuZ4a27oc-b1JWqR1DYjVpZdlbwlY_kEJLstY0W8nXKFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNpX8kQdJNQZTS1EUeSdIHIVz_Fgxgcm1hLDMqQRf7N3QUgqi4lQ5sNPK3Nvju5-or7cFqAAllo1_5FDHtFiYlzmNvJ5YRdxxD0WOERwlFd39ouNNhERqyAb9cGFCu6kF2B2pu78vbJ0sfo6amyWqVlJlujlWCO7KggSr9ISKWLReu0qa0zZVj0v8sFRO-sgTz6Qn7elKHfQ2299P0OvhZaf59pcE24-gY8C4LCO0Lq_8KKemvbf_4rfmH7szFEYEo_fPGns2J2NG8c9aIY8de4-ckxVMzvDZRJIcjoIA4ObxTX8PntipAD8V3i1gGqv3mXVpuWUTXpapBoaXJ3nIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpCa-co5KQvuWW8vS75yC-sNv-5U1cVpZPf2eX5zlOqR9xz1oujCUFdKbQh67pQPtNCQBq-P5j9z8U9jSlPwC_WLAhrWuJMObsyAfticuSMchmC13_MQGu_RRc0J-jev1kh_JNjCjm3imVOqGOsv0YarFYFglAR0O2bQCegIQtz19rRHEXxkHUEfwz4JDN8zrvXTQgQbe86JiCBRNnT6b9GKCm80BRWL3IU_Do_mdo-g7zH8SoQHGYAzUn20pAzj3BVJnSHhWJsgYItgRu6O4ntAantuIOpRgDUQWWEyor8995_puATcnj4P81eM9oihCNt-XTN3wnvr6ocvmsMCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKkJvoZrzPRFJcKOj7mUTp0KSsXtXFKaY2E_tSL0PBGGWEbfJ-EmYBytUUr0v1OKcnyWfsjkvOb47TYKodZYiKW0t07VjrSAZa1d4uBAqk-VSqeS7RzRn8s-1H6wZxxb_zBaoXrWlqH0q7YJhYGW56g1nLvoKR1hwQqgQbwEJPDiS6IYDocvRuPwVrhXNHgk85bNRj2EMd667GfMSiBG3GoyHRQqgF_LsPvhotcogUDVQsuiWoI2x1zt5B5ui8ZrTJZjGDiOsBctXH9gGWc9Pl1pfZeSjISj0yiM10U5JEdtbwmZBtkvAJrBxirppwYjrTu9lNOjbGGygPCS896a0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=eqzYPa2Igg5OGkux6d4dTuj49hiH7fviRTN-x4iCSly9z7fGPTdBTDgaoFYc4tIy4GJmQ38zv-ngjk8Ahu-TC1heNzBK4vapYKhJSxfsjAPau7A25ItlPitVr4nTh7pHhWDWkNXToYgUD568F6DdSzM0U258NuH6g5ekMEIkkwBQm9Vmw8fkc8Be_P_OYsJPpyLXG73xL3SzencrDj-OuwScIbXFeZMcxNwunQTLiOCk8p6wn52LFfE61pf7yVa0Fkqe1O-wbp03gVIliNsPLWQN_k81hyX77TyeoIwCbOUmsvgDumAEGUqZtCvH6M1jbWCFpBmZdr9KtkpTc2VhLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=eqzYPa2Igg5OGkux6d4dTuj49hiH7fviRTN-x4iCSly9z7fGPTdBTDgaoFYc4tIy4GJmQ38zv-ngjk8Ahu-TC1heNzBK4vapYKhJSxfsjAPau7A25ItlPitVr4nTh7pHhWDWkNXToYgUD568F6DdSzM0U258NuH6g5ekMEIkkwBQm9Vmw8fkc8Be_P_OYsJPpyLXG73xL3SzencrDj-OuwScIbXFeZMcxNwunQTLiOCk8p6wn52LFfE61pf7yVa0Fkqe1O-wbp03gVIliNsPLWQN_k81hyX77TyeoIwCbOUmsvgDumAEGUqZtCvH6M1jbWCFpBmZdr9KtkpTc2VhLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6t0AnGkx3TCuF__wWF571mQc3SaCR-FA65ktWWN3dzJq_kqCOwsnlHsAoXUcefVvqH_MMq0V9yMS3csJ2i2rM88rDzIc8hPzLO-Y2MgUTcCtoHr_o1gl2pKnsQ0TLUxsNmscpKVQ5UWQdZdtJX71EkctiEtEfGIkV3GG-nAr2dlppUR_BPIlW93qZjGD0SANSpW5pOD8Ge_rLXb83Om7s5blgx09Jv0D92qnJK9rWKq9GKPl3BYf8DJeyNid73vw2D5HXkGbyuF7fBRYGsClXV4TAXVR7sJLrCmZduRi0-z04P6aZrBPDMZJ4dErR5vY2wYc3sVdN_4AFiVHTr3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین
پس از آغاز نخستین محاصره بنادر ایران در
۱۳ آوریل
، حمل‌ونقل ریلی کالا از
شی‌آن چین به تهران
افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر
سه تا چهار روز
رسیده است.
این مسیر ریلی پیش از آغاز بحران نیز فعال بود.
نخستین قطار باری مستقیم از شی‌آن در
۲۵ مه ۲۰۲۵
در بندر خشک
آپِرین (Aprin)
در نزدیکی تهران تخلیه بار کرد. بنابراین، مسیر مذکور پیش از اعمال فشارهای دریایی ایجاد شده بود.
مسیر قطار از
قزاقستان و ترکمنستان
عبور می‌کند و سپس وارد ایران می‌شود و به آپرین می‌رسد. در این مرکز، محموله‌ها ترخیص شده و برای توزیع در سراسر کشور ارسال می‌شوند. حمل بار از این مسیر ریلی حدود
۱۳ تا ۱۶ روز
زمان می‌برد، در حالی که حمل دریایی در شرایط عادی حدود
۳۰ تا ۴۵ روز
طول می‌کشد.
افزایش تقاضا برای این مسیر هزینه حمل را نیز بالا برده است. قیمت حمل یک کانتینر ۴۰ فوتی در ماه مه به حدود
۷ هزار دلار
رسید که تقریباً ۴۰ درصد بیشتر از سطح معمول بود.
هر قطار حدود
۵۰ کانتینر
حمل می‌کند. محموله‌ها عمدتاً شامل قطعات خودرو، ژنراتورها، تجهیزات الکترونیکی و سایر کالاهای صنعتی و مصرفی هستند. قطارهای برگشتی که با ظرفیت پایین حرکت می‌کنند نیز هزینه حمل در مسیر غرب را افزایش می‌دهند.
بااین‌حال، ظرفیت ریلی قابل مقایسه با تجارت دریایی نیست. یک کشتی کانتینری بزرگ می‌تواند هزاران کانتینر حمل کند و انتقال نفت خام یا سایر محموله‌های فله‌ای در مسافت حدود
۱۰٬۴۰۰ کیلومتر
از طریق راه‌آهن از نظر اقتصادی مقرون‌به‌صرفه نیست.
در نتیجه، این کریدور ریلی نمی‌تواند تجارت نفت ایران پیش از محاصره را احیا کند یا جایگزین دسترسی آزاد به بنادر شود.
پس از آنکه آمریکا نخستین محاصره را در
۱۸ ژوئن
لغو کرد، این محاصره در
۱۴ ژوئیه
دوباره برقرار شد و اهمیت مسیر ریلی به‌عنوان یک کانال جایگزین افزایش یافت.
ایران همچنین از مسیرهای زمینی و ریلی دیگری استفاده می‌کند. خطوط ریلی در شمال به سمت
روسیه
امتداد دارند و گذرگاه‌های زمینی در شرق نیز امکان ارتباط با
پاکستان
را فراهم می‌کنند.
هیچ‌یک از این مسیرها از نظر حجم قابل مقایسه با حمل‌ونقل دریایی از طریق خلیج فارس نیستند، اما امکان انتقال بخشی از کالاهای مورد نیاز ایران از طریق مسیرهای زمینی و ریلی را فراهم می‌کنند
.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20142" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
