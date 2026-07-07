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
<img src="https://cdn4.telesco.pe/file/rgnE7Es-HyvCJxRyByB89ZmE8oDxlaFkxGg-naHYYTGKtbVoBek4yq4JYb4WHFnmP9CfGn8sTGvoHdANBmOk7aru99gdaQKd7uAdtt4R2NO4rDTfpdO9TRBBCucbekDR0gjsEA2gSRiP0ybeMuB_ylh1IuIzLSE3pFkcklgBgCb4g9dVnplokEdANW0PzgThVqlk_jcsWzbsGcRnnafKZyTVnWjqU8N2FWW2EUL64OYSVEjZz1gPaDYOIcs8Ml4LO16thcAwPJD7YyTiwCrlwST7Xnau45MwjMQtHvyA129yCX5aZCr3oDeg-XP4s6qvIVO_peWwXOcfgnmwbi30XA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY4R0Bv86qbqnxNFyQXAsVnFnXEcmfooW9Z8Zu3VvVN0wOvgJq4UpsCrsjj7_RFXBBbR7eqsUhhONLRb_N5S2yciDV7qjMUvgJLjwRsDCSCFWtfedMmt5819_K1qUV-xpm1wY1sSoGnhICPPyn9d0DN2SyNgvQxqamiHQFjkO-FpVVIBPB6VH97cqYYzUZl7Ys8MiPum0FDKyrXEmaKSdDXXl3k3NVHXZqoFDdmLI3znuReTOfzlCNmRM9oYL6ot4DcnLhTN4zu0F8WF40QOCk_gNr2mXpaef-8YUEBVFJQqh5KaMWAK4Iko0VDXWi1RN8RnEx72G2Y_YlVxCX_mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایین قرار دارد و ادامه شرایط نرمال پیش بینی می شود.</div>
<div class="tg-footer">👁️ 752 · <a href="https://t.me/SBoxxx/18264" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SBoxxx/18263" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت . اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند . این حجم از اختلافی که…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SBoxxx/18262" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1a9F2v78hZAyRh8Qntbl1jBlppLHoNn-irS2rEBt0ad67RH9hnt7UYK0PZIJSC_rY2O1CsVBzPgtqaBGodPCVgGnn_8e-V3WZl643jDeJ8QI0e_unk8Az05E-aGzsxeMTvqRxq7BTZgTiSp0385YoJ8oTpiQ3byKkjHbC-63A5rbAIrnmIsXrTuAbbS9Ec60UlliN6dCFfSHDcfL-9umKfd6aKNeffuM1v574Hllycfsse8iaxhIRHfP5_719cFezZ5Yof8fJbt5lhpd-BxYilWWjQlARaL_tinNSLFNje4QcPvdPcM2JUlvdxzLGIr6UinzCeLX29AseVA51n1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت .
اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند .
این حجم از اختلافی که افتاد واقعا خرابکاری نیست،شاهکار است!!!
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SBoxxx/18261" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست     معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SBoxxx/18260" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست
معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری باکو نیز در میان این کشورها قرار دارد.  این برنامه شامل توسعه مشترک، تولید و صادرات پهپادهای اوکراینی و همچنین تبادل تجربه جنگی بین کشورهای شرکت‌کننده است.</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SBoxxx/18259" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18258">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/18258" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4NzlxiTlD_pF8KbdjMBXJZ3yHmyYjcBwPQihlpf-EMr3QXEutnHdzuLGQ5sVmOLxhAGC-hwpMDot9LS0uK1p0Y6WBGv1xo1dp5cXGvPqX7uWYJYi8ua2R8iWmO5peY5PkUmM_TaS7CDZ_S-hwy8rueJwP6G2dpJ0_26QBGFG7ytbdtRN1FQkGtlaBMQrTBRorpnK841FrgP7sOL0VzAERkEatKlkhmMOdDEB2APS0PpZf8GlUm4cn83b00tAD3KaiN3FXrZ6uvdJj_l_1Br4psRXffILoKxpwVv8fP4Qsnh9z1JcIDmwWfrmsHS18PWhRxo6a3v9GzhYhvFs1VC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/18257" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/18256" target="_blank">📅 09:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مسئول آمریکایی به اکسیوس:
بیبی وعده‌های زیادی درباره جنگ با ایران داد که محقق نشدند.
اما چه کاری از دستمان برمی‌آید؟ او خواهد آمد. او وعده‌هایش را می‌دهد و سپس ما مجبور خواهیم شد همه چیز را بررسی کنیم.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/18255" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18254" target="_blank">📅 20:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opgHQafMCUsymF3FhqckU3S7iHnuqOXNYa0ZEzNHtFu8dW5Jay55mDiD5maYTPawfvEJhnSLCrVGC-HcX9nmjdewgO9Nd1jgNLIidSj5rfQT0tccfAyVApZd1mo4ozLTmjf4tksBIVqnjDQpdVCl_cT_V5eSAs3P71sPEM4nvpMmz2fPkuQxqgYeEXs1SegPxf60bYa9LaL9_xce-jne9o2S740_2Spdj1LJyJusROYRliZzRrUimyJHvCLBhiR3qnZ7hesIGdC8EVh1hu4Gr8J94OYAZCxqlITSZfzvgJ3j43hHGneg3_iJ9kyvFgkIf7QLwZykW5fNvpoIOameXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما در کل این سیاره خاکی بگردید هر جا کمبود برق و انرژی باشد احتمالاً یا کمونیست هستند یا دوست دارند شبیه کمونیست ها باشند و با شکم گرسنه و خشتکی پاره مرگ بر آمریکا و مرگ بر سرمایه داری سر بدهند.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18253" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شبکه ملی برق کوبا روز دوشنبه دچار قطعی شد و حدود 10 میلیون نفر را بدون برق گذاشت.  مقامات اعلام کردند که علت این قطعی همچنان در حال بررسی است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18252" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گویا آمریکا می خواهد در این مدت آتش بس موقت با ایران، تکلیف کوبا را یکسره کند.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18251" target="_blank">📅 20:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز  افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18250" target="_blank">📅 19:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ در مورد جنگ اوکراین:
به نظرم ما بسیار نزدیک‌تر از آنچه مردم تصور می‌کنند (به آتش بس) نزدیک هستیم.
پوتین می‌خواهد که این جنگ پایان یابد. من این را به شما به شدت می‌گویم. ما یک تماس خوب داشتیم.
زلنسکی در واقع می‌خواهد که این جنگ همین حالا پایان یابد.
ما می‌خواهیم به ناتو برویم و می‌خواهیم در مورد آن صحبت کنیم. و من فکر می‌کنیم که می‌خواهیم آن را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18249" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
بمب خبری ... اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران  https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18247" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Movahedian Channel</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=CODYaPLODR4nqP5sXoKuLkQn-881H5VmsZHzreZiHrkJkiZiVBtLYEKCZHOff9we0etHwvXcq6Wd9cMobTyFfXOywRVj0bicU-2F-BbvHxFJw377uOgpTckz8RgjWNfuyfD6dnnFMQDHBZWIBEOzEklPZutR3u-0cCBwdj-2OLGmvtIe5fOElu1tsWI-fr2YJNOpB1llgpIqbZDpGxLfeYSsObJpl1XzMD4yAtDGKEYElEPoTk2qTkD16KJt7d83zvmcCDzM1rXNpSMJrGrQUWB74bbOcxZUMd0h7hKHIY3LVWWxaomLrUJ6kXdUkdT4NHsEeGYBXsWiX0wogHyitA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=CODYaPLODR4nqP5sXoKuLkQn-881H5VmsZHzreZiHrkJkiZiVBtLYEKCZHOff9we0etHwvXcq6Wd9cMobTyFfXOywRVj0bicU-2F-BbvHxFJw377uOgpTckz8RgjWNfuyfD6dnnFMQDHBZWIBEOzEklPZutR3u-0cCBwdj-2OLGmvtIe5fOElu1tsWI-fr2YJNOpB1llgpIqbZDpGxLfeYSsObJpl1XzMD4yAtDGKEYElEPoTk2qTkD16KJt7d83zvmcCDzM1rXNpSMJrGrQUWB74bbOcxZUMd0h7hKHIY3LVWWxaomLrUJ6kXdUkdT4NHsEeGYBXsWiX0wogHyitA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بمب خبری ...
اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران
https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18246" target="_blank">📅 15:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ونس: ظرفیت تهاجمی روسیه نزدیک به صفر رسیده است   در مصاحبه‌ای با تایمز بریتانیا، جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده، وضعیت نظامی روسیه را ناپایدار ارزیابی کرد.   ارزیابی او: توانایی روسیه برای عملیات‌های تهاجمی بیشتر «ناچیز و تقریباً صفر» است. این می‌تواند…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18245" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18244" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp4yrGzNVI6qPORsxnPVp5NOXNKl_7KcT6FeWrimFw13WQZP3lMF5wamqIPoTbbEax0A_qVHshwxeY6m4duYWB2xuYaOdxMhDF3mIosJ18Fz1KdSKqscYC-u--I8_hUBoJefmw6hBEHegsACeUlj9fQmbrjMaLCgOYnY3xvtpHS4aosSBQxTqbu_dUFZR-JPf6Gv0QiwTl2QP5r2FLDAbcVx4QP7gI8Ktg857HPLwE2mcFIVLom7HZ0SGtcTwV7_r0GFq7vNVWmSAVUr8tWxypNtT5rBShAuvnfilLiwI58k62R2_-aQtOyrQquXj15r6LTHyu52JSMTYVjivwfEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18243" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18242" target="_blank">📅 12:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز
افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت اقتصادی پیچیده‌تر از این برداشت خطی است. هزینه‌های دفاعی معمولاً با تأخیر وارد چرخه تولید و تقاضا می‌شوند و اثر آن‌ها به‌صورت تدریجی در اقتصاد پخش می‌شود. تجربه‌های تاریخی، مانند بازسازی ذخایر تسلیحاتی آمریکا پس از جنگ خلیج فارس که چندین سال به طول انجامید، نشان می‌دهد که این نوع هزینه‌ها به‌جای ایجاد شوک‌های فوری، بیشتر اثرات میان‌مدت و بلندمدت دارند.
در سطح ساختاری، ماهیت خریدهای نظامی نیز در حال تغییر است. جنگ اوکراین و استفاده گسترده از پهپادها در عملیات علیه روسیه و کریمه، نشان داده که فناوری‌های کم‌هزینه‌تر و غیرمتقارن در حال بازتعریف اولویت‌های نظامی هستند. این تحول به‌طور مستقیم بر زنجیره تأمین دفاعی اثر می‌گذارد و تقاضا را از سامانه‌های سنگین سنتی به سمت فناوری‌های سبک‌تر، هوشمندتر و مبتنی بر داده سوق می‌دهد.
از منظر ژئو‌اقتصادی، یکی از روندهای مهم، بازتنظیم روابط تأمین‌کنندگان تسلیحات است. اروپا به‌تدریج در حال کاهش وابستگی به تجهیزات نظامی آمریکاست و به سمت توسعه ظرفیت‌های داخلی یا تنوع‌بخشی به شرکای خود حرکت می‌کند. این تغییر می‌تواند در بلندمدت ساختار صنعت دفاعی غرب را دگرگون کند.
در این میان، خاورمیانه نیز به‌عنوان یکی از بزرگ‌ترین واردکنندگان تسلیحات، نقش تعیین‌کننده‌ای در جهت‌دهی به جریان سرمایه و فناوری نظامی دارد. این که بودجه‌های دفاعی کشورهای منطقه به چه نوع فناوری و از چه کشورهایی تخصیص یابد، می‌تواند بر رقابت جهانی صنایع دفاعی اثر قابل توجهی بگذارد. در مجموع، آنچه امروز مشاهده می‌شود نه صرفاً افزایش هزینه، بلکه بازآرایی عمیق در معماری اقتصاد دفاعی جهانی است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18241" target="_blank">📅 11:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJygRn-n0LindGaIHxbEoaMGimS1t-FQ7rlb5azm9X4xIOu_6Hgz0gYzvRfDxYqLlzRnkw3bMLiZwQ9fza4NIjLBq1R2mRY7xNgybgJBn0YiYsDhIKOCAZt5pcU61gy8EkksUuyZqWYwmpEc-69VvqHzejPFXomwAHtAitjkCTxmM9IIaZ1CTm0AbXSpjus7F-ERzTAGF0WNU2WSuBMn45xw20GOjedscgSZWjZ8CZGPVtOYeR37hE3U95svzzexsxeC1s3zoWlKnJtL8bGD3oI0j566BESX08KfaKW-MZ22JNFjojJzHd5NFqxnYVndAU_dDKrx4EUC8IzfMgZgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتک برای امروز در سطح میانه پایین قرار دارد و ریسک پذیری بسیار ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18240" target="_blank">📅 11:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18239" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شبکه ۱۴ اسرائیل:
سپاه قدس واحد جدیدی به نام « یگان مختار » تشکیل داده است که با شهروندان مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18238" target="_blank">📅 10:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18237" target="_blank">📅 10:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvCLEtO58ciWc22sRGYR9r7r9nx_H8A2YyOCH67rIHeaLuvEUdnAauBP0qswX-xm1Z3LJz8vdpqEVpx6vD3FikynWb46FZBPsVwALRBWxqlxA6cS0IP2VKTtrMUPLcDaWuCDgCpLR8nJKV2Q9pAOQ7TR_RxYlDjS0hDOCVBJl9r7LCRC7_CRSvvNHe3C-0TrVXAm8d8Yg5mbp3vzfc9renXKQNK2CIgpZthxF8DCWBuDjilXdSfcl8ArC-9OC1kRt2I2nqe1MWM5D7F2Lr9r2GOverW5_wJjyX7AFR66Hkys6uN8P4zh3Y1ftcJgPmELnPQRBbtN7H_e3n9bjKn31w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گویا واقعاً زنگ زده اینفانتینیو و گفته یا بازیکن اخراجی ما را می بخشید یا بازی خراب!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18236" target="_blank">📅 09:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18235" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTlCKdMvyKAVxjkb-5w5MGAoM1R3PRnZtIajkYh63mL0BCzUDpGJ_dShAuhpsFDqJLDHcFFJdiKeIMGmcPQH2Ur-gS1wVZhkstKQNzEmmKXlz-MWQcmAN2XJUo45DZs8BNu8GHkpD_QVfNGzHZCOZ4j_Ngo3yxnpNRwU6Tbp_qol4OWpN-OHblHdHGT4RBrr3TT1t3b6SCvzf2lppatL0rPPnursvoIBc8MsAHEoGxzd6b57K5q4nMIi6FNr77Vm_TWYpJuPwGu5hkR2Wyo_gUZnYaTcYYMIX6dCf5XOnsJQxlgAFoxf9UWL4E6dsHRIeSTfGH3LKZz1isF9i0MNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استقرار بالن نظارتی (الکترواپتیکی)  در آسمان تهران</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18234" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو:
«برخی روستاهای مسیحی‌نشین لبنان در واقع درخواست الحاق به اسرائیل را داده‌اند، زیرا ما از آنها در برابر حزب‌الله محافظت می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18233" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایران می‌گوید از آتش‌بس با ایالات متحده برای تقویت آمادگی رزمی خود استفاده می‌کند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18232" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18231" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.  @MonazeratChannel</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18230" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمناظره‌ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=L_l2ag0sA-8hTEwv8s0etz7azlusrWzZaYlZrjtY_ED_-fd5ZfqUE7j0yVKpsWb-7KJHsVKJ5zUTR3OmPfN_qbQP467D-PGSqpZvCpm21Txl8Fm6w0Ms9MWC20o3TJgUoeKMsTtYRvBzsXEr9QVtCuqPZG8-wfzABRPlAYqgpU7AZnHP11TSgE4JqanzHKkc47reJfKwAckj97zK3h1X9DS86m5NJxFG7gzXnSwQy6NHqOomHQae12KRFBC_VveG5bIF25wWai6hHLCGr3EOgH6F3_REdZclRqn7Xcgo9WRc7hq82UgVr4YkCxBkVU0oSmgb380IFaPJH1oc0rhAIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=L_l2ag0sA-8hTEwv8s0etz7azlusrWzZaYlZrjtY_ED_-fd5ZfqUE7j0yVKpsWb-7KJHsVKJ5zUTR3OmPfN_qbQP467D-PGSqpZvCpm21Txl8Fm6w0Ms9MWC20o3TJgUoeKMsTtYRvBzsXEr9QVtCuqPZG8-wfzABRPlAYqgpU7AZnHP11TSgE4JqanzHKkc47reJfKwAckj97zK3h1X9DS86m5NJxFG7gzXnSwQy6NHqOomHQae12KRFBC_VveG5bIF25wWai6hHLCGr3EOgH6F3_REdZclRqn7Xcgo9WRc7hq82UgVr4YkCxBkVU0oSmgb380IFaPJH1oc0rhAIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.
@MonazeratChannel</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18229" target="_blank">📅 16:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18228" target="_blank">📅 15:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.  با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18227" target="_blank">📅 15:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18226" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قالیباف، در مراسم تشییع رهبر سابق ایران:  «ثمره خون خامنه‌ای آزادی بیت المقدس خواهد بود».</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18225" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18224" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کلا خاطره خوبی از محاسبه خسارات و جمع آوری شواهد نداریم.
بار پیش
هم که جناب عراقچی داشتند خسارات اشتباه محاسباتی اسراییل در جنگ ۱۲-روزه را محاسبه می‌کردند که اشتباه محاسباتی بعدی روی داد و اصلا محاسبات ما به هم ریخت.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18223" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18222" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:
"ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18221" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Trump Accounts
سرمایه‌گذاری بر نسل آینده یا
پروژه‌ای سیاسی؟
دولت دونالد ترامپ با معرفی طرح «Trump Accounts» تلاش کرده است ایده‌ای را به اجرا بگذارد که در ظاهر، حمایت از آینده مالی کودکان آمریکایی را هدف قرار داده است. بر اساس این برنامه، برای هر کودک واجد شرایط، حسابی سرمایه‌گذاری ایجاد می‌شود و دولت برای نوزادان متولدشده در بازه زمانی تعیین‌شده، مبلغ اولیه‌ای را به این حساب واریز می‌کند. دارایی این حساب‌ها نیز در صندوق‌های شاخص کم‌هزینه سرمایه‌گذاری می‌شود تا در بلندمدت از رشد بازار سهام بهره‌مند شود.
طرفداران این طرح معتقدند که ایجاد سرمایه از ابتدای زندگی می‌تواند فرهنگ پس‌انداز و سرمایه‌گذاری را در جامعه آمریکا تقویت کند. از نگاه آنان، حتی یک سرمایه اولیه نسبتاً کوچک نیز در صورت رشد مستمر بازار، می‌تواند هنگام ورود فرد به بزرگسالی به منبعی برای تأمین هزینه تحصیل، خرید نخستین مسکن یا آغاز یک کسب‌وکار تبدیل شود. این رویکرد همچنین می‌تواند وابستگی شهروندان به کمک‌های مستقیم دولت را کاهش داده و مشارکت آنان در اقتصاد و بازار سرمایه را افزایش دهد.
در مقابل، منتقدان بر این باورند که اثر واقعی این برنامه به توانایی خانواده‌ها برای واریز مبالغ بیشتر به حساب فرزندانشان بستگی دارد. از این منظر، خانواده‌های پردرآمد بیش از دیگران از مزایای رشد سرمایه برخوردار خواهند شد و در نتیجه، شکاف ثروت میان طبقات مختلف جامعه ممکن است کاهش نیابد و حتی در بلندمدت افزایش پیدا کند. همچنین برخی ناظران، انتخاب نام «Trump Accounts» را اقدامی با رنگ‌وبوی سیاسی می‌دانند که می‌تواند این برنامه را به بخشی از میراث سیاسی رئیس‌جمهور تبدیل کند.
در مجموع، موفقیت یا شکست «Trump Accounts» به عملکرد بازارهای مالی، میزان مشارکت خانواده‌ها و نحوه اجرای مقررات آن وابسته خواهد بود. اگرچه این طرح می‌تواند گامی در جهت گسترش سرمایه‌گذاری عمومی باشد، اما قضاوت نهایی درباره آثار اقتصادی و اجتماعی آن تنها پس از گذشت چند سال و مشاهده نتایج عملی امکان‌پذیر خواهد بود.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18220" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون:
فرانسه دارایی‌های ضد مین را به خاورمیانه اعزام کرده است، از جمله به‌ویژه دو کشتی  ویژه جستجوگر مین
همراه با دو ناوچه و یک هواپیمای گشت دریایی، این دارایی‌ها آماده هستند تا در کنار شرکای ما، به از سرگیری کامل کشتیرانی و تضمین ایمنی ترافیک در تنگه هرمز کمک کنند</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18219" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
پناهیان ؛ مشاوره ریاست نهاد نمایندگی رهبر در دانشگاه‌ها :
حاضریم تمامی منافع ملی را فدای خونخواهی رهبر شهیدمان کنیم</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18218" target="_blank">📅 23:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
بابک زنجانی
:
به زودی خونخواهی رهبر شهید شروع خواهد شد و آن خون خواهی اقتصادی است</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18217" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران قصد دارد به چین تعرفه‌های ترجیحی برای تنگه هرمز ارائه دهد
تهران قصد دارد به چین و سایر کشورهای دوستانه تعرفه‌های ترجیحی برای هزینه‌های عبور و مرور ورودی تنگه هرمز اعطا کند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18216" target="_blank">📅 22:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به گزارش کانال 15 اسرائیل، دونالد ترامپ از اسرائیل خواسته است که فعالیت‌های نظامی خود را در لبنان افزایش ندهد، زیرا نمی‌خواهد این امر در مذاکرات جاری او با ایران دخالت کند.
به همین دلیل،  نتانیاهو یک عملیات نظامی که پیش از این برای منطقه علی‌الطاهر برنامه‌ریزی شده بود، را به تعویق انداخته است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18215" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئیس‌جمهور عراق:   عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18214" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18213" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.  «همه آن‌ها آنجا هستند. با یک…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18212" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.
«همه آن‌ها آنجا هستند. با یک شلیک [می‌توانیم همه آن‌ها را از بین ببریم]، اما این کار را نخواهیم کرد زیرا در آن صورت کسی برای مذاکره باقی نخواهد ماند»</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18211" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اردوغان به اسرائیل هشدار داد: "نباید اجازه داد اسرائیل منطقه را در خون غرق کند."
رئیس‌جمهور ترکیه، اردوغان، در سخنانی مشترک با نخست‌وزیر پاکستان، لحن تندی علیه اسرائیل اتخاذ کرد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18210" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18209" target="_blank">📅 18:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترکیه با موفقیت موشک بالستیک TAYFUN Block-3 را علیه هدف کشتی متحرک با سرعت هایپرسونیک آزمایش کرد.
شرکت ROKETSAN یک آزمایش آتش‌زنده از موشک بالستیک TAYFUN Block-3 انجام داد و با موفقیت یک کشتی سطحی بدون سرنشین آزاد در حرکت را در دریا با یک سر جنگی زنده با سرعت هایپرسونیک هدف قرار داد.
هدف حدوداً ۷ متری — که یک قایق ماهیگیری کوچک بود — با آنچه شرکت آن را «دقت جراحی‌گونه» توصیف کرد، نابود شد.
این آزمایش نخستین مورد از این دست است که در آن یک موشک بالستیک که با استفاده از سر جستجوگر برای هدایت در مرحله پایانی، یک کشتی سطحی متحرک را در دریا درگیر و هدف قرار می‌دهد.
ترکیه می‌گوید این نخستین یکپارچه‌سازی چنین سر جستجوگری بر روی یک موشک بالستیک در داخل کشور است و یکی از تنها چند نمونه در سراسر جهان — قابلیتی که به طور موثر یک موشک بالستیک را به یک سلاح ضد کشتی تبدیل می‌کند.
سرعت پایانی هایپرسونیک TAYFUN آن را تا حد زیادی در برابر پدافند‌های متعارف دفاع هوایی مصون می‌سازد.
نسخه Block-3 پیشرفته‌ترین نسخه از برنامه موشک بالستیک توسعه‌یافته داخلی ترکیه را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18208" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک کارشناس:
به نظر می‌رسد که ایران در مراسم تشییع جنازه رهبر خود هر هیئت خارجی را با یک آیه قرآن مرتبط کرده است که هدف سیاسی خاصی را دنبال می‌کند.
عربستان سعودی: آیه ای درباره دو ارتش که در جنگ با یکدیگر روبرو می‌شوند، یکی مومن و دیگری غیرمومن.
ترکیه: آیه ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که "نشسته"اند، برتری می‌بخشد.
دولت لبنان: آیه ای درباره افرادی که در صورت درخواست، از انجام فداکاری خودداری می‌کنند.
حزب الله: به آنها گفته شد "ضعیف نشوید یا غمگین نشوید، شما برتر هستید."
حماس: آیه ای که مردانی را که عهد خود را با خدا وفا کردند، مورد تقدیر قرار می‌دهد، "برخی از دنیا رفته‌اند، و برخی دیگر در انتظارند."
حوثی‌های یمن: آیه ای که به مومنانی که بدون سستی جنگیدند، ستایش می‌کند.
قطر: آیه ای درباره بخشش و لطف الهی، که به عنوان اشاره‌ای به نقش میانجی‌گری این کشور خوانده شد.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/18207" target="_blank">📅 13:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اظهارات مدودف، نخست‌وزیر روسیه:  ایران به جای سلاح‌های هسته‌ای، سلاح دیگری را کشف کرده است که از نظر قدرت، نه ضعیف‌تر از سلاح‌های هسته‌ای است و آن، تنگه هرمز است.  بحث‌ها حول این موضوع است که چگونه باید به توافقی دست یافت تا این تنگه در آینده به چه صورت عمل…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18206" target="_blank">📅 13:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جناب الکساندر سرگین هستند از گه خورهای اعظم که بیرون گود نشسته و به ما میگویند لنگش کن!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18205" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcemMUhPkS1lpacuheCSjYdFXV4970q_3SRu8kxDNTkJX6JGilDyNWRNkUhFRtKJAx5yY02tLP5kd6b7dIrixfmYpJAVJPXY85jc3DmpGnYCMgQ_iBKZeb3F5_cQWRGuTLdGyC3OoGW_RiwFPEXeF_-I6SAeF6uNaBaVFJXKmuYFm2EwXzrbSExFujzPDXOHHj--w9H7wOmmv54d7bqJFYaj76NAVZw7EsOpHcQYHrCcpStR1KNmIKOAy9BFxhBJ5kGCYf6R5KxZ04k26H6L0bus1KItfJxPWiNQaJpYog1KqtXMgEQmYiEnYmRnbopS-cT9KhBA3L7_cLvKM9EpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس ترنس هست اما نجس هم هست؟!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18204" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه‌های غربی:
عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند و از آنجا که ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد.
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18203" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18202" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ
:
ما مناقشه با ونزوئلا را در یک روز حل و فصل کردیم و ضربات بسیار سختی به ایران وارد کردیم.
طرف ایرانی بسیار مشتاق است و به هر طریقی به دنبال دستیابی به یک توافق سیاسی با ما است.
ما از روی حسن نیت به ایران یک هفته فرصت دادیم تا عملیات را متوقف کند تا مراسم تشییع جنازه برگزار شود.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18201" target="_blank">📅 09:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VokeGfuIpj8IlcbFGO10TjZty_WGAHT0XY2-54jX4CZze6kWRwjfLoxjFrE792pH6MlbQg0a0mFTamWnrB6kfmmUY7w5Ta578JF7X5S0AD1_mRqRHBiBWC0n9QgjsIqZakxJOoYdjaPnD2SL59hjMSvwlL2tlYm1GgUpld_anr0b29jaUGGIG8oSKYHWHEXOb-q8tNzG9qJFp2FwIDYeHC0EeBKbdnIA84ogddFsb-UPb_aozDtKOwMMrCJvdU6I-LKuiPaJNBGeudRU--y72Ane_IAzvnS4CCtv3yq_hyYfqCJZIxG2xUjgCUHWN83er92hU3RoAtPvNoIZlGUtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!
ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. د
ر ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی»
عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که نزدیک‌ترین فاصله به نقطه نمادین فاجعه جهانی در تاریخ است. این سازمان، تضعیف امنیت بین‌المللی، ضعف چارچوب‌های کنترل تسلیحات و رفتارهای فزاینده پرخاشگرانه قدرت‌های بزرگ را به عنوان دلایل اصلی این تصمیم ذکر کرد.
یکی از واضح‌ترین نشانه‌های این تضعیف، افزایش بکارگیری اصطلاحات هسته‌ای در گفتمان سیاسی و پوشش رسانه‌ای است. عباراتی مانند «حمله هسته‌ای»، «ضربه هسته‌ای»، «تهدید اتمی» و «تشدید هسته‌ای» بسیار بیشتر از چند سال پیش به کار می‌روند. در حالی که عبارت «حمله اتمی» بیشتر با اوایل جنگ سرد مرتبط است، گزارش‌های مدرن ترجیح می‌دهند از اصطلاحاتی مانند «حمله هسته‌ای» و «تهدید هسته‌ای» استفاده کنند. این تغییر نه تنها نشان‌دهنده تغییر زبان، بلکه نگرانی مجددی است که سلاح‌های هسته‌ای دوباره در محاسبات استراتژیک نقش مرکزی پیدا کرده‌اند.
جنگ در اوکراین نقش عمده‌ای در این روند داشته است. از آغاز این درگیری، مقامات روسی بارها امکان استفاده از سلاح‌های هسته‌ای را مطرح کرده‌اند، در حالی که دولت‌های غربی و تحلیلگران درباره اعتبار این تهدیدات بحث کرده‌اند. بولتن به طور خاص اشاره کرده است که جنگ روسیه و اوکراین با تحولات نظامی بی‌ثبات‌کننده و ارجاعات مکرر روسیه به سلاح‌های هسته‌ای همراه بوده است، که خطر محاسبه نادرست بین کشورهای دارای سلاح هسته‌ای را افزایش داده است. شکست‌های نظامی اخیر و فشارهای اقتصادی رو به رشد، بحث‌ها درباره گزینه‌های استراتژیک روسیه را تشدید کرده‌اند. گزارش‌ها و تحلیل‌ها بر فشارهایی که یک درگیری طولانی‌مدت بر تولید صنعتی، تحریم‌ها و زیرساخت‌های انرژی تحمیل کرده است، تأکید داشته‌اند. این فشارها باعث شده است که برخی تحلیلگران گمانه‌زنی کنند که مسکو ممکن است برای بازدارندگی از مداخله بیشتر غرب، بیشتر به سیگنال‌های هسته‌ای متکی شود. با این حال، فعلاً و در شرایط کنونی گمانه‌زنی درباره تصمیمات آینده روسیه نباید با شواهدی مبنی بر استفاده قریب‌الوقوع از سلاح‌های هسته‌ای اشتباه گرفته شود. کارشناسان نظامی و سیاسی عموماً چنین گفتمانی را بیشتر ابزاری برای اجبار و بازدارندگی می‌دانند تا نشانه‌ای قابل اعتماد از استفاده نزدیک از سلاح‌های هسته‌ای. با این حال کمبود گسترده بنزین و گازوئیل یا صف‌های طولانی سوخت در سراسر روسیه  بشدت روی روحیه و غرور ملی روسها تاثیر منفی گذاشته اند و برای نخستین بار از سال 2006 به این سو، مردم روسیه تصور می کنند استانداردهای کیفیت زندگی شان رو به نزول نهاده است. این مسئله روی پوتین و هیات حاکمه روسیه فشار می آورد تا دست به اقدامات تهاجمی تری برای تسلیم کردن اوکراین و ناتو بزنند که یکی از آنها می تواند بهره گیری از سلاحهای کشتار جمعی باشد.
از سوی دیگر، ناکامی نسبی آمریکا در دستیابی به همه اهداف نظامی اش در ایران نیز می تواند از دیگر حوزه هایی باشد که نهایتاً ترامپ را به استفاده از سلاح های هسته ای وادار کند. در این حوزه می توان به اشاره ترامپ به راهبرد «شرمن» استناد کرد که استعاره ای از یک استراتژی ویرانگر مخرب با تلفات بالا برای به تسلیم کشاندن دشمن می باشد. (
لینک
)</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18200" target="_blank">📅 02:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqZ_Llck-7EfLT74WsNfA03WbDmi4NY0xQFdeEw1hEOT81GsJPRtva4B37Q6RQo8AVcKb13f8VMabERtpcQIbaHSFiVhoFSE6XJO6R7QsynlDLt-KSeSTbEZ6H-rTBj62kXpajMTun3XL57QTQGTOn3Ium_ERdkNOKzXiAWluMFMebmmQB_5kwJWC9qJIvYGveUhswm-YHOAOCrMDDe0PR4bnEOnv7BNMTTV-dHa2ZzngMklp6drbdUxWOYz3dxySZL8V2IHkB1GVdVQoRXcCp766pnEmg_AafsN0dfjEI1ESr1GK07YwqfmS0PK-T2oeDoVWT4dySVa8hLQA9N8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در اینجا گفته شد که پوتین مانند گربه ای در گوشه اتاقی بسته گیر افتاده و این خطرناک است</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18199" target="_blank">📅 01:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTVw5VNSfv0r4qBhwTe4qYTDFM7B9CXIbRlgBxbDxS9Q0GL9-YWlFByBm8BhKUeenr8u1xHoDSkXbR9dL9Xm2r7-R-7QFijqCWMabYKxI7U-WXGunrRQ77G_x7KRtDc9lBlr6cHgzdTpstpUOf2moc8O_adNwxEdLAtX7fJMguHJVCOxROhlbsA20d5NtE0_LoLvTxBskp8rqMtLmEQWDuoK903BG-TFX9s7W_teEF21KgWHtsp1lTLNMUnhfa8EWnQ_86u1bNUoOwezFE3i7smp8pAkb7ozKej7GJ0e4UMPfFTdeOoXmyp_5Vq4gC6brzz5Rerp9XUhNU7Sd-0Snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18198" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18197" target="_blank">📅 22:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18196" target="_blank">📅 22:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18195" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امام جمعه کرج:   اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18194" target="_blank">📅 20:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امام جمعه کرج:
اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18193" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">موسسه رتبه‌بندی فیچ، ریسک‌های مرتبط با ایران برای بخش‌های شرکتی در سطح جهان را مجدداً ارزیابی کرد
از دید این موسسه، شکنندگی توافق موقت ۶۰ روزه، به همراه عدم مشارکت اسرائیل، نشان می‌دهد که درگیری خاورمیانه همچنان تهدیدی برای صادرکنندگان شرکتی محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18192" target="_blank">📅 20:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18191" target="_blank">📅 20:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18190" target="_blank">📅 20:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUJJy6j5l2ytvijwowsqqfcXGG4fQwe-H8eQ0isyaEnBPN8sQM1KPudMAbbsQn6d865ZdFBCuRU08I6tjMP9If8uA6M7Q_BkmUxP5bKFHBSuxK6wYDjD0jM2l5RqEzc5bnRyJfttTv3cVqhJD3Vp2DnoKhRD_hzntkJeHhMqBe04eiDhofbxDpMmv86oxCYYe56P9JkdQhLr5NCNwo6ZwTYr1NxHaPHLW-pB8rddifgAlMtQj9ZuQsq-T8N1gE1QGszLgxhaOgSlw92FpjfjbLuiG85bllLrb9dKQzbJXUrQkmeub2icGiPahuCkW1cde4nwJPKLr4Jn_veVRLLtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی ساختمان عظیم وزارت دفاع مصر!
افتتاح مجموعه «هشت‌ضلعی» (The Octagon) به‌عنوان مقر جدید وزارت دفاع و فرماندهی راهبردی مصر را می‌توان یکی از مهم‌ترین نمادهای تحول ساختاری نیروهای مسلح این کشور در دهه اخیر دانست. این مجموعه عظیم که در پایتخت اداری جدید مصر ساخته شده، قرار است تمامی ستادهای اصلی نیروهای مسلح را در یک مرکز واحد گرد هم آورد و با بهره‌گیری از سامانه‌های پیشرفته فرماندهی، کنترل، ارتباطات و مدیریت اطلاعات، سرعت و هماهنگی تصمیم‌گیری‌های نظامی را به شکل قابل توجهی افزایش دهد.
ساخت چنین مرکزی تنها یک پروژه عمرانی نیست، بلکه بخشی از راهبرد بلندمدت قاهره برای تبدیل ارتش مصر به نیرویی مدرن، شبکه‌محور و آماده مقابله با تهدیدات متنوع منطقه‌ای است. طی سال‌های گذشته، مصر سرمایه‌گذاری گسترده‌ای در نوسازی تجهیزات نظامی، توسعه صنایع دفاعی و خرید سامانه‌های پیشرفته از کشورهای مختلف انجام داده و اکنون ایجاد یک مرکز فرماندهی یکپارچه، حلقه تکمیل‌کننده این روند محسوب می‌شود.
از منظر ژئوپلیتیکی نیز افتتاح «هشت‌ضلعی» پیام مهمی برای بازیگران منطقه دارد. مصر در سال‌های اخیر تلاش کرده جایگاه خود را به‌عنوان یکی از قدرت‌های اصلی نظامی و امنیتی خاورمیانه و شمال آفریقا تثبیت کند. تمرکز فرماندهی نیروهای زمینی، دریایی، هوایی و پدافندی در یک مجموعه واحد، ضمن افزایش کارآمدی عملیاتی، توان مدیریت بحران‌های هم‌زمان در جبهه‌های مختلف را نیز تقویت می‌کند.
همزمان، انتقال وزارت دفاع از مرکز سنتی قاهره به پایتخت اداری جدید، نشان‌دهنده اهمیت این شهر در ساختار آینده حکومت مصر است. دولت مصر با انتقال تدریجی نهادهای حاکمیتی به این شهر، در پی ایجاد مرکز سیاسی، اداری و امنیتی جدیدی است که از زیرساخت‌های مدرن و استانداردهای بالای حفاظتی برخوردار باشد.
در مجموع، افتتاح «هشت‌ضلعی» را باید فراتر از افتتاح یک ساختمان نظامی ارزیابی کرد؛ این پروژه نماد ورود نیروهای مسلح مصر به مرحله‌ای جدید از سازماندهی، فرماندهی و آمادگی عملیاتی است و می‌تواند بر موازنه قدرت و معادلات امنیتی منطقه نیز تأثیرگذار باشد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18189" target="_blank">📅 20:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حوثی ها می‌گویند جنگنده‌های سعودی را از آسمان یمن بیرون کردند زیرا سعی در جلوگیری از فرود یک هواپیمای مسافربری ایرانی در صنعا داشتند.
آن‌ها هشدار دادند که اقدامات آینده سعودی با حملات به فرودگاه‌های سعودی و سایر اهداف حیاتی پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18188" target="_blank">📅 18:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از زمانی که روس‌ها تلگرام را محدود کرده اند و ایلان ماسک هم استفاده دزدانه شان از استارلینک را محدود کرده، توان آفندی پهپادی ارتش ظفرنمون مسکووی بشدت کاهش یافته است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18187" target="_blank">📅 16:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسرائیلی ها، تاسیس پایگاه نظامی از سوی ترکیه در عمق خاک سوریه را به عنوان تهدیدی برای خود ارزیابی می کنند!  حملات ویرانگر اسرائیل ضد پایگاه T-4 نیز در همین راستا ارزیابی می شود.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18186" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmczTFvttBCF8a_KvBhRxZeaoi4KPze4kFjmoeQhrphATl5N6FTNVKXX_txiqEkT83e3NCtwB8nQUGFyP0iMDWCvA1oxZQrLVv6MwvOg3zMOwqeDHe9Pu72t_JTRgWr9KJRlTV6YzNT0r6nxS9KVDB2nWrUdfAl3O3Tkx1s-7Jb7JGrIN2gvqBSFrLJL-OY8Mg8PksLNQyeXMWkdDHT8qmn7_a6v0mCp0wj4N9ju7FNjJ6GjRmUpWkcmyWatyo3s_QsDNK6tow7V6IV3y7Fnjrp39ZivrpkWb-uU0RamykfrBh-XcKc5xc5nrnjeFDJF3lC8E45V4brRex34UhFovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18185" target="_blank">📅 13:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-poll">
<h4>📊 مدت زمان و محتوای پادکست مطلوب است:</h4>
<ul>
<li>✓ کوتاه تر — بازاری تر</li>
<li>✓ کوتاه تر — بدون تغییر محتوا</li>
<li>✓ بدون تغییر در مدت زمان — بازاری تر</li>
<li>✓ بدون تغییر در مدت زمان و محتوا</li>
</ul>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18184" target="_blank">📅 11:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 1
جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18183" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18182">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjphGPh-g14jn8aeNGweNUslDekmniud58qIGFW0uw9UtgoOrr7a9ZhIUUTGhwwuPR6e7LNkQv_pp7n2QWbtdhYydYj6m8f9MWHgpq6qKoZ20plCFGyqOwltsTn4kglZT7ccU58jZVpiXXtIS-vAq9eB7M80KFO4GTZYohUKPdP1uudUpERsreLK_WjWp286eJmvkVd5PHX90hEGvyc0jyNXt1kSizGoRNaDw5MN89wlwQ9BccIBYkA7dON3-g9slNhoELpFi73thGViJEWo1Ot6dgC57Wsi645MNcx5_OJdVTeDNHbsYNHBxjXRIcmFuW3QtOxWUB433uj_aPtwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز نسبتاً پایین است و ریسک پذیری ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18182" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18181" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18180" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18179">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18179" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18178">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQzYrbBmmoHDt8uMSFiV1ocv4IamsAYIpR4TsF2NUzFcCAdoK042l_pYQkEA5qcAc4L_2osmn_JCumQATFpIujrAByRDEPUOCauutBMfym9m8LjbgyLKh_5XRWKTskS5ORA8AoSqvdHJZ4YoZgtNs4fKB9pF2zNu8_r0JsBu5kVGf4-ibAyMQh3kA7GjbtmZyVQHIVxm5q0W3mpGpVv9eMRXbYmGOkv4BLvTwHHttyv3vfSBYWO7oqV9fLdky-mFz7OSOqLqWPlnJMdaMDo2_VDDv_gvHm_Cy8JBloD4k-VwXjFJs96qHxZj1c3edo9psjZCQGjYrwVM0wyiY3Fxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18178" target="_blank">📅 10:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید
همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای انتحاری و سامانه‌های شناسایی گرفته تا تولید مشترک برخی تجهیزات نظامی در خاک مراکش، شواهد نشان می‌دهد که تل‌آویو در حال سرمایه‌گذاری بلندمدت بر ارتقای توان نظامی رباط است.
این تحول زمانی اهمیت بیشتری پیدا می‌کند که در کنار سردی بی‌سابقه روابط اسرائیل و دولت چپ‌گرای اسپانیا قرار گیرد. دولت مادرید در دو سال گذشته از منتقدان جدی سیاست‌های اسرائیل در غزه بوده، از به رسمیت شناختن کشور فلسطین حمایت کرده و در مجامع بین‌المللی مواضعی اتخاذ کرده که با مخالفت شدید تل‌آویو روبه‌رو شده است. (لینک ها:
یک
|
دو
|
سه
) طبیعی است که این تنش سیاسی، بر محاسبات راهبردی اسرائیل نیز تأثیر بگذارد.
در چنین فضایی، افزایش توان نظامی مراکش پیامدهایی فراتر از شمال آفریقا دارد. مراکش همچنان ادعای حاکمیت بر سئوتا، ملیله و چند قلمرو اسپانیا در سواحل آفریقا را حفظ کرده است. هرچند رباط بارها تأکید کرده که این موضوع را از مسیرهای سیاسی دنبال می‌کند، اما از نگاه بسیاری از ناظران اسپانیایی، تجهیز ارتش مراکش با فناوری‌های پیشرفته اسرائیلی، موازنه قوا در غرب مدیترانه را به زیان اسپانیا تغییر می‌دهد. پرسش نمایندگان حزب راست گرای Vox ووکس در پارلمان اسپانیا درباره آمادگی این کشور در برابر پهپادهای انتحاری ساخت مشترک اسرائیل و مراکش نیز بازتاب همین نگرانی است.
سیاست بین‌الملل، برداشت بازیگران نیز به اندازه نیت آنها اهمیت دارد. حتی اگر انگیزه اصلی اسرائیل اقتصادی یا ژئوپلیتیکی باشد، نتیجه عملی آن افزایش فشار امنیتی بر کشوری است که در سال‌های اخیر یکی از منتقدان اصلی سیاست‌های تل‌آویو در اروپا بوده است. از این منظر، تسلیح مراکش را می‌توان نه لزوماً «مجازات» اسپانیا، بلکه پیامی راهبردی در راستای بازآرایی موازنه قدرت در غرب مدیترانه دانست؛ بازآرایی‌ای که به‌طور طبیعی هزینه‌های راهبردی بیشتری را بر مادرید تحمیل می‌کند و می‌تواند بر محاسبات آینده دولت اسپانیا در قبال اسرائیل نیز اثرگذار باشد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18177" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=fhPcvlpzGLX1AJ-qbkB9NF4bQRs3xXSxOjeowYSnp4JlpBAk7CU0p0QRatjFhpcINDHT2KGlwJpcnyRPXEST5fgCJvW47FDD3KS5RNlhpuA68SZ6Ev-sxfpoUzIGkqjxIxK-TiQUosP7DXPw_WcxwXjjTn8o8hbd1gFpLktfIeaQXI8HBUFNZKydFTaJY7bJkvN7gwKPP-PTmQvS4PKlZr8dwfCoYTv1Q_mZcGBTY7GbCDQf9NB8szT79EyqfZS9d6YG54RHTzRPAK_vxPYaJW-0lBJC52vm_TFIjBASHaxdyApysopf7AR-62cYbzCff2GJz9UbUMzteg8iUeF41w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=fhPcvlpzGLX1AJ-qbkB9NF4bQRs3xXSxOjeowYSnp4JlpBAk7CU0p0QRatjFhpcINDHT2KGlwJpcnyRPXEST5fgCJvW47FDD3KS5RNlhpuA68SZ6Ev-sxfpoUzIGkqjxIxK-TiQUosP7DXPw_WcxwXjjTn8o8hbd1gFpLktfIeaQXI8HBUFNZKydFTaJY7bJkvN7gwKPP-PTmQvS4PKlZr8dwfCoYTv1Q_mZcGBTY7GbCDQf9NB8szT79EyqfZS9d6YG54RHTzRPAK_vxPYaJW-0lBJC52vm_TFIjBASHaxdyApysopf7AR-62cYbzCff2GJz9UbUMzteg8iUeF41w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.  ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18176" target="_blank">📅 01:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18175" target="_blank">📅 01:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.
با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را دوباره شعله‌ور کند، واشنگتن از کشورهای منطقه خواست تا ایران را از این خطر آگاه کنند.
ایران اقدامات امنیتی گسترده‌ای برای محافظت از هیئت خود انجام داد، از جمله اسکورت نظامی و تغییر برنامه‌های سفر پس از دریافت اطلاعاتی درباره احتمال حمله اسرائیلی.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18174" target="_blank">📅 22:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-poll">
<h4>📊 در‌ جنگ میان ترکیه و اسراییل دوست دارید:</h4>
<ul>
<li>✓ پیروزی ترکیه</li>
<li>✓ پیروزی اسراییل</li>
<li>✓ جنگ فرسایشی بدون برنده</li>
<li>✓ من Gay هستم و دوست دارم جنگ نشود</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18173" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18172" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر امور خارجه ترکیه، هاکان فیدان:
سیاستمداران آمریکایی تا زمانی که حمایت از اسرائیل به منافع خودشان خدمت کند، از اسرائیل حمایت می‌کنند.
این پویایی آن‌قدر طولانی شده است که همسویی بین حمایت از اسرائیل و پیشبرد منافع ایالات متحده به عنوان یک فرض دائمی تلقی شده است.
با این حال، برای اولین بار از زمان نسل‌کشی در غزه، تحلیل‌هایی که ظهور کرده‌اند به نتیجه متفاوتی اشاره دارند: «سیستم موجود در حال کار علیه منافع ماست.»
هیچ‌کس ادامه سیستمی را نمی‌خواهد که در نهایت علیه منافع خودشان کار می‌کند.
در سراسر جهان، از دانشگاه‌ها تا روزنامه‌ها، احساسات ضد اسرائیلی به‌طور چشمگیری افزایش یافته است.
چرا؟ زیرا مردم می‌بینند که اسرائیل آشکارا در حال ارتکاب کشتار است و در هر جایی که اقدام می‌کند، نقش بی‌ثبات‌کننده‌ای ایفا می‌کند.
در گذشته، آن‌ها می‌توانستند این موضوع را با چند مانور رسانه‌ای ساده پنهان کنند. اکنون، دیگر نمی‌توانند آن را پنهان نگه دارند.
اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
تا زمانی که اسرائیل — یا هر بازیگر دیگری — به روش‌هایی عمل کند که با منافع ملی و منطقه‌ای ما در تضاد است، ما هیچ دلیلی برای ترسیدن، مردد شدن یا عقب‌نشینی نداریم.
ما مشکلی با رویارویی نداریم. اگر به آنجا برسد، برای ما مسئله‌ای نیست.
اسرائیل فقط مشکل من نیست؛ مشکل جهان است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18171" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر دفاع اسرائیل:
ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18170" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عبدالمجید حکیم الهی، نماینده رهبر ایران در هند، گفت که به دلیل نگرانی‌های امنیتی، بعید است آیت الله مجتبی خامنه‌ای در مراسم تشییع جنازه پدرش شرکت کند.
وی افزود که آیت الله مجتبی خامنه‌ای مایل بود نماز میت را اقامه کند، اما مقامات امنیتی این کار را بسیار خطرناک دانسته‌اند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18169" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تولید نفت خام کویت در ژوئن به طور میانگین ۱.۶۵ میلیون بشکه در روز بود در مقابل ۵۷۸,۰۰۰ بشکه در روز در ماه مه</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18168" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🩵
کاتز ؛ وزیردفاع دولت اسرائیل
:
ما درحال توسعه لیزرهای فضایی برای تهاجم خارج از جو زمین هستیم
يسرائيل كاتز ،  اعلام کرد دولت اسرائیل در حال توسعه لیزرهای فضایی به منظور توانایی حمله در فضا است.
به گزارش اورشلیم ،پست کاتز در نشستی با خبرنگاران نظامی گفت: یکی از اهداف اصلی که نخست وزیر و من تعیین کرده ایم این است که برترین استعدادها را جذب کنیم تا امروز هیچ کشوری توانایی اجرای حمله در فضا را نداشته است. ما باید در برخورداری از این توانایی کشور پیشرو جهان باشیم
او افزود: اگر به این هدف دست یابیم این امر میتواند برتری بازدارندگی، توانایی حمله و انهدام و دیگر برتری های راهبردی ما را در برابر دشمنانی که از منابع گسترده برخوردارند تضمین کند
کاتز پنجشنبه گذشته گفته بود اسرائیل مصمم است به بازیگر پیشرو در زمینه توانایی حمله از فضا تبدیل شود با این حال این نخستین بار بود که به طور مشخص از لیزرهای فضایی نام می برد
اسرائیل هم اکنون نیز در این حوزه از کشورهای پیشرو به شمار میرود و سامانه موسوم به پرتو آهنین (Iron Beam) را به عنوان یک لیزر فضایی مستقر در زمین تولید کرده است
سامانه پرتو آهنین که اواخر سال گذشته به ارتش اسرائیل تحویل داده شد نقطه عطفی تاریخی به شمار میرود زیرا نخستین سامانه دفاع لیزری عملیاتی جهان است که میتواند راکتها پهپادها و خمپاره ها را با هزینه ای بسیار کمتر از رهگیرهای سنتی، خنثی کند</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18167" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فرمانده سپاه پاسداران قم
:
تمهیدات زیادی اتخاذ کردیم اما بصورت قطعی نمی‌دانیم در مراسم تشییع رهبرانقلاب چه اتفاقی خواهد افتاد</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18166" target="_blank">📅 15:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه (۱۶ روز دیگر) آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18165" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
غضنفری ؛ نماینده مجلس
:
یک شبه کودتای سیاسی علیه رهبری نظام درجریان است - تجمعات شبانه نباید جمع شود</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18164" target="_blank">📅 13:33 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
