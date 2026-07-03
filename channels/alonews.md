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
<img src="https://cdn4.telesco.pe/file/J5wUx1ecuigg8FHemIEK4JBpFcDnOGFT1VXwFPSLUZ9_rPlcWhO_KfWxZPvS9GXGuyP6pmJQQHRiccnzfyCYKiAPIVfyNWV7p0I8tNO7UB7zQVgaOE8FpBKoCCEIC9wLdgAva5I_zco1z0-k1lz2_tYTr8r1dYGUtnS2nbyKxbYAz-7zgsVIYHx1cMInLbQLEYiMXc_vWypdJMm77pbyMfFMf1sGc0nJedyiRwCifykBPrJGAE5AzyqPBbigQSyjmyRjpBWefuznKuxVam194w-Ye9HOMGIsXFDmggUm4UmaRJKHtza6qTnP5MGwjh0XDI679OJK6EKsRamdv9xSjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otCSifEwsjuqiMW-JRmuf9hT4mqw2yTaSC9jtvcXNrip2a8ExsmGSq7-zOSXwDfGtreranWNvAaiF6RqwGXi-NeVa3NfAcB1fOLnNDZrj0wxUf2KZyCXVTvDiCHE1yYSg_-M7ALkrZcCa2uaRAkNp4QxUsQBaMemPJ25KwaCCl534eaOUhk7FCR9EBO2WsZNt6PZvSmTHk70PERWDLEWJA7ha4zuh_UmLJ9c5y_vFJUCGQjsmD3eSoNol1CF2ETcxDORvLapTmreCn4dus3ql4h3UgnQ40xiUBr-z6UDNZd9IRhUnjPCz3ZrOyLSni9SWdZydq22IEYXluwPOpDckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلش ریپورت: پنج فروند هواپیمای بوئینگ 777 که قبلاً متعلق به شرکت هواپیمایی سعودی بودند، علی‌رغم تحریم‌ها، به شرکت ماهان ایر ایران تحویل داده شدند.
🔴
دو فروند از این هواپیماها در فرودگاه مهرآباد تهران دیده شده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/131612" target="_blank">📅 15:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt01xbCZu8S-iBTAlHwydQPlU6GdvB5J6Jy19gjQSQpH1_gb8kXJMgfFhbCt5_y15FqGg8_YpLB5LrTxGMe0kzcxfNbOQyuO0naC-4efBobLV9l1hNx0NxyW_RLJMVGDt9VC6wZ4PQ3oYuzEDZVoAOazmGlHqat9_GOcB-Y0slUy6c0cpmTP7RFkY_J5g0-Uuk7ztj5Zw1Uzmfx5CcqY1hmr6_H3zRWC7l65hAJz5m0wgXd7VSbAgMTdGLO6E8DFR8XXg8oyDjB6y1vw0t7Sq1EWmhxbWQxHIORQqNEekbbfar44EuA5DfkXV-aX_6V2u8hEpRHdjU-JZZaMcixDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش آشنا به نبویان: راست می‌گویی در حدی نیستی که از بالا تذکر بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131611" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=fjitt_znSnDNve09W7Bsqq8hc5v7HEHyf1N6fhCPXqbw2nCZSBdBVX6hHymTOBjYg9aDv04kCinq9UErxY-x3TYeZpfzQorVeyBwmDA-70S9M9O1GtExb7ZqBr7fBBQFS6deIMExUfBABEINfUyCGISI1O8bAEcoTuXGkgbOUi8nMQk--pMwjlgLhumsQQB1M47GSDswm-ZgvA8UJXe7mEyF7hi6T_3miUperIHvZHQIkgABgCkTIcqYn3nrxe2dkFvXdLLt4WytxlBcWgoR-l0ISXQmCXevmtkK6D9qVLzCv5uf7jJIJIvumJYpOdriSFTnUh5OHrydBXMOtQnh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4987a0d8.mp4?token=fjitt_znSnDNve09W7Bsqq8hc5v7HEHyf1N6fhCPXqbw2nCZSBdBVX6hHymTOBjYg9aDv04kCinq9UErxY-x3TYeZpfzQorVeyBwmDA-70S9M9O1GtExb7ZqBr7fBBQFS6deIMExUfBABEINfUyCGISI1O8bAEcoTuXGkgbOUi8nMQk--pMwjlgLhumsQQB1M47GSDswm-ZgvA8UJXe7mEyF7hi6T_3miUperIHvZHQIkgABgCkTIcqYn3nrxe2dkFvXdLLt4WytxlBcWgoR-l0ISXQmCXevmtkK6D9qVLzCv5uf7jJIJIvumJYpOdriSFTnUh5OHrydBXMOtQnh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عده ای از مردم هند در راه ایران برای شرکت در مراسم خاکسپاری سید علی خامنه ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/131610" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac7N7Bd7LH-HjwT373e1--HxBs0JoYoQScj7NenRinjwfl417ZBQ3qwJfly0gBr1LkOW7Q7GUoh9egNux5f9LN2-jxJOzxKNT1kAQRirJjS61yuTPTo2Z6pTrXUCmeDk3iQgf9k8G7Ck-Nzl4JHyv99NOa5Ivc-H61tMG3U2cOHP1iAGEqlYTTqL995eyOlRY8OsrLdGCEqFNTy5SRXRIkkmmRDc33sTjMeEkS9VVCoLluCokzgcrU289rWo-RLywO37RvzHuQvHhVf98Fs_o2LfqOzEQxZDAVZCky5u5eQiLbmuCcWbw9_KGt5YH9DPgPhkq9I-1IE9OpRe_VtX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهره خوشحال پزشکیان در استقبال از مقامات کشورها با انتقاد حامیان حکومت روبرو شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/131609" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
احتمال گسترش بیماری‌های عفونی و آلودگی آب‌های زیرسطحی با برپایی تعداد زیادی توالت در سراسر تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/131608" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: اگر حین مذاکره تخلفی و نقضی را از آمریکایی‌ها و افراد مذاکره کننده در طرف مقابل‌مان ببینیم، در میدان به آنها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/131607" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
واشنگتن پست: اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
🔴
واشنگتن پست مدعی شد: مقام‌های آمریکایی اخیرا فاش کرده‌اند، واشنگتن طرح‌های از پیش‌تدوین‌شده اسرائیل برای ترور عباس عراقچی، وزیر خارجه ایران، و محمدباقر قالیباف، رئیس مجلس، را خنثی کرده است.
🔴
این اطلاعات همچنین اختلافات و شکاف آشکار واشنگتن و تل‌آویو درباره اهداف جنگ علیه ایران را برجسته ساخته و نشان داد که اسرائیل به دنبال سرنگونی نظام ایران و براندازی آن بوده است.
🔴
طبق گفته مقام‌های آمریکایی مطلع به روزنامه «واشنگتن پست» دولت آمریکا خیلی زود به این جمع‌بندی رسید که این هدف از طریق جنگ، قابل تحقق نیست و بنابراین تمرکز خود را بر هدف قرار دادن توانمندی‌های نظامی ایران و ناوگان دریایی این کشور گذاشت.
🔴
نقطه عطف، ترور لاریجانی بود؛ در حالی که واشنگتن به دنبال فردی در ایران بود که بتوان با او وارد تعامل شد و ناگهان چنین فردی دیگر وجود نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131606" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / آغاز درگیری ها در یمن!
🔴
گزارش ها از پرواز جت های جنگی عربستان بر فراز آسمان صنعا، پایتخت حوثی ها و بمباران مواضع حوثی ها در نقاطی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131605" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تحلیلگر عرب در حوزه ایران و پژوهشگر ارشد مرکز مطالعات الجزیره: آماده‌سازی‌ها برای آغاز نشست‌های سطح بالا میان ایران و تعدادی از کشور‌های شورای همکاری خلیج فارس و عراق
🔴
این نشست‌ها طی چند هفته آینده آغاز خواهد شد
🔴
هدف از این نشست‌ها ایجاد سازوکار‌های امنیتی و نظامی است که منافع مشترک را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131604" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خروج بیشتر نیروهای آمریکا از عملیات ضد داعش در نیجریه
🔴
به گزارش جروزالم‌پست، فرمانده فرماندهی آمریکا در آفریقا اعلام کرد که واشنگتن بیشتر نیروهای مستقرشده برای عملیات اخیر علیه داعش در نیجریه را خارج کرده و اکنون به درخواست ابوجا، پشتیبانی اطلاعاتی ارائه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131603" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131601">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEfchmfzdsw7HsM_w0SJ_LnLvQWHs4IRae9mPIzsohfyiqgsYTzgnoFsSe0rhXFYRIaJVZT7nDR11zcTzIo8sbwGW4IRBabsEyAMXVHgBsJLOy4uwcT6fXZUxh7r2NDk0JP4SMVmdaBPgUoqe5SrU4e5h-bS-v2igPkRaVhOjDZWFz_LTsNeqeCtwk8OfxrzUyNVwYr56Z91cp-4piDlTvaAqyHZGmOUEQEwHbiYgwbuhQz_bOGaz2ezgkZwJNt0nwurKeMhtUseBTK5LKbfaYXw0rtjeGf6IzMRULaeadNKzrBvWbCxepr_U_qGa7zRKp_I_1l_-OMS3L39ho0bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0pxGFr55rRlzjIs_RwBWphvZboXDJC4ovhBEBlgf9KYC8Ch8kSd3_j2vyj6mi28mdebunTTAgZn08p7tkdv6Hx0RyaAT4VfwZaaip_3vbiyO4JQ5zKLc8_mTHKHgqjmpj4CYjRSnU0pAs2VVApnKzS4r7hOoRhkfgJj4D_U2St7d57Ql3jF4MHcTDkOkIc5y5fo8OpZPv5dEC3lhyjQDq6zjA_41GU6n-kJrXqJOQkc5280xOdxfaAebj7QpDeAcRJku2UAfPV6OJSWvL4kBhGADgnqr-Z4UE3nHo-HwUAz7tDRRSsW3lIMwvLkUjO5OIvBVeut61dlfDtQ6tc_ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجله اکونومیست حدود یک سال قبل یک تصویر داد بیرون که اتفاقات آینده رو پیش بینی کرده و دونه دونه داره پیش میاد
نکته اینه مجسمه دست خامنه‌ای هم تو مجله اومده بود
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131601" target="_blank">📅 14:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/131599" target="_blank">📅 14:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
صدا و سیما: تا کنون نمایندگانی از بیش از 100 کشور وارد تهران شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/131598" target="_blank">📅 14:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=ln2lCW2GcP0wfTk2lUKVMZAH7AMecwRINezO6aG0pX9sdpVR2T8zhj7cN3qFjSvhBbkI-ZSNckl13lTkKIQGcVtoYipZM_Ubbc9nCdkaGwzVeY1lNc74UkQzKLk3a-44WGSokAbROs4KTMJIEOml6TAUlM074XGkwgUXOonjTUpLhCw00zJCM4i0B7T-4pCYpwRn9hv0XZhx2NZvAjlpTLSBebxkqslg5kKgicuMoBqOPSbpKsa45GBavXbbiG1j14FhzjQT_I-kqrz4iXCf2lbp3qXt9Zo950f3SVN-PyRvp_thrRAbSKZYfz9khAGA1i2HEhEeJdZSIo-EBpt9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23cf75c5.mp4?token=ln2lCW2GcP0wfTk2lUKVMZAH7AMecwRINezO6aG0pX9sdpVR2T8zhj7cN3qFjSvhBbkI-ZSNckl13lTkKIQGcVtoYipZM_Ubbc9nCdkaGwzVeY1lNc74UkQzKLk3a-44WGSokAbROs4KTMJIEOml6TAUlM074XGkwgUXOonjTUpLhCw00zJCM4i0B7T-4pCYpwRn9hv0XZhx2NZvAjlpTLSBebxkqslg5kKgicuMoBqOPSbpKsa45GBavXbbiG1j14FhzjQT_I-kqrz4iXCf2lbp3qXt9Zo950f3SVN-PyRvp_thrRAbSKZYfz9khAGA1i2HEhEeJdZSIo-EBpt9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه پزشکیان، قالیباف و محسن رضایی در مراسم تشییع جنازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/131597" target="_blank">📅 14:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343711e162.mp4?token=BMyl19lS3ZfnmzfnPBFmZwIPy-f5y5vd102n9PpOUjfOOluynVl9TVfkY17YkNYvSk07korMimXMq2ZWkMYeAa5cs37CL2ngVc0MBEAvvIImnqP_p-Q3Ml_vcHqy_YTHStCmHiAuCOv66UikmSeY_327ttLkP4gd0Ico3A4yZ2UwgdtZw1SC69mi7Bx80-WPBt6_thqZ13123VujEOG5sOOtq-CzaHdkiL2EYheIFc7hAGIlMSCz_hbOJ3OIjQZACY8PF4pyh_PoYXDUmBVyXGwc0z5y1qRkOh2fokbkoLwnFU7IBzjl4RTyS4jjePp4jzDZSmkiii9iut7KoPOVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چندصد تن برنج
🔴
چندصد تن گوشت
🔴
چندصد تن مرغ
🔴
چندصد تن حبوبات
🔴
چندصد تن از همه چیز
👈
فقط برای یک مراسم خاکسپاری از پول بیت المال هزینه میشه
🔴
اونوقت به مردم میرسه میگن کمبود داریم و گرون شده و نخورید بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/131596" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی ۶.۲ ریشتر سواحل شرق اندونزی رو لرزوند - USGS
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/131595" target="_blank">📅 13:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=NCciB_DpxSEUP4vS3Nzm72PjNB7JkhNfzvi2yo07v5AYEwk3boI4VOdyjioEHsD5ZU-PQcZARk7_m0vXpuyh7NWIBjBb5JifHvZxhhuJvKh3KjPfOGIqdNNhkk4vFBAVg5tHe8V8BjpjeUOhOXyyK0K2zJbi34zkommYORdEmQi8uZcFsqlubPRucgJcjeXqHba5cEDFGIFVZYSgzP-yFl92OG1-ErWfLTS1Nu68CmIQmdT5hzOW8xeCg88svTV5PRyHyGCX859g0x3zS0HXr3sKoBc6dNoYwSKRonPRZABLfFGcJ7z__aKLUj6YQPd2BR6TeeGW7RHWB2Ov-kMU9QPqK4Dm1gn35oLqqWMetnTVJ7VwfYt3KA4Prwd6XX-iFmoKMJXlBRk2ie-6jHDmBiL2qiojjWRg_gIRX3ZdvoSBAP-P8Hm82p7itwySZRIBI7H9xHvx5dGvHZ2Er2mKCDmJG0JisN08jSKqbxBvs0fDx9kr5lRHLFGBcu5xIcq2EPWK3Wac-MXXcyNBPIq-1jhX6N75lPIdoWWdKufXlyrBdZLFPX7WeEOgN9swEuOUip9s_pGCAn7Kh85gBWilgZtZ4dpuNQCMUn_v0FyGzHXNI-V6K9cvZsMqXBh4rumbEhsN-dRGJ5kONVJrq7sg5BPI8xTTWn6idCxKskhYYyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a42929a30.mp4?token=NCciB_DpxSEUP4vS3Nzm72PjNB7JkhNfzvi2yo07v5AYEwk3boI4VOdyjioEHsD5ZU-PQcZARk7_m0vXpuyh7NWIBjBb5JifHvZxhhuJvKh3KjPfOGIqdNNhkk4vFBAVg5tHe8V8BjpjeUOhOXyyK0K2zJbi34zkommYORdEmQi8uZcFsqlubPRucgJcjeXqHba5cEDFGIFVZYSgzP-yFl92OG1-ErWfLTS1Nu68CmIQmdT5hzOW8xeCg88svTV5PRyHyGCX859g0x3zS0HXr3sKoBc6dNoYwSKRonPRZABLfFGcJ7z__aKLUj6YQPd2BR6TeeGW7RHWB2Ov-kMU9QPqK4Dm1gn35oLqqWMetnTVJ7VwfYt3KA4Prwd6XX-iFmoKMJXlBRk2ie-6jHDmBiL2qiojjWRg_gIRX3ZdvoSBAP-P8Hm82p7itwySZRIBI7H9xHvx5dGvHZ2Er2mKCDmJG0JisN08jSKqbxBvs0fDx9kr5lRHLFGBcu5xIcq2EPWK3Wac-MXXcyNBPIq-1jhX6N75lPIdoWWdKufXlyrBdZLFPX7WeEOgN9swEuOUip9s_pGCAn7Kh85gBWilgZtZ4dpuNQCMUn_v0FyGzHXNI-V6K9cvZsMqXBh4rumbEhsN-dRGJ5kONVJrq7sg5BPI8xTTWn6idCxKskhYYyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ۲۴ میلیارد دلار منابع بلوکه‌شده در قطر و چند کشور، به‌زودی به‌صورت نقد و تهاتر آزاد می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131594" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشکیان: ایران همواره خواهان روابطی مبتنی بر حسن همجواری، احترام متقابل و منافع مشترک با کشور‌های منطقه است
🔴
انتظار می‌رود هیچ کشوری اجازه ندهد قلمرو، امکانات یا ظرفیت‌هایش در اختیار متجاوزان برای اقدام علیه ملت و حاکمیت ایران قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/131593" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به گزارش جروزالم‌پست، محمدباقر قالیباف، رئیس مجلس ایران، در دیدار با مقامات چینی اعلام کرد که تهران و مسقط درباره تنظیم تردد در تنگه هرمز به توافق رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131592" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131591">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/131591" target="_blank">📅 13:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دلار هم اکنون 175,700 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/131590" target="_blank">📅 13:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=j0x-7-CCDa4kShstonCGI5l34ssb12j1VQywJkw64SVMHAffk37unpXzmpaA0liVlN_hBchqyQ1TBLk3tmj3-AG3KiHqRUR0PP-Kcn4McbbR8dsuF2jnSdxrcOh1QPUD2KYerzR3et9rKu-ESeRwGeZ9mhqnZtLQIgocuHbn7usJWtdFlQseJBZRVN1dE0OrfRYZN1SaVv9W0YRlfMdaUPRi8CIap0jWUDWKDOpdFhR7eGZc2a4HRlIemm8x2S5I--hQsoALW3BV_d3nE___gPQo4ZOT7E8GdPgRiw2fULwITXgQTOaP9-c1n2ODfdR9RYx4yoUDJ04lQvPQI2s-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d447837fc5.mp4?token=j0x-7-CCDa4kShstonCGI5l34ssb12j1VQywJkw64SVMHAffk37unpXzmpaA0liVlN_hBchqyQ1TBLk3tmj3-AG3KiHqRUR0PP-Kcn4McbbR8dsuF2jnSdxrcOh1QPUD2KYerzR3et9rKu-ESeRwGeZ9mhqnZtLQIgocuHbn7usJWtdFlQseJBZRVN1dE0OrfRYZN1SaVv9W0YRlfMdaUPRi8CIap0jWUDWKDOpdFhR7eGZc2a4HRlIemm8x2S5I--hQsoALW3BV_d3nE___gPQo4ZOT7E8GdPgRiw2fULwITXgQTOaP9-c1n2ODfdR9RYx4yoUDJ04lQvPQI2s-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده ارتش پاکستان با استقبال وزیر کشور و سرپرست وزارت دفاع وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/131589" target="_blank">📅 13:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
امارات : یه حمله سایبری به نهاد مالی‌مون رو خنثی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/131588" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=ib3kuZF7u5odnh210UXIQelfnSAHoWPGMmVFHnrGLZWwENKpUlaFdflyju3HWByNu0Xhh3PgFkCRVYmGUmNhM-11RQcmGcg6EJeUoaYfQkPrkAnILDoMe0XNOLWTh6wMmrytSZJQcug6szB7nNYOVjWMBssDkAH2tNYs6OdDGU-Y8_iB8dZjkkMHaeH2WVp_znN_zEO9W10Xr8MS0f2x_i6IqzlQ09eS0SJDb-eUS8FC2rdn3ajd0CGYDVj61gL72QINUqnBHrAB_nAzgn_kbM5sepXvgGl6A8QpBzmMG1Kz056HYm7S9vKfEbhfFM5yoJqb3SBosLJKHtvKObMx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
دیدار رئیس‌جمهور گرجستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131587" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحرونوت: انتظار می‌رود «اسرائیل» برای مدت طولانی در منطقهٔ امنیتی باقی بماند و این منطقه همچنان یک میدان نبرد فعال باشد؛ اما این بار با اجازه و موافقت دولت لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131585" target="_blank">📅 12:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شرکت آمازون سرانجام به تعداد ماهواره کافی برای راه‌اندازی سرویس اینترنت ماهواره‌ای خود موسوم به لئو(Leo) رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131584" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گروسی: درخواست دسترسی به تاسیاست هسته‌ای ایران را ارائه داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/131583" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
🔴
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131582" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBlioKFXI4dkqilQnKCf2zInwudWVo92Zr3LSGJLVdc_r13vnFlYyEw7XPRJVhYngEVV3wfBGCYurQiO6D3bN3qeKRpk8L9ZLZU6EjX2CXn_kg94GYn4hz7DlMaJPosPQmon5b8ZHrWXM9oV318JXajfeOH9mzomcv3NB4sV8nEjbA-t2estsA-lq-vbfZFXcb-Z_V8bic4nBd2bznwUrC71n--_vQM2bfrhhOxbMcDR_Rd0FdbM7rW8Z7WghBCFRT6uRhFTQDehWC8v3FI_HHFiTdkpE4Q9GlyFB0BLiI3xegpU3sOPKxBE_nxsTr88V1aiIP5OYm2vRjE_JIJ_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
15 سال پیش در چنین روزی؛ احمدی‌نژاد: به هر خانواده ۱۰۰۰ متر زمین می‌دهیم
🔴
مردم بروند ۱۰۰ مترش را خانه بسازند و در بقیه زمین فضای سبز درست کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131581" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=kNihjiINQy4oP4ibiNIRFdUWkBadHcPVBm7IwvK3SgOGvZ9TxCBaXIQn7pOZO0wJP-GWzU3_OrpRY6j9UptAzAQE8xlAio3p4HTfsAxuyklv-y_QKCwKmbrDevEtYm3CIKB68pDSp59j8borHTJ4rLS5QCEXnd-zEWtxcDMMesjZfDMZPNlcfO4X8xReh-5zT0WZKrzS6wKWJvEmrAPSrAvu7tI25OZuTMa-32LY1QGLa_PJBiD3MCnPZDmJJtIRoCpML_g7pN82Hbu3e4o2JyQ0YnxHmDn6gVkul-zEs0YRcXccN97GJRRP3uxu5DqnWpU4YgBudP1-joAWP851SjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ab2ff613.mp4?token=kNihjiINQy4oP4ibiNIRFdUWkBadHcPVBm7IwvK3SgOGvZ9TxCBaXIQn7pOZO0wJP-GWzU3_OrpRY6j9UptAzAQE8xlAio3p4HTfsAxuyklv-y_QKCwKmbrDevEtYm3CIKB68pDSp59j8borHTJ4rLS5QCEXnd-zEWtxcDMMesjZfDMZPNlcfO4X8xReh-5zT0WZKrzS6wKWJvEmrAPSrAvu7tI25OZuTMa-32LY1QGLa_PJBiD3MCnPZDmJJtIRoCpML_g7pN82Hbu3e4o2JyQ0YnxHmDn6gVkul-zEs0YRcXccN97GJRRP3uxu5DqnWpU4YgBudP1-joAWP851SjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور عراق با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131580" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قالیباف: آمریکا و اسرائیل به تعهدات خود عمل نکنند، اقدامات متناسب خود را از سر میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131579" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmpPTWpw2GpE6a_Sx174mkIpr3vMtwgMTNaPaht_CutQ2qROVau2sBVfy5k4LhyC-KIVjd6qnIxHtk1uSO_9mv4RgjvswrJncpJ_-NejmyChMyMoXUABIwl4JoTNBFSxdV7bKimmvfIUs8UGdImPkaW8DHT17rzvPy9LnE_yTMU8_Aq7QM_QERumztwiFm6tEo2TlwDPJmtCeHGYEGsoDQdoRUmQUm3dk9OY56KmHxXZmpqSM-1uZ6c9BFfuoOd1K5BZKg9Qbg_wXF4FdG70F0fAXzwcXRSnGY_cyvY06d3RyivAjPzOpQ0Drc55o91AgPfvErr0mSdzaO7YgDzOhRww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f39132db.mp4?token=vVPl7dowVH6y_CuYf3e8hHTAqBuYdMZaGZENNHS4Y0J6k32vr7vlkwjnrqx_JsKXY5Y-6kYd48l6uC2WM3sGZtDVnjZfwddT6GpslIM4dPGoRFlWnuX6IKsFDr-YFINbwt9n6elIdt3fdHu3SlBELaN8KuPZqt9GmzwmUhsVcazYnSckxO_VdFIjonYW63U8kpcH7F9fFvYvJiV9Z8gRguVnijsP6dQHrOzDEWj62RIaxufV-mUx0nLa-g7bUJd2xqd-_SpatI9VZgYqkfjI95Xc1AgOhgx_Pc89s7Pal0yrqXhpOqx9e3s7V5iuiZ6wLQtWGElSF24T53JXwmUdmpPTWpw2GpE6a_Sx174mkIpr3vMtwgMTNaPaht_CutQ2qROVau2sBVfy5k4LhyC-KIVjd6qnIxHtk1uSO_9mv4RgjvswrJncpJ_-NejmyChMyMoXUABIwl4JoTNBFSxdV7bKimmvfIUs8UGdImPkaW8DHT17rzvPy9LnE_yTMU8_Aq7QM_QERumztwiFm6tEo2TlwDPJmtCeHGYEGsoDQdoRUmQUm3dk9OY56KmHxXZmpqSM-1uZ6c9BFfuoOd1K5BZKg9Qbg_wXF4FdG70F0fAXzwcXRSnGY_cyvY06d3RyivAjPzOpQ0Drc55o91AgPfvErr0mSdzaO7YgDzOhRww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار رئیس‌جمهور تاجیکستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131578" target="_blank">📅 12:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رئیس مجلس عراق با قالیباف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131577" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbWnqaYBMVSKevkEG4HEH4gjYdIa738xvqZ4e0WV8Psm2pEWKQhHQwlg9IkS3lFMvkDdRD-x-Tz73Dp6E1DshCQ1-nxAJ9BNLeN5LBSd0t1DR8Wo7tr94n9PUgwCfCshWcyjcX-KVYSElU1UNGBxROAOX1CsrQwKImKbe8vRt3fSf_BmVKBg33Tm1h8B5LmUJ9kzF_nH74CX8XxPL8eG7Zu3Kua821v9dI0jF0yAXiaWuUGEln0syTRVNiXoqGR_AAWWBXvyZXSikNXqGIVkgCiMpn6GxL0T6aYUexrETh4hVtZAWU4OavtuQ_2I22s1woc0-pyT2OLicIOMOFNiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس حوزه انرژی: با روند فعلی تنگه هرمز، آمریکا به زودی عوارض می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131576" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رئیس سازمان هواپیمایی کشوری: فضای هوایی تهران دوشنبه به طور کامل بسته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131575" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیرجهاد کشاورزی: هیچ الزامی برای خرید کالاهای اساسی از آمریکا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131574" target="_blank">📅 11:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سپاه : «خطای محاسباتی دشمن با پاسخی کوبنده‌تر از همیشه مواجه خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131573" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojQGOnkElcQRbrmVWvcm3UAtV18XS644iKUD3Rf6XXt1bGB_rksC0nmxbHV_ljURS_1zWQRbYY6mN9abMP4AoZJWa9UA9qLdF1maI7JsLoIQIC8eUFsXH6Euilg5yRqVFIzXwouZrPlVm5l4N6wCtxH-b8jv3YMa6IksW7uJl0Qq3DnSAX_KyHEV-RlS8wKw0P1ORdYw9cKqW6K7BV-Cv4QHGY9wurl45jcRDFdDN-Tm0HRbbSRuNusgP8c0UbzAlkB3SgWM7-IuQlNB6AasAOG7RTlbJUbGLMweDjq1qogFQSF9xw24wIdsz9kahNJxm6eeYD93ctor8EWyEO5C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پل ارتباطی دو استان کرمانشاه و کردستان معروف به پل بین دو بهشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131572" target="_blank">📅 11:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی اتحادیه جایگاه‌داران سوخت: برای تسهیل سوخت‌گیری، تعداد کارت‌های سوخت جایگاه‌ها افزایش یافته است؛ هرچند اولویت همچنان استفاده از کارت سوخت شخصی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131571" target="_blank">📅 11:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYpLJZGsXqXMntRAv9ZUA9JB6ON2paRSvPCTG0Z9lCzSVmaaIL7rNNPUjmwhPAyrfZVHZ77XEyCkHNL8pqcg2-ZZQkJntkKr9EJS1OqnZTGCx3HpZgYXVz4g38JUTrlzvaekAzxGsGrbeSGfg0D28RuRJtgh_psQxphrzTRakPtVRSSkGyfPixWyE1e94_KP0YxSqwb9lTQi08xuWDShOYhMMMDj1beWm3KnbdUfvPClF9hYn_W5E92U79VHlrWjg5245TpzgQawcdLpsaIFnjxGyEFPxBgMJolCRmEk2zF9WJk2q1_HRpToWEUq7lcEIkrMNtWGP8Vr55Gz8A6DeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5EpYt5_wr0KPYOPygqVJGE_ZiPh54NaTogNKVa-MB2PA7lOl-sb8TacgWm4RQgi2pO_3XgV0IOVpP0z0B_9wc7NQffljnl7S2IK21jNuSJMnDw16LcnyqvoZqNkPkt4NFx2onvPAEAq0uKhAXx34ptov1ccS8-FXC3KLx1en3oxjaCyLl8bbuYurx_0TEWUhIlY0nnJSgPK2pUExlX5Htx4Gat4wvUlA2edPjqWdKWY2EVP87MIE8jm2BIU5vGHX8nQMVUvygXk8jEPeDgm6rvUnShorNvuMJbt5JVA8YMDLe0erByWU7MQy2XwnbKV7XsFTj9xK0yLXnGtlE3n9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBXgbNfTLxkr30l3JETk1i4kV-LCMF3PcMIhjzV0rjdikVvuXsvUzP02layrS3pN4vOH-JXIpdKS_FV9lsrCt59Pi52Xp6AsdfK-aO_pzhPXvvbArAEAOYGoXQSwFkSVofgbuaXJ679lav5vGr2UzBhUF7Ka3fjasFtcp8vXMqr_MwReorRz17Wb7zP47eoMvyM3LKeNx0HYbr1KyGUIteMtXr5kulcZadO1yRT30pMzJhPrjDb9yl7ioc6FObhPPJ-T4G98qNxec9pzihvSAPxRrvpS4RXfYi_v1md7oMSKOcZFi7mhLxNSuS9hGsSJ5R1YkNKWztorld5LcS41zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYREvYn7pHGosOtI0kCPvtG_qCM7_cxK1baMQUd-prqjDzjkYPLXbIiqgnWOqYp9wnVafsA0y5XjV6jfhbz4XBbzPZUbH8hT0rVLoV-kLIBGx_dgkcbo2GLONo-CSfCoCscXmgcVllS6S24vWO9sYSs4Ts9wgPj0h3e9VzJrUnF7VrKLIYzMtzJNDQs0dr7iQSMasWOwCvNfGs7OIm37HaIjm8O7yMEkjUdiPLAhXUbe2CJphooDihjj8qJxisekprsGRcW93fNr6T_JPD2y1ejC4NqtSrhvN1XtLC6c-e_yczUuLKZ8nd7RlUfiNMC91Dt3Ktwx_g2cp9XfOvd4hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار نخست وزیر ارمنستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131567" target="_blank">📅 11:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qd6HXuAZdsm7QqpfqimNBcDJhf-rKBKznphbGgipniBaBlumOkfU_CiJhEu7XUbP1oI2KWCL3IGOpJt8MdvQWUDb_2T69Nri4l8Fd9FG1OuQkNLtzxPrgqgO3xM23HyZRphkpm6VQdbgoyyxW7v8zQ5QPxC9MVajVkIKaMDhQ-kP1sSLFK7fjh8av7s-F40j7viEAazvon4FN6_yJt9RbZ7w8Ltg5FWQfARw55dsozqPAds2neq3MvjafPldSO32NXkkCaq8a-6xe290fJapbzYsDvC_9LghPF7CC5Png1aLxiF_CeeUQuziQc2vPBAFNQLn1VC_dQHtgwBnynVHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwZY-WWHrbOIpNECxRDWJkhy6_UwR6XDRHkwA9EDNc297KGms2cXYm_n-H6J3IMwwEyNt8P45kb2ubyyg4txmtyQbJ_qPmam06mwI2dciVfyr1FsK7155oar90xtKy_MQOlGhm0e83rOudNXFWX0_1u-YTHP--b99jtMttlNOLmofTT9EXrezjBtPnhOStKvFn-Xc1wZrAUi5DDMbbjbvjwzYoINPC084ekVIoY8d1A7D7i8EFamotD_ZDeJVK60W2vHEqnPT-8guDZBUSPr260sV2K2E9HpWtpIm_5iUQNLeHOi9bsFqJ_ik7iQU0BxJKP5t967v4AcabZsmeVRlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
🔴
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131565" target="_blank">📅 11:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYSwr_AFZUcs75GTF1x_886HeJZRIsuNsGMe2SfqUXIQV2XCEZVVOUGIw0l4ZHiqAIudp4UmZnsJXtXTKUHynFmFdwWBPjoaMZ67hvmPzWBXUjiV6ZE0tp3qK6Ssyr6L8ZtEZus1zU0K3tHI354Co6PFJaG-_H449_r7Ydmkrlgufen_-qyq1rU6oY3BQ2yg7CuRwZAvtEBnosgvJP62NGkJftc3YAqG-8Poennbm0wc_LrQ-3UipKRj90KUHLliOsVr5zV997CokmxrqCcdqF-p5gow8GltGZBZvRiNWI6YDjZSpuenv8z5JKKyJxF_86YDf8aZZDzIJmdtR0kieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFlSLbM9CIIAA0FF8BPRspKKCDrIgkD9cQpyFzicJlodkHVGQc_1hnjwc-lcvpDn3r23d-WQJDY1-RMMDLOyvxF1FnOzVe30Mgev94MlF-v1EylbOSxs84s09VpwnJPrH8clMqAY3_Xf7yPYwrBxLlpDt-EUsAkUzIzFBqG5qInXIG1T0bD_lboewhg_U-c2QbSvyRxSVjq3RnhpyXFEm6nOKQ_t6RNpg7vd1btjIX2dImawb4x87erYoCC65MrDDJQ5WgCDmmnW_1L5x5bW3j8LhtjFfAQBctUl8LAG1k67iyl43mSTWEui1b1oTGiuBUl91QABDfyTEBBzB_XKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vY0sOsHyeyx-Pbnmrff8iG0h0JZqZ7BdEiHgRiSIYHN2LKPp1xthYckDtDAI9ZkUnexPrHjN8wJUvCWxxQl3hlZVXO8ffdc3f2h2WYgcB6pX0BhpyuLLnMcicna9hjQo1FYmGay4WSjAD7yUcJ2ZVHJ_u18gpRpcYxZ7MLzN4B6hhDt0kotiNfFRbHMZG4rq72RhQrKSvJ80I45tGHtActIvYn9bCDU4hNQCBLXF7pHzmRx8PjywVWHtNEUBEhW4hph_THhVUJyhGnnoyTyVE3LH2_YLYTYpAgvwhjwhMatOrXIdZNtxy25upbx9FAjBiHzTohRWEZQpTKV-4F447g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jg_wnyKNqKtyRaww95FA2AqOU8HwnT7ZzrJ5EHzzo0ugBIm1TfEh98DyBc9s7R2MQMCwbj7vhpgat6tZs2lB9jHElZqdoodYrmC873EBk6lVq0V5BKVkS6U_EkLvp9DdVSqir0nNZONsxRm0DD6RQ4NC32iqI2syHFMxpd4WDJFz4lLgljrE54uKVcJ6Ht_335vqn791gI-U50nZ-7NWuhAj7fyJ8WxtogG42yD1TC7M1zyqGFPz8ismZjbjz62IKbDEaKTsmHyNtZl0abd6ZTzrsteKqWXEpICblR-LonMeSe_cLTJFzi8cOVlW3-qXu0o3VNwQXmwxKhTEoc-iUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBR64w1Q5aVmMTNue1TAUo0dAH4S60QgtNdDO1Bns3BTDd3jkf1BIojx6LgLMBElHGiYl_U0tCL13g7xhwIF2Diqjs_vkNIVafcmiiGUcxMNV339dUciyKd3aKa4kS2LYMKakzI4eQeNBE-c98-YhXInRLKgXexjnnvx2VTdVwBv__cTxyc9lnQLk-0R-4OzTJXJazH0CGI5wQ4U3UQBlKi2KXr4D3pSde-a2B-O8FvVFN8C5Ad_lZtbwR1kCG0yB1VDCjW5BREHTYmIkuUoy_AXZGZxvxIAmiOdQWoTK-TXJq9nsGOaUo59CBDBtGJ3r_JvOd9RSYY6zScSYPMZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTJ-PlNM5CYYqLXMGdkPrPQwMVLeImIk1WgUoc-IjkU6YKuos1DlL516zV1eFeVSFCR7WGEH-4uZYyjrspcmy4ucyVFrovEEAwQR9N0GfrvnAP8i5EHn73oOsTj34NKbVoutLHCt4LxWKtX9g3slwsFcNyhfq2adjKlphlEAj1wFYCO8X0nzHCtp1HSwClQ2bRTPKWgGajI179Zs4tEXOtr4zwtm9l_8JV8BwmKn5V2at2IJyjS8r-TF8qWXZnInzZv6KVE3wUNhhREQaRv0BHSZL5CO566xk5Cg3_AUgbpjARCdOgc9miGuZtxgoenJiHx3wCkU0Hw6XCn2EGCWxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار رهبر ملی ترکمنستان با دکتر پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131559" target="_blank">📅 11:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fwa6qsvV9nGXZSkFmbxr_LtLkSWmXhzmIxLvUYueINWkZhGM_WACE_6gs5ea8EX4jKQLwo4bHUmy9pNcr0hJ1KwmZ7BadG4sRvmylb853ffdVI0eWaL9LNXzJGjqJNNHpHjvEiGq4Zek5kGEwqfgifTPc8PvIMpfXEIq0Qk8lLPiNwsLPFL3_PvkclWUl6ukaQ7-uCxqGNbIxwJhm4lnGo9gwx7hwKIdYFCnvfInhoHGVWuLGh6N7Q5bxuOqxNbcruocLEIpHx0-EgPaEuxdUtd16r3hIOQE_NgpDgHtZ0dNF416XgfRMtXhcychviZHplrc_7d-Ueaz4L-LN6V5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqQEFqqrwxKBChDjXeFc5MDgte45tM8ByDZoTGdxPjcN8AZ3Tq4U_VH-JjmAA5w8usi3ka1RNUSWAXmOrVkCKrszfsr55S8itNZd-nH-32aUj8TG7eptEOn3BLTK6NZvVkAhVx8iJeCCOKBoSdgDW7DHl2fQqCFsQo1L75doPHITGEitLVsjJEUHhODoTqeYFcodzyHbWg2f0-bOAQKIG9acZsv278NnJXvHqQ8XGzjx5uxWNw3-n_xQzbTHaJq-evJI1DkRJKiAVCgIOhpvrAboQtmQkH9MyxYfkr04Lduvnk5yJHeuBXrKLiXd5DI0xANuOrxd_qKlP1VkpEhW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1CbrkXT86Sb9PToKLPRQjGlNSrzX9VhPG0z8MguVloOJA5DIkiOl57MZLEMTRIcq_0-p1uf5Ql9jLK1JUYIO-35s966RW12M6OKsLp2eJzKbMUIav8fF8ZM0BnS3cpYwHAgaIxkqcGPGh7hDyXJreUN9xQ8PBhskPbS-ihVuGTMxUIhZZ9sytQTHBU7aJ0EmdnT0sICU6rSQZ0DsGQjfzn7dYs8HV-GM76MPHppeJ5CPKRsgfLb8ir-4L1uab_xP55ibmc3ccqfl8Lv01vnq6EsSg34tJPnkJXp1wPh_1_hFLeLqKYtPKTSdyN3M8kbcL0yjsBsuKi5rkOa86clbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار چارلز موبیتا وزیر کابینه ریاست جمهوری نامیبیا با عراقچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131556" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ3UBGaTKJ_qs8v0fAIgbICQ-rE9RzupLhfMVH_cyI9SnaThUq0pk-8qUY58vgw_IHA7Z_OlosjeVRCgigQA6DQFnTuPpov3VgJBnHp9_vEL4QMudku6wGeqrQFJFKOfXcDHww96ROq_DGBAWz0QH6F3Mn2IOh0Q3fjZW6OvujcZl16HzINr_W2eI4EdbWVaMPE3uGyVC21VCY1x78YtdgIg8vlK4NgRUGjV3ZcBMGMmBmCFD5IoGjhZ707jjiTdqjKs1xpf6b_LTqiejIW-pkc-V6En3vwn46qZq8m5jhl7Hfx_iGnQTN2t7hxC5Dj7GZaoEqRBCslpAsNVYNaIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید ظریف ، وزیر خارجه سابق
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131555" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
قالیباف در دیدار با معاون کنگره چین: اجازه دخالت آمریکا در تنگه هرمز را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131554" target="_blank">📅 10:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=AgHPB6LZe1udpTTD0IWRIZ-KrTI1uq9OZtlahcx_4CVwbHpNNsboEY38GGKhRb-pB6tqq9-NzbC8NzhpY3DfPDPWt3UxjBLBAL5DusA_GaMWGMp6UQWxCKeieFcHRqkeXwzGpPKURaJwRc-9p7LDVgy4oqEjOofMDlhCDAbJM09Rnk_m3-Ywws9lYe6wOMQDqvMmtVsfckCIo9KPKqbNOGA1_8LvsIThupXMrMtsoh2u3iMjUSdHYbNgFFTahP53PkpsxtWiUxmZ_Ev5_7_apBQSamMPeuuTzrWFq0FzkpXUYBJsFaeRI_vmdO4skyn1j8rYb_8hOw87q1dF8D36tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9742057ed5.mp4?token=AgHPB6LZe1udpTTD0IWRIZ-KrTI1uq9OZtlahcx_4CVwbHpNNsboEY38GGKhRb-pB6tqq9-NzbC8NzhpY3DfPDPWt3UxjBLBAL5DusA_GaMWGMp6UQWxCKeieFcHRqkeXwzGpPKURaJwRc-9p7LDVgy4oqEjOofMDlhCDAbJM09Rnk_m3-Ywws9lYe6wOMQDqvMmtVsfckCIo9KPKqbNOGA1_8LvsIThupXMrMtsoh2u3iMjUSdHYbNgFFTahP53PkpsxtWiUxmZ_Ev5_7_apBQSamMPeuuTzrWFq0FzkpXUYBJsFaeRI_vmdO4skyn1j8rYb_8hOw87q1dF8D36tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت جوان پول خود را روی هم گذاشتند تا یک موتور بخرند و نوبتی استفاده کنند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/131553" target="_blank">📅 10:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فایننشال‌تایمز: ترددها از تنگه هرمز چهار برابر شده‌است
🔴
یک رسانه انگلیسی نوشت: اعتماد به آتش‌بس افزایش یافته و ترددها از طریق تنگه هرمز در هفته گذشته، بیش از چهار برابر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131552" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر کشور پاکستان پس از ورود به ایران: اینجا خانه دوم ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131551" target="_blank">📅 10:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=bg1iD0Phrgw9-xm3SJg3Mc30KyYczJZzJJgqzDHj7EhWMec1mFTOXezJjaY_9qw2VYAp91pM1RXsQiilK9QOyCvqwsZSW7-3g8yAK83gxcjX8z8ZjXIJ5j7iEGLt-Iovmb9H0Or2UaMX8nHt8IAJUKGC4kgjHrRjMXcUusM1qMVBGcc7hYUKD80c2BC2qtKPQbPzPHyZi1LMVWHTWHoYvydU6MBW8udSWgHS1Ri93jTzzAbnfWqKmHkW3rR_R1pe7iPffTir4VkLAj9eBIZRQAHKv7Gk3pEpIslFqTUOcfyAVBV5ko-LzrSUegL5uX5Z4onHqtaMI6rvA0KIElmOQLc2pK3jR-cV5A3ypkcJpJXlheIOJ1Xf8FYN4ea6uANexRQQLFZkkDZTrm3PnCwKEmZhi7Iy19KvxUZIrC1V-d0xFONPY1C7jG4pvzoSREh-oIbhfT24jLyyba9wOTubadsR3677YTBXYVfWeUV5AGjb-28nXvYs_L7dmF56J1F8FLaglBbjN5ZqdIWUoy21pv7v2muu8tROP43OTrP_9G5Dhd84NEYBnoEMtOBlNNtiSEhWVTdVzjveBJY9W-Klf2AHxFYgO5SLm-k-B3EX_-ZWpAfs-8d-4eRnwTTkx06Njtdy7lBAMYzOf7ewLN7HGJufzRvQXbdYOY9TO8dEt5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd05539a.mp4?token=bg1iD0Phrgw9-xm3SJg3Mc30KyYczJZzJJgqzDHj7EhWMec1mFTOXezJjaY_9qw2VYAp91pM1RXsQiilK9QOyCvqwsZSW7-3g8yAK83gxcjX8z8ZjXIJ5j7iEGLt-Iovmb9H0Or2UaMX8nHt8IAJUKGC4kgjHrRjMXcUusM1qMVBGcc7hYUKD80c2BC2qtKPQbPzPHyZi1LMVWHTWHoYvydU6MBW8udSWgHS1Ri93jTzzAbnfWqKmHkW3rR_R1pe7iPffTir4VkLAj9eBIZRQAHKv7Gk3pEpIslFqTUOcfyAVBV5ko-LzrSUegL5uX5Z4onHqtaMI6rvA0KIElmOQLc2pK3jR-cV5A3ypkcJpJXlheIOJ1Xf8FYN4ea6uANexRQQLFZkkDZTrm3PnCwKEmZhi7Iy19KvxUZIrC1V-d0xFONPY1C7jG4pvzoSREh-oIbhfT24jLyyba9wOTubadsR3677YTBXYVfWeUV5AGjb-28nXvYs_L7dmF56J1F8FLaglBbjN5ZqdIWUoy21pv7v2muu8tROP43OTrP_9G5Dhd84NEYBnoEMtOBlNNtiSEhWVTdVzjveBJY9W-Klf2AHxFYgO5SLm-k-B3EX_-ZWpAfs-8d-4eRnwTTkx06Njtdy7lBAMYzOf7ewLN7HGJufzRvQXbdYOY9TO8dEt5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مأمور پلیس آمریکایی، یک زن را به ضرب گلوله کشتند
🔴
مقام‌های محلی در اورنج‌کانتی آمریکا اعلام کردند که سه افسر پلیس پس از مواجهه با زنی که چاقو در دست داشته، او را هدف گلوله قرار داده و به قتل رسانده‌اند.
🔴
گفته می‌شود تحقیقات درباره نحوه عملکرد نیروهای پلیس و جزئیات حادثه آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131550" target="_blank">📅 10:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پنتاگون: اروپا مسئولیت دفاع از خود را برعهده می‌گیرد
🔴
وزارت جنگ آمریکا مدعی است که تلاش آن برای وادار کردن کشورهای اروپایی به برعهده گرفتن مسئولیت امنیت خود، موفق بوده است.
🔴
«البریج کولبی» معاون وزیر جنگ آمریکا در امور سیاست‌گذاری، در صفحه شخصی خود در شبکه اجتماعی «ایکس» (توئیتر سابق) نوشت که ائتلاف «ناتو» اکنون به سمت تکرار وضعیتی پیش می‌رود که در آن «اروپا مسئولیت اصلی دفاع متعارف خود را بر عهده می‌گیرد».
🔴
این مقام آمریکایی اظهار داشت که هنوز کارهای بیشتری باید انجام شود، اما واشنگتن به حرکت به سمت نسخه جدید ناتو که مبتنی بر مشارکت، نه وابستگی باشد، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131549" target="_blank">📅 10:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131548" target="_blank">📅 09:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سرپرست وزارت دفاع در گفتگو با وزیر دفاع ترکیه: ایران توافق آتش‌بس را با هدف کمک به بازگشت ثبات منطقه و به درخواست کشورهای دوست و همسایه امضا کرده
🔴
اظهارات اخیر مقامات آمریکایی درباره گشایش جبهه جدید علیه حزب‌الله لبنان می‌تواند کل منطقه را با مخاطرات امنیتی جدید مواجه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/131547" target="_blank">📅 09:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
میخائیل گالوزین» معاون وزیر امور خارجه فدراسیون روسیه بامداد امروز گفت که مسکو آماده است تا مذاکرات با کی‌یف برای پایان جنگ را ازسر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/131546" target="_blank">📅 09:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی:  مذاکرات با ایران همچنان ادامه دارد
🔴
ویتکاف و کوشنر، در قطر نشست‌های سازنده و ثمربخشی برگزار کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131545" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
تعداد کشته‌شدگان زلزله ویرانگر ونزوئلا از 2500 نفر فراتر رفت
🔴
به گفته دلسی رودریگز، رئیس جمهور ونزوئلا، تعداد کشته‌شدگان زلزله در ونزوئلا به 2595 نفر افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131544" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
گروسی: ذخایر اورانیوم غنی‌شده ایران هنوز از تأسیسات هسته‌ای خارج نشده‌اند
🔴
ما دقیقاً می‌دانیم که این مواد کجا بوده و می‌دانیم چه مقدار از آنها وجود داشته؛ پس از جنگ ۱۲ روزه در تابستان، ما با استفاده از تصاویر ماهواره‌ای و سایر ابزار‌های مشابه، اشیاء را زیر نظر گرفتیم؛ هیچ حرکت قابل توجهی را ثبت نکردیم
🔴
بازرسان آژانس انرژی اتمی هنوز به تاسیسات هسته‌ای ایران بازنگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131543" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=VMuSsC3vLNDVRaKuyGt8fZG5wKSNNGvGBIWWsnHwZM1IFSpcOxPxcVUnMDutak2KT58GNBpo0UD9WYeArTSatyhp_brVjodrbyIK5JvcBcLxPVCMSQK2X5ZCgag5o-sXGd78FshpoMuhwAIPnJzcrFDiPLptvH3m3O5TUbCFcNoi5oSuM5des66gt75s-x0Su36OZFHW66PqMk5HdG1kxLnWWbDgM77f2vaVr35SnaEk3jJiV1alnh6egZkXnqiriIb18vyszhjxZU7B1D6Ye44jOu_5xgwsgDeg-HeqzlZ-30YnQ16uPSQlrzm9j_jj6Q1Splyeu-z8Y41v1aLs9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=VMuSsC3vLNDVRaKuyGt8fZG5wKSNNGvGBIWWsnHwZM1IFSpcOxPxcVUnMDutak2KT58GNBpo0UD9WYeArTSatyhp_brVjodrbyIK5JvcBcLxPVCMSQK2X5ZCgag5o-sXGd78FshpoMuhwAIPnJzcrFDiPLptvH3m3O5TUbCFcNoi5oSuM5des66gt75s-x0Su36OZFHW66PqMk5HdG1kxLnWWbDgM77f2vaVr35SnaEk3jJiV1alnh6egZkXnqiriIb18vyszhjxZU7B1D6Ye44jOu_5xgwsgDeg-HeqzlZ-30YnQ16uPSQlrzm9j_jj6Q1Splyeu-z8Y41v1aLs9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل : اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است
🔴
این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/131542" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فاکس‌نیوز: مقامات ایرانی نسبت به برخی بازرسی‌های هسته‌ای روی خوش نشان داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131541" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فایننشال تایمز: با افزایش اعتماد به آتش‌بس، عبور و مرور از تنگه هرمز هفته گذشته بیش از چهار برابر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/131540" target="_blank">📅 09:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYRPMS-pXiqr73kcPWMMEqalOyWSSPdR1y99LYEfMK8ul2XVlCkAx_mOSJ5kiFYxG_9m1lCAzu3rnVT4BXkMWqMDm9_ZcKx53l9De7huXHnd47gVqWvLH6bhZXXO8mTxnPMoYEYASWsKQ6jghq88HLxdQtxt290cdkOws1wgfTaBy2KHJb85qCLePWjnWvxugdJ8W1RiP6JQhQKoGh-f9cbp4zLMEU70FE8NK9MfmyNLbjtZj6YhloMdp1wbB4PA_76HlppHWK17To9MITRRS4J6DttyIvHKqRing28yMF3vrcO1YCt1NWY0RcrKw0piEE7IM-wm3P3L4_5s3X9M8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان برای تشییع جنازه سید علی خامنه‌ای، وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131539" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghDyJDglnNtLToDmdKgT6vM5HvRW_PAfGBsfSHmOjLEXqdl2ANqIz4koDTQL7zJ87x09pC27sSqGrJ9s_80dTQu1nL7OJeauJpRCOmgDWWyLBmjJy0rvmw8JAHtzU0XhlMZLI1nFkhRD3Zo2JOfSaiNXkQr7m21YUf7-jFOhBS7PUQpKYKHtlWHOn5ervFh6eC0qi9lKDJj0NJVOTC43_SIO7aHD8pGu_AMBNQASJ2ChikVEVRWiXqpdPlkKL1P8kCrnaixFC0db8EeDZxPXmRjyVvmLCyVl8Y6t4u35o5JM_3jDn_pc3xKvlWznVWTN7yJFx712nW6rqAnIuiJZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آسمون منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/131538" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
منابع خبری از حملات اسرائیل به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/131537" target="_blank">📅 02:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: مردم ایران از من تشکر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/131536" target="_blank">📅 02:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/131535" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExpWcHgYyHRr1V9LRl9xb0ytjQwljjnTl4-uBp6SbV1DGYMtSDzFaZkCreGNHelv_hZyM1itjxFWp2FOm62kBoofq7kUPM5mf58gs0cU5XCN7eVPVXIUPuvl8SGNQ_de9mQZit66PQsgRzHS1XSfpUfq5jo_OKmISoL_n1O3E-zgPNi0VPSzNdBatk1JkC5ALp5rPaXY5d1JFaR-jgCX3SW3QTBrUA9vKREHf1mWKMCtufXYm3SDYqR0CPDj_KvsJjAMuh9z_o_nbGFDZFn13Dj4MES43-8wPYTY4MXtUYoXyTpm09GrqSqSxZNS6IzDIMQD2M_bT-s5Zb-zpJYEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/131533" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131532">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=KHlL7EOumF-G8lzPnX-qsByevlTav9P59_qoJo69cXtVQTxGWUZ89KgrQ3ZtUz49OI2IK8nwuP-IAwelzd-Rx3--un9tmDuLUdmEbdG6YoZsUThdpnthAsocPr-vPxmpVA2nzb5RqBT-PNKzEq9ma8cPLL4aC9HU0hpYYNvjn2_lJw_b-QOjtfMSkEPOB_L4D0zV1HqefV1lLqICu8vK3DX4H675xXmEOLgQ1y0Gvc-X9XGAAIWaBU-IjPYC-Ad-qV9MOfPVSb23YMnKl7DX2O-jxAm1tS2J904HaSMcDgRLJrxdzqlu7oILpXWTxRVGXE4z85HxBK7jSbWNWAEb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3df6d8da.mp4?token=KHlL7EOumF-G8lzPnX-qsByevlTav9P59_qoJo69cXtVQTxGWUZ89KgrQ3ZtUz49OI2IK8nwuP-IAwelzd-Rx3--un9tmDuLUdmEbdG6YoZsUThdpnthAsocPr-vPxmpVA2nzb5RqBT-PNKzEq9ma8cPLL4aC9HU0hpYYNvjn2_lJw_b-QOjtfMSkEPOB_L4D0zV1HqefV1lLqICu8vK3DX4H675xXmEOLgQ1y0Gvc-X9XGAAIWaBU-IjPYC-Ad-qV9MOfPVSb23YMnKl7DX2O-jxAm1tS2J904HaSMcDgRLJrxdzqlu7oILpXWTxRVGXE4z85HxBK7jSbWNWAEb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور:
نمی‌فهمم چطور یک فرد یهودی می‌تواند به یک دموکرات رای دهد.
من بهترین رئیس‌جمهوری بوده‌ام که در تاریخ اسرائیل وجود داشته و آن‌ها هم این را می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/131532" target="_blank">📅 01:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131531">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=E6_66VUYyyUFi6BL7zIPuHeNLgjOTiAF19pdjeCJxOBC3wrY31PBa6-icClc-kjnfB4k-keZLWfh9SVf4Pu8MW0pFSxnJp55SeAmaUb2DHQoVUBbU-c4tOrbwotTa4y1BkGjkBRg9GzHhDB3dNcvfMU9ht8iHLN4huLAYWwUoJwYvhVpK05Ff2sUyetukfb8CCMPpa6816Zy5WvumiCXjbX3vpC5DKgheFH_ISscxxUzVAS1T1dlOdVrzKrAOWAxhHZLvz17UcCrXL1biCr1Ug14hWguDbVUmQnPp_mwKfXt6QEY7Pu89-Bby2ay_1Rq6H5Ryyi7NzB16P3MjQoAww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac200869f.mp4?token=E6_66VUYyyUFi6BL7zIPuHeNLgjOTiAF19pdjeCJxOBC3wrY31PBa6-icClc-kjnfB4k-keZLWfh9SVf4Pu8MW0pFSxnJp55SeAmaUb2DHQoVUBbU-c4tOrbwotTa4y1BkGjkBRg9GzHhDB3dNcvfMU9ht8iHLN4huLAYWwUoJwYvhVpK05Ff2sUyetukfb8CCMPpa6816Zy5WvumiCXjbX3vpC5DKgheFH_ISscxxUzVAS1T1dlOdVrzKrAOWAxhHZLvz17UcCrXL1biCr1Ug14hWguDbVUmQnPp_mwKfXt6QEY7Pu89-Bby2ay_1Rq6H5Ryyi7NzB16P3MjQoAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان که تو تهران با بیت المال داره اینهمه هزینه چند صد میلیون دلاری میشه برای یه خاکسپاری، بهتره این کلیپ هم ببینیم
🔴
ان‌شاالله که همه مردم راضی باشن با حقشون داره اینجوری ریخت و پاش میشه و دینی به گردن مِیت نباشه
#بیت_المال
#تبلیغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/131531" target="_blank">📅 01:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=I1N4VT5-wUvAJzP2S9BRz2E36QM5O7SvK5HzzSS4Gj52JIkkxawf61qt4ZCEwijl1zBAjOWy-2WhHNCtgO1gAq-MMXjFu_jURg7W99cZW7dNucF0-SBFjAgXAgLWDMPX9VEJAb-NHk3FYIrLoLfqfoEHzmy7JDm-yqLHY0v4Dej3NtS5KAF1Hv_ByUF6ob_57xkS2TPpzyFmBGOGnPqUNBEjqkIcZu60JEOUtd7jFGdD7CCkN72sRpnqQIVgl0tqbG0ojV04m4qlHu9MVeR-QD-ZKd-DlPi3R2TK5ZJhpFuoRknITXgFZNmd9Sc2va-paQWxb3uw_Bs5MpekeugBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937314ac6d.mp4?token=I1N4VT5-wUvAJzP2S9BRz2E36QM5O7SvK5HzzSS4Gj52JIkkxawf61qt4ZCEwijl1zBAjOWy-2WhHNCtgO1gAq-MMXjFu_jURg7W99cZW7dNucF0-SBFjAgXAgLWDMPX9VEJAb-NHk3FYIrLoLfqfoEHzmy7JDm-yqLHY0v4Dej3NtS5KAF1Hv_ByUF6ob_57xkS2TPpzyFmBGOGnPqUNBEjqkIcZu60JEOUtd7jFGdD7CCkN72sRpnqQIVgl0tqbG0ojV04m4qlHu9MVeR-QD-ZKd-DlPi3R2TK5ZJhpFuoRknITXgFZNmd9Sc2va-paQWxb3uw_Bs5MpekeugBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تورمشون ۳۰۰ درصده هیچ پولی هم درنمیارن برای همین یه بخشی از پولشون رو می‌گیریم
🔴
اگه به جایی که مدنظر ماست برسیم، تأمین غذاشون فقط توسط کشاورزهای آمریکایی انجام می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/131530" target="_blank">📅 01:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی: رهبران فعلی ایران منطقی‌تر هستند و ما با آنها کنار می‌آییم و این تغییر رژیم است
🔴
من به دنبال تغییر رژیم در ایران نیستم، بلکه به دنبال جلوگیری از داشتن سلاح هسته ای هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/131529" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfe688da3.mp4?token=hT3g_X7sKqbdnU_xX74Zo3LJzfahs_a58VZZbLHerX6ktvOfEQSPzrM2iGyyRYF_LXBpFM2k4dmbtXDv7FvMo4cvI9NyFxCLalhaCm9gQdU0iblTYflVHlYuBj7vNrKSz8IHCug13sSZgDrGY2TgAphDp8lL9Pl9OLzigsFKW-u6lH6Y54AxBxBfR6vBk72pBQoJ18PmtTFx1GxTym7AxQ6B8biMjfQtYsq8DEKGWdYIPYi3dB3X3ambvj6R1puGI7scuu74yJqFEJA2ioS2AHFwY4SBzHLlXRWeQJz0Qk1zsRC_vcJRPXCmHKgJK2NZfghWN7OBpasMz1WzQ3-VNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfe688da3.mp4?token=hT3g_X7sKqbdnU_xX74Zo3LJzfahs_a58VZZbLHerX6ktvOfEQSPzrM2iGyyRYF_LXBpFM2k4dmbtXDv7FvMo4cvI9NyFxCLalhaCm9gQdU0iblTYflVHlYuBj7vNrKSz8IHCug13sSZgDrGY2TgAphDp8lL9Pl9OLzigsFKW-u6lH6Y54AxBxBfR6vBk72pBQoJ18PmtTFx1GxTym7AxQ6B8biMjfQtYsq8DEKGWdYIPYi3dB3X3ambvj6R1puGI7scuu74yJqFEJA2ioS2AHFwY4SBzHLlXRWeQJz0Qk1zsRC_vcJRPXCmHKgJK2NZfghWN7OBpasMz1WzQ3-VNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
🔴
ما شب گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/131528" target="_blank">📅 01:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673b985d42.mp4?token=ownkD2wAvTkPXBvwurkI9huaxNvZvZDRxAdjMP-8nR06vmXyNoy4AjthHu8GR6eGQSElQrpkup1PnnJttw88yi-cmZJjRqW7GJrwtO0mUEh4og68ThA2w-EE6-EJYGB190jUj6ffj7sTNAWZPS5wBhBi-6SPQhTr1xzsKlRjdIz4e7q5spJ9Xo7hpStKGTKKgPBUFGqrameNVKraQLQG6xx5BMK3ciAHnosMsJGJndjd3f2oBFhHvXVGCoJONsEd5heC9kdH6BYpzgXC-0uohw0TBb-xoRkrcVQu-ofAuDWZ7WWB-LUCiTPRSe6WnALLloC8VtQ8w-pu8l8ZPDrfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673b985d42.mp4?token=ownkD2wAvTkPXBvwurkI9huaxNvZvZDRxAdjMP-8nR06vmXyNoy4AjthHu8GR6eGQSElQrpkup1PnnJttw88yi-cmZJjRqW7GJrwtO0mUEh4og68ThA2w-EE6-EJYGB190jUj6ffj7sTNAWZPS5wBhBi-6SPQhTr1xzsKlRjdIz4e7q5spJ9Xo7hpStKGTKKgPBUFGqrameNVKraQLQG6xx5BMK3ciAHnosMsJGJndjd3f2oBFhHvXVGCoJONsEd5heC9kdH6BYpzgXC-0uohw0TBb-xoRkrcVQu-ofAuDWZ7WWB-LUCiTPRSe6WnALLloC8VtQ8w-pu8l8ZPDrfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/131527" target="_blank">📅 01:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌بی‌سی گفت:
ایران در طول 47 سال گذشته، با بهره‌برداری از ضعف روسای جمهور سابق، زورگویی و ظلم در خاورمیانه و علیه ما انجام داده است.
🔴
اوباما 1.7 میلیارد دلار به ایران به صورت نقدی تحویل داد تا از آن برای توسعه سلاح‌ها و موشک‌هایش استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/131526" target="_blank">📅 01:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی گفت:
رویارویی با ایران به خودی خود یک جنگ نیست، بلکه یک عملیات برای خلع سلاح هسته‌ای است.
🔴
به هیچ وجه نباید اجازه داد که ایران سلاح هسته‌ای داشته باشد و من از حدود 4 ماه پیش، تلاش‌های خودم را برای خلع سلاح این کشور آغاز کرده‌ام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131525" target="_blank">📅 01:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ به سی‌ان‌ان: ایران تقریباً با هر آنچه می‌خواستیم موافقت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/131524" target="_blank">📅 01:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQOQnTDm2tovS_mS_h_8ZU7qcSmcrVD1PrGMTIDMBXbKUYZj2AkCn1gz8ktGRTft9uRgArcsUm-pQhtnxTl4sY5R8BPfV7WmEE6sZoqXZKSjv_Xo2sXpXJfO0MPWRjXmyd7I1WCIx2wskiTZAF26p2zPp3sF1BYdtPrPqkwHxLCP3ePHsS0w3uEYIGf07Th4DwL8oaU0jnvODg9Tn8nKX_MDKosBbQE2z2nc5AxfEBuHEVm-5al6Xi2mFDdjirNg4Q81C46cxXm1IpN-h5mfyEKYQh1otEjUZ0_2XUmLFyaX-1KITGmo4AtAkVioL79Gnyws6tF7riDwG9IA7GR9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی، شهردار تهران: ۲۵ میلیارد دلار پول نقد دست مردمه و میتونه در اداره کشور استفاده بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/131523" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/131522" target="_blank">📅 00:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بچه‌ها
الو اسپورت
و
الو توئیت
هم دنبال کنید
@AloSport
🔵
@AloTweet
🔵</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/131521" target="_blank">📅 00:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131520">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f6f491fa.mp4?token=I9KczZkC0MehxEWgGLre0al56PysCWcu-4QfX3MOeDMfnYMN6jFFHUr4gZ9L9cSx9-DEF360p_LNL-q1-QitcLWr8hfTQ1kOVnfAAfl9whjT1BRIIm5578qbcvaZWSKgbhE2oj2uTR7me90QuYuHd0jVahdZWkvImAIZBwSb7rZoy8ohYiNgdNgw7FmNJbG_tGSr9dFydQmUebhjm2aU2srGesgmStx8ewiuCpQwlepWZiaUqCCzVosVRmDlxAz7T-5aMI9txrY_lVLQ1aLDfc3tsrCeASiUOv3bnbsuXkWkrviwOP1LUn-m3I-qSpBjMtEjFAn6P_yxFxkVKvjAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f6f491fa.mp4?token=I9KczZkC0MehxEWgGLre0al56PysCWcu-4QfX3MOeDMfnYMN6jFFHUr4gZ9L9cSx9-DEF360p_LNL-q1-QitcLWr8hfTQ1kOVnfAAfl9whjT1BRIIm5578qbcvaZWSKgbhE2oj2uTR7me90QuYuHd0jVahdZWkvImAIZBwSb7rZoy8ohYiNgdNgw7FmNJbG_tGSr9dFydQmUebhjm2aU2srGesgmStx8ewiuCpQwlepWZiaUqCCzVosVRmDlxAz7T-5aMI9txrY_lVLQ1aLDfc3tsrCeASiUOv3bnbsuXkWkrviwOP1LUn-m3I-qSpBjMtEjFAn6P_yxFxkVKvjAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه 14 اسرائیل ادعا کرده که قراره به زودی یه گزارش کامل از صحبت‌های دونفر از جاسوس‌های موساد تو سپاه پاسداران منتشر کنه که این فعلا تیزرشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/131520" target="_blank">📅 00:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هشدار سطح نارنجی گردوغبار در تهران از پنجشنبه تا جمعه (۱۱ و ۱۲ تیر)؛ کیفیت هوا کاهش می‌یابد. سازمان محیط‌زیست به گروه‌های حساس (کودکان، سالمندان، بیماران) توصیه کرد از تردد غیرضروری خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131519" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131518">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هلند ۴۸۰ قربانی جان باخته دیگر به دلیل گرمای شدید ۳۵.۴۰ درجه ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/131518" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV-5gLcoYt476D5tFSdNMtlmiy1yugEFpIP2uB608DTurdQbR4cdhaKYNNALEKbSZgeHTWiDKuYwzcli2bBcQYo1noktnTG7a_AzWB3tMIRUqJksiwJeOqLvdC3M09WpO6lt3sFj1F2PdTKlWTyqhWRmAQwlg9zpV1ohO2qx-LKmRYh0UJT7mFV3t7QLkrTctq14mEjWZoNUUlSWYICxHxzG0Fw8sKwe9zME18tPMQgmY9FoNehLKYvQVH6uFL7qnRpy1rPOkWaPLqZBMC-oRazR8AFuv8ADOEBvLNZkxrlKMFDfz0-W--75Aibx_S_ECYGbG9gu0r2QbH-o2_GRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
🔴
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/131517" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131516">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خلاصه هرکی بیت المال و حق مردم رو حیف و میل کنه در دنیا و آخرت ذره‌ای آسودگی نداشته باشه
👍</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131516" target="_blank">📅 23:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131515">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یادمه تو کرمانشاه که زلزله اومد مردم برا گرفتن یه چادر و یه بطری آب پدرشون دراومد و آخرم‌نگرفتن
الان برای یه تشییع جنازه(تبلیغ) صدها هزار چادر و .... به خط شده</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/131515" target="_blank">📅 23:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چه پولایی داره خرج میشه برای یه خاکسپاری</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/131514" target="_blank">📅 23:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131513">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131513" target="_blank">📅 23:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131512">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiVgwQBHnBnD1VVO1JH0XetPlEwbwkewFE5zRJFGLLhNlvI6aaPn8ifFeECusPfar4xfIQIIWj6AM5LirUD2L5RHxm9gGgkaxd03cOuPPwgyzUG-ygObtB3wSsaQg5U6OcT4G8h0TAvJQ5DehcFG9VD16i2m85O0SvQoyVRgHyjNmDeYU7VVKHaws5tYuRhKfoRBYqjIKIZm41JWjvCNMd0dK_DIBJTjv57kTWBNwjSJk7SYrDdteuH8qOZYOE-adUrL5DRlMy6QzbOF19rC_fk3UD7cTTPxQWQrh0SLJ3MFg5RFNeGEbwsbzPJ9mM-YxMz9Uylt-6MCBg4XoLSTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده تو تجمعات شبانه : وای برما؛
تو تاریخ اولین ملتی هستیم که خون پیشوای خودمون رو به گندم و ذرت فروختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131512" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131511">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العربیه: فرانسه، ایتالیا و آمریکا ائتلاف نظامی‌جدید در جنوب لبنان تشکیل می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/131511" target="_blank">📅 22:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131510">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سفارت اتریش در تهران فعالیت خود را از سر گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131510" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131509">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/131509" target="_blank">📅 22:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131508">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: مذاکرات با ایران ادامه دارد؛ ویتکاف و کوشنر جلسات سازنده‌ای در قطر برگزار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/131508" target="_blank">📅 22:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131507">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n24XSms9oLZb6yBcXbfCNL6V_kCrRBYikit3LfBWpLJHGiR66PKxlNSFFOLmbnhvC6qu8AJzREaMDxEMHnnsOsXW49OlBtNukrvZwhT4AKJFh6G77vhJTb6yJPSfGOqfXzOwjVWmKiF3ouLa9SrtaUmwVS_e5PpBIpscrMzy_oYijMFDwV6W12qwtwcySXcIbHE0bArKgmr_IoV0RxUp5Xh6gkDdlR_l-RoFfN_GLy1bj5RG4VN3vuygLiV3gc74ZIM6uTg8QkL6yBT4ZwYoeYc8AtCBJo-zZ2JE_44KbtATYH9ch8W3QWBN7D5ASRj-_ZUE2SuBTYucaxKaU0SnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی در واکنش به جلسه فرماندهان منطقه با فرمانده سنتکام: فرماندهی مرکزی ایالات متحده (سنتکام) امنیت را به منطقه ما آورده است یا ناامنی را؟ پاسخ کاملاً واضح است.
🔴
همچنین، نیروهای مسلح قدرتمند ما ثابت کرده‌اند که حتی خود بیگانگان نیز نمی‌توانند از خود محافظت کنند.
🔴
صلح در منطقه ما تنها زمانی می‌تواند پایدار باشد که جامع و فراگیر باشد و هیچ دخالت خارجی در آن وجود نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/131507" target="_blank">📅 22:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131506">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه، فیدان: اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
🔴
تا زمانی که اسرائیل - یا هر بازیگر دیگری - به گونه‌ای عمل کند که با منافع ملی و منطقه‌ای ما در تضاد باشد، هیچ دلیلی برای ترسیدن از کسی، تردید کردن یا عقب‌نشینی نداریم.
🔴
ما مشکلی با رویارویی نداریم. اگر به آنجا برسیم، برای ما مسئله‌ای نیست.
🔴
اسرائیل فقط مشکل من نیست؛ مشکل جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131506" target="_blank">📅 22:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131505">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزارت خارجه فرانسه به «العربیه»: با بریتانیا و شرکای منطقه‌‌ای‌مان برای بازگشایی تنگه هرمز تلاش می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/131505" target="_blank">📅 22:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131504">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا باید با اروپا وارد مذاکره بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/131504" target="_blank">📅 22:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adq-GHvM7LLwHLAxcJI_CFRMPmE_oQDpd9kNFU0Dj7c97t0a0f5tQJcecEsFRJhLGIWh1ENM6ZErLg6FgUtHhS6BYXv930YMFlbEEFwitF0KzwRInhsFe8hWMhUvxL24L_B684k8y7UAdWCcPnxg956EesOqS2S4BNHee1IN9U74dsUdOW2f2L2IHzXzTyBQ9mX_I44A-m9qzvHf3YwPomqeu25dYsz4JWFzuuQwqPhaZYXKQYmOVb9pagScryfzkbmTlEdbk9uNSz7EMQa-6NdyK26bEoCeAu7p9WewAxXp4N6QIX4sblOsXr44Px6ghC39datWyLvwT7s2cifJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه: آماده شهادتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131503" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131502">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر خارجه ترکیه، فیدان: هم رئیس‌جمهور اردوغان و هم رئیس‌جمهور ترامپ تعهد قوی برای لغو تحریم‌های کاتسا دارند.
🔴
در سپتامبر گذشته، این دو رهبر به‌طور عمومی مواضع خود را در این مورد بیان کردند و ما به عنوان وزرا دستور داریم که این مسئله را حل و فصل کنیم.
🔴
من معتقدم که لغو ممنوعیت فروش F-35 به ترکیه پس از لغو تحریم‌های CAATSA رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/131502" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
به نوشته فایننشال‌تایمز، کشورهای اروپایی که اجازه استفاده از پایگاه‌های آمریکایی در کشورشان را برای حمله به ایران ندادند، ممکن است در همکاری‌های نظامی آینده میان آمریکا و اروپا با محدودیت‌هایی مواجه شوند.
🔴
فرستادهٔ دونالد ترامپ در ناتو گفت آن دسته از کشورهای اروپایی که بودجه نظامی بیشتری داشته باشند، امتیازات بیشتری از آمریکا دریافت خواهند کرد و آن‌هایی که دسترسی نظامی آمریکا به پایگاه‌هایشان را مسدود کرده‌اند، باید منتظر مذاکرات دشوار باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/131501" target="_blank">📅 22:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
روسیه: اجرای کامل تفاهم‌های حاصل شده میان ایران و آمریکا، ضروری است
🔴
در پایان هفته گذشته شاهد تبادل حملات شدیدی بودیم که می‌توانست تلاش‌های دیپلماتیک در حال انجام را تهدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/131500" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: در بحبوحه مذاکرات دیپلماتیک، ایالات متحده همراه با اسرائیل دوبار به دیپلماسی خیانت کردند و در نقض آشکار منشور سازمان ملل متحد و قوانین بین‌المللی، دو جنگ تجاوزکارانه را علیه ایران به راه انداختند.
🔴
این تجاوزات تهدیدی جدی علیه صلح و امنیت بین‌المللی به شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/131499" target="_blank">📅 21:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deh2--uoy5bRaqcI8n3SA3w6GLh3vMJsQSNEF65A0v-mj8Fllde81f312yFR1ba0B5J-ugUdQLL-3YM-oK5JMu1mSOz7y591-1CsF2z4XPXZitxuPZtqky8K2wMGY72shv2hlU7XC1jN69bZSu6TTUkoJv1dXjwAxYW6maVM86aNcej_-QfVQxVtQM_GCbodpPz3SplyrdaFB4hB4YprM5RUEYwiQunXkFmvS2anuC0Ce0xztxx7WYVMw3zEeQoshs3gF-hp-fGHxlC-8VrhLbujCgOSO-hYqYPb-DTJGwmFcXF3j4tfwJ05OzBVSZjXPPmxsFlFdM82Kak1zdSnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه توهین به پیامبر و قرآن را ممنوع کرد.
🔴
این قانون با دستور پوتین تصویب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131498" target="_blank">📅 21:43 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
