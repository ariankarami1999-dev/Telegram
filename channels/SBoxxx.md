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
<img src="https://cdn4.telesco.pe/file/nFutMZfjMrMT3yVCbXjtQ-e2zPnVYKJKXiy9tVp4mU3NybvMEWqBlNE7-N6ZgEOHYYoeSfjKUAUVA7EeCNzDhXbkLiD_hSqnRIrdFTexqbB772YkSS4C0QSFF4zbt7IcUwCuK3H0QFwuuHfI97nURvzHwe3Ci2u4KLwJmOQUsgd714ZYD9FdVkmQZiLfTphEDtMqBYOm3xNINCtEQ2e5wazvoNxe4qeBgK7W6XFM-zKvIm3HVIitroARjIzFDhNqUKStTIKD_aj7J9apa1K1zIAVjEOsKJDypKpgaXzIW_-peq5FgsP3Y8Z8wA_p4lKGo0nGEntvDR4oob9swOjMCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاخ سفید برای یک درگیری بالقوه طولانی‌مدت با ایران بر سر تنگه هرمز آماده می‌شود.
مسئولان آمریکایی می‌گویند مدت زمان این درگیری به اقدامات بعدی تهران بستگی دارد.</div>
<div class="tg-footer">👁️ 550 · <a href="https://t.me/SBoxxx/18415" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evDRaL6YMF8BDKZH4TfLYYo2waffHQPs3rGyPmt9usAxemClT5FTkAzScK-13aePL65GZVCZoLjJ-ceGidTAEMS6u70E5YOGR0mSelfELTrgj2u8abVvKKa4L9i4hoWpPQkP6bnfsHyR_1AxrI6CP5YcyRejk3r_nllR8mrVoDstvBd2z9ywx1lZtOmP0pT42slD8USXRtp6HxFWQXHwFWuZSdjHSKqGTk-M-gA5nFa9B_16eI1ScP95ofJRhl6RbnxUAlKo50MH9G2FTqNvZMMeMZWJe93JA3gIxS4xDK7xabdKfi1y_4ABIRjl09xu4i_O-M2hUgYsnH79Tx2klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/SBoxxx/18414" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:   به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.  برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از…</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/SBoxxx/18413" target="_blank">📅 08:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:
به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز
به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده ای به مشهد مقدس انجام شده است.</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SBoxxx/18412" target="_blank">📅 08:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/18411" target="_blank">📅 08:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB7bbognf6xURrqADtQgnD2TjMmApsKW9ky2XvU1dy0d67TGAEpCpYOzdC5siEsZyXruhCAX-keRtQeFpN73ZTmyuslZ-3wwG_os80DDuPdZPpuHo8SK5eHpifZLetTQwkzFNTi5XSG-_mBfoGSAymjfO2lprKS6rPLRsNlYdsvlxVzD7ziUD170kpQtfasSN2J730LxXrZG9lreVxbVYeP0xwzYmDel9y2Mb1RQv4MzVc149vGw7komq-VmlPRwHnzirKdqH4SFhE4xo1k72rfE_W8AZtqYJNxo5CEeVoNKxlq8goAeEngzcd95HSnUqo0m9N1B4aF6tHddXvFY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/18410" target="_blank">📅 08:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/18409" target="_blank">📅 08:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع‌شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید سرزمین عراق حبیب، مستکبران کاخ‌نشین را وحشت‌زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد‌شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی‌پاسخ نخواهند گذاشت.
در اولین مرحله از پاسخ تنبیهی علیه پیمان‌شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/18408" target="_blank">📅 08:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/18406" target="_blank">📅 02:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHwSa35R1iTWwF9F3SSxB5gt9VJZq_B8fZ4qIwdekNHq5Xy-_JQdNh5ZS0rRQL1bzneGO33vRXK4_b1VmNI8UV5LwVpdzV4erMoP6BsgvPRsGWyYZY56umeLpHO9bhIqsmFtEVJ67fUCfaJ4fDqDRhS2bBheT819Px_POEcuPZV5u9FOXT_aRGy0Yoe9O3TyxOYPigtchwxLlsZyTR9MTS1j1eBCu_jw7NVW20Dflcz7OnasJs_gZRcHYYDtAwrPlGwdqSooy-cCxsR5tLSc_kgFBZcGkOi-L50SMVwxZX9d6WsWeeI0q88MO9fobGr59UTYRezbpsStMnakx0qB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال انتشار زنده ویدئوهایی از حملات آمریکا به ایران در امشب است</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/18405" target="_blank">📅 01:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18404" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">زاهدان</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18403" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ابوموسی</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18402" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تماس شبکه خبر با اژدهای بندر!</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18401" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY-EKRkCU7VXp1emmvZvEr-q4xBeoo_oTW-wmElGIySBGXxd8_aTxDq7HVRzYQ2DXoeQP1pFataR4ioWUbCojq5GGxy_4yadtKAldjWn_xnXvLAtszlsDfLvnMw8wD_02v_qwoXCByFJzcV9wNjNUcrqkRo0rls4BKBs_3l0FJWG9ZXTB2uYaaeF_W2e1rIV1-NhimQJtng2jMmCFRbYGQTFqV3Uii_mVrY1OGrlZ4sv8yrhTMXMid5s81BnHSNuB4uVPWv-oT_zD7ndusgjD4k5cSWZyI7vXqkAt8RYq3Z3WjAva9wrw4fJsUWsvylUvi9STx9_uXJr5xzt3uHNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18400" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گفته می شود تا 200 هدف امشب مورد اصابت موشک ها و بمب های آمریکایی ها قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18399" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انتشار اخباری از آماده شدن پرتابگرهای موشکی سپاه</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18398" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خارک، قشم</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18397" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تسنیم:
براساس برخی اخبار غیررسمی، پایگاه امام علی نیروی دریایی سپاه در چابهار توسط جنگنده‌های آمریکایی مورد هدف قرار گرفته</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18396" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عربستان سعودی در حال پیشبرد طرحی برای کنار زدن اسرائیل از کریدور اقتصادی هند-خاورمیانه-اروپا، معروف به پروژه «راه‌آهن صلح»، با تغییر مسیر این کریدور از طریق سوریه به جای اسرائیل است.
دو منبع به نقل از جروزالم پست</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18395" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18394" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18393" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ-ELBpxpcfVpXWU23wWqrmtcOZ14iOtyEYFkwZ-cL3RBGQgU2OByut2cVLtWHFIGmhCymVI1OZebCBvc338sYkx2ZrfT8ZQkhJC-fvjMfzAfZ9R9UA06dlSwF0ut-7fSCKe2aguHz-UFVvIt30tLoEmLqLAPNOdh3vdstnQf_h9Y-rZvvlLIwPNBD_fNZalDtAW4rTTwqByIn-DziGQiPKbD87L1rIDpTE_FBwig3iah7B5Nlr9p9XFeSBleVYgmhXCtnD6dIQ1fCo6ZD0iSN5Yzu-veUAj0xXAbIlsfgFM1BywsfD68Yk9T757FY1iCUyNtTnDCGiZ3ZcrZcZ14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار ه زده شد و برق قسمتهایی از شهر قطع شده.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18392" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18391">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حمله به پالایشگاه ها هم آغاز شد...</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18391" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18390">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله به پالایشگاه ها هم آغاز شد...</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18390" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18389">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بوشهر، لاوان، چابهار….</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18389" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18388">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18388" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18387">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">At the direction of the Commander in Chief, U.S. Central Command forces have started conducting additional strikes against Iran to further degrade their ability to threaten freedom of navigation in the Strait of Hormuz. The United States is holding Iran accountable…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18387" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18386">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At the direction of the Commander in Chief, U.S. Central Command forces have started conducting additional strikes against Iran to further degrade their ability to threaten freedom of navigation in the Strait of Hormuz. The United States is holding Iran accountable for recent unjustified aggression against commercial shipping and civilian crews freely navigating a vital international waterway.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18386" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18385">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری را به ایران انجام خواهد داد.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18385" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18384">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18384" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18383" target="_blank">📅 22:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در ساعات اخیر، ایالات متحده شروع به استقرار مجدد هواپیماهای تانکر سوخت‌رسان در اسرائیل و خاورمیانه کرده است.
— خبرگزاری اسرائیل</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18382" target="_blank">📅 20:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:    با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد   کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ،…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18381" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:
با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ، از توهین به ملت ایران تا تهدید به حملات بیشتر، نه نشانه اقتدار، بلکه اعتراف به شکست سیاستی است که سال ها بر زور، تحریم و تهدید بنا شده و نتوانست ملت ایران را به زانو درآورد. با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می فهمد!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18380" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:  اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.  اما او در آن جنگ دخالت نکرد.  او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18379" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.
اما او در آن جنگ دخالت نکرد.
او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18378" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  به نظر من، جنگ با ایران دوباره آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18377" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18376" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18375" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18374" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18373" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ درباره ایران:
می‌دانید؟ ممکن است من کشته بشوم.
من هدف شماره یک آن‌ها هستم.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18372" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18371" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18370" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ در آنکارا:
شرکت‌های لاکهید و راین‌متال از همکاری خود برای ساخت سامانه‌های موشکی تاکتیکی ارتش خبر دادند.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18369" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18368" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -
تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18367" target="_blank">📅 19:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.  سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18366" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-GlLmQGadCH3EJIEQ5caeo6qQFvUZnY4dXwrALCPiy0I2p3RMmlHCD97n9Lir5Y885KiD7XiFD6ADLiaOKur8h3jPdIi3qZVWvqN7_a80fPfkqRxLRC58IFKaShUUVrzKfICEzxcfMFkT8okCfJmxJlwmf7sRVfbHD1bsmHqzh96y2t8o8bfueosn0rq4sC-JxoO9nkb86S-M0ZZa5S22EXXmgPhCA1wly6LTCbMJRN8vuZzl968i3nI2Jb2bg7aUwgSXEZNrQDF_RuzmIhDdmcTBcdBjI3JJm_pUIIdHkcDh3TXIC1GmlVrp8fyL-EEODq_-2Bm6orJA-f1mpjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.
سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم امیرحسین قاسمی، استواردوم علیرضا زارعی ثانی و استواردوم علیرضا بالیده از پایگاه شهید عبدالکریمی بندرعباس و ناواستواردوم شهاب امیدی بزی و ناوی محمدجواد روانفر از منطقه یکم نیروی دریایی ارتش، در این حملات، به مقام شهادت نایل آمدند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18365" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.»</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18364" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-pQ3hw4mypInPwTHjSmMpPSPgAlFH9Gomh1GQb5vTqnnuWvcJsIQW7uTriFzZc_MAfXb704EhvRIfOOqy2OzatCdad0z0SxOKwZxTIAItwLLscQu2VQsg35RVNlP7ws1-zeUBUGywbR1EJ6O1NdKpq84GuO_FdZxh7ye6i4xvxjZhPSAIm_F7v9XazA2coDqZVMWS4IkbDTzodbEozVE23FF27TU25kh3QuTaWH4wtJid28YRyTdAq_qQ-xYSf096d10y8RiBQBBr5fyr9dx5dzX84xcrgdFByu54kv_7xVLXXd47dfHeni-BmE3TN2XQIBlP_iHrBnLuEdvVCczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18363" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKe6xSuIhVWQa05pQ85bCF9bDbJXm1lew21UDb3rW9KWGRlISzWRvSoRlvt4tfJDCBVNVZrggEeC0sHJ8G3hwM5Rld494OPzj-VZxx6WsbKjTFLcTusW0P1sIZqvdmxC1sXzCP8gthpUYd1iGpLfDi_8NAX4u2UtDGAfldXpFmByqUFaCdTLtb2RtNXYvY5E3RVafJWpzElFvcQypXS2ypPmWWFFLHPR10h7cUre-lU1M_D9Znmnn49f2iiaOw24yg9cbVEkRRQ9gjEmBesV0PnhuOuB8wA6BLp3zYTN9TU2BQY6_SNXxy6ZEMEQFFGIJ9jTjGtQudrPvvsT7aUeew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/18362" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏یک مقام امنیتی بسیار بلندپایه اسرائیلی دقایقی پیش در مصاحبه‌ای اعلام کرد:
«دور بعدی تقابل با ایران، آخرین دور خواهد بود. ما از ابزارهایی استفاده خواهیم کرد که تا به امروز به کار نگرفته‌ایم؛ موضوعی که حکومت ایران برای بقا در برابر آن با دشواری جدی روبرو خواهد شد.»</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18361" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">— دونالد ترامپ:
«به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/18360" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18359">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18359" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18358">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ فکر می‌کند اسپانیا عضوی از BRICS است !  در دوره دوم ترامپ، مشاوران و نزدیکان ترامپ قطعا نقش برجسته تری خواهندداشت.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18358" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
جمهوری‌ اسلامی ژاپن دیشب ۱۱ تا موشک به سمت ناو هواپیمابر ما شلیک کرد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18357" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در مورد ایران:
احتمالاً امشب دوباره به شدت به آن‌ها ضربه خواهم زد.
به آن‌ها یک اخطار کوچک می‌دهم.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18356" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18355">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیروزی های ارتش طفرنمون روس ادامه دارد…
اوکراین می‌گوید امروز یک جنگنده سوخو-۳۵ روسی را در جبهه شرقی سرنگون کرد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18355" target="_blank">📅 16:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18354">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=iWY0LaqpumsiCXWPvqMbrvC5F37TQzmDQ2ren8T2Up21Hd7LEMqgN9-_N5JdZHHRZ9TKHEaLhfOMtRUxXurfvj3N37tCxycM5iyURv62MgYULXTQG07JWV_clPqn7UPXbqnub8zFv6syMtAtF4eEW--N7e5DcC_20CTN1TjziWjlzNQAszpzQp-LtVlG8uUNQG45UeVmrDdw2Nx0XzIGbIbM4p9oSc_hZ_Tq-1dUSaTeviHyhR3mIfKkjd39xfB5OOrLDXpNCK7qTEjT2SiTJELaSWpTfzevQC75P-zl5ED3wrKEgD79CMf8e3VcRnhVKoUxop0nYMtCgfNsbkN5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=iWY0LaqpumsiCXWPvqMbrvC5F37TQzmDQ2ren8T2Up21Hd7LEMqgN9-_N5JdZHHRZ9TKHEaLhfOMtRUxXurfvj3N37tCxycM5iyURv62MgYULXTQG07JWV_clPqn7UPXbqnub8zFv6syMtAtF4eEW--N7e5DcC_20CTN1TjziWjlzNQAszpzQp-LtVlG8uUNQG45UeVmrDdw2Nx0XzIGbIbM4p9oSc_hZ_Tq-1dUSaTeviHyhR3mIfKkjd39xfB5OOrLDXpNCK7qTEjT2SiTJELaSWpTfzevQC75P-zl5ED3wrKEgD79CMf8e3VcRnhVKoUxop0nYMtCgfNsbkN5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بح بح!  موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18354" target="_blank">📅 14:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18353">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">باور کنید برخی هستند که  مطمئناً این چرندیات امثال شریعتمداری و رسایی را ترجمه می کنند برای ترامپ می فرستند.  شریعتمداری و رسایی اگر هدفشان ترور ترامپ است چرا خودشان اقدام نمی کنند؟!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18353" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18352">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hicqt8WlphXIoST9utFUGLHB-2pwNxzqcncOntg7fiEcn2kIXY0ReU-lr6SEWCCoizj1pLw6DKa65SFcYa5UY0A_eDhoR-k0DWUpINaEfYpqp9dFQMVw3laO8Khd7w1ApE9dy5bfBh3S0oRIyIhqfmnErhVd9dMqPeZw_QpI8ac3KUHehJpz9JFpgewg1wbQHCzfrh_ml-GZZvd6emJE3hgqArbZXeDG7CBYF-BjViT_4wBLqHkfraAHAQvqsbAaN0BnaAT-F4owiAXzpkjZcDOUH-4n-W_q0tBxfgDtoe-CW_odVoql_b-BzqJ4T8_dLNOmbLKPQcdhub0AU7TQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18352" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تا این لحظه،
هیچ منبع معتبری
(از جمله رویترز) خبری درباره
هدف قرار گرفتن نفتکش آمریکایی شورون (Chevron) در دریای سیاه
منتشر نکرده است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18351" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkAMyCzjoC7-1j8tGd3oG3hj70MM_Y96dYRQXAvBhrnt4_bhFXA2lNx9wTr-vGYeEXhJRwOzfBUhHngbY0MNPufBwdnFc5YWkJuA9LAkQYQO0oCU0yVAgmukQcl-Yy4mGy_vtsNLz4Xz1sZF99PtONe_dDEoQ1h7CeqCry4gST6qzbhl15y3ID9ivNMWLZG_OsRiLPHggXvo9uR-GbXxkW8SZotZpo77a7K2C9P2a8UkSt98ayvcOwV-RA8KEZpI5uh5NFbOjfcklDA68_uoi7T1AdH1K1anjh4D9MhjTKAw2KVUkRYR_JwhWZepGBGXAQxIowF8EQ0gCODAJrlohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18350" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18349" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=m9m0TqsOkKZJdDXsTNNfVSptlELNOrGQp2LIL8TaaMR9B5rIF6jjL0NWL4htpav46eL2aIqF8cE9U6oYwQ0bKeg3HPjMYKasDB9fFvVY60jfbuPCecLJTT9wKEaiKpZkspY5pQjAZZjpll8c3zjb94dLLFG0E3Q4mAkFf9pNsuLW5An6XRRLCiJGXA7F9bscBsI04-mtuyHvMKd64aNwoF5AhikErnty86VtBglw94R67lDsGCMLo3Gd3GVGQ6tvISrt-1V_OFOy5RQhUkLbm3DEXB1zy22V8K-K8hrV2N_cDDKeownZrXI4BF1u39kmHwtuyCszcIzbQq71zzmdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=m9m0TqsOkKZJdDXsTNNfVSptlELNOrGQp2LIL8TaaMR9B5rIF6jjL0NWL4htpav46eL2aIqF8cE9U6oYwQ0bKeg3HPjMYKasDB9fFvVY60jfbuPCecLJTT9wKEaiKpZkspY5pQjAZZjpll8c3zjb94dLLFG0E3Q4mAkFf9pNsuLW5An6XRRLCiJGXA7F9bscBsI04-mtuyHvMKd64aNwoF5AhikErnty86VtBglw94R67lDsGCMLo3Gd3GVGQ6tvISrt-1V_OFOy5RQhUkLbm3DEXB1zy22V8K-K8hrV2N_cDDKeownZrXI4BF1u39kmHwtuyCszcIzbQq71zzmdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18348" target="_blank">📅 14:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عراقچی را در ایران فحش می دادند در عراق بشدت بزرگ داشتند!
فکر کنم عراقی ها چون دیده اند فامیلش عراقچی است فکر کرده اند ولی خب.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18347" target="_blank">📅 13:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:
«ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18346" target="_blank">📅 13:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان درباره تن ماهی پرسیده بودند؛
به نظرم زود است و می توانید از مرداد هر هفته پله ای بخرید.
تصور می کنم هنوز ذخایر نفتی آمریکا پر نشده و انبارهای مهماتشان هم.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18345" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فوری | اردوغان: موضع قاطع ترامپ در مورد تلاش‌ها برای دستیابی به توافق با ایران قابل تحسین است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18344" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ :   تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18343" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-J-DikYGkg_RaOy1--wz9AR_wY_SShHw-ZB2R7KTlxDl9kOSUOJPZOdoMCq5cMOldgKw5CJee8umiT7AJ03jS3BcIArDAG30xJyoJ5m3-zrixPzqe6rUBh3Hf1tn6XSHyv9QV594wSSwfSr03anIguPUpRKp38x-jy-Z8TZm9NNIQKSbztoP9D-pwi3iIYWzz4QQCgPzF4nPDK92SKCkGAwRWAUHKlYrJ8bMDkiUj0ASQYIK0URYH95djE1vg7KRr1YZS3QGn0voWjr7wO_4TdVBZJIW5wbz-WiRQseeI4pm0ZC783yB8PgKVuXp3f4YOYnf91IH-aJzWTNAIaQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولانی به آنکارا، ترکیه، سفر کرد تا در اجلاس 36ام ناتو شرکت کند.  قرار است او با ترامپ دیدار کند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18342" target="_blank">📅 12:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18341" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2gB4dTBWviACdflOL0BIUs2P8fBN-15j3WOD-pzuPQ31zr6BkAPWNmPkkWmBvplS_T8V0BTBEvAJdXtHAQGi0FSm124-bl7RoLVIoTM0DdiEfjcpQ-6JrCH8KLfXwtqH_LluFvkRP-jq6Bpe6jsWZSVTKvjkAg1aAoof3Tpi0oZ0TTD4f4ENKQrN2tkYlDLHxbwkyX0G8oHUjNt-R2Cn3C7uJLADWq36XwGKTCBMh9rkDnm8c0oBWcxxDpMbcBziA6cjIo3xqM1nyKfvs8icvNYwVqluBy5OijqMO2VGIXqjw0FH_1EFlis24E_rjN7rg5gkMW39lI2uVwEssp_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پهپاد آمریکایی توسط پدافند ایران سرنگون شد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18340" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقتی در اجلاس ناتو در ترکیه این چنین صحبت می‌کند یعنی یا به من کمک میکنید یا گور پدر همه تان !</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18339" target="_blank">📅 12:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ:   با اسپانیا حتی صحبت نکنید. آنها کاملاً ناامیدکننده هستند.  آنها آدم‌های بدی هستند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18338" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18337" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18336" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18335" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deA6bddeCwhiEyon2edDbmXGklVmO4dG1rkGYZ4-3iKOHOAED_7CP-joudb1562xtW5pRs8IQo8fkDWr8Ye4uU5E3afBJ5syC0Dor-ynYoCXF3d7ChuMjSlqZtWrWLxPn0ql6gCYgMBqvauMKio3v5soCr8GIAUQiYvztK9_kcVdCCTqn09Upz_OEOygEiNB8snGcbzN-QjXi4pSNFKW-yH4cUO1KAPAtFa7x3b7QTf4JDceE_vtqWmmaIWb8ofsQEYH6tpUACDXU33apSQqMjZmwuMmwDiXQrGk0H-LsYgAnT3aBOd4AcJSJo-qy6ScWjq8N8zi2sCFHRtnI1_RlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18334" target="_blank">📅 12:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره اردوغان:
به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
اردوغان شخصاً فردی عاقل است، و به نظر می‌رسد که ایرانی‌ها رفتارهای غیرمنطقی از خود نشان می‌دهند.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18333" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:  آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.  شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18332" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اظهارات کامل ترامپ درباره رهبران ایران:
آنها دروغگو هستند، فریبکار هستند و آدم‌های بیمارند. آنها به مردم خود آسیب رسانده‌اند. تا به امروز، ۵۴۰۰۰ نفر را که در حال اعتراض بودند، کشته‌اند.
شما می‌دانید که وقتی مردم می‌پرسند چرا هنوز قدرت را به دست نگرفته‌اند؟ چون آنها نمی‌توانند قدرت را به دست بگیرند، زیرا کشته شده‌اند.
آنها آنها را کشتند. هیچ‌کس نمی‌تواند قدرت را به دست بگیرد، زیرا آنها سلاحی ندارند، در حالی که طرف مقابل مسلسل دارد. و سپس آنها به کشتار ادامه می‌دهند. رسانه‌ها این موضوع را پوشش نمی‌دهند.
من به مذاکره‌کنندگان عالی‌رتبه‌مان اجازه خواهم داد که در صورت تمایل به صحبت ادامه دهند، اما من این موضوع را بعید می‌دانم.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18331" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ :
تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18330" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:  «آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18329" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مواضع جدید ترامپ درباره ایران:
«آنها یک مشت آشغال هستند. من اصلاً از آنها خوشم نمی‌آید. ما وقت زیادی را با آنها تلف کرده‌ایم. آنها بی‌کفایت هستند. ما فقط باید کار خودمان را بکنیم. آنها می‌خواهند رهبر ایالات متحده - من - را از بین ببرند. من سال‌هاست که نفر اول فهرست آنها هستم. ما باید سرطان را زود از بین ببریم. من اینطور احساس می‌کنم.»</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18328" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">️خبرنگار:واکنش شما به حملات اخیر آمریکا به ایران چیست؟
مارک روت، رییس ناتو:به نظر من، این اقدام کاملا ضروری بود. ایران، آتش‌بس را نقض می‌کند</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18327" target="_blank">📅 11:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای انفجارات در بوشهر</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18326" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه پاسداران در پاسخ به حمله آمریکا، یک حمله هماهنگ موشکی و پهپادی به ۸۵ هدف نظامی ایالات متحده از جمله ناوگان پنجم، پایگاه هوایی علی الصالح در کویت و بندر سلمان انجام داد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18325" target="_blank">📅 10:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18324" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYEUSiTo3xhmzWB_EsRaeTzlWsfqjOtCNcJ01oJBH5fP_jf_AaUrxfoq2BdYhfhosjiu57hmaf4YKw24ysK1zomnhqBS6kXl46eYW8y4EY3dpPDNnxNxH-RWnCKniZYiKlwYKkWdDZb2kbbmyq5O4bwCbJuj0d8l1Rnylhp6j87y-NyH0AsmQcma1whYLBaD9i7SCB_cC7DGtPFgx3BEtuJeqlpr0J8vhBdTC_bLrMASz2E4deP1oSNk0X-d-kx999eQC7Zm59oldBe8taOWrjKdYwqSCFzGLY3dYErxf-vIif8R7jMwQtvenkecgYi_nSUqAyUz5AVbxiEoc85wUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18323" target="_blank">📅 10:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">CNN:
وزیر دفاع ایالات متحده پیتر هگستت‌ در روز سه شنبه سفر اول خود را به اسرائیل انجام خواهدداد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18322" target="_blank">📅 02:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro_5TLGEzJLpl3CFQNPLT0K84kjjXf5LtFcAZ-kWcWYSpNvosc3rHlblEWfV6qZCCCXgsOIWCVsXv91WBHsZBoe6Yp1l-EAAOiaTnC4rIKui-NQwXCSPtutqX67TfiBvhFEHmon0NkneXKBMiVktgG8qEjtqLe9Kls9q8LWqJI1S7amVLoMIIq0IY2aOMXQ8HfeuBRhhxmsryWadls_62wxFDXRgHHwph5ewqHoWQiFEYqAzin2dSyWh4lXqgEJ9kmxCkxcDBg7PioDmNs298RfLAbg90JXiNdJbINt6cF2JfK3_was6d3JDOCyDPlNdHP4dT4pMi9tF7tIBJvHYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!  ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18321" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حملات ناوهای جنگی آمریکا در ایران، اهدافی مانند سامانه‌های پدافند هوایی، سیستم‌های نظارتی ساحلی، موشک‌های زمین به هوا، موشک‌های کروز ضدکشتی و محل‌های پرتاب پهپادها را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18320" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام آمریکایی به CNN :
حملات به ایران برای تنبیه‌ست!
نه مقابله‌به‌مثل؛ و این حملات فعلاً ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18319" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEEJBawGdBEUKm4Vr2IcH4S4dfX0kJ_rYJcyYDWudBq_75ukZ9hm10OH-eUMNBkFKyanR8ffMy9-w4Pn0jHffJgD9Qk3TpXNc8LTMP8Ld9lYWsP1LkUFeE1MaAXaqACFC6D11xQ289Rb0hd2kgG4IjaUwvBltb3KF7nOojCcPc7NL7ZdvsimSAeQMvj0ms23ba_8kTxb3gTE-b4MThuTe5odfYbjujGbR57rxrDg7jUmYoa1ATjdkmfX4LyhUOwmN1WmE9oJehyyqJehxVdm9-T0LRLmgjbE1DbRuO2a6x0JSWkRHPBkxC-_0czexh87p0tMy-GHwdTqyQUCU409AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18318" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=G2cCNqmyFxVQchBT7_FRm-93uGoKsiUa-BlPH6R2FnqUprESs_JMzLC9fpB-Y_sx6oGlEy9U3jf2nUZUZcrUSIskdcYAmSdoyHduOw2cHi1ywmummx3UxjtzB2C0k2Jolwxe-mr_xKrfDV_-5jUBCj9sUr_BklYjMFLCOEFQLkfULK6e0VjD96E7HgC7vaD5kgxbYAXx1NYm2HsaVmJnDWBsW8Hmj-s2YWFQTKeoetkXMxDPfNTBR7s4FcPiw-7SfxrA2J98kprJY7yc7AYRkjbP7wvniyd58vjCelZoMAvXU5h1G0H9MZV_QN3gqa9MUyMlT1-EK8ksQN2R9tq5yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=G2cCNqmyFxVQchBT7_FRm-93uGoKsiUa-BlPH6R2FnqUprESs_JMzLC9fpB-Y_sx6oGlEy9U3jf2nUZUZcrUSIskdcYAmSdoyHduOw2cHi1ywmummx3UxjtzB2C0k2Jolwxe-mr_xKrfDV_-5jUBCj9sUr_BklYjMFLCOEFQLkfULK6e0VjD96E7HgC7vaD5kgxbYAXx1NYm2HsaVmJnDWBsW8Hmj-s2YWFQTKeoetkXMxDPfNTBR7s4FcPiw-7SfxrA2J98kprJY7yc7AYRkjbP7wvniyd58vjCelZoMAvXU5h1G0H9MZV_QN3gqa9MUyMlT1-EK8ksQN2R9tq5yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی انفجارات پیاپی در بندرعباس!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18317" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نفت را بای داریم پدرسگ ها</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18316" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18315" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
