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
<img src="https://cdn1.telesco.pe/file/X4ZPdHU_dPERTHqyWb_lfhY_r-SMnw8OeIMoruqWpjlchOyTiZrnT1D5asZ7Nv4tzA37IqYSq24KqDFv6TiLyivtwOOfp9sTTDNbwbGI4YSVNsoZpHvE2EJjWkHA3_DEwMka7MYH7lb09CYrUzgYh4JykxrcPutuT7gMwmqDHB7loUpeak0L7AOS69G-S9Y-G2vJ48bPBH4GjkNGJuDgbqQBZC6qmXg4npow1wZJblNlCkJeOUEsPuTZX7MZLgpJj2ka3IAie_a58t8ljhZCzDnTAN9gCf0BhHk1jJ11ThHNBZZks8k-94K7Yk1_jAhceIaAUmfHm43drqQwynolsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 03:42:57</div>
<hr>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hto2cEI3Pw_wNL7gUF4a8FqQQUoaJSzHkg5AltxIGbIjxHm92VHCrkv1pnuJrypNH-YbLeSuOTR4ZMPScpXYunycMpH_910U9lQ4svQ73wx6f6KRBcY3tF_AbB1XTFQrqbWiSCybRA1vaE8i7mILIzNDXOjzKWrVInR9qInAmpCbqtmvPan67k5Snfc4gvNEqgrI3cBI64Zzn87uO612tV8retuXG73DDS_CdOht2aQEhFLEXdv01s6W-zfhbtAd1Cf78jjlB5Qq5kBkCNXIsumwKgmXMJF__pOznMHXPf1m4cZQbGtJylEynqytar2O_mZAiBS7HPwEzcAZaWggRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cwpij3Lt-Hj9tLyMDvknTPJQG1kAcrJnpf8dcKgmPp_gUHP5oJdU0b4zv_LzmoBVUQ8dWqf5qUFt923yE9SPQ1T1wR7bUAClzeaq5vcCwhcHd62JU5u6IqxI82kZ6csbcb5Q8did710m0vSf_Lxx5g28dr7UEIMo9GFTBgyF98PbyzYRvfmyEj7mnGTPfGNdTCyrfek2wTBuAoxI1O1qCfvrsGRPzK4gREhDV5IK_WB1pTsBz73_4qavdkQSy3UOOYao_AOUmox4kFEcXSqqXU-NWNDRZawSNloS6dbdUFB0duWk_xA2hBxA4jTPcMjMBVNlQoZKuqCmKzYooXrHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k8XcfsnwXi4IANTiFCkgD0CquHZQH3UoNTqMx7k8_BUiM6pPNc9AF2WJ6kQ31xhMJrZpk5egnatuo_imdeSDJ7_-qvIJDeCHVFkSQNt-98zRCWcaxiFavEyG6axF_Pulu4iotGPaGB8Chbv4uF6vSegmIcCJ8O-WTAMs6fYBLHQ7HT1WcS2Epd7kkTfYoM2tS5Y5p1beKv8KHKmcsZGpWnAUJ-a0PUKueLSpmTp08sPACb_RAbxzTofoMUE3RkVlb9RECCpAez2Ga5-fV53236xoLI0OHiriRKJNZktT5o39gcSTfXvOgLdnNgB3-jXU3tyBrmvG4dN1nCU3GRIuCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vpim8qT5hMX2oLbNnTgzgxPKNrml9NWBrloqObnluQL03pWA00ZZDWMMhyJBcCNbTZNpJLNlymc-z_ykpmNsiaRozLkNEuHXh3XA7GBOlae6hGenpefVGBGmPHlnfU36eCqm6TxTAxpNSa7lkPbewMHg6L8qFAbzZHbMuJVh6DabDD3B7LvPZHTNFeLq7g-Bh6CEzCinfW7rL4GsrmexUioL1zZ3iu7ULhy9Np6oMaVufWrGoeuHOT4CV3cJdbLZRztRhYZd3TpvwkJzKR_mjBMvx271iHdbdcvc_L8y5KHxmCEd5_r7SVm_YzdrIXthOYN1MMgyTsPKPmYm7kKFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IbNJumGv3RF7ZrNhnEs6kc41Li2BKkOVVa2yuPSDqvISJW7jqdaXJ7hSXlQnNY1wnjcKluJMnX0KR4WaRGKPrj0ZJfEdsZZPyVbeZ-gwpoeibJuAWxLmzosSejKUHzuLYHQkxEBp5R1L9vj18MrRhJFK59ru4bWF45_iPt1KwlCIbJPOHezibe26w9fxUUhWnxMiHJjmPCjURUZBO_m5rPYUcR3nwlM7DnNLrikC6b2slvxCzDlA_VROS4sH_RunrfsyiBSF6lyhdyPltTdPFEXtOwR3chgYPMORmj6qwvZXBsjtRuzSrSyf3wuYCpopCUZjh99ywzvCFM9_LiZHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sjgSr8xcO2w-cRZgsW_mGnB9Z_PiB-Q6INsgCuuSDEcSMQ5diyuZmefTxu2aKf6W7s7KAlWRw8RuQE9m7ETOAA7A_FUXsns9RsRrIQpBeTk0MFl4h61B9BRLcvTYH3jxWkgANlxGl3lgG7b29QVjvVH7FiQMEy3qThuJ80iJCtDdYYQWwpO0KkhfY_8zPap_HLXYO-cUkM8t3LevE-bNbnVNck-r8ikOWIy9zroRUCJyIFCKURcp09AywkDZcRQQYkklaUr95GokByBvsFwF_s2onBTEWZnKe8rKm2zahmNA5VKT-6RS6bN7chdgjzaF9wZg3JN9iRNKdsEkX8r4nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y68DCl1Hj28OnBqUKaWT1rAkj5W2VKgg61_rhP37CSugSmPIhbnBiyEPLxDix0MvC5FW_3dLjGtsYE8BxRKJq1W_AYMclxC3NfFLZICi2VPyh9ygY8Tql77upRPepORM1ju41xzbQkCfyVd759Bc8hfTE-tVFqMiv8QiXUqcqXmRCLulmjItGI4OOttDxx9GcI8b34lEeNcU1gIcl02xvuuWcbgLrc3GKSbZ_9Wg2Wcy5gfcBEuZJfjpUXtWIl2lEIb5RbsFIJfIUkL3OJ63PHY5tSGIjK3JgbgbkJxmokCqOYTeXkCK8kEnxofPtWmg4L1tSXeh5h8wd-z6olPd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QRMS7w0bcLNcJodjfVXuqJ9rxj6QoITWVD-e5jnc7FNX4l1g4l2fx1TVHQqk7ei9ncaeDzGv_qH_DCq_PZfRdBal4Q59AGFtWDvoUvIIK6xaBqDvn3KebMx0gMDmM6IL6eShqSk8yt08jK8IiYkXv7XY9u8WflaG0OYa8RtJBygTGTUGTHTkkiQUPVijPn-3wx-P3tMFNV-Mp09Tw1F1G54-tustTgSTpNbMI5wWSaaTbEexpkKQZToeCnz-FrGUuK_yAXovqAVVtF9uX5nZBxZTeH0lXYGT3PfIcTqwzyKeFHEUF_7hFL0vQ9sv7nuKYu0UO7cj9ej3zscR3jfkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
برای آن آشغال‌های خائنی که حاضر نیستند درباره عملیات نظامی ما در ایران گزارش دقیق بدهند: ما عملاً مقادیر نامحدودی مهمات با کیفیت متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنچه بتوانیم در این جنگ یا هر جنگ دیگری ــ که وقوعش بسیار بعید است! ــ مصرف کنیم. علاوه بر این، ما در سطحی بی‌سابقه در حال تولید مهمات هستیم. در حال ذخیره‌سازی و آماده شدن برای هر وضعیت احتمالی هستیم که ممکن است پیش بیاید. این مهمات را برای خودمان، ایالات متحده آمریکا، نگه می‌داریم، به‌جای اینکه آن‌ها را به دیگران بفروشیم؛ اما فروش به متحدان نیز به‌زودی دوباره آغاز خواهد شد.
همچنین لطفاً همه بدانند که دولت بایدن بسیار بیشتر از میزان مهماتی که ما در ایران مصرف کرده‌ایم، مهمات را کاملاً رایگان در اختیار اوکراین قرار داد. صدها میلیارد دلار بدون دریافت هیچ هزینه‌ای به اوکراین و ناتو داده شد؛ پولی که اروپا حاضر بود بابت آن بپردازد ــ اگر فقط از آن‌ها خواسته می‌شد. اما ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
از توجه شما به این موضوع متشکرم.
رئیس‌جمهور دونالد جی. ترامپ
truthsocial.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78217" target="_blank">📅 18:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mb3W5TX_IZSVnNTe4bFmR1f8II52i7L9GmsBMigNPkmRddDBX-BrUN0E0n-cAd9SO8HOTJByYKviQDTxyRCTHf1otkLxFHs-VugHPdc_IdkDC9XM5BwED7ura8J8X_ILrffw4Rp9JmkSmuT9fbGeDAaYYStmkfca_ln-2egWr2U8LiDUHYCs_UJXAMqRyFIWt494-wPvKeLR1AyFSp-dl1n_tpJ8H2b8a32tzHVG8SCnz36-QH7DLQ0tnANvPNNYf--y5OkLZaIp9xgHTGWlYl9dPtE92bRHMAyHrMIHvmDR87lLY5J7r1jhFz1Pq8G0laTVi-kLBmeR_2Xj64ajqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رئیس‌جمهوری اسلامی ایران، روز پنجشنبه ۱۲ شهریور هشدار داد که «ماه‌های تاریکی» در انتظار اقتصاد ایالات متحده است و از مردم آمریکا خواست اقدام به ذخیره‌سازی سوخت و بنزین کنند.
او تاکید کرد که «جنایات جدید آمریکا»، دکترین دفاعی خود را به تاکتیک‌های «نامتوازن» و «چندلایه» تغییر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78216" target="_blank">📅 17:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DJfDGu4hjwMz1dY1yzo96q2hhMNl98reVtnerfDi2lOTOe5zTiPrnHBAX1navjMLuBu6xbKSn9efElhB5nsbnOI8p_yExuWfBAo8mVGSKuNIjE5x38bL5a_g1zBQw9YZsPqzAiZtBGcMHi1OkvfYcnW-kgkUhkfPMVOV0u9fSe-41qt4aDZGIf-LpYtKQhfOYQboXATRq_F8ftUP6Y0-xoZDoVngQrok9m2mAYpTEJE0cWbr7ClVBcfQs50CXgQb4BRmevZ-60_zz9kdE3kdKMrQqHco9GEvbMCrI5UMja2g2hEN7_R0NYAXsuWFDuWyZuWQB_or9GXa5D9MJygz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">916208
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78215" target="_blank">📅 16:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJsqNURcB_p8rERjlcMxmXs20oC52HWWtBp5z90H80NNf0s-ryR-sT10wcDO3moc4qzXbA_hgiHqLC4TTZ-cm2hohaKocWuECBjFpIO1wMdL41DR2TmbMWGsNS7KWPVt1Y2KVRCQ6vrhRjGzcV5l4SwDL1PkdTwjoqQsXpDPllxiFCllSe1xO2LOx33PR_MOfBg16S48TfXxWOCVg5Br2ILoNyHOdgoeqFuvdPy5f1PDVZ74K7WcmTkfeP4nNRUYSIcZEvQ-YuJBL4p2ybv-ikdk-1V0gvdrZMYy_qNfIQD6VO-zVVeomEkBRcduk3xnV-7OsYwo6IW4UfjSuk3adw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا با انتشار تصویری در شبکه اجتماعی تروث سوشال، مجموع حجم نفت و گاز مایعی که پیش از جنگ از تنگه هرمز عبور می‌کرد را با میزان کنونی آن مقایسه کرد و نوشت: «حجم نفت هرمز بازگشته است!»
ترامپ در این تصویر، مجموع حجم نفت و گاز مایع عبوری از تنگه هرمز در زمان پیش از جنگ را حدود ۲۰ میلیون بشکه در روز در نظر گرفت و میزان عبور این مایعات در حال حاضر را ۱۸ میلیون بشکه اعلام کرد.
این در حالی است که سامانه پیگیری موقعیت نفتکش‌ها در جهان، میزان عبور نفت و گاز مایع در ماه گذشته را به‌صورت میانگین ۷.۵۴ میلیون بشکه در روز اعلام کرده است.
بر اساس داده‌های این سامانه، حداکثر میزان عبوری در یک روز، ۱۰ میلیون بشکه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78214" target="_blank">📅 16:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kepLw6naIfmt4I9A6RJq4BfI9z3d-1HYaMkrf_BliU9bTkP3A8i5WQcQykpzAxOg75F-WuquTPnIL1DGS6EPYdEsQO6JQDb6uyg7dPFnlXlO_YoMimG0o-Rjk2gAYLypQw29YsEag9QPvhKnlru76mqryXnJX3ixvualMoN2Wm4P4InqAZUOKFVzW5i7QWERO294uE4zyTODXkn5v0SSZv713KtnwJhYD5JY_ZZifHRixoE_w3YBzNFDZCGLjkFBoSr2qzT6wbXHc9lt3fJd27G5InPPmOy3qN60xcFrgsvSdraImukm6yK_bU4fk7m-lQCbpfBxqo0Z0KTGli4xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgFyAATbP3jmqCXE3uqeh8UkUpdd-YAfKp8gX_I5Ybh8Wj0vMJEceDi6WcjMiTDgCc86wMvLtzBvatk7jvZZuewcHU4RScVfhDMtDVGUmGFzyFdhvsotGvjlxHoZ5if1UyalAbYgL27f8_-igGvZwzltFy3UwstqaauSOgx33ZwfFg0Q2qqHHnx0TU5FLK-oVERqs6AsAFqvTh9dpd5EtOz7FFqsTsaxJFUJtOj-_zXy1ow4xYwQHHMwa2ugCyKtktVtFrbuvBIO7Zguw9lIVA3squ8UoSPf57D2C3unaVCN8HK_SBeI0KHMCAdFL-jzcda54fzsgKKFPm5TM49izA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=jnxgqo6-drBhKFmXrHrEtfW4zAumEhaSnyCvOvs1r2dj53rCQllpXtQMCr0ynfuasdo85PM5AF8oIzFSCjQVpqyNvXxojvTsa18PtF_2FSW4IQGSzvXZLnlOqz1QWJJlriycpfa-Pi77-GJDjM1nbaGpdx38YzY3TMrd0z5qBHix80Bk-xHhQ4qpK48dFDXcup1Xq7EainBNwElqVpInqa7aprdhGtgGOExmm9SA22_fmH6orQlK_ztV1xX3iJ2yo-m9khF0Lv78XWTLvJqO4e1qqP7WohUeSbSTT_FjjIyTjpl-ELYYpVQuVJZpiLX_czCc-Uxvot05mgxRNPm--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=jnxgqo6-drBhKFmXrHrEtfW4zAumEhaSnyCvOvs1r2dj53rCQllpXtQMCr0ynfuasdo85PM5AF8oIzFSCjQVpqyNvXxojvTsa18PtF_2FSW4IQGSzvXZLnlOqz1QWJJlriycpfa-Pi77-GJDjM1nbaGpdx38YzY3TMrd0z5qBHix80Bk-xHhQ4qpK48dFDXcup1Xq7EainBNwElqVpInqa7aprdhGtgGOExmm9SA22_fmH6orQlK_ztV1xX3iJ2yo-m9khF0Lv78XWTLvJqO4e1qqP7WohUeSbSTT_FjjIyTjpl-ELYYpVQuVJZpiLX_czCc-Uxvot05mgxRNPm--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">dadban4
:
"امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه.
شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند.
ما مادران نه می بخشیم و نه فراموش می کنیم.»
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند.
او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد."
abelbalb
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/78211" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlGW_w-U6qbFprJkShhgns2DxlD6wy37J24OXPbtu1DnZLnBAyfygrlGFFDXHQlJxNCx8SXSg8qpkgBqBBicgO1XB4efJctySSgJ-PTmX1pZ7ChclB7C_rPRD7hk4Clqy-rO1S7RLVkaeLGMhsa-9tqFXd1WXHHMVqleZyXYoI3dyc6IKNglajjbDsmR22FrwitGTAhUQ2TeTElA-ha_s6zZpfRkVYBMpY9Z-MxOtciNonyEE56QuKjzL451yCpSF3olaeXLD_xLjllTLBvp5IPtak8Exfb3kfFytrhY2PUYYjmmbIgtQHc-dh-7H5GKa_M2Z49vUzb5a7ohkZp7zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، از کشته شدن سه خلبان ارتش جمهوری اسلامی ایران در حمله سه‌شنبه شب آمریکا به ایران خبر داد.
این خبرگزاری با انتشار اسامی و تصاویر این خلبانان گفته است دو نفر از آن‌ها از خلبانان نیروی دریایی و یکی از آن‌ها از خلبانان نیروی هوایی ارتش بودند، اما اعلام نکرد در کجا و چگونه کشته شدند.
با این حال، اسامی اعلام‌شده سه نفر از هفت نفری هستند که روز چهارشنبه ۱۱ شهریور اعلام شد در حملات آمریکا به شهرهای اهواز و آغاجاری کشته شدند.
در جریان حملات شامگاه سه‌شنبه آمریکا، به‌‌گفتهٔ مقام‌های ایران، مناطقی از جمله فرودگاه جیرفت در جنوب استان کرمان، عسلویه، کرمانشاه، مناطقی در استان خوزستان، شهرهای چابهار و کنارک در استان سیستان و بلوچستان، سیریک، لاوان، قشم و بندرعباس در استان هرمزگان هدف قرار گرفتند.
سخنگوی وزارت بهداشت صبح پنجشنبه از کشته شدن «۱۸ نفر و مجروح شدن ۱۴۲ نفر» در جریان حملات اخیر آمریکا خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78210" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pVxsCFzVGWG5AJRf-1fND-5Xq9ajKPdO_YEyF7b6asDOaw3oKruxspW0BDwaa1W_K0ls8E28lVQ8bQfybBiyfPcQgrcjyGSvySevSiZgWx6vG5OSvA8hyU9SIrTNAGEy_-N64xyo0Tftjw2ChVx7SnXuZJkjUXW9xOIYbBfd92WUkEpUf2JSl5OcXI_VyPBxXgPlsjjiw4D7EYKz5rQ-uYIJ-ePBhTqjUYGa4dQ_9XYCEo010_iZiRBFHz3jUVGkLnvElNaRBl3YIFqPCRarAcALG7IREEaoMx19ax2yyXshKerK2LzFTTDXOdjbH18bDQWlsJf8r_p3Eo0VR68Img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78208" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gUKnNm6UBo8AnR6y2CjB_pOYcaipBZyoiaD543lCA_nvvNqwTNSpAPJmG0nzcloXgj3dxUE_6TKTnsSMmsde1vYELG5hGb1BEXhFDukO_Zzb3NKXtKayfynBMwzPMmCTwsDgA0t9lhg4OJYq4ku8yeXoReT1Coim68y_7LcElKWqRX6tFnQLp4u-WhbafrzB_91kUQm85GQ4FA8Y3o9tHBE8omCqXLEO7oK8JDOyv0_95Z5sjdGkcEhy4ITRF11343feMA682ohJ7O0sftd35x1-QhlX_yoXBAYWwDtZaLrv-Xwuk2dAsgkupLpr3wHPHVV6BpmB3aaz0EEsSPj0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، پنج‌شنبه ۱۲ شهریور در مراسم روش هشانا با کارکنان وزارت دفاع اعلام کرد حمله جمهوری اسلامی به این کشور، اسرائیل را از همه محدودیت‌ها رها خواهد کرد و این کشور حتی زیرساخت‌های انرژی را نیز هدف قرار خواهد داد.
وزیر دفاع اسرائیل گفت: تمام زیرساخت‌های ملی، نظامی و غیرنظامی، از جمله زیرساخت‌های انرژی را هدف قرار خواهیم داد و ایران را به اعماق عصر حجر و تاریکی بازخواهیم گرداند.
کاتز همچنین افزود: فشار اقتصادی و نگرانی از قیام و سقوط حکومت ممکن است جمهوری اسلامی را به اقدامات از سر استیصال سوق دهد.
او گفت: حکومت آیت‌الله‌ها در ایران به‌خوبی می‌داند چرا پس از آنکه دو بار ضربات سختی به آنها وارد کردیم، برنامه هسته‌ای را نابود کردیم، خامنه‌ای را کشتیم و به توانایی‌های راهبردی آنها آسیب شدیدی زدیم، به اسرائیل حمله نمی‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78207" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdYfAtRG-xAa-GvX3zCvLEfNbAApbN5AfJqqx7tRLlgxfWDktA2XaYfzQeyQusXmvYmUO4ZKC0TZCZu96Hrn-BbmGbQryQfHbqxqRWuXSxRbdWlNhlbQKDDbRSiEqVmMBgVDYwCmOMbMC5zm-vpCufQAlw2dFMAW5nu0jpnf3_w3yOBcPvZA-WbxSkgldpdSU73vKk7pDwuh5c3XmaOBU2L-FqR9v_Jcjs0H1wDZS1ZLWxlQFOKPLYtKCr9wHTq-rExtyOsG6satT9_QjMrpL0icYXRC5erI_-oUM67ap8TgOBBATwzDM0GDNgzIIsqUmafh5AarXspuwVZOVwiniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خودروسازی سایپا، روز پنجشنبه ۱۲ شهریور ماه و چند روز پس از آغاز ثبت‌نام طرح فروش فوق‌العاده، با صدور اصلاحیه‌ای رسمی، بهای مصوب چهار محصول عرضه‌شده را به بهانه «افزایش هزینه گواهی اسقاط خودروهای فرسوده و سایر عوارض قانونی شماره‌گذاری» به‌طور چشمگیری بالا برد.
بر اساس جدول جدید منتشرشده، بهای مصرف‌کننده «کوییک اس» و «سهند اس دوگانه‌سوز» هر کدام ۳۳ میلیون تومان گران‌تر شده و به ترتیب به یک میلیارد و ۳۲ میلیون و ۵۱۰ هزار تومان و یک میلیارد و ۱۲۳ میلیون و ۶۸۸ هزار تومان رسیده است.
در بخش خودروهای مونتاژی و وارداتی نیز قیمت «سیتروئن سی۳-ایکس‌آر نسخه وی‌یک» با افزایش ۱۱۵ میلیون و ۵۰۰ هزار تومانی به ۳ میلیارد و ۳۸۹ میلیون و ۳۲۲ هزار تومان و قیمت «چانگان سی‌اس ۵۵ پلاس» با جهش ۱۹۸ میلیون تومانی به ۵ میلیارد و ۸۱۹ میلیون و ۱۲ هزار تومان افزایش یافته است.
این در حالی است که متقاضیان در روزهای گذشته بر مبنای نرخ‌های اولیه اقدام به ثبت درخواست کرده بودند و حالا این محصولات با موعد تحویل ۹۰ تا ۱۲۰ روزه با نرخ‌های جدید تحویل داده خواهند شد.
روز چهارشنبه ۱۱ شهریور، بازار آزاد نیز با موج تازه‌ای از گرانی همراه شد و چند خودروی داخلی دیگر جهش قیمت داشتند.
به‌طوری‌که تارا اتوماتیک با رکوردشکنی و رشد حدود ۱۰۰ میلیون تومانی به محدوده ۳ میلیارد و ۷۵ میلیون تومان رسید. بر اساس گزارش فرارو، در همین روز دنا پلاس اتوماتیک با افزایش ۲۵ میلیونی به ۳ میلیارد و ۱۹۰ میلیون تومان و پژو ۲۰۷ اتوماتیک پانوراما به ۲ میلیارد و ۹۸۰ میلیون تومان رسید و محصولاتی نظیر شاهین اتوماتیک پلاس و سورن پلاس دوگانه‌سوز نیز به‌ترتیب در سطوح قیمتی ۳ میلیارد و ۳۰ میلیون و ۲ میلیارد و ۴۱۰ میلیون تومان معامله شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/78206" target="_blank">📅 14:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLeBwLrdWXfEx1DnwAXxE44jzPltf1R9TkKwKeAwdlidkBxfvTBIGIGqa5dyGn5_8ojl4hAc9h8PXGo_svr9_y56YJQEBnVhpJgiApZAq5okMrWjZ6mbKyonbE4yv8Nnl4jZ5VHtwC6o_H9EcJ-Zzp0-cg1T5lT9ponISnBihaPd7oT6MLO_iPTgE-MHw5zouYYG3xV0QCaT329C-xMqcciUaUHyh7axZjuu3X-LRYpIdrRzcr36K2u0DuSQ4wzZTwCcUF1-4G2MEUXU40_xx0E0p74NDhDavuCumo5tD6lyYkpXmhwoa5URknk0aVCUcZ71XCMt8DtzrJ-T5okK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین شریعتمداری، مدیرمسئول روزنامه کیهان، پنج‌شنبه ۱۲ شهریور در یادداشتی نوشت که ارتش و سپاه باید از «اهرم» عبور کابل‌های فیبر نوری بین‌المللی در خلیج فارس و تنگه هرمز برای «مقابله با آمریکا و متحدانش» استفاده کنند.
مدیرمسئول روزنامه کیهان نوشت: «در عمق آب‌های خلیج فارس و تنگه هرمز یکی از شاهراه‌های فیبر نوری بین‌المللی جای گرفته است. شاهراهی که بیشترین ارتباطات اینترنت، تماس‌های بین‌المللی، تراکنش‌های بانکی، سرویس‌های ابری (iCloud) و حتی ارتباطات هوش مصنوعی و دیتاسنترها از همین کابل‌ها عبور می‌کنند.»
حسین شریعتمداری، نماینده خامنه‌ای در روزنامه کیهان، تاکید کرد: «سخن با مسئولان کشور و مخصوصا با ارتش و سپاه است؛ خوب نگاه کنید! کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78203" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxThecU-eA_R-ds3QwJ2PVW6P627iUUk20TyLZeuJgrUvdiuaG1YBX3AN2VNPttZZ0m71Tz1bYa2ufHIVPYvBS9OJ7xoBxGFV6kRL7mIf_BqQ_8OJJd-7Bj6JxCVL-wqatmh2P1zY3gk9xNIxftwOEZmUVfJmzxrtjPT0QR09KoWP-2Dmv16u9XsrK7PCGSJFyPud5CZcF_v0vPtItAIEtWsazZVok33HzDWGZoq0KecDY2ZYEUDVJESSQ98BBo_-Egn0tLwehtz5pKeFNIp-cKTac0i2XigcYLcQgzDFRWvkAMu7YuBGWdT22QBN3wJ8zm2o1a6eEp4M5eoAunwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه افزایش نرخ ارز در ایران، قیمت پوند بریتانیا پنج‌شنبه ۱۲ شهریور در بازار آزاد برای نخستین بار از مرز ۳۰۰ هزار تومان عبور کرد و تا زمان تنظیم این گزارش به ۳۰۰ هزار و ۲۸۰ تومان رسید.
در همین حال، دلار در بازار آزاد با قیمت بیش از ۲۲۲ هزار تومان معامله شد و قیمت یورو نیز از ۲۵۸ هزار تومان عبور کرد.
قیمت سکه امامی نیز از ۲۳۵ میلیون تومان عبور کرد و نیم‌سکه به ۱۲۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78202" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EV7p7F_EXhtpudxhaF0Mc5MoMnDQNaJN_DB0A2adkV1g1rCm0ANH75Z9fdE720ebhn32z68X7a_9DsIFmkVt5fQkvfBQ96zlso9a_ejN0-FsilWyTUSEOcqQk6RdARfm4mu23ZwtC8ORi2mz7NIEzGvBGhPYyfAuwGKvd82caqtGdJM8y7L5pXKZImvY3dtHEy7jD9d1JV9cLEIZL_Az10V7HHSCUQAR7d7hOozDY6deJQ7RTWh7R4ApEp6HqJflmUEH93gbH0vXsl2_tjSk4HPXmyfC1K2eliKB4RJypHOn-RRWL83NAbq3HdcFVIqtaInyx6wX1_PN05ah0IgVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور حکم ۱۲ سال و شش ماه و یک روز حبس، مصادره تمامی اموال و دو سال محرومیت از کافه‌داری برای صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای «ساعدی‌نیا»، را تایید کرده است.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ اعلام کرد این حکم به‌دلیل حمایت ساعدی‌نیا از اعتراضات دی‌ماه ۱۴۰۴ و تعطیل‌کردن واحدهای صنفی زیر مجموعه این برند صادر شده است.
براساس اعلام قوه قضاییه، صادق ساعدی‌نیا به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به ۱۲ سال و شش ماه و یک روز حبس تعزیری و مصادره تمامی اموال منقول و غیرمنقول خود به نفع دولت محکوم شده است.
دادگاه همچنین او را پس از پایان دوران حبس، به دو سال محرومیت از فعالیت در حرفه کافه‌داری محکوم کرده است.
قوه قضاییه انتشار مطالب اعتراضی در اینستاگرام، حمایت از فراخوان‌ها، تعطیل‌کردن کافه‌ها و فروشگاه‌های مجموعه و تشویق کارکنان به شرکت در اعتراضات را از مصادیق اتهامات او اعلام کرده است.
براساس کیفرخواست، صادق ساعدی‌نیا با سه عنوان اتهامی شامل «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های مخالف جمهوری اسلامی» و «فعالیت تبلیغی علیه نظام» محاکمه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78201" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4gG8_eLZpaX_AgRV8aLYqaA99UaiEnQP5vIaAGIdY6uXp-nhDqBgrRtTTPaY-W6tlcGDpVLs5itiutQyvtEUJ5NqfoY4UcaE_89gZr4n0M1NCZfFa60ivmxHYgfg9yltgWQbSmXgV1W4GL2n9kme4NWj2hLKUmCUzS6in2tPDmnXBjn6PLwz3LXHSss840fwt4GiI3gpFg1naolt_xHoUuaaW7nzXooP8XrKi5pjl8AKEYRTY-t-XgikH_NTkmVlu45_1TljKAv7YLR813wDBZeH2WZA14ANCPat7294bYZAHIG7iBgVqfPOfuJs03KWJqqB6-I1gH0jg4P-M92gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAQxsabM8yayNRmHmpAxqNyS-zB3WC-6h7YKqOAWvuWFFZQyAIccB-2r1y8maBLse9hKtcYHvIb4qlOkX_uIyego6kMGLFGNcdODtwu0HSGFfg1MmQhBbPkX-4SbmtOdrUJgsEdTjtTS6lMSY-Zxc747spoMhQgY7OkUd50UbbO4bswQpSA-REuKye50mwiCw5KyAf2pG1CYL69G3neAgu5lH73SSePmpXgzC9wBmi4enjCItfMnbuJjacbQRIx3Vxmmyqddr1XteFp493V7RTax1WugJczN8iMkkWPaK4hF41wcL24nzn3hrxPfTpbR3rjFQFUmLZanIPC7Y-CN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=lcUPQM7GDDYlJ1Z_Lc7Edt12oRAFdufyQ1znaJ6U6MvX9aXueC7SdYAoQMYPax3h8b46Ofvrni45nCaCtIXXBtHFMPncpza7ngZ6npxMuuwedpsjn3vv1cbDHA-54tZlTvMV39iYVT3rukL4v-Fxp6DD2nHk_bsaZRJB7PQaJeGyixQuwR6NqwbuItV5PXCIldonDJswFf-70DNEELGoiv3_WzTqJLbBFddlV6a215VLMBPIntEoSusS4y0bj9VVntMQ88Sa1CR2s9ISgBbiyqhwvCsUzdq-TODsYz3uFGKqoeYXcmbNnCY0WIps1ZzOoRw0dTFvUywiJvgISL2WHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=lcUPQM7GDDYlJ1Z_Lc7Edt12oRAFdufyQ1znaJ6U6MvX9aXueC7SdYAoQMYPax3h8b46Ofvrni45nCaCtIXXBtHFMPncpza7ngZ6npxMuuwedpsjn3vv1cbDHA-54tZlTvMV39iYVT3rukL4v-Fxp6DD2nHk_bsaZRJB7PQaJeGyixQuwR6NqwbuItV5PXCIldonDJswFf-70DNEELGoiv3_WzTqJLbBFddlV6a215VLMBPIntEoSusS4y0bj9VVntMQ88Sa1CR2s9ISgBbiyqhwvCsUzdq-TODsYz3uFGKqoeYXcmbNnCY0WIps1ZzOoRw0dTFvUywiJvgISL2WHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفت.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
آپدیت:
حال‌وش روز چهارشنبه ۱۱ شهریور ۱۴۰۵، به نقل از شماری از شاهدان محلی خبر داد که پیش از انفجار، صدای دو پهپاد در منطقه شنیده شده است.
این رسانه، علی ملاحی، صاحب خانه و پدر عروس، را یکی از شاهدان معرفی کرده است. او گفته پیش از وقوع انفجار صدای دو پهپاد را شنیده و پس از آن، ساختمان هدف قرار گرفته است.
شماری دیگر از ساکنان کوهستک نیز از مشاهده یک پهپاد یا شنیدن صدای آن خبر داده‌اند.
منابع محلی همچنین می‌گویند خسارت‌های واردشده به خانه تنها ناشی از ترکش انفجار در یک محل دیگر نبوده و یک یا چند پرتابه مستقیما به ساختمان اصابت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=GZ5DDph4R2ppFEOg3-g8Xcwitp9A07PEhCrEpI2FW6NhS3bw_u8o49_PYDgeEyER2Kc_1Vxdar1oVeMF96JMh0wz-WRLCC3uFuVvNG4AwGo5p9HkE-vkWNpg7mFA8-swsFi1zLUDxkI2aEIQhOpGDnIMfdhjjotwP2QLNk96v35gOiRpMTDz8Xeq_6JPDRnb_LRCgls1VESUXziSpBYDiDIqeAlg7IHodUwOorLM7FbcVV1PhxrMgag6PnP6LNHOh6ba4ApOOEtw6NqnokIiMTZ5ZgXkfcx0lvyM290epCCMgN2mqb5KzpR-i-m9lmNBY-AbhSR5Kmq_hKBOeKjqdItwswMxAUn9BrijLriHr9rPoFLl-DH2dgJSFVVDOHqMcGhawqA1Z1mWsSQq8cyJ5RfPf-MYzn3mAk2AK_5SPUGmbHVcN_8d1n0EDgfaZoN5S2c-K4guU-RUFkn8L_9VQW-R0z-nvx7k9Cm_UaEbdRqGHYRXky0QRlLDofmnzff68CmHs-WJPI76-dx8CTPYgBTE9IG-RlipSktfVncaJsC__SA1sW_iCyuWZk7FKrHoBpr0Wg9A5sMWf588wKWJhf2yv-cbaycl96P42rAefpwfKn4nRY725Zr3DrxSUaYw-ggcvzGeBQtMRDKYih-B6d4B3GNZermNjoY25qSRxOo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=GZ5DDph4R2ppFEOg3-g8Xcwitp9A07PEhCrEpI2FW6NhS3bw_u8o49_PYDgeEyER2Kc_1Vxdar1oVeMF96JMh0wz-WRLCC3uFuVvNG4AwGo5p9HkE-vkWNpg7mFA8-swsFi1zLUDxkI2aEIQhOpGDnIMfdhjjotwP2QLNk96v35gOiRpMTDz8Xeq_6JPDRnb_LRCgls1VESUXziSpBYDiDIqeAlg7IHodUwOorLM7FbcVV1PhxrMgag6PnP6LNHOh6ba4ApOOEtw6NqnokIiMTZ5ZgXkfcx0lvyM290epCCMgN2mqb5KzpR-i-m9lmNBY-AbhSR5Kmq_hKBOeKjqdItwswMxAUn9BrijLriHr9rPoFLl-DH2dgJSFVVDOHqMcGhawqA1Z1mWsSQq8cyJ5RfPf-MYzn3mAk2AK_5SPUGmbHVcN_8d1n0EDgfaZoN5S2c-K4guU-RUFkn8L_9VQW-R0z-nvx7k9Cm_UaEbdRqGHYRXky0QRlLDofmnzff68CmHs-WJPI76-dx8CTPYgBTE9IG-RlipSktfVncaJsC__SA1sW_iCyuWZk7FKrHoBpr0Wg9A5sMWf588wKWJhf2yv-cbaycl96P42rAefpwfKn4nRY725Zr3DrxSUaYw-ggcvzGeBQtMRDKYih-B6d4B3GNZermNjoY25qSRxOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=Qxg3JulP-wEfZ3AwmZ-nCHVGEy73rwp1-Q_SzTbFEHcC00fzJAUWccLWx5FqrrzgTVMOhxin8nm0QY3_brmB5f_VPf3amVlgvIYo8G5rksEV2xvqFHLi97ys29T_U9kHJ2Th4m8wEJsAeuNW3JxrJEwQ8fpZId5J0cOLs7C6NNFPQWBUzEBxcn1mBJqwaKhIyTp0nmODgz-k7QWC4KBm7kKKlOFAw0VtPHt44J2K5L7vgGFjt1OjOiCoTWd04uQpGVBCVWbG0ypwlpbA_8xA--KiW0BAJyxB5zca2i9VIBrUiQGRMvyXTgRKYHvKO3KSvCd_7vV0pK9bTqANdgZTow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=Qxg3JulP-wEfZ3AwmZ-nCHVGEy73rwp1-Q_SzTbFEHcC00fzJAUWccLWx5FqrrzgTVMOhxin8nm0QY3_brmB5f_VPf3amVlgvIYo8G5rksEV2xvqFHLi97ys29T_U9kHJ2Th4m8wEJsAeuNW3JxrJEwQ8fpZId5J0cOLs7C6NNFPQWBUzEBxcn1mBJqwaKhIyTp0nmODgz-k7QWC4KBm7kKKlOFAw0VtPHt44J2K5L7vgGFjt1OjOiCoTWd04uQpGVBCVWbG0ypwlpbA_8xA--KiW0BAJyxB5zca2i9VIBrUiQGRMvyXTgRKYHvKO3KSvCd_7vV0pK9bTqANdgZTow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، و دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، روز چهارشنبه توافقی نفتی را در کاراکاس امضا کردند که بر اساس آن ایالات متحده کنترل اکثریتی بر ۶۵ میلیارد بشکه از ذخایر نفت ونزوئلا به دست می‌آورد.
این میزان حدود یک‌پنجم ذخایر عظیم نفتی ونزوئلا را شامل می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، این توافق را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده است.
بر اساس این توافق، آمریکا به ۱۷ میدان نفتی ونزوئلا دسترسی ترجیحی خواهد داشت؛ تأسیساتی که برخی از آنها پیشتر در اختیار شرکت‌های روسی و چینی بوده‌اند.
همزمان، شرکت شورون نیز از توافق جداگانه‌ای به ارزش هفت میلیارد دلار برای توسعه دو میدان نفتی دیگر در کمربند اورینوکو خبر داده است. شورون می‌گوید این سرمایه‌گذاری می‌تواند تولیدش در ونزوئلا را طی پنج سال بیش از دو برابر کند.
وزیر انرژی آمریکا پیش‌بینی کرده است تولید نفت ونزوئلا تا پایان دهه جاری به بیش از دو میلیون بشکه در روز برسد؛ حدود دو برابر سطح تولید در ژانویه، زمانی که نیروهای آمریکایی نیکلاس مادورو را سرنگون کردند و دلسی رودریگز قدرت را در دست گرفت.
این توافق با انتقادهایی نیز روبه‌رو شده و منتقدان دولت رودریگز را به واگذاری حاکمیت ونزوئلا بر منابع نفتی خود متهم کرده‌اند. دولت ونزوئلا در مقابل می‌گوید این توافق به این کشور برای بهره‌برداری از ظرفیت‌های انرژی و جذب سرمایه‌گذاری کمک خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78195" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBGdKm-RH4J3q5o5I-azlMvlhUZvpx9Z48HXrBm4nsPayZzWug7H4b-YaPMsOG5Wyq8dqPkvIeIQX3-3TGqmEZ0qKeUWC347BVTInIw__CuHnihi9yJIGK3JOpiswVpJbi-JAyhixNaiM5vtoYgTXDmZnuRdoPqZz33ec4CKSd-Hfd7P0oburNiabQRR9NpxSsp4e3ziR7XfhrSXqcaq6rGOdYJMx268shRwzzbuVamPB6gLVAfRX3dO946mv9mXxAMdYXw4QCuCl2Jm_a_2WG-cdld6298eUgs08iiQnPpG3aQeYeIU8ooZ6qBax8abAcj3B7BmKZsW0UeHb96kgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=rvKGprOnautlpwyikZTWNm1hW5Nxq-jLtcpWT28tyntiGnAiBXotuxB57YTvu73U17Homivmi8aoIRnNg_U3Oc_tjE8IIWxpp-P5V4a2_hkwdV3FXtua6vgaNB0kK7Gp1spoXF0AyxGlyUBfM_kPAZp5kE-yGyPe0ne0LkOeR1VOKpS83SIWEKqDnS4AObUjhuwdkkwOp590XuuqzUVY4gKQ41Vc9yNZKIPpM_qJ81yltshRM6DmuOw3eYMZzZIFqFAlXz-zgadF0GT9n-WAOPp3NKVt_HjCmRZfqKtiWViq_X3BLRUB97cRoH_8WJq8vAX7ak1qZeI6S9Le374ukA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=rvKGprOnautlpwyikZTWNm1hW5Nxq-jLtcpWT28tyntiGnAiBXotuxB57YTvu73U17Homivmi8aoIRnNg_U3Oc_tjE8IIWxpp-P5V4a2_hkwdV3FXtua6vgaNB0kK7Gp1spoXF0AyxGlyUBfM_kPAZp5kE-yGyPe0ne0LkOeR1VOKpS83SIWEKqDnS4AObUjhuwdkkwOp590XuuqzUVY4gKQ41Vc9yNZKIPpM_qJ81yltshRM6DmuOw3eYMZzZIFqFAlXz-zgadF0GT9n-WAOPp3NKVt_HjCmRZfqKtiWViq_X3BLRUB97cRoH_8WJq8vAX7ak1qZeI6S9Le374ukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با شبکه نیوزمکس گفت که ایالات متحده لزوما به دنبال فروپاشی جمهوری اسلامی ایران نیست، هرچند تحولات درونی و قیام مردم امکان‌پذیر است.
او همچنین به مخاطرات شخصی پیش‌روی رهبران و فرماندهان نظامی ایران با افزایش فشارها اشاره کرد.
بسنت ادعاهای ایران درباره کنترل بر تنگه هرمز را رد کرد و گفت با عبور حدود ۱۷ میلیون بشکه نفت در روز گذشته، کنترل ایران بر این تنگه بی‌معناست. او همچنین گزارش‌ها درباره وجود مین یا برخورد دو کشتی با مین در تنگه هرمز را تکذیب کرد و رسانه‌ها را به بازنشر سریع ادعاهای نادرست ایران متهم ساخت.
وزیر خزانه‌داری آمریکا، با اشاره به تداوم خرید نفت ایران توسط چین تاکید کرد که تنها حدود ۳۰ میلیون بشکه نفت ایران روی آب باقی مانده و این ذخایر نیز به‌زودی به پایان خواهد رسید.
بسنت روز گذشته نیز در جریان سخنرانی در مجمع اقتصادی جی۲۰، تاکید کرده بود که فشارهای اقتصادی یا به ایجاد شکاف و دودستگی در سپاه پاسداران و احتمالا مقابله مردم با آن‌ها منجر می‌شود یا مقام‌های تهران تصمیم می‌گیرند که به میز مذاکره بازگردند.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با شبکه آی‌۲۴ درباره حکومت ایران گفت: «نیروهای ما می‌توانند هر لحظه در آنجا باشند. ما این حکومت را شکست خواهیم داد.»
نتانیاهو درباره اینکه آیا منظور او از شکست دادن، سقوط کردن حکومت است، گفت: «بله، سقوط خواهد کرد و ما آن را سرنگون می‌کنیم.»
نتانیاهو در پاسخ به این سوال که آیا رومان گوفمن، رییس موساد، برای سرنگونی جمهوری اسلامی فعالیت می‌کند، گفت: «همه دستگاه‌های ما تحت هدایت من برای سرنگونی این حکومت و شکست آن فعالیت می‌کنند.»
نتانیاهو گفت: «در نهایت با سر اختاپوس، برخورد خواهیم کرد، بازوها را قطع خواهیم کرد و محور شر ایران را هدف قرار خواهیم داد. این کار را با قدرت بسیار انجام دادیم؛ خلبانان ما آنجا بودند و هر لحظه می‌توانند آن جا باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78193" target="_blank">📅 21:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lPdwMkI-KXoBOZ0b_dB3Kh999iTZkkJoifXbbErbSr6mjXXCKjrtb8gX7P0yv901APxU1XBbtlkcnlEurdIAvKgZ7tn0fp-6P3CxezGLXDqW5UmmcBH-Pn9z4SgiPWqjwiITLJxiUMde672wuRcLsAiracexlS0p2EBtxM114XLgG9jdw1kfBZ61U7Ueysq8RR8ByCkH-miypqMus_GzZJN16Txd7T_rYCNOcv0nsGpWjPAKYqRWybm8xeglPffHt7pD-XyvMWzmR187NznD7nmNUu9O6K6Vw3bZpRwGfJsvoS--A5lHmFo-y584JB5Qr0O67urC5OXNCal9OrbiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی جمهوری اسلامی، با هشدار به ایالات متحده گفت تهران در جنگ جاری از «راهبردی جدید» استفاده خواهد کرد.
رضایی، چهارشنبه ۱۱ شهریور ۱۴۰۵، در پستی در ایکس نوشت که تلاش‌های آمریکا برای خروج از شرایط کنونی نتیجه‌ای نخواهد داشت و افزود: «به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، پایه‌های شما را درهم خواهد شکست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78192" target="_blank">📅 19:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QhXcplbFqbNTM7TM6hS5GhoU7rL3wDK5JdbFC1gFTbSTKnTsqYfbV0KSjU7BgY8sULJDzX77UJgBIPm1j_8oS32yswwXANuI9ndzP-gre6Wq64h4igv1hL0ITnXBpbqSZRSZdNWWvQ2YQsEoxZQHGmGgO3wSLCF8RqfEzBQmUEocTDddosrB6OX8N3rWQwKobZyDK4X9QMrnKjGoAFobqfp3amVlDEI0_x2kHcpeRQyy-v_3FOYZttA4F7exf1Vg8cmXk954EbUnT49wSwuwJ7oJitG9AOYCapj8oaY_1n5dZ17adEpuozRk89mG6fhDma-vHd_fNLPlShVcJjkP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حالا که آن را تحت کنترل ایالات متحده آمریکا درآورده‌ایم، آیا باید نام «تنگه هرمز» را به «تنگه ترامپ» تغییر دهیم؟؟؟ درست مثل خود آمریکا، این تنگه هم «داغ‌تر» از هر زمان دیگری خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
Now that we have it under U.S.A. control, should we change the name Hormuz Strait to TRUMP STRAIT??? Like America itself, it would be “hotter” than ever before! Thank you for your attention to this matter. President DONALD J. TRUMP
realDonaldTrump
در خبری دیگر:
ترامپ در گفت‌وگو با پادکست «دن پاتریک»، درباره حملات سه‌شنبه شب آمریکا در اطراف تنگه هرمز، گفت: «ما اکنون کنترل تنگه هرمز را در اختیار داریم. ما آن را کنترل می‌کنیم. دیشب ۲۸ کشتی را از بین بردیم. ما آن را کنترل می‌کنیم، آنها چیزی دریافت نمی‌کنند و ما کشتی‌ها را از بین بردیم.»
ترامپ همچنین درباره حکومت ایران گفت که جمهوری اسلامی دو هفته با داشتن یک سلاح هسته‌ای فاصله داشت. او افزود: «اگر آنها سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت، خاورمیانه از بین می‌رفت و آنها به شهرهای ایالات متحده حمله می‌کردند. چون آنها دیوانه هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78191" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntUMNaorhy-iiQEveUczq23E88ZF8rlbWyOzzEr9AuqZDjP8TCbGIk41fuM9lb754Br5VwoDSE_3N4IgLpZACPP6AaO13InDo-INeCWc5d1hgbb-FLj7C18YDn6LsmnRfKhFHHYyZqJJM2oTVBxN8sy1efb1Ig-PmR0wJp1rQ8ZJ27pwpKhIdo1zo4TJIi0VjDT4yNBosu8BNvXxNJ-Zv6YVcIukQtRy2Mxd7Sy39OsgkcIY6xirHkNqxlVBydaMMgh88ZTnnivqizV4niJXaYJlFoInLlTwLWTURB5-jpCO3VHhtmCIniln8ZxHZ4TEm_hpFt55VsKBpOX8nb1kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی گفت: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
محمدباقر قالیباف، در دیدار با مسئول ارتباطات اسلامی حماس گفت جمهوری اسلامی مذاکره را رد نمی‌کند، اما آن را «ابزاری برای مبارزه» می‌داند.
او گفت کنار گذاشتن مبارزه با آمریکا و اسرائیل به معنای شکست است.
او افزود جمهوری اسلامی در جریان مذاکرات، پایان جنگ علیه ایران و متحدانش در «جبهه مقاومت» را در ماده نخست تفاهم‌نامه مطرح کرد، در حالی که به گفته او، طرف مقابل در متن اولیه ۱۵ ماده‌ای خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و فعالیت‌های «جبهه مقاومت» شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78190" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNhLdbxGbVXILbtgeNLZkk-6hxlo8z4EFrlWG1nFrh9cZ4ydmg_HyO4Ni5hXLbZPtRWZq-S6Kx6Wh9iZ1Eps4fizidWWtcf7F2jlTjzIkcd2LW-gGxuPzh7AMeaXzQkTZBz76E2xIov5cNYCEcmVqdaaEz1qazUT-DLMBGHAJniJ4IFM27Jbt4NYSxIaIe_i8e4YfbZwHMgt4V8B4ugdH4cNN5X6gNxLSQAthAQZ2DrCfXjnL7ehvtRzc5w6TL9iLmFBlBufzq6mTqXdQzqjMtwjGewavPs13ehWQa1wOcy4OJdSdPfBxwOw3qiL3YCNaYLfFmDow2Wqx8WoHfUqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آمارهای اعلام شده از سوی شرکت ملی پخش فرآورده‌های نفتی ایران، میانگین مصرف روزانۀ بنزین در نخستین هفتۀ شهریورماه از مرز ۱۴۸ میلیون لیتر گذشته است.
بر اساس این آمارها، بیشترین میزان تقاضای روزانه در ۸ روز نخست آخرین‌ماه تابستان، بیش از ۱۵۴ میلیون لیتر بوده و در این بازه در مجموع بیش از یک میلیارد و ۲۰۰ میلیون لیتر بنزین عرضه شده است.
کاهش شدید ظرفیت تولید در ماه‌های اخیر در اثر حملات آمریکا به تأسیسات نفتی ایران از یک‌سو و مشکلات دولت برای وارد کردن بنزین از سایر کشورها از سوی دیگر، باعث افزایش قیمت بنزین و حتی مطرح شدن احتمال بالاتر رفتن قیمت این فراورده و افزایش شدید تقاضا برای آن شده است.
مسعود پزشکیان رئیس‌جمهور و شماری دیگر از مقام‌ها تأکید کرده‌اند که دولت توان چندانی برای وارد کردن بنزین و بخصوص عرضۀ آن با قیمت‌های قبلی ندارد.
دولت ایران اما در عین حال ادعا می‌کند که تشکیل صف در برخی جایگاه‌های عرضۀ بنزین، ناشی از هیجان و بار روانی بوده و مشکلی در تأمین بنزین مورد نیاز کشور وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78189" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H_UpDU2JeH7XdvLRHNOvqHQ18QMQsIziaIbKvXmf7h3ZKzn5s_B_mQbeEC4l6KmUX32cNojSKWyf7EgJpz95y3hj4Qg3pN57l6ALgHT_kDFkOgjm0K0gYNESw5gtPjzYHRCHHWQOWvt_QatLIFRvazmg7Wg2H6ywDhrPW6uVZ745qPizg4-IfDdhOFpM9cTUm_3mlh4BOPFDhNvl-wo1GHUHLXspmuKlj-bpsXtUiOTZ6LJ7cgMiCxjc8Qs4SxY3528043Lzl6YjnKY6zfg1a8nwvpa_VdjVpO88s_Eqw-uEBvg4h9MjOgRgXuUivzR_NfMiJbzjf0uYksr3SVdokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در ایران بامداد چهارشنبه ۱۱ شهریور و ساعاتی پس از دور جدید حملات آمریکا، رکورد تازه‌ای ثبت کرد و قیمت یورو، پول واحد اروپایی، برای نخستین بار از مرز ۲۵۵ هزار تومان گذشت.
وب‌سایت‌های اعلام نرخ ارز قیمت دلار از جمله «نوسان»، قیمت دلار آمریکا را حدود ۲۲۰ هزار تومان گزارش کردند. قیمت درهم امارات هم به بیش از ۶۰ هزار تومان رسیده است.
افزایش قیمت نرخ ارزهای خارجی در بازار آزاد ایران از زمان اعلام امارات در قطع روابط مالی با ایران و آغاز برنامهٔ فشار اقتصادی آمریکا موسوم به «عملیات طرد اقتصادی» شدت گرفته است.
در دو هفته اخیر پول ملی ایران در مقابل ارزهای عمده خارجی بیش از ۱۰ درصد دیگر از ارزش خود را از دست داده است.
روز چهارشنبه قیمت سکه طلای موسوم به «امامی» هم با وجود کاهش جهانی قیمت طلا، ۲۲۴ میلیون تومان گزارش شد.
عبدالناصر همتی، رئیس‌کل بانک مرکزی، روز ۱۰ شهریور ادعای کمبود منابع ارزی و احتمال فروپاشی اقتصاد ایران را رد کرد و گفت بانک مرکزی آماده است برای مهار بازار تا دو میلیارد دلار ارز عرضه کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78188" target="_blank">📅 16:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UCtiaje76HTA6i1rUuvCDVZ2B91js1P3UdCAFzFZAh-x9rCgaGltpjOAjxDJj4SPopkKVc-hzojvVeksfaumWU6wtSkpvmlIKW190NIRE3kGrBY4Y3t09zyqC7g4wx7b31S9r2OL8E3HosB6ppeJqVegXyUVo4KdSALBYUYk3-SAuGHc-BKeL1IhpJiXsOJMtHChfapyFbV0nnGLeENCFBeQL8ZmyXoYF7b1P_aduIZ1P1fGNJD7e3HDYo9K9Wd7Li0ec-7k7JPjV_ck1zymdbOTk24mWahU_5pODCR0YzZT_cNr4KAIflUxALX5DnNPCGQ3AydovMVeRUTOMJ0_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد که ارتش ایالات متحده در جریان موج حملات شامگاه سه‌شنبه دهم شهریور به اهدافی در جنوب ایران، «دو نفتکش دولتی» این کشور را نیز هدف قرار داده است.
بر اساس این گزارش، این دو نفتکش در نزدیکی سواحل ایران و در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند و پهپادهای آمریکایی با شلیک موشک موتورخانه‌های آن‌ها را هدف قرار دادند.
فرماندهی مرکزی ارتش آمریکا، سنتکام، در بیانیهٔ رسمی خود پس از حملات سه‌شنبه‌شب اشارهٔ مشخصی به حمله به نفتکش‌ها نکرد، اما در تصاویر ویدئویی که از حملات منتشر کرد، صحنه‌ای از اصابت موشک به نفتکش نیز دیده می‌شود.
اکسیوس می‌گوید این نخستین بار است که ارتش آمریکا نفتکش‌های ایرانی را نه برای جلوگیری از نقض محاصره دریایی، بلکه در واکنش به حملات ایران به کشتی‌های عبوری از تنگه هرمز هدف قرار می‌دهد.
یک مقام آمریکایی این اقدام را بخشی از سیاست تازه‌ای موسوم به «نفتکش در برابر نفتکش» توصیف کرده که به‌گفتۀ او دونالد ترامپ برای بازدارندگی از حملات بیشتر ایران به کشتی‌ها تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78187" target="_blank">📅 16:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SD7hrw_-Gu-LUnukEjpF4drax7cbegsNfWSrXC9f3u9_h737jUV8w_gqDhmpeiABNTBnWrxZhnU7lV3pivggXfUUe4aJqkeFPGNAe2IF8uy5PwApd1tdh5pp470eNtOCJy7NuFyL9PwLEHqT75Y7sSmM7daKvoMwgtkruLFrlHy1AxdwE2_Ozo_3GrBuF2CI5AMaKSIrykP_oHrCc6uw0CYMriITS6dEHPDpxJ1Mz9YR9h17a0b2u3a19uJmh33pPTllfN6TUoXV6pXwI3sBiH7vOCmHlyV-Me57dX07ldoybrSawufSvDKzR5oVqVCrbLIA9vlKmtzn2O7KTMYz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nk-fYaYl431aZhO3boozQAlAawUSDcuX-Y2IzQRcVtKe9u8ENqVBx-K7ZIzIywTqBdV_0W8yXq9Fu1fvnju2WEAO-wcQyJxqGQz7heljShjaU8tjecU9-O5itO4-MMdyf7d5ssMnxZAk-Q3YN7GxapUFE_GyFQ5Y_ASemJgjUwOY2krhV4-tsJsb06i0w6BJKupBmkep8UFffmGvIzlu6ib7q_MuT-PXHjQ_yTF8-CpMEr6DanO7d1SSzzd8l1gFcgrreiIQe08RZeqcNOnyAs6jDXdZ1Uxw75f2wIVg7j24A1uOIAZ0G7qX0V7GUPXpmqkErSuoDU7UXgVZ-17yAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=LLXB1k9GL6PM4cjQ2kb7US8h5BM5erOmvWgsRRFJsdfyD05ASnxIu7w_E9xu4arfLjtLR3fzWbz4HxEVcyBQIuOOFUGvgEHI1TyAU7I0UtSZmb-QNbAGMyk46xuWatr-qz6T84ph4KYHpMTjK3dWi_FPsDdrcVys1ItgU5KgDwk8GOqaxS6FEK9p2LgdQIucF-azuCpUqDZvKMM_6YDJZ2h7HrVP7_hKIorsFIqcb4DsUmPqdpKIag6lDBZDASfMQgoV5d6mQ38v43Q7a93fxCS463oj29aMLu_MhRD7KRTe9rjXm3A3GecvFlBMhgtdUwLs4_dXDcNR7F4ov40RDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=LLXB1k9GL6PM4cjQ2kb7US8h5BM5erOmvWgsRRFJsdfyD05ASnxIu7w_E9xu4arfLjtLR3fzWbz4HxEVcyBQIuOOFUGvgEHI1TyAU7I0UtSZmb-QNbAGMyk46xuWatr-qz6T84ph4KYHpMTjK3dWi_FPsDdrcVys1ItgU5KgDwk8GOqaxS6FEK9p2LgdQIucF-azuCpUqDZvKMM_6YDJZ2h7HrVP7_hKIorsFIqcb4DsUmPqdpKIag6lDBZDASfMQgoV5d6mQ38v43Q7a93fxCS463oj29aMLu_MhRD7KRTe9rjXm3A3GecvFlBMhgtdUwLs4_dXDcNR7F4ov40RDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح چهارشنبه؛ وضعیت چند منزل مسکونی در کوهستک (هرمزگان).
@iliaen</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78183" target="_blank">📅 09:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05113c6026.mp4?token=E4FizHSb3Wm0Gf3Mn481JrdsdkLLSWcRru0dak-7TKyKyPYVSmL-OO_-X_KcTNO2sQaCzEgAXwVdkkjZjEIa0gD3zw4Ef-5QCM82N9u_4mDnqByrxuSFyIuGz4xnntU6NcoQAgjURCIDF0wTlrRxTINl8b6bnWChbBTl4bVOYs95z2J8oTNmwzWAga47nbS6PPHHYGE28wAVnFS-992XwA37PG44tnIPZlhHUISBkOdR6e6y_DuBbtjDGyAsREPT8EeowIi0uwKnmKJhRm9G-wrg-GCv6KSWJEo4h1NDcWXKMfbAKVwNSedFK3bE90Ck8b8FkZfKj7Xwy54cTOZu7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05113c6026.mp4?token=E4FizHSb3Wm0Gf3Mn481JrdsdkLLSWcRru0dak-7TKyKyPYVSmL-OO_-X_KcTNO2sQaCzEgAXwVdkkjZjEIa0gD3zw4Ef-5QCM82N9u_4mDnqByrxuSFyIuGz4xnntU6NcoQAgjURCIDF0wTlrRxTINl8b6bnWChbBTl4bVOYs95z2J8oTNmwzWAga47nbS6PPHHYGE28wAVnFS-992XwA37PG44tnIPZlhHUISBkOdR6e6y_DuBbtjDGyAsREPT8EeowIi0uwKnmKJhRm9G-wrg-GCv6KSWJEo4h1NDcWXKMfbAKVwNSedFK3bE90Ck8b8FkZfKj7Xwy54cTOZu7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روستای کوهستک در سیریک هرمزگان
ویدیوی منتشر شده در منابع حکومتی از مکانی که مورد حمله هوایی آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78182" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbb5MzzWJ6qEZfe_7-g-xrpAt3EOgfsL7ub-QlgjH5kgE1XzQ2R6dHi9VcBrChVPflcnZ7MvIZAF7lPRXWzUupPAwnFoo20epnx4t6Rp5vFhpRL846-viyFknAdUu7Ckz5e9lCvU077k5D-HgfvfoG7qvONT9H0DlCahRsgmoEaziLZyB9Epx0dr5hrjzd6sayJAxHxsJneyCakZCQnOURPOylnraMCnzbq8EAQ9ASrjRnMmkaF9Fvuq1oBM-sr7jBknL6nId3Q50RUTRQ0BTeL5s0IxZFFNlZXUZuJtPvH_TaNve-ug5RR2sYGQ8ncbhJ877MYSiq4e_2JdGx8hWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من تلاش نمی‌کنم ایران را، آن‌طور که ABC Fake News گزارش داده، به پای میز مذاکره بکشانم.
اصلاً برایم مهم نیست که آن‌ها توافقی امضا کنند که برای خودشان هم ارزشی ندارد.
من موقعیت فعلی‌مان را خیلی بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در ایران کاملاً در حال فروپاشی است.
آن‌ها فقط دارند روند اجتناب‌ناپذیر را طی می‌کنند.
مردم ایران چه زمانی به پا خواهند خاست و خواهند جنگید؟
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/78181" target="_blank">📅 04:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=VHr3G3e3JAyI46JG_s2otBwF9HcW06aRCg8PpRe9wXL3J-2BJZP7_iaRnp-DDVoDnMtYEWTEVyF22VKsYH8EbP2_A8zEEEYhRAZMVT2waCJ-BBWkd1HcLv83tqE1X0z4TYXEDvXwJ561WLPOC0gWVCtS2C_W8Baeo0Aobjrsew3f4-weiTK5h7u8KuuPKwbRJJXYnUEzt6l2SqN-8FG44EKkaWiGydXFdh6Jjnjkx-tNlJVRDTXP_vA5PMz-l1SJ5h6BZbXzKmjp_1EyxI5hDSwAe-jqIz4onGIY-dZj5CsHwfocFvaes0jhQ707AI6B31RXLqyAL8BA8JbISDRkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=VHr3G3e3JAyI46JG_s2otBwF9HcW06aRCg8PpRe9wXL3J-2BJZP7_iaRnp-DDVoDnMtYEWTEVyF22VKsYH8EbP2_A8zEEEYhRAZMVT2waCJ-BBWkd1HcLv83tqE1X0z4TYXEDvXwJ561WLPOC0gWVCtS2C_W8Baeo0Aobjrsew3f4-weiTK5h7u8KuuPKwbRJJXYnUEzt6l2SqN-8FG44EKkaWiGydXFdh6Jjnjkx-tNlJVRDTXP_vA5PMz-l1SJ5h6BZbXzKmjp_1EyxI5hDSwAe-jqIz4onGIY-dZj5CsHwfocFvaes0jhQ707AI6B31RXLqyAL8BA8JbISDRkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شروط پکن برای سفر قالیباف به چین'
حسین مرعشی، دبیرکل "حزب کارگزاران سازندگی"، گفت: خیلی روشن به ما گفته‌اند که
۱- تنگه هرمز را باز می‌کنید
۲- عوارض نمی‌گیرید
۳- با عربستان سعودی مسئله‌تان را حل می‌کنید
۴-  با آمریکا مسئله‌تان را حل می‌کنید
بعد قالیباف به چین بیاید.
قالیباف در اردیبهشت سال جاری، با پیشنهاد مسعود پزشکیان و تایید رهبر جمهوری اسلامی به عنوان «نماینده ویژه ایران در امور چین» منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78180" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منابع حکومتی:
روابط عمومی سپاه:
🔹
مردم شریف و انقلابی اردن؛ یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن، اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/78179" target="_blank">📅 02:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=GX_CFi0KYw2xBQ-P9W0sQahxsgJNIQzkqCWXp0pG_-U9_gTIyyjVGPu_uZ4Q4rKeZc1S7q_ubkL8gjD_-VHUrLXl1Z8xuz7xtV6sJ0yLmG3QEAWwLz--kSL7g-wtpv93mims9oMV9tWUQwvTn5n9QEL75w_4bWpIsgIFmkGaU6WzYDCa8hYAt7R807SGRVS0ptr71MRqI0_t2VKKCpOPUk-JTixL0k_JQGwvG1Eqy0ARuVubOtd5YM9Vc-XL4eeSxSYyvXlTu5cvylYfZm_hsNikWiI3mpveIOYaQLvI9sLNoLHtgarVZ0GUPBJy2HOGdilWbXAPkQXucm7XhxwreA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=GX_CFi0KYw2xBQ-P9W0sQahxsgJNIQzkqCWXp0pG_-U9_gTIyyjVGPu_uZ4Q4rKeZc1S7q_ubkL8gjD_-VHUrLXl1Z8xuz7xtV6sJ0yLmG3QEAWwLz--kSL7g-wtpv93mims9oMV9tWUQwvTn5n9QEL75w_4bWpIsgIFmkGaU6WzYDCa8hYAt7R807SGRVS0ptr71MRqI0_t2VKKCpOPUk-JTixL0k_JQGwvG1Eqy0ARuVubOtd5YM9Vc-XL4eeSxSYyvXlTu5cvylYfZm_hsNikWiI3mpveIOYaQLvI9sLNoLHtgarVZ0GUPBJy2HOGdilWbXAPkQXucm7XhxwreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متنی که اکانت سنتکام به همراه ویدیوی بالا منتشر کرده، ترجمه ماشین:
سنتکام حملات به اهداف سپاه پاسداران در ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، توانمندی‌های مین‌گذاری و مراکز ارتباطی بود.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتیرانی تجاری در تنگه هرمز و نیروهای نظامی آمریکایی انجام شد.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول فعالیت هستند و همچنان هوشیار، مرگبار و آماده‌اند تا به اجرای عملیات‌هایی که فرمانده کل قوا دستور می‌دهد، ادامه دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78178" target="_blank">📅 02:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qzazep1L6KfMbRGHAFDHxQUlUinKIPPaQ3-YJgmVdp9jPTI_i92BHB_60q_jZ9Q0ZNsf5HSfmyyAWBEv2mFmcrJWPea9fW7xBxuCiURlmSFRJKhzvwKjS30kNI6pQgQqZft101WujTCWKVQmDpw8Eq2PRQEI3qdJp6ukMT3B4cc5a3dTvdUymRGwzMkjuEl4Lg5iEvk8yOZDbjiD-Uz9Osf-ds_Iei0fWxpZITSYKqjdnGEJMrpvf1ToKQ5anSmUwSaqtehik4m1zbAjEAbqu0xn9HY12D-G1oVFq8d1zt-pFvslSc8tY-prpieCIa11H9mFG-nK8JSfISzBiijFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cE1985mazNiw2iLhy7aszemv4JtNyZ7fBtyE_deu6cotD2rAx0L-1p9WhFttmUEsXfz2crCVn5WyDcBZirofyMGvtF4Y-ZSxPXq7We7pSh3lo-uwn4EOCShNQcsTcGbQhc3NioV0zhfJj45dd2QQrq8krKC9FRUhyBZspEyV4dZny3lB0VFBdIwP99Q6hy0YnmLlU6W8RBxC9sABwjgZ7IrLcWdknVDksVzXMhM6rXxp2rYh1rwGrsEIK7LYx4Y8I0Jx3s-gvfvImEU0vu4ruNWFPGPNcnPs0KuO3we84zvOzHN0NcdRpnt0u4UhWu6sTgKn0-u6t6GjUJG_UJVDsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">"ستاد کل ارتش کویت" در فاصله چند دقیقه دو اطلاعیه منتشر کرد که گویا دومی فقط یک کلمه بیشتر داره. ترجمه ماشین:
اولی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادهای متخاصم است.
KuwaitArmyGHQ
دومی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم است.
KuwaitArmyGHQ
ادامه متن:
"ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، این صداها ناشی از رهگیری اهداف متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی مراجع ذی‌صلاح را رعایت کنند."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78176" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78175">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=YhBm53RcxOjy2LStl8YEzj4G0C-Mb3UAAHwnLa6Y9_7b-Wmb5VmVpQBL1zNwqdyuAyUovUpJ8TiXRLRLTzyS2Cbx2WwuNH_8esz7Sunt78Th6Nm3_nLcj_ykNjIHDcU4qxvNOvknl9na4-aJ4l8RYNMSs9A1SClgQJPkFEMBn5q_g4kdqjYzxL6Sz28cFMfQgqJ9ZMmKXN5C0ET37-9sdKz35Twn-nCNh8u6rpZWT5YAhKBSh3WgQCNTN5Mx7RUL87KmrzQJ3Z6W-g2CSSmPsE1jzdPv0_-L_zSkU7Ex4ZjjFPesR_C7RbMHR1xMp_NgbLekz-au0KrLZz93igUoHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=YhBm53RcxOjy2LStl8YEzj4G0C-Mb3UAAHwnLa6Y9_7b-Wmb5VmVpQBL1zNwqdyuAyUovUpJ8TiXRLRLTzyS2Cbx2WwuNH_8esz7Sunt78Th6Nm3_nLcj_ykNjIHDcU4qxvNOvknl9na4-aJ4l8RYNMSs9A1SClgQJPkFEMBn5q_g4kdqjYzxL6Sz28cFMfQgqJ9ZMmKXN5C0ET37-9sdKz35Twn-nCNh8u6rpZWT5YAhKBSh3WgQCNTN5Mx7RUL87KmrzQJ3Z6W-g2CSSmPsE1jzdPv0_-L_zSkU7Ex4ZjjFPesR_C7RbMHR1xMp_NgbLekz-au0KrLZz93igUoHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان ویدیوی دریافتی از شهرستانی در استان ایلام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78175" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9KDOq49wcITlqekpYr1nFLZDytBD7gUD3Bc8IMFhIopSP9PYJYMHEk1vhg9eKz1SOdUZn1Sz9N8kzRC6KgAQd0aa1Ws3aslXIi_RSt_897KkFP5FY3kevuHy0PQVo4oxD0u_npa_2b5IruALerEwQj2-NXvojUHaPWXFXDhoJBF3OZJsVJ-1d8UWs4QR7JnWENVSrZLpxJyG9ZHgbiUrWWQqpB91naEYLhmCNH4wQPu2wC_NXlZ2nk0jFddOHtsIiBp7zDt1-LTitqdbfGFle-MhMl_ZcZjfzk5CEi6-4PnW21DzRwWeH3okqmODtI1BNxNJlxFjCscCGEC5iWXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار در کویت
ترجمه ماشین:
هشدار: خطر قریب‌الوقوع
............. تهدید امنیتی .............
همه موظف‌اند در مکان‌های امن بمانند و برای تضمین ایمنی عمومی، از پنجره‌ها و مکان‌های روباز و در معرض خطر فاصله بگیرند.
دفاع مدنی — وزارت کشور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78174" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=EOyQdbH4FAYA28SpDMOalyGbow_dgdujlkJ0wWtHyDY6qXCJXaV4lbk71ivqZ_MedsQYDCyEM7-QbHx76U8LSHS5YprheSSh8_qAuBtplxJ4FZ-VIuY95VPrjjv2ovccBg0pArNy6gdlngs5UhYCoRUEXCgR8RkOH3kavm2D875a06QCrJFg5RQVjqyapHppLpe9lexCqrYKIEFfmdHuJPNf4vLE46Qc3YiBU6w_xit4AQ5UhwCPnti1mCYXSs3FcwTIH0OtvyWn4nDZQTWgPeqfwpXHY26fODLQxPJVBCdtcVNr1Ne4brIefbSI_HyRmJbC__2hDYyMgycmADqXXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=EOyQdbH4FAYA28SpDMOalyGbow_dgdujlkJ0wWtHyDY6qXCJXaV4lbk71ivqZ_MedsQYDCyEM7-QbHx76U8LSHS5YprheSSh8_qAuBtplxJ4FZ-VIuY95VPrjjv2ovccBg0pArNy6gdlngs5UhYCoRUEXCgR8RkOH3kavm2D875a06QCrJFg5RQVjqyapHppLpe9lexCqrYKIEFfmdHuJPNf4vLE46Qc3YiBU6w_xit4AQ5UhwCPnti1mCYXSs3FcwTIH0OtvyWn4nDZQTWgPeqfwpXHY26fODLQxPJVBCdtcVNr1Ne4brIefbSI_HyRmJbC__2hDYyMgycmADqXXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس راهور جمهوری اسلامی ایران:
یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78173" target="_blank">📅 01:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=HGGRum4tnj_PCKbXWD_X6VgTPfSjcAtj7Ku3x9I0vFgTLRLCmcW06ZRrQyNH425aAHnY2AOazah7rGCLxukh0WRyRigqFqOFzLGB8QXgJcvj6v7ahJLOATboBND8rlg21av3sXOo9GQxv8pKxwG4Mko7hL8r9tGLwt_DBkL1ZRvx5lNDih8Dhs94CQNDIqR0mPAx0xYSOOfLxtF3SYS5g4h0yrbn5dcev9gojlwPkDfAsbuRVSqw18L3PfjeboaspOPH3a5KFYV04BnxUsUeMk-4Z1HCMgEuQ0GPIQNqE4nDlf_3QzYvIj5Br2YvWE1OQdeV-EcylVmgxtV_0VRKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=HGGRum4tnj_PCKbXWD_X6VgTPfSjcAtj7Ku3x9I0vFgTLRLCmcW06ZRrQyNH425aAHnY2AOazah7rGCLxukh0WRyRigqFqOFzLGB8QXgJcvj6v7ahJLOATboBND8rlg21av3sXOo9GQxv8pKxwG4Mko7hL8r9tGLwt_DBkL1ZRvx5lNDih8Dhs94CQNDIqR0mPAx0xYSOOfLxtF3SYS5g4h0yrbn5dcev9gojlwPkDfAsbuRVSqw18L3PfjeboaspOPH3a5KFYV04BnxUsUeMk-4Z1HCMgEuQ0GPIQNqE4nDlf_3QzYvIj5Br2YvWE1OQdeV-EcylVmgxtV_0VRKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پیکر بی‌جان
ویدیوهای منتشر شده در منابع حکومتی: یکی در
#مشهد
با خودرو کوبیده به تجمع بسیجیان
سه‌شنبه ۱۰ شهریور
Vahid
دست‌کم چهار کشته در برخورد خودرو به تجمع‌کنندگان در مشهد
دقایقی پیش خبرگزاری‌های ایران گزارش دادند که راننده خودرویی که به میان تجمع‌کنندگان در بلوار وکیل‌آباد مشهد راند، بازداشت شده است.
خبرگزاری صداوسیما گفت که در این حادثه «۴ نفر کشته و بیش از ۱۰ نفر زخمی شده‌اند.»
پلیس راهنمایی و رانندگی مشهد گفت که یک ماشین «هیوندای جنسیس با سرعت بالا منحرف شده» و پس از آن به میان جمعیت برخورد کرده است.
گفته می‌شود این خودرو به «تجمع‌ شبانه حامیان حکومت ایران» برخورد کرده است.
هنوز علت این حادثه از سوی مقام‌های مشهد اعلام نشده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/78170" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AEnK7gTy2Nv5pU4y_LET3dRrG2b6INk75LcyWmTx4s19leQBYpRfib-UJRZIzYqBBuC-CPHiIHq9Z-ubzWXLbCS2TObRlGzCnhNWISvZYiRcuLsvD6Y9pQ3_1LppQvebsgi-LzVKwz7am0-klIuaRFBSG2FtG99rUmrQEV4nsakmgD_KqlfapXgMh1svhlg2bsC1HRUno6YxYwzFGIZzA3tlwk-MRCIGNG4tIDrs4xx1RzQO-9PJr8V5Z21GgfmjvzQJBi8nZepGKAh7rq6Zo-G23FRbo89aOuIgMpAkoaCrSF-ZvAWF_OoNMspGiYrOP6em3dP6Mr4AtfxRuQemqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L5XqOJ9zQakZry3Ex3niMbMt7ldqUGNjOhr0rjQB-eSJoddplTKHRBkZ31_rPdZXucLPPWq0fDYxOeir5Nfnm-wiOd7TQKbohD-l_XI4Tump-QCCV96Y1paXkyEbOHDo6SRrSZQlLvbi4JZG29X6PXrGEGhUwrRcLFVP_hSOn9-yC83hYsAASZlFk9XOG3Elyoy5a1fZRTAhTeOqCAlDrlITlJdeNEjrA8_tMw-f-7XI8HIPEmv1DKrkwHzP02Sel4ilL5sh2zmDyYirrd8uINosI_rUtUmq-L9ReF3n7oKhO_8BsVImu0oZs1NbGF-deX9UZevaCrVIMWvUjHur5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت دکل مخابراتی کوهستک که در منطقه مسکونی واقع شده بود.
@iliaen</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/78168" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=ZChEBCDdpJ4mPQciYaPXZHeqUS1RAK96vTT84Z3IBHRe2s4uwJlhzR_SGKPhT0ikwJkYWFy-hExPAr6473-74nicWfrd5G-3UPOlB-XA0JVmrX_MUGm0ZkoTOSCrOb-MVh2JVD7-7hYQsc81ny8lwc50m6KXU0r0TJaj7BnKDTJzOOBIWpxUFIQKuAtaXarKk345_5UbOCvFcQH9OdcfN_2RjU190xfOgfOyfWqO7RWn8ebc1MKInZDAy16GTPsid1XGOn6aB6RZTAVI3JhJpGnhoDuc6b1Aq7yNDFZ7T13uAkq2c5wANrV5-gMwZrn9dqZ4TPgk9pbD8YGeyuDOMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=ZChEBCDdpJ4mPQciYaPXZHeqUS1RAK96vTT84Z3IBHRe2s4uwJlhzR_SGKPhT0ikwJkYWFy-hExPAr6473-74nicWfrd5G-3UPOlB-XA0JVmrX_MUGm0ZkoTOSCrOb-MVh2JVD7-7hYQsc81ny8lwc50m6KXU0r0TJaj7BnKDTJzOOBIWpxUFIQKuAtaXarKk345_5UbOCvFcQH9OdcfN_2RjU190xfOgfOyfWqO7RWn8ebc1MKInZDAy16GTPsid1XGOn6aB6RZTAVI3JhJpGnhoDuc6b1Aq7yNDFZ7T13uAkq2c5wANrV5-gMwZrn9dqZ4TPgk9pbD8YGeyuDOMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: '
در حمله به سیریک ۴ شهروند کشته و ۶۵ نفر زخمی شدند
'
ایران گفته است در حملات هوایی آمریکا به بندر کوهستک شهرستان سیریک، چهار نفر از جمله یک زن و یک کودک که در مراسم عروسی شرکت داشتند کشته و ۶۵ نفر مجروح شدند.
رئیس دانشگاه علوم پزشکی هرمزگان گفت دو نفر در محل کشته شدند و دو نفر در بیمارستان جان باختند و «شش نفر از مجروحان در بخش مراقبت‌های ویژه بستری‌ شده‌اند و ۲۶ نفر هم در بخش‌های جراحی تحت درمان قرار دارند.»
@
VahidHeadline
در همین رابطه یک منبع محلی به بی‌بی‌سی فارسی گفت به گمان او هدف حمله هوایی «یک دکل مخابراتی» که در فاصله «چند متری خانه محل برگزاری عروسی و آن طرف خیابان» قرار داشته بوده است.
@
VahidHeadline
در پیام‌هایی که من دریافت کرده بودم هم نوشته بودند هدف حمله یک
دکل مخابراتی
بوده و در اون حمله شهروندانی در خانه‌های اطراف، از جمله در یک
عروسی
، کشته یا زخمی شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/78167" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=NMSJuFs_gXJXugzRibz8sUpFZ1R8PExZhwBEpWQLAb26L32ZHqvQLDIWKg57SpS9sKfDG0rqyslJ98thzQEtHeGAnIKYLwed1zOvixCiMzY1ElcnIKufk1olKSM6I3E3bdHNvxoVvhZfJKk5YsYYTFOvKEXfiR_WTPAai4_kRWxWVFHwT-ISP1fFJ1EN7Sb0QXYWY27yrrO8rrnjLruw-Z1QjkEjkArPhBanYdT_2w51Kuf3pyv1hHP3UKYCic0UtMN_X7gZgARm0QwzmYLk8fUAklRiAdSK2ybiFY8jToHGnmnR3jWBa0HQaOCN7nZaPgKAzJv9HcHGUDM6E-rh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=NMSJuFs_gXJXugzRibz8sUpFZ1R8PExZhwBEpWQLAb26L32ZHqvQLDIWKg57SpS9sKfDG0rqyslJ98thzQEtHeGAnIKYLwed1zOvixCiMzY1ElcnIKufk1olKSM6I3E3bdHNvxoVvhZfJKk5YsYYTFOvKEXfiR_WTPAai4_kRWxWVFHwT-ISP1fFJ1EN7Sb0QXYWY27yrrO8rrnjLruw-Z1QjkEjkArPhBanYdT_2w51Kuf3pyv1hHP3UKYCic0UtMN_X7gZgARm0QwzmYLk8fUAklRiAdSK2ybiFY8jToHGnmnR3jWBa0HQaOCN7nZaPgKAzJv9HcHGUDM6E-rh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از بیدگنه
سلام همین الان از بیدگنه موشک زدن
سلام از فردیس موشک فرستادن
سلام وحیدجان
ساعت ۲۳:۱۳ از سمت جنوب مهرشهر کرج صدای بلند شدن موشک میاد.
سلام الان از بیدگنه موشک زدن
از کرج موشک زدن چندتا
از بیدگنه ملارد بود احتمالا
درود همین الان صدای بلند شدن موشک از فردیس کرج اومد
همین الا از ملارد بیدگنه موشک شلیک شد
همین الان از بیدگنه چندتا موشک شلیک کرد
سلام از ملارد موشک زدن ساعت ۱۱:۱۲
+ ده‌ها پیام مشابه دیگر از این منطقه پرجمعیت که نمی‌رسم بخونم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78166" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان از کرمانشاه موشک زدن ۱۱و۰۷ دقیقه
داداش کرمانشاه پردیس دقیقا همین الان صدا اومد
همین الان از کرمانشاه موشک پرتاب کردن
صدا انفجار شدید کرمانشاه الان
وحید همین الان از کرمانشاه موشک فرستادن ۲۳:۰۸
کرمانشاه الان موشک زدن
کرمانشاه صدا جنگنده میاد وحشتناک [صدای پرتاب موشک با جنگنده زیاد اشتباه گرفته میشن.]
10:08 کرمانشاه موشک رفت
همین الان از کرمانشاه موشک فرستاد ...
سلام وقت بخیر الان هم از کرمانشاه صدای شبیه پرتاب موشک اومد ۲۳:۱۰
کرمانشاه دارن موشک میزنن، هنوز ادامه داره ۲۳:۱۱
موج دوم موشک از کرمانشاه ۲۳.۱۲
آپدیت:
پیام‌های کرمانشاه تا پنج تا موشک ادامه داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78165" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌های دریافتی:
الان موشک از،یزد زدن
از یزد موشک زدن الان
سلام وحید جان
همین الان از یزد موشک بلند شد
همین الان از یزد موشک زدن
وحید یزد همین الان موشک بلند شد ازش
الان از یزد موشک پرتاب شد
🔄
همین الان دوتا دیگه
دو تا دیگه از یزد زدن
۲۳:۰۸ دوباره از
#یزد
موشک زدن.
۳ تا موشک دوباره یزد بلند شد
سومین موشک هم شلیک شد
ساعت 11:08 دوتا موشک دیگه از یزد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78164" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qApxIxoS4uGUAism91iV-Co9OjHzOYrKQRtU3kUmAzzQo8MLzDagmBcPo_3MziGxc0JLEj3yW-Kq1slf7aIwfm8iRBK7qvAJHXq4FvX17ZWvvwskQjZox-L-9H4qsTxiCw2AhPHeckyfVxsUdAhKQXlb3SxGLHhZbpDDqk4eWlda6gRo_TH_j-YKaWl3smNUJNdGDrNZLFTU-eeCYza8mNFdRM67IGrB5aVZI9dCxEvQmXb7gIC07dCpFG5UX8AwMeTS1mUOjP2CP8Rf4X5QT37xJdNYc5rZ8SmTuMUa65Q459xiFBtScBrB-cJgeS5MBo8EteNbmbVRE3_o8pjC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kt8Xhikp0BIB--iWrjoXREmRLiSEUEKeUT_ldaKR-jSBGch3mUzvsGFKdN_eqZyysk4xwIPlZ50ujlLpxuZEzopQ8jQIPii-xb_jRsc8z_lX3_mrlLPiK911K7ySr6Uf_LsNvc4WQIxybTp10eXsFYjdvMWXZLlDaSx6HaR2EOf3jx4JkZyO67zMpSpkuX25VyTdgFaWcmgp0fXhVcuDPdUSvRDJgaVNGfpOeH0cQSV3HqJ5CihS9YwkRX_pA5dmyrlNI5b1RKN-Hqle7rxsxYP7P9y0cRt9lvDX0wHnEVa-oV-126Wx7AZmaaoI1Bdopz0glZgKzVJmT_JVi8WScw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=lehN2U4g7r4XjeERksUeYVW4dnRSJ2IvW8aZfgI0vaiWyq0KSwjv211HF7vm1ZVQufHSBxha9TEF5zVLkNWoOoNZYRj75in5zD_L_q2i2Onusvv_a91RMV8hfatEPSk_CUXYFluPgMemkLhME8qPBwn602hACm_6zkZoPOT3ps-rTfPt7q-Y3uZzsz5WZeG_kch977m42FBEKLTDZZzd4zc5mjvj8TkSwJgp8Yba66k2GwtdGAzNd3ry14OnUGBQS52MFz6xGO4P2NUb0wMuNBPZHW7gCxEMGc5VbBd4Rug87v2cLpsHn66jiaBKTBrB_XP2EhalVwANgtW8TVirhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=lehN2U4g7r4XjeERksUeYVW4dnRSJ2IvW8aZfgI0vaiWyq0KSwjv211HF7vm1ZVQufHSBxha9TEF5zVLkNWoOoNZYRj75in5zD_L_q2i2Onusvv_a91RMV8hfatEPSk_CUXYFluPgMemkLhME8qPBwn602hACm_6zkZoPOT3ps-rTfPt7q-Y3uZzsz5WZeG_kch977m42FBEKLTDZZzd4zc5mjvj8TkSwJgp8Yba66k2GwtdGAzNd3ry14OnUGBQS52MFz6xGO4P2NUb0wMuNBPZHW7gCxEMGc5VbBd4Rug87v2cLpsHn66jiaBKTBrB_XP2EhalVwANgtW8TVirhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی: سه موشک از
#خمین
پرتاب شد
تصویر دریافتی سوم از آسمان ازنا در لرستان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78160" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=vDpiDoXcfVlwyrqcN1scpycM6ytPXc7AeYI06nTLagJ-r1NmcGtQraHyCimT0Nfgy4g61WMdIbmzF3XOW_Oi_5J_uW_3uDJN-w1iakxU9VlmpEvXMQ_ZsRySx7rYvixcTBOP-v8UkO-ITTLqmST9lZFsGbnq4xetQ-hvXsFXx_cdKijr8WUqUgkSVNEABI0WJYKB9Ie43n-xMk1GvYlX7CJmwuHSWUX-u9Jhc0_qXZ7u3d7lUT-5p4whMOKjs2emzHkwIOEuhgKhKMKOgv46w3EcPovWbccb0aWY1uRSyRpuSG3cpKLp_QmnZl_14cpqwmkEmXyYCkXRTQjjB7dSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=vDpiDoXcfVlwyrqcN1scpycM6ytPXc7AeYI06nTLagJ-r1NmcGtQraHyCimT0Nfgy4g61WMdIbmzF3XOW_Oi_5J_uW_3uDJN-w1iakxU9VlmpEvXMQ_ZsRySx7rYvixcTBOP-v8UkO-ITTLqmST9lZFsGbnq4xetQ-hvXsFXx_cdKijr8WUqUgkSVNEABI0WJYKB9Ie43n-xMk1GvYlX7CJmwuHSWUX-u9Jhc0_qXZ7u3d7lUT-5p4whMOKjs2emzHkwIOEuhgKhKMKOgv46w3EcPovWbccb0aWY1uRSyRpuSG3cpKLp_QmnZl_14cpqwmkEmXyYCkXRTQjjB7dSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
خمین همین الان دوتا موشک زد
سومی رو هم زد
سه تا موشک از خمین زدن
سه صدای شلیک موشک از الیگودرز - احتمالا سمت خمین باشه
شلیک مجدد موشک از خمین، بیش از 3تا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78159" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌های دریافتی:
قشم دو انفجار شدید اطراف شهر
شد ۴بار پشت سر هم و شدید
ساعت ۲۲و ۲۸ دقیقه
۲۲.۲۹
دوتا انفجار بزرگ بندرعباس
سومین و چهارمین انفجار بندرعباس  ۲۲.۳۰
سلام قشم رو الان خیلی بد زدن
بندرعباس ۱۰:۲۹ سه تا صدا
چندتا صدای دیگه هم داره میاد
بندرعباس دو صدای انفجار
بندر دوباره دوتا انفجار
وحید شد ۴ تا
وحید جان بندرعباس مجدد 22:28 صدای سه تا انفجار از سمت ساحل اومد
ما خونمون بغل فرودگاس
شهرک صنعتی طولا قشم یا ناحیه سپاه چهارتا انفجار، صدای سوت موشک قبل از انفجار هم اومد
۲۲:۲۸
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78158" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gaYTL4DoDDvZr-yOL8SxNE-JC2jpsfjVNyXUuIkaLlvD8TRpIpY3vt2r0oyv4A7HOC6WbAy6EXg4_tnC2gdYufOb5WIhgTRHnDv7Itsao8JBfXGeR65Wz_DzIRsfgW0LeeTQgvPUJG4O5puY9O3-ndiqfFpF3H7CJW8C66TzaxXJZs36VHFh30A8ZOEU59ggoKxPJ9zNOC5aI1eI6aMVyerlpxM9bKPwvV245QLI6736EgcxH9L58wJsBvMAcza-yrcO_gpsKNhTRy9a5NDUQ0_VqhFn14hQO07qTQ4-gk8aawDFQ2k6Zb4so23_2tX5E_6nuLmAR0ecdpbbqxiMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، روز سه‌شنبه ۱۰ شهریور در گفت‌وگو با شبکه فاکس نیوز بازگشت به «تفاهم‌نامه اسلام‌آباد» را رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد».
ترامپ درباره پاسخ جمهوری اسلامی به حملات آمریکا گفت: «اگر آنها پاسخ بدهند، با شدت بسیار بیشتری هدف قرار خواهند گرفت.»
او حملات انجام‌شده را «بسیار بزرگ» توصیف کرد و افزود اگر درگیری برای سومین بار تشدید شود، ایران «به‌عنوان یک کشور به‌طور کامل از بین خواهد رفت».
رییس‌جمهور آمریکا گفت حملات اخیر، سامانه‌های راداری در جنوب‌غرب ایران و نزدیکی تنگه هرمز را هدف قرار داده‌اند؛ سامانه‌هایی که به گفته او ایران در حال بازسازی آنها بوده است.
ترامپ گفت نیروهای آمریکایی بخش قابل‌توجهی از شبکه راداری ایران را منهدم کرده‌اند و افزود: «آنها تلاش کردند رادارهایشان را دوباره بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریبا آماده شود و بعد آن را هدف قرار دادیم.»
او همچنین گفت ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» به‌طور کامل برای ادامه عملیات در صورت نیاز آماده است.
ترامپ بازگشت به «تفاهم‌نامه اسلام‌آباد» را نیز رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد». او افزود آمریکا فرصت‌های زیادی برای دستیابی به توافق در اختیار جمهوری اسلامی قرار داده است.
رییس‌جمهور آمریکا همچنین گفت متحدان واشنگتن در منطقه خلیج فارس پیش از حملات اخیر در جریان این عملیات قرار گرفته بودند و رهبران ایران درباره عزم او دچار «اشتباه خطرناکی» شده‌اند.
ترامپ در پایان سخنان خود درباره مقام‌های جمهوری اسلامی گفت: «آنها دست‌بردار نیستند؛ آنها دیوانه و احمق‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78157" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=qHfOGdgBt3jlJHCQtWCZJzgf4fTE6FMyYA_1yDPseY40pLKLeuv5hrNkq45HQ61WXYH8ZL2q64vhOf4aiBtJZNGbKHE2HHLgn2Jfkv352IwR3ykCgRlUlDu2RqJm2l3dKHI0R4E2-FzcFkYiS5OeYSJQpBrqJFSREQjDZMcshY-Jr-AFQG4LR5sR1vjb_vi39hfHHHRiMJ1wts6SdGM5aSDi16P1lnA0UohgSgNRKCI56xTDfEl4NbwBNrNkCZneemnHQFmEJ19LnZ-vzMUgw6yqucE6DSdmbHXZ6yaBtF_9xS5WbpSZ545PQ1i1oz10TlaOtIr8tWm8DNyx3U2HWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=qHfOGdgBt3jlJHCQtWCZJzgf4fTE6FMyYA_1yDPseY40pLKLeuv5hrNkq45HQ61WXYH8ZL2q64vhOf4aiBtJZNGbKHE2HHLgn2Jfkv352IwR3ykCgRlUlDu2RqJm2l3dKHI0R4E2-FzcFkYiS5OeYSJQpBrqJFSREQjDZMcshY-Jr-AFQG4LR5sR1vjb_vi39hfHHHRiMJ1wts6SdGM5aSDi16P1lnA0UohgSgNRKCI56xTDfEl4NbwBNrNkCZneemnHQFmEJ19LnZ-vzMUgw6yqucE6DSdmbHXZ6yaBtF_9xS5WbpSZ545PQ1i1oz10TlaOtIr8tWm8DNyx3U2HWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
پرزیدنت ترامپ به فاکس نیوز گفت که امشب شمار زیادی از رادارهای ایران هدف قرار گرفته‌اند.
پرزیدنت ترامپ گفت: «آن‌ها تلاش کردند رادارهایشان را بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و بعد آن را هدف قرار دادیم.»
رئیس‌جمهور گفت اگر ایران پاسخ دهد، «ضربات بسیار سخت‌تری خواهند خورد... اگر کار به بار سوم برسد، آن‌ها به‌عنوان یک کشور کاملاً نابود خواهند شد.»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78156" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه‌های وابسته به سپاه از آغاز حملات موشکی و پهپادی ایران به مواضع آمریکا خبر دادند
خبرگزاری فارس، وابسته به سپاه پاسداران، شامگاه سه‌شنبه ۱۰ شهریور به نقل از مشاهدات میدانی خبرنگاران خود از شلیک موشک‌ها و پهپادهای جمهوری اسلامی به سوی مواضع آمریکا خبر داد.
همزمان، خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت «عملیات قاطع نیروهای مسلح ایران» در پاسخ به حملات آمریکا آغاز شده و «پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشک‌ها و پهپادهای ایران قرار می‌گیرند».
تاکنون مقام‌های آمریکایی درباره این حملات جمهوری اسلامی اظهار نظر نکرده‌اند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78155" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-wfLPbPvS8yf_GVRWXIE9thRulhaS88T0z9Rb8LgoOyEVHfQ80B5hDxMzAknmIMXh1YkCaQ6IPGVH4jLdQ1MMD2J9rwMVPnziwgqznZP3tr2O6zwC9Ruze3aBIx5iJLAhMKMqZY2vWUgzgj5W2eGkXnEgDcg1HdpisDs6sXFzOL200YuxbnfY-2FI5UpdbKpfWW2iR2WJygRXMpzx35jRCt-MzhlD6sAjAr0TU8SymXlzGhrJZBKGj5NJ7ALFSRmHXCTpwcpepTlLBY_OC4BEV8gVAgPXCb-gUJUA5Tzu9kqbBZLM-KihB_K4AitgpxXHRgdBgY8flexxMbDFteug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با تری ینگست، خبرنگار فاکس‌نیوز و در پی آخرین حملات آمریکا به مواضع جمهوری اسلامی، هشداری صریح خطاب به تهران صادر کرد.
ترامپ با اشاره به پاسخ احتمالی ایران گفت: «اگر دست به تلافی بزنند، بسیار سخت‌تر هدف قرار خواهند گرفت؛ و اگر دوباره چنین کاری کنند، دیگر وجود خارجی نخواهند داشت.» او با انتقاد شدید از اقدامات تهران افزود: «آن‌ها دست برنمی‌دارند؛ رفتاری دیوانه‌وار و احمقانه دارند.»
رئیس‌جمهوری آمریکا در ادامه به جزئیات حملات اخیر اشاره کرد و گفت: «آن‌ها سعی داشتند رادارهای خود را بازسازی کنند چون هیچ دیدی نداشتند؛ ما صبر کردیم تا ساخت آن تقریبا تمام شود و سپس آن را زدیم.»
ترامپ همچنین با ابراز بی‌اعتمادی کامل به مسیر دیپلماسی با حکومت ایران تاکید کرد: «معتقدم توافق با آن‌ها حتی به اندازه کاغذی که روی آن نوشته می‌شود هم ارزش ندارد. ما شانس‌های زیادی به آن‌ها دادیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78154" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صداوسیما: فرودگاه جیرفت هدف حمله آمریکا قرار گرفت
خبرگزاری صداوسیمای جمهوری اسلامی شامگاه سه‌شنبه ۱۰ شهریور گزارش داد دقایقی پیش فرودگاه غیرنظامی جیرفت هدف حمله آمریکا قرار گرفته است.
این رسانه افزود اطلاعات تکمیلی درباره این حمله منتشر خواهد شد.
@
VahidOnLive
اسکندر پاسالار، فرماندار عسلویه، به خبرگزاری فارس، وابسته به سپاه پاسداران، گفت: «حوالی ساعت ۲۰:۱۰ شامگاه سه‌شنبه، صدای یک انفجار در شهرستان عسلویه گزارش شده است.»
فرماندار عسلویه گفت که از خسارات جانی و مالی این انفجار جزئیاتی مخابره نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78153" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78152" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=L9fn07yP6jJXZJHqj8o8I7KuSFlzMArVDwHys5aVvBy8qsqZrlDiSP5BaeEhPVTt67-SQbSaq4uQYwSa6dR3k26lEHwXYk5cs7JsDqAtw5QVxmqe9Mw4ps2h4aulzgJPd8nKGaeXHnOy_085sXZD4AfxobXi1LMOC2bHp176PI2UUSvhRKSRYCgZdOnHQAKzEYR8IfoEo4t6NN9sBoMVV1uGn6BQ5gNn11p9NvGn9g_zhoGahalu8U5dDXAkN5FuEj-9WAgYqaG2v9SeOw8xJqFuBPx1ZZ0xjW_Ui1j0G8O5N0p-sy3Em5WjtVSo4x3VkRRLdBOjujVB8eEttfxMkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=L9fn07yP6jJXZJHqj8o8I7KuSFlzMArVDwHys5aVvBy8qsqZrlDiSP5BaeEhPVTt67-SQbSaq4uQYwSa6dR3k26lEHwXYk5cs7JsDqAtw5QVxmqe9Mw4ps2h4aulzgJPd8nKGaeXHnOy_085sXZD4AfxobXi1LMOC2bHp176PI2UUSvhRKSRYCgZdOnHQAKzEYR8IfoEo4t6NN9sBoMVV1uGn6BQ5gNn11p9NvGn9g_zhoGahalu8U5dDXAkN5FuEj-9WAgYqaG2v9SeOw8xJqFuBPx1ZZ0xjW_Ui1j0G8O5N0p-sy3Em5WjtVSo4x3VkRRLdBOjujVB8eEttfxMkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های زیادی دریافت کردم که نوشتند حدود ساعت ۲۱:۲۵ از
#خمین
موشک شلیک شده ولی پرتاب موفق نبوده و برگشته.
ویدیوهای دریافتی: سه‌شنبه ۱۰ شهریور
Vahid
آپدیت:
منابع جمهوری اسلامی بعدا این ویدیوهای دریافتی رو با شرح هدف قرار گرفتن پهپاد آمریکایی منتشر کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78150" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌های دریافتی:
صدا ۹:۰۵ بندرعباس
وحید بندرو دوباره زدن همین الان
صدای انفجار بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78149" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TJ1bFo27wY5igpGETY-V1VRllLYgYNS31mVjRMVuWTrsN72r4-AKgWfo2ZrLRoulW9eKSopQDS6dgTcWjIVg3h3rC6MSTCNHBWFdiEvcIZqQYDFyvMlm2Yo5aQAgZr4y1Ifr8oGxHenXwiq51hCsw_rzeNXzGaZ-aP7OuUkFl1cJwctw04C4_yXZ4-LjJIAOUaRRsBVekNODJr3R2MtEDJJhJeSR7pRQEU1MkpUfTLJ1frP5TKjuNdHVIIBrIUH-DSB1BfhLkwkLVaHCSpGe1PehtGGyDQLe5XqnXUnQ6UlxQP-9QGEfSdRRmC4TgrbjxN9YfzfcLhFRw-kCVs0dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر ایران پاسخ دهد، حملات آمریکا شدیدتر و گسترده‌تر خواهد شد
ترجمه ماشین:
ایالات متحده همین حالا، در حالی که صحبت می‌کنیم، در حال حمله به اهدافی ایرانی در نزدیکی تنگه هرمز است.
این حملات گسترده و قدرتمند هستند و در تلافی تلاش نافرجام ایرانی‌ها برای افزودن مین‌های دریایی به تنگه انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (همه آن‌ها به‌طور کامل جمع‌آوری یا منفجر شده‌اند!)، و همچنین در تلافی شلیک هشت موشک از سوی ایرانی‌ها به پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به تلافی بزند، بار دیگر و در سطحی بسیار شدیدتر و بالاتر مورد حمله قرار خواهد گرفت؛ اما آن هم بزرگ‌ترین حمله از همه نخواهد بود. آن حمله هنوز در انتظار است و وقتی به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78148" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی:
سلام صدای چند انفجار اومد بندرعباس ۸٫۵۰
۸:۵۲ قشم یه انفجار حس شد
بندرعباس صدای 2 انفجار دیگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78147" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN26i5qIGM8LONQcS9WB07htlZFJsRZyvSFgn4q2mBOdAk20qx1uFoUlf1SdPDUH0NM74RuCC_3ddS1QxmFZK8nXeECanrqOkMMKplgeAPTrPgtz9lwU4KkhEqdrXHX1Ev39aj-ATJKtvPKSFbZqBNaF0VuZu4F2sVis38mcusu6kP_5bZ_xdZenhcUpPccGgZw7PEMsgm8410BLE_-ahK4yvR36o6TynClax09z8pyjwb4erapuM5GdrXj35dRT-dlysYzAu02GNAlC6ofEJvlm2KwCUmZeTFVD-VHhZMXd2-PIgEdjmwT66mS8q1jKMFwonhLHZGw-jb0EGFhSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۱۰ شهریور، در پی شروع دور جدید حملات ارتش آمریکا به مواضع نظامی در ایران، خبرگزاری آکسیوس این اقدام را صحه‌ای بر گزارش خود مبنی بر طرح آمریکا برای حملات مداوم و دوره‌ای به مواضعی در شهرهای حاشیه تنگه هرمز دانست.
پایگاه خبری آکسیوس به نقل از مقامات آمریکایی گزارش داد که دونالد ترامپ و مقامات ارشد دولت او در حال بررسی طرح‌هایی برای انجام حملات محدود در تنگه هرمز و مناطق اطراف آن هستند. هدف اصلی این حملات، جلوگیری از بازسازی سامانه‌های راداری، پدافند هوایی و توانمندی‌های موشکی ایران اعلام شده است.
به گفته آکسیوس این طرح که توسط فرماندهی مرکزی آمریکا (سنتکام) تدوین شده و مورد حمایت پیت هگست، وزیر جنگ قرار گرفته، به دنبال مهار تلاش‌های تازه ایران برای تهدید شناورها و نفت‌کش‌هاست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78146" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cxP_Znio92ASTchnjqEOvurJIoJbsv1G5eAqanq1NagXvlZ8gai4lUcsyk6PryzLE6HsD_NBwymZtP8kgBbIrmM0diC1i6EAc-EulZ8PoJEWNyfZ0tR7Tx1JVhcWGZ68CV2POfioQsFsfO-1GLbpl53F89N2x1hTF0fxO97lA0rxrDZCKHEwR4657XhqEKCkNqT8PFayjsKA4gh4yY5pHwBKorQk6jDs46KSh1FJNVS4VHUKG0ii3EO2BkUSZ6fxsGv9rHHgUO6QBPL6z92EkZnCm1kBatZFJXx2ymiq9LgOxNsVno34we9rbVrfLAQIrDNrD83Doip3xgop5oXkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سنتکام در این لحظه منتشر شد. چیزی که پیش‌تر در منابع دیگر پخش شد درست نیست:
امروز ساعت ۱۲ ظهر به وقت شرق آمریکا [ساعت ۱۹:۳۰ به وقت تهران]، نیروهای ایالات متحده حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران را آغاز کردند.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و نیروهای نظامی آمریکایی مستقر در منطقه انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78145" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ebTuGEgxVFTMyWt1tlXpqIU5dQSOTtZSAkoSfyOER_nPVMe8jSSQAqq-hnFwtVLLcKTrkOXrP-MfcBoI-h8VcCxc7GbxkZJ6YOSqJWpfIWJW1fqnFxipRSMOyKPiAKeFYHjRK4nGRS1MIy46GEtDQV38Prw1xAhaqK_ygRVtwtQnZ-3nA5y9r2rx57zeMRBvEQCbEkLeqE9DfmpZvdaL6WkFgyWFIqmPLkmHfVBYnrYxVeHQ11W1YLidDzCaFSAQlRUrDGNtlBlUane5h4g-37fjCVo37TZlav1SdkhHt_SnTDjIDXDUuEMZs8XKTz21V3V6CISyd_Tau7-7DfID3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی از شنیده شدن صدای چند انفجار در قشم در شامگاه سه‌شنبه خبر داد و نوشت: «دقایقی قبل صدای بیش از ۵ انفجار اطراف روستای مسن قشم شنیده شد.»
این خبرگزاری نوشت: «دقایقی پیش، صدای ۴ انفجار هم از سمت تنگه هرمز در قشم شنیده شد.»
رسانه‌های ایران از شنیده شدن صدای انفجار در بندرعباس، سیریک و چابهار نیز خبر داده‌اند.
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، می‌گوید تاکنون هیچ‌گونه اصابت یا حادثه‌ای در هرمزگان گزارش نشده است.
@
VahidOOnLine
علی خلیل‌آبادی، معاون امنیتی و انتظامی استاندار سیستان و بلوچستان، در گفت‌وگو با خبرگزاری دولتی ایرنا از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78144" target="_blank">📅 20:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیام‌های دریافتی:
۱۹:۵۸  چهار انفجار پشت سر هم
بندرعباس ۷ انفجار شدید ۱۹:۵۷
دوباره زدن بندرعباس
صداهای پشت سر هم ولی این بار خیلی دور
7 صدای انفجار بندرعباس سمت شرق پشت سر هم ساعت نزدیک 8
سلام بندرعباس حدود 10 انفجار
7:57
صدای ۵ انفجار  (۳ انفجار پشت سر هم و ۲ انفجار جدا ) از فاصله دور جزیره قشم شنیده شد
ساعت ١٩:٥٧ دقیقه چندتا انفجار پشت سر هم شنیدم یندرعباس
شیش انفجار مجدد بندرعباس ساعت هفت پنجاه هفت دقیقه خیلیم شدید
7:57 بندرعباس 10 شهریور بالای 10 تا انفجار
بندرعباس ۱۹:۵۷
چهار پنج تا پشت سر هم زدن
دوباره زدن ، شاید هم صدای موشک از اینطرفه، صدا اینبار کمتر بود ولی تعدادش بیشتر بود
بندرعباس انفجار های پشت هم صداش قطع نمیشه
چقد زیاد ۷ تا انفجار توی ۱۰ ثانیه ساعت ۱۹.۵۸
دور از قشم
۱۹:۵۸  ۴ انفجار پشت سر هم
احتمالا بندرعباس
ولی از قشم به خوبی احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78143" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌های دریافتی:
دوباره زدن بندرعباس
الان یه انفجتر دیگه بندر عباس از بقه بلند تر بود ساعت ۱۹:۴۵
یک انفجار شدید الان در بندرعباس
۱۹:۴۶ دوباره بندرعباس صدای ۲ انفجار متوالی
ما شرق بندرعباسیم، صدا ضعیف بود.
سلام دوباره همین الان قشم رو زدن دو مرتبه19:47
وحید جان صدای شدیدتر همین الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78142" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های کمی از سیستان و بلوچستان:
19:34 کنارک انفجار اول
19:36 کنارک انفجار دوم
سلام وحید جان صدای انفجار چابهار همین الان
چابهار داره میزنه19:33
شیش هفت تا انفجار پشت سر هم
چابهار صدای پنج انفجار پنج دقیقه پیش
سلام وحید تو خونه ۶ تا شنیدیم شاید بیشتر بود
کنارک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78141" target="_blank">📅 19:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔽
#بندرعباس
پیام‌های دریافتی:
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندرعباس صدای ۳ انفجار ۱۹:۲۸
بندرعباس دو صدای انفجار
بندرعباس 3 انفجار همین الان
درود چهار صدای انفجار با موج انفجار بندرعباس ساعت ۱۹:۲۸
وحید بندر سه تا صدای انفجار اومد ۱۹:۲۹
بندر عباس 19:29
صدای ۴ انفجار سنگین
سلام، هم اکنون صدای دو انفجار در بندرعباس
درود وحید جان بخدا دیگه دارن میزنن بندرعباس الان دو تا انفجار محدوده فرودگاه ساعت ۱۹:۲۹ حالا یا زدن یا خوردن
سلام
۳تا صدای انفجار مانند الان بندر عباس اومد تو خونه حس کردیم نمی‌دونم چی بود دقیق
سلام بندرعباس الان با فاصله های چند ثانیه ای صدای ۴ تا انفجار اومد
صدای دوانفجار بزرگ بندرعباس ساعت هفت وبیست وپنج دقیقه شب
۱۹/۲۹ چند انفجار پشت هم قشم حس شد
احتمالا لارک، هرمز یا بندرعباسه
احتمال بیشتر لارک صدا از سمت جنوب بود
بندرعباس الان دوتا انفجار شدید
۱۹:۲۹ زدن
منطقه بهشت بندر صدا واضح بود
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندر رو زدن
وحید جان صدای دو انفجار سمت اسکله رجایی العان
دوبار ۲ تا دیگه
سمت قشم درگهان بود موج
درود وحید خان صدای 4 تا انفجار پشت سر هم بندرعباس از سمت بلوار شهید رجایی
خیلی شدید
درود وقت شما بخیر
ساعت هفت و بیست هفت بندر عباس صدای انفجار
قشم خیلی صدای انفجار میاد همین الان
شروع شد ۱۹.۲۹.  صدای ۴ تا انفجار دور از قشم
یکی دیگه دقیقه ۳۱ دور بود
سلام وحید جان قشم صدا و موج انفجار میشنویم
خیلی دوره ولی بزرگ احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78140" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db6862775f.mp4?token=fLkf3Nq-Xp0QaefhkWx74SsxvGeMPmg5KZia-O5pTBKlyWfiXIZ6J3Ef34Hpz1pe11cLuP4HcF94YmluFIsN6Fzm3wd15pibz1cBETt8TK30GpZ-nVe5jkNYTrckc6WfLSa7TfMWOXTYaWDJ972daIRt8kDh-Y0XFWpeybcnQn5yVVuXbJ5XNEz8QjUJZDJTiW858krJFK2LsWDDYZoxRgGy6SyXVXdlDCNFkgONPVERaXrIw9Vhe94TGxydcmxyf8NzU7OdXpp6tO2WWTY_UMeV_P0SGLHIAVI0HUrPhU4ShLSwfjxB2H1e6DOkHPHPpF3BO9xu8ulzmCpYc4VbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db6862775f.mp4?token=fLkf3Nq-Xp0QaefhkWx74SsxvGeMPmg5KZia-O5pTBKlyWfiXIZ6J3Ef34Hpz1pe11cLuP4HcF94YmluFIsN6Fzm3wd15pibz1cBETt8TK30GpZ-nVe5jkNYTrckc6WfLSa7TfMWOXTYaWDJ972daIRt8kDh-Y0XFWpeybcnQn5yVVuXbJ5XNEz8QjUJZDJTiW858krJFK2LsWDDYZoxRgGy6SyXVXdlDCNFkgONPVERaXrIw9Vhe94TGxydcmxyf8NzU7OdXpp6tO2WWTY_UMeV_P0SGLHIAVI0HUrPhU4ShLSwfjxB2H1e6DOkHPHPpF3BO9xu8ulzmCpYc4VbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.  درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید…</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78139" target="_blank">📅 18:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_DeSmiNlTs-qFcnISaFZ1tQYqQkrb0sVHTV6F9uB8jav1IdUHwo3NI_OLVwyZFdazyA4jIClUxYrKtULvP28BQbJvakXdqNJy1dF-3Z4wsnOO_-n9pHnh00jVmu2kBRAI0Rb70mUMCuyBB5EjR9MpkCelEQRWIU4Ejd4yfBOirkAPj8bcYY6EEg2-lMTHAFOakkUVZLV3Bk5r7vbFNis1P72DSPmCAVuyOSVaH6gp0WMoitIceqS0c_VtzD7lo0Sv6-yeEmPHgr67lUhxoiEdPWITOfNxegBVVm3Q0blsS_ntz7jcOGgYb-rs6zZQpH_meUjSMXtoE1gm5CyeWG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=QP1gh03Qj18WVsMZmOTOQh-2K-O4tOGYqWoovtkhfqrfyTF0W6sLWxNTxUDoEXn6fgwI5NEnieeXP_uMwqudosWRDxIG6L1k4WEzwnTH6_4INpMUFossnjxKOJ7zYPTV7LpKERlRpdJmCWmABBo5cx6ypx7DCLMauDR2QsndmFIc665BnpBfBqeZfA6AsuuMVRuoFlK313uH5KRgYtA8gmL-9-0wt0yGVu5JOtYXvds_-xYdhIEzAoRhFWM38KY7cwE9tRX82BHsTZ3kI3BOCYIZTSIX5Mq_LcwYc8HDzyGlZK8_XXHjF_KlWHQvJ5yqzz88Z0_erLFFxdse12Ub0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=QP1gh03Qj18WVsMZmOTOQh-2K-O4tOGYqWoovtkhfqrfyTF0W6sLWxNTxUDoEXn6fgwI5NEnieeXP_uMwqudosWRDxIG6L1k4WEzwnTH6_4INpMUFossnjxKOJ7zYPTV7LpKERlRpdJmCWmABBo5cx6ypx7DCLMauDR2QsndmFIc665BnpBfBqeZfA6AsuuMVRuoFlK313uH5KRgYtA8gmL-9-0wt0yGVu5JOtYXvds_-xYdhIEzAoRhFWM38KY7cwE9tRX82BHsTZ3kI3BOCYIZTSIX5Mq_LcwYc8HDzyGlZK8_XXHjF_KlWHQvJ5yqzz88Z0_erLFFxdse12Ub0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا گفت: «جهان از رژیم مطرود و یاغی ایران خسته شده است و ترامپ به‌جای مماشات با آن‌ها می‌خواهد یک‌بار برای همیشه به آن‌ها خاتمه دهد. مردم ایران این فرصت را دارند که به نظام جهانی برگردند، به‌جای اینکه سرکوب شوند.»
IranIntl
بسنت گفت: «ما سر مار ایرانی را زیر خاک کرده‌ایم. مار هنوز نمی‌داند که مرده است و بدنش کمی حرکت می‌کند، اما با غروب آفتاب از حرکت باز خواهد ایستاد. رژیم ایران نابود شده است و به‌زودی خودش هم این را متوجه خواهد شد.» او تاکید کرد دونالد ترامپ قصد دارد این پرونده را برای همیشه ببندد.
@
VahidOOnLine
اسکات بسنت گفت: «ایرانی‌ها تلاش می‌کنند از تنگه هرمز به عنوان یک گلوگاه استفاده کنند. این تنگه برای آمریکا گلوگاه نیست، اما برای بسیاری از کشورهای دیگر هست. این وضعیت تا دو سال دیگر دور زده خواهد شد. تا دو سال دیگر، تنگه هرمز به پهنه‌ای بی‌ارزش از آب تبدیل خواهد شد.»
بسنت گفت: «نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.»
@
VahidOnLive
وزیر خزانه‌داری آمریکا: در حال شناسایی و ردیابی دارایی‌های سپاه هستیم
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز سه‌شنبه ۱۰ شهریور در حاشیه نشست وزیران و مقام‌های ارشد مالی گروه ۲۰، از تشدید فشار اقتصادی واشنگتن بر ایران خبر داد و گفت آمریکا احتمالا این هفته یک بانک و هفته آینده یک بانک دیگر را تحریم خواهد کرد.
بسنت گفت: «احتمالا این هفته تحریم یک بانک را اعلام خواهیم کرد و هفته بعد نیز یکی دیگر را اعلام می‌کنیم.»
او افزود آمریکا در این زمینه با متحدان خود در حال گفت‌وگو است و از حمایت آنها برخوردار است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال بررسی تحریم شرکت‌های لیزینگ هواپیما و دیگر نهادهایی است که با سپاه پاسداران تجارت می‌کنند.
او گفت: «ممکن است این‌ها نهادهای مختلفی باشند. ممکن است شرکت‌های لیزینگ هواپیما باشند که آنها را بررسی خواهیم کرد. ممکن است هر کسی باشد که با سپاه پاسداران تجارت می‌کند. ما در حال شناسایی و ردیابی دارایی‌های سپاه هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78137" target="_blank">📅 18:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78136">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=v7HxrVdUC0fr-Qo6Aa9wTcWvxrd0n8iHdDqJvWbu7kNveqE2UiBbEIp7S0rPoQNm90WLBL3efBQa1ZKArIO3qrqBBhHMx9rFcDWFf0vsOIVUrA5JbDZNOjUsGPHCjVGR1XgvItgqnzk9rJpX-Lf84IAQl0ukLZkj4O5MeXONEh3Rsuyw5iQlvydTySLhyysvNewhP36DULbcq0aXQcTt6IUrxehkj7N0-gdtYJNWCTn79ypTyONloDs3Md13m9PqgsDh1MZWsO5R4n3tq9AjL1YdfC2FvvekEfUjJf-XZNyB6Qeq-ZC2kRbVm3vMVLeAKK22luAacqtFYTNObXwY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=v7HxrVdUC0fr-Qo6Aa9wTcWvxrd0n8iHdDqJvWbu7kNveqE2UiBbEIp7S0rPoQNm90WLBL3efBQa1ZKArIO3qrqBBhHMx9rFcDWFf0vsOIVUrA5JbDZNOjUsGPHCjVGR1XgvItgqnzk9rJpX-Lf84IAQl0ukLZkj4O5MeXONEh3Rsuyw5iQlvydTySLhyysvNewhP36DULbcq0aXQcTt6IUrxehkj7N0-gdtYJNWCTn79ypTyONloDs3Md13m9PqgsDh1MZWsO5R4n3tq9AjL1YdfC2FvvekEfUjJf-XZNyB6Qeq-ZC2kRbVm3vMVLeAKK22luAacqtFYTNObXwY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس شورای اسلامی، سه‌شنبه در پیامی ویدیویی با تاکید بر اینکه محاصره دریایی در قوانین بین‌المللی، یک اقدام نظامی محسوب می‌شود، گفت که اگر محاصره را تشدید کنند، حتما پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد.
قالیباف گفت: «اگر دشمن اراده‌اش بر این باشد که ما از خلیج فارس نفت صادر نکنیم، هیچ‌کس نخواهد توانست نفت صادر کند.»
او گفت: «آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد.»
رییس مجلس افزود: «دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است.»
قالیباف گفت که دشمن پس از «شکست در عرصه نظامی و دیپلماسی» سراغ جنگ اقتصادی و شناختی رفت و آن را به جنگ نظامی خود اضافه کرد.
قالیباف افزود: «هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78136" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_vwW3z4fCJf9i_BMOpdU5rPvEclvOUgdAXBV3NL031nVKgBQO7nT0V08fm9XONyKAWAIquzeTgOSXda-rFkE8jaFlkIsCioOuXMt0vDP67LJq48IdOyj57aC2P-r3cKweNG51TcwwAW_2dq1n5T-8NmPuptRWQAv8KK9NyWX8jw38IWZrKGESPAfzb8_oXodmfRHM5d_IOTZcnSzxAwr13tmTTaxOeRgkE0LxB6LCY8kVsMugWtggyD5HZD95gi2VwuqlAEUxSq0U40gunnLbqI4K6qaKS5ULuKBNZ7Ji2bIY5Pu9B4YzkV4ZMSa8TQT1RWV0yQszSeapcwzcgUxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با انتشار اخباری از حضور «حجاب‌بان‌ها» در بازار تهران و سخنان برخی از مقام‌های جمهوری اسلامی در رابطه با لزوم «اجبار حجاب»، تصاویری از نصب بنرهایی در شهرهای مختلف ایران منتشر شده که در آن‌ها زنان به مجازات قضایی در صورت رعایت نکردن حجاب مورد نظر حکومت تهدید شده‌اند.
در این بنرها، به تبصره ماده ۶۳۸ قانون مجازات اسلامی استناد شده و آمده است: «حضور بانوان بدون حجاب شرعی در معابر و انظار عمومی جرم و دارای مجازات حبس است.»
در بنر نصب‌شده همچنین به مواد ۷ و ۹ قانون موسوم به «حمایت از آمران به معروف و ناهیان از منکر» اشاره شده است. در توضیح ماده ۷ نوشته شده افرادی که در برابر «امر به معروف و نهی از منکر» مانع ایجاد کنند، مشمول تخفیف یا تعلیق مجازات نمی‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78135" target="_blank">📅 18:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uWVU9un2K1Ny2qwkAU3xaOdNV8BB5syWAy5m4decmdJIWvrEIQ4Gd_N7JzOagWBJH8HgWC3Sk4d1ly7op6-4B6b7nOMhfBvpd4647FSjbCyX-FGaSPxLRT2g8SubKwLrLvd1wsx84g3aqQURPnIpAAAMNVpEzEv1X5aiTYJc5OQpQox8-okjeCdTVSsMA8JowKSkuWpzciKw9MChw-16oc_gNFFv9E23zWk9sWCo_1Pd9Hrp18o5Lle13CXpBGoIKnDTJYGUZqzd_kClZMEhcAx9UJbtlR12Q1pw8Uw9OYGp804TBdhZwd-oAV_qaV79Mm3HvGuEDiRAj8SeQ3acvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران به ۲۱۳ هزار و ۷۰۰ تومان و حواله دلار به ۲۱۸ هزار تومان رسید. هر پوند بریتانیا نیز با ۲۸۹ هزار تومان معامله شد.
رقم امروز چهارمین رکورد پیاپی در چهار روز کاری است. دلار روز شنبه با ۲۰۶ هزار و ۴۰۰ تومان بسته شد، یکشنبه به ۲۰۸ هزار و دوشنبه به ۲۱۰ هزار تومان رسید.
همزمان با ثبت رکوردهای جدید در بازار ارز، رئیس کل بانک مرکزی در سی‌وششمین همایش بانکداری اسلامی گفت ایران کمبود ارز ندارد و ادعای فروپاشی اقتصادی کذب است.
همتی در پاسخ به اظهارات مقام‌های آمریکایی درباره نبود دسترسی ایران به منابع مالی گفت: «این ادعاها به‌طور کامل بی‌اساس است. ذخایر مسدودنشده، منابع پایدار و درآمدهای نفتی و غیرنفتی متعددی در دسترس بانک مرکزی قرار دارد.»
او افزود بانک مرکزی هفته گذشته ۵۰۰ میلیون دلار به بازار تخصیص داد و اکنون آمادگی دارد در صورت نیاز تا سقف دو میلیارد دلار ارز تزریق کند.
اظهارات امروز همتی با موضع پیشین او فاصله دارد. او هفته گذشته در گفت‌وگوی تلویزیونی گفته بود: «درآمد ما از فروش نفت صفر شده؛ یک واقعیتی است که نفت صادر نمی‌کنیم.»
چرخش لحن پس از پیام مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به مناسبت هفته دولت رخ داد. او در آن پیام گفت گاهی بیان صادقانه ضعف‌ها کمک به دشمن است و بر ضرورت «تبیین و روایت قدرت و قوت ایران» تأکید کرد.
رهبر جمهوری اسلامی در همان پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/78134" target="_blank">📅 18:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i78_k8_UlLl1migJDw6Ml4-lIliVoigyjANAzzJqSZR-3vp-o3Q12ja37n_j35MZceca-IPODVmfESR2b6BYVF31t1REHYQJAZOR0sGZwNZ-PRtYF8EG7HPmExL21K487DndKo7pcW-E5_fV7ZAskrYiM3xRlDUTLODYf_BimpI36YlwBeLzS9O3dv_62xPea_Xs_yWD8n5CubQGGj30Qu7s2fXtKrHFDKcfHL8BoF_eeK09BzrGyPnsQtHQHlAmmiJHipiPHvOmqLDkG31HWST-1tt_BqfPlv3w16XiC8n2alKx_htpMchPj2gopYLbFmZBl3JqKtPJQ57ydvhe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت‌های‌ ناظر بر کشتیرانی جهانی می‌گویند دو ابرنفتکش حامل نفت عربستان سعودی اواخر روز دوشنبه نهم شهریور هنگام عبور از تنگه هرمز به فاصله چند دقیقه از یکدیگر هدف اصابت پرتابه‌های ناشناس قرار گرفتند.
به گزارش خبرگزاری رویترز، شرکت یونانی امنیت دریایی «ماریسکس» روز سه‌شنبه دهم شهریور اعلام کرد که ابرنفتکش «سیدر» حامل نفت خام عربستان سعودی با پرچم همین کشور حدود ۱۶ مایل دریایی در شمال شرقی خصب، عمان، ساعت ۱۹:۵۲ دوشنبه به وقت گرینویچ مورد اصابت پرتابه‌های ناشناس قرار گرفت.
شرکت امنیت دریایی وانگارد تک هم گفته است نفتکش «سنگال پراسپریتی» با پرچم لیبریا دقایقی بعد در حدود ۱۷ مایل دریایی در شرق خصب مورد اصابت سه پرتابه ناشناس قرار گرفت.
پیشتر سازمان عملیات تجارت دریایی بریتانیا از حمله به این نفتکش خبر داده و گفته بود سه پرتابه به آن هنگام خروج از تنگه هرمز برخورد کرده است.
بر اساس گزارش‌ها، خدمه این دو نفتکش سالم هستند و هر دو به فاصله کوتاهی از یکدیگر متوقف شده‌اند.
داده‌های شرکت کپلر نشان می‌دهد که هر یک از این نفتکش‌ها هفته گذشته ۲ میلیون بشکه نفت خام عربستان سعودی را از بندر جعیمه در خلیج فارس بارگیری کرده بودند.
با تشدید دوبارهٔ درگیری ایران و آمریکا، قیمت برنت روز دوشنبه نزدیک به سه درصد افزایش یافت و به ۹۰ دلار و ۴۹ سنت رسید و روز سه‌شنبه نیز با ادامه روند صعودی به حدود ۹۱ دلار و ۱۵ سنت در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/78133" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HS4WGdYHAATftQgoZEVlSZSorvBKI9hsZDZKFPzLlvPzBH4s1YxYk8JFqDRtWMBpK1N86ZqqScGQeDObGE3dD9JIylYsS1KYmAJtB8NPbjKbqL9zQMvEzn32etk3yGiFZY4BoooYf10VVeuPhGAZ8q2SHsTgmcvHQwn6ucnRDGs--rOEdYvqaORgvanLOQdoJth1EHPPwHynLkUxnWclckvvk1l4EmqJesxSGQeTYtUKz8cs3zSI8aUyGuj9dpqwDYPe31S5R6G6MqjseIgY23H3p9PiSEJME2PJYZdRLsOLPtu8576bv23J03f-vNyZwel0e3cdOoBrY5Yf8R8QCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران، از ساکنان اسرائیل خواست به کشورهای خود بازگردند و «به‌سرعت فرار کنند». او گفت با کسانی که بمانند، مانند بنی‌قریظه رفتار خواهد شد.
نقدی گفت: «آنها باید بدانند رفتاری که نیروهای اسلام پس از رسیدن به آنجا در پیش خواهند گرفت، همان رفتاری خواهد بود که با بنی‌قریظه شد.»
او افزود: «پس باید به‌سرعت فرار کنند و هر کس بماند، بر اساس شیوه‌ای که با بنی‌قریظه رفتار شد و مطابق حکم تورات، نه بر اساس رحمت اسلامی، با او رفتار خواهد شد.»
بنی‌قریظه یکی از قبایل یهودی ساکن مدینه در دوره محمد، پیامبر مسلمانان، بود. بر اساس روایت‌های تاریخی اسلامی، پس از نبرد خندق و تسلیم بنی‌قریظه، مردان این قبیله کشته و زنان و کودکان به اسارت گرفته شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/78132" target="_blank">📅 18:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qrQd_Nhfeq2dZhXWsyWyft3qyGBru4oydEKBAzllP3HFp1EkteyFAJYaefDeFJ01vzgrs_kDNKo0baGVb0RYu3RW-Qa2vZUR4nnyufa-4Pk4hk2b19zsSzq19Hn98OF_HuS01p92Q5awC0HLOuYfndoxj8uCIfZGv04E2nTXe_k_6UX-21uKBomLHx6O7uQpDmhP-RFYZ2tzKwtwagYLFJVxFD-G0L4TAze5JF29IQil0kbx_CmzeGGy8RblBPw2jEC7BPUvjQ6PMd-CWnRrfn9ORJL5kHZoGkIo1z_NS--eAwRUwPG8plOJCNhvxYKNmGlvJevLf8NTqIKPOc1Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u-47G4uWbBwMblt2XNEqzPjCj7HOvbqk-6jbpd3A4O9AZWFktM3aknPickmJplpkdFSOaylfOjLTPm_VUQbC1dFEZw72di_PAFvsOYEOW_ZO66SqMP35YngDOODD1vF5Opp3KrYzwDlHQTkoOVvMzsBMUJZI_QHxcERfhWxwGuwoUmD_N2zUYAEC5exx-rvJ_4muF1jV7bGK5HOHsBYpy9Wd9CU8w-E3-MyjjLK7acr8Y0Fs1wWHmyaYHH2s5GQaBhDWtH8V3k6cYBKZ4MLUsQaPCcHOE0ZkCZ0cMflh8fW2XqOqktuoMUGHvaFbW9akU_gZVmxYGYfw-RoRL5O8kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«کانون صنفی استادان دانشگاهی ایران» هشدار داده است اگر قانون ترمیم حقوق اعضای هیئت علمی تا پایان شهریور ۱۴۰۵ به‌طور کامل اجرا نشود، از استادان خواهد خواست فعالیت‌های دانشگاهی خود را از ابتدای مهر تعلیق کنند.
این کانون در بیانیه‌ای اعلام کرده است تعلیق فعالیت‌ها، حوزه‌های آموزشی، پژوهشی، اجرایی و مشاوره‌ای را شامل می‌شود و تا زمان اجرای «کامل و بی‌قیدوشرط» قانون ادامه خواهد یافت.
کانون صنفی استادان، سازمان برنامه‌وبودجه و رییس آن را به «مانع‌تراشی‌های سلیقه‌ای و خارج از عرف» متهم کرده و گفته است مکاتبه، مذاکره و رایزنی با مقام‌های مسئول نیز تاکنون به نتیجه نرسیده است.
این تشکل صنفی همچنین هشدار داده است ادامه بی‌توجهی به وضعیت معیشتی دانشگاهیان می‌تواند به افزایش مهاجرت نخبگان، کاهش بهره‌وری علمی و واردشدن آسیب‌های جبران‌ناپذیر به سرمایه انسانی کشور منجر شود.
مصوبه اصلاح حقوق اعضای هیئت علمی روز ۱۸ اسفند ۱۴۰۴ در شورای حقوق و دستمزد تصویب شد و قرار بود از ابتدای سال ۱۴۰۵ اجرا شود. این مصوبه، تغییر فرمول محاسبه حقوق و اصلاح ضر‌ایب مبنای پرداخت به اعضای هیئت علمی را در بر می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/78130" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=GeG2hfoseiMMMglYfn6iKwapjCP8A1yW-g1c5USfwUk-acO5OhQvuTQjohpPeZPgQAClfI_haMm6mjTgVYH8PmfVGl2rFI_RWqQ8Zo8N9a55pU69z6pwBThG_Y872iOT58XFNpreMoj7Br0LYbgFL_p47rdTfJHf8SEOT4xIg5wUC4LXCQffdVwsbeNwQKWMe9i8Z_IZBl68HbjzAwFY4TJyLOcmO5VpYH640XtL-ZpatVZZ53g2YbhikHD1cOS7sbqiayhubQikvFKBeajKUSOwItX7LdlixgFe7ImDKpTNuc3AYKJuLArZnQwdFmHp_mtkZXjBQq_EMyDmye-xpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=GeG2hfoseiMMMglYfn6iKwapjCP8A1yW-g1c5USfwUk-acO5OhQvuTQjohpPeZPgQAClfI_haMm6mjTgVYH8PmfVGl2rFI_RWqQ8Zo8N9a55pU69z6pwBThG_Y872iOT58XFNpreMoj7Br0LYbgFL_p47rdTfJHf8SEOT4xIg5wUC4LXCQffdVwsbeNwQKWMe9i8Z_IZBl68HbjzAwFY4TJyLOcmO5VpYH640XtL-ZpatVZZ53g2YbhikHD1cOS7sbqiayhubQikvFKBeajKUSOwItX7LdlixgFe7ImDKpTNuc3AYKJuLArZnQwdFmHp_mtkZXjBQq_EMyDmye-xpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، روز سه‌شنبه ۱۰ شهریور در دیدار با ولادیمیر پوتین، رئیس‌جمهوری روسیه اعلام کرد که اگر ایالات متحده آمریکا به تفاهم‌نامه اسلام‌آباد برگردد، تهران نیز آماده است که به مفاد آن عمل کند.
پزشکیان، در این دیدار که در حاشیه نشست سران سازمان همکاری شانگهای برگزار شد، حضور ایران در سازمان‌هایی چون شانگهای و بریکس را تلاشی برای مقابله با «یک‌جانبه‌گرایی» آمریکا توصیف کرد.
پزشکیان در ادامه با تاکید بر تفاهم ایران و روسیه در زمینه ضرورت چندجانبه‌سازی در سیاست و اقتصاد جهانی، ابراز امیدواری کرد که این فرآیند به شکلی موفق پیش برود.
@
VahidOOnLine
مسعود پزشکیان، رییس دولت جمهوری اسلامی، در دیدار با ولادیمیر پوتین، رییس‌جمهور روسیه، گفت: «از موضع روسیه درباره جنگ و تحریم‌ها تشکر می‌کنیم. می‌توانیم در برابر یک‌جانبه‌گرایی آمریکا مقاومت کنیم. آمریکا حق ندارد تحریم اعمال کند و قوانین بین‌المللی را نقض کند.»
پزشکیان گفت: «حمله آمریکا هیچ توجیه منطقی نداشت.»
@
VahidOnLive
ولادیمیر پوتین، گفت مسکو از هر فرصتی برای دیدار، گفتگو و انجام رایزنی با تهران استفاده می‌کند.
پوتین با ابراز خرسندی از دیدار دوباره با پزشکیان گفت روابط دوستانه روسیه و ایران در همه زمینه‌ها به‌طور باثبات در حال توسعه است و این روابط مطابق با «متن و روح پیمان مشارکت جامع راهبردی» میان دو کشور پیش می‌رود.
@
VahidOOnLine
عباس عراقچی در پایان روز نخست نشست سران شانگهای در قرقیزستان گفت: «یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود.»
عباس عراقچی گفت «آمریکا باید به تعهدات خود بازگردد و به مفاد یادداشت تفاهم پایبند باشد؛ پس از آن می‌توانیم از این وضعیت خارج شویم چون همه کشورها دغدغه دارند که جنگ هرچه سریع‌تر خاتمه پیدا کند.»
مسعود پزشکیان امروز در حاشیه نشست شانگهای با رهبران هند، پاکستان و آذربایجان به طور جداگانه دیدار کرد.
شی جین‌پینگ، رئیس‌جمهور چین، ولادیمیر پوتین، رئیس‌جمهور روسیه، مسعود پزشکیان و بیش از ۱۲ رهبر دیگر امروز در قرقیزستان گرد هم آمده‌اند تا در نشست دو روزه سازمان همکاری شانگهای شرکت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/78128" target="_blank">📅 18:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78127">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWBKT_LTd-HuWgOdtxw18yNhXWadm8lWpjXApRucB-nDwcjWPg5ThfjjgK-zbSaPcblYbvlLmfdciX5zTbZcr6chTZQ5PBQ2q2qhCqZw8haEiI0jDeIikqBGShMRQg6iiY5vXVOT3rn7pwnrAlr-5mXpVKmeoXeJP3xtH5a3D2GmQgPWMxyOmw8XN5ky_mMisxP-fhStd9KL2Jqtk0jEontRr2c23EHm8Ru3GoSNiO6YbJhlaUvOkKFFk8vs59ZfquG6VJFyfQeBxYtsJWJ5V54p8efjzTSY16p2dWxEN14tzJH7cHsB4J9Tc0NFFF2Cx2b6gyPMM7FeWsK2HAYLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر بختیاری، پدر پویا بختیاری از جان‌باختگان اعتراضات آبان ۱۳۹۸، از سوی شعبه اول دادگاه انقلاب بندرعباس در مجموع به ۱۰ سال حبس تعزیری دیگر محکوم شده است.
براساس حکم صادرشده، او با اتهام «فعالیت تبلیغی علیه نظام جمهوری اسلامی از طریق هم‌سویی رسانه‌ای با معاندان» به یک سال حبس، با اتهام «تحریک مردم به جنگ و کشتار با یکدیگر به قصد برهم‌زدن امنیت کشور» به چهار سال حبس و با اتهام «ارسال فیلم به شبکه‌های مجازی بیگانه برخلاف امنیت ملی» به پنج سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/78127" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezrIBHgwWF1PnEO4t7Tn_NpP2LiJns24S3fD3VHKqT3O-33MKZaL_1YUyXQSCAYZ2DjhPFz6eazf2tfjqTgqQp79jHAkSOPinO7j07qSw7tWFzpYJNOvH1nxRdPob8PxNs2UBeJCgQWuiHiBwGoCt4tXBDGzrJMXN7LWXaTXL42uppkaOLXPjk2NUlqDG0Jyo_tyvTqd8Pwk-DWCaL8IOXcZiHTxjhwVsXvqML8q7PQZO8kwXLaIMPMIRg70BSKaqoi2Rm5d5a64WUzD1Daw2JaRHbWoFVPLWhDUyfV2XDZKDf7ME5HGSuzBl9rHUAV3BlPxQpxQJZeyHUaL6EpwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=FWNPl-9hgDsI0BbwoBTyoNBQQ1fyLEUq07E3VTmRqPsY7WcKooTX44Ai1YthrtJ995hznkMDpSSwwdTNzJ0DvMJdwmkV7xSnjfsmELkYNAIJyEHYaofJfRvm4ocaz3edMS4WdRXFPLlRNXmCh3fy-ytjwG3RAKj51lH-u12L5Ev5OIRtnrcUPOrf1h9tYsqOiw6VgONKMOgHIa85egsc-I35LcUkk75ownSoEAmWPcvFmlXBjALmE-bUIXlrqfiCuXjxyASXsi1Nh6TzLP0CCyYtfd9vdxzUGOtPOE6f6dAIyITaa5boW3jvxpO8jhud4XSlr9naD68x2M1D-rHU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=FWNPl-9hgDsI0BbwoBTyoNBQQ1fyLEUq07E3VTmRqPsY7WcKooTX44Ai1YthrtJ995hznkMDpSSwwdTNzJ0DvMJdwmkV7xSnjfsmELkYNAIJyEHYaofJfRvm4ocaz3edMS4WdRXFPLlRNXmCh3fy-ytjwG3RAKj51lH-u12L5Ev5OIRtnrcUPOrf1h9tYsqOiw6VgONKMOgHIa85egsc-I35LcUkk75ownSoEAmWPcvFmlXBjALmE-bUIXlrqfiCuXjxyASXsi1Nh6TzLP0CCyYtfd9vdxzUGOtPOE6f6dAIyITaa5boW3jvxpO8jhud4XSlr9naD68x2M1D-rHU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.
بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی از بابت اتهام «افساد فی‌الارض از طریق اقدام گسترده در انجام فعالیت‌های سیاسی، ایجاد انعکاس خسارت تصنعی، تهیه اخبار کذب، تبلیغ علیه نظام، برهم زدن امنیت و ورود و خروج غیرمجاز به کشور» صادر شده است. حکم مذکور در تاریخ 1شهریورماه ۱۴۰۵ به وی ابلاغ شده است.
آقای زارعی دوزدره‌سی که پیش از این در آلمان به سر می‌برد، در تاریخ ۸ اردیبهشت‌ماه ۱۴۰۵، پس از ورود به ایران توسط مأموران اداره اطلاعات بازداشت شد.
پرونده وی در مرحله تحقیقات مقدماتی در شعبه سوم بازپرسی دادسرای ناحیه ۳۳ تهران، موسوم به دادسرای امنیت، مورد رسیدگی قرار گرفت.
وی نهایتا در تاریخ ۹ تیرماه همان سال به زندان قزلحصار کرج منتقل شد. این زندانی در حال حاضر در واحد سه، بند ۳۷ این زندان نگهداری می‌شود.
علی زارعی دوزدره‌سی، حدودا ۲۷ ساله و ساکن تهران در جریان اعتراضات سراسری سال ۱۴۰۱ یکی از چشمانش با شلیک گلوله ساچمه ای آسیب دیده بود. وی پیش از این نیز سابقه بازداشت و برخورد قضایی را داشته است.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78123" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCZGGkUTE9BQ1mXvCaH-OvWEKPknElpzeKtS7SlWOkCgbl6AofZUYXelr3PmwThp3xpBOFDarsvV9J08IjFQqMdn5CN0PPUpwIPtkZW2QcGm4nDTlGkZOO7_d_egyiQ1TOnU6jYK3s1k8G3WcsCYODFl6mZeqEEznzyE5T1sKdh-S50xx7NnDeJ6BlOJ3Jiv_qIPwHpkn-0yQTn8mKiYhAmZvGZvZ-8ALZW37NhlMFBchsD7ugLe9XuTNqAwVUYXziQHXU-TgOAbQtSWLSjuurUEE_-f4A-U_HedZfDFWhgq2TZzCIwfi9Swi8ndcLTaU7I5qa8jBvax2RP_NE3eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک نفتکش در تنگه هرمز «هدف قرار گرفته است.»
براساس این گزارش، این نفتکش «هنگام عبور از تنگه هرمز و خروج از آن» هدف قرار گرفته است.
سازمان عملیات تجارت دریایی بریتانیا گفته این حادثه در فاصله ۳۱ کیلومتری شرق منطقه خصب عمان، «هدف اصابت سه پرتابه ناشناس قرار گرفته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78122" target="_blank">📅 03:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78121" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khGgEL346-t3xC0_2SeQg6w37KWHlxGg_g7Zkm_lInG7uFm6UKAOApJikttcY5Fx2qMHEt27yXHrNXyVxe1PHD01Ag3hu871E2zkorl-0VgXKokDgDxczc8AFqJA6u7Fg6AiBBrQVwuDGRgHkGiVKmcP_l3-CWWYclXwjzgmUc7Pl_Ivrfe61jvqh3cvAP299w9iw05CVDunMRGjQgHUEMhV0sY1G5Q0_D-XgxON2tt_CkAhPlk9pyc5YrVldNvUugtsHcyn7wi3_VdUcTzfSwQOxF3SnZCNpDWsPW4kD_3jOD-xVIAs2xpC7byGAAqRskAD4NN2h0do0Qp1kdKHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه مقام آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهور آمریکا، و مشاوران ارشدش در حال بررسی انجام حملات محدود در تنگه هرمز برای جلوگیری از بازسازی توانمندی‌های راداری و موشکی جمهوری اسلامی جهت حمله به کشتی‌ها هستند.
بر اساس این گزارش، این طرح که طی هفته گذشته توسط فرماندهی مرکزی آمریکا تهیه و از سوی وزیر جنگ، پیت هگست، حمایت شده بود، پیش از تبادل آتش این آخر هفته با ایران به تایید ترامپ نرسیده بود. اما او ممکن است پس از تشدید جدید تنش‌ها با آن موافقت کند.
یکی از مقامات آمریکایی گفت ایده اصلی این طرح، کاهش خطر حملات تهران به نفتکش‌ها، شناورهای نیروی دریایی آمریکا و هواپیماهای نیروی هوایی آمریکا است؛ به گفته این مقام، هدف «کوتاه کردن چمن» است.
یکی از مقامات کاخ سفید گفت: «رییس‌جمهور همه گزینه‌ها را در اختیار دارد. ایرانی‌ها می‌خواهند توافق کنند، اما همیشه یک روز دیر و یک دلار کم می‌آورند.»
ترامپ عصر دوشنبه به فاکس‌نیوز گفت که آمریکا به حملات جمهوری پاسخ خواهد داد و «آنها را به‌شدت هدف قرار خواهد داد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78120" target="_blank">📅 22:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7deyJKt_5h1qih8XxBpt7yhg-h3gpbAfNP7Has8I7MDt81MkC1J0dgBuaJfG9rCsK-CsvEi9U8H8UgtzJRxFakOtFaH_zCH_idIyFbI5moFJb6PfMeB3CO2BL_YSmWnzR508PkwTUlmW_AYGOZOS_8Xzl-39wZeUPPeH2W1Oj8W9oK9hMsHbVL_VmZrbumAigdBlmpmGcrmZkJaNM7vXZq0Ijn7-ex0f_fsgr-LC8W21yaUXiqaKZPNLLQGtdHTtMSp6n2dScvzYPMvIYv3sPdqjY7b7zpOyDTQ27SNVZZoX3QaGcIsKrNRT3Ox8B4_HuRl0hPSFq1YjnOGa5p27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح جمهوری اسلامی روز دوشنبه در بیانیه‌ای مدعی شد که ایالات متحده از آسمان یا خاک برخی کشورهای خاورمیانه برای استفاده از ایران استفاده می‌کند و هشدار داد آنها را هدف قرار خواهد داد.
این بیانیه ساعاتی بعد از آن منتشر شد که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد ارتش این کشور به حمله شب گذشته ایران به نیروهای آمریکایی در اردن، ایران را به شدت هدف حملات انتقام‌جویانه قرار خواهد داد.
ستادکل نیروهای مسلح ایران در بیانیه خود گفته است «ضمن احترام به حاکمیت ملی همسایگان»، در صورت ادامه حملات آمریکا، نیروهای نظامی جمهوری اسلامی «پاسخی سنگین‌تر» از حملات شب گذشته خواهد داد.
ارتش آمریکا اعلام کرد شامگاه یکشنبه «نیروهای مین‌گذار سپاه» در جزیره لارک را هدف قرار داده است. در پی این حمله، سپاه پاسداران از حمله موشکی به دو پایگاه نظامی در اردن خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78119" target="_blank">📅 22:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hLjgueS2tdUKjocunylg72i37R0kp5NrcFyLTZiftXs7DRPuT4A0jkPc9GMYpzQAKsBaqENpWlaHb06gK1UoUz2aoj5y1wSbYtURQuxUbih2bYSruCUuRk9IhE4B0t_kMUO53PpoULvKgGUgZuwhO9_9A6JGnCtMXnqSel4fA06Gxwz8pcOItXPxH2gQfO47TrDO2osHul7-y3HLuoiogGG0LE7teCZLEguV4vTYSaasWpsET99gNPzRI8NKlttqcKUhdtOoJdPtbesapM0Rp2ou6obqzGAepj7VFGdWglSHXeuWJnSJeG8jhMB1o8LYS0L4fxX79F4BqxisakAr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه عربستان سعودی روز دوشنبه نهم شهریور در بیانیه‌ای اعلام کرد که کشور‌های عربستان سعودی، ترکیه و پاکستان توافق کرده‌اند در قالب «پیمان دفاعی مشترک مکه»، دبیرخانه‌ای را در عربستان سعودی تاسیس کنند.
بر اساس این بیانیه، ریاست این دبیرخانه در سه سال نخست بر عهده دبیرکلی از کشور پاکستان خواهد بود.
در همین راستا، وزارت امور خارجه ترکیه نیز اعلام کرد که تنظیم سازوکارهایی برای پیوستن سایر کشورها به این پیمان، در دست بررسی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78118" target="_blank">📅 19:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=JaIfvaHqm39hly1K9PU_H5TEAXgeEVK1Fb87HHma75THH54yaPAYgIJRJTRStVYPHSHyefDaYBMhz4J6Nr3kSNu5F-Ghq0QTyGBviGskdtEuW6wounW8S-mImLCNFNPGJv-RBSsCOwndLDuvid9S5rvJlBfPPM5hOfzHiqqU3wUqkAR70HTiPVpw2_NP2SkMgrnXRWSfns3AqcNNxrE9CpkLiGy_cf_SGyxiz6NuFXKokBXFk25jWJBr7nq84-sgOtGMtRzjLnvfTyV0oKA8_msyrWASLdPuapKWp_rC_3dfh__sOmUFN19naQwrsy5iVRLz5cndyxCMrhosMwSZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=JaIfvaHqm39hly1K9PU_H5TEAXgeEVK1Fb87HHma75THH54yaPAYgIJRJTRStVYPHSHyefDaYBMhz4J6Nr3kSNu5F-Ghq0QTyGBviGskdtEuW6wounW8S-mImLCNFNPGJv-RBSsCOwndLDuvid9S5rvJlBfPPM5hOfzHiqqU3wUqkAR70HTiPVpw2_NP2SkMgrnXRWSfns3AqcNNxrE9CpkLiGy_cf_SGyxiz6NuFXKokBXFk25jWJBr7nq84-sgOtGMtRzjLnvfTyV0oKA8_msyrWASLdPuapKWp_rC_3dfh__sOmUFN19naQwrsy5iVRLz5cndyxCMrhosMwSZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا ویدیوهایی ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.  ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»  این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر…</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78117" target="_blank">📅 19:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=DQjT3UZ1zqvzqPSKkaCL6MKNia-KYmpJDtINEpVndd-yNXp1umFCvTSkGrkHA8l_HhIEIQsM_uAZ9EIsvX0yDMi_mv4wd32G5cHL3V93BSi7jeJLMs8GCf1LBMPCwPEbfxXyz0y5xpIHxeyYs3q0enE9mNtJ5u-ArLeqvK1gWjk-rS9S6hQmg_VptCFMi81CShe1iusN-VsrqMT_REnDaaA69IwBLxHi1d6GzVwerpA6pzymDTnXzV9B2AF5zlSit8jQZLc-ZPWU6cgb0xj3wVWRIcVAlayPzSsN7uVnVX0_RseWzxbaldaX-CI3Csf8BJc8vCot9Pl6gi2gMFoarA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=DQjT3UZ1zqvzqPSKkaCL6MKNia-KYmpJDtINEpVndd-yNXp1umFCvTSkGrkHA8l_HhIEIQsM_uAZ9EIsvX0yDMi_mv4wd32G5cHL3V93BSi7jeJLMs8GCf1LBMPCwPEbfxXyz0y5xpIHxeyYs3q0enE9mNtJ5u-ArLeqvK1gWjk-rS9S6hQmg_VptCFMi81CShe1iusN-VsrqMT_REnDaaA69IwBLxHi1d6GzVwerpA6pzymDTnXzV9B2AF5zlSit8jQZLc-ZPWU6cgb0xj3wVWRIcVAlayPzSsN7uVnVX0_RseWzxbaldaX-CI3Csf8BJc8vCot9Pl6gi2gMFoarA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه نهم شهریور ماه در حاشیه نشست «جی ۲۰» در اشویل آمریکا گفت واشنگتن به اعمال فشار اقتصادی بر تهران ادامه خواهد داد و ممکن است نتایج این فشار طی هفته‌ها یا ماه‌های آینده نمایان شود.
بسنت در پاسخ به پرسشی درباره زمان احتمالی فروپاشی اقتصاد ایران گفت: « مسئله این است که ما محاصره را داریم و به اعمال فشار ادامه خواهیم داد. ما همین حالا گفتگوهای بسیار خوبی در اینجا داشته‌ایم و فکر می‌کنم این می‌تواند طی هفته‌ها یا ماه‌ها رخ دهد.»
وزیر خزانه‌داری آمریکا افزود: «اقتصاد لزوما نباید فروبپاشد؛ فقط باید حکومت ایران به خود بیاید.»
این مقام آمریکایی افزود بسنت در حاشیه نشست گروه ۲۰ با همتایان خود دیدار خواهد کرد و برای افزایش فشار اقتصادی و منزوی کردن ایران تلاش خواهد کرد.
اسکات بسنت، در ادامه با اشاره به حمله ایران به پایگاه‌های نظامی آمریکا در اردن گفت: «به نظرم آنها به‌صورت نظامی دست به واکنش می‌زنند، چون از نظر اقتصادی در حال شکست خوردن هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78116" target="_blank">📅 19:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=YHwR87a4lw1i6aiXLHlW5IziARAyaMJZ-4IJ0dxEdbe1DN7IxIrmIkXjtESJnsrTMdRLfg7JJnSYlee-9zYCKA9zzdME1dZt-qXEzCcLnKUcPx89XcnPlKopiADYvbzj20baDq06YUwCer16VCRJQGdTW5nzD4KjrEYKli1_w5HNnbUNmP0VDrrQkN0j6z-ixguFQ8cO8hODd-0u-dRX6WSaAru_RRU6T4MLVKXKjuTfyTJW_XGOMd3d3romugJ8IVCVMHhjW9fi-CLXQnRuN2Tz8NyCewJSkGu4Eu28fsFin1FbPcmYh93_Ru6DAy6cgtqMrSgfpCGSrpnoMmw54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=YHwR87a4lw1i6aiXLHlW5IziARAyaMJZ-4IJ0dxEdbe1DN7IxIrmIkXjtESJnsrTMdRLfg7JJnSYlee-9zYCKA9zzdME1dZt-qXEzCcLnKUcPx89XcnPlKopiADYvbzj20baDq06YUwCer16VCRJQGdTW5nzD4KjrEYKli1_w5HNnbUNmP0VDrrQkN0j6z-ixguFQ8cO8hODd-0u-dRX6WSaAru_RRU6T4MLVKXKjuTfyTJW_XGOMd3d3romugJ8IVCVMHhjW9fi-CLXQnRuN2Tz8NyCewJSkGu4Eu28fsFin1FbPcmYh93_Ru6DAy6cgtqMrSgfpCGSrpnoMmw54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز دوشنبه ۹ شهریور ۱۴۰۵، شماری از شهروندان جویای کار در شهرستان گچساران در اعتراض به روند استخدام نیرو در پالایشگاه لیشتر تجمع کردند.
در ویدیوی منتشرشده از این تجمع، تیراندازی نیروهای انتظامی برای متفرق‌کردن معترضان دیده می‌شود. برخی گزارش‌ها نیز از زخمی‌شدن یک نفر در جریان این تیراندازی حکایت دارد.
این تجمع در اعتراض به نحوه جذب و استخدام نیرو در پالایشگاه لیشتر برگزار شده است؛ پالایشگاهی که به‌تازگی افتتاح شده است.
@
VahidHeadline
نیروهای امنیتی و پلیس، جوانان عرب معترض به بیکاری در مقابل شرکت نیشکر «دعبل خزاعی» در اهواز را با ضرب‌وشتم و تیراندازی متفرق کرده‌اند.
در این ویدیو، مردی که در حال فیلم‌برداری است می‌گوید: «این جوانان همه گرسنه هستند، هیچ‌کس ما را استخدام نمی‌کند. هیچ‌کس برای ما ارزش نمی‌گذارد. هر کدام از آن‌ها با اسلحه کلاشینکوف به‌دنبال جوانان افتادند. ما کار می‌خواهیم. جوانان گرسنه هستند. ما هیچ آهی در بساط نداریم. ما کار می‌خواهیم.»
سازمان حقوق‌بشر «کارون» روز دوشنبه نهم‌شهریور۱۴۰۵ در گزارشی نوشته است که «جوانان و خانواده‌های معترض که به نمایندگی از ساکنان همجوار این شرکت دست به تجمع زده بودند، با طرح مطالبات خود اعلام کرده‌اند که شرکت نیشکر دعبل خزاعی در زمینی به مساحت حدود ۱۲ هزار هکتار فعالیت می‌کند که بخش قابل‌توجهی از این اراضی متعلق به منطقه و مردم بومی آن است. با این وجود و علی‌رغم حضور جوانان بومی دارای مدارک تحصیلی و تخصص‌های مختلف، مدیریت شرکت اولویت را به جذب نیروهای غیربومی داده و باعث شده تا جوانان منطقه همچنان از فرصت‌های اولیه اشتغال محروم بمانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78114" target="_blank">📅 19:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NWIp57JQoyiqfteUKTYbrDmTfe6jIH5YM0-kkODA2uIEzPusEsP6ldx0HFmLSDM0B-4RtYsNISR7BkKNRLfFpjbU_gcdevtlmZ8eaWakrwctP3GZqwfHzwwLKBNxp7TCNHxkNDWxO0iSut-7XCHHzxl4lLdwraj6zL6EW_mAH6wh5TkaUmkI2KmsKB8zbRtYUEpfbNGyRgfnbKlY3_tOs5NiYyZkV0lHYONfLuu_pLgfOeP92FhIAe88-5Xuc8tB6B7BUQIWBv2sVVBPgDPJNNCF3y7vAyizFmE15NF_wrZCgOQ0ShterFIlxOjhk3DMDbO_e4BgsA8QgQRoRGwfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fh6wfKwrmtD9ZxUqBzbdkvdBCpnW9pn3prhuaL6ZuYs-cgZ7chj33dSrtv9tClUgRRbHg5B3US1Uklo8ZCtwLZGx6UC44gEgg6haq4UuPMVZNhx_9ftiPwOJCR6F1-VSGZdia9YvLKAcEot8kDMUptmaEk4BRCPWh5BFrybc0Jnbq86lsuQ6pEiXnR9TlaABZ7iZnWLpxHBj_6Fp_yJ1ZpMzwmU_zOCbzmp0LQmCTIonOpDQO_lIPzyM6aon81DB2SC0Yvg5G_R7y9zM-OveMoVu2VntoHbB22YrJW872spTiGWHgQpLVdVSK-cdlMgWOKnqOoFpry9kzqHlSMBH5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اژه‌ای معترضان را به برخورد قاطع‌تر تهدید کرد
در پی تشدید بحران اقتصادی و رسیدن دلار آمریکا به مرز ۲۱۰ هزار تومان، رئیس قوه قضائیه جمهوری اسلامی گفت این نهاد برای مجازات «عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است».
این تهدید پس از آن صورت گرفته است که دستگاه‌های حکومتی بروز اعتراضات مردمی را پیش‌بینی کردند.
غلامحسین محسنی اژه‌ای افزود تحکیم امنیت و مقابله قاطع با عناصر ضدامنیتی از مقولاتی است که مردم و مسئولان درباره آن اتفاق‌نظر دارند.
این رویکرد با پیام مکتوب مجتبی خامنه‌ای در هفته دولت تشدید شده است.
خامنه‌ای در این پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با انتشار گزارشی به حضور «شماری از دانشجویان زن بدون حجاب اجباری» در جلسه رییس سازمان امور دانشجویان و مشاور وزیر علوم اعتراض کرد و خواستار «واکنش قاطع و فوری» وزارت علوم و واکنش نهادهای امنیتی و دستگاه‌های قضایی شد.
به نوشته فارس، انتشار تصاویر جلسه‌ای با حضور رییس سازمان امور دانشجویان، مشاور وزیر علوم و شماری از اعضای شوراهای صنفی دانشگاه‌ها که در آن تعدادی از دانشجویان زن بدون حجاب اجباری حضور داشتند، «با اعتراض گروهی از استادان و دانشجویان» مواجه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78112" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78111">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RlE4nwiEEVmcfNsizLdnDZ9BDeni1nIaNYGp-2pLcAgaiJ8XJu4NXHAXmUetjKflZqE3yg-oJ2Odxz_E489GCYTXDWUrVswa5rp1tJ2OsFXk0cDVLSCoJeGtFfjtB8zMJ4db_L4E0X_00hYVjZ1s928Y6dv-9g6J55eEddBi--sBF3Ik0Ux-aFLXiGSEszRHLczDkBbhtnu4wYaSqkgemu9Z3pMhxkR_6O1POJNllf6zCCmANZmIdQctb7XCZPQ0bOZI0S32j78-xIIuo_UkghSHX2kCjFed8mMHZCBnSPyrsu6WmMBMGEw6HN217l3anpJQem03W9yzG3Uqooiwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا روز دوشنبه اعلام کرد که به همکاری با ایالات متحده و سایر شرکای بین‌المللی و گروه هفت «برای حفظ فشار بر ایران و کمک به کاهش تنش و ثبات منطقه‌ای» ادامه خواهد داد.
در این بیانیه آمده است:‌ «اتحادیه اروپا از تلاش‌ها برای اطمینان از اینکه ایران فعالیت‌های بی‌ثبات‌کننده خود را متوقف کند و با حسن نیت در مذاکرات صلح شرکت کند، از جمله از طریق فشار اقتصادی بیشتر، شامل عملیات طرد اقتصادی به رهبری ایالات متحده، استقبال می‌کند.»
«عملیات طرد اقتصادی» عنوانی است که مقام‌های دولت آمریکا بر برنامه فشار اقتصادی تازه بر جمهوری اسلامی گذاشته‌اند.
بیانیه اتحادیه اروپا در آستانه آغاز نشست گروه ۲۰ به میزبانی آمریکا صادر شده است.
اسکات بسنت، وزیر خزانه‌داری آمریکا به خبرگزاری رویترز گفته است در این نشست از وزیران دارایی و روسای بانک‌های مرکزی کشورهای جهان خواهد خواست تا روابط اقتصادی‌شان را با ایران قطع کنند؛ در غیر این صورت با تحریم‌های ثانویه آمریکا روبه‌رو خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78111" target="_blank">📅 17:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNnKAVj1owV9a4bS5SweHiQcTcPMC9UKqhswVvSin0qj8Akd4zh8qgkm629FEzn1Q5BvTEcOoK9u_VwE3x2UKruUa3zjm7X1gYrRjr-Tl_ib52sXx-seh_vKiyliNU9ajb7jScFJuVf0Y4ZbqB8XRgHpK4o2kn_GB02W039nafMiHHPj9ZBYfomjrWv6DdDcAojBwojy34fcpwmn3lPYHj5N6TsAl8J6_6Pwsj7AFaPY-VWdGe5iYINE1ii7RaGH-Y3iR_0BghRyWrWi-_Nhup1lb3AdzwO92oovQgiq-oYMZijVtzdFTKi2KxBG7mNE2kVUMo9eBgIl3W2h9E_YQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روند نزولی ارزش پول ملی در ایران، قیمت دلار آمریکا دوشنبه، نهم شهریور از ۲۱۰ هزار تومان عبور کرد.
همزمان پوند بریتانیا از ۲۸۴ هزار تومان عبور کرد و یورو نیز به مرز ۲۴۳ هزار تومان رسید. قیمت هر سکه طلای طرح جدید، موسوم به «امامی» نیز از ۲۲۳ میلیون تومان فراتر رفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78110" target="_blank">📅 17:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cshDTpLQUWmlqIdHk2O7bJvqUe0UNUaSBLh6F2n5QaQJ2L90fYIX_0Xw8WeldqvXPmLcAieGbpS6_0KnmmAvN7w6COwJA4Sj11snTUXb0aNiAHB8e-aEUaiibGkmkTaXo2MYtQmJ5gX8tiAkgapqA0CXefN2CJXzn1QCzlGOqB03gg-7SfKUJh-DFBBHAxeklObiF1obU8WCvZzKXZZID4HsrFELsaOXMSoLd9pLgYJOw7TDTRLoa-MgOkPF48n9AnRZRM2z0YE4D6ckneeZlIFu5Shm9iyehQEWQk9RJlCAQlV7Vrn20hPQ66RSmKUT44c5QBzT4CUkmfbzaE1GYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران (IRGC) ادعا می‌کند که یک ابرنفتکش هنگام عبور از مسیر جنوبی تنگه هرمز با دو مین برخورد کرده و کاملاً متوقف شده است. این ادعا
نادرست است.
✅
واقعیت:
هیچ کشتی‌ای در تنگه هرمز با مین برخورد نکرده است. این نیز یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه از طریق انتشار اطلاعات نادرست است.
CENTCOM
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78109" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78108" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78107">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCfiAcxmK_oqlOwfN7zBdR-JlVGI1cB5XUk9Kv7SwkpLfxg-XDZpReBiYe_8Q2iOYYLJXxhLu8og4BauIx1vAX9AWlDx8GrFHr7ZeQTCJ863oNj7SmEG6B2KQ28KF97BvRd-3kw04NC6WSMYJ2_PGp9l1HW5IIzv-5LgnxDkvk0dFmszDlTYkOzw1SMr1RV46aMitaYv1y54bQQ5UY5FCFZPg7LtpPp6UXCnwyVdL6-_a8cJG4ExgR6af6rAmiwDEKi0idC6im2cNIijInw4GYBS7tBb-8ezTt6P5pGc1rv0qaiUBVp3bUK2ZkQcrVXLtrCvdclSzTzdLH7OF4mtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه نهم شهریور، در شبکه اجتماعی «تروث سوشال»، جمهوری اسلامی ایران را رسما یک «کشور شکست‌خورده» خواند و خواستار محاکمه بین‌المللی رهبران آن شد.
ترامپ وضعیت ساختارهای اقتصادی و نظامی ایران را «فروپاشی کامل» توصیف کرد و نوشت: «ایران دیگر نه نیروی دریایی دارد و نه نیروی هوایی؛ ارز آن‌ها از دست رفته، حقوق سربازان و نیروهای پلیس پرداخت نمی‌شود و تورم به ۳۰۰ درصد رسیده است. رهبری آن‌ها در آشفتگی مطلق است و توانایی اداره کشور را ندارد.»
رئیس‌جمهوری آمریکا در ادامه با متهم کردن تهران به سرکوب خونین اعتراضات داخلی افزود: «تنها کاری که آن‌ها بلدند کشتار معترضان خود است که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است. مقامات تهران باید به اتهام ارتکاب جنایات جنگی علیه بشریت محاکمه شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78107" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78106">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UhM3oFZ1RbeFLwEBFvpsSCdlSggOtR32ahxTTc7T88GzM3Zy2BtZHtG6nM2XtHWINhFHjzAxikUpFpA3KFjw4FzzzqJYnD7xdEIF0ldNixG_Qa5_6g47mI7xDlFqlxdxdAYoUDSZRyAxCgt47hPV_1aW3-MPsa52m4-tCVd8nkRa3lUyAG1dVxviepCCiq2AudVjikVvwu_3NT7b7xRIQDopqzmELgpKiVRXKxEHGs6bhtBdpJI__KfjZe32OdV6p-bNd_QNO0mfNM8wIqNYdFECX3dMMdsy6ljcbt2EFqCdLmHqOxxlvIzCkiqsl_ydseJB8PuoHQ9j_f-pgkM2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی:
نتانیاهو در عبری آشکارا پُز می‌دهد که دولت آمریکا را فریب داده و به جنگ با ایران، به نیابت از اسرائیل، کشانده است.
نتانیاهو صراحتاً با خنده می‌گوید که چگونه با ۱۰۰۰ ساعت حضور در شبکه‌های تلویزیونی آمریکا، بر آمریکا «تأثیر گذاشته» است.
اما به انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78106" target="_blank">📅 16:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=NhchV6ae4eP0OH7YOUZbl9OzQBRxmO2QHxLhiT1ip3cc3RLXA1WajgdBsGQICrVSUhXK4ODERHxZ_-FnkJnGtGMrn28lXBuoxYj8qCcV5l3VnJ5cGvC6WyIjPgKLh7F2o7hgpEcbD6iMwSdVz2ZnK6O3vMbb7pYHPYAr1qZJQu0QgYsiq0tjfKosUHnpXA2BAmTp1UtePK02aXaY02etoWe3Kqeg8oNVaRKfyTxnGT5eSrzCzSDDpVkW2MoXc95cwTCILmVv92_QON5bUXoXAKAZ-uSBskPtHK7s9UuYWdMNSlT2Ly_t-Im8RxSqFEyfZ-Xt04uDojzIUJXEVmCCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=NhchV6ae4eP0OH7YOUZbl9OzQBRxmO2QHxLhiT1ip3cc3RLXA1WajgdBsGQICrVSUhXK4ODERHxZ_-FnkJnGtGMrn28lXBuoxYj8qCcV5l3VnJ5cGvC6WyIjPgKLh7F2o7hgpEcbD6iMwSdVz2ZnK6O3vMbb7pYHPYAr1qZJQu0QgYsiq0tjfKosUHnpXA2BAmTp1UtePK02aXaY02etoWe3Kqeg8oNVaRKfyTxnGT5eSrzCzSDDpVkW2MoXc95cwTCILmVv92_QON5bUXoXAKAZ-uSBskPtHK7s9UuYWdMNSlT2Ly_t-Im8RxSqFEyfZ-Xt04uDojzIUJXEVmCCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزرای خارجه و دفاع ترکیه، عربستان و پاکستان همراه با فرماندهان نظامی سه کشور روز یکشنبه نهم شهریور در استانبول اولین نشست پیمان دفاعی خود موسوم به پیمان مکه را برگزار کردند.
عربستان سعودی، پاکستان و ترکیه روز جمعه ۱۶ مرداد این توافق را در شهر مکه امضا کردند.
بر اساس بیانیه سه کشور، حمله مسلحانه به هر یک از آنها به‌منزله حمله به همه اعضا تلقی خواهد شد؛ اصلی که شباهت آشکاری با ماده ۵ پیمان آتلانتیک شمالی، ناتو، دارد.
هاکان فیدان روز شنبه ۱۷ مرداد در گفت‌وگو با خبرگزاری دولتی آناتولی توضیح داد که ائتلاف جدید علیه ایران یا هیچ کشور دیگری شکل نگرفته و هدف از آن، ارائه یک تعهد کلی برای حمایت از امنیت سه کشور عضو است.
روز یکشنبه گزارش‌هایی از احتمال پیوستن هفت کشور عربی دیگر به این پیمان منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78105" target="_blank">📅 16:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eTgVkA_QsA4ddJRXNkSDfZeE5Qoszg1cUAPLfVyX64qZ3ui-LU4aEhkzRzkIvDz2VDiBwy60HsNE6O3BbcDS6kPu-NrLvoB_rSFBAq4XTRbKDDDP_ND5WhJouE79Rh2WfoVPBYVfGwo2Fa5d-YOYx_UhPGXDw5BQRu0lakeMpG6Who-rFO-VyrK3j9krAdIJBcUG6EAbZbmDTA4-R0uvePEdV8v66FUL9odZOdwzUzyjuoeLP7w6cDTCdVLy2pzFjWYtD9wiRm6D3lzEjWjT1X49iX4fNhhc3veSU1BMpYTLYNn-LnYV8zyhn0NnToBjV2Pr-ocVCNncid17VfAu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zwl8BLU1CDVGbYTp6yn--ZXfYK2yT0KY0eXVqTvKXUTvcy--kSlkvjyoNTFHukSDwdSQQeooq8_u17UrYY6iXTtwHXjjj4V1iTE84RDir86IWPa3S4ljjaZTrl9mYhHouFxMhelSdEcfygs0lgye5FWw5ppkXoTU2gy0V1eKjpNOc0kZIMngp9-GUbb98OpQ82w61XuZMgPenzVlW5Z6qPcKRrThOV5YBMkYUhyAKm9vLIp7WR-BoWWF4HSyxPtNADScS4O6SJhM5NMPLrTc0AJ1qPXhE0a61zgpv4zAZQPH1qaDRQf5QsJWGypzwngqjXhePMAYXgotcRZbgtottA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دفاع امارات متحده عربی پیش از ظهر دوشنبه ۹ شهریورماه با صدور بیانیه‌ای گزارش‌ رسانه‌ها مبنی بر هدف قرار گرفتن پایگاه هوایی المنهاد با «موشک» را تکذیب کرد.
ارتش جمهوری اسلامی ایران ساعاتی پیش از حمله «پهپادی» به این پایگاه آمریکا در خاک امارات خبر داده بود.
در بیانیه وزارت دفاع امارات آمده است: «نیروهای مسلح همچنان در آمادگی بالایی برای پاسخ به هرگونه تهدید احتمالی هستند، به گونه‌ای که حاکمیت، امنیت و ثبات امارات متحده عربی را حفظ کند.»
@
VahidOOnLine
پیش‌تر:
روابط عمومی ارتش با انتشار ویدیویی از شلیک پهپادها نوشت که در پاسخ به کشته شدن جمعی از نیروهای سپاه و غیرنظامیان در جریان حمله نیمه‌شب آمریکا به جزیره لارک،  «محل های استقرار بالگردها و نیروهای» در پایگاه المنهاد امارات «با شلیک دهها پهپاد انهدامی، هدف قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78103" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iv5Id5nga5hgYxbYGQPFm-_IjNdNQBEwFzBI27MMO53zuW4kPcU9tkUwPBaw6PQLhLT4sXG-1PXLwzgPlwbsopXfUqgTnG-_bsAXvsc_YHCx-lJhHhbIcniEic7KKEToSNuK9craNOZdtZcwJg_sRc85ALGu8Q1iazjCBQNIwKkMLHk9I-_RZ9AbTzdugdBS5Z-6gS-ROyQdOV96gAEEJiHIRLTiWVCjxBYgM4pA_DXFGKp0UT9W89kLdsfVEpopg3PEN55bU7uDGFAkyMOwgtmakFJWAQH5988w-CKclMttNgNMaF0SCdm4O4q_6LslRLi6ZY21fnsmqaHdhGMBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.
درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی صادر شده بود.»
این در حالی است که به گفته این وکیل دعاوی «هیچ‌گونه ارتباط سازمانی یا ارتباط دیگری، به هیچ نحو، میان موکل و هیچ‌یک از گروه‌های متخاصم وجود نداشته» و پیغمبری تنها در اعتراضات حضور داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78102" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZSetxsTBklyxNkx1hGUL5WO5S0W8n9F9GceF44iwpCVSrWp4UBL3RjFRtuQPR8uVflsduutOJ9lcEaC_FxxeNqa7yA6Lt8DKf1YTKGggOcrS8XSI6jcvVRQYcJNYQN_sOrq6dlXawm30PIgQmw4hEN0FribSMMlcHLAFttMZG9vBB0Rc8UFq3lt7u8Cjc2L74Uo-LwIBtSHlouEEdI0QjGjNlvx7mC3V87tFmXu4KcbNJ4fOk84PrLKcaNWh36w2gREOIlIM75E3ScsGy9FIIJYHNmjOMERLDpUg_qyoZZep7JfrfpqisGTvtEK5nZJRl9s21UHuVohxp65VN1V-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز دوشنبه در بیانیه‌ای که از تلویزیون حکومتی در جمهوری اسلامی منتشر شد از برخورد یک نفتکش غول‌پیکر با دو مین دریایی در تنگه هرمز خبر داد و گفت این نفتکش آتش گرفته و کاملا متوقف شده است.
سپاه در بیانیه‌اش مدعی شد که این نفتکش قصد داشته «به طور غیرقانونی» از بخش جنوبی تنگه هرمز عبور کند.
در پی جنگ آمریکا و اسرائیل با ایران، سپاه مدعی است که عبور کشتی‌ها از بخش جنوبی تنگه هرمز یعنی نزدیک به سواحل عمان غیرقانونی است. این ادعای ایران با قوانین بین‌المللی همخوانی ندارد.
در بیانیه نیروی دریایی سپاه به نام نفتکش و خدمه و مالکیت آن و زمان وقوع حادثه برای آن اشاره‌ای نشده است.
این نهاد نظامی به سایر کشتی‌های نظامی هم هشدار داده است که در صورت پیروی نکردن از «مقررات امنیتی» تنگه هرمز، «سرنوشتی جز این نخواهند داشت.»
بیانیه سپاه پس از وقوع درگیری‌های نظامی تازه آمریکا و ایران منتشر شده است.
اما تنها گزارشی که از بروز سانحه برای یک کشتی در تنگه هرمز خبر می‌دهد مربوط به ساعت‌ها پیش از حمله آمریکا به لارک است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78101" target="_blank">📅 08:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=LUaoplVOKRZfIOVUHLccD2I0W9aNkfv4BX93vO9dYR6iP9P_kaA6YzLMBfTE8uP--8KSE7zwhViT_hfg5RXBG1I_ndkTpUcbRfFk2vInFLTcCKxFpR8De9_0IVnYM9nbfQge-iqMoFM79rRLfiSiIpkUdaGVT1hSCYa_S9YJZlt5g5OmykTops1dm7JPCLcIxGoY5gSzgweDqsNhr-Jhd-yU2Jrj3p-0-CtG3zMmkNgai1Upq2Oyt2lDi0E-jh_NFbnhnukkYlcxvg0G_-AtxU0sY4BHJe3RvPc2oFnee_7Bg8QvfryJkQytNxGd-kRmbZWLkXjfv0craYyhasa50w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=LUaoplVOKRZfIOVUHLccD2I0W9aNkfv4BX93vO9dYR6iP9P_kaA6YzLMBfTE8uP--8KSE7zwhViT_hfg5RXBG1I_ndkTpUcbRfFk2vInFLTcCKxFpR8De9_0IVnYM9nbfQge-iqMoFM79rRLfiSiIpkUdaGVT1hSCYa_S9YJZlt5g5OmykTops1dm7JPCLcIxGoY5gSzgweDqsNhr-Jhd-yU2Jrj3p-0-CtG3zMmkNgai1Upq2Oyt2lDi0E-jh_NFbnhnukkYlcxvg0G_-AtxU0sY4BHJe3RvPc2oFnee_7Bg8QvfryJkQytNxGd-kRmbZWLkXjfv0craYyhasa50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا
ویدیو
ها
یی
ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.
ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»
این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78100" target="_blank">📅 08:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p95VWEHzWDnQoBURYDgfvxxFYxSPnwGI1SAwFiLALhVCgB_ZjhiJlFS71IvGrwscVpYbDOOSNbqxMTunMqpsKsj6WdaJwxGVe6Z2SuyZiA6tTkUNWhdaf0-9K_rpW9_OFlk2C4l-wMtvfPVZms3rv_dgIJGdP8KJWKgf_jl5ZntlqZ1DwPcAEEH5uoL0cnteCI4IaLOEHxhyg8DhVuZ8IujMGStvPNq8Xo00uvxPDodKkJA1wJ9Ps4RvXy6YGxae4wKE0C3x-XaygAvNCoQBtO4GoWJHXVSVzosGKT12CNf21jz0monKHPF_8zmln4KoF8JVTlRyzSXz4XfYUQbk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین
تصویر دریافتی: اسکرین‌شاتی از وب‌سایت مرکز لرزه‌نگاری کشوری
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78099" target="_blank">📅 07:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لرزش زمین
بنا بر پیام‌های دریافتی از شرق تهران
سلام و درود همين الان زلزله اومد ٢/٣ ثانيه طول كشيد خونه لرزيد پنجره كوبيده شد من لواسان افجه ام ٧/٢٠ صبح
شرق تهران زلزله حس کردیم
تهرانپارس تهران زلزله شدید
چند ثانیه طول کشید
انقدر قابل حس بود ک من از خواب پریدم
زلزله تهران
یه تکون ناگهانی شدید
ادامه هم نداشت
داداش تهران همین الان لرزید
نمیدونم‌زلزله بود یا چیز دیگه
سمت جنوب غرب
تهران زلزله اومد شدیدهم بود ولی کوتاه.
زلزله اومد تهرانپارس لرزید
زلزله خیلی وحشتناک همین الان حکیمیه
سلامم تهرانپارس غربی لرزید
تهران چنددقیقه پیش زمین لرزید و زلزله اومد
زلزله بود؟؟؟
تهران زلزله
خواب بودم از خواب بیدار شدم، حداقل ۴ ریشتر بود
سلام. یه لرزش شدیدی سمت تهرانپارس تهران حس شد.
اقا وحید نارمک شرق تهران زلزله شد بد لرزید الان ساعت هفت پ بیست و سه دقیقه دوشنبه
سلام تهران علم و صنعت حیدر خانی همین الان زلزله
وحید زلزله شرق تهران کوتاه بود ولی سنگین
من سمت پارچینم
لرزش شدید
یا زلزله بود یا موج انفجار
سلام پردیس لرزید چند دقیقه پیش
شرق تهران ساعت ۷:۲۱ دوتا پس لرزه شدید اومد
سلام وحید جان دو دقیقه پیش به وقت تهران من رو زمین خواب بودم ..جوری زیرم لرزید که بیدار شدم مدتش کم بود و شدتش زیاد
آره وحید زلزله اومد سمت شرق تهران خیلی حس شده
سلام، فکر کنم حدود یکی دو ثانیه زلزله اومد تهران
من غربم :) اینکه گفتی شرق هم لرزیده مطمئنم کرد
تهران  الان  زلزله اومد  شدید و کوتاه بود
زمین لرزید الان
مرکز شهر تهران
من سبلان زندگی میکنم.. متوجه شدم
ماهم تو جنوب شرق مشیریه لرزیدیم
بحدی لرزش شدید بود ک ما تهرانپارس شرقی هستیم خواهرم تهرانپارس غربی
همه از خواب پریدن
لرزش شدید
شمال شرق تهران
همه رو از خواب بیدار کرد
شرق تهران.تهرانپارس
پحید اینقدر تکونه زیاد بود که از خواب پریدیم
حدودا ساعت ۷:۱۹ ۷:۲۰
ببین صدا نداشت ولی قشنگگگ خونه لرزید عین زلزله همه پریدیم
سلام من پاسدارانم از لرزیدن خونه از خواب بیدار شدم
لواسان قشنگ لرزید
سلام من جنوب تهرانم منطقه ۱۷ طبقه پنجم زندگی میکنم کاملا لرزش حس شد و تکون خورد
ما نارمکیم خونه ی ما یجور لرزید که من با وحشت از خواب پریدم
😭
سلام وحید شرق تهرانه چیه
من مهرآباد جنوبی سمت یافت آبادم
قشنگ خونه لرزید
تکون خورد
غرب تهرانم احساس شد
سلام ما دماوند هستیم لرزش احساس شد
من یوسف ابادم
ساعت ۷.۲۰ لحظاتی کوتاه زمین لرزید
تهرانپارس چند دقیقه پیش کوتاه لرزید
سلام صبح بخیر ، ۷:۲۰ دقیقه پردیس لرزید
نارمک هستیم در حد دو سه ثانیه زلزله حس شد ولی خیلی ضعیف بود
سلام وحید جان ، من ستارخان هستم و کاملا لرزش رو حس کردم فقط شرق نیست
وحید جان ما هم مرکز تهرانیم این زلزله رو حس کردیم ساعت ۷:۲۰ بود حدودا
سلام ۷:۲۲ سهروردی خونمون قشنگ لرزید یخچال تکون خورد ولی در حد یک ثانیه بود
تا مرکز شهرم ما لرزیدیم
خیلی کوتاه بود ولی بد لرزید
زمین‌لرزه_تهران‌پارس. شدت خیلی زیاد و کل خونه لرزید
سلام من سمت جنوب غربم خونه طوری لرزید که همه بیدار شدیم
سلام وحید جان سمت مشیریه هم لرزید ولی لرزش عجیبی بود شبیه زلزله های سابق نبود
وحید بد لرزید جوری که من همه رو بیدار کردم گفتم زلزله
اینجا نزدیک دانشگاه امام حسین
قشنگ شبیه موج انفجار بود یه تک لرزه
وای خیلی وحشتناک بود خیلی بدجور لرزید هنوز دستام داره میلرزه همه از خواب پریدیم ما شریعتی معلم هستیم
ما میدون شیخ بهایی هستیم
لرزش زمین اینجا هم حس شد
همه مون فهمیدیم در جا زمین لرزید
ساعت ٧:٢٠ صدای مهیب و لرزش زمین در پردیس شنیده. و احساس شد
مردم اومدن بیرون
سلام، من مرکز تهرانم و متوجه لرزش خفیف زمین شدم.
سلام شهرری خونه شدید لرزید ۷و۲۰ دیقه ۵دیقه پیش ما طبقه ۴م فهمیدیم
ما تهرانپارس هستیم دو تا تکان شدید مثل انفجار بود دومی خیلی شدید بود ، زلزله نبود چون لوسترهامون تکان نخورد
نمی‌دونم انفجار بود یا لرزش ولی ساعت ۷:۲۰ کامل سمت نارمک لرزید
جنت آباد هم لرزید و کوتاه بود
زمین لرزه شدید  شرق تهران   تختم  بد تکون  خورد
یک ثانیه بود ولی تکون خورد
منم رو زمین خواب بودم متوجه شدم ما مرزدارانیم
زمین کامل لرزید
سمت ظفرم
ولی لوستر تکون نمیخوره
سلام وحید جان شمال طهران هستیم اینجا هم زلزله رو حس کردیم ولی خیلی ضعیف تر از شرق طهران
سلام ساعت ۷:۲۶ دقیقه سمت میدان خراسون تهران زلزله حس کردیم به حدی بود که خواب بودیم از خواب پریدیم
نارمک خونه لرزید
انگار یه موج از زیرمون رد شد
حرکتش کاملا معلوم بود
من از رسالت (شرق تهران) یه چیزی ضربه ای خیلی شدید حس کردم شبیه زلزله نبود
منم لرزش رو حس کردم کوتاه بود ولی قوی بود
منم پیروزیم ساعتای ۷:۲۰ دیقه شدید لرزید
سلام خونه ما نیرو هوایی هست چند لحظه خیلی کوتاه لرزید ولی خیلی شدت تکان زیاد بود
ما نيرو هوايي هستيم از شدت زمين لرزه از خواب بيدار شدم
من هم لرزش رو حس کردم توی نارمک
دوتا لرزش بود شدتش زیاد بود ولی زمانش کم
فکر کردم از بالا مثلا همسایه محکم پریده روی زمین تا الان اومدم پیام ها رو دیدم
رودهن هم لرزید
سلام وحید من شرقم علم و صنعت
نمیدونم بگم زلزله بود چی بود
انگار بمب افتاد
خونه ما شرق تهرانه(حکیمیه) و حدود ۷:۱۵ برای سه ثانیه لرزید، نمیدونم زلزله بود یا چی ولی هیچ صدایی هم قبلش نیومد،
خواب بودم تختم عین گهواره شد بیدار شدم. اتوبان بابایی تهران
سلام اقا وحید زلرله ساعت ۷ و بیست دقیقه بومهن و لرزوند شدتش زیاد بود
من نارمکم، زلزله اومد، یه تکون شدید خورد قشنگ، از خواب بیدارم کرد
ساعت ۷:۲۰
سلام .تهران . نارمک شمالی. با زلزله از خواب بیدار شدم. تکون و صدای شدید داشت.
سلام زلزله شدید سمت نارمک میز کامل تکون خورد و لوازم لرزیدن از شدتش بیدار شدم
میرداماد هم حس کردم
به حدی که از خواب پریدم
هروی زلزله رو‌حس کردیم ....
و از خواب پریدیممم
۷:۱۹ صبح
پاسداران زلزله درحد تکون خوردن تختم از خواب پریدم/:
از شدت لرزش از خواب پریدم
خیلی عجیب بود
ساعت ۷:۱۵ ، نارمک هفت حوض
سلام وحید جان،حکیمیه از شدت زلزله از خواب پریدم هم خودم هم خانوادم!!
فرمانیه هم من کاملا متوجه شدم
ولی بیشتر از لرزه موج شدیدی داشت
سه تا موج پشت هم که قشنگ تو پنجره و دیوار پشت سرم احساسش کردم
ما پاسداران سمت حسین آباد هستیم
قشنگ خونه لرزید
پردیس حدود ساعت ۷،۲۱ لرزید
وحید جان افسریه جنوب شرق تهران لرزش زمین بود که از خواب پریدم
سلام ما شیان هستیم خیلی بد لرزید
به خانواده ام گفتن باور نکردن تا کانال شما رو چک کردم فهمید درست بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78098" target="_blank">📅 07:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✅
واقعیت: نیروهای آمریکایی اقدامی محدود و دقیق علیه نیروهای مین‌گذار سپاه پاسداران که تهدیدی قریب‌الوقوع در تنگه هرمز ایجاد کرده بودند، انجام دادند. در اصل، ایران این تهدید را ایجاد کرد و ارتش آمریکا برای حفاظت از دریانوردان غیرنظامی، کشتیرانی تجاری و جریان آزاد تجارت جهانی، آن را از میان برد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78097" target="_blank">📅 05:23 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
