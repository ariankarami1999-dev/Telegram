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
<img src="https://cdn4.telesco.pe/file/N6RxhacZtHkJGaCRAUBkbsO2QX6IQ0j-tpj0X1r4xj97M_Ya6GUzLcrR3E8GPZZKt1oOzyj4GEHyUI8XQGuBMf2CJ6UthhN5lKeQZzWdti0MjVpdmUFOfDHgGw0N2jcLUpbReEgE3JxzOLvMq1OUyEPtLzJ9eEWMBvO7ezoPRpijI4he8uNwyMrG3EgNweTb289azJi6C_6cucMD1yZ6OM1aSM9slbUPvpfLgACiP_PM_YCntTX0zzWiIktzV5cXvobMLYDdCDMQFHmgdW75Kh0VVHjMk4LWosy70_noOOZ68dubuoO9jnxQgIO0WPlXRsLzNpkPEiIleDUX50aeGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr88eFVpnYz3Vb9w1m83hfU7FBoAW282mc0VSjoIKvYa-sMAUn0jp05pITIky0Fj1fA3t9dvqBdN3A2qSpedZnOll13gUU_RHKMav8IqL8uYSLvFcFFasCgWhCOGt50hu-Ezdg1SpKStpk1v1MqyJhJE3oUq3dEFYz26SsTA6Ov7J4QZ_Ka0nhfdbReD4X16HMFrSGXljUX_SiVoSvt4mz9ohWqcBavbbkE0bczic_RuNIdAm8AXZKw3UfzJMbuTtz-25_cdJEz3IBdS7x2vb5j0dIAtqdNc-Qn0unuLfNavitzZVJwTWT4n0gZ8T2OrtO_E5GDRd0FyGFzTz-X-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!
ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. د
ر ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی»
عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که نزدیک‌ترین فاصله به نقطه نمادین فاجعه جهانی در تاریخ است. این سازمان، تضعیف امنیت بین‌المللی، ضعف چارچوب‌های کنترل تسلیحات و رفتارهای فزاینده پرخاشگرانه قدرت‌های بزرگ را به عنوان دلایل اصلی این تصمیم ذکر کرد.
یکی از واضح‌ترین نشانه‌های این تضعیف، افزایش بکارگیری اصطلاحات هسته‌ای در گفتمان سیاسی و پوشش رسانه‌ای است. عباراتی مانند «حمله هسته‌ای»، «ضربه هسته‌ای»، «تهدید اتمی» و «تشدید هسته‌ای» بسیار بیشتر از چند سال پیش به کار می‌روند. در حالی که عبارت «حمله اتمی» بیشتر با اوایل جنگ سرد مرتبط است، گزارش‌های مدرن ترجیح می‌دهند از اصطلاحاتی مانند «حمله هسته‌ای» و «تهدید هسته‌ای» استفاده کنند. این تغییر نه تنها نشان‌دهنده تغییر زبان، بلکه نگرانی مجددی است که سلاح‌های هسته‌ای دوباره در محاسبات استراتژیک نقش مرکزی پیدا کرده‌اند.
جنگ در اوکراین نقش عمده‌ای در این روند داشته است. از آغاز این درگیری، مقامات روسی بارها امکان استفاده از سلاح‌های هسته‌ای را مطرح کرده‌اند، در حالی که دولت‌های غربی و تحلیلگران درباره اعتبار این تهدیدات بحث کرده‌اند. بولتن به طور خاص اشاره کرده است که جنگ روسیه و اوکراین با تحولات نظامی بی‌ثبات‌کننده و ارجاعات مکرر روسیه به سلاح‌های هسته‌ای همراه بوده است، که خطر محاسبه نادرست بین کشورهای دارای سلاح هسته‌ای را افزایش داده است. شکست‌های نظامی اخیر و فشارهای اقتصادی رو به رشد، بحث‌ها درباره گزینه‌های استراتژیک روسیه را تشدید کرده‌اند. گزارش‌ها و تحلیل‌ها بر فشارهایی که یک درگیری طولانی‌مدت بر تولید صنعتی، تحریم‌ها و زیرساخت‌های انرژی تحمیل کرده است، تأکید داشته‌اند. این فشارها باعث شده است که برخی تحلیلگران گمانه‌زنی کنند که مسکو ممکن است برای بازدارندگی از مداخله بیشتر غرب، بیشتر به سیگنال‌های هسته‌ای متکی شود. با این حال، فعلاً و در شرایط کنونی گمانه‌زنی درباره تصمیمات آینده روسیه نباید با شواهدی مبنی بر استفاده قریب‌الوقوع از سلاح‌های هسته‌ای اشتباه گرفته شود. کارشناسان نظامی و سیاسی عموماً چنین گفتمانی را بیشتر ابزاری برای اجبار و بازدارندگی می‌دانند تا نشانه‌ای قابل اعتماد از استفاده نزدیک از سلاح‌های هسته‌ای. با این حال کمبود گسترده بنزین و گازوئیل یا صف‌های طولانی سوخت در سراسر روسیه  بشدت روی روحیه و غرور ملی روسها تاثیر منفی گذاشته اند و برای نخستین بار از سال 2006 به این سو، مردم روسیه تصور می کنند استانداردهای کیفیت زندگی شان رو به نزول نهاده است. این مسئله روی پوتین و هیات حاکمه روسیه فشار می آورد تا دست به اقدامات تهاجمی تری برای تسلیم کردن اوکراین و ناتو بزنند که یکی از آنها می تواند بهره گیری از سلاحهای کشتار جمعی باشد.
از سوی دیگر، ناکامی نسبی آمریکا در دستیابی به همه اهداف نظامی اش در ایران نیز می تواند از دیگر حوزه هایی باشد که نهایتاً ترامپ را به استفاده از سلاح های هسته ای وادار کند. در این حوزه می توان به اشاره ترامپ به راهبرد «شرمن» استناد کرد که استعاره ای از یک استراتژی ویرانگر مخرب با تلفات بالا برای به تسلیم کشاندن دشمن می باشد. (
لینک
)</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/18200" target="_blank">📅 02:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne2WZNFn4MKGm3usXSlrlA1tSGJ_Y4jyz__ECngK3fLW0C584eUwuNsV-k7A6GNw7SpOZPZzEFjBHOBDxTP7dOsTSlzFqGcs60teYXYxqg8DiJ8OwdZYhWsWJL3XYeexsrFVOkqN6UbQ44xTUDrLb-vwix1uDhuL1D81Mx15UOFIZTLJPSUb2XU0XqbwBJt9cXeK8dCdKcCNUqZC31Ykm2tsNXSsrhyOdiJqcOr4ikIgRhcD62AUOTES28d-V0y-nH1pVnovRcBKYxsAwYtnP3xDRQh5KjAjOUMXemOK1s1Q5wZhgj_jq-1hs6VUl9PGu0wv1ihYJhEvcgB3MTOSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در اینجا گفته شد که پوتین مانند گربه ای در گوشه اتاقی بسته گیر افتاده و این خطرناک است</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/18199" target="_blank">📅 01:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2rqG05HSdtBqW_u-0q9D3ollqaYkS7U_0AmnPPUlP0eviRJvGD9jRdoJXY86hc0KdmprTe2UzJx7J7uyRvj4dTYMGJxmxY-vWn9953avdTlv73kerJfqs3tq3Zv_VnnNTvL5Y7BzlDuHbCRPc0aX47xdQIXlN6Zsn95dJmcotpXhunNqZb_6NWZ68k939q45jYUoZnJ95PGAX9KLAG7jTwr7H8qtKQQCz0fPCAOBDosbtWPPStG1OHlXVEUQ8-jITTsdwojjJgNW-lxmZXBgFiyS_Kzt-i6Ryb4JBKKKlXpz1VXNGlOwOZJI8muXcHIbG18AFCjdxKimlAgmU-yGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/18198" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18197" target="_blank">📅 22:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18196" target="_blank">📅 22:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/18195" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امام جمعه کرج:   اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18194" target="_blank">📅 20:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امام جمعه کرج:
اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18193" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">موسسه رتبه‌بندی فیچ، ریسک‌های مرتبط با ایران برای بخش‌های شرکتی در سطح جهان را مجدداً ارزیابی کرد
از دید این موسسه، شکنندگی توافق موقت ۶۰ روزه، به همراه عدم مشارکت اسرائیل، نشان می‌دهد که درگیری خاورمیانه همچنان تهدیدی برای صادرکنندگان شرکتی محسوب می‌شود.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/18192" target="_blank">📅 20:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18191" target="_blank">📅 20:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18190" target="_blank">📅 20:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOajQDlmbdc-XCYiLT1Fn4V48TrZvNdO5Be60ChsPCeIW-lKKgpZD1Jjbjxo5ekoJwK3f7FWlZp_WmrTm93sv4w3RX80yPPHdhqAQrZrIN3oMr_CrqqAPfn5QRdVS23W34Pox91xhvQXaBn76S_DbjYujQhJogIYd4czbsvspJVqZ1Jd7gl_7PXAswRtgN0bl22R9DDx9nWiIGaxaM2rTNuShDlk8rFLZr5ts4kTUR6rjDb_ip69m9YHwmUWr1l4HxBkb2vtLq1Ht5zpTWTUzZTCzZBiYjQOmRg3Kgmx3Wd2R_0xmn_4PyYpgGkfntplQt-PgY4fIhcNRvKVA0LWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی ساختمان عظیم وزارت دفاع مصر!
افتتاح مجموعه «هشت‌ضلعی» (The Octagon) به‌عنوان مقر جدید وزارت دفاع و فرماندهی راهبردی مصر را می‌توان یکی از مهم‌ترین نمادهای تحول ساختاری نیروهای مسلح این کشور در دهه اخیر دانست. این مجموعه عظیم که در پایتخت اداری جدید مصر ساخته شده، قرار است تمامی ستادهای اصلی نیروهای مسلح را در یک مرکز واحد گرد هم آورد و با بهره‌گیری از سامانه‌های پیشرفته فرماندهی، کنترل، ارتباطات و مدیریت اطلاعات، سرعت و هماهنگی تصمیم‌گیری‌های نظامی را به شکل قابل توجهی افزایش دهد.
ساخت چنین مرکزی تنها یک پروژه عمرانی نیست، بلکه بخشی از راهبرد بلندمدت قاهره برای تبدیل ارتش مصر به نیرویی مدرن، شبکه‌محور و آماده مقابله با تهدیدات متنوع منطقه‌ای است. طی سال‌های گذشته، مصر سرمایه‌گذاری گسترده‌ای در نوسازی تجهیزات نظامی، توسعه صنایع دفاعی و خرید سامانه‌های پیشرفته از کشورهای مختلف انجام داده و اکنون ایجاد یک مرکز فرماندهی یکپارچه، حلقه تکمیل‌کننده این روند محسوب می‌شود.
از منظر ژئوپلیتیکی نیز افتتاح «هشت‌ضلعی» پیام مهمی برای بازیگران منطقه دارد. مصر در سال‌های اخیر تلاش کرده جایگاه خود را به‌عنوان یکی از قدرت‌های اصلی نظامی و امنیتی خاورمیانه و شمال آفریقا تثبیت کند. تمرکز فرماندهی نیروهای زمینی، دریایی، هوایی و پدافندی در یک مجموعه واحد، ضمن افزایش کارآمدی عملیاتی، توان مدیریت بحران‌های هم‌زمان در جبهه‌های مختلف را نیز تقویت می‌کند.
همزمان، انتقال وزارت دفاع از مرکز سنتی قاهره به پایتخت اداری جدید، نشان‌دهنده اهمیت این شهر در ساختار آینده حکومت مصر است. دولت مصر با انتقال تدریجی نهادهای حاکمیتی به این شهر، در پی ایجاد مرکز سیاسی، اداری و امنیتی جدیدی است که از زیرساخت‌های مدرن و استانداردهای بالای حفاظتی برخوردار باشد.
در مجموع، افتتاح «هشت‌ضلعی» را باید فراتر از افتتاح یک ساختمان نظامی ارزیابی کرد؛ این پروژه نماد ورود نیروهای مسلح مصر به مرحله‌ای جدید از سازماندهی، فرماندهی و آمادگی عملیاتی است و می‌تواند بر موازنه قدرت و معادلات امنیتی منطقه نیز تأثیرگذار باشد.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18189" target="_blank">📅 20:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حوثی ها می‌گویند جنگنده‌های سعودی را از آسمان یمن بیرون کردند زیرا سعی در جلوگیری از فرود یک هواپیمای مسافربری ایرانی در صنعا داشتند.
آن‌ها هشدار دادند که اقدامات آینده سعودی با حملات به فرودگاه‌های سعودی و سایر اهداف حیاتی پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/18188" target="_blank">📅 18:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از زمانی که روس‌ها تلگرام را محدود کرده اند و ایلان ماسک هم استفاده دزدانه شان از استارلینک را محدود کرده، توان آفندی پهپادی ارتش ظفرنمون مسکووی بشدت کاهش یافته است.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18187" target="_blank">📅 16:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18186">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسرائیلی ها، تاسیس پایگاه نظامی از سوی ترکیه در عمق خاک سوریه را به عنوان تهدیدی برای خود ارزیابی می کنند!  حملات ویرانگر اسرائیل ضد پایگاه T-4 نیز در همین راستا ارزیابی می شود.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18186" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18185">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me_UESyyVIEXIyHBiN6snRWsBeFz3PYVtrJtO4mRuqwXRRkOH4aN7azCOwme7rdArNW5SN6QmiJzts9b_N84rtY1q8OLrePjVjb-T7RKmUe_dXvge7K8X_0zP86YLtYEdMii0G_Eczw3kw_RleWF97l43lCxleHXLMpDY5J-wwIGfj47bWUKG81AUXh1F9osxA0SQ3pd_tC2m9Rco9Ii-OYoFWuGJA21BL7lHqseptS5TVnyGhNtsZsOb4mLJc5Ib9dSnl0YCzJ1iscQ8qlJV5iP3A-r_npOHuSVjK-L1Kuu0QQuIrHz97u83YLoKlyE3L3DWLEU-2Q6tunwxoH7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18185" target="_blank">📅 13:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18184">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18184" target="_blank">📅 11:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18183">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18183" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18182">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx1fJOcFlwUMp4X-HaYzAzCf2eSuygIxMLhPwAncYNXcPjKDcJoLlTIVDJyVlDRaXTO9k1hHKX3VGAXnjpg2Z2gQLxdsgQgtEKY0nuqL9yPltrgZt2GXoDKaaYXj1tFAV-lG09CH7ViSL-YmED-UFmBPPL1OzvwSCNqhu1mGbbfjgUOglXtvM5p_4l3n9qUfSbelS9UkkXz1yjLPelUuJAlVdu9TPXf5-EANtDbgSrsBNmLAXhgLLNPFTCjtFq4DobGzxVxy-jzRUmf-1I33FnsffRs3ypFlMTpFICtYIrz1VfzBn-yPgDr_yBVWhA0JIIxZtv4ir-uiQ1_nfKOVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز نسبتاً پایین است و ریسک پذیری ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18182" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18181">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18181" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18180">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18180" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18179">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18179" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18178">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-B-AkzlM-xvmloCW2lL0sjmU4SuhIXF-z2AohTqP-ReLvqh7QrRUpUzKtEjcjUWyTQ_l7h7dWDUU9jylXreJkKMQ3PuNf_4Tsd7VKlT32tyx413KfDgO9TTBDjw7ZXwOAi3S0QkD71R3eM11jme3IeWkOm6zoETGgYnIHGBR2fgciXUfjGqB84MEtWjOZEqr3kHk1qHFhk_LfWtQdqTpOdwC3A-PJ-em8lY9rxHetL4aEzXgjWzkiUle1So-WrtMFyPakW3MmqXGopBsqKeqr4F1wyKr6STSWqqx3sQFTUE2cpJ5knZnBzALl13is3HPZH_q9j2-z5nWU6HZ0bk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18178" target="_blank">📅 10:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18177">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18177" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18176">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=TfZzUJvU3jJ3_C7ilS8sybfvt6T7Y5mZ1lV-Y3h4Vxwd09DTGcAsVFi8vJhGZerNxE1NcGlOqpX7DMCJnadjeO8ekH2Dn5xPPyGJk7ohKAGgW_SkjYMQ_2p-UrKQUtY-YU-DY-ylfyS2QZOcemO64b9fXT8M7VGP6ttt8UL-D8y5EpTn9M_0zt1mGr1ppQAyUBae-Tg4hYL5aVP1hhMKuS66lRoWZb2vACjs2n2BV5OC0sp75Jl6u4hrGlfOzQcDmYSAVyipQfnNWOp07tW6p5m4mGju_sFv3tERA7W-HIYC0sWkuWs_ws6ArKGhKI5brQGrC_9NmTj0GdQ17txFIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=TfZzUJvU3jJ3_C7ilS8sybfvt6T7Y5mZ1lV-Y3h4Vxwd09DTGcAsVFi8vJhGZerNxE1NcGlOqpX7DMCJnadjeO8ekH2Dn5xPPyGJk7ohKAGgW_SkjYMQ_2p-UrKQUtY-YU-DY-ylfyS2QZOcemO64b9fXT8M7VGP6ttt8UL-D8y5EpTn9M_0zt1mGr1ppQAyUBae-Tg4hYL5aVP1hhMKuS66lRoWZb2vACjs2n2BV5OC0sp75Jl6u4hrGlfOzQcDmYSAVyipQfnNWOp07tW6p5m4mGju_sFv3tERA7W-HIYC0sWkuWs_ws6ArKGhKI5brQGrC_9NmTj0GdQ17txFIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.  ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18176" target="_blank">📅 01:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18175">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:
ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18175" target="_blank">📅 01:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18174">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.
با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را دوباره شعله‌ور کند، واشنگتن از کشورهای منطقه خواست تا ایران را از این خطر آگاه کنند.
ایران اقدامات امنیتی گسترده‌ای برای محافظت از هیئت خود انجام داد، از جمله اسکورت نظامی و تغییر برنامه‌های سفر پس از دریافت اطلاعاتی درباره احتمال حمله اسرائیلی.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18174" target="_blank">📅 22:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18173">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-poll">
<h4>📊 در‌ جنگ میان ترکیه و اسراییل دوست دارید:</h4>
<ul>
<li>✓ پیروزی ترکیه</li>
<li>✓ پیروزی اسراییل</li>
<li>✓ جنگ فرسایشی بدون برنده</li>
<li>✓ من Gay هستم و دوست دارم جنگ نشود</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18173" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18172">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18172" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18171">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18171" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18170">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر دفاع اسرائیل:
ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18170" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18169">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عبدالمجید حکیم الهی، نماینده رهبر ایران در هند، گفت که به دلیل نگرانی‌های امنیتی، بعید است آیت الله مجتبی خامنه‌ای در مراسم تشییع جنازه پدرش شرکت کند.
وی افزود که آیت الله مجتبی خامنه‌ای مایل بود نماز میت را اقامه کند، اما مقامات امنیتی این کار را بسیار خطرناک دانسته‌اند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18169" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18168">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تولید نفت خام کویت در ژوئن به طور میانگین ۱.۶۵ میلیون بشکه در روز بود در مقابل ۵۷۸,۰۰۰ بشکه در روز در ماه مه</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18168" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18167" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فرمانده سپاه پاسداران قم
:
تمهیدات زیادی اتخاذ کردیم اما بصورت قطعی نمی‌دانیم در مراسم تشییع رهبرانقلاب چه اتفاقی خواهد افتاد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18166" target="_blank">📅 15:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه (۱۶ روز دیگر) آغاز می‌شود.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18165" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
غضنفری ؛ نماینده مجلس
:
یک شبه کودتای سیاسی علیه رهبری نظام درجریان است - تجمعات شبانه نباید جمع شود</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18164" target="_blank">📅 13:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دلار ۱۷۷۰۰۰ تومان!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18163" target="_blank">📅 11:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFzYwN7OT9exif9HZqITHofJdJldWy-KKqSOs8pL1vR6IyoTt3lWq2h7fay2-CV9JVFoyt_oYFl3n8nCZzXCaKNekLF0OpNmsA5W2nlEyIVNU0M8wUaPdsZAYffHOsHJJ_XsS_pEzEsVwIu0yDD5gXR4ObiAi_f1GmbQJ5PVVJ7Z9nMQsloEhFytK7B7xj2jvWbbAvQlt-TmcyNE0XboMuRamEHWtStatM1zUBtZfn7kYQ6X_2p5xL20emd9fjjQ7gjKpCUPhOIz9sxdDXEZb-84TpNaKJiogD8bJEnC37yLIa-vuY9-q3AUcs_W8gRuP11vsozc5PCLyIy2V6qnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی برای امروز در سطح بالایی قرار دارد.
توصیه می شود با توجه به انتشار گزارش NFP، امروز با کمترین حجم معامله کنید.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18162" target="_blank">📅 09:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جهش انفجاری معاملات شخصی ترامپ در سه ماهه نخست ۲۰۲۶!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18161" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18160" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آمریکا رسماً توافق‌نامه‌ای برای ساخت سفارت دائمی در اورشلیم امضا کرد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18159" target="_blank">📅 00:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سقوط بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده در دریای عرب
ناوگان پنجم ایالات متحده اعلام کرد که یک بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده که به ناو هواپیمابر USS George H.W. Bush اختصاص داده شده بود، اوایل روز چهارشنبه در دریای عرب فرود اضطراری انجام داد.
سه نفر از چهار خدمه در وضعیت پایداری پیدا شده‌اند. جستجو برای یافتن نفر چهارم در حال انجام است.
ناوگان پنجم اعلام کرد که هیچ نشانه‌ای مبنی بر اینکه این وضعیت اضطراری ناشی از اقدام خصمانه بوده باشد، وجود ندارد و علت آن در دست بررسی است.
این دومین سقوط بالگرد نظامی ایالات متحده در منطقه در هفته‌های اخیر است.
یک بالگرد AH-64 آپاچی ارتش در 9 ژوئن در خلیج عمان سقوط کرده بود که ترامپ گفت که نیروهای ایرانی آن را سرنگون کردند و خدمه توسط یک قایق بدون سرنشین Corsair نجات یافتند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18158" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:  چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.  چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18157" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:
چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.
چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18156" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">موجودی نفت خام آمریکا در ذخایر استراتژیک نفت (SPR) در هفته گذشته به پایین‌ترین حد از ماه مه ۱۹۸۳ رسید - EIA|</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18155" target="_blank">📅 18:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18154" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKPycv--bOjM1fC-3NOv29XReMN4VE_YlGjnPByEMQUC90mqokoi6JR0zCNfR-LVdQQ-J4a8HbKu4Ex3wOBIfZHRghz5b02PEWjfvHtR77n3URMIeppyYMAfRh7IxjPxscrnQEJ9znDtG-ZsrT_DF-CoypQTVzyREN9gPoo7FrM02nkVumiERek4ppkeXsiUMXdMfKNHwl7EnVHA6VU-dEKgFB0ZfF6hh5zvM8hqv72LxOkiSzBpEG6IRQBOlzO4SYUsH__RMab1hk7sSHFIS-wFzC4Ggb1Xpy8JXMt3Jehj-vSY2K3KUGC0X2gvRuT0Hhsms1_fz2FujkiS6X8ryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سومین روز متوالی ، امانوئل مکرون با عینک آفتابی دیده شده است.
به نظرتان کار آن عفریته زنش است یا صبیه وجیهه رفیق بهزاد؟!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18153" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گفته می‌شود با اجرایی شدن این توافق، قیمت چص فیل در سرزمینمان بزودی ۹۰ درصد سقوط می کند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18152" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به گزارش العربیه، آمریکا و ایران به توافق اولیه برای آزادسازی ۳ میلیارد دلار از دارایی‌های مسدود شده ایران دست یافتند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18151" target="_blank">📅 15:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18150" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b926ep6DtSxej2W4WBefryluYuLMX0qMztaShwg58BiGw6dRWDviWBDyGzcVZ580NUpt-MQRehb_fOpVWy7U0rVtrp66mGxknauNwlOnv__Fn7MFEFlUzCU2zakE2jY-IFosHdHDFOIf5d65saBuZmjYBWaY0E1yQjNJSr6-mBOAXyUUj6KlWaY6WlMpeCuf1exsvh0mfe4zIsQWgLOIT4SBe51VLmsgk3slYz5az91dKI7pu7TM4W5W1V4zCKP_dJbe8JgizUmcu5xNQj6pL3kC1oPWGN6wMnZQd7ho2_EZ81-nclvrsrdVjv0US7_2t33ImA0jK-bphXP3Cxl4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد دارایی های ریسکی و افت بهای نفت!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18149" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBZ5i9UcmLQhuL_gsZb8mWCYMKvPtEV6N3ETW5wtj56-Lb6FH-RbnI_NM08xegKI7xJ59ebK_Tve_xebY4dFItdQf_3XCSBgLcogM7ktMhd6dUPcBVIr3Cvlvhu9_lL4a1FXg3CuonhvfCndp7jGzLucXxSyUfDpiJKMYGGbx_DISdNbxyajUVG6bKWIDFO9fPArzOOp-xURqp3W26shfGZW6dKM5XnEYlu2HSjWov1kss-t0nbf4xGZ3TN8J0y5nfye-sRJt6rW3z2f-RcJrwAKo4dDNTTgj-MHc3Pt_AQdTu2IKRzrctrDHwCimG2k4uS2wTnvQ8RxrqHob-BLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18148" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عراقچی در پاسخ به تهدید کاتز برای ترور رهبر جدید ایران:
شرایط تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است.
رئیس‌جمهور آمریکا متعهد شده است که حیوانات خانگی خود را در تل‌آویو ساکت نگه دارد. اگر آنها به ارباب خود توجه نکنند، ایران به آنها درس خواهد داد.
هر تهدیدی علیه مردم و رهبری ما پاسخ فوری و قدرتمندی دریافت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18147" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=llHoe9djx_u4bGWTi-oph3rbx2yaqCXHX1H2c9j6MH2jIopk-hLevWWpFRe5p4tajhjZ7qC0siHe4KStLkeuAuqkteC_m9nmTw9fZsv8_QJqj0ZNv5TbBJlsKG7bzinWzDOZ7CVQSjmpBR4RaKxdfTXJn9qKmByvmFh04Zh1KcIkTx9uRR7ZO2okIVlz78Y24a6PY09zYGFpUI2x7ItKH4c0k90rRtcGF_rn2HirKYr9BL9jEcXXi9BJ1plXGshCfaRUqVeAMTDTrT3DltRssivl2euwu2noSS8sZz709Yxo3mmHXIvo-ojkPmZi4U5K6xQ-YKO_iDFQgJQV-ClRcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=llHoe9djx_u4bGWTi-oph3rbx2yaqCXHX1H2c9j6MH2jIopk-hLevWWpFRe5p4tajhjZ7qC0siHe4KStLkeuAuqkteC_m9nmTw9fZsv8_QJqj0ZNv5TbBJlsKG7bzinWzDOZ7CVQSjmpBR4RaKxdfTXJn9qKmByvmFh04Zh1KcIkTx9uRR7ZO2okIVlz78Y24a6PY09zYGFpUI2x7ItKH4c0k90rRtcGF_rn2HirKYr9BL9jEcXXi9BJ1plXGshCfaRUqVeAMTDTrT3DltRssivl2euwu2noSS8sZz709Yxo3mmHXIvo-ojkPmZi4U5K6xQ-YKO_iDFQgJQV-ClRcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18146" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">محبوبیت فردریش مرز  به پایین‌ترین میزان خود رسیده است!  بنا بر گزارش بیلد و با استناد به داده‌های مؤسسه تحقیقاتی INSA، حدود دو سوم آلمانی‌ها از عملکرد صدر اعظم فریدریش مرز ناراضی هستند.  این رسانه اضافه می‌کند که حدود ۷۰٪ از شهروندان آلمان از عملکرد دولت ناراضی‌اند.…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18145" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">💳
اعتراض عضو فقهای شورای نگهبان به بازشدن اینترنت بین‌الملل
🔹
مدرسی یزدی
:
باز گذاشتن شبکهٔ جهانی اینترنت بدون ملاحظات کارشناسی دقیق از جانب متخصّصان متعهّد، به انواع بهانه‌هایی که نمی‌تواند جبران‌کنندهٔ آسیب‌های همراه آن باشد ـ از قبیل آنکه کسب مردم آسیب می‌بیند یا حقّ مردم است یا خلاف وعدهٔ انتخاباتی رئیس‌جمهور محترم است ـ کاری بسیار خطرناک است. این کار، اقتصاد کشور، امنیّت شغلی مردم، امنیّت داد‌و‌ستد‌های تجاری، امنیّت نهاد‌های مهمّ کشوری و امنیّت شخصیّت‌های مؤثّر نظام و سلامت روانی اقشار مختلف مردم به‌ویژه نوجوانان و جوانان را در تیررس دشمن آمریکایی صهیونی قرار می‌دهد</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18144" target="_blank">📅 13:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ9nOP9unTMk32hwLPba1Xz_yt9szA0-iJmdXWOZnM4jy9zYqtAQNLswvhFH46P3tMlPzfui7kK10zz1Kr73dFXBoQE_iFZPZ8BnxPhcEofRJtldRGxoFZEcTOO6XVBUkDeY17cx0_QzTQP20Mg04BePqLkhRSRIvARccrBm88HK2Lp_zfhutsOWlhaFy-Yn4letBFCq4a2LN8XR2_IhkDCl8z-WqqmL-Ewh6DzMYIn1JfAR3b6m5zLo6_-xTC-Q27u7Ss2t3304m05VOriufGUU9-HG6lcPpLocrjpIsMCBe9zH4_qPYNzmuaBuFQ-D5h7GHsWp3xR3vdXdcOy9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18142" target="_blank">📅 12:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18141" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Secret Box
pinned «
🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/18140" target="_blank">📅 11:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه
ژئوپولیتیک و بازارهای مالی
ارائه خواهدشد.
یک
شاخص ریسک ژئوپولیتیکی
هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18139" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbTeubXQ6y1C3WPL7HVZ4cNOTAAvmQeay7PG734Vfj8T_tmtuEhlQipg2sI31Mkt5iG-yNmqiADhj5L0ViHImoDwI6HLduFEyub6pxM2SYwrmC8GCsrUiGli_tUs75BLP9Hbs9P7HIyV7a3o-kT6eII66CukjwRdLgHmphyJLygfwMeAGW4lF_7AyBMWFKwSeX2hKihn7xJ91CpPw2D-JvALdnhv07WnBUkTBQvTsB2t8dxewpe7K-8zhl2CapaSWv3Vnloql3k_Q3SHxk1GR2ROvxwi_fGNaVviuMZqF6RVDrPfn44qgZXpJ2ObY3kI8NKA8Cx1CwpTclDjbrIwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات جدید قاسمیان:   واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18138" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اظهارات جدید قاسمیان:
واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18137" target="_blank">📅 10:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxTt58z4hL2tuy4WUAAGbGEkmXiIytYOCZOHguoDew_KE5cxTGnA6KDnrC226HoG0nzPgZhklZmMW0tWWAiN68PqvuI8th3c-1yiPu4eTM6g3oPh8eCjwfS851oPgxXs5J5IvhqNyIrMFI_aRp7CQqb6MlIxPmP_W-_N68j83NCMdSRDDc7lI1XDw5MKqtoef37hb5toayQUQk17YvfM5IchblRQ_wW_GJ4NXVR36h370m01o3mTOH89vKOL3zafS-tAQE63sW9kB_YKQn1ENpejcmSTgKyjj6_X1IZqBl0aI5ACweMooenH7C75OWC8Rc-41Eh5PqyH-apBqx0Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18136" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzayLUZILuWjACbW5lGBb2VNqLkqqMmWoy6583GwSwvYZ3y0pioARr0x59Olu2Sdy97gciV7XdmceCBV6jbqqXcj5th4IEexuHpZ6wX6qb0fVH9-4YvcKUeLprnVvRP5ejaMD8SWmWVAJTA7iHDJ-qOh05HBTDAuPreojptQV8hRslOGpALETH_4aymj5tL_EAKSqvLAOnRV2zpCLC3a2N6kWwuWC56vVOzFfIJik2pMygEHlS7mzzY8qTKcwi-PaOd4U2P9jJVOXLVZanBc4xm_4mbh4l0jDeL5BPL9dRtdxhmcZ7Z-mQqPe6rwms7gHs-GqbHEHMfVU8ho0hWN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد دو ناو آبی‌ـ‌خاکی آمریکا، باکسر و پورتلند، در حال حرکت به سمت خاورمیانه هستند.
این دو ناو معمولا برای انتقال نیرو و عملیات آبی خاکی و ... مورد استفاده قرار می‌گیرند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18135" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فراخوان‌هایی برای اسکان مجدد در غزه پس از مصاحبه نتانیاهو
بنیامین نتانیاهو در مصاحبه‌ای با «پاتریوت‌ها»، بازگشت به اسکان یهودیان در غزه را رد نکرد، که این موضوع باعث شد قانون‌گذاران برای تبدیل این چشم‌انداز به واقعیت و اصلاح «ظلم تاریخی» جدایی سال ۲۰۰۵ فراخوان دهند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18134" target="_blank">📅 09:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18133" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=UVOwsNDBF9aUBVapWyGPaCdL93fl_UBHiVV4blG--R3I0hc8zzebs-CXZrelt8mlWslQhm2_Z93Cu1qv7Ickqox-1w3InwSvV1TDvohspG-kkwtIBNJQZVmuXtg2wEcKXD5zYqrrm1811kELK5ulX0k3Ajt-toWtKnYGOgMe01aueAGXV1Bc-rPQVaxN6zzhgE1b2gYswWuHVZwuyx53dUcdIk3oXkrRV00XFwh8ce6fs8u0z2sdGMrJg93VbNvBW6Q9I0Eyn-kmED3XFp0g-E738DODLyqyARmXcj0sji1nvi-Nii2xXRh_O9CsnMHhXDPVlS5UpFiRQ10zWv50sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=UVOwsNDBF9aUBVapWyGPaCdL93fl_UBHiVV4blG--R3I0hc8zzebs-CXZrelt8mlWslQhm2_Z93Cu1qv7Ickqox-1w3InwSvV1TDvohspG-kkwtIBNJQZVmuXtg2wEcKXD5zYqrrm1811kELK5ulX0k3Ajt-toWtKnYGOgMe01aueAGXV1Bc-rPQVaxN6zzhgE1b2gYswWuHVZwuyx53dUcdIk3oXkrRV00XFwh8ce6fs8u0z2sdGMrJg93VbNvBW6Q9I0Eyn-kmED3XFp0g-E738DODLyqyARmXcj0sji1nvi-Nii2xXRh_O9CsnMHhXDPVlS5UpFiRQ10zWv50sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد خوش چشم:
«یک چیزی از آقای حاجی زاده بگویم که احدالناسی نمیداند جز خانواده اش
که آنها هم به من نگفتند!»</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/18132" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جِی‌دی ونس درباره ایران:  یکی از چیزهایی که درباره ایرانی‌ها برایم هم جذاب است و هم ناامیدکننده، این است که آن‌ها می‌گویند «نه، نه، نه، هیچ گفت‌وگوی صلحی در جریان نیست»، اما گفت‌وگوهای فنی بین ایالات متحده و ایران درباره توافق صلح در حال انجام است.  این یک…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18131" target="_blank">📅 23:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18130" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قالیباف رئیس مجلس ایران:
تحریم‌های نفتی برداشته شده و ما نفت را ۲۰ درصد گران‌تر می‌فروشیم</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18129" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=gunhNnqhbkse11ZApvjIT2QBqlw7wPn7tCUZboJhXBGfhX2Nu0kjtuF316zSn5tz-YGzScdeW3JFgO7fWXV6MZM6pJIXUh3VNseto6B8UqRG0WIRUd_seULferdGUKFhwSF94Lu2qNCT9TgMuO5M0nWwt7JfCD6_TtM56lfjpamAylBa5mrxCoD6qSn5qTPnGPBWuPOaixJbrpGRSdBvGjPEH6TBB1XfughS_T8UJq3DoE3U68nM1YN_k570NAbdzaPSF0kVr_udHvStrXUDZPmev8i_GIhWd8rHq031d6rJtGokqWc3l_ndPzKl4X4cOPxfHqTYptSnAtt68EECwANSk3HRcTA7rxDRGtzwEFvVMciZ8GKa4YmclbRA5kiAGkcPWeHj7ebUePYobTyxtJkkevqHOE_-4WPiHCYqMSUWCd-Go0ALsJtasZiE2frU8WWZojzGjHA-wPmk2iP2B3QcFzisZDQPi5ZAxF2u4b2UwqFcEK2S2YmEuB4LcLyTCd93hKMK--1uX4EDSVBueeuv4czuuG2KDLRnXAlNY0NurELK-c7maW_engOEeDlj-zEda9lsWX9ntYIlHLDiNC5q4m8xHFZsoIgnLxrOjZMtSXw2a501QJ_fBncpYpdk8wGE8SNgS-K2YB3Z7uK0Ry7C-cWgJUviMyL2ofkmPUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=gunhNnqhbkse11ZApvjIT2QBqlw7wPn7tCUZboJhXBGfhX2Nu0kjtuF316zSn5tz-YGzScdeW3JFgO7fWXV6MZM6pJIXUh3VNseto6B8UqRG0WIRUd_seULferdGUKFhwSF94Lu2qNCT9TgMuO5M0nWwt7JfCD6_TtM56lfjpamAylBa5mrxCoD6qSn5qTPnGPBWuPOaixJbrpGRSdBvGjPEH6TBB1XfughS_T8UJq3DoE3U68nM1YN_k570NAbdzaPSF0kVr_udHvStrXUDZPmev8i_GIhWd8rHq031d6rJtGokqWc3l_ndPzKl4X4cOPxfHqTYptSnAtt68EECwANSk3HRcTA7rxDRGtzwEFvVMciZ8GKa4YmclbRA5kiAGkcPWeHj7ebUePYobTyxtJkkevqHOE_-4WPiHCYqMSUWCd-Go0ALsJtasZiE2frU8WWZojzGjHA-wPmk2iP2B3QcFzisZDQPi5ZAxF2u4b2UwqFcEK2S2YmEuB4LcLyTCd93hKMK--1uX4EDSVBueeuv4czuuG2KDLRnXAlNY0NurELK-c7maW_engOEeDlj-zEda9lsWX9ntYIlHLDiNC5q4m8xHFZsoIgnLxrOjZMtSXw2a501QJ_fBncpYpdk8wGE8SNgS-K2YB3Z7uK0Ry7C-cWgJUviMyL2ofkmPUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیریت Secret Box حدود ۲ سال پیش این ایده را مطرح کرد که این روانی عوضی را در قالب یک معامله بکشند که هم برای ایران خوب بود و هم برای اسراییل و اتفاقا ۴ ماه بعد این فراخوان لبیک گفته شد اما سوگمندانه ناموفق بود!  مردک حمال یک دیوانه کامل است و می‌توان او را…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18128" target="_blank">📅 20:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وال استریت ژورنال:
اولویت‌های متضاد ایران مذاکرات صلح آمریکا را به خطر می‌اندازد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18127" target="_blank">📅 20:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!
از این جهت خیلی شبیه احمدی نژاد است؛
منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18126" target="_blank">📅 18:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسپوتینک:  اختلاف با عربستان، جنگ ایران و تله هرمز عواملی که ممکن است امارات متحده عربی را به سمت خروج از اوپک سوق داده باشد  دکتر ممدوح جی. سلامه، اقتصاددان پیشکسوت نفت، به اسپوتنیک گفت: «مدت‌ها قبل از جنگ ایران، امارات متحده عربی به دلیل اختلاف با عربستان…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18125" target="_blank">📅 18:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18124">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بقائی:  ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.  آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18124" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بقائی:
ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.
آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های مسدودشده ایران با طرف‌های قطری است.
بنابراین تأکید می‌کنم که هیچ دیداری با طرف آمریکایی در هیچ سطحی برای روزهای آینده برنامه‌ریزی نشده است
تمامی مقدمات لازم فراهم شده و امیدواریم این روند به‌درستی پیش برود و به نتیجه‌ای رضایت‌بخش برسد
رقص و ابراز شادی مقام‌های آمریکایی از صعود نکردن ایران به مرحله بعد جام جهانی، با همه معیارها و اصول پذیرفته‌شده میزبانی مغایرت دارد
هیچ درخواست رسمی درباره بازگشایی سفارت کانادا دریافت نکرده‌ایم در صورت دریافت درخواست، آن را بررسی خواهیم کرد، اما تاکنون هیچ درخواستی به دست ما نرسیده است.
﻿</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18123" target="_blank">📅 16:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRIaItiP56_E0fGnwN_Gz_D9Kkl_LB3lmLS9PHkx_N3-Jv5-c1J2m3tSSZynBn2Lmfo9OnbMr1r4pYzwnhfDoU67VcbPE8V0Z2ILEFOlxOWpt7-DmNdt0kFN9J6SymklbBxPDq7HejtniPWMZLnDikquQhSZnLe07nr3GCYqMgzLZFcrmx4i9bsIGV3jwTn45uo3mEKg45is1UwPnOhvJgDTqfCzSAiprKFCNakGbwJ0fGC1z7wDwEolHrx1X5kfHEVSbKDijbZTQngDOIF_RW3aParcuPzxghGQ5z5WlyrvV237UZtRyg-QMKpaquyH5yoPM1duzsYyxPwQk2gyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.  سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18122" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.
سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های مسدود شده ایران هنوز منتقل نشده است و آزادسازی آن‌ها به پیشرفت در مذاکرات بستگی دارد.
او همچنین گفت یک خط تماس کاهش تنش به کنترل تبادل‌های هفته گذشته بین آمریکا و ایران کمک کرده و قطر با عمان هماهنگ می‌کند تا عبور ایمن از تنگه هرمز را تضمین کند، که آن را به عنوان اولویت اصلی توصیف کرد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18121" target="_blank">📅 14:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.  در این بیانیه، او از اصطلاح "دموکراسی اجتماعی" به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18120" target="_blank">📅 14:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N40CZe9GSq_FP4Rala2O-XdovJsTfOfYCKOvyfZV-nKG_RzOA5MII-VPSpAHSlDQIdVcDt4yNyoBTN4VGa7SZ_7gWQCkkPPQQM-HCn6UnHp0329TniOh3gGfl8MxMp6X4aycExfZbCVasUvhRN7-EeI7EwvCCl9mVK0GkaEtBGgNvDraA0tF6p2N_z1nVrr8jE4SP4qLCSOlBU8YdNcMGYskBi174FGrpm0P0FvPH0SLSm8cIVgucqSrhes3NBBEwQADlLODTeIJGPmzFgY1MG7GGZp7mundMRkf5NI9qtBZVGfjS_g3VzlHyYRWMDC1i_P09jzVxGeedeAxRTN2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.
در این بیانیه، او از اصطلاح
"دموکراسی اجتماعی"
به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد این اظهار نظر علیه جریان‌های سیاسی داخل ایالات متحده هدایت شده است.
طبقه‌بندی کمونیسم به عنوان یک تهدید وجودی، حتی از خطرات کلاسیک امنیت ملی در فرهنگ حافظه آمریکایی نیز فراتر می‌رود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18119" target="_blank">📅 14:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18118" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_gNhZNW2YByMF7xZRlYXkRl6zqW81v7e_1SOS20v1fphpFUk5kcqNg-_l4EcF5zZhSWLxWDooPGQc6daM5JlQZIMwpRsM1JkexVWqCY_K64W6aL7I0EOtbLK-9Gf9KCJslPlppWjSK7fHSboGIqv28iTn5YdHA-zbBzTuUOZaIssmlEWKDjQPY-IObxM8kvGdZThvdzUEM2JyA2M62CMl8OvskVANF1X_83UEjdyapNHJAPIFxistY_0PZAQHqkPGOYY0gWmBUMo5m0dw-hX_tYii2entGa3_ScZJXe-Eoj_F6M-Ri7TAdS7QMM5wApftqf77hu1YikIsoyGpV8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18117" target="_blank">📅 13:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
قنبری ؛ سخنران صداوسیما : ترامپ جنایتکار باید ترور شود تا رهبران ما بتوانند از مخفیگاه خارج شوند که اگر چنین نشود آنها باید تا ابد در مخفیگاه بمانند</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18116" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است  یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.  یوسی کارادی،…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18115" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است
یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.
یوسی کارادی، مدیرکل اداره ملی سایبری اسرائیل، به روزنامه آلمانی
دی ولت
گفت که مقامات اسرائیلی در ژوئن ۲۰۲۵ حدود ۱۶۰۰ حادثه سایبری خصمانه را در جریان جنگ علیه ایران ثبت کرده‌اند.
به گفته کارادی، این رقم به طور چشمگیری به حدود ۴۸۰۰ حادثه در ژوئن ۲۰۲۶ افزایش یافته است.
کارادی گفت: «برخی گروه‌ها بسیار ماهر هستند.ما می‌توانیم با آنها مقابله کنیم، اما باید آنها را جدی بگیریم. برخلاف حوزه فیزیکی، در فضای سایبری آتش‌بس وجود ندارد.»
کارادی اظهار داشت که حملات طیف گسترده‌ای از نهادها را هدف قرار داده است، از جمله سیستم‌های زیرساخت حیاتی، سازمان‌های بزرگ، کسب‌وکارهای کوچک و متوسط و شهروندان خصوصی. در میان اهداف کوچک‌تر، شرکت‌های حقوقی و دفاتر حسابداری نیز بودند.
او گفت: «تا کنون — و امیدواریم که اینگونه باقی بماند — ما موفق شده‌ایم حملات به زیرساخت‌های حیاتی را دفع کنیم.»</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18114" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سردار محمد اکبرزاده، معاون سیاسی در دفتر نماینده رهبر ایران در نیروی دریایی سپاه، در یک تصادف رانندگی در استان کرمان کشته شد.
اکبرزاده یکی از معماران کلیدی استراتژی ایران در تنگه هرمز محسوب می‌شد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18113" target="_blank">📅 09:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18112" target="_blank">📅 08:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">غریب‌آبادی :   اگر عمان به هر طریقی تمایلی به ایجاد یک رژیم مشترک برای آینده تنگه هرمز نداشته باشد، جمهوری اسلامی ایران این امر را به تنهایی پیش خواهد برد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18111" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:   ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18110" target="_blank">📅 23:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دکتر محمود سریع‌القلم:  دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.  مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.  اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18109" target="_blank">📅 23:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دکتر محمود سریع‌القلم:
دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18108" target="_blank">📅 23:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9NDsxXypZwwUjFJLYenig46DkShWw0ZPqsPxRiOSKYRf6_VP7tI8g8c2b8TshNX7hxV0D0nkRg3yAfgNBrqOi1LCJvUnqf6-516kyWqhP5a5dFgXUHwZwU7WKhejiEPAVRPe4ee1pp_WWsogUcthyZYEqa3r2GiYt66USYZ34OZb16uUMw6Pz9SR6lGuU6Bflck0PMRqLdE7320-lRI-yO30ZygDZ-cKfEIZxYIG-THVp44jRPAXeqf7VChGUQOs2FWdenTV6EbQQthoGZJ3UdNBR9CxCzqjxBexKN507A0YBORjYEIaW7Ap1NWXJEkhKc_W0Wg-9RxmXJNP2GX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18107" target="_blank">📅 21:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:
ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18106" target="_blank">📅 21:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مکارم شیرازی در دیدار با پزشکیان:
اگر بدخواهان مانع‌تراشی نکنند، توافقات اخیر می‌تواند آثار مثبتی برای کشور داشته باشد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18105" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty83ZlsEG8rbFuAVRueZ9pUyfZcnnqMjQoDPPkOpbw22RXyMaVrnIVNXyTPkRm1UYcpPf6sYOm0p0Tv0FTECs9CbVUEGD9C58Wls8JMsFMZ7L5tRFUeHH-TYpJLhU58N3Wug8K3huw5RIDWz43Ffzn0qZWwxzXYYVBg0q9Y_JHOjBX4t2qxvj2qNLnlfTP2OYkqNjGrFm29vKriMLfg-U1B7-s2l986dskAp2FLUki3R7U2sCcMWdz02cOaGzFrBoypqm08r0byCk59L5NY6hFryfVar26X-N9B09jOn4159fFzf9vQ-GnldwHTFr4vi_P3YYJRFatRtvgrFzxD_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18104" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایران می‌گوید برنامه‌ای برای گفت‌وگوهای مستقیم با ایالات متحده در این هفته وجود ندارد، با وجود ادعاهای مقامات آمریکایی.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18103" target="_blank">📅 19:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18102" target="_blank">📅 19:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18101" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
«من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18100" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
