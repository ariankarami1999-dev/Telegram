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
<img src="https://cdn4.telesco.pe/file/ert6_YE3kBdM4QtsN4LKZm_yk1oNA-4dNHPGCsHm6HQmctNAlmBY187k-OkFnuD7th7a_thslCE2P4KUptv4RribOhV2gOaEyYE18aqoEglQSy6W4LjKymEHwi1AlYitHGU6fX1RK0J368YiyarDYve_jVFvbEeCOCit3e_AlI8SUWYsooQW9A2GJOwQld0PvTE9D39K8x1Hj_IJgi_BuaMU5Pe3ieR_diTEgBcUfulHC__UQ663eEG2eNL6eotJY8WzJ_-gjJ4JSxkl6TjReSPLyjxy45z8BrT3M9S4P73gqVFVh3rNA0weQrpWH08oLigdFd13t0OvE60Mtwm-Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 16:44:49</div>
<hr>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حمله پریشب به انزلی به نظرم بیش از آنکه یک محموله نظامی از روسیه را هدف گرفته باشد، از جنس حمله به تاسیسات راه آهن در استانهای خراسان رضوی و گلستان بوده و پیام تشدید محاصره و کور کردن بقیه کریدورهای حیاتی کشور را داشته است.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/19228" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اوکراین پالایشگاه نفت "تیومن" در روسیه را مورد حمله قرار داد. این پالایشگاه بیش از 2000 کیلومتر از مرز فاصله دارد.
استاندار این منطقه تأیید کرد که یک پهپاد به این تاسیسات اصابت کرده و باعث ایجاد آتش‌سوزی شده است.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/19227" target="_blank">📅 13:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19226" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNn025mKJMKDhf18DVn6HX7pPQ4J4408iQhoFU6ETssVGmqgoBm_ZyAHqpYdUj49BggrpqZ1RYRqaIQpGFX4HcydKcItbu9HOk16zw8oWXfwSYxXaaXAu9UOWD28vQDpYM2EytAkuk11fUHOrHzLiG8RVdAeg0fPi20eddXD-MdDbA3ZG-JIwHPjYpp3g1b6y466qVifOfytVOmzmw7fKtwJrlyFxfkj7kuFwZwirMNo2JgVtfoD7ZjoSwrjZMh3PXF2_zSRdD_eE2PS42UBOWp85TJvwVFU8Pg7pH2zcMdih8qTacTC3Wd4VAxq2ReJ4Q9YR1MBRpClmCU0Rff2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان سوم جایی است که در آن برای یک سری بوزینه دستمال کش بی عرضه برای راه یافتن به جام جهانی که 48 تیم دنیا در آن حضور داشته اند جایزه 350 میلیارد تومانی می دهند اما برای نخبگان علمی اش هیچ!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/19225" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/19224" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان  مدیرکل مدیریت بحران استانداری اصفهان:  از ساعت ۹:۳۰ صبح امروز عملیات کنترل‌شده معدوم‌سازی مهمات عمل‌نکرده متعلق به جنگ رمضان توسط تیم‌های فنی و تخصصی ذی‌ربط آغاز شده است.  محدوده اجرای این انهدام کنترل‌شده، مناطق…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19223" target="_blank">📅 10:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19222" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">منابع اسراییلی:   بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.  تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19221" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اگر این خبر درست باشد و اهداف نظامی ایران توسط کویت و بحرین که ضعیفترین ارتشهای عربی منطقه هستند هدف قرار گرفته باشند، یعنی اینکه عربهای جنوب خلیج فارس با راحتی بیشتری می‌توانند تاسیسات زیربنایی و غیرنظامی ایران را نابود کنند و اگر تا کنون چنین نکرده اند ناشی…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19220" target="_blank">📅 10:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">استانداری گیلان اعلام کرد   صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19219" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند  به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19218" target="_blank">📅 09:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19217" target="_blank">📅 09:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19216" target="_blank">📅 09:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19215" target="_blank">📅 09:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19214">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فرماندهی سنتکام ایالات متحده اعلام کرد که یک کشتی تجاری دیگر را که بارها تلاش کرده بود از محاصره بنادر ایران عبور کند، غیرفعال کرده است. این دومین کشتی تجاری است که از زمان بازگشت مجدد محاصره، متوقف شده است.
منبع: خبرگزاری آسوشیتدپرس (AP)</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19214" target="_blank">📅 01:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19213">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این یادداشت را دوباره بخوانید.  یک روند ضدتورمی عجیبی در حال شکل گیری است که طلا، بیتکوین، سهام، مسکن و ... را همه با هم نابود خواهدکرد. به نظرم اساساً پول عوض خواهدشد و آنچه بستر ارزش خواهدبود توان «جلب توجه» و تاثیرگذاری بر اذهان خواهدبود.  همان که آخوندها…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19213" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19212">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWpdn1CgYUhwLQEJzKEk5eI8HIKgdLfiKk0GWhHa2Y2WW83lU0p-eGWBoAiqAC7aCuAF-S9hc3TH_c2cj_z1vPMNY2wlnJ_ZGX-lMtytDDgGtv-gBClC1uYupe2MUMcpwr7whADTMmrJpHI1aY5Z74xtyTiwz3keJR7Zk7PiqBF8BOo0NKBAERe2I6mJIpqjlQy-HCrdnQAAx_5YVjFdYIriKucnRJbvF-erJDPCyZw89xJOvde4Aa_UR16xqRbGPAetYdu4Uhh3pgiZmqP4m6qISkxn5UEDFg2cwqAJJKI1a55Te5tvykYka4egDM_VnUhi4NRh1OLBgt4vj8bBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.  محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19212" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
یمن (منظور یمن تحت کنترل حوثی ها): حماقت عربستان تاوان سنگینی خواهد داشت
وزارت امور خارجۀ یمن: ما رژیم عربستان سعودی را مسئول تمام پیامدها و تحولات ناشی از این اقدام جنایت‌کارانه می‌دانیم.
رژیم سعودی به‌جای تسلیم در برابر مطالبۀ حق و عادلانه برای رفع محاصرۀ یمن، مرتکب حماقت بزرگی شد که هزینۀ زیادی برای آن درپی خواهد داشت.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19211" target="_blank">📅 01:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19210" target="_blank">📅 01:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLve_kS-ITC-Knk5G8bg_3bcTqPugXZ-4s0dvRJLmi93WK6XHfpuLCopW31oSaXVyJqIzxLjGt9IRdsl3G1SBCh_qRz3nkgTkDVjAqmLY89vtiQoi0f7GPQ4Nb3E_eO-belWF42DOddgidY3148gSyb4cI3uVCkkIcRiLCVKsTuYbS5uhtbZh9wMliX4e4vXrj7NCt2Ilolj4-_9bdik-FHW0dB9SmLzkAekjwDC_UoSFsaC9lZcbt-N2mIELqyJjN_AOXwkTop4fGWvMRH-8H1RbLlWUccbeHhJO8qWtvcSLezl0bSxozu5EGv72VRn9AUOdgTuyFTVQEeMnbv_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان آتش‌بس ایران؛ ضربه‌ای مهلک به سرمایه سیاسی جی‌دی ونس   تا پیش از فروپاشی آتش‌بس میان ایران و آمریکا، جی‌دی ونس یکی از مهم‌ترین برگ‌های برنده خود برای رقابت‌های درون‌حزبی جمهوری‌خواهان در سال ۲۰۲۸ را در اختیار داشت؛ این ادعا که توانسته است در کنار دونالد…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19209" target="_blank">📅 00:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">308 KB</div>
</div>
<a href="https://t.me/SBoxxx/19208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 12</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19208" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمله عربستان به شهر الحدیده یمن</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19207" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارشگر: می‌گویید که با ایران در حال گفتگو هستید. چه کسانی درگیر هستند؟ ویتکوف؟
ترامپ: تقریباً همه. جی‌دی، مارکو - افراد زیادی در حال گفتگو هستند. این یک مسئله بزرگ است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19206" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند
به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته شده آن‌ها علیه جمهوری اسلامی بود.
بر اساس این گزارش، حملات به تأسیساتی که برای ذخیره پهپادها و موشک‌ها استفاده می‌شدند و همچنین سایر تأسیسات نظامی متمرکز بودند.
امارات متحده عربی که پیش از این در مراحل اولیه درگیری چندین حمله به ایران انجام داده بود، به گفته ژورنال، اطلاعاتی درباره اهداف بالقوه ارائه کرد و پشتیبانی هوایی دفاعی فراهم نمود؛ این گزارش تأکید می‌کند که این اقدام نشان‌دهنده هماهنگی فزاینده میان کشورهای عربی علیه جمهوری اسلامی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/19205" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیویورک تایمز:
بر اساس ارزیابی نهادهای اطلاعاتی آمریکا، (آیت الله) مجتبی خامنه‌ای، رهبر جدید ایران، برخلاف پدر علاقه و تمایل بسیار بیشتری به دنبال کردن دستیابی به سلاح هسته‌ای دارد.
این موضوع را مقام‌های آگاه از این ارزیابی‌ها به نیویورک تایمز اعلام کرده‌اند</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19204" target="_blank">📅 22:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در 'حالت انتقام' و خسته از جنگ با ایران
به گفته یک مقام آمریکایی ، رئیس‌جمهور ایالات متحده تلاش‌های دیپلماتیک برای حل درگیری پنج‌ماهه در ایران را کنار گذاشته و طبق گفته مقامات، وارد «حالت انتقام» علیه تهران شده است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19203" target="_blank">📅 18:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به گفته سه منبع پاکستانی، پاکستان در پی تلاش چین، در حال بررسی از سرگیری مذاکرات متوقف شده آمریکا و ایران برای پایان دادن به جنگ تقریباً پنج ماهه خود است.  به گفته منابع، مذاکرات مقدماتی در جریان سفر این هفته اسکندر مومنی، وزیر کشور ایران، به اسلام آباد، که…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/19202" target="_blank">📅 18:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گفته سه منبع پاکستانی، پاکستان در پی تلاش چین، در حال بررسی از سرگیری مذاکرات متوقف شده آمریکا و ایران برای پایان دادن به جنگ تقریباً پنج ماهه خود است.
به گفته منابع، مذاکرات مقدماتی در جریان سفر این هفته اسکندر مومنی، وزیر کشور ایران، به اسلام آباد، که دومین سفر او در ده روز گذشته است، انجام شد.</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SBoxxx/19201" target="_blank">📅 18:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: چین و پوتین گفتند که سلاح به ایران نمی‌فروشند</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19200" target="_blank">📅 18:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت امور خارجه آمریکا: وظایف مرزی و گمرکی درمسیر TRIPP  تحت کنترل ارمنستان باقی خواهد ماند.   وزارت امور خارجه ایالات متحده در مورد مقررات اتحادیه اقتصادی اوراسیا در مسیر TRIPP اعلام کرد، تمام وظایف امنیتی مرزی و گمرکی تحت کنترل ارمنستان باقی خواهد ماند.…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19199" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بنیامین نتانیاهو روز سه‌شنبه با رئیس‌جمهور ترامپ برای ارائه لیست خواسته‌ها و انتظارات خود از آمریکا دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19198" target="_blank">📅 17:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بنیامین نتانیاهو روز سه‌شنبه با رئیس‌جمهور ترامپ برای ارائه لیست خواسته‌ها و انتظارات خود از آمریکا دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19197" target="_blank">📅 17:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «ما به عموم مردم کشورهایی که پرسنل نظامی ایالات متحده در آنها مستقر هستند هشدار می‌دهیم که فوراً از مناطقی که در شعاع ۵۰۰ متری از مکان‌هایی که پرسنل نظامی ایالات متحده، چه به صورت آشکار و چه به صورت پنهان، مستقر هستند، قرار دارند،…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19196" target="_blank">📅 15:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«ما به عموم مردم کشورهایی که پرسنل نظامی ایالات متحده در آنها مستقر هستند هشدار می‌دهیم که فوراً از مناطقی که در شعاع ۵۰۰ متری از مکان‌هایی که پرسنل نظامی ایالات متحده، چه به صورت آشکار و چه به صورت پنهان، مستقر هستند، قرار دارند، دور شوند تا امنیت خود را تضمین کنند.»</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19195" target="_blank">📅 15:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19194">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 12</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 12
جمعه 24 جولای 2026</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19194" target="_blank">📅 13:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19193">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL61qMOIZJ4Xw92HbDAZl-8OLYorwYue-I46CH5v4itIItqjQ38Pb-7JT-bbEz9dp2I07ePPi6I53a9B3tVRPeI8_9DrlMQzJuV479t4RbS6PA-9QTrhwflFJl8QII4_TLt_rCEt_8z2ky5Y6V4nMfrCzMkkCrQ3DaL_OvMjnCwB7p657BRtudE7NXlj7LsbQNJQa6DQbzc8P9U0ywyA4dpl7S6Zer6oLnbSFuFRpvOK6-6RvFySHVqOyrtmtiZFyLdJehoQASUJ1pFg1cCIU2XliwDEoqEYiZmGEqxL6UocFyI_xyejudvThiFyew3g0ZEphYxxXDYOocwJpaky1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.
محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19193" target="_blank">📅 12:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19192">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارت امور خارجه آمریکا اعلام کرد که تحویل جنگنده‌های اف-35 به ترکیه انجام نخواهد شد، زیرا شرایط مربوط به سیستم دفاع هوایی اس-400 برآورده نشده است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19192" target="_blank">📅 11:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19191">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگر شانتاژ اسراییلی ها برای بر هم زدن ماه عسل ترامپ با اردوغان نباشد، معنی اش این است که ترک‌ها حاضر هستند از اف-۳۵ چشم بپوشند اما شاهد سرنگونی جمهوری اسلامی نباشند.  به نظر در این صورت، تنش‌هایی در دریای اژه خواهیم داشت.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/19191" target="_blank">📅 11:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19190">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بوی آغاز حملات اسراییل می آید.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19190" target="_blank">📅 11:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19189">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">استانداری گیلان اعلام کرد
صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19189" target="_blank">📅 11:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19188">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملهٔ هوایی به پیرانشهر  مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.  در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19188" target="_blank">📅 11:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19187">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملهٔ هوایی به پیرانشهر
مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.
در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19187" target="_blank">📅 11:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19186">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frArMvJAieJYv_0Ka2USoJdRIXbaFe55vEqnUKfPHbFudQjMX4SzKuI4w6CoseosS9NxEpqxKxuBnAw9DfPVwPqpoLZJeaKkxKr9DHxgIKfHyjvDBfaGxNC8PHuXYJ6OgKJrwdnKDGr3QTCcxJkJYQSH-_Fb3etyRxlStZp-56sKY7CYSTZ8xRBbSdPidcBxcJkwXMSniFj39PKPNFW3WoPDHcDbIW_-xVi9uQjPwOmFG57kIYA6zxTmg7fj44o208NmLiFusCU2ZIfpKaiSrlpWwEjXmfn3RXSpuTRv9geHCH9zzh59DC6uaBlUSpg5411RIN2dnXsUIc3r_8rfsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز کماکان بالا است اما از دیروز خیلی پایین تر آمده.  به نظر می رسد طلا یک اصلاح صعودی رو به بالا داشته باشد (بعد از ریزش 700 پیپی از سقف دیروز)</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19186" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19185">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc2d5ac32.mp4?token=gh5StZ_H6bQiH4v5I1wt948MqL9Uws_4f0lnbh_sX3aGnNoSKttLI5jXX0y2DyI_ym7oogfT96HXJF8gYMpYYpA3u1Pl78EPuAkVpRrkx6X-aU-vBK2oDRG-mTp8WR0NZzOd0LEeD9CV_8tNNsnl7ddBxYYhe2uecLsrx0fvhuLWyeuoyeH4aryNX2w4tqe9QfIS-AAWbP6YIBkJdH-MiWvDz25VbTz0cxqHRo2ePaiygzzEsc9OevBivvI1EyIvBXtD2FiZaA5LYuasxBhJ2qC_KPhoMsfEZXpgJnrnl17fngH2QB0bhU0_VC2s-9MnyBH8U4xI2XarbiEvlnY32A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc2d5ac32.mp4?token=gh5StZ_H6bQiH4v5I1wt948MqL9Uws_4f0lnbh_sX3aGnNoSKttLI5jXX0y2DyI_ym7oogfT96HXJF8gYMpYYpA3u1Pl78EPuAkVpRrkx6X-aU-vBK2oDRG-mTp8WR0NZzOd0LEeD9CV_8tNNsnl7ddBxYYhe2uecLsrx0fvhuLWyeuoyeH4aryNX2w4tqe9QfIS-AAWbP6YIBkJdH-MiWvDz25VbTz0cxqHRo2ePaiygzzEsc9OevBivvI1EyIvBXtD2FiZaA5LYuasxBhJ2qC_KPhoMsfEZXpgJnrnl17fngH2QB0bhU0_VC2s-9MnyBH8U4xI2XarbiEvlnY32A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کویتی میگوید از بس صدای آژیر خطر به صدا درآمده، پرنده اش مداوماً این صدا را تقلید می کند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19185" target="_blank">📅 10:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19184">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادامه حملات ایران به بحرین و اردن</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19184" target="_blank">📅 09:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19183">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c330773d3a.mp4?token=NblBmh1-LhhISGLL8QUIdkiciTMDQngENYmXnUSiyHsWYcNQUvf2p3up0ld8K5zi7t7spNPTjkO3oYeR-16F9i6qLbLLIzVQu7obBIKq9HZojRJEcEOLSdQryHrKIp7JvRYWyr2v7e5zUgXiJjK8_qS5MFulCrojdKkwlfHwfE_4MYOfdjf3akIqvIztsxFRCG1LgJZFEZ-Mf-y4s_rDUcUDzlpI4n-omZLJ7jq8K9fwP4KkBZWt18ehEOcRJ4dM_65_bbl-qusHlGokOoEa1qHxz3OeqOSxw48UYz92IhxuA60ZFzXdDyMV95kld6ZPk8SZFsB6sE9--iCMUpP9dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c330773d3a.mp4?token=NblBmh1-LhhISGLL8QUIdkiciTMDQngENYmXnUSiyHsWYcNQUvf2p3up0ld8K5zi7t7spNPTjkO3oYeR-16F9i6qLbLLIzVQu7obBIKq9HZojRJEcEOLSdQryHrKIp7JvRYWyr2v7e5zUgXiJjK8_qS5MFulCrojdKkwlfHwfE_4MYOfdjf3akIqvIztsxFRCG1LgJZFEZ-Mf-y4s_rDUcUDzlpI4n-omZLJ7jq8K9fwP4KkBZWt18ehEOcRJ4dM_65_bbl-qusHlGokOoEa1qHxz3OeqOSxw48UYz92IhxuA60ZFzXdDyMV95kld6ZPk8SZFsB6sE9--iCMUpP9dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تکه از فیلم «فریاد مجاهد» ساخته شده در اوایل انقلاب که مثلا میخواسته با دیالوگ ماموران فحاش ساواک و چند تن از مجاهدین اسیر، مظلومیت عنترهای مجاهدین خلق را به تصویر بکشد اما رسما به مایه انبساط خاطر بیننده تبدیل می شود و آرمان‌های اصیل سه خر بنیانگذار مجاهدین را به تمسخر می‌گیرد!
خطر ترکیدن روده ها از شدت خنده وجود دارد.
#تاریخ</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19183" target="_blank">📅 09:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19182">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ:   از این به بعد، خسارات وارد شده به کشتی‌ها، بارها یا اموال مرتبط از پول‌های ایرانی که در اختیار و کنترل ایالات متحده است، پرداخت خواهد شد.   خسارات ممکن است قابل توجه باشد، اما این امر عادلانه و منصفانه است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19182" target="_blank">📅 09:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19181">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19181" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19180">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۴ کشته و ۵ زخمی در حمله موشکی ‌آمریکا به اطراف شهر اهواز
استانداری خوزستان: پس از حمله موشکی دشمن آمریکایی به نقاطی در اطراف شهر اهواز ۴ نفر از هموطنانمان شهید و ۵ نفر دیگر مجروح‌ شدند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19180" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19179">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDdW2gjZn4yjZzUAGjoULNYi2uDUO70JScbMAXXnmKVWNCj6KiVjQjitYTG1BlJBwc7Z0QQtmtcAVACWaK0XfkibgE2WYkSAHl1W_3fTctucpHMXQLZMoU1gve576usWtetgmliaIA_Z99XDhTVvIGkKkBwu3zize-6u6WqLIpZzDirYufbmO0RDeXOjc6vwVFV0w7ZgyuONYlq4bT148Tr3BSBBXT4bujAkfDWTd7v43lj_SiMxWjdyendWTiverzWd-Zr29wzGWIONffINqfax6GG6bOe4LygteiCV3rejHEzh2RMDbXwb_adMMKzXZilEU9dA9qGRHou1wV8RdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست :
«دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19179" target="_blank">📅 09:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19178">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گفته می شود یک هواگرد آمریکایی (هواپیما یا پهپاد) بر فراز جزیره قشم سرنگون شده است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19178" target="_blank">📅 02:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19177">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خوشبختانه در کشور خودمان به دلیل تدابیر داهیانه سازمان بورص، میزان ارزشی که از سهام ما کم شده حتی نصف 1 تریلیون دلار هم نیست.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19177" target="_blank">📅 01:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وال استریت ژورنال :   بازار بورس وال استریت آمریکا بیش از 1 تریلیون دلار در ساعات اخیر ریزش کرد به دلیل جنگ تمام عیار احتمالی در خاورمیانه.   #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19176" target="_blank">📅 01:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19175">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال استریت ژورنال :
بازار بورس وال استریت آمریکا بیش از 1 تریلیون دلار در ساعات اخیر ریزش کرد به دلیل جنگ تمام عیار احتمالی در خاورمیانه.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/19175" target="_blank">📅 01:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19174">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0be177031.mp4?token=ugdneWnA3XRaRejUuxuk5o5yPGZpm9LTiqVVmIqUPqgH01Mn6h5XxqqE4iLkZFAbqt5BJLagXNJdjKaJjKzdoCsv1yfJzxx3XzM0xgVTuyPkU3tGDIqEwV2hQ5xidv6v4DPlxLDo4Sz53q3rEjfo_Mrsq1d2EYvoQTZYCjK8HUal1El4x39I9bTByW-74BPVuySpcbrcicfIkV8RM9RfFKplAu8NUkM-dAXyRNTEfZmWSV-avYlpxO79o-SkV-HVo0t_dbTGI0rp0k5mZa1LYrfVikqrGunEuEMsOGz54FEjYizMVKc8PEjKzWa4IgT4iieasif1DGfIOzHuewXdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0be177031.mp4?token=ugdneWnA3XRaRejUuxuk5o5yPGZpm9LTiqVVmIqUPqgH01Mn6h5XxqqE4iLkZFAbqt5BJLagXNJdjKaJjKzdoCsv1yfJzxx3XzM0xgVTuyPkU3tGDIqEwV2hQ5xidv6v4DPlxLDo4Sz53q3rEjfo_Mrsq1d2EYvoQTZYCjK8HUal1El4x39I9bTByW-74BPVuySpcbrcicfIkV8RM9RfFKplAu8NUkM-dAXyRNTEfZmWSV-avYlpxO79o-SkV-HVo0t_dbTGI0rp0k5mZa1LYrfVikqrGunEuEMsOGz54FEjYizMVKc8PEjKzWa4IgT4iieasif1DGfIOzHuewXdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژدهای بندر تک تیرانداز می شود!
راستی می دانستید از تنب بزرگ می شود همه کشتی های جهان را دید؟!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/19174" target="_blank">📅 00:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19173">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصاحبه مایک هاکبی سفیر آمریکا در اسراییل با تاکر کارلسون درباره حق الهی اسراییل در تصرف و کنترل خاورمیانه.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19173" target="_blank">📅 00:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19172">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چقدر حس خوبی هم داشته یارو که ۴+۵ را درست جواب داده !</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19172" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19171">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب اسکل جواب سوال دوم را میگفتی مثلا ۱۳!  ما هم خب ۱۰ خط لوله داشتیم و مخ آنها هم مثل مغز خودت میگوزید</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19171" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19170">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔥
خاطره عجیب اوجی از تماس موساد به او!
🔹
جواد اوجی وزیر سابق نفت: ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
🔹
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19170" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c687c4b9c.mp4?token=FNK7A-_FUHAP5KQ5wFnSxDxcBvVXabd9h4yvsS-AZSDd_42PtlygTr7NTusfzHlcU0HJtk7QOTaCq6Kh4VJSInkXyOvbiYSt17fbVTzwppkFlPk_tpgojUYdACpmzWz4NaTKmKn4hr1P9eASwxvgKPAdE8a_OGUaTojfA6q3oHXTaHnhLzgC63M1SgLxT2_iBVM_faEfefC0Jsng3iylD0l_adVUCfahv8pxhDMtyU6i4MzR-RyOUV3wBgDOejUM0KxxKjU5x3gkAURC_t1jB7vg9HjntJLkSO4RmnJVZexLCcoK-c6P-s7Oh7TzCaTDUtgBGu-OyLiAWw5BwfcpHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c687c4b9c.mp4?token=FNK7A-_FUHAP5KQ5wFnSxDxcBvVXabd9h4yvsS-AZSDd_42PtlygTr7NTusfzHlcU0HJtk7QOTaCq6Kh4VJSInkXyOvbiYSt17fbVTzwppkFlPk_tpgojUYdACpmzWz4NaTKmKn4hr1P9eASwxvgKPAdE8a_OGUaTojfA6q3oHXTaHnhLzgC63M1SgLxT2_iBVM_faEfefC0Jsng3iylD0l_adVUCfahv8pxhDMtyU6i4MzR-RyOUV3wBgDOejUM0KxxKjU5x3gkAURC_t1jB7vg9HjntJLkSO4RmnJVZexLCcoK-c6P-s7Oh7TzCaTDUtgBGu-OyLiAWw5BwfcpHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
خاطره عجیب اوجی از تماس موساد به او!
🔹
جواد اوجی وزیر سابق نفت: ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
🔹
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
🔹
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@khate_energy</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/19169" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwqbPzKcatYqRZUvq4G6v_l1eg1qcHBZgWsvcpB7QiEj6L-05WWc5M5F3iVFS5tQ4M0qbWiJc3deWI5ERWUinNUIAhsQ9EXm-zVVBFE-eBla7J5wtasLSbSB7vs3HxgPeAI_xTz7wvOQhcvDxLt_bNDjtZZ4CydBgAA9AO_swwRMHaMu7zw11bpuGqKwgbXCJHXiAxdHzFu5Ft9BcO2yr9q_oB472eB225-6X-MVTB7Z--RxpPTNNKiHxH0vgKAe4y0bogCwCWoV09dEy3wLqF8KkjnkwpsZviZgKwDAnEyhvhVPWkB875jrETE-QJmsfUZpxEs2oQv9g3D0ZwJLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این حجمی که سوخت رسان های آمریکایی سمت ما می آیند فکر میکنم محتاج دعای خیر نیاکان باشیم.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/19168" target="_blank">📅 21:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کارخانه‌های پالایش نفت چین، نفت روسیه را خریداری می‌کنند  خبرگزاری رویترز گزارش می‌دهد که در بحبوحه بسته شدن مجدد تنگه هرمز و تهدیدهای حوثی‌ها در مورد ایجاد یک محاصره دریایی برای عربستان سعودی، چین به طور قابل توجهی حجم خرید نفت خود از روسیه را افزایش داده…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19167" target="_blank">📅 21:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVt3vNmKYbffGVyLeGTkfNs8BhDQJDmDxeHvvF_eY0B1rcHhqQ5AmcKL45Dtb_wO5WhqrBDkXs9I5l2CLGYX4IoEiDDcGeDhlj05LEQDflww8zSeQJ6wM5V9Bz1Z7PI7f9Mfj0Yc7KgfFnV_wtCZEAnW_p1vTmfnnkzJxLW6yirzUujkS3VK8IdAP8pVlfrsn6MGoz0kJrCe9XRIdKFH7qBahw31TccDd4dKo47L2_ErNid1pFeMZwzoyQJRbeKP6Tun_f_4vNG_uu_A5Xzj9im9G2_Yr7JrqSXxJ7dZVLY-USyjM6lsaKC2ioU5koTp8OGcoKpfOMPEOOSpvHztIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارخانه‌های پالایش نفت چین، نفت روسیه را خریداری می‌کنند
خبرگزاری رویترز گزارش می‌دهد که در بحبوحه بسته شدن مجدد تنگه هرمز و تهدیدهای حوثی‌ها در مورد ایجاد یک محاصره دریایی برای عربستان سعودی، چین به طور قابل توجهی حجم خرید نفت خود از روسیه را افزایش داده است:
«با توجه به اختلالات در عرضه، کارخانه‌های پالایش نفت چین در هفته‌های اخیر به طور فعال نفت را از بزرگترین تامین‌کننده خود، یعنی روسیه، خریداری کرده‌اند و همچنین مذاکرات خود را برای خرید نفت ایران از سر گرفته‌اند.»
نویسندگان این مقاله همچنین اشاره می‌کنند که دو شرکت بزرگ پالایش نفت چین، بخش قابل توجهی از نفت خام روسی با نام ESPO Blend را برای حمل در ماه سپتامبر از بندر کوزمینو خریداری کرده‌اند. به گفته یکی از مسئولان یکی از کارخانه‌های پالایش نفت چین، نفت روسیه در حال حاضر به عنوان قابل اعتمادترین گزینه برای تامین در نظر گرفته می‌شود.
«با توجه به عدم قطعیت در خاورمیانه، ESPO به نظر می‌رسد گزینه امن‌تری باشد. علاوه بر این، قیمت آن نیز ارزان‌تر است.»
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19166" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">منابع اسراییلی:
بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.
تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19165" target="_blank">📅 20:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">محاصره حوثی ها ضد عربستان سعودی می‌تواند ماهانه تا ۷ میلیارد دلار هزینه بر ریاض تحمیل کند
دیروز گزارش‌هایی ظاهر شد که «حدود ۲۰ سوپرتانکر بارگیری شده با نفت عربستان سعودی در دریای سرخ گیر افتاده‌اند.» این نتیجه محاصره‌ای است که حوثیان یمن اخیراً علیه تمام کشتی‌هایی که به هر نحوی به عربستان سعودی مرتبط هستند اعلام کرده‌اند.
آن کشتی‌ها دیگر نمی‌توانند بدون خطر حملات از سواحل یمن، به‌طور ایمن از تنگه باب‌المندب عبور کنند.
در درجه اول، این موضوع بر حملات نفت خام و محصولات نفتی تأثیر می‌گذارد.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19164" target="_blank">📅 20:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گویا سپاه یک کشتی را در تنگه هرمز زده است</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19163" target="_blank">📅 20:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:  یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.  ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19162" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19161">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو فردا بعدازظهر جلسه‌ای با موضوع «تصمیمات امنیتی» ریاست خواهد کرد.
به احتمال زیاد این موضوع به ایران مربوط است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19161" target="_blank">📅 19:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19160">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شلیک موشک از ایران</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19160" target="_blank">📅 19:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درباره ایران:  من در حال بررسی یک حمله عظیم هستم؛ بزرگتر از هر چیزی که تاکنون رخ داده است.  من نزدیک به اتخاذ این تصمیم هستم.  منبع: N12</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19159" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتنياهو:  آنها مطالعات ژنتیکی بر روی جوامع یهودی مختلف انجام دادند — اشکنازی‌ها، یمنی‌ها، شمال آفریقایی‌ها و حتی اتیوپیایی‌ها — و چیزی شگفت‌انگیز کشف کردند.  آنچه کشف کردند این است که همه ما، برخلاف ادعاهایی مبنی بر اینکه ما هیچ ارتباطی با یهودیان اولیه‌ای…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19158" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتنياهو:
آنها مطالعات ژنتیکی بر روی جوامع یهودی مختلف انجام دادند — اشکنازی‌ها، یمنی‌ها، شمال آفریقایی‌ها و حتی اتیوپیایی‌ها — و چیزی شگفت‌انگیز کشف کردند.
آنچه کشف کردند این است که همه ما، برخلاف ادعاهایی مبنی بر اینکه ما هیچ ارتباطی با یهودیان اولیه‌ای که اینجا بودند نداریم، دارای ژنی هستیم که ما را مستقیماً به سرزمین اسرائیل بازمی‌گرداند.
به این معنی که همه ما، در جوامع مختلف، این ژن یهودی را داریم.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19157" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره ایران:
من در حال بررسی یک حمله عظیم هستم؛ بزرگتر از هر چیزی که تاکنون رخ داده است.
من نزدیک به اتخاذ این تصمیم هستم.
منبع: N12</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19156" target="_blank">📅 19:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار: آیا لیندزی گراهام حذف شد یا مرگ طبیعی بود؟
نتانیاهو: نمی‌دانم. ادعای آمریکایی‌ها این است که بررسی کردند و میگویند مرگ طبیعی بوده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19155" target="_blank">📅 18:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شورای رهبری یمن:  «پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.  ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19154" target="_blank">📅 18:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرانسه کارکنان سفارت خود را از تهران، ایران فراخوانده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19153" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه :
پس از از سرگیری رسمی جنگ، نیروهای نظامی متجاوز ایالات متحده از موشک‌های کروز استفاده کرده‌اند که از کشتی‌های دریایی خود در اقیانوس هند پرتاب شده‌اند.
با این حال، پس از اینکه آن کشتی‌ها ذخایر موشکی خود را به پایان رساندند، دیروز به استفاده از بمب‌افکن‌های B-1 که از پایگاه هوایی RAF Fairford در بریتانیا پرواز می‌کردند، روی آوردند.
همچنان که مقامات وزارت امور خارجه اعلام کرده‌اند هر پایگاهی که برای پرتاب حملات علیه خاک ایران استفاده شود، برای ما یک هدف مشروع محسوب می‌شود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19152" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند
ترامپ: یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری ما با ایران، آن‌ها رفتار بسیار مسئولانه‌ای داشته‌اند.
متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته دو کشتی سعودی را مورد هدف قرار داده‌اند.
لطفاً اجازه دهید این حقیقت، تأییدی باشد بر اینکه اگر آن‌ها این کار را دوباره انجام دهند، ایالات متحده مسئولیت آن را به ایران نسبت خواهد داد، زیرا حوثی‌ها یک عامل یا واسطه برای ایران هستند، و ایران با مجازات‌های نظامی جدی روبرو خواهد شد، و البته، خود حوثی‌ها نیز مجازات خواهند شد.
من از حوثی‌ها بسیار ناامید هستم، زیرا تا به حال آن‌ها به طور بسیار حرفه‌ای و هوشمندانه عمل می‌کردند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19151" target="_blank">📅 16:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 11</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 11
پنجشنبه 23 جولای 2026</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/SBoxxx/19150" target="_blank">📅 13:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مارکو روبیو درباره ایران:  عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.  سیاست ترامپ «سر در برابر چشم» است.  آن‌ها بهای بسیار سنگینی خواهند پرداخت.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19149" target="_blank">📅 12:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XykASIw9uKTSKHjFbAjaDBymf6F15sw01eXVv8LZTZdicgd7PbcORAKR9D1D_4Mo_l0IhQ4ic2V_sRukYC5fnLNja15B9Poq6_GGT8A7-fUtRygyBK4-Stz5U_APoRcJYhW8Yr7sIP5fumqD7NgOB8FVaOBNtr07goqbEBcJ2JM-Tg9E8H4YX480rO3j9jFQEEZYNJG1n_EtjeCBXtpBFWO0uerVdzDglJgaCdn-heAinYm0D311boYSY1NTvB25wlQgbAu-5TY37tjITv4NzcL5J3hBkZS0MlbhGs7E4yAdFuJOnoI8lvQKUKJNYl2DONl-UCHEDP85I3a2orw79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.  توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19148" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مارکو روبیو درباره ایران:  عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.  سیاست ترامپ «سر در برابر چشم» است.  آن‌ها بهای بسیار سنگینی خواهند پرداخت.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19147" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مارکو روبیو درباره ایران:  آنها هر روز با ما تماس می‌گیرند و از ما تقاضای توافق می‌کنند.  هر بار که آنها به توافقی می‌رسند، یا آن را نقض می‌کنند یا پس از توافق، خواهان تغییر آن می‌شوند.  احتمالاً آنها هنوز برای توافق آماده نیستند، اما به زودی این آمادگی را…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19146" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مارکو روبیو درباره ایران:  با وجود سخنان تند و ویدیوهای لگویی احمقانه شان، آن‌ها به شدت در حال رنج کشیدن هستند و تا زمانی که به واقعیت پی نبرند، این رنج بیشتر خواهد شد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19145" target="_blank">📅 12:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مارکو روبیو درباره ایران:
با وجود سخنان تند و ویدیوهای لگویی احمقانه شان، آن‌ها به شدت در حال رنج کشیدن هستند و تا زمانی که به واقعیت پی نبرند، این رنج بیشتر خواهد شد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19144" target="_blank">📅 12:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار در کنارک!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19143" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایران پیشنهاد آتش‌بس میانجی‌ ها را رد کرد</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19142" target="_blank">📅 11:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19141">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0PC78FL7A2lytC30dcvvLp-X1eVX_OaRzfXq9Tu0czTHp52OuY71-lDwN0z4aEx_PLca8XDJMv8ShmGsIhqjzC1Yl5sD0dVqzWYnYASd-bqXbX6mIgeUsIEYy6ihnheKdUQ3CmLdigUwRLm-Sy0Cs7nIuEoWvY9e7HvMR1J1nNkHgXcoTj7_lK5aOY_8pk34LwMUq1AANnTNSDqIVfIsLzUh7F87j6XMVTeyPu0sEkCEWlLp_8iA_9yRAAmlvsVHfOgNqGIOlB7u7Vd5sNBXR2UdQ1hGuKEOqaUv9p5E3qYhfZvCdCTxxqkVS67Tn1oJSi1ExYllQ4e1rXDbKelDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19141" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19140">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf6EbCKIQiGMN-Fe2ofwqNdYgEO1DA_MlNycYmWOB6kKLWbkXjiolkkwxfvCxAoRwjnSoAqZ5cUfzzUpu43AhnQBzEkGrXj3X3oyoYGeGVyEYaBXwG_EXyI7fyqcZZiOVrrZ_V9NNeEvYUVZUC7ze05ayQ3vcfUtki_tz1zPPR5bv6zuKNoM4Nq3fQ3LuDYSZpFo_kh6ZtlVqzVq-fhyuF3xHhKiYMbl0b--BmVhL_2jfTFz65W8lIo4dvfk7b4DuoqTAOL9iGCnQ_X6CW_0gaBBKwjyZI1kda85Ml2OuGcyJ1yttmWFSZZ6oLktxSz7QYDwXJqfsitbG0PdpmjREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19140" target="_blank">📅 11:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19139">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMvmIFPoHVqVDV-Jr4tRFa9-hvFxgta56HyACnonEEUjFmBcTTDCiK86nrk1Z48-tDysMZY8X7wZLPtGW90YfSxh3HdJxSlOFMABsQzPPbjLtkbzD6cjwfvPEc43sky1d7WOTSU7F8CWx879r983-gaeB4AuQvuD3w4h8bG01sqUuT5a6VRrymcMFom9FfgrbfWzOOf67ZcQ9cvuKO84IUfFaW1Bmh-UYs_9iP8ldb5zIbvrKpZWJNP9fN6OZ5hVaKDY1CnMZp7mAEboZMM0BziDmdzvaKO-oNVYtSTv8NAoEO27k28zwJ6emc--uucea-S3KxXbIL4nKl6zy7R_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند
تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.
از آنجا که بازارهای آتی بر پایه انتظارات قیمت‌گذاری می‌شوند، جهش قیمت اوره، آمونیاک، فسفات و گوگرد می‌تواند حتی پیش از کاهش واقعی تولید، زمینه‌ساز رشد پایدار قیمت گندم و سایر غلات در بازارهای جهانی شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19139" target="_blank">📅 11:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19138">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فایننشال تایمز :    آمریکا نمی‌تواند با مذاکره به اهداف خود برسد. بنابراین تغییر رژیم دوباره در دستور کار قرار گرفته است!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19138" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19137">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECk_A0FqjyRTmRNbnRTzDzhvolHpHUkWs7QO2UgIBzsWPYP1ITbCiQ5yjfHn3BAwsI5MJqbymeb045DIvyqKCj9tv-eouPoZ1w7utGM5XqufJ99idgl25STs91RqMJwIGI4I4rDlzqnY8erxCmIyI2qewE4q7o2di9dINXRwEcR0P6JX_izP0ctcu1aon_UJbTq6NUvNIo-a7rxWThmpBiiBJgrlYbLfImEE0Mdb-hCZBkbS6W8J2druXk588rpBykayYrM-SWM89utlttuz5jXhkS0TEScxd7-b9eFH3di4bCgNNB-TLWbybgZnQszeywtYsRhOaNd5C7aZRP7zlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19137" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CemT_SxnudxSxuYYS8jYAAH7Kk4qVh2WcIj2_sfmkDJFw4mX7zbNEDBz9vlLplOFHFN5v3Bcr9kdQPERuZN2PnQgnaScEr9xGmqgcFVbR9Ba5HTq4ioT6VkphoxprCuTeWD0UtkWSiGHZysXEmxHEh-4Ht9Cm0dHp4tQZRrT-OU6p3Cv4GmKrjNVWvloIpGTat4QD7RddvQ2njrmJnyr7X1owLUgr8l1HhZ2uAlny4Rfxks8jNuEvHkbQTkHAbHfG0IeBi_mzvZKDUvouYB6Y3uEXel-YXE9wUPdFDxqmRqIe3FfYcujyczCrdmDLRSAke5eddMOJqKca0Jl5NWrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چند ترامپ می گوید تنگه هرمز باز است اما داده های بلومبرگ نشان می دهد که شمار کشتی های عبوری از تنگه هرمز (آبی) به کمترین سطح ممکن رسیده است.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19136" target="_blank">📅 10:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_1y4OqwRvZACMErHz5bOj9pp-_npNKIv0vt-uA5YTSV9l_SKEu-AGt3BoMt1YugE_frDhMCYx1Y3j2WR3bySrF7cQMZq-InZSyJyqZS9wXLZ42Y7hypmNpd1deM7rEC3d3aF4LsdlHOIBpA2ufcDOP5RRJGelzt1mBfA14CRfccVhpqC5p4c0Hbvogar2XXPQb2OvfjdmVWam6MOur1NIxf9CTlx2lCT3mZe2TAjhT5udvHuimy-MQuW0TsHkElhltooUAspOkG1e-Ldva2ICHK5JzGtVwBc9PYl6L-3D-nC2rGcPTeBGIhUhJ4RhhD50gva2Z2qB5oISTwYm7aNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان، طرح بودجه دفاعی به ارزش ۱.۱۵ تریلیون دلار را با وجود مخالفت‌های جدی دموکرات‌ها تصویب کرد.
دموکرات‌ها از ترامپ به دلیل همراهی با حملات اسرائیل به ایران بدون تایید کنگره انتقاد کردند و با بندهایی که به تعمیق همکاری‌های دفاعی بین ایالات متحده و اسرائیل می‌پرداخت، مخالفت نمودند.
این طرح همچنین شامل ۶۰ میلیارد دلار بودجه اضافی برای مسائل نظامی است که بخش زیادی از آن انتظار می‌رود برای پوشش هزینه‌های مربوط به درگیری‌ها استفاده شود. اکنون این طرح به سنا ارسال خواهد شد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19135" target="_blank">📅 01:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19134">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام:
امروز، ساعت 17:30 به وقت شرقی، نیروهای ایالات متحده با دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند. این عملیات ادامه خواهد داشت تا توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه، بیشتر تضعیف شود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19134" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
