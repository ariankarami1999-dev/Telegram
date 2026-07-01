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
<img src="https://cdn4.telesco.pe/file/i58JyhUHqgRorKnq0hR06cOP1HlmhmLaf1WZgc_51rUt6ljGSwVDzKAWqDWXz3CmN_twpNIg40yDOQ3PfU_oLn1NT19fjS90MX0wixWFjXJBdTwKp3Tcj2nFW-BwMpVyjJM0U6h6ibjY_R_69D8hm8-7PLJbUrtxn-38GppcDuXDw3z80DSYHthuwmnXRsUvUFeo9X2Xsr2SrEyyntcJwbAjStyQ2owav118SMUaWHup9yOTqCcuNje-xscnlAuUHgdThPnTDMHlHdgrR26YW8w2bDo3cg3OyxOXq1tz3BgxBUkyj4fuYFhT7RtCDnzD3F8HXV1al-5_bzT0Yoo58Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 20:12:33</div>
<hr>

<div class="tg-post" id="msg-665383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: تیم‌های مذاکره‌کننده فنی ما در حال برگزاری گفتگو با ایرانی‌ها در دوحه هستند
🔹
ما هنوز در مراحل اولیه هستیم، اما مذاکرات به خوبی پیش می‌رود.
🔹
اگر ایرانی‌ها از ورود بازرسان جلوگیری کنند یا به کشتی‌ها شلیک کنند، رئیس‌جمهور گزینه‌هایی…</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/665383" target="_blank">📅 20:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای الحدث: ایران بر تابعیت تنگه هرمز از حاکمیت ایران و عمان پافشاری کرد
🔹
ایران آمادگی خود برای همکاری در ازای آزادسازی دارایی‌های مسدودشده‌اش را اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/665381" target="_blank">📅 20:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مدیر مدرسه</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/665380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
کتاب صوتی مدیر مدرسه با صدای ماندگار بهروز رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/akhbarefori/665380" target="_blank">📅 20:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aa14doIilJlcORVSL6lGNAizjTRJ-uzi8sxaiYXhmXsyjr9qbexH_3jXGzwQXTAbr1p8vrW8pyz2juEz7-czxgSGL53-MM3urTsdFasQ2FetGHPZka7OkhmcVs2kFbTKT6YSpTs6DVN1NpC-cUIJKrfMpvSNyO0zdGWHCyXNRv7OLlhjP3E4k976LVdUDwqLAZs0_G9Bmlaf9NolEsAPEUU_FoMU8TDefvMSMwLTie0bgBvmqBegCAWcjk4wQ7HhX7ihTl-yAgzU5m1lxZWfCqH40XpC0keGCbyPCjFW4xmNVCRHHxNDkHPHkmtLYpAEAIuBUNj5lE-xF0DuRtwRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLm1lVI56SJs9MSZIYd1X3_VcYyuCipS2tHCq-RW35cu7mVlTXB_MOQQ2QTuk52iwMn2S6bQ50V8up7pKjPNGdGyqY2bbtXuBe612hYLI9KQCq0pRAtRunOhPm91niLW7cfT9b909xFvKyQYjEzrxfSYNZhpSJjKPRZ9umE0WvVzJBjIkyqnT_VAopfGpJhNnPmcAZANM5Cc1xTUcHBBHgeLUiIipdr5m9qKTuBuELZfpgWmxflF4BEu-vfkm3v0aHOSXOEpyW_X4kaUrezZXU_KBY5XtwlHJljz0Z1uVZXTUlvR9kVreCROJY941GJ1VnFWGfsPD6kZXncXYguNHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر از فساد و تبعیض خسته‌ای، این رمان کوتاه را بخوان
🔹
«مدیر مدرسه» اثر جلال آل‌احمد، فقط داستان یک مدیر نیست؛ روایتی تلخ، گزنده و واقع‌گرایانه از نظام آموزشی، بروکراسی، فساد، تبعیض و مشکلات اجتماعی ایران است و نشان می‌دهد چگونه ساختارهای معیوب می‌تواند انسان‌های آرمان‌گرا را نیز به فرسودگی و سازش بکشاند؛ مسائلی که با گذشت دهه‌ها هنوز هم آشنا به نظر می‌رسند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/akhbarefori/665378" target="_blank">📅 20:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/akhbarefori/665377" target="_blank">📅 19:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cveDLIOkAPyvS_AhFc5NBsQIuY03ldWr2TI3Re1p85E0JFZYQ2h-7eUcKM2kq4ppZyHFCUNSCoynvofpYWLzcL8FYzJ-SmznDCGEgLdnEwuLgSn8JHaqQCW4fb5eU7tC4rYXw0hn-NjVDFmt9UfdxKaZ0Szj-41pgejYIZd2uER0K1BhdpojOgzZfDl-Dt5tk3tctIM6VBYLaj7Be1GXAr0TC5Npd_hUMcfh55d6roEg8U40pyvgH_fm1Ys7dOaODfYGQZDZV94lKbhU7VVTkB_v73TUrtZZZsztVc8XHD-qN5c-0XrkWUuZnl-htkqe6lwG5tuWBF-scslh5HisfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران در آستانه میزبانی از بزرگ‌ترین رویداد ادبی تشییع امام شهید
🔹
آیین بزرگداشت بین‌المللی شهید آیت‌الله سید علی خامنه‌ای با حضور شاعر برجسته فلسطینی و چهره برتر ادبیات و هنر مقاومت، استاد تمیم البرغوثی و دیگر چهره‌های شاخص رسانه‌ای جهان عرب؛ به همت پردیس بین‌الملل سازمان هنری رسانه‌ای اوج برگزار خواهد شد.
🕓
جمعه ۱۲ تیرماه ساعت ۱۷ الی ۱۹
📍
تهران، شیان، میدان شهید تجرلو،
مرکز همایش‌های بین‌المللی کشتیرانی جمهوری اسلامی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/665376" target="_blank">📅 19:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس، معاون ترامپ: ایران امروز از هر زمان دیگری در بیست یا سی سال گذشته، از ساخت بمب هسته‌ای دورتر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/665375" target="_blank">📅 19:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوشکی: اگر قرار بر ارتباط با کانادا باشد، باید متهمانی مثل خاوری را تحویل دهند
محمدصادق کوشکی، کارشناس خاورمیانه در
#گفتگو
با خبرفوری:
🔹
پس از بسته شدن سفارت کانادا، تحولات بعدی از جمله نبرد رمضان باعث شد کانادا به ضرورت حفظ ارتباط با جمهوری اسلامی پی ببرد.
🔹
حضور ایرانیان مقیم کانادا، ضرورت ارائه خدمات کنسولی را افزایش داده و متهمان زیادی داریم مثل خاوری که خانه امنی در کانادا دارند و اگر قرار است روابطی برقرار شود، باید بازگشت چنین افرادی را هم مطالبه کرد.
🔹
وزارت خارجه باید کانادا و برخی کشورهای اروپایی را برای اصلاح مواضع خود درباره سپاه پاسداران انقلاب اسلامی، تفهیم و متوجه خود کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/665374" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a09f77d74.mp4?token=XTa0pOID7etFNWzgiL4THsBe5BzclOgnVTRz2_76x7iZY3AY6hAEAtu3cTLXIKGJKhwjyTZn1Du0jYqpknN0eOQMJvQ9cNvDds1ptgdI8WBKTrw3TiWjvPTD7wW0qYFtWK3-HQAQ6G7j0PC9C75yktYITu_2V-l-1Sf6MpAu3-0pO-As9pMqBO5ZXFjao6A61KbeZoJkyyCr4inKqVgmFKSole4JTNeB8-jOmNPeikK-4_oDO5_bo9y6FoL-ucgdCFKchJnyw0ZkvOzN56F0sFxoZYQos71fpuSvGUq4hDAG3XMdqJcu8S3KriRrvlutSRlUPUiJJmyA0PFYaNi1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a09f77d74.mp4?token=XTa0pOID7etFNWzgiL4THsBe5BzclOgnVTRz2_76x7iZY3AY6hAEAtu3cTLXIKGJKhwjyTZn1Du0jYqpknN0eOQMJvQ9cNvDds1ptgdI8WBKTrw3TiWjvPTD7wW0qYFtWK3-HQAQ6G7j0PC9C75yktYITu_2V-l-1Sf6MpAu3-0pO-As9pMqBO5ZXFjao6A61KbeZoJkyyCr4inKqVgmFKSole4JTNeB8-jOmNPeikK-4_oDO5_bo9y6FoL-ucgdCFKchJnyw0ZkvOzN56F0sFxoZYQos71fpuSvGUq4hDAG3XMdqJcu8S3KriRrvlutSRlUPUiJJmyA0PFYaNi1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کنگو به  انگلیس توسط برایان سیپنگا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
0️⃣
🏆
1️⃣
🇨🇩
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/665373" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
غریب‌آبادی: مذاکرات برای توافق نهایی هنوز آغاز نشده است
معاون وزیر امور خارجه ایران:
🔹
جلسات هیات ایرانی در دوحه صرفا به طور مشترک و سه جانبه با هیات های قطری و پاکستانی برای پیگیری اجرای مفاد یادداشت تفاهم اسلام آباد، به ویژه لبنان و آزادسازی دارایی‌های مسدودشده برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/665372" target="_blank">📅 19:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
گسترش حضور نیروهای چهارگانه ارتش در سراسر مرزهای کشور
سخنگوی ارتش:
🔹
در حوزهٔ تأمین امنیت، نیروهای زمینی، دریایی و هوایی ارتش، حضور فعال خود را در سراسر مرزهای کشور گسترش داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/665371" target="_blank">📅 19:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس، معاون ترامپ: ایران امروز از هر زمان دیگری در بیست یا سی سال گذشته، از ساخت بمب هسته‌ای دورتر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665370" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh76wdtvwl-m9ES2w6sMGUxjnCOsxIjb6ZYKNtQKHKxMXdKBAUouGlxH0lQdBegtBCYloVXBHc26tvnDWONlc1AyZoL2yGvN_7jTHyG2u6x_2F_X8X5e_O-LRhir7T2iMiKnlpbIG0VZwydmDMA9efbWGIK35qd0O8oKq38yQ-AqX8nxeaZJp3cCNScjnrYyh_ImkkEYQ6AdQ-XsLr2ocIPa_e2yDnCKfnpL7pXZriDXbssFGFeRY2PGTUfd4qOXRiGxpqPH7rEUcUtUVkD_n6qn6_UycMtAEInw41UeZ4T3CshBM-Hy08jy2Ug2_Pw_Ajb9fNwlSH3WsRlbKsLRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدال بر سر اسرائیل در آمریکا؛ جمهوری‌خواهان یک چیز می‌گویند و دموکرات‌ها چیز دیگر
🔹
نتایج تازه‌ترین نظرسنجی مجله اکونومیست نشان می‌دهد ۵۵ درصد جمهوری‌خواهان معتقدند میزان حمایت واشنگتن از اسرائیل «متناسب» بوده، اما ۳۰ درصد آن را بیش از حد ارزیابی کرده‌اند.
🔹
در مقابل، ۵۵ درصد دموکرات‌ها معتقدند آمریکا بیش از اندازه از اسرائیل حمایت کرده است. تنها ۱۰ درصد حمایت انجام‌ شده را کافی و مناسب دانسته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665369" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc7ad112a.mp4?token=tng16mcKGpbrlfG7uoh-0AQhbrSTbesIHoJj0xuSYc-SLRi4_GJiW_eUv8KylebNP_JkkqU-f3e9Y50vNQh2lDPEIeCN9CIRzf23Zrc3QjuinCTAcBTjW8nBxvhFxn8R9aJLkRN7eUc-ZleP5fEXB6In_g7DH6EPG2wXvNdzJ8pXFWyuZOFHgTjFHukCtAtHFdiBgyh0W2pizQWPMw3PLskJOrw3NTAptMB7g2qRLqS5funyodDUrZG56ArqdFk0i1Vj2Ztlx2yJxApJ6DWL0feT_Ed0ohpecv25kQjUVmZbBbWwQPLJ7y41CKn3nayU07y2H9IeLn_jed6yEU6mEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc7ad112a.mp4?token=tng16mcKGpbrlfG7uoh-0AQhbrSTbesIHoJj0xuSYc-SLRi4_GJiW_eUv8KylebNP_JkkqU-f3e9Y50vNQh2lDPEIeCN9CIRzf23Zrc3QjuinCTAcBTjW8nBxvhFxn8R9aJLkRN7eUc-ZleP5fEXB6In_g7DH6EPG2wXvNdzJ8pXFWyuZOFHgTjFHukCtAtHFdiBgyh0W2pizQWPMw3PLskJOrw3NTAptMB7g2qRLqS5funyodDUrZG56ArqdFk0i1Vj2Ztlx2yJxApJ6DWL0feT_Ed0ohpecv25kQjUVmZbBbWwQPLJ7y41CKn3nayU07y2H9IeLn_jed6yEU6mEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قلعه‌نویی: بعد از بازی با مصر خواستم بگویم فوتبال با ما سر ناسازگاری دارد اما اشتباهی گفتم خدا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665368" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKMwl4zdKW8FxiCkMGA_8Rdqact1FX7a4EjRavVfNjuDgj_IPP-44wuC69X7tV2j-aQUuz-VW_LqQ4X3YFht_Y4rLXaKgLNM6szdvRyELXtwfjJjxPQX_S-DYfhb70EconbBTyy9HfhGdVh7TMPfKMnxv9WAgzqVEOgEZefWaD_2ZaVRuZF4If4jb09CTobGX8rhvrz0dESa8g3agJNBPeSaH89gUKWTV9S7Yh9UeRvlPabBg3I8RPMD5xgdBw4tAP5TBiZ-I-IlPL-l2nsyg94uSmCIsVHHYPWPlA4rvYYymzPQo-ScR9Q-xK0rujbuopg8xED8f3KFascW8gbQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش پیج معروف ترول فوتبال به بازی آمریکا و بوسنی در رقابت‌های جام‌جهانی
🔹
امروز همه با بوسنی هستند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/665367" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665365">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPjCdcE2v-fiu_EKiV-sRQhi_0YK__5SXOqFfsQ5kEYXxCJH9hllgfFU8gG2OIQ9lLb4usSVm1w3Iy686tP9GlDHV-edH-FsC6I7cOo0MHjf87hE-s16w5RrQiSeASnuzHAqiXO8mT01ug-oPCSpCzMaxAcfgCJtZ1vaMlDz6yJ0PljGFDCSx8UIE9GZ8C6lXQn0l_RR8SG5hCIVS1NnY74d6PYRLTESGm2Mx7hI1TkgC_OtHjJJ-1obv4rpJe3V-PBHC4cdZMClhzCuBQL-OMG2X05EX0Y9ZnBQKBQOXXqbEZBpjL2VluyrxotdXNfxsMMg5FJpnfQh58A_4vaG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKAXyf2jTY4c2PB-ZGTQ4kRiAp25jkBRmqFthAJZvW4eH4eRuU_k2fk9DojoZmu9ExDek4L01vNfUI281_bimG6iv9syf5yQH-WQoon9Cr8ITl-7wVlK95iq9F62ttmldkE4gXLNP1rq3rDan18Vt2qeCHRQVJIFTPLtoqBjsxwfpaYMcV1y5UH-VAQfSJppnXG9nEeQWvWPItLmImHmi3y_TLnGC1bvhFKDF22Fd_d3_1E5mV4E7DstP4ZV7pOUuvIYGoa3UG5S2iLvxY48VIMLfUFgne9uMvO99T8EweFSjArPiQkfo8ceiBQB7wBtW-W-jFamET78mGTIaDHLMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت بابک خرمدین؛ مقاومت، خیانت و مرگ
🔹
بابک خرمدین (حدود ۷۹۸–۸۳۸ میلادی) رهبر جنبش خرمدینان در آذربایجان بود که بیش از ۲۰ سال علیه خلافت عباسی جنگید. او از دژ «بذ» مقاومت را هدایت کرد و سرانجام پس از خیانت دستگیر و در سال ۸۳۸ میلادی اعدام شد. منابع تاریخی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/665365" target="_blank">📅 19:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665364">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
غریب‌آبادی: دیداری میان ایران و آمریکا در دوحه انجام نشد
🔹
جلسات هیئت ایرانی در دوحه فقط به‌صورت سه‌جانبه با قطر و پاکستان برای پیگیری مفاد تفاهم‌نامه اسلام‌آباد، از جمله لبنان و آزادسازی دارایی‌های مسدودشده برگزار شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/665364" target="_blank">📅 19:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665363">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
نامه اعتراضی ایران به شورای امنیت در پی تهدید رهبر معظم انقلاب از سوی رژیم صهیونیستی
🔹
ایران در نامه‌ای به شورای امنیت، تهدید وزیر جنگ رژیم صهیونیستی علیه آیت‌الله سید مجتبی خامنه‌ای را تروریسم دولتی و نقض منشور ملل متحد خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/665363" target="_blank">📅 19:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665362">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0IjB46X4BEk7RYt-eEAxvOjgAPL6b-JSiYkm2D2-J9M82BG26-Nq1b8m5RtlHVUEfD1k9A6Q8qfPLf9nFdKngiWa5YuW0z5h_X_sqeogz2F8nlcYMpReGte5vj3P_ExdAu-8aniz863xzhjz8sEXvZZcew0qxrgrzdT9CsN0hocfHNUYrSNExG2ncQ34LKE18N8Ew628iz3OVdl4-xX12W3sx-yYte4T2OGydou1QVJeHa3n_1sbdZL7Jw63E-49_0nYin0VN2bXQwT5mVod7H4rQxta1D8e3EX-40wrR1mMWGpHJgYhIlCO7insuEPdKxlBOmHvBKT_dZW4bEOVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/665362" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665361">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frJdUhLGqSS20d8eBEmx80B6eJ90lfMxcUl76eE6YKFfjuQSF9_C-b-1T53kv_bbl3OF1VZPtOYaAR8aoHQLrUu2JIcDZjT_RzPUs3BlMJbPejVqxdQj5HHynHKSkHYWbk3GDy9K7LGmC1UMx4gnTQnOw-LDvXQLAv7ODjWSksKy1DSMTLDnsetfhM-gUPZT9UKb06STUeTryHzlR8a0O1_mFwfDX58zcylBVG6ufPWo4SvLQ60KjsIsm16-jyOdEkFwSkHrpQT4HT56extVIjzvj3DbMpKoJ0cvYeFOyjao9ui1jnhATKyz645s2-Rv5IE4XwrrLre-NszZMEQKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مدیرعامل بانک صادرات ایران در آیین تودیع و معارفه عنوان کرد:
✅
اعتماد مشتریان، سرمایه انسانی و ارزش‌آفرینی؛ سه محور توسعه پایدار بانک صادرات ایران
🔹
مدیرعامل بانک صادرات ایران با تأکید بر اینکه اعتماد مشتریان، سرمایه انسانی و ارزش‌آفرینی برای سهامداران سه رکن اصلی موفقیت این بانک هستند، گفت: تحقق همزمان این سه شاخص، مسیر توسعه پایدار بانک را هموار می‌کند.
⬇️
افشین خانی، مدیرعامل بانک صادرات ایران:
◀️
این بانک صرفاً با صورت‌های مالی و ترازنامه شناخته نمی‌شود، بلکه سرمایه اصلی آن اعتماد مشتریان، انگیزه و توان سرمایه انسانی و ارزش‌آفرینی برای سهامداران است.
◀️
تجربه این روزها بار دیگر نشان داد هیچ عاملی جایگزین سرمایه انسانی متعهد، متخصص و باانگیزه نخواهد شد و تلاش شبانه‌روزی مدیران و کارکنان شبکه بانکی برای حفظ و بازگرداندن خدمات، اهمیت این سرمایه ارزشمند را بیش از گذشته نمایان کرد.
◀️
بهره‌گیری هوشمندانه از فناوری در کنار اتکا به نیروی انسانی متخصص، لازمه استمرار خدمت‌رسانی و عبور موفق از شرایط پیچیده است.
◀️
این بانک با برخورداری از نیروهای فرهیخته و توانمند، حافظه اقتصادی کشور محسوب می‌شود و در مقاطع مختلف از جمله دوران جنگ، تحریم، بازسازی و نوسازی، همواره نقش مؤثری در حمایت از اقتصاد ملی ایفا کرده است.
◀️
با تأکید بر ضرورت تحقق همزمان سه شاخص اعتماد مشتریان، انگیزه کارکنان و ارزش‌آفرینی برای سهامداران، زمانی می‌توانیم بانک را موفق بدانیم که هر سه شاخص به‌صورت متوازن رشد کنند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/665361" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665360">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766a8912c3.mp4?token=djYp30nE-ZQNnRNuevgbaErAZIB3cSW6fD2gBfIiYeHgPIs2LVN6jo5BOhMRYgcYinogiGekLESBZwsY-NRtIBFUklXO6ALwzc4qTgCRh1sfmfDYaaoyTf3pefdGhir-Fyl6oWO8Zsr70kke--I2Q6IHnhu3zoGXTbwXDwgdF-9xWFE7dgWPzCNZKKRkt7hSsmRyhbe23OfcRpUXc_G-6J9LZeqY_8Me-N40LL6LL1KnJCOsXuIDvNIt1tyv02Yqaj7OWQAl7C27yJQFXJVDivsGQ-k7q2dVeMul3MNnC-ulatD4ZH3RZV65RT5oueuE3uNiICVe2WIm4wshPe4oYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766a8912c3.mp4?token=djYp30nE-ZQNnRNuevgbaErAZIB3cSW6fD2gBfIiYeHgPIs2LVN6jo5BOhMRYgcYinogiGekLESBZwsY-NRtIBFUklXO6ALwzc4qTgCRh1sfmfDYaaoyTf3pefdGhir-Fyl6oWO8Zsr70kke--I2Q6IHnhu3zoGXTbwXDwgdF-9xWFE7dgWPzCNZKKRkt7hSsmRyhbe23OfcRpUXc_G-6J9LZeqY_8Me-N40LL6LL1KnJCOsXuIDvNIt1tyv02Yqaj7OWQAl7C27yJQFXJVDivsGQ-k7q2dVeMul3MNnC-ulatD4ZH3RZV65RT5oueuE3uNiICVe2WIm4wshPe4oYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش سنگین تگرگ، بخش‌هایی از استان عسیر عربستان را سفیدپوش کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665360" target="_blank">📅 18:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665359">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
با حکم رهبر معظم انقلاب حضرت سیدمجتبی خامنه‌ای، حجت‌الاسلام‌والمسلمین محسنی اژه‌ای برای یک دوره پنج ساله دیگر، به سمت رئیس قوه قضائیه منصوب شدند/ هم‌میهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/665359" target="_blank">📅 18:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665357">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5bde9fb2.mp4?token=Vg754Y0zbMcaAAmDSY-uWPh1VgaEwIET1ncupQaGjl4SoKbuvCST1_SkWgdzMro7Pr6Vxj7foWuTGI4bGS4KAta6SHIT8MMLjdp85AZ2RJm5OlAgY9Nu6UyRBwxIPMvllTijrktFJ2W6nyPjnsZ1CygI1yf1fMn-_NqT5HZaiUwTDfkGWp4UAgXUfoMT4nzDdsO-0DvW9zixGGTuIdeli9JKVwozIPVSkyOJU9Ct_NRNNdJJCL2sA5vuoieXJJ5ap7Tcf8mUltNSBJjA0GmEs5UZJStH3QpPYrsxGJsULXQvXrpX7Dp-q_3hc0rQeiNKmyekLdZSTsB-3JyyQWtmiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5bde9fb2.mp4?token=Vg754Y0zbMcaAAmDSY-uWPh1VgaEwIET1ncupQaGjl4SoKbuvCST1_SkWgdzMro7Pr6Vxj7foWuTGI4bGS4KAta6SHIT8MMLjdp85AZ2RJm5OlAgY9Nu6UyRBwxIPMvllTijrktFJ2W6nyPjnsZ1CygI1yf1fMn-_NqT5HZaiUwTDfkGWp4UAgXUfoMT4nzDdsO-0DvW9zixGGTuIdeli9JKVwozIPVSkyOJU9Ct_NRNNdJJCL2sA5vuoieXJJ5ap7Tcf8mUltNSBJjA0GmEs5UZJStH3QpPYrsxGJsULXQvXrpX7Dp-q_3hc0rQeiNKmyekLdZSTsB-3JyyQWtmiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از دانش‌آموز آدامس فروش
🔹
بعضی وقتا به‌جای اینکه خونه بشینم و اکسپلور بچرخم، میام یه‌کم آدامس می‌فروشم؛ حداقل از هیچی بهتره.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665357" target="_blank">📅 18:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665356">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1s17Veh9rddTQaaJmdElZtUlTNfXBK8GmMKqutyMCcJqd3JOPnHAgbTXifAdeJHmrMhMkaVCIEtn6ZzctmPNyUFcYTnqN3D-Qq5Zmq-zjYQbOXUQE6GrR-_BdsU2svnNWzOic85zpjV0mZYzGnuXIgqqcWKKWTdlUA7VrgQkjp8lgHosfHB9TuRQZM1cpTrymLXxpjkZjVARxNckaKcKoMRMTgeeAwZNrTl30839zqHpcMbx3CdGdg4w0Y4HZEw9j_Ok2-hbEGHeOtZ3vf2-JrtRCMtAdJd3V-ITl-Q_IZ_b6hopq1zbAhkYxdAhIkBwjfIbiZitUfVjvGL8hR_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان خطاب به تیم ملی فوتبال: خداقوت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/665356" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFyxS7FkQH7z06lpGAAsF4Pgu8d5BM113ocsRQF_w3oPImn1_wTwnvS7ZTOYPlIgRyrHQ6XS4J4eAoftnm9eCipAgUn4krq9eAbgzZ1XttDNt_1ns-jlANkk_F_ljYweFCw68dJYid226SDwDJWKWArAqeGNhYV17-p4KQ8Srulh7-VYSPxeWsWXAppN5XY3s8ZZDKp6tWGUl1QmIFkojJ7rROzvK7piXen7wDNUsW5DohD9TI62HkAa-CTaC3BlsIhQIPsg87XMrAcQiDIXxU-YiIl-Xk2dQrsMecrp0SgmPfMamFNEFHBrZ1mel1J-SJdUv2RoH43bzxtAtB-nuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkExwzaJHs3d6Ibu0bDpYAtksHBiJEnNCGVkN0kJbq1pBsVishvbGjZuXUSZ83uSmixPRT-vadvM2Gavdvf362WmRvGWt6IdsBLXhhQth2f3qeoEddFXBhsSNffJh6bODg_GsaTy3XVwNYcOYdLwSsPkpIZrpdoNCqk7F2vsQTr_x1x_FzuQg8n7Vmx9jEFFbDSlUYWQNk-ramI7Us8hDZUtR_U_Eu7TZLOCOICe5cLfET6kYp1rD9ugkKEG_mOGTiO3484Tx-xRiKB5lmvqi8YDh6-07fis0ibfqHaPTw2wyzaD9CbgYBgycSj4wPfvdoNXC_vyssh_FJte2sEg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKT7nUOzZFyLb25XCOwlO2gP9hQ9D5AKNgO7fmutPC3ETblRvG6P1_rI6uionu5CclcRNjj2EaIBEzq1VjJqLjpzsCuK0ndrRieVui9F8oCvCnPKf1enTsl2oDpjMhiMDU9MELvyiUYhW-S55A8PI85HuPWRjUVzYveMyVkRkp57KLnapKMAeNOSIHp-BgFs0Lur6x4Xn8OLO5tqchS_hSZYD7qUBwECQFJQIMsaLTX2RZKFv2muBCWrUMFcr7WnyqhE1YuaIujN4XaELFQhTK5sCmJbNTGYmTjxxN02D8kF8dC5eJHzPRRz62Ckakh6qSLDjN9xJl2mWEv4E_yzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mojoNeYcosuHiglTxOLxeUe1hYiPUsjND5YKeDr5Pwtj0WUOMNKjjAqbJ4IPcSWklqHuYDxmo6EPCmGNraH9YCX_-gg-pXbd8RPoFwKkrcIi8V1X52CtA0c5Z-BElDoje2kISsOCIT1J5HyfP9FCtRL0MI37inabnIE_dUzA_CTsr3KcBBK4Vk1gWaQEAmxqtfj-rYCA7sHB_TeqkxBv4kVtu4xoAOXX7xe3oqSeyWW7m0phZbTJXjWU0K03KV20WdkaLFpTkBMagJZMb3b8VKa7c01MS9zlyYCU4fGF1mO73o4q_vlJvWILZCBFSGhJoej6gPRzNiHOxhMHbHKcQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJyXHecMrh2vNeJjU0y2PlH44Kxac2AQF8VzxNXvgYw5dqQx7OH8THN3OCDwAVk3CL63jJlO7-rAuPY094OOzzexhVxm9w0L5EYUJyXnCLhdKK_gQO55_0aNFjgl5Iotc8Bme88fcniD3Ohr5n_6Ds7SdHP7Ij0DFPMv-5J-e5K8-52QXENyDohjR9DwqZ-256-VUf0SRowzKEy96UvPwtWICR7zN77hmLNuCaHR2L2vTHBdnMZSjB_ru9jTjvKSJxnAvkCbVAVztHNXKMEmdhgmmZ00itBdYiVPRca1d2DsnaRgAQWEUnqlCTnpNyav6G04NeWOgBob36A1t8O6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmaBA_24U4_bcaWxFNUGjgQgNAmMxqrC_38ADo7iS0fxskzAsWQrHgcssBRbZ11xUi86wQYsKfiIbBy-MemtDRSIVD6Ig2FAj0TjFO87_-ysSu2fOgaXtmx0vsgcNcReRVBt6_Fw91S5zXaUXmL4UF8koSeW2igvFxjETc1cu1VsIdi-pkrGKarJ_lbYNtB77b05N2sdi6UrH4tMZB3I7jvIFZ9aPzr7uWob3kS_KqPBc8OAAUOV40RV2UPiv9zrcVYp-gT-DJ0SSz5msQ9flmX1_PXWk6RNvA3I3NleDybo-p7bTYmsfOenJFdLNmi3VcYfM5Ap2U3fSXkJyG3URg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بهترین حوزه برنامه‌نویسی در ایران ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/665350" target="_blank">📅 18:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be4a6bb48.mp4?token=WmNJZLMhDy-k4W5oqftINFnNqHT-TRa8dk3B6H4Qbg-1hV6ikTKoGEhGHJYMsXl5RCo4n88sHqNv_gqPUJDQ8dD_Xdbixw-wfpSxfe2AzMOoIfkxeKgluiva_w_-FcsPEjNBuDqu_xNLhb3EMX9O0qRNg74FHNrVlsRAcQ71czOE-F8QudhqwTuTOI3B9hUXgyGJSZiXinn_i-07vmTysUjqGgiOiReYAx3P5T4kBjxzceyBhvK2l90ooLKPBV9ELJkyXQEIxbR2o_dDGtYh4Ld2F4pWWJn0KTmztDHeXqR8i7lkf423bhY8RblqScXSIJLH12F1jCKMMgQijXRkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be4a6bb48.mp4?token=WmNJZLMhDy-k4W5oqftINFnNqHT-TRa8dk3B6H4Qbg-1hV6ikTKoGEhGHJYMsXl5RCo4n88sHqNv_gqPUJDQ8dD_Xdbixw-wfpSxfe2AzMOoIfkxeKgluiva_w_-FcsPEjNBuDqu_xNLhb3EMX9O0qRNg74FHNrVlsRAcQ71czOE-F8QudhqwTuTOI3B9hUXgyGJSZiXinn_i-07vmTysUjqGgiOiReYAx3P5T4kBjxzceyBhvK2l90ooLKPBV9ELJkyXQEIxbR2o_dDGtYh4Ld2F4pWWJn0KTmztDHeXqR8i7lkf423bhY8RblqScXSIJLH12F1jCKMMgQijXRkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر قلعه‌نویی: بازی‌های با کیفیتی در جام‌جهانی انجام دادیم و از بازیکنان تشکر می‌کنم که بخاطر مردم ایران و شهدا جنگیدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665349" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKf9VSNU_ChIR7XmOM7tvuwRrc5fk0aPxsfkDBbI31HoVY-LUg_LH2KNoHbruQhuzjaLkGKNcUTRqBOTht7BAjr2vzhK_wGXi5mfcAN1vEjtstEc3XkhLsKUCo2IlzKpZ4E7xZYs-gU1czrCNszrmbHIaLQMkksXewuRD0_3YfF2nZoGURManM2ic_rMPxAbVLTuM9bba26XxxfHY199h_Vb1_WdKpfH7YQYLdSkkVTwir8pz-qfLnc0viGMyy6Thy3k_MZL6dbaUifJ5iFgQODX6fQBg5GJchCngHVVwfK6lA1phAwe1eBFmAOK6ojdcI6ENgU3cD-rbvmOwazZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/665348" target="_blank">📅 18:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665347">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
امیر قلعه‌نویی: بازی‌های با کیفیتی در جام‌جهانی انجام دادیم و از بازیکنان تشکر می‌کنم که بخاطر مردم ایران و شهدا جنگیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/665347" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665346">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICnqihiJQEc-qUqhlWrmM8y44RbXrPs9zvcgtLiNlx1M1ISXdECrmrmNX1ZPcCVfeQdSD4QYwKSUvgt0-jw2XmtxqgAdsh1UCYEMGjyrAuiz8A4mIdU0mGAUVK_yVHlykcDwKoPFiCSqvwGRMDaxEpuGliX0b4CZagkDaifOJD9n7cYl04euZFOHienWCzq_RspNs1jEPYDDp590O9ipvPmDbiyxyLb1C-95rhQ9LrR5LeoCrfz9uv3OgFIwnu0j6wUzUoZQEWmm2rcYCO6CSTciaYMBP3S6EGaAhzlRf6sCxEDGhkULR6mNKYStssUEe61dg2x6Uah0L_gZCDaOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدامات لازم برای نجات اقتصاد ایران از نگاه رهبر شهید انقلاب
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/665346" target="_blank">📅 18:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665345">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5877f3cb1.mp4?token=TKzTLVXbLLAPg2H_AL2gC8AGz0mtp75C7L-xodygkL7NL6dkFWeuM7z43JbBl42F7x3k8zXfwYGnGsVCrz6DGUoB9OWA58UnCidLvSRESGqV5XUx-CuJUPPaYwjUGV1IFVDH9ms7M6A0XWXJwLGdRui1DdPw_dw_NJzL-NqYZe4lMlobXJtBHhLWsOTPTSxOlA3Pgo41hw9lubs68ZSP_ff1rnBt7Kbr7lQ-PF5gwK1N251by8n1jupqia9ShhRtQ-vSnCPg-JTo4BX92-upw19j2yd9aMchGscL8kyomGR03liEP5DylH0PJL5QGKuUcfkCMtasQcWorKZroXuusA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5877f3cb1.mp4?token=TKzTLVXbLLAPg2H_AL2gC8AGz0mtp75C7L-xodygkL7NL6dkFWeuM7z43JbBl42F7x3k8zXfwYGnGsVCrz6DGUoB9OWA58UnCidLvSRESGqV5XUx-CuJUPPaYwjUGV1IFVDH9ms7M6A0XWXJwLGdRui1DdPw_dw_NJzL-NqYZe4lMlobXJtBHhLWsOTPTSxOlA3Pgo41hw9lubs68ZSP_ff1rnBt7Kbr7lQ-PF5gwK1N251by8n1jupqia9ShhRtQ-vSnCPg-JTo4BX92-upw19j2yd9aMchGscL8kyomGR03liEP5DylH0PJL5QGKuUcfkCMtasQcWorKZroXuusA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ملی پوشان فوتبال ایران به فرودگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/665345" target="_blank">📅 18:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665344">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLihdu66tfhGTTOTYqScC2LYzvTrXfAKcwDyHmD-EEEEXpX8uOFkvrDnTxpAOIwgDi1zawkOcMawV1Kfn2_qYc_zsxBrn2l6jL3gLU7NLNsJwd5LaDSDHX1tpO-p4UkxW618tDg4c1yBN4lMtuOqeDIs7E8fy6bbc8udwU3oCE0HD_ZbLer-8FUfLuHKe9Q6xqkxc_eWwLpCiZQgixGMM9rDk-CLmChlkoqs3kirBukNsEPfmvfRMHb-mvENvnzMiuOuCs41oJ8EyuPzR7ROyQfW1Ox9hYC8diwUGpJDqREMgAzM-pxD9uG64I-pJ20r4Vt2karLHMxCBRGM28C_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر مرتضی شیخ؛ طبیبی که «پزشک فقرا» بود
🔹
او از پیشگامان پزشکی نوین خراسان و از محبوب‌ترین پزشکان مشهد بود. سال‌ها بیماران نیازمند را رایگان درمان کرد، هیچ کس را به دلیل نداشتن پول از مطبش بازنگرداند و طبابت را رسالتی انسانی می‌دانست. محل زندگی او همچنان…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/665344" target="_blank">📅 18:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkf7sxfWwKBClkE9enjQ9Lpc-G0hw-U5uY7fNrv4CKtsmz5as3IsRk0JUNWjZ2Fr3f-9bt4Jg4-Z5y4fKwmljO6mFAYU2UWBk2N0LScbANjoCpJPMXCGf8BpJaQRGyBHX_aMeuz2dGQYHBiq_ucWudn6oQe7jX_e5RhhxcZ-rXtxGEPaX4dod8tyRcmGGD_VakmXqAm1I4dn5oo8Jj5rTsCPiBdZcr5i1_sobAEH4Ej5QisZyfvYO0V6UrDfZLoUzZznBorVvU9gJmNAgZy6TeXNGvW7XRTT--G5Fb7XH5jZ-YmiDm2byT1vsITd-D2rEf2PO8W5Rj1tar2MbKYyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn2p-06um9u9PF6Kqwt5xhQQ3Q5cQdEOMg_lz2IKmlREyzc7QnBYLcrn2b1zQMu8mi_Tst4keD0eTcigHdg0W-QHcr-VeQoWuvgF8y0p8aQBJUnbEREOxZrVVGI0l-b7UwC0VlyFjarfmbJxlHAgXLR2G8EhIkmQuF40WJap1lgw9CFkXx_lqC2yHIy7Hpge8FmeyKkCIqSV1k4R5l80QPNRgPdCDMO25rPyDV2XF4yT1ovlIGxqpQZ3YHuGr33Jy5ZmC_xLThlSAlIX6hkKeigUOtesKc1s5I_SFNfLxq2vn32cEhTFTyJcjNHaxuIWVhzAPKcXztIrIEE2Gs7Hsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2I9PUJnhE4fiK5moOcwM1x1j1poxjh4iMbovT_vGBfoLPcT72Y_wIHOLN2EV7cvM6O5RdM13N9OYIkc6HE2e9iHXoBu8GnrIqbNlWB2ZmQMedxakkBXM7NaT5F8ho6-8EkW_VydxraoTyExgSs90oBGmjxLmc5W8pEMYDfVnIGC3DZ4v2iAurAbgw4_HFM1Dr_jkpgzBU5K8esWDE9u-lzw__qEuFfOcpKuM7eEV-X11o3iH8NSVWr1mVjYOnRGr77KwucWKpY4RGX39TMzB6TPYG3F_U_v0Z7RFAFHpi-s33c5ng4KuC2po9Fn-j5rgAm4op674jFo7U0-IW3RYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کارگر جدید بی‌ام‌و؛ ربات انسان‌نمایی که با ظاهرش همه را شوکه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/665341" target="_blank">📅 17:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تلگراف: کشورهای عربی، مستقل از آمریکا با ایران گفتگو می‌کنند
تلگراف:
🔹
این گفت‌وگوها ابتدا میان ایران و عمان آغاز شد و سپس به مذاکرات عمان و قطر، ایران و عربستان و قطر و عربستان گسترش یافت.
🔹
محور اصلی مذاکرات، مدیریت تردد در تنگه هرمز، کاهش تنش‌های امنیتی و ایجاد چارچوبی برای همزیستی منطقه‌ای پس از جنگ است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/665340" target="_blank">📅 17:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f54d31d7.mp4?token=V4axIt-zoLExMdFBIR4qGUSVGcTV0E08Y-47oV7VncHFWfJDYZmw7b5T-VHJDVsDm8517cDGhuSP3pCHp8y5fjaj8ZFTZ_Ga3RYu2vEYUO7KuOPwVU1TfL0pTalJ5ynQkU-ewIMuecjYfwD_Jlyv7LofH0D2bVoCnT-N68gw6kDQCl73mnf2pU7809hTlXAILdecyBwCXp-yvD6VuxTuJhcCMcccXZuB0lKEgxE8dOcLhCK541oHqO83-uQTZ-jznA4AkzK5Q-vxaISSIs8PktFqRG1HdOdQ_HyTAuXJGoO7dpUwlg8eXZ3artjjTNOvQ_7auFv-E_HASLBhD1k5BcAOvQoSa-Mu0n5o_4Y6MwUn7q55VPnwoMb42nARm0MBHmD7Gj4TbkgXTsiavIa0oHVVvTnFENgLoTMj-oHpM3PRMehqbjOneOUfPnsSMIxARTY4mSPpS-WPr7Aqap0h1WgiYjRJwdrL_peFbNS7MnZYnu4eJqWHkjIFrgZvPuPyTxwvRJ7pmvLTx0tOx8daijg7C-8d7sLxcZeC0t1CdjCS0Tyx29X_OBUZHFZc3tiT02DCEbKmNxRh1Rvt-LVhvTohiACTD2Xku_6Shf-35aALKZKfkHkHsoRHWnbzpfx4ApCBbH2FlQ8MUO-RTiOV1ZSk38uB84S8zJwiN-Qrbak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f54d31d7.mp4?token=V4axIt-zoLExMdFBIR4qGUSVGcTV0E08Y-47oV7VncHFWfJDYZmw7b5T-VHJDVsDm8517cDGhuSP3pCHp8y5fjaj8ZFTZ_Ga3RYu2vEYUO7KuOPwVU1TfL0pTalJ5ynQkU-ewIMuecjYfwD_Jlyv7LofH0D2bVoCnT-N68gw6kDQCl73mnf2pU7809hTlXAILdecyBwCXp-yvD6VuxTuJhcCMcccXZuB0lKEgxE8dOcLhCK541oHqO83-uQTZ-jznA4AkzK5Q-vxaISSIs8PktFqRG1HdOdQ_HyTAuXJGoO7dpUwlg8eXZ3artjjTNOvQ_7auFv-E_HASLBhD1k5BcAOvQoSa-Mu0n5o_4Y6MwUn7q55VPnwoMb42nARm0MBHmD7Gj4TbkgXTsiavIa0oHVVvTnFENgLoTMj-oHpM3PRMehqbjOneOUfPnsSMIxARTY4mSPpS-WPr7Aqap0h1WgiYjRJwdrL_peFbNS7MnZYnu4eJqWHkjIFrgZvPuPyTxwvRJ7pmvLTx0tOx8daijg7C-8d7sLxcZeC0t1CdjCS0Tyx29X_OBUZHFZc3tiT02DCEbKmNxRh1Rvt-LVhvTohiACTD2Xku_6Shf-35aALKZKfkHkHsoRHWnbzpfx4ApCBbH2FlQ8MUO-RTiOV1ZSk38uB84S8zJwiN-Qrbak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلسلة‌الذهب؛ حدیثی که تاریخ را روشن کرد
🔹
در نیشابور، هنگام عبور کاروان علی بن موسی الرضا، جمعیت از ایشان حدیث خواستند؛ امام حدیث «سلسلة‌الذهب» را نقل کردند و با تأکید بر توحید و ولایت، آن را در تاریخ ماندگار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/665339" target="_blank">📅 17:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هتل‌های تهران هفته آینده نیم‌بها می‌شوند
جامعه هتل‌داران تهران:
🔹
تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/665338" target="_blank">📅 17:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6f832d65.mp4?token=k0i2ElTOtq59mc4Rzwx8OHdm3BCBWoAaKw1xByLAEnyLOzGJtf9w53TSEVwXern_4_HIXQ0iZ2shFs7_X26-3OvPYuzm7Rq9-5gN0KSTGoPcbItd1mP0JTtIj71I99gqA23MX1ZIzsZmy_dM-JlYWXIVYNqw-v3zHSZrEpoQTGDOdjnHmkhBUMY1eN_MxUe2IFhRzzlGtn6d9vWRiNKB_OnjMTbCxJEVUAsP2ehN3w_IWVdtv6HR0crgDxcyz8rOOs5fLwRENbwzG0gzZlD4_S3QNWc4lK9p1YI-pihxZvK12YHQCiR3TI5bnHqBSCcM8b8BNGMeM_5-rXEv6QWkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6f832d65.mp4?token=k0i2ElTOtq59mc4Rzwx8OHdm3BCBWoAaKw1xByLAEnyLOzGJtf9w53TSEVwXern_4_HIXQ0iZ2shFs7_X26-3OvPYuzm7Rq9-5gN0KSTGoPcbItd1mP0JTtIj71I99gqA23MX1ZIzsZmy_dM-JlYWXIVYNqw-v3zHSZrEpoQTGDOdjnHmkhBUMY1eN_MxUe2IFhRzzlGtn6d9vWRiNKB_OnjMTbCxJEVUAsP2ehN3w_IWVdtv6HR0crgDxcyz8rOOs5fLwRENbwzG0gzZlD4_S3QNWc4lK9p1YI-pihxZvK12YHQCiR3TI5bnHqBSCcM8b8BNGMeM_5-rXEv6QWkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات الکساندریا کورتز، نماینده کنگره آمریکا به لایحه توقف ارسال تسلیحات دفاعی و تهاجمی به اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/665337" target="_blank">📅 17:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کاخ سفید: گفت‌وگوها درباره توافق با ایران ادامه دارد.
🔹
وزیر جهاد کشاورزی: در صورت رعایت شروط ایران، از خرید کالاهای اساسی از آمریکا استقبال می‌کنیم.
🔹
طبق اعلام باشگاه پرسپولیس، همکاری با اوسمار ویرا سرمربی برزیلی به پایان رسید.
🔹
مدودف در آیین تشییع رهبر شهید انقلاب شرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/665335" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAukRGzH84hgBWN_YQ4pix28A0-grRT12Hi5TDis-MC3eunkJLRimCApidAhYXuRqNCD0ZHsk_PG-utvid562unArkAX_HY059XyE3h1-CT1lk2r2RV5Ivix-efRf1D6WTxtpUmcN6FZtdbmp7711YaJkosrPYkI9znXjEjwYiijo6kzEe0Mg-7Sg0fOgJaXyiBRp2YaWoVAVTw1MFkhWygsgUpyts_fjWoIUf4ZnEHKGo6UXmEqgZZOTfZS9DNxrXZX6BezyqUC6N-0HyB34oyzgGkPhlvZwXINZnxerRz-ELRA6aLzH0R0KiRAs_bx7aoJ6hV3Bgl_9fJMZhsPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این چند اتفاق سرنوشت ایران و منطقه را مشخص می کند/ شبه کودتا در عراق مقدمه «سونامی» است؟
🔹
اگرچه ایران در حال حاضر، درگیر مساله جنگ با آمریکا و آتش بس در لبنان است اما این تمام ماجرا نیست. اتفاقاتی به مراتب کم سر و صداتر اما مهم تر در حال رخ دادن است. شاید یکی از مهم ترین این وقایع، دستگیری برخی نمایندگان عراق باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227179</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/665334" target="_blank">📅 17:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA0VvW1ukfgBGeYULbCHbuinfrkaK5pIJC0qmk6n-qD1_BotyVuDBZqu5pNH5vmXrx-U3liNdSh9BRkwWsUoWSxyT9BGxrvuAnEErmgiNN-gQcu48cfIgQyNzcpTvRIIJY0aaFHLw2nYvvEqQZuNrnb6edyCgjjXQl9XpH5F9ameuWUh1Au7XJQS28x1pnUf0xGGXI2oM-kH81mFbyaoF3M6jTb0A83MSX4tmBpREnhh0r9roCGohaMreRB4j3DGsr4WHBujPsBoUO9b8rJKjwkmRjou9Fqa3AucfvyUdQ4hAP5MdlEkxieS-F0UJA_BNq_NkmE3NUU9oMDY7zQynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه رنگ‌ها در قلب شیراز؛ سرای مشیر چشم‌ها را خیره می‌کند
😍
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/665333" target="_blank">📅 17:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
متفکر آزاد، عضو هیأت رئیسه مجلس: حتی اگر آمریکا گندم را به ما ارزان‌تر هم بفروشد، نباید از این کشور خرید کنیم/ نباید پول به جیب قاتلان رهبر شهید انقلاب بریزیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/665332" target="_blank">📅 17:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7d97719e.mp4?token=vgHWLkQTV-9PKqVj1KMe5QnCgapSfuColUOCrBvNfndIFfZIA2fwERlJtNpbPkLA_7EUEWrVYsf7fvi2pLWMfE8NiI_OXSEvJhUk-DQbQ-XvamNIpaXfvoOdD35O2p-_kCGHMW_bjWxYgPnnPuBq2hTYxLdQJ9ZNippws1XifwS79UbrTKQm3dUh8gblAYA7kxrYF686DptIZboX1mpV4TfhP0qdpsUCyXAdQHZkUJSJqibhyWXePYeN6YKb507qx9_3dKJ97tY7ExGaBTuPSyI8QIEVPr1mfhjPpkT3r17J-XPxdN-9SDgqCKp_2focowfw1Lb9efR3QN7MCHBlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7d97719e.mp4?token=vgHWLkQTV-9PKqVj1KMe5QnCgapSfuColUOCrBvNfndIFfZIA2fwERlJtNpbPkLA_7EUEWrVYsf7fvi2pLWMfE8NiI_OXSEvJhUk-DQbQ-XvamNIpaXfvoOdD35O2p-_kCGHMW_bjWxYgPnnPuBq2hTYxLdQJ9ZNippws1XifwS79UbrTKQm3dUh8gblAYA7kxrYF686DptIZboX1mpV4TfhP0qdpsUCyXAdQHZkUJSJqibhyWXePYeN6YKb507qx9_3dKJ97tY7ExGaBTuPSyI8QIEVPr1mfhjPpkT3r17J-XPxdN-9SDgqCKp_2focowfw1Lb9efR3QN7MCHBlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر مستقیم واردات کالا یا دور زدن‌های پرهزینه؟!
مجید شاکری، کارشناس اقتصادی:
🔹
مابین وضعیتی که شما از یک مسیر پرفساد و پر اشکال و با سه مرحله دور زدن از کانال آمریکا خرید بکنید و مسیری که مستقیم از آمریکا خرید بکنید، حتماً دومی بهتره و حرف‌های همتی به لحاظ فنی درست است.
🔹
همتی قبل از رفتن به ژنو، به روسیه سفر کرد و در عمل ابتدا در روسیه ترتیبات جدیدی در حوزه تنوع مبادی واردات کالای اساسی ایجاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665331" target="_blank">📅 17:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
روایت بابک خرمدین؛ مقاومت، خیانت و مرگ
🔹
بابک خرمدین (حدود ۷۹۸–۸۳۸ میلادی) رهبر جنبش خرمدینان در آذربایجان بود که بیش از ۲۰ سال علیه خلافت عباسی جنگید. او از دژ «بذ» مقاومت را هدایت کرد و سرانجام پس از خیانت دستگیر و در سال ۸۳۸ میلادی اعدام شد. منابع تاریخی درباره جزئیات زندگی او اختلاف‌نظر دارند، اما نقش او در تاریخ ایران بسیار شناخته‌شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665330" target="_blank">📅 17:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت کار: تعطیلات هفته آینده شامل کارگران بخش خصوصی هم می‌شود.
🔹
موزه‌ها و اماکن تاریخی ۱۵ تیر تعطیل است.
🔹
رویترز: کویت پدافند هوایی خود را با کمک نروژ تقویت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/665329" target="_blank">📅 17:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
امیر قطر با فرستادگان آمریکا درباره ایران گفتگو کرد
🔹
شیخ تمیم بن حمد آل ثانی در دیدار با ویتکاف و کوشنر، دو فرستاده آمریکایی،  تازه‌ترین تحولات سیاسی منطقه و به‌ویژه وضعیت لبنان را مورد بحث قرار داد.
🔹
محور اصلی گفتگوها، بررسی آخرین وضعیت مسیر مذاکرات ایران و آمریکا بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665328" target="_blank">📅 17:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔹
در حمله افراد مسلح به ایست بازرسی سبدلو در بانه تعداد شهدا به ۳ نفر رسید و ۵ نفر دیگر مجروح شدند  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665327" target="_blank">📅 17:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665325">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a9e06306.mp4?token=Uu9DiaOV5yaydkP2ROa3NNpuDIHk6snULHl__JPQYvFPLKSVcdcDVBAVa_ZENRy5oNKAzICQMAIoO_I29E3KIWii4LGq7s6e56NpRmP5H94b2nxhza3zLjuCUrGTh-E1LD3HCphlOmXCBwn-EdeM2S6PDoocP3BWNU5lfwzjSRFWXcfug0E9NxdemNtzULS96eXJNQtTJe1rl_go8rrK6Jb35LmjA5s7INhP76sLOaG7sVTV6r0yehKOGVrOJfbiaV8u-_S0hLKgxuhPYb14_y3uH-jnMtHW-lLnADx4LCCyu1oRG0uKFtjJ0flYryAlp3xIZ9N_ZL-Cfem5_q4YrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a9e06306.mp4?token=Uu9DiaOV5yaydkP2ROa3NNpuDIHk6snULHl__JPQYvFPLKSVcdcDVBAVa_ZENRy5oNKAzICQMAIoO_I29E3KIWii4LGq7s6e56NpRmP5H94b2nxhza3zLjuCUrGTh-E1LD3HCphlOmXCBwn-EdeM2S6PDoocP3BWNU5lfwzjSRFWXcfug0E9NxdemNtzULS96eXJNQtTJe1rl_go8rrK6Jb35LmjA5s7INhP76sLOaG7sVTV6r0yehKOGVrOJfbiaV8u-_S0hLKgxuhPYb14_y3uH-jnMtHW-lLnADx4LCCyu1oRG0uKFtjJ0flYryAlp3xIZ9N_ZL-Cfem5_q4YrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
هشدار گوگل به میلیون‌ها شهروند ونزوئلایی قبل از وقوع زلزله
🔹
در حین وقوع دو زلزله سهمگین ۷.۲ و ۷.۵ ریشتری در ونزوئلا، سیستم هوشمند هشدار زلزله گوگل توانسته بود چند ثانیه پیش از آغاز لرزش‌های مخرب، به بیش از ۱۱.۴ میلیون شهروند هشدار بدهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/665325" target="_blank">📅 16:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای نماینده مجلس: تا زمانی که ۱۲ میلیارد دلار آزاد نشود، هیچ مذاکره‌ای در کار نخواهد بود
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات برای آزادسازی ۱۲ میلیارد دلار از منابع بلوکه‌ شده ایران به توافق اولیه رسیده و تنها موانع اداری و اختلاف بر سر بازرسی‌های سرزده باقی مانده است.
🔹
ادعای ترامپ درباره آغاز مذاکرات در دوحه شانتاژ خبری است و تا پیش از آزادسازی این منابع، مذاکره‌ای انجام نخواهد شد.
🔹
همچنین ادعا شده است که پس از توافق نهایی، زمینه سرمایه‌گذاری ۳۰۰ میلیارد دلاری در ایران طی یک دوره ۶۰ روزه فراهم خواهد شد.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/665324" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم
🔹
می‌دانید الان چقدر سهم داریم؟ هیچ. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/665323" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665321">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjpvhcknutsc5d97qJVFBV6SudsbRY5-D5mjMqzcTohQlxUcDEh15CaAc7lFIDMRqvKTQNgXwwGycQPEQhV_60HVMA_4TfyW9puqxHr9lWHcjkUn5cNzafKCjdO_3BFn2dP9q6N0YYNEqujdxS49D1fX9kzHO7mRdGdZgwbDb4OngLljMzijt-CiaiGCTI1eWa-zvTT-gxrZLFErazGPTd2LWASNa4payiPDl7ERMB-ZYOFHIK3p3ryGyr-N8h8iVFwN35aV5OyWe2Qk11O1eAkLHls1CgsxUdlziqGqAEo_kC74TZPnSh5OkB7C669G--8U1pPe92JJLjAWBy0dvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiBkdWI4Rm2J_5b9ZbY4OktZ9mO-DYEMyP7lZ7SrCPbZe1u9Nr0HSU22drFJZ8iTyuWySjMtT1Jv6yX8A81YrrMdRsyNOZeXW5bDKglr2wmRFesNK16GPp2DlN1iGfrVDbHDhbM7uVNAHPN_aT3N2j31T5AoTizCGfmFSXUKrTnlSIuG9vWFgVmL4BhDFAOcusU-8oqtHmooOgzwQ6HcpGoAC27sZU32GDtEJ61DAGT5-8ExjIyKKFwXZSG31uFi7KoeymKVx1daa_flNuc7UrhPZ68brtyLpkAW65UP2vlkXOcgOPcxUqHTsRlaS3mcvvuVvmxd_Cmoer_q95rtyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یک چراغ خیابانی در وروتسواف، لهستان که کاملاً با پیچک‌ها پوشیده شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/665321" target="_blank">📅 16:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665320">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f12816b9.mp4?token=g-k-kbtGAG72UyB1DikESJHCVajvms22QAUQPU-s36l2JiDub9S4i0Gf5gT5PSu5XphrH3piKt6ihDlTd2d6FitocNjEfZiAQn6jEZiT2oDUKY0mTJzY2F_NvR4nIGXqZK8i8oTrxiq7eUjg_tIgwLLKDkkqIyi4JJ2__04mJkk6Y-qUOAp79-TZxjefQ8pE5c-30lL8grdvZxNb7QwKJppqGq8bzMiHiDOqO4r__3SgcqMd52pgPyMttbcE3yptM7tQIGr1mgLnFbJ0rwu2SNSGE38zyRJMqU_Uchi-A0TMG0o7xXKcPTPdYCJ8xU-cyzu83G0wX-rt9KUr7xan9Q3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f12816b9.mp4?token=g-k-kbtGAG72UyB1DikESJHCVajvms22QAUQPU-s36l2JiDub9S4i0Gf5gT5PSu5XphrH3piKt6ihDlTd2d6FitocNjEfZiAQn6jEZiT2oDUKY0mTJzY2F_NvR4nIGXqZK8i8oTrxiq7eUjg_tIgwLLKDkkqIyi4JJ2__04mJkk6Y-qUOAp79-TZxjefQ8pE5c-30lL8grdvZxNb7QwKJppqGq8bzMiHiDOqO4r__3SgcqMd52pgPyMttbcE3yptM7tQIGr1mgLnFbJ0rwu2SNSGE38zyRJMqU_Uchi-A0TMG0o7xXKcPTPdYCJ8xU-cyzu83G0wX-rt9KUr7xan9Q3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم
🔹
می‌دانید الان چقدر سهم داریم؟ هیچ.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/665320" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ روز دهم</div>
  <div class="tg-doc-extra">محمد حسین حدادیان قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/665317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک ویژه مداحی هیئت قرار ویژه تشییع رهبر شهیدمان
💔
🥀
بر سنگ مزارم حك کنید؛
او غریبی بود که جز آغوش قمر، پناهی نداشت.
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/665317" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4BKyIbcgg255TWyUsZsAKzWnelgjhvae_LosvBXcUStUi9R3537fI7BcAba_8nq7W3BXoIPUCRZLZFv0UVeuYOJ5Skql2KzBX7BOe2T8CK0PDN76Aw0Xck4YaA6MzPlQ9zhoXZBx100xBxydCeEYyk-AKXMXAbx78F42DbAIo_BQ-S03ieOWFh8y1FcxRPqG0E5td9BVc1Z9iTI2RAXd475v46GxE-tKlzrXXQIwd0_foUQD--zyKkX9lryh8hmuXWkYCvhW2hsRRBjJy1AriVssZGyC1zUS208fNcgSWfHhIKUdvOoRJy8UxYutoXoM1AhBWL0aAIGgYglS3eCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtRJXojo3pL0LM9uHpndP9OpISXeyRKvJh3ReZ7Fd8mIz8NTiBTtqDOMY14G8wRpF01cvCPZfbT3lOdxuTMctfIj2J0FhDmY2p44--ooNQoAtfrZCXf-QyejXY7Ee_AoQslh8aWKR9GyV8Hr8KCc4mSdh5gitwYXMLrkhxItQC_MQKSKIsiuiXNtesVftQL0wIGO81tfpch8ua0TrwnqSXolvW4QsVFVX0qQExpg_sL-_pSu0uRM7-ljE0W8b7xr4DbUweRds6EcEoUHWuO2CiHnJkyuWyx_6zq_6o6qP02E89J9nzH1CM4oBt00Q7CuEvgWXp-3FL8juIuMieDgrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست رونالدو، سرنوشت عکاس پرتغالی را تغییر داد
🔹
یک عکاس با ثبت تصویری از رونالدو و بازیکنان پرتغال از روی سکوها و درخواست هزینه آن در کامنت، علاوه بر تگ شدن توسط رونالدو، موفق به امضای قرارداد با تیم ملی پرتغال شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/665314" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCmCY5RuzT3Be52aLFtrMSEKXrMzuLpUOpenl6iqYMtn8a6GCkjYwSgohuLkvC8IcCppwkAIrHIaScufBqhVQ1m6exs1lVGVbBCvMHa8MebrNqEKg26XISOphvoFp5pti1P3RHvza9KGj2bmbFjEWsEczJEfRZe26K1VWzZx3bJ4V6mZPN9nqe7IMRObqo9mW_JuHLi8Wlx71xNmpd6uOScm2cBBcyrg6KWJmXmLQub5G-uBxnS1i32yi4RcHjQ5nlSm13jWAf53JvLjKXtcac1OWy5Bt0bnib77i1imN6HS6FT-aDuhpegHBDJK7IVjMXlnGtzW4FVPlldgY4_fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در حضور وزیر امور اقتصادی و دارایی و با برگزاری آیین تودیع و معارفه
✅
افشین خانی مدیرعامل بانک صادرات ایران شد
🔹
با حضور وزیر امور اقتصادی و دارایی، آیین معارفه افشین خانی، مدیرعامل جدید بانک صادرات ایران برگزار و از خدمات محسن سیفی، مدیرعامل سابق این بانک قدردانی شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/665313" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbrash Group</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a4a2c989.mp4?token=ZWnL6EnA9Sf4n8jfb6r44jVBuUs-KJl4RsndFStUaNXf8nzIMYvyHdmCO1ATI0Iq2VGv2JyvYuRQVz46PoDsz--5FEkaR4mHin8KUd7pi28nOp7YcPMiImMS_aGENrat2Gn4y6YLmVRO7A7f1aNzGrwxBB6LcRLUDG8D9nGAF0d8Exgs5CziClQARpG6wJzFuksJjZkeJADUYIp_p7JHDTAZKEY9aLY8kEsLf9s3YPjgczG1-R223zM-o4NiGkP5gYuwgsrSHwzB7i8truwJCoDTwt1sQUCELgEtQ5IoR3iEYqQBWoVoHcqJ3v6DJQ45ShOuf0jpRttEhf6XggnwCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a4a2c989.mp4?token=ZWnL6EnA9Sf4n8jfb6r44jVBuUs-KJl4RsndFStUaNXf8nzIMYvyHdmCO1ATI0Iq2VGv2JyvYuRQVz46PoDsz--5FEkaR4mHin8KUd7pi28nOp7YcPMiImMS_aGENrat2Gn4y6YLmVRO7A7f1aNzGrwxBB6LcRLUDG8D9nGAF0d8Exgs5CziClQARpG6wJzFuksJjZkeJADUYIp_p7JHDTAZKEY9aLY8kEsLf9s3YPjgczG1-R223zM-o4NiGkP5gYuwgsrSHwzB7i8truwJCoDTwt1sQUCELgEtQ5IoR3iEYqQBWoVoHcqJ3v6DJQ45ShOuf0jpRttEhf6XggnwCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه کارخانجات ابرش
🏭
با بیش از دو دهه تجربه، به‌عنوان
تنها تولیدکننده
هم‌زمان
شیرآلات
،
لوله‌های پنج‌لایه
و انواع اتصالات برنجی در
شمال شرق کشور
،
فرارسیدن روز صنعت و معدن
⚙️
را به تمامی صنعتگران، تولیدکنندگان و فعالان ارزشمند این عرصه تبریک عرض می‌نماید.
🤩
با آرزوی تداوم
پیشرفت
،
نوآوری
و
شکوفایی
در صنعت
ایران
.
✅
ما را در فضای آنلاین دنبال کنید
https://www.instagram.com/abrash_group
https://t.me/Abrashmedia</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665312" target="_blank">📅 16:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تفاوت حقوق ۱۸ تا ۵۰ میلیونی در بین صندوق‌های بازنشستگی!
ولی‌داداشی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بر اساس قانون برنامه هفتم، صندوق‌های بازنشستگی باید برای کاهش آشفتگی مدیریتی تجمیع شوند.
🔹
برخورد با تخلفات احتمالی در روند ادغام، تداوم نظارت مجلس و سازمان بازرسی و یکسان‌سازی حقوق بازنشستگان با کاهش اختلاف پرداختی بین صندوق‌ها لازم است.
🔹
تفاوت فاحش حقوق بین صندوق‌ها مثلاً ۵۰ میلیون تومان در برخی صندوق‌ها در مقابل ۱۸ میلیون تومان در تأمین اجتماعی با عدالت اجتماعی منافات دارد و ادغام به یکسان‌سازی حقوق کمک خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665311" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ترامپ متوهم: ما سه شب پیاپی ضربات شدیدی به ایران وارد کرده‌ایم، اما در حال حاضر روابط بسیار باهم داریم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/665310" target="_blank">📅 16:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnm09lz3RQUBeNQR1EzzGsDOt8ExdDqAjWvo_gArdgiKENy5_pFJlqDjembcCiOncll_RJ0dLa7nrNAByQ_gwhTFFpAWVajXk62dHg977mrQyrOronXMyKvqLfq4ClAnHwzqIGM4foVq0gKJvCc9ssJxmg4J2b_ye3-WPJY6IurGuAhY8EBXR-DuoDjjnHFyl5wvTpfnhrjtEYMKsY5BWAPV1WOUjMzC5T0Rz2eEkcLij8NDVp20CP1AIZTtWjL7UKTDg1-kkHPC8Xr1Wwc72AskgEQE_3FOKrcFirRBHW2f4znuZPORxezUqzcg-arXXuFNJxgbAxziH8kSyJE2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ تهدیدی خاموش برای طبیعت و سلامت انسان
🔹
پلاستیک فقط یک زباله نیست؛ تهدیدی است که از دریاها و جنگل‌ها تا سفره غذای انسان نفوذ کرده است.  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665309" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83c6cadb4.mp4?token=no6piV77lf3LsIq-Z3nbH7xXsKJTWrkA4056V6I9IU0Wfy0nbnU6PX6d7rUWlSpNvXFg5OK8eDyKqeUBOPpDADIMqaiMvD0KQ6itLEIMp169LpjknKl9O4UlZCh6TUcEWC5LO9GJ98DyZKXkTDoypVRkW36Zt-sztErmJyb-ogarQTyAE-a-y5rqcyxubWeQihdBgy5lww5dJnGaQ3Df_ViqcOAULCYF2ejSgwS9b9NYySeYmwtczR0ujSSIclJRaBcUfgUk1y17FPoBh41lTj5gi85NrqqllXoCH0h9oMEbq7q4InYqa7IrCg_fLUIu9GtjcLI1HiQqaqdx4rGxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83c6cadb4.mp4?token=no6piV77lf3LsIq-Z3nbH7xXsKJTWrkA4056V6I9IU0Wfy0nbnU6PX6d7rUWlSpNvXFg5OK8eDyKqeUBOPpDADIMqaiMvD0KQ6itLEIMp169LpjknKl9O4UlZCh6TUcEWC5LO9GJ98DyZKXkTDoypVRkW36Zt-sztErmJyb-ogarQTyAE-a-y5rqcyxubWeQihdBgy5lww5dJnGaQ3Df_ViqcOAULCYF2ejSgwS9b9NYySeYmwtczR0ujSSIclJRaBcUfgUk1y17FPoBh41lTj5gi85NrqqllXoCH0h9oMEbq7q4InYqa7IrCg_fLUIu9GtjcLI1HiQqaqdx4rGxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ما سه شب پیاپی ضربات شدیدی به ایران وارد کرده‌ایم، اما در حال حاضر روابط بسیار باهم داریم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/665308" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb7qOeFBnOWOVR4Z59ALaMWFARwcRqaI2aMZMD6NfNFQyK-zlOHW29sUGVE5dvirtdZOox6EEbf8JROJW9PzXi5H_eyQBN9sSrDLPbjLSyripDtEssDHKn-AblLsQCLXYJByma5KP6NR-In7AY-fYt8JQMEfKUNOrMklHYn4Kp0uaJGcXmX8fugwQ-13VGeSJihE5Wxs8RpfXLE-lxLzq-Jd02iNmIgA0P6x9PZ8usv-5K5RRfR1X5qHLDyGKCD9AxJamkBSSYVclipRYFVvzsXyr2hRjs1LLbuv6dWS6i8m1y4mMLcWQzbiXoxJYqUVXroynIjmuuaKhXt9LY8kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند پایان استعمار در جهان
🔹
در سال ۱۹۲۵، ۹۷ کشور امروزی تحت استعمار قدرت‌های اروپایی بودند.
🔹
پس از جنگ جهانی دوم، موج استقلال‌خواهی باعث فروپاشی سریع امپراتوری‌های استعماری شد.
🔹
بریتانیا و فرانسه بیشترین تعداد مستعمرات را در اختیار داشتند و بیشترین کاهش را تجربه کردند.
@amarfact</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665307" target="_blank">📅 16:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SH-e8iw90vVKjJDdubr7eYUWws95mER1DMIHXNTibrueZBoLExjgn5rFDBr8nvGJfUlXz1mdsbBU3aauW0DjxtgsiNj06X8JrTeau2SWHH17xsNt9Fg-NC9oXLzpwAiYgcD2_Zmi23AC1wTDSZxMI590OccnCjwKz5VCAkqEHYbvFi36gZ7ASP8u_HuJFtW2wSZe5UlgNwKloFsONI8RDJtDIEn72S2AjhnFZz8NZ8p2E3i4pf8tx6CplpEz-V0EPfjiYXvaEkj51XJnvOggokDm-dGy0l8_a1q3b9FsHP9Xg6WgN8aLytaAvfVoELWUHpa0xHsPgPLO8uIO32eWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbzmWUxARPBGY9JsBzTWb9glrMjwLLInglLvydn1erw4tmBtPVHeXCyDf9bcvjrcX11SK2A5Is3JDBMwxnPEo1hv8gzZClwBU-hs1Qd5_jXU4NHp9tU7p85ubsNTGRgDxxw216W9Z-FF_qQsGizxyehrWImOWRDEcdlwLfRI4MEbgSVrgf9eMxJ8a_4VeTLtoJJ8pdi7k-52p-BIK63orX9tVR4QFLXiAagMVwJPaZIdKLwwmF75w9rNsIPy5QgEeXLDymEWxjbIW2ufBR1yI0MSWTsUibKxCnEaYz2blTdI2MxLAnENaW1LyftxsNzgXBKUqu4e7Bufv2Sip8uJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvAZ388wmSGf7f9U2j2cXtP15E2M-9XM9P8eTw9n7_barF27g73mVkFgDjdePWorMBtci0bxMpfX3nSmcGBsERNtJYXRd3jzEbPNs1MtZSLbK2k1751wGbZwpMKGWhFwSMir3yN6DhCIm5emLPRF5uwSsg3KpQJAdZKfJXIE_x-3GAMDDXdhKjFzeBjC486hkRUe00tD2pti1BZmzpvjr9llSow29jq0EvEba2Pe9hMHPrZd6z5afpra0iOFX0fOiPliaxJ9J5S1uI_mdX5lzfcc6oMgFB-Gxi7ybuTghzgbukRb2HLrh5i2ZA7MDUrcvEfhRO0ZfVs7lTfPRcjbpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴ اشتباه والدین در آموزش سواد مالی #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/665304" target="_blank">📅 16:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f119648.mp4?token=g30TXNruzT_FyqivUli5O-FNWiYPqxr46KbOA7yzdOLqmNQFa4DLTEwu2c1vcrDKA5nhYrtS9yx6pBqpzr_G5KOr2_gF-ELpf486uNkPqTyuRpXFrvN1RQjqxp33iiP5jUyyUPf18ANeT9QUvHJvMeB5JuQyk36f5ce85uYX4wEqaXPMsIUlrCr6b9fTOD5STdNRfdEvxjqEUoypiHCAEE7Obm7Eim8KTrZeT72EB3fXgOvmABRsBL3xqhrLQr0SPWpHmzYZ0gZAesZ_DkpxeADKlPk5Y1Po5LGTMDibQTpycYTK_mcWHALyCQ-ZPDmYIYn9qPqpzQsIIBXdtabRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f119648.mp4?token=g30TXNruzT_FyqivUli5O-FNWiYPqxr46KbOA7yzdOLqmNQFa4DLTEwu2c1vcrDKA5nhYrtS9yx6pBqpzr_G5KOr2_gF-ELpf486uNkPqTyuRpXFrvN1RQjqxp33iiP5jUyyUPf18ANeT9QUvHJvMeB5JuQyk36f5ce85uYX4wEqaXPMsIUlrCr6b9fTOD5STdNRfdEvxjqEUoypiHCAEE7Obm7Eim8KTrZeT72EB3fXgOvmABRsBL3xqhrLQr0SPWpHmzYZ0gZAesZ_DkpxeADKlPk5Y1Po5LGTMDibQTpycYTK_mcWHALyCQ-ZPDmYIYn9qPqpzQsIIBXdtabRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنج کودکان غزه زیر سایه جنگ
🔹
دختربچه‌ای در غزه میان صدای جنگنده‌ها و انفجارها، با پناه گرفتن در آغوش عروسکش از ترس فرار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/665303" target="_blank">📅 16:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ایرانی: مذاکرات دوحه بر تنگه هرمز و پول‌های بلوکه‌شده متمرکز است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665302" target="_blank">📅 15:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گلایه نمایندگان مجلس از وزیر نیرو، پس از بازگشایی صحن به جد پیگیر استیضاح علی‌آبادی هستیم!
هاشم خنفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
نمایندگان مجلس خواستار استثنا شدن استان‌های گرمسیر مانند خوزستان از برنامه‌های قطعی برق هستند، چرا که هوای این مناطق در شب بالای ۳۰ درجه و در روز حدود ۵۰ درجه است و قطعی برق معیشت مردم را مختل کرده است.
🔹
وزیر نیرو، قبل از جنگ آماده استیضاح بود و نمایندگان امضاهای لازم را جمع کرده بودند اما به دلیل شرایط جنگی و توصیه مقام معظم رهبری مبنی بر تعامل مجلس با دولت، استیضاح به تأخیر افتاد.
🔹
نمایندگان معتقدند وزارت نیرو برنامه قابل قبولی برای رفع مشکلات کوتاه‌مدت برق ندارد و در حوزه تولید، توزیع و نگهداری شبکه دچار ضعف اساسی است. در خوزستان مشکل تولید برق وجود ندارد بلکه مشکل اصلی در توزیع و مدیریت انرژی است.
@TV_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665301" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na8ASjfjVFl5A3k7mpKVxF07uSNE6Ax80EKWIp5biS1__Ri8oxCEo6unNieEqUNFLpHixBRJ4YHCeKvxAzyXvs2uKFHBXrN_nMsiWKnQxdsDaFiCHFnrC7MmAdIB999Cr4SzA-azy1_i-i6J6UOdfuNAfbr4whDJg1851yBEDVLkcY3tN88MgQo2I-EzjrY9aIy-qnBd986yUvaYxoan4mtNvpeWoWECo4glfU_QBUnIPThdRczNM8rPucV_A01G12qhzsh8Apa_ehvYPix0rrEIW8IST9RAFb9qFmdqd3qq-NwULXoSW_UIOeCBB8wg-ywNfJOvUxkaWtwNUF2l5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/216c4f6e99.mp4?token=VJ9fR1yj9yuwcpRQVy6PL08GB-XbK1Nb1VkTbdOxFazbqYtmGmR9HcZS20DVCJjkjfHR_jqQDf7KeCVefJzKe-mOcK055ZVj2RQyp8FACC-91-vQW6LHjwLsRt05epqafNGCCSg9y3jwNAr230D6ELOhiZM7RG-JkMMd2TjEXkWdEj1BHZ3s-IGKzFrtYPQ2iIH3HMYge63LK_MAloNj12IZkfglpxOxpH7zyINytMNw1a6uJyZvZOywaCVl27YVe_GOUGywysESMz7iyIuCjUWr6kxoxZoV0tH76XVoBzVuitUDN6wPLt-F5g087238lUoai0R2vjSygXucmX450g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/216c4f6e99.mp4?token=VJ9fR1yj9yuwcpRQVy6PL08GB-XbK1Nb1VkTbdOxFazbqYtmGmR9HcZS20DVCJjkjfHR_jqQDf7KeCVefJzKe-mOcK055ZVj2RQyp8FACC-91-vQW6LHjwLsRt05epqafNGCCSg9y3jwNAr230D6ELOhiZM7RG-JkMMd2TjEXkWdEj1BHZ3s-IGKzFrtYPQ2iIH3HMYge63LK_MAloNj12IZkfglpxOxpH7zyINytMNw1a6uJyZvZOywaCVl27YVe_GOUGywysESMz7iyIuCjUWr6kxoxZoV0tH76XVoBzVuitUDN6wPLt-F5g087238lUoai0R2vjSygXucmX450g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عذرخواهی رامین رضاییان از هواداران تیم ملی
🔹
رامین رضاییان با انتشار پیامی ضمن دلجویی از مردم بابت ناکامی اخیر تیم ملی، تأکید کرد که همواره با تمام وجود برای شاد کردن مردم جنگیده و خود را همیشه در کنار آن‌ها می‌داند.
مردم عزیز ایران...
بعد از بازی هرچی تو دلم بود بهتون گفتم، بازم میگم؛ ببخشید که نتونستیم اون خوشحالی‌ای که لیاقتش رو داشتید بهتون بدیم.
من همیشه خودمو یکی از مردم دونستم و هرچی دارم از محبت شماست. هر بار پیراهن تیم ملی رو پوشیدم، با تمام وجود برای دل مردم جنگیدم و این فقط وظیفه‌ام بوده.
می‌دونم این روزها حال مردم خوب نیست؛ فقط دلم می‌خواست حتی برای چند دقیقه لبخند رو لبتون بیاد.
کنار مردم بودم، هستم و همیشه می‌مونم.
ممنونم از همه عشقی که همیشه بهم دادین
🤍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/665299" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELoyErWYZX3dWfyUvlQVeOhb_EOBYtBSZtjgvCygmA3k3VuMSDuOknbviv5rI9A-UDOh9US_sZGZpyLTrCJ7nShIED3uz5awUVcd2l_UU8sQsKSrjVhktcRaR3OK4CgvKkZweQW5knTVEHYRxnaYs58Y8ef85RF8LqV_0ffzG9hSiv_6ujQQrYp_EJEOPUQOD5DbZ48-VzZzWSxjO1aaM_ztb9iYa3XYFCc97Yr0yOnt0lCeXIEC9_q6mXChHJipSjoCwqquOS2mFPxGYRYLqstfuUSELQDWwM8v2rZMY9pYnm9vsyTzsGqqojariqV9lIEhguk8TCZJDwX9kBlkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعات کاری سامانه پايا در ایام برگزاری مراسم تشییع و خاکسپاری رهبر شهید انقلاب اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/665298" target="_blank">📅 15:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983e343a91.mp4?token=fs3PH90VOEMimq0sTnINLJRkGIkbp_OgCl2xdNnqFUn8TARSUwgj6iiuun5ENiUR63a0EYS6u3a5zFVy0zqm_kq-4ijZZUyXSie1B2-V-KCwqXhv8I_didJfnsHk0z6aUlV0HkAuyBLuENznQdPF-XHMJ8g9XZ1l1J5Ev6T1TPaBmSdaa9dL7lrT2RNaWipDS0dW7O11rbUmFZFGaYofUAnL54KcJKZZaGCgf7W2QucLrgo-IKNnhzwqG3DYIvUjd51ONeKhcmSF6uD4iMnvJ8dDMMT6ZvCONpWCLiHB09FMtmKzfDKpdljYBLwSgZC8ZUZctPHzx1CPZYgqmkSm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983e343a91.mp4?token=fs3PH90VOEMimq0sTnINLJRkGIkbp_OgCl2xdNnqFUn8TARSUwgj6iiuun5ENiUR63a0EYS6u3a5zFVy0zqm_kq-4ijZZUyXSie1B2-V-KCwqXhv8I_didJfnsHk0z6aUlV0HkAuyBLuENznQdPF-XHMJ8g9XZ1l1J5Ev6T1TPaBmSdaa9dL7lrT2RNaWipDS0dW7O11rbUmFZFGaYofUAnL54KcJKZZaGCgf7W2QucLrgo-IKNnhzwqG3DYIvUjd51ONeKhcmSF6uD4iMnvJ8dDMMT6ZvCONpWCLiHB09FMtmKzfDKpdljYBLwSgZC8ZUZctPHzx1CPZYgqmkSm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی تیرانداز، شکارچی دقیق آب‌ها
🐟
🔹
ماهی Archerfish با شلیک قطره آب، حشرات بالای سطح آب را شکار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/665297" target="_blank">📅 15:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-poll">
<h4>📊 آیا شماهم در یک ماه اخیر افزایش قیمت نان را در شهرتان تجربه کرده اید؟</h4>
<ul>
<li>✓ بله،گران شده است</li>
<li>✓ خیر، تغییری نکرده</li>
<li>✓ مشاهده نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665296" target="_blank">📅 15:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1UcV4V1BhGgEOB-dN9WQIDH7b8fV46pDmVJKu2Lpxy9exPUaDgkFo1UCoAXrPC527YYlwo5JRMz0DhzLRVXgpYZ0nEzgNEohi8xoOkpo21BBKYUFEzLBeyIcS3HZCdaW2KDvnGSzIhjxFE4BshzP6AW-Ec5gde_8wJ-Lvg00CdimDSVtiD-_FO7fEwy8Yoj8VzhEtdbREKsokZ_o3SBLS5n5m3JfqiUu1hsoesDVxqDeIfQwL2LwdZEJvYrfzf_foE5rgbzBL4dOrgH1zfYsvIZdoLD7w6vNc2unRNRKiwj8jR1rMVWyJJ9HEvZ2Sf6gEAranI7FBac9Tta3iMepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دیده‌نشده از رهبر شهید انقلاب در کنار موشک سجیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665295" target="_blank">📅 15:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
فوران کوه آتنا در ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/665294" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXQeWd2OFWXraGSZvgYPHb58d40DuxoC7CCNS9KD5E9g1k-2mEnTwB-z5DBr4rHma8lF0oHA0qX32MPC99q_LXFNQqkmX1BdERXMbWqcQtq7uW0eUg_o4l2D4iYLQ_d2cPPT2KquSvn4yEP332OBzJRsYvUmFthiDnaSplHyT76CDHF3xSJgVUDWiMEsaUrTw3yBsxpt0E299mvXJBj6VsNH5wKRViOHNscM4m29kMlU1aSW1gnytBsNvxKgFVjCYRVCrw4lGK70-OPQtKOG7QS5vPlaHApnEFBQHLFkuwwjfPaDoGtHlyuB71pwF-Q4drfSADiEHYmSKFJJ-6fkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله ایران به پالایشگاه حیفا کارساز بود؛ ۶۰ درصد تولید نفت اسرائیل مختل شد
شبکه ۱۲ اسرائیل:
🔹
حمله به پالایشگاه حیفا، مخزن اصلی بنزین و نیروگاه آن را نابود کرد و ۶۰ درصد از ظرفیت تولید فرآورده‌های نفتی اسرائیل از بین رفت.
🔹
بازسازی کامل تا سال ۲۰۲۸ طول می‌کشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/665293" target="_blank">📅 15:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp6qju0J9xcOJ7Ny7FHo3_1P55gTbgc4VaCBhTDIUoDMvwxAUJIVyKS7h-E_nqUZi6wRXNOo34sR2URIGryazaMuHlY3HLojrdTjvO1zvSb659C99idlRkJYQ1eyDHLr2zfHkQ4hLFJR217ZhayQ7I3s6JwEEL335sb3DVLVkv8TeQsXLwksrz4DsTmgxhr0ERRhoJ83BJskNOcIybhD7Fj042_uEvELlgeft2y4TzdpJkcWVCUirAh5iwg5Rm0mJvSFqT3LPKDAw96RK6xSfPj4ebs0fHfLVGNedFVxuWCo0SjCbc5m3z7C_SiZkxncf2lVgMY3w7ur6BwFdAa-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه درباره شروط تازه ایران در مذاکرات دوحه؛ رایزنی درباره تنگه هرمز
العربیه:
🔹
مذاکرات غیرمستقیم در دوحه ادامه دارد؛ ایران خواستار آزادسازی ۳ میلیارد دلار از دارایی‌های خود در ازای هر پیشرفت در مذاکرات شده و هیئت‌ها برای بررسی پیشنهاد عمان درباره تنگه هرمز، راهی پایتخت‌های خود شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665292" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تصویری از آتش‌سوزی بزرگ در فرودگاه بین‌المللی بغداد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/665291" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
گزارش UKMTO از وضعیت یک قایق مشکوک در منطقه
🔹
طبق اعلام سازمان UKMTO، یک قایق کوچک مسلح با ۴ سرنشین و مجهز به آر پی جی، پس از ترک یک کشتی، همچنان در منطقه فعال بوده و خطر بالقوه‌ای برای سایر کشتی‌ها محسوب می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/665289" target="_blank">📅 14:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPygsx7uCaa8gsi0VxlelEW7YDAR4Ss5XzyOugnAYc_OFY2qgNlLS7U5fcixkxEuLJwqrWzPvhH9QSPMIXYdD-nTCaW1vVdN6_FNt3zP0QS8FDwS-ADLoQ0WwAYYhiPNU6hez_f_2YbQmrHGVdfZztX1oNIsOoRraOafq0kcfM8mRQi89Sc-HxkqH1aPLQOKawxRFaXtTqFfeDtaGmjCW7NsmIY3ufC3bR7Y3TcfLX1DHUOUT9PyeVhofVwHUmAFy0FH9ZCNjgslkWx35Ft8dRww3p72t-SJr7Wr1R0TqpjVQAqAwvVI2ZMiEIiNAdR00nmDJOZ1Kd_4EU2hZ_5_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ بیت‌کوین به زیر ۵۸ هزار دلار برای هر رمز ارز سقوط کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/665288" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAVTSJ9rYU-EvxVRmvx7SwdHMgv_-MwivbF8SXB72AfUQI3vY1HP5nRlAkDdaff1eJf4uuyUX1r2Ai9FI2WHMSL4D6bl2272tLG0g-T16RKowz1VmuCA-2iGRxMnAYr0KXFZxNlsEtcll5bHvXbZUosdRZoo_PamptIj9WrKDzsZWvZCumLT7YpiTUHKM5Lc2GxV1NywdsPlfE_XN2o69LpVT3FAQmKKjA0ecdA4QhINVIGQDqnoBdTYcR1OjgMRqAn79rOld0HdARtUN67yioqKPnWlJC5c_rkK5HlUh7M-AgPmrU7egDyHdcNALVQ226PVqxbIQeVLk-hbpGBtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رز ترنج؛ امنیت دارد
🟢
صندوق طلای رز ترنج پشتوانه واقعی طلا دارد. دارایی‌های صندوق در قالب گواهی سپرده شمش و سکه، با پشتوانه طلای نگهداری‌شده در انبارهای مورد تأیید بورس کالا قرار دارد.
🟢
واحدهای صندوق فقط به میزان طلای موجود قابل انتشار هستند؛ یعنی ابتدا طلا تأمین می‌شود و سپس واحدهای جدید صندوق عرضه می‌شود.
🟢
با «رز ترنج» بدون نگرانی از نگهداری، سرقت یا اصالت طلای فیزیکی، می‌توانید به‌سادگی در طلا سرمایه‌گذاری کنید.
▫️
صندوق طلای رز ترنج از تمام کارگزاری‌ها با نماد «رز ترنج» قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/665287" target="_blank">📅 14:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSypSvZ8Zr2KpqaNh04FUd-lFl1wQABJJ7_lX2ZX3Oksib79Jjs49X94H90hjc1bjjq1vJn8p81lUYN_jq6SZCtiXxWtACviGIEO7mpl6LQ19JPRDcsqDjnFUGFGfRPOK2lItGEbIdJE1Q5Wwq2LuwHkWUBAyPJXoo5NCbaA7IDZttN890DF9mxWdT-cJrLvbJjiRrNdd3hsVIhdHxqWZoRAfhV7iPfoDKgrxFzXSjlys4yVf58LYg_fsUmSq6v-C0YyKSIG99RRBhmegrqjbyho7YjoaKa236WTIWtmMo5sEJazbCnJCdLkL7lWSTuTk_KDUzDprgY5agNQ2xOQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا خبر داد:
بانک کشاورزی در آستانه ورود به باشگاه هزار همتی‌ها / تمرکز همزمان بر تقویت منابع و گسترش تأمین مالی تولید
🔻
مدیرعامل بانک کشاورزی با اشاره به عبور منابع این بانک از رقم ۹۲۶ هزار میلیارد تومان اعلام کرد: این بانک با اتکا به اعتماد سپرده‌گذاران، در آستانه ورود به باشگاه بانک‌های هزار همتی قرار دارد و این ظرفیت جدید را به‌طور هدفمند در خدمت تأمین مالی تولید و تقویت امنیت غذایی کشور به‌کار خواهد گرفت.
🔻
وهب متقی‌نیا رشد فزاینده منابع این بانک را نشان‌دهنده افزایش اعتماد عمومی، ارتقای کیفیت خدمات و تمرکز بانک بر تجهیز پایدار منابع دانست و افزود: این شرایط به ما امکان می‌دهد منابع بیشتری را به شکل هدفمند در اختیار بخش‌های مولد، به‌ویژه کشاورزی، دام، طیور، شیلات و صنایع غذایی قرار دهیم.
🔗
مشروح‌خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/665286" target="_blank">📅 14:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
دستور قضایی برای ترخیص خودروهای منطقه آزاد مازندران صادر شد
رئیس پلیس راهور مازندران:
🔹
با صدور دستور قضایی، فرایند خروج و آزادسازی خودروهای دپو شده در منطقه آزاد و گمرکات استان، از ساعت ۸ صبح فردا، ۱۱ تیرماه، در بندر امیرآباد آغاز می‌شود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/665285" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6db7G-eimb4s4ljEfVmQOOpvtUDPQuFLdOiFoPmZTlFarYJBlREgwXFZWAJ4oHaB5_AZG3t_mBKuTEM7IYqQ1bfW9CTWapaXZcwoPaWYq5zefOwtWriuwRztyxgGxXmV20HJnCuS4ZkIZ3eSDOAkU-YIaSvdChFQwhVSLn66v7fK2IAEGuwaPhDuyrW9De3Zg7lL7LXSC8-yxMsttBnnYwAtH48rQNOK89lC3Kofk5TuhiFYXlgqqYKvRRpMkM46BSWLzaiZSNgTe1lYvPeNI8x0RWLtk45sVcOowHyMRopz87ifiPaidVr57JyrKGkKzIOidQeWc_3WFQbhZrEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از آتش‌سوزی بزرگ در فرودگاه بین‌المللی بغداد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/665284" target="_blank">📅 14:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
گزارش UKMTO از وضعیت یک قایق مشکوک در منطقه
🔹
طبق اعلام سازمان UKMTO، یک قایق کوچک مسلح با ۴ سرنشین و مجهز به آر پی جی، پس از ترک یک کشتی، همچنان در منطقه فعال بوده و خطر بالقوه‌ای برای سایر کشتی‌ها محسوب می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/665283" target="_blank">📅 14:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
کارنامه مثبت دولت پزشکیان/ صنایع در «تابستان» بیشتر از «ماه‌های عادی» برق می‌گیرند!
🔹
بر اساس اعلام صنعت برق؛ از ابتدای خرداد سال جاری تاکنون، صنایع انرژی‌‌بر ۱۵ درصد برق بیشتری نسبت به مدت مشابه سال گذشته تحویل گرفتند.
🔹
در سال‌های ۱۴۰۰ تا ۱۴۰۳، مصرف ماهانه برق صنایع، در تابستان کمتر از ماه‌های عادی بوده. موضوعی که طبیعی به نظر می‌رسد زیرا در پیک گرما، اولویت با بخش خانگی است و برق صنایع محدود می‌شود.
🔹
حتی در سال ۱۴۰۲ صنایع در ماه‌های گرم سال ۱۷۱۰ میلیون کیلووات ساعت برق کمتری دریافت می‌کردند که یک رکورد منفی محسوب می‌شود.
🔹
اما جالب اینکه این الگو در سال ۱۴۰۴ رخ نداده و اتفاقا مصرف برق صنایع در ماه‌های گرم بیشتر از ماه‌های عادی شده؛ آن هم به میزان ۸۷۸ میلیون کیلووات ساعت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665281" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bd6a5f10.mp4?token=NhrQVURFrQyi2CQEr1kdOtZ1n9Ingaij4aEcdfEUPXWbSlUUziSyCMPjNKVvl-LKPi9V-gL0PaiAnbw-i2LneX3IXSOFsuF_PvSl8srLQFQ6dWR7WvZbsrCvg39dhEjTdy0Ha65lnYk4CzFlDqL3QsxFa-wJau_dBWVie2MDqeqFPXWiM88n5ovdYa1lkJ_7xJ1QCteO5aYkSdF-sdtjNkOYK5TDMvsDTRyWQpxxDYTG_rn0cw7BipqTVKPvwBdGLx1_uK9DDj8RDQkx5MRPaisd9FIA22PSLAavHl4Wlwprc-vahpD9aXDGxRb2Bq1W-hF2iOuoscjDKEkNOFIZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bd6a5f10.mp4?token=NhrQVURFrQyi2CQEr1kdOtZ1n9Ingaij4aEcdfEUPXWbSlUUziSyCMPjNKVvl-LKPi9V-gL0PaiAnbw-i2LneX3IXSOFsuF_PvSl8srLQFQ6dWR7WvZbsrCvg39dhEjTdy0Ha65lnYk4CzFlDqL3QsxFa-wJau_dBWVie2MDqeqFPXWiM88n5ovdYa1lkJ_7xJ1QCteO5aYkSdF-sdtjNkOYK5TDMvsDTRyWQpxxDYTG_rn0cw7BipqTVKPvwBdGLx1_uK9DDj8RDQkx5MRPaisd9FIA22PSLAavHl4Wlwprc-vahpD9aXDGxRb2Bq1W-hF2iOuoscjDKEkNOFIZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کشتی به گل نشسته در مسیر غیرقانونی تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665280" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
شهردار ایلام بازداشت شد
🔹
دادستان ایلام از بازداشت شهردار این شهر به اتهام سوءمدیریت و تخلفات مالی خبر داد؛ طبق اعلام مقام قضایی، پرونده تشکیل شده و بررسی‌ها برای تکمیل مستندات ادامه دارد./ فارس
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665279" target="_blank">📅 14:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=OdGJDWXu-0kku581W0LpFF9W2h2HB6r4ESjXKqHn0iYkA3Sq4lWZRB4aAoYaA1qj8SPJDL95L5DcdsYHN7GI0NmGq25T1KP5v2YC-19Ne0JjVL68-fwQfNRKBeNHad_36gsmFzmXIMfZDyUNiQ-c_ERasVHd6XfOMs7aq2za8bTkzsKantkhCQKAtqU-t1NYdXIDbf72aMkfOEBn-KNtyHT8mAo2Y42e1xlLpPbfWp0zhhuANqe41Ud90tmwJwwzY5mqAc_abhxoQFyb04y7_QgqwpE49Gk1GB64PCn2ARVANTIyTgZKFgxIZqEuwXs6DEIgRpmOHUbPv6r-kHmghi6Vy4-dhHyg9pGpo-xxONEkMEzOw6DLiGPaBlyxyipKgswQVQlws0K4u5nKg3TiesSX7NlGFHrU9rUKGIE3ebNiPvm7qNDfm-hv4yi88uIuMYOvmi70XSLagJHaUpdaEhSB0kTRvz0qg5HDJeA0l_6lGLlBQYXeUooH4K2y5xjrhGJe4JTSnXAZY9PbBvoAmO7-fIwoSxl6Vd8pFS73NmUZ_ZJSLOM_d9Kty9ARWQAmKivYoyL_qo1pDsy0lqBRmldFxE3z61UMbOQbmsfdZsDFdHPMxEgknMvdlJXjwdcy00BYkxlKEPwLs721Te4kVbF-JiVh1AwMd43JPLv22Zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=OdGJDWXu-0kku581W0LpFF9W2h2HB6r4ESjXKqHn0iYkA3Sq4lWZRB4aAoYaA1qj8SPJDL95L5DcdsYHN7GI0NmGq25T1KP5v2YC-19Ne0JjVL68-fwQfNRKBeNHad_36gsmFzmXIMfZDyUNiQ-c_ERasVHd6XfOMs7aq2za8bTkzsKantkhCQKAtqU-t1NYdXIDbf72aMkfOEBn-KNtyHT8mAo2Y42e1xlLpPbfWp0zhhuANqe41Ud90tmwJwwzY5mqAc_abhxoQFyb04y7_QgqwpE49Gk1GB64PCn2ARVANTIyTgZKFgxIZqEuwXs6DEIgRpmOHUbPv6r-kHmghi6Vy4-dhHyg9pGpo-xxONEkMEzOw6DLiGPaBlyxyipKgswQVQlws0K4u5nKg3TiesSX7NlGFHrU9rUKGIE3ebNiPvm7qNDfm-hv4yi88uIuMYOvmi70XSLagJHaUpdaEhSB0kTRvz0qg5HDJeA0l_6lGLlBQYXeUooH4K2y5xjrhGJe4JTSnXAZY9PbBvoAmO7-fIwoSxl6Vd8pFS73NmUZ_ZJSLOM_d9Kty9ARWQAmKivYoyL_qo1pDsy0lqBRmldFxE3z61UMbOQbmsfdZsDFdHPMxEgknMvdlJXjwdcy00BYkxlKEPwLs721Te4kVbF-JiVh1AwMd43JPLv22Zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی چهل‌سرا در جنوب مصلا برای خدمت‌رسانی مراسم وداع "آقای شهید ایران"
🔹
فعالسازی تلفن ۴۰۳۰ برای اطلاع‌رسانی مراسم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/665278" target="_blank">📅 14:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d2420819.mp4?token=jUMXl_t-OPM--5xHGT-H7YWTijnRras2fEyN3EUCfXeuS6GIi3pw_ZqD88q-QgfQP0QyRrfXO-bwHgzFHB7E7SUIoKwsZmQNyy7dQr77ypr9y1BUgAk8GGxP-bCl10xrpX3yWtL25djuTwbXurSap_jDjh4xJD9ldDQWZORmBQPib-f03PC4zGuSviZgeV7FGLqqdUvgqexGL1RVgdbpDXacxMfaTnXaEsUOuWm6iN-yzrn6cfsq3qAEBM1R1rd_fA5php_ybw1DvwSQgHzwQzRP5VB906b6D9EyIIr35Hlz9tCcurDGWPyJBcCTO9Eg51_WduUh4P9rvM59rjc4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d2420819.mp4?token=jUMXl_t-OPM--5xHGT-H7YWTijnRras2fEyN3EUCfXeuS6GIi3pw_ZqD88q-QgfQP0QyRrfXO-bwHgzFHB7E7SUIoKwsZmQNyy7dQr77ypr9y1BUgAk8GGxP-bCl10xrpX3yWtL25djuTwbXurSap_jDjh4xJD9ldDQWZORmBQPib-f03PC4zGuSviZgeV7FGLqqdUvgqexGL1RVgdbpDXacxMfaTnXaEsUOuWm6iN-yzrn6cfsq3qAEBM1R1rd_fA5php_ybw1DvwSQgHzwQzRP5VB906b6D9EyIIr35Hlz9tCcurDGWPyJBcCTO9Eg51_WduUh4P9rvM59rjc4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسواسِ والدین، قاتلِ نشاطِ فرزندشان است! پدر و مادرهای وسواسی حتما باید خود را درمان کنند
/ مدار
این گفت‌وگو را به طور کامل اینجا ببینید
👇
https://aparat.com/v/jjy2nnk
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/665277" target="_blank">📅 14:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رایزنی غریب‌آبادی در قطر برای اجرای تفاهم‌نامه آتش‌بس
🔹
کاظم غریب‌آبادی، مذاکره‌کننده ایران، در دیدار با نخست‌وزیر قطر، ضمن بررسی چالش‌های اجرای یادداشت تفاهم «خاتمه جنگ» و تحولات لبنان، از تشکیل کارگروه‌های ویژه برای توافق نهایی خبر داد.
🔹
به گفته وی، زمان و مکان آغاز مذاکراتِ این کارگروه‌ها در حال رایزنی است./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665276" target="_blank">📅 14:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv5o0bRb8lYuDJ9Liviovv9Wpm2pI2GJ9zESWoHCWRRVWf4xA86AA2mFLvEarhrXUN9AC9hAJNsNk1VZWcInMkoA2va8SeZ2T443cx5mB0-8z30mshizRwLTpy-H9QsvszsxHINZ7RwA6EdRJdAhF1AvDvtGVsfnvuVvDqtZr28hdLpGw132x6nvlSXuod8XjsgEs8npW5y3CVWwcgAqX7Fahe_zmH9p9KT_OjHXER0_1ZPaCRje3hBSTYkSIR0rNNGvQLc7vx9EKfgWrhqXz1UgLajbuMsb6o3ZNDfIzoXiNaEPXrnWQh8V0RhG8V3hetLWw8QRpEdfb8p4HYs8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز یک واژه، برای فهم بهتر خبرها امروز نوبت اصطلاح «کیفرخواست» است؛ می‌دونستی یعنی چی؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/665275" target="_blank">📅 14:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXeZ0rfaLxuh1yfuWMiIkBoeqMf_Pu3l5ILaADZirt5yrJKEfmSLLDMX2TMrROfrNL7YJTQ2fOla1OojW4SnZCtDegV9HeXKLsPVt8UBHrtGTymFTK7Mztb_p2RBWfenRlWWA9CX-pRc1czRTBEOHIy-4zXL_DR_5f5GkRyhhlEP_m4sMoMtK1VAzpSYVQIxr8ltzVAE4xGQHCSzPDg0J3QDuA0MP3VmSWqdoOq_TQcRR6XroatPrzPWQsNvr_SxnlB-xoRJHDPigz_38xd7PQIOmFWOcnHTo05gdRG1fNEjLDjq7K_TfpoUUKvtXVABUFOud4FwX5nQChE5PaAKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: مراسم تشییع رهبر شهید انقلاب باید نماد وحدت و انسجام ملی باشد
🔹
رئیس‌جمهور خواستار تبدیل مراسم تشییع «رهبر شهید» به نماد وحدت ملی شد و از مردم خواست با حضور گسترده، پیام همبستگی را به جهان مخابره کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665274" target="_blank">📅 14:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_o3bmvNhrd5mVIRt6m2okJT6Z70tsxHMYIZUNsCpkuABkHMrzGGU_2VBv6TPfE487S1jGprgpOPRbcbm_AfuKWBed01Hz-QKEl6LEYE1ahSxfsBDqsHUoH1xJjG0coggSj9x0F7T9gsRkJvjmXmIFic2eszlvs4_YY7uZNFft25fBLwyctZpkOMldgACDAGwtllkTTxiD3uUus46CGWoOjuIubSaxLFw9ljWuRfkmqsbqam847IAM2TwdXxJKTN4UAfg1zJ00AVHzPEwXo7LHZ_dRYP0iu3e0HSvP1kImS8O74KU-2TuOz5doGrJ8zvyil0BN_z4WDLlxxCqTvY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ قاطع وزیرخارجه به تهدیدات گالانت: اسرائیل را سر جای خود می‌نشانیم
سیدعباس عراقچی در واکنش به اظهارات خصمانه «یوآو گالانت» علیه رهبری ایران، با تأکید بر شفافیت مفاد تفاهم‌نامه اسلام‌آباد، هشدار داد:
🔹
رئیس‌جمهور آمریکا متعهد به مهار این «جانور دست‌آموز» در تل‌آویو شده است؛ اگر آن‌ها از دستور ارباب خود سرپیچی کنند، ایران درس لازم را به آن‌ها خواهد داد و هرگونه تهدیدی با پاسخ فوری و قدرتمند مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665273" target="_blank">📅 14:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نماز آیت‌ الله العظمی سید محمدرضا موسوی گلپایگانی بر پیکر مطهر امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/665272" target="_blank">📅 14:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665271">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
پیکر داماد رهبر شهید انقلاب روز جمعه تشییع می‌شود
🔹
مراسم وداع با پیکر مطهر شهید مصباح الهدی باقری کنی، داماد رهبر مجاهد شهید آیت‌الله سیدعلی خامنه‌ای، روز جمعه ۱۲ تیر از ساعت ۱۷ با حرکت از میدان دوم شهران به سمت پل شهید احمد کاشانی برگزار می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/665271" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZBC5LfyOj-UV5FYcOYC1JWXNcnVj3AUAbNdm6iR_rTsWUyvBlXkThU7BmlAgduDcK9ePcuwG0Zjpy7WfnJZSxD0R1-TRZOGIQIizardS6Hv3c75HuN4ZrjOjYgfQVIY61o8MhuRWRTEveQ08HjySygbYPEJLMBU4D4SNp4DHm_d30cTmTDnYUc5CrpMpkq3Wm2pyaF8CbJzD43toqD6P2AsJtvXatCZTkzZhkB-u3VXQSPuP70PT2u0bm19IrYXQLW-RBPFKZ7nxcI_MNv9fckx32AewScVzdyWvjiF_pZdx3sWmwQEin7gzs1noTdSYymEJH5SSGewDsdJdZbpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی جهانگیری، رئیس گروه مالی گردشگری، به مناسبت فرارسیدن روز صنعت و معدن پیامی صادر کرد. در این پیام آمده است:
«صنعت و معدن، ستون‌های استوار توسعه اقتصادی، خوداتکایی و پیشرفت هر کشور هستند و شکوفایی این دو حوزه، مرهون همت، دانش و تلاش خستگی‌ناپذیر انسان‌هایی است که با نوآوری، مسئولیت‌پذیری و روحیه جهادی، مسیر آبادانی و آینده‌سازی را هموار می‌کنند.
فرارسیدن روز صنعت و معدن را به تمامی صنعتگران، معدنکاران، مهندسان، کارآفرینان، مدیران، متخصصان و کارگران پرتلاش این عرصه تبریک و تهنیت عرض می‌کنم و از نقش ارزشمند آنان در خلق ثروت، توسعه پایدار، اشتغال‌آفرینی و تقویت بنیان‌های اقتصادی کشور صمیمانه قدردانی می‌نمایم.
امید است با اتکا به سرمایه انسانی، دانش، فناوری و نوآوری، شاهد شکوفایی روزافزون صنعت و معدن، افزایش توان رقابتی و دستیابی به افق‌های روشن‌تر برای ایران عزیز باشیم.انشالله»
گفتنی است گروه مالی گردشگری با حضور در ۱۱ حوزه اقتصادی و ایجاد بیش از ۴۵ هزار فرصت شغلی، در مسیر سرمایه‌گذاری، تولید، توسعه زیرساخت‌ها و خلق ارزش برای اقتصاد کشور گام برداشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/665269" target="_blank">📅 14:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5969f713.mp4?token=RtHPzx6cIkQv-3gcvfxIYw51YwIZpBXE_zVx1qlkAv-Yr3qv37esrg81XqdhvXFmG9p6EIxXD8acuKmyq-HTon8NECWkX10X0Pqdm8QM3hzSqNI3_8Un8zwKIsnvLPjrAZ2yy5DIxDJFvZnLWaW5le_8E63RyK3TFbUKnyJVrs2Mjpn240jah9jd8KGcd4BZvL7lw_jv19aF-aFrsNUCy4LraB4XQN6PykAH27xAWAjB8QM5bLC6f6zeJcFqIylFkDQU1--V46qz6UyrSs9qayOHNSNbz79FW97Ew8H41l5JRSb26RZAiO5p0LbANDanY_y3IOlyv1FxHdEemrYmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5969f713.mp4?token=RtHPzx6cIkQv-3gcvfxIYw51YwIZpBXE_zVx1qlkAv-Yr3qv37esrg81XqdhvXFmG9p6EIxXD8acuKmyq-HTon8NECWkX10X0Pqdm8QM3hzSqNI3_8Un8zwKIsnvLPjrAZ2yy5DIxDJFvZnLWaW5le_8E63RyK3TFbUKnyJVrs2Mjpn240jah9jd8KGcd4BZvL7lw_jv19aF-aFrsNUCy4LraB4XQN6PykAH27xAWAjB8QM5bLC6f6zeJcFqIylFkDQU1--V46qz6UyrSs9qayOHNSNbz79FW97Ew8H41l5JRSb26RZAiO5p0LbANDanY_y3IOlyv1FxHdEemrYmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان عجیب ازدواج و جدایی محسن مسلمان؛ ۲تا خونه و ۱۱۴سکه در سال ۹۶ دادم رفت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665267" target="_blank">📅 13:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f147454758.mp4?token=SKatDpfC9UwpcPlN2GYtbgNoB9h6eTJ-yVmM6ER6rbTe2Q83V1MAGE-9JnuTuV9hvet7NMjyOUT7woAkljGYYO103KP14oyfZb-g28Ce9uwJBmZWj3TyVwL5HU2iWUUBEqCa2KBfryM4IDkmYK4Gev4e8bXVE4ccx104CTz21Uv0FeppTdHEFGe5vBQT9Uu6hnu__UFN-CjpyymQ9kZBJ5ZaSdHuF_LXhCFhcEw-rIkdiZ8LTEDdX2cAOEDezn8qOEbljuZ8h5SE-_CZYtp2IlFnpfN0unsv4Mt33sP_1Jwu-n_Ebt1uPwAhhtjdC_Ue-en6GrgV-PpkKz0Uv212Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f147454758.mp4?token=SKatDpfC9UwpcPlN2GYtbgNoB9h6eTJ-yVmM6ER6rbTe2Q83V1MAGE-9JnuTuV9hvet7NMjyOUT7woAkljGYYO103KP14oyfZb-g28Ce9uwJBmZWj3TyVwL5HU2iWUUBEqCa2KBfryM4IDkmYK4Gev4e8bXVE4ccx104CTz21Uv0FeppTdHEFGe5vBQT9Uu6hnu__UFN-CjpyymQ9kZBJ5ZaSdHuF_LXhCFhcEw-rIkdiZ8LTEDdX2cAOEDezn8qOEbljuZ8h5SE-_CZYtp2IlFnpfN0unsv4Mt33sP_1Jwu-n_Ebt1uPwAhhtjdC_Ue-en6GrgV-PpkKz0Uv212Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر آمریکا در فلسطین اشغالی: خداوند ۳۸۰۰ سال پیش تصمیم گرفت که اورشلیم پایتخت اسرائیل باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665266" target="_blank">📅 13:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe9a027b9.mp4?token=kk9PwjwaeVWn5p_NijlfXvnBefd_s6veL9jvcg3HhPNJAQ1uI2RVtlQyvnF2hu65E1NKY-VdJORlASFmR28Xp47R9ADcKVS857zSoFI43iXNCNcHYpldEaCBawHRnlzCnwwl0icTrCPh-nje7VbjsTJybZuCUJG7F4Gl3dtWsQmUOKKY0M2z1hN3ksAgs5e86Ro5qMIReeNQAlnvcgwqjMrDA6YhpsL-1tzDwbIb2HpMrxPylaFuP1RLs1eDiqZ640aP8NxSpdXrHLuAMV0cuNR_LnvlHa8jGLngTUKZnyw6RZAm2RUbDKPfr8OIx_kQrNJ39by6ws8MiUlMDVSyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe9a027b9.mp4?token=kk9PwjwaeVWn5p_NijlfXvnBefd_s6veL9jvcg3HhPNJAQ1uI2RVtlQyvnF2hu65E1NKY-VdJORlASFmR28Xp47R9ADcKVS857zSoFI43iXNCNcHYpldEaCBawHRnlzCnwwl0icTrCPh-nje7VbjsTJybZuCUJG7F4Gl3dtWsQmUOKKY0M2z1hN3ksAgs5e86Ro5qMIReeNQAlnvcgwqjMrDA6YhpsL-1tzDwbIb2HpMrxPylaFuP1RLs1eDiqZ640aP8NxSpdXrHLuAMV0cuNR_LnvlHa8jGLngTUKZnyw6RZAm2RUbDKPfr8OIx_kQrNJ39by6ws8MiUlMDVSyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قتل نوجوان ۱۴ ساله فلسطینی توسط ارتش تروریستی رژیم صهیونسیتی در کرانه باختری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665265" target="_blank">📅 13:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTxvKgQHRyxklfZZz3jacNhv8BviG_8bLobZdPmUi7y23cM2aCoJLoPBU4igH1pyHRhDulmCtc6JprFrGNGtPa23gPVnJkD360UThLie_uUx86LgT1wCFNQortH46PhzGio8pW_xdWe64hptTesPRkHMKate-XgI9A1no8XH9vQ6EcHWJNVjG3Y1mSJxubp3ZNKN5r3baq3Gz_DgPb635nlrrWtLS06CTYHHLIzkMQ5HvESEBcO-UqKtDoNmu-QyNMnjr0N9cf7A1Z_u1QcC3U3if-i6_aX0WPv8_abmuXynq3bqwd5gY1-VQcENW2s__S1FbT7Q9I1BsSoPo7ou-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین بازی‌های جهان/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/665264" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8NK5vTCJRbEv9HjLkXQfXC8cmhZSnuYei7slFllD6YtYV5-RUzyHLmr4Qb7blAQDXsHI5QVB-paLHw6YW_hBidreSRwuCq_ChMe9wyRPyKnj3ogR97sQksyNwnGoSCS732ebX0q2elyvkMGIGeELwgKDEU21gAeDr197e9ry6Uur-IyMoiF1uMwrH0LqFxmptfnfAJ2W6rX9c2PQj3czLv1hrCvQllG06rSaTNZ7XTLI5VEcYQKOsA-wWpwO38XMKxB-q_Y7aInXRrg-0JhbnaToxQXvITrT5Xcmg4DMjMll4yMvcYMTywSYnS99nzgToGrM3Vy0lFArBDDAL06bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت نفت اسیر جنگ روانی نخواهد شد/ وزیر نفت مجدانه در حال انجام وظیفه است
📍
سامان قدوسی، مدیرکل روابط‌عمومی و سخنگوی وزارت نفت در اکس نوشت:
🔹
جای بسی تأسف است در روزهایی که ⁧وزیر نفت⁩ مجدانه در حال انجام وظایف و تعهدات خطیر تعریف‌شده ⁧وزارت نفت⁩ برای خدمت به مردم شریف ایران است، عده‌ای معلوم‌الحال با شایعه‌سازی به‌دنبال اجرای نقشه‌های نخ‌نمای خود هستند؛ وزارت نفت اسیر جنگ روانی نخواهد شد.</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/665263" target="_blank">📅 13:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d177a891d9.mp4?token=dhr93xo6SxF_HRzEs8KJxxqfq87w7nym1bWrr8M63rAiUDfjddt8LlEvmMoniCp0_YUBdA-IUUt5iY4QZhpxHTPx2tiZIelFQB9hjRMwsrqg4LVnJ6eZNZ-c-cn1C_8It4S_9Ui3P2R0-9fHG-NEQ4jJTPu2q5R5-9Raz-sp-d-5XMo0mbDGQVo68ls9mzhs5NsgCgRDEKFTP516K9xFb4J34Ah8sUUJyqooapKQYMcwCHl14glafCYZXT9GqvtorMIzE96FYO9dSP-rhwmFMn3Jl1lyX-7513tae4P2b2PbVprDMP9KQPDY1CMwaePibgEbB1xz9iOaV5xb99cZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d177a891d9.mp4?token=dhr93xo6SxF_HRzEs8KJxxqfq87w7nym1bWrr8M63rAiUDfjddt8LlEvmMoniCp0_YUBdA-IUUt5iY4QZhpxHTPx2tiZIelFQB9hjRMwsrqg4LVnJ6eZNZ-c-cn1C_8It4S_9Ui3P2R0-9fHG-NEQ4jJTPu2q5R5-9Raz-sp-d-5XMo0mbDGQVo68ls9mzhs5NsgCgRDEKFTP516K9xFb4J34Ah8sUUJyqooapKQYMcwCHl14glafCYZXT9GqvtorMIzE96FYO9dSP-rhwmFMn3Jl1lyX-7513tae4P2b2PbVprDMP9KQPDY1CMwaePibgEbB1xz9iOaV5xb99cZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲٠۲۶ #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665262" target="_blank">📅 13:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YInJEe_PILdJpwrkRIWby8P0FaxNzcEtmeZiQgMkztsqlsSp5AsgBMebgFQLtCEo8Ld0dT8WjBrN6jkoykUQPVwKBVeGdzRaCvHTFRmrHuCVhQo8se7U2580rzVvpQitYbZIJ0NOD4YSAt3PEWyPgYhE5Z2-tdATyyN1bO6uW1ZBSgzhO-eCHKXm-BH6hg_ChDaomaEXBtY1mfGv4UYEEykXodwERT8PfPG40xmRSTxvadWwPDqJxQBSxtfi18veT44H1EksHSfsHyF0lP2ylUrOllQPjxDhuDe7ASjfl2pW8EqHYpzCSYqZ4E3NMIVqtGSxZIluteBXWKAE5VFKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
علاقه‌مندان به بخش
گزارش ویدئویی
سوگواره «بدرقه یار» می‌توانند پس از مطالعه آیین‌نامه، آثار خود را از طریق لینک زیر ثبت و ارسال کنند. در صورت عدم امکان ثبت از طریق سامانه، ارسال آثار به شناسه رسمی دبیرخانه نیز امکان‌پذیر است.
#بدرقه_یار
▪️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
▪️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/665261" target="_blank">📅 13:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbdhRGrXb7PJG4bjmmP83YZTNJ2HJxColOwlw3urXdcN5ejH76WOvzRTW4Lk_rGGEUk4pEVZ13lnxjI9vvCvAddcBcYAN0rSLu_MBFdxBlAlCq3KJuuLxzGwNGs3jbYFKPjxlvpzwicRrh8Ga6VNfxHpJWRNgCJSJIHha7mjkXANcBj8Fhi5oqBax0d8praZQJrLTx1HaypYvihNwmk-FL9fxP-R3V4-0JXxbhC9-byC2Uf6AL59VFmRZRqgnfoMDwFfVbDpBLrhjtwfLMuahNlC41RNkFxYriD9MBSxZEKM4QYbVOvo0ckU_Pjfg4inAM8MRgt4u1-s_po9xcMAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تعطیلی استان‌ها برای مراسم تشییع «رهبر شهید انقلاب»
🔹
بر اساس بخشنامه سازمان اداری و استخدامی، استان‌های تهران (۱۳، ۱۴ و ۱۶ تیر)، قم (۱۶ تیر) و خراسان رضوی (۱۸ تیر) و همچنین سراسر کشور (۱۵ تیر) به منظور تسهیل حضور عزاداران در مراسم تشییع پیکر مطهر رهبر شهید، تعطیل اعلام شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665260" target="_blank">📅 13:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
معافیت تحریم نفتی فقط برای فروش‌های جدید است؛ مبالغ قبلی را آزاد نمی‌کند
علی مسعودیان، پژوهشگر دکترای حقوق بین‌الملل:
🔹
با توجه به موقتی بودن مجوز ایران، باید در قراردادها، سازوکار‌هایی برای دریافت قطعی پول و جلوگیری از اختلافات بعدی پیش‌بینی کند.
🔹
اگر قرارداد در دوره اعتبار مجوز امضا شود، اما موعد تحویل نفت یا پرداخت، بعد از پایان آن باشد، ممکن است دوباره با محدودیت تحریمی روبه‌رو شود./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/665258" target="_blank">📅 13:07 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
