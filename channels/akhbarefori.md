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
<img src="https://cdn4.telesco.pe/file/oHN3QiGLRDYxAVSqUaSAM06iWOdnDDXaHZ_9ljPrJN5YvII6Twk9ip4OfBC577_Zq0bkIupPGbAJ_XoEKUDjYFmaYyT_XfAM0_Hf6MVmyNYeLZFCb5Cxqg1ssrJk_Hi1WhhtnI4-3R5H5VNtH32Ht8DCarKaAuSUH_8OaYW8ZNitdWTa5LdxtMXMwxCBotluVMg38bXwSJTeLcJ9Hh8nOkymtVZ_gSBQkiw1uqzEf45Y3cViJJbeMvdHnvqJsHk3DjiDL7itLpuJzrnbRYqTqLtzdzNpn2P1guVIPGHeE8WLEj8tTFC-WHYRR8qypdii0kduVygsHQgXYvdJUQczkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-686994">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نشست امنیتی مقام‌های ارشد اسرائیل در بحبوحه تشدید تنش‌ها در منطقه
🔹
شبکه ۱۲ رژیم صهیونیستی گزارش داد، «اسرائیل کاتس» وزیر جنگ این رژیم، با حضور «ایال زمیر» رئیس ستاد کل ارتش و شماری از مقام‌های ارشد نظامی، نشستی امنیتی برگزار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/686994" target="_blank">📅 20:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686993">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ارتباط هوایی قشم با دبی پس از ۶ ماه وقفه از سر گرفته می‌شود
مدیرکل فرودگاه بین‌المللی قشم:
🔹
نخستین پرواز این مسیر با یک فروند هواپیمای ایرباس A320 روز سه‌شنبه ۱۷ شهریورماه انجام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/686993" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686992">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتِ تغییر نگاه در صداوسیما است...
🔹
در روزگاری که مردم، زیر سنگینی جنگ، اضطراب و فشارهای اقتصادی، بیش از همیشه به اندکی آرامش نیاز دارند، باید مراقب بود آخرین پناه‌های ساده و کم‌هزینه‌ی آنان را هم از میان نبریم.
🔹
مردم چیزی جز چند لحظه آسودگی نمی‌خواهند، چند ساعت خندیدن، دیدن، شنیدن و فراموش کردن تلخی‌های روزگار.
🔹
در چنین شرایطی، تفریح دیگر یک تجمل نیست، بخشی از نیاز روح انسان برای دوام آوردن است.
🔹
شاید در خط مقدم این مسئولیت، صداوسیما قرار داشته باشد، رسانه‌ای که می‌تواند در روزهای سخت، خانه‌ای برای آرامش باشد، نه پنجره‌ای رو به تلخی و التهاب.
🔹
هرکس که بر صندلی ریاست صداوسیما می‌نشیند، پیش از هر چیز باید بداند که مخاطب او «یک گروه» یا «یک جریان» نیست، مردم‌اند، با همه تفاوت‌ها، دلخوری‌ها، امیدها و رنج‌هایشان.
🔹
هنر رسانه در روزهای بحران، افزودن بر اضطراب مردم نیست، هنر آن است که از میان این همه غبار، روزنه‌ای برای نفس کشیدن باز کند.
🔹
واقعیت تلخ این است که امروز برای بسیاری، تماشای صداوسیما نه یک افتخار، که گاه به «سوهان روح» تبدیل شده است و این، پیش از آنکه مسئله‌ی آدم‌ها باشد، مسئله‌ی سیاست‌هاست.
🔹
شاید پیش از آنکه به فکر تغییر مدیران و چهره‌ها باشیم، باید در سیاست‌ها تجدیدنظر کنیم.
🔹
آدم‌ها را می‌توان تغییر داد اما اگر نگاه و سیاست تغییر نکند، نتیجه همان خواهد بود.
🔹
مردم بیش از هر زمان دیگری به رسانه‌ای نیاز دارند که صدای آنان را بشنود، نه اینکه بر دردهایشان صدای دیگری بیفزاید.
🔹
گاهی برای آرام کردن یک جامعه، لازم نیست کار بزرگی انجام دهیم، کافی است چیزی را که مردم برای چند لحظه آرام شدن دوست دارند، از آنها نگیریم.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/686992" target="_blank">📅 20:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686991">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9c88ce4c.mp4?token=sB2VaMkP3M83SS_nV6b9e85YgQGAEI69kdXbxH35w7tS68fVI6Bh59yo9-BB5SiEnd2nsPmHqPbK-5xqmUU_p8biNqu5mpLg_gAyiEy97vG82j8lC_vW5TvzqL8jS7wAWj5QFZw9ECfH7zjmZB7_WXykT-6jqTBkrq8LKv75cXvxrAGy6eZ6fmHW3yKdZBx38UtVDDk4eb0breWNmbPHvTtceKUZTQw5XHYlhi9quDp4_97aywsJMm6Bd2di_DuvOPrUBcILGQoG4gTrQtjbwFG_E-5Hr9YZkZ4EkPtJISNOEsVeothHLkPerH1ZcrpNPC9ea3hadqwnlk4ZsBIzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9c88ce4c.mp4?token=sB2VaMkP3M83SS_nV6b9e85YgQGAEI69kdXbxH35w7tS68fVI6Bh59yo9-BB5SiEnd2nsPmHqPbK-5xqmUU_p8biNqu5mpLg_gAyiEy97vG82j8lC_vW5TvzqL8jS7wAWj5QFZw9ECfH7zjmZB7_WXykT-6jqTBkrq8LKv75cXvxrAGy6eZ6fmHW3yKdZBx38UtVDDk4eb0breWNmbPHvTtceKUZTQw5XHYlhi9quDp4_97aywsJMm6Bd2di_DuvOPrUBcILGQoG4gTrQtjbwFG_E-5Hr9YZkZ4EkPtJISNOEsVeothHLkPerH1ZcrpNPC9ea3hadqwnlk4ZsBIzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راه خروج آسانی از جنگ ایران نمی‌بینم
فرانک کندال، فرمانده سابق نیروی هوایی آمریکا:
🔹
حدود یک ماه پیش کمی خوش‌بین‌تر بودم. فکر می‌کردم ممکن است از یادداشت تفاهم که داشتیم، کار را پیش ببریم ... فکر می‌کردم می‌توانیم تنگه‌ها را باز کنیم، آن طرح از هم پاشید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/686991" target="_blank">📅 20:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686990">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdwwQQEaMMvljZkX4i29r6Ox0A_KLT76eoH41ETui-2Cm_LB9KEBYoJaMoSWWaAp7uZDBsYU0PauXtiGSKn65KDOUIrz1JQcfwYZKIhceAhQBE0JI1AFB7CUJFrmPdpZsgExWECWTLOi-NDT6wb2UthQ3SWzf-kWUP5C4nxGpaMNiR6s5nkPtqYhUjOn-0vCfRJK3TXvH7uttoLt4eGI15l-qtDd3tOx2qpwq8qa-ijM6fVlmk2ER0bT5L4iGKeaVC6VMShsuVU8zHoostleFg5lBa_VgNGdEZXl_PyaiXcz_YPCQ38wA0KQaPxwkRhxqIpDtxOAdcYMRrN0TKamMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کاهش سریع ذخایر استراتژیک، افزایش بی‌سابقهٔ نرخ بازده اوراق و جهش پرشتاب قیمت نفت آتی، بسنت را در لبهٔ پرتگاه قرار داده است
قالیباف در حساب کاربری خود خطاب به بسنت وزیر خزانه‌داری آمریکا:
🔹
قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
🔹
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/686990" target="_blank">📅 20:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686989">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
برنی سندرز: آمریکایی‌ها نمی‌خواهند تنگه هرمز به نام ترامپ تغییر کند
🔹
سناتور آمریکایی در واکنش به پست دونالد ترامپ رئیس جمهوری ایالات متحده در مورد تغییر نام تنگه هرمز، خطاب به وی تاکید کرد که مردم آمریکا نمی‌خواهند تنگه هرمز را به نام خودتان تغییر دهید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/686989" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686988">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZNu7XLcf7aHsN7FxZKI_mKX18-C-kOPvqY2CQEFwGLh06w9HHp4URwXmyRpvhVao2WM6nO7zpOptLeVnhRFbK9GRpWj98EFtIhWAyDu6bDk5cESEqP5gN-YbJD2lgLlc6d1wY7yGoqipIXDDYulZz4O6i2VEiQwsXzIe9X45ymUBoMEpTkRtZES6351CyNp_4e9Hb-4EjHL_rVX3Vr3oaI9qv3hCM8IzdzEySXPBA2_3sRSPm_H2e37-3q9vFofXDngEtyMk2yWe5jmChpVSzCsxCFcibyK9NiIgozRoSYvDnxSKQ4i9OY0meZ1eUIzZ1GrOGwqQzoC7hPfCNJJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب مکانیزه در مزارع نیشکر
🔹
دکتر علیرضا کاظمی، مدیرعامل شرکت توسعه نیشکر و صنایع جانبی، در گفت‌وگو با خبرنگاران از تداوم عملیات کشت نیشکر در ۱۶ هزار و ۵۰۰ هکتار از مزارع هشت واحد نیشکری خوزستان خبر داد و گفت: عملیات کشت از مردادماه آغاز شده و تا پایان شهریور ادامه خواهد داشت. به گفته وی، اجرای به‌موقع و کیفی کشت، نقش مهمی در بهبود عملکرد مزارع دارد و می‌تواند بخشی از آثار و خسارت‌های ناشی از خشکسالی سال گذشته را جبران کند. در روزهای گرم خوزستان، مزارع نیشکر از نخستین ساعات صبح میزبان عملیاتی فشرده‌اند که نتیجه آن، ماه‌ها بعد در فصل برداشت نمایان خواهد شد.
🔹
مدیرعامل شرکت توسعه نیشکر و صنایع جانبی همچنین با اشاره به انتخاب و کشت ارقام متنوع نیشکر با هدف دستیابی به درصد قند مطلوب اظهار کرد: توسعه و به‌کارگیری دستگاه «کارنده نیشکر» از دیگر برنامه‌های این مجموعه برای افزایش سرعت، دقت و کیفیت عملیات کشت است. گسترش استفاده از این تجهیزات، ضمن کاهش وابستگی به روش‌های دستی، مسیر حرکت تدریجی به سمت کشت مکانیزه را هموار می‌کند؛ مسیری که می‌تواند بهره‌وری مزارع را افزایش دهد و به نوسازی فرآیندهای تولید در صنعت نیشکر شتاب بیشتری ببخشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/686988" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686987">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار هرمزگان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3b8981a7.mp4?token=UkrHyj6ojZqTWFb4ppKUeq9f4PvHWdTJxvmJ-u8ujQ-lKE8sbmid8X9lEYOsi9CwmzSprffTYtTkSCreJM2mBhaMDzp9oO5-TRlWfxyqBuz_Q1RZbwGiCTaoHvAcdxEmJd_SUKQ_q7kwA0ngGOlpQbF2dF1TeFxJMAwnany700wS0V5WFO9sXB6G2XwKc-rqmSYNvOnpI7wJ5hWC9Hz6c9eYIcMSwIzsv_br5JdhGY1psd4Jqao_Pde0CTXNQsN9VYWGJIU0kZNYkZkCDH0pAVSFp-d-H8WbUJhKl-7paXdk1Vz3oLcpFLf6kB_qJYjuUnV_lJLZ6TBFRz_aMfAqIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3b8981a7.mp4?token=UkrHyj6ojZqTWFb4ppKUeq9f4PvHWdTJxvmJ-u8ujQ-lKE8sbmid8X9lEYOsi9CwmzSprffTYtTkSCreJM2mBhaMDzp9oO5-TRlWfxyqBuz_Q1RZbwGiCTaoHvAcdxEmJd_SUKQ_q7kwA0ngGOlpQbF2dF1TeFxJMAwnany700wS0V5WFO9sXB6G2XwKc-rqmSYNvOnpI7wJ5hWC9Hz6c9eYIcMSwIzsv_br5JdhGY1psd4Jqao_Pde0CTXNQsN9VYWGJIU0kZNYkZkCDH0pAVSFp-d-H8WbUJhKl-7paXdk1Vz3oLcpFLf6kB_qJYjuUnV_lJLZ6TBFRz_aMfAqIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصویر از لحظه تدفین پیکر شهید خردسال ۴ ساله شهر کوهستک که در حمله رژیم آمریکا به یک مراسم عروسی به شهادت رسید
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/686987" target="_blank">📅 20:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMvq3a4OZOgeaNM7IsA8-Tg0haDFbObOFTWgzTchwztAcDVunJ_4fF3pE9Odvi5xXJdb3ZZa5VAr0iAhDECZ6LkXaXRLpvZ-2Uo_CySuSLQ9kKWyqGBf9A_3XPAKr7RP45iCBbV4opL29IvtzrBmLcdt9nQpp0a-kcOuqSFUhXRG7SuczyJCQM0jqkTKjMVZI0XOTcMQRhRX1Dk09-u73n9p0mwXaPVHivwQ3ZTqUX7Cg-csuDlU6GiyytDEEPQe9HG0JecWymQ1EPeozXFX6njAm1YCb9JQDgIC6uXt0IL9Rl4k9XOx_bCxIBktJVAr4W4JWYxfTdjeHRZOnzAFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfDtDuIijcQU7_GPkSKys0WbsNkyDxEWP4iRQ_iSIVpSsmWRJUqUfvcPGRrABuhEfNnE7uj5ffBweCuixt6FqFFOAjkanf67CVs5sULSVvotqb30Edu3T7C4VUbFFcrooyZ81i1Gpg8nCFtiNMus1IezUNn6ppCB8rTyzbBd0-l0lHrC-wZHCgBEfm_GDg-5gES8ZHXxn9eyodaBB54O5wqRY7-rLE7njPtB5Dp2IKav_6rEb2AHUzsqrReHphu7frc24iQdwqqpEEr4XxN1JN25az0bwuwA7Sh0QyRMxhzDff5uK5dJQrmDU9H0bcX_fMNl5WM7jCER-TOJCb3oMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترامپ رسوا شد
🔹
طبق رصد ماهواره‌ای از بخش جنوبی تنگهٔ هرمز تا ساعت ۱۴ امروز، تردد نفتکش از این مسیر «صفر» بوده است.
🔹
ساعاتی پیش ترامپ در تروث‌سوشال تصویری منتشر کرد و مدعی شد، ۱۸ میلیون بشکه نفت از تنگهٔ هرمز عبور کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/686985" target="_blank">📅 20:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">10 Ane Manaee (1403-09-15) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/686984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه دهم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن
🔹
ادراک، فرمانده اراده؛ چگونه باورهایمان مسیر تلاشمان را عوض می‌کنند؟ [1:51]
🔹
فراتر از حس؛ کوره‌راه دشوار باور و اراده [8:52]
🔹
کمرنگی علم، خاموشی اراده؛ چرا ترک گناه دشوار می‌شود؟ [15:47]
🔹
هشدارهای الهی؛ وقتی تجربیات نزدیک به مرگ چراغ راه می‌شوند [17:09]
🔹
نام‌ها و نیت‌ها؛ عشق به اهل بیت (علیهم‌السلام)، برترین انرژی مثبت عالم [22:25]
🔹
زیارت عاشورا به دستور آیت‌الله حق‌شناس؛ وقتی شرط‌ها، مسیر دعا را هموار می‌کنند [27:48]
🔹
استغفار حقیقی؛ کلید قفل‌های بسته زندگی [33:33]
🔹
وعده الهی درباره استغفار: باران رحمت اموال و بنین [36:28]
🔹
رب لا تذرنی فرداً؛ دعای روی سنگ فیروزه، کلید فرزنددار شدن [38:14]
🔹
عبادت، جنگی با شیطان؛ راه یقین از استمرار می‌گذرد [49:04]
🔹
یک قطره اشک برای روضه؛ بخشش گناهان ۷۰ ساله [53:05]
🔹
از سحرهای تنهایی تا ناله‌های بی‌پاسخ؛ غربت خانه فاطمه زهرا (سلام‌الله‌علیها) [58:24]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/686984" target="_blank">📅 20:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of7d7gal5dc2xOUh_2XxyZf2YyMjYfT6KvCJoGLIr_f7yvPf9Tv7HDHzB85RAz_uHUL58lSx8XQFDLekfjEaEYwx0I94-g6TFGGfKyV6N7NxbuJjCHYaaeONKay0w17depZn_zT_dqOUrDaq37CIfEiDh8GTbCoCK7NTyk6Baccxvlu8T1z7opJ9U8PghdfwL3ABLz0X5u6DVCpd1m5f8uX7rdXF5c8eRtoUkPw6CvdUBrjl2gkeJ9OKJU_9ne-eI3-HQFitcQbnBU0Dmmgie6d8memj8i0j4v5YPQpMfKewRpw3HShiBjAse46a763dUmhL3RwDMq8ljB79fBN8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه ترفند کاربردی با تافت مو #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/686983" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
منابع اسرائیلی: حزب‌الله در حال به‌روزرسانی تصویر اطلاعاتی خود از نیروهای اسرائیلی است و خود را برای درگیری گسترده آماده می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686982" target="_blank">📅 20:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpubrelEffQ3d-4AZZh40iycxo1SNlfIhH0SiViuWVhiinA35iQhubNh8bq6AT-ODpOnExImJtsGv99iVeSglqmaLRJreA33pc22kmNEyJgCVzMaqv_14-WQBIu7B2aaK3WqU3dMUu2PsLZIimP5-Chs1_UjBKohjWDLDBsZsolpWF8q8-wQJd5d78xWwah6iuuzZK9JEZ5Jgfjo6BdhKGL6DpMtiQKuQzd4RDZYiOCveIwByQ7IEvU7f9Tk8UkuF2RRO3xU5Sju8ZNs8fsn-fmRZds7Nt9pnc_EqH7GEJNc59Q0q1g_eRT2gZnHe-CSJMMd2H1DddcECWsIsubtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#اسکورت
به سرعت میلیاردی شد!!
🔹
اکشنِ جاده‌ای و پرالتهاب «اسکورت» به کارگردانی یوسف حاتمی‌کیا، اکران خود را با قدرت آغاز کرد. این فیلم که روایتی متفاوت از دنیای شوتی‌هاست، تنها در نخستین روز اکران (۱۱ شهریور) با جذب ۵ هزار مخاطب، از مرز فروش ۱ میلیارد تومان گذشت.
🔹
«اسکورت»، پدیده و سیمرغ‌دار جشنواره فجر، هم‌اکنون در سینماهای سراسر کشور
🔹
با نقش آفرینی:
امیر جدیدی، هدی زین‌العابدین، افشین هاشمی، مهدی زمین‌پرداز، هادی شیخ‌الاسلامی و با هنرمندی رضا کیانیان
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686981" target="_blank">📅 20:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b50a317b.mp4?token=oF9Gi47EPcvGdVdH3WoLJnXInSCQuP7rwasS1063_iuspDjs0vlCCLvpQiSXPue3wKTk4_gGAgXn7O6YQWfK4LnebwE7_4mwCxc7uqX6A9gZEllxHai1XIiDuu8F2aol5IolYsp838sUtKGIh4XjGDUhevJhrV7XYGrYQaOpAyJcfRjLDR4DOR7aXMm_D4s82405uNAWlG3w8cKjOKKCcQsCtbhWoqdGdbFz4Ya8G9GWa4jLg4wiDnrr-hcpPjjoRXKl7TMQhHowTbVauhXuymWMEdE8IPhMGXTvcxrgt3hB29eUN4rUC7TBNQDM6IO2RMr02LTY1WULlVvnZCOJ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b50a317b.mp4?token=oF9Gi47EPcvGdVdH3WoLJnXInSCQuP7rwasS1063_iuspDjs0vlCCLvpQiSXPue3wKTk4_gGAgXn7O6YQWfK4LnebwE7_4mwCxc7uqX6A9gZEllxHai1XIiDuu8F2aol5IolYsp838sUtKGIh4XjGDUhevJhrV7XYGrYQaOpAyJcfRjLDR4DOR7aXMm_D4s82405uNAWlG3w8cKjOKKCcQsCtbhWoqdGdbFz4Ya8G9GWa4jLg4wiDnrr-hcpPjjoRXKl7TMQhHowTbVauhXuymWMEdE8IPhMGXTvcxrgt3hB29eUN4rUC7TBNQDM6IO2RMr02LTY1WULlVvnZCOJ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
𝟲𝟬% و %𝟳𝟬 تخفیف تمامی کالاها
در جشنواره پایان تابستان «چرم مَنطِـ»
➕
𝟮 میلیون تومان هدیه اسنپ‌پی
با کد: 𝐏𝐀𝐘𝐂𝐖𝐆𝐙𝟓
در تمامی شعب و سایت
👇
🌐
manteofficial.com
با اسنپ‌پی بخر، 𝐁𝐌𝐖 ببر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686980" target="_blank">📅 20:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686979">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
کنایه سفارت ایران در لندن: برای تبدیل عروسی به عزا، کار را به ارتش تروریستی آمریکا بسپارید
🔹
سفارت جمهوری اسلامی ایران در لندن با مروری بر سابقه حملات مرگبار آمریکا به مراسم عروسی در افغانستان، عراق و یمن و تازه‌ترین نمونه آن در سیریک، در پیامی کنایه‌آمیز نوشت: اگر می‌خواهید یک مراسم عروسی را به مجلس عزا تبدیل کنید، کافی است آن را به ارتش تروریستی آمریکا بسپارید.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686979" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686978">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh6t8yjdNQGJV8oSeh1vaC9fGhppJ8LKkM8KXE5cv9q1fpVx-S02fFr6PXNcsrbeN3mNrTxX8f4uj6bEvOqyaxib8Alp2Rb5iNByg4PZbTwDf2mtJDuQHAx5xaXrxBPSbOzjWvdlUk9nrzpZyxobM4z9RAJ2LkDqTgOU_fnPTzhYYrQOOT_ZliBvABAvKUOXLZkApUPSkBcD0uihzcg8HbN6Wwla5N46UNPJeKMEqySWIML177nYbVDTlmG_hWbl3DEAH0lIb_QvbgNHgzxZce-Q-Ssasp-AFoJjhma5XFgo3W7ZdJyVnjVIKtIvoa76wOhrmCrz8UXTh_71FsDMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لس‌آنجلس تایمز: ترامپ چنان رفتار می‌کند که انگار می‌خواهد رأی‌دهندگان را علیه حزب خودش بشوراند
جکی کالمز، ستون‌نویس لس‌آنجلس تایمز :
🔹
ترامپ در دوره ریاست‌جمهوری‌اش چنان رفتار کرده که گویی قصد دارد رأی‌دهندگان را علیه جمهوری‌خواهان تحریک کند و کنترل این حزب بر کنگره را به خطر بیندازد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686978" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz9GqylP_YHDNaKHrBeFOWyMhKER5MMtoATv1TYtUD7Aomhd1vkkiEGFOy9wc4shLnML3pkefvErejcg-X0HTEDhgynnVdV8atyYJXdW6WIZRBoZbwGCDtqMA7BEbUk0nlk9EIAy3VyCEzyjNh7xjViLrOuC-xFZ5-YD_E-KlIPuxp115XENjNkvfjBKs5Myj6iuKe7i7e0_X69lTTdIdiXk884665i61Dy_zHMeQCdFdNduJuiqs4zuVe-KK-cNA7mrcsOC7wU4b6qrNCfR8PsWtOHUZzBH1KpYN8-i5XpRXuIdIyoTr91jpSd2MMd6bRGWWok4nPNh86C8pdujOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUOHi9DWB7Z4J2ErV0KHJ8aOUfrlZjxYiNlJTbBk5nXA9_1iuYbY-TR_z4GtF-3TQ6ANBwE678heKt6oTf7GDDUGEwK-CGvpTcOpscakoySwwFqfYlZcM37qMosWlRZjYkiWuhqSnLjwPedfUurNavvAA7UEE2sUsV4MOEx62H9MqeSn_SaSP55VDJm1u_K-ee1xDgaaOvPlyWS6RYRkRdnCWTk5DHE18GOthVzTXq7pYOjE_imrrWx-NMFrsWzCMn1SumKcMj1OeoIDWdsWWbhgDWo2anPKmd0CbGmZV0ZyJLdPe0MJkzJ_vwhgNp8QS--CVobqBtynsZzru7IK1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیوار نویسی‌های عجیب و معنادار انجام شده روی دیوار منزل رضا کیانیان بازیگر سینما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686976" target="_blank">📅 19:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنگوی شورای نگهبان: زمان جدیدی برای برگزاری انتخابات شوراها اعلام نشده است
🔹
همان مصوبه شورای عالی امنیت ملی مبنی بر اینکه دو ماه پس از اتمام جنگ انتخابات شوراهای اسلامی شهر و روستا برگزار می‌شود، همچنان پابرجاست و هنوز چیز جدیدی از سوی این شورا اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/686975" target="_blank">📅 19:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861094ab9d.mp4?token=ORUSUEnoX0hgxi_5tPhJBUJM1r-68qyivRiKCcFQ8RrRjAoD0IRGXND64xxRGrXv6ikOuSP-JjVNeU3qKrvjPiG2vjN_yp_QQvtrnvNKBq33YcYr52SqTSQqHi4-4f0J1uE3Yl36XKSUiFyf63KvKkLtRbrSCSWrwA9YKLJDZnz_NivHBrYcTT2ZsHOW_8g2nb9Xq67vzsjJsq2ZOeXJYlcEXIrym9smiL08pbXZjIhJl5yMgNcbb6igJx-0BIiQTOp7mxh-nzKSdXDvbrcxXt6j5hMGc_6yIZ2FBxChpbY5ehKC0X605ahkAZeZps0XB4-23Gmee-nsX2z3NHFPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861094ab9d.mp4?token=ORUSUEnoX0hgxi_5tPhJBUJM1r-68qyivRiKCcFQ8RrRjAoD0IRGXND64xxRGrXv6ikOuSP-JjVNeU3qKrvjPiG2vjN_yp_QQvtrnvNKBq33YcYr52SqTSQqHi4-4f0J1uE3Yl36XKSUiFyf63KvKkLtRbrSCSWrwA9YKLJDZnz_NivHBrYcTT2ZsHOW_8g2nb9Xq67vzsjJsq2ZOeXJYlcEXIrym9smiL08pbXZjIhJl5yMgNcbb6igJx-0BIiQTOp7mxh-nzKSdXDvbrcxXt6j5hMGc_6yIZ2FBxChpbY5ehKC0X605ahkAZeZps0XB4-23Gmee-nsX2z3NHFPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای کاربردی کوچک برای زندگی راحت‌تر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/686974" target="_blank">📅 19:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008e8b2ff9.mp4?token=Ad3fcsAezC9u3yzucyJGLdRQVsTR_weXLuSYNm2zETEunNNadotRcpCoGE8hhDsdIfJ5GJoSdqx_TqDOCOOUl1LZwgtc-arAKNRFIMkTOFTVLvop9IyS3UMIseqUpmrz_Wttk_1FjvMGuVto8h_TjQxucsMBzVAtygxmPT7W_iRILPVlFeKyw7NI7rh-mhDFyM3GRYajf-_AcbvcYI6yyty7XtqkTBzo1vLAqmkkTWWtybbX78j4-ygrF0AoA0pUB73-jtaPP8VP-yTsdyyAvnUXDbwIucft8unTjgPTfooyLOLEg4HsxtsJadFzNv5Tk3zEKogXRoPAJMQq1_IzN7BwYEpT1CLLIz1SA6GwUaNdy3KDns2JHaU8X7uFj46gJ9AZhcAlrFeRpxULUo4fNrclgz0uqfdlYhBLTxnugCIKqE_FXa5wEkBZvu7OZr-sZzPJwaFJl8w6GPSoGPmbumCivFaSoUNCdiXn7BkC0ZAAsDptINHucnzy8ntIxF30yqk_xjcygpYpiMvFsbwZPvOYxvaO-7bvDDnoatHJwlZnpYeD9DjUkg3rZQQLYlekwU3EvW_4NmgqjCNJnj5TsLUpszidZqU8ivXn4PaGUFewWYWk_TxFuTQJt8B8grXDeqvfYCJUkbv8MTKKCpgccz7nBjLdNqpjRPmkRy-Wtts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008e8b2ff9.mp4?token=Ad3fcsAezC9u3yzucyJGLdRQVsTR_weXLuSYNm2zETEunNNadotRcpCoGE8hhDsdIfJ5GJoSdqx_TqDOCOOUl1LZwgtc-arAKNRFIMkTOFTVLvop9IyS3UMIseqUpmrz_Wttk_1FjvMGuVto8h_TjQxucsMBzVAtygxmPT7W_iRILPVlFeKyw7NI7rh-mhDFyM3GRYajf-_AcbvcYI6yyty7XtqkTBzo1vLAqmkkTWWtybbX78j4-ygrF0AoA0pUB73-jtaPP8VP-yTsdyyAvnUXDbwIucft8unTjgPTfooyLOLEg4HsxtsJadFzNv5Tk3zEKogXRoPAJMQq1_IzN7BwYEpT1CLLIz1SA6GwUaNdy3KDns2JHaU8X7uFj46gJ9AZhcAlrFeRpxULUo4fNrclgz0uqfdlYhBLTxnugCIKqE_FXa5wEkBZvu7OZr-sZzPJwaFJl8w6GPSoGPmbumCivFaSoUNCdiXn7BkC0ZAAsDptINHucnzy8ntIxF30yqk_xjcygpYpiMvFsbwZPvOYxvaO-7bvDDnoatHJwlZnpYeD9DjUkg3rZQQLYlekwU3EvW_4NmgqjCNJnj5TsLUpszidZqU8ivXn4PaGUFewWYWk_TxFuTQJt8B8grXDeqvfYCJUkbv8MTKKCpgccz7nBjLdNqpjRPmkRy-Wtts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای مهیب در پی آتش‌سوزی گسترده در افغانستان
🔹
وقوع یک حریق بزرگ در یک فروشگاه عرضه گاز و سوخت در شهر جاغوری افغانستان، منجر به سلسله انفجارهای پیاپی و هولناک شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686973" target="_blank">📅 19:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686972">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg8Vw1jVxJ9MIUHeeY0IzA-bU4U84SgDOvQn0pxJx5Q8WrUV5U7X8jejHlpm7f_I8OFmEaVOgGnwKAvzcXSwPxr0sXt7fHkxAUqSDCbtO-bg1qelTLC-4zk8WcbCxyRqiD4wUMkWnzfeCYFQb7tu6kuO_TEfPCR54i8q5NvSMVX-WJVqHxcxXStXE0WMU0kFWyZIsYx8MR6VzgtIW-z76Sq83dzu2CStEpIzKTwo3P2qJNPni287iAvZF0od0c68zbFDPbs6n1f6Kn3A01tsra0c-Qf7qZsDBt_3_6KqdhCKahWo5C8aPTjPzneR-_ZuEp1ciMx7ge2G8HzIVFKnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتازی آمریکا در سرمایه‌گذاری بخش خصوصی هوش مصنوعی
🔹
بررسی آمارهای دانشگاه استنفورد نشان می‌دهد  آمریکا با ۲۸۵.۹ میلیارد دلار سرمایه‌گذاری خصوصی، در صدر جدول توسعه فناوری هوش مصنوعی قرار دارد.
🔹
چین با ۱۲.۴ میلیارد دلار در رتبه دوم و پس از آن بریتانیا با ۵.۹ میلیارد دلار قرار گرفته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/686972" target="_blank">📅 19:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وضعیت ۵۲ هزار ایرانی حاضر در کویت نامساعد گزارش شد
ادعای رسانه Newarab:
🔹
از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران، جامعه ایرانی کویت که تقریباً ۵۲۰۰۰ نفر جمعیت دارد، با فشار و اضطراب فزاینده‌ای روبرو بوده است.
🔹
مقامات کویتی امنیت را تشدید کرده‌ و تنها مدرسه ایرانی کشور را تعطیل کرده‌اند و افراد مظنون به ارتباط با سپاه ایران را دستگیر کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/686971" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ترامپ کانادا را به فروپاشی اقتصادی تهدید کرد
رئیس‌جمهور آمریکا:
🔹
برای سیاستمداران کانادایی، مثل نخست‌وزیر کارنی، خیلی خوب است که ترامپ را «دشمن» جلوه دهند؛ اما وقتی اقتصادشان فروبپاشد، آن‌وقت معلوم خواهد شد که این رویکرد از نظر سیاسی چقدر برایشان بد است؛ بدتر از هر اتفاقی که تاکنون برای یک سیاستمدار کانادایی رخ داده است.
🔹
فقط صبر کنید و ببینید!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/686970" target="_blank">📅 19:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون رئیس جمهور در امور زنان: مصوبه صدور گواهینامه موتور برای بانوان نهایی شد
.
🔹
راهداری گلستان: جاده گنبدکاووس-مراوه‌تپه بر اثر سیلاب و تخریب پل مسدود شد؛ تردد از کنارگذر انجام می‌شود.
🔹
منابع اسرائیلی: حزب‌الله خود را برای درگیری گسترده آماده می‌کند.
🔹
سفیر نروژ در ارتباط با توقیف کشتی روسی به وزارت خارجه روسیه احضار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/686969" target="_blank">📅 19:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686967">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb6c5b9fd.mp4?token=vm4eyU3am3OEZPgmyQqP0Zi-1snvB_EKOzTm3Q_rQCBuamRlsjUJ9ZgCaPP4ED9DByJ5iVzPbsPVSQwXhNNCxmjkAnhGf5GkG3aEJtErXGu8wBMJsf-W3tardcm6x5szfg5-GE6o1zYriz52sMbl5GsecRydQMf8iRqMf7CXv-hUBNN3I40tVXROiFgypNFjiGFS6WUOKQA8cMjcuPd32SCycxF4OAW70qn-LhcugNbAIVRYki1J86Cp_rsi6QPr7ZpG1bJGKRG3vgF2549F_EnUWgfLFOsS_UARzlBxZAEpsqOIgYpZH5tfJR0jdJudE-sj2rVSuNbl0GNdFhkkXzBlJ4R9Qbk49NUSuc_d-DwEHgaPXmOCu0x3PF7Yark4xwt15VqYVJ8dEoYa3oe9IhpbjAETT5FnZqgl7jjQdVW4Lbb2slanPlgu7ZqpVhiDjl00q5DVzxjtVxGsiYSTWu_LRJhyY1LXxR2yliwWOtLvXFW8BrNNE9ua7Rp5KvtblAWeTPqA8VfhNqmppfuun7psve9Gow0ri94jqUsFZc0RaVoYUwen0kv6drd80SSgaL_Wsrh7xprOxJ5BZ4mf6KQ-V5x3dCI38zzcY2QI-ihiUSHdefaz-VcMzQwOdI_D2uuqeB_HrgliJWPR_hS5h82KoP_TM12TOCiZyQu_yL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb6c5b9fd.mp4?token=vm4eyU3am3OEZPgmyQqP0Zi-1snvB_EKOzTm3Q_rQCBuamRlsjUJ9ZgCaPP4ED9DByJ5iVzPbsPVSQwXhNNCxmjkAnhGf5GkG3aEJtErXGu8wBMJsf-W3tardcm6x5szfg5-GE6o1zYriz52sMbl5GsecRydQMf8iRqMf7CXv-hUBNN3I40tVXROiFgypNFjiGFS6WUOKQA8cMjcuPd32SCycxF4OAW70qn-LhcugNbAIVRYki1J86Cp_rsi6QPr7ZpG1bJGKRG3vgF2549F_EnUWgfLFOsS_UARzlBxZAEpsqOIgYpZH5tfJR0jdJudE-sj2rVSuNbl0GNdFhkkXzBlJ4R9Qbk49NUSuc_d-DwEHgaPXmOCu0x3PF7Yark4xwt15VqYVJ8dEoYa3oe9IhpbjAETT5FnZqgl7jjQdVW4Lbb2slanPlgu7ZqpVhiDjl00q5DVzxjtVxGsiYSTWu_LRJhyY1LXxR2yliwWOtLvXFW8BrNNE9ua7Rp5KvtblAWeTPqA8VfhNqmppfuun7psve9Gow0ri94jqUsFZc0RaVoYUwen0kv6drd80SSgaL_Wsrh7xprOxJ5BZ4mf6KQ-V5x3dCI38zzcY2QI-ihiUSHdefaz-VcMzQwOdI_D2uuqeB_HrgliJWPR_hS5h82KoP_TM12TOCiZyQu_yL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحول دیجیتال در عدلیه؛ کوچ از پرونده‌های کاغذی به عصر دادرسی الکترونیک
تبریزی، قاضی حوزه سایبر و فضای مجازی در
#گفتگو
با خبرفوری
:
🔹
با تصویب سند تحول و تعالی قوه قضاییه، شاهد چرخش بنیادین از پرونده‌های فیزیکی به سمت اسناد دیجیتال و جایگزینی رسیدگی‌های سنتی با فرآیندهای رسیدگی دیجیتال هستیم
🔹
در دنیای امروز، سکوهای دیجیتال سازندگان آینده هستند و رفتارهای اجتماعی ما نیز در حال کوچ از اقلیم سنتی به اقلیم دیجیتال است.
🔹
ارتقای سواد سایبری و سواد رسانه‌ای در مباحث حقوقی، نقشی قطعی و غیرقابل‌انکار در پیشگیری از جرم و کنترل رفتارهای مجرمانه ایفا خواهد کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/686967" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ترامپ متوهم در پاسخ به شبهات درباره کاهش ذخیره تسلیحاتی ارتش آمریکا
🔹
ما مقادیر تقریباً نامحدودی مهمات درجه متوسط تا بالا داریم. علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم.
🔹
فروش سلاح به متحدان به زودی دوباره آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/686966" target="_blank">📅 18:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZHu4gK8gA4UZBJS4jCXoJ7rxptnAnshuQXi00_YdewuZ5ND4BKXaTIIDHefBWXCZ8joLPg6L27S03Rh7Bzx1DOeNhbd-TOuyxHtg7n2bZdbgCbkEUIN45XWTQgSMPFx8kNJg5fdWT6a63xtDI4YUcLLuOv41CJPwVLoftsl8yjw1JZGkCbmY85p3aFGwVa3uhw9olzqxfJmQND35tt2M8QN71kwz41NT6UkcZbsHyrnnlqUU5NamcfB2c3S0CxIiU8YCikMpC9ipHwwJVRUgKMU4AZiRW5vYlmkQYLz7suflqiodQtyR57NB9ivOMS85jbyGVP2GoUuKIdqB3lLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ال‌دیاریو: ترامپ برای پنهان‌کردن «بی‌کفایتی» و «شکست» خود به ایران حمله می‌کند
🔹
روزنامه اسپانیایی ال‌دیاریو در تحلیلی درباره حمله آمریکا به جزیره لارک نوشت آنچه اکنون آشکار است، «استیصال ترامپ برای پنهان‌کردن بی‌کفایتی و مدیریت فاجعه‌بارش» در حل مسئله‌ای است که گزینه‌های او برای آن رو به پایان است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/686965" target="_blank">📅 18:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686964">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVOAQ1tSFGaVGe0Dh0d2fcLDTh-_V2ZcR5sct1Lzxq1hCZy90ip95zVNe1D6sZr4xZ36lWoRvu0Ho-BgYqSs9dQ66ZxTiBLc1X2uPvx9Z-vVBHSW96OgP7NQEWscReDxT1jDfPxNlrPuSu04JSZsOaxUwawyNLAxbOb-hwBXkgIz2ZlvI931K_C7koDtGVZMsnF4b9Shod3RcWEbrZy1xJh3ze387DXg1z-Q_PLpJzNHclq-qZGmXrYyG-_WlL2rK1pXnY9hsTulxqBXf6GphejbvHKlgOOY1mQwHlnT-dYGgQ8UzUuloHFx3OWnBzPQLEpDnNCD2Z8-LEbhNXCJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر ترامپ بابت انکار تلفات آمریکا در جنگ علیه ایران عذرخواهی کرد
🔹
هوارد لوتنیک، وزیر بازرگانی آمریکا، بابت انکار تلفات جنگ با ایران عذرخواهی کرد و کشته شدن ۱۸ نظامی آمریکایی را تأیید نمود؛ هرچند گزارش‌ها حاکی از آمار واقعی بسیار بالاتر است که دولت پنهان کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/686964" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a3ac210f.mp4?token=rxFDlzewUafNJRr3al-f2D_SzQOPybj7kntSni2d9fN_WdfBx_cKbCBxOOMQYCXRT2cwWZeMUepA0rMI_YnbZYKZA7RzjDipZv4djJTpR2oR9BdRZQZtwPBu2kWCnmIqU7zu21MuB1KQ9DhsjXOySEF4vFI_vdJpFpFH3GxgT8SnNaOPHh8X5tFEI9-GoWZl_uAER2ZAx6YB-oCclaU9eKAuMCyQulJpd87c0aQawdRRg345wJbBDVBF20UtvfH3DHAl6egjcccqRs_10D2Bjz4FEzbzIxqvPkL5YHSiSQ6g3-qiqXZCaRVrPXn3eUS0FHt-tyCohqVi7_ci8XWpe7ry0QHK9CYXSN9WvyG-k6_EsiBPrfLFQrj5GNtZb4wPA6UaRoYB1ubeOGBtjrlPnuMxtI834oyNt-AFp_OL1CeG5jXYL24ga7sJy_fqV4AjsnXoPlEg5qhilt0RKFQlXvNgpXQnESA2IEX8ISHeEQaU9EkKlbJMk_hvjO-XrBE-WX5pc8pHsJ9q7mSNHGI_0CDjHYoYHx057MD0l3NIrE8KnygpvoPPwR03qtcX109wB6sOOfEzzZVwIIEFQh3037832IM-PNBpsWtOhqDCY3pXKCpybMrvRbM3qqRr-mI4rTTkadSSOFDodlYpCCYMrBWD2iE714G0a-jF9oh1vMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a3ac210f.mp4?token=rxFDlzewUafNJRr3al-f2D_SzQOPybj7kntSni2d9fN_WdfBx_cKbCBxOOMQYCXRT2cwWZeMUepA0rMI_YnbZYKZA7RzjDipZv4djJTpR2oR9BdRZQZtwPBu2kWCnmIqU7zu21MuB1KQ9DhsjXOySEF4vFI_vdJpFpFH3GxgT8SnNaOPHh8X5tFEI9-GoWZl_uAER2ZAx6YB-oCclaU9eKAuMCyQulJpd87c0aQawdRRg345wJbBDVBF20UtvfH3DHAl6egjcccqRs_10D2Bjz4FEzbzIxqvPkL5YHSiSQ6g3-qiqXZCaRVrPXn3eUS0FHt-tyCohqVi7_ci8XWpe7ry0QHK9CYXSN9WvyG-k6_EsiBPrfLFQrj5GNtZb4wPA6UaRoYB1ubeOGBtjrlPnuMxtI834oyNt-AFp_OL1CeG5jXYL24ga7sJy_fqV4AjsnXoPlEg5qhilt0RKFQlXvNgpXQnESA2IEX8ISHeEQaU9EkKlbJMk_hvjO-XrBE-WX5pc8pHsJ9q7mSNHGI_0CDjHYoYHx057MD0l3NIrE8KnygpvoPPwR03qtcX109wB6sOOfEzzZVwIIEFQh3037832IM-PNBpsWtOhqDCY3pXKCpybMrvRbM3qqRr-mI4rTTkadSSOFDodlYpCCYMrBWD2iE714G0a-jF9oh1vMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیگنال خرید طلا که رایگان بهت دادم تو پیج
اما الان وضعیت چی میشه؟
قیمت ۲۲۰ هزار تومانی دلار از لحاظ اقتصادی بالاست و هر لحظه ممکنه بانک مرکزی اصلاح در بازار ایجاد کنه.
به دید پایان سال(بیش از ۶ ماه) این قیمت ها برای خرید مناسبه ولی اگر برای کوتاه مدت می خوای بخری باید ریسک کاهش ۱۵ تا ۲۰ درصدی طلا رو قبول کنی
@Titretejarat</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/686963" target="_blank">📅 18:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اکثر مجروحان حادثه سیریک از بیمارستان ترخیص شدند؛ ۱۱ مجروح حادثه سیریک همچنان تحت درمان هستند  رئیس بیمارستان میناب:
🔹
در پی اصابت به یک مراسم عروسی در سیریک، تیم مدیریتی و کادر درمان بیمارستان میناب بلافاصله به حالت آماده‌باش درآمدند و پذیرش مجروحان آغاز…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/686962" target="_blank">📅 18:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/686961" target="_blank">📅 18:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1ba24c8d.mp4?token=bbKMw3xjzO6YVZeV5TKhbqDM-hnVQ8W2Z5t8giObDo1Q3cvSfrpttG3Bcb9ave6RxfakrMI2Wk136uZvpCk2NtlyPmw8TO44gKoQutcAVq1snjpdoAZxM6j7ZAg4URxx0HyVam0Xe7HdCzFbwczFVPccsQ7oHFRELcLpPojsm6naxn87WR0FlVScTqgWTJmfutDb3MBQP7-TIz0jlFNDuMzzSAx-czScwhBpue92GBPtPv35tnn5i5Dx8mHy37_2j7_cvMZVVoMUSh7-caAmYyGyvDiGzIaHzBBZwICmDtU6OVMbtftBi6azIfOOHC0X5DOqWa-TEJ4-9RqKJXfhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1ba24c8d.mp4?token=bbKMw3xjzO6YVZeV5TKhbqDM-hnVQ8W2Z5t8giObDo1Q3cvSfrpttG3Bcb9ave6RxfakrMI2Wk136uZvpCk2NtlyPmw8TO44gKoQutcAVq1snjpdoAZxM6j7ZAg4URxx0HyVam0Xe7HdCzFbwczFVPccsQ7oHFRELcLpPojsm6naxn87WR0FlVScTqgWTJmfutDb3MBQP7-TIz0jlFNDuMzzSAx-czScwhBpue92GBPtPv35tnn5i5Dx8mHy37_2j7_cvMZVVoMUSh7-caAmYyGyvDiGzIaHzBBZwICmDtU6OVMbtftBi6azIfOOHC0X5DOqWa-TEJ4-9RqKJXfhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی ساده و کاربردی میوه‌ها رو به انگلیسی یاد بگیر و کم‌کم دایره‌لغاتت‌ ‌رو گسترش بده
#زبان_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/686960" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72021cd08e.mp4?token=soJynDO3Z-l56P2B9g20OQMY61kiLHKifsEgk3QjbPZPTiCJRrw5v09bmNP0WFG5JBfNmOcvVCciDaoTxsJxILRHcxOEzLpdHjkwg8xmNgU9LhYJWTkfaTj7BWAvhgCnUtxisKy2kFKcFCTVa3gmHc7DzwVgxRoHNUyBswSdvRFTrYCGqZXS4fQpXl-6RI1STnz_3b4d7xOPJ0P8BnjQFS33cKSZNoGFT6lZPhH2xpJzt1pGmLkjeKIvgfU1Oo5Fb6O42AhgbRjl4a1tTcoMk13pNlRVaqiKthIy2A4Y9ZvLK328jsAZQwB7pP-kC-WrYs8-DHlMTxRgVs0kUUYQCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72021cd08e.mp4?token=soJynDO3Z-l56P2B9g20OQMY61kiLHKifsEgk3QjbPZPTiCJRrw5v09bmNP0WFG5JBfNmOcvVCciDaoTxsJxILRHcxOEzLpdHjkwg8xmNgU9LhYJWTkfaTj7BWAvhgCnUtxisKy2kFKcFCTVa3gmHc7DzwVgxRoHNUyBswSdvRFTrYCGqZXS4fQpXl-6RI1STnz_3b4d7xOPJ0P8BnjQFS33cKSZNoGFT6lZPhH2xpJzt1pGmLkjeKIvgfU1Oo5Fb6O42AhgbRjl4a1tTcoMk13pNlRVaqiKthIy2A4Y9ZvLK328jsAZQwB7pP-kC-WrYs8-DHlMTxRgVs0kUUYQCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ثانیه از حال‌وهوای آخرین روز الکامپ ۲۹ در غرفه خبرفوری؛ دیدارها و رفت‌وآمدها همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686959" target="_blank">📅 17:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NObzJ2iijI7W6GjgiDIEpMjXuxdx0KxdtNc18-qdGw8NxPA_suYAiT5cS7F8wRXcKaX1nOrWTp1bVYB3TsewWUaqDBeraBBtAaLTupbmd1jeU7R0m0c_vpBZr-pXqO_CYQX82jdhETTnXVlzJRjsrI0SK5prgP0P2pG73PvelvTMg7Yoiu77MantFodjs7XTOc-1OUWUxlBnkbGR6IKcOb3JgLTaJpgqmc6om5SSPq56wWpx2S-fs-1VvmmSOIpcJg_CVLm65dc9YgflEmWZ8aNbrOH6vkAUnwOEK50a4aw3xuIZLbs8yTC_YYAxWKbodwskqbitws_cYOIGzeqyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۱۰۰ درصدی فروش کتاب «رویای نیمه‌شب» همزمان با پخش سریال
🔹
همزمان با پایان پخش سریال «رویای نیمه‌شب»، فروش رمان مظفر سالاری که این مجموعه تلویزیونی با اقتباسی آزاد از آن به کارگردانی حسن آخوندپور ساخته شده، افزایش قابل توجهی داشته است.
🔹
مسئولان انتشارات کتابستان، ناشر این رمان، اعلام کردند فروش «رویای نیمه‌شب» در دوره پخش سریال نسبت به ماه‌های پیش از آن صددرصد افزایش یافته است.
🔹
این افزایش فروش نشان می‌دهد پخش این سریال که محصول سازمان اوج است توانسته توجه بخشی از مخاطبان را به متن اصلی اثر جلب کند و آنها را به مطالعه رمان ترغیب کند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686958" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس مجمع تشخیص مصلحت نظام: جنایت جنگی سیریک نشان داد تمدن آمریکایی چیزی جز توحش بزک‌شده نیست‏.
🔹
وزیر خارجه عراق: تحریم‌های جدید آمریکا علیه ایران، ثبات اقتصادی عراق را متأثر می‌سازد.
🔹
فاز ۱۱ پارس جنوبی طی چند هفته آینده به حداکثر تولید یعنی یک میلیارد فوت مکعب در روز خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/686957" target="_blank">📅 17:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686956">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb2a35d23.mp4?token=t_Q9twuhA41xAXUudntbTBcuA52jSl9D4JJcQ-vaxIzfaoub0VjNTp_s6b9L6VUKdMmQXfC6NPLQYPPgxwXySI5xt9o9tOBoprcQjeCARzUfxV_zrEe81DezRCuy__TzWuzjJpYk_OLI7waIc_OIN7AWvi9gwz4AmvohyLYYZsdpswgO9uGx1dcPOsfTAThR2k5niuTgyFoiLNNrEr8N8Fo4Dyooni2jctPjfrOvUvLk8V6PhrETKC5A4Bk_noY_yil8INoT-E7n1BZ3Mpn02sftBa3aMfP73vGgRKUQnHxvaTojPbBMA193O2TZXEXH38RvW6wJfUlPmoWuQuSVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb2a35d23.mp4?token=t_Q9twuhA41xAXUudntbTBcuA52jSl9D4JJcQ-vaxIzfaoub0VjNTp_s6b9L6VUKdMmQXfC6NPLQYPPgxwXySI5xt9o9tOBoprcQjeCARzUfxV_zrEe81DezRCuy__TzWuzjJpYk_OLI7waIc_OIN7AWvi9gwz4AmvohyLYYZsdpswgO9uGx1dcPOsfTAThR2k5niuTgyFoiLNNrEr8N8Fo4Dyooni2jctPjfrOvUvLk8V6PhrETKC5A4Bk_noY_yil8INoT-E7n1BZ3Mpn02sftBa3aMfP73vGgRKUQnHxvaTojPbBMA193O2TZXEXH38RvW6wJfUlPmoWuQuSVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف پیکر مطهر ۲ شهید دفاع مقدس در چیلات ایلام
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686956" target="_blank">📅 17:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7e317256.mp4?token=o-LHQzL_5l9ZIeD4SS2M28RwYp2QEaqDFUKtjLplSooQcLWC7_vTiwEXZK3HKKkI5txfTentP9QB0AM_-v4pAT_CjbM56KHjBOPijNACx8D1NfZw1PQyUMfiAt1PJCmNfhWVkpKtUf-9P-2kOSbgwvnalYKLE93O2caRZp93hci_9_nmhc9sn9Fd-DWzPaFfaHsTfG_IF_CzalG0QEwd459JNL8KGz1MRBa7IF5Zi-PdiMsZUNlnYvmUFbLDQ4omiaARIsYsnUnZnUDUuZXHub8nP93JYJTMtYdDPx_Xb3ufwxlSt4ZMS6kKLsmc5aOpEtDmboWOSNkC2QcvbKOOtTdanTV4zIxlWosDNGJ3VibYO5ihYLtROMuTfgxnAfyIbXpmuufhmD-eEvFptABydg7mCyFiKPi_nMsD8yAZe928WooZoBwv5YYWuCzLPDqxX_TNO-Ae2oEXhRj_kamWwPmdE4K4BGa6J4-uGsEsYDVqe9sRa2tRo6LmQ1xQ7PzuKqlO548wOd0zz_c0WFZryjPh_D8X2Wq_lJQdiHK8qGwruj7wTlY8rNsDMq0djsZHlz8lpRf1x_SIXGNcSD788MqMy4_WDs0jwAvOTEJ9BWX91M2UlErf_XK2n2jsiKyvMNyGjUwUHRp_UeXfUTYJN0Qvo0PIQSJRZ746iIAxJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7e317256.mp4?token=o-LHQzL_5l9ZIeD4SS2M28RwYp2QEaqDFUKtjLplSooQcLWC7_vTiwEXZK3HKKkI5txfTentP9QB0AM_-v4pAT_CjbM56KHjBOPijNACx8D1NfZw1PQyUMfiAt1PJCmNfhWVkpKtUf-9P-2kOSbgwvnalYKLE93O2caRZp93hci_9_nmhc9sn9Fd-DWzPaFfaHsTfG_IF_CzalG0QEwd459JNL8KGz1MRBa7IF5Zi-PdiMsZUNlnYvmUFbLDQ4omiaARIsYsnUnZnUDUuZXHub8nP93JYJTMtYdDPx_Xb3ufwxlSt4ZMS6kKLsmc5aOpEtDmboWOSNkC2QcvbKOOtTdanTV4zIxlWosDNGJ3VibYO5ihYLtROMuTfgxnAfyIbXpmuufhmD-eEvFptABydg7mCyFiKPi_nMsD8yAZe928WooZoBwv5YYWuCzLPDqxX_TNO-Ae2oEXhRj_kamWwPmdE4K4BGa6J4-uGsEsYDVqe9sRa2tRo6LmQ1xQ7PzuKqlO548wOd0zz_c0WFZryjPh_D8X2Wq_lJQdiHK8qGwruj7wTlY8rNsDMq0djsZHlz8lpRf1x_SIXGNcSD788MqMy4_WDs0jwAvOTEJ9BWX91M2UlErf_XK2n2jsiKyvMNyGjUwUHRp_UeXfUTYJN0Qvo0PIQSJRZ746iIAxJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم‌های سنتی که به فکر منافع خود هستند از فضای فیلترینگ و فروش فیلترشکن سود می‌برند
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
قطعی اینترنت اشتباه است و با فیلترینگ مخالف هستم.
🔹
ما به خاطر پدیده نفوذ و جاسوسی نباید فضای فیلترینگ را بر کشور حاکم کنیم.
🔹
ما باید از تکنولوژی نهایت استفاده را بکنیم؛ نه اینکه بگوییم از تکنولوژی علیه ما استفاده می شود؛ پس این ۴۷ سال ما چه کار می‌کردیم؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/686955" target="_blank">📅 17:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ترامپ در گفت‌و‌گو با مشاوران ارشد خود، موضوع اعلام رسمی پایان درگیری با ایران را مطرح کرده
🔹
این نشان دهنده تلاش دولت آمریکا برای دستیابی به اهداف خود از طریق تشدید فشار اقتصادی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686954" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حضور پرقدرت نخستین بانک خصوصی ایران در الکامپ ۲۹!
🔹
بیست‌ونهمین نمایشگاه الکامپ امسال شاهد حضور متفاوت و همه‌جانبه گروه «بانک اقتصاد نوین» بود. غرفه‌ای که با مسابقه هیجان‌انگیز لیگ وینگری‌ها حسابی انرژی نمایشگاه رو بالا برد و با گردهم‌آوردن تمام زیرمجموعه‌های قدرتمند خود شامل لیزینگ، تامین سرمایه، بیمه، نوین‌معتمد و نوین‌تک نشان داد که یک اکوسیستم کامل برای پاسخ به نیازهای مالی، سرمایه‌گذاری و مالیاتی کسب‌وکارها ساخته است.
🔹
شعار گروه اقتصادنوین این است که کارهای مالی و بانکی نباید یکی از دغدغه های مردم باشد و باید مثل یک مشاور برای مشتریان خود در حوزه مالی، سبک زندگی نوین بسازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/686953" target="_blank">📅 17:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfbz7SNNbm9GAP8Dt7eqhaf5gVgKLlGOnvTxargggv2MTT3ANRGc62ryZDFqGn2Ow6GCjv0XjQs8IdctklURYyiA1Z5n6QT8nNPbJ-xD5b9YH5IGfvv5DGuoWoSCFDO8glNawreZbBp-TAQq_JeKDkIw-0EQxedH8zY9wLXRuVnnBj5pUlcn8hY19MpOB3K92nezR6ylEkfmz8J5of-bLg0VAK2kcy8OW4-h1ilkzjE6nufIZIavV8Jkrg1VSqVCrHefMCA3hysdyOyByq3MqOHxuVbWYne-qTGbCRrqWdCcvv8sW6jREoVz5J_ckpeYcYVMPmGTGuasnLxv7MYbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/686952" target="_blank">📅 17:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b374894ff6.mp4?token=f5-xuCOr0FYIxVdU9dHfo5W49tHKollfyAUXv5w4CTSf3lJIFZk4QU-5kSgiIlXLgXyFmfcQHv3YnuIaHngEf4f_OSTyKDwZHkeJXdLprnf-WOCLUgf22dMJ5YsqiqvwmbxBItK6QAK5p25k8I9eYkl3MZJzlC-lW8Jf53qexBA_rbgcX4lPmPPLQ8MkaktfF9nf7a4MB0E1xZ65La-SamkaamSYwy7dDbBSJLWFeOpu3rOiQZVWYQaICmS0H6dnAS-wX-okcvmdEdwBIer69NYtBv8nsr1biJDNgpb9aLzFSc1Kd8Qeku1Scp2ADZ6eO_u-6V-mcqgdqa7CD8qMWLa4pGhGaOHxDs1ThJXZ0IHcDUnCeNNV4Xov_kic7lvMXsfpLN1niMKEH_0Qfqr_ndozegvloG-yxEnT83acoi3SdSWZ9SPqOjGwNQXdqjOMSuaA_NJPqbdRF9v5tgHuUk3m7aMO4qsGeo-ua7Tpvv4ppJkSZVtpS265bAcwh_SipymD18VGmJEa_LB2ZoYxQ4HefV2_9dgbTTUcn0GiVbwsE-z-nTPKYI-Fj-y_trRJ3qdjBykHx17vCh8CSa5iLH1pdWsynsanqOgNUGsj6ZBqq4DXHvhecz4NN7HhuHT0fkq8vJg87UV8Lbr-tGnd7fzUtahF1bHbhpUsAJgKapE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b374894ff6.mp4?token=f5-xuCOr0FYIxVdU9dHfo5W49tHKollfyAUXv5w4CTSf3lJIFZk4QU-5kSgiIlXLgXyFmfcQHv3YnuIaHngEf4f_OSTyKDwZHkeJXdLprnf-WOCLUgf22dMJ5YsqiqvwmbxBItK6QAK5p25k8I9eYkl3MZJzlC-lW8Jf53qexBA_rbgcX4lPmPPLQ8MkaktfF9nf7a4MB0E1xZ65La-SamkaamSYwy7dDbBSJLWFeOpu3rOiQZVWYQaICmS0H6dnAS-wX-okcvmdEdwBIer69NYtBv8nsr1biJDNgpb9aLzFSc1Kd8Qeku1Scp2ADZ6eO_u-6V-mcqgdqa7CD8qMWLa4pGhGaOHxDs1ThJXZ0IHcDUnCeNNV4Xov_kic7lvMXsfpLN1niMKEH_0Qfqr_ndozegvloG-yxEnT83acoi3SdSWZ9SPqOjGwNQXdqjOMSuaA_NJPqbdRF9v5tgHuUk3m7aMO4qsGeo-ua7Tpvv4ppJkSZVtpS265bAcwh_SipymD18VGmJEa_LB2ZoYxQ4HefV2_9dgbTTUcn0GiVbwsE-z-nTPKYI-Fj-y_trRJ3qdjBykHx17vCh8CSa5iLH1pdWsynsanqOgNUGsj6ZBqq4DXHvhecz4NN7HhuHT0fkq8vJg87UV8Lbr-tGnd7fzUtahF1bHbhpUsAJgKapE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به پایان آمد این دفتر...
🔹
لحظات آخر نمایشگاه بین المللی الکامپ ، بین شما شهروندان عزیز و غرفه داران آمدیم تا گوش شنوایی باشیم برای شنیدن نظرات....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686951" target="_blank">📅 17:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686943">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnSrEHc8DjFVt2TK0SDek9OwJ25ReOfbLi-s3toMzPKMcgWv_TO2WVz4PyrUqfCempZexwZ4G5-w-KR0jEsjWxrU_dRp39c01DKTCEucernIqmNnBeeDfl8ldaLYujofIZPklRzk96IMGqhaFmOVINt4qKza7cDxNwKQaR3l8Smb4An7zyjsx3_6VXecxQo2mDUbY-bx4CdCLS87DeFYnyPJ7TieGWKXu8XLJkQXocxAO9WHtZRpXDZkk4adHczYp8n0LFeasC_cq7-3k5JBa9Owa3E4NMfD0iYHGd8RkWlWM8Bel3D2kn1antEmKzNoE72AseY52-yqzlpLLF59EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DudE_3lKK1E_NSWuMV9cKfVrla51XgjkQzgeARB0BGPKGIPfLCr3eEahOMXtVQqDmhDeq_0U3Tu_veVYUYoJ7p2L7_7rhzivqmHL-3QPpqT7NNuAGSZFW8R7utTcLHkxLBd_xNrvMtbbEk-p_GvU-2ADhba1Sm17PeVRu4vr1DzI_GZijwMAlnczw2x818dkHhJ2hYQIBncCvLts7V-CiPuYtJLbzGFE7OGOFaFtIcfCa41-2HCiPmIpSyLvdIpbVvOMbUaBXU3KrK28DzJ3p7kpL5b-UNy1lRIIkZfyMP0kBTIGaOKZmv8qkK4yWrBPK_Z_npOct9Mt5-FSezo1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmmwHzDg5xyP2pNzFcbKwCrrvCt7dCXJ3lVOZ5UG6lswthPX8cXVm_F98ywa9VIf8QZfR-b33-CwqDNyop9J_okazWRZM2e--3uhn4hvQcbxjprf27vkj1GscP0SFLXa5HV9SE3726_frRRbM4UK0zEH8hRNO5iTgCyou2iDpDQLFGV4Fu-KXsfWgQuY-_Q1HuYO6JcjwaU5iC9c8bHB2wkoO0rhjRJl4go5nohzbZJWyMSxxWiDRifJkKM_R_4_h-ejKNWy7ms0SmGpsjoaWoLcLeDqln3UIDDjzmBI-LmgC1TTAODYxpFIDtkNBFqIJm_vNnDeOIpTrLNjSO43jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMaL_lFlAsvRjhMufzOiDM3zpmbJLVNIuooaHBSuJ2Em2MWFedydiqimKgqxd6vBO4b9YIsruA7CSov92P6pZxO9qzN0MqlgaJpqL6QZ9mDleajngRZOUA_BD7ZiV1ngwCe-ez3FZ17tEIJy9ZhCDcwlfvo7wPwYDE8lKVVesWXm50A_ViXYUkjckOiucntayjhiBsfSN91k1GDgUcCfkQAP8jcm5k4o9a0q3zlWDK6KVjKw8mlp_uCidF1hFbwYKEUbOnQar76Mk-SftXohgW_ZRehibRc6_GlPqIbRvuAiLgkYlWiCvzjWqriyT5sSwPrtVsA_WamSRNXAzB5Pkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1k4xbVhmiQpCE0udzc0G8TGK9uwIj7-iC26OjreOI4onVy7xzJPJD38_0GrsaX4YIokd6e2TpSY6SIRIoGSaYznf2O8822JCGtpUkhXYj3jKiUbCdYcD822I16V_2CZofbdQu0m-adG_MoN9cIJoy4CjMWLibrdbQANkN2_zJdLWeDcB-ZvXWTuRo1RdE_q7V8js7vCajgtxn1dSq28k_19D5FAIL3I4wvPxzv6nkUMIfgpWGUaSMx8T_9wFuYylh8lrYixU8H9Ym4hbirxn5gOgro4asnHyuv3-6PuyiNeNTvBnoqpj3bFkLvW_YSHR-hV7flbYNDaKUsm1sqaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnhCbOzXLDtKf9aC5eV8VSW0Bp_Dt58zlje_6hy4jJuFPR6AsJ1tMDc6k0maowNqU_7JugQrjEtIcCuHH01IOk2NGxquJfHIBmxXV8V9rEBkNpCYsd8afi1JGqI8hpBoYSkMktsNpGVJc8w5Ny9-zOz8IcFK5V1J-Uk0LysY_a8_cVXIPMnIHhTRVKugvE5o3YTNKJV6XOd8_A7v7odUfQRicDLOefpWDDHeZO1wA3JExb-3hrHn60Ycw5mHJJ1FErlA3Tp5l9qYNKRaX9ACNEZmTIBBSH9rmhxeeTs6UtUn5feSG0r101szEhmjde54pZEif1eQQ3NJDSPQVyLvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLQjc9NwMLogwQSG3MpE26G-Q2CGW2cZtfvLNdTwFke2q-YMVlIBq1MpGj0tsKMFcevpNgQkKTn9Ol3PFseVXLoXOAvHjbtrxkR5glsef-2ZNt2K3cgV3C9JwUtuwsteDG-BamU8EusxdJ0mn8pf7pO7XMiBwoIAiyhQ2wKBDNgGTQPtWQDEmzqvL8DEdTpYJSNOAynfd6KqhS508B0QZyWtIT4M2jQaU6N5DgZBwBOmLr2BdJr9-r_YOH-jzbGd-8pysdfdTI5_11cMZ0SzFfDrJ9kDF5CFcy9rklM6M4sUYZBxyXBWRvroL4ZqWNHj3mVkdirUookOl8M6TYkU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieaEUj7p7Obbj2Hh4DfSN2UPkEbs2ZiiG4gRbjOGk76kchYYDqx1FQ1Y2prOSQdJdJIewcFzimtjM1BXCgc_txpzlYNVHkaxAwwP6lBYXrgkgtGbGq74NOdZ2F8NqL0BSNYxci6XWLlb-P_ozHR6SOYxX58RBsCf1tz16rStiZZ_x1ldmdylPN8Cg3Ssx3iUJuEJz2hTqALVfLprwnkQLml7MBzuHbt3SVjj4Y6VNYxrl_DcRib-3M7D35IYrqhpVBZCPzumIJuB_-g0hCGbW_i4KZpdNiOAT_kuym9jMONemiAkk98CYIoRMATIKQssiK7-ENQjh5lqBnJ1V9IJog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ حضور
💫
✨
برکتِ هر نذر، به حضور دل‌هایی‌ست که بی‌منت کنار هم می‌ایستند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم برخوردار این همراهی را معنا می‌بخشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/686943" target="_blank">📅 17:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686942">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
شهید ۶ ساله عروسی سیریک
🔹
امیرمحمد کریمی، کودک ۶ ساله که توسط ارتش تروریستی آمریکا به شهادت رسید.
🔹
خواهر او نیز در این حمله تروریستی به شدت مجروح شده‌است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/686942" target="_blank">📅 17:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686941">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8732916c9.mp4?token=lZ-xT1OsOBRg49-uw8NuMhPtcAmM_-RFyh2msEXThx538EZ7dEZph30Lj4Wi43aooRrhBg-jbB-RdMh7qszBLqez0eYrrQ6jBNcUbByb1UPFenZHymOBQqRrubbJ6Wqcu1SfoXgYgCN-xNZFKV0AUXa5AkKOvrrSHKHA43NH-ryPo3p_UjbHlGTRuJkPzXWT8V6Js1PezWxUKXKm8oCaGT9aguzUEx6jZ1x8fA5tQ0zLCxYNgPgr4o3LdKHCtsQ_YCbZ2fxfYd9FDfnJ5dYIUxtiLVXOt45mY_D8iSuQW1GblWjF9YIwv9jyLKgU_lOGy98OHwowPSMxUerO4tdK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8732916c9.mp4?token=lZ-xT1OsOBRg49-uw8NuMhPtcAmM_-RFyh2msEXThx538EZ7dEZph30Lj4Wi43aooRrhBg-jbB-RdMh7qszBLqez0eYrrQ6jBNcUbByb1UPFenZHymOBQqRrubbJ6Wqcu1SfoXgYgCN-xNZFKV0AUXa5AkKOvrrSHKHA43NH-ryPo3p_UjbHlGTRuJkPzXWT8V6Js1PezWxUKXKm8oCaGT9aguzUEx6jZ1x8fA5tQ0zLCxYNgPgr4o3LdKHCtsQ_YCbZ2fxfYd9FDfnJ5dYIUxtiLVXOt45mY_D8iSuQW1GblWjF9YIwv9jyLKgU_lOGy98OHwowPSMxUerO4tdK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی زودهنگام؟ بابک زنجانی: دات‌وان را به بورس می‌آورم و می‌روم پی زندگی‌ام!
🔹
بابک زنجانی در حاشیه نمایشگاه الکامپ با اشاره به آینده مجموعه «دات‌وان» و برنامه خروج خود به خبرنگاران گفت:
🔹
«معتقدم باید دات‌وان را به‌سرعت در یکی دو سال آینده، با زیرساخت‌های جدی‌اش و سهام‌هایش شفاف‌سازی کنیم و سامان بدهیم تا وارد بورس شود؛ من هم بعد از آن بیرون بیایم و بروم دنبال زندگی خودم!»
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/686941" target="_blank">📅 17:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686940">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
بقائی خطاب به بسنت: تاریخ فراتر از خاطرات حیاط پشتی خانه شماست
🔹
سخنگوی وزارت امور خارجه امروز با بیان اینکه وزیر خزانه‌داری آمریکا عمق تاریخ و تمدن و غنای فرهنگ ایران را با مساحت حیاط پشتی دوران کودکی‌اش اشتباه گرفته، خطاب به وی گفت: جنگ انتخابی و غیرقانونی شما هم قرار بود با توسل به قساوت حداکثری، ملت ایران را به فروپاشی بکشاند، اما آنچه بیش از همه فروپاشیده، توهم قدرت مطلق شماست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686940" target="_blank">📅 17:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686935">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntSrrBMkvQHzP923wSWMnSmD6JXem8v-YtoK_N1c3yyfC6HShp-kd2kih5qyRq4KJqW5A2j8Y2LXDLJj62ZTms2HQCVYGhmZ0VnT5GLEVY3zZvkgY3wEK3eSqx7ThBrAMCwe4-mEHfnPsm6R9kEnFQzmVzrTDxh-ErmL7xaH_AUGAcdP1i1VKLRIcnFUo92k7uzHGcltuMNZtd5U5uJ-4SPRtOy05979qmqie1LPd-gpca_gDV-B2T3KazSYnF7DlsCf7NnXDeMNrEEEU1CZTYv6vuzVHzz9KhXEroF1FQGLqbyVwqarjeeopf-fhxJ-x8oJYqUEKQ3L6n2kFv1EjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgKIETxbsGQOsGSEbYBfDJIYloAWrILqptOfWljQBz6fbcBwaH3t8LSy9a-jLofCwS09W437gFApOGkbzdbnoAGDmQPkrSVk6qF7DrgiF6oZLCQoo27_MagJOo127QHfv0LHiQzuApLBRmGOhU0L53ICYdCIWf6IUCdazS5hVBQeWo4qYCRxwO-VgF9KfJLEUQjOpNeRt4VWSyV922UZd1lzKaUvUYiUlMA9ag2k_H1cY9HMEKfv_na3XVSugZIB7iia8RZ_-pkZuTZmADh837lemgQKVBY1232Pv-nVHvaZ7a9ZHgtl8DJVMjW0xbQaYRtiJSJJU1U4pUjmDQvP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5d270b7d.mp4?token=tYkXERFLyrhVKx2TC5oYujn9Lzj6rBoqxH-NjM9Rm2ICYoVBIl_TdEWE1lOlYmylkp-sf5h6qParYIoSge62-f8585JyNi4AyTEf9UrC4hwslRps2UWDgKeMv8luuiE1e039ykX4n-GNs1QgkbwwIhvx37lAE5-TbxkiMl1LcWtGkOMUHOWH2wJ4RYkHNNXSQlrBigqVSXp9iZF5pA1dQOF7QibNxJS8snwSsn1EyC--0Wz9pambpEc_qVhhh6epOtFLJGc7gpAPe-w8cNMiudhaXGh1x-rXchrODQHuArW19JjryJw2F8TtV6IS2dvCip4dHDSC7N3jXOGolMbhzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5d270b7d.mp4?token=tYkXERFLyrhVKx2TC5oYujn9Lzj6rBoqxH-NjM9Rm2ICYoVBIl_TdEWE1lOlYmylkp-sf5h6qParYIoSge62-f8585JyNi4AyTEf9UrC4hwslRps2UWDgKeMv8luuiE1e039ykX4n-GNs1QgkbwwIhvx37lAE5-TbxkiMl1LcWtGkOMUHOWH2wJ4RYkHNNXSQlrBigqVSXp9iZF5pA1dQOF7QibNxJS8snwSsn1EyC--0Wz9pambpEc_qVhhh6epOtFLJGc7gpAPe-w8cNMiudhaXGh1x-rXchrODQHuArW19JjryJw2F8TtV6IS2dvCip4dHDSC7N3jXOGolMbhzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه جالب بین نسخه قدیم هری‌پاتر و نسخه جدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686935" target="_blank">📅 16:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sC2VNvMFgAjSr33pGfcH--yNo_beEhuShAECU_W6raOmq3xNOC8prnQqMX_C6uRRxAHJu1N_EP2yeE1ksMDKIW4MJhiUmOu--y4eYCesM0Tf-OYn-FV1WGbKRdGWXI1l4phis2rZvk_cS5GV0FkxdnPPJM1nCs4PDdqYeB6CSY4cayqxk8056bZdCdYM_qybSwb1u8lFU8JsrorPLGEqYPmR1EMo18l2Xj8PCMJ8EuHbtyE7X_tIKFhnaU0sTlvLGhPXjcTbDJ4cQuEo4JSCE6KOWwAqc1cx8MOXQU35PuH-6ooQOzBKw6pmvpf9m9rNeULd_U3O3374C9U2zE0tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9e75p35kP5HyXOdewUnN6374K42zaBKQHgrJodA7MomLSAknRxk9NLaA9Ir89WN9r4C0CEd9eIAGVCd6M6EcEl7xzelUSKxFcCib-xO7XPEPsTRuHDmeFCOYAHZcgqoWhA815WED5H-84zD3k7UzRG0qLFaoH49Fy1q0QJ8lKgsocXttLYJRxx27RDvrWZJJxdFPKihbkcROaxO2lY342Tn1OKSPHLY3uxOji-DmnhkYORE-moDcGkwcCkncXoNF-lKFc-6_uT2Ydwg-meKYFjPhkstR_EwRH1vkgEpnwDpU4RIKkua-20VNQYFHuFwM9dOB65--higFovyrkeNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cT2P9lBl5stmKZO2aLZQtx5r7syUYd_L31RZGF3xZfxuRJ_aKOs9v8a9VFZVhEzxBqts-xOD8IjtdeB5SAc9F00IqM-Z_qigaabPJ7-8NPIrAIp7-DPBOAIVmyDiUMb2K5n5FPae33WIaXUEp27q_01ZBPi4auM8ipRY_mX_TG5cVJYviq8nzt7YZCJxN7qkYRRe-JBagnFi_JFoE9co43ZkKizFXChYzhUyDNjzMbi4zBcFJqqxfr7MxXEIZfArDAvEJOykbEq_xOVpWYGID4SJD4QYEXAg66-xWAZBQmdstIJ593XUOaZiOVN09k2JJtUOhdtT9ldODwf1jt4Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhurvTj7A4kA8B6Bgl5rQTTVkaNzp7dzpK_Dr9yiIEgO1yfEYS6Wk3tT_fS-n5bZCpdbww6l74StKXOoqGJdlvfLPbyEoZ6c74splvDpz4AKk5itb7h0yrz4C6uN63uMqZEL1q-xd27T7EY-z2qmHf3iTCmNApZRxIOiWJUDvCrVR6XVc2Oo_0-5S_XnvyBMMcVzFjb4wUVc4cBDRHT6qiaZHxd1E0BcXV5wjLa6VSxRQ4G-0yOiqFenS7DHBwoR4huetq6ekR9GVj4d6hVmur_Jkuq_huli9P4x_Icw9GMV-Jj95f7LmoTR5SPDja3dtiJkER6PfhtjxOGb35-ecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esMil9h1XymE11jJaU9-_MYPyscyokzheAzam812GmBiGMZVhLBjv9gnYlC-bdT_AfU7RIbh5m6YH8gtAIPnKCf1tvInHroFNvS9EKrqx8t7H65DP3NeZubTkCNUFX1p0BI-YaFXV1gAOo9fnpWOsKz03LxBMRPoruOJMk5hsWnS_uyPVfzc5wVU6u-L9_fZHGBwalKbcBKQEnjZB74JM6zTJHCMq5sjeGg3XgdzRS-Uk05qwo9BikPkHXtqUCltqEY6HWL4LTeZogrTB8Uj2bn4oK6SikT_8uVHXNw4FLaQbgqKD30dyq0QIhY5qqj98_Id8ogBeimUrHkiWVAGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmUVLVIZfCws4UwLGlgCftV8kqp5UJIItgOj29pxj-MNH_Cspnx8r0UOf5I6t_jakXPadV45FpEsLz6Fp_qSsUuPPcA8YaC0zb5L2EPd1XhsmOwUvrBG_qeWPzVgYkFBoKkRvIJQ0NGdRa8EhaZClaBS68qPBEh9Cks7UYbFBxAgI6Rx0iPrgWYhmJd28ZFVfjxqfyeY5fHfYqDniQiP74KHcz8LZbfWM_l-7sQN1e6tFfe5exPeDEhQ1EYMP5z4WI43K3kROi9kcWubZyWEF43X8pJZzK4l2VPby5i4agrU7M-eL87ZqTNYBEZANtnGK7YeELM0F99FuxOCRDHu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkXn51-rrORA7Z5XNc_0PE7RBQb-yXCnb-tSFjZEyHTmw84E0InKVCHawiSnThghcsnEwPuuyVMBAuT9YXUsJMkAlAmN2IrsjSQHE3KXdxQ2Gf9Afi_LrsCvmO2B1v2PSNo2cHRViQ6hb9TOksMk16sbl3QYoZI-LhorTjU8OwIA3NL8cWZ-FQrLc_4I_Fg_ursUkxGy793GaRurQs1EYkxvJk1M71FMNK3S7zycnQiXHl6S2I0C5pb7DcPG2ojWuo8fV2k7RZ39cJGjQCBPH_Uy1choPFAakb3BxkPeM204DwsRN5w3nkEqLD4bJN7rRhs1z9jSPnRh4kfH4UCyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVpHc3DqXsXUP-mmKyqsEcfLEaTZyMMGh0tDNYoYkPf8qo-CehMtLZ-_pLl4XFU9CW7iclMzStvhIxVnq1V8fFAwSrTZWmEWkUNe5hIgu5PKQbpJODP99D1iwSAYgAqIHXnidbZk-9zLwMIRg8ZGI12juVDosRg0eJuiuWHP0lN2cRqjrBNlKhQnVqrh4fiiFuBs55iAYeGeOVtc9kAvGPbZvC7E7-lwRou3MnLo88MeJojUD1HCePwdbk_1t11OjXw_pn3RnE6SJIA7v19Bgi_2rv-rpbxvMf60jJeG7zg49cvwd1XBzqkbmIh2aLVYwsGk6ELAjOK8-ZtcrMM0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsVf_rwfRkxJ_IJFFxx_PFAv5NVge1G7Geo0YqK0moOiSbV62zHCA1ceE3pAcnxrbsdNqcj9r7lYfCFSRBWJ3mi1OKxsnpOB5IVYGNP84mSMYEmI37Nzxl0z8dSUWUG_j9xxrwf2XXzHZKTlR7Bzdsg8yEq0EtwoIGbH8r-gQFG4hocA9-FJ2OQ-bC1FvtcRXbUbGqetu6dyfsMiyQITfXP3erem4dZlm3ai2bgGYcXDdLd6m4K0jj7UF0EA4QkEsi6shgjNPYPL4h993wV3wr9R6ac2Vw1VnmnRh3U2zI3G5rJb9eNQmsHbbEPQBrmPds-3UgwakJL2ks1VQnIU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ill4w84L_kKkcgw5jcZxKAH21Vndca3qSJ6pHTlcfejyl8bH0zIS095zs_0om-21uIp531I-XAhoiMNvCEqxnNgJuG56rli3vt32uggH7Ve9zfBc-XwOwgPY5jtP7DR2mZxeEuWRc3m8E9utCYIyjOgLihMjCnvO72gX4ppBy6dW0dpsUn3Cj67_A8RlKvheyCN0mLau4FBOtXyvegPRxkgVVPmwhaJ24aQgO4wY6fLrYSS735Zmc-ABJoOLwKsIKEEWifozEu8xLjb8mE69vlE3pMzVZW2nymF5NpsfZA6xlmv17lw4pbMObZqgNHT4Srf_WJbgfKaRz5DCDIQNog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آخرین روز الکامپ ۲۹؛ همچنان در کنار شما
🔹
آخرین روز بیست‌ونهمین نمایشگاه الکامپ هم با حضور بازدیدکنندگان و مهمانان در غرفه خبرفوری ادامه دارد؛ چند قاب از حال‌وهوای امروز و دیدارهایی که تا اینجا رقم خورده است.
📍
نمایشگاه بین‌المللی تهران | سالن ۶ | غرفه ۳۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/686925" target="_blank">📅 16:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsInyxCtj3oP86zv8jfNxTUoPaYPv1oCEKXFKeOilMLEr-Wl54v1u19bM7aMGVS2k1bx5HG-sE3ImwzW34B327XNkjAI9MKIrlOiEm6B8MA22aKwAR0wxQOADWKu13izaz9lCEJvV47wsU7UTfcQMgqYjte9EEDxnqiAmWCL-zS8oJsaEHTOAJ4fZdEaOUJJSCXvoMz-1C18G4JRnkB7JH6kiGtnFnfmrBY5CKHBdqG-LKB7JuvIhHKh75iITqynwYYGysB5BIYNLbE0zbTCgAbdaGsccS0zdKz4SXbsXrkEMSyNO5HvLuJW6jxZ76DOArvvlqhF37RWNHkcdxdP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستگیری تیم ۷ نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی
روابط عمومی سپاه امیر المومنین (ع) استان ایلام:
🔹
طی اقدامات سازمان اطلاعات سپاه استان ایلام یک تیم هفت نفره از عناصر وابسته به گروهک‌های تجزیه‌طلب کردی شناسایی دستگیر شدند.
🔹
این عناصر با تامین مالی و هدایت سرپل خارج از کشور، اقدام به تهیه سلاح نموده و به دنبال اقدامات مسلحانه در شهرهای غربی کشور بودند.
🔹
در بازرسی صورت گرفته، مقادیری سلاح گرم شامل کلاشینکف، انواع سلاح کمری و شاتگان به همراه مهمات مربوطه از مخفیگاه آنها کشف گردید.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/686924" target="_blank">📅 16:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از منابع: دستیاران ترامپ به دنبال «آرام نگه داشتن» جنگ ایران هستند، اما می‌گویند حملات ممکن است پس از انتخابات نوامبر تشدید شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/686923" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در حوزه تکنولوژی خودتحریمی داریم/ برخی مانع از اجرای مصوبه هوش مصنوعی هستند
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
مجمع تشخیص مصلحت نظام، مصوبه هوش مصنوعی مجلس را تایید کرد، اما اینکه چه کسانی مانع اجرای آن هستند، مهم است.
در این راستا از شورای عالی فضای مجازی یا شورای عالی امنیت ملی انتظار بیشتری می رود؛ از دستگاه‌های ناظر انتظار بیشتری می رود.
🔹
تصمیم گیری کشور نباید به دست کسانی باشد که دارای چارچوب فکری مکتوم از قبل هستند.
🔹
ما تحریم هستیم و خیلی از کشورها مانع از ورود تکنولوژی به کشور ما هستند اما نباید خود ما نیز خودتحریمی به وجود آوریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686922" target="_blank">📅 16:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نیروهای مسلح یمن تصاویر شکار مزدوران سعودی را منتشر کرد
🔹
نیروهای مسلح یمن با انتشار ویدئویی جدید، صحنه‌هایی از هدف قرار دادن تجمع نظامیان و تجهیزات مزدوران عربستان را به نمایش گذاشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686921" target="_blank">📅 16:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پاسخ کرملین به آمریکا: روابط با ایران را حفظ می‌کنیم
🔹
سخنگوی کرملین در واکنش به درخواست وزیر خزانه‌داری آمریکا برای دوری از ایران تأکید کرد مسکو روابط دوستانه و شراکتی خود را حفظ می‌کند و توسعه خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/686920" target="_blank">📅 16:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug0rI8QJvDzf4OwIYHvpgxXS0SeNkBUHkJrHIj-lbqaud64DhLCFTF5Zy--BZYK-oHHMLZtMJGcMvoJW1IvkRc2GOdRqE5STB8GOrToRIegqvnQwmTRWwGnz4Sm346F4h_zILdms-QutDKGzwRtc_pnVlL1bAxm1CS9srkqkyvdy9RmBqRj5-yDMjO5mg-JbFC807BAIs6gUWjIL-7b-s4Ohy8lSUpLyHidJJ253wLS_--Q6oBiS5r2hiYPHp86dRi1Z1j6BBzG-715Bo_Z9t0J7exvhRDu_tcv2klaNgYCgV8xtq6Tk7f83cEY5QkO5ek1boKWqXTRY74cyjroPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بشکه نفت برنت به ۹۶ دلار
کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/686919" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
قیمت پیشنهادی تخم‌مرغ درب مرغداری ۲۷۱ تومان اعلام شد
رئیس هیئت‌مدیره اتحادیه مرکزی مرغداران:
🔹
قیمت پیشنهادی ما برای شهریورماه ۲۷۱ هزار تومان به ازای هر کیلوگرم تخم‌مرغ بوده است.
🔹
تخم‌مرغ با وجود افزایش قیمت، همچنان ارزان‌ترین کالای پروتئینی کشور محسوب می‌شود.
🔹
صادرات تخم‌مرغ از دست بخش خصوصی خارج شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686918" target="_blank">📅 16:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آزادی ۵ اسیر لبنانی در ازای تحویل اجساد صهیونیست‌ها
دفتر نخست‌وزیری رژیم صهیونیستی:
🔹
۵ شهروند اسیر لبنانی در ازای بازگشت اجساد صهیونیست‌ها از لبنان آزاد شدند.
🔹
این تبادل در حالی انجام شده که حملات و تجاوزات رژیم صهیونیستی به خاک لبنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686917" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd8408c33.mp4?token=KK_b-HdlUm3LUPsX6evCUO9oO8gf1aLA6ZOYD01KPwXVUmw4SvAyvZN3bWz3tj06CheD1h6fCWVv2RPEM4hF4HqOHMhwV1tktPJr9qm8uNNk5L-5jB_8is8kmp7cartTRGpmB_a2rXMNkHSkhzM4WCmf-A3bRzU7HM7AxGDgTGZpXjqCsFrK4ku-aABMTStRl7vmrdFtzCph7y7_OE20x_ot0r8HwuDPRpSR6WiG3X15fU5iFoLQpM1kpHSw8N-mVBzrfjL1a3Y4wq3zzR_d1n6XWTD7KN3YWZF_WHxy-DdBvZATo5XZhYQYAG-_lc6oGA4LGZgszdm2UWIPAHkNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd8408c33.mp4?token=KK_b-HdlUm3LUPsX6evCUO9oO8gf1aLA6ZOYD01KPwXVUmw4SvAyvZN3bWz3tj06CheD1h6fCWVv2RPEM4hF4HqOHMhwV1tktPJr9qm8uNNk5L-5jB_8is8kmp7cartTRGpmB_a2rXMNkHSkhzM4WCmf-A3bRzU7HM7AxGDgTGZpXjqCsFrK4ku-aABMTStRl7vmrdFtzCph7y7_OE20x_ot0r8HwuDPRpSR6WiG3X15fU5iFoLQpM1kpHSw8N-mVBzrfjL1a3Y4wq3zzR_d1n6XWTD7KN3YWZF_WHxy-DdBvZATo5XZhYQYAG-_lc6oGA4LGZgszdm2UWIPAHkNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم نترسند، ویروس جدید خطرناک نیست!
مینو محرز، متخصص بیماری‌های عفونی:
🔹
ویروسی که اخیراً در کشور شایع شده، همان کرونا با درجات خفیف‌تر بوده اما مردم نگران نباشند چراکه قابل درمان است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686916" target="_blank">📅 16:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
برگزاری آزمون‌های تافل و GRE رسماً در ایران متوقف شد
🔹
مؤسسه ETS در صفحه رسمی ثبت‌نام آزمون TOEFL iBT اعلام کرد که در راستای رعایت تغییر اخیر در مقررات وزارت خزانه‌داری آمریکا (OFAC) برگزاری آزمون‌های TOEFL و GRE در ایران متوقف شده است.
🔹
این مؤسسه یادآور…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/686915" target="_blank">📅 16:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ce38f22d.mp4?token=NAxRVATnri68gX2cu3i93NAtBwSSS5JEkvLOmIv0aGABnDDK2RkMPYziCfEr1WztXOLS7KmFs5j_fZM5DjEXkd8eelb6Kl46Tg9Fg38s0J91qpugCuWlYOT0y7vfy32BWtvXlgfAh3I4ZPluMmNWlHKcl8w38PPG_sq9AnhsxEiVnWl5BwKleG5pUWzDVjRwNTsjGMhFYKxc9Dd32xB6xlkno_jo2m4kKwy8OJSdsOMkWHRZNjZBJLsNbv6aZKyvtpr6C0vFQ4sofXtBNHrO2DDjOJUKRMnsn5KrcuJA2pFs0ceWCjMWqaCeMSwHzobLBF7h5wcyL6G6grhc1N_7QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ce38f22d.mp4?token=NAxRVATnri68gX2cu3i93NAtBwSSS5JEkvLOmIv0aGABnDDK2RkMPYziCfEr1WztXOLS7KmFs5j_fZM5DjEXkd8eelb6Kl46Tg9Fg38s0J91qpugCuWlYOT0y7vfy32BWtvXlgfAh3I4ZPluMmNWlHKcl8w38PPG_sq9AnhsxEiVnWl5BwKleG5pUWzDVjRwNTsjGMhFYKxc9Dd32xB6xlkno_jo2m4kKwy8OJSdsOMkWHRZNjZBJLsNbv6aZKyvtpr6C0vFQ4sofXtBNHrO2DDjOJUKRMnsn5KrcuJA2pFs0ceWCjMWqaCeMSwHzobLBF7h5wcyL6G6grhc1N_7QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با استفاده از هوش‌مصنوعی نابغه بازارهای مالی بشیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686914" target="_blank">📅 16:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b424c36ef.mp4?token=I7cRZ_8zyQ3oR8x1P1TdZWduIx-HjugIoK5VUY94OtmZsBqMDmlymlusN7ewwhtrhTiufQes5Cpk6b21Q8PYuzbIXzU3CMwq1sf1lDouHkW0ywA_LVe4M03d9FfHPDRCAqRUkMWP733U428bbjtiWmVkgQzC0z7B7myrMXpCp0WGxkdZkTIvD4AKMffWpKd3M4K2F3F7cKtTR3l1pu4K-FdeAJhnRuUb2ksTiVk39yC2Io515ZH8qLE8iDQVOFJPEeBeWEe1ANSVq5FrntQ-X9It7pNLhjgch3fU_j9GxVf48FmffIatXUz1KGxPjTaA_RWCBXd3gZJJnIIvfBcwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b424c36ef.mp4?token=I7cRZ_8zyQ3oR8x1P1TdZWduIx-HjugIoK5VUY94OtmZsBqMDmlymlusN7ewwhtrhTiufQes5Cpk6b21Q8PYuzbIXzU3CMwq1sf1lDouHkW0ywA_LVe4M03d9FfHPDRCAqRUkMWP733U428bbjtiWmVkgQzC0z7B7myrMXpCp0WGxkdZkTIvD4AKMffWpKd3M4K2F3F7cKtTR3l1pu4K-FdeAJhnRuUb2ksTiVk39yC2Io515ZH8qLE8iDQVOFJPEeBeWEe1ANSVq5FrntQ-X9It7pNLhjgch3fU_j9GxVf48FmffIatXUz1KGxPjTaA_RWCBXd3gZJJnIIvfBcwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار بابک زنجانی درباره پیامدهای نفوذ در مجموعه‌های اقتصادی کشور
🔹
بابک زنجانی، مدیر گروه ارزش‌آفرینی «دات‌وان»، در حاشیه نمایشگاه الکامپ، با انتقاد از ساختار مدیریتی دهه‌های اخیر، نسبت به پیامدهای «نفوذ در مجموعه‌های اقتصادی» هشدار داد.
🔹
او گفت: در سال ۹۱ که من بازداشت شدم، نفوذ در کل مجموعه‌های اقتصادی کشور رخ داده بود. این نفوذ بود، نه چیزی که به اسم فساد مسئولین مطرح شد.
🔹
زنجانی معتقد است بازداشت‌های سال ۹۱، پوششی بر نفوذی بود که در کل سیستم اقتصادی کشور رخ داده بود؛ نفوذی که هدفش زمین‌گیر کردن مردم و فلج کردن معیشت بود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/686913" target="_blank">📅 16:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyrOYLZD37pzmKJkFosqvCGlQLN80qkywwOPGVlzDNx5_PQOm_Lbj4LRYQWImAqxU2vfPe1v3PeuVMKI2N2ygYk2zJEI0INi68JE0-KLVsyIBQY0WlpNt-s6BZacSdYZ72bZVzWoqZq52cdgQdNOnUtwAJQ4QZ9-kf0nalV_TnCDZqpzlpdwZMnO7Kt7eef3ZXezrJWgCkcwpKJP8Bc5zAVcPu7j7DQufBuxfCovI6jJwfXCZJJaIn-75UUc71hOlSYaWz45yiG9YsO8FCvLx-NcZY5kj1OQZb14Zt9w1uH1UN_bNixZJ9jv931v5ji6dRyjOfdFmfaw3q--rea56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات خنده دار ترامپ: سوریه خود را به عنوان جایگزینی برای تنگه هرمز معرفی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/686912" target="_blank">📅 15:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_P-pzm_npJteIzEfjbNQveoVpU7ncwQjZjw5bXcHwt4uFNZOtjJ1T42fJ2IXQPmXw4hM5bBtytY9v2YcbB3EY7AYm0vnSOmkjOmpg8S-FG0CKrIieUZrZuSdBAgsxlq2R5N5rN3hkvjSbX2B52FHou13aZ6IJeAMJM75gGA5__JUKr_Wb5TluroEXtGBikb8Tq3nO4S1cDcF35CcFhepYbNtJ4D3xXv2dormkc_i6cyQRZlMX3PPH2GPgCuzX0Sa--HcYTCtLv6jM-3x4abkYwtL3vvQUOOT6vkRnPlA1yiNJsw6NPqBtuzQ1wn87SE8IIodJuNpPGU6rTbNhcbNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز: پنتاگون به نیروهای نظامی دستور داد دیگر از عنوان «عملیات خشم حماسی» استفاده نکنند
سی‌بی‌اس نیوز:
🔹
مقامات پنتاگون به پرسنل نظامی دستور دادند که دیگر از عملیات جاری ایران به عنوان «عملیات خشم حماسی» یاد نکنند.
🔹
این دستورالعمل توسط دفتر مرکزی روابط عمومی پیت هگزت، وزیر دفاع صادر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/686911" target="_blank">📅 15:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سرلشکر وحیدی: سپاه و سایر نیروهای مسلح پاسدار حرمت خون شهدای کوهستک و دیگر شهدای اقتدار ایران اسلامی هستند
🔹
فرمانده کل سپاه در پیامی، حادثه حمله به مجلس عروسی در کوهستک هرمزگان را محکوم کرد و آن را اقدامی تروریستی علیه غیرنظامیان دانست.
🔹
خون این شهیدان بی‌پاسخ نخواهد ماند و نیروهای مسلح جمهوری اسلامی با قدرت از امنیت کشور و مردم دفاع خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/686910" target="_blank">📅 15:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900e9f9010.mp4?token=E5kh2nEjXBlsRgSzQVtZ-J6i-2iP5Y7sBjvn8ei3gPVHc77DiTsaDIPAX8fBvsZSB0V0MdqGcRCWTgtqiXQEHqAxVg1ajJ_xV16LjueP5CWXbhYizsout1WSp8LU7i10o5R-WjSvYFSQ_JXi11A_tCoQXDNsyo03UaR1GXnBp92rnWSlrJDHkrsZo865vARPMrh_lTD9WTBlZSDbDUbYeo552qzxCxKWpX97INTKexVZpeSGGIVZAfSCzh6qNBzwsXk3-EJOekUSMwr-PiDI37hEX6HApTduEh815WLFDWpONs2yE2-CukDZ7RrsLMAZqmg_E_QVXYZBa3nfr3cC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900e9f9010.mp4?token=E5kh2nEjXBlsRgSzQVtZ-J6i-2iP5Y7sBjvn8ei3gPVHc77DiTsaDIPAX8fBvsZSB0V0MdqGcRCWTgtqiXQEHqAxVg1ajJ_xV16LjueP5CWXbhYizsout1WSp8LU7i10o5R-WjSvYFSQ_JXi11A_tCoQXDNsyo03UaR1GXnBp92rnWSlrJDHkrsZo865vARPMrh_lTD9WTBlZSDbDUbYeo552qzxCxKWpX97INTKexVZpeSGGIVZAfSCzh6qNBzwsXk3-EJOekUSMwr-PiDI37hEX6HApTduEh815WLFDWpONs2yE2-CukDZ7RrsLMAZqmg_E_QVXYZBa3nfr3cC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ بابک زنجانی به حواشی ترانزیت سوخت: ما گازوئیل نخریدیم، کار لجستیکی کردیم
🔹
بابک زنجانی در نشست خبری حاشیه نمایشگاه الکامپ، با شفاف‌سازی درباره فعالیت‌های ریلی و ترانزیتی مجموعه خود گفت:
🔹
«ما به هیچ عنوان گازوئیل نخریدیم؛ ما شرکت لجستیکی هستیم و کار ترانزیتی انجام دادیم. روسیه بنزین و گازوئیل خود را به بنادر شمالی می‌فرستد، ما آنجا تحویل می‌گیریم، با شبکه ریلی خودمان ترانزیت می‌کنیم و در افغانستان و پاکستان تحویل می‌دهیم که برای کشور تنی ۳۰ تا ۴۰ دلار عایدی و درآمد دارد.»
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/686909" target="_blank">📅 15:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvMGGOu7H9DxOT5G5aLaL7vY_6XdQo4nKYlkaE63dRG3GiiGQ4Pfj56AbNQBU7OHRvAyj3m8uaShRi3jB74j6IfczRAsN-laswuy7FDtIRtMx9NmiMSJewCkAgXs0UFvkLu9cejpzXG7kHXVBLG75p1Sh7igysZsR8R3CyeX7D33P4L7ZmrNnDAk94Mo79bY32iwL2NmhtuMtWEMZvbJSSBzWkos0ZRJS9tZd0sK6g8ElXLQHtYf1xAIaSSZsFfPxRxBVLV80Sj2awy3_Gaz52zntmHRzNiq5iy603vodhNYDRRkHUZ30GN3x-OsrD0VowqGJIygE2FKj7wiZdjIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ۱۸ آمریکایی در جنگ با ایران کشته شدند
دونالد ترامپ:
🔹
«وقتی وزیر بازرگانی، هاوارد لاتنیک، گفت کسی کشته نشده، منظورش ونزوئلا بود.»
🔹
او افزود: «۱۸ نفر در ایران کشته شدند!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/686908" target="_blank">📅 15:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50bc8b540.mp4?token=FtT-4G6rUfAN_IorLL2RvKd_qMj-rYUZD9Op3MHo-4v0nbRrB4LXSRWEkdkDj3ZPVTe_NhkTtdja7bvyRdpqG8WmU0jYrR7zFOpYSh8MlNHsneBNOZQyOEwQRYUAGk4_khimMJuTEadGv5yMvQ3MyR68Z5E0K6900L3jHxyf8feRR6wNRrz6Oe94LQfzbGaeSOLsMaM-0rIawICMXvwAxxtvjsyprAKaaC7eIEvkEViHtA6JroAEYAyVzAOtOaeQcZHTgbKfpBp8bE9jV3XLpiz5L5oeWU39NAb_GZUj8-fNlABpZ6kbEFwAIByD4Cc9Ykl37oD0e0YWYp2cP3fh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50bc8b540.mp4?token=FtT-4G6rUfAN_IorLL2RvKd_qMj-rYUZD9Op3MHo-4v0nbRrB4LXSRWEkdkDj3ZPVTe_NhkTtdja7bvyRdpqG8WmU0jYrR7zFOpYSh8MlNHsneBNOZQyOEwQRYUAGk4_khimMJuTEadGv5yMvQ3MyR68Z5E0K6900L3jHxyf8feRR6wNRrz6Oe94LQfzbGaeSOLsMaM-0rIawICMXvwAxxtvjsyprAKaaC7eIEvkEViHtA6JroAEYAyVzAOtOaeQcZHTgbKfpBp8bE9jV3XLpiz5L5oeWU39NAb_GZUj8-fNlABpZ6kbEFwAIByD4Cc9Ykl37oD0e0YWYp2cP3fh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند جالب بند اضافه کوله پشتی‌ات رو تبدیل کن به ستاره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/686907" target="_blank">📅 15:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5962991312.mp4?token=fOqwAILiEUrvELEHeCh-WfFvWIgnRp7Couc0gL23u47lWH10Nd3_dUBFqmyxto_soPLwunMTbdf3SnNTNYArBnq2F6LjxwfzS1fHStWJRg05YUhWoOshrxNf9x5VDahE-OuSX46kRwJMZ_3fx1ZeU89mabJJwdCPVhdl7CdqoaPm46ghLkWAFAJcexX-K5TwnfNad0TVhOg5XeNur5eYI4k8CiJWfaEzpV4XL--WD-Wz7YNeI2-D9wWkRda9mo395C0NFPmFVsxtDhNjqinD_N6cIxqe4gDevQBo9ju4GYq8zWcmP9guQ026cKc3Bt0mZmxWcm9uTV9U7LGZWRKZ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5962991312.mp4?token=fOqwAILiEUrvELEHeCh-WfFvWIgnRp7Couc0gL23u47lWH10Nd3_dUBFqmyxto_soPLwunMTbdf3SnNTNYArBnq2F6LjxwfzS1fHStWJRg05YUhWoOshrxNf9x5VDahE-OuSX46kRwJMZ_3fx1ZeU89mabJJwdCPVhdl7CdqoaPm46ghLkWAFAJcexX-K5TwnfNad0TVhOg5XeNur5eYI4k8CiJWfaEzpV4XL--WD-Wz7YNeI2-D9wWkRda9mo395C0NFPmFVsxtDhNjqinD_N6cIxqe4gDevQBo9ju4GYq8zWcmP9guQ026cKc3Bt0mZmxWcm9uTV9U7LGZWRKZ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: حجم محموله‌های نفتی عبوری از تنگه هرمز تقریباً به سطح قبل از آغاز درگیری با ایران بازگشته است
🔹
ترامپ در شبکه اجتماعی تروث سوشال تصویری منتشر کرد که براساس آن، در حال حاضر روزانه حدود ۱۸ میلیون بشکه نفت از این تنگه عبور می‌کند؛ این رقم پیش از آغاز درگیری حدود ۲۰ میلیون بشکه در روز بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/686906" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
غلط اضافه وزیر دفاع اسرائیل در تهدید ایران
🔹
اسرائیل کاتز، وزیر دفاع اسرائیل در اظهاراتی گستاخانه مدعی شد که حمله ایران به اسرائیل ما را از تمام محدودیت‌ها آزاد خواهد کرد. ما به تمام زیرساخت‌ها از جمله زیرساخت‌های انرژی حمله خواهیم کرد و ایران را به عصر حجر و تاریکی باز خواهیم گرداند.
🔹
بنا به نوشته تایمز اسرائیل او گفته که که اگر ایران به اسرائیل حمله کند، ارتش تمام زیرساخت‌های رژیم، «از جمله زیرساخت‌های انرژی» را هدف قرار خواهد داد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/686905" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686895">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9awRoslUiUy-MDsDvnHUIDbBtStIU2xIgWMtDh3IY4gAo5njCTfjvx1ZpihthSiWg1kZ5n7oQkpIv4wMthhvp054CjqqSTj5uXvQV_Pmrad0y620jfevp9P4Aau8lq2tHN51F2MwUKJaAlYQNV4LHMkLsDteRYdTgen0snOPbzBG4xuulVq6yMGxTzXoFzYK4bMSGVc5AVEEHevE2l6I0hn3doz0O3J6QHiLdtfqvq7BPlE8S1z3Px2n-Yi8sp04kaJgdsjrhjo3m9YgmFZd7obIl0fHpepW3MKtdbCV1Kui8oaemrBvqJp4NbdBQV5tiNcE0peRSGRt_y3jSVPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf9gCDuvlodYT1pIK-LzAIUnpxNWvZ5sAV3jMPZ3bQpLZNjgsr0cqUzZpCM5qTT4uyXsFyPEVkX7AT4dcA0DcLg2WrLZmUX3kNJGEWQERWsbBvMWUXoi1j1jI9Lchx_Wh3N4ISfjsLBoSCaozsTTEnSxxs8V81Ip-FgdsCW8URTH2PJ4HvzrhB9ACcA4HQYVlRs1G33NqgO2FPDGr1u4nXkgp8P1wERfw91oRdHIXKMGrg-xXfz3XX6d5mknnfLd-tv6cAqFqU679fTrESu3z16CAumtZyquRkSL_mfu7hiLvaA6j8KfjxbgQR7OBAx12mt3fUiTFG72QdRgo1dxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHCSHcl1o_HSTs5t0Z4EIjrJ03c3YVtwQdBIjTM_IVIPshIUU-C6viHvRE3wM64ZO8oXboOcspRlIWB9HGsVTFFq3tcS0RcZabtaBivQ5OrFALFe17mvXezdAIRfABViJcgbSDX9o4HgdyDxqoE2pAz2xwxYRR5_zMIFLOK-cXsQ5XMHT-sPs6Yi04Me4drDQAaq-6Bp51_aoslX50oqWCX_IHsG1rry-1iEnJrLPg5AGCKzGq_YKFJemmI_RvUnNGhzPYL2yfWFUcTcKqVKkv69fsCkqp0tA3uqVHK9ZLNvZNBdTXmz7ze6rIcCGtHIn4T6Nra26WY_adcF8U-PWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSkEyi9FX6JywcAYCLez6lFi_GeiPUKtsnf0Wtgijn_-LXPjJN0no8l6llBNKAvucOdVSzM0WJTRK5PQE0OgDduRJ-pNXwB2U8HElvSqj5JKiuHsGLH6n5NiIpopDELOHoBhrHYIR2LqUyTS27lbElY_i8wsjhtlhheFODwNsz8Dgj3D8yUq3gMdz1_rfDS3pDWQHVF1Xf81ia6gwWuxUoQeb-7gbaYXXfxjCkJK4IvLzYmxA1_iR-XN59IcHzz8cTG-IYtiN-lVkzhcdJdA9qgPK2tZ9FxM8nuvjW0uY7ZrPuJi9Lq2TVteD9wGbZ_hIDl9E_NEyWU06NxlQlThIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWJJG7GWamQH22xccrPT7WSSb_hWzzI_VKu3pzngshQilNNJIz3bFSbqESTWLkAMT9XMnZiEPEQl4x0KCqumU4f24XZfi8WH7fmBEcyb72CVSlGNFsRUIqklqxyys6LdxgzsG_7coeBxN1GnM95h4ctZAAybBrZO1CUl0iuM0LQAbUPuY-B5-_AdH2wCk5_en65unx7GTNJGBmife0CKmOIcIJElQcoKLWyIp58KPVJWsilmJNUL8yvxE4TyRaTTYB9VGWX2GK2GBd-mJQUBn3DxX9BvMNY-3KFLObbAKu7os4U5UorpSMVvgixwXyO2IsQvj3WmsPh7jTTFCvu9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzdGjGQDY6aX1gr_hVaDFuMozpIJ0NXvDv7Yfdk07zRw-TnkcRJbmy_hHWGbbi4iE_HZait68feWnHyAtZLSHruDkOqGakAdWCspv1dWQFVi_XkuyXEBGdipBE0X9ee2uoJH-1-sCcLdII8hi3ooabRuCC58J2hhK-JRePy0cOXkQFm3izmQuihHvwWvspsYXtSfIfa6uk5_XEWrGSDVsdvMSWGAQDBlfgGfLVV64DPQd3V9Tm-G9edE4OYkRhTHIiErY_N3uU9MR8usK5tMWP7D-EB5f_slMmm59prAfW2Yx6tESWFqaFZLREWnpVOaVhqUPssYvdaewUBYbd2o6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV_VAygaf5UIoSokNLC-lZN5iLAtnEZYyySO_8EZ0_t2K1ntg-163OIeg-Wc5UZnBR1MNJj1gPhYLDeb-n1DVpJdZ3DBcR9L-Dz0i7wMNteXucK6zixM-8BJ0WwvZtP5BfwtYVdoiWV6-MsznSrhA6qnpBPLt0FhLjla6oSWpuvvW1rpcVgpnI2bK1I0O0Mm42wNps_cKJw0dyD9CK_fBjhf7xynOJG2MD5GPZoQeFykDD4bFyLpBEG2OxA-Kek9UgCodDYPEBzC-723H5dkqgKLVsw2cU438JgrH_0Xnca4xslyDtZagftv7wXvM_I5sQsui2RDH6KprQ7xpJOlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLCxCDXX5rxNHbv3ftblYrCCWIVFLS3XDNBfE_RzJGHDmGgeajZanuT6F3prOSFdwhiPcGAh4Gnl-bEYrCB34p9z0z-HGisiNjdDGyV4lwBPRU9JY79inpJ-Odk67C_-0wTus2SuC5cYMobU3uuZphvOgifFr50N6eJ9wuO39imTeV3ohYinWgyvRdyE0OOY0gIPjU1MCrgxWHpmPqisGd-OfppkNkgoybUXM-nECtFEf-sbwtP3tbijkENYct5tvAW9JjvWWZwnzmHtahAKiz6UuK7HFojA_lIOql7DoEQQ3wkKt8KWxp0Hoc5BezufuPyYUjD81DW_WrEZybOE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWv5uYIV1ZlNuD1nWKLElmWjtw6XjQq3K8KAxMnx9WwfCbb8xRk6kijvD6j0uQXe66EmDa71X0yZyVcpS6g_w4WXpmrE0PYABkRqDsysmQtru1-dxWzD7u0b7-g4v04MYJNItQ7fR38Y-t9fASp7k2LUSzFIX5KzBA6_LrfUS4oc-6M51vXOgaAIfhzDM8CeKHOd58ERkg86lyBEOxY7TuWhSt3K-OJGu0rnmWu9YMQIwT8p06XsCWm-qGEkveHXyTQsaIHHvuF_yof3Za_ciE96FL8JmywaGSUISiyd5WEIytY4tMq7zXYBS7vUn_XprWaaBrzlvbN32WPQug4HCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYw8pj_fdApSOHzjeuJFM9dQQw5UBpDXcw7USDFVgMsyLrmFkvilna0Mp16Y2zNRC13Vh8fjwi6RPoiEYe9whYIr1YynErU0jODS2iajHcLWR3d6CxYBu9o8S-3z8EFHI80Dk1sY9IqcxPzD73ME4Cx2Mae8q6SyelAEGHNHVaQBMs7wHdARKcNlwJR69FVYaIHueJ2xjA7s3GNDO0E4R_4dE-u8VLAd-b8WP2TWKVarCeolHyQMmLz_ZVdS29YawwrisuAPAiqrIY-j3a6T8vY5kdZzgB9Jzssw7Ma3S20LiMgsoF4U9zGFPRH9X1crDzvzUa42hgMw1uBV7L6oFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و چالش‌های واقعی در تأمین داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/686895" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686894">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b75a927a.mp4?token=AQ3uvTZMfnJ1ZO68t_yTuolxA3Prcht6BLcuQO41WpAiXeIzaojZu4f_pRSVcVeG6IbQJnlN5C3poy25-EEDLAZpEZt4G7J2y481LQf9gotcWTS9cwbgXTgUjsBMAS9VoUvenC806pBVJH22D3o7MsGhLXZTTMOH2GUwFfLDGo1yRfNp68aWwekDEOSJyUJ0sj6ZFbUxsJgMqtDTmjgh2Z2UOZxCfMyTMf7D2GRZcT8hS7vvbp8Op-utrgSiBc0WkR7EuAr0N0HIMA6zCF_5lVZMD3cR30SmyLmOqomqPjvpkmVwFD3T33i5b7cNy3ellSlaycn9HWR6CXaMUKStWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b75a927a.mp4?token=AQ3uvTZMfnJ1ZO68t_yTuolxA3Prcht6BLcuQO41WpAiXeIzaojZu4f_pRSVcVeG6IbQJnlN5C3poy25-EEDLAZpEZt4G7J2y481LQf9gotcWTS9cwbgXTgUjsBMAS9VoUvenC806pBVJH22D3o7MsGhLXZTTMOH2GUwFfLDGo1yRfNp68aWwekDEOSJyUJ0sj6ZFbUxsJgMqtDTmjgh2Z2UOZxCfMyTMf7D2GRZcT8hS7vvbp8Op-utrgSiBc0WkR7EuAr0N0HIMA6zCF_5lVZMD3cR30SmyLmOqomqPjvpkmVwFD3T33i5b7cNy3ellSlaycn9HWR6CXaMUKStWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده یک اتوبوس کلمبیایی یادش رفته درِ اتوبوس رو ببنده؛ غافل از اینکه همین اشتباه ساده، قراره جان یک نفر رو نجات بده!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/686894" target="_blank">📅 15:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686893">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پولی تراستی‌ها از دهک‌های فقیر و ضعیف جامعه بوده است/ سال ۹۷ با دلار ۵هزار تومان نفت فروختند و پول ندادند و الان با ریال برمی‌گردانند یا برنمی‌گردانند
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
تراستی‌ها سواستفاده کردند به طور مثال در سال ۹۷ که ارز ۵ هزارتومان بوده است، یک میلیارد دلار ارز در اختیار یک تراستی بوده و درحال حاضر که دلار ۲۰۰ هزار تومان شده، ثروت این‌ها چهل برابر شده است.
🔹
کسانی که به عنوان دور زدن تحریم‌ها تصمیم گیرنده بودند، باید این پیش‌بینی را می‌کردند که مدیرانی را بر سر کار گذاشتند، سو استفاده کردند.
🔹
خیلی از مدیران تراستی ویزای خارج از کشور دارند و برایشان مهم نیست که معیشت مردم مشکل دارد
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/686893" target="_blank">📅 14:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
میانگین قیمت مسکن نوساز و چندساله در تهران
🔹
بررسی نمودار قیمت مسکن در مناطق مختلف تهران نشان می‌دهد میانگین قیمت هر مترمربع واحد نوساز حدود ۳۵۵ میلیون تومان است.
🔹
این رقم برای واحدهای چندساله حدود ۲۷۶ میلیون تومان برآورد می‌شود.
🔹
یعنی خرید خانه نوساز به‌طور میانگین حدود ۷۹ میلیون تومان در هر مترمربع بیشتر هزینه دارد، رقمی معادل ۲۸ درصد اختلاف قیمت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/686889" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686887">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
شهادت ۶ نفر از نیروهای ارتش در حمله تروریست‌های امریکایی به جنوب کشور
🔹
در جریان حملات جنایتکارانه دو شب قبل (۱۰ شهریورماه) ارتش تروریستی آمریکا به نقاطی در جنوب کشور، ۶ نفر از نیروهای ارتش جمهوری اسلامی ایران (نیروی دریایی) به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/686887" target="_blank">📅 14:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686885">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cb4df88d.mp4?token=vY_Hfh3f5ztfqgNbz8WCVgrPJtvUph-xx4qlrCUj4dkpaOARqRmPHAYM6J6BJMPOjXqKF0PI1dtDy_fId1CU6GM8-T7qK7-jaxZOV6sBEc7YY1OoY4Qip9U7_BoSpdLHmDe25_Jfi5qXjVv2bY2oBREqJQGFVrW0JVG9u8cQvwKwKtIsf-J3IxiF9grYVQYOqKDlztEEU52IsKMjCkndEe5u0AT-eoWW7EieC_CZLCmc_bAtqbsV5xNYPE7wzGZMwoeGm3Fu5W6w7YQh38sRDqX22Y1flGP52HnahhDJL5v5jb-Rj_L0t9v0RYe1-7eDRPOGgFsZZzq44bn2yWX5xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cb4df88d.mp4?token=vY_Hfh3f5ztfqgNbz8WCVgrPJtvUph-xx4qlrCUj4dkpaOARqRmPHAYM6J6BJMPOjXqKF0PI1dtDy_fId1CU6GM8-T7qK7-jaxZOV6sBEc7YY1OoY4Qip9U7_BoSpdLHmDe25_Jfi5qXjVv2bY2oBREqJQGFVrW0JVG9u8cQvwKwKtIsf-J3IxiF9grYVQYOqKDlztEEU52IsKMjCkndEe5u0AT-eoWW7EieC_CZLCmc_bAtqbsV5xNYPE7wzGZMwoeGm3Fu5W6w7YQh38sRDqX22Y1flGP52HnahhDJL5v5jb-Rj_L0t9v0RYe1-7eDRPOGgFsZZzq44bn2yWX5xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیستم جلوگیری از چرت زدن در خوابگاه‌های مدارس چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/686885" target="_blank">📅 14:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686884">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5d3ddb7c.mp4?token=sqrFti8sPuoxiapJXFdAJsR-OVeEMUe0EI8FydrilqN7YBEayHQ8PtH8_xse9MUtAeyn19MXfGFS68qyOAXbWF-Zi9N7-8y1zeZQ9-UjUF7k8R138N8Q5nEh9FVHLpuNyFR2AEW7XcqIrODH_Pzsbh2V6Fern4zFoW9klllkaIO73ikCpqok2BFCc52upl3NLxL9Z_JCWMffxjHZUcY4SjkNOIdiAUJdGhwKgQss1lTI94R7C_9uVygHQ-w7LMxLaSmAus-OCrOkYvzxYmskRa4MX94YfHLH4tROswWrjPBp6s4KvPTBx4pkR49wYwN6daFFAL7LIUP6nLqLQGMwXbtNumoAbxt7JEdwGPP-d5e9nG_-eTgDUUd8r8c7IMIPq-Y0_iKOAPhlMOKd-7RRtIcAbJH3ku-trPtiFhvr2ADOtMx3wwsWnUufr5TnbAJnwsox-DQHtr38ccMUdN700sIO67ZtwY0XYcwqFRaZgMTqHwNMaXcI5MoM5ozGonU07oowvmhYR6ZWWyytjOLJRjYniLZ0etDQ06lFaPPyaQZKCBGZywqDJUKJofNDw65R_vTAM_sPyup_YQz8rOpNECiFk2yy9pOrf8aUZjWOcfX8BJLYyNz27icvaSHGKvLj1yT9kX-S1-_jjF4FnGIVazVs3uN1yBE2U-4Neyl-gzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5d3ddb7c.mp4?token=sqrFti8sPuoxiapJXFdAJsR-OVeEMUe0EI8FydrilqN7YBEayHQ8PtH8_xse9MUtAeyn19MXfGFS68qyOAXbWF-Zi9N7-8y1zeZQ9-UjUF7k8R138N8Q5nEh9FVHLpuNyFR2AEW7XcqIrODH_Pzsbh2V6Fern4zFoW9klllkaIO73ikCpqok2BFCc52upl3NLxL9Z_JCWMffxjHZUcY4SjkNOIdiAUJdGhwKgQss1lTI94R7C_9uVygHQ-w7LMxLaSmAus-OCrOkYvzxYmskRa4MX94YfHLH4tROswWrjPBp6s4KvPTBx4pkR49wYwN6daFFAL7LIUP6nLqLQGMwXbtNumoAbxt7JEdwGPP-d5e9nG_-eTgDUUd8r8c7IMIPq-Y0_iKOAPhlMOKd-7RRtIcAbJH3ku-trPtiFhvr2ADOtMx3wwsWnUufr5TnbAJnwsox-DQHtr38ccMUdN700sIO67ZtwY0XYcwqFRaZgMTqHwNMaXcI5MoM5ozGonU07oowvmhYR6ZWWyytjOLJRjYniLZ0etDQ06lFaPPyaQZKCBGZywqDJUKJofNDw65R_vTAM_sPyup_YQz8rOpNECiFk2yy9pOrf8aUZjWOcfX8BJLYyNz27icvaSHGKvLj1yT9kX-S1-_jjF4FnGIVazVs3uN1yBE2U-4Neyl-gzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقشه بزرگ بابک زنجانی برای مرزهای ایران؛ از ریمدان تا سرخس و آپرین!
🔹
بابک زنجانی در حاشیه نشست خبری نمایشگاه الکامپ، از برنامه سرمایه‌گذاری گسترده خود در زیرساخت‌ها و بازارچه‌های مرزی خبر داد و گفت:
🔹
«به سرعت باید تمام زیرساخت‌های مرزی کشور را باز کنیم. شهرها و استان‌های مرزی که امروز پای کار این کشور و نظام هستند، شایسته این هستند که بازارچه‌های مرزی‌شان فعال شود. ما هم داریم سرمایه‌گذاری‌هایمان را در این بخش فعال می‌کنیم؛ از ریمدان تا شلمچه، سرخس، آپرین، بندر ترکمن و خواف داریم انرژی می‌گذاریم تا زیرساختی فراهم کنیم که ورودی‌های پول کشور از این مناطق افزایش پیدا کند.»
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/686884" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686883">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
مرغ بالای ۲۸۰ هزار تومان؛ گرانفروشی است
دبیر انجمن پرورش‌دهندگان مرغ گوشتی:
🔹
فروش مرغ بالاتر از ۲۸۰ هزار تومان گرانفروشی است اما در حال حاضر هر کیلو مرغ در خرده فروشی ها به دلیل ضعف در نظارت‌ها، با نرخ بالای ۳۰۰ هزار تومان عرضه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/686883" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855cdb85ed.mp4?token=lym1A0ix7kC_GpEreb1XkcYe_-HlJXnTG5TSA8HA5Jo3kj-cDiGocdY6e-MX2cxttYUNqY-sXkAOZkrFWMxrZcZFq9lSlR5nQ-kLLDPcc1lX0fo-Dmtm2GCn9KE85QJ1VDgxqoFseF2S1pym2VLaNlyYrwQurWmA06H5ROpAzM7zXZH7TUpP1ityXIOoJsEUcXYXwtLZq5juwT-tBqNe4F7B_OeTvwKVnZ13re8tBhZPeUdLp3uTQWqVmZI-vHGf5EdrUFXmHGzvC002wGhqZvH9eUWZSYTY5i-2boEfFvKcLyT_9nkEEBpppZDrdU_9SngK1EhTm0QPzefGidbOCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855cdb85ed.mp4?token=lym1A0ix7kC_GpEreb1XkcYe_-HlJXnTG5TSA8HA5Jo3kj-cDiGocdY6e-MX2cxttYUNqY-sXkAOZkrFWMxrZcZFq9lSlR5nQ-kLLDPcc1lX0fo-Dmtm2GCn9KE85QJ1VDgxqoFseF2S1pym2VLaNlyYrwQurWmA06H5ROpAzM7zXZH7TUpP1ityXIOoJsEUcXYXwtLZq5juwT-tBqNe4F7B_OeTvwKVnZ13re8tBhZPeUdLp3uTQWqVmZI-vHGf5EdrUFXmHGzvC002wGhqZvH9eUWZSYTY5i-2boEfFvKcLyT_9nkEEBpppZDrdU_9SngK1EhTm0QPzefGidbOCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ایران هر روز ۸ تن برنج دور ریخته می‌شود؟!
🔹
جزئیات این ماجرای عجیب را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686881" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سوگواری برای آینده‌ای که هرگز اتفاق نیفتاد
🔹
گاهی لازم نیست بیشتر تلاش کنیم؛ گاهی باید چیزی را که دیگر وجود ندارد، رها کنیم.
🔹
ما فقط برای آدم‌ها و اتفاق‌های از دست‌رفته سوگواری نمی‌کنیم؛ گاهی برای آینده‌ای سوگواری می‌کنیم که هیچ‌وقت به دنیا نیامد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686880" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1eb80dfe3.mp4?token=POH9O-XaR9oS_B71dXjtse9mcV_8LyKOZMnQIsjxuLIYZxNjdMyP6M3ADPK5wG6Jc3XmX1g1oHP8Mi3oQU1tEHV3KPxiIQ8CfcCXehAoVWssl3vIi00NRGjWRx4xYcAWbGzrzUFM_y7VWZfrY93qchwko_YK6AZuAsXaI9_UUgYrwTmxrqug_XW3yOI8GOSDG2wftOw68RtLkr6VQYJhBzIA01F2DUOhDECtd7XW39JKqgTLRkwwxFM3NTn-7dD6Zd6SrSfFu-156QEWSHLKEJBE2yR1PT82ANx5FBR2Y8ykFGGMNhUnXRhnLCn26Y1Qorx8zwk2RaqMiDT0TuILrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1eb80dfe3.mp4?token=POH9O-XaR9oS_B71dXjtse9mcV_8LyKOZMnQIsjxuLIYZxNjdMyP6M3ADPK5wG6Jc3XmX1g1oHP8Mi3oQU1tEHV3KPxiIQ8CfcCXehAoVWssl3vIi00NRGjWRx4xYcAWbGzrzUFM_y7VWZfrY93qchwko_YK6AZuAsXaI9_UUgYrwTmxrqug_XW3yOI8GOSDG2wftOw68RtLkr6VQYJhBzIA01F2DUOhDECtd7XW39JKqgTLRkwwxFM3NTn-7dD6Zd6SrSfFu-156QEWSHLKEJBE2yR1PT82ANx5FBR2Y8ykFGGMNhUnXRhnLCn26Y1Qorx8zwk2RaqMiDT0TuILrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لبخند کوچک، امید بزرگ
🔹
نوزاد کوچکی که به دلیل بیماری قلبی مادرزادی در بخش مراقبت‌های ویژه بستری بود پس از یک دوره درمان دشوار با لبخندش دل میلیون‌ها نفر را گرم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/686879" target="_blank">📅 14:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB4GxQdOb5CdueRs8DL3wmZ-DfU6H_jM0hayb-uVbU2i460Ld7hVm6WV-ex7tHEpNwcz3Sei_DfkkvAI51DEgWVNRwsMoU_KgroBf6fvPsT7nrLRYRdX24O5_2yf-tevvQ_wV4klz_lt9mWXfNXeJpVU6tLqC_2X7DXM-0Wu_kg9KI30aStzjgTNtENaJh1CemLkiiI5qkQZCyKKxQ5QpQMQv2OvbctEnv7y5Nq9-due-u5cMZAmkAEWdWrHZDv_9yqMBDr5hxoHVJCdpJJoSEywwkHDacUelgegrNEjYe2G3_TGF_4_6fT0cHHWmJ0bC29jMP93yFzoDMzp3RM6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686878" target="_blank">📅 14:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
خودروهای خارجی در ایران چقدرند؟
🔹
در سال ۱۳۹۰، از تولید بیش از ۱.۴ میلیون خودرو، تنها حدود ۴۰ هزار دستگاه وارد شد، یعنی سهم واردات کمتر از ۳ درصد بود.
🔹
اوج واردات در سال‌های ۱۳۹۲ و ۱۳۹۳ هم سهم وارداتی‌ها را به حدود ۱۱ درصد رساند، یعنی به ازای هر ۹ تا ۱۰ خودروی داخلی، فقط یک خودروی وارداتی وارد بازار می‌شد.
🔹
اما از سال ۱۳۹۷ با ممنوعیت واردات، این سهم عملاً به صفر رسید.
🔹
حالا با بازگشت تدریجی واردات از ۱۴۰۱، سهم خودروهای خارجی دوباره بالا آمده، اما حتی در سال ۱۴۰۴ نیز تنها حدود ۷ درصد تولید داخلی بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/686877" target="_blank">📅 14:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16fdb5f91c.mp4?token=uw70VHWr_qOBFDeLJrkXIrrLhc57p5feJE5h34u0UYbycMKiyVfJCZE8icgPYrRGhzeT80_l1V2hwk8akrT_ru4b2wi1y_VtP8qs4SG6GGuT9icIFRzSUlfcrphwmB8bt128Ramth9IFoup_MqAfYPhLn3TZQR0lUkdh3Cr4XtQEDIxkw6QRqUCS14SspzhP9tnWufRLzn4NwYPIvcuPryg1BFlNkzjerrg4c7AhNc_Q_pn9cf14NYS6njFYfdzu2YYVy_k8BGxOslerKWyzTM70jJW25lm7X1cMUpWULjWaij1mzuj0v6x8aR9d5b7_-aycVK4LjpxnOEHZKeiF5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16fdb5f91c.mp4?token=uw70VHWr_qOBFDeLJrkXIrrLhc57p5feJE5h34u0UYbycMKiyVfJCZE8icgPYrRGhzeT80_l1V2hwk8akrT_ru4b2wi1y_VtP8qs4SG6GGuT9icIFRzSUlfcrphwmB8bt128Ramth9IFoup_MqAfYPhLn3TZQR0lUkdh3Cr4XtQEDIxkw6QRqUCS14SspzhP9tnWufRLzn4NwYPIvcuPryg1BFlNkzjerrg4c7AhNc_Q_pn9cf14NYS6njFYfdzu2YYVy_k8BGxOslerKWyzTM70jJW25lm7X1cMUpWULjWaij1mzuj0v6x8aR9d5b7_-aycVK4LjpxnOEHZKeiF5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این مدل گره کلی دست‌بندکشی بساز و با هر رنگ لباس استایل کن #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686876" target="_blank">📅 14:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/903a5fe07e.mp4?token=HVY-weeqkyvPNS6Q8ohOtPdJ4BrpC4llpFKw4AevaALOZhlKcu2qyIafDdeHMH87MSrkVLgunyrEwiwL0p8t4wEK-e3NN7owZWeuB3DsyQJvrfs5-1CW9jvR6b0iQYDNRzGa4vaH48J_SRHSmKaTUuNCZTH1NMSR9IxOI4hf4eVKZpEDvCMc2bipL7F-sQRnyFzbpAeLZPpp4a1R-Ex_zrPEzDAnRVrSu2Qubcb8TE2_3sQWNEZhOrFEwY05hzEvvxa8R4rwStHWI89d63GmeSTxw5JCu4iB0k_9sHIMHunm6vPvWzfoWn5Z4GFs-reSG5jZ6CRKLTeUwScIakQozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/903a5fe07e.mp4?token=HVY-weeqkyvPNS6Q8ohOtPdJ4BrpC4llpFKw4AevaALOZhlKcu2qyIafDdeHMH87MSrkVLgunyrEwiwL0p8t4wEK-e3NN7owZWeuB3DsyQJvrfs5-1CW9jvR6b0iQYDNRzGa4vaH48J_SRHSmKaTUuNCZTH1NMSR9IxOI4hf4eVKZpEDvCMc2bipL7F-sQRnyFzbpAeLZPpp4a1R-Ex_zrPEzDAnRVrSu2Qubcb8TE2_3sQWNEZhOrFEwY05hzEvvxa8R4rwStHWI89d63GmeSTxw5JCu4iB0k_9sHIMHunm6vPvWzfoWn5Z4GFs-reSG5jZ6CRKLTeUwScIakQozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکثر مجروحان حادثه سیریک از بیمارستان ترخیص شدند؛ ۱۱ مجروح حادثه سیریک همچنان تحت درمان هستند  رئیس بیمارستان میناب:
🔹
در پی اصابت به یک مراسم عروسی در سیریک، تیم مدیریتی و کادر درمان بیمارستان میناب بلافاصله به حالت آماده‌باش درآمدند و پذیرش مجروحان آغاز…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686875" target="_blank">📅 14:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt9q2V03pNQ752xOxlGf8ca3FZ7VQa6qRDB1khpcvh4Qc3jXs7sJtUF0bvKu2xt1iz-tTo73zNdo_QFIcQKQQNWvyWXGcOFbGqvZLTNtDLQWtsbNyPly0YmcJjE_0kcnTe1Jhzu-ES8It6S30yHbF2p3WxbzdOOOxARSAB4jsNMGWCYYQbuNOvFZQQVGU4vhsgBLWgPqotXgog5KZKt4nDHnFM4xDvuDMxXvt4xsax6QRuSOMQ-YPvLktCEWmyqvFG5p3wqhcNJawLMhWkqeJRKLqoLIAimM1u90Toenirn2WvD2eSElj0S3CMpngyVmlxlhB91gBKMMUAYsRxb8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: رئیس جمهور ترامپ به طور مخفیانه در حال بررسی امکان اعلام پایان جنگ با ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/686874" target="_blank">📅 13:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVxRUVkXvTpADUIYWT6oVPOpz24IiCjBjy7IeX47p2j-bq4k5_99WueWQKPAF-wjx21tRiMwp20k3Ht_8bz1del3h1sNHPtVI5IHTNNIALwsbPgIhk4lWZbTsUx8_f7aFhi8Cd6WKiFKnU_ZoAyib2pnjxXKtwddVokmfTdk2p3poRM0KHCxaYMFRyBq7eDJJgKBsxCzmI2lCr5BmlpR-03tu1_GhLKkaDqDdPNUUZ7fOMty3zM79qZx08RqjFCacgJGa8v9ZNa9EURqtB8Ec_EjAeAlZrA-ZUxj79jry41Y_TDT7tjiSS_9AK8zXa69QyPhz7E0ERHtnqPL8nhiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت ۹۷ دلار شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/686873" target="_blank">📅 13:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارشناس حوزه نفت: نفت گران، کاهش صادرات ایران را جبران می‌کند
سید حمید حسینی، سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی در
#گفتگو
با خبرفوری:
🔹
با وجود کاهش حجم صادرات نفت، درآمد ارزی پیش‌بینی‌شده در بودجه امسال قابل تحقق است چراکه قیمت نفت در بودجه ۵۴ یورو در نظر گرفته شده است.
🔹
اکنون نفت ایران تا حدود ۹۰ دلار به فروش می‌رسد و افزایش قیمت هر بشکه می‌تواند کاهش حجم صادرات را از نظر ارزش جبران کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686872" target="_blank">📅 13:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651396028d.mp4?token=qM_iI-4ajcjCbjwwBXg1A-sPZPCp3bG4zOu-yk4WOLwG2MY18dGYUk1tozgTe_ir2QWWEulWmk-gkYcNw9qwxwKBlvXRBr5mZ5GY3cWG6f3ND37BVgLTkUokQ8o3xSRs7vnOC2q_OAA2ca2LMmz9rvT2fRXE6gvNUXs_yh3SyotXEMfazyqm1RtMjZa6Ty4Oe-2FM6BAa7_VwbMgylpbNfnFY4YIBM4nRQFvRK7xbMPm0R1Nvyabe9l4eOMhAcGnhHdpb4DaoaYz-IaIlG0Ci1synP3qOtEvsiLywXqS5FAeFJT5qt2husv__v3YwTaDSlTETjJY2KTc2ZFMvePBzktbbqHXdhAmdqFddVjrVZ8DV12Z24WNbLKehD8-_ainrYWGGy-1gwyGhjXUDU5BaU3vOoXg3iqVdn1uwDbRMwcx9WtlZvM1Of5hM5QIDaCBlX4AE_w14tJncVddUqDKISrNPblyBo8MjlbrQEVlNLtvvzib69vKy9t-GW7suAhXIAsQbvtITW1HrtUSf5msQ4SKU43jT6mSCVlSmRgD8FbO_jlPAjnn19rbgBCmVrE0UKTs8aI9iNfMZsH9ueachvh--Q0eKxusbDgakp_1Ut8Pep1mZTvkz5QkUMf-WVh7tysxhygOF1OPNODy4LwzyFYEwne-XpAr0QFvjORAjWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651396028d.mp4?token=qM_iI-4ajcjCbjwwBXg1A-sPZPCp3bG4zOu-yk4WOLwG2MY18dGYUk1tozgTe_ir2QWWEulWmk-gkYcNw9qwxwKBlvXRBr5mZ5GY3cWG6f3ND37BVgLTkUokQ8o3xSRs7vnOC2q_OAA2ca2LMmz9rvT2fRXE6gvNUXs_yh3SyotXEMfazyqm1RtMjZa6Ty4Oe-2FM6BAa7_VwbMgylpbNfnFY4YIBM4nRQFvRK7xbMPm0R1Nvyabe9l4eOMhAcGnhHdpb4DaoaYz-IaIlG0Ci1synP3qOtEvsiLywXqS5FAeFJT5qt2husv__v3YwTaDSlTETjJY2KTc2ZFMvePBzktbbqHXdhAmdqFddVjrVZ8DV12Z24WNbLKehD8-_ainrYWGGy-1gwyGhjXUDU5BaU3vOoXg3iqVdn1uwDbRMwcx9WtlZvM1Of5hM5QIDaCBlX4AE_w14tJncVddUqDKISrNPblyBo8MjlbrQEVlNLtvvzib69vKy9t-GW7suAhXIAsQbvtITW1HrtUSf5msQ4SKU43jT6mSCVlSmRgD8FbO_jlPAjnn19rbgBCmVrE0UKTs8aI9iNfMZsH9ueachvh--Q0eKxusbDgakp_1Ut8Pep1mZTvkz5QkUMf-WVh7tysxhygOF1OPNODy4LwzyFYEwne-XpAr0QFvjORAjWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش بابک زنجانی به اتهام جهش قیمت دلار: برایم پرونده ساختند!
🔹
بابک زنجانی در حاشیه نمایشگاه الکامپ و در ادامه نشست خبری پرحاشیه‌اش، به ماجرای پیش‌بینی‌های گذشته خود درباره قیمت ارز اشاره کرد و به تیتر تجارت گفت:
🔹
«برای من پرونده درست کردند و گفتند تو چرا گفتی دلار می‌شود ۱۵۰ هزار تومان؟ چون تو گفتی رفت بالا! من گفتم کشوری که قرار باشد با حرف من اقتصادش خراب شود، بگذارید خراب شود! اقتصاد نباید دستوری باشد!»
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/686871" target="_blank">📅 13:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ: از موشک‌های ایران تعجب کردم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686869" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpRBYtb1uJNkZLw0RlTq5nWDFd9uDBAiE9o15-OsAr3Qcr6O6zEmryDk8jJ3xjYZpnjmAFQ03_HSgie4IPNDkYjCqbahEb0olFVQmZzB-SISUZRsx_NpDbNlTP78iGcyYCcrWnFUPFhqGRWXl_r4lrnZGzjI0L5pncqkZClyxps1QGGmV0OnGTyUF8LsLsMz1P4B8S8i0SBtzy_BsQvzjAp2KIqSb8yuGZpp8HZKlUYBQtCFJUJf2P90HWcOOnvXDcv_6TToEJQRBthCULWphRkVo_jfQYwNAPpyo1DI5WraGdYcSNt4NXKklDg_uJG8A_fSXQm1jtpix--yCtKiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۲ شهریور ۱۴۰۵؛ ساعت ۱۳:۰۰
🔹
رکورد تاریخی در بازار طلا؛ هر گرم طلای ۱۸ عیار امروز با جهش قیمت نسبت به دیروز، به ۲۳ میلیون و ۳۸۵ هزار تومان رسید و بالاترین سقف قیمتی سال جاری را ثبت کرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/686868" target="_blank">📅 13:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: رانندگان و مردم را در جریان اصلاح الگوی مصرف قرار دهید
.
🔹
دبیرکل نجباء: اگر نیروهای آمریکایی پس از ۳۰ سپتامبر در عراق بمانند، آنهارا سالم نمی‌گذاریم.
🔹
نان سنگک در فهرست میراث ناملموس ایران ثبت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/686867" target="_blank">📅 13:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686864">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058b000ccf.mp4?token=jaZt4MxQIiPE0uldGAk77V1W4LP_7MXCCi-7V2OU72HiAeivolMSrnsiboy2UkMY7nDQ6teyuUhr7Nbm-Lq9GxMeSWHH0JbWjq6lvZpt-0v-1BG2y1d2cUyQW22PdJXJqCF5Vf0nGJumV_k0snKZlgOoeF_Q9Jhk_VVrQt2UJ4U6GX-Q49kqFtKakDlIH7OfpXO2MpEgpca69vnHvTe7Zi4gqDXoqV3hnmlMmB3xPNm4j5x6YAJ3RwGB2VZF51ot2kPAwLEksuWKvRj0FK71Fe4_i-MfjNJbP9H2Bz2HWOxxR_huH-4jC3JaltBjaHbAFagIKCh0g4NeKp7JmWY2OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058b000ccf.mp4?token=jaZt4MxQIiPE0uldGAk77V1W4LP_7MXCCi-7V2OU72HiAeivolMSrnsiboy2UkMY7nDQ6teyuUhr7Nbm-Lq9GxMeSWHH0JbWjq6lvZpt-0v-1BG2y1d2cUyQW22PdJXJqCF5Vf0nGJumV_k0snKZlgOoeF_Q9Jhk_VVrQt2UJ4U6GX-Q49kqFtKakDlIH7OfpXO2MpEgpca69vnHvTe7Zi4gqDXoqV3hnmlMmB3xPNm4j5x6YAJ3RwGB2VZF51ot2kPAwLEksuWKvRj0FK71Fe4_i-MfjNJbP9H2Bz2HWOxxR_huH-4jC3JaltBjaHbAFagIKCh0g4NeKp7JmWY2OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض هزاران نفر در اسپانیا علیه بحران مهاجرت
🔹
هزاران نفر در اعتراضاتی که تقریباً در ۲۶۰ شهر اسپانیا انجام شد، شرکت کردند و خواستار اقدام دولت «پدرو سانچز» برای مقابله با مهاجرت غیرقانونی، پس از هجوم گسترده مهاجران به سئوتا، شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/686864" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنگ ایران انتخابات آمریکا را از ترامپ می‌گیرد؟
🔹
همه می‌گویند که ادامه جنگ آمریکا با ایران باعث می‌شود که ترامپ و جمهوری‌خواهان در حساس‌ترین انتخابات پیش‎رو ببازند!
🔹
این فرضیه تا چه حدی درست است؟ واقعیت‌ها چه می‌گوید؟
🔹
در این ویدئو آخرین وضعیت انتخابات میان‌دوره ‌آمریکا را بررسی کرده‌ایم تا ببینیم که جنگ ایران می‌تواند دار و دسته ترامپ را پایین بکشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686863" target="_blank">📅 13:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSx8AdcFjB0mnE2vFmykGKID41ECMNwXZOObmiPC9avN6Yro5OfvGS_FVm9vlDdhmPiGpG67Jf-qD-SwK8zdPdkJTzIVp-iL9C30hBpRlsmgTyjUOSiSaKrw0SUhwK4yyokb3QaxorqPz0-JQtVjbeIG43uVQDjUgNydloSaAvGHnmIn0hNf0CBgUxhgjjafhHrlTOiYxrjYHKV9lWm1m0vWkElbLLA9n7ZdJY4UdAInuhQB2NGVBxyS2e9noZFUYma4cScVIXqiuv6YqW3_0v4xAd4FQA9CJ4TD79DksOenT8ulaitGneKIr5Kzm3IINtHjTWjlZYyxrldNjRFKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موبایل‌های میان‌رده از مرز ۱۰۰ میلیون تومان گذشتند
🔹
طی دو هفته اخیر گوشی‌های میان‌رده و اقتصادی به شدت گران شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686862" target="_blank">📅 13:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686861">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
واکنش سازمان ملل به حمله آمریکا به مراسم عروسی در سیریک ایران  سخنگوی دبیرکل سازمان ملل:
🔹
دبیرکل سازمان ملل عمیقا از گزارش‌های مربوط به تلفات غیرنظامیان از جمله حمله‌ای که گفته می‌شود به یک مراسم عروسی در ایران اصابت کرده، نگران است و خواستار توقف فوری خصومت‌ها…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686861" target="_blank">📅 13:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رویترز: ایران به آمریکا درباره حمله اسرائیل به تپه «علی‌الطاهر» هشدار داد
🔹
ایران از طریق عمان به آمریکا هشدار داده در صورت حمله اسرائیل به این منطقه در جنوب لبنان، با شدت پاسخ خواهد داد؛ منابع رویترز می‌گویند فشار آمریکا باعث تعویق عملیات اسرائیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/686860" target="_blank">📅 13:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686859">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaCXQQGmWXAvyLWRBVf1uQ7HkULpPOyLFq1pGTvKOYZbUOEVCR0WmBxy-BNkjMSnWgr_14Yn9XhYeR86TKEsfI83vnRYDhoOQS0rt5l0j83xlB28NVHrj2CsJHNWG1LDiE9QImVKZ0ehJv-GwB4xs58U209HsDOy8iGVYwlZWkurmr5OATcFy6KSmjbVUsgRAXrO5tqvWXsJp68k2KeqzoAnlPaUJ1wCwMDrs7jEJsDmCyC-h741hd1Vb4n5HHzbgStmkSERNkUGgpfdeSxL4Qam5rQ9tlueTkYC7LQ_n2hP9OYCp1IzNez0PUbfr7iFD2gVA7A3iRVRsWPpuWFyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه ۷۰ میلیارد پوندی جنگ ایران برای خانوارهای بریتانیایی
🔹
اختلال در تنگه هرمز تا پایان ۲۰۲۷، به‌طور متوسط ۲۴۰۰ پوند از درآمد واقعی هر خانوار بریتانیایی کم می‌کند.
🔹
مجموع کاهش درآمد قابل‌تصرف خانوارهای بریتانیا به ۷۰.۴ میلیارد پوند می‌رسد؛ افزایش هزینه انرژی و تورم عوامل اصلی این شوک هستند.
@amarfact</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686859" target="_blank">📅 13:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686858">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsNW3NMXdXhb8oWxQ3vEuDU3dyOp-UyyNFKAq6-wuFILlAwtH9bGxRz6utW3fEuHHXP6n4E9KtTOIieuD9fOGv6OOWDK2nH9k53GvHquSgLjXyiLmX0c8nJUu3JcP1WHjzS41jCrfER8OIsyyvSEJqFibxBmzSrIu4UbmaBH4vAE9iNg8N0848FLoTHKLgTOeiIYwjRUFSqr0zP7dWNiqoMZKXwjXLZnkS_aPcXML-gslAQLgTZwnbMRZeAdp-oX8J9hxTlIpypY6gJ9DZJqN_9w9pzCEuQlIu3bXTQ859EPASBsPpS_VzPt5sR6HFqBM74oDbSc2uaY1aUFovgB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: بمبی که در کوهستک با اصابت به منطقه مسکونی، عروسی را به فاجعه تبدیل کرد، ساخت آمریکا بوده است
🔹
بنا بر اظهارات یک کارشناس تسلیحات و تحلیل تصویری «نیویورک تایمز»، بمبی که به این منطقه مسکونی اصابت کرد، ساخت آمریکا بوده است.
🔹
تایمز ویدیوهای…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686858" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686857">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
مخالفت قاطع چین با تحریم‌های مرتبط با ایران
گلوبال تایمز:
🔹
وزارت بازرگانی چین به طور قاطع مخالفت خود را با تحریم‌های مرتبط با ایران اعلام کرد و از آمریکا خواست تا رویه‌های نادرست خود را در این زمینه اصلاح کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/686857" target="_blank">📅 12:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
استقرار نیروهای آمریکایی در خاورمیانه را تا سال ۲۰۲۷ تمدید شد
ادعای جروزالم‌پست:
🔹
پنتاگون استقرار نیروها در خاورمیانه را تا سال ۲۰۲۷ تمدید کرد.
🔹
منابع گفتند که حضور نظامی با هدف حفظ توانایی دونالد ترامپ، برای انتخاب بین فشار اقتصادی مداوم، عملیات نظامی محدود و تشدید گسترده‌تر تنش‌ها است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686856" target="_blank">📅 12:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686846">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bO5A5d0wB_RTaduRlKGzzyx3AYrNzg58zRnmNMP3JDtmCTd4Ab03SIkXZdoNuiT9rC0daEjOm8tS5WJDj-3L_oXCMhRUzYPXIzS8z9AaxS0mFsUw0A65W0V96yEObA5x3MWEQ7AKcplZwbh9diY-ikNGdR8cPrcTqcTFvH5VrUPZl8RntPlYbNlix33mNL1ewjHHggPg9daT9cLslIkAejDIji7tMueGl-OZNUCl-koS6vjSuVz7dKnHaJQ6_-KVqkLdeCY67PDqTbgU0WbLPTX_FCCM2Ln4i04yiTEfTy6B9PxRtRBjYm2P1bc6LJQhtyu1IDKTN3YvIVRvkwdGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lM4t4pD12XPBK2Uk3KQ7gWRV3jWtAyMVOtaJUUfO3WnhGHrWHtbm7ChPALuh58PcDA0k0imF6OlqbAAEA2nIZFEa9fke6_0gZOQq5dpqjYfkeGjCZWcwhgmi1gbJ68qSyTZJOylTCjOM8lj-n5sKkA61m5mBbHQOKOFnYGFjlDRO5nDLOoMqMljs7Ze5bZwMaAsgKArMFO7afnfxoIPy6EXj7nuKI_A_9BuYwJlxumIjkkcYtPp3wwzJ3mLwbe-pNU7RG5agmh0a5anXxnoWaeh7G3naOJGrYB23P7uuUadm9hNhpfp6c35cxDHuPavASSKh1f_zkHwQlzFQHPpk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXnNPdwILQLEpbuhh3abrxw6GOD35sL5nBCp73YXbaZ3LZtJ75qAddcE0QMBhLmAoizEmEYLTJ-xLHR-eltZ4_n-FzESu60a_uOTs5wQYPXUrFZdfFAu4TM1vNYjY-aFfVTlhmR-8-xqPrs-UoEK04nCpNknjZlQp2l0GP93eTPMZ_EZPF0C1iw2s7u9d8MKbCGGH55AfaHaj7WVXdBlaJx3dfoxhzfGBvNKESOvIuB653jlSmbxsPDaxo6qQv-WsMVzCXyybeb0S1pQNMsvuuir2JuazbByyoekkL0uoKyHLxPKb5p-3gaGxcHs0D4OXV0fu2Xmn3RJ6O-3G_hhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmaCw-lyHoPi3gQjIykt0Wsm4OfzCC_0zXnMJpvxu1t5rRYVOm8CN0Qxffc9vbOHFBVqPYXNOPLeDZFGb16iVdvTtE07AHyND1p-H_kKVcOtWrlJ4gPJ8c5u2sEEZaYtU71oRAxtLVlOhlddE1DPxsrnFrw-N2TKqj-5XaZE5IRPMh-JSWamatvHqLkOcVCZn7k8XITThcBWHES23Y_nZ4E0TTc1W9JW6uq7yrGiM-m6tji5vESAOnM2FgCaX9UWg4n0Vg3l2598ZBv4z2M9Jpw_u7tkhjJWVuVYj0aCJg58c2O0VrjwUkh-VmbHWwdoq-8yFsVpl0gP9HY9ZgCECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_s6e9mcfJZt0FD9nHutIb2Kj2xKABcWTsO3yq1G7tzJAYRaVEfwoQktvsXx237O-Q0HwggkznAyvWqQu8E-uP4qTDggObmifqawccvD8Dg-3I4DtpnuaazyVQJwVEQw8cw9FxpPXx_Vpva65gh0Ol-gL4TpMHr-bryufZ5MTkgAQAs9tv1CJ24vVFp4r7Hzk4jurk1NDMe0W9mzyhf7kvDJWrTq1Gw8RgjHIhPz22wXYQ7jDuvL5fNLarunFdwODFm9x5Hw_1U7IQxvEsg46kU4g2q1GALSEwJs4faP5UmJMNxT6ilP-FthG3cToEkDwA7gMpbge1198JsXAYJfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAY41mUBcqUCTS2NN3iSwG499zIpmrUtT_M8ropq1st_LbIBdnYYUb6cD0WFZfunUTKkmlhTAy8nfUNPGHtmgFdMvSc7FDUbDpRVPC8KhvDTx47-ojMCZppgOMZZStynq2HD-Dy1lIHlf7s7Ps6iNoY20NEisFQ44B5rkp46cp8Na9MuVi89kzRmLqgmf08GCeKmUA_GEyl0tAnjjx3wNsWJ0t7oe6D3kSVPdjbytXT6TC1EKE9fvZLHcSh38e24vWLP6taQTCjji-oS6dRcUtXJSBUGQPIikGtk33YBpyo_r5t5W0r2aY3sHWHPaXbQbMMaxV1udOCrlTK_0zSEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBE57tMzzsUnRbMNGDzeXJBb2lutld9UiBc2xqx1y2tz3oMpfMX5fg2tXx8fh925_bFt33Mg-FTsPDmJqvLpM2LCfEU_3R0jqdaMu_akVFuY_M5Xzk07qH6D4uqvfiMiUSamb1iwlA3E8CU1DEoSk5EC-g1WkzGElUfsxsGc1u3oBEgKxKIGYdan44P5AKC_h0MD1MhTvk9tCJxM7kEwsDnwDAeF3Zc648qR0QDp8q4tiJT8dZ-br2c2ix48nvFU-rLC_4Ca0hAaC79bHZCN_vIPQ0wQgoFQr2HAFyUF-6DUfn4izPokUuu3qprfhSFdMKNzn2EQuJUMGag7n4T4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFoGBEjnCV4ypUTY0MQtdjXLNYfZ2zWslooLxxchVwpjvGQEcry8k2p66u0Oy47euABrzx6qfDUwRUR7FehpmuDhzOl9d05AzNus7ZA1EBIcHdHgwTwxgI_HBb0a9rulsGLWFkLC8A6HjexjF1ACgkT5mBfLmZvKT9DK_zqcNdxxTGqX4NA5PSVPqu3wO4Jal9vsJdihAPi1Jj8deltdVJ3XeA06oki06t6iMmueAuUvMZH9lBjQXiq8qlHi3adxsTbG1Gvsq5-uq2HG72jF23MAxqJVSm3qWMpGEPutFciwHwHUZmmmFYmFw20mPrSptd8AQZWb7YC-OngOvwQWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0Yu_aTOa3OeReNoZjtc33EjzdAizEZiAVnQHfXWZnn1sXKuRG3iOpLyLa4ffYKt9iazdH8dA8lycGzJluNq4-WV79_eIBG3ENFEwk6PujfT9-7Vo16pLQ-rEAvfxx7Y3TdKCobNHMmAmwJRI_O5p54tiNJJgmTuMtvzEZijzSUVVmqx5MDgvTognP5AqPtFKkWwvOsyEZNVQaEJaPThKhZK5iq_3JQEQGx3iC4zAGFup6JfB7C9Fem5JiyUitzVGAFxIWuku1SyJIACopz8f3slmMeBM2qJnkYk3-mm27LQGachxi1tUgdu-feUTIEQkNYd5e0PqDoobgpGisBFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUBE_P0VPdTezlck4kfs1t9Skms_ntZpoDFYY2ysgYDHCejd-FDymSK8Rnd0ZSoT6lhdrisEi__emjzk898e-5ir_462OKtgpKfcwZ-ltepTsSh9jpdCr12Kmc0XqKg_sp05DWvrU9o6XPXMrP9j_eqI2SW48iLx1vQNGvf4wWGSQZllW764fiY34Qz3we65kNZ3QvcLskfZHySbdH6JfkkzsqTkeQEwz6Ne1ZzIEeJ38uUNzh3qzLA2U-sslbuLGFAI6j4nik-kzVjETuqAWfGfxeVBUpX4ip4hJv_uskUavNc57NPyL80R7MCGDcqJaI1NzPLAvQau8G2K-IWW4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در #چرخ_زندگی سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/686846" target="_blank">📅 12:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686845">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0d184e42b.mp4?token=vsQrgY0ge2rb8MJ87yID5LZMfLGTTbHaCKDfXCmdx3b1UAzfqQRgmUgHM1jzsJg516w0PWLgEFR_OWBsVlHB1zPOjgzPOtfUFgvC5fl679eTPi53LoMeWbrBQ03hTS1DbEUiHA71ya2zt1HnH85PSIW6b981YcJriiCtmPcraTidmk6gwjJCM9IZ57Q9mzFMnQr44mWdv4249E5CL4OFTBaBEP8ch3xMgONbOpg8s6I601wrZKCg8grCOUx9LvTJ8I3ht5Aft3OXtotpE4WlrYSsE2Ne6icZDmVExyxMidcp48i3Sl6qxg5KuQ-uhlX8WaHTLvkzLljrwM3sT6FGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0d184e42b.mp4?token=vsQrgY0ge2rb8MJ87yID5LZMfLGTTbHaCKDfXCmdx3b1UAzfqQRgmUgHM1jzsJg516w0PWLgEFR_OWBsVlHB1zPOjgzPOtfUFgvC5fl679eTPi53LoMeWbrBQ03hTS1DbEUiHA71ya2zt1HnH85PSIW6b981YcJriiCtmPcraTidmk6gwjJCM9IZ57Q9mzFMnQr44mWdv4249E5CL4OFTBaBEP8ch3xMgONbOpg8s6I601wrZKCg8grCOUx9LvTJ8I3ht5Aft3OXtotpE4WlrYSsE2Ne6icZDmVExyxMidcp48i3Sl6qxg5KuQ-uhlX8WaHTLvkzLljrwM3sT6FGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غذای رژیمی و سیرکننده برای دوران کاهش وزن
🔹
این غذای خوشمزه با ترکیب ادویه‌هایی مثل نمک، فلفل سیاه، زیره، گشنیز، پاپریکا و آویشن، گزینه‌ای مناسب برای رژیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/686845" target="_blank">📅 12:35 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
