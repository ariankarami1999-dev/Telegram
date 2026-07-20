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
<img src="https://cdn4.telesco.pe/file/CNH3YUT3YvaYyJynyQ3RGCWV2F8v2CIpyUUfBzpGDbT5NqTAU5_FfQ9YgZmOlPC9anQhn521i6Uetpd5OdQnXhI8TL8KDXHvbmM89giW6ThmBkgmV9ejalaTDMEOJLe-j_2eZ_STR6TsbzimZhl_m7FFRiH8cAkrJ7DQrMcJ_w9c3EXv7i5cibQ95sNc5SZkXSt9TQoV3rFPMuop_hbFKusdFBOF64fI3cEtbkwdaJEpUltnyhXxtX2DUwj1cjFGh1d7XEQxSzACiXenl5GD5DPvpVg1exjmY433cgpaF2Y8XYKoAhSxgRUoarQ17jz73m8CEwsyiaQ46aDAEwJBAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.4K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 02:18:51</div>
<hr>

<div class="tg-post" id="msg-19044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک مقام آمریکایی:
اگر ترامپ تصمیم به گسترش جنگ بگیرد، حملات شامل تهران و سایت های هسته ای می شود.
اسرائیل ممکن است در جنگ ایران شرکت کند اگر ترامپ تصمیم به گسترش دامنه آن بگیرد.</div>
<div class="tg-footer">👁️ 126 · <a href="https://t.me/SBoxxx/19044" target="_blank">📅 02:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوزاری گدازاده کم بود، گروهبان قندلی هم به فهرست گه خورهای علی دایی افزوده شد!  گویا سرگین شهریار چندان لذیذ است که این مگسان آن را انگبین می بیینند!  پفیوزهای ... مال عوضی</div>
<div class="tg-footer">👁️ 596 · <a href="https://t.me/SBoxxx/19043" target="_blank">📅 02:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!  ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/SBoxxx/19042" target="_blank">📅 01:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عادل فردوسی پور > New Castle
علی دایی > New Castle
کریم باقری > New Castle
99 درصد ایرانی ها > New Castle</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/SBoxxx/19041" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینطور که پیش می رود فردا در هند عزای عمومی اعلام خواهدشد.</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/SBoxxx/19040" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddjvtuugO77wYoLQnhKglbwsZfzb1LctW5vHlgh6YbutVelEl738511yLkslROlesOKLFMyb0rVfTqMiM-JM3jyxw1ASF-Sm_SWagaEr52UwzqE_ExG_zS2qS9Xq0Bm0uKSYLHMBGhUzyfT3Vq7M76giLMbj5UkF_fQTaLiZP7YafkT5U_l7g-zD4PU0EI01JXx49xReO56Ob_xfQgYOEW4uToFOK5nyjLyngQ9tu2sl4h3ijXTm1b1acn2cb7oNjNvVJM41zWLTjR_5YKhGLXlc65R4TUXHYOQjZNcUg1nEUUYs5q6-C6peoLrHp-Io8GgOCvUISUJi9_gbtrn_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی نفتکش دیگر در سواحل عمان هدف قرار گرفت!</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SBoxxx/19039" target="_blank">📅 01:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19038">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واقعا به نظر می‌رسد این الاغها تا یک
جنگ هسته ای
جهانی راه نیندازند دست بردار نیستند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/19038" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19037">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت خارجه چین در مورد سیاست هسته‌ای ژاپن:  از زمان به قدرت رسیدن تاکیچی، نیروهای راست‌گرای ژاپنی نیت خود را برای احیای نظامی‌گری، رها کردن اصول سه‌گانه غیرهسته‌ای، جستجوی سلاح‌های هسته‌ای و ادامه مسیر نادرست آشکار کرده‌اند.  اگر ژاپن به تلاش برای اصلاح اصول…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/19037" target="_blank">📅 00:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19036">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاخ سفید اعلام کرد که ترامپ روز سه‌شنبه در مراسم انتقال با احترام پیکرهای چندین نظامی آمریکایی که در هفته گذشته در جریان آخرین دور تنش‌ها با ایران کشته شدند، در پایگاه نیروی هوایی دوور شرکت خواهد کرد.
این نظامیان شامل دو سربازی هستند که در حمله موشکی بالستیک ایران در روز جمعه گذشته در اردن جان باختند</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/19036" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سنتکام:
امروز ساعت ۴ بعدازظهر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، دور جدیدی از حملات هوایی علیه ایران را آغاز کردند. این حملات برای تضعیف بیشتر توانایی‌های نظامی ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شوند، طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/19035" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش‌ها حاکی از آن است که مقامات نزدیک به رئیس‌جمهور آمریکا، ترامپ، تحت فشار قرار دارند تا پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرند.
آمریکا امکان آتش‌بس را رد نکرده است، اما اصرار دارد که این آتش‌بس باید طولانی‌تر باشد و به تفاهم‌های خاصی در مورد تنگه هرمز گره خورده باشد.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19034" target="_blank">📅 21:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حمله دوباره ایران به بندر عقبه اردن</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19033" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اخباری از حرکت نیروهای زرهی ایران به سمت کویت به گوش می رسد!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19032" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اخباری از حرکت نیروهای زرهی ایران به سمت کویت به گوش می رسد!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19031" target="_blank">📅 20:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">— یک کشتی در ۱۷ مایل دریایی شرق امارات متحده عربی توسط یک پرتابه مورد اصابت قرار گرفته است.
هیچ تلفاتی گزارش نشده است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19030" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:  «نتانیاهو به هیچ وجه، به هیچ شکل یا فرمی، در حالی که در ایالات متحده است، دستگیر نخواهد شد.»  «او علیه جمهوری اسلامی ایران می‌جنگد که اخیراً ۵۲,۰۰۰ معترض بی‌گناه را کشته و در ۴۷ سال گذشته سربازان آمریکایی و دیگران را کشته است.»  «تنها کسانی که باید…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19029" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:
«نتانیاهو به هیچ وجه، به هیچ شکل یا فرمی، در حالی که در ایالات متحده است، دستگیر نخواهد شد.»
«او علیه جمهوری اسلامی ایران می‌جنگد که اخیراً ۵۲,۰۰۰ معترض بی‌گناه را کشته و در ۴۷ سال گذشته سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید دستگیر شوند، کسانی هستند که ایران را به این مارپیچ بی‌سابقه مرگ و ویرانی کشاندند، چیزی که باید سال‌ها پیش توسط رئیس‌جمهورهای قبلی حل و فصل می‌شد.»</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19028" target="_blank">📅 20:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19027">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سازمان صدا و سیما:
یک کارخانه صنعتی در حومه شهر خمین، ایران، حدود ساعت 7 بعد از ظهر مورد حمله قرار گرفت.
هیچ گزارشی مبنی بر کشته یا زخمی شدن افراد وجود ندارد و مقامات در حال بررسی میزان خسارات وارده هستند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19027" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19026">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ذخایر نفت خام در ذخیره استراتژیک نفت ایالات متحده حدود 5.1 میلیون بشکه کاهش یافت و به 311.4 میلیون بشکه رسید که کمترین میزان از سال 1983 به شمار می‌رود.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19026" target="_blank">📅 19:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19025">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر امور خارجه فرانسه:   امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19025" target="_blank">📅 19:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19024">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر امور خارجه فرانسه:
امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و در ساعات آینده به فرانسه باز خواهند گشت.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19024" target="_blank">📅 19:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19023">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDODEQkZhUqrY-ZRJl_xwFrVzO0WfpcEg1_QMyDNQWCFv9jWFs06NuBf8yaWYqYiN40IL9lV5fDztSy7goxtxFCoId8zozZXAvKIsIkK1JJyELj4VMrx040C5s_e2aEsPtjlySF6W_1QtAtRy2x43e4ioQBmjHQLiNw_f8TXpwmX-vsvx9oYvYtfK_3ZXGY5gJNsT0FfZ1D5JCEkCixB_NHJgESMt7ofGcrPbG70CTlj4EF0M-94jf58zZ7Am66Ik2EjTwb3ye7CQFf1fZiubvgY23sF6TJZRbSLyZZS0WNo0f0mf2BQfYxiOI_9ebe4PTDjaU1z6T-psxXQePKSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.  معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19023" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19022">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چهار شهروند هندی در جریان حمله به کشتی تجاری "My Golden Leo" کشته شدند، در حالی که این کشتی در حال خروج از بندر اودسا در اوکراین بود.   سفارت هند در اوکراین به دقت وضعیت را زیر نظر دارد. هند این حمله را محکوم کرده است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19022" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19021">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6XYPxILgSmLeu-FI4ZvbGeNfptIFoPQZnPgxdKxjIecgTG0yEIoORHOlNGyhgK5CvGgVAhX98MB2N5CY38MCWsUKm5ByHWoCBruVGSwtH1X4K4u7MCZY3EqA1kyR7FUG8e12xsGCboBMQgoo2IQWuNBhXYhw3GUMSP4kIUkLN61HDyPzNiB5RR2johDD03J7RM5g56uYNF2g3_OiJ_NSwJn7szBUusdwrTIlWiMLoyjz4T2C_yz6ELTWN-4kFG9VA0T3JIgPrSx3IHicM2PpWztgMT343uRfKZE2C3-cxr28WGgG02vPyzeY7RXkPKeXvBYkJdEk2_7UTQ99GmzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره کل کشتیرانی هند شامگاه چهارشنبه ۲۴ تیر با صدور دستوری اعلام کرد تا اطلاع ثانوی هیچ دریانورد هندی نباید به کشتی‌هایی اعزام شود که مسیر سفر آن‌ها شامل عبور از تنگه هرمز است.    در این دستور آمده است: «با توجه به تشدید وضعیت امنیتی در منطقه خلیج فارس، اداره…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19021" target="_blank">📅 19:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19020">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله ایران به بحرین</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19020" target="_blank">📅 18:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19019">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از دیشب دیگر دامنه حملات آمریکایی ها به جنوب محدود نیست و تبریز و شیراز هم مورد هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19019" target="_blank">📅 18:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19018">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19018" target="_blank">📅 17:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19017">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آتش‌سوزی در یک کشتی باری یونانی رخ داده است. این کشتی در نزدیکی تنگه هرمز مورد اصابت یک پرتابه ناشناس قرار گرفت.
— رویترز</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19017" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19016">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار در شیراز</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19016" target="_blank">📅 17:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19015">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب از هرمز ۲۰ میلیون بشکه نفت در روز عبور می‌کرد که برای ۷ میلیون ش جایگزین پیدا شد (خط لوله شرق به غرب عربستان)</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19015" target="_blank">📅 15:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19014" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اگر یک بار دیگر هم فریب میخوردیم با ۲ بار قبلی می‌شد ۳ بار و این اصلا خوب نبود.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19013" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قالیباف :   آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.   ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19012" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Ob4TqRzY2WcM_wGPkvGjLHdPXgZn1_aFu2aCgqmsTXrieOwRcnIUVqT-lMi4KkeieBMdUZ6ygRYlMfwEjnhrI7-ow4IQ7gROfUY4pj74hr_W6g3b3z7k-J7PJNXrKa0ZTIX6wAaWZNrOv8ldk7S58mlx17lK0324QNQs4fAAvGb4bajmMGUIXBRml9U3tYkkdQYyJ3fk4L8TbgNWQId25Uu4kYPtwxk9qzL-sEruNW9owpwYnoltBYJ2IIgnUDwk8rOMxXNJVklaIRC3k2aMiAYRFh97LNTNNoXDZF6zdHVn24mRaY4kDrFXM-ZRuE4MILs1DSM4Y7GC88KVSqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف :
آمریکایی‌ها تجهیزات نظامی جدیدی را به منطقه می‌آورند و ادعا می‌کنند که قصدشان متوقف کردن جنگ است. آن‌ها شرط‌بندی کرده‌اند که ضریب هوشی ما به اندازه هوش اندک خودشان است.
ما به مرحله‌ای از تسلط در تشخیص این بازی‌ها رسیده‌ایم و بر این اساس خود را آماده کرده‌ایم. اقدامات باید ادعاها را تأیید کنند، نه اینکه با آن‌ها در تضاد باشند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19011" target="_blank">📅 15:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19010">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.
این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون تصویب پارلمان صورت گرفته است.
این درخواست در حالی مطرح می‌شود که تنش‌های ایالات متحده و ایران همچنان در حال تشدید است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19010" target="_blank">📅 15:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19009">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار فردایی تهران
⏳
188,700 فروش  بازتاب انتشار مواضع ملایم شده دو سوی نبرد روی قیمت دلار داخلی  نکته — موقت است و دوباره بالا می رود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19009" target="_blank">📅 15:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19008">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ببینیم آمریکا همان بلایی را که با قربانی کردن اوکراین بر سر روسیه آورد، با ژاپن بر سر چین می آورد یا نه.  در نشست با نیما (پیام ریپلای شده) مفصلاً درباره تاریخ تنشهای میان ژاپن و چین صحبت کردیم.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19008" target="_blank">📅 14:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19007">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بوی مذاکره می آید…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19007" target="_blank">📅 13:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19006">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نیروی قدس سپاه پاسداران انقلاب اسلامی ایران مدعی شد که با استفاده از اطلاعاتی که از سوی افراد مقیم اردن به دست آمده بود، به هواپیماهای آمریکایی در فرودگاه عقبه حمله کرده است و ادعا می‌کند که این حمله خسارات جدی و تلفات انسانی به همراه داشته است.
این سازمان همچنین از حامیان خود در اردن تقدیر کرد و خواستار حملات به نیروهای آمریکایی شد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19006" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19005">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJB8jSY67A01TdFH0RQV_qRz8W300T6jsLJTuAdbO6yOhbV_zw5pQQ-LvRvsVjhDhlT7yWihOepAqS_EzS7-kDfr8VKaXSGrO3j9tM1_4cEK8mU-UHFaBEMOJI_xlUOH8s9CjLsgyBOx6gg-C5SjHKcK-ldqCiEsjOirP2Us18Ep4jkxCdhEmNFHaaJ_VNf_40l9ske_a_ekmcF0t5PY-tcrQ4Vn6cbTYj9S85J3vv3BfOfYp1g7WUKzDexd76YEU1Ynh0E6rDQRpYsyETNOAzu4OuKXAWJhAny_yNeBLbZwO4FXRnQg3ED5I9r7aQvI6KMo7FMopXkFKOn477AXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
سکوت وارش و واکنش بازار اوراق
وارش در نشست کنگره با وجود تأکید بر مهار تورم، از ارائه هرگونه راهنمایی درباره نرخ بهره یا سیاست ترازنامه خودداری کرد و بازارها را در آستانه نشست مهم فدرال رزرو در وضعیت انتظار نگه داشت.
بازار اوراق این سکوت را به معنای احتمال پایین افزایش نرخ در کوتاه‌مدت تفسیر کرد، اما رشد بازدهی اوراق بلندمدت و نرخ وام مسکن نشان داد نگرانی‌ها درباره تورم و بدهی دولت همچنان پابرجاست.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19005" target="_blank">📅 13:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19004">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">347.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19004" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 9  دوشنبه 20 جولای 2026</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19004" target="_blank">📅 13:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlTqZBwWeLKAgc2xX7IUyOHsWePWAUBZsI-UWHmNiSpYCaIFU5RQXtAKLnygePFD_V3kG0kaOxi9KjoEzTR2KWE5n7cDD644_GksSnhG7L5TWDFV5AEIc40Hc5Dfj2QaZ2wZixVxfi1GAE51S5yOQl0dFkZHfN9BddsFUQXwG3uIM6tM37Xzlo_7EZGEWjXsPZTo5BrdahwKApu4ENU2ocjFC-w-JArk8N3ZyCuyJNW_Jxb-PaGd1bRnvHLVjrlsP4UXwt0fXnCVX4hikCiu6q5J9tMXp8K_6ffQsjuysIM3wdHWKdsqkvl_b4Aga5gOkvuMnlbKUBtjQoYxxR8M8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح نسبتاً پایینی قرار دارد.
معمولاً در این شرایط طلا رنج می شود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19002" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19001" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 9
دوشنبه 20 جولای 2026</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19001" target="_blank">📅 12:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدای انفجار مهمات عملکرده در تبریز و مهمات عملنکرده در تهران!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19000" target="_blank">📅 11:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18999" target="_blank">📅 10:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">UKMTO:
"یک کشتی در فاصله ۸ مایل دریایی شمال غربی شهر خَمْسر در عمان، مورد اصابت یک پرتابه نامشخص قرار گرفت و خدمه کشتی به طور ایمن از آن تخلیه شدند."</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18998" target="_blank">📅 10:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنان شنیدنی دکتر موسی غنی نژاد درباره حرامزاده شیادی به نام علی شریعتی!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18997" target="_blank">📅 10:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15659d093.mp4?token=TWt4gqkbyNP01c8Gk0Zc7khj_lcBb1IAUaTor9BWhtHQ1Y8bEnb-wnyqEhnC8lqYKNBviX5yQbtxYFeFewsy3btnwb2fhipPt89EOims6aQ4Kutn4vNzP5rNqMAJk7SHYyGzrAnvg5o5TS1puo-y42NqZ1l3t0mSAT3y07jUzV2QpyTAG5uO6iPDi3HZ9Cj4gdvFF7XPPKJMDY9WLMLomTOW6KwJcvmow9_hrLtpvJVGNT664wXwCafxnepxaE1JJ2iTpOEOJppmKfGzV7q8O0MMEhaYwgPUMRJtspCEmKbOEp3i9Jd6MNwpQRnFX7VqJ8BpQUNuhwBr6XRIRnr43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15659d093.mp4?token=TWt4gqkbyNP01c8Gk0Zc7khj_lcBb1IAUaTor9BWhtHQ1Y8bEnb-wnyqEhnC8lqYKNBviX5yQbtxYFeFewsy3btnwb2fhipPt89EOims6aQ4Kutn4vNzP5rNqMAJk7SHYyGzrAnvg5o5TS1puo-y42NqZ1l3t0mSAT3y07jUzV2QpyTAG5uO6iPDi3HZ9Cj4gdvFF7XPPKJMDY9WLMLomTOW6KwJcvmow9_hrLtpvJVGNT664wXwCafxnepxaE1JJ2iTpOEOJppmKfGzV7q8O0MMEhaYwgPUMRJtspCEmKbOEp3i9Jd6MNwpQRnFX7VqJ8BpQUNuhwBr6XRIRnr43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان شنیدنی دکتر موسی غنی نژاد درباره حرامزاده شیادی به نام علی شریعتی!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18996" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله به بوشهر!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18995" target="_blank">📅 09:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امروز جلسه‌ای برگزار می‌شود تا درباره وضعیت فرودگاه بن گوریون بحث و بررسی شود و به درخواست واشنگتن برای اعزام هواپیماهای بیشتر برای سوخت‌گیری پاسخ داده شود.
برآوردهایی در اسرائیل نشان می‌دهد که واشنگتن ممکن است درخواست اعزام ده‌ها فروند هواپیمای دیگر برای سوخت‌گیری به اسرائیل را مطرح کند.
— شبکه ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18994" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18993" target="_blank">📅 09:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حملات سنگین موشکی ایران به بحرین</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18992" target="_blank">📅 09:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صدای انفجار در چابهار و تبریز !</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18991" target="_blank">📅 04:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:
ایران از نظر نظامی تقریباً همه چیزش را از دست داده؛ فقط تعداد کمی موشک، پهپاد و توان تولید برایش باقی مانده، ما تنگه را کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع ندارد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18990" target="_blank">📅 04:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کویت اعلام کرد که سامانه‌های دفاع هوایی آن پهپادهای ایرانی را رهگیری می‌کنند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18989" target="_blank">📅 02:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تا لحظاتی دیگر پخش زنده بازی تیم های  ملی New Castle و سوییس از شبکه نسیم</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18988" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-wdKd9Q5796eG8Yjho6A-7IjB5VGiR6wEQbUzyZpZLNrgISQhjsNU7r9mGBhAzrpY_ohPC31EtGOvs2RijUy3cBigDQLS7lP0gItJEvutp8EWTj9-Bh0YnCPDEZFA6NHTEQ29Swx-LH1jPwpoxOTfluoWmH5uSuUKt8pnCiJ9qDljpzY2O6KOerk-LllZUF4iVJUaRyv9yZJxPcSPfSJslpV9bJ7POJKW8N4_-gw9UFTjhpHVMbYAuQufNJ0dSElWbgdcHqSwqmeKggMdiQa0NtZS1odQVqY4SQZIYehY9ylTt3Td-kUj2K4ml0oiivf9Ps05q9nmDNrp12CL4Ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت پرورش غیرمجاز دام و طیور در حمام</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/18987" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پمپئو: فشار اقتصادی خفه‌کننده به ایران را ادامه دهید تا اعتراضات داخلی در آنجا رخ بدهد!
وزیر خارجه دولت اول ترامپ:
واقعیت امروز این است که به‌زودی آن محاصره‌ای که سنتکام با کارآمدی بسیار برقرار کرده و همچنین تلاش برای کاهش توانایی آن‌ها در آسیب رساندن به کشتی‌هایی که از تنگه عبور می‌کنند اهرم فشار ایران را کاهش می‌دهد و در نهایت آن‌ها دیگر قادر به پرداخت حقوق نخواهند بود.
حماس، حزب‌ الله و حوثی‌ های یمن، آن‌ها نیز دیگر قادر به پرداخت حقوق نخواهند بود و پول لازم برای خرید مهمات را از دست خواهند داد. و زمانی که این اتفاق بیفتد، مردم ایران فرصتی را به دست خواهند آورد. این مسیر پیش روست. فشار اقتصادی خفه‌کننده، قدرت نظامی و صبر دیپلماتیک، به نتیجه‌ای مطلوب برای رئیس‌جمهور ترامپ و جهان منجر خواهد شد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18986" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کشتی باری ترکیه‌ای گلدن لیو در اودسا هدف حمله قرار گرفت  کشتی باری گلدن لیو که پرچم گینه بیسائو را دارد و متعلق به یک شرکت ترکیه‌ای است، هنگام خروج از منطقه درگیری با محموله‌ای از غلات، توسط سه موشک کروز خ-۵۹/خ-۶۹ هدف قرار گرفت. این کشتی بخشی از «ناوگان سایه»…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18985" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18984" target="_blank">📅 00:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">پناهیان:
اگه بی‌برقی و بی‌آبی رو تحمل کنید،
جهان رو آزاد می‌کنیم و آنها را هم بدون آب و برق خواهیم کرد.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18983" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سنتکام:
یک عضو خدمه ایالات متحده در ۱۸ جولای در شمال عراق در عملیات کشته شد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18982" target="_blank">📅 22:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa18XrZ3WyEOUTSGLrVwDBXh_t2jhmGYBDPA_FeHfvYgMhj6Xm29Kt4qTMMtneCPEuDMGv-B70D4nyhkPG0-Rl-qWEUC0uXc2HbO6ftk6hAaKHvyctFv3c-PNtIlKlRiiRel102nOKDIXscq9xYmShTANf7hVsxYqyWd-vPQ96fo1NLO5DUb4ZUER8yfaNu-6QbK3gtPrv2qposcNgHHpq2FAe9vfausbDo3sOUAo1aZgWIKqBNWK1dMwlUktlGFCCCaAKzvoM72fHPyBVWhdXuK92IU44DrV2qXeqcN5MgvS-j5RbS6AJYCjdsU3CwgFkN6-QkrxOky2IgYnLRarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید معروف امشب موقع اجرا واسه فینال جام جهانی، رویِ لباس خودش فروهر نماد ایران باستان و آیین زرتشتی داشت.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18981" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18980" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مقامات ارشد اسرائیلی به سازمان پخش اسرائیل گفتند:  «ترکیه تهدید کرده است که در صورت عبور نیروهای کرد از خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.»</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18979" target="_blank">📅 21:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گویا داریم به ساعت صفر حمله زمینی موج 5 نزدیک می شویم.  شاید سرانجام ترامپ توانسته با آب نبات هایی مانند اف-35 و قراردادهای تسلیحاتی و اجازه دادن به ترکیه برای حمله جولانی به لبنان و یافتن جای پا در عمق راهبردی اسرائیل، موافقت و همراهی اردوغان را برای حمله…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18978" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سایت والا:
ارزیابی‌های امنیتی اسرائیل نشان می‌دهد که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18977" target="_blank">📅 19:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک نیروگاه برق دیگر در کویت در اثر حمله ایران دچار آتش سوزی شد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18976" target="_blank">📅 18:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:  رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.  اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/18975" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزیر انرژی آمریکا کریس رایت:
رئیس‌جمهور ترامپ می‌خواهد جنگ را با یک توافق مسالمت‌آمیز با ایران به پایان برساند، اما برای انجام این کار دو طرف لازم است.
اگر آنها آماده انجام این کار هستند، این راهی است که به آن پایان خواهد یافت. در غیر این صورت، ما جریان ترافیک از طریق تنگه را بدون همکاری ایران تضمین خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/18974" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irxm_GywaYk3sakG8aVSNMh5gA1g1BdZr-m_HoYAUeKVeyKXgaXNJKhCJTCdynUND9BJlFnazpWbA-y4KL_BkWxpbPycBe9hkA_M1_ZRjPi6FPd0398ihM12MBTd3-YkDd8lVhTMXW6NuPHpm0rXLp9JiueHObhB3nSMqeelfPYTc_d4bhe8jXp2JhaST0dWjSsCbAHR6bQLrtYaFXGPPyKTkj_pWEkxfS_VjTilH_RG6PrKz2Xw8SXZMSOwcwZfeLCQTnRj_X-9eGb-lRsgYW47bkFXG6kmxOqyHrsBATu1oDV0ZWxFJ6UlmyW183rgyiGsOffOgbHwnmFQR7OgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات موشکی جدید ایران  ایران موشک‌های بالستیک را به سمت اردن پرتاب کرده است   برخی از موشک‌ها به سمت بندر العقبه هدف‌گذاری شده‌اند که در جنوب اردن واقع شده است.  تلاش‌های رهگیری موشک در شهر همسایه ایلات در اسرائیل ثبت شد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18973" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18972" target="_blank">📅 17:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز:
هجوم‌های اخیر ایران به پایگاه‌های آمریکا در اردن باعث خسارات سنگینی شده است.
بیش از چهار حمله در پنج روز، موشک‌ها و پهپادها ده‌ها سرباز آمریکایی را زخمی کردند، چندین هلیکوپتر بلک هاوک را آسیب زدند و به تأسیسات نظامی کلیدی ضربه زدند.
کشنده‌ترین حمله روز جمعه در پایگاه هوایی موافق سلطی در عزره رخ داد که منجر به کشته شدن دو سرباز آمریکایی، مفقود شدن یک عضو نیروهای مسلح و زخمی شدن چهار نفر دیگر شد.
دو روز پیش، همان پایگاه مورد اصابت قرار گرفت و حدود ۲۰ سرباز زخمی شدند.
حمله دیگری تعداد قابل توجهی از هلیکوپترهای بلک هاوک را در پایگاهی در شرق اردن آسیب زد، در حالی که حمله‌ای قبلی به یک تأسیسات مسکونی ضربه زد و چندین عضو نیروهای مسلح را مجروح کرد.
مسئولان آمریکایی می‌گویند این حملات نشان‌دهنده توانایی فزاینده ایران برای غلبه بر یا فرار از دفاع هوایی ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18971" target="_blank">📅 17:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سبحان الله این چه وضعیتی است؟!
قرار بود به کمک تازیان بشتابیم تا فلسطین را از اشغال اسراییل آزاد کنند اکنون طوری شده که عربها از اسراییل کمک میگیرند تا پرتابه های ما به چاکرای پایینی شان فرو نرود!
یک جور کمدی پورن شده که انگار عطاران سناریو اش را نوشته باشد!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18970" target="_blank">📅 16:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیروهای مسلح اردن:   سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -   تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18969" target="_blank">📅 16:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیروهای مسلح اردن:
سه موشک ایرانی که به سمت پادشاهی شلیک شده بودند، رهگیری شدند -
تلویزیون دولتی|</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18968" target="_blank">📅 16:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18967" target="_blank">📅 14:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18966">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaJHqbNYagZw34xovV3LjQOuGVF-fSR5R1rqHxWeUvkqEbHXige_H2K9d-rBUgpMrkUQ65LA2LxV8Mcq3O8EgThLswIH6JZQezr8y5hBu4MsgGyyYdm5I_LSMJX4oXVnvU3ME_3JljqaRf_6IspOHdPVzzI2lX_uLdUsMA8m3KQH-gwAr7iScSc8zm-6bfW6gA-rNF4-PgHLG7Jfp_FNJRYqkPFEjaKf0f1EpxXBbXoNylI3VuLTewtHUJ--HYFUORhxNVzCqRl04uTJSyTymOgr_kDlHjK3cl2cx59CAkN6WsYz6XgHg5F9xXcQYkx7P0aO9sgPOa0Dkko6dqf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپورت:
کاخ سفید به آرژانتین مجوز داده تا در صورت قهرمانی جام‌جهانی، بنر «جزایر مالویناس متعلق به آرژانتینه» را در مراسم قهرمانی به نمایش بگذارند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18966" target="_blank">📅 14:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/18965" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18964">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده و از طریق یک مسیر ناامن از تنگه هرمز خارج شوند.
دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
نیروی دریایی سپاه پاسداران انقلاب اسلامی اعلام می‌کند که کنترل کامل تنگه هرمز در اختیار این نیرو است و تنها مسیر ایمن، مسیر مشخص و اعلام‌شده است.
همچنین تأکید می‌کند که هیچ مقداری از نفت، گاز و کود، بدون هماهنگی و مجوز قبلی از تنگه هرمز عبور نخواهد کرد.
کشتی‌هایی که تحت تأثیر اقدامات دشمنان آمریکایی قرار گرفته و وارد مسیر ناایمنی می‌شوند، قطعاً دچار حادثه خواهند شد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18964" target="_blank">📅 13:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب جام جهانی هم امشب به پایان می رسد.
گفته می شود بازی ایران—سوییس  بعد از فینال برگزار خواهدشد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18963" target="_blank">📅 09:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18962" target="_blank">📅 09:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز  در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18961" target="_blank">📅 09:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18960">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbzJHU1w7nSMB6rG-o0UaadgetL4oI35G41xc-ZSnvs4T8ycWRmp4yCEvw8OHncAbPEV0HaChvuZQWoMD5y06bLK8hd-zCvebVbGhiTxlaSIwyohGoHefv5faHhaIQmZKKemPlmNuIJI-wRrN1Euo6a02eONfSlJfHOxl5cOSWeTwt8Qwp8Xnu9J2EI0ymR4C3gc5va8Ea-kdpX9g5X7d28K2DeQbcx-fb4NpMl9uqU2QBSYrG_kvvmfSQufzfer_RPUqUw4G0cp7Z7ivCJdDntmAKumpRR10V5Qxjt9tykPy_EYPfCXAdZUz8tnRD-KdEV_0_j0NxEJNjHicSRqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز
در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود عرضه را افزایش می‌دهد. با این حال، ساختار بازار جهانی نفت در سال‌های اخیر تغییر کرده و اکنون یک متغیر جدید در معادله ظاهر شده است:
رفتار وارداتی چین
.
چین که بزرگ‌ترین واردکننده نفت خام جهان است، دیگر صرفاً یک مصرف‌کننده منفعل نیست، بلکه به بازیگری تبدیل شده که می‌تواند شدت نوسانات بازار را تعدیل کند.
گزارش نیکی آسیا
نشان می‌دهد که چین در دوره‌های شوک عرضه، نقش «واردکننده نوسانی» (Swing Importer) را ایفا می‌کند؛ به این معنا که با کاهش موقت خریدهای خود، بخشی از کمبود عرضه جهانی را جبران کرده و از تشدید افزایش قیمت‌ها جلوگیری می‌کند.
این توانایی از چند عامل ناشی می‌شود.:
نخست، چین طی دو دهه گذشته سرمایه‌گذاری عظیمی در ایجاد ذخایر استراتژیک و تجاری نفت انجام داده است. هنگامی که قیمت‌ها افزایش می‌یابد یا مسیرهای عرضه با تهدید مواجه می‌شوند، پکن می‌تواند برای هفته‌ها یا حتی چند ماه بخشی از نیاز پالایشگاه‌های خود را از این ذخایر تأمین کند. در چنین شرایطی، کاهش واردات به معنای کاهش مصرف داخلی نیست، بلکه صرفاً جایگزینی نفت وارداتی با نفت ذخیره‌شده است.
عامل دوم، انعطاف در مدیریت ذخایر تجاری است. چین در دوره‌های قیمت پایین، معمولاً بیش از نیاز روزانه خود نفت خریداری کرده و مخازن را پر می‌کند. اما در دوره‌های افزایش قیمت، این روند متوقف می‌شود و حتی بخشی از ذخایر مصرف می‌شود. در نتیجه، واردات کاهش می‌یابد، بدون آنکه فشار قابل‌توجهی بر فعالیت‌های اقتصادی وارد شود.
از سوی دیگر، پالایشگاه‌های چینی نیز انعطاف عملیاتی بالایی دارند. بسیاری از آنها می‌توانند برنامه تعمیرات یا کاهش موقت ظرفیت تولید را با شرایط بازار هماهنگ کنند. علاوه بر این، تنوع منابع تأمین نفت از روسیه، آسیای مرکزی و سایر تولیدکنندگان غیرخلیج فارس نیز وابستگی کامل چین به نفت عبوری از تنگه هرمز را کاهش داده است.
این تحول، پیامدهای مهمی برای بازار جهانی نفت دارد. در گذشته، کاهش عرضه از خلیج فارس تقریباً به همان میزان باعث افزایش قیمت می‌شد، زیرا تقاضا در کوتاه‌مدت انعطاف چندانی نداشت. اما اکنون، کاهش چندصد هزار بشکه‌ای واردات چین می‌تواند بخشی از این شکاف را پر کند و از شکل‌گیری موج‌های شدید سفته‌بازی جلوگیری کند. به بیان دیگر، چین علاوه بر اینکه بزرگ‌ترین خریدار نفت جهان است، به یکی از ابزارهای تثبیت بازار نیز تبدیل شده است.
البته این نقش محدودیت‌های مهمی نیز دارد. ذخایر استراتژیک چین نامحدود نیست و اگر تنگه هرمز برای چندین ماه به‌طور کامل بسته بماند یا صادرات کشورهای حوزه خلیج فارس به مدت طولانی متوقف شود، پکن نیز ناچار خواهد شد با کاهش واقعی مصرف، افزایش هزینه‌های انرژی و فشار بر صنایع خود کنار بیاید. بنابراین، توانایی چین بیشتر برای مدیریت شوک‌های کوتاه‌مدت و میان‌مدت کاربرد دارد، نه بحران‌های طولانی‌مدت.
در مجموع، یکی از مهم‌ترین تغییرات بازار نفت در دهه اخیر این است که دیگر تنها عرضه‌کنندگان بزرگ مانند عربستان سعودی یا تولیدکنندگان شیل آمریکا بر قیمت‌ها اثر تعیین‌کننده ندارند. اکنون رفتار خرید بزرگ‌ترین واردکننده جهان نیز به همان اندازه اهمیت یافته است. این تحول باعث شده تهدیدهایی مانند اختلال در تنگه هرمز، هرچند همچنان خطرناک، اما نسبت به گذشته تأثیر کمتری بر جهش پایدار قیمت نفت داشته باشند؛ موضوعی که می‌تواند بخشی از اهرم فشار کشورهای صادرکننده نفت در بحران‌های ژئوپلیتیکی را نیز تضعیف کند.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/18960" target="_blank">📅 09:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18959">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcseA4bd3orQbzncxZNiXuVCg53o9Jz3AxK_l9KmwXCfD9yf637rvQ-IrZ31RUvt8EnO6kQPmjATw4eI4382NRGvaXAQiPgu4JwvXlQiw5JTX5zN_05Xde1P1yjIaJYob5Em-VVm0HgBPUZCI40aggnHNUkp9vXJdOk9gmRJBxrv_ELq9whAOmhKbtwuG4C197ecgLAojSoAUAdxqWmlTv14QCctndwH7YYkDIQJ-fT61dm_UDOU6X7DRGK0ymWltNsgmqQE-H8H3UTmlsh08dX92RpDpn-cmZ2kofV_PlXX7EJQYonnOMLNDBX5pGVzbet67cLF0pN9E989WRERIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی از یکی از نزدیکان محسن رضایی</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/18959" target="_blank">📅 01:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18958">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a107e63.mp4?token=lA_O_YgbsrG-uY6c38MAs5de979f_1fdl4Ib-Kba28WZV9euBsqy0fiFipS8jNp4AtMcOeTeQEnzyDX42W15yB7HVLKttfDxu-i4qo5hdbiW3Ewsi1o0gcfWaXnoJW8_oYxd2jwfkXXuBx7bSXgsviDdV6Z4tKa_sZLCv8j3NUDlIXDQgfY75W6KapfKr09Cms7_nQqjPD2L-OGS60klmsHKPG3QNTT2GNp01Q6lerma0Iy6D8xQTdZEAamU39k2kZZYnjnwVvy8BYQAdAfYNJ9pz76LjEQZHYhAfSPderf4D6tKeWlkEU4vwq0lKIDAIXtsufcuXInH_czSajdUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a107e63.mp4?token=lA_O_YgbsrG-uY6c38MAs5de979f_1fdl4Ib-Kba28WZV9euBsqy0fiFipS8jNp4AtMcOeTeQEnzyDX42W15yB7HVLKttfDxu-i4qo5hdbiW3Ewsi1o0gcfWaXnoJW8_oYxd2jwfkXXuBx7bSXgsviDdV6Z4tKa_sZLCv8j3NUDlIXDQgfY75W6KapfKr09Cms7_nQqjPD2L-OGS60klmsHKPG3QNTT2GNp01Q6lerma0Iy6D8xQTdZEAamU39k2kZZYnjnwVvy8BYQAdAfYNJ9pz76LjEQZHYhAfSPderf4D6tKeWlkEU4vwq0lKIDAIXtsufcuXInH_czSajdUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SBoxxx/18958" target="_blank">📅 00:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18957">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است   بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18957" target="_blank">📅 23:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18956">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">—گزارش‌ها حاکی از آن است که جنگنده‌های F-16 نیروی هوایی ایالات متحده مستقر در پایگاه هوایی اسپانگدالم در آلمان به خاورمیانه اعزام شده‌اند. این هواپیماها قادر به هدف قرار دادن سیستم‌های راداری پدافند هوایی ایران و همچنین دارایی‌های موشکی هوا به زمین هستند.
علاوه بر این، جنگنده‌های پنهان‌کار F-35 از پایگاه هوایی لکن‌هیت در بریتانیا نیز به همراه تانکرهای اضافی سوخت‌رسانی هوایی برای پشتیبانی از عملیات گسترده‌تر هوایی ایالات متحده به این منطقه اعزام شده‌اند.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/18956" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXH8vT3rHiWItM4iYPotG5Vfe3uuT-5csb-EQxabcxzkJt_OmL1XYjQwpqxn8VbCoKh22VlBNs-72XTS7CfKMFobalSTVyahXzCE2RwPzmMJRKpTNq4Sq3FYXAKHLFhIiEC3HC5avU8RgMibIybI3LG5Y1USFE6oXFgXIc7_I-6mdaWgdAkXuNF5wYFTGBkKhDQf7N5kXeVyia5bOlvsLfE0jfvvS73K38CLMkJF0YxyaN140_5HcW74yYdv7_6MVp-j6IkXL9Zpv-35SuWjwy42MjUoMKG-NnJqbmoDS-EQOUiS7DhgO7IOjGo24Jjef1hgD3WuK21WHKYgMo6ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است
بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛ سالانه نزدیک به 6 میلیون کانتینر و تا 70 میلیون تن کالا از آن عبور می‌کند. این بندر مستقیماً به شبکه ملی راه‌آهن و بزرگراه‌های ایران متصل است و همین اتصال، آن را به مسیر اصلی جابه‌جایی تدارکات نظامی، سوخت، نیرو و کالای تجاری میان مرکز ایران و کرانه جنوبی تبدیل کرده است. موقعیت مسلط بندرعباس بر شمال تنگه هرمز نیز دروازه ایران به مهم‌ترین گلوگاه انرژی جهان است.
اما اهمیت بندرعباس به کانتینر و اسکله ختم نمی‌شود. پالایشگاه ستاره خلیج فارس در همین منطقه مستقر است؛ بزرگ‌ترین تولیدکننده بنزین ایران که به‌تنهایی حدود ۴۰ درصد بنزین کشور را تأمین می‌کند و بزرگ‌ترین پالایشگاه میعانات گازی جهان به شمار می‌رود. پالایشگاه نفت بندرعباس نیز در کنار آن قرار دارد. افزون بر این، در دوره‌های کمبود، بخشی از بنزین وارداتی ایران هم از همین بنادر جنوبی وارد و توزیع می‌شود. به بیان دیگر، تولید سوخت، واردات سوخت و ترانزیت کالا در یک نقطه جغرافیایی واحد متمرکز شده‌اند.
همین تمرکز، شکنندگی خطرناکی می‌سازد. انفجار مهیب فروردین ۱۴۰۴ (آوریل ۲۰۲۵) در بندر شهید رجایی، که ده‌ها کشته و نزدیک به هزار زخمی بر جای گذاشت، نشان داد چگونه یک حادثه واحد می‌تواند قلب تجارت دریایی کشور را از کار بیندازد و زنجیره تأمین را در سطح ملی مختل کند.
اکنون تصور کنید ایران این بندر را از دست بدهد. پیامد آن، قطع همزمان ۸۵ درصد تجارت دریایی، توقف حدود ۴۰ درصد تولید بنزین ملی و مسدود شدن یکی از اصلی‌ترین مسیرهای واردات سوخت خواهد بود؛ ترکیبی که به بحران سوخت سراسری، اختلال در زنجیره تأمین نظامی و لجستیکی، و فلج بخش عمده‌ای از اقتصاد وابسته به واردات می‌انجامد. از دست رفتن دسترسی مطمئن به تنگه هرمز نیز اهرم راهبردی ایران را به‌شدت تضعیف می‌کند.
بندرعباس دقیقاً همان نقطه‌ای است که در آن بیشترین اهمیت و بیشترین آسیب‌پذیری به هم گره خورده‌اند و بنابراین حفظ کنترل آن برای ایران نه یک انتخاب، که یک ضرورت وجودی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SBoxxx/18955" target="_blank">📅 23:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مقامات آمریکایی نگرانند که چین یا روسیه ممکن است به ایران در حمله به اهداف ایالات متحده کمک کنند.
به گزارش وال استریت ژورنال، ایران اکنون موشک‌های مانورپذیری را با سرعت‌های بسیار بالا شلیک می‌کند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18954" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الاغ ما سالهاست در جهنم هستیم؛ دروازه هایش را بگشایی همه فرار می کنیم!</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/18953" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/18952" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTorh4265VRdVn1bze5hldwcybqU_GNdG4m2HR9aSZV6ejjC3a8m9a5S8efHEX5XdviiZueug-Bj7L3zQ_XmQsjFQ31RjEgxgSfeyU5ASuZujfGoeUIEHgbpTTiOgT3Kw9msjq6n9aBNl60lWMFzY4O-Dnei1LNoTC5V_ZExI8M2OL36kpT6lhQTtO0AjZ50ZUMYtoSY9GKgTzBR1Lhqaeg20VTXqKR1KddRfv8wGwtEg6uJj2eNCDzo375oZBcDap2S1q8CRGDAZMsNO5CCp3SnQ7K45oXpcE9lf8xEoav7-ZS2rpLQaScaZi0P9MXPfNzlbFahuNMRrQW23e2I4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع آمریکا در واکنش به کشته شدن دو سرباز آمریکایی:
«خدا نگهدار قهرمانان. فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند.»</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18951" target="_blank">📅 22:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کریمه؛ از ویترین پیروزی پوتین تا آسیب‌پذیرترین جبهه روسیه
حملات مداوم اوکراین، کریمه را از نماد اقتدار روسیه به یکی از ناامن‌ترین مناطق تحت کنترل مسکو تبدیل کرده است. منطقه‌ای که زمانی مقصد گردشگران بود، امروز تقریباً هر شب هدف پهپادها قرار می‌گیرد؛ تا جایی که مقامات محلی برای جلوگیری از ایجاد وحشت و اختلال در فصل گردشگری، سامانه‌های هشدار هوایی را عملاً غیرفعال کرده‌اند. در بیشتر نقاط شبه‌جزیره، حملات به پایگاه‌های نظامی، زیرساخت‌های انرژی، خطوط راه‌آهن و مراکز لجستیکی به بخشی از زندگی روزمره تبدیل شده است.
تمرکز اوکراین بر قطع شریان‌های تدارکاتی، فشار بی‌سابقه‌ای بر کریمه وارد کرده است. حمله به پایانه نفتی کرچ، آسیب به کشتی‌های باری و تهدید کریدور زمینی از جنوب اوکراین، انتقال سوخت و تجهیزات را دشوار کرده است. خاموشی‌های گسترده، محدودیت فروش بنزین و اختلال در تأمین کالاها، نشانه‌هایی از فرسایش توان لجستیکی روسیه در این منطقه هستند. همزمان، پهپادهای اوکراینی پالایشگاه‌ها و تأسیسات نفتی در عمق خاک روسیه، از جمله اطراف مسکو، را نیز هدف قرار داده‌اند و بحران سوخت را تشدید کرده‌اند.
اهمیت کریمه برای کرملین تنها نظامی نیست؛ این شبه‌جزیره مهم‌ترین دستاورد سیاسی ولادیمیر پوتین پس از الحاق در سال ۲۰۱۴ محسوب می‌شود و جایگاه ویژه‌ای در روایت ملی‌گرایانه روسیه دارد. با این حال، افزایش ناامنی، کاهش اعتماد مردم به توانایی دولت در حفاظت از منطقه و مهاجرت تدریجی خانواده‌های مرفه، نشان می‌دهد که هزینه‌های جنگ به قلب این نماد سیاسی رسیده است.
با وجود این، نشانه‌ای از تغییر گسترده وفاداری ساکنان به روسیه دیده نمی‌شود. بسیاری از مردم، به‌ویژه در سایه تبلیغات گسترده امنیتی و نگرانی از برخورد احتمالی اوکراین، همچنان بازگشت حاکمیت کی‌یف را تهدیدی برای خود می‌دانند. اما آنچه بیش از هر چیز در کریمه و حتی سراسر روسیه به چشم می‌آید، خستگی عمومی از جنگی است که پس از سال‌ها نبرد، هنوز چشم‌انداز روشنی برای پایان یا پیروزی آن وجود ندارد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18950" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC7kg_KJb6Bu5bAYEFfqo89AkCxZjy_1SPWXotiFADc_C6QFQdriyYRgCpmSM--bPe1hNKLF3HZ_IaWRS0dCVt4n0aWnQjxcEDgd4Wwwti9SfBOZnHFyhmS3sDpChakqvW6yh-I9Bj81I8T9lmAMyN-VE9Ltz3VVmmWvrzwLfYQocBV38kJYVEFm92LmR-Xyv2Oo2mLeNEJpuknrcalqmzig4gCUMK95NbQCI-7aB6OqKWublGiK-86J_u6efd3fD9oxC4YQoEOCKKeG-RQCUHcUuWRnG9zArmWBWykmzCTRSr-80NZ6jVdy1loWEq167k25Q8JusVRn2vweu_CcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید گدبان سفیر اسرائیل در سازمان ملل:
موج آهنین درحال برخواستن است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18949" target="_blank">📅 21:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8ou3Mp_83-w4bMLEds0max23nOkoaYI7ouy9Xmbhzf5_2O-M8FiS9UCQg-EcMOolT8AVlSGREI_AAW2LWhBP_00FG_zuoIkib0zOYZ9BO0D4ndnMbbYBoKxuqLVb8NrFskkF6TNhd1SXqD5-AQQRy_Ddh1UvlvAMnQOfHjtBY12deHdC53Fcm-E6RgQg8GDx3sQ1AdHSxHLAZHyZ6OSRsAsA9mtgjs7s46lwnlBMgN3GP8vIxgG14LKJur7WsZeFYDRiU87Tva6QpNC4heHvmsCq2YTYs6-T4TqQP_wRfPX_L8zuPQjKKqyOkhCHUm4Cm7A3qOV61HW-Uz-baOOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است سپاه پاسداران را مانند داعش نابود کنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، در اظهاراتی تازه احتمال اقدام نظامی گسترده علیه سپاه پاسداران انقلاب اسلامی را رد نکرده و گفته است که واشنگتن ممکن است این نهاد را «مانند داعش از بین ببرد». این سخنان در شرایطی مطرح می‌شود که درگیری میان آمریکا و ایران پس از فروپاشی آتش‌بس دوباره شدت گرفته و دو طرف وارد مرحله‌ای از حملات متقابل شده‌اند. (
Time
)
ترامپ در پاسخ به پرسشی درباره اینکه آیا ممکن است سپاه را همانند داعش هدف قرار دهد، گفت که «خواهیم دید چه اتفاقی می‌افتد». او همچنین مدعی شد که ایران بار دیگر خواهان مذاکره شده است، اما همزمان تأکید کرد که واشنگتن حاضر نیست بدون تغییر رفتار تهران، مسیر گفت‌وگو را ادامه دهد.
سپاه پاسداران یکی از مهم‌ترین ستون‌های ساختار قدرت جمهوری اسلامی محسوب می‌شود. این نهاد علاوه بر نقش نظامی، در حوزه‌های امنیت داخلی، برنامه موشکی، فعالیت‌های منطقه‌ای و شبکه نیروهای هم‌پیمان ایران در خاورمیانه نقش گسترده‌ای دارد. آمریکا در سال ۲۰۱۹ سپاه را در فهرست سازمان‌های تروریستی خارجی قرار داد.
مقایسه سپاه با داعش از سوی ترامپ نشان‌دهنده تغییر احتمالی در سطح اهداف جنگی آمریکا است. عملیات علیه داعش عمدتاً با هدف نابودی یک گروه شبه‌نظامی فراملی انجام شد، اما سپاه بخشی از ساختار رسمی حکومت ایران است؛ بنابراین هرگونه تلاش برای «نابودی» آن، می‌تواند به معنای رویارویی مستقیم با یکی از پایه‌های اصلی جمهوری اسلامی و افزایش شدید خطر گسترش جنگ باشد.
اظهارات ترامپ در حالی بیان شده که آمریکا حملات خود علیه اهداف نظامی ایران را افزایش داده و اعلام کرده است که مراکز فرماندهی، سامانه‌های پدافندی، توان موشکی و پهپادی و زیرساخت‌های مرتبط با تهدید علیه کشتیرانی در تنگه هرمز را هدف قرار داده است. ایران نیز در واکنش، حملاتی علیه مواضع آمریکا و متحدانش در منطقه انجام داده است.
از نگاه تحلیلگران، تهدید علیه سپاه نشان می‌دهد که اختلاف میان تهران و واشنگتن دیگر تنها حول موضوعاتی مانند برنامه هسته‌ای یا تحریم‌ها نیست، بلکه به سمت یک رویارویی ساختاری درباره نقش منطقه‌ای ایران و معماری امنیتی خاورمیانه حرکت کرده است.
در صورت عملی شدن چنین رویکردی، آمریکا با یک انتخاب بسیار پرهزینه روبه‌رو خواهد شد: تلاش برای ضربه زدن به مهم‌ترین نهاد نظامی ایران، بدون آنکه تضمینی برای فروپاشی ساختار قدرت تهران یا پایان درگیری وجود داشته باشد.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/18948" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAwC1ImZu1OhAGbHxg5lfpGnQUFnkLVAdtfmT10fMVLyp1gJ2Gfbbae3fSnbTYfToYgnIkJOtd69eq5k4HabnV6O-j74_JqpsulQZ_-6kbvysnxj_NtNq-mf1vnPDZunfb7X_6rHWHBp2BJ0dcyiHQ4n35e_Gbv3Mz8MvFpfud4iU1lr5S6JroagH8LiKGnKZQTZR3mv71Q8Q4uxlHxg21fmI7wLogVvbg-RyAwExc1_0ZsIlPHgFvvIixXyIXmOI74Q2azBjkqfi7JsiZ7h4Y42JWTjs2LUEH_MXT9fXCHAoZ4lcU97SyJUCK5Jtw9_AL_C-NNsC_wL1cxa7jCM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/18947" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18946" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKogY5Zb33aE8xI9iTK0mrlpzSknFWX8cuQRypDPoGFrrFGdz9WpCufDz6_GwmO0Ky5xD7vXZXQlsQ4eD4S5SQtNROwCWeVLT2O-exXqfxnHvQyPLL5n33bPSQuF0nH93-Zlpr8lxU6r_SIRfZB5ayIedx0nIMc_nuYhoVSU18ohczKX1fNM7y4hp4V0JOvEF-H-os2IsdZXfZOxV1vrMPHqyutBCWLHq09kO7L3UIxA0zA_Ux2EotqUo0flVcGb8yb0-3bBHVSqbxocvXUvpWgwaHpzDZtW_F5zqkBVzZoTiaKGbIENJvXs68-2QtHq0KK4lbF9RmbqvXG_3vDTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SBoxxx/18945" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18944" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
