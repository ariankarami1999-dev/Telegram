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
<img src="https://cdn4.telesco.pe/file/ullXou7PZ7gIyA9p8zaw5DYdgTi3Xo5EuYh2MZD2vyKidwaewUA_vFUQKaFdLyWSRxODIjVDPJbAGhiXHP1Em3LGlCp_iJEN0OcC6RU--gEtElNuiitTMlyv89E1X8UCo_6fQaFV_OLOqc22UA9V5DXeC8JAIIeAKMlJ1OatSHRzJngEY4ykkirGfP3Tztti8uoG7K5AZs0tstkXdx1_RhIlKZu7baQN5uMQOE39NKvpIgocpwoDXmp2Pfjd5azLYNvrtDVet1TjDZyXidt6PfWjVLYxXHNHfGcXeCto4PDTKUXn0Y36BlgPj7dQeqAd-fno43mkrxZ-YCEFcI8JHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 03:16:29</div>
<hr>

<div class="tg-post" id="msg-652456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtKjEm3KX0w7Te-5orQzpBKMcmCi9dP5YBriJ69CsB8Y7U2cjN5dAELSgjY94t0cWgSC0bs4pmy5ZvCCUoCHWo5v-n4JKHCEemBRD4E2Y0LqlSWr_H3EnoJsWn2UDg6uMMfzL4xHcDj3pJwous808ejQS31V7mjZG87L7tKyrZx3VqyXEpJUuHaoa6I5gqbUyamw2TVXu2hMTooEO8f-7Dn9MJQOWS4YE9SiuGaBpUYZwuHNbZ6nOqzIxUjYkqlwjYAsbEx5KljxgLwZep0iQab-FkdIJpbOJrQtQzHI63DPuVzAt1FZQJZgj98dWbeO7eW3yWedIj3SIU0mgrrGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر کاتولیک‌های جهان از آمریکایی‌ها خواست تا با کنگره تماس بگیرند و قانون‌گذاران را برای پایان دادن به جنگ ایران تحت فشار بگذارند
🔹
تریتا پارسی، معاون اندیشکده کوئینسی: فوری! پاپ لئو چهاردهم جنگ ایران را ناعادلانه دانست.
🔹
او گفت این جنگ «هیچ مشکلی را حل نمی‌کند» و تنها باعث گسترش نفرت بیشتر می‌شود.
🔹
وی در ادامه از آمریکایی‌ها خواست تا با کنگره تماس بگیرند و قانون‌گذاران را برای پایان دادن به جنگ و تلاش در جهت برقراری صلح تحت فشار بگذارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/akhbarefori/652456" target="_blank">📅 01:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGHsmG6fe57ECRNVKrz7tFy49dNE5oQeq8OTINJ3Zqn-4tzu1eWV3kL3_0fWy22TSzVRPNTSEqOBSulzArFC9x864qVSbsjiNENZ9JtDzRKxq4mNscuiehIMI5vO1sar9yCvn8qEn3DDqNkQpMzCpt9BuXQBzNzTKg8SnWj61IrGhlDTqmc87h9RYGJQzvRzH02CJn1lvLM-aQS5ethtkEl2HL2iI4cY6KS_ciehE8Ty1tkKrU9knymLgyNNEs0P0iq1g0nv0V9fIEXOj2BATR8lc3bRThbfwCfWC5Uv4BpLhNJs9cd3muZrxZj3qVVr17B-xz2f85K2d8YAXQe1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسته بودن تنگۀ هرمز برق کوبا را قطع کرد
🔹
صدها نفر از مردم کوبا با حضور در خیابان‌ها و روشن کردن آتش نسبت به قطعی گسترده و سراسری برق تجمع اعتراضی برپا کردند.
🔹
کمبود سوخت عامل اصلی قطعی برق در کوباست که به خاطر جنگ آمریکا و اسرائیل علیه ایران تشدید شده است.
🔹
وزیر انرژی کوبا می‌گوید، ذخایر سوختی که روسیه به این کشور اهدا کرده بود تمام شده است. وی آمریکا را به خاطر بسته ماندن تنگۀ هرمز سرزنش و تاکید کرد که قطع جریان نفت ضررهای زیادی به کوبا وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/akhbarefori/652455" target="_blank">📅 01:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: دو مقام خاورمیانه‌ای ادعا کردند که آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه ایران هستند؛ آماده‌سازی‌ای که بزرگ‌ترین سطح از زمان آتش‌بس محسوب می‌شود؛ این حمله ممکن است از هفته آینده آغاز شود
🔹
مقام‌های نظامی آمریکا به‌طور غیررسمی می‌گویند پیروزی در حملات جدید بسیار دشوار است، زیرا ایران بخش زیادی از توان موشکی و زیرزمینی خود را بازیابی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/652454" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx--FyJnXBcKu3SLj2agxdYNOWhRfp0AD6nxsHpU7Sywve68LrXYXxl8w903YOTVBOxcVFeXasWvikA58L_uoSme5MDggGmBa0cj_9SlPa-PLbgR-jDPtatdGj7ZKVNWRU1eFMscJC7eqWEObMPk36SHV_6mDItPjv7ImHqfSzVtvMwylRonlFCtatvjQgjGH-EqFJH-SpAFDsLjVNU2-IewoZ-kDmU9x-br4Na_IZebYyRt9NRt4NXCOu8fzp0xRvKiJIUdM_ghc49bl02ZxqOa9YM4TXhxFvnNJ7vWMs8FZozuIzaHzCF4_Fu-QhDURdaN2VPsSeZt7nqH6fo8aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران: هیأت حاکمه‌ آمریکا شریک جرم اسرائیل در نسل‌کشی هستند
🔹
وزارت امور خارجه ایران امشب در بیانیه‌ای به مناسبت روز نکبت با تأکید بر حق بنیادین مردم فلسطین برای مقاومت علیه اشغالگری و مردود خواندن هر طرحی که متضمن کوچاندن اجباری مردم غزه و کرانه باختری از سرزمینشان باشد، اعلام کرد: هیأت حاکمه‌های آمریکا شریک جرم و همدست قطعی اسرائیل در نسل‌کشی فلسطینی‌ها به شمار می‌آیند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/652453" target="_blank">📅 23:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5dYE83DsAUEo6_DZ5Ck89K5x4-uqw7vgDWILPr1OxEjQtAAsSQwD3q0QRkt6ozbAeoSBGP6XmVeFCYM7pz4Bbq8UHa0DtW9-hKilnnucI90RnswlcvH8JzGbaGIdGvy7OHGiv_9oeyIrs0Jo1c59AVkIR3GZdYb23nIG3QIjkYk48fk7njWU-eb5UV0DWDZYDXCvAgxMi9Grk1yfIpEQxnjzLaSMBLPmnZliQParq9Nx7jrZcafxGxKAC436O0bpIzRIbPHgkTkl8YxvfMASiRR3gGgjGXigLeQ3GUJ4iBHeU6Rb3DMH4mCeG-EfwTqnCHDFPswfQr7fFt_g65mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهنامهِ ایران
رهبر انقلاب:
🔹
ملت عزیز ایران در دفاع مقدس سوم نیز ثابت کردند که داستانهای اسطوره ای فردوسی واقعیت زندگی و شخصیت قهرمانانه آنان بوده و مفاهیم انسان ساز سلحشورانه و قرآنی شاهنامه همه اقوام و اقشار ایران را در حفظ هویت اصالت و استقلال خود و مبارزه با ضحاک وشان متجاوز همدل و همراه می‌کند.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/652452" target="_blank">📅 23:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhtmYwTBLYK2NDa9DskaTjtryHaE_hK-tuwWF0gusyA2d7IXlfj1bLhqt-RS-yuA3BpDEwWLNxsu0KNQDyYLZ_SRukV49SfIVomIO3YxAsgiIwOL1m4IPBeZUm6EiF6cgCeRh54x7nZaFNgKbte0A2LxFBhFIrSRovZcQATzthwPdbEhqono4C6PeNBhuj14Pqwo9QeIWqzT7wkVCWsA8R--75CcDtGrRJtAYP1BE9B9nSwORy5cy29Q7VWlzpveA1dLspDdjbggioemBqa4k1e09O7gIPtFp0h9D3dTZvAclD7ghcUgtHABM9cA7kn-jKECEddXGlox9m1sJpi81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
*بیش از ٪۲۰ کاهش وزن با داروی جدید داروسازی دکتر عبیدی*
⭕
بیش از ٪۲۰ کاهش وزن با داروی جدید داروسازی دکتر عبیدی
اپلیکیشن تخصصی «مان» با همکاری داروسازی دکتر عبیدی، با استفاده از دارودرمانی زیر نظر پزشک و ارائه روش های ساده برای بهبود کیفیت زندگی، توانسته برای بیماران خود بیش از ۲۰٪ کاهش وزن به همراه داشته باشد.
آمپول لاغری زیکورپا (ZCorpa) به‌صورت تزریق زیرجلدی هفته‌ای یک بار استفاده می‌شود و مصرف آن باید همراه با رژیم غذایی کم‌کالری ، ورزش منظم و زیر نظر پزشک باشد تا نتایج مؤثر و پایدار حاصل شود.
📌
فرآیند درمان به صورت کاملا آنلاین در اپلیکیشن «مان» و تجویز دارو تنها با تشخیص و تجویز پزشک انجام خواهد شد.
🔻
مشاوره رایگان پزشکی</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/652451" target="_blank">📅 23:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
در لابلای اخبار، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
بن‌بست تازه در مذاکرات اسلام‌آباد؛ آمریکا پیشنهاد ایران را رد کرد
👇
khabarfoori.com/fa/tiny/news-3215084
🔹
ترامپ رسماً اعلام کرد: یک دور دیگر از عملیات نظامی آمریکا در ایران در راه است
👇
khabarfoori.com/fa/tiny/news-3215168
🔹
آمریکا برای این زن در ایران ۲۰۰ هزار دلار پاداش تعیین کرد
👇
khabarfoori.com/fa/tiny/news-3215122
🔹
بحران در بازار مسکن؛ ۱۰۰ درصد افزایش قیمت، ۴۰ درصد کاهش فروش!
👇
khabarfoori.com/fa/tiny/news-3213856
🔹
علائم عجیب و هشدار دهنده آخرالزمان | وقتی شوهر به مرد غریبه پول می دهد تا با زنش زنا کند!
👇
khabarfoori.com/fa/tiny/news-3214791
🔹
ویدئوهای جنجالی را در آپارات خبرفوری کلیک کنید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/652450" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXX-PeVjjHOZQyvwUfIEaVL0_2upK_6vQtSdhxRLokO1R03SUnELfG5Yyf-K77jAKcAvrWb4BIY4-FM0MAXhRpS90EvubqzsZsdm26vix-EbHBNoXccREpgF7aHjp4xy32IjSWmc12ZKe8zLDGh3Qweo0DzEvGpITRuzTo7yul7n1Rdk8YBSthD1J31uGEf0lSNd1ZKX8no1v11OSJF2ErLnAb29-PPHyaTX1of32InpA5Wvf-Wc4FS3JEHjd1WeKyi-0YDA2AADV68krpKzURPj46pUMsk_2wLhQzpN0syEJMmc-P-K8RXlSNgHbW1J_bxSdQF2BUmjFDrdwuMQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری دومین نشست مجازی مجلس با حضور وزیر تعاون
🔹
«گودرزی» سخنگوی هیئت رئیسه مجلس: دومین جلسه مجازی صحن مجلس با حضور وزیر تعاون روز یکشنبه ۲۷ اردیبهشت ماه برگزار می‌شود.
🔹
دومین جلسه مجازی صحن مجلس با محوریت مشکلات معیشتی مردم و پیگیری اقدامات حمایتی از جمله کالابرگ برگزار خواهد شد.
🔹
قرار است در خصوص تأمین کالاهای اساسی مردم و کاهش فشار بر دهک‌های پایین از جمله کارگران و خانواده های فاقد درآمد و جامعه هدف نهادهای حمایتی بحث و گفتگو شده و تصمیمات مقتضی اتخاذ گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/akhbarefori/652449" target="_blank">📅 23:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651e0e3dcc.mp4?token=VRR609CrXDyRk8digRryLgzVM1BOXjy3RtdNhj_iKfQB_hL7lzGq55m_ZbVhQQp1UbBQgUdxF6NFDYUueq9delKlmRDuzaDyS4-nbagEvPFGyNYq0elNXrc87AM-mdrAUegN05ckZkQRjABtiwWToqJZEj64Ti0cZGwu_7yNX2Iz8h7Lw8fbY5o05f2xLwzfFHbMviEwzX6N6dfi2sFi6gp88mtJTNoWgKvNepVp5QbY6aMmMkv8Iw-VZdhDm0Dl_cRb63Fmk3RlhRB589oid1OMCsnVdbGZorEkXwvB1_P3pgobfW7G0M2sBHFFTmEnUA5wfYBjHMLVqHXKV8Pbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651e0e3dcc.mp4?token=VRR609CrXDyRk8digRryLgzVM1BOXjy3RtdNhj_iKfQB_hL7lzGq55m_ZbVhQQp1UbBQgUdxF6NFDYUueq9delKlmRDuzaDyS4-nbagEvPFGyNYq0elNXrc87AM-mdrAUegN05ckZkQRjABtiwWToqJZEj64Ti0cZGwu_7yNX2Iz8h7Lw8fbY5o05f2xLwzfFHbMviEwzX6N6dfi2sFi6gp88mtJTNoWgKvNepVp5QbY6aMmMkv8Iw-VZdhDm0Dl_cRb63Fmk3RlhRB589oid1OMCsnVdbGZorEkXwvB1_P3pgobfW7G0M2sBHFFTmEnUA5wfYBjHMLVqHXKV8Pbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داستان خلق درفش کاویانی ...
نسخه کامل را اینجا ببینید
👇
https://youtu.be/YrDeYT6DO1Y?si=2RpPQjKDe8vTJ-4g
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/652448" target="_blank">📅 23:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b883Ha5bmZfkF2TCi31pTggomuQcoxjA6Jrrau0y_FMg6o1zH2paJA3qzF_nIoRK6K-gIxyI88rHsvdY8zqKy78UXlMKHZ-Fw9xJYd12W-QmmEnC3OypYTcseXHtVrkiHzN-j9R1N7D0TSK4jPVa0K-yFoNrfxvL6jFs6mJFnH-Y5Lv-yFfT0uLy9Ng4pijTkfeJjNDxzPaGB26KXvuFQnYRa3icOm7uLUI6jlSFhSs66TFS0J0CKAaOXEP6erSGh8HY2peKGQs0yP025mjN6FJ8qg4tzhfC2hXUpSfvdGfTXgSJMqR3ucdx5dy4rqkkrET0tMnshUYWkq3b94iDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستاوردهای چینی
🔹
سفر دونالد ترامپ به چین تقریباً هیچ دستاورد قابل‌توجهی نداشت، از عدم توافق برای تحریم نفت ایران و فشار به ایران درباره تنگه هرمز، تا بن‌بست در موضوع تعرفه‌های تجاری و تایوان.
🔹
تنها گفتگوهای اولیه درباره هوش مصنوعی صورت گرفت و خرید هواپیماهای بوئینگ هم کمتر از انتظار، با ۲۰۰ فروند در مقابل وعده ۵۰۰ فروند ترامپ نهایی شد.
🔹
هفتصدوپنجاهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori
,</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/akhbarefori/652447" target="_blank">📅 23:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyAG89BVuSoGB4YJ0PVQA2xsR0rKZXXrypLYnm6g3aHlI_yvP5dNNvV4nNWxfYJ-WDW_NlX9NA1p-ZYxgYzaiLagK9YSAi7dcglLEsbY1wRiWVKaTCDyGkT_lpu_vxeAxhdfWIo_arbmOUwIfyvG2q0zPAGENSCUJ-BMA-ycbKpdPR8F4KLcVZwvtwnPh8DnRFZ_0_-Rb5-7Q3l_Dzme-mw99dWS8zGkH_ZV3R8XK_lowaeKIAdYiMQFuTg6AEs66jFltRDN-hhUrZc24YaCVbEEf-AZ-727kIYsSBtKkyTsOTdaLT1AdjKlEvSc9Q6nb-WxYsAJk5d1xpgsu3CpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت خارجه به مناسبت «روز نکبت»:
🔹
هفتاد و هشت‌سال پیش در چنین روزی، مهیب‌ترین تراژدی انسانی و اخلاقی دوران معاصر با اعلام تاسیس موجودیت جعلی صهیونیستی در سرزمین تاریخی فلسطین شکل گرفتکه پیامدهای‌ فاجعه‌بار آن در منطقه غرب آسیا و در سراسر جهان مشاهده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/652446" target="_blank">📅 23:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2iPCVfeBF0cQWXFq33Y5nrrQKsO48gGlmULuf90muCpkdU3coFou8BtmbMWNmNIROuKwFtSu30gsIO8ys78QjOERAvF3xWiiFAhtGcADb996vat-obasuSsuNPK-MZFMHC-NbWNazmCFw5qgxkXgh9Uet-9K4d6vQZKe4ACMll91hwfu3NfhWL_pwnRW847NWuiVYt3h7AwbGIGxzuMUn2Q5_etYqDHlVRDB1lRDCWW3pO-huLHon8QTrnnnzFR-36u_7oRSDP3m3DNxJ_vMxDlof9sptRng9UGvueU74JnO7jyPIoQ_AMxVS9zqM57PDCq-3BeR1KDEWd77qpNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراض مردم انگلیس به استفاده از پایگاه هوایی بریتانیا در جنگ علیه ایران
🔹
تظاهرات‌کنندگان با تجمع مقابل پایگاه هوایی بریتانیا، خواستار توقف استفاده از این تأسیسات برای عملیات علیه ایران و خروج نیروهای آمریکا شدند.
🔹
معترضان با بنرهای «جنگ با ایران را متوقف کنید» و «آمریکا از پایگاه‌های بریتانیا بیرون برود»، سیاست‌های ترامپ را «مرگبار» نامیدند.
🔹
این تجمع پی گزارش‌ها مبنی بر پرواز هواپیماهای جاسوسی برای پشتیبانی از عملیات در خلیج فارس شکل گرفت.
🔹
سازمان‌دهندگان اعلام کردند این آغاز موجی گسترده است. آن‌ها معتقدند هزینه‌های این درگیری فراتر از توان جامعه است و لندن باید به جای همراهی نظامی، نقش میانجی‌گرانه ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/652445" target="_blank">📅 23:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961e48dba0.mp4?token=BLZ7nKyDAwFaV5CFZv0-sruNj9_30JXJK07aJSTC-29jNCD7U9w1oa2rkkmB0qZFBX7eAzGkKOpbk0nBwS6ShHsxfwI09VfwoxR5WLXHpMNZae5hqlurFCZHVMLczoUvRCX4fXhcAYqd1k1fxKhW1sm-l9ouJbsf35MjAc0wW_hf_-AQOso87dl3Dp-pKA1Pi3FF_ZbNr2wBjP9ecKTLxCp1pXTqctJqKoWNbY6gvXHvqArHScm6w4iBOm6BKUhQnUmeuYAVZ2XnqE5rdYGSl6am3snjiMfb37kcZpQon6SucDP2wVGGPo_5rUoJvHg8V9znTuIkTr-x1npHOFWVxms6HoEXEhoNzyisVfkfSl2SQPx4LYci3ZgxDHH5frd83SaYFn093OqQlQQXqFL7AD5u__ssbxjHW3Ofw8o5_W6cg6pZtJpfDD8tkYXKj-uTYHserSxQlBpPvSS5t2CPe1T7UT3LjTp0UtD0ZyMxa8ifgH6Fz8ulr9VZx7vwUREwIMSBmVTJrFVHFX5KnZ10NxQOwSFsAgLdFMSOfHvzDKH-XwJBkaFfuUYcdn-7bUivagpEMtVUItjwTquK-wL9dIY5kd2uRKjExyuL1Z7AJMj4UJaViHnyvjEuHFpOiMcGSXHK_WGIb2nrNCpEQpJSZSveajbjLk24FbhYPvlddRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961e48dba0.mp4?token=BLZ7nKyDAwFaV5CFZv0-sruNj9_30JXJK07aJSTC-29jNCD7U9w1oa2rkkmB0qZFBX7eAzGkKOpbk0nBwS6ShHsxfwI09VfwoxR5WLXHpMNZae5hqlurFCZHVMLczoUvRCX4fXhcAYqd1k1fxKhW1sm-l9ouJbsf35MjAc0wW_hf_-AQOso87dl3Dp-pKA1Pi3FF_ZbNr2wBjP9ecKTLxCp1pXTqctJqKoWNbY6gvXHvqArHScm6w4iBOm6BKUhQnUmeuYAVZ2XnqE5rdYGSl6am3snjiMfb37kcZpQon6SucDP2wVGGPo_5rUoJvHg8V9znTuIkTr-x1npHOFWVxms6HoEXEhoNzyisVfkfSl2SQPx4LYci3ZgxDHH5frd83SaYFn093OqQlQQXqFL7AD5u__ssbxjHW3Ofw8o5_W6cg6pZtJpfDD8tkYXKj-uTYHserSxQlBpPvSS5t2CPe1T7UT3LjTp0UtD0ZyMxa8ifgH6Fz8ulr9VZx7vwUREwIMSBmVTJrFVHFX5KnZ10NxQOwSFsAgLdFMSOfHvzDKH-XwJBkaFfuUYcdn-7bUivagpEMtVUItjwTquK-wL9dIY5kd2uRKjExyuL1Z7AJMj4UJaViHnyvjEuHFpOiMcGSXHK_WGIb2nrNCpEQpJSZSveajbjLk24FbhYPvlddRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«ناوگان پشه‌ای» ایران بلای جان ناوهای آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/652444" target="_blank">📅 22:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLM1ZiyJgTgig9olTMWAwPOKnlrDM4vPrc4Esa0jdxGy5_xXEnzwc5w6MJhRuQRPH4YAt1oLSYHhgh_Qe3F2m08Y-0bqT3WhYuYCK0nVrnSyRYQXXKDRf9Dprw-arJCOMWgNNz19j19ib0XlDeHQWZd8c4SQ-_K20WD2r4MUyyIA12oloVx1gJCO8KUJvxsSCSPIYsHB4hOk-k6Z2KZY36Y-qjSmZfEjXqnJPv_INRUXeJhQlijAEyKX6fuIZYGvFvbC-AJdn3k1gbjOSxjbVcz60io0ZYEo9G3J6DDYFZLx5XYRLvwjJQdMQGxGgylcDAH6rOKMh3Q8W3SXtS4jkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زندگی تسلیم نمی‌شود
🔹
حتی در باغچه‌ای از پلاستیک، طبیعت هنوز تلاش می‌کند نفس بکشد.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/akhbarefori/652443" target="_blank">📅 22:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b036fe427e.mp4?token=YKThofcT86ryQ-JNoYdrlTDxKaNDIB9LyIHnLG2fMGVb2RwbZGvXphHc6YAeco7y7ZItJq06LP2QEOGmWTDikmVjwW_-TcZkDUijncwH6qd2TR2jv-Km09SeGY40-GEino06I3kFELGfPlZTZ6Uz8ovr0AHBe6vQW6lBhD94GCgUZZIvL9hhCehQM0VYaOGLOG6S9Lvsn_Du-UwRfTrtTJE3nQpF5s0sNDoRHbFWY9ZwQ2dtKzk8X7fbe7vEnraJEbrZVbuorY3-91heLvtL4JM72Qcam2R-9bVCqK05j7-AOun54qHkbaymsW8j-W78q3IIzrOGJWDG94fkevgdLH29FXJ5U0Jd9cq_uVCjhcSM8Xr11wYTz1tjblA80x9_mfX-Yxg-NA6mich7kKTb-Cfr28pfn0YRshs5F9e-6CgEQ8kFeiw9AJEyCOunoNpoVZvOeppEJwoBRh4seep-_uHdP4JwGglTrHacjS9YNZEb_h9-niH4qhsQQ48TcCWMEC_5S_ahjzYFG1UGLGoGBjAWvw5jLmhh8973l7Lkgjl4bYo1i5dELLKtBU-QnlLaQQz2MjsjGhqRNXgHVF2bhe5VcgmSKZTxoNXS3HRZXfO9D_yZFbYgVwZ9vX4pmWOQekPFP2EuiFfNOT6oe352-1d6CVVXkDafK0LxNugmWIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b036fe427e.mp4?token=YKThofcT86ryQ-JNoYdrlTDxKaNDIB9LyIHnLG2fMGVb2RwbZGvXphHc6YAeco7y7ZItJq06LP2QEOGmWTDikmVjwW_-TcZkDUijncwH6qd2TR2jv-Km09SeGY40-GEino06I3kFELGfPlZTZ6Uz8ovr0AHBe6vQW6lBhD94GCgUZZIvL9hhCehQM0VYaOGLOG6S9Lvsn_Du-UwRfTrtTJE3nQpF5s0sNDoRHbFWY9ZwQ2dtKzk8X7fbe7vEnraJEbrZVbuorY3-91heLvtL4JM72Qcam2R-9bVCqK05j7-AOun54qHkbaymsW8j-W78q3IIzrOGJWDG94fkevgdLH29FXJ5U0Jd9cq_uVCjhcSM8Xr11wYTz1tjblA80x9_mfX-Yxg-NA6mich7kKTb-Cfr28pfn0YRshs5F9e-6CgEQ8kFeiw9AJEyCOunoNpoVZvOeppEJwoBRh4seep-_uHdP4JwGglTrHacjS9YNZEb_h9-niH4qhsQQ48TcCWMEC_5S_ahjzYFG1UGLGoGBjAWvw5jLmhh8973l7Lkgjl4bYo1i5dELLKtBU-QnlLaQQz2MjsjGhqRNXgHVF2bhe5VcgmSKZTxoNXS3HRZXfO9D_yZFbYgVwZ9vX4pmWOQekPFP2EuiFfNOT6oe352-1d6CVVXkDafK0LxNugmWIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: نباید اعمال مدیریت ایران بر تنگه هرمز را به کسب درآمد تقلیل دهیم/ باید از تنگه هرمز برای تأمین منافع ملی استفاده کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/652442" target="_blank">📅 22:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556fbab204.mp4?token=TdIQD_phuypLkXKSAoJ_fkEFcUHJjqudZok7EtZ6sdBs6_6zhzc3CIy46U0-4LMEokpV_wpThuiwkSLMIL8feSS9mpH-q9eLIVPT8ZtmgcqW3YPyTWPtd8i_weYjPSEqpSVEyaW9nnmwdIUVOpE2xXl_EmuDd4neFB4rfzRCXiWvuKIgfUG8ePH4WdAxPJXkBFYBhyoJqQRXV3T05Mln-Z332D89nGhS7ntjI1FFpathnW6SISWRsO2CZXQd_Gtxq4cAzIoBK9MPQ8JZhwfxc-K00MFmuyaqft5-PiTfdyb1xSFp4sikdD5qRoVJnZCKGPsR67zL1L6MMYLLpRhGNEiRO63WinjjJwXOJka_4HJxGlLEVxBgBBfWYPLwVp6HOAVOoSg8_uxPpSTX2Z_TjiWH7qFjTBq8pfiFqRu_EIRywpq4NuwqP81xK-9SZbOzibWsm1Iem6ro2YXAZ3GcEtPCOtTOWTqHBHyB-LTttTDupMo5cGnWIcdYerY6GlUk8VEX4eKDbQ0ldo5WI_Wb41jkA9GzUMHW8Dy7pGnWVdfmaJ9tyMl8oSOFDWZpg8uHBwb1HABTFnVmd7DPtPTe5GL1U5-LcUXXdvfahilgb2jKT5Un2eWCvpVORt5ZXmo5VcHU4FkZe5RjfBYqhlF2pfFoEEln-zx82NmseZVDPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556fbab204.mp4?token=TdIQD_phuypLkXKSAoJ_fkEFcUHJjqudZok7EtZ6sdBs6_6zhzc3CIy46U0-4LMEokpV_wpThuiwkSLMIL8feSS9mpH-q9eLIVPT8ZtmgcqW3YPyTWPtd8i_weYjPSEqpSVEyaW9nnmwdIUVOpE2xXl_EmuDd4neFB4rfzRCXiWvuKIgfUG8ePH4WdAxPJXkBFYBhyoJqQRXV3T05Mln-Z332D89nGhS7ntjI1FFpathnW6SISWRsO2CZXQd_Gtxq4cAzIoBK9MPQ8JZhwfxc-K00MFmuyaqft5-PiTfdyb1xSFp4sikdD5qRoVJnZCKGPsR67zL1L6MMYLLpRhGNEiRO63WinjjJwXOJka_4HJxGlLEVxBgBBfWYPLwVp6HOAVOoSg8_uxPpSTX2Z_TjiWH7qFjTBq8pfiFqRu_EIRywpq4NuwqP81xK-9SZbOzibWsm1Iem6ro2YXAZ3GcEtPCOtTOWTqHBHyB-LTttTDupMo5cGnWIcdYerY6GlUk8VEX4eKDbQ0ldo5WI_Wb41jkA9GzUMHW8Dy7pGnWVdfmaJ9tyMl8oSOFDWZpg8uHBwb1HABTFnVmd7DPtPTe5GL1U5-LcUXXdvfahilgb2jKT5Un2eWCvpVORt5ZXmo5VcHU4FkZe5RjfBYqhlF2pfFoEEln-zx82NmseZVDPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دعوت به حمله مسلحانه تا دفاع از عاملان قتل در رسانه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/akhbarefori/652441" target="_blank">📅 22:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6f50fde5.mp4?token=Eyk6r0ufSLHxy_JjRDw49J7_R5SZC-IzTZoNmIo32v9C92S5oWDiN-x30Yj3vbKNRFvn_oXhlk9k4wVAxpbnGjTf8FNw64sqBW-7lhXvD--qqjEr3LSrVZo0J0TGfD2qCKdeB11ZaRXe7Zfr-aTUlxD1mp1VfuciUR31i4tPEBgnLmO9iarfQWM_OJfAnQ4GZuOTZAanWk0YHrpbUTgPY0aUrME3kbpUCSKj2XGilDNyJRASboyy26Zbr9iNH0aWaJoURv0Cq6CKCoFI99FuTbGTIO7gpBw1SQ1nq1oRCXRM44kePECQwvNekeye-pVOVqHYIxxZq7iKjQsMvVEHAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6f50fde5.mp4?token=Eyk6r0ufSLHxy_JjRDw49J7_R5SZC-IzTZoNmIo32v9C92S5oWDiN-x30Yj3vbKNRFvn_oXhlk9k4wVAxpbnGjTf8FNw64sqBW-7lhXvD--qqjEr3LSrVZo0J0TGfD2qCKdeB11ZaRXe7Zfr-aTUlxD1mp1VfuciUR31i4tPEBgnLmO9iarfQWM_OJfAnQ4GZuOTZAanWk0YHrpbUTgPY0aUrME3kbpUCSKj2XGilDNyJRASboyy26Zbr9iNH0aWaJoURv0Cq6CKCoFI99FuTbGTIO7gpBw1SQ1nq1oRCXRM44kePECQwvNekeye-pVOVqHYIxxZq7iKjQsMvVEHAYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: ایران منتظر کوچک‌ترین حماقت آمریکایی‌ها است/ ترامپ لات کوچه خلوت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/652440" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd37f5ac2f.mp4?token=IDUTFVCKOE68ri7rn6nHbIhgugWlTi9JdGhyGfUpqyOXFb77HaBLYvPkv8pUnEjUd3q8aS_f9zeNv2YkJVkKiWq3_0SQgJsFcOuWoZYW2WAn-vmH31sFoqncx6EMRY-bX-Izg-8FkkpjgxMMIsJv5TRkkoHOSa3RzhHOLYaElDov1WueKGVa1bDEVe6cxQWNmIeuAELTUg2sTfxab5MUpdlr_pXP48rGi9s3-7OJDGA7QOQuRtG-zg4tN_Gtsb5SOJQP5Q6h2ts2fp_5gzUjh_gOXrInhiHasGY7c4xO8PRXdkz2t8uoXN-I8587tXUKrjHsqquyErV2K-4g-3AlEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd37f5ac2f.mp4?token=IDUTFVCKOE68ri7rn6nHbIhgugWlTi9JdGhyGfUpqyOXFb77HaBLYvPkv8pUnEjUd3q8aS_f9zeNv2YkJVkKiWq3_0SQgJsFcOuWoZYW2WAn-vmH31sFoqncx6EMRY-bX-Izg-8FkkpjgxMMIsJv5TRkkoHOSa3RzhHOLYaElDov1WueKGVa1bDEVe6cxQWNmIeuAELTUg2sTfxab5MUpdlr_pXP48rGi9s3-7OJDGA7QOQuRtG-zg4tN_Gtsb5SOJQP5Q6h2ts2fp_5gzUjh_gOXrInhiHasGY7c4xO8PRXdkz2t8uoXN-I8587tXUKrjHsqquyErV2K-4g-3AlEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوزات وحشیانه رژیم‌صهیونیستی به مناطق مسکونی غزه در شامگاه جمعه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/652439" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 49</div>
</div>
<a href="https://t.me/akhbarefori/652438" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌ونهم
رائفی‌پور:
🔹
0:10:40 داشتن حب و دوستی نسبت به اهل بیت از اصول و پایه دین است
🔹
0:15:06 نشانه های آشکار از شیعیان واقعی
🔹
0:27:10 فاسقین چه کسانی هستند؟
🔹
0:34:00 وصیت پیامبر به اباذر در مورد حمد خداوند نسبت به اولین نعمت ها
🔹
0:42:30 تمام شدن حجت به همه مردم در آخرالزمان
🔹
0:49:00 بشارتی که خداوند به مؤمنان داده است
🔹
1:06:50 بزرگ‌ترین نوع کفر و شرک در آخرالزمان
🔹
1:23:30 چرا اکثر انسان‌ها ایمان نمی‌آورند
🔹
1:46:50 راه مستقیم چیست؟
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652438" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Subw7rmskg3UTdK3xIASfCNRSYiA-arSi6MXgGEOdPaY7j8LsnzrA50h-7HRjKT9YRjzqN26w0ZaObMhr66WyFSVdPeAhUfMtjXCohdVI7UXXG_oOJiJWkY-Y1PlCY1I9jZ5KYf5bIJLZN1oaE6StD3fjBLXQOWa9MHKhg5rkZ4xZqHf9ClLz1evbMly_kYNVAn7IuvcJaeZjfzNjNoj7H0pU9LhF0TtR9Zwtsb7lPtkn7WD5Tkr_ixeSe7UWcVYiY-ZFFDPtY8cpfPcIZco67YbzB4wt5ahLpJ2HQaiYYjGWexc5W9u6CVa7RJ4s9oLl7iLZ0u8Xwuu_n0gm_Dckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIesWeCe2Q3VQpbnkj6a599LNzQ5i2uXd8V9NK3cjUYxFcereDNW8MByMSV-msz3WO1kap0qwqI4TO3XagAtygSpGV1PuftYbJDs3ZwwLvo-PVCGrXI4SQRV5rUd2z4squPKcNpZZxf2DqRnbZWhBCDtlASRECx952moeAjoHQxr2-up4CZamFK616qfGfR4xriSnIyCE_gDMToTyxWpgtftoSide1kaNBmlJYbSo2cIfIdweeKntD4Bgfs8kz2EkVWQjRoxB0Ws-0kHcf7B5tMK_6EKRWxnABLNh_SKARQ2XsF-Jbvzzfo0y6Z4tLth0BtCOrBXvhSqVMCrl1fRCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی دستور تخلیه برای مناطقی در شهر صور (جنوب لبنان) صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/akhbarefori/652436" target="_blank">📅 22:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fc19884e.mp4?token=vk0HN-xb4liTA_3PbwpJQ1scHMmNLUN_JkBLf0l3nc20IVjLwSxNv6f6ovsgadt0dRPNxVF31IA9GbWxFfMPOIZqNrk748Sw7C-GSvJCMDAFJML-cvhWhlz6_oRZYkFKzoI4IBsPtAg1whO5R43n8l3gOHXA09WeD68NoDE526wqdsxxHAJ3DLhVlyzFJ0QdaOmeef5Fe-0XHS0A1ARAmNb6Amk5EFufcjLL8fbMKuOkK7Ef4GJsLXKK7MwbulwR4ZtNXp6B0ZyLF7uXos_JcnDWjPG1DqiMGnSFLMWvAWtv59xQENb3comfN4DDKNqFvzcr_4tWyVAKeidm63R7Tqim9XzM7YexonEkXb5gq01p_bg278kNYtQv0lYxXBVLc4-z1JaF1B_BL4AMsihuWpR_ggSXqU5iUJlfOhj8sJLDVjmWU7Csz3bH0gSy1dqFYHAHWc2EmWeOFlNDJxffkVMo6kNDilS-l5ZYmE2YIglNmxwvfW_UwbaOTONjcN1uAapFgXwVBCVokorcilkNxs_MlRbPUnkYEuXx-v7hMNqYOY8JlLzhcVhPA9V4DP07xFyPIlnBaBJPjqdIwOwqUSvjJc_OZV_y7MmasxkgQFCA0eyYyDQE5T1-Wgx2UTxHZumate_v0fhWUiPoZLmbNPNUDfLTSMxOMp_1HmhfxVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fc19884e.mp4?token=vk0HN-xb4liTA_3PbwpJQ1scHMmNLUN_JkBLf0l3nc20IVjLwSxNv6f6ovsgadt0dRPNxVF31IA9GbWxFfMPOIZqNrk748Sw7C-GSvJCMDAFJML-cvhWhlz6_oRZYkFKzoI4IBsPtAg1whO5R43n8l3gOHXA09WeD68NoDE526wqdsxxHAJ3DLhVlyzFJ0QdaOmeef5Fe-0XHS0A1ARAmNb6Amk5EFufcjLL8fbMKuOkK7Ef4GJsLXKK7MwbulwR4ZtNXp6B0ZyLF7uXos_JcnDWjPG1DqiMGnSFLMWvAWtv59xQENb3comfN4DDKNqFvzcr_4tWyVAKeidm63R7Tqim9XzM7YexonEkXb5gq01p_bg278kNYtQv0lYxXBVLc4-z1JaF1B_BL4AMsihuWpR_ggSXqU5iUJlfOhj8sJLDVjmWU7Csz3bH0gSy1dqFYHAHWc2EmWeOFlNDJxffkVMo6kNDilS-l5ZYmE2YIglNmxwvfW_UwbaOTONjcN1uAapFgXwVBCVokorcilkNxs_MlRbPUnkYEuXx-v7hMNqYOY8JlLzhcVhPA9V4DP07xFyPIlnBaBJPjqdIwOwqUSvjJc_OZV_y7MmasxkgQFCA0eyYyDQE5T1-Wgx2UTxHZumate_v0fhWUiPoZLmbNPNUDfLTSMxOMp_1HmhfxVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازی با خون
🔹
سناریوی چند مرحله‌ای برای تجزیه ایران از دعوت به حمله مسلحانه تا دفاع از عاملان قتل در قاب رسانه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652435" target="_blank">📅 22:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAi485fnKMuW3gcVkJclpgiDUC6sLlpJ7OFZd4tvR1Rk_HXnlzphLe7IcbYmHTgMrjpUp_rJyUQpePdN_7M4chGZGrUp4yl9rZeHmKWZGiF64aGEsI1zcYjl2x1DpmgvLoR6cMxHaSkQnYegKp1ami-W-szW9OYiBVOY37VGbLufVm6-T7fHS2jCH_kwdJnarWclbJwycH64PKWLjgntkVR6TErXinsAOX2nG5AEqGLxo3DkxjJgwIgy1vFr0dg_KRCthlnAQ9t3JjONAPF5jM3-VesB2YdGR1ADE_InBdQsNgdSF2lBE2hMcZ55OA5zSaBBqyXJMnMexqwiwduh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: وظیفه خود به عنوان حافظ امنیت تنگه هرمز را انجام می‌دهیم
🔹
وزیر امور خارجه درباره دیدار امروزش با همتای هندی گفت که ایران همواره وظیفه تاریخی خود را به‌عنوان حافظ امنیت در تنگه هرمز انجام خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/652434" target="_blank">📅 22:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/652433" target="_blank">📅 21:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Blf3FuhUyXJEeMWSVEpxJMakunpv1cs92fzLShVW2OEmQ1H9Y-tyXIBDgs5lz-SPx-BcEel16XlFl52_illTuv94PUJxmyepcAf9vTgV-lQVgmXI2-UCqeWxaRHnrKnyNLVj10cMLOQbPPS0OBpe-LJw_41JVUjJOAIysUOPk-zZzM92Nxld7t8SplE3ikGWfBW0LwbNFBPTJdWJdqjdpumbWBbZ8JOQ7tqu25243Nsn5OAP-ejGQDpcFw-fft8FVQwlRFXH-J-eYo-1W2laVUEnliIfsKYSYLAK_hnFH39RyXos3Bpq5fAQhbQ3aXT1d-mi-pyfxIiTaQHAtt8WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات عربستان و امارات به ایران چه تغییری ایجاد می‌کند؟ | نتیجه خودشیرینی برای پنتاگون چیست؟
🔹
نزدیک به سه دهه است که مقام‌های پنتاگون در دولت‌های مختلف آمریکا تلاش کرده‌اند کشورهای ثروتمند عربی حاشیه خلیج فارس را متقاعد کنند که توان نظامی خود را گسترش دهند و در برابر تهدیدات همسایگان قدرتمندشان، نقش فعال‌تری ایفا کنند.
ترجمه گزارش المانیتور را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215165</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/akhbarefori/652432" target="_blank">📅 21:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwJHf6VSavGqp6YqD1fBQ3aWvit411dg9UfTXWS_bGrVkqcqOTiejYGqxCgiIh5MupM_m3DUMg4ZC9BCJv62hmUr3qpAr2IuuNF-qtF-mVqt2lnjxDtFP-SPsIstdFzsN3DjafS8Bc0GIxKeFJLpXXNh3FpzOVJJoaSGdRlpJLICHXCCf6wj8XXROzPXN72U2SotUELwgsQBUWF2IHX6Sn5eMMhRJ20qH3PCURMem-12OGMZCzgC_JrwgF3xsavdU1KwyAp0WoKBEj138Neo6g9WkP2iokjlXYzuh3Iee6QCVcBN7uELD7FjVKOiJeNy3QOAEzwwMOZ92NtRlTcg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعیین جایزه ۲۰۰ هزار دلاری توسط FBI برای کسب اطلاع از افسر سابق نیروی هوایی آمریکا که به ایران پیوسته و اطلاعات نظامی حیاتی را لو داده است
🔹
شبکه فاکس‌نیوز گزارش داده است:
🔹
«مونیکا ویت» متخصص سابق نیروی هوایی ظاهراً از سال ۲۰۱۳ فرار کرده و اطلاعات طبقه‌بندی شده دفاع ملی را در اختیار تهران قرار داده است.
🔹
او متهم است با استفاده از دسترسی‌های امنیتی خود، هویت همکاران سابق و جزئیات پروژه‌های حساس اطلاعاتی آمریکا را به مأموران ایرانی لو داده است.
🔹
مقامات امنیتی آمریکا معتقدند ویت پس از خروج از کشور، همکاری نزدیکی با نهادهای اطلاعاتی ایران آغاز کرده و در عملیات‌های سایبری علیه پرسنل نظامی آمریکا نقش داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/652431" target="_blank">📅 21:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نتانیاهو به گسترش اشغال غزه تا ۶۰ درصد اعتراف کرد
🔹
نخست وزیر رژیم صهیونیستی به نقض طرح آتش‌بس ترامپ برای نوار غزه و گسترش مساحت سرزمین اشغالی به ۶۰ درصد اعتراف کرد.
🔹
این درصد بزرگتر از آن چیزی است که در توافق آتش‌بس منعقد شده با میانجیگری ایالات متحده، که در اکتبر ۲۰۲۵ به اجرا درآمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/652430" target="_blank">📅 21:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای ترامپ: من تاب‌آوری ایران را دست کم نگرفتم
🔹
ما پل‌ها و نیروگاه‌های ایران را نجات دادیم و می‌توانیم همه آنها را فقط در عرض دو روز به طور کامل نابود کنیم.
🔹
من تاب‌آوری ایران را دست کم نگرفتم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/652429" target="_blank">📅 21:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mci7kc_YJlnOnxjCpSA7AmBDY_67ArRWyXzB47yORCXFygCf211MGcTNB7MnDe83lmA5G0otGciZL4uhvCjCBcbc7Kr_wEuhnrvz1snU3_IUkYfXDWx1TpZR10bEqXgkr7bx0CgeF9gJFFHwfuN68kmmJh27c2Jy3LqNZTA0XlyNBiY6wLwoMAUlBUtiTw3h7TdVUk-bQ7rtX3KYTkZYcJfl56JQjLCe7cFVc-g-VjnlC-NVPMIkOPC6_apgJLkEjcA3QvXXLl7nuaoHCwPOJaPpbWgUkyqHN5aM7uJVfppX7ALh53AggoibNIm_X3KFRXdUggVIE75zrMOvh11o_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانسون: عملیات خشم حماسی به پایان رسیده است
🔹
رئیس جمهوری‌خواه مجلس نمایندگان آمریکا: عملیات «خشم حماسی» آمریکا علیه ایران به پایان رسیده و ایالات متحده هم‌اکنون به دنبال بازگشایی تنگه هرمز است.
🔹
دولت آمریکا در حال حاضر به جای اقدام نظامی، در حال مذاکره با ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/652428" target="_blank">📅 21:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAfwM45XsH7SW9GKG_aT5qPT4cfB1cbFIMvOMsg-lNlrIoun9wDyDSCAGzJTStIuXRCs2n21ZK1aXmVCa2mrCmXfSGLSQL8bUzCGXube8uwwy_JQxEEV_o5_NWwDrkDymhcF-3Vk2Wqd6J4aav77eciVFHNRfJTYOsirScqOL8_q1AqjY3LjXLY3XuDVyGPJc9kj5CoYpsByfMdxy-ptrGZ7YFgHfy9Vhwf5zUiQkJ8PfBY72NnGiBQqokYSKyRsB7NoCiMlQlFzmsyJAFjZFJeKeInxThpjpA2F6FlTF7qVurRa4IjR69lLexyMYx3JHk1RmuKhid1rwWgm-oC7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: قیمت نفت به‌زودی ممکن است به شکل تکان‌دهنده‌ای افزایش یابد
🔹
بزرگ‌ترین شوک عرضه در تاریخ نفت به‌سرعت در حال بزرگ‌تر شدن است؛ حدود ۲ میلیارد بشکه یا ۵ درصد از عرضه سالانه نفت جهان به دلیل بسته شدن تنگه هرمز از دست رفته است.
🔹
به زودی ذخایر خصوصی در کشورهای ثروتمند شروع به اتمام می‌کنند و قیمت‌ها می‌توانند به شکل تکان‌دهنده‌ای افزایش یابند که ابتدا فرآورده‌های پالایش‌شده آسیب خواهند دید.
🔹
خطر دیگر این است که ترامپ کنترل خود را از دست بدهد؛ در صورت اجرای ممنوعیت صادرات توسط دولت ترامپ هم قیمت‌های جهانی به.سرعت افزایش خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652427" target="_blank">📅 21:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای نتانیاهو و کاتز: ارتش اسرائیل فرمانده گردان قسام عزالدین الحداد را در غزه ترور کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/652426" target="_blank">📅 20:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7NkECgrIT_XNJem_rBsqJFc9UkRf31_RitYnjBmCuSqbWeebsdb27hctKcqFxLMFDbCHIkMyTGV_KsBhBkcsXVOyt8lVKB2CKAU18AYl8GB8VCcnpCIQnH61zLCVU3prEH-e4DHs9EU0CwfkuJw4GKSYxv_REQsJFdV-3i-TAXl2SkYSS7azSSBGgUEd4p-CHfaTdtpRf_1G6MOAPkR0UVxRLYzoHZL2F3vpot8_jqr65LeBPrJRp1KJjLbU1f_RUc1AOyqG7sjpKeMTs8oDqhAYfkHX6ZCas2EEHv-psmBRtJIaKiN-v8Z6PVepBV5VfdrWc0XxV6m-UeNgf9dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش بهای نفت و سایه رکود بر اروپا در پی تشدید تنش‌ها با ایران
الجزيره:
🔹
سپاه پاسداران اعلام کرد از عصر چهارشنبه تنها ۳۰ کشتی از تنگه هرمز عبور کرده‌اند؛ در حالی‌که پیش از جنگ روزانه حدود ۱۴۰ کشتی از این مسیر عبور می‌کردند.
🔹
هم‌زمان با بی‌نتیجه ماندن نشست پکن، قیمت نفت بالا رفت و بورس‌های اروپا نیز در میان نگرانی از بحران انرژی و رکود سقوط کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/652425" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPRdGIGrxRyl5uFiinWLQaFmSEZcTr9XR9zbCUylYW5vDFXEzJo9rcYojnWA-SAyKS2P167WP0sceHlXsuJe8NoPRQaD6cOicJLZeW_WVxIg0awwkygkbuk96Qtf640Tq5tHj7JDjT62luxRm-p0iXGLHOHogCZZI_IlKDAU7FIgkmrFxWCJL80q4EUzXlmOprQK_dxOny2dxBmDlf2k7JpQKTcX5NaVaTIpKKCvJHq0WqqISkg6YVWgjIBJ4zmPcjxrhfwfEwoV5YyizrpiXZVna-rnNTbU4hCc1GEdyTO9xzvQsh2pZM5I8U66vjyMhF7hrs6GePrPyoe9qnKtzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا برای این زن در ایران ۲۰۰ هزار دلار پاداش تعیین کرد
شرح ماجرا را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215122</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/akhbarefori/652424" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e91b011a6.mp4?token=NFJ_AQ4kzJ5RyiwXqX_wjf1pdj1t-RfVL1dAko8hM5Ca9uBHELEOMpGhPz06mI1x7N0vlBFr0JObRIHZik37zRiE9HrId3kkyK3lb29S0qI-UnrzIxZvHQrcrGVtlhhnPkI9Hr9aJZW4YSBY-iuaidtWNQxMLOxU8k5UgfnMipAFG3rqSstr8ueqBd5GC0wC6smxavqYeqVI0hlltsZlk-HgnnarOiYRFuNcMQPCSRUu-0f3gyzeCMgTMg0CxnDQ7eJT8pOkXSn6kdKQGbSNulIasnK6kSqWwHLlqLO1rpIX2SkUjoxfENNRammk8kQ_CoclfK4G18LsqfdTkQAaPyfgZEwNPny69AWJ9NiwiIbO7f0abQ9Q03CYyG5VZxmhUSyl870W4WWhNcz0Sjd1_8oRGe7Is97-w8pMv8PDhrdHom55VPfJsGgnyV6JcVOB6J8rBHq1y64N6IuC33RRNTC7h-jLJqA69H0ULrBzHBukMKLMd15igFA5fAgGRjYfZLhKntvNaL2-X3X-OqEjovSdvIUHdn5sYCmxYgpvH6StcWWn_hgWYNAb6yCfV1XEMs0HlMPahA9tz5h6wgBZ1wKXb1ZhSMCVjfHYK4pQ9pB1El4z0gvoVg2ju0_8cgLnxGgqXr2YLZuJYDHvWSLOoFjUd0v_gG2RK1w_uvhJKdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e91b011a6.mp4?token=NFJ_AQ4kzJ5RyiwXqX_wjf1pdj1t-RfVL1dAko8hM5Ca9uBHELEOMpGhPz06mI1x7N0vlBFr0JObRIHZik37zRiE9HrId3kkyK3lb29S0qI-UnrzIxZvHQrcrGVtlhhnPkI9Hr9aJZW4YSBY-iuaidtWNQxMLOxU8k5UgfnMipAFG3rqSstr8ueqBd5GC0wC6smxavqYeqVI0hlltsZlk-HgnnarOiYRFuNcMQPCSRUu-0f3gyzeCMgTMg0CxnDQ7eJT8pOkXSn6kdKQGbSNulIasnK6kSqWwHLlqLO1rpIX2SkUjoxfENNRammk8kQ_CoclfK4G18LsqfdTkQAaPyfgZEwNPny69AWJ9NiwiIbO7f0abQ9Q03CYyG5VZxmhUSyl870W4WWhNcz0Sjd1_8oRGe7Is97-w8pMv8PDhrdHom55VPfJsGgnyV6JcVOB6J8rBHq1y64N6IuC33RRNTC7h-jLJqA69H0ULrBzHBukMKLMd15igFA5fAgGRjYfZLhKntvNaL2-X3X-OqEjovSdvIUHdn5sYCmxYgpvH6StcWWn_hgWYNAb6yCfV1XEMs0HlMPahA9tz5h6wgBZ1wKXb1ZhSMCVjfHYK4pQ9pB1El4z0gvoVg2ju0_8cgLnxGgqXr2YLZuJYDHvWSLOoFjUd0v_gG2RK1w_uvhJKdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری شبکۀ مرتبط با موساد در اردبیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/652423" target="_blank">📅 19:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بن‌بست جنگ ایران؛ ترامپ دست به دامان کنگره شد
فکت‌چک:
🔹
رئیس‌جمهور آمریکا پیشنهاد تعلیق موقت مالیات فدرال بر بنزین را داده است. این امر قیمت بنزین را حدود ۱۸.۴ سنت در هر گالن و قیمت گازوئیل را حدود ۲۴.۴ سنت در هر گالن کاهش می‌دهد.
🔹
اما این طرح نیاز به تأیید کنگره دارد و هنوز مشخص نیست که آیا حمایت دو حزبی کافی برای تبدیل آن به قانون وجود دارد یا خیر.
🔹
کارشناسان می‌گویند که حذف مالیات بنزین، حتی به طور موقت، می‌تواند به افزایش بیشتر قیمت‌ها نسبت به حالت عادی کمک کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/652422" target="_blank">📅 19:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scu2T8mav7ogX-tt1VLbXAojNQSiKppZ8dXoW6Ov2_drPSPx1gbY_cTef4aoDfe0v-Y3ykoBhvMjMSvCrAdTo_uXoJlRb-8bvQ6jLi6vEwQC9VySrqTfBRMH9LM6sVM2uuehQTgVnB0MvMyJevab8ySHf7MA9qw5i7dwpdACENwRtKl_3t4A2PDnAmUjfESA0e-fjSTI89goEyn7HlTTmXzF7Q6zAjajOqdCpE0GVzoU6cV6x89brGHEP0uy_4dyrr0VMUfPSV_NoOyKilPDs6FWvbBLqOrnPepryVOv2itPKNBprOzRHjUJfpwE555siw-sBbX4ssPXmPnsZr7tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ایلان ماسک در عکس یادگاری چهره‌اش را تغییر داد؟ | هراس از اسکن چهره + ویدئو
🔹
در جریان سفر رسمی دونالد ترامپ به چین تصاویری ازایلان ماسک در کنار تیم کوک منتشر شد که در آن ماسک هنگام عکس گرفتن، حالت‌های اغراق‌آمیز و طنزآمیز به چهره‌اش می‌داد.
بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3215173</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/652421" target="_blank">📅 19:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
یورونیوز: ایران به دنبال اعمال عوارض بر کابل‌های اینترنتی هرمز است
یورونیوز:
🔹
ایران به دنبال اعمال عوارض بر کابل‌های اینترنتی هرمز به عنوان اهرم جدیدی علیه غرب است
🔹
رسانه‌های پرنفوذ ایران از تهران خواسته‌اند تا بر کابل‌های زیردریایی از طریق تنگه هرمز عوارض وضع کند و ترافیک جهانی داده‌ها را رصد کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/652420" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a02fdd912.mp4?token=pmwBKyKUzYUwTLIKL_-4LDVGzafIPW6qSyaqPZGcmOODf39F3ObhOzanM0hvEtbJdZEwJJ1oSyQZj7PfqFI-2kSOLv1vabSgYR6KZAckOh-BMHiMDrK2XEyZmO2lNdN1QRkZ82LPT4aIGNFULMI4-XP00G11qzKNimHtCXVUlDHS0amqIsFyTNCvYFIW40-FL6CvKRVhfJaO2UTdSX2-m0ywbU-KMyJlqxLct-ZCMttx8_IM26zaS4cqYG0NYbu6zglsOaw5H42HkpY3Y-5IEGRRy3Ad_WInv1ximD9K-EMc675SkgNWzwaE30mJoBVDpDLGIa75XEBAHPdThN4NZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a02fdd912.mp4?token=pmwBKyKUzYUwTLIKL_-4LDVGzafIPW6qSyaqPZGcmOODf39F3ObhOzanM0hvEtbJdZEwJJ1oSyQZj7PfqFI-2kSOLv1vabSgYR6KZAckOh-BMHiMDrK2XEyZmO2lNdN1QRkZ82LPT4aIGNFULMI4-XP00G11qzKNimHtCXVUlDHS0amqIsFyTNCvYFIW40-FL6CvKRVhfJaO2UTdSX2-m0ywbU-KMyJlqxLct-ZCMttx8_IM26zaS4cqYG0NYbu6zglsOaw5H42HkpY3Y-5IEGRRy3Ad_WInv1ximD9K-EMc675SkgNWzwaE30mJoBVDpDLGIa75XEBAHPdThN4NZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش‌‌‌سوزی در پتخ‌تیکوا در شرق تل‌آویو اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/akhbarefori/652419" target="_blank">📅 19:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652418">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0c9844d7.mp4?token=JMqoHvxVazyoriqJBuX09yrFUzoIezzezUXGSNB6K6OD3V3df2AlZRM3vraz-NVdRRZxAY9cgGXdKoxAL3yAw8GS2SebI4UxL6zAtk8QPAU0TJ4gT_MMHx3ZmekiM1HuethTabfwfutrmWDrzFSK3pcgkmUeJmxc72nrV_Dk9uHhmtGDGQj-sA18DJ9EXUZj71YR7WZ5DX1zWWK-ABcokIZ_8KgXzXgBRCuToJ00530QyVW7T4xjalC5aIJF3GECwIiT6yxO34XkifHbkyfvfGoIpwGmtX8ObOOyfXj1BaaAWb_h8lbKZ8iqJVVQBetoQXouqH087Bi5mrN4PBCw4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0c9844d7.mp4?token=JMqoHvxVazyoriqJBuX09yrFUzoIezzezUXGSNB6K6OD3V3df2AlZRM3vraz-NVdRRZxAY9cgGXdKoxAL3yAw8GS2SebI4UxL6zAtk8QPAU0TJ4gT_MMHx3ZmekiM1HuethTabfwfutrmWDrzFSK3pcgkmUeJmxc72nrV_Dk9uHhmtGDGQj-sA18DJ9EXUZj71YR7WZ5DX1zWWK-ABcokIZ_8KgXzXgBRCuToJ00530QyVW7T4xjalC5aIJF3GECwIiT6yxO34XkifHbkyfvfGoIpwGmtX8ObOOyfXj1BaaAWb_h8lbKZ8iqJVVQBetoQXouqH087Bi5mrN4PBCw4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانی که ۳۰ سال برای ایران جنگید!
@TV_Fori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/652418" target="_blank">📅 19:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652417">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlOTUWI5O9TAivPHbuwRwZA3c2dxKfkmLWqFRCUWupPhy7ntSulG2G2c8rHHoT1snUhj3nml6UyiRqTx00KWmgXNbZWQH0k49ylNz0W9RbDYgPwxCPpuByfeZWGq4fKxdSAm2Az6u1L2k421w50YfyNFjwBIiURYhR4cT3tXptaC0FAPhBfGsd5GQXIgjRabffNdiPc1T2PstFMCMQEKz5QhJ2xIORAbZFvTLglcyMovJaKzna3V5cmC9YsJNJYLKQLjAMmr8mYXk0MhiNQ7d3deD6cOk-xS7PSgrs_ai1cxEuO4xsyEuE_DbBfrbxqQrOyNY9DtiegBNkz9hSjp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میز کار هم می‌تواند سبز باشد
🔹
هر انتخاب آگاهانه در محل کار، قدمی برای آینده‌ای پاک‌تر است  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/652417" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652414">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJCjQ32AZ5XlW1Ho2CLwbX1cSLWs1MnrRndWtq1ILYC7eHOE59s-iyC3xVvvsM-0ss5xlfT3odkCaUws8-a080YEf5VFqr8oPtuyZVmWWCtPj64_t92lAf0hFqhXeEQ8ZDdTnXZsDxaGRvxt8W7tE_JczSl7D9tHIVxNF7-KibGM9uz7AqK5P4WqI409eicpH_0M6E6dwi4tugoACM9usaAQdmrLuAt3wSMi9zCvd10u_DRV_8lHea0vnO6GCc1jU8HcirKaOT_xDKC0rcSeSDI5ExW11EIrHl4NT-WMpZegZxXzLrdTx-aVOVPNqDk_J743d_dUSSgI6mYcJX-rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: با شکست دیپلماسی، ترامپ با مجموعه‌ای از «گزینه‌های بد» در قبال ایران روبه‌روست
🔹
ترامپ در میان توقف مذاکرات صلح ایران، با افزایش فشارهای داخلی و بالا رفتن مخاطرات ژئوپلیتیک مواجه است.
🔹
گزینه‌های تداوم درگیری نظامی، پذیرش ایران هسته‌ای یا عقب‌نشینی از مواضع قبلی، همگی گزینه‌هایی هستند که نفوذ آمریکا در منطقه را به چالش می‌کشند.
🔹
نارضایتی‌های فزاینده در داخل آمریکا نسبت به هزینه‌های جنگ، مانور سیاسی او را بیش از پیش محدود کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/652414" target="_blank">📅 18:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652413">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR1KuiH7TJp-7d4xrIUOGkrCxuBwAEQGX-7Q1A0h66MOoTi8M6kf0skhv9fGv3NZGRt4DoNHAjPIjIqzYKMQD0gh8hILOgm6qnXiTebbB9Jg2bSR6k9NT-c4_emS5-aJtZoHqV70Sg4VBrwQeRDZ-PkSTjAI_z0ehw6KfaqahuLEs_a-QdqLUH_4XilaAUjxdFNEPP-4-zjOA0RjaytRYBIyQcaxeY_i1SFwcEcBlSHRJFmI1Lu1LzIUFuuUVg6M4M46VrAM_emSr6t5x-uF6VazsjG2v_JM_cQkBaovmXtrXLTM20DYiCxQYNB0J6DQ6kYkk8eVET9l9XwGXEEanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تاکنون از چین در مورد ایران چه چیزی به دست آورده است؟
🔹
این که دونالد ترامپ، رئیس‌جمهور آمریکا، بتواند همتای چینی خود را متقاعد کند تا برای پایان دادن به جنگ آمریکا با ایران کمک کند، انتظار بالایی بود؛ جنگی که بازارهای جهانی انرژی را دچار آشفتگی کرده است.
ترجمه گزارش سی‌ان‌ان را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215152</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/652413" target="_blank">📅 18:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652412">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e9f34e9d.mp4?token=upSS34nkM1lmSQQgLwcmyZPPwzuLXGWeiv5F_smEd1D3dWu3XeNluVSVMwtBtC6Jr30Q9GdmrADg8KqKFlQzquKbZm2hhpzK3ZIgCeiZKk581lIm54Hkv400ESDN8C2DoPvKMiVdjEabCMs5icayHp2knG3PFDEow--WPXvrVzy5q75Xgnnju7rh6myEmRcX2KHGdDSaHEpCQgQIv_EbvUA4FwdCIfkURTugoWHoxpWMbS82tr3swcFYzVMsZ_axGLtaMzwr9fg6danQeqWPLl9LY5sdMUva50xDS_DnjUKpr7et5Y07lFXxozRwnm7TzoQqgxclybZAvLe0ru1YuS84UlwsvhaURlN1DovvpNL9DcmnNbhWQkg9y-49tQ0XU10lX69y-AAjPkYze4YHmPeIwb3Xops4vCdIO6q9t1yPESBb8wpyT4dHkQsWcTVO245eusXnIAqQBlbv3c5glaVNeRrU93mmUg7aOUIv2GDAgRK2XGp3xwogWPTm7prCiB9ntmb89Or6wpvPBBKG4BKc4q6Hcqxd3IZrQL5GbYw0tA49SJn1NRu4Xrc6ldOqwA-Rk3NA5UlwF6buj3n1H3_LhWqrvC8jVphNVG6YXf0nPcRf9fJrSM7VtNkT045NNGBlxtRg8JNK--kXSBVHejfx-3sAcMXI1p-sN-fSLos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e9f34e9d.mp4?token=upSS34nkM1lmSQQgLwcmyZPPwzuLXGWeiv5F_smEd1D3dWu3XeNluVSVMwtBtC6Jr30Q9GdmrADg8KqKFlQzquKbZm2hhpzK3ZIgCeiZKk581lIm54Hkv400ESDN8C2DoPvKMiVdjEabCMs5icayHp2knG3PFDEow--WPXvrVzy5q75Xgnnju7rh6myEmRcX2KHGdDSaHEpCQgQIv_EbvUA4FwdCIfkURTugoWHoxpWMbS82tr3swcFYzVMsZ_axGLtaMzwr9fg6danQeqWPLl9LY5sdMUva50xDS_DnjUKpr7et5Y07lFXxozRwnm7TzoQqgxclybZAvLe0ru1YuS84UlwsvhaURlN1DovvpNL9DcmnNbhWQkg9y-49tQ0XU10lX69y-AAjPkYze4YHmPeIwb3Xops4vCdIO6q9t1yPESBb8wpyT4dHkQsWcTVO245eusXnIAqQBlbv3c5glaVNeRrU93mmUg7aOUIv2GDAgRK2XGp3xwogWPTm7prCiB9ntmb89Or6wpvPBBKG4BKc4q6Hcqxd3IZrQL5GbYw0tA49SJn1NRu4Xrc6ldOqwA-Rk3NA5UlwF6buj3n1H3_LhWqrvC8jVphNVG6YXf0nPcRf9fJrSM7VtNkT045NNGBlxtRg8JNK--kXSBVHejfx-3sAcMXI1p-sN-fSLos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا: درباره بمباران ۲۲ مدرسه در ایران تحقیق نکرده‌ایم
🔹
- سناتور آمریکایی: اگر به ایرانی‌ها هشدار داده شده بود چطور ۲۲ مدرسه را بمباران کردیم؟
🔹
- فرمانده سنتکام: هیچ نشانه‌‌ای در دست نداریم که این چیزی که شما گفتید را تأیید کند.
🔹
-سناتور آمریکایی: چند مدرسه را بمباران کرده‌ایم؟
🔹
-فرمانده سنتکام: درباره یک مورد مربوط به تلفات غیرنظامیان تحقیقات در حال انجام است.
🔹
-سناتور آمریکایی: پس این اطلاعات علنی مبنی بر اینکه ۲۲ مدرسه و چندین بیمارستان بمباران شده‌اند را چطور توضیح می‌دهید؟
🔹
- فرمانده سنتکام: هیچ راهی وجود ندارد که بتوانیم این را تأیید کنیم.
🔹
- سناتور آمریکایی: درباره این ادعاها تحقیقات انجام داده‌ایم؟
🔹
- فرمانده سنتکام: نه انجام نداده‌ایم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/652412" target="_blank">📅 18:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3f626cc5.mp4?token=jNK967fFETnXC0Iq8csREQM22r9FOTiH8nli0tyBfd8gf9kbQTGtVrU0AdS_KQWCJ6-3Ta9hvVHnyx3b1QvNmqd0gJ-TYeN6sRyIET4gwPWzCZ4SIVW_h3GsEJvG-3pNUrMQg8wKrwUqPDVJ-0ij3eFm0u0SXkwXHYbxgUw7NDwLag8r632TRVus8LI191Cgsh-corYo_kc5RQBMNJExDLWVUHFXydanUrE7RBjajC1K_M1VGEBq1bfU8yBt5JADnY45yCtSlp51_83bV_SPo3rk0F_Sd0qaJj3mHXcVwMnlbjTS_p_mATNPIheSjsWRVxFJcu0kdQ3-YOuY27sRfr7qhGcqmGn53vYyE6-21gCJvGeoMhBACQMllsBAYGFaQT1PJlSNP9vxWEufziSUiPvL0rlN196edPOYrMuauhdVpDLewQPaUDfp6L7bLs85xHkHyJmgPiFKFLoeavKlZf3LJQSTWZqZr1SOkMoarmBMSGo5mwfze0fZbidcrqhV-vTha4ovXRkBXqqGdvOJV_hTcfKnPuEP4tkIIDthPQ3kIbKcD6v0umav-193uG32y04IwnevfNUfQDFLFCJ7ZblKclCfGwD0IYht3cLugUGZXw6LFRmWj13GbXLcmnury7oSkh_JLaA31CMhpAHmpiQOfGMr-UaOQJpuFTrPI1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3f626cc5.mp4?token=jNK967fFETnXC0Iq8csREQM22r9FOTiH8nli0tyBfd8gf9kbQTGtVrU0AdS_KQWCJ6-3Ta9hvVHnyx3b1QvNmqd0gJ-TYeN6sRyIET4gwPWzCZ4SIVW_h3GsEJvG-3pNUrMQg8wKrwUqPDVJ-0ij3eFm0u0SXkwXHYbxgUw7NDwLag8r632TRVus8LI191Cgsh-corYo_kc5RQBMNJExDLWVUHFXydanUrE7RBjajC1K_M1VGEBq1bfU8yBt5JADnY45yCtSlp51_83bV_SPo3rk0F_Sd0qaJj3mHXcVwMnlbjTS_p_mATNPIheSjsWRVxFJcu0kdQ3-YOuY27sRfr7qhGcqmGn53vYyE6-21gCJvGeoMhBACQMllsBAYGFaQT1PJlSNP9vxWEufziSUiPvL0rlN196edPOYrMuauhdVpDLewQPaUDfp6L7bLs85xHkHyJmgPiFKFLoeavKlZf3LJQSTWZqZr1SOkMoarmBMSGo5mwfze0fZbidcrqhV-vTha4ovXRkBXqqGdvOJV_hTcfKnPuEP4tkIIDthPQ3kIbKcD6v0umav-193uG32y04IwnevfNUfQDFLFCJ7ZblKclCfGwD0IYht3cLugUGZXw6LFRmWj13GbXLcmnury7oSkh_JLaA31CMhpAHmpiQOfGMr-UaOQJpuFTrPI1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به منتقدان جنگ ایران: خجالت بکشید؛ شما خائنید
🔹
دونالد ترامپ خطاب به «دیوید سنگر»، خبرنگار روزنامه نیویورک‌تایمز گفت: «من [در ایران] به یک پیروزی کامل دست پیدا کردم. ولی فیک‌نیوز، یعنی آدم‌هایی مثل تو مطالب نادرست می‌نویسید.»
🔹
رئیس‌جمهور آمریکا گفت: «تو یک آدم جعلی هستی. ما به یک پیروزی تمام‌عیار نظامی دست پیدا کردیم. من فکر می‌کنم چیزهایی که تو می‌نویسی نوعی خیانت است.»
🔹
رئیس‌جمهور آمریکا اضافه کرد: «باید از خودتان خجالت بکشید. فکر می‌کنم واقعاً خیانت است.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/652411" target="_blank">📅 17:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
امام جمعه زاهدان با انتقاد شدید از عملکرد مافیای اقتصادی در شرایط جنگی، خواستار برخورد سریع و قاطع دستگاه قضا با زالوصفتانی شد که خون مردم را می‌مکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/652410" target="_blank">📅 16:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652409">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d04831a3b.mp4?token=s2cCXrIJWH51aKuyhUripp9_5SfWNKtKIUBw9C__fpmXgAAKmYkd95qA9HU4sf3VSc0BRGTqtrLOdKmhXjIwxPPLfO4wQLmY5CJYGZhcRyf-BfV53881fMO9h23vZKgypB4jIxV9yKDRFcNnS2v2HOwpt4xgsiMwT_u_nixTs2kZZLtae0GMwQOT-hMg7sncOgXA1ANjcHiH6aCWOIvdBK5DCu4nJrRTdNiecwRSFf20qY-f2Doex7HfBKfUwVuFwtHsjd0FRQMLn5rrG9wElQfyue3ilLF04yp77vfyMWX8NRSCwe_rqJE-rdSAeOI7lYxtimHGgoGG8CxMp5iRzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d04831a3b.mp4?token=s2cCXrIJWH51aKuyhUripp9_5SfWNKtKIUBw9C__fpmXgAAKmYkd95qA9HU4sf3VSc0BRGTqtrLOdKmhXjIwxPPLfO4wQLmY5CJYGZhcRyf-BfV53881fMO9h23vZKgypB4jIxV9yKDRFcNnS2v2HOwpt4xgsiMwT_u_nixTs2kZZLtae0GMwQOT-hMg7sncOgXA1ANjcHiH6aCWOIvdBK5DCu4nJrRTdNiecwRSFf20qY-f2Doex7HfBKfUwVuFwtHsjd0FRQMLn5rrG9wElQfyue3ilLF04yp77vfyMWX8NRSCwe_rqJE-rdSAeOI7lYxtimHGgoGG8CxMp5iRzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه محمد منان رئیسی، نماینده مجلس به عباس عبدی: یک ادم وقیح است که خودش از همه رانتی‌تر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652409" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652408">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owk-5cmBVPi3Y9YtDHVsUzwjH75s-baXemdgoB6Y-fi9idyRSZqsjWQFyvQE8bgtcyKdnFLuHm-UhinQ1gdm4VKFJFKj0BWSShk9rbw4XmHv4dQV5a89DmI6GynY3FIIXuQgYqOWzMivCk-4fJH5jUOkr6mtIRaooF-FVoK7EM1vljHIrYyPq5TAIYKBGdO5JZVmuAGn9NSuNKZ1eruLeCaiN-W9xGR66iR0Hi1K03qCR6pQrwdKLg-XZctadXG2e-ns4458upKcMHTFKncYxBpZs4W94o3BaqvBv_PZVyAezB1JQAGyeFj4oCcVRNEP5oISrIZ-_DYjjMEt6Du-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرید هوشمند، زمین سالم‌تر
🔹
هر بار که پلاستیک رو رد می‌کنی، یک قدم به زمین پاک‌تر نزدیک‌تر میشی  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652408" target="_blank">📅 16:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igdl8VHeBQMjN1kfMXTku3izTf6eUDIVUsRF_paSumWYw309KEczQ6i2mekloPt1gF4VmwqryrsBSOw0McG53juSg3rGEvQVq13LH7zo-ZLwFMHDPk0h9L5J58Lpc1WyAs8mFZCOlLF6b11cNDeuJnXOilYcW53HLR5LKATvvl-KTDo3lULCVE84JzKP_g_jRnFyqoSKRYJ39KMqlEykFviNAUTAglfqYucIokIPc37hl2ArWyD9gdS7NPBHJ_QJ9vma0m_DaOSlPSS1GV8QwpZXOlwN11zZCRnMill2Y8iNo0fw3SYiSMyQf5C3YbT-1A7Q5-BDn27GThcI6_yQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی سران آلمان و آمریکا درباره ایران
🔹
«فردریش مرتس» صدراعظم آلمان امروز به‌صورت تلفنی با «دونالد ترامپ» رئیس جمهور آمریکا گفتگو کرد.
🔹
مرتس درباره این تماس تلفنی گفت: «من گفتگوی خوبی با ترامپ داشتم و ما توافق کردیم که ایران باید همین حالا پای میز مذاکره بیاید».
🔹
«ایران باید تنگه هرمز را باز کند و باید از دستیابی آن به سلاح‌های هسته‌ای جلوگیری شود».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/652407" target="_blank">📅 15:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zixaooe92l74C8HK8qE-MPV2CZAPVqOHVmmlWe7TjrPhJA_oaZwUE2xG1IQIbdqhRE8661OQGXztBlUw-zynoKlXGLwDbAVyQYfsnt7Bd4t22lVk6uWCwRLQBP8Ua-Slrg3xfp3uIQwyY6FNFHCqDg8Ebspg2tD95RrZn-1PzCGQQWZfCfluCHYyQcHcTSoTVFfwjjvR61YHP46WMTyLp41xedShbQy0BWnY9t9bQgf4Nde7Qo4Jxfq-A_hEWLjBrl6JncN89gtjOQkTAwCwrhzim9R4aTvQTkPBMP8hnPSPXnWntf4kOPSDpaSeDLCurJe8I9crVrzCamL4ecYi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رزمایش غافلگیرکننده اسرائیل در امتداد مرزهای مصر
🔹
روزنامه عبری معاریو اعلام کرد که ارتش این رژیم سحرگاه امروز با مشارکت چندین لشکر، مانور غافلگیرکننده بزرگی با نام «گوگرد و آتش» را آغاز کرد که هدف آن آزمودن آمادگی نیروها برای سناریوهای عملیاتی اضطراری در جبهه شرقی به ویژه در حوزه استحفاظی لشکرهای ۸۰ و ۹۶ است.
🔹
معاریو افزود که هدف استراتژیک این رزمایش ارزیابی سطح آمادگی و رزمی ارتش برای مقابله با سناریوهای اضطراری متنوع از طریق آموزش فرماندهان و نظامیان در تمام سطوح از ستاد کل گرفته تا واحدهای میدانی با تمرکز ویژه بر منطقه مرزی شرقی که لشکرهای ۸۰ و ۹۶ در آن فعالیت دارند، است.
🔹
این روزنامه عبری تصریح کرد که این مانور شامل اجرایی‌سازی سناریوهای متعددی است که رویدادهای اضطراری را شبیه‌سازی می‌کنند تا نحوه عملکرد نیروها را آزمایش کنند به طوری که این رزمایش برای سنجش توانایی ارتش برای حرکت در «زمان صفر» از حالت عادی به یک جنگ با شدت بالا مشابه آنچه در ۷ اکتبر ۲۰۲۳ میلادی اتفاق افتاد، طراحی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/652406" target="_blank">📅 15:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652404">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b764854cc4.mp4?token=qheIUBRanFAAnT7D6QzKxK7rzKqnDYGJ6OVPxK-1us0X-vTnzuF3MYnOQX4D6-Mp6CtECG_qS27DyhZB_JECf4gST2R3PEYP50bVd-8u-S2uLy2Jst9lAmJJI7WD48XVC-Rtxa4mweCJcPf2AQWFl_Bx6JVpQmFg3a6X3IJWkWg9abG-UYunTqqBxTo7YFs1qGj13LTrrbl0kKGbBu1IozVgurXyo8MZhzvH3ARodA8lDOiw54elP8rM9J_4Q2qmX9a1fA9O4fQGlxGA2rLjgV7TWtZZKa0T_T9fufRNIssnC-IiAmJTvO5gW3V77KRdCtakGs9U8dSLiQ6WiUjVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b764854cc4.mp4?token=qheIUBRanFAAnT7D6QzKxK7rzKqnDYGJ6OVPxK-1us0X-vTnzuF3MYnOQX4D6-Mp6CtECG_qS27DyhZB_JECf4gST2R3PEYP50bVd-8u-S2uLy2Jst9lAmJJI7WD48XVC-Rtxa4mweCJcPf2AQWFl_Bx6JVpQmFg3a6X3IJWkWg9abG-UYunTqqBxTo7YFs1qGj13LTrrbl0kKGbBu1IozVgurXyo8MZhzvH3ARodA8lDOiw54elP8rM9J_4Q2qmX9a1fA9O4fQGlxGA2rLjgV7TWtZZKa0T_T9fufRNIssnC-IiAmJTvO5gW3V77KRdCtakGs9U8dSLiQ6WiUjVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران:
🔹
ممکن است مجبور شویم یک کار پاکسازی کوچک انجام دهیم، چون یک آتش بس یک ماهه داشتیم.
🔹
ما واقعاً آن آتش بس را به درخواست کشورهای دیگر برقرار کردیم.
🔹
من خودم خیلی موافق آن نبودم، اما این کار را به عنوان لطفی نسبت به پاکستان انجام دادیم؛ مردم فوق العاده، فیلد مارشال و نخست وزیر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/652404" target="_blank">📅 15:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652403">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btb9GGT0SjNcInudfuX9jv52Edwb8InavdvWu_khp5gzNWJyC1Akwi_mRgFik3ZOYgCYvZHEmVRmptKuXKL-6U5F8uKcpewPbDLrIuGB5lQtODYIol_32SfriaHeGv9OrBnC7sr7D-ZPopE5xMLfcuEdzYLbtxgZla4YPifblK1HhE5p_4C59eNcerHIwpfNTsdf2UG5feGbaQbYZ0qcSuDXjlr87vTR4_jBFcsPBpYIYaHDG0aJyMnksr28KkzsAcEjr_tmP5xcH2qL18jfaNJmA1U6V5CDr6SbXILWeeuEuslVqdFUd8XlSsdexqtKjS-hT4uVX5eWr5PBJGJAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معجزهٔ ذخیره‌سازی ایران مقابل دسیسهٔ آمریکا
🔹
وزیر خزانه‌داری آمریکا می‌گوید بارگیری نفت در خارگ متوقف شد اما شرکت همراه آمریکا در فشار به ایران می‌گوید، تهران تاکتیک عوض کرده است.
🔹
شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران، تنکرترکرز می‌گوید، اگر ظرفیت ذخیره‌سازی جزیرهٔ خارگ پر شده بود، نزدیک‌ترین نفتکش‌های در دسترس را می‌آوردند و آن‌ها را پر می‌کردند.
🔹
یک ماه پیش ترامپ گفته بود خط لوله‌های ایران منفجر می‌شوند، تنکر ترکرز اعلام کرد، بدون درنظر گرفتن مخازن خشکی، ایران یک ماه و نیم زمان دارد حالا ۲۴ ساعت از ابراز خرسندی وزیر خزانه‌داری آمریکا برای توقف بارگیری نفت در جزیرهٔ خارگ نگذشته است.
🔹
این‌بار هم این شرکت که پیوسته در حال پایش نفتکش‌های خالی ایران است، توضیح می‌دهد، هنوز هم نفتکش‌های زیادی هستند که ایران در آنها بارگیری کند اما تولید را کاهش داده تا با افت بارگیری نفتکش‌ها هماهنگ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/652403" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652402">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msz7cGRz5TAprdZs3jQ0IMEqLGGf0l-FcEKvWzdQ7aVwHLxN8dfQYFOTGpUKLACA_bB3i897ZDuFwF0RcivztVZ8k55rAdXLFPrXPkg11j7Y02HAM-u2kkkFMMba6rVAtVq1WQBa5PS2TvzGSDw7ofVnP6afF0Lu_dAMU_5uU5eie0K_9qpjwvl45xY42UFol9w_t2VAWvNsiN5N-QxTIjMAIi5W_lPF7Pfwj6JwC18ifCcR2Nh4Nm-CDZ-LVC0uJ0kXdZmfXT7Lp8iIXaEVHqQBFmyZGFqHdRqUSHlOwfZU7NhOGydOPG6QHKY6pehKYV9twmd93ar1lT6tc5Zz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها باز هم مصوبه دولت را پشت گوش انداختند
🔹
کسب اطلاع نشان می‌دهد از بستهٔ ۷۰۰ همتی مصوب وزارت اقتصاد برای تامین سرمایه در گردش صنایع بعد از حذف ارز ۲۸ هزار و ۵۰۰ تومانی تنها ۱۰ درصد تسهیلات پرداخت شده و ۹۰ درصد پرداخت نشده که به توقف تولید، کمبود کالا و گرانی اخیر ختم شده است.
🔹
اواسط دی‌ماه سال گذشته بود که دولت اعلام کرد برای حمایت از تولید و جلوگیری از شوک به تولیدکنندگان درنتیجه تغییر سیاست ارزی، ۷۰۰ همت تسهیلات سرمایه در گردش مصوب کرده و به ۴ گروه از تولیدکنندگان پرداخت می‌شود.
🔹
ابلاغ این بسته به شبکهٔ بانکی اواسط بهمن ماه انجام شده و قرار بود همان زمان به تولیدکنندگان پرداخت شود اما بعد از گذشت ۳ ماه تنها یک دهم تولیدکنندگان موفق به دریافت این تسهیلات شده‌اند.
🔹
مدت اعتبار این مصوبه ۶ ماهه است و بعد از اتمام آن بانک‌ها دیگر الزامی به پرداخت آن ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/652402" target="_blank">📅 15:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652400">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiwB4kuqbji51TfeqmDx6DuhstqAQKEBTal_D25LCfSuTbXOSgBjCm7CKDRoNCmvJWfyYTnm6XqgkB2UFjBL78603VGxZ1AZxEg5mpSNUf7k4RYdaqJz4x5JGoTNEHIgZZQ79zp5O0HoU3I8qQd12_e_09B_9VpR8FMU4N6ITuE-IHDMRurgMVJwy1weSx7UXTd2aMgK8sbJUfixO2aZsxccUOMvEugvd3u5idms00KrziStk50_ijJEJ-O4cL9O_Y7QYhfzBZT9ZSJMYvcddBl1xFc8JXEr3p-yn1Vg1-08V1ULAZD-dH7I-FL6XJgfK8lRcFSs2mFtdNE6iiUmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJq6CDIvIeytTU4JxuCoN4oUZPquBY9xX5puVNVDRgTepNsPEhcYQh2-HkWvYUgHSUkExXEeV2exeughVVSV7I-N6jBhKTtKCrFCyB9rwvveh_Y-jPDy9dOB64y_RsOxO48-OnmD43oIHfxMTv9i4mheLYNAMour43FZKD2wVCzu_IhpSXCamcJPQefZQx5NxeOB-JfFfLE-K6syXupcNnANIw9F5Femo_3KIGY4I-hM7aSNW6Ypxqa2kqlfWQsRLStdvclwhHvvsoh3I4Ph5kVGvqoUpLAPYv5zrBJimdzu8-WD0hxp3QrChCDWOTkZdW4o_GKIU0pI1LP5nmS96Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اعلام سقف ارزی جدید برای واردات برنج و نهاده‌های روغنی
🔹
وزارت جهاد کشاورزی: قیمت‌های جدید اعلامی در سامانه مربوطه ثبت شده است.
🔹
مهلت اصلاح قیمت ثبت‌سفارش این کالاها نیز از یک ماه به دو ماه افزایش یافت.
🔹
ملاک بررسی ارزش ثبت‌سفارش واردات برای مباشرین و شرکت‌های دولتی، تاریخ صدور کد مجوز موردی خواهد بود.
🔹
هدف از این تصمیم، تسهیل تأمین کالاهای اساسی و هماهنگی با نوسانات قیمت جهانی عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/652400" target="_blank">📅 15:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652399">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
امام جمعه بجنورد: هر قدم عقب‌نشینی در برابر خواسته‌های دشمن مستکبر، قدم‌های بعدی را در پی دارد و باید تنگه احد زمان خود را حفظ کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/652399" target="_blank">📅 14:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652398">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ترامپ: تحقیق درباره حمله به مدرسه {میناب) ایران ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/652398" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652397">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ترامپ: به‌زودی درباره لغو تحریم‌ها علیه شرکت‌های چینی خریدار نفت ایران تصمیم‌گیری می‌کنم
🔹
ترامپ گفت ظرف چند روز آینده در مورد لغو تحریم‌ها علیه شرکت‌های نفتی چینی که نفت ایران را خریداری می‌کنند، تصمیم خواهم گرفت.
🔹
من از رئیس جمهور چین نخواستم که به ایران برای باز کردن تنگه هرمز فشار بیاورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/652397" target="_blank">📅 14:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652396">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5ce4b8cb.mp4?token=ie8cdS4GzbmbM53WrjzSscU7txse2eeVkpdlISfA3SekijW03G79gGczvrtggVyPjliWgc2oWimMDyvrXAfRa-d923GflhV2K9NNL-yr27esoiiFZJyET7OgoxccJF5vKgnx6skvzKK4-XmikOsZW46c3raECjA1JU1fMivafqOumiff-AxmBKSPeA3m_4F6t41TWNInu3knxptfDJmmMzwycDEPXcpBBT6Gen5rllmAwtFdee5iB4J2riu_vUve-tZpVg5Lu3aa2OcuKXzVYHggi5z8TOJib8q4MrDQiQ9Wn_iVEUYDiLZeN-fTeOzkCDFFdcxDWa360wzMZ-_DXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5ce4b8cb.mp4?token=ie8cdS4GzbmbM53WrjzSscU7txse2eeVkpdlISfA3SekijW03G79gGczvrtggVyPjliWgc2oWimMDyvrXAfRa-d923GflhV2K9NNL-yr27esoiiFZJyET7OgoxccJF5vKgnx6skvzKK4-XmikOsZW46c3raECjA1JU1fMivafqOumiff-AxmBKSPeA3m_4F6t41TWNInu3knxptfDJmmMzwycDEPXcpBBT6Gen5rllmAwtFdee5iB4J2riu_vUve-tZpVg5Lu3aa2OcuKXzVYHggi5z8TOJib8q4MrDQiQ9Wn_iVEUYDiLZeN-fTeOzkCDFFdcxDWa360wzMZ-_DXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: همزمان با دیپلماسی، امکان جنگ هم وجود دارد. امیدوارم به دیپلماسی، فرصت داده شود هر چند برای جنگ تمام عیار هم آمادگی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/652396" target="_blank">📅 14:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652395">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aynws7Bbz7Be73M0qATsB0rMnw0j8MtoWxxIk0X5hAIj1XcQRee4tYBELPjF-bqMxnfr_T-ENgzh6ul8VOq6_97v168zIwIXx79Fsm0V4uoJNuu_0_XS6VeKHRYYT4qcl2Fty3WRzO36MrpWZMajP-DtopNbw3qpfGk9_s-Qi_rmAecNuF1TlvkQG_h-cJXSW6UJCpDioDa8R8wCSDVADqmOGhhHxTkDBbhK47ewqr-dLc330RvKTBbBSfr9apPPBcBCm2k450_1qwsUUIZSo7pi_6hPMpNmXh9HGdL7VBAW5E7zQr2Zq58SQ8qzY1rRLyGnqyFUet9JHn-MAlnutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: من هیچ مخالفتی با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال ندارم، اما این باید یک تعهد واقعی باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/652395" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652394">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad8617c6d.mp4?token=T-XZ-191VFupIWcARIIRO1lmW9Mc9UrPbqSwmjE4rbcLIxSJwat7KpLOiyEbQLUoKplNj4qNNNbZdVN2gUUjTB4ZWV05a5_Mbiido993XyD3AeSqtzu50SePl2-Otyb4173oWKaCtP3ymgnf9puE0mqvBIlgMw-Oo6Ll_yT6HFweQmN9MgCt05DWXH88yJdbgoZJKVJetSUNu8Gc25fLp8L62RkoVoZ07BNxnqf6vLwt3U8r7BVFgP3k2aHm5KvsQ8y65Iug-qbBLoWhzyHO7DzYduBUQLm7SiIiLMUsEdTqcJe_74Q1blgGIBkQo_XRIFONxMX3rsreXZGi23CNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad8617c6d.mp4?token=T-XZ-191VFupIWcARIIRO1lmW9Mc9UrPbqSwmjE4rbcLIxSJwat7KpLOiyEbQLUoKplNj4qNNNbZdVN2gUUjTB4ZWV05a5_Mbiido993XyD3AeSqtzu50SePl2-Otyb4173oWKaCtP3ymgnf9puE0mqvBIlgMw-Oo6Ll_yT6HFweQmN9MgCt05DWXH88yJdbgoZJKVJetSUNu8Gc25fLp8L62RkoVoZ07BNxnqf6vLwt3U8r7BVFgP3k2aHm5KvsQ8y65Iug-qbBLoWhzyHO7DzYduBUQLm7SiIiLMUsEdTqcJe_74Q1blgGIBkQo_XRIFONxMX3rsreXZGi23CNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: احتمال بازگشت به یک جنگ تمام‌عیار وجود دارد ولی ما هم برای جنگ و هم مذاکره آماده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/652394" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d206e144.mp4?token=mUL1PhMsaxUqRTyr3GAaGAEoZENVYpqcssDDPcB4Dq4SfzV1DDhQqzZsnwo6EBPHak3SrdOwZVQV15i7aK1nzmnU12FoH6QKzfpotRdNJA0ePBFtNhbzsyq09ifiqVtASQxMe0comteptmxQAAKM9rzWNy6rdPeDXrXT48nfgke6E1AIBBqBr8oV2HoHVQFIVpVtxi1DEsfS4SD6_LN_lvXuQ2Lc_xOuZALj0a_2bB9couaScy38AuRDlK1DCfjXW6amaW8-Zs8UmCF6FdaAPXfbjyXQXlEmpQWnM2bqWHmHyl7c_wSb5pYs6_xbXgiZl3sKhvE-Ae5MmiGKyTyvIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d206e144.mp4?token=mUL1PhMsaxUqRTyr3GAaGAEoZENVYpqcssDDPcB4Dq4SfzV1DDhQqzZsnwo6EBPHak3SrdOwZVQV15i7aK1nzmnU12FoH6QKzfpotRdNJA0ePBFtNhbzsyq09ifiqVtASQxMe0comteptmxQAAKM9rzWNy6rdPeDXrXT48nfgke6E1AIBBqBr8oV2HoHVQFIVpVtxi1DEsfS4SD6_LN_lvXuQ2Lc_xOuZALj0a_2bB9couaScy38AuRDlK1DCfjXW6amaW8-Zs8UmCF6FdaAPXfbjyXQXlEmpQWnM2bqWHmHyl7c_wSb5pYs6_xbXgiZl3sKhvE-Ae5MmiGKyTyvIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: کشور هایی که به اسرائیل و آمریکا با اراضی خودشون با حریم هوایی خودشون کمک کردند باید پاسخگو و مسئول باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/652393" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
عراقچی: تنگهٔ هرمز در آب‌های سرزمینی ماست و مدیریت آن نیز با ما خواهد بود
🔹
تنگه در آب‌های سرزمینی ایران و عمان قرار دارد و میان آن آب‌های بین‌المللی وجود ندارد؛ بنابراین مدیریت این مسیر باید توسط ایران و عمان انجام شود.
🔹
اکنون نیز ۲ کشور درحال رایزنی هستند تا سازوکاری مناسب برای ادارهٔ آیندهٔ تنگهٔ هرمز و تضمین عبور امن همهٔ کشتی‌ها ایجاد شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/akhbarefori/652392" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652391">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c515097104.mp4?token=IzIz5a_dqUtI0zZI4lR9EaOynZEZPSiwvKUy-yGKV9FuH-V8rkxJVtEba__jdwGpNe_xzJMleCiM8kJDVtGny1mJqyzJ0UYyEAxwdAWXn2Rww-ABMvT5BkFvyKeOBwmsvk6NRbmyJNsHKsjNeKM8Nt7Wm_NOOv6fY66nERw79ZyxT78Fp1dX-ti4cibX93WJcaxh7MXp3POUh1zR5Kpk0mSHUxbwm3y6o9VGii0-oHgnvhQf88oD0-KQzHyAtYw1_j6ZpDtnUOsi3k3W2IhYH0T4-btbuBn5qfwsHg6J9ZLmYpweqGEKnhBaWKja3XVA8hAQXksxaWDYU8nSEKRsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c515097104.mp4?token=IzIz5a_dqUtI0zZI4lR9EaOynZEZPSiwvKUy-yGKV9FuH-V8rkxJVtEba__jdwGpNe_xzJMleCiM8kJDVtGny1mJqyzJ0UYyEAxwdAWXn2Rww-ABMvT5BkFvyKeOBwmsvk6NRbmyJNsHKsjNeKM8Nt7Wm_NOOv6fY66nERw79ZyxT78Fp1dX-ti4cibX93WJcaxh7MXp3POUh1zR5Kpk0mSHUxbwm3y6o9VGii0-oHgnvhQf88oD0-KQzHyAtYw1_j6ZpDtnUOsi3k3W2IhYH0T4-btbuBn5qfwsHg6J9ZLmYpweqGEKnhBaWKja3XVA8hAQXksxaWDYU8nSEKRsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی:  خبر رد پیشنهاد ایران توسط آمریکا برای چند روز پیش هست/ پیام‌های از آمریکا گرفتیم که مایل به ادامه گفتگو و تعامل هستند
🔹
وزیر امورخارجه کشورمان در نشست خبری:
🔹
اینکه مطرح شده آمریکا پیشنهاد یا پاسخ ایران را رد کرده مربوط به چند روز پیش هست که آقای ترامپ توییت زد و گفت که غیر قابل قبول هست و ولی بعد از ما مجدد پیام‌هایی را از طرف آمریکایی‌ها گرفتیم که مایل به ادامه گفتگوها و ادامه تعامل هستند.
🔹
اینکه امروز چطوری دوباره این موضوع در رسانه‌ها برجسته شده، من اطلاع ندارم ولی قضیه مربوط به چند روز پیش هست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/652391" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652390">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffeede06a6.mp4?token=aMYs94Ptl7VMpp7ym7y35cWzx8aUx4SiEpi82baBJzUuawN41JOVx2fRfj8U4U5QGYbjbDSuoRJgyOkrl64bFihJq459_79sx6IU0W0arwstUA3SAeiVCtg7OH4Dgg_hnKUtAXh3DUA-Wmd1w_EZmB5WTNFvdFMTcVbu_fSHKjLhMl6oegpn0KtNJqC4H92iuDElGI-uYSdCR6_xQRuALkyFZVeg0OwbCyc47u5LgxMMS_neRLnUTrMlI3MSvrGNK93MI_InUEEce2e2GIWeCNDjVrvvj9hw2RCKeMl0Z_vUY9uHId4ByIEmk-_C20oaf5jqENvAEdbTZuHuRoLFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffeede06a6.mp4?token=aMYs94Ptl7VMpp7ym7y35cWzx8aUx4SiEpi82baBJzUuawN41JOVx2fRfj8U4U5QGYbjbDSuoRJgyOkrl64bFihJq459_79sx6IU0W0arwstUA3SAeiVCtg7OH4Dgg_hnKUtAXh3DUA-Wmd1w_EZmB5WTNFvdFMTcVbu_fSHKjLhMl6oegpn0KtNJqC4H92iuDElGI-uYSdCR6_xQRuALkyFZVeg0OwbCyc47u5LgxMMS_neRLnUTrMlI3MSvrGNK93MI_InUEEce2e2GIWeCNDjVrvvj9hw2RCKeMl0Z_vUY9uHId4ByIEmk-_C20oaf5jqENvAEdbTZuHuRoLFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به محض مطمئن شویم آمریکایی‌ها جدی بوده و آماده یک توافق عادلانه هستند، ما به مذاکرات برمی‌گردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/652390" target="_blank">📅 14:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652389">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25be2c076c.mp4?token=rpUg6pO-hby6vvWvK9_drCOHVhtc6tczhnUEhPHo4MkOZ3_c3mCDmt4l74yf1BMWf0RrjE8hNEsewNfoKUHLONwSmyZgUx3P8Za90KGaI4jlB8y6ntnUdq0Mj2L0E3I8UGXD2P77Y9aJ8VK5hFy-Vgn35x6rgDC2qjm_TIXmc-t3yGfxVKBGbqTqkW8iOVFpXrAX0RY6j354GEA1ZbD8S3tpnSdeBboiS9GLVFu_b3qfl51axrWP_nyUvsffRtc6D0nawN_pETqq0TB8Xh2-I39bACHEYEd_RYvkDHygKm041ThL1M8I77mSdvwc0pU4O5j7caFw9HPAoPvbBXTf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25be2c076c.mp4?token=rpUg6pO-hby6vvWvK9_drCOHVhtc6tczhnUEhPHo4MkOZ3_c3mCDmt4l74yf1BMWf0RrjE8hNEsewNfoKUHLONwSmyZgUx3P8Za90KGaI4jlB8y6ntnUdq0Mj2L0E3I8UGXD2P77Y9aJ8VK5hFy-Vgn35x6rgDC2qjm_TIXmc-t3yGfxVKBGbqTqkW8iOVFpXrAX0RY6j354GEA1ZbD8S3tpnSdeBboiS9GLVFu_b3qfl51axrWP_nyUvsffRtc6D0nawN_pETqq0TB8Xh2-I39bACHEYEd_RYvkDHygKm041ThL1M8I77mSdvwc0pU4O5j7caFw9HPAoPvbBXTf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: تنگه هرمز باز است/ به جز کشتی‌های متعلق به متجاوزین، همه کشتی‌ها می‌توانند از تنگه عبور کنند
🔹
وزیر امورخارجه کشورمان در نشست خبری:
🔹
ما یک برنامه صلح آمیز هسته‌ای داریم و همیشه آماده بودیم تا اطمینان حاصل کنیم که این برنامه صلح آمیز هست و صلح آمیز باقی خواهد ماند.
🔹
ما آماده‌ایم به کسانی که شرایط ایران را قبول می کنند کمک کنیم تا عبور ایمنی از تنگه هرمز داشته باشند.
🔹
به محض اینکه تجاوزات پایان پیدا کند مطمئنم همه چیز به حالت عادی برمی‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/652389" target="_blank">📅 13:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74d2591b6.mp4?token=LjDkMs2bmcvW5FDs3bGyYtgjL0pqnzZiR7_6UmeLRBmK7_4coV6-pyviMCs1Jq3OrLY2P9vaBJkNDujvCF5N_SBe900M2Kx-Zi287IGgQ8M_TtaYKf87tQA4plK6PYQ4OsDcE-aG4P3KgDow8qh4m0Aih8NQt_5qmMWQl0hrJDAbqPebRtb-yPf0KHOzcJ31tXKYpzfL_qNzlM8kouYQTK4MP-H_zuJZAjG6JEgkS3hn4o6dQaXJBxc4R7_jyp48e7DRRj7dnpPeVZXDaOLII9lc8j7wcg1G-LWKGBCokBqKsanj92Vb4uUOl_FV-vEWZcIUyVx2heaMm30vV6BaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74d2591b6.mp4?token=LjDkMs2bmcvW5FDs3bGyYtgjL0pqnzZiR7_6UmeLRBmK7_4coV6-pyviMCs1Jq3OrLY2P9vaBJkNDujvCF5N_SBe900M2Kx-Zi287IGgQ8M_TtaYKf87tQA4plK6PYQ4OsDcE-aG4P3KgDow8qh4m0Aih8NQt_5qmMWQl0hrJDAbqPebRtb-yPf0KHOzcJ31tXKYpzfL_qNzlM8kouYQTK4MP-H_zuJZAjG6JEgkS3hn4o6dQaXJBxc4R7_jyp48e7DRRj7dnpPeVZXDaOLII9lc8j7wcg1G-LWKGBCokBqKsanj92Vb4uUOl_FV-vEWZcIUyVx2heaMm30vV6BaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: هرگز به دنبال سلاح هسته‌ای نبودیم
🔹
وزیر امور خارجه: تنگه هرمز باز است جز برای دشمنان ما، هر کس می‌خواهد عبور کند باید با ما هماهنگ شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/652388" target="_blank">📅 13:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652387">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLdU-rSwS9eRMh5BlYObJ_4apAEvSV5Z3L80Kb8miDwaPi2igo841oT1iWlBxR84LSjLrHsSY6AgBSeXE4R6n89HoBiTLxDNDUVrpzObk-foUi--X36kYiWO2CRtcTVpsffWp0t9U9ISO9BpUQd4Jy8drLB8CfBgKjtmBkHt1lVUhG3Y-HFOde7t-beAAoppGWQwVx6tc28aBgux0eTOAg12ZNzZtmPWnGNa_vQ7BD1ziY12vbU-9Ru6huVD_59Jf7uJ09_UHetYbaRNMcF2FZRJ0VS9nXh0_RizDs4KxERmM1UkGw4vSZXGchAj1VOXCCK_w4ruVqlMuFoWQliWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکمیلی /
🔹
عراقچی درباره خروج اورانیوم از ایران به روسیه گفت: مذاکره خوبی با لاوروف داشتم. مشارکت راهبردی با روسیه داریم. با پوتین در روسیه دیدار کردم و در خصوص اورانیوم هم صحبت کردیم از پیشنهاد طرف روسی متشکریم این موضوعی بود که باید در حین مذاکرات به نتیجه می‌رسیم. موضوع غنی سازی ما پیچیده است و برای رسیدن به نتیجه با طرف آمریکایی پیشنهاد دادیم این بحث به تعویق بیفتد.
🔹
در حال حاضر این موضوع مورد بحث نیست.
🔹
نسبت به جدیت آمریکایی‌ها شک داریم. آماده توافق منصفانه و عادلانه هستیم.
🔹
رئیس دستگاه دیپلماسی در پاسخ به سؤالی مبنی بر اینکه آیا در زمان اجلاس سران بریکس امیدوارید به اختلافات با امارات پایان دهید؟ گفت: ما مشکلی با این کشورها نداریم. آنها هدف ما نبودند. پایگاه‌های آمریکا در این کشورها قرار دارد.
🔹
امیدوارم در اجلاس سران به فهم مشترک برسند. ما قرن‌ها با هم زندگی کردیم.
🔹
اماراتی ها باید متوجه این موضوع باشند. اگر به مسیر عقلانیت برگردند می‌توانند ایران را به عنوان دوست در نظر بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/652387" target="_blank">📅 13:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5517ce1975.mp4?token=XFFaQGRTH_ikN1FgS9A5UGSK4zxlss-LdxrxroHqa-4SdzaIN6AzgDjmDPFrjeN-gCjBd6qqolssKsAtO0eJi2FlU75W7e6B5vh-3RgzpEho7hVDKmagm2gPqHITRkjruYDjCu6Yspe7W5AhPjjvrEEFY9tNX9cBa207NJuvwYWH2ooU2LDqPX6BcQNEgzJa9g-Yb1HpC7XhZXlsbRPCHVKvmw1Wmo75etxM4xDZ2HzNZ6xV8r8R3zgBYdhI_JcyU3K6TDIMvmwDBRCjW8iBrm3wwYGIwYUm8Q5s-9JKrk4scxuJDcqnpGY-PsCJ9P1zoyOMLE3qDMKNd72s6tbJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5517ce1975.mp4?token=XFFaQGRTH_ikN1FgS9A5UGSK4zxlss-LdxrxroHqa-4SdzaIN6AzgDjmDPFrjeN-gCjBd6qqolssKsAtO0eJi2FlU75W7e6B5vh-3RgzpEho7hVDKmagm2gPqHITRkjruYDjCu6Yspe7W5AhPjjvrEEFY9tNX9cBa207NJuvwYWH2ooU2LDqPX6BcQNEgzJa9g-Yb1HpC7XhZXlsbRPCHVKvmw1Wmo75etxM4xDZ2HzNZ6xV8r8R3zgBYdhI_JcyU3K6TDIMvmwDBRCjW8iBrm3wwYGIwYUm8Q5s-9JKrk4scxuJDcqnpGY-PsCJ9P1zoyOMLE3qDMKNd72s6tbJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه: پیام‌های متناقض آمریکا مشکل‌ساز است/ توییت امروز مقامات آمریکایی با توییت دیروزشان فرق دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/652386" target="_blank">📅 13:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652385">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر انقلاب اسلامی به مناسبت ۲۵ اردیبهشت ماه، روز  پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/akhbarefori/652385" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652384">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036c33f3d1.mp4?token=XYJtc2miu_toLs_VjcI-70gaYZMOSWUiw-zIRrjDT3Ltdw2lwYlm1lH_mDWKkdGsL2JUfWx51uBQKUogslUHHvXRE0pi0tdZeR5CM5XVs4OtkFtnBjapSh_08JO5LjsxYibnmItNacTYNmGrTnRM4MP8peP_-PoggTJ_aHpfuWC5Angycc1Ht-AZ3DkAwY7vh8RGTJW8_VtfQdZXzwtut9Hj9tJeqZ-SD8aNJJCF9n0ygRYRNZ0WW7d6YW4erBQvinttp5LWM605NKorjxtkRhNlI2hlAEMD3yb5A0Jy6lqZY8d2l1Oia8aOwxD-J_xyWxJdCkOwz0BWbe77TsY-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036c33f3d1.mp4?token=XYJtc2miu_toLs_VjcI-70gaYZMOSWUiw-zIRrjDT3Ltdw2lwYlm1lH_mDWKkdGsL2JUfWx51uBQKUogslUHHvXRE0pi0tdZeR5CM5XVs4OtkFtnBjapSh_08JO5LjsxYibnmItNacTYNmGrTnRM4MP8peP_-PoggTJ_aHpfuWC5Angycc1Ht-AZ3DkAwY7vh8RGTJW8_VtfQdZXzwtut9Hj9tJeqZ-SD8aNJJCF9n0ygRYRNZ0WW7d6YW4erBQvinttp5LWM605NKorjxtkRhNlI2hlAEMD3yb5A0Jy6lqZY8d2l1Oia8aOwxD-J_xyWxJdCkOwz0BWbe77TsY-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما به هیچ وجه نمی‌تونیم به آمریکایی‌ها اعتماد کنیم برای همین قبل از توافق باید همه چیز مشخص و روشن شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652384" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652383">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3abba85efb.mp4?token=epRJvUArw6OKBFFfjHtyaI0FN6nmGq6GvXchTo2kfkTSgjfHTXgJtWHGMsXOhYrESNa5G6_sDxDvkfFh5jWePoZ_SzHEf0Hh6vg8b__SaI2VJpry2qkRVztuYXySIR-r6DDhztWubgoo7xtEwn6GJXdBPMrVdVi1MNLnSq81ieUpWJ6v8uDRjpSQOxna-CtxJ5agmH7WM01XQOEv9FmDs6Qo_HeIMWZwD-zxTDsPS20SxLcnwanaW9LEWBbacFWgxuEuTk55eR4jdOyuvl9D13I2L-HBiWMTkveDiTPRivpaIs1gQEthMn6eb5V309DdNNVKRLao_L7Ph4CIL_PCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3abba85efb.mp4?token=epRJvUArw6OKBFFfjHtyaI0FN6nmGq6GvXchTo2kfkTSgjfHTXgJtWHGMsXOhYrESNa5G6_sDxDvkfFh5jWePoZ_SzHEf0Hh6vg8b__SaI2VJpry2qkRVztuYXySIR-r6DDhztWubgoo7xtEwn6GJXdBPMrVdVi1MNLnSq81ieUpWJ6v8uDRjpSQOxna-CtxJ5agmH7WM01XQOEv9FmDs6Qo_HeIMWZwD-zxTDsPS20SxLcnwanaW9LEWBbacFWgxuEuTk55eR4jdOyuvl9D13I2L-HBiWMTkveDiTPRivpaIs1gQEthMn6eb5V309DdNNVKRLao_L7Ph4CIL_PCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ما در آتش‌بس هستیم اگرچه بسیار ناپایدار است؛ اما در تلاشیم تا آن را حفظ کنیم تا به دیپلماسی فرصتی مجدد بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/652383" target="_blank">📅 13:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652382">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_IIAtcBVB2d6WRQ3qlzRYd7oE9WJ98QJ8UGchRiY4jQbLHre6ZIR3Lldg9Nj0Z1V9SlnfZTuLezVSbfgTNhsuOdxwW_Yoc0BD3zWMSOg2Eyr5e25HCIjcYNNrqIjv3u28ckHS4rm9UNire38y3DesJCd43GBP_V-VY_0eVco9Iatb1-fAdK0Qn5L2qBYqQlnhZqXD9_ExVKP_j-CbxmW2Mdxuub0lSl_rTdQvQAEq2Y-cJDHXE-h868yhVwrgVqVTdUizOBOkmDGMJ0QJmm8gY-0zE6Pzf19EjhbyX8BtAD6mQgzdV4WbYE-eKV4ea--MoLpqi_NOKD2TiThXqPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: امروز آزمونی دیگر در راه است، مبرم‌ترین نیاز در شرایط فعلی، اصلاح الگوی مصرف است
🔹
رئیس قوه‌قضاییه در فضای مجازی نوشت:
🔹
مردم گرانقدر ما بیش از ۲ ماه است که میدان را تسخیر کرده‌اند و حمیّت و غیرت خود را در ولایتمداری و میهن‌دوستی به رخ جهانیان کشیده‌اند؛ هزاران آفرین و مرحبا به این ملت سلحشور و وفادار.
🔹
صرفه‌جویی ملت در منابع حیاتی، مصداق مشارکت ملی و حضور مؤثرتر مردم در میدان است. قطعاً ملت ایران نیز از این آزمون سربلند بیرون خواهد شد.
🔹
در این نهضت ملی صرفه‌جویی و اصلاح الگوی مصرف که روی دیگر جهاد مقدس ملت ایران است، مسئولین و نخبگان باید پیش‌قدم باشند؛ مسئولین با اتخاذ تدابیر و تمهیداتی که مصرف بهینه‌ انرژی را مقدور سازد و نخبگان با ارائه طرح‌های مبتکرانه و خلاقانه در راستای تحقق مصرف بهینه‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/652382" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652381">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZGwWq49As_WLfCAYQkXjfQiMXb-hpPQwOEOMDfiQr4i3BfPkUTQCcvS-sm--PszCBBQOWitN-RcsOjgI1aOi_FgXI3Ncyqkb0fY5sb8r8kqVq7i3r8Kcc6bHiuYgMidYSaRhNAgvxZPkL_7GDAV5J_-MYwk21aX7dHALSFBU23bNz1oBr6aK2Iz6v55fwZXxyjzEPrasVSuZtZPXMLlY5FiA7kEP_9TBYjNpCzNhc_feV4DLoun5LQ-gcPu2KPSvjSlLq_p-x7WWl9WB7rZO2dngdckrIwbmZHwxnZxoZOSpkSGWb4Pz6SucLznyvafGd07twZwjMONNsLC27xvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است
حجت‌الاسلام و المسلمین ابوترابی در خطبه‌‌های نمازجمعه تهران:
🔹
جنگ فقط میدان احساس نیست میدان تشخیص هم هست، در دوران جنگ جامعه‌ای عقلانی است که به استحکام دورنی قدرت و تحکیم پیوندهای ملی، دینی و افزایش سرمایه اجتماعی می‌اندیشد
🔹
آنچه در این نبرد مورد تجاوز قرار گرفت بخشی از حافظه تاریخی و تداوم تمدنی ایران بود، آمریکا خواست امروز ایران را محو کند ناخواسته دیروز بلند ایران را به یاد جهان آورد، این روزها ایران فقط در میدان نبرد و دیپلماسی اقتدار خود را به نمایش نگذارد، در میدان زندگی هم ایستاد و حکمرانی جوشیده از درون ملت را عینیت بخشید
🔹
مهم‌ترین نیاز امروز و فردای کشور تحکیم پیوند ملت، دولت و حاکمیت است ، تحلیل‌های سیاسی باید بر پایه عقلانیت، دانش، گزاره‌ها و داده‌های صحیح ارائه گردد، ارائه تحلیل‌های نادرست مبتنی بر داده‌های غلط و تحریف شده زمینه‌ساز تخریب سرمایه اجتماعی و فرسایش اعتماد عمومی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/652381" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652380">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آمریکا بازهم دبه کرد و پیشنهاد ۱۴ ماده‌ای ایران را نپذیرفت
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره شروط پایان جنگ را داده است.
آمریکا با رد پیشنهادات تهران، بار دیگر مواضع باج‌خواهانه خود در موضوعات مختلف بخصوص در بحث هسته‌ای را تکرار کرده است.
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به پایان جنگ و انجام پنج اقدام اعتمادساز از طرف آمریکا می شد این شروط شامل برداشتن تمام تحریم‌ها، پرداخت پولهای بلوکه شده، پرداخت خسارت‌های جنگ و غرامت، به رسمیت شناختن حاکمیت ایران بر تنگه هرمز  و پایان جنگ در همه جبهه‌ها از طرف امریکا می شد و در صورت تحقق شروط ایران، مرحله دوم مذاکرات با موضوعات دیگر طراحی می شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/akhbarefori/652380" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652379">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3FRjqpeccCUdR4sA1_OZjUOapOwVQ2cj-cAl9viW2YEFWe_xvfbBV71OxbNtFstpXRTXZNKGwTci018BBUGEInULTW0ZjcK4YPPCPKTwnc1BchzZ73qZFfB24RR7PuYCYzhLmByG-fcjfzoIcIG9FrHDkzgjOQ4wzrgaiygrD5FFR4N7qnHS0WK225El90I4ruxHwaeYQTIri7Fkqi-vvJn5CP92i3N1DM9mjvvo4jyz2lBuH8s5m8uF6YGGf--mKX386m5_WVAZGb_tNIG8bF4Ldokpi2q8-z47luW4jKage9HlJ_b1BGt-KIQmTHeUUJLvsvmJ3vbsiVGB-iwjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: هرگونه صحبت از خلع سلاح مقاومت همسویی با اهداف دشمن است
🔹
جنبش مقاومت اسلامی فلسطین (حماس) اعلام کرد: هرگونه صحبت از خلع سلاح مقاومت در حالی که اشغالگری و جنایات آن ادامه دارد، همسویی با اهداف دشمن در تحکیم تجاوزگری تلقی می‌شود.
🔹
جنبش حماس تأکید کرد که «مقاومت با تمامی مظاهر آن، حقی طبیعی و مشروع است که پیمان‌ها، قوانین بین‌المللی و آموزه‌های الهی برای ملت‌های تحت اشغال تضمین کرده‌اند.»
🔹
این جنبش عنوان داشت که «اشغالگری، هر چقدر هم که طولانی شود و فداکاری‌ها هرچه باشد، هیچ مشروعیت یا حاکمیتی بر سرزمین فلسطین ایجاد نمی‌کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/652379" target="_blank">📅 13:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652378">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcr_lgrp0M3nZyVaqFbr65-Ikvy3rBT5zu-FakRgkhTEFCb3yu6Hm0c5sSyT9TJWQ2leRdW6a9Cerx7K50_JZsmcpn7KNMakTozfH1hqt1IITKVU5zRURojaxjX2b6D5Sc-b6pTY9tyPkKKI8HJJGYq9C2BbPz9Las30r3dgh7LLVC2NcnOD7ZeaK7O1Htbfq5AkaamckuB6EyXrl17e2KjfMs6r4-JjgTHs2-zVvAgjlL90m6mKeGMjns_aV8-kUG76fWMXHL6Wwx41EDd0jFcJ2_yLX1feEWGYMjOJ_MG7PzWcWnrh6tLIn2lXkVgTCITJGiy4otQUDwRMxIYRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش تند قطر به یورش وزیر صهیونیست به مسجد الاقصی
🔹
قطر با اشاره به یورش وزیر صهیونیست به مسجدالاقصی اعلام کرد: این اقدام، نقض آشکار قوانین بین‌المللی، تحریک احساسات مسلمانان و تلاشی خطرناک برای تحمیل واقعیتی جدید در قدس اشغالی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/652378" target="_blank">📅 13:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652377">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ایران جزو ۱۰ کشور برتر جهان در مصرف پلاستیک است
سمیه رفیعی، عضو کمیسیون محیط‌زیست مجلس شورای اسلامی:
🔹
متأسفانه ایران جزو ۱۰ کشور برتر جهان در زمینه مصرف پلاستیک است.
🔹
با وجود اینکه مردم ایران دانش و سازگاری بومی نسبتاً مناسبی در زمینه صرفه‌جویی و مدیریت مصرف پلاستیک دارند، اکنون در بحث تولید این محصولات با چالش‌هایی روبرو شده‌ایم.
🔹
باید این تهدید را به فرصت تبدیل نموده و استفاده از محصولات پلاستیکی در زندگی روزمره را به حداقل برسانیم.
🔹
مصرف بی‌محابای پلاستیک در سال‌های آینده می‌تواند مشکلات متعددی را در زمینه مدیریت پسماندهای پلاستیکی ایجاد کند.
🔹
از آنجا که هنوز راه‌حلی قطعی برای مدیریت این پسماندها وجود ندارد، از هموطنان عزیز تقاضا می‌شود با کاهش مصرف پلاستیک، به حفظ آینده فرزندان و پایداری کشور عزیزمان کمک نمایند./جریان
#نه_به_پلاستیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/akhbarefori/652377" target="_blank">📅 13:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652376">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ثبت ۲۵۰ هزار دادخواست و شکایت علیه آمریکا و رژیم صهیونیستی
🔹
معاون قضایی دادستان کل کشور: ۲۵۰ هزار دادخواست حقوقی و شکایت کیفری در رابطه‌ با جنایات جنگی آمریکا و رژیم صهیونیستی ثبت شده و در محاکم و شعب ویژه دادسرا‌ها و دادگاه‌ها درحال رسیدگی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/652376" target="_blank">📅 12:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652375">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای بلومبرگ:
🔹
امارات متحده عربی در طول جنگ، تلاش کرد عربستان سعودی، قطر و دیگر همسایگان را به پیوستن به یک واکنش نظامی هماهنگ علیه ایران ترغیب کند، اما شکست خورد
🔹
منابع آگاه می‌گویند شیخ محمد بن زاید شخصاً با محمد بن سلمان و دیگر رهبران منطقه تماس گرفت ولی هیچ‌کدام موافقت به مشارکت نکردند. در نهایت امارات به تنهایی و کوتاه عمل کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/652375" target="_blank">📅 12:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652374">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a8cdcd60.mp4?token=IASU1b_b8O4nE7qC5keeyAmGzCOLISjXJJQbSbEb3s9V0jOmE9XSNieCkzgpCFH4Z4usKN_4eEF2gA1DdGXIPO6F0f6Vvxb3XR1zQ27QSBmvvnSXw55L_jzCYqGBvhDppuoVLeJL1B3EPGqdVYABoGPaE54h7neaQuWjJcuKLJ0ygtEpZmiEGP19tzUYhHW5n0O9AQyIfoYT9W1RtBAao79i3NuWh5abnOSRajEDxOz88AT_bAAlOUIHclgoofOP31EgI2iXzXdXEUUy82iO6k0ROjtTubGTkmDURwR-GQyv1otD4RR3JUBaoIhOcgLctht9yyyFIszFRouOSmJoPJRJ0zSSWFS_RySSR8gMJ0sbChuxYrk0yoyNJLYQLg8GVY1WIgnh4I7rYkLuGaNmzFGnxflj8FDa4xwC_nhnEgWDnhXyzJQrndSm7CFRK7BfuHMuFVIEqbisHXH2Cei9eWxblwlBIGhWtc5AkRKVJcn6cBiBHF7E6Bjw9PB-YgNeH8eMtV_YLlI64zPrFFY5oaKXzzKK_WELHEDiQ5slBgH_2gmjLei2Ax4zBFgNvNOM0iqRMgdbt85Xo6_ZUF0ELicuKvW9qpm8WGRG5ZJGFzLEHKQImHNSbuV-e3YYYDpvDLxSHBjIAOLXgsVhz1I25pGRME-B6y1q3l9LAfs7Ooo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a8cdcd60.mp4?token=IASU1b_b8O4nE7qC5keeyAmGzCOLISjXJJQbSbEb3s9V0jOmE9XSNieCkzgpCFH4Z4usKN_4eEF2gA1DdGXIPO6F0f6Vvxb3XR1zQ27QSBmvvnSXw55L_jzCYqGBvhDppuoVLeJL1B3EPGqdVYABoGPaE54h7neaQuWjJcuKLJ0ygtEpZmiEGP19tzUYhHW5n0O9AQyIfoYT9W1RtBAao79i3NuWh5abnOSRajEDxOz88AT_bAAlOUIHclgoofOP31EgI2iXzXdXEUUy82iO6k0ROjtTubGTkmDURwR-GQyv1otD4RR3JUBaoIhOcgLctht9yyyFIszFRouOSmJoPJRJ0zSSWFS_RySSR8gMJ0sbChuxYrk0yoyNJLYQLg8GVY1WIgnh4I7rYkLuGaNmzFGnxflj8FDa4xwC_nhnEgWDnhXyzJQrndSm7CFRK7BfuHMuFVIEqbisHXH2Cei9eWxblwlBIGhWtc5AkRKVJcn6cBiBHF7E6Bjw9PB-YgNeH8eMtV_YLlI64zPrFFY5oaKXzzKK_WELHEDiQ5slBgH_2gmjLei2Ax4zBFgNvNOM0iqRMgdbt85Xo6_ZUF0ELicuKvW9qpm8WGRG5ZJGFzLEHKQImHNSbuV-e3YYYDpvDLxSHBjIAOLXgsVhz1I25pGRME-B6y1q3l9LAfs7Ooo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: مهم‌ترین مشکل گفت‌وگوها، پیام‌های متناقضی است که از سوی آمریکایی‌ها از طریق اظهارنظرها، مصاحبه‌ها و مواضع مختلف دریافت می‌کنیم
🔹
در موضوع تنگهٔ هرمز ما مقصر نیستیم. ما آغازگر این جنگ نبودیم؛ ما فقط از خود دفاع می‌کنیم و معتقدم حق کامل دفاع مشروع را داریم.
🔹
تنگه هرمز برای کشورهای دوست، بسته نیست. این محدودیت تنها برای دشمنان ما اعمال می‌شود.
🔹
کشتی‌های متعلق به کشورهای دوست و سایر کشورها فقط ملزم هستند عبور خود را با نیروهای نظامی ما هماهنگ کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/652374" target="_blank">📅 12:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652373">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YInWaibOOUuvITj-DeS-lGlPc5j1-o1vTPL3Lh__qUnzX7V65ILzKDtG2AxNd95LvG6Gr3CQRfzNYkuhz6kIM5M89xXvQFKlKt79DgaPQ1y4CX5oOAF0O3kXIGN89A1veiGcJdYGsWLQ0IgL1pxdI2dBn7Uh7AJyN92H6nf_ETUOoI2lKVs7Rg_2h7vgBeO9LstrIZezu-TqLHMCB-1F44CbJSmOZUR4uKhBlQzjuz55DPH7cvjqxXW0UbNtlpFLEZ8wjDAIkKYxA-UPEpsyVIRZHSN4Ch0QhxgwWm91U7qI9__J45x7QtfpLecDmwGWH_pz4XvCqyee_umRzXVO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال‌تایمز: اگر تا ماه آینده تنگهٔ هرمز باز نشود، به‌دلیل تخلیهٔ ذخایر استراتژیک شاهد موج گسترده‌تری از کمبودهای جهانی و افزایش قیمت‌ها در حوزهٔ انرژی خواهیم بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652373" target="_blank">📅 12:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652372">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwHuWknrBP6aiRCk2CydV20KClBX-IIx1gzaq965of6BY9p3K6UCM149rxGhhl1_ejQnpcSN14wi5ltpnt8-zRP_B9KhNNlsqfIh1GhNDL6z9eZm9W3zW2KQrd2DUDM0YwVkjH5S663l3r_VXix8G0Kontkuto0ub07rt69FTwhKCDaoV0PWs-roMG10Ynha0NJ9H1G6ecXKidXCaOTnD0_JeO2jj0ZrGfdqKa9ay4Wt-ZmDLN91d7_vGBKnif2zyUv1mKFHqApjgUc0JHtDk8ZW1oyECUXoOUuVgpRi_JQp8QtQwkp2g9w1QRQA4oBJvKBuPSym8jbjmjMpI3q0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌گویر: طرح‌هایی برای شهرک‌سازی در لبنان داریم
🔹
ایتمار بن‌گویر، وزیر امنیت داخلی رژیم صهیونیستی در سخنرانی خود در جریان مراسم «روز اورشلیم»، به مناسبت سالگرد اشغال اورشلیم شرقی در سال ۱۹۶۷ گفت: «ما همچنین طرح‌هایی برای تشویق به مهاجرت از غزه و یهودا و سامره (کرانه باختری) داریم». وی در عین حال تمایل خود را برای ایجاد شهرک‌های صهیونیست‌نشین در داخل خاک لبنان ابراز کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/652372" target="_blank">📅 11:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652371">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmb1tSWTucxM1hDpUyMImyLE444_dI5Q8oH904pWzOq6uJF6lgSunpXIv8xGBwcXOIkoOTo5AHjqZ601a_SXbjY_ba7B4vBaPoqfu4830T8eCP_8l03DtxwS8n4O3KACmMZ658eKK434I5YwGou9FhgeGe6fsaZ6rJtCk574zLMY-Ca3LcQL4EONrV8wCiQUGXGnNN2QW4o4xDR8oBWD7MnBENas3qGyLbUQ0XKdPXNFIOqhHWyoxVfAIXiSFsH4iI1aQ6ZJ5wN_buPaexzyIsPuQvuZTMg1ruT58YHvpLRaj9CpZBLuTRr47oB74z6p05bAlTTS0F5Lug0zGky1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل ارتش: تا آخرین قطره خون از ایران دفاع می‌کنیم
🔹
امیر سرلشکر حاتمی: این قدرت ایمان است که می‌تواند یک جنگنده اف-۵ را به فراز مواضع نیروهای آمریکایی در کویت برساند، در حالی که آن‌ها از پیشرفته‌ترین سامانه‌های پدافندی زمین‌پایه و هوایی برخوردارند، مأموریت خود را انجام دهد و با آرامش کامل بازگردد.
🔹
نیروهای مسلح با تمام قوا از تمامیت ارضی، استقلال کشور و نظام جمهوری اسلامی ایران پاسداری خواهند کرد.
🔹
ما به مردم عزیز ایران اطمینان می‌دهیم که با تمام وجود، تا آخرین قطره خون و ان‌شاءالله تا تحقق پیروزی کامل، به این مأموریت مقدس ادامه خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/652371" target="_blank">📅 11:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652370">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsDPtCiihq2ldi027HGOnvc5G1LDrD3E5h2o_7nJJYY4Ngh3OQUW5Otn57UxSpCYaJfF3VTs2Plpui9DR7xQXIuXoXuIoFhbz_Jeay23OlfKLgEQrPHzN5E5E0Tu0Q6QIe4xNTS8A8tvlrCPYUPWwTCTXn5dE3mmEepCU4rZzuALypCEb_vJUcNK5NMFKpSCOZR9W9PtrvvLnXD4eQWgNlMFq0z5hXdOu_KXXfjFyH5d-uqCeEu6KRxKfQY-euLV4zC1v_J3PdYNzIEUVkfuxTn25wi91OdqAB_OjF7tkz2bBAHI3mX82gJP9L-3AfoGm212_-z2QibfdwBPn-gh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: جنگ علیه ایران باید فوراً تمام شود
🔹
«سرگئی لاوروف» وزیر امور خارجه فدراسیون روسیه امروز خواستار پایان فوری جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه جمهوری اسلامی ایران شد.
🔹
لاوروف در گفتگو با خبرنگاران در نشست اعضای «بریکس» در هند ضمن تاکید بر لزوم پایان هرگونه درگیری نظامی علیه ایران، خواستار تسهیل عبور و مرور در تنگه هرمز شد.
🔹
«وظیفه اصلی در حال حاضر در رابطه با ایران، پایان دادن فوری به جنگ و دستیابی به یک توافق پایدار است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/652370" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652369">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJw5jbdi2yLyt93JMBrSPr6MmOVKJmmReOAa0EnhjN-OM9q5Otc5r0_SEhQa3BnvoahIM5ThihZADpIFRpBAyUWOkujBRr19H4UxzlrsBExTaWUiulb4BqyT1JvgWFgHddYq05AnZqjG9ugpGhWZtf6PJJJuS7wvgHiRccZSeLdh7oFj3AEkCXJmV2HCRNRleHZeCN5ETAie4kp89zgW1jKrOjS66cZLSSV_NTutCrdQX4lIUE_NgvmLOm_NaIfcOZpmGw17k3SssEXPfnDSI-25rze684iKQNI9eYICJ8_L3jT7AxEIbSZsmWNj2NDBguLnsryMcKAHs8C-CWpbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح تامین سرمایهٔ در گردش واحدهای تولیدی از خردادماه
🔹
رحیمی، مشاور معاون اقتصادی وزیر اقتصاد: اولویت ما برای آینده، تامین سرمایه در گردش و حفظ اشتغال و نیرو است.
🔹
با تامین تسهیلات حفظ اشتغال بنگاه‌های تولید، در گام بعدی، وام برای تامین سرمایه در گردش واحدهای تولیدی است؛ این وام برای سرمایه در گردش بنگاهها منهای حقوق کارگران پرداخت می‌شود که از اول خرداد اجرایی خواهد شد.
🔹
در این طرح معادل ۱۰ درصد از میزان فروش سال ۱۴۰۳ که در سال ۱۴۰۴ حسابرسی شده را به‌عنوان سرمایه در گردش به بنگاه می‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/akhbarefori/652369" target="_blank">📅 10:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652368">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqnbkgWkiNSzMSKLAyYAamx03DW9JxOra6XDUrR8ILxIFjIRZwYYk0SVhyeI_Yr9J3EPZxSVk3lh09TI5bfl0eh1OYcnypdtgoqW9hp8VX4NXbvd9gx_gsv6UYnhGBFsuVOFsZnV1lqgCaT2fLIKpkuCgTWr5UyS1kjsWRqrsMv4hG5tesNDHRZBXuRAiqXu70NfjHhoKja3iB5wnP9kAOet80xjYvHe0e8sryxL1jI3H6bogWL-6Mb1kA-UiuOXZlU5gvIuP4ERL34i_SP815THJ0wGg-ETkTOQiPgt5tzJI_edCkiFbd2X95QeOOvA291rKzWP0hZr54iI6L73BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز بدون پلاستیک از صبح شروع میشه
🔹
یک شروع کوچک در صبح، قدمی بزرگ برای زمینی پاک‌تر  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/akhbarefori/652368" target="_blank">📅 10:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652367">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_tfZ1DMvPzlVnGihrTcdsc5dm6j8vXmPACq_D3-nIpmqIh-5NULSvUfZUmTAm6JkqBtIT-80qJQrkiEj9oTy0xgrSD4IfpLopMQEhaJaV0AdaYdbczArdW0Bn3Gp9fW-BZFWvPVRwR_AXMI5n1WzQSzNirbhx9DZhbbBdpPyO_u3PlKlXBbGt4_dwDDe-BSfjuPpv8Eqq_f-KnjqNGrrvG3YweNp-_h6p2kXZjbnVKw5I3FzWYiiZpK8ydivop34w73bqE79llHCJaL6jGbbzTlVi9DcKDgWc5mcOmumkxbse_Kf31J9xQRzBOviMyFPJDeQMoD3d8pweDulH3rqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از اعدام جاسوسان تا مصادره اموال؛ قوه قضاییه در این ۷۷ روز چه کرد؟
🔹
در ایام جنگ، قوه قضاییه با تمرکز بر پرونده‌های امنیتی، اقدام به صدور احکام قضایی و توقیف بخشی از اموال مرتبط با این پرونده‌ها کرده است.
🔹
در مجموع، ۱۰ جاسوس حرفه‌ای موساد و سیا در این بازه زمانی اعدام شدند.
🔹
سخنگوی قوه قضاییه اعلام کرده بود که تا ۲۳ اردیبهشت ۱۴۰۵، ۲۶۲ فقره ملک در سطح کشور توقیف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/652367" target="_blank">📅 10:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652366">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZXV54Ahv11Y2LHCMVT8YxdZVJr3vfFN7-AYkMryFPYS-0KeiwMSPpeWtqnj5bHimisdHQVghKA3QTC7HyngiHjQKsTiv7On0emcdvZMLFiVsLtET5j4zS-9NJukP_Df2iMYSfwRkaKaSd2mM-ng2ga4njwMxEynaEFXGxv-YDK-IVEJiV6CbgX4nMMlo-5-nZAXVC_abtZYvsYOB6FtmaaC4kAOYqDzbnbCfta-El8cgcE8NfulguW-YU6nlFF8W86N_zu5L-FsLNHApzal_kkOTlX87SQnkH4q9e9JMBTZ1O3aQ-YzPSM7Gj505SDPtjmqhgvHtYMj7I2WUv1eoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
🔹
وزارت خارجه چین: استفاده از زور درباره مسئله هسته‌ای ایران به بن‌بست رسیده و راه حل نظامی پاسخگو نیست.
🔹
درگیری بین ایران و آمریکا هرگز نباید اتفاق می‌افتاد، نیازی به ادامه آن نیست و پکن همواره معتقد بوده که گفتگو و مذاکره بهترین راه است و بايد يک راه حل فوری پيدا شود.
🔹
وزارت خارجه چین خواستار آتش بس جامع و دائمی شد و تاکید کرد دستیابی به یک راه حلی سریع برای پایان دادن به این بحران به نفع همه خواهد بود و پکن به همکاری با جامعه بین‌المللی برای حمایت قوی‌تر از مذاکرات صلح بین ایران و واشنگتن ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/652366" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652365">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAp-80YoVYoIw2sRaFqKhzJ-i_MEPOcumFcZQgNan85x3kBM8-s8g10cPRiHPLFmqCRU5SMHo8vc1HnLEjJK4DtgvbsTJR9Yrw1lmfRlJvjyLUZ6sRnu8Ob9s6MyeUS_18AwL3ySKKm47A6pLuIlUREzKCoz2HFBcsUFE1wH5RHsTrsvX--jp5k1ULtrJQvu98zPDyY8uFgf3dEc2yVQ0XuI38i_tbBE7KDwQ6BLsfFXI7OsupfCLUUKL0Trd2K2BE6fLmlx7grxDDUIVsQFSmdDaQRzxSSQNRJhkETMi_BUGjqqxPz8AUdcO7ESIW_SuTy4Xz8t8ReJnWLRJQ2zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: شورای امنیت نماد بارز ناکارآمدی و عدم توازن است
🔹
نمونهٔ آشکار ناکارآمدی این شورا سکوت در برابر جنگ تحمیلی و تجاوزکارانه آمریکا و رژیم صهیونیستی علیه ایران است.
🔹
در این جنگ، زنان و کودکان به‌صورت سیستماتیک و هدفمند هدف حمله قرار گرفتند. این اقدامات، نقض فاحش کنوانسیون‌های چهارگانه ژنو و مصداق بارز جنایت جنگی و جنایت علیه بشریت است.
🔹
فاجعه‌بارترین نمونه، حملهٔ دو مرحله‌ای به مدرسهٔ شهر میناب بود که طی آن ۱۶۸ دانش‌آموز و معلم در مکان آموزشی به شهادت رسیدند.
🔹
جامعهٔ جهانی باید معیارهای دوگانه را کنار بگذارد و نشان دهد که جان یک کودک در میناب، به اندازه جان یک کودک در هر نقطهٔ دیگر جهان ارزشمند است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/652365" target="_blank">📅 09:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652364">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
قاچاقچی‌ها بخشی از گازوئیل صنعت را تامین می‌کنند
🔹
اطلاعات رسیده از وزارت صمت نشان می‌دهد، سال گذشته صنایع مجبور شدند ۶۰۰ میلیون لیتر گازوئیل مورد نیاز خود را از شبکهٔ قاچاق تامین کنند.
🔹
سال قبل نرخ گازوئیل قاچاق در مناطقی تا ۱۵ هزار تومان نیز بالا رفته بود.به عبارت دیگر کمبود تامین گازوئیل صنعت سبب شده تا ۹ هزار میلیارد تومان از بخش تولید به جیب قاچاقچی‌ها برود.
🔹
در سال ۱۴۰۴، ۳.۹ میلیارد لیتر از تقاضای بخش صنعت توسط زیرمجموعهٔ وزارت نفت تاییدیه گرفته اما تنها ۳.۳ میلیارد لیتر این میزان تامین شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/akhbarefori/652364" target="_blank">📅 09:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652363">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohebqCtZTqXJMpyRwnjX-ToLwlyHuXbFBOQkU0MsUp8DFUw-0ae8dSLPMarzRhIIfvLoNLlVd40t0q2sGXCxPcyz4qFevE8CT4CCgTr_y8y9kg-yweF_TgfRTJGy32H1Y-f-IG99nI2DRd5HmlstUJMOrUgzBGu0ccLUwcR8bV4-Xx0vT6Ti9XImtsxHW2V8sR6RZN8qu0SdTUQpwtRuGRCrnSPWWaYGU6CGaZAHX-BorkESr6_yeOS2Oeh8aAqz_wBV4IkSNoNj3p5I1ASBXvuaWWMmUVqXKB8Jrm2vMXO8e_nvheu39Tgla3Txj2umLa6ar_JpobqOhavokY7YRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکو: روسیه با اوکراین در جنگ نیست، بلکه با کل ناتو در جنگ است
🔹
نماینده دائم روسیه در سازمان امنیت و همکاری اروپا تصریح کرد: روسیه با اوکراین در جنگ نیست، بلکه با کل بلوک ناتو در جنگ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/652363" target="_blank">📅 09:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652362">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
«تامی داکورث» سناتور آمریکایی: ترامپ تنها در دو ماه اهداف نهایی متعددی را در جنگ علیه ایران تعیین کرد و از تسلیم بی‌قید و شرط و تغییر نظام ایران صحبت می‌کند که هیچ‌کدام محقق نشده‌اند
🔹
رئیس‌جمهور در ارائه یک هدف نهایی روشن، شکست خورده و هفتگی اهداف جدید و محقق نشده‌ای را اعلام می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/652362" target="_blank">📅 09:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652361">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2Wa_sh0pPAoxijncXx7J0DRrqZrcMkvw-AboK7oL03elYDNcnntmmHG-PVsDvYLw6FjaZV6vnd6Bp4ownrjx5AD-ZHTVs8zrGh8hQTnEuNndsPNdZVF7qe1Y2-T5x9hs0buu0KUDRGmKO5yn1VY309QS_DugE5KazW7CB3hg7LDFRrqWEORfiEewtnE5PB6CgFKf1YrdcJsDYy6631zZEgAPuw-gLiUtw6EYdWDqvfkqEZGtvT-quH6U447ViKjoI2TT1p_zD0ZnhdjucS0sJM2g4eZxbzZKPN6u0VYOWlakK2V9KgkrT9hz3mW7SnOqX5hKTlRaq48ehHdUOzWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط جدید دولت برای متقاضیان یورو با کارت ملی
🔹
مرکز اطلاعات مالی وزارت اقتصاد، ثبت مشخصات دریافت‌کننده، هدف دریافت ارز و محل و نحوهٔ هزینه‌کرد وجوه نقدی درخواستی برای متقاضیان دریافت ارز با کارت ملی را اجباری کرد.
🔹
بر این اساس، بانک‌ها و صرافی‌های مجاز موظف‌اند اطلاعات دریافت‌شده را در سامانه‌های مربوط ثبت کرده و سوابق معاملات ارزی را مطابق الزامات نظارتی نگهداری کنند.
🔹
بانک مرکزی به‌تازگی اعلام کرده به همه متقاضیان بالای ۱۸ سال در هر سال، معادل ۱۰۰۰ یورو با کارت ملی خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/652361" target="_blank">📅 09:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652360">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0xU57vqEy-9S_V5B-WxWW9U8CJerStncRNZwHYCMf3ZeGeT_OsvSCkWi0k6F2uLuP3y5qsbMIs0Y_PhZroOrAR3_f9gQo02rDN4s72Kp87z_5PVlM9yufqc8grPrio0fCGv1x-wvAzGwsL5RVbqHeRSZnoVjTWuRuw5PSbPyo0kBmTh-3oGu853SRIj8MK8-415m2kSIV4esUO8UIXuwJmIDrmxn3ddOC5xhKEBESZy-U_9Kcu5N3pohWw6fSUETyp_XXnS-QcyR6V8udWRBMD1eJd7xYPP7NjBVUHNyJCvEYvQDZbSDehZxUNQtrxg-UfZhYYsgBOqi0oTxVW6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۰ روز بدون پلاستیک
🔹
تو امروز انتخاب می‌کنی، فردا زمین ازت تشکر می‌کنه   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/652360" target="_blank">📅 08:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652359">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی ارتش رژیم صهیونیستی از هلاکت یک سرباز صهیونیست در درگیری با حزب‌الله خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/652359" target="_blank">📅 08:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652358">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Ek8EJIFCzXMbNlWgrTLrhZapzsf9VSEXxxLW9FgIvBlzpqiP41Tf41O6Z01747UWV-jyUau0eUXJlViesZffgCIGhpI9fdjjNtBZBGaB0-SdE2NOKYp5nsCBmS488_IoVxgNUbzTXWsa3uMsDnHIQJKGEJWYfqttpIckdT_-M_ndV6mD1GYGIM2mXWPj9_J75L8zguLWOGfV7oA6K4zvTACjBKa4YM-wvsgQHIyK3q3O56jnVuQ7-IeF_QQon8GaCJisdtgwUJXtCpqQPqXB_-bGS0T4Af3PLx9f1yrhCc3MkGoXRM1nypN_Sr-T7s3i6yX1hy0JPFSOQlXGX3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر بررسی کرد؛‌ احیا یا افول؟/ چرا برآورد غرب در خصوص وضعیت محور مقاومت درست نبود؟
🔹
ایران در طول جنگ رمضان نشان داد که برخلاف برآورد غرب، در موقعیت ضعف قرار ندارد. تاب‌آوری عملیاتی، توان پاسخ‌گویی مرحله‌ای و حفظ ابتکار عمل در مقاطع مختلف جنگ، نشان داد که ساختار قدرت ایران همچنان پایدار است.
🔹
جنگ اخیر نشان داد که محور مقاومت نه‌تنها دچار فرسایش نشده، بلکه توانایی هماهنگی عملیاتی در چند جبهه را به‌صورت هم‌زمان حفظ کرده است.
🔹
فعال شدن جبهه‌های لبنان، عراق، یمن به صورت موازی و تحرکات دریای سرخ نشان داد که محور مقاومت قادر است در شرایط فشار، الگوی رفتاری چندلایه و مرحله‌ای ارائه دهد؛ الگویی که از وجود انسجام و مدیریت میدانی حکایت دارد.
🔹
جنگ رمضان نشان داد که روایت ضعف ایران و محور مقاومت، یک برساخت سیاسی بوده که بیش از آنکه بر واقعیت‌های میدانی تکیه داشته باشد، بر نیازهای سیاسی و فشار لابی‌ها استوار بود و میدان، خلاف این روایت را ثابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/652358" target="_blank">📅 08:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652357">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=WSmGaz2AYQJRzyIxFIm8v4SGKI7kPPMJ6HjVcGnwpz27lQmzQ3zyeUxYpEpvpXjPyTf8I5YiAXtN5t2noAC-Pda-Q3VUsW1nwDS-ECtgMUE737LcfQpEkMugajuyRcSaIRrA1_-SKQS_bufm7K3FfXw1yP0NDiqmMYJssPg3R2omoiT0jl81Tz2Gy5xUAGhMyJ7UMcLNe4lEWgbJ17o-PDBAkixFm5xkAeq7f5RWCWWAkO_qQxnT4XgAOExXA2zyaT4JgTVyfk9RMJCxYc_N2C6lzVT0wPFhsbJTTlcTHYPBEZA9_93vW6L6P63hhfo5GDa4pvqAbinMn60NAjfEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be64a7f7c3.mp4?token=WSmGaz2AYQJRzyIxFIm8v4SGKI7kPPMJ6HjVcGnwpz27lQmzQ3zyeUxYpEpvpXjPyTf8I5YiAXtN5t2noAC-Pda-Q3VUsW1nwDS-ECtgMUE737LcfQpEkMugajuyRcSaIRrA1_-SKQS_bufm7K3FfXw1yP0NDiqmMYJssPg3R2omoiT0jl81Tz2Gy5xUAGhMyJ7UMcLNe4lEWgbJ17o-PDBAkixFm5xkAeq7f5RWCWWAkO_qQxnT4XgAOExXA2zyaT4JgTVyfk9RMJCxYc_N2C6lzVT0wPFhsbJTTlcTHYPBEZA9_93vW6L6P63hhfo5GDa4pvqAbinMn60NAjfEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجۀ آمریکا: در مورد ایران، درخواستی از چین نداشتیم
🔹
ترامپ هیچ درخواستی از رئیس‌جمهور چین نکرد. منظورم این است که ما در مورد ایران به‌دنبال کمک چین نیستیم؛ ما نیازی به کمک آن‌ها نداریم.
🔹
ما مسئله را بازگو می‌کنیم تا موضع خود را به‌روشنی تبیین و آن را شفاف کنیم تا آن‌ها درک کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/652357" target="_blank">📅 08:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652356">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت بیستم</div>
  <div class="tg-doc-extra">سردار عیوض‌خان جلالی</div>
</div>
<a href="https://t.me/akhbarefori/652356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
«سردار عیوض‌خان جلالی؛ مردی از دل قدرت و توطئه»
🗓
این قسمت روایتی‌ست از یکی از چهره‌های کمتر شنیده‌شدهٔ تاریخ؛ مردی که در میانهٔ بازی‌های قدرت، جنگ‌ها و توطئه‌های درباری، نام خود را در تاریخ ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/652356" target="_blank">📅 07:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edecf976c1.mp4?token=UUpaRWCbrzc8JJfv5y-g_li1xbFgigZ00APhdPGUHbVOlTZ4dnTA19HWy2C3JGF_kJFL_CE9jbNFuBLtbkDiVJcKJy51gDKTPsYm3eH5U4knw0ESP6Sm-_qCQvcX0I2JaIx1lC7mXEPWHSw48LCXSFBm83X4TqF7c-H6-R8kMSBGy4RFAY-eyiWEhTr5p05sXY0YmbcfGmKn3NTk_byF-E8dOPzjddnrB0lZ1u-mrWX39KiDUEO7bfxCz96QwEzJAPrxipNPVK4lP7db8LnG-Xxz4JU-6X2tHYtmAY10Li9suiVxk9Skj6vpDN65wFpmAXCh7Ll2_W2CQRT1-9jCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edecf976c1.mp4?token=UUpaRWCbrzc8JJfv5y-g_li1xbFgigZ00APhdPGUHbVOlTZ4dnTA19HWy2C3JGF_kJFL_CE9jbNFuBLtbkDiVJcKJy51gDKTPsYm3eH5U4knw0ESP6Sm-_qCQvcX0I2JaIx1lC7mXEPWHSw48LCXSFBm83X4TqF7c-H6-R8kMSBGy4RFAY-eyiWEhTr5p05sXY0YmbcfGmKn3NTk_byF-E8dOPzjddnrB0lZ1u-mrWX39KiDUEO7bfxCz96QwEzJAPrxipNPVK4lP7db8LnG-Xxz4JU-6X2tHYtmAY10Li9suiVxk9Skj6vpDN65wFpmAXCh7Ll2_W2CQRT1-9jCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای دینی به کرمانج‌های ایران‌زمین؛
به آنان که در مرزها زیستند،
جنگیدند و در تاریخ ماندگار شدند
قسمت بیستم پادکست کافئین منتشر شد
☕️
📜
روایتی از زندگی عیوض‌خان جلالی
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
🎧
https://youtu.be/IpMt8R6uBX4?si=5ppbO4oz91FFpq6i
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/652355" target="_blank">📅 07:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
کالابرگ سرپرست‌های خانوار با ارقام پایانی کد ملی ۷، ۸ و ۹ شارژ، و امکان خرید فراهم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/652354" target="_blank">📅 07:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4NPeuD7Kp2uG1SsYvu3HO9lsYkAkOhPfzvqXZl5dJeayPpya8we0pCgapCNFJyeFr8EJSwcPRumKSS-FnP6W-GJzhVt6QuxAkXqxf7fS1u3XgIvmOaMYGFl3LEArNja5cmjgi88S3iuyoLrYMRFmYZTP45B5GStLgD-fXyedNG0fzc2rBkRN8aP_q5oiF8IcL0Re1TyTWpxKaVUOjngkChHAroGkG9cTnJz10FNVuBnWfwidLnS7Xo28sKFivngH6VXPogigszi3tH1O_Nnk98Ez5BnvMBsQXNJ7ofXjiGukx9aXHZ2VxGCvAi9QfnmR7vA8reaO77fErv-GWl5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۵ اردیبهشت ماه
۲۷ ذی‌القعدة ۱۴۴۷
۱۵ می ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/652353" target="_blank">📅 06:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652352">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
یونیسف: ۲۰۰ کودک لبنانی از ۲ مارس تاکنون شهید شده‌اند
🔹
طبق اعلام صندوق کودکان سازمان ملل متحد، از ۲ مارس گذشته تاکنون، در پی حملات رژیم اسرائیل به لبنان، ۲۰۰ کودک شهید و ۸۰۶ کودک دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652352" target="_blank">📅 06:12 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
