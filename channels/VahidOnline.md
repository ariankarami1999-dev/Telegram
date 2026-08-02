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
<img src="https://cdn1.telesco.pe/file/vhU8vp1rSGrAo8yVbbvsPUf-w7BhxCOpzttFRKNw5iscqavLF6O74NRQI0haedgULLYxJ0too144hyv_pRbu_5-v3My1fPP6N1gDecLP-RaUXWMw8r_ufV4FTwb3w_ui9tr8B9Ad3Ut9Fpn1UziC_cRjpTsm24uIFNSoyfD7CoWqvHz_8CAVq7BkHcb1DnC4ayHmz8lIyXBSYgAntYAzjEr6OfUb4_dxmRVNx22hWzCsaiSyRe_7st3Ke9M-9gDFuXR4vBXGnfiTLXAkeVjDzct5lHhkAdR0tfjATZaTQIaVE0IXVskFw3b1qTpdy4T37UmaFJvOfQM1_QZtUxY3Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 10:57:27</div>
<hr>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XTQW-N4x7FP_bmC7uA-Gg6T61rAWT9Fp6lnoqnkNDNmOTFa7TnRDdwN2jk2AOfP7nYBYfiWS0fEd4RUJwWVox_GlDRjHRwvd9p0vEf45yUvF2XbZR9_yassbbwxsNLwBfFLAtXpHyA2rRC2g8KL2caan3sGfBGET-rZ8-IHS9KbgHhjpRVmEcdd9HGL4EnNs3JvgT71L3T_hGXg7Ft9W9m3skVufTebgN78nB5bE_6jV3WukAcd84a3k7oqXwtv9-8OaoUDj5SW2-gHmR3DX6UFfZXTfiT3CcOCC5mHe0BK7OyhaSbDn1sz0Ms6P2mR-pSwLtpI6q00gv4Jg8svYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به درخواست ایران و کشورهای منطقه، حمله را برای فراهم شدن زمینه توافق، متوقف کردم
ترجمه ماشین:
ایالات متحده کاملاً مسلح و آماده است تا با جمهوری اسلامی ایران مقابله کند؛ با سطحی از رعب نظامی، توان و قدرت که از زمان جنگ جهانی دوم تاکنون دیده نشده است.
با وجود این، ایران و دیگر کشورهای خاورمیانه همین حالا از ما خواسته‌اند که از هرگونه حمله دست نگه داریم، زیرا بر سر چارچوب‌های یک توافق تفاهم حاصل شده است.
این توافق شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
بر اساس این درخواست، برای منافع آینده جهان و همچنین بقای ایرانی موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانیم به‌سرعت به یک توافق دست پیدا کنیم.
کشور اسرائیل نیز در این تعهد با من همراه است.
همه دست‌به‌کار شوید و کار را تمام کنید. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. is locked and loaded and ready to go against the Islamic Republic of Iran, at levels of Military Terror, Strength, and Power not seen since World War II. Despite this, we have just been asked by Iran, and other Middle Eastern Countries, to hold off any attack in that the perimeters of a deal has been agreed to. This would include the Immediate, Complete, and Total OPENING OF THE HORMUZ STRAIT, and an end to Iran’s  nuclear threat. Based on this request, I have agreed, for the future benefit of the WORLD and, likewise, the survival of a successful and prosperous Iran, to cancel the attack, subject to being able to rapidly make a DEAL. The Country of Israel joins me in this commitment. Get to work, everybody, and get it DONE. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77702" target="_blank">📅 05:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HiKbshyHzvJAs57mHRUvRJVndNuCsZ7xaHrLTo8H5GFMZLngocIG0fSAVMgI8NI2oLhDcHNmJQwih4lkCnCyDPjbnbk-QBUhu1s2fVOpZudDufWcQOMFe2L5XKs3VlxeWhu0i78auSaDW-8-UAKYRwnXKP3OizMNDdOVXFpAEAAPRg6ciFY6ezDOxhOd0gqUejoMKJWwhLBg_uHl374GiM3AnIkOdgpn8vuviS5vJNpJ83Oftw3j3kwWV4AigofO5ZnAt-LBTIdf4T9km2-X7zdr0agTIucfx9qnpbZa2Rrhedfo-wwnw4-tuGwWqrSbo8Nxhc1XHc6mdEwvvxt-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان درباره برنامه‌های ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد
اختصاصی
اکسیوس، ترجمه ماشین:
محمد بن سلمان، ولیعهد عربستان سعودی، روز شنبه با دونالد ترامپ، رئیس‌جمهور آمریکا، گفت‌وگو کرد و درباره برنامه‌های او برای حملات گسترده جدید علیه ایران ابراز نگرانی کرد.
این خبر را دو مقام آمریکایی و یک منبع دیگر مطلع از این تماس اعلام کردند.
چرا اهمیت دارد:
ترامپ در واکنش به حمله موشکی ایران به یک پایگاه آمریکا در اردن و ادامه اختلال ایران در کشتیرانی از طریق تنگه هرمز، به‌طور جدی حمله به اهداف انرژی ایران در روزهای آینده را بررسی می‌کند. او هنوز دستور نهایی را صادر نکرده است.
تصویر کلی:
چنین حمله‌ای ممکن است به تشدید بی‌سابقه جنگ پنج‌ماهه منجر شود؛ جنگی که با باز کردن راه مذاکرات از سوی ترامپ بارها متوقف شده، اما پس از شکست این تلاش‌های دیپلماتیک دوباره از سر گرفته شده است.
جزئیات:
ایران تهدید کرده است که با انجام حملاتی علیه تأسیسات انرژی و زیرساختی در اسرائیل و کشورهای خلیج فارس تلافی خواهد کرد.
▪️
یک مقام آمریکایی به آکسیوس گفت: «سعودی‌ها ابراز نگرانی کردند و خواستار شفاف‌سازی درباره برنامه عملیاتی شدند.»
▪️
یک منبع دیگر مطلع از این تماس گفت محمد بن سلمان از ترامپ خواست تنش‌ها را کاهش دهد و از انجام این حملات خودداری کند.
▪️
کاخ سفید و سفارت عربستان سعودی در واشنگتن از اظهارنظر خودداری کردند.
مرور سریع:
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی که با نام اختصاری «کی‌بی‌اس» شناخته می‌شود، دیدار کرد.
▪️
یک منبع مطلع گفت این دیدار پس از آن به برنامه سفر وزیر سعودی افزوده شد که او با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، دیدار کرد و به او گفت عربستان سعودی خواهان کاهش تنش با ایران است.
▪️
این پیام با وجود حمله مشترک این هفته آمریکا و عربستان سعودی به شبه‌نظامیان طرفدار ایران در عراق منتقل شد.
▪️
این منبع گفت هدف از این دیدارها انتقال دیدگاه‌های محمد بن سلمان درباره جنگ ایران و اوضاع گسترده‌تر منطقه بود.
در پس ماجرا:
عربستان سعودی یکی از مهم‌ترین متحدان واشنگتن در منطقه است. ریاض، با وجود دوره‌هایی از تنش طی پنج ماه گذشته، از زمان آغاز جنگ در چند مقطع حساس بر سیاست ترامپ در قبال ایران تأثیر گذاشته است.
عامل خبرساز:
دیگر قدرت‌های منطقه‌ای، از جمله قطر، امارات متحده عربی، ترکیه و پاکستان نیز آمریکا و ایران را برای کاهش تنش تحت فشار قرار داده‌اند.
▪️
عباس عراقچی، وزیر امور خارجه ایران، روز شنبه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، که نقش میانجی مهمی میان واشنگتن و تهران داشته است، گفت‌وگو کرد.
▪️
عراقچی همچنین درباره احتمال حملات آمریکا با وزیران امور خارجه ترکیه و عربستان سعودی گفت‌وگو کرد.
▪️
عراقچی، بنا بر بیانیه‌ای در کانال تلگرامی خود، به همتای سعودی‌اش گفت: «هرگونه اقدام خصمانه از سوی آمریکا یا اسرائیل — یا مشارکت یا همکاری کشورهای منطقه در چنین اقداماتی — با پاسخ قاطع و متناسب نیروهای مسلح قدرتمند ایران روبه‌رو خواهد شد.»
آنچه باید زیر نظر داشت:
میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی برای بازگشایی تنگه هرمز، جداگانه با عراقچی، استیو ویتکاف فرستاده کاخ سفید و مقام‌های عمانی گفت‌وگو کردند.
▪️
یک منبع مطلع از مذاکرات گفت این گفت‌وگوها پیشرفت داشته است، اما هنوز مشخص نیست که آیا این پیشرفت برای فروکش کردن بحران کافی خواهد بود یا نه.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77701" target="_blank">📅 03:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EaLnDLhw5_dOLm6Z142P0i0RsmwBAOcuY4DcYjp2e2Ho_AOYkYniLm8T325hjelgOhVRGGt39r5MyiDT4kp0sQh6-4mhrdzIhAVbn3iW565sbzxpm8e9133iphSjG8xMl2IRV-ElZkm5bWHZS2GsBXjWZoGOHwhm4bHTSTA7qCeSy3V2N15cgntIaaSfqU5-_hLhyv3p8E-kLFVE_JSHggtxqcekVeamHy2x5QAjEE3Kg2hBt8S4yXVchVaHBSF6I1IWURvsEOVtSoBEBtVOxf35Q1Ur_Rqt4uaK2usHchy_IQNdo7QEc-1aZ-9p9mCxRKpZLx_F9vBwnORtkCug4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با افزایش تنش‌ها میان واشنگتن و تهران، «وای‌نت» روز شنبه گزارش داد، ورود و استقرار بیش از ۳۰ هواپیمای سوخت‌رسان نظامی آمریکا در فرودگاه بن‌گوریون تل‌آویو و افزوده شدن ۱۰ هواپیمای دیگر در روزهای آینده، موجب بروز اختلالات شدید، ترافیک سنگین هوایی و تاخیرهای روزافزون در پروازهای این فرودگاه شده است.
بر اساس گزارش سازمان فرودگاه‌های اسرائیل، میانگین تاخیر پروازها در ترمینال‌های مختلف به بیش از یک ساعت رسیده و دریافت بار مسافران نیز تا دو ساعت معطل شده است. وضعیتی که هم‌زمان با اوج سفرهای تابستانی و نقایص فنی اخیر در سیستم‌های کنترل ترافیک هوایی اروپا، مسئولان را نسبت به تشدید بحران و جدی‌تر شدن اختلالات در پروازهای بین‌المللی نگران کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77700" target="_blank">📅 03:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kW14Noma7hCTi1c6St3i4e19mb_G51hyjBjo47ro9TGfEDWA-3nMRO_ueSnoHQ21zj8_g6holFp64D54wROnFKzqvhd6HSKK3vwYFgnoSqTtfCG5tqYXZcxFvOdw9Lz6rD1lgGSY5XFoP2NsX4Q1mZZ70hMYGI4dtHQi9NwTPDvNcrvhqObEO_iqLXBO1lxOWSKM_r7MITAIKserUKHfRIhRT0XccyCkZSD8wCy_u3Y3ElREihRc5rODeFbBz23t7R19BAUnDHhTojjKCCaXsVrOXXWTBGbvkMeFfpEUSgYWXINIYywI_HPUzlMf1QowjfUY9tmEQE_yZFPR-Gacrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است
هم‌زمان با افزایش تنش‌ها در منطقه و انتشار گزارش‌هایی درباره احتمال از سرگیری حملات آمریکا علیه جمهوری اسلامی، دونالد ترامپ، رییس‌جمهوری آمریکا، تصویری را در تروث سوشال
منتشر کرد
که به کاهش ارزش ریال و افزایش تورم در ایران اشاره دارد.
در این تصویر با عنوان «ترامپ در حال نابود کردن ارزش پول ایران است» نوشته است که ایران با تورم شدید روبه‌رو است و ارزش هر دلار از حدود ۹۰ هزار تومان به ۱۹۰ هزار تومان افزایش یافته است.
ترامپ توضیح یا اظهارنظر دیگری درباره این تصویر منتشر نکرد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه شنبه دهم مرداد ماه، تصاویر ساخته با هوش مصنوعی را در شبکه تروث سوشال منتشر کرد که او را در لباس رزم جنگ استقلال آمریکا نشان می‌دهد. در مطلب دیگری، تصویری از ناوگان دریایی غرق شده جمهوری اسلامی در زمان ریاست جمهوری او دیده می‌شود.
در یکی از این تصاویر ساختگی، ترامپ با پوشیدن لباس فرماندهان جنگ استقلال آمریکا و در میان دود و آتش نبرد به تصویر کشیده شده است. در تصویری دیگر تحت عنوان «۱۵۹ کشتی ایرانی»، شناورهای نظامی ایران در دوره رییسان جمهوری سابق آمریکا روی آب نشان داده شده‌اند، در حالی که در به دوره ترامپ، تمامی این شناورها در قعر دریا غرق  شده‌اند.
این تصاویر در حالی منتشر می‌شوند که رسانه‌های مختلف از جمله
شبکه ۱۲ تلویزیون اسرائیل
از احتمال حمله گسترده ارتش آمریکا به ایران خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/77699" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0plL8q_gmZ2qV_6cpgkRLkYP94MVTc6aSeB3M0jEb4cjJyrfGuUyrhZxis2jbbhSvkWocWEXCgTDtcXdJquCWW8ig8DjWfvtbwlNY73j3uhNk4NEryLCbrFVkWAVhX0QCXcD3UN1hUjA-VBenKODjTnay8-N97rr_Wp96Jjy0WKWphZXVIDTHA3P8LJPTQb_jotCzSwvCU9OXh3R5blCeFbmBXZqa7CBzac4mW9-dD6jjcv5QmTXa8Xsh_tDnUPfw2jl1QdGXRlOWx0eBs3C_wYQpaoftAtUhFkXFFy1DcHldlm_wvsFatZd24dhEtBZN04axluY6EaZsihKKPzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سحرگاه روز شنبه ۱۰ مرداد ۱۴۰۵، حکم اعدام آروین خیرخواهان، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان شاهرود به اجرا درآمد. این جوان معترض، پیش‌تر از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شده بود.
به گزارش خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، حکم اعدام آروین خیرخواهان حوالی ساعت چهار بامداد امروز اجرا شد.
یک منبع نزدیک به خانواده این زندانی با تایید این خبر به هرانا گفت که مسوولان زندان تاکنون پیکر او را به بستگانش تحویل نداده‌اند. به گفته این منبع، به خانواده اعلام شده است که ساعت سه بامداد فردا برای تحویل پیکر مراجعه کنند و مراسم خاکسپاری نیز باید ساعت پنج بامداد برگزار شود.
آروین خیرخواهان در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت و سپس از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شد. این حکم پس از اعتراض، در دادگاه تجدیدنظر و دیوان عالی کشور نیز بدون تغییر تایید شد.
تاکنون جزییات دقیقی درباره زمان و نحوه بازداشت، مصادیق اتهامی، روند بازجویی، دسترسی این زندانی به وکیل انتخابی و مستندات مورد استناد دادگاه برای صدور حکم اعدام منتشر نشده است.
هرانا نوشته است، آروین خیرخواهان هنگام اجرای حکم اعدام ۱۹ سال و شش ماه سن داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 512K · <a href="https://t.me/VahidOnline/77698" target="_blank">📅 18:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=GTi_QBPdT0p6I3oV80CjEqg6jJ7KE4Q1mN0WQCdv_-Pq9SrlP3sEs-ElaSRJsy4T1qaevGvH5-1wSaujU3972ZeMHEQTYAFq5SiGyTd9JtqKFmIG0Do8q_-_0pOGyAaErpwvKVW3NYLAuUj8C-p7_wOGOq8u0k1eTgOYx2qnzuiJcZRtQctbSYa7eACfPx6WCd4_lyPYs51Wj364_JfR9yASSdWW1DHLwWq4HAw4nZ2CO0Zp5fXwiGFbM4bCy2aTVfeckkWeQYFoNsfJb9JE1hGw1xDZzjCurkaQFADLu0is-L-ukcbJyxY2W6ZtKnfirw0e-_sS0IlEfkiaEQIoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=GTi_QBPdT0p6I3oV80CjEqg6jJ7KE4Q1mN0WQCdv_-Pq9SrlP3sEs-ElaSRJsy4T1qaevGvH5-1wSaujU3972ZeMHEQTYAFq5SiGyTd9JtqKFmIG0Do8q_-_0pOGyAaErpwvKVW3NYLAuUj8C-p7_wOGOq8u0k1eTgOYx2qnzuiJcZRtQctbSYa7eACfPx6WCd4_lyPYs51Wj364_JfR9yASSdWW1DHLwWq4HAw4nZ2CO0Zp5fXwiGFbM4bCy2aTVfeckkWeQYFoNsfJb9JE1hGw1xDZzjCurkaQFADLu0is-L-ukcbJyxY2W6ZtKnfirw0e-_sS0IlEfkiaEQIoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر علی منوچهرآبادی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، با انتشار ویدئویی در اینستاگرام، تولد خود را کنار مزار فرزندش جشن گرفت و یاد او را گرامی داشت.
علی منوچهرآبادی، شهروند ۲۵ ساله کُرد اهل کرمانشاه، در جریان اعتراضات دی‌ماه ۱۴۰۴ در محدوده فلکه سوم تهرانپارس با شلیک گلوله جان باخت.
او پسرخاله میثم کُرانیان، از دیگر جان‌باختگان اعتراضات مردمی در کرمانشاه، بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/77696" target="_blank">📅 17:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c4i0TyoN50dmz8QujqNfm32cH17QtU1DCv1Iq18BXaPOtgEpTVM2InZMONSeAVrDw2vi78lNqd9W5_v4ujMIjeWO4U86YxgtY4fJV2NlAdJZ-QtW7Qok60aWvUouVAyBy5Sl9jXOnv7mRf2JNh7UcgBbRZc81N_zRHHFFVxw8ZD-iqaxYGKq3D_L0Zxavb9X2vz2ZqyyR7EF5wu_-TnLU7-qfePkQhpND-gV9INFpVGPH1myUS0qKqxsXQeMkNiy352nNrEq78ngUTBIqUSiMxgnilVQcPSj7x-TygThQS8gg3rF9f1t_w-Cn8rx451bzWGWA33vC8VKPFxP9FR-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت ارتش کویت، ترجمه ماشین:
سامانه‌های پدافند هوایی کویت در حال مقابله با حملات پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران، هستند.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان درخواست می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 518K · <a href="https://t.me/VahidOnline/77695" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INa_DjIZysslTWcgLn7UBm3k7Js_zJYX7IrPh-9RFVQ8eQFwnQu6Vb703mgkQEtBLgfqg_bP8aAtS-Oqy3u9hOujt5eGVnMbDc_NO5x_wRWiqANAL720eB3VO6Mi2djuG2-OqOhl-DLP433otVouDPT-XVY5s0qozpHPq246RGNqwsT-lRavNuNdlLMcH4TbkCqgiF99R6VnP5aVb-C370JXFi2-acX42blq8SciM8w_cVGVSA5kazFpzS4U07IaX0VSFbeg6_dprAt3jeNYh_aKUs_oY63EIanOwiTh0dMi0INf2SZXWwmVIHpPiTDkh20JZSWPqf-qU8yqildx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا از وقوع یک حادثه دریایی در شمال شرق خصب عمان، در نزدیکی یک نفتکش گزارش داد.
ساعاتی پیش نیز گزارش شد یک نفتکش در ۱۱ مایل دریایی شمال شرقی لیما، در مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/77694" target="_blank">📅 09:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSWd0dBp1HhPyNEVRNZzLwK3XHKpSP-2g4-i_0EmeX5cm4kvp94B6Q_eQXwqF2bvQzEu9MZ_YLp2_gWcihcuB3Mlz5rfhuCqGywLiJrr4RUzjeAnSgQrckKk7eRIeYlc6tEd7kLYzu5SH6Q0MEt_W4FFY3Z4OF759gY9Iqd43NDwYQeCbujc4gnSds3ddFvrDwBSZbbcsMQrM4rjqBQzH7q5ZrRos_ZnPUqyQIh_-nWHEmaxZMK6ovACTisjvGyq7AqI9iLd9a2ofyCIvZHFig74Z7Sa0rZL9obfVylAKSEkwUmPps92EWBO5n8LDXEfQoBVjFBocZmQQ7iHbvOI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس گفت: در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.
او ادامه داد: تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.
او اضافه کرد: بعدتر تصمیم گرفتیم همان سحرگاه خبر مرگ رهبری را اعلام کنیم و به مردم بگوییم به خیابان بیایید.
قالیباف در حالی می‌گوید که همان ساعت اول از مرگ خامنه‌ای مطمئن شده که مقام‌های جمهوری اسلامی تا بامداد روز بعد خبر مرگ خامنه‌ای را تکذیب کرده و اعلام می‌کردند او در اتاق فرماندهی حضور داشته و مشغول راهبری جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/77693" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D1TZPjDf2Py3ETIRdZ5S2OZvnI0UzjJH4-2bFSohfaHuwvcZOsy4tvpiEvWNnOsKbWILBeQLrj9HoNtrqjEMI4OMCZX-6sV3d_pAtip0gGxUhGfJFRA7KRfDv7PDU4y42U2012MKImdzwaTuCtuNrm-4DDc0dI4n1qiCCBcgyXIznFtVGuGzXzdoju11HvQett5H8J9aMm144iPIoGCZGsyqd-lvI6HcVd-n_p14kPlhPsfnbWxxXeW0r86RTvMJOLsQvTtSdy3CTvuZtpKGI7oeKVYDE_7lBur__tAvpIbb-rs1ZMqQLgECdFZKEL1SQW2jKvJtPdrIwWSPE6LPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در حدود ۱۱ مایل دریایی (بیش از ۲۰ کیلومتری) شمال شرقی لیما، در استان مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/77692" target="_blank">📅 07:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOat_5GNwPwDM6tPXWKvPM5nif06dkoJ_5bpa2SSZe7Ys38TVsGF4a9Fr-Jzy-yxP32nsZWpGzcfMLWwNa0b3z0wdET6P6s0mJkeMVEZkhURRyHOPGa9VkuzlId_gyQTrdf0IOJfftij70x0A5bsCKInm-CGl8KWPLghzGUtnZu9fE0Q2h6v9nkRgfPhDI37ZN_EMZ2SvA43NZX6Gt3E4ceQvMEdQvGH62zvb6-KWnFJExxcarkHId76InWLPiSN-iYO-0qI3bR2CILDSyRHJZa_VJl4fX3d0ittGaYArdzV-jr-OfWCUaTKazIaZnCvmlMLNMKd4warWWavkk-wiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آمریکایی و اروپایی آگاه به «ان‌بی‌سی» گفتند که روسیه در حال به اشتراک‌گذاری اطلاعات ارزشمند الکترونیکی و ماهواره‌ای با ایران است که به تهران در جنگ جاری با ایالات متحده کمک می‌کند. به گفته این مقامات، ردیابی ماهواره‌ای و اطلاعات سیگنالی روسیه احتمالا ایران را قادر می‌سازد تا نیروهای آمریکایی را در حملات هوایی با دقت بیشتری هدف قرار دهد، دفاع هوایی خود را در برابر حملات ایالات متحده تقویت کند و در عملکرد تسلیحات ساخت آمریکا اختلال ایجاد نماید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/77691" target="_blank">📅 03:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5Lo66P31BC4I7DNFX2CKo8Dd5ML3K6_z4yCvotb-hyxmP-kJUEXL2nuHR_Ilh_HdaN7QFaHAYPjRQWH_icdzHlz3AMcrYpmoSVn0VsUiganVgfWx4_dNLA8JGZRIF-Ds8BGenkZ5JgvQx0gruqR5Ik1MaZHA9mbb1AePfOz63HPiyWUn75Lr36uX1a-YtQZ35kEIxhPjd-IwBBSDC3W6HImPqY0pJCf3VF9OScaE26k4L7sONo_US5j6hXTSYmdLCnBjF74pBSJtXpvBzU0EF5r4Dqy-mfXhBU1Bqsp_3W00B5Yo3F_wJ-8UvDxfYBD7pxb_zYQsN-FOysgFRnAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
ترامپ دستور حمله‌ای تازه به ایران را صادر کرد
"
وال‌استریت ژورنال
به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، طرح حمله جدید به ایران را که در کمپ دیوید ارائه شده بود، تصویب کرده و این عملیات ممکن است از آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز ادامه یابد.
به گفته این منابع، هرگونه پیشرفت فوری در دیپلماسی یا تغییر نظر ترامپ می‌تواند اجرای حملات را متوقف کرده و مسیر مذاکرات را دوباره باز کند.
این روزنامه نوشت یکی از گزینه‌های مورد بررسی، کارزار دو هفته‌ای حملات هوایی فشرده برای تضعیف توان موشکی جمهوری اسلامی است.
مقام‌های آمریکایی گفتند ترامپ معتقد است توافق موقت صلح کارساز نبوده و همچنان بر توقف برنامه هسته‌ای جمهوری اسلامی و پایان کنترل تهران بر تنگه هرمز اصرار دارد، در حالی که تهران از مواضع خود عقب‌نشینی نکرده است.
وال‌استریت ژورنال افزود مشاوران نظامی ترامپ کاهش ذخایر مهمات آمریکا را یکی از مخاطرات احتمالی این عملیات ارزیابی کرده‌اند.
@
VahidOOnLine
اکسیوس:
ترامپ حمله به اهداف انرژی ایران در چند روز آینده را بررسی می‌کند
ترجمه ماشین: دونالد ترامپ، رئیس‌جمهوری آمریکا، به‌طور جدی در حال بررسی انجام حملاتی علیه اهداف انرژی در ایران طی چند روز آینده است، اما هنوز دستور نهایی اجرای آن را صادر نکرده است؛ یک مقام آمریکایی روز جمعه این موضوع را به اکسیوس گفت.
چرا اهمیت دارد:
هدف از کارزار جدید بمباران آمریکا علیه اهداف انرژی و زیرساختی در ایران، تلاش برای واداشتن ایرانی‌ها به پذیرش شروط ایالات متحده در مذاکرات جاری آتش‌بس خواهد بود.
▪️
این حملات ممکن است برای نخستین‌بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
▪️
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین رسانه‌هایی بودند که درباره حملات احتمالی گزارش دادند.
آنها چه می‌گویند:
ترامپ در آغاز جلسه روز جمعه کابینه به حمله احتمالی اشاره کرد و گفت: «خب، ما خیلی سخت به آنها ضربه خواهیم زد و می‌دانید، بالاخره در مقطعی خواهند گفت که دیگر نمی‌توانیم تحمل کنیم.»
▪️
او افزود هرچه ایالات متحده حملات بیشتری انجام دهد، ایرانی‌ها ضعیف‌تر می‌شوند «و بعد کم‌کم از پا می‌افتند.»
▪️
کارولین لیویت، سخنگوی کاخ سفید، به اکسیوس گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در جلسه کابینه گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 484K · <a href="https://t.me/VahidOnline/77690" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JORDOa16YZKTV_y4IXC5oqTpYKn4MFliq-CBD17Whd-LtFVTGjCI9VCFCMTRTzDy4EmxomcHEKd0zE2oVWZSLK8naBEdPKemamAz8StyDSc3GLO9i3xzIETBAsQFAi8L4JWbjucvfFlVx6hxEo-yMhT7xtTcCcReCeL1HJCC6Tld5IwjoNLIVFLBVi1kY-gsy14tQ4D6T39yZ8IGUSU93XO3wzY5XXlUwsF6WbgtPNen9UiOP1bTiQzLJmBASAeT9YAfN8tl71SUy3cVJG6jzRo5Ml_9zwk2gOlB0diVgrwZ8Lqb9_YiO2o6Djx_oo3iK2kdT9FHcdPme7j3b00UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا و اسرائیل برای بمباران اهداف مرتبط با انرژی در ایران آماده می‌شوند
"
سی‌بی‌اس به نقل از منابع
ترجمه ماشین:
واشنگتن — چندین منبع به سی‌بی‌اس نیوز گفتند که ایالات متحده و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین کارزارهای بمباران تاکنون علیه اهداف زیرساخت‌های انرژی در ایران هستند و احتمال انجام حملات در طول تعطیلات آخر هفته وجود دارد.
بحث‌هایی درباره تلاش برای پایان دادن به عملیات تا زمان بازگشایی بازارهای مالی در روز دوشنبه مطرح شده بود، زیرا نگرانی‌هایی درباره تأثیر بمباران‌ها بر اقتصاد آمریکا و جهان وجود دارد، اما زمان مشخصی برای پایان عملیات قطعی نشده بود.
به گفته چندین منبع آمریکایی، اسرائیلی‌ها در جریان قرار گرفته‌اند و در حال هماهنگی با ایالات متحده هستند. این منابع گفتند رئیس‌جمهور هنوز دستور نهایی آغاز حملات را صادر نکرده است.
سخنگوی دولت اسرائیل به درخواست اظهارنظر پاسخ نداد.
یک عملیات مشترک به معنای بازگشت اسرائیل به عملیات رزمی خواهد بود؛ عملیاتی که این کشور در جریان آتش‌بس میانجی‌گری‌شده از سوی آمریکا متوقف کرده بود. از زمانی که تفاهم‌نامه از هم پاشید و ایالات متحده در اوایل ژوئیه عملیات رزمی را از سر گرفت، ایران اسرائیل را هدف قرار نداده است.
به گفته منابعی که بعداً در جریان قرار گرفتند، طرح حمله نظامی روز جمعه در نشست کابینه دونالد ترامپ، رئیس‌جمهور آمریکا، در کمپ دیوید مطرح شد. یکی از منابع گفت برخی از دستیاران کاخ سفید که بر مسائل سیاسی تمرکز دارند، به‌شدت با این طرح مخالف بودند.
زمانی که خبرنگاران در اتاق حضور داشتند، آقای ترامپ گفت: «ما آن‌ها را بسیار سخت هدف قرار خواهیم داد. بالاخره در مقطعی خواهند گفت: “دیگر نمی‌توانیم تحمل کنیم.”»
او در پاسخ به پرسش خبرنگاران درباره احیای دیپلماسی گفت: «فکر می‌کنم ما فقط می‌خواهیم پیروز شویم.»
دو منبع گفتند زیرساخت‌های انرژی، از جمله نیروگاه‌ها و پالایشگاه‌ها، احتمالاً هدف قرار خواهند گرفت.
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، در بیانیه‌ای به سی‌بی‌اس نیوز گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در نشست کابینه خود گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
شان پارنل، سخنگوی ارشد پنتاگون، گفت پنتاگون پیش از آنکه رئیس‌جمهور تصمیم نهایی خود را بگیرد، درباره اهداف اظهارنظر نخواهد کرد.
پارنل در بیانیه‌ای گفت: «وزارت جنگ کاملاً آماده و مهیای عملیات است و می‌تواند در هر لحظه دستورات رئیس‌جمهور را اجرا کند.»
یک مقام پیشین نظامی آمریکا به سی‌بی‌اس گفت، فایده حمله به زیرساخت‌های انرژی این خواهد بود که بر توان نیروهای نظامی ایران برای ارائه خدمات و اداره مؤثر کشور تأثیر بگذارد.
یک مقام ارشد اسرائیلی گفت هنگامی که آقای ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اوایل این هفته دیدار کردند، نتانیاهو او را در جریان سه گزینه برای جنگ قرار داد که یکی از آن‌ها حملات نظامی متمرکز بر مسیرهای تدارک‌رسانی زمینی بود. نتانیاهو همچنین با هگست، وزیر دفاع آمریکا، دیدار کرد.
یک مقام آمریکایی گفت ایالات متحده در جریان این درگیری پیش‌تر به پل‌هایی با کاربری دوگانه — که نظامیان و غیرنظامیان از آن‌ها استفاده می‌کردند — حمله کرده است.
روز جمعه گفت‌وگوهایی در سطوح عالی دولت آمریکا درباره قطع برق سراسر تهران انجام شد، اما تا بعدازظهر جمعه هیچ تصمیمی گرفته نشده بود.
هفته گذشته، آقای ترامپ در تروث سوشال نوشت که در ازای هر حمله به یک کشتی در تنگه هرمز، یک پل یا نیروگاه ایرانی را بمباران و نابود خواهد کرد.
این خبر فوری است و به‌روزرسانی خواهد شد.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/77689" target="_blank">📅 00:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gUvsDpH39WHUyhYo0WB03xEwxriQgcDUjYGN5lvtVPAKgaXLO8nBesgdzCNlg3QME6amU3ALmpf8jpC8Bk2EK17yjnwEdCUWmXdwNm4rfzXKegr00-KRbfHKtPw0fOVehkZH85nwt2_EwImGqFG4ONON726t7gtxBeiECUZuael69Pcuhu_5ldKoneG8bhwH3Ee_DhlTrRTNROMVJRlGaWrkIRWy2DZ7bFSDLLUybTW0rwItS_EhqbAxHNsuKLPBNh_Kj142FXuRrC3cZZfK-gP_AHcsZQ9Av4iv8b3QEYA_KH0uC5cMXgLzESb-aPFt3Eii9xqff9nSF9vpcPXgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد. این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های…</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77688" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrE74ry6pDPhcYd84NpTmu252IZ_2mdeLV2ImlFfr8i1VwKbKsE21HhCTaMJ1o9VJNH59cFT7EGONeqGzgCuSud_1CEbZ7XltljvGvL3BjbkYURHvW5l3fn3VdaKDl09I8SxaB-HU0x6lkesMLiQG915T7oEKJ1Vq4DvQDVNugfzgo81wOTpVjLbAYJoYT6QAh49M7RZgGDlk_U8_4btg6cZ-NdX6-5wy832-aX1Go9M5UNLp2ZnsG6uNueFsmqI9WwBgixUg8kHlXVsLJhTZG3pjBKeUiKpgl2Z0bi6NDiTGcqhm1DHsG78bo8HemHlH4LJIuCjiV93-EmE93SooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز جمعه ۹مرداد۱۴۰۵
گزارشی تحقیقی
منتشر کرده، از استفاده سپاه از شبکه قمار غیرقانونی ایران که با آن میلیاردها دلار را به رغم تحریم‌ها جابه‌جا می‌کند.در این گزارش به یک صرافی ارز دیجیتال مستقر در دوبی اشاره شده که  به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
در گزارش رویترز صرافی مذکور «شل‌بیت» معرفی شده و تایید شده است که این صرافی، یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.
بنابر گزارش منتشر شده، «شل‌بیت» صدها میلیون دلار ارز دیجیتال را به «بایننس»، بزرگ‌ترین صرافی ارز دیجیتال جهان، منتقل کرده است. دو شرکت تحقیقاتی حوزه ارزهای دیجیتال و یک تحلیلگر مستقل مدارکی ارایه کرده‌اند نشان می‌دهد نشانی ثبت‌شده صرافی بدون مجوز «شل‌بیت» دفتری در بالای یک هتل ارزان‌قیمت در محله‌ای معمولی و نه‌چندان مطرح در دوبی است. این صرافی توسط یک ایرانی مقیم خارج از کشور اداره می‌شود. رویترز اطلاعات ارایه شده در این زمینه را تایید کرده است.
در بخش دیگری از این گزارش آمده است که یکی از مشتریان اصلی «شل‌بیت»، یک شبکه قمار فارسی‌زبان متشکل از بیش از ۲ هزار وب‌سایت است که توسط دو اینفلوئنسر مشهور ایرانی در شبکه‌های اجتماعی تبلیغ و اداره می‌شود. گفته شده که این دو ارتباطاتی در سطوح بالای حکومت ایران دارند.
یکی از آن‌ها در یک ویلای گران‌قیمت در مادرید فعالیت می‌کند و دیگری تا همین اواخر در یک هتل لوکس در هنگ‌کنگ مستقر بود.
هر دو اینفلوئنسر اشاره شده و همچنین فرد اصلی اداره کننده صرافی «شل‌بیت» در سال ۲۰۲۳ در ایران به اتهام مشارکت در یک پرونده قمار غیرقانونی، محکوم شدند.
مطابق قوانین جمهوری اسلامی «قمار کردن» امری غیرقانونی است و مجازات‌های حبس و شلاق برای مرتکبان به‌دنبال دارد با این‌همه گزارش رویترز تایید می‌کند که این شبکه قمار تازه شناسایی شده به سیستم پرداخت آنلاین ایران که مستقیما تحت نظارت بانک مرکزی است دسترسی دارد.
شل بیت بر اساس گزارش رویترز در مرکز عملیاتی است که شبکه قمار، بانک مرکزی و دیگر نهادهای تحریم‌شده ایرانی را به بازارهای جهانی ارزهای دیجیتال مرتبط می‌کند.
یکی از چهره‌های اصلی این شبکه قمار، «ساشا سبحانی»، پسر یک دیپلمات و سفیر پیشین ایران و دیگری «پویان مختاری»، یک چهره مشهور شبکه‌های اجتماعی و خواننده است که پس از اخراج از دوبی در اواخر ماه آوریل، مدتی بین هتل‌های لوکس هنگ‌کنگ جابه‌جا می‌شد.
پویان مختاری اخیرا و در جریان جنگ آمریکا و اسراییل با انتشار ویدیویی گفت که مخالف جمهوری اسلامی نیست و دچار «تحول فکری» شده است.
تحقیقات رویترز آشکار می‌کند که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال پول به خارج از کشور استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77686" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OFyddEswqq63yYJhhF-kqBQYwbX7WC6zcAGYEo9gCspJlJQ74eGzOSLoL_HqBr3j9bu-dfhl52S9tKJoyNhMJfBnbf4sBP0NVGs_kI6NwT52smeQ5hTJbOxI_brLJ3enS1kFV78CbhvO-Z290zIMwBFzdiDJVMIwrwjAe6cevlDKuZWuC3CeJhsuhGayMb0v6kEWymG5Ubkw9T7n_ET9drfilys6gh1oJ1TqlsUB0_oCBy_SuRgnBfQAYTURvAtmy56ZrKnFsloKnsA5_VOvN4IOHxe0-39RxZyWo_GtJcl7IcrtbSp_WuoTgS8yyhOm7vVsOfLtLScpRK5bbQodfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tHxCK862vW30UOyMoULwph-spPop7WZaGEW-rBivoESAga65SBaK0Q1Q_Bc9eox7DmcOmkDa1Mvnh-46XJ8SKMUr8M2DfhqRRck55aUF3FvlDk1Chbrk2AoO4aA198OHzssAehDNokHi8qltpvJ7zpAgpkLX4gyi-c3Gk51sIk4YZRZ-h8IwtAjtusq8IgJ5zVKLmrmNShsGs1pA_pPB05vE1o4BmHd55YnB3PvUenm5A9NrNrWP3sh0i_XUZlASVoxz3BYFUhsWqUjuMBRq52Y3lBiz6U8S7_nrxoJroqDsXHt3Rb-rs2OFMzJkE1ma2JN_wrSGlYb14zBlyj5MWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=ii_kVgA4awVfhBt5oMa_ndhdBHWWw7G-YNiJckQETDA2sMbsoxDbwiJDIIw-m2a7YjqddNbEy9LwfRJXXsNWHweCQpuGCZNL-oFrVQRfqSdPneasEswDChUcAfzvCSeWdWe2SobOK7QiBSYEftXV2FezMY3c5RBeqmABNsrTG17YI4dDSTqmiwjVFYbcOebuahxxa8JWQlMdccP4U8vdiqWp90J2HAEsL6C0jVJNvDKUmjf46sdNrRuZZej4zbC1Y2QtwwhZOqBAgIgetbQWlMpEWh3JnoaTOSDiKiYN2zrTAWEca4OdWd_IOwZYi8dEh3xH5qCa_Ib6p94yFL7TRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=ii_kVgA4awVfhBt5oMa_ndhdBHWWw7G-YNiJckQETDA2sMbsoxDbwiJDIIw-m2a7YjqddNbEy9LwfRJXXsNWHweCQpuGCZNL-oFrVQRfqSdPneasEswDChUcAfzvCSeWdWe2SobOK7QiBSYEftXV2FezMY3c5RBeqmABNsrTG17YI4dDSTqmiwjVFYbcOebuahxxa8JWQlMdccP4U8vdiqWp90J2HAEsL6C0jVJNvDKUmjf46sdNrRuZZej4zbC1Y2QtwwhZOqBAgIgetbQWlMpEWh3JnoaTOSDiKiYN2zrTAWEca4OdWd_IOwZYi8dEh3xH5qCa_Ib6p94yFL7TRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد.
این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های اسپانیا، پس از این موج ورود مهاجران، حدود ۳۷ هزار و ۵۰۰ نفر به‌صورت داوطلبانه به مراکش بازگشته‌اند.
در جریان تلاش برای عبور از مرز، دست‌کم ۵۷ نفر جان باختند؛ شماری بر اثر غرق‌شدن و برخی دیگر در ازدحام هنگام عبور از موانع مرزی.
پدرو سانچز، نخست‌وزیر اسپانیا، این رویداد را «نقض حاکمیت ارضی اسپانیا» خواند و گفت روند بازگرداندن مهاجران فاقد مدارک قانونی با همکاری مراکش تسریع خواهد شد.
اتحادیه اروپا در شرایط استثنایی به کشورهای عضو اجازه می‌دهد به‌طور موقت کنترل مرزهای داخلی منطقه شنگن را دوباره برقرار کنند.
@
VahidHeadline
پیش‌تر:
هزاران مهاجر از شامگاه پنج‌شنبه تا صبح جمعه با عبور از مرزهای مراکش وارد مناطق تحت اداره اسپانیا در شمال آفریقا شدند
ورود مهاجران در تمام طول شب ادامه داشته و صبح جمعه نیز همچنان ادامه پیدا کرده است.
همزمان، تصاویر خبرگزاری رویترز، هجوم جمعیتی از مهاجران به گذرگاه مرزی میان مراکش و شهر ملیلیه اسپانیا در شمال آفریقا، را نشان می‌دهد.
در سئوتا، دولت اسپانیا برای مقابله با صدها مهاجری که از مسیر دریا و خشکی وارد این منطقه شده‌اند، یگان‌های نظامی را مستقر کرده است.
تصاویر منتشرشده نشان می‌دهد صدها مهاجر با شنا کردن یا استفاده از تایرهای بادی از سمت مراکش تلاش کرده‌اند خود را به سئوتا برسانند و گروهی دیگر نیز با عبور از یک دروازه مرزی زمینی وارد شهر شده‌اند.
@
VahidOOnLine
وزیر کشور فرانسه روز جمعه اعلام کرد پاریس در پی ورود هزاران مهاجر از مراکش به سئوتا، کنترل‌های مرزی خود با اسپانیا را افزایش خواهد داد.
@
VahidOOnLine
فنلاند اعلام کرد از پیشنهاد ایتالیا برای تعلیق عضویت اسپانیا در منطقه بدون کنترل مرزی شنگن حمایت می‌کند. اقدامی که در پی ورود ده‌ها هزار مهاجر به منطقه سئوتا، تحت حاکمیت اسپانیا در شمال آفریقا، مطرح شده است.
@
VahidOOnLine
پدرو سانچز، نخست‌وزیر اسپانیا، روز جمعه نهم مرداد ماه، ورود گسترده مهاجران به سئوتا، منطقه تحت حاکمیت این کشور در شمال آفریقا، را «نقض و حمله به تمامیت ارضی اسپانیا» محکوم کرد.
سانچز پس از موج اخیر عبور مهاجران از مرز مراکش به سئوتا، این اقدام را محکوم کرد و تاکید کرد دولت اسپانیا از حاکمیت و مرزهای خود دفاع خواهد کرد.
@
VahidOOnLine
ایلان ماسک، میلیاردر آمریکایی و مالک شرکت‌های تسلا و اسپیس‌ایکس، در واکنش به ورود گسترده مهاجران مراکشی به شهر سئوتا در اسپانیا، با انتشار تصاویری از فیلم «جنگ جهانی زد»، این وضعیت را به «آخرالزمان زامبی‌ها» تشبیه کرد و نوشت: «وای، اوضاع اسپانیا واقعا دیوانه‌کننده به نظر می‌رسد!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77680" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نشست خبری دولت ترامپ در کمپ‌دیوید
ویدیوی کامل با زیرنویس فارسی:
۱۰۰ مگابایت
نسخه یک گیگابایتی:
اینجا
متن فارسی ۱۶ بازه از ویدیو
بخش‌هایی از متن لینک بالا:
🔻
ترامپ:
در مینه‌سوتا یک حمله سایبری رخ داده و آن را به ایران نسبت داده‌اند.
فکر نمی‌کنم چنین باشد. من مینه‌سوتا را مقصر می‌دانم، چون به‌شدت بی‌کفایت هستند. حمله‌ای سایبری به ۳۰ تأسیسات آب انجام شد و من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم.
آن‌ها دوست دارند بگویند: «اوه، کار ایران بود.» ایران باید خیلی خوش‌شانس باشد. ایران مشکلات بزرگ‌تری از نگرانی درباره مینه‌سوتا دارد.
....
🔻
ترامپ:
جنگی در جریان است. شاید شما آن را جنگ بنامید؛ من شاید آن را عملیات نظامی بنامم، چون آن‌ها دیگر نیروی دریایی ندارند؛ نابود شده است. نیروی هوایی‌شان نابود شده است. هواپیما ندارند.
بخش بزرگی از موشک‌هایشان از میان رفته است. هنوز مقداری دارند، اما بسیار کمتر از چهار یا پنج ماه قبل. ظرفیت تولیدشان تقریباً از میان رفته و ظرفیت پهپادی‌شان نیز تقریباً نابود شده است.
تعداد بسیار کمی دارند، اما هنوز مقداری باقی مانده است. از نظر من اگر حتی یکی داشته باشند، همان هم بیش از حد زیاد است.
🔻
به ویتنام نگاه کنید؛ ۲۰ سال آنجا بودند. به افغانستان نگاه کنید؛ سال‌های زیادی آنجا بودند. به جنگ کره یا هر جنگ دیگری نگاه کنید؛ سال‌ها طول کشید. ما پنج ماه است وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
باز هم مقداری برایشان باقی مانده، اما به‌زودی همان مقدار هم باقی نخواهد ماند.
🔻
مارکو روبیو:
نخستین موضوع، دادگاه کیفری بین‌المللی است؛ سازمانی بین‌المللی و نامشروع. خودشان را نامشروع کرده‌اند، چون ادعا می‌کنند حتی اگر عضو آن دادگاه نباشید، باز هم می‌توانند به سراغتان بیایند.
معنای واقعی آن این است که در آینده نظامیان آمریکایی، رهبران سیاسی و افراد دیگر ممکن است از سوی این دادگاه کیفری بین‌المللی تحت کیفرخواست قرار بگیرند. ...
🔻
ترامپ:
هیچ اطلاعاتی وجود ندارد که نشان دهد آن‌ها دنبال من هستند. البته ممکن است چنین اتفاقی بیفتد.
حرف من این است که این یعنی او نمی‌خواهد از من دفاع کند؛ می‌خواهد از بی‌بی و افراد مختلف دیگری دفاع کند.
افراد زیادی هستند که نباید به این شکل با آن‌ها برخورد شود، اما در حال حاضر هیچ نشانه‌ای وجود ندارد که من یکی از آن‌ها باشم.
....
🔻
پیت هگست:
... تعجب می‌کنید چرا حوثی‌ها در این درگیری حضور ندارند، با اینکه نیروی نیابتی ایران هستند؟ چون ۴۵ روز سنگینی قدرت آمریکا را احساس کردند. و شما شجاعت انجام این کار را داشتید.
🔻
اسکات بسنت:
... در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگ‌ترین بانک ایران فروپاشید. بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد.
اکنون تورم آن‌ها ۱۸۰ درصد است. قادر به پرداخت حقوق نیروهایشان نیستند و به دستور شما در سراسر جهان به‌دنبال دارایی‌هایشان می‌گردیم.
این پول به مردم ایران و آمریکایی‌هایی می‌رسد که از اقدامات ایرانی‌ها آسیب دیده‌اند؛ چه در ماجرای ناو یو‌اس‌اس کول، چه پادگان‌های لبنان، یا حملات ایرانی‌ها به آن کشتی‌های در حال خروج.
مشارکت در این کار برای من افتخار بوده و مشتاق ادامه آن هستم.
🔽
درباره ادامه جنگ:
🔺
خبرنگار:
آقای رئیس‌جمهور، در ۱۰ روز گذشته حملات میان ایران و ایالات متحده را دیده‌ایم. چگونه آتش‌بس را احیا می‌کنید و دیپلماسی را دوباره از سر می‌گیرید؟
🔻
ترامپ:
فکر می‌کنم فقط می‌خواهیم پیروز شویم. عملکردمان بسیار خوب است. تلاش می‌کنیم تا جایی که در چنین شرایطی ممکن است، ملایم باشیم، اما آن‌ها در حال نابودشدن هستند.
دیگر نیروی دریایی، نیروی هوایی یا پدافند هوایی ندارند. این به آن معنا نیست که هیچ توانی ندارند؛ مقداری دارند، اما بسیار اندک است.
فقط می‌خواهیم پیروز شویم. نمی‌خواهیم آن‌ها این توان را داشته باشند. موضوع بسیار ساده است.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران سلاح هسته‌ای نخواهد داشت و نمی‌تواند داشته باشد. اگر چنین سلاحی داشتند، خاورمیانه تا الان نابود شده بود.
اگر من برجام، همان توافق اوباما، را متوقف و لغو نکرده بودم، آن‌ها اکنون سلاح هسته‌ای داشتند.
فکر می‌کنم اسرائیل دیگر وجود نداشت؛ در بخش‌های بزرگی از خاورمیانه و شاید کشورهای دیگری در قاره‌های مختلف نیز، چون صادقانه بگویم این افراد دیوانه‌اند.
بنابراین نمی‌توانند سلاح هسته‌ای داشته باشند و نخواهند داشت.
🔺
خبرنگار:
[پرسش ناقص و نامفهوم درباره آنچه در چهار یا هشت هفته آینده باید انتظار داشت.]
🔻
ترامپ:
می‌دانید، به آن‌ها حمله خواهیم کرد؛ حملات بسیار سختی به آن‌ها وارد خواهیم کرد. بالاخره در مقطعی خواهند گفت: «دیگر نمی‌توانیم تحمل کنیم.»
🔺
خبرنگار:
آقای رئیس‌جمهور، بازگردیم به ایران. گزارشی منتشر شده که ارتش پیشنهادی داده است تا ظرف ۱۰ یا ۱۴ روز حمله‌ای بزرگ و سخت انجام دهید—
🔻
ترامپ:
ما همین حالا هم حمله بزرگ انجام داده‌ایم. منظورتان از «بزرگ» چیست؟
آن‌ها ۱۵۹ کشتی داشتند؛ تمام نیروی دریایی‌شان همین بود. هر ۱۵۹ کشتی، تمام نیروی دریایی‌شان، در کف دریا قرار دارد. من این را حمله بزرگ می‌نامم.
تسلیحات پدافند هوایی بسیار خوبی داشتند، اما کار نکرد و همه آن از بین رفته است. تمام رادارهایشان از بین رفته، رهبرانشان از بین رفته‌اند؛ همه‌چیز از بین رفته است.
🔻
ترامپ:
برای مثال، خواندید که پنج موشک شلیک شد. سرعتشان ۸۶۰۰ مایل در ساعت بود.
فکرش را بکنید؛ اگر با خودرو ۶۰ مایل در ساعت بروید، کمی سریع به نظر می‌رسد. این موشک‌ها ۸۶۰۰ مایل در ساعت سرعت داشتند و موشک‌های بزرگی بودند. به سوی اردن شلیک شدند و نیروهای ما آنجا بودند: بنگ، بنگ، بنگ، بنگ، بنگ.
[خنده حاضران]
این می‌توانست کلیپ صوتی خوبی باشد! پنج موشک شلیک شد و هر پنج موشک را پیش از آنکه نزدیک شوند، ساقط کردیم. هیچ کشور دیگری چنین توانی ندارد.
🔺
خبرنگار:
آقای رئیس‌جمهور، گفتید هنوز مقداری توان برایشان باقی مانده است. آیا آمریکایی‌ها باید آماده باشند که این حملات متقابل ادامه پیدا کند تا زمانی که ایران دیگر توان حمله فوری نداشته باشد؟
🔻
ترامپ:
ضعیف‌تر خواهند شد. شاید اکنون کمی قوی‌تر شوند، اما ضعیف‌تر خواهند شد.
🔺
خبرنگار:
و بعد به‌تدریج از نفس می‌افتند؟
🔻
ترامپ:
بله، فکر می‌کنم همین‌طور است. احمقانه است که بگویم نه. همیشه باید مراقب باشید.
🔺
خبرنگار:
وضعیت مذاکرات چگونه است؟ چه کسی از طرف دولت در مذاکرات حضور دارد؟
🔻
ترامپ:
آن‌ها همیشه می‌خواهند مذاکره کنند، اما بارها زیر قولشان می‌زنند. استیو در حال مذاکره است. جرد هم هست؛ افراد بسیار خوبی داریم. جی‌دی به‌شدت درگیر است. افراد فوق‌العاده‌ای در حال مذاکره هستند. مارکو هم درگیر است.
افراد بسیار خوبی داریم؛ بهترین‌ها را. اما آن‌ها توافق خواهند کرد.
برای مثال، درباره موضوع هسته‌ای صحبت می‌کنیم و هفت ساعت آنجا می‌نشینیم و درباره برنامه هسته‌ای حرف می‌زنیم. می‌گویم چرا هفت ساعت؟ ده دقیقه کافی است؛ پنج دقیقه وقت دارید، باید حلش کنید.
اما هفت ساعت صحبت می‌کنند، بعد بیرون می‌آیند و من می‌گویم درباره موضوع هسته‌ای گفت‌وگو کردند. آن‌ها بیرون می‌روند و می‌گویند: «ما هرگز درباره موضوع هسته‌ای صحبت نکردیم.»
می‌گویم چرا؟ چرا چنین چیزی می‌گویند؟ تنها کاری که می‌کنند این است که من را عصبانی می‌کنند.
🔺
خبرنگار:
با توجه به آنچه گفتید، باور دارید می‌توان با ایران به توافق رسید؟
🔻
ترامپ:
بله، می‌توان. ببینید، دارم اعتمادم را به آن‌ها از دست می‌دهم، چون دروغ می‌گویند و واقعیت را تحریف می‌کنند.
چند روز پیش پنج موشک شلیک شد. ما آن‌ها را ساقط کردیم، اما در میانه مذاکره بودیم. منتظر تماس استیو بودم تا ببینم مذاکرات چگونه پیش می‌رود؛ در عوض پیت تماس گرفت و گفت: «آن‌ها همین حالا پنج موشک به یکی از پایگاه‌های ما در اردن شلیک کردند.»
خوشبختانه نیروهای ما تجهیزات را به کار انداختند. کارکردن با این تجهیزات بسیار پیچیده است. از این افراد می‌پرسید کجا درس خوانده‌اند و پاسخ می‌دهند ام‌آی‌تی یا کلتک؛ دانشگاه‌هایی که معمولاً با نیروهای نظامی تداعی نمی‌شوند.
افرادی فوق‌العاده باهوش این تجهیزات را اداره می‌کنند. وقتی چنین افرادی نباشند، شلیک‌ها خطا می‌رود، سامانه ایمنی خطا می‌کند یا دقت کافی وجود ندارد. ما افراد فوق‌العاده‌ای داریم.
فکرش را بکنید؛ چند ماه پیش در یک بازه کوتاه ۱۱۱ موشک به سوی ناو هواپیمابر آبراهام لینکلن شلیک شد؛ ناوی بزرگ و زیبا و از نظر طراحی یکی از زیباترین کشتی‌ها.
هر ۱۱۱ موشک مدت‌ها پیش از رسیدن به ناو ساقط شدند. در چند مورد تقریباً همان لحظه‌ای که پرتاب شدند، سرنگون شدند. فناوری باورنکردنی‌ای است.
ناوی که میلیاردها دلار ارزش دارد و موشک‌ها به سوی آن در حرکت‌اند؛ هر ۱۱۱ موشک ساقط شدند. من با افرادی که این کار را انجام دادند صحبت کردم. دوست دارم به افراد پاداش بدهم؛ من رئیس‌جمهورم و با آن‌ها تماس می‌گیرم. آن‌ها کاملاً خونسرد بودند.
🔻
خبرنگار:
آقای رئیس‌جمهور، در دو هفته گذشته سنتکام حملاتی انجام داده است. سنتکام گفته هدف این حملات کاهش توان ایران برای مختل‌کردن تردد در تنگه هرمز بوده است. چند حمله دیگر لازم است تا این توان به‌طور چشمگیری کاهش یابد؟
🔺
ترامپ:
هیچ‌وقت نمی‌توان دانست. بیشتر مردم تا الان تسلیم شده بودند. آن‌ها دیگر نیروی دریایی یا نیروی هوایی ندارند. بیشتر مردم تسلیم می‌شدند، اما آن‌ها نشده‌اند. از این بابت به آن‌ها اعتبار می‌دهم. سرسخت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77678" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J0s3aGFGJXmnhhmYDTa82-W6_j-WvTEpwb_bRL7irRi-V78g-rAg0_C2XmDRNtpVOrMM2QKop3mt4PI5m7dvbxaAHgxw2UARghE3euHgbD0GMke7Fd1XKc6iBaMM8HW_l0tSgRRTktH-9YMMSbLn_qNyhFpROCIzkAH8crhOu-m3X4dDcV66GuHht42uNI8XzK6LToL7Gg5vc1gsiCMMu7Pxpweqk2t_tL-jnfagL-FOnDMLHSxb9y7pi3t5Lk3u5A-0RF1HgEF5OGgHYT5UmBymf1jfLL41kHsa2x7-x0J-CiBK3_hLoeBpOpLCcBzRPH_ONDj0_TFz69crnlSDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
✅
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77677" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbjc4636Le8hnXLuVuLX-oDkre_OD6i1n2tyBRbbgZLFCGe3eg4rbNMGIswcsi5YXV1OU98f6MiPXE6D3J4jkPxjVwYXS5esnxf8RHNaJTv11f4WfmT-IR4mj-j9nVIelr-xVPwwOlKAbeyfcOhtu4RVuCggDEJ4JrYr5QyyL8NnFPuPlISvalcDjapQeOLALmcA7Ufi5ECsNASHx0g63ieW82xgQLwy_Vz97Sj3EQvw3eAMpmLsmXSrrKRdJ8MCcAICZk5niqwx2QTAILwuunHUhkah-qHAdtKUJEQVRM2u00o7Fm4dcbMVptA5ZV_faCH1Yd5sH8j2rq9IK8tjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دوروف، بنیان‌گذار تلگرام، یک روز پس از آنکه اعلام کرد روسیه او را به دلیل مخالفت با درخواست‌های این کشور برای اعمال سانسور و نظارت گسترده بر کاربران، در فهرست «تروریست‌ها» قرار داده است، با انتشار تصویری از ملاقات مقام‌های طالبان با سرگئی لاوروف، وزیر خارجه روسیه، به این اقدام واکنش نشان داد.
دوروف در این تصویر که در شبکه اجتماعی ایکس به اشتراک گذاشت، عکس خود را با برچسب تروریست، کنار تصویری از دیدار مقام‌های روسیه با مقام‌های طالبان قرار داد و زیر عکس دوم نوشت: «شرکای مورداحترام» و برای عنوان این تصویر از عبارت «گیج نشوید» استفاده کرد.
دوروف پیش‌تر در ایکس خبر داده بود که روسیه به دلیل خودداری او از اجرای خواسته‌های این کشور برای نظارت گسترده و سانسور در تلگرام، نامش را در فهرست «تروریست‌ها» قرار داده است.
او همچنین به کنایه نوشت که بر اساس قوانین روسیه از «انتشار اطلاعات در اینترنت» منع شده است و افزود: «به نظر می‌رسد مقام‌های روسیه درباره اینکه چه کسی می‌تواند چه کسی را از اینترنت محروم کند، دچار سردرگمی شده‌اند.»
روسیه تنها کشور جهان است که رژیم طالبان را به رسمیت شناخته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77676" target="_blank">📅 19:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORCDGxxoBvV0_Up-pYqBchw9TKcolRlo6Kh3DPUCVRPgWdLCeF6HfwM2_hkxLl8B9738Q0DBQp8xp_2eFpsCiT7TMngYXaMl2_Us_iwQUPNFzGoZcZPFrNmZ9xZYVDSbH2vzEc5KIPlXZgcAqLN1fkz_PaoW83aC9u5y54UBHdtQOhy0rsBN2XGILk05PxJH238eAZwpiHE41F2kuRrPiwZyYsvh_sBffLLo2yF2FwNByBKFaBaxJioz2jo9CR-JoepYDlxC_YyguZIKBja_PV5sQxCyf_oOhkUvNtJp7_JOdurRTXEt5jLlTG-gykbgyrokAGvikNy6sJ37_w7L-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن عاملی، امام جمعه اردبیل، در خطبه‌های نماز جمعه این شهر گفت: «نتانیاهو در دیدار با ترامپ گفته قدر مرا بدان، من جلوی موشکهای جمهوری اسلامی را گرفته‌ام. ایران موشک هشت هزار کیلومتری دارد و به راحتی می‌تواند خانه تو را با موشک بزند. من جلوی ایران را گرفته‌ام.»
او ادامه داد: «ترامپ همیشه از نتانیاهو گول خورده و حالا محل بحث است که آیا این بار هم گول خواهد خورد یا نه.»
امام جمعه اردبیل افزود: «ترامپ پهلوان رسانه‌ای است، عملیات ما کمر او را شکست. او هر وقت شکست می‌خورد به جنگ رسانه‌ای پناه می‌برد و خود را پیروز میدان نشان می‌دهد. اگر این کار را نکند دق می‌کند و می‌میرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77675" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efZN4rHg_X0kfUtJnlPqkUcNJaXe1IuzzAY6dQdhpS4oNYBfd_SmYo1YRGteblWjtO7gg9p0ETRyX6OOcP-TrMK0B7hYc_ahhHnIWXkuTRgz4lysP2OOEcJDHCE8EXWzYuL0SeebpW1osaHJP26RpzbP3k7w1ZIAmV4QM9Mpg7OR9NR5gj_j0Zh5PkeHdIRE2-cCNiw-VmS8DutJCl5XgnRPgM9Inu6SuJiXcxaSTlg_pTsZKh7-pD6PAkUaF4g9O2ROe84kZrvsAA6Tpwb7RAzrNifmepoAaaJCXgIxOeNzPU2a8E7D1FS3s_ryhaK_F37HAOTuNaZIoaDZ7XkSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس‌جمهور آمریکا، روز جمعه ۹مرداد۱۴۰۵ در گفتگو با شبکه «فاکس‌نیوز» گفت درگیری با ایران «به‌خوبی پیش می‌رود» و با اشاره به حملات ارتش ایالات متحده اعلام کرد که ایران در نهایت چاره ای جز عقب‌نشینی و تسلیم نخواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77674" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx1yLW961Sco_wcjYTf6Ji5iTHTG-R-ld2HE-YBmRO6ln5E-15SHISKYN9FGRmT9Anbxsq6ZERQfLYj0jIvBq9aPu5bFSo2_m2TPBYsvulIp2aYMJ7Qa80kfPw5QwrMYtc_Zt8_kuCG_NmONn8YpXvpdDFhgK1xW3pGjzZ6GMjvpux3TNoEfu0MjgCnw5IIYV6SGnjGsqIWccj_Nj_tPuC56Z07xgVEAFJUVv12UlFbPOihEJGn60ibkDZjiN-TpmdOjSoodFSHJlNGJQMYlC9U97YwrtAX7-lUbxxa3BxfcKlV67nQVcTcQHaOpETPq2bkqJdGzGOc4Vzv-FeSjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز جاری و در میانه تشدید تنش‌های خاورمیانه، نشست کابینه خود را در اقامتگاه کمپ دیوید برگزار می‌کند.
این نشست در شرایطی برگزار می‌شود که دونالد ترامپ در تلاش است راهی برای پایان دادن به جنگ با ایران پیدا کند و همزمان قیمت بنزین را که به تهدیدی برای جمهوری‌خواهان در انتخابات میان‌دوره‌ای نوامبر تبدیل شده، کاهش دهد.
انتظار می‌رود سیاست خارجی و موضوع جمهوری اسلامی بخش عمده دستور کار این نشست را تشکیل دهد. ترامپ درگیر حملات متقابل علیه اهداف نظامی در ایران است.
ترامپ برخلاف برخی رؤسای جمهوری پیشین، در دوره ریاست‌جمهوری خود کمتر به این اقامتگاه کوهستانی ریاست‌جمهوری در غرب ایالت مریلند رفته، و این سومین سفر او به کمپ دیوید در دوره دوم ریاست‌جمهوری‌اش خواهد بود.
@
VahidHeadline
چون جمعه هم هست و بازارهای مالی تعطیل میشن باعث توجه بیشتر هم شده. دیشب، توییتر:
فردا ترامپ قبل از رفتن به باشگاه گلفش در بدمینستر، توقفی در کمپ دیوید داره. در هر دو باری که به کمپ دیوید رفته اتفاق خاصی افتاده. اولینش حمله بمب‌افکن‌های B-2 به نطنز بهمراه داشت، دومیش هم توافق با رژیم...
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77673" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0IGc7TYv_d5gRLygW13qnMjZrpuk_M8CENaBGrdlJT6udRwZQDNYrKdquHgIEvYLXuH5GgO8BZ1mWQedwIzLZoZo6nPj3M8kSVrtC1he1_2_y8erWf7AuKPlNJQr8Z0UrCvb5ERmHxQzSqMcTZlSJVElp8_AscG6r5D5CZD3ntyboPSKZyCgvvXEkMWWNAFoxL7In-4nPScxDhC8d5d3hDq4akUA9mVMXHqbEFB7z6QSz5Q0oExhBE8cyHz7BvwXC5kC8vNJlv1x8KjPdw7MCCEHJ9Umk9v4VjlrtpK7vlYOeEz6vsPWV30DED9bqTvcHVVXAz7s9TbdYgDaALEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی رسمی وزارت دفاع کویت اعلام کرد نیروهای مسلح این کشور، بامداد روز جمعه نهم مرداد ماه، چند پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده و آنها را منهدم کرده‌اند.
سعود عبدالعزیز العتیبی در بیانیه‌ای در شبکه اجتماعی ایکس نوشت: «تجاوز گناه‌آلود ایران تعدادی از تاسیسات حیاتی و نظامی را هدف قرار داد که اهداف متخاصم رهگیری و منهدم شدند.»
او افزود: «در نتیجه سقوط ترکش‌ها، خسارت‌های مادی وارد شد، اما هیچ تلفات انسانی ثبت نشده است.»
پیش از این بیانیه، ارتش جمهوری اسلامی با انتشار اطلاعیه‌ای از حمله به پایگاه احمد الجابر، محل استقرار ارتش آمریکا با «پهپادهای انهدامی» خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77672" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwrR6sQKr0BPLjQZgrPM9EbmTnhpTAQuSKbZT9nU3Z6uZZSlkxbo31G-7GZi9LHU2ZYtBcqcFz6w1WP1HU8qYSgTqQALogfbjSvNXEaSm-7SbOOBDto4w_HpvEPZYDofvymTFWeJX0P20OVjP-gOWBf7-zilVinrbLWEz2hQLCLbRP-JgzLOWk2OSB8TyNvHVetMTtd3S9-8Dp-0U9e1oKBqgbWw9X5lUTDXbnqMrPtWqne97qSppmPyl9k1Hp4wfqBGNJSeotEBco8uZlHwF4U4ImQGzDo73o0KQQ_UxRYdfyAT5syJNTsf0_CQGT_eRjBPcERzpy5T5aB-kkrIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، در پی اعلام فرماندهی مرکزی ارتش آمریکا مبنی بر تکذیب ادعای سپاه دربارهٔ بسته بودن تنگه هرمز، با انتشار بیانیه‌ای دیگر با پافشاری بر ادعاهای قبلی‌اش گفت به دو نفتکش دیگر حمله و آن‌ها را متوقف کرده است.
سپاه در کنار این بیانیه که روز جمعه نهم مرداد منتشر شد، همچنین تصاویری از یک نفتکش را که در میان شعله‌های آتش در تاریکی می‌سوزد منتشر و تاریخ آن را روز جمعه اعلام کرد.
سنتکام بعدازظهر پنج‌شنبه سه ادعای مطرح‌شده از سوی سپاه پاسداران و رسانه‌های نزدیک به آن دربارهٔ بسته بودن تنگه هرمز، انهدام سه جنگنده اف-۳۵ و عبور یک نفتکش ایرانی از محاصره دریایی آمریکا را را «نادرست» خوانده و گفته بود این ادعاها با واقعیت مطابقت ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77671" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=TsceFqVH_lLdObtGDFF29rjmzKZzNoiTLD5PesxDR1fTSMMvKygYhib25APP2DTkwag69ZxQ-Z918ExuckDmaxqas20M5j5MAbLm02992786hWLowJrLEaptTxQKlxIS1QG50wZcOHn-hmchrOtJqUt-pg6lbYjnS0HQ15e8EWvSnA8eX46EhJl2GCrcSIZcxiIhCNKqQztyfuZnlcCmuGpp2htoU1cbSr0UgqzQn4z5b4OHUabA82PfWN8YygUI3qaceQJykQT3pvQVNzHm9mlEt2Bk-NUNzabv207c0pE1B30iMILTC-IvLiAHkgFOLXX8xOVWrRR5mZw21QkAyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=TsceFqVH_lLdObtGDFF29rjmzKZzNoiTLD5PesxDR1fTSMMvKygYhib25APP2DTkwag69ZxQ-Z918ExuckDmaxqas20M5j5MAbLm02992786hWLowJrLEaptTxQKlxIS1QG50wZcOHn-hmchrOtJqUt-pg6lbYjnS0HQ15e8EWvSnA8eX46EhJl2GCrcSIZcxiIhCNKqQztyfuZnlcCmuGpp2htoU1cbSr0UgqzQn4z5b4OHUabA82PfWN8YygUI3qaceQJykQT3pvQVNzHm9mlEt2Bk-NUNzabv207c0pE1B30iMILTC-IvLiAHkgFOLXX8xOVWrRR5mZw21QkAyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌تر در صبح جمعه:
ارتش جمهوری اسلامی ایران مدعی شده است بامداد جمعه ۹ مرداد، پایگاه هوایی احمدالجابر در کویت را با پهپادهای انهدامی هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای اعلام کرد در این حمله، آشیانه جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات ارتش آمریکا در این پایگاه هدف قرار گرفته‌اند. این ادعا تاکنون از سوی فرماندهی مرکزی آمریکا، سنتکام، یا مقام‌های کویتی تایید نشده است.
احمدالجابر یکی از پایگاه‌های مورد استفاده ارتش آمریکا در کویت است و در گذشته نیز ارتش جمهوری اسلامی بارها از حمله پهپادی به مواضع آمریکا در این کشور خبر داده است. در یکی از حملات پیشین، ارتش جمهوری اسلامی مدعی شده بود ساختمان‌های اداری و سامانه‌های جهت‌یاب در پایگاه عریفجان، محل استقرار بالگردها در اردوگاه العدیری و ساختمان استقرار نیروهای آمریکایی در احمدالجابر را هدف قرار داده است.
ارتش جمهوری اسلامی حمله ادعایی بامداد جمعه را واکنشی به حملات اخیر آمریکا به ایران توصیف کرده است. رسانه‌های ایران پیشتر از حمله آمریکا به بخش‌هایی از جزیره قشم و کشته شدن شماری از غیرنظامیان در این حملات خبر داده بودند.
با این حال، تا زمان انتشار این گزارش، مقام‌های آمریکایی و کویتی درباره وقوع حمله یا میزان خسارت احتمالی آن اظهار نظر رسمی نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77670" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NqCTEqv16YDudusLk95_zZXsfRX1H2KAOGcz5UKZueY10ie_sAZNWBRPhrHh006muiLQp0bLnkBRevNduE4PYt_qyzSB7O5aD0kwHJZC7KicGsSdickwrTSZw0IiOCiA8bN5VxenXGg2T9UrJ1k7rZd44d_SyqpmQb8bBT5IDVjyTXrlR64JLhVXRk_MMvZlXrYrHnm5XclLp7Z0a8JCBbB1XMD9OAma6A51B_vcjZZQfv0Eb6jAM0KFfK0sEsrbtXJ7rPtVoFbZzF60fEr-KN4kSPfGJypywCWc6m_UPH61Y_Qw6O2pBNcSEQ5XLklgXkysfWGkqF_6TE8KCiPTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IL7tE9DXsi7ftVTGKbTfbcDB2bZwh6pN8UAUpCHH8wxxeCDAEuXL7ysVBpnIDuRHYJ0MMfbsz8D7jqlITSC7SI0E0fOYorrQ7DWL9z87wHHXiC4MeRyY0cFys8UpRH-3eaOelvzCO02ODrdZWk4lt7VMLlcAhsEpFiApn2JwwgKZg_GgonQL26fNdInUpC0v2QlydJtcYpsujKK5PFEb9fZRUphogC-h3ywMhX_qz79mTLzlMmw4HLOr2alSGeFNoxd1nfFGkVLqvhVES5zUHh1dhh4WJ6PPrBLY4GA0yIpWkhFpdb5BYDvZSxpda_0DMScywT_zVBxiSJcAk2etlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D4jFpcCownOEUFjBy0LtZry-RElXum1ono-Bx1vzm2zdMjWM-BBS3y-HWKAcI7-95Gj3frNCowlXdAKUzkRKuZ2T-Xg1t7OuABsq9soAfp03Qaz3tt_48WInmTd2NWNtxLlrJAZlEI6bWL-l-JBBEWPGiPYVSaj2R0Z6UABTPIhTAY4hkY2c6BVUAf-D09oZMPo-H7jsNT1p_Oy9uFvfMoXX6qS5ffeJdqXwitxJenyO6ARV1rXEOTonNLA7MG3UFCdBL2tCFQHzK-m4IGDPix627sLgNBVf15IkmYtMkdvVOSKwuQ8LS7KAWJmFcQqajeeIN5BOi9ROfy4axbunTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOnZEjH6oE_q47RA5C96Ook0Iiq1wwN3T2wWeIs_STGhFezrbLomQUma-ghnQXjZeJSfCWK51OyV0ndQH-UF3dVIRoqwT0kiAKG5RyKIbrHXUOJiJavrw8UsXmxAi6gfx6dJtvpv8bsIYasWYo12ASlUzX3eD2dJbQGpQ-zljiCowCrq6qQ3HMxKj_G-AF84kXTqCUChMi27BAgeS52z9IYCvRtt_xIX3nX6iDy1jVAixeJivRodxmtL3u411sJt1b4kYhzvAz2hT8qc9JDWNHbdh3GxwgD5CZxVn_SV6VAl5GT1qHgBKXyx13b1lEAKW0G4JOYlt2wcaHNw_gUWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ggvoIpjtt1lrQDy53NeouKgD4wAn8Y8jX7SAkBaq_oszaJ7oiwvlAcLFGpC3DQaL_whKxSF6IbVEuK49unn38wXKm6JnnsE-58Us1veLyjXmnQn1zZQUhxlgYp5dEGuydwuaHMJpPWX5Qpih9kTznZRLWTz3ELTe-xAo_VmP8Ihh4tcpzwbiI2XjpSB8pLlwZiSlwGRs59cETH_0XepXa0WV9-nh-BFnPD6K8RlwAjH6Qk_vrBz3V_oUJXeub4vXvwQUime-Kv2UE2BNjolKmw-4fFZpNQU7FUNkfzlcu0y5KlLhd6yHK_NC13Pva8bHKjQl_gDkniZYmUfk_-sBeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=HAB16HlWqMjc9GP6qiTq5HABZcUV6qYNX6ynKQYoUu_OySDWL5F16gSnz3YiEXFrK0J7YOBdjO3vWIiY9nN83uK01BzIXTXHr8bSyeQI7ik1dKVHF_RKj4idnDcbYgSa98IIMaol07ts_EwClGFITXpSxMTDVzsa3xY-qXuDees7bBJ_KaFtp1G7vj-AoAqvpdd0hfFf_3GwlbiH_ADCEYUs7YQkk-gl6kbIJ2vJCJ7RHk06eqkecCIHuXYttQbcfOdNgkuVNArCewuNVl3QOc4brDlKUGlf0tq5RBURqu_P22t6oQqBE7ORSTsf5fPKFS46thhzGxPyctgygxL_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=HAB16HlWqMjc9GP6qiTq5HABZcUV6qYNX6ynKQYoUu_OySDWL5F16gSnz3YiEXFrK0J7YOBdjO3vWIiY9nN83uK01BzIXTXHr8bSyeQI7ik1dKVHF_RKj4idnDcbYgSa98IIMaol07ts_EwClGFITXpSxMTDVzsa3xY-qXuDees7bBJ_KaFtp1G7vj-AoAqvpdd0hfFf_3GwlbiH_ADCEYUs7YQkk-gl6kbIJ2vJCJ7RHk06eqkecCIHuXYttQbcfOdNgkuVNArCewuNVl3QOc4brDlKUGlf0tq5RBURqu_P22t6oQqBE7ORSTsf5fPKFS46thhzGxPyctgygxL_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۰:۳۷ درباره پرتاب موشک از یزد
همین الان از یزد موشک فرستادن ساعت10:37
۱۰:۳۵ پرتاب موشک از یزد
سلام الان موشک زدن از یزد
از یزد موشک بلند شد ۱۰:۳۷
از یزد موشک زدن الان
وحید جان همین الان ساعت ۱۰.۳۲ پرتاب موشک از یزد
وحید جان همین الان از یزد موشک زدن
جمعه ساعت ۱۰:۳۶
یزد ۱۰:۳۵ یه موشک زدن
بعد از مدت ها جالب بود سمت جنوب پرتاب شد
همین الان از یزد موشک شلیک کردن
۱۰:۳۷از یزد موشک زدن
همین الان از یزد موشک زدن
جمعه نهم امرداد ساعت۱۰/۳۰
سلام وحید جان همین الان از یزد موشک پرتاب شد
سلام خوبین الان موشک از یزد رفت
شلیک  یک موشک الان از یزد
وحید الان موشک از کشور یزد زدن
همین الان ساعت ۱۰.۳۶ دقیقه از یزد موشک زدن
شلیک موشک از یزد به سمت جنوب
ساعت ۱۰.۳۶
سلام ساعت ۱۰:۳۵ یک موشک از یزد بطرف جنوب کشور شلیک شد
از یزد موشک شلیک کردن ولی مسیر متفاوت از قبل بود
سمت بندر و جنوب میرفت
ساعت ۱۰:۴۰ صبح یزد  موشک پرتاب شد؛ صداش خیلی بلند بود
سلام جمعه ساعت ۱۰:۴۰ از یزد موشک پرتاب شد
۱۰:۳۷ از یزد موشک زدن جمعه ۹مرداد
سلام آقا وحید ۱۰:۴۲ از یزد موشک شلیک کردن
موشک از یزد زدند
وحید جان شلیک موشک از یزد
چند دقیقه پیش
ساعت ۱۰:۳۵ از یزد موشک زدن
از یزد همین الان موشک زدن
امروز جهتش سمت جنوب شرق بود
بر عکس روزای قبل که روی شهر رد میشد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77663" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اکسیوس:
ترجمه ماشین:
ترامپ از توافق «تاریخی» برای خلع سلاح حماس و بازسازی غزه تمجید کرد
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اعلام کرد که «هیئت صلح» او با حماس به توافقی دست یافته است که بر اساس آن، این گروه خلع سلاح می‌شود و کنترل امور غیرنظامی و امنیتی غزه به یک دولت جدید فلسطینی متشکل از تکنوکرات‌ها واگذار خواهد شد.
چرا اهمیت دارد:
در صورت اجرا، این توافق تحولی چشمگیر در طرح صلح ۲۰ ماده‌ای ترامپ برای غزه خواهد بود و مسیر بازسازی این منطقه ویران‌شده را هموار خواهد کرد.
▪️
اما این توافق مستلزم آن است که حماس و اسرائیل طی حدود هفت تا هشت ماه، مجموعه‌ای پیچیده از اقدامات متقابل و مستقل را که اجرای آن‌ها راستی‌آزمایی خواهد شد، به انجام برسانند.
▪️
مقام‌های اسرائیلی همچنان به‌شدت تردید دارند که حماس سلاح‌های خود را تحویل دهد؛ در همین حال، اظهارات یک مقام ارشد حماس نشان می‌دهد که ترتیب خلع سلاح و عقب‌نشینی اسرائیل همچنان ممکن است محل اختلاف باشد.
آنچه می‌گویند:
ترامپ عصر پنج‌شنبه در شبکه تروث سوشال نوشت: «امروز، هیئت صلح به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی گروه‌های مسلح دیگر در غزه دست یافت.»
▪️
او افزود: «این گامی عظیم به‌سوی صلح و امنیت پایدار است.»
وضعیت کنونی:
دو مقام آمریکایی گفتند حماس پس از چند ماه مذاکره با میانجی‌گری قطر، ترکیه و مصر که یک مقام ارشد دولت آمریکا آن را «بسیار حساس» توصیف کرد، با مفاد توافق موافقت کرده است.
▪️
این مقام ارشد آمریکایی گفت انتظار می‌رود اجرای توافق طی هفته‌های آینده آغاز شود.
▪️
یکی از مقام‌های هیئت صلح گفت این نخستین بار است که حماس و دیگر گروه‌های فلسطینی در غزه با غیرنظامی‌کردن این منطقه و واگذاری مسئولیت امنیت و خدمات غیرنظامی به یک دولت تکنوکرات موافقت کرده‌اند.
بر اساس این توافق،
حماس از هرگونه نقش در اداره غزه صرف‌نظر خواهد کرد. «کمیته ملی اداره غزه» موسوم به NCAG به‌عنوان جایگزینی برای حماس و تشکیلات خودگردان فلسطینی فعالیت خواهد کرد.
▪️
مقام ارشد آمریکایی گفت: «این ساختار به نفع مردم غزه خواهد بود.»
بررسی واقعیت:
غازی حمد، از مقام‌های حماس، در گفت‌وگو با الجزیره تأیید کرد که مذاکرات «دشوار» به توافق منجر شده است، اما توضیحات او بلافاصله پرسش‌هایی را درباره نحوه اجرای آن مطرح کرد.
▪️
حمد گفت: «ما پیش از عقب‌نشینی اسرائیل از نوار غزه هیچ اقدامی در زمینه خلع سلاح انجام نخواهیم داد.» او افزود که کمیته ملی اداره غزه بدون دخالت اسرائیل خلع سلاح را اجرا خواهد کرد.
▪️
این موضع ظاهراً با توصیف ترامپ از یک روند مرحله‌ای و «با ساختاری دقیق» تفاوت دارد؛ روندی که در آن، هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی می‌کنند.
▪️
مقام‌های آمریکایی و هیئت صلح گفتند اجرای توافق از طریق اقدامات متقابل و مستقلی که راستی‌آزمایی می‌شوند پیش خواهد رفت، هرچند اذعان کردند که جدول زمانی عقب‌نشینی اسرائیل هنوز در حال نهایی‌شدن است.
تصویر کلی:
بخش‌های وسیعی از غزه در جریان جنگ ویران شده و بیشتر جمعیت دو میلیون نفری آن همچنان در چادرها یا سرپناه‌های موقت زندگی می‌کنند.
▪️
مواد غذایی و دیگر کمک‌ها در حجم زیادی وارد غزه می‌شود، اما وضعیت انسانی همچنان وخیم است.
▪️
وزارت بهداشت غزه که تحت کنترل حماس است می‌گوید از زمان آتش‌بس ۱۰ اکتبر ۲۰۲۵، نزدیک به ۱۲۰۰ فلسطینی کشته شده‌اند. برخی از آن‌ها از نیروهای حماس بودند، اما بسیاری دیگر غیرنظامی، از جمله کودکان، بوده‌اند.
نگاهی نزدیک‌تر:
این توافق بر این اصل استوار است که غزه باید یک دولت، یک نظام حقوقی و یک مرجع امنیتی مشروع داشته باشد. انتظار می‌رود روند غیرنظامی‌سازی بین ۲۰۰ تا ۲۵۰ روز طول بکشد و هر بار در یکی از بخش‌های غزه اجرا شود.
▪️
پلیس غیرنظامی حماس ابتدا سلاح‌های خود را به یک نیروی پلیس جدید فلسطینی زیر نظر دولت تکنوکرات تحویل خواهد داد.
▪️
پس از آن، سلاح‌های سنگین حماس از رده خارج و در انبارهای امن نگهداری خواهد شد و تونل‌ها و کارخانه‌های تولید سلاح این گروه برچیده خواهد شد.
▪️
سلاح‌های سبک مطابق قوانین فلسطینی جمع‌آوری خواهد شد.
▪️
تمامی گروه‌های شبه‌نظامی دیگر در غزه، از جمله گروه‌های مخالف حماس که اسرائیل در جریان جنگ آن‌ها را مسلح کرده بود، نیز ملزم به تحویل سلاح‌های خود خواهند بود.
کمیته ملی اداره غزه
تنها زمانی کنترل هر منطقه را در دست خواهد گرفت که یک سازوکار نظارتی تأیید کند تعهدات مربوط به آن منطقه اجرا شده است.
▪️
مقام هیئت صلح گفت در پایان این روند، دولت تکنوکرات و نیروی پلیس آن انحصار سلاح در غزه را در اختیار خواهند داشت.
نحوه اجرا:
بر اساس توافق، یک نیروی بین‌المللی تثبیت‌کننده به آموزش پلیس جدید فلسطینی کمک خواهد کرد، در جمع‌آوری سلاح‌ها مشارکت خواهد داشت و میان مناطق تحت کنترل فلسطینی‌ها و نیروهای اسرائیلی مستقر خواهد شد.
▪️
یکی از مقام‌های هیئت صلح گفت این توافق بر مبنای «اعتماد صفر» طراحی شده است، زیرا حماس و اسرائیل از همان ابتدا به‌صراحت اعلام کردند که به یکدیگر اعتماد ندارند.
▪️
این روند تا زمانی که ناظران تأیید نکنند هر دو طرف به تعهدات خود عمل کرده‌اند، از یک مرحله به مرحله بعدی منتقل نخواهد شد.
▪️
این مقام گفت هدف آن است که از وضعیتی جلوگیری شود که دولت تکنوکرات در طول روز غزه را کنترل کند، اما گروه‌های مسلح شب‌ها همچنان قدرت را در دست داشته باشند.
طرف مقابل:
عقب‌نشینی اسرائیل به‌تدریج و بر اساس جدول زمانی‌ای انجام خواهد شد که هنوز در حال نهایی‌شدن است.
▪️
ترامپ گفت هم‌زمان با تکمیل خلع سلاح و برعهده‌گرفتن مسئولیت امنیت از سوی نیروی بین‌المللی و پلیس جدید فلسطینی، نیروهای اسرائیلی عقب‌نشینی خواهند کرد.
▪️
اسرائیل همچنین عملیات نظامی و ترورهای هدفمند در غزه را متوقف خواهد کرد، مگر در مواردی که تهدیدی قریب‌الوقوع وجود داشته باشد.
▪️
مقام هیئت صلح گفت: «تمامی فعالیت‌های نظامی در غزه باید متوقف شود؛ چه از سوی اسرائیل و چه از سوی حماس.»
پشت درهای بسته:
مقام ارشد آمریکایی گفت دولت ترامپ در تمام طول مذاکرات هماهنگی نزدیکی با اسرائیل داشته است.
▪️
دولت آمریکا همچنین قصد دارد با وجود تردید اسرائیل درباره خلع سلاح حماس، اطمینان حاصل کند که اسرائیل به تعهدات خود در چارچوب توافق عمل می‌کند.
▪️
این مقام گفت: «ما از اسرائیل چیزی جز اجرای تعهداتش در چارچوب طرح ۲۰ ماده‌ای نمی‌خواهیم.»
▪️
او افزود: «اگر آن‌ها این کار را انجام ندهند، رئیس‌جمهور ترامپ بسیار ناامید خواهد شد. فکر نمی‌کنم اسرائیلی‌ها در شرایط کنونی بخواهند تنش‌ها با ما را تشدید کنند.»
در پشت صحنه:
به گفته دو منبع آگاه از مذاکرات، مصر، قطر و ترکیه فشار شدیدی بر حماس وارد کردند تا این توافق را بپذیرد.
▪️
مقام‌های آمریکایی و دیگر افراد آگاه از مذاکرات گفتند حسن رشاد، رئیس دستگاه اطلاعاتی مصر، نقشی کلیدی داشت. او میزبان مذاکرات بود و رابطه نزدیکی با خلیل الحیه، رهبر سیاسی حماس، دارد.
نکته قابل‌توجه:
به گفته یک منبع آگاه از این دیدار، هیئتی از حماس در جریان سفر اخیر خود به ایران برای شرکت در مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، با مقام‌های ارشد سپاه پاسداران انقلاب اسلامی دیدار کرد.
▪️
این منبع گفت مقام‌های سپاه از حماس خواستند برای امضای توافق عجله نکند و با وقت‌کشی زمان بخرد.
▪️
یک مقام ارشد آمریکایی نیز مدعی شد ایران تلاش کرده است حماس را متقاعد کند که توافق را امضا نکند، اما گفت این گروه تصمیم گرفت به توصیه ایران گوش ندهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77662" target="_blank">📅 06:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3ZI6NGwifgMGJal05yaeaUzbR3VVRJAY4ybsQjx6UPML6gQjXYTF5C6ElyYS8eU895RZPfXK8ySfohTBQGnDf5263BTcLAIDA38EIhzx3mpbys7gOg5oX_TzxUYzgSTGD02V4jLF69lWnx1X9z_-p62ESfRNL5dCcFPkYXwX-aHZlujziad_RhBZ4iINAvND-VHv874NxcEYbbt0c24dHArjV743GNfQdUFwuQkEGHLjUiVjYwhrPPGumaYCORlgxlWk-3EcoNnebYXQ7B2BSvIgyVG_CO1E531hH3SyQKGm7Km2qN_Skb7S31nIkNYx-6q6WEG_LyWKbixUSlHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
امروز، «هیئت صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و همه گروه‌های مسلح دیگر در غزه دست یافت. این گامی عظیم به‌سوی صلح و امنیت پایدار است.
این توافق، گامی حیاتی در مسیر آن است که غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای کمک به مردم فلسطین، از نزدیک با هیئت صلح همکاری خواهد کرد. هم‌زمان، اسرائیل نیز از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به‌عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این توافق، نقطه عطف بزرگی در اجرای طرح ۲۰ ماده‌ای ترامپ است. این توافق در مراحلی که با دقت طراحی شده‌اند اجرا خواهد شد. هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات» با یک نیروی پلیس جدید فلسطینی همکاری خواهد کرد تا مسئولیت تأمین امنیت غزه برای ساکنان آن و همسایگانش را بر عهده بگیرد.
یک سال پیش، جنگی خشونت‌بار و مهارنشدنی، بحرانی انسانی و گروگان‌هایی در اسارت وحشیانه وجود داشت. ما پیشرفتی تاریخی کرده‌ایم و هنوز کارهای زیادی باقی مانده است.
می‌خواهم از میانجی‌ها—مصر، قطر و ترکیه—به‌خاطر تلاش‌های مهمشان تشکر کنم، و به‌ویژه از تیم فوق‌العاده‌ام که تلاش خستگی‌ناپذیرشان این دستاورد تاریخی را ممکن کرد.
تهدیدی که در ۷ اکتبر از غزه سر برآورد، اجازه نخواهد یافت دوباره شکل بگیرد!
بر اساس این توافق، غزه سرانجام در اختیار یک دولت جدید فلسطینی قرار خواهد گرفت که به مردم خود خدمت می‌کند.
این تحول شگفت‌انگیز را که همه می‌گفتند هرگز دست‌یافتنی نیست، به همگان تبریک می‌گویم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77661" target="_blank">📅 02:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9yXy3fSjxBMvaFG6ny9gBNwsxUlUBWBV442PWV6UEqZVVvHnUOd9AK-MLLIEPRYLS58eLPFmHOVorQHSq75J98kHTs61POKmJc4igh9Ehvl_mO7ZanUeZcNDXIFYIL9IQ2H-qLLrg9agfGmJosBkm7qEJoSUaxl4u9wD2wO5HM1o2-xKhLFnZD3QYMIo8vmo7K8qA2nmi3Y0kWppZhkMRMvwU6HlOKHdNuQAvBy2WCeXciJN2bjf3tqf987641d6mEDCiHPIWIoewlQ-jZ228M02cvZwIqa4VcUj09LVANz-Bsjh01konawI2yhdhNgZF_O515wb0DEoaCYD4mtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس اعلام کرد افرادی که به سپاه پاسداران انقلاب اسلامی یا هواپیمایی ماهان خدمات مالی، پشتیبانی لجستیکی یا حمایت تجاری ارائه می‌کنند، به تداوم فعالیت یک سازمان تروریستی کمک می‌کنند.
او افزود وزارت خزانه‌داری آمریکا به شناسایی این افراد، افشای هویت آن‌ها و قطع دسترسی‌شان به نظام مالی ایالات متحده ادامه خواهد داد.
پیش از این، وزارت خزانه‌داری آمریک، شش فرد و نهاد در ایران، چین، هند و روسیه را به دلیل همکاری با هواپیمایی ماهان و سپاه پاسداران تحریم کرده بود. واشنگتن اعلام کرده بود برخی از شرکت‌های تحریم‌شده به‌عنوان نمایندگان فروش هواپیمایی ماهان فعالیت می‌کردند و در حفظ شبکه بین‌المللی این شرکت نقش داشتند. وزارت خزانه‌داری آمریکا همچنین شرکت «استودیوی استارت‌آپ داده‌نگار» را به اتهام همکاری با سپاه پاسداران تحریم کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77660" target="_blank">📅 02:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
مصر دوست و شریکی مهم برای ما در منطقه است و امنیت آن برای ما از بالاترین اهمیت برخوردار است.
همه ما باید در برابر توطئه‌های اسرائیل و عملیات‌های پرچم دروغین که برای تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.
تهدید روشن و مشترک است و از همبستگی مسلمانان هراس دارد.
araghchi
پست قالیباف:
ایالات متحده هر روز دست خود را به جنایت جدیدی آلوده می‌کند؛ حملهٔ تروریستی به منازل مسکونی غیرنظامیان در جزیرهٔ قشم، ادامهٔ جنایات در میناب و لامرد است.
امریکایی‌ها عادت کرده‌اند که سیلی‌هایی را که در میدان نبرد می‌خورند با ریختن خون بی‌گناهان جبران کنند. تاوان‌ خواهند داد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77659" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_u-RNBvsYC6OxXDJcbNC8uvsNX-tVG_-qX67pnEPkD0sTKFWD0bNWJlSEwKoENH-U59l80Jz9hvHRKIzGvauAIr8xA9dcE19BBCyeSufpWU3eNbD4dqXLcAWrqI3zcIkNJD38k4ofbsWumWbutaL1znSLBTw4QGgCYPmdRLS_S12stcvqtKoHbsCyteynETKEbTBDSGA8nCh3uDsvHvorqh8NBap3g75sAO0-MIAIpX_R1xF3hYpalGYGrHHYi9gI6HDNXANaSXkw-qaLBnMsOkcaHThZW3XKS3PULAMhq0u967JLBgnVyTTu13-HxyBC4gmggPGc13Rhtb7EyWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی روز پنج‌شنبه از طرح تشکیل یک ائتلاف بین‌المللی برای دفاع دریایی با هدف حفاظت از کشتیرانی و مسیرهای انتقال انرژی در دریای سرخ خبر داد.
وزارت دفاع عربستان اعلام کرد نمایندگان ۴۳ کشور و اتحادیه اروپا در نشستی درباره این طرح شرکت کردند. بر اساس این پیشنهاد، عربستان به‌عنوان کشور بنیان‌گذار و رهبر ائتلاف عمل خواهد کرد و مقر آن نیز در این کشور خواهد بود.
به گفته وزارت دفاع عربستان، این ائتلاف با هدف تقویت امنیت دریایی، حفظ آزادی کشتیرانی، تأمین امنیت مسیرهای تجارت و انتقال انرژی و حفاظت از منافع مشترک دریایی در تنگه باب‌المندب و خلیج عدن تشکیل می‌شود.
این طرح پس از آن مطرح شده که حملات حوثی‌های مورد حمایت ایران به کشتی‌ها، یکی از مهم‌ترین مسیرهای تجاری جهان را با اختلال روبه‌رو کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77658" target="_blank">📅 22:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=Rkfm6d035sB9nnsdpHgRN7xHbP6-0Yt5t1qvmdNnAUHAWrg15QOJ-ByjmZU3_cz3ZYs0wkYXYXENz_jykSU9VAGL8arYuNpyAOHq7YX7PGQKjoHWnSW0qqhAUfKiW5FrJ8QVjc_cchqVPufiD9bNB2kWQbRhGxTIgnAYlim3tD6LMVtcECelGWBEWBIuMBSsYj5Sscobm0M6heKLiRxTu3rA67bVGi48LwiwVgChmLfAo45Bvrtsvomdhri7chfVXJSWx4c-CsWWcEGsNm5I0gMz0GNeDbm3tqC4WFuwa3xeK5E2HoR-D87GGrmIHcTqU0JDzNgVLz0V6n7s6wrDJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=Rkfm6d035sB9nnsdpHgRN7xHbP6-0Yt5t1qvmdNnAUHAWrg15QOJ-ByjmZU3_cz3ZYs0wkYXYXENz_jykSU9VAGL8arYuNpyAOHq7YX7PGQKjoHWnSW0qqhAUfKiW5FrJ8QVjc_cchqVPufiD9bNB2kWQbRhGxTIgnAYlim3tD6LMVtcECelGWBEWBIuMBSsYj5Sscobm0M6heKLiRxTu3rA67bVGi48LwiwVgChmLfAo45Bvrtsvomdhri7chfVXJSWx4c-CsWWcEGsNm5I0gMz0GNeDbm3tqC4WFuwa3xeK5E2HoR-D87GGrmIHcTqU0JDzNgVLz0V6n7s6wrDJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر جاویدنام آیدا حیدری، جوان معترض کشته‌شده به دست حکومت، در سالروز تولدش بر مزار او می‌گوید که آیدا حیدری «شیرزنی» بود که جانفدای میهن شد.
آیدا حیدری، دانشجوی رشته پزشکی دانشگاه علوم پزشکی تهران، در ۱۸ دی‌ماه ۱۴۰۴ در تهران با شلیک گلوله جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77657" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=NUBrFcjczg3aBj8GlxE8fYm6W6unCyRDL2y8yFm629_rhNnpk_O421EHKoRUxl_KlZBYpFdUvESCAQFIZ07aC6rgs5oh8zkqTQdWTg-TH0nRR9e2BoLCoSoQ6mDqhIHvJAPqYLwdehzuA30ZQBuK3BZCKpSzmcnhbj4hQjlmtRrjzolsHob-AINaEMFI7-lXERkwX-VEr85n2SoXqJoSj3QIrE8SEzGHizeJ9xl3eR0c8j81mDvME-7gPs_RB0_4mSOlxxx0peUMr4zUh1kNX0o4nDW8Jw53Ec8IA1FA0Gcv2cAClx1KJ55VG5PP2938Qam6bUn1J5KPpjtV9nSi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=NUBrFcjczg3aBj8GlxE8fYm6W6unCyRDL2y8yFm629_rhNnpk_O421EHKoRUxl_KlZBYpFdUvESCAQFIZ07aC6rgs5oh8zkqTQdWTg-TH0nRR9e2BoLCoSoQ6mDqhIHvJAPqYLwdehzuA30ZQBuK3BZCKpSzmcnhbj4hQjlmtRrjzolsHob-AINaEMFI7-lXERkwX-VEr85n2SoXqJoSj3QIrE8SEzGHizeJ9xl3eR0c8j81mDvME-7gPs_RB0_4mSOlxxx0peUMr4zUh1kNX0o4nDW8Jw53Ec8IA1FA0Gcv2cAClx1KJ55VG5PP2938Qam6bUn1J5KPpjtV9nSi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
در چند ساعت گذشته، رسانه‌های دولتی ایران همچنان ادعاهای دروغین سپاه پاسداران انقلاب اسلامی را منتشر کرده‌اند؛ به‌ویژه سه ادعای زیر:
🚫
ادعای نخست: سپاه پاسداران بار دیگر ادعا می‌کند که مسیرهای آزاد و باز عبور از تنگه هرمز برای کشتی‌های تجاری خطرناک است.
✅
واقعیت: خطرهای فوری برای کشتی‌های تجاری و خدمه غیرنظامی آن‌ها، تهدیدهای لفظی و تلاش‌های سپاه پاسداران برای حمله به آن‌هاست.
🚫
ادعای دوم: سپاه پاسداران مدعی است سه جنگنده رادارگریز اف-۳۵ آمریکا و سه هواپیمای دیگر در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✅
واقعیت: در تلاش‌های اخیر ایران برای حمله، هیچ هواپیمای آمریکایی منهدم یا آسیب‌دیده نشده است. همه موشک‌ها و پهپادها رهگیری شدند یا نتوانستند به مناطق هدف برسند.
🚫
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام M/T Nora محاصره آمریکا را شکسته است.
✅
واقعیت: این کشتی تجاری نتوانسته از محاصره «دیوار فولادین» آمریکا عبور کند. بیش از ۲۰ ناو جنگی آمریکا، صدها هواپیما و هزاران نیروی نظامی همچنان در آماده‌باش هستند و اجرای کامل محاصره را ادامه می‌دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77656" target="_blank">📅 19:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkqV9_zOt7sSLhHecMcGi8p-7TURsheMG34O2y05SMzkMX7ZMp3x7WPGWjqYZiSwhgUgCv0liJrXLPBAkjYlF9mxkHjG9Qn0SF3Ea8D7ZqDhgZhv-KuVbCv3tgx-RHmq3fKmI57jDwQJWBFclTKZho5Uc0zrqoI8XPp7okwyzy1tksJPYAvWXkj_p-YSjx1K95eypzBvBMFE3ZlQEOCd3IirJJ0t0VHPJ-UNJK05ov-NQOQZ69z7BZ5abRgLMKAzwY_LeYI-zYGd5LAFdIgqv_AJKxUcym6J6GN16fGrfiD7ANBCGU-XSWCgTetQfgzeH_ZmBe_wCQoXd8SZETn0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=k3d4wP5RbWVW-I2ecKXzzf2-ZokIdklawhhCZ2jbjPDTaPcX2TWrUq8dTcIgFWLBQmiGfyHatmA_hQCjIDDS98SepFXChEqrSa7P9W23GfSHbwMLu7JfFS1xfgwtCEBLpIUlVomLIMjS9RRqLqubnlwgzUxndnXI_2TmnRaT3FIgMUJ9xl9Wzx7RuM0TReD74L7iwd96vaTPaqCTEBEE728d3tpBZKu9Mx8H4Kl9xsqudLDWs00r1rxkuVnUrQxIlIk3brJnBN7jm3W-1WjjJe7Qc8XtngQkCeK202lDoCRZXCxS3k0nZOi-z8TBGWdj23z_ce2UpkL23AsvICswKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=k3d4wP5RbWVW-I2ecKXzzf2-ZokIdklawhhCZ2jbjPDTaPcX2TWrUq8dTcIgFWLBQmiGfyHatmA_hQCjIDDS98SepFXChEqrSa7P9W23GfSHbwMLu7JfFS1xfgwtCEBLpIUlVomLIMjS9RRqLqubnlwgzUxndnXI_2TmnRaT3FIgMUJ9xl9Wzx7RuM0TReD74L7iwd96vaTPaqCTEBEE728d3tpBZKu9Mx8H4Kl9xsqudLDWs00r1rxkuVnUrQxIlIk3brJnBN7jm3W-1WjjJe7Qc8XtngQkCeK202lDoCRZXCxS3k0nZOi-z8TBGWdj23z_ce2UpkL23AsvICswKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی قدیمی منتشرشده در شبکه‌های اجتماعی رقص علیرضا سپاهی در اصفهان را نشان می‌دهد.
قرار بود او بامداد سه‌شنبه اعدام شود اما پیش از انتقال به محل اجرای حکم دچار سکته قلبی شد و به بیمارستان الزهرای اصفهان انتقال یافت.
@
VahidOOnLine
یک شاهد عینی گفت پس از انتقال علیرضا سپاهی، معترض محکوم به اعدام، به بیمارستان الزهرا اصفهان، فضای بخشی از این بیمارستان امنیتی شده و شماری از ماموران امنیتی در آن مستقر شده‌اند.
بامداد سه‌شنبه، ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو نفر دیگر از بازداشت‌شدگان اعتراضات ۱۸ و ۱۹ دی‌ماه ۱۴۰۵ در اصفهان، با حکم دادگاه انقلاب اسلامی اصفهان اعدام شدند. ابوالفضل سپاهی بادجانی، پسرعموی علیرضا سپاهی بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77654" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec49421.mp4?token=AQ98RGlfgBwwOMn3l5HWB14XgZFQ58KV6t_jPjaIMS6EBggISG5FLsFu0_BokOTM_1-fqC70HX2aXKqpDXLqUSlRQo34EXpHXNfPjCbWNrolqKYVIpEZIGBS8WWNgdNuXR3jfF6C6Cq9CowVNGgoFvh2PPwZ_OJD6rUAByOhGT9CgCrxgupACmheonV5B0dt6YV9Gr8ZQjbKxBFm_eiA8joLAHDwWx32w0fFqfAxMmxbgHw4ICluNTdXDLZZXnCXECLdrHfwAnCQnqVQxUrdOakhxvfSZGncYUA4hsrkNWzQLElGT6zQsT0UtAsHLoEEGdFOl6zNk4Cpwf0_Wg-1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec49421.mp4?token=AQ98RGlfgBwwOMn3l5HWB14XgZFQ58KV6t_jPjaIMS6EBggISG5FLsFu0_BokOTM_1-fqC70HX2aXKqpDXLqUSlRQo34EXpHXNfPjCbWNrolqKYVIpEZIGBS8WWNgdNuXR3jfF6C6Cq9CowVNGgoFvh2PPwZ_OJD6rUAByOhGT9CgCrxgupACmheonV5B0dt6YV9Gr8ZQjbKxBFm_eiA8joLAHDwWx32w0fFqfAxMmxbgHw4ICluNTdXDLZZXnCXECLdrHfwAnCQnqVQxUrdOakhxvfSZGncYUA4hsrkNWzQLElGT6zQsT0UtAsHLoEEGdFOl6zNk4Cpwf0_Wg-1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار خانواده جاویدنام محسن رشیدی خانی‌آبادی و علی ایازی با خانواده عرفان اسفندیاری و امیر حسین صفری ـ گزارشگر (ویدیو صدا ندارد)
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77653" target="_blank">📅 19:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu7KBhh1dSZPbdaxApa-G5i5Dl6gccouidkwsbxwQZxUIKv3xxkrGsZEB1zGlO76Om_X2bUcqR1YHnvN_HPdZBIBj33jR8Z8BBurNX8thyG-s11pbOFBYjfQ9-yo3XvU3QzcEGKebafV2RynSN0_K2_v-AQapBinCo4lGzEhgtXJqRflFktkkXoCnCCtC9Ca5c7EM4JAt3SxS8Ap-_9YIBHr8dSCu78ws8nexD4vPGLufRFVDBl97TpIn1n3FytzZWrCeNWoiUDExhgmh-szUq7fHYCsiJKNN2ZQYXxbYyiEbD50EkCnYXJ7XZsQB0WcqM6OWm2vArjEfCv37mDLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ان‌بی‌سی نیوز روز پنجشنبه هشتم مرداد، به نقل از یک مقام آمریکایی گزارش داد که دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در جریان نشستی در هفته گذشته از فرسایشی شدن جنگ، محدودیت گزینه‌های نظامی علیه ایران و دست نیافتن به توافق خشمگین شده و بر سر مشاورانش فریاد کشیده است.
به گفته این مقام مسئول، بر خلاف اظهارات عمومی ترامپ مبنی بر رضایت از روند جنگ، نه او و نه مشاوران ارشدش از وضعیت موجود راضی نیستند. یکی از متحدان ترامپ در این باره گفت: «رئیس‌جمهور کلافه شده است؛ او تصور نمی‌کرد گرفتن امتیاز از ایران تا این حد دشوار باشد و هیچ راهبرد مشخصی برای چگونگی رسیدن به نقطه پایان وجود نداشت.»
این گزارش می‌افزاید نبود شفافیت درباره اهداف نهایی واشنگتن—از جمله این‌که آیا هدف اصلی جلوگیری از دستیابی ایران به سلاح هسته‌ای، بازگشایی تنگه هرمز یا نابودی برنامه‌های موشکی و پهپادی ایران است—برنامه‌ریزی برای پایان جنگ را دشوار کرده است. یک مقام آمریکایی تصریح کرد: «ما پیروزی‌های تاکتیکی متعددی داشته‌ایم، اما بدون داشتن یک راهبرد روشن، با یک شکست راهبردی روبه‌رو هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77652" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEBl-rkmLcntK4rBujV6oT1mgp3WUhRn2lqzwFTRGztYegRUnUd9EmIvDhiX31JCZC8vhWUH7n9IJzdYCKS-cN427XLBh-7SO6aGwalOdTNWWTyHpcao9mSB8lDvoDtldmbwxl4EwIkHbCDYgpZ1OpxNDqVTCPP14DY_ccBVVWO8w0vbfG2pd_xydS6mJmRwnKRokec06dX9BJ1I3IwzEiIXe53CC9E6OtyXXZ_jZ0QJ-pNGx0fsZJ_oZSMbeRL_fzDnsllySVqD5rTqKYPkUpWffHWNlTCkUuml9NNrlDMOqPb9t0YR6aq6SXw7htaK_reMYQApC4LSa6nK_GtF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌وزارت دفاع چین گزارش‌ها درباره برنامه آن کشور برای تحویل صدها سامانه پدافند هوایی دوش‌پرتاب به ایران را رد کرده و آن را «کاملا نادرست و خلاف واقع» خوانده است.
جیانگ بین، سخنگوی وزارت دفاع چین، روز پنجشنبه در پاسخ به پرسشی درباره این گزارش گفت که ادعای مطرح‌شده صحت ندارد. وزارت خارجه چین نیز پیش‌تر گزارش مربوط به این معامله را «بی‌اساس» توصیف کرده بود.
رویترز روز چهارشنبه به نقل از سه منبع آگاه گزارش داد که ایران قرار است ظرف چند هفته نخستین محموله از مجموع ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل ساخت چین را دریافت کند. به گفته این منابع، قرارداد مورد نظر شامل موشک‌های کیودبلیو-۱۲ و اف‌ان-۱۶ است و ارزش آن بین ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود.
بر اساس این گزارش، قرارداد با یک شرکت مستقر در هنگ‌کنگ امضا شده که گفته می‌شود میان ایران و تأمین‌کننده چینی نقش واسطه را ایفا کرده است. منابع رویترز گفتند که قرار بود محموله‌های اولیه از شهر ارومچی در غرب چین ارسال و از مسیر پاکستان به ایران منتقل شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77651" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dideEbWcAmHYJNRcVUz_4oqM0yEn-fuNXoZMa7i0mtpLL6J4EKueFECq6TAuC0LxJgdrxx-mZekjhJ8Lmg_fpVvsptjsBe4oCcJh-kBoPx61i2duIvYX8UwUu_vXTjUhYKJlRxUYYzPakmMNEBoa6ZIBojXKPJe9Gx378YuWE-M_fGSCLa2pq14qBUTThsaHnXCldvpnuIb0D_jS6ZOBz1UFyEZAGT_OlmnoQ1g91eug0qSJ1Wo-l1_q7a1QjC8Rqwk9edljn2ZsjPeJQiyLGlP9UaRfEZPIbC-f5h2DYK1cr86fZAzISVqSqiWDJdYxizbnDhoC_nbSQB_sHJQJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jCbqq_ZSanHFN4ja9QiX27R2nA7Qx6T20qj8iWFvTFTDL1c1iejUklcJ5Rx1B9UQ1Euy5yFT_FEomHVCB3PIOnlcCzQhgx-ndeeACVneOre3_9mKzvYvBILk4b9FTZjKUt3OrDaNUOTT90fzt23x809gQbQOEIbde48sZ-fMJL0sgn8NlkSxxq-_ff2ZgppZSUP9LqN-uNHWQCoBspqI5FdHu7hGGh2YarQfkefPF08MCQN68ATWsw2ZlllJKbPO2DycZc9DnLyjYAEev8jkwIJG_r8LK9hkyzWrPlUCmjIvh65zILpjAmiD-qZer-8XyBMlo9siiCSJPeoaPr70dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: با شکاف عمیقی که پس از کشتار دی‌ماه بین مردم و رژیم ایجاد شد؛ حکومت ایران در نهایت سقوط می‌کند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در پاسخ به مجری ای‌بی‌سی که به او گفت طبق گزارش نیویورک‌تایمز شما به ترامپ گفته بودید که ظرفیت موشکی حکومت ایران ظرف چند هفته نابود می‌شود و تغییر رژیم ممکن است رخ دهد، گفت: این ارزیابی اولیه من نبود و این بیان نادرستی از آنچه گفتم است.
برآورد من این بود که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای اقدام کنیم.
نتانیاهو گفت، من گفته بودم که می‌توانیم شرایط را برای ضعیف‌تر شدن رژیم فراهم کنیم اما بر عهده مردم ایران خواهد بود که سرنوشت خود را تعیین کنند.
او درباره احتمال تغییر حکومت در ایران گفت: «فکر می‌کنم ایران از همیشه ضعیف‌تر و اسرائیل از همیشه قوی‌تر است، اما نمی‌توانم بگویم رژیم هم‌اکنون فروپاشیده است.»
نتانیاهو گفت: بگذارید یک پیش‌بینی کنم؛ پس از چنین شکاف بزرگی که به دنبال آن قتل‌عام (کشتار ۱۸ و ۱۹ دی‌ماه ۱۴۰۴) بین مردم و رژیم ایجاد شده، فکر می‌کنم که رژیم ایران در نهایت سقوط خواهد کرد.
نتانیاهو هشدار داد اگر ایران، اسرائیل را هدف حمله قرار دهد، «اشتباهی بسیار خطرناک» مرتکب خواهد شد و اسرائیل «بسیار شدید» پاسخ خواهد داد.
او در پایان گفت: «هدف من این است که مطمئن شوم ایران با این حکومت به سلاح هسته‌ای دست پیدا نمی‌کند. این موضوعی است که من و رئیس‌جمهور ترامپ هر دو بر سر آن توافق داریم، زیرا در آن صورت جهان متفاوتی خواهد بود.»
@
VahidOOnLine
نخست‌وزیر اسرائیل روز چهارشنبه در گفت‌وگویی اختصاصی با لینزی دیویس از شبکه ای‌بی‌سی نیوز تأکید کرد که دونالد ترامپ تصمیم‌گیرنده اصلی درباره جنگ ایران است و او تلاش نمی‌کند ترامپ را برای ادامه حملات علیه ایران متقاعد کند.
نتانیاهو در عین حال گفت نسبت به امکان دستیابی به راه‌حل دیپلماتیک با جمهوری اسلامی تردید دارد.
او گفت: «نمی‌دانم این احتمال کم است یا نه، اما نسبت به شیوه عمل ایران بدبینم. آن‌ها همیشه دروغ می‌گویند، تقلب می‌کنند و زمان می‌خرند. آیا تحت فشار کافی ــ فشار دیپلماتیک و اقتصادی ــ ممکن است این رفتار تغییر کند؟ می‌توان امتحان کرد.»
او افزود: «واقعیت این است که ما شریک و متحد هستیم. او شریک ارشد است؛ فراموش نکنیم که او رئیس‌جمهور ایالات متحده آمریکاست و من شریک کوچک‌تر هستم. اما من نخست‌وزیر اسرائیل هستم و هر زمان لازم باشد از منافع و امنیت کشورم دفاع می‌کنم.»
نتانیاهو همچنین از نقش دولت ترامپ در مقابله با «دشمن مشترک» قدردانی کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77649" target="_blank">📅 19:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8X1KIanwudtN3FXmsmTJrqfq3UfZY3yGwGbJFvDuC8fzYugOobBMUmLjduYD3Qpfi1bCLN0pxB2T2D-vWYQq9Q8OWBql-c15XNIjrUHAF8Ylk3rFaCBS7c-C_LUlFiwmvk0shqquBEt3Ct7vsW0sLZBVoTvsT_jTyvfS5C28670pwkS1xQMC3OtBKxxz_lCphIhVTslgamgsmXWX9RaNr5Qgsmcus1t1tMn8J8Zd1ReuTpbhufK9Jwiwj-ML--1fdV-PXVB7D49oJesIh0hdXqI4bNx8DnijBAPj_EeP2uCrNLdoVnertqkzJ7V5f2Wxwoxh1k--hvFQtKC1jOVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار ویدیویی از ضرب‌وشتم چند زن در ایران در جریان یک پخش زنده اینستاگرامی، موجی از واکنش‌ها را در فضای مجازی به دنبال داشته است.
به‌ گزارش خبرگزاری میزان، وابسته به قوه قضائیه ایران، پس از انتشار ویدیوی این لایو اینستاگرامی با دستور مقام قضایی برای این فرد پرونده تشکیل شده است.
سعید راستی، معاون بخش «مبارزه با شرارت و جرایم خشن» پلیس اعلام کرد که این ویدیو باعث واکنش گسترده شهروندان شده و اطلاعات ارسالی مردم در شناسایی متهم نقش داشته است.
آقای راستی اضاف کرد که این فرد بامداد پنجشنبه، ۸ مرداد ۱۴۰۵، «در عملیاتی» در مرکز تهران شناسایی شد و «به دلیل مقاومت در برابر ماموران» دو گلوله به پاها و یک گلوله به دست او شلیک شده و در پی آن بازداشت شده است.
هم‌زمان، ویدیوهایی از این فرد پس از بازداشت در شبکه‌های اجتماعی منتشر شده است که او را در یک مرکز درمانی نشان می‌دهد. در یکی از این ویدیوها، او در حضور پلیس از زنانی که در ویدیوی ضرب و شتم دیده می‌شوند و همچنین از  شهروندان و پلیس عذرخواهی می‌کند.
@
VahidHeadline
دیروز بارها اون ویدیو رو برای من فرستاده بودند و می‌خواستند پخش بشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77648" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAAsBPM8TYsbZ3j-Q-IisD76W6ROGJiTGMn_b7VzV_ImhHvadbRTtXTBfSkWX3gwxFiyGFp71SwkfPHTlncK9ojcUwPtIK3d0gB11bOnNNeZnd1wzXWclxxrXibKRBvrnZZXhtas-8zcLq1O6eXO0v7AqnCeprPK-V50ICxcY26d270ZSKA7W4KnGMkwSY9eZdofzKs4pdU2GDJzDrMGN891Ax5WGBWePq1Y2adRbBiSJ9ksTM3iIH9cm7WSk9sZ9ujihtpixJJ6-Mwq-a6fDwpax2A7d_K6aX1VUjOvJyxYEAbwP_vjpq6N9LJ49hDdG8Et_UB_x8fjkMGvxn9pxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی (آرمین) جنت‌خواه، فعال شبکه‌های اجتماعی، برای اجرای حکم قطعی سه سال حبس بازداشت و به زندان فشافویه منتقل شده است.
بر اساس این اطلاعات، آرمین جنت‌خواه روز ۳۰ تیر ۱۴۰۵ بازداشت و پس از انتقال به زندان فشافویه، اجرای حکم سه سال حبس او آغاز شده است.
اتهام منتسب به او در پرونده قضایی، «تحکیم مواضع اسرائیل» عنوان شده است.
جنت‌خواه پیش‌تر نیز در دی‌ماه ۱۴۰۲ توسط نیروهای امنیتی بازداشت شده بود. جزئیات مربوط به روند رسیدگی به پرونده و نحوه صدور حکم او به‌طور رسمی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77647" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeC_fjjCjPmPlQK7k5Fyc2esVzx9-5zfBo7pCNNlrGrEcwC0WPxZE_ExrBUP1pWzpP-bhwt7Y7SXf_2x6ftrHBF7EHOWr4sI-f1trqA5R_O3py1dtUpSQFEx5IB3raZB7Vvmmc83JgL8RWhEjXIBpSc8e-x0vOWQoEPx-5d9nYkmfA2iHEIGdTjNoRCH4h0s1Uahs8tt8cuFVJEHLysBovQB83lm9ZZr4kzTc7oCtxa1YlQ30owsE07hXdjNygx4epGvEheEi3ARKdeOUoH_ALSkItfNnTm1AemLzaShK2P651vJ_tSsIKRgYMKrW4r5cDxynXGJDux9odALyu4l0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران زنجان با انتشار بیانیه‌ای از کشته شدن سه نیروی این نهاد نظامی در حملات بامداد پنجشنبۀ آمریکا به نقاطی از ایران خبر داد.
در بیانیه روابط عمومی سپاه استان زنجان، به‌جز اسامی این اعضای سپاه پاسداران، جزئیات بیشتری درباره محل کشته شدن آنها و درجه و محل فعالیت‌شان اعلام نشده است.
این در حالی است که تا ساعاتی قبل، رسانه‌های ایران این مناطق را به‌عنوان نقاطی که هدف حملات بامداد پنجشنبه قرار گرفت، اعلام کرده بودند: «اهواز، آبادان، بندرعباس، قشم، بندرانزلی گیلان، کازرون و فراشبند استان فارس، چغادک بوشهر، شادگان و اروندکنار خوزستان و جزیره کیش»
@
VahidHeadline
پیام دریافتی بررسی‌نشده: در خود زنجان کشته نشدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77646" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MViS6oPJy9ofa4d3G1vub7GXT5YdHBD-NHydTcxxIZKPGQaoxABIATNRULGTyO5bAuEipw4IopSNo_kg8X9idMw4x9KjdL_U--1gf7EQACKm4axznpkngqd7ZhnJBTUndSVoDeHjtoLRVC-b7NUa9Tp6a58Whx55i3pxUcEjo5a3JHEiiWvIQh1wiRPjB4_Kh6JRfDLwO158x2347eO6TgXjVAw_vxhbWvO2eBAFHbyaMWbLq4iZ6MYUiQln-LZ5e7nBcwvQEy0bOneKKsiISzSy0XGF5ecBxX78f54kZnF2UTWSs2rljt3XFKkBDhF9GRkk06V6oggZMOW1fxs01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران ادعا کرد که در حمله به پایگاه الازرق اردن «سه فروند هواپیمای اف۳۵» را از بین برده است.
سپاه پاسداران در بیانیه خود ادعا کرد که پنج‌شنبه هشتم مردادماه، با حمله به محل استقرار و سوله تعمیراتی جنگنده‌های اف۳۵ آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، «سه فروند هواپیمای اف۳۵ را به کلی منهدم و به سه فروند دیگر خسارت سنگینی» وارد شد.
سپاه همچنین ادعا کرده که در این حمله «چند افسر و کادر فنی و تعمیراتی» کشته شدند.
این ادعاها در حالی است که پیشتر ارتش اردن اعلام کرد که پنج موشک شلیک شده از سوی جمهوری اسلامی را در آسمان این کشور رهگیری و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77645" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCPgDswY8GIW_DSPKrJrRlaV8ZeCpxl1aATNxG0OYKjHmzU1-eg3sLkQbb0kuJ_VqD7Z3yxPNOPUArFGX3b894T9ldJa8lTDenkraBAq7rOXKGd8xZc3UqChoACeCFWZiMYQxF8zVGzlRsbyq279LR7EaWkWD_OU1odFElo5w7Wh7cK3KEBog6DN7gihhLB-LiH0FS2Um3HLx-c8xV6RX8hq-X_Rz8Obsr_Z_vvspRGFUsZ1GCtZLej7SUdYNq-Y90YZMymPTsQoNvrZoSxYLSE5St5G1UwWYGtdAi0OomdK1TBBpX3NQz8ImkpN99Eqi8XF0hxeQCeDxnz5804mFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۴۱ دیوان عالی کشور حکم اعدام بنیامین نقدی، از بازداشت‌شدگان اعتراضات سراسری دی ۱۴۰۴، را که پیش‌تر از سوی شعبه اول دادگاه انقلاب شیراز صادر شده بود، تایید کرد. وکیل او می‌گوید با وجود ابلاغ این رأی، درخواست اعاده دادرسی به‌زودی به دیوان عالی ارائه خواهد شد.
بنیامین نقدی شامگاه ۱۳ دی‌ماه ۱۴۰۴ در جریان اعتراضات در شیراز بازداشت شد.
بر اساس گزارش‌ها، علت بازداشت او شعله‌ور کردن یک کپسول آتش‌نشانی در مقابل نیروهای انتظامی عنوان شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77644" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F9mrliVDbbwULfpVs6UesZgetDM_8YSWvINrdEBr-FAaCJqUuE1RBtMv2IvJYRYt09N1z_e26nfbsK8OlTwtyn40dTUah3l_Q9mMIcPScy3UeLiGd0OcBxibOLJTb5ASX5Hz0G5z-2d-X4r2dOiVm6lMhkipBPoLSXHa5nA5ZGpNyE8okCF44Rso7C44lCs506UhG0ygUVCPudtQgzmv-egZqmo-yX9zD9KkJivKjylKVtTngMRp5rlxT0FAIAN-4nKepZoYtx4YQ4nVGz3bhJZYmeOEpE6ldOzpRvojKRZ3KfhavOLaIpuGqhzjHlhe5OZRh7w1AxrxzQfrTwhQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: آتش‌سوزی پس از حملات آمریکا به نقاطی در
#اهواز
پنج‌شنبه ۸ مرداد حدود ساعت ۵:۵۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77643" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8kBA0X3QamQ1aQb8LEsO2XhG0TmoqlLhsjp4u7CZYRZ_6hayxhbDWGC4ebxNMVC--88NwFUVdHdEDvceBo-A-LcqCRjl_kFCW7JOp7w-rG1uVWqK1H5Ob2wpPMGukQGa8tBCKCoMseZOt3O0jxI2In9AZo68ZGpn9bJwh260suY9rpaDDjffWPtZhCgPrJuC7pJtLvizraNnK_FCD79qXtgH_jqE_pjPIgnm2X-7qa1s_tiE1MH3qA2UbHKl5jvLo26ha4m4-_Nrgu7IVsGuuoRO_seEe92pV5DOYCg3mUnrWAJH2aCwxzVtSNqHWyXn4ZUIf6z5TYBZlavtkO6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اردن صبح پنج‌شنبه هشتم مرداد از مقابله با حملات موشکی ایران خبر داد و اعلام کرد پدافند هوایی این کشور «پنج موشک بالستیک» شلیک‌شده به این کشور را رهگیری کرده است.
سپاه پاسداران روز چهارشنبه نیز باوجود توقف چند روزه حملات آمریکا، به سمت اردن موشک شلیک کرده بود. پایگاه‌های ارتش آمریکا در اردن از ابتدای دور جدید حملات متقابل آمریکا و ایران از اهداف اصلی حملات موشکی و پهپادی سپاه پاسداران بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77642" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=m4oCanqRcfckt8u6SXQ7dsQnBPyDlfjUId0Yz36QEBbwiPMUGtjIPF6qtSHJIfSjLKAZzZehRCJiTyOAw9NF1WDYeOsB52B4PxtBXMW8J8E_KSbO6J0Rn3_CSe42FGXbKHsGshcQ-aCiNF0RZ_46BaXDFMVhjwFmSM3hXgsJwVxJN3XoWlIUp-Vz7z295o3po7DuQ4GVfQgO-ll-qotfqN7hgLUT_m5V-BEFpM6kFzQOMA-nDHQIv6TEh_SVXkT8UVVeGCsGFh_eFnzpJNMEOMJ5hUZwr9vnRHHkibp6RAJAMCcyVB9blKz-prn3g0JBLNlzJEceBg4l8z0vuX3nDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=m4oCanqRcfckt8u6SXQ7dsQnBPyDlfjUId0Yz36QEBbwiPMUGtjIPF6qtSHJIfSjLKAZzZehRCJiTyOAw9NF1WDYeOsB52B4PxtBXMW8J8E_KSbO6J0Rn3_CSe42FGXbKHsGshcQ-aCiNF0RZ_46BaXDFMVhjwFmSM3hXgsJwVxJN3XoWlIUp-Vz7z295o3po7DuQ4GVfQgO-ll-qotfqN7hgLUT_m5V-BEFpM6kFzQOMA-nDHQIv6TEh_SVXkT8UVVeGCsGFh_eFnzpJNMEOMJ5hUZwr9vnRHHkibp6RAJAMCcyVB9blKz-prn3g0JBLNlzJEceBg4l8z0vuX3nDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77641" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rN946b-cwXgogpRNfd_8GiKl3xgMTpPF-YeeSLb4k8cJ-vAUEcEwqAGa-LAUI2wS1Ge5JfXvDvoXeOsDj7rjKET0HDjl48Bc1jVdm0FI9syVphOS9HbjFCGOmjwYFqNCghAkTuNiY2Ov3GynIvNHy3WycQjhGehTpcB9VSJQ4o9NLbcKfwUnFxe5G_sXGcNR1GmYxWWOQoYZMxJZzSaWI6pGLaIkxV_hYnfWpM3TarI3674LAZWOJy3vkX6qqMqvfrrSjvuINIXanq6NvNvZC9Zk_YNx2oTmVmzwL3PqHKr6jPbUXY0hkJzz7Mjg6ImcoERSM5R2rfqBPC70QLNITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف خمین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77640" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXKdHhd-4vLmEVbTeLtX0ZW7YvGmUB-VZwUoybThmXmIXqbo3El0D5CVdd6HR40h2JgV04E8bgq30rSXA-Tp7mslAxKaEvYc7T1kVuUCk8hqz_0VRrH5EqsCq0gdj8Plgj1Rdvn0--F_lB3CckSxYtC-KnBFm5IEoy0n-K16iZlqfH-03zJsubJIwhZINCBAk46PhEkvAMMCt89F9mlVdwNRJQE6ymmB4JRT8VWaWTc78CjTdTRIrtNkbwuyGbXBYVBRRlzSCsbqVFzJ_aiWN28WKIH1OssT7xTXrWAAZ26jzxZiy5e3iHnr_rEA_k2OW3mpqKzOa5JeiH2GhFeLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از یزد
سلام وحید از سمت یزد دارن موشک میزنن
از یزد موشک زدن
سلام ساعت ۷:۲۱ صدای ارسال موشک داره میاد،
سلام از یزد موشک بلند شد ۷:۲۲
الان یزد 7:21 دقیقه  موشک فرستادن
سلام وحید. جان ساعت ۷و۲۰دقیقه از یزد موشک شلیک شد
وحید جان از یزد موشک بلند شد
۷:۲۱ پرتاب موشک از یزد
همین الان از یزد موشک زدن</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77639" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyN59kZO66B4cyLb6flES4rOSfL0n2WLufOQNSaOkxeEWMCprFEWBT4qg4mFmiY9pP8-4S18yhln3q4hzILhwwsKymdRS6vvWQvzEIUgHxCv30_BcEeT5uHx2YTIIKNed5dWl3U2MDEgQd2I9uEPmKUrXr_AHXkttFsnaHVUj8KZvpp10Rs4B0PzSh-afA_Bu13L_ItosgYOZXPU9WXyen0RlZ0SzJZmYMyeK1pAMYfnpOVinwZhMHaug4UecrIL9jsMtlyKtqJKwOJThs8pZzg4ObrkDWSuhiS6_IjzQSLlP1GKYknY9DYqNYJC6NZmb3ijJvI3_q9VTt3PO7ZR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال در گزارشی نوشت آمریکا در پاسخ به حمله موشکی جمهوری اسلامی به نیروهایش در اردن، بامداد پنجشنبه حملاتی را علیه مواضع سپاه پاسداران انجام داد.
به گزارش این روزنامه، با وجود گسترده‌تر بودن این حملات نسبت به عملیات‌های پیشین آمریکا، یک مقام آمریکایی گفت این اقدام به معنای بازگشت به عملیات گسترده نظامی نیست. امیدها به دستیابی به یک پیشرفت دیپلماتیک فوری نیز با این حملات کمرنگ شد.
ارتش آمریکا این حملات را «پاسخی قاطع» به حمله روز سه‌شنبه جمهوری اسلامی توصیف کرد. این حملات چند ساعت پس از آن انجام شد که دونالد ترامپ، رییس‌جمهوری آمریکا، وعده داده بود به این حمله پاسخ خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77638" target="_blank">📅 07:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=GwGubL50WdxMkpD_csHcbW4Ya1xlQT1Vymz6ScyTlHeGx48rXYfWMjiMrvEH8jucueoulx_UrCE_MSaZxthFbbnU6d7Q3IpMUbInTFuLXto66NmN93PI3DzdhpLBnInbdWoKafMpSZczjObwONleEgbGyZixOSc808gNa1we8ie9xYiLVWJP67tO6R083sPWiOuyLCwfxx4-P4NV_NyBugu0TnUb-tJ2yc_kpSqQOtdmsTJY5eXpQ7DlCCUh7lBPWumiEh7b9yXbfS8FKn6ae2Q-tojESW8EsR6MN4k-G_J46gi2yReec5_Gy2irLggoRif5ForLuacFWOGZWdIutg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=GwGubL50WdxMkpD_csHcbW4Ya1xlQT1Vymz6ScyTlHeGx48rXYfWMjiMrvEH8jucueoulx_UrCE_MSaZxthFbbnU6d7Q3IpMUbInTFuLXto66NmN93PI3DzdhpLBnInbdWoKafMpSZczjObwONleEgbGyZixOSc808gNa1we8ie9xYiLVWJP67tO6R083sPWiOuyLCwfxx4-P4NV_NyBugu0TnUb-tJ2yc_kpSqQOtdmsTJY5eXpQ7DlCCUh7lBPWumiEh7b9yXbfS8FKn6ae2Q-tojESW8EsR6MN4k-G_J46gi2yReec5_Gy2irLggoRif5ForLuacFWOGZWdIutg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا پس از تلاش ایران برای حمله، مواضع سپاه پاسداران را هدف قرار داد.
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۱۰ شب ۲۹ ژوئیه به وقت شرق آمریکا، در پاسخ به تلاش‌های دیروز برای حمله موشکی به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
تجهیزات و نیروهای سنتکام ده‌ها هدف متعلق به سپاه پاسداران انقلاب اسلامی در ایران را هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، مواضع نظارت و دفاع ساحلی و توانمندی‌های دریایی. هدف این حملات، کاهش بیشتر تهدیدهای ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حاشیه خلیج فارس بود.
در ۲۸ ژوئیه، نیروهای سپاه پاسداران چندین موشک بالستیک را از ایران، در تلاشی برای انجام یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری شدند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در خاورمیانه مستقرند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77637" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام‌های دریافتی:
۴:۴۹ اهواز انفجار شدید
انفجار های وحشتناک و پشت سر هم در اهواز
خیلی وحشتناکه
پشت سر هم
حداقل ۴ انفجار
اهواز رو زدن صدای ۲ انفجار
اهواز و دارن میزنن شدید
صدای انفجار مهیب توی اهواز ۴:۴۹
همچنان ادامه داره
تا الان ۴ انفجار بلند
صدا انفجار پشت سر هم ۴ تا زد ۴:۴۹ اهواز مرکز شهر
سلام وحید ۴:۴۹ اهواز ۴تا صدای انفجار شدید اومد
اهواز سه تا انفجار ۴:۵۰
سلام وحید الان ساعت 4:50 اهواز زدن
5 بار صدای زیاد اومده تا الان
اهواز رو زد چهار بار الان!!!!
۴ تا انفجار سنگین ظرف ۲ دقیقه
همین الان اهواز چهارتا صدای انفجار شدید
ساعت ۴:۵۰
همین الان اهواز نمیدونم چند تا افتضاح بلنده
تمام شیشه ها داره میلرزه
اهواز همین الان ۶تا انفجار
۶ تا پشت سر هم اهواز
اهواز ۴.۵۰ دقیقه صدای ۵ انفجار شدید .
سلام وحید جان ۴:۴۹ ۵تا انفجار خیلی شدید اهواز
وحید واییییی خیلی بد بود چندبار زد اهوازو
۴:۵۰ وحشتناک نزدیک ۴ یا ۵ تا انفجار شدید شدید ماشینا به صدا درومدن
ما همین الان با صدای انفجار از خواب پریدیم اهواز ۴:۵۰
اهواز ۴تا اتفجارشدید پشت سر هم
اهواز تو چند دقیقه چندین انفجار شدید داشتیم و طوری که خونه میلرزید و برقمون هم به یک باره قطع شد
اهواز به گلستان خيلي نزديك بود ٤ بار
😭
😭
😭
سلام وحید جان، اهواز اطلاعات توی گلستان رو زدن ما اونجاییم
اهواز فکر کنم سپاه توی اتوبان گلستان بود، سایت اداری. ۴ انفجار.
اهواز کوی سعدی بعد انفجار دوم برق رفته الان ساعت ۴:۵۴
سلام وحید،4,49دقیقه4انفجارشدید دراهواز احتمالااسنگرشکن بودن،
سلام وحید جان ساعت ۴:۵۵ دقیقه صدای انفجار پشت هم از دور شنیده شد
ساختمان اطلاعات اهواز توی گلستان رو زدن
اهواز سمت سعدی و گلستان نورش بود،برق سعدی هم رفت
من اهوازم جفت خونمون چندتا پادگان هست الان زدن چهار بار
خیلی نزدیک بود و وحشتناک
اطلاعات اهواز واقع در پیچ گلستان  رو زدن
وحید تو کل جنگ همچین صدایی نمیومد اهواز به طرز عجیب و وحشتناکی زد در حدی که خونه میلرزه نه فقط پنجره ها
ساعت4:50دقیقه صبح هشتم مرداد
حفاظت اتوبان گلستان رو زدن
🔄
ترکوندنمون اقا وحید
این یکی خیییلیییی بد بووود
بازم انفجار اهواز. ساعت ۵:۲۲
صدای انفجار مهیب در اهواز 5:23
انفجار مجدد اهواز 5:23
5:23 اهواز انفجار خيلييييييىىى شديد
اهواز دوباره زدن شدیدتر از قبلیا
۵:۲۸ یکی دیگه
یه انفجار شدید دوباره اهواز
اهواز صدا انفجار دوباره
وحید همین الان اهواز رو زدن
وحید دوباره انفجار اهواز
وحشتناک همین الان
اهواز ۵ و ۲۳ دقیقه همین الان شرق اهواز صدای انفجار
مجددا اهواز ساعت ۵و ۲۲
۵:۲۱ یدونه صدا اومد،۵:۲۷ هم یکی دوتا صدا اومد
باز اهواز رو زد وحید
زیتون کارمندی ۲تا دیگه الان زد
اقا وحید دوباره زد اهواز
اهواز الان زدن دوباره شیشه ها لرزید
😭
خیلی صدا و‌لرزش داشتتتت
هم اکنون  بازهم زدن05:23
5:22دوباره اهواز و زدن
5,23حمله دوباره اهواز
سلام گلستان اهواز باز زدن.. ساعت ۵:۲۲، ۵:۲۷
5/22" بازم اهواز رو‌زدن شدید
۵:۲۳ اهوازو بازم زد
سلام ۱ انفجار دیگه گلستان اهواز ساعت 5:23
چرا ول نمیکنه
الان یکی دیگه زدن5:23
ساعت 5:22 انفجار شدید اهواز
سلام اهواز وحشتناک بود گلستان سعدی اگه چسب نداشتیم رو شیشه احتمالا شیشه های دو جداره خورد میشدن
ما هنوز برق نداریم
🙏🏼
🙏🏼
انفجار های آخری بشدت به ما نزدیک بودن
آسمون قرمز شده بود از اتیش و صدای ویراژ هواپیما میومد
راحت میچرخیدن
با انفجار دوم برق رفت
۵ و ۲۲ دوباره زد همین الان
🔄
الان دوبارههههه
یکی دیگه5:27
دو انفجار دیگه ۵:۲۸
دوباره زدن وحید
دوباره زد
خیلی شدیده
الان ساعت ۵:۲۸ دوباره بد زد
اهواز همین الان دوباره زدن خونه لرزید با همون شدت بود
باز الان صدا دو انفجار
۵:۲۸ دو صدای انفجار مجدد اهواز
بسیار شدید و لرزش شدید تر شیشه ها
دوتا انفجار دیگه تو اهواز ۵و ۲۸
آقا وحید انفجار به شدت  شدید موج های بسیار زیاد در خانه
بازم انفجار خیلی شدیدی اومد ساعت ۵:۲۸ خیلی ترسناکه
دوتا دیگه زد ۵:۲۷
بندرعباس ساعت 5.24صدای دوتا انفجار وحشتناک بندر
پایگاه هوایی رو دوباره زدن
به نظر میاد یک جا رو دارن چندین بار میزنن. احتمالا سمت گلستان
انفجارها پشت سر هم شدن دوباره
بازم دارن اهوازو میزنن خیلی وحشتناک تر
همچنان داره میزنه
۵:۳۰ دوتا انفجار شدید
سلام اهواز بد دارن میزنن برق رفته مثل اینکه اطلاعات سپاه زدن
هر ده دیقه یبار تا خوابمون میره یه قلمبه میزنن
افتضاحه خیلی نزدیکه صداش
همه شهر حسش می‌کنه
اهواز، همون اطلاعات توی گلستان رو همچنان دارن میزنن
۵:۳۵ اهواز
بازم انفجار سنگین
همه شهر رو بیدار کرد!
یجوری اطراف مارو زدن که کل هوش و حواسم پرید حالمون بده و دقیقا ۱ ساعت دیگه باید سر جلسه امتحان باشیم ...
اهوازیم .
پمپاران در اهواز تمام نمیشه مرتب داره میزنه
سلام وحید جان.
خواهر من دانشگاه علوم‌پزشکی جندی‌شاپور می‌خونه. خوابگاهشون  توی گلستانه، روبه‌روی اطلاعات. می‌گه بعد از انفجارهای مهیب و‌ پی‌در‌پی اهواز شیشه‌ی اناق‌ها شکسته و   همه‌ی بچه‌های خوابگاهی هراسون توی محوطه جمع شده‌ن.
صدای دانش آموزان خوزستانی باشید
نیم ساعت دیگه چطور به سمت حوزه های امتحانی راهی شوند؟؟
🔄
دوباره اهواز رو زد 5:43
ساعت 5:43 دقیقه ی انفجار
بازم زد همین الان صداش دور بود
اهواز ۵:۴۲ مجدد زدن
ساعت ۵.۴۳ صدای دو انفجار در اهواز
دوتا دیگه اهواز رو زد
وحید دوتا دیگه
بازم زد این یکی لرزشش بیشتر بود
.۵:۴۳ گلستان اهواز دور بود ولی دوبار زد
دو انفجار مهیب دیگه در اهواز
تمام خونه و شیشه‌هاش لرزید
اهواز ساعت ۵:۴۳ دقیقه صدای انفجار
اهواز ۵:۴۳ شدید ترین انفجار از ساعت شروع حملات بود
😭
یکی دیگه
سمت شرق خیلی شدید بووود
دوباره انفجار در اهواز ۵:۴۲
سلام همین الان ساعت۵:۴۳ دقیقه روز پنجشنبه  اهواز و زدن
ملی راه هستیم صدا خیلی نزدیک بود
۵:۴۳اهواز ۲انفجاد شدید دیگر
بسیار شدید سمت کیانشهر‌اهواز، دزدگیرا به صدا در اومدن و خونه کامل لرزید
۲ انفجار پشت هم اهواز خیلی سنگینن انفجارهاش
شدید کیانشهر ۵و۴۴دقیقه
صدای انفجار اهواز همین الان ساعت ۵:۴۳ صبح
وحید بازم زد اهوازو دو تا ۵:۴۳
اهواز، ۵:۴۳ …این یکی شدیدتر از بقیه بود
5:42 صداى انفجار در اهواز
ساعت ۵/۴۲ دقیقه انفجار فوق شدید در پدافند اهواز کیانشهر
5:44 یکی دیگه اهواز
دوباره اهواز انفجار شدید ساعت ۵:۴۴
وحید جان الان دوباره صدای انفجار اومد دوبار پشت سر هم اهواز
وحید زد همین الان زیتون اهواز لرزید
وحید مجدد زد دو بار یه صدا انفجار دیگه هم اومد اما لرزش نداشت و نزدیک بود خیلی ساعت 5.44
سمت کیان ابادیم ما شدید صدا اومد ۵و ۴۴ دقیقه
همین الان اهواز کیانشهرو زدن
جفت پدافند
ما کیانشهریم
فکردیم داخل خونمون رو زدن
تا الان ۸بار اهواز رو زدن ۶تاش اطلاعات اهواز بود دوتا دیگه خیلی دور بود معلوم نبود کجا بود
انفجار آخر پدافند بود کنار میدان تره بار
سلام وحید بالای۸انفجار در اهواز رخ داد صداهای خیلی وحشتناکی داشت تروخدا صدای مارو به برسونید بچه ها نیم ساعت دیگه باید برن امتحان بدن گناه دارن اهواز رو ترکوندن
اهواز هم ۴:۴۸ دیقه هم ۴:۵۰ دیقه
هم ۵:۲۰ دیقه هم ۵:۲۸ دیقه
دوتای دیگه هم الان ۵:۴۳
مجموعا حدود ۱۳ تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77636" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHbWShUVl5DETOW6hWH5SV9p7bn-UA2cxWGu4OiNOMFQ7u8cCEVPI3gCkkObRkaQz24J9CHIwNK0haQ5JlDVI67FyOT26tO0FzmkdfC0XWJCVJZyU5Re12viPUcwjWdqwDbujrNlisN1sSMBj0rszKfUo3C6o1cJhQVUcHbhhIjDQxr1mmHugL2GJf7NqgtddTFvIhg4W5Nz7_IUiheM4m0pOSMwjekX3y5CIulJ1Mu9LxH87OYl2F0mW2sm2k5DsB06Q9JpmowiLj1I_OqRZbU_6YkbRiYWvvb_mTzRj815_BUIkOex4HIPR6T_UmYRz77zPHICpklFUty91ytP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم، در پی شنیده شدن صدای انفجار در استان فارس، منطقه‌ای در اطراف شهر کازرون هدف حمله قرار گرفته است.
پیش از این رسانه‌های داخلی ایران از شنیده شدن صدای چندین انفجار درنورآباد استان فارس خبر دادند.
@
VahidOOnLine
پیام‌هایی که من دریافت کره بودم:
درود کازرون خونه ی ما لرزید
در نزدیکی کازرون صدای چند انفجار اومد ۳:۴۲
ساعت 3:41 - 3:42
کازرون چند تا صدای انفجار شدید اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77635" target="_blank">📅 04:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام‌های دریافتی:
‌
۴:۳۵ قشم دو انفجار
۰۴:۳۶ دو انفجار بندرعباس
وحید دوتا انفجار جدید بندر همین الان۴.۳۷
بندرعباس ۲ تا انفجار در حد لرزش در و پنجره ساعت ۴.۳۷
۰۴:۳۶ دو انفجار بندرعباس
صدای انفجار بندرعباس
دو انفجار شدید بندر عباس ۴:۳۷
بندرعباس شدید تر از قبل
دوتا همین الان
۴ تا انفجار مجدد بندرعباس ۴.۳۷ دقیقه
وحید جان صدای دو انفجار در بندرعباس ساعت 4.37
بندرعباس مجدد صدای مهیب ساعت ۴:۳۷
بندرعباس الان ساعت ۴:۳۷ صدای انفجار
وحید ۴:۳۷ زدن بندرعباس ۲ تا شدید موج داشت
الانم دوتا سنگین زدن از خواب پریدیم 4:36
سلام وحید جان همین الان دوباره صدای انفجار میشنویم
دو انفجار شدید همین الان بندرعباس
دوباره بندرعباس انفجار به همون اندازه ۳.۳۸
صدای سومی اومد شدیدتر۴.۳۸
دوباره ۴:۳۸
🔄
دوباره انفجار پشت سرهم ۴.۴۳
همین الان انفجار دوباره
درود ۲ دیگه زد ۴.۴۳ بندرعباس
چند تا دیگه هم زدن همین الان
دوباره ۴:۴۳ بندرعباس
این جدیدا فقط موج دارن
بندرعباس ساعت ۴:۴۳ صدای انفجار شدید
محله چاه تنگو درگهان چن تا خونه دچار آسیب شده انگاری ک زیر آوار موندن کسی بعد انفجار
ساعت ۵ و ۱۰ دقیقه باز قشم زدن
قشم محله ی نریمان،  زیرانگی و محله چاهتنگو رو زدن.. یه دکل هم زدن
سلام وحید داخل قشم محله چاه تنگو  یه خونه مسکونی رو زدن الان رفتم راه رو بستن معلوم نیست فعلا کی داخلش بود ولی خونه پودر شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77634" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZJOKruPggjnAsGzJhnNzMrNjnQsUyAoDzUxf8M840s5prInkT8K8ERWiDLvBTSIhVO97TJ44ED4XsFvrFZO7z9OJKXaBM1f22dHMQ7Si-cR78P1tu6zrzWb4Y_Kou_WvQijwqV8b9Yvt0vz4M-smXoWK4uFs0WwyZxYa6AMeDa9usSr4WbFnaDv5STOhDZuMvi3QysX5XZRHnZuemytplXiFYQnfC0jdqMzTpKqn_sSkqp37yFtyaqBDUep18i_H9PwmFFGik-I0-qR9Hi1avzseHrTBsCM2wiijhgvCzTpifLLP-gHjfkdblMuX7xEGcZ7nujarMNTKFRxcP7qJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای ایالات متحده امروز ساعت ۸ شب به وقت شرق آمریکا [۳:۳۰ بامداد پنج‌شنبه به وقت تهران] حملات علیه ایران را آغاز کردند.
این حملات، پاسخی قدرتمند به تلاش‌های دیروز ایران برای حمله به نیروهای آمریکایی مستقر در خاورمیانه است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77633" target="_blank">📅 03:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان بندرعباس صدای 2 انفجار
3:40
سلام ۳ و ۴۰ دقیقه بندرعباس دوتا انفجار
۰۳:۳۹
بندرعباس
حداقل ۲ انفجار
درود
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
۴ ۵ تا انفجار توی کمتر از ۱ دقیقه بندرعباس
سه تا انفجار ذیگر
همین الان ۳:۴۱ صدای چند انفجار در بندرعباس
دوباره یک انفجار دیگه 3:41
دوباره یکی دیگه تند تند دارن می زنن
صدای انفجار بزرگ همراه با لرزه زمین بندرعباس
3:41 همین الان بندرعباسو دارن میزنن در و پنجره میلرزه
دو انفجار شدیدتر ساعت 3:41
بندرعباس صدای سه انفجار اومد ساعت ٠٣:٤١
سلام وحید جان همین الان انفجار شدید بندرعباس
سلام وحید جان بندرعباس رو داره میزنه سمت فرودگاه و پایگاه هوایی رو
قشم ساعت ۳و ۴۰ دقیقه انفجار در حد لرزش خونه ها
قشم همین الان با جنگنده بمب بارون شد
صدای سه انفجار شدید در شهر قشم
بندرعباس رو زدن همین الان ۲ تا صدای انفجار
شد ۴ تا
بندرعباس دو انفجار مهیب ادامه دار
صدا دور بود 3: 40
سلام وحید جان الان ساعت ۳ و ۴۰ دقیقه صدای انفجار اومد قشم ،برق ها نوسان پیدا کرد
بندرعباس همینننننن الانننننن خیلی شدید یا خدا
همین الان که دارم تایپ میکنم زدن
همین الان 3:40 دقیقه قشم با صدای انفجار بیدار شدیم
قشم صدا میاد پشت هم
سلام صدای انفجار۳:۴۳ شدید تر از قبلی
۳.۴۱ بندرعباس صدای انفجار
یه انفجار بزرگتر تر
با موجش در و پنجره لرزید
بندرعباس ۳.۴۳
قشم 2 انفجار نزدیک شهر
بندرعباس الان دوباره صدا اومد و خونه لرزید ۳ و ۴۳
بندرعباس ۵ تا انفجار پشت سر هم
انفجار بندرعباس ۲ تا شدیدددد بود صداش الان ۳.۴۲
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77632" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
بوشهر زدن
بوشهر چندتا صدای انفجار اومد
جم همین الان دارن میزنن
۵ تا زد
دوتا صدای انفجار اومد
بوشهر ستا انفجار ۰۳:۳۸
سایت موشکی برازجان رو زد الان.ساعت ۳:۳۷
بوشهر، جغادکیم
همبن الان از خواب پریدم
دو صدای خیلی بلند
سلام ‌وحید ساعت۳:۳۰ چندتا صدای انفجار شنیدیم صدا خیلی زیاد بود پنجره هامون انگار تکون خورد
سلام برازجان همین الان صدای جنگنده و یک انفجار
وحید جان جم الان چندتا صدای انفجار با لرزش اومد
ٰ3:38
بوشهر دارن میزنن
درود، سه بار جم صدا اومد.
۵ انفجار بوشهر همین الان ۳:۴۰دقیقه
بوشهر -چغادک ۴ انفجار ۰۳.۳۷
اقا وحید بوشهر چند تا صدای انفجار شنیده میشه
ولی خیلی صداش دوره
سلام آقا وحید ساعت ۳:۳۸ دقیقه بوشهر رو زدن
صدای جنگنده توی برازجون چند دقیقه هست که تموم نشده و هی بلند تر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77631" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان سه انفجار در کیش
کیشو زدن همین الان ۳:۳۱
کیش دم بندرگاه ساعت ٣:٣٠ ٢ تا زدن
وحید جان کیش ۲ تا ۳:۳۲
سلام وحید
کیش رو الان زد
دوتا انفجار
وحید الان کیشو زد
۰۳و۳۰ دقیقه انگار  تووآب بود
سلام وحید کیش همین الان صدا اومد
سلام وحید جان
همین الان ۳۱:۰۳ کیش صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77630" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=swj5Yq2LDM3cAPFuR8ji_IekaP6zWtUxDJiVvLC4HJS5PBMQh-7bkFA0df6mmwQGtgW5ohVfeQVN1c6TgQFXjrx8BASU90lIQrXrVQBQEBtbKdIgn48RDHRn_gUe3iRatJJJkNZlSqiG4DwC3bIiT3T_qBO1r6CfX2VKzNIzPFwI5UwbPEzZQDoERyVy9ruvnb0q1KOKPqACFnyKXEj154OSd9wW86B2kxY7hFdMOEVKeZchyBNDyATxOXbvsht7KQIbeVylef1iLOC727GHU64OjJRzedJyHDEjxGie4KGeqryBcDX-n9piufoFnd4Z2dpO4hwwig8PPfNk-j_VuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=swj5Yq2LDM3cAPFuR8ji_IekaP6zWtUxDJiVvLC4HJS5PBMQh-7bkFA0df6mmwQGtgW5ohVfeQVN1c6TgQFXjrx8BASU90lIQrXrVQBQEBtbKdIgn48RDHRn_gUe3iRatJJJkNZlSqiG4DwC3bIiT3T_qBO1r6CfX2VKzNIzPFwI5UwbPEzZQDoERyVy9ruvnb0q1KOKPqACFnyKXEj154OSd9wW86B2kxY7hFdMOEVKeZchyBNDyATxOXbvsht7KQIbeVylef1iLOC727GHU64OjJRzedJyHDEjxGie4KGeqryBcDX-n9piufoFnd4Z2dpO4hwwig8PPfNk-j_VuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
آبادان ترکوندن
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
صدای انفجار آبادان
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
سلام وحیدجان همین الان چهار بار صدای موشک شنیدیم آبادان ساعت ۰۳:۳۲
سلام آقا وحید تا الان آبادان ۸ بار صدای انفجار اومد ۳:۳۰ دقیقه
احتمالا دارن موشک هوا میکنن
سلام وحید، آبادان ساعت ۳:۳۱ پنج شیش تا صدای انفجار بلند شنیدیم
وحید سلام
۶ تا صدای انفجار
همین تلان ، ابادان
وحید سرساعت ساعت ۳:۳۰ ابادان صدای چندتا صدای انفجار اومد ولی دوره احتمالا خارج از شهره
حداقل ده تا انفجار آبادان ساعت ۳:۳۰
از ساعت ۳:۲۰ شروع شد
اقا وحيد صداي ٦ انفجار ساعت ٣:٣٠صبح در ابادان
وحید آبادان ۵ تا انفجار شدید ۳:۲۸
همین الان صدای ۶ الی ۷ تا انفجار از آبادان اومد
ساعت ۳.۳۰ بامداد
آبادان نزدیک ۴/۵ تا صدا شنیدم ... برای اطمینان حتی به دوستمم گفتم اونم شنیده
۳:۳۳ آبادان رو بیشتر از ۵بار زد. بیرون شهر یه چیزی آتیش گرفته، نمیدونم کجاست
آقا وحید آبادان رو ساعت سه نیم زدن شیش تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77629" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuPpvTizZmWj1SMj8xcx9hZbUhOnOnqxiW4_1qe4Pd4Y2-iV-QjV9MCe_S4I-gRBFmSbNqZdCeawsLt_HVljCTJL6BRFGEhWlrs6nl6HXUDfW_Tt72uR4y6YB27LeI84Kbl2a8GlLJJhwbFwH6RZIkQxxJf9ojwzcPD27fwKoXy8XzTeWf18l7T53vwVa75x1n_1L80om-K-33ZPUdch4F5AfIz0rIqFVjBh5tMqABjR9MpW84GC8BN2IrAHuSjKyUwHe3OS1PlAhdfweeqn4I7EPDyfQ_IVr7vkuE2aChQVXk9J_xFk7hvLzbLWAKfTHjCLyRmiyZNoe0QUPq7p8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست خبرنگار اکسیوس:
یک مقام آمریکایی به من می‌گوید ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
BarakRavid
آپدیت:
بعدا همین گزارش در خود اکسیوس:
ترجمه ماشین: یک مقام آمریکایی به اکسیوس می‌گوید ارتش آمریکا روز چهارشنبه اجرای حملات هوایی در ایران را آغاز کرد.
چرا اهمیت دارد: این نخستین حملات آمریکا در ایران از زمانی است که دونالد ترامپ، رئیس‌جمهوری آمریکا، جمعه گذشته کارزار بمباران را متوقف کرد تا فرصت دیگری به مذاکرات بدهد.
حملات روز چهارشنبه در تلافی حمله موشکی ایران در روز قبل انجام شد که یک پایگاه آمریکا در اردن را هدف قرار داده بود. به گفته ارتش آمریکا، همه موشک‌ها رهگیری شدند.
محور خبر: ترامپ بعدازظهر چهارشنبه به خبرنگاران گفت که آمریکا در ادامه همان روز ایران را «بسیار سخت» هدف قرار خواهد داد.
ترامپ گفت: «حالا نوبت ماست.»
ترامپ مدعی شد ایران پذیرفته است که شلیک موشک‌ها اشتباه بوده و از آمریکا خواسته است تلافی نکند.
تصویر کلی: ترامپ پس از ۱۳ شب متوالی حمله به اهداف نظامی ایران، حملات را متوقف کرده و فرصت کوتاهی برای دیپلماسی ایجاد کرده بود.
حمله موشکی ایران این وقفه را درهم شکست و ترامپ را واداشت پنج روز بعد کارزار نظامی را از سر بگیرد.
یادداشت سردبیر: این یک خبر فوری است. برای دریافت تازه‌ترین اطلاعات دوباره مراجعه کنید.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77628" target="_blank">📅 02:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77627">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از ساعت ۲:۱۹
سلام وحید جان صدا ۳ تا انفجار شنیدیم نوراباد فارس
۳ تا انفجار همین الان نوراباد ممسنی
آقا. وحید نورآباد ممسنی رو بد زدن
۳ تا شیشه ها لریزد
وحید همین الان نور آباد صدای انفجار اومد ۳ تا بود دقیقن
وحید جان چند لحظه قبل صدا چندتا انجار شدید نوراباد فارس
آقا وحید نوراباد ممسنی رو زدن
صدا هواپیما هم میاد
وحید همین الان نور آبادو زدن
🔄
پیام‌های ساعت ۲:۲۴:
اوه یدونه دیگه
یدونه دیگه ام زدن
البته دور بود
وحید بازم زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77627" target="_blank">📅 02:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی شاید درباره پرتاب شدن موشک که با صدای جنگنده اشتباه گرفته میشه:
یزد الان صدا جنگنده اومد
ساعت ۱۲:۱۰
صدای جنگنده روی آسمان یزد
الان یزد صدای جنگنده امد خیلیم پایین پرواز میکرد صدای انفجاری نیومد اگر بیرون شهر زده نمیدونم
سلام وحید جان
۰۰:۰۷  از تنگه یه صدایی اومد مثل انفجار
شایدم لانچ بالستیک بود
ده دقیقه پیش از یزد موشک بلند شد
وحید جان صدای جنگنده میاد یزد
آپدیت:
پیام‌های دریافتی  بعد از انتشار پست:
یزد هواپیما رد شد
موشک و جنگنده نبود
ارتفاع به شدت پایین
سلام یزد جنگنده خودی بود
سلام وحید جان صدایی که از یزد میومد مال هواپیمای مسافربری بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77626" target="_blank">📅 00:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA5PP9GA9_iffgdjjzoTas0QTYzcBFo7IU-8i154uMPzpUza1SdjnoHJPkNrbobsiefsHmQ8G7LPq-SPLniq-ykCInG8ln531QirBDJHve_Y8KDmDdG8KkVcd_hbq1cVR199c8CNVHgb69iWqcvtDD2sEJuLB1Jj_zEnJbxjiSJ1hBDRp6nBD3j3TzBKxu1bF0ub9ekHLWKmsEsXwMMvp4tb248BJQTaT8hQm99S4j-xJO1PWNkVPfI2_wdRm2QMtDQKrKsnbwWg1Grg0uKEOvFp7rSMJQg2WY7l5brrJ2y1qT2eApO6bKOTfpz8jkieIA5udp3uYRUXu1lR7LB5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس نوشت «رژیم ایران که با سقوط آزاد اقتصاد و تورم سه‌رقمی روبه‌رو است، به‌شدت به منابع مالی نیاز دارد».
او تاکید کرد «ایالات متحده اجازه نخواهد داد ایران تجارت جهانی را گروگان بگیرد یا از کشتیرانی بین‌المللی برای تامین مالی «سپاه پاسداران»، اقدامات تهاجمی و سرکوب استفاده کند».
پیش از این، وزارت خزانه‌داری آمریکا چندین بسته تحریمی علیه افراد، شرکت‌ها، نفتکش‌ها و شبکه‌های مرتبط با صادرات نفت ایران اعمال کرده و اعلام کرده بود این اقدامات با هدف محدود کردن منابع مالی جمهوری اسلامی و سپاه پاسداران انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77625" target="_blank">📅 00:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c878874010.mp4?token=ZBBGWprQ7XeyfJNdb9KKosCgVS85Wbk0rpj3s9UAAxMyvngTiF91F-SNKx7KENkBCh3khD6HwVcVy_bda1lfsAu_y2BaTcGqcm0GxNndbogBjDh4UCzDTE--BGfbwOrKdQBgbr6oJ_qtfgK7uNaNC2n7IThHyKRVWQPYu2LuvP-5Tv-MrzQ1TE9P14Ko-V_LXlD_x82woFVasBomfQXF9hT4rah_59cRrZtLwZGhTSxDNfw1tssTGUblFurD3rbHmPB97iX2fMb_0IUdjqRocWiYBhI3Z-4XySDy9t45gLZb6uYEnRPhwVompXrpYTvfA88WLfoErBAYXR6kAWxWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c878874010.mp4?token=ZBBGWprQ7XeyfJNdb9KKosCgVS85Wbk0rpj3s9UAAxMyvngTiF91F-SNKx7KENkBCh3khD6HwVcVy_bda1lfsAu_y2BaTcGqcm0GxNndbogBjDh4UCzDTE--BGfbwOrKdQBgbr6oJ_qtfgK7uNaNC2n7IThHyKRVWQPYu2LuvP-5Tv-MrzQ1TE9P14Ko-V_LXlD_x82woFVasBomfQXF9hT4rah_59cRrZtLwZGhTSxDNfw1tssTGUblFurD3rbHmPB97iX2fMb_0IUdjqRocWiYBhI3Z-4XySDy9t45gLZb6uYEnRPhwVompXrpYTvfA88WLfoErBAYXR6kAWxWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از گفت‌وگوی ترامپ با خبرنگاران در کاخ سفید، ترجمه ماشین:
خبرنگار: در مورد حمله پهپادی به نفتکش LNG در سواحل مصر چه اطلاعاتی دارید؟ آیا نشانه‌ای وجود دارد که این حمله به ایران مربوط باشد؟
ترامپ: خب، می‌توانم گزارشی به شما بدهم. در این باره توجیه شده‌ام. این کمی از همان ماجراست، اما اوضاع رو به صاف‌شدن است؛ وضعیت دارد روشن می‌شود. در این میان، ما قرار است ضربه بسیار سختی به آنها بزنیم، چون نوبت ماست که ضربه بزنیم. آنها می‌دانند که این حمله در راه است و از ما می‌خواهند این کار را نکنیم. اما دیشب سعی کردند به آن شلیک کنند.
ما پنج موشک داشتیم که با سرعت ۸۵۰۰ مایل در ساعت در حرکت بودند و هر پنج موشک سرنگون شدند؛ اما با این حال آنها شلیک کردند. پس نوبت ماست. خواهیم دید که آیا در مقطعی به یک توافق می‌رسیم یا نه، اما ضربه بسیار سختی به آنها خواهیم زد.
—-
خبرنگار: در چه سناریویی تصور می‌کنید ایران به تأسیسات و پرسنل آمریکا در خارج حمله کند و شما عقب‌نشینی کنید؟
ترامپ: چنین چیزی را نمی‌بینم. نه، ما عقب‌نشینی نمی‌کنیم. ضربه سختی به آنها خواهیم زد. واقعاً می‌توانم این را بگویم، چون آنها در این مورد کار زیادی نمی‌توانند انجام دهند.
این گروه با گروهی که ما با آن سروکار داریم متفاوت بود. آنها قبلاً عذرخواهی کرده‌اند، اما باید یک ضربه‌ای به آنها بزنیم.
خبرنگار: وقتی آنها حمله می‌کنند، آیا همیشه پاسخ خواهید داد؟
ترامپ: بله، تقریباً.
خبرنگار: آقای رئیس‌جمهور، آیا این در پاسخ به حمله موشکی بالستیک شب گذشته به اردن است؟ وقتی می‌گویید نوبت ماست که ضربه بزنیم.
ترامپ: بله، فکر می‌کنم بیشتر به آن مربوط می‌شود. آن رویداد کوچک‌تری بود، اما آنها پنج موشک با سرعت ۸۰۰۰ مایل در ساعت به سمت ما شلیک کردند. خوشبختانه افرادی را داشتیم که بهترین تجهیزات جهان، یعنی سامانه پاتریوت، را به کار می‌گرفتند.
فکرش را بکنید؛ پنج موشک بزرگ با سرعت ۸۶۰۰ مایل در ساعت مستقیماً به سمت ما می‌آمدند و هر پنج موشک سرنگون شدند. چطور است؟ خیلی خوب است. فقط ما می‌توانستیم این کار را انجام دهیم؛ هیچ‌کس دیگری نمی‌توانست.
—-
خبرنگار: آقای رئیس‌جمهور، در مورد جنگ، آیا می‌خواهید مجلس نمایندگان پیش از ۳۱ اوت برای رسیدگی به لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: اگر لازم باشد، بله؛ هرچند راستش نباید لازم باشد. آیا منظورتان طرح لینزی گراهام است؟
خبرنگار: بله.
ترامپ: می‌خواهم ایران را هم به تعرفه‌ها اضافه کنند، نه فقط به تحریم‌ها. فکر می‌کنم این مهم است و همان چیزی است که لینزی می‌خواست. شنیده‌ام روی روسیه تعرفه گذاشته‌اند، اما روی آن پنج کشوری که به ایران مربوط می‌شوند تعرفه‌ای نگذاشته‌اند.
دوست دارم تعرفه‌هایی علیه ایران ببینم. این موضوع را بسیار قوی‌تر می‌کند. شاید بتوانید به آنها بگویید که به نظر من باید برای روسیه تعرفه بگذارند، اما برای ایران هم باید تعرفه در نظر بگیرند. این دقیقاً همان چیزی بود که لینزی می‌خواست.
——
خبرنگار:  رئیس‌جمهور شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اکنون گزارش جدیدی منتشر شده که می‌گوید ایران قرار است ۴۰۰ پرتابگر موشک از چین و از طریق پاکستان دریافت کند.
ترامپ: خب، این تعجب‌آور خواهد بود. چنین چیزهایی پیش می‌آید، اما واقعاً تعجب‌آور خواهد بود. او خیلی قاطع به من گفت که در این کار مشارکت نخواهد کرد و می‌داند که من کاملاً ناامید خواهم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77624" target="_blank">📅 23:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اکسیوس:
پشت پرده دیدار تعیین‌کننده «بی‌بی» با ترامپ در کاخ سفید
ترجمه ماشین:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدار خود با رئیس‌جمهور ترامپ درباره احتمال دستیابی به توافقی با ایران ابراز تردید کرد و درباره افزایش فشار اقتصادی بر ایران «از طریق ابزارهای نظامی و غیرنظامی» به گفت‌وگو پرداخت؛ یک مقام ارشد اسرائیلی این موضوع را در نشستی با خبرنگاران بیان کرد.
اهمیت موضوع:
دیدار روز سه‌شنبه نخستین ملاقات نتانیاهو و ترامپ از زمان آغاز جنگ در ۲۸ فوریه بود. این دیدار در حالی انجام شد که ترامپ همچنان برای دستیابی به توافقی با ایران تلاش می‌کند، اما هم‌زمان بازگشت به عملیات رزمی گسترده را نیز در نظر دارد.
▪️
چند ساعت پس از این نشست، ایران برای نخستین بار از زمانی که ترامپ روز جمعه حملات آمریکا در ایران را متوقف کرد، یک حمله موشکی علیه پایگاهی آمریکایی در اردن انجام داد.
▪️
ترامپ روز چهارشنبه در مصاحبه‌ای با فاکس‌نیوز وعده داد که پاسخی جدی خواهد داد. حمله غافلگیرانه ایران ممکن است رئیس‌جمهور را به سوی تشدید تمام‌عیار درگیری سوق دهد.
▪️
مقام اسرائیلی گفت نتانیاهو در انتظار تصمیم ترامپ است، اما به‌روشنی به او گفته است که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری و قدرتمند خواهد بود.
آنچه در اتاق گذشت:
ایران موضوع اصلی گفت‌وگوی ۹۰ دقیقه‌ای بود.
▪️
مقام اسرائیلی گفت آن‌ها سه گزینه‌ای را که ترامپ برای گام‌های بعدی در نظر دارد بررسی کردند:
۱. دستیابی به توافق با ایران.
استیو ویتکاف و جرد کوشنر، فرستادگان ترامپ، همچنان با ایرانی‌ها مذاکره می‌کنند، هرچند در حال حاضر اختلاف‌ها همچنان گسترده به نظر می‌رسد. مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است که نسبت به امکان دستیابی به توافق با ایرانی‌ها تردید دارد.
۲. ادامه محاصره دریایی ایران
هم‌زمان با افزایش فشار اقتصادی.
۳. ازسرگیری و تشدید حملات نظامی.
▪️
این مقام گفت: «همه این گزینه‌ها را به‌طور مفصل و بسیار صریح بررسی کردیم؛ نه با هدف ترجیح دادن یک گزینه بر گزینه‌ای دیگر، بلکه برای بررسی اینکه هرکدام چه نتیجه مطلوبی می‌تواند داشته باشد. موضوع گفت‌وگو همین بود.»
نمای نزدیک:
مقام اسرائیلی گفت ترامپ درباره تأثیر جنگ بر بازارهای انرژی و اقتصاد جهانی ابراز نگرانی کرد.
▪️
نتانیاهو به ترامپ گفت حکومت ایران عمدتاً می‌کوشد از تنها اهرمی که برایش باقی مانده است — تنگه هرمز — برای وادار کردن آمریکا به دادن امتیاز استفاده کند.
▪️
مقام اسرائیلی گفت نتانیاهو نگرانی‌های ترامپ را نادیده نگرفت، اما به او گفت راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد؛ اقتصادی که هم‌اکنون نیز تحت فشار شدیدی قرار دارد.
▪️
مقام اسرائیلی گفت: «درباره افزایش فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی گفت‌وگو کردیم. درباره امکان ادامه محاصره با هدف تحت فشار قرار دادن ایران صحبت کردیم.»
▪️
مقام اسرائیلی گفت در درون رهبری ایران میان کسانی که به‌شدت نگران فروپاشی اقتصادی هستند و عناصر تندروتری که معتقدند تا زمانی که کنترل تسلیحات را در اختیار دارند و می‌توانند از پایگاه حامیان حکومت پشتیبانی کنند مشکلی ندارند، اختلاف‌نظر وجود دارد.
▪️
مقام اسرائیلی افزود: «آن‌ها با مشکلات تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها و کمبود گازوئیل روبه‌رو هستند. اعتراض‌های کوچکی شکل گرفته است، زیرا مردم به‌شدت ناراضی‌اند. حکومت بسیار نگران این وضعیت است و می‌ترسد مردم به‌دلیل شرایط اقتصادی قیام کنند.»
پشت صحنه:
مقام اسرائیلی گفت مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، «درباره همه‌چیز» موضعی بسیار منفی دارد، اما مشخص نیست دستورهایی که به او نسبت داده می‌شود واقعاً از جانب خود او صادر می‌شود یا نه.
▪️
مقام اسرائیلی مدعی شد: «او زنده است، اما هیچ‌کس نمی‌تواند شهادت دهد که واقعاً او را دیده است. به اطرافیانش گفته بدون تأیید او هیچ کاری انجام ندهند و حتی گفته می‌شود یک بار وقتی بدون اجازه‌اش کاری کردند، عصبانی شد.»
نمای دور:
مقام اسرائیلی گفت نتانیاهو نقشه‌ای از سوریه را به ترامپ نشان داد که براساس آن، مناطقی که ترکیه در سوریه کنترل می‌کند «۵۰ برابر بزرگ‌تر» از مناطق تحت اشغال اسرائیل است.
▪️
مقام اسرائیلی مدعی شد ترکیه ۵ درصد از خاک سوریه را کنترل می‌کند، در حالی که اسرائیل ۰٫۱ درصد آن را در اختیار دارد.
▪️
یک مقام آمریکایی گفت برخلاف اشغالگری اسرائیل در جنوب سوریه، حضور نظامی ترکیه در شمال سوریه در حال حاضر با رضایت و به دعوت دولت سوریه انجام می‌شود.
▪️
مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است اسرائیل تا زمانی که تهدیدی از جانب «گروه‌های جهادی» وجود داشته باشد، حضور خود را در «منطقه حائل» جنوب سوریه حفظ خواهد کرد.
▪️
مقام اسرائیلی گفت: «نتانیاهو می‌خواست این موضوع را به ترامپ نشان دهد، زیرا او گاهی براساس اطلاعات نادرستی که بعضی افراد در اختیارش می‌گذارند، به دیدگاه‌های مشخصی می‌رسد. اگر در همان مراحل اولیه راهی برای تغییر نظرش پیدا نکنید، آن نظر تثبیت می‌شود. بنابراین می‌خواستیم واقعیت‌ها را، در صورت امکان به‌شکل تصویری، به او نشان دهیم.»
▪️
مقام اسرائیلی گفت نتانیاهو همچنین درباره توافق هسته‌ای آمریکا و عربستان سعودی با ترامپ گفت‌وگو کرد. ترامپ به نتانیاهو گفت این توافق را در چارچوب عادی‌سازی روابط عربستان سعودی با اسرائیل می‌بیند.
▪️
مقام اسرائیلی گفت: «اگر شاهد پیشرفت واقعی باشیم، درباره موضوع هسته‌ای حرف‌هایی برای گفتن خواهیم داشت.»
تصویر کلی:
مقام اسرائیلی گفت نتانیاهو به ترامپ، معاون رئیس‌جمهور ونس و ویتکاف گفته است که درباره کاهش کمک‌های نظامی آمریکا به اسرائیل تا رسیدن به صفر ظرف ۱۰ سال جدی است. او تأکید کرد که خواهان پیشبرد مذاکرات برای تدوین یک تفاهم‌نامه در این زمینه است.
▪️
مقام اسرائیلی گفت ترامپ و اعضای تیمش اعلام کردند بازخوردهایی از جمهوری‌خواهانی دریافت کرده‌اند که نگران‌اند به‌دلیل حمایت از حذف تدریجی کمک‌ها، به ضدیت با اسرائیل متهم شوند.
▪️
نتانیاهو به آن‌ها گفت شخصاً و به‌صورت علنی رهبری این تلاش را بر عهده خواهد گرفت، زیرا می‌خواهد اسرائیل به استقلال دفاعی دست یابد.
▪️
مقام اسرائیلی گفت: «درباره یک فرایند ۱۰ ساله صحبت می‌کنیم. از پیشنهادها استقبال می‌کنیم و شاید این اتفاق بتواند سریع‌تر رخ دهد.»
▪️
این مقام حتی گفت نتانیاهو به بخش دفاعی اسرائیل دستور داده است روی ساخت یک جنگنده مدرن ظرف یک دهه کار کند تا نیروی هوایی این کشور حتی در صورت توقف تحویل جنگنده‌های اف‌ـ۳۵ و دیگر هواپیماهای پیشرفته از سوی آمریکا، همچنان قدرتمند باقی بماند.
▪️
این مقام گفت نتانیاهو نمی‌خواهد اسرائیل به «حسن نیت کنگره آمریکا» وابسته باشد، زیرا معتقد است جهت‌گیری سیاسی هر دو حزب درباره کمک‌های نظامی در حال منفی‌تر شدن است.
▪️
نتانیاهو معتقد است وضعیت اقتصادی اسرائیل به این کشور اجازه می‌دهد کمک‌های نظامی آمریکا را به‌تدریج کنار بگذارد. مقام اسرائیلی گفت نتانیاهو پیشنهاد کرده است تفاهم‌نامه جدید شامل ۱۶ میلیارد دلار کمک نظامی مستقیم آمریکا و همچنین ۵ تا ۱۰ میلیارد دلار حمایت از توسعه سامانه‌های دفاع موشکی اسرائیل باشد.
▪️
افزون بر این، نتانیاهو پیشنهاد ایجاد یک صندوق مشترک ۱۶ میلیارد دلاری برای تحقیق و توسعه سامانه‌های تسلیحاتی جدید را مطرح کرده است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77623" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=Y4MI928GkfREPVc9DOn8C316wklVDNrQ-20gDDv05lhXlih5hJ2STxP9QkdZlbPKnPSvLEVGunt8UqEJKoNcPk_TZjeKyR-mjK2XyZWgQNVEslCBf6y8yOsVY-QvyZJQwMYpiOB6vAnjW8I9BBu3qnBKvSJQslUtUNs9n2wyr8UNgUFNXrfRDrKI9-PkqKBk3yL3mpQSx2WNoNX3doQUli-G5zBSCzPmmvpApG8hZQkvoHndQACkmo74UQeWYMRgLyd7EoXN8uYWnvfV38_vybTEjb__uUyoy_wASk3VM7JMJ_OkQE_R8iiP4HxycLivlUGjo7DgnuGrnD5NJt0eSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=Y4MI928GkfREPVc9DOn8C316wklVDNrQ-20gDDv05lhXlih5hJ2STxP9QkdZlbPKnPSvLEVGunt8UqEJKoNcPk_TZjeKyR-mjK2XyZWgQNVEslCBf6y8yOsVY-QvyZJQwMYpiOB6vAnjW8I9BBu3qnBKvSJQslUtUNs9n2wyr8UNgUFNXrfRDrKI9-PkqKBk3yL3mpQSx2WNoNX3doQUli-G5zBSCzPmmvpApG8hZQkvoHndQACkmo74UQeWYMRgLyd7EoXN8uYWnvfV38_vybTEjb__uUyoy_wASk3VM7JMJ_OkQE_R8iiP4HxycLivlUGjo7DgnuGrnD5NJt0eSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی، جزئیاتی از گفتگو و تبادل نظر خود با پیت هگست، وزیر جنگ ایالات متحده که روز چهارشنبه هفتم مردادماه در واشنگتن انجام شد را به اشتراک گذاشت.
نتانیاهو گفت: «هگست در این گفتگو به من گفت وقتی به وضعیت جهان نگاه می‌کنیم، کشورهایی هستند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی لازم را ندارند. در مقابل، کشورهایی هم هستند که از توانایی برخوردارند، اما اراده جنگیدن ندارند.»
نخست‌وزیر اسرائیل در ادامه افزود که وزیر جنگ آمریکا تاکید کرده است: «تنها در اسرائیل است که ما هم‌زمان شاهد وجود اراده و توانایی مبارزه هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77622" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7j_kVKz5-Ehn-dBXz9V2n0Q5T81wSbZEHmutZeYaB0N-Y9yWo5-9G5M_rGxdBKJFp7WquITGV8xxKdmMaX4Oj4U71Zad9EAewYcsGUY592RP5FpFF-ZCzVsZJvLrvXrtiOro3v7C3jNTQCUJSTqcKXgELdyGR_KRDbX_KKit2Np2XrcJapmNPuc1_wgFNgodukSanM19Yw5ZwKPZR-_K9a1qJG7ewiV66KZJ0hsj5tDAyg1zQpvhhC-FtmNoyfRMpW2Bbf59BTlteEYClJgvt4ixoLAQT1bA1x6vJiT0RrtXTctXu0LwWirD6KvrjnfvzjwKYUhrvnfrL13XkosqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از وقوع انفجار در پایانه گاز طبیعی مایع بندر دمیاط مصر هنگام تخلیه محموله خبر دادند.
همزمان، شرکت امنیت دریایی امبری و منابع امنیتی اعلام کردند یک پهپاد به یک شناور ذخیره‌سازی گاز متعلق به آمریکا برخورد کرده است؛ حادثه‌ای که به آتش‌سوزی دو کشتی منجر شد، اما تاکنون گزارشی از تلفات جانی منتشر نشده است.
بر اساس گزارش‌ها، این انفجار هنگام تخلیه محموله در پایانه گاز طبیعی مایع بندر دمیاط رخ داد.
شرکت امنیت دریایی امبری اعلام کرد یک پهپاد به یک شناور ذخیره‌سازی شناور گاز که تحت مالکیت آمریکا است، برخورد کرده است. به گفته این شرکت، در پی این برخورد آتش‌سوزی ایجاد شد و سپس به کشتی دیگری نیز سرایت کرد.
شرکت خدمات بندری اینچ‌کیپ نیز در گزارشی جداگانه اعلام کرد دو کشتی حامل گاز در بندر دمیاط دچار آتش‌سوزی شده‌اند.
امبری اعلام کرد خدمه هر دو شناور تخلیه شده‌اند و آتش تحت کنترل درآمده است. این شرکت افزود تاکنون هیچ گروهی مسوولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77621" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AcSi-GA1k_H0TurA__dYbyUQnwCVpG1pqi2LkSykDWzd1UKQbhQ-UivZMz4xaUKneCaop1zYRHlWgXIF6MUOb5GqSTGD_D3cD6DOp1fNbaSfv8jWHLVgqkYw0tcuxYtdyQx--uf4_EF6bG6PXX80NgUXD6YYSYxwFlCNLvzK3aeMX3zsiVGgSb4gdMvY_InrtQx_6PDPy2PWpfTTmNfDTjWX3fQ1L6djStQtFLOrNTzXAaZMrUt_vf6T9sDr75En5f1TWFDg5VO-kfi1ArWvXRSpNb6384g01Wxqr8sC023eVEj63pCDs0YGey49dCVCciWZje_Fd040wwYOxi6p3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: پس از تهدیدهای اخیر و تلاش برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناه در حال عبور از تنگه هرمز، سپاه پاسداران انقلاب اسلامی ایران همچنان ادعا می‌کند که دریانوردان بین‌المللی باید فقط از مسیرهای مورد ترجیح سپاه استفاده کنند.
✅
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه هیچ اختیاری برای تعیین مسیر حرکت آزاد و بدون مانع ندارد. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای سنتکام به عبور حدود ۱٬۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77620" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ild0CcCaSyKJvksO6NLnomxDNDLv1TAbdcE8PLFYcCPsijMEGHqBq68gfF45zeS1XQll_r_nmeIIQLitE62-A05dVxj2c7n7N6VqT7F7LpyKlNYhIai79AcxitqRjUr5W1TzhcOy2O2t0V-_BgOYs9rA-sIeH3FehPgHATD4Fzt1PQCCv7KLLGSUytkjSmBcz7nxcx9AJ8M2nnMtAv_kMYBJHQlZTJgXsoXqcTuU3ek7I3y_E8U-pBKGOa9csNgsvxAJx4789ObrABiZEwEGknLNHvjsagO0LBWBZqpks0myh50iEyrElsEKCmgo05uPGh9XnwedULt4BLOzM7dZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، نیروی دریایی سپاه پاسداران انقلاب اسلامی روز چهارشنبه هفتم مردادماه، اعلام کرد سه نفتکش را در تنگه هرمز به دلیل بی‌توجهی به هشدارها «هدف قرار داده و توقیف کرده است».
در این گزارش به نام این شناورها، مالکیت، محل دقیق حادثه و جزئیات تخلفات ادعایی آن‌ها در این آبراه اشاره‌ای نشده است، اما تهران مسیر جایگزین جنوبی در امتداد سواحل عمان را رد کرده است.
بر اساس بیانیه‌ای که تسنیم منتشر کرده، سپاه پاسداران تاکید کرده است که «مداخله‌ها و دستورات غیرقانونی» ایالات متحده از سوی شناورهای حاضر در منطقه «بی‌پاسخ نخواهد ماند».
مرکز عملیات تجارت دریایی بریتانیا، هنوز وقوع چنین حملاتی را تایید و گزارش نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77619" target="_blank">📅 18:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EGI95w_oDVQ-3DftRWRWluRsAKww823uNiOuwEfMwRj3yluK3Lhus4NMduGb0dulHNjVGQXI0_8CAPITngpBhF6aNYHsnLKi3ieClI2oDKbvD5mlJcZusRb6pJdM1ReOVVXjdCirZWadDQ3rEnzh4w6Z6nQVjcB9-nOAx6ig39eOo68yKava4SeeGni-mg9T-FDasGU1Ses-19TqdDd1avmmbjH2zdDJkQSeDp-91-3mjTALFQ3sE18xl9RVoZhpbeORqCtUjib13qN-SizvEBKHbMGTvHQwjnWd5rWNVv4b1dBQ0Mi2WuG9BC2e3xiLYWAVU3i77WxiI0Mbn2whsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ دانشگاه ایرانی در رتبه‌بندی تاثیرگذاری تایمز ۲۰۲۶ حضور ندارد
در رتبه‌بندی تاثیرگذاری و پایداری دانشگاه‌های جهان در سال ۲۰۲۶، نام هیچ دانشگاهی از ایران دیده نمی‌شود؛ این در حالی است که در فهرست سال ۲۰۲۵، ۳۴ دانشگاه ایرانی حضور داشتند.
تایمز امسال نحوه مشارکت در این رتبه‌بندی را تغییر داده و آن را به عضویت دانشگاه‌ها در شبکه پایداری و ارائه اطلاعات از سوی خود موسسات مشروط کرده است.
برخی رسانه‌های ایران این تحول را با عنوان «حذف ایران» پوشش داده‌اند؛ تعبیری که اقدامی هدفمند یا تنبیهی را تداعی می‌کند، در حالی که هنوز مشخص نیست نبودن دانشگاه‌های ایرانی ناشی از تصمیم تایمز بوده یا شرکت نکردن آنها در سازوکار تازه رتبه‌بندی.
رتبه‌بندی‌های موسسه تایمز از شناخته‌شده‌ترین و پرمراجعه‌ترین نظام‌های ارزیابی دانشگاه‌ها در جهان است و نتایج آن می‌تواند بر اعتبار بین‌المللی، جذب دانشجو و همکاری‌های علمی دانشگاه‌ها اثر بگذارد.
@
VahidHeadline
برای نخستین‌بار از زمان آغاز انتشار رتبه‌بندی «دانشگاه‌های تأثیر‌گذار» موسسه آموزش عالی تایمز، نام هیچ دانشگاهی از ایران در نسخه سال ۲۰۲۶ این فهرست دیده نمی‌شود. رخدادی که در کنار افت مداوم جایگاه دانشگاه‌های ایران در دیگر نظام‌های معتبر رتبه‌بندی جهانی، بار دیگر وضعیت آموزش عالی کشور را زیر ذره‌بین برده است.
بر اساس نتایج منتشر شده، در رتبه‌بندی سال ۲۰۲۶ تایمز، یک‌هزار و ۶۴۶ دانشگاه از ۱۱۶ کشور بر پایه اهداف توسعه پایدار سازمان ملل متحد (SDGs) ارزیابی شده‌اند. با این حال، برخلاف سال‌های گذشته، نام ایران به‌طور کامل از این فهرست حذف شده و مؤسسه تایمز نیز تاکنون توضیحی درباره علت این موضوع ارائه نکرده است.
حذف نام ایران از این رتبه‌بندی در حالی رخ داده که دانشگاه‌های کشور از زمان آغاز انتشار آن در سال ۲۰۱۹ همواره در فهرست تایمز حضور داشتند. تنها در سال ۲۰۲۵، ۳۴ دانشگاه ایرانی در این رتبه‌بندی ارزیابی شدند و برخی از آن‌ها در چند شاخص توسعه پایدار، از جمله «سلامت و رفاه»، «آموزش باکیفیت»، «صنعت، نوآوری و زیرساخت» و «برابری جنسیتی»، جزو دانشگاه‌های برتر جهان بودند.
همزمان، نتایج تازه‌ترین رتبه‌بندی جهانی QS نیز از ادامه روند نزولی دانشگاه‌های ایران حکایت دارد. رتبه‌بندی QS که از معتبرترین نظام‌های ارزیابی آموزش عالی در جهان به شمار می‌رود، دانشگاه‌ها را بر اساس شاخص‌هایی مانند اعتبار علمی، کیفیت پژوهش، میزان استناد به مقالات، نسبت استاد به دانشجو، همکاری‌های بین‌المللی و اشتغال‌پذیری فارغ‌التحصیلان ارزیابی می‌کند.
در این ارزیابی دانشگاه تهران ۴۵ پله سقوط کرده و از رتبه ۳۲۲ به ۳۶۷ جهان رسیده است. دانشگاه تبریز ۱۰۸ رتبه، دانشگاه فردوسی مشهد حدود ۱۲۵ رتبه و دانشگاه‌های شیراز، اصفهان و آزاد اسلامی نیز افت قابل‌توجهی را تجربه کرده‌اند؛ به‌طوری که دانشگاه آزاد از جمع هزار و ۴۰۰ دانشگاه برتر جهان خارج شده است.
در مقابل، کشورهای منطقه روندی معکوس را طی کرده‌اند. ترکیه با ۲۵ دانشگاه در رتبه‌بندی QS حضور دارد و دانشگاه فنی استانبول به رتبه ۲۷۹ جهان رسیده است. امارات متحده عربی نیز سه دانشگاه در میان ۳۰۰ دانشگاه برتر جهان دارد.
حسین سیمایی‌صراف، وزیر علوم، کاهش سرمایه‌گذاری در پژوهش، ضعف همکاری‌های علمی بین‌المللی، کمبود زیرساخت‌های آموزشی و پژوهشی و محدود شدن فرصت‌های مطالعاتی را از عوامل افت جایگاه دانشگاه‌های ایران دانسته است.
شاهین آخوندزاده، معاون تحقیقات وزارت بهداشت، نیز اعلام کرده بود که محدودیت‌ها و اختلال‌های گسترده اینترنت در سال ۲۰۲۶، پژوهشگران ایرانی را حدود یک‌سوم سال از فعالیت علمی بازداشت؛ موضوعی که به گفته او می‌تواند به کاهش حدود ۱۰ هزار مقاله علمی و افت بیشتر جایگاه علمی ایران منجر شود.
کارشناسان آموزش عالی نیز می‌گویند کاهش ارتباط دانشگاه‌های ایران با مراکز علمی جهان، محدودیت در جذب استاد و دانشجوی خارجی، کاهش بودجه پژوهشی، ضعف زیرساخت‌های آموزشی و دسترسی محدود به منابع علمی بین‌المللی، از مهم‌ترین عوامل کاهش رقابت‌پذیری دانشگاه‌های ایران در رتبه‌بندی‌های جهانی است.
رتبه‌بندی دانشگاه‌های تأثیرگذار تایمز از سال ۲۰۱۹ با هدف ارزیابی عملکرد دانشگاه‌ها در تحقق ۱۷ هدف توسعه پایدار سازمان ملل منتشر می‌شود و تنها نظام رتبه‌بندی جهانی است که نقش دانشگاه‌ها را در حوزه‌هایی مانند آموزش، سلامت، برابری جنسیتی، نوآوری، محیط زیست، عدالت و توسعه پایدار می‌سنجد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77618" target="_blank">📅 17:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYORdqJiOu54kDOKT6sF7llDwH4KDsN92DFilaNIfxQP-ZzZbzpwIv6ZLxGeRGD8afLuiF-LbPogk_UVIrYvHUcfLp-IvEdfS8p1SqYjBldQknB9rrHNh3rMeaAUc0DoT12DNC-aw_VN6jixPZIj3C0WZeg96CjrgnSQzlWZAYTWuN9dxCQncUk1OJqUzXt4vi7ufnhjAAC2RdcJoYhj2a3uVSZNyNTsw-Upztjz8DdunwKamlUJt9t685-VCVOJzgE1R0nmn5nvp2lTbEtrVfyNOr8ExLupHok9yJtAa0jLZIWiqS3gYmbp5839FK-w3OwYuTB3IsuKOBt8DPjGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه پس از آنکه ارتش ایالات متحده اعلام کرد چندین موشک بالستیک شلیک‌شده از سوی ایران به سمت نیروهای آمریکایی در خاورمیانه را رهگیری کرده است، وعده داد که ایران را به‌شدت هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز گفت: «حسابی نابودشان خواهیم کرد. خیلی سخت به آنها ضربه خواهیم زد.»
این گفت‌وگوی تلفنی به‌صورت کامل پخش نشد، اما یکی از خبرنگاران فاکس نیوز خلاصه‌ای از اظهارات ترامپ را منتشر کرد.
@
VahidHeadline
گفت: حسابی نابودشان خواهیم کرد. ضربات سختی به آنها خواهیم زد و به‌شدت تنبیه خواهند شد.
ترامپ همچنین درباره حملات هوایی آمریکا و عربستان سعودی به شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق گفت این حملات با هماهنگی دولت عراق انجام شده است.
رییس‌جمهوری آمریکا این شبه‌نظامیان را «سرطانی برای جهان» توصیف کرد و گفت در حال بررسی صدور هشدارهای بیشتر علیه نیروهای نیابتی جمهوری اسلامی و ارتباط آنها با حکومت ایران است.
ترامپ همچنین گفت اکنون موضع بنیامین نتانیاهو درباره جمهوری اسلامی را درک می‌کند.
او در پاسخ به پرسشی درباره احتمال ادامه مذاکرات با جمهوری اسلامی نیز گفت: «اجازه می‌دهیم به گفت‌وگوهایشان ادامه دهند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77617" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=XkQ00f9Deh3g4aBxHtQFtyXmJ4dmjDuaFm_IJHyns8Ql_w8ify5aDjR7mFPaJlMqYNpGTFNGD4n1uT8uKq4iRLs4j2N3t4QY-dEB0PMERBatn6huIJ3Vo5ejNSEU879Xr8apPtpnNNjHZSyA7xmwlM0Q7DP6vhDhJ3VvmL_HLJnII9EYqRj6UKpPbeTrUa6g2t049d3oPs8EwxJ3elGHRVulsfjIdRhsZ4UgRL3T16beghK7uiaMOoOGc-Zg6N7ECBOiWf-846UMc2e1OHrgONXVYyhSLNsoBTDj3yevC_bGvLNd7Ya9AW62FKdS9UVyhuBZ1U16Ag5T4q3Zkq0wMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=XkQ00f9Deh3g4aBxHtQFtyXmJ4dmjDuaFm_IJHyns8Ql_w8ify5aDjR7mFPaJlMqYNpGTFNGD4n1uT8uKq4iRLs4j2N3t4QY-dEB0PMERBatn6huIJ3Vo5ejNSEU879Xr8apPtpnNNjHZSyA7xmwlM0Q7DP6vhDhJ3VvmL_HLJnII9EYqRj6UKpPbeTrUa6g2t049d3oPs8EwxJ3elGHRVulsfjIdRhsZ4UgRL3T16beghK7uiaMOoOGc-Zg6N7ECBOiWf-846UMc2e1OHrgONXVYyhSLNsoBTDj3yevC_bGvLNd7Ya9AW62FKdS9UVyhuBZ1U16Ag5T4q3Zkq0wMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته نیروهای آمریکایی و عربستان سعودی در عملیاتی مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در شرق عراق را هدف قرار داده‌اند.
@
VahidHeadline
بر اساس گزارش‌ها، پایگاه‌های حشد شعبی در استان‌های دیاله، کرکوک، کربلا و نینوا هدف حمله قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77615" target="_blank">📅 16:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD894ezkkZ1k--3N_Nl_70-93nrATBMQ9DEc4ex0FlV_eNs07LWUL6-1C0IN54Zf1Y4cLHqNdTxYXTtYS4yw0xa_0Vq9RLIWofoTvw_gKCwQkmjm7rJ8cP2wcgw44SiZpF6my3xiv1JIGuypPv07gx7Vuh8VfzJEITvKKijAMKwUZUoJVXLrnTcF1HRpUCSHLI2J-qqjfJZNSuXIIBxS-Ehr3IWKbOmryvUObBLp6XRFl2XrfsMGjbJgPlnop2NwM1HRH-2YqhnkfbpjIyUM2AwiWgPZK5cmH844ALAcSiVox9h4dFOizEbIdKmP2L7pUg4Hvj5gD1TWVhxwWRMUgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرحی را به مرحله بعد فرستاد که در کنار تشدید فشار اقتصادی بر روسیه، تحریم‌های مرتبط با ایران را تا سال ۲۰۳۱ تمدید می‌کند.
این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، هنوز باید در رأی‌گیری نهایی سنا تصویب و سپس در مجلس نمایندگان بررسی شود.
@
VahidHeadline
و  در خبری دیگر:
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) اعلام کرد ۱۰ شرکت و هشت نفتکش را به فهرست تحریم‌های خود افزود.
این تحریم‌ها بر اساس فرمان اجرایی ۱۳۹۰۲ و در ارتباط با جمهوری اسلامی اعمال شده‌اند.
در میان نهادهای تحریم‌شده، «اداره خدمات دریایی هرمزسیف» و «شرکت بیمه دریایی خلیج فارس» در ایران نیز قرار دارند.
وزارت خزانه‌داری آمریکا همچنین اعلام کرد این دو نهاد مشمول تحریم‌های ثانویه هستند.
شرکت‌های تحریم‌شده در هنگ‌کنگ، جزایر مارشال و چین ثبت شده‌اند و نفتکش‌های تحریم‌شده نیز با پرچم کشورهای مختلف فعالیت می‌کنند. این نفتکش‌ها به شرکت‌های تازه تحریم‌شده مرتبط معرفی شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77614" target="_blank">📅 16:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpEOB-sE91Y2Cz3K4MJeW2VIP9YeTC38aGKyLTHRX_f4YUZel4oGnRIjbKEd1G3-rj2FcPqUlWvGYqS_-eLN7rfd4PmjHcNMnEfuMJ5eXNnW7qDQaoANTzJ2UDq277ec5aU0m2I2-7zp3CjgrpsaJpxzu54YtvoyLb5XOa_48BYPbhmFS9qQcm5VSVS6DDqxU3NiBtmIMPdXwjpP9pJN7Fh_miigQwlP97H5IbGqzfYDInTKaZydvg-Rl8MbD98qZQgKQjbYHKXh_5Gg4uxewgiw7trc_O1MCMdIDt4hZykWYjOi-GE6i9KCCMcQCrDf_rrXDfECnarc9xJ4cd7eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع منطقه‌ای گزارش داد که حوثی‌های یمن در حال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب هستند؛ اقدامی که به گفته این منابع، پس از اعلام محاصره دریایی عربستان سعودی مطرح شده و می‌تواند فشار بر آمریکا را افزایش دهد.
به گفته این منابع، حوثی‌ها در حال بررسی دریافت عوارض از بیشتر کشتی‌هایی هستند که از باب‌المندب، گذرگاه راهبردی میان دریای سرخ و خلیج عدن، عبور می‌کنند، اما هنوز زمان مشخصی برای اجرای این طرح تعیین نشده است. دفتر رسانه‌ای حوثی‌ها به درخواست رویترز برای اظهار نظر پاسخ نداد.
دو مقام منطقه‌ای که از سوی جمهوری اسلامی در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند مقام‌های حوثی در سفر خرداد به ایران برای شرکت در مراسم تشییع جنازه علی خامنه‌ای، درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب با مقام‌های جمهوری اسلامی گفت‌وگو کرده‌اند. به گفته منابع، هدف از این طرح عادی‌سازی دریافت عوارض از آبراه‌های بین‌المللی و افزایش فشار بر آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77613" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbfbmJfdtu_csxYzaomjB_QPoxF4INOT3xvr3cJg4-UCZIyN3IbzmdfLnyB5-SYTGhk-gT1z702mrGtV6dlP1Lk9oqBS-lS30C0XxT1_y49wDzRHRBQkSj--yfnuNgP7CeFaHipdw0qMz7rWgEMdf3Odom2EsDsAnD0QQE_VlgutAOKvjucOvRdy0tCxoDbdvDlw2GBDDmIM1JUsvVtSwmsQVsuDmndVqmkznhUZld3gRzx2Fp-ZTPegFhvvjWhllS8cfoG5UZmXXg7dg-7NFD5ruElB6L4tbMiVpMG4fpd0cDgzb2XYzHjEx91w1IK-Av_vp-jBy85Dt1oLkNXZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون دولتی جمهوری اسلامی گزارش داد منطقه‌ای در نوار مرزی پیرانشهر در استان آذربایجان غربی هدف حمله هوایی آمریکا قرار گرفته است. در این گزارش آمده است: «منطقه‌ای در نوار مرزی پیرانشهر مورد حمله هوایی دشمن آمریکایی قرار گرفت.»
پیش از آن، خبرگزاری فارس به نقل از یک مقام استان آذربایجان غربی گزارش داده بود موشکی به منطقه‌ای غیرمسکونی اصابت کرده و تلفاتی بر جای نگذاشته است.
فرماندهی مرکزی آمریکا تاکنون این حمله را تأیید نکرده و درباره آن اظهار نظری نکرده است. تأیید مستقلی نیز برای این گزارش وجود ندارد.
پیرانشهر در غرب استان آذربایجان غربی و در نزدیکی مرز عراق قرار دارد. این شهر پنج روز پیش نیز بر پایه گزارش سازمان مدیریت بحران استان به خبرگزاری ایرنا، هدف حمله هوایی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77612" target="_blank">📅 16:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4Rw2N9q7hXgUciDWfTjytbts781enG3ngHP3RD6lEScjFlPGTCMN-KNWdTBZgB6pzvGhJJMuw_Tw_MbigCmWtwK1XrgO89csBEaTtGBJnQCt8cQIefBwvw7i0debZO1xtaUp1RXdeYo2UfySvy0pgmNA1iGaC3Gl5LLGtKotQxfnZfEfIL_84V6hGpOz1ZTce5SnkYyjLLsfe4-tAFX-f36xwQFN7hu3x-MiXBazyF8ZHjuRIkLGKmWDQE_iGQxytnGbQdDVpBagHfyisFhk8OM1ERS9OXpQ7JxYL9ZZ3aY8labAZVIvxMHyZ-CLKFpt_TSjYx_mrK4vtC0tEy_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر، رهبر جریان صدر عراق و از رهبران شیعیان عراق، با انتشار بیانیه‌ای از سپاه پاسداران خواست خاک عراق را هدف حملات خود قرار ندهد و هم‌زمان از گروه‌های مسلح عراقی نیز خواست با اقدامات خود به کشورهای منطقه بهانه حمله ندهند.
صدر در این بیانیه که روز چهارشنبه هفتم مرداد منتشر شد، نوشت عراق نباید به محلی برای هدف قرار دادن جمهوری اسلامی تبدیل شود و از «برادران در سپاه پاسداران» خواست از حمله به «سرزمین مقدس و مستقل عراق» خودداری کنند.
او همچنین از آنچه «میلیشیاهای خودسر» خواند، خواست با اقدامات خود زمینه حمله کشورهای عربی خلیج فارس به عراق را فراهم نکنند.
رهبر جریان صدر با محکوم کردن هدف قرار گرفتن خاک عراق از سوی هر کشور یا هر طرفی، از دولت بغداد خواست حاکمیت خود را اعمال کند، امنیت را برقرار سازد و مانع کشیده شدن این کشور به جنگ و درگیری‌های فرقه‌ای شود. او تاکید کرد عراق و مردمش بیش از هر چیز به صلح نیاز دارند و سال‌ها جنگ، توان و ظرفیت‌های این کشور را فرسوده است.
این بیانیه در شرایطی منتشر شده که از آغاز جنگ ۴۰ روزه، سپاه پاسداران بارها مواضع احزاب کُرد در اقلیم کُردستان عراق را هدف قرار داده است. هم‌زمان، فرماندهی مرکزی ارتش آمریکا (سنتکام) بامداد چهارشنبه هفتم مرداد اعلام کرد نیروهای آمریکایی و عربستان سعودی در یک عملیات مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در عراق را هدف قرار داده‌اند.
@
VahidHeadline
مقتدی صدر در بیانیه‌اش به جای خلیج فارس از عبارت دیگری استفاده کرده:
Mu_AlSadr
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77611" target="_blank">📅 16:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtOTX_4bVZJnvvb3DnIi32w0YvnO9lhDmdVs8DbxTxhsso9IHS82lfAQFQT7webMQDW_0xVTObAsvrUmZ3OBhknB4GQxE3i7WbIXI-w1ZpOoj8kcEhIgc8O7yGi_Jc-LkVdTXE1J8UdVY62uWdDK_10HhkMi4dtsmmRrS__N1OM2u2O2ldl09F7oUeM9WJUHBY7cHmlx5yPwfYwwGF8OEvfnN4tV_D6o-djlz584HPf6HX237gcQoKKJUEx_a6HAClfcMb5nrjDh_eAahDX_ZaCFdss9hJmjymUypbBkDkmJrBOgXAF3aMU5ULYN6IUrGKkD7NYZfKxyo2UzVufpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ نیویورک‌تایمز، به نقل از چند مقام ایرانی و غربی که نام‌شان اعلام نشده، گزارش داد که حکومت ایران قصد داشت در واکنش به حملهٔ اوکراین به یک کشتی ایرانی، به یک بندر در اوکراین حمله کند، اما به‌دنبال اقدامات دیپلماتیک از انجام این اقدام خودداری کرد.
این روزنامه به نقل از این مقام‌ها نوشته است که انتظار می‌رفت ایران در این حمله یک موشک بالستیک با کلاهک کوچک به سمت اوکراین شلیک کند تا خسارت نسبتاً کمی به بار آورد و به‌صورت نمادین پاسخی به حملهٔ اوکراین داده باشد. این مقام‌ها گفتند که هدف حمله احتمالاً یکی از بنادر اوکراین در دریای سیاه بود.
بر اساس این گزارش بامداد چهارشنبه هفتم مرداد منتشر شد، مقام‌های جمهوری اسلامی امیدوار بودند این درگیری با حملهٔ تلافی‌جویانهٔ آن‌ها پایان یابد، اما مقام‌های غربی هشدار دادند که پیش‌بینی چگونگی واکنش اوکراین دشوار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/77610" target="_blank">📅 16:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KcDEgVhw5H1Nm7tQq819T_l61a9611hwpOuhnOuhfnGpsUzfhUu89KluJAC1uq27476fqpsQNdj499cLqWCzeN0ZsCu3P5d8dGvg-U9u5qSNmx3PeYcIoefu_mPM3BEnqMCKTpdWu3STJ6WtBUfiNI3waDoWbdp8ga_wRQNWNTlSR4k82g5WapDyqFA9gzGf_VGmxNdX-t7KbjQiLfvYqpLOnnK8248dpZpJLM3cWGtJaCwDg5a0cB3E-GfWoR3546FwZ5ACO8Cl4YbiQQgS-1R4nSE9u-EejqmHXzvD5cc2uLgX3D_wVm5MGC3XH1dXTHr7FmkxyBO2tqptW240cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BRuoiNXqP9RVSjqjcx1Hys1U6q5aeWbG2yj-CmJK0GZtYusyaK277fuyyF-a6Inz6JBBz44EXmgkbAC5_fQqjCnw6RwQSyvIrCQvXF6S1_j2CamYlO54s189RkbWSKsHmpiCwI0VojVm8dT7UyLUYYXbCDtRps47Si64JxhAIr29BqUTl-3D0V4qS9mkNq0m8G8rcVAwi8Xbk_o-osSYK5G5uXJJTZqxuLrII-SFWQwJsR8f1KvrB5i2LyvtkvHoIY8jvvSANTTYKZSdVqPb_fTfpxXK-GAmmsgHmoPWr48b33XCfSvvWBhl9Cm6gb8VKjpcxF8kMnFwIK5SWDvE0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برخی رسانه‌های ایران و کانال‌های مرتبط با سپاه پاسداران گزارش دادند که چهار عضو سپاه پاسداران در حملات منتسب به آمریکا و عربستان سعودی به عراق کشته شدند.
به نوشته این رسانه‌ها، این افراد در حمله‌ای به کربلا جان باختند.
بر اساس این گزارش‌ها، علی اصغر آستانه، ابوالفضل متقی، مرتضی اکبری و امیرعباس درهم‌فروش از جمله کشته‌شدگان هستند.
@
VahidOOnLine
شبه‌نظامیان حشد‌ الشعبی صبح چهارشنبه هفتم مرداد اعلام کردند شمار کشته‌های حملات هوایی مشترک آمریکا و عربستان سعودی به پایگاه‌های این نیروهای تحت حمایت ایران به ۲۰ نفر رسیده است.
حشد الشعبی در بیانیه‌اش این میزان تلفات را آمار «اولیه» خوانده و گفته است که دست کم ۳۲ نفر نیز در این حملات مجروح شده‌اند.
حملات مشترک آمریکا و عربستان علیه مواضع نیروهای حشد الشعبی در بغداد، واسط، نینوا، بصره، کرکوک، کربلا و دیاله انجام شد و خسارات مادی به تأسیسات و تجهیزات نظامی نیروهای حشد الشعبی وارد کرد.
فرماندهی مرکزی ارتش آمریکا در بیانیه‌اش گفته بود که این شبه‌نظامیان طی روزهای اخیر بیش از ۲۴ حمله پهپادی انجام داده‌اند.
به‌گفتهٔ سنتکام، هدف این حملات «تروریست‌های همسو با ایران» بوده است که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77608" target="_blank">📅 16:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=Y2v36nySpdIHXIC7VhS2Nveq1hQmr9ryEkSM7kEzPsqYnMM9zZ1_7GBSEzyzBRdAZRe_A01xo2M_XbqcVnU-NyNIrytjM-iW3oj-VjO29708LQGLLcBFruGyJfNLhBhC-MMK2l4m8BwY7nK0a9Slsj_UHLfjaQzRRNUfVpto8oq-HzovWuLs2Cnmy-kOARA4kngu-wT9EBP21XIZGxP9WZZVJaqUki7gLY_jDsrWpuQkUQfYZQm064EHbkhCZVff71IoeNy-UoMYxpJc0YPnRfieuNEDn2FI9gG7DCHXkdMZMn0BqpgD2E2ggXsWgnnwouYTTi9dFdUTrs9s3ubj77gfLXWpwfRBQ0UeGmyBuyiU3r8arHAf6ZRZcx6dCAT3RI9rbfD8Ws_1PAp6BO35DeVTwkBALiMXJMoT1kniGS9-zvN6YQd19dXYmlIHh9MzzsjxwQ2gNOneYeeXQdxf1weWREdHMX7RVFDkGfT8q5U-emnJ49CuF1XeynobFoPbXjRr_9l51YykBCiU1f3-IPjn6Os8l4hSVPIM8e-jojnkhVSajrF1xFARzoFFCYNDiEcDWMoH3r3G3xPT6q0SwVkrpnFxR_v4uSEPbdcXJn0eMOXwATL0YFWusWIVr2KS2UP1Jrg0Z6_dNFLZ98n5_UBU2GirmXbyKxJeWAYwPcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=Y2v36nySpdIHXIC7VhS2Nveq1hQmr9ryEkSM7kEzPsqYnMM9zZ1_7GBSEzyzBRdAZRe_A01xo2M_XbqcVnU-NyNIrytjM-iW3oj-VjO29708LQGLLcBFruGyJfNLhBhC-MMK2l4m8BwY7nK0a9Slsj_UHLfjaQzRRNUfVpto8oq-HzovWuLs2Cnmy-kOARA4kngu-wT9EBP21XIZGxP9WZZVJaqUki7gLY_jDsrWpuQkUQfYZQm064EHbkhCZVff71IoeNy-UoMYxpJc0YPnRfieuNEDn2FI9gG7DCHXkdMZMn0BqpgD2E2ggXsWgnnwouYTTi9dFdUTrs9s3ubj77gfLXWpwfRBQ0UeGmyBuyiU3r8arHAf6ZRZcx6dCAT3RI9rbfD8Ws_1PAp6BO35DeVTwkBALiMXJMoT1kniGS9-zvN6YQd19dXYmlIHh9MzzsjxwQ2gNOneYeeXQdxf1weWREdHMX7RVFDkGfT8q5U-emnJ49CuF1XeynobFoPbXjRr_9l51YykBCiU1f3-IPjn6Os8l4hSVPIM8e-jojnkhVSajrF1xFARzoFFCYNDiEcDWMoH3r3G3xPT6q0SwVkrpnFxR_v4uSEPbdcXJn0eMOXwATL0YFWusWIVr2KS2UP1Jrg0Z6_dNFLZ98n5_UBU2GirmXbyKxJeWAYwPcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند از ابتدای سال ۲۰۲۶ تاکنون، اعدام دست‌کم ۸۸۶ نفر در ایران را مستند کرده است که ۵۶ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
زندان قزل‌حصار یکی از بالاترین آمار اجرای احکام اعدام را در سراسر کشور دارد. همچنین بخش قابل‌توجهی از اعدام‌های صورت‌گرفته در ایران مربوط به جرایم مرتبط با مواد مخدر است؛ به‌طوری که طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مرتبط با مواد مخدر بوده است.
🔸
از ۲۲ تیرماه، در پی انتقال شش زندانی محکوم به اعدام در پرونده‌های مواد مخدر به سلول‌های انفرادی زندان قزل‌حصار، جمعی از زندانیان واحد دو این زندان دست به اعتصاب غذا زده و برخی نیز لب‌های خود را دوخته‌اند.
🔸
با گذشت بیش از دو هفته از آغاز این اعتصاب، مسئولان نه تنها هیچ پاسخی به خواسته‌های اعتصابیون نداده‌اند، بلکه با اقداماتی همچون جابه‌جایی زندانیان و ایجاد محدودیت‌های شدیدتر برای جلوگیری از ارسال پیام و ویدیو از داخل زندان، در تلاش‌اند صدای آنان را خفه کنند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77607" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز: منابع می‌گویند ایران ظرف چند هفته سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد
▪️
منابع می‌گویند قرارداد شامل ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی دوش‌پرتاب QW-12 و FN-16 است
▪️
منابع می‌گویند ارزش این معامله ۶۰ تا ۷۰ میلیون دلار است
▪️
چین این گزارش را بی‌اساس خوانده و پاکستان دخالت در انتقال‌ها را رد کرده است
ترجمه ماشین:
۲۹ ژوئیه (رویترز) — سه منبع آگاه از این معامله به رویترز گفتند ایران قرار است ظرف چند هفته نخستین محموله از مجموع حداکثر ۴۰۰ پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که هم‌زمان با بازسازی توان دفاعی این کشور در میانه جنگ با ایالات متحده صورت می‌گیرد.
این خرید که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد شده، یکی از بزرگ‌ترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است؛ جنگی که ضعف‌هایی را در توانایی ایران برای حفاظت از مراکز نظامی و زیرساخت‌های راهبردی آشکار کرد.
با خبرنامه Trading Day، تحولات بازارهای جهانی را بهتر درک کنید. از اینجا ثبت‌نام کنید.
به گفته منابع، این قرارداد خرید بین ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، شامل موشک‌های چینی QW-12 و FN-16 را در بر می‌گیرد.
این قرارداد با شرکت Zhongqing Baoshang International Investment، مستقر در هنگ‌کنگ، امضا شده است؛ شرکتی که به گفته منابع، به‌عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
ایران پس از ماه‌ها جنگ نیاز به تجدید تسلیحات دارد
منابع به‌دلیل حساسیت موضوع، به شرط ناشناس ماندن صحبت کردند. وزارت امور خارجه ایران بلافاصله به درخواست اظهارنظر پاسخ نداد.
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین همواره در جهت ترویج صلح و پایان دادن به درگیری نقش ایفا کرده است.»
گروه Zhong Qing Bao Shang مستقر در پکن، شرکت مادر Zhongqing Baoshang International Investment، تا روز سه‌شنبه به درخواست اظهارنظر ایمیلی پاسخی نداده بود.
ایران پس از ماه‌ها درگیری، که طی آن آمریکا و اسرائیل تأسیسات مرتبط با برنامه‌های موشکی، پهپادی و پدافند هوایی این کشور را هدف قرار داده‌اند و تهران نیز با شلیک انبوه موشک‌های بالستیک و پهپادها پاسخ داده، نیازمند تجدید تسلیحات است.
این درگیری دشواری دفاع از مراکز ثابت نظامی و راهبردی در برابر هواپیماهای پیشرفته و تسلیحات هدایت‌شونده دقیق را برجسته کرده است.
واشنگتن روز شنبه به‌طور ناگهانی بمباران‌های دو هفته‌ای خود را متوقف کرد، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت اگر مذاکرات برای پایان دادن به این درگیری پنج‌ماهه شکست بخورد، حملات از سر گرفته خواهد شد؛ درگیری‌ای که در ظاهر از ماه آوریل در وضعیت آتش‌بس قرار داشته است.
تحویل صدها سامانه پدافند هوایی دوش‌پرتاب، موجودی تسلیحات پدافند هوایی کوتاه‌برد ایران را به‌طور قابل‌توجهی افزایش خواهد داد و نشان می‌دهد روابط نظامی این کشور با چین در حال عمیق‌تر شدن است.
منابع هشدار دادند که هرچند توافق امضا شده است، برنامه زمانی تحویل، تعداد سامانه‌ها و دیگر جزئیات اجرایی همچنان ممکن است تغییر کند.
بر اساس طرحی که طرفین بر سر آن توافق کرده‌اند، تحویل‌ها در مرحله نخست از طریق هوایی و از ارومچی در غرب چین انجام خواهد شد و سپس با عبور از پاکستان به ایران خواهد رسید. منابع مشخص نکردند که انتقال از پاکستان به ایران هوایی خواهد بود یا زمینی.
روابط عمومی ارتش پاکستان، ISPR، اعلام کرد: «گمانه‌زنی‌ها درباره دخالت پاکستان در انتقال تسلیحات پدافند هوایی از چین به ایران کاملاً ساختگی و نادرست است.» سخنگوی وزارت امور خارجه پاکستان به درخواست‌ها برای اظهارنظر پاسخ نداد.
منابع می‌گویند چین و ایران مسیرهای زمینی برای تحویل را بررسی می‌کنند
کارشناسان نظامی می‌گویند با آنکه ایران طی دو دهه گذشته سرمایه‌گذاری گسترده‌ای در زمینه موشک‌ها، پهپادها و رادارها انجام داده است، سامانه‌های پدافند هوایی قابل‌حمل اهمیت دارند، زیرا می‌توان آن‌ها را به‌سرعت پراکنده کرد، با تیم‌های کوچک به کار گرفت و مرتباً جابه‌جا کرد؛ ویژگی‌هایی که آن‌ها را در مقایسه با آتشبارهای ثابت پدافند هوایی کمتر آسیب‌پذیر می‌کند.
یک منبع امنیتی اروپایی گفت مقام‌های کشورش از چند قرارداد در حال مذاکره درباره فروش احتمالی سامانه‌های پدافند هوایی دوش‌پرتاب سری QW به ایران، از جمله سامانه‌های QW-12، QW-18 و QW-19، اطلاع دارند.
یک منبع امنیتی دوم در خاورمیانه گفت ایران به‌دنبال خرید موشک‌های QW-12 و QW-18 بوده است، اما او از نهایی شدن قرارداد اطلاعی نداشته است.
‏QW-12 و FN-16 سامانه‌های موشکی زمین‌به‌هوای دوش‌پرتاب و هدایت‌شونده با فروسرخ هستند که برای درگیری با هواپیماهای در ارتفاع پایین، بالگردها و پهپادها طراحی شده‌اند. قابلیت تحرک آن‌ها امکان استقرار سریع در اطراف تأسیسات نظامی، زیرساخت‌های انرژی و دیگر مراکز حساس را فراهم می‌کند.
تحلیلگران دفاعی QW-12 را ضعیف‌تر از مدل‌های جدیدتر خانواده QW، از جمله QW-18 و QW-19، می‌دانند، اما می‌گویند این سامانه‌ها همچنان می‌توانند لایه‌ای مؤثر از حفاظت کوتاه‌برد در برابر پهپادها و اهدافی که در ارتفاع پایین پرواز می‌کنند فراهم کنند.
دو منبع اطلاعاتی غربی و یک مقام ایرانی گفتند تهران همچنین استفاده از مسیرهای زمینی را برای انتقال محرمانه‌تر تجهیزات نظامی و قطعات دومنظوره چینی و کاهش خطر ایجاد اختلال در انتقال بررسی کرده است.
این خرید نشان‌دهنده تداوم اتکای جمهوری اسلامی به ترکیبی از تولید داخلی تسلیحات و تأمین‌کنندگان خارجی، با وجود سال‌ها تحریم و محدودیت بر واردات مرتبط با امور دفاعی، است.
رویترز پیش‌تر به نقل از افراد آگاه از مذاکرات گزارش داده بود که ایران به امضای توافق جداگانه‌ای با چین برای خرید موشک‌های کروز ضدکشتی نزدیک شده است. رویترز نتوانست مشخص کند که آیا آن توافق نهایی شده است یا نه.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77606" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_4jNOLyFK4-tY3ro6JE3Ano11YahQt7HU7NAqJMMq2IyPXQvoNNqR_f4yEtW6ppAvqNhlicpVTFH3a70CFZRVeuu4jE4y8jH_Kd1sX_fEfGKT3oQHI-j75s3msLNyVJW6-cZpEMQkMbfTLLolZ6tCGQ4kkpz_mdXg6ziSPDNcZtgBCiA6KrUc3_bDiBEPCbmuqV_x88oqXFX0HEK5YJv5iJM7ajFI4QPnzqT55AdT8xWPiGrY7VO4wPnHuFkHl74x5xwviapSItdSTZH4_t29BWsqdOlgGsH-oYay-yRFVMmWtahwNNArqMUSMd0ZjiCBG63wKU_l8mJlFxpjtAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی ایران هویت خلبان کشته شده مجید کاظمی رو پس از چند ماه اعلام کرد.
نوشتند یکی از ۴ خلبان دو جنگنده سوخو ۲۴ بوده که در حمله به نیروهای آمریکایی در پایگاه العدید قطر هواپیماشون مورد هدف قرار گرفت.
نوشتند تلاش‌ها برای تعیین وضعیت ۳ نفر دیگر همچنان در جریان است و مجید کاظمی هم با آزمایش‌های تخصصی و بررسی DNA هویتش تایید شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77605" target="_blank">📅 07:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJS1SUYab-h6hmzMocFqGgctqHlfb-FW8KzagpaW_jkwKE7yR4qJuRV3clbskLDbo4YajJHuIXOzuvPgGQb7h__wIZ9AThFVXxp8J-CxlSm7-1-JvcY5bN00__P9RYB3Qx9VmYAgzn1Oa2HVZuZ98T0SxrSRs0ED1V9oggf5Tor_YyhGutXNadii3rT0Rlg65HRyBui_f5iSDS-3oiynK5OXM72QQ_k3Z-_duuTbUA1kL9p7fc-ak05PtzJpZZisPR0FSOtMGaGaSNT5MLoMpmrwt7ulT5zeCsujuOyFfxirxVrcPfwtQ6M01efiZD41PmVqr7iNPYRjFDUvcDhVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران، صبح چهارشنبه، با انتشار دو بیانیه از حمله موشکی به پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن و همچنین هدف قرار دادن سه نفت‌کش خبر داد.
نیروی هوافضای سپاه اعلام کرد پایگاه نیروهای آمریکایی در اردن را با چند موشک بالستیک هدف قرار داده و هم‌زمان نیروی دریایی سپاه نیز گفت: «سه نفت‌کش متخلف که به اخطارها بی‌توجه بودند مورد اصابت قرار گرفته و متوقف شدند.»
این درحالی است که پیش از این، فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار بیانیه‌ای اعلام کرد که تمام موشک‌های شلیک‌شده سپاه از ایران به طور کامل رهگیری و منهدم شده‌اند و هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77604" target="_blank">📅 05:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، می‌گوید دونالد ترامپ، رئیس‌جمهوری آمریکا، با اعطای مجوزهای لازم برای تولید موشک‌های سامانه پاتریوت به اوکراین موافقت کرده است.
آقای زلنسکی شامگاه سه‌شنبه در گفت‌وگو با شبکه فاکس‌نیوز گفت پس از دیدار با آقای ترامپ، با نمایندگان چند شرکت بزرگ تسلیحاتی آمریکا نیز گفت‌وگو کرده و امیدوار است زمینه تولید مشترک این موشک‌ها فراهم شود.
رئیس‌جمهوری اوکراین که روز سه‌شنبه در واشینگتن با دونالد ترامپ دیدار کرد، تأکید کرد مهم‌ترین نیاز نظامی کی‌یف همچنان سامانه‌ها و موشک‌های دفاع ضدبالستیک است.
هم‌زمان، سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرح گسترده‌ای را برای تشدید فشار اقتصادی بر روسیه و ایران به مرحله بعد فرستاد. این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، به رئیس‌جمهوری آمریکا اجازه می‌دهد بر بزرگ‌ترین خریداران نفت و گاز روسیه تعرفه‌هایی تا سقف ۲۰۰ درصد وضع کند و تحریم‌ها علیه نهادهای مالی، مقام‌ها، الیگارش‌ها و ناوگان موسوم به «سایه» روسیه را گسترش دهد.
این طرح هنوز باید در رأی‌گیری نهایی سنا تصویب شود و سپس برای بررسی به مجلس نمایندگان برود؛ مجلسی که تا پایان تعطیلات ماه اوت تشکیل جلسه نخواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77603" target="_blank">📅 05:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRXj0s_alNoOUTeOZKNyJrelnthsCDMXd1y8kivpMxApvmOU8HRopwj8pHhZE5TGIIsdyZUyNr5jidfpXP5pIPaSQzTaxP6Wz085gpSSDzSo_PDQKVTvNl3najOHopud5eJRFCMELEBJf3obb1qIku_HJPUKzc6Ol_eVIncL9Ot2RqJqWvRODaSvWMyJNtH7sABsv1KNgJsMXdRnNsM4OE2-IiEsK7u-3GJnB5aY4l70coUU_8LJ6Zm8IXbwgoMgn1ApUjpdxI-_ocfdQ0cEmgeMXTHSYVkarWnKdOPAqJcDMi1Ge94H5QK0mxRAucrP8ArYJYzId9FWXF9wJk7EYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، با انتشار تصاویری در «تروث سوشال» از دیدارهای جداگانه خود با رهبران اسرائیل و اوکراین، درباره دیدار با بنیامین نتانیاهو نوشت:
«نخست‌وزیر بی‌بی نتانیاهو از اسرائیل، همراه با من و نمایندگان، نشست بسیار خوبی داشتیم. بدیهی است که موضوعات مهم متعددی مورد بحث قرار گرفت.»
ترامپ همچنین با ابراز خرسندی از دیدار با ولودیمیر زلنسکی افزود: «دیدار با زلنسکی از اوکراین افتخار بزرگی بود. موارد زیادی بررسی شد و این نشست بسیار خوب پیش رفت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77602" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htYEu46Bb7FwTh60HPUINOKUKTlyGInLNpRXtZW6Pn35m2s-6iY815fSk_nSR6SjUMmiiMmNIJYm1gdIce6kpGOlU1VAx8W4ldEPvbDlD_g0x8lKev9ennBzQFd-X7xhxq64y6mMEy9GwJtsqgcz8esxNsyKNY2mtGTwlUFeWiDBWMANVGRwWGpHLD0iUm5lBrwB-okeQQiY4VNpuKKubjxM8phOaFRBOx1hg3WyXuuckpLZ9rzDxecUQ_vgPb5euH2aSCIuUuXPnUjSTDFOp6ZpWdNGWpa42BwxlKYaCf8VNuSdFxItxKXuW8tgfMDQhKZJZ2U5Urdu1tEob5aNxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست شده در اکانت سنتکام
متن پست، ترجمه ماشین:
نیروهای آمریکا و عربستان مواضع تروریستی مورد حمایت ایران در عراق را هدف قرار دادند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده و نیروهای مسلح عربستان سعودی روز ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند؛ عناصری که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان هدایت کرده بود.
جنگنده‌های آمریکایی و سعودی در پاسخی قاطع به بیش از ۳۰ حمله پهپادی هوایی که طی ۷۲ ساعت گذشته به دستور سپاه پاسداران انجام شده بود، چندین مرکز لجستیکی و انبار تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
حملات ناموجه علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، شبه‌نظامیان تروریست همسو با ایران در عراق بیش از ۶۰۰ بار تلاش کردند به شهروندان و تأسیسات آمریکایی حمله کنند.
سپاه پاسداران و نیروهای نیابتی تروریستی آن باید برای جلوگیری از واکنش نظامی بیشتر ایالات متحده، این حملات را متوقف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77601" target="_blank">📅 04:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0H0p2BE_yaIVrMrK7KzfGCkDXprSbvgjsXgsHGYLo7KqC9muSkA2RxudPnljnb2zcIRP5vZ9hPiOG7G0IXU40c2lYsQnbKWYXLmeoAtwPyfbCf2TZ8ggz4d5l3TIwQ86VOyDF454Z2wF2BiFm6O8fK3ShCQTDzK6p1W5DVA8ZgfYKEhyiIgeolRNK6xCN9vOTqxpoLyhRXXoNJo0NP8RberWqOUWcpCfWVJ1CiEOGY7IiyCG5Zqhjyz7PJGMHI0NIvv1zX7K5uG_U2Lx_dK5-TdSNcDhx7SY9mtr-KFyYyAnTYiuOnFj_vTi_sRvey4qAGS2fJ19DzOU3D_j-RNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور چند پهپاد را که تأسیسات نفتی در استان شرقیهٔ این کشور را هدف گرفته بودند، رهگیری و منهدم کرده است.
ترکی المالکی، سخنگوی وزارت دفاع عربستان، روز سه‌شنبه در شبکه اجتماعی ایکس گفت این پهپادها از خاک عراق و به دست گروه‌هایی که او «شبه‌نظامیان تروریستی مورد حمایت ایران» خواند، پرتاب شده بودند.
او افزود عربستان سعودی حق مشروع دفاع از خود و تأسیسات حیاتی‌اش را محفوظ می‌داند و «در زمان و مکان مناسب» به این حملات پاسخ خواهد داد.
@
VahidHeadline
خبرگزاری صدا و سیما می‌گوید که یک »مقام آگاه نظامی» در ایران، در واکنش به اظهارات وزیر دفاع عربستان سعودی، هرگونه ارتباط جمهوری اسلامی با پرتابه‌های شلیک‌شده از خاک دیگر کشورها به سوی اهدافی در عربستان را «قویاً» تکذیب کرده است.
این مقام که نام او اعلام نشده است، به این خبرگزاری گفت نسبت دادن هرگونه اقدام علیه منافع آمریکا در منطقه به جمهوری اسلامی ایران، «خطای بزرگ محاسباتی» و ناشی از «کم‌اطلاعی از اوضاع منطقه» است.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77600" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T6BB9J2l1F6NZX-7zvODPo6vTm8Bkqh2flnUPSpRtB7V-upKS-TNSEbYQBUSYonS_cnlrPoz4a_J_T_G8B3ihWzey0gu_Xvmc9E4SexVUwFAji7hvMy55SgKcE7WXsXSTPuB0fOfBayIHXarMUfBkkKCDeF9pevp9LKvlqoXDI8RLY-RBS2rNzUaddba2Ldc1MIlS6qChjfBB6hUNSnc5C6XhhnoBAXxwy0GRfZHGyGthIGYeMDseoxtXN6ce7QC9qqogPgGAmfM_K5Bn4UUjLAGXPBYXqZYCx6KqgtJBgCFqPdeREr97fQTXiTLF0bfWMIu5yD5-5ytB5wCZ00tZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرق آمریکا [۱:۱۵ چهارشنبه به وقت تهران]، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از ایران، در تلاشی برای انجام حمله‌ای غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند.
همه موشک‌های ایران با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنان هوشیار و در بالاترین سطح آمادگی قرار دارند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77599" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lGTJ3FOxgFSU_nIiwbeZl5DVvvF0xg7rQKmD8swAhR_IzZzQ01k607rTJdpklprYe-VsrrC2sRLfnPl0hTgCugXYaVaPW9vE0zIYit0F_Go5KKs7nAoqlLUqBIqLzhHNuuEbr8VdmZxKrpSNWuGB61XHwgQvKKLC029BXqnI1TN1VSm57Ny-5XW_dLfF6P3C5lEJgquGlMkm91oAaFRzL3xk7VIdxHkpecaThEjYaMONQ-tblP0LKy2kZ4GFvk_Svg6a5U5kyiWFbEp-WSUd4D7aTYIEe-MsZ0tvHXpGx65uB_05pvXjXGtx8z1m3ptcaHp_OvF0_2gVrvJoOqAcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oJhDoPJ-sxuGW6sd9_TDG8zqZA3EE81ToOi9Ysjbtrl5dX-uPjwtBtQGINSJjcXo2wk3OEnaEf2j5aLXFel04ceKakEUUJGq4-mwdb9JBFikQyAEpNlLiWbSG4sBQs4CvzXCi61kPiiT_z4LGNd6ehSX2sEQQex8-X7M3bJ8KL9ZqzVpzDLH-R1CrVqPMLd13wtZlW9hdzMZQFDqJ4sdNw4J1Wpf0AujufEbwQaSRGQyl3yUikEkkuCAa3zJZtmsPiNRKNLbkqiZCeb5S061Q9_tyhen72bLS80mLEWm3KSsj9hDfe7wxKX1ZCPKYbAo0GrBLdzlc9wd2W8pXTh-RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=sX4AwMxOLFaGJwrDfDwpzhTTLHorAkmLbXtsM1DUC4scA3BlK6Yj5EKQVXxbDS-qGwJfNZufDJ50tD5S5P-_N4vt3pvNFR_qK6y6acALdvYxDB3cGOtSegaxQUSnJwla9U6tvfQycvHcL9bTI8bKdMRGUb8f9Gkz6zbjJVWi-y59HSelc8fnTO5960G41T52I2pTZVSCN6yQDF-1q9KEI1snAnOiTvAwvVEvmMS-pBLAAr9RfQYsKEOGNMwL2w5uEoJs9h1uNSPVC9pyNgPXAxRo1O8LtSEohSfh0hMBFKOV_vE9NBmlH9qpCO6ZH2_UBDhWjV6pxLAs7en6TJz2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=sX4AwMxOLFaGJwrDfDwpzhTTLHorAkmLbXtsM1DUC4scA3BlK6Yj5EKQVXxbDS-qGwJfNZufDJ50tD5S5P-_N4vt3pvNFR_qK6y6acALdvYxDB3cGOtSegaxQUSnJwla9U6tvfQycvHcL9bTI8bKdMRGUb8f9Gkz6zbjJVWi-y59HSelc8fnTO5960G41T52I2pTZVSCN6yQDF-1q9KEI1snAnOiTvAwvVEvmMS-pBLAAr9RfQYsKEOGNMwL2w5uEoJs9h1uNSPVC9pyNgPXAxRo1O8LtSEohSfh0hMBFKOV_vE9NBmlH9qpCO6ZH2_UBDhWjV6pxLAs7en6TJz2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'پرتاب شدن چند موشک از
#خمین
'
تصاویر دریافتی از شهروندان با شرح بالا
چهارشنبه ۷ مرداد حدود ساعت ۱:۱۰ بامداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77595" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mge6N613Qssi0apEp2sD7hYVy65Kmd8KXxJR0btaGapXD3vdumTKOp7V2fuwWqHcdDmC-l94YMwTiTB708unkyWFDa67LlJr63VOAxs8a4mIq31P5tMV7cmw-_7fpTR4JaT7Cep6qyZucyAZjF4xPsU1sCaaJJDr37sRMuaJPSmiZ1vUJIgI82STmrrS3hZsr8esOuhn2_o4MDKzWgcpqDIaEr-KTTenHxzF5SZlZk9WR7WkXj9f7a5YJbh9YNH-izjmIqVuroBzbxHSkqzqdrklHaRnuQGMAMoXbB6UD0g22-dD28IpZhotbK7iVDQAAsFia1E_4phDvXrQQy-v2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
از خمین موشک بلند شد
سه تا صدای انفجار
همین الان از خمین ۶تا موشک زدن
۳تاشون صدا نداشت فقط نور قرمز بود
سلام همین الان یک موشک از خمین رفت.
داداش
خمین موشک زد
ساعت ۱ و ده دقیقه
وحید داداش ۴ تا موشک از خمین زدن همین الان
از خمین موشک زدن
سلام،الیگودرزم،،صدا ۳ شلیک موشک اومد صدا دور بود احتمالا ازخمین بود
پرتاب سه موشک خمین
سلام وحید جان
سه تا موشک تو آسمون لرستان از سمت اراک دیده شد
صدای انفجار تو آسمون لرستان میاد
من ستا موشک بین نهاوند و بروجرد دیدم خمین نبود فک کنم نتکنستم عکس بگیرم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77594" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=jpwLhbkqIlPfFz1ECKRV8JChjSTIHDiUtcKip-eRbHLHei0sZz3jU10Xtb5kBh_J9EddX22GO5X_wctdPBOIk7F1G6IOy5TnuasT36c6ooQazQWs7J06Y5bbBT2XZReR5znh0FJ5HJe9nI0ZpaNtzPqCiTSH_px2HmkNrpSFVaZsoxW8MHl0HhfuGVMn_CLL0X-L-sxVrH1Ox2iMoY3rlxUYxgk5HJwsBXxd5-Hzhg_puaPOu7KPynvKEBRi-QcNnwbbuNdrUpM-xM7s_htp6Mt7UBeQxehalwFvRXpEMXVXmItYzuLboXfaCy1eMiNEUew1-Fw5hzJYNQwkbDuLBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=jpwLhbkqIlPfFz1ECKRV8JChjSTIHDiUtcKip-eRbHLHei0sZz3jU10Xtb5kBh_J9EddX22GO5X_wctdPBOIk7F1G6IOy5TnuasT36c6ooQazQWs7J06Y5bbBT2XZReR5znh0FJ5HJe9nI0ZpaNtzPqCiTSH_px2HmkNrpSFVaZsoxW8MHl0HhfuGVMn_CLL0X-L-sxVrH1Ox2iMoY3rlxUYxgk5HJwsBXxd5-Hzhg_puaPOu7KPynvKEBRi-QcNnwbbuNdrUpM-xM7s_htp6Mt7UBeQxehalwFvRXpEMXVXmItYzuLboXfaCy1eMiNEUew1-Fw5hzJYNQwkbDuLBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ادای احترام به لیندزی گراهام، سناتور جمهوری‌خواه که ۱۱ ژوئیه در ۷۱ سالگی درگذشت، در ساختمان کنگره آمریکا
به غیر از نزدیکان آقای گراهام، صدها نفر از قانو‌نگذاران آمریکایی در مراسم حضور داشتند.
برخی از رهبران جهان هم برای شرکت در این مراسم به پایتخت آمریکا سفر کرده‌اند.
سناتور گراهام از ایالت کارولینای جنوبی بود که چهار بار به عضویت سنای آمریکا انتخاب شده بود. او در سال‌های ابتدایی فعالیت سیاسی خود از منتقدان سرسخت دونالد ترامپ، رئیس‌جمهور آمریکا، به شمار می‌رفت اما بعدها به یکی از متحدان وفادار او در کنگره بدل شد.
او از چهره‌های شناخته‌شده جریان محافظه‌کار و از مخالفان سرسخت جمهوری اسلامی ایران بود و زمستان گذشته در جمع مخالفان حکومت ایران در آلمان حاضر شده و سخنرانی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77589" target="_blank">📅 00:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WU5LHIOkEZzfeNXvmSUApdtjWA7A3tXyoBmvLxxfmepMiRdcyvfjQvR5swcz6AljwyCRtw590XDc0LAh7GsZx_-wJHq3au7MTI0wVIK_vpl_be29TCEnibbMSzUReMc3GrZml73VlMVVs-I2DN1EJBGuTqWO0zhwI0ebMrobhbc46qLHyDQvuEzsRC4UU8vk1cnV3baNxStnANg1kQ8dT_1Mnzzrn2DymdI-Fx3H_B1ERi9dSkzen7fzZKUsUHG1naCy8CEO5kfHrJua9qyfkE4Hgz3Z3RxV2i0BAFR4hTaLduvPeKjU_6PoJeR2eKzKJLLifr7pcJXPcphajffznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
این حکم با اتهام «محاربه از طریق مشارکت در تخریب اموال عمومی، تبلیغ علیه نظام و اجتماع و تبانی» صادر شده است.
به گفته منبع این گزارش، مهنام نواب صفوی دو وکیل داشته، اما وکلای او به پرونده دسترسی نداشتند و امکان دفاع از او برایشان فراهم نشده است.
همچنین دادگاه او به صورت غیرحضوری برگزار شده است.
مهنام نواب صفوی در جریان اعتراضات دی‌ماه در اصفهان بازداشت شد و اکنون در زندان دستگرد این شهر  است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77588" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77587">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y7WB7iqfFUwsDFbQY5knGQMjBsefS5Or1Z1P4FwExqkmEUvzhnxgaJos34L07bW76szOFA5CKCfPUIf71ulBNs_gczMcdqjcgFuAiYIAgh4MTCwFAWXwjUFh4ScSPQ0KUtJAbFLplOWt1_L1Evr7VLj4heTaiKlJVXO85ZLUExcFUHFw99pCb4NNyItvpnATHchqov3Op-nI5tIlYIPGKRnEqF-FjO_auYc9_1mrDnNUn_PcYFV3b0RKzsI-2emzOhqrfcmpzxxIZ8oTWYYbMSEbO4a72sv9l9DFHOX8m9R61LzISujigcv5WbpSZXQfjPNVeQrslWUnThN-PQK5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:  برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.  بار دیگر تأکید کردم که تمام اقدامات…</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77587" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=YyyG4GFiAOiUiUccn5-xP8_uTuXynIDhea1m7ra8as-lY1zL3teSKxjnbZsmwBJeOMLSfe1eOUYcWPoR3Plt8kgjUZiAM4HMJG2t-9av9ctAJlrJlv85hNTgUI9YyWePGxkKAJ-uo_fL6id3YnpC2U7yJ8Gd8mzihP_cK53VaOQ4ob6me267JxpDdO4RJa2-XN987dXfFKpWvWhCwz6riYaA747-hqVQjNCCZnUF1kYID32g3y0Zyb_Blv-4A07cy_uhRw_odfEYssmqY8J5jdewOnylmzVfKKVhimegsBtKQUiPFbMu5AD866NFTxmTKwDAQCENXkhrlSTSEBb3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=YyyG4GFiAOiUiUccn5-xP8_uTuXynIDhea1m7ra8as-lY1zL3teSKxjnbZsmwBJeOMLSfe1eOUYcWPoR3Plt8kgjUZiAM4HMJG2t-9av9ctAJlrJlv85hNTgUI9YyWePGxkKAJ-uo_fL6id3YnpC2U7yJ8Gd8mzihP_cK53VaOQ4ob6me267JxpDdO4RJa2-XN987dXfFKpWvWhCwz6riYaA747-hqVQjNCCZnUF1kYID32g3y0Zyb_Blv-4A07cy_uhRw_odfEYssmqY8J5jdewOnylmzVfKKVhimegsBtKQUiPFbMu5AD866NFTxmTKwDAQCENXkhrlSTSEBb3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، روز سه‌شنبه اعلام کرد تهران پیشنهاد عمان برای تقسیم برابر مسیرهای عبور و مرور در تنگه هرمز را نپذیرفته و در مقابل، طرحی موقت برای بازگشایی این آبراه به مسقط ارایه کرده است.
غریب‌آبادی در گفت‌وگو با تلویزیون حکومتی ایران گفت عمان پیشنهاد داده بود مسیر کشتیرانی به گونه‌ای طراحی شود که ۵۰ درصد آن در اختیار ایران و ۵۰ درصد دیگر در اختیار عمان باشد، اما جمهوری اسلامی این طرح را ناکافی دانسته است.
او گفت: «ما گفتیم این موضوع رفع‌کننده نگرانی‌های ایران نیست.»
به گفته معاون وزیر خارجه، تهران در مقابل، طرحی موقت پیشنهاد کرده که بر اساس آن تردد کشتی‌ها در یک مسیر از آب‌های سرزمینی ایران انجام شود و بخشی از مسیر رفت و برگشت نیز در آب‌های ایران قرار گیرد.
غریب‌آبادی همچنین تاکید کرد سیاست جمهوری اسلامی این است که تنگه هرمز «هیچ‌گاه به وضعیت پیش از جنگ بازنگردد» و هشدار داد هر ناو اروپایی که به گفته او به تنگه هرمز نزدیک شود، «هدف مشروع» جمهوری اسلامی خواهد بود.
او افزود عمان همچنین پیشنهاد کرده بود کشوری برای مین‌زدایی از بخش جنوبی تنگه هرمز اعزام شود، اما تهران با این درخواست نیز مخالفت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77586" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=H8tZlmWiqtB6xZjPjyMJbWsMyRyCBmmWvFmewZym80LNGFNGAvNoSAQRWFH6Zy7yXgkNvNDI0PDt-APdt1LJwPNVAvWVqf1eaVnqUPjeqKlsftjYQkTUVw-Cz2peGaDD_y3MqoM3sRVCMA9AIH0JMV5J2e7t7dKW-GV71MWPstSLwTCZQI8oYwdu0kYUKlUd3oGlPljENyqMScmIomx-soXLkx2VppxNnlUxiWOxr1d6vss8kl1H8Rg49FfmSdJS9J-rkMFWDvHf14BRB4zw73iGpomA-AJ3UmxHVpCSjcGV0tIaVc36nUSyCJJw4jmqbHcKVLJCanMWlWNTFLbkqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=H8tZlmWiqtB6xZjPjyMJbWsMyRyCBmmWvFmewZym80LNGFNGAvNoSAQRWFH6Zy7yXgkNvNDI0PDt-APdt1LJwPNVAvWVqf1eaVnqUPjeqKlsftjYQkTUVw-Cz2peGaDD_y3MqoM3sRVCMA9AIH0JMV5J2e7t7dKW-GV71MWPstSLwTCZQI8oYwdu0kYUKlUd3oGlPljENyqMScmIomx-soXLkx2VppxNnlUxiWOxr1d6vss8kl1H8Rg49FfmSdJS9J-rkMFWDvHf14BRB4zw73iGpomA-AJ3UmxHVpCSjcGV0tIaVc36nUSyCJJw4jmqbHcKVLJCanMWlWNTFLbkqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی که در حساب اینستاگرام خود منتشر کرد، دیدار روز سه‌شنبه ششم مرداد خود با دونالد ترامپ را «عالی» توصیف کرد.
او افزود: «این گفتگویی بر پایه مشارکت کامل، حمایت متقابل و درک هدف مشترک جهت اطمینان از دست نیافتن ایران به سلاح هسته‌ای و همچنین سایر اهداف بود. این یکی از بهترین گفتگوهایی بود که با رئیس‌جمهور ایالات متحده، دوستمان دونالد ترامپ، داشتم.»
نخست‌وزیر اسرائیل در حدود ۹۰ دقیقه در کاخ سفید با ترامپ به رایزنی پرداخت؛ دیداری که پشت درهای بسته و بدون حضور خبرنگاران برگزار شد. نتانیاهو تاکید کرد که «تمام تیم ارشد» ترامپ و همچنین «تیم ارشد ما» در این جلسه حضور داشتند و این دیدار «فرصتی برای تبادل نظر و هماهنگی ترتیبات مهم برای امنیت و آینده دولت اسرائیل» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77585" target="_blank">📅 22:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQG7LlFjr4EyqirdiRnpevmSzUwTxAAAXmxYAn-qH_aBRURgKZDZpghRXVCaDXx_iDISKO1f5X6ROimoQ5mxrnKks11w_zcHX4aUUSWJLM9vwZamhxFnEX2cx3wpz-oW5DJXLvbAGDgYeMkLQ7L3o6mOGuSZtCAz7sACIDRGgBUVzKA1sHNRlk3R1MYjlP-chh1kKIjzJ2x1mVD1_bu9BiT4Ojhk98Or838vP8VA8ihKjtf2HnA_3YKNvVCDZE_mdrgG6YKHMl9nRdMcjmcvKwPjOjThwTH4B3Wkz67k761sig9qZA16riA1K9-8YFGjhah8m1gyrc4Cyka6RlUbkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:
برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.
بار دیگر تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن شناورها یا افراد غیرنظامی را نداشته است.
این موضوع درباره اظهارات ایران در مورد تبعه این کشور که جان باخته و نیز یک شناور غیرنظامی که در حادثه‌ای اخیر هدف قرار گرفته است نیز صدق می‌کند. هدف ما مقابله با تجاوز روسیه است که ریشه اصلی همه این حوادث است؛ و این روسیه است که مسئولیت کامل همه تحریک‌ها و تلفات را بر عهده دارد.
بر ضرورت خودداری از هرگونه اقدام تنش‌زا و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین تأکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77584" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mYgsKzLYpDxwlRFMD2JFeWZPw2CbT5mVoypC0pT9tgwNPiBDH7JatTAleL4HN2cZ7WQw-qVa7ap6uB4fKx_eGwdh2WmCNoOLY8mlzto_cpkIN_Smko07ohLrvPIu5fooNIHZHdlSrRwW_lSWzatYFB94itgxQLqAoR765eDJyvTQn0lPTNtxZFqt4Ns6CMyWkZ3keRamQiCzvLYvmCWDPpMCsI6XFeFI9wAfijlb9PG2b1P58bV3pMvI4fk4mmZJFGM8Qd3t86LcVL0to6TbUVuSfJsPjno30-p4ZeP7rwbhmZNCSDLBcJ4RaCBUupM2fx38ubYsbhMtjELW64BZyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RIXecw86Yp7B7S1cjD87_UbkbCLzyFBoHqUZXtV0TBuzn8joyzN_m9C8Luazivr_mbS0Wlvku29pwY2VOaWvqmDPCO-RoKRdSvPIOFTfRxaVYA8cfHlwi4mRYaa8nIgD42npGUvXyhoptUBTX8TUu68SHYkANfY_MqbzUZxBn-mBHWBHhJ1tX4FgAKoONlZquwC0mPtI7OSz39zNXBRLZcej_0jgWzQ5lAFPmZyPzmEh3jsevq_DWxZvzWZmGmANRUz8OgCohCroCTKTa_UJVolcTIwfwKRrfMJ4M8tiOAvvTTIMj1alWKjCW0o7rquZUQJKACyFMOgM7opVXmkEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vl--gbMmPDcduno9yRva1Azt6ui3t3CtC83MCx5fUSpCTy6DfQVx9QcSxr7eShyg3fwGumWVFndLslnMAYDBT0Pzq44cdkQ-eAbzXBWwt99j7NCTr9C8-3I2PYvFcK4cXbusfFjD98vBZws8snUrDoLdb1Emh5PQoAEIAak8NA7rIimKbRJEtK40J9j22A3O0HY0qeZ3sKlMHIvFHGTrnzZf-8Xu94yND-htBxT4sjaaQerybFzhfWMLGIFy7RufvnK5-Cigcb5URco10xjy9LMqR50NTZJ2_61r9sOn2fTb1d5mgzur5C2sjgNnGj7glBcWHyFUe-g6cFgrpSELWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pDR9cMI26GYP-6lsR8w_9BvXBaIQIl6kWwYcy7TGDTNA2ftRXBxXMTX0AE_oV-PMPHdyQTgtMH4ololQkB71ZUC-evCQPaymYhXWeq3XG6VFJEvHnxgkxAHBpyKJz4NIA3lx3EZ_njexN4mydNkrN48joWhfFbKkDHhRX9LaZUPhRx9LCQVIt7MyTjVm60wcZCE3mt7hTnUOltnR0XPfwwxe5Pg29uJsBNc_ZGQ1GZm4HSwL8EPzpWwq4aE8q52bm_o4eunbXu1hWrHbXKOlP-UdkD0VSfwyqKzfxW-Qp_YUr52vdwS-_MAQ5iFWCFkHlZUSAlsVlr-9Qh-Js5B9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r522VmyobzEjGfJrndOyQXQKhnx-BKwDrv0YYK3gWw5uOOWD8MZf4R9yZjuG9W0deohXndW6vt-8Bh5mLPI5uFr0ifjgopLW7tn-H2DNjsMIZjYJuDvF8l7yIW_gp07-vXwtcqcjuM_6EYoAlCOh7Mw8vHJgOkKFtF145Yex-_bH78eBAtnpAGZOGaRuPPOyYQVWH5jliGMP_nila-lji6VnprqhtvfuU-4WwC2cW8UwiK39NLczwR5nKJi6PHpGl4i-Wk0xW7LW8u5CejzGW8wzo2FhS6DGCvfQV5-_EhhND7KaQaOU_nN6tH6D6t42wjXDmkR5lT-9OH_kUOiLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XdAO9x69GDWyymaiml6p-7fzNs9kXR-DwvxyWNItCYE0zVQ0TivbiAJRuHNBGBJ1NVuQJMHBVLGbzLClOKLv8FaY8CEfoS3CYqKFRW8_pbdmfArut4rkF4MPnCuZ_7MdTSI4Q1NnAzAuAq_k0KGkM-Tku7SEDad1cj9zD0YGGbt1kOU4xf6yyqgd7y7X7QYFNGqW5EM1GG838Nsa0QXgFszIiWgFasQ6ne_ANRAIRz5Xggv73n3ryLkLEnqZOG6rV7m_zOaeEZI6xlvs_GUpLPaEwY8KXtPdap8wt-ZbGgx4h10GKgHWRVetUcL5uIg9fIu7VRz1bUKZEBzWvh3caQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uo2zupN6LzcKNqI9GxRQw2IW1FHtFW9ndp8S3VLxGFsVmPGQ1NLX79Wy3sQTffwJadq8pnHAgOpX6I00Qg9k1lWRgsnMGG-7YbqRgISY6nBASzrKAxKVtDN69paiHKeD_gwbAuGPiGbv6eJzu18eq_0gt1A6nbJ3WaEOg3W1YQSljGfyVcFsXorpemxGJH83NO5i-UtS-iAClKaJxMFOxvzQGQu8taJk-D93PogIFm1TPjnKE-vyVMjQL2ITtWIb_uhtSf1KAH6cfwfd5HCyRBBlJ8hvJu47vbBHV59IDFsHaPI-mMlX54kQ_l_NhofTyX9agova7AH8R1Qo4Dyj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EcYFJH0mgR-8bdW2NfQB0-DfJPOLo2gx9ImTKv9UStDq_zm7MDqYKFZ5JN2rmojj5Kwd4wXI_gxa-ispfIJbS_qnLnzLArfbYwRp3T7edtTiE_i66_QgLPjD7YD942nyEULpY0ASY4AUaGeQoh37WZKTmYbnmA-yuOlrb0Y2_-uwWRyBkbgV3gbVhdmLzF7EHxf8pakncrRgLF0LOq47LGXTnCGYw2DgQ7SHS-hTTQqGtSKvQ5XTOQrTx4UxX5sPdT7wfQedj60czizWTPItybNKFZvJWvEIBUEPLyOVahpamqD3H2vrdgYAOWEYEhGdFxifYS3HSwfqfGE3lygZaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل روز سه‌شنبه ششم مردادماه برای هفتمین بار با دونالد ترامپ در آمریکا دیدار کرد.
این دیدار در کاخ سفید و پشت درهای بسته انجام شد.
دقایقی پیش از نتانیاهو نیز، ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، مهمان ترامپ بود.کارولین لویت، سخنگوی کاخ سفید هر دو دیدار را «مثبت و سازنده» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77576" target="_blank">📅 20:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fNFI4uH6fBKBxGbyuyl2Wz5ZR4lPrcmXn9Epqm4HLcqkyLPi_JU0Hj31_3gKwx8LRRHcNO0_jWTmr_zbV8wKNgMhynSgWRhmA0Xfvg3SAIfyRoABZ29l4h7gM7HvmVVCCQs846WMi0R2cXaq31m9J35ErZ8Ew2ALkWWc8HUmOfFCr-4VPlDMrBw__kTxFMUff0gMM9ES-0LYK-mEtbpEas0xViaHXMfLvP8p5zefv-rVFtY1p20_9vA_caXKVDStYwYg6on8yC0Tlc1_z4V6mx-1XTjZ6ZXcUuKZ_zq5gaKGmNAw2alR4HRnOAkqOh7LvXhkhQP4dZGeQoPz5H1GRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S_DLPqyjHX81rlqKPuSsthOMjAvX8LSnAkM3DeCCMC35nKFj-hRCv8oE_gvHWjsceZPVxvAZQdqL9XGqRpePKzdrxK6h2X9MDpL-1yrRNrYqUFkLI0yTJDDtQ0nm3yW1O16w-r2dySqUd7vnvIRnH5TYfG7DmeKyWpL97nS9Jjwb0lYgEy8DS9EGFiiFqxczK0sSgMGd20Pt8jIhLVRSMHHXd1Ha8O2zd42VzvV0Ym_m6j1RLr33mMT3gTgH3BECk2PR-LpKSMI_fBGtgqihNjDmkKOutTA-KUQDg3DZZYtpTrGYqp13esROijju-rL1yhc4cwyjXCkrn56yDKSBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cn4qZ1SxRkAZpuZENlEyMQd71-k6wSlO7ay4-6xVBSd6FHdpHB5OImf46ivxPkFt2S-QMJeGv-ePoK11pUeY2ylsXWPmM7QvWLpezr6naRil0Mv3H0PtYaOOJeATgXC6VSutLljk7Gg9GHy7hneEzPBQlzou4vEBmI1biSiV-ZBDih_aGk3NBc7aKbKXaEvZXH_0BO472QW7vaKifJWRXIGI2ElWAXgZl_SwH018EDMdc2wvP0BWRJ4qESYczzKriTHWu1d-zBjzCXJEnoeTMDz5LFv0v3Z5C4TxOJooYgfKnRQTpNgcfcheu6uXYS7iDiv_ff-kHLIheLnQGEZ6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s7pTSUQ4qu1bEuBLtM9D3_IXigZVlzf61EO70cI5X8oXvafwKmRLeM5kHKiH61nHWGEFs89VSG9PspTxXqeeobw6s3uEZIE4IZUlvyLNFGlQ2qUVsJ2yKbWCybWmDTl_oOnXPRikoD2495vJ9o9jpZqER5Sf5liglUoW2Se6oHZ63DFEGxr_Kr8miwCcdyqJ5LznS4Qh52_X_jm17NvXOuLNVYeIEH4gtBTBbtu2GlsOSQG-9sWel09EUD5G1lmfl5yItoLwxd26AYUqUscOKvEY2VTfwra5F6VQXpHH4kdeqitXMGZj4AQo0Tm5rrJ1HV32efDE8VDtw_kXGaBxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BQHuhHHHPYZcHDb5TU1kS5v42P5S8KRsAmx5OKF6UQtGdvtzopxTySyAcp1L21KyeJdMj_VSqhstJDoBYqNl-H7YQ2tpWfgcmbaTUmiW9Yt5JsoW0su-hqZPWMZKmmSdE0EeX2MxJF0hexLIG14jLqeiWjITatM22__MrwXKwDNwNuxKSuqQzo76s1kaxKTLa-foX2tkIYWjzyFZ5gXmsX0Xk9pJNYgEkInBQ-7W-Lbu6pdnFP3i_dflXt5Uw2OSGY9RAMalKkojqlz8zx1HQt7lNsiHy8dSDjKQADh862m_KhrPSkLRYzpsi_yhKEhBgASC9ewKA7S2hmY0t-zEAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی در ۲۵ تیر با شرح: ترمینال مسافربری فرودگاه بوشهر و باقی‌مانده‌های یک هواپیما
سخنگوی دولت، امروز: فرودگاه بوشهر دیگر قابل استفاده نیست و باید از نو ساخته شود. از یک هواپیما که تازه خریده بودیم فقط دم آن باقی مانده است.
Vahid
سخنگوی دولت جمهوری اسلامی می‌گوید فرودگاه بوشهر در حملات اخیر آمریکا کاملا تخریب شده و دیگر قابل استفاده نیست و «حتما باید از اول ساخته شود.»
فاطمه مهاجرانی روز سه‌شنبه، ۶ مرداد، در نشست خبری هفتگی‌اش با خبرنگاران گفت در بازدید از فرودگاه بوشهر «بقایای هواپیمای نوی به تازگی خریداری شده» را دیده که بر اثر اصابت مستقیم موشک، جز بخش کوچکی از دُم آن، تمام بدنه آن نابود شده بود.
این نخستین بار است که یک مقام حکومت ایران از تخریب کامل فرودگاه بوشهر بر اثر حملات به ایران خبر می‌دهد.
@
VahidHeadline
یک توییت به همراه اسکرین‌شات‌هایی درباره اطلاعات یک ایرباس ۳۱۹:
عمر این هواپیما 24 سال بوده! سال 2019 هم خریداری شده بوده.
iranimerican
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77571" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMLqGH-CUOQO970cXubb3AmtdFbX8O--h_F-4UpvLPBDIWSYh5KU1CyvwH3H5IKdhQKn4d9c4OZerUaKCzMNWPqyVK9knR4xfeqKeUSK0DcCO8WVgE0xke6E5DfiTAWdYz99xv9P4VF45telWzXfF_806MXrJ4BWHZLIC1Hfhh2mmwo_KydZKpxJFapuIzk4okyvl9TmjAGehAhlIKIGPxnzBTWP6vg9UP-v0u0vE5rPluW5RkEUGYmhO6iZFkkbzTTv0uW2scOPExquTufmmrBGj0Fg-ApMNuVjD1WWGnWeoBtKs_DWqQYX9tUjr8l5G3PEz66gP9VfYfe5sc1YlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های نزدیک به حکومت و شماری از مقام‌های جمهوری اسلامی در روزهای اخیر بار دیگر بر اجرای قانون حجاب اجباری و برخورد با زنانی که از این قانون تبعیت نمی‌کنند، تأکید کرده‌اند. هم‌زمان روزنامه «همشهری» با انتشار گزارشی، از قوه قضاییه و نیروی انتظامی خواست با آنچه «هنجارشکنی» و «بدپوششی» خوانده، برخورد کنند.
روزنامه همشهری، وابسته به شهرداری تهران، در گزارشی با اشاره به انتشار ویدیوهایی از حضور زنان بدون حجاب اجباری در سواحل کیش، مراکز تفریحی، مراکز خرید و برخی رویدادهای فرهنگی، این موارد را نشانه «حیازدایی فرهنگی» توصیف کرد و مدعی شد که ممکن است بخشی از این رویدادها در قالب «پروژه‌ای سازمان‌یافته» برای تضعیف ارزش‌های اسلامی انجام شود.
این روزنامه با اشاره به ویدیوهای منتشرشده از ساحل سیمرغ کیش، برگزاری نمایش‌های مد، جشن‌های مختلط، کنسرت‌ها و تغییر الگوی پوشش در اماکن عمومی، خواستار ورود دادستانی و نیروی انتظامی و برخورد با افرادی شد که از نگاه این رسانه، قوانین مربوط به حجاب اجباری را نقض می‌کنند.
هم‌زمان، شماری از نمایندگان مجلس نیز بار دیگر خواستار اجرای قانون موسوم به «حمایت از خانواده از طریق ترویج فرهنگ عفاف و حجاب» شدند. محمدتقی نقدعلی، نماینده خمینی‌شهر، مدعی شد «برهنگی و بی‌حجابی مانند خوره به جان جامعه افتاده» و از مسئولان خواست اجرای این قانون را در اولویت قرار دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77570" target="_blank">📅 17:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WYwlv3ZpZeejw8Mog-LLr-4k0QPKmP2R9Q8TCQvlLQ0UFHD1F7LwrBK9unIgUVzdxyrEp2KL6Ko0PQCUSKkR84OrDi866O76SwVsnpXzsfhRpCQGu8JdzVztKW4pDZJvorR6pSEcx9JO3Q39YwN6CPpUK--HYgZZSxsEjub__V5dIjHvAr9e0vCfM2xcLw6CbvDhOlRuw0XR3wiiWoRRvxz8CGomtbbeIN1uDYAa-yjo22JhCCO4fzIFVhQJLmY7-SN3DN39vVn8JnrXE4rUCrqOp6tcUlb4TrsAAcIjtlZSDcQwtyqICfrblX6W3VvaWUJX87FvifcJB0LeTqcYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=oQXzJvBmWecwOIEUkge8r0QbyRrkaGqmYH8G5qf6CTBNVPbXfyzQalTRBcG7Cc94gJT1o2Os57eESsSNaAbr39VG_wWLHKPT7j-tY6Cy08juRVVX0DKleaf1v0xYmz_L3IYfEHXyYKm5BzCVHXD7YFrDBKz4j8FYAq-pN_4t36VSDpeEhE2L9KwUgewAp3noyNCysoGIMvUx6DsHl2Ueapsul2m2xtNAvfdQpwanOtZSHsODJ9crWNwABf79FYbGqKgJV3rT9nJcGDxjxEP8nlZH00bYkSuljnjg1b0gDX7uAFN2ETDBINeu9_P4vfK1ClWvfO3Bu0REkrpppXAPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=oQXzJvBmWecwOIEUkge8r0QbyRrkaGqmYH8G5qf6CTBNVPbXfyzQalTRBcG7Cc94gJT1o2Os57eESsSNaAbr39VG_wWLHKPT7j-tY6Cy08juRVVX0DKleaf1v0xYmz_L3IYfEHXyYKm5BzCVHXD7YFrDBKz4j8FYAq-pN_4t36VSDpeEhE2L9KwUgewAp3noyNCysoGIMvUx6DsHl2Ueapsul2m2xtNAvfdQpwanOtZSHsODJ9crWNwABf79FYbGqKgJV3rT9nJcGDxjxEP8nlZH00bYkSuljnjg1b0gDX7uAFN2ETDBINeu9_P4vfK1ClWvfO3Bu0REkrpppXAPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران تن به توافق ندهد، کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق را می‌زنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، روز سه‌شنبه گفت که گفت‌وگوهای خوبی با ایران در جریان است، اما بار دیگر تهدید کرد که اگر تهران با آمریکا به توافق نرسد، تأسیسات زیرزمینی در کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق ایران را هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز اعلام کرد که در صورت امکان ترجیح می‌دهد پل‌ها و نیروگاه‌های برق ایران را هدف قرار ندهد.
ترامپ توضیح داد: «من می‌توانم همه نیروگاه‌های برق آنها را ظرف یک روز از کار بیندازم. تمام نیروگاه‌های برق آنها از بین خواهند رفت. فکر می‌کنم حدود ۹۱ میلیون نفر باید بدون برق و بدون پل زندگی کنند. و این یک توازن بسیار، بسیار ظریف است.»
او تصریح کرد: «آنها می‌دانند که اگر توافق نکنند، من این کار را انجام خواهم داد.»
دونالد ترامپ هشدار داد: «می‌توانم بگویم ظرف دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همگی نابود خواهند شد و نیروگاه‌های برق هم ظرف یک روز.»
او افزود: «اگر بتوانم از انجام این کار اجتناب کنم، ترجیح می‌دهم از آن اجتناب کنم.»
رئیس‌جمهور آمریکا همچنین با اشاره به تفاهم‌نامه امضا شده بین واشینگتن و تهران در خرداد ماه که در درگیری‌های تیرماه به آستانه فروپاشی رسید، گفت: «ما دیگر نمی‌توانیم اجازه دهیم آنها توافق‌ها را نقض کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77568" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SHn4PQEZdeZPaRuHGBEw2rZUapIGp6obUsbKdlJjj7R0EzwILAnCNWhYN5lLq7GT2aBYSwZou-R8udHrqBX8Xbdn13gSweJS58RyUOFX6beqD8rY8VHaJTrOWcPM7WWytQyJwzvfdfYNfTiE991-BLTWxJo3o0FKamarauyueucIVSS8XPWFzDzb5LJwwDlUDB_FZPgKDE_WBhnxrqgdjBjCd7jQxXjrCSfp6ccE7CmcYYUZDutS15AljaLp0HkxSkdO6viCS1Acx8JzT7vxqnhCbET44DsxF7Xl8RlR4ZHmaeOJq24V4RPNVJCaVlHQhY0-Pfa9T1bcf1ZERop9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v-clVCFiDgkkAZz0pIV5m4IQCD8AdGy3Y94Htzo1lYyk15Y0GJ8CKF--szor2X8TSVuit2Lv6BU479bLwEiAPvmbQ00OE0GcPZDhlVHyhbSehW5tVraP5e9Lgekn6BUmOPDKWKfBqb3H9CYD_VoYLIoXNGnOTjbf3_5SyN14BMnaBulE_YoJlASwQNl_0Hr4JGA2b6mOp_Q2FXlem5WsZjgI3KAENvNX8VvAy4_ZkumLze6umUNUVulTHL9uUzuXJPttQx8zS_V_WjxivzVBrqMeHZaYARyi6-U8pHMLDD0JoOxZUoXhk3N7l469d9uh2RH1oUNnRnD5QQpItCtd8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل روز سه‌شنبه ششم مردادماه در مصاحبه‌ای با کانال ۱۴ تلویزیون این کشور گفت که در هفته‌های اخیر، جت‌های جنگنده و بمب‌افکن‌های نیروی هوایی ایالات متحده از پایگاه‌های هوایی اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
کاتز گفت: «ایرانی‌ها می‌دانند» که این جت‌ها از اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
به گزارش اورشلیم‌ پست، کاتز در این مصاحبه گفت: «امپراتوری مغروری که اسرائیل را به نابودی تهدید می‌کرد، فروپاشیده است.»
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در کنفرانس امنیتی کانال ۱۴ با اشاره به دیدار دونالد ترامپ، رییس‌جمهوری آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واشینگتن گفت آمریکا در موضوع ایران منافعی دارد که فراتر از منافع اسرائیل است و افزود: «بسیار مایلیم به ایران حمله کنیم، اما آمریکا موافق نیست.»
کاتز با اشاره به آنچه دستاوردهای اسرائیل در برابر جمهوری اسلامی خواند، گفت: «امپراتوری متکبری که اسرائیل را به نابودی تهدید می‌کرد، در هم شکسته است.» او تهدید کرد: «اگر به سوی اسرائیل شلیک شود، با تمام قدرت حمله خواهیم کرد. ما آماده‌ایم با توان خودمان به ایران ضربه بزنیم.»
وزیر دفاع اسرائیل در پاسخ به پرسشی درباره واکنش احتمالی اسرائیل به پهپادی که روز سه‌شنبه از عراق پرتاب و در مرز اردن رهگیری شد، گفت: «ما می‌دانیم چگونه امور را مدیریت کنیم؛ آماده‌ایم.»
کاتز همچنین گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، «درک می‌کند که اسرائیل از مناطق حائل در لبنان، غزه و سوریه عقب‌نشینی نخواهد کرد». او افزود: «هفته گذشته از غزه بازدید کردم؛ هنوز تونل‌های بسیار بزرگی در آنجا وجود دارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77566" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhaMQJzOCiU-2swu3qQJ-OaR-SXc_SJQ4KlLK7_i56hdLW2Y2LKrkH6HJbd76He_a_4GO_1cJ4HzODGkxe_wToY840kqUTTtoP5ZGzBJiYMaCejvJ7Xg2bvHpFTNtY_by1P9d-lynG3XXCTc5xiUcMNm6yL7X7S2pgRaSOFUaxx3_yHw81xEq8gfNmMtO21Q90wJPBCAb0noFwTed3EQbwSO11g3ziagOQYJtdtk8kBQ4csdIUcK6Pdv5YcZ21H-YO_NsQDa6vh7e0ijKPlrS6XUkqq3cKqjfDsYgI4aDJCDuvzeL4kfuxoK3w_04goCIvcmD53AKkDqOnhUiiJ8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه می‌گوید که حمله اوکراین به کشتی ایرانی در دریای خزر «باید به‌عنوان حمله به خود ایران» تلقی شود.
دیمیتری پسکوف، سخنگوی کرملین، هشدار داد که این حمله نشان می‌دهد که از بین بردن «تهدید ناشی از کی‌یف» تا چه اندازه اهمیت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77565" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
