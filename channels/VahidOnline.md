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
<img src="https://cdn1.telesco.pe/file/NiXOY5F8LTqz6OIGnC3Jx77eMZ4o3p6XwWtswzDtIxaP2EWOzLnCXOxRPLB0LvGR-pMlxSBCDl0uBklPyppOH6fCcdU-Lbhhrt3zHwSNAOsV0uK4zcsHbZwXGhBq-4leE5xznJRmFx_u1ULDu0Hy3vgE5GEsJQB-Hq5AO0P5NRlSDnn0syaHeUHYWAK9m_yRyeY9pY8JB-vNXyVUY7erYte7UnXTPCALhCOMvNcbNi2INoCNXGdRxgM4BHAgGUjnzlH1PKsP-wdq95znsMmPDtT4Rn-12l72ZaBKiDDnB-ZrTWglfLqEQfIvnEV-24pDT7cbmLuBRnvNptcTQTVzSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iO6hgUDfkRU1dmgMQqWJrQUAzrjcLToaj3Z8ogXFuj72PqDZWQwjCCDdhDnU7iNtMKhSlSD559Tjw3kuPQ-bPa5WnknZF5lcycZmkVCgTEwtG6tk__W3pYSed-s5_1WSjAW9r7Gwklfi1tc4RGzZqqirLsz3yhHbek5bPzu6ObyxAX-jLIt23YAzcVFGM3hRohNG6mcK6pfVetSrWxBI2SpPELtuxH4umUVVoGFVMB2YmO8cls0bYH_616KBgTutAJBWq_qhnQjYl1_AlmCQp0SqmO7aVnakWDTx9fUXvj7FNF0FmWkhh3mPA2Z0UYDiV2vLcvE3GK76Gm3-xjL3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ba1IHviZDXsJt_ZBMK3eXey3hOIh5OaCc1piPQjBDgLK7i_f8nTxG8uYByA5dLI8YsZJ-ZEyLnx4Z_6SfuIb6_Bbwi7gbK-ppXhaGWm1mdLuoUtPuUjjjEi3HfYaZCGXUXMa_RqJ_9SEqFw64HWcJY0yP7vBwiXbXpIxljVp0IPhmwwuvoZxiK8m-FsZZhSgNxeeV3zD9GFTJmV-UKljp9ZPMOEKu2hlYIsy6MZw17rVSM8JZmmwUbiL6YM5e_2kMknkdqLnSZEEv5y7vfm1JJPCY8DpnksYlPAz5wBZYqTvfQYrN6nxjZJAcBkKRIQKVK9bSTSuz9oZ-FXM05RtSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=mCZRPd_ZT61PrjQv1J-t5oyS7i8vLJulsYj2OYQNK-nnNjhbwb5R9IV7blMAfA6eY8yOaajfcbslOAy3Vvx4GZPLunVO68gqC0glC1I92OpwtWL6YuPzMDEBwSvldGeXChzrJ62eSL8vftkNOFlHxYLcDPKqkV_u4gcI5DLMuFi5wkN6KWkvPTFv4RfLvGQhby1Z2HxOsbHw7xg143LjeDkGUikmGIwPN2seBIZrADKeBLfPGITuJDKb7YkeaKsrnkXpfiOAJiWOhNAniEj4bPg7cibkaJy3a0st5jEodiU0Gv55ZioST50213FloMg-tjkjVKd7AKXLhsM_Wkn-Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=mCZRPd_ZT61PrjQv1J-t5oyS7i8vLJulsYj2OYQNK-nnNjhbwb5R9IV7blMAfA6eY8yOaajfcbslOAy3Vvx4GZPLunVO68gqC0glC1I92OpwtWL6YuPzMDEBwSvldGeXChzrJ62eSL8vftkNOFlHxYLcDPKqkV_u4gcI5DLMuFi5wkN6KWkvPTFv4RfLvGQhby1Z2HxOsbHw7xg143LjeDkGUikmGIwPN2seBIZrADKeBLfPGITuJDKb7YkeaKsrnkXpfiOAJiWOhNAniEj4bPg7cibkaJy3a0st5jEodiU0Gv55ZioST50213FloMg-tjkjVKd7AKXLhsM_Wkn-Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r56sa0lOUdOZ1IdU0MQZ7H5HmngKnNywJnUDRtw4lKGRJxWgRDHCZ3syGJ8QfvYKWyeRk4dRDwG0sOKBi4GU4Z8H20tr1MHipdt-OdYrPDuQgMr6t_3Wb8q3V7d3hPweCjD4PzCaHU0SNhfocGbysb09yU-n5OsO_EFpSGX2UD-hLgDOgT-VUCBNczS9SXmPw2h85D4rElhx9afRZF1IcQXMYxITTG7IWHFFHZlezMcXMq10zdS2lNktikU7rzYFtCg0MPadnFAhFpKzYITsrC8449G_SaTJln0jFiQemFd5axoMZFMyCg8ydvUMOeN9yxI-OZcMievlccjfRSj2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QXbPYLEIOYp4g9rq7t1AegWNC0pcw0FhzPrWKpAAyRZhx5OPybSw6rxYc3fjp6kGzrCsOtI4lF9wfmyLHQm5qbqkuKOOBbM5GTHF8eivzA_ahBbI8HGx8W7raxeJnbIvOBc3PtaeIKkY16UwJbYKSSpyig-vWTN9oujViCCSC4V9SxHwkXkWUplmNloP5_Q1C2TOz9ppEuO0DU23Nbd-_sUGdC1438BRTMsjewgbmeFs2QcFc9ZmD4pIPxJlXYlBFOqVo7fN6qJsqzrlkEKQLA5_KFrNbXvqcVJqRw4w3f5PXQOrVWWoQhEDCZXnYcIg4-D_V6ndNmgy_NCHkp6h-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pR7E7Jz-A46QIX4xtkyOEaXvdYphnZqB6N43Khsiq0ZcbnsKH1ES9Q6n71Fzw2r2PkXzCJbZ87AKZmbba00-2cTSK4ir0jJEj8bhZUkZn87C_AyHgcj_n-REPrEbW6R0HlmaWRLi0ox-Q9XHWoCkkVitaLUgDzHN5lYxJ_MSSyf_yJwBqDO0lMtQPsI3bufzEDUBtweSM77vIolOb4y1jsiyxfBP7b04__ZYliT_JYgftVg-ke5FwI3-hX5RiWBmdd9XnHzUjL87-6vAWy-L1kqe2ahFJkLRPg5OQ7NmfULQY2PUFFmCN-0SWDeZIWD8mzA7621vcQ461vW8anhXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=iS14TBvG1mQlcn9SiE9IH53xZvvLzlcDL7kJ_OdFXU83xOoXMh0Qkw31vKVTlzzNwv8QNzWGIGctuI99HxRkjeJVCaavVNdzgqXMN_enwYvgfWNnUqw2KhP1gV1UTP_U1QiopSnmu7VmRrG7J8aEx2ePgO5CaXC5h36lx1jNlac9_6-ffRQE6LF8sZA_jPug2HW2IPM_UuJH1d6vzhQhXtIUUikUE2ur29iyNyOuvligt9CAhmMoU_ds5oyI9dH6FULrV4yvvmSV4Dlvmq14svTx6OGMZWgwM9GtTOFcBtJl9iBD7ZyCe4ujcxZ7N7BCt67Kvj7KnCwjDL9IAOMlFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=iS14TBvG1mQlcn9SiE9IH53xZvvLzlcDL7kJ_OdFXU83xOoXMh0Qkw31vKVTlzzNwv8QNzWGIGctuI99HxRkjeJVCaavVNdzgqXMN_enwYvgfWNnUqw2KhP1gV1UTP_U1QiopSnmu7VmRrG7J8aEx2ePgO5CaXC5h36lx1jNlac9_6-ffRQE6LF8sZA_jPug2HW2IPM_UuJH1d6vzhQhXtIUUikUE2ur29iyNyOuvligt9CAhmMoU_ds5oyI9dH6FULrV4yvvmSV4Dlvmq14svTx6OGMZWgwM9GtTOFcBtJl9iBD7ZyCe4ujcxZ7N7BCt67Kvj7KnCwjDL9IAOMlFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GLk59rmpDlVj_yLVe9TKzoDW3wRoAdymCGGVGvIISXDv56jQOSt6pHsy3kH3GcVjujwm-i78qn_j8__RkOOdIt6vtfunT5bWtMR2d6_O4hgpzs1CrAAUZP68JjAbX7T8koUzaCksXqNxfM_cmTKL63YEFctpcxMJD5Y_zE2AEr8VDegnPxysK7TFDdtoB98b3HtzhAvKFF_j22BFDwr_bdzxoHNBF1UD1gvXoBZ5tv_jyug586o2Uz_lL5CtKoxf3fVNHqDEvZ55MPNX3EW30JUKjs7VBlqAyiJ2dPfMX5n3VgDxGsc7H1RyCR8AOHbPdTGpwoBSR_Bs7hS-4U57hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j2XydzZR0mEYYxTg73I8Bph4ypjxDUS_EfSObrHV3tEYlfkXCOMQWMkZY8zwUCJw3qOerUqCtXUaC1J7QV2E7z3gFozM9FlaZzX8sfevM_566G-CcJ5Yg7ABEyo01vpmJfN0B9SRwxmkf96aeOdmLAqCOV1BNAgfG02obPELSK2FmZU0MoefutZjuRE2q4ETcjKrk5ToRqiF45qr1QEGMr6TIF7pMMLanZso6auxaz_jKn1RTBOusO0mLBkFQgWuEt4ko4Tf9uNcrv7HdUvNsCwo9-ksAJ1hm3GfLFzUYA2zI4LLTDdAlh5vbTstA8F03d1Ab8LLd2SsX7DRL1hSaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SkKYxzUR8fkLiUBb8aWKJs705X9EBkR8NgSwiOXTAgmbJG3okJujiFh2rNnByxaYJSQtUxGbzBwfvLW4p0oMUV_FFL4gbjzZSK7f6pLZ_iCFuHl-JI7iXK2skqXvORFUShZFonvC5bI6g72WoG3-KoH1tTc1BlyL8kphHLL59whT3do_to8QzMec0I9UJp0kHmveo1ncVWyRTukiS3-UM7g2orYUkFXuU9dmUotJxzw12dRAUppIcjV4s-xDsYIezP0MJHIjWVEJiqYVeakfh8T_7-YxxuiZYfvwDOwjkIqGHjk3INTZWSUs5hCtildNshkKJ24B-BoAY-wlbURkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D4m87Z5o8tdk3xbQ142AS7WZU-0wFfP-fb162ncP8eEIf_xPbFwJtZwB4glp90XxAZNwx10ap7rt49CgppQ0Bfz3GuyVxMkdmbKNHPeGlkUW7VOWPtHNDFUJV47uMETrdS8UTS0agwJLiSqBl_2I06j17BIJH4K_oN1wQXPHFNs8ucg2h-dD4gSRUsrEVgYmjQzW4mBQze_rQZSJUsyldo_dfFC7y02KoiHQvU7EuQgvAhis13V2NnegDruOxUgCQFy371zceE3hmwmVoAYgUOAT7TYkk38ZdAaYD0yfiN646hZeUwXIn8bZdiKhtBF0aF9v1RzSwJitbniAzB11-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pb0fpsBgkRao98D3IIE_hoMj5eJ7mzVbGO_nciJ7-u-Dqkiyeen5ZOyLsrUILeHz9rq9HLscXF-DNwQQODtOxecyLY1r1_SPsXOYP6eTDnehPtgZl83PFXeaInVPZw9EdwOkmZ7O1weV7_H02NV2SFIEvNWWeVtCkC6MfpWA4g-HqiMjZ9uUZo2VepWbevcn7cpmE8pwDi_aCOLdoxRCT4ivmn-s1No4UaebSWOlMSkMfJoJMVoJVWvefWOtjqhfsoh4Ilz90MQed9xJBRC3DVnMkJhznyVMjtHqAHIhgHKfoj-C-7QWJmlLMvwe2FzgWo4x0GWic06S1DBE6l1QHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o_ygFBkQY-w_tYWBq9M3dGccCYZd2d_Xt_MZ5PmRt7hArBb--VnwYZKQBytc7TaE1k9A_PbUCeLSbptMsRinVpvCrEokK7PCqJ9Db-e7Bi6Q8S5FSuk5dvj6AnuwyQYphiXk4VjEr4BwTsgYzlxHH0jqJg0StLKJcea5nyGPmnCHCl3fiqZDP-BmLTZC6NObYPwBqU25vvh1oQ37N6GARiJbYKeoHPV1zBEk8924uSJ2-YHHAYD41Vdc77By5rQufrkFFSp_q5v8fbzwivq-_ur9TbJq_g1vW8uWr9uC7OSRvowmfLYTx1Bkhj6cR-Q4inlRkRAoYdx3elwCyyDO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=oRZrGmepw5m3DL0DqQTgH2arXkmFYCIRKSij8SJNRwOiYxW7K_5Gy3nMM3nhp8zZgFmbayYlFdbqp_TRjWgfCylfx5nSPpvY5AAV_ffXMiO3G6OrVOxZ2-iYkOxt_Nq-SbWLJj3fGIZNSYAVFrAhBhzJG3cQyTR2qu3nSSR8mbtleh3ulJjFi656Zu0y8_qG1ev6lI0biERJWbgQkNta9cMljRZNTWTCt1gw49YtcQOSUmLkJbHH6MzvV8lqwJZHhWGRKKVLxSx_qZBMYuy_mutdOofNV19SzCzUH0bo06fZa3f32Gpnqo1TYKXF3-m-LJPdsj_YCWP7OhEfBMigBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=oRZrGmepw5m3DL0DqQTgH2arXkmFYCIRKSij8SJNRwOiYxW7K_5Gy3nMM3nhp8zZgFmbayYlFdbqp_TRjWgfCylfx5nSPpvY5AAV_ffXMiO3G6OrVOxZ2-iYkOxt_Nq-SbWLJj3fGIZNSYAVFrAhBhzJG3cQyTR2qu3nSSR8mbtleh3ulJjFi656Zu0y8_qG1ev6lI0biERJWbgQkNta9cMljRZNTWTCt1gw49YtcQOSUmLkJbHH6MzvV8lqwJZHhWGRKKVLxSx_qZBMYuy_mutdOofNV19SzCzUH0bo06fZa3f32Gpnqo1TYKXF3-m-LJPdsj_YCWP7OhEfBMigBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn1vTb7Opy7kCAbTRUc8DSt4KtnUZEg8G92UK7uJp6nfWnFd121dRj6IS1zQqIpZlv7wiNYqkPU7KD8OPjeeeD7X2-s9OZf5xg-Oxlsle941BsXmZInQmA79Eb0MN8co8mjo9D6qctDGXrZWtre4BxEFFlJe5J6qNKd46E8jGMpXIQQNdMMW0ho4zDh7IBWBuqGtnndBzeVEgysVWW0S4wzMrSiuFzVXIeR7u_LNBXutvj7HAYmHDKzwufcUHnpo2RHjcYamyJ4POlQb_6METgxsZ-MGhG4UjD6y0CB4xDK8BkufN8Ds-juCnnwIc5mbOpLzWppxjNveth7JGJ5ZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzHTJcqoCVgO20cbQViX-YFpsZ6iCODQ3_fvgt9UN2Kl-kFvKeLNT2LliSrdtMfJJX_T_jIcly_lOqAN7qcZSe6X-OUAnGjQqC6ZwYWOLgRZFEjm3EHJRJ7gZUphhRN3ZM8cr_t41ltScNHj8H_NDPUMTbd8Lxu18fcyRWZQupLHGMAdrKxC2qD4p7jL_J8YueQWsGLDdlDSG1T9iwmw-K9nMB8YmEAExx2Q1tIn9-l1MckRVUMMIXyrmt1WHUKs-wRj47nvTnX1WHw_hWPIHI1nez_Bj8iBk8yIk4FUmoCBUcbF7XCegWT5JMnzkqPFG_L4aVJIr7Etx9H5sfxjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR84kqrrQSdGsMf50F7jAxsuM51MTL0UA32Hv6N0PKzoEG7dUWcEmVHav3MQQSemnycmnphHcFXJu6z4Bm7Q0lFTrKqbnpzkHGs9hlR8FB5jQ_3z1fsPIknxMoKXNbspe5e02PY9kobRujv_GVoQgqu7QVI_567vQXX1GkLSojUFDSwIdAyOlhslNyjAfx7wg9I_8XA398no4zVY_yXiYDhIpPwVhaUcyB8aGDo-UInAPeeA-dib7b0yokyKzLKTD8jC7gi4dTlE_pLB9wRkejAqTb7gBqSauIB-9YRpF3OYH7ZS92RJ5rRSidcupUcG_rQaa1RvI3dQDz8eQxlYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SOLJw4TI6j3YwEyhQqihEOwyUs0aaqQSorglqSEFqtJAGRAwUsQO42Be50md2MvbxuQbC8DiOehbaAy6AX2zwInkQO56WfD0aFAT5vcsHppIUovU85tV5cue0x4R6TvdpZplLRMxNpesVFBjoHNhMz0v80aGhAZHf6VdZvxNeIxpYqeh_tBFDVVn9HEO_RS_5JAZLEeNKl-y_AVknvTZsbprojl4alS9_u83S6M6DgjLtqRYzzpzd6472235Pq4XuEHrYsN5zpfJ0hqAiycvZIm7_3Yk_ZgyOpzaADFtymfm-GSEjtPeWxX9wAWpu_yUf1LIKuEm_zC816l9QfoFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cuJQyPuiTii_V9kknBmNVqWdRA4pTKWtth-0R_h7V1LEQOJ1Of2cqCYK_sZyrZRX1LU_R5WeWv6iwtX4ocHmYHXSFDivnQOEDi5UMJP2yjd3MVubrOxGD-19Eu1nEL4C9Gw5kD61WIQeTBtgUvhcxwypgqhoAGFtOOa3_VnixTNdjAAgJ4vZ33gJO-AQGeLuDJqdjLU5FOw_ybpS7wGSNeF8F1IE7NtWGR5FeF7lZIUcshm1VkyAZJexGezeMxDcsNolHl9mkflZNNYmle5E6epdn9XJtKj6iL0f6ztgndOegoDjkuxpTmLr9elBldA1IWMvrm3x4UQ9qG5oeCWBPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSUFYKeom06u6hbOVpUaMT7S2ItieD9r3Zgf5ElcgNBfdE3tosv338ngLg8so8E25vTLeEuwCc-UnapYfEOu14ok7ikIH0d-nnq2yolW0NgkSDFCKB-LwwpeLOG4F0tnl0StpmNvJPtX8_kV57pNY39PVpwB5HtmXfmbYjRUmOVxJQueYN092aleehytAXWmBQWXeZVZGyqYThev033jeeQaNffgWnS1Y7nWhS4xVqtfYwG_KIiNKkHVBphUi1S_YxRTLaTKXyKDESPqzyug56EFshCPyBJ3hnzIis00208h6mtxTQ8_Fhb8F2taNG3Qx7gHLStTqMNRjR0cqTkgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jck5-V0n_5179oUKik49424i2cwaniqtkAPfBewIZoOGB3oTtVDJvM_yU0i5aCVl-tvALoQWXUEkuy_vLNZnYTmgA-fz_O-Yqka__GgKoswQagNkt74JW33aAh1Qo5r5SdYW5aHqYsHnpg_BI4o94YGfdH3BPsn1Pk_bUDsYtRhFOxFJOuhcS3MvGYH3nR-ZF4CsakHxE1Y2ARgfcikIWZNjmx7scTJncWngjIA1jJPaAks89hCXW_8UJxGBcwJBkMSKFkaW4SctJY7dtENlCnFOOrKZMUXXQbbvXFMb01oSBQYTAxjdwaUBPk4Ia7rRxHo43TVTQeRFc1han0M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvFSwFJ2xSsJ0_-eZ3V9dXKUa1JTtFlOOCGWkH9_m_WB8D7Z31h1or9UODyRSKtf3COwNBi5FNjeuj2VPC37GzXqDx0vP2O50_0mST5_DSxoDlcJsJhZQ67XaJsKom8bYRmGvDhlRurn0vTnpax0Tqk-SIIfaCbQkf4yYEID53BeVQgRF33SzlSWbRJeXGGzcjsWeEf5jVHm1bMpq3pmNUsefvIdZHKUEwY2nDkb2n2YraftqzuGwg3d0K440DhNCIX-Nyx-eNoh5Uayq21pY_0KBo-JsKwpywdZ427wLn5Czp7kyMEf6e-5dJdvBlTOsqFgCAtHrV-2xngTSrOmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j331t6Lpb1TULAVFe9V0VV30sN1U2ZD5DAUBADcOmKZqbQLhpzMHqjPJ1YhK_jE3Z4HHedpf83prPGI3pfr5HoQ3U7bwldG9ZR5p5bT_HIxPewzxE3DnOZtZzNCsVqpKw1I9fGwozJ5uDP9yYGRqA01E-NyOWTjeSV07Q5bKdJ5ht7OpEXkmxIBxIqr4eFuvtgur6WgczfrdpKNiPymFQ8yA_ehTDrf37zwZySEqLep7HpCxQo_d0pRMbClduo09KBR2O2c5fB2_WmhDWdFtYpuUSzuWOYhS7ALGZ1s4MKkbav0rXI2M9oiaIOkjMFD0GNYylcGjeNvtFOZ3KXstVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuCrLMzO4oci9W0Vw-IhM2jlEr9ENutJGQZvP-5PNUSJCvAt3yCUK9FxYGsg4XG1p6P9kHUtwZJca1U_cYQCTg9O7o1piO-wrLxIhM1fgGyNtHrNLqTOps3AHbmEmWZ6NvFSoT12szFv3ps037d-wZ4jIswraBbeBD7BlqqGgqivLLF0oGLNCIb_H9p4CTOg9fbv6aJGesf3ZRqcapQwd5nid8VjH9rhrVO0RPyxCG81v1Fr1owtacVymAbb70DM-m6LmYeGl7MUj-QLg_CVSBj_hky6pwY41BAdbGiUgUAKiieBEU_XVtij92bP5R48MEmfsSkI3BxpLhwWkrz00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM5M_Z4hH1zz0pCy62_ihEhtTjcKRDbraXwUPoISIZ-Hf6TJFeiiHYE_yTqacskTbddRdhFHMzSBZmQOK1BT9vIJ6Tve3ImIKeoU4kBuJdxf2qkI-t9z029JG5_DAOlK9RlycwMo0zm657brdp5LzdDU7qjlxFmToyjCcnQkxuSwuRNdrnSlnMB31oU3hK7xDy22FecaeFzawJUyrIyQvBuLvgTk2HvU8LFCkGz-eZZpzm6tD86DKt2AjeK8FQcCUDOn0ESE4fvwvZ4gkqWTj1cpy7QeukXPV2L3kQPQdIPO1UsBHkCrR4uXaWyPuCHJ1gU1Kc-LriEZ1wimmQOzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rg-IsBvKbRb-kMq1pHvhXFpcSU3kZpbFD8HVqE_TfGsUd-2dK7_UasZIrJGrEzsmhNG7yGW1pQgsOianoj0eW78AgfNOSxGEyWlVdT3Iz3EVvKHNvABbAb9b7792G18x6C1bNVpEU8Miz6x3zGEnY-9DGwhI5bMUwy28KOdNJJ3QXKbE80jWiZ8cK5TIyuLmPUfYz72BEUFw2RswCAPw9NDGweWtTriz1IhLMnF6yHR2WBh0nR_N9A-2zRjCZQw7EO4HiYZQ7PH-vRK1I_eugp5GUVb34Lq_FWyMpMmBX_uOpuZlO8xicijxC5cmBtkjgviJ5F6vPwprQ-S35NdSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZvBiEg0vVjHucYdsmVXG9rB1vdvmPrGkHxblf-eZ2VplHQ9OdRbMtTIYckTO1UmiqJw5NN8ncI7dvnwBwGZx69TTOezP7tiLkKTEuDLpjyoiEfht_YY0feHz74-6ntmKxHPqnxu0MUMX68g_10zniybHkykwvKvd1tMmYAJpRm3yCXpwpNhkr468rsFwQnR3yybwEh4QumTV-tn1uPlufCbR3K8j0I0jAKL6r9bT5kkAv08bz_-h8xiwFZ3Mld3NZgphs6N6v-jLwUKBfhrfTEa4vjZJwMXG-hjqIKkLg0Q3LC2VXORck-W4f_S0_o1w2fYrDXdZD6mAiipPEbClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goM4sFPjfsHHoqs5WJ9zF6O3BhmckKkDhwzYJGaGC6hjqH6i6KkTwin7gDVcUlTm8JlRzg180Hf_QSZHD6qkJBEnqqV7PydklroSAZKq5t8BcehEh7kNGjRhx19RPdkqLZ49xUJYHhjr06_ryszck6guazGgr83weIhjHId_Q3asrXhvQlm_YmFMswHVqiPtXYwCDAk1GYlZUIpHKpwcRsYG6opmywi-5yDJDKnLMxMxztNbLg_xfKeGOK9gxKLySxP31cTXzwIojVL8cVYjIo8tzouKpyDUhabXmBiDswtes113SHo2-Oa9APjk27WG4CGnvfMxZX5M7rx1FWpVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zb4paD0WXOwN-WMs7X3sG-ky7ZA4ver2qumL8hreMu1B6dnS8h30Drf3OnUgbI31NCi2AI7JkMckre53TkYLGwnbu5y6qFrgVQL-Z8BLnqUOWtZ-0NQDsmnw1SqB6VyCmtEPZdhnT2qLeumFYb2Ec_0VWSuCN2eYrycg1CBdBZBGXO0owDYuOP0b1qfeAO0sikHmM943xDXmRJSead3rUl7gPAeHmLreAyW6IdZmX11jO3RrhqO0Rmff8MP1c8M_J_wIJEgOnfx0de4pb59migAXa_U1TpW449pvHLL6SOArMr0lPWGNmkAnNdhLVkpynV51Ok_oyzsAnvOsW6ZEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHoLartgOTtjaHPSaQ_ORo6R_XdXxyzUf7kFiYyZrPO7mVe7wQc9DeEOXZ9buG5T-mKewjEZ4zNORAMdPRCEtEXp3b3dVmaaofLhoCMuRvERENEKCIuYWAXpUv9fgooWxiWTvdx_Cnx7F78TgVROf8lYQU8bZ1eW5mA1aAJv93wSmsP1hWJmCkE9pqQYdpO5ieVA708uiprRc_ZJUDpbV6d1peF8AkZkK2HnJlsSURxgMfWDr1WEnW3p7RxIVm-6G8lhcQJXqSnGFVAs4bkFuwbleNhZpWMDHeOMuS_Z-zsV9K4rzMW1lNBA2vlq-XgwZfKPIsuB211gnFKHKBiL7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sSd_L8YnobkGcfHwLnH-woRDbvrTMo_sHCmkA84RQnzynPOdFesRXufiSKRBceM6b-McWabEfPHZEJ1BW_76Kab5CXOCE3GTMtjUZ9btGcbCh0p_R33gc4IR64wIhMwSihbWa9Kjb9bifUcZe4cnOaFnxcy9ccN0atahav62LMpTZYKREt4WqO725-E4Wc0unRzCiFNWxBhGKltMDcOKqVkRR2yIPaITvOJzvZFZ0ZAks_axMF09Nl3A2YOYHkK2WJ5l2TELZee2za4_VDnaZj4w_h9-wgfbdeKzd5uwESgiYDqD8uor3XCWghQiV5fZoF8XSiqHe4hDahfyqXOfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D-QxY6UeyRPYlOGDiHDUUMY0t1SV5B4s7Ux5nlLftJq3Vsy4FXyDs9BzzseMgakQVAG2_We7N9xZGG-SEPhjBTIyIsvS1WfP9Lu0HCgR7uDIWFdOIazCmcf8cxyPbgpKT3KoXickhIGPZpq-nmkilkgNzXhs9066S7CDR3l7wejSkYh9IQoIgUOLJdbPEZtdx0QhTTSQ34L4qd3QI7RdBjw5yyp8d47j3b2bETnoHFJ7YPlUVT1CdB1wzyMBAy3TKmFx4FxWRTM25_o3M9VdKXiqUxS1JvAjwqfHfD2OaRGO9I-tB1a0AEnhM8UcwGF6LGv1DuUKIQyR7FjRe0f6FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr2LrNAMilsibsa2-CUeahdIf3fuqnERGC0J6bnAX7W8406nntbjkudrH3XSw4DKzdw_lrbG92PBsaHXXz1-8I6X3y-mnb1NncLKAJHSf2mz9icQ4vSH8EuehazMd4mTxjhadCeR6uArr58c5jnfROkWJjoXGWg_puOVfR1y9GNsJJmOitOKkD2ZuHWZ26M3_DMWrbdCKU8ho8uA-szEfUURBOoKeHyBRCnJA0JMDeMEwGHoqO2LOxcBIJNWIjnMPGk7kkQVwZN_U14NmVKCZx9xnzg46mJpwuvTHYNFY1UWpfKfM0Uke_eJpEZgikTji4LqtqDrQGYIUqYcQYgcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe3nNI57gGASx_s8_gl5qr4jCfMyq-YYT52ohGCmeNPOGl4mnv6dZV_a_8RA24T3Jn3Kg8eYhtqpJxYyVqYXEtC3f8qkaj1TjliVGke7HdEVOcP17v52a4dhwEdBO7xTefCPqREdwjJ7LZKoyeD2pq-PBpHLE_0pAD2swMtjuvj8b09_hKA5kDtVJPOZTEClMmgjn22HbWNzpVQwAZfxs-R4tMbKeBkxkLOc9-CDih66TPQalWDCykOTTcUQbMIs7lKJluiAivcTFV6pEXJyfH6jB_Teq04zaaiq17yQHvATnyniA0zPrJErVOjy3cKa5kgZsLsQD7RVn-uBE9ds7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S27QxhKGrkGWpjCBEq4PvhBgby-fhEAI2_F8s1E3sp7KFU0pQBIx8WzVSjJdIs_32HcYgCp-Tr6NwzkRVqAGQmHkepHHMx0smSslr3-EIlaaIS5W4RbLB06j1ohUBDlAO91jAwiLIartZoF4GRGc33_4jOcNppz0ipq7rnq9N0W1ZZEAwMGJYbo1ElcLaOXt59kuqPK_AOrba5_AyqYZEIxXUaEB4RYFNg8fgVX04YwZQjPPOJt1hHnsRlALYtS8FHxEObl_7mGbzqK5VavomlEuiYADy4ESje5e9mxbIiF2K8ZSFZ9YGLxD4L87RJRLVQUIH4VlvJR0mJoIhGTIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgRimLZFYZYgnqE_gNENgg1noDa6fjZ4oVDiuheAUK0ve--v-5-UjmguZRo8fLKLoOoCko9RUY8H9LdTSX1qIph-x309fjSI2QO42lzLbvHfqVrC9fauGN2h97onTIRk7DnR3NH9iqsdEJUcqfeF8Z7KFrctRABXGld4jq2rdnVO1mAakpGgBeqwahXthcYOFyIEOYzxeAsiBXtPTrAd-te2klKzvEtG2bjlREa70zr9AURLfcuKsproIdazAB67YpzvEwrgOTNwtQZyNnfLZhATxReX_gptd-uLokRHTeVWZXCXiQ1yt4OljD-ZTzFyeavKfTpES76Pc6-Y5imH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=shIHMV4puzHZOAspgBvSCPauIR3Vvlzjha3aqCao9Idvlx2KBNRcH08s8slijunYVt-1iZUEMoiBISr2Oe40nePqI92cRo-mi_ss0oiGGILTVKLl_n0WdkCZiiJxEqE-Ia7h5PjmGBhj3Zdjsq3g_N-A5tszlBM7OK5-Sgg9lscHOTR8FMjREXmlXIGbbqRPWMrFqS_j7_rUf25SX2lovKHvkDY1W98ILCd5ERjmYtLebyWkm_2HmDy0nE2CNWzOCdTeka4RuOWujj07Y-bBrywRt_ZddMNLj8A_YyhE5ykGso78uBjcLeyVPminRUwglM8zuYJpwefJxVWdO-wx6IY4gnJhry13bWNjF-aE-ftGhu7lclDPMvafBvt-DiiBxcU6ETvVuq9gOyZvNPMQhmJguq_A74_9zpt3N98moZh3_Z7vpNKxjIKQUJwmgJA7JnPilmzS7Y0fDKwu3KsLHftF3HhdoEKL658HTujV5ogoRuJCqOyyrI78qa3kF0DGJG7byr7Dyo4wH4mrV1nyByxR5PL2wGbedFiSXDxktKRGNLpRO1W74ngOrWPKZUiW7IBt9oxxXFtsEFcpg-OYvLY51nvefAqbS7QHWzyIYRNi70Dh5BI58BdAxUJ3HGsElYFVzwTqQ_36MdlOC3fhN3yx-Q00VImsaXXLaWUDJz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=shIHMV4puzHZOAspgBvSCPauIR3Vvlzjha3aqCao9Idvlx2KBNRcH08s8slijunYVt-1iZUEMoiBISr2Oe40nePqI92cRo-mi_ss0oiGGILTVKLl_n0WdkCZiiJxEqE-Ia7h5PjmGBhj3Zdjsq3g_N-A5tszlBM7OK5-Sgg9lscHOTR8FMjREXmlXIGbbqRPWMrFqS_j7_rUf25SX2lovKHvkDY1W98ILCd5ERjmYtLebyWkm_2HmDy0nE2CNWzOCdTeka4RuOWujj07Y-bBrywRt_ZddMNLj8A_YyhE5ykGso78uBjcLeyVPminRUwglM8zuYJpwefJxVWdO-wx6IY4gnJhry13bWNjF-aE-ftGhu7lclDPMvafBvt-DiiBxcU6ETvVuq9gOyZvNPMQhmJguq_A74_9zpt3N98moZh3_Z7vpNKxjIKQUJwmgJA7JnPilmzS7Y0fDKwu3KsLHftF3HhdoEKL658HTujV5ogoRuJCqOyyrI78qa3kF0DGJG7byr7Dyo4wH4mrV1nyByxR5PL2wGbedFiSXDxktKRGNLpRO1W74ngOrWPKZUiW7IBt9oxxXFtsEFcpg-OYvLY51nvefAqbS7QHWzyIYRNi70Dh5BI58BdAxUJ3HGsElYFVzwTqQ_36MdlOC3fhN3yx-Q00VImsaXXLaWUDJz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=S1nlloR0EidEVYjP6yPL1a8CGcGu4XCASLBKKcjLg28xbu3ZHlujM64b2jm-xCs_GyUNu08c_EhPPhA4OPqc4S8Jv7bhCEbQCl6x2egh5WtdWXhUOn-FFNASsWPDuULv7j_eYv95GclR0ls--WdboBLCe12Ej01yTNVRfjtxViY4THo5_lhRn0tFx0etkmWfoHQ160Px7RbEC46P9VI-swove-q6OEL7FOI1s-ild_Tc9tLEw_d6QZ7XJHsaCMDVsjXJ7QgVz4WyXgw4vvnxt-OtqA0A9KwbV0KDqzRgS7MnB9p5VZje9ACkwCf_RN8DPk8zKHew3L3KjNu65CZv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=S1nlloR0EidEVYjP6yPL1a8CGcGu4XCASLBKKcjLg28xbu3ZHlujM64b2jm-xCs_GyUNu08c_EhPPhA4OPqc4S8Jv7bhCEbQCl6x2egh5WtdWXhUOn-FFNASsWPDuULv7j_eYv95GclR0ls--WdboBLCe12Ej01yTNVRfjtxViY4THo5_lhRn0tFx0etkmWfoHQ160Px7RbEC46P9VI-swove-q6OEL7FOI1s-ild_Tc9tLEw_d6QZ7XJHsaCMDVsjXJ7QgVz4WyXgw4vvnxt-OtqA0A9KwbV0KDqzRgS7MnB9p5VZje9ACkwCf_RN8DPk8zKHew3L3KjNu65CZv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tB2Def1CE0pSZqehZVrqZWP4vRK0gELPUJ7NAmaLpWFvve6Z_Yk73ofQJOBC17N0d999S9FIjvwv07NWIo20blu0P2E318tyvOs3IgbhClFaBCVZu9DG1qPuY179Xm6BeHvKaelwybZrJ9NOMuti6Oh9e3oPCIU6In2yPk2eiRFY8OcUh5PQZ5A6-Fetg5Ya_lpI0IwcbetVFepxpoqniqqBidl8iseD9HKFf1ADhP3BFbd0wF7ST-APUxwLG78XFubkzZuG9-hnTld8T1b3BslKg9gRSkRPkcIyO_SQMlhTGGlyFJHp-zl5-XE6pYhzqx1lXk9RCUnajw0kyFyHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MS5FAzI-yAb7KhnGNhaoeeIQGKT2ll0NlBi0axrWniRcKlfWlzdVll9zbw8Tvm2E6TEkfoPvvCasNXNxSluT9P8xFesT0pNbpIiT9FCYW8g3rh4_QrKyHFYLkLVBzJOTZHFOCOvcD_5TryX9W8RzP7Oy2VfnSyU2ARizTPd1GQrSvOZOU9wAo_U8w2EqUKsoP-1vhgFU0n3R-_OObly-CjxXF1cao7EVw14vrpZN22CRMdKJk2TqnnaKFzvlxfDzk3IiL13LT2ZDm33O3dz1r6Vz9BlLMandDZPq2TCHRFySWqrMD38q1Fz_AAMm08vpJrdxAGugHFSLac1xcNZLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIsQUAo_-LsYrXZL1YD2TyZnacKNQFshxfp7R5ZZ1gvr8P2q8zh9kPlSEUG862bfJLvxrFMq-E4eNejxozxtCJSV0WKhs_9nBi3KLXTb2mSKqGmRZkb61ONGBbW_MYehV0fDrMP9DtJ42_mlkp80j8tlaCZIz6k02_USrBOXPGDYuikRWvp6wVAMdAvBSLAi4ceIY_RTG6KXdvM7xTsLqRrjaD9rNT3i0_ufJgeCmJUlXVG7IsnmPUaoPEPLxFb5BRWqEVZ8mDAS1Gt7LUVMapcytgHjwCCdx8JwKAEmG86WiRGOSD7CTSu3376eqygfCV4UpFoaLh20u3_-CJZkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPWXEfDTwkJAMBL83lMC9_RNG8uYv4ClIWCCATH_OEqqGdk12fZ885S74q1MYJJDA03knC35k1HJm0RND-M_uLzYTspi0ljK84MEpwVuynI5sJydX7D27lKo2hM1mARc9fS93YUqZ83vf5X9_Q_bEtuX_3G1NuPtPr53rBgVSAegV4ZFHNfdxr0-sUjdXZElBUq3O6h-luXJCAE8AkoptOyZYhSoKwM8A14NverJJG97jGAPzJQAZzCL8FUCXf8MVj8ddjqI9wsm0hI11zdIYKOe8SUTeD71DhF9cZOnvWGFpZSgJW7OeLufm98C_lLrej1NzaKspXkSaKllAwmrUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_g3u3igcGIY_PSaBMTRnM1QlMsEXpG3mlU3zhdN0riJ-_qZ1ukanWTYmP3rw63lyEuUdQnnfEwwTZZnPmdJgfWkMeK5DflCEwAwMz-2HAtKCnOaYJwY8I4VYN9ttbTZ1joPpPvyYr8WX9lUwTn9WnCLKO5e9aUNHTKUMEdyXLn3UYt3eb81RydkK0hBIzFsKHXH-s1dJeTTVCSO1TBzO5mOzHeQEycQ2Fel3M7Zto8or-_Z-RWfu_TGEUHW9jVbSET0xN7U2eN83SVynRl6B64aM2tI_MspUjp1Jtvpot3FhkWQ_9WV2GTVs4BzxA2x13VQe-3XQZhQF-BuC692mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp2D9zAdxVegmkKaH5Z5Aa_X3c2Qk88q_aTknxnAfLft22sTceHMULCK3DkEp_yihY1BRR3UGjbnvVaFiAZaBl3T6aNKq26-ZL4Pz-k_uc6yHm4S6oZ9F3lmlWZaIeZIpu_73AB9czh3jKZlbG-GlDRDBUMdRn9ROESU3RfreJ_0TgIcH82ehTu4DmsCWicJ8ZYXYnlS0UtN7tSmskedvMjPRx5rLLeF1N-gt502R1hO_OxWOtXK8I-4Fbtg_JzbPG_BThDMCcjTdkCNMY0OWPuRETSiYQb5VN1wkPIW9oRtTx_Io-V50mStVy020pfOLYXvnrclhl_Sanc-BF6Mcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o58QFwb91a4HhF_eRc8PzdEvC9obuTUt5Jxy4cm999xZHo6aWz_E9KPm29Y5jXkoM3kKiJaXPNUJrXyiNY3p-PlQCuxqohQ3YgvQu-XKqiMrBGmSzbKLpldw_8751npEBnMXYj9nVRKaCj9rdh4C1XeBrPTzA_iIHR91MatMqdbAWYs6aDyGIex4DoCg5TOTNaubEq12cGvhf7TwNDaEDtN6sLHjYPZJ88fnd4jKsImdPyeyv5ezxMxovR11TS04X_Brn6_dZfsnDb4WWfExLHt3EnX0PzPuetHlMOzk6-gsgyUnBUB3KE8pdwTmx-y0ItezqJks1e0lWjwooAR8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=J6xh-JBSXPiQhBOu5KYFFjFZR_kZAJk5xVTvOq2Q8ZR9Mo8KjdebcdUkIy_l6FFxIeTf2UNSkGyjRuKiTZ3FlSKQRERuM1msJbsyZY09i4LkFwhEAzMha1kI6eXQJh5YQT1eGdFd_ccIchi20ZJOJA_MvsDjSX8fgJ4q2h7frT4S0lKMFjYfL6MwDZyQaj7sQPAzfnGvdUCQoG6403pwJ_4g3gv-7PQcDRmIUgk6FnKx77mOMw50OmWx3DTqJ4OlbvgFikZAPhOct8XE4ufDyX3kW0t9IWArpOgpMDkOWnhPV__OA-ciPXmQDE7gt5SMF3h29HkrYZdr-ctuZ2CUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=J6xh-JBSXPiQhBOu5KYFFjFZR_kZAJk5xVTvOq2Q8ZR9Mo8KjdebcdUkIy_l6FFxIeTf2UNSkGyjRuKiTZ3FlSKQRERuM1msJbsyZY09i4LkFwhEAzMha1kI6eXQJh5YQT1eGdFd_ccIchi20ZJOJA_MvsDjSX8fgJ4q2h7frT4S0lKMFjYfL6MwDZyQaj7sQPAzfnGvdUCQoG6403pwJ_4g3gv-7PQcDRmIUgk6FnKx77mOMw50OmWx3DTqJ4OlbvgFikZAPhOct8XE4ufDyX3kW0t9IWArpOgpMDkOWnhPV__OA-ciPXmQDE7gt5SMF3h29HkrYZdr-ctuZ2CUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU7-vB5ps8kXz3vaHOfAeIVEHwNXP-PqgICbeGSSxJNRyWfQq5D6-MAqzXfGFKZmjHEl8qs0mVtAEYDp1UMWcfVTNYc5jnaibUL4KdCYSnDS4-5mEjrIMXCabyxYlH93IT07tWMRQ3vzfZ1eu2aAd0IdPsj2Mfj8omTgf8tvclhNxJIxbbbXc-AHw5uVflXU8WjVr7HYlDeMFI0UOdARc7wB7LtutAZrRLxvf-8EM2gncDEjPx0km-6rCdCKU1i8SW73yISe-mforG7NS2QcOLG2Y2548RHOQpBCbeBOyDymUa2xoHuDYxrrB1-D-RIfo1K57-OlcfvO1oBz2DBJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mnkeoSgGk0SbRZjAGNMzOE0xuEhm958bP5u34OCACL4K-9hQoTQUAG9VwGlJpCQMjMvtfxM1zGlS_udnyEimOAhmF6ZYWSwuCa-JL1Mq4qNwSGy6TnLWXzKXsaj2mo6pPfkbdMlH7WaF-S4NDUhAvggFnJUP7ZDhhU1db08fXOK4lk109Y7NqybXBNsBmOLkPs_07iS5JB4sdnlSHEw0T0aiSH30hArBz8jiSFIzmWWDvHXau5ei6LrhBKKlSwrn887F0ZzOizGXtfJhF55Qp_uH32hgkx0Lu79ZI7gTzT7_o9lV_qjVI9M0pIiUG5V1mYHg_EwiqxMrb4jMzUV2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VnsIQ8BbnV6QtOWDpsqv-i6qXzk7HgE6c3_8PlXV0kDYy2AV9xt_c887qIl26SoxNbilwrgTb0MuyqYPvIRvjBNMBQpdcv7FPyVwnUQLgMtRcKdYVyrmwon7ZOmBhOPbU0tFL-6BFKSsu7adOwN1H0PpDp1F6Z9aq-mIGRNw7oI8nenf6mSGCIFXl90W4iiM1c0UvJ7vD4UsYvWAv1rj1sBFg2IQChpvd7_OX22X8AJb7y0N_C8LyYouProoL6lntSVIn1XzSZ6aK2RJthha9G37b1nonD3g5PIuflWZLgst4i8jKtPLfUHOepAmyHp4QNP0EaRSMTTUxkz0VuMxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=IBiG1FxkQBNr8OzgnOe_vVkSjodPH5zsogMj35WRxgzajz2HRnnYh9ZDqSO3QSWiT-jGbnA--Turm-hRwEOHMTbL9tUosQFC2Xe2rrVY_llO6RnJLhdZYSL2D1gyO51QyBlg0RK6npAVHvXfeWdt1M2ym2fQcJdyb82H_a6anUdQ7bUZsVpK525Q2Fdb1JuxbFCMz-hjvXq_mxTLjcKZkIzJy5rYY_JwlfByTXr0oysNuYlAJV5NUsFIi8vJYEqiKtnmFHrq1nZBbv0Hhej7h2Kl_mnGQy_Nv_o010MSeLH8vDZhHxSubhW9Qc4S7YOEvHgIQC-A6c7FnEBTzfv8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=IBiG1FxkQBNr8OzgnOe_vVkSjodPH5zsogMj35WRxgzajz2HRnnYh9ZDqSO3QSWiT-jGbnA--Turm-hRwEOHMTbL9tUosQFC2Xe2rrVY_llO6RnJLhdZYSL2D1gyO51QyBlg0RK6npAVHvXfeWdt1M2ym2fQcJdyb82H_a6anUdQ7bUZsVpK525Q2Fdb1JuxbFCMz-hjvXq_mxTLjcKZkIzJy5rYY_JwlfByTXr0oysNuYlAJV5NUsFIi8vJYEqiKtnmFHrq1nZBbv0Hhej7h2Kl_mnGQy_Nv_o010MSeLH8vDZhHxSubhW9Qc4S7YOEvHgIQC-A6c7FnEBTzfv8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G8NrqWep24SA3LUNCZB-BsLO7CtrIXtn8uHp-inFFuKIpGzFwuK-2FUY-mjDWN7RQ2nlDbSQ0Qms6zNgVl_YM6G1WpUd7uGfSeYVRE0QiajDs7-7r1mAAClZtij7qhdiMhrN7dGK-r8oXkEAU9_jnkmJk47ZUAvXZZgOTyig6cego_Gvh27EFz4yCxkmkePqcuAX36P0-0LT1xvmF8O7q84Ijlh4II9R1n0S8eVyWxmNdMaRQimi-Bvj3N84Htq3ZQoc3sw1hat1BTk8N3mBJAJodxy22axjhfz82EpKDkXkcWdJ2xiMnlwXOzYK5mMtuo5Xgg-QbC8bDQO1P-jzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HeToV0Jqw8vZTteNN8yp6tuo_C9aNb8UNkJo5U8NlrvmOS8iGaH-DVDeBDeq4WJgtnGDZWm1_7m7apkH2zOKZM11omS7MAJBA0DhP8dV6z5439MTsP9Zui6ab4jgRoXn107cFaRoL_lqtQBOydIzNYpB-KxESXudOwxKSrX5IwhM6cXjQrQ4rCCILbA2Pg9YN1Wo6lMzayHTOsAgcB6dEOllS9Ue9bC25ihTp77GsMumoEqi-27VGIJaOo9Gyv8Wd9TaeFkXlp9adMbgXnvyv6nh6Yc8W0dD19zUm6gQLcg-wlFn8JgmBfjkn1xV_ni5rvv_qDJ6cLHJVgM8F5DcoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlSF8DxQND0AfmnBEUjZHQKb-85NsXFifZmBHAtOTT5k765iUVuKttD9v3d5rdf36S8F1Jzx_lb09SDKQ23KRBrC4I4OVKpHci_2kbyxyUdDQKK-ld1KBvsoWpbolSVe3I1w7IxTVZQsZQL9aatr00eEbFIehJhOSLLcFe1FHcaY4PRSmbL4szYVGMS-QgQqddllzy4Vc0sNxkP9Z_RgJLMoW8EMiBNaiw0KHuTveUzWERDfJeuK7F4yahTdc5Yz3wJRZamUTbVG-PuLRzpRiQUGstDAJ3ldwk8GWLROoLAxe1ozXALT2K4CO6UbzJSDQkPz8JIBNThCJ3DO3NSzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=YxZ3pCenRRuh71UNzOkUdD5UyOf1vpUZlPkIrhhr8EQBWdsjVaYjTlRDob5ueCuHqphs22__LUmP48zvgd2TOd71VEQYAQGiZvHiji4nbgjy8PXNvItUoH1LZPqp_-f4nzgZ1_oflCZJskF1LTVRcQqJ635Kt91mOio_mmDBZFEIXs2FnLBF2NnN8MiWsC11CObVvmTGBXhU85sjLc7J4G6JiWmufqN_gDVMDx1WXG89oX-eNk1g9LdVniDSllXwEoSnoswexuCXkvPSW6yJOMz4NElH6b4zjMSTZDf0_KJhRcD1_RIHdIL56RgbcTGaVvntb1pig8bUYfnkEe2jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=YxZ3pCenRRuh71UNzOkUdD5UyOf1vpUZlPkIrhhr8EQBWdsjVaYjTlRDob5ueCuHqphs22__LUmP48zvgd2TOd71VEQYAQGiZvHiji4nbgjy8PXNvItUoH1LZPqp_-f4nzgZ1_oflCZJskF1LTVRcQqJ635Kt91mOio_mmDBZFEIXs2FnLBF2NnN8MiWsC11CObVvmTGBXhU85sjLc7J4G6JiWmufqN_gDVMDx1WXG89oX-eNk1g9LdVniDSllXwEoSnoswexuCXkvPSW6yJOMz4NElH6b4zjMSTZDf0_KJhRcD1_RIHdIL56RgbcTGaVvntb1pig8bUYfnkEe2jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=fF26w8Lj4yUz3zOo3EjNpi5IcgV1fB81CzMMQ-nXfm1Kn8vW5mWViObRr1DfCOalqZvnNel-I6iPyKH0WEV3tjLQv4JkpNV4zeqdYQlJL2brW-T-e6xHPjVfib7QPVKYT5N77NE2mUHrh0gYSa173Dts5mgnGaHETADUnzDAyA2Q7EwsFcW94uqNBJOmk9_hHwgNx3hn-kbhHVtQtxRZBx49oUXfzNA3FurvJbyFHAZ_IXoTFmI7633moQfsB-4Z_VtFQLQ7t9y0sw_qqbejEx1a-QNXx9QKqp7O6h_jaoncn5_WQ4uP0k0ZBzr5pcaG25jZr0RXbt8GHv6v_njv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=fF26w8Lj4yUz3zOo3EjNpi5IcgV1fB81CzMMQ-nXfm1Kn8vW5mWViObRr1DfCOalqZvnNel-I6iPyKH0WEV3tjLQv4JkpNV4zeqdYQlJL2brW-T-e6xHPjVfib7QPVKYT5N77NE2mUHrh0gYSa173Dts5mgnGaHETADUnzDAyA2Q7EwsFcW94uqNBJOmk9_hHwgNx3hn-kbhHVtQtxRZBx49oUXfzNA3FurvJbyFHAZ_IXoTFmI7633moQfsB-4Z_VtFQLQ7t9y0sw_qqbejEx1a-QNXx9QKqp7O6h_jaoncn5_WQ4uP0k0ZBzr5pcaG25jZr0RXbt8GHv6v_njv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t0SHvGkeI5FZ3QbCiF6tAvUwsR3lGQ_KuOOJdZZSoTySvZo50Yvq5Kq0W_lA2ZPgIrXwI1AROh6YEzcw0qGH9Kv6_Zb5eQQARvomZS38NE8BeRg486vu77f2qnBOLKI-97NhH4y5agjR5ymw5jkRA_tLVv9S11nU3t2qgPLsUVPWuQm8ZEzC9gIrWu_FozfWhnOZAhIQvyCySFHAvnZGjsk3w26IzDo_AWV-R2PZOFMyV3yAulv5ZwePC8sKu5EAvbPjl6piBe4lOOHIxOLjjRmZoz9MxpW2JQSmLC3Tuaqy480Z17kzxXwiEdcHroecPETSUidvyscSS8VmS0Wg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O2GSBp0p6VkbmWQCJ2E8pdrYAwyNz48ip0_r7Z6B1QKaNvMPRjpt5_UOvpyC1FTPisgNbuSfQ9wfRvQrN04EtgD6qNNESXhZAkQVMzmCBf81VvhGfsjr1vVIiqEVLZaQ_SpkSR8VIa9_XbaB_AiNs7qyt8-UFS4YB4RHpLLoN1jANfv0cNAiFlY7PZTy7NNN8samuKL0EiN5_xaLZkUeTDitkTK17JnN88Eu-_KCzKN6Q6Ajwtj1a0r_Ki6jH3pUKmdZLA9Uii2YNFV_Z5uY7VerX9hSkcb8CsIKWSahTeE4di81MPkvQ0DJ6MN7uzIprcHnDA3UG6gE33hiihWyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vi3mA7msXmVUrRu6EHqagPU_oWkrNF8TIKdz1kamPNE9BE4vedCSCmKmRcfACCKAcoE2Mize9SNbcCMkEjEUfqAAXoOPJuLgnEOLfd91uJjcGLfZUkDH6rhAvZM5Kq9L0eUZ5CdSd_18Hyz0ZU8oXmqlJ6ZOUxIvGUld3pdoyc0FMu2Da6j3xLKstClEEfiHF9dnsRc0G03pB8Y1gxAJAZYfXoFd1ZQr9mSVwMdhhbyEQFgxsC_sn1g8XBbLvzdHTR7Ei78PxGQqAMjaimtMz4mu058i0ZoDa8oYwf4kx4A2CxSvqWeNY7NPVGJP5Af-yz8tUsyTxuR_sbVT2F_nuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=JRYYQeUzcx7rKYv7MKfl6mvXha6SmWeZB6t-4XuHChGzb2zrtIxJt_Tjj069fAskY-kWM2NSBV0D3sVrkX2aCQJ26kvQmQDEXr7Olpoqj2Xg3na24Xjs1frbjiMP_NV4kvr65eYkl9Ca_42NJ5pTq5amvyRbtqHdZyLxuAdSmhCk2naAAHCxgHLqABoAOfzhUADxUvORuU5pwxQf1BLRAluYuAKHr_ymqZX7thmA9ZAVbDBRgJT4VJBZ7JZNksZur2-1roCH3oG-FmGEKJXx80QCWjTmlHgN4oq_wUdERd16odgD9tDEhD_xGwnX_bsfILmI5amHz02k792MxOR51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=JRYYQeUzcx7rKYv7MKfl6mvXha6SmWeZB6t-4XuHChGzb2zrtIxJt_Tjj069fAskY-kWM2NSBV0D3sVrkX2aCQJ26kvQmQDEXr7Olpoqj2Xg3na24Xjs1frbjiMP_NV4kvr65eYkl9Ca_42NJ5pTq5amvyRbtqHdZyLxuAdSmhCk2naAAHCxgHLqABoAOfzhUADxUvORuU5pwxQf1BLRAluYuAKHr_ymqZX7thmA9ZAVbDBRgJT4VJBZ7JZNksZur2-1roCH3oG-FmGEKJXx80QCWjTmlHgN4oq_wUdERd16odgD9tDEhD_xGwnX_bsfILmI5amHz02k792MxOR51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0OLdvL97BTGkvlrCBh344LqM2dNesgW8_UaRMTdLNTtOxpzW9iAuMmc25cUbZ4OnDWmLPnEtleR2eboI-cd3vrnzfYsZ6AB26q1uKeXwz-TqjCOQAAVSMcZtM-KpiHvEdgggZj-H428fgg2Ag1jvB4BgM5RmYwsrpiQzahGvj8OOi5jBqFifMUWSS6lToAV1DaBg_mVlZInzGLclsFVJ_D8qVwS9J1vbvUEKRT8VOf_SDJXCBurOplFcxvMKkg8ZA_ASId3zfAkoXwj3zMiqMEJ05LyKjQ7yuzyOlwxfHrq7-JNwk_-dk0Tt5gBhsDN0E46vSfkSA2KM3ffv2npJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKGmfe10BY7JyjArtRiUSVkHY-DmniPLykVWongm8L84vTgNzc0FNou4u7OGdSq5zc4v5uGtddylF29r3Vn2B_2h-1EgogC1qGgOiRLnS7oD5_LYJGNTXDNfXqQaQ5innpx5_nte11PvfUwRM4-IfRb5Dnr5PprcXavynvxXX5bh5L0lZAEUGJaqWn7QvGRwPuIPnccZMx6eds-Jqdxs9qbTd3zlzlKk82wbX9xyTkruU2GjpVT3bESWsgnFtVn3CrZK8QvrP6RqNoyDhO25l_dFQyOuBWDJjI2EhUgX_NbNZ0HGC_oRSwZEhmHz6rVrPKmom5tt2OMxu3tsR1xG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHhJJzuiUQRZsKOlWJGpnU_L8_v79VzA7IarTC8Yxm9NPv6REa4ZZbPk_RE_YGrVU53RQsKWFtk00chHR-fefkxLsjFqCcMcxHyAXUsipk7ny-iLRjVwDryiYERtoWkzKUoxXkBTfFNooPXK_sPdXTuk4ram8isxp08kbJbQUXMYsggdY4BLMWJSVQVifQALSriT40ObJl7muvqPNizLbRPJO7wUgwHbHGRTyY49uiLwhOU6QKg6XWQ0Pn5UHBZDrXu4VGjUgQOPKPiUAxPA3xrgsoD_gavAZTrkXS7PHI26H808Os0bn7xSbUo81sP8B4P76NuxsfjxeXu7javqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs9r3BsDIygKVis9vSNsBydqWoqqB47lzqIBght0UBqbAvf-r6wk4bh8pAqrEyTAmKQ-NYgrTTnO4KwoLEQo3MRqV8AYgbWHACRuNTxOV1q466IfObct5p0ffgASFmCHMA4unw21SEsVxDsUoL7pgoH1ALK7rKMoi7cQMZMw_td3QwKw41NJB-ZGLC6JojFzqP4Oq6uaB81EiKmdoClSvf2hXq9mTAA-2EUl1wRvs546Mhn-kW6ds4whKveh2H2Ah3CgQvu1_hmxQFzTGWtrDS6Vg_5cCGm8EAjEIOwAjVjL_cUkrcWT9mEw631qbbP0_eSTDjrKvGDpRCxwKlta2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BtWACrazJvqFgDYnT9wqR4_cgdAq8OgyHbpsljx8Qlu_3gjIKNOkjYEUFqAsG98WDVRkMZScJkue06SbrR7WMA4AY6CsfOkosbnmJxIm-G-5gbABFJkyygRzLyePXwFGt2jxCyro4Nlj4mT84J3hJnylVhJ9RFY4NxXbmWm_5LDvVAOj-lZ3OcK-JcawHaOlRvFmc1uAe-oJpItZ1H3QnyD-3_AtPpH1owsmWKqSgQ8mGUnliEDwaeMsYehAMClwOQ8_PfkThwEO-mGbqBJ2ERpZspg2Ocrof_jkFmGgNnr_dCRu79H7Ikkc5601nE62N3Be2OzptctFLKGIDHkBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8rmSez6VPCYNbcMEMGz30ungGP66J81GOqOa29oh0FewecTCcSgn5ZORlkhRfyTXgWN2K9rWv1IKigwtJH5j724sgxpcNHDQ57TDMY4s8CmKZZjy3kmnjtdYV3KLA-ebNt852Md6FqjpPosE_IlqPYhOP1LJsR1fLMhF8DmoFVuj5S1fLPA1cVLDJ5vEvjBY7Q0iPUquELyznZ6g370EUNqbTEJKM9smlBu7Pj2-UAhlOZWInlO95MxFdikP-YGAnRovYxBq7f2n9H8JBI13e1FBLFKtqTLz-DNhY7hbTk7B-jHKUlPmtlprHAP-YLNrFEff9JlgpG5shJZv4kHMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CtS_QFKUuO5H7jHhfiJoDSh6I-RMZMSh58aPOHE_23KdgH48ayQGqpxia-lEqx7GLQpYYFG-bW-cYiBYpQDONqmpmdw7klj2soFGj2woOj91Fra2lTmEcus_BZW0SrH9a3JH0RL0-97lgSTz2HjxAC5gVxyQBTebFj06FmTGEo71JR7khk1SA9CdWx045mlAtDzh1bGGSbEM-YFNJeTIIq0R2-x78JBW7bTS6tc9tRKnxpTDRiiB8W5GvQBw1w3v7VQQ5zhONv62Almr7jmrwdpRKEvPVb9m9KCry3mAwoFnPg839WL_hrqnDIb9Vd44WXn9K1dJOdO3gbmJmL1Ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4u1YYTb2T4jZKslpfvyDlMyY-tgJmQOAICiMkIu1C4TkdSA-m2SMaJuuoiHsFbZvqGu-LOJvXXqimbc139kfPY9Qylgs90pbeBO6Wnzh7hmWL8CZPvrSK48iKUUtr2B8QPsas_FHtGpTkWleUeGVVWCcVn-HnpNtdOS45EsKKH4Otmi0N1HaSmm59N6BEUKcUTRJWruhmvxRXwytomPCToFETaj82Vm1IC7LV_ANY1Tf1brTd0MP-q_UIRwl0ZkbMReGH8mjygo6YQvcTtNkY5fgZv1JPyUAuCKdbDa_zWJeSUKONheqaEtbtJtINjMj5tNPHktDUtcoH5cyG9oHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=tG9PVOykbdYne3QD20gNfInwolBlFfmPJPb4y_jYNkZIfFgj4OyI6ZyIXqsqAF0x-4eDdN6HmCAr-Y6WRafIpiwM55Wb4IuK0O8vE40KZUEAQJgMOY7f9WHoT8UQVdpgzo7P_AMcNG5Il4fPmQ7xG8ngmQsvQtuOKB-UtasHYspViNGvmo9eVsnwdbd4e-lmTxVAC5LOUFYsAM8LllSW32Y4COei9b2ek64EAefHyNDVFpZ86mQy-M4ImMySXg_iIuQUG8iu_ZYQEUu4fehrZW6Nj6sVE9SBa7ZehcWGKHY93URHZCsuvoZ0oFDNMJwJc_ctA4Lr1amNhSyhV2H6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=tG9PVOykbdYne3QD20gNfInwolBlFfmPJPb4y_jYNkZIfFgj4OyI6ZyIXqsqAF0x-4eDdN6HmCAr-Y6WRafIpiwM55Wb4IuK0O8vE40KZUEAQJgMOY7f9WHoT8UQVdpgzo7P_AMcNG5Il4fPmQ7xG8ngmQsvQtuOKB-UtasHYspViNGvmo9eVsnwdbd4e-lmTxVAC5LOUFYsAM8LllSW32Y4COei9b2ek64EAefHyNDVFpZ86mQy-M4ImMySXg_iIuQUG8iu_ZYQEUu4fehrZW6Nj6sVE9SBa7ZehcWGKHY93URHZCsuvoZ0oFDNMJwJc_ctA4Lr1amNhSyhV2H6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD5f5GV6vFtnMQkUETUpTDJjIGuUNaiSqJ4lVLYrv_wqvCPDiZO_nryZM7X8keNmIWLlOrkpU2jBqe2DbRVvSry4sahqIJ4_mlnyavougPymMAlwwiZL5Trba9qfkaWVpoQExtJsuE-7f8Z55bOugUj3OJgyGBerXMI4O4l6hD4omB1keQ50XX2FN2f810gYYJ6KVuOAtY24ci-ZxO-D82UfH5-VVIKRz5B3tgx5qVL9C5YUAnoOHnDr6OX9qe72Ss66BuYgG5XNFf0tO9oPKwsrMbbcvojDTlDmdBWvmm8CD00NSkv07RPHBPLkcFymURNrpGJFe_m9QiO-xnJxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQ8RKgNeD_ERq6X7NKamKdjBwMQE2Q62IAkCIIOlz4Phd5YBOepXxuR_meuXWER7vqv-cqKoF5FEceC3s94YIlHBShsU7r1Jt28xdAYajbR_DL5NuI6IJ53nBwBgRFzrKlRQ4_3KQo_0ThPqOtaMonUwBs8Zczl4EnHC45S7yCm7Kii9iD3b8HuVP_6C5zYy9jYk7zFg2cT7JW6Yno2t6oZffc6HXrQwMXH7KoLrrK-6oNXDvwA9VTUpsdAJlcwiuewiL0KdrieBeXrVCdkIFI99RBDhgdwa6kyWcgSNgGHwMYFz6yNtEHaiX6-7v9JHNyA73lW3tRdm3Us5JrYsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-UH-ail4PeDEsq6rjcMlW7xRgwyglPkzxRdMjflfXv36f50kE3e2fqYMwk0Jzfmvqw0woxP3H7TOC17y4I91I3zpkW_ks5yJ0Wcs0XFgUJnTUrw47YAb3JYVGhVQHd444s4_N24TDWh_XrDBCFEPLEmncTXSAW22ui10Sljj19ON05GJWuNz-TRzv95mZdbpMnFxrY7xouCCK8g0zmZ1GUvFcLF8FSIcGdL8Q5hpRPjv4-QCJ-_xUkHvWQidVDY-hTxmi-zVcDLsrYtQFoyyAyP5ULjwhZ1BrtI89ejNWugnZ9ASsmCl2RTV2UOY4Jn67FxFifRMYW6d-L4bfJdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fm6VKLGAAWazN1kHIgaZSgBojM0R67msoNTTQuimyifztMPgp_n67Lzolo2x563E4Xd_pQl-ZBOVzo8uN5a7PZUgF5HyiOE4sgRU1pqb4iOm38xylnK_qT3rzns3xLPqROsJGZx4PcJlGzKBV-NKtlPTFWntjQ28LQ074Ul6Sxc2fpeU1fvE_Lg5mFlw1ci35ooisxyHqXgpHJl1FZX1yZIkY6baCvlgU0sew9xVSLlfLjvKa9ODqsHU0IS3a6hiRFawtCR5uUfpwE955gpgEVSAkBVN76vj2tJTT61MfVEGHzIjct4mTuig2Wa5yDElEz92CbW4i7hcaZC7-k5ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=CsEIWJ7KZpaAf_XvSEH5tGGY4gBqyuJfEyARLIbkMMmOS8wOy5oEiorkJhSac2RbAjcBkNnutUbzlitMZaviFp7jld9NY1sV04qfSaj9Crpn2q6H4IXRNV1nuTt72AaZqx6OZx_7GgAxSOodNubVrJaCfKzfcZ7xK8j7_7YC_TnlBuQngv5Z3iov2XT-6LQpS5pMsehZAmnEXkF9s1B3ularIU2Whlm-47N9JTQHNH_KEloKqDUUZZ6r4rjNcydNoys59MGx1AypV-BiCLUA35wfdW-exvaZV_hZlBvcfNO6Y3PLPaWE6ZefvuojdxXy92QJdysrTVZRLrP0E8n9ZCnRg4NU5PeJiQK7vCgvePD5XjgUG4Fp3U_Yb-MQMem74AN-ZTvmxVSbnZ9xF8SHmxcnXEQqJj4jxW6aAfwUoLVN3QsikgIVHnkpwcFB0uObtXbc1gtzjZkAg4mRKjDvEelUyQJ8aYzpSSWPc3_9W3IHRh2vdlfWBP5HzKYfTFuA_Bz3vEMjtsnFvYwOCFjWm7Cp8iFs78iDRig8k7oCPjoJWlQTkLWPJNgDOXgtcqtMt8iEFQEqG0brYT77XggVOINYh-ZcJ7dV6ULZTdKdcMDgHvlxnhtDoHVla9QzjnKKyOsiG0RHI7LUobd7r2cP3wqvuGiPQ7BURqiiabygYUk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=CsEIWJ7KZpaAf_XvSEH5tGGY4gBqyuJfEyARLIbkMMmOS8wOy5oEiorkJhSac2RbAjcBkNnutUbzlitMZaviFp7jld9NY1sV04qfSaj9Crpn2q6H4IXRNV1nuTt72AaZqx6OZx_7GgAxSOodNubVrJaCfKzfcZ7xK8j7_7YC_TnlBuQngv5Z3iov2XT-6LQpS5pMsehZAmnEXkF9s1B3ularIU2Whlm-47N9JTQHNH_KEloKqDUUZZ6r4rjNcydNoys59MGx1AypV-BiCLUA35wfdW-exvaZV_hZlBvcfNO6Y3PLPaWE6ZefvuojdxXy92QJdysrTVZRLrP0E8n9ZCnRg4NU5PeJiQK7vCgvePD5XjgUG4Fp3U_Yb-MQMem74AN-ZTvmxVSbnZ9xF8SHmxcnXEQqJj4jxW6aAfwUoLVN3QsikgIVHnkpwcFB0uObtXbc1gtzjZkAg4mRKjDvEelUyQJ8aYzpSSWPc3_9W3IHRh2vdlfWBP5HzKYfTFuA_Bz3vEMjtsnFvYwOCFjWm7Cp8iFs78iDRig8k7oCPjoJWlQTkLWPJNgDOXgtcqtMt8iEFQEqG0brYT77XggVOINYh-ZcJ7dV6ULZTdKdcMDgHvlxnhtDoHVla9QzjnKKyOsiG0RHI7LUobd7r2cP3wqvuGiPQ7BURqiiabygYUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pWSRde3tvw-JeH37TEOgCW6DC78iZdjwSaY0nPlty7JOkKHI0HjJYpJDNUUKApD6uLetf61UZIEkzFQS0eapp2hs7i2MfuXGJx20h27EeG_jD4nOZafBpAy12pUd2cV4Uzr9NjmiHi3IIcxCRBmV2K1hYkx6dZ7Gyynj3QgskOM4AJtkPisB_pWD_TYkSPvBYu97OYxEJ7qhzwSLfFgewaOoqzc6JLSq758zxY_TgLDQXMr3mfrQh2uFsbFzRgD6CI9TuRdaVXSmlfEXGdG6jwPTi6d_lJ0uSgXJ73is4YxgbnXwNNDxFat7vlBu4h6gOlElvjXB2q4z_B0ZKQgReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pRdQY0mV9VnwnaqbO-FR13X7UIMdoI3UOgxTkyYPiL8BFKtJO6CmK9i54nXlRpnS9WfnTl50V2mA9CSWvykDKHgwNxuNT16noIM4KYtapuNpR6qHjsceRbZEAlI_1FhJeW0YPEWrSXu31TRTjqnpCSm9D_JsftuVdg-y1zAQzATw3JNH9A7jeZDjr28LdoXabn-PouwIMpFyXhBPl7IArqabot9C8XkSxu59dhEcY7jFcUDRUcbpGCa13p7zujbFkEYaAj8ioTpl3bxUev3Jv93uXcL9G27HYYKSq_v5H7jpSH9QIdBcNxmq_pwRmeXmwqj7L9Alqz9PCh-u65_uVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=B2JFSe3hs92uiwaMKCMdQoVarbLN0mMnw61TQf6G_pL4kuxXTMcm7XUw-Ein2gUQRd4uI9drZzLqd6ZJsz2AQRxk6gmv7XpjCoAXt3rxF0Nq0y4fY9sUzi3y1nWUJMl_2k2aAR9HqzwfPXpwolavdyYBcQiUmc35oZVkRvbGca90kAnIF7a3lrOgYIpUt3B1El896EO-nfWQ9mTMHZsQIP70Cb0t7lVXZlRpFgzMmnRzyDEVJkVVsg-c5LoX9NedFIhXj2mfUUkSJUx2Hw38F6Kl0nEXrWuJsxfBBkrJh-fXfO4GcIT1EphfOIu1bROdZF9o_q9Kbm2vYxMQE9Prkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=B2JFSe3hs92uiwaMKCMdQoVarbLN0mMnw61TQf6G_pL4kuxXTMcm7XUw-Ein2gUQRd4uI9drZzLqd6ZJsz2AQRxk6gmv7XpjCoAXt3rxF0Nq0y4fY9sUzi3y1nWUJMl_2k2aAR9HqzwfPXpwolavdyYBcQiUmc35oZVkRvbGca90kAnIF7a3lrOgYIpUt3B1El896EO-nfWQ9mTMHZsQIP70Cb0t7lVXZlRpFgzMmnRzyDEVJkVVsg-c5LoX9NedFIhXj2mfUUkSJUx2Hw38F6Kl0nEXrWuJsxfBBkrJh-fXfO4GcIT1EphfOIu1bROdZF9o_q9Kbm2vYxMQE9Prkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=Yyo_QcLIRVNytuB3q3KLt_3mIshVtda1x5ibl-RimFNYaJuzi7uFrRnl5vkxaFcH_ceiRvK1Pvra6Z-j1jQ9uxzu1R3lb5gwoobS5mHMHMR-2wQ_6AUkiPLBO7t7bNrljtG822BZGkFUWw5Z7ar0XygjVQLbJgldQ-7eKjMoGKKabQQrMEY15yCP0mpdN_Sj9dNG_uXfGj1tCi-6ZTV4y2XimnAO7Jd7N95Xs5e9ji4w8khZIZZrvAShvEjRTllEmqKbnSFcyR9t6ZEgHCo5Nrw3se6vzd2-uf0LFwQ0zXCsbWyhENmHiEiyBT2c1_D75oJO63ZF3UW-CVTrV409Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=Yyo_QcLIRVNytuB3q3KLt_3mIshVtda1x5ibl-RimFNYaJuzi7uFrRnl5vkxaFcH_ceiRvK1Pvra6Z-j1jQ9uxzu1R3lb5gwoobS5mHMHMR-2wQ_6AUkiPLBO7t7bNrljtG822BZGkFUWw5Z7ar0XygjVQLbJgldQ-7eKjMoGKKabQQrMEY15yCP0mpdN_Sj9dNG_uXfGj1tCi-6ZTV4y2XimnAO7Jd7N95Xs5e9ji4w8khZIZZrvAShvEjRTllEmqKbnSFcyR9t6ZEgHCo5Nrw3se6vzd2-uf0LFwQ0zXCsbWyhENmHiEiyBT2c1_D75oJO63ZF3UW-CVTrV409Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=kZHFVwY_jfbGKbDvNW1H3ZdN1OUWLqQb3ThIEtYBP1y4ogiQg27VrDXdUs1VfMm_NG9xDSm2h7EPUmeb-D46QJC5Ll5fSCcE3Xn_ko_JafhztAuu6NOtwmWzQ2GDuvowHroeNZh0vGA929pY3JLjsv6M-PAR5UYPHa0fjaaWd8S3yXesimNAB53MuFV8Mo1wb1iodMw3oUJoVzIzDQ08IbkOcDQdb2_mAvZvZyBZxqsjtMB6vAhGJHSvdSYa_pw2r5-YZdJJaGmhpW8CXq2PM5tTRGwv2GcttGslnuZOGo4HAyNT-j6wHTo1VF9gYwZudf5tf5YVGEze9MYEzHBlkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=kZHFVwY_jfbGKbDvNW1H3ZdN1OUWLqQb3ThIEtYBP1y4ogiQg27VrDXdUs1VfMm_NG9xDSm2h7EPUmeb-D46QJC5Ll5fSCcE3Xn_ko_JafhztAuu6NOtwmWzQ2GDuvowHroeNZh0vGA929pY3JLjsv6M-PAR5UYPHa0fjaaWd8S3yXesimNAB53MuFV8Mo1wb1iodMw3oUJoVzIzDQ08IbkOcDQdb2_mAvZvZyBZxqsjtMB6vAhGJHSvdSYa_pw2r5-YZdJJaGmhpW8CXq2PM5tTRGwv2GcttGslnuZOGo4HAyNT-j6wHTo1VF9gYwZudf5tf5YVGEze9MYEzHBlkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBTP-T8Ys5KNZj_JEwh08bDysK4dFd6RRcKRRMnFt33SpALQw2uwCeVEmDC8xm-EL-gYzfZOZvtYkN-ByeqWO2VGOlqOlrK7_Ab6zow72aG7ltkaGQK_96F1km8QTFUizdVCQbMqbygDpAN1LYTgIYymbaRJw1f2seIGgbN0BSFfFPfm6Qx-Y7wqxvS3GxRPIh2hNFgWkod5d1uVsYObgQ8DsCz5lTTkznFnsaVb3LXMhcatZ7s1VAbek9n0_HX851D3hvAztEBe36wmFv_oGvcb3iyP74ll-isQCg7kbrVcHuKxubzeN1VLeh5zNYocgL92G__9rWjNLik2DDfXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k1ixoa4naK7WkYxGFWffpUjFWzT7uexFYA-8zr4Vn2FMw4i5YkbW5F8ZynzC8eMkvuxkK5j1AGwYt-6ota_Mx7xaL6DIdIGPj82V1LQmWORbigyniJNqsOt5xZNxcjD-8Dg7ECiMh04Pj4J3Hw04Vi_1EaFtcL5tUFFG3MSA5p7OPPAuYsnhN-6_VbvfjHzOu5tUuDUjoRZelJfHTOaZ9iuZzisWJW1dGdEB-t9dgOJEn-I3yavUwUIro_8xeEa_-x02tVWj3cfxcrQ-JNsfr5k6OLABlqcozgLFh6w_x3_XEh5eiyjO_dpyPGT551iJRjLcHAhWWWEpwfm5CPgUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvjVikKpvmlD5loQUXcFzwNDcK8i0HNoycvTffR4MtmsPHotPee5hKzv33kyGUWyNGuM7yK-_xo7RnRxT_pNclGurpJQGtl3Th8wk_v17sY1MZX41Zar9ScD514GjTZTVEn4jTTT8X1jy4Wiktx4XvjsjjeDtIcQm4p9B0eGdo3Fqm7ZqQ5ZPH0KscPdDwi3l1wQBL4CeMJP2BmJRM1J4EekdVfmIR_-WLRb7WYDuS766KKy1Oawk_KGdFwFBqUWodCrRK8_D_4tVEHpzXEjS7RKPPbjPeCA2vmJ_WL0D5GVyIPmUZjebFfmwR_poiIMASZDiBNSoOlyd4AhEAhTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fkBW-xuzYQ58k8WTjuFLFCdJjY0Y1hdGr0Rb97XoFK17uwbdPmLbe5kAAkkkIHNc7-CIs3h9aJ2UhTA-DHMuEX5sFMT4pdIvyw9PqQw3Z007u_Nelu80rYbejPWtgYLscWwDcIH4Uei8UXLqWvaeTLRTEF3Guwy8kLDrpaE944zBmRcj8KOhuGSJb61xHRQAgzIPoEcMQdIj-urYQU5q3d54umdKn9bjj8V_Hv08UBr6FT_LjbZxJ3YeVmTLTMiw6y6YRPvqVrxZLiCiqxS78lwVgl3XKGlR0ASy1JeadEejd_wSTh19qV9fJYJ7y_pl2zrcYiTDaXHB7wBtpjAqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CGDaObKploQAj6qv-sDPrq43i5oulyP2sPO6BkTX9PZiq86SPdFsOLsC8roT-SOLq0JtPeTTZsCGT8TPqCrwJ0EEokl94EnK-zeRS6eTYMQY8WDnwq3CtavIfEf1ZLdVJLMP5l6s0vYngo9Mw3UUr0s6q8-j5E1G_yrMoFzUculaMlpOZOfHivV5R50oYa_wwwgaNhe41w7iSTI_wVpfWSyx0J4YegX53YEo5awFJF-NYnLR58J5BYsx_00MEd8zFchx9JhyTFvGd5uHNwlJnVY8pKuypqECE1LBTE-fdHnBpPnAOYBRjj7yLLitCoxJAKL4craFwEDzuCAu7dIT3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YHECz_ADHlK0aRy3H42Mpgkb0xXK0B3yK9h8P45Fcos5tj_ZBWSsIu3KZpYi4FaJePHM0admLxKV7Z057ndh5bk67gSTxrHATsiiSzDRnfBxvEyzpi1FescwL_gShuDER2Ed8C9wxYbOJ5nHy3R5uorodlP43kI3ShGkzAemh-hQjsSrs1BLS4soKORDLaYFi4vs8dz9cnl8BqS4N2ZvNmH5lyWjSg-2gZ1LFHaeAxzHybAMyvFk-YZ4pz66ZNSzFqfIv0c5VVFHLGSINyfzcIRcIm1W4_tr3G-XwCvO5TbRDMFh2MLEsIWvpkibNrCnGy3JI9wYDjOq7MEHxxV5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PO8o2USqAAY1okIsv4ZE3Cp4bexJ5eDRY1TkxWGIUQjDfAyJs2aupQxVv_fOgdMag8x0k3hP88w5tWe4C7ZrCbsrprb2LjjGGqy-jrA_as3SAeO3F8MlKu4JOkgYjD9h5M1UjcCO0ukQDhGKpSReb738SStFmNQGyFjYzJ7VKtbNoxsRrgDZyuP_TqJJnw1QMSL_S2gK27dSNXzWr9wDNUhb65-M1vZWj47fdfLwucf1KD1Khmf53VbpJtm9D4Bel4I2Ej2UY9tg352uF3p6hgsVFQwW35cebec8BQGgn2HEvSVGSuwcynsp70N_K7iyH_mNaFwzil0v44oMfrkPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rkagaLFykLqsCHiIn6Q-1hZpWL61UeJOalOUUvNehnRezy94Sw58KCIqj4ujEMR-GkEA_fWUNwjr33_2Tb-CyxIvwoszQQq6oaQIRuN5egvcCzq_NyEaFoEBEC6AV06O0jqv1kgk51oGFzb_Q4lN-6_eQ5-FrMrOpzsk3fKbmNPxSCT_vjRNfO2UbJ9R_pEcsmXW--pff8sOwQzwOkNFQ43b8ob18LzFagilfT26M8Kg-kyQohrzcNan4a8CPlZW8CEe_efgPq7MLgoWDeOZOaZyOdsS8pGCMIS8TrcKm-UKnuSAEThhflS9v26DahO0GnabTBu5Y7hGMxjsHJuUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mTxvS7P_OWFPa2AhdxEV3tz5F2RH1_a2S6tD1C-ouSfDXKaywIxa85vSz1hZTQVuGXusL1emdP3vSEhdVvdZhvLzVQBYqDVpn4cdD7EaI_QVbpYO1BQu5YB6dcnsJwqXGlJ9fHIzP5FK3lZkBCfUNTbsSJ_h1nAygVpLRSzT3GnFOIlk6NzyI2Qu-Ms1dpsWxxRPP2Yj2UIudeRxKXxQTx9pODuz-wvzgLlHT9LMeZie0B80Hmp2ZIsijIyMwOmPCFEoMpfIYrBv3eh3eoZDkUaL_SvNT4kouyqZt3zKYYrHrt52W2w4LsUUp1KlVfALoKjlTRmBfRgiF6YxDAlN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z8KMRhLE1upYJxqw96a8LUVl1ZYTUIh70Z1il7t8TVgWQXZjPDPxKoIC__HzYKbSaIWuKAj7pHsosGnr7s_0uzSHnrqSkxqlB8cQTS5lgAdAvDuj8KGyK4pbU12-UMSI3vWTbCLas1ZI4iSGkaitW_m9zMMTUeMPb9jw49xVVBEaRqbRFiQkS9cBX_yGkgzR6UnqY_vp-yzgdYywyciRXv-gd-Q0QCHkcJG2CIXR2039KsQskEOXqFBp7g_awvoGSNvzGg_pKCnHRVQnPwWRuN7TIRGe8HA8r75qYTe98TUCLndrgSVamzUN5zkFAS4Ib_uyATvXM-pdKjJfU6T3gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L3vBFNeDX0Qq5J4FJwFjsoNAjYwUFBx5D9PwiPnD3idI8Yvogb8UfD2kYXbkLSQAKm5p46P8SU8vzSaginYhHUd0L1KuNb61OWRfERz6Wi8QbMkdn0j5UmPFifzNL9wzuOvl7yeufN4qOX9Vhp27vR_gIjTL7IKHfnCFEb-EKLJtnTmAUlsQPDw-DCJpGjQp180CT6b0XnOQoz4uznd2KdFpL6QthoKD4o2ziAc63voFqGLnY8pC4VHxwBRG8mhacftlOnNx3uBAIxth1h-BJKYNzdB4s8rCc8Hn77ujhuo3GLhX-P3Ui8EkYL7TXhJ666ZjJTIsDQeyvejjjRK_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OyugL38Qy0jftcUrjf-jjlUQtOt_1Lhe_3itC5Zl5DToGL8_uGNpoV0egA-XASch5VJTnV_88wCvK06JHhxniTw3v_JtsJeCNY8Yybjl6qLlO3d-8RWGmUdbJQaDXIJrQMiLdKWgZeUgxKa96A-NTrigZr8-NDQbo5B0eZJgekySovAn2a4lfa2HsHEgxpJBzN4qCtSWWtLKmgbsYKP7WuqX2iukEIoNCaWz54MxIcmsl9SNdDtBhegkBw8ZwtHs6zkFP2saJ-ZIHrC1y-W0uv2-ECa_Evg5MJSWrzb4-mABpH-eB88LZ2TBk492Ildcih-2pAZoXMIYIOWvAXXMUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBmdrRYUl-dUS6JM1MLVbi5V3eNgIspbKM2GTQ-aM4leBd9f3ZW3rltm2ygJKOBc8wrJJmhvjwnEO-4jO9Hx3T46yZoLXvexreuyPfZPB4BgCqBMuE5rvlrlURAjRL3cb7GC1cj9jq1IW_iYwtoSev1b8uKWLhPByqhJ3MFnIKR1PSHmoJ91q_7BF432BEm7JwB05Or7HnuNSbBBSP3LXwd4cTMwOalAMp4rrJBWoFn0J3uU0Q-1oyJMMFmIQswuw629c6FpWQicD-VpR0Ekj5QREXSEIr4mhzLL1dYHHtRo5K39yrbUjVP189_PBgGcxr3W7jS7NUulsGJJZyZCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6hcnaFE0ZA5uQzL2Mmp0lSkXxpqcdICKnEHp60ZKLWq6ZExSZm7b-pw1mRA5LLWoi0NKwM6LcGAvWpKmLaxzRyRN1pKBu9dcyfI3e3odOaJGiC1aqdr0z4TehPmE9qaFCwzPsq2InjMbA4G_pIwJxNR4WdVmLUff-vM2DeoRNGQLazkS67pNZ9-UXxy5sun_8sFC9Ae_lS-6HZyNR_FE_8FTkgTVmMQVdt9ljcJHLeNcY5Fvrso8h0HUffzUHHEULMOql4fhNaAI0KZkw21FZCWOaJL4jaZqOU9wwiOhC6_rCG2C9MRidFsSsQEQd-ziZ57Huyi5ZmAphphc-pdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=t_NsQZ1HfEeUrZMGWbKfUEIS6sfPPUuPs167zv6LxQMVWDiE-c2LhCqauM2a4Z-dfSMBXtSLEC-K_jeuRJc55I0Xlv1mXGSTCQxJG9L2FNDL0ERuWQVttKj50eXpSGvaX0S3ZKgDfzQS5QSqPwrUO6W19B6XgFBYcZsCnoFXzjMvj3gA_vdGG2q7GlMo9v22fQLhTY6f_OHwuU-RicvpuwdWPGyP4hZbrxB86Sm6wrpdEvbkXw2UOboeXkNqg2_TI_TfJjG-YSzzle3SC4a9dCRqzb9ZysC8AFqi3PbY9lAmb1WTdC6vWzs6WlQU6nqDMD0FEGhASzQKLg-kiWSdmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=t_NsQZ1HfEeUrZMGWbKfUEIS6sfPPUuPs167zv6LxQMVWDiE-c2LhCqauM2a4Z-dfSMBXtSLEC-K_jeuRJc55I0Xlv1mXGSTCQxJG9L2FNDL0ERuWQVttKj50eXpSGvaX0S3ZKgDfzQS5QSqPwrUO6W19B6XgFBYcZsCnoFXzjMvj3gA_vdGG2q7GlMo9v22fQLhTY6f_OHwuU-RicvpuwdWPGyP4hZbrxB86Sm6wrpdEvbkXw2UOboeXkNqg2_TI_TfJjG-YSzzle3SC4a9dCRqzb9ZysC8AFqi3PbY9lAmb1WTdC6vWzs6WlQU6nqDMD0FEGhASzQKLg-kiWSdmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AaVUdcHGWesVtYYgibFjA-HRwSO_7HyQI6YZ84lpE7TWMVL14xHNHXRSNQAvac34PrivTQVndp8LbdARsY7WtjlpZ5Dj5giaGRzW0IoJ-Xo9BS3pQjnDPBuBgohoj4BazNcl8_RCm62JnI-EXetTPeQDGIDXHwYi041KuSK23rX1W4Q0BcJkkk9ar0tEPM489iL3cO0KLdy_zBmOp1VAmGZJ7Rg6cOyYMpduRvqxs82uk8KZhqzToDSVwUa2UBfvQrOUK8NjsX-hAMaz-cSMYzKYO-ZIyYz9wyFIpKcAKJYhWU3wKLD1q-BzZ8dp35nfJhdeN4F5gOFZt9dDOQEbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JhWMgGiFu3p17hjmJ_AFajIVxQ4J6SFZaEITe3u78JanZpSsElrE3Tw4l5W62AVVRkt2WpwrxPGMR87QMz0yQdSrIKwgZnRl4kfyrbIubxiy76orKqZq6lgiay8bR5O_H2ssvbnWvOR1oWUG9pomsEdziiXrAsDhRMEyCShVZHY6DRXEPBZz4cbcPQTcOdQ302uhunh1eIo7n_6zapSemh-mW-IXUf6LVvjFujJ6opvB4_3deS4INLI0e8_ENFa5bWSGijABkNA4sRt9OM3t7GfQxkrc3UX_pPUnMvQZtvfMuTt8iemtyzoe-uqtRD1idPGJQcjmk4CyBryTDL0kMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QAEBQUPtpjB_iD8JdWCaGrK23i3ui5b1B_-iipmwbUf44f3ov8Lz9_6tGQfhTUumdffnCoL9_J4p2jRrhFfrCDh71BEH_zO5lffe3h0vj2E99yYhHh6so5yDxu1W3F4JQ-3jV-Qo5oltW1YxS6epjCvQmvB4W3gMKdUbFRwJ8JEK1LgxWLbA948CkGAef3m8qwYnGnSV_P_q1iuio3-n5_DLGehw8aVBzT4cQBlkk6cgCtP-gfiBgN6IJ81VXV-xq_P6AWFi9bf3x2JXjaGxE6yNbrltuKOIi-wlkDeF3AzQl5IIFJE91Pw-IYxSKV96Y14ZNJ66KL6bTaifESk_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bIuUH0cJwoEb5xQL0GCyJIGV50Yd4UPLDm2ivp2DAf6EcLnT9HWtFE2UILBs3cn_yn8MKiFJpKf6waUJadovkdJPaRFUh6lryfIeM_s5AXXaEwHveF1TwGHBeVYQI__4fC26IVb5bqUafb4OYRbX6gwCiPrVHNT5JfzaK3udRGTZSW177USYEJGanD2GVOnCBC-teNnEivMwu1j1f7fS4KzQ-SWctGdTm6TV36CxG1N0vmUNVCKiAVdSEDVcoPlYk7W1QPukjSsXM16256aIioFUYu-0Fo4fqp6aHR6QgxmPhjEmaFLUsobiyFrkRVQpssQi3j8L33Ag2toJIFxSgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l97HAZKrMVf8CuD5XxOrqrdBVqIq3jpt9uclq0Xf5M-nQgk1WYbZpZxefeFJ0_rm-y8ZZu77nyzJ1vbotgsOzW_jUr_TpZVGk-wuGwITH9D_2Xa0nPJzmjyD2ZPxpsDDVJqv2gCI0EpjTH49eLw9B6XRqdJqUwq0QxLk6H39Q7fMiGzd5-XpqzDEkj0p9OTSgESfVq2UyPCBQcqnXLWz88ygtjQAaCBg7_zOevr_pRbbwiCSbOZALMbCkYMBruK1y4-YvPoafRTolG5MBei-fIWMUR7iXVTMh1bZ-9mcUcKeMBgVroavohGC5m1l2cBgUbHtskaOJQ-_sk5UbDLofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BqsGEPlcj4p5e6eXfNgjuce16yAol-or0xeY7EDVhavNmwUgkfkJaD1SQi1UmtHsiNl65pZ20HU12Sly2KFEDrSx_07MxqUFwuW6QivI2CX3tmxEVEnv1yhV3junHvHkuVgmXBaz90Fkgd55fyX291tyfjwTF5P5gjna2QXSwPswV0smYf5D-Jvt9Gp8F_HrFxMhib-07PO42eT-xVbCr1BG1Li3cuTKe2uYoUwT6P0sLNZs6ybzwzVioub_424a_xiKjpksZDvHwaSrvBZmYU5ZcQR0DlRj0K8eL0uIyX17mbF53DMNUcw8-AVjjPUWTWZ6FYxVgpTeh2MAnrq_Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=Qt1a0WgrjGEaO2TNLS9SEs_S4C4IzjZicbVN_aMQV7DanHdO0CGjVeq9dIu55TW2hHoSq82fu6pxiQaJnUBG_JUm-VqLt4h2Ieyw4mOGo1jRv0GW29n5halSL4V0VMb0vvOufMaz9utJycb0ITfnR94qoDRTcVqq87xfJR_9ZTessMYWHHmKdRjqpNCdwTCAw6c5eg66fAtL8x7k4Pcn-9mRvFe02X2kvy0IhBhPT8CBCDFi8XpAOpphiQJwuE5xv8ha-rLK8ZidVrUR6T9R7zDsFXlCSWAZiDEDUn727NYTrRo5eUdICEuYxpOvTPYAGXbRpbEXADlQwRhmSf8I1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=Qt1a0WgrjGEaO2TNLS9SEs_S4C4IzjZicbVN_aMQV7DanHdO0CGjVeq9dIu55TW2hHoSq82fu6pxiQaJnUBG_JUm-VqLt4h2Ieyw4mOGo1jRv0GW29n5halSL4V0VMb0vvOufMaz9utJycb0ITfnR94qoDRTcVqq87xfJR_9ZTessMYWHHmKdRjqpNCdwTCAw6c5eg66fAtL8x7k4Pcn-9mRvFe02X2kvy0IhBhPT8CBCDFi8XpAOpphiQJwuE5xv8ha-rLK8ZidVrUR6T9R7zDsFXlCSWAZiDEDUn727NYTrRo5eUdICEuYxpOvTPYAGXbRpbEXADlQwRhmSf8I1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5mOeP71Da8-KHENYPWgmlt20GLNw8vpMzzdvIwccpaTgxKRUv9mA0HihCm_EhjRfPOto8Sp29k9D0AN4KYGrin8UYahrdnnkhakQYtOZ3MPu3kAcd82NKVkrUpr2c6gngKTG14hfK0KhzCe39VqGvOx6pDnQzPNTQ8gPrzliHoNtO1qHhY2s3c_hSs9CS31rvW3lt2vX9VcX1doAz7fe-ax9clIQzuTBhv7ztKTy0q3PpJLiwirHKEKN3kskStynVwL36CF5jA1PzqvFfDXSvjNxy_KvkxxnfKXvCCZUrUuzs9UZvAK0KH0sJgWIxLQIBRYw97J-x-Nyp2KA3ViiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=njq2_-MH6b2zFkv7sXFQgYpbQ7r-hSC8sD1FRg9ghrW5VBgziBxzZpEgHFNFwX3lncAW7aV2Dn3VGlCpVzYCG0_UERvgDlBBo61ew6nJ9jShi90e9PurSKgdt0g-e_7hw8W_Ufi6u2jDoFx1T4Sl4gD-c7j5EyMxlTrmZEXlbO3uHQakdAz014tOA1uRmptJ_FrFiORL3ATDVpPQVfy0q_UbVDBrtshDl6DsVGrX2aTjiEkxVjsn7DkR7UnWyZSH1dW1IOkS-OFLNNMC3pA9L1523_sXijWnKN-0c8s5xBfQecAS7amccSJEfVHMF80m9s-MTuX_iUZdVipLCAZVnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=njq2_-MH6b2zFkv7sXFQgYpbQ7r-hSC8sD1FRg9ghrW5VBgziBxzZpEgHFNFwX3lncAW7aV2Dn3VGlCpVzYCG0_UERvgDlBBo61ew6nJ9jShi90e9PurSKgdt0g-e_7hw8W_Ufi6u2jDoFx1T4Sl4gD-c7j5EyMxlTrmZEXlbO3uHQakdAz014tOA1uRmptJ_FrFiORL3ATDVpPQVfy0q_UbVDBrtshDl6DsVGrX2aTjiEkxVjsn7DkR7UnWyZSH1dW1IOkS-OFLNNMC3pA9L1523_sXijWnKN-0c8s5xBfQecAS7amccSJEfVHMF80m9s-MTuX_iUZdVipLCAZVnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP98R_D1qFEvyx5yjM6namYhe54MiuMV_ai2kpl30n8WcVdCH5dLrEPmbFGlBZ6BBJIQGC9U6_B4T-A8m_V3XPgvEIxFAxwNVXE5tTKVh_OOoF9v6hqx0RzdPuo97wLbjhgX8SssWdjA0mXW0uU2ZajTGRG3a5Nu4tTct86cyFsj23KfiXNjJlMEnJ4B7PSufMxJXWD44iKIscV7XfkPMMo4M4aE-E-6QeClMoGzNUiKvXBVNELzT4pvo-7osIGJbVD5bbLu1V0xqbQyXpM0thbpAe8vMkTR9yjchnXVFNqUrUNaZyF1FCb-9uaqwpi85_EmH7n0dKBjemrpZS7GuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LKn9lQM7oVuxnvYdWUY7NhTQL_b7aGTAe73wlFIKkD7IV0_3WQ77aQnqJ0uWQGR10prRu-2DbjHgBKq7mjIajm5fnCeQlckBsA1KEY3GnAbk1HsTsVUORUb-QxLy7CP2m8CkPaI8dGDmW3ExMxKAjEaR3GSXbpp5gAlqTNs-XJ1Qh5qIHHuUz6wciQ5Ursr-7cmDECgqe7lf0CLZo3xaTAzLYAEfcZNmwIuG2f3QLC6V0jV2Uk6uqQOlAnz5yDUyogz09B-sb2R1dDsjcScWFjzk7H2Im4CsWF8Pk07BZKmORVpCfd0P7W0HjAyWCeuAgH8k1InyVbWvAj32fzSnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTWo3w0kllr89d-kzGNgkze8epX7kIZER8nJC06KRpy4QWJtVaAbGWGAjCT5T-hK-p6A46I-hXXDgN8_0gqIOXnPzYA0m_DRU01dRIpxHiOwnNK0nxsJX6ysHU7Kh0HcZUQQ2_knyq97XxMsaRUu_oNb8oZLjfoL10W6iYYmF6QWEGnhpKmMh87oxZDV930wMyRWMJBziooauwVUr_dkU7fS9eQG0Fb3_dRtU8Cs2KBka6QSwda2qjR9drqjt6vQUwjGHKb5L5i3EZGLDkx3YKzoFwl3SmAfIcwWNHr1FP0cRLeTCeieHPq5Lm7qeDRD15w80NhPxAToWJi7iBtZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijXwaxEtQSsy9k13qRfwTbqYYT4TmeWipMetFXVCAZWaACJ1bitaCF8juSpRB6WEXJRu_yY9jqdYvQPM-HmB3FQePWnQJX64Fek6uZ5C7nrrjvecWVjISi7Y_-6hVm2390VUWZ8NWj6c_lk9a_NFCI7HXTf5n82WfTMLBvN3kNXoRuXPDUHCt4VA2IXAjVXT-_L7FyTeulJHRsiu9nwsq_vFwxzvuem2YiXKPXUu46kY0npp8jM5p1dzyN15GVQhd87iOr9jbdY4LiU9v69T41-aJRiBvd1IoXCPaWlQ2YQf8x_X4QeA6AKWTG2O8nWfU0SIBqiYZsVs8DzvSZJj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oEXP5pgbYrhbYUYnIhvwAxok3yJFk-jegut91Utrcy4YWXT59tefxwnhoI_2ao0FDDatNULRmwg2mHGO5FQHfgI0wvPNTe4yu-4IkrlB8Ad43IQyenr3kpvcCLSVhBKGlZE-Ujyq2fHxLrIHhFbA4kU2Tz6D23rc4xKxApRSzQLYW6MZs1uH5WCr3iSXse69JK2zLvvCSFjMhKXSKhP8EnPVl78Drt1VenmUrUnDhpI-uc5xkLSprFC7RH_NMr0_nPC_u5oHzfZ_VKauhDPLHUnBjZ3bNDKzm1oVRLDw16mTE4qX-HnWsxHiQZbJso6syNm4fyBhEv0_0DBz7eC_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=YGnPLiGsVtEiY5g2fKef5KEV0heH6W0u813lKeJwNUqu8AnftTUgT-qWKJyxXm15QXRY6GqVZu08Y3ZyZRKzzOPqa5n-gDA8nFu6gN6IQMm72fDRrup32_e3KcwCscIyFtwGUgGLBBaDv0ZE71VU7N966d5NbFRIzMTuegKegQKCgUkvBEQypiyw7mocnrqNTJSABZJ_DFp3xbgtlkGcOKx0G9ot2i_2ecans_2HaxjVfpyW-fhad4mtob74FxJUv0dP0mI7FuKNu5uygdZz_JftpAsrmN9dEdZrJ5F3p05_A2SwQaobbfyx52pbL2vFkh_6vkSySBh3fNvPW1lWokHh9v0pyqpkuwaSDmaX3pcSlI7wrj4aDztq-d2NR6uuzZhGoTAzT6J2MI6as1vf3uuYo0Nbod8r7gfvts-DgTDWOqboB0sgcKF2xFKe0x6WjNxXPKp15-jOp5PAF2FWCB83opibI1WZn-3ULaEeIIwPsPmBU-XI_gAsZXpJLgX33D50dG4RoLWGIZa_xSXkA0MgePOwsTPWLRCwGCrpeoI6y17CQznislC1dJNosvaakJxcJTxPP2ocq42-TtRHYw7_dwE__LyWrciDTR5z6n6e2JdHkFe3Ij4FwgN25LVFTElUSlANh6w4EkT4nP0u1uA9oKwEJeNgiXOsGDThBI0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=YGnPLiGsVtEiY5g2fKef5KEV0heH6W0u813lKeJwNUqu8AnftTUgT-qWKJyxXm15QXRY6GqVZu08Y3ZyZRKzzOPqa5n-gDA8nFu6gN6IQMm72fDRrup32_e3KcwCscIyFtwGUgGLBBaDv0ZE71VU7N966d5NbFRIzMTuegKegQKCgUkvBEQypiyw7mocnrqNTJSABZJ_DFp3xbgtlkGcOKx0G9ot2i_2ecans_2HaxjVfpyW-fhad4mtob74FxJUv0dP0mI7FuKNu5uygdZz_JftpAsrmN9dEdZrJ5F3p05_A2SwQaobbfyx52pbL2vFkh_6vkSySBh3fNvPW1lWokHh9v0pyqpkuwaSDmaX3pcSlI7wrj4aDztq-d2NR6uuzZhGoTAzT6J2MI6as1vf3uuYo0Nbod8r7gfvts-DgTDWOqboB0sgcKF2xFKe0x6WjNxXPKp15-jOp5PAF2FWCB83opibI1WZn-3ULaEeIIwPsPmBU-XI_gAsZXpJLgX33D50dG4RoLWGIZa_xSXkA0MgePOwsTPWLRCwGCrpeoI6y17CQznislC1dJNosvaakJxcJTxPP2ocq42-TtRHYw7_dwE__LyWrciDTR5z6n6e2JdHkFe3Ij4FwgN25LVFTElUSlANh6w4EkT4nP0u1uA9oKwEJeNgiXOsGDThBI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLSe2eZduM90OQsbceVWBkYtzH2XIel1S8uIK8ArQnEwSZxGURSNUDO0heKiz40cQTPba9dKR-NQ2zY9aPbzWBcIIzO5fIdHB5qxSkZuwbV6mJordzX-iCn5LpzPZyOrZzIcve6y0iJsHwAJ8fe4jGFQTLlCGidE9x_dO7YBls5jhQWCxT1SB6m_2_8JXLkd6MqcR6GsO2oXfdmGGcetLLs4DUshg1oXT6VZ4WrujcaAZUGIWG7b5CL6FNgG9jwX6lS9yIzaKyJ7-Cxzs7NrmmN7HLC_7UL9y2ghgiCn0PJOSE5JvkybTq1pXKKah2MPSMk4yPX3bFt4Z0H6iAsVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=kD3yhcBkBTdRT4yEcASUaUeM4QOw6A_5lFYZtfpKocq2DCl-Tz5yA6k3ZvkDVvCqbfQMMIuDJRM6YqCJXSxILR8pamIalogzlLQpfm-INsr8zW6uBUkOY8XKIjl0_vSLvv80ALl30mfBF6mU1UzYDLLRMI6JiXczZbYTu_sjwDiFSC_6gfsZ_c9md_dOxl5Af3Jt5pu5x9wx0X5xpmR6ypui43Kear3JhYUJx8toc-Hi_TcGS7QanDYuz5w5sEIFf6tLabg_BTYU9Uucv7XEPJbAsK2Q0tjGi-JsrvEOaXOHLJvisqjGyJITkz_X44nhftomZeDcykh1koG_Vo4JOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=kD3yhcBkBTdRT4yEcASUaUeM4QOw6A_5lFYZtfpKocq2DCl-Tz5yA6k3ZvkDVvCqbfQMMIuDJRM6YqCJXSxILR8pamIalogzlLQpfm-INsr8zW6uBUkOY8XKIjl0_vSLvv80ALl30mfBF6mU1UzYDLLRMI6JiXczZbYTu_sjwDiFSC_6gfsZ_c9md_dOxl5Af3Jt5pu5x9wx0X5xpmR6ypui43Kear3JhYUJx8toc-Hi_TcGS7QanDYuz5w5sEIFf6tLabg_BTYU9Uucv7XEPJbAsK2Q0tjGi-JsrvEOaXOHLJvisqjGyJITkz_X44nhftomZeDcykh1koG_Vo4JOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=fssFc9Yf3ueKNuSumlC2MMO8h3eiXVP4pLTs9Ee9vs8Tm1wP-DtNXoqiiJXcMuf_O7kVOwfdVZWb7P6E_eokyVI4Yy9lUXZrUz3G-k4Ai1GwM5_XMA7NMAStBQVsyESMvwhxWdPYWxXgfIDjiPxDDjse3E90CeRaXjThSGL87b1jVg9AqErDTQdNvFefshp1rGAapglm9XUetlpjLG1AWelt0L5Lrb9UShvL06HU0pYg0XrGzoJG4-LpcWjv19VMpcSVxLgzeYyEKTdebyz1B9cLcShWFKwj_emMaaT6KRHc5-DtpSw1PQxtfzOhmldAgwygSTxbTLDEgHSZPf_Z-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=fssFc9Yf3ueKNuSumlC2MMO8h3eiXVP4pLTs9Ee9vs8Tm1wP-DtNXoqiiJXcMuf_O7kVOwfdVZWb7P6E_eokyVI4Yy9lUXZrUz3G-k4Ai1GwM5_XMA7NMAStBQVsyESMvwhxWdPYWxXgfIDjiPxDDjse3E90CeRaXjThSGL87b1jVg9AqErDTQdNvFefshp1rGAapglm9XUetlpjLG1AWelt0L5Lrb9UShvL06HU0pYg0XrGzoJG4-LpcWjv19VMpcSVxLgzeYyEKTdebyz1B9cLcShWFKwj_emMaaT6KRHc5-DtpSw1PQxtfzOhmldAgwygSTxbTLDEgHSZPf_Z-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=K3LoRWIFJrk4fgov8DwA3lL6bzolEpPxzmpuLzoj03wA9CBHLuVyHLPbYvDc5UXwwd_hFHQpLUQ8HCRlV4rA4ikA3LMCUCpYA2acvADY1t4_BflmMKSHgdqYfVK9gJc8xXd7Xq5rDmjHYIfi3_aG1BAUxnbAEVIPTFxG1LeHQQ38LQzijK-THEvGsugnawPe9hNKu6KfYb1qZRUUacvRNUEAO1j5XPlyySJ1v2KlKGdptjbrAsPAgWxF5W050nfz4RvCXT5sHwn_KoQ4ahHSGsQ7tmTRmkEMTWPmeAUkLPRBECS1bowAer4puUP9qo6lZ93V2z0s2txMj7JcWpcZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=K3LoRWIFJrk4fgov8DwA3lL6bzolEpPxzmpuLzoj03wA9CBHLuVyHLPbYvDc5UXwwd_hFHQpLUQ8HCRlV4rA4ikA3LMCUCpYA2acvADY1t4_BflmMKSHgdqYfVK9gJc8xXd7Xq5rDmjHYIfi3_aG1BAUxnbAEVIPTFxG1LeHQQ38LQzijK-THEvGsugnawPe9hNKu6KfYb1qZRUUacvRNUEAO1j5XPlyySJ1v2KlKGdptjbrAsPAgWxF5W050nfz4RvCXT5sHwn_KoQ4ahHSGsQ7tmTRmkEMTWPmeAUkLPRBECS1bowAer4puUP9qo6lZ93V2z0s2txMj7JcWpcZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=Tbd9vaEdOwL5HgE4MmVIhtYa7pmUZFEA0fP8xFfjFzG4izauS_1vZVp5ZYykF0dOeQCssHsYJG6NFPQ2hw3ejk-DRZLpgABd87ZM07JhBhvW9bSI0FOTfm8UfCTsOMAsa-vTjU7Gu7Y5hSY5MkCTdzjBI1N0XUzvXT4799K02xkwm3I1nb9_zQKpZYOSSq_jkRprGGIcaF9BLl_fz1CMdFvRgghniZIXjxWPqLqqfW4xDR5VO1CgYTd7mhICOSY3Dkzl-wNnSZKgixTx7cbQrSnNznzCF76P4sJsYYJR-bVnEC5w5Qk506GFLHQaa5pCQlcNc2gYSeoNsCJTIir8vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=Tbd9vaEdOwL5HgE4MmVIhtYa7pmUZFEA0fP8xFfjFzG4izauS_1vZVp5ZYykF0dOeQCssHsYJG6NFPQ2hw3ejk-DRZLpgABd87ZM07JhBhvW9bSI0FOTfm8UfCTsOMAsa-vTjU7Gu7Y5hSY5MkCTdzjBI1N0XUzvXT4799K02xkwm3I1nb9_zQKpZYOSSq_jkRprGGIcaF9BLl_fz1CMdFvRgghniZIXjxWPqLqqfW4xDR5VO1CgYTd7mhICOSY3Dkzl-wNnSZKgixTx7cbQrSnNznzCF76P4sJsYYJR-bVnEC5w5Qk506GFLHQaa5pCQlcNc2gYSeoNsCJTIir8vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7rPDzED3lH8vwLsnNHxAI4BmskBuTMJiaGqbsiUP9FKkzS6PnasADEgePtBwwwhmra5Fmwr-J850McIkorp0VKarpKiRj919otDRHZk_U5zXB3An4in40NfcUcEYkQe8eRPVnXE6G4ZI0ujxBLhn7uOA8VXD7VdezFqzKlnv7IMQLS8xWFd7fVi-lu6cYkplY33lISYTvhlUg4Iip6ZCxrTI-WX3btF06k-2-V32YYztR7qycXsscGBvyRdUmCUwpUPetq6kdDk7zcnXvK4FsVFxujasj2vgfjsl6t-nbFls-ytJkj_EWKpSUj0zct49bX_QyAy3EfTsWGwyHaeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaB0u3bTV1BN8--_aNimWdBlkv311SKU_iRbZqUwChpDWR_MLDF5ChLk7mhzk2mQ9b6ZkgxpJDhgb3GBXofruepyivQJh9_oR92orLOOGIGLsE0KFnVMfXMngiZY4qnWOBtS6rOrVumxHUQyOCjrgHfrz-qiBvnprJ2CgmWDh-MU4_ABdSNb6Z9TaAq5JEQCx1VBXECaAFVZvZtOpe8yUZawdmHGwG6ZDpNF1NnGiDXE5Fw9vh8ZbhJutrKeaOcHOT4FsNuVpPO2sw4TVqvns7wNDazmeKPSIQlwUU5I07neKA_wbyW0nDVFqeWMOzD9Jk0Z2SooFNnQ-NQoFJHjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfYY603UtOSls92qzW4zIbkYS-1MyYGYkoIgPu07aF61Lq-WesiFfDPewxGNOJhLWWyUMQJiYU06JuffZX6prbLeIAmnCCBbhLOri9W3WRvX5BwWpgWtQ35NOopU9XoGTrzBeTq8gSA6H9Xj4ZxmasPxrPrhV2T-b21nyJB42Z2Pbjc548Y-_INpU6qi3QskosOPbbi9mKso6fX59oIdnT3moAMjFtBrCa5ZJSYQRUHAdImWd_ZwczixjR4wVBOqmm07joLqg8Itwju-wotxNq_mtQTIX_GmkKpK6DXKuKdwkNwwIvYbizHbKDeWtbxUm3KQg09n0nlqvdKZQ_Ne9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0f3YTS14-shRjqcRTtHlo5pkJ5FRHg838DSMIsJpUT4l8nLPL-NLdTVi8p7YGbA8w9VSEIlLTeEHV0zWxqO0Arit6qvsLAcqVMDCGFU_ufMWPALfJ8Tj0nw_3jKT3tqCV8SLTQBckkbfrv_Q7bMa3Kp6OFbIFF1XU3HlmkRVA57_w-mNTi_1U5JIZ24OLUIoTINzESVHlrCfUQvTrv9_KrTq10laGWrCQ6YN4sld7mJn9HXBWhNYXUPZ6HYexFCWSbxy2zVt3utM0hS1vqNXH3vVKlAT7a8cqyvsV1-Bpss29ILSY09-AeMXmnRTc0JKZYlfAzEfdkFHmG82r4oUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e1haNMBeoF-PWEanVSW7OIW8r8drv-9T0YLzZmfLhlWU8yTtaDYtii0n4SRga9dWCkiUZ_HvDKNai89WGlrILWoWLNBzcXuycO5pu3XJCfxDBnqOgIW2OTAqw7FTB6OATy62w1xhmZFpHf-1v1o13ZjrVO29OEpeGtSeeFPHX3wRccyXs4A27Y3yBHHcTQBVJCIWgljQ6z83Y1vZTu13GLtrMGOk4kUgUan0cBvVRpVUSWGVoUp_tKWZpIzuFAG61OlEiHjgRiIF5cjjne4WDZLvP7sxIA1S-7AJc8fpxCvjCNwSz9VJDsdFREFiKaVEUr93DyWOzJxDhr1oPddzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBrKUYEsG_-5M1gMGWen7IhjqJk6Pkj74YjQz38uN5BXySwJuIAIpi5H3YA2SXPOjBN9CY6A4ERrd8KLPX9-xt1YTF-7Gk2QYYy4wh5li7mZbEO0ZEE1G7nNTiQ7qpYXXo8pbdr00AxEeieZhGhDWdN1rPVyxaOnC5q9E-RsOEMk080VVA3fvVE994FdgMWd5zyv5IcDW6Lzbl_BPF3ixh5vn8WlsOE3gJx7sYi7WczpBdpv4dp8CR-BmF1gTQv_TQv_cPX4Pv_V00Eq89Lh7AnYpQOlBkDBMTgZJA7xWLrSI0mNIyGmRr4TL8pQ4aZ5_kkyJQeu1CYUWDlEhBkyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsX0deTreFmG1mMV8dMPlEaBImDfP0sXqmWLTDvTGrx7Z8cwhizAoC39sf6jRTAKx6n-lbhkV3q-5jn6NO8JghMiI2hATdAka6vR63vT5_6VA9kHI3yYWvPTyBZKqh9zfrvZoL6suiUZIQFF8TzgPaGh99vIIVFbwJ1cNjDLPe0siVpfA8NB_48wMeIhKsr21HPtG5PnJAs5CT0P4Z_qR6oHdu4pkL5aijlb8uWxzuMoOy8i-mraEcdN5yw0fNtHskPApWbxwjTg8cxMjZ9IcSMSRHoFKBSvZCOoRRsY0fwv8G0sxXon6_a0Bpu0EKxyBmvUa_-PUlHq0TK-IU-lVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzUSeLI4TKjHx6nCJ4cplST1F4fnO58N-I0hcnsjOU5Bek7bmON4mdeZ_HbicLqRUFMyVERbqi-eNPLnY2j-D8Xl2aoku23-R_1TaRr5h3t8uIwSitXE5XEGezcHAcI0U0VJH7UFhC5IdZajlBtJAfN-aCV--ODQ1E3E9ZK4xPGvqvsPYP_HG3N2f1R-LMqxakALt9O7TXJJzI_-VUpeqA42VPqbWmpw8oKFgJhiBYpIUDq2isvCbzwYIrfsnXxn3EVdio33NQiAXB4i5FcAFpCQWErI248XJd0vkDqVSAg_SPTu9hUohOX7gqMkRITnMROjXcbfDeL44BSBLCkJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMjuRDN7xounTwFOmiayzlDWgaB63ci2WdJE6d8ASQtNOry0qms1A-tznFZ0JWm5d__1nFjWYxEIukVkcQbDmL09XyHDpWKcLkvAVbmphf43IYiVxUO-WOr8les0doW4gFFFZfZrPw0t6D3YYCHucVTMcf7oNNm6SwQhJF2iFCfEdmVBph5tatR6-XLNpBRjEhJWN_xqLJBstaOslJsPjwbzafCZxr97If85KRHgGVwS0mbzdz9uO0LJpUZ7yktH8xQHaHmfF_P67wvfnAP-Cjf-uY5UtoeFLzWXYgZF8Zr8AN8KNnwfk93rL2nn_8cwMIyOVvofpHNXv_w_ihn6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVqRC6l7otXtXmByu11LngEAzYuvvPP_leLb-cN-LerriQAYxVnw55-Zbxyj5JZUP7AxtfGmm2w7xzM0mGfvsM_ekkxUwIB6QktND7vMoHNnjVh7dy2JprT89_bLy1LWmRsOSmNu5WjYYIpMigbhf5jecP0UZYGMpwnyafUHr9Tsgp9sJYyDRQwznPbNZqgoB4RMe9ycYCE15f9c_pnitrgx6irg4aHaso-Us9vBqtiHTHq-YgwcWcObKgt3SfGSs6F5UjZRoH7TcGqWx0oPH0KRsUqxto1i9HrGP-_ox7T4ZeXEimh3uU1cVA_1ucwlILUibpYHUURn61TyJYfLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/makWfMevnq3HjwlHMBjwQ61Yw4MwIF2B7lcP5whaewyFb2nwoMpHI2CcY53--5Qa9y7x1QC14CAjX3pnuMKsmRjCqrpaKbQRKkRti6t1BQaEckZBBqel7QzOvfl6uAfsV43RWA3VA2CA0taQ2famNd1xZo7s6klLFwuKY678glFN6Ubj9YDxdS8fZn9TDRHrJUJ8brXhyj1-5pSlZ3AOXieQ0Q2u5IydkBD5Lv3k1aqeOGY_n4CtLO6-MjkwqI85JHbRX710yQc3c-XpslY32uOOonIxbWua3zEDCGx1qhU3K5LXwajIWz6s0LhdmPvbFIPkbLQIplyuH2sj9rqqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au6NI1iC6HGTsj0p5lB2RELw6xMdK_CxVZnwOm-K0LxsSfwCND4kX6Q6qKupFsAoLYOxvMm-qE-S1scGwBBVu3FbnMwrSRVYSuki7kkp9MkXlx-wpG9eDGIxLv9uXh-4RmVZIJ5reM0NRrAZWsqq6gmx_Ha4GvvH44ldkUpbC-h7IMsOewuxbtlOXKZG94L9hjPcQmHL787PNENEgPC9aKn9KXVEO7L-Ze4DrQJGz2qjOIkzGt_jtDvZJM5ciQWTwBHjNa-Xh6cTRi8B8bayfSxy6z8hpKTGaGgy_LduFnHlJy6Kuu-qLGh7cBGwMxr7RQbmztJFO-T4jrg3L4RxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4kNUtft8YpIDwMTzynUjT8yYm6K6LIoPIOh04gcBbqm2tzpo-1TQwc5mtVzuAtiwz-FcirXPoIoqW0oPMllutaF1XH8vV2iJeDdAu6OkK-1chkAPeZsTn-D9ucsJ8r4C5c0DyXdKCqXqYp1UzMsF_Y6K7TCknWvANThF_Q7AjUVcjO4SH5CmfnjAzZ03m5ej6ulgr1EQE35PTzmgb6ouAwNu0dpzp0i4mNczMNJ0mSaZTmeCa3cQPY_olphMfidS937NMFEwqxTOV7VaxupfDgTsHsOLvRwk3dfu5OxHke5JGa9zjjmNgaR4UFOkBqsc-ARSrSHvBua-R2oCevFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbPIOtQ-u_ykbpncxUIQ42PTzMjXnI3NqouD6CFFLpemdbKmNI9_gDke9j4D25rEP5tcDYwVATy61XNteKKmX-f0OwoPh9TSnGCE3AMU7f6paGLn0xMRk4kj51hfUri9dqc-h70DHrNEwBEuWbdMYsBTY6HNNQp7c1LHoktoYzeE_9gJBrC9zpgzWnbTmme81v-kSzr0DzTMSGVOLLfGScO63jszKVs96WvuXwOIjDDc5KWTcYZcB0wX-YidCXBq7sAp-gfh0qdeMtRQM9FqDFbk99721M_027ExRQItQvD4iyJNnRY56VYFg6D5_kQ5vnkWcBjZjNIPoP9TZJSbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYuTjAYyThIp_ijqbifvHvfC7vwq86-3vLhh6DQjZUV5Bi_RhAIFO9cgPqRxjExkbHkStuZ-ISaHHq-45167hsyC9RgflQZ4yuPO0ytEzD1WhjsaBbEshL0GSGzkANTQnRZ2BZDzALp0oLRyX-6HZk412oZrp-Z5pintm00GzoJbHnVWF78NgZAsVqwbhxwiTjTv_hipymCLrFUYitj2gb5uPTf2IgW6FVI4uDzzzQJkV_-8yvJBA-hED0Q1gxglexCkL9-EhanEt6atqYVqWxcsFmGF1D8P7mcXGl7-VCURTtyAGx8vLoTmG94BblMHxkpetjAly21TuJHFTOl7uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=BlGYfz8UFfjbL087K3i2weBRRIKHcqIQujBZq4UGXNCkB-mgjvR7VU_J8ttnia2mLzik36RHQZtCzzCKRbDuNlq96L-0_2vtUMu_jsjXuddech417fTwzwbeVjKL33oWpn7fUFAnSeAx4xUpX8Iopaqy6jNzl0m4m0HzjTyDaGTvO93p1ofx0oVl52AjY_MwTzjU3nqCiZYC9bXVk36Lhl16WCxO1dKMXT2m56M6gwL4QYePArhDTUPbP3O1MycMDEujpjgJ4qTHOKuGC8Afwo0vCzxEZDDutosEvNjONR4bvzJljnABKx1e7fQK5CB_niSy14c7GZAFFfZBUAcptw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=BlGYfz8UFfjbL087K3i2weBRRIKHcqIQujBZq4UGXNCkB-mgjvR7VU_J8ttnia2mLzik36RHQZtCzzCKRbDuNlq96L-0_2vtUMu_jsjXuddech417fTwzwbeVjKL33oWpn7fUFAnSeAx4xUpX8Iopaqy6jNzl0m4m0HzjTyDaGTvO93p1ofx0oVl52AjY_MwTzjU3nqCiZYC9bXVk36Lhl16WCxO1dKMXT2m56M6gwL4QYePArhDTUPbP3O1MycMDEujpjgJ4qTHOKuGC8Afwo0vCzxEZDDutosEvNjONR4bvzJljnABKx1e7fQK5CB_niSy14c7GZAFFfZBUAcptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XiTTWulRX89qJ4ETeaR_zt-RMWsOtiWfkfbj_6xXaYEEIhetIlMFueAxe02WbKRNQdH2A3E3my3QODCjiMttKJ6piM3CMW5bEJk8LAIZaRkj3uWHGyZjkcqT1eT1qPXEkQTb5YHOrVteqTuYzrUjuyn8cTYXjDDyTfEUu8EnPp9V5EuKD_jENUR1vKGt_sDZEGIYPEU1lPTwRg9Uh1DQsk7UYDIW8R29YIJKNFxHPCmZichOzECInFRx9rGMlBpFb-P_Fo2hNES6XXLziWghx2zyHjuOaEk3g8wTjOd7OAgupZ5GHx0ZATekIgc-4u58YC8Z0gfcu6EQBWFb9cft-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
