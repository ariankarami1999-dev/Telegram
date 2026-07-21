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
<img src="https://cdn4.telesco.pe/file/pCnxx0_Va9lufx-Ok2iXLhH4DfEolZgeYzDXkLhQfMmqokabdkERatpKmp_2wx4fSFeHYo_X_xQ-X-DNF7yaX4xzgXt0Keo5FEXWIOT6nWRBMmywjruVVIoV3726s9s6GurskYB-GcMpIpmmxdzA0lPXKaAHJkrB1sQ_WBViqB0jzAFl5mB4RGvyijHazOyArblLCVCZtILWS7HI2ezpmUbKhjcwIn1p56YTqkq0L39ZiZBUvYPbqmvIrvtz8IrU7rrUsP8la4isGUY8dWLAsDfDQcA1d7WJfomy1douP1UTBiJMH2G2iv7gqcgFER5vcZ17QG3-tSJvAZsKSYccog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.4K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-19070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ درباره ایران:
بچه‌های جوان را می‌کشند انگار هیچی نیستند، انگار آبنبات هستند. کارهایی که انجام می‌دهند دیوانه‌کننده است.
آن‌ها مردم را به صورت تصادفی می‌کشند—بیش از ۵۲,۰۰۰ نفر—و هیچ‌کس درباره آن صحبت نمی‌کند.</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SBoxxx/19070" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها به شدت مشتاق دیدار هستند.
تا زمانی که برای دیداری معنادار آماده نباشند، ما هیچ علاقه‌ای به دیدار نداریم.</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SBoxxx/19069" target="_blank">📅 18:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد تا یک یادداشت اعتراض‌آمیز درباره هدف قرار گرفتن یک نفتکش کویتی به او ارائه دهد.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/19068" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد تا یک یادداشت اعتراض‌آمیز درباره هدف قرار گرفتن یک نفتکش کویتی به او ارائه دهد.</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/19067" target="_blank">📅 18:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiG7zscY8PldVnoeGHCpHBMfccXiLC4vuT1Uw2cp4IAM4klEL0SvKZ5tGKmuIXaY147ORRrBK_3Fgk_-sZpvc4FY5MYeKUwJamHFNJi2Vnnl5qfRc9M4-DKp8iLeHi-aqg7iBQBc-kyOl5lgC08WOyRSTtbX19hfsspd-w9I4HCXWulTIW0w1WZZJtzEpbaxXtX5zn7CIs1IFizceoPSI8GRy1DsKlHXwtoCgJNQH33YIEOCodVyCTWcrHc6pxpoTvJ2iU6BhNcvqmwVGkwWCKoPK0tLmbnnC28x1pZ5ZgmPHfx1yG0QRhh5LlBuedzQ1uAV9u56G4dug80n1rza4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد تند ثابتی از عراقچی و برنامه جواد موگویی</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/19066" target="_blank">📅 17:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الهام علی اف:
روسیه دیگر به دلیل شکست پالایشگاه‌های نفتی خود، کاملاً قادر به تأمین شرکای سنتی خود با نفت و گاز نیست ‌.
«از سرگیری سرمایه‌گذاری‌ها در زیرساخت‌های نفت و گاز توسط بانک‌های اروپایی به آذربایجان اجازه می‌دهد تا صادرات منابع انرژی خود به اروپا، از جمله به آلمان را به طور قابل توجهی افزایش دهد»
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/19065" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده:
چین خرید نفت خام ایران را حدود ۴۰ درصد کاهش داده است</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19064" target="_blank">📅 15:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19063" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/19062" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dabbbd67.mp4?token=tjwiw3CLd_dEoLALLES5Hyl6jrzPbZys1PyiqJ0zlMdkLumVTyAgdzMzoADxQWLk7V0Vpdh2z8HfEEqKrgTulcnPFSSrYE2hwebJ4j2sAkRx6oVjRUPXudRzfP7SYCqauTvhYj_qDIqzuA28llraUu-BVji3pLVnXQ2zK9rIgS5MWpLO3rNCojJbBIb_gQSz7kwuUYK1Sb4MWKgj0d2UwkIv5rszWwZIvR9bVtvVSWKmhBA5gtaR10QgccDqhE4v6Q0MZZnqYgRBL6FqESvoFPfhp2xAS-a4Pck_Wz5zwV3T9DzKyoNw_pZPDnMNDJScBUymzjiI4Ql3xSB8_veVdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dabbbd67.mp4?token=tjwiw3CLd_dEoLALLES5Hyl6jrzPbZys1PyiqJ0zlMdkLumVTyAgdzMzoADxQWLk7V0Vpdh2z8HfEEqKrgTulcnPFSSrYE2hwebJ4j2sAkRx6oVjRUPXudRzfP7SYCqauTvhYj_qDIqzuA28llraUu-BVji3pLVnXQ2zK9rIgS5MWpLO3rNCojJbBIb_gQSz7kwuUYK1Sb4MWKgj0d2UwkIv5rszWwZIvR9bVtvVSWKmhBA5gtaR10QgccDqhE4v6Q0MZZnqYgRBL6FqESvoFPfhp2xAS-a4Pck_Wz5zwV3T9DzKyoNw_pZPDnMNDJScBUymzjiI4Ql3xSB8_veVdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای روزنامه جروزالم پست:  ترامپ پیشنهاد قطر و پاکستان برای آتش بس 10 روز با ایران را به شدت رد کرده و اعلام کرده حملات به ایران ادامه دار خواهد بود.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19061" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای روزنامه جروزالم پست:
ترامپ پیشنهاد قطر و پاکستان برای آتش بس 10 روز با ایران را به شدت رد کرده و اعلام کرده حملات به ایران ادامه دار خواهد بود.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19060" target="_blank">📅 15:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast Text.pdf</div>
  <div class="tg-doc-extra">305.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19059" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 10</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19059" target="_blank">📅 15:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv_VPDee4KjP4Vltd53cTISoat--5o0Vs4roPNuzXNChvP4EfKasgU3yDJKQqd8Q8fWXGSrKsKqrJtepk11D-K7R2IvUw5gb3t-HUyWXPo2P8Mmyt79UKvRRNDswqe2Twp4XDnL7gkZHTL9P7b0tUjGBQ_o7O68ciLkE_9c1ulOu8pW6JIacr_x7Kw55PGYquQhC6AWW8-t4vOC8yw7ZsFOLyiCstnYJxm4eRhiDBhGJ8db8gb7Kvcc7K7fJooZmUDfhLBQqfrmmyMSyZkIw92KKm4y4pE3JobsrDPg5l5aAgemf7xzX-VkIkLNklWetUTO3PeWMjhzB4c6WdXqAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایینی قرار دارد و پیش بینی می شود طلا ابتدا ریزش و سپس رشد داشته باشد.
محدوده مناسب حمایتی 4015 الی 4020 برای امروز.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/19058" target="_blank">📅 15:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 10</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19057" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 10</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19055" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 10
سه شنبه 21 جولای 2026</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19055" target="_blank">📅 13:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حمله ایران به کویت، بحرین و قطر</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19054" target="_blank">📅 13:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ایران می‌گوید که زیرساخت‌های داده آمازون در بحرین را با موشک‌های کروز نابود کرده است.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19053" target="_blank">📅 12:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شما قدرت رنگ آبی را ببینید فقط که تا کنون این پایگاه کذایی «الازرق» حدود 15 بار درهم کوبیده شده اما هنوز نه تنها سرپاست بلکه بقیه هواپیماهایشان را هم می برند آنجا!  حالا اگر اسمش «الاحمر» بود با نخستین اصابت شاهد واقعاً در هم کوبیده شده بود!  آبیته!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19052" target="_blank">📅 12:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارت خارجه چین در مورد سیاست هسته‌ای ژاپن:  از زمان به قدرت رسیدن تاکیچی، نیروهای راست‌گرای ژاپنی نیت خود را برای احیای نظامی‌گری، رها کردن اصول سه‌گانه غیرهسته‌ای، جستجوی سلاح‌های هسته‌ای و ادامه مسیر نادرست آشکار کرده‌اند.  اگر ژاپن به تلاش برای اصلاح اصول…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19051" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— وزیر امور مالی اسرائیل، سموتریچ:  «اسرائیل هیچ علاقه‌ای به پیوستن به درگیری محدود میان ایران و ایالات متحده ندارد؛ وضعیت فعلی بهترین حالت ممکن برای ماست.»  «هدف ما سرنگونی رژیم ایران است و بهترین راه برای رسیدن به این هدف، ایجاد فروپاشی اقتصادی آن است.»</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19050" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لینک نشست امروز با نیما  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19049" target="_blank">📅 11:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی (IRGC) اعلام کرده است که به یک پایگاه نظامی آمریکایی در منطقه الرکبان در اردن حمله کرده و مدعی است که در این حمله، چندین سرباز آمریکایی کشته شده‌اند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19048" target="_blank">📅 09:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی اعلام کرد که دو تانکر نفتی که قصد عبور از مسیر ناامن در جنوب تنگه هرمز را داشتند، پس از انفارهایی که منجر به آتش‌سوزی‌های گسترده شد، متوقف شدند. سپاه همچنین از ارتش ایالات متحده به دلیل گمراه کردن این کشتی‌ها انتقاد کرد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19047" target="_blank">📅 09:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وال‌‌استریت ژورنال: اسرائیل مدعی انتقال هزاران سانتریفیوژ ایران به «کوه کلنگ» شد
این سایت در عمق حدود ۱۰۰ تا ۱۴۰ متری کوه ساخته شده و به گفته کارشناسان، هدف قرار دادن آن بسیار دشوار است.
اسرائیل معتقد است این انتقال می‌تواند تلاشی برای بازسازی ظرفیت غنی‌سازی ایران و محافظت از تجهیزات هسته‌ای در برابر حملات آینده باشد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19046" target="_blank">📅 08:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزارت امور خارجه آمریکا:
ایالات متحده اقدامات خطرناک و تهاجمی چین علیه ناوگان دریایی فیلیپین در منطقه "توماس شول" در دریای چین جنوبی را محکوم می‌کند و  از چین می‌خواهد که فوراً اقدامات بی‌ثبات‌کننده خود را متوقف کند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19045" target="_blank">📅 02:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک مقام آمریکایی:
اگر ترامپ تصمیم به گسترش جنگ بگیرد، حملات شامل تهران و سایت های هسته ای می شود.
اسرائیل ممکن است در جنگ ایران شرکت کند اگر ترامپ تصمیم به گسترش دامنه آن بگیرد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19044" target="_blank">📅 02:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوزاری گدازاده کم بود، گروهبان قندلی هم به فهرست گه خورهای علی دایی افزوده شد!  گویا سرگین شهریار چندان لذیذ است که این مگسان آن را انگبین می بیینند!  پفیوزهای ... مال عوضی</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19043" target="_blank">📅 02:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!  ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19042" target="_blank">📅 01:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عادل فردوسی پور > New Castle
علی دایی > New Castle
کریم باقری > New Castle
99 درصد ایرانی ها > New Castle</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19041" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19040">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینطور که پیش می رود فردا در هند عزای عمومی اعلام خواهدشد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19040" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19039">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddjvtuugO77wYoLQnhKglbwsZfzb1LctW5vHlgh6YbutVelEl738511yLkslROlesOKLFMyb0rVfTqMiM-JM3jyxw1ASF-Sm_SWagaEr52UwzqE_ExG_zS2qS9Xq0Bm0uKSYLHMBGhUzyfT3Vq7M76giLMbj5UkF_fQTaLiZP7YafkT5U_l7g-zD4PU0EI01JXx49xReO56Ob_xfQgYOEW4uToFOK5nyjLyngQ9tu2sl4h3ijXTm1b1acn2cb7oNjNvVJM41zWLTjR_5YKhGLXlc65R4TUXHYOQjZNcUg1nEUUYs5q6-C6peoLrHp-Io8GgOCvUISUJi9_gbtrn_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی نفتکش دیگر در سواحل عمان هدف قرار گرفت!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19039" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19038">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واقعا به نظر می‌رسد این الاغها تا یک
جنگ هسته ای
جهانی راه نیندازند دست بردار نیستند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19038" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19037">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت خارجه چین در مورد سیاست هسته‌ای ژاپن:  از زمان به قدرت رسیدن تاکیچی، نیروهای راست‌گرای ژاپنی نیت خود را برای احیای نظامی‌گری، رها کردن اصول سه‌گانه غیرهسته‌ای، جستجوی سلاح‌های هسته‌ای و ادامه مسیر نادرست آشکار کرده‌اند.  اگر ژاپن به تلاش برای اصلاح اصول…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19037" target="_blank">📅 00:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19036">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کاخ سفید اعلام کرد که ترامپ روز سه‌شنبه در مراسم انتقال با احترام پیکرهای چندین نظامی آمریکایی که در هفته گذشته در جریان آخرین دور تنش‌ها با ایران کشته شدند، در پایگاه نیروی هوایی دوور شرکت خواهد کرد.
این نظامیان شامل دو سربازی هستند که در حمله موشکی بالستیک ایران در روز جمعه گذشته در اردن جان باختند</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19036" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19035">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام:
امروز ساعت ۴ بعدازظهر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، دور جدیدی از حملات هوایی علیه ایران را آغاز کردند. این حملات برای تضعیف بیشتر توانایی‌های نظامی ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شوند، طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19035" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19034">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش‌ها حاکی از آن است که مقامات نزدیک به رئیس‌جمهور آمریکا، ترامپ، تحت فشار قرار دارند تا پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرند.
آمریکا امکان آتش‌بس را رد نکرده است، اما اصرار دارد که این آتش‌بس باید طولانی‌تر باشد و به تفاهم‌های خاصی در مورد تنگه هرمز گره خورده باشد.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19034" target="_blank">📅 21:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حمله دوباره ایران به بندر عقبه اردن</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19033" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اخباری از حرکت نیروهای زرهی ایران به سمت کویت به گوش می رسد!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19032" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اخباری از حرکت نیروهای زرهی ایران به سمت کویت به گوش می رسد!</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/19031" target="_blank">📅 20:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">— یک کشتی در ۱۷ مایل دریایی شرق امارات متحده عربی توسط یک پرتابه مورد اصابت قرار گرفته است.
هیچ تلفاتی گزارش نشده است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19030" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ:  «نتانیاهو به هیچ وجه، به هیچ شکل یا فرمی، در حالی که در ایالات متحده است، دستگیر نخواهد شد.»  «او علیه جمهوری اسلامی ایران می‌جنگد که اخیراً ۵۲,۰۰۰ معترض بی‌گناه را کشته و در ۴۷ سال گذشته سربازان آمریکایی و دیگران را کشته است.»  «تنها کسانی که باید…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19029" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:
«نتانیاهو به هیچ وجه، به هیچ شکل یا فرمی، در حالی که در ایالات متحده است، دستگیر نخواهد شد.»
«او علیه جمهوری اسلامی ایران می‌جنگد که اخیراً ۵۲,۰۰۰ معترض بی‌گناه را کشته و در ۴۷ سال گذشته سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید دستگیر شوند، کسانی هستند که ایران را به این مارپیچ بی‌سابقه مرگ و ویرانی کشاندند، چیزی که باید سال‌ها پیش توسط رئیس‌جمهورهای قبلی حل و فصل می‌شد.»</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19028" target="_blank">📅 20:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سازمان صدا و سیما:
یک کارخانه صنعتی در حومه شهر خمین، ایران، حدود ساعت 7 بعد از ظهر مورد حمله قرار گرفت.
هیچ گزارشی مبنی بر کشته یا زخمی شدن افراد وجود ندارد و مقامات در حال بررسی میزان خسارات وارده هستند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19027" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ذخایر نفت خام در ذخیره استراتژیک نفت ایالات متحده حدود 5.1 میلیون بشکه کاهش یافت و به 311.4 میلیون بشکه رسید که کمترین میزان از سال 1983 به شمار می‌رود.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19026" target="_blank">📅 19:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر امور خارجه فرانسه:   امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19025" target="_blank">📅 19:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر امور خارجه فرانسه:
امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و در ساعات آینده به فرانسه باز خواهند گشت.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19024" target="_blank">📅 19:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QI1_M3nAarFXZXszKefZ7o065w1XmxLmEE4JouLcSutSoQ0yxauqBnfgT71SIx6JmZepEhyLeYVTbsue06G2T14Wl_cIfZxGDTP46n2daYFmQ7DWHrrGnvUrFjQD66TziQxZUaTGdNwcjB4Oc2upkjgB9LvsRi58GIR3u_KwiNQ9WuiFYeO6VJX107KVBbFsWOLOf_09yP3-lqFUPpCHtu34Unfp_2BDMMEV2tlu8v86kl5PL4z1bmYb0IDB1TlYXZmDze-iUepHdHXaQl7Ri6HYuiwRchSiHUdJTbti5wCUZip_yS91ky8eMxUWE_2BIe_HZK65l6BAkdrzh6_YzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.  معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19023" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چهار شهروند هندی در جریان حمله به کشتی تجاری "My Golden Leo" کشته شدند، در حالی که این کشتی در حال خروج از بندر اودسا در اوکراین بود.   سفارت هند در اوکراین به دقت وضعیت را زیر نظر دارد. هند این حمله را محکوم کرده است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19022" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8VVZSltYzUDgBPzikOEuuiy39oY_E9rrFE9fGKyp07PHxgpVlpuCjfc5FS2dfX_1m0bpDh27wmr76hSQE6yRqwDcjUbAgFUm5j2Hgn7cz4opgHraqEAfuEARfRea4NI7xi949-X8HrFKqv2gCX1UUCqVjA7SlI4AsHep5PJmOO1ixWlT2FPzYOPxCveWedairggwBLCSz-0MUZLK0q5PD-EvG1CXxFT4ugxyP8SvZ6AyOupsDxZ85731llIxuhdqwUT0JTBDRyQvELhyDuwO3a8c5-4PVUvRu4qgS6UvUvyhXdPsSRRiYenIAtgRVr9fv6qFFh6AAxXvdbluILi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19021" target="_blank">📅 19:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19020">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19020" target="_blank">📅 18:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19019">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از دیشب دیگر دامنه حملات آمریکایی ها به جنوب محدود نیست و تبریز و شیراز هم مورد هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19019" target="_blank">📅 18:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19018">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19018" target="_blank">📅 17:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19017">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آتش‌سوزی در یک کشتی باری یونانی رخ داده است. این کشتی در نزدیکی تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت.
— رویترز</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19017" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19016">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجار در شیراز</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19016" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19015">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خب از هرمز ۲۰ میلیون بشکه نفت در روز عبور می‌کرد که برای ۷ میلیون ش جایگزین پیدا شد (خط لوله شرق به غرب عربستان)</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19015" target="_blank">📅 15:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19014">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19014" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19013">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اگر یک بار دیگر هم فریب میخوردیم با ۲ بار قبلی می‌شد ۳ بار و این اصلا خوب نبود.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19013" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قالیباف :   آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.   ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19012" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToflrtIwpyTSaq0UAVMxB4Js_kl7jm_VZ0wwcdawqHCh8ta8edbiyicL7hvLBWURtn8c2itrmONnD88UiaIpgeo17iKKDpEuOXtvbUa_F8vbRrZ_pi1ClAqjHgBLtRSBwyH3FHk_Pyjm4zdNCtg5ikd3hXcdU9bjzvuoiZyaqyIoXxn-Vw_U8vcfECFay-rLwnMIPDJbZlq15S2mSHRW0sCrTRGmaaAgfIpX2F3X1B1TKK8kqtViGBtdcjU2oTu5DAY7d8yBP_Rv1YSjbdH9jN1zYBttDaFEFbJbYyy63z2TQdErR6TiZIQJYcYS2gn3dJJoJKm1yVx-OxKqinSGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف :
آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.
ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را آماده کرده‌ایم. اقدامات باید ادعاها را تأیید کنند، نه اینکه با آن‌ها در تضاد باشند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19011" target="_blank">📅 15:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.
این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون تصویب پارلمان صورت گرفته است.
این درخواست در حالی مطرح می‌شود که تنش‌های ایالات متحده و ایران همچنان در حال تشدید است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19010" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دلار فردایی تهران
⏳
188,700 فروش  بازتاب انتشار مواضع ملایم شده دو سوی نبرد روی قیمت دلار داخلی  نکته — موقت است و دوباره بالا می رود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19009" target="_blank">📅 15:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ببینیم آمریکا همان بلایی را که با قربانی کردن اوکراین بر سر روسیه آورد، با ژاپن بر سر چین می آورد یا نه.  در نشست با نیما (پیام ریپلای شده) مفصلاً درباره تاریخ تنشهای میان ژاپن و چین صحبت کردیم.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19008" target="_blank">📅 14:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بوی مذاکره می آید…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19007" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیروی قدس سپاه پاسداران انقلاب اسلامی ایران مدعی شد که با استفاده از اطلاعاتی که از سوی افراد مقیم اردن به دست آمده بود، به هواپیماهای آمریکایی در فرودگاه عقبه حمله کرده است و ادعا می‌کند که این حمله خسارات جدی و تلفات انسانی به همراه داشته است.
این سازمان همچنین از حامیان خود در اردن تقدیر کرد و خواستار حملات به نیروهای آمریکایی شد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19006" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh8zS4iq1nFzryO7Xwc6qAS2ppYV3Gi3goPHngptQL_00N14IoLsduX9yujjpMdmob4EDAJ54pEnXqa4hLw4Z9NvfW1eFKk0DanrVkf1Q8jup533JZq8r7k8-eQhL3o71W-qk3RbbTQOCo3OO_fMJBUlEwiuKR226q6Pgt_p9SpvpuIH-39P-doXWI-dNzRTv6Le8bD0A6S8rIwDgkKbhLGYXx_orXIC_sFHEoNPvszEyq5HmDmod_NlZQVbSFVzZbiCOtLfBjBNDx_2nPz5Q3aMjFJA0i1Hgnd7MroBkloG08DuQ4dOAPGqqxReBefd7G6Te9K6bCv4wA_ifPkDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
سکوت وارش و واکنش بازار اوراق
وارش در نشست کنگره با وجود تأکید بر مهار تورم، از ارائه هرگونه راهنمایی درباره نرخ بهره یا سیاست ترازنامه خودداری کرد و بازارها را در آستانه نشست مهم فدرال رزرو در وضعیت انتظار نگه داشت.
بازار اوراق این سکوت را به معنای احتمال پایین افزایش نرخ در کوتاه‌مدت تفسیر کرد، اما رشد بازدهی اوراق بلندمدت و نرخ وام مسکن نشان داد نگرانی‌ها درباره تورم و بدهی دولت همچنان پابرجاست.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19005" target="_blank">📅 13:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">347.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19004" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 9  دوشنبه 20 جولای 2026</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19004" target="_blank">📅 13:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19002">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8esqwvGtFk4Vsllb0e-KmQ72s2H1EvcFLZnYpLjjk25-8IWW3kxLOJ-EQvjWSJBDbc0VYS8jOWTLtUugDG4_Y8qMSEEBf7wl95gVZuMdleAdX0l0VWXkS1R9bYHag-lhsDizpvuJP3GIMQ3zi_FvSRjUXE5kcMvWT1VZsqqeG7_kMvuHc5ZkwPTw2gpKX3TqFBUBqp43OIwsnzP-5AiSYhFKeGeV5zfetWCuG_gQFwuq0Ir8Y-brwkewFWHAfL9e_o8cpPUBN1BeYCD_1iT7WVe8oFoolNmJCPGAlOX_qMoX5_R_28BZ1JJtbLFxPs20OOHJprlWpCq-TIDMdVzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.
معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19002" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19001">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19001" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 9
دوشنبه 20 جولای 2026</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19001" target="_blank">📅 12:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19000">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدای انفجار مهمات عملکرده در تبریز و مهمات عملنکرده در تهران!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19000" target="_blank">📅 11:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18999">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18999" target="_blank">📅 10:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18998">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">UKMTO:
"یک کشتی در فاصله ۸ مایل دریایی شمال غربی شهر خَمْسر در عمان، مورد اصابت یک پرتابه نامشخص قرار گرفت و خدمه کشتی به طور ایمن از آن تخلیه شدند."</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18998" target="_blank">📅 10:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18997">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سخنان شنیدنی دکتر موسی غنی نژاد درباره حرامزاده شیادی به نام علی شریعتی!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18997" target="_blank">📅 10:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18996">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15659d093.mp4?token=vyhiNa53pldNfHFV9YPlEgsRCqIvqmB8OewH0eWXSDQ36eqJdNJ842xI-rSo1VtGJR1l8ZcxM7bnhAe7O8riYyRaYR-sNdDfSUCIT-AEXGL2L1xuj7WyMJAxqOy5418KRCoXVHLvo1exQMk9QCZI9w1ELVaMKCxbxE2yx0lWzuEyCeZET-seVv5-W15iD0sDjM82Rz1Fdvp3B73wFtlLANYkOrls0c-DWQ79KWimW7y7b3l2N3qa7u0OqZoKIpHzQ88H-EADx0rw2lo8bTcj-vh-WBaYQ97hfXdAXX12V8_NpGxEI7MeikWQxYp0upQVTa0_OAY8OePzgWae628csQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15659d093.mp4?token=vyhiNa53pldNfHFV9YPlEgsRCqIvqmB8OewH0eWXSDQ36eqJdNJ842xI-rSo1VtGJR1l8ZcxM7bnhAe7O8riYyRaYR-sNdDfSUCIT-AEXGL2L1xuj7WyMJAxqOy5418KRCoXVHLvo1exQMk9QCZI9w1ELVaMKCxbxE2yx0lWzuEyCeZET-seVv5-W15iD0sDjM82Rz1Fdvp3B73wFtlLANYkOrls0c-DWQ79KWimW7y7b3l2N3qa7u0OqZoKIpHzQ88H-EADx0rw2lo8bTcj-vh-WBaYQ97hfXdAXX12V8_NpGxEI7MeikWQxYp0upQVTa0_OAY8OePzgWae628csQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان شنیدنی دکتر موسی غنی نژاد درباره حرامزاده شیادی به نام علی شریعتی!</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18996" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18995">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله به بوشهر!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18995" target="_blank">📅 09:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امروز جلسه‌ای برگزار می‌شود تا درباره وضعیت فرودگاه بن گوریون بحث و بررسی شود و به درخواست واشنگتن برای اعزام هواپیماهای بیشتر برای سوخت‌گیری پاسخ داده شود.
برآوردهایی در اسرائیل نشان می‌دهد که واشنگتن ممکن است درخواست اعزام ده‌ها فروند هواپیمای دیگر برای سوخت‌گیری به اسرائیل را مطرح کند.
— شبکه ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18994" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18993" target="_blank">📅 09:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حملات سنگین موشکی ایران به بحرین</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18992" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدای انفجار در چابهار و تبریز !</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18991" target="_blank">📅 04:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:
ایران از نظر نظامی تقریباً همه چیزش را از دست داده؛ فقط تعداد کمی موشک، پهپاد و توان تولید برایش باقی مانده، ما تنگه را کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع ندارد</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18990" target="_blank">📅 04:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کویت اعلام کرد که سامانه‌های دفاع هوایی آن پهپادهای ایرانی را رهگیری می‌کنند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/18989" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تا لحظاتی دیگر پخش زنده بازی تیم های  ملی New Castle و سوییس از شبکه نسیم</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/18988" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f82WymtUrECsOAW9XiAWRAG9E2hNiy54gFCcas_KRqu-YhhfUXW-5eP3kHluDXGKhs3xQsTcmwv6k2-3QUOfXoO9tQTSBqFvinYzLCn8d7upBICmCY2JDpntdzyFz0k8vjXF7E23UvpnB-TdOFgvOcZeYj0wNsy9Ldc5nUzgNa5G8camEf_NRNWMy-os1nYMXDYW30v5bvpeOXINSqzo1jy9FzgTsd-ZOeX_UwK8Jo_D26L4-hmALn8gtpkQFQpgc1wDAYLDMen8ODIdnyW6tP7qK_F-mNC0tN7URz5SnPjPVwd9GVo6_zctNWR9NjzfX8DonWtu7Z3pMznbqMbX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت پرورش غیرمجاز دام و طیور در حمام</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/18987" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پمپئو: فشار اقتصادی خفه‌کننده به ایران را ادامه دهید تا اعتراضات داخلی در آنجا رخ بدهد!
وزیر خارجه دولت اول ترامپ:
واقعیت امروز این است که به‌زودی آن محاصره‌ای که سنتکام با کارآمدی بسیار برقرار کرده و همچنین تلاش برای کاهش توانایی آن‌ها در آسیب رساندن به کشتی‌هایی که از تنگه عبور می‌کنند اهرم فشار ایران را کاهش می‌دهد و در نهایت آن‌ها دیگر قادر به پرداخت حقوق نخواهند بود.
حماس، حزب‌ الله و حوثی‌ های یمن، آن‌ها نیز دیگر قادر به پرداخت حقوق نخواهند بود و پول لازم برای خرید مهمات را از دست خواهند داد. و زمانی که این اتفاق بیفتد، مردم ایران فرصتی را به دست خواهند آورد. این مسیر پیش روست. فشار اقتصادی خفه‌کننده، قدرت نظامی و صبر دیپلماتیک، به نتیجه‌ای مطلوب برای رئیس‌جمهور ترامپ و جهان منجر خواهد شد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/18986" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کشتی باری ترکیه‌ای گلدن لیو در اودسا هدف حمله قرار گرفت  کشتی باری گلدن لیو که پرچم گینه بیسائو را دارد و متعلق به یک شرکت ترکیه‌ای است، هنگام خروج از منطقه درگیری با محموله‌ای از غلات، توسط سه موشک کروز خ-۵۹/خ-۶۹ هدف قرار گرفت. این کشتی بخشی از «ناوگان سایه»…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18985" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/18984" target="_blank">📅 00:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">پناهیان:
اگه بی‌برقی و بی‌آبی رو تحمل کنید،
جهان رو آزاد می‌کنیم و آنها را هم بدون آب و برق خواهیم کرد.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18983" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سنتکام:
یک عضو خدمه ایالات متحده در ۱۸ جولای در شمال عراق در عملیات کشته شد</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18982" target="_blank">📅 22:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upp1twSLsDoOvkCq3kpQ9FKB3bxijVSwdjInicbtRP_GAW_TLFd2wSxpVXjfi6-ubaYWWJ2Pd3Ham6Xc-x2eAzEQIFPrBN8V1JHB7snhtwBJ-XOB6ey3ph--m-Ey2U96CC4DDDgzLPoaKD9xCAPYdD0uusZzxDZQcDsLrxdM-CRIkt7vNGGoMAI2DehmnCh1rWGKIc0G4mrzGbTUTfSxsa2p_i1J1qDd5UcWfFJsEQIdiVivJleluX-aucjOsZyFbJKaX9wfE_PbqfuTxr3MYbck0-oRNEtIOmICH6UiaWHjyRqllu2yHWC6Pgo9xfxszUpAG3tftbvcj0pLPf0uQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید معروف امشب موقع اجرا واسه فینال جام جهانی، رویِ لباس خودش فروهر نماد ایران باستان و آیین زرتشتی داشت.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18981" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18980" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18979" target="_blank">📅 21:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18978" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سایت والا:
ارزیابی‌های امنیتی اسرائیل نشان می‌دهد که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18977" target="_blank">📅 19:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک نیروگاه برق دیگر در کویت در اثر حمله ایران دچار آتش سوزی شد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18976" target="_blank">📅 18:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:  رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.  اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18975" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:
رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.
اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان ترافیک از طریق تنگه را بدون همکاری ایران تضمین خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18974" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai_N5sR3dK7DCQhsl0ls2o_7eZO-hjSFK5TwTC6uMqW9JpdpFBk5HZZ3yZflnSTqcCzIhcYh_M6Gb9C0zboycqX6tEY3q3MTHgfATonUIdT0lXyzQ1e7UgQAt4az1T_Eoqp3lacGXh4kdfcnb1EGbItwr_ZbUB0vDP9ejKXDbNVSxDofE6DpXN3_B58veJABNjUJhb77ApWCHwDydJB-xTgLt-vk2zRu0XVyL__6scPc5pU-Ro3I9lkWl3lTNO3u90IvLUVeRxTu0NA8MNrsHyCablLfB1MfOYLn3UjS-n24fbBOdJXdR67xDSSVTA9n2Vli4R4fKX49Zr_7F7LR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی جدید ایران  ایران موشک‌های بالستیک را به سمت اردن پرتاب کرده است   برخی از موشک‌ها به سمت بندر العقبه هدف‌گذاری شده‌اند که در جنوب اردن واقع شده است.  تلاش‌های رهگیری موشک در شهر همسایه ایلات در اسرائیل ثبت شد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18973" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18972" target="_blank">📅 17:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک تایمز:
هجوم‌های اخیر ایران به پایگاه‌های آمریکا در اردن باعث خسارات سنگینی شده است.
بیش از چهار حمله در پنج روز، موشک‌ها و پهپادها ده‌ها سرباز آمریکایی را زخمی کردند، چندین هلیکوپتر بلک هاوک را آسیب زدند و به تأسیسات نظامی کلیدی ضربه زدند.
کشنده‌ترین حمله روز جمعه در پایگاه هوایی موافق سلطی در عزره رخ داد که منجر به کشته شدن دو سرباز آمریکایی، مفقود شدن یک عضو نیروهای مسلح و زخمی شدن چهار نفر دیگر شد.
دو روز پیش، همان پایگاه مورد اصابت قرار گرفت و حدود ۲۰ سرباز زخمی شدند.
حمله دیگری تعداد قابل توجهی از هلیکوپترهای بلک هاوک را در پایگاهی در شرق اردن آسیب زد، در حالی که حمله‌ای قبلی به یک تأسیسات مسکونی ضربه زد و چندین عضو نیروهای مسلح را مجروح کرد.
مسئولان آمریکایی می‌گویند این حملات نشان‌دهنده توانایی فزاینده ایران برای غلبه بر یا فرار از دفاع هوایی ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18971" target="_blank">📅 17:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سبحان الله این چه وضعیتی است؟!
قرار بود به کمک تازیان بشتابیم تا فلسطین را از اشغال اسراییل آزاد کنند اکنون طوری شده که عربها از اسراییل کمک میگیرند تا پرتابه های ما به چاکرای پایینی شان فرو نرود!
یک جور کمدی پورن شده که انگار عطاران سناریو اش را نوشته باشد!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18970" target="_blank">📅 16:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18969" target="_blank">📅 16:25 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
