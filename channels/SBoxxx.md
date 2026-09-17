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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 01:20:28</div>
<hr>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
نیروهای مسلح ایران به آمریکا درسی خواهند داد که هرگز فراموش نخواهد کرد</div>
<div class="tg-footer">👁️ 550 · <a href="https://t.me/SBoxxx/20964" target="_blank">📅 01:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حمله ایران به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/20963" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک کشتی ترکیه‌ ساحل اوکراین توسط پهپاد مورد حمله قرار گرفت.
بر اساس اطلاعات اولیه، کاپیتان و یک ملوان کشتی در این حمله کشته شدند و ۱۳ نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/20962" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ساعتی قبل وزارت خارجه آمریکا قصد دولتش برای فروش ۴۸ فروند جنگنده F-35A به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را به کنگره این کشور اعلام کرد.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/20961" target="_blank">📅 21:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:   من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20960" target="_blank">📅 21:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:  طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/20959" target="_blank">📅 21:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این دیدگاه Secret Box هم تایید شد:
طبق اطلاعات افشا شده از منابع محلی، حدود ۵۰۰۰ تروریست یا جهادی که بیشتر آن‌ها از قوم اویغور و اهل آسیای مرکزی، از سوریه به یمن اعزام شده‌اند تا به عنوان مزدوران برای عربستان سعودی فعالیت کنند.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20958" target="_blank">📅 21:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20957" target="_blank">📅 21:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/20956" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:
تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است.
هر احتمالی از جانب من وجود دارد.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20955" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">— اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف، از جمله شرایط اضطراری بود.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/20954" target="_blank">📅 20:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
من آدمی فروتن و با سطح هوشی بسیار بالا هستم</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/20953" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#FairValueCurve  شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.  در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20952" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نخست‌وزیر اسرائیل، نتانیاهو، می‌گوید که اسرائیل رژیم ایران را سرنگون خواهد کرد.
«این رژیم سقوط خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20951" target="_blank">📅 16:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20950" target="_blank">📅 14:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk8De3DTT8CqIKw3zWX_hSpCBGjn5ow93Gzrq1x8rSsGwJ_ohEKSma1NP1KWg5GW8bJIZtZE1JzxzSo5NO85g_0vqmPcBzz0-rQRkqfFGlKSzrHMNfa60GpHRiXA6alkgLZEj9RtgcpmkEP1xi5ySd6reJLp0SJBlvSYvECoV2J84KnU_kFeetU2hPoRPtJkBwiGrY-_svLc8rFJitqepORWD8vH7oKOe9thGZ7a41sAmrLteuzbyJmhJm1Xk4bcVs_wVvOxaz62kGeUu_WDYhe3T84fs2rBNul_glLwtfIKVfw5XsR8-BefFIkokWjBDP3_y6YVthWrBHftnaD1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
شاخص FVC اکنون سقف بالاتری برای طلا پیش بینی می کند و لذا فضای رشد فراهم است.
در نتیجه انتظار برای یک اصلاح تا 4300 الی 4290 و سپس اقدام برای خرید برای امروز منطقی است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20949" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6heC1XzxYLQd8wt0-DC8_ZdZCE9nuO0uq_HdGF2aLRbg2BpovSJrNo78gFtxi7EyA8W6uwFnPGj9oW6gd7hRHCxR0-TUYadHMuu7Paz9krLzywYHv1CM6gJer3Hc269_0Z0HMdS6R2b9WSLyZAx1TpTtdPVu572WiHWb2tuj1-e5kUH_T3UkRQkHECrif4Eqt11bAXDPYNjCBWWxsCce71kCMUx5XWOv1qxGBnlpkLQTGX68R2_WDfmA3PYYzKW4TN9UCmd9Z5wMU0tVvhLlD2yaYrr7zwtaxki-hAxPfiVWbZgDsCohx7KdpfnTWztBk5Hs91jz-4w21rZybj3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و انتظار می رود یک اصلاح نزولی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20948" target="_blank">📅 11:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20947" target="_blank">📅 11:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCgdP5etzmnPZH8OtuDM9qw66dqkNcPXGNr_WYKuTOCU9Ovd6cFyCuVhBKA9CM-Leq1JDkjjhoDtgRQu9zCuEPwfXMfQgw59tw9EBDB2x4KG5Fo6m1WfJc6bqMkOAjTirmLK3OkarCmlsanS7drR5gpL4JP30kEtls88YbwXLjQQOy3435JoSxdMcytYMNxhqC8cqoNPNU10oCaEavgbBWmVi7E3AgLgMBhth0a07nR7FleVxOAazuCETbndRaAgIGN0xQYxiyTkBEwTm577dow-xhb1l6Gcni5cOXAaaw779CTkDBnSwO4SyB6Hrr9PHSC4PC4Pbgp7WMRKEYNLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین توییت برگ افکن دکتر قالیباف</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/20946" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شروع شد:  اخبار فوری: کاخ سفید افزایش نرخ بهره فدرال را «مایه تاسف» خواند</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20945" target="_blank">📅 00:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20944" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skDIrhpyivtWOPbPLeGZXweJ9Yzwcjq54Tw5aXAAHjbaHzdSqrQiAgQxCwGtblc3N6gHDCcYwGV41JvTQBvhhsaeA9QmRXz6fYDS2eqrOAVZiadcjrlqp3jlhdBZdJViUuWpmM7ZqGGsmPg21qAHMOLbjQiT5mVQygHZzt6khLMxHS0Avjkk2u88ewRNp-E03W3gpN_B41-Osq1iItXOHxvHIFkDjCdYkxoD7Mi1fsq3SWAqLPDvhI8jZ0BLWSKIEgvAAPeGCiSszF4PFkYJzASA0IGzJanTUHw5YDQiqZZ6ES8ft4jYq7N-jIpcjBMsU2FUraZg-qMDjW0a_q-S7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پوزیشن دیشب برای همراهان ما ارسال شده بود.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20943" target="_blank">📅 23:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20941" target="_blank">📅 23:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqQdTn3j12IGxDGlOnx18HwaYpGypPD_Mgrayu3TGCfx_B7GpcPbpu16FEWB8tczZxN_uC_MhHqNSXeoMO5cS3xqcjWM5ngHCsV78E0wW_1tvqIElKcyVJqj9dV-FbDHI7ruovd41X8xbHrbbcVuj4O5q4-F7e5ON9VMNva6t-z9LBQaFxbHdCR8vGeDv9gkfcoFDxAsrRUWLybeZKX8ztmSzZ0DChqiQ3lgwF6SGCXeBcs5HaIY214E1Ef0Ok0VZdQfQx2BWILOCbR7TUtkdeL1J78FH96RUp-B9Uwi2n8YAtq3YAa_Hw6HEs4R1QF3Z9g8kLsQVnQS29FkQuBmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20940" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قیمت : ۴۲۶۰</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20939" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خرید طلا یک پله توصیه می شود</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20938" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شبکه کان عبری:
مقامات عربستانی به نتانیاهو اعلام کرده‌اند که اگر اسرائیل جلوی پیروزی یمنی‌ها را بگیرد عربستان سریعا با اسرائیل روابط خود را به طور رسمی عادی‌سازی خواهد کرد/کویت نیز بعد از حملات ایران همین قصد را دارد/اردوغان نیز با محکوم کردن یمن پروازهای ایران به ترکیه را لغو کرده است</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20937" target="_blank">📅 22:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20936" target="_blank">📅 22:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به دلیل ورود حداد عادل به تبریز چندین فواره بزرگ توسط شهرداری تبریز پرتاب شده است، به دلیل اینکه فردا میلاد و هیچ جشنی نیست مردم تبریز فکر کرده‌اند پدافند فعال شده است.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20935" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUGL3G6ViftcbPu8fXcqb_8OpAp1A7E7X4R9dJOviwmOGlgyBOveEo9C3TsE3Kz9-9JsldGEokdPOZwUWvVWWikYNydxMynN_tJHF2IRslKFRTXIqKfhELZxS9s0wJok5_YkGsu_rFfoFi8kyt-BD3i1OsHCgUnyINailx96akc8Gq5VnN2eAY13A6AW-gUWm0UIxvVVw7TVlIQyNoNZDx9p8kYIs1s1Ek18kP678fMQYxMaBSDCOl8aXR921G-169X0QEvaMppp_OjevFzjqR6W24SiJUh0X8VRTk70G-MqzuJDHsqydtTjWtwvC9zU_b7sY0KwkHDM9RH1t1XCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20934" target="_blank">📅 22:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae6gv6Z_HvXB2MkVuQP8pOoCbfmggMiq8LyswKlSI7Gt4hVk7unKifeXTEN8jZ9j8wy5O1bBNF0XsfM6uer5j462DDtqtlufQELKH8B76AMEwBFE4T0rayaoNiat2lCuuMGQ_gNuUczFkXyYFWwonnfoAcFO3AcCAgHqmTB7s4ZAlV6VlsTov8w_CToNMgg8kpbQJfnrQN7SUaNFUi1EAI5X6nKjDESornJx8o67oPBv-t72vwwpEkwNhFXn6Mf7PARkokXeb8_dpB4_3qL2HZ0GHItGNcgQAPa9mXDdTcexuEZBsX9oKQTfedJToRRqb1CIwh8wY465w07aq3G2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20933" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo1qt9ax7AQdhWRSKN3dCVooUyvIUgjDJtfb_nOa-O512uxTiUElEZmlFRydlveOknYkbD1F-Npa0bWLIruL8l8b0Hb9-ooPkiPkUK78Mc2tYlrtOuI46Jrvu_4CJGdplJ00tAo2_2J-nKIjG999QYMHJIreRdxah-Q-6LzNWj_UASsrhBTaQAbTT3V_PStP1PIijoHZ5hfLTQ9y0J9w6iymHUuyloZ4NTLiNnuFr0Q4YM_Zbac4cvET5ohOLaY3A012fu1SJMQhapOjHHMsnpzPrRV5zSeydZ4FNqC0i7OVkyutcAuga9sROtCJXR-l-8JJ9S3AiAezUQ1DLZo7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20932" target="_blank">📅 20:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=ixanZKtbuv5LU_VWUHPCnyHCNTTPZdgRP-tPfbfhIu8f1phuXr9Jr2b9pwP78kC5FT7Ei-u6Qf1VqidJAvkE_oYPeG3sDURR9iUCUCmLoqjypuNK4u3HYWYXxtujbuO0L6xdpICDSTM_HhzscjhNMvT_Pgp9k7-5MFpedxEBYPWBTHPn_TBHkWTnt2XXB28lQ8yz2GXiD51p4K0FLgK09_kH2z71t4YadfsSezWI2Gs-fxN1Nh8FvzK-C5ZkZLjLKL7M7Yz6SD_p7bDzed3TKCeW2BPIaiLyQyJtVzeQztukSuf361RpmBQJg7AtYFnVcOa65FFSyt70Ub0DjqQy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=ixanZKtbuv5LU_VWUHPCnyHCNTTPZdgRP-tPfbfhIu8f1phuXr9Jr2b9pwP78kC5FT7Ei-u6Qf1VqidJAvkE_oYPeG3sDURR9iUCUCmLoqjypuNK4u3HYWYXxtujbuO0L6xdpICDSTM_HhzscjhNMvT_Pgp9k7-5MFpedxEBYPWBTHPn_TBHkWTnt2XXB28lQ8yz2GXiD51p4K0FLgK09_kH2z71t4YadfsSezWI2Gs-fxN1Nh8FvzK-C5ZkZLjLKL7M7Yz6SD_p7bDzed3TKCeW2BPIaiLyQyJtVzeQztukSuf361RpmBQJg7AtYFnVcOa65FFSyt70Ub0DjqQy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW6YDB7xAOmvQbGvGBjCAQQfZxRQiMTjD93N1ayuITnVFDH_NBPJQxSGISsXbPhV9a1JaMsdjCVwku7wWleEvrz6gxQmtneD1ziH4w5yd3GdH2J01g3WIUb5DP4hbax4tE0fD-sGR8o8M6j7koj7VbsPVnpaLRqBgCxa57r7vMDk3t8R3nnmC1PU_moVKqUDw1xtkZoF5jef7uI8FUIdqWUdukgbIB7Kw5u0DmeOCQb6Rh3Sc2EhCZsMzA3WUhImxYX6gRxzQZpVix9M72Xr2ZlS8dznQj7PBq9ajKnMVPk6c9tBmigt0J9A9XIUedLMEnznbXGne41B6YFWQ86Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGGPypFUKo5NYUfQIbJKY02nmgjdmDwUvrwNRy_1C2FymIchnZbbjMDYAelk_fBe0-Lg_BPvELg6gmht0jrdRFU4E_zBRLS1w7Jx1pSlw83AmiwU-aMoW19wJH-R0HJjhPbOSOZX9qtZYMRzJKofj7C_YCkhKxZlNHSZwy7I5MGtzpmaBlP0Vwom3wwTU8wEInHC_Oc0E5yzS4aPgKom1YHIOG5fv17Tc2LBQDMRk8i7rk1ZnX3_85R6J6FA5gtUgjR13yNQ_2Ul22jSM8iA5wgSKmTzfYxSpduYUJ38EkEvlUysey_PbUSyoUnXobvX-p9TQwIL7TFJf2u4qeQDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH15ExCkv6u5vgPVdgddVnd_oR1yOMW5ybsdFW9yEFI8zCEyjKvvXobcZK_PgjJ1Wn10hjl5VDeqRfpIO-BuIZ9ODc5_TTqUbf_QQKsaU-XH2sT05tIEEHUxOtHH_qzNsGO89Tr4yBEmjIY8MrV6uRyVVJ6RcL0tBsVBz2ctNDnlx37Napt1qNkNW4a3OzU7B-R0ytI6FGieWK5pgCnf93Ll3-8esKx4P_HUR2dW4dJHyrVOb30alHUCWDmos_PjS6GAnGqErbnYti8cbOXHD7QxTGwARscoTJbLJBLWP96_dkQwNLli0sR2oNWjhNlWlstGYsnmbQuOgGnIGys5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=gNAs8uUJ83Yz4qshoh9qHvgl2wAnuKiGJUd8xprqk_OrnrxcyNFzPwK3xugvzRnsT5HUmDsqNbTvQsne631h12qzT6UKJyxZI-uZVnBeAoR5EsYi8sOLkySDj4Bvrfuypz9R4BD8GQsnUV6o_slQ2lESyD1V1ZG9JW-iV64fitSK4Sp34qfj_LTizC8EW86labnJzHloD-DY5KeDWvZz95GZ8KHeDH7od7TqgK9wBlVsm8Q0XsB8gn1tgnZcmmq-9Z0MVHwtogsW4GmnQd3dZq4SVMcySgQpV6Ser0X459KZgWjDJP8ZczMwbZaidi8Aiy7EVNlkUAsFp7QuSsU0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=gNAs8uUJ83Yz4qshoh9qHvgl2wAnuKiGJUd8xprqk_OrnrxcyNFzPwK3xugvzRnsT5HUmDsqNbTvQsne631h12qzT6UKJyxZI-uZVnBeAoR5EsYi8sOLkySDj4Bvrfuypz9R4BD8GQsnUV6o_slQ2lESyD1V1ZG9JW-iV64fitSK4Sp34qfj_LTizC8EW86labnJzHloD-DY5KeDWvZz95GZ8KHeDH7od7TqgK9wBlVsm8Q0XsB8gn1tgnZcmmq-9Z0MVHwtogsW4GmnQd3dZq4SVMcySgQpV6Ser0X459KZgWjDJP8ZczMwbZaidi8Aiy7EVNlkUAsFp7QuSsU0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwxeOMTMmqrzrrDc0RpOfBCTYyFbvVHFA-JSDyNJlvDfTrmDaeZdAO4cMcgn25SzyaOf2NDStRi8ZHsXvad-v8Ma53W49I6QeFtfUsk6-QzwWSiGoQZsyh2F0n6DwJSGOwrx2GO8Ac7uSAbhOu1Mr7acjnqz__SbQc3VK0upZPLea8jJhWJZdi9Avl2-kR6c-s58Ck7GXkxT2COiOilD4GptHMDdNZ2pQunPVsS50y9EPQvj5SQDXXgu0kpAoTm2fCplomCDEZoyNl0DUABeRSv2mjsa1kIqj-I6JAZ6A0_OEG6MI96LSX9J9SqC-wGcHHQrBiln-Ffs_gVVxLklNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNx4C4Oa5JWy9oSRXZCTnNF6p5paUMu3g8k85-W5OlK2bUEhK3Uq_HYD5kt6SQm8OdXnGaAHNo62InpK13AR18WfNh66bAPrj1vMVK-V_l7sJhzA2-ZpGWNLELpBURxJbWYry4jhk8_KcboeEnQ7IQ597OflOEbK1ADISmgohmtJQ2uumSViKVv4JmE5o8273dTxsR-ttK-gXl2COUBnPH6Ct4h38mcYLvwxiD52E6GccDRxoztRZI0bOpZJNrZ35J5sbilunUTaG9Fd4D-NBQH3foJaB7SWWeq8rYaVkZFauRU0kRrSAgKNPbwvRj4ZH_4EM990CBvw9eLLGgY1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtsNO9msr5Nbh5pjnx1pwWAvgPQNGZl-iIknDJ3Q7Y3gta3QYvnn6hTii6tMYUnlZQ8c18fGgnJtfEcAvJCVM55GjN03JtWVjNn8f-poLzDhT3NAYL8cfLSrLU97eDb1DBNQFsPhv8ue81m5c66_LNMp9qGfhzD-Wchh4c2alLs_bL2ak40yWnqYdOQJ_Ii5cdqh_yoj-rnSfTqipaGox26STeqICem0sKfEBaY1loISnqkkUxZkVScoBh9oHUaCxmjvTDcoMZhljw6ovMZz3BtZ1Uqb4feyyTldDQzuYz0sYjflwZC-6y9f0SnfHuS-bd-krUVI4J5Ly5bnE8G98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnazHPkC-HdCwjZf7uV6tzsiRStS4mz6zoxusFCecPcNAP1R1gUa-CrDDIqPgZE-GYWiJs_ljFXWbceTRjPNp1TpCEw56WY4LW8-quh236td-ht1l-O1zWrwbOyp5a_Ek9uHYSN_hhY8KJcoZIMMb3rZzLZ9po_GNx39zFaq_yRWozj-evA9txjcTflRibKngVkKp6gt6Q6nR3OybbyAHgyoXLU4WdqW-C9-RAVKqkYuBJJ-5pr5UJku1iYDgZSSfHb8U9GN5YbX8Assyg8iD0ycFFELKfZ_RccbC9UFvQxJc3hsK-4aNi27rEh28pawTJOHq-tbR8bn7j5wqxqhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiyJJQAIpNGeuydp3qoy_WQFOeobYp-o0VVUfExrYcWKciBntrMMYrJCMY6EWBMnPuiQ8NYVVHogrjvO222jdr2YKsv2JAHqz_XdKPANmynMnnozkGygd8_6edv9GDoJ9DfENHflrgaXYKCvusPyDWhI1fFBPugrcqEbhkOC06FTXSVfzSan-1FnEtFuFjM86jK-u_gaKl1QTUy3iX0mllM5TKAiwj8V9y9zdwmukKfv52rriubZpTbA42fPRkggj4D4nFgEMoYFJNv14Ey26yfU4ZG3viv_YixZkMI1HMjvY8lf4ZuYTlNKqBsW_OlU4s1syQLeyGa6xS2Q98qgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYK4kJgkf3M32iJXIvprT9odMJDkAe0GRj9mSKtWcnJVmpeH-qpljHqqn2QLdho8RUQSkoUHmzmpYJzRXgvKS2qEXm6QocCseSUc3xMlGtATeMZaMzKaV8N_xmhEMLlnRanGBrbM2ggzkiOySc6BXgHq-DwgkmJk3EMZqIZLcTIaq5oaZSVc_lwoltlaseoLfmoeo5J1_Z17vcpO6V0Cphdm9mdWsNvd64MfLCz1Xf_YPQSLlWEbS91fBLhJVD-fR5SI9Hh2CLmLJNYMEMjb-n8OSYmWlBzmZOdXgscOoOtBZtFNuXCFzxoAEfmSf5L0HtxMQ--L7DAegUwsqWxk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkjiHwOK1TxpPJupEHTSDppjhRwEZDA4a8yFgqlnyv5gG4_EeT7gOQQl65ynP3U5rSjq_afcj-ZH_k-ErDD3oBkaILpIzjGcdshXDOS154LU_XYXBcYkQPclZ1QpXCNoFNJIqie5Ojmdf8IYs80mn_I4Cs9nExlz-rKjpctfbut8WDLHtkdldVgmWDWr2AzcST_4AL49uqDhwkkkgRalPp8KRvd4kqWN9Axn_XECzLfTjJ24wTZq77VozrBNX0AnItJ_gUpr78pF0htrjw3qYD0G5Ct4XtS_BTMiK_mZ1dP04xO4OiTh05fcsuXdf-wNvkk3JsplRutd6CDRZInBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIJOUqA1cwxtQYHci7wc6yx431GYc2CAr-AVrHUyveWTbZDBb-iLWZKcV4T-FUJCUXjEjLRjIlJ1Ci4ugGIAdJZr_8QDeygYUUvaRpeopgI_R2l7YJhjzJ1D6U_N7QVK0rXzX67zPCAoxxiuWUKz8NN7BmZJDAD6Q2bnxvLbKAnxi42DomL7AkHmB-DZsC0AsHAs2wf2HEzQ6rTneRdUek6anFDSExtPKM7SB_E9Htnf5SpA94uwdi7OBCrrbyrWk1evLzq5-CGW1AYoqih_rBt8zrugXGcimm1LPmY1UHnBXIpW3PtKYerylG2jUyFPbDpYVydnPwdixfGEGLH9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbmMPC0I7PAULXgu3DhKks3pXyTVnhmFozwXjFjvlcd9Blhcei5Y1ArOGNC2t6mz0hoaW3u7yCqAysPgo4SMQ5YY8Y60X7B7MBVcTO8O_5NpT6y8Y6Aue3aTFfjq4z-Fjg6EsYbGAC0uEHFY86ArOhG0A_vnhlRl4mcwmw5b16kuJESWYoUSbfZIo-CvN5ewbcH7rYLGK82PRmPVnywHh7u1pGKdE0wpQhxelsXaENQSQjQ5FnFJi0QbY8qkZM6jf-mfB90Bw4updYERH8l8x7ciCt2WRMMghdmSjsRB-HxfwQnfmspRYBvCfkHKnfJf7rKTgsxmd82qRTJz6ifgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHQUVsq1xQpjDKgk-8LukVVzv6rZ85Sj8sIJI2lcG2mwgBoYXtTXd5uly4Cj0uqyab2Kq7hd4wWz3K87-m223RlqAH2aMJqcKdLjMzIQ_WvTSp8ckiVTxNyroKooSAVBX-FZPe_XV_u_A1TTY1ZojiYnVXEInZDs0S_D-Ud-uzlqWtNhf_mS8GK9OKR52ak02k7HZfC2LUHyOEDZMd6Ag7QZ4K5_PF81cKqxGZRyA1aBZvjeXniu9BH4Oa628tK4Z1GUmyVCZEVOuZ9mZEwhCd_nxDqk_bbaTRNjKOWrKN4HID2MnOKRzOi92a2U1-gX7_OdWNyWmvWqgR8ai0gwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMxUD1IhPdWT3dJYmFWeu1QcFxDzjuQeyyc-LWHeYSTRrp0F6xckQlODtrfk01jZUNB2KKD7ufVV3_RMSXIdyGqfg-bG8ujrmncEGlH_eQMARGTF5HW66xfQ4A23EQmNdMFPC9lnO4elW0vZlVTcDLFrYx8kT-Xo71W6QEqBn9ySphICGPrGzXLDMRrPzvzvvB2kfy23fsAuXdVzXa8CcCU-HNO4RMN-ano5S5efT-gCc5LTeKOk211zVVZXTWErW4WVurAI9JoCAcIdUkjAX6TOlMhCtqeTfGDTkSY3XWaVTFrL1ELSjvGayxYoos1gtsHdnfCqxCNv2WBf1uRhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiKbJ0laIAMq0iKtQX-YnHoPPQCwYGkFb1mBv1j5vjTP0aimSbwlqTAYWJm-Kh3Ptuo6mXrqgzHVXbyGMxKpuiydIbc6Vs36h-rD68RKAGwJIhBvFxN7SuBq3ZCsAJujvty7ripR4fKJn6kPU2RS2mdafiYVHKvm7x-SJGQevLN8m-kFsmx8gzc2gZNYJmbltLWZlzSsY5AcSvgMkTW5Qgyc-1xPzoiRN6cSURyNDW6WHWZ8o32gzZbb0W86amp86k6gwRj4NC9nlGOVLML3F7cChNDwcoA9rFS0Os7aBqGA-Qg-MS55ithKv622vRVr4N4iJ6OON5v6k-wZykI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIXM7K1kPRyktbVzSbgRfbPyRx-L9uZaBLYt2TwAxJnqgKlEkAJiQN08xx3P406nHlEbhzAK5px1e5uX64hUB9OYdikpdcnDMH_nMGyIWGgQUrPCSuGj_PkHBmmNMhNbH2zDeLOMBORkHp44w_u96hAPm4iEajrkfDvG9nGLFOhU5o-r21EMikqSYzb9_mg6blyy4aLM82bN94rgaxXkgjPfHBJ-CSsE67VMdMqX24g5MPPdX7_TGyYNhl-08Zwlatux9LnN7ojc0Mi0R0WS_BpFDFNR1iAJjW3JeZOm3JO4mgdfsscaLjBfjokkh8Tju4QWVEcm_MlubhWHHoHTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX3PUXj5EhMuX9FXyMBnQWU7cQjfyuYLVscaquR10X2ARLUDuN9cjxHmbV5WAIQjJridzmTfF6N8PgR-ewt5iRW6kT1Hh4V7zDW_Ltt45tx604aei5WEAMfdFf1kXpNWKpFfE7MuZtBEdeAhqFRGGF5t0UAMMGEPWejSirtq9Ju61y85dz4MLKiBoXenNW1GmJF2iKlCt9U1svlPJHgZr9St_Evqi3XQw3wtT1-mSEtzqT7GhtV_TpvkyCNZcaA7QONz8eUEYQSjTfQubDQIaF8WblskGxzHAhI1GTp9gza3Bov-2AWDd55Qvr2fk4FEB53i3VqbIZp95X40rOlEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw7lztL5l78pJAbWBrBmYpDXyEdcW2R3PHutGKQ9HXsR98EHvlXHI7v6hIzbgZNYEIbLnVD3RuJjc1ZseC9LLebrxhyiFIY6c5XKwFc3BA5-nmPaLkfax4PCGUDHXckbijgfMOp9ty5abcZQmHhTHzI6e8wTTR58VbHyTsqqBs4Uu_zWaJBgWlo9cqkYS91n6isGkPxQC-zJ8jFlmnXqn6-bvBjTmeZ-f98cx73ZxYU2w4fVRiDoKjYO-FlL4ARSDhyVkDXRWHJYkHTwZXGQrgpcQP4DhForBfZ9VwipdtJ38gEshGsYSI4jhrWK4ZfXU4JuyBCd1jw8PwC1yMZidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN0g2rHcAF-N9f5BdMci-kQm8qkOQUS9a2ThCMkt6qS2tEe4sjcZiQyBOr3jWosm2vhROJRXEfpCV5ifB8RIIBV8t1VVJ9bfUC7IB2w4s_CLFsPsNdBeAkRmSoJh1z5xJnPief8OuWEb0nFv-KgNPsVDu8MwCTBzmYvWe4wUEyvar2WHR14GHtgsgDomkV880G_ZjkLUzd5s3DGWTSk2iHcj8L9Z4_OUTmWnE1sENZBpnzxkqBn84wCDQXXe3EDXinufeawVH2fX6P9OKsSLdm-A4Y8PqVRmnb1DS4IU0KxQ_QJGRnK-j92CHsUUEO8DiQ624l5BG3kpguaIEGRvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cki5dGL_MIAAXROjr7RH73aLyWdbcbLkQXpsK9ytKAwdv_L2dziYmdkotksG3zWZfCTTKByi8v1qZuiPI7m7VSAjmjgqdJlnu6tKW-v7VrDrk8OYOPOLuDWDqT43AbyS6nMpuYnWWwlfeLB92ZiUZpvEqjmJNm8LfBqQDCO24e-uu5XRTIIj16YKwlxjoYAauP77BelysfrF3L0WmpNVvFZpr7Y9z_OQ1SChwU4doYpZhVOQOeTL9FfSvlLf2aTPJPgcdclkfth3lOXxqoBswHF6sRpbjwPyVOfearclff0fvRPoK13bZqaGXt92xs3rBEdPefTkIYd9W-qlXSTIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpLDjWymQjucnvfvIuqq7OGLxZjF6YaFpBp-B3zKCabee3xORO0bG287gLuhvU6Y33tK1C17dnomqT5lm1ehVL82aAo1i7LlLnWCwfPkzslUVyW9RzbCtWbWBz8SY3h7EY4D0JTpis7gXQUtqjyUB4CFXGqWJEfzLlvSTLdG2usCdqZqln-rVl8PDIds5QYuj8riHYEWJy8k7aPP4-LFjX1Pmios-MFD3sPczoZ459fRBtgImIkzg1w6qgB4wSziyrCLX_TsRPmrvHbozhCuYkKE9x5dpyauT51LhzDdbMBL_9V_XLNRPU5R_pL1_8eB-VETbC7DHy36Yuz2dazB7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9bTbHBWPHPJzv6Ml9jnWeiZOl3--hVp7aqzqhDymlCtfDCe28OUIo03YLjGkLkz4ykig06Vd5FxZFHoFmYJEeEzE21riewcPpCFfhUW_0z6vZJL2sdk5XUSseX1phMFwN79gIsbmKrPRMmgjWHT_lv5ddm0F6n4vQ7-rYOx6T8Ia_Bb55_XQjZv3V90uqTuPg4vIxwRxius8FvlMjzUXnzHoWK_U4g9v3sKcUZzQA3yVkznntSfBnG-63gONnqZNi06UC0I62EhB8LqYdGfhshXyWOaM8c6AoyrRhlmfuIlF0wIKNG1qi9i_BCQ89YkmM4P_sYS15r6QGCfXWFLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4KRYPh3-vhbJI6IIIa6ffV0m_5eafiuHXkevp7vWWytAkp3mY0aRtfctvwb74tuONDPxLiDRpgAAHZ9zWq_WQn1Huyvw24n9mkJTZOfEVA0ikehY_gh443gPSz_UD8QB1QGK7KZ7BUXGRv3zZMbB9WadjX85HULJgF5DwoS_GIghO7xwoKjE_KkY_cFUTylzo9WXujTCvgw9yGVKiY3-cA-d7XKGEeJFztUjXvsX65-3pfKfGkY0CJegjX2adN5HypNSTVs6h0X9slObX1llbgNgOm3m8gnXihiOJFIlZ4v7a9cBe7krT8P1EYlhTbfJN6sB_bpbdNeWLnN3nIkow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyFAdVgBqZDcEFJazR6QghdLpGGMZoXMJ3LGKei6zjdFpmekvoRm-cyb6IxBlLrouTprwHNT-b58XZKCSLQwzb4RZKs_a4eXhUTkS4Ez1ldIHi9jm7vkB9xmlYhIY_3UYIlJKdAV-V9lvEykWEtF828zh2ENHEyjy7Lvt_3oD2HgyEQ73EdrtfjZ1OrB1qouiw8lZFIlNYkK86Ek49NuqKaDXbrQfcvnJP_IwyUJ-RJSiGOQjlQU89CDIMR63IC7qzeuBr06RZrPWOe2JSiliwnhGcyzCHvTTjSelLdXMpdKHVLbkhIIk6Km_Cn0TwqjMkCoOc5C3qB5ecCPAbfS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
