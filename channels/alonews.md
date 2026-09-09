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
<img src="https://cdn4.telesco.pe/file/PvYZJF6_lG48crPabzVY03ab2gZcegIEUR9H7JAYXvU6XTGpqwfNqRDH785Y0y215X2klCtzRwDYmguNEgXASB4zEd-SFYet2Rx5tiXLOjsZSbu70iAsSlY3KeWT5cAonlDS0gMO-24vNuZBYdofTwzV6Y3G37cpJNQk5KrIntKM2j_mZJJBOty6bFYLOHmkWsqxlkRtbQrbZTMj3-VOdzr8BZ3pn2nJFB41JpZReKDWhB-8-31EbmojADQRoptUVSO1qWoHLQ-Xm8ucJjwqdvMjsoK72dOMLc8l8kKNj-OgGfM6CD9kLYmpNB_agMumdLYTIR7r5WGkYCglSOfaqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 09:42:44</div>
<hr>

<div class="tg-post" id="msg-146408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: در واکنش به حمله به ناوهای جنگی ایالات متحده، به حملات علیه نفتکش‌های ایرانی ادامه خواهیم داد
🔴
هر بار ایران به کشتی‌های جنگی ما حمله کند، یک نفتکش را از دست خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/146408" target="_blank">📅 09:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64f3accac.mp4?token=DLRgoJsRnaX5Oq48K7fwQMceCGQv9M2dmPAYOIaGndI6ZYZbA1jldy4XPzOal8RRcRqwwVaFAm9uXWEhtYAhPXrl3uHetfUL2mJFC_kB7qVSIo1VB4d4jMYLs55cLcMcKuyF2nLoL8z6yFPsXhw6BCKCpG18lM3yhD9L97_dOYnH-3xqbpxGFB3LhM7PKG3HbF2oUnO3p5ypf0NVMd4PYNQ2A2LPYnlwd-AuqlZ1L6IslbMJIDM8b2vHoCjnGYf548AKnIDnx99aSDtvh2Ji_s8i9kaz27k622zakFjem-GmeqVe0sO9OvwYueJEJcpy-saPUKeNxpfVWq5pDu7J1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64f3accac.mp4?token=DLRgoJsRnaX5Oq48K7fwQMceCGQv9M2dmPAYOIaGndI6ZYZbA1jldy4XPzOal8RRcRqwwVaFAm9uXWEhtYAhPXrl3uHetfUL2mJFC_kB7qVSIo1VB4d4jMYLs55cLcMcKuyF2nLoL8z6yFPsXhw6BCKCpG18lM3yhD9L97_dOYnH-3xqbpxGFB3LhM7PKG3HbF2oUnO3p5ypf0NVMd4PYNQ2A2LPYnlwd-AuqlZ1L6IslbMJIDM8b2vHoCjnGYf548AKnIDnx99aSDtvh2Ji_s8i9kaz27k622zakFjem-GmeqVe0sO9OvwYueJEJcpy-saPUKeNxpfVWq5pDu7J1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
34 میلیون تومان وجه رایج مملکت
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/146407" target="_blank">📅 09:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سپاه: ناوشکن‌های رزمی DDG-119 و DDG-53 آمریکا مورد حمله قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/146406" target="_blank">📅 09:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU9l4KgDOFqLaoYaG0chxZ2TtTwx2TAi_LV8iFp316HonfGrZktffzjjB4QxKT3wYdX06Dnq6S8NLdED9cRMZIunRAEMrhSlg6miV1N8yigsz5R4ypsepyRs8kDxLW137pkHBAPgJpcaLzww0Mb24kOlW0zAzBex44N0c-SF8kVghHPgEuJ61GrYdiG4rQYAq8tkSh7IiABG6t7x_XKrJzzVN6uSwekaISZiAHxVGI7NPBKLlazE5m2nkXE9oH0yTOXVQumAS1cDQsqIR12bUJ15I1S7JUySDiUDU7CSMQjs9lQXOVCXGX3aja8NsqcxvPgZ_46EjPw9tLjx4u2neQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دولت ترامپ با اقدام تحت رهبری بریتانیا برای تحریم شهرک‌نشینان اسرائیلی و نهادهای دخیل در گسترش شهرک‌سازی در کرانه باختری مخالفت نکرده است.
🔴
به گفته مقام‌های آمریکایی و دیپلمات‌های غربی، اندی برنهام، نخست‌وزیر بریتانیا، پیش از اعلام این تصمیم، ترامپ را در جریان گذاشت؛ اما ترامپ مخالفتی نکرد و از لندن نخواست مسیر خود را تغییر دهد.
🔴
مقام‌های آمریکایی همچنین به بریتانیا گفته‌اند که درباره سیاست اسرائیل در کرانه باختری نگرانی‌های مشترکی دارند، هرچند با خود تحریم‌ها موافق نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/146405" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عبور ۶ کشتی حامل کالا از تنگه هرمز در روز سه‌شنبه
🔴
داده‌های شرکت کپلر نشان می‌دهد که روز سه‌شنبه ۶ کشتی حامل کالا از تنگه هرمز عبور کرده‌اند؛ موضوعی که نشان‌دهنده کاهش این میزان نسبت به میانگین روزهای گذشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/146404" target="_blank">📅 09:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آتش‌گرفتن یک کشتی در قطر
🔴
قطر از وقوع آتش‌سوزی در یک کشتی در بندر «الوکره» و مهار آن خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/146403" target="_blank">📅 09:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
منابع یمنی: جنگنده‌های سعودی ۳۲ حمله هوایی به استان‌های مأرب، الجوف، تعز و الحدیده انجام داده‌اند
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/146402" target="_blank">📅 09:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dee846013.mp4?token=pTkTrRXe2m27G1wsJNceVXk6ErN6bVSZKhES4TlpnEVGyzLjRIYnlKrwrq3eqUMAxYdGJsbdY18S7AkT0OzHGU8Dw4kgcxN-tubyVd92A0EUYu0jaCsBc2PjtXwJ0SK6ZEyBIT5A1VTPfUxyEBneOePYj8vwfN4-b8doBPjggaFaJNt0qP4wtF7AxP1FoK3hnPcMoXj9eLvQvY_uEksZ5UjGoXMccNz2UPMlU567kggoOJplSYFYLNT_J-mg5zGSznNr-fBQwOQaD07njen1efbOaBcQBrbAu51hEWIVz2e_WyYFC4waLB1aNl3xmPHX9u6EfVCrNW88c_tUrfCgNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dee846013.mp4?token=pTkTrRXe2m27G1wsJNceVXk6ErN6bVSZKhES4TlpnEVGyzLjRIYnlKrwrq3eqUMAxYdGJsbdY18S7AkT0OzHGU8Dw4kgcxN-tubyVd92A0EUYu0jaCsBc2PjtXwJ0SK6ZEyBIT5A1VTPfUxyEBneOePYj8vwfN4-b8doBPjggaFaJNt0qP4wtF7AxP1FoK3hnPcMoXj9eLvQvY_uEksZ5UjGoXMccNz2UPMlU567kggoOJplSYFYLNT_J-mg5zGSznNr-fBQwOQaD07njen1efbOaBcQBrbAu51hEWIVz2e_WyYFC4waLB1aNl3xmPHX9u6EfVCrNW88c_tUrfCgNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل کوثری: ستاد کل نیروهای مسلح، سپاه و ارتش از سال‌ها قبل برای ایجاد آمادگی لازم، برنامه‌ریزی‌های دقیق و بلندمدتی انجام داده بودند تا در شرایط حساس بتوانند پاسخ مناسبی به تهدیدات بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/146401" target="_blank">📅 08:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌ان‌ان: عربستان در تلاش است تا کشورهای دیگر را علیه یمن وارد جنگ کند
🔴
پادشاهی سعودی پس از حمله بزرگ ارتش یمن به خاک این کشور در حال برنامه‌ریزی برای پاسخ به آنها در یمن است و متحدان خود را از برنامه‌های خود مطلع کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146400" target="_blank">📅 08:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bede8db302.mp4?token=b8cAMvW54lg5V3YD0YqBaXg5_P4tB9GUqwJh2QQhO1WgH6OuEiExNchqnuQN9_jgoB7yd1BqIlKYk7ztl1LDt6grghsYGd1wo_BhftFtjVW7XoLH8TJq2MUHvfT8oDhvzyaX5tHeDszbkycSuXNoeTgE06GQ7JAa9kiogsTXAZmIl41DUg-EcDE3ndjrcsGjiHjNXUqIOR73mz4Rg5sLX5babF4uvvsRU-SEnGBMvL5Syvt0wN0FphTbkR_Z49oKAI8Byv73n_0pIuPd-nzu8EaZAYlkE79adHezQrQxTjxTBP7qV5p3z0gxu3BSkBg3efoSYM2LJxwC1vM9KuBaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bede8db302.mp4?token=b8cAMvW54lg5V3YD0YqBaXg5_P4tB9GUqwJh2QQhO1WgH6OuEiExNchqnuQN9_jgoB7yd1BqIlKYk7ztl1LDt6grghsYGd1wo_BhftFtjVW7XoLH8TJq2MUHvfT8oDhvzyaX5tHeDszbkycSuXNoeTgE06GQ7JAa9kiogsTXAZmIl41DUg-EcDE3ndjrcsGjiHjNXUqIOR73mz4Rg5sLX5babF4uvvsRU-SEnGBMvL5Syvt0wN0FphTbkR_Z49oKAI8Byv73n_0pIuPd-nzu8EaZAYlkE79adHezQrQxTjxTBP7qV5p3z0gxu3BSkBg3efoSYM2LJxwC1vM9KuBaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه شلیک بیش از 100 موشک پاتریوت، سیستم دفاع هوایی آمریکایی، در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/146399" target="_blank">📅 08:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وال استریت ژورنال: حملات اخیر ایران علیه تجهیزات نیروی دریایی آمریکا نگران‌کننده است
🔴
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/146398" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6c355c1f2.mp4?token=u8Cd_8rKrdXw1xifDDdPj-oUj-GrLmrjV6FSMbTouR2QIq1XFMDl2Ekeza0ePkZzvvpOclscOQiZafGKyu0vQ1xXox-89nSCdzHMTCAia16ozv-fUlWQijv98KV3xK_a0cYCTPL9b-yiFbusunOapHhwaYhHJeMGhspD2h66Odd4lseanGfJKueOVv8WBdMowF3mon6ZXNFyQV5I9lWvseYjothxoizAXb3odmaVJwfvhNHOOdsWXUuOdQy8EprtGqdL6hIq4RlZJ13jUij9fclgJTl8Sxs3AEvJN_xDnInSNSDieoMxlAnLkaGpHk09brFPfJkdCw9sb_EcwR0S3p971SYmgz08YvwKDXEF3JL8HrDN96A23DvEC0uebeoI6Jt_r6_GxVn78c6zyZhmAAc5MUlOC-DXEdbLL8sy7q9XyrNJhpO9aF2jjZLm1tXcVGPtDg9A4-EfJm2WOPjIECfda2Q3CCcCw6D6KN7MbiAgJakvUZx5W1wfI8BLijUuCixZxK7rbnF0nfwhiRNQ2E9SAcsFLkFJs396fnAnfQKsWQ3vFOmVr9cSj4EN99sJPQSoQPiIaA4K3r0sDgy0jJ28Zs-nJRsWMQwzFg6-M0HvejTL2zgTHSWwJy-RWW20mK2T6AUz6QoUl81uPkXOGU-BiJ20j8sPrRe0VtF2bLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6c355c1f2.mp4?token=u8Cd_8rKrdXw1xifDDdPj-oUj-GrLmrjV6FSMbTouR2QIq1XFMDl2Ekeza0ePkZzvvpOclscOQiZafGKyu0vQ1xXox-89nSCdzHMTCAia16ozv-fUlWQijv98KV3xK_a0cYCTPL9b-yiFbusunOapHhwaYhHJeMGhspD2h66Odd4lseanGfJKueOVv8WBdMowF3mon6ZXNFyQV5I9lWvseYjothxoizAXb3odmaVJwfvhNHOOdsWXUuOdQy8EprtGqdL6hIq4RlZJ13jUij9fclgJTl8Sxs3AEvJN_xDnInSNSDieoMxlAnLkaGpHk09brFPfJkdCw9sb_EcwR0S3p971SYmgz08YvwKDXEF3JL8HrDN96A23DvEC0uebeoI6Jt_r6_GxVn78c6zyZhmAAc5MUlOC-DXEdbLL8sy7q9XyrNJhpO9aF2jjZLm1tXcVGPtDg9A4-EfJm2WOPjIECfda2Q3CCcCw6D6KN7MbiAgJakvUZx5W1wfI8BLijUuCixZxK7rbnF0nfwhiRNQ2E9SAcsFLkFJs396fnAnfQKsWQ3vFOmVr9cSj4EN99sJPQSoQPiIaA4K3r0sDgy0jJ28Zs-nJRsWMQwzFg6-M0HvejTL2zgTHSWwJy-RWW20mK2T6AUz6QoUl81uPkXOGU-BiJ20j8sPrRe0VtF2bLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی اردنی‌ها از دیدن موشک‌های
سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/146397" target="_blank">📅 08:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
👈
سپاه: بامداد امروز آشیانه تعمیر و آماده‌سازی و محل استقرار جنگنده‌های f-15، f-35 و f-16 آمریکایی هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/146396" target="_blank">📅 07:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هم اکنون وضعیت آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/146395" target="_blank">📅 07:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/146394" target="_blank">📅 02:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468d01fd4.mp4?token=KSuSqW9aMXi0HgbJJzecm-5oxsMC92Yb4NWvqsmPiDyP3lpPE6Fbg0e2XhWNqbWoK__ylmxVPfzpsX68Mn1UJKOMRxc1lR1FtEAvhwRsPc_fDEVIcjmxNf43IIBxo2KU0kNYsSnx-y-RzWPHNGJNX9z5t9RMHEG_gGyn3wDN4gOI76Iitg0cdvHH6FtIUViv9eDzo8jMiKO4-9AW1XEPiFSGIkYsNmL6Pxt9w1MwWWwTlKutS_lkdogFPc-EWjlBvc9o_NMe37tWj3mIlJAZAjgbBIqIJK_Icw4pw8VtgmtFRC3T7tiCCtus5zHkW6LZSfky5rGKHH47zkeq6xrLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468d01fd4.mp4?token=KSuSqW9aMXi0HgbJJzecm-5oxsMC92Yb4NWvqsmPiDyP3lpPE6Fbg0e2XhWNqbWoK__ylmxVPfzpsX68Mn1UJKOMRxc1lR1FtEAvhwRsPc_fDEVIcjmxNf43IIBxo2KU0kNYsSnx-y-RzWPHNGJNX9z5t9RMHEG_gGyn3wDN4gOI76Iitg0cdvHH6FtIUViv9eDzo8jMiKO4-9AW1XEPiFSGIkYsNmL6Pxt9w1MwWWwTlKutS_lkdogFPc-EWjlBvc9o_NMe37tWj3mIlJAZAjgbBIqIJK_Icw4pw8VtgmtFRC3T7tiCCtus5zHkW6LZSfky5rGKHH47zkeq6xrLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه ویدیو حملات به اردن رو منتشر کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/146393" target="_blank">📅 02:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
‌سازمان دریایی بریتانیا: ما گزارشی درباره یک حادثه از یک کشتی تجاری در تنگه هرمز دریافت کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/146392" target="_blank">📅 02:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
آیدیش:
@khabar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/146391" target="_blank">📅 02:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ایران از این نفتکش ها به عنوان بخشی از یک شبکه مخفی چند میلیارد دلاری برای تامین مالی سپاه پاسداران و عوامل ایرانی در منطقه استفاده می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/146390" target="_blank">📅 01:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146389">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ویدیویی که سنتکام از حمله به نفتکش ها منتشر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/146389" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146388">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: پس از اینکه سپاه پاسداران انقلاب اسلامی ظرف دو روز دو بار یک کشتی جنگی آمریکایی را با موشک‌های بالستیک هدف قرار داد، 5 نفتکش ایرانی را منهدم کردیم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/146388" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c99f81fed2.mp4?token=N6x7bjg7nBvfNp3QdloHSVqRT_IXbFZh5kiG4mUAHls5sv_jlL2ud7HV27Ty7bBArdUKHj6u72cxxNCFAVP4mi7u5wU17qE2fD0WhFg-nBaULn4N78_5NU5OOf1pak_St3C17naDZ9P4om9oE483uikU9SsyDs-cyjM6ubUyFVVBx1ITyNn9bx260RlUkZL4Wji_Pv0virUi5H4Couel0OirpeD9VvbOHEk4oSdsZDA_CJY9rWW1-13_6is_06W06Gz7I0cmFtRBB7K10x3jI8ikH-r0DryDkj-qwT639QV7c64tEUNn6iafwcOC_P1e_tT412t59cEmNZo7P1xgbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c99f81fed2.mp4?token=N6x7bjg7nBvfNp3QdloHSVqRT_IXbFZh5kiG4mUAHls5sv_jlL2ud7HV27Ty7bBArdUKHj6u72cxxNCFAVP4mi7u5wU17qE2fD0WhFg-nBaULn4N78_5NU5OOf1pak_St3C17naDZ9P4om9oE483uikU9SsyDs-cyjM6ubUyFVVBx1ITyNn9bx260RlUkZL4Wji_Pv0virUi5H4Couel0OirpeD9VvbOHEk4oSdsZDA_CJY9rWW1-13_6is_06W06Gz7I0cmFtRBB7K10x3jI8ikH-r0DryDkj-qwT639QV7c64tEUNn6iafwcOC_P1e_tT412t59cEmNZo7P1xgbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از شلیک موشک‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/146386" target="_blank">📅 01:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
منابع ایتایی: در پی حملات ایران به اردن حدود ۵۰۰سرباز آمریکایی کشته و زخمی شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/146385" target="_blank">📅 01:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146384">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
یه موشک هم رفته تو سوریه که رهگیری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/146384" target="_blank">📅 01:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146383">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گویا یه موشک هم رفته خورده بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/146383" target="_blank">📅 01:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146382">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارش‌های اولیه حاکی از آن است که یک نفتکش ایرانی دیگر با نام «DERYA» هدف حمله نیروهای آمریکایی قرار گرفته است.
🔴
این گزارش‌ها به‌تازگی منتشر شده‌اند و هنوز مشخص نیست این حمله پیش از آغاز حمله تلافی‌جویانه ایران انجام شده یا پس از آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/146382" target="_blank">📅 01:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146381">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هرکی موافقه به اسرائیل حمله بشه و انتقام‌گرفته بشه لایک کنه
😂</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/146381" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146380">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فووووووووری</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/146380" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146379">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فووووووووری</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/146379" target="_blank">📅 01:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146378">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هم اکنون وضعیت آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/146378" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146377">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری/پایگاه‌های هوایی «موفق السلطی» در منطقه الازرق و «شاهزاده حسن» اهداف حملات موشکی ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/146377" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146376">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/سپاه با موشک خوشه‌ای حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/146376" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146375">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFin4SLNJG-LxQVL43nv-AZYLSuy4P-TdXWwI0hOE_GkE5fksyQIpXzOuoOTYxnX4CPv7qzQVuEn_laVgH7EWVR6LLx1NQ10S1d45ak2y1xNTKLMnP9aA6N5qlw8l1JXyzs1MLRguvEzCbKaKc9yapRnb5D9vgcGKak_9OOBww8mA-sG0HK-iU-KuRIddDlWO-ljChES6Y8YlwgQaScNWKcW6BkcGGJoauI-VmAjEIfswYSrWtrR3GngH_09xNXfNM0O6VV-SOjB6o4yD53cn4kjxa_DZQnS4Y8h_zncyQ2b_gEZ1Kihvh2bM0PF5NoC0ggR8he3LxHB7JSRBAi5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هم اکنون آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/146375" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146374">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سپاه گفته خدمه‌های نفت‌کش‌هایی که تو اسکله های بحرین و کویت هستن تخلیه کنن؛ چون ما میزنیم
‼️
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/146374" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146372">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/حدود 15موشک شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/146372" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146371">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/حملات به اردن هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/146371" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146370">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/از ۱۲شهر ایران موشک شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/146370" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146369">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/شلیک موشک از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/146369" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146368">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
از اصفهان موشک زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/146368" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146367">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/146367" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146366">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
از بعضی شهرهای ایران موشک شلیک شد
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/146366" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146365">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فووووووووووووووری</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/146365" target="_blank">📅 00:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146364">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فووووووووووووووری</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/146364" target="_blank">📅 00:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146363">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری/فاکس نیوز به نقل از یک مقام آمریکایی: حملات آمریکا به اهداف ایرانی همچنان ادامه دارد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/146363" target="_blank">📅 00:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146362">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
المیادین: عربستان ظرف سه روز بیش از ۱۳۵ حمله هوایی علیه یمن انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/146362" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146361">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/منابع عربی: یک کشتی ایرانی دیگر مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/146361" target="_blank">📅 00:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tjh22K2sxPJSO9l5SrkcE_YNZzDQ-TZYhryo5VRRHVSEyeqGbXeAvlcoOMN25J0Cj_AefcVFYhnuBnFastirk_lCa65d5Z6gnnFkbG4qI30xvjXa75RR5aImuqzg7hJuiD1ZKSUKoQU6_Hz8u22sgBA8QzJtw-9fPOPMvI1L0meNMC-wZCYTd-vHZm7xLOFDz7wrUHYzY246CBI77UfH4eyNsXLHxqoEwKzKBJvBRwMlKjaR-sgUhEpftw4N6Tcl31FW-809dXlDYmExFeydZz-xMls6vgdNE1Q-3VPyJEu2zdRpXFPyP8kgykNcO9hvWymK2Y-LRcSnbx_b3-v5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیرو دریایی سپاه:
ما دریا را برای دشمن جهنم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/alonews/146360" target="_blank">📅 00:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
قیمت نفت: ۹۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/146359" target="_blank">📅 00:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
10 تا نفتکش فدای یه زیر دریایی رباتیک خراب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/146358" target="_blank">📅 00:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوووووری/رویترز: امشب در سراسر خاورمیانه آماده باش جنگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/146357" target="_blank">📅 23:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار صداوسیما: ارتش آمریکا به نفتکش دوم در نزدیکی آب‌های جاسک حمله کرد.
🔴
خدمه هر دو نفتکش با قایق نجات در حال انتقال به سمت ساحل جاسک هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/146356" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وال استریت ژورنال: حملات به نفت‌کش‌های ایرانی حاوی این پیام قوی است که هدف قرار گرفتن کشتی‌های نیروی دریایی ایالات متحده تحمل نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/146355" target="_blank">📅 23:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/146354" target="_blank">📅 23:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5385acef5f.mp4?token=WVCb-JRRK41SzKc8_D05sNONQlT12WZga0FO-6LKdf42QCC2V3yAWR8ZE1Drv-IL4BLUOGhgSP_XunioOPKfKbfWL8ldG90fb29ByrmbyIJDa07EVfq5TdGfsvDpmePgN9NeTwIFnK03LCHZUlvkQrFR1kjC0p1fvPA5tTJNaiHd_cBZFUrKmKw1RhDw_kc4K90m2dbz_3YokAZS8KUrpkTyrMAlRCN3UwUIBi78W2MEjlTwmHNzz-hk5JytyWqKd_gMb7iAdE7Im4ezonh2-PRw5Ao3CrE_UWidkYpIjzPoUb5KBIykYPD4FNSJYTb7-xkPhbi_FzJQWQDON4pBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5385acef5f.mp4?token=WVCb-JRRK41SzKc8_D05sNONQlT12WZga0FO-6LKdf42QCC2V3yAWR8ZE1Drv-IL4BLUOGhgSP_XunioOPKfKbfWL8ldG90fb29ByrmbyIJDa07EVfq5TdGfsvDpmePgN9NeTwIFnK03LCHZUlvkQrFR1kjC0p1fvPA5tTJNaiHd_cBZFUrKmKw1RhDw_kc4K90m2dbz_3YokAZS8KUrpkTyrMAlRCN3UwUIBi78W2MEjlTwmHNzz-hk5JytyWqKd_gMb7iAdE7Im4ezonh2-PRw5Ao3CrE_UWidkYpIjzPoUb5KBIykYPD4FNSJYTb7-xkPhbi_FzJQWQDON4pBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط مارکو روبیو به کلمبیا سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/146353" target="_blank">📅 23:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146352">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8KcoTzuTmc5OjVdr804XZaskzEtXjTZELbFdnap0hGKBmfkMq9UXwrOhMMJT3CUNEp5Qkbq0QyK5hwU7ogHc4wQqSv1K2WbThNa8kW7dNKgOVWffZPM7uzJCLM4m01sxOzcdLO9NoqW6mfHLQZrge0bYEBflRKPE9FiTdDjF5QbaUV574mXsi7Ws-_VTfMNTVuw-gHgkBnkoMlWbV0vjy6Q2OyCuoT9IdPAfk1ozJ_Uz0cCPWSlhjtOmM0hTTyLoHRk1VzKUJmptkD_ofiwOq-CaCtLHaIDPhTyVYrAOGB3IeaSNEPQjzRdIFwjNUTY5NO0Qoc0yyK51fu5lpSwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی : اگر ترامپ تنش را تشدید کند، این یعنی دیگر نفتکش‌ها، کشتی‌ها و بنادر عربستان سعودی، امارات متحده عربی، کویت، بحرین و قطر امن نخواهند بود.
🔴
مردم این کشورها باید خود را برای روزهای سخت آماده کنند
🔴
ایران هیچ ارفاقی نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/146352" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146351">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGSkoUKa-8VZbF62sTf8aCWIwGAConG8Kbk9ujjh98Iy_rbH2kkYFLdVqrKr62Nvk4NNlgEBT6izyX5on4VT6hQ_FP5R1DCGcdsyK99Xtz21ydJCgLPYJSI4pPqkJx1fqK-C8d0y2U-D_c6K4Jo7ccE_3ujvEfGM0r_Q831DHL3iGepd24_ysAgLy8uexw4_ZyFnQN7MFFf9XJe_nOBJmaEj3nm0vATTd8TmvDtuSrMNeI2sSwgNgf3Qu9MKM_08cxyQ3QJcK7xAHRwv4Rvzr7s9s1iHo1BDlMdSo0C-534rlD4HQZjbp0miqBCe2A94Eqq3RxrvvtdP5LKRntsKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا در یمن: گروه حوثی‌ها این درگیری را آغاز کرده‌اند و باید مسئولیت عواقب تجاوزات خود را بپذیرند.
🔴
جمهوری یمن تنها دولت مشروع است و هر حقی را دارد تا از مردم خود دفاع کند و توانایی گروه حوثی‌ها را برای ایجاد وحشت پایان دهد.
🔴
عربستان سعودی نیز حق دارد از خاک و شهروندان خود دفاع کند و از دولت مشروع یمن در پایان دادن به تروریسم حوثی‌ها حمایت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/146351" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146350">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=uZ-iYxsr3UxGS-wFCqwd0BPL62nIg6UNKlEveMKksV-4gOh-sRhlIB98jh-AxPxbeH3MSDjgJkS_pR2gmD-7hoa8sNSTWYrnwQb20ZhsnCo1mbzPjwiSDLq3T7l4Iy8lCH9sVnwOZeVfC0CdpDOQZZSufoeHAokcsALTAS_b0HD0Qn4ihsDQMuBpr-IwXZfyKlm2GAeiA2SmmiSifTL7VEw5DEATK1JqFOEopJm4nG_oLg66n4ZnVwBFcaqFOcAMXYCAeF28V3ABm49RZw5f8KR37ET_CKqoKa0H7JwV57DP4Ml_bPt2Zmy72RW1EzVFsjz92_BJUrGo7yQeoUhf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd6f07ba.mp4?token=uZ-iYxsr3UxGS-wFCqwd0BPL62nIg6UNKlEveMKksV-4gOh-sRhlIB98jh-AxPxbeH3MSDjgJkS_pR2gmD-7hoa8sNSTWYrnwQb20ZhsnCo1mbzPjwiSDLq3T7l4Iy8lCH9sVnwOZeVfC0CdpDOQZZSufoeHAokcsALTAS_b0HD0Qn4ihsDQMuBpr-IwXZfyKlm2GAeiA2SmmiSifTL7VEw5DEATK1JqFOEopJm4nG_oLg66n4ZnVwBFcaqFOcAMXYCAeF28V3ABm49RZw5f8KR37ET_CKqoKa0H7JwV57DP4Ml_bPt2Zmy72RW1EzVFsjz92_BJUrGo7yQeoUhf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/146350" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146349">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال استریت ژورنال، به نقل از یک مسئول آمریکایی: ایران دیروز، دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/146349" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146348">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM3gvLbuYmV4EOPsOHS3buWqulM9ddkKCJkLtPBqRJtsv_VSi8R3SjoXfq1ICqbfSV29WWFwp9bG4kuPKt0YAWc5gMdETUPbTYhr0j8x4ltUWY_zruW-Fj3FwP9ltsIg57FsqcHF85s92mhuQXFm_cnlSBHUHEpYeSiegsk8v1HYpq6eDV3lmZ1dofyO3fAp8U7czucd2V1FVRc5t61rQ4-u4VXHfZRH3xwxaIKeNAo5psfKFlvFdts5tkQlPFe37L9cKunzICcWbyDbDd2hRIBtIKElfrZo6vUOFgMqxEuj8YCFlcXHVbriZfcC9LnVGLV0Zff2KKmsi7d44JXz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / هشدار فوری نیروی دریایی سپاه: به تمامی خدمه   نفتکش ها در محدود اسکله های کویت و بحرین که میزبان اخطار می دهیم شناور خود را چه در لنگر گاه و چه در اسکله ها سریعا ترک نمایند چرا که مورد هدف  قرار خواهند گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/146348" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146347">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmNaraYHG3WQSIOsURgPWbrZvgXEEKwupAEGkYl828SSDxrRgBO01MxMZ9zsUB39zNbP0shuCWVsYzuQjKwY4cmQajXmv0KRykkp6PEv3qpHd3mkrSq5AFO-VMdAHzQNMJhdk2sFFc5-tCte1-sSLJEwMj-d1iUGN0MM6PLnmtI41Fcy3qIm3BXO6LkhqZJbEEOMFL4HD5tm2BWuL7xSuqiRJTmJLBsdKVJo-gPK2VAG3mktqqm7NRB0-25mlMVpEtS5G5WAja0PuP3PosrRIkK6QSAJHljUP4lChBKP4kKeNLTyvFNkemDpAx_-AkinAy0dNkmAORewTGd_Z2tEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند فروند هواپیمای آمریکایی در حال حاضر در آسمان هستند که از یک پایگاه هوایی در قطر به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/146347" target="_blank">📅 23:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146346">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/ دانشجو: حمله به دومین شناور در اطراف جزیره خارگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/146346" target="_blank">📅 23:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146345">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuHPJX-_9FfgJ8prOEsR8s22FBbJ_h4M0dCr9ipX6LFumgIuZkFdiOE_KIhHP2QN7vNeFuJynPkWrA24zUoz5qrSIOj-gIC5-tkjYoL-Mmrbmr73B3ioPpAU7ULD0vVyLZ3XwWyu3KlT-HVAX-MIp4S7sFEVqSPpDZZks-XDppA6wWZ_ZcGKbMbniWZ6WBMdH81nJTXXn95w7YZmvuZfrqsTM8CBz5wlNFFlwuEJVo9UA3nMnwjkTjvoxU8xRudPpbmcgBckzdPBRNjgrX_zeduh10iZM-V6j3zEA3ZzdzUcN2M13u8rCm-Bxbp64GnKLUWM9Dmqr_W-5j2oGbuShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت مجددا صعودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/146345" target="_blank">📅 23:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/146344" target="_blank">📅 23:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/146343" target="_blank">📅 23:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146342">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / به گزارش منابع محلی حداقل یک تانکر نفتی در سواحل جزیره خارک مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/146342" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146341">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از مقامات آمریکایی: این بخشی از تلاش گسترده‌تر برای اعمال فشار اقتصادی بر ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/146341" target="_blank">📅 23:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146340">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فاکس‌نیوز به نقل از مقامات آمریکایی: نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/146340" target="_blank">📅 23:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146339">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قالیباف پیش از این اعلام کرده بود: در صورت حمله به نفتکش های ایران، به شرکت های انرژی آمریکا در منطقه حمله خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/146339" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146338">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / به گزارش منابع محلی حداقل یک تانکر نفتی در سواحل جزیره خارک مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/146338" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146337">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه عبری i24: گزارش شده است که نیروهای آمریکایی نفتکش‌های ایرانی را هدف قرار داده‌اند
🔴
پهپادهای آمریکایی نفتکش‌ها را در سواحل جنوبی ایران هدف قرار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/146337" target="_blank">📅 22:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L654l9YYdUX64hvlpgnX7KZD3STXvTgK7f2r8px5xSXRtUr3lUVtzYD-ofVk4PWvrLLVj9K8zqoKC_6iY08BmtzI6MBtjrToTrvBJSE-x4WWWeX6IVAHX1muBxwte3gXFDTYuoo-2msUiN-hnVJuYGV__71uoaHzQyefj1YLJQ7OMCC2Ua7gYFPDtJMVeNw63TNqifX5Q8uUGitSNQY__jHZlj9Bh4EPavnyfzzOeK0bujH5jT4c8RQDYPneNKUPD0X_Htk4DTldjQjkGa1LGwkVLfpu6FmpOHhcMsNVK8SuemrmcyWmvlAvU_oTXDbdC4cdwfqqDYiEWvoypkn5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W78A79MYb1QrFWwNee0LMiwmuOt-j7zu5lKgAXOFdLXGfQk4pZF_H-qJtYgNZDULODOgLrH2b_Rc07qn-iLsYCGdxRMb3IQKKssN--dadqZJ0oFzQrlrxER37vpgVdn9GKja--snHAGkTZ6PbmD59M46vzMf2qP56voDobFJuIG7T4rYyV_iA5JmlVXnMOkIwIXwCus11jP6GgemSRS7yLdG2oY9AUyA50qrxhIxFZxS7Y2y9gzTkdmYNs4n7pDvT0axifMrP9g2wYrRqkwH_6QSzJHmoPZHGul_dRu0SSXMRhE-Fo5bdaK7qyg0Es8pOEB53vVEU39_te-3NRB6Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات جدید اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/146335" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146334">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رئیس‌جمهور برای شرکت در اجلاس بریکس جمعه یا شنبه به هند سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/146334" target="_blank">📅 22:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146333">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / به گزارش منابع محلی حداقل یک تانکر نفتی در سواحل جزیره خارک مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/146333" target="_blank">📅 22:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حوالی ساعت ۲۱:۴۵ صدای انفجار در جاسک شنیده شده است.
🔴
منابع محلی می‌گویند صدا از سمت دریا و در نزدیکی منطقه سنگ‌سیاه به گوش رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/146332" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی سنتکام به الجزیره: یک فروند زیردریایی بدون سرنشین ما روز گذشته طی یک ماموریت نقشه‌برداری از آب‌های سرزمینی دچار نقص فنی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/146331" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفیلترشکن BESTVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKljg_0GPwmjGjZxlGDJZnIiKCCF1CO1f6YVWcczxLhSgXmusLEzX6vA65GuMzpYdaNO7B2vnLh2TKoAD2Yrq3Q2Bb8SGJyBXMPgH5KKxARIkgwXtIktjsIPar4pc88uXx6c75cDWGJLLJI9tLbVqnhPSIHVf6Tx8b3s8-Vbt2x5EHaILvt-2naLerF7PQtgBHNhOwLaTVwrBFuQhIq3PuDqmUcjy7wBhqX7AcB5dtvc1hI_XvTjCi-C6kJwXAMhtkQMyleUS77hoBdESI_4WxChLR6KbW7lZe1doMrfNaP_DXFToaD4tw1YspgZ2YQ3JbZZRRxwp8d2LLwhk-CYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎁
فیلترشکنتو ۳۰٪ ارزونتر به مناسب ۶ سالگی BESTVPN تهیه کن!!!
➖
➖
➖
➖
➖
➖
➖
➖
➖
✅
۲۰٪ تخفیف
با وارد کردن کد تخفیف
✅
۵٪ تعرفه ارزون‌تر با تمدید اشتراک
✅
۵٪ بازگشت‌وجه
به کیف پولتون بعد از خرید
⭐️
کد‌ تخفیف : IRAN
➖
➖
➖
➖
➖
➖
➖
➖
➖
📍
۵۰+ سرور آی‌پی ثابت در یک اشتراک
🔥
مناسب نت ملی
💻
ویژه گیم و ترید
🎬
فیلیمو و فیلمنت رایگان
🚫
یوتیوب و ساندکلاد بدون تبلیغ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/146330" target="_blank">📅 22:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JujXzeWONRxeaqYEgFIDOHY3DOIR6udyJW_p0Hmf77c03KSOa2pRl8BPwWk-mBdEvZwanUXt8HLcY3mbwQFbhp1m81mJfB2JScE6o5ZxpihvN_LuKhMEsKbMzM14yZwuqzmfpHIMDCXbgwpW5vCTyQ1h-AvIn_BIUKZCNTH6jZ_BAkD0Rd1U-TP1b0HDOrsUG7mzT-9h0iINSxlq85pEp5ZWw0fRr8qqEmGyX8XCea9Oual7NSg1CNrjds9vmvKuH61dvx53XQG4KsjxPLAJQIQ5DCoSsry13TS6TGBYZzcZyoznPhDqoOLavw-K4GnkJv3lyFIFPcYJ9RQhrD-NTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/prtYP7NODIbymPmhUSUG_ScX0S2mU15-nDViwADnH9esC1xBqdyKmrRken9UOClF6bk7_g1W48VKPfTdNhxX8oHrUEuqJuemwWyefv3PF2r8hSgSDndk-viWjdUbHp71tki9IDdeYabeuP1ICV4NM0VbmndmU92LBTnQiMgnmeRKZOEvTbL7qsQb0c61PBJHp0GSVBXzy_VqiVqnFPMhdaZn0sWH5EfD-1UQowp32huq7pWR5PF9XlxB308HmsmEHFjfq0IMU8fsy25uek4MRtc1ad6fXKams133rkwSzJMGId6wg9akAr72CBDdzFMNAiIyRUoYSJvk4O_VnRZXSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پیشروی ۱۱ کیلومتری ارتش روسیه در دو محور اوکراین
🔴
گزارش‌ها حاکی است ارتش روسیه در جبهه‌های پوکروفسک و اسلاویانسک مجموعاً حدود ۱۱ کیلومتر مربع پیشروی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/146328" target="_blank">📅 22:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
لحظاتی پیش دو موشک از جاسک، در جنوب به سمت تنگه هرمز شلیک شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/146327" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxYxVMrQKPEd3CawnKMx9UzS5hD-ni_aSYxrPn_K83R8b7b9bIC7UwWWHIQLl5YX3nHhCl3E1QY_Q7EnILW2iefZDF8m3Mhln6AjBDw2E6ePgWgOvclYBH65ou6jFuFY5vK1eK7uNLIpVyOJoL01N0iCmw7XLnoFCEWucjoqq319y7zu-NFb7FuykET3gRGeLUOMIU5lbWB8kr0JAuwwUowx_0SEfniHhMaTftMsjZs6Wo8GfH7mwfKMV9Z-GJF48zidHIzcy6elmM8DPS9xUTURB9RVY43FKGk7OPNuwLJ6ATmy25HTQcvPvWv79Awb7tohU7l-ZpNZmAYxfoiZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : پس از ۴۷ سال تحریم، آمریکا به نیابت از اسرائیل وارد جنگ با ایران شد؛ جنگی که پیامدهای فاجعه‌باری برای آمریکا، از جمله برای جایگاه و اعتبار این کشور در جهان، به همراه داشته است.
🔴
پس از آنکه واشنگتن نتوانست با تحریم یا جنگ به اهداف خود دست یابد، راه‌حل «ابتکاری‌اش» این است: تحریم‌های بیشتر!! جدی می‌فرمایید؟!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/146326" target="_blank">📅 21:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز: این زیردریایی بدون سرنشین چندروز پیش دچار نقص فنی شد و به دست ایران افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/146325" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146318">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZt_jVRJKlrMPVAyKOzwxlW6mtCLvQmpzFhmL3iYpXz9OZ0s2ureK_P06VOKsYLNp0FdLjGnJGtpqHPqxnlmoM62XQLmJx6ETCbJb4sf2EqsRuvc9r8A7lui7QMTQahqu1DWndSLbICFiKILFq61WNoflu9g_ooVvAHlIe1FgwH2ML2kMhy2EvSkknhicRSYMCUU5rLwrqadwmEDgIErSQItHfLTmdAYPjPh0X1GJHLrrJoT_Jf6JPkkv07F4DxJzT8PEW7JlwufupKXXpVDu538MMKFsWqens4MIGVZB--z2-a8AyZPuG1st8Q9BUJWSO8_EMUg4cICW3Lyalft8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Js--cu77uHjtG3Oc3TSgYsX33QI8b9d_Uqwcp2UI7HL4vlEv5ueNHHRZ4_wjLot8ps2ghiVWk8z1_tD5WNn31aGhO079u_M-lN9itNpAZ7aSnYxPBcEqPVbY7cHK1053tiW2_LN0Pq0hQ0slnuSe5twaBqLy69I7F_Sw8M5fwBaLGfKbwuYGNGXNKIBNSlfB-0BkknUNqAMKXs9C9IZdy8Pzd0GNUvSFdpdiWU28TC88AGQvrRRYLcapoRwLCimoNiEY45v2F7_u9IPlDShGRKepO-raEYhooAxoIqJyzvkyRErNYax8hYSVgekC9FjafA5DrUL8rvEiOjG8f_KbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie8Gb8MjdcpKfwkRPYXHhJ6Nex_w4rGYKGKhRE0t91s4l0qR59QFsNVIMNrAuQSR3GbeKnHWHL4R10w3Ut1n5c5ln2_9RHwSt8xaI2GpDyNylDWHtrut9MjlZmfx2mVhkMl1kRP1ljcGPq5-GOVWaNOkhTPHEtR_wYXFa2jAueUxO7Lq9nbHcc-G-hZ8RVV2stm0ec54K06Xezpa5G-lCctaTeO0JiK2YWmfZKDPzedClapAYXn-6NmRjT2xcZtIFRmiQK1k-9zWWTSGS4r-00-KMdI5q9mcuB4-KDiYyq2SBvcf6H_7NQwdpYlHpUnHjm_PtSM-4jCXt3CryWBPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3if_TZrj08_rNhMatinR6nb1n6CLbpYzlMM0F3sqcuja7TtcS4H1odR006HFQ63Qe2xNrDrIZlx8QbuoPESIetVmsU28Lco7t0CUD9oXcIDXSZy9FdkE97pL2k3_mUDk0jYsPF-tO4q_ELKDRpI1X_cryADZ3dVNJvP8AxbbsVkDVHXF9shZB-JJbqr-SoO64xcAgjnmQ5wl9IGAFmLXmGnzFpUx72b9UqFEYUKslSLTEDpiG0DLTsXZTsy9WJuQNd3de16DO3T3Xt9eO7Zp9hacIcxBBKzObQ0gI-UMPHN7o-FUzMTuA2uXXsEHwZW91iWHchM-STHeaSVBMwPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXoqvIV_B29RinW8fFFT8fCFXykEFrajkD9AB3H1TDquUfzbdhL278qJqNhmZ-hnxVdeF6m9nobjFyNieq9zlQdaGDnfCnTmv5AtKsvRREsm4RCzRnov3gl4G6BzRlBirpStBu5JM3Iz5ns_YkzQsqO51lJHmCm__Tp8X1sH8d04viWR6BhMZ8HpFSCSNzu8B5mTEvnkmuSu_yZ7EqmD_svCnqLxe4fphcZLlgQSBwdMjwdxTqdXW7X_5BODAJ5zEBpp9uLdikn6pA0HYWkju9-XROmTKCwOFO7N-Zmeocwt4P280cqZsL8F8_ZKYjNjK2Z-gu2zfqB7fJxCGRnczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jH174UUnqfzJ0RRaC3_mEr2kiCwjE18luz7pP38nIhFf4LdC2HadFi0f2aKSBy07IYfkOwE_tmfJG6ut4-qUVmVJ5xjjKjOeBqPHCvwDGzlIomPryFJFjo3XOKKQL7QUYav1dWDJSdpob60Do5k7nGvXG6GkuFRJwDO0PeNfVr58kia5WyEGyLXCB3m8dm5nRoP-pA59mw1JDjtVkhAXbm-BDg-5U9x_dsvgPr_TwCfUO7XVTn4vWMdIBHTCn5FXW-lDl5MdO3QY63fzLUzu57GCHLV2y0b-ASklWZyMRu9hZOayavQKUPWYIcg_OadPpCz0hgmk25UNWA0_PU0Upg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ec47ba7d.mp4?token=Z7LdthY9sdugipPO3_LrSWiXeNuG26t7OjyW6o0K-XPfaqjLux5ltVaZNjoST9p2RBRPcERP0atDXyiZyeHGpJszsiah81fuAg1kg--3wF7ZZ-Fmo9vOHo7dlm540XbFdwpTfJw5s7zSvyx9G2gHUU2vBJBh8W_2-o2jZyv8dPeCvtg3-p6OGwVdlyN9yFxDsGGajT05UpbkbC4teytKoT88KyTNAzx2fdVomYlqusIo-PtDoEwjN3dQMNnKNUOFRxt7Jelpn1Z0sHDXauLsWx_yWj5-069bYhA-OFBOLPwFUVCRNpW-LhRmEb8n2WeaIg6Um_sRqsmVHWNYxQxy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ec47ba7d.mp4?token=Z7LdthY9sdugipPO3_LrSWiXeNuG26t7OjyW6o0K-XPfaqjLux5ltVaZNjoST9p2RBRPcERP0atDXyiZyeHGpJszsiah81fuAg1kg--3wF7ZZ-Fmo9vOHo7dlm540XbFdwpTfJw5s7zSvyx9G2gHUU2vBJBh8W_2-o2jZyv8dPeCvtg3-p6OGwVdlyN9yFxDsGGajT05UpbkbC4teytKoT88KyTNAzx2fdVomYlqusIo-PtDoEwjN3dQMNnKNUOFRxt7Jelpn1Z0sHDXauLsWx_yWj5-069bYhA-OFBOLPwFUVCRNpW-LhRmEb8n2WeaIg6Um_sRqsmVHWNYxQxy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از زیردریایی بدون‌سرنشین Dive-LD آمریکا که امروز توسط سپاه به‌غنیمت گرفته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/146318" target="_blank">📅 21:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146317">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPMCCFBd4RMDSObgVRxAhXhVB1SN1gTo_-6txp3RMqdOPrCFiPUM4sxBle8SOnNOmhNT744pG3LrP2_Hsu-S-oqDbQwkYJsLIe9xFdMACo6TW7604tTp_YuXF1JpMp6On2UbbKd0N5jdeus7bwP2pB6P8ePBba1dHJamNgu-AKCRl6Vl8Z4wF5ncuEukh7R-YChexWY6C84b7G91gemJktP2VVJqOZ1MwzWIYc3Ix550F9FcKZRzgoxVyyBKRpETC9N5K3l45OMwTyNDAh3oEDzJ0a8T3w2jYyChlv3W2GdJZPqqY0c7IMdlu4N3enAjAa-FdJjcl_MlEF7Tf2AG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون‌های دود پس از حمله موشکی یمن، آسمان شهر جیزان را فرا گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/146317" target="_blank">📅 21:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146316">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عارف، معاون رئیس‌جمهور: به‌زودی مبلغ کالابرگ افزایش می‌باید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/146316" target="_blank">📅 21:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146315">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد
🔴
اکبری، معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:  کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/146315" target="_blank">📅 21:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146314">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9191d8e017.mp4?token=OPLYDmxGzZhEhgccnP4yBdkXdoYAklSEInCkzKMvCAbmk867ptROg_SZ8uu9cSEU9ZXB7-2OHUnR180wpKwiaSpZpcZS4dc3TFhUw2fvGwUTcbw4GaVkzniD7-gEF01tvCCxSuXEzEsuHgR9c5FsD61XJEFwpVRBYk41OehXABEmLGy2pJbuhmxwUKwTjrqlw8gL09QXTcCUI1zGycXRU8fDqVhUBKXVUkdgDyKGlS3W1EvnE3m6T1o74UqqhkdPkeG1_ze9dYQ4H9X_AJf_efyxoPVclxvIn1yJcSBWX76UHamfhLB4EtxuS4Kj5eVOJUie4EJwkxFVQ2CFYJzJKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9191d8e017.mp4?token=OPLYDmxGzZhEhgccnP4yBdkXdoYAklSEInCkzKMvCAbmk867ptROg_SZ8uu9cSEU9ZXB7-2OHUnR180wpKwiaSpZpcZS4dc3TFhUw2fvGwUTcbw4GaVkzniD7-gEF01tvCCxSuXEzEsuHgR9c5FsD61XJEFwpVRBYk41OehXABEmLGy2pJbuhmxwUKwTjrqlw8gL09QXTcCUI1zGycXRU8fDqVhUBKXVUkdgDyKGlS3W1EvnE3m6T1o74UqqhkdPkeG1_ze9dYQ4H9X_AJf_efyxoPVclxvIn1yJcSBWX76UHamfhLB4EtxuS4Kj5eVOJUie4EJwkxFVQ2CFYJzJKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی طباطبایی معاون دفتر ارتباطات رئیس جمهور: ما هیچ وسیله نداریم جلو آمریکا استفاده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/146314" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146313">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی کرملین: از تردد آزادانه کشتی‌های تجاری در تنگه هرمز حمایت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/146313" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
دولت بریتانیا در چارچوب بسته جدید تحریم‌ها علیه ایران، فرود هواپیماهای ایرانی در این کشور را ممنوع کرده است؛ مگر در مواردی که معافیت مشخصی صادر شود.
🔴
این محدودیت بخشی از مجموعه گسترده‌تری از تحریم‌های مالی، تجاری و کشتیرانی علیه ایران است.
🔴
لندن پیش‌تر در سال ۲۰۲۴ توافق خدمات هوایی دوجانبه با ایران را لغو کرده بود؛ اما مقررات جدید، ممنوعیت را به‌صورت گسترده‌تر برای هواپیماهای ایرانی تثبیت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/146312" target="_blank">📅 21:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146311">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPFzcXaqD-77hvAVjFKFpvmcmZiiNavCmm038P61RQMRq5jjF92U2WwtC9-mMOHAOd_h2C5LPvWe0b7EHFIbBxG68Knod76FNQddD2Z5nkEnXsSh8tK0Jy0i0A0-Cuw4Z53ly1RZaqgcI_Q4LKhv0KPQBs85znxu-rgNkYZkYcAf4fe4yt3FJqoxo1KKNVhA8fBUHK-s8NIIMxOcidqmFgVJuVEmij86jgUESbyI23S9X-gfUdrt1Y7x3zopQtOj8EvaoExtyydRkWRfawtL__9EsvWSmi1dC5L8P9fMpMxAfv4HLm2ke_T3wC5G9lxqtjYL-fS5gNO99JyMDzWoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل چند لحظه پیش حملات هوایی را بر نبطیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/146311" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146310">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/146310" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146309">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu9z8IGe5OxDzr6TOB8fWrXYQwIZNIp1JaZ78FLj2qZh7DpaHLSE6Cq43K0jHEPSMLDu1A7dDcisAht1eD0Cw5rZhplAPwcQDqOO0rZWIsZzO8rO5w9klxn-AJa0N08XyH7gdLyPZj9H4x6PN2Oz2t1KebQ28Kq9IumohORoHXoqkETEQgWL1TW7fJ6X8vFXo2KZaY1r9zRTQioC7WwRgXGZnyebBN2hETZEVS4b4jZOv5m8LZvlNlujyh3gYW_jUTQ3BPecQrSX8e2ashk56VnxItLVvPkaqUvZUU7qC5qvnMPx-mZ4_D43kGv6Ew8QuM1OSj746Yn-ASEHMoJq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل
:
گزارش‌های رسانه‌ای نادرست است. هیچ هشدار از سوی امارات متحده عربی به نخست‌وزیر قبل از ۷ اکتبر داده نشد.
🔴
اگر اطلاعات مرتبطی وجود داشت، از طریق کانال‌های اطلاعاتی بین دو کشور منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/146309" target="_blank">📅 20:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146308">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI3ye_Ef7MSxN66lGuYD8N-fVsGOtWLXlCAFbvAQRv9-3VHn2-EMfxgevwfpv_WNLp7e9pPzZRofZoe9cLrZoPo9nryWjEO9fU1nfDct6gTvyDfBwNSlpjZIUJrzukvXbWC98XZ_134On5Rq7LyXNm9aUtEYoAiFcgcmvyaTtw3VlXxEs8QBs_wqDmzpg5nPY6GyedttXV79eTOSTw9aSIxdrCdZRMO2CCHI5McIi-R3p7nkLH1OTQpRLZV0UrX5UVlN0oe833XZaLoocm6dFowYjsnAOH1eNsdlS1w3PhoioGHwk1d-Ug__XPtcLnzsdYxQUgh5Q_aDhbRL9rddig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت اپل، فردا از آیفون ۱۸ رونمایی می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/146308" target="_blank">📅 20:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146307">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anGznIZQFr9YtmEbml1iuB-XrIHPSSRzNINfZjCZW4rSfp7pkxJpsHzGlW3aRXIRpfd4miFAUn2wwm0EHLXU3kR9SjtojQAbWD-RmR_rTUrOcJLh_c9KRRzVLnYNqmqHZS7yBdSAksnA8bE2_lbkXe4SvuqbCcoJo9dOS6cZGutVhKGE9k6WBWbEIinBAE_Kd4zkx_eqy9m6FazqHRjoO9rSGbvPfTYF5c0NqYyoBlDPZbTxZ_6rhohkaVD-7C88-63NOAfTtmiNK00g4OwEDhrhUPO-CKOWknnQqBYh5XPLY4Wv4eysMyBRlgwUUlj5kH-HsIe6guivh01xVfJDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارها در نجران، عربستان سعودی قطع شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/146307" target="_blank">📅 20:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146306">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
عربستان سعودی: سامانه هشدار زودهنگام در منطقه جازان فعال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/146306" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146305">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0dd43b40.mp4?token=AWs8VLWP2th2ydcBm_PyqU3b96NrjCUsEJWDGDPesWmsOEaeW4wJ7w3N51IOhdrJvsHqzEect2X2GhLoQtbQHMNquZ8_X_BS4EZZfe8OAQ6xZP_rg79sMLgJHmCt6PczqcN55IRtDq2S_EzSbFdX4Fz71V_w7n7dJA2nogVPXnvepO05jS2Pst0RbOKWjJW2GaiMFIura5E619_RxV5kmG7rF-yPsftqxbU5vAtWdbwk8fUs12fX6tDPf73Q98Z6cTRpIxWpGzyRUlbar0Ld_jmz1bwe5edMrsECGcjlRhNm5pEIcFwiz30zx4vM7BXAT6P9QWqxvuLnga99AWCcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0dd43b40.mp4?token=AWs8VLWP2th2ydcBm_PyqU3b96NrjCUsEJWDGDPesWmsOEaeW4wJ7w3N51IOhdrJvsHqzEect2X2GhLoQtbQHMNquZ8_X_BS4EZZfe8OAQ6xZP_rg79sMLgJHmCt6PczqcN55IRtDq2S_EzSbFdX4Fz71V_w7n7dJA2nogVPXnvepO05jS2Pst0RbOKWjJW2GaiMFIura5E619_RxV5kmG7rF-yPsftqxbU5vAtWdbwk8fUs12fX6tDPf73Q98Z6cTRpIxWpGzyRUlbar0Ld_jmz1bwe5edMrsECGcjlRhNm5pEIcFwiz30zx4vM7BXAT6P9QWqxvuLnga99AWCcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت درباره مراکز داده:
ما باید داستان واقعی مراکز داده را برای جوامع توضیح دهیم.
🔴
همچنین باید اذعان کنیم که در این زمینه تبلیغات سیاسی زیادی از سوی چین وجود دارد و این اعتراض‌کنندگانی که در مناطق روستایی ظاهر می‌شوند، نتیجه یک خیزش خودجوش و ارگانیک از سوی جامعه نبوده است.
🔴
این اعتراضات بسیار منظم و سازمان‌یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/146305" target="_blank">📅 20:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146304">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae902a64.mp4?token=DvM09FNfPc9pNaAFytNlQaRBoyJyS-5w3eEmDLneOOwTx5O4cf5oq_Rz4loCcxgUWgrfeY7H9YyaKu0QxArIToNdrBqDsYsRkkKaVaNPYaXztwi02D-e6a1NBQ_EMke70WJa_a-uSsHMetPNdkcBNZUpuQDFZspOXffRR4rvu1mYgJLWRgguIB0AZktGsR4Ge0LKv0MEnuAoYwz-vFPUTSyJ7LMnALtqVL9ZgKa2Gj4k11y5AEPBp0JZaFjND91bklTTvY4AXbSljihB1LiZ08vAxbEQtXffOTXmjxg9iCNi4wxqZhvOuEIaVcFXZnP5voCaadXHD7Rn-xH1ErgfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae902a64.mp4?token=DvM09FNfPc9pNaAFytNlQaRBoyJyS-5w3eEmDLneOOwTx5O4cf5oq_Rz4loCcxgUWgrfeY7H9YyaKu0QxArIToNdrBqDsYsRkkKaVaNPYaXztwi02D-e6a1NBQ_EMke70WJa_a-uSsHMetPNdkcBNZUpuQDFZspOXffRR4rvu1mYgJLWRgguIB0AZktGsR4Ge0LKv0MEnuAoYwz-vFPUTSyJ7LMnALtqVL9ZgKa2Gj4k11y5AEPBp0JZaFjND91bklTTvY4AXbSljihB1LiZ08vAxbEQtXffOTXmjxg9iCNi4wxqZhvOuEIaVcFXZnP5voCaadXHD7Rn-xH1ErgfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت می‌گوید اگر چین در رقابت هوش مصنوعی با آمریکا پیروز شود، گنبد آهنین «اهمیتی نخواهد داشت»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/146304" target="_blank">📅 20:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146303">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0931e227.mp4?token=g6vzSKQ-_RZmSV2eqJpnqsoJzpSoZdr0_JCLkGof4OQNkkSntw_SlcOEYqGv82NfKKitYy64oAN9SSrI9kYi1YNjBn0mp1rZRxNr2oJMmjWQLpq40_oOJnKvjT8xQLa9eLH2B7kNK2wEbCa7tqFIH7w51meqCJ41M4aDWN7SgZR-yDPXUHP-O-EWm6hccwsqU1dx_S9pXP9_vwCy8ar_NCJRRe40bYGmVVy4TQ0oSpixtL1coWFXsgLvZ2jGu3A_zZ_oahH5IFeHZmMz1S-TbIXizM9ZI7VZthfj4VkmzcfDYbQAVQl5ParxAKZHjbvWjKzKHgYfgPxFLIB_Q6Whbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0931e227.mp4?token=g6vzSKQ-_RZmSV2eqJpnqsoJzpSoZdr0_JCLkGof4OQNkkSntw_SlcOEYqGv82NfKKitYy64oAN9SSrI9kYi1YNjBn0mp1rZRxNr2oJMmjWQLpq40_oOJnKvjT8xQLa9eLH2B7kNK2wEbCa7tqFIH7w51meqCJ41M4aDWN7SgZR-yDPXUHP-O-EWm6hccwsqU1dx_S9pXP9_vwCy8ar_NCJRRe40bYGmVVy4TQ0oSpixtL1coWFXsgLvZ2jGu3A_zZ_oahH5IFeHZmMz1S-TbIXizM9ZI7VZthfj4VkmzcfDYbQAVQl5ParxAKZHjbvWjKzKHgYfgPxFLIB_Q6Whbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت
:
هنگامی که اتحاد جماهیر شوروی فروپاشید، اقتصاد لهستان و اوکراین هم‌اندازه بود. اکنون اقتصاد لهستان سه برابر بزرگ‌تر است.
🔴
اگر اوکراین بتواند اقتصاد خود را به‌درستی مدیریت کند، این می‌تواند بازدارنده بزرگی برای روس‌ها باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/146303" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146302">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007c3cad6a.mp4?token=G1PWLC7y_pDUa-IkAvqslpu7R2mhnGMkovE653Do5lGMKlM3kyPGh8Dvju3yLjHpO9nHbaZnsvXkEfjIbZHFnV2Y5dpwmKCN5dRUGwVlvKGTYFXnmeHCPuZ1FotRQelRy1kme4qPwk-z4jKfO7iHerR3db4tGA0_UNI3mNKBe4U_5rnOVfoPFVhl1TieY-ipzJu0qSybFcmA88alSs6sw9-8ZquB6dIHJCIPd4V5XJvg_AL1Gq4b4gg4F1V7ptvcMEYleknwIpbFH0ZHPAcLtMz7yYfgbzmWbgV9sIH7PiNsv2afEl7oBiYym3hY4zvvHdCCzrMaGGKiADK73RCiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007c3cad6a.mp4?token=G1PWLC7y_pDUa-IkAvqslpu7R2mhnGMkovE653Do5lGMKlM3kyPGh8Dvju3yLjHpO9nHbaZnsvXkEfjIbZHFnV2Y5dpwmKCN5dRUGwVlvKGTYFXnmeHCPuZ1FotRQelRy1kme4qPwk-z4jKfO7iHerR3db4tGA0_UNI3mNKBe4U_5rnOVfoPFVhl1TieY-ipzJu0qSybFcmA88alSs6sw9-8ZquB6dIHJCIPd4V5XJvg_AL1Gq4b4gg4F1V7ptvcMEYleknwIpbFH0ZHPAcLtMz7yYfgbzmWbgV9sIH7PiNsv2afEl7oBiYym3hY4zvvHdCCzrMaGGKiADK73RCiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت درباره اوکراین: آنچه روس‌ها در حال انجام دادن برای اوکراین هستند، یکی از بدترین چیزهایی است که در طول عمرم دیده‌ام.
🔴
اما اگر صحبت نکنید، نمی‌توانید جلوی آن را بگیرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/146302" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146301">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d29fdee52.mp4?token=GGjmNHmzlrxvXEDecbjBEfkHwwQAYrJ7szVsFAIrgmsXCxAWk9i7JABmHNX2H83enoW9L1Nt5UqFwljSjO-i3l63JKOrTY3G1TF6RkSs--Jiz6A5xGa_HpNvdSw-QwojC9fbDRV1GfjFKckgKix1A_WzJibYl2syGA9FTpDgQCz_N4YAfofP6MQtD0YHh79WhAs_xJpg70UZlSB-YrE4QRFEBDc-qmIrvbI89wh1TKs_xpvbnlAIBCQICQ7xuwk9Tx0REcPhyxy_E-Zh5vE9VmXiedh7TahTbDJKblXcJ6C2iVH_XBQszQ1MxftP854MDdTyYb2GJMzB9Hpgizi6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d29fdee52.mp4?token=GGjmNHmzlrxvXEDecbjBEfkHwwQAYrJ7szVsFAIrgmsXCxAWk9i7JABmHNX2H83enoW9L1Nt5UqFwljSjO-i3l63JKOrTY3G1TF6RkSs--Jiz6A5xGa_HpNvdSw-QwojC9fbDRV1GfjFKckgKix1A_WzJibYl2syGA9FTpDgQCz_N4YAfofP6MQtD0YHh79WhAs_xJpg70UZlSB-YrE4QRFEBDc-qmIrvbI89wh1TKs_xpvbnlAIBCQICQ7xuwk9Tx0REcPhyxy_E-Zh5vE9VmXiedh7TahTbDJKblXcJ6C2iVH_XBQszQ1MxftP854MDdTyYb2GJMzB9Hpgizi6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسنت وزیر خزانه‌داری ایالات متحده آمریکا درباره مقامات جمهوری اسلامی:
مارِ ایرانی، یعنی رهبری، هنوز نمی‌دانند که مرده‌اند، اما مرده‌اند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146301" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146300">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192ff7f923.mp4?token=kWQAk9aLHIQ99ehLohIRqaGBr4U9iyOfiO1qA6SZJvfDsipSD0e9symKhxEiV0U4T62U1QwPwe3wpMhE3W5yA8UcUJ_oYl4GbCietl-UTNPNOiX0Rva5GooPKY-pWNUQHiCYQ0va0ne_q14-aNbcyV2ryHaMG1dpSHNucTaBCNB_DtEGh09liHhaNPQwFOuGhG4w_5nxt-Rr09NRZb7kj3A7nXLwZo6EKtHFQQ9n9F8R5HYmO8gE_pp6vOi-dwoUsMktnaJShO7u6z_FBMJjMgGk4PNURNuuE9boMue_VUZMz6jRPb035piI8yQKokmndTFxfzF3jKlD7JskX_CbOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192ff7f923.mp4?token=kWQAk9aLHIQ99ehLohIRqaGBr4U9iyOfiO1qA6SZJvfDsipSD0e9symKhxEiV0U4T62U1QwPwe3wpMhE3W5yA8UcUJ_oYl4GbCietl-UTNPNOiX0Rva5GooPKY-pWNUQHiCYQ0va0ne_q14-aNbcyV2ryHaMG1dpSHNucTaBCNB_DtEGh09liHhaNPQwFOuGhG4w_5nxt-Rr09NRZb7kj3A7nXLwZo6EKtHFQQ9n9F8R5HYmO8gE_pp6vOi-dwoUsMktnaJShO7u6z_FBMJjMgGk4PNURNuuE9boMue_VUZMz6jRPb035piI8yQKokmndTFxfzF3jKlD7JskX_CbOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده:
ما فکر می‌کردیم مهم است که هیئت روسیه در اجلاس G20 حضور داشته باشد.
🔴
زیرا اگر قرار است صحبت نکنید، چگونه می‌توانید این جنگ وحشتناک را حل کنید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146300" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711062d2d3.mp4?token=ZoIOsWUFaIkfR4-d5oY_Mv3gd5wgK43kEvlNd5j9b3jwS9ae5I7odHZpulrbCmMTpepeY2aCUvZnms9Jlwe2TvoDldmdwUReWBD4971qGfjbY_wdNYrxrDpoSc0P4B2_9yKyuLuOeLtRMSZRPoavN1AWk8GWbtHPJ4Ng8e4C-fCUa1uK2Mz92dx1bb5EK6zzyZAJbhsBfaFsTJX47_PHd60Xoq2qRWn1O-1U2-sWeziBc2GT5TuTb4D9T0i51739Tlh35Ooz13aOiWUbHgWvDa4lODBfe9E29DqU5WhY8Psg_CrDH8_Zfao36mMnF1Rhxgm6-M09dNkQNph0DZ0DNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711062d2d3.mp4?token=ZoIOsWUFaIkfR4-d5oY_Mv3gd5wgK43kEvlNd5j9b3jwS9ae5I7odHZpulrbCmMTpepeY2aCUvZnms9Jlwe2TvoDldmdwUReWBD4971qGfjbY_wdNYrxrDpoSc0P4B2_9yKyuLuOeLtRMSZRPoavN1AWk8GWbtHPJ4Ng8e4C-fCUa1uK2Mz92dx1bb5EK6zzyZAJbhsBfaFsTJX47_PHd60Xoq2qRWn1O-1U2-sWeziBc2GT5TuTb4D9T0i51739Tlh35Ooz13aOiWUbHgWvDa4lODBfe9E29DqU5WhY8Psg_CrDH8_Zfao36mMnF1Rhxgm6-M09dNkQNph0DZ0DNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد سیلی که تو رشت اومد، مردم دارن با قایق رفت و امد میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/146299" target="_blank">📅 20:12 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
