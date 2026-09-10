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
<img src="https://cdn4.telesco.pe/file/JxPHwy362BZWIgAiddq2S0RySJEA5nN6a2o1mX6U6YHLWt9gCLa9EUGv4Rj7Vh53vsjcvQ-pUONhGERULCAJAzsg3BYkLiXq4ujU_MqaqfKsbmpTDDz1SVUfCMT8t9eucUF1cLKaEKu9qZoeIjZ9lQY-I-3AHINzgmjUM1LuTs1OgamxDV0iAcCkljGjPXMsqcINB5m22HGibb84KkhX4s6gbJo6u3gUmxvturY4KnzDpJrDuXE1CrqR03i8NKuSGAF0wKkL7TLZ1fWwdDXrgl6C2wlp0AEtl_E6ZJ_6azkHeG3RF47g8iomLrcuG-5p9FXClqhtigqj4nTrUbGFRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 04:45:16</div>
<hr>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9UC5jsccZ8pZWfu97pldEjpvUxXXENLbNVG6A6iSatjhsPpgO5Z-rCLoOm3439t_kgtBrVTz89-sbxv7SUTjcCOBh3bAHcyxwNsDqTYe5jJWwnjjBzd6bBrV9GIkV-5r6OU21aYwp-HLivrpLo1PQhYisxIsrJ8R844W3JGSczRmRhe8Y31R_HwV__RCQiDUvHq2L7xfrwLPu5DTAxuV10lutml4e-BZ_trxUf2waNUY7MmroUbuTwm1u4X8adXt9c6jOu8Y5pi5MLVchLMxJftCs_-GKLhOUpMBMFPhD-lJJu5NDJYy1JNJjiSm-CmzlOCJ0YnamOX4YaP8aMJHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SBoxxx/20753" target="_blank">📅 01:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دو انفجار در طائف عربستان</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SBoxxx/20752" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4rq9uFk2zfOoDmvgVjaz88pYEdi4kmzaZT5JfFEvZAgMo8qOLSuYC58Bk333abtxSZjiCbrYxR4hMH2jzeI_D3CXZhcguJZRjae3y3IkrSXLvSTdvjdkrPEmPg01p_DM4Y9cYxbfXN_E5gCIx99GL7N3dinZAIaB9CP7IJKoi6z2fTFO9zXam3hdbi_VCJve8Raw_V5R2ulUojOnjG9ilAUKzS34GC_fzy5YsEtNGGXGkHt4FnCUH-eqBYQysEOjdMIpKdq2MnS1DqO6QN212PRDPWj92Pub-yldNLJmIPmZjgJ4OTfSzAUBKoGx72E71OqXNZPRvPcYmdHGzk65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک؟!</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/20751" target="_blank">📅 01:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پست ترامپ در
تروث‌سوشال
:
این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SBoxxx/20750" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برخی منابع عربی از پرتاب موشک به سوی تنگه هرمز خبر می دهند</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/20749" target="_blank">📅 01:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SBoxxx/20748" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">لینک ویدیوی ضبط شد
ه نشست امروز با نیما</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/20747" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E95MKit6WxcdPnk7A1S_QmlVbpVYRUvWri6Q5d0y716zDAKuiXwYvknyHEHF9HM2zovXFkRCebAHkOgu6YKsTIRfbBTPo8oq9_oSad0bDczJvo345vW9LLPkhRqLfqFaQSXONfGGn3-UNMpHyu6NOIZpf9PNn7mUrz74SEJtKNedgNvNXqZ-NGihn1X3KrPPbKVnCPN5WBAqL-Lm4nwMlUJlo6Ds2cCiQns4V4Tb6WGvQg1yvoljPWW6fwJlnOY5qVnzGAwbFY6_bl484HGyW112Qj_lHgHHpimUP4i5aeQVO2gdeb_WogtvYxvER3X_OBSQpP4ptmZQn7sbuezOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/20746" target="_blank">📅 01:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SBoxxx/20745" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SBoxxx/20744" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجار در بندرعباس و سیریک</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/20741" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/20740" target="_blank">📅 23:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktk4ioSEZyM1vD_dSpO3oztyS1GF9LoAcA_CCWzGV33mNx-_Ut2pu2eRI6St55oFKrLpgpQjJlhKeIpCBa1BjRq9DVao2-3yB-qGAXju0U1V4riKxZwQhqpXxIFuWqkbghbwYunKz91DguclU5pWdscqgavlk_14leWf_my5OUvc7dCa09IZOOM3Qjs7pQIxIeWBPSDimKZkgjuHMbL22Db0SJ4PbwOBIx6lXbUZWz6c03ey2pxWKhdI5X6vAvdvR45wZu39PGdMdgOaAp5rh1CbKxwCjVms5eosNLNLboYLD6yw4Cli5DIQIAxdR7Mufhcqi5btqc0zbbNtoWUw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/20739" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
باز هم به ایران حمله خواهیم کرد؛ مذاکراتی در کار نیست و جنگ علیه ایران بعد از انتخابات پایان خواهد یافت</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20738" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigiato | دیجیاتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHMwrWx_51iuKlBU2z_TRqPaBGTWkXl_ZXGTh0ODc7g-vZQDktoi10kqGKWK1GRO3l__OnvAzMejVrjsaGqQr7JeO7FYwDpUUWcAWq62aPiBJhDZUR4oiHweT8UWqEYGTMZ9WDoR1oV6fGpL9z8Q3-CM7m5_vClLCteGKEoXsbHAPRCJH2EFiAztRRh9fP3VBg8QVGfiAqpcHvsrw2P8xgNHnlsf9SNClpxpJVMSndL4Yb-PLilFpuo4Ag8SkKFjLm_zKpvgJl0vYWK-ydz_fXRHRTSgAg42tCxdIb4KH-QZQFaY5K5tWfh2XJMjGlCj4_kDvltQM4ZhdlcVBalO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
مریم عظیمی، مهندس ایرانی اپل دوربین iPhone 18 Pro را معرفی کرد
یک ایرانی در قلب توسعه دوربین آیفون؛ مریم عظیمی، دانشمند الگوریتم‌های زیبایی‌شناسی دوربین (Camera Aesthetics Algorithms Scientist) در اپل، در مراسم معرفی iPhone 18 Pro درباره فناوری‌های جدید دوربین این گوشی توضیح داد.
عظیمی که در تیم دوربین اپل روی الگوریتم‌های پردازش تصویر و بهبود کیفیت عکس و ویدیو کار می‌کند، درباره قابلیت‌های جدید سیستم دوربین iPhone 18 Pro صحبت کرد؛ دوربینی که حالا با دیافراگم متغیر، کنترل بیشتری روی نور و عمق میدان در اختیار کاربران قرار می‌دهد.
حضور یک مهندس ایرانی در یکی از بزرگ‌ترین مراسم‌های معرفی فناوری دنیا، بار دیگر نشان می‌دهد پشت محصولات محبوبی مثل آیفون، تیمی از مهندسان و پژوهشگران از سراسر جهان فعالیت می‌کنند.
#AppleEvent
🔵
@Digiato</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/20737" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بیانیه ایران، روسیه و چین در نشست شورای حکام: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد   راه‌حل پایدار برای وضعیت کنونی تنها از طریق توقف فوری و دائمی تمامی حملات و رفع تهدید به تجاوز بیشتر حاصل می‌شود   همه پرسش‌های مشروع درباره برنامه…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20736" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20735" target="_blank">📅 21:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/20734" target="_blank">📅 20:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20733" target="_blank">📅 20:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تغییر موازنه در یمن؟!
(این مقاله ترجمه یک یادداشت در یک سایت ترکی است و لزوماً همه موارد مطرح شده در آن مورد تایید من نیست)
جنگ یمن در سال ۲۰۲۶ وارد مرحله‌ای تعیین‌کننده شده است و ائتلاف ضدحوثی به رهبری عربستان سعودی پس از سال‌ها بن‌بست، بار دیگر ابتکار عمل را به دست گرفته است. نقطه عطف این تحول، توافق دفاعی مشترک مکه در ۷ اوت ۲۰۲۶ بود؛ پیمانی در سبک ناتو میان عربستان سعودی، ترکیه و پاکستان که همزمان با شکل‌گیری یک ائتلاف دفاع دریایی ۱۴ کشوری برای مقابله با تهدیدهای حوثی‌ها در دریای سرخ همراه شد.
این ائتلاف توانسته است نیروهای پراکنده و چندپاره ضدحوثی در یمن را تا حدی متحد کند و زمینه را برای عملیات‌های هماهنگ در تعز، الجوف و حضرموت فراهم آورد؛ مناطقی که نیروهای دولتی توانسته‌اند در آنها بخشی از سرزمین‌های تحت کنترل گروه مورد حمایت ایران را بازپس بگیرند.
نقش محوری پهپادهای ترکیه
یکی از عوامل اصلی این تغییر موازنه، توانمندی ترکیه در جنگ پهپادی است. پهپاد بیرقدار آکینجی، پیشرفته‌ترین پهپاد رزمی ترکیه، به‌صورت عملیاتی در یمن به کار گرفته شده و سرنگونی یک فروند از آن بر فراز استان الجوف در ژوئیه ۲۰۲۶ تأیید شده است. این تحول پس از انعقاد یک قرارداد دفاعی گسترده میان آنکارا و ریاض رخ داده که شامل انتقال فناوری و توافق‌های مربوط به تولید مشترک نیز می‌شود.
توافق مکه به‌طور مشخص همکاری در حوزه‌های پهپاد، جنگ الکترونیک و هوش مصنوعی را دربر می‌گیرد و به عربستان سعودی اجازه می‌دهد از سامانه‌های پیشرفته دفاعی و فناوری‌های عمیق ترکیه برای مقابله با حملات موشکی و پهپادی حوثی‌ها استفاده کند. اپراتورهای سعودی که آموزش آنها از اکتبر ۲۰۲۵ در ترکیه آغاز شده بود، اکنون از عملیات‌های تحت رهبری عربستان پشتیبانی می‌کنند. این مسئله نشان‌دهنده یک ارتقای راهبردی در توانایی ائتلاف برای انجام حملات دقیق است.
تأثیر فوری بر حوثی‌ها
تأثیر این تغییر بر حوثی‌ها فوری و شدید بوده است. پیش از این، مزیت نامتقارن این گروه ــ یعنی توانایی انجام حملات موشکی و پهپادی دوربرد ــ به حوثی‌ها اجازه می‌داد زیرساخت‌های نفتی عربستان، کشتیرانی در دریای سرخ و حتی اهدافی در خاک اسرائیل را با آزادی عمل قابل‌توجهی هدف قرار دهند. اما ورود پهپادهای آکینجی و سامانه‌های پیشرفته مقابله با پهپادها موجب کاهش آزادی عملیاتی حوثی‌ها شده است.
پدافند هوایی عربستان، که با فناوری ترکیه تقویت شده، توانسته است چندین پهپاد و موشک حوثی را در میانه مسیر رهگیری کند. همزمان، حملات هوایی ائتلاف، مواضع و سایت‌های پرتاب موشک حوثی‌ها را در صنعا و حدیده هدف قرار داده و منهدم کرده است. محاصره دریایی حوثی‌ها که در ۲۰ ژوئیه ۲۰۲۶ اعلام شد، و همچنین حملات آنها به تأسیسات آرامکوی عربستان در جیزان و ینبع، واکنش بی‌سابقه ریاض را به دنبال داشته است؛ از جمله حملات هوایی علیه مواضع نظامی حوثی‌ها و تعهد عربستان به استفاده از «نیرویی بی‌سابقه» در صورت تداوم تجاوزات.
حمایت گسترده‌تر دفاعی ترکیه از عربستان
نقش ترکیه تنها به پهپادها محدود نمی‌شود. حمایت دفاعی گسترده‌تر آنکارا نیز موقعیت عربستان را تقویت کرده است.
توافق مکه امکان اشتراک‌گذاری اطلاعات، ایجاد سامانه‌های هشدار زودهنگام و نظارت دریایی را فراهم می‌کند و در نتیجه توانایی حوثی‌ها برای گسترش قدرت خود فراتر از مرزهای یمن کاهش می‌یابد. اگرچه اعزام مستقیم نیروهای نظامی ترکیه به یمن همچنان بعید است، اما صنایع دفاعی ترکیه و شرکت‌های نظامی خصوصی مانند SADAT پشتیبانی لجستیکی و فنی در اختیار ائتلاف قرار داده‌اند که اثربخشی آن را افزایش می‌دهد. گزارش‌هایی نیز درباره انتقال تجهیزات نظامی ترکیه به یمن از طریق سومالی منتشر شده که می‌تواند نشان‌دهنده حمایت غیرمستقیم اما حیاتی آنکارا از نیروهای مورد حمایت عربستان باشد.
تضعیف موقعیت حوثی‌ها
اثر تجمعی این تحولات، تضعیف موقعیت نظامی حوثی‌ها است. این گروه اکنون با برتری هوایی، جنگ پهپادی پیشرفته‌تر و نیروهای زمینی متحدتر روبه‌روست و توانایی آن برای حفظ عملیات‌های گسترده در حال کاهش است.
شکست احتمالی حوثی‌ها می‌تواند ضربه سنگینی به «محور مقاومت» ایران وارد کند؛ زیرا تهران در این صورت مؤثرترین نیروی نیابتی خود در شبه‌جزیره عربستان را از دست خواهد داد. چنین تحولی می‌تواند توازن قدرت در خاورمیانه را به نفع بلوک سنی به رهبری عربستان سعودی تغییر دهد.
در شرایط کنونی، به نظر می‌رسد برتری فناوری و انسجام راهبردی ائتلاف ضدحوثی در حال تبدیل شدن به عوامل تعیین‌کننده‌ای هستند که می‌توانند روند جنگ طولانی یمن را تغییر دهند.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/20732" target="_blank">📅 19:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/20731" target="_blank">📅 19:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9t6uo92D0s3sI43pzm8Kljv79Ftgl6a6gJ7WxjklN4wrw6oCLS79c2MEkrJPMNPJ-Qw7YMFjt16Vr-8cqcYZ_R8WUJWxRn-OaqrWJI4dyWApDJ9Y0oykdiE_DsKFRG0u7rfWPAM2zQG6aEC8qjOXu9i7Vl-cd080L-yVSXZzR8PU9AU_rf7MLpfP858HUlW6SOlcZh3c3kE_R3ejdM3e7edz3bWAzNW_gihW5IcB9J19V4xgLGCleIKO0zuF7BP8ChV_8lp-y-yEpCcA1z9EZpZ6c-9Rp2JArUO8vIJ3RGtV0bpySvmBYyvNNRywWkBFQGuYR5tGgX2DdQlZX6gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9z50aCVyHpdhZ11JOp4IcPGe9tQUE5DRttFFGObHR0lIfalzpZwcb4WiWYavpTwfVVXfu5jloK1u7XrP8vD7c2QCVCWsJ_yUJzHCf4qqAtCoMrQ80ZRqyMSyX0g5nQSZKzyY-22kl9gn4l9t_U9Lq0oKQ2XA5IlRtIW0RZ1Rm1ieffa1DlQQDQ9pB1emBectcjtFSbHUXet5gJSJYuZOEwQO40xVcCxBd4_W1jsUS8togrX-yMU8cfiFdP4npyBW8mzxqDGjWe9ATbcTu8J3zs3ZUQ2gIdvYr_kotm97dfv9xIpXtL-dQceM4_gHkGV5r0Ja94493yxuxWjkz1ymA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20729" target="_blank">📅 19:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/20728" target="_blank">📅 19:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/20727" target="_blank">📅 19:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20726" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک روزنامه ترکی:
عربستان سعودی از پاکستان خواسته است که در عملیات نظامی علیه انصارالله شرکت کند و مداخله نماید.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20725" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfgC5ixupAZ07YXURuwljtnKI8EuqwZglBkfetXsnIBP-LImorfj8CNcsxDu14CQmWqfSmRZxWylzSnvv-ZLNEWGRNL8opzeXgUDWadZI4ioq79M9KFX44nxYG_KrA4sPN5PQ3qZ1wX9Zim-A6qArSEarrRqWr9p2VgNW-P7dG1GXu3Rgh86gnlNPck4OY5hlAAa0ctUz-9mxABWGwu6hFuTlqqBqg6CARzwI_U9FBR3-G_-dKUtu9jkyoABYq7b4QR2fHdgg0zOXzHZY2eI73S-TYo2GtQV9Ohsswh1muH79cOSHjHtYo4QEqoWs9L3Y-1HOH3g_rKlK_BcI8sf_qcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfgC5ixupAZ07YXURuwljtnKI8EuqwZglBkfetXsnIBP-LImorfj8CNcsxDu14CQmWqfSmRZxWylzSnvv-ZLNEWGRNL8opzeXgUDWadZI4ioq79M9KFX44nxYG_KrA4sPN5PQ3qZ1wX9Zim-A6qArSEarrRqWr9p2VgNW-P7dG1GXu3Rgh86gnlNPck4OY5hlAAa0ctUz-9mxABWGwu6hFuTlqqBqg6CARzwI_U9FBR3-G_-dKUtu9jkyoABYq7b4QR2fHdgg0zOXzHZY2eI73S-TYo2GtQV9Ohsswh1muH79cOSHjHtYo4QEqoWs9L3Y-1HOH3g_rKlK_BcI8sf_qcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکایی ها عموما از اوضاع جهان بی اطلاع هستند و خصوصا سیاه پوست هایشان که رسما توی دیوارند!
اینجا این منگل در پاسخ به این که چرا به ایران حمله کردیم می‌گوید چون ایران داشت نفت ما را از زمین میدزدید!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20724" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منابع محلی:
بیش از ۱۵ تروریست هیئت تحریر الشام (HTS) در پی انفجار انبار مهمات در حومه شمالی ادلب کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20723" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خر تو خر در یمن!
نیروهای ائتلاف جنوب مورد حمایت امارات امروز سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20722" target="_blank">📅 17:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0e7HeRAEhDSJFq5WQAtroo-g5DEIFa9ezVKMpXBBUy_fWp3Ra3Bjompe6s0lWyHPJu_t8gnTYV9zBWq2aKZhmeFrQ6d8ksSKdcZ-xeiDL5bIlWwFfIIgoWDZQOz211hIR4mlyKR7acBkvnkuzklbi4S1I6eXWMENWUqa2L-FBfTBJaYx-y9NWKBJKl96WwpqgVivrr_YaQUYa3OfGcxaQtlIyHv6_RaQjkI6zdO5ZSQWj-JYjY2Ib9MvGc2sfJDTQMsGvdP6aS8Acl7ytH-4kVz_9Vf8xTYx70PzwENtZONnSMya54F9Mlmc1C3laVpPtguOkKgO8jcg71s_r5mcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoOQT375zfRrhT6YU4gDCIDTqvlENgxazX52UMXC_xSRZE8Q-SMuIjqEC9u3yemJD4m1uGwoiwyC1JqPtdvHBZd9cOVqwugm8VM3Gpszp7o1kV4_rhLwX3lwH2GRdPHd7H5NvXIpn1BsW-03ia7Lr0xOfr_hmbX6EeQM4ZG230DmzcAypJv5fyqvoJ9OaV0PGsj_Js37naxy7qfS5W1xorHRPADjc-YFWozkEa9dUqqzqilElteg0z8hcXPV3lOSuB9CzdH9x7y3M16ssGNd38_NrO57SFl6kR2m3jp7o6cy2cM6wUwcVE_vkj4JT6NC8m5meHr7vvDY4ZvtzyYBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alWXy6HErgWsscX0RIUoQjtWUhraZWm6_ZodJ74GX8Q5lB6DtrZG42cOwHLuzZ2NIjmMGHUcjzaVA7U531wQSHraiEHGwQbdZ5vt9HyY7dniJNe6OhORT8w9OYfugefCzpadD8tce3HuICQI7Ou_3qvjnXD7SuQMJgZUewUw-ozMftzHmt5bwKnP7f-Rhg9eqaYk-s85YwsuXhwHd5FuVJnm3-U0RIMxqyl870vYi2PHqmd8U1oZBhjI7WjgNnDGmd9w_Pt20hI2MyFiMoPyUlfcq5bEK4gquAwjMSiUGdyV_Eqr2-Gp9jGknPYBbJxPCirJapFbC815wJkIfYuifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewOAXSexuf4UUh-P9dPg7rdp9k07Om3GVbmXmqJzKmgZg-cJVU9rS_F4BX9S-JVYdNHAQtc7gd4HeAidDTjyhgwG4i8SAtyqE7m4ZcfRK--I9Q0murxoGG9BO0MXvy3Vy2Sm-YeNNjb-lL8nwbbTcalAc5OOvA99gVJyXfFZ5PMMYMAMfyQyJGNI6f1mQXOKEsRoHNkQWUwQPvPTTB7iZg1zrzzUWbvi1TpOluBN_pS9kt2I3ZPvERZvYTMGDjWwb_xN0PxMCtyCOvlmsIscC6pHXf20Qq8GD4TZ9jb_03MINsSXtzRDA6YTEeVCu5QYrJ9VwdPwN9OtxxuQcQtFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9tT2ntY3VhdLC5RaOeDSvxluWGEUD_2MLccOZhrCQKxo4iD_3rUiMr7YbyKh5AUiUUR6QmoZKSulqOr5DlHWp1QRo4MinnD0MX0u7PN5p_NbEUfI7J6HIdN13scJJbj1yE-b8dzu6KqG2zSIu-wjII7eOB5763xQ0IL0-vbXk3CXBTyZiBH7s_otQCG_GlntKIc_MNPd5HLNx5dmGRLCXaxDuDSnQfzqswJEE7iPz9ugrfupTxk1BEbdpzOyMUmic7Y4r9TUCs7BPybNxMYOrLFMiCRQpC7VXv9oN-NxC75NOvsV9mYYjwp_or_EFHToxXSolQRk3-KRCfTkVfcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDiZDs45EL0rwEcJDhStt6a0zLltzPF9gm_iEn6Dp8zr-Kx8JBRQJGvT811ARU_BaJCC6vOhymkyGpO2l2FMnlLscW3bMBGbC6yVbyP8yGztVOdNN1hjTCuHqt8skO42wIxWw_jYM1yrWo6sZbcCdgcfB5aARhqtAGlDXv_jwvHHQEBh1eJ24gtWPkHexOzvskL3gcO9siywAXmCKUAUk0iFWMBWpYO3j-Obl_9tu2hIyBG5NE4L5ZHsrBWWSXCwgHdX9tC8W4SuRFIPIgvcjnxsBOwGuYM_C3O53CLfIaGMVgUBysyhTM_Nah_ml2qlyZaEhuRMigrKWMBhQ2x3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh47I7xQv6RFubpDxfA0azzfCYO_bR8tV-YVopbSFovzXrkqF2Bm7ayHKN3TiTGk6SqKvumI5K2BJ3OuOFsZMVhB7DPgP3jyi0ZkMQQ_-5y6qSpfs_0MUvzAXQ7ZuxqnjO12Z1uZt8Ylr7mpbf-C6CxYYRX9-CS6L188ViW1XIUNFY87TlRjzA6rNAtpohiRhJ9DPw3a3m6pifGaqrADxy2kbyS2yp8CZorELRaEBJAAdkgq_vt_36EQ61mDiN-d8c18V1nB-0zluGhnilGzEJKoMBV7O9dRsEvaUsquhVzurikPRoloqurpAn5GEB-7aydKWw7KQ_AFK6tTQ8KsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPsCF5mB6-LNtH-QWjvWGG6mCTHozyR8fsvAH9RR-e-6AhLY-Ebk0g5mobWsp_RFL-1hV85AL0pYoV1V-RQmUgL56HvVSXwEXwMrPDeEzCQ8hrWC6Rk5CDqdLGR7e5lQ4LriWgcP5Ud5sfFSnhNebWmyfuSBkGPCthZmSwqKaoXdfKD-FXJkr4ED3QbTdIbDPqnIvgYLM_YNJAKbeaOmdlWnzIYphOrjw5KAUXSzrh6pNgcYRXfBV1bFeUj9zux3YAd_jkLrQ-fwTXjpdJ03grXRwWloEviOOV0Z0r_Wp5xxfqPL8Kf6yCGK9STs1n9r78v7NdvCB6fiSo-mbbIIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrbbsF93rxFVsuLH0y_KP08Z1iO5kfYJRiqtIHtfeC3SmY4It0JC6w7ccJb2DXjUJjgiv1G00uIk4W8erzNgwiaIajRqRED6uDliGFek4UGrUo7zYFffMBs0XOQbwnqiO1wdG8c3ueqDn_NcDzQIDNDqHzlBYPrageOgQ7Qa2U7wHjl9m0VvidZKJip9yAgpy9CJGrLjIFesMtMGfQO5k94L5jnAXCWBpc-5e33QpbtfKlPX0xtr0GBMgcCWtFELMMi2MsG2g0V0Y2VEehrvnG6KxhRZ-nuuAb9hIWsWeW6JJMjN0CPI0Ckmhuxu6pM-b_UedNtS2_JtlcTDLjD2lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در دره پنجشیر، یک تنه در برابر ارتش سرخ شوروی ایستاد، آنگاه که کل افغانستان زیر سیطره رژیم کمونیستی کابل درآمده بود. در میانه جنگ‌های داخلی، کوشید که ثبات بر این کشور گسیخته‌از‌هم حاکم شود؛ اما نشد. تا انکه طالبان شهرهای افغانستان را یک به یک تسخیر کردند. این بار نیز در پنجشیر جانانه ایستاد، آنگاه که دست یاری‌کننده‌ای را نمی‌یافت.
در میانه سال‌های جنگ، روزی در تخار در شمال غرب افغانستان، در جمع مجاهدین و خبرنگاران نشسته بود و دیوان حافظ شیرازی را می‌خواند که خبر آوردند طالبان در منطقه‌ای حمله کرده و در حال پیشروی است. مسعود توجهی نکرد و به خواندن دیوان حافظ با عشق ادامه داد. یکی از فرماندهان از بی تفاوتی مسعود ناراحت شد و با صدای بلند گفت: آمر صاحب! طالبان حمله کرده اند. مسعود گفت: بگذار که این غزل را تمام کنم، مگر نمی دانی که جنگ با ما بر سر حافظ است؟!»
۲۵ سال پیش در چنین روزی، احمد شاه مسعود، شیر دره پنجشیر و قهرمان ملی افغانستان، ترور شد و جان خود را از دست بداد!⁩
@Iran_Simorq</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20713" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!  از این جهت خیلی شبیه احمدی نژاد است؛   منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/20712" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">منابع خارجی:
بر اساس تحلیلی که از بررسی تصاویر ماهواره‌ای به دست آمده است، در سال جاری شاهد افزایشی در ساخت‌وساز در محل زیرزمینی مشکوک هسته‌ای ایران در نزدیکی نطنز بوده‌ایم.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/20711" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر خارجه یونان، جورج گِراپتِریس، درباره ترکیه:
«ما درک می‌کنیم که این نوع تنش‌های بالا که اغلب از سوی محافلی در ترکیه همسایه می‌بینیم، همچنین به این دلیل است که یونان به قدرت واقعی دست یافته است — صدایی که بیش از هر زمان دیگر شنیده می‌شود.
من فقط می‌خواهم اشاره کنم که هر کسی که فریاد می‌زند، همیشه قوی‌ترین نیست. در واقع، اغلب آن فرد ضعیف است.»</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20710" target="_blank">📅 15:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20709" target="_blank">📅 15:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20708" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhNRNKMOVgOv8WkAJV3AxTmkTV2i8WSum0stI9_Hs0NPPYe6Ix1mlQIA6N6DMkZI_JzRPaQkooZZBY8LOG3b3kvIzixquEt3YmzEueG0QVYYV7I_1OcYJckWcTixgh90_m9DCLPRpk93GBsoINmgzMsqZRYNHBnR_7LDufk6dR9ApclCAuHOtLI-qnofw7pCU2IR5tT0hgTsQfrqKURMx5MnMG3WKiCva8Ozlgs3GTEPGjLiVN5-Z-7a1lEsQh3A0ZA-uoA-j2Deq-JwawMK_hW3uhehaI9Z7apncyHR-vrio9mssxCIwo19DoPKIskkRrYqL0t5Z6ySaC-hj9_0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20707" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی سپاه:
هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20706" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">این تحلیل برای 1 اردیبهشت است. تارگت من برای قبل عید 150 هزار تومان بود و تصورم این بود که از یکی دو هفته پیش یک اصلاح موقت بزند تا حدود 120 تومان که این پارت آخر نشد.  با این شتاب، اگر 150 تومان را رد کند تارگت مرکز تحقیقات مجلس در 240 تومان را فعال خواهدکرد…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20705" target="_blank">📅 15:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شروط ایران برای پایان جنگ توسط سخنگوی سپاه اعلام شد:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش اسرائیل از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20704" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skW-IwdY5Brf5ihpWZ73Tuez1YP4Txwlke8XZPWdFh7-tB9rqa3R5Q4ccV2Qbf8TkbJiA_ze2G7-USIHi_9CxnG3BpMriANAUQcIN2FBBC8-VVTGf5s2-K14D5wtlFZnfsyZmQKjawwPYBzJQ1V3b-3H7NPtfnr8oux_3Tk0WE2ZDaNbBxLyDicG2O0ddh6ATdIW1qxvhoX4mUaGPWjqLaHvGnve7aLMluP8qXArmYq4OngddiPw6UrVgbZHHZqHVMhnLkd0i1vzlp3Q2Eea0LrHmD1VhFbw482aS3NlgKaz3nP3Nm-AJtzWnDzngb2HWZ-olHZgMjtMU1YPUpol7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های رهبر حزب AfD درباره برنامه های اجرایی این حزب  دقیقا کپی برنامه های خاویر میلی در آرژانتین به اضافه:  — کاهش حمایت از اوکراین  — مبارزه با مهاجرت بی رویه</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20703" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏اکانت صابرین نیوز در توئیتر:   حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20702" target="_blank">📅 13:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
اکانت صابرین نیوز در توئیتر:
حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20701" target="_blank">📅 13:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شعارهای شب گذشته امت مبعوث در تجمعات شبانه
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20699" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20698" target="_blank">📅 13:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4qhkUHZQRSCzRHTQnOe6yD14Z98xJ06do01qjq7Q0M5BthXLL3WTXj-rgw_4Ph0jEjZOx2JEmjlgHS-UvOj-xfqUgHKx6ukYwbFeDprrQWDdo_QlOTp56mluI_EV12Cxp6bhrMx_1vg_s2T2Z-NtFOrHudTQu17Uz_pOCjR9xf_InCTVd6Xy9Ff-FQmeNrm_CDTJ7nPVVZBVtv5Xq7Y5KO9FjJr7WQyOvb25_Jzw70GVuw4ujvxzlnb4Tad4ZLMe7Qm5XFdDXRkiluxU-Mp5DNLZVzG0WiZrn4HF15877bHKBVKBkUo6PBa4ygd88PKl4yIODwG_D-DI5krfQirIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20697" target="_blank">📅 11:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وال استریت ژورنال:
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20696" target="_blank">📅 09:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جنگ اراده‌ها در تنگه هرمز؛ ایران و آمریکا چه کسی زودتر عقب‌نشینی می‌کند؟
جنگ ایران و آمریکا وارد مرحله‌ای شده است که در آن، اقتصاد به اندازه موشک و نیروی دریایی به سلاح جنگی تبدیل شده است. تهران و واشنگتن هر دو تلاش می‌کنند هزینه‌های ادامه جنگ را به طرف مقابل تحمیل کنند و در نهایت او را به این نتیجه برسانند که ادامه درگیری بیش از دستاوردهای آن هزینه دارد. به همین دلیل، آنچه اکنون در اطراف تنگه هرمز جریان دارد، صرفاً یک رویارویی نظامی نیست؛ بلکه یک جنگ اراده‌ها است که در آن هر دو طرف منتظرند دیگری زودتر تسلیم فشار شود.
از یک سو، ایالات متحده با ایجاد محاصره دریایی و هدف قرار دادن برخی زیرساخت‌ها و نفتکش‌های ایرانی تلاش می‌کند صادرات نفت ایران را محدود کرده و فشار اقتصادی بر جمهوری اسلامی را افزایش دهد. از سوی دیگر، ایران با تهدید شناورهای آمریکایی، ایجاد محدودیت برای کشتیرانی و تلاش برای افزایش هزینه عبور کشتی‌های تجاری از تنگه هرمز می‌کوشد هزینه اجرای محاصره را برای واشنگتن بالا ببرد.
ایران؛ فشار بر مهم‌ترین منبع درآمد
برای تهران، مسئله اصلی اقتصاد است. نفت همچنان مهم‌ترین منبع درآمد جمهوری اسلامی محسوب می‌شود و محاصره دریایی آمریکا مستقیماً توانایی ایران برای صادرات نفت را هدف گرفته است.
بر اساس گزارش شرکت Kpler، حجم نفت خام ایران که روی نفتکش‌های خارج از منطقه محاصره ذخیره شده بود، از حدود ۹۰ میلیون بشکه در اواسط ژوئیه به حدود ۲۹ میلیون بشکه کاهش یافته است. اگر این روند ادامه پیدا کند، فشار بر درآمدهای ارزی ایران افزایش خواهد یافت و دولت برای تأمین هزینه‌های جاری و واردات با محدودیت بیشتری مواجه خواهد شد.
اما فشار اقتصادی تنها در سطح صادرات نفت باقی نمانده است. دولت ایران هم‌زمان مجبور شده قیمت بنزین در بالاترین سطح سهمیه‌بندی را به ۱۰۰ هزار ریال در هر لیتر افزایش دهد. این تصمیم از این جهت اهمیت دارد که افزایش قیمت سوخت در سال 1398 به اعتراضات گسترده در سراسر کشور منجر شد.
بنابراین، تهران با یک معادله دشوار مواجه است: اگر در برابر فشار آمریکا عقب‌نشینی کند، بخشی از دستاورد استراتژیک خود در تنگه هرمز را از دست می‌دهد؛ اما اگر مقاومت را ادامه دهد، فشار اقتصادی و احتمال نارضایتی داخلی افزایش خواهد یافت.
آمریکا نیز هزینه جنگ را می‌پردازد
با این حال، تصور اینکه تنها ایران در حال پرداخت هزینه اقتصادی جنگ است، اشتباه خواهد بود.
بر اساس برآورد لحظه‌ای دانشگاه براون، جنگ تاکنون حدود ۱۰۰ میلیارد دلار هزینه اضافی انرژی بر مصرف‌کنندگان آمریکایی تحمیل کرده است. این رقم با سرعتی حدود یک میلیون دلار در هر دو دقیقه در حال افزایش بوده است. به‌طور متوسط، افزایش قیمت بنزین و گازوئیل از زمان آغاز جنگ بیش از ۷۶۰ دلار هزینه اضافی برای هر خانوار آمریکایی ایجاد کرده است.
فشار اصلی در هفته‌های اخیر از سوی بازار گازوئیل آمده است. قیمت گازوئیل در آمریکا به حدود ۵.۹۰ دلار در هر گالن رسیده؛ یعنی تقریباً ۶۰ درصد بیشتر از یک سال قبل. اهمیت گازوئیل بسیار فراتر از هزینه سوخت خودروهاست، زیرا بخش بزرگی از سیستم حمل‌ونقل کالا، کامیون‌ها، کشاورزی و زنجیره تأمین به آن وابسته است.
در نتیجه، تداوم قیمت بالای انرژی می‌تواند به موج دوم تورمی در اقتصاد آمریکا منجر شود؛ از افزایش هزینه حمل‌ونقل گرفته تا افزایش قیمت مواد غذایی و کالاهای مصرفی.
تنگه هرمز؛ میدان اصلی جنگ اراده‌ها
اینجاست که اهمیت تنگه هرمز دوچندان می‌شود. ایران می‌داند که نمی‌تواند الزاماً آمریکا را از نظر نظامی شکست دهد، اما می‌تواند تلاش کند هزینه پیروزی آمریکا را بالا ببرد.
حمله موشکی ایران در ۵ سپتامبر به سمت دو شناور آمریکایی، هرچند بدون اصابت و تلفات بود، دقیقاً در همین چارچوب قابل تحلیل است. تهران می‌خواهد به واشنگتن نشان دهد که اجرای محاصره هزینه نظامی دارد.
در مقابل، آمریکا تلاش می‌کند با اسکورت کشتی‌های تجاری از مسیر جنوبی تنگه، نشان دهد که ایران نمی‌تواند به‌تنهایی قواعد عبور و مرور در هرمز را تعیین کند.
اقدام ایران برای ایجاد یک «منطقه محدودشده» نیز بخشی از همین رقابت است. تهران می‌خواهد کشتی‌هایی را که از کنترل ایران عبور می‌کنند، با تهدید به قرار گرفتن در فهرست کشتی‌های غیرمطیع، جریمه، توقیف یا حتی مصادره، تحت فشار قرار دهد.
بنابراین، هر دو طرف در حال تلاش برای تغییر محاسبه هزینه ـ فایده طرف مقابل هستند. جنگی که هر دو طرف می‌خواهند دیگری آن را تمام کند. ماهیت این جنگ را می‌توان در یک جمله خلاصه کرد: ایران می‌خواهد آمریکا زودتر از محاصره عقب‌نشینی کند؛ آمریکا می‌خواهد ایران زودتر از استفاده مؤثر از تنگه هرمز دست بکشد.
واشنگتن امیدوار است فشار اقتصادی، کاهش درآمدهای نفتی و تهدید ناآرامی داخلی، تهران را مجبور به پذیرش شرایط آمریکا کند.
تهران نیز امیدوار است افزایش قیمت انرژی در آمریکا، فشار تورمی بر خانوارها، افزایش هزینه حمل‌ونقل و نزدیک شدن انتخابات میان‌دوره‌ای، در نهایت افکار عمومی و سیاستمداران آمریکایی را علیه ادامه محاصره تحریک کند.
این دقیقاً یک جنگ فرسایشی و روانی ـ اقتصادی است. پیروزی لزوماً به معنای نابودی توان نظامی طرف مقابل نیست؛ بلکه ممکن است به معنای آن باشد که یک طرف زودتر به این نتیجه برسد که ادامه جنگ دیگر ارزش هزینه‌ای را که می‌پردازد ندارد.
مسئله زمان
در چنین جنگی، زمان اهمیت تعیین‌کننده دارد.
ایران باید پیش از آنکه فشار اقتصادی به یک بحران داخلی تبدیل شود، راهی برای کاهش فشار پیدا کند. آمریکا نیز باید پیش از آنکه قیمت انرژی و تورم به یک مشکل جدی سیاسی تبدیل شود، بتواند به یک نتیجه قابل ارائه به افکار عمومی دست یابد. به همین دلیل، جنگ در تنگه هرمز بیش از آنکه صرفاً مسابقه موشک‌ها و ناوها باشد، مسابقه استقامت سیاسی، اقتصادی و روانی است.
در نهایت، پرسش اصلی این نیست که کدام طرف می‌تواند ضربه سخت‌تری وارد کند؛ پرسش این است که کدام طرف زودتر حاضر خواهد شد هزینه ادامه جنگ را نپذیرد. و تا زمانی که تهران و واشنگتن تصور کنند طرف مقابل زودتر از آنها عقب‌نشینی خواهد کرد، احتمال ادامه این رویارویی بالا خواهد ماند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20695" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد  تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20694" target="_blank">📅 07:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد
تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20693" target="_blank">📅 07:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر دفاع پاکستان، یمن را تهدید کرد:
اگر حملات از سوی یمن ادامه یابد، ممکن است مجبور شویم توافقنامه دفاع مشترک بین پاکستان، عربستان سعودی و ترکیه را فعال کنیم.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20692" target="_blank">📅 02:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_AbleDmzwa2PLf46EAvPR9TQAtl15CxLmQS93E04SIUJwIBC-k1KxgUJUUx6qR7ddf8eTc03V7bcdiCVmCXdadRA8TAtsv06rtXOKcdMZSJ9ey9SCjVRxo-2OnFMwdRFAp0iBlNQZZgW4i0lpwcldNG_M6vnhnXChrUCAMyDx8S2_pWQqyitTsyPcRLPPgoI1qaL3okTUEfo-QsJeDuP5MLsQ3X2TEQL1OvsitN5fwfdrqBlIEI1Fr1jqqah2HD1pl64xUHomtsnOLP2XUTx7ah_ol2HuKNXs8fLKu8u-YT29UmdQ_InYZnYy6T2BWAQTOzzkC0QvbHXhVo9l89oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20691" target="_blank">📅 02:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=c7FleD-_9qq7XyYdt9TIC16Q1t2zo3kS41hhHAylgMOQ6T_f4jlqeVKkfQQ2w5NCZceZsoVyqxe48sZdTPMkfUvYDSSuUmnIXCwuVXpe4QTwNJTaLkDvA_Q9Hw-do6Fwt6oH2JDYU69lmGB4W7rDa8y6kInn5to-DafcBPlyL91NQ5IvJWTrwYUHF6OfmI0RCr3UeK_d1dKYvra2b2ADLdrUYC4V-ylX5m9C4RZE-EQlZMNaT0EiuZ67jazDJ-uq5aaq9weSUi4eQrkr3JWMANcy_cRHdR9MLIVLxhFVOS1VyyoxF9Pc03zuUi04FDdCrs6RDs0WxKpKgWwocO-YMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8172d6b5b3.mp4?token=c7FleD-_9qq7XyYdt9TIC16Q1t2zo3kS41hhHAylgMOQ6T_f4jlqeVKkfQQ2w5NCZceZsoVyqxe48sZdTPMkfUvYDSSuUmnIXCwuVXpe4QTwNJTaLkDvA_Q9Hw-do6Fwt6oH2JDYU69lmGB4W7rDa8y6kInn5to-DafcBPlyL91NQ5IvJWTrwYUHF6OfmI0RCr3UeK_d1dKYvra2b2ADLdrUYC4V-ylX5m9C4RZE-EQlZMNaT0EiuZ67jazDJ-uq5aaq9weSUi4eQrkr3JWMANcy_cRHdR9MLIVLxhFVOS1VyyoxF9Pc03zuUi04FDdCrs6RDs0WxKpKgWwocO-YMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک انبوه موشک‌های پدافندی اردن برای دفاع در برابر حملات موشکی ایران به پایگاه موفق السلطی</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20690" target="_blank">📅 02:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehys9bDjMpadpJru9aiduu4QDRpcZwnRHyogZM8ijL3CUxejJvWo3yhk8vbgdacpaIMfiQcB4IiWkN2vrkK3gc4KssiniV2_31l0fF0VCrzfV-fClbkFF9nxN4cVfz7TdrBUYceYuXDLda7qJlFDo3sqB-ncQqTwCdulNutJrqbLw9sjTc_6P88vJlKZDe9fFc8KZ7ustqxrHjVKoZ0IzVcq6uWrNMcxPCjIedy44NeLdVa2unj3W019DkxRQjJ_sMSR4m4_sQZmLJzMheTBHs9LXsLVgxpeHUvWoAcdnc_cOoxFxVC5-q8WTSPadOPiftEEco84XPt_LZWZaZqESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20689" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، ۵ کشتی نفتکش ایرانی را منهدم کردند.
کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20688" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=l-weDLwx94GfK6iSTBE0bBYULn41l0GXOhp8NMRhejDWx2vWZrdtsniMUdJViUbJo_ZIC6KZk-P7dvNDabjc0aZJUF450rv-WxJNkEsbyWyuq7UVoWp0udbAQekKxKpI1ay4_CHi_HCBnKiS_2xpsP97gpE2NvEWuZ0__2XpZlBZSpcYPpyxdHtjDRWWnGRM3UEuC02kanO4cdkhEMMcVymGrjQ_QxxTgfEaHK4ZesYrZmK7VbtAoXRsJ5uxa2BhisEDf3HJ7GdsTmk3yyHry7tgLYkHa8YpH3sqahruN_xwRq5xDX015EiOchT6L7FxmPWNtJTUVu-l7EQFJdtLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03fbb033c5.mp4?token=l-weDLwx94GfK6iSTBE0bBYULn41l0GXOhp8NMRhejDWx2vWZrdtsniMUdJViUbJo_ZIC6KZk-P7dvNDabjc0aZJUF450rv-WxJNkEsbyWyuq7UVoWp0udbAQekKxKpI1ay4_CHi_HCBnKiS_2xpsP97gpE2NvEWuZ0__2XpZlBZSpcYPpyxdHtjDRWWnGRM3UEuC02kanO4cdkhEMMcVymGrjQ_QxxTgfEaHK4ZesYrZmK7VbtAoXRsJ5uxa2BhisEDf3HJ7GdsTmk3yyHry7tgLYkHa8YpH3sqahruN_xwRq5xDX015EiOchT6L7FxmPWNtJTUVu-l7EQFJdtLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردنی ها برگ هایشان از مشاهده موشک های با کلاهک بارشی سپاه ریخته !</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20687" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20686" target="_blank">📅 01:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من تردید ندارم مرحومه مغفوره برانیگان بخش هایی از اثر خود‌ را برای توصیف پدافند اردن، کویت، بحرین و اندکی هم خودمان خوانده بوده است.
مثلا اینجا به انفجار در پایگاه پدافند و شکسته شدن دیوارهای پایگاه اشاره دارد:
In the night, no control
Through the wall something's breaking
اینجا به تاثیر جنگال و عملیات SEAD روی رادارهای خودی اشاره دارد که کنترل را از دست نیروهای خودی خارج می‌کند:
You take my self, you take my self control
اینجا هم از قول یکی از سربازان پدافند می فرماید از این وضعیت تخمی خسته شده و دیگر اراده جنگیدن ندارد:
I, I live among the creatures of the night
I haven't got the will to try and fight</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20685" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20684" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20684" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آهنگ زیبای این شبهای خواهرمیانه:</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20683" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اصابت بیش از ۲۰ موشک به عقبه و الازرق اردن</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20682" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسراییلی ها دارند اذا رمیت میخوانند</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20681" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موشک های بارشی هم به سمت اردن پرتاب شده و در حال فرود آمدن هستند</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20679" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شلیک های پرشمار موشک های ایرانی به سمت اهداف نامشخص گزارش شده</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20678" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r72y8mYxYxoSZHeu9S6z9PFJua-1B3kLcSMFLiTL1ZNV9Qu9AB-FGdb2XfrmYuxs2bgkJotPFqHcGf930dpq7r6xIUS9BgSByJ63i6FRBABk8jgE4OjU-dr0-oJGoKMa7Z0LA4dGMTeMXC5bthVexHJcrU4nDXGmR-25wn8Viud5mviCorTqjDi20tcB-XgO69W0P8z5pkxTQteEHu0uQy-3Iy-QrrKYRZZOUbKtid3OuH-egJ_OhiLqcWyqeY-ZME5k7i_qERxNrr7_52NY7UNaURyE0Dz4ZY9dWbJndw_NS0qNC97Vb3d-UR3PZLf-5dzdrWZJJxxGqpCkVxWGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دوباره مرندی ذوالاکتاف به عربها</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20677" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرماندهی نظامی ایران تهدید کرده است که به نفتکش‌ها در بنادر کویت و بحرین حمله خواهد کرد و به خدمه هشدار داده است که کشتی‌های خود را ترک کنند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20676" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این هم رونمایی از ربات تماما بومی-محلی ایرانی در نمایشگاه کیش اینوکس  که اینقدر طبیعی ساخته شده که اصلا طبیعی شده   خودشان میفرمایند یک «داده» هستند و چه اسم با مسمایی که ولی خب.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20675" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLMEB3eKkh4z5b0gNmptGPuAWkBLe6-WfFipgxktC4cHqud2Ow1ffunDzCC43mShcDUfEL-x5LvATLYtXtCgUzq0XRPueRwjCPvzg1mMiaLi0PGEyl_hliDaVa1fz5r4T8vBx_ebi48Z6uS9pkQRtji--UkkgUqQHlzKOcxlJNACyMp4kaxQphkkUMvkMKJ3MuWsUnv2-Yifc-EXQtJv_tbTb0rjCf5lTI_FSHfxgLtXUDfZ3Nh2DjB-A7t3M7Xvd2nZUcs8gyyyg5_Pb_tD2k22r8fYcWiKmNedT2NjES19eons7kZLJQjlXQ7PLs0Dqku2clvMvo9ly_Pb6qfs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش هایی از حضور ربات های نظامی اسراییلی در حمله به مواضع حزب الله خصوصا در علی الطاهر منتشر شده که توان حضور در تونل های زیرزمینی را داشته اند!</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/20674" target="_blank">📅 23:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار در خارک!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20673" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجار در خارک!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20672" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گفته می شود چند نفت کش ایرانی هدف قرار گرفته اند</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20671" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">باز هم ریزشی است تا 4355 دستکم .</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20670" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شلیک های جدید از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20669" target="_blank">📅 21:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مصطفی عامر از رهبران انصارالله :  سپاس و ستایش خدایی را که عربستان سعودی را پر از نفت کرد و به ما کبریت داد</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20667" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZ-CbDXvbmYKGkiuCapjgPkgShaMpjtujXPRB5DWIlSR5B-5Fk_woJTe_fM5qTV3_NhO2VZSK8ypTxs7LSUfp7ei_xG3emj58hgn3x1ub3mGhWFUTxIzlE6NcTb0uNP4_MK1DqAVZizNaLP53ouYVP92EDVTeIJmv_w9SNu6-dWfETZnLoI5GFHSd8PwbSFJ3kUQg7nGzoNtogrql5b7xfkbwCBIy_eSspxHGYP3iswxKmkSANWFaPO9-U7w8vX4YnQfZyWad6xzoDICrjgDk44-Z6pOl4Z_wB9TgQAjENqmd5RGTj_d5s5ja9jYBAekLTySRofKO4eG3e2cnG93_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">video_2026-09-08_19-52-57.mp4</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/20666" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">video_2026-09-08_19-52-57.mp4</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20665" target="_blank">📅 19:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">video_2026-09-08_19-52-57.mp4</div>
  <div class="tg-doc-extra">1 MB</div>
</div>
<a href="https://t.me/SBoxxx/20664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ویدیویی از انبوه تویوتاهای نیروهای مورد حمایت سعودی که به سمت جبهه های جنگ با انصارالله (حوثی ها) پیش می روند!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20664" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20663" target="_blank">📅 19:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خب منظور این بوده!  یک شهپاد زیرسطحی است  (شناور هدایت پذیر از راه دور)</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20662" target="_blank">📅 19:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هاآرتص
:
حاکم امارات متحده عربی ۱۰ روز پیش از ۷ اکتبر درباره حمله تروریستی حماس به نتانیاهو هشدار داده بود.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20661" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSZnaS-vmS95scxS2S1rweOIlCscRMGORVesMFndBZgM5Gsr1ccD0sJIMw13w80xdIrw4HggK1L1XEzywIMmpurOp1USiKrb2S63cxYkkmGj3NFUqaCVVSlhklyLeEf9i8ohqKuMhvWCra3BYZxY555Smyqqnj0493khC49DVtSsIXhSpFmDi62pKUXgDiKiK4BLRGdPWvvGJwec-6q_9kbMNneBZ4vuPu-fl0w5TS3An04YcVSRvXVuYcpp_cMhWTEGybYXhn-CjmUi0DE8YmvrBgtKzjutR-IPlMsXZbqtjagYNfMRn0WIo_GEjj_npAaPW4tTOHI_LhRIhuWAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  به لطف پروردگار متعال، رزمندگان نیروی دریایی سپاه پاسداران انقلاب اسلامی موفق شدند در ورودی تنگه هرمز، یک فروند از جدیدترین زیردریایی‌های پیشرفته متعلق به ارتش تروریستی آمریکا را به دام بیندازند.   این عملیات در یک…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20660" target="_blank">📅 18:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
به لطف پروردگار متعال، رزمندگان نیروی دریایی سپاه پاسداران انقلاب اسلامی موفق شدند در ورودی تنگه هرمز، یک فروند از جدیدترین زیردریایی‌های پیشرفته متعلق به ارتش تروریستی آمریکا را به دام بیندازند.
این عملیات در یک اقدام اطلاعاتی و عملیاتی پیچیده، صبح امروز انجام شد. این زیردریایی پیشرفته، مجهز به جدیدترین فناوری‌های موجود در جهان در زمینه زیردریایی‌ها بود و در سال 2025 به ناوگان ارتش تروریستی آمریکا تحویل داده شده بود.
لازم به ذکر است که این زیردریایی به دست گرفته شده است و تصاویر آن در چند ساعت آینده منتشر خواهد شد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20659" target="_blank">📅 18:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو:
ما به جنگ نهایی با ایران بسیار نزدیک هستیم.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20658" target="_blank">📅 18:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کرملین: پس از بازدید نمایندگان ایالات متحده، پوتین و ترامپ در یک تماس تلفنی «بسیار صریح» گفتگو کردند
پوتین به ترامپ گفته که روسیه هیچ «طرح تهاجمی» در قبال اروپا ندارد</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20657" target="_blank">📅 17:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الاخبار: ترکیه در حال میانجیگری میان دمشق و حزب‌الله است  روزنامه الاخبار لبنان: ترکیه در یک حرکت دیپلماتیک موازی با تحولات منطقه، در حال میانجی‌گری برای تقریب دیدگاه‌های حزب‌الله لبنان و دولت موقت سوریه است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20656" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الاخبار: ترکیه در حال میانجیگری میان دمشق و حزب‌الله است
روزنامه الاخبار لبنان:
ترکیه در یک حرکت دیپلماتیک موازی با تحولات منطقه، در حال میانجی‌گری برای تقریب دیدگاه‌های حزب‌الله لبنان و دولت موقت سوریه است.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20655" target="_blank">📅 15:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 25</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
سه شنبه 8 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20654" target="_blank">📅 14:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رائفی پور ورژن مونث بدحجاب موجود شد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20653" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….  به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20652" target="_blank">📅 12:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa849e433.mp4?token=B8v4F8_v9Z5DwLwk4DlrGjkOHv_zGcDNoKGZygCKdJub8hkCkmlpBvWi-ZXRt-ZZvqdquXBG3raElGcfLUGhDBY6V9yA_HgK_hzDVh3xq_FOyRW7iTTXdScdwXYtnlNEfLqhmk960a_RxWGN6KvbuJlvgYFnZd0Wz4svxtaPvusdo3rbWPRKLtwje6ih0W8SEgagL_gIkTuRqdHy7d3fus32kqBOhaaK7FcuAKQD8gA7sLy7HKYcixib7DyuQyg_zt3pf6OG8cnxFxf0hSsP4sy1ec_fKse3Is-JeNCp14fVLGQsI3ZzVxGzUGFWhM9y3Leg9GoGYjyNDX1famktdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa849e433.mp4?token=B8v4F8_v9Z5DwLwk4DlrGjkOHv_zGcDNoKGZygCKdJub8hkCkmlpBvWi-ZXRt-ZZvqdquXBG3raElGcfLUGhDBY6V9yA_HgK_hzDVh3xq_FOyRW7iTTXdScdwXYtnlNEfLqhmk960a_RxWGN6KvbuJlvgYFnZd0Wz4svxtaPvusdo3rbWPRKLtwje6ih0W8SEgagL_gIkTuRqdHy7d3fus32kqBOhaaK7FcuAKQD8gA7sLy7HKYcixib7DyuQyg_zt3pf6OG8cnxFxf0hSsP4sy1ec_fKse3Is-JeNCp14fVLGQsI3ZzVxGzUGFWhM9y3Leg9GoGYjyNDX1famktdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی پور ورژن مونث بدحجاب موجود شد</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20651" target="_blank">📅 12:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw_VWdmhHRk2cOMv7qtC7Uj4CNUqVOmel2PBdjalKviuyDsFxYv-sVe2IRgS8RtvkOq4pjtGtPPvrekmtHW9EWuxHNJJ_9JZjMNh70p-5YqPEc8ORi6lxPxGYmLVGdDuhYPOkrnZtwMR7ZyVWg-R4Xv3viCa815dJBTySUmeObr88t5XvD-0onVp8RGvo_wYoxXj3BK9R8zCt8D5R33ugg-IilslM-QQ7WyC_QG_aH9WoRcDUgfwuITfbEWIa723SpYBgy4yWaOlkBwkAVJJnxkSXThE9Pxv0bVUGlzZe73TDEsnYE7rzfYpeSKesbMzLRNYSDnz3dXRa1-BypQrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولکس‌واگن با پیمانکار دفاعی اسرائیلی «رافائل» توافق‌نامه‌ای امضا کرده است تا کارخانه خود در اوسنابروک، آلمان را به یک مرکز تولیدی برای قطعات سامانه دفاع هوایی «گنبد آهنین» اسرائیل تبدیل کند.
انتظار می‌رود این کارخانه در سال ۲۰۲۷ تولید خودروهای سواری را متوقف کند و به‌جای آن به تولید کامیون‌ها، ژنراتورها و سکوها برای پرتاب سامانه‌های گنبد آهنین بپردازد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20650" target="_blank">📅 10:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی از اصابت به فرودگاه ابها و شنیده‌شدن انفجار در مناطق جنوبی عربستان منتشر شد.
این حمله سومین حمله به تأسیسات نفتی عربستان در کمتر از ۴۸ ساعت است.
‎</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20649" target="_blank">📅 10:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">220 پیپ</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20648" target="_blank">📅 09:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20647" target="_blank">📅 09:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfe837d4b.mp4?token=QtIx9GmJCu828W5_Lfy8RxWsYooJXq5NqAnOwZ0J5kB3hkG_PNuoEaOGb03sURLbED5qmU-zXEjpZbRdRTBuP05mWSVBlrXNAIxX-0ePR7JMIxg6nzlg7L0QOXPJvSdmrdWuoaPEY7hjsuNL2q3-eTuBBdlDRlvy0Kr26Rz5oeoayig9G1buXSE-AukDI2MlCjO477O4Gs1Czbstm86vQxFf1sXYajo7DEZcv4wUsDmRAF1I1gjXIeEzk1DYxojrB2vrtCSfRUXlXMqOiZzv7UJOd3wOnlj7GnCNfkVsbeco9WSyRDoZ5hDoiAjSA_18iK3BFwcBS1pNnRil_NWJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfe837d4b.mp4?token=QtIx9GmJCu828W5_Lfy8RxWsYooJXq5NqAnOwZ0J5kB3hkG_PNuoEaOGb03sURLbED5qmU-zXEjpZbRdRTBuP05mWSVBlrXNAIxX-0ePR7JMIxg6nzlg7L0QOXPJvSdmrdWuoaPEY7hjsuNL2q3-eTuBBdlDRlvy0Kr26Rz5oeoayig9G1buXSE-AukDI2MlCjO477O4Gs1Czbstm86vQxFf1sXYajo7DEZcv4wUsDmRAF1I1gjXIeEzk1DYxojrB2vrtCSfRUXlXMqOiZzv7UJOd3wOnlj7GnCNfkVsbeco9WSyRDoZ5hDoiAjSA_18iK3BFwcBS1pNnRil_NWJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تببین مگاپروژه هوشمندسازی پمپ های بنزین !
حتماً ببینید.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20646" target="_blank">📅 09:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRDMtYUSwy-TfMlSyzq0EC3rmE5PY7xXuscs2gecjKmj4lYHqtFENpv5F_LrJD68-O52uG_c1_BDK7Q2n7Jb1ZCbYMA7lgIrwBQDo4ltNOLLTzDyinSToK4viLzLsa5UusPKzchukF0BbyeoNCi3ZO4gHMc-NYXo3YRJAn2hsTkZwJy2QFfwlfnw0RVI5xw62hPl22xZc-bf3_gS_KflLR_Qp1slAi4h_DoHh8Y7HEQe6y7wF4L4Vg6kyCGRUZLc-kwGj8hRDUkosdV4nZHc8lPQAfLXMgSv8o-AYZM6cyjT4PLkmzEolYYZGt3QBueCvI-nuCi_Qf_9_XMi6ItZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت یمن</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20645" target="_blank">📅 09:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvBYhbBCyzV4cUI_iigRNJqefMFRjy7dKcu4VFfsANydblfbqPQYZdj5IXsrQC65fgtPElVCIi8CHkY9Ae6SwxLTUOeAxFVnoHh2lt5S5wxs0jzdau9Sx_nQy9eoPzW7caiDOveyRzl8DEtadIttfWGk3An9Sm8Gt4mMi_AUm7JFnYPLrcZYCkKY5RAPVlIff7xtavvR6Isc9rk4M8osx1MMyDP1xDeTA3OcFzQvZkqY_lzWsQEDcMJldWzB-BU9Zm2hTPW5tfbS94K8bjaQ6a-65pFbXIuYAdW_T6lLxj045g6KOOHcFI9nvDJtt60p_0gwHMVFvmPgzRJhGP9qWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد. نظر به رشد طلا در بامداد، از اینجا به بالا توصیه به فروش طلا داریم.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20644" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdE-LSO_VCvXJxrhpBXL4rWAtgzIuWzd0gDTZW_MWWDHHBwHaoIDXhVtZV2jQtvhfjqRnDhWe7DH_1j7itmNN305aDIgU34wxzC4blG2RECygui-dFtUio4Y-QUO-X8xeBTrrdRm61R6aj_mmgEV1kxH8dt4GNnuJvb-khVkH1Pmu3frL6MJZnaERf4W-vSAqfmKwEfe8aZycCmbOCVF7RPkWjmYwPH27FOn_iOX9Yw7Tl-DK3MCELL9qutovSaUrB_Pu8szIByudsxfHRWA-GpkMcLWBY8WDug7Cotn1IMTXoPTnjQrOoM4m3kURFlZxm9YVGDtmuMCHzBOiqyTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20643" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سفر امشب ویتکاف-کوشنر به روسیه قطعا با افزایش تنش میان آمریکا و روسیه به دلیل تصویب قانون تحریم های گراهام و متعاقبا انتشار گزارشهای موثق از کمک نظامی روسیه به ایران برای ساخت موشکهای کروز ضدکشتی و سپس اعلام ترامپ دال بر ازسرگیری ارسال تسلیحات برای متحدین…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20642" target="_blank">📅 08:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzo3JlpGbkeHaZWT2WPJhNnSxTALdnGjWBrjuwrY_K4FIPcLPP0EcUhS9eABMIjYatMdWvzQjjTvb7u3W14ZfQZut1K94ZTr8w71NB6hXnTmonyHu37L-Bq7MiKAEHF_YJ-qOz8nYDxm2kU2RjgFJp4xT91i8kTnDNJizEjlKCS-3f2JlFharOAz7J4DxZXFXZuUaojoCGMx34ffuyv8lTyEsEPCyxMmKz0vBUOhmwolekSgvQ2qHKEsNLeUHMLhOdSzhZ6fWZ9FfPb62jGeLF2Zs0pkTjH_Ojs1Q7LJ7lOTKhXyfCku3xtoGfOx9K24X4QJ9jEy99MOt9caQTOHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران شرایط جدیدی را برای پاشینیان در مورد "مسیر ترامپ" مطرح کرد.
ایران به طور غیرمنتظره، شرایط سخت‌گیرانه‌ای را برای نخست‌وزیر ارمنستان، نیکول پاشینیان، در مورد پروژه TRIPP تعیین کرد، در حالی که لحن دوستانه‌ای را در بیانیه‌های عمومی خود حفظ کرده است.
تهران خواستار این شد که امنیت این پروژه توسط نیروهای مسلح ارمنستان به طور انحصاری، یا توسط نیروهای نظامی یک کشور ثالث که از قبل در ارمنستان حضور دارند، تامین شود - به وضوح، منظور نیروهای روسی است.
به گفته منابع، به این ترتیب، تهران تلاش می‌کند از حضور نیروهای آمریکایی در مرزهای خود جلوگیری کند. در غیر این صورت، در شرایط تشدید تنش، طرف ایرانی، حضور آنها را به عنوان یک هدف مشروع تلقی خواهد کرد.
این موضوع، اجرای پروژه‌ای کلیدی که از قبل عملاً فلج شده است، را به شدت دشوارتر می‌کند.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20641" target="_blank">📅 00:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سارا خلیفه مجری مشهور مصری به دلیل قاچاق مواد مخدر به اعدام محکوم شد!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20640" target="_blank">📅 00:26 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
