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
<img src="https://cdn4.telesco.pe/file/mnzZq2Ib38_A-QVCZ8hsoI6hXCWl8NNCRspsoENeE5McKNF_uerfQXzm9VifvDorwAH8YTu7KFkoFJGzOuwJcvT4pqobM72JtghdHPKsz7zJCK0-kpZ9y7XR3CuKqNcOt4ds0FuM-DKhBHCRu8zVxOkG00hQdqPGIgJQch5xM2mpYj4sUlauFXYAJ03vXhJFKYZb5pIwOTXQfCQIXKZ7nfNjVB1G9D0pw5N70xzkyaxuCAl6yBSthqYbjYR7zu1v1DI14kMMzK_ASXJ4VYBcsdN8Jry34OeGAccfJJPzdvAMcwlUEwLgr33QU0PI3wx94r4UiYDCjty6nMNZnOoNzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coK1LljTQ4Ih-_izl3FfNGcMuV40FtGLqIkzihLz0DQkCm1wpFdnEMC7TXicOnrAGuzODChiw8gRh43-fAFSM9SGJgvLWaFfrFpuJ1BN0XCU5ZpNYagqYrmAXT0u1_Ug-XarnUF84bg-Nco0s1gnnXuDrtHdLV_hH0WjBg4iJptJ8PvzknZW6vRZlwWT515L5i8NyckWWT2mWMC9iXt1gALw-sBtTQA9ybDFYgPmmQF8GMw6Quuh-KxKWN6DLBSulj5MoWrsb2S6eg-lSw_llu96jR3fqPeAEAgwEqEtPfzvM65F9Nm1WyWMWzWtiq9RM1v8kU4QOcXdp5kcsl_JGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.
پس بهترین استراتژی برای امروز:
خرید پس از یک اصلاح سنگین 400 پیپی است.
محدوده های پیشنهادی:
4366
4355</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/SBoxxx/20970" target="_blank">📅 10:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn17AU3Id7KMWUSWUqc5bmnxJSt3i-cd1lb501biCUfsX0OJjzpY42hNA9guktghbtUw5XfoC1DopyDFwtF0vYRDHaY57I_4_Oa6nQZ-F4aGvxnK565qvpH0S6LNKw7CQBfsC1ClLxicXyWJuFzo2GnrLkGukgRTC0jRS9hLQmDqlyYG5QnhxfRK-MvuMtQdxIW3ALFWA2URING82fw7N9F-qut0t_NUxZHyYxQzkbh2asyocDflbEfS8KJXnEsOv_ANvvnHmhhQIARwLpc4MigATaBsCczPpIEx-ZX0HgMM4TVOWGEQCVjTYk14cvFFbW-Xk9wDaSiuSDYVD4FgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد و انتظار یک اصلاح نزولی قابل توجه (دستکم 400 پیپی) در طلا داریم.</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/SBoxxx/20968" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر دانشگاه تهرانی ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=QXk_9ZHECEo0kn5RQEbr8a1DRCxQ53jazwCtrLzrMeNyl6Di6NbFE9KCAxxt9GMST2pXUjcWFqr2TQ67zUFZtv39QZR-RJEhJB9R_zmyYoW5n0SqsYMkjWy7L2AiH40uKPXUQdcKzi-8nBfAdP5evwX-tTFlqVRVeCBI7RzFeRbYquMuIyhWMxSrxfLxZj6Y3AZ10fT2vK8V8mmP88dTPRp8jEwjL8D4PX9bNy1he0RyZ7Bfu9s2nKe-gLKG0UdiMYI-9YboijqKsu_OBenHjJxmo9HCEmjkpxaQXBS8BvPOYqRZyLqHevYqulZM9T4oFP8DQFCcQJWg43tFTvdtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1dc786c4.mp4?token=QXk_9ZHECEo0kn5RQEbr8a1DRCxQ53jazwCtrLzrMeNyl6Di6NbFE9KCAxxt9GMST2pXUjcWFqr2TQ67zUFZtv39QZR-RJEhJB9R_zmyYoW5n0SqsYMkjWy7L2AiH40uKPXUQdcKzi-8nBfAdP5evwX-tTFlqVRVeCBI7RzFeRbYquMuIyhWMxSrxfLxZj6Y3AZ10fT2vK8V8mmP88dTPRp8jEwjL8D4PX9bNy1he0RyZ7Bfu9s2nKe-gLKG0UdiMYI-9YboijqKsu_OBenHjJxmo9HCEmjkpxaQXBS8BvPOYqRZyLqHevYqulZM9T4oFP8DQFCcQJWg43tFTvdtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهریار میگه آدمهای پیشه‌وری بچه‌های گرسنه تبریز رو جمع میکردن و می‌گفتن: « بچه‌ها بگید خدایا نان بده». نان نمی‌آمد، سپس می‌گفتند «بچه‌ها بگید
#استالین
نان بده» و نان می‌آمد.
اینها علاوه بر بی‌وطنی چقدر کثیف و کودک‌آزار بودند که با روح و روان بچه‌های گرسنه آذربایجان بازی می‌کردند
_sheshgalani_
@uttweet</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SBoxxx/20967" target="_blank">📅 09:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خریداران جهانی سوخت روسیه در برابر لایحه تحریم‌های ایالات متحده مقاومت می‌کنند
پولیتیکو گزارش می‌دهد که واکنش جهانی به لایحه تحریم‌های روسیه که به تازگی توسط کنگره تصویب شده، سریع و شدید بوده است:
مسکو هشدار داد که این لایحه تنها جنگ علیه اوکراین را طولانی‌تر خواهد کرد. هند قول داد از منافع خود دفاع کند و پکن در برابر آنچه آن را «حاکمیت گسترده غیرقانونی» نامید، مقاومت کرد.
این لایحه که هنوز به امضای ترامپ نیاز دارد، تحریم‌هایی علیه رهبری روسیه، بخش انرژی، صنعت دفاعی و شبکه حمل‌ونقل که سوخت‌های تحریمی روسیه را جابه‌جا می‌کند، الزامی می‌سازد. این لایحه همچنین به ترامپ اختیار می‌دهد تا تعرفه‌های ۱۰۰ درصدی بر ۵ خریدار بزرگ جهانی این سوخت تحمیل کند؛ بندی که از پیش متحدان خود واشنگتن را نگران کرده است.
از سال ۲۰۲۲، چین ۵۰ درصد از صادرات نفت روسیه را خریداری کرده، هند ۳۷ درصد، ترکیه ۵ درصد و اتحادیه اروپا ۵ درصد. اتحادیه اروپا همچنین در آن دوره بزرگ‌ترین خریدار LNG روسیه (۴۹ درصد) و بزرگ‌ترین خریدار گاز لوله‌کشی روسیه (۳۲ درصد) بوده است.
از سوی اتحادیه اروپا، منتقدان لایحه استدلال می‌کنند که این لایحه اختیارات بسیار زیادی به ترامپ می‌دهد؛ یا برای ایجاد استثناها و معافیت ها برای شرکای بزرگ روسیه مانند چین که واشنگتن به دنبال گسترش تجارت با آن است، یا برعکس، برای اجرای انتقامی علیه متحدان ایالات متحده که ترامپ از آن‌ها خوشش نمی‌آید، مانند اتحادیه اروپا، با استفاده از خریدهای نفت و گاز کشورهای عضو تکیه‌گاه (اسلواکی، مجارستان) بهانه می سازد.</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SBoxxx/20966" target="_blank">📅 09:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به گزارش برنا، در نخستین ساعات بامداد جمعه ۲۷ شهریور در محدوده خیابان دانشگاه زاهدان تیراندازی رخ داد که این خبرگزاری دولتی آن را «حمله به یک ایست بازرسی» توصیف کرد. برنا اعلام کرد در جریان این تیراندازی یک مامور نیروی انتظامی کشته شده است.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/20965" target="_blank">📅 08:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
نیروهای مسلح ایران به آمریکا درسی خواهند داد که هرگز فراموش نخواهد کرد</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/20964" target="_blank">📅 01:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حمله ایران به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20963" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک کشتی ترکیه‌ ساحل اوکراین توسط پهپاد مورد حمله قرار گرفت.
بر اساس اطلاعات اولیه، کاپیتان و یک ملوان کشتی در این حمله کشته شدند و ۱۳ نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20962" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20957" target="_blank">📅 21:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20956" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:
تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است.
هر احتمالی از جانب من وجود دارد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20955" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">— اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف، از جمله شرایط اضطراری بود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20954" target="_blank">📅 20:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:
من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20953" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk8De3DTT8CqIKw3zWX_hSpCBGjn5ow93Gzrq1x8rSsGwJ_ohEKSma1NP1KWg5GW8bJIZtZE1JzxzSo5NO85g_0vqmPcBzz0-rQRkqfFGlKSzrHMNfa60GpHRiXA6alkgLZEj9RtgcpmkEP1xi5ySd6reJLp0SJBlvSYvECoV2J84KnU_kFeetU2hPoRPtJkBwiGrY-_svLc8rFJitqepORWD8vH7oKOe9thGZ7a41sAmrLteuzbyJmhJm1Xk4bcVs_wVvOxaz62kGeUu_WDYhe3T84fs2rBNul_glLwtfIKVfw5XsR8-BefFIkokWjBDP3_y6YVthWrBHftnaD1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6heC1XzxYLQd8wt0-DC8_ZdZCE9nuO0uq_HdGF2aLRbg2BpovSJrNo78gFtxi7EyA8W6uwFnPGj9oW6gd7hRHCxR0-TUYadHMuu7Paz9krLzywYHv1CM6gJer3Hc269_0Z0HMdS6R2b9WSLyZAx1TpTtdPVu572WiHWb2tuj1-e5kUH_T3UkRQkHECrif4Eqt11bAXDPYNjCBWWxsCce71kCMUx5XWOv1qxGBnlpkLQTGX68R2_WDfmA3PYYzKW4TN9UCmd9Z5wMU0tVvhLlD2yaYrr7zwtaxki-hAxPfiVWbZgDsCohx7KdpfnTWztBk5Hs91jz-4w21rZybj3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCgdP5etzmnPZH8OtuDM9qw66dqkNcPXGNr_WYKuTOCU9Ovd6cFyCuVhBKA9CM-Leq1JDkjjhoDtgRQu9zCuEPwfXMfQgw59tw9EBDB2x4KG5Fo6m1WfJc6bqMkOAjTirmLK3OkarCmlsanS7drR5gpL4JP30kEtls88YbwXLjQQOy3435JoSxdMcytYMNxhqC8cqoNPNU10oCaEavgbBWmVi7E3AgLgMBhth0a07nR7FleVxOAazuCETbndRaAgIGN0xQYxiyTkBEwTm577dow-xhb1l6Gcni5cOXAaaw779CTkDBnSwO4SyB6Hrr9PHSC4PC4Pbgp7WMRKEYNLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skDIrhpyivtWOPbPLeGZXweJ9Yzwcjq54Tw5aXAAHjbaHzdSqrQiAgQxCwGtblc3N6gHDCcYwGV41JvTQBvhhsaeA9QmRXz6fYDS2eqrOAVZiadcjrlqp3jlhdBZdJViUuWpmM7ZqGGsmPg21qAHMOLbjQiT5mVQygHZzt6khLMxHS0Avjkk2u88ewRNp-E03W3gpN_B41-Osq1iItXOHxvHIFkDjCdYkxoD7Mi1fsq3SWAqLPDvhI8jZ0BLWSKIEgvAAPeGCiSszF4PFkYJzASA0IGzJanTUHw5YDQiqZZ6ES8ft4jYq7N-jIpcjBMsU2FUraZg-qMDjW0a_q-S7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku1_e810P_6NQUyONti0lphKOpFJ8liJwMqIVlqRR9niJzKOUHp6ld0EV_BO4tUPOJB0M5Hnd1aeB0djFcHrvY7IcZC6jNjBbGyCu0Lf19Lk-7j1-q2qTVcFW8TdP0FtbfGKa1ZHAc2Yb0boj1JkzRhQa0mzl8pnjnyPp1HMsPNxrrBXiOdHuYX4qEvDfakdLFyIhhGTce2O9kKFzROFYDwRM6BHBele7DGNHRgBJjioTb_xdzssO91CUMHtDXGQMUi1O-ugyotAeSkV9ZsjZAM6ChvX9AO_gZrPls3ZpZ6HVa1OAxqVYQFCdzpxrS5RViSd1WeLh4FzCg9yEUTOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MelulPAsgWqJqwUUXERbE9cR8m7VQGkoPtXezDjUipSStk5GrI3BYhochD_0CPT0G4p56AKFy1IvDrP6GU-EP4US4VA97KBzuTvfdsbH81GTy8G017HrnX9CKosnCYrbNqoYvHI1hMUOccZGiZrwcFMO4KALzjUvX3XOT7Hug59OshnjjKuMNqwZ2nRFku0dB02uX-J5ioePBuCavJ_NyCG8Eh1LA5rGw6hlTKRvRkzfg6UAnnyyRH4QjL9_T6IdZMk4HEuEOZZHw0372RLjKkohOnbmTtNRQd6ySONLeeaOCY_7WRsr5DGARhfQ7xQMkOZzG356_8ajDeReoGmFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owfctA8AjOsqGKqerri37etBkQKps9gusYDoY4jANY6KXnOXbybSJqDFmLoSekUZj4yvMk3N7t4qgEMx7PqAsYkylcgtvOURJMZi8kTLl-vwIc2EsrQSTE2YR-PfTPb08vQU2K9IauCX1eIwo2cXN1H2o64CDT2E2YZPNA6srnrcm8jLYFnLBMX_MYu-G_21v5d8mroVJByG63zPqoD7vEmx2-VyRtyNvwjPeRlO4nDs4dDvhGV7bsVDtrX9vR0EzEvcG08FVlHQ1tOGrwOt_jLxG1djWIdplvjcySojFo9Ic8et-TfTNn9l5F0-7Vf1fc_ZjrJ7IQCPmhSJ7mzMvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvJg2Kq1waa9ksjCceAN6h4gOPMh3vzaMekArVOJZZulWl9cXE2B9tlPhqs4b0vcZYYcK5H4r749eTq33VJgy-ZkKayxqISGGrUBfPiIfMukNJ5P6mohA2NwfA0125TVVjtGmwxURfB-GWH00WjipB0CvzuXyC3lyzRq40lLCKba6rHyTuUOLufmKyvJNH3WxQGaTr0KBjYBRUN9JQwH3w5Rgu-fglzfzkQytdHhONgGg8Pd4tIqa3CJpm_4Y5JpQa7gMTjbjTnTL3tYYq8hpfNhNuV_YJXbZUpp5mK20qiSGUEuWVnswRgfySiLgm5hNMohDoI7VPxTTKd-b4WG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=ixanZKtbuv5LU_VWUHPCnyHCNTTPZdgRP-tPfbfhIu8f1phuXr9Jr2b9pwP78kC5FT7Ei-u6Qf1VqidJAvkE_oYPeG3sDURR9iUCUCmLoqjypuNK4u3HYWYXxtujbuO0L6xdpICDSTM_HhzscjhNMvT_Pgp9k7-5MFpedxEBYPWBTHPn_TBHkWTnt2XXB28lQ8yz2GXiD51p4K0FLgK09_kH2z71t4YadfsSezWI2Gs-fxN1Nh8FvzK-C5ZkZLjLKL7M7Yz6SD_p7bDzed3TKCeW2BPIaiLyQyJtVzeQztukSuf361RpmBQJg7AtYFnVcOa65FFSyt70Ub0DjqQy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=ixanZKtbuv5LU_VWUHPCnyHCNTTPZdgRP-tPfbfhIu8f1phuXr9Jr2b9pwP78kC5FT7Ei-u6Qf1VqidJAvkE_oYPeG3sDURR9iUCUCmLoqjypuNK4u3HYWYXxtujbuO0L6xdpICDSTM_HhzscjhNMvT_Pgp9k7-5MFpedxEBYPWBTHPn_TBHkWTnt2XXB28lQ8yz2GXiD51p4K0FLgK09_kH2z71t4YadfsSezWI2Gs-fxN1Nh8FvzK-C5ZkZLjLKL7M7Yz6SD_p7bDzed3TKCeW2BPIaiLyQyJtVzeQztukSuf361RpmBQJg7AtYFnVcOa65FFSyt70Ub0DjqQy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtubNBWBUU7JIFj0j1tSkIiWOAvtUFoOidt9IkOixR3M5dWTHDW8l5rJvzRc2aVSo9F3xBT-SDM77TCFqMJ-IWQFAo6-bTC6xIrmjp5yLvDadR7OLeHB4ZaIe5Nyzom-ArjG5yGre3pZ-6xggxmt4YsM9GabaxXEoyQk4RrKLlYnUG9_qAeHA4lA9KDlXpxOqPj8vMRs-7nsVPLH_DTvAedVyXq8j0zE70ZZNGNDY_PjjP9yd6dmnm-5bsu0lDaCAwpLtHnN8-vdPyLJfDLzwWI5wj70Mjxyg84Iko_pSHE3ci7x5kJRm3Oh0gc9G_-Zr-bKamxsFsVED4oD8L963Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjaOnwVWH3VOR_6dpg_c1I96bXm7uatdTKGPLFGyo54Aj0ThnOsFSU6kOaE6SP2FCc6I2euI_B8Q-9GLbk3Uac18GBfWGq6YS1gLkyC9uX19agsWRKLJ_8Wt5bVpkXVX34PVOqUbQbSmPtGUwr1qm7ur1FYi6zo8KcSEY31yh_-Wzlap5k_CVYEtlWoBL7rdrtPjVOTZqTUL0S-bz2TPAZGHDVYNU-S2dfvzpYeebQkyzm_0ymy6B6j1oBZrruycT5O3HSgwMUd17Rq1Hw0_0-uAkFCckw_j5XlqAHocMV2V6lROyu6Tr0xmb0yu8Dbig5xJgZavhlKlzMsgxU9Riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv7s-8dsp_HcN01owq8m0V-yqopgaNeLR3YV0bH221_k-qxpL6EGUcL13apoILcgKyeffRcS1vHdlqfciVJT-mlwaa_HT6fR8uY77gAvjUQhOP1332v98SEJT7QpPuzsuYKFPapyZYKbhXH5z3LSILaE-NIg_x7xEGUOYGDWOkq3hBddfm5rbJWH0X_2Sd8WrjfZew5e7Ee8RDiVXETI1nKadg_CQne0y_n3GMS9U2pRn3Io-dyQUUgbZApBouzt9e4iS0DyNWDJeGJvutDwZg2-CEsVr6G5Cty2uWTAYj6rFHPBY6JRJAjSNdXho6hsRokJZK3PLriNfTz6GUr7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=WseOX7w--SFg6znc0smKBVGMJZ8HA8XUpCA_QevpZ9slY9gLXjDjh4ZYN9fWsKyJ92kMZv96iuQ9OHXK4l-JzN5uUGq3mzOWucnsgTJ9QC-l13CxJimCYBOgIKmKJH1e6LEFEhvOXdlNz9MXAMlSW3imap8TSUzkEUtrfczHz-BBEhpmGD3m_V1bVD_2Ib0fqt60xEillLoH2iDUfz60VaI21jJs0DYsTIFGALmct1JE72pzSLeN8bCLgWLu4skZHkH4yzdH2S0aIFjyoOeaP7XrXjM-qvTv_VlJ-cotEOSnLs_sP-E6JlMtLcak3s_YBAcvy94VX5w4WKveS5MWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=WseOX7w--SFg6znc0smKBVGMJZ8HA8XUpCA_QevpZ9slY9gLXjDjh4ZYN9fWsKyJ92kMZv96iuQ9OHXK4l-JzN5uUGq3mzOWucnsgTJ9QC-l13CxJimCYBOgIKmKJH1e6LEFEhvOXdlNz9MXAMlSW3imap8TSUzkEUtrfczHz-BBEhpmGD3m_V1bVD_2Ib0fqt60xEillLoH2iDUfz60VaI21jJs0DYsTIFGALmct1JE72pzSLeN8bCLgWLu4skZHkH4yzdH2S0aIFjyoOeaP7XrXjM-qvTv_VlJ-cotEOSnLs_sP-E6JlMtLcak3s_YBAcvy94VX5w4WKveS5MWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk1RCiXaOfUe8ga6xZwYFgAyjEKgt9fiG8sycv_jBYtjibpiHMktKCWxDGS8PxwfKEj0KWO-3QTGVlo3EaIUxyUGF9Wbg_-NSFCXCcBlqkV65CCieZJy1Ygv6ooopZFjHgNk-MeTnOdU6MvvJpTu1BdrKLS-9pEhJmOvJ-MXNx7yKnAqgIRJmbkDOm03L_agav3qb5yScF9YHKRJVvMsb0jdxNrl5P5RDoc9KP2V8zJsjLGX_vYiLvJs7EkAnMOiEQ4x-8aYgp0COCGBrsp9XTsd0LMRzQB2DaqKHuwfXYC1nkm9GlqUTFXjyihxWpQ3MZXC0yjOaSkZlQh2Idxc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnW7sdROC-sB0dVBZs_PPq7YoVcZ5Mtlnuba1qSoEbU1RX7FadeV72FYgG8p0OR-PP210iJDAPxHBerOXgxAGRz6f1gUmDdRpgrUeYsipf5DTRz2mJd11Lex6Q74ykJDlyUc1BMvFKI45yWON5kTQoyTfryVe5x2gH0xhiVa-yfV5lvjNxd4T79WSiPkwjQFwZPXbCwRUOslJ0swZa27wIynl-_U4tmJJJd8qJ-b2UyL2CG-Gx_wn91HGA2KYrVsLtIyFhTCq2cw0Mdohn7IodjKLoZzN91cef0pp_5-qzMQcUFzE8wPYhOGcikiNnfCSzOOvd1Jb_K1QGH3Kv8BqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK5HxvzEy55cg8C8Tvmj5yyyc-uezIbJVf5WjjmLl5kMqSL8Zil6J18LO61SWLs2DiZTjbKjYttC92zBiZ8Sm787VnMQBMoGhKKp0c_pnXD3zO4kutPg5B-iVq3te02VGfZ6mq1GQMZIFYiZXOggHRTATlQZxB_JfgD6cWKl8tPOuHjpvNoyYF5-rYQZoClUc4KGCmD2DICIjAet_eCT_uOhh7gOTWT9qc4D4ROjfkc56Q9dF3TrymPpHRHgvKktLi2NRoQj7bcI5iLUmyIzna_51YG9bURFNKOMjHKMDfMaYIiMGvRFiIahGu_Lv9TXHZZqtF3YzR9kBWLIMmiGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxwciwoV-fT5E9sHVOtOg7ODy2l146NIO42bfwyUeayLb7d0f6coD05Fr90csFOCdU5yPvb5ImEiEOpuoaR64B7gyBvoNOJi_VM4FEpKfrim7vdrlrlt2lX1vaGxGt3PT7b1mKWZcymiJlLUXJb9ZaDU25No1wuX9ms1u5l6QTVPvty4kq_rPZ2Ey0VoxSnk8aZCrsvwDiClQHFxhk_A70-t-Y1mmQGtav379AyIkMd9PiT6MqV0bsOkKr1GtTMM4CiK7dN72ezJqZxf3mru9hl7iW5y4WXXGvejfFgxA8wOPS0ynZsf52E1Yzbv0dw7bou9pEcPop-hdarkZ7ML0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zlfpo-Jqewyp2p9vRDYvDTGFfDjPQS-tVdPg40e4W9ATvbVEQO4n3gnYL2GPSAx_YQMP3yVoweYGJV3Mfu1K7KMZVmmWJtG6-WUSVLNAp240fnno0ysI03OM74zdjpaLyc-CyWC4WowCXTCu8JtTOissMmLpD_TDXGUy5uLsx0NqoQ2iwqBWTSUcqJ2kwM3PWuWfRMh7gVRalfa8zyTfGT0o06Dl7IjEIkmr9XE8Th7UQVr1kYm4K6mEXUMUnBHN9Kme9-tNWZnZugRYN-1BQz187-1cVN4vqzGbHEIaXiWFQYTheaszvQWpjIZvdEbk2ZGq4nPZfPfEEQLWRmpEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 27
سه شنبه 15 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHj5BZN_SuRiu3guwFO-q4ltuRNRJJDH8CN0Z0nBWjQef-qPf-l5mTAdQOdGlnNtn1-Owivc-9Qkry6l5LroB1d90O1A41fdXMKn7UnBIzplJmzDjxZs8x10lwjWn6ELkVgVNtOGLe_tbTL5-u3hC9GZ-itEL8qlizJch-SLXyz-KMa6In-DDQ7XFT5NqQb3G70AoptrMNsTQvjoqh0L-YxzFHzUFEwOuhNDlM-c8zOVwqEcvq07dtNOp97pkbIM1b-OToVWCJmVBS1Qtu3ZDr2kB5qBdZOri3uVs_Zvvr9b0JBZrNUW32i__HWVJup-fUJsIkuMANcBt-8QiZ0pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m41hjnDgITW7ho1WelXVfuPRnN9DnLY71sLlPzLRGg1Bu8oH0SXYB6qZf0go70x50MKErMGo6NgfO8E_lNuptWxZGQ-sCFrXsBbj4f_EimXlZOnKVF_u-d2LWqAX45kmLUJpoywvB8Bt7xkthUuZ6Q0JM-a1dW4Xy6dhgxmrtIGQPx5ZkcyDrtw0TAlIwItS73Zb7Iz4sO6XCS6wq4PfxJVRMmTjU0FfsVZA14vp3pmA1r9imo1yMsvCzr6pj7m1cdx8ICxfFJBXasZa9ZILHsHhnROtx-XvSw4E7GccEpQvDv2zEgD2GNTt6VBWDCviqov_LGDcmi78xfXF0p8dkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZMOJn1iiBByGK1rvzUFAyjNOij_c52CfXPkxpg4OHlFQjKUZ2tLgL5VKxBxgi3YDHzqKQytskCIGqnV2ShzVjZ_X5ft2nqPxNSoeLOQW3A5OMeWutZ5w1PaGiQjW-C9xP4d9kMMQqLf1euJVwP1JqdLNVqDS_edGyITtPQk2ltFgImG-Jw3vYrBj1zw_6dY4KGh3VEwKPU1DFlCmDtdUCh1HwjBu2_B6QwdwzSCrtDsm5iinT-c2SEpsqwADD2-zKXOKR-wboPN_pgcqHyQwERkL1vDtGp1aQwycnKMCIywfdc6gzsthMuEjI3x9uDNvSakCRKxXbQziHRWoFn2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiP47nhnUse-wSqx81qPAzmRUfWC_nZwzGm0LO-Sx1OktsH_Zr-0w5jbFO-MaKb_yXnUI2BuvSMrhjti8ruAX1PW36EPW14jVw4P-MFsxws28iGIS9Gd70HmEhIHczjkWkZh45ArULH6l7bDO0SvBuGl5cOMRQBkuUCPz3QTQ80syojzTTCUGNhiUaai8BqMhfrhCyxiY-0NnOeEKDnxlbDLkn_AE1MAgrerC2r48fS5CPgiJHPyjNfQG3nTpGVpA_Bsb8Km1cNHf-j7oPP_e9n3Gff20tNHKBHkMG9cMT3BBaeg_r1_dt9omkkVL-GSt0DNk_UpFaJagD7D2WDqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cugH0lnngHsSDFCfU177iA1l62dwyXdsyRgC2wPl43hDF6sOyqnBmt8a0HBDMo9hqGhsyNtcS1cmWeYoy5JhTsSoiDCWpLlvm-kT8ozzxQY1416a2fLFVNd4Wp_tOBcJ0_uYfc7prx2iuFbolboPxOl0RCsc6BU2UA6jO_BYFLDwqHbefOoVG9HsopfLOJAx7Xk4MTKCpsa4Gk5TmWqgoMo_85SKoqxKRWA98WNu7h0rDS_9wrH3NddBnN7zS9-9rPEw8Pd1QK3oDM6tEUuE2cUATeIyBndrQkFz1nHAeWR6z8AdzGcCmm1BqIYQlKIj-TsOt_Rid4bE4WxsRMg5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjc9aXCoZFCwJIuaa88GT86mE4eOXL6SNADgn9ebqVf2mtjW2vOzDcTTAYqR4828x4oFV4yHclC6QXIws_SAxwbu28wWTBCk6xMuh22oVLBCsd21gWA9OFkD0rqzIsOFeAXHGpRLfOUbsxnHO_hTVIswJBxsLaSPTm23oUZK2L8FvdMEFK18ekS_V_IW2RGvmCr8bekdN2ng658BwcaSnHiwuSLqs880vMxD12BPQohwGgXiOs1G79wP6gl1XzrsVtyPIQuaeLgrtiGjH0aIlLX89iltTV6vUQueUc4AKdjLrTFp5H-tilmfyKNZFMU0kiN80639JyFrtram4K7HNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDpKqAwxAO11TJXr6-MBkggQZzuf0v5CKZ9GHJ6nE_xK2z8qmh1EkWAEDBae6INz_3KP8nl1nBRNCHNyktbTyUisjxLlmqIP8ygJ-hn2UWhMlHdyOA2MN9xKtfVXAWMUnnbjNsrU4dLxUWJeXuSqrjhHnOcLiSP2TmDD2_jRkr7XdqmhGMYUQbCFuRRcMujI4eyXS5EFwbBDPVXiUKZlC5twlcnU8huJDnxaCIvcClG9I4DzaMH5R3jh-N-olta0JZjAh2U8wO2rr1geBCP2maysU-B40hrdSReYVpmsygAe-sQqcIsu8E3mNLX6PCs8PHBL7ANvdk2ue5p3pQvWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDi6Jv9Fx3fr5XiRPwQrL-x0cdSkxosVLC5Bh5GBVUKVepZo4xjA0AFhUqs1CkDMeIo-tYdoKvECjUBkZyolg_qpJfwooXiviQo4ycj1n65I2b6ghvFNDbgS7t59_-TWD2Jl_bMdsyBcw8x7oNnyLd80rnukEgbi9RogsQne60aX1-z6WkUAFA9nO1yIpUxJOOUGT0NsgvUpfW1Lux1SEGucivG3RxoUR_yiorwLWjrdSiOoIoN8Sohoc0GuWKrUkAUzAnDbroY8JV5y6BYxmJ7AKW7QwmiYo5i4QyI8Tq83IBvD7RGS5lra9J-e_-QYMak9yAX7RkMolbua7wDSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI1CRA8bmPLOrPK2OFrlgKmlRU6HIUQOwInLNxVj5yFgRkc4LdQwcMlFWnzHxpE-AmUXFhUY7wfxkE5rOpMhFLkGrp_RKQHKyf5fiMVrSVlHujm90WBXxiYbzvlrfgA-PejgtjfnjCU51MNki7OmxXzoO5egakhr-QjfUTb5Z4iXPt9DPP84kGXm02D8-PWi3IiCCkBMPKx33w_wSDaSU5Q-N2JmUJ1mP6A6xPcZtLTpd427AB8MUWmW21WW-hP6nEP3mfUzN1qAmHuG6-J7BLmFK5bQOsm7XP-31q8cWvGhRbe-dcVsUWPbheVl38uoqAIQ7uIRUExmuS--h6Y4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw7lztL5l78pJAbWBrBmYpDXyEdcW2R3PHutGKQ9HXsR98EHvlXHI7v6hIzbgZNYEIbLnVD3RuJjc1ZseC9LLebrxhyiFIY6c5XKwFc3BA5-nmPaLkfax4PCGUDHXckbijgfMOp9ty5abcZQmHhTHzI6e8wTTR58VbHyTsqqBs4Uu_zWaJBgWlo9cqkYS91n6isGkPxQC-zJ8jFlmnXqn6-bvBjTmeZ-f98cx73ZxYU2w4fVRiDoKjYO-FlL4ARSDhyVkDXRWHJYkHTwZXGQrgpcQP4DhForBfZ9VwipdtJ38gEshGsYSI4jhrWK4ZfXU4JuyBCd1jw8PwC1yMZidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN0g2rHcAF-N9f5BdMci-kQm8qkOQUS9a2ThCMkt6qS2tEe4sjcZiQyBOr3jWosm2vhROJRXEfpCV5ifB8RIIBV8t1VVJ9bfUC7IB2w4s_CLFsPsNdBeAkRmSoJh1z5xJnPief8OuWEb0nFv-KgNPsVDu8MwCTBzmYvWe4wUEyvar2WHR14GHtgsgDomkV880G_ZjkLUzd5s3DGWTSk2iHcj8L9Z4_OUTmWnE1sENZBpnzxkqBn84wCDQXXe3EDXinufeawVH2fX6P9OKsSLdm-A4Y8PqVRmnb1DS4IU0KxQ_QJGRnK-j92CHsUUEO8DiQ624l5BG3kpguaIEGRvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiyaqI4I1FYhiNd-2foQl1EKCteCINESytx7Ko1k__FMMchI_iIdRqFHyRdADWz8JljIDMX2H8Rbaw3bSp9Yc9xuEz8jqPhxoxDKyUnaUxlRIEk64r-wIsoQr2fetAxCrGBb0CiWsi6dK-Dhjtu7ARaJW-KwYXLcVXrWX_wMJLgWPeNg7mPpCnJCp4s4ipBn-jU8p0KSh-sHmiXZBwx_k9xyjaHWTUrHaN8hnUX7ULACUkL5s5RIn4aA-r3vDzF3Xr6bgttWGz1eKA_ycyYtQJxwR8gV4Z2zj77bgUKtBtKm5jZhFsZyVYR-Fk9ydV00OAIfksm254dgpJQwBmCE5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
