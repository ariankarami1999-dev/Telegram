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
<img src="https://cdn4.telesco.pe/file/FqLpROwANUT4gGNE6RiHgWRC9p3V7bjPEjmo_2uaOtdgROh3iEe8TseAh8wE9tngMsjU0yIj4w8aLmf5FlDLw3Xqv5ZjKyh19CSUCxGER5K2GjiUFtiV8dqnm3PkZfN1BGu8EqBDL-4gGGLLO8TL2KcHtuHU0DLzR1c_fcTtzbac4ABRmwSRBdIhJ1BW_w4FkEoz0EbY5gzGivRoW52Q0HXwYJ8dMI8ubaFWP0XLYxiGM-3qtmrag-UxMAxcdPV8ofug3bN9ke0THEFSWAYlkVdKCKn-TC0OakEKCHwOscU7XeQKn_miwdRmrvEiLDYZcaWS0sTeObUQV7GlYh1Q5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-442637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtCOuRetcizoHrUiwGPdfBzSwOWr5a8MHrHzln3L6UFEfsIvtfuI_prOt0buWWUF4w0qzx26k4e-WX0SEPUyj8ZPA82Rie-fKqwJA5bJke7dASuymRS0zwggnjXHBf582INLCUgBWH4AQtzzbCKGJe8e17cBUNrRv9NGseuFMJaeRyIVrgyJorD6_U7YhODMjCO_S0-_Nyk7z5KxUVezEL0y32EYuEs0vGcMgKBwEZ6YKdP5VK464eELTTb1Ws19I8jzhUE43aou75I5XP6IEopmrIVWz3FFuEz8o9uydFhBkGSlN5IuR-VMxBx859A80mAmhnUayFPapv5jpwmT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بخش خصوصی: نان مردم را به ما واگذار کنید
🔹
رئیس بنیاد ملی گندم‌کاران به دولت پیشنهاد کرده موضوع خرید تضمینی گندم را به بخش خصوصی واگذار کند تا از هزینه ۵۰۰ هزار میلیاردی هرسال خلاص شود.
🔹
امسال با گذشت ۳ ماه از آغاز خرید گندم، دولت ۱۲۵ هزار میلیارد تومان به گندم‌کاران بدهکار است. در حالی که کشاورز برای کشت بعدی نیاز به پول دارد.
🔹
دراین‌باره برخی کارشناسان معتقدند خرید گندم باید همچنان توسط دولت ادامه پیدا کند؛ مرادزاده، کارشناس بازرگانی می‌گوید ورود بخش خصوصی تضمین تامین نان را کمرنگ خواهد کرد.
🔹
در مقابل لطفی، کارشناس دیگری در این حوزه می‌گوید: وقتی دولت به تعهدات مالی عمل نمی‌کند، انگیزه کشاورزان برای کشت سال بعد کاهش می‌یابد و محصول به جای سیلوی دولتی به بازارهای دلالی هدایت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/442637" target="_blank">📅 21:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سی‌ان‌ان: ایران درصورت شکست مذاکرات با بستن هم‌زمان تنگه هرمز و باب‌المندب اقتصاد جهان را منفجر می‌کند
🔹
این رسانۀ آمریکایی نوشته: ایران از این پس می‌تواند تنگه هرمز را به دلخواه خود ببندد؛ این یعنی رژیم ایران پس‌از این جنگ توانایی همیشگی برای آسیب‌رساندن به اقتصاد جهانی به‌دست آورده است.
یک منبع آگاه به سی‌ان‌ان گفته ما اکنون تنگه هرمز را عملا به ایران واگذار کرده‌ایم و این سلاحی قدرتمندتر از هر سلاح هسته‌ای است.
🔹
منابع متعددی به سی‌ان‌ان گفته‌اند که درصورت شکست مذاکرات، ایران از طریق حوثی‌ها اقدام به بستن تنگه باب‌المندب می کند؛ بستن باب‌المندب، همراه با تنگه هرمز، اقتصاد جهانی را کاملاً منفجر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/442636" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
آغاز مراسم تعویض پرچم حرم‌های مطهر امام حسین و حضرت ابوالفضل علیهما السلام به مناسبت آغاز ماه محرم الحرام  @FarsNewsInt</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/442635" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58693fe30f.mp4?token=nGJVwR4Erpc5DLoIqa3_KfEXW7n1bWxSYlPwQXggAon8QOx_vANaAimoBWRH5p9nTedoQPxxs78LE2CN_W4KuCTU7kAYW5ByLX4aPE5AjgCwQEbOsKDfYULiYltpDkqBLyOl-7sPA1R9xxGMCPpDad19DTVFWLK9PyiyDGqZkYh-lA9ufeLnQx9L4BSqQPT-96UaHq9FqkcQZVyBSZMjvKLNPIChknJrxPnB5VJio8BLI6kvYt1l5jZhvU9qPmh13OraV2azPDpJzsEHyClQX-gljFgCTQZUaUyc118k2RwxyeW_1Ne7JIAJSMSNj_Sy-haaXrJCuS3XwRPzayLwHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58693fe30f.mp4?token=nGJVwR4Erpc5DLoIqa3_KfEXW7n1bWxSYlPwQXggAon8QOx_vANaAimoBWRH5p9nTedoQPxxs78LE2CN_W4KuCTU7kAYW5ByLX4aPE5AjgCwQEbOsKDfYULiYltpDkqBLyOl-7sPA1R9xxGMCPpDad19DTVFWLK9PyiyDGqZkYh-lA9ufeLnQx9L4BSqQPT-96UaHq9FqkcQZVyBSZMjvKLNPIChknJrxPnB5VJio8BLI6kvYt1l5jZhvU9qPmh13OraV2azPDpJzsEHyClQX-gljFgCTQZUaUyc118k2RwxyeW_1Ne7JIAJSMSNj_Sy-haaXrJCuS3XwRPzayLwHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راه‌حل وزیر بهداشت برای گرانی داروها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/442634" target="_blank">📅 21:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442632">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd206c8ee.mp4?token=j6uoVv857FfG43J_aM_yFYiXO77-98xhZGPN4RIr0VGWz9JsaCUnl6LyL1Dos1VD3qIn4OGMegGcHdsZxOKJMx1sWDVfYlYqHwywQzsMga9YKCrE1aLa63UuH5mZOEYVxn66nzMR_skftLSTLuUi1sBkoxkQNreY583US36QH0Dl4grqinU7uPUSSUiWwG-HeJWE9MTXIe396L9ADKrTSMeG2p1GApYEFAiji0EqMRucAUz7koCHP-O6P3L6dvq10ILev3U-R_UKD5ZZ6ejBZIMcrRkiVWHdqLAHdJpSfmEaPhS9Ovn0hQq6Aj02kCOEY02jgnADCR0G7_t93TFgGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd206c8ee.mp4?token=j6uoVv857FfG43J_aM_yFYiXO77-98xhZGPN4RIr0VGWz9JsaCUnl6LyL1Dos1VD3qIn4OGMegGcHdsZxOKJMx1sWDVfYlYqHwywQzsMga9YKCrE1aLa63UuH5mZOEYVxn66nzMR_skftLSTLuUi1sBkoxkQNreY583US36QH0Dl4grqinU7uPUSSUiWwG-HeJWE9MTXIe396L9ADKrTSMeG2p1GApYEFAiji0EqMRucAUz7koCHP-O6P3L6dvq10ILev3U-R_UKD5ZZ6ejBZIMcrRkiVWHdqLAHdJpSfmEaPhS9Ovn0hQq6Aj02kCOEY02jgnADCR0G7_t93TFgGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم تعویض پرچم حرم‌های مطهر امام حسین و حضرت ابوالفضل علیهما السلام به مناسبت آغاز ماه محرم الحرام
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/442632" target="_blank">📅 21:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442631">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp8y_1TDVvpluHMcE1yPaCEB61gRcY4QVzqHtM1HK4Vq7St-_gX9Sbsa224_RiprIUngYrbbMzWJmLHPVeYQzK-VGZDjLiW-QCxWkOoJp-tADa8Txp49sLFbR5j4RUbQQOrgcovxj67oFunGU6BoJG3jTldt-X8mnqTUUAvKs9wr8anLIieRgT5d4KN82ESq0pUJ2v8_6mUbd821WVJ-4YdjLyqNUSsCI01Rgx8RYMsEuCoLDIQ3-cDMnCkAEld12wWRkiBswX-oEBEuuUQLA0L32fZT6TAaUyWSh2bKrK7HIAJN2tMQhjVFzUOp23JqPpdksy9evh0sAWKle23DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه شماره ۴ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
بسم الله الرّحمن الرّحیم
السلام علیک یا ثارالله وابن ثاره
◾️
همزمان با حلول ماه محرم، ماه پیروزی خون بر شمشیر و ایام عزای سرور و سالار آزادگان عالم حضرت سیدالشهدا علیه‌السلام و اصحاب باوفای ایشان و در آستانه برگزاری مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای (قدّس‌الله‌نفسه‌الزکیه) و شهدای خانواده رهبر انقلاب اسلامی، جهت‌گیری محتوایی و رویکردهای تبلیغی و ترویجی این رویداد را به‌ استحضار ملت شریف ایران و دوستداران آن یگانه‌ی دوران در داخل و خارج از کشور می‌رساند.
◾️
حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم‌ انقلاب اسلامی(مدظله‌العالی) در اولین پیام، درباره‌ی رهبر شهیدمان فرمودند: «من این توفیق را داشتم که پیکر ایشان را بعد از شهادت زیارت کنم؛ آنچه دیدم کوهی از صلابت بود؛ و شنیدم که مشت دست سالمش را گره کرده بود...»
◾️
این
«مشت گره‌کرده»
که نشان رسمی بدرقه‌ی آن یگانه می‌باشد، فقط یک نماد نیست؛ تبلور همان دست مهربان پدر امت است که بارها در برابر استکبار جهانی ایستاد و هرگز نلرزید و جز برای خدا گشوده نشد.
◾️
از دل همین مشت گره‌‌کرده و از جوشش خون مقتدر مظلومی چون اوست که دل‌های آزادگان جهان به تلاطم درآمده و ملت ایران بعثتی دوباره یافته ‌است. بعثتی که باید تداوم آن را در اعتلای پرچم جبهه‌ی حق در جهان، انتقام خون پاک امام مجاهد شهیدمان و ساختن فردایی قوی‌تر برای ایران اسلامی دنبال کرد. حضرت آقا اعلی‌الله‌مقامه‌الشریف در یک جنگ خونین به شهادت رسیدند. شهادتی که در میان علمای امامیه رضوان‌الله‌علیهم برای شخصیتی در حد و شأن ایشان در جنگ اتفاق نیافتاده است.
◾️
در امتداد جوشش این خون مقدس که زمین و زمان را به تلاطم درآورد، شعار محوری این مراسم این خواهد بود:
«باید برخاست»
◾️
این شعار، امتداد همان «قیام لله» است که در طلیعه چهاردهم خرداد امسال از سوی رهبر عزیزمان (ادام‌الله‌ظله)، زیربنای مکتب خمینی کبیر و خامنه‌ای عزیز خوانده شد؛ قیامی که از نیمه‌خرداد ۴۲ آغاز شد، در بهمن ۵۷ به ثمر نشست، در عصر مقاومت استمرار یافت و اینک با شهادت مظلومانه آن عبد صالح خدا، نصابی تازه یافته است.
◾️
«باید برخاست» یعنی این خون چنان جوشان است که دیگر اجازه‌ی سکون به هیچ دلداده‌ای نخواهد داد.
◾️
«باید برخاست» یعنی عهدی که ملت بعثت‌یافته با خون او بسته است، تا پای جان ادامه خواهد یافت.
◾️
برای این مراسم که
«بدرقه آقای شهید ایران»
نام گرفته است، بسته هویت بصری درنظرگرفته شده تا مبنای تولید و انتشار تمامی آثار رسانه‌ای، اقلام تبلیغی، فضاسازی شهری و مردمی، محصولات فرهنگی و برنامه‌های مرتبط باشد.
◾️
اما این عزا، تنها مختص مردم ایران نیست. از کشورهای جبهه مقاومت تا اقصی‌نقاط دنیا، آزادگان و آزادی‌خواهان جهان داغدار این شهادت عظیم شده‌اند. امت اسلامی با الهام از همان مکتب، کلام الهی
«قوموا لله»
را سر می‌دهد. این شعار، عصاره آخرین رهنمودها و پیام‌های حکیمانه امام شهیدمان است؛
«قوموا لله»
نه فقط توصیه او، که تجدید بیعتی است با مکتبش. اعلامی به جهانیان که آن عظمت، آن ایمان و آن شجاعت بی‌بدیل با قدرت و صلابت بیشتر ادامه خواهد یافت.
◾️
به توفیق الهی و عنایت خاصه حضرت ولی‌عصر (عجل‌الله‌تعالی‌فرجه‌الشریف) این بدرقه، طلیعه فتح مبین و نقطه عطف بعثت ملت ایران و امت اسلامی برای افق‌های روشن پیش‌رو به پرچمداری رهبر عالی‌قدر انقلاب (مدظله‌العالی) خواهد بود ان شاءالله.
دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی
۲۶ خرداد ۱۴۰۵ مصادف با اول محرم‌الحرام ۱۴۴۸
@Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/442631" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442630">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رهبر انصارالله: به رهبری و ملت جمهوری اسلامی ایران، برای پیروزی بزرگشان در برابر طاغوت مستکبر زمان یعنی آمریکا و اسرائیل، تبریک و تهنیت می‌گوییم
🔹
ما همیشه آمادهٔ مقابله با هرگونه تنش‌آفرینی یا تغییر اوضاع از سوی دشمن آمریکایی و اسرائیلی هستیم.
🔹
این آمادگی شامل هر سناریویی است؛ چه زمانی که کل منطقه را هدف قرار دهند، چه وقتی که بخواهند غزه را دوباره هدف بگیرند، و چه زمانی که به هر بخش دیگری از محور مقاومت و کشورها و ملت‌های اسلامی دست‌اندازی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/442630" target="_blank">📅 21:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442629">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef5de62c7.mp4?token=v2pkv4SSVFVmUOpRXnd12VRIpnycmRBhU6J3GEIDilWTVQGdSbXiypcNGZ4d1Lxq86_HZg6WDUC9-P6qnCFsym-Ao595S3EJsQZWWl5DOJx_OFfNX8zplBuC8VgkzEuIEaN1GWzstj1C-nCQYzv1Mzchye3X0GEq4Y7lOlqGx2EoVlN2KaJBr3nreTcGhHovsyHA2LOdbVE_0hwsv1dT2hH2iPK9PMaTSDTbHs_9AHVizld-qQ9Dfs5aUIsjIADKgGSozjqNNsuTLx4eWT9wLM8Yt7e-FZDAUp_LZbwgtANN5BypKIkV3LkClgObchTmvy5VtQ4_3OF_72uV2jRqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef5de62c7.mp4?token=v2pkv4SSVFVmUOpRXnd12VRIpnycmRBhU6J3GEIDilWTVQGdSbXiypcNGZ4d1Lxq86_HZg6WDUC9-P6qnCFsym-Ao595S3EJsQZWWl5DOJx_OFfNX8zplBuC8VgkzEuIEaN1GWzstj1C-nCQYzv1Mzchye3X0GEq4Y7lOlqGx2EoVlN2KaJBr3nreTcGhHovsyHA2LOdbVE_0hwsv1dT2hH2iPK9PMaTSDTbHs_9AHVizld-qQ9Dfs5aUIsjIADKgGSozjqNNsuTLx4eWT9wLM8Yt7e-FZDAUp_LZbwgtANN5BypKIkV3LkClgObchTmvy5VtQ4_3OF_72uV2jRqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرکل خودرویی وزارت صمت: از امسال به خودروهای مونتاژی با ارزبری بالا و ساخت داخل پایین، مجوز تولید نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/442629" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60722f8d84.mp4?token=CcpycI6vZghO5jq4MmZE4Gg6aN2s2Sy-seq4VJ209qlKl8wssCY-OmVEbAWg3njzRznHZr3538FLCkFl_FezyWBddDkuzOBlYnp04R1RM4VnIMdtKoWmbPVOZIRR15muAkT2atJ82GzltXXmBEWNMVhqxC-4JdBcJYI8Gs02PBNhpw9-0QyZGcahgxtMx8p699tDFgK0KpczkgPv0tXF-64OggzDDcqyMGChk9wIxkdks43neYMdsf9PGKhkvLu9ZZsmIBlihy7VAntlA58ouI7TiM2BEFeoCP3SEfXD7qgVT14r6LYORpqLBD37I82gTpMbMRTzKQU1Py549CJ8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60722f8d84.mp4?token=CcpycI6vZghO5jq4MmZE4Gg6aN2s2Sy-seq4VJ209qlKl8wssCY-OmVEbAWg3njzRznHZr3538FLCkFl_FezyWBddDkuzOBlYnp04R1RM4VnIMdtKoWmbPVOZIRR15muAkT2atJ82GzltXXmBEWNMVhqxC-4JdBcJYI8Gs02PBNhpw9-0QyZGcahgxtMx8p699tDFgK0KpczkgPv0tXF-64OggzDDcqyMGChk9wIxkdks43neYMdsf9PGKhkvLu9ZZsmIBlihy7VAntlA58ouI7TiM2BEFeoCP3SEfXD7qgVT14r6LYORpqLBD37I82gTpMbMRTzKQU1Py549CJ8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک خودروی نظامی رژیم‌ صهیونسیتی توسط حزب‌الله در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/442627" target="_blank">📅 20:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442626">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaJ45AfaYTobmVOWggcO2P9Nk1FrFAk9kpGGoF6bYbpKQzrEuAcXWEzcr5_LAPBRAm8zwcKRSkenoFLTYdtO1L4nlRmThC5k80agoKnZuOlVxvI2J1eYMiKqnEXf7GSV8SwG9rSh9DNTdvk2ZPYLEMQWbCTfIcGxSR2f8QM7G2Lcgl_NuSLpRH_q-JjtfnQCC22EeHGXxCCNOx2IStSKxCHuKPUEngyDGRYhm_5CWfA2BfbZv51LmWZkCqv2lXG-bSYDkljEoCrbXhGkUdWWWNyub250kSxWF05U-u1YJ0ZYIXaqXodgyCSGwwiREk2cgOISjUymyNNO8Swk8fUPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین دیدگاه‌های موافقان و مخالفان مفاد تفاهم‌نامه و مذاکرات با آمریکا را در فارس تعاملی بخوانید
تازه‌ترین مطالب و یادداشت‌های:
🔸
محمدجواد لاریجانی
🔸
آیت‌الله میرباقری
🔸
سعیدرضا عاملی
🔸
یدالله جوانی
🔸
حسین شریعتمداری
و...
را می‌توانید در صفحۀ اختصاصی هر یک از این افراد در فارس مطالعه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/442626" target="_blank">📅 20:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📌
مهارت‌آموزی هیجان‌انگیز/ چرا اتوبوس‌های خلاقیت، میهمان مدارس پایتخت می‌شوند؟
معاون شهردار تهران:
🔺
دانش‌آموزان در کنار آموزش‌های تئوری، با لابراتورهای سیار شهرداری، مهارت‌های ساخت محصول را یاد می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/442624" target="_blank">📅 20:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoBFqLdQv-kvxcDLUiVeqa5hZPCAdAbs6GNL_BEOvqZLeNoc5Pz07csERZX3pO8n8WW2F8JaD9hrnDPxuNbCJcpsO-ybdPig3MmSjHrkEm1QnkqjUFIPMJ6HIxWxZEpv0jcmja5qny01tca6jHkRBYT5U1vcVfA9fPyHYY5agj5ikKoRNHgAHNvOO2eS-5AQzDr90ZmMVRoPALUMtpjMMNt39hPIpr6BeMUx1OYuc40W_VlNebdxeaBTbl1Fxx3pjtiti0XqmblB-seARc7ueieIF5pUnEPOMnOdaFMv6_miqAN5p3L4juvj4U0wMgBsJkrh5BdPwkt3X-Bzi2harg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
فهرست برندگان ۲۵ خرداد ماه طرح «فرالیگ» بانک رفاه کارگران اعلام شد
🔹️
همزمان با برگزاری رقابت‌های جام جهانی فوتبال ۲۰۲۶، فهرست برندگان روز دوشنبه ۲۵ خردادماه طرح «فرالیگ» بانک رفاه کارگران اعلام شد.
🔹️
در چارچوب طرح «فرالیگ» و همزمان با مسابقات جام جهانی فوتبال ۲۰۲۶، در پایان هر روز ۶۶ نفر از شرکت‌کنندگان بر اساس امتیازات کسب‌شده و از طریق قرعه‌کشی، به عنوان برندگان جوایز روزانه معرفی می‌شوند.
🔹️
طرح «فرالیگ» همچنان ادامه دارد و مشتریان بانک رفاه کارگران می‌توانند با مراجعه به سامانه «فرارفاه»، تا پایان رقابت‌های جام جهانی ۲۰۲۶، نتایج مسابقات را پیش از آغاز هر بازی پیش‌بینی و ثبت کنند و شانس خود را برای کسب جوایز روزانه و همچنین جوایز ویژه پایان دوره افزایش دهند.
🔗
فهرست برندگان
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/442623" target="_blank">📅 20:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/442622" target="_blank">📅 20:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2T1gYI1qhRM54VC-Yb0p-fWFI3nICaFvirhaVzw8xY0MRVMBURc9liDz2mLh-eHWVg_GVdvftIOhvQJYQhJB9ARaWZMaZk5k2x04HqfKrqGC-Eoa-_La__ZsBOGdwewmjk3Op9rE-_5K35Ad7yuWvffV2BFmJ6sUnjVJVt6B41RA46K-tw19P7Lh5pBzu8rhHPSEub0yeKuwwflTr8Cri4I4B5yI9RheJvfZGnor5Lg48ZRz9PEBtpRsJJRhgjqfYfhygPeLryi8Z_wVLw00cKPoqcP2PhgSUm2gC2YRrmmmO14OMRKdUvUFNcxEYSKPEaE_akjVQ0hAF6qyfg61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv4EMwJ1dE_swzAxZU5_DTiUr-ZyBvIpMaT59ST3oITp5qYapkDjGjG27SNgtL2e0d7wvumafdTYVtQ3HtZghHbFfhojY-lAWiZZefXUuHCsCYSj173QzP_1_8Vb6kuv7yl1_jwk_apYinw9t-Xl8mirMnmIw3PqftmK7sf0qX_qKCVwCO9XWusiWcnt454L3NE-r1D2HGotJfmuAUEmhKSF9W2KrQR-ggnT9epIU8s-C4qnOdwwy5HEo87OLu9FeMwRNO5Zr8pDhls62NMyxBewRiPygwfU2xkkwkObuMUPQyGP-8fcViH7mzkobCIYuQ4nZLXSU01hTx0SNTAcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZgQOfw4YQ2UXe7FcHah8mXiK7KOLJ1wWMbH7W3UZiT7JlOppSA2zdCWcMapWFv6QHZcenrWi64oDyD5KTG50iTMADC8NEsV6Ny0GSP9hKYQlHxuWA2a2aqMstQYbGXVhgfL4h0GeSC-FDuT3L8sidOKIauGs3b77gvdUHhkcEwZr335dSRYYrnP3fWoUkWQ7_4ULk4JoZzTJkkg26yLxq0o-LnZXOOmGlpHnKGWdqG0alE2G03yx1A7e5jbXVzUDo80gvvgkoa_v4uYnmWGFJUrQFvCPgBIAn_Mei_iL1DdJe9Z9zQG1QTpY4LhLnMzBqr-_mFolCl-HJrx8V4b_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3GqiyfYZkb-QWmhyeUiV8dzdLVBqnALG5WW_PlUcYHsjRPySrp7J4tgM7ogswAp8QvCPy97LrV-3wx1nio1PEOXctsfsc4Gr6Ma_6wfAi7v083t7DtoEtaTuP3XpSG2jrBVmO3IL-8ArDziXTExsaGzT4OoFgMV8TQZKNlL0K3C8A8yomfb3sB_0NB1iN8m-ZB2dch7LnUBVLgBMk3kWEjUi_iYtsIGDPhqu1QKl54V6umEG-VHe4feZ9tNaIO-VVnCXACMgXsxsX985f5P5Mt42gasetM2xxE7HkpZY2q6fdPdAL-jInr76BVqJ6n72wuG6y9vG3g-IaHCHG9lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-x4H5IfPhXZWNX4z6ti-6IKiNka6neCCTQo9q23_iTBdtYXgXJn2M9DaSJ8mBzb4gHtytPX34WV5gt0eFGzdYjN-YfYx8d35Pd5UGryU0K-9o2kYLsdBP4FaynsQ38CBOpvjFqnHiX5KxuT9GmdK0n-8Idq76hwXDn8ObDLQvu6anpSAVxJ87t1-stYlzWesguwppRPQOapl0iIVsVHbZjnkP2HXe6DdkvzXOZuvKe5xNp4dc624qUfwmfk1Pd-cSOXNpPVMnOhutnhvNlXn490nceZwUY4d4WGb0o8VTGZxiH1r6IGD0d0x4TG6voxhan8DHFhYvs-80LyqgTwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHeFlJ4NyiggXCrBkhTIVwVS2JBKlaAbYVNcCVWL1n7kcn2ZGNqpbwWs4oSiZadYc2zNdiX2uheSpR6MlNVNf6PHZpE1w9ONL2khiUy1-Vi9Ut9JXHK_c_5EFkx8VIyuClBeLnUhHOlFwc_gXvvVoi466daBcmewNJqozmVzKkHNJPyGS24SIPGVudXThF_gdyzsfdoLD28xy1TN_IaQDLo2KN91nuWUyq1xLASqff3cXf-jpKbzZPTm4sjyQTMvMOWJpk6WX1vaLx2jwMDBp9y4yNP6Fa2fwvPdh5eqTPTB_S2Yw36_-m4cvBXIaZDV5IaxNUlf2i_t2JWT8cmTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlzhS0JQTOJwoVmKXf4Cdxaj2LUXEOpjxmeGW445xbGLKKhangeyFDzVNvE9i18ffKM4_B4-fnU_qgE8RL2mzfn2fF4r-TemFkaKhHwgbBLrIHtiqKOKhO2gfuYgiYYVh7ibkiQThs_0Iea4FE_wIgU8BqxQgwPb1DffcHfC9PH9alsw6qYSu_8zud3TdWQUp5kCCTeQEgyIqpuUgOTVwCpqXVl0Vzu1S7P5iISX8NvTb-z5qFLedB4r9pKoKjS2ha2KA8Wy_wpaXxSfXOI0qT13uPDbHNFGU1SAOMNm-CScDV_a3s3u-G4rEMjRhaz1-KDQYXJyiSNDrmhFBEBhBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تمرین پرسپولیس زیر نظر اوسمار ویرا
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/442615" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyS0prJ8_Q3bcuYzN1Lm0gj3fUUVZl-sJTJP4cTbmr31hiwUe5B4NmySILVBpJ16Z5-5m4Exng7o_ceTQu0MMUCvLcMgxPMsq_YlxnuAKMc6RGr4uhIStJUASiJgXVwxnRNzeDKoS8TcGPmHVIyZSqxXiNEw9qGFAZk6fGQYwl1RyXCfpJPAPsipEZH54cXvDBklmWRZm0yDYJFng_ZVA3gPccHq-DRAUXhSkR2g3FzlXSEN8m2NYCl2kFnIiDnC4rtRe9CoxLjkp5Dshk7tPOnw9g9ToTC4XR9WxxkF01lkAqE_XrsirocnjsWZ4sFUbLRDHoJ_do85Y7IvPaFCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هریس: ترامپ دوباره ما را به نقطۀ پسابرجام برمی‌گرداند
🔹
رقیب ترامپ در انتخابات ۲۰۲۴: ترامپ هر مذاکره‌ای را یک پیروزی جلوه می‌دهد، اما در نهایت آمریکا به همان شرایطی بازمی‌گردد که پس از برجام وجود داشت؛ توافقی که خود ترامپ از آن خارج شد.
🔹
تفاهم حاصل‌شده صرفاً «مفهومی از یک توافق» است و هنوز مشخص نیست در روزهای آینده روند مذاکرات به چه سمتی پیش خواهد رفت.
🔹
اگر رئیس‌جمهور بودم، هرگز وارد جنگ با ایران نمی‌شدم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/442614" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e815bcdbf7.mp4?token=QHy76N0Qqg7zJBNiJery96NTIcRDjAjvUFT4Sw5tc96gILtK1STeDz2fy-og-QIgJyy0n5BWBmfaJqWYsC54FRzDPpXXWE1WCqThcabFPz0DPZqUhA1kka1_-5Ic9XVcjdt-UmO_LHrk5cjDC23ViEel9xLUxp0A8R33pUqeMb7R4HYusq25YiaDpPrW7Vfm69o4Aot86D4-F-99Bl6bivSV3qyxXHEWIot96Tr3g5oj_ttxssOqWo4fobvh3QJGVwwOiCCda8RfrwvSrJM18PAGIF27palFQoVMpDK8C_1d4trZaH53BR3h-MD0l6xr9O2eLhlTtJlKQBgt6feSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e815bcdbf7.mp4?token=QHy76N0Qqg7zJBNiJery96NTIcRDjAjvUFT4Sw5tc96gILtK1STeDz2fy-og-QIgJyy0n5BWBmfaJqWYsC54FRzDPpXXWE1WCqThcabFPz0DPZqUhA1kka1_-5Ic9XVcjdt-UmO_LHrk5cjDC23ViEel9xLUxp0A8R33pUqeMb7R4HYusq25YiaDpPrW7Vfm69o4Aot86D4-F-99Bl6bivSV3qyxXHEWIot96Tr3g5oj_ttxssOqWo4fobvh3QJGVwwOiCCda8RfrwvSrJM18PAGIF27palFQoVMpDK8C_1d4trZaH53BR3h-MD0l6xr9O2eLhlTtJlKQBgt6feSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان به خبرنگار خارجی: مسائل داخلی ما به شما ربطی ندارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/442613" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال دربارۀ معافیت‌های تحریمی نفت ایران
🔹
روزنامۀ وال‌استریت‌ژورنال مدعی شد تفاهم میان ایران و آمریکا این امکان را فراهم می‌کند که تهران بلافاصله پس از امضای توافق، صادرات نفت خود را از سر بگیرد.
🔹
به‌نوشتۀ این روزنامه، معافیت‌های تحریمی تنها به فروش نفت محدود نمی‌شود و حوزه‌هایی مانند خدمات بانکی، حمل‌ونقل و بیمه مرتبط با صادرات نفت ایران را نیز در بر می‌گیرد.
🔹
این گزارش درحالی منتشر شده که برخی تحلیلگران معتقدند دولت آمریکا ممکن است همانند تجربۀ اجرای برجام، با وجود اعلام کاهش تحریم‌ها، موانعی برای بهره‌مندی عملی ایران از مزایای توافق ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/442612" target="_blank">📅 19:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1db2a80a8a.mp4?token=hqy4VYyYBdtbzWpbpffEGca0Hxgi5mdFNacRmdVMbhbU8AscBJWgfKdHfcwhUjVueaTfeZOfPmz0MtaohXTq6NxdrVROItz6MQnC0hZnkJAh3cigWAky9odsaoERgXqXiSc9Vi7jhLQ_YJt3oNLZZ_SYlrnkaMtZSHBHlahzyAbySjUql4YIklos8bjBM1PRGONOZM7eeWTNrp2Fis8MtDrkdvp3k7DmQPMsJxwurQY58muSHZiU-TxdZ7r4ku8Q24XXhObZLhzInC4NW5QMG9Vw9jB-Mc_nwJyRjMswd9QPT4pXgT18pk2juAYsVsiHCV0PJJNzoyGoNGjgtiIyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1db2a80a8a.mp4?token=hqy4VYyYBdtbzWpbpffEGca0Hxgi5mdFNacRmdVMbhbU8AscBJWgfKdHfcwhUjVueaTfeZOfPmz0MtaohXTq6NxdrVROItz6MQnC0hZnkJAh3cigWAky9odsaoERgXqXiSc9Vi7jhLQ_YJt3oNLZZ_SYlrnkaMtZSHBHlahzyAbySjUql4YIklos8bjBM1PRGONOZM7eeWTNrp2Fis8MtDrkdvp3k7DmQPMsJxwurQY58muSHZiU-TxdZ7r4ku8Q24XXhObZLhzInC4NW5QMG9Vw9jB-Mc_nwJyRjMswd9QPT4pXgT18pk2juAYsVsiHCV0PJJNzoyGoNGjgtiIyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابتکار شعام برای خنثی‌کردن بدعهدی آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/442610" target="_blank">📅 19:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-xGUV5AEzZFFenbeJWCHVAbAs6iq9TbcmvZIv-EMW9bf17G2N7eKxLbNo7ZCBPCiWZSJ3FJQOjl7OshtOgw3ETlSNjFS5as-nM0OrzfdYanrymzO6PWXx7sNpGjhnJ-pX7mdZo37-KHc7s-mxs96IUoWzUEJ2wSi-M5FGSxScbTtu-CsREVL303dGvCkFyXv1XioOZ-AMNaWcdwVTTnsa1V6DfKPoNZjoet_kuN8ZjA_-dqYRZ6RjhCfD8NphaDF9LqwD_qubPrrFf2FW625TzcWjaZegDXCFm1cUiM1THZXyFlCXvD5ph3W36upYALw-hLiBUudTpMVpXysf8p_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای اف‌بی‌آی دربارۀ خنثی‌سازی طرح سوءقصد به ترامپ
🔹
اف‌بی‌آی مدعی شده طرحی برای حمله به رویداد یواف‌سی در کاخ سفید که ترامپ نیز در آن حضور داشت، خنثی شده است.
🔹
به ادعای مقام‌های آمریکایی، طراحان قصد داشتند با استفاده از پهپادهای حامل مواد منفجره به ساختمان‌های اطراف محل برگزاری حمله کنند و سپس افراد حاضر را به سمت محل استقرار یک تیم تک‌تیرانداز هدایت کنند. همچنین برای مرحلۀ بعدی، یورش به دروازۀ کاخ سفید نیز پیش‌بینی شده بود.
🔹
براساس گزارش‌ها، تاکنون ۵ نفر در ارتباط با این پرونده بازداشت شده‌اند و ۲۳ نفر دیگر نیز به‌عنوان اعضای احتمالی این شبکه تحت بررسی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/442609" target="_blank">📅 19:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
چرا مدل موی فوتبالیست‌ها عجیب‌وغریب شده است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/442608" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-68.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/442606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۶.pdf</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/442606" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtFyL6DtdpEXRGjLIbwYoMitXW5iCM3r2L587FEpegQalJibWSjOdMHSLhvlRQRN_e78OVzkV6dnb6bzwmnHNkhdfPpGCO83tUkDO3us1oE5-v621psCK4ALLufnDl5t4bULcRK20_-LtMW2Xas1JAHSM8zfGXMI6ALgeSsGXdUOfFuIjiOhH0a652XJo9SGTs3CFeFlR6PCT26B3BfibrVpmSanytBxAV0DfidRDYOXyItfCgPnzMBUg_AclbZMTf13A3Y65ePesD-GKAbZdvo23e6ssTIOHJkg_nEbuvdVn-eyk0xKc6fy8UkAbwvIxff_A6__0VuQyH47XS2UcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ حذف تدریجی چک کاغذی به شبکه بانکی
کشور
🔹
با ابلاغ بانک مرکزی، بانک‌ها مکلف شدند نسبت به کاهش تعداد برگ دسته چک مشتریان حقیقی در ۴ مرحله و مشتریان حقوقی در ۲ مرحله با فاصله زمانی حداقل ۲ ماهه بین مراحل اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/442605" target="_blank">📅 19:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adbba6886.mp4?token=CjiFp-cRerIMPy2cLcJRhWVDsvFd9OPLPI3h6rVbrkB-ZBqj1k4JUgCn7qfwX-CrFqKpgR0hXrxG2HOnSWNFfvH_61uqubbSF_DHSOVCpo4vTmNkgy4i3vfA1opalpJOXXElTF7oeGhiDh4DE0dFmG_vvkjeumX2E2dFmorrCT8t4rfHukQ1UDSmk7huubhOsAAvG9oEVWhs1_ytAXQ_1RQPDn_MAIRGhvA1KiULerctyCJ88_IET9O18AqB5bliYOFcACLdcCy2sob7AOmlr9x8ZlSpndLiNF2QS7jj1sP39flXt1DP3SCTurjFV1P1zylBSKOHF6_rXEBF30kF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adbba6886.mp4?token=CjiFp-cRerIMPy2cLcJRhWVDsvFd9OPLPI3h6rVbrkB-ZBqj1k4JUgCn7qfwX-CrFqKpgR0hXrxG2HOnSWNFfvH_61uqubbSF_DHSOVCpo4vTmNkgy4i3vfA1opalpJOXXElTF7oeGhiDh4DE0dFmG_vvkjeumX2E2dFmorrCT8t4rfHukQ1UDSmk7huubhOsAAvG9oEVWhs1_ytAXQ_1RQPDn_MAIRGhvA1KiULerctyCJ88_IET9O18AqB5bliYOFcACLdcCy2sob7AOmlr9x8ZlSpndLiNF2QS7jj1sP39flXt1DP3SCTurjFV1P1zylBSKOHF6_rXEBF30kF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اگه برای چالش‌های تهران تو شرایط جنگی یه ایده یا راه‌حل فناورانه داری، این فرصت برای شماست
سازمان فناوری‌های نوین شهرداری تهران دنبال ایده‌ها و طرح‌های خلاقانه از سمت شرکت‌های فناور و دانش‌بنیانه تا بتونه تو شرایط جنگی، چالش‌های شهری رو بهتر و هوشمندانه‌تر مدیریت کنه.
اگه شما هم تو این حوزه فعالیت می‌کنین، می‌تونین طرحتون رو ثبت کنین و هم تو حل مسائل شهر نقش داشته باشین، هم فرصت همکاری با شهرداری تهران رو به دست بیارین.
📲
برای اطلاعات بیشتر، عدد
۱
رو به
۳۰۰۰۱۹۱۵
بفرست
🔗
ثبت ایده و طرح:
https://deftech.citex.city</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/442604" target="_blank">📅 19:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442603">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdVe8OkIbFDSjsHOuq3c8-jOjyo4evXC2djE_GvctUQg0l8lTug5m7sEY8GF7-u0_KrMtPd7j7lZqVwewHe3prg_cms1qspyd2KEdeaYHXkpEDgN0fixJ6qOFOWCavDN8keddZHVKXVsx7_FS7p05dQDkn794Z2lIaq-zWK-EwnPAxVz2CcV4rHRvkedj1Q_3rMMfi-bf7VIqokLO0npGfvzUunxkxMEku6cxBOe5EPyfJgAMyBhkZ2XLEfbzOgbgWJqKp2n9Z1hstgddQeQDuZExMVdoJ3fIkWweyw7p--bkNqs-4JAM26Na3LXnPoKsJ7rRc_yhLSeQdBBMaeOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
آفریقای جنوبی «مس» را مشمول مشوق‌های صنعت خودرو کرد
🔻
دولت آفریقای جنوبی با افزودن «مس» به فهرست مواد معدنی مشمول مشوق‌های صنعت خودرو، بر نقش راهبردی این فلز در زنجیره تأمین خودروهای برقی و توسعه فناوری‌های انرژی پاک تأکید کرد.
🔹
کمیسیون مدیریت تجارت بین‌الملل آفریقای جنوبی (ITAC) اعلام کرد فهرست مواد تحت پوشش این مشوق‌ها با افزودن عناصر نادر خاکی، آهن، لیتیوم، گرافیت، مس و کبالت گسترش می‌یابد. پیش از این نیز موادی مانند آلومینیوم، فولاد و فلزات گروه پلاتین در این فهرست قرار داشتند.
🔹
قرار گرفتن مس در میان مواد مشمول این مشوق‌ها، بازتابی از اهمیت روزافزون این فلز در صنعت خودروهای برقی است؛ به‌گونه‌ای که میزان مصرف مس در خودروهای برقی به‌مراتب بیشتر از خودروهای متعارف برآورد می‌شود.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6R5
@mespress_ir</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/442603" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/442602" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbuG2CoVco0a0RhUQbuVD3FBxGX6eGdX_LhpCgzEcTkzet1pIPkX6rZP1RiRipWesOzTA-rZNs6kIAy9Y-EPytkIferHpSQm8rXSpLSvlGD4VLTb70tWMGZ0Tz3GK6KkN2Tdd3uZzMFfJsKhym3Me7cKHkD_KUUxGcdMTgwaAHyAdtElIAv4slHJ_0mQP-D7dylrTMe7fGFMUdr1bDHi2o6xH9ryRRQirntmWpWR1citWZgrSCYbKZYOX6nHYFlgl9UzMXH0j_MPHBuefg597SEohUZRM30d1jIor7Av6fPY-0EZBmILqsLzUsyuu_H-_V22OhJVyfCCm4WQ79vcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه صهیونسیتی: احتمال پاکسازی کابینه ترامپ از مخالفان توافق با ایران وجود دارد
🔹
اسرائیل هیوم گزارش می‌دهد که ترامپ در حال بررسی «پاکسازی مخالفان توافق ایران» در دولت خود است.
🔹
منابع آمریکایی در این‌باره می‌گویند این مقامات شامل «وزیر جنگ آمریکا پیت هگزث و رئیس سازمان سیا جان راتکلیف» می‌شود.
🔸
پیش از این، رسانه عبری از مشاجرهٔ شدید میان برخی از اعضای کابینه، از جمله معاون رئیس‌جمهور جی‌دی ونس و ترامپ خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/442599" target="_blank">📅 18:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQityupOJVWe1Wcg2Uaq66ayxdpqd08t1OAGuOyN_eQaLpypgnlMp2uVejaTtkzjGCm5BRaHj7SlxmZPu7yyXQeH4Bkl06LsMCpoii-q_wuSs8ho4e0pTCeN912UfI1dwXVhoMxMvIR5C_4PCd_q_i5XRIkRjUxLylVLgqPgHZswUIaPehvHQ74TKvgkqhA_7X3vDMzTPDWCoY84ci2_nooKnyS7NJsm9ZjzscNTi-jV3cfTX8p1BuU8i1mmH6uCbBqpYN0xdxceUzgG6OZSv_QU2D0haWDsZvCSPc8QPuSYsrX2iscRhYNhYXg0JhWYom-iVxt5Ye4C2Bx6A6N8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اگر بخواهید فقط یک جمله به رهبر شهید بگویید،  آن جمله چیست؟
🙍‍♂️
جمله‌تان را در یک صوت حداکثر ۲۰ ثانیه‌ای به
@Fars_ma
ارسال کنید.
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/442598" target="_blank">📅 18:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e5d3bb29.mp4?token=cmCufbtN2-xa-n5F1XqxPrZ_SJ7fiLDm5Kll9DUKmXVXhCeG7OjzQKjsSlUgsJ_B_tf4ns-daMc29HmInecUE7tQI0QuXl5isa9_FdMtlqqFVnT0qWlOMp_a3c9MtZyyn-eEO_aZi8_TzjAKmKxXzIL_PnepsEt7HiVI2qxxKO5cCJVhc5B4k38XlyCW3H1-yspTuGnSQbMBKPcGx_Jb2AO4XtL6jsW8uhjMYuwBKtfXcvdCiIuq5pO9GvmEfs6_UnU_FxMjHvkynaCGXWVp3sVzWw2qWXL7n0-Bn1EhXDGuCilFhniZAWGplL6MNtBgbnmZWOa6yg39QgFqO3yN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e5d3bb29.mp4?token=cmCufbtN2-xa-n5F1XqxPrZ_SJ7fiLDm5Kll9DUKmXVXhCeG7OjzQKjsSlUgsJ_B_tf4ns-daMc29HmInecUE7tQI0QuXl5isa9_FdMtlqqFVnT0qWlOMp_a3c9MtZyyn-eEO_aZi8_TzjAKmKxXzIL_PnepsEt7HiVI2qxxKO5cCJVhc5B4k38XlyCW3H1-yspTuGnSQbMBKPcGx_Jb2AO4XtL6jsW8uhjMYuwBKtfXcvdCiIuq5pO9GvmEfs6_UnU_FxMjHvkynaCGXWVp3sVzWw2qWXL7n0-Bn1EhXDGuCilFhniZAWGplL6MNtBgbnmZWOa6yg39QgFqO3yN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: عدد ۱۶۸ در حافظۀ تاریخی همۀ ایرانی‌ها ثبت شده و فراموش‌نشدنی است
🔹
فراموش نکنیم در یک سال گذشته چه اتفاقاتی افتاد و چه هزینه‌هایی کشور داد و چه کسانی را دیگر نداریم تا امروز بتوانیم در مورد فوتبال صحبت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/442597" target="_blank">📅 18:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDO0H4e5b31tkGLXU7yywe7H3uC4pxYbfxxmavsd6XOyOkYNCg2ixwv5zj--RLZtWwtknmg1A3iM_rcRWfZQaCyKEUJbNFM8jYsNGikkbwv-ZeGWfjReSy1bvKT3TRVRJhT_HWCtt1ID-KGg778ffaw06fA6-giED5nff3R1Djg8Z_4xovFdUbWncRECYzTwkHowHrj-4sFCcNEsK2SgrVDylGHdyyRNc1imepUf2WJ6WBrIvUxazbVzsXX8uuQNdfNVk39jX7j9JdtLV7SW8Pz63RBA962dWNzgaXAsY-_yekw8TiAU5jgoZpJDO1ifUxNX79QBa4Umc6ALZ2F6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D79lXwKaUsR64BjAM7VgYJEIwOEhD_ZM8kccTaCBUY2afAcbEkMyTLKiJk1vDHcwvdaJLqm6jH3tX320YACGeaSRjXjTsAlvna2J8seMtfGwsawwZfZ8UIwKK_21RK3w8xUksAGaBxglmUb-INm--FskqCDoavboqUe3P2KGwfL6SSU6EAUoZrUTodfMIwmDa_hx4xWKiH8oeQD-aobEGIj7i7O0W2UaJjPyYcC5QR4KsFittl2lWufJjuaMESi6JeahsHqQwmg64HXk5EuCOxovAX-nZQnZPuiwZhtCQ1sGbj1X-2IcFO_mjMIDO_gXAPZq5h-Oy_vwHOJUG929Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Grt9UR8tIRbppGJWVPzfKWNSGF15HlPE6La7r0nbVUCY9QLeMjfYPEytQB_G7cOUWzGYokBXwZlsMzEqNqq8J8bGTFJ0F6Vvo31bHRtqAJlLhbRBUKG_mtFk5HJNXnI9C75ssC9BOmSDAwC1dvehLmFAJEysOcjn5e2_gDBnoQFRMXv2x4BRhI2AJtR75LNe5PUQxVA04hoMd_e27-k0WTWEWzpaA4H3KqJcTSxzCt_DNSy29NnRyjdTfLOR3hqhw1U4UcByWBTO-sikSY2s-16__ZUA-VnWjW5Fyq-XAkGaKjB3lO-pj4gDgD6aauacDnSZ519WRqofJjEVmqkDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_73A9vrxp_k3iTrS5sLrlLjCMP7XTaGGR6TGp7G6ivnasI_GRmMyvx9sce4DlIYv6ItnPYlNAu0MaPdFpZkfbEugjWT2CI4UnGOFb_Oqc17NG30ubvlG4U3huDZEf32-8s31qwP93iEAM58rJOiB4wC08jSqFj3c7-uw54_s7EuYQ-xJV383HE3p8QOaRJbqhRW7aDLRenGs_JoiC-qywM3RNME_abNEMch9lb15yvApKbk82LqgN0MRuozf66Jy_l30lbDd43qXloeJNB7nro-mYfsBN-Erf0nzwJwOi8Po1ruzqV-slsPP6K2p8oeDhy-ymLW84QOgzj_FhFBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDP6HUtic0vezCJTscZqYaoh_2nR4pcB3Oy4Fe6ry43BjPm8guGAtVM8i5U6HAIy5EJrEmEsITwK5fgd4fE4vLIM1bXpFfOiU4Gs-zVHRW3pR3qf4hSyTiZ2dZz4al0joGPPI9KSmu0doLMrwkgTKa5ZGLeXnreWcmFgqyVLKbAjccF_Nqf3BDAlUJezQA6ZpJuyqKXs266P1_Zi8L6EIEsOtdHwWbsWVrmO8-DJP389d9M-QNzYfh1nvMB6VqhsgNhkHguG-0WnTT0XEwTuZ9LJGO0S7J-L4C0YlTNwMP9nZBialHQoU6Fqnnmv3Rur8eHiw8THOAMQr_Wkb92Y8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J013RZoP48kabpz3sYyO86e3TUBV08Eeb2tq8W5OgXjw7KfeaND53-U2BE83153YyZ28s8YBzFVDFGx4Ch64Gzu7b8GhJvKFGtTgvYAGGVYOjZ8A_tLbYvqFXLSajjwqYPt0gnKoNlKm9GM3sIBu-iGmmqEckAijjUx7jIT5O1Ul076_Rwp7mncy90jTPzC1Yo7_VRbRBHS-8tUj8BoMdeaF_n4aP-9q9f3xz4G1aERdTuGHUD4oJJtMc_FRGsl1yCCMOOJWZycrA0b3t6PJCAvnpn_GUnBa1QpTuZIV8lTZugsLMG-VEUlmFoZkjDuUB9BjGWiRqZj5gg7NlZ2Kew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار با خانوادۀ سرلشکر شهید شیرازی
🔹
غلامعلی حدادعادل، اعضای دفتر حفظ‌ونشر آثار رهبر شهید انقلاب و جمعی از اصحاب رسانه با حضور در منزل سرلشکر شهید شیرازی، با خانوادۀ این شهید دیدار و به مقام والای او ادای احترام کردند.
🔹
سرلشکر شهید شیرازی، رئیس دفتر نظامی رهبر شهید انقلاب، در نخستین روز جنگ رمضان و در حملۀ آمریکا و رژیم صهیونیستی، همراه با رهبر شهید انقلاب به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/442591" target="_blank">📅 18:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926e5026ed.mp4?token=OLmRwNzA7HkJaDnBZzMkbM6ljcq7--Cc9ogw4srvsp2d30czSTL_ondvVuwhLK-In5FxlGaXHzsI7ifq2V5ib4Q6M74AItb4Qka-og8OPengcAKYYUrcyge8UwJO2483fHO6ijtf_wcaOOicaWYbskhvztwy6-BBCq2XMMJ_mpcqt8Jx09e9xBZQgw4BhaAd6nhIyYWWKk74G-JkgZx_NBCRU17zEkLDBMHbq4xruFU4dtW9MNeHCvt7zrCysWTCPTCmUvjaXYO2EASIatIq7HfjdT3vFr5lh-KvYJkuLg7m9yep-4cYy2MhYaGMw0-HsLcO35-r00wSOQxQz2ebxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926e5026ed.mp4?token=OLmRwNzA7HkJaDnBZzMkbM6ljcq7--Cc9ogw4srvsp2d30czSTL_ondvVuwhLK-In5FxlGaXHzsI7ifq2V5ib4Q6M74AItb4Qka-og8OPengcAKYYUrcyge8UwJO2483fHO6ijtf_wcaOOicaWYbskhvztwy6-BBCq2XMMJ_mpcqt8Jx09e9xBZQgw4BhaAd6nhIyYWWKk74G-JkgZx_NBCRU17zEkLDBMHbq4xruFU4dtW9MNeHCvt7zrCysWTCPTCmUvjaXYO2EASIatIq7HfjdT3vFr5lh-KvYJkuLg7m9yep-4cYy2MhYaGMw0-HsLcO35-r00wSOQxQz2ebxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران در اولین روز محرم مهمان حرم امام رضا(ع) شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/442590" target="_blank">📅 18:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd1093a5f.mp4?token=YALFLB3fzCrRJbeUdSecUHFeXdn56jTgXhW_Q7kK_pGHeiKd6Fxmn0yMWD1NA58aB53cm7QljHwJ2t71Sz4tlGqHhUO-fqZLOLbirbcbkqo3R4XYRsbqG7wwikXox7LmKtRmk8zGMTIGOsq5189pMixl5KyjBRfhdiro4-kKYI1kqJDwlwhXqelJtz0e_NTLx3VAd-d9f5-1KIQE3rnM5GJpkA8u48od_latBUe7DLx8JqNt61UJAleUgvQOMZgEohck37LH6wH9WbPyP63O51clsBblgwaWhj-zxoIPPaf-x52xdmhxKS-dpasg9B_3X-Rt9Z11QPS0oNpaeFPV6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd1093a5f.mp4?token=YALFLB3fzCrRJbeUdSecUHFeXdn56jTgXhW_Q7kK_pGHeiKd6Fxmn0yMWD1NA58aB53cm7QljHwJ2t71Sz4tlGqHhUO-fqZLOLbirbcbkqo3R4XYRsbqG7wwikXox7LmKtRmk8zGMTIGOsq5189pMixl5KyjBRfhdiro4-kKYI1kqJDwlwhXqelJtz0e_NTLx3VAd-d9f5-1KIQE3rnM5GJpkA8u48od_latBUe7DLx8JqNt61UJAleUgvQOMZgEohck37LH6wH9WbPyP63O51clsBblgwaWhj-zxoIPPaf-x52xdmhxKS-dpasg9B_3X-Rt9Z11QPS0oNpaeFPV6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ احساسی بازشدن پرچم سه رنگ ایران در کف لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/442589" target="_blank">📅 18:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شهردار بوشهر برکنار شد
🔹
اعضای شورای شهر بوشهر با رأی به استیضاح شهردار، به فعالیت حسین حیدری در شهرداری پایان دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/442588" target="_blank">📅 18:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2746eb9dc.mp4?token=ldRGKtZaGlHt-QBVSVzpnXYK-NuIKMXnFwZB-AXIo4B1cmJz_WfHL7d9FbUMsHbrTA54tMh3JYsN5vsOsC4pj6AZUcxvnSRzs-sVohYvTxirdH-d5293zMQ2RqQGleDqlnp8gs6fVBIyV5YmTF8SjNpnv8GM91lnldFdv9pNcD7YdrqDokMUOadFtDakUQL03JRQ7J-t6rkZqF2cHTWnxt5aTvDu_W6o5fGL85gw51aOgi6gmEMs8gOMExiWoSatboOmPalnaKxebhnA9xWFUPs1J9zgEF7N1bxI9ZsDZmlemnZmjkFYn7EWmHNFvwu0Q3q_s6JkMitFcSaqvT5ggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2746eb9dc.mp4?token=ldRGKtZaGlHt-QBVSVzpnXYK-NuIKMXnFwZB-AXIo4B1cmJz_WfHL7d9FbUMsHbrTA54tMh3JYsN5vsOsC4pj6AZUcxvnSRzs-sVohYvTxirdH-d5293zMQ2RqQGleDqlnp8gs6fVBIyV5YmTF8SjNpnv8GM91lnldFdv9pNcD7YdrqDokMUOadFtDakUQL03JRQ7J-t6rkZqF2cHTWnxt5aTvDu_W6o5fGL85gw51aOgi6gmEMs8gOMExiWoSatboOmPalnaKxebhnA9xWFUPs1J9zgEF7N1bxI9ZsDZmlemnZmjkFYn7EWmHNFvwu0Q3q_s6JkMitFcSaqvT5ggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از فروپاشی روایت تا تصویرسازی دروغین اینترنشنال
روایت‌سازی دروغین اینترنشنال برای سفیدشویی سلطنت‌طلبان، نقش بر آب شد و رسوایی‌شان را دوچندان کرد. این جریان فحاش، با همان رفتار زشت همیشگی، ثابت کرد که هیچ نسبتی با ایران و ایرانی ندارد.
@Fars_plus</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/442587" target="_blank">📅 17:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14addb21c3.mp4?token=Ib-xL_lCdjwxV5-IpHiKDLO5nN8UuHmtYJ667fyz6hCAxj-_S1-zAgu6m2WJ9ZdCXmS_xmerN_LLuKQSsclHkTQLaNFzv8ALJb86yHSBvD-A4dJy3gUuRFqWcZoDrMdcUY0c1c4BQdZhTtZTu_aWNsGi98mzV02EwUYpDxug5lVCwIyCFEWnntFxJwv3j2a-z9voX5umxSnm6uGYADsD2I4AIuAp_DmGWtjTQJe5NxyU68bX4tFOe4WZSPR_HnLOs5Y_omruT4HKy1sOJlS413_JFbYn5ZmAuIzcZIMvk_V_nHW87blFoP5CPZL8S18Lmw1zUW7ABM-ZxYmppBftyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14addb21c3.mp4?token=Ib-xL_lCdjwxV5-IpHiKDLO5nN8UuHmtYJ667fyz6hCAxj-_S1-zAgu6m2WJ9ZdCXmS_xmerN_LLuKQSsclHkTQLaNFzv8ALJb86yHSBvD-A4dJy3gUuRFqWcZoDrMdcUY0c1c4BQdZhTtZTu_aWNsGi98mzV02EwUYpDxug5lVCwIyCFEWnntFxJwv3j2a-z9voX5umxSnm6uGYADsD2I4AIuAp_DmGWtjTQJe5NxyU68bX4tFOe4WZSPR_HnLOs5Y_omruT4HKy1sOJlS413_JFbYn5ZmAuIzcZIMvk_V_nHW87blFoP5CPZL8S18Lmw1zUW7ABM-ZxYmppBftyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اسرائیل به جنوب لبنان
🔹
در جریان این حملهٔ صهیونیست‌ها، شهرک «میفدون» هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/442586" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d999b963b.mp4?token=rBGT4MlvoBEEasfZDEwpE8KannqgnDiIMh85BQudhudHGfAJPJj3vShxRqdehPqIbsK-bo493W-alquDMDUFKlBmu-Nsv0tOKN1tsKGzEfRjIH7hOhKtsFnAQc2gi4FCAWNoFnmmTBnmP2NrPCVTaqZrgNoJnSM0e09VvYHKJmqgs8p9JFzK5dBKK4NmL31vWVYvY_R4wwkd4PvqyOz-RUtMFdjOSHfJ-7WhBSz-DZiOl2mFN3eQNMRiJurJa01eg16l3JGyGb04-lxzwXIOj5ThcRoWUhSHibyQQYTWctIO1DqgjUxL_e63ZQyXBAJyShtQnjM7ZZxskBZ-3TmeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d999b963b.mp4?token=rBGT4MlvoBEEasfZDEwpE8KannqgnDiIMh85BQudhudHGfAJPJj3vShxRqdehPqIbsK-bo493W-alquDMDUFKlBmu-Nsv0tOKN1tsKGzEfRjIH7hOhKtsFnAQc2gi4FCAWNoFnmmTBnmP2NrPCVTaqZrgNoJnSM0e09VvYHKJmqgs8p9JFzK5dBKK4NmL31vWVYvY_R4wwkd4PvqyOz-RUtMFdjOSHfJ-7WhBSz-DZiOl2mFN3eQNMRiJurJa01eg16l3JGyGb04-lxzwXIOj5ThcRoWUhSHibyQQYTWctIO1DqgjUxL_e63ZQyXBAJyShtQnjM7ZZxskBZ-3TmeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معجزه‌ای که امام حسین(ع) برای طراح ضریح خود داشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/442585" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie-QjmmLe3dg4w07WlKclCHIfxEHWjpRT1jLbOaELuruJ1MwXv_ZAruBBDOrnedu6PpQt5BOi0vVJnQAaE1t2svpNM4XqPnGQJx_RVb2DQXMc-HaT-FBQdc1u6qBr7RtLfIWlai6iyJoPDL4jXGu1vzDNhfuBbgBcWB-c8y8vBW9y9MoRn4l6SjDEU53n-WPLuG5Fq6-Lat5xNTdXohQ7DhfHC1o1wz5kifPKRqA-G-drVyv9iJuDO5Csz0tj0lFSynJl3GaNfUziDiPmPvocEOIy8JQYseYr8SEZsNPJLMzxmcEfMnN4AfP6MOIJSpfk_4kITnxq-5Ygda6hh68jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست: پایان جنگ ایران، یک شکست بزرگ برای اسرائیل بود
🔹
اسرائیل به امید «نابودی ایران»، تجاوز دوباره علیه این کشور را کلید زد، اما اکنون حتی رسانه‌های غربی هم اذعان می‌کنند که این جنگ «ضربه‌ای» سنگین به اعتبار نخست‌وزیر اسرائیل بنیامین نتانیاهو وارد کرده است.
🔹
نشریه آمریکایی اکونومیست با اشاره به تفاهم بین واشنگتن و تهران تاکید کرده که بنیامین نتانیاهو همه سرمایه سیاسی خود را به کار بست تا رئیس‌جمهور آمریکا را به جنگ با ایران قانع کند و «حکومت حاکم بر ایران را سرنگون کند.» اما در نهایت به هیچ یک از اهداف اصلی خود در جنگ ایران دست پیدا نکرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/442584" target="_blank">📅 17:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bddd12045.mp4?token=mnj0hVf-Q86jt355aGBK_d0dJpb1v_fphUzpvLLscLG2gHuhRrF7oP70yiPn0ePjo0O7-YEkbRUnfaH3gL8mv24bH1gfuB5xWQSvpM_m1-UfXI8QINv6o7rOm4UAljC598E0lTBzb31M9fS_cgKGJKBcnciavZOeq2MWsArktMj8O8QJ2XOQ70Lq5wh1JUlbeh37UASD5CXYi156kiOyDNxwffhDv3EtEt02yf1G-T5RkynKuJ6oBqBzkucQDpv9vU4UOI_3KLK2kHou2LOO0JcOi_m6LdSmySDA1GFx5Taxg6jgXhMwMavyZvxZpjGa7s94w2tPevItyyEkZi6iHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bddd12045.mp4?token=mnj0hVf-Q86jt355aGBK_d0dJpb1v_fphUzpvLLscLG2gHuhRrF7oP70yiPn0ePjo0O7-YEkbRUnfaH3gL8mv24bH1gfuB5xWQSvpM_m1-UfXI8QINv6o7rOm4UAljC598E0lTBzb31M9fS_cgKGJKBcnciavZOeq2MWsArktMj8O8QJ2XOQ70Lq5wh1JUlbeh37UASD5CXYi156kiOyDNxwffhDv3EtEt02yf1G-T5RkynKuJ6oBqBzkucQDpv9vU4UOI_3KLK2kHou2LOO0JcOi_m6LdSmySDA1GFx5Taxg6jgXhMwMavyZvxZpjGa7s94w2tPevItyyEkZi6iHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرمزِ بسته؛ ۱۰۰ روزی که بازارهای جهانی را به زانو درآورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/442583" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtVaukPR05jkFy7e-jdwGa6fyLyfgGI2T8wXiYBqBSVq5Dq004X0fJ5gbjRmVpnzdSN8SWhPI7k3ieghyInLybCsCpl3tBoDYX0qbQ3Eee-uDvmw-wxJhWsiDhWw9rX5GQXKdutlJDxMZDEx8hw4rPimH7xZfYktlovDJx3SMgcGq1kTtHWTNxr2DDszPlYh7UG0RV6N8Gkd6e8JFVLFbQFoJSpH5ss_DgjwNKYC-l0Ite0PSd4DepLJV5nVtKlk9JEydJb4RjUnzKwvYWVvEjdHQyvueoJL3TLYGxBCCWiFhb8HJ5ccyjX4aFEEd-8K0l1DRAeqmeMGxxPR50GQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توافق با ایران را به کنگره خواهم فرستاد
🔹
نه‌تنها متن تفاهم را منتشر خواهم کرد، بلکه احتمالاً یک کنفرانس خبری خواهم داشت و آن را کلمه‌به‌کلمه خواهم خواند تا رسانه‌ها آن را به‌درستی پوشش بدهند. برای این که این توافق بسیار مهمی است.
🔹
تفاهمنامه درباره یک موضوع است، این که ایران هیچگاه سلاح هسته‌ای نخواهد داشت. باقی مسائل، رک بگویم، بی‌ربط است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/442582" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b257fc1a8.mp4?token=lMBN4LVKCTklrMXtSJOlUT1SsdF0NfrlMC3CJU2oxBHn2M1pI3nSHjK-QZUcrfdULdGxGhHlWe3yVQfML4ojJHVwF_gI_xlqQN9C2N9bG2mKxwM9SFA_4IfFNf4n9Xq2jKGTNK796JNpZ3q4i0gVWme170cucw5dOg-txafNWQMOduVEZyt-m6b0g2QypHV_v1UfdmXUh3J0dKp4GpYPi85Tsp45TX_nalM285xk5V4E48LYnWkY-YQIy1yp__Va1tQT8cht-sOue5cRaaozT1U8NjkqKQ8T-u5qBpdZCzd4BCIuRCRStgWxKj1kGCWQXGicH3gVdcIZwR_KioyWpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b257fc1a8.mp4?token=lMBN4LVKCTklrMXtSJOlUT1SsdF0NfrlMC3CJU2oxBHn2M1pI3nSHjK-QZUcrfdULdGxGhHlWe3yVQfML4ojJHVwF_gI_xlqQN9C2N9bG2mKxwM9SFA_4IfFNf4n9Xq2jKGTNK796JNpZ3q4i0gVWme170cucw5dOg-txafNWQMOduVEZyt-m6b0g2QypHV_v1UfdmXUh3J0dKp4GpYPi85Tsp45TX_nalM285xk5V4E48LYnWkY-YQIy1yp__Va1tQT8cht-sOue5cRaaozT1U8NjkqKQ8T-u5qBpdZCzd4BCIuRCRStgWxKj1kGCWQXGicH3gVdcIZwR_KioyWpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تونل‌های برفی در ارتفاعات اشنویه
🔹
با گذشت ۳ ماه از زمستان راهداران آذربایجان‌غربی همچنان مشغول برف‌روبی در ارتفاعات شهرستان اشنویه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/442581" target="_blank">📅 17:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE43w2o1F19YsT5sy4PBMVJyNI8GRE1m95400M7f2X-4bmDDyRWG6wK2YIyQJbw5vPZS1dFxLfPIY9BzKIz7wlRJeDVRo27ySA1uQELJrZFQjVO8iJdQDET9Gf_NfRZPjvAewa0QND6pmic8bIHHIl8HrwxbvuuTmFX6roSxlIltOcVTgFnM_I8zCJwTu7lGQrk2zhDutJZNDjKLgGGmQBp1pJCYeWIFp9A3COGlK0wRGoBsxyv4HVE1n7jmCcJe0A4zbjv1lWgnT8HU8c5XmAV1eSUgZPpzvos7RQcQVNJh6sr5gX8kc3I7uZG0iO63_Ad6idY1BOqGHwy_D6qyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: ایجاد منطقه آزاد در تهران به تسهیل ترخیص کالا کمک می‌کند
🔹
رئیس شورای شهر تهران در واکنش به مطرح شدن ایدهٔ ایجاد منطقهٔ آزاد در تهران گفت: چنین اقدامی می‌تواند در تسهیل ترخیص کالا مؤثر باشد. برای نمونه، در صورت ایجاد این منطقه اتوبوس‌هایی که در گمرک…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442580" target="_blank">📅 17:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c4fe8180.mp4?token=dtZeSTJO-UbingZUpby1JUBT0N64w7JQ21wdrqdUeE4gdrEL8PfQD8Xtppt0jRTfFqJG5FFGQcKVlYnHYA7O7riG1juytDnGltQkxuCGC8-M0aOmCIkD1Yp7eOePYrUUsPD4swYiylgemmP1cYB3MNcZFg-_27aiAjMLMoJuHCqHuGhfOhOFigRWn_CjccrYWSGaPLPs_VUBmT6D1MgMK4Xdls8RGbN8u7r8cDxeSRmn_WCFsKY9V6_agCdDy_OhBTVMM3CDjPrJXpCBhu4dX4pzXsAhCQlIhnZ14n_UVjJ0JZ_uZ9lZ-aZ75lImypXmTUqz9EsjAuMsDu3tyWBXBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c4fe8180.mp4?token=dtZeSTJO-UbingZUpby1JUBT0N64w7JQ21wdrqdUeE4gdrEL8PfQD8Xtppt0jRTfFqJG5FFGQcKVlYnHYA7O7riG1juytDnGltQkxuCGC8-M0aOmCIkD1Yp7eOePYrUUsPD4swYiylgemmP1cYB3MNcZFg-_27aiAjMLMoJuHCqHuGhfOhOFigRWn_CjccrYWSGaPLPs_VUBmT6D1MgMK4Xdls8RGbN8u7r8cDxeSRmn_WCFsKY9V6_agCdDy_OhBTVMM3CDjPrJXpCBhu4dX4pzXsAhCQlIhnZ14n_UVjJ0JZ_uZ9lZ-aZ75lImypXmTUqz9EsjAuMsDu3tyWBXBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی محمود کریمی برای فرماندهان شهید و ماکان نصیری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/442578" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67a9666a7.mp4?token=rkfjuTHtdo2tOUoemz_WyS7U5tVkMXJypfHXe3EDhM7aFN3T26wGR14qLP1Cu-ersY_ZNVTxF0T48lSxJhQBdHKO5yfx3k_OxXF7fW_cJTUiL_a8xJ4MrR9Cf7AKQPeBKqnBiLujKylxrbi8U9hd_7eF0XbJ_5x6ZtcjHsPjjeBXu2Dmys1gWwOitr6F3EAPd8Lr4gzYTffDt9ChMU1CIe6ZcFMEjtBQ_uuv9kCEgkNXo7lsbrZRDgdqdAFUWPLpcrp8B2plsKd1tkjO2jFz4S6TlFPixUGBy9TK5TI27HNRqY4z5EWg-ESFaZiuLmSPUAHvi3y2Fd65YKf5LfPetA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67a9666a7.mp4?token=rkfjuTHtdo2tOUoemz_WyS7U5tVkMXJypfHXe3EDhM7aFN3T26wGR14qLP1Cu-ersY_ZNVTxF0T48lSxJhQBdHKO5yfx3k_OxXF7fW_cJTUiL_a8xJ4MrR9Cf7AKQPeBKqnBiLujKylxrbi8U9hd_7eF0XbJ_5x6ZtcjHsPjjeBXu2Dmys1gWwOitr6F3EAPd8Lr4gzYTffDt9ChMU1CIe6ZcFMEjtBQ_uuv9kCEgkNXo7lsbrZRDgdqdAFUWPLpcrp8B2plsKd1tkjO2jFz4S6TlFPixUGBy9TK5TI27HNRqY4z5EWg-ESFaZiuLmSPUAHvi3y2Fd65YKf5LfPetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌ای از ۴ دفاع پیاپی ملی‌پوشان والیبال مقابل بلژیک
🔹
با وجود ضعف‌های زیادی که تیم ملی والیبال در هفتهٔ اول لیگ ملت‌ها داشت، اما ملی‌پوشان ایران مقابل بلژیک در صحنه‌ای دفاع جانانه‌ای را به‌نمایش گذاشتند و نشان دادند می‌توانند با تمرکز بالا، نقطه ضعف را به قوت تبدیل کنند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/442577" target="_blank">📅 16:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
شیخ نعیم قاسم: از طرف حزب‌الله و مقاومت اسلامی، و به نمایندگی از مردم وفادار لبنان که مشتاق ابلاغ مراتب قدردانی خود به شما هستند، و همچنین ازطرف شهدا، در رأس آن‌ها سید شهیدان امت، سید حسن نصرالله و جانبازان و آزادگان، از شما در مقام ارشدِ مذاکره‌کنندگان…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442575" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما همیشه گفته‌ایم که ایران به حزب‌الله و مقاومت و مردم لبنان همه‌چیز داده و چیزی از آنها نگرفته است
🔹
ایران به ما امکانات، قدرت برای آزادسازی سرزمین‌مان، برای التیام زخم‌های جامعه‌مان و کمک به آن داده است و اکنون ایران خون می‌دهد، با حمله…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442574" target="_blank">📅 16:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
نامهٔ شیخ نعیم قاسم به قالیباف: کلمات از بیان سپاس عمیق ما نسبت به مواضع قوی و حمایتگرانه از لبنان و مقاومت و الزام رژیم اسرائیل به توقف عملیات نظامی در تمام جبهه‌ها از جمله لبنان به‌عنوان بند اول و اساس توافق بین ایران و آمریکا ناتوان است.
🔹
شما تنها و…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/442573" target="_blank">📅 16:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
نامهٔ شیخ نعیم قاسم به قالیباف: کلمات از بیان سپاس عمیق ما نسبت به مواضع قوی و حمایتگرانه از لبنان و مقاومت و الزام رژیم اسرائیل به توقف عملیات نظامی در تمام جبهه‌ها از جمله لبنان به‌عنوان بند اول و اساس توافق بین ایران و آمریکا ناتوان است.
🔹
شما تنها و مؤثرترین شعله امید را در بازداشتن تجاوز اسرائیلی-آمریکایی از لبنان به حقیقتی تبدیل کردید که به جهان ثابت کرد ایران حامی حق، مقاومت و مستضعفان است، و اگر دیگران راه آن را دنبال می‌کردند، آمریکا و اسرائیل این‌گونه گستاخ نمی‌شدند و اشغال صهیونیستی بر زمین فلسطین و قدس باقی نمی‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/442572" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0426334c5.mp4?token=lvd68_MC6ISsMXBo-q4-h3GGVR9z5tXGQhr0OTq0EJxpr2KWvdALgkQo-iA4MKrTa5kAMQ0mn4z3IBaRae3wQNAxtB30-M1KfbEuoCkmpwwp9hC4W3BToGz-p8lkBRLnm3EytGFAAxcbwGbzARGe3aUjq9mnyoV6GZXx2hF_pRreHczv8Z81if1ddrL7iqHNfH7SJjPSN2lrncAGHqoEUcqZvTW9fkc2PP7z5TUeopgaA5K-QkMnhydEtHaADYI5fjldDpwZax_0H-m1Nb0079XtkNBA99U8M-Oah5Mu2BT-GFdh0CQVTaFRKiJm0yJGPpjg9eqZhZcEh9J8ztVdPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0426334c5.mp4?token=lvd68_MC6ISsMXBo-q4-h3GGVR9z5tXGQhr0OTq0EJxpr2KWvdALgkQo-iA4MKrTa5kAMQ0mn4z3IBaRae3wQNAxtB30-M1KfbEuoCkmpwwp9hC4W3BToGz-p8lkBRLnm3EytGFAAxcbwGbzARGe3aUjq9mnyoV6GZXx2hF_pRreHczv8Z81if1ddrL7iqHNfH7SJjPSN2lrncAGHqoEUcqZvTW9fkc2PP7z5TUeopgaA5K-QkMnhydEtHaADYI5fjldDpwZax_0H-m1Nb0079XtkNBA99U8M-Oah5Mu2BT-GFdh0CQVTaFRKiJm0yJGPpjg9eqZhZcEh9J8ztVdPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطعۀ دوم آزادراه شهید شوشتری بدون قطع درخت ساخته می‌شود
🔹
رئیس شورای شهر تهران: قطعۀ دوم آزادراه شهید شوشتری طی ۳ تا ۴ سال ساخته می‌شود. بخشی از پروژه به‌صورت تونل زیر جنگل و کوه اجرا می‌شود و به جنگل آسیبی نخواهد رسید.
🔹
یک کارشناس شهری هم دراین‌باره گفت:…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/442571" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610aa9973e.mp4?token=Sk6kzK8iMQinL6t0Aonn36SQ4YFmgYBRhsB5egIkXqUrmTbKPn-1ngd6Whmvo9bbTnCtz6xscrW1JdKLX0MqYZeqo0ulgssbQWeVOUINykeLWVEZjDZvWCEubbAYXTEtImadHE5hnE6HGvG3_2AGwdASolGdfwV5EiLLCZatbM4ECa2FuPTqBooZwSOM9hCRfpJsiJROqenFO-iIZVyASf46P9EGs24ToM0sCAgXrXItwlqqo48ct_pCDHSE31ANK2lH1mA2zwJkqbSZbWxBc-fccqOGSA2evAuU7lhLO2A86sA_zzxYgFDJjTFI__QTk-D5zN_6UD32B3wM59RcSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610aa9973e.mp4?token=Sk6kzK8iMQinL6t0Aonn36SQ4YFmgYBRhsB5egIkXqUrmTbKPn-1ngd6Whmvo9bbTnCtz6xscrW1JdKLX0MqYZeqo0ulgssbQWeVOUINykeLWVEZjDZvWCEubbAYXTEtImadHE5hnE6HGvG3_2AGwdASolGdfwV5EiLLCZatbM4ECa2FuPTqBooZwSOM9hCRfpJsiJROqenFO-iIZVyASf46P9EGs24ToM0sCAgXrXItwlqqo48ct_pCDHSE31ANK2lH1mA2zwJkqbSZbWxBc-fccqOGSA2evAuU7lhLO2A86sA_zzxYgFDJjTFI__QTk-D5zN_6UD32B3wM59RcSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات جدید از ثبت معاملات ملکی در سامانۀ کاتب
🔹
سازمان ثبت اسناد و املاک کشور: مالکان املاکی که دارای سند مالکیت حدنگار سبزرنگ هستند، می‌توانند به‌صورت خودکاربری یا از طریق مشاوران املاک، نسبت به ثبت معاملۀ خود در سامانۀ کاتب اقدام کنند.
🔹
این قراردادها دارای…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/442570" target="_blank">📅 16:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9767cf1552.mp4?token=kEbrHY0-P7F8M088dSuFJd4wh6KVzOsMbbTVj01-VyqmfIjYugd-wr2iSBuIFmT_dCpn0ghHO0UL_BGjXE3WgeK2tbj9mukkW-HMmmE4rD9E_R-8f3OydOGbdkOtJyQh911QJ9G0TdA2C3mSVDF4z1NKZBHiSkZRGJSN6SWWeaEOpKl7xKZtRGTe5oMklIrMjb3pY8r457DuLc4G9HMZCttZ7l36J6VI8sHQWHqgAMEDh7OW6bu3iTSzIsk6i4IzYYagyFaJFf3dgtZfnW7EZa2OetJyACWEE-qMWep9Or8IlgKQOgmnTEjBZp-dopMeP5TtQLfcrTjJ6FvjxqiQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9767cf1552.mp4?token=kEbrHY0-P7F8M088dSuFJd4wh6KVzOsMbbTVj01-VyqmfIjYugd-wr2iSBuIFmT_dCpn0ghHO0UL_BGjXE3WgeK2tbj9mukkW-HMmmE4rD9E_R-8f3OydOGbdkOtJyQh911QJ9G0TdA2C3mSVDF4z1NKZBHiSkZRGJSN6SWWeaEOpKl7xKZtRGTe5oMklIrMjb3pY8r457DuLc4G9HMZCttZ7l36J6VI8sHQWHqgAMEDh7OW6bu3iTSzIsk6i4IzYYagyFaJFf3dgtZfnW7EZa2OetJyACWEE-qMWep9Or8IlgKQOgmnTEjBZp-dopMeP5TtQLfcrTjJ6FvjxqiQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شهید لاریجانی در منزل شهید محمود باقری، فرمانده مقتدر موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/442569" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-KoUGN-bc3JsVmkDCIm3apR7xa-pYhn37KzVIQmICx1xo8Qjb7Z_vB8zdBN0qWTcQiEjloRbt1J0dc2eXSABMMjBdd3q8BauszBmsKJJBnrTY8GEr3SFaFUcEnM17k8GV8cqPXUhpZzYTqMgxWhKeg7b7_tE4herNwmmML7za9LUtozZ-7mJ1V2zU0C1H_3NpWSORXNTG5WmlM5gdgyhG8bDUyw8mEejmZWGxEBJ_OYeQhnh7C8GSVqyMUk_fi6avVC9tnKCqv8X_kJAgzhBVgnjCLQaRgv53VreW680MWLITO0Yh07hu_e0lnOgarG9cTtZ3PhnqLuF2vLg3woMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd87c0908.mp4?token=unM8t6-VhCrg9-CLjDivZX1LUkUja5SYht3P2915KC-41lmrx6wNR-UhxWFG1If2yvWyBMYZ1nBackr8TDSxJMp-81P4zEBL3NHgyd1LjE7vRULno-OmjZW8ygT2SDJYy8etMNRMOTkQlh6F7cretj7T8K-KfY0rb2ZWA3t8rtYCkRF8CvlRntxTdgdXYBSquTQRsPkMGgNqxs7RDjlS1op68LSMOcjdkpj_oyOtko9kUDvQDdqlVsISHmyUKMdSHO7bIDm7Ob_w380_9itIvvR9qF5gb7fAKkfLULBgSWQil3-wkeCxzAcbiYTwcSjAh3mLAKa8J1OFpmPWdF9pcpDRa8aDDXbbovd0N4YHwRj_UqTITiHS1mCl_h2T-iGXlGsPxrWs1sg3mVZ9tgfg5ZYSrdCkRBH8YeTOwmgrzo0tMzlkheCil0rIhyQJqYs7SMQtirNQSvV-0iinn1KeCcZU6twNixPxMK4WKVVc9vLHFhsfQfx8RkzpL36F0AkNZsbQty0X3odU1xb3UsHp4fviTjXpzklSjgqFuQWHBE-Vgzpxoqd-O8svWopQOiOshEMzOu8OY15Q4946WopMWQIn7KaasBjGZy1WSrFNzD_Sansj1Kfcv1CsIGz3JXPJrLC_zEozDfXvpq7J6w7THA-F00aqMth30lSr0zizmaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd87c0908.mp4?token=unM8t6-VhCrg9-CLjDivZX1LUkUja5SYht3P2915KC-41lmrx6wNR-UhxWFG1If2yvWyBMYZ1nBackr8TDSxJMp-81P4zEBL3NHgyd1LjE7vRULno-OmjZW8ygT2SDJYy8etMNRMOTkQlh6F7cretj7T8K-KfY0rb2ZWA3t8rtYCkRF8CvlRntxTdgdXYBSquTQRsPkMGgNqxs7RDjlS1op68LSMOcjdkpj_oyOtko9kUDvQDdqlVsISHmyUKMdSHO7bIDm7Ob_w380_9itIvvR9qF5gb7fAKkfLULBgSWQil3-wkeCxzAcbiYTwcSjAh3mLAKa8J1OFpmPWdF9pcpDRa8aDDXbbovd0N4YHwRj_UqTITiHS1mCl_h2T-iGXlGsPxrWs1sg3mVZ9tgfg5ZYSrdCkRBH8YeTOwmgrzo0tMzlkheCil0rIhyQJqYs7SMQtirNQSvV-0iinn1KeCcZU6twNixPxMK4WKVVc9vLHFhsfQfx8RkzpL36F0AkNZsbQty0X3odU1xb3UsHp4fviTjXpzklSjgqFuQWHBE-Vgzpxoqd-O8svWopQOiOshEMzOu8OY15Q4946WopMWQIn7KaasBjGZy1WSrFNzD_Sansj1Kfcv1CsIGz3JXPJrLC_zEozDfXvpq7J6w7THA-F00aqMth30lSr0zizmaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442567" target="_blank">📅 15:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjKataFc-1PwceMDnQS6qB4bQMNV4Twy7fUv0dcaIkVhQoZrY5qFlPyglOboLhBAXXZEQbZLsesNCri04QAhTr1G7ssPMDQ0YUXuUqcLyuR0aa8NAgzxnX2EhuGzRHzjXkKKalQOXL08NUerWaqnG8EPf8WwJ-X4Pya9K1c8hkIx86eNwHhM2HPbUwZJuni2cNVv_va3RRQ63s0Hv913HfHQpd4G312O6YxzGeOucd1tjjLw8oGVCeqfBL16iXgZrZjtHB1yILS3EmtDTCXV1W8OQQuGIgiTJ-IY0LRmKvPOYwnCJWby2N8xSsBgYPMazjS7j2kfoAU0KmvZ6LCfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال وقوع سیلاب‌ در ۸ استان کشور
🔹
سازمان مدیریت بحران کشور: از امروز به‌دلیل فعالیت سامانهٔ بارشی شدید، احتمال وقوع سیلاب ناگهانی، طغیان رودخانه‌ها، آب‌گرفتگی و رعدوبرق در استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، خراسان‌رضوی، اردبیل، گیلان، مازندران، خراسان‌شمالی و گلستان وجود دارد.
🔹
همچنین در مناطق جنوبی کشور، به‌ویژه سواحل هرمزگان و بوشهر، خلیج فارس و تنگهٔ هرمز، وزش باد شدید و تلاطم دریا تا ظهر فردا پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/442566" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR4ZrygWsHcTCrG9IlJx5_Qm-W7w3TWfy06CokkkvOWYGgN1S16Jx_h6upp2TCaKU6RywrnIM6FeqPScKCiG8drB6om6gQCyar3WnCJfGkifv7arLt0dT3Fr-jojjqG9rjg8wFQf5xjRRh-U-I1vZN_Q9OKLqr8BaGJ0jy5DPNOw-rCS8RhVklKGu3lweiQJj6BdyYa9XN9uc8c9FBaPlh-Vi7k1a1USCIyWiVVuuOHBFgOeGXAF3Toyiq55In5dI_YqJNxvMIxvC58Cf5d7OqFpk52U-Ig5t09AmL_feF4mSJgtKMHWu2RYzSJXB-60HGeOoyQxG7ayohhI0k5frQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزش باد شدید در تهران ادامه دارد
🔹
براساس داده‌های هواشناسی تهران، در ۵ روز آینده آسمان پایتخت صاف تا کمی ابری در بعضی ساعت‌ها همراه با افزایش ابر و افزایش وزش باد پیش‌بینی می‌شود.
🔹
همچنین از امروز تا پنجشنبه در دامنه‌ها و ارتفاعات در ساعات بعدازظهر رشد ابر گاهی بارش پراکنده با احتمال رگبار و رعدوبرق مورد انتظار است.
عکس: حمید عابدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442565" target="_blank">📅 15:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSnCKaeW2TqM_1lCsfaJrFAtLZUFM2J-0x6EzqHYFQWsryIeqK62_N1bOUUUjm9XNHS5QS5E9etEgerSePuMN-nFw7linf2su2oj-OlnTpk3A4-9SYDIUZNaDHZXSmd3SqgyY0nb7m_4fBqplsjw5MIkgUyKCwWc8ZVyOPO9HDidS8H-mDkbIbLnxwQLpb20Uhp5OMMovybyTN4c3XbgIY0vqaFe5B3xtTFlt0CJvhMWujYIaInloVkhpII_3u14pQ3UqSmRBL5cFZUBh5pOGcgpzdipSscoBLtCUT1ph1HgiVBw_VZSUajwgcNtdUcpP4fW-W3R0fWvvpwKosaq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران در رتبۀ چهارم
🏟
پرتماشاگرترین بازی‌های جام جهانی تا اینجا
@Sportfars</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/442564" target="_blank">📅 15:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
یادش بخیر آن رهبر جاویدان در بزم ماتم
🔹
مداحی محمود کریمی در شب اول محرم به یاد رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/442563" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM7r1Z5Zp5VCODbGPZXcehGVK-6OVx9Wn-CKH4u1i8m4EL0Ds5sdM2y12yygaGs5jeI8t3rVTgrdQhseLEMb8IUpE4ustSaQNRoM7SaJ04m8siTuX1T4a0Yg9VM-K6R8zCB59zuzZPF_LYQ_tDVt3W9-LpRgWvSiW39PAKRFZEfIFwBcXrVKVhI3HG3GJyh_ZQ60AZ2VOsm1xCl3KxQZKsS31Gf73roiU4C_Ue_ksWQL6O9dokojI8lkoXuvQEIbQH-GjDsPl02biXnbIKuBdc7KjiiIqn2GjCs3QmH3z-6Aba8s6L0jIAOTyG1A8KwxTEtBVPZGaKI_4UUdlCMXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سرباز طبیعت به‌جای ۱۲ نیرو کار می‌کند
🔹
فرماندهٔ یگان حفاظت محیط زیست: یگان حفاظت محیط زیست به حدود ۷ هزار محیط‌بان نیاز دارد، اما در حال حاضر کمتر از ۶۰ درصد این ظرفیت تأمین شده است.
🔹
بیش از ۲۰ میلیون هکتار مناطق تحت حفاظت در کشور داریم و بر اساس استاندارد جهانی، برای هر هزار هکتار باید یک محیط‌بان حضور داشته باشد اما اکنون برای هر ۱۲ هزار هکتار یک محیط‌بان داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/442562" target="_blank">📅 14:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14d10416a.mp4?token=AmSiNNB8jmc8HDNJM-HdLuKie_bErLWcQ9P3M0FBHltPaoiJnUyEzYtiPCwOuQDteDZTvOb94M2QvlVMSwyLMJO-Frqp7S6_w9NTL-X3A7PRsySjxY1vtzzK2YncK7oNANQ50dGbXAm2dZ6hcFGiwSMvLD-el7egOt0Ca4fblSvkRnCC0wj9JbKTuBKQmlWVtejaaNZTxRkAk3Z-HoUaZHbzgI5OgXwgoozD9zSjR795pCqtYknPWs32H1oNAeGi5FlEQx59KJv7_axXEsz4qB2IgKwZhr5s9CYIRKD4Gz7V7jzhA3ruFWa-zJ5g85Bx12Earqjn-TOquTPsU2tPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14d10416a.mp4?token=AmSiNNB8jmc8HDNJM-HdLuKie_bErLWcQ9P3M0FBHltPaoiJnUyEzYtiPCwOuQDteDZTvOb94M2QvlVMSwyLMJO-Frqp7S6_w9NTL-X3A7PRsySjxY1vtzzK2YncK7oNANQ50dGbXAm2dZ6hcFGiwSMvLD-el7egOt0Ca4fblSvkRnCC0wj9JbKTuBKQmlWVtejaaNZTxRkAk3Z-HoUaZHbzgI5OgXwgoozD9zSjR795pCqtYknPWs32H1oNAeGi5FlEQx59KJv7_axXEsz4qB2IgKwZhr5s9CYIRKD4Gz7V7jzhA3ruFWa-zJ5g85Bx12Earqjn-TOquTPsU2tPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان محاصرۀ دریایی آمریکا، با عبور کشتی‌های ایرانی
🔹
دقایقی پیش چند کشتی ایرانی نسبت به تردد بدون مشکل از خط محاصره اقدام کردند.
🔹
طبق اطلاعات ناوبری کشتی، یک نفتکش ایرانی VLCC از آب‌های آزاد به‌سمت بنادر ایران در حرکت است و از منطقۀ محاصره گذشته، همچنین…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/442561" target="_blank">📅 14:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39152c14ac.mp4?token=idZGmkFDytUOFvLRkh8_9IEAGOipAGovreR2SLq_2gNzZgwlNQ4H31sIt1LM_CZh9Mw5l6mU0ZO58nTkw7iZBKi3qwfMrm7fBg2ylG5jhvI66FT5a5SYE87UzdrOo61A53S9AosydfzU3Gf-cwdWv1woZS1qMSw_xrOhdRg77s4u0PQDqzJ-UONqWaWD-vgxNmll1wtEjtAGaDKtu9hnfGCTiWU3eyJ3BXEUCg-On055BDqUYgoGryj95yDW0qhhFpNNI_UkZ7lg4jHYd9CIa4BwJ1t18SfNegxqEsd7L0LjU7JK-Vi28jGWNA03yAnAtGrib244qsIDnDGOj4AjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39152c14ac.mp4?token=idZGmkFDytUOFvLRkh8_9IEAGOipAGovreR2SLq_2gNzZgwlNQ4H31sIt1LM_CZh9Mw5l6mU0ZO58nTkw7iZBKi3qwfMrm7fBg2ylG5jhvI66FT5a5SYE87UzdrOo61A53S9AosydfzU3Gf-cwdWv1woZS1qMSw_xrOhdRg77s4u0PQDqzJ-UONqWaWD-vgxNmll1wtEjtAGaDKtu9hnfGCTiWU3eyJ3BXEUCg-On055BDqUYgoGryj95yDW0qhhFpNNI_UkZ7lg4jHYd9CIa4BwJ1t18SfNegxqEsd7L0LjU7JK-Vi28jGWNA03yAnAtGrib244qsIDnDGOj4AjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اژه‌ای: ما برای گرفتن حق‌مان مذاکره می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/442560" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HETSNvde76GD0iE0GufyPIezTogA2_Fvw1wIEYvjN7jRuF4QsSHFZ6gJWS4mIU0YzfqAZCm6kVCtbPGohln-pdw_-V5IWLM6KJBJx9uoi4XZEbqUBmKQ3IeqvkPuE2Cbnp6wjGeX5gMinqW-KkJh5fmhYvcUW1uQK7NOPXKpj0tOrgq-0AKMm7ls_ndcWtRaGNm_P72JAjKaK1T3NGXSlLJxCsCucNsgTyIW54xuD1qvVi9i5g_FK6dLPZ4korKkdwO7KrVNUcWRuiucFn-BRKPZd54Qu0DKxaR0ULzYR3T44qvRjITf1-8EcL08mDL-0lPRFzjaaQJL9IZ9yvxZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhHPKW46XhwSfxPzpULV-vLk_80c8crMMSdu3RQoN4cjsErTA5maXDakgLGIubqcgHznXuORmeVEewH7dG9skFhavJmN69-bkEbn2AnV6keKB-rqpVregLlUUzVCK_6UJGz_cp0ZW7eZEJf2rUZU_zBxx81ffqEAA5DnHsaCNDAbs2_yZisYRiR2IFmdPaGeYhRpJnSVXGg417z3yzZ_pNB2SA8VrxDIVimbHupzGztrWqDUPe-LrITVAesFJckZQWjMyz2ny9xlD9MGXK2NI5WKVKv2taGQloZN-Wg18rAHgKagrrLEoKWD5jXtJgnpBcZh1PGemWuoK-1Be8sKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفنگ محبی مجوز دارد
🔹
شادی گل محمد محبی در بازی با نیوزیلند باعث شده تا رسانه‌های ضدانقلاب و برخی از کاربران ایکس با حاشیه‌سازی این شادی گل را خشونت‌آمیز تعبیر کنند و موضوع محرومیت این ستاره تیم ملی ایران پیش بکشند.
🔹
نکته جالب این بود که محبی به چندین شکل شادی گل کرد و تنها در بخش کوچکی به شکل شلیک تفنگ آن هم به صورت ضمنی شادی کرد.
🔹
اما با نگاه به شادی گل‌های ستاره‌های بزرگ دنیای فوتبال این نوع شادی در مستطیل سبز عادی بوده چون بهترین فوتبالیست‌های جهان به این شکل شادی کردند و محرومیتی برایشان درنظر گرفته نشده است.
🔗
شادی گل‌های مشابه بازیکنان بزرگ را در
فارس
ببینید
@Sportfars</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/442558" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b69d86769.mp4?token=HjjxZC6a6BhJOX7XCVzB4gUG0FEuI4wGCzuRnf1SvCbgByr71bgoK2pztTNlSvVpnLBwQWKR_Pp0-kZ7ti--dcsojeZSRWdrGLy0deSh_sIElj0RC5hjxO-pV7-UBxp3aVuIZfB3mTqwL11wDLggRA04of6UpvSnZLEE0uMTXx8SstOFBuCxo2dDcGqFQilDeoyq7cP8iDQ9_gxMcIq6IxvrLmESqAyWrfGoSG3JgLSSTJ7sjAYs3I_Y9pgSrN5lFbKJJ1YwHT5EAUsMH3gsZhQi5UiXnGbMZxJ78ng1h3xGj8klTM6hgKxieHq3o4IYCE4EIaV4odzA8xlQTnrT3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b69d86769.mp4?token=HjjxZC6a6BhJOX7XCVzB4gUG0FEuI4wGCzuRnf1SvCbgByr71bgoK2pztTNlSvVpnLBwQWKR_Pp0-kZ7ti--dcsojeZSRWdrGLy0deSh_sIElj0RC5hjxO-pV7-UBxp3aVuIZfB3mTqwL11wDLggRA04of6UpvSnZLEE0uMTXx8SstOFBuCxo2dDcGqFQilDeoyq7cP8iDQ9_gxMcIq6IxvrLmESqAyWrfGoSG3JgLSSTJ7sjAYs3I_Y9pgSrN5lFbKJJ1YwHT5EAUsMH3gsZhQi5UiXnGbMZxJ78ng1h3xGj8klTM6hgKxieHq3o4IYCE4EIaV4odzA8xlQTnrT3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مقابل بدعهدی دشمن می‌ایستیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/442557" target="_blank">📅 14:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYQwSL2CrZDFEJpFSZNhztjQBa-9GysOxp7Vl79Un1BvFNZcGNxYf6ZhgqcFcMGaXsptJUN3MoE_ugd9OpFjsWYVw5qdNWpCVhr0yXPonABU3S3AF3xlNIffBPbqiUZmQhZy2u-a9IwwNmpD7NPXJ68sJhlGmkJBxkKt6nX_pKH7GJ1ukD1HNfPHBsGgua_9EI_R0CsZpKGgLo2J5WsXKzv2v-Opd4dCAHISeMIH347aF0euHF1nt3gYbxqHGYg_Jy3KMYp-msEddgQ1Z-6mdnbu--H3tIu2FkBfEJ33gXiHY9XWZHHmrhVWguMGHJx_nBx99tKeSZ1FWBI0T83oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: جمعه پس‌از امضای تفاهم، مذاکرات آغاز خواهد شد
🔹
در مرحلهٔ اول مذاکرات دربارهٔ خاتمهٔ جنگ، محاصرهٔ دریایی، تنگهٔ هرمز و آزادسازی وجوه مسدودشدهٔ ایران تفاهم شد و در توافق نهایی دربارهٔ موضوع هسته‌ای و لغو تحریم‌ها تصمیم‌گیری خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/442556" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7cce6c6e.mp4?token=Z10wGLrxp13LyOfF2I5CPbNu5s3Be4w0RWpomuvanaYEPgp8EVaawcA8UVwU5wtDbVtKZ8-nxp9Ugx3-4hmKbYeTT8J0qVMmtibeokyqi7cSWdU_1XGCEdU8gfNbN8O3hrvVv7AQ7qV1QPqK9MvYg7tOqB39xsfrtDlirw1Ww9uGgkWB72N_zV9Qwv_EkHGKiUPgG92_IEY87liMAnurJs82PdotyYnnMsnNZW2J6CCetuIJU6nWmfY447T3p74G0OOpPdB_qAi5i-boj_k2FXYpHU3D_Uj1xFsPQ2V6mGaQP5k-9mOjjOUo0pKX9RKBKgdy8HJJXpUsB5rzJ9Wezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7cce6c6e.mp4?token=Z10wGLrxp13LyOfF2I5CPbNu5s3Be4w0RWpomuvanaYEPgp8EVaawcA8UVwU5wtDbVtKZ8-nxp9Ugx3-4hmKbYeTT8J0qVMmtibeokyqi7cSWdU_1XGCEdU8gfNbN8O3hrvVv7AQ7qV1QPqK9MvYg7tOqB39xsfrtDlirw1Ww9uGgkWB72N_zV9Qwv_EkHGKiUPgG92_IEY87liMAnurJs82PdotyYnnMsnNZW2J6CCetuIJU6nWmfY447T3p74G0OOpPdB_qAi5i-boj_k2FXYpHU3D_Uj1xFsPQ2V6mGaQP5k-9mOjjOUo0pKX9RKBKgdy8HJJXpUsB5rzJ9Wezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر من نبودم الان اصلاً اسرائیل وجود نداشت
🔹
الان اسرائیل ۱۰۰ درصد از روی زمین محو شده بود و هر آدم باهوشی در اسرائیل این را خوب می‌داند. @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/442555" target="_blank">📅 14:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9149ef45.mp4?token=DunOnneTphUS5UoA7Id5_U3iozxkfzbDJ-ZC-RQx0XRpBYi0tb-qyGEm_jgmUHWadLQ3cY3pMEcbyRorSzPO9GI4j2nuhu0A4UQxXMbV8iw9Ni5rCAc_xRPijyrzGYfAiyiea1bqxHtbmvsXuM7dV5NKg4mX89iNDR5Zw_1c65BEIzhPFsiKNQ6i0wCalDRjuzmri9rUigsCZ2rfEDkyr1OOZj0MiEoeRT--IpFzgjtfMuVqgBl1REv0Tw4ooBbz7ssT4WGg_HjG8U7yJ_71R-IYmJhHSIBFA2mLG5_51PhGq-ST2DHSbZAOqhc_X3dTx1WF4S3_2Ce6OiVdF_m7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9149ef45.mp4?token=DunOnneTphUS5UoA7Id5_U3iozxkfzbDJ-ZC-RQx0XRpBYi0tb-qyGEm_jgmUHWadLQ3cY3pMEcbyRorSzPO9GI4j2nuhu0A4UQxXMbV8iw9Ni5rCAc_xRPijyrzGYfAiyiea1bqxHtbmvsXuM7dV5NKg4mX89iNDR5Zw_1c65BEIzhPFsiKNQ6i0wCalDRjuzmri9rUigsCZ2rfEDkyr1OOZj0MiEoeRT--IpFzgjtfMuVqgBl1REv0Tw4ooBbz7ssT4WGg_HjG8U7yJ_71R-IYmJhHSIBFA2mLG5_51PhGq-ST2DHSbZAOqhc_X3dTx1WF4S3_2Ce6OiVdF_m7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مقابل بدعهدی دشمن می‌ایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/442554" target="_blank">📅 14:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6800f9e7b.mp4?token=CltjZ5dlB8-CSl1QJ9iZFvGoWtPn6tQkvIqjWYilKNS5tqkIZjlrXwOJM-8yKtvUxpng6Ql3i_t-vX60YwKFpP-isWmGsU1Z7iSN8EDJKQA9dEZ4e5FT1yimMxCH084daS2rqSqyJ7eFVQwUvSU0RdVxPrEf4oYTIa78Swxw6giwIwizTG5PcI40W2ybixFOCLC9opDWljM1oqUCtrKFkk0_PBoeDvV6CEQaryfRqBVAY9SMs1J-d03Bi7aR1RfCFtpqXTeN8mBu5hsk3U-w4BNEfEAZVv9-YRDwSgHHSX-dC1YHG1clRXAJaqpwkoP3o-Cjgt7xBUJflc9f0vTjXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6800f9e7b.mp4?token=CltjZ5dlB8-CSl1QJ9iZFvGoWtPn6tQkvIqjWYilKNS5tqkIZjlrXwOJM-8yKtvUxpng6Ql3i_t-vX60YwKFpP-isWmGsU1Z7iSN8EDJKQA9dEZ4e5FT1yimMxCH084daS2rqSqyJ7eFVQwUvSU0RdVxPrEf4oYTIa78Swxw6giwIwizTG5PcI40W2ybixFOCLC9opDWljM1oqUCtrKFkk0_PBoeDvV6CEQaryfRqBVAY9SMs1J-d03Bi7aR1RfCFtpqXTeN8mBu5hsk3U-w4BNEfEAZVv9-YRDwSgHHSX-dC1YHG1clRXAJaqpwkoP3o-Cjgt7xBUJflc9f0vTjXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: جنگ اوکراین هیچ تأثیری روی ما ندارد، جز اینکه ما سلاح می‌فروشیم؛ ما هزاران مایل آن‌طرف‌تر هستیم
🔹
اتحادیهٔ اروپا هزینه تسلیحات را تمام و کمال به ما پرداخت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442553" target="_blank">📅 14:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afed014df.mp4?token=VHI4xvai5-mn3ehOtoR1BIX8HLDGIexCmtbcTqofxVrzMmjQxwFq-rgFmept7g8AzM_ZUTSMaFVBN5VSJXgRzDXnDobZcq6iSEcWzihqO8atFD1WDrzsoRWobcY0Q9oizRQ5jq3T2PQiw6_tHknWHQahec3Ee_HY1qz-WzcjwPk0Y2lLwqO_stIfxhFCC_Dq_yLmIjhpo-58aALodVrds2hS99uCphyQkv5sykwGytLpesoxHvgc9yXGot8r09mwWnCEk9mfIFf-dgO0r-IDcRET0uvC4PcUaPe29Va8xPui_T4hr0jOe9VeGCNLqIEmW5WnaGGEUhLttiUBeT21Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afed014df.mp4?token=VHI4xvai5-mn3ehOtoR1BIX8HLDGIexCmtbcTqofxVrzMmjQxwFq-rgFmept7g8AzM_ZUTSMaFVBN5VSJXgRzDXnDobZcq6iSEcWzihqO8atFD1WDrzsoRWobcY0Q9oizRQ5jq3T2PQiw6_tHknWHQahec3Ee_HY1qz-WzcjwPk0Y2lLwqO_stIfxhFCC_Dq_yLmIjhpo-58aALodVrds2hS99uCphyQkv5sykwGytLpesoxHvgc9yXGot8r09mwWnCEk9mfIFf-dgO0r-IDcRET0uvC4PcUaPe29Va8xPui_T4hr0jOe9VeGCNLqIEmW5WnaGGEUhLttiUBeT21Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به اسرائیل گفتم «بگذارید سوریه حزب‌الله را کنترل کند».
🔹
من فکر می‌کنم آن‌ها بهتر این کار را انجام می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442551" target="_blank">📅 14:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54dbe2cab4.mp4?token=lzIGmUKxItPq8TouqsAlnj6X-6UMXYyDKcuz3-nUHb3Od27lZz7G6OUP0NBw-6eKD1FZ2_5BAMRpZHaGr32clyeuhhij9ByOveG0aGAyEYtwTiH_uJDQaK0scoMFJcZeKqaT48hUC3udq2qp-AilynfALoYy6qH8Ch5FSndsizSp5YxdnViIVnGzWLd08AbwTQhGWsYVJZFJmILN5w5ZDQzHh0CK-f4xXS4nsTtgXO9n1iZr_Rri0vyrX2DD5_M-9RUAol3Eyy-v9L83sNx0sOTVrwW-kY8vodsN698lrym0lupnc0dxKQvqbaQ1-nshnbM2FmCWNdEh5DHgtAI3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54dbe2cab4.mp4?token=lzIGmUKxItPq8TouqsAlnj6X-6UMXYyDKcuz3-nUHb3Od27lZz7G6OUP0NBw-6eKD1FZ2_5BAMRpZHaGr32clyeuhhij9ByOveG0aGAyEYtwTiH_uJDQaK0scoMFJcZeKqaT48hUC3udq2qp-AilynfALoYy6qH8Ch5FSndsizSp5YxdnViIVnGzWLd08AbwTQhGWsYVJZFJmILN5w5ZDQzHh0CK-f4xXS4nsTtgXO9n1iZr_Rri0vyrX2DD5_M-9RUAol3Eyy-v9L83sNx0sOTVrwW-kY8vodsN698lrym0lupnc0dxKQvqbaQ1-nshnbM2FmCWNdEh5DHgtAI3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانوادهٔ شهدای میناب مهمان حرم امیرالمومنین(ع) شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/442550" target="_blank">📅 13:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b48cc3d0.mp4?token=anS-AkSw9V8OOxLyHGpdBZUccMSHsq2VWASw0g-1oIPFWw9GyUKQqdNTOH4uIRdbr4Xaft6jJ2jkrvFF9NcaU5HyMV0hHkTeWtJElA30vZRP_-GTzsRH8VV_VZOxVEsDnJ29nmphfsz8Szu3-PiH6dnK0tzcsUvyNOCETXJPsh0Qi29unhrnH81_ajwxWlNGn5awuqUO_8apTsJxn7MXhNldFCKTEBMQAJPC2kpltDAkRBBGzod5rFCO_qTrdoTQ4uqJRRCriiaccbGkYUXYjhEtzBdV9hq7ts-Bwe6nidtEX1OYLm03G18gKhJs8oS0l2pODCcBn3cv2qrdeE_oNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b48cc3d0.mp4?token=anS-AkSw9V8OOxLyHGpdBZUccMSHsq2VWASw0g-1oIPFWw9GyUKQqdNTOH4uIRdbr4Xaft6jJ2jkrvFF9NcaU5HyMV0hHkTeWtJElA30vZRP_-GTzsRH8VV_VZOxVEsDnJ29nmphfsz8Szu3-PiH6dnK0tzcsUvyNOCETXJPsh0Qi29unhrnH81_ajwxWlNGn5awuqUO_8apTsJxn7MXhNldFCKTEBMQAJPC2kpltDAkRBBGzod5rFCO_qTrdoTQ4uqJRRCriiaccbGkYUXYjhEtzBdV9hq7ts-Bwe6nidtEX1OYLm03G18gKhJs8oS0l2pODCcBn3cv2qrdeE_oNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاخبار: الجولانی ‌دنبال آتش‌افروزی علیه حزب‌الله است
🔹
روزنامۀ لبنانی الاخبار در گزارشی هشدار داد دولت الجولانی با سوءاستفاده از تحولات منطقه‌ای، به‌دنبال فراهم‌کردن زمینه یک درگیری جدید علیه لبنان و انتقام‌گیری از حزب‌الله است.
🔹
طبق اطلاعات مقامات لبنانی،…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442549" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_jQdtQZ7HrkrzfvFg-e7fqefpQ41165uv0AA4CtOVYyifWWaNXYaoY-FNA90gPnrWeY3EXp9xO4nFdp55TE3M72nTyNNMvzNVcUHOKyuGzvmVrCvADHmXLFdSRRf-uGcnHuT9_en7LMbGPGs7ssA3DFm-gYn7go6IdYfQjaCtrri6WMto1Mq0D2ZRXBwY2_fba41Sax7SnZ6Js33V_97TyTOW17t4asi-EmnvBIw8t1bjPtS2OMQkNVoE6FYUTEnkmsqONZqTwkrhS9OgIenEcZQOmTs4QHROfQuxescXLKnqWGQJTah0xO_pZ4yidHuHSKDu4m6KhymZqr1zLaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXVtJz6RzK5TuzbtxARoRVCYG9sGizYizcQ2h-caLAOCh0lm48liz2Az3_nplbBdqhs_IJHE5uQQoNfpAl8qSHsb2KOXvG9cPFidz5wd-Ap6_Md7kd0Yxm46oZie4tmJUGV5dm28F-NPxBS0tg_zl-QF1l5ZbGIAvjR_t8-KpJPpYG50v0Q8HHmAg30uLZJTUHqjzbR-LlqIctWzEvFjvPua3Ht7pR36di9EdXrP-JXD9Nl-uSk6GiByyfr5Nn0NuOIxQefWasPsc2QQOq45CFUwLsq0nH11LDLPRXKjYvfmS1DBmik89VZSQio14mS7aZPwTUVZjtEq6K-cyfcyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx5y05jLEdXd97z1-AJTLNIMXxfTk6RCfO4xKq6EuXdThxa1xb-s0S-rGio_RS2utSCfCpdsFKlXigvEWH36rWjxucS27EZ_u16eY-gnrYJPYbZKml3gvsunzHra1gjHBtSfmL-7OrE1nB8jN4yPWukipQR8_Iy3Q8CQUpQGt-bOX0IRaMiUwnN-6wO6cl92CwNPKNjayqQxpu74m-VnQdHELZJKFI7VId8q8AJ3WMOFZOvwRbLIUNhOh9HCt3b-feaIvsxo-Gwq6kkwizxsFbldkBgWUPP4K6Or4w_4UnxjyNB4ERu9B59AZ973s-8cLb74heXqI2Hmr5mXCVOAGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ovu3djmAV06YOmcU4dGKu7N5A3c-iPAz_QT42GFutDxNNGOrNFy2eSZoySWUMOIDmlngVBYdanw1Rblv8v-g7aM5BNANN6cOOe5o-WMom1Wa4Hh6wRneu9Fye7SDBvX381czsC2TiJSDTkzLPDh3Bhuu2Jy7Vy9ZhcfzmeFz8I5d5cResay3fUshDKNIl8bZbYgtCgxSO3K8uYKBoscl4K7S2M1mlzBiYpXoOJdmfMz4psnLZxZI_w-8Vdb73-PN23YyQ3juVYbxaONvHN1UZLoxtWP8DcsN94m3cOKzQjpztBT2SB8RBP1oJgixPYdpc-uxZgXaodU4RiwtAHRDMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfLNiTNzVfdxFfCpLuYx_bWd_D2E4b_GMaexsGuZJBQssoFWl6BZJkfaJ-KwOdEvTMcuUbn9-8AwL3wBJFS1XAjT-Z98sWQhRmBD5nwkX83OiYr8sVBDkch_KwQpGiDPKXzARLx48aKk6f-94q73nHPHLrGrwpL6VYAJzdd8yzdOdy9DSEu5pTG_wu8zs_OhpZVZx0Vvn5GDMtkm2VkN5YmBnLFJcaTl6A0Ppakc6K9VC-BwD5kEK2FYrogOdiljRdKbmRLqAlk7P3KavLFmw7a-ChiMs9ovufSGbXRy9dK-TchDLyldltsZkeBGUnthlkebsoDVV8jxLRT_OR0INA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrM3GkfOb43C3DQkGkj_3L5qQV0yo_OAvAXf7SKqDtk5edxZ-OC57tMIOLlzeEm8CQvinX7qyw4tnU5oggio-B6fgHMtIY4tg-_-dt12FD6Da3B5_s85GIcigC1Txr2EHYMbcc7nIFqf7Y5e5CooAH7r9BqQAk9AK6g_yHT07xVu9L_3EjvosrjxTgcq5D_BbFZ8m6fBdkQR3Gi2qEGvvYAerepP0-qbndUiMHHTAtfMLp7PLcl_eJwRV2TwEoTQX1v0syUQ_IiIs0j-3_mPJbK5n2A0qPzNyizunHryJAc_t1toZRVEgibNFrevO51baEI5yn0MEspc3OlTknTf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvHBb70qNVUkYMbm6iMJj98FAONiGrxiiHNWHCSeze6AibU_J4WHl8o0jf5iCdVzSt5SKSJVb9gyqwDxcaxsKztamA-HalFdmy1xsw2j_tp4Q_x45g-HA4wcZ7a7uXYuHy6pM6ExqZ_u0C0shBHC3nJTlBXSRktv4pa5JsdA93eITm8MKChvs0-lA010yaA-Rjz4741__CTaiex6Benyr2RmdGrgErpctPQ14cqwUep-JXzjIdRT2o5V0GsEQENalh48Atwpn6aRtfRoIbzOr2ZJ7m77SBfpgQiDNvzxGDkat-mDOzqSshmQ9S9WashV5tXufOdZggehMbanq_tBGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عراقچی: از صبح دیروز جنگ رسماً در تمام جبهه‌ها تمام شده و هر حملهٔ اسرائیل به لبنان نقض تفاهم است
🔹
یک طرف این تفاهم‌نامه ایران و حزب‌الله هستند و طرف دیگر آن آمریکا و رژیم صهیونیستی؛ خاتمهٔ جنگ مشمول خاتمهٔ اشغال است و بدون عقب‌نشینی نیروهای اسرائیلی از…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442542" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b96935ff.mp4?token=IAliFKAwcjA2-her-UGjyPt9iKN8ZU69aQxvInfkJePArkHisgm3kl2T2me0u_Jmxml8ifL7tLg78lZqR2s3GJ-Sf559la-S4GMHifZZLnfCi8SXUoEKNLi8-w_AjgkdU1YUa3jbLGLli7zsPft9gAgyUxVeKE43EPQ7Y-getdKxM78aHAq-63lIkzxLhZlQMlAE0hqORgsybYHxYz-RxdPoS8iN3qGaVLqT6k-u5JvF1EBXgU-p-wjlvmwMGJcflewzKxBIttV-53XxJ5f16w9OGME56rkmaUjCSHFHiYNLObLVN4WGRRmjAEcz4t7EOp81LM_38eTQ4SMm89ad5B8nLM2WDhMdoSko9ffDUwGjbVYPPmjw2yMcSb4gxOCDHtQPl8d1qWmGi0jfNE8UOowyVh1w17_hhSd68EmIppYdeEUOZuq2IXC2xchv0tPPLdzRVsJRu_DBlJTl0fvxQamGJjjW3qh-yT0X41XFuP554DQMFxb8jX5wS1f0dPMzUnrAVcnDe-lAvLWUj-TOIvcw7aNocHzxmWxSqxJIcruyy_V71K8tHtkMPQ_tb_F0LAZG0INsa-Si6URZo2d9ZQeKzrAniV1efQClT9nly5ntYr6vtCNj2FZcyTdaDCYooihgE7up_mY6B2bUlSf5val3ye_dpEHjycNJ7rUx9fI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b96935ff.mp4?token=IAliFKAwcjA2-her-UGjyPt9iKN8ZU69aQxvInfkJePArkHisgm3kl2T2me0u_Jmxml8ifL7tLg78lZqR2s3GJ-Sf559la-S4GMHifZZLnfCi8SXUoEKNLi8-w_AjgkdU1YUa3jbLGLli7zsPft9gAgyUxVeKE43EPQ7Y-getdKxM78aHAq-63lIkzxLhZlQMlAE0hqORgsybYHxYz-RxdPoS8iN3qGaVLqT6k-u5JvF1EBXgU-p-wjlvmwMGJcflewzKxBIttV-53XxJ5f16w9OGME56rkmaUjCSHFHiYNLObLVN4WGRRmjAEcz4t7EOp81LM_38eTQ4SMm89ad5B8nLM2WDhMdoSko9ffDUwGjbVYPPmjw2yMcSb4gxOCDHtQPl8d1qWmGi0jfNE8UOowyVh1w17_hhSd68EmIppYdeEUOZuq2IXC2xchv0tPPLdzRVsJRu_DBlJTl0fvxQamGJjjW3qh-yT0X41XFuP554DQMFxb8jX5wS1f0dPMzUnrAVcnDe-lAvLWUj-TOIvcw7aNocHzxmWxSqxJIcruyy_V71K8tHtkMPQ_tb_F0LAZG0INsa-Si6URZo2d9ZQeKzrAniV1efQClT9nly5ntYr6vtCNj2FZcyTdaDCYooihgE7up_mY6B2bUlSf5val3ye_dpEHjycNJ7rUx9fI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/442541" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1BBEJVjkZFAyKsnPhbo7agmZYIjn8EGjnUjCtDX59UJnZZ75tILhyKLUCfc0h2Du8U-bNGlKc8zqZaZWSE-wRj_R-qoNHem09eJ9JhGiMGXnEDqlsWqVQiOhJ4RoNw6TieWCxv1Xy6mqYBeIR8qHsaQS21HoWF4K1nEHPsAc6qf4XXMUtB7DBMXYfWCogGPfCxvXljwBUEVL2202zaTfoRe6V9jhMEHavP-PRkK5Q6T0gNbtuKriaZkXZlbNvWiCHIg42XaFwXgHg4yK81gSI4YHlgHnTsxRljg0wIX07h75WTvSruAOpjS5rjUhIxLJRAKL__PWOdFa_qv2DUHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjDDgMS7c-sndohh5NwcgczLVo6BVLhZ6r0d2uTrJWXYhuTM1f0qlvreedG9uVs1FfXoOqQOPIQGBY1hXvGgRj2ztUDtpABYcNPTjAZlc9qEHE3M6yyrZUdLRS9c6PG8gZDYGwtMfwBGO3SVmCSG1f25gpIvaBIQr_xyUsy-p30zPAKBtWpwC3nN6sva78-EhQ5NsMVNE6r2SNKhMt2ghTSKm_Ltb1bvKwGfveCX5CU3QON6_QYx55BeKUYztuBJahHBnpaPui4Yzb9Wz3ElhHgBsYICUO9paS7INL_j4SVRp3xOSX9lnWOz785f_laEgxCX-nVKVhjW9rcRMCFa_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ تعویق یک‌هفته‌ای زمان برگزاری امتحانات نهایی دانش‌آموزان
🔹
آموزش‌وپرورش: درپی برگزاری آیین وداع، تشییع و تدفین قائد شهید امت اسلامی، زمان برگزاری امتحانات نهایی پایه‌های یازدهم و دوازدهم یک هفته به تعویق افتاده است.
🔹
بر این اساس امتحانات نهایی پایهٔ یازدهم…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/442539" target="_blank">📅 13:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63468508a.mp4?token=XheaelvkdwHRZk8IDsHe18BZKMYlGu6yxu0DfU2MKmTbopVSheuP-HXW69BqVGeroRI5WQg1r5n578mmpuVJ6pBEVgQD8wV9XfEnQOhCLMcziiqC0aNS2Xl9DsqAiFblQoy2lKyABmQkFbimIqghYw4y441mvDpYFhFjaAEnQA_T4VC8RivD4qdGXKZ3QddQVDQVozftASz0wdm5vwhhqYYshypGcM0AnZJmki-uJmKp8g3d5ztbx2n1L79b1Wwnz2fodwNUiY9bjnomLT_JBLBEJ4F28B99APaVnAUPDgCRysjybzCbkV-ZqecD7yrAvYds4HS_OME-5Ia01lJXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63468508a.mp4?token=XheaelvkdwHRZk8IDsHe18BZKMYlGu6yxu0DfU2MKmTbopVSheuP-HXW69BqVGeroRI5WQg1r5n578mmpuVJ6pBEVgQD8wV9XfEnQOhCLMcziiqC0aNS2Xl9DsqAiFblQoy2lKyABmQkFbimIqghYw4y441mvDpYFhFjaAEnQA_T4VC8RivD4qdGXKZ3QddQVDQVozftASz0wdm5vwhhqYYshypGcM0AnZJmki-uJmKp8g3d5ztbx2n1L79b1Wwnz2fodwNUiY9bjnomLT_JBLBEJ4F28B99APaVnAUPDgCRysjybzCbkV-ZqecD7yrAvYds4HS_OME-5Ia01lJXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانهٔ آمریکایی: حال ترامپ خوب نیست
🔹
همزمان با سفر ترامپ به فرانسه برای نشست گروه ۷، هفته‌نامهٔ «نیو ریپابلیک» گزارش کرد: «واضح است که ترامپ حال خوبی ندارد». این رسانهٔ آمریکایی با اشاره به این سفر نوشت: ترامپ ۸۰ ساله در دیدار با ماکرون بدتر از همیشه به‌نظر می‌رسید. به‌سختی چشمانش را باز نگه می‌داشت درحالی‌که ماکرون داشت از تحولات صلح با ایران تمجید و اغلب برای قدردانی از تلاش‌هایش به ترامپ نگاه می‌کرد.
🔹
در ادامهٔ گزارش آمده: بعدتر، ترامپ که در کنار ماکرون و همسرش در فضای باز ظاهر شد، خسته به‌نظر می‌رسید و دست راستش متورم شده و تغییر رنگ داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442537" target="_blank">📅 13:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0TnriyETisoM7JpOdKw8pibY4QRUV8HMr9lkLR1fsoDpp7AXMH8lBK7pnL4acEag4GZvk57E4FutYSak_LQZmrvmYv4r89emfLctJ8x4lJSwY69wg_NxGUPdTKgoqRI8zEi-y2OI86poqoipqQ26H9l5lrqqDhdUSY-MGFViFwEMVrtPpWLXXznxXFDBIz7yAvO5IIHAtufpLQhOU6bVXLkcJAzCL2FN6ZQNXbpoNkbVi686y9hMheBZwGEfpoGNQsjT6lljkgt8USYXu7nKWHE0UsOdEJQz8HsFV-v1zLdT0q-ZgyqG9Sek7RIOiqSl1iOxLJ5FkbZJApdSq9f9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BsZbRCAaV9kcxPiDJln98M7HKdmCtsScCvldZ3XwqcNdCa9SCpJdG8tmRiZcMH3iCrRPOGsZFoLRt7YWzDVL-QGYH45OJlMdg7v-waYdwUN9cJlEL7U6EyGz4l4HYpuP5jsZz1HiYMDXKjDt4crPgIR37JQRiTosMYeV19Gq0460v59o1GQglSaC5Tylo-U_MGe85YpKwuexnr1mamaJwoQaMe59v5fV4CGYtzbjdBLfPcndJq9SX36ZgOemjyV6XXDQutXUzVbUTkZYhKzXti5cZpIDbc_srMy79cxOjasHp935GSn6T0_6OGQmWHAa-ljx-VOoLHJZYsyEH8eqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyRhN9TkKuBSM9xTtWpZIdMe9hP2W50tdN1wSEl5FgKwrBmUN-yhkowuuDnJqT97iyVMyhJUmzK7fC_UpH5L2nhSUFM-x9DN2cTFC3UGvrwQ78r0vcCiz1hY1lIwtdg1DQOSkS2yj2d8zJWcYcNRxAmXrqCkJHTKX5OR3Lb6Sjkiq8JyT3nmv74MWeoU_6jmZjBNB1wmY3Y0qaRTiobZJNF_1uv3TENcWG9m821TpvNUvrrr9R1Co_PkzotOIhD4SxLj0Gdud0bdlUwDT19s_u_WKvtqsXaR6758BORSEOQFmXX5baX-sI5c2PlXCG9NmXRI5zLwI_uJlimLOAnVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyimdzSIXIHH8rqTGaT148TWbKxnHH-sxorvF-vtAEVjb2rEoO6b7zjK13N4Vmb2Ge2XSxhxSopbbzU6phg4RTHZZuEsGVYtIT8gF3EoGIYilKW2dWljuSV2VZScBdzU4ALVChqZ27EF9ZqFCvHdcjy-gUisV-3Rgfkreh9W5TVmgEwAh_zGRYOwXEFkP7LHZrdQG-kSvTgpfrk5tuxoCTRnrL2uTWJg5GP6CG7Ds1uCqy10V8OiU_AvFENpzM6_yrZ9rLsmK7tKLQMfY9vikP2srvkppeHE9TyGlxHAVd2BC3agbcz8sBaaq6EOtdcvp96k39NRRGGSS5z_ASupaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJ-d97SE9naPdQJtMSB9IF1oJYwXJqU2V2KNgyaPuxM_SBUSg-fjI7paRjhuE_iYbh1ErwJ8nmrlWlXcDCW4_7u8CbnM4v82WR-xzpj34bMY_6b2dhWiVmgMBByxyBG4n-GVYscYnotLVT4SqGO9_Jt_naFhw3rRtSEMUHexZzmCOQac1KmzXH4yTjsiyaBEt5M9bFh-KDThykIq-mnbJA2GPzYJR2tumcKsQ930qvBqg4HG901eDS0JW_fu-TwIz02FdledZmwOrPZbbOpUIS4-WGgMGH7FmDyCeqD_5kMXFGJmpRDH9Ys4-E4-fUOsuu4XvOHJg3TZ4ktRq7HnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OeyViJDjupsxt1psD010L87JFbcHohETXWezbLL6PI0vz3JCsXAaKt-Hvx9iS61vexAKybfngtY4SsiOwVwnOJWwB1P-HXuejW3fVYHjPWuaQjg-mAQSV8YqFer0TkTplFroISvVnMJnr2GUPdZGiCkkRdU_40o-uxxeuSQMtleWtkZeaWde1sD4hQBoGYcF6TtXNbWqX1Pm-px3sYVdvNU69udEFQBC09vEG7lIJ16hh_9GbY1__jKMJY4sGkNuCQ3nwE43FCHFzGhTD3i7zXGzseOuE4DkaqF5h2KnQhgfzWj6UKKQRLyDUnBbFEtFGGF3Ahwl2grHOQr5ahehRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bjp6pmwrWPvMEet8t0sgD2x7FrParcvVUX23FDDyvuoT7bi5DE7a3sorwMd_XK2uiR8qOObHvLCuoJJgqjZSd5CloJexzLZpoYuUNwR-5Mp_Vo8SYI3IpxnG2iMGpUHztFCmovdBgFwSK238knarrjORD6rhEp4O1SKqT5WLindlbD0v_52bjx4zRuE1LHd1Wa8guYGEzAoKs2mwq2euuUB5aMhAnWooVp7_E-YfaoMYeUlh3QbHtEQjM9HkJJfX3MCdYnY0n40l2sehHdwKolebNgBiPQqLXPQqxadvpUFa3USZB63MVYqXs8ORu2OHO_MOL3SWYQYI76HmX-WZlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعطای نشان فداکاری به خانوادهٔ ۷ شهید ارتش
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442530" target="_blank">📅 13:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جواد زمانی و ابوالفضل ساعدی از لیدر‌های مسلح کودتای دی ۱۴۰۴ اعدام شدند
🔹
رئیس‌کل دادگستری استان سمنان از اجرای حکم اعدام جواد زمانی و ابوالفضل ساعدی به‌اتهام محاربه و افساد فی‌الارض از طریق کشیدن سلاح گرم و سرد، تخریب عمدی اموال عمومی و خصوصی به‌قصد مقابله با نظام جمهوری اسلامی ایران و اخلال در نظم و امنیت جامعه، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور خبر داد و اعلام کرد «حکم اعدام نامبردگان بامداد امروز اجرا شد».
🔹
در ناآرامی‌ها و اغتشاشات دی ۱۴۰۴ شاهرود، این افراد با سوءاستفاده از مطالبات و اعتراضات برخی اقشار جامعه و در راستای اهداف دشمنان آمریکایی صهیونی علیه جمهوری اسلامی ایران، جرایم متعدد از جمله تخریب و آتش‌زدن اموال عمومی و خصوصی، اخلال در نظم و امنیت عمومی، اجتماع و تبانی علیه امنیت کشور و سایر اقدامات مجرمانه را مرتکب شدند.
🔹
براساس مستندات موجود در پرونده‌ها، محکومان اقدام به شکستن تجهیزات و در چند شعبه بانک، ایجاد آشوب و شورش در مقابل فرمانداری، واژگون‌کردن خودروی پلیس و مشارکت در آتش‌زدن آن، حمله به منزال و تخریب خودرو و انجام سایر اقدامات مجرمانهٔ مؤثر در برهم‌زدن نظم عمومی و امنیت جامعه کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442529" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqyyjJzaS63X8o3rVjQiGO5QgzK2oafMcWW_9Y3AJkv0Ad2k58hgPSuFunm4l8aluVHNMjRPSc44eMMa4rCMFskxpKa6WKDjQnXeVghtg5W1eRzCXbotnnItacNKFeDCFvXsLk9_o_KjRt3BHetjyOUtUGoCuHn2eTVTAOjpwVbKKYaK6blhLZX7IrhB3c9gSTEGDw4PR_zgvp7FpJdB_lDGJNZyKn5TmYTJT0LiZaCXyhaD1VWGGz9oP7a0dTgZk0f0NGpjXX-BQIoxarJgTwktvOJCUtjgVOpUmDWZ4Ukma7SVaodJUxSfXzvmERXKOBZo3oat56SVgKw_tqY5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با عبور از مرز ۵ میلیون واحد رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442528" target="_blank">📅 12:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
اذن عزای سیدالشهدا(ع) از امام رئوف در حرم مطهر رضوی
🔹
مراسم اذن عزای سید و سالار شهیدان در حرم امام رضا(ع) برگزار شد و با تعویض پوش و پرچم گنبد رضوی، حرم ایشان به‌مدت ۶۳ روز به‌رنگ عزای امام حسین(ع) در آمد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442527" target="_blank">📅 12:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYNUuy4NExvGKLJNdpFUnUBDLjvL6-pwbln-ro7zQMqHnYkRkAG6ZX-FaZx2c09V70fi3cSFCSSQWs12O-lUoHNGaKuGATfrgSxW3_G4dFFts92zi2O0v_Z9Hjar8IAV79GyqsEVk7LXs28TGbUj5cLeiS8wpxAulrlFShxcOnd-uH1KOGFMsU3RAwPC9Eely8wtfozG_qug90aotwJdGy2Y1MiE3UTrN2V29mK-yv_O5IpZKM0Mb74r3DmibUlx6PzvBBr1tvdoLDekqpsg22Jm4VoTeZPDGEDhYc05YSSVlAzoa_TAm3aOusFWNM6HKMDa1465TNSWR1f3cDxlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم آمد و افق خونین نزدیک شد
🔹
سال ۶۱ هجری قمری چند هفته از خروج امام حسین بن علی از مکه می‌گذشت. کاروانی که از مدینه راه افتاده بود، اکنون در سرزمین عراق پیش می‌رفت؛ سرزمینی که هزاران نامه از آن رسیده و نویسندگانش از امام خواسته بودند به کوفه بیاید و رهبری آنان را برعهده بگیرد.
🔹
اما در همان روزها خبرهای نگران‌کننده‌ای نیز به کاروان می‌رسید. فرستادگان کوفه یکی پس از دیگری از تغییر اوضاع خبر می‌دادند. عبیدالله بن زیاد با شدت عمل وارد شهر شده بود و بسیاری از همان کسانی که نامه نوشته بودند، یا سکوت کرده بودند یا به اجبار با یزید همراه شده بودند.
🔹
چند روز پیش از آغاز محرم، خبر شهادت مسلم بن عقیل به امام رسیده بود. کاروان در مسیر عراق حرکت می‌کرد و از سوی نیروهای یزید زیر نظر بود. فرمانده‌ای به‌نام «حر بن یزید ریاحی» مأمور شده بود راه را بر امام ببندد و اجازه ندهد کاروان به کوفه وارد شود یا به منطقه‌ای امن بازگردد.
🔹
فضای کاروان با روزهای قبل تفاوت کرده بود. نشانه‌ها حکایت از آن داشت که رویارویی بزرگی در پیش است. امام بارها در طول مسیر به همراهان یادآوری می‌کرد که اوضاع تغییر کرده و هرکس مایل است می‌تواند بازگردد.
🔹
کاروان در این روزها تحت مراقبت کامل نیروهای حر حرکت می‌کرد و عملاً اختیار انتخاب مسیر از آنان گرفته شده بود.
🔹
محرم آغاز شده بود؛ ماهی که حرام و زمان پرهیز از جنگ به شمار می‌رفت. اما این‌بار حوادث به سمتی می‌رفت که قرار بود در همین ماه، یکی از مهم‌ترین و تلخ‌ترین رخدادهای تاریخ اسلام رقم بخورد.
🔹
کاروان هنوز به کربلا نرسیده بود؛ اما سایهٔ کربلا بر سر همه افتاده بود.
@Farsna
-
#روایت_کربلا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442526" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هرگونه حملهٔ نظامی رژیم صهیونیستی به لبنان یا ادامهٔ اشغال سرزمین‌های لبنان نقض یادداشت تفاهم است.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442525" target="_blank">📅 11:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-OWZNWRFmY0i8uN83rc9VInfXUQqPKRAOzTUclV0qLJCp6x68Hms7U0hS16EMJ8YuDot8kmpeIe-A2uMmKJLQCrygOxxijhrU2TFSDooKNOCHM0mKKLhn8mlTfeNKh2eY87evOmOgxXvQdRBmobE-U5sBKXniWkf-gTUYTd0tUyerIrBndMxYsFifB3EiAaPK20k4sOce9MlYQfHjSgHAPlMxiXq05N79k1PILE0ubkozlBCTWTQCSI5r9YjomeeB6zBtoGYFxwQ1DJ8w3YfIuGsS4nAywlYoGqECYM4dhvm3qMoDxQL_1HPW47v6M1mhhQFExbpMDx_IkytNU6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حماقت ترامپ
🔹
کاریکاتور جدید کمال شرف، کاریکاتوریست یمنی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442524" target="_blank">📅 11:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=Dcm5dCLMV3cjvzCyNOkzw89ej8KeT3bM_AZOgqltUgi74G72fu5qrwhu_tfdF0sa8TtxiXb84DnwvgoFgLadOvQmV0-PWtxtFJDqY-4QOV--bWDig1MkVdDDbL127iSB8GemJaPIPYHPurgnEIkqCsPmPCCw33npfvLlQFAWjPkpYXutc9REbQFrLNCTGtH4gdUV_rUu1bG1TNSgL4-AwpwlibNqq6hWKzCe7Y8hTBqMcKVeLc9GbZ2CRK4_s9rvLnGCtad2r-Nus2AFqG80s8ESVbCw3qEA0RUX9A6c2kTYKYSrIYUwgI7vWURHZZvcLSo03NG8qL2SSVii4NBwv6HCYU0Z_NwatNwGy3w4tKPJYZSVtlwZrs6FI6KeBkQbnuT3P_3OcsKyikVl4rJT-_-GhoEDmYruF8yh4RgZC9-Z4UnmeLe6DK3LOGYK1fWHOguRn-8DMGeF0uGeLDtVe6LjYGTMozw3v7F6SZZQOk_-mjlMtKdFybo-vyrPjdRQ-Ja_z6h-YL604oi0zBAkaRKXibM-8wQ6xKcwJmjXh4cHzJoeT830v7yXNCPI8jhjsAbJqHKmo948zYdpO5Cug5Bv8KFCF91tPCoNifWmR1f5lMTJPgms500m6oG9PKSYZ3xMQK_qO3yGKZ7VWPgur19UUWxBFbmBCsJhz5NQL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=Dcm5dCLMV3cjvzCyNOkzw89ej8KeT3bM_AZOgqltUgi74G72fu5qrwhu_tfdF0sa8TtxiXb84DnwvgoFgLadOvQmV0-PWtxtFJDqY-4QOV--bWDig1MkVdDDbL127iSB8GemJaPIPYHPurgnEIkqCsPmPCCw33npfvLlQFAWjPkpYXutc9REbQFrLNCTGtH4gdUV_rUu1bG1TNSgL4-AwpwlibNqq6hWKzCe7Y8hTBqMcKVeLc9GbZ2CRK4_s9rvLnGCtad2r-Nus2AFqG80s8ESVbCw3qEA0RUX9A6c2kTYKYSrIYUwgI7vWURHZZvcLSo03NG8qL2SSVii4NBwv6HCYU0Z_NwatNwGy3w4tKPJYZSVtlwZrs6FI6KeBkQbnuT3P_3OcsKyikVl4rJT-_-GhoEDmYruF8yh4RgZC9-Z4UnmeLe6DK3LOGYK1fWHOguRn-8DMGeF0uGeLDtVe6LjYGTMozw3v7F6SZZQOk_-mjlMtKdFybo-vyrPjdRQ-Ja_z6h-YL604oi0zBAkaRKXibM-8wQ6xKcwJmjXh4cHzJoeT830v7yXNCPI8jhjsAbJqHKmo948zYdpO5Cug5Bv8KFCF91tPCoNifWmR1f5lMTJPgms500m6oG9PKSYZ3xMQK_qO3yGKZ7VWPgur19UUWxBFbmBCsJhz5NQL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر زیبایی از یادبود شهدای میناب در رختکن تیم ملی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/442522" target="_blank">📅 11:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda22ccf1d.mp4?token=ByzGOlo1BubCAbfyISVIA8YyJoorJHvXSmvfcJds5f8DZ5AOK48vQbVPRFQwor08-q3UcIvXH7PdaLCfPIKLQyyXuAm5599hDYA3AlIPXn4uE4A9ZwYQfY5ajXm9r0GIwwwnSKhL4l3dsj9Bz5qGTDTetKVRZUrFSjl-Xar3IRYus5WM_wqulCaB8G2R9jckdIyZbtDxjxi1n2xTiy0E4Bp5ELabb74J06I2gbWr04G_Zdox2K_spJD7aOo4efgFvdEKlDtCqPeP130gDIg1Vp5AQcNquBx-2jvfaXV6EsH7CcsEPkqDbOQyIqi1XVwRa_XQOl7QvxHGy75PGngF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda22ccf1d.mp4?token=ByzGOlo1BubCAbfyISVIA8YyJoorJHvXSmvfcJds5f8DZ5AOK48vQbVPRFQwor08-q3UcIvXH7PdaLCfPIKLQyyXuAm5599hDYA3AlIPXn4uE4A9ZwYQfY5ajXm9r0GIwwwnSKhL4l3dsj9Bz5qGTDTetKVRZUrFSjl-Xar3IRYus5WM_wqulCaB8G2R9jckdIyZbtDxjxi1n2xTiy0E4Bp5ELabb74J06I2gbWr04G_Zdox2K_spJD7aOo4efgFvdEKlDtCqPeP130gDIg1Vp5AQcNquBx-2jvfaXV6EsH7CcsEPkqDbOQyIqi1XVwRa_XQOl7QvxHGy75PGngF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: جمعه پس‌از امضای تفاهم، مذاکرات آغاز خواهد شد
🔹
در مرحلهٔ اول مذاکرات دربارهٔ خاتمهٔ جنگ، محاصرهٔ دریایی، تنگهٔ هرمز و آزادسازی وجوه مسدودشدهٔ ایران تفاهم شد و در توافق نهایی دربارهٔ موضوع هسته‌ای و لغو تحریم‌ها تصمیم‌گیری خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442521" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85b3d54d.mp4?token=Adyzi4qPDymqdFf8_VoMJeGqYazYX--hU_ElaYyL10xi5d6Dk1e3Iobl3hAR0uMbR2rFcACJ0zQf6pA-M4DCtoostm4FON9fQF4OgjOC-zORaWCr58N4R2LqcsGZhkvt6i9BIucqdjlQG-8oKhSk1oXez6DH_WKFzBgVob_iV-_sQih0FZQvc4fEwnUtCbXFXBI_5pohqJ0tqv8Dfjz--zz45-d1jUaxjCwNj42ntPpHkca4z1PiwLmqegeXEGlGbbSWSoJLmX90w4foY7LhUO9NIJQF7QU62G2aB6whnuk5pJ8g1V4bVogcLar7u8_51t8WdkBs9P_mk1UpM9du3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85b3d54d.mp4?token=Adyzi4qPDymqdFf8_VoMJeGqYazYX--hU_ElaYyL10xi5d6Dk1e3Iobl3hAR0uMbR2rFcACJ0zQf6pA-M4DCtoostm4FON9fQF4OgjOC-zORaWCr58N4R2LqcsGZhkvt6i9BIucqdjlQG-8oKhSk1oXez6DH_WKFzBgVob_iV-_sQih0FZQvc4fEwnUtCbXFXBI_5pohqJ0tqv8Dfjz--zz45-d1jUaxjCwNj42ntPpHkca4z1PiwLmqegeXEGlGbbSWSoJLmX90w4foY7LhUO9NIJQF7QU62G2aB6whnuk5pJ8g1V4bVogcLar7u8_51t8WdkBs9P_mk1UpM9du3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: متن تفاهم با ایران بعد از جمعه منتشر می‌شود
🔹
این سند بسیار محکم و تأثیرگذاری است. مثل سند زمان اوباما نیست که یک سند افتضاح بود. این یک متن بسیار قوی است و من می‌خواهم که انتشار پیدا کند. بنابراین احتمالاً خیلی زود این اتفاق می‌افتد. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442520" target="_blank">📅 10:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICKNZyYD8kkQBrH4zl3Az_fnuBg7qD6fYIncaVdgKyzrNj26nycS7UdAE7QSbUbX-jbGrPtuEuVEIB_ih--p44SnPbDecMgUiLBKYlEftqbJ5HTLOFI-5y57NuN4DN-98K6wlJR1x9mJ_-PX4NuzvO-tyKRG0x1NEXG025LQ6Xt9DOT_loyrcPbnbwVjmc0gdVpgcM6KgdJmxZV_okCWgBcs2xxUtU_WcE2Y-P8MS_Rsn0MTgEawo8d-CrpSaxmCHP4NcDSccopv0Mxxf2sJSjiB4ZLQceRpUs_HNeNthmJ8ogufKZt0jRnnZWhSOf6QFeFWpxKbY6-Dpx9Sgz5fCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXn-6p4ffdGdtjR1FZh4pAEi5_E5B0B4Jd4DMF20P1QLSiZSh-Pdb3b3JWCS64jlDjAuUxiso-ayjMlRajd0r010LJIjEiZuc4Kli8DCbQSC79VlrjvlYacpmOFgmCG7YPJt1uveg4wlPxIdeqW51QIxTfX2AreolICkzo52_LoQWiY4o60HPJDo4QX-nAUfGV-E-suaeMSgCkqerW_fmaP4Gbyv7pqvIrtk2XJ3x4QvpE3F5i7A4KW7y97-WIuyvXMPAvR3bf_mhq_fzTLyuoMW5T9XUqZsTc-0VVsiTlt_yJBU1W5htyony9Et7Gc6oPh7HIlGfZku6Owssq1o8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBYRg3tRxtv7-96_els1lgKPUHz-b0DuA8oiPbft54mYzp_Yo7SNCMuKDCWvemRVLM5lYCW7MFgvT4ORERHz8paDX_Tzc3lsg6nCmMKYISG2rvuJ-ZbxeFOKn46ZUn5Xmn_Y-TGDL3FSxnJDHI3OK-exE6-cZYziqdBrcVy43q_Har9eFXsCBEab2S7uxs3vpCrg9ESYdpi5NMtyWXs4b84OB98I2zxU3KDw2xhhT3mnE-Q6520SH1PNPjCb5b0o8paPQ-zeRrWNJb8TMH3_GzIP5-G_OWZ3eTzmpXdzbIHLZ-Rm8y5Lfx9IWAGbwRp0voN8RvZGSweSSM9VEV2rNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6IrpiLd7TqvlfqMvUqLfJBzXUnHo-pTkBV7Oi2q5GQF0U8McJ-GhOrZ7LYovcd9Ae71I12cDRX_Ds3ELRxHfbpQNXvj0GNe2epmT-JJt-dQI2CszQw0MGq3-ponqlZFUJfoeN2gkFi0OglSAeb4UoO-3oUdFj93O6CBrml37hIqMS_SZHhfolTCoINKaOubLJrqEq_7BMKR1XJGbvuyQHkzxF68tOOrc2u9oTagIBlUFVB4JSTwjjU03iuf4eFmBkKgpT9REfJi_V73qAcUdwguq6-xWqTpW5BnskSYF-uQxR7qtObZ4yWfwGheN73By9wP-Y1S3DuwbQx1He45kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOfbYYGt9Vl2_eJYH4nEPXMIfXl1CxUAKl_ofi8V3rYaui5K174vyj5HscLlr_Dsx4c4lFc6QqnsAaKwjVKOnFoUjLuht-0ACFx_nJu0v4DIgxpExlxGUVZJuVqP_NRfOr5zheNv2lcLK-EI4CD4uWvqXIWEYeBF9T5Ng54tT8MsnOHQeoL2ku2f9zuhycfBxklr62oyXFVetD59fZPJ2ORlNUdLc4_4wbkU1RieUp_CV7F5DvZUGVOLSxBIp6An7IHAr8hztbjqhFF4V7hUe6A5VM7Jf2KwoNBUxEX_QxdTZavbhozynmOxKJxACxekKNc2uBG1j8pITwIOG-Yt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS6VtIYsZT3IHBdU_FomRQebwrva5vKnG1F-UFswH16WLeXJtU2ZpIgX-KuIBs3ablpFUF0BeUE1Kls8Q608X82Y7tbkcpPo6uUFMpRCEAUsJ6sHfP-ej_KkACdngUaQkpzczB4nop35rBRgABiVrmYLAOfH4bREIae32Ze4GpngVJD4DdPg3IykHLziGk6zlLiMm-111_5bwhQcjwPa5U5WsmpsZw2Rqpu_c83wglvVIxwIOjkOU22-aSAthJ59Y-tonqWkyn7qsMW87n1Se-VhQRVc7QNKL5LtAAzRlW0r7Wsva7n-ntOcfGJr6zbEbxz8MhR7gQGxqr6flMGSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOAsH5_9anK2xUdfNo7KUcSdL7o7ybbU47BYflsnEpnS0mTvqWDC849IVsamcGSjsMhYRhwQ_7PtNYQ04_dIYR6EXYmCUOpmS8NaXMFbg0hDVoar8mL-s79J_0-nx08tsetevaPo47oOrfj10Ot6QJZo-3sZXYHEejHssszOeX3OCLPeDQ-F6Ja91hJf88SckmUGD2Ww1YqkZLB3DNafEHhn-fhkmipuUGKaYPYAR6S8wq3hw_zLFdw3OkNPmY5p-x-1yPPsNz-xWyO9lfJq2XLKzbHNba9graeXIHdCx0aQrLceBlK0bRr2crVM8YfX9ZiF1sUaU4xIEWWT1xTxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خلاصۀ بازی ایران و نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442513" target="_blank">📅 10:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4pzZoMOxGbN17s-KrY1zcz5lOuILwhrO8882VlU4frhvFI65m36LoMrQpcO4S_IAo1wjnAMgxw4tRutzdcdvtG9EWIwK5SglrC-ztsnWwhcboIMhp1wnFYHtbou77uLWNZTunxJmhDH4sHJKEj1-XP-DizE2rrLBBgwm6TD_hOT_wTf__lW85vUt0Xz0Sr65LEsLP3ucuoVmx3Jxnbgg7skdzwYLO3Nd3AZ9svmrVnO2-35RANYmz5Ux0Cyb_4xauzTKIz2zGkLrkIgmedccuO0d1rLx6wYtIcS5crCxIK1m9v-DeQGex5ah2tFGYDujyZfTOPTfd3w-PzLuXIE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: هرگونه خطای دشمن با خشم انباشته مواجه می‌شود
🔹
دشمن در جنگ رمضان و جنگ ۱۲ روزه به‌دنبال تسلیم ایران، نابودی جمهوری اسلامی و حتی تغییر نقشۀ کشور بود، اما هیچ‌یک از این اهداف محقق نشد و در نهایت خود به‌دنبال آتش‌بس رفت.
🔹
برآورد دشمن از مردم ایران اشتباه بود؛ ملت ایران با حضور در صحنه نشان دادند در دفاع از کشور، اعتقادات و نظام اسلامی ایستاده‌اند و بخش مهمی از این نبرد را مدیریت کردند.
🔹
اگر دشمن اشتباهی بکند با یک خشم انباشته مواجه خواهد شد که کار دشمن را بسیار بسیار سخت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442512" target="_blank">📅 10:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjcTDspoWViuUgj6TWX-sBh4SMHubSTecHK3ugMYeissoKu3QgbZabg1_Nr8BzkMJ3sq8ZDPwaWrQtJtpJsj05dSwXypANlbQaHaApMMSuu1k5EyJ9qoT22EQcr_uH3maTVjv0WF4XoqddJ-rYGYNQboF2EF6Mqrq86QwtEhHTfF9-ZDq8lhEeXEx5XjfZQZZlzWJqG9RTVvK94nO_0I1mEbG5Bp_a7yVXLhuvf58Af4kY-lYWvZFv-Ut9ajsRLAjf3KsA71_Fg8lfr0g0AhjDbtQyHyfrVUfgswEL-Giq3A1HipLfg6QBSXqc8y3Bg4nPGFVPBxgKqKjRGFoO9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: ایجاد منطقه آزاد در تهران به تسهیل ترخیص کالا کمک می‌کند
🔹
رئیس شورای شهر تهران در واکنش به مطرح شدن ایدهٔ ایجاد منطقهٔ آزاد در تهران گفت: چنین اقدامی می‌تواند در تسهیل ترخیص کالا مؤثر باشد. برای نمونه، در صورت ایجاد این منطقه اتوبوس‌هایی که در گمرک بندرعباس متوقف مانده در تهران ترخیص می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442511" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442510" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQTXJMvA0Sxkfr0nMu__lSr5xMSInmJFj40P3y0AarINq4U7JJeT424jvI1HOnNhGAZgGLsOAjvLnQ5ZrQDy90eX0yYxlAArnQMUqa7Gt-Fo1kTfco6meez8l7-oXdBbqApP-kgMY3Xpf2d1nwZT8KVE6Khhqh1GpWxkIvYoyP98OwA_JdaI3pSFHYJcKysc1D_XpIOK8MHFWJiBQ6vI0fUpBfKdEw1lpVtFLe_klOOAbgDV90LvoXX1a6zC2uZIZLqsNN17GaUUiaWNKJ6wojLS-XZZPuWJb4nPwDBqSBYx2LJzHztG2DhBJfdvsWXrLZ06r5EN5LwAHCaa_uF6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر تمامی اعضای تیم ملی در هواپیما حضور دارند، اما این ۲ عضو تیم ملی همچنان در مراحل نهایی خروج از فرودگاه قرار دارند و تلاش‌ها برای رفع این مشکل ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442509" target="_blank">📅 10:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442508">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAJsOKgaoZBxmqPt9KdDnVWnI5XxoSB0Ot7iFx2dnKAmEi2IKspmaO5HbNerhQWOzU6RtqJxXeMxVzVxGqS2Vai9JJsZu8ZMoDrq9bYGUZzHZ_s1RAhivopIoKa2qA8svm3ZQMXzWdm52EOgjv1LO3GVM4OQEFmBxKW2sx8-8kgL6yino42TXdGQ6Q1hmYItAYolIz8LXTYyNX4p7XhV9l57aFY0S__vQcr0qEmHeiKMoehUpSvuqSpDFmD5cE8Ab_IvUwPt_nsnkiXMvnoeX4iHbsFBu6axFDhV3NJ8MSeFYETqQZTZEojWBwH_Dk3WryCMmHUayB4CkwCarw56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب گزینهٔ اول استقلال
🗣
براساس پیگیری خبرنگار فارس، درحال حاضر سهراب بختیاری‌زاده گزینه اصلی سرمربیگری استقلال در لیگ ۲۶ است.
🗣
قرار است شنبه هفته آینده کمیته فنی جلسه‌ای را با حضور تاجرنیا برگزار کند.  @Sportfars - Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442508" target="_blank">📅 09:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442507">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیدن صدای انفجار در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442507" target="_blank">📅 09:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ8QkNh8MqONc-OoxmkkaRbcJm3a2H9FSRTeqoSme710QFI68qt_OXZV3rBtxJMEEQLRbRPgypHI3OQyRIL3GjIhXN0s-CTZUXQ82U9mQMs2sXBFvSEiwItLLK1wECTF_F2RwzOxCDjRKCpnsgF-AluGeavw_Zi5QnnyckW4EqO3-5svsgvgqtAp7kAUDfTm7bO43nHXFOloQSs0E6InwfpwdWsEzot0FYXlf3QJEIkRUs_9w9WUgIFianCZabPqd6x_7i43u_EMJJfdz1NaQBrBgwENttLpkYJp1Na3yjnPoHnVqJa-eXJOXkAY8Zd2ElsVUc-F9xH-X7nHoobGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک افسر پلیس حین مقابله با قاچاق
🔹
ستوان‌دوم عرفان شکوری از کارکنان انتظامی تالش در جریان دستگیری متهم به قاچاق کالا که دارای چندین فقره سابقهٔ شرارت نیز بود، به شهادت رسید؛ طبق اعلام پلیس مازندران، متهم دستگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442506" target="_blank">📅 09:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxtCGAFWNW_U6DCzKXVv1q4JQXI32EaZSmiQDsIREGcMVX2R38QbcYiScgNka710plYWHFO19jUyd0kgJYxXsQ4bYZP7hMzppIa6Fn-bWru80WspRua2ICsnNRnzxwmxIeubBc6fjojC0aLdq-IgZL4s2tuwGDV7BtEdAzKSbfCApKMVpcXZajTvfyUHGaHFNqbj1Hgjwopw8wrupPjXamallClojFhRq8X3L6Ki-M_6lNEiFMl3a_z3TM0P4vAlFER9PHjz9SV6xh_z-UGJpyb9orpQJ4yhN-NZT5tz16dCdGzD_0Fdf_O0gP_ArR9aIKqFduR9-su2w_w62JO4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سند منطقهٔ آزاد مهران صادر شد
🔹
سازمان ثبت اسناد کشور: سند مالکیت منطقهٔ آزاد تجاری-صنعتی مهران، به‌وسعت ۷ هزار هکتار و در قالب ۷ پلاک اصلی صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442505" target="_blank">📅 09:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZYAAks7Q7r26zBCzAIfwAxWlKRsfPOJ7jmvUEwb0BCNqIpShQXx3hsXYgA2PaxKC7DnCCtPpZMRbfk9jdtBDfPOT-E95MetmANpWCVFunY8u7Za3jhu-x4Iu_1D5eQjLy8ofPLtx10o64yhlzCUDAyAbxAzxncLlrC9NfETnRlek6lOVDsGe6XyvX4HJ4g-WQiq6EwAelItfUAn_WgVSOYreiGx5NPwKZKCr40S5ghTwe4d7DuA07vYEd1znZaSeOtrR04Z3U2Yz6QN7AiaqUmRmkEWh_4CMaB_hoNI4P15heYMFGrAqCGvPMDjZOkD5Qv-7JgK2ARnYYECSLVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با عبور از مرز ۵ میلیون واحد رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442504" target="_blank">📅 09:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
زاکانی: ۱۴ بند تفاهم با نظریهٔ تفسیری مذاکره‌کنندگان و امضای آنان به‌عنوان یک سند در نظام اسلامی است و اعضای شورای‌عالی امنیت ملی به آن رای داده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442503" target="_blank">📅 09:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1areXz022BwyywlA5zzTXQmWCugD_rzPlB6kGu7t5DutKMlQKlrMPwEBzo8JWYEq3EYHqDmuIJ6fP5Bekz-VLkn7SibRZ7niKGlQHBIfBZ9d95zRjX_HfWImN1NwsEuXITp8kwuIedbcq-GFLvuQOep-J8EXENYu-SnRqogOVvAVzMGzt7vbbY4V9AvsFXmYMWWflYYd9sfzGiqvpbCWkj8fHUiN40xRwDwYqFnFi07aWzYhViAyVesH8ixUVhGdzlq91S7zBCHB8n8qX7YFgMhFp_d3V5xa074OR_1uh_gh_uYbk39unpRT2ZESS5qkyqEZ3CvBzrJ_WQl1HvTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌙
ستاد استهلال دفتر رهبر انقلاب: امروز اول ماه محرم‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442502" target="_blank">📅 08:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0379533dc4.mp4?token=Zk_w1Y_M_pwGTBGG-rZd2lONvpeCtfqOOvOt25IPKcB66rE9DRRXqRLzX40tz2Ah3sjVc6af3XtHcVNm0mrjk-abD3dmY2A-_j5lwVXSkym7mrxjZrPdaqdRX0kwtyctMMydBtMEWFpUtEaBXVGfq7utUHgHxzgqfhGORWdLtAYzjWBkoapqg_H1q9tPVVcNE8BtmE7WQ00pvlIkX34mFjoOshS5HJyHlPu4eu-ZI-4i2cQKuJRnhwxDN5tQtgF69OqnnmepVKWl94PWDcILtU75AzJCS2hrANN1exzB1iUKu3HDoCdJBId7Y6Me8vuORNtxQ2RrR3z99cKEVOVjQmpA3_lyCL3BpaWsDJhRTZyqPm7U_tLG0p-Uk1kIxW-xSwmXQmw4K9nD94uKLo_DN21j2sjb796aDZmww_vBq41mE_5o0ajqVWV34V8mlPExBLRoSxkRp5BUzBW-yQdFYq_U_ALK7j7lUttSW1r-rHIox-0Gg4KmxFnu3XTrqd78qXMjuZ5ANKFpCBbBcIY02UvHqJcBk_bvn6wSa4ckgRLLFim1JF2wo2JFJ4niYRc-Q2UZFx94d7wDnkg986TwllEiaVipHACatSaUEe3xMhFjPfysQD4hEN4VpH91zbXejEAE23GMfhcKP9OJLg6FyxqM70kV0jZ-FERIZBGJfjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0379533dc4.mp4?token=Zk_w1Y_M_pwGTBGG-rZd2lONvpeCtfqOOvOt25IPKcB66rE9DRRXqRLzX40tz2Ah3sjVc6af3XtHcVNm0mrjk-abD3dmY2A-_j5lwVXSkym7mrxjZrPdaqdRX0kwtyctMMydBtMEWFpUtEaBXVGfq7utUHgHxzgqfhGORWdLtAYzjWBkoapqg_H1q9tPVVcNE8BtmE7WQ00pvlIkX34mFjoOshS5HJyHlPu4eu-ZI-4i2cQKuJRnhwxDN5tQtgF69OqnnmepVKWl94PWDcILtU75AzJCS2hrANN1exzB1iUKu3HDoCdJBId7Y6Me8vuORNtxQ2RrR3z99cKEVOVjQmpA3_lyCL3BpaWsDJhRTZyqPm7U_tLG0p-Uk1kIxW-xSwmXQmw4K9nD94uKLo_DN21j2sjb796aDZmww_vBq41mE_5o0ajqVWV34V8mlPExBLRoSxkRp5BUzBW-yQdFYq_U_ALK7j7lUttSW1r-rHIox-0Gg4KmxFnu3XTrqd78qXMjuZ5ANKFpCBbBcIY02UvHqJcBk_bvn6wSa4ckgRLLFim1JF2wo2JFJ4niYRc-Q2UZFx94d7wDnkg986TwllEiaVipHACatSaUEe3xMhFjPfysQD4hEN4VpH91zbXejEAE23GMfhcKP9OJLg6FyxqM70kV0jZ-FERIZBGJfjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بازی خوبی کردیم اما از نتیجه راضی نیستم؛ شانس برد داشتیم.
🔹
باید زودتر می‌آمدیم که اجازه ندادند. سازگاری ما هنوز کامل نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442501" target="_blank">📅 08:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همتی به مسکو رفت
🔹
رئیس بانک مرکزی در رأس هیئتی با هدف توسعۀ روابط پولی و بانکی میان ایران و روسیه، صبح امروز عازم مسکو شد.
🔹
این سفر در راستای گسترش همکاری‌های مالی و تقویت تعاملات بانکی میان دو کشور انجام می‌شود و قرار است طی آن، طرفین دربارۀ راهکارهای تسهیل مبادلات پولی، تقویت همکاری میان بانک‌های مرکزی و ایجاد سازوکارهای جدید برای افزایش حجم مبادلات اقتصادی گفت‌وگو کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442500" target="_blank">📅 08:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508119118f.mp4?token=EDwtN7snBHwGXCLXl60hbDWhh1gFyGJzDcqGxGtD9CdqXp59TSEoEb3Bhl2_ImHwgImKm7z3RMXIiu7Y8YcP1PiHP-Fx83cXxNzCpBQF4gC8zbif-tjHSZjG_y7pnBIL-J-2LIVoF1DRQsd90c9tcF15iSCMOzbSGe7jW6_pgrWHQj9Uq12_PtO-rymQz5xgbmdY09d4wrDg31yxEKJvpxYgXjXJt-5PowyBEu6uYHU9xM6Upsv44OPQ2mk2Qqb6Kp8HPpyId5dV0EjRNdIPaU_hPLEJZ2RblW6efsXkU7H7g3Hx019rb_8Un3K_W4Bl4MGV6tVAzH6t8pOQJNit2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508119118f.mp4?token=EDwtN7snBHwGXCLXl60hbDWhh1gFyGJzDcqGxGtD9CdqXp59TSEoEb3Bhl2_ImHwgImKm7z3RMXIiu7Y8YcP1PiHP-Fx83cXxNzCpBQF4gC8zbif-tjHSZjG_y7pnBIL-J-2LIVoF1DRQsd90c9tcF15iSCMOzbSGe7jW6_pgrWHQj9Uq12_PtO-rymQz5xgbmdY09d4wrDg31yxEKJvpxYgXjXJt-5PowyBEu6uYHU9xM6Upsv44OPQ2mk2Qqb6Kp8HPpyId5dV0EjRNdIPaU_hPLEJZ2RblW6efsXkU7H7g3Hx019rb_8Un3K_W4Bl4MGV6tVAzH6t8pOQJNit2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت زنانی که پای آرمان‌هایشان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442499" target="_blank">📅 07:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg4AxkHEiPouEDSP5wQ4S2RZFbW27iv0JTv9wwipmyK1_9mLSiVbCbMYW6v0YFIsUKasZel8tvTiWf8rKIftZYii_gabtI4gCfkrcp2moybd1lcIHsc2QehKKYejBOl6xY-e_4Cszx2kOKsrsTziiXuseMijDXlauwyniILXZULwQxyuCgrqobK2S7ggFAixFvChwTlsQ1o44_lvWa4X0_XSI55n8yKOpwZcb4Zw39xfMsh7lA7JdJVVD9jLJs8miH8nC_hxCZk4Lu8OtzWDBHiib_MLBGHF7ki9diUxRkGBBtBBEdXFzflyUAKapntKBN9rEhrc0C5ixhnmnW2ogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغوش باز «شیرین‌سو» برای ۲۰۰ پرندۀ مسافر
🔹
تالاب شیرین‌سو در شهرستان کبودرآهنگ به‌دنبال بارش‌های زمستان و بهار دوباره آبگیری شد و جان تازه‌ای گرفت.
🔹
به لطف باران، بیش از ۲۰۰ پرندۀ مهاجر آبزی و کنارآبزی به این تالاب ۴۳ هکتاری بازگشته‌اند. حضور این پرندگان نشان‌دهنده بهبود شرایط زیست‌محیطی و افزایش ظرفیت زیستی این زیستگاه طبیعی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442498" target="_blank">📅 07:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f9ddb167.mp4?token=bHv-UDRBSzED6o3_s-iNYH-VDbrtEqIAqKRI_z0uNyCED6wco4kxN7VHfXlB7cM8f-9Bn29C6phNRTMWt9KDFCwFy3TP_SBBImYie_Jm33GionXNNEk7UmMhO7mA2Son07UU4bq6GdMAN24qBRguI5JZDSMgG1VoiJ9wsrRqdZkfSBY07a_MIbzSOWyE5hdrYPTgXLWRD_hXAPAOLjigTxCmqkNQvGQmlFC-5hNahJihYcsu74VEIxemBc8H8SIcXzIN1Rbkh9jHC0TCFJMNxDImdPPIdkYStFbNWHgaNn_O3dCh0Es8Pu7Q0x7oWbcU6dQLXJgjrC-935DL7GpzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f9ddb167.mp4?token=bHv-UDRBSzED6o3_s-iNYH-VDbrtEqIAqKRI_z0uNyCED6wco4kxN7VHfXlB7cM8f-9Bn29C6phNRTMWt9KDFCwFy3TP_SBBImYie_Jm33GionXNNEk7UmMhO7mA2Son07UU4bq6GdMAN24qBRguI5JZDSMgG1VoiJ9wsrRqdZkfSBY07a_MIbzSOWyE5hdrYPTgXLWRD_hXAPAOLjigTxCmqkNQvGQmlFC-5hNahJihYcsu74VEIxemBc8H8SIcXzIN1Rbkh9jHC0TCFJMNxDImdPPIdkYStFbNWHgaNn_O3dCh0Es8Pu7Q0x7oWbcU6dQLXJgjrC-935DL7GpzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442497" target="_blank">📅 07:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abq_CVJZaP8WB-lmCNZuzZM1tmJDd1vOT35GcVTrw8_pDaPru5GaXN3pohy4f2hV79499SZ83PrCvX-uf0t9158IeUEV0ybb7iI9WPf1lzG5ac1IR_ll33jnkUgAe5J6gkUif5dofNIZHmcC8yDPJOE0n9Z__puT4SaLrkFcondS91ypC_QoWHfPU91szltjbnoHC4yAXllcLHY94mqOy6gXwxP2iKz1oWD6RYyLb_inMgyocA69zXTifnkNAqDTSwvmWurCIk3_mimUORzyC2-UGlyYO53I_wvKb-Fs-jjCkiuAmqXIuMMWwSukPIB0UWH7PmKT2zcB-OVYhleYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس داوری فارس: داور در اعلام خطای مهاجم ایران اشتباه کرد
🔹
حیدر سلمانی: در دقیقۀ ۶۷، داور به اشتباه خطای مهاجم ایران را روی دروازه‌بان نیوزلند اعلام کرد؛ دروازه‌بان با مدافع خودشان برخورد داشت.
🔗
شرح کامل تحلیل قضاوت داور بازی ایران و نیوزیلند را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442496" target="_blank">📅 07:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442495" target="_blank">📅 07:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627745dd75.mp4?token=np4l7tA7odNnuQ1YJj4UrQtbwwwkqdp62UsJLRvlymxinMlpqQfKxXVJvle1OCh0lzvcOR_zdxWYQkonHgahGRRWU_N2g_9iW7B_zu4kRHtv7od1hr0sQ6-rqeopo6AgB0M7Sr_Jn6dqOVOflLLURUjiHRHGBBnZBq6liwVsoBtZqSRbRKjFVcpzEz01UMa1YuoXvND8WLIb3wkEKCKDzJ_fhDibOJPXI0f3SIEaQEDEWKeU9fdYWjYn3KrUuODwiJacCy8zs1Cw4PuK-Rka8L3azEnmZFoPTkA2Zq81Rg131oPq5OPri9oIkOXbxCkcQgkDSI0qEDb8fNDEVz--UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627745dd75.mp4?token=np4l7tA7odNnuQ1YJj4UrQtbwwwkqdp62UsJLRvlymxinMlpqQfKxXVJvle1OCh0lzvcOR_zdxWYQkonHgahGRRWU_N2g_9iW7B_zu4kRHtv7od1hr0sQ6-rqeopo6AgB0M7Sr_Jn6dqOVOflLLURUjiHRHGBBnZBq6liwVsoBtZqSRbRKjFVcpzEz01UMa1YuoXvND8WLIb3wkEKCKDzJ_fhDibOJPXI0f3SIEaQEDEWKeU9fdYWjYn3KrUuODwiJacCy8zs1Cw4PuK-Rka8L3azEnmZFoPTkA2Zq81Rg131oPq5OPri9oIkOXbxCkcQgkDSI0qEDb8fNDEVz--UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بازی خوبی کردیم اما از نتیجه راضی نیستم؛ شانس برد داشتیم.
🔹
باید زودتر می‌آمدیم که اجازه ندادند. سازگاری ما هنوز کامل نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442494" target="_blank">📅 07:02 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
