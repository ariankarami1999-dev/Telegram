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
<img src="https://cdn1.telesco.pe/file/OUAfTRxVh1RofLvpH4zhzALCrVAclCDBO4qwYXx4YVUAkgMVTuxaOoBUeA7N_zgjWtjJEDP7FljYgjd3hxN0YwhMA_Ebh7sR2mKGK9kSb31N6bSZpIKTa8PcA7qn7bNrTuxdQdwKStLG6-gXRCZu3F8NfkDjLC39hjzAEYMVQl9RbQBG4-UzsPmi9Kt_dNP2ks0D5fBOlLNIEx3VDIeperq2P7V5AuQmypbnqkQxv7m1jVJLhBdgPqlIZfEpuxQaA2vqbOxfaCtPhf5PLX096V01arWfyeVFInjG4KhzTGLeU8sG-5MIuUU8Qt0W5ZIFDHijRDKvs0Ro0xpn6PE5EQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 08:37:57</div>
<hr>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TyAxl67jqxbYb30qKGFIQ8XGr5UjyQG5otqBdvxI7PMAepOA0XrEXTojVGmnvJpF1QqTxnPdjoJBYVVAHVURbtwDcUkFD_b8zVyZPqPTEPWntTmrfl05roAbTjrzKvar2Nw1kCER8kIJTzpXW8ubpF0MwlE9yzyHuCl7pHS5y2JjtBwqQx0iVIFaOwBWBlcXei8eL1R2aNYjEAGoyl49RHLJ07CkMYHySi2X_aPW7LPFHAV-SxOEsV19XK7Cd7Yjexgqr37XlFJi_lgFdj6uwaLzzVxy3yVjIoAPP_-bUiaVlf59thwI6v1hEV77iCnn-iyUfnSx8r65YSlaBx5MPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ علیه بعضی از رسانه‌ها
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">باز هم صدای غیرمعمول پرواز یک هواپیما خیلی‌ها رو در تهران از خواب بیدار کرد.
پیام‌های دریافتی:
صدای هواپیما سعادت آباد
سلام، تهران صدای توافق میاد فکر کنم
صدای جنگنده یا هواپیما ۰۴:۰۹ غرب تهران
دوباره همین الان دقیقا ساعت ۴:۱۰ صدای شدید تر جنگنده غرب تهران
سلام تهران صدای جنگنده میاد چخبره؟؟!
مطمئن نیستم ولی غرب تهران فکر کنم صدای هواپیما یا جنگنده اومد
تهران سمت  سعادت اباد صدای جنگنده میاد
خیلی پایین بود صداش
همین الان تهران صدای کلی جنگنده اومد ک رد شدن
خیلی بلند بودن
صدای جنگنده غرب تهران
ساعت۴:۱۰صبح صدای جنگنده سمت شمال غرب میاد
تهران جنت اباد 4 09 صدا جنگنده اومد
4 و ده دقیقه صبح بالا سر شهرک نفت پونک جنگنده اومد آنتن قطع شد و وصل شد
همین الان غرب تهران حدود ۲ دقیقه صدای جنگنده اومد
دقیقن ده ثانیه پیش ساعت ۴:۱۰ ‌صبح یک‌هواپیمای از همونایی که موقع جنگ از بالا سر خونمون رد می شد
تهران حدود ساعت ۴ یه هواپیما مسافربری رد شد صداشم زیاد بود
هیچ وقت از این مسیر رد نمیشه!
توی فلایت رادارم نیست
شهرک‌ غرب ۴:۱۰
صدای جنگنده او‌مد
سلام وحید جان . ساعت حدودا ۴ و ۵ تا ۴ و ۱۰ دقیقه صبح شمال غرب تهران صدای مهیب جنگنده اومد. کاملا مشخص بود تو ارتفاع پایین داره پرواز میکنه . البته نه پدافند عمل کرد نه بعدش انفجاری شد. احتمالا برای نیرو هوایی ایران بوده
امروز سه شنبه دوازده خرداد ساعت ۴و۱۳دقیقه صبح صدای هواپیمای باری یا مسافری اومد چون چراغهای کابین و چشمک زن روشن بودن، مسیرش رو دنبال کردم مهرآباد ننشست تا جنوب تهران ادامه مسیر داد، صداش عین هواپیمایی بود که دیروز دوشنبه ساعت ۹و۱۵دقیقه صبح ، بسیار طولانی و ممتد حرکت می کرد به سمت  شمال ،چون از  کوه های البرز رد شد
صدای جنگنده نبود غرب تهران
یه هواپیمای خیلی بزرگ بود که اونقد پایین پرواز میکرد احساس کردم الانه که بخوره به ساختمون روبرویی خیلی بزرگ بود هواپیماش و خیلی پایین
پنجره باز بود دم پنجره خوابیده بودم صداش شبیه جنگنده نبود مابین جنگنده و پهپاد بود
همچین قیرقاژ داد رفتم رو هوا
سمت پونک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن موقت خطوط تلفن همراه در بعضی از شهرهای استان‌های فارس، بوشهر و هرمزگان و...
از حدد ساعت ۲
▪️
شیراز کلا قطع شده انگار
نه میشه زنگ زد نه میشه کاری کرد
▪️
کل تلفن های همراه توی شیراز قطع شده
تمام اینترنت ها قطع شده
مشخص نیست چرا اینجوری شده
نه ایرانسل نه همراه اول نه رایتل آنتن نداره
▪️
وحید از حدود ساعت ۲:۱۰ تا همین الان انتن گوشی ها و اینترنت خانگی و هر چیز مخابراتی توی شیراز پرید
همین الان [۲:۳۰] همراه اول وصل شد با سرعت کم. ایرانسل وصل نیست
▪️
شیراز خط گوشی بیشتر از ۲۰ دقیقه رفت
از ساعتای ۲:۱۰ دقیقه تا ۲:۳۰
ایرانسل هنوز نیومده
آپدیت:
ایرانسل هم وصل شد
ولی همگی 3G  هستن
سلام وحید جان بندرخمیر هم از ساعت 2 همه چیز قطع شده الان به زور وصل شدم بهتون اطلاع بدم
اصفهان هم دقایقی خط همه رفت
تو شیراز یک دفعه همه انتن ها پرید. حتی نت مودم خونه مون هم کاملا قطع شد
الان بعد از حدود نیم ساعت دوباره انتن ها اومد
وحید فکر کردم فقط واسه من اینطوریه نت خونگی مبینت ما هم قطع شده خوزستان سربندر
از شهرستان های فارس نیم ساعت همه انتن ها رفت و اینترنت مخابرات هم کار نمیکرد الان اینترنت مخابرات اومد و انتن همراه اول هم با سرعت کم اومد ایرانسل قطعه
نت و انتن و... کامل توی بندر ماهشهر پریده
اهواز هم همینطور
سلام بندرگناوه چند دقیقه کلا همه چی قطع نه زنگ نه حتی شبکه داخلی همه چی بسته شد
بندر ساعت ۲ بامداد تقریبا آنتن ها رفت
و بعد برگشت خط 3g شده اما اینترنت کار نمیکنه
الان فقط اینترنت فیبر وصل شده
دقیقا راس ساعت ۲ کل دیتا سنتر شیراز قطع شد
تلفن همراه کاملا بدون آنتن
تقریبا ۳۰ دقیقه شد که وصل شد
همین الان حدود نیم ساعت در نورآباد ممسنی همه چی پریددد نت و آنتن و خط و همه چی
😐
شیراز از ساعت 2 تا 2:30 انتن همه اپراتور ها قطع شد
بندرعباس هم همینطور، قطع شد وحید جان تا الان
اینترنت و انتن های تلفن همراه تو قشم کلا قطع شد یهو
تقریبا ۱۰ دقیقه قطع شد
هم انتن هم اینترنت همراه
بوشهر اینترنت مخابرات و ایرانسل هی ده دقیقه ده دقیقه قطع میشه
خیلیاهم کلا قطع شدن از اشناهام
شیراز بعد از نیم ساعت وصل شد
کل سرویس های ایرانسل و همراه اول و شاتل حتی اینترنت مخابرات قطع بود
خط  ایرانسل هم برگشت
وحید سلام و خسته نباشی، اینترنت و خطا برای ده دقیقه کامل قطع شدن هم بوشهر هم بندرعباس، بوشهر وصل شده و نت همراه ضعیفه منتهی بندرعباس اینترنت ایرانسل قطع شده
وحید اصلا همه‌ی استان فارس همین شد
من فسا هستم منم قطع شدم
دقیقا از ۲:۰۲ تا ۲:۳۶ قطع شدم
وحید بوشهر هم کلا قطع شد الان وصل شده و خیلی ضعیفه یه نیم ساعتی کلا آنتن نبود
میناب هم یه ۲۰ ۲۵ دقیقه ای کلا انتن نبود
بندرعباس: ایرانسل کلا قطعه، همراه هم قطع و وصله
سلام اقا وحید داخل بندر دیلم استان بوشهر ما از ساعت ۱:۴۵ دقیقه هیچی انتن نداشتیم چه ایرانسل چه همراه الان درست شد تازه نت رو h هست
با تمام سیم‌کارت‌ها ما الان وصل شدیم
مرودشتم کامل قطع شده بود همه چی الان وصل شد
سلام وجید جان
ما برازجان هستیم
برای ما هم نت ایرانسل، همراه اول و رایتل و مخابرات کلا قطع شد
الان که برگشتن 3G هستن
سلام از جنوب استان فارس پیام میدم اینترنت خانگی و همراه و همچنین آنتن از ساعت ۲ تا حدود ۳۰ دقیقه کاملا قطع بود
بوانات برا یه نیم ساعتی انتن پرید
سلام توی یزد هم آنتن همراه اول کلا قطع شد، فکر کردم باگ گوشی خودمه، اما الان که گزارشات رو دیدم ظاهرا چیز دیگه ای بوده
درود وقت بخیر شیراز حدود ۲:۱۰ دقیقه کل خط ها انتن و اینترنتشون پرید و بعد از حدود نیم ساعت با سرعت بسیار کمی وصل شد
تشکر وحید جان
سلام وحید خط بستک و کل غرب استان هرمزگان بعد ۲۰ دقیقه وصل شد
سلام وحید جان بندرعباس الان 45 دقیقس که همه چی قطعه آنتن ایرانسل اومده ولی روشن نمیشه همه چی پریده فقط فیبر نوری وصله فعلا
سلام وحید جان :استان بوشهر :کنگان از ساعت ۲:۲۳نت ایرانسل و مخابرات پریده و هنوز وصل نشده خدا میدونه چیکار میکنن.
شهرستان
قیر و کارزین
هم ایرانسل هم همراه وصل شد اما مودم مخابرات از ساعت ۲ قطع
درود. از لاهیجان پیام میدم. اینجا هم امروز اینترنت مخابرات دو بار برای چند دقیقه رفت و بعدش با سرعت خیلی کمی وصل شد.
اصفهان هم حدود ساعت دو انتن قطع شد‌ ولی چند دقیقه بعد برگشت
سلام داخل اهواز کل آنتن ها قطع شد و سریعا به حالت قبل برگشت
مجدد همه چیز پرید توی بندر ماهشهر باز الان وصل شد
وسط بازی بودم پرید بیرون انتن رفت فکر کردم خودم اینجوری ام  از ساعت دو
الان وصل شدم دیدم بچه ها هم نیستن هیچ کدوم نوراباد ممسنی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1Pp8tzggLzdFCVKBO2IhMV26EbaM75MmI92cc0fCaK79vogbwoiWZSKq5E3tS9g71C6SphYjrzDuSujtZq0tqv6kWce7KI4hOKwc8sc9nqhvVBRqTleT29E0Nmf7Ot81b8yInnmnTdUSca8I4lMlOIljVBvE0G0eTcXEobUTBeCqwmST5ANFI8BhyYNSxboagr_vD-i2bIAHMhyMZEkQLi47Jzhrc8DB_bhM6UC7_566Ae5Bhz5JQoHkj0xpW1bjj5n_qzWry2BkoIcPWJFHwm8u2SiU8VmaNYFe5mOeCGOAz9Lh4y-1tIdge9NIfExza4ofzRP-533Thw73TPRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HajLH_mSt4xhJHB3kZsNC7GreOPmidpWX3mafpQcgzFgXKjV8E7-gKy1hCFfQkdXJFJBAyygrgZgFZbXtEtX1uldUshACFJnXPpykiwKBu_bNgj7FMKD6WFIkqe1mpfSb6BVT5xQvDOC8VKW1623E3pDeg4SgAX04vosRkQO2sOY_TYh0EfPyuGwXhw8KH2-TygFTsPoZJF_-phUflapzGi_C7e3WPrRATQWRoC_bMXyqiHqjLzh4A16s_hPUDcVr0Rwr4ON5aHOqXr188vcqiQ8uVOx6aG1cLdBIlo84XVNTkwIPwY9DRt7x1aFo6ze1aSvYWXAFLx1UOsxHMs7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
امروز با بی‌بی نتانیاهو گفت‌وگویی داشتم و از او خواستم وارد یک حمله بزرگ به بیروتِ لبنان نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آن‌ها پذیرفتند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب، اسرائیل هم پذیرفت که تیراندازی به آن‌ها را متوقف کند.
ببینیم این وضعیت چقدر دوام می‌آورد — امیدوارم تا ابد ادامه داشته باشد!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
خیلی شبیه به
پست چند ساعت پیش
ش به نظر می‌رسه. به نظر می‌رسه همون رو بازنویسی کرده ولی قبلی رو حذف نکرده.
نظر چت‌ جی‌پی‌تی:
در اصلِ پیام، تفاوت محتواییِ بنیادی ندارد:
هر دو می‌گویند ترامپ با نتانیاهو صحبت کرده، نیروهای اسرائیلی از رفتن به بیروت منصرف شده‌اند، و از طریق نمایندگان/واسطه‌ها با حزب‌الله هم درباره توقف درگیری صحبت شده است. گزارش‌های خبری هم نسخه اول را با همین مضمون منتشر کرده‌اند.
اما متن دوم از چند جهت مهم بازنویسی و تنظیم‌شده‌تر است:
۱. ترامپ نقش خودش را پررنگ‌تر کرده
در متن اول می‌گوید:
تماس بسیار سازنده‌ای با نتانیاهو داشتم و نیروها به بیروت نمی‌روند...
اما در متن دوم می‌گوید:
از نتانیاهو خواستم وارد یک یورش بزرگ به بیروت نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
یعنی متن دوم بیشتر این برداشت را القا می‌کند که ترامپ شخصا جلوی حمله بزرگ به بیروت را گرفته و نتانیاهو به درخواست او عمل کرده است.
۲. عبارت «حمله/یورش بزرگ به بیروت» اضافه شده
در متن اول فقط می‌گوید:
نیروها به بیروت نمی‌روند.
در متن دوم می‌گوید:
وارد یک major raid of Beirut, Lebanon نشود.
این مهم است، چون متن دوم وضعیت را جدی‌تر و عملیاتی‌تر تصویر می‌کند: نه فقط «نرفتن نیروها»، بلکه جلوگیری از یک عملیات بزرگ در بیروت.
۳. تماس با حزب‌الله با احتیاط بیشتری بیان شده
متن اول می‌گوید:
I had a very good call with Hezbollah
یعنی ظاهرا «تماس خیلی خوبی با حزب‌الله داشتم».
اما متن دوم می‌گوید:
I also had a conversation with Representatives of the Leaders of Hezbollah
یعنی «با نمایندگان رهبران حزب‌الله صحبت کردم».
این تغییر احتمالا برای این است که مستقیم نگویند ترامپ با خود حزب‌الله «تماس خیلی خوب» داشته؛ متن دوم آن را رسمی‌تر و غیرمستقیم‌تر می‌کند.
۴. تعهد حزب‌الله محدودتر و دقیق‌تر بیان شده
در متن اول:
all shooting will stop — Israel will not attack them, and they will not attack Israel
یعنی «همه تیراندازی‌ها متوقف می‌شود؛ اسرائیل به آنها حمله نمی‌کند و آنها به اسرائیل حمله نمی‌کنند.»
در متن دوم:
they agreed to stop shooting at Israel, and its soldiers. Likewise, Israel agreed to stop shooting at them.
اینجا حزب‌الله مشخصا متعهد می‌شود به اسرائیل و سربازانش شلیک نکند و اسرائیل هم به آنها شلیک نکند.
تفاوت ظریف این است که متن اول از «attack» استفاده می‌کند که گسترده‌تر است؛ متن دوم بیشتر روی «shooting» تمرکز دارد که ممکن است محدودتر از «حمله» باشد.
۵. متن دوم تردید و شکنندگی توافق را اضافه می‌کند
متن اول قاطعانه تمام می‌شود. اما متن دوم اضافه می‌کند:
Let’s see how long that lasts — Hopefully it will be for ETERNITY!
یعنی: «ببینیم چقدر دوام می‌آورد؛ امیدوارم برای همیشه باشد.»
این جمله نشان می‌دهد ترامپ خودش هم دوام توافق را قطعی نمی‌داند و بیشتر حالت آرزویی/نمایشی به آن می‌دهد.
جمع‌بندی کوتاه
متن اول بیشتر شبیه اعلام رسمی یک توافق فوری است.
متن دوم بیشتر شبیه بازنویسی سیاسی‌تر و شخصی‌تر همان پیام است؛ در آن ترامپ نقش خودش را برجسته‌تر کرده، تماس با حزب‌الله را غیرمستقیم‌تر توصیف کرده، عبارت «یورش بزرگ به بیروت» را اضافه کرده، و در پایان هم درباره دوام توافق تردید نشان داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tEXMPFngltyibxPjUxAXwPzWToqmxR7DMAHnIBXvN3QykkK2GJC6o4Usg-fUv4ZLJjvQPW87qiDICkW1eVyoxlOOeZIEpd_yw8P9VliFUM9HcuROh99fUvSkISGPPs9AJl1IeSp6d85MVWT-yJRcEuLjLf4E8cgyO7JE1JpFESZmWePYTQYmRjm2f3wiaBDBOVbDWUpWxIJGkep09atZ36gRvbUseJCvInGFAS1fyvSifBCjlyVyAEfIq8d85DNQ2gH4Gvm3j2uwj1Gm50BEgDSdY8mS5psV16o6uPbhsmkXmAqoa_qGGMJgSg5NevA5oDsEAow5ZTlGtVWwN7AgsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=ay8RV9EbJc_yASfLrXXeD8ZI7-Ta6bFrfiTkimZu7KwVOg8ct01MzRPUr9MluoOxyjPrT9Azm31SdNPtv0Vl94ZodVj5pJaIDwkEs2rKaQSOxKGJ0KGiepNqm4k7HLVxAIvbxGHYM6_BFCvwYIc7Ji6aiEhbr2YLWsxfEJNAsfl5N30Uns2tMejh0inqPPxrTlaRkxDcsPRXeVFLSddr3wT-315cfXphLRZUgtIkjfOkKVsDvllBczBVid5bDKtQxThFvSGudGF9Uv72LRdZc2rgcWWqMDhG4ogh3QKcVNsmc7StmzbgGELKBVQnlcDTvH62yBWDrXcFJvz1-JxVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=ay8RV9EbJc_yASfLrXXeD8ZI7-Ta6bFrfiTkimZu7KwVOg8ct01MzRPUr9MluoOxyjPrT9Azm31SdNPtv0Vl94ZodVj5pJaIDwkEs2rKaQSOxKGJ0KGiepNqm4k7HLVxAIvbxGHYM6_BFCvwYIc7Ji6aiEhbr2YLWsxfEJNAsfl5N30Uns2tMejh0inqPPxrTlaRkxDcsPRXeVFLSddr3wT-315cfXphLRZUgtIkjfOkKVsDvllBczBVid5bDKtQxThFvSGudGF9Uv72LRdZc2rgcWWqMDhG4ogh3QKcVNsmc7StmzbgGELKBVQnlcDTvH62yBWDrXcFJvz1-JxVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G2mTrds2QSkJZ0Ku4ELr-vFtqFQhCoVy5BvqENJXddduOWqwlRqs7FFHfcPl6uXyzLcXQJtpkvM3te9LIjRj1Rm3XvK5OJ1vQ2TITWPYuuZfK2rG22tyuG5DbSG8C6x90kdLD9lILOrbHUnu-dMTS6IP_wcMXYA9M4Ie5_un9wf5FBD7Bm7L3xiG9YroDT0NiqQ45eaJmOEZF403iDtwyW34KmoO4RRbkxb_zp_gvxOl3Y0VmWtsNyMlTQ89sNShAVUsZr71Lt083MZdrXWeo_648iy6o30YpLBFD44zGwjK0OentKKpjdw6sHKcom5wHhk5r-Ui60LXMfbcdNSi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام دونالد ترامپ مبنی بر موافقت بنیامین نتانیاهو با توقف گسیل نظامیان به بیروت، در شامگاه دوشنبه ۱۱ خرداد ماه، با واکنش منفی چند چهره شاخص سیاسی در اسرائیل مواجه شد.
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، با انتقاد از این تصمیم گفت: «زمان آن رسیده که به ترامپ نه بگوییم.»
همزمان نفتالی بنت، نخست‌وزیر پیشین اسرائیل، نیز در پیامی دولت این کشور را به ناتوانی در حفظ امنیت متهم کرد. او با اشاره به حوادث امنیتی در اورشلیم، بیت‌شمش، لبنان و غزه نوشت: «مکان‌ها متفاوت هستند، اما داستان یکی است؛ دولتی که کنترل بر حاکمیت اسرائیل را از دست داده است.»
بنت همچنین گفت: «هرج‌ومرج در همه‌جا دیده می‌شود و ما امنیت را به شهروندان اسرائیل بازخواهیم گرداند.»
یائیر لاپید، رهبر مخالفان دولت اسرائیل، نیز با انتقاد از نتانیاهو، تصمیم او را «اعلام تبدیل اسرائیل به یک دولت تحت‌الحمایه کامل» توصیف کرد.
@
VahidOOnLine
دفتر نخست‌وزیر اسرائیل در بیانیه‌ای به نقل از نتانیاهو اعلام کرد: «امشب با رئیس‌جمهوری ترامپ صحبت کردم و به او گفتم اگر حزب‌الله حمله به شهرها و شهروندان ما را متوقف نکند، اسرائیل اهداف تروریستی را در بیروت هدف قرار خواهد داد.»
نتانیاهو افزود: «موضع ما در این زمینه تغییری نکرده است.»
او همچنین تاکید کرد ارتش اسرائیل به عملیات خود در جنوب لبنان طبق برنامه ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IcIglenDwcmbJDUY3gQwB7FlFQaC2lX4wZJUw9PqhqcRhEraBYp2CaoG3VDxdmXZPnWo5ai3nvUl19Z8zpnOXLKv2_yjYQXdIJGsW9zd-jK7nW--GwnTtqE0R9cUdpQws9fZBv8SBMM6T1GqTscGzGB0SCP76lVpE7TY2SVMo_R03PY4x2lPwFJvkAO2498LgSNNHG_ZImjytrtbMVzjNgSMnEvALWbN64iUbtgW4KwNJ5iRW7M4Q4OFZOU6AFUxrx3aIrzU9ix3TfzpTn30GW9hziLWw57L7SYpUPtiTDFOWapc1creKSBCHo5jWR_3-NV33dDE-kYbIRUfOtBeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی: ادامه حملات به لبنان و غزه، باب‌المندب را به تنگه هرمز تبدیل خواهد کرد
اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، شامگاه دوشنبه ۱۱ خرداد ماه در پیامی که رسانه‌های دولتی ایران منتشر کرده‌اند، نوشت جنگ اسرائیل در لبنان و غزه «در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعال‌سازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگه باب‌المندب با تنگه هرمز رقم خواهد زد.»
فرمانده نیروی قدس سپاه همچنین هشدار داد که ادامه عملیات اسرائیل در جنوب لبنان و غزه، این کشور را با واکنش‌های گسترده‌تری از سوی حزب‌الله و گروه‌های فلسطینی روبه‌رو خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/75857" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pm_T3RkDnx7E4YRqb908VWdaoW1FkdVLzdIDVgr3ld_CAfQ-PQbVVb1OHCfgpaCfZmSRp2vaHQ0dq6R4DV9HhyMdHy03qhyc13EYj2F7PlDbdrgTSEpUiuIno0ea9xc0TkeGUKUa7dKMwt6ZqIvKFG-hBiWkGuhcFfiihrDn0eAtr9RKH7KYhls9KeY-vimJfcInDvFOE8yqOh-gSsPXpdctoKk0qaDuBEjCPhv4uIinTzqcv-hBCTrghu1c8hd-dTAkzc3Qmz9ElnzcweLwG9JgNmZLOcttN7SGQlrUhvCkMNLZyo6RvSmxwXsX94rFzodG9-T-m2ghf052PTCgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با جمهوری اسلامی ایران با سرعتی بالا ادامه دارد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
این دفعه گفت "جمهوری اسلامی ایران"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75856" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oKmve2_YbYSkzy6OsvnxpLltZa_vbKqAuZYYlb_95Ze7TXjJV0hJdjaAI6Sizv-dCQfQk1zKiT9NTivR2_brWNLlYgsU3SVEmoh4H_fDzfRFpTI9LIlJM60OiDlixxfn8VJsYz6uhMO8mLtgWUDYPYFoddj8Tu5xoMdyW__q_togCPRomLbQYfccFdA6ndHAWTghACowSCp8vHQqY6u9SQmfVtjT2hxodw1DH9OoH64tDYvRVzaEp0CGVzDKOV5gYvNEltTZ1dQPopzXh_ErPrWq0qJVDV5Hhb0dZ15lXwWLE_OsXmDBN4LSn2TClIVqRptpsUGpOULNl_BUFPR_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و حزب‌الله پذیرفتند حمله‌ها متوقف شود
ترجمه ماشین:
من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل، بی‌بی نتانیاهو، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد؛ و هر نیرویی هم که در مسیر بوده، همین حالا بازگردانده شده است.
همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها پذیرفتند که همه تیراندازی‌ها متوقف شود — اینکه اسرائیل به آن‌ها حمله نکند و آن‌ها هم به اسرائیل حمله نکنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75855" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nf642AAlRRvcgPIjs-ssCUOzclEGe40pEMju3IB9o1nooC9P-qpc_Su2tRJ8ydowrQpBzkxcP-cbij-PlA0OY-eR4JsR2y7TjdYOi_Lu5GhaLOW_L9NEyJ7-PmO2PSR5X2IznpP8v8rZ5tVFBh3Kw9ysJklOssweeRqtUzYcfYlkF04CRQWz6sZGIrWC_T1D-JW-WL5MLT0FC5vr7lBj0BTQJmVP8cU0x4D-MtEN1ra_iAsgg4XM_aog4k27i5yqMmg5oJdrsgCbR2_DarLKt-m7pZXltTnZeS_1Vl_HdpHsqAHy-eprm6zcCNiTbGzxY-mD4XdgUJeOHp3XQEk2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره را حفظ می‌کنیم
توییت‌های خبرنگار NBC، ترجمه ماشین:
تازه: رئیس‌جمهور ترامپ به من گفت که درباره گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا، چیزی از ایران نشنیده است؛ اما اگر درست باشد، اشکالی ندارد:
«فکر می‌کنم اگر حقیقت را بخواهید، زیادی حرف زده‌ایم. به نظرم سکوت کردن خیلی خوب خواهد بود، و این می‌تواند برای مدتی طولانی باشد.»
او ادامه داد: «این به آن معنا نیست که قرار است برویم و همه‌جا آنجا بمب بریزیم. فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم. محاصره یک تکه فولاد است.»
آیا می‌تواند آن‌ها را آن‌قدر منتظر بگذارد تا کوتاه بیایند؟
«فکر می‌کنم تا هر وقت که بخواهند می‌توانم صبر کنم. آن‌ها دارند ثروت هنگفتی از دست می‌دهند...»
همچنین وقتی از نویسنده کتاب «هنر معامله» درباره گزارش‌های تعلیق مذاکرات پرسیدم به نظر می‌رسید با اکراه نوعی احترام برای مذاکره‌کنندگان ایرانی قائل است:
«این حرف مناسبی است، چون آن‌ها مذاکره‌کنندگان بهتری هستند تا جنگجو.»
GarrettHaake
الان هم:
ترامپ و نتانیاهو دارند تلفنی صحبت میکنند.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75854" target="_blank">📅 20:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dV5pFpD_4F-bt_S3wb7-R8rV_wCjh6C35tcckDTsjxjKcCYBRZAOhkDZx7hMBuI6CSLGCKFaqNJc-Md6Y9TfFt2_6L3ipbIkwz4SJ-CIY-Z_Jli1IOnDjDpouXXuph3e1jONrM9LeuoGZ0bYBEwZMJbLdWqcAvL5g3OEUyrzWWDLdhc7r-uPKKfPwSQndB5CPbYPavQZE2p1g-Nvealj1VkHaYh6GLHyRNrQCNyWecVNj6nc0-zLwbEVPWNgN4k8JRelM3AD7vBRZbbX6_LWzcHACIUxTp0waotvrQsJM7LXaMjq_VzN_28zeWa-yh4WYsCVxlzu3nUSfOQnP5mPSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با صدور هشدار تخلیه از سوی ارتش اسراییل برای ساکنان حومه جنوبی بیروت، فرمانده قرارگاه مرکزی خاتم‌الانبیا به ساکنان مناطق شمالی اسراییل هشدار داد که در صورت عملی شدن تهدیدهای اسراییل علیه لبنان، برای جلوگیری از آسیب، این مناطق را ترک کنند.
علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، اعلام کرد بنیامین نتانیاهو «در ادامه شرارت‌های خود در منطقه»، ضاحیه و بیروت را به بمباران تهدید کرده و برای ساکنان این مناطق هشدار تخلیه صادر کرده است.
او افزود: «با توجه به نقض مکرر آتش‌بس توسط اسراییل، در صورت عملی شدن این تهدید، به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75853" target="_blank">📅 19:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=exs_9dFfsjPvSSd5TOk0xtL14crLqCp69XfWDMTc8Xu1mo-_8oYBZrI34eZsVlbMAhkaJFe_Uz45hjEY8u8_YcX-lJOTVunDEJ7qnQajBch5rP76158Ni4op5xobJL3sATc3S1XB2v0GUoVO9qeLMeR-bWU43x3zt4_Vl7mMgBKWG9VvEzkRNMntEITRsLrkzteBBnldWxJT5CdjQ0CX_Olh0Qh60Od8PaVAO6MUrPOnelANbWwW0T0q6MxzfUG_4QwiZBwZM6csBErSjk7oCMQGMQFo7zeBVqUxG9-n4Z0tPQmMWPtdzoAAcOdXyk9HivR9PpxVDDR3qj5HrVIUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=exs_9dFfsjPvSSd5TOk0xtL14crLqCp69XfWDMTc8Xu1mo-_8oYBZrI34eZsVlbMAhkaJFe_Uz45hjEY8u8_YcX-lJOTVunDEJ7qnQajBch5rP76158Ni4op5xobJL3sATc3S1XB2v0GUoVO9qeLMeR-bWU43x3zt4_Vl7mMgBKWG9VvEzkRNMntEITRsLrkzteBBnldWxJT5CdjQ0CX_Olh0Qh60Od8PaVAO6MUrPOnelANbWwW0T0q6MxzfUG_4QwiZBwZM6csBErSjk7oCMQGMQFo7zeBVqUxG9-n4Z0tPQmMWPtdzoAAcOdXyk9HivR9PpxVDDR3qj5HrVIUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«حمید سلیمیان» در حال نواختن تنبک
#حمید_سلیمیان
، متأهل و پدر یک پسر چهارماهه شامگاه ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در زرین‌شهر اصفهان با شلیک مستقیم گلوله جنگی جان خود را از دست داد.
حمید سلیمیان راننده یکی از شرکت‌های فولاد بود و به گفته نزدیکانش به موسیقی علاقه فراوانی داشت او  تنبک و سنتور می‌نواخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75852" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kD1E7iPofak2U7jzOEnE2lMkjWrfyzCZgfl9gJkrkGv2DZGgqMWUZv9MKCDrMzQG5cfzjlXSVgvOj-mgY23zedlgoG1E34u0XNuO1H22azCcVlb6jn1iE5gUa8dnD0FTRWDJcggSoQa3T1FjuJqRDJ_zUmYtXq5exk159W1Sa8G7FmS8OEbEhUeINprCG_y80Sld34PEof1T3mY810PDNQr7d_t_-saPSQngqUEhtxoZMjskRngGxbqJVBZweBbHZnvI3CX0EI_Zfg2NjIWRhWIDkvp_BoQiHEAeoQgoElOiyOBJCiJwEkx8Vv_40b_IpCMonYwbMHyVRmHW77KcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HXQzihwPkPfCjjh_fQwL8DAoUFYGbSUqZruPxsIb1mHXLrV01MF1G2l8nJJAi_xECBgJiIN5coZQhflSYOZMUXg-i37Ctz_UFETyY_OP5mfAdwMuwS_RC6pqF5W9xT5EokU55NRUg9DpUIrLMNnyDSk7z3CWreIQAFfCUlhjzIbaCorL5YZXYCxopJffq3uU8Ol0J-eSRv5X5gRURLtZLDqLea2zeqiM5t1za6S5u2hYzM-0P-pukIp_WO6OlE3IzDsGsW-qgk8hAepOy1B7x8aWajsI7v52OWYP6SgsthG6HoA8-_OjTpUFhA4dtddh8kFY78gV8IciU3HvRVnvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ovXZrDjjRKVMEjOL6kwWkoW0mBbUB-LHCdwt7l2lPmTHi9vZ7Jomu6FGzeUAe2pP-_z_0Frp0OtrGy_qEHTV-xh7K2P3EQFNkd40qE3f0Rmn-Wve00YMVmKqchh4W_G1jsafMXbUBKbTu5ur_rM1pcqqVJFdXG7uc7afueoQ_UlPL9eGa3S8uwGYBUjU1Z50jf7dc_sm__fK7L4h-xAVu-I0BvREEfqmCIKw6mdo1zzwItLLkjFjm7rax2LPGdVD-NBhYmiJVNnAHAeAPisw-ddxBNNW2IqDt5iPMBkLnryVUDCxQzFKeYCH5R1pZJ_6zPuyBS5hKNG_uV2X_Sq-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OLi0y9hZWINuP3OJA3VTvDYKV2HyPMr31CLHYTJILCFb-o1Qehih-P65NwMaLcA6bqmcNfZptkZCZlYkf9_shaHQdpIbZ6SmtuXdkIUIPk0NGlIG8t8H8isg4QBtq0E-V-mBlmAvp6TuLhUqlHCA5P3q10ju-GFRcP3Fwk_OZ3PZHWntSN1k5vg_7bkYkniGDqwtVW6LQixEw_OFTqjqpGIr9TdddR3bgKhLjdQyv6JT8opXQHi36Cl8HN7rhuDQAl_rSz2ElfIA6Ru0pRHtk-wT1_Bsew8b9EjFJqiUf_8ZOw7CWWpFlJ1l5kXpKaycu3iUqYHAJkjU6OLiZrCU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c541l7ghncqnpzawGhdQhwxjCSctCfvCQNGuZ2VYvg4MEisSdr1b-CDbq6e8KMIyaohYNV0D8KUCmvpfN0XpMNQ-nabjcOX2Ipi8Olk7gr7UiUQJ0ko9ysPusT31DmMiUlhzR16zA2dwaN7c8RztI2Qtwt-8N8azntrHVjLUF239s2mYZqc73nvDY2IrKFcRw6WpTmLz0rCyO8Kz67jGscJIJNJhU3Qe5ymBLyD6P34RK1q4Uj-3wj13Hsv-XqLHf3GMdjkdzGrlmDBaFPEG2wHSB53Cgs7zzpox_edTN6feVP6Bla6m5bkfYI51wONi8TrXhVlN9P9bLR3A97Gd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vHz5QGKoRwGXvAQJDWlL8XyvbaIYO3-96BrFEAoU_SYr8-oFDdmH2C5lcLRoBiUAUBXJy_Ybs0VO-ZHbasIWyYI5eBID3O4P1eWDlsPouPJT8rEOmXLMqH4MZ5KiGt8ujBYmvbUIXOGC-x9JNCpFaPQxpMqELwkQ80bp72q5wsVZfa7o4pg8l-RqDCMLvZaAS_HcPFEGUaZcnAIJAix7veIcVJF8yKXeHbPQGJrAnC2eGX48ZWPepSGN-ndAuNviU6I01XJ1x4_OtX92Tj71sxhlFc2O8DND77P9np6h7QhjcwF-VBmrRDMoeWa-iAlfHtr_NCKg9tE4y595b0CZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L8UpNrogDVH2o52iLc0tcqIXgN6PjEx9XwBZK2CLDsZHbZac_OVC5B_aUsKOfP-4ho4LghhbAerDHX-MO3Pxq7qEKsOgy6WpxRaOhwD-BkVKxvA_ruST8iEDpraCxorMdZRo6uW_5iHgPSoME8UEp1Xp7Vm7xDhUqJsbmNUO50aSGDEW66s2-VkGwNTqUNj5hG7Wxqm96bTBw8YaJjOSE_ZMd2Y4j4kDHETZIKr4cqZHtWTYiVHpl7m1aCglFN-XK5uOB42VMpXDrxDdfGzc6yGFVnp5I3ODeM1cCE-GzIaTggZMw5j7rCWtJ1JLDfAgrR92wcTtvwkBuWIUUCAIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v6W6TdiBCF6enOMr1uQBDmi4PiUl6VRmd69Tlz9GPY7xfQvpJJljah29c_VC5l0CHDEQaeLKT3ESYGxzyIPST6b1W4AYzUj-xk9GFjB_5aNcA-AY_hPSFPU3MmLMyCwtqCwpQkEQdyla5M3xOOCZ_ht_wTDh1O8znujbQ-DoRaVmakbUbHFI9km9d6W6IPev8029XNdhSNCJmF_77fOistliIlPIGx1qyxti7PkpD7zhYeAcNBAIYt9BJfXp3zUU8UdnLYmi022kxkZXzfIWx_Szkl1F2emaDB_MwwAlEzsYVE5NRekTHVO2U7Hs-zxGy4bBHnUEqLfQHU2QYx4OGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K86J9lT6h9wsMFEmxR5lNGil25d1rTgMkcHibNgRO5yW8ibk7r-vY1r-vlyd-8_7FmovBE6G205j5kMR216H76vtIVfDHVBYkOJFpmALL0y8BiHG_VQml0yuH7-YU0Eng3iPVvoc4ZXb53kewoxbIVk-UcaAj3OFb_wPBNbMKRjdvITLT7D6khOOVMWo8Qwl5MWjWVcCmhdzys_yGblEOzrSmYQlwuP592SlB7SQ2v0ca3Ir_lnNe-Gs5tPQ7ONyX00bjQCm1soVhZtusrHNfMoulV4lL7k3WvjYbCYAejhKs2L3pCSNkM2oOjnsz6lZ6VXrN6D9u2Mp6Mw-DaE5CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با تشدید حملات نظامی اسراییل به لبنان، مقام‌های جمهوری اسلامی بار دیگر تاکید کردند که هرگونه آتش‌بس میان ایران و آمریکا باید شامل همه جبهه‌های درگیری، به‌ویژه لبنان، باشد و هشدار دادند ادامه حملات به این کشور می‌تواند پیامدهایی در پی داشته باشد.
بنیامین نتانیاهو، نخست‌وزیر اسراییل، روز دوشنبه ۱۱ خرداد ۱۴۰۵، اعلام کرد که به ارتش این کشور دستور داده است اهداف متعلق به حزب‌الله در ضاحیه، حومه جنوبی بیروت، را هدف قرار دهد. او در یک پیام ویدیویی گفت: «هیچ وضعیتی وجود نخواهد داشت که حزب‌الله شهرها و شهروندان ما را هدف قرار دهد اما مقرهای تروریستی آن در ضاحیه بیروت از حمله مصون بماند.»
دفتر نخست‌وزیر اسراییل در بیانیه‌ای اعلام کرد نتانیاهو و یسراییل کاتس، وزیر دفاع این کشور، در پی آنچه «نقض مکرر آتش‌بس از سوی حزب‌الله» و «حملات علیه شهرها و شهروندان اسراییل» خوانده شده، به ارتش دستور حمله به «اهداف تروریستی» در حومه جنوبی بیروت را داده‌اند.
نتانیاهو همچنین گفت عملیات زمینی ارتش اسراییل در لبنان در حال گسترش است. اسراییل در جنوب لبنان منطقه‌ای امنیتی ایجاد کرده و می‌گوید هدف از آن جلوگیری از حملات حزب‌الله به مناطق شمالی این کشور است.
در واکنش به این تحولات، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در شبکه ایکس نوشت: «آتش‌بس میان ایران و آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمام جبهه‌ها، از جمله لبنان، است.» او افزود نقض آتش‌بس در هر جبهه‌ای «به معنای نقض آتش‌بس در تمامی جبهه‌ها» خواهد بود.
عراقچی همچنین آمریکا و اسراییل را مسوول پیامدهای هرگونه نقض این آتش‌بس دانست. جمهوری اسلامی پیش از این نیز بارها اعلام کرده بود که آتش‌بس میان ایران و آمریکا باید سایر جبهه‌های درگیری، به‌ویژه لبنان، را نیز در بر بگیرد.
ابوالفضل شکارچی، سخنگوی نیروهای مسلح جمهوری اسلامی، نیز به اسراییل هشدار داد که «تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود.»
هم‌زمان، محمدباقر قالیباف، رییس مجلس شورای اسلامی و رییس هیات مذاکره‌کننده ایران با آمریکا، با اشاره به آنچه «محاصره دریایی و تشدید جنایات جنگی در لبنان» خواند، این اقدامات را «شواهد آشکار عدم پایبندی آمریکا به آتش‌بس» توصیف کرد.
قالیباف در پیامی به زبان انگلیسی در شبکه ایکس، بدون اشاره به جزییات بیشتر، نوشت: «هر انتخابی بهایی دارد و زمان پرداخت آن فرا می‌رسد. همه‌چیز در نهایت سر جای خود قرار خواهد گرفت.»
این اظهارات در حالی مطرح می‌شود که عملیات نظامی اسراییل علیه حزب‌الله، از گروه‌های مورد حمایت جمهوری اسلامی در منطقه، شدت گرفته است. با وجود تاکید مکرر تهران بر ضرورت گنجاندن لبنان در هر توافق آتش‌بس میان ایران و آمریکا، این مطالبه تاکنون محقق نشده است.
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، نیز روز دوشنبه در نشست خبری هفتگی خود گفت: «ما تاکید کردیم و کماکان تاکید داریم بر این نکته که آتش‌بس در لبنان بخش لاینفک هرگونه آتش‌بس و هرگونه توافق نهایی برای خاتمه جنگ است.»
او همچنین حملات اسراییل به لبنان را از عوامل ایجاد تاخیر در روند دیپلماتیک برای پایان دادن به جنگ میان ایران و آمریکا دانست و بار دیگر بر ضرورت برقراری آتش‌بس در لبنان به عنوان بخشی جدایی‌ناپذیر از هر توافق نهایی تاکید کرد.
@
VahidHeadline
تازه‌تر:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد که جمهوری اسلامی در واکنش به ادامه حملات اسراییل به لبنان و آنچه «نقض آتش‌بس در همه جبهه‌ها» خوانده شده، روند گفت‌وگوها و تبادل پیام با آمریکا از طریق میانجی‌ها را متوقف خواهد کرد.
تسنیم همچنین مدعی شده است که ایران و گروه‌های هم‌پیمان آن در «جبهه مقاومت» در حال بررسی اقداماتی از جمله انسداد تنگه هرمز و فعال‌سازی سایر جبهه‌ها از جمله تنگه باب‌المندب هستند. این گزارش می‌گوید این اقدامات با هدف واکنش به حملات اسراییل و حامیان آن در دستور کار قرار گرفته است.
@
VahidHeadline
ارتش اسرائیل در بیانیه‌ای به ساکنان منطقه ضاحیه در جنوب بیروت هشدار داد و از آن‌ها خواست برای حفظ جان خود این منطقه را تخلیه کنند.
در این بیانیه آمده است اگر حزب‌الله به شلیک راکت به سوی شهرها و شهرک‌های اسرائیل ادامه دهد، ارتش اسرائیل اهدافی را در ضاحیه جنوبی هدف قرار خواهد داد.
در ادامه تاکید شده است دولت اسرائیل با مردم لبنان در حال جنگ نیست، بلکه با سازمان تروریستی حزب‌الله می‌جنگد.
@
VahidOOnLine
در پی اعلام خبرگزاری تسنیم مبنی بر توقف «گفتگوها و تبادل متون از طریق میانجی» میان تهران و واشنگتن، بهای جهانی نفت بیش از ۵ درصد افزایش یافت و به بالاترین سطح خود در هفته‌های اخیر رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75843" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5H3TS9LQidKHFuDjLvBiWWusjOZUPmRekOx2Ak0-9jqZswqhgOBBnR9Gz4InnEUa-1t19sb0gLn3S1z3I2DiYozg7bPKnIUeBLC2v9kdSLB3RVjVM9fE-Qr57scU0rYXVywkXYvD6-2koLhdbmlQZVxA6sufvcZCompispn4Tpwwe6pfumapxWIQi0hvaNWvAg7HNlfJPnEg9bOUAd_daljJuCI7G60caTQd6f48E20Y-jvdlKe6T7DakZiaQ1Oemj26Z58NEGUHwyE-k8twOvGAFaWaMsC4ySLPPcPJbJT1PEoG1unmHgfhodBWuI40IFCrxGSvEkhfA6Lmk7avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از کشته شدن یک دانشجوی زن در دانشکده دندانپزشکی قزوین به ضرب گلوله خبر داده‌اند.
میزان، خبرگزاری قوه قضائیه، از قول دادستان قزوین نوشت: «بررسی‌های اولیه نشان می‌دهد این دو دانشجو که در آستانه فارغ‌التحصیلی قرار داشتند، در مرحله متارکه از یک رابطه عاطفی بوده و پیش از این نیز اختلافات خانوادگی شدیدی با یکدیگر داشتند. صبح امروز، مرد جوان با یک قبضه سلاح کلت جنگی وارد محوطه درمانگاه شده و چهار گلوله به ناحیه سینه دانشجوی دختر شلیک کرده است. شدت جراحات وارده به‌حدی بوده که متأسفانه وی در همان محل جان خود را از دست می‌دهد.
در اطلاعیه دانشگاه علوم پزشکی قزوین در این باره آمده است: «انگیزه این واقعه، مسایل شخصی و خانوادگی بوده و ارتباطی با فرآیندهای اداری یا محیط آموزشی دانشکده ندارد.»
به گفته حمیدرضا قافله باشی، رئیس دانشگاه علوم پزشکی قزوین، «این تیراندازی به دلیل خصومت‌ خانوادگی اتفاق افتاده و دو دانشجو که زن و شوهر بودند در اثر شلیک جان خود را از دست داده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75842" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام‌های دریافتی از تهران درباره صدای پرواز یک جنگنده یا هواپیمایی دیگر مربوط به جمهوری اسلامی:
سلام تهران صدای جنگنده اومد همین الان
غرب تهران وحشتناک صدا جنگنده میاد ۹:۱۵
صدای جنگنده داره میاد غرب تهرانم ساعت ۹.۱۴
سلام وحید همین الان تهران صدای جنگنده میومد نزدیک ۲ دقیقه
شمال شرق تهران صدای جنگنده
سلام تهران صدا جنگنده شدید
الان از بالا سر ما صدای جنگنده اومد
رد شد رفت
همین الان منطقه گیشا صدای جنگنده میاد
همین الان ساعت ۹:۱۵ دقیقه صدای جنگنده سمت غرب تهران اومد(فکر میکنم جنگنده ارتش بوده باشه)
سلام وحید از سمت لویزان تهران موشک بلند شد
وحید الان ساعت ۹:۱۵ صدا جت منطقه ۲ تهران
تهران-فرمانيه
ساعت 9;16 صداي جنگنده مياد
وحید تهران ساعت ۹:۱۷ صدا جت میاد زیاد
هروی
الو سلام تهران سمت شهرک غرب صدای نمیدونم هواپیما بود جنگنده بود چی بود خیلی نزدیک بود
الان ساعت ۹:۱۷ دقیقه در قیطریه صدای جنگنده اومد
شرق تهران صدای جنگنده شنیده شد الان
سلام تهران صدا جنگنده شدید
احتمالا جنگنده های خودشونه
ساعت۹:۱۷
سلام دوشنبه تهران ساعت ۹:۱۵ صدا جنگنده من شنیدم سمت هروی
صدای جنگنده تهران ۹:۱۷
صدای جنگنده منطقه ۳
خیلی پایین بود
تهران صدای جنگنده اومد
سلام ساعت ۹:۱۵ سمت دروس تهران صدای جنگنده اومد
صدای جنگنده شمال تهران ساعت ۹:۱۵ رقیقه
سلام ساعت ۰۹۱۵ دوشنبه صدای پرواز چند جنگنده شمال تهران
منطقه ۳ صدای جنگنده انقدر زیاد و وحشتناک بود که از خواب بیدار شدم
سلام  پاسدارانیم صدای جنگنده اومد چند دقیقه پیش
صدای جنگده نارمک
سلام وحید. صدایی که ۹:۱۵ اومد شبیه جنگنده بود ولی از پنجره نگاه کردم شبیه هواپیمای مسافربری بود فقط نمیدونم چرا از ارتفاع کم حرکت میکرد
سلام آقا وحید من خونم گیشاسصدای جنگنده نبود هواپیما بود من بالای خونه رفتم دیدم ولی هواپیما بزرگ بود ی مقدار دیگه باری بود یا سواری نمیدونم ولی از بالای گیشا رد شد
من از روستای اطراف شهریارهستم یه هواپیمای مسافربری بزرگ تو ارتفاع پایین از بالا سرمون رد شد به وضوح دیدمش صداش زیاد بود
سلام وقت بخیر نیاورانم صدای جنگنده اومد وحشتناک بود
وحید من شهرک محلاتیم
بین ۹:۱۵ تا ۹:۲۰ صدای جنگنده میومد
(با ارتفاع پایین)
سلام وحید جان صدای وحشتناک جنگنده ۳ ۴ دقیقه پیش خونرو لرزوند
-هواپیمای کارگو سپاه از تهران بلند شد
.
-صدای جنگنده برای این بود؟
-ممکنه برای اسکورتش بوده باشه
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/75841" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی از
#بندرعباس
درباره شنیده شدن صدای سه انفجار:
بندرعباس ساعت ۹:۰۷ سه تا انفجار
الان بندرعباس ساعت 9:7 دقیقه 3انفجار قوی
یک صداهایی شبیه برخورد جسم سنگین (بمب یا هرچی) به زمین داره میاد از دوردست.
بندرعباس ساعت ۹:۰۹ صبح دوشنبه
سه تا صدای  انفجار اومد بندرعباس
ساعت ۹ و هشت دقیقه
دوشنبه، ۱۱ خرداد ۹:۰۷ صبح. بندرعباس.
صدای ۳ تا انفجار از نزدیکی پایگاه هوایی شنیده شد.
آپدیت:
خبرگزاری تسنیم وابسته به سپاه مدعی شده که مربوط به مهمات خنثی نشده بوده. البته دو روز پیش‌تر از این هم اعلام کرده بودند که طی ۷۲ ساعت آینده قراره از این صداها شنیده بشه در بندرعباس.
پیام‌های دریافتی از
#اصفهان
درباره شنیده شدن دو صدای انفجار از دور:
پیام ساعت ۹:۱۷: اصفهان صدای انفجار میاد، دو بار پشت سر هم
اصفهان همین الان صدای انفجار اومد سمت ناحیه ۶
الان اصفهان یه صدایی مثل صدای انفجار اومد
سلام وحید، اصفهان ساعت ۹:۱۸ ۲تا صدا مثل انفجار و کمی لرزش حس کردم فاصلش خیلی دور بود، بین ساعت ۸ تا ۹ هم یک صدای مشابه اومد فکر کردم توهم زدم
اصفهان صدا انفجار نزدیکای جی شیر(مطمئن نیستم)
سلام. اصفهان حدود ساعت ۹:۱۵ صدای ۲ تا انفجار به فاصله چند ثانیه.
نمی دونم چیزی زدن یا دارند مهمات خنثی می کنند. البته تقریبا هر روز صبح یه صدا میاد که به خنثی سازی میخوره.
امروز ۲ تا پشت سر هم بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/75840" target="_blank">📅 09:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eHThNKPSSM5PED7rxCinK_CZtcczenPTC65vgf3kPV2DmGqbmL_Yl_52AivZmkqrXp5bP0nIhOOFsaYfsQ7zcHHaYOPKVzT3HWHmYoaCyonx4MLURBWAII1u9CJ7Ldom4z0FZe3jE2tN5uEZ2Tj5BE9v2BGvdhVqkQ24ebsx5kM87Kwt9561zbjlWtZfQ0TzXfHNHge4W9fwgBbc8Kbuz5079snRTt_bKhMkBDYD8X9v8_1GHpE6Vp4xVpUQnFeI6DcMp6ELH3f1R94KYMPuvZ7LKqlf9ZKgLBDG4D3F3ak9u56IjfU5s-kulzUggYdeJXr05_e5uKzx5DJpzA0aLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌های کودن و بعضی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند وقتی سیاسی‌کارها مدام و با شدتی بی‌سابقه غر می‌زنند که باید سریع‌تر حرکت کنم، یا کندتر، یا جنگ کنم، یا جنگ نکنم، یا هر چیز دیگری، کار درست و مذاکره برای من خیلی سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور است!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/75839" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیام‌های دریافتی:
امیدیه خوزستان صدای انفجار شنیده میشه
از امیدیه خوزستان پیام میدم
طرفای ساعت ۸:۱۳ دقیقه صدای ترکیدن اومد
ساعت ۸:۳۱ دوباره زدن
همین چند دقیقه پیش صدای انفجار واضح ای اومد
امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75838" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد [گیشا]»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» اعدام کرده است.
نام این دو معترض که بامداد دوشنبه یازدهم خرداد اعدام شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
میزان نوشته این دو «از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران [بودند] که اقدام به تخریب و آتش‌زدن مسجد، تخریب اموال عمومی، درگیری با مأموران حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند.»
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75836" target="_blank">📅 08:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XJlqwATPFMunB3kM4D5Z3F8FIFNR1mDnLNdLXBcX8r84IX0jZlzUXSY3XQ5NAM4pw7IPXLozMOeQ46wymi-cg8jIVxmRjh7OeBAMTUsXGzo7aTYtV8IKIQsw_AxkKo3S5uMIP8cKbq1qPV84R8jbJXWupcTgUxt2DWMAbKr18aizkvb0_OsXlQxeR3RsSQw0FFN_cGgvd2lApNs-hQLzRNJaDLs1GRpDiH3jfFsLDExHqqCSJ3deGEQdRbhGx4KnqT-D58HkAA1SOUnWeWh9iMek2MPIIxwXHJi7g2pCPyl5xAApnuNkhe8njyaYKML191kzICDarOZs7sLC9hqGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KoWkpDpbTvQ8-SmOMpJ8KiBsto1AJUFzloPFMu-5oSg-kNi1sYF6HYn1GM1NLP_1rskRit2vzDQfABcHWCCz7uVy_YEawXPeZO_rPV87ThYkrIoB30qZ_3xjEpzddFnemHCsVbKkF5H4oc6jyMVzQRy9plseAZKAb-rfwbLkQel7KODeFXowRpRvO12M1Y78Uea-uFpqFfpATYrtBfhobWm1DLHMxUnm4NI_MKPhavZWkkv-Bw2Vr4dell1dhgJd5ARHZtuDj3C3sEwrmftUST31L_ixxyI_wiCS0mf5SBvcpVw_V5yInCvNFETS7BhY2vMZBvqE5rnLRRP2fW3BXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه سپاه: ساعتی پیش آمریکا به دکل مخابراتی سیریک حمله کرده بود پاسخ دادیم
من اون موقع فقط از یک نفر دو پیام داشتم:
ساعت 4:00 چهار انفجار در شهرستان سیریک
پایگاه سپاه سرخور زدن
ساعت 4:26 دوباره یکی زد
هرمزگان شهرستان سیریک
و الان کسی تصویر دوم بالا رو فرستاد و نوشت:
"حدود ساعت چهار صبح، آمریکا با چند موشک به اینجا حمله کرد.
پایگاه  نیروی دریایی سپاه  شهرستان سیریک ، حوالی روستای گروک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75834" target="_blank">📅 07:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=M5YMXH6KyG0yq9bV5u1ZOVnPFMfjOQJvJJKGyp7N1AS9Y7PIDD_yoRyQXp5a4GqdY9-5q6ieIG6EsurJAOT1ccLr4BVie1_blaVGjZhIUVMsFEse-SqsESYJPciRYTDrowZvHPLUOk58QumXasKMLw85ZiFwhnUaUfEWXIXL6mGS8yMXGEWgrOEc-P3AYuEokwMAXo21wqyR8liXH2OxrPtKU8hybWnC7wFQC-VMie-C0Bycvrfhfkc83HAUJoStxa5PzBse1iVM9bQt-G8mYXK85j_lZvQQ8K-3IjcINL57o8PebKSIPoqdf61HHxk1F5dvU6CB0hwf64JJhlXGJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=M5YMXH6KyG0yq9bV5u1ZOVnPFMfjOQJvJJKGyp7N1AS9Y7PIDD_yoRyQXp5a4GqdY9-5q6ieIG6EsurJAOT1ccLr4BVie1_blaVGjZhIUVMsFEse-SqsESYJPciRYTDrowZvHPLUOk58QumXasKMLw85ZiFwhnUaUfEWXIXL6mGS8yMXGEWgrOEc-P3AYuEokwMAXo21wqyR8liXH2OxrPtKU8hybWnC7wFQC-VMie-C0Bycvrfhfkc83HAUJoStxa5PzBse1iVM9bQt-G8mYXK85j_lZvQQ8K-3IjcINL57o8PebKSIPoqdf61HHxk1F5dvU6CB0hwf64JJhlXGJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
ویدیوی دریافتی دیگر از همان موشک،
دوشنبه ۱۱ خرداد ساعت ۶:۳۰
Vahid
ستاد کل
ارتش کویت
دقایقی پیش اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
به گزارش خبرگزاری رویترز، جزییات بیشتری درباره این حمله پهپادی منتشر نشده است.
ارتش کویت در بیانیه خود تاکید کرد که صداهای احتمالی انفجار ناشی از رهگیری اهداف مهاجم از سوی سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75833" target="_blank">📅 07:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JEYxr_EwBVs5feuJOLnjWVX6kIWaqIQNCDgzu-RcGJ7PmGhQYdy4mn1EWQYr-fZTnZgwkgIYo6KZkKUznRUmde65h-erFSDoU2RyRSiaDcqPFyzYUV_gcMZpSLgmiKsbTz7EbsKAgTVO-0WN2ogkD3-FUb0OLOlYmi1BF1De7rgvGP4OVHPPK9MvGmrYa-GoIc1zTDNFrIR6N3mwTVT41JSk5l5qwfDKxhUm2ACxM4DqDoUFZs2SEpALHPdZVP-b06r_M1CZ1xPdMS71pa3bMGqMp1aeb7k7MAYtdU--EN6ZdgyxPoO6rTc7x8tTaFASfe3KILTwMocczYNKur886Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام درباره حملات شنبه و یکشنبه
(از جمله حمله ساعاتی پیش به سیریک هرمزگان که با توجه به
پستی پایین‌تر
گویا حدود ساعت ۴ صبح دوشنبه به وقت ایران انجام شده. در آمریکا هنوز یکشنبه است.)
ترجمه ماشین:
"آمریکا در واکنش به تجاوز ایران، از خود دفاع کرد و تهدیدها را از کار انداخت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، این آخر هفته حملات دفاعی علیه سایت‌های راداری ایران و مراکز فرماندهی و کنترل پهپادها در گروک ایران و جزیره قشم انجام داد.
این حملات حساب‌شده و عامدانه، روزهای شنبه و یکشنبه و در پاسخ به اقدامات تهاجمی ایران انجام شد؛ اقداماتی که شامل سرنگونی یک پهپاد MQ-1 آمریکا بود که بر فراز آب‌های بین‌المللی فعالیت می‌کرد. جنگنده‌های آمریکایی به‌سرعت واکنش نشان دادند و پدافند هوایی ایران، یک ایستگاه کنترل زمینی، و دو پهپاد تهاجمی یک‌طرفه را که تهدیدی آشکار برای کشتی‌های در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند، منهدم کردند.
هیچ‌یک از نیروهای نظامی آمریکا آسیب ندیدند. سنتکام در جریان آتش‌بس جاری، در واکنش به تجاوز بی‌دلیل ایران، به حفاظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75832" target="_blank">📅 06:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sygn0tRfKfR2R42XgO8xO-lJ6Sp5bzPASqUhBcW1xZJiumHww5JmIknW0RL_QQGXu1hmPCo5h9bWD9EQgmTK0YjoUNP-vCNkPOOPQnH6EiHDBt8IVudB19Vxnikqbilq33QrlgxKcdbyDJsUbUKNZOtOQJ2g0heBnKhQCUYaP0Cf0IPRvzCNuy96hhDmEElYHZjhiAThJBkVpe9CYDak4UC3b2QN6X_qerhsSkPvFRm61IWqd-uki5P9bnRECsj6xOtT3Lh3iHF95LN2m6Ap-bcf6KEv0vxYijEqdb2QF99IwJhzE6n3qkrmCqFiW6FBGmDpcsPbl0lhFmi4-zCBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gElVXqoXXHaNe4KDTm1NURe2LlGmP7APt8QQrniMgfSq_yrYO8H33DmUo5GZtJdtSYff3dLqTkNlJb6JSdjhrUKG3qPsL3AE6fGEdvMvyKaWxq8IcU2gqFjyHHJrgRQuAVY7VHh2kWAgy-T0MYhXcXAssDL0535yjQ4bjtVp7tLGHeKe6jnjCPqqtmSUwGg5TCXgfMiBbQDlqzyir0xiTDYL6jCUaIDLibRTz7r9F13u60zsWU74TghMotyunrbIdEqe8fSXVkeJc2n-zWPPwKU1FUutC4j3cY4jR4_wQMpS06ccs6osZASjvHJYapuENn75dZSgx2OaUobu11uMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cHol7ZrAKysg4wS2_3oWtpkZyFFgbaTeu_Tl5KJbp1ICoYc_Xed9FxqCYSPLf6OthiNez0xxyvdeTd0yI883CyBxt8GC_vohDsT0uCR0IgAJn02ORd_4ezGXGvCke0g83iahtcIfRVuS5lPIAhsQKGA5Ujgd0AF_leePFlYJ2HCjZ_tchnarJEsbkj6BAklmtJVeZMMHO05AJuucjKmcTsxr3EbA4RnlAhnn_slCtDOVgnBaSlxHzvS6OhglwPYYEkxbC7bdC1gSz1lR6Zk7F_jsskvVStE4kGO4lfdFZ8NyLy_mdVfJxjUirae4X6JjPUCiqstG8Q3fgyW_XiQXIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=GsluPWqECwXgibDdxI9lqaI0ArLqesqSh8-KUMrcx0r8JnV2H7Ndqrjw0SLKu8yOMwYjoIwKsB-i5WWBYr-ftA_VjkMlVuMfvG60gLs6Zqc0jejuvAPmuJvHoOzpKjFpkWwSXPPZxpOT3_n0jaUb5JwOils-qU1f8Jmds_dN9QFF7T0G6PMLrO2FnOfwk_DkFNYZvFn1tRHYqYuAnrpA_LVeBUXdmtWC6Uuht6mlzdjvnrfwAjEQ6_IxU8vGQcVRLvN3RCQDOkeX674PlEOLAgXPHrSuZO8JPH-Kzy1UaLX7QMCeNetDfZblxlbCI00c8MS2af1EeLVwc0Tl93zysA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=GsluPWqECwXgibDdxI9lqaI0ArLqesqSh8-KUMrcx0r8JnV2H7Ndqrjw0SLKu8yOMwYjoIwKsB-i5WWBYr-ftA_VjkMlVuMfvG60gLs6Zqc0jejuvAPmuJvHoOzpKjFpkWwSXPPZxpOT3_n0jaUb5JwOils-qU1f8Jmds_dN9QFF7T0G6PMLrO2FnOfwk_DkFNYZvFn1tRHYqYuAnrpA_LVeBUXdmtWC6Uuht6mlzdjvnrfwAjEQ6_IxU8vGQcVRLvN3RCQDOkeX674PlEOLAgXPHrSuZO8JPH-Kzy1UaLX7QMCeNetDfZblxlbCI00c8MS2af1EeLVwc0Tl93zysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
تصاویر دریافتی، دوشنبه ۱۱ خرداد ساعت ۶:۳۰ به وقت
#ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75828" target="_blank">📅 06:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNAN_97G8FnE1T26pr1n0dr4ojUiVR28SN1OjxcOOxSzhxLbjQ6WZVPOeWR7-RDLyg334hLsPrze6olWletzB4ouTL-yjJIBR2wXS-sskL-aFsDi_UoSlntiyaFHWtrJhmCmJTmzlaHfTA3vyftHgb-bcMxUcDnFWuSRSFHyxpHlPUkSpt2c3O59D4Snja-8PXB2XEe87Hx05WZdTH3sh18k7knIVldDnPYXs80dHyO2W7qW45Ogrm5EnviKSp3CDS6jPVsKeGEl77L5IVyrirnbOd1Kgg8VWGP8ieF972c75_uO4SxrntJxR-m0CAFgmIInw1timpK9Aj4uDdbL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به کویت
دوباره همز‌مان پیام‌هایی درباره شلیک موشک از امیدیه خوزستان و اعلام هشدار در کویت دریافت کردم.
دوشنبه ۱۱ خرداد
ساعت ۶ به وقت کویت که میشه ساعت ۶:۳۰ به وقت ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75827" target="_blank">📅 06:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1WT_jts1FV2r1LJ3iIBHUdcJeIce0j76rYkWWbzhXTy9E_Row2PvsPqUrr-1cEroWQ6g-kS1tuEa8ITjNcUbcWUK1sXVAN7b6UzvKzkDm_Bl4dAyd6I_u09SkFameQR--B4xsxKU9kvjeOc-XulQOl_Dy3-BQ-7kCIoXtZMu1Mi4nGGolDFOa-bwyHYoTHiyv0glX67hnTACGwAOSG4V5_o7l8Lcvt8U5gmj66DfPYjBwQkjfPkiTCOjFhGLuKcH77HOHuLpvtFVb9zyhDVWn-HsWG8AXY_Lzg5dxcuc_OPLtXIIxHXadrENhiSBorPWrD45MTsYu4-uq_znKewgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه اخبار جعلی سی‌ان‌ان امروز طبق معمول گفت که توافق هسته‌ای ایرانِ من درباره مسائل هسته‌ای صحبت نمی‌کند؛ در حالی که در واقع، بسیار روشن تصریح می‌کند که ایران سلاح هسته‌ای نخواهد داشت.
سپس با جزئیات بسیار محکم و مفصل، به جنبه‌های مختلف دیگر موضوع هسته‌ای می‌پردازد.
در واقع، بیشترِ این توافق درباره همین موضوع است.
سی‌ان‌ان و بسیاری دیگر در رسانه‌های اخبار جعلی، فاجعه‌ای با رتبه‌های پایین هستند.
حتی با مالکیت جدید هم بعید است اوضاعشان هرگز بهتر شود!!!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75826" target="_blank">📅 03:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cI8W6CKD_6J29Si0Kjx4AjwOpgfZc1F8fsF4yB9y1UvskNPU67moV_6sLAnj1MCdLNdA_FGRyO2tH_Aw5hdRI9j2QY1Vgr6QCUPaQy4BfLV-Zd0MCAQ0hHsGK7nyG4uckGkV3TRmQgxrvuQ4AMQW3Of_ZBXe0sXhm760JU5FxDaazYicSGIiTPdWzzyf51qgmFZvCMSRv5jAtn-5rgPG5cl10NZ1OVaVlPiB4r1FesbTJrL3o_LQ0USi4MafkxHOWc73fdASJxtOE_q8bf8byuudTstrSEobG-LxP1ApfaUVRHr0aQsrtO7D9cSi1fHb3acLMTvcDZGt9rjeA6xApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز هم به درخواست استعفای پزشکیان پرداخته:
FoxNews
چند مقام دولتی با تکذیب شایعه استعفای مسعود پزشکیان، آن را «خبر کذب با هدف ایجاد ناامیدی» خواندند.
فاطمه مهاجرانی، سخنگوی دولت، الیاس حضرتی و علی احمدنیا که از اعضای شورای اطلاع رسانی دولت مسعود پزشکیان هستند در پست‌های جداگانه به ادامه کار رئیس جمهوری و تلاش او برای «حل مسائل کشور» اشاره کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/75825" target="_blank">📅 00:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIYCiPGrrV0zY5D5lSAWdD0KT96OtDPHp0XDR7loQtbXRDtVJ7VQl1lZSANAeLKUDTCCgiKzx2RKKmaVYKnBxjMYwa3k-Cg-WapsaM7ll1Je3WxZQAuSflS1Ijh8F4ZwNEu1U6R23E0F4ByK-bUZH6LDXpg_V2DLlwR3dUczR_lk8hSjb1S8B0GlKjTuuo6NccE3uzZuYJMcAn5o8dA1Er4fj80Ko-oC1k3Jz8o3Ph7-cOKSxu_xghIA_5cxrunNZxQ-r4NqTr8Lqe798ZO0UleZeD8sUw70_Y_E398-EawFb2q_QZXaqrT5lLQYGNgJZHdpu-eNqwFTPrTCEn-t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی وقوع دو انفجار را که تقریبا هم‌زمان در تهران و کرمانشاه و در ساعات پایانی یکشنبه گزارش شد به نشت گاز نسبت دادند.
سایت تسنیم، نزدیک به سپاه پاسداران اعلام کرد که در ساعات پایانی روز یکشنبه، «انفجار گاز» در محله باغ ابریشم کرمانشاه باعث مصدومیت ۲ نفر شد.
این سایت‌ همچنین [با انتشار عکس بالا] مدعی شد که انفجار در یک واحد مسکونی در «فاز یک اندیشه» در استان تهران ناشی از «نشت گاز» بوده است.
خبرگزاری ایسنا به نقل از سخنگوی اورژانس استان تهران می‌گوید این انفجار تاکنون ۶ مصدوم بر جای گذاشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/75824" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=VrZeXbt8XhgmaJuYMXs2QPPLUSfhZ3fCtW74xGcSjGRmNgsOiUehFRSu_4boR50GMMSv_u5QeI8b25GWNpOMISUrDcO_yy7IZl6izkoC5bG3kLabntVa_XqDn8eUruw5QIA12kvyBM1Aa_oEtCcws5Bk6_UPmdpdkkr5JmkDfaTO5TMINZq_aW4Lvui5mHHqbZWNrancRY8NKmKhVdaVyOVRF8AWG2Y_BIloZeGK-TN86TQcLq6wHY6LwGnoJupIIjgdHTlqOuDWcr9cD7zVPQuxs9fzU07ziQ5r85N-lGuOQXD0Luzf-nPU3EnOYquqc3myexXUKDpH0scT-Gzx1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=VrZeXbt8XhgmaJuYMXs2QPPLUSfhZ3fCtW74xGcSjGRmNgsOiUehFRSu_4boR50GMMSv_u5QeI8b25GWNpOMISUrDcO_yy7IZl6izkoC5bG3kLabntVa_XqDn8eUruw5QIA12kvyBM1Aa_oEtCcws5Bk6_UPmdpdkkr5JmkDfaTO5TMINZq_aW4Lvui5mHHqbZWNrancRY8NKmKhVdaVyOVRF8AWG2Y_BIloZeGK-TN86TQcLq6wHY6LwGnoJupIIjgdHTlqOuDWcr9cD7zVPQuxs9fzU07ziQ5r85N-lGuOQXD0Luzf-nPU3EnOYquqc3myexXUKDpH0scT-Gzx1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی، در واکنش به گزارش شبکه ایران اینترنشنال درباره استعفای مسعود پزشکیان، رییس دولت، این خبر را تکذیب کرد و آن را «شایعه‌سازی» خواند.
شبکه ایران اینترنشنال، ساعاتی پیش در گزارشی اعلام کرد مسعود پزشکیان در نامه‌ای رسمی به دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خواستار کناره‌گیری از سمت خود شده است. این رسانه همچنین نوشت در این نامه به وجود اختلافات ساختاری در اداره کشور و نقش نهادهای نظامی در تصمیم‌گیری‌های کلان اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/75823" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZOSd2jTQ7r-YPNZ5cvpO0oWFRw11wEQbfDtppJxRL-ixvsSnlI1AKve_NGfYnCb025yx6zUs_EUVKWKBXWc8-9ua2Gx8mg-jjo_AqiLGq9CIjobHIUDnPRBJGyftRjLevxhUMdBchbluDvrFVhfmvmd0PqC0DpeR2I5EDmDQ403Pker3z6GK88Y5VkSJHg7zr538OYFCZL4S0A95ivhdj1BBaZ_drs5Kg1dq3yYOlL9yupRdyEH93ItLHlilUiRxButJ1_vtSorZ4xi3xSOV9h3KKia17PHqk4RQswpV4Dvs6GNf_aZP3nS4YIIrgXQy8WnsV5t1rwYIm-teduQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/75822" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmxONpRp06JslwADMrPcFZy7AdewQsUEK22Vd04DXqftZCEo2fbTZ9Y2D-ZZb7iF9-i6tvii9TwBwSYo7edHOM1RjOflWrSgsD86GA9aZUrw8CcoZTekMIziWdYkJ7umqcKOCEqyIttKlq5PuGnbuu-_YUEmgixXKC81MCS1uPX8KEUBFrM_Vp1mfRFx0YyF6ZEEqNrRr6oN4rB2Fxy1wBfqo1un-Lq2erExJl1ATpkhN70QmB71tBvUobC3stRJoHprMth2gS5F7ghVKH--ycFDCSG50pD6ijdHtpwEEm85dEZ7QKmxXnAjUJzhj9lvEkDn_uHu9QH9nCyLe2QzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پیاهو، مردی که تصویر معترض نشسته مقابل نیروهای پلیس یگان ویژه در مقابل پاساژ علاالدین در آغاز اعتراضات دی ماه سال گذشته را منتشر کرد،
به گفته وکیلش
به ۱۰ سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/75821" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6220710705.mp4?token=HjxWAC4PFAEz2eHuzFI7SgUHh4gBZdjqDsFBNnREZb9LqX2RuNB49fRSn9B0z1vRu6bUq2SOh_PQISrlivt_yVpY-dc5mMtNnlDj_hDa_BdHhgAMcuZo29T3rHClpnDdNnux5s-r08lthmgdYgmgqxc4Hs4ZQ7nWrpFungl_eIqwrzWorSYbQgVTiAeWJI8w6uVZ2R03f_wy58Zrrg0-uvI1jdbezHwUcl8UvbO9uWHl7R96YVk30zBH1DpkfMHW8lxlqGDkVJFR1kgmByXv0VHTe4opNh-aUDfyCg1GBgnSTrGzCsOA0AxYSROUNTvMfNiBbyfI2fq8S173PIGZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6220710705.mp4?token=HjxWAC4PFAEz2eHuzFI7SgUHh4gBZdjqDsFBNnREZb9LqX2RuNB49fRSn9B0z1vRu6bUq2SOh_PQISrlivt_yVpY-dc5mMtNnlDj_hDa_BdHhgAMcuZo29T3rHClpnDdNnux5s-r08lthmgdYgmgqxc4Hs4ZQ7nWrpFungl_eIqwrzWorSYbQgVTiAeWJI8w6uVZ2R03f_wy58Zrrg0-uvI1jdbezHwUcl8UvbO9uWHl7R96YVk30zBH1DpkfMHW8lxlqGDkVJFR1kgmByXv0VHTe4opNh-aUDfyCg1GBgnSTrGzCsOA0AxYSROUNTvMfNiBbyfI2fq8S173PIGZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با فاکس‌نیوز درباره ایران اعلام کرد: لایه اول و دوم حکومت آن‌ها از بین رفته و اکنون با لایه سوم روبه‌رو هستیم. شاید آن‌ها دیده‌اند برای بقیه چه اتفاقی افتاد و می‌بینند ترامپ آماده انجام چه اقداماتی است.
بسنت افزود: اگر ترامپ با این توافق موافقت کند، همین حالا به رهبران جمهوری اسلامی می‌گویم که او این توافق را هم از نظر نظامی و هم از نظر اقتصادی اجرا خواهد کرد. آزادی کشتیرانی در خلیج فارس از طریق تنگه هرمز باید به وضعیت پیشین بازگردد.
او درباره اینکه آیا ترامپ «کار را تمام خواهد کرد» گفت: اگر «تمام کردن کار» یعنی اطمینان از باز بودن تنگه هرمز، در اختیار گرفتن اورانیوم با غنای بالا و نداشتن سلاح هسته‌ای از سوی جمهوری اسلامی، پس کار تمام شده است.
بسنت تاکید کرد: چه از طریق مداخله نظامی، چه محاصره یا فشار اقتصادی، این نخستین بار در ۴۷ سال گذشته است که ایرانی‌ها درباره نداشتن سلاح هسته‌ای گفت‌وگو می‌کنند. این موضوع پیش‌تر ممنوعه بود و اکنون برای نخستین بار روی میز مذاکره قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75820" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهمند عليپور Farahmand Alipour</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=UUnfa1H0hVZCXXOxM0e1Ane_b939twrkuB9me02xKRWvZygHqijfrFFWex4EAtEBQt4Rjbic0oi2LQBJ-lT1yhettezA0YcM94jgi3_aX_nzJnxR2Js3_gD1lvZxo9Ex7q1qnhThiQ8FhGaRcLQhiiBs6dbZm2f9bEMpLrPyEfVTivt7pmmw6j9zPt-15jma9mlembECvCTAUc5Sp08EY_8e9o2kfKECT6uo4DJhsG7hY4qsxBC3rACEn399UTOOFmFH5_2IAhiWrRjzUjkqyqa2GahDFo_UGerpcjQC_eVoCtIsK8OvR9d_kd965PUaDLEfiad24PX8iuE3PoEGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=UUnfa1H0hVZCXXOxM0e1Ane_b939twrkuB9me02xKRWvZygHqijfrFFWex4EAtEBQt4Rjbic0oi2LQBJ-lT1yhettezA0YcM94jgi3_aX_nzJnxR2Js3_gD1lvZxo9Ex7q1qnhThiQ8FhGaRcLQhiiBs6dbZm2f9bEMpLrPyEfVTivt7pmmw6j9zPt-15jma9mlembECvCTAUc5Sp08EY_8e9o2kfKECT6uo4DJhsG7hY4qsxBC3rACEn399UTOOFmFH5_2IAhiWrRjzUjkqyqa2GahDFo_UGerpcjQC_eVoCtIsK8OvR9d_kd965PUaDLEfiad24PX8iuE3PoEGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴
در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته
«دو گزینه بیشتر نیست»
یا جنگ و خونریزی یا مذاکره مستقیم
«برای از بین بردن غنی‌سازی و موشکی»
این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات آمریکا و جمهوری اسلامی همچنان همون چیزهایی بودند که باعث یک جنگ شد، و این مصاحبه یک ماه پیش از آن بود که دست به قتل‌عام مردم در خیابان‌ها بزنید!
الان هم محور مذاکرات کاملا مشخصه!
همون چیزهایی است که جنگ ۱۲ روزه رو رقم زد. همون چیزهایی است که در آبان ماه عراقچی در تلویزیون گفت.
خون تک‌تک ایرانیان از جمله کودکان میناب پای شماست! شما طرف مذاکره بودید، شما انتخاب کننده و تصمیم گیر بودید.
و شما بین اورانیوم و موشک، و یا جان مردم، زیرساخت‌های کشور، فولاد و پتروشیمی و…
اورانیوم و موشک و دشمنی با اسرائیل و آمریکا رو انتخاب کردید! هنوز هم طرف مذاکره و تصمیم‌گیر شما هستید! و‌ جنگ ‌از سر گرفته بشه باز تصمیم و انتخاب شماست و مقصر شما هستید!
نمی‌توانید پشت کودکان میناب قایم بشید و از کشتار دیماه فرار کنید!
هر خون و ‌هر ویرانی ، همه پای شماست.</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75819" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bEhvKdu7lLaX8taZ8upJggVQORWxGLyxXbhXDd8T3obO8JOwtvcG7dNgf1JreCCrpdoaApRSeCX7ykpn35IadaI72S2oP8h974FR0LRE00-4BgTHFnP_rn8c5Xuc5OJrujNDnJ_ZmulD3deCZY1oirhEshiMo51fck06UVIvXzA0O8p7IPH9rJQsU6BEzhCy_K4zRd61KPEQ4CBF11kOZxFqXLfzC-2nbuDpWHvqq-R0I_AON-X0XAXVKn7JME-B5e8pBfwxmeJQB7I9mS0_acrYfvg-tCmFnK78OhzgOrkC5MFtwMi2gr47u2PIui9PlpqrAnVANibZ6araBmQ_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن و حسین امیری، دو برادر دوقلوی ۲۰ ساله محبوس در زندان قزلحصار کرج، از سوی شعبه ۲۶ دادگاه انقلاب تهران به ریاست قاضی ایمان افشاری به اعدام محکوم شدند.
بر اساس اطلاعات دریافتی هرانا، مبنای صدور این رای اتهام «جاسوسی برای اسراییل» عنوان شده است.
یک منبع مطلع در گفت‌وگو با هرانا اعلام کرد در کیفرخواست صادرشده علیه حسن و حسین امیری، مشاهده تصاویری از ساختمان‌های آسیب‌دیده به عنوان مستند اتهام «جاسوسی به نفع اسراییل» مورد استناد قرار گرفته است.
این منبع همچنین گفت: «حسن و حسین امیری به دستور بازپرس پرونده به صورت جداگانه در زندان قزلحصار نگهداری می‌شوند و از حق ملاقات با یکدیگر محروم هستند. این دو زندانی در حال حاضر در سوییت ۳۵ این زندان محبوس هستند.»
بر اساس این گزارش، این دو برادر پیشتر در یکی از ایست‌های بازرسی و پس از بررسی تلفن همراهشان بازداشت شدند.آن‌ها پس از بازداشت، به مدت دو ماه در وضعیت بلاتکلیف در زندان قزلحصار کرج نگهداری شدند.
👈
حسن و حسین امیری از دو سالگی در مراکز بهزیستی پرورش یافته‌اند و خانواده‌ای برای پیگیری وضعیت قضایی و حقوقی خود ندارند. به گفته آشنایان این دو جوان، نبود حامی خانوادگی بر نگرانی‌ها درباره روند رسیدگی به پرونده آنان افزوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75818" target="_blank">📅 18:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M--5bQeo79TApzUAMiUq-PCW6hmxVphHK2fDXo4BeiFk0_bkwI2ZweTJy27QCSAHM2ocrflRjY7qsGB61cCGcYZdcu7NZoA8PmZqWj3zv1lccVt7PrAOR4r8DVq86EYC6RVqZyAdm7OeTuNe4CqjgL9iNVx1YMEracNL5yBZysw1uXgcb2ZWDbFQeDr28rm_ouEGS4KkOMjoWoCA5fTiRE1RdlpFPjyog3L-uYhcZdYUtB1VQb_4kRyez9XdA5xSN3Oje_Xm7UGZfGk1hCg-7LeAvWo6o0t5GIPyl2rCJ3SP0uPu2Va2OPNAD3y4FAmKKrNHQ9qJGjzfkrbD_ywiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران چندین ورودی تأسیسات موشکی زیرزمینی خود را بازگشایی کرده است
شبکه خبری سی‌ان‌ان روز یکشنبه ۱۰ خرداد با استناد به تصاویر ماهواره‌ای اعلام کرد ایران توانسته از زمان توقف جنگ شماری از زرادخانه‌های موشکی مدفون خود بر اثر حملات هوایی آمریکا و اسرائیل را از زیر خاک بیرون بیاورد.
حملات آمریکا و اسرائیل با تخریب جاده‌ها و مسدود کردن ورودی تونل‌ها، دسترسی ایران به پایگاه‌های موشکی زیرزمینی را محدود کرده بود.
سی‌ان‌ان ادعا کرده است که ایران تاکنون ۵۰ مورد از ۶۹ ورودی تونلی را که در ۱۸ تأسیسات موشکی زیرزمینی توسط آمریکا و اسرائیل هدف قرار گرفته بودند، بازگشایی کرده است، از جمله در پایگاه‌هایی در خارج از اصفهان و در اطراف خمین.
بر اساس گزارش این شبکه خبری، ایران همچنین بخش‌های دیگری از این پایگاه‌ها را نیز ترمیم کرده است؛ از جمله جاده‌هایی که آمریکا و اسرائیل برای جلوگیری از تردد پرتابگرهای موشکی بمباران کرده بودند. تصاویر ماهواره‌ای نشان می‌دهند که تقریباً تمامی گودال‌های ناشی از بمباران اکنون پر شده‌اند و در دو پایگاه، این جاده‌ها حتی دوباره آسفالت شده‌اند.
ایران شبکه پایگاه‌های زیرزمینی خود را در عمق خاک و در مواردی زیر کوه‌ها ساخته است تا در برابر حملات هوایی مصون باشند، به همین دلیل آمریکا و اسرائیل بسیاری از ورودی‌های این تأسیسات را بمباران کردند؛ اقدامی که در کنار تلاش برای شناسایی و نابود کردن پرتابگرهای موشکی، باعث شد توان ایران برای شلیک موشک به‌طور قابل توجهی محدود شود.
این حملات خسارت سنگینی به پایگاه‌ها وارد کرد؛ به‌گونه‌ای که بیشتر ورودی‌های تونل‌ها زیر حجم عظیمی از آوار مدفون شدند و جاده‌های منتهی به این سایت‌ها نیز به‌شدت تخریب شدند.
سی‌ان‌ان می‌گوید باز کردن ورودی تأسیسات موشکی زیرزمینی می‌تواند به ایران این قابلیت را دهد که در صورت وقوع دور جدیدی از درگیری‌ها، موشک‌های بالستیک بیشتری نسبت به اواخر جنگ ۴۰ روزه به سمت اسرائیل و کشورهای دیگر شلیک کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75817" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75816">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ-yoeMjhTrOc3uS36i0HvQOHhQZ98qupGRYfQF8IfVyNcypHFxGncNmDrBbu9P-evtaM713oWIhmeoSCufzLUAyD1FTeRRQ16k5NA58SV8nWXY-XMsW3u-a-Awud-GHpCJqQU1KH_gZAS5oxJb7A7-bMgQaRBnXJAZ9YGXx7dnTsoYrE6z9JCBfZXi4uGt-Yk_Gc0qZdFq5jO5tcBwOeBgDUFqgEauWZgXYBzBqo8JfKLqS5YX5OrfL7ozzB_0Cv68BX6X6KvYnb8Sq4bML6ZM1ii88IzqgrPqiJSUk9AGPGOVGSDpM7CAHSSau_PSc7tQp0av9Pqt8nRFZbmKv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس مصوبه جدید شورای شهر تهران، هزینه خدمات مرتبط با خاکسپاری در بهشت‌زهرا به‌طور میانگین حدود ۴۰ درصد افزایش یافته و در برخی موارد رشد تعرفه‌ها به ۵۰ درصد رسیده است.
روزنامه دنیای اقتصاد گزارش داد نرخ خدماتی از جمله حمل متوفی، تغسیل، تکفین، تدفین و برگزاری مراسم افزایش یافته است. بر اساس این مصوبه، هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری ۵۰ درصد افزایش داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75816" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH1M7OGMw0X354y8WCMWBLzZReBIP5dr-Io6PkFRevixV4b4CtsuFjjynGmyzaLWlaGBO4YLkEvhEp-CaaX7cfTs-A6IXNmOZkl8Ot4n6OljMqvmI5jZj6w-RusyodCU2cbU1lTMaAmLHKzhRYwoTeWSpjRRaxxmkkeoEBVM8gc4u5r4XrSdfQY0hL8sBLWXMGqL44AMKAY6qxx1bisbBKQ4DlMoaPnfhxr0cZ3aYTAh3pG3pcN2DneuviW0KFadVF--0DrNWhmFpvNSiC4tuXEmeGca9s6PFqLEUNAa5UcbFnUFMzQcf86F5FWpwZBqSi-2Ng1b29lek0fD6uQEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد زهرا شهباز طبری، زندانی سیاسی محبوس در زندان لاکان رشت، پس از نقض حکم پیشین در دیوان عالی کشور، بار دیگر از سوی شعبه دوم دادگاه انقلاب رشت به ریاست محمدعلی درویش‌گفتار، به اتهام «بغی از طریق عضویت و فعالیت در سازمان مجاهدین خلق» به اعدام محکوم شد.
این زندانی سیاسی ۶۸ ساله، در فروردین ۱۴۰۴ در منزل شخصی خود در رشت بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75815" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHQuqTefCbbtWLKcvNjuSbETaDb21XdX_0HgJFjYBWckFDaX5k_UeXD4HFsbw4P24b2GrBtwJHnd03PPs9lPVzu9nmVur1f7BvznXY83q9UM7c-PAUmO6GNe6SrW9ruC7d0C4_h0xPpyzDM4cTZUAcxySmmpmlyDcVup2jYIX_w-CySyFfeeudLU1Z_qnAf1-_D2MvdPFP_ZpdQcfRx9LXY0dV1K-29k6yyrHkba2KneFmNzbAmVYK7yFKyQhuNltlhwAAMh8BsxIh_kjMTdLIjiKVAM2yCHw4VDj5UEk4I51xQ6dACWiVJS75mRe5r4Sb6VnyGSEX5x0fbLZU3Peg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز یک‌شنبه اعلام کرد‌ «طی شبانه‌روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینربَر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.»
ساعتی پیشتر روزنامه اسرائیلی «اسرائیل هیوم» نوشته بود که ده‌ها نفتکش حامل نفت و گاز طبیعی مایع در هفتهٔ گذشته با اجازه آمریکا و پرداخت عوارض به ایران از تنگهٔ هرمز عبور کرده‌اند.
این در حالی است که دولت آمریکا بارها اعلام کرده است با پرداخت عوارض به ایران برای عبور از تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75814" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1wZrKPwqopwvj3rgfyVCYh3jWchLvxLALLi0ezHCMoQIak0nHaM4vp-lgQxlGRNsO8UyhbyMsqWaW_f7Vetn_avuUaM92_T3tbMC0TIse59nzPNcBG-47d31sa5I3UsyBRN6SUbS55HF9MY4PgzURzmhSF89KJQRmTLQDJRTAhV4hh2TJ2-lMkowinJrQ2PwC2iQnfqqDAHSBlrpS3Zc1FAEzDgg3ZSr6bSHaMTlfdKAf0-hFyep6aHhf3ASsuztdbl-tNqp7y4lq8sQ4FS2fsxkiG56kurNnlypnHG4DMp8bihOj8Ire6p99BfIXpLbSAykCScQHpXxEtzS120FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=eLnnb8qKtjqCgQIDzIruYlWk_eNb59Z9j615exZwNP4D-B3Eg6Z8sekBowY8wa1AnOMFI1uAWggRo2ggjQ5gqANG7GHMxoeNOWKUSFhbWIKm33Hpg-T2T9YNwu6SIx7IWnx0Vb5g25bu75-Zh9YgwLLlS-r5F7uGmbnBiEPkACZk-sgyeDdNpeu-yvZ4__8XIxihTLB9ouZdMQcAETGdA8a3gWIgK5CGy_PL4BohXZFkJuA30tW3Sa43sErZBp0qfn-1RZxy9Jzryx8Bi_pFstEwc5HKyInSFx2lOp5TRucFGrvqN05Kh90uzMXdE3gT6qcHf9iKjMNkJl7PDr9jZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=eLnnb8qKtjqCgQIDzIruYlWk_eNb59Z9j615exZwNP4D-B3Eg6Z8sekBowY8wa1AnOMFI1uAWggRo2ggjQ5gqANG7GHMxoeNOWKUSFhbWIKm33Hpg-T2T9YNwu6SIx7IWnx0Vb5g25bu75-Zh9YgwLLlS-r5F7uGmbnBiEPkACZk-sgyeDdNpeu-yvZ4__8XIxihTLB9ouZdMQcAETGdA8a3gWIgK5CGy_PL4BohXZFkJuA30tW3Sa43sErZBp0qfn-1RZxy9Jzryx8Bi_pFstEwc5HKyInSFx2lOp5TRucFGrvqN05Kh90uzMXdE3gT6qcHf9iKjMNkJl7PDr9jZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه مجازی صحن مجلس شورای اسلامی به ریاست محمدباقر قالیباف و مشارکت آنلاین ۱۸۷ نماینده و حضور ۱۴ نماینده برگزار شد.
در این جلسه که اولین جلسه از سومین سال مجلس دوازدهم بود، اعضای جدید هیئت رئیسه مجلس سوگند یاد کردند.
جلسه روز یک‌شنبه، دهم خردادماه، همچون جلسات معدود گذشته در مکانی مخفی برگزار شد.
محمدباقر قالیباف در همین جلسه تأکید کرد که «تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی تأیید نمی‌شود».
قالیباف که از او به عنوان رئیس هیئت مذاکره‌کننده ایران نیز یاد می‌شود در این جلسه بیانیه‌ای را قرائت کرد و در آن ادعا کرد که «در حال عقب نشاندن دشمن در یک جنگ تاریخ‌ساز هستیم».
@
VahidHeadline
محمدباقر قالیباف، رییس مجلس شورای اسلامی گفت: «سومین سال مجلس دوازدهم را در حالی آغاز می‌کنیم که یاد و خاطره رهبر شهید با ماست و هنوز فقدان رهبر و پدر امت را باور نمی‌کنیم.»
او ادامه داد: «رهبرمان به ما آموخت مقابل زورگویی و تهدید، ذره‌ای سر خم نکنیم و با مشت‌های گره کرده مقابل خصم تا آخرین قطره خون مبارزه کنیم.»
قالیباف اضافه کرد: «دیدن جای خالی رهبری برایمان جانکاه است، ولی دلگرم به مدیریت و رهبری جدید هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75812" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DV916VZkeeEJ3QHL6uUxVNG4EJpx4RFFKyVRXHquCOz30dyegCTZBRuZscuZ8nE6o49_yE-IjWmYDiU-7mHSUxe1KVx0rtxcOToaawNlx760lDm-Ck0XuEDK-XSkyCADizx1daWKtPCd1xT936N56DlhNh_EQ_56KJmc0Tq1CvbTP_DFXp2J6BXhF747YZnhBkKjsRTk4LeJlgEmghCBq2euKrXxg4Gom8oOZ0MhTt5_yL-IEOrlQc68nyaEhYZg70cCiRX6AF7ibcGEUGbeRkMy1oROG7tbAg8cP8LyG6rqbiPenGvmQFK5zQtpy2cPpG-9v3xA-clh7ozfgCsDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=RVMMQYIICWskPLYvKNa77bGOiCRZsI3DhHcDJIr7LK2m_qBKswiyvG_ruDrlrGOnXbTmn9kZfsuhLG2Fij_iXrXLFABHPm92J1RqZJ8TxgUF4wtSG6XrA8Gpx8LbdIEho8bqrNIGG083oZDSFMzIBNgAlPZz4j7iC_DOIIcBVha9NxE5dOT3iGQQGFi2mEWD690Q9lNInRQS2BjJrAqzy-1fsvPzhXx6EGQi-t7pNX_f0bb3kR2AkFCdBTBYYKg0uPGZFkNTI_P3CiWfp9nMXsAXXfKWi5jCyd93Spwq9ijBdN8gx87_quF2CPP07FW9aIBHEVdqVcM4eyCOL585Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=RVMMQYIICWskPLYvKNa77bGOiCRZsI3DhHcDJIr7LK2m_qBKswiyvG_ruDrlrGOnXbTmn9kZfsuhLG2Fij_iXrXLFABHPm92J1RqZJ8TxgUF4wtSG6XrA8Gpx8LbdIEho8bqrNIGG083oZDSFMzIBNgAlPZz4j7iC_DOIIcBVha9NxE5dOT3iGQQGFi2mEWD690Q9lNInRQS2BjJrAqzy-1fsvPzhXx6EGQi-t7pNX_f0bb3kR2AkFCdBTBYYKg0uPGZFkNTI_P3CiWfp9nMXsAXXfKWi5jCyd93Spwq9ijBdN8gx87_quF2CPP07FW9aIBHEVdqVcM4eyCOL585Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی انتظامی تهران کافه‌ای در خیابان ولیعصر را که در آن برنامه‌های موسیقی اجرا می‌شد، به بهانه آن چه «فعالیت‌های مروج فرقه‌های انحرافی» خواند، پلمب کرد.
مرکز اطلاع‌رسانی پلیس جمهوری اسلامی در اطلاعیه‌ای نوشت: «این کافه با برگزاری برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار، و آنچه که ماموران توصیف کرده‌اند "تحرکات شیطانی" فراهم آورده بود.»
نیروی انتظامی جمهوری اسلامی نام این کافه را ذکر نکرد اما ادعا کرد که «مشتریان این کافه، شامل دختران و پسران جوان، در وضعیتی غیرطبیعی و با حرکاتی عجیب و غریب، که از آن به عنوان “شیطانی” یاد شده، مشاهده گردیدند.»
پیشتر نیز بسیاری از کافه‌ها و اماکن کسب و کار به اتهام‌های مشابه پلمب شده‌ بودند اما جمهوری اسلامی سرکوب‌ شهروندان را از زمان اعتراضات دی‌ماه گذشته تاکنون شدت بیشتری داده است.
موج تازه اعدام‌ها، صدور احکام سنگین و بازداشت‌ها نگرانی فعالان و نهادهای حقوق بشری را برانگیخته است.
@
VahidHeadline
ویدیوی بالا رو هم به عنوان "تحرکات شیطانی" در اون کافه منتشر کردند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75810" target="_blank">📅 15:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpRUIdYKWyHpSn3PXtId-mRrnOFF41tBskh8huuMX9T05p4GLHKatRhy2J00aztNFbygfu5eM3HH1lYKSHPqLFlr2eA750ec6Wmwlm601GzqrpVaBRxiOqxA7oqhuP4s_8deyXtpk7hSmwOHsno5YT5stQbfTrGOhajbBs6-Zb3FY2TO0rg-wdC_9zLXCfzYIg_tBVEV3GXgtZ8woo2b0zAIKDvAIY8Xdw658eioClYl_9ZOwIHmhu5jgd5gWDSZE4OnFfqVWp89oby1YJgBgq7DFjMyKwPkdP4JKG9xn8XGOfXjGQt4yCa37fFN60L3ItLDr-wadYKrIloygkopwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس، ترجمه ماشین:
رئیس‌جمهور ترامپ در جلسه‌ای که روز جمعه در اتاق وضعیت برگزار شد، خواستار چند اصلاح در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن رسیده بودند؛ این را یک مقام ارشد دولت و منبع دومی که در جریان موضوع قرار گرفته بود، گفته‌اند.
...
مقام‌های ایرانی به رسانه‌های دولتی گفتند که آن‌ها نیز متن نهایی را تأیید نکرده‌اند؛ هرچند دو مقام آمریکایی پیش‌تر در طول هفته مدعی شده بودند که تهران آماده امضاست و همه چیز به تصمیم ترامپ بستگی دارد.
به گفته این دو منبع، ترامپ از تیم خود خواست تغییراتی در پیش‌نویس مربوط به بندهای برنامه هسته‌ای ایران ایجاد کنند.
در شکل فعلی، این تفاهم‌نامه شامل تعهد ایران به دنبال نکردن سلاح هسته‌ای است، اما امتیاز مشخص دیگری فراتر از آن در آن نیامده است.
در این متن آمده است که یک بازه ۶۰ روزه برای مذاکره درباره تعهدات هسته‌ای ایران و کاهش تحریم‌ها از سوی آمریکا وجود خواهد داشت؛ نخستین موضوعات در دستور کار نیز چگونگی تعیین تکلیف ذخایر اورانیوم غنی‌شده ایران و محدود کردن غنی‌سازی بیشتر خواهد بود.
ترامپ می‌خواهد تلاش کند این بخش را اصلاح کند.
یک مقام ارشد دولت گفت: «موضوع، جزئیات بیشتر درباره این است که آمریکا چگونه مواد را دریافت می‌کند و زمان‌بندی آن چگونه خواهد بود»؛ منظور او اورانیوم غنی‌شده بود.
منبع دوم گفت ترامپ همچنین می‌خواهد برخی از عبارت‌ها درباره بازگشایی تنگه هرمز را اصلاح کند.
این مقام آمریکایی گفت به ترامپ گفته شده است حدود سه روز طول می‌کشد تا ایرانی‌ها با پاسخ برگردند. این مقام ارشد دولت گفت: «آن‌ها عملا در غارها هستند و از ایمیل استفاده نمی‌کنند.»
این مقام ارشد دولت گفت: «توافقی در کار خواهد بود. اینکه چقدر قریب‌الوقوع است، باید دید. ما حاضریم صبر کنیم تا رئیس‌جمهور آنچه را خواسته به دست بیاورد. ممکن است یک هفته طول بکشد. ممکن است کمتر باشد. ممکن است بیشتر باشد. امیدواریم در آغاز هفته چیزی داشته باشیم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/75809" target="_blank">📅 05:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMprB_aJzVYk2CMoQ3Ao_Nll-7eoPR9H77lH91Do2prOWJy3r2glOUaP9eiUwIiu33Gtlb8h5wQwthu-UR6xkgkJh87Y4xUtLULrfvWHzAugG0QlB0l3c38G_ZXn_JRq5siq3JYzAyev-nl0cuq9hZbSN2ptHRit6gcDBHe15Y636KouffoZffW_EWh6UC515zOeYXDXkL5eE7d73vckz9AzX3Uva-oD7p1LySqzmVQKlC2P9d33zyFgCnVJ9H0WYoBZylFQa0Hd2-z42e5yd8RCOyt-5XkxBC-0_3oFk3Utf_xKFkTvof-RHfAj0-dozbZDqyPR0lg_GWF4MD1HYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی سپاه بامداد یکشنبه، ۱۰ خردادماه، اعلام کرد یک پهپاد «ام‌کیو۱» (MQ1) ارتش آمریکا را منهدم کرده است.
خبرگزاری فارس نوشت: «این پهپاد با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت که بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/75808" target="_blank">📅 04:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEBfSbtL7fRJpS4hoZUrx82exa03gWd3kxxpuqjaLueu-n8LbpdbSt6sXvNJ0hNxeKZdFAvsHqoOeJomj017sjYQTzu4l48CcLnzuWo8wQhUbh0NA1m-MPUTrJF6PIwq9amqzXislK_BYGIBATRvPU6ZZW25dlqtl8Y-HThnYiPfoppXYRhTTkpCZ6QZyz7QsTCJHkMQkI7-E33xwDCFga9fJbEL-0GkxPJJex9RbmTYvQFTh-62FEEbhC4-4-vWZNWpyvqiDFEvtRtCFZyOAm4CP5izjAvcJb4M8A5IckByx2KB3a3cdTgz1CWHoITG4tp-dY7iwQMAocOdB6fbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، اعلام کرد نیروهای این کشور یک کشتی تجاری با پرچم گامبیا را که به گفته واشینگتن در نقض محاصره دریایی به سمت یکی از بنادر ایران در حرکت بود، در خلیج عمان هدف قرار داده و از ادامه مسیر آن جلوگیری کرده‌اند.
سنتکام روز شنبه نهم خرداد در بیانیه‌ای گفت نیروهای آمریکایی روز هشتم خرداد کشتی «لیان استار» را هنگام حرکت در آب‌های بین‌المللی به سوی یکی از بنادر ایران شناسایی کردند و بیش از ۲۰ بار به خدمه آن هشدار دادند.
به گفته این نهاد نظامی، پس از آنکه خدمه کشتی به هشدارها توجه نکردند، یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت.
سنتکام افزود این کشتی دیگر به سمت ایران در حرکت نیست.
در این بیانیه آمده است که از زمان اجرای محاصره دریایی علیه ایران، نیروهای آمریکایی پنج کشتی تجاری را از کار انداخته و ۱۱۶ کشتی دیگر را وادار به تغییر مسیر کرده‌اند.
سنتکام جزئیات بیشتری درباره محموله کشتی یا مقصد دقیق آن در ایران ارائه نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/75807" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaMDUfKN5qkuzEHFaMXWNkogZy3igOD2ab39ZKSfd81kIN_Rfyj9XfejUUo1NF7W1KRX-FgLerVUTj1IpNJ3JafnxMDXQ2K5QS2jHAT0BIThpwjLPhHXU-ZJ6LiGAKhNx-iJJYkSaARWcCk_Cp43qh0UgQ3uVC_PbwsBf6XuzuRtBxjK1hk4_G_wVFmH1zdoCTeBRHr5y0ltxnYgO4VrhPd1qPROLjYqwL0DeJyEE2UCkbVbnj8BPcCRrBtI7F_HKUrtNbye3nDkxgZ-XKmEJ6Us2-S6Iiu-oycJlLZkeCSlkLaPA4oeSh3z04Lu6fXjEN85eQlXZZUVLlAJizmmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی در گزارشی درباره تفاهم احتمالی بین تهران و واشینگتن با عنوان «جزئیات غیررسمی»، اعلام کرد آمریکا متعهد شده در طول ۶۰ روز امکان دسترسی جمهوری اسلامی به ۱۲ میلیارد دلار از دارایی‌ها را به‌گونه‌ای فراهم کند که این منابع قابلیت انتقال و هزینه‌کرد در بانک‌های مقصد را بدون محدودیت داشته باشد.
این گزارش افزود که بر اساس این تفاهم، جمهوری اسلامی مرجع انحصاری تشخیص ماهیت شناورهای عبوری است و هر شناوری که محموله آن تهدیدآمیز شناخته شود یا بهره‌بردار نهایی آن در «خصومت» با جمهوری اسلامی باشد، به عنوان کشتی تجاری شناخته نشده و اجازه عبور از مسیرهای تعریف‌شده را ندارد.
صدا و سیما تاکید کرد که این رونوشت هنوز در حکم یک تفاهم غیررسمی است چون مسیر آن همچنان در چرخه بررسی، مذاکره و بازبینی قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75806" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNY6peCUMgz7FkjiqTQKZjYyBTAIOgUtw-2XllcoFnNQ3QVWUoM_cVvvsBqkNqr3fqFaIhAedRbv83dFdc1w8k3sQ7Tyoy23ZqZuRcSiRhcjZ4_G90_X-85TojERCyIW9cH274ZY_Q1rlJR6wmatYaFenah7EumvJSpYtCbGgEh_HZ-_biWylQB1i5hHhDMZHauUU3SJcqLMjkyra-o_URVSlPPYGVcjNMjA4PCsE8oTeQTpF95YByHJsmEQ-nn-D2Ok2d_pCtUUIUiEALqoe0csG611yh4ar7t24TeDt50ZIXfIm15JWSm6KXI7-X1Fca_LlRqre0-8iaboWkWUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش نیویورک‌پست، در پی حمله موشکی جمهوری اسلامی به یک پایگاه هوایی در کویت، چند نفر از نیروهای نظامی و پیمانکاران آمریکایی مجروح شدند. این حمله در حالی رخ می‌دهد که دونالد ترامپ، رئیس‌جمهوری آمریکا، در حال ارزیابی پذیرش آخرین پیشنهاد صلح تهران یا بازگشت به شرایط جنگی است.
یک منبع مطلع روز شنبه نهم خرداد، اعلام کرد که در پی رهگیری یک موشک «فاتح-۱۱۰» توسط پدافند هوایی کویت طی ۲۴ ساعت گذشته، قطعات و ترکش‌های ناشی از انهدام موشک بر فراز پایگاه هوایی «علی السالم» فرود آمده و منجر به جراحت سطحی چند آمریکایی شده است. این حادثه همچنین خسارت شدیدی به دو پهپاد «ام‌کیو-۹ ریپر» (MQ-9 Reaper) به ارزش تقریبی ۳۰ میلیون دلار وارد کرده است.
این حمله در شرایطی صورت گرفته که دونالد ترامپ روز جمعه با تیم امنیتی خود تشکیل جلسه داد و اعلام کرد که قصد دارد تصمیم نهایی را درباره توافق با ایران اتخاذ کند؛ توافقی که شامل تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و آغاز مذاکرات بیشتر درباره مواد هسته‌ای ایران در ازای لغو محاصره دریایی آمریکا می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75805" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pTHuVgtYYyLkKwQTXKmdt4FbjabOFpFsPthdYWJCt5IE2vY_130MIAP0dDuSBIyYEaQttpGe1eY69OdTCqHPCGoKDacdKPnuF5HSbIUFnpMqIheBNi5p0kJ5i98E1x2myWWxR8Z4lbWtbIxngffslweAk7WCSwowlMyFxCUUAAy4jD6jU-3LmrXwB76s3LJJ5vCQuv89Zi-hrl8ywZjzoeeQ8OZf54sWGTfU2L8cs93Jy3J1vFIBA1mbxqUPto8LKgVIN_JPt9IaXSd8L1ocP2T1DmKBlQDFZzcN9AMhNnWGzXTZFtKYFyNSvXi9v0cfOpiqvRRTHK5vHTIx05xrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75804" target="_blank">📅 19:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=HwdjHdUUdOkJgp8Charr6bOQ_iZ_MNnYSV16hHep2WerRXoAwV095-9YCVcwf61wWuOmNzreWRFNinRsdntX_KHNL7Qgv0sjkxSNhfdSwMh5EwiBiLZfsr2yrhIWYaEf0i1bzqfPiFWd5kMuCRdXlQPHiz819xfptndZAEWBD7iYBkj16SDi4icjLRfLFEpcj1vpejAXDYEZwPfd6RyiQAfF6o-r_OW-2Vd6Y6g_eZa4rsOgCkJEtv3WNxJoRmp_QDXXT9JqzhQlrBMRrrZuCqMQ4QLzwRP-8R_v-SJ4iIXf_dau7jAQ0xOeci5mpCXlnA3k9EDidPwQvo-EemTB7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=HwdjHdUUdOkJgp8Charr6bOQ_iZ_MNnYSV16hHep2WerRXoAwV095-9YCVcwf61wWuOmNzreWRFNinRsdntX_KHNL7Qgv0sjkxSNhfdSwMh5EwiBiLZfsr2yrhIWYaEf0i1bzqfPiFWd5kMuCRdXlQPHiz819xfptndZAEWBD7iYBkj16SDi4icjLRfLFEpcj1vpejAXDYEZwPfd6RyiQAfF6o-r_OW-2Vd6Y6g_eZa4rsOgCkJEtv3WNxJoRmp_QDXXT9JqzhQlrBMRrrZuCqMQ4QLzwRP-8R_v-SJ4iIXf_dau7jAQ0xOeci5mpCXlnA3k9EDidPwQvo-EemTB7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز شنبه نهم خرداد گفت ایالات متحده در صورتی که مذاکرات با ایران به توافق منجر نشود، آماده ازسرگیری حملات علیه جمهوری اسلامی است.
هگست در جمع خبرنگاران گفت: «در حال حاضر تمرکز ما بر حفظ آمادگی و آماده بودن برای بازگشت به عملیات است، اگر لازم باشد.»
او افزود دونالد ترامپ «صبور» است و به دنبال دستیابی به «توافقی خوب» است که تضمین کند ایران هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
اظهارات وزیر دفاع آمریکا در حالی مطرح می‌شود که مذاکره‌کنندگان تهران و واشینگتن در تلاش‌اند اختلافات باقی‌مانده بر سر برنامه هسته‌ای ایران را برطرف کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75803" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kyhTdcJmrTpvS4HFkcSvGyJ8-guxjctqXL7zvmAZsvzezkihJHmPYKog0ughXACYTcMQA-xBnJJPE4SmOEmKPZJhteYMs4I1kqSZ0jL592a1OsSV-MqTdRg1fvwSgL_zbWgsvda0bw9HphaIe_Ozzk1lJc6rbjF2nIc01sl1RMKwEo_COR6QsbgPreC_6NchBtlIhEVl-AjcU_No_KiiSAnau89dKxayLGZB9lkdmGCIkWp7mkvQ585eS9one6RJhJjntmv1v6mNsEZcfXNlHHzz5C2HrLf_Ss7c6prFNlL18xGHgYdfaWX0oBCsOBgkdQfOQkzz-EOwUE1UIGct4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی نیلی، وکیل دادگستری، اعلام کرد شعبه اول دادگاه انقلاب شیراز بنیامین نقدی را با اتهام «افساد فی‌الارض» به اعدام محکوم کرده است.
نیلی در گفت‌وگو با امتداد گفت که بنیامین نقدی شامگاه ۱۳ دی‌ماه در شیراز به دلیل شعله‌ور کردن یک کپسول آتش‌نشانی به سمت ماموران نیروی انتظامی بازداشت شد.
به گفته این وکیل دادگستری، در ابتدا اتهام «شروع به قتل» به موکلش تفهیم شد، اما پس از آن اتهام وی به «محاربه» تغییر یافت.
او افزود پس از پایان تحقیقات مقدماتی، کیفرخواست بنیامین نقدی با اتهام‌های «محاربه»، «عضویت در گروه‌های برهم‌زننده امنیت کشور»، «اجتماع و تبانی به قصد ارتکاب جرم علیه امنیت کشور» و «فعالیت تبلیغی علیه نظام» صادر شد. به گفته نیلی، در خصوص اتهام‌های «ایراد صدمه جسمانی به ماموران» و «حمل سلاح سرد» قرار منع تعقیب صادر شده بود.
نیلی همچنین گفت قضات شعبه اول دادگاه انقلاب شیراز در جریان رسیدگی، مجموعه اتهام‌های مطرح‌شده را مصداق «افساد فی‌الارض» تشخیص داده و بر همین اساس حکم اعدام برای بنیامین نقدی صادر کرده‌اند.
وکیل بنیامین نقدی با اشاره به قصد خود و همکارانش برای اعتراض به این رای گفت که در مهلت قانونی درخواست فرجام‌خواهی خواهند کرد. او ابراز امیدواری کرد که با توجه به این که به گفته وی در جریان رخداد مورد اشاره هیچ فردی آسیب ندیده است و اقدامات موکلش مصداق افساد فی‌الارض نیست، حکم صادره در دیوان عالی کشور نقض شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/75802" target="_blank">📅 18:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت.
انگاری که درِ ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشی‌تون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75801" target="_blank">📅 18:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mrYeAAyD3Fol29vUHgiYoL7d8YQEt3pjkCmwtnuHvnvxePs-zhE4-66FK9tGZ0CX5OXteXXN2ijAuQuss6bLTNOi0p7mfihdWU99KpaunEFXa83068klDLYcJsb0UZ-PuUrtS5v-8L4NMPdQ_ef7hKVVWcmBBYJ5bzfvN9bcXhkEgjrMgt49u-0Mhf372u91PPWG9l7BS0clu7iyKydZ2ZGWpAHIl2Ni2kOLl-c_UVGgP9kDlawzhRxVnCWnDIZdpgYsZqAs6vMF3vmthUfIMmHIP7iLFh_FWyWRo1Z7DsIT8Qho17lqewW37JzH2aCFOXo2d4fjg3MkPW8wO3YdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی به نقل از سه منبع آگاه گزارش داد جنگنده اف-۱۵ای آمریکا که ماه گذشته در ایران سرنگون شد، احتمالا با یک موشک دوش‌پرتاب ساخت چین هدف قرار گرفته است.
به گفته یکی از این منابع و یک مقام آمریکایی آگاه، چین همچنین ممکن است در روزهای نخست درگیری، یک رادار هشداردهنده دوربرد را در اختیار ایران قرار داده باشد که این رادار توانایی شناسایی هواپیماهای رادارگریز را دارد.
ان‌بی‌سی نوشت مقام‌های آمریکایی همچنان در حال بررسی سرنگونی جنگنده اف-۱۵ای هستند و هنوز روشن نیست تجهیزات نظامی احتمالی چه زمانی به تهران تحویل داده شده است.
کاخ سفید به ان‌بی‌سی گفت شی جین‌پینگ به ترامپ اطمینان داده پکن تجهیزات نظامی به ایران نمی‌دهد. سخنگوی سفارت چین در واشینگتن نیز گفت پکن صادرات نظامی را «با احتیاط و مسئولیت‌پذیری» کنترل می‌کند و با «تهمت بی‌اساس» مخالف است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/75800" target="_blank">📅 07:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZlyWABmLQTXrN-kzCpB1do4LOrdxlP1xExx6L8cy6ALtR7PmAGIeNYK06i_mqxIDSJmaOgaTcWQdiqEMSrAXaDx5haNSk1E449omSBR9IbME4SDVzKH150-UsLHZb3H81CCND76qUVK5cGBne9vw_P_NSM6ElsuqJiyG6qTdGRy7aFOebrsaUdqupXnIS4cMT7LLgKya5N5f06x_N3bSfHVfVs6O6Tb5RvpO1SBbRVhjcYq_2q5LUpBjKdyvCjKt5qUC7gA481TyPi3KJPiieqLvVc_UedjIz_5JlTKZyKCPQ_Xsqy_UuiRL9sghC7GZjTT09e70yQ5PhjfvvGM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'به جای پول نقد قطر موافقت کرده ۶ میلیارد دلار  اعتبار در اختیار تهران قرار بگیرد تا کالاها و محصولات اساسی را از قطر خریداری کند'
یک منبع آگاه از روند مذاکرات به ایران‌اینترنشنال گفت سفر قالیباف به قطر به شکستی دیپلماتیک منجر شد و با وجود درخواست تهران برای آزادسازی فوری و بی‌قید و شرط ۱۲ میلیارد دلار به صورت نقدی همزمان با امضای یک یادداشت تفاهم اولیه با آمریکا، مقام‌های قطری این درخواست را رد کردند.
به گفته این منبع، مقام‌های قطری تنها با آزادسازی نیمی از این مبلغ تحت محدودیت‌های سخت‌گیرانه موافقت کردند.
بر اساس گفته‌های یک منبع نزدیک به یک مقام قطری حاضر در این گفت‌وگوها، دوحه از انتقال مستقیم یا نقدی این منابع به ایران خودداری کرده است. در عوض، این پول تنها به صورت اعتبار در اختیار تهران قرار می‌گیرد تا کالاها و محصولات اساسی را مستقیما از قطر خریداری کند.
این محدودیت در شرایطی اعمال شده که آمریکا به شدت با اعطای دسترسی مستقیم و بدون محدودیت جمهوری اسلامی به دارایی‌های نقدی مخالفت کرده است.
آمریکا ابراز نگرانی کرده است که تزریق مستقیم پول نقد می‌تواند برای تهران فضای تنفسی اقتصادی حیاتی ایجاد کند و به آن اجازه دهد حقوق‌های معوقه بخش عمومی را پرداخت کرده و در دوره‌ای از تنش شدید منطقه‌ای، تجهیزات نظامی را از کشورهای دیگر تامین کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/75799" target="_blank">📅 03:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=Fq02m9DtKBCmGU4Q-6YFGsgASkcuMHM07YkOWJIbMHYsgBE5u53-eYml79jXKlLAf0t_3fqbiJY0KmbXl020wYct9rnAiQG2SSV4e0YUt-Ho1bk4dsVwpogDaHTBpn_cLeyY9yiLtdJ9Oxxi9pBtIa4UpsOk_Rfk0ZT5OSGwGCn07T7zd6dDLGyNTNcib-wiYeGHxvo-EpAs08CFDvrI4sy6oDzqbbK6bigKkAEuCteABDX4qCVsqBrUdf1SGbtM9vTZia_t1DklBfGzSHs7JPc-K_dLgcKMMNVz5OUsarLra7NtahGOKrrLJEvh46erKrHgLD0aUwuSomRYzjXKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=Fq02m9DtKBCmGU4Q-6YFGsgASkcuMHM07YkOWJIbMHYsgBE5u53-eYml79jXKlLAf0t_3fqbiJY0KmbXl020wYct9rnAiQG2SSV4e0YUt-Ho1bk4dsVwpogDaHTBpn_cLeyY9yiLtdJ9Oxxi9pBtIa4UpsOk_Rfk0ZT5OSGwGCn07T7zd6dDLGyNTNcib-wiYeGHxvo-EpAs08CFDvrI4sy6oDzqbbK6bigKkAEuCteABDX4qCVsqBrUdf1SGbtM9vTZia_t1DklBfGzSHs7JPc-K_dLgcKMMNVz5OUsarLra7NtahGOKrrLJEvh46erKrHgLD0aUwuSomRYzjXKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، بامداد شنبه ۹ خرداد با انتشار تصاویری مدعی شد بقایای یک پهپاد متعلق به آمریکا و اسرائیل که در حوالی قشم هدف قرار گرفته، کشف شده است.
تسنیم بیان کرد این پهپاد با واکنش پدافند هوایی ارتش هدف قرار گرفت و منهدم شد.
پیش از این خبرگزاری مهر به نقل از منابع محلی گزارش داد یک ریزپرنده در حوالی قشم از سوی پدافند هوایی هدف قرار گرفته و منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/75798" target="_blank">📅 02:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SUgb6X5kklgodnh_cXT94HzRAEBcoYHjOALDZ9ZYX5FSlE7jEp0aciz_z6zv-bwxZMrjX1PyY-lqTBtwOom_0LV7t2MTlfui61Ei0knzvOgDjE11ZX2X6mTaNExo6lAMgwZRtr1cUmBFF3X3-9j98Q2oGCTtaU6Wm2EBPbPchZSYxoWYdHjm61IQX_S5jrHDHccMxIzGrVZ7mkXU6PMkan-oB_5iQGHeuCxbFpG3Uc_l41o8RGIajm7h42o18_8sfs7ZM2lOpbLoUTKYlugr1Z1JE1khzipHX631vUPjbWk0mV1tBmxyJEI0_WIYZsJ3KxX3obAg1H6U8nUit0C3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌پست، یکی از آخرین موارد اختلاف بر سر راه توافق احتمالی میان واشینگتن و تهران، چگونگی آزادسازی مرحله‌ای دارایی‌های ایران است که در قطر نگهداری می‌شود و برای اهداف بشردوستانه در نظر گرفته شده است.
بر اساس این گزارش، منابع مالی مورد بحث مستقیما در اختیار حکومت ایران قرار نخواهد گرفت، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده می‌شود و سپس این اقلام به ایران ارسال خواهد شد.
نیویورک‌پست به نقل از یک مقام دولت آمریکا نوشت پرداخت تدریجی این منابع به اجرای تعهدات از سوی ایران، از جمله بازگشایی تنگه هرمز و پاکسازی مین‌ها در تنگه هرمز، وابسته خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/75797" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=Nj-w_vDkKOP8-dGX1VHf4rS5vtHsnt0FCtNtZAVIFOPzpEhZ_HZqS4l-iG8MCjQQPR5d_nxEZIHObAx27NLGKYjJoZFrPLcFQJwqNHAaBOHWCeTWOY31SA4cVhnWSKE2ohVvJNPQLMQkBm8R_EZ5SxWav7D-yeUtt90rELwpKFDo5oTqW6m_4nZKZVLa8DC7EU2xQrzS15ZuoUEnfO093ld7Ys3JFV-6ANyFMumoDFeUsYBrLONdNjFp32-0HW-OnTzWikHAQGpBpD6z8pbgTc9BDI3a7JloOoqOd_bu7NPgbVkE-SNAar8tAP17et-lRUw1vi3UCYnajX6w2xH01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=Nj-w_vDkKOP8-dGX1VHf4rS5vtHsnt0FCtNtZAVIFOPzpEhZ_HZqS4l-iG8MCjQQPR5d_nxEZIHObAx27NLGKYjJoZFrPLcFQJwqNHAaBOHWCeTWOY31SA4cVhnWSKE2ohVvJNPQLMQkBm8R_EZ5SxWav7D-yeUtt90rELwpKFDo5oTqW6m_4nZKZVLa8DC7EU2xQrzS15ZuoUEnfO093ld7Ys3JFV-6ANyFMumoDFeUsYBrLONdNjFp32-0HW-OnTzWikHAQGpBpD6z8pbgTc9BDI3a7JloOoqOd_bu7NPgbVkE-SNAar8tAP17et-lRUw1vi3UCYnajX6w2xH01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز جمعه هشتم خرداد در «مجمع اقتصادی ملی ریگان» اعلام کرد که واشنگتن حدود یک میلیارد دلار از دارایی‌های رمزارزی مرتبط با حکومت ایران را به طور مستقیم توقیف و کیف‌پول‌های دیجیتال آن‌ها را ضبط کرده است.
او با تاکید بر اینکه این اموال در واقع پول‌های دزدیده‌شده از مردم ایران است، اشاره کرد که بسیاری از صاحبان این حساب‌ها هنوز متوجه ضبط دارایی و کیف‌پول دیجیتال خود نشده‌اند.
وزیر خزانه‌داری آمریکا همچنین افزود واشنگتن با همکاری نزدیک متحدان اروپایی خود در حال ردیابی و توقیف املاک و مستغلات، از جمله ویلاها و خانه‌های متعلق به این افراد در سراسر اروپا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/75796" target="_blank">📅 23:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4nz71ML5qFNAcdVlAnZJGr4aj_RWWM4oXJcWVsIzRdV16lqbUziIXrPYH9k0kfCN-QaBO-X_1BJ-TeMaQIAoudElytYCv8g1BBXey7EBg4n3xYD2TFGIc48HK6W05y6AMTb2wmQh80Z0x2b1u1YKS1nX7f5oZ2amLX9kWv-QZJ_uivcUUHk9Q2HAzg2dPSW4kNHnEA-AOGiIT_r3LZZXTxk_somCphCgV4UtLjhhhTKOiA61_VFB3883oxlSEQ3DeevysVyALd9EDF-k6RfasDYPOVLhv-n4Dga1N37bbonWscNcvKgRTs5IyXWrM_LuP9FObGVizlR642erVyQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از یک مقام ارشد آمریکایی گزارش داد نشست دونالد ترامپ در «اتاق وضعیت» کاخ سفید دو ساعت به طول انجامید، اما رییس‌جمهور آمریکا هنوز درباره هیچ توافق جدیدی با تهران به تصمیم نهایی نرسیده است.
این مقام افزود دولت آمریکا معتقد است به دستیابی به توافق نزدیک شده، اما برخی مسائل از جمله آزادسازی دارایی‌های مسدودشده همچنان محل بررسی و اختلاف‌نظر است.
@
VahidOOnLine
یک مقام ارشد به خبرگزاری آسوشیتدپرس گفت که این جلسه در حال بررسی چارچوب توافقی بود که آتش‌بس را به مدت ۶۰ روز تمدید می‌کرد و مذاکرات در مورد برنامه هسته‌ای ایران را پیش می‌برد.
این مقام رسمی در مورد اینکه آیا ترامپ پس از این جلسه تقریباً دو ساعته تصمیمی برای پذیرش این توافق اولیه گرفته است یا خیر، اظهار نظری نکرد.
sky
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75795" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWgURMjQapmll8I_YY_VxDf-lawA0vMhjlbEDDFhwX74BpN_DmzyX6uQh9IHlib_RuprUQNwg2UETSCQZRYNbe-A-UhpfHLIh2j5_XQjV_zLn3f0oJ1CZyKfDmeEWipT59Ii_CxkdtpLAGDBWDn-UbMaJE7PbORJ6eL35W5IJOF-3n2qn-f7u40FC6Q703HanoXWItpeIu3Xv3j-vEDvmMebq69puu8RNDsEFuv02AN6cQW204nybz2g8Lo77YtoekCPpR8shILrODOMZSPgO3HEJhrwYp5G1tJ8xlB4SHYQY9KOyF3dFvywNCDk-qr40zTle9FNmVYy_6Lb5skaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال روز جمعه هشتم خرداد، در گزارشی اختصاصی به نقل از منابع آگاه فاش کرد که امارات متحده عربی در طول جنگ، ده‌ها حمله هوایی را علیه مواضعی در ایران انجام داده است.
منابع وال‌استریت ژورنال می‌گویند نقش امارات در این کارزار نظامی، «بسیار عمیق‌تر» از آنچه که پیش‌تر گزارش شده، بوده است.
بر اساس این گزارش، این حملات با هماهنگی کامل واشنگتن و تل‌آویو و با اتکا به اطلاعات ارائه‌شده از سوی آن‌ها انجام شده است.
اهداف امارات شامل جزایر قشم و ابوموسی در تنگه هرمز، بندرعباس، پالایشگاه نفت جزیره لاوان و مجتمع پتروشیمی عسلویه بوده است.
حملات به عسلویه که به صورت مشترک با اسرائیل و در پاسخ به ضربات جمهوری اسلامی به زیرساخت‌های انرژی امارات انجام شد، واکنش‌های شدید بین‌المللی را برانگیخت و واشنگتن را وادار کرد از اسرائیل بخواهد حمله به تاسیسات انرژی را متوقف کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/75794" target="_blank">📅 22:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#قشم
پیام‌های دریافتی درباره فعالیت پدافند:
سلام وحید
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
21:26 هشتم خرداد جزیره
#قشم
صدای توافق خیلی بلند به گوشمون رسید. حدود یک دقیقه صدای شدید پدافند، احتمالا برخورد موفق با پهباد نفوذی.
درود همین پنج دقیقه پیش پدافند قشم داشت شلیک می کرد درگیری بود
ساعت 21:25
همین الان پدافند قشم فعال شد و یک چیزی رو زد
🔄
آپدیت:
تسنیم: "در پی رصد ریزپرنده متخاصم دشمن آمریکایی ـ صهیونی در حوالی قشم توسط پدافند هوایی ارتش، بلافاصله در عملیات موفق مورد اصابت قرار گرفت و منهدم شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/75793" target="_blank">📅 21:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiEGLQudEzdQZKzLW6wVdcOH0iLQ02gM38cg0I3WiiduKk3q7IhZGcEfz2K6YIg4rPdDN3fuGBJbNCBcOkfmzXpowUhWsECvED6Je1SsLFbf_qi_xwrbst24_x4iVLPxoCKfBVD74xDIwzFtFMWw9sgUe9o6_a_m7uRhNdvKRTVKwShq-CCzcyFLWDSNmK8iFPdwqoHgKTrWPvmpVrqZuq6hixxxoNn2zPN8voAaYtLFNsBjjYqmqjC_OWhdYNF0EUSpo2-bH3JOeK37MseuFY_x_Bc6vQOh6vb1L1Gvul70yu3_tb6xGUwt2ab9De_c0Jq25vWQYwSg8AChLQ7eMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ پستی از نیوت گینگریچ، رییس پیشین مجلس نمایندگان آمریکا، را در تروث سوشال بازنشر کرد که در آن نوشته شده بود: پس از بررسی جنگ ایران در این هفته، متقاعد شدم ترامپ در آستانه یک پیروزی تاریخی قرار دارد
IranIntlbrk
پستی که گینگریچ ۸ ساعت پیش نوشته بود، ترجمه ماشین:
پس از آنکه این هفته را صرف بررسی جنگ ایران کردم، اکنون متقاعد شده‌ام که رئیس‌جمهور ترامپ در آستانه یک پیروزی تاریخی قرار دارد. نقطه عطف واقعی برای من زمانی رقم خورد که تصمیم‌ها و مانورهای رئیس‌جمهور ترامپ را نه از منظر یکجانبه‌گرایی آمریکا، بلکه از منظر رهبر یک ائتلاف تاریخی چشمگیر بررسی کردم؛ بزرگ‌ترین ائتلافی که تاکنون در خاورمیانه مدرن شکل گرفته است.
همه می‌دانند که اسرائیل متحد مهمی است. اما آنچه کمتر درباره آن صحبت می‌شود، عمق حمایت امارات متحده عربی، قطر، بحرین، عربستان سعودی و دیگر کشورهای منطقه است. برای دیکتاتوری ایران باید بسیار تأمل‌برانگیز باشد که دریابد حتی یک متحد ندارد که حاضر باشد محاصره دریایی آمریکا را به چالش بکشد. آرام‌آرام، به‌تدریج و با احتیاط، متحدان اروپایی ما نیز در حال صف‌آرایی برای کمک در خلیج فارس و تنگه هرمز هستند.
بخش بزرگی از مانورهای رئیس‌جمهور ترامپ علیه ایران زمانی معنا پیدا می‌کند که او را نه صرفاً یک رئیس‌جمهور یکجانبه‌گرای آمریکایی، بلکه رهبر یک ائتلاف ببینیم. من بخش زیادی از چند هفته گذشته را صرف بررسی گزینه‌های نظامی کردم؛ از جمله پیروزی در نبرد خلیج فارس و تنگه هرمز و، در صورت لزوم، استفاده از سطحی تکان‌دهنده و خردکننده از قدرت نظامی؛ مشابه آنچه رئیس‌جمهور نیکسون و وزیر خارجه کیسینجر در کریسمس ۱۹۷۲ علیه هانوی و هایفونگ به کار گرفتند؛ اقدامی که هر دو رهبر معتقد بودند ویتنام شمالی را به پذیرش آتش‌بس و آزادی اسرای آمریکایی متقاعد کرد.
اگر این یک کارزار یکجانبه آمریکایی بود، می‌توانستم با اشتیاق از یک کارزار نظامی تهاجمی‌تر حمایت کنم. اما در عین حال روشن است که چنین اقدامی ائتلاف را از هم می‌پاشاند، زیرا متحدان عرب ما متقاعدند که ایران هنوز می‌تواند خسارت عظیمی به میدان‌های نفتی و زیرساخت‌های آنان وارد کند. ائتلاف‌ها ذاتاً کندتر از کارزارهای یکجانبه عمل می‌کنند. با این حال، ائتلاف‌ها در نهایت قدرتی به‌مراتب بیشتر را وارد میدان می‌کنند.
من نیز مانند همه دیگران از سرعت گفت‌وگوها با این دیکتاتوری سرخورده‌ام؛ اما پس از بررسی توازن قوا و گزینه‌های در دسترس ائتلاف از یک سو، و دیکتاتوری مذهبیِ ایران از سوی دیگر، آماده‌ام بگویم که رهبری ائتلافیِ رئیس‌جمهور ترامپ ــ چیزی که تقریباً هیچ‌یک از منتقدان او نمی‌خواهند به آن اذعان کنند ــ در آستانه دستیابی به یک پیروزی عظیم تاریخی است.
و اگر دیکتاتوری ایران در نهایت ثابت کند که به شکلی نومیدانه به موضعی انتحاری پایبند است، زمان کافی برای یک کارزار نظامی با قدرت و اثربخشی عظیم وجود خواهد داشت. در هر صورت، ما در آستانه یک پیروزی شگفت‌انگیز برای ارزش‌های خود و برای خاورمیانه‌ای امن‌تر قرار داریم.
NewtGingrich
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75792" target="_blank">📅 21:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHGsjv-DOTWEoBn8bqK5FaeLuvtPn9Lz3lwBN6o6twfWYMlYOkLvKqH6M0I1k1eU-OlmxP9eGjjBQL-b0_aXNjns3xVS9HlcNFDmYJn2jyCeW2fZdzWxSDjCx-b0CC0YYqrV8yOLIf93a8bwl5WO1uzG3d6_uWv_Cl3Yom3zL23r0AYDBvlpxf3n2WVLTLtgqpdg-bYqQBid6e9kkv4HovVjvJPdVH8ErVFAd4jymczPPNsd86vdu5k22coC4eBu1C-9A6wTf3Rj4QgJxnE1IXZ-KZeiip3fqlcIIlXDRhhEcZDbHtBjjbi26hgEfAt2xoEHla9SI03WGTiX_Xe-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی خانعلی‌زاده، عضو تیم رسانه‌ای هیات مذاکره‌کننده جمهوری اسلامی، نوشت که در متن تفاهم احتمالی هشت بند از ۱۰ بند بیانیه شورای عالی امنیت ملی که به تایید مجتبی خامنه‌ای رسیده، رعایت نشده و زیر پا گذاشته شده است.
او افزود که تفاهم‌نامه کنونی برخلاف بیانیه آتش‌بس شورای عالی امنیت ملی است و مشخص شده که اساسا مذاکرات پسااسلام‌آباد، بر مبنای شروط رهبری انجام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75791" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A36hmp98ngs21sM-7apmcUI6bkD-DSy6z-hwIPQi6grtn_61wSwoJQCdJ-_O1ro6Bao08ERQag19eesZ7T-F82CmG2bynRcztRFXndquwlBsPkKX3BHOD8-Gc8sAwjry61vEbiIrcQNsxCaXNdBmdt7v7yRAt4tE7aW37aFC874tHY5FncA0SNahUw6TUSxMDfAl__xzBs4b-f98mR3t8mCwGgHhEDJm5fIn9nUJyIkcAgxvdAhrzuZFX_4jEID1f9mKINxXy8X1qLOP-m3VPvIcvoC85pQZKFYsWr2DmKxyGCqex53qRLrPCWxUVytUWQCXKKKIrk4m1GpM2cY_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه ایران در مصاحبه‌ای با صدا و سیما گفت که تبادل پیام‌ها ادامه دارد ولی هنوز هیچ توافقی نهایی نشده است و افزود که مدیریت تنگه هرمز باید توسط ایران و عمان تعیین شود.
او بار دیگر گفت: «در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد پرونده هسته‌ای هیچ مذاکره‌ای نداریم.»
این اظهارات در حالی از سوی ایران مطرح شده که آقای ترامپ فهرستی از خواسته‌هایی را که می‌گوید ایران باید برآورده کند، مطرح کرد که شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای، باز کردن تنگه هرمز بدون دریافت عوارض، مین‌روبی کامل این آبراه و خارج‌سازی ذخایر اورانیوم ‌غنی‌شده ایران با همکاری آمریکا و تحت نظارت آژانس و سپس از بین بردن این مواد است.
@
VahidHeadline
پیش‌تر: خبرگزاری فارس، نزدیک به سپاه پاسداران، نیز به نقل از یک منبع ایرانی دیگر اظهارنظر رئیس‌جمهور ایالات منحده دربارهٔ توافق احتمالی با ایران، را «آمیخته‌ای از راست و دروغ» خوانده است.
این منبع گفته که در متن توافق بندی درباره باز شدن تنگه هرمز بدون دریافت عوارض وجود ندارد و تفاهم بر سر نابودی دخایر اورانیوم ایران را نیز «بی‌اساس» دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75790" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PeqGHMp5Ik58owfoJ07AFhizoJVK9oSHUApnvm35RFwpnJmkDo-8WQDRsG-8Rnk00Epb_nLHhc4WI_8K6Fp-TjM1jA-yC-MUXhtcXGWQ2MhbokBArBJtjW_vv8RJxbfBzkWkqRzM5NUGJRdryVLCH8x7-LQOVjMUf6pqyev-qq1lAhRYwK9n1Y_tjB4NqUQaalyod6HZdHjgC5ljthMoAP2L71ibd6_aAVcPPrPEC5du9HKBtcoQ6RtxhJYYYtBSfeD9K0_9XfFRmCwEobkhszjigbZC6VAhe_TtEX8E7yI75mzidtaKPZYRe0TUWjRwUR9PdBDfxA7tqIJeg_nP3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
پست ترامپ، ترجمه ماشین:
ایران باید بپذیرد که هرگز سلاح یا بمب هسته‌ای نخواهد داشت.
تنگه هرمز باید فوراً، بدون عوارض، برای عبور و مرور آزادانه کشتی‌ها در هر دو جهت باز شود. همه مین‌های دریایی، اگر وجود داشته باشند، برچیده خواهند شد؛ ما با مین‌روب‌های زیرآبی فوق‌العاده خود، شمار زیادی از این مین‌ها را از طریق انفجار از بین برده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده‌ای را، که تعدادشان زیاد نخواهد بود، جمع‌آوری یا منفجر کند.
کشتی‌هایی که به‌دلیل محاصره دریایی شگفت‌انگیز و بی‌سابقه ما در تنگه گرفتار شده بودند ــ
❗️
محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدران، مادران و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده، که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده؛ در حالی که کوه‌هایی که عملاً بر اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فرو ریخته‌اند روی آن قرار دارند،
❗️
توسط ایالات متحده از زیر خاک بیرون آورده خواهد شد؛ کشوری که، طبق توافق، تنها کشور در کنار چین است که توان مکانیکی انجام چنین کاری را دارد.
این کار با هماهنگی و همکاری نزدیک با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و سپس این مواد نابود خواهد شد.
❗️
تا اطلاع ثانوی، هیچ پولی رد و بدل نخواهد شد.
درباره موارد دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
💥
اکنون در اتاق وضعیت جلسه خواهم داشت تا تصمیم نهایی را بگیرم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/75789" target="_blank">📅 18:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=bxIRZjVFAw2woIy79FoRwymT5JE9lg31yEzKRfbsZ5p1nuB5auNTchoQEAsemFNF25LLcyLQKcPzfu1cpJ3t2ivqXPoZ8gr8jF2B1kQNEP7IV-JCXHFxeKFsVNwCLG_9Vpp6PFYO5gE49FD3RuVfFkc9Kxc-SSqkwF5U_M8hbUo2zNHclq5mAbLbvpjaRc56PtOtPiLfz9uXj1K87Np-fDPxg7KtbGi0sbIswmc8JOw0WZGRD4q336F2QoqyRs4GZNWOWl5IQMKcHare-yUSVu8ZJZstgVqaKGddb6K2zTOOFT_GXCWWhrmNmxvpPkw7btlVwtyUwOmjR-OYfACW-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=bxIRZjVFAw2woIy79FoRwymT5JE9lg31yEzKRfbsZ5p1nuB5auNTchoQEAsemFNF25LLcyLQKcPzfu1cpJ3t2ivqXPoZ8gr8jF2B1kQNEP7IV-JCXHFxeKFsVNwCLG_9Vpp6PFYO5gE49FD3RuVfFkc9Kxc-SSqkwF5U_M8hbUo2zNHclq5mAbLbvpjaRc56PtOtPiLfz9uXj1K87Np-fDPxg7KtbGi0sbIswmc8JOw0WZGRD4q336F2QoqyRs4GZNWOWl5IQMKcHare-yUSVu8ZJZstgVqaKGddb6K2zTOOFT_GXCWWhrmNmxvpPkw7btlVwtyUwOmjR-OYfACW-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با شرح عبور موشک‌های تاماهاک در مرز عراق و ایران در شبکه‌های اجتماعی و چند رسانه منتشر شده و گفته می‌شود مربوط به روزهای نخست جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75788" target="_blank">📅 17:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=DeSiYeQrxRpCjKVw0wliGZJCIL8dsA3YyZH8n6wASUvrt-Ube6DBSf2DBw99w6fkEF2EMb1U4va5VyNH5h20xy-PLHKTLiyd3qFGGAt8L133HnxUh_G-qNJFBiEYIf3g3p7lQyU9dztdfFfiPckL4E6QRpSdtcHOzX2V-Ta7kHAKqywATHR44u2Vr597mloTpluMIUxxrSk25K11U_5k8QZT4gb1jwB0mPfbp92NWv2DZbFe2UO5rcO7r-9FUGioGoguZT8QSKOBhHSSa1P3s6VXqtxGbS8QPfmO8Ccdf6ys4faZSmyqIljvt5ByYcnUicMvaCIwOvZ4lAgAhRnqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=DeSiYeQrxRpCjKVw0wliGZJCIL8dsA3YyZH8n6wASUvrt-Ube6DBSf2DBw99w6fkEF2EMb1U4va5VyNH5h20xy-PLHKTLiyd3qFGGAt8L133HnxUh_G-qNJFBiEYIf3g3p7lQyU9dztdfFfiPckL4E6QRpSdtcHOzX2V-Ta7kHAKqywATHR44u2Vr597mloTpluMIUxxrSk25K11U_5k8QZT4gb1jwB0mPfbp92NWv2DZbFe2UO5rcO7r-9FUGioGoguZT8QSKOBhHSSa1P3s6VXqtxGbS8QPfmO8Ccdf6ys4faZSmyqIljvt5ByYcnUicMvaCIwOvZ4lAgAhRnqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه هفتم خرداد ماه اعلام کرد عمان پس از دریافت هشدار واشنگتن درباره پیامدهای احتمالی مشارکت در طرح دریافت عوارض از کشتی‌های عبوری از تنگه هرمز، به آمریکا اطمینان داده است که برنامه‌ای برای اجرای چنین طرحی ندارد.
بسنت روز پنجشنبه در نشست خبری کاخ سفید گفت که صبح همان روز با سفیر عمان گفتگو کرده و از او شنیده است که مسقط هیچ برنامه‌ای برای دریافت عوارض در تنگه هرمز ندارد.
او افزود: «به او گفتم این موضوع از اساس غیرقابل قبول است و او نیز نمی‌خواهد افراد عمانی یا موسسات مالی عمانی را در معرض خطر تحریم قرار دهد.»
بسنت ساعاتی پیش‌تر در پیامی در شبکه اجتماعی ایکس هشدار داده بود که وزارت خزانه‌داری آمریکا هر فرد یا نهادی را که به‌صورت مستقیم یا غیرمستقیم در تسهیل دریافت عوارض در تنگه هرمز نقش داشته باشد، هدف تحریم قرار خواهد داد. او تصریح کرده بود که هر شریک احتمالی این طرح نیز با مجازات و تحریم روبه‌رو خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75787" target="_blank">📅 17:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDkfluRrCHxB-A5CHrn08ZI_amIwunsjj_6hTutbfWkpcVKd8nBFM3l785Og3QMbD_1Rilk0oWPM-0tllOEpfAM03XPp11LB_KKoHzF7GnDyb9DTGMCI8CJ7goNuxJB1d1lXhR36-S7BjGzlxPh7cbH2DKm_UM0KfvA2dAq0hvowSmhLyfrjVU59t3tEFirtGNiG20fBXitSEM0r_-_CEp79cw_VRu3vWZp8lBQZnhF2brlpsAPfzLuPeNVGVcyhHvqOpUz0oZPwuHkwSyBfsJ3naYADa0np8boZVumOv5JBJqbNBjKOApzLtV_sC4m5HOX8LlU3BEfvD6OQekh73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
به گفته این منابع، بسیاری از نکات مرتبط با برنامه هسته‌ای جمهوری اسلامی در مذاکرات جاری حل‌وفصل شده است.
بر اساس این گزارش، جمهوری اسلامی با نظارت بین‌المللی بر تاسیسات هسته‌ای خود برای جلوگیری از تعطیل‌شدن آن‌ها موافقت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75786" target="_blank">📅 17:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Db2nfI-Zs9bW_5BJXIjPiUTuQ7KQc9Og6NxaqjhHetFVOwYq_my1F05JudSN0kUBUQ7p5uRRwfPdkGv53U3MweQ51Z_ehCvKNOfVMru6XLyyO9rMmHVwVlp7qF6r0GUQMAICFHfP2JfuJmCQqsQyzmCAfv_x81E_adheO6R90y7fvtQbcwXyYK2P7LmBM-ix1fgEox5ZjZ-I1_AJxBKr9kXVQSkLNmsiPsh8OAs3Zw5y4Socrd956-lTnczyM14j2f9L_mkT8wKwAGbI3V4Ga1-T2acPN7drjBeA27EOHxSgtwGp2-4waLO2X_KLA9S9koBJr5JVo989o_Hn0E2Ygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی با آمریکا، روز جمعه تهدید کرد که تهران امتیازات مورد نظر خود در توافق پایان دادن به جنگ را با «موشک» می‌گیرد و پیش از اقدام واشینگتن درباره این توافق اقدامی نخواهد کرد.
او در شبکه ایکس همچنین نوشت: «هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است.»
این موضع‌گیری یک روز پس از آن انجام شد که چند رسانه غربی خبر دادند آمریکا و ایران به تفاهمی برای تمدید آتش‌بس و رفع محدودیت عبور و مرور کشتی‌ها در تنگه هرمز رسیده‌اند، اما این توافق منتظر تصمیم و امضای نهایی دونالد ترامپ، رئیس‌جمهور ایالات متحده است.
قالیباف در پیام خود اعلام کرده که «اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد».
از سوی دیگر، رسانه‌های نزدیک به سپاه پاسداران می‌گویند گزارش‌ها درباره توافق تهران و واشنگتن صحیح نیست. خبرگزاری تسنیم در این مورد به نقل از یک «منبع مطلع» نوشت: «متن توافق تا این لحظه جمع‌بندی نهایی نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75785" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoNOvgzvpNhBn2f_Rf0HYWzJ4ocYwa72Dh5NoOFxUdE3A0GQnYCLfDfIesprLZw7mNHDYC43ruXPrJ69Bi8kL2BhJEK5dz-8Kz_ICUzgT-LLuCJ0lTIUHF3s9jUOMq1jEEOLr788vX4KSYN7ZFIBZLMFVyIw-io6bB-TL3KNKjK9N4C07aDK6oEuUt7kJzU46XdX1j_SyqIXX6_gqtgJTtfkOhDKGvx5HFQQgGS0lYTYmfCH2YngOIEyRCav67TL2dI0Xc_FtL7wDOS5ktD3v4cI9Y3me4JiJHqsJCcuSdX6fMq8Yr5F3VYJtM8SZl41CbLhL6Aj9gOMGwjaJZXEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از ابتدای سال جاری تاکنون، اجرای ۶۶۰ مورد اعدام توسط جمهوری اسلامی را مستند کرده است. با این حال، به دلیل ماهیت پنهان‌کاری و غیرشفاف بودن سیستم قضایی ایران، آمار واقعی به احتمال زیاد بسیار بیشتر از این رقم است.
‏
🔸
از زمان آغاز جنگ، آمار اعدام معترضان و افرادی که به جاسوسی و اتهامات مشابه علیه امنیت ملی متهم شده‌اند، با سرعتی نگران‌کننده افزایش یافته است. «اعترافات اجباری»  قربانیان، اصلی‌ترین «مدرک» مورد استفاده در این احکام مرگبار بوده است.
‏
🔸
این اعترافات در شرایطی کاملا مبهم و تحت فشارهای شدید جسمی و روحی اخذ می‌شوند. جمهوری اسلامی به طور مستمر این اعترافات اجباری را در رسانه‌های دولتی پخش می‌کند تا از آن به عنوان ابزاری برای توجیه اعدام‌ها و سرکوب مخالفت‌های عمومی استفاده کند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75784" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t94W4h8uQnXXbT5ffddfu3J29KOnDWudPRKrzgaGyUdrweqwazFSwb_jfoeWvhyUuCgD7CDmG5TE0ueReDzcMOVRIDzWhqeN2HehADr07CjBaoiO5EO6r_iy9FFA8PCBSeMQ5ug4Iby2RLknGgbq5vUjaNMAxI2TpEz6HwuweB7dMtm3dZRP2htJELd9vypaiKdjEQVoV5xhjQMrUKIdF7Lj6E88UT8_G6-A5XTzRmoYuW4-FJ0xhgxOrSuy61dNb2PgwHRmqKYlkNyJqLeytSRakI7YYs2NHg71Ir9CTHIvkpdgu8GPE_4XrlZaXYwltmeaHhQsanVfKj-MudDwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
شیخ تمیم بن حمد آل ثانی، امیر قطر، در تماسی تلفنی با دونالد ترامپ، رئیس جمهور آمریکا، در مورد تحولات منطقه‌ای گفتگو کرد.
دفتر امیر قطر در گزارشی از این مکالمه تلفنی اعلام کرد که شیخ تمیم بر اهمیت اولویت دادن به راه‌حل‌های دیپلماتیک و گفت‌وگو بین همه طرف‌ها به امید جلوگیری از تنش‌ها و تشدید بیشتر در خاورمیانه تأکید کرد.
در این بیانیه آمده است که ترامپ نیز به نوبه خود از نقش قطر در حمایت از تلاش‌های میانجیگری پاکستان بین واشنگتن و تهران قدردانی کرد و «از تلاش‌های قطر برای رفع اختلافات و ترویج کاهش تنش در منطقه» تمجید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/75783" target="_blank">📅 02:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=Qg1M6Q5UyJ57tDjnfwIhJv9L_Xh-gl93b4SM0Svexz-n72AAbmxBkpXyxHY3bMz5-kF4OsQpJEoLcYtsOyaBvdNUMiDS04B-vmYSj3XHek_EEJBzFFmBOGu0tJZ7sRyOXjemlyx1v_3K0O6F9AnB6tLUl1DQYEmiwyDIOBXx7PIMbTy73BD66ku7W8ZR5TSpmTaYAtcTgg12qTtTLbFuBc0yUS_FWMBdAOYRjD4-5YJzoYKrQupF5Yp1W6fxttrAQjV4CReTyfsPJcbCTXFSc0y6hmOhOYIC2TXZcepD1KFbxM9-o_ZljnmRh5-56ZMKkuU5I-v_REXyIAlAioCo3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=Qg1M6Q5UyJ57tDjnfwIhJv9L_Xh-gl93b4SM0Svexz-n72AAbmxBkpXyxHY3bMz5-kF4OsQpJEoLcYtsOyaBvdNUMiDS04B-vmYSj3XHek_EEJBzFFmBOGu0tJZ7sRyOXjemlyx1v_3K0O6F9AnB6tLUl1DQYEmiwyDIOBXx7PIMbTy73BD66ku7W8ZR5TSpmTaYAtcTgg12qTtTLbFuBc0yUS_FWMBdAOYRjD4-5YJzoYKrQupF5Yp1W6fxttrAQjV4CReTyfsPJcbCTXFSc0y6hmOhOYIC2TXZcepD1KFbxM9-o_ZljnmRh5-56ZMKkuU5I-v_REXyIAlAioCo3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: جی‌دی ونس می‌گوید ایالات متحده در مذاکرات با ایران «پیشرفت زیادی» داشته و معتقد است تهران «حداقل تا حالا با حسن نیت در حال مذاکره است.»
جی‌دی ونس: خب، فکر می‌کنم گفتن دقیق اینکه رئیس‌جمهور دقیقاً چه زمانی یا اصلاً  تفاهم‌نامه را امضا خواهد کرد، سخت است. ما در حال رفت‌وآمد بر سر چند نکتهٔ زبانی هستیم.
کاملاً واضح است که به نظر من، ایرانی‌ها — آنها یک معامله می‌خواهند. آنها می‌خواهند تنگهٔ هرمز را باز کنند. ما هم می‌خواهیم تنگهٔ هرمز را باز کنیم.
🔸
چند مسئله در مورد موضوع هسته‌ای وجود دارد: ذخیرهٔ اورانیوم غنی‌شدهٔ بالا و همچنین مسئلهٔ غنی‌سازی.
پس می‌دانید، ما با آنها در حال چانه‌زنی و رفت‌وآمد هستیم. ما واقعاً فکر می‌کنیم آنها حداقل تا حالا با حسن نیت مذاکره می‌کنند.
داریم پیشرفت می‌کنیم و امیدواریم به این پیشرفت ادامه دهیم تا رئیس‌جمهور در موقعیتی قرار بگیرد که بتواند توافق را تأیید کند.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/75782" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3wlRsAqD8QPXjYah7oddYwA0P9otT_dFpJgO0kWWh4eMpDQj7peNkwIEwN5zIPzXjbdBOaShLOZ29k8M4xkZtdQUXg8YoiyiwvgRVA-DcvEY_7RaCkuTWXiQCMrks-VDCF1UQCObbKP4xfCDdGNkp_MlzQVOrdflroZfvH4Nnz1obE0g9fPKbi-gJBSfxFbuqbyTjypL4dgUVUxDq-GxHUyxoX381L1BRua-CYXWizA3gOiR51YzUCFZatUc2kx8PsFzSLdMIi4T5CA-uA6uGyFxVBmX_vo5UTiYMIvjoW7bLRcWWYrdUl1SjpoMvo6JeEg6TnvxBmwerIt-dMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که نیروی دریایی سپاه شامگاه پنج‌شنبه در نزدیکی تنگه هرمز به ۴ «شناور خاطی» که قصد عبور بدون هماهنگی از تنگه هرمز را داشتند، «شلیک اخطار» کرده است.
همزمان، گزارش‌های منتشرشده در رسانه‌های اجتماعی از شنیده‌شدن صدای انفجار در هرمزگان و بوشهر حکایت دارد.
@
VahidOOnLine
ساعتی پیش پیامی دریافت کرده بودم که در پست قبلی نقلش کرده بودم و الان به اینجا منتقلش کردم. پیامی از شهروندی که درباره یکی از اعضای خانواده‌اش نوشته بود: الان قشم بود. پلاک موقت دادن بهشون گفتند فقط از جزیره خارج شید سریع
همزمان با خبر بالا هم پیام‌هایی داشتم:
صدای انفجارهایی در بندر عباس شنیده میشه.
صدای انفجار داره سمت قشم و دریا میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/75781" target="_blank">📅 23:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DiwXPIhKdexMCYaLW5Yu67M6tGi1uykXl1hE3KTZmnYKcMaFXV_F3YZVVvf6sW-s8KD8mtTgX05IPkQ146OnROlILydGF9zcTdvHRuyhYb3nIcXKmUOHXOws2RaMTEbF1v5bWRZG25FfpjKZ8TMdkGmYRkDHo_UKVlPA2Bmmzkhx1nCYcUNy6PqS7IByiCDBTlVewMnZZboQV795KmOxsJv4WNvZNS4Ogx2O4OvHsaMG8VSzIXR0jEQ0mWisdKM9EHiuM0JU5FHS-v-SVe5iDqbx7G9A83C6hZcB4_6qAgKddQ2VyMDVNDC7FnvpB-wkkIbsnADb5cmew4aZNY5BYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
#جم
در استان بوشهر
پیام‌های دریافتی درباره شنیده شدن صداهایی
:
▪️
همین االان 10/42دقیقه موشک از جم پرتاب شد
▪️
الان جم رو زدن...صدای انفجار زیاد ۲۲:۴۰
▪️
سلام آقا وحید
امشب ساعت ۱۰:۴۶ ۷ خرداد
بوشهر شهرستان جم نمیدونم صدای پرتاب موشک بود یا جنگنده ولی خونه ها لرزید
[معمولا این دو صدا با هم اشتباه گرفته میشن.]
▪️
درود بر وحید جان آنلاین از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
🔄
آپدیت:
مسعود تنگستانی، فرماندار جم، به خبرگزاری صدا و سیما گفت نیروهای مسلح جمهوری اسلامی «یک هواگرد» را در آسمان این شهرستان در استان بوشهر هدف قرار داده‌اند و اکنون وضعیت منطقه عادی است.
@
VahidOOnLine
یک مقام آمریکایی ادعای صداوسیمای جمهوری اسلامی درباره سرنگونی یک هواگرد آمریکا در استان بوشهر را رد کرد.
به گزارش رویترز، این مقام آمریکایی که نخواست نامش فاش شود، گفت هیچ هواگرد آمریکایی در نزدیکی بوشهر سرنگون نشده است.
@
VahidOOnLine
آپدیت: تصویر بالا
به صور رسمی هم از طریق
سنتکام
تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/75780" target="_blank">📅 22:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM31vx-UI9gXtYlaeEBKhKm9QgH9AxfZLg2w-tWD-8F0QcXCRi_YfuK3mjvaHd82vhx0pN1T_OX1lwhoWOm0BilP7mOM06tBSlcsJ68n0uXVapuh018Nxb1wNkGSiH2NyEIzPi5Ck_BCrSwe9vUD1Rjuyv-8LIzxSXIek7wGge99RB362AkZ1U-MTkhHisL-J21jkaaTvrvx-RhiaoaXtWhNdP4a0vlijm7md5WtaopQxjw_IkDfhoTb4q0Pdg8jgYdzx21pZ_VDSO3t_jyqLy4DfmETTJoo0T1jBqZsrbDhGpRxX6vuF0cPfYhXfWAs2lnwXt-CvO7I7WN1HU-BMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارگان خبری مجموعه فعالان حقوق بشر در ایران خبر داد که تارا و کیمیا داوودی، دو خواهر محبوس در زندان اوین، توسط شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی در مجموع به ۱۶ سال حبس محکوم شده‌اند.
براساس این گزارش، کیمیا داوودی به اتهاماتی از جمله «ارتباط با گروه‌ها و شبکه‌های معاند» و «اجتماع و تبانی علیه امنیت کشور» به ۱۰ سال زندان و تارا داوودی نیز به اتهاماتی شامل «اجتماع و تبانی علیه امنیت کشور» و «تبلیغ علیه نظام» به شش سال حبس محکوم شده است.
این دو خواهر در تاریخ ۲۴ دی‌ماه ۱۴۰۴ در جریان اعتراضات سراسری در تهران بازداشت شدند و هم‌اکنون در بند زنان زندان اوین نگهداری می‌شوند. به گفته منابع حقوق بشری، بازداشت آن‌ها با خشونت نیروهای امنیتی همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/75779" target="_blank">📅 19:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVwooQn7D8OVJKQfFCtJ0Z6kPSsEqAVNQ4YugV1cy5cjoq5pSaphOMQwX83aC6qRMsZDVcW8I9xzaQ3ztW485DSGY9A14Gufnn2Ltk0TbD841KGkfFhjM6qGIivmJk4w7gsxLhXXUmVt1939gbN0dY7W0C3lhxuQm8JORvuV0aVHCo8VXFtqcHE3YnTb5_XruCWn95kQ4XxwubolxvvmtlD-_A5YFAAOeZ8MwMShswy8odkPLAz9-eSYLcvWQwj-nHfcWQutxOnscuha9asi2C-NV8Qblk_5MUsAzdAcBVWA2_dr3qaI-SzFbWO43ni8JqeMOA_wY4UPZwwVgm0bvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی گزارش داد که مذاکره‌کنندگان آمریکا و جمهوری اسلامی به یک یادداشت تفاهم با مدت ۶۰ روزه برای تمدید آتش‌بس و آغاز مذاکرات درباره برنامه هسته‌ای ایران رسیده‌اند، اما دونالد ترامپ، رییس‌جمهوری آمریکا، این متن را هنوز تایید نهایی نکرده است.
مقامات آمریکایی که نامشان فاش نشده به این رسانه گفتند که شرایط توافق تا سه‌شنبه تقریبا نهایی شده بود، اما هر دو طرف هنوز نیاز داشتند تایید مقامات ارشد خود را بگیرند.
مقامات آمریکایی افزودند که طرف ایرانی اعلام کرده که تاییدهای لازم را دریافت کرده و آماده امضا است.
تهران هنوز این موضوع را تایید نکرده است.
اکسیوس نوشت مذاکره‌کنندگان آمریکایی جزئیات توافق نهایی را به ترامپ گزارش دادند و او درخواست کرد چند روز برای فکر کردن زمان داشته باشد.
@
VahidOOnLine
بعدا
فاکس‌نیوز
هم خبر مشابهی منتشر کرد.
و گویا به همین دلیل هم می‌خواستند اینترنت را باز کنند. پیروزی جلوه دادن با اعلام جشن و پروپاگاندا در جو جام‌جهانی و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/75778" target="_blank">📅 19:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kQydgPE6jnDQAsgB4NE057AG4X0ctUT16mBaJXnxCrKUb2P9_oyb_x3AJ3dqQqKqEXEFdGTQBnbzUzyBgTZ9DDZRU7nZaGLQ_eETkAiZkXpqnePX9bo17D2d1lbwYfJnYzeXwXuCvKNFvitF4wAyluN4SpSX2RsaA3o7ZjBA78hjirSzsS2tv0fZ5JEdDF7FBW8j7T0srQzGeqRiqD4JWDcXtmqgjTjS7aee7YPkXOTMGVL8N9Nx0kABMAHdmmfHicbExS3yP9Wi4_qTQ5uatdgdpOTOg-28xoLymz4spO3clPgunA8abTD3isoRuVpjtCRwJ4j-DHleS3IvS_MENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v6Fkmr4jPKT9VDTTs4GpWLeZHNcFjr2R73gHROKC5c1ER41r5cgt6rJ5mw4o-5bNSPnhrFvBV5wHgroK5CVJSF0dIk7QTK97IRYSVHHG99lu06eL2ECvN69r6WlRt-sN1fDwiq4ONs6wBJoAxsvzx2iowr5c5gklQbizEF9Qwe4TX_1GYsBX6uy58QYswR9VPOpLlaSgocZCRIK1RJr22AaACYcWAT0jpC6aZVxqoex2hGWXIoPgXhAie0EHYVRyBrNic_YJwOjNAgn4IYkGSpWh56IGRbyLFCDnrxIXtOFPaXYEiQuLUqh7QW4DE8lvuolgc9dAWDiC1Di7gD25fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس از انتشار پیامی منسوب به مجتبی خامنه‌ای درباره «نابودی اسرائیل تا ۱۵ سال آینده»، رسانه‌های ایران تصویری از دیوارنگاره جدید در میدان فلسطین تهران منتشر کردند که بر آن جمله «اسرائیل ۱۵ سال آینده را نخواهد دید» نوشته شده است.
در پیام منتسب به مجتبی خامنه‌ای که رسانه‌های ایران آن را منتشر کرده بودند، آمده است اسرائیل «به مراحل پایانی عمر منحوس خود نزدیک شده است.» در این پیام به سخنان علی خامنه‌ای در سال ۱۳۹۴ اشاره شده و تاکید شده است که اسرائیل «۲۵ سال بعد از آن تاریخ را نخواهد دید.»
@
VahidOOnLine
سپاه پاسداران روز پنجشنبه هفتم خردادماه با انتشار بیانیه‌ای به مناسبت کشته شدن محمد عوده  و عزالدین حداد، دو فرمانده حماس اعلام کرد منطقه جز با محو اسرائیل روی آرامش نمی‌بیند.
سپاه در این بیانیه از حمایت جمهوری اسلامی از «محور مقاومت» تاکید کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75776" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JebR2eWYzpqgnm0Dufai5mN2XZS6LH742w8B9fmfCL8fIXVASI0OPouaHuR40Vm4yB2qXwSyqScQqhKLAcDcSSSkL2xU7gu2Png7tmezeLja7NO5JudfOy-SQq1qrknrU56OaQ2Ea16lOT4vw7NKp5K5yubGVielYVX7j7Dly77QBYJjkgwgxX9BH1a4eFrpzIDljivKnbleR4zMU4CS_lb9K2oj5JKeWOW4oGy-217v1C7jCaMXZ4a5MRuRtrJIwiK3fsCcO305QumqEVtUfgq7p95p4D2q1tO1qIysg1OyeWo3My6budZ_nGtkV4Dx2ZFjcB-n3-upjdayrOMeTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fz20-YGhejh42lWKhGwI3rF5irby8j5nbLgMT-9t9Q7C-JXhi-hRZsos5WKOxjCHzCRIkrCoxoRZKdw__KchyJZxDPCDMekuGRw9kE7JIpoyiDYRPpqMrC1of4iAIo0SDx83XRJOjg2TKAdvPJP1UBIGT-gCVr-cM6ch0jlX7L2rWeny0xhtpsZ2HJpJQ6pLEVkt9czMem-84Fy1HdsS6yTriGA0r5BgVRMt7o8Xe6cvPO8MuP3AEBJj5hjtR3mk-J-X2RpTcY389zXhDdlCRRh2z_vaw2R8kh01JwXO4V-pOSY8516EtPStzQSNzW-Vktxqf0m5O_4y-5h0t9OWxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنج‌شنبه در پیامی در شبکه ایکس نوشت که ایالات متحده در راستای افزایش فشار بر تهران و باز نگه داشتن تنگه هرمز «دسترسی هر دو شرکت هواپیمایی ایرانی به اماکن فرود، سوخت‌گیری و فروش بلیت را متوقف خواهد کرد»، اما جزئیات بیشتری ارائه نداد و به نام دو شرکت اشاره نکرد.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، با تاکید بر اینکه این کشور به کارزار «خشم اقتصادی» علیه حکومت ایران ادامه می‌دهد، در شبکه ایکس نوشت نیروهای جمهوری اسلامی حقوق دریافت نمی‌کنند، پلیس‌ها سر کار حاضر نمی‌شوند و جزیره خارک تعطیل شده است و اقتصاد و ارزش پول ایران در سقوط آزاد قرار دارد.
او افزود سازمان مدیریت تنگه هرمز از سوی جمهوری اسلامی یک شوخی است و امروز وزارت خزانه‌داری آن را تحریم کرده است. ما به هر نهاد شرکتی یا دولتی درباره پرداخت عوارض یا پنهان کردن آن به‌عنوان کمک هشدار داده‌ایم.
بسنت اضافه کرد با تشکیل «دیوار فولادی»، محاصره دریایی آمریکا باعث شده میزان نفت خام ایران در دریا به پایین‌ترین سطح تاریخی برسد.
او تاکید کرد تنها یک نتیجه رضایت‌بخش در مذاکرات این روند نزولی را متوقف خواهد کرد.
@
VahidOOnLine
دولت دونالد ترامپ نهاد موسوم به «سازمان تنگه خلیج فارس» جمهوری اسلامی را تحریم کرد
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75774" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dv4gEVr86DUhfLQcYBc0yYT7bgT0gwfSo9CJ5QbA_uKgrxMnqnmJ4Ewdav5Gw3wS9w_WK3U-dZa4p5_Vc5OSnq8WGYCETsDSs3vso4yhVkmoHv-P8pQW2BKy1BclS76QK4g36W_uGUwBUctv1Or9g_f6LUqsW_0HBlovD8aPAoHxKffEeqYFumyQBKHz2kh5NmCKIzPuNGeItBMhK1ySe6WT3ug4PSAuZ-GifZNfaI5wmzNIjhvcRrops6fqsjqjNqQfBYlATPfEhbS0K8xsmnlJfKjZXdlnQxv9_RzfZiyr5N_68PmH8-9FHVlHT71CySCrQlipjpdqijZz8hmrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g6DO85i8pwtdw2VTN91RchvWIVp3puQh-Hi_NcAyHORP_9XXQ7-yQe1iHXjM1vbPF0u4eeBJkDCTocsedkCLN0lWUQhsgn7qSyYs3a3ngBAtzbmH2SZhad-5kWyk_19YcFw-6iw8RsYi3IXCOYw4ZB9qCFoOhUwrosJPS7K45APD0N2aOUZ8gMtOXgHjFCSQU4_zacnqwcejSDBq0My-6r4BfcBAPTcLSnf3KBAbHuzgwHE0cqwg-K-Tkwbsd1DSg3EeEsTSFeqf7VqoUQD1kzITk--b8X-GexnDL62UO6eyXzs_JRqfWYCgZ-P5Pt6D2NQMAauh78SCBN33Jzy2uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خارجه کویت حملات اخیر موشکی و پهپادی رژیم ایران به خاک کویت را به عنوان یک تشدید تنش جدی و نقض آشکار حاکمیت و امنیت محکوم کرد.
این وزارتخانه روز پنج‌شنبه اعلام کرد که تهران را کاملاً مسئول حملات اخیر می‌داند و حکومت ایران خواست فوراً و بدون قید و شرط حملات را متوقف کند.
@
VahidHeadline
اسماعیل بقائی سخنگوی وزارت خارجه ایران، حمله بامداد پنج‌شنبه آمریکا به مناطقی در بندرعباس، را «تجاوز» نامید و آن را محکوم کرد.
آقای بقائی این حمله را «نقض فاحش حقوق بین‌الملل و منشور ملل متحد» دانست و افزود: «شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخگو کردن متجاوزان آمریکایی است.»
سخنگوی وزارت خارجه ایران می‌گوید آمریکا «به‌طور مستمر»، آتش‌بس میان دو کشور را که از ۱۹ فروردین اجرایی شده، «نقض» می‌کند.
سنتکام با این حال تأکید کرده که این اقدامات «سنجیده، صرفاً دفاعی و با هدف حفظ آتش‌بس» انجام شد. این دومین بار در سه روز گذشته بود که آمریکا اهدافی را در ایران هدف حمله قرار داد.
@
VahidHeadline
فرماندهی مرکزی ارتش ایالات متحده، سنتکام، حمله موشکی ایران به کویت را «نفض فاحش» آتش‌بس خوانده است.
این نهاد در حساب رسمی خود در شبکه ایکس نوشته است: «ساعت ۱۰:۱۷ شب به وقت شرق آمریکا در تاریخ ۲۷ مه، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.»
سنتکام نوشته است «این نقض فاحش آتش‌بس توسط رژیم ایران، ساعاتی پس از آن رخ داد که نیروهای ایرانی پنج پهپاد تهاجمی یک‌طرفه را شلیک کردند که تهدیدی آشکار در تنگه هرمز و نزدیکی آن ایجاد کردند.»
فرماندهی مرکزی ارتش آمریکا می‌گوید: «تمام پهپادها با موفقیت توسط نیروهای آمریکایی رهگیری شدند و آنها همچنین از پرتاب ششمین پهپاد از یک سایت کنترل زمینی ایران در بندرعباس جلوگیری کردند.»
سنتکام در ادامه آورده است: «فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای کماکان هوشیار و محتاط هستند و ما همچنان به دفاع از نیروها و منافع خود در برابر تجاوز توجیه‌ناپذیر ایران ادامه می‌دهیم.»
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای در شبکه ایکس، حملات خصمانه با موشک و پهپاد به کویت را به‌شدت محکوم و تقبیح کرد.
@
VahidOOnLine
وزارت خارجه قطر در بیانیه‌ای هدف قرار گرفتن کویت با موشک و پهپاد را به‌شدت محکوم کرد و آن را «نقض آشکار حاکمیت» این کشور و «نقض فاحش قوانین بین‌المللی» دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75772" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SayE6J9NtB8cODfOHbUytK50IaqbtZ5zMJAyLilQ04SyvGEvxzvTwRABTOUzaXvXoC2c738VXdY843UlNGEXSMO5q0X4rV331Qv6kvzhsiIeq-4uKafZPWt58WljuL5y2_mUudr42oiOPeIQNxY3fLA0ml3HgS6_tD08YeWsLo845uG4TjyLoHRbsYl8eA0THJCX3uLb4oTWRqx8GSHQhyreGP9DLHMPqFbCQmQyhBuPUKzO5DfuC6TNy-5dMunkEUuNN5I4kZyqxPSdLCQky1veImDuCPcfVAmtJwCT6PBVqZZBnuAdyD_RklwyiMF8mJeTcy7fmYQl7JPeFuslRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را خطاب به نمایندگان مجلس شورای اسلامی منتشر کردند که در آن می‌گوید «ایجاد تفرقه و تجزیه اجتماعی»، در کنار جنگ و فشار اقتصادی و محاصره، «طرح و نقشهٔ کور دشمن» است.
مجتبی خامنه‌ای در این پیام که روز پنجشنبه هفتم خرداد منتشر شد، همچنین به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داد که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
وزارت اطلاعات جمهوری اسلامی روز گذشته در بیانیه‌ای هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
وال‌استریت جورنال نیز روز پنجشنبه در گزارشی به نقل از تحلیلگران هشدار داد که ادامهٔ محاصرهٔ دریایی آمریکا علیه ایران که به کاهش ذخایر ارزی ایران انجامیده، می‌تواند احتمال بروز اعتراضات جدید در ایران را افزایش دهد.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75771" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojcz2YXFouKUeHfZey1gaKKmeWapmVDLMbBvGPnTyR3Y1CCUqMWLx3qYWfsjxDZI6YTwL3hAcY2ZD86MVJ8z1oBUHSIYdjHJhS9r1XJyTyElM-6PP2l3rDSTivweCzDsJ-fIqdTRgmgpJm2q5GubjlhsJPN8YoAbGB4vPFtzCUM7kZmUabiAY0RlOMZYKGSQeX56iB2syHmQ0IJvwTFJsRChF_92nVKMgKy4Jhu5N_iDh75lQPerB6gRS-9RZOOGQfuXFh271pKdLmjHtBqNJFAMvkfIMcfs40JwtylLKoruNhxjgTttCh1iJomU3jH7byN81jXSqpNXFQsvvLuzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری آمریکا اعلام کرد «جاناتان لودهولت»، شهروند آمریکایی ساکن استاتن آیلند، به‌دلیل مشارکت در طرح «تعقیب و قتل» مسیح علی‌نژاد، فعال سیاسی ایرانی-آمریکایی، به ۱۰ سال زندان و سه سال آزادی تحت نظارت محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75770" target="_blank">📅 18:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DQ4tIjee_SrNvbfReZpaFCkyxXnJwIRrF0iA8zW5kXNZUa41sytSQy_hbV7OSUPfpoMNJYfCQWn6v2poMcqLZOQ8wHS_gH1EjYAMudlCjLp5fLLZXGSp-iGa5VtVvJGTMOZeGRR0YKPDKPu1QHXUL3U503JlfR4_t2Qr00Gn64TlTN_bku59bVXpYrlB3cUpb3-pi-Kr4d4Fl3z5fHCjvFUJTbGu-XsKOaRb7pGhDI8qb5nEK37OXpep09Dj9jThVCbS_GE3RCWZAtA_bp7ZO6Zuz9WtabQM5qwH1iO8dl6s9TKoHGvVjZ5g8xAt_QSXjQvK46IfTRbl7q1vrSnpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، در پیامی به «غلامحسین محسنی اژه‌ای»، رییس قوه قضاییه نوشت: «قوه قضاییه زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد با قاتلان داخلی و خائنین به ملت نکشید و خوش درخشید.»
این تمجید از عملکرد قوه قضاییه درحالی صورت گرفته که در طول روزهایی که از جنگ ایران با آمریکا و اسراییل می‌گذرد دستکم ۳۹زندانی سیاسی اعدام شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75769" target="_blank">📅 18:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3AEqvckH8pEa_KvwLKMbd3qxJ_Ng9f6mcZKhSvnzWGkwEfmIkIEcYOVDMwKg2H71wMaCmolESs-kaJ3uMUXsp8v2LQCTsaqMeLLagoSetmiF8dL1jx73oLKzi8Wh-LkY8D6uqBqha7WaX5PwN3_5ILif0sU9BWhOJFosBaP_sFmrHvGv5BNDqPXABImXRZssmHA-zDGuGJ5Vz4uOdcPZ-0ZyjDGbP6dif0TpID-FXtsgSPm8dJPLfoYz-7b-Pc9NnKBVeFZCghq-B3bgOhVKnq2hy6-M7DXd_SfZo9vx5sXxHeNg9q1G8tUX9zTaUfJvgiOqo-nnhmoNwowFt0lHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس، نهاد ناظر بر اختلالات اینترنتی، اعلام کرد که علیرغم اینکه دسترسی به شبکه جهانی تا حد زیادی در ایران بازگشته است، اما شاخص‌ها نشان می‌دهند که کاربران همچنان با فیلترینگ شدید مواجه هستند.
نت‌بلاکس، این فیلترینگ شدید را مشابه دوره مابین اعتراضات سراسری دی ماه و آغاز عملیات نظامی علیه جمهوری اسلامی، حدفاصل دی ماه تا اسفند ۱۴۰۴ توصیف کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75768" target="_blank">📅 18:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMmpnsOQq7V54qMBPtKGSurVtyD4zoJbRN_YBZHINMfyFRx4yC2J0kqp6ETfRfQixLBXEpndTmdF16AKU0fKgi3D98RCSxm7mSJ3TF93WpMLF8HRsLCc7hv5KhFZHDSnD9g9BftrIyxiiBr65AyueBd1Ia-kKUR3wDn3WDOOgjdN1EzOfgsq3zzhnLhLVX7V-KhoQar9gwpStVWo_NZMjpv8ATeZUYDgnZRgvML-v0ZjxDfoo_pI9BNwT9xfLLis9ED-_gTInhfS2WfX5TxnNKMskqvjyqu-p9iDfzMXgKgN6GqKHKlxEGz3H8DGWFkr-MUAbPVkRiiJTEN_hHsDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر پیکرهای بی‌جان و شیون مادر  تصاویر دریافتی از: 'بیمارستان الغدیر #تهران، بامداد جمعه ۱۹ دی' Vahid #بیمارسان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/75767" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=RoxtCdHrLvT9vw07YsKQoOywDp2F56idam8kXpQe9oXUrcsd6MPmY5a4dWxDHX8_xX5IbU7Qqg8GGh3eW7qzJtbBhOzlH3lkIFNa0HvTw4_Agq2-RR8gE7Jc-g2dWxqnB4lzNY7rawfAaL2Fv9RZYqgXYwC5vaizYGyxrmG-EIyHdXnDjDDWkXsvdx6AGAcebCiUdfiR3-zGZwLvzvCwcgiuftQl2AuPUy7cUN8KOn8IdbpWZOlZEeJ2MjY06wqht0a9TpaHY4JCYrlbvlYhQaX_vCMgIKrYeqHlgqVyGUOTKIDGqJ4QLYKW2-ReiWuoHZBhO8NUuPmUbF5lRpoWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e61830c9f.mp4?token=RoxtCdHrLvT9vw07YsKQoOywDp2F56idam8kXpQe9oXUrcsd6MPmY5a4dWxDHX8_xX5IbU7Qqg8GGh3eW7qzJtbBhOzlH3lkIFNa0HvTw4_Agq2-RR8gE7Jc-g2dWxqnB4lzNY7rawfAaL2Fv9RZYqgXYwC5vaizYGyxrmG-EIyHdXnDjDDWkXsvdx6AGAcebCiUdfiR3-zGZwLvzvCwcgiuftQl2AuPUy7cUN8KOn8IdbpWZOlZEeJ2MjY06wqht0a9TpaHY4JCYrlbvlYhQaX_vCMgIKrYeqHlgqVyGUOTKIDGqJ4QLYKW2-ReiWuoHZBhO8NUuPmUbF5lRpoWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'رد موشک شلیک شده در آسمان
#امیدیه
خوزستان، پنج‌شنبه ۷ خرداد'
Vahid
☄️
سپاه اعلام کرد در واکنش به حمله‌های پرتابه‌های هوایی آمریکا در سحرگاه پنج‌شنبه به نقطه‌ای در حاشیه فرودگاه بندرعباس، یک پایگاه هوایی آمریکا را که مبدا این حملات بود در ساعت ۴:۵۰ هدف قرار داده است.
سپاه تاکید کرد در صورت تکرار حمله‌های آمریکا، پاسخ جمهوری اسلامی «قاطع‌تر» خواهد بود.
@
VahidOOnLine
رسانه‌هایی که بیانیه سپاه رو نقل کردند، از جمله خبرگزاری رسمی جمهوری اسلامی، ایرنا، نوشتند "ساعت ۴/۵۰" حمله کردند که یعنی چهار و نیم ولی با توجه به اینکه با دو رقم اعشار نوشتند احتمالا منظورشون چهار و پنجاه دقیقه بوده.
اما این هم عجیبه چون آژیر در کویت و پیام‌ها از امیدیه مربوط به ساعت ۵:۵۰ بودند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/75766" target="_blank">📅 06:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DaThmMOUcvPE08p8wqRAYaM3c5KHysCvZ97wGEV23MZcOgiGYt6VGkwoeEFhhNSaQ8yTeXY3J3Qf0UOWTo3osQQx61VLMa9Deoq9g3b0p3cPHq3a0snovPniwx5uWjU2j5OfcBC81ixyVune1x1DFulwSumvC98EjYgjPYreYJbpAk0b9xu_ZFzXuFGk9yoj63RVuuueLXTblwhK3D789lPOxnplRlYrb5cet6DAbn49phWxvJGsWkYqu7DIHC09JG0QrWKcn45XBmAp3sGgI8SMaidKL3Flif31dRGMq-cPRXvc47tfkRkMnU5ZyWS9MGy6UpmKYTDIvpqJ3_niEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QdgDHqacMRf1b2HCM4R8hLr8AV9hL7UfZI8YC7yxfvBy5Jaip-Mc7nAOQctZSrbOYFf_pZn8CYpogYAtcwhO1aHvXE3mVrOXGwMYBAmHz6G3K8IWDms4ti8WCbnC1t_MU0lNFqCeYxLVbjzCw7nrNsD5A7YMaoSqeIzUzUVUWUtErl2d8DhrDmpEg6icb_XbjftilNMRUx5XjFPs8Dkryv5Phmncb5FteZclukOThIqWjL9AUhvf4_zGaR7Z5mv14jZMZilz_pxagbjeKgu-6DP4jLAWE8pfNQowUqHTR9GBpPBNvhJYXaN67zEVRs1g326G9U5Nf46TcF1kzllScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uyu1S0HMqoJFNHs1rGw_DP6fRkb_r9NAQpzCeNgvEnIdw6mQESqmoodJTXQK8uf6v9IHe2kQ515IBxvkaa6Ke6e2xKf0DujGtwqnz50pOgzzzKOc1f-VAjKVgRqdMEpl259rWQvlynh-g03-nPQPKOAcg-gmKmzCh5XX6T8Xpx8XEqdOmtctVWSVQZqpEwEbHvWZq60kZchWTq3KFZ0IVApCQSddaRerxCbDaQ8mlo9WuLXdnFhmxFfs7G515Y87RuA-uEXN6r-ekHaJ_I6vQHN90uM8hFf8_QnHayBatop2SwTCh5dbzrynP8GoNxK-fPPF1JNMFXTZJFEN24EDUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از
#امیدیه
در خوزستان پیام‌ها و تصاویری دریافت می‌کنم  که میگن حدود ساعت ۵:۵۰ موشکی شلیک شده و سمت تونل امیدیه میانکوه صدای انفجاری شنیده شده.
یکی نوشته لانچر هدف گرفته شده.
دقیقا میشه هم‌زمان با
شنیده شدن آژیر در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/75763" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hv36hUetyUXiCiL-bM9u9zK_njbuVJoo3RrdPg5PvPPC6BfDu26OxUbrQuVdtvOnH9mHy8OFWc1YOT2LDWlG4gY-8IxF0e44N5F4sK1XDaXEQcK3TMRNy-c29d8EbvXUHuJnFepZFYs3sOZStD32idhVLj2QijA3Vnfe04ZgjIQsd6V3zdvG2IZNEKCr-sLTH_8nYIc33gURgjYIEqSdBD9X55YlUwaiqPpkfaCnIt6aUf2pxaybGzbxS-4j5hbJlOspTJxOlb9wdHb__kAhZN8jVKZqFvv3Jr0g-wpoo4uaGPicEIX_LJj3hM9MJiER40DcvQtl9GI19Vt3InxJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید الان کویت رو زد ۵/۲۰
وحيد همين الان اژير كويت فعال شد
سلام صدای پدافند و تقریبا ۲ تا انفجار در کویت
درود وحید
🙋🏻‍♂️
اینجا ساعت ۵:۲۰ به وقت کویت صدای اژیر اومد و رو گوشی ها هشدار اومد
ولی هنوز هیچ رسانه‌ی کویتیی دلیل این اتفاقو نگفته
آپدیت:
ارتش کویت اعلام کرد سامانه‌های پدافند هوایی این کشور حملات موشکی و پهپادی «متخاصم» را رهگیری کرده‌اند، اما مشخص نکرد این تهدیدها از کجا منشأ گرفته‌اند.
ارتش کویت در بیانیه‌ای اعلام کرد صداهای انفجاری که در کشور شنیده شده است، ناشی از رهگیری این تهدیدها توسط سامانه‌های دفاع هوایی بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/75762" target="_blank">📅 05:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6ILrSezW5x0Yp3_hGcKPdRJk96WoprFeYvvgUaO8fRBlp_HgLwu7g_OkyyZh9Zm2AntAXqYmMfnjyyoB7LTfqJZSQALCWWnykSj1RY3DZMjX7cLKzaLxbK0vDvY1rXz9QaWrTMI9VnOtiVh8oCZwdd__Qh8FOX7PiZwfms1xPWifjo2FOnCdlx1zPr-4B__9KW15bFd_ZG0OrNa1Mwk7ZGUYePBQVjvJNMno94t7C1zzOZTmZnNAWIK_MM_oBSZ_gCe02SlxukWg3FbyHyWL0qMkwJaW_R0FPMIMsSo2H5KX9frOo14GGwGrP0y0x-qxUD4dHtAqFRDs-y9uWBmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسوشیتدپرس به نقل از مقامات آمریکایی گزارش داد که نیروهای فرماندهی مرکزی آمریکا چهار پهپاد تهاجمی یک‌طرفه ایران را که در نزدیکی تنگه هرمز تهدیدی ایجاد کرده بودند سرنگون کردند و یک ایستگاه کنترل زمینی را در بندر عباس هدف گرفتند که در آستانه پرتاب پنجمین پهپاد بود.
@
VahidOOnLine
در همین حال، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، به نقل از یک منبع آگاه نوشت: «ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.»
تسنیم درباره حمله هوایی آمریکا به نقاطی در شرق بندرعباس نوشته نیروهای آمریکایی «به زمین سوخته‌ای در اطراف بندرعباس شلیک کرد که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/75761" target="_blank">📅 03:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی:
چهار تا صدای انفجار پشت سر هم اومد الان
ساعت ۱:۳۳ بندرعباس
درود آقا وحید همین الان سه تا صدای انفجار اومد تو بندرعباس ساعت ۱:۳۳ دقیقه
حاجی صدای انفجار دوباره شرق بندرعباس همین حالا  سه تا پشت سر هم ساعت1/43 دقیقه
سلام وحید
۰۱:۳۳ شب
همین الان بندرعباس صدای ۳ تا انفجار اومد
سمت بهشت بندر
احتمالا باز مثل سری قبل باند فرودگاهه
بندرعباس ساعت ۱:۳۰ هفتم خرداد صدای جنگنده بعدش سه تا صدا انفجار اومد
سه تا انفجار بندرعباس
ساعت 1 و 33 دقیقه بامداد پنجشنبه 7 خرداد صدای سه تا انفجار رو از بندر عباس کس دیگه ای هم گزارش کرده ؟
شبیه صدای موشک زمین به هوا بود
بندرعباس صدا اومد
سه بار
درود. ساعت ۱:۳۲ دقیقه صدای سه انفجار شدید در بندرعباس اومد و خونه شدید لرزید.
ساعت ۱:۴۷ باز هم صدای دو انفجار دیگه اومد
صدای سه انفجار بندرعباس همین الان
سلام وحید جان بندرعباس چند انفجار وحشتناک پنجره خونه لرزید 1.38
دباره زدن بندرعباس ساعت 1.49
۳تا صدای انفجار بعد صدای پدافند
سه انفجار پشت سر هم و یکی هم ده دقیقه بعدش بندرعباس رخ داده
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/75760" target="_blank">📅 01:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvljEpXXSsF2dTfiX7cx45FzxGeQ4-UV61xPCYmrhIxX6MmUOklAOaQQreSOzK9zj22sHYQgdCOos-5p8ua-u3fLLB2XPNC6fLhEZ6Pn20VQCqxNN5MLEYsC3L_jpailjlaIwUILWxj4eRiur-i48kWsdpRzepeQjTHh7EvuDHjSn66ymIpRWcBD_Nxfk5RGaBgWmFwNmYBLVA0Luxe5irTAr5ce4P5E35XTilLT5Sw2jC42vnUNgqW4qTS5nPh2qc1x5mxZo0bXJo7BoVP_dIN6NDWYmDtKc9T-_BlLSOAv2-V8n-pivStwPwB74Zz6lj9jhixkKhpmK-a58gbQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=JoOWlHyLkQIclvOxY_fhuI4fWf0rb9FIUpkV4lPeuFBIovBTkeN6aUCI7zQtihOJdcNUIFnXAmALmyciZOD95d-f-w6jZa6zuKJnOxw_DS_TOy_oLtZIHadIScvHZC4ZcepZ1gWaQ_piC2vpfG-YZJrhisfCocA-nzKbXRlM25Yz7kjJZ-UuMMvrEoyIAtsOkv5UVI85N1-LNkjHcd1OEmbf7ZNwygn9qLmVYt_LMrGdgsaT5c6GelECmb2giZdo9g21LQdDII1Ntr4n0q_4b_2wWx7BKBLkFCZiJf_-vA-1xFexyhcJfPObqmE7GFcSnLeoGYGzY6y9cHC3jnYWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c97c6720.mp4?token=JoOWlHyLkQIclvOxY_fhuI4fWf0rb9FIUpkV4lPeuFBIovBTkeN6aUCI7zQtihOJdcNUIFnXAmALmyciZOD95d-f-w6jZa6zuKJnOxw_DS_TOy_oLtZIHadIScvHZC4ZcepZ1gWaQ_piC2vpfG-YZJrhisfCocA-nzKbXRlM25Yz7kjJZ-UuMMvrEoyIAtsOkv5UVI85N1-LNkjHcd1OEmbf7ZNwygn9qLmVYt_LMrGdgsaT5c6GelECmb2giZdo9g21LQdDII1Ntr4n0q_4b_2wWx7BKBLkFCZiJf_-vA-1xFexyhcJfPObqmE7GFcSnLeoGYGzY6y9cHC3jnYWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره لغو یا کاهش تحریم‌های جمهوری اسلامی گفت واشینگتن «درباره هیچ‌گونه کاهش تحریم‌ها یا دادن پول» صحبت نمی‌کند و تاکید کرد: «هیچ تحریمی، هیچ پولی، هیچ چیزی.»
او افزود آمریکا کنترل پولی را که جمهوری اسلامی ادعا می‌کند متعلق به خود است در اختیار دارد و این کنترل را حفظ خواهد کرد. ترامپ گفت زمانی که جمهوری اسلامی «رفتار درستی» داشته باشد و «کار درست را انجام دهد»، اجازه دسترسی به این پول داده خواهد شد، اما «در حال حاضر چنین کاری انجام نمی‌دهیم» و «این دو موضوع به هم وابسته نیستند.»
ترامپ همچنین درباره انتقال اورانیوم غنی‌شده گفت با انتقال ذخایر اورانیوم غنی‌شده ایران به روسیه یا چین موافق نیست.
@
VahidOOnLine
دونالد ترامپ در پاسخ به سوالی درباره کنترل تنگه هرمز توسط تهران و عمان گفت این تنگه برای همه باز خواهد بود و آب‌های بین‌المللی محسوب می‌شود. او تاکید کرد هیچ‌کس آن را کنترل نخواهد کرد و آمریکا بر آن نظارت خواهد داشت.
ترامپ افزود کنترل تنگه بخشی از مذاکرات است و ایران تمایل دارد آن را در اختیار بگیرد، اما چنین اتفاقی نخواهد افتاد. او درباره عمان نیز گفت این کشور مانند دیگران رفتار خواهد کرد و در غیر این صورت آمریکا مجبور خواهد شد آن‌ها را منفجر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/75758" target="_blank">📅 21:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUc6BCkIsKQVqCh3Ua3mMFqWZe_O8fXed5CchQwqcIl6DUwBjMWSmJGSeZefBWx2PI8-Asqpw4L5ktc9BWEIlQJu7aApWeZ55YQC7OBTg4nxptPTitc4gq6vAfBMTnWxaIuQbKri-yO9bNybYw92lo4Iipt3eSCfOaPwYpwSuiFygBmmvKRqBUFo05WNcIMBJA2J9zouJ9aj4165bKTSuanbDIyz3jxupacCYAiRSY8dT6Z-Wd9Oge0He0p0CxC6WuNKW2IhpOARB5UWvFattmItNy9lzzAep8pR10UIDZYou0rgxt3j_FFi8r1TpGs01QxhtVJK7jyweMN8NbGb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه گفت که ایران در ازای کنار گذاشتن اورانیوم با غنای بالای خود، از لغو تحریم‌ها توسط واشینگتن برخوردار نخواهد شد و از پیشنهادات ایران برای توافق پایان جنگ ابراز نارضایتی کرد.
ترامپ پیش از برگزاری جلسه کابینه خود در یک تماس تلفنی کوتاه با شبکه پی‌بی‌اس نیوز، در پاسخ به این سوال که آیا توافق فعلی به این معناست که ایران در ازای لغو تحریم‌ها، اورانیوم با غنای بالای خود را واگذار خواهد کرد، گفت: «نه، نه، اصلاً. خبری از لغو تحریم‌ها نیست، نه.»
او اضافه کرد: «آن‌ها قرار است اورانیوم با غنای بالای خود را کنار بگذارند، نه در ازای لغو تحریم‌ها. نه، نه، اصلاً.»
ایران بیش از ۴۰۰ کیلو اورانیوم غنی شده تا حد ۶۰ درصد دارد که در تأسیسات زیرزمینی هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون است.
رئیس‌جمهور ایالات متحده ساعتی بعد در ابتدای نشست کابینه خود در کاخ سفید گفت که ایران بسیار مایل است به توافق برسد، اما آمریکا هنوز از توافق پیشنهادی رضایت ندارد.
ترامپ در این نشست در حضور خبرنگاران گفت: «ایران خیلی مصمم است، آن‌ها خیلی می‌خواهند که به توافق برسند. تا اینجا هنوز موفق نشده‌اند... ما از آن راضی نیستیم، اما خواهیم شد.»
او سپس بار دیگر ایران را به ازسرگیری حملات نظامی تهدید کرد: «یا به آن نقطه می‌رسیم، یا اینکه مجبور می‌شویم کار را یکسره کنیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/75757" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpIEy2K_bYawfhxcZNs4gBanD8B8VsOTOGOwDpSyNeNIHQxNPLJEnzyQ5SwAra6p513U-S-wURm_TlgjjjgMqQSbU0RbFU2MfVkAQg-BVPdfZype7Xm1g1YRh3EEBoAjNnno7YmHikbTDMEfjJzkdHG1T-zFvwe-DIxZYPDUmiS-tZgc6i7wFCkaBknkFnVU09HYFgdn-F5fAPSn4dHy541Ki5SpVIR4eEWdLauM5PxPFJfKXg4lBTGndlRmuuxCltb5ev7mpPo4LhRKsyBe3e2lWIej_3QLqRfBklmD0_D3Y1uanXTZkhN3LZ-BXqavSzqi-QDOk286V_gg5FbAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تصاویر دلخراش از اجساد مردم کشته‌شده در بیمارستان تهرانپارس تهران
⚠️
دو روز پیش ویدیوی دوم رو با تردید منتشر کرده بودم و نوشته بودم نمی‌دونم درسته یا نه. حالا عکس‌هایی از بیمارستان تهرانپارس با شرح جان‌باختگان ۱۸ و ۱۹ دی دریافت کردم که نشون میدن اون ویدیو…</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75756" target="_blank">📅 20:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=VBuoTQk50mW0kD0ruQgRJYaCJWVJWUryYvC289Ir9996MFq6c9ktWzD6aprV00wceE81i86wOrk5Dw9Ujdvq6i1WhvqSPGauundq6batx7Tmii_tDTi7B_2RDfcHZve0xkRrzLMcNy0vMe2MtuKohn-LdGXJAd7lgfi4AUcUHg9Wc3uKXiQTU588B-QdQtXWxGWWPKJ_O1orIMUMuHUsbB616ZJXrehiRiBDEmNwOKEMqBeNcSR43WYUtg2anUNItlq4PpK8EhbWUYaCJtdqSHCXsqBrY0OvioKP7k_JeyEEyQjAbv7Eifgl4uouBpc9-sUapvTSTGjKRb_JJyUqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43dd15a53a.mp4?token=VBuoTQk50mW0kD0ruQgRJYaCJWVJWUryYvC289Ir9996MFq6c9ktWzD6aprV00wceE81i86wOrk5Dw9Ujdvq6i1WhvqSPGauundq6batx7Tmii_tDTi7B_2RDfcHZve0xkRrzLMcNy0vMe2MtuKohn-LdGXJAd7lgfi4AUcUHg9Wc3uKXiQTU588B-QdQtXWxGWWPKJ_O1orIMUMuHUsbB616ZJXrehiRiBDEmNwOKEMqBeNcSR43WYUtg2anUNItlq4PpK8EhbWUYaCJtdqSHCXsqBrY0OvioKP7k_JeyEEyQjAbv7Eifgl4uouBpc9-sUapvTSTGjKRb_JJyUqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد، در نشست کابینه در کاخ سفید درباره مذاکرات با جمهوری اسلامی گفت تهران «بسیار مشتاق» توافق است، اما مذاکرات هنوز به نتیجه نهایی نرسیده است.
ترامپ گفت: ما از وضعیت فعلی راضی نیستیم ولی خواهیم شد.
رئیس‌جمهوری آمریکا همچنین جمهوری اسلامی را تحت فشار شدید توصیف کرد و گفت: «نیروی دریایی‌شان نابود شده، نیروی هوایی از بین رفته و همه‌چیزشان از دست رفته است.»
ترامپ افزود جمهوری اسلامی «در حالی مذاکره می‌کند که چیزی برایش باقی نمانده» و هشدار داد اگر توافق حاصل نشود، آمریکا ممکن است «برگردد و کار را تمام کند.»
ترامپ گفت: «آنها تازه دوباره به اینترنت برگشته‌اند، چون به‌شدت تحت فشار قرار گرفته‌اند.»
او همچنین گفت اقتصاد ایران «در حال سقوط آزاد» است و تهران به‌دلیل فشارهای سنگین، گزینه دیگری جز حرکت به‌سوی توافق ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75755" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری فارس به نقل از «منابع آگاه» گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، ممکن است در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق میان ایران و آمریکا نهایی شده است؛ اقدامی که به گفته این منابع می‌تواند با هدف اعمال فشار سیاسی و اثرگذاری بر افکار عمومی انجام شود، پیش از آنکه اختلافات باقی‌مانده به‌طور کامل برطرف شود.
بر اساس این گزارش، این سناریو در حالی مطرح شده که هنوز برخی موضوعات میان دو طرف حل‌نشده باقی مانده و روند مذاکرات به مرحله نهایی نرسیده است.
در همین زمینه، یک عضو تیم مذاکره‌کننده ایرانی در گفتگو با فارس تاکید کرده است که تا زمانی که همه موارد مورد نظر ایران حل و فصل نشود، هیچ توافقی قابل اعلام نخواهد بود.
به گفته این منبع، جمهوری اسلامی ایران تنها در صورتی که اختلافات به‌طور کامل برطرف شود، نتیجه مذاکرات را به‌صورت رسمی اعلام خواهد کرد و هیچ توافقی پیش از رسیدن به جمع‌بندی نهایی، مورد تایید تهران نخواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75753" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gYzfk4GJL0qnW54oyU8UFAwEyP5r1VD9j9ULdrPyZ9qj2v12EbTNnBM7EAZ3X0BwaHRSqbHbnvEzDbmOgoMVS7OA9pytxM_Y2ZQntcC5YhXTlXRKS1zOXVnUpriFQVz1RA8MuFyyBnNM99aGYVoVuv2BlHi6rvOwb1cMdgRjxrdVoObxXedt8Uu0OfPzQuI148I-gnIGOgAgrEIqzcNGwxXV21bKqANkxJn6sRL9x9sxoJhWklc7ORXHUI8-SwYT6_5f3fu62tyqsda_qOqkqqmj1NvJgE6jMGr-PruecxpenoXXnRAF_3fQ5n39U40AkbsvMy9qfAyzi1VWxfz6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=wAfWIMzSaeP1lcJ8ndhVaVNqHOH6CRKirBBRkV_h9FDUE89MzKJinP880_DYyWZeqiPahhzE9_xJyVvcbaky096yaOJxpsDtrAoHw6icqDT3IbH28tk1IJpO316KOyyxHd5s8gxnat-poW31Chglh2gmQkcPQdFdu8dl_KsgGWIbinoSA_5pUerdUTZJbohnSONvZJ4a1h0qDqdPqrZV4j2q365uaB9U4VkIakTyNwNa0EV3DKQUa5sNSbznDzsp_C3X3IJ8WiYxOMsWX60XcsDNqIkbVkLZ5bJsfWZb2j3fbl9V9wIN3HEWu6WAL-4XUOPKtWxFA7YmpiFxCeIBEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a77ea28679.mp4?token=wAfWIMzSaeP1lcJ8ndhVaVNqHOH6CRKirBBRkV_h9FDUE89MzKJinP880_DYyWZeqiPahhzE9_xJyVvcbaky096yaOJxpsDtrAoHw6icqDT3IbH28tk1IJpO316KOyyxHd5s8gxnat-poW31Chglh2gmQkcPQdFdu8dl_KsgGWIbinoSA_5pUerdUTZJbohnSONvZJ4a1h0qDqdPqrZV4j2q365uaB9U4VkIakTyNwNa0EV3DKQUa5sNSbznDzsp_C3X3IJ8WiYxOMsWX60XcsDNqIkbVkLZ5bJsfWZb2j3fbl9V9wIN3HEWu6WAL-4XUOPKtWxFA7YmpiFxCeIBEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آتش‌سوزی
در یکی از برج‌های مجتمع مسکونی پامچال در چیتگر
#تهران
تصاویر دریافتی + منتشرشده، چهارشنبه ۶ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75749" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqvsssNT_4RdyBsV0JnWMFRf_oMITN-ETUWr9_f-0JRCaRh2EKQy6nRUt5w5m3UXkcW1sh0IaaUYyiWwRHYhex4SEjwz6PPCaVHKcT8uPBDVUOQRGb3h3yhJUUlx6A3MmCcxkA7rapGgZFAjl5YUCeufk-vyd1WC3ZsHwOzWhYZ9s2-LMOnT0F89uh9vTP5awMEXHfyrdVBRT8yKbWj_Hibcvjnc98Eqw-_YpTnsmhsh9-EasvtUe-ldZH0kCPrOXM5Edu85MrR5rKNbQyrE9JP_uwHbVo_vVH0X_ghLJP_fxXnPDsEkVTLLa8wMzzK6c88mW7T8Dt_2aeYeS5VXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید روز چهارشنبه اعلام کرد گزارشی که از سوی صداوسیمای جمهوری اسلامی منتشر شده و به پیش‌نویس یک چارچوب اولیه و غیررسمی برای تفاهم‌نامه میان ایران و ایالات متحده اشاره داشت، «صحیح نیست» و تفاهم‌نامه مورد اشاره «کاملاً ساختگی» است.
تلویزیون حکومتی ایران ساعتی قبل گزارش داده بود که پیش‌نویس یک توافق چارچوبی با ایالات متحده شامل تعهد به لغو محاصره دریایی ایران، بازگرداندن رفت‌وآمد در تنگه هرمز و خروج نیروهای آمریکایی از منطقه خلیج فارس است.
کاخ سفید در بیانیه‌ای اعلام کرد: «این گزارش رسانه‌های تحت کنترل ایران حقیقت ندارد و تفاهم‌نامه‌ای که آنها منتشر کرده‌اند کاملاً ساختگی است. هیچ‌کس نباید آنچه رسانه‌های دولتی ایران منتشر می‌کنند را باور کند. واقعیت‌ها اهمیت دارند.»
گزارش صداوسیما
مدعی شده بود که آمریکا متعهد به رفع محاصره دریایی ایران شده و در مقابل، ایران تعهد داده تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند.
تلویزیون جمهوری اسلامی همچنین گفته بود بر اساس این پیش‌نویس، «مدیریت و مسیر عبور و مرور» کشتی‌ها با ایران و همکاری عمان انجام خواهد شد و آمریکا تعهد داده نیروهای نظامی این کشور از «محیط پیرامونی ایران خارج شوند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75748" target="_blank">📅 18:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-UpqyOdcaILMzC7id_GfrC_yuPmbU-ldvAMdk8TsXfEWw_22s20jtwSmaJJf-MuHUiVr9qtVMu0rJ3wiBMwc3zoNOd9dJK9Z-cXy1WU-DWZosy2mI9DN8LL6nvrF3UekAAJ-7GL44BYbPDxL0kzgvC012JuvPc0eeFeLPYisa3V2Odyntjg0gn6_5T7d3GcotNbakmYgO4CHQlFEmZDS_y28d9I7RGt9X0F-raFs0RCyNM1UdtqmkFOogwkzd_97767u0rcUx14iVSSBuBCJLX_rdP7Inn83R4ldlStX5OH4q4uVFMD9k8W4vyMBl_LvO8JzQ5HLBuIr5iDcwlRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد‌ ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه ششم خرداد در شبکه اجتماعی تروث سوشال با انتشار تصویری ساخته‌شده با هوش مصنوعی، از شبکه سی‌ان‌ان انتقاد کرد و نوشت این رسانه نیروی دریایی جمهوری اسلامی را قدرتمند نشان می‌دهد، در حالی که شناورهای ایران در اقیانوس غرق شده‌اند.
در این تصویر، جمله «سی‌ان‌ان: نیروی دریایی ایران قدرتمند است» در کنار تصویری از شناورهای غرق‌شده جمهوری اسلامی در کف اقیانوس دیده می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75747" target="_blank">📅 18:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C8-5eHx2PdAZ9yHl6HPlLQD6N8VQob5LzIG33zmzGPw78jVT8e3GDHx2z2yQ2jGAZFTc3REisVttUQYhfClyT1XuVBkeNdKThwCkN48EUOJV0HwOFLYPgN2fLgoqGiKBmfInigUmeR9MpTVOpticYLel4Qcf2T3SbKY6Tnc8QL5zuStiSXHxN-2DdAitdSt9lcJkoz8Hicio6C9ikBk49I6CaICmn9BKlelxOGFbLKAbwEDn77bb459jHW6ec0IJkmsDvEtxJywPMeGo5BQF6imRlS5iOqhzAYm9_aRJKOqlOdGp3MD2oXDqqMygWRb31n0yRvL6D8sLiOgFAM6GlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گروهی از کاربران در شبکه اجتماعی ایکس (توییتر سابق) پست‌های انتقادی گزارش‌گونه از تحولات و رویدادهای سیاسی خارج از ایران منتشر می‌کنند، خطاب به شهروندانی که پس از حدود سه ماه به‌طور تدریجی با فیلترشکن موفق می‌‌شوند به اینترنت وصل شوند.
‏این پست‌ها که با عبارت‌هایی مانند «
وقتی شما نبودید
» یا «بچه‌های ایران که تازه وصل شده‌اید» آغاز می‌شود، همزمان با کاهش تدریجی اختلال در دسترسی به اینترنت، به محلی برای مستندسازی و بازاندیشی انتقادی نسبت به تحولات سیاسی‌ ۸۸ روز گذشته تبدیل شده است.
@
VahidHeadline
دوستانی که تازه وصل شدن یدونه «
سلام وحید جان
» سرچ کنید آرشیو کامل از اندر احوالات ایرانی جماعت در زمان قطعی نت رو براتون میاره
iamroyaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75746" target="_blank">📅 18:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=QD42khBfKQK32p6opgJkFA50cXf29sdn_9BvG8yWwW6rcztyGzYEL8uW3u2ovcY_Glh4aocxwD-HFJB94yznbeK9cjuuW5F_GyEDQGxfUsGFgA9ZTx3FvqBlRudC39imSMNKhgPiUnEAIJ0JrCBKZVtcFDHoyM5TrXvZIsHgTlzIlGcLRczpxUtCXDGJpW-2qW2aiWXLf7BmW-TMzBfCi3wPLzcddmHT9ZBKkn4bIOXpCiQEFIhFOyVIGKqpqLdrfbAhg5PukRddE-wyEu314nL1ZcvWryRDCRn5LYeQZiq8Dz6NZbpo-iYX7gXC-LBoGf9gj6Z7p1hZwZFZZ0YDbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d05e2caab7.mp4?token=QD42khBfKQK32p6opgJkFA50cXf29sdn_9BvG8yWwW6rcztyGzYEL8uW3u2ovcY_Glh4aocxwD-HFJB94yznbeK9cjuuW5F_GyEDQGxfUsGFgA9ZTx3FvqBlRudC39imSMNKhgPiUnEAIJ0JrCBKZVtcFDHoyM5TrXvZIsHgTlzIlGcLRczpxUtCXDGJpW-2qW2aiWXLf7BmW-TMzBfCi3wPLzcddmHT9ZBKkn4bIOXpCiQEFIhFOyVIGKqpqLdrfbAhg5PukRddE-wyEu314nL1ZcvWryRDCRn5LYeQZiq8Dz6NZbpo-iYX7gXC-LBoGf9gj6Z7p1hZwZFZZ0YDbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما اعلام کرد به یک سند غیررسمی اولیه از چارچوب ۱۴ بندی تفاهم احتمالی میان ایران و آمریکا دسترسی پیدا کرده، سندی که به گفته رسانه‌های ایرانی، هنوز نهایی نشده اما حاوی جزئیاتی درباره وضعیت تنگه هرمز و حضور نظامی آمریکا در منطقه است.
بر اساس این گزارش، در پیش‌نویس منتشرشده آمده است که آمریکا متعهد می‌شود نیروهای نظامی خود را از اطراف ایران خارج کرده و محاصره دریایی را متوقف کند. در مقابل، تهران نیز تعهد می‌دهد ظرف مدت یک ماه، عبور کشتی‌های تجاری از تنگه هرمز را به سطح پیش از جنگ بازگرداند.
طبق مفاد این سند، کشتی‌های نظامی مشمول توافق نخواهند بود و مدیریت مسیر حرکت کشتی‌های تجاری در تنگه هرمز با همکاری ایران و سلطنت عمان انجام می‌شود.
صداوسیما همچنین گزارش داد که هنوز چارچوب نهایی تفاهم تدوین نشده و ایران تاکید کرده بدون وجود «سازوکار راستی‌آزمایی» یا همان مکانیزم اطمینان، هیچ اقدام عملی انجام نخواهد داد.
در بخش دیگری از این گزارش آمده است که اگر دو طرف طی ۶۰ روز آینده به توافق نهایی برسند، این تفاهم می‌تواند در قالب یک قطعنامه الزام‌آور در شورای امنیت سازمان ملل تصویب شود.
@
VahidOOnLine
🔄
آپدیت:
کاخ سفید: گزارش رسانه‌های جمهوری اسلامی درباره تفاهم‌نامه تهران و واشینگتن کاملا ساختگی است
کاخ سفید گزارش رسانه‌های جمهوری اسلامی درباره بندهای تفاهم‌نامه احتمالی را «کاملا ساختگی» خواند و گفت نباید به روایت رسانه‌های جمهوری اسلامی اعتماد کرد
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75745" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-ymkvoOZJtHJgUJJ-S6Q0nFpYxmeZsFHuwG3PtD1oQiKuPhzM9SoydgNIjC36dZVHJMvSe80dMLGZgFFF_9zhpxuQgSoj7sybce89T_LJ0Cm1NobHK90Im15xQ3rQxcNaLDMWHJi5sRHQurC70jvemGb82GGz1tXD99dUFI3JiBD0miMD_GM9cEcqvvb2f6YFUU8GBKW8Zc1Y0ykXAgUg9NQldIcB99Uq2no7-4OwNtKpI0x7O99XOtcAWmqu-k0-ndMeWSq3MzwvPtmUAmUVxp6w7jFQKEJ45VCayatNpiLLlq5R7uteGYIPWTxlbO6sH0xp4E48cQ0fCHTB_0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در تروث‌سوشال گزارشی از جروزالم‌پست را بازنشر کرد که بر اساس اطلاعات اختصاصی «مدیا لاین» نوشته است موارد آزار و تعرض جنسی به زنان بازداشت‌شده، به‌ویژه زنان جوان، در زندان‌ها و بازداشتگاه‌های جمهوری اسلامی در دوران آتش‌بس افزایش یافته است.
در این گزارش، زنی جوان به نام کاملیا گفته پس از بازداشت خشونت‌آمیز در خانه‌اش، دو هفته همراه هشت زن دیگر، از جمله دختری ۱۶ ساله که با ساچمه از ناحیه صورت زخمی شده بود، در اتاقی ۲۰ متری نگهداری شد.
به گفته کاملیا، او پس از انتقال به سلول انفرادی و خودداری از اعتراف اجباری، در اتاق بازجویی هدف خشونت قرار گرفت، لباس‌هایش پاره شد، با باتوم مورد تجاوز قرار گرفت، به‌شدت کتک خورد و به تجاوز گروهی تهدید شد.
جروزالم‌پست همچنین با اشاره به قطع گسترده اینترنت، بازداشت‌ها، ناپدیدسازی قهری، آدم‌ربایی، تهدید روزنامه‌نگاران و مخالفان در خارج از کشور و افزایش ناگهانی اعدام مخالفان نوشت سرکوب در ایران تشدید شده است.
دونالد ترامپ پیش‌تر نیز با انتشار پستی در تروث سوشال خواستار آزادی هشت زندانی سیاسی زن در ایران شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75744" target="_blank">📅 17:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CaRP06_PwFrP5_VbG9RYwTH7m8vldXvazpzBIioVqMblMPCZJWCv5pXzh6S1PTNOu8QHCKa1brxFaypGffeidPWvmD8l52nuMsM0IBr16UCWvTMTonmEnS2WbteaOSHvnod6iusrY7c3NwHQcoFEZlv0SQN3fhRLJqCiqhQy3aZWStTV3bkO1spdL-SVJOSlTlGugH9-2W0yPTchr666XAGYP3Exag0lFdkZAZrLEw2xRO2laqS5HUNUCa4jtLR92otVRwoTbiwJ-YYVeYRKK9Jm095rBfK46Jnpz9pebesmt3Pz5-aZ8CiMSFjjLgdF5o-C_ncf3-XJSCY4sa-MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bj2BMi8ygOnrF0Jt2Cp_qljrHhWcO1XwpNVMmLN33FFghQ-eymr1y2lo0BbmMbs1-6uFN9tpgBEl3opWWQCABSpSh0oxNML-i6YrB8An_QLtDslkEVu_Z5mrS4CekRrjywsVtgYM83CpHQwvrGA6uUPwW7GfK2fVvHDOLeigKM_m6mvdCkCTVGsIW1Is72Bul-c9thhsXlmcufyLao9zHpJ9h_NFfwW9JDIhIysZU3J5AjfZwe7peihONPsUQAtAd5GwwsBwxgwoUQ3EWxAswz_wFNITeB_Qpqzb4IUcdLLzzTJ-8cL8v8L75GUMSXz4X58Fa2G97SAGexnNld98Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز چهارشنبه ششم خرداد هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
این وزارتخانه در بیانیه‌ای مدعی شد که «تشدید فشارهای اقتصادی و متعاقب آن، انجام تحریکات گوناگون اجتماعی توسط عوامل دشمن و رسانه‌های مزدور فارسی‌زبان بیگانه، با سوء استفاده از برخی کمبودها و گرانی‌ها» یکی از محورهای مورد توجه آمریکا و اسرائیل است.
هشدار درباره احتمال ناآرامی همزمان با افزایش شدید نرخ تورم و و گرانی کالاها و همچنین انتشار گزارش‌هایی درباره کاهش شدید درآمدهای دولت جمهوری اسلامی در پی هفته‌ها محاصره دریایی آمریکا و سقوط شدید صادرات نفت ایران مطرح شده است.
این در حالی است که اعتراضات دی‌ماه سال گذشته نیز بعد از افزایش مداوم نرخ ارز در بازار و مناطق تجاری ایران آغاز و بعد از چند روز با افزایش تعداد معترضان، با خشونت شدید نیروهای امنیتی و کشتار هزاران نفر مواجه شد.
وزارت اطلاعات همچنین درباره «عملیات تروریستی و تجاوزات مرزی بویژه در شمال غرب و جنوب شرق ایران» و انواع عملیات «ترور و خرابکاری» هشدار داده و مدعی شده که آمریکا و اسرائیل به دنبال وارد کردن «انواع سلاح، مهمات و ابزار ارتباطی غیرقانونی، بویژه استارلینک» به ایران هستند.
ابراز نگرانی از رواج اینترنت ماهواره‌ای استارلینک در حالی است که بعد از ۸۸ روز قطع سراسری اینترنت در ایران، از روز سه‌شنبه شهروندان توانسته‌اند به شکل تدریجی و محدود به برخی سرویس‌های اینترنت جهانی دسترسی پیدا کنند.
@
VahidHeadline
این بیانیه که با عنوان «سخنی با ولی‌نعمتان و هشداری به دشمنان» در رسانه‌های داخلی ایران منتشر شده، ادعا می‌کند که «دشمن شکست خورده در جنگ نظامی، بدنبال تولید دستآورد برای خویش، گرچه از طریق جنگ نرم، می‌باشد.»
این بیانیه در حالی صادر می‌شود که اسماعیل خطیب، وزیر اطلاعات جمهوری اسلامی در سومین هفته جنگ در حمله اسرائیل کشته شد و دولت هنوز جانشینی برای او معرفی نکرده است.
وزارت اطلاعات در این بیانیه علاوه بر اسرائیل و آمریکا، بریتانیا و اروپا را به همراهی با این دو قدرت متهم و کشورهای عرب حاشیه خلیج فارس را به‌عنوان «غلامان متمول» مسئول تامین مالی «جنگ ترکیبی تمام عیار» علیه «مردم قهرمان ایران» معرفی کرده است.
وزارت اطلاعات در این بیانیه معترضان و مخالفان جمهوری اسلامی در خارج از ایران را تهدید کرد و نوشت: «مزدوران ضد انقلاب و تروریست‌های مقیم خارج کشور و حامیان آن‌ها نیز از آتشی که می‌افروزند در امان نخواهند بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/75742" target="_blank">📅 17:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avcqJih_7Oy6c3HaYEwVq4wyM9nU4nSC0miW9OM_Ulem7uBy2ENPEtR1ZTgmqjmK0e_fE2-33gMZVT2A8oFD4OCpFZzf6U3T9wmD4kObFEP_YTdx7_DVNx2EwaJGGaUPxijaTI43Vfr_hGGROgLyvPFX5AghIpFYxZ0cIk3Z5nmYEhrdtnZb5rWL4Nn7djEOq_jUpf0T22UE-RHpZkDHS3ZsuC10PNZUYSqmwNEs3cwkp9IkSw1GIIV4YnXnb6HN8Mzf4voweev35tQg5covNHTh0ztAgBZXppCGzPxw2bd99YdCOGC6LwyvA7MpRAITRSwh--vvUWSxXEGZz7eXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی در روز سه‌شنبه ۵ خرداد گزارش داد که حملات دوشنبه شب نظامی ایالات متحده به اهدافی در جنوب ایران پس از آن صورت گرفت که تحلیلگران اطلاعاتی، مجموعه‌ای از اقدامات نظامی بالقوه تهدیدآمیز جمهوری اسلامی را در ۲۴ ساعت منتهی به این حملات شناسایی کردند.
هواپیماهای جنگی آمریکا دو قایق تندرو سپاه پاسداران انقلاب اسلامی را که سعی در مین‌گذاری در تنگه هرمز داشتند، غرق کردند.
این مقامات که نخواستند نامشان فاش شود، همچنین گفتند که جمهوری اسلامی پهپادهای تهاجمی یک‌طرفه را به سمت حدود دوازده کشتی جنگی نیروی دریایی ایالات متحده که در خلیج عمان و دریای عرب یا اطراف آن هستند شلیک کرد. این کشتی‌ها در حال اعمال محاصره دریایی آمریکا علیه جمهوری اسلامی هستند.
طبق این گزارش تحلیلگران نظامی آمریکا همچنین فعالیت‌هایی را در برخی از سایت‌های موشکی زمین به هوای جمهوری اسلامی در نزدیکی تنگه هرمز شناسایی کردند؛ فعالیت‌هایی که امنیت هواپیماهای جنگی آمریکایی مستقر بر روی زمین و آن‌هایی که روی ناو هواپیمابر آمریکا در منطقه به عنوان بخشی از نیروی اعمال‌کننده محاصره دریایی حضور دارند، تهدید می‌کرد.
تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، روز دوشنبه در بیانیه‌ای گفت که ایالات متحده «برای محافظت از نیروهای خود در برابر تهدیدات نیروهای» جمهوری اسلامی حملاتی را به اهدافی در جنوب ایران انجام داد.
سایر مقامات پنتاگون گزارش‌های رسانه‌های داخلی در ایران را که در روز سه‌شنبه مدعی شدند یک پهپاد آمریکایی «ام-کیو۹ ریپر» توسط جمهوری اسلامی سرنگون شد، رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/75741" target="_blank">📅 04:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRwWt6A1OWXNOqTjo_xh4xRORYyXW3MxBZnRzHnmjWnH7Ji9GIu4wXMpcPlUlYp2WrIf9ln39gy82W3nPp1v0BYUO4IEnWROXQ712U7lgA7smBpHuqbee7jCa_1kOyyGQmiuk6THuYoAMlrfjt63kPOWK-OXtSQhXPN2fA8CxQILKJPxi22KKKwX372wZZjQ_Wj9vdUvkJ_6cWxkXn6m5ase6ijdYS89ls66rsTfaCZd8s-pWpF5CXf7xFl_lXi5EkxLLDRmXzo8-wQNTKxUSwpAoiMZVj2psTT4ZbI4UQnNqymSrSRvWJVYgwqEqVc53jdC62HMPCxonlU6NFi-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
با توجه به احتمال نامساعد بودن شرایط جوی در روز آینده، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق می‌اندازیم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/75740" target="_blank">📅 00:20 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
