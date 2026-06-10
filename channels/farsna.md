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
<img src="https://cdn4.telesco.pe/file/qnH6093dB_hs3kqc-xb5tae1zdvzf8ZwKfmLvvu3f1cuy2soWhVY4ETnxN8aUCZujewDMFkJsTdLhXRfJYzyANT0so94L6_czv7SBgI0EcioNjzUS79gFwyPBmXEF2qVGtd56_U53fsuOTlrE1rO9oBUL7n_QCiqxvKMIt1Q9ehHhPjnvBVm2RrakBpY7Fdt-8WjVw_Rx-q10o_Ns4aFH-bNugGMvms0FEo-KXQPNNjkZ1pjIKpIbrgkC0ImQ4cU_f8CHObHXL8k5Km3Q3Si-8RQsPGOjiqq2zsFR7-XiF8THE8CsSRtP_zImB6Uazf_FfeNiW2g1GjlrDWGednmiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 06:07:11</div>
<hr>

<div class="tg-post" id="msg-441067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
آسمان اردن پس از حملۀ موشکی ایران به پایگاه هوایی «موفق‌السلطی» و تلاش‌های ناموفق آمریکا برای رهگیری موشک‌ها
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/441067" target="_blank">📅 06:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ۴ هدف مهم از جمله آشیانه‌های جنگنده های F35 در پایگاه هوایی و مرکز فرماندهی کنترل ارتش کودک‌کش آمریکا در الازرق اردن مورد هدف قرار گرفت و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/441066" target="_blank">📅 05:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441065">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: ۴ هدف مهم از جمله آشیانه‌های جنگنده های F35 در پایگاه هوایی و مرکز فرماندهی کنترل ارتش کودک‌کش آمریکا در الازرق اردن مورد هدف قرار گرفت و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/441065" target="_blank">📅 05:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/441064" target="_blank">📅 05:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/441063" target="_blank">📅 05:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441062">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ef1e3afd.mp4?token=WaekKBgrmElh80WBxUEjK9B4PZYKC4j2ve960A_-LXW2-axk0TToE-UsZE_xLUwOeGkm45GlQK2LNJuFOFHPpM1-CoDdu8Mk-eQ1FRMQw4hMPy3SrphTNvot2ftQ5vVjUKkGbGYTYQDoYNurr_Se4daLwciiTIv8qhkzV1NJnwDdyFB1HuOCaHKCX8Hx0R85Xd84gX_yASsyW-bcrvXER79vvlQVrnFy1fG4FqOlLazTFqPXfJ96c5DOR3ErKMEukD7Zo7QBc3srk2_0KFktGDLDyyE4Zf7zuH7zmwSWNBPWFBxMEYzQkPUroIbcqntQHRqOa0I0oEcJiB49QStQoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ef1e3afd.mp4?token=WaekKBgrmElh80WBxUEjK9B4PZYKC4j2ve960A_-LXW2-axk0TToE-UsZE_xLUwOeGkm45GlQK2LNJuFOFHPpM1-CoDdu8Mk-eQ1FRMQw4hMPy3SrphTNvot2ftQ5vVjUKkGbGYTYQDoYNurr_Se4daLwciiTIv8qhkzV1NJnwDdyFB1HuOCaHKCX8Hx0R85Xd84gX_yASsyW-bcrvXER79vvlQVrnFy1fG4FqOlLazTFqPXfJ96c5DOR3ErKMEukD7Zo7QBc3srk2_0KFktGDLDyyE4Zf7zuH7zmwSWNBPWFBxMEYzQkPUroIbcqntQHRqOa0I0oEcJiB49QStQoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: ناوگان پنجم دریایی آمریکا در بحرین هدف حملۀ پهپادی قرار گرفت</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/441062" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441060">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد
.
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/441060" target="_blank">📅 05:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441059">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/441059" target="_blank">📅 05:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/441058" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441057">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
آژیرهای خطر در بحرین فعال شد
🔹
منابع عربی از فعال‌شدن آژیرهای هشدار در بحرین، در پی واکنش موشکی ایران به نقض آتش‌بس توسط آمریکا خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/441057" target="_blank">📅 05:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441056">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
روابط‌عمومی ارتش: در ادامۀ عملیات مقابله با شرارت‌ها و مزاحمت‌های ارتش تروریستی آمریکا برای ساکنان جنوب کشور، بامداد امروز، ارتش جمهوری اسلامی ایران در اقدامی متقابل، با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را در بحرین آماج حملات خود قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/441056" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441055">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در منطقه مورد حملۀ مشترک ارتش و سپاه قرار گرفت
🔹
قرارگاه مرکزی حضرت خاتم الانبیا(ص): در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانۀ واهی سقوط بالگرد خود، برخی از پایگاه‌های آمریکا در منطقه هدف هجوم قدرتمند ارتش قهرمان جمهوری اسلامی و دلاورمردان سپاه پاسداران انقلاب اسلامی قرار گرفت
🔹
ارتش جنایتکار آمریکا بداند در صورت تکرار تعرض به جمهوری اسلامی ایران، حملات سهمگین و گسترده تر علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/441055" target="_blank">📅 04:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441054">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
🔹
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/441054" target="_blank">📅 04:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441053">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سپاه: ناوگان پنجم دریایی آمریکا در بحرین هدف حملۀ پهپادی قرار گرفت
🔹
روابط عمومی سپاه پاسداران: رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک، سیریک و قشم را مورد حمله قرار داد که به یک دکل مخابراتی در سیریک خساراتی وارد آمد و دو مخزن آب بخش بمانی این شهرستان منهدم شد.
🔹
در پاسخ به این حرکت شرارت آمیز دشمن، رزمندگان نیروی دریایی سپاه ساعت ۲:۳۰ دقیقه بامداد ناوگان پنجم دریایی بحرین و پایگاه علی السالم کویت را مورد حمله پهپادی قرار دادند.
🔹
درگیری‌ها ادامه دارد و پاسداران غیور ملت ایران در حال پاسخگویی به تجاوزهای دشمن هستند و در صورت ادامه شرارت، پاسخ‌های سنگین‌تری در راه است
و ماالنصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/441053" target="_blank">📅 04:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441052">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بندرعباس
🔹
دقایقی پیش صدای چندین انفجار شدید در بندرعباس شنیده شد. هنوز محل دقیق این انفجارها مشخص نیست.
🔹
همچنین ساعتی پیش، دو مخزن آب در بخش بمانی سیریک هدف قرار گرفت و تخریب شد.
🔸
در ساعات گذشته پدافند در مناطقی از بندرعباس و شهرستان جاسک و قشم نیز فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441052" target="_blank">📅 03:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441051">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایران میزبان اجلاس خزر می‌‌شود؟
🔹
کاهش ۲۰ سانتی‌متری تراز آب دریای خزر به محور اصلی اجلاس کشورهای ساحلی تبدیل شده؛ نشستی که قرار بود با میزبانی ایران برگزار شود، اما به‌دلیل شرایط جنگی به تعویق افتاد.
🔹
لاهیجان‌زاده، معاون سازمان حفاظت محیط‌زیست در این‌باره گفت، پیشنهاد شده اجلاس یا در کشوری دیگر برگزار شود و یا به شکل برخط انجام گیرد.
🔹
وی تأکید کرد که جمهوری اسلامی ایران همچنان بر حفظ جایگاه میزبانی خود اصرار دارد و تمایلی به واگذاری این مسئولیت به کشور دیگری ندارد.
🔹
با این‌حال، اجرای هرگونه تغییر در نحوۀ برگزاری اجلاس نیازمند هماهنگی و تصمیم‌گیری مشترک میان کشورهای عضو و همچنین بررسی در وزارت امور خارجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441051" target="_blank">📅 03:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441050">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cth0OVrW6qdzxbHUPafDCRBURGFrWh6WQq3cor-o4DAoSXag-qo631rd6yVzpKx6KDYKK5u6mK2vhKZCZ9bA7XKZD-_iHH0nuVRIYfADLPsksPsva2x35HTumMSywd1_oWqNuFRJQj5Jz75qmPhrCp4-8O7kqt9kyv7zWVuXyqm1imzvqgvr-7m2cL9gvMp1lftTPWCAbGSQTxZ3qyI6vCEfOKZkg6qawimXhoXRK1vZyK44iqP-8qqYQYOaCZnX7Y6SCGk5TkvExpXdD03uFLVZoMFT1yhQlllArPohwCDEQRUubYc9zQRH8yM6-f2vFGz7UedF1k_p8eQys167Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجاوز مجدد آمریکا
به جنوب ایران
🔹
یک مقام ارشد آمریکایی در گفتگو با شبکه ۱۲ تلویزیون رژیم صهیونیستی گفت: «موج دوم حملات به ایران همین الان در حال وقوع است».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/441050" target="_blank">📅 02:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441049">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🖼
گروه هکری حنظله: آمریکایی‌ها درصورت هر اقدام علیه ایران باید جنازه سربازان خود را از مخفی‌ترین پایگاه‌های خود خارج کنند‌.  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441049" target="_blank">📅 02:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp8B2tU8nVa1UeYD9AM_0toJ0bt0ZIx_JFTqqlq1jf6zX-4ekzTvJ1qfJIuJToilDpKDHbAL8yBUbLW6gyP3asG48gBMMPMWuzdjTuaBNEKDBE0F9zF3D2cB591dbZSHeVl-1ql2zhiqVo20cp1tnMcFppBJprw0BQuoCfTxOWlN-Q-vfhF53TgJhPlQLA59OQ4TzNK73WUa5zH56XzhB5UzR1yyIq6dDGd4xD26LJEq3SqPuyii5ISbW_kuI6Ld6PkaYrwvqicW5UZhPM9houtcP00RfOkRs-4-T-ehSGvF_9PoPwBHGUAerbI3tC37IunmccpW3GZkxIFzaupv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: اگر می‌خواهید در امان باشید بهتر است منطقۀ ما را ترک کنید
🔹
با وجود شکست در میدان نبرد، ایالات متحده یک‌بار دیگر تصمیم گرفت عزم ما را آزمایش کند. نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نمی‌گذارند.
🔹
اگر می‌خواهید در امان باشید بهتر است منطقۀ ما را ترک کنید.
🔹
تاریخ خلیج‌فارس در مورد سرنوشت شوم بیگانگان متجاوز داستان‌های زیادی دارد.
🔹
هرمز در آب‌های بین‌المللی قرار ندارد، بلکه میان ایران و عمان مشترک است و هزاران مایل از سواحل ایالات متحده فاصله دارد. مرزهای دریایی کاملاً روشن و بدون ابهام هستند.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/441048" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef134277c9.mp4?token=eKfL3NIlihzplI4ROnTz_Vy0Q8APMW4ZEqaVWhiUi92UeABiMRezb14vhxMSVJ8EGNvetU_KKXf8bBkJxcDUtusY-cWxxlpLjSU5gEigSsKvVyJDnAIruQmKlMPa0Lci12odQdpEDV5JdR8roQ-hqgE_-3Imoi4hjUuiqTbL2Uq1eepFnviCVuyX6amgCFWBI65Q8-RLehUkLHc22EtSC8qOHHXYNqh06ngo6ryI6vnh4v5gF3-RFlWjQr7_18qeuwtYjFTMQNmXc2FRKCHa7wnabyNRXrzwYmwM6EKB4np9qEsvUrwVqHYZuHxkx_zq96KxYpl3CrzMI3Kilz9uPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef134277c9.mp4?token=eKfL3NIlihzplI4ROnTz_Vy0Q8APMW4ZEqaVWhiUi92UeABiMRezb14vhxMSVJ8EGNvetU_KKXf8bBkJxcDUtusY-cWxxlpLjSU5gEigSsKvVyJDnAIruQmKlMPa0Lci12odQdpEDV5JdR8roQ-hqgE_-3Imoi4hjUuiqTbL2Uq1eepFnviCVuyX6amgCFWBI65Q8-RLehUkLHc22EtSC8qOHHXYNqh06ngo6ryI6vnh4v5gF3-RFlWjQr7_18qeuwtYjFTMQNmXc2FRKCHa7wnabyNRXrzwYmwM6EKB4np9qEsvUrwVqHYZuHxkx_zq96KxYpl3CrzMI3Kilz9uPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در مناطقی از هرمزگان
🔹
دقایقی پیش صدای چند انفجار در مناطق شرقی هرمزگان از جمله در کوهستک و سیریک و میناب شنیده شد.
🔹
هنوز منشأ و محل دقیق این انفجارها مشخص نیست اما منابع محلی از فعالیت پدافند در برخی نقاط استان نیز خبر می‌دهند.
🔹
سازمان…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441047" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441045">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_oNrdFMuaX_4wVDM8myGNpM32NSmIRU7VypUmiflPrjd-Ytfto-1TOE7Hvf5eWMVKmyDp5BeDTQEAaykUt3PwNRVGfeq8oeMajPoVLSgZO8jiNvh_d9PETTKCSolD9_S7pz6yGYN2PmM4-d1yDtNzdvJ5DIUDwVITPZKRnDzvTBvWanMz2bj7v-PLZ-EQ1CgEPPLfYWJceJFueNEPL7_AHfWDTuVkRtTcyCF5EnATY48UxPRTVZxFAWu9soMe5KZyG-u5Reo-dtWpyOdaA9EKYuR7r-uToZRuXui_SSSBiPyJoi-M6F2nmgUIIzvY96wH0V1k8U8l2lC95ymuft9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ عراقچی به شورای حکام درباره پیش‌نویس قطعنامۀ ضد ایرانی
🔹
وزیر امور خارجۀ ایران در نامه‌ای به اعضای شورای حکام، پیش‌نویس قطعنامۀ ارائه‌ شده از سوی آمریکا و ۳ کشور اروپایی را اقدامی سیاسی و از روی بدنیتی خواند و از اعضا خواست اجازه ندهند آژانس بار دیگر به ابزار سیاسی آمریکا تبدیل شود.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441045" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441044">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پرواز جنگنده‌های صهیونیستی برفراز بیروت
🔹
منابع لبنانی از پرواز هواپیماهای جنگی با سرعت زیاد برفراز پایتخت لبنان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/441044" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در مناطقی از هرمزگان
🔹
دقایقی پیش صدای چند انفجار در مناطق شرقی هرمزگان از جمله در کوهستک و سیریک و میناب شنیده شد.
🔹
هنوز منشأ و محل دقیق این انفجارها مشخص نیست اما منابع محلی از فعالیت پدافند در برخی نقاط استان نیز خبر می‌دهند.
🔹
سازمان تروریستی سنتکام دقایقی پیش اعلام کرد که ارتش آمریکا حملاتی را در ایران، در پاسخ به سرنگونی هلیکوپتر آپاچی آغاز کرده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/441042" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: حادثه بالگرد آپاچی موضوع جدی نیست
🔹
ترامپ به وال‌استریت ژورنال: حادثه هلیکوپتر آپاچی موضوع جدی نیست و خلبانان سالم هستند. @Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/441041" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441035">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc9_MU_A4Hc92XRMALele2PBfgxVZihIHH9YOfVKLJSYPdo3A7rrmCsHUUMIulgccVQkvcYxPx6bKMIavXlhJdm-pvB5b1F16ChjpvDpl9D6oY--38tB9cI6bSYnLaRof58rRl_mhAANYS8JcAZNFK3hV09b9KtluJteBEWFd5n_uU5j8NfRf-HZGJsrkXgZLHxik-lgn1kygjs1dJCpe2bGdtAIefrs6IH-Pgfu3LNtvdegFoELDHa0SG7_byvaEww_eYAWkBxjfLuqlzHr8p3Jr9OjQnIT09f_J4et82xfwlTsETywp64tblTJfq1ZSpPcdW-O20oibEL7FdsBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwaTLtho6hKb1O7loPyDginaRt3GqPp7UlEvFKcEA5aMZpr2lnaRPfBd4KtK0xfix2IjO2QcXidIDOTQjDn1d9q7oDAE0FhYmHZAWipx_iRx876Ie5Jln9cvefOXgQQUSHdn1RsIvjmo84schqKf3vP7h_RlmZbry5rGkJ3HKTsn0EWE-GPRI43o5pXPc_tBnUCn29k4s1HRWNjviNcZOkYkHGRm4gqJnF1kG9RjjFlvW3kdRIj9SfDNaRy6OemyIegeZCIhcShGCnpHIFpYLnC4qG4HBsc0ubJhw1WFUOzgKtfKznQ_TdF0hUy9kXHvScb2hddJ9n-d7J4un8tQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jK9ZfQHgWy5sjbcTqQlixN3e8Ozc5-ac4VNNNtK4wYbu0NXYkIPlKyXbu69fpRcgYFfUS7F3P4FdNkogdPIEJ6SA3uh5Cm1FAdVyv4UYwhN5NIlY_Xu1IDkt-xZNGpxybEJP_3bTcrOero6Y2ygEBNe1GuMSgp96Wj_rLJVxBZGrcxqWxKk9NQhIHWB9al6sDAs-3caeF7DNvG7CXB6wFcUdj6blFirk7D6TsIqtzbm-TkBNQ4KQThQU-4K89z6Rw_bkR6onun_osdjlpu8P8v1B9SBfoEOD_CfZ_9WhkeaxHONMy9WclTPsMuiDdUdvWHJOLLwc9G2nsKVfnXQfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F07O1RYSYkx18BmAIYM8_9tF-F5EtPhS1_QCED331HFFuxgkNnreQoXSPjXVck1Ph3YZ_pphmuVEdtN86KtQJV-reDWWf58cpv39Pl26lWy85xmdaEbk1XUzrZnyAEg4TuJLEkUpBIykJUnhnCAqgQ0G1bVgONihtmgWOQoOIQQdBuJxLkekYSUGvILuWCJM1o0dkvpcPCI8oI_MUBRuKWYxSWjnZbnWgZadIpN3rStBPZIpA1lkH5xIQz5vPub5_sgjvqGpcaTX72WfvcYf_sUeBG-XuH0qotZIR9HbeJqXEiRG1s_0H7DxvFdC6aAgNVhFjOLKk3WZGVZotygbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHA6ZZevjiaWaxYTcutrI_KR0pyoCJuUpcyeancggpuGDh6ceEU52fI25JtoFy4BYYsC0zvIZUHC-_d2nynCrVE_wuOov506PnWLKaEow96c3umqCvqk_8LXlBb7BzhsDAF-UJhc1CSDGHbqlVDuRsHs2jHGNYQk90_OFDvc2Zq5e4LJJqrJe2pIlgddgrwZHNkeCAmH9hHmOY0-xKoXlbp8W9OGjIb97paSLgJf_407RXQM_D_6-U5JX9cZzwCQr0cPfPslBWVOjQPvVSASt8w2Ii8PCtWOihM7UEi4Iikuudc-6WeS-lndcWy4g-QVkRZf4sNi8VtJksYw75j1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KER1S3IcwpY8WQOT7yaVGEbbrs4ZHk1dqURCsTP5J8RGZteoqNI9_YO5TC0_t8l6CgjI1jVkw5941XicTV3RnJv79471XeiOShjzMO5F3VM2AwJLceI4gwtjDdBw6Dh_wB226PPIQ6mP2dOzmwgVd72xYOSfaoMcB64J-dEOa3Awu4TF5arfdli-NCKQuVCUfIvWWEMC0MwO8ijoI1cTeq09tyJiu9NLxbi3SXjA4cHfIBhH8tt4rYBj2XEBT15rpPF2bi56IS4pxxSrX90EvbuqX3XdxEUkWMXTFoHiLGBfKUSkuEmErPzhEKpVMsqCu8Yg8J3fTiAvRi2it7TFoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/441035" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLp8b1U3KDs1NSfi2pSw_XL_dJa13JS4EUKV_o_LcEQxk_sE2BRy6Kr3u2_lLZr5kWwLY4vFEMnoSxW0AcJEw7BpfZ06sO_ufHDL6EIwVoRfruyC8KDUAeyFhhKb6d7QUYekV4j9_KjysPTuL343fhWaV5K6lJyv0OMkaIx7hqX_sD7LwTssivzz0BwxJKmqhCHkVDCUYiJiWvJ9MDF5GSpezLgnG3vESwFqvq_-O21t-u349l1Oi1Tlhezo1J1VzTR4UUqypZnzY3S2ap5e5R1Xz2o4i1WYTiumq06-if0gxDBH6o1Ap4MVnTyJEs7tQJkhPCe4wAfenrx3eHDu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stGIGQWOWDSjelp_4VeYYuPES-l1Iiwzo8N9s0bNgU0q9VPyoVRdV71ZcTokdDjbHcRP6xDkCKsKXVNuSkhh4SChs73t6HvtU6GLD66PXh8lIGf6DS8r0drjpjVDjbBWmIeQdXhJuaE2y_dFmKEdmEeAShXm-MQLSoezZ7-8TibXhtLJ-PPKIwrS0J-Sj9_RAJPLY41kM-gSn6ik48FDEn_jPftRjNdcvmAWKOYlN0VDdBs0PeEUPtvbp2bY4p2gxwwfGBFp1K3RZijDc981JsRVIJK8yEFZrofCH9xrlHSeaQTh025ENOWlUGN2rPTfDGi0I3h1_SN-ouh3HW3Oqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dp2IfYxtXG0ayADCZsm_eFkdCsaCEnL-RdEe09AycMYLjxevDRLp2j5CyuPmvaqNAKIs3-CNq6zD3y9oM3gpd8jEOp5aODbe3niKwTJYfmqPB4swDGVrDeh6qHS_XErCQXnbvpz9PfqEbmRIXb0k4RjTM3JpylwKUMk2paAA0oNKZWxCMhQhJndXrOGmTRfkXwM_IEHoxcRspRCxv1nGubwMGDotTjR1arMzAwRvn6lXoQ3LG9cXc-PqPZaQNe1axdhuvmU9Xfn6cX2Iu-PGMl2bqVUx1qCLWiRiDgJtTonua9uj8BWX1vyjPPNmkxAedh_CK6Ym3OVwc-YecNNzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4axi7XzmYmBNNYGzDKRjSW1aUDJmbpkZxyFEL6Q4VzhvY8v4Dd7DT3-WSKDOVo6iYdqTx0sAJW8Oc4uen3Hzt89wd5T-QgnpOxo-ZzGmRbiVZPbynsfRSG2-0q7by8he71MNakud4xPRIiHIzpXGwhvv0R2T2_pJ4olElcaG4qTyl9ed81WCYXNfOcbFnzeMxgM-Uuqy4KfqB9TbpJANS4VvwfB7Jqkf_CYbSFrVj2Dn9kntK37uivV9PE8en1AKU-JkZdsjdMexmbqQIbjNhwmpO1yado27fz5bdJ-Jpo5NP2rh2TuOXiCPdtyPhYPPb2BRNvxq1XQHLxQM5_ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMONUT2gE3ZccucnprtFO0t55mYlgKhd8CPJow9ooYzFsGP5EjyKVMnCSgPs3uaVEX7KVfZhTmFBQs_LzlfLEC25T_EiHkKiFoJlpR7MWjrRBYMTJcBc680s-_9t1o6yAHe43UuF9Ep8zo2yXvmE_Iyf57h8UXRmAuFM0yslez4rO_AkmOIku6fXSkPO1qs--TAw5m1RvOeqiKiKbQUO4C80Cd0fdsx1GiRuChsJKkPtwhyVVdCiUJsIY67PGT6Zw2BsmIrVwYcfH5chkeq8zz_3N0ScshS5i4Y5EvXV0urFqMTnDlEIxdg9ibjiHT6BfT3XND55yGooScxvhFHj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvNPnkuKbwbYZ6f0Gg8LwBPyncciBEKN3DsC7xXgPBw5BJvjsEm0uJqZvlL7WZ9HXo72kQGiQSUOMoDhSEP51O9JPGZd2dTZ1NDIk6Mvsd_pDbLt9MTR-_ZsBRk8jqiwcQD3xZUwmsBeAEd0zs2eP3iyUNytmwcuiVvqzDjb7VwM7Uu8T4-vLiouPrSm4pLkpePNy9LlLegqPFSUtDgWntHDHMpnbcQH1xvssdJQXrmAvIq2FmU16GwdOISsbvdeFqWFitbx8bJuM3eHnMwfN64GYYG3X2oinlRhu_wol1fhM1qmA5oeQfJafJcIwcu77ahfSeQyI84O26yoGfSLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJBgc4If1IQ0Xy7-dDBDxKGjt6rOaRV4vlxwoYyMGZajYyspxABl07VgchFxlTZvrxorm46ZLqFEC5huY5H9g1xAiCsnMCJfBkgGcgWwjkyhfOjn5g74Lj3EatB-J8kPCq-366aNXsZ2iZnvgAp-xUXyhDB8WQ_bX49gfq4wlzsLDy8TugN0Cr2c_WjLHjmzLDQIqVqyGGDJRKE2I642_t-eiete6XJpSbiaYsrYDmt9SXIqxChzghJTlwcAVJTy7u1g2IFVdf30P37hi5kSaph39UHIRn7cfF9MLq_HDpcyxfaPN-cuZklmlfVB6aNJX1egVy8o_My7tvI12osZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Or-UNRBmTn80WOqKhb38QB6N1L77VDx_kRuOebo6lQtI38Tvd2CamNd85kdrvH83gQazgm8VSxO9gA55U3CNNiznAEq1UJms8EdfYU0zhe5BuGGabrAq2j2QSMqLNyxKNmNLuByMhDCbvuRsToah0BtniKcUvp5MECO015r0aINMcu6l79Mt21zR7pMNpIkMlRXBA-WiHugy8lIesa3fwXw9kMq-eM2codFJV9ZA-W4fCh8iEvDT96bDzVm2h0V5Db6-TnVk23jM4imL5wvTfOFjh-HSHBd9cLQstOSsjL3Q80xRqCd-aY4N_P75X6OcmscxXtpNEs0riAThpjwEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxfcdlAHtXRVeMAfS-vEmVh0bvTLNOAy5vp7DYGYJPsMSfQhj3sy6wf_ZD3tSnR15tGl0VoLRRK3xn1CsP-LHvkD_y9rRaQxzFgARrTD__1m8XBAWBnCG348ESpnGH3Y7Kf7K8hUy_8O9JERb-1EB4O6tD8sb4K0ecsK1aLb7KmKkgpVwBDjrKq_s8QYVqfACvXkxAXB_xppn89S_Xh7Ds-ZsI84kTHyiUbe4rihLAgqjq4G_quYRlHiKu2Q0JWOix4eRaSqDXU4XR4j-Hc99RHnUKwLCgIeh4NtJWrICjZ3nvyrHDF8F-vbXPY6FGy6x7vou35v48AgZ0tbpG4ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d72ZfOP5zP93lCLDe5sZvxaQrzdy06DedGeJ_tG0u2-BDU4VHbFMUBmkpdsyA2FWwRbs3dZaKWq88JnZd8c6X5tdTs8sCouXqlGTiTxhf8HK1GVAeebdQC1emTFABZ3Djo7vJ-W77GLJpVzyw5cQXn7x_Bj6b_AeHPJIctBYq2MAivqzc09Hiv90WEOuadYCa_xofAJXagwo0m9mPLmGhWj50y_gU07ty--DtQzRGP5AAov7ZW0ukl9OEHtUgh5se7MrljlC6JP6EZ_kNMhvRDURwq5GEpasexw6lz6PSY_py9oYAulH0sm-ULrYPHjrP5afNC3MElGh_0SFDb3mTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/441025" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441024">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شلیک موشک از جنوب لبنان به مواضع صهیونیست‌ها
🔹
رسانه‌های صهیونیستی می‌گویند در پی شلیک چندین موشک از جنوب لبنان به سمت شهرک‌های غصبی در شمال فلسطین اشغالی، آژیرهای هشدار فعال شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/441024" target="_blank">📅 00:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441023">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reBNlBhimjRez7RZNxV8hQYts4vjNgb3jYrjCYI0N6WyjP_B7RrdeT-LemZjccF5621rfFXvEc7LwomLhE-7GbKMsXnbvyMNnSD8wknR3THLeTgR1nOT3JaWpV4G_BTgwo1ooH3TZa-MKdE4ULiSjy_YWbuqEsZTEIs-54A_mfy_JVWXtZdLaEJR1xqkVyxoDigI0JWnqEIh5OcDArsbihIG94Boo0kigWHPEIYp2v6zkWHK6ahLLsfvF7DxxPAYyb4_tEAbNrZVeXJq1VaPedrKQjIiKlVt7mSM-0D_GTYgixjnaWY1YSpqogvr-vGymSuV5ENYyPzlM2pHsCxnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از جنوب لبنان به مواضع صهیونیست‌ها
🔹
رسانه‌های صهیونیستی می‌گویند در پی شلیک چندین موشک از جنوب لبنان به سمت شهرک‌های غصبی در شمال فلسطین اشغالی، آژیرهای هشدار فعال شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441023" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441022">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس این حکم، این دانشجو به اخراج و محرومیت از تحصیل در تمامی دانشگاه‌های کشور به‌مدت چهارسال محکوم شده است.
🔹
از جمله اتهامات مطرح‌شده علیه وی، لیدری تجمعات غیرقانونی، اخلال در نظم دانشگاه و اهانت به پرچم مقدس جمهوری اسلامی ایران و مقامات کشور عنوان شده است. پروندۀ قضایی او نیز در قوۀقضاییه درحال رسیدگی است.
🔹
همچنین برای هفت نفر دیگر نیز حکم بدوی اخراج صادر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/441022" target="_blank">📅 00:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441021">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/689b02f0cb.mp4?token=KgCNxsJQ65MP5eQekz0A734cR6NmqhWRnQiktzZWeADdjf7zFBh_JCRLT3LRG3N_rntzgQbKYAbUXZzmnYYiDH_U1nLJzz0D1oSd1w2F_ghCPEwtbhQeu9Di5qx1YuDESRmoAlV2YKnR0ftAgMI2yVbtGIw9T5loUiIUTFhkKHLwL9d_9RQIFUCc-B23zfgE1WDyAVnj4dB_-qNCYIGPk5iaWQZ4hNr9TFeLjF-Uv4ApJPc0DBw3IXutQxSpXpk3u5mjNqSXqF8JGeIDSBTnY0G63jm6m7epyyRIgAeIQIblxgYLUd4i9mtP90tl3pWVffz5oiyv9I-1JNJRFh1ICg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/689b02f0cb.mp4?token=KgCNxsJQ65MP5eQekz0A734cR6NmqhWRnQiktzZWeADdjf7zFBh_JCRLT3LRG3N_rntzgQbKYAbUXZzmnYYiDH_U1nLJzz0D1oSd1w2F_ghCPEwtbhQeu9Di5qx1YuDESRmoAlV2YKnR0ftAgMI2yVbtGIw9T5loUiIUTFhkKHLwL9d_9RQIFUCc-B23zfgE1WDyAVnj4dB_-qNCYIGPk5iaWQZ4hNr9TFeLjF-Uv4ApJPc0DBw3IXutQxSpXpk3u5mjNqSXqF8JGeIDSBTnY0G63jm6m7epyyRIgAeIQIblxgYLUd4i9mtP90tl3pWVffz5oiyv9I-1JNJRFh1ICg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران در ورزقان آذربایجان‌شرقی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/441021" target="_blank">📅 00:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaEgvyn0_49Qz62C8rDqyod2JAtZuOlppNzy7ZsV4ucWhsOq5j9G0ONNVhPKoAzVP7GwYl_ufbi58nPgGNK_rn5bACztl_ywWF3dS4EvJdoLERcLyE8iH0B0a4RAQKysmBq2REWpa7IShRxcTBUOu9cin9UhEKxtUXffSCHVjFlZ02Qe6W-_ttxW9eW7s_kM_9HKxx8GAmrnyRi9vP2BJWbPjGhqBSuLJKvZljHmXyrSqoFRndkh46iKnjSvR2_OkCaAIZHVq-mN-SrT61m2Y_9xF1W90rTMjn5USLa2Rjn2pVx6fG3DWen7J4KR5--O1uxI4i9pm-3iJM4U28GIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSaen3f9fYgcQ851K44halvUPw33N3LmHtzPAAt4FECRJeEempYUECoAxEMfuVtacF__rj9CwNnuXXobD1E2IS0lUkbKbec5NNHnIeG4xNhBFhhCyszE2K2cofTcyiVB9Nb_aN6Dlw9Ek9VpnppOnEAG6mVtjFc2ID-IvjpjKQ_RR27arbUuYCnt5PA50G_b1440A9WyDX2i8621qQNMb-oDnndu1l-YHoGC2G9Oug9ry6D-dpNmX-ZocLCfbgue0dGY1VyKeXQwGkrObq0NlqwUV7qMWhlJbhjIyAtFBQ5ph05chx-eQs7HAC0H2OJuI-f4JjPKCqcvUgkmg2zY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2tHF8PDoTgoUsigAPuKdSylu-8FMM5WixjbU3_BsfGnd5bkw-4CdfVFH9lE5m7v_j9xUETub_clNQ8ET_1J6ZWkP--w3lPRNF8nDsUEvld5vv6v7rnYvC-vwyrM1hXZznGEzXxxLMmHUJQmeCu526hoO1IXXaczeF4a6QhX_4jtICAN-PjRvR8khbk2rjD4hyV0g5pBYDugS5F5Tf2BYKZJZbYQ_EKp9RxKo2CQvh3QO4WHfp3ENRWpJN4nitTOWPJ13IhGELnbKvSrj5YatdGLoZgZA-9eWSmc2K2ljyo6FEAu1WnXj2C30dmr9kgbCV2ZZ_ruqo-nfYkG1-3HZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C983_1BEnH0sY9YLLgHodAIXVH5Nu-BBayBfGAjsfxBxvEm3f2CXExPNvWSE4lMTlGYDN1zXgNUHaWSHRIOv4ryJKjaHmye2BZjrG66InbJc41tjykthH8NAgyR6Im5YtcxrTPQEXitNiuVdcd7gCPJ51rqDTvT0eHNzdbJcdwYwol63mTnjuzBJEK0fmSvPGxSpTK6rFuaq-W3ogCyWRUZdW6p6pUPhdMeKnh5AmkUbqPpUiCuLA7UIwOC5S0n6W3CZpGQcA1jWfAD6dQgriaoktFCr-fxB__p0hjGv-TWU3DK-2hVSaRSNBotK_v6qfN82umo8WU9Zq7tTS8qVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m670SNomfj8JlnlyFXciQg-MTk56Z8Z3EZTGSKKWBQdWfAbAIRZzCcRtABbAUXeXOPgd-f5U7vQH6W2umS5VK_WHtXztHF-fYm8d7nJd9OD80Bn758nnm-k7igx1qopEvgCuGUNwHs9KjieBqSRIL4PoZsJsicXaixYX9UGPaYQvVM9e-sLCqCujM1BFqpL04i_1JhjRGbVR5Lx-YutwjzqK0w-cJ89VJBYiLUTd4hA7WmOFR6ItV71tKfDwJck4nfvyyDBRW_uTwkfjo-wb6olePRngVjkP9MfYvqHguAvdiEHuUvoWycJQfA8EOdBdrxii9Wl8oqXLX6pCZa0sNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCPORwnAPAx5OS_xtpOTQLtIF4svfH136ywULZ-lEYx0IJ0Ztam2aDd4ettf06iuscVw0Lju1RmWBcVsKVq_lgeDWUEwTcM-m5qLNrFNrF8sq9XEGeYmQ_PtbDzFtX7zOJwniHWeLwrbO_Rv9DCbZ7GqnkfuIhrErK1xSmnGyPSZP7j8kMWJq4PGNZODDiMw9uF-cWuT-8H4l1zZ0-SW6jx8VUp2qutMiTTbE867Z7QJ-pAX45pSIHSEFah3g3qIcs6RSPc8ZtgWmGOUtyZKMHC3Pui8tf1WDThH0Y-DVmJ2J0CPJbHElW-SwEfQpLR7OtOKjlPlpHiLoAvSpFs_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmqC3qwUEGreutj2VsuKvwVhI0H2LtYTXeZRj0LVHrg6elwW-gyARV_6QdkNSyyb7I-o4mOa6aoUC2tJDcb9Rc7H2PDbO4E8vWvyRzF-T6HrN_fK3m5jpVIwEFFE2pNN6krl6vv5Fbzyp6nO0xjxqmRdb3LaIA3ZDz0M4Rozv1RuvtjJKOrCj9lCPkwHVppW-lAW0nPOk4Sq_-YRXtmCBv5d564OGAo4Htms2VW5vE56qQBddd9us8FHga-8ojD3zDi8A3IPD887E-0vvJpL-c_PsX8PUe08Wg1Q2iCKREiwilrtBxbcqYe2Z-lGaDvMO-5gyZcQgy1BXI3kku0Q_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم تشییع ۲ شهید پدافند هوایی ارتش
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441014" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5sqlbh4gruNWWsbbsjHOs_dIol-Hqcgxgw5h-yZL3ZGj0bIubYJZbNTniXJvAkl5wHFqOvZJ6pVO1uRq3Kes3v_8Koinwv_0zO0P4iTC4tO-OMyMSwn_L1LdTUKl1IDgZ_rwDa8KEsWOyvSeHLQ6kNkeIxN1q8GarcrID0HTxIVcN7m-veowSiH1EJFqswj_GYGAh3taEI9m0Dp3tu9X00eM93MYvMIbRIzMoI13K9a-5_NpDQv0PhiSDjOI4Py-i2cIsp9QOGhk427KeS9C9zIQ4rfKnVXt0RJVaDtn90yEKLYd01EL2k3I0lAqQvFGMIcBX8B5rXGqS_e6l5yhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای ترامپ: ایران بالگرد ما را ساقط کرده است
🔹
ترامپ: دیشب، ایرانی‌ها یکی از بالگردهای بسیار پیشرفتهٔ آپاچی ما را درحال گشت‌زنی بر فراز تنگهٔ هرمز سرنگون کرده‌اند. آمریکا باید برحسب ضرورت به این حمله پاسخ دهد. @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/441012" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جلسه شورای امنیت با موضوع تلاش برای احیای کمیته تحریم‌ها علیه ایران
🔹
شورای امنیت سازمان ملل متحد در حال برگزاری جلسه‌ای برای بررسی احیای کمیته تحریم‌ها علیه ایران است.
🔹
این جلسه با توجه به آن برگزار می‌شود که سه کشور اروپایی مهرماه سال گذشته ساز و کار…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441011" target="_blank">📅 23:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">جلسه شورای امنیت با موضوع تلاش برای احیای کمیته تحریم‌ها علیه ایران
🔹
شورای امنیت سازمان ملل متحد در حال برگزاری جلسه‌ای برای بررسی احیای کمیته تحریم‌ها علیه ایران است.
🔹
این جلسه با توجه به آن برگزار می‌شود که سه کشور اروپایی مهرماه سال گذشته ساز و کار موسوم به مکانیسم پس‌گشت (اسنپ‌بک) را علیه ایران کلید زدند.
🔹
قبل از اجرای برجام شورای امنیت در سال ۲۰۰۶ کمیته‌ای به نام «کمیته ۱۷۳۷» تشکیل داده بود که وظایف مهمی در خصوص اجرای تحریم‌ها به عهده داشت و بدون آن اعمال محدودیت‌ها و ممنوعیت‌ها علیه ایران عملاً ممکن نبود.
🔹
نماینده روسیه در جلسه امروز با برگزاری این نشست و تلاش برای انتصاب کارشناسان مربوط به کمیته ۱۷۳۷ مخالفت کرد.
🔹
نماینده روسیه همچنین یادآوری کرد که دستور کار شورای امنیت در خصوص برنامه هسته‌ای ایران پایان یافته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441010" target="_blank">📅 23:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnftqcC-v6FaCpjOyDLYnUROUhl8JXSVgHC8vuzQ4PFQUhg2kul_Yoa_3dhcxXfUB3LpfYLenFpxSm00tHK-3pwWOcqcjfm4Dxl-rBCcC6yMgpeijq7hPTshDnXY6halTFGfePOk-CsCS285y2MMNG0TzYRILGJIkEzr4bBKgNkq-lMIDZ6qchCYsUdDNIEGUCvZJGUCYPA2bscPIgDnn2B7Gd95PcLb7hfInmhx7QqQmnrtNFek34UXauHoz9niSrzCbL3jxAcmdeJcpT44FETCKdr6z3zdp1PO57xXzhlrUX4ObjjO6ULF44HzY06YPozGSxxysVXWabad9baj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارتباطات طرح خودش دربارۀ وایت‌لیست اینترنت را فراموش کرد!
🔹
ستار هاشمی، وزیر ارتباطات، امروز در نشستی با صراحت از لیست سفید اینترنت انتقاد کرد و آن را طرحی «پیچیده از نظر فنی» و «آسیب‌زننده به نوآوری» خواند.
🔹
او تأکید کرد که با این مدل مخالف است و در بخشی از صحبت‌های خود با طنز گفت: «در جلسه با طرفداران وایت‌لیست، به آن‌ها گفتم ماستتان را بخورید».
🔸
این درحالی‌ است که بررسی‌ها نشان می‌دهد ریشۀ این طرح به مصوبه‌ای در بهمن ۱۴۰۴ بازمی‌گردد؛ جایی که بندی مربوط به وایت‌لیست اینترنت، به عنوان پیشنهاد وزارت ارتباطات ارائه و در طرح گنجانده شد؛ موضوعی که به نظر می رسد ستار هاشمی آن را فراموش کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441009" target="_blank">📅 23:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEDK3Ck344tTa6VDzb4YeiEfVg6Vxg9bNS87N_xsHhR_RrX8mzw1YzmiRh9b5R4BoMhOHd6lpoQj1uP5M-t_Pcum_ejFDRbsGdQxZpMhV0-2uHRDm51O3i3xLu-tvTLyUJfaRwABF_pk0i5AP9QrgielSMKiEk_N-kFB9Yh-aDE5h-qhcJp5U2oAKZqJkPJ0SZmLFNKp9w7uDU0PWNi-ewxGfDFm2LZYdxJuqd6kY-p0ZJbQ6hXJTbPDYtw2uCXRcElvGHoEayGieln4hlmDAp_sGj7OLKS_9FdwEFZEC32oX0n6OneM71YgHko1opKWwqXXh6K3meSvlSWlZ_Aqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیط‌زیست بخشی از منطقۀ حفاظت‌شدۀ بهرام گور را به یک معدن واگذار کرد
🔹
شورای‌عالی محیط‌زیست محدوده‌ای در ضلع شرقی و جنوبی منطقه حفاظت‌شدۀ بهرام‌گور در استان فارس را به‌دلیل آن‌چه رفع مشکلات شرکت گوهر‌زمین عنوان شده به این معدن واگذار کرد.
🔸
منطقۀ حفاظت‌شدۀ…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441008" target="_blank">📅 23:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyabvQPlEbmxdk0lv_hDt1EbVEfifZjkHuvI-vJLrLFDdtncsIZO47GZfKUSwk_9aUbiCj1_O7qiBuDFt-EhSS2cam8l9Z_Y5pgA0DpK_g6EK9IXB56lti5-OLVZd-ojxM3ihEDnQnEgEW6QkM9ayZOAh4prd1AjbH_CPScoBvQZNgiKJMhaz9R-EyZ05bSTnB_UuNF80tBOBxcRcxI44MrhTBR3ZeKwnnQ-EboXBks-bk_1Duj3t3weWTpJjjETaAFwe8nStg_yuWY62lobHINRByy5TPexb9l_0dHf_9eLuTBaex4G0VDI-D4fkJVGOOPUhjSZzKCZUUtkmqOhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdoiM2--s4XbYaFpeRMeSg7A0CSdomJfBSbYUSsInhMRXSnGY63yvZClcJBK8eQz031nXp4nfEP1x2ScR-QLrmuPS6fjX_7jf0u2FU9peTghzwx79mLig7Lh5y2BRsSdToI5189dKgWlYMbekFStP3LmkdEuwYgZTUdvK_pKZYR3m9KOpXTQkxKM9uVqOjfDqrGOlw6gVl34aZs5l3d6u_0CT8CluzXqJY9uyLsamuSfZK4-Ghsubo1xoo6CJA2sa8jT3N66LclCOMWeLaQN1TEj97ZF9KIXPIVrMOaBoXj7COawUoOVp52EoKpGDkPZLCi57z4iJkJfLI3t40B2_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جزئیات عملیات نصر ایران علیه اسرائیل
اهداف مورد هدف قرارگرفته:
🔹
پایگاه نواتیم
🔹
پایگاه طبریا
🔹
فرودگاه نظامی رامات‌دیوید
🔹
مرکز پهپادی تل‌نوف
🔸
همچنین در پاسخ به حمله به «مجتمع پتروشیمی کارون»، «مجتمع صنعتی بازان» رژیم، هدف حملات موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/441006" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441005">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43976cbf1.mp4?token=Ys1IbFHjGaON5Kfm5iX228KCaIjDAceHPcUPIX3uTQeHwAxFqRwFG-eV1nFkyWl0GZOprdwbVYsmJ3xDxwaSyZym7C1SxY-IlMJsMHVPusRNWg68tumho_yuC7gqelH9dS9RPVetuiU6fanAZlPc8PJfF2AIFgez1xFh4BPdsYXPJs9czP2T3Qt_CZz6kLf7rT1V2DtuCfy4X9EHBmbu7fdVQgfsLjkUzGrl6TycDz50-SLDl4l5b-MjiXh0gqDAO5u6KTHZA8xhLsMA4Prn2gEeR5SIXIisnQbER81OJfcax1CFOrq2js8nZ68DeSEdLm30fyJwM_Iai3Jaa7iXBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43976cbf1.mp4?token=Ys1IbFHjGaON5Kfm5iX228KCaIjDAceHPcUPIX3uTQeHwAxFqRwFG-eV1nFkyWl0GZOprdwbVYsmJ3xDxwaSyZym7C1SxY-IlMJsMHVPusRNWg68tumho_yuC7gqelH9dS9RPVetuiU6fanAZlPc8PJfF2AIFgez1xFh4BPdsYXPJs9czP2T3Qt_CZz6kLf7rT1V2DtuCfy4X9EHBmbu7fdVQgfsLjkUzGrl6TycDz50-SLDl4l5b-MjiXh0gqDAO5u6KTHZA8xhLsMA4Prn2gEeR5SIXIisnQbER81OJfcax1CFOrq2js8nZ68DeSEdLm30fyJwM_Iai3Jaa7iXBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم شهرکرد در تجمعات خیابانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441005" target="_blank">📅 23:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441004">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7d54e3d3.mp4?token=DPSs7Qx9XZ5-fYaj00-v0_ONlGO0j4nqykOJaUKT9xkACB3nGZLDfrmaQDKrp9HqKr7c2CI_HWUHbIuJqSZ3Z8AvylfZYg0x5xV-4uWLezkTzSgmHEmgVEE9Ho6ceMjKSE-hhNetboJaBc1mJ_lZqpETDjghaqoB_5RXr-b5BznFk6vWn7LprLRhP49ZdGVyGn1UdxDJK4IChP1n6DisRal3Y73TWnhLunfxAd1uPxUE_K6f_ibxFalw4j4adB4liXNG5nTiYJb0Q86zFE-_fn9KVe2D3e_UV2259LauMgEoErN1aFp72eqMDuIxmzynrinUIL0u-7LHnDGfml8ePg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7d54e3d3.mp4?token=DPSs7Qx9XZ5-fYaj00-v0_ONlGO0j4nqykOJaUKT9xkACB3nGZLDfrmaQDKrp9HqKr7c2CI_HWUHbIuJqSZ3Z8AvylfZYg0x5xV-4uWLezkTzSgmHEmgVEE9Ho6ceMjKSE-hhNetboJaBc1mJ_lZqpETDjghaqoB_5RXr-b5BznFk6vWn7LprLRhP49ZdGVyGn1UdxDJK4IChP1n6DisRal3Y73TWnhLunfxAd1uPxUE_K6f_ibxFalw4j4adB4liXNG5nTiYJb0Q86zFE-_fn9KVe2D3e_UV2259LauMgEoErN1aFp72eqMDuIxmzynrinUIL0u-7LHnDGfml8ePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با رانندۀ نیسان معروف جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441004" target="_blank">📅 23:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441003">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaZlbyeJHhv3yeKQBVN1uDE5CoIDJLCycNYu6vzhnnls2BnY0JNH8575CKsHwDNQwTNshLs131JDmhLREhXCVcn0AoGwU583UkbUfp9koLWV9vfLno_9BsFgvBk4W8-QGhIl__4BIHKwpsWULPxtsDpRJbAG-yY-BINLs4Ll4vR-4ZHptq0v9sdCZDstHwPSSUylK9KQ1_amxMLLEc2LPewO6-EWmeTzxKmWTPGLZ9RSnP3KD0sSQHlRP5KfLDjuiFzCb26GdxYY16pi6ZsaT3HNgfT2r5V5zsuIgrHMBv6StHhjvv8w5QGznaByeacBjcOyM7MnZjVyDA5oDLzDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استفادهٔ آمریکا از استارلینک در تجاوز به ایران، هند را ترساند
🔹
ایندیاتودی: هند روند صدور مجوز نهایی برای آغاز فعالیت تجاری استارلینک را متوقف کرده است.
🔹
اقدامی که به گفتهٔ منابع آگاه، مستقیماً با نگرانی‌های امنیتی ناشی از استفاده از پایانه‌های این شبکهٔ اینترنت ماهواره‌ای در جریان جنگ اخیر آمریکا علیه ایران ارتباط دارد.
🔹
مقام‌های هندی نگران هستند که استفاده از تجهیزات استارلینک در جریان تجاوز آمریکا، پرسش‌های جدی دربارهٔ میزان کنترل بر این شبکهٔ آمریکایی در شرایط بحران‌های ژئوپلیتیکی ایجاد کرده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441003" target="_blank">📅 22:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">یک منبع آگاه ادعای اسکای‌نیوز درباره پیشنهاد جدید ایران به آمریکا را تکذیب کرد
🔹
یک منبع آگاه نزدیک به تیم مذاکره کننده ایرانی در گفت‌وگو با خبرنگار سیاسی خبرگزاری فارس: پیشنهاد جدیدی از سوی ایران برای آمریکا ارسال نشده است.
🔹
اسکای نیوز امروز در خبری اعلام کرد که تهران پیش‌نویس جدیدی برای طرح صلح به واشنگتن ارسال کرده است و گزارش‌های اولیه نشان می‌دهد که طرف آمریکایی آن را «قابل قبول» می‌داند.
🔹
پیش از این هم العربیه با انتشار خبری مدعی شده بود که تهران با انتقال اورانیوم غنی شده به یک کشور ثالث موافقت کرده، که این خبر نیز از سوی منابع ایرانی تکذیب شد.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/441001" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
رسانه‌های عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441000" target="_blank">📅 22:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsDY4D_jDBcISvCSlyvBzN2SR-TUPbf5RFICSYBttc45t1OFwRuva7f4QEj8MFWox4UMLqt5JUUSJSVefDC5lWNsTqcEOjPWH7SyPBAIETWS6vBQTHrEmyZnpoX6KueyoQ2dsV2XS2EbEW5NZPpRWbWYKmsSXMPIlAwaDGDrD48yN8rQP1UGJfqRVS8lOM7wf4Ze5B_57fvGdk6rcINDCHOf2k2IwsX48tkfO9UIcaUj5FIA-xlY-eaUQn-20Zs5cQ6NYgl9JEu8I8qCXg9F3kvPnrd4D84hN3xISBRanVX2dKbyQNObl2NVhc8uvm0_v-4Z3Lt-_wb84FOi3NfQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نصف نفت ایران را خواهیم گرفت
🔹
وقتی از ترامپ در مصاحبه با ABC پرسیده شد که آیا آمریکا در بازسازی ایران پس از جنگ کمک خواهد کرد، او گفت که کمک خواهد کرد اما افزود «ما نصف نفت‌شان را خواهیم گرفت.»
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440999" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
فریاد حمایت از لبنان در ساری طنین‌انداز شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/440998" target="_blank">📅 22:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a3962773.mp4?token=lwLGHQlVjMB_BMJafKGw2GhUh-SAg08szUb47ohnohQfWJfLN0sp4eon0KkP5C4Z0xn0YgRCmpWWBiTjgke4bBPQHC22wULLA5Z7DBInrlo5aibxjYozJXqvEu_Id5dAFX63Rk3ycY1WlH4KWJnDA93F93qlohfCjk3y6Lv_u9SLTwordSKQiOg6B5M7aYZnfnRMFizypL8fBrCjbvayf0BmHmuLIMCuk_N1mhqtBJuZRDzkA7OZzI5HkZTH-MXKYc_RgpC9u2Vx3TE8LYNRdgntj-ds0UyrMhPOv3QWuxGOVErpEhvcPjhu9JpCjkEJK8NSjQilN6X8Vkz2Om_-vF3cTprVdYnH5seH5aasgWDMrybRrGnawNm6jaYtC85nGUViJIl6He0JsatSqevCP2lE5JTRLN5KbOQuhZlYDsHfSKgau0SM0xeGhELVn5mETZgj62a9PG0O4kszDiF963RqMF-TNST0SPEP6K4YnkZrR25dwRnisoxMs19Rr4PvIWroeRwZdnXmvhPo2ExsizrzaJQxwCVT5BNBe42bRxPPcdY8CLuLdv9r8iWR0gl8-XL3NJ3onrmxb5EUDEqsnBYPlpZe1G62tjkWK4q7inj2I0sIpaI5WM9Hy1cNnKYk5UJOOMKmfGisgUGx4eFtrGjzO1N45xRyHH6MUwDvMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a3962773.mp4?token=lwLGHQlVjMB_BMJafKGw2GhUh-SAg08szUb47ohnohQfWJfLN0sp4eon0KkP5C4Z0xn0YgRCmpWWBiTjgke4bBPQHC22wULLA5Z7DBInrlo5aibxjYozJXqvEu_Id5dAFX63Rk3ycY1WlH4KWJnDA93F93qlohfCjk3y6Lv_u9SLTwordSKQiOg6B5M7aYZnfnRMFizypL8fBrCjbvayf0BmHmuLIMCuk_N1mhqtBJuZRDzkA7OZzI5HkZTH-MXKYc_RgpC9u2Vx3TE8LYNRdgntj-ds0UyrMhPOv3QWuxGOVErpEhvcPjhu9JpCjkEJK8NSjQilN6X8Vkz2Om_-vF3cTprVdYnH5seH5aasgWDMrybRrGnawNm6jaYtC85nGUViJIl6He0JsatSqevCP2lE5JTRLN5KbOQuhZlYDsHfSKgau0SM0xeGhELVn5mETZgj62a9PG0O4kszDiF963RqMF-TNST0SPEP6K4YnkZrR25dwRnisoxMs19Rr4PvIWroeRwZdnXmvhPo2ExsizrzaJQxwCVT5BNBe42bRxPPcdY8CLuLdv9r8iWR0gl8-XL3NJ3onrmxb5EUDEqsnBYPlpZe1G62tjkWK4q7inj2I0sIpaI5WM9Hy1cNnKYk5UJOOMKmfGisgUGx4eFtrGjzO1N45xRyHH6MUwDvMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۱ شب ایستادگی مردم بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440997" target="_blank">📅 22:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ddc4bd412.mp4?token=HnARvtVlLm9-3gykWhPUjs36q1Fg5K7SU3mtkzAkNz0URtOhcNZpS4U5PDWSpqlxyMTQhQ4fOJGHBOmuQglphtcgCIy3wUw6iOKEszqBf3kba7-S8SukWFj8dWu_A8f9bL67YY1ej8Ioi5GNPOenk7-HJDr7CVkH6Xm1VZrX49tszh7DyV1542dnnwrUmyx46GPC0kGxyg930v6vsarMrPZMgQvb3bcnEDRfMp0tR7zM1QBO6SY9L7HmpGIN7_s9rnsb7WdECqyjVBzPps2p3WmCCtmnLb8jVElBtb4mC7ROIFaiwxbWtLCBoGXLiw-hA7OyqAxKF-z9LwkvCu6mwm7FPbcuLq9qfWRJIUPQShioz4je9dZF86yiQNpmcTM9KHrbzzne5QvrDlKhQIMxkhaYjeKkIGsTzg7DllAhCjzoubC37Cy1SGcOVGYzO89VUSDJbvCLTdATVYk95jL1PXSY-t9MTgyijEB503Q46i_CJ4EReHZOsWzgUrVmK1zp0J5BviEwv3ExeITlt36rjzZpVouytdjOL7661C2g_kKYCakyiXitBycmH3EiKFpOSaVQ6I73akMP4yZK4tgn4F4j41nIyC-w0S67y3dHfLcnRsvN666gLwnk03s4ZbCPAs7PH34VChErWIVEhwvTdkuQZoaIpkYgePv-EaduL7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ddc4bd412.mp4?token=HnARvtVlLm9-3gykWhPUjs36q1Fg5K7SU3mtkzAkNz0URtOhcNZpS4U5PDWSpqlxyMTQhQ4fOJGHBOmuQglphtcgCIy3wUw6iOKEszqBf3kba7-S8SukWFj8dWu_A8f9bL67YY1ej8Ioi5GNPOenk7-HJDr7CVkH6Xm1VZrX49tszh7DyV1542dnnwrUmyx46GPC0kGxyg930v6vsarMrPZMgQvb3bcnEDRfMp0tR7zM1QBO6SY9L7HmpGIN7_s9rnsb7WdECqyjVBzPps2p3WmCCtmnLb8jVElBtb4mC7ROIFaiwxbWtLCBoGXLiw-hA7OyqAxKF-z9LwkvCu6mwm7FPbcuLq9qfWRJIUPQShioz4je9dZF86yiQNpmcTM9KHrbzzne5QvrDlKhQIMxkhaYjeKkIGsTzg7DllAhCjzoubC37Cy1SGcOVGYzO89VUSDJbvCLTdATVYk95jL1PXSY-t9MTgyijEB503Q46i_CJ4EReHZOsWzgUrVmK1zp0J5BviEwv3ExeITlt36rjzZpVouytdjOL7661C2g_kKYCakyiXitBycmH3EiKFpOSaVQ6I73akMP4yZK4tgn4F4j41nIyC-w0S67y3dHfLcnRsvN666gLwnk03s4ZbCPAs7PH34VChErWIVEhwvTdkuQZoaIpkYgePv-EaduL7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت هولناک جراح لامِردی از موشکی عجیبی که آمریکا روی مردم ایران آزمایش کرد
🔹
۷۲۰ هزار ترکش بر سر یک شهر ۳۰ هزار نفری ریخت!
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440996" target="_blank">📅 22:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlugXGlp2fvSMmsY7Qu9OQowryapzzcDxxDsHsOYY-VqX_oyFLE0yg1Ds0-inAl0war3MosAKKgnGnPm3U6c81X6ydxrvmxd_wC_PSstW2b6vtAK_dygcHzXmpx0QILaBrIbS-If8r-yAvO6EBML5272FvxuCg523OJutrhBcNcez8lATXZOtHZICGhXJI3vdAglg98BuUNVKyj1qSFA0fJdfMYTJJsjpLq791IDrqqzzn2TYgAZt4PLr_VYc7bjGLK8amzEJCicn-Op4uXSgDPVv8YjsNO6oTQchSwOXOC5on9cLZOnFmU2od6aMr3JFL40NmyRnNEobKl2__nBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
زنان روستایی به بازار آنلاین کشور وصل شدند
🔹
همراه اول، دیجی‌کالا و وزارت جهاد کشاورزی با امضای یک تفاهم‌نامه مشترک، مسیر تازه‌ای برای فروش مستقیم محصولات زنان روستایی و عشایری در بازار آنلاین کشور ایجاد کردند.
🔹
در این طرح، همراه اول توسعه زیرساخت‌های ارتباطی و خدمات دیجیتال را برعهده دارد، دیجی‌کالا آموزش، بازاریابی و لجستیک را فراهم می‌کند و وزارت جهاد کشاورزی نیز تولیدکنندگان واجد شرایط را شناسایی و حمایت می‌کند.
🔹
هدف این همکاری، ایجاد کسب‌وکارهای پایدار و افزایش سهم تولیدکنندگان از فروش محصولات است؛ اقدامی که با کاهش واسطه‌ها، امکان عرضه مستقیم کالاها به مشتریان سراسر کشور را فراهم می‌کند.
http://mci.ir/-A1AN5G
@mcinews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440995" target="_blank">📅 21:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN9awUJLchILGc4qnfqyEdJNmQqRuER6iFvPn6JP0edJquynFEibHD15NbUadkXfysQMZXsKSvSrv_OUl605yTJ587R8_rheTShY0oSgWAp20gtumX65ibizPmXiFYPn_Hf9j5Zy2JNtKgXJBNjjpRV1fBS_3zThPjfOwWL1bAzmJWQHUESSAowAALszMevIFwhj7uycnyvyIGEzmarj-xIAd1Ki1ryrKzJ5UF0vDd2Hk7SYyphCRZHyJf2dLeCJUD61KMDbarZ1_4Mymh7GGaSlVg8uLFgqZzdPc2VcJHd5Bp3NH0RUNyk7vl3s2MnLaOn74t4koueZPmRwtbf3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#انتصاب
| احمدزاده مشاور و مدیر حوزه مدیرعامل نمایشگاه بین‌المللی شهرآفتاب شد
◀️
محمدمهدی سالاری، مدیرعامل شرکت نمایشگاه‌های بین‌المللی شهرآفتاب، طی حکمی  محسن احمدزاده را به عنوان مشاور و مدیر حوزه مدیرعامل این شرکت منصوب کرد.
🔗
متن کامل خبر:
https://exhibiran.com/احمدزاده-مشاور-و-مدیر-حوزه-مدیرعامل-نم/</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440994" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440993" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_1h3kxrxSD1YmFAe_Lm5W9VhItwDxfWX_sK08Tp9_XxeAbkaXhBsnmczhZYs6sJSbnzqXXQoj6StcsbNJEXw2NZlIxbnOYBNxV3Kpn0bReuSsC4NwZ8B65xEqE_lAA9EMUMkzv93ja_67HCnGgLiik58ldG-BElFcrpdjzqv4znyl9TTviKvqLH86_hFRDYxZ_gY1oIGlqtsvTur0c4dqcOoAxt1IzZAeMU5F53wc7a3kZe28Z6rzpMTfWhslKngpVcOixTRULmaqXXixEFb9t8eKFYkJRh_Oe-aVMF9Ln9JgOfVBLb2vP683zX7hDFhs1A2RZ93XKyhqPxYmtPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
گروه هکری حنظله: آمریکایی‌ها درصورت هر اقدام علیه ایران باید جنازه سربازان خود را از مخفی‌ترین پایگاه‌های خود خارج کنند‌.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/440992" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440990">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpbcDqWR3pLc_UgeQ7xrf66PXmj50gm5fzvWzggvD1inVWz2aAurVC19yyV2RbzWhhrfNt-Rl1JDfSmQjEOvXugy-lf1w9OXw1kiN8m3CKWNo4tPljcgCoGX3wfRAdDXKevqrkBf2JGaTwdTpgVZgqCuoTXvD7mhL5mR2x51ab60eC7D3HycaElpBUVXQVhQTFmAYbZo0EWqNloJl63HkdGBJCxRnk9-2e8eoUKNhic7m-Pur1SarvKugEFwszItW-yLjqIiicHxdjqdlAakVuWgjarfE25XGBNDkRDDBpkPvPMthPZ4PFGFXUTGFoX6CCaZjPL05YivyAg_7U6TpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XU42Py81V5jvwk6c7ZjMVSXz7uocLkOzqux8ZzTJwQETmO_ATkb8pSTPB9LIeIMt9WKFzWlCul4icSNE8lfvESOXn6oyjqr4aZgAA9eLAbUfVUIPcwXoHUbaX3tZiE2eJgM010O8nch7sAy3-wYNohqv9AXtdXXthuatQh_XJwqlmgRwtQsKPF4HrFtHeb2n-BFumvV-9WIWA85LWj-9VMlzpoRNlf9D3csgk_cjz2FjdFYuL9bpB5RCDScsMIaVgFfSmBiX4TcVBrS3omgtt8R7vFnmbOfORYfbhdOvkhUfS3NH3WH282Wr4cZuCqw6ScghHXbExVAPPsIPN_M3xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
عراقچی: دیپلماسی را ترجیح می‌دهیم اما سخن گفتن به زبان‌های دیگر را نیز می دانیم
🔹
تنگه هرمز در آب‌های بین‌المللی قرار ندارد، بلکه میان ایران و عمان مشترک است و هزاران مایل از سواحل ایالات متحده فاصله دارد. مرزهای دریایی کاملاً روشن و بدون ابهام هستند.
🔹
نیروهای مسلح قدرتمند ما به‌طور مستمر در حالت آماده‌باش قرار دارند تا با هرگونه نقض حریم هوایی، زمینی یا دریایی ایران مقابله کنند.
🔹
نیروهای خارجی که در نزدیکی قلمرو ما قرار دارند، همواره در معرض خطر هستند؛ چه به‌سبب خطاهای انسانی خود، چه حوادث ساده، و چه احتمال گرفتار شدن در تبادل آتش.
🔹
برای کاهش این خطرات، بهترین راه آن است که نیروهای خارجی هرچه سریع‌تر این منطقه را ترک کنند؛ منطقه‌ای که هرگز پذیرای حضور دشمنان نخواهد بود.
🔹
ایران زبان دیپلماسی را ترجیح می‌دهد؛ با این حال، همان‌گونه که رزمندگان شجاع ما به جهانیان نشان داده‌اند، ما به زبان‌های دیگر نیز سخن گفتن را به‌خوبی می‌دانیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440990" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfeb9f3597.mp4?token=E_i8dYWbsn6bGWTorQdlr-jgefMobHs4Uu56k1-BA5118lI5xvomq4qVjefunmFx30yTSXzp9HQxMolNl44mteZpyudLEzQQxj_RXYTjFSXY_SB-feEfes7d-blAAZkDjBNFzIqU5u6oZxwAUlGkx-vzfzKBdnN8a28jPpOXHyVuwxIz3AhS2T8iN1GejYh2zo_Ej8QEYijakhWdDSDcpZaaFQxtADdX688BcffyLhhTbx1Pa0aP9zglHe1U93DlY18s33601eJ--1IWDwmd3KliFd_nQnUSeb0D1b5DkPffMPyA1XU24lIj7kIt5ZhYiV4RpEFgyCjKxYRJKZYeMBYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfeb9f3597.mp4?token=E_i8dYWbsn6bGWTorQdlr-jgefMobHs4Uu56k1-BA5118lI5xvomq4qVjefunmFx30yTSXzp9HQxMolNl44mteZpyudLEzQQxj_RXYTjFSXY_SB-feEfes7d-blAAZkDjBNFzIqU5u6oZxwAUlGkx-vzfzKBdnN8a28jPpOXHyVuwxIz3AhS2T8iN1GejYh2zo_Ej8QEYijakhWdDSDcpZaaFQxtADdX688BcffyLhhTbx1Pa0aP9zglHe1U93DlY18s33601eJ--1IWDwmd3KliFd_nQnUSeb0D1b5DkPffMPyA1XU24lIj7kIt5ZhYiV4RpEFgyCjKxYRJKZYeMBYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برگزاری آیین گلاب‌گیری در خوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440989" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a01d81fcb.mp4?token=KIOvHe4dGBpMBJA7mlFaYcjjSy63_sdBhiRTQMtnQAIKOM14RuRoMudALW7xgeNIe3eJuDhfCJHPWV0wGYe59ijqi91ECSJ-KsaoTVsIXrk30nblU5JMnn_LBpMnsNhuLYemCOn3lWAom5dFcBYr6a9HJjhyIhdPtyrhuc0U07RWmTm4Amn70BwJWliD0udz1Pg9xm_wYonjPBbAqDQGJtpgqeE3GoaPZ6ZMKE4JlpCUKhnbrd54U9pYciOqM6opB7YJa_pmhBorKByJgCApEZ4ynTsZYpC5a28-KAqD9HSzzf0iiVZ-AyeXLt2joITPD67en-BHp6Ef67U7RvY0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a01d81fcb.mp4?token=KIOvHe4dGBpMBJA7mlFaYcjjSy63_sdBhiRTQMtnQAIKOM14RuRoMudALW7xgeNIe3eJuDhfCJHPWV0wGYe59ijqi91ECSJ-KsaoTVsIXrk30nblU5JMnn_LBpMnsNhuLYemCOn3lWAom5dFcBYr6a9HJjhyIhdPtyrhuc0U07RWmTm4Amn70BwJWliD0udz1Pg9xm_wYonjPBbAqDQGJtpgqeE3GoaPZ6ZMKE4JlpCUKhnbrd54U9pYciOqM6opB7YJa_pmhBorKByJgCApEZ4ynTsZYpC5a28-KAqD9HSzzf0iiVZ-AyeXLt2joITPD67en-BHp6Ef67U7RvY0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جواد موگویی، مستندساز: ما باید از لامرد در دنیا، هیروشیما بسازیم
🔹
اگر جای مسئولان تیم ملی فوتبال بودم در جام جهانی اسم لامرد را هم روی سینۀ بازیکنان می‌زدم تا با این نام وارد زمین مسابقه شوند. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440987" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b15fc357c1.mp4?token=YTERdOtimH7S4Jsml1g7AY-4XQkg4rpF04_avnWHGvZXlGRgLgMquWvwf_Y4rO3CLnq_WfLxnBh887dLUIMy_8o6u8VyQaE5WfEZbLjeNlQ09GjaP8xt-jYBeOsPIgS7BcErtQFF0TH3ssllXIqZU8lJ_QKZBrfoPedP1lR17fA_PvRkjEe_HytvLR59sZnHfvEV8gNCZdi8NW3wM2Sgk3CzSsiLhYtLgbqLrOK40s-Zlu2Z_Sj2dD5lhrURt7bzRhyeIWDURTStR8veYIyoTlKz1J4fnvtu1UL2x7WtBPlXPtYCBaI5LJTObYaodlX45W054MxJJBxenGOuQQ-Pyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b15fc357c1.mp4?token=YTERdOtimH7S4Jsml1g7AY-4XQkg4rpF04_avnWHGvZXlGRgLgMquWvwf_Y4rO3CLnq_WfLxnBh887dLUIMy_8o6u8VyQaE5WfEZbLjeNlQ09GjaP8xt-jYBeOsPIgS7BcErtQFF0TH3ssllXIqZU8lJ_QKZBrfoPedP1lR17fA_PvRkjEe_HytvLR59sZnHfvEV8gNCZdi8NW3wM2Sgk3CzSsiLhYtLgbqLrOK40s-Zlu2Z_Sj2dD5lhrURt7bzRhyeIWDURTStR8veYIyoTlKz1J4fnvtu1UL2x7WtBPlXPtYCBaI5LJTObYaodlX45W054MxJJBxenGOuQQ-Pyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان حمایت: به خودروسازانی که بدعهدی کنند، اجازهٔ فروش جدید و افزایش قیمت نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/440986" target="_blank">📅 21:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440984">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7bf84d1d9.mp4?token=eFSHxclhuJIcouhzl6RmWsl8bD4RK_7ZbLmMtnMEWas-YZPqXnnRaHwinPpCZil_N0PY5GSLidKolpmEXh9p1J-qsBzfeKoQpXIrblUHTBW6HlxluNUbs7c1H734EDCrf7KMj8F9kB531ODdw7jMqz80TA_ciXmXMfN8YPjsVL3EbfQrt2MQYx15mHkczLxXPK-gxt22T4mgt_3i8y0MDIt4l5pvV-qnfO5gtXU--eQyOAhH007bpDNlBTEVSWFur3PYXMPGE27Js3fWwYf_KdPPnYbiQ8lO1cLYCsEj5YPqp2aAJ-GYNACzciECOueL10d70TGapspmzh8c2pehXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7bf84d1d9.mp4?token=eFSHxclhuJIcouhzl6RmWsl8bD4RK_7ZbLmMtnMEWas-YZPqXnnRaHwinPpCZil_N0PY5GSLidKolpmEXh9p1J-qsBzfeKoQpXIrblUHTBW6HlxluNUbs7c1H734EDCrf7KMj8F9kB531ODdw7jMqz80TA_ciXmXMfN8YPjsVL3EbfQrt2MQYx15mHkczLxXPK-gxt22T4mgt_3i8y0MDIt4l5pvV-qnfO5gtXU--eQyOAhH007bpDNlBTEVSWFur3PYXMPGE27Js3fWwYf_KdPPnYbiQ8lO1cLYCsEj5YPqp2aAJ-GYNACzciECOueL10d70TGapspmzh8c2pehXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ شهید لشکر ۱۴ امام حسین(ع) در اصفهان تشییع شدند
🔸
«مصطفی امینی» و «عبدالحسین شیخ‌کوپایی» چند روز قبل در منطقۀ راهبردی تنگۀ هرمز به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440984" target="_blank">📅 21:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmyNNx8WRFpumeH4FsTNWlQ1Kl21M2N9TGRkJu_W6LJEmnMfnjHq0XA-TmNdB5hzP66sUR7xBVreo7lCMxCKaZlyxdDZwG5uiR1Q9vEmsKVst_JW_OstDREj-658CI2RCNIo5dwPhcUOIGtYra1hzhFjuoMtdCT-wQv5kao4rSvGdB442xZ0mxrMy75OWc0bCnaznAKUdFtnZezedeVOtKZ10o-Yb5tD6g5lj5wkwxp8ymXek_-Y7c9A_V2vY-nv7XnIo-ZCmOnpqSPXpQUSyd-wb4CbcJqNHyUlJZZUZqbiJoPB5yoVaFZP1-bWjdeCoJI00PcLqMvcvYXncpyUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
🔹
۲ فرودگاه‌ بزرگ تهران از صبح امروز تمامی پروازهای خود را متوقف کرده‌اند.
🔹
روابط‌عمومی سازمان هواپیمایی به…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/440983" target="_blank">📅 20:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POl-MOEDwvZp3vJdfAXGEnBmMzgk7z1TSmpT4fcjSWN4XMlHe_YxSITKwRdWSsP-GUsBW3vAfvRbyNASwJE4v8hXX7cy_ryYz2Pwepq1j-jPgQiQP3-B96wsBjrRgSVESoGBBUBVgLYrO1PXUh39ItiYtKScdyTmWF7oOgjkuagAGpGLd4GFAQJZRyHpdmvS4Tpp7EKsTl4C33tgGGlEMjlIEl9ooaUABGGO6jTgjB-1bFtDRk3rzfhBYKQIVdMK2MWUJiP1hZ4oqO43ElfWDMERIyWWvoTCUxRXO2QcYgaWDASMfdV0xy67cxD5bK_skAGklBN31JKqDeqZfzCUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌   ادعای اصابت پهپاد ایرانی به فرودگاه کویت عملیات پرچم دروغین دشمن است
🔹
یک منبع آگاه: صحنه سازی دروغین دشمن در مورد اصابت پهپاد ادعایی نشان از عملیات روانی و مربوط به پرچم های دروغین دشمن است.
🔹
پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/440982" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBBE1DjFv9a7nUTHStqcIZmPxxhuQeJqX3lLO06qVQB5j61nof1ofJKpdv0ISuvy6ELXw82vEShIHrC5QoLLC7W7IcgrzVxfcrZpBf9SKeFbykUBoSyUnulmJ7faAIlpj-kazUmo_15KnJlufqIVtQ3R6Xx-MQ-zscNYCmm3a8bBsBh6BVnqgpU9xJC1XmUvxBVKp5nQmIVXox4_mnnbzc_bS4UN2CT5k5Xll6hqeO7Z785oSZW3h6LJI9WtF3oWw_qxMrFrWkoHGmP5o1eaAMbgxZULaDv3A2EGuHmrsoOC_f9H5DuHRDpsSOu4_z0El07nwNgKPajeTZF_pOs6PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات احتمالی در مالکیت پرسپولیس
🔹
سال گذشته ۳ بانک صادرات، رفاه و اقتصاد نوین هر کدام ۵ درصد سهام خود را به‌صورت امانی در اختیار بانک شهر گذاشتند تا این بانک به‌علاوه ۳۰ درصد سهام خود، با ۴۵ درصد سهام‌دار اصلی پرسپولیس شود.
🔹
حالا بانک شهر به‌دنبال خرید ۵ درصد از سهام بانک صادرات است و در ادامه احتمال دارد سهام برخی دیگر از اعضای کنسرسیوم را خریداری کند تا به‌تنهایی جایگاه خود به‌عنوان تصمیم‌گیر اصلی قرمزپوشان پایتخت را تثبیت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440981" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkdjGhrQ7GLHIhRM_Xmimf6yL-_qqUbL4vgrpDfTnLWQYwKCRcQkK7uDYpXqdV8wqds4hYkdRa9DeZ0V3fe4LcjbIJsrhLK2l6BXfG6SVK4xW2fsKfLUODAEhotg5CRu1WZfLtnbvBpMSfVeXG3Pyj5O4PL1a7MCRKgbC-dhCPCB-EUvko0fYlI83Fk492tU0K3qMfsIp5H9H-lr8s4d_7McIN1qHHxf6N78C2FNC3xNWWfABh9DEMCyJq2w0yjhP2JDHoYkK_O3F5N_LPAlSSoLBkKpnH34Vxtk0n4DDrbXxxTf9ky8ZG8yfrkfaWrOvtrUFyZp1VUh_Rf9JWYzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارندگی‌ها در کشور ۶۸ درصد افزایش یافت
🔹
وزارت نیرو: میزان ریزش‌های جوی در سال آبی جاری به ۲۳۲.۷ میلی‌متر رسیده است که نسبت به مشابه سال گذشته ۶۸ درصد افزایش نشان می‌دهد.
🔹
بیشترین رشد بارندگی در استان هرمزگان با ۷۱ درصد بوده و بیشترین افت بارندگی مربوط به استان قم بوده است که نسبت به دراز مدت نرمال ۳۵ درصد کاهش بارندگی را تجربه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440980" target="_blank">📅 20:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f52d14f4.mp4?token=OHmTgp-Wnk7Ipes70_YXbl8TmuTSoAX5bJKCmWj0ybxHJrn7gqyn8SJyoIr-3P5CEhsUzRTZrvhQvULHnh1UpFt21hBS5XSwJHiOUqEh-dlyD_9vMz6OniFhvrhw88jUDrd6ItwxQ-1CrmfGzQufsyCe9ejJyquGG7xFKpHBk_yaBWAY2teG9I06H2qOZprXNZwRAdSP5liOwEEZiFo_5J8Xoe3FY2DPSqSgUYVRZIc6tQSgcs-gXLr8UIVoPqPDFAPBf7-7aLk4i5VHBEsP8LgFMxxG_8kALnloHJ_neiOdutbpiVJTpNoTz5LV5hsrrR9pCtuRXxRvvCfug0ghzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f52d14f4.mp4?token=OHmTgp-Wnk7Ipes70_YXbl8TmuTSoAX5bJKCmWj0ybxHJrn7gqyn8SJyoIr-3P5CEhsUzRTZrvhQvULHnh1UpFt21hBS5XSwJHiOUqEh-dlyD_9vMz6OniFhvrhw88jUDrd6ItwxQ-1CrmfGzQufsyCe9ejJyquGG7xFKpHBk_yaBWAY2teG9I06H2qOZprXNZwRAdSP5liOwEEZiFo_5J8Xoe3FY2DPSqSgUYVRZIc6tQSgcs-gXLr8UIVoPqPDFAPBf7-7aLk4i5VHBEsP8LgFMxxG_8kALnloHJ_neiOdutbpiVJTpNoTz5LV5hsrrR9pCtuRXxRvvCfug0ghzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قشقاوی، عضو کمیسیون امنیت ملی مجلس: تا در کل لبنان آتش‌بس برقرار نشود، امکان ندارد جنگ به پایان برسد
🔹
کسانی که ایران و لبنان را از هم جدا می‌کنند اطلاعات تاریخی ندارند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440979" target="_blank">📅 20:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7JWLI7zPBe68MA84aKbGUzHcU-cATu1RV9R-Su0Y0sl8Lsy3Xeyv-XjuvA2QukitERMlQWgHrvuP8s_IESP-tTxgq32qh4QA7lzyvSHufjpFNp8QE7t0GQgoS4TTt_qwVtuQMoJ15AFMIPWlIDONEZfpubaieVR-oBxUyxs9T8pKTtkQf4U4S3O04y_LS02PaAdv_9xVBZQNxxptI3UTitVGXqKe1rjAxzBFzUP1d_KijNutc3j27InSk7Xyo6aRCE8n1kEwnb2o0zSboKzPKruyWS9Jm_uZ-zS0cv7GSS0nFtd1O-HCS3RJXfXHU-_eKweKW8d3x9KO3YucdFQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ترامپ سقوط بالگرد نظامی این کشور در تنگۀ هرمز را تائید کرد و گفت حال خلبان‌ها خوب است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440978" target="_blank">📅 20:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmy-_8tr0d98UU_4HsLp-eKXYHbQc9kOcvjFANDMj8PQOASEy5JZz99gliC17KBab96LEemtv6I-nvBd9IMOtaT-wOFBYFvsdWc9rE7HnR4PT0d6xod43_QU3bQQ_l9nQBGDelAqA9oXu_OBaMeULFZGJobhchLArbnMoqElmOJYeG3kNvbdl3SAIxNYXI5x_fLEh9JD-7hKbj5JPfy32Z8TKGUIq6m9GtNMA18zc3yU0A57EcxyV3A60u7KCHhKtW8duxbRVJmu52ENRzild7-egAEjWqzgVGhsncTEjSsuhlH_CwyjEUByq1yLAFMuS6I7lvQMtZLnxcSbmHnOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم
🔹
عهد خود را بشکنید، تا به همان زبانی برگردیم که از همه بهتر بلدیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440977" target="_blank">📅 20:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb207decc.mp4?token=FMASjhEsX9h_1Jb6u2wZ_-UnoWBjgJ9S3pwnA6PbP1QJS2NtuI_59B7KLTQ2yljdnQN7LgEpOXmIOrabCghyK7mxBOPpi0DLsvhl-kEptUqmEzyxrmjJYfa83GrLlwRn75aIQXHLJjXXXv_tAh_wpvWoIJApi0i8JlF7MR4Mup_DjHX1dWpPTjtkLPUM8Inj_N0O7p8zbFgKpXHe-o4eXhgWxKCIekULRxVHwN5NpmB62yIdDAvhhLknv4FHqBrtFOfFnLfigRWXtfq1PdAgu0VTJ0VHRlmzPmCklu3QoCCphmyyC4mjgQWitWDUfVbl4UZUqHfFtj6L416VU3gGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb207decc.mp4?token=FMASjhEsX9h_1Jb6u2wZ_-UnoWBjgJ9S3pwnA6PbP1QJS2NtuI_59B7KLTQ2yljdnQN7LgEpOXmIOrabCghyK7mxBOPpi0DLsvhl-kEptUqmEzyxrmjJYfa83GrLlwRn75aIQXHLJjXXXv_tAh_wpvWoIJApi0i8JlF7MR4Mup_DjHX1dWpPTjtkLPUM8Inj_N0O7p8zbFgKpXHe-o4eXhgWxKCIekULRxVHwN5NpmB62yIdDAvhhLknv4FHqBrtFOfFnLfigRWXtfq1PdAgu0VTJ0VHRlmzPmCklu3QoCCphmyyC4mjgQWitWDUfVbl4UZUqHfFtj6L416VU3gGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی کمیسیون امنیت ملی مجلس: ضربات کوبندۀ ایران به رژیم‌صهیونیستی نشان داد آمریکا حداقل در ظاهر از حمایتش نسبت به اسرائیل عقب‌نشینی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440976" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48568ab659.mp4?token=dWnH-diOV6MzTeGnvV0xJiCXitShjZmyrHHuszsCoTsTtUC-u_Vmeyb5_LvHUrfFHTgD9hAHnd_K1l2HSNulDsLdgPSlxIwxsiAkXIp-Lj4WbUoTGGbsWkm4a0KTLam8H9DObTalDijpHyNS4laPdz1Xwiq-i44q13U6fG8SwKJyC_1WBNBOQ4I5N45TcXSWipqN4uguwz23Z_GUSwW6uUAA7wupAtuU_ZbrZS5TkzeWrs0YMOf3SKC6IOYjZ9gLPxFKVPZkXZAwJukIyxro6tU964VvwLagtO-R_g9z6J5VLnUWWI8sUVmbCXnuZ4KBFKk-20wFzYbgyJBozN6v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48568ab659.mp4?token=dWnH-diOV6MzTeGnvV0xJiCXitShjZmyrHHuszsCoTsTtUC-u_Vmeyb5_LvHUrfFHTgD9hAHnd_K1l2HSNulDsLdgPSlxIwxsiAkXIp-Lj4WbUoTGGbsWkm4a0KTLam8H9DObTalDijpHyNS4laPdz1Xwiq-i44q13U6fG8SwKJyC_1WBNBOQ4I5N45TcXSWipqN4uguwz23Z_GUSwW6uUAA7wupAtuU_ZbrZS5TkzeWrs0YMOf3SKC6IOYjZ9gLPxFKVPZkXZAwJukIyxro6tU964VvwLagtO-R_g9z6J5VLnUWWI8sUVmbCXnuZ4KBFKk-20wFzYbgyJBozN6v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قشقاوی، عضو کمیسیون امنیت ملی مجلس: تا در کل لبنان آتش‌بس برقرار نشود، امکان ندارد جنگ به پایان برسد
🔹
کسانی که ایران و لبنان را از هم جدا می‌کنند اطلاعات تاریخی ندارند.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440975" target="_blank">📅 20:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40a476a17.mp4?token=KMOCW3v7zJ8BMDqL4hV4bHG3xRUtqyAhgu8jZuUcm-LgTTr3bhsYf1Itap526taSHhN1-R8f51rQrqgNa-xqMxGv5EQ_PbmVqpcoAvSXys22LSsMslwIwmlmNdcl6iz3vSbPA0vDM0n1i8-Q8fTAwhb4oBtfHN4A2mNokqerxIFYBNwssEd9wppXDZu1jOZTztplcgiehYOjWa2RHG3wW4QKPu3RAHqUdcMuKXqKE70hWu5rFIuewGQa-cP74_2KRKagUHudUDhSHAukn2r2LxxL5kjDlyVbqLEUQ3KAO2hhYAYJxG_9c_obt_XEXW25pV_0N896jJhG-IdhXGjVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40a476a17.mp4?token=KMOCW3v7zJ8BMDqL4hV4bHG3xRUtqyAhgu8jZuUcm-LgTTr3bhsYf1Itap526taSHhN1-R8f51rQrqgNa-xqMxGv5EQ_PbmVqpcoAvSXys22LSsMslwIwmlmNdcl6iz3vSbPA0vDM0n1i8-Q8fTAwhb4oBtfHN4A2mNokqerxIFYBNwssEd9wppXDZu1jOZTztplcgiehYOjWa2RHG3wW4QKPu3RAHqUdcMuKXqKE70hWu5rFIuewGQa-cP74_2KRKagUHudUDhSHAukn2r2LxxL5kjDlyVbqLEUQ3KAO2hhYAYJxG_9c_obt_XEXW25pV_0N896jJhG-IdhXGjVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جواد موگویی، مستندساز: آمریکا برای اولین‌بار در دنیا از موشک کشتار جمعی ممنوعه در لامرد استفاده کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440974" target="_blank">📅 20:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-61.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/440973" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط ۶۰.pdf</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440973" target="_blank">📅 19:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40cb2cad7.mp4?token=cBb4tqbYYVNR-m4zmqkQ07_ENQXN8CQ2R15o4jJPhmBk0vkO3dPDu2scB4VF-3tvQCvlzkPE_n-uxcGZ47uz9qMUOIjAKQdDfioqbKJJp1ikOacvCHEeu69bGNEkvJ2ZzlaWz2lUSUNN2wc1-sVvNdumGr10di8mJDDfgl4L9ICaRS-e5Wg6GOwj5BiIDQgY2NZoauAs4FeC57Y2Wyxh_NVbJzspiOJGCOVsC9yspG60SFkDoM4b7VqSHeZ9bfvWuzCZtr8eeFvyMTw_qYeRg-oI60oYo2AAbWirQtIbymzrHXLsiX9HeDY1orFd29CXOdmzawdcG3LANAv3tpkeAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40cb2cad7.mp4?token=cBb4tqbYYVNR-m4zmqkQ07_ENQXN8CQ2R15o4jJPhmBk0vkO3dPDu2scB4VF-3tvQCvlzkPE_n-uxcGZ47uz9qMUOIjAKQdDfioqbKJJp1ikOacvCHEeu69bGNEkvJ2ZzlaWz2lUSUNN2wc1-sVvNdumGr10di8mJDDfgl4L9ICaRS-e5Wg6GOwj5BiIDQgY2NZoauAs4FeC57Y2Wyxh_NVbJzspiOJGCOVsC9yspG60SFkDoM4b7VqSHeZ9bfvWuzCZtr8eeFvyMTw_qYeRg-oI60oYo2AAbWirQtIbymzrHXLsiX9HeDY1orFd29CXOdmzawdcG3LANAv3tpkeAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت جواد موگویی از نحوۀ شهادت کودکان لامردی در زمین فوتبال با موشک ناشناخته آمریکایی  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440972" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85559cb733.mp4?token=TDVcNAqecoPxpLzbZBWv2leXMzU8MDZHl-IiUNNRIydmLhF3WoZLwQHuGerlpB_zIfmuk6aWZI8PqmMsD7x3xC5UAiKtB0FvoFZir5pPOAmuSier4Hu4pXjSbSx1X2kiMiuNdq-tJzEviiRGouSdLK5PEPB4_C443UIW20Bn_llErDPZ75mAe-EMMowQ7MWJ0GTCRnuc9rFy3cEjD7Bal5J9he7hWfSbVa9AmsKqeug9cacicM4B73YopDboV6QKosVNLRDulZ49v8f3KQqpJK7ENO0lYtFg70DEGnCLqrAneYpVfDf1umWEOy7nw68SnXualPXJ4jfXVyMR6kXhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85559cb733.mp4?token=TDVcNAqecoPxpLzbZBWv2leXMzU8MDZHl-IiUNNRIydmLhF3WoZLwQHuGerlpB_zIfmuk6aWZI8PqmMsD7x3xC5UAiKtB0FvoFZir5pPOAmuSier4Hu4pXjSbSx1X2kiMiuNdq-tJzEviiRGouSdLK5PEPB4_C443UIW20Bn_llErDPZ75mAe-EMMowQ7MWJ0GTCRnuc9rFy3cEjD7Bal5J9he7hWfSbVa9AmsKqeug9cacicM4B73YopDboV6QKosVNLRDulZ49v8f3KQqpJK7ENO0lYtFg70DEGnCLqrAneYpVfDf1umWEOy7nw68SnXualPXJ4jfXVyMR6kXhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بمباران سنگین منطقه «سجود» در جنوب لبنان توسط صهیونیست‌‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440971" target="_blank">📅 19:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440964">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njXbd-qOd32DZp_1UvOMT0JvkqEs4_7vs0aHHcAaZGKRAiD__tmISPqONFBsYah0wtzvXMkex5y54CtYCtOejjmzNa83bmiCeySFQn9Ajj5QapKfHQfDtHX-Kpr33TiKhrtK77g2WRKzJZFHhGkRvFgcPTYHyAfTjkw3x3q43Y-NJvum8OSX80Z2_MoatcupVbXq8yxjgk8Ek2uKyZB4FNElw4j5Pj36WQ07l7EhqArIMdkwZnqE1W1ogLi-uq5d9HIFx3xXfLkKd8eZ9KJjvSRqLQliA_oN18Kkfcx5QDzChXCFE1wGPkpx8FXuSLqPCSZOI6P-9oarMxa9-9Gadg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSJOlR5YqPMrKWKFe9y7AXvTJK_4PH-Aq_ykHBwc2kmkjXwUTR6FLJwMCnumcjuN5hpmxewMgPZv6GvQ-n-eZUz_nvyf5tzI342psph7TvuyVmsxu9fXUyuIN9yLOW_eVhtQgxikMGD-7H3M7WOArdqR8BmXKP0gL382TqVPH9rxlPQHFxrtHXsWnkMoYlq407hCiQF8bDNkIlqyRsUtbi-GGe0mqiOMGrfqIn4Ru_EsneRY1-r7vXdwES1f5sgVAfGyu-Gewhc8gvVpLCxMrc2_mkEPZllolY0JLoQaBnF1JpXHbLPz1EqgHK2LCyOt72KLTKcOTPoIMEZr_nmW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PS4aBWmOjzGOF_8-VllK6uRhgq7PDtQU-gb6gWv2co7k9EnSfhwH41DuOP5UyUTqYX8yWLMvrXnLMMrzAM3ub0CcIGIxZBSeRY6fzZUA_ZgHfSg5nt3yEzjSovTHnK-HocbAEw8e0XQucjmnDZB15gsDDy4IWEEv-CiMI8A74QXZuOXIRrrvW2uX3VvaxZZ8CCyobtv56Fhrnm4KGEP0FdefDNTOu93bKcrp4B92rHMcbUm5tUyunnp1kIGgc1SlpPUfU3UWmYlmZLEAp5qkG1lr9B6Xda1cfr_gfOIxJoZUGIhKyqvYGZkzVIC_LerAwW0r0H80RKnIdV1JWiWgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWxuyc38t2ZLl7uxQMifIExPEO2HHstI1Y2mkSy7MM801eKrSS6GMqkM7akF0ppF3NmaAM6UAXvJY9qF_rskGia7r9ar6UP0tF7i5lFJFl6dvGZ-X08sYvvqopDqePsGn-yCTGnSQvXjYP6HNPQWNQlViUHqe9xaiiiefYzeKKZVEKvzJ-lZPJZEH7x1XZpZtezOUAbBitw7CEkcxh99neS0B3o3VgtMaGCMeRCdRFKXPaMpdczPJUkovsPJYnFcM4qCSJR_PMjU-nqcn-ySOeCUZ0Nc1SLZ9gGMaLZnzE5RYSv5vkX5Rrwy99LAsHQFMfQDV2JsSU3Ni-DJ9TbHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjpRt4TANZIQIS3p62dHLs_4VUc0DJrNCuRZEMJ_1adoI16PAHIFVLYgjh0doMF4tM-lCTFF0_N_d5k3WpB3lzefUfLfe3kg86gaykJNeMuMeR8UFuKwW7pMhgXgxM0S9WIsAZGNFSEA1RlUShhictjZsoftvjtfU5ewRCUMj2Ihn3E1EaDMfxfntPYHHhQ9haiyE_DLdCat7ew4t5cSbF2IGZ_4cyrsFXnyFnBoqf_mh2kp-7zBBSOIQ04HCAN-MhVLYZYn29HyuN53-VH3n_3GIsAQkqtRQCXJIHaGaqcKVoV_jM9R_l7H3bT2QU5tITCgIKldQJdznu_2n4MiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtgmxXv6X8vVsSDlhjVUJTj1dfFW509vGPvUOCoOYqjNV2USPvHPAXmKKHuaNZYLSGe-fj6_m2HoRQ-fntrLpbxPKPTHy7mwhRoCkZvb_5IAd7_fXgudhDnHPbwajnhF2thnHotkTAIVgCJn_CMcu7sT2ajZ3V7EtYEhVvuokAYgHbk3DshO9-bOs79vApJfxfsZrLByLv91_sy2egUFPT9gR1c4rKAOmgTWpu_gDoEp11G1qFHfgCO4tzXOMCrEail20TVBxS84xCz5WIgHPSWj051laojnew7D5TOTmHyuoAFwp6u9-PvYnW4Z0W0Fg24eiWVMOIIwDI8QRg9lWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKJHDUk_TRJHoNtbZpM30-i30fTOrDETuUiQYQSyomaIz2-fM22bNK4xJS4Bx0yPHsMMOu-l5YhaCzl28fNHk5su_SgrHOrNsY1-lXqrH_ICfcb2_Rl1XX2h5izfFSFb3uITt6J_Kz44TkqH8US5LwSVFv7rMeyDfFV4fn3ygBRs-Ee6v4qG1to3t8pBEdgh3yQ-1kkZP30pVsI7gF2caV830AVQPASv9bIOQKqWhnJU77GX-ULg6wV7fjmg7ZMJ3z6OkqeikLLcT3JPVDKmRHD7jRAGUBXmR_rpD1JTmKY2E2K7R8FS87RqYmEhMtxpv0wffgYSneJH5zOdma9oHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازگشت حاجی‌های اصفهانی به فرودگاه شهید بهشتی
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440964" target="_blank">📅 19:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440963">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev7hUyYTuR-dLDP4PSpsl6G77Bg9_8RVasMOgWPi__Td1CSYUfz-e5JH8EfcPluV2UEDWXXfBVFDFQZeMsil4VNOtg3YrPy-KyHv74TdB1w5frEqyfWP76DjLAex0bmQU5-yCB4qn_RqyHBJdrNU-8lCB5sBlf-yC0RoF2Lb3W6hU2OpGKod8SQmK3jll4hUKPMhdzQzjK6lM9rZsqD502q5NxMoCkhKxNi2PMbm3mH_6VSbIcYOUuAwvhP7r0wydchYeoMy2SU_WkaTOWWmFNXD2xNwTgfZCtAF_d57lsyPNLKS2V-6PkhRxu0NTlqYV41e-GnF2WYve-K_0QXAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشان‌گویی‌های ترامپ درباره تقویم توافق با ایران ادامه دارد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا همچنان در حال ارائه جدول‌های زمانی جدید در خصوص احتمال دستیابی به توافق با ایران است.
🔹
او در جدیدترین اظهارنظر امروز سه‌شنبه مدعی شده که توافق با ایران می‌تواند ظرف «دو تا سه روز» حاصل شود.
🔹
این نخستین بار نیست که دولت ترامپ وعده توافق قریب‌الوقوع با ایران را داده است. از زمانی که وزیر خارجه او مارکو روبیو گفت که مذاکره برای رسیدن به توافق با ایران «چند روز زمان می‌برد» الان چند هفته گذشته است.
🔹
شبکه خبری سی‌ان‌ان امروز گزارش داد ترامپ طی دو ماه گذشته دست‌کم ۳۷ بار ادعاهایی درباره نزدیک بودن توافق با ایران مطرح کرده است.
🔹
این رسانه در تحلیلی به رفتار ترامپ به چند دلیل اشاره کرده که از جمله نوشته او ممکن است این‌طور فکر کند که تکرار مداوم این گزاره آن را سرانجام به واقعیت تبدیل خواهد کرد.
🔹
با این حال، برخی از تحلیلگران هم معتقدند که ایجاد برداشت‌های عمومی درباره نزدیک بودن طرف‌ها به توافق بخشی از راهبرد دونالد ترامپ برای کنترل بازارهای مالی است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/440963" target="_blank">📅 19:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440962">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76fa83f43.mp4?token=uuBv6Ft_c_LHy1fMmVUw-UBhEvdNKWTeIpabL5UnoQLVCM4CaearnX2-soDn49rJzhMhv9tVZ6l2oRY9OAf1XzKi5JRBhINlIaZXkgWyAUZAAj43R3-7DfgyUoYEKNTEdvJXv45IgGn6nU9l8GOv_vJXVFRR8O07iXb5m98JViBjmNALfotTS059HAvtnrigQt2fsV7YgIoP6R2fsgYw4zByGOKPHF15Ce2n-svVRbRRbEgloEi5czvOT9i8nOa8YDG8-KQ4-JzWWcAiqH-ax98gfZF4BIBMUa8GoUc59e8rRhfGz12rT5rKo25CezAxoyngwjzh2fez_DtnfLJHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76fa83f43.mp4?token=uuBv6Ft_c_LHy1fMmVUw-UBhEvdNKWTeIpabL5UnoQLVCM4CaearnX2-soDn49rJzhMhv9tVZ6l2oRY9OAf1XzKi5JRBhINlIaZXkgWyAUZAAj43R3-7DfgyUoYEKNTEdvJXv45IgGn6nU9l8GOv_vJXVFRR8O07iXb5m98JViBjmNALfotTS059HAvtnrigQt2fsV7YgIoP6R2fsgYw4zByGOKPHF15Ce2n-svVRbRRbEgloEi5czvOT9i8nOa8YDG8-KQ4-JzWWcAiqH-ax98gfZF4BIBMUa8GoUc59e8rRhfGz12rT5rKo25CezAxoyngwjzh2fez_DtnfLJHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در ۳۰ ثانیه ۷۲۰ هزار ترکش بر سر مردم لامرد ریخت!  @Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/440962" target="_blank">📅 19:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440961">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo2SZJWSMeUphcXEgNFUCInmC2lppO24k4DEdfVK652EdkWdLbpg6_LqHE96azhKkQTUnbMLSpjmvYiKGjGnxa8yxj6JpdCdj57AfhtTRm3tTO279piQ-wNeBWDZ4hSihWKHu4IZmuLcsaZbzJVKcJcnOhxMWtUD3jtaUgcK3ZHRCqLacoYWKUNcRnaiyAddIU92Fham9pl0XY0fFkxT7yb5SZFQIRdZnZ-ViktWtn_hnLRDqASpnrrquAgmHwk15FD9hp2TQT3UEu7GsJJ7zozC59_j4lnEf-twpjo_aWSJL1vAmWuMxLR55o_o8Dem5oo9gKQye8wcDU0KftDHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از دل دریا اورانیوم استخراج کرد
🔹
چین اعلام کرد با دستیابی به فناوری استخراج اورانیوم از آب دریا، موفق شده چندین کیلوگرم اورانیوم را از محیط‌های واقعی دریایی استخراج کند؛ دستاوردی که می‌تواند مسیر تجاری‌سازی این فناوری را هموار کند.
🔹
برآوردها نشان می‌دهد حدود ۴.۵ میلیارد تن اورانیوم در اقیانوس‌های جهان وجود دارد؛ رقمی که بیش از هزار برابر ذخایر شناخته‌شدۀ اورانیوم در خشکی‌هاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/440961" target="_blank">📅 19:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی زرهی ارتش رژیم صهیونیستی در نبطیه هدف اصابت قطعی پهپاد انتحاری ابابیل قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/440960" target="_blank">📅 19:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92c29ad0a.mp4?token=heSleToB_czZ4MKaD5W8ejJZPWa5M1nXvkydQt0Nre8wx2Yit26WaUH84SfVVyMeuBRotNacTuvBHGSUwTzLC7J9dAkjTHunnjofW_5lsxWhh04-VlCCHnx0vh3toVsU17auwQqZGpPLiAckjRJRscPTPkeW4raoPfaELYZJPE4MPG-5Jz-Pnmc6s7HtHHxy1sAdLZLMNMP2YOMagmxBjHYtesBVALwnILakQfmmunmFtvWExSmuAhcQ2dUAHRiYcQmrqX69BmpTwzuRnYsz6aXXDBUs0r15h243K2xiYMEbUGxLeEZK7TyT1O5GOuP4Qv4X-b9YNdRMfhf6n4z_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92c29ad0a.mp4?token=heSleToB_czZ4MKaD5W8ejJZPWa5M1nXvkydQt0Nre8wx2Yit26WaUH84SfVVyMeuBRotNacTuvBHGSUwTzLC7J9dAkjTHunnjofW_5lsxWhh04-VlCCHnx0vh3toVsU17auwQqZGpPLiAckjRJRscPTPkeW4raoPfaELYZJPE4MPG-5Jz-Pnmc6s7HtHHxy1sAdLZLMNMP2YOMagmxBjHYtesBVALwnILakQfmmunmFtvWExSmuAhcQ2dUAHRiYcQmrqX69BmpTwzuRnYsz6aXXDBUs0r15h243K2xiYMEbUGxLeEZK7TyT1O5GOuP4Qv4X-b9YNdRMfhf6n4z_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید دوربین مداربستۀ بیمارستان لامِرد در ساعت حمله به این شهر  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440959" target="_blank">📅 19:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440958">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎥
تشییع دو شهید نیروی پدافند هوایی ارتش در تهران
🔸
«سید بهمن حسینی» و «علیرضا عبیری» از نیروهای پدافند ارتش، در جریان حملۀ روز گذشتۀ رژیم صهیونیستی و در حین ماموریت به شهادت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/440958" target="_blank">📅 19:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEQKc1vRef6zraeaDpFIfpSNWyP7Gmtg30RTGvxtjmiYAw1ueKQVlqRmr1ZGNhPQbswS4mm1CKKiENTArSJM5dilqMD80UjLMVDlWzplLF57iT2ubsd4tnj1BbmGZ725CPgAOJIRubB_jyu1CuSbJn599X_mu7xN2sSFn8maEU417uVgl1_BBUTGQZmSAFt1c87jzZICjb6UbQvzA-tBl-7UA90XZxv2I-pSEvApc8Bmn3zY8J_0Esc-Mrx9I-e7oNy-JIcFxFSq7Uxrd5gPYgbpEsXPyVB5uxH62_GOJpNhDoKM0-2Msbm9urHkWzxkoT3COwBSG8tC9s5YpC8mRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهار شد، قاتل دریاچۀ ارومیه برگشت
🔹
همه در آسمان‌ها به دنبال راه‌حل‌های خشکی دریاچۀ ارومیه هستند، اما به‌گفته مدیر روابط‌عمومی جهاد کشاورزی آذربایجان‌غربی، چغندر روی زمین سالانه معادل ۷/۴ درصد آب دریاچه را قورت می‌دهد؛ یعنی اگر آذربایجانی‌ها فقط ۱۳ سال از…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/440957" target="_blank">📅 19:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440956">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdDOhDJP2tJ95Jxo-ZpVEO7xLOfGDRIF6vNWrhZY9vlqeEHBLiyL-jb_LjsRwU61EX2W35YBir8cANKU353gUeX9yjd-Apg2ty7yFnwaXoxoXB6j0HuR_DAWs8hv337QdNnUEw2-F9pZ7tQKDAX0v0QrBO-V7s2AcKFMZ1dmWGk2fCz7sDbSS4-6w6asVFLl5AsDLS40s7woBNFMk7JmlpD7-4We_ZXrEP3DBZvO94H7KM0eKcl_T1Umk7VrxNSh1L9JtsMKpgqPUTHrNGOrVwALo294K1w9hCybPBAeM1b3GdItW54HdbVEko0ycfnHRZx0AvXGT8AifS5UKhc9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۴ درجه‌ای دما در تهران تا پایان هفته
🔹
اداره هواشناسی تهران: از فردا تا جمعه وزش باد شدید همراه با گردوخاک در بخش‌هایی از استان مورد انتظار است، همچنین دمای پایتخت تا آخر هفته به ۳۷ درجه سانتی‌گراد خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/440956" target="_blank">📅 18:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440955">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNK1UUFXUWuRLumWX8gXMMj0GS3ahyO0wZJgCdlMG1wfYbEZbkVO5p3bJF8Y-XA8AinQ0xdtAFLEFP7hmZS0sNzy32v5izYRzshl_cKxqG4qsbI7pzHm9mY_1YOXjVhYawasx844Te__vPCWwAHhCloYz9LTVHy5SXBUL7sjjuueNQgYE7tukIIi1cbYfTKXqNcqFYk99fwZZAl4wCVyk4NcOEU4wXOY4roDdO7UN_8DIJ8UFEOkan3Kx6wZO9kNnkp-EnqhUGY7ydcHDde0X2s-XamTnVKlhDWI_j_k0GBQW__uDx3nmH9PnU67ku4hQF-aa5S55lSk71q2fQJNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت یک صهیونیست با ادعای جاسوسی برای ایران
🔹
رعنان اوهانا، ۴۴ ساله، نام فردی است که  توسط نیروهای امنیتی اسرائیل با ادعای جاسوسی برای ایران بازداشت شده است.
🔹
رژیم صهیونیستی مدعی شده که این فرد در چندین مأموریت به عکس‌برداری از مناطق حساس پرداخته و مبالغی را نیز دریافت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/440955" target="_blank">📅 18:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440954">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjSZcNVwfkFzQoSKVJXhFzc2DzZ1sVO5f5nBjMAUs9ARqx3WqS9HR16_tfQCpUMgzS9cnef78wrylMn-S_b9JvLhs8v3yzqD-oZsIwl7lyaCw9WuHKu3sIr4eV6nATa_Azgmwe7V3-u8MdwVp8AfSJKa12E9B46bzMVIchKaslrXFV01-6_mJoiq51metrXeSmsIjyyIRReQ2lWFfDyGOYeQ3rOAUCrqY2Tzf890UkKnWDb_LGZifuv2-V95bcNj1MMUWmbn1sRSXTOTY-WvoMp6gbAMa43X696NPFarCypOQzeuhaFjI4qWyPPXodMCgjr51qVlLx5DXFgkmuENBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی از کارکنان شهرداری تهران
🔹
سخنگوی شهرداری تهران: در صدمین روز از مقاومت تاریخی مردم ایران، امید بختیاری، یکی از کارکنان شهرداری در حمله دشمن به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/440954" target="_blank">📅 18:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قوه‌قضائیه: خبر احضار چند سینماگر به دادسرا صحت ندارد
🔹
از ابتدای سال ۱۴۰۵ هیچ سینماگری در رابطه با حوادث دی به مرجع قضایی احضار نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/440953" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286eeda6c1.mp4?token=IpLzBfzOoLF4-x_qPqlHzAOkd_3H7X7P2HvsL1S9N70RLV10OM-6kIMWA8uTs-_ORLfJuaMyozQmgiqW_zGM7cxlLEypDe6D52_eR9unp8e5bHfQVcU0x-FX2bVkdQw9cQ52kZVricsqZ2KnNKE7vjFTNPI6Yxsmvwp3ueXVw6CW1xPJ0j4P1C247d0SwFqshPUf6bpybwQuJJIygBKjkRHeJLIui_78H5b1P29q4NBHaR7GTxeNm3mwSrR_UJojnIjGKXVBHgDiwqJ11H3ZysXe7AgQwZrui0qWd5f9IVnDP7h8CWpNcdj9NOXpRsp6LKHv0mOoGV-n9rbgfMWysT2hw3mEw0Mn-2ldLLpJGo3oMrlL4brekg1pth6QmZE3iKudJfZ5-KC3EiLZ0Jf-SbYIP4bqO-ic-fw79JAM5hzVqz-iUi47SQDocdCrXGwNbaNUXQjxI6BRyayqeE_Ktp37FuDI9rz0rcYVYtqc0S7Tc6d2_onVJyiwDGs5odIVYxb0eC1Nt3X-RBXHY9aJl7cMqRnYoVKzztwUTEwY12_UZwNTPqefsmNybtnw_3d6Q5W__ZMMDS_RSd-ShyGXmdydeRlAFwQXiwdf2BXAuNqR80YfSTEXsn_b5RsAXRFoBFx3b6i5Txy73Dve5RHOjJRnXpQ8ld6joSTUWUvKzco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286eeda6c1.mp4?token=IpLzBfzOoLF4-x_qPqlHzAOkd_3H7X7P2HvsL1S9N70RLV10OM-6kIMWA8uTs-_ORLfJuaMyozQmgiqW_zGM7cxlLEypDe6D52_eR9unp8e5bHfQVcU0x-FX2bVkdQw9cQ52kZVricsqZ2KnNKE7vjFTNPI6Yxsmvwp3ueXVw6CW1xPJ0j4P1C247d0SwFqshPUf6bpybwQuJJIygBKjkRHeJLIui_78H5b1P29q4NBHaR7GTxeNm3mwSrR_UJojnIjGKXVBHgDiwqJ11H3ZysXe7AgQwZrui0qWd5f9IVnDP7h8CWpNcdj9NOXpRsp6LKHv0mOoGV-n9rbgfMWysT2hw3mEw0Mn-2ldLLpJGo3oMrlL4brekg1pth6QmZE3iKudJfZ5-KC3EiLZ0Jf-SbYIP4bqO-ic-fw79JAM5hzVqz-iUi47SQDocdCrXGwNbaNUXQjxI6BRyayqeE_Ktp37FuDI9rz0rcYVYtqc0S7Tc6d2_onVJyiwDGs5odIVYxb0eC1Nt3X-RBXHY9aJl7cMqRnYoVKzztwUTEwY12_UZwNTPqefsmNybtnw_3d6Q5W__ZMMDS_RSd-ShyGXmdydeRlAFwQXiwdf2BXAuNqR80YfSTEXsn_b5RsAXRFoBFx3b6i5Txy73Dve5RHOjJRnXpQ8ld6joSTUWUvKzco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نذور موشکی شاهرود به خط مقدم رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/440952" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj7SvMqedkKbYYGP7C_A5V6zrziCp81HkM8dtCXpfE6rTV_abKC2HnL8P8Wrar2vBuZWSukCBreFKDZqDwHxND3-vDyRSszbcZ2Y_0tVLoJqphgdPma8lgBISmY-3rKY-c0Y6k3JWQURwjKcBZts534TOutrWhYPHd_FZRxBcq5937SeCu5WUSjxOWEPzwqJ19g3F6JoMCNSW-MTmYMqy0DWGPykh7EWpwWLsOjcU_IWU4yNS5BBHQ52HaIpTPqFHr58a1Y_kWfiZWBSErYwikfNxyhm6d8V_HbRYsEa7dN973qLaAFMfZxKIb4qo3ehbu_j4p8q5Ckb1umTVGOBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ با عصبانیت مصاحبه با خبرنگار آمریکایی را ترک کرد
🔹
ترامپ در اواسط مذاکره با خبرنگار رسانه آمریکایی ان‌بی‌سی، پس از سوالات این خبرنگار، با عصبانیت جلسه را ترک کرد‌.
🔹
ترامپ در حین ترک مصاحبه خطاب به خبرنگار گفت: تو یا فاسد هستی یا احمق، رسانه شما هم…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440951" target="_blank">📅 18:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIHDI61IG3U3773DVSnsnp7AjL-C3K829ExQuESjZBENQGq6TfOH41rmsbB-uA-m4ApuqSmz7uid28Dd5jx9wCF7X5ukBadNlvcj8z8NsnBSE44NX97ERfYwN4jT72xQZRDJIJWF2rDA9HPjEl3h9vL7MCMXbwsbBwGSCBaNeclqvclCPAgoci142yS5PjricGShtNwe-KpO49bOHdgQouRupp6nIyTY2S7FSTqZTMSogElu98R-ZcfX9vkxkx91GmDm04fQwd7UuppninZGGKf41JLJDHZrDoLwiWaVXl3WBW9o4rLGr5AiLqPYYoYAfAj5QYQfl1_I8T6ihln8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط حماس برای آغاز اجرای مرحلۀ دوم توافق غزه
🔹
سخنگوی جنبش حماس: گذار به مرحلۀ دوم توافق آتش‌بس، منوط به توانایی میانجی‌ها، کشورهای ضامن و «شورای صلح» است که بتوانند اسرائیل را به توقف نقض توافق و پذیرش این توافقات ملزم کنند.
@Fsrana</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/440950" target="_blank">📅 18:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjQ8vnQs16q-4oFAF63J-TmlNm32bYt8zrT8xzQrkMZHRDz9r-L6vIOmZ8vXGApSSDbvicXp7x1Ns_TM1loU81r15gJR28QZQyy0mZnR98miDAKnKe8cIYLI6q6CNxXnA2TNeQ-xlI76I-iblGh5mcUKxUfgsc8wM__sdlLqD9WlE4udnZdd108TWo38sh4TLK4BxY5_V27qoQGkkqC5bozQA73PjVxhKtycDN-CpJij7uVf8vmUZg2PvVWL1TvRIVgh5NVRxn4OyrOUWJ9JUPkVJpPTIgx8iZ7D2Jj-QphHPMOTJtqRZ7aZcq9zSO-AwNliSnEm5Xka4C8tti1eRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه ورود بن گویر به خاکش را ممنوع کرد
🔹
وزیر امور خارجه فرانسه: به همتای ایتالیایی خود می‌پیوندم و از اتحادیهٔ اروپا می‌خواهم بن گویر را تحریم کند؛ وزیر امنیت داخلی اسرائیل از ورود به خاک ما منع شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/440949" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwzd3wZL7Z5jkkmIoZbhNqE8qd1E9VnIeKX6VZnxZk6p7CukNFoAS8eG41HaskJxntoStAn0LEpMaX8w8AytWX0DJ1oVJ1iYa8Slay9sYO9Jkd128ICrizfPndQkUVIcjIvEpLPw-ZH-go7obwUOyu9snrVkHi4L_lFQ7jKVU7p0J0_lcg1DL-ohrXceHVUuT3ZkJK4T8UlSiUueJfql3uyegczadncAGJFhyMSgoIuY0Dt1jGwqAwj-nbUPVy6WH4d9-vfPMMakMYo6jfzuYOk9gdL58YrqfAAWTweVOW3y80N6u00jxOFuYsLyVbUHM_XvNUrBDcW-m-WOn_IqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
چاپ ایران‌چک جدید ۱۰۰ هزار تومانی به یاد شهدای میناب
🔹
بانک مرکزی اعلام کرد سری جدید ایران‌چک‌های ۱۰۰ هزار تومانی با طرح یادمان شهدای مدرسۀ شجره‌طیبۀ میناب چاپ و به‌تدریج وارد شبکۀ بانکی کشور خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/440948" target="_blank">📅 17:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bahQgSCcbWhtzVodxz4wJqXm-4KICk5U7sQ4Ln4mZa1CYsCrARXJlO9vyru3AcKZ-CHX4G9HAcM26i43BrHHi5WIz2ofa-f9Yka9P2CAZSFhzsxNjwnoC_tsxBtRWwdDlSI59pGQFKM3XEOSGDjqGfgZJauu-awzlUie4jhHq0Mkos_iLeI8OEn6PZYzEkgQjI6PZcs86odNhuu2cEwoXnyLbIYyhEUdPHGJpY3ruYHHcFDjpMfc3KT_8ywtEbhnF7cPvdGwmyf0oAacnhCM_IyayW_FVRjIvh5m-LC8G9xCZIO94lgqJHioCChpqWfw6V_qUCyJ7vQa6j0knAJGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوجهٔ ارزان‌ به مرغداران تحویل می‌شود
🔹
کارگروه امنیت غذایی و تنظیم بازار کالاهای کشاورزی امروز تصویب کرد جوجهٔ یک‌روزه در «سامانهٔ بازارگاه وزارت جهاد کشاورزی» به قیمت مناسب به مرغداران فروخته شود.
🔹
بر اساس این مصوبه، یک‌سوم از جوجه یک‌روزه تولیدی کشور به قیمت مناسب در بازارگاه عرضه می‌شود و به تدریج تمام جوجه‌ها از طریق این سامانه، مستقیم و بدون دخالت واسطه‌ها، توزیع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/440947" target="_blank">📅 17:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvE9U04TiRm8RD6pBhIY6RSbYrxUGQRpoxSWn1Xi8VMJVK6ApZNb1HME-mt4ENEfYrQi7wfzIHqskU4LP3kJ-_MWTJd60MXzpyHU7cWoFp6B7u7KB8-pW4bLdnQhgISik_esr8Q2mmEQ5zh1rucWi4Pj2UhNPdV2uncHWQLsnDpwQfnHVxgVwrn9kxg2VZsBwZ04O3Jk0jsQvi73KVRfZ4ggDwlXtol70bKq2QKhRUMTMc6C-O5ocjoKomnp-LMMhuka2z2Zm_nt8-4sh3RzXML9FnAb8lB0MNLShjL8x3lirIcymTC0sPQ_GpiA4Wo1Oq7tM_6uj6yk6ORSQU-ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5zE86hK8gPp5nygi0Q0PlUV57FRVAJg5z0-MT_-8BC3B9nu-Uda7jyDemvgemz72TD_OgwEwBfkm_K3ut3MYWhMs0pZAekimXfD592ruB9COaptzmGcNkj9n3QPVslya5H1FmjcsMqluiwdq6M5cvicswYrEamOdamKU0o1np_DLQXqqcwETzOz_PgVMTGtqJ55jE8B0L8Iua2jr7rCBEfj29nfMS75KUKHtBftZDBLln_uxnvnwU-TrnP5MJeqQtiC_vMziNX4-Zz293JaVN_L75VYc1l7kTzSNO-iaW1iwtiI023N18mcpzIwNYTK879fnBKinhi5SOu0bkXWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcqjBuvgB5j9kpV8ztXJ-Xi6ANTABXczXBiGALopx6Zq99ySXcbwH9rq-4-ndHKb2HAIrjARR6j1RBrYPOfRZQRHiIXAx6T1qYpkVBRMUQD0phG0bzcrnrJp0k-f6vj0x67JsTxCWXFgpoQlm6dNslDACUvhr1teLj5YZpSG2SHC0ixm7sw2R0nqtiOZJufdbW56Xjxp-TuTC-aSzjD8UAaO60Qh1Twq981EgHpZ6YxYu6YeXMOGWdA5zYBrQsUR6_7JzzZrK6JVoNM1iw4oEjTBrxg_dFtQs2qxXfv6l-1EDhm0g4NlStTxjcsHxZDso-DGcMo7NSCAhWogQnvatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gdhya6DsOlikkimdbyWT31uoqK98A-bdU9K-E10nGc0395ANKbk0tXG39Tk06G5_sfmukfxeYTKG4tspAjDBUf8nH_i5b6PD9t2SxWEvPIDbDKSoi-2XFYdOno_96w-Zd8b82Y1b_WRygdfuFzhrIL6FSSnFOSTLReDzdKlRSBr3OZ_DNkK6Tr5aPJQKNz-1PH2UFYnN7dLUgGfPtc6hMv0H--CQbKT1GWwvBBxTZ5z7hpXP5SCcIGUg2wLnLr5WXsz90oqtYLhf4UuX928eZ58F45KZLUg0GtyY1zigUhe8qsO8F3nWXZrg1qnBUkE946VkRwVvaDSEruoLTHIPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhY_vzodow9pPkWCudlZxkvrvG_Vme1hzvwNpyvLksGRVyhyTXcYD_bG-JxoJGrDaLWk8QUWSLPiDz-sLQDUP61MADuaShGhJgBAKxveWlMwnrEltY_hkRXAhFVR7BSK2IVs3ou1yFAjUbcBVuAqJBplZ8f04L1-Gm3FUvHuDkpYt1KoUfhi2lmRXsbJG9PvNHhsLEz4b1WaaP3MWSPBntIJg2Gk_Epxv9gn8QDQ5SfnCV41p1Xq88Sx_QfySWzsIuvq18aLwpgJ3K7lQbWCNSOAQXSwCdaPL1yzPQ6Wdl2xbi1Dd9sQ6wsCwuBWE_BTvUN3AJQ0acuf8xBxO06rEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رها‌سازی پرندگان شکاری در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440942" target="_blank">📅 17:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTBPDM6FrmeTzk5EZu9MtSEDkxW03dpHjeljUk_CJbd6jq5047DhXrqUmB2gICjARb4u_MI7kfNkK1bsU6VQgyeBmanrj3QH1pBkSKfTG2d0T-bxOJL4_Qaefc9Rym-LqALgR_WbGRJ39pCgh0dwZtcpqmGuTNh218NbEWBIiGoHTYyUi0Ai121RIG2uF60N3O-aE76WNt-hSJAeYUqrKoAIKVhuIWtFlgfAtZBdXB3K2YUyCGPoQtCc3K018nVW2aQil1qv7oCeE8gggwtZH7mPa-27D8Jm0p1XOIY63Odc9Xhlv33SW5XyG7HklJnn0uR2omeP2K7uql4urdj5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف خطاب به مردم: درود خدا بر شما که کشور را از دهان گرگ‌ها بیرون کشیدید
🔹
صد روز از جهاد ملتی که برای حفظ ایرانِ جان قیام کرد می‌گذرد.
🔹
درود خدا بر شما که پشت ایران را گرم کردید، دشمن را ناامید ساختید و کشور را از دهان گرگ‌های درّنده‌ای که برای تسلیم کردن ایران اسلامی دندان تیز کرده بودند، بیرون کشیدید.
🔹
پاینده ایران و زنده باد مقاومت ملت بزرگ ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440941" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhw_WF7YFYYcguapXZykdi4i72scQkY_DQ28E2IXOkW5lEsHM529IS3kLi2-AOdZ54OH7w_-zXiYCvCbGix8aTWikYJ6d3e9ZUiRs6hqUlUozCvIUGkA2w7-vM5Lb7LP3cnGo30Z6hGJo3BFOxP1WduBK3mVQNwXrDqvbj0xD8rBZZbjI0gKnYXT2QdNfZzHTNVa6aZloApXgZ1bOhWWV7f_c7stQ8Hh9bRhdeTYsNwliNTf07l0d7H8k7fqaA2YPft4NMr0sWj5dVN3nXemuGjcuSOzPsgST2a83pWEp1-hF03diyzcqLTH3mihq6hQg2KKykopNjplSliWOJzrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ یک میلیونی دیگر کفاف نمی‌دهد
🔹
دی ماه سال گذشته در زمان حذف افزایش قیمت کالاهای متاثر از ارز ترجیحی محرز بود و دولت جهت پوشش افزایش هزینه‌های خانواده کالابرگ در نظر گرفت.
🔹
خبرگزاری فارس در تاریخ ۱۶ دی ماه سال گذشته
با توجه به نرخ کالاها در ۱۶ دی یعنی پس از افزایش ناشی از حذف ارز ترجیحی محاسبه کرد که کالابرگ یک میلیون تومانی افزایش هزینه‌های خانواده را به صورت کامل پوشش می‌دهد.
🔹
این گزارش واکنش‌های بسیاری داشت و مردم معتقد بودند، همزمان با تورم مبلغ کالابرگ ثابت کفاف افزایش هزینه‌ها را نخواهد داد.
🔹
اما سخنگوی دولت اعلام کرد، خرداد ماه سال ۱۴۰۵، مبلغ کالابرگ متناسب با تورم افزایش خواهد یافت.
🔹
در خردادماه قیمت‌ سبد کالای ۱۱ گانه افزایش جدی پیدا کرده، به نحوی که میزان افزایش قیمت کالا در ۱۹ خرداد ۱۴۰۵ نسبت به قیمت‌ها در قبل از حذف ارز ترجیحی برای هر نفر ماهانه ۳ میلیون تومان است. عددی که در ۱۶ دی ماه تنها ۱ میلیون تومان بود.
🔹
به عبارت دیگر دولت برای عمل به قول خود یعنی پوشش افزایش هزینه‌های ارز ترجیحی باید رقم کالابرگ را ۲ میلیون تومان افزایش دهد و به ۳ میلیون تومان برسد.
@Farseconomy</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/440940" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440939">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi5Of2vP2jKJ8Pu1xCljy0h4L2_T3qEAM7cX7vHmBb4prOhF8hc_f50tr5_kbZP4g6kDKpOQLlkaiMCvEolrZjY6VY3DZfOTkFPNoZJn_2n72hm1pCsQRekBFalWlhNDYouC201Nyti8uwKNzaOnEmRCEtoEIpuNZr5hUApQRXrcnfln7btBPZ6IzISwj6H6UKcecuorWil4swaOJDhwxc54vclUy1kws1_8FMPpfrEQ8_V9JeoS3_HWa2YYgR_ngxrC9g28lE4wwdAo8e81CVPnqCvFUlZKsbiy2ENyIGHyCs29hSEJqxaaKkZ_wzj__6eVEUdaLMfvONuIKx-9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۴۲ درصدی هزینه‌های طرح ترافیک و خدمات شهری
🔹
رئیس کمیسیون حمل‌ونقل شورای شهر تهران: طبق مصوبۀ دولت، کلیه هزینه‌های عوارض یا بهای خدمات، متناسب با نرخ تورم اعلامی یعنی ۴۲ درصد افزایش می‌یابد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440939" target="_blank">📅 16:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440938">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696cefc457.mp4?token=P2W7217aGBdfJUYstHO7A6PdXU_BbUSFYFEbYkIJB3zbuvoEIWhHj3jV58LPY6njd5U22PbBHyj_1NuxPWVfgMaY9te-ihS6dXdoirWwcH5m_nyASS0AQJdlGtzzjpWt1zKlPPi-HqNsO6m3BdbDU7cKkbDagYZgIMoaMv5kGmBJwR_NCXw2U3b8e4lyvuqYt9dCU1wr7JYpZkw6J9hbB0-lgKAXTyvPoGpRKfZvt9FZFXzSj4Z24yIugV7DCPYlZvI748_wRfYBEhMmOui6-gwFXfR_GS-SqQ4PbsKZ_6eyjo2J7GYfd0FMmT5tLhXXsaNqztVb-CMV9oLx7EKmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696cefc457.mp4?token=P2W7217aGBdfJUYstHO7A6PdXU_BbUSFYFEbYkIJB3zbuvoEIWhHj3jV58LPY6njd5U22PbBHyj_1NuxPWVfgMaY9te-ihS6dXdoirWwcH5m_nyASS0AQJdlGtzzjpWt1zKlPPi-HqNsO6m3BdbDU7cKkbDagYZgIMoaMv5kGmBJwR_NCXw2U3b8e4lyvuqYt9dCU1wr7JYpZkw6J9hbB0-lgKAXTyvPoGpRKfZvt9FZFXzSj4Z24yIugV7DCPYlZvI748_wRfYBEhMmOui6-gwFXfR_GS-SqQ4PbsKZ_6eyjo2J7GYfd0FMmT5tLhXXsaNqztVb-CMV9oLx7EKmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح راه‌آهن ۱۷۳ کیلومتری اردبیل-میانه
🔹
پزشکیان: ۴۳ کیلومتر از راه‌آهن اردبیل-میانه که روند ساخت آن به دلیل بروز بحران‌ها، جنگ‌ و تحریم‌های ظالمانه بیش از ۲۰ سال به طول انجامیده، در دولت چهاردهم اجرا شد.
🔹
امروز پیام ما به کل دنیا این است که در تمام بحران‌ها، ایران ما در مسیر پیشرفت و توسعه قرار دارد و با همراهی مدیران و مردم بر تمام مشکلات فائق خواهیم آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/440938" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrBDV1EcWn_OdmRR-aqE2RgsoxCrbVh1I65qhAx4-4X7pOWnlRLb5tRb85xStJYRdE6qPehXmNnODhogK0fcsXzQ7kN8DYL9UrOmE-RZCwWx0HuTC-Lo6S90smToNGkaBX94cBwoH0q3WBh2OfXjMXFbhHgkmWty1QvBIzbMIKqELC5OTxzXJlyOVCAQuXGdTVzUQhIS5c638AGamukqcWv-jlnjsYnFDcIf_bDmo40xa0S_R6ae_6DjZ5e8tIbPAXLUgUid-t2R9ZwNWQj_oqo6Q0HqVOiy2B3G2Uv4VqRp7nENvFBrRGQHnbj2LJhBgGyO9b0xbjZ-mmmi-T4vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ دیوان عدالت اداری دستور توقف مصوبهٔ ایجاد ستاد فضای مجازی را صادر کرد
🔹
دیوان عدالت اداری اعلام کرد: در پی طرح شکایاتی دربارهٔ ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» هیئت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440937" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUgj8sd4WOK2pJtEQnVF8zU-_jKZcid9U10QVDBik17T0CHPCmd2H-cPqIGE8ZR1nSxvfCEFPC2qES8SEXnAmx0wigq3-VxYdocNcEtRLwZ4UPUK6Bpm_kKTkuaSHaARgDBgEGSEeBcJIFhy8poXyOlmOyie7Q_32kAHEwv1M9X6cAaWoafwkGpckq08ScGBmDdsOjGCX0bfksod8ENQvTfKQEYdeafVm1vbSACxAABcu4NQfY4bkHk4XlHmYybYs70PwdtdWwCdZekWkbKi-JKcMecmyCKNjaDmucjmblIbRRyRt9aCRTEgJeMKtlPRIglFkMAmedV6RYTM4sqm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با تصمیم شورای معین شورای‌عالی انقلاب فرهنگی، تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد
🔹
همچنین شورای معین با کاهش تعداد دروس امتحانات نهایی پایۀ یازدهم به ۶ درس برای کنکور ۱۴۰۶ موافقت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farsna/440936" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
ارتش صهیونیستی: یک نیروی حزب‌الله از مرز عبور و به‌سمت نیروهای ما شلیک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440935" target="_blank">📅 16:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
حزب‌الله: یک خودروی زرهی ارتش رژیم صهیونیستی در نبطیه هدف اصابت قطعی پهپاد انتحاری ابابیل قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/440934" target="_blank">📅 16:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2_f0ZhBDor0uq0hNA88gNlXtEHqkBF5NZNKrNjrzMxqWTDtBhj9pwl17iVbe_Z7xE6SOa5etcu8GCXyC1h7dvVm7HKgbw8HoXSoqjbfcTKrIcW-oTfQ44pM4lnsZDl0fkirlwIBxm6c7tVtzbJk91socKE26XG4I2nT-RERD8x_ANSW7Qrcl1a6hTl1vLV0CG2sEq48HD8ZyiL8eU3PN9ppnxBJ0ZpNtXBTQ6FVr2ybM882BqtoXROHgAmUvYA7_Uqoyl5HyOnbK8ANXIEwjUHQMi9LvTcOyT8g5Drl1kDO7LYJ2oFl9w1SnFe-x0YKCmbydrgTBoVX3vbrtYnTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی ۱۲ پاسگاه محیط‌بانی سمنان به دلیل کمبود نیرو
🔹
مدیرکل حفاظت محیط‌زیست استان سمنان: ۱۲ پاسگاه محیط‌بانی به دلیل کمبود نیرو تعطیل شده و معاونت محیط انسانی تنها با پنج نفر فعالیت می‌کند.
🔸
استان سمنان با دارا بودن ۱۸ درصد مناطق تحت مدیریت کشور، زیستگاه ۸ گونه از گرازهای وحشی خاورمیانه، آخرین بازمانده‌های یوزپلنگ آسیایی و تمام نشخوارکنندگان وحشی ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440933" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa48ff6f2f.mp4?token=Ke-kPrdj4FgmEmwcjJgCt65c97G7PzwZJCLjVrF3dSo3iJ2rhRSPl6j6YPXvfKzH7n4VW73eeUrkNJm9Tq3BTcTVOE-zLnoUvnv6_AtIusq0Zx9stirCObaG2Pp1NKV7vgJfJsADJ2ZnKOQZgYzPgdqeIeFWGRyZ9MOoqfNsEBGGHuBhV_Rui6dzNLHArLAHIO7NKa0SxJtED6SNUEKEnsMFadOQhMM2yU-BYg8kJTxRBuKacnpa68UlYm_HN_lD3dNh-SPzGRDcfdgLxdcaDIDFXKBy-TvINc9pM1oETknEgVA37VOMz6PS1DcNL5JO00n_H51_qo2zFjozJqSfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa48ff6f2f.mp4?token=Ke-kPrdj4FgmEmwcjJgCt65c97G7PzwZJCLjVrF3dSo3iJ2rhRSPl6j6YPXvfKzH7n4VW73eeUrkNJm9Tq3BTcTVOE-zLnoUvnv6_AtIusq0Zx9stirCObaG2Pp1NKV7vgJfJsADJ2ZnKOQZgYzPgdqeIeFWGRyZ9MOoqfNsEBGGHuBhV_Rui6dzNLHArLAHIO7NKa0SxJtED6SNUEKEnsMFadOQhMM2yU-BYg8kJTxRBuKacnpa68UlYm_HN_lD3dNh-SPzGRDcfdgLxdcaDIDFXKBy-TvINc9pM1oETknEgVA37VOMz6PS1DcNL5JO00n_H51_qo2zFjozJqSfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی حزب اصلاح‌طلبِ ندای ایرانیان: ایستادگی نیروهای مسلح در ماجرای لبنان هوشمندانه بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440932" target="_blank">📅 16:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
حادثهٔ امنیتی در شمال سرزمین‌های اشغالی باعث اعلام وضعیت اضطراری شد
🔹
رسانه‌های صهیونیستی: به‌دلیل حادثهٔ امنیتی مشکوک به نفوذ رزمنده‌های حزب‌الله، از شهرک‌نشینان مسکاف عام، مرگلیوت و مناره خواسته شده در خانه بمانند و جاده‌های این منطقه مسدود شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440931" target="_blank">📅 15:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
حادثهٔ امنیتی در شمال سرزمین‌های اشغالی باعث اعلام وضعیت اضطراری شد
🔹
رسانه‌های صهیونیستی: به‌دلیل حادثهٔ امنیتی مشکوک به نفوذ رزمنده‌های حزب‌الله، از شهرک‌نشینان مسکاف عام، مرگلیوت و مناره خواسته شده در خانه بمانند و جاده‌های این منطقه مسدود شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440930" target="_blank">📅 15:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMD1duoh_NIBOCcNNaFUw4B2hwI2LZbSu0oK2U3SJbrY2lmHSss7bOGqTt9D-IPK9zreR-AeUaIByCijKYuYGGGiTgjkusV9FqNU1cDPxoaq-ja5i5XsBOzc1AOFuqaP2HMsp5va9rMZtExt0qztaEpEBMe7Kd28BYF2OJiZ4GoRkNAI1SADfkzzG-b-VolZO1wMLqwtXRTql0toooZVJfygnS5mVIYMfFe-VHkvt4B-aBLjiTGbn_vLa36ABRE3cb6MUfYPBWtDNS1EKCVJLYHSd2ioubQLE4Og989XB5_LYg5oufeAK8J1rYEunNC3A1gSzEs0wVDHq2zxrzu6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خطر خطای محاسباتی
برای
مسئولان
🔹
رهبر انقلاب: دشمن با شکست در میدان نظامی بر تا‌ب‌آوری مردم و ایجاد خطای محاسباتی مسئولان تمرکز دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/440929" target="_blank">📅 15:46 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
