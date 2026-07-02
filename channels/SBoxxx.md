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
<img src="https://cdn4.telesco.pe/file/NlV7tWPI4i7UtYqfvRK39N94SiKNNSvme42seUSfgtjMQhMnepg9V9onJQO4ILfpOFCsoI-z2IU7Ytvk1K4SSsb7NrKW5EPZ9_GcBroi8-brhzG4uTueyrjxcM0si5__XFnOcIBcMobVAMDrzj5XFNnnrNuwtZ-GkN53f-gXellLuq82tqcrTY407sEHNPhIQ-bOydzSG7MaI1HHHMns868Ju-7_2jxR8E_LxXUSaqRXc-7nrqGq72FlVE7T0fHFKQBS3NbSXqhdr493ec38N7zL2HErykkyIMR3_BWv-EzMvH7E_WNsoETdFi-_jZZcwaPs1PG7g_oyofWsiD67-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 03:26:36</div>
<hr>

<div class="tg-post" id="msg-18177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید
همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای انتحاری و سامانه‌های شناسایی گرفته تا تولید مشترک برخی تجهیزات نظامی در خاک مراکش، شواهد نشان می‌دهد که تل‌آویو در حال سرمایه‌گذاری بلندمدت بر ارتقای توان نظامی رباط است.
این تحول زمانی اهمیت بیشتری پیدا می‌کند که در کنار سردی بی‌سابقه روابط اسرائیل و دولت چپ‌گرای اسپانیا قرار گیرد. دولت مادرید در دو سال گذشته از منتقدان جدی سیاست‌های اسرائیل در غزه بوده، از به رسمیت شناختن کشور فلسطین حمایت کرده و در مجامع بین‌المللی مواضعی اتخاذ کرده که با مخالفت شدید تل‌آویو روبه‌رو شده است. (لینک ها:
یک
|
دو
|
سه
) طبیعی است که این تنش سیاسی، بر محاسبات راهبردی اسرائیل نیز تأثیر بگذارد.
در چنین فضایی، افزایش توان نظامی مراکش پیامدهایی فراتر از شمال آفریقا دارد. مراکش همچنان ادعای حاکمیت بر سئوتا، ملیله و چند قلمرو اسپانیا در سواحل آفریقا را حفظ کرده است. هرچند رباط بارها تأکید کرده که این موضوع را از مسیرهای سیاسی دنبال می‌کند، اما از نگاه بسیاری از ناظران اسپانیایی، تجهیز ارتش مراکش با فناوری‌های پیشرفته اسرائیلی، موازنه قوا در غرب مدیترانه را به زیان اسپانیا تغییر می‌دهد. پرسش نمایندگان حزب راست گرای Vox ووکس در پارلمان اسپانیا درباره آمادگی این کشور در برابر پهپادهای انتحاری ساخت مشترک اسرائیل و مراکش نیز بازتاب همین نگرانی است.
سیاست بین‌الملل، برداشت بازیگران نیز به اندازه نیت آنها اهمیت دارد. حتی اگر انگیزه اصلی اسرائیل اقتصادی یا ژئوپلیتیکی باشد، نتیجه عملی آن افزایش فشار امنیتی بر کشوری است که در سال‌های اخیر یکی از منتقدان اصلی سیاست‌های تل‌آویو در اروپا بوده است. از این منظر، تسلیح مراکش را می‌توان نه لزوماً «مجازات» اسپانیا، بلکه پیامی راهبردی در راستای بازآرایی موازنه قدرت در غرب مدیترانه دانست؛ بازآرایی‌ای که به‌طور طبیعی هزینه‌های راهبردی بیشتری را بر مادرید تحمیل می‌کند و می‌تواند بر محاسبات آینده دولت اسپانیا در قبال اسرائیل نیز اثرگذار باشد.</div>
<div class="tg-footer">👁️ 905 · <a href="https://t.me/SBoxxx/18177" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18176">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=lQLHcWBgvxux-KYPaXrgRaRioe6VBxoNtSVLyAqOb1R3DzPXN9Xc9Ojet5_kSufHkllEGBdJEABTNJ781iuYEUdAayRTKIgobmVaZKSTRL79En52d6VjnaMqNYMybvIbsNm-_a8L4sC08P_pl-xHzoAEDaFMZ7ivN5eapWOgT0TB85LzgvKCIE31qV8Yif5xvdJAmd-_jeFP-PPONIvO9xY6h0ZjOUx1xUA3ULA9mMGYDr8DRx7OEH7JIuvdmeNPCkZN_FJDTWlSa4AZ5pSPfoTJsXCa7niBEVE7LoSFMdR7DTSrAu-k2_keDZgkWGDqjNc_QQLYBBJPny6Zm3fTGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=lQLHcWBgvxux-KYPaXrgRaRioe6VBxoNtSVLyAqOb1R3DzPXN9Xc9Ojet5_kSufHkllEGBdJEABTNJ781iuYEUdAayRTKIgobmVaZKSTRL79En52d6VjnaMqNYMybvIbsNm-_a8L4sC08P_pl-xHzoAEDaFMZ7ivN5eapWOgT0TB85LzgvKCIE31qV8Yif5xvdJAmd-_jeFP-PPONIvO9xY6h0ZjOUx1xUA3ULA9mMGYDr8DRx7OEH7JIuvdmeNPCkZN_FJDTWlSa4AZ5pSPfoTJsXCa7niBEVE7LoSFMdR7DTSrAu-k2_keDZgkWGDqjNc_QQLYBBJPny6Zm3fTGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.  ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SBoxxx/18176" target="_blank">📅 01:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18175">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ:
ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/18175" target="_blank">📅 01:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18174">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.
با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را دوباره شعله‌ور کند، واشنگتن از کشورهای منطقه خواست تا ایران را از این خطر آگاه کنند.
ایران اقدامات امنیتی گسترده‌ای برای محافظت از هیئت خود انجام داد، از جمله اسکورت نظامی و تغییر برنامه‌های سفر پس از دریافت اطلاعاتی درباره احتمال حمله اسرائیلی.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/18174" target="_blank">📅 22:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18173">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-poll">
<h4>📊 در‌ جنگ میان ترکیه و اسراییل دوست دارید:</h4>
<ul>
<li>✓ پیروزی ترکیه</li>
<li>✓ پیروزی اسراییل</li>
<li>✓ جنگ فرسایشی بدون برنده</li>
<li>✓ من Gay هستم و دوست دارم جنگ نشود</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/18173" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18172">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/18172" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18171">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر امور خارجه ترکیه، هاکان فیدان:
سیاستمداران آمریکایی تا زمانی که حمایت از اسرائیل به منافع خودشان خدمت کند، از اسرائیل حمایت می‌کنند.
این پویایی آن‌قدر طولانی شده است که همسویی بین حمایت از اسرائیل و پیشبرد منافع ایالات متحده به عنوان یک فرض دائمی تلقی شده است.
با این حال، برای اولین بار از زمان نسل‌کشی در غزه، تحلیل‌هایی که ظهور کرده‌اند به نتیجه متفاوتی اشاره دارند: «سیستم موجود در حال کار علیه منافع ماست.»
هیچ‌کس ادامه سیستمی را نمی‌خواهد که در نهایت علیه منافع خودشان کار می‌کند.
در سراسر جهان، از دانشگاه‌ها تا روزنامه‌ها، احساسات ضد اسرائیلی به‌طور چشمگیری افزایش یافته است.
چرا؟ زیرا مردم می‌بینند که اسرائیل آشکارا در حال ارتکاب کشتار است و در هر جایی که اقدام می‌کند، نقش بی‌ثبات‌کننده‌ای ایفا می‌کند.
در گذشته، آن‌ها می‌توانستند این موضوع را با چند مانور رسانه‌ای ساده پنهان کنند. اکنون، دیگر نمی‌توانند آن را پنهان نگه دارند.
اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
تا زمانی که اسرائیل — یا هر بازیگر دیگری — به روش‌هایی عمل کند که با منافع ملی و منطقه‌ای ما در تضاد است، ما هیچ دلیلی برای ترسیدن، مردد شدن یا عقب‌نشینی نداریم.
ما مشکلی با رویارویی نداریم. اگر به آنجا برسد، برای ما مسئله‌ای نیست.
اسرائیل فقط مشکل من نیست؛ مشکل جهان است.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18171" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18170">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر دفاع اسرائیل:
ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/18170" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18169">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عبدالمجید حکیم الهی، نماینده رهبر ایران در هند، گفت که به دلیل نگرانی‌های امنیتی، بعید است آیت الله مجتبی خامنه‌ای در مراسم تشییع جنازه پدرش شرکت کند.
وی افزود که آیت الله مجتبی خامنه‌ای مایل بود نماز میت را اقامه کند، اما مقامات امنیتی این کار را بسیار خطرناک دانسته‌اند.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18169" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18168">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تولید نفت خام کویت در ژوئن به طور میانگین ۱.۶۵ میلیون بشکه در روز بود در مقابل ۵۷۸,۰۰۰ بشکه در روز در ماه مه</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18168" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🩵
کاتز ؛ وزیردفاع دولت اسرائیل
:
ما درحال توسعه لیزرهای فضایی برای تهاجم خارج از جو زمین هستیم
يسرائيل كاتز ،  اعلام کرد دولت اسرائیل در حال توسعه لیزرهای فضایی به منظور توانایی حمله در فضا است.
به گزارش اورشلیم ،پست کاتز در نشستی با خبرنگاران نظامی گفت: یکی از اهداف اصلی که نخست وزیر و من تعیین کرده ایم این است که برترین استعدادها را جذب کنیم تا امروز هیچ کشوری توانایی اجرای حمله در فضا را نداشته است. ما باید در برخورداری از این توانایی کشور پیشرو جهان باشیم
او افزود: اگر به این هدف دست یابیم این امر میتواند برتری بازدارندگی، توانایی حمله و انهدام و دیگر برتری های راهبردی ما را در برابر دشمنانی که از منابع گسترده برخوردارند تضمین کند
کاتز پنجشنبه گذشته گفته بود اسرائیل مصمم است به بازیگر پیشرو در زمینه توانایی حمله از فضا تبدیل شود با این حال این نخستین بار بود که به طور مشخص از لیزرهای فضایی نام می برد
اسرائیل هم اکنون نیز در این حوزه از کشورهای پیشرو به شمار میرود و سامانه موسوم به پرتو آهنین (Iron Beam) را به عنوان یک لیزر فضایی مستقر در زمین تولید کرده است
سامانه پرتو آهنین که اواخر سال گذشته به ارتش اسرائیل تحویل داده شد نقطه عطفی تاریخی به شمار میرود زیرا نخستین سامانه دفاع لیزری عملیاتی جهان است که میتواند راکتها پهپادها و خمپاره ها را با هزینه ای بسیار کمتر از رهگیرهای سنتی، خنثی کند</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18167" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فرمانده سپاه پاسداران قم
:
تمهیدات زیادی اتخاذ کردیم اما بصورت قطعی نمی‌دانیم در مراسم تشییع رهبرانقلاب چه اتفاقی خواهد افتاد</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18166" target="_blank">📅 15:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه (۱۶ روز دیگر) آغاز می‌شود.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18165" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
غضنفری ؛ نماینده مجلس
:
یک شبه کودتای سیاسی علیه رهبری نظام درجریان است - تجمعات شبانه نباید جمع شود</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18164" target="_blank">📅 13:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دلار ۱۷۷۰۰۰ تومان!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18163" target="_blank">📅 11:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTPMuDoY3dZihaDJ1hSD0HOmClQQ7sHNz68BuNIWyJr-ieAtHLrmr-XzUzzhmo4TP-Zvnf8ytf1IK8JOABpJiKEa58PpxQ6ePub_gPx2ypy-mBI21C46TGzB4d024QNanc0CZkUpdEmL7Zp8q1IdmbOuAutziTkilU5BE7eJsb5aSpnpV-rKdVEYjkXeMhoFZ3ZZyyxTgh-MulzZYJS8_dMYNpzWL60TRdK8QhgKqmsJdHeDMr9qlHHQykEUooICdckT0iLqaO_Lc3gkSUkdEtHW_q8Arw7GzIcjO4UGTGPLyQNBx-sdH3Uopmal56fDZOfHkyViNBUSL-Y28nGiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی برای امروز در سطح بالایی قرار دارد.
توصیه می شود با توجه به انتشار گزارش NFP، امروز با کمترین حجم معامله کنید.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18162" target="_blank">📅 09:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جهش انفجاری معاملات شخصی ترامپ در سه ماهه نخست ۲۰۲۶!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18161" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18160" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آمریکا رسماً توافق‌نامه‌ای برای ساخت سفارت دائمی در اورشلیم امضا کرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18159" target="_blank">📅 00:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سقوط بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده در دریای عرب
ناوگان پنجم ایالات متحده اعلام کرد که یک بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده که به ناو هواپیمابر USS George H.W. Bush اختصاص داده شده بود، اوایل روز چهارشنبه در دریای عرب فرود اضطراری انجام داد.
سه نفر از چهار خدمه در وضعیت پایداری پیدا شده‌اند. جستجو برای یافتن نفر چهارم در حال انجام است.
ناوگان پنجم اعلام کرد که هیچ نشانه‌ای مبنی بر اینکه این وضعیت اضطراری ناشی از اقدام خصمانه بوده باشد، وجود ندارد و علت آن در دست بررسی است.
این دومین سقوط بالگرد نظامی ایالات متحده در منطقه در هفته‌های اخیر است.
یک بالگرد AH-64 آپاچی ارتش در 9 ژوئن در خلیج عمان سقوط کرده بود که ترامپ گفت که نیروهای ایرانی آن را سرنگون کردند و خدمه توسط یک قایق بدون سرنشین Corsair نجات یافتند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18158" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:  چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.  چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18157" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:
چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.
چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18156" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">موجودی نفت خام آمریکا در ذخایر استراتژیک نفت (SPR) در هفته گذشته به پایین‌ترین حد از ماه مه ۱۹۸۳ رسید - EIA|</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18155" target="_blank">📅 18:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18154" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRk0vEgL23KG98-xxvt08oTPQZKiJyGc3I4LLnAFfZnf9YwEu6KDlzVQpSq-gZB16Y5nsCkZ_ytr_eewuET0b6yGvxfRRmzf8CdDZfjOip31xxYoB_9-HRepUR3IQNrWxzEYyl9z1-opNDS3ThUd1LK6P1urCKMPAx0lTPnMV1MTMpFUgwbIB5QBsvxVHylgeoW5NxkFy3uxDccdTE40vmQPlT4a6OjnCEtg8L2gpHL_3F5iS0F7sGbOFi1t2fW45StBBodDfwYxfSy8ZNvY7DRZ3bjrc5tX0oxyFeGLzeXCiRmazmwg4aLvOavB-pP7vOd0e0JjUHYWZYFkSkgqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سومین روز متوالی ، امانوئل مکرون با عینک آفتابی دیده شده است.
به نظرتان کار آن عفریته زنش است یا صبیه وجیهه رفیق بهزاد؟!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18153" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گفته می‌شود با اجرایی شدن این توافق، قیمت چص فیل در سرزمینمان بزودی ۹۰ درصد سقوط می کند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18152" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به گزارش العربیه، آمریکا و ایران به توافق اولیه برای آزادسازی ۳ میلیارد دلار از دارایی‌های مسدود شده ایران دست یافتند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18151" target="_blank">📅 15:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18150" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKH-sKXr39wewKVoXEySODiIq7nno4vRh2D-dgMLcmsy6JRDxmlKN55yncg_54TAVFMaFn9MDVtbDFjHed26z0OgMiMEFNG3DF8aaovxXrJq1aU7bEM2zuqy2f8rN5XjprRbjzlT1QJwi1Hqq5z2GgUb6u7QMFZDk-DqEoR8CL9gdyYPD_pPj8GXNhB9R-4wH_znTpe7-E13zy2NYVdCN784jDTnsuHy0KztzhiBMw5KnXqtMVIro4YP0IATagz0i24wI5Cx8xiuq9iq8dcpKnME7PEhZ2qRAJ_Bz129tcgoTeArjYFe8f9IN4HEOpntMuj90KDuY3KOJ5uFGmHaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد دارایی های ریسکی و افت بهای نفت!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18149" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7aWBmgjq0SMdN45S-XeLb2ldiH5zc0pVQognD3lBKqo8JjxHUhv9q8NgrpX5567PrOdVFCbqOedY997OCQwLLusljB2TaNjVSXUioXq2WcDOwOzqvZAkIwCyy1FUGczQhWdXR9enkLLdmyga_93HvHAly9b5OECPJfq-9vHL7FEvJcKN94159GNHspd01WFB1ZhuHpcWC6a1mZxkbWpQ_0sKNMKoO2x5ee0-uEhq3bJQ7XcXg9l3gkBVujmEun19KJhtRX6XDORIYbhZOq6XdHxfrnZo6zbGQCTfnUOAqa8EHHZ8UXePUCA0GgFDK8NvSmXN3PZs6hrQRFTb-Rw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18148" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی در پاسخ به تهدید کاتز برای ترور رهبر جدید ایران:
شرایط تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است.
رئیس‌جمهور آمریکا متعهد شده است که حیوانات خانگی خود را در تل‌آویو ساکت نگه دارد. اگر آنها به ارباب خود توجه نکنند، ایران به آنها درس خواهد داد.
هر تهدیدی علیه مردم و رهبری ما پاسخ فوری و قدرتمندی دریافت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18147" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=Ky_3A4ZTX5nHs9vqrfTfildbXlhX_PFDWIk73CkSpWM7E0DXSlpxVNKcbT2u_vUWWsaym0n1sL0T9Aer9bmetJvIQasZLX7kRoOIbkciHpbcBOpC-jN8nbBTeCZPW9VKFUwBkk6kvrI378-PC6qmvdwZVM8LkOzGC0FfeRx9dTfrTD36sDQB4M3O288TfsVQKNQVl-AAewSL6nkGMWFgsPdzWbxYRuq9yZW9d5xNbt0QPzLHqDV_Cq5C4vBEe7Z6BGVpnSr4G0Bjth1caKaaPjtEMhJTUjElyEl5m9U0iTOHVri7cDCpIhGHz4pdczIzzqiWi8cp6HF1PNxspf6i2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=Ky_3A4ZTX5nHs9vqrfTfildbXlhX_PFDWIk73CkSpWM7E0DXSlpxVNKcbT2u_vUWWsaym0n1sL0T9Aer9bmetJvIQasZLX7kRoOIbkciHpbcBOpC-jN8nbBTeCZPW9VKFUwBkk6kvrI378-PC6qmvdwZVM8LkOzGC0FfeRx9dTfrTD36sDQB4M3O288TfsVQKNQVl-AAewSL6nkGMWFgsPdzWbxYRuq9yZW9d5xNbt0QPzLHqDV_Cq5C4vBEe7Z6BGVpnSr4G0Bjth1caKaaPjtEMhJTUjElyEl5m9U0iTOHVri7cDCpIhGHz4pdczIzzqiWi8cp6HF1PNxspf6i2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18146" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محبوبیت فردریش مرز  به پایین‌ترین میزان خود رسیده است!  بنا بر گزارش بیلد و با استناد به داده‌های مؤسسه تحقیقاتی INSA، حدود دو سوم آلمانی‌ها از عملکرد صدر اعظم فریدریش مرز ناراضی هستند.  این رسانه اضافه می‌کند که حدود ۷۰٪ از شهروندان آلمان از عملکرد دولت ناراضی‌اند.…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18145" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💳
اعتراض عضو فقهای شورای نگهبان به بازشدن اینترنت بین‌الملل
🔹
مدرسی یزدی
:
باز گذاشتن شبکهٔ جهانی اینترنت بدون ملاحظات کارشناسی دقیق از جانب متخصّصان متعهّد، به انواع بهانه‌هایی که نمی‌تواند جبران‌کنندهٔ آسیب‌های همراه آن باشد ـ از قبیل آنکه کسب مردم آسیب می‌بیند یا حقّ مردم است یا خلاف وعدهٔ انتخاباتی رئیس‌جمهور محترم است ـ کاری بسیار خطرناک است. این کار، اقتصاد کشور، امنیّت شغلی مردم، امنیّت داد‌و‌ستد‌های تجاری، امنیّت نهاد‌های مهمّ کشوری و امنیّت شخصیّت‌های مؤثّر نظام و سلامت روانی اقشار مختلف مردم به‌ویژه نوجوانان و جوانان را در تیررس دشمن آمریکایی صهیونی قرار می‌دهد</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18144" target="_blank">📅 13:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xkej4EoSAhMTEiRmfYF3fvv3NT8NlTF2r3q4UWz_iGb_HPI56afjEzrBLh0jfMW2KOLTkFhnAoDat-hcru4ijRLDghJh6F7PeKMcTXWtVmhN74w_IYG6cWC15wXhy09u-wBAxEgAo8HXEFzzZip0MFAVqVrZ5K8u7_0RhZDRBeSDxKTqyPBSLhNvsFzMq6cH-r4b4wht7Rgod-MuQN61WtW3Xvg-WkDsOiliBgWGZjXTwG2mIQLT7Y3JIaQk_idpQos6ksf7T_X7qO9VT6MWHyNU7P2DSTypvws7wErHJWIXH7OFi-zJwV_T-LAqLgM7zEWNE_WWwC7K-jGnnHVPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18142" target="_blank">📅 12:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18141" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Secret Box
pinned «
🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/18140" target="_blank">📅 11:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه
ژئوپولیتیک و بازارهای مالی
ارائه خواهدشد.
یک
شاخص ریسک ژئوپولیتیکی
هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18139" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEaeKwyWZIsAc-xxehFGAUdVuyQXQscIg4ZMlPBoNk4OrLgnsz_Eh5LzCg56zeYjSF-s3qaG0hFw6rBEfDY-jcGA3Q716Fpn8P9HnjwiR8x6JjlPCfZjCd9AhowVS7gkdgeW7JWGZWUyFqrJDpGhahrOK-QqjaVu7EfwzXGgdSFXPohDuZuKHM2bAWMJtrB_Cj6wvnCr-B38aIVPscV-QsBFHu88owFtEfb7EvBGaJjV-WkPWTzNb_YPdjdQ96LbWUUaElJv1nlk3qYqgb5-mp34g3PNh32j65YOF3JVH5Awy-vGCHEWGpNwlyieZJFifcI9Y6694eeztyGivEWVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات جدید قاسمیان:   واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18138" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اظهارات جدید قاسمیان:
واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18137" target="_blank">📅 10:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLa1FbsrBkomnbsQ4v851SswGPjfQeN7C3V5rU2B3JlbTitHZby301Jm847dBaYKFuQJA-Qfk4Tznki_BYNnbNzsP52AnkEPZ85xWlxaB3K_RHXga7nPv75zyNhRowC9c3R9bCRNjGs3wPJEN_ILmLXlHYABwcKVtk1P-0AFeQtiIso4--9sUdD3YADTpk5tNMLJP1fIJeg33d2p0qT2xWoAJvtK45Wx3GfddMJnd5SBgVd2NPQkDPTaLYopz7JQli6TTfdKQCX4DNpTbMOCu3J2dZMgvh_PKgb2UdTzYk-TIcdiRnScuCO1MNGAUmG7AxpEZs97ohuVpFDGS4Uevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18136" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7cmYCZjDxlPm0uoFgLKd-R8i0xsurxexq0juuXMmlC0h_o35xkEIf95RcdCfxU7u0yRS4qZPcuDGMUWvXEmnYFonw-ZMvobOSxkLRhUWAmppEQQgSz_l8-1Ena7LMwH-Anj9UHzEAS1DMjtPYFCvjtqlAwoVZLt6oU3d3bLE0k_BXj1vPSP_EXBYl8v1wk-PRF3dH4S0k1NGjgEnc2lSpm-A67SMTYP-AO24A-cSnxzApTSdLBCQhr3DPj9nlc3erQF8tfQPlSQBLDW9zacATGpPpPXy1OqxBXs5vGGot-pI4t-e374DHCsVJbUWI_8kjhXBV5DXXNQkcxyNObEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد دو ناو آبی‌ـ‌خاکی آمریکا، باکسر و پورتلند، در حال حرکت به سمت خاورمیانه هستند.
این دو ناو معمولا برای انتقال نیرو و عملیات آبی خاکی و ... مورد استفاده قرار می‌گیرند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18135" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فراخوان‌هایی برای اسکان مجدد در غزه پس از مصاحبه نتانیاهو
بنیامین نتانیاهو در مصاحبه‌ای با «پاتریوت‌ها»، بازگشت به اسکان یهودیان در غزه را رد نکرد، که این موضوع باعث شد قانون‌گذاران برای تبدیل این چشم‌انداز به واقعیت و اصلاح «ظلم تاریخی» جدایی سال ۲۰۰۵ فراخوان دهند.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18134" target="_blank">📅 09:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18133" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=NZfg5FncE85TEzfQt76HMWgSYVROu8wORJrdTRxNaNHCrP4oRtrLPLGyRguRBI9vNMG_0dUL_uB_cVvqXLo5aiZZAPE_QMJo3YfrUsZ6kB7KHa1XUpiJO_h-RaYJGLlioPBA75UFHoHP1UJOk1nK2rG7mmOoODxi48Imn2WC-Fs4tKLwHLtmKMzdMwzX9A-KHo6jD6GKj2JE6ocBymxG_Qou483fCg0D00TPpSosehcfPIV48WN1DwEv4IvHEUBufG2qGBVbXPmmdoI7aEUEnuHl-6O5KPBHjrO_NFQg_BZ_VHV3X9Kk_L365V2TaCuUfOj_KnLIIxWK9KXgxAIggA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=NZfg5FncE85TEzfQt76HMWgSYVROu8wORJrdTRxNaNHCrP4oRtrLPLGyRguRBI9vNMG_0dUL_uB_cVvqXLo5aiZZAPE_QMJo3YfrUsZ6kB7KHa1XUpiJO_h-RaYJGLlioPBA75UFHoHP1UJOk1nK2rG7mmOoODxi48Imn2WC-Fs4tKLwHLtmKMzdMwzX9A-KHo6jD6GKj2JE6ocBymxG_Qou483fCg0D00TPpSosehcfPIV48WN1DwEv4IvHEUBufG2qGBVbXPmmdoI7aEUEnuHl-6O5KPBHjrO_NFQg_BZ_VHV3X9Kk_L365V2TaCuUfOj_KnLIIxWK9KXgxAIggA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد خوش چشم:
«یک چیزی از آقای حاجی زاده بگویم که احدالناسی نمیداند جز خانواده اش
که آنها هم به من نگفتند!»</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/18132" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جِی‌دی ونس درباره ایران:  یکی از چیزهایی که درباره ایرانی‌ها برایم هم جذاب است و هم ناامیدکننده، این است که آن‌ها می‌گویند «نه، نه، نه، هیچ گفت‌وگوی صلحی در جریان نیست»، اما گفت‌وگوهای فنی بین ایالات متحده و ایران درباره توافق صلح در حال انجام است.  این یک…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18131" target="_blank">📅 23:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18130" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قالیباف رئیس مجلس ایران:
تحریم‌های نفتی برداشته شده و ما نفت را ۲۰ درصد گران‌تر می‌فروشیم</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18129" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=Oxz7DuXOj_msp3eRO7EnE1sw3o29azYVmN5BdPuObQLMtiUksFUypFqCWqWwr7r76sCLpEOTBDpv0NliePhaLEQEeSguw6kVAIGmwIkSpwGlFtJ8sWZViylI7UwE56Jj1B7IrszuGyuttE34mn5Ivrf6vDiUQxIWSPMKCfjiEJuBTV1GxdA8QoqYp49XGTFUTSsOf1uzOBewnCM8GkNcpv4auTIMQ0SKStIvyMBxubonQ9lasqwlnkqutmjD_EJ6_tVAaSSLg9ibhC0GDw6w4bC7SK3wpyn6zXwU0Z6d4wu5t99qCRZBebkRnCx3e5ajKXLKtcItaoEtjhGwf-8diphSdUCNdAZXRXjv9gxb6yb9n8cjkvc_ADDH--dGOkbzdK79RLjM6EiIimPxmTsXAKj0ael2vD5t49FxqcGaXRj2i00M8tNm8N3f2umSKFFfIOFW4YFU2Gs2bFMc9KIzmT2yAO0NWA40u5OSTHJ1SqwO8JKH8nyEfu7BN-VIfZwMpV6e4s768MTTYoJfLhCXutVii7_LI8lPKvrvwO4dO-PxoSnwZu6vgXA8coBpxrAT7gXwhDYaDRFeZYp5bMrX_I4rCMjVgtxl9Uxt-f0AK_Tq5oNayxe3LzPQeDQikss6bLtbsn4GlKaKK5Oin4_k0h6qcI7U9sQ4_yp7iYk6PcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=Oxz7DuXOj_msp3eRO7EnE1sw3o29azYVmN5BdPuObQLMtiUksFUypFqCWqWwr7r76sCLpEOTBDpv0NliePhaLEQEeSguw6kVAIGmwIkSpwGlFtJ8sWZViylI7UwE56Jj1B7IrszuGyuttE34mn5Ivrf6vDiUQxIWSPMKCfjiEJuBTV1GxdA8QoqYp49XGTFUTSsOf1uzOBewnCM8GkNcpv4auTIMQ0SKStIvyMBxubonQ9lasqwlnkqutmjD_EJ6_tVAaSSLg9ibhC0GDw6w4bC7SK3wpyn6zXwU0Z6d4wu5t99qCRZBebkRnCx3e5ajKXLKtcItaoEtjhGwf-8diphSdUCNdAZXRXjv9gxb6yb9n8cjkvc_ADDH--dGOkbzdK79RLjM6EiIimPxmTsXAKj0ael2vD5t49FxqcGaXRj2i00M8tNm8N3f2umSKFFfIOFW4YFU2Gs2bFMc9KIzmT2yAO0NWA40u5OSTHJ1SqwO8JKH8nyEfu7BN-VIfZwMpV6e4s768MTTYoJfLhCXutVii7_LI8lPKvrvwO4dO-PxoSnwZu6vgXA8coBpxrAT7gXwhDYaDRFeZYp5bMrX_I4rCMjVgtxl9Uxt-f0AK_Tq5oNayxe3LzPQeDQikss6bLtbsn4GlKaKK5Oin4_k0h6qcI7U9sQ4_yp7iYk6PcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیریت Secret Box حدود ۲ سال پیش این ایده را مطرح کرد که این روانی عوضی را در قالب یک معامله بکشند که هم برای ایران خوب بود و هم برای اسراییل و اتفاقا ۴ ماه بعد این فراخوان لبیک گفته شد اما سوگمندانه ناموفق بود!  مردک حمال یک دیوانه کامل است و می‌توان او را…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18128" target="_blank">📅 20:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال استریت ژورنال:
اولویت‌های متضاد ایران مذاکرات صلح آمریکا را به خطر می‌اندازد</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18127" target="_blank">📅 20:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!
از این جهت خیلی شبیه احمدی نژاد است؛
منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18126" target="_blank">📅 18:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اسپوتینک:  اختلاف با عربستان، جنگ ایران و تله هرمز عواملی که ممکن است امارات متحده عربی را به سمت خروج از اوپک سوق داده باشد  دکتر ممدوح جی. سلامه، اقتصاددان پیشکسوت نفت، به اسپوتنیک گفت: «مدت‌ها قبل از جنگ ایران، امارات متحده عربی به دلیل اختلاف با عربستان…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18125" target="_blank">📅 18:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بقائی:  ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.  آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18124" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بقائی:
ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.
آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های مسدودشده ایران با طرف‌های قطری است.
بنابراین تأکید می‌کنم که هیچ دیداری با طرف آمریکایی در هیچ سطحی برای روزهای آینده برنامه‌ریزی نشده است
تمامی مقدمات لازم فراهم شده و امیدواریم این روند به‌درستی پیش برود و به نتیجه‌ای رضایت‌بخش برسد
رقص و ابراز شادی مقام‌های آمریکایی از صعود نکردن ایران به مرحله بعد جام جهانی، با همه معیارها و اصول پذیرفته‌شده میزبانی مغایرت دارد
هیچ درخواست رسمی درباره بازگشایی سفارت کانادا دریافت نکرده‌ایم در صورت دریافت درخواست، آن را بررسی خواهیم کرد، اما تاکنون هیچ درخواستی به دست ما نرسیده است.
﻿</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18123" target="_blank">📅 16:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4QQS22P6RbHNUYaj0wyZvGPuYXeIJLUfDoFK6cfydmwQjnxNssRBakOmUgZUOxsC8FLtWI_3EqspgUNYk_SfhFt13ZlI4DFwinshD4cIm2FtKib5LDKofUcOZaOtIKngamdsbGnF2T66log7vhwf58AphqH27ieAkWlc4_LUtLrltWKas1e3Gc0OMvwA5s-NyLyNR0-p4UZ9CIfDHMDmFwDLSw6JjmHTN78fpij9lSUiuUIjceoZCb5svXohZ_QNjnGAlH9rnqTSpEUvaF0HemlZqyAyeT2BkUoWFeoXb7UHgqazj-Yu0R3XTq2lvgRB0ivOo0C41GMli0bUCQW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.  سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18122" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.
سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های مسدود شده ایران هنوز منتقل نشده است و آزادسازی آن‌ها به پیشرفت در مذاکرات بستگی دارد.
او همچنین گفت یک خط تماس کاهش تنش به کنترل تبادل‌های هفته گذشته بین آمریکا و ایران کمک کرده و قطر با عمان هماهنگ می‌کند تا عبور ایمن از تنگه هرمز را تضمین کند، که آن را به عنوان اولویت اصلی توصیف کرد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18121" target="_blank">📅 14:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18120">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.  در این بیانیه، او از اصطلاح "دموکراسی اجتماعی" به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18120" target="_blank">📅 14:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18119">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2alcuk6Tk3RcHXxLS6hft_TMpgLX9WXeBk8CD2HcCE66uuMD2x6yrdK1RNOFeAj4ecasSO-y011Vv98NzDey0DDfRRqMy4p2td7-cy5XLvRjlbNqEMzmBUwq1bFmw9eXn9MBhblHdXG0ta6K6JLOXi8cIhtQOY8Fd5xEOa2_P9jg4JSJDomg16C4FsMRDREDJtWvdALw48x8avxVvnvTeBRgdmtGmAJBW7elSxtwfTzYf__od9pv7VrusFPEUr8o74b4q4R1ao3Imbsd_Z4qHqZIX9ONytjXyeFITrXykvXLt9g5fx4dIrqyPiuLN32SLqC7Q0p16MlaED0CzSsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.
در این بیانیه، او از اصطلاح
"دموکراسی اجتماعی"
به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد این اظهار نظر علیه جریان‌های سیاسی داخل ایالات متحده هدایت شده است.
طبقه‌بندی کمونیسم به عنوان یک تهدید وجودی، حتی از خطرات کلاسیک امنیت ملی در فرهنگ حافظه آمریکایی نیز فراتر می‌رود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18119" target="_blank">📅 14:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18118" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syMihlEg_tyjAfjYgzspQH383QHKGMTwkDlq4tX9Vs3RlWVRhMDl7xyDF2TsSztZf-DSqfyNnKYXVc7z7NEJ3QZRm4p67wl5nsWrZ95_E4t1VH6vqR2x8suXfxOSkFPLcwpH1iYot61iv143Gsz5NMiOmT-vyyQnwmxfE-JxqDdGEkq-xsvmZaVQl5dlLqq-pjg6XSsJUrIpYE-nRjLL3ZAUsavRzzDTh-JWA8_WOi7yBVGBVd_9NCWjSXHTszUNwkmly2NmIMtclPL9Yvm1S5YID_PbEH0uUTTgInPwjamcuRrpxZxxqYX_G2hG1zNwgsk0SYPIptzmLVWZJrvAig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18117" target="_blank">📅 13:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
قنبری ؛ سخنران صداوسیما : ترامپ جنایتکار باید ترور شود تا رهبران ما بتوانند از مخفیگاه خارج شوند که اگر چنین نشود آنها باید تا ابد در مخفیگاه بمانند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18116" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است  یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.  یوسی کارادی،…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18115" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است
یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.
یوسی کارادی، مدیرکل اداره ملی سایبری اسرائیل، به روزنامه آلمانی
دی ولت
گفت که مقامات اسرائیلی در ژوئن ۲۰۲۵ حدود ۱۶۰۰ حادثه سایبری خصمانه را در جریان جنگ علیه ایران ثبت کرده‌اند.
به گفته کارادی، این رقم به طور چشمگیری به حدود ۴۸۰۰ حادثه در ژوئن ۲۰۲۶ افزایش یافته است.
کارادی گفت: «برخی گروه‌ها بسیار ماهر هستند.ما می‌توانیم با آنها مقابله کنیم، اما باید آنها را جدی بگیریم. برخلاف حوزه فیزیکی، در فضای سایبری آتش‌بس وجود ندارد.»
کارادی اظهار داشت که حملات طیف گسترده‌ای از نهادها را هدف قرار داده است، از جمله سیستم‌های زیرساخت حیاتی، سازمان‌های بزرگ، کسب‌وکارهای کوچک و متوسط و شهروندان خصوصی. در میان اهداف کوچک‌تر، شرکت‌های حقوقی و دفاتر حسابداری نیز بودند.
او گفت: «تا کنون — و امیدواریم که اینگونه باقی بماند — ما موفق شده‌ایم حملات به زیرساخت‌های حیاتی را دفع کنیم.»</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18114" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سردار محمد اکبرزاده، معاون سیاسی در دفتر نماینده رهبر ایران در نیروی دریایی سپاه، در یک تصادف رانندگی در استان کرمان کشته شد.
اکبرزاده یکی از معماران کلیدی استراتژی ایران در تنگه هرمز محسوب می‌شد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18113" target="_blank">📅 09:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18112" target="_blank">📅 08:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">غریب‌آبادی :   اگر عمان به هر طریقی تمایلی به ایجاد یک رژیم مشترک برای آینده تنگه هرمز نداشته باشد، جمهوری اسلامی ایران این امر را به تنهایی پیش خواهد برد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18111" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:   ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18110" target="_blank">📅 23:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دکتر محمود سریع‌القلم:  دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.  مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.  اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18109" target="_blank">📅 23:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دکتر محمود سریع‌القلم:
دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18108" target="_blank">📅 23:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFFaZwU6-Wpd1TLqVNEhhnrIrK-7LYRkyFJ7EdMeDogSXwfpK6CZSZRrGTm-WF3fgLykjg-UuPXLT0QWiGHjv8J1_Itg27ng_NVR2g_ev5brOY4Uf7LcSohhEXGFMV-5xJESBQxBhT1MsbZSbKLMbnas3fh3zGGN6GizDOOidlD2UQs2WjPKIeHzxrJWePAmQ8vU2bClas0hm0hLHSmCYczEesX2TyWlMUIBQ0NDmvby2w5-gz12f5DZbppewPJNZWPpO3Mlo5nnMYBq2bBopxUQ4hw_IF9cNUGvMyMyZp6onuvjEmO3V8zH89w56cAHCIQoPl_IrLVP0aa7-GZYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18107" target="_blank">📅 21:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:
ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18106" target="_blank">📅 21:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مکارم شیرازی در دیدار با پزشکیان:
اگر بدخواهان مانع‌تراشی نکنند، توافقات اخیر می‌تواند آثار مثبتی برای کشور داشته باشد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18105" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP2Gegceu3XidqAVPACDs6mszFu4uifAAW22uj3xVujVcB75SwUfBe_r1tzpa-iKLL2rR-pGuVj6XLfA-e_-io4AgK8xXHrRiC_MmSV5ZTJiPcoyaLY0JrWEcPJ3BVoVyrrX6FLn--UMUWrWsKiVSwRImj4Zl9xMOf61b2uC89np1giYr-8298INQeIVaqfEzasRs3IvjytrKIioUNuYnLOM-RKQpSMbyS6BrftpXlsvsz3Pkrd5PRsXpEsgakWLr-pL_gPm0TKYSA5U8AHPYV5odFPQUlinen9LxH3D1IO_EWfSB9VHl-XHD8aNZsKQrK7EudyL1u19ihrOpSyCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18104" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ایران می‌گوید برنامه‌ای برای گفت‌وگوهای مستقیم با ایالات متحده در این هفته وجود ندارد، با وجود ادعاهای مقامات آمریکایی.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18103" target="_blank">📅 19:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18102" target="_blank">📅 19:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18101" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
«من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18100" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18099" target="_blank">📅 19:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:
— حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران
— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی
— توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله
— آماده شدن نیروهای مخالف حوثی ها در یمن برای حمله به انصارالله</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18098" target="_blank">📅 19:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18097" target="_blank">📅 18:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18096" target="_blank">📅 18:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18095" target="_blank">📅 18:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18094" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رستم را به زابلستان بازگردانید!  ترامپ گفت ایران درخواست دیدار حضوری در دوحه داده است!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18093" target="_blank">📅 17:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6Sbip0iazdOdrnTFj05Rg2hNRO6k8ALlgRnzJ3v2S2Yl1GaDAmNVVADSkme9gVgDDyFrmUBmrcbgVgYw7Q8aZH0vRrLkpnOLqOqtqTd5-7ghnycas9hFdMDa3T_EhSrtL23VudJGVOs_YRSciZzIYzJ66ihHVw0K4eXRA2NYTu8KtyJGoFZjj5xEP70kt3vXdE7A1VVTJMGYJdJZZwQ-XHOOPN_bN-ElMjHhOV3TaSBUAGxm-OyuhvMK3oa5UrWBbtDoVe1AB239JQOjewq7z7nFI-F0uzKK_w9KPhtD6Xwit2MNLTo_UAOoxJT09d7otK07S3FTXv5tJ6xwWGO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طنز بانکداری ایران  به دلیل حملات سایبری به دیتابیس بانک مرکزی شما به پولتان دسترسی ندارید ،اما بانک بابت اقساط به پول شما دسترسی دارد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18092" target="_blank">📅 15:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi9ouOuoYCUprUhlmLsU3SbF0XNTgGfXgACG1xxBdPIg4hi8VIqRREPh6fsrClUO_XRdNJEbi3yVfMX4cD3f31iP4Xv12yUpbqbDG6HG3f3VmIbdjmNoIyB69_KlhQuralKzx7dzHd_b_PJXUw3b2KWixNwvycEwN508MNxyQHwuNyG5VOMxTV0k8ZmlrTGmF0MMoCyUq_aW0y5CJmsPzO316A8zu3OzaVaFCTW74bngoHKQ3IjSFvutIByPuTZ_e0mymoVieCaEk-zgAOa0PxHaZCx4hL-2uKUrbXp-ANOSQtkYK4qCfeDKgnoykDnUqOo-JXdJeDOyyqS2KI_NfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینطور که بویش می آید بایستی بزودی رستم تهمتن را دوباره فراخوان کنیم.  فقط فکر کنم عینکی شده باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18091" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18090" target="_blank">📅 14:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXHWESIjsaf1i4K-0tp91gQCQ_yChdEjUsSQVfuY00amc9D0mKTiyTdpKt1KKUK8ntVa6KeLwU8KAWEExD4Z-2C0cBu_eQSImJqNZTP5Yb5cPKyVHYPxWSU37zew9NOo-VW0_zPA9bW6kmJGZrtXRUsXQrgOFhbCc-FoqZ5bcJCqKBCMarUjiivubwBfaBsjZepEGCZC_QYKgrwQr9Oa7gUY4mjyu2ZhhvQHML4t-2ByJ9xV-4nFBFlqd55RYR-jTNW0YbjhNJl1-fV-tADmuGE2zYcLd2PjoOU7rfN_zRzlaSn_ZQ8O9L3bfv0SI9eStuEWA7TFoE__5Y3_Zm9iCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت اسرائیل پهپاد به شهرک نشینان در کرانه باختری اشغالی ارائه می‌دهد!
منابع محلی می‌گویند که پهپادها برای پرواز در ارتفاع پایین بر روی چوپانان و کشاورزان فلسطینی استفاده می‌شوند تا دام‌ها را پراکنده کنند، فلسطینی ها را بترسانند و اطلاعات جمع‌آوری کنند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18089" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18088" target="_blank">📅 13:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18087" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18086" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-uoMV9sFx70PFNnZaglGhsDjBhJ7XSldZfOuQvx1qVcsqzgvR5TgzkHEAHRM0g9jH2iwrxqr9rFT0WnQGBYyN64m9l2QKbL0fOQXS1RyCoAqixGL_QfRCzNLOJmjHXrGE377tmOJtSnFb4H6GRUYryg_8R7GR7i_ps_Kg086_d1yryaZgzaN7irOv7HFqw1cpvR--e2-OJ15QXzw3POIylCcHuFb_7kdeMyZ36clH7oY9KWy3Y2kGG-6YxnFUSwyUXjWFVoV7WQs-VJq66YHiGSr988Kr6DYMSppRgIuNqCT8qgAmhHGaYkexLFvOcDuk7Sd63F6rDygigbqOwPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا رقابت هوش مصنوعی میان آمریکا و چین این‌قدر سروصدا کرده است؟
رقابت هوش مصنوعی آمریکا و چین فقط رقابت فناوری نیست؛ هم‌زمان رقابت بر سر ارزش بازار، سودآوری، امنیت ملی و برتری ژئوپولیتیکی است و هر جهش جدید می‌تواند انتظارات سرمایه‌گذاران و موازنه قدرت جهانی را تغییر دهد.
مدل‌های ارزان و باز چینی در کنار جنگ تراشه و محدودیت‌های صادراتی آمریکا، معادله اقتصادی هوش مصنوعی را تغییر داده‌اند و ابهام درباره فاصله واقعی دو طرف، به مهم‌ترین سوخت این هیاهوی جهانی تبدیل شده است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18085" target="_blank">📅 11:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5vzch0rK-qrALkYyMHZpTUu-z5uimoVZ92hmVb4Z56T1XEU1FVGCXEkbSX79wN1p5xymypy-Ti9z4kjrmwHSluSegGd5FQnykIRu9YdvXKcTYy0xv3ItsT-VdUF_Dw9ZSeROsehLCVNjXGDlorr1YUlIiXVNwnKu_cwCYlwgoj0zpClDo-WAo1d6gyDiAL_eVddTEXyiirfwge4V0p2FIt7nv3tbGks9HNNFro8iQFK6w60hNoHBceLsYIB83a1fo1itKYJcOGLaS-8b2mtacF-iRDIgqtYDSu_AfeYktu9AsjHhkF5pXgdGtOU9oaQ03tf0aKtnwtLbPoUvmL3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عبور کشتی‌ها از تنگه هرمز به طور قابل توجهی با ترافیک سال گذشته متفاوت است.
پورت‌واچ آمار جدیدی درباره ترافیک کشتی‌رانی در تنگه هرمز منتشر کرده است. در ژوئن ۲۰۲۶، ۵۰ نفتکش و ۴۰ کانتینر عبور کردند در حالی که در دسامبر ۲۰۲۵، ۱۱۵۰ نفتکش و ۴۰۰ کانتینر ثبت شده بود.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18084" target="_blank">📅 01:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حمله سنگین اسرائیل به منطقه "مجدل زون" تو جنوب لبنان</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18083" target="_blank">📅 01:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی  ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18082" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه  بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.  برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18081" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه
بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.
برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام این ترور را بر عهده نگرفته‌است
چندی پیش یک عنصر چچن با نام مصطفی الروسی از اعضای نیروی ویژه تحریر الشام موسوم به العصائب الحمراء نیز ترور شده‌بود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18080" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18079" target="_blank">📅 00:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی
ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18078" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزیر علوم و فناوری  اسراییل، گیلا گملیئل:   وقتی که از رژیم ایران عبور کنیم، نوبت به جاه‌طلبی‌های امپراتوری عثمانی می‌رسد که به دنبال گسترش و نفوذ خود است. شکی نیست که ترکیه با آرزوهای گسترش فراتر از مرزهای خود و رهبری منطقه بر اساس دیدگاه خود، تهدید واقعی…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18077" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
