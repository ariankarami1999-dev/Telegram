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
<img src="https://cdn4.telesco.pe/file/AK1jvWB4vKBkGYutaI2ZI5hydeXHBdBB6H0OcWvntyaZrmTXf_deHtGBvzhDCMKRVu9IFOiU4pi6fr5lQ9j6Axnhvsly_06yS2Fvyoulxy9b0K_qUi0DDH9TXFna77XnZ6rIVJOVDbL2yqgqK7ylZ1xg88mGyLFoig89qcwseotLWrqAdy7IOVjebpXRzA5b5wB5yaoYBspddYf7CM2oJmvOtK6mWhjDYv3FuNLVfz8Ubezwrp02MSUs6ZQZGlSKZ9H6_zERm9ZsAlcNK1eMiRWdGRWb4zu-9kg6D9Jhgo1j738wtgahFZGIf-yQMlyKSe5wGl72pGDxohdvBMIKMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 18:01:49</div>
<hr>

<div class="tg-post" id="msg-19109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.
روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند که این همان چیزی است که ایران در ۲۰ سال گذشته پول خود را در آن سرمایه‌گذاری کرده است.
هیچ کاری که چین انجام داده، به هیچ وجه مسیر آنچه را که در مورد درگیری‌هایی که با ایران داریم می‌بینید، تغییر نداده است.
و در واقع، در برخی موارد، آن‌ها در مورد آنچه که به طور بالقوه می‌توانستند انجام دهند اما انجام ندادند، بسیار همکاری کرده‌اند.</div>
<div class="tg-footer">👁️ 526 · <a href="https://t.me/SBoxxx/19109" target="_blank">📅 17:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الان عرب ها بیشتر نگران هستند تا خودمان</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/SBoxxx/19108" target="_blank">📅 17:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/SBoxxx/19107" target="_blank">📅 17:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:
آمریکایی‌ها مخالف جنگ نیستند.
آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند.</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SBoxxx/19106" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ :
ایران برای کشتن سربازان آمریکایی بهای خیلی سنگینی خواهد داد.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/19105" target="_blank">📅 17:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-x4ON81Di-wrIOuRlL_40y-imTxuLsjEf0b9vKJo232ncHs4kE4aWPLI3yvNJKkQC-KEfAw19I-Rj5rCkTlTuJPjES9Ho85ZkTvsqO4Nf4F2ccmOvXmlGhmRYfufV7n89886Ilst0rZCAs13gdtgetvvDWmG0-cR_RW_8yxaDhMDyfUcSqNU4Gp2gqA9alqSPl7uZOWTiD3ZGD4BRtETjLIfOyZjDU5VkdSAVb3VtUb1Kw358RvLWgJ_MzPJxUtyWaJ-90-UzX4oGOX0-MPgFZ_7TtU7c6EHhA4o6EnIX927Kv7HXhnG9a2ugyfDN-Rh2KMMK9WAja5z3tsAO734Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
انتظارات تورمی مصرف‌کننده آمریکایی؛ آینه‌ای با تأخیر برای حرکت دلار
انتظارات تورمی مصرف‌کنندگان آمریکا معمولاً با تأخیر نسبت به بازارهای مالی تغییر می‌کند، در حالی که شاخص دلار زودتر به چشم‌انداز تورم و سیاست پولی فدرال رزرو واکنش نشان می‌دهد.
تداوم یا افزایش دوباره انتظارات تورمی می‌تواند نشانه‌ای از ماندگاری فشارهای قیمتی باشد؛ موضوعی که معمولاً از طریق رشد بازده اوراق خزانه و حمایت از دلار آمریکا منعکس می‌شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/19103" target="_blank">📅 17:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مرندی باوجود   حامی نفت کرود!</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SBoxxx/19102" target="_blank">📅 17:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دکتر مرندی در پاسخ به تهدید ترامپ دوباره دستور تخلیه شبه جزیره عربستان را صادر فرمودند</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/19101" target="_blank">📅 17:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfqwV1ZNMrtX0sM5VhuX-sZMuDHq3ScVqwcI27KaSFik2SDka5l3vSsMlONAxBh9hZyYqOiEAZ2WbGr9Wk44Sumygnebd8SgOmgSaiFUEO37pVdPijz3dL18Pahzyd_GuPAcAK88BkjQKhhqNhpfnvtC0oA-GzRe3mKeMrcjPrSa-sfOx0NlBS8Vm9d7BaI56h-BMgHgNzTeapJSxPilBqh5JmdBeG84RMw7GPXNEjjww-dfXBjwpHRcT_3cnp3INoFbPtfuUxm5If-bdqD_H1iEON7nhMOo9ihqYmCvOep-lN7T5ErurpiqTChAWzIYShPUo5kC_ZbznYVwg15Oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/19100" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:
از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/19099" target="_blank">📅 17:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پاکستان از ایالات متحده درخواست یک تسهیلات تثبیت ارزی به ارزش ۱۰ میلیارد دلار کرده است تا ذخایر ارزی خود را تقویت کند، روپیه را پایدار نگه دارد و وابستگی به وام‌های صندوق بین‌المللی پول را کاهش دهد.  این درخواست پس از آن مطرح شد که پاکستان در میانجی‌گری مذاکرات…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19098" target="_blank">📅 13:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/19097" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19096" target="_blank">📅 13:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">با این سبک بازی، چین عملاً دارد ضد محور ایران-روسیه در حوزه ژئوپولیتیکی عمل می کند که پیشتر به این موضوع اشاره کرده بودم.</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19095" target="_blank">📅 13:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینها اگر بدون پدافند درست بروند با A-10 قتل عام خواهندشد.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/19094" target="_blank">📅 13:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19093" target="_blank">📅 12:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ساعت 12 امروز با نیما در نشست هفتگی به بررسی پویه های ژئوپولیتیکی موثر بر بازارهای مالی خواهیم پرداخت.
لینک ورود</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19092" target="_blank">📅 11:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKbb6lafxwogAVzy5MIf3chpaRXqw0LZJFESBWOGiQOjUCeueJJFW-V5hyT0vwZgGTkZpPupNOjWcwexG3FElkqkSB0nxzPy44pm6BA-Axcip7XRiwzJOXA-S_AKUTTq75o_W4NjEvTUYR-6IJq_qfKYH2k80NWRzIY8iF4ZG-lNvi1Ef5WEMY5Klq8aXR15jFbFYpknatS0GrzeC-9a6it-THcyhxWxTtjsP_QLLR1EhIIdtZSvXA7YRzWmzKg2aBhv3H3rNoZWkfSePsjvXKjCwmj552tG7y0j618MJcHJ74-QYXAqCffT7_jHk7Lk5e7V8SaoP-j52kF2g3I4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.
توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19091" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهور آذربایجان، در سخنانی پس از دیدار با فردریک مرتس، صدراعظم آلمان، در برلین، به خبرنگاران گفت که مقامات سابق و فعلی آلمانی و روسی، این ماه، در باکو جلسه‌ای مخفی برگزار کرده‌اند.
علی‌اف گفت که باکو هیچگونه اطلاع قبلی از سوی آلمان یا روسیه دریافت نکرده و تنها پس از خواندن گزارشی در روزنامه "تایمز" از این دیدار مطلع شد. او افزود که مقامات آذربایجان پس از آن، تحقیقاتی را در مورد این بازدیدها آغاز کردند.
او گفت که: «به عبارت دیگر، از قلمرو ما بدون اطلاع ما استفاده شده است.»</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/19090" target="_blank">📅 10:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNt_vgMiny_cv8kxzidQZZKHemdt4tvPZMRB79AEYVOJO_W6uW7_d3NQEXf9AIFgI17G322qcvS_pAJhZMRJtEn_xUpu6OpgxM3r-NUE_rlSDYfd_xY3duDQdSuZVCTSMv1YJ7giBBjE1rWPezQhFkPOANXvvwO464PRpg4YA_uJyS2aBVD0faJ1UfBgkbSoOhsAlk_pQhIh5Utmb7fzyhcwba9PFzdsyf0Qju0DVrPSgsxxtH3gl7iAs_tpoTafk4qfUmaYhn0VS6okrEBNaUnAmgIcYjptmz4BAjG4Ta9IjU6BJ54HnDGEaaHTeca8v1t7_S2bfrm9vLkZaSiuNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاواریش ها هم یک تخته شان کم است!  در خود مصکو بنزین پیدا نمی‌شود و مردم سوار هم می‌شوند آن وقت می خواهند بروند در ماه نیروگاه هسته ای بسازند !  لابد چون مطمئن بشوند دست پهپادهای اوکراینی به نیروگاه هایشان نمیرسد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19089" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادامه حملات سنتکام برای یازدهمین شب متوالی</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19088" target="_blank">📅 09:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادامه حملات سنتکام برای یازدهمین شب متوالی</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19087" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19086" target="_blank">📅 01:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هگست درباره ایران:  ما این جنگ را شروع نکردیم. ایران این جنگ را ۴۷ سال پیش شروع کرد. ما آن را شروع نکردیم. آنها شروع کردند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19085" target="_blank">📅 01:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هگست درباره ایران:
ما این جنگ را شروع نکردیم. ایران این جنگ را ۴۷ سال پیش شروع کرد.
ما آن را شروع نکردیم. آنها شروع کردند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19084" target="_blank">📅 01:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله ایران به کویت</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19083" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaXIjKJ0M2iO5rPBKdtMeeAVP8QnACBVckX2fWmh--zsDw4APAIQEVNRoWL_EGETfxpsMJOKQjWjjOZ_iG98lsJJJ-sn0v4C25J00ifcOvGSMt-pitxVkN83UHR2MFJtfB3GMXcYwDzieu8eOIG6Wikdc__Op40z33TTHhOU0ZcAUXXBrzbQ-igS4a8HvP0I3j8BoYvEftoLdVrqNeDgHrbXY4M8Pb3C9dCPI9dMQ_gLLgaWKCOf5YkPC1HtGkRFkXBuhmBV9QOfCz7iuXHX4a4Ewk9rpAClqHOUCdlfcq4vDg2zfiMXEm6TLzO5ADHIJWud_K8ZJ9X0HtTAHmyt8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://nuclearsecrecy.com/nukemap/?&kt=10&lat=33.6506104&lng=51.5503762&hob_psi=5&hob_ft=2207&casualties=1&fallout=1&zm=12</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19082" target="_blank">📅 01:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اگر بر فرض چنین فاجعه ای روی بدهد، این دایره ها نشانگر محدوده های آسیب انفجار یک بمب اتمی تاکتیکی سنگین خواهندبود.  روستای زیبای جهق خیلی نزدیک به کوه کلنگ است....</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19081" target="_blank">📅 01:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19079" target="_blank">📅 00:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0e5eMdM5iunPE9FcchbvxJD2E7pPVxBbf6CPLuHy2bgv48FwozY21ho7wAg3ganCHhBOd9xslhLLowKYb7ettWdVjOhLU1-zVEQQ-0S4hizCu34t88511GNcegMcH7ozWUhyHZ5FWKk6tH73VGqTmxKsCvvHKE1R7XTm7bf_RZtidv92f-iBfxACblVFtUdMhGbJLtbc9qS9AS4JNpT20uTL_bqaJo2HuXzZNggNjELAL2h2R394A_uLaXgY8yu4Et_MfUsNiStOs0HWJvs6VXf93prilrKNccGa_oUzNR0yV2ZFRTjS9jWwPNyS42Q0Vu96VrnAcESiGsu0-SJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19078" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سناتور آمریکایی: آیا ما توانایی تخریب هر چیزی را که زیر کوه "کلنگ" در ایران قرار دارد، داریم؟  هگست: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19077" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سناتور آمریکایی: آیا ما توانایی تخریب هر چیزی را که زیر کوه "کلنگ" در ایران قرار دارد، داریم؟
هگست: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19076" target="_blank">📅 00:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پیتر هگ‌ست، وزیر جنگ ایالات متحده:
«روسیه و چین در برخی از فعالیت‌های ایران، و در سطوح مختلف، به این کشور کمک می‌کنند.»</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19075" target="_blank">📅 00:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0KCO5qdlDBjrhfBXlroaoCpv-LB0xMDCSr23MeN4buzDmkAjo6n9xV4IpOAqP2aMA9uceECi2B0LIukASj9jU1nWLlqVN-JF8gTKuaJlLoeVXevYtXpPJ5ztkUgTmY3wRVWQc6NZvHvfJObfaOIHYKuqjPpnLrPDjxN-PMl6GutERAbHqrNz-EiaLyJ4OuTVW27kILCsyYFI6FA0iTsn-jjd9qTTMNUeZAEKQWzu4NtpKC090O8EWOHsSiC7wkufkljFEPacAOGZIvlVbIToMAlfVzASFpHf6xZQHpR3QHiGFjEWG7RsndOkO7HhDxRcd78ADAJ2HvV8DwpfgzgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19074" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN6aaCv3-RcHYnotZz4lmtZ7Qh7tKxvp6gwrXfMiEyOxr6UddulmrxE-OGQHD1vogYD7waCBHStncCg3NlJ_2WqqzbLAicoeNVUsylgeev7QvU0MKt7HjuMf-hIxBnVA-ihp9QzvSrV_ifn-4TBN6KNgCLoFaFC5Wvk9EUa9aKew5yAfMEAUipRfhSEvzlWuRH0_QI37jx99JZK_o08AL7Hpzr48gCZhq7jQ20pkwuCXDfU7aCkiLcC9vdO-Vak3dbIT9zkNV_RoaLbWdlltqpoOTwlRInvW44BEPY2tVuRCtr4HOKOfFt9Nj6ltGTsfCa9PANt2czmEZVFxgFGn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایینی قرار دارد و پیش بینی می شود طلا ابتدا ریزش و سپس رشد داشته باشد.  محدوده مناسب حمایتی 4015 الی 4020 برای امروز.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19073" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.  این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19072" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">️ترامپ:
ما اصلاً کارمان با ایران تمام نشده است،
ما در حال حاضر قصد ترک خاورمیانه را نداریم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19071" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره ایران:
بچه‌های جوان را می‌کشند انگار هیچی نیستند، انگار آبنبات هستند. کارهایی که انجام می‌دهند دیوانه‌کننده است.
آن‌ها مردم را به صورت تصادفی می‌کشند—بیش از ۵۲,۰۰۰ نفر—و هیچ‌کس درباره آن صحبت نمی‌کند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19070" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها به شدت مشتاق دیدار هستند.
تا زمانی که برای دیداری معنادار آماده نباشند، ما هیچ علاقه‌ای به دیدار نداریم.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19069" target="_blank">📅 18:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد تا یک یادداشت اعتراض‌آمیز درباره هدف قرار گرفتن یک نفتکش کویتی به او ارائه دهد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19068" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد تا یک یادداشت اعتراض‌آمیز درباره هدف قرار گرفتن یک نفتکش کویتی به او ارائه دهد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19067" target="_blank">📅 18:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7Uh2YnyjuEwuLRPIEcO09qbPmDHmM_m-Edvp_bJX1Wb-HvtPIztYWMBiqGdfX71AhWAFrUGMqQkNkDGJcSVfBUtlOK0CA-LY9MoEeImT7tUudQX04WX42w9UzbN7-lSa2PWYhmz_l6IfamfqS1u5NGGt8QDuBQuzVeHUPHUj73TTNuabX9tZyhIPsVJXWs-xnnamiKjF4JtTK8nbvu88hUh34-rh_FEO6Ffrs65kziZqaOjmxES6nr8H0c-v3S8F0YRQDJZQoEnoISb8ecKvDrc0qGGEIcTdPJ4hz-gVGYs3L5h1knUcM-fPXGBTC55Rrri6Veb6Qvsi63WjsrZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد تند ثابتی از عراقچی و برنامه جواد موگویی</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19066" target="_blank">📅 17:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الهام علی اف:
روسیه دیگر به دلیل شکست پالایشگاه‌های نفتی خود، کاملاً قادر به تأمین شرکای سنتی خود با نفت و گاز نیست ‌.
«از سرگیری سرمایه‌گذاری‌ها در زیرساخت‌های نفت و گاز توسط بانک‌های اروپایی به آذربایجان اجازه می‌دهد تا صادرات منابع انرژی خود به اروپا، از جمله به آلمان را به طور قابل توجهی افزایش دهد»
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19065" target="_blank">📅 17:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده:
چین خرید نفت خام ایران را حدود ۴۰ درصد کاهش داده است</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19064" target="_blank">📅 15:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19063" target="_blank">📅 15:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19062" target="_blank">📅 15:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31dabbbd67.mp4?token=SBHLE9-DyZh5kQqs3PEOXRoyHSy4s-IzmjMXpfB_OCaH5prAimudEWzs8OBUlmlNIPP3pAo-IsZsun2paEPZDDvguSr7wPpxs86_D1fUlCFfumQjOsdhxDyvI8JZbPQVNMNEhRn1LrlMiI3HImTCtyNDhV3LoJ5eGP2iYxQiwyCp51r2Wu7ZRg63VmHF0gIFOj4z3t8WSix1AG1_xRx31dElNRzEMnTR8uFTOjxhuRSDRypQe3hnDedeKv65gygd3ljduQ5RlYk0YQVnzjhq71t3hQAo6-M90iq1vXm4pEJIYcBEhTFvkdxn0GYkM82PmBzXJ3sd8N3s25YEWYsSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31dabbbd67.mp4?token=SBHLE9-DyZh5kQqs3PEOXRoyHSy4s-IzmjMXpfB_OCaH5prAimudEWzs8OBUlmlNIPP3pAo-IsZsun2paEPZDDvguSr7wPpxs86_D1fUlCFfumQjOsdhxDyvI8JZbPQVNMNEhRn1LrlMiI3HImTCtyNDhV3LoJ5eGP2iYxQiwyCp51r2Wu7ZRg63VmHF0gIFOj4z3t8WSix1AG1_xRx31dElNRzEMnTR8uFTOjxhuRSDRypQe3hnDedeKv65gygd3ljduQ5RlYk0YQVnzjhq71t3hQAo6-M90iq1vXm4pEJIYcBEhTFvkdxn0GYkM82PmBzXJ3sd8N3s25YEWYsSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای روزنامه جروزالم پست:  ترامپ پیشنهاد قطر و پاکستان برای آتش بس 10 روز با ایران را به شدت رد کرده و اعلام کرده حملات به ایران ادامه دار خواهد بود.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/19061" target="_blank">📅 15:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19060">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ادعای روزنامه جروزالم پست:
ترامپ پیشنهاد قطر و پاکستان برای آتش بس 10 روز با ایران را به شدت رد کرده و اعلام کرده حملات به ایران ادامه دار خواهد بود.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19060" target="_blank">📅 15:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19059">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast Text.pdf</div>
  <div class="tg-doc-extra">305.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19059" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 10</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19059" target="_blank">📅 15:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19058">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHqJeLO1JesoIBY4EcDA9sQVSJTdCa5W57mhsOz3EJJPl_k-YCwtHTOkskhZtwjQLAlvYNdLYSLKo-Ecc6s0e8F0wEnpNi-rq0u0LD2BDKxPIIb57THbmGOyISavqruu1fMtKVuWBhUpPTVDRr3aSPU6gKApImXlLelvtQIOsJYkETbsEhzfbuXGRNbIa71B-vHKltO9DFXiz5wNXLzhMP9RIv_fsHlnXsqa09az7TKK4ABRVj--OHy9oMmhz5TQjxPUnlApCgwsv56dZd7-dZPDntTqS9D-fbLbH8ZBqxiF0_qiNSNAwKokD4UTQV1aSH4yHa21dqW4A3a7_HGR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایینی قرار دارد و پیش بینی می شود طلا ابتدا ریزش و سپس رشد داشته باشد.
محدوده مناسب حمایتی 4015 الی 4020 برای امروز.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19058" target="_blank">📅 15:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19057">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 10</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19057" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19055">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/SBoxxx/19055" target="_blank">📅 13:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19054">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حمله ایران به کویت، بحرین و قطر</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19054" target="_blank">📅 13:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19053">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایران می‌گوید که زیرساخت‌های داده آمازون در بحرین را با موشک‌های کروز نابود کرده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19053" target="_blank">📅 12:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19052">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شما قدرت رنگ آبی را ببینید فقط که تا کنون این پایگاه کذایی «الازرق» حدود 15 بار درهم کوبیده شده اما هنوز نه تنها سرپاست بلکه بقیه هواپیماهایشان را هم می برند آنجا!  حالا اگر اسمش «الاحمر» بود با نخستین اصابت شاهد واقعاً در هم کوبیده شده بود!  آبیته!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19052" target="_blank">📅 12:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19051">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت خارجه چین در مورد سیاست هسته‌ای ژاپن:  از زمان به قدرت رسیدن تاکیچی، نیروهای راست‌گرای ژاپنی نیت خود را برای احیای نظامی‌گری، رها کردن اصول سه‌گانه غیرهسته‌ای، جستجوی سلاح‌های هسته‌ای و ادامه مسیر نادرست آشکار کرده‌اند.  اگر ژاپن به تلاش برای اصلاح اصول…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19051" target="_blank">📅 12:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19050">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">— وزیر امور مالی اسرائیل، سموتریچ:  «اسرائیل هیچ علاقه‌ای به پیوستن به درگیری محدود میان ایران و ایالات متحده ندارد؛ وضعیت فعلی بهترین حالت ممکن برای ماست.»  «هدف ما سرنگونی رژیم ایران است و بهترین راه برای رسیدن به این هدف، ایجاد فروپاشی اقتصادی آن است.»</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19050" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19049">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لینک نشست امروز با نیما  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19049" target="_blank">📅 11:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19048">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی (IRGC) اعلام کرده است که به یک پایگاه نظامی آمریکایی در منطقه الرکبان در اردن حمله کرده و مدعی است که در این حمله، چندین سرباز آمریکایی کشته شده‌اند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19048" target="_blank">📅 09:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19047">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی اعلام کرد که دو تانکر نفتی که قصد عبور از مسیر ناامن در جنوب تنگه هرمز را داشتند، پس از انفارهایی که منجر به آتش‌سوزی‌های گسترده شد، متوقف شدند. سپاه همچنین از ارتش ایالات متحده به دلیل گمراه کردن این کشتی‌ها انتقاد کرد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19047" target="_blank">📅 09:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19046">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال‌‌استریت ژورنال: اسرائیل مدعی انتقال هزاران سانتریفیوژ ایران به «کوه کلنگ» شد
این سایت در عمق حدود ۱۰۰ تا ۱۴۰ متری کوه ساخته شده و به گفته کارشناسان، هدف قرار دادن آن بسیار دشوار است.
اسرائیل معتقد است این انتقال می‌تواند تلاشی برای بازسازی ظرفیت غنی‌سازی ایران و محافظت از تجهیزات هسته‌ای در برابر حملات آینده باشد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19046" target="_blank">📅 08:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19045">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزارت امور خارجه آمریکا:
ایالات متحده اقدامات خطرناک و تهاجمی چین علیه ناوگان دریایی فیلیپین در منطقه "توماس شول" در دریای چین جنوبی را محکوم می‌کند و  از چین می‌خواهد که فوراً اقدامات بی‌ثبات‌کننده خود را متوقف کند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19045" target="_blank">📅 02:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19044">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک مقام آمریکایی:
اگر ترامپ تصمیم به گسترش جنگ بگیرد، حملات شامل تهران و سایت های هسته ای می شود.
اسرائیل ممکن است در جنگ ایران شرکت کند اگر ترامپ تصمیم به گسترش دامنه آن بگیرد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19044" target="_blank">📅 02:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19043">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوزاری گدازاده کم بود، گروهبان قندلی هم به فهرست گه خورهای علی دایی افزوده شد!  گویا سرگین شهریار چندان لذیذ است که این مگسان آن را انگبین می بیینند!  پفیوزهای ... مال عوضی</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19043" target="_blank">📅 02:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19042">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!  ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19042" target="_blank">📅 01:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19041">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عادل فردوسی پور > New Castle
علی دایی > New Castle
کریم باقری > New Castle
99 درصد ایرانی ها > New Castle</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19041" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19040">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اینطور که پیش می رود فردا در هند عزای عمومی اعلام خواهدشد.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19040" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19039">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIulk98NToSbDYKOw4r6CNPuHYFnqMnmKMTd4xqKKZKpP1NMuUvzNST-O0KWfkbjfqCXw82YZkUUl_3q83rCz9dDZQk-whhBj4EjsiQx49wmCwNrvqQVSuVqEwmvfFps6q04EeKcWkxO7fEeyTXLI-9lGkzDMInnTvJs5CKAJRvMVgkPFyd4e6Wn7gMhGpzM6fS2LAdRadAi9OY0jkcC9blFrOd4dMJxEpklSym51D-_8yUkLDF_P3_JL5PDQUPY4Eop7u6Y6J7r4wIU5iIkcRMKT3AxcuW7Ci8nD7P8SlfUKWvMzG2elL2yFdD6TxoWQxqJTE5FLIEUwROu0oI1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی نفتکش دیگر در سواحل عمان هدف قرار گرفت!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19039" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19038">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واقعا به نظر می‌رسد این الاغها تا یک
جنگ هسته ای
جهانی راه نیندازند دست بردار نیستند.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19038" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19037">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزارت خارجه چین در مورد سیاست هسته‌ای ژاپن:  از زمان به قدرت رسیدن تاکیچی، نیروهای راست‌گرای ژاپنی نیت خود را برای احیای نظامی‌گری، رها کردن اصول سه‌گانه غیرهسته‌ای، جستجوی سلاح‌های هسته‌ای و ادامه مسیر نادرست آشکار کرده‌اند.  اگر ژاپن به تلاش برای اصلاح اصول…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19037" target="_blank">📅 00:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19036">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کاخ سفید اعلام کرد که ترامپ روز سه‌شنبه در مراسم انتقال با احترام پیکرهای چندین نظامی آمریکایی که در هفته گذشته در جریان آخرین دور تنش‌ها با ایران کشته شدند، در پایگاه نیروی هوایی دوور شرکت خواهد کرد.
این نظامیان شامل دو سربازی هستند که در حمله موشکی بالستیک ایران در روز جمعه گذشته در اردن جان باختند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19036" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19035">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سنتکام:
امروز ساعت ۴ بعدازظهر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، دور جدیدی از حملات هوایی علیه ایران را آغاز کردند. این حملات برای تضعیف بیشتر توانایی‌های نظامی ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شوند، طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19035" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19034">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش‌ها حاکی از آن است که مقامات نزدیک به رئیس‌جمهور آمریکا، ترامپ، تحت فشار قرار دارند تا پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرند.
آمریکا امکان آتش‌بس را رد نکرده است، اما اصرار دارد که این آتش‌بس باید طولانی‌تر باشد و به تفاهم‌های خاصی در مورد تنگه هرمز گره خورده باشد.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19034" target="_blank">📅 21:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19033">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حمله دوباره ایران به بندر عقبه اردن</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19033" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19032">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اخباری از حرکت نیروهای زرهی ایران به سمت کویت به گوش می رسد!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19032" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19031">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اخباری از حرکت نیروهای زرهی ایران به سمت کویت به گوش می رسد!</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/19031" target="_blank">📅 20:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19030">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">— یک کشتی در ۱۷ مایل دریایی شرق امارات متحده عربی توسط یک پرتابه مورد اصابت قرار گرفته است.
هیچ تلفاتی گزارش نشده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19030" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19029">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ:  «نتانیاهو به هیچ وجه، به هیچ شکل یا فرمی، در حالی که در ایالات متحده است، دستگیر نخواهد شد.»  «او علیه جمهوری اسلامی ایران می‌جنگد که اخیراً ۵۲,۰۰۰ معترض بی‌گناه را کشته و در ۴۷ سال گذشته سربازان آمریکایی و دیگران را کشته است.»  «تنها کسانی که باید…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19029" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:
«نتانیاهو به هیچ وجه، به هیچ شکل یا فرمی، در حالی که در ایالات متحده است، دستگیر نخواهد شد.»
«او علیه جمهوری اسلامی ایران می‌جنگد که اخیراً ۵۲,۰۰۰ معترض بی‌گناه را کشته و در ۴۷ سال گذشته سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید دستگیر شوند، کسانی هستند که ایران را به این مارپیچ بی‌سابقه مرگ و ویرانی کشاندند، چیزی که باید سال‌ها پیش توسط رئیس‌جمهورهای قبلی حل و فصل می‌شد.»</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19028" target="_blank">📅 20:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سازمان صدا و سیما:
یک کارخانه صنعتی در حومه شهر خمین، ایران، حدود ساعت 7 بعد از ظهر مورد حمله قرار گرفت.
هیچ گزارشی مبنی بر کشته یا زخمی شدن افراد وجود ندارد و مقامات در حال بررسی میزان خسارات وارده هستند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19027" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ذخایر نفت خام در ذخیره استراتژیک نفت ایالات متحده حدود 5.1 میلیون بشکه کاهش یافت و به 311.4 میلیون بشکه رسید که کمترین میزان از سال 1983 به شمار می‌رود.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19026" target="_blank">📅 19:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر امور خارجه فرانسه:   امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19025" target="_blank">📅 19:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر امور خارجه فرانسه:
امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و در ساعات آینده به فرانسه باز خواهند گشت.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19024" target="_blank">📅 19:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVrCqBFdRaQkJmAnSs9rlLD2VTICmsNRZFHCo1v-blU3418kvFp1fxTrW3YvwaSL2NiNxOU1tLyB5CglpP_XJmqVQOQPJKrtvABFTaXoxukM396PE5MRa1DJiJ2Mpq3Tnf0nvvH6H0ULl9v8W1U_MiDCo1poSCPBcXltlDCSPg8d0-7VuFUhFSVaIJmNE_WFQe-Cl6l1NVef5TH3byBnC0ikfuK0AnRkdzoQ3BG6BlOaCuKvHkV31jMIH52n1u1BTbcY_ahn1QcReKy-dH2iCI8a-7q3YneLZ24XWONOPI7_aCGTlW6_aKRkvV4WHPx6WvqsEwS6GCiSxZYACpVWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.  معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19023" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چهار شهروند هندی در جریان حمله به کشتی تجاری "My Golden Leo" کشته شدند، در حالی که این کشتی در حال خروج از بندر اودسا در اوکراین بود.   سفارت هند در اوکراین به دقت وضعیت را زیر نظر دارد. هند این حمله را محکوم کرده است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19022" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19021">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYz_kA8gSBpTUcp0w_F5LM8FxjtCNImPeCWQ7_ysGZqA6xtcA_sqpWEmh2TgIeWLYjMy074UuCsN-Hcq3tYzEBLPLwPC8iATu-DpIUK9rjkfR1O0LypqxhI1fT81GGiTF_BzfzZdR3oX2UAygDk7Z77mtzfXnpzwdq4xa8l7WkOEOVtzOQ4rkPK6FidDmKbkTBN3c930KeqssXNIX6whKInmaHTQ2OLbkNc65_WfBzwOO3TI55yrjbzczkpJxqE9rNkRaafjIRa50unw2GOqoasL8c4MAggMACPkL1XCSmJGmuB_kmudpdk3gylMCFw4F4I5JgS636qZZne4VkuMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19021" target="_blank">📅 19:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19020">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19020" target="_blank">📅 18:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">از دیشب دیگر دامنه حملات آمریکایی ها به جنوب محدود نیست و تبریز و شیراز هم مورد هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19019" target="_blank">📅 18:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19018" target="_blank">📅 17:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19017">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آتش‌سوزی در یک کشتی باری یونانی رخ داده است. این کشتی در نزدیکی تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت.
— رویترز</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19017" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19016">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار در شیراز</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19016" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19015">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب از هرمز ۲۰ میلیون بشکه نفت در روز عبور می‌کرد که برای ۷ میلیون ش جایگزین پیدا شد (خط لوله شرق به غرب عربستان)</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19015" target="_blank">📅 15:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19014">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19014" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگر یک بار دیگر هم فریب میخوردیم با ۲ بار قبلی می‌شد ۳ بار و این اصلا خوب نبود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19013" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قالیباف :   آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.   ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19012" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldzu8BuxNjXYLPE4t5WqmnlLKaN9gy7Ovwla7LrH3iY6uUQLqQX9BPXW1N4Li31EZyj_0cAw-0DRxy4xXrIrB_jPBYMopIdPQAfprYrB_EoJVqHsiLeWhPJeSqWRsX-8hxGb984FLRs9EgwVCa8DcFRDuiF9-bhOSbZ5gj5kKCkqL117oK3C3lxbpCqGxSWVTxvaplLdWTjK_yeUmqC0CJRCg_1tioUkDYXufhx0vowBFdO7Pt2i3LMezflGvY2IVhYHnjdTfHkvZtCvV53b9EVJaPhJ8qVjm8NXXfWp8rROgt5M-lpk4wW2LN279ZiZZbRAsViWCxAs1J9OMHFoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف :
آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.
ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را آماده کرده‌ایم. اقدامات باید ادعاها را تأیید کنند، نه اینکه با آن‌ها در تضاد باشند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19011" target="_blank">📅 15:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.
این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون تصویب پارلمان صورت گرفته است.
این درخواست در حالی مطرح می‌شود که تنش‌های ایالات متحده و ایران همچنان در حال تشدید است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19010" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دلار فردایی تهران
⏳
188,700 فروش  بازتاب انتشار مواضع ملایم شده دو سوی نبرد روی قیمت دلار داخلی  نکته — موقت است و دوباره بالا می رود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19009" target="_blank">📅 15:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ببینیم آمریکا همان بلایی را که با قربانی کردن اوکراین بر سر روسیه آورد، با ژاپن بر سر چین می آورد یا نه.  در نشست با نیما (پیام ریپلای شده) مفصلاً درباره تاریخ تنشهای میان ژاپن و چین صحبت کردیم.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19008" target="_blank">📅 14:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بوی مذاکره می آید…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19007" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
