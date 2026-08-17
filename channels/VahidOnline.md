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
<img src="https://cdn1.telesco.pe/file/sywDNrL6S9gUTJYwSa9-M2laZ53ARyly2GP64RG8p7VhY1o7pZCXRNyUNFL0I5qW78w9C3aAJcpkbd-zH8kOoyfJZKOsVtDaGvcyWe6RjJ8iYQaBxyhZ5F7Uu23NLt-_nLmpsX47g_CYjX87-I3jR_RPa4pqNF6LYs72FRl-1uroRbqSWEvUOcgk6EYXpT7Mz0lwLeZPGMctJoV0fDZmgvI0UBstvrkxKAEKSac0FD73wdDqxg824Gi8kda9RJQo1_FWcqokOLagXQD2w_MVsGyI8ZD20IeYhmPKIkUX_a-By10xIka4JV3tMxoHKsXsdIrXtts65WVJQakq4UAJ0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 20:22:01</div>
<hr>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hXinTtXryNQo3srah6pCW3FzdMz3DdrIrF2Sk-4FF8mXuyKVVa3LgrbxNIDlu1Fep6YmqtcYpDZl4El1lxOvdvrP1_B5VKbKds3zANfumfuliQLm_bGEuhEwBE9J2m7LitS5AYX4M7jzFepj-46FshnudLxvTC-aFc28Mea822apE62mQ8afIcaqRQpTb4cBRP_0jmKNZTSRFGpHpQ2nDhYRtEDPVRPayzyLTFY9hAyvfmBCURtVSX6Ct38JjkxQ3PJhuUXgNY2fh_5qJOzGUlPFALjMyrjvdclXUABy9sE22l5kwynnfipAUe85AIV6fJFsW_-6eioGWXfpap0tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TNlJFsU-6BrrL4nDWGUtb92QqgWqDn2O36PrbNFHww9eACABSOTcFRAgc1fC_0sC_JdJUeCh2wuisloH4V_PcFKqsL8IdjrAhmoQ_JiNuiRKzw5g5RptR645HbjdczcZDcGfLRfHEBMeGtjStWPHQXL5Cy9xhAyDn-g18ZntQTchnh4ZEgMJFJwGnEau59ZZZ7mjIXXGEIisdT_v3lInpvzUhLYHUS6Kjh9gIoKSKLjsfCcsGEHDopfhW3fk3LvA42Q27LkNHUIvNFPSyxgTRzkosc202kAeI0RFJNeZhGCP1-jFCKUaRmwGWMrTCEcQiMdBF6BWGT0kGTZkzcw9Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V84MdaHraWOb8K0Fhk1VW3XHW89y67OSDskcAlfKZ43OWReNfPgmrSjWl8_YXevDSnkORhObR2EjmJGgY01iUSj-Aezo6olrw6xfwuMrrxyVPVhQ1kaB-GhVfB6aysoC37ZPb8zEpnk_plglcWwpRbUX7PlfJGV0keuCOUUOWykcvlnvlECs5k_M30EiLuHDuurHpR-vWytJEn7RPtcYfZ3TUUJg382bwC5SrLJ8X0K3zQl6tiWNXjcDomOySYqbItt0r2di4eSTNFtTTLHA4KlzCVbpEpaU1lDirHusM1guEYU1S3CbITCHD0Jnn1bNc5qKEGJ-mR8-ShgyTLrPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=WSv6QGoeTOm3lJQiqIIwyr2kGB_8n6tWpddLjkXKN036m2iRclmjSLZQuEStVqHLSXd5NhTxaP52Sc7Ys0gn5wchWj8drtcQVaaE8wI60ctIL3B-NBmW58QQIJsNP37vQzam6A4OgKhdYDz2sIjD8xSIPakqVjDLSzh-iZ-Vmh-id8EJhy2Bla2IDCzZjeFMDSQkAfdXxxJpFKfvJ0MSOvMPOtqiQ5he4vToSsD_dk6ov8goU0UHOVr9AiqLKWYo5-h3t2w1l16pW-c0jj19bUIWveQlnQ7LCBVaUBlLeLTdgepCRko9fExBfCSuvMf9d53VE8iub8aCZjCXNMISew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=WSv6QGoeTOm3lJQiqIIwyr2kGB_8n6tWpddLjkXKN036m2iRclmjSLZQuEStVqHLSXd5NhTxaP52Sc7Ys0gn5wchWj8drtcQVaaE8wI60ctIL3B-NBmW58QQIJsNP37vQzam6A4OgKhdYDz2sIjD8xSIPakqVjDLSzh-iZ-Vmh-id8EJhy2Bla2IDCzZjeFMDSQkAfdXxxJpFKfvJ0MSOvMPOtqiQ5he4vToSsD_dk6ov8goU0UHOVr9AiqLKWYo5-h3t2w1l16pW-c0jj19bUIWveQlnQ7LCBVaUBlLeLTdgepCRko9fExBfCSuvMf9d53VE8iub8aCZjCXNMISew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bTAx1z_IdMIcoTqlUZ4WhmZcdbnru0_gLAjwGRIiNo9GV3zSHTsXKvp1arvV-gejwElM8RyhFC0DJcOiJjjVXWNgzI8_dYA2EkFVHL1kaMUYOqeDAgRp09EPR8_qjrlYORt4X6alu3SgMUJ1ARQ82Lp8scUbzWPfT6Iz0pwhAUSOQ8-q7YsB5rLP6kLcNUhCkpz5w7VPT-eCzuSVfUUynbs-d-sGZ-4hXL9y0-i94kyVQImWwQn-IjSjJn_z7-FVrTrzw9zJi-YCBqTPcUequzykIuMNrB8EYQ8RI8wOqBh7ubYemruhNP3MF1BE8-hAKxJFIJOPIluZhxiTs2BDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1FyBKh9PtcBlIByyfQgg1ZUlzxeguVjiCzh23IVybykZlSAEu6fS8eFv6XmRynBaAaNVkGemZbHZkyJDEW0j6OqgPkPtI8b757ZX2x8oh7jlx8ZHwB7I-oCeEYBJmfnnViucDLFONw7zFCHTbdx8yuh6ChJ66zaj6iEnNIKMhTAN2Pdsl4qvrtRzeH6lR_7iJPpqnl-ksTD-bSA9BJ_XrlPVonWnzCoZVq9PThbypmA1NGTYSYZrXZ_cetF8iFiTrRZGJv1M4RQx5MnODwU3_MkK7q-1K25TxwYt-kDkBOIGJ2AS-0Lp6s4v2F9cz0SK3lzUPFSyY3s33p4B1PNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ملیکا همت‌زاده»، دختر ۱۳ ساله اهل روستای دسک شهرستان نیکشهر، پس از عقرب‌گزیدگی و در شرایطی که به گفته پدرش امکانات و داروی مورد نیاز برای درمان او در دسترس نبود، در بیمارستان نیکشهر  استان سیستان و بلوچستان جان باخت.
پدر ملیکا روایت کرده است: «فقط یک خانم دکتر آمد و گفت سرم می‌زنم و پس از تمام شدن سرم، او را به بیمارستان نیکشهر که مجهزتر است ببرید.»
با وجود وضعیت او، مرکز درمانی بنت آمبولانس نداشت و خانواده با خودروی شخصی مسیر ۷۵ کیلومتری تا نیکشهر را طی کردند و ساعت ۳:۳۰ عصر به بیمارستان رسیدند.
سعید همت‌زاده درباره ساعات بعدی گفته است بیمارستان نیکشهر نیز به دخترش سرم وصل کرد، اما پلاکت خون در اختیار نداشت.
بیمارستان چابهار نیز پلاکت نداشت و قرار شد آن را از ایرانشهر تهیه کنند: گفتند یکی دو ساعت طول می‌کشد. یکی دو ساعت شد پنج ساعت اما پلاکت به دست ما نرسید. تا ساعت ۱۰ شب منتظر ماندیم، اما به جز همان سرم، هیچ خدمات درمانی دیگری ارائه نشد.
ملیکا همت‌زاده سرانجام در اواسط شب بر اثر تاثیر سم عقرب دچار تشنج شد و جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=tprB1MXrJcS5ZFvsXXE7nJjBSe_Gjh7Bss8epEZpweVn99BLBfina8mlxJHNT66X-WzwQp67HKbyz5qxXcAVkKNTu2t_8IaqFXLH_DsgbVG5azcVGNvjJSfZLqv_etxJCuMUE7yEH5TUM071e9sxsJqNTtI5pNRG4fV6WzgdRTc4Msk_sx9tHx34hWLjEyzlpA4s4FZoJUVYiVp3ajfBHEWRkOhGH2Keb-RgQc8IceETHlITM8ImX2YcSJGhM-ayR1l9mpp-_g-oPmYV6SQimJDKrXaGN_L3C428EkdNdxnk0pGOK5dK2bQRbsId2oJ5RV0UAvwmSCg2S6NPDDePhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=tprB1MXrJcS5ZFvsXXE7nJjBSe_Gjh7Bss8epEZpweVn99BLBfina8mlxJHNT66X-WzwQp67HKbyz5qxXcAVkKNTu2t_8IaqFXLH_DsgbVG5azcVGNvjJSfZLqv_etxJCuMUE7yEH5TUM071e9sxsJqNTtI5pNRG4fV6WzgdRTc4Msk_sx9tHx34hWLjEyzlpA4s4FZoJUVYiVp3ajfBHEWRkOhGH2Keb-RgQc8IceETHlITM8ImX2YcSJGhM-ayR1l9mpp-_g-oPmYV6SQimJDKrXaGN_L3C428EkdNdxnk0pGOK5dK2bQRbsId2oJ5RV0UAvwmSCg2S6NPDDePhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=ihvYV_wUReyqeOU44pa-kh8Fr3driI2OrRg7ucapgXwFQXN2sl7DLhai2bT8mn3Jz8mjFDfTdv6BrIoOdcUtT5uwVKFMQlOLcb1HKXGnfp6WyuWzu1JQnNNBg2X3FoLRPrC0wKAmTeY2iKa74Zr4ftAeFWWKUzuwwaxWtvJvA5Qrg65VvNKgAF-z75HiHWuBqikn6EaNBQ0OPEkSIq6RwwLUENM0KPugLOk75z0ARbhhHF6OHEtgaOtPaUqcD4OXs4FgNZPOlPOBWpPARktVBAcp4Xrfykph_gELBuTNFFGFB1xawXKS_ZG8K66ctwOAnuawi8xrKibE20UvAonYKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=ihvYV_wUReyqeOU44pa-kh8Fr3driI2OrRg7ucapgXwFQXN2sl7DLhai2bT8mn3Jz8mjFDfTdv6BrIoOdcUtT5uwVKFMQlOLcb1HKXGnfp6WyuWzu1JQnNNBg2X3FoLRPrC0wKAmTeY2iKa74Zr4ftAeFWWKUzuwwaxWtvJvA5Qrg65VvNKgAF-z75HiHWuBqikn6EaNBQ0OPEkSIq6RwwLUENM0KPugLOk75z0ARbhhHF6OHEtgaOtPaUqcD4OXs4FgNZPOlPOBWpPARktVBAcp4Xrfykph_gELBuTNFFGFB1xawXKS_ZG8K66ctwOAnuawi8xrKibE20UvAonYKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر قالیباف تفاهم‌نامه میان ایران و آمریکا را «سند افتخار و پیروزی در عرصه دیپلماسی» توصیف کرد و تاکید کرد که ایالات متحده و اسرائیل در جنگ اخیر «به هیچ یک از اهداف خود دست نیافته‌اند» و تهران پیروز شده است.
قالیباف که در جلسه‌ای به مناسبت روز خبرنگار [در تقویم جمهوری اسلامی] صحبت می‌کرد گفت: «با تمام وجود اعلام می‌کنم که ما در این جنگ پیروز شدیم.»
او افزود: «در جنگی ناعادلانه به رهبری ایالات متحده و اسرائیل، ملت ما با قلبی باز و بدون انتظار هیچ چیز در ازای آن، شجاعانه ایستاد و جنگید.»
اظهارات قالیباف در حالی مطرح می‌شود که او جزئیاتی در مورد اهدافی که معتقد است واشنگتن و اورشلیم در دستیابی به آنها شکست خورده‌اند، ارائه نکرد.
@
VahidHeadline
قالیباف: ما نتوانستیم آن‌طور که باید این پیروزی بزرگ را روایت کنیم تا حس افتخار در ذهن و وجود همه مردم، جبهه مقاومت و آزادی‌خواهان دنیا شکل بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=BzukPfp7iQwho6YLy4_UovJeXFD_Vy8BB7hGXKPEQLo7pIJfeCjqi7HbtdqoYSvuvLJS5rHQJ_B7hlgncfdv_gGhdoRBnACPujUqyMcKCmdwLFwSolie6bfL8hzViU0b1mcaFKfotkkF7bbqY8VRYtmPj4O0lw-qZi2HwI1AEwPka83ev27DiEO5k3RxWPFIeg5zqXiGvxVvGM5adK0sz4mOQB6bCl4CCVMXylnmU9J0PKWMe2zfqxDI9mOP2ikvGV8qj09tjNugSb1ebpcJlL7F8Clg12Kgj0Swv_RBTKYcspUmhg6hNUGt2hZUr31KybbfEojN_5-DKArKZO_GLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=BzukPfp7iQwho6YLy4_UovJeXFD_Vy8BB7hGXKPEQLo7pIJfeCjqi7HbtdqoYSvuvLJS5rHQJ_B7hlgncfdv_gGhdoRBnACPujUqyMcKCmdwLFwSolie6bfL8hzViU0b1mcaFKfotkkF7bbqY8VRYtmPj4O0lw-qZi2HwI1AEwPka83ev27DiEO5k3RxWPFIeg5zqXiGvxVvGM5adK0sz4mOQB6bCl4CCVMXylnmU9J0PKWMe2zfqxDI9mOP2ikvGV8qj09tjNugSb1ebpcJlL7F8Clg12Kgj0Swv_RBTKYcspUmhg6hNUGt2hZUr31KybbfEojN_5-DKArKZO_GLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inC3xf_cYQgvamQ9a-6oZTOlcbhp1EkqZ7wFHJ8re7YcQBukgoXm6BfHN8zv8I7TMIoLtRhH10FAB7GJJ1dSoxO6eUrGldzmGYELCTAptCQCyc8VlJVA0hIwuKZDJaLmYve430s5FDRIET6vuZaP3l9kSkoTpzfgM0iKjyGKRo4uE5wf87QI9ab8ul1eLQfnUDnaxaGR-KBj8P-wiCKmmKlT5SJT4zluVEVMxNlslqGKDOmZmxlWmwkCM3-DsJj68e7O-MgT8RlA0NokVJGgFPWIYNNkRnzCkAyPZJ9shZlrGZqGq_pkG7xR7mgRoJQelvJNb67BE0zq_kT5p5OlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmC-1zodDGRDnd4ZM9ZpeNh7m9geUlAijDqM4SSydKlNn1PUOfE1yWW-axtrSBV0LxrpWkfyp7PvFwlnskxdeV3waPlk7iItwtO6pPAPqnG_lSAYDy1Pvpxh-gkgQg0cGXrydf6ZSH4gRiOY83uuAm762mCwDQRUYhivA-gzf4UgkYIzkGdJEWEd9mBN2MVYpyEp_W61uuzk9FMZcteKLdya5oWS0qLSLDwSh1NYOoVEP0hFOrtTiriyhGborkKSL3t78mT6L5Tuxs8NCoJ-j9kLgreRNMuzoYWhuzxEx0Bg8VAyet2XYacicpUUg7nsvNp5ygMOZYRYwf3NKb2bsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_7TJfZmf_RhRhsd9q-DLGLbpMp934L4NK7zPXCdDjemc-Ya8FVQicddDlts_0WQwaDrYv1kaC0r8Z7habCOYoIRBU-GoFtDxB6sCHK1GxHuEdTzIT9rq4dX5bdqRLZ2hVRoS7vxAqYA9wayqS6z3qlLm0fFVCRGolHVS3gy-WXfzdzJnaGtlHo0DOPfcqz2OiyhVcLW2lEMNF9bJhM8TTgJzynYaT1BiaiA8TvM58ciJSg1yMGNh0J96itcq-UNDtuZFLCWwL9xcYljg1e7whOnwMP_-Lw1WEw_1qcbECMllx98yJjmoo7VCSafvun2JwhJ4f_8TsNcDBMB0jewFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9Nji01d6vTF8O1ghCD3LpzUC9b7Xy2hWK_2QbhdtIL7YKJD_pSaV3sVTYQu5dsLAOHuryjd4M_qYrdIY1EJSrjcVvXvHNpT1xtdJ5cxnT0L_kH3QyZ49IDDFyZRWw0wZRSTGp97GkoCGGbEekQlmUn0AtKd_exJTrgGNnvWEqn6Z9Gm44aV7kuEUTTiZJWJrTUNNtB_25PXa2YdSiAOnj6Oc_3I1x3dlU9auz9dBpl3SKUqpH-Mx36vgyXQl0Pd2J34JZAaFC1g29yO-VDK-oLsAjNaWXEDCZUQfTBVLM1aBbBi1kGEH0ICQ0s3QZioWr2mF7Ae0J2y0fcwBHQ7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-Zx0pEUlZe6WfI2028kf5XDCRHrtE6BpPh0aS_GOvHuuAu9VmJDG0xqmWgaiBCfQxnTy6K0ip2b-hUAtB1P4Qw7zB5rre75gVUCrBtl7SL-sD7eqQ9JVhjKAQv1gYomsyZCpyp1JAgfcpAFt6JYcfOJjvFQ1GmhscBFVEdzhwrFFcypK5jkMueQgeehad8DHJMkMvMRfGUlDc4NglyYNTQFJsIo00zj7dQiTrjOzTXUVFy1ajZVwrmoXSwMZ9stl63gbHAtwJqKcB_2TVUE0gWXJ2JGYagk1vImsd65LIT0XuXOgFnl1_D9VhD0HNcRNOPu7D-FgCnp8PgHuZ_UIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETp0M0WzreB2R_qFbyr8WHmawfLh_Qnw7SufqMbQcX9f5EH-iovQRTOw6OP8uJpIrmrIjtaef_5nGoB5ebfRAzPlBo77jWEf05OutBM8cmb-xU7PSu8Yguk-jxYuhbkQb-VizJTCdvnrnWaEzJaDll5NP-ct5RMKYMuu4aQV0E0qBxngaExykuRH9TN8OrcDSu-QXOBvisVdMrwBjBXoEqZ40uRgWwLvwdav1paspa4Yc7Rvh10Jdqvu7SXEcadiaCdapZqwSSZy5v_hDIJ8utPrIQDAuH7tR9nCaJOX6v9orhJYU6HM5Z60abWEEAj6KrNbF8GZmT18YbG6YK703Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg_ELP1dvg-MdbqWC70LwkVtocXCcYtWfHusJJGKLr3cn86cGQjadDQUNpU524lEMRMxFRgfO2-1TAaCAXAeoNpE6_1kdlAP6yvXYJUg5RiPV0soKoonUP726RFYiQaKiGxDrnleyhsHAZlEOKnC7VdCEexoPMAV-fWgfn1C-kaAfMbGXMbYT5k5tldDXQQ_lDKNq0ZjGfd-OaeSgqRT-hkYyGWKp_TMS-S0SVqNYkGjWIsnuL-1iBZ9oXeVWme5zo4wUpI_W7GcnIGRvQadCju9ULjqUAZINV4WMCjOBGKCKEzEsf8zapm6pQ82rCGs-V85LADaw7JZUzlFdDnarQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=eaKcJvnqpW4SRMli87SHl9twfu7TTjPYO2pjKcMpxod1b0uGDDO4r4wtvKUocDhdbysqkpYQpYR5D-6nkTBY93okKp10N-LG7HCTNIvdDD7V93M9maknY4DhzfC5faBPt2g-nQmgAJ1YrxCkI8_C1_VeqVTyIV6Jzi21ZL5uh_MnBnNUvxMDQ_55mG33uMqj0CKitl4JTUcwcM5AcHj4EhwMNmQqiFGpjjTglNg1l2lERbId0gK1u_tmXPjl86HYHsuX06l2lzbfnzsS0FB2k9gm52ga0-X64pQnSM00KLT2972Uh6El5WnQHQjrGFx6V-uUbMZiaYX6xgMW9sfG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=eaKcJvnqpW4SRMli87SHl9twfu7TTjPYO2pjKcMpxod1b0uGDDO4r4wtvKUocDhdbysqkpYQpYR5D-6nkTBY93okKp10N-LG7HCTNIvdDD7V93M9maknY4DhzfC5faBPt2g-nQmgAJ1YrxCkI8_C1_VeqVTyIV6Jzi21ZL5uh_MnBnNUvxMDQ_55mG33uMqj0CKitl4JTUcwcM5AcHj4EhwMNmQqiFGpjjTglNg1l2lERbId0gK1u_tmXPjl86HYHsuX06l2lzbfnzsS0FB2k9gm52ga0-X64pQnSM00KLT2972Uh6El5WnQHQjrGFx6V-uUbMZiaYX6xgMW9sfG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6VTyulJMENeLplDNYL8IrOssTZqtTwc1P0tqi-8b4tuIZH7jc01LQdL0nVSDo9MTQZcIa8whZTFMZ75CZgbKqJrUzCbz13BLqcMv3c-xnagEr_5dOohMeazwQOSGsu-4YcNdh5mgqa0g8PMVqywXOv8zb6-HZJcyVP_tO0CbK1kD04i44Xkc9HVzxMVdZumG65jmp553q57TiI5xSawbPAmSIC2rhqpzFjDZwRmaLzgBBurbZmSuvM1HB2jWOVF9G9Lg3Bk0M7--7uhW54TiaCi49gupN1sPPEa6GR5blBn_y8GYp3O6UFQ6FO8OY7vNruVXt-w5jeq_hllwW5nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQgUt3aP6QdpoTBdfrWyVjSNG_2wlMP5RBf42gsR1Z2PrkJln3-WyqWpoFlSdQQoOCeCn8rcAQXJM91Agruo9MTJyEAWTCg4H3YqG8zr-ttl17UjMm8EH3NsAKZeP2J53ahQPlJJo7fYbMMfWD57t3SkgUdbMJXFwTVl_4Zgit-xxJOfk7Z2DqFNCK-nTinbU_FpwTMLWRW-VFjg5Gpm3wIbE0PFRt9bi62d0myLp9AX3k1qUUYgZoA5KzR5uNFoOo147PcL6ZmUhS6usJFg6nOt2oItB3nwYcCGIP8u4MWJX6Zfp9BjxAs7ni1G1kSWL6Qltb6XympOR6_LEJr81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccMfemrNIQMYWHFEHMnaSV95DQgButyKQmL4Injd223eHDP1soeIA0zb7rzfmipRgouMxE1yOPfLmlQufohpgPVo2jxqN7IbZdhBl20vs-Fpj94PyycnUsxapdd3xcBKx5ZZ6YjBe6lJUooOsPzKrUFyM0qLBywMf4TunrbINZRTffRxVxS9RpxnBQLuauhD1reKn5X8kSLp36pOFvgmpXa_-BU5JWdMxlneoJ8Mr7xu9FLIIfFJDWQ0qGy9NdVVJVm6s8jLplNy-xm-GNjiRgQbcgDYXCWPVRIq3CTjrBigfYE-ZgkbY9q69q6P6Q1TZUc7pItYfdXftQew7xkZkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=ThHxQeB9QCeE51YgwEaNS25JOXEfFy3pv3EgsEhIY97_Ei2Ku1KTNeizE2kUmbpDK3djnTV6oPgIC643RbdbVpuIj4E3puFyCavdikmo6Z_mC28yOnK_eBidadn1DPcLw9GGvRqADZCKj0xPcbB5V2EDPbXu9f9F0PZpEnK_Jyj2XHxnw_Rb9E-smv-uoR3se2IXcSFWOF6W7GCdxvn9k7qcPp-9923v1xinkfW97Kaxu0RqQivbdTWvkxENj449qWHZd0U0GcsVNtSlx-TF26TwfdklMlmVSYde24u5a4DMkGDcySea27N8PKGdZujKgSccdQ3vXhIUIuR94lwkrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=ThHxQeB9QCeE51YgwEaNS25JOXEfFy3pv3EgsEhIY97_Ei2Ku1KTNeizE2kUmbpDK3djnTV6oPgIC643RbdbVpuIj4E3puFyCavdikmo6Z_mC28yOnK_eBidadn1DPcLw9GGvRqADZCKj0xPcbB5V2EDPbXu9f9F0PZpEnK_Jyj2XHxnw_Rb9E-smv-uoR3se2IXcSFWOF6W7GCdxvn9k7qcPp-9923v1xinkfW97Kaxu0RqQivbdTWvkxENj449qWHZd0U0GcsVNtSlx-TF26TwfdklMlmVSYde24u5a4DMkGDcySea27N8PKGdZujKgSccdQ3vXhIUIuR94lwkrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pXjqfmtjT5Ce838Dn_MZ5yAlm7Wduo-uUnmQxAfw9u5wsT_Rry3qCmx0SPgv-3pU3DJz7uE6Pi5QM6Iz6n3mhEr1Wer6W-QqZDG1twoXb_QRbdhxwvWFhJ2opl-FEwkerGwjiSe-oNZflxEhlBlLUeRZcd4MJ-jl8uqjb-xewS0Um5oVXK_90B0gbEBj6w-NEUZrRAtkLvzSufKcupF-4itq_4xmc3GGzzAJWZgOmeUWgKWyz8BNOGIFi3mFIVdezpFvLuZkuKNN5h7GRiXh8ikCXHfsLuDfbXOwnBk4BRS0ynHsovQJXfOVtJ7KLrXqtGW9g3zmaVmvhN9jchOorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AidBA_CKCMmixX6KvCh38Z9aS1scvMAsIQzsuAv6cro6f1SbUXknaxlFHyLoXu3E4BMIqpX9vXjwLHoKA_O039daYtXwxrHqIMgVr7PkVcIbVo9-G-gX-1hMzHvB5rzfjzq3DGIZPCNDT-VwXkL3p8ySokBPzx1os6rq1y5MjNzwhCgH6ZVGSqG_vfZO6gpaa5PBW2P08yeqAX66M0jlzKzLTFWz-J4RyGbkorswAoWNvTDfnfnlOHyiL2ZG8cCr4GLVkpMO3GHRgO76YHeC_eX41MT-BvTuXvAkuxhxWJZzYgSXac8nIKNtOaCXXN09mdF5Ow_ij3fbQlqSNUvkdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RVZunxCIYMrRpa1ICrRnZM5QuqWeWUdNcnVKSl69_khUsBRmfy28rQIwnyTCndvPPEC94Tl_TQR3rSG9pJIkKsS8zeldnMcWGSuBadqMzTU_N_IUiCiBWFLRu-veVvxHQ3gJSnLXO3oORQxA0-RbB1RD7MQ0zZbdpSbEFbB8ne7ox17gf7sF3pUtjekdB0ORmWEbh5gcgpmYwi_sCmh8b7K3aJXJxXx2RjLQtfcuiekm9Hgz45hnn51znxCJN4HRJtVhfO11bjYYIx-7lTOXzD1LXj5m7dBLt9d5_Q2PxRzEHWCvWHbIeN8CUhjw_AmPAlPjgIsPS_m2mUyw2WrFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uc2tIDBzTsElJm6d7h70xMTlVrUNl7rYHvLK7eLyZTAocGzMyIHZPiZipfyFNDTl9J17EEY1AAmzbUQp4OMOPVzp4S302deMToivTprg069kkEWRREMlJldJZQyVIxyQFqQIsbbhRVt6_7V7D23_RlICBZM-WqhiDoznTsLoDu3rz4c5Sse_RqFYJPeWPmDiM6xZpvACsWZ0etV0v6AKHkjqiXZWgp42cUmnNSpz2ReSX3Ykqu4YdOmZIxNWGs3X3L60tk3W8VZM_ljY2Q1E97WoKNQCLopdhovaYQT3j1qq2-aFVa6VabUka1dF87TszUvyGfMCz_PZSAp8iYTL7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=EAMrknUc24UHlHX7f8nwAZMR7fNE8_OUvMhC0bz7lnuYycg7puejKRIE7ERb-EVgWmOQqAaCOzHG6kR5arHNf7T8TJ15NahFZVTRhdQpVnvM2E62gkkE68RAqhVNrKyjVBes8IP2ajyXdyHfkNHv_XdqxD3v6poJ2P8yP3P_Tn2pLunbDGaq-C-HFpRF_9GgX82-Yo0vZ_LRHPoYfM8UPHjP5aSaP6W1Udxhs-ZDP_JxDOhkZdoaXGHd17_ijthZRKMbbrH4TdTfq2p-HssFL8i5oVJshEwcgq8JAF_NSeFvXS7DU0Pjrb9yTvduhm3BPBpw9SiMx4-99Da9LCeIrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=EAMrknUc24UHlHX7f8nwAZMR7fNE8_OUvMhC0bz7lnuYycg7puejKRIE7ERb-EVgWmOQqAaCOzHG6kR5arHNf7T8TJ15NahFZVTRhdQpVnvM2E62gkkE68RAqhVNrKyjVBes8IP2ajyXdyHfkNHv_XdqxD3v6poJ2P8yP3P_Tn2pLunbDGaq-C-HFpRF_9GgX82-Yo0vZ_LRHPoYfM8UPHjP5aSaP6W1Udxhs-ZDP_JxDOhkZdoaXGHd17_ijthZRKMbbrH4TdTfq2p-HssFL8i5oVJshEwcgq8JAF_NSeFvXS7DU0Pjrb9yTvduhm3BPBpw9SiMx4-99Da9LCeIrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TuuEI-v65UzvgPdixO-hpNdvZX00albjuTK0DYjoIUft-HlEmPDBJNTR0iH7CIAEMjnpImIvdRWjfAQNLrs_92IDFAsdTcFPkEgAwoQlmLbj8Th5MTP48nd3j5kgZZvi9Oij3EMGP1BxRN7N3qtiFT9MzImUoGrag2HJMVcMNO4Ml5VrUeA66iRF9k3oNe894KEBBW1xDSGT-1YX2PLk4XoNOHF_gI7FMsWiBYOZ7jzLE7Qa9JaMU_Z-UhuQTTlTfNGJqqAiumuTtjoXIQ4oTuZSikgsIYNn_nD1-MS_1Yn5X7yv9BS8KLdhSEpO4q_TedIBlm1UQnWvt_RjcB6iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r1VldPIa8VXPwIft0eFbATCU1RvtjkZBEAEu3nHj7v7cixQGkJZ_a6VEAPh4M_MECzW5zkP1qghIRYvmCT-4YwB4m7zZ6rBkKsoJlJHpRTzD6ujdESQqRsA96NsHJ2GC6t6i5bUQCHuvbFRFSM4G-y1wwMRb9CBk9hi5pIY-Uj2ZAIWSxDkS2chFPB2h8Ik0uOemwsnpBt392h1XCTHTDO_Bvy9OZP2jZsP2EZ2Rh3Mr9QmeCkGS3c7JJqJtAwfSGJ-6p0UUtAsG-8cmJns7xxmzqn3dGciHBDkvi_gQZqReoKUDm0POCrEIvayT8bnKV8Y7uY8t_ENRxpiI7je9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bFp_whSkAYT9mEvwHqyJGkAkpVRM4Q4YHJ-Qy4NMepbPS1DVAkKM2wPd8cuq6y4bcBZeOMZaimb5PjGHJulB5wMIaKppHuDCNg8wXlH7_KLppB8iDZL1Qkas1_GK1kKmgyBddhIbdSjvoqe-U6N1DtmiDlmtLVwLMp134u3njAgwtmvk0sQ1li16bngTgMbObS7q9SOqL-dEKnjQWpaUQiys0uxq59GOzlmRA44QGlzG0PETwNH-2MyxZHrbYl1BW_KADVK9JJIDoUUg8OgovQwqUXppnkGIaqmsGWaR4HGhKBKeRkKvRGgMnHyDMUCbdy6InbiQMALtHJP7oB8l4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/anBcwcAjtnLtWQPCkWSglmPvnUDtTCnztHWJSbeObaR6mFKprpZpp0YDRRFBSJyAg63OQLfoYDV7c88alHIDlHP8-sNsN6h6w5UwJxbYb4tmqtP8k4Bm6Wc86S46XTjqn810Q5yUI9SsSyHwuUew5A2867C3V73dsOYcdpxvr_nIsF06eqU67M2f-2ZzTfeTykSMfbrmyQPEsDtVJDBdJyiDOH4a5Sb1-rm1uL2d1BRxiS6G0DyT2hA6kcVAvtgvMUtFXzV4UPc3orcwF2M9CzNdJc_E6ERva66RAqEL4kUGwKcSom1VJrqTryyeNdESGRzPatJ6hezvyvRyhMcicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NmB9RbxD5I2vXBIplGmt_I30wQKZMH4DhEFJsVBiWGiVT2_Kt7a9dv3NKO92LNC56zHr8A7jFBREoTkC3WSwJYO-cigJjf555MAqOITjcXWS9fosTJhLi1Fw0fNdJ4apO4lLm8rl1cXbvg1DTnAiO71m2KvGW4V22WZjUtUZQSii1EVF3p3D-rVKCMTJNtuCH_7Gmi6Z2r-QOer6QT8pI85mcjhS9fljSk_hj15Q0F-iNvbTb8P2YaLTNV6_R5E2SXViNmlUliR_wvg5mAbRUPEs2kRAKTSEOZZTAtoXZYUNNW3DREuHso4yYg4djhtVXtjy0kw02sx1knbR2-GNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ESnndJEhBUdqfKPdGdbv0m_AFaB72VMj8y8da1lM4pqzsOz0YNT4Pxe-ZIqilNhq5O5iKIqqxuiW0j4oTjR4gRf0o-eGW-DMNODX4Sc1Ft9UhtaOvoApnwEfPHiCro-DIK0gPxo_yzlOliGFg-0JW7lefaQ5BA3FyWQQgGY1yLzkDYTE-yoJ_n2N-XcOxa56qzEILuy6fzvwSdxxbF0v-BY4ffEsebfrif67oPT-2K4ZT7pIFNCqZnQZz8r7gMnsRqx2vzzzjVXBGgx2dxzOku6fHOxnKHqWJ2eaMxptE0XLIVSBWHa9do30AUZSVdpHEwAnZlSbHS7Ok5BhEhQbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NMNkx1imkY0tDahAgqrJGhYanb4eiAH5w-oimYwEpDXKtj8a92kI5_b49yn6EnDL5OAmWuWjH-DL9qVEfbnfsy3Eh0hOjQJkJlenVpxExvlFMduynCJ21g40LZhh0QNBB0RQ7svpjHpLNsih7kzxYf_OzhF-iYhJOkr6sRo6ItEwKlNQ82UBAP3AKWpUjBIQj2qswMEiE7TGBtqONo6TcNAb1yX_ENyxyMZ8Yjpvp6-EJt1VW1_RCe2FEyUXbjHG8jQ9NM5ZBB7B1pXW-M2QA_QxvRPR0EwQ1Q07YY7tNIgJPGRQtdd1z6LS-IJbC4tcDWj2a7q13RXCEvAwR4jYHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XKoJZ8lm0y-2lDhFg6QLQn-wVW-_Xr9yfcAW8VoJDnBv5T7alnmu2w3ZQK71N-ZPKZyxk5h3txCl_371Wn4Hr-pVYCcECECkfHdqFvQ3ZElFNCnBDpp4swj-rpoeKUt5Smn_3Fcn9iB3oto0uYWst-zVk0AKNfFZIipO-y6UwGFcWP9B4GlU1UI_5JKipU6nPKYJdNaFfNMd0jn_aUraSEfSbNbpF9joOiVHDI2_1Fff671noHmPIv-hxTjMJfK8ZtdbapOQeWw_PEZdmY0zhgwh7uxZMb6J14j3Kl8BrSdfeoozCZ6BlYLR4orrmfF7wWmRl-AyekHRocYvn2oxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ShYsWXFtZB2In0qVQJQZnxFTlc3vPzQ0Gk0kBHOlBhFAl8rugLTcepZscy8apFIYEm6M2W_YFLQkET_XcIsAeUZ2NZtyL0EEo8xW_gk2oomT6BtSzBMIwQqDeBRaAU-e7psuilTbScCRszhhGc29l5Ox7YOL87tyaaY2s-KRA-p4iWBb7AgClbojkAnrEJ05ZJYupETSkZ58o-bj9WG8KKJ6rM-5ZZ6Sto3nhd0ReOymqzArHIPsSh75ZLidCv4J2tEllfH6xVyCKkAdQUHoEcizaG7kHmM86MrgxuEA109VQK2CXe4p3u9btT4Jm92Gx2ysmVqfqewNJz3n4sdWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lMdLSavl9V8wuouH4ZPvBVAIOn99xf1khBdXq5ApWjzNjA9v5vmaHLr6SaPWj-Ro_IvDaeKmFX4D_9afirJVkzYvKLIU1C790bU_qd_2haDFkSI6LDR5rconG-Tbru6_RkN2X6wyUMPjgesdGd64pP9WmDLK_fgNmfx8oS8ts8AccXOodT3id2EpkdZMJsDC70ybEBlULBBj0kA01NVdxiBe1WOTyrZCF-K7Pl03ytfn7rfqrrLkfz0-JDKhfE75WppsRZ5FEcAECPj4ou32bXNk0m2zaZmQaz7LnS938OSbyLRTa6Yr_Cp3tZW2CA9XOc9YXXNxufcF8_AjLNrOZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hoLbK4V3WvDk4_vwo9SgMSJOl7GV6L0G1xIx32Sq_yw-2deuSUa3GLmn7ee-laEgNsFFEssu7r4cfwwSvXkKbR2Er_QZhgqC_iuyUEYMdV1ZFVK8OHC1EZqQs0sBn6z9b7aLOSrtpOo0pFRB6u3LxRTxqFePF7nAPoZc0wZi0yOCfHe2tqt4tO1ViLRv3sKOyEoxNoPN8MWLKwtx2nocT8mhWqA81L7_X-epXSY2D9O0aHbfVDawfM7LtPTtbqq-SsiqQ6CPFN3kiccvkWzMkoyAfxHGjptyXQ_COjUL3zdgqGwrPa9sTaeyL1Rl4UqGAHEdQ-ehsrVV4yjJyv3ezw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=J3vx4x9WDC0IFzr9lMPjjBSfpb1IEOFNKM2gUb80x9D-MpWNXi9O2BKbYqfy16CGHGbCzMiaaKXk4bGtscAUg3L0-W0mDhzWoiBsGnU_KTUyb0jKBkx0XluRcqUlhsoUBu6VRHKPmcIqaHT4Hc2dBmJg6K_vQI6rd4YgJzg5ZS7-BT1GN-7qQR70I8zzU8R5gn1fYjQoZJBXnKwQ25OsjmSBljFGHxs2aGsWmucJpbGlJOY8JqUCnsN09HxHHqWYIk7XdtDDhFEG4PjFlwe102B1PaCN5Razo34wGI4kpU4KDBmaWDXczqaZaqVOcsoGr_oD5kkR2WJ93d3gJxNVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=J3vx4x9WDC0IFzr9lMPjjBSfpb1IEOFNKM2gUb80x9D-MpWNXi9O2BKbYqfy16CGHGbCzMiaaKXk4bGtscAUg3L0-W0mDhzWoiBsGnU_KTUyb0jKBkx0XluRcqUlhsoUBu6VRHKPmcIqaHT4Hc2dBmJg6K_vQI6rd4YgJzg5ZS7-BT1GN-7qQR70I8zzU8R5gn1fYjQoZJBXnKwQ25OsjmSBljFGHxs2aGsWmucJpbGlJOY8JqUCnsN09HxHHqWYIk7XdtDDhFEG4PjFlwe102B1PaCN5Razo34wGI4kpU4KDBmaWDXczqaZaqVOcsoGr_oD5kkR2WJ93d3gJxNVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBb5vofG3VWIXsIaZ3zR7cOts9yK8MggAGF5_DWJfYropI3KnqkS6pvabWwgDOgSj5R3KAFcgDYkSfNWI6Spq0oWSh2NbaC3KX6JBb28H9j7PU4fNpY7Ghvk11asHQN-7eisF5kgkgr2epD564Z-r90aHu_fhqGBKX5kGUuanSSh5q_Q3Y7kHmXQLe3zUa5TxMgQ5kXnBUxO-6mJzLvWuXQgSk4A0raMNhiuA3vzswJjBFu1hRVtnftlk3tNzwQnOKgALphWs3uhXWs6MtEWrQoVnq-i_-seIIpgAJlHzycqbdfkU-FfNX5NYi8JKV8wMwZ4nuBOI9D6QlNNcah2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgqW3k4pAiAj_FAbsWjgRP0zEMj_530AbmKmYIzO-iuAqCw-PWsAkez-tFs98vkQ6RqIbnhFiLAWC9fr4lhue2FxCUILeCi4XDbyzwdasnMnAIofmWst18aYi7T2nuNvVKv8V0u_bx86AcC5y-bA09bGZK0ekYq_H2o4atsMGRTmpd6XHGrOyFOtSZt0ZgG0m2zF-ujJ60clIcgbIa5n7T2AGmR1qdkZ7QpGKSJqIUfaP8qH4ToORJ6HTqQHaaedwlEXwdDPdHjx8DbWbVL_gUtJ5-8GiaSD_ITz1JiIs8REvbNjmIHXJToGXWhqarKrqReJOGyofPoKbFK9gBvZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjKO3rM6dzgka9I1xl6vOHyBnTF3R09HM8Dz4ifblHVg_Zq3klWHZDpiONuSUe65VNOjEy_3CzG7UHvav5Szd1tbRgE87FVMUyoFKEhuXw0pgSRTPkffuIgLKdNmNcbtbEOm-6-SsoyGm4OvLqZE6crLcmPvOcd8Ua5MQMAPlAHLKQ6ulsNJrvol7COsyDG4EDapCmjBJL01JSG56WIUshe1GGXR5gcs_KMZLNW5Q8zGAUYkIcfqh-LDSuS5EyrJrNpfNkhT3GQxLfTcCl-qVEqxgWxbcclE2bD121zKYMAI5iHVEGdNJhnnYsdKg4ob6g3BWzcLSgUCIZiH1d1xEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=frqFCtH7S0XyarnWWcWd4dGA62YMp-PzM62dgn-jpyw2zuwQ6Pi5aVWMAt87MGMaJk3TCVHmp1vjlp4XjG2FW730XdU4HahCfVusZ29WBsteVP_tBonjYAUtwe3Knh6hZProj9NaZ2qDCqFLZhVVeeKX7ZnITBM0mV6obBtuFfLDX6IDF6gz9Tjj7RxQjq8X82A-3MZ3-DVPuFkApzabxU7gwN1r96bfI6GEyG7yRfvr5V5oSbu5PwSr5-0LqdmY-4ePU03FgY4xN9fqR0izQoIBDneDxbKHvE0mH-RuXCf71uBzw9MfhwMJgk5F5Cz3JWl3l5LrWmumyTOq48pBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=frqFCtH7S0XyarnWWcWd4dGA62YMp-PzM62dgn-jpyw2zuwQ6Pi5aVWMAt87MGMaJk3TCVHmp1vjlp4XjG2FW730XdU4HahCfVusZ29WBsteVP_tBonjYAUtwe3Knh6hZProj9NaZ2qDCqFLZhVVeeKX7ZnITBM0mV6obBtuFfLDX6IDF6gz9Tjj7RxQjq8X82A-3MZ3-DVPuFkApzabxU7gwN1r96bfI6GEyG7yRfvr5V5oSbu5PwSr5-0LqdmY-4ePU03FgY4xN9fqR0izQoIBDneDxbKHvE0mH-RuXCf71uBzw9MfhwMJgk5F5Cz3JWl3l5LrWmumyTOq48pBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=U9RaFw6oyfg8hzAs4wzxjbAbY1QkFEfYKhHePm67aquWKCBnm8vGr0YakzDJ7ohYExP9UGLvzxPEoP7_rOZGXQUTfxpxxzx4vCuJwEVr6IMtMcWaL8U4N0Mp7zneshSq7rqRewDqzEZ4IrwbrzMf3a3hKF_TENVdeQdzIAMo7nuDCPQ3DWAvSyJ5IKJBPv20J5pnfPPNbKEB8p_wepJsLYtWg1drIV7WIKTsAlr_0qPuLACtaO2knoi7Z8eiLjtO79OSjVmfmbd0oF6aZYMv0B6D0P8okwkS1jDiCbcePQLQhnSdGzC8u-gc6O9Bqr1WT4bADzyb5CYSM5SGWZoiKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=U9RaFw6oyfg8hzAs4wzxjbAbY1QkFEfYKhHePm67aquWKCBnm8vGr0YakzDJ7ohYExP9UGLvzxPEoP7_rOZGXQUTfxpxxzx4vCuJwEVr6IMtMcWaL8U4N0Mp7zneshSq7rqRewDqzEZ4IrwbrzMf3a3hKF_TENVdeQdzIAMo7nuDCPQ3DWAvSyJ5IKJBPv20J5pnfPPNbKEB8p_wepJsLYtWg1drIV7WIKTsAlr_0qPuLACtaO2knoi7Z8eiLjtO79OSjVmfmbd0oF6aZYMv0B6D0P8okwkS1jDiCbcePQLQhnSdGzC8u-gc6O9Bqr1WT4bADzyb5CYSM5SGWZoiKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUiJ2--GXMutrd3ngtEV6F5LW4tllzMq1AcWFtJ6tzoPkwnVl2xb-D_Miu4yE0dn9u8hMcG8Vj643BkDQZTb1r2QDKY_uNbWl_KHYrPkVCYhFVJ9w9kpNA7dTt6F6pabFGI03D0DO-1WsbtkZ_KfNJnFK2PqZC23BukS-lbnLWPWX5yJkd2lUt6ACBNpOZIIrKHnRiVGhVxoPTfvp3PuK045UdZJUPbtaML-GkZcypwhgcLYSmX2Zwi1M-O8p9kmqrLq2tDN9t0KS2fWJAi0ck0Q5mPw6dc0fZkFe2XQecFP-EQXnixJHgq3e7vadxjWClZL63RNAMFVBO_jsrMo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JEz7N7MTe6CERGIvEvvuWmBepbW_Z7HQEAnyNHIsiAriYEdCezMc5DAVdXwyUSS1I1CPoJC3QlF3NBQ2DrZbvvo0lhWb2-SSpkoRycAmH6ghZcgeVvgXJCtlNcaxUP2An0N-bofKJ6tD5BilahXdnfBG2JiVn31NZ0hKAhO2j0JVR6VxjRFvsh_Pa2WvW468bG49P4hd07AQNlOvbIHLy-bkwj5nTlRd0Q801UA5LDfd-uDMcP2NNA4HWwT1EXgrYUb_JiAtm4Np3E3qPc_V_8Ce_qTQDBRorTp9AAAqo1Zwu7XWUZt2twW2Snt1h-S9LRpH7koU0SUFy_0rsaD2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ روز جمعه در نیویورک با اشاره به حملات آمریکا و اسرائیل به ایران گفت: «آن‌ها دیگر رهبری ندارند. رده اول آن‌ها از بین رفته، رده دوم از بین رفته و نیمی از رده سوم هم از بین رفته است.»
او افزود که این وضعیت، مذاکره با جمهوری اسلامی را نیز دشوار کرده است: «یکی از مشکلات من این است که کسی برای مذاکره وجود ندارد.»
ترامپ سپس با لحنی تمسخرآمیز گفت ایران «تنها کشور جهان است که هیچ‌کس نمی‌خواهد رییس‌جمهوری آن باشد.»
رییس‌جمهوری آمریکا همچنین مدعی شد سامانه‌های راداری و تجهیزات پیشرفته اطلاعاتی جمهوری اسلامی از بین رفته و توان تولید موشک ایران ۸۲ درصد کاهش یافته است.
به گفته او، جمهوری اسلامی همچنان تعدادی موشک و پهپاد در اختیار دارد، اما این تجهیزات تنها بخش کوچکی از توان پیشین ایران را تشکیل می‌دهند و ظرفیت تولید آن‌ها نیز به‌شدت آسیب دیده است.
ترامپ در بخش دیگری از سخنانش، گزارش‌های رسانه‌ای درباره وضعیت ایران را هدف حمله قرار داد و با اشاره به تورم و کاهش ارزش ریال گفت ادعای عملکرد موفق جمهوری اسلامی در جنگ با واقعیت‌های اقتصادی این کشور هم‌خوانی ندارد.
وزیر خارجه جمهوری اسلامی روز شنبه ۲۴ مرداد در گفت‌وگو با «شهرآرانیوز» گفت هیچ مذاکره‌ای میان ایران و آمریکا در جریان نیست و تهران هنوز درباره از سرگیری مذاکرات تصمیم نگرفته است.
عباس عراقچی گفت قطر و پاکستان با تهران و واشنگتن در تماس‌اند و میان دو طرف پیام‌هایی ردوبدل می‌کنند، اما این ارتباطات به معنای آغاز مذاکره نیست.
وزیر خارجه جمهوری اسلامی همچنین گزارش‌ها درباره وجود یک «آتش‌بس ۶۰ روزه» را رد کرد.
به گفته او، در تفاهم‌نامه اسلام‌آباد از «پایان جنگ» و تعیین یک مهلت ۶۰ روزه برای گفت‌وگو درباره توافق نهایی سخن گفته شده بود، نه آتش‌بسی که اکنون نیازمند تمدید باشد.
عراقچی مذاکرات تهران و مسقط را نیز «فنی و تخصصی» خواند و گفت ایران و عمان در حال تعیین مسیرهای دریایی تازه‌ای برای عبور کشتی‌ها از تنگه هرمز هستند.
نیروهای مسلح دو کشور نیز در این گفت‌وگوها مشارکت دارند.
به گفته او، ابتدا یک مسیر موقت برای رفت‌وآمد کشتی‌ها تعیین خواهد شد که ممکن است مبنای مسیر نهایی قرار گیرد.
عراقچی در عین حال تأکید کرد تعیین مسیر کشتیرانی و بازگشایی تنگه هرمز دو موضوع جداگانه‌اند.
او بازگشایی این آبراه را به تحقق شروط جمهوری اسلامی از سوی آمریکا مشروط کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=kC-vOOcAtsYnx_wpOmUf4-3vsj0uB-Moq9A7LjJwL_3gwouuAlX2siyQ5QTDATrUPHv31VmOOwbUVP4cIPkdVaZ5qejP9O56RtIUawQtJxG8yVUJBnUDfuSMXIFz_AbUx6YuJA1JxvzVkd8yuWf5EbO8QZH3G2NYGzZMBnbF9MfpxDsPG9Lids_RkG4VNwM8iJHD6u4KyipNPMQ5Q3klTXbozGE3TX-r8dr-08hHUPQegxZFy5PIFRDV6_2YaxuiskQjWLYmVc4Ww_UJl7JIZLLaDNN_3WibDzKwQqTJYr0qbjjcxlawnAGp-B0aSqT-35ZoQydZE0b-kNhzQbHgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=kC-vOOcAtsYnx_wpOmUf4-3vsj0uB-Moq9A7LjJwL_3gwouuAlX2siyQ5QTDATrUPHv31VmOOwbUVP4cIPkdVaZ5qejP9O56RtIUawQtJxG8yVUJBnUDfuSMXIFz_AbUx6YuJA1JxvzVkd8yuWf5EbO8QZH3G2NYGzZMBnbF9MfpxDsPG9Lids_RkG4VNwM8iJHD6u4KyipNPMQ5Q3klTXbozGE3TX-r8dr-08hHUPQegxZFy5PIFRDV6_2YaxuiskQjWLYmVc4Ww_UJl7JIZLLaDNN_3WibDzKwQqTJYr0qbjjcxlawnAGp-B0aSqT-35ZoQydZE0b-kNhzQbHgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=HvGruQrUdkUhAyNBJvOdj_dPx9pEVGJ5-k3LkfnaaujNE3U43Y55yPRzmPcegZRvGu2HAtGQHZ5jGWfNq65IJu2D-KFBZMBbi3jr1hAI9ylnZdkgkP3COaemAyfTNyTSWfeubaJSZ6R2-ti_bD-dwvmUxZnpC7eGLZwCzbLrtFK3ksHmlYkdQ9UvRQ5y3Gt1UUflNFfJDJ2WlzEGiQ4ZoJgFIdd9CSPTt_o2F1_vbt73zH8Y5b-7G9S08wLQ8ATt1cTrzZy0ZSk1m4FZP0nQfJhKUhCNFoadxOQxNAvUW5mcgqSVu1l1dwwNpXP_vAXN2OMqORecelJsD0lGxuwMNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=HvGruQrUdkUhAyNBJvOdj_dPx9pEVGJ5-k3LkfnaaujNE3U43Y55yPRzmPcegZRvGu2HAtGQHZ5jGWfNq65IJu2D-KFBZMBbi3jr1hAI9ylnZdkgkP3COaemAyfTNyTSWfeubaJSZ6R2-ti_bD-dwvmUxZnpC7eGLZwCzbLrtFK3ksHmlYkdQ9UvRQ5y3Gt1UUflNFfJDJ2WlzEGiQ4ZoJgFIdd9CSPTt_o2F1_vbt73zH8Y5b-7G9S08wLQ8ATt1cTrzZy0ZSk1m4FZP0nQfJhKUhCNFoadxOQxNAvUW5mcgqSVu1l1dwwNpXP_vAXN2OMqORecelJsD0lGxuwMNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=Wm-RogdaagEZbZKLdPvSpe48rEUevv1qY1yeZTiuV76TtcfcLfYjAPtEvAQMV0EwyzarCHxS_3qWItSMW-Mu9b2okDTqIexfPEe9xdLcwoh1YFNlkv9H8Yb9uNpLqqY22-E63oNu4jp76z5ZpeLeS9dVedkjETHo6ANCDUMfwFjByPBTMl5T4E3DOP2UZ99MmemBc3pMEQIZSl7KXPeUvjQX_WHwMt-irGbQOGdLRuy7dea5fxR_UjGjXzbk-dHKBsC56Uyfx1M0S-PTas7DYg_4XXpG1HIE4uvV3Hl1ZQekKO7YdqRp0H5KY0Qk5zPxHLHFRmiF505B_mQhAbP0oYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=Wm-RogdaagEZbZKLdPvSpe48rEUevv1qY1yeZTiuV76TtcfcLfYjAPtEvAQMV0EwyzarCHxS_3qWItSMW-Mu9b2okDTqIexfPEe9xdLcwoh1YFNlkv9H8Yb9uNpLqqY22-E63oNu4jp76z5ZpeLeS9dVedkjETHo6ANCDUMfwFjByPBTMl5T4E3DOP2UZ99MmemBc3pMEQIZSl7KXPeUvjQX_WHwMt-irGbQOGdLRuy7dea5fxR_UjGjXzbk-dHKBsC56Uyfx1M0S-PTas7DYg_4XXpG1HIE4uvV3Hl1ZQekKO7YdqRp0H5KY0Qk5zPxHLHFRmiF505B_mQhAbP0oYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z61uOheKfemheIyAqeQKIWt6rXrvzeVTlGu66c0iaGR6610T1bRL8wOKjbBDvbCrB_tK4EbtFbwmBFSXB_XXOQm83nvpw3mU_wIFWuv7Mu2lp7vKYwIAg1jUkiXYftLTeHD4h5LJHoRRhq7jZv3Unltyf6LiYpMuGBhxxzc0LFYD9WP44WPXUzspto4_YwlOXplz8U_Egkx9VxvDirI1HJq0V-e0sKIZfadnqn1eNFSt4Wytgt-69CIqTl_5cHz2O7KyoxVXCT9Addyhh0sL6NjfzsP7ge2RY0BL3uBAaw3EK_QdyjprvEA1ucIbROmkAf2idW5uTUaOYcaRPTOdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iyydcKyHXHfkRF7zxJC7kMN81RihnS-l8CD4EDSkY1JH1enb4Y6nBQDZjN3zp6ghCQR0b21xIdZeSZ1HRhoJiqtmItKMG5gvi0qML25YN7aQdn0MQnkhqGtH8MsnMUcj7hJe_nUzBSt4yksASIse8sSkMfKDwnTixFTC0KlfW6At401FkhmwJYNtij0TUAMJdQLiFTBgimxp6woNkvBs8NKKb82gSG3fqYMEddqAeA6p5ZvH6Q0EkIz8YzGsxUNOKm5hBROFggosWMD1ghou_4cQ0xsOVTuxtyvc-OzWsK2iIWd1SRT49Vtc-MR2eG0kbXAIvuoJqRLQusfo1jdt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=uFrh1F3HFCbBlA8RPAZCKlQInQ_1EniRhWGj2olwZmRjiPkl3F6yrhplOW53x8O6W_1_KhMtkbGwra-QzUHon6Q9GxNXzyhsiK8Z5r4m9MwA3Gxosg_hWrQnW14hSy3NsVOC-j4QmS4miMJvKNUGyHolUXNLJj1fPaWUdGD5aDk1rWGhxSV5UeCz-OWNv4WMVVPRLHXxUWevhZdCUyn4GbdQgicq6fnYjiYLJ8Og1GqOwPLSfrcEsEYWDHS4pHfX_YjqoHjYYJHGdwHxBKBgaI9sb6-dUaUGKiRi2yL2iEQfN4pWYDaFZm_itGxeMi4Sd7I0e_FX33plbqmqlMU-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=uFrh1F3HFCbBlA8RPAZCKlQInQ_1EniRhWGj2olwZmRjiPkl3F6yrhplOW53x8O6W_1_KhMtkbGwra-QzUHon6Q9GxNXzyhsiK8Z5r4m9MwA3Gxosg_hWrQnW14hSy3NsVOC-j4QmS4miMJvKNUGyHolUXNLJj1fPaWUdGD5aDk1rWGhxSV5UeCz-OWNv4WMVVPRLHXxUWevhZdCUyn4GbdQgicq6fnYjiYLJ8Og1GqOwPLSfrcEsEYWDHS4pHfX_YjqoHjYYJHGdwHxBKBgaI9sb6-dUaUGKiRi2yL2iEQfN4pWYDaFZm_itGxeMi4Sd7I0e_FX33plbqmqlMU-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SkL9xwHtOYclGEmNnpviyu0C5HS1LtjX7VHBtCTE6RrdGkhmQdgnIsHudVNEksQpYIVAgrwxzRU9D6sVJ9B_xnIJ6YmR1lZExHu-2mCtY_J9nsRAJ94SQIPpeNlxHa_RWY4LE8qc40MmZkz5sx60RKD7yydPbFPEW-KNo_kcgdN7XPw0rrp8HZ_m1Mz8TJKR3XGzianckxPAozyGHVNhijaphJoM11VgjdEG5_qFnc5UhoPjQR2ghJK_K8YT4AgGcXqnUEgmgKVVc9SGXJspLsw90cPAZPJqZ48pN1Fho9P98VsYv8g6_x2H7BiYsskPKiQVamP70QYqPji_aJ_NpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j_EtPLIY--NkKUX16M-X5HbD6wFScZYVKNFQ4O26v-QA2Va2aKWJMXGOvdPuvZdZkAL1h0PvTwzEVW6HB4lVq-oYoAiAVLI0Xs08zp4vHEjDkXBEe7cr4hEU4Vj2sTcH37guHcRKplXYz0LWxbXWi-dxu5Nts509KvFSbgf8K5EbolSWD3K_bxRY4xGiQK_lh6BJ2IrK9UYe6jZZJYjM1SrJlYAUjcjEII9fF13aO7QwvfKOVgA6msxwkulmJ2eUb2POkz937_NBctWsCDOrfHOD6MktA_LNJ3cq3D4v7WULClBl28W10BBNgIEOfV1PmpDLss8O3evt860R6dXI3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UU6qM2mqsTAzFQHmysTt5quKn60y3NxFb2JKlDWbhSpsw91Fhyd5mAqDU4_nAbM8TtWSM_iiLd_zYFYVb6gqLXJlm2tqJxV4Mp03MRsF2HuDfJbtu6yRa4Lzfu0XGsQgf7uixVuca911MlBSUCI7s_Y1a39xBQSSuG-wtQeu7BsFV_p9DpeW1s5lUPV8AVVgfcmpKLoT35zGYv_7v2IrhpxkMtFcCFvC0nsHTDMSXBEZ_SxYxCp1ndyQLzAh6clloK6rzqHLFDzbbyVU9D5eaD_gPbpriykRZeaJVMw0U5orIocEnN52btVu1Bxf68q80Bvv454Y_hAliYdC9cq8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILDhF1nar_Vc-fPR-ZazSzRjxAf1-LBfSXTYhhDKOBc7nYyA6NW6RjMZYU3RYL4CO_Kg-DCf85w0_Zr3lzkkjRqHYRZ8s5H_KBKUwJQHBUVmYfuZd4G2ZS6mWXR_uvYdlUtw8nUy87rjqceq7xcO2iZeRhIyMtlapcEMjPSwY1UuUT2EHeE7vdLnqdkLXBXRQqoEaoKfvp5Z4ycVuTZBLghJkxpsyasdcDYGDLFQufjVv6nDtn9cVC3q-Q-e4KfzyM8H7CSYO3kcJWLVGXjBjZ-lVNN7whTRd08Uw7SAgvJ7j3EOOe6jNG66qzPq4wOJHdzLJ1IPItkMrQpuXsHglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_TjrJerNcfb6vEFTZMsyEova8Ystp7RmT-qLAawZtKRlkoKZlAa6EM_I5kyW3N29ulzv3Yz8bo0l3VhlE226pofjTUDHNaxZxtxrzUmS_UV1Uu1Wi4nSTpViahqj5-Icbcbmt3qQFnes0EcJo-tIkXghLriLEDHCr9HeBh6gr0-uy_pMLBX10bK8PFSjJLHPFdaiyJzE1WBQqi-PWG8yzUiLTrXeBsIyoZCFGFun6hZ4wvAEdeWujmZ4MSN1ufcBhxOnSzy-9fgXmMskia8L_m7bcRsH9ssO0ZZTg9It2xHqelJCOHxJdBPfquMsTCXVdY_P9kdwGmlyqYWS1UnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oP_7UUB9qs97qeFWB5FXFelNDZIaERHVYnl7M1qift3fc48JlY9rhEmTioV8cgx6DbLiZqxloX_bPVFsCC5PKaTX24HJe1LyrS9-jmIWUd4C_YDmTVF-tGTcaZI4YwW8NEP4DLOwzLj-1ewPLfoV8jDCY3vNFLWvGOeMJ3MPQQ-vFWEb9obERj_UbJM6bD1-2iOWrAqm7uHvqDcRl84Kpzh2-PVhF03metUY_Tjvef4c1XggHNCPlp29pLNbbJXVsgMYFOjlAxpjq7WIlXaYYiHtCJ4jx0eqdS7Ehxdc5qkOXp19GzpjiQsEU_PrFNde9_EGdvcs92X4Eap6DlCRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvP-fW2Smji5qcFyzPYGUrMLhOY7OupFl_Ft3hCfW8gKwCcYPkx4R0UHPFLYo_Ei9ySlSp4_n5oa5wyYqKwJmxpopmTSd0-sm8RDhdkAGnbyzf3ctN6HhMQAk4tQXNGuh2HxqW7IHndAUooUUCPtJtdysNvHApa8JTlp-a8f3BTK_li-NstWLCTd1yyAT7W-Xg3asttpIc38439XzCXQZZ8b35nc7ENjyn0SxuGtVOIq932hkdcZ0yZ1PgGpHlkol2zesfR18d1JP7mc4_kyxVWxkKNUEezV65paZwsLeITF2YPdhDGwP_3PAm0Ge9PJK89pAAFnFFrOqrbKIVfixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EMwOmz5gBJbwUoCVtnIHMaMHYaEKptfUQg14bSQo-PGlGklO3cCTiXq9We-vNlZcK5q0QCSly8m7s91Gm7p-Yz35-j-4hwHIbdNHiiOtR1_vgVCH4vQTh82JRDvCNhxh-XgLREuSFsihhB5VWFhpxBgaJI_vrInPXhk8icZYKr7padq3Vlwqf0HIsr3u08ug41wtJAYSp-2vYxMwAER1iAAT2uvrmZsR9w91nutEWAu0f0Cq3LqBZmIKgAhmaV7q2x3XTbbDSk-VXA9snIRHV9ht0y-4Q9u_R3YFFyUr62gQSeXyttXW_URepmGYr1AICGI_kdf2QwACvvrs5N0gLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dsRVwcjRYPnJWaGLJZ0NCRj__YVS-tztNrz7Ss7Wxs_HAzUtmrxZFGORtti0KkhsgcACcVr1-gZYM1WnpCG_NPkLSCF4_rn09lHiQmSdPkoAeE9bBR1g6KMIQmQW_ZIU2Ga16rCjS93Q28otuQUE1NZBSrj9PCpaIIDjWOioVnAkqBWVZwOnQ_REIGdKCdjq9cbPh9hoJLg8jJvQiRilL4uBA0_Q-NkLm2knKmHeE44wacZFgIdRj4BNXJDyiFQbsWxPrw0PCMbh3AbhlrtP4CD20X2kotBIAkzfxnAkZtghMMVfHEt8_4QQEkJ9cZglXxTe4l54nhDybIBGk-jknQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7DtxnV8Kw5Pp6JSYFoD23P4aIZZwFgIxo25JRdrLZimqEHXX3diUvgp7_Wx9_H51IU-e4dI_mqhllQStW-nZnJ1uLb_SYRrJMfQ6S4Bxetra3TWMHzRsHfrIlyRuV2DAkCx2sKx0Q7iJbHRUMc6pUBOYf94MdD7nhIU2FGzjDBy2E-zGEne4gkXLcGwybzs12JM5UTkyEQAJ1954D6IWuhC7hp12k1ZWUxkI2xpVTT5pRD-lZ0L6NePRw1eXNmAcrbaGUXNRV7BOVEWlF27-It6tOSn1paEW_uRkbfe93AifxXpPSiRTySI9EYSAdkwR1DD7kw_pTWHvH_6Hc9KfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=Me2RaF0Vp7CaKynvyC8wP6H09HUHuCAKexY2Ag8PZIZrNpe36RMdXHy5LNX9biKJWZZMoYhC6hE70GML4qO50aCLGyKe7t5Qslc5UC34aNA1IphaOvbEkczsYMomdrweY2s2fTIfGFEH8o6dTYMSh-StuUctdtdSxSDL7n8z7J03-HN_Yauti1ADGFKwqvXiXb8ABPHdOXzyv8yDb_KiDW4pajYjZuefgZj1Wkj6DgzqsJRR6tsplbTxR31LHWbXQNiXmCx44_TeHUGm6-R5oc1FvHu23Iib45TbNgWX45WmfCxS4huRIfSI8R8MZnxm48-mJTnqOrAHIaIXF8Q_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=Me2RaF0Vp7CaKynvyC8wP6H09HUHuCAKexY2Ag8PZIZrNpe36RMdXHy5LNX9biKJWZZMoYhC6hE70GML4qO50aCLGyKe7t5Qslc5UC34aNA1IphaOvbEkczsYMomdrweY2s2fTIfGFEH8o6dTYMSh-StuUctdtdSxSDL7n8z7J03-HN_Yauti1ADGFKwqvXiXb8ABPHdOXzyv8yDb_KiDW4pajYjZuefgZj1Wkj6DgzqsJRR6tsplbTxR31LHWbXQNiXmCx44_TeHUGm6-R5oc1FvHu23Iib45TbNgWX45WmfCxS4huRIfSI8R8MZnxm48-mJTnqOrAHIaIXF8Q_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2ecSoNiyetldZJmbLZQs7Rz4IoS37mgw73QLQox3fk_SenndakwC5fRNNjfsKfyF4-gdZGOAfCKro_Fcb4knsz99Hyt-QPPmtXJMl5LoNdn8P_8SvsJOMs68gdvxKEz2IJLaXMAmuFbHzqWEs9jNazpa-DPPyl0Son1e6oFA7HAMQmVq64KgTSiIG2Nrnf_IHAOrg5j1nw4SG5o91aLUwZbAPhbSp_i277q0aOWUcwABiwwCvIJoV_men1mqONzlyvyGCWJWlLRusl8W9cZjqBvaEjfMcUZ0QpATJE_C5zWlRPAE-h6tgzA5sMK_FOrTaqFr3engyvtJQ0VabHfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kLDGC8J6iamnlEJ_fT-yzOEAQ8GEJyBl2EOPdZ-OkWBzAPsNvlf0yEGCvGl0zqvoejf-jDjrWlcycldZQNJ8_0u0ExDjQdem7q1f6dy4ZJpGZ-s0enmwPU2cU39WFXRpQoEDtHgRbkrtIVLcQCiaObVn1BM7uo_HxVy17b7_jEw2Nn3ouKUC4jypy_MdqAh6z6IcsGTAWiz7XjmmtRle_598334NJHxV_go8GbANiKLJtUFC4vnqCNGlWxxvFOtQ1m57g23CZwlB2YHVWthD6nkIprWWOuC9NyCR6MulR_q-5xS8023GX6JY5xsBBc2vdPo_YwSVtCXDrbQ2AHtrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUzkcEai609TzV7SlPam9redWgDbmhaCWgEHHgvVRUvJVSDvXP7Cv1caGjcSIeV_dlqEwlhf8wNymeXyW1Y8eIft_Ad89PFEhkhIz8KXKIJAf_ZXn3PervyZ3aTtV6hzC6xAaV9gPZHC0J6GhIFBDjjTaewBMaFwAVEDf2aYSHOPUV3Iw4qTYH6EZFHnMOIt1P_oiLLbhbVSVPbZlhbYJgZ16ET15qhfUd7tQv9HbqAHfTJUaH0fV2mNGy9sat6OMThescQzNMyMZVnsxJKN08UMzbtuNmC7-Rh_letmij6lb_po3FAb80JTcM5O_T1A8vr2k-1B3cWF9GLrf1jJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tTLzOX0XV-WswLGdEpPLTs2ODPJSNlaLg8tpXFnY92McLTHckmmVfElkuyBrqsHqDa5dm3xe50ES0zgWVgIIzaqUbNRoYG7BAsM3FP_Ue4KdyRiWKzmYKH90YTW2EudO-zZ4TFP7dFoPK1ictmOkTn_47zYOUk9lorSQz5QLy34Aq6VInAm7FwutW41vnYlSCU1nA18I3_FtxsOg6jBcyNZ763hCvd3accQXKe0qziluEFyjg3he5cK4_xSaTc_638YrXS2biB5iXZH5S5xaq3Bii_J5rTHelkvocRXfUzhd-vIH6APgBkLyd6tfo79mfT5RA0h7NUQUqNbGZbqyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h3bQsys01foLKZ8yLq6DcJ__JROEUKCSSppwnyfAnICYTvtNMco4FwQoVXDELum4Z_ra5N6irXE2zVDbYAut5sB-EezcRR6D0CmQ54-t6YCcCTupRYIn_9r8dM_VeiWL1iABU8HUf4q5cYTGSP8FSt4D_6szkVSAnVBFft7JH2U1dWEnEOhBMvZhHsO0Afuz9ky23pXYUVlrExX8S8nvbFczC-KZIIMvWdygr_0MGkmkq-fcuNndK3b3-8v3m8vU5pNN8EH8kEho51z8DuVXzztt8n7T0kl6ZfsxcmfPEvq4DqmtNQECBX2-oZcA-bHoTSysttZBh-rVuQxjHKFlwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hqY006mpyGXbooGCCNcSOexNcuPW4ofVCkwbUJwNGgTu-uoZDp6kkRSylTjbqPtdzrjCu7nd6-_9DdOiPf5h-Z-DyGIRFvfa429Mwba8F9fjkXp8o3fDN9bZDm7ife35eDnsYSw2nALU6Aa_JFstVA0vGmVgQCbkf6X5FAaKUGzkc_yu4WPYsxosCUm9Se4IyRv_6VLc0OdhKP2ETCpsTyXVwzUwd7BUjqs6BeexARFHvEmibGS5iYPGRSPvFOiYWfHD9Cwhk4UfbltVGxv8yndRSyVD4J8s2aG3DkRw7tZBczhfoFr8RiFa7Fj4tHQdUqUh6FKKnienIJVqf7fBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFME1Y_ELQgBXaDCmOn4G6iUC0sgZsjhLeiHa9aggoYQVohgHra8ihJsqNNJS2V8pAayJMGSx_-DELKZo4QtWPYhocLs64SHxMgOeIq_FSOdTBt-WujuDBKtbgIMnrvTA7Hrz2SWInilzKd31_lzNPN9bF2pMFrlC3ca16Tv7xRXzkrJXTaNmT0t2SFGKetz4yXHj-Z5BE1Q4OKJwDuONF7rSJqfisyrxkxqOdp19hMii2jWV21HIAfPDV3JLQzlXjdVe8NyNq73-CbQnZvQT0c-eOxdEIYa6J3BoL1ewGkR-mOda02pcWuF1fRpC05toc_BQ6uqL53yUXYRtkxjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMOsLBVve5-1k4gUZh50mXHCI5N58OxL5ktOQqKF4Rk6ySHsZUVP3pAxftzEeOril-ThVImJf4rpZhz-4TXeHrfYzhYoAHRf-vp_rCF8DemIZIl6jSbUv_B_B1NZI_qgsIxDc6woRlD57cQYCA9jxL9DtyM8Stngy928qnFsbvs4hv-MDmBKS0oqUe3lRjrlxAWsBEf-pTj8nE9v8f6Yt0BilKUYTYtcMY9yLtnHBW4NbguQrMh-WkWQ2B33DXz6za0cR41I9RUPTBm8D6_3iv14y3q8MbWAqryhBdlzqkY3qo2M6NHk4R3RcalEaDFrCAOikzo6Rb6b_U3NGUmo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm_gO2uTWPmwLsPRQ2EPhhuAjuLW6dk84kmvNWy6EZsGJn3wuIr7X4H6XTvf1-kvIOUBRct2GwLhkGhB1p2SPNE6MlQRGjr-cP5zrw4NEACoy1DPQOvqY9tTTfVKVU96A2JVkPCQMD66423Qz3sC2W3ed_TbCI0jHFfaozcv8MN0wCeMMTA9BVetQdG3j0xOTBfo3ttlz6Qpe2Tq_gMhdyJw5OXTFp0tFFus2lqgtB8lGCx7M65fkcoRbHtXrGqa2CorWXsYJeJi4xfu-72XW0eGr1FTCngNCtRVtkJ1p_v4ZZQdOUmBeFxde2jcZB9PEnNy8y1LBC9tCziLEbX6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad4opI29Guu4o7NZeZGTotcwlFid3PD0xCZQqfIWrrRYs-G9WDXKjHBmLYUKc8MreWh-3PWyxtSxDNhEzc5m06Sel2oRvARKE1VVLc4W5L9xTWWUigh3nPpuJyI04YNiyQ_jZ2egKZfMYwNhvh_fboLkmgGVTO67XZP9CdsGGrLxIT98LZYz7eBGY9-HqbGbZG5NcCxh4p9YZ76lB0t0MFqK6fp9mlMHb6xxy5Rg3znto49dgGeA9YbSCQrvNMr6XINDG6c1-U_cWcxhEu02SJntRv1Vu5-O2E0aglkLJejRrA45gK8pr9tT9e0q4OMifndTdFGcPMibJ6LrnnHmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLa5Wp6_VbX3oV0pkvCmqMm86KGiX9Kqxtyg6RFEMjTQjwT93OWDgPQBs1HwQs7hmebBUZW1hLuAJM8v55Vu9oA-lb4xjL8_J2-F39L0Bk6OxeMzEbIkWPnz-dhIMvy9BybbfT0yY_S6HOkS1VvhM1uFs96FU5v5KRyTv7PK4LxF5Td9fw0BusmdDRFh2H0BrmhuqizIhFOV57GtnvhDLXW2oiAfg_U5YG_2hL8HHXlCsfs1Gomo4FmDtHq7G78bgmB7aq8iMohJ6MUIhbBDsKLjegrOfwM0WrcpoR_e1YXW86yniFOi36NVohNSbC0aBc0cllnQWR6IhxqF-m7yPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFE3xLc4l-0Wv0SSPia0T9QWp1bNpfKEK1n6FjtkdIsV5Rv39R2Anhz6Zv9glBwCRjQKLk79r7zCfe251ml7fgTFkC49xU6tWuneGYzngIy7NkJ9T4GBU9qxqF9do9Q4H4ITFOpu44843zIDCseH6X_EG_G74vefMLWykPoA-PtMTsVRmIxoVT0svnD4xTnCLcS2PV4kGk37whnobRTDEaEF0lm43O-P5eQzeJ_XltJgZvKqngOdlmlQdeRFXnlVleUPJpaFh2PUwe-A0lpk1xFSZVW62ESP2KuS-8kjiVwwpD_aUggDDibwPSLgegii7CNPbmUj9l2siKVuQ1_VaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmRCZdlNE9OKu16Xwi1ECJusWE-JlYRdefocKICn4XLi276ddVLW5CCK9qcDnb1SDwtCDQTrdMpsw3B760GW0UZw2ORDL6-ha1o46ghhG5KD1H1srjzXL1WbXkh3WR36GkFaLs84Hnj_Ql8oEZPDsWSnBU_VZfh37oiCk82JO_F4gv_x6Rq44Qqw1CVD4izzG3wliu9vR54CatDt3bv-qL9uFNHMynkSJ3Oc-xbjdYJcS2AI1PtqwtakGXn-KTjzz7oNBQYlv5iPj6elld8gbHqs1E9F7OkyazfQ1mE6ctSonGN-9S0N7MSzO5j9YH0hwiOPSRaeczlf5ELvWZuqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-6hyz9M8U6bhb1V_NP_ZPEABeIKzHEZhj1F4SVw9Fkeg7gU-Z76QEYgVrM8oKXWEDytTLfhBwgyIdWZvDM2reNVXivo0m3xwuMX2NH9KOkgZ4-yQrRTmdGN__hqBwh2sn4s6dB1_6WDziJstEeB3NST5NMu6ZPgFe5NL6JzZPF2m3xPDeWApr0uc1lcwM7Vzy9-v2eTVL52CADZx4ZwU2Tn4kBD6uXMbnNSa01QIjtNnvKdPB_EfOgfe99KcnuyKFiRSQ8olyXtwH_9cnjCk28H_nVd31lfKkD3ohMlmHpQlWwZJGDgt1p932H73G6KTRk07fXpgAZBTLGDgC666g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3IPYyLzGYp7OOG4CFzoUg6or99VZC2YRLZgJqy9nlzNIl7TMYX29KOFT_89asDxcc4bxS1Z8PCyNG6kXmLmWPZYjGfMm32wMJCihlF4jv1GNvENtRFh_ia6HYLi01W80o2TJQo8nFi4cKnUDi9kg0FQPNZJZ9WmygmaK8qHbaSqaTRY7m5ckPiOXwuCHBLgS0Rf6KNbelGwebUlqo0jgoCJZCmr_mMPX_xmrGizCA3mwXJo7zpjhirbJ_eJdBeIbEC6hiT6XyB88rgVm7YiGaHPLkAyi5Y5ktqlGrQHQPQ6Yd6O2HihR21a_dQd-t8JNUJ17dbnuIk5H7ITW2G4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJ08iX8HHKBFYUTYR0bd5VC7nSpo4HiWGEoTC1NAmnyc-0sa-BCkvthMLnoEAmNo0Z0nqmDWqNyIckTDCFlE-eehkMmvcmA5XxSn46Rcigpk4m3NyHLM-IP48zg5DVfY0HQjdRwNlmFjk3KUTPvRPY9XzNx1eByMolFbYNpsGTsYBYo5lItMn1yEtv85Qe3eDbXMrsBdpyPsQb-OU3jYyTFTl2Gmdjyy6gga5vW3Uu3FKXi6q3PGfg1snX-aGLPMNM_LZivZ2Zslaok4PkDZBGBUk4yzF7wX1gykJEla4WWwDVS0DyWdPIynJztQZ1QOV9fb7x1MINR_CecZFm5Sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IJvGtvlG0HvJzfgHahTjJSRTtbDyQevH0owSQfrbaIWDJOMyAeSKi5w7YPgZEMo11IbQI9L9FpL5wMke4fH1zZcL4Fs0qZPudASbbfGPj-vs9QyetuQrqDzlSeRhHtABnA83CL1g6WbB2g0OSmypL2AhLToOF4eRP-GTHrmuSLAc9bV26eWvHI584EzbZYgQgrgU7ZrmLZ2OdRVZVuyuSflHIEN5KI82wYuIOEIZEFv_21QTkvr26IhqzHNXs6nG82TywMgm7IBe0FrL0V8kAqi1cHF1k0UBUwh18gK6j9YJDfkpPZUvD6QAcHO1BiOx7xzWtIOlMBd9q5ZQFf_Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SvtKu0K2yd-cVOZfJIJDfojdS1YktqxahpYn7nXPJwWwX_3e79hyATxtdi8CeeTOPcyDSbvCvakDsL0QYGKHdg5bjSW_55_hQdL0nFa6pEKxXhKrn676iAm0har_bzHr45W5NuZviQFjRZTUCvrpEU7J8CGGdvb4889wCH7wnkv8rhZ0Hu2oVzg2wNi1qTZEKoJb6U03OMING8FeLn9Nx9-fx6Q1DjCsTJY-3L6Z-bFSNyux5xeUj7BHpo3spO4pIfFGlBjVI4bA7b2QC-DO0kEyjIHb0UNkmsmAP74lYxcQZ_-QiR0VIcOfdQ1LQaR2wOfcdeq6w5OpiuRFBsyn3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QmjARNK5rMRUwv29sFVTaknijkmcjsGP5z4XfsZQ8ZjQUI6I8EUdXOyTcw72FsgZyPoPxvLJKXDFbqKf5vdxouuQoEsetGBGw1Hzh-lQgdbohbU7LNvMsmfrfsDmi2jwFYLSKbxqAIcNXpmhj0dCSpLiMKV51aFBbdf4AggBv09Y6X1wUshKN0elyAbkmgE5kC3ZWaiwYknXhZ3R-Gt5gK1Rh31qSbgfB0kqo6DRtQSpStwblzRdrva0ULTkXavA03OuT4LLXu-Z_2Qb-OA-w1TxtHENHMtCb9SmphPLCcUzWasZCm1ei_-v3KbDBipNuAv0FxX3LwqJHR-O4dY6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=um5w3fZNU3pZr_yzuvrJQxznseqFjiPAHa42FlSt410xAwRS2l2HaEji2U5ErComAYllIhbB78XmPhCI7_GTbCyq-jNHBGUiQ6ef54R63hePbm9IJA-Pn8V6WP92t92buGlJy2z4FHt6CckEq1_oT3FnFh2j1STj4Qchq1o2aVO7JlaULW9LFvPt_xehUDNZE1sG3QhpTkyYE8AnkKRupBrrJZ9o9CeAwUBIvOosDg67l43Kq4fzIg4hjjIjYA-CfyiZUEoi7B2dExWu2oB_5PaPVHNoGU-hxFMdZZOybo4bQNlm8WUBYtIYSGd9aFK5RrGxS4PNuCeWUUb5J5c-QiNMrnBvnlOvlrDxBG492A2ymRzbOMySg_wngBugr07CWhHcSbE4QXpabdGAV1H2opCWNxUvwPRzckKJ3vQKilxubXKRyuxyNj7b4RSNNns2rF8DxEy_nUDFONdyfifwTvZpQ6y46_waebh7-CemLeu8oDeZeADDBYcq4d6lEUZ4O6B9r24ImuYlecsGuUKYMwWP42yvaz-4H54nuE0cLw7HztnRPfzJWQUpJ1ePxgvPNySNxZwWw32JSCdj8f9A4dfvgvp41R_43r85jzu2r4Hi7AF0lk4Dwdx2RDBgemAsN5luMzaL_B1b36vODG3fn2IIES_NYgFf4y_xBg70-jU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=um5w3fZNU3pZr_yzuvrJQxznseqFjiPAHa42FlSt410xAwRS2l2HaEji2U5ErComAYllIhbB78XmPhCI7_GTbCyq-jNHBGUiQ6ef54R63hePbm9IJA-Pn8V6WP92t92buGlJy2z4FHt6CckEq1_oT3FnFh2j1STj4Qchq1o2aVO7JlaULW9LFvPt_xehUDNZE1sG3QhpTkyYE8AnkKRupBrrJZ9o9CeAwUBIvOosDg67l43Kq4fzIg4hjjIjYA-CfyiZUEoi7B2dExWu2oB_5PaPVHNoGU-hxFMdZZOybo4bQNlm8WUBYtIYSGd9aFK5RrGxS4PNuCeWUUb5J5c-QiNMrnBvnlOvlrDxBG492A2ymRzbOMySg_wngBugr07CWhHcSbE4QXpabdGAV1H2opCWNxUvwPRzckKJ3vQKilxubXKRyuxyNj7b4RSNNns2rF8DxEy_nUDFONdyfifwTvZpQ6y46_waebh7-CemLeu8oDeZeADDBYcq4d6lEUZ4O6B9r24ImuYlecsGuUKYMwWP42yvaz-4H54nuE0cLw7HztnRPfzJWQUpJ1ePxgvPNySNxZwWw32JSCdj8f9A4dfvgvp41R_43r85jzu2r4Hi7AF0lk4Dwdx2RDBgemAsN5luMzaL_B1b36vODG3fn2IIES_NYgFf4y_xBg70-jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ixzQauIpYL9apzw6ltgZmmFNmC2v6FGvCBnDSHT1kA-D6IzeC8PAZW7nsT9bGmV5Lcr0p-vSPUHWDXdzdCLMREmcyHmvA8GKwdRXE1rsHgSzIHeayfd2mRp37dEUOlloNKGtJU9zTIsHJJ66VLyDGxYysrgidJKjJ9OoneA0ewN5VaaIgCRbHvF7ZhiV8YeawcObo3ilJAGYS25QWqARWwenY7-J1j24GdZhsVOYJEPrvKPlycf95pRsxBgx0ByaqJ15W7UPry8tUsJ5xBNycZXHMVmAFqJv7HgVf2HKZyzLejVAOdfmZ2q6j9yhdrT-ar6_Y_YKTPIZhwWUMkD6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AVByXBcWEdDswoO6PI_-KCCehlPADAfoQSIYJlctWnfoNWJFfk0jbLh0bDgB3INnZVE0MffjRU6EcMiTaIMTgtFB_tAaAz7YzvGnsRfOXUGSi6ArDBwXdvg5VQ8LEf9fGyX50GlZ_b4jNumchfANz6H0ImmVze4pnm78LnBx9S4zqD-oO_886zMiE97tpe6-6vcXIKtHbNkHnPCHhs7hsdDK-ynx9P-XPaSCtkp9KdTUR_BMS7DCqmt6MvJBafRrCioYJQ9dCNCRJdWGCQlHdi-GtahDo4vGQUboZ-Fz_WWG9vjMf7GKra52JJtACKI-VMqswmI7p3butUzTqtIdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DvpN-mVtbSH-mrajNGq5mR2nF5xqksLdkg1KzsU88WmiOlAAmByNYg9mY6RQB1jTkFfT_daV_bZSo_lryXmDfJy8ZiDjzh3p1nz68VMq0kh3aYRnaUnymN9Gp0NCftTcsc4azEdJF90iN99klr5FSL2JSH97mCRFZZB5evfS0A17p-QS53QhNj7awRjXzI5lpcDaRoXpvDg6JRgplxgXEWkF7YrhRSif_xdFUy7Wb2mwqQwwTsH3DZY8SIDmNgVEHCpbWNm8UUQsnLAOlFxAgIfafTiKvBPywUbgylyjFaEsYvwzaKma0hWraBFVoJuEPp-7eYxHQvfwqvmeSRp1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ooME_F2EcgMmTW34RrFfi3D_EhYoS_R9lMK1x0gscuK1SdY-lj-kjcNEr6uA5P9tEegvS_BKjwxOzOrCZxexgqdEmONZOSUMQMBwz_87J_5R2tQrDqqwQum9GPLFVxNLninCTHf40KiC3aINg-tu5xP_O2SvLjW4bMsqPQp50U1ihJ3_X_zcb6m9MLNTjH8oRSWZbRjWpBImGSg4LtSEIVBDeWmLeqYz8VvDJn8rQ9ywuX5NzNcXN6BD1SiwT8bIDK3LdnZDd1LC86sRnwi1IvDjlo0ygYxZLjG_e1WUh89u5tefieFDUKNzUBRMI7jKJ4uhgkhnZm6nZrn4GA1OOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pZiCvqjq6vN1epvr3NMgE9h303VRWaG5ryRh_8kOdrHe6cigwQDnwOyKvlMxQXFcwQb5M5K3jq-pM8S74yQfmcqVe4sTwLSPiNKnYEng4-UzWsY9prqMUB19iokwyOieRy56GlIu25KoOWTpGStuBuEwYpKbohlmc5kQTz8JYanmbHmA80-8Hsc9FWcGXDEl2b10_6ustl4wqiHAa9R3PZpnSl4WXQY-t05nVH9qlNcDXfpnizUwjQG68FyHBxy9HiAtf3kucCaGGLXr08M9C7X_WQCN783b5dWEBnFE7cuEWiwydcW7Sl7fW8mh-wQisxCKuf8m4q6FIiwNNCBoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jzwpdZJQqmzCPnB2s7Rni3aJGbbKcPI5BPm8mJr8NPUhJrp9zOKSHcrlxoYfDSPfMmc5K_hD5CF2fjXvyvYtH3ILmsZChvwa3CnNANMjcvJ2qUIN3FnoaFg9T3wXabwinmD8NT72P57Vyfoxxg_pia2YNlIWVk52JVsjNSgiO3d1mwtoVOhip_X8FufkZ-D4zB6FC-foZVEfG4hxDTezceHJOcXiSAh3Z9vD8TPgDqlLvZnhqUAbZ79-03m2Mnx_RmpanRBBHWYiSjvoK0NQlBj1JVtzosoH6JQDi64UP5zLqIlom1ZGuS8HIQvLLLLp3vCneLfPuhxouePKvXIOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pj549KKpyNPLk4pJB20AMKWtKq4Jo_f1Xe_vPmkx6RAMbRc3iV4xuMg9MnGz7DG0m_04C8fYWhCZW5fR0qk-pxXDunPwHKL6QXxDIpu5KzoQFabGCb89iGwmvUO3WpJYCa_iYYe_2ivYSrXUUBsfarfJG3WoOp4MvXOWiH6MY25fxTb8V0HK8LPF38_mzWHS9gaVDIdL2WZnkLAxMZN1XQgqifcL0zQ6XSIrlNIHiBJxq8hKyswHNa3oJVFW0UYBd4VEgMVjN6exX2vezto1xXe-6jE1jVD67i_vxhWh46Muh60Bqh2KqT2elaoqb7CXNc7zIDRHIGEjb6GJW7aOIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=QkBCUVoHicXEoEjl81mdg14WmS--v1x5_RpIY4iYKPXiUcwoRyoPMHGA1uQmGpxYqCyI6EyLmmdmRT5lEQw_z3nDYumJYyxnNRbPWicmdGsX4Yo13GcuAURWPKOXAvK3ZqN1MSTAkJ_nMVymanfZngslhFSoVMO2rI7BFzfFnHLe8DRxrHvo9zOAKxindJDJneTTYTDZKFNTmj4lCMJVdNYEprezjIVpoId51x39czpr-PbJlxZFonAKvE0AXnNI5fftmvN3n3pnNBH9wy5E0xmSXF3KokbK0Ybc1C3hScB6jMJ8ghgs0v_IOtxpFBZGiUApHxKkBPN8lI71UDWpRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=QkBCUVoHicXEoEjl81mdg14WmS--v1x5_RpIY4iYKPXiUcwoRyoPMHGA1uQmGpxYqCyI6EyLmmdmRT5lEQw_z3nDYumJYyxnNRbPWicmdGsX4Yo13GcuAURWPKOXAvK3ZqN1MSTAkJ_nMVymanfZngslhFSoVMO2rI7BFzfFnHLe8DRxrHvo9zOAKxindJDJneTTYTDZKFNTmj4lCMJVdNYEprezjIVpoId51x39czpr-PbJlxZFonAKvE0AXnNI5fftmvN3n3pnNBH9wy5E0xmSXF3KokbK0Ybc1C3hScB6jMJ8ghgs0v_IOtxpFBZGiUApHxKkBPN8lI71UDWpRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVykdr8jsxuGsnPXPPODBOz-aajFKHQ13UqAHSAFThVMbULrNZ198JAW0bSqrbed5c05F8FJVlUnW-95CXAPOW1dlp1zG5tUqzReRN4tbhlrDGdd_0HRrZTWZGj4LkuDBLPIYSCXUKVik2kfCLRQbAv3L3kH5osfBfkmQi25PYIFMBbknco1_8ianAp3Nup4NR_LPH6hQcxyelj8qCYOrid_LGcY_JSbN5dYUEWwhcTrxwduTRpluIeXrviJhHPg8EhRlaKD1j2pYXIu-tj76mZuBabmsiE5zlmudEAIHd_klxsOkc1QYbXIWx1pQacv8Q9xN7uwSfaFsYEUHC1m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Afn7julXp5lmpsqyfPl4-rwBzOTzPpdnu84pBSHVaLXIonV5mIHfDqkjJoHZvpLctRCm5T1WwP47zKgnaGaH895CIragfshYJP4fNxH2sLewzDcN53DA_LcdE5X6VHoP-SqCZLItll2CKOszvWEw8XxKo3DFGdI_Fv9U_T-ZGQsdy3BuoiDMd3g_0NljZ-ggxil2bp_gnFfmmDbE40UvNMwUyazCd-DC3loLIqnVtnyqMiCcOBsH5SEnyeFZNgrltPefhyT-6lXb3zMEMXScNhqe8SXHrrXHw1jA73iJ8ASasRTWK3FuP8Yfxuvbk8_VR63Oq6zlRMpruKr7u1sd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SgDm2ob020DwWbLw-OxQN5vS5Qu54eYa9C5sxv9d496ZL02JyC3OS_xzLl295HMZulRAAK4xh__YLftP6XxArzZeK_JLjXjozEEjYx-89GA4tFQucX8R6XMcqUHFP8DDSNmUSokdQqfi5Pkwq2G_LNeYekxnkpoYq3b-h3uLPSARYZf2qiFSEUSfxOZEA3FwqYD65ruJCZQqI6OstmBAY3QWCTfujVt8zjW0j3MpbpWYUxI4JYJOrI9DZRdeuTWwjXJfdM_BCrwlrNOmwEpM-iAkjJeqn4xbv3ayVRwdw81BurX9dMmP6DjvvI2tG5H3lhPXOUKHDIpzUNjsXz_UUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=AMT1oQ-QJPGByzXZJezIXGEICjKTy6KJkT53ZFK8ZBoT5M9RMJIUnMIy8Z_rn9lxgNCfT9XSo0C8xhWyzMtO6rzrjIav3IapCs6mRwtHw6WeIgKAvBpumXZ2Z63NlMN6YfZRc-wkc7IMV-xrfXWk5LzCxNvNTpsUYdyKUM-3GGriGB2lnvuEXW8B4hjJoHgh4tgF-TX8b0YfIDmC35TayUMyUmKWN6ZIAilpuVCg3kSgECSYtZTdI4_q8Rt0A-izzqeRaaLNEJguxMJFJK6q_nb3H5D59KopbDrO03ZiGeIPzyroIcjVmEHTbXmai7aGvlh_3UAB8rCmtqxxvQaL5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=AMT1oQ-QJPGByzXZJezIXGEICjKTy6KJkT53ZFK8ZBoT5M9RMJIUnMIy8Z_rn9lxgNCfT9XSo0C8xhWyzMtO6rzrjIav3IapCs6mRwtHw6WeIgKAvBpumXZ2Z63NlMN6YfZRc-wkc7IMV-xrfXWk5LzCxNvNTpsUYdyKUM-3GGriGB2lnvuEXW8B4hjJoHgh4tgF-TX8b0YfIDmC35TayUMyUmKWN6ZIAilpuVCg3kSgECSYtZTdI4_q8Rt0A-izzqeRaaLNEJguxMJFJK6q_nb3H5D59KopbDrO03ZiGeIPzyroIcjVmEHTbXmai7aGvlh_3UAB8rCmtqxxvQaL5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=SHPXJRqxaSI2rEXOyh3Gwpy9D1hyhDlqDnYEdpk9EhCz58QuBQP6uJ4pImqy9HBL3qunUBlQv7Pj14Saw8GldW1LL4jo_8jyTfsWzdzwH8tlvSvVg00qVjGs6dBdBl0FxBQQApLfgGacOspiEZoYhk7qlEcUKsNg6ZE_54y030KpQP1VpnGvxHwCWJEln1ius6Wb_NoPuoW-j7tHmA5n_f_k2Jc8k1oBYDptShRA009B6RvaMwnyrVNA1-WYAr_pig_Q3FSf3pqWwgrHTZyq62kDu_LAEl-_KeFIsOz0RjRP7_iex2qD95jnTnqkxzwahRDu1QPAV3pL-vKtgY6Itw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=SHPXJRqxaSI2rEXOyh3Gwpy9D1hyhDlqDnYEdpk9EhCz58QuBQP6uJ4pImqy9HBL3qunUBlQv7Pj14Saw8GldW1LL4jo_8jyTfsWzdzwH8tlvSvVg00qVjGs6dBdBl0FxBQQApLfgGacOspiEZoYhk7qlEcUKsNg6ZE_54y030KpQP1VpnGvxHwCWJEln1ius6Wb_NoPuoW-j7tHmA5n_f_k2Jc8k1oBYDptShRA009B6RvaMwnyrVNA1-WYAr_pig_Q3FSf3pqWwgrHTZyq62kDu_LAEl-_KeFIsOz0RjRP7_iex2qD95jnTnqkxzwahRDu1QPAV3pL-vKtgY6Itw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifzv0OhoBAHxZFTch4iVn-7eMFpWf4ysCQisZL30vS_CSKhUjSp-qjWhxWxcZ9ewkuFbLBA-wpM0GZD0XE19IDDDVMKGGO0WK-9X5GfBytsg6Ut76ZRUoRfkRrMVnvavxPdu_dbMan4RUiB0p-_o44k1sWzL8tk0kliqYzOCi2RjKUINvINONF1ZGf9OCymr9BUvjhJ3Ms-XxeW30CRrNsir5uBpwMnfbHtVcxsDrojp1vdH8jjndvc7fZ-iQZcoz1X3hgEFdeSuduv-fTrQIIUjOb5Sm9duPlJ0rY1RTCK0WNPPGGH-ufmTJJTBB0LreHnfucOmxRA8Q0CSSlcqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSOo9TQDLIbI-OUQs6Q1v1acIV-3kuNW0NbRh-6zuP_Wmd6Ki52j01DkXETui3V3RzIgL1Kb_mZd9mjb_vwkfZQAn0L17S70J2d6z6RPYqPSiS6HrY0n9hB-VgMnZ-u1GG8mO4urSOBeqt2BgzwxPczhuGWgPr3-mBXWziMroCEjdwQp3WTq53GuyW9-HUEY0AvE74mKvY3lL62YIxe6MsA1Ohu5V1sAgLsxcrNLeVU0_PjU1mln-gvioIEZV4cAQSesBFfAFJRDeFl_eRmRDxBM4cRRO5l5aHTrx-_2UYa4ueh88LdXtRA_aVUU1WFHLKA9yi8v1cRnM-nm5iNJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fPrhS7HJPYzTTTiY0HKeNTCKmvGM4juD0W489Tk8pEk7KuXv-BH8wMgCJUDKxI57M7HPbtPlWN-RJF55VR9UkmAIizFy7hrtQsEF3UfDxjKXxz4F9OyN9RmblgeTsDlgFQjnlOh4_oFZ7b0qREY2ET2K73BE6J_z52byuyONTPGGLd7IKhPsi_qHONOtZ7uE4mm8EvNqneWSjTlgHvf_FbZypN7HtwuEkNyBOUZMBr_bbMPtGinWYmLIEV6o3ueDjdtw5aHUs2kQUH0UXTw7dchlbgueMkYv-25Ym1uvJu1A9NMVc2z7eYPfC9bfPoV2XnOgEWAdWtJpLXn-7VsH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8d9zSZLAaqKq9QY8GGJoH5QXTT6L2QTTizb7OyobkKuoff9UKc6u34c5lSO_MZ6Orl_kVlHGJve2qwH9TxQcB6GgG4_RXtzw3iiVnZkaZaME9Bm5HNZeoDLeHsEdA3AqEyLjHG50hZ0i8-wlzLEtUDJbMxYkDfJvlsVY_HeyLcMZH1QYryQPd31NDnMfI1dLjitce5uc3tIfoqoozlD04-ZOpyOoFVIAFKLbPJEkkSv4xNrAMQuC0OdZ6lHxXD0jdVOjxNyZjtwU2OFVawWi09SkyW4L4e2vr8pB8njIAV1ekRiEGQMzssma-emdEBKXzOkToOZ_3DtglQ-WCh6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpG5NoL1gblO5AzQEhDLqQbhqMlghW7n9belm3zkX6DmSb14rRai3-rC-bdlwPi0_ldxS66uEAOQIwoPSWEeJS7ZnBAGzfSni6Fn43rIhbURf6amdhamOTaIS-_Si-Oit6XW7x0Kz6C8OqO-3Ij4xCAPXdy4Q5x00XFiNXoBabaJNAI_UixZyUtap8UOFQt79EHLgeOyHAD-3bv7wdy17XG31FVNyM2fSasaKEGzEXomZrC8MXG5jfajUw2-R4s_Ys08-Lek94mpgGB82uRrGYxIkuyAn-Mw2hu5LbJtrNp2XVtZ_NDUsUoXkX66F5_uTfhcQYvYkpJrfR3K2imOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AGHcADJNCroqr6dF7bi7uEL_7pT5nPY18IA_6ACZMGdg11OHhT0exQEEYLA0Fh_nyU8InJ1XZGcz5ZOVtpx4SXP-psl9RDTgrimraJjDWzksQnltuk-Q_7sK44JnNU14BCEChQJUc7x4zDysWuoIbzsq_wjY3uVhT27HX0TxMbC7uDfMJK3bIB443oNUZofI7OrHL35Bued507EWn47rkK8MrzDc18iNaDijYfLL9_TTasZPAnb-N0z8BubufE8zcKjIk35YrFyJ9EdhXwFWM0mT9aLzxrxNQK2KISBmw_VYRJSszpnl9FgZsd4LRQ4OuMJvEua7Y_wAPTXDWUjqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r14jwSrGPF4lDY4x-Lr8A2nlet_8fZ_-ETfwWlpX5jtyGRmPxvsKgnxZd1MgIe-oZ08hxQV6zFRXp6G4ZoScq1oym3FTH5_ZLG3_4cU6JQ8ORY5O4RS-eueoU8CAZ08dnHFRI6ExJzA-2AfiYK60ClJI-Yq7_wyfPr9uvtlwGbEga8jq4rzSK2sjKcLiH6Az8B-TwK6LHhxrtahm_D9LBm3mL2LERNEI4voq787fjofmrRVq5jhcktiJfdOp9zwQh8If3THAU7pHX1cFs0hqdSdKLQv55CucIGox0xjNylMe5g2KWxFkUb3JnJ2kk962yOKUsIXuXWVuSdHXAGQ9Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QESGHYCVrsIuQ9pP8keBD0qgbKF377VccnfgHAXek9ZqJY15k_NBFDdgALyBwJlsUEJwFbrTPVss6ySHiZNEVhzx0_udY9B7otx03H6mmdBABtHLn12Cfva0hEcHC8g484zaw32PT8ka2ZzlvItUE4LPYIO3__vjLWGhs7mc0ovP-_LnmcwNqzbo2lS9Eqdv0kavFLMcwxaRmfQA9IIgsolXy6oT-IdIWbQ1ye3p-8lLYXUuptb4kh76QQaX9z86dMtyXS06Rg-oZey2vDewFVR_WHRige-lL8le4-XC9Qcn7sMPydiBudcGcch6LOWH1RVnBg63EH_7O80X8HYK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=loqhU4aeiBC3ayCUK6SMWxy5hY0k513JF7FUtpwXuhW6LM7jXkrjOAoENJHk0UKVt1oKw2MvH9-iCheAcwXEwSUNtEKYh3kKabbdHH9IoOQs4fF7IDXLEsVBl5hR3DQSejSt3Vapl1mVj5H20sKsYeFSab5gu0SHxXVhC99sdKXW81tt5_9q0Tn0MS00RNNSK9ZGCVHxxsijt7ekWBXvwOwChlsjlKyRPSvytPluNKlxmQFRTtsH0l6o4YtGt08qeyVXSAyTFclqGsi_GSoPBEj4LYF5FMU8FRkufVYBoDPqGBHqD5swSIq99iFBkgYa3zSzTJs1YV8TZHICh71JFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=loqhU4aeiBC3ayCUK6SMWxy5hY0k513JF7FUtpwXuhW6LM7jXkrjOAoENJHk0UKVt1oKw2MvH9-iCheAcwXEwSUNtEKYh3kKabbdHH9IoOQs4fF7IDXLEsVBl5hR3DQSejSt3Vapl1mVj5H20sKsYeFSab5gu0SHxXVhC99sdKXW81tt5_9q0Tn0MS00RNNSK9ZGCVHxxsijt7ekWBXvwOwChlsjlKyRPSvytPluNKlxmQFRTtsH0l6o4YtGt08qeyVXSAyTFclqGsi_GSoPBEj4LYF5FMU8FRkufVYBoDPqGBHqD5swSIq99iFBkgYa3zSzTJs1YV8TZHICh71JFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XArEbtSgdIh8s-QjoBAH617aYv2nwA8IwQilt-9BWjK-YCYIqhkH93JxqXxGi4CmYarR5QQZN6y6XvT2JVYOfwvfdI-ZouzabcSOMyWIW-rxMvTwBxBQ6H6dJyhKbTkJ3tq9QQaWWdEluJ_LWAFVFq8KNk8UmrhG6snQUQ_Hrlnw1Y1mwPh-e-TngItaYa0T2iR1BN03icv-Yg8ydxB8uaCnyhAY9kRfzdageY20jbBBhIIYkGijA9T_QNmpQUM2LM6pjQGI47r2SFED6qYZfgjP1Jo9F2ZFocf46NEzuIYwGiC_Wh1xR5pVmg0i2Lbi2fIN27jclnXC03f0NKe9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f49cXWmlG9tvcGOaIpVhufHPlRxyFw5mInlqlHLLbOIlWe1BcCNtYz7cw-Y0jy6Ll1COeGJn3r42l2cynKH9qrX8QLKDihnsZV6X2kihibBq0-rBj2E8xIkRUZZhEtkAJMMmDtrGXaz4WyuZLRfR9rB2LJjueiF9HifKaYbnPFiiWsbl-EYDUY77SfNS1DavmZmduwXh0iU49Qbv2umN3AFx5sDb2dEg8zsD_P4bPCekwm2XFhYjOhtitAX40xOJ4wRwzoFWoY-FeRu9KJcFbElPSTF4mi0DgqoKjUSh87ZHqL4AtdzUAQZrvb-8voHiF5wuBMP590gKNyAu_OPRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W2fRsTo2-4biuc6ikwWYjzz1SORu2xzFz9hEJ8pVJmzAXrC0VAoOcC83mhh5mnl9vyEqVfroPwHT8BrRkXMBitTf5Z7dBuv3qSiejWmXmXulQeDQoRpIuFEHLmKqPm9Kn4XdGU4YmdRcxFvEBfJ7C2VHizCwwmM28gFxhRhEID44yQgqs1K0EpDOLeUw2dF_Te6HXokEg5EtW2b1ytW1IOyLZiV5YrbfuOvvl0Q1fxV1tJw5z0WfVc2J5YklrtKEcotf9f8uTiP1Zp5MvFQUfqYo_iR3QsYg7_-9vPCMiX3mZ8c4mIoi5psGsMkkzx6OPINN4xpwEgmHpLjN_wlpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=MLnRoJmL8g3OnMMZIMlxY22KMzkYF5_-9StYWrWpZ3XWaEAPrRgowmCGijyr9ciAmlvqN64TaW1gl_SFdg_nkhTtDqX8XYVnExMGidRdvXSiY-dhTImice8_pqbsUSwktVivD7KosI4oNpc56NtWF1yJMQY9tX2nzPfA6jOcDJY1wDWnoCWkr1JAmbngmUYBe8WU8ID_aW6exoQqDVLAgaGbwwTKoM6x0vjgtE6HIAx0MN6D-wL4XLoZFJ3sURgIbVncj5nEgHGNe7eKbXmwJJA5ymGjHGyS6DE8i7Gy56Gy81TStDLyn9QJhIRaz0-gRiLrOKQjuS6vGzFi6YK12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=MLnRoJmL8g3OnMMZIMlxY22KMzkYF5_-9StYWrWpZ3XWaEAPrRgowmCGijyr9ciAmlvqN64TaW1gl_SFdg_nkhTtDqX8XYVnExMGidRdvXSiY-dhTImice8_pqbsUSwktVivD7KosI4oNpc56NtWF1yJMQY9tX2nzPfA6jOcDJY1wDWnoCWkr1JAmbngmUYBe8WU8ID_aW6exoQqDVLAgaGbwwTKoM6x0vjgtE6HIAx0MN6D-wL4XLoZFJ3sURgIbVncj5nEgHGNe7eKbXmwJJA5ymGjHGyS6DE8i7Gy56Gy81TStDLyn9QJhIRaz0-gRiLrOKQjuS6vGzFi6YK12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nI7dpbfgC_Y2zjgFNoCQ5LEZiNYie77mD8tmUEGa8GxeVZV88YNtiHJXcYXUa_MpjmRweBdoJM6d8cTRvWkmC9XEQXlUkS9vZWichSePa-IuDyLupMuYTJkkrsJ4151JP6AOL60ywx4HItj4FHfFc9glZ8GVqRHBsi6kc2qlQESpxcrDVg63ivx-a3B_aKBFZXzxCJwOfbcKHVePggj9RUd8SjlUou_XZfDAHBDF72DVc_wuAmLzzVe3VM7V6BuCgwQNB673qtPV-5IPbBk0hHhXavAvsS8ZC2NDGq6GcdqSFJiq7D8RTz7_n2_EfG9-zuOkPJJUyQlgzPxqPPyJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X55boiv4rjcgOmRxUQTmXEMX9XkMMCM7pvt28JS2EVWSIs6oE8RrdP1LMWHHumiHozWKxaiuVJqg3hVOGkNs3j6ViUgJp0Dpw4cgIADar_JF8XQNP-QJalkBqs_aMzPNwd2ILQxiNsK4fgk1gITaXPCo_yuXQG9Tz2JZIkwiK6zSO6U4WImzmqjbieojGQlhYqXL_yhDhc3klximE-ZN4oZDky_RaRe4K6yD-VdqnzmH1tDjPPnAdJ6KrKtqfT2Fc0RFmHcDETolc7XfZ7xIqRb8WP7VavTymJlgzOJR3DYXc9wgmZq_y7muzLJ5NKQjOm8dYb3D32gEHzUG9-Dzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=NZBN8Z73vC3K4OJ-4gXZbv_QSRqTFceLHe5AfA4DCCw95Q9wnNS6n8vaecFWqv27sesCj9U2OYzFR_gaK9BxX_P6DfzcRGNNt2qbytzM2rjP6l5VUc52yXLYpvvnJXXIfzGWobZD6RjQKmmPOUdBSFYl7NRmMt5DqWmFHnWpdi535H_MfcFLv_tEerYWKIKAT3z4--xqYhaPOtvVGnsi9TE_Pn-d1PpzU2bJT5mBHU_u9Bji2tehlOX2SG70QLRMeBF1E78fNFyeFio70KRRc32VyoNzPbMn6GfuzPwEgcnQGN4PRu7SXBQtT8LZZCyNQs_M0w4MRneGLAzqXbiPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=NZBN8Z73vC3K4OJ-4gXZbv_QSRqTFceLHe5AfA4DCCw95Q9wnNS6n8vaecFWqv27sesCj9U2OYzFR_gaK9BxX_P6DfzcRGNNt2qbytzM2rjP6l5VUc52yXLYpvvnJXXIfzGWobZD6RjQKmmPOUdBSFYl7NRmMt5DqWmFHnWpdi535H_MfcFLv_tEerYWKIKAT3z4--xqYhaPOtvVGnsi9TE_Pn-d1PpzU2bJT5mBHU_u9Bji2tehlOX2SG70QLRMeBF1E78fNFyeFio70KRRc32VyoNzPbMn6GfuzPwEgcnQGN4PRu7SXBQtT8LZZCyNQs_M0w4MRneGLAzqXbiPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7evXiSNYCRWnQBiEyeltlAEGejIBhSwk988rgQmu13m2cObn5sXIwk3ssA2fLal3SB30AV8OkKmNxTmIHl2Z3rl32COZpHQjeaxtft0-u_yImZla_rdMLYkgHrmBb7bfQCB5mCqYzpJqzK_EY6wFj3mZwx-dyTvtbqqeRjxWoYg8o2DU1J_Ed8H3ICyDUIO-dk9UFah54fwGnBG5HquSTa2uCfhG0H-hMVUGb9K6QI-PYYdgPYekkt-CXaRg5UjJwOkT-FNAWgOSNzpC3tgU5e08Fnmin-faVMVa9Rg7tVlQ15dMHhcwkhBQyFNZGq0uFnSWKNgNHUYqcHdNbUKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/URdoCxOkMMxQS7P85R7xuknQdIhsw54Wq6UZeBOYWAiZP5X6LVbkR71PzdrLC6DTht22AA0hPjhsbL5qX_KnfUUGR-74CwOwBpOn8502gQgqvfTmoa_KC64RLkwCAT3LPME7GYLbcBReouMqPGMDTij411nUsINEoLSbhqbTPnoNyXsGWx9WqWGE8krF829M_66CFYRZD8qARBnRweHRNglLMXRo--akE8kJP84OMTT3mExYbVuprW3Tdx4ZKLLZdON0Lb8RgQ7rtUTGRpCsfBcDEtljEXasr_6jimkH-THvlRrJavpRlh1zXz2gZ9PSwnwXVNShn4mCekEuMrUvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UODYY6vLM_aPeOI8GaafuPmBwELt9LA3n3fvgvce1NR8VOzRJ78o8ivt2fS8GAVT8sBqA4o-Pe3q2egXx7aAt0GhdYPkCPNn-A11NFmwmbNX2eRm_dLzwzi8ocaA38UbDtGsCp_ShDL-o1kxllpnHCGl1EGGD4IumjHO_50Vtbdf8gv-l6nsVk16y5KHuQpXISLwT5265yC2As8qPGx7KT6dGC3ZBrxGDi4uczvPPbFlGlFcmFWXMagD6C9tphkoiv8-KAIX_y2AAnkee21_M6FIzCqdPbCwVMA4AB8fmA5lNiEiOiUM7MrLEOm6wc7zcxTckcW2givq0TFYK5xuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuezIUoDrkCba6sHV-3Jk8z4or4KkIEMa02TTJdzOuf7VnJZgMZEEO2-epA0j1MKYPKuw_L6uXelDGg1GpAhCerGCENawWyX5GEWAH3IYNmxvsP4woMKuYkg54p9FlTEfjg2VTKIqr_WIxZRK2HYCAzcvI0mZO_BRtiiNFX56iMHQIfSNKHVrlb_bn2nABYpGvy5Nj9_AuzCqFEJJt6W7rE9zJTRl2Twl_z_E3MWqwb55KJdKeKF3Kq1iRrhS5vTar06X65hnTbZZSsd4LRJ7b88up6yDzc6GKDY2aLJfBGARQSwD3iA527tm2hUkR0jBCb_vfHkiQvvvBjiBAKokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احکام منسوب به مجتبی خامنه‌ای برای انتصاب شش فرمانده ارشد نظامی؛
بازگشت رسمی حسین طائب به قدرت
دفتر رهبر جمهوری اسلامی روز دوشنبه ۱۹ مرداد خبر داد که مجتبی خامنه‌ای احکام انتصاب شش فرمانده ارشد نیروهای مسلح را صادر کرده و خواستار آمادگی برای «عملیات تهاجمی پرقدرت» علیه آمریکا و اسرائیل شده است.
بر اساس احکام‌ منسوب به مجتبی خامنه‌ای، علی عبداللهی که فرمانده قرارگاه مرکزی خاتم‌الانبیا بود، به عنوان رئیس ستاد کل نیروهای مسلح و کیومرث حیدری به عنوان جانشین رئیس این ستاد معرفی شده است.
رئیس قبلی این ستاد عبدالرحیم موسوی بود که ۹ اسفند سال گذشته در نخستین دقایق حملات آمریکا و اسرائیل کشته شد و ستاد کل نیروهای مسلح ایران در حدود پنج ماه گذشته بدون رئیس به کار خود ادامه می‌داد.
موسوی تابستان سال گذشته جایگزین محمد باقری، رئیس پیشین این ستاد، شده بود؛ باقری خرداد سال گذشته در حملات اسرائیل در ابتدای جنگ ۱۲ روزه همراه با شمار دیگری از فرماندهان ارشد نظامی جمهوری اسلامی کشته شد.
مجتبی خامنه‌ای در حکم صادر شده برای عبداللهی خواستار «تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیا» شده که به گفته او «تدبیر» آن در زمان رهبری پدرش آغاز شده بود.
او همزمان با انتصاب عبداللهی در سمت ستادکل نیروهای مسلح برای فرمانده جدید قرارگاه خاتم‌الانبیا حکمی صادر نکرده است.
احمد وحیدی که از آغاز جنگ و در پی کشته شدن محمد پاکپور، فرمانده‌ کل سپاه پاسداران شده بود، روز دوشنبه بر اساس حکم رهبر جمهوری اسلامی درجهٔ سرلشکری و حکم فرماندهی این نهاد قدرتمند نظامی، امنیتی و اقتصادی را دریافت کرد. او پیش از آغاز جنگ ۴۰ روزه، جانشین فرمانده‌کل سپاه بود.
احمد وحیدی از اعضای ارشد و تندرو سپاه پاسداران سابقه فرماندهی نیروی قدس سپاه پاسداران را دارد و به اتهام دست داشتن در انفجار مرکز یهودیان، آمیا، در آرژانتین از سوی اینترپل تحت تعقیب است.
او به جز مناصب نظامی، در دولت ابراهیم رئیسی، رئیس‌جمهور سابق ایران، به مدت سه سال وزیر کشور بود.
در حکمی که به نام مجتبی خامنه‌ای برای احمد وحیدی صادر شده است، رهبر جمهوری اسلامی خواستار «ارتقاء مستمر و همه‌جانبه‌ توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن» شده است.
بر اساس حکمی جداگانه، مصطفی ایزدی نیز مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفته است.
مجتبی خامنه‌ای در حکم دیگری علی عظمایی را به عنوان فرمانده نیروی دریایی سپاه منصوب کرده و او جانشین علیرضا تنگسیری شده که فروردین ماه در جریان جنگ ۴۰ روزه کشته شد.
مجتبی خامنه‌ای حسین طائب، رئیس پیشین سازمان اطلاعات سپاه، را نیز به عنوان فرمانده سازمان بسیج معرفی کرده است.
از طائب که کار امنیتی را از وزارت اطلاعات آغاز کرد و سپس کنار گذاشته شد و سپس در سپاه پاسداران نهاد اطلاعاتی موازی ایجاد کرد، به عنوان یکی از اعضای حلقهٔ امنیتی و سیاسی قدیمی اطراف مجتبی خامنه‌ای یاد می‌شود؛ حلقه‌ای که سابقهٔ آن به بیش از دو دهه پیش باز می‌گردد.
محمد سرافراز، رئیس اسبق صداوسیما، دربارهٔ نقش پشت‌پردهٔ مجتبی خامنه‌ای در تصمیم‌سازی‌های سیاسیِ مقام‌ها، سخن گفته است. او که خود در مقطعی عضو این حلقه بوده، از ارتباط مستقیم مجتبی خامنه‌ای با حسین طائب یاد کرده و گفته او به گزارش‌های امنیتی طائب علاقه‌مند بود.
او در تیرماه ۱۴۰۱ از سازمان اطلاعات سپاه کنار گذاشته شد، اما بر اساس گزارش‌ها یکی از چهره‌های مهم و نزدیک به مجتبی خامنه‌ای به‌شمار می‌رود.
مجتبی خامنه‌ای در حکم خود برای حسین طائب گفته چند مورد را «مورد انتظار» خود خوانده که یکی از آنها «تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن» شده است.
او همچنین خواستار تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت حامیان جمهوری اسلامی که از ابتدای جنگ ۴۰ روزه در تجمع‌های خیابانی حکومتی شرکت می‌کردند برای «حفاظت از انقلاب اسلامی» شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77803" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77802" target="_blank">📅 18:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0943082a05.mp4?token=uQnwX4zqVXrxfYYlmcc5DpG0edZBqvPvJ7HcT_HCaNxDMfviqhzr4Uci7qA7mpetsHoAcxqsr508oj8pAusNdOxPNBzDSll0SlT_qaZUw3yxO1t6FxUWDSlnJKopcVU0XxDrZfGcjr2Z2Z0hn8hN76P2zX96RtFJLHk1dStsQujo9W7M2vCxmbqFMRIkYdtiBnpUYWEfHxsAM47zBeLXM4z2CJHYKN6vEaXjMiI7_xfDN_Td3MebF9NB6_m0bGnaS7dbf7ep9U1P73OZftBXY72akfS8CFZwzBGJROsBwDoOOTVaSWCoUG2d42_TdO7pqs9rHMj-byil-honczu4Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0943082a05.mp4?token=uQnwX4zqVXrxfYYlmcc5DpG0edZBqvPvJ7HcT_HCaNxDMfviqhzr4Uci7qA7mpetsHoAcxqsr508oj8pAusNdOxPNBzDSll0SlT_qaZUw3yxO1t6FxUWDSlnJKopcVU0XxDrZfGcjr2Z2Z0hn8hN76P2zX96RtFJLHk1dStsQujo9W7M2vCxmbqFMRIkYdtiBnpUYWEfHxsAM47zBeLXM4z2CJHYKN6vEaXjMiI7_xfDN_Td3MebF9NB6_m0bGnaS7dbf7ep9U1P73OZftBXY72akfS8CFZwzBGJROsBwDoOOTVaSWCoUG2d42_TdO7pqs9rHMj-byil-honczu4Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز دوشنبه ۱۹ مرداد اعلام کرد دیدار اخیرش با مجتبی خامنه‌ای، رهبر جمهوری اسلامی، «حدود هفت ساعت» طول کشیده و به گفته او «از هر دری گفتیم».
مسعود پزشکیان در گفت‌وگو با تلویزیون حکومتی ایران گفت: «تقریباً حدود هفت ساعت خدمت ایشان بودیم و دربارهٔ تمام مسائل کشور توانستیم گفت‌وگو کنیم».
از این دیدار عکس یا صوتی منتشر نشده است.
پزشکیان در ادامه درباره وضعیت جسمانی مجتبی خامنه‌ای اعلام کرد: «از نظر وضعیت سلامت کاملاً سالم بودند. کسی که می‌تواند هفت تا هشت ساعت بنشیند و بحث کند، نمی‌تواند از نظر سلامت مشکلی داشته باشد. بسیار راحت حرف‌های ما را گوش می‌دادند و بحث می‌کردند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77800" target="_blank">📅 17:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTzcka5qUEPsikd3H_HiMsAQWOsXgO-A8yZf7CQcCg2a10FnzU1E3JiGgBzFi_1FH9dAyMJ7VxoK2eMoD4X7aQ6o4oEbD0O8GjPMWKIKl4-3kIW16n8coB_KSiXXExaAK7kd2SziJKD5JEEPFBi4LDEUT7Rqm9UMepI5NUfrlRUUKnN1EQjhh7Kuxp1FyDBLa2n_r-_3H3-EFr2kEBJZBp_LqSj9rcH_rFHACcbXozDg7psgnZpZ0edzsBAUUXIHIhkMrwHE_ChdzwztI4kR_yQdUHNJ4_QcHvZTZHHyngwjBD_UuvNQMkFtZbF4M7LFxqdUC6-dPkuO6zzVs8Hw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، یک کولبر ۲۵ ساله بامداد دوشنبه۱۹مرداد۱۴۰۵، در پی تیراندازی نیروهای نظامی جمهوری اسلامی در منطقه مرزی «هنگه‌ژال» شهرستان بانه جان خود را از دست داد.
خبرگزاری هرانا به نقل از کردپا، هویت این کولبر را «محمد توحیدپنا»، ۲۵ ساله، فرزند عثمان و اهل روستای «وزمله» از توابع بخش سرشیو شهرستان سقز اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77799" target="_blank">📅 17:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJbWaOD2PxCjDV-7YPrcT4CYJMS7CbXRY1NwfqnQ5QpZZ_3KIuE4AYOKiqv01OBNF0LjutKrecRIxcRa7W_WykAdjeXF6g7-hyo2bHlDIOYDXmHGnmVUmx6l-r_5HZ3saU5BAfzVuR0h027aRWlj44-dwbfg2kBiAqaWrHgeUD379_rr4AZIxz4KgYuz3uEoUZvwi2MP7x18qbUVAJ38gpKyvAZ8dVuGSKITd5xCgM5UjrLe5U4NiR4W4quiz-3y-cGxzM3k8Hl_MLDw7fFKPJuhQOyem0I7ZvsgSAXmPXRG9JxfiA5s_UrRmJ2TbGm9-E40mZGeo_UJOj8wsVL-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، یکشنبه بعد از ظهر به وقت شرق آمریکا با انتشار نموداری در شبکه اجتماعی تروث سوشال، به کاهش ارزش پول ایران واکنش نشان داد و نوشت: «۵۱ سال رفتار بد!»
realDonaldTrump
در تصویر منتشر‌شده، با عبارت «ایران هیچ پولی ندارد» تاکید شده است ارزش یک میلیون ریال از حدود یک دلار و ۱۱ سنت در سال ۲۰۲۵ به نزدیک ۵۳ سنت در سال ۲۰۲۶ کاهش یافته است. ترامپ توضیح دیگری درباره منبع آمار این نمودار ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77798" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAU6TdvI-tRd9GcKDcus2Xyxy3FMGx66u3mz3_DKno4Xa4wU8uOuLka5ftE8AyjCti5obf_24M-3-yPRT99J45fvr4xDI1qBWBIkYfkdVvNXiL2brmFjJTqwpI3bHAuxeWgG44zgd9Mwn7c2rQuFet91G5QWaPUiNIo-DsxeciHzxlnw_PIq_HUcritcKcyH_D65uMaXJanhG8IRky45ZZlvjZWH3dr7CU1V5zZ3Svz55yKw2N-Vc3eIB5EO8XNPoCfzgy9M5QBLNBoZfN1CQjfezPhuWJKktTIqr09kl1R8CzxQ0xIV-Lf2DWaJMNQeMFU72K6MfbQU_gohYHCXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/evOLV0-h5A9jSR0UO7-i9htuqAPDw7uJovFKPf43i2RO5MFQ71TvZ_2TwrWmGsV3-PFuxippyViQKN-iJRoso-pCh5qh2_G4259MJxn2Y-E0qhq8rc4l6siDDQzrh2gQ-57ITlmf2tHrTam7N2AIpyXYuuxpYD-LGpNUhL1yNgic5D1fvW-mP6eB3_bFTrF33VelRz5J4Ax8ZP4tmE4U5zta49MFSQCo2G-YBKVoI4IBKG0-SW8727WHryfNcqacCwyvBxoslLv7RacgB3A7a9V6OX4giZS6rjOmzBNwmrUqw3r-mS4tKI8sYehiHO5BQCVGUqoUrisKSpKfKXJDnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بحبوحه گمانه‌زنی‌ها درباره استعفای محمدباقر ذوالقدر از دبیری شورای عالی امنیت ملی، روز یکشنبه ۱۸ مرداد ماه، پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در خبرگزاری حکومتی تسنیم منتشر شد که در آن محسن رضایی به عنوان «نماینده رهبر» در «شعام» (شورای عالی امنیت ملی) معرفی شده است.
در ادامه این پیام مکتوب، بدون اشاره به استعفا، از محمدباقر ذوالقدر «تشکر» شد.
این خبر در حالی منتشر می‌شود که از دو روز پیش اخبار غیررسمی درباره استعفای محمدباقر ذوالقدر از مقام دبیری «شعام» و جانشینی محسن رضایی،‌ منتشر شده بود.
خبر انتصاب رضایی در شعام، صبح یکشنبه در خبرگزاری‌های رسمی ایران منتشر و کمی بعد در بسیاری از آنها
حذف شد
.
آخرین گزارش‌ها از فعالیت ذوالقدر به عنوان دبیر شعام، مربوط به پیامی منتشر شده در روز شنبه است که بازگشایی تنگه هرمز را به پذیرش ۶ شرط جمهوری اسلامی از سوی آمریکا منوط کرده بود. پیامی که بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت و تلاش‌ها برای بازگشایی تنگه هرمز را با ابهام‌هایی مواجه کرده بود.
@
VahidOOnLine
🔥
رجا نیوز نوشته:
در اعلام بدون تاریخ این حکم نشانه‌هایی است برای اهل اندیشه...
🔄
آپدیت:
کانال خامنه‌ای نوشته به ذوالقدر پست مشاور سیاسی  رهبر جمهوری اسلامی داده شده:
📝
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
💬
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔻
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
✏️
بسم الله الرحمن الرحیم
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر
باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید.
✍️
سیّدمجتبی خامنه‌ای
🔄
و در نهایت حکم دبیری رضایی صادر شد:
معاون ارتباطات ریاست جمهوری:
محسن رضایی دبیر شورای عالی امنیت ملی شد
🔥
اما بخش جذاب ماجرا
محمدباقر خرازی
است.
او پیشاپیش گفته بود ذوالقدر می‌رود و محسن رضایی جایش را می‌گیرد.
درست درآمدن خبری چنین مشخص، همه ادعاهای خرازی را ثابت نمی‌کند؛ اما حالا دیگر دشوارتر می‌توان گفت او از پشت پرده قدرت هیچ خبری ندارد،حتی اگر خودش مدعی باشد کلیپ‌های جنجالی‌اش را هوش مصنوعی ساخته است.
@
pourostadv
🔥
امیرحسین ثابتی (نماینده انتخاب شده برای مردم تهران در مجلس شورای اسلامی) علیه پزشکیان با عنوان «علی الاصول ۲»:
پزشکیان مقابل خواسته مجتبی (رفتن ذوالقدر و آمدن رضایی) ایستاده بود.
علی الاصول ۲؛ انتشار حکم محسن رضایی توسط رهبرانقلاب
با آشکار شدن حکم نمایندگی رهبرانقلاب برای محسن رضایی در شورای عالی امنیت ملی، یک مساله دیگر آشکار شد و آن اینکه مدتها پزشکیان به عنوان رئیس این شورا در مقابل این خواسته رهبر انقلاب (رفتن ذوالقدر و آمدن رضایی) ایستادگی می‌کرده است.
به لطف خدا، تقریبا همه چیز برای مردم آشکار شده و دیگر کسی فریب "همه امور با رهبری هماهنگ است" را نمی‌خورد و اتفاقا مردم فهمیده‌اند کسانی که تحت پروژه وفاق و با چوب وحدت، میخواهند مردم مطالبه‌گر را سرکوب کنند و مقابل دوربین همه چیز را گردن رهبری بیندازند، در عمل خلاف نظر ایشان را عمل می‌کنند.
آقای پزشکیان! حرکت در مسیر رهبری با حرف زدن نیست، دست فرمان‌تان را تغییر دهید تا مردم تغییرتان نداده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/77795" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwvoTyyqjC9tB8WIKZ23-KMmskb8RE_YHwJ5njwa-ISBiggWmns5Ajj04DqBotjqZB3t9yZamS7yKyXHENKQ2VJqljKnZEL-4k755af0VdEd3HogA_XIbfYYeK-Q8SKBdqJ2g0fodV0F3HJSiXbIDMoN_vRuhj6Bmreg0JhkDrWlPtWohnq0YtRE2UHaKIUPpk-ANqmmYyJVN__vNNbFdwV86BfyJCZo_ZQQemzciUfiPepY2O-pGswnKwHrnKEPYgAsbhNnwYnliup5JvFz43yp3ONa-DbLgM3qlNfFGOBzZpq4MmcoUiJzN1_ZvSCALhu3w_Kq7WgtFFRLGHEHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس: درباره ایران «داریم قضیه را کم‌سروصدا پیش می‌بریم»
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، روز یکشنبه نشان داد که آماده است اجازه دهد فشار اقتصادی بر ایران افزایش یابد — به‌جای آنکه دستور یک حمله نظامی تازه را صادر کند — حتی در حالی که این کشور همچنان در برابر آمریکا سرپیچی می‌کند.
چرا مهم است:
تنها یک هفته پیش، ترامپ در آستانه صدور دستور بازگشت به عملیات رزمی گسترده بود. اما او در گفت‌وگو با اکسیوس هیچ تهدید نظامی تازه‌ای مطرح نکرد.
▪️
ترامپ همچنین از اینکه ایران اعلام توافق با عمان برای بازگشایی تنگه هرمز را به تأخیر انداخته است، هیچ خشم یا نارضایتی‌ای ابراز نکرد. ایران روز شنبه فهرست تازه‌ای از خواسته‌ها را برای اجازه عبور کشتی‌ها از تنگه مطرح کرد.
ترامپ چه می‌گوید:
ترامپ در یک تماس تلفنی کوتاه گفت: «داریم قضیه را کم‌سروصدا پیش می‌بریم.»
▪️
«ما فقط یک‌جورهایی، نیم‌بند با آنها مذاکره می‌کنیم. فقط داریم ایران را تماشا می‌کنیم، با آن تورم عظیمش و این واقعیت که هیچ پولی ندارد.»
▪️
او تأکید کرد که ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت به نیروهایش ندارد. ترامپ گفت محاصره دریایی آمریکا بحران اقتصادی حکومت ایران را تشدید کرده است.
▪️
در عین حال، ترامپ گفت با کاهش قیمت نفت به اندکی بیش از ۷۵ دلار در هر بشکه، مصرف‌کنندگان آمریکایی فشار کمتری از جنگ احساس می‌کنند.
▪️
ترامپ درباره کش‌وقوس با ایران گفت: «درست می‌شود. همیشه درست می‌شود. مثل یک بازی شطرنج است.»
اصل خبر:
توافقی برای تنظیم تردد در تنگه هرمز میان ایران، عمان و آمریکا مذاکره شده و چند روز است که در انتظار نهایی‌شدن قرار دارد.
▪️
بر اساس توافق جدید، ایران کنترل بخشی از تردد در تنگه را به دست می‌آورد — چیزی که پیش از جنگ در اختیار نداشت.
▪️
میانجی‌های قطری و پاکستانی مطمئن بودند که توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان چشم‌انداز آن رو به افول گذاشته است.
▪️
مقام‌های آمریکایی همچنین می‌گویند اختلافات درون حکومت ایران رو به افزایش است. یک جناح به رهبری مسعود پزشکیان، رئیس‌جمهور، به‌شدت نگران فروپاشی اقتصادی است و معتقد است ایران باید با آمریکا به توافق برسد. جناح دیگری به رهبری احمد وحیدی، فرمانده سپاه پاسداران انقلاب اسلامی، هرگونه امتیازدهی را رد می‌کند.
وضعیت فعلی:
محمدباقر ذوالقدر، رئیس شورای عالی امنیت ملی ایران، روز شنبه شروط تازه‌ای را برای بازگشایی تنگه مطرح کرد — افزون بر شروطی که در توافق عمان درباره آنها مذاکره شده بود.
ذوالقدر در بیانیه‌ای گفت
برای بازگشایی تنگه، آمریکا باید:
▪️
«هرگز با هیچ زبانی ایران را تهدید یا به آن توهین نکند.»
▪️
«جنگ علیه ایران و متحدان ایران در لبنان، غزه، یمن و عراق را برای همیشه پایان دهد.»
▪️
محاصره دریایی را لغو کند و نیروهای نظامی را از اطراف ایران خارج کند.
▪️
او همچنین خواستار پرداخت کامل غرامت خسارات جنگ، لغو همه تحریم‌ها و آزادسازی تمام دارایی‌های مسدودشده ایران شد.
▪️
تا چند هفته پیش، این خواسته‌ها پیش‌شرط دستیابی به یک توافق هسته‌ای بودند. اکنون ایران آنها را صرفاً به‌عنوان شروط بازگشایی تنگه مطرح می‌کند.
▪️
یک دیپلمات از یکی از کشورهای میانجی گفت بیانیه ذوالقدر بازتاب‌دهنده کشمکش سیاسی درون حکومت است.
پشت پرده:
مقام‌های آمریکایی گفتند ترامپ یک هفته پیش متمایل به ازسرگیری عملیات رزمی گسترده علیه ایران بود، اما متقاعد شد که فعلاً تنش را کاهش دهد.
▪️
یکی از این مقام‌ها گفت ادامه درگیری به حکومت ایران اجازه می‌داد از مواجهه با پیامدهای جنگ، خسارت‌های واردشده به زیرساخت‌ها و بحران عمیق اقتصادی ایجادشده اجتناب کند.
▪️
این مقام آمریکایی گفت وقتی ایران درگیر جنگ نیست، ناچار می‌شود با واقعیتی تلخ روبه‌رو شود که هیچ راه‌حل واقعی برای آن در دسترس ندارد.
▪️
در عین حال، این مقام آمریکایی گفت هر شب حدود ۸ میلیون بشکه نفت با هماهنگی ارتش آمریکا از مسیر جنوبی تنگه هرمز از خلیج فارس خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
موضوعی که باید زیر نظر داشت:
جی‌دی ونس، معاون رئیس‌جمهور، روز شنبه به فاکس‌نیوز گفت: «این ماجرا تمام نشده است. واضح است که دیگر در ابتدای آن هم نیستیم. ما وسط بازی هستیم و مجموعه کاملی از ابزارها — ابزارهای دیپلماتیک، اقتصادی و نظامی — را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77794" target="_blank">📅 20:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77793" target="_blank">📅 19:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THYDvXVzOZZUw6w6qgIGgwrVcXFhLlO-CQY6SXEXw2s15U39qHrVJ6JPMlqeK2d6hk5iYn9YmFNv_XLI0ttmKZbZ2QkUU9Wh01fRS7EkFNI0f9NL-bJzzSOi7jRSdobYFTVi0W-ceo5-Bd-jA2TimyAfbfC1KBfe7i9iW-uL5IYTorpIg4DTmqx9bKax54qrxVN9le6YVLWetYCiPxOlFkaRiRMHbxuhhJ2l9t7l8Bk-SBD9VhyeNn9cH_ooqP0rWSHcXrvwrm_y3fHkMTv1B8cgUQeCIDIbU-V1ytOaugrYb3GB7brn1G6todz5ZGDLKNrIlnO-kbRTS3M0rhZ13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه اطلاع‌رسانی دفتر رهبر جمهوری اسلامی روز یک‌شنبه ۱۸ مرداد ۱۴۰۵ اعلام کرد پزشکیان هم‌زمان با آغاز سومین سال ریاست‌جمهوری خود با مجتبی خامنه‌ای «دیدار و گفت‌وگو» کرده است. خبرگزاری مهر و ایرنا و دیگر رسانه‌های حکومتی نیز این خبر را بازنشر کردند.
بااین‌حال، از این دیدار نیز هیچ عکس، فایل صوتی یا ویدیویی منتشر نشده است.
پزشکیان پیش‌تر نیز گفته بود پس از انتخاب خامنه‌ای به رهبری، با او دیدار کرده است؛ اما از آن ملاقات نیز سند صوتی یا تصویری منتشر نشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77792" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77791">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X3Jv2SOs9qXJk_zbawIpxvLYs1eGzUlQdbsbXmsTjBWa3wGAEEqalYOCwYbEq2riIXkNYkHIt1vOrtGvqmdDDtkdQ8cSvpkDjcwep-96UqRfJ5WJdaPJg3MUItVmaJcLJL4a47_GFq1H8fDGY-TrAyxhy_vzxh5fBACWPLPOCaXsWz5iok0j8qchHAsjtm9FZJJPZvNHxTdb_2XnWkDpRu4Ju9encRCZEFPE2QtTZIe9I4EdYhsquv1QGrVLt_HYmX4arzLNtJkwxKBnca3AI_OD6mmVKS9ViIzB_-9WsIF9mkpQ2Szto6rBJvR0-2Y6iWbGYJWrNOuKIPyjyawRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری از رسانه‌های حکومتی یکشنبه ۱۸ مرداد از انتصاب محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به‌عنوان نماینده او در شورای عالی امنیت ملی خبر دادند، اما دقایقی بعد این خبر را حذف کردند.
خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از «شنیده‌ها» نوشت که با این انتصاب، محسن رضایی و سعید جلیلی دو نماینده مجتبی خامنه‌ای در شورای عالی امنیت ملی خواهند بود. تسنیم پس از چند دقیقه این مطلب را از کانال تلگرامی خود حذف کرد.
رسانه‌های مهر، ایسنا و جماران نیز خبر انتصاب رضایی را منتشر کردند و اندکی بعد مطالب خود را برداشتند.
انتشار و حذف این خبر در شرایطی صورت گرفت که در روزهای اخیر اختلاف‌ها در ساختار جمهوری اسلامی بر سر روند گفت‌وگوها با آمریکا، از جمله پرونده هسته‌ای و چشم‌انداز تنگه هرمز، افزایش یافته است.
@
VahidOOnLine
🔄
آپدیت: خبر شش ساعت بعد از حذف دوباره
منتشر شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77791" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=WWIvawlHvp008vbocjWPwAwT5j0-tbTZC1HYdJtp45zbu6iB6RVbQcnVsjdw5ezFzicRvNLUulIvf9mAEnr72fZRKvwTwzXWnACtKBeoZE93oYmRix-xRmg4mi9v442mzioap5hueJyflfnle8GBBbC1O-mDGRBeUQHrYR0j3gO0nOaMSdnX02Cf5Km3mBMoIbguBBHXTeKtf98iQoINzti9APGFn7zcQQ0yv4U4XinkS0PPy-N3hMR_1LurmATJfutS3T3OZA_Lx0e8A_jq44hZSEkBrwzS2ksIwxC8bjIJkWACxLmR6uDJAA9EXRo6U5nfuhuvfx9POJfRtubr8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67846c93bc.mp4?token=WWIvawlHvp008vbocjWPwAwT5j0-tbTZC1HYdJtp45zbu6iB6RVbQcnVsjdw5ezFzicRvNLUulIvf9mAEnr72fZRKvwTwzXWnACtKBeoZE93oYmRix-xRmg4mi9v442mzioap5hueJyflfnle8GBBbC1O-mDGRBeUQHrYR0j3gO0nOaMSdnX02Cf5Km3mBMoIbguBBHXTeKtf98iQoINzti9APGFn7zcQQ0yv4U4XinkS0PPy-N3hMR_1LurmATJfutS3T3OZA_Lx0e8A_jq44hZSEkBrwzS2ksIwxC8bjIJkWACxLmR6uDJAA9EXRo6U5nfuhuvfx9POJfRtubr8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در نشست روز یکشنبه کابینه، با رد صریح طرح ۱۵ ماده‌ای «شورای صلح» دونالد ترامپ برای غزه گفت: «اسرائیل طرح ۱۵ ماده‌ای را رد می‌کند. ارتش اسرائیل تا زمانی که حماس به‌طور کامل خلع سلاح نشود، هیچ‌گونه عقب‌نشینی انجام نخواهد داد.»
او با تاکید بر لزوم خلع سلاح واقعی حماس افزود: «منظور از خلع سلاح، شامل تمام تسلیحات سنگین، نیمه‌سنگین و سبک است؛ ما از یک خلع سلاح واقعی و نه فرضی صحبت می‌کنیم.»
نتانیاهو همچنین با اشاره به رایزنی‌ها با طرف آمریکایی خاطرنشان کرد: «ما در حال گفتگو با آمریکایی‌ها هستیم. آن‌ها ایده‌هایی دارند که برخی از آن‌ها برای ما قابل قبول و برخی غیرقابل قبول است. امنیت اسرائیل قابل مذاکره نیست و ما قاطعانه بر سر منافع خود ایستاده‌ایم.»
نخست‌وزیر اسرائیل در پایان تاکید کرد: «تا زمانی که من نخست‌وزیر هستم، هیچ کشور فلسطینی تشکیل نخواهد شد؛ نه در غزه و نه در کرانه باختری.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77790" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y29yKPkuOyk5fD4N9mfCef1Xqw_w77Pg1G7RlNJB5bDQLg0F-Le2PHU9HLvq3cUMfK6vxh2yqVlOCwWQvWPvtDBd3ZtbRVc7Rpp7CyS-zlzHyrnSHeOUBczfvZ9s2CgYRESPTK_6HURN_VgcHc7zTwS7_UirB8tGAsUX6X1BXfSEnDaiMQuWC4VaFIsAnuuItt8wBtI0blNc_6e23UXVAOttJUuKVHhzGnpBYYDHoJpNgtep4fKWI62uke2hG3BhUyWfCjYaiMEXfJDCdepia9vbW3lW_vLIAH-J5ZeTIZl9KbdCvdfAGyMZ5X_e2GvItl4wWh-tzJ7nkCpzK1sgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان امروز منابع حکومتی درباره قتل مداحی که ۶ ماه به بهانه "دعوت به حجاب" مزاحم یک "دختر بلاگر" شده بود تا رفت سر قرار باهاش:
حمیدرضا رجب‌زاده حدود ۱۵ روز پیش ناپدید شده بود اما ۴ روز پیش ویدیویی از پیکر آسیب دیدهٔ این فرد در یک کانال ضدانقلاب منتشر و در فضای مجازی دست به دست شد.
مرد گمشده مدتی قبل در فضای مجازی با خانم بلاگر جوانی آشنا شده و به او امر به معروف و نهی از منکر می‌کرده و می خواست حجابش را در پیج اینستاگرامی حفظ کند و به مسائل سیاسی نپردازد که در روز ناپدید شدن نیز این خانم بلاگر از او درخواست ملاقات حضوری داشته است.
تحقیقات کارآگاهان نشان می‌دهد زن جوان با طراحی قبلی و با دعوت از مرد سرشناس به محله خلوتی زمینه حضور وی را فراهم کرده و پس از رسیدن مداح جوان به محل قرار با تعارف خوردنی مسموم ابتدا مقتول را بی هوش کرده سپس با همدستی 5 مرد او را به قتل رسانده اند.
خانم بلاگر در بازجویی ها گفت : من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و... من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند.
...
تحقیقات همچنین نشان داد این افراد پس از قتل، اقدام به فیلمبرداری از صحنه جنایت و جنایت بر میت کرده و فیلم تهیه‌شده را در ازای دریافت پول برای  شبکه‌ معاند منافقین ارسال کرده‌اند چون تصور می کردند برای این فیلم ها که در آن بسیجی ای کشته می شد پول خوبی می توانند دریافت کنند.
بررسی‌های کارآگاهان در این مرحله نشان داد مقتول با ضربات متعدد چاقو به قتل رسیده و پس از مرگ، با آتش زدن جسد جنایت بر میت رخ داده است. متهمان همچنین درباره نحوه انتقال و سوزاندن جسد در بیابان‌های اطراف پرند توضیحاتی را در اختیار تیم تحقیق قرار داده‌اند.
براساس ادعای افراد بازداشتی، یکی از متهمان که به عنوان عامل اصلی جنایت معرفی شده، ضربات اصلی را به مقتول وارد کرده و پس از آن سایر افراد نیز در این جنایت مشارکت داشته‌اند؛ با این حال، متهم اصلی پرونده پس از ارتکاب قتل متواری شده و تلاش‌های پلیس برای دستگیری او ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77789" target="_blank">📅 18:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHFxl_8zdRJLcLcUJWlMIRC1TPLSe9YnMSZc6r9hE3Fva_2K0kNp85t8hEb5Ms0FdJ4Hk8MM_g10e9MWawExhZpyZ7eczhczzzbIHkeyLbfpyYOg7ux1gcvf9AGpPWMT18ony_uZ6vVD9SxbpyLR5AbTTkQR6TDmO9RkCZEd0IAI9kvZuWP9TEGSvCH4Ia_AF9H6eiuLmom3WLRhlik0KEaCY4dccokuH--B1EzglPPSypfepVD8dw-LvTOjqinUMwZir9zOWgtlUecCNxizQIJj7JqG97AYhjUoEJi5fxAzsuHalbKC9Rkmrs-UWnujxfAgFfsYoUJ5QaJgQpb6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات حکومت ایران در عین اعلام پیشرفت در مذاکرات ایران و عمان درباره تعیین مسیر کشتی‌ها در تنگه هرمز روز شنبه، ۱۷ مردادماه، شرط‌های تازه و گسترده‌ای را برای باز شدن این آبراه مطرح کردند.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه گفت تا زمانی که آمریکا به گفتۀ او «رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد» و تأکید کرد این شورا «چه در جنگ و چه در مذاکره» از این موضع کوتاه نخواهد آمد.
او شش شرط را برای بازگشایی تنگه مطرح کرد که از جمله شامل پایان جنگ و حملات آمریکا به ایران و متحدان جمهوری اسلامی در لبنان، فلسطین، یمن و عراق، رفع محاصره دریایی، خروج نیروهای نظامی آمریکا از پیرامون ایران، پرداخت کامل خسارت‌های جنگ، لغو تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران است. ذوالقدر همچنین خواستار پایان تهدیدهای آمریکا علیه ایران شد.
ساعاتی پیش از آن نیز سخنگوی سپاه پاسداران اعلام کرده بود که بازگشایی تنگه هرمز اساساً «ارتباطی به مذاکرات ایران و عمان ندارد» و تنها در صورتی انجام خواهد شد که آمریکا «شرایط ایران» را به‌طور کامل بپذیرد.
@
VahidHeadline
شرایط شورای امنیت ملی ایران با یادداشت تفاهم با آمریکا چه تفاوتی دارد؟
انتشار شش شرط ایران برای بازگشایی تنگه هرمز، چشم‌انداز بازگشایی این تنگه در کوتاه‌مدت را در ابهام بیشتری فرو برد.
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، گفت که این شورا چه در جنگ و چه در مذاکره «هرگز کوتاه نخواهد آمد.»
شورای عالی امنیت ملی ایران زبان صریح‌تری در مقایسه با تفاهمنامه با آمریکا به کار بسته است.
در یک مقایسه سریع با یادداشت تفاهم، ایران این بار به شکلی صریح خواستار پرداخت «بی‌کم و کاست خسارت‌های دو جنگ» شده است، موضوعی که در نص یادداشت تفاهم‌ دیده نمی‌شد.
پذیرش آمریکا تقریبا ناممکن است چرا که آن کشور را در موضع «متجاوز» قرار می‌دهد و به زبان سیاسی هم به «شکست» تعبیر می‌شود. در عین حال، پرداخت غرامت، تبعات حقوقی دیگری هم به‌عنوان آغازگر جنگ و همچنین اقدامات غیرقانونی بین‌المللی دارد.
این در حالی است که دونالد ترامپ گفته بود که خسارات حملات ایران را از پول‌های بلوکه شده ایران می‌گیرد. این موضع آمریکا عملا نفی ششمین شرط ایران برای آزادسازی تمامی‌ دارایی‌هایی‌هایش است.
شرط دوم ایران هم اگرچه به بند نخست یادداشت تفاهم می‌ماند، با یک تفاوت بنیادین. در تفاهمنامه دو کشور تنها از پایان دائمی تخاصم در ایران و لبنان نام برده شده بود. این بار اما جمهوری اسلامی خواستار پایان دائمی جنگ در «فلسطین، یمن و عراق» هم شده است.
به نظر می‌رسد شش شرط ایران نه موضوع مذاکره که موضع این کشور است.
پیش از این، اگرچه مقام‌های ایران اعلام کرده بودند که توافق با عمان به معنای بازگشایی تنگه هرمز نیست اما رئیس‌جمهور و مقام‌های وزارت خارجه تا حدی این موضوع را به بازگشت آمریکا به تفاهمنامه و تعهد عدم نقض آن مشروط کرده بودند.
حالا به نظر می‌رسد شورای عالی امنیت ملی مطالبات را افزایش داده است، اقدامی که حتی اگر با هدف فشار بر آمریکا و امتیازگیری در مذاکرات باشد، مخاطرات خود را دارد و مشخص نیست که واکنش آمریکا چه خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77788" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJBy6UTQn3S8-oUFbkjCOOjs0wuK5SS3kbTqARiCf4KEHDpYyQbMDw05Xw0nSGiHbiJVVi-1xPpT5rKJgB0LMJPOj_aDEcuk-N-iMiF6SQLEuIzpxipU0J__63AJehJMyE6Le5sGgG-ceGo8yLrQflegK8iTNNe28dNXROMhQ4_BsmHkVdTyF_vEMfWocAVkx162cpI2dnCEs6DsW6sDy9_84akHKgdjT7N3fMR0s8EOAUcMAJqLD8myskx_5lQAXrl41YXKWevPLIK_tVjkKrGBENzJKoz4Z-ngljQKBwIVAw2SCPKsM_u8DVi7bEGm0-LyVBCaYKK7pEnk9ogFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام رسول رضایی، شهروند ۲۸ ساله اهل فریمان و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در دیوان عالی کشور تایید شده است. او پیش‌تر از سوی دادگاه انقلاب مشهد به اتهام «محاربه» به اعدام محکوم شده بود.
خبرگزاری هرانا، روز یکشنبه ۱۸مرداد ۱۴۰۵، گزارش داد، رسول رضایی که در حال حاضر در زندان وکیل‌آباد مشهد محبوس است، پس از تایید حکم اعدام در دیوان عالی کشور در معرض اجرای این حکم قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77787" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=F3yTeCBMN-U58BkOM-r5RUvswuAc2hMk4GNvIl-JGOt_0R40jsIOuEi2wWNv3Crzb-YH8G44nR3rbzl78ffyIx8jQ0B2Zro5bdU0Ot9J56AttWSjvgbA7hN1TY-Um8P_nAkSgtfwexdHQa9P3lTuB8dePXMeQFdj2GPudL2DEcBiCJjpYiUpJVpZC8rgRs4Nn0-9bUXThMRikMXcUrT4d2vOvXJ-gadM7iS32XBXVvHO8O4TEMAyAqJXYWiRsZ_OjjGSf8lJazfrflIsSS0R_v1hIoqrfOtKabNGcNMx1UjgUJgTw2olpv8-8SgcBKcVjYM8zjTKBVnJXj-ntDWsBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/899458cc4c.mp4?token=F3yTeCBMN-U58BkOM-r5RUvswuAc2hMk4GNvIl-JGOt_0R40jsIOuEi2wWNv3Crzb-YH8G44nR3rbzl78ffyIx8jQ0B2Zro5bdU0Ot9J56AttWSjvgbA7hN1TY-Um8P_nAkSgtfwexdHQa9P3lTuB8dePXMeQFdj2GPudL2DEcBiCJjpYiUpJVpZC8rgRs4Nn0-9bUXThMRikMXcUrT4d2vOvXJ-gadM7iS32XBXVvHO8O4TEMAyAqJXYWiRsZ_OjjGSf8lJazfrflIsSS0R_v1hIoqrfOtKabNGcNMx1UjgUJgTw2olpv8-8SgcBKcVjYM8zjTKBVnJXj-ntDWsBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا با فاکس‌نیوز، بخش مربوط به ایران با تشخیص و ترجمه ماشین:
🔻
ونس: ... ما با ایرانی‌ها در حال گفت‌وگو هستیم.
تلاش می‌کنیم میزان نفت و گازی را که از تنگه هرمز عبور می‌کند به حداکثر برسانیم. در حال حاضر بیش از هر چیز روی همین متمرکز هستیم. فکر می‌کنم می‌بینید که قیمت نفت امروز به حدود ۸۰ دلار در هر بشکه کاهش یافته و گاهی کمی پایین‌تر هم می‌رود.
بنابراین فقط تلاش می‌کنیم مطمئن شویم آنچه را که از این درگیری نیاز داریم به دست می‌آوریم.
اگر به عقب برگردید و به یاد بیاورید که اینجا چه کرده‌ایم، برنامه هسته‌ای آن‌ها را نابود کرده‌ایم، نیروی نظامی متعارفشان را نابود کرده‌ایم و آنچه را می‌توان توانمندی‌های نظامی نامتقارنشان نامید، به‌شدت کاهش داده‌ایم.
و اکنون می‌خواهیم ببینیم آیا حاضرند آن نوع تغییرات بلندمدتی را انجام دهند که برای داشتن رابطه‌ای بهتر با ایالات متحده ضروری است یا نه. اگر هم حاضر نباشند، اشکالی ندارد.
ما همچنان هر فشاری را که بتوانیم وارد می‌کنیم و تلاش می‌کنیم تا جای ممکن نفت و گاز بیشتری از خاورمیانه به جریان بیندازیم تا آمریکایی‌ها بتوانند از قیمت پایین‌تر بنزین و انرژی بهره‌مند شوند.
این همان موازنه ظریفی است که باید برقرار کنیم.
آخرین چیزی که در این باره می‌گویم، کیلی، این است که همیشه سعی می‌کنم به مردم یادآوری کنم که واقعاً هنوز وسط بازی هستیم. این ماجرا تمام نشده است. دیگر در ابتدای کار هم نیستیم؛ وسط بازی هستیم و مجموعه‌ای کامل از ابزارها—دیپلماتیک، اقتصادی و نظامی—را به کار می‌گیریم تا مطمئن شویم بهترین نتیجه را برای مردم آمریکا به دست می‌آوریم.
کاملاً مطمئنم که به آن نقطه خواهیم رسید، اما هنوز تا حدی وسط بازی هستیم.
🔺
کیلی مک‌اننی:
ایرانی‌ها هم از راه‌های مختلف این پیام را داده‌اند که می‌خواهند کنترل خود را بر تنگه هرمز محکم‌تر کنند. بنابراین در یک توافق فرضی، وضعیت قابل قبول در تنگه هرمز چه خواهد بود؟
🔻
جی‌دی ونس:
انتظار ما این است که همان میزان نفت و گازی که پیش از آغاز این درگیری از خلیج [فارس] خارج می‌شد، دوباره از آن خارج شود.
ایرانی‌ها به ما گفته‌اند که قرار است همین کار را انجام دهند. کل ائتلاف کشورهای خلیج [فارس] نیز همین را می‌خواهد.
اما می‌دانید، ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف مردم نگاه نمی‌کنیم، به عملشان نگاه می‌کنیم.
می‌بینید که برخی افراد در داخل ساختار ایران درباره گرفتن عوارض صحبت می‌کنند. ایرانی‌ها به ما گفته‌اند هیچ برنامه‌ای برای گرفتن عوارض از عبور و مرور در تنگه هرمز ندارند. اما باز هم خواهیم دید در عمل چه اتفاقی می‌افتد.
آنچه طی حدود یک هفته گذشته در جریان بوده این است که ایرانی‌ها و کشورهای خلیج [فارس]، به‌ویژه عمان، درباره چگونگی تضمین عبور و مرور امن گفت‌وگو کرده‌اند.
البته یک مشکل این است که ایرانی‌ها در آغاز جنگ تعداد زیادی مین کار گذاشتند. بنابراین آنچه اکنون واقعاً داریم روی آن کار می‌کنیم این است که چگونه می‌توان سازوکاری برای تردد ایجاد کرد تا کشتی‌هایی که عبور می‌کنند بتوانند با ایمنی عبور کنند.
این طبعاً شامل مین‌روبی هم می‌شود. همچنین شامل تعهد ایران می‌شود که به کشتی‌های تجاری شلیک نکند.
آن‌ها به‌شدت آسیب دیده‌اند. می‌خواهند این ماجرا تمام شود.
سؤال این است که آیا قادرند—آیا نظامشان قادر است—چیزهایی را که لازم است ارائه کند تا ما راضی باشیم و احساس کنیم آنچه را از این رویارویی نیاز داشتیم به دست آورده‌ایم.
این هنوز مشخص نشده است، اما فکر می‌کنم طی چند روز گذشته مقداری پیشرفت کرده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77786" target="_blank">📅 18:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXv1ZkWFR0--AS_68rQXULoYDxUcgSJZzkTsQm9vNR7tENOh-u-fqxFoR2M456TO_TR_esLatWMxSZKyguC9zwTP2t0ivQVNqpk-t2XxzcGP1iXpe5QHuvklFZdI0r14FRURK-yt83MA-CKlc85uCl64aHkNadCfQEib-3XANHWV5gaWgBwNM4m4IE6sht7GwS9DC132476e1h4hKmDRfhgoGXpFtm60lXI0C6N5Ok4fq7YWUbvYqbX9OwPxDNg22-FYzN6JHDdQsLjhNeT0zgv_uno8GvPUGMPDTtmrWYAxiHsCW_wQkPvbyiAeSgI0uG3vph1qEoIjbY5DNIPi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از هدف قرار گرفتن یک شناور در تنگه هرمز، در فاصله حدود ۱۸ مایل دریایی شرق خصب در عمان، خبر داد. هم‌زمان، امارات متحده عربی اعلام کرد یک نفتکش متعلق به شرکت ملی نفت ابوظبی، ادنوک، هنگام عبور از تنگه هرمز هدف حمله موشکی قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77785" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH7Am1BBqZWSG2yeqPjbDZQ9vOahQuWAuNS2WECPU07p6e4A9o69k4aTduTE7DdFE0uPGxmdVP0jcZJ0qXbGYVPJvU54iqHWk8IPuBQ949yFkx9aezpmUKgHWYwhoRHAI0mVujmfQq_Fg1qqlulIkoLq2hxIRshoZ8owwCdMqn19j1AbkzJw9Rf0dikYSvQHjGFzBw5tLuQfqj4J4jjOl-TlFdAbMH7G7BHrBlELLALBcPG4XzkG99y2IMKuYsm4L8hN69D65v0Y9NwXr_3QiGNuEOWmP8fSbUWisKjPkQozb63FKmc9XIz3RPAX7NiGuPpkcZs1rrYJpHAWZNQ8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، روز شنبه ۱۷ مردا ماه، با انتشار پیامی با تشریح شروط جمهوری اسلامی برای بازگشایی تنگه هرمز، تاکید کرد تا زمانی که ایالات متحده آمریکا رفتار خود را تصحیح نکند، این آبراه راهبردی مسدود خواهد ماند.
دبیر شورای عالی امنیت ملی تصحیح رفتار آمریکا را مشروط به تحقق ۶ بند اصلی دانست و اعلام کرد آمریکا باید تهاجم و جنگ علیه ایران و متحدانش در منطقه از جمله لبنان، فلسطین، یمن و عراق را متوقف کند، محاصره دریایی را برچیده و نیروهای نظامی خود را از اطراف ایران خارج کند.
او همچنین پرداخت کامل خسارات جنگ‌های تجاوزکارانه، لغو تمامی تحریم‌های غیرقانونی، آزادسازی بی‌قید و شرط دارایی‌های مسدودشده و پایان دادن به تهدیدها و توهین‌ها علیه ملت ایران را از دیگر شروط اساسی ایران برشمرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77784" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er_Wsnkq7mmzluJ6ozgRIGliBqMC8wfdDM1KeSSVxIAfy898CO2F7-FOawoVnYMVWJefdpY-5LilAdLoiEfAQWZuO3pMCNE57Mo0r80E4kJ7Xiz16h6aJl1RDMFNkTMH0k924Z2VRc-c74To2_YL6EVTBR0eP1TQUmcAbr1bv1QWJ5uCnnanb1tdKFuXcPBOihkHfI3Q4TYWJxWfRhX2mDxv6o4DxWc8KeucwdgMDz9Mxjf-Ze706MKS--IG1lfwqf0K2v80-n4zV5G5XRwBi9xa2n6X-bwwat1UaOZFuK8uQogj3tj2d-ZDHsk1axgtFz-dw0D5y-fy-7y4eudtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که مسعود پزشکیان، رئیس‌جمهور ایران، با استعفای محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77783" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxmK0FsnhrGKj2DplOSrXHv0RAp3X2AJKKBrf4XsHm5g8RJOAfHY1VFKxKpv9R5tPcRQ6VPXZXvnMz9KdWf8Y1mVEuKOUKmd4AD2zVJtCwRFDJ47fEBRQVZ_sDUTL7hGRyYdV9tYEQ3MHk20s2BHucE_MeIbRGXQ_RNp_LvNLG0vpseFym_PFKBwXsyqtkp7-b-3FtJCXa_x1wyoTTqqf8OG17gLFe2Wze3f9KrtgUv5emMLfZBQ75QxmvTeLl4VK3BrHJPf-hobjvPfXu0WA9KVTAELt0QBNMP115-qrZDhdYVQfwWGmsQx9o7aDeTfWpFE4-ttJCHnyffytoPB_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌ها در مورد حمله موشکی روز شنبه نیروهای مسلح جمهوری اسلامی به نفتکش اماراتی در خلیج فارس، وزارت خارجه امارات متحده عربی با انتشار بیانیه‌ای ضمن محکوم کردن شدید این حمله اعلام کرد، این حمله تلفات جانی نداشته است.
وزارت خارجه امارات، روز شنبه ۱۷ مرداد ماه، در بیانیه‌ای این حمله را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل متحد دانست؛ قطعنامه‌ای که بر آزادی کشتیرانی و مخالفت با هدف قرار دادن کشتی‌های تجاری یا ایجاد اختلال در مسیرهای دریایی بین‌المللی تاکید دارد.
وزارت خارجه امارات همچنین اعلام کرد هدف قرار دادن کشتیرانی تجاری و استفاده از تنگه هرمز به‌عنوان ابزاری برای فشار یا باج‌گیری اقتصادی، «اقدامات دزدی دریایی» از سوی سپاه پاسداران محسوب می‌شود و تهدیدی مستقیم برای ثبات منطقه، مردم آن و امنیت انرژی جهان است.
امارات از مقامات تهران خواست این حملات را متوقف کند و به‌طور کامل به توقف تمامی اقدامات خصمانه پایبند باشد. ابوظبی همچنین خواستار بازگشایی کامل و بدون قید و شرط تنگه هرمز برای تضمین امنیت منطقه و ثبات اقتصاد و تجارت جهانی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77782" target="_blank">📅 18:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hEBIMNShW0DmPQFT2p7DRAuxMA_zlXPmNbXys3U3qWSvFKn4xHL6Kn-sqGAaWPG20_rYHZkO1N06-884mkInP2HtmHQw7lG_L_l-ssxI1bg51K629x6jfJOSPpdGbbKvuP6iBhWviZtrzxKDBMBoqHRPa6Nq3nYtSuT2c8cLsnIKiGEsNZ6tQIRveOrn4kmn1sFF4om8b-mQUsIRKCupTB6268XS-NCpYHOse16TlACaG-070fhQ2SaCNwAlRwjGsU5M8xGBDOYmYpIMbPAQZHLExMRdegMsflLE1jsgK4ClADiSya5ZNO2wNvZYxFY-GkK9cdFvA30MXq8rdFYoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJqFfg_FKRIELJphdrpfh8PTpKQcefrlSMAhQ_f2jJTOMjXodfZz_ca9IrQRBWrSy7TvbsScD4iKFY5cxg_v4PRSidNZqNm-9aT_e38711YucqJRVHJjS1m9AjXPChxuPFf5JPXFCx28jy-3R7CtSraZFtYL5aefRPq1rV_q1lbJvoge3KAC0wB8xUmEp8WQmLuMeqa-PbotDg_MjWHGZKcn37Nbl0BC9Jo0kNPNKWZLhjkvr7DN6grkzB9TU4zIhqGNfez0Y-eCiqZgK1z72CQQEUZzY_8NpzCZ0tIIe46BNqo_2M6ZBM6AxiDLYYTu7BiNKrmK4j98Cmh5OYNcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zeth5JBiG5iEVIdVFijzzwhY4ImHVmQiPynBJUv8a2MemTSqNBZle8N1DdScO3DmJBFoSKdt73v222vZx1a3IQxK0q83IMxJkHRDUUmz-bXTjufi4lFD8wDm65SiYa4IR85jUB3wRvTL-Zti6pAw6HDQKWF9YvJOAk6Hos6cV2mJe444rnmKDqMqOYiGkYdivoxG9be013O19NGjL2CWwjPVlSVyOlMW-HgMQC-iZyPvbyW2jQfxqn0C0CSjd8oOdeSdcqFoMFNip-cf1GLfXJRlRB79Q7LIuV9F_OP-ZS8-p9RHhqmEXDTZtRKb6i80pimqeOrWoXhoX3XNi0PZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Moyk2FyO8gG4bjWuthFSjVm8k_YOsTWeIVMStul4HYW1YKjUsSAsIRqGAXdxqTDJn6StMCq8S6eewA9US1EVcAmgTRMpuKzDS0wy6PwocV2nzrgQogV4pZSA1YPslzBJpMEX8GoSBnSuF68Xux0eTN3MwCpnklwa95ZnpFrFvViLPbPKhOSGYEws3HmegMUZtM0xrjcCv9hSajGTPGE69NwwA_AOBHolVr8QyUVLoeR4KS1JYW4TV1DZC-KuW0Aq6zDDwO0-9mmh0aobujY4Sxi1CAYXaOsIBynPlphnebtUj4drDjL7q9rogpXnT6fKNOhmXvWzQ0A-5puJoYkMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYxTmv_p8xzCL-XbWzf2Hxz0atC6JhdjrKVsYuMT1RFw3l-MVOCjUqXRksIE36FTNnx6QLeHG3VFzya-yItrYjEgX487d5OODQqApao__DGEYWc3ykTDF-2rtv3HpIAiYrm9R128el88w8y-BmOne9rK0S9xgX44JSacoapTvJiSORC7Q5yOiOxgPOLXu4g9eEn53W3sSJw8p61Wf27czoRDmab_qdlVv739b6ryOgBbXqHtfKgV6Up5RTerYxXSvUZZcy_ZFVrCx3pjAVPGvmk6ilZJj18AtiWRt4NFz9yVOqFWgrbRi8zF77Wv0K49jlD4PHW-ax-nbOLvHByA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueBssJTuOb8mibw9LAi2fVwN3_DGGqZ4yv6jdzs3V6E6dok_85eZ3LnbLRpUegMRECXXZEPFvZO4jUy0DNZ_YZkG_TWqZLdDUAPURAJ8KYIyWPc7xZEksl6XSev7metdWvS_Dl_AiopYz_1HN9v8Dugjse8C4Qx9zp0SgBqHPmXpyr0rb2SS5e8plqmKL2W6cDCliuQy7VI2AWrm2-gcVBzbqAM82w-LVphl6lJLJ7ZaqVJx02YnF-RwBdl90azpmdEV4OQ3wgr8LqMdjENtj6MHdJwUJh3rTSVbZUPU-tDGmQGvLAUH5cgetE0yxUV1TzmA5TX7KMFo4rthMxh65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgcZWQxO5axAfYdfvsSFsA01_RynSch1tazYnWCSsbDZKMpuCcHe2XrSrcr0ob4FgMz3y8eaK1YjfShV56Alq0kLotDiIWgl8k9TxidfnJDzPCKAXIxp5EAipC4z6IkxacMUOS-UYdq_J8nHa3BtwBfvcsgIYR7w0ceuV24bul9c87lnqxL9OqHRByoTe7wpMg50FujWuJyswk5r8DA3ChHGr2uYaEhuOOUR3oyG5u98kDIO8jLyod4xwyFkdOMADiQiRI77isLpNmrMhxyABwRld_O8Mgld3AdDXvvPvCjkhSeqYqrVIC4uz6vAw1x9szDf_5o464YFIcYaLt82Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی
قوه قضاییه روز شنبه اعلام کرد محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در پی اظهارات اخیرش به دادگاه ویژه روحانیت احضار شده و تحت تعقیب کیفری قرار گرفته است.
به گفته سخنگوی قوه قضاییه، با توجه به روحانی‌بودن محمدباقر خرازی، رسیدگی به اتهامات احتمالی او در صلاحیت دادگاه ویژه روحانیت است. او همچنین گفت خرازی «می‌تواند اتهامات متعدد امنیتی» داشته باشد و در صورت حاضر نشدن در دادگاه، برای او حکم جلب صادر خواهد شد.
@
VahidHeadline
در حاشیه ساختار قدرت در جمهوری اسلامی، همواره ردی از «خودی‌های دردسرسازی» پیدا می‌شود که مقام و جایگاه رسمی ندارند، اما آن‌قدر به حلقه‌های قدرت نزدیک‌اند که نمی‌توان حرف‌هایشان را نادیده گرفت.
نسبت خانوادگی، لباس روحانیت یا وابستگی به یک تشکل حتی کم‌نام‌ونشان، به آن‌ها امکان می‌دهد از تصمیم‌های پشت پرده خبر بدهند، مقام‌های حکومتی را متهم یا تهدید کنند و سخنانی بگویند که واکنش و تکذیب بالاترین سطوح قدرت را برانگیزد، اما خود در حاشیه امن قدرت باقی بمانند و پس از مدتی با ادعایی تازه برگردند.
محمدباقر خرازی بسیاری از این ویژگی‌ها را دارد.
روحانی بدون منصب حکومتی، دبیرکل تشکلی به نام «حزب‌الله ایران» که وزن و جایگاه واقعی آن در فضای سیاست ایران چندان روشن نیست، و عضوی از خانواده‌ای که با حوزه علمیه، دستگاه دیپلماسی و خاندان خامنه‌ای پیوند دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77775" target="_blank">📅 18:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4l92HHk-hPISGW5BlHa20tZHnH7Ox7cCQ6fMHOqJTlOBHcJqb3W1qkcIzGNpXtDTK8Ia3uZZWCv3QlxPOtrV30DwhvGIJ3bjQIVaDmld1oy3zSobk7unO4Ss9JoPCrGcRUm_cSuqb79wa3mhSAHblcTqrUKRCP-P-YxsNuVOClbdvEzobnu7hKgUjKkV7AGIEXfIe5zfxgfdHbf3HUztkah40f99m8jzDzvYtDiGuR8sc5Oi1sdh-9i8Djbuo07xiX-3oiESGq7kMPKUn4X8QIq2nqeehB5s106SAVAhWR1Nm-hy8kBJDUkWWqJsywg8us4XLAZHsAzbBgVWiwJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم روز شنبه ۱۷ مرداد از ربایش و قتل حمیدرضا رجب‌زاده، از مداحان حکومتی، خبر داد.
تسنیم به نقل از یک «منبع آگاه» گزارش داده است که رجب‌زاده چند روز پیش ناپدید شده بود و پس از آن، ویدیویی از لحظه قتل او برای خانواده‌اش ارسال شده است.
بر اساس این گزارش، پس از اطلاع از این حادثه، تحقیقات پلیسی و قضایی برای شناسایی و بازداشت عامل یا عاملان قتل آغاز شده است.
با این حال، تاکنون اطلاعات رسمی و دقیقی درباره نحوه ربایش رجب‌زاده، محل وقوع قتل، انگیزه عاملان، هویت افراد دخیل در این حادثه و جزئیات ویدیویی که برای خانواده او ارسال شده، منتشر نشده است.
@
VahidOOnLine
🔄
ادعای دقایق پیش تسنیم:
🔹
پس از ارائه اطلاعات جزئی از سوی خانواده وی درباره آخرین برنامه رجب‌زاده و مسیری که قرار بود طی کند، پیگیری‌های تجسسی صورت گرفت و نهایتا، خودرویی که رجب‌زاده برای آخرین بار سوار شده بود، شناسایی و مالک آن دستگیر شد.
🔹
این فرد که در ابتدا منکر هرگونه ارتباط با این ماجرا بود، نهایتا اعتراف کرد که با تحریک شبکه‌ای تروریستی در خارج از کشور، به همراه 4نفر دیگر اقدام به ربودن حمیدرضا رجب‌زاده کرده است. آنها در ادامه اقدام به شکنجه و قتل او کرده و تصاویری را هم برای خانواده او ارسال کرده‌اند.
🔹
به گفته این متهم، آن‌ها با وعده دریافت چند هزار دلار، اقدام به ربودن و قتل رجب‌زاده کرده‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77774" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پست زلنسکی، ترجمه ماشین:
ما از سنای ایالات متحده و از همه کسانی که از اوکراین حمایت می‌کنند بسیار سپاسگزاریم. تصویب قانون تحریم روسیه و ایران، طرح لیندسی گراهام، قطعاً به افزایش فشار بر متجاوز کمک می‌کند تا این جنگ جنون‌آمیز روسیه علیه استقلال ما و مردم ما پایان یابد.
اوکراین قدردان
تمام
حمایتی است که ایالات متحده از اوکراین به عمل می‌آورد — از سوی هر دو حزب و تمامی مردم آمریکا. و اکنون، زمانی که پوتین آخرین امید خود را به موشک‌های بالستیک بسته تا جنگ را طولانی‌تر کند، و زمانی که ما برای یافتن موشک‌های پاتریوت به‌منظور دفاع از خود، با تمام توان وجب‌به‌وجب همه‌جا را می‌گردیم، هر نشانه‌ای در حمایت از حفاظت از جان انسان‌ها و پایان دادن هرچه سریع‌تر به جنگ، اهمیتی فوق‌العاده دارد.
فشار واقعی و قدرتمند آمریکا و تحریم‌ها علیه روسیه بیش از هر چیز دیگری کمک خواهد کرد. با هر گامی که برای افزایش فشار بر متجاوز برداشته می‌شود، دیپلماسی نزدیک‌تر می‌شود.
از همه کسانی که این را درک می‌کنند و از طریق
قدرت، صلح
را پیش می‌برند، سپاسگزارم.
ZelenskyyUa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 477K · <a href="https://t.me/VahidOnline/77773" target="_blank">📅 23:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
نیروهای مسلح قدرتمند ایران آمادگی، توانایی و اقتدار خود را در برابر گران‌قیمت‌ترین ارتش جهان به نمایش گذاشته‌اند.
وقتی مسلمانان در کنار یکدیگر بایستند، می‌توانیم با هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، رودررو مقابله کنیم.
وقت آن است که فقط به خودمان تکیه کنیم و برادری واقعی را در آغوش بگیریم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77772" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرنگار اکسیوس:
یک دیپلمات از یکی از کشورهای میانجی به من گفت که تیم مذاکره‌کننده ایرانی در انتظار تأییدهای نهایی شورای عالی امنیت ملی ایران درباره توافق با عمان و ایالات متحده است. این دیپلمات گفت: «انتظار داریم این تأیید به‌زودی صادر شود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77771" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTOrc2W04TteorXz6jt2vKHz2nk6H0JBwGcjdR8WnJlH27ouoJlSIkcclqcF-96xeFTZbnF9EEqDh0uiRwqCt-rnymD6qVlmcfzSvV_Ow-NDiYkXZhQppYGiey-fiVJyKOzlU1bWCmZMQaXrRhqH71KPGdcgT8SxaR0L_dSEMrqEyfDjjxs03D6eBuXFgqONIu72CyasBPdNOLMcPMQ_0r0uC6YXM3cvSXiKgexh8rpx8AR6xhuG8WTU4ryWcxqcyLR7mhNPrE-sF30nQqkduX13I8LpCBItXjPsHF5uWAkzOW9m1n_soI8mcnaGSsVo-gkfq2UmQBdphTSCivn-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده آمریکا در گزارشی که روز جمعه ۱۶مرداد۱۴۰۵ منتشر شد اعلام کرد که «شبکه‌ای از صرافی‌ها و شرکت‌های پوششی مرتبط با جمهوری اسلامی» را هدف قرار داده است.
در بیانیه منتشر شده از سوی این وزارتخانه تاکید شده است که ایالات متحده در حال اخذ تصمیمات قاطع با هدف «قطع شریان‌های مالی» است که حاکمیت جمهوری اسلامی ایران را سر پا نگه می‌دارند.
این وزارتخانه در بیانیه خود نوشته است که این اقدامات با هدف برچیدن شبکه‌ای از صرافی‌ها و شرکت‌های صوری انجام خواهد شد که به ایران کمک می‌کردند صدها میلیون دلار را به‌طور مخفیانه از طریق نظام مالی بین‌المللی جابه‌جا کند.
در بخشی از بیانیه وزارت خارجه ایالات متحده آمده است که «تهران از طریق این شبکه‌ها به درآمدهای نفتی دسترسی پیدا می‌کرد، تحریم‌هایی را که با هدف مهار فعالیت‌های بی‌ثبات‌کننده‌اش وضع شده‌اند دور می‌زد و با استفاده از شرکت‌های پوششی، منابع مالی خود را پول‌شویی می‌کرد.»
هدف قرار دادن بانک‌ها، صرافی‌ها و افرادی که این شبکه غیرقانونی را اداره و تسهیل می‌کنند از سوی آمریکا چنانچه در بیانیه منتشر شده آمده راهی روشن برای اعلام آن است که «هر کس به ایران برای دور زدن تحریم‌ها کمک کند، با پیامدهای جدی روبه‌رو خواهد شد.»
وزارت خارجه آمریکا اقدامات انجام شده از سوی وزارت خزانه‌داری این کشور را نشانی بر تداوم سیاست «فشار حداکثری» دولت «دونالد ترامپ» علیه ایران دانست. سیاستی که بر «قطع منابع مالی مورد استفاده حکومت برای تهدید ثبات منطقه، حمایت از تروریسم و تقویت توانمندی‌های نظامی‌اش» تاکید می‌کند.
@
VahidHeadline
پیش‌تر:
وزیر خرانه‌داری آمریکا روز جمعه گفت که ممکن است «امروز یا فردا» توافقی با ایران برای آتش‌بس و باز شدن تنگه هرمز منعقد شود.
اسکات بسنت در گفت‌وگو با شبکه «۱۲ نیوز» با اشاره به وضعیت وخیم اقتصادی در ایران گفت: «فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد توافقی برای برقراری یک آتش‌بس ۳۰ تا ۶۰ روزه خواهیم بود و تنگه [هرمز] باز خواهد شد. قیمت انرژی هم باید کاهش پیدا کند.»
او با تأکید بر این که ایالات متحده هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست یابد، گفت تحت تاثیر عملیات نظامی آمریکا و اعمال تحریم‌های شدید علیه تهران، «آنها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی مواجه‌اند و دیگر توان پرداخت حقوق نیروهای نظامی‌شان را ندارند».
بسنت همچنین درباره وضعیت زیرساخت‌های نظامی ایران گفت: «نیروی هوایی نابود شد، نیروی دریایی نابود شد و بخش بزرگی از موشک‌ها و مهم‌تر از آن، توان تولید موشک آنها از بین رفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77770" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#توافق_مکه
:
وزارت خارجه پاکستان در بیانیه‌ای اعلام کرد جمعه ۱۶ مرداد، پاکستان، ترکیه و عربستان سعودی، توافقنامه مشترک دفاعی امضا کردند.
توافق امضا شده تصریح می‌کند هرگونه حمله مسلحانه علیه هر یک از سه کشور، حمله علیه همه آنها تلقی خواهد شد.
در این بیانیه آمده است این امضای این توافق‌نامه «نشان‌دهنده تعهد سه کشور برای تقویت بیشتر امنیت جمعی آنها است.»
وزارت خارجه پاکستان همچنین در این بیانیه نوشت این توافق با هدف تقویت صلح، امنیت و ثبات در منطقه و فراتر از آن و برای دستیابی به آینده‌ای امن و با رفاه بیشتر تنظیم شده است.
همچنین رویترز به نقل از یک مقام ترکیه اعلام کرد «توافق دفاعی میان پاکستان، ترکیه و عربستان سعودی ماهیتی کاملا دفاعی دارد و هدف آن، ایجاد تعهد برای حمایت متقابل در زمینه دفاعی است.
این مقام به رویترز گفت: «این توافق علیه هیچ کشور یا طرف مشخصی تنظیم نشده و کشورهای دیگر منطقه نیز امکان پیوستن به آن را دارند.»
به گفته این مقام، این پیمان جایگزین یا لغوکننده هیچ‌یک از توافق‌های دوجانبه یا چندجانبه موجود میان کشورها نیست.
@
VahidOOnLine
ابراهیم رضایی، عضو كميسيون امنيت ملی و سياست خارجی مجلس شورای اسلامی، عربستان سعودی را به طور غیرمستقیم تهدید کرد که پیمان دفاعی مکه برای آنها امنیت به همراه نخواهد آورد.
رضایی در شبکه ایکس نوشت: «سعودی‌ها باید بدانند که توافق کاغذی با ترکیه و پاکستان برای آنها امنیت‌آور نیست، همان‌طور که سال‌ها شیردهی یکطرفه به آمریکایی‌ها برایشان امنیت نیاورد.»
او عربستان سعودی را به «گدایی امنیت» متهم کرده و به مقامات این کشور توصیه کرده به جای آن، سیاست‌هایشان را «اصلاح» کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77768" target="_blank">📅 18:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=WDNCS73aZcX0g2MAxViJ_32AaP8u0ESfpe_zUt1SdK32kofoRNvtlg1DFNrHYXUKgrpV-I1h5z0VkSai7JW4mr1299YWEAZ73GJyoxg3M6W0xDkfyqSTNAUXUafZM45oL0zk3Fwn3N4PCn7wAj4LxNheIyYcYgYFPDYejvbMcDd5jDBjj9mOSBW8l5-_uKyejfgpcxoREW7VpIqNPsfBZGjfeTgP6cA8rxg_4pwEDpMOjpeLFquVUP2CCr5T7cRx-gUrJlvqvU1wncKjMpmjM4MyeFvk_OPO7xaLg4betqb1FwU_-xy99h1R-fY6HR8cKny1XotNZSk4pOcjkLIUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=WDNCS73aZcX0g2MAxViJ_32AaP8u0ESfpe_zUt1SdK32kofoRNvtlg1DFNrHYXUKgrpV-I1h5z0VkSai7JW4mr1299YWEAZ73GJyoxg3M6W0xDkfyqSTNAUXUafZM45oL0zk3Fwn3N4PCn7wAj4LxNheIyYcYgYFPDYejvbMcDd5jDBjj9mOSBW8l5-_uKyejfgpcxoREW7VpIqNPsfBZGjfeTgP6cA8rxg_4pwEDpMOjpeLFquVUP2CCr5T7cRx-gUrJlvqvU1wncKjMpmjM4MyeFvk_OPO7xaLg4betqb1FwU_-xy99h1R-fY6HR8cKny1XotNZSk4pOcjkLIUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین:
🔺
خبرنگار:
و آقای رئیس‌جمهور، جمهوری‌خواهان اکنون بحث زیادی درباره قدرت خرید و هزینه‌های زندگی دارند. پیام شما درباره این موضوع در آستانه انتخابات میان‌دوره‌ای چیست؟
🔻
ترامپ:
سؤال خوبی است، اما پاسخ آن تا حدی ساده است. من بالاترین قیمت‌های تاریخ را به ارث بردم. بدترین تورم تاریخ کشورمان را به ارث بردم و ما کار فوق‌العاده‌ای انجام داده‌ایم.
قیمت نفت اکنون به‌سرعت در حال کاهش است. اگر به اوضاع نگاه کنید، تا ۷۵ پایین آمده است.
وقتی آن اقدام بسیار مهم را در جمهوری اسلامی ایران آغاز کردم، اقدام بسیار مهمی بود؛ چون آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. در غیر این صورت، تمام جهان منفجر می‌شد. ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. مسئله فقط ما یا خاورمیانه نبود؛ برای تمام جهان فاجعه‌بار می‌شد. چاره دیگری نداشتیم.
قیمت بنزین در بسیاری از نقاط، مانند آیووا، به کمتر از دو دلار رسیده بود؛ قیمت‌هایی که مردم سال‌ها ندیده بودند: یک دلار و ۸۵ سنت، یک دلار و ۹۵ سنت. سه‌شنبه در یکی از توقف‌هایم در آیووا، در یک محل قیمت ۱٫۹۵ دلار و در محل دیگری ۱٫۸۵ دلار برای هر گالن بود.
بر اساس هرچه می‌بینم، به‌محض پایان جنگ، خیلی زود دوباره آن روزها را خواهیم دید. فکر می‌کنم جنگ به‌زودی پایان پیدا کند. تصور نمی‌کنم آن‌ها بتوانند مدت خیلی بیشتری ادامه بدهند. بله، بفرمایید.
🔺
خبرنگار:
آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
🔻
ترامپ:
نمی‌خواهم بگویم که توافق حاصل شده است. تنگه در حال حاضر تا حدودی باز است. می‌دانید، چیزی داریم که «محاصره» نامیده می‌شود و نیروی دریایی آمریکا آن را هدایت می‌کند؛ ما آن را کنترل می‌کنیم.
اکنون کنترل آن با ماست، اما آن‌ها همیشه می‌توانند به چیزی شلیک کنند یا مینی در آب بیندازند. حتی اگر فقط یک مین آن بیرون باشد، اوضاع را به هم می‌ریزد؛ چون مردم نمی‌خواهند کشتی‌های میلیارددلاری خود را وارد منطقه کنند و تصادفاً با مین برخورد کنند.
اما فکر می‌کنم عملکردمان بسیار خوب است. خودم در مذاکرات دخیل هستم و فکر می‌کنم اوضاع خوب پیش می‌رود. ممکن است توافق حاصل شود؛ ممکن است به‌زودی باشد. بله.
🔺
خبرنگار:
آقای رئیس‌جمهور، درباره مهمات؛ شما شب گذشته نوشتید که آمریکا مقدار عظیمی مهمات دارد و وجود هرگونه کمبود را رد کردید. در عین حال، یک درخواست بودجه تکمیلی ۲۱ میلیارد دلاری برای پرکردن مجدد ذخایر وجود دارد. اگر کمبودی نیست، چرا این درخواست همچنان مطرح است؟
🔻
ترامپ:
چون همیشه به مقدار بیشتری نیاز داریم. منظورم این است که مهمات بیشتری لازم داریم.
ببینید، دولت بایدن مقدار بسیار زیادی به اوکراین داد؛ رایگان، بدون دریافت هیچ پولی. میلیاردها و صدها میلیارد دلار.
خوشبختانه من در دوره خودم ذخایر بسیار زیادی ایجاد کرده بودم. نیروهای نظامی را بازسازی کردم و مقدار زیادی تجهیزات و مهمات نیز در اختیارشان گذاشتم.
از بعضی انواع مهمات بسیار قدرتمند، ذخیره‌ای نامحدود یا تقریباً نامحدود داریم. در مورد بعضی انواع دیگر، وضعیت کمی محدودتر است و هر روز محموله‌های تازه دریافت می‌کنیم.
همان‌طور که می‌دانید، شرکت‌های دفاعی ما اکنون بیش از هر زمان دیگری در تاریخ کارخانه می‌سازند. برای موشک‌های پاتریوت، تاماهاوک و همه‌چیز کارخانه می‌سازند.
در عین حال، انواعی از مهمات داریم که ممکن است به آن اندازه دقیق نباشند یا در آن سطح ممتاز قرار نگیرند. نمونه‌های ممتاز را هم داریم و این موضوع را بسیار دقیق زیر نظر گرفته‌ایم. اما بعضی از انواع مهمات ما بسیار قدرتمند و بسیار خوب‌اند و ذخیره‌ای نامحدود از آن‌ها داریم.
بنابراین در وضعیت بسیار خوبی هستیم. بااین‌حال، همیشه مهمات بیشتری می‌خواهیم و باید مقدار بیشتری داشته باشیم. ممکن است مسائل دیگری پیش بیاید و ممکن است هم پیش نیاید. امیدوارم هیچ مسئله دیگری پیش نیاید، اما ما در وضعیت بسیار خوبی قرار داریم. واقعاً مقادیر عظیمی مهمات داریم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77767" target="_blank">📅 01:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGYFt__RB2zpmrCFSBytySvEkbcfFu7gH0C8FvkzXflFYZkkaGyMshEKyO3eeEe9pSoDbml7n5gaTawZ7jpAx6jvxj4AfyJLxqdOY9PxVE0FDpgRNvwtMRMrLKe-lLqeFPbZehHh1-LTKn7ZPdkWoYqcNFl-0FOnQqwWpQhgfWo2qoDi1GgIM-5GsEco7w3_slcKgl7374UH82cE1K0H8sWIinNF-ISvElqQW7Dy2DPGsU_1tMYWNZ7PfjZF-20QYjCoPlenEURPSy1hRl5Pcyu2Ug35Sv9z0c2QfWHunLBr0MSb_yY9YKvCxXzibEcWD7j5MnfGM1qpGdEFWv4T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی: سلام وحید جان  همین الان دو صدای بد انفجار شنیده شد قشم  سلام ساعت ۲۱ و ۴۳ قشم دو انفجار نزدیک شهر   سلام وحید جان الان قشم صدای دو انفجار بد اومد صدا از شرق جزیره احتمالا یا کشتی زدن یا تو آسمون چیزی زدن  وحید قشم رو زدنننننننن [لطفا صداها…</div>
<div class="tg-footer">👁️ 498K · <a href="https://t.me/VahidOnline/77766" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aQZ3CO16vz4rtcTZOrg-tWm_4GBdw8X7Nv46L4DIK74AZNz--bHohyusqYnS0oRQ48d_Av1A4BA55XUWcfEQgbWmnDGyfX5uPLytbZk6YBdPqmlrnPldNGFqMLyZkaQA2yEKUqeAHDdZvpt_VZv6W3cleAqmF2I2fMLmPPGt9Q10M_y5rZYNtSbaVLWzs4an-NVH5in6TdB_M0S-rJ-9W5pTFCsnmzdqquZLvZ_9gXO8WalEElsoYsP3otZuQVBDtKnIhrX_CgkVUGWgwRSKh4CxiR6hgV_p-gmyVPKAQ9LBcUkcyngS0967hdVAv1lVgAXtmYmUjQUJPRyW_adPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77765" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
