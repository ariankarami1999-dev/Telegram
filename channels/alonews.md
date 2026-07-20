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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اداره هواپیمایی غیرنظامی بحرین اعلام کرد که پهپادهای ایرانی، سامانه‌های ناوبری هوایی غیرنظامی این کشور را هدف قرار داده‌اند، اما این حمله، فعالیت‌های ترافیک هوایی را مختل نکرده است.
🔴
این اداره اعلام کرد که این پهپادها، تجهیزات ناوبری هوایی را در منطقه اطلاعات پروازی بحرین هدف قرار داده‌اند و افزود که مقامات، بلافاصله و مطابق با رویه‌های عملیاتی و امنیتی، به این موضوع واکنش نشان دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/136001" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مقام آمریکایی به سی‌بی‌اس:
تشدید تنش به زودی آغاز خواهد شد،
هواپیماهای ترابری و سوخت رسان آمریکایی به صورت پی در پی و بی سابقه در حال ورود به خاورمیانه می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/136000" target="_blank">📅 14:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ایلی کوهن، عضو کابینه امنیتی اسرائیل: اگر ایران بار دیگر به ما حمله کند، پاسخ اسرائیل از واکنشی که در رویارویی اخیر شاهد بودیم، شدیدتر خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/135999" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cdf507a0.mp4?token=L9jQO4zix5WvjOPW1I6OfwqeTkRrynD0ALHlhiu8-eY3SugH24dGYlE9oGJbV51f7zOS1Tlacn5esrk4Mxd6EUIJGMmW5lbBkup_B_vDme8GjWlpXUyEmYohH21mafAlDKGuyifPwimD1BkDmTodw310hDMdWrqr1hmcD8_uvpU9JH0HjrMHxAEcY2ZG6IvznCaAMZbKyf9ym95KPzliremxJ0okCIPWMq8bzsu8RjpfaBe4pfXkK61R14kYnDxSC2nTxKGf7H0UK2o_lv8fXMz7ovJE8MTKCv0d12LXL1L1xYgqj1YQEWIuWxBeBhk0J6P_Yn6ENxhvGzk7UXWf_jA46a6Iprqvxo_6eIhMzKuyf9KXsmeuEi7pUbAi8qISaxw90iVs6vXPlzQgFKSAi8ro2cxCpGpVoxNiDvA8Mpln9UC6hZ8tvGy4dIGv6YMg7VSB6tGtnHLJe9-pvicW9Mgkdy7BgP_CpteisZ36H4IGolF7Adk04hcb2cAlIHLpxPpFrIw4r846ItpC85jWpw6xRWb6Y3wtV3gyV6MiPtk470sHiELaxWbKMP9Cu2fN6NoisfGGmydsZwqQv7ofdwYiRA9vKdfbbjz0cYO8aSBVqLrY6K5ptBD20Gu9WP2aWswzAO_zxddNnfKsqt6k3rIYUZThEmTWjZBJ3JMl53M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cdf507a0.mp4?token=L9jQO4zix5WvjOPW1I6OfwqeTkRrynD0ALHlhiu8-eY3SugH24dGYlE9oGJbV51f7zOS1Tlacn5esrk4Mxd6EUIJGMmW5lbBkup_B_vDme8GjWlpXUyEmYohH21mafAlDKGuyifPwimD1BkDmTodw310hDMdWrqr1hmcD8_uvpU9JH0HjrMHxAEcY2ZG6IvznCaAMZbKyf9ym95KPzliremxJ0okCIPWMq8bzsu8RjpfaBe4pfXkK61R14kYnDxSC2nTxKGf7H0UK2o_lv8fXMz7ovJE8MTKCv0d12LXL1L1xYgqj1YQEWIuWxBeBhk0J6P_Yn6ENxhvGzk7UXWf_jA46a6Iprqvxo_6eIhMzKuyf9KXsmeuEi7pUbAi8qISaxw90iVs6vXPlzQgFKSAi8ro2cxCpGpVoxNiDvA8Mpln9UC6hZ8tvGy4dIGv6YMg7VSB6tGtnHLJe9-pvicW9Mgkdy7BgP_CpteisZ36H4IGolF7Adk04hcb2cAlIHLpxPpFrIw4r846ItpC85jWpw6xRWb6Y3wtV3gyV6MiPtk470sHiELaxWbKMP9Cu2fN6NoisfGGmydsZwqQv7ofdwYiRA9vKdfbbjz0cYO8aSBVqLrY6K5ptBD20Gu9WP2aWswzAO_zxddNnfKsqt6k3rIYUZThEmTWjZBJ3JMl53M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین: تایوان، بخشی جدایی‌ناپذیر از خاک چین است. این، اجماع غالب در جامعه بین‌المللی است.
🔴
پیام ما به مقامات حزب دموکراتیک پیشرو (DPP) کاملاً واضح است: روند تاریخی غیرقابل توقف است و استقلال تایوان، راهی به بن‌بست است.
🔴
تلاش‌های مردم چین برای مقابله با جدایی‌طلبی و استقلال‌خواهی در تایوان و دستیابی به وحدت ملی، روز به روز درک و حمایت بیشتری را به دست خواهد آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/135998" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
موگویی: «ترامپ درباره مشهد درست گفته بود، مشهد سقوط کرده بود.»
🔴
یادتونه ترامپ اون شب چی توییت کرده بود: یک میلیون نفر در مشهد تظاهرات کردند!
🔴
یک میلیون نفر در یک شب فقط در مشهد  اومدن بیرون، جمهوری اسلامی قتل عامشون کرد و هنوز داره تک به تک جوون‌ها رو اعدام،…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/135997" target="_blank">📅 14:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت خارجه کره جنوبی به بازدیدکنندگان کوتاه‌مدت توصیه کرد «فوراً» خاورمیانه را ترک کنند، «مگر آنکه دلایل قانع‌کننده‌ای برای ماندن داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/135996" target="_blank">📅 14:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بقائی: حقوق حاکمیتی ایران بر تنگه هرمز غیرقابل‌مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/135995" target="_blank">📅 14:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0792b06244.mp4?token=iG3bQjljLOTVy0H6rbERPbs5FJkgcpAgUTrk8tsJ3a36L1ogiEIHR8jlyCdfeASvcBMMCKB_cTzTjikYT7eJZjRr4LFdoPgazIeFkHAPa2nbdosviaDjR8HyxtTjNoVMzbtR5F-iv1kkbt-uo1b6cbP04b8lGbdh2GGdpygBVqKQ-BEp6EbHiRgbn6zXn9AIpyMshV2KM2USZ3FVd5JN7_MbFQ_Hq1WvsCa6KPUHwAcpr_8PU1KirY8hL5K1dRDta4JGBmo6ze2h8bcxiwRLPau7xAEXk6ASn7DQxuhx6szt3PX_AAeB5NDweoORqLzmRWlL2ZQL9YpbzzCFluv9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0792b06244.mp4?token=iG3bQjljLOTVy0H6rbERPbs5FJkgcpAgUTrk8tsJ3a36L1ogiEIHR8jlyCdfeASvcBMMCKB_cTzTjikYT7eJZjRr4LFdoPgazIeFkHAPa2nbdosviaDjR8HyxtTjNoVMzbtR5F-iv1kkbt-uo1b6cbP04b8lGbdh2GGdpygBVqKQ-BEp6EbHiRgbn6zXn9AIpyMshV2KM2USZ3FVd5JN7_MbFQ_Hq1WvsCa6KPUHwAcpr_8PU1KirY8hL5K1dRDta4JGBmo6ze2h8bcxiwRLPau7xAEXk6ASn7DQxuhx6szt3PX_AAeB5NDweoORqLzmRWlL2ZQL9YpbzzCFluv9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی بامداد امروز به ساختمانی در شهر مسکو، پایتخت روسیه، اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135994" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m31Ah6JeKuDZvfxuHirIHax4ahOPjJlrEHfSmcAfrpqRVx8e-WRB6vyplI9zZATFFRy7PtLCsPOhrskgdOkNyDFrCrpxkK_eTyVaixgWlUww8yWdezhsJX3I3O_5uVE5eI4DOLcWvqGtP9Kg-uMaeC56OZmZMc7EDPHOtWYX3jmYbq8s8UZFMLmq3IA2F24qKjxalEEwW2bEXKJHuCAiSqN5qwyisgoC5QQjQ-idsyN-KoDm7rrbwRy_sVPAFQqTTbH3cxWViWSo7R4-Ao1zQqhytvrotnumC3vjReqcIsocujEwjau22hKAHwTq-5EweVI3h8S_e2q10Wvej8oauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پادشاه چارلز سوم، استعفای کیر استارمر را به عنوان نخست‌وزیر در کاخ باکینگهام پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/135993" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b2fcbad5.mp4?token=IlEFieB-3yAgDwHFcn116XfKL2aMIGe26lMOFgWzIzjvCY92Cdb2dhN2A97JXR09-AtipErT3mTWQrRLP6lrp0X-rnZOIPIx-hLsuK-BWIsXngs3e67lVOQQZ3hXYND1n6sb1QM52n6hWVrwyL7PCJ3Y3s015brzipOxLOVD53G18rN1d68h9klckhdrIoeHOwYEMRkHtbBcC4HRngsfYiW7PVtvVYFJHNG3C7NIqQvZsw3yPlvOL6N754ZRIJXljLLaTg2EdITjrelfNRfzBOEe8GZ85oY60xnQfOJrl0sigXz2D3baz-hDLl_kBGxr9pg4aJDYRjkyUwHIz842DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b2fcbad5.mp4?token=IlEFieB-3yAgDwHFcn116XfKL2aMIGe26lMOFgWzIzjvCY92Cdb2dhN2A97JXR09-AtipErT3mTWQrRLP6lrp0X-rnZOIPIx-hLsuK-BWIsXngs3e67lVOQQZ3hXYND1n6sb1QM52n6hWVrwyL7PCJ3Y3s015brzipOxLOVD53G18rN1d68h9klckhdrIoeHOwYEMRkHtbBcC4HRngsfYiW7PVtvVYFJHNG3C7NIqQvZsw3yPlvOL6N754ZRIJXljLLaTg2EdITjrelfNRfzBOEe8GZ85oY60xnQfOJrl0sigXz2D3baz-hDLl_kBGxr9pg4aJDYRjkyUwHIz842DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزاک هرزوگ، رئیس‌جمهور اسرائیل:
ما نوادگان پادشاه داوود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135992" target="_blank">📅 14:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1ddfa795.mp4?token=JsNeMczEXNg4ppQYoJwsasIAsdjCvDBykDMM1KFoqGQVsBJaB7Xn6_zDLjVNsTo2vCcw_jM3TgJKHfNikiFGkfs8w2gzQhmXdchXFqG-OUTiVP0tsBPLx92LkUJoC5pKrpwXQG-SXjj9j0YN3gluAFL6YVIKIlmbdo5BG5KBSPmk3M4FbXfJOHCYDgwzNmdrW_J-c8GQx6nF0PTUyuHn5e88FdOH5ZRoRPkkHEIPpCRSH53amVUkXA_nagzqmE_cCAD2aLads-kNXRDfmseFvzCMbUO3w3CwO4jDs4JCWzvmWFnlc_kDSMJSM2CfugIQlxeoJLTp0B-1c2FaYi4cUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1ddfa795.mp4?token=JsNeMczEXNg4ppQYoJwsasIAsdjCvDBykDMM1KFoqGQVsBJaB7Xn6_zDLjVNsTo2vCcw_jM3TgJKHfNikiFGkfs8w2gzQhmXdchXFqG-OUTiVP0tsBPLx92LkUJoC5pKrpwXQG-SXjj9j0YN3gluAFL6YVIKIlmbdo5BG5KBSPmk3M4FbXfJOHCYDgwzNmdrW_J-c8GQx6nF0PTUyuHn5e88FdOH5ZRoRPkkHEIPpCRSH53amVUkXA_nagzqmE_cCAD2aLads-kNXRDfmseFvzCMbUO3w3CwO4jDs4JCWzvmWFnlc_kDSMJSM2CfugIQlxeoJLTp0B-1c2FaYi4cUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد اسرائیلی به یک خودرو در شهر غزه حمله کرد.
🔴
گزارش شده است که حداقل ۱۴ نفر مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیمی به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135990" target="_blank">📅 14:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca140d784d.mp4?token=edepPKHo5kaYgcyOTbzovtQKr58lokpXv5eNRq4EhiGv1D1UFenVN8xKdQUtJtKsKhHnIPu8_poesgUC7rvUiuZm4XqGWSGI9v4czyHrlpLv-H5UtRvM5SLPE0K_EMFL8RjLCzCMoGjGuwXgSsvYiKOlMsfuaiuaO1uZW1E3aVaj0rHDc5EQw3N8vJZ2AMoecCP04JX0hGxIBXL6AEOqFtxTsetwxNhabTegWMYVz9CuWAYUdgGpWpmawXjtmSZ6Kh1zPo3EEzfGcxCwuki7BtWPOWcyvO7Axx4JHDDk87acn23X4tFqFZhESb8uUByTmdfqjLa-RziYwxaOp-uckna07DDD7VbrC6JmnFlYhf6AEW1C-t2GAi8eUL0jdLGOvaAz1oeNqAVsbwZ_XeyqpOP_-VM-qG2qyj6DMilZqLQH61OfgWaD4KoX4_CrhcMsaVYS5mxSoOHeIKu0QdZV79GXuS4Ov-YfA8ztn6-Rw08VwD2dUOFoNIFFtXCA73Xb8lZ7eTCFZDJuXjslc0WyfpVSbzLjdawlDh8-cbpE4TL3B7nM24Y6KzBZImkQyiIkWU0-rTtfOkxdJ22ycge2tIQ_pf8g7ZNKe4wsq3cEUFOKmBDIKi8U4jL7GsMulP33R4vtISrYXJIiLwYsN46EEN5-PcpUUX6QmZcuXouV_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca140d784d.mp4?token=edepPKHo5kaYgcyOTbzovtQKr58lokpXv5eNRq4EhiGv1D1UFenVN8xKdQUtJtKsKhHnIPu8_poesgUC7rvUiuZm4XqGWSGI9v4czyHrlpLv-H5UtRvM5SLPE0K_EMFL8RjLCzCMoGjGuwXgSsvYiKOlMsfuaiuaO1uZW1E3aVaj0rHDc5EQw3N8vJZ2AMoecCP04JX0hGxIBXL6AEOqFtxTsetwxNhabTegWMYVz9CuWAYUdgGpWpmawXjtmSZ6Kh1zPo3EEzfGcxCwuki7BtWPOWcyvO7Axx4JHDDk87acn23X4tFqFZhESb8uUByTmdfqjLa-RziYwxaOp-uckna07DDD7VbrC6JmnFlYhf6AEW1C-t2GAi8eUL0jdLGOvaAz1oeNqAVsbwZ_XeyqpOP_-VM-qG2qyj6DMilZqLQH61OfgWaD4KoX4_CrhcMsaVYS5mxSoOHeIKu0QdZV79GXuS4Ov-YfA8ztn6-Rw08VwD2dUOFoNIFFtXCA73Xb8lZ7eTCFZDJuXjslc0WyfpVSbzLjdawlDh8-cbpE4TL3B7nM24Y6KzBZImkQyiIkWU0-rTtfOkxdJ22ycge2tIQ_pf8g7ZNKe4wsq3cEUFOKmBDIKi8U4jL7GsMulP33R4vtISrYXJIiLwYsN46EEN5-PcpUUX6QmZcuXouV_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک ستون دود غلیظ از بندر الاحمدی در کویت به هوا برآمده است، این اتفاق پس از حملات اخیر رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/135989" target="_blank">📅 14:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVUycls9NIDyFXIVLMl86HhTkwPIQZ7wx_f-5vRUprJ54BR2fsuqms4eLBN4DZZwXpzi6MZXTgY_0Cyj0O8dVaVfKPeh07L9LiyiQhjUwBVZK5g6Rh6hhwceS83uAx7J50h250quPNoRUhP4PSmSgcHkLuI-6QH3e_afR50oHlbT1hk2B--TjwVF5_aKwKLb6S7-CJ6kK_RM3hQVb9sANTLTvzvuxvxCpxMSuyVLgZM8iv9XHu5a8rRmjTuo37LSGjUIH8VupdrLCwz3W4T529lCAh-IBKuUQMZHanKlOPXDchjoAWaiGd1urLGkQKyCcldh2znS6klrw2nXqcqRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW78NF03Eb18nn6-gp-t7XDiGr42NA_cRXuZ-J2dljTcTj0utiWsk6zG_w_44r8mLHd7XeFPeaiR593VD8XHzWqz3IWE4kXfnDcMajvgeC0EwzlaDm_VBwqJYFEN37UnF12ypnk6iAErE9T6-34PJishorF_t2Si2_bTgYLZsU2EfpyIQvG6OI2KB-Z1MFEKQxTuzeE_0TkE792LpI60v5nT1dMQ4yykYP6DTJ2yeCyFcz4hr4pVDxWEN077znHschXR1KOcN8sIuL10YQSdy3xP2r1FKBh-kZcV-ZnEJdQEDcNoampbCwPcPJivAE5VyeZibk040YBVe29LyJIY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B33nsMJ6ZrxMgS9HEE_1i9WeXNMmUwcFyWxxVlHjWxPBDhGfVAjAcGFTlX-ddT1wEAhO0_phymGyfLo7UkJUbSIN6cNKQWyXDG1Sq1is4AHrIYFN076A2TT_E3OCBaMWwtyykHS-7_iN8R_s9yD2bbv3reJ0IazGRW9h5o8V6Fe4GELESI4qtIGWZ6gdcz7t07UdZnbhZbqPN5dorvCJ81fq-v1drqE6dw54Ceb934kbIGTnvZtFZtum5mSMc-xC81i-qefYPDBv2OH7Ik4nZ1pf1i8JbB2GlMeMxu9NRKbEs6PKQl-dx3xg3IZwLdse0Xf9l68oMXR-ySmBzoyFKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی که توسط ماهواره‌ها گرفته شده، ویرانی‌های گسترده‌ای را در پایگاه "الأزرق" در اردن نشان می‌دهد. در این تصاویر، تخریب محل‌های اقامت سربازان آمریکایی، به همراه انبارها و محل‌های نگهداری هواپیماها، به وضوح قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/135986" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93c584a72.mp4?token=Ynvwj_6xz-UjdYHVKdha0pylTByLdWTD6IuK0cpbHhN8tzvDVuQXo_KLoune6JB5aTePKgxgogvoMTP5GhPG3szy9u2alBUop89a6XFTHKGBSlViN-Ya4pL6P5-LzqGSXwTSvuxDuksxuDibav32UcwsYzKS9aPTXE-2Pta9hgOEg3N9yLRu4dX5tapGNrENveCN6yRygvYJo51ZpHPifCsfE7NI_ELYlK14sSiq9mfTYF87xgldXZa5Yja0VucfZV5HqVV-b0OPVuxtHQWr9YQyRpp_HtFe5nhUnAJycEaHIzWj8FOf5YpWqiP18zXGi8HgcDzaDyeueMtPSYjRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93c584a72.mp4?token=Ynvwj_6xz-UjdYHVKdha0pylTByLdWTD6IuK0cpbHhN8tzvDVuQXo_KLoune6JB5aTePKgxgogvoMTP5GhPG3szy9u2alBUop89a6XFTHKGBSlViN-Ya4pL6P5-LzqGSXwTSvuxDuksxuDibav32UcwsYzKS9aPTXE-2Pta9hgOEg3N9yLRu4dX5tapGNrENveCN6yRygvYJo51ZpHPifCsfE7NI_ELYlK14sSiq9mfTYF87xgldXZa5Yja0VucfZV5HqVV-b0OPVuxtHQWr9YQyRpp_HtFe5nhUnAJycEaHIzWj8FOf5YpWqiP18zXGi8HgcDzaDyeueMtPSYjRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها که شرایط جنگیه و پدافندا هم تو اکثریت مواقع  کار نمیکنن؛
پیشنهاد میکنم این ویدیو رو یه گوشه‌ای ذخیره کنید، بعداً حتما یه جایی به کارتون میاد :
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/135985" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh7Qw89i_dZIsQz3AxnghPSPd2_kc799KTb5KQ-mOlrPHKP7Hj7hoo8hZ9taeG1z3jmnmaaYl6Bqmv-4_lNuPP-vwRQdVaW3QAiCiKRHd-fwLNmwIYCeiQM46mCMMptpk76NjN4lgeSIXpdi0yw-QnW_KYDPX3LTBWtP5WGdpA2BV6MTLeYJaDhX_kiJhC3ybjzrNrbnCOWe9GI7Fc247bigs2_bbdttaLFAkB7-bY4ys0vNvmS9HNHeHNGsF-Kj6_ij1akqW_nBeC1wiqe7uxEcRp6420gFcgFjBALhO1FbtwLprsqy0Mb8M8v9SvN5pKqdK4xAduXkEdYLV5XMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
فیروز کریمی :
میمیک صورت مسی رو ببینید داره الکی گریه میکنه چون دید رونالدو گریه کرد و وایرال شد اونم همینکارو کرد !!
@AloSport</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135984" target="_blank">📅 14:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrHpnVquIcq09ldEOXdkJASBE6pCJoyBNFHZWZyyItKIsF4aWbogtwr3iDZAaaeutVKzebvgvNbkBkl9OmunQtWAF6FddB-mV4yDb49EbkMJBh02u1gd1MQXLzWQWhVQXawWlHZ1zJ_3bcOn5dkQhH9oKjEEDLWhWOzrayMnjeT0v8h7C4SKiw7url8zyvn1Z_msc9KSDOjrWLjvbyXzFKXAZlG2yksdrs30RWKMSTmQrP0NDvUM_JBuROTBHwYBFy90IqdUf4GOfkKNi83M4BL2esaDhCCHDFisGKvwa73IhGdhAJK_z0P9Uswez3gFSnw-dhVGRxZm3p5GAnLIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBmMLcI0U9bW7ZHpqcK-N2trnquh_vrD0bQjjg8CFutpjpZreiNsiNNzUkwV6wS8uYxd939PHbVIYvtuOdu3YW121UdvxrgkfdvRJsit-Gtz9pisNxs4ntzNOB3eN9fVAAqwJPX-9hIxeKFZ04prQ5hTuEWakTTkuLOgUuuf_-qTwm1PRU8J20Gr3IKLe0BgQd0baJq3_BGJ343FoNnFBO0sU6JWGEkCrrfzV62rK98WCQ2Xs2YP5AHAJZNYptG6T8nDhJkJyOexWuLsg6eEqEbz_dGPK9Ge9_lbCKGEy7-zoJfetjy5cSX3DO609cylSP-JB5hrTYewYAORewV5Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کامران غضنفری با شکایت حسن روحانی به حبس محکوم شد!
🔴
دادگاه بدوی کامران غضنفری، نماینده مجلس را بابت هریک از دو عنوان توهین و افترا به پرداخت پانصد میلیون و یک ریال جزای نقدی و بابت نشر اکاذیب رایانه‌ای به سیزده ماه و شانزده روز حبس تعزیری محکوم کرده بود. دادگاه تجدیدنظر اعتراض متهم را مؤثر ندانست و حکم را عیناً تأیید کرد. این رأی قطعی است و مجازات اشد قابلیت اجرا دارد.
🔴
کامران غضنفری، حسن روحانی را به «جاسوسی برایMI۶»، « ارتباط با سرویس‌های خارجی»، «داشتن تابعیت انگلیسی» و «افساد فی‌الارض» متهم کرده بود. دفاع او این بود که مطالب مطرح‌شده را از برخی اعضای کمیسیون امنیت ملی مجلس یا گزارش‌های مربوط به مسئولان دوتابعیتی شنیده و ردصلاحیت روحانی در انتخابات مجلس خبرگان نیز مؤید ادعاهای اوست.
🔴
دادگاه این دفاع را نپذیرفت و تصریح کرد که هیچ‌یک از این انتساب‌ها در مراجع رسمی و قانونی به اثبات نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/135982" target="_blank">📅 14:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1232873fbd.mp4?token=EtqaW0iS2Fnv5FGi-et-oV1AWIBGRB7NkAFQrk4hJdYguGj1oopyTaC6Xbth1VQNLoJfScnAe4fW4oBsAU7Hk2gc-4yhGkpRmQEG59-TSjKlPSTcNJKbyBiRc028s9K-5qiYLz8unu_X2RJPzA_LLbjugUdnJnhB_ySIt6eHo_M3E4uppwVIwUxivnutSbzQi-EIgJTSvRSP58_xpxsdvqfsQy01Mni0RF-wqA_T0yMFiAMjlP5GXwMpqFD1InhD7WgCcrcA4N3cp0OKJX1EyVoX5B1pqBduIH3JLkDlgibT_VFsI7mx-26dLRaMsO3qOzebjEIzvTUU2JS0pWcCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1232873fbd.mp4?token=EtqaW0iS2Fnv5FGi-et-oV1AWIBGRB7NkAFQrk4hJdYguGj1oopyTaC6Xbth1VQNLoJfScnAe4fW4oBsAU7Hk2gc-4yhGkpRmQEG59-TSjKlPSTcNJKbyBiRc028s9K-5qiYLz8unu_X2RJPzA_LLbjugUdnJnhB_ySIt6eHo_M3E4uppwVIwUxivnutSbzQi-EIgJTSvRSP58_xpxsdvqfsQy01Mni0RF-wqA_T0yMFiAMjlP5GXwMpqFD1InhD7WgCcrcA4N3cp0OKJX1EyVoX5B1pqBduIH3JLkDlgibT_VFsI7mx-26dLRaMsO3qOzebjEIzvTUU2JS0pWcCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بندرعباس - دی ماه ١۴٠۴، حرومزاده های حکومتی که جلوی چشم بچه به پدرش حمله میکنن!
🤔
بعد مارو از نیروهای خارجی میترسونن. نیروی خارجی با مردم معترض کاری نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/135981" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشکیان: درست نیست افرادی که هیچ مسئولیت اجرایی و نقشی در مدیریت مستقیم امور ندارند، خارج از فرآیند تصمیم‌گیری صرفاً بگویند که باید به شکل دیگری عمل می‌شد. طبیعی است اگر همه واقعیت‌ها و محدودیت‌های موجود بیان شود، بسیاری از این قضاوت‌ها نیز تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/135980" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پزشکیان: امروز در شرایط جنگی قرار داریم و اداره کشور با همان قواعد و رویه‌های معمول گذشته امکان‌پذیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/135979" target="_blank">📅 14:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پزشکیان: زمانی که تصمیم می‌گیریم در برابر دشمن ایستادگی و مقاومت کنیم، باید پیامدهای این تصمیم را نیز بپذیریم و نمی‌توان انتظار داشت که در شرایط جنگ، جامعه با هیچ‌گونه دشواری مواجه نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135978" target="_blank">📅 14:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان: فشارهای اقتصادی می‌تواند به دستاوردهای نظامی ما آسیب بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/135977" target="_blank">📅 14:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
پزشکیان: از هیچ‌یک از بندهای ۱۴ ‌گانه عقب‌نشینی نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/135976" target="_blank">📅 14:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان: امروز بیش از هر زمان دیگری به وحدت، همدلی، تصمیم‌گیری مبتنی بر خرد جمعی و همراهی همه ارکان کشور نیاز داریم و دولت نیز با بهره‌گیری از همه ظرفیت‌ها، اصلاح ساختارهای ناعادلانه و خدمت به مردم را با جدیت دنبال خواهد کرد.
🔴
پزشکیان با اشاره به مسیر دیپلماسی و توافقات انجام‌شده: برخی بدون توجه به واقعیات، مطالبی را مطرح می‌کنند که از اساس مبنای درستی ندارد. گاهی نیز ترجیح می‌دهیم پاسخی به این اظهارات ندهیم، زیرا بسیاری از این سخنان با واقعیت‌های موجود فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/135975" target="_blank">📅 14:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859193bada.mp4?token=JojL1lwNQXUxV3f5_itf4e6pTSANNor87dhnTEIv0RCGfXNvJpJknAwoO_JXGVWbpIvibSvFMcE-JiLW3CYOGYht_dOz-33V7dQe52Ktco6k_w9P_QRzogex7N5ezG3wFAl1elx-qaN6_HkBOiP9YvRtTqpOwZogwu8kFtw9uT2jpsIXu091624BgPmWTHcKy8i8b8qAjZzLNnteZQO2K4hplruCEFhDdtpDtCwKDP_3wmNme1T1Yr5tdRbSyhbHq7NIN-GbvKkiUvMHplzVQ_lWLor3bUggCQ2l4kRvbIFFZTu5920HnQGLbfg6mdkZMT8jjjlmgkS23BiRLIdBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859193bada.mp4?token=JojL1lwNQXUxV3f5_itf4e6pTSANNor87dhnTEIv0RCGfXNvJpJknAwoO_JXGVWbpIvibSvFMcE-JiLW3CYOGYht_dOz-33V7dQe52Ktco6k_w9P_QRzogex7N5ezG3wFAl1elx-qaN6_HkBOiP9YvRtTqpOwZogwu8kFtw9uT2jpsIXu091624BgPmWTHcKy8i8b8qAjZzLNnteZQO2K4hplruCEFhDdtpDtCwKDP_3wmNme1T1Yr5tdRbSyhbHq7NIN-GbvKkiUvMHplzVQ_lWLor3bUggCQ2l4kRvbIFFZTu5920HnQGLbfg6mdkZMT8jjjlmgkS23BiRLIdBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیِر استارمر : من برای اندی برنهام آرزوی موفقیت دارم. او از حمایت کامل من برخوردار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/135974" target="_blank">📅 14:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494c3c2054.mp4?token=PZetjf2MpKeS-zYavTOk3aLw6tXzX5EO7jbcob0dvYwrP3HoX3Y70slqh0syDl7TGIqW3bsRwWKiotYtXVJ_aIgDAJQ0-RzWw8fcUH8TQIemjIdK2hE64fw17mAb_QmSxhbxQ5nFvQIPQz3QLMg9oEf6UDoiFDa7E5BI6cLBjaFZkjSqAyKKHoKkFENKiXBIz6I8Ux5lEnA0ANo1k93d9jdeIVGDAqouZPKMPk6C8mva9ebJ3_yNz2v_C-3B4BNPPjybKKY_ieu0cNCJWvNSfG8FtpbDw7LuxOhjzRKaCX31rW4kk1IgBLDvG4Iv3oa3DE0txmToRv2e9UCX1E-Cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494c3c2054.mp4?token=PZetjf2MpKeS-zYavTOk3aLw6tXzX5EO7jbcob0dvYwrP3HoX3Y70slqh0syDl7TGIqW3bsRwWKiotYtXVJ_aIgDAJQ0-RzWw8fcUH8TQIemjIdK2hE64fw17mAb_QmSxhbxQ5nFvQIPQz3QLMg9oEf6UDoiFDa7E5BI6cLBjaFZkjSqAyKKHoKkFENKiXBIz6I8Ux5lEnA0ANo1k93d9jdeIVGDAqouZPKMPk6C8mva9ebJ3_yNz2v_C-3B4BNPPjybKKY_ieu0cNCJWvNSfG8FtpbDw7LuxOhjzRKaCX31rW4kk1IgBLDvG4Iv3oa3DE0txmToRv2e9UCX1E-Cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیِر استارمر، نخست‌وزیر بریتانیا (در حال ترک سمت): من با آرامش، با لبخند و با افتخار از دستاوردهایی که به دست آورده‌ایم، این سمت را ترک می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/135973" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری / الحدث اعلام کرد که هواپیمای نتانیاهو حریم هوایی اسرائیل را به مقصد نامعلوم ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135972" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت بهداشت جمهوری دموکراتیک کنگو اعلام کرد شمار جان‌باختگان ناشی از شیوع ویروس ابولا در این کشور به ۹۳۰ نفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/135971" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXgc6BJdY33FtxUh3_Pivm0wy5hjpb37s4VL4UKbppWZsCBzIN08FzmTu24dAYAqO16j6BFKAhjFfLd72oOrJ7e22VjcXaa68HWqc9NwhGp0FKzfgAm0Tcfv_QOYMsH8tYo-HazoXeZFdEg7kYJAMTjkTQn1A_OownRNtDQG00em-C2C0QWl18uYga6pHs-43dLMdzc9JnoS1V4sLFsDKL3cHq3m9MA80iTPybUG50GzaFpeD59RNp-qQPioQZE32_utt6dsDAGrnPevjhbn2301ru6o_6XxSPQtWpU7S04lRtQIz42Jfj-ALz6mN_9jsjKI8qgsKn0EV4opESaU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از چهره مسی هنگام دست دادن با ترامپ که در فضای مجازی وایرال شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/135970" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0116054239.mp4?token=Jh7NtsHcBa6C4LRsdYQ2qY2Si-ljJNiJqu8TA4A5hUttaiDy7iqnMsg1R6iyTBqKIc0gFxqop08lI3f245nqnBq3HX4mDqFd3qzuvCShygRrrcThVMIEySTMOSbTWZgkqhsRLKw2x9cFwJRPdZNqW7QWN-utaEktNiAj_B6Qdr_IW6o1WVPisFl4hiPVSIhFWNvdtMMN_6B14y40s80VbfQOdurzGcz8WJhqQjDsJemafh9m9REBMlcjyd3MgHFUxkiyQtXYT3TKP-ABulJ0HuEqH72SWuSfbzWOLQOwpaG66HfumbwaTZGH1o0me_ycALs_fDb--WBOZu01hUADag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0116054239.mp4?token=Jh7NtsHcBa6C4LRsdYQ2qY2Si-ljJNiJqu8TA4A5hUttaiDy7iqnMsg1R6iyTBqKIc0gFxqop08lI3f245nqnBq3HX4mDqFd3qzuvCShygRrrcThVMIEySTMOSbTWZgkqhsRLKw2x9cFwJRPdZNqW7QWN-utaEktNiAj_B6Qdr_IW6o1WVPisFl4hiPVSIhFWNvdtMMN_6B14y40s80VbfQOdurzGcz8WJhqQjDsJemafh9m9REBMlcjyd3MgHFUxkiyQtXYT3TKP-ABulJ0HuEqH72SWuSfbzWOLQOwpaG66HfumbwaTZGH1o0me_ycALs_fDb--WBOZu01hUADag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: ادامه فعالیت بانک ها ناسالم و ناتراز را تحمل نمی کنیم/ مهم‌ترین ماموریتی که برای همکارانم در بانک مرکزی تعریف کردم، کنترل ناترازی بانک‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135969" target="_blank">📅 13:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=ZGaI1_J7BC3F5ZXnjDmA_uVwHx4mtL_HAwvZYUV8OHSzCmhZpbk4h_0nGsc7-Iy1XQ3TkPFAy64K5_rrI_DfRIFgUknME8tIg-R5at0DgtH-Z42dp-G369VlV6a27mad3cQsDsFQQpWFVdangGKqwcasVyk0KEFBvpoP5HexZyyZM8CpivvlQaO3ICqtDqjN4e6EiGWnNuSJ2lInZx9dumlu1VeBSsIu0xAp1r2P-77uQsUg76Ctw9TSK9ZryS7wUHNme7Uj1hrZRwTCQJqkWBcX3PU6s_mAnbNlUmL2M3uMg86a4lCzNof_N4AMP4_t5CmXaVwx3OHGjULge4S2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a594ec6809.mp4?token=ZGaI1_J7BC3F5ZXnjDmA_uVwHx4mtL_HAwvZYUV8OHSzCmhZpbk4h_0nGsc7-Iy1XQ3TkPFAy64K5_rrI_DfRIFgUknME8tIg-R5at0DgtH-Z42dp-G369VlV6a27mad3cQsDsFQQpWFVdangGKqwcasVyk0KEFBvpoP5HexZyyZM8CpivvlQaO3ICqtDqjN4e6EiGWnNuSJ2lInZx9dumlu1VeBSsIu0xAp1r2P-77uQsUg76Ctw9TSK9ZryS7wUHNme7Uj1hrZRwTCQJqkWBcX3PU6s_mAnbNlUmL2M3uMg86a4lCzNof_N4AMP4_t5CmXaVwx3OHGjULge4S2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: اجازه اضافه‌برداشت به بانک‌ها نمی‌دهیم و هرگونه اضافه‌برداشت منجر به عدم صلاحیت مدیران بانکی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135968" target="_blank">📅 13:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgX1RJ1AbcVMGmUWb0r-4zR-IXULxm0AlvizXtsYo0cBRJQEUq7et33h8R401QIWiidtQNxZH68k1WJf6gYm5xBLkGly6VTceK7SFFdHhTffkAn4ghGC4U1cvTdivpbU4D9Fxl2itaEvdPoHw0M4FC9vbuv6allKUNTV0AbQGtwuN3vynnqUz7X_djrowUqpkjaKWydb1ELouyeff4PBWRBA-AEmNILcuQoeCmkEIaoDGT7N-7mLxD1vNXmo2yjZ9Be28JS5WB5AdKFezcRBJtPu19UDd--rf4dNKdGalCHLMwEesPGyXvY81bnNpeLc1Oz119hs2HkbZe3cmAnt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرپرست وزارت دفاع: جنگ و تحریم، موتور جهش فناوری دفاعی ما هستند. در جنگ ۱۲ روزه که یک جنگ فناورانه بود، با وجود بهره بردن دشمن از بزرگترین شرکت های فناوری دنیا ، ما پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135967" target="_blank">📅 13:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTcX_v9GFtgoSfsoU9u1PviXslhMxD3HeEZPVE3jm3HnqqdcTN0Khrof1tihDujMYIk4VRWEWFyB51BihY1sLvTnhqj2Kl7IsDm2QAayVo5o0msztWBZN_p71pRHIImSFyeUSab7Sp103cfayYJIzck0rce829vw4Wz0jwfAhti5pUXzUHxfp_hV11ZLPywgu3mKdBnKKhD9CK6r1QvgyIEDJhp8hCLc4f1CWuXV5UAc9CLwdf_Vc-i9X4TF1hlXBoIPjmeIrE46g9zmRykiJj5CC7NFDumcA6-yW7XMGCMEow30nbbJBLsVsrve_dTwodyGaMfcY2O9tUtdZ2OutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز دمای احساسی زیر آفتاب تو تهران به ۵۰ درجه تو قم به ۵۷ درجه، خوزستان ۶۰ درجه و هرمزگان ۵۸ درجه رسید و روز گرمی تو اکثر نقاط کشور داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135966" target="_blank">📅 13:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نیروی دفاعی بحرین از رهگیری و انهدام حملات امروز هوایی ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135965" target="_blank">📅 13:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I61yWgSDBAcOTxty6vzUD5gxMrkAvE0yWBCPFNd357c9ljFIZGoqoCNxMF3qto5IeJjpXB0ShQ7zfvS_mCkwcZMuMKmzZAfvBmnUlMnOUYwmGoFp0yTyPCQC8YPQcWUrBhL5CN393gn2HIvwyFS67phGv-4VtoT_-7fNfWWHSCKBaL-4Gjyj6G8HwRA7BIiti6nENeGREGs7OQYeYu3v0L1kHKyD0C2ctC1Rm1evZjHjWEByncOKNo35huSMVHNDI4rkMPzT8PL4SSQEQvoq3NTXJZkunuqrsGaBBpnyf3y1o_YfmDwZkAgeJekmBya_lfkGF_5vKIPctavKDTpp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219af3c8de.mp4?token=vCNm29v-nMBlc_FEKKZOT9urky2zFnv5Ikg3WjyizaiQcZZSKvgEPcsdKKOyLwfYHh-QF1U2XWBZNet9OOZ4_qC8ZuEDBxstYxZmrTyIZ2g-IQ9YTLgWHm4x8s1Z-kIcHjOYKFGgnO2GfG4pW3Q8IDRTJzkuVcE7f6SYWyYHGNOcaUnTXowvcwPlMD_UFOQUCQUhK-T0JJT8vf67Mqtr23VE_07xpu167fIfkVQmqTFAXNo0AFxw2YoxyGeMLO1chvH6dG9lP-u_8-q7a76b5MtdHXc_OieaV6Ys7PbdU0ykez8JQvsUyfmL1xjWGu6pU0voBQDEUBGaJlVpXdJLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219af3c8de.mp4?token=vCNm29v-nMBlc_FEKKZOT9urky2zFnv5Ikg3WjyizaiQcZZSKvgEPcsdKKOyLwfYHh-QF1U2XWBZNet9OOZ4_qC8ZuEDBxstYxZmrTyIZ2g-IQ9YTLgWHm4x8s1Z-kIcHjOYKFGgnO2GfG4pW3Q8IDRTJzkuVcE7f6SYWyYHGNOcaUnTXowvcwPlMD_UFOQUCQUhK-T0JJT8vf67Mqtr23VE_07xpu167fIfkVQmqTFAXNo0AFxw2YoxyGeMLO1chvH6dG9lP-u_8-q7a76b5MtdHXc_OieaV6Ys7PbdU0ykez8JQvsUyfmL1xjWGu6pU0voBQDEUBGaJlVpXdJLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های ارتش اسرائیل به غزه در جریانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135963" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafbeec7dc.mp4?token=LYnpdTtBhP2HhO8RaBcDGTn5IIb-vFawgn0E6lbSJ942ln5Ubl28RNnwhMV6hKUCuy-7jZbiVlHH6FbX_AWXCPWREuJMGdFJln6tbk-i5FMCLpi-wNKbDGl0Ub2-LCOZWgmTPnN0tuTr7JSRcgvbB_wsTaS2uKw6whGgMUMiVjmlJ6zgl-r9gyI1JTf4swRcGBK9cSO0N20HH0ZcRcFxXH9fnSYDn6XZ-Qnl8Y_bMY9BvLBBH1PZM7IDEkS-h4eykbw4dgFxrfSN4H93qSY5lifcc-JTN7hSvfHpN085Vr29Y84A71--4KsK7tHtkFNkn6HYY43QGp5PBAbpDn2Fm4cvULcv8AUqoTb9U1zPQBoRLdl3HnmDoh61uvEnRQ3AugD9NqOba8yQOdb3GaFxBk5VOdd2rhAjFU2W37BWvKakch0MFIRShIgUaCwu63LonbZj7K_BCwEHegoaXTt6y1Jvdr_j6Hhbbp8x6H7QhIKMXYa4Y_iKt3IXUMxelX74eZ2tGWTOMa39a_uuoTnph7nZ2uEQDaoAFb4oLHpfR4um9DdWZi7rhAx0DwaHms7cBTmtztXaFtFDo4XDXQUaXvHzAkLIeksOqqOOKGT8eGpOR9NXOPwJguMgRGLgO0aSKEeN-CQ9H4y9UzOFTyNEuHXdESuJRqPsLZc-obbIjqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafbeec7dc.mp4?token=LYnpdTtBhP2HhO8RaBcDGTn5IIb-vFawgn0E6lbSJ942ln5Ubl28RNnwhMV6hKUCuy-7jZbiVlHH6FbX_AWXCPWREuJMGdFJln6tbk-i5FMCLpi-wNKbDGl0Ub2-LCOZWgmTPnN0tuTr7JSRcgvbB_wsTaS2uKw6whGgMUMiVjmlJ6zgl-r9gyI1JTf4swRcGBK9cSO0N20HH0ZcRcFxXH9fnSYDn6XZ-Qnl8Y_bMY9BvLBBH1PZM7IDEkS-h4eykbw4dgFxrfSN4H93qSY5lifcc-JTN7hSvfHpN085Vr29Y84A71--4KsK7tHtkFNkn6HYY43QGp5PBAbpDn2Fm4cvULcv8AUqoTb9U1zPQBoRLdl3HnmDoh61uvEnRQ3AugD9NqOba8yQOdb3GaFxBk5VOdd2rhAjFU2W37BWvKakch0MFIRShIgUaCwu63LonbZj7K_BCwEHegoaXTt6y1Jvdr_j6Hhbbp8x6H7QhIKMXYa4Y_iKt3IXUMxelX74eZ2tGWTOMa39a_uuoTnph7nZ2uEQDaoAFb4oLHpfR4um9DdWZi7rhAx0DwaHms7cBTmtztXaFtFDo4XDXQUaXvHzAkLIeksOqqOOKGT8eGpOR9NXOPwJguMgRGLgO0aSKEeN-CQ9H4y9UzOFTyNEuHXdESuJRqPsLZc-obbIjqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمهوری اسلامی نقض آتش بس کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135962" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر نیرو: آب‌ شیرین‌کن‌های جنوب کشور همگی فعال هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135961" target="_blank">📅 13:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نیویورک تایمز: پنتاگون، ده‌ها مورد از جراحات سربازان آمریکایی را که در جنگ با ایران رخ داده بود، پنهان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135960" target="_blank">📅 13:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoE8k20Dp9X3Qp5SMRasZs7aDBCvzT_m5_Sia62FiLnuqAX2iEWlZJlmWoQYKZ6e5YZKzu3WdU32adTeqA4CbQcc47tnO1y-oN_11yNvzLPZ5RhDxBac7RTHf8dv29Jkp6XK4srPU0Z4Ukf9neaeEYmGi0rmAvC0zoI3ATooMWbKcpl5OvdIX0bBZ-8yPoENrgolWdyY_BMVBJfb05MWC4Y07ml7pVk_y3t6wQjs_weCQbXsv6Z3FAeLSf7fUUwZVEtqK7SoNy1U2vqR0DDZhMo6V7_1kMlahKEVvC_NYxzlTlLIlXNffaDGAMWw101rY8j2x3_8CBHChSeumK3Pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دیشب در جشن قهرمانی اسپانیا، تا لحظه آخر، قاب قهرمانی و بلند کردن جام را ترک نکرد تا اینکه اینفانتینو اومد بردش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135959" target="_blank">📅 13:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b53f8115.mp4?token=kNqt7qsWvKQCjQ00vAkXQB0CGURtWRCSvb6CyBzAmJdiA-bPFkKLID9Y7-loigdLKKnT3J2_14yegedJYPE_YLd_mlfxmW-jRDdWdEzijXF2ZnNwkxRfOWVH2uLqpVx2mB5knnwlLf-ySV3oIPuZepmicaM4FCYO8fZERWeZzKwQgy69b0knKMwyMTW0NBrDFvMHd-ExEmpCAOW6YIN6vPtHStMV7utnd_ItYJ-ZfcBbhkpTCXkq0K8UysJNYii3Ge-ZH42v4uYPjNL1xGV943s8jKiX0PjjzHyTjWcqh4p5CYkdWZ6Z1h2-qfMQ4H2t52TO1Fc4Ff8UZ1l1AmwM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b53f8115.mp4?token=kNqt7qsWvKQCjQ00vAkXQB0CGURtWRCSvb6CyBzAmJdiA-bPFkKLID9Y7-loigdLKKnT3J2_14yegedJYPE_YLd_mlfxmW-jRDdWdEzijXF2ZnNwkxRfOWVH2uLqpVx2mB5knnwlLf-ySV3oIPuZepmicaM4FCYO8fZERWeZzKwQgy69b0knKMwyMTW0NBrDFvMHd-ExEmpCAOW6YIN6vPtHStMV7utnd_ItYJ-ZfcBbhkpTCXkq0K8UysJNYii3Ge-ZH42v4uYPjNL1xGV943s8jKiX0PjjzHyTjWcqh4p5CYkdWZ6Z1h2-qfMQ4H2t52TO1Fc4Ff8UZ1l1AmwM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه‌های سنگین عادل به قلعه نویی
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135958" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90c8a06ce.mp4?token=g5C7GiBxLVo448SJlm4sGiYJ-g-9pOVbmVHemNFxDO3c0l_BRtt6uTrRfjNV7mVOz_G6gS7MpMFUvCdAZnZJ6RdOmkYqYMFhS9gjZirtxabX7vRL-gWDCryumUmoc_txyDKj9t4RHf3Qh-lYNSzb7-_luA0n4SlzFaK7unBUMMYYCBxpf1VfntGtE4tLIpbNRaYNCepMq3kPdzLfWcxbrdbzrf1lsFIGyp-ca9V-vjk_ivMWsI_g1xt9BfSs3O2FzjU9tNUe3prv0_2lJu5Qzia7k0B1vGuZMmQjg46QhhPyQ8qm4i1Qs1rLXGu_PS84cco6nZsN3-fsdfVeTVwnxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90c8a06ce.mp4?token=g5C7GiBxLVo448SJlm4sGiYJ-g-9pOVbmVHemNFxDO3c0l_BRtt6uTrRfjNV7mVOz_G6gS7MpMFUvCdAZnZJ6RdOmkYqYMFhS9gjZirtxabX7vRL-gWDCryumUmoc_txyDKj9t4RHf3Qh-lYNSzb7-_luA0n4SlzFaK7unBUMMYYCBxpf1VfntGtE4tLIpbNRaYNCepMq3kPdzLfWcxbrdbzrf1lsFIGyp-ca9V-vjk_ivMWsI_g1xt9BfSs3O2FzjU9tNUe3prv0_2lJu5Qzia7k0B1vGuZMmQjg46QhhPyQ8qm4i1Qs1rLXGu_PS84cco6nZsN3-fsdfVeTVwnxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: «ایران کشور ثروتمندی است. یکی از دلایل نابسامانی وضعیت ایران این است که هر پولی که این حکومت به دست می‌آورد ـ چه از طریق کاهش تحریم‌ها و چه از محل فروش نفت ـ صرف حمایت از حزب‌الله و حماس می‌شود... آن‌ها باید میلیاردها دلار را صرف آبادانی کشور خود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135957" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75666bc36.mp4?token=HxjOZZVhwc2DhX6e9Kwumqhe-lBJue_6m--70rztJptEo6p45StjUaIvkwByWY89AErKwlNkwpzW_G8PBq1spYGybaXdC0QjoAPOkDNw96mO2DP_L96rc4Pf67WUomqg051w6xTP8C0Yh66oNR-KiRSKqSyd-GQ7diyNIBIi1wgEQhvrGy1GrG0sQe32FaKsZRQCshSxSBGjTQdWR8q38z0yXXrQrWzJZavszpyyzIgiTdZTapBo9L4-3Dn9D3qmre5Q70Xy5i94_Vy4dwwo8MuCNwtJ-eXuYhSRD67y3int65tslM4idmg-T1jvE8cLUrl62Ambdiz01pt_WADbZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75666bc36.mp4?token=HxjOZZVhwc2DhX6e9Kwumqhe-lBJue_6m--70rztJptEo6p45StjUaIvkwByWY89AErKwlNkwpzW_G8PBq1spYGybaXdC0QjoAPOkDNw96mO2DP_L96rc4Pf67WUomqg051w6xTP8C0Yh66oNR-KiRSKqSyd-GQ7diyNIBIi1wgEQhvrGy1GrG0sQe32FaKsZRQCshSxSBGjTQdWR8q38z0yXXrQrWzJZavszpyyzIgiTdZTapBo9L4-3Dn9D3qmre5Q70Xy5i94_Vy4dwwo8MuCNwtJ-eXuYhSRD67y3int65tslM4idmg-T1jvE8cLUrl62Ambdiz01pt_WADbZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه امریکا: فکر می‌کنم جهان به نقطه‌ای رسیده که مشخص شده ایران — حداقل برخی از افراد در ایران — می‌خواهند تنگه‌ها را کنترل کنند و از آن به عنوان اهرم فشار علیه جهان استفاده کنند
🔴
و جهان باید تصمیم بگیرد که آیا می‌خواهد یک آبراه بین‌المللی تحت کنترل کشوری مثل این قرار گیرد یا نه.
🔴
این کاملاً غیرقانونی، ناقض قوانین و غیرقابل‌قبول خواهد بود.
🔴
آمریکا به انجام آنچه برای محافظت از کشتیرانی جهانی لازم است ادامه خواهد داد، اما کشورهای دیگر باید شروع به گام برداشتن کنند و چه با تجهیزات و چه با تأمین مالی، به تحمل این بار کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135956" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7J03B_fjC-0-UTTs0H9MEWad-Slthh7tsRM6Ac4uwfW00ePj6_TcVMyX4saXoO4KE4D5iCPUDvffrMnNq_r-eAO31WfH0-84r0zd8eNN6diuyrHJHgG_HagDwz2FAYhORuNrcfH6RLAGz3jag5gYrazVQ-T3-MDKZ87xCFr3-Rq-oA01nqCjHWyzebuIuWzDFp9e2h-ssYqmcnAEyzsu4LF7p2LC7AzHnmjvNXtyPXo9fjQ9NbOSGCk7uxC6rWODJa1c1-GLqTGGceXyX49TxymoegtozVWsk6gB_iicDTjU80cIC69ygDR-Ocu2N7I2QVQ40sJ4cFj8VgYdbwZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو یکی از جاده های اصفهان زمین لریزید بعد این دود بلند شد
🔴
مشخص نیست دقیقاً چیه این
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135955" target="_blank">📅 12:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a6ff1db.mp4?token=jYYE_UhYpwAhuzkDMIxGWcv_wYD5QAzxhAXJPLxcaJr9FSXxfZrhfex5hsb8bXjkA4U1iwtoTaqE7yXhzhcXGTcyHNk5f772yj7I5q_M2r3zu69Hq6ElK5_pTNLGrOI713lYulV3HXjobhUuQic00Mdh9Phn0PykaER7KR6Fl-VII662LjStaUrqs3lvDybJhGNURfnYUxAK3hGy7b-edguhfxmTTyAHcHpx4BGhKXUjvdGNFRmviVpxF07oAA4fkld7P2fkiB-zrGk2uY-5_VjWb2Ak3YIjVG8ltSFMdReEhzYHtSE8qM7lgWBITYKdw9fY3FbZ-6fn1bMrbuKwdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a6ff1db.mp4?token=jYYE_UhYpwAhuzkDMIxGWcv_wYD5QAzxhAXJPLxcaJr9FSXxfZrhfex5hsb8bXjkA4U1iwtoTaqE7yXhzhcXGTcyHNk5f772yj7I5q_M2r3zu69Hq6ElK5_pTNLGrOI713lYulV3HXjobhUuQic00Mdh9Phn0PykaER7KR6Fl-VII662LjStaUrqs3lvDybJhGNURfnYUxAK3hGy7b-edguhfxmTTyAHcHpx4BGhKXUjvdGNFRmviVpxF07oAA4fkld7P2fkiB-zrGk2uY-5_VjWb2Ak3YIjVG8ltSFMdReEhzYHtSE8qM7lgWBITYKdw9fY3FbZ-6fn1bMrbuKwdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانیانی که تا کنون با برند dior همکاری کردن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135954" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
یدیعوت آحارونوت: نتانیاهو، امروز بعدازظهر جلسه‌ای اضطراری با کابینه امنیتی برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/135953" target="_blank">📅 12:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا:
هم اکنون حمله موشکی ایران به یک نفتکش عربستان سعودی در تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135952" target="_blank">📅 12:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm4h-dX7shIxEcxN4Gy_2Yg9NlmGll-h5Rornuo6whcTKeMU-08AGqT5KSPuuF1kP25JFA34g00isj6cPXeq0o2YxQm9vTRBPZb32xUMvOfvPQTrDHkti04uXjP7leE6IKsPItZZwqdIeScaHDeoS8bPdLemIVF9neIYE42ZcY5GPGZqKmpiLfIreFTRQvzT7MRpvIRwLGna6u_dxiuy7pRSDur9TlGK_zLMaU3ysWmOz2kOOu-zuMMQKFKiJT00aqQFc4zO0PR7bNs7bZY21MnHDW0WKuyRVLGdKwqUquVrZKBx51tHPnK7m-k2mVQirTrrSKD7eLWnJkq19o8V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستوان‌دوم مهرداد پاشایی، از نیروهای پدافند ارتش، بامداد امروز در پی حملات آمریکا به تبریز جان خود را از دست داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135951" target="_blank">📅 12:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQlxX4Rx-B8rY5dmyv1GrKThX9K60QsSGdW3iX3XCakvGWJR0pg5iD6_Zhzs3uyPlpgs4F01WY8bKtoLme6NC9W9OX--pHwtSx9V2V04MVH8NTrtHkAcS2c6i9wx5JmFusYH6my42JaiwdcHO9uYC1QR0XeiIJIV9Ap3K6pvmZ8p2JBouP6kWxY6WbZSu8ZwsDTQOKgXL7vZuh7h5ewLNmFUfdqEAF17-d2Pk6ACQPI2sWKVHbMl5uX_c1ws_0Hp1Qnnv4JhNKuuhqa9xJhA_TiGJvn-dpfTJWHDgEW5ASCy_gMkBQaasczXJoyEwjnIaMXoVSbXHPQvrs0FnTHmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
چطور شما حرام زاده ها به ورود حشدالشعبی، فاطمیون، حزب الله اعتراضی نکردین ولی از ورود نیروی زمینی آمریکا مثل سگ ترسیدین؟</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/135950" target="_blank">📅 12:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روسیه: آماده‌ایم میزبان گفت‌وگو بین ایران و کشورهای عربی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135949" target="_blank">📅 12:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRQs6tPqLpcxwLH43cB4cLZn_if4Ir4Fv8GUWsaDGcN3jzd1NeKgpAzEAI5pYYal_PCvMglDeqBGowT300RpSFcPv-Iv9HQ0NqagkAptwHc8g1dpby7iKa2LMOg5xPd7Lqzv1CrwU5tUVLwcbU4IsKqJX8x3NBVLGTEzVFwIQZAJTTsmUNXOqySRKLeUUQW-ddVnFYmlAFXjj-o8_veUYg4vw7mNNDZD3z28kncKmacwU-w9ZaH-n-Y-Vy0SGQllNVuS49GqYkXsF4RuwAVR43CbB8-QFbXFLzuzv3WnaQqOuwN1YMJ62MS0ZLzcaEKki4eq9ES7-g34xGSxuxmSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۵۸ هزار واحدی به ۴ میلیون و ۸۱۳ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135948" target="_blank">📅 12:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae713a91f.mp4?token=F5S1EK7P9kXkSbJ8dJkgkBv9bs5lStklbIpozxY4cwV-89yn2cXmkmko3QnAx3LSZfTVwH4uURB8D9Kv7yPHfc0SetQdnlg_IKcqH7spgO4-wsa_2rkhw_D2rgsvfieaMRNuZd2y4KINebLY-DoNhkG9oa8AoCkDR4hNML7MlbtLi9yFmhFy0wBY2DeBhJzQMneyAo8BVKRW2g9fogmnJ4g5hDWaVx_yymLOHkpeM6AurJIAlB6AzQwilbmhZPEsVE5jWtktoclgJjDdcpps3vs5WFqYWGU_Qte2GczVtyrfu7kloqVRBEaoaET0lngXg_zsjmxYkHpXluePa-LhuWvV7b62Pp0uJT6FJOaO_qAYXlYpVnG6ltRARPLqzp4_sB_hQYFpnzqlLOcRZQaqV0DCtQDbWVxnmb11-e9eU2-2lDoMcE-3jz6ps1uC8gU-s5xmkA9L_wEes8iCXiGmCogFz2a8vpH8hIbAOHAHXxePvs9YkBFiXv8vVUI2YRrc7fZjHsQgeiT5nMLEwyp-rOAh-l1vP1B0UdNbLSSIdOvn7dFdzc0hhaesLX7jKCJPbe385PtTT61EQ1XzgzzM55JByXVJa-6eCUknySt8nw1srI6rc7LovoVhiVhRh3hjJ4esioO-FOKl-wNLUklQ3rT5pm2gnaLTK0PCaZteM-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae713a91f.mp4?token=F5S1EK7P9kXkSbJ8dJkgkBv9bs5lStklbIpozxY4cwV-89yn2cXmkmko3QnAx3LSZfTVwH4uURB8D9Kv7yPHfc0SetQdnlg_IKcqH7spgO4-wsa_2rkhw_D2rgsvfieaMRNuZd2y4KINebLY-DoNhkG9oa8AoCkDR4hNML7MlbtLi9yFmhFy0wBY2DeBhJzQMneyAo8BVKRW2g9fogmnJ4g5hDWaVx_yymLOHkpeM6AurJIAlB6AzQwilbmhZPEsVE5jWtktoclgJjDdcpps3vs5WFqYWGU_Qte2GczVtyrfu7kloqVRBEaoaET0lngXg_zsjmxYkHpXluePa-LhuWvV7b62Pp0uJT6FJOaO_qAYXlYpVnG6ltRARPLqzp4_sB_hQYFpnzqlLOcRZQaqV0DCtQDbWVxnmb11-e9eU2-2lDoMcE-3jz6ps1uC8gU-s5xmkA9L_wEes8iCXiGmCogFz2a8vpH8hIbAOHAHXxePvs9YkBFiXv8vVUI2YRrc7fZjHsQgeiT5nMLEwyp-rOAh-l1vP1B0UdNbLSSIdOvn7dFdzc0hhaesLX7jKCJPbe385PtTT61EQ1XzgzzM55JByXVJa-6eCUknySt8nw1srI6rc7LovoVhiVhRh3hjJ4esioO-FOKl-wNLUklQ3rT5pm2gnaLTK0PCaZteM-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرگونه شانس ایران برای دستیابی به موشک هسته‌ای را از بین بردیم
دونالد ترامپ درباره ایران گفت:
«ما در ابتدا فقط در حال انجام اقدامی برای جلوگیری از دستیابی آن‌ها به یک توانمندی خاص بودیم، اما اکنون کار را به پایان رسانده‌ایم.
🔴
بنابراین، موضوع کاملاً متفاوت است. کاری که اکنون انجام داده‌ایم این است که هرگونه شانس ایران برای دستیابی به یک موشک هسته‌ای را از بین برده‌ایم.
🔴
اگر فقط یک هفته و نیم یا دو هفته بعد به نتایج نگاه کنید، نه چهار هفته بعد، خواهید دید که ما آن‌ها را متوقف کردیم؛ احتمالاً... البته نمی‌خواهم از واژه "احتمالاً" استفاده کنم.»
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/135947" target="_blank">📅 12:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662307f341.mp4?token=JKW9a3inSyxfNweItiWDaqt--eNxkaCeTM8zXQPd9OszOb1ZUtu7_GY5C_uKaMaRX94lfz5XdMXnBZM-bng_kE5pFQ6t9u1Z5v48DNUPqNe8aM9dCzEdvHXTASoyrOsIUnOdVETszfA7ycaOVDlVYmO23_Ip2aB5TpfqfMk9LJ4F40su-0qNSKEDsKUOr3Pha5Gew6TsiQBCBOq53Aa9TSrhkK6zGDO1EIahkQIohLWihKMWZNOkdZHUOVKe01ZUUslTaqnhR83QI5tEHDZgVBqsi98uVe7RfHK0448ySzOU1xbOoXFDFY_VihOsqis0bwXP78aCUCzP3-NDk_EeWUGMH_LQb4R-Wjuw9X-EO6sxJIezZb-N7lhm17FlCQnMLlWAh-G7Pa3dl4P-tTmI5sOjIARlPg4Q86l9_uiXdtdJmg7OYgecJ3HIP5GKdKFyDFNMh3uWOEAFeZu1mXM2Y2CVrUxZtOAHfNzoHRro6U25hLDdnaXGlUNNlri7TBOyxrOJW79hNp1TgjmuoU41mGszft6EOUsd033kqj34xlaVVoeM7sC_E0EYk9SiQ2QTYmWGY6tRdIH9KXCikZtcNBQ2FCvAUTVUcm4aRobKVH_jzehBzJwZI9uPUgHLorMykIn4RaDMVgM1GqYtzY3HCWEaIqXtGtXp0_k1-1R_OYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662307f341.mp4?token=JKW9a3inSyxfNweItiWDaqt--eNxkaCeTM8zXQPd9OszOb1ZUtu7_GY5C_uKaMaRX94lfz5XdMXnBZM-bng_kE5pFQ6t9u1Z5v48DNUPqNe8aM9dCzEdvHXTASoyrOsIUnOdVETszfA7ycaOVDlVYmO23_Ip2aB5TpfqfMk9LJ4F40su-0qNSKEDsKUOr3Pha5Gew6TsiQBCBOq53Aa9TSrhkK6zGDO1EIahkQIohLWihKMWZNOkdZHUOVKe01ZUUslTaqnhR83QI5tEHDZgVBqsi98uVe7RfHK0448ySzOU1xbOoXFDFY_VihOsqis0bwXP78aCUCzP3-NDk_EeWUGMH_LQb4R-Wjuw9X-EO6sxJIezZb-N7lhm17FlCQnMLlWAh-G7Pa3dl4P-tTmI5sOjIARlPg4Q86l9_uiXdtdJmg7OYgecJ3HIP5GKdKFyDFNMh3uWOEAFeZu1mXM2Y2CVrUxZtOAHfNzoHRro6U25hLDdnaXGlUNNlri7TBOyxrOJW79hNp1TgjmuoU41mGszft6EOUsd033kqj34xlaVVoeM7sC_E0EYk9SiQ2QTYmWGY6tRdIH9KXCikZtcNBQ2FCvAUTVUcm4aRobKVH_jzehBzJwZI9uPUgHLorMykIn4RaDMVgM1GqYtzY3HCWEaIqXtGtXp0_k1-1R_OYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ گفت: «هوای ما به‌شدت بر اثر آتش‌سوزی‌های کانادا آلوده شده است.
شاید کانادا باید به ما غرامت بپردازد، یا شاید هم باید تعرفه‌هایی علیه آن‌ها اعمال کنیم.
کسب‌وکارها در حال تعطیل شدن هستند، چون مردم نمی‌توانند این هوا را تنفس کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135946" target="_blank">📅 12:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: وظیفه ایالات متحده این نیست که برای همیشه از کل سیاره محافظت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135945" target="_blank">📅 12:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1a0b1aed.mp4?token=ChaMIO8mnW8ocg7xQF5WTteEwoX2ddATNSSPLk6YNl2UrbPl5FQ9Gv9F5LjYVfdkBd8qgBM3ovm6cX_PZAm2HGy9J4f-_U6NteDPW7-chNVVraqyLs8tzMqjOXFn4ZR3gkWA04Tn6-XHBJ8w4qh9FZGsS8Ao_Ulujhvok-Cwdh-veaRFXF8yxUJD-cWVGl9wHo-jKGsiiQ5EvuMQ7cNU-Vq0en3iOMSfmEKR0wsiZ4rXdhFwqKULSJsZR9GKkFxkfbnE9Bi93NpT608u1TupywM6fPeD1smdkYgPwLuNUtZwiJAd7560Kjs0NwWHXnaHlDLSH6IkEqAb3sLYzKjd4ZSskAQKrGwLFvrVfBlYMW1vE9I4fAjrSEXKcKF9vO2Hsy1neklTeM7P0AMUT6wM6ZdfD61Pu8NLn2ZrOia2NE69lPHl5yzdD9G6f13r7U3R0MSMNcGrNFFxZY_2svFCQwSYUVwdp28NE4OIX9iMue47QdgIw8P2Qlj8-cBNkrKrJY4zT-nDjHOWylQKOsjLAKhPD5TFSNcZKECyc--8Imp6xPS0BYLO2E15Pmc-jzfj9Miy8gnu19nGFhcza_eLXNIE6QR2jhrOUW7FyGFSsQ252k2jxJRZtG_NszZZ7yW_QQwyTGaiJFX_YkX10toUBv3YM9_FOT54wkquepLCSvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1a0b1aed.mp4?token=ChaMIO8mnW8ocg7xQF5WTteEwoX2ddATNSSPLk6YNl2UrbPl5FQ9Gv9F5LjYVfdkBd8qgBM3ovm6cX_PZAm2HGy9J4f-_U6NteDPW7-chNVVraqyLs8tzMqjOXFn4ZR3gkWA04Tn6-XHBJ8w4qh9FZGsS8Ao_Ulujhvok-Cwdh-veaRFXF8yxUJD-cWVGl9wHo-jKGsiiQ5EvuMQ7cNU-Vq0en3iOMSfmEKR0wsiZ4rXdhFwqKULSJsZR9GKkFxkfbnE9Bi93NpT608u1TupywM6fPeD1smdkYgPwLuNUtZwiJAd7560Kjs0NwWHXnaHlDLSH6IkEqAb3sLYzKjd4ZSskAQKrGwLFvrVfBlYMW1vE9I4fAjrSEXKcKF9vO2Hsy1neklTeM7P0AMUT6wM6ZdfD61Pu8NLn2ZrOia2NE69lPHl5yzdD9G6f13r7U3R0MSMNcGrNFFxZY_2svFCQwSYUVwdp28NE4OIX9iMue47QdgIw8P2Qlj8-cBNkrKrJY4zT-nDjHOWylQKOsjLAKhPD5TFSNcZKECyc--8Imp6xPS0BYLO2E15Pmc-jzfj9Miy8gnu19nGFhcza_eLXNIE6QR2jhrOUW7FyGFSsQ252k2jxJRZtG_NszZZ7yW_QQwyTGaiJFX_YkX10toUBv3YM9_FOT54wkquepLCSvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «ایران آسیب بسیار، بسیار شدیدی دیده است. آن‌ها از نظر نظامی تقریباً همه چیز را از دست داده‌اند و چیز زیادی برایشان باقی نمانده است.
🔴
آن‌ها هنوز تعدادی موشک و پهپاد دارند و تا حدی توانایی تولید نظامی دارند، اما نه چندان زیاد.
🔴
ما کنترل تنگه را در اختیار داریم؛ آن‌ها کنترل هیچ‌چیز را در دست ندارند. باید ببینیم چه اتفاقی رخ خواهد داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135944" target="_blank">📅 12:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT1FQbrSvRVCYdg_LWQ5b8ZTB9ignTjYvmFF-368viNN5j_C_VBaNqF5K9VD4tzq6DPZfmRZ2_cygkPHhult-ACPPJCG6xs9IS0EJIrUN3ojYt98qT0FAxCY6VdIRPQNySPMYn71twlA-rXPMN1W2_3UVx07gYQHkIy9IJVQxIPe_JuM9VRA34n_DT8URmmdXYlkZJHxmTzm_j2Gaxn4RocQ5f6JkK3EXtdHmdnsud74XNp2JOdBWGuMHiVigGr6JRBzmlg5_YhA7cK1TkFLiDPksGrv3hDyj23sI58lgUauB8q7fr34SeUpVeHf-gXwxP18KcEA5T3wszHpYxYG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانشگاه علوم پزشکی لرستان: لحظاتی پیش طبقهٔ همکف یکی از بلوک‌های بیمارستان درحال ساخت نیایش خرم‌آباد دچار آتش‌سوزی شد که با حضور به‌موقع نیروهای امدادی مهار شد.
🔴
دود مشاهده‌شده در خرم‌آباد مربوط به این آتش‌سوزی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135943" target="_blank">📅 12:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQm00s2IobBVWUXF6kcsV9mrg-jvwiOIfYJMgpCQ31GHpkBWz-tkD2hOx-7YcL-cGQAioluFfzD11c4SNeaRNmVzkFh7TI4X-GYH-lh-FuyjKb5NJGzSz8QT1TseA1nJ-l2_YQ1atZozujtx_niDO_W01tg3dINg0jJrjWE5F8YWv1PqlJGju98_QpAd3gBFkx8u8EctwGI1ukAL0UX3W58KplgHSYDER-vZXXfAW6YPHD4keJoGAOGYWa7Gcy0_2T9FVnVhOzwv0rKciRSNAWVL3m2T5fBOlEknNlNGq7JTgWLBGD3lPVdGrI8G-lz8dxTwKltzbEaN0_ChUAtxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXcQszNckonLueOn0QCVenIHlb8uG9MdHzE8Ej5OXj8SPxDJykzH6JPBpxm5WZm-lHZYknyrrwgyXLyJlmYSyfv17Id4yjbGAwbhoPM_XkzBl0iPYE0j-wRMAnGsfmTOAWduQVYKjMhKZaW_LpaZoAI4H5k_lQg9ye5pGwBnlViqbqa17fZoGp4nYBJFE1S7kVwogVXVsDbYDcRUbGUTG2mYznUptya0Tnb59Ub-CV7l9LnfLIxQFe-HTON5CdFx41kBdLc2_QG5Wzk-EjCYE_3yidd_H2riNhaGV0n_F2QvVFP1HSeZIeYbYtuQXYlqctYgj8WMorbJ2rvniWxkNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کامران غضنفری با شکایت حسن روحانی به حبس محکوم شد!
🔴
دادگاه بدوی کامران غضنفری، نماینده مجلس را بابت هریک از دو عنوان توهین و افترا به پرداخت پانصد میلیون و یک ریال جزای نقدی و بابت نشر اکاذیب رایانه‌ای به سیزده ماه و شانزده روز حبس تعزیری محکوم کرده بود. دادگاه تجدیدنظر اعتراض متهم را مؤثر ندانست و حکم را عیناً تأیید کرد. این رأی قطعی است و مجازات اشد قابلیت اجرا دارد.
🔴
کامران غضنفری، حسن روحانی را به «جاسوسی برایMI۶»، « ارتباط با سرویس‌های خارجی»، «داشتن تابعیت انگلیسی» و «افساد فی‌الارض» متهم کرده بود. دفاع او این بود که مطالب مطرح‌شده را از برخی اعضای کمیسیون امنیت ملی مجلس یا گزارش‌های مربوط به مسئولان دوتابعیتی شنیده و ردصلاحیت روحانی در انتخابات مجلس خبرگان نیز مؤید ادعاهای اوست.
🔴
دادگاه این دفاع را نپذیرفت و تصریح کرد که هیچ‌یک از این انتساب‌ها در مراجع رسمی و قانونی به اثبات نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135941" target="_blank">📅 12:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
دلار هم اکنون 189,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135940" target="_blank">📅 12:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=dq4TAzQYOmyV75OM-B6u1Fd9UzpvdvVDArHZ6HWPfxtLcWvEpTY8ss_bn0UBDhg1khXLZ-vtwAEvs-aqSYzZSLF1Ghg3UMkuGRf9H6-L_UFBs9eYD80hW_bv8azFdDOWEBgatEmlnktVu-GZOYnoYm9LD4gD70hwbzpCyUkN1WN0RyOgXgkIBpZfeKeahBRWiO-IdD3ZO6y1qAEioXvknksbKM69N5IbB1Icg1Hb2pO-QHGfe5x8S263lNuchFYisjLI0JGjoYOKGx7QUGqR1KUbfDr-ZLBrnJKUQtQviaQ_ESK8_7zISCLQ0GHXYSQ5RQT4RUi7hI7UMUuTRFIJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d6385f7a.mp4?token=dq4TAzQYOmyV75OM-B6u1Fd9UzpvdvVDArHZ6HWPfxtLcWvEpTY8ss_bn0UBDhg1khXLZ-vtwAEvs-aqSYzZSLF1Ghg3UMkuGRf9H6-L_UFBs9eYD80hW_bv8azFdDOWEBgatEmlnktVu-GZOYnoYm9LD4gD70hwbzpCyUkN1WN0RyOgXgkIBpZfeKeahBRWiO-IdD3ZO6y1qAEioXvknksbKM69N5IbB1Icg1Hb2pO-QHGfe5x8S263lNuchFYisjLI0JGjoYOKGx7QUGqR1KUbfDr-ZLBrnJKUQtQviaQ_ESK8_7zISCLQ0GHXYSQ5RQT4RUi7hI7UMUuTRFIJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: هیچ بهانه ای برای پیمان شکنی آمریکا وجود دارد. دشمن فریبکار، خدعه‌گر و وحشی است، اما این دلیل برای عقب‌نشینی نیست
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135939" target="_blank">📅 12:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بیانیه نیروهای مسلح یمن در خصوص اعلام موضع مهم خود، 3 ساعت دیگر منتشر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135938" target="_blank">📅 12:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798b7b085.mp4?token=o5wPZmwoWOS_cSRWhoMwqPQe9m9nf4a-d3XsuHddBwPVMcifPckpHlcmi2LJsYCPG58Lwofi2pngkUwCQAddJkM4a8ytf1dYntITMQbnLyvbkM3M4q4zbnLVa3DnQq9dDphV2LFfGq9lkCFtpPaIcfB5K0J5ngLONGQXYh2cLsuSlCQ1d3qpYUzrw7oTxwyiGMARRS8FIcET4PQfvoUShzW6vqphEL5YnlxnSMON6WxdSiWROoAKuY0QJuFNR_bh-zMIZgW6kxPbaxup6dZKkkzY_rKrEA2oTiorRGGCeUjFgsN6DwK1AUkcDo6u_WuCg5smTyYksdtA0gw4_ev9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798b7b085.mp4?token=o5wPZmwoWOS_cSRWhoMwqPQe9m9nf4a-d3XsuHddBwPVMcifPckpHlcmi2LJsYCPG58Lwofi2pngkUwCQAddJkM4a8ytf1dYntITMQbnLyvbkM3M4q4zbnLVa3DnQq9dDphV2LFfGq9lkCFtpPaIcfB5K0J5ngLONGQXYh2cLsuSlCQ1d3qpYUzrw7oTxwyiGMARRS8FIcET4PQfvoUShzW6vqphEL5YnlxnSMON6WxdSiWROoAKuY0QJuFNR_bh-zMIZgW6kxPbaxup6dZKkkzY_rKrEA2oTiorRGGCeUjFgsN6DwK1AUkcDo6u_WuCg5smTyYksdtA0gw4_ev9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فراموش نکنیم که بندر عباس در دی ماه ۱۴۰۴ مورد تهاجم دشمن قرار گرفت.
🤔
زمانیکه که حرام زادهای لباس شخصی جمهوری اسلامی، مردم بندرعباس رو با گلوله جنگی می زدند‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135937" target="_blank">📅 12:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwI9SDrdxQV3k7mlOB5lBK7Jg8LxTEZnTdwQet2XjYEgu9u01Lz_qifdi2HLh5Ux6eeAM09StHujkGGGqWq8c4T8L_OwcGH12m5epNBBNM2Ap7_ZcGgau33XT5q3QG9iw5mmPEI4dvU2mQyO3NCW8PihmvpR5COVh9jMcLm6siBHuM0iaPjGLxeV64bc4q09WE1wPC2vamxTIo1AySp3mbzpADVGMgOYWrsjf6FxXNDomxWCf3Dfn-VDmVCWL_GeSwxiiWt13Z049hmatcu8LGR-vM3onW7u4w9GNSAlChF6h2TDUR-0QwAsvl6fc-tjrrBu3h54ewnfIckueQLlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های تجمیعی مربوط به ترافیک مصرفی کشور در ۲۴ ساعت گذشته، که در IRIX منتشر شده، نشان می‌دهد در زمان برگزاری مسابقه فینال حجم ترافیک کشور به ۷.۳۷ ترابیت‌برثانیه رسیده که نسبت به سایر ساعات پیش و پس از پخش این رقابت یک افزایش قابل توجه را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135936" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0663cc2.mp4?token=akpe-bQJSfS4C7X6iLLQtG3kn2SFKcxLyiFvYrfswijQ-rqlIX1HUq37oRfXs1P9l0mLYb0t5J3jLrJ5ylbBYXqAhhBrcDgXqJz4kn91PIfftiRpA-VbFoySyTbfm2Hjr5fpTWeXoeo9iDmhfQ9WXqTjgzbWkY0NMihBGZGiXevG6o2DVf2wgGzryay4wr35f3ta4nGOa3IELAlCwRtma8kxqHb5SI1-FLqz4DrU0_rFAwfct5ODCHtwWhW4EOXgosL3REF6AKnIL5mP9yJFe1Tx8URs3Tasg10cofy7J_g2oz2DEXLBHbb5hvcghQPJMiWCWx8i36o-YPljRLqYzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0663cc2.mp4?token=akpe-bQJSfS4C7X6iLLQtG3kn2SFKcxLyiFvYrfswijQ-rqlIX1HUq37oRfXs1P9l0mLYb0t5J3jLrJ5ylbBYXqAhhBrcDgXqJz4kn91PIfftiRpA-VbFoySyTbfm2Hjr5fpTWeXoeo9iDmhfQ9WXqTjgzbWkY0NMihBGZGiXevG6o2DVf2wgGzryay4wr35f3ta4nGOa3IELAlCwRtma8kxqHb5SI1-FLqz4DrU0_rFAwfct5ODCHtwWhW4EOXgosL3REF6AKnIL5mP9yJFe1Tx8URs3Tasg10cofy7J_g2oz2DEXLBHbb5hvcghQPJMiWCWx8i36o-YPljRLqYzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایران پیام مذاکره می‌فرستد، اما همزمان موشک و پهپاد شلیک می‌کند
🔴
مارکو روبیو، وزیر خارجه آمریکا: "ایالات متحده همواره برای دستیابی به یک راه‌حل دیپلماتیک آمادگی دارد. ما تاکنون چندین بار تلاش کرده‌ایم با ایران وارد گفتگو شویم و این تلاش‌ها را ادامه خواهیم داد.
🔴
اگر آن درِ گفتگو گشوده شود، از این موضوع استقبال خواهیم کرد. آن‌ها همچنان پیام‌هایی ارسال می‌کنند که نشان می‌دهد خواهان گفتگو و مذاکره هستند، اما آنچه ما به آن واکنش نشان می‌دهیم، رفتار آن‌هاست و این رفتار شامل شلیک موشک‌ها و پهپادها به سمت کشتی‌هاست؛ از جمله همین امشب."
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135935" target="_blank">📅 12:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71469609f.mp4?token=D2OZes5LCFi4EQmvxOQFRQ7VHOWHvc3u-J4CGWOZs9oT8TkA3CtH2CRol0mqGLpWxbCmp2lZQJuh2_4XIljqSScF7JqGv5KRESwsV2kzzBpVq_AWosMpnGd2g-odcITXM_KYgj0cmVHw8-rI-GtsNmOcwjizs0su100ebdR00WtGiEBPIXcmBj2v_ao7jXW942iFTjPts50NfpMXBoZdGjHkRPU_N31mdoD-inIQRoMSifWAmrY395fNsxLaSVrdsHuN5lS_M1reZ1xLD_z6TRXQPT8x2CWduDg4biTR3FPTQ3Xm3-4uLydqRKBOBDqRU89ScriXKWD3L6sg0J--kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71469609f.mp4?token=D2OZes5LCFi4EQmvxOQFRQ7VHOWHvc3u-J4CGWOZs9oT8TkA3CtH2CRol0mqGLpWxbCmp2lZQJuh2_4XIljqSScF7JqGv5KRESwsV2kzzBpVq_AWosMpnGd2g-odcITXM_KYgj0cmVHw8-rI-GtsNmOcwjizs0su100ebdR00WtGiEBPIXcmBj2v_ao7jXW942iFTjPts50NfpMXBoZdGjHkRPU_N31mdoD-inIQRoMSifWAmrY395fNsxLaSVrdsHuN5lS_M1reZ1xLD_z6TRXQPT8x2CWduDg4biTR3FPTQ3Xm3-4uLydqRKBOBDqRU89ScriXKWD3L6sg0J--kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد شیلنگ رو گرفت رو قلعه نویی
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135933" target="_blank">📅 12:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDwX_EDPoqFReNZWTazWxh9fNVqpqa37cwH6-RVB-2TGPWAWWvpcBKiNW0L8db5CD1s7scQdNuxnfMnh7KDpDuWRvpurATW73Sz9EEPpwof2SYifx-8STGxYNL162i5yQWWOCW7_XjMZB0EtXKrvjJsDmfpeZcBd1zULxC0GK_j7LhqJdmkWnQMSBJvN1pfKittGYWBQUOII1ew1SoAX6FbBhXmLAIh2dcyIyqYPAN-w7IIH0UXrQKEq64XFze54i8E1bS0ObSmJaF0ipErS0xL-kh3S2SXLKiWVV2-Mc279ZZPdeddSOy-SXD3GHrAuNZ31TZrzxMSAX4XJnxXWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: موفقیت تیم ملی فوتبال اسپانیا و کسب عنوان قهرمانی جام جهانی در کمال شایستگی را به ملت و دولت این کشور تبریک می‌گویم.
🔴
شادمانی ملت و دولت دوست اسپانیا شادمانی ملت و دولت ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135932" target="_blank">📅 12:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5bf2b8b2.mp4?token=jMR9f6Rsg6-Hq6KXxq0UpXgIPu_Ei168jP6kYA5M8ULOkbcoDKUsqa-tGkP2l4-zBpldKlBCvMk-ym4s3t-UO5K-VKw5MqsXtn2foUP-R4bvDNRs4m8J3dZOQYYDshaRc6KAhIQjczbg6LIgGwMV_rALQlwq_WeRobgNz1LI7oaelAOdBj6bpspGItLT-KZMvx6ZACjm5M6Z1PE55ikvpLyszCQOfGOv-ocj2UX1TgqsOqsK37ce7PYySIpAYk1mvt9ghf_x_8SLnxV4Mvdih88ZDwvfX_tA-KoEByQd14AQkmI_A_jijJRJOv_0V5FkII2PZF0WsNm6WfQXGhYLIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5bf2b8b2.mp4?token=jMR9f6Rsg6-Hq6KXxq0UpXgIPu_Ei168jP6kYA5M8ULOkbcoDKUsqa-tGkP2l4-zBpldKlBCvMk-ym4s3t-UO5K-VKw5MqsXtn2foUP-R4bvDNRs4m8J3dZOQYYDshaRc6KAhIQjczbg6LIgGwMV_rALQlwq_WeRobgNz1LI7oaelAOdBj6bpspGItLT-KZMvx6ZACjm5M6Z1PE55ikvpLyszCQOfGOv-ocj2UX1TgqsOqsK37ce7PYySIpAYk1mvt9ghf_x_8SLnxV4Mvdih88ZDwvfX_tA-KoEByQd14AQkmI_A_jijJRJOv_0V5FkII2PZF0WsNm6WfQXGhYLIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک منطقه وسیع در یک اردوگاه مخالفان ایرانی در شهر سلیمانیه عراق، به دلیل حملات، به طور کامل سوخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135931" target="_blank">📅 12:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edcee8203.mp4?token=tNoZgIAbU7nju0f0uD8FfL1ltv4j5iL5tbfDyJKCc8pZh8P3fH5TykdAImHZA7Tl37C14SYg-8WaSFZT4W8QEfIDe9Q_0nT6IjBvpYmNlPvA1ptrhSGqEWnBi8oZD1wO46VNebstwANK01oioBGVgOXUFBzAfNzZG2IjEGKCDvy-VrFos9pxqi3GeEIyrLxVgRq4cchfVXbvZLpC0kV0Ljjpf-msfmbuGHNdjtknyl8PPQYZPfnhoW7IeQKnrolHXU8SjtZANlqr703k2LIOo0iD-oy7A4tqOXjskSjeMIlqMTrKIztNRUIvCgo29r6onGLAKu2Wpc6mnXgKbRn_FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edcee8203.mp4?token=tNoZgIAbU7nju0f0uD8FfL1ltv4j5iL5tbfDyJKCc8pZh8P3fH5TykdAImHZA7Tl37C14SYg-8WaSFZT4W8QEfIDe9Q_0nT6IjBvpYmNlPvA1ptrhSGqEWnBi8oZD1wO46VNebstwANK01oioBGVgOXUFBzAfNzZG2IjEGKCDvy-VrFos9pxqi3GeEIyrLxVgRq4cchfVXbvZLpC0kV0Ljjpf-msfmbuGHNdjtknyl8PPQYZPfnhoW7IeQKnrolHXU8SjtZANlqr703k2LIOo0iD-oy7A4tqOXjskSjeMIlqMTrKIztNRUIvCgo29r6onGLAKu2Wpc6mnXgKbRn_FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: زدن برج دیده‌بانی در چابهار یا پل‌ها و نیروگاه‌ها یادآور اقدامات داعش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135930" target="_blank">📅 12:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی دولت عراق: علی الزیدی به ایران و ترکیه سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135929" target="_blank">📅 11:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گروه تجزیه طلب ایرانی-کورد، حزب آزادی کردستان (PAK) مدعی است
🔴
«ایران از فسفُر سفید در حمله خود به پایگاه ما در اربیل استفاده کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135928" target="_blank">📅 11:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: سفر نخست‌وزیر عراق، به ایران، سفر بسیار مهمی است.
🔴
ما از هم‌اکنون به ایشان و هیئت همراهشان خوشامد می‌گوییم و اطمینان داریم که این سفر می‌تواند نقطه عطفی در روند رو به رشد روابط دو کشور مسلمان و همسایه باشد.
🔴
با عمان از مدت‌ها قبل، یعنی از همان روزهای نخست برقراری آتش‌بس در نوزدهم و بیستم فروردین، در ارتباط بودیم و با آنها در مشورت بودیم.
🔴
تلاش ما این بوده که با همکاری عمان به عنوان دو دولت ساحلی بتوانیم تدابیر لازم را اتخاذ کنیم و سازوکارهای لازم را تدوین کنیم.
🔴
همچنان هم معتقدیم که این کار باید با همکاری و مشورت مشترک دو دولت ساحلی انجام شود. اینکه در رابطه با تنگه هرمز ما مصمم هستیم که منافع و حاکمیت‌مان را حتماً اعمال کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135927" target="_blank">📅 11:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135926" target="_blank">📅 11:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هیمتی ، رئیس بانک مرکزی:  درآمد سرانه واقعی کشور بر اساس قیمت‌های ثابت سال ۱۴۰۰، از حدود ۱۴۱ میلیون تومان در سال ۱۳۹۰ به حدود ۷۵ میلیون تومان در سال ۱۴۰۳ کاهش یافته که معادل نصف شدن درآمد واقعی سرانه طی ۱۳ سال است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135925" target="_blank">📅 11:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سپاه هرمزگان : احتمال شنیدن صدای انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135924" target="_blank">📅 11:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f8e3c491.mp4?token=iypxU-fqWsS9hzw9Y-rCzfaZVOFzl5z3CvYWzdrD2_ZPZ_oBV45IVrIRyOZq2v6j9JhLr7JKvsVLfd26DfIkElxlu3D7E1HKJhblEfeD1fVGJFciBeUdW_CpzQsUF3U7INrml9jWazyh6xTRxtsa7muEonAjPHPDhDdy2moVioZAJde9PPD9F4bj1AgoHwIF_BcI2gUBoWNsFpCIY-qjEfM1YySaF1xPsuQXk00AxjImhJXt4h77HehDJJfWlRgiJEUXDRLxTaOszKbT3bFOf9ZryZPpMQDYE7hrWRuWz9qkDML5a8O-t5KnnwzH9m3P4Yo0N_T-p_i2ofUOOSeKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f8e3c491.mp4?token=iypxU-fqWsS9hzw9Y-rCzfaZVOFzl5z3CvYWzdrD2_ZPZ_oBV45IVrIRyOZq2v6j9JhLr7JKvsVLfd26DfIkElxlu3D7E1HKJhblEfeD1fVGJFciBeUdW_CpzQsUF3U7INrml9jWazyh6xTRxtsa7muEonAjPHPDhDdy2moVioZAJde9PPD9F4bj1AgoHwIF_BcI2gUBoWNsFpCIY-qjEfM1YySaF1xPsuQXk00AxjImhJXt4h77HehDJJfWlRgiJEUXDRLxTaOszKbT3bFOf9ZryZPpMQDYE7hrWRuWz9qkDML5a8O-t5KnnwzH9m3P4Yo0N_T-p_i2ofUOOSeKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیضه مالی مجدد مِی‌ساقی در آنتن زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135923" target="_blank">📅 11:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت خارجه به تهدید آمریکا به تصرف جزیره خارک
🔴
افراد زیادی در جزیره خارک لحظه شماری می‌کنند برای خوش آمدگویی به نیروهای آمریکایی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135922" target="_blank">📅 11:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642abbab66.mp4?token=uii-QkuOPRB-hcKH7dQGZks541QpidUleUXYXJriZo0KMwzm8hUnl-ECz-mJMAT4SSlLbQw9SpOwNIeLOz1Xsmat4BawQSQvmK_noZDN33lg0ID7S9We0-3vaQcdOcQG-Q9WrJ8BIGHxlct61fPCCBMqBLzCQdTUsu9TXuWFAdd8WvlbrQJoIk5D36apMJ_W1nY76vyEDRg2YsGBHmqSc3laUpKrsao_9A4T80RpewjuBVwEKNGmMki206Yw3NrWw2Yl_y3jVkm540J3wmGTIxziA3nNZYA4Ty_I75aiI1j3JZHFCGVtetJcntZ09aAl-sAiHFFbgw5KLLxmjuQ_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642abbab66.mp4?token=uii-QkuOPRB-hcKH7dQGZks541QpidUleUXYXJriZo0KMwzm8hUnl-ECz-mJMAT4SSlLbQw9SpOwNIeLOz1Xsmat4BawQSQvmK_noZDN33lg0ID7S9We0-3vaQcdOcQG-Q9WrJ8BIGHxlct61fPCCBMqBLzCQdTUsu9TXuWFAdd8WvlbrQJoIk5D36apMJ_W1nY76vyEDRg2YsGBHmqSc3laUpKrsao_9A4T80RpewjuBVwEKNGmMki206Yw3NrWw2Yl_y3jVkm540J3wmGTIxziA3nNZYA4Ty_I75aiI1j3JZHFCGVtetJcntZ09aAl-sAiHFFbgw5KLLxmjuQ_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی : هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135921" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135920">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:  متن یادداشت تفاهم هیچ بهانه‌ای برای طرف آمریکایی باقی نگذاشته و حتی خود آمریکایی‌ها نیز ادعایی مبنی بر اختلاف در تفسیر متن برای آغاز مجدد حملات مطرح نکرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135920" target="_blank">📅 11:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / الحدث به نقل از منابع آگاه: وزیر کشور ایران امروز با نامه‌ای ویژه از پزشکیان وارد پاکستان می‌شود.
🔴
نامۀ پزشکیان که وزیر کشور ایران به همراه دارد، به پروندۀ مذاکرات مربوط می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135919" target="_blank">📅 11:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تخم‌مرغ گران‌تر شد، کوچک‌تر هم شد!
🔴
قیمت هر شانه تخم‌مرغ در تهران به حدود ۴۸۰ هزار تومان رسیده؛ یعنی ۸۰ هزار تومان افزایش در دو هفته.
🔴
خریداران می‌گویند با وجود قیمت‌گذاری شانه‌ها بر اساس وزن ۲ کیلو، تخم‌مرغ‌ها ریزتر و سبک‌تر شده‌اند.
🔴
تولیدکنندگان گرانی و کمبود خوراک را دلیل افزایش قیمت می‌دانند؛ این در حالی است که وزارت جهاد کشاورزی از افزایش واردات و ترخیص نهاده‌ها خبر می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135918" target="_blank">📅 11:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa3dfa981.mp4?token=CIE7D0BQlOMaBx8UyTcse8h2ZIuDyfzd8-YK0Ie-VzmsKMnATUCDbLYZBsf0BJ2_DM70n1Nz0H2sIhVmtxvkx7_XU_qKLF4uOT-yW4NClfjsBU2Bq3EHcsINrxu69wlICtVZdT7EF7y5Y9zyEu7oEH6SOhFwIiWnjtcJ6UhHiFR3TCUYDZJaJFEtaHVMWSM90U-Nzlg1KqlAMJzq8FpMiDMTs5PoIW4u73eGWhDxB-aaYdI0M8klK50TIuWM01iy2c-aT5_CaDVQxgaUQqI9O9ZFXB_BkokxKeFltytzYO129irwOsMOS2wj4326W2nljdXYE9nFAx6kwuZ4RH6MeqBdLcqvzk0QPmh_tVgr01aQGvChn-zVqlR7swrUa6yovoNYkYfBq11_xrQ1MnnnsbB5kWwPqwS8E64KTtc5383XkCjrWDDwSvEuipKCzwyQeF6kZznaMzmTfo7eL8pGKlgZCQSz0jT1fAUPuS-zAnjpzmYmOiVVTSB2xHPIHREBAvL-emjeqjt_6Zobhgpb-bkj_U6WzdOdwZWfBvutSWpq0za9omerOohDLzIn8TjSimjQnTIhp23FNitatRRJwKevol-rC8IDWP9GpDP7yEzzsKbGevkJWnXeCfeWf3t_1BUPhDi4naURnqAGh1bIcDWVUxjg1qR-k1VxiNqyDUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa3dfa981.mp4?token=CIE7D0BQlOMaBx8UyTcse8h2ZIuDyfzd8-YK0Ie-VzmsKMnATUCDbLYZBsf0BJ2_DM70n1Nz0H2sIhVmtxvkx7_XU_qKLF4uOT-yW4NClfjsBU2Bq3EHcsINrxu69wlICtVZdT7EF7y5Y9zyEu7oEH6SOhFwIiWnjtcJ6UhHiFR3TCUYDZJaJFEtaHVMWSM90U-Nzlg1KqlAMJzq8FpMiDMTs5PoIW4u73eGWhDxB-aaYdI0M8klK50TIuWM01iy2c-aT5_CaDVQxgaUQqI9O9ZFXB_BkokxKeFltytzYO129irwOsMOS2wj4326W2nljdXYE9nFAx6kwuZ4RH6MeqBdLcqvzk0QPmh_tVgr01aQGvChn-zVqlR7swrUa6yovoNYkYfBq11_xrQ1MnnnsbB5kWwPqwS8E64KTtc5383XkCjrWDDwSvEuipKCzwyQeF6kZznaMzmTfo7eL8pGKlgZCQSz0jT1fAUPuS-zAnjpzmYmOiVVTSB2xHPIHREBAvL-emjeqjt_6Zobhgpb-bkj_U6WzdOdwZWfBvutSWpq0za9omerOohDLzIn8TjSimjQnTIhp23FNitatRRJwKevol-rC8IDWP9GpDP7yEzzsKbGevkJWnXeCfeWf3t_1BUPhDi4naURnqAGh1bIcDWVUxjg1qR-k1VxiNqyDUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تشییع جنازه ۹ نفر از نیروهای گروهک های کرد در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135917" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHa0Kr70m1yLtd_m1t4tb4h2l5a6yzYCg0RmXxVpmeueDkVooc6I3_HJqLpcPMpFafRWl1zsyHN6mFDeh9qp9oQ3d4pp7xIyfc7MCH8Xq5FNmvlq1Bh9USIfvcD1B6pZfyEt2q5M3R6zgi09USDbeWht3PfY-AjfTzYiaLuQmZW6Yplb21lp9Jw-anYLnbS7ERG1g9cK2oAIwRE4DNh783yfWs8Yesp5jd-2ZG6muoFqPyjj37MFVx4L1oKHq4LlnmKsuyhRkWh1PVIKSp-3CDY7M4EH2ReIyio1KsA0CfwJqVmukZk-23UjRfQ_VY5-ZV-o96pPZeVYsDExG1AZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب گذشته، اوکراین به یک پالایشگاه نفت در پودولسک، واقع در منطقه مسکو، و همچنین به سه ترمینال بزرگ توزیع کالا متعلق به شرکت Wildberries در حومه مسکو حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135916" target="_blank">📅 11:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: پیشنهادهایی از سوی میانجی‌ها مطرح شده و دریافت کرده‌ایم.
🔴
اصل موضوع که در این روزها هم دستگاه دیپلماسی فعال بوده و هم ایده‌هایی از سوی برخی از میانجی‌ها به ما واصله شده تأیید می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135915" target="_blank">📅 11:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اگر انتظار دارید دیپلمات‌هایتان به خاطر ترس از فریبکار بودن دشمن صحنه را ترک کنند حتما چنین نخواهند کرد. دشمن فریبکار است و خدعه می‌کند و وحشی است ولی مثل این است که بگوییم کسانی که پای لانچر نشستند و از ایران دفاع می‌کنند از ترس اینکه طرف مقابل از تکنولوژی برخوردار است، صحنه را ترک کنند.
🔴
دیپلماسی و دفاع دو بال هستند. اگر هر کدام نتواند به هر دلیلی وظیفه خود را در دفاع از ایران انجام دهد قطعا وظیفه حکمرانی ما به درستی انجام نمی‌شود.
🔴
به همان میزان که به مدافعان میهن در پای لانچرها افتخار و از آنها حمایت می‌کنید دیپلمات‌هایتان هم به همان اندازه شایسته حمایت و دفاع هستند چون دیپلمات‌ها در کنار مدافعان وطن برای یک هدف می‌جنگند
🔴
اصرار بر دوگانه مذاکره یا جنگ ، دیپلماسی یا جنگ برای کشور ما مفید نیست.
🔴
اینکه فکر کنیم دیپلماسی نافی دفاع است یا اینکه دفاع با دیپلماسی سازگاری ندارد به هیچ عنوان منطق صحیحی نیست.
🔴
کاری که سیدعباس انجام می‌دهد با کاری که سیدمجید انجام می‌دهد با یک هدف است.
🔴
هدف صیانت از منافع ملی ایران است. گاهی با ابزار دفاع و گاهی با دیپلماسی و گاهی همزمان هر دو
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135914" target="_blank">📅 11:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYRlPmrlz1Fi3IKHMXLr5WBwWlLmCv5cpIozMV7_-fEuIJ4cPFAJNjgrEZ9kgW5a1l5ZT1AtQ0APunbyWzVd7agHJg98YKGE_TbeXVqzxHqoXIPI8p9mxa-325WHpt6va1U5CFRtb7yvl7Fw-M9MfMKcLSvM79mqfOz_rmSo9AFJXfLqc6wYI6RGS4TiVz0_8pZODToJLNeHvRM24DjAqQz39ijAKEvS_jz-MBBxGvMML5EjsFLdHjh03-VOcUqtQFGmtmH13U76Keie28GxK2JshNXtyMYGRgRLcruHHXWMgXcrX5pk4Cdrlo0UetstCuA_ql99hk-ICXlefNYt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه اسراییلی: پایان بازی در حال نزدیک شدن است: بقایای رهگیری موشک‌هایی که به‌سوی عقبه شلیک شده بودند، در نزدیکی ایلات سقوط کردند!
🔴
مقام‌های امنیتی اسرائیل برآورد می‌کنند که پایان جام جهانی به پایان خویشتنداری آمریکا در خاورمیانه منجر خواهد شد.
🔴
تمامی نهادهای امنیتی در بالاترین سطح آماده‌باش قرار دارند، زیرا احتمال کشیده شدن دوباره به درگیری‌های نظامی وجود دارد.
🔴
با این حال، تصمیم درباره اینکه این اتفاق چه زمانی و به چه شکلی رخ دهد، عمدتاً در واشنگتن گرفته خواهد شد.
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135913" target="_blank">📅 10:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZIvndZJGlu9OOIlM0fp9wY43fZb66tlJ4wNaACLYIAmZ8Qa_ugD6BcXZy8BKqjitHNgN5umL1qdfPGyfpI8uAox698qQ1HYcderBobVBXRYekUAN0_lyz4O4jFYacLOQz40gwNImEN2kIh2tNTu7uNHE318urL73W1Pl6_nKR3PVw3TcvnNuVN63Yxwt819VNB4WC6jDzzGcR-gB-b85eblu3Rz-02uC3N9ITmKhx2_j8F1KLD3C4GjxNhUkTZRC8eGGBKf1wClqlYJsEfJ0fL7OLn3b_1au5vF8IVoNnH0cHtlB2NLWyDQKfaAE2acUpaSi8vXnA3_9mDDGToOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
🔴
۹۱ دلار را هم ثبت کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135912" target="_blank">📅 10:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3a65c5f.mp4?token=s8z34NCUns9zWG0IhcdKjRNrKtYBPM7brbRv4vmFqoEYZwQt0R_nRl4J-OEJRmMIDkjH68u1SagVElKB5GULXMcIfBNUpGOEl-a1qCah-zKuL6GbLm2GGthfoAlBfQTJGg_P0X9J4fbcB8GT663F6BFbo4I8TKR8RJThyOI9AtSI5svqSoQCp0z3jYYtYh7NVIU0ya5SCxjzLh6wvKrpAWgpbjqG_nIIpRPkkS0Krm-sFeqY_XtUoSRDwt0R7ieV66v8kPnztQfmmm_aBdK1APl1vIQjAuqbS_0Lq_ps2V2LXnuRxv1UQpqBv121KErkHCCfNT42y0k7PCzUBRD44A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3a65c5f.mp4?token=s8z34NCUns9zWG0IhcdKjRNrKtYBPM7brbRv4vmFqoEYZwQt0R_nRl4J-OEJRmMIDkjH68u1SagVElKB5GULXMcIfBNUpGOEl-a1qCah-zKuL6GbLm2GGthfoAlBfQTJGg_P0X9J4fbcB8GT663F6BFbo4I8TKR8RJThyOI9AtSI5svqSoQCp0z3jYYtYh7NVIU0ya5SCxjzLh6wvKrpAWgpbjqG_nIIpRPkkS0Krm-sFeqY_XtUoSRDwt0R7ieV66v8kPnztQfmmm_aBdK1APl1vIQjAuqbS_0Lq_ps2V2LXnuRxv1UQpqBv121KErkHCCfNT42y0k7PCzUBRD44A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: فکر می‌کردیم دو نفر [نیروی نظامی آمریکا] در حملات ایران کشته شده‌اند، اما سه نفر بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135911" target="_blank">📅 10:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / نقطه‌ای در حوالی اورمیه هدف اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135910" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae303cbc4.mp4?token=RVG_C-qiHjW9PqaLcG6wVyy8fHK5uFttE9aWR59W6z34Xh2ykMfZLTLZvxjO5p8ZJbBIEZYTeCki2DRnQhv9-sfSz0vGha-45kFupZhuB3q_Wl4Hj8fsuzqu6eFPdoNhGZUPj9EO25362aIqIz69kWaj-2ZuJQM24z_3vGO4f-PoNLD_vGEH82vTIL_Nw1gNhGqVmFrrfieKYf8Nrp8AgtH27hFJ2istEkcsWYm6ZLPyNSBtyxDkYNi9stfl0rJVNJ5OkOE4WkqhcvHk8YkR9Ko_1-tEpI3FhRqRm-lkdIarlB3IZlRkqVx2ChK8iO6u7rIoLiUvAngvodlIKI1-uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae303cbc4.mp4?token=RVG_C-qiHjW9PqaLcG6wVyy8fHK5uFttE9aWR59W6z34Xh2ykMfZLTLZvxjO5p8ZJbBIEZYTeCki2DRnQhv9-sfSz0vGha-45kFupZhuB3q_Wl4Hj8fsuzqu6eFPdoNhGZUPj9EO25362aIqIz69kWaj-2ZuJQM24z_3vGO4f-PoNLD_vGEH82vTIL_Nw1gNhGqVmFrrfieKYf8Nrp8AgtH27hFJ2istEkcsWYm6ZLPyNSBtyxDkYNi9stfl0rJVNJ5OkOE4WkqhcvHk8YkR9Ko_1-tEpI3FhRqRm-lkdIarlB3IZlRkqVx2ChK8iO6u7rIoLiUvAngvodlIKI1-uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا کویت به دلیل از کار افتادن بخشی از  شبکه برق، که نتیجه حملات مداوم است، از ژنراتورهای سیار برای تأمین برق مناطق مختلف استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135909" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: وزیر کشور ایران شامگاه امروز به اسلام‌آباد، پایتخت پاکستان، می‌رود تا با همتای خود و مسئولان این کشور دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135908" target="_blank">📅 10:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / سازمان دریایی بریتانیا آتش‌سوزی یک کشتی در نزدیکی بندر کومزار عمان را تأیید کرده است.
🔴
منابع خبری و دریانوردی این کشتی را با پرچم مالت و مدیریت یونانی معرفی کرده‌اند.
🔴
این کشتی در حال حمل نفت عربستان به‌سمت آمریکا بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135907" target="_blank">📅 10:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
انفجار  در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135906" target="_blank">📅 10:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135905">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سپاه:از اطلاعات مردم اردن ممنونیم؛ هواپیماهای بزرگ ترابری c17 و هواپیماهای فرمانده کنترل p8 ارتش امریکا در فرودگاه عقبه هدف موشک بالستیک قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135905" target="_blank">📅 10:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135904">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روبیو، وزیر امورخارجه امریکا: ایالات متحده همچنان برای دستیابی به راه‌حل دیپلماتیک در قبال ایران آمادگی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135904" target="_blank">📅 10:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135903">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌ها از وقوع یک رشته انفجار در سراسر بحرین حکایت دارد و انفجارهای پیاپی در چندین منطقه از جمله پایتخت، منامه، شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135903" target="_blank">📅 09:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مهر: وقوع صدای انفجار در اصفهان
🔴
دقایقی پیش صدای یک انفجار در شهر اصفهان شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135902" target="_blank">📅 09:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135901">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / نقطه‌ای در حوالی اورمیه هدف اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135901" target="_blank">📅 09:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135900">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری /شنیده شدن صداهای انفجار در بوشهر و کنارک و چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135900" target="_blank">📅 09:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135899">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=luf3CJPrGZoKYtK-WGU7WcJNnMKA42DUh_7r-XJR-W3HDgpWi8zl4SdFuOAfZTcI7icscvbmqHt0Ky24dtdUXRN5_irePAaR0V_vedekx95oCpu5x43Ecsfy8VhXBicfJMCf1fwexsCQEuGRi3ob4n-kkbM-mnmzn1VrZki4F7G9WSoMuaOXebXAGxT-objXa0G_1oC4Dan5b3ykYShJgrVfo8SxqvStrJrKorB1AG2ujXoZROqavDODW4aeAWAd_0CC8wS76tEwAhfDYxW0l2OtV-_Ug8Cg__MzuhlFTeAtf8wQLHkYjTN8xeH3NxR3g7GbSwsaCDQcyskbYnOOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=luf3CJPrGZoKYtK-WGU7WcJNnMKA42DUh_7r-XJR-W3HDgpWi8zl4SdFuOAfZTcI7icscvbmqHt0Ky24dtdUXRN5_irePAaR0V_vedekx95oCpu5x43Ecsfy8VhXBicfJMCf1fwexsCQEuGRi3ob4n-kkbM-mnmzn1VrZki4F7G9WSoMuaOXebXAGxT-objXa0G_1oC4Dan5b3ykYShJgrVfo8SxqvStrJrKorB1AG2ujXoZROqavDODW4aeAWAd_0CC8wS76tEwAhfDYxW0l2OtV-_Ug8Cg__MzuhlFTeAtf8wQLHkYjTN8xeH3NxR3g7GbSwsaCDQcyskbYnOOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاول دورف»، مدیرعامل تلگرام، اعلام کرد که قابلیت Carousels به این پیام‌رسان اضافه شده است. او به شوخی گفت با این قابلیت کاربران اکنون می‌توانند تصاویر گربه‌ها را درون اسلایدهای ارائه خود بگذارند. با این ویژگی می‌توان با کشیدن انگشت به چپ و راست بین عکس‌ها جابه‌جا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135899" target="_blank">📅 09:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135898">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قیمت نفت خام برنت با افزایش سه درصدی از سد ۹۰ دلار گذشت و به ۹۰ دلار و ۷۴ سنت رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135898" target="_blank">📅 09:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
تعداد زیادی از هواپیماهای باری نظامی آمریکایی به سمت اروپا در حال حرکت هستند و مقصد نهایی آن‌ها، خاورمیانه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135897" target="_blank">📅 09:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135896">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD7UFnZWCkPp8qSZqytEzPCH9RlJZV4IgsG3e02ZLS9vtWdcD_5J2-Mh_BSB7bvIf2qnTkcOZMp4sSsxQY8mCFjB8ZLmmNwKeeEdllXmdt1Y7_cFat2u5A9S1wj4JjN2hz62RnJZErxIyLVEEB5KWT6d2kEQ_tYbyXxh9z3oj1irOpNo3Cwki9696XDD4swQG1vq4yebiJG7kBl-Xv1K67PxxxuGyG0W4CxM4WoflCGEvnDdA4vBm_WfOvmmP0GkqC5ui7AgSsNtijKvUelEqa6emGu8E9I4Qp3mu_rV-49wS36uvx_53i45cpuIpQ1Fb03aWWrX-UjVqL2GAY5YMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعت ۴ بامداد امروز مولوی محمد انور ریگی امام جمعه اهل سنت مسجد علی‌ابن ابـی طالب (ع) شهرستان میرجاوه سیستان و بلوچستان توسط افراد ناشناس ترور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135896" target="_blank">📅 09:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135895">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزارت کشور بحرین: فعال شدن دوباره  آژیرهای هشدار؛ از شهروندان و مقیمان می‌خواهیم که آرامش خود را حفظ کرده و به نزدیکترین مکان امن مراجعه کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135895" target="_blank">📅 09:06 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
