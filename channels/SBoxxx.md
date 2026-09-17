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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/20957" target="_blank">📅 21:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/20956" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است.
هر احتمالی از جانب من وجود دارد.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/20955" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">— اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف، از جمله شرایط اضطراری بود.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/20954" target="_blank">📅 20:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:
من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/20953" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk8De3DTT8CqIKw3zWX_hSpCBGjn5ow93Gzrq1x8rSsGwJ_ohEKSma1NP1KWg5GW8bJIZtZE1JzxzSo5NO85g_0vqmPcBzz0-rQRkqfFGlKSzrHMNfa60GpHRiXA6alkgLZEj9RtgcpmkEP1xi5ySd6reJLp0SJBlvSYvECoV2J84KnU_kFeetU2hPoRPtJkBwiGrY-_svLc8rFJitqepORWD8vH7oKOe9thGZ7a41sAmrLteuzbyJmhJm1Xk4bcVs_wVvOxaz62kGeUu_WDYhe3T84fs2rBNul_glLwtfIKVfw5XsR8-BefFIkokWjBDP3_y6YVthWrBHftnaD1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6heC1XzxYLQd8wt0-DC8_ZdZCE9nuO0uq_HdGF2aLRbg2BpovSJrNo78gFtxi7EyA8W6uwFnPGj9oW6gd7hRHCxR0-TUYadHMuu7Paz9krLzywYHv1CM6gJer3Hc269_0Z0HMdS6R2b9WSLyZAx1TpTtdPVu572WiHWb2tuj1-e5kUH_T3UkRQkHECrif4Eqt11bAXDPYNjCBWWxsCce71kCMUx5XWOv1qxGBnlpkLQTGX68R2_WDfmA3PYYzKW4TN9UCmd9Z5wMU0tVvhLlD2yaYrr7zwtaxki-hAxPfiVWbZgDsCohx7KdpfnTWztBk5Hs91jz-4w21rZybj3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMaBdz-BRH8OLUnQB1WVu3ePcFmCYRh0ErlqSo7I9wXGo8wI9p1yFaM5Psxuxtb9cjr_gUJUzPbFr_Q7mSQ9g7lByHptOLVrCNvGq-tbn9OnWTihWAP1uSVJEWWHXKErFDxJ4biubVvsHPXRMe3IgUYTs7mINQgC16kNY3FWYV7CIo2qPQxmoO2eLLnoxYwt12F6aFYJTtqrVNKBUcnCUxS9i0k-jW8aEamEEJm_PemDOEqZnUjLYbnYHy4HbtWdWjw7kFHcm1ANr0NDchni-Aaqw4ZHCtvxBCtnEObHMvRsSjYgS8CWyZtqCoM8H2yt-WvImLGsnWUuzKG6U5I3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCrXN-2ZUznAAlWZKI9kJD9dgzjmR-X3dqUWR4NXDNmhB2Sk0jciOl9FmiZasPDYqTUBkmcDql2_bazC7py7myXQkASor9sxee-87-GQ2M3SfjUzFLusNCM5CM2gIiQIiur90H13Zd3q37UTqr8oHMzu9yDqRgDHz8d5XGkzsquRmjGIaTlmSptnXSMelxsC3MEvy-9kDbot39wMj7bb8xoJcbwNuPv3MDwwzzzBc5lrBEh-cJwwl0TT8sIXw1-WBPalIALKlbPCA13Z3LkGr9MnghcJtxLH2cQYLe0LREgFm83pOqPov1jPDGFIh0IICKniDHuOdTv59Rj04qmYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqAjCtZMmwIlkOYaCs5cFlsARRaXiMZ8hVB2mWLGuIdNRLbiitBxQ6WzsaVy0TZgK6Oz1mFR-Sn16HOdsgT6990kDFr9UlsFKoX_w7VBbVvvZ1amzqWwcojOOgJMw1ZP80mB3BiSNR4jXHSrcwmFjVOGjc6MSbR7mAUiatK6xOvLYOjEjtSSmMoWgkaTyp_8gTgP7tEK8hqsnnZTAFeL7wMbPU1Q2FULS0W3iwCUq6OYL0MhVf4mA0EH_KolcURDEgCxcXpaLW6pbVeiwi6ssz2AvVhZEEJe8GqmVWGELs3CTNAJH7dy4wxga0IrVONyqBXQBt1wzkgerwKKyPUh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFIQtACTg4hryQDAU8OP0VXT0LXNJLmmjKA4rpdYCXpPQ2TSqJJvBz2yFAULL-1LYoW-DNBnz41uMd6OA3SQB8W6Vjry123LdrXkOdnjcYFnN8wFIcY1eeskWsowSch64oijLzeS7ELTkNcPvtE4EOTr4OYnwXpenh8uenotnxEW5zZmm1SCuwrcXlBoyk6thTq1S5dGVS1yHYz2FIYJ35IGDiqKaBHDnyU0fbNH_CN94Lr57E7snZZKVi2ZmCjB37dFEu8dEjzA5OXP72rL29yi5BymXN9iCuzsoHLoKVj3eA3viXK2bDwVb5DXUHwH1CepJpmwUdy3wiTcw-Zftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae6gv6Z_HvXB2MkVuQP8pOoCbfmggMiq8LyswKlSI7Gt4hVk7unKifeXTEN8jZ9j8wy5O1bBNF0XsfM6uer5j462DDtqtlufQELKH8B76AMEwBFE4T0rayaoNiat2lCuuMGQ_gNuUczFkXyYFWwonnfoAcFO3AcCAgHqmTB7s4ZAlV6VlsTov8w_CToNMgg8kpbQJfnrQN7SUaNFUi1EAI5X6nKjDESornJx8o67oPBv-t72vwwpEkwNhFXn6Mf7PARkokXeb8_dpB4_3qL2HZ0GHItGNcgQAPa9mXDdTcexuEZBsX9oKQTfedJToRRqb1CIwh8wY465w07aq3G2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt8IgHKA6YaxxjDQ6bvwKoiZYoxKU2KcRI7j5BYRDYCIF0sjqW3gyUcxZT0DWFAOLbXPOKK6wNIKx2zLrwmd3NJf-sr8_onNo4fO64pBZjcQSvxxFqtC02Cm-sY3pjkmgWFP1BCciSw4-th4BDfm8hvBf7sIhJgbxT_NkjBqGfDj7XylAuXpxnqSzvq-v_7CA_gyjQNbYst9sMdLzTWZnwWwPrBTYf7pr3m2RabLla8v37D5kV0krYSIhBnXOSyRtYDVxXKIO47mIZ94P17TUdGsenrmVU8uKWSCn_eBoFjBqL48MfzZ19U02f8RCvIkLpBEHOggnhJANJC-TRarBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=ixanZKtbuv5LU_VWUHPCnyHCNTTPZdgRP-tPfbfhIu8f1phuXr9Jr2b9pwP78kC5FT7Ei-u6Qf1VqidJAvkE_oYPeG3sDURR9iUCUCmLoqjypuNK4u3HYWYXxtujbuO0L6xdpICDSTM_HhzscjhNMvT_Pgp9k7-5MFpedxEBYPWBTHPn_TBHkWTnt2XXB28lQ8yz2GXiD51p4K0FLgK09_kH2z71t4YadfsSezWI2Gs-fxN1Nh8FvzK-C5ZkZLjLKL7M7Yz6SD_p7bDzed3TKCeW2BPIaiLyQyJtVzeQztukSuf361RpmBQJg7AtYFnVcOa65FFSyt70Ub0DjqQy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=ixanZKtbuv5LU_VWUHPCnyHCNTTPZdgRP-tPfbfhIu8f1phuXr9Jr2b9pwP78kC5FT7Ei-u6Qf1VqidJAvkE_oYPeG3sDURR9iUCUCmLoqjypuNK4u3HYWYXxtujbuO0L6xdpICDSTM_HhzscjhNMvT_Pgp9k7-5MFpedxEBYPWBTHPn_TBHkWTnt2XXB28lQ8yz2GXiD51p4K0FLgK09_kH2z71t4YadfsSezWI2Gs-fxN1Nh8FvzK-C5ZkZLjLKL7M7Yz6SD_p7bDzed3TKCeW2BPIaiLyQyJtVzeQztukSuf361RpmBQJg7AtYFnVcOa65FFSyt70Ub0DjqQy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0TJIUgVYwWZLFK56hxfmB6vbKotxk9A5UOhQLgOxdC8pZKULKZEKB5WHQhNMREZIwAniX61rWOa3ssCKuiQmshHlGaw6-GT2O7SivxTcwPGQ7jFY1_isXeZkysFYKXKUO8QOCtrNmeQwJerb9QSj36h8DMWtQwzQWLAGrA9OjWjShKFcO3IMkRRinUgS3SoDF9wEWxmMPFpHhbYC2hV_RMVzFNbh7pd9LNciL3Fh6h3rax5jbLjYB9x9bi65Ktas3NWH57bvHRYJIWZ_7UEseqltKOUt-cWJxSQ3r83lFWWciNYFMyIK9gH460Nm4J7Q-olUeU9dGBVyrOfBwOVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcFsPcwY-hLhkMYoDSiuZsVqY6bHKrxO2B1XMJNdnOj48zWfAAW58SPDdMIUiiCcBoLlo87vFpieIbeIdKAnJUpjbPM09NqXFI16nydMjEl7vOWLRww6aKrDR8UA-k5z_s-dm8EHepSs9q00iosIhZ6MZNr-n10bSaUCvWLoEVUSTwCtMyHPTp2WtVHTOrtZN6x2pNvGNhNF99GEd6j9UsLiWiRSVxk6a6nAoxmE9SOvE-iTsVT5XYwtD8Nq36TRQ1Z83xrLGqc6BQWSczEnT3Q8eECskUs5_toqQ70cBhpcN1HDkbMmpb9Rt6mQjihjA7GfDhSPq4f29pcqNrYZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH15ExCkv6u5vgPVdgddVnd_oR1yOMW5ybsdFW9yEFI8zCEyjKvvXobcZK_PgjJ1Wn10hjl5VDeqRfpIO-BuIZ9ODc5_TTqUbf_QQKsaU-XH2sT05tIEEHUxOtHH_qzNsGO89Tr4yBEmjIY8MrV6uRyVVJ6RcL0tBsVBz2ctNDnlx37Napt1qNkNW4a3OzU7B-R0ytI6FGieWK5pgCnf93Ll3-8esKx4P_HUR2dW4dJHyrVOb30alHUCWDmos_PjS6GAnGqErbnYti8cbOXHD7QxTGwARscoTJbLJBLWP96_dkQwNLli0sR2oNWjhNlWlstGYsnmbQuOgGnIGys5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=gNAs8uUJ83Yz4qshoh9qHvgl2wAnuKiGJUd8xprqk_OrnrxcyNFzPwK3xugvzRnsT5HUmDsqNbTvQsne631h12qzT6UKJyxZI-uZVnBeAoR5EsYi8sOLkySDj4Bvrfuypz9R4BD8GQsnUV6o_slQ2lESyD1V1ZG9JW-iV64fitSK4Sp34qfj_LTizC8EW86labnJzHloD-DY5KeDWvZz95GZ8KHeDH7od7TqgK9wBlVsm8Q0XsB8gn1tgnZcmmq-9Z0MVHwtogsW4GmnQd3dZq4SVMcySgQpV6Ser0X459KZgWjDJP8ZczMwbZaidi8Aiy7EVNlkUAsFp7QuSsU0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=gNAs8uUJ83Yz4qshoh9qHvgl2wAnuKiGJUd8xprqk_OrnrxcyNFzPwK3xugvzRnsT5HUmDsqNbTvQsne631h12qzT6UKJyxZI-uZVnBeAoR5EsYi8sOLkySDj4Bvrfuypz9R4BD8GQsnUV6o_slQ2lESyD1V1ZG9JW-iV64fitSK4Sp34qfj_LTizC8EW86labnJzHloD-DY5KeDWvZz95GZ8KHeDH7od7TqgK9wBlVsm8Q0XsB8gn1tgnZcmmq-9Z0MVHwtogsW4GmnQd3dZq4SVMcySgQpV6Ser0X459KZgWjDJP8ZczMwbZaidi8Aiy7EVNlkUAsFp7QuSsU0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwxeOMTMmqrzrrDc0RpOfBCTYyFbvVHFA-JSDyNJlvDfTrmDaeZdAO4cMcgn25SzyaOf2NDStRi8ZHsXvad-v8Ma53W49I6QeFtfUsk6-QzwWSiGoQZsyh2F0n6DwJSGOwrx2GO8Ac7uSAbhOu1Mr7acjnqz__SbQc3VK0upZPLea8jJhWJZdi9Avl2-kR6c-s58Ck7GXkxT2COiOilD4GptHMDdNZ2pQunPVsS50y9EPQvj5SQDXXgu0kpAoTm2fCplomCDEZoyNl0DUABeRSv2mjsa1kIqj-I6JAZ6A0_OEG6MI96LSX9J9SqC-wGcHHQrBiln-Ffs_gVVxLklNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNx4C4Oa5JWy9oSRXZCTnNF6p5paUMu3g8k85-W5OlK2bUEhK3Uq_HYD5kt6SQm8OdXnGaAHNo62InpK13AR18WfNh66bAPrj1vMVK-V_l7sJhzA2-ZpGWNLELpBURxJbWYry4jhk8_KcboeEnQ7IQ597OflOEbK1ADISmgohmtJQ2uumSViKVv4JmE5o8273dTxsR-ttK-gXl2COUBnPH6Ct4h38mcYLvwxiD52E6GccDRxoztRZI0bOpZJNrZ35J5sbilunUTaG9Fd4D-NBQH3foJaB7SWWeq8rYaVkZFauRU0kRrSAgKNPbwvRj4ZH_4EM990CBvw9eLLGgY1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpkMOBnbnMvfnIjwuRamdU2tL-3TkkbErgW13uc5NG1_WOm6hf-tawIBYv7qmUngxfA00jZF-7b9J5t7nAoZ6ha8phLDaFbvEOOIGlgjJeyAQqAffyIYlBK7u_2wqQHsdlN4wWnZYuqykHpWoDA6CKgcxZN5s3HPpvtWlxvIoUdQe6tdu3VVY5V7YGANNQSCwiU1l9-6DnldcvZQVTVsDtGbFMhwmedF0doEKBEDXRuHAb0aD_QgjSst9qNRy-WamerJj7jyJl9TgOzVIcRTUmeEjpZx1Rn6ggEoG1QIFQnk7yhYyj1d3d8YNz1V5m-VaTav_RW5x7CfIZfNGlK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnazHPkC-HdCwjZf7uV6tzsiRStS4mz6zoxusFCecPcNAP1R1gUa-CrDDIqPgZE-GYWiJs_ljFXWbceTRjPNp1TpCEw56WY4LW8-quh236td-ht1l-O1zWrwbOyp5a_Ek9uHYSN_hhY8KJcoZIMMb3rZzLZ9po_GNx39zFaq_yRWozj-evA9txjcTflRibKngVkKp6gt6Q6nR3OybbyAHgyoXLU4WdqW-C9-RAVKqkYuBJJ-5pr5UJku1iYDgZSSfHb8U9GN5YbX8Assyg8iD0ycFFELKfZ_RccbC9UFvQxJc3hsK-4aNi27rEh28pawTJOHq-tbR8bn7j5wqxqhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajvdlP-9AVq5zj5tMFViwT2Ml-vT8zJPCJ4GnBQrDCse8y6xQ0yMX0uazb2V8sVaGzfWcvH-ec4Gxpn4NlLIJiD5C4UsF-e-H721sgddEONGVmLRxRULOhR_YTY_mBOOnoe-_hSveexclDz784Feb5D21V20BC9a-B--azDhDpTBvL6Qt3CvrIPHzrvwWETEgG4goOYgMlqbdaK8ZBbogU5ELF0FDx-olq9SIKzQu74Jxdist118NhmgDk6-_rLNQ_AMRnZxd5jUYoNybjHICeGMsj5VuszdCX0yWBvY0B8eLM2lvWZkG3--GrmVoOxqVZtl5BVKnzWa4x-pJUhy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYK4kJgkf3M32iJXIvprT9odMJDkAe0GRj9mSKtWcnJVmpeH-qpljHqqn2QLdho8RUQSkoUHmzmpYJzRXgvKS2qEXm6QocCseSUc3xMlGtATeMZaMzKaV8N_xmhEMLlnRanGBrbM2ggzkiOySc6BXgHq-DwgkmJk3EMZqIZLcTIaq5oaZSVc_lwoltlaseoLfmoeo5J1_Z17vcpO6V0Cphdm9mdWsNvd64MfLCz1Xf_YPQSLlWEbS91fBLhJVD-fR5SI9Hh2CLmLJNYMEMjb-n8OSYmWlBzmZOdXgscOoOtBZtFNuXCFzxoAEfmSf5L0HtxMQ--L7DAegUwsqWxk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd6jmR2jZJWxRz5zGMLMewlPzeqHEGuejaCQ2nr0MxMJc_1f20ufBVe3Sb156EpNLN6Juyjwo-r33-6lVFzrK66fAGj9B64BxK_F0qyjLGRQBIEMtiP1HKkf_R8mkJvYEWhu5r03ARM4JQmpSVMFM8-TlWHGfKGI54fWYuBiO2fqWqic-mo8tFhv0AfmHzAcqhsU9ktpjIcsmmK_4VP33ju7nNs_YcFTEp7mUkT3Bkhzc5bGf8aopKNouIXlmp3tLnNYj6mHGJuwp6KB9tHmf06E2tcAeDW4zsVXrg5j4j1k1iCgvunm13sbQ9DB8Be2V2aA13uNIZzVUuxI8JcLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZREdDCkS_rdwDp6vnOVXQYwf7HjZQTLehPvM8mY4HfkPQgeASPARr6YSiFDM1F-AOaJ24aztpQ8r5qbTE8JHdfnyXf-vu1jrqqf-xgIJ0tvM_1TrTpoF72n0dFESSjh3ZdzVhxuSpKEXv7KFP1fRS0tXrM9DDFaQBxZZMtwdzq_qKIh_Z8hzR-QUpqD628kJ9Pu51ouQn0cSzWB5VPUivsCEgd-8GJzqlJm-CeyLDDppubGewApp40r5wUHvfl02Iq-TNPaj8hEwHpfcVOknufbAwCQ_4w9gMmPzGWi9CeAjrXIexw91-BBTlR5-qa1bSVTgVxP-oiP4V2TtkFOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjHCk_H4ig2JMVbUCC10GM23DvEHg8aMi2pBBJ98RqBTDRqmNpcQ0dqbHitjZf7ay8ALBETVXna93r9jDbOKBkCN3p15RN2Vz4JXp2McWZCuqGgYW7PlPTEaomNhNAy_DCfOD2UmB-d_y0Qe0PCY2vHvceQtzaQv76UjeEnkRPx1qaCNutdGueWUIOFE9jTxGilMCWrPSg7QaUXkl-bsDgLjHKwiHJZYH4XCeO1miA3giANqNvBwM3r-ggyBIKllcgflKZjWtlXs1uAQViBuxWx5JrLJSY3d3s-xjGy5R3P7r7biFrgcEsWLpkdCNovbZuyeUwlxymW_H_k1_NQgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgYjwjfGYbTr0f1NyjcNDzVx5O6Q5w4swX_qb64jvs5z8FZqcRJYnRjPpvUjJHr6PGg82bl7t_ghH6HuPnDpl3l2AR5RQMlVuZ_9WPS0v0hin8cdBQ1e1KwQmK918XarAKty5MWCFalQQiVTIOm1tfVACN7yK0Ssv4Lky6LIzlw9pOxNtFkryWL_JPQijtn1VBRNeQYFl0gqDxBvLw0Ra1FReEFEC2l4rcxAmGPGeCIWorBLlez53HfElAZEgtjaHnEtc2CkqS4SZhHhOVI0Kgg6De3RKB5qdMXL8WMPXdIkCRdaCIp4VrHqBFLN-zpiqj36cK1u8vjYAW7-UpgR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoWxYok4nvJiFxR5rBla-DSlduWQx207CTrnW9Mr-TJ7du7UgayBp6eTd80GQzkCBC7JmNDSNV_u4H_FrJcHHugiq6fhtvVqMGgTwd8rz-E-kmGcf627Rtfp7thDiIOY6b7iYS0dkRpmQ80w8a0tGe5iLzYvYjio5gDUBD7vulhox5qT4GdJBSR4KxBDG-5211gsSwfW-8BMiUQqPeEWnVBfCDrO21YSuzC8jfLF7zrKdw4Hs82L8hDJoqw9lGP08xbKxlVMQmONBvmhGwMbFTwn7FC9xetzBEcqTO47jRx4WRxRZKwIoFcqhr-grr8av8mdZk3azY4RmXLV8mf7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYw7T2gySX4ajOPcOHlF_17f18AzqbNJes4d_nkObXbDB2s8QudyWlBo_QFb6Z1hi6jr11uFGyUvJToAkDRd7o6cb9RFFPpNwTSj1GJhW_OgMBuRbcICYPVQQpd3F5jFwkBbKW9N0uJc5Qq7FkfDovDPMz3WEjvO8Nt4uABmRfoXCQVAuZ9p8TVkL481aOY46o54t-legVpZEVXGau9LXaA3WzrrGH4G1whwan38VcidqI9dX6C9wtyHHqo3Ei3m2Gv1EAh52PnmAZaUHXu5Tfopw79tidzZRWWwaR3uSm7nAXU4YjWV7VIygvjnGtvkFP3z9NmR9P30hPxDeDn9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0JQ4gs-YVv7mmhrl0gRgXv1LlX9fhnj1f2lGcX2s6rRHh57F96uU6TX08Ts30IqEmLcYTlp7GejpzIg06FTgCwNPTJMfKB9wEPKnr7XSJaI01eYXMlD8gYbX7ddxiyS4Ja48wCs5eTkKAyssF4Ycs6yX2M3nDiSjTJEpx-mzTqikFexB9Fk5zy8_jJV53x96jnmElylQeuSVqtVU6hNSiLIQHX6ZVZkMJ6qncRWFxgqnLmtsLSA40FpGCHr5QgOSXOwnagKitw40T50baoQ9NGVUNRrJAFUQaWUCQDFm-hsgP2w6zbtE4X7uqijXZ5Ja2ThXGldZ6dNMPXrHGlU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiebGIsIEavpNJtv9XpIh9Nb5WNMS8TjMKViL_n28qWR7V_dX9TcfCrBS6531IPS9rt3cZQb7BClAuWg019npLm0G7prOAAaVerbYCglfsTg8XVI9qpqADfo7TpaK5_Cu6hh5In7r-jwD_Cw_jQxJZl2Gh5r0vCB9sTcfOrvcwpHLDX6z6KIAAEZT59ie3y8NXhmgCIe3HY5w7wd_LBfsjibm1hufrCMhlRj0N6J98knyfvwDdDQ-Yt8q75FQo6piEcRiHoO6oOZCYIIi3zaPX6FeogsgQBeJKa5EO12sTPUKO0rDCpvp_5Kwk2jZEGnrTnQphhW6h7J4-kQx3FnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNHgvhL_DDxtDyP5CDY6PJGNdxbKlgu2k8mfNunXa0dhOaG4StICQRitmAeuvz86hCkXJ62HI7U-n3kymWdX2_y_ZJM1jz-tUOY7wRBZol1dLiCM4qfNzceRZm76DGpY9CkkVJyJjRKKEfnoVtCo713N67BH_hpcE9C_qY-Ln9nKhJRfvtoK3-Aqf_eRvEfBsKo9KHB7NJDxG0VMQa7sc0ja3IxVYfOoXNWmpK48k-i7vZG-uv0eG-ScH90U6nhoxDnf7dy54K6RlkXhAVdtb-q6WY_s8K_THBfnU56VUGwDln2cGGZijHdJ92_TOwjl1o6ghOmrMoWpcqy-arQkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN0g2rHcAF-N9f5BdMci-kQm8qkOQUS9a2ThCMkt6qS2tEe4sjcZiQyBOr3jWosm2vhROJRXEfpCV5ifB8RIIBV8t1VVJ9bfUC7IB2w4s_CLFsPsNdBeAkRmSoJh1z5xJnPief8OuWEb0nFv-KgNPsVDu8MwCTBzmYvWe4wUEyvar2WHR14GHtgsgDomkV880G_ZjkLUzd5s3DGWTSk2iHcj8L9Z4_OUTmWnE1sENZBpnzxkqBn84wCDQXXe3EDXinufeawVH2fX6P9OKsSLdm-A4Y8PqVRmnb1DS4IU0KxQ_QJGRnK-j92CHsUUEO8DiQ624l5BG3kpguaIEGRvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCRkrYh6t0TgdGSZQBRuUXs01dgBJUBAVgHqm6q_C6Po1WFHL7cgBq63lDLpFn9dFO7rI1GH2yk3_evHs-1Rk0yZVQPC5kNecV1bY2Iy9d4RZ6LPITLahvTiU-mZnXGfHhfUAzqKqTNxaVJgLg1ioBNIeP8gx0XBKI6jpT6aRRWUzo2t_kFt1xjjscjQh4znkvx4yN177oNW0-_8jZRFeO_HrMe5ePyKKo98UFPtH7ggTuJ_gOWAjXxv8ivCKJ2Jnm4SdZd1wJ1sy7jHXPd6NuPYCuUHBaVTXP_-wvqrEBYbxiXW5gs7rEzugSQq3I2u7oAj9R9UFiDW53s2Pzv__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIOyrHN0T1hgLUjvFi8MaFZUzYNHp1QnEZ60vxqp49uZ_s7BKHDuvOUt1lg8AlIzv7K45AvfcpF0XkJux10aVlExkfQDlNpp4_irRERkghcyNH1w1PgSEt38OylA8vT4vFOJhdROlNj_nQ58qbzxxTb2MYoEwZ5OtclD8QvSghkpqv3GBTeIHEwIoHZs9iRs6LgtTH7Yfx9q1gWE4vJqXCB57IzPe_lSLodxJ_LvWplvavRKLSs6yotPQxnB6V84dCYcRCqdUfsAOrSECPybGLngxiVCIhFWyn-hoTf-s-onPl-ycfhfq5NMvlg3XjSEvsheedEcKSS-ZWB-kb7iAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی | سناریوی اختلال کامل در مسیرهای صادرات نفت عربستان
یک سناریوی حداکثری برای بازار نفت، تخریب خط لوله شرق–غرب عربستان، بسته‌شدن تنگه هرمز و هم‌زمان بسته‌شدن باب‌المندب را در نظر می‌گیرد. اگر هر سه اتفاق به‌طور هم‌زمان و برای مدت معناداری رخ دهد، بازار جهانی نفت با یکی از شدیدترین شوک‌های عرضه در دهه‌های اخیر مواجه خواهد شد.
اهمیت خط لوله شرق–غرب در این است که به عربستان اجازه می‌دهد بخشی از نفت تولیدشده در شرق کشور را بدون عبور از هرمز به بندر ینبع در دریای سرخ منتقل کند. ظرفیت این خط حدود ۷ میلیون بشکه در روز است. در شرایط عادی، صادرات نفت عربستان حدود ۶ تا ۷ میلیون بشکه در روز است؛ بنابراین از کار افتادن این مسیر، وابستگی عربستان به مسیرهای دریایی خلیج فارس را به‌شدت افزایش می‌دهد.
اما اگر هرمز نیز بسته شود و خروجی دریای سرخ از طریق باب‌المندب هم امکان‌پذیر نباشد، تقریباً تمام مسیرهای اصلی صادرات نفت عربستان مسدود خواهند شد. در چنین شرایطی، ظرفیت قابل استفاده برای صادرات نفت خام جدید می‌تواند به حدود صفر تا ۱۰ درصد ظرفیت عادی سقوط کند. البته این رقم یک برآورد سناریویی است، نه پیش‌بینی قطعی.
اثر اولیه چنین اتفاقی احتمالاً در بازار نفت بسیار شدید خواهد بود. بازار نه‌تنها کاهش فیزیکی عرضه را قیمت‌گذاری می‌کند، بلکه «ریسک عرضه» و احتمال تداوم اختلال را نیز در قیمت لحاظ خواهد کرد. بنابراین افزایش قیمت می‌تواند بسیار سریع‌تر از کاهش واقعی تولید رخ دهد. ساختار بازار نیز احتمالاً به سمت backwardation شدید حرکت می‌کند و پریمیوم نفت فیزیکی افزایش می‌یابد.
برندگان مستقیم این سناریو، تولیدکنندگان خارج از منطقه خلیج فارس هستند؛ به‌خصوص تولیدکنندگان آمریکای شمالی، کانادا و برخی تولیدکنندگان آمریکای لاتین. شرکت‌هایی مانند ExxonMobil، Chevron، ConocoPhillips، Canadian Natural Resources، Suncor، Cenovus، Petrobras و Occidental می‌توانند از افزایش قیمت جهانی نفت و کاهش وابستگی بازار به نفت خلیج فارس منتفع شوند.
در طرف مقابل، خود عربستان با یک تناقض استراتژیک مواجه می‌شود. افزایش شدید قیمت نفت از یک سو ارزش هر بشکه صادراتی را بالا می‌برد، اما اگر نفت فیزیکی امکان خروج از کشور نداشته باشد، افزایش قیمت نمی‌تواند به‌طور کامل زیان ناشی از کاهش حجم صادرات را جبران کند. فشار بر درآمدهای دولت، پروژه‌های Vision 2030، پیمانکاران و بانک‌های داخلی نیز در چنین شرایطی افزایش خواهد یافت.
اهمیت ناوگان نفتکش‌ها و مسیر SUMED نیز در چنین وضعیتی افزایش می‌یابد. در صورت بسته‌شدن مسیرهای سنتی، دسترسی به مسیرهای جایگزین و ظرفیت حمل‌ونقل دریایی می‌تواند به یک عامل استراتژیک تبدیل شود و نرخ حمل نفتکش‌های بزرگ، به‌ویژه VLCC و Suezmax، را به‌شدت تحت تأثیر قرار دهد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20867" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQCQeh4kpM5-ClCcR4gtfoO1kWCciKng-AJ7BV75pI-AIAQjOVKm3goGMVliRDuoV0R-3Eca9Et0eUD8WXOJCsprojcGl8ALSG_FuhjX0A5W3muK_3B8Yr-S_-kboap1k0VnD_HJBHvG3KzE4WRCs205atxENQ9QhVSEQX_GIzX-bM06CNYafpNV4y26733Pq14nTbwqoZE6p1ScplWwMWul82-rA3svCwarNdRiJW0eF-J0wqDZ9Qb1omJE9wXJMPC3fBD2VLN0Ly257_G3-4Onvff1hbujZdsBWkt0kbZKKwuGRb4Jy2avLydwi80qis3dHXGE738RapoBbroN5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu0QBLs6myVJm2BuYysC6Wcpjr5p6DvrWoljH0_yG0HKSvCt3u9qoR1szX5hecdq_Nl0NW8twL3KkfaxlekmabtRfqkt5Qk2w4LKfyYZLtNiLwMpdIF-6ku-rJErVFJ1A0HT2V-BdgHMKTrxC7dJ8NSuKebp38F32QXwAvtGETycpN_LmjjnMm4GgxP8Xd4eYx__UykC2foAJsiqrAb0SrnAx4IcvdhqZDpGQ60wTDD5MLFC-Pcw3mrfCXdeuM7qpViFJyWUiR5AkmOV2WVW_jEQKXY0_G-gl4S72H1Qghum3Br1WC1kwxrzuPGX8toAGOvwkeJUs9kHfONFBtPsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl7mpuH9Loe73dKcITWy5zdBpTVku37gRScuDdxqMW3w4Q1s56zBmP8a_I4aHKEwr2sig0x40u22n7GFoVEbCQDs93xfliwe10xyCu33ZzAwUJ5d61ujZDULGW2Q0tC6ixe4u_Kt74YOffSARVCLCXRQyUBUb8BO4rJz1QPAxMQzaCL34600jwDfWebDWi6C2DL9IDOr2sL8GRTkHFPdZP__QwrQ4Nkgpn69LpoWLu0btHOcSo1wyyLmgibfFi70HAE6mEnPWD8tL3wNAK0jzcORut_bo2KRWgQMR2M0gnn_CRO7cSvlJKCqq48ho24P04_ngLIjsGU4NLB0RK6pIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نشست فردای ایران، عمان و کشورهای عربی سر تنگه هرمز فعلا لغو شد</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/20862" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20861" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/igpapowvAlwj789KiR3dvLRHNbvOrqeDZHphtaQDpiHrzjQaTEGIXze4_MKW0Be2_ep9ZgEff0MFg9bRSnUKu20ycSK0NB9pvJdLzEkP89RSgLGq31kHG9wjMX7HNM4L6rZOU4nYKJDMAVry6CP8kiHmG3bs8Ouq7XTc02ezURFKRiuRhaH1HeLIWDSZj57KJwByhKNbfIYsAINj--NxbJJw1E_pg_8q3s63z4r-lCuAvEE6QeKc1sOh1Lukyr9UUBEt96ZA-j83WNOxRJuVSiuL3P0wDwxxjljTooBAOB6pxuJHabynPgLriJBHFgXjwqIGK9knqL2FVaDVDmRBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان
پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20860" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
