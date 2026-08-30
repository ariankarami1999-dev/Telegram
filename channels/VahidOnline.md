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
<img src="https://cdn1.telesco.pe/file/WWswQihvvBkkjUsb64QnMSDQVdnMbymAo0hjsfRJyS_ekB4PWf4kEYD0QxwaOuqhlX8QpUWX8-G0yZNtnOoKDTazmEzUQCVD1cfkfpPvBxwmRyIuyqHIS9gW1mYHKvzHhoZkZ_syFECJBVjLejgTuGadhMOqXcg7FIqfcLOe4lFveOwJvfR5IOgccTOw9L_Cp2mtYYLohGs8eAt1y-cmOruRzO0NIYIJp5Gg3h0a_bMS5JHs3NN0WLuB8FnztECDdrjbkMwUijGaBpveyuGNY7iQuAi7qaR1RSRTRlK3lzKjzyF5e2iPAwt_Xe3MhzVhV7wFnoaiXBtIXpyVkUyZhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OFf9UF5TepvcQp2RFwlZJxB2NdipzF-Uv028ojqDanmWT-ohMDK23h7jECGsm0cqWJSsYYo1CFRbv1E7PDH1XuL-fCWxfT5cI2UcqyhxZMVKsPFx6f9vCeXXSrKrFdj5eHnkrxMjnG40m8o3h1v8gDOv7SUW1J1PMRjWAoqfVMOBDOL-dombBqd1YlZXmkeKU2_S01asA6Nid-kf7205_OFOyXWJobIYuwr9WjysWTikcm7dBjEV_ShhOrf1g6ZY4Zq7H1PtuIH9RGHlahv1xUeYZ4fOGYQaTEO2F0CRSJG-sXaQ5rmXTEA5e87FV-Lz0hAaQytRGoVZpzbnrTWhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه با تایید کشته‌شدن شماری از نیروهایش در حمله آمریکا به لارک: پاسخ خواهیم داد
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
🔹
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.
پیش‌تر یک مقام آمریکایی اعلام کرده بود که دو پرتابگر سپاه پاسداران که آماده شلیک به کشتی‌ها بودند در جزیره لارک هدف قرار گرفتند: @
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/78091" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/78089" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZmHRNwP6G_9hkmYQz4eJ3P7uH-cGToapEa74T85qBfckTK65h7bKzztD74FaBWKV_aDvvv7h2s7I7-pyckF1L3eQ-G0PWRTnwg9bzBWewSo-ZoY86WJcNJQkapSEhsAwLeVOoVGnnjDspwpCDkf3RPIRg0n_3WF-XngOzfxZtQPQlgWnBQnkrnjZjzZXpJjMfoLp4Kh5IVb06640s0WgQwkd-WUdGpFMl2NQBgnYkWVTYaTuKWv2cP50ePH8OKK_tx4Vs1KaVBWHMBIPU-3LPmvFmSkC5ykLoFZwhLpblWtI_uPoD3nzoXPkEn84zhVkozeLJ25m8ELcHI_0fVm0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
یکی از کارهایی که قرار است با نفت ونزوئلا انجام دهم، پر کردن ذخایر راهبردی ملی است؛ ذخایری که به‌خاطر جو بایدنِ خواب‌آلود عملاً خالی شده‌اند. روند «پر کردن تا ظرفیت کامل» به‌زودی آغاز خواهد شد و این هدیه‌ای از سوی ونزوئلا به مردم ایالات متحده است. متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78088" target="_blank">📅 17:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBn-E3sdk_ceGjqJ6iXpcAbj0TKlDa68pkYUWI0-2EMRl79GNN6El5yN9yoprJoR-8pSAuR4FEWF7Q0Bfc68bwUkiMbbUWZi0g5I2x9sVp_X0EcwjU6UnHlMU4inpFg7NOzhuaOInDT8D3dT89KrS1ZYfvKXfO9u7znxNONqAzMOlLwwcPv2pA0LXiJVp_NYT8WkZKuJD5sAa7lIEDxxvIrDbdHdoNpTo8KSBjpep4C2akIcR6jK6edYXuCVPrrAGyBfi4OvEgcLLUo2fecRd39Ns3z7I1IuWX5jgxciTpdX4Hv59DzMlRPDwpPrw05Fo8w7aOPHjuJxSd09qFtXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن‌پست به نقل از افراد آگاه گزارش داد چند مقام ارشد نظامی آمریکا به پیت هگست، وزیر جنگ آمریکا، هشدار داده‌اند که ادامه عملیات نظامی گسترده علیه جمهوری اسلامی پایدار نیست و توان ارتش آمریکا را برای مقابله با تهدیدهای دیگر، از جمله دفاع از خاک آمریکا، تضعیف می‌کند.
به گفته این افراد، این هشدارها که روسای ارتش، نیروی دریایی و نیروی هوایی آمریکا، همراه با فرماندهان چهارستاره مسئول عملیات نظامی آمریکا در اروپا، آسیا و آمریکای لاتین، در نسخه ۲۳ مرداد «کتاب دستورات وزیر جنگ» به هگست ارائه کرده‌اند، بخشی از یک سند محرمانه است.
بر اساس این گزارش، با توجه به تاکید ترامپ بر اینکه گزینه نظامی همچنان روی میز است، ستاد فرماندهی مرکزی آمریکا (سنتکام)، که مسئول اداره جنگ با جمهوری اسلامی است، ماه‌هاست بیش از ۵۰ هزار نیرو را در حالت آماده‌باش نگه داشته تا در صورت صدور دستور حملات بیشتر از سوی رییس‌جمهوری وارد عمل شوند.
به گفته افراد آگاه، نسخه ۲۳ مرداد کتاب دستورات وزیر جنگ مقرر کرده است که بخشی از نیروهای مستقر در خاورمیانه تا پایان سپتامبر در منطقه باقی بمانند و ماموریت برخی دیگر تا سال ۲۰۲۷ تمدید شود. احتمال تمدید بیشتر این استقرارها باعث شد فرماندهان نظامی نگرانی‌های خود را آشکارا مطرح کنند.
به گفته این منابع، فرماندهان ارشد فرماندهی اروپا، فرماندهی اقیانوس آرام و فرماندهی جنوبی آمریکا، همراه با فرمانده ارشد نیروی دریایی، در این سند نظر «عدم موافقت» ثبت کرده‌اند؛ به این معنا که با دستور وزیر جنگ برای تمدید استقرار نیروهایشان موافق نیستند، اما آن را اجرا خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78087" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVY7c8hzy-7GKo5FRc2F3UbdmO53TfcdGZD5IG8Zf2Na7sI6H733Fc8CMzmX0yhcB8JV8CHKDas4LPS85BKAXMKmaByHSD1wYcyCFkuW5l_q9ME15yk0ZxuOovFvmwLkExrywgnZNd9g_JIrQUHlQxtHyZEIAwPZpqlEaKCnQuaMn2iV0PAX-7CiriDH4QVh8tn-e2nUJ7J6ZxWwEbqdy7pynp-Rb9fZm9y0J3NFblJped6glwr2iG5Z86xoCdmwGzGr4NHacY7dDHXKbLpxB88b1O293RKD3j1LDDCg6x9OE7xHxukRKi7Wj3nV5trV3N0EAxPyomAn3Y6PpNKe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه اول دادگاه انقلاب اصفهان ۱۰ نفر از متهمان پرونده موسوم به «میدان شهدای اصفهان» را به اعدام محکوم کرده است. شش متهم دیگر این پرونده نیز احکام سنگین زندان گرفته‌اند.
کانال تلگرامی خبرنامه‌ها خبر داد این احکام در مرحله بدوی صادر شده‌اند: @
MahmoudianMehdi
«ترانه رحیمی»، «نوید الیاسی»، «ابوالفضل دادگستر»، «مهدی منصوری»، «احمدرضا سعیدی»، «مهرداد بو‌ئری»، «محمد مهدی اسدی»، «آرمین غلامی»، «پارسا جعفری» و «مهدی جعفری»، معروف به «مهدی خسروی»، ۱۰ متهمی هستند که حکم اعدام گرفته‌اند.
در بخش دیگری از حکم، «رومینا رحیمی» و «میلاد بو‌ئری» هرکدام به ۲۵ سال حبس و «حامد مهرعلیان» به ۱۵ سال زندان محکوم شده‌اند. «ستایش ساعدی»، «سجاد عابدی» و «علی بوئری» نیز هرکدام به پنج سال حبس محکوم شده‌اند.
دادگاه همچنین هر ۱۶ متهم را بابت اتهام «اجتماع و تبانی» به پنج سال، «تحریک» به پنج سال و «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم کرده است.
پرونده «میدان شهدای اصفهان» در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ تشکیل شده است.
متهمان این پرونده از ۱۴ بهمن تا ۲۴ اسفند همان سال در خانه‌هایشان بازداشت شدند. شماری از آن‌ها کارکنان فروشگاه‌های کفش و پوشاک در محدوده خیابان شهدا یا از بستگان صاحبان این فروشگاه‌ها هستند.
بیشتر متهمان این پرونده کمتر از ۲۳ سال دارند. ترانه و رومینا رحیمی، خواهران دوقلو، هنگام بازداشت ۱۹ ساله بودند.
جلسات رسیدگی به اتهام‌های این افراد از ۲۲ تیر ۱۴۰۵ در شعبه اول دادگاه انقلاب اصفهان آغاز شد. اتهام‌های آن‌ها «محاربه»، «معاونت در محاربه»، «تخریب اموال عمومی در حکم محاربه»، «اجتماع و تبانی» و «تبلیغ علیه نظام» اعلام شده بود.
این پرونده پس از کشته‌شدن «عباس کامرانی»، عضو سپاه پاسداران، و یک شهروند بی‌خانمان در اعتراضات ۱۸ دی تشکیل شد. بااین‌حال، در کیفرخواست صادر شده علیه متهمان، اتهام قتل مطرح نشده است.
منابع مطلع پیش‌تر گفته بودند در جلسات دادگاه مدرکی که نقش متهمان در کشته‌شدن این دو نفر را اثبات کند، ارائه نشده‌ و اعترافات گرفته‌شده در دوران بازجویی، مبنای طرح اتهام‌ها قرار گرفته است.
شماری از متهمان در دادگاه گفته‌اند اعترافات آن‌ها با ضرب‌وشتم، استفاده از شوکر و تهدید به تعرض جنسی گرفته شده است. «احمدرضا سعیدی» نیز در حضور قضات اعلام کرده بود که در دوران بازجویی شکنجه شده است.
براساس اطلاعات منتشرشده، یکی از زنان متهم این پرونده نیز از تعرض در زمان بازداشت خبر داده و شکایتی ثبت کرده است. بااین‌حال، دادگاه بدون رسیدگی به این شکایت، حکم او را صادر کرده است.
وکلای متهمان نیز از دسترسی کامل به پرونده محروم بوده‌اند. گزارش‌ها حاکی است دادگاه اجازه نداده است هر متهم از شمار قانونی وکلای مدافع برخوردار باشد.
«محمدرضا توکلی» و «مرتضی براتی»، قضات این پرونده، پیش‌تر نیز در پرونده‌های سیاسی و امنیتی اصفهان حکم اعدام صادر کرده‌اند. توکلی از قضات پرونده‌های «میدان علیخانی» و «توماج صالحی» بوده و براتی نیز در پرونده «خانه اصفهان» برای سه معترض حکم اعدام صادر کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78086" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvKoqScXsigxVXn3lsNvtAAOmx1sHp-hEYMfORF9Wz4FUAusDZJyM1uR00cd0KEUm-hT7pZWEKCIAOkdWEXg2AMllDlZYgMH36lXNTvq1sd_OXstzTxj81zpVjIVNCtMZgS82BC5pbRYshUeuczgeD1poMegAARnyVGL1VmlG1nAEt8jsbgDmbOofHlSEJBt2_6_DTipt7c-9HcCTMq6c8I0P0J5zMT9bFMH2mGGFVm_X1WSJqKljBlLPxABH3Cf4czFnPeSajmsXQskt-pPyXfMM69iCPhqIg2lfoR65HIXjUeVjayTN1v2jZn_9GvwCQ5HuT9JOEW-74vNF_yzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو اعلام کرد آزمون زبان این مؤسسه در ایران و برای دارندگان مدارک هویتی ایرانی در دسترس نیست. همزمان گزارش‌هایی از لغو آزمون تافل و عدم اعلام تاریخ‌های تازه برای برگزاری آن در ایران منتشر شده است.
این تحولات چند روز پس از تعلیق یکی از معافیت‌های تحریمی آمریکا در زمینهٔ خدمات آموزشی به ایرانیان رخ می‌دهد.
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک) روز دوم شهریور مجوز عمومی موسوم به «G» را که از سال ۲۰۱۴ برخی تبادلات دانشگاهی و ارائه خدمات آموزشی به ایرانیان را مجاز می‌کرد، برای مدت نامحدود به حالت تعلیق درآورد.
دولینگو، شرکت آمریکایی سازندهٔ اپلیکیشن آموزش زبان که آزمون آنلاین انگلیسی آن از سوی بسیاری از دانشگاه‌ها پذیرفته می‌شود، اکنون در صفحهٔ رسمی پشتیبانی خود اعلام کرده است که این آزمون در ایران و برای افرادی که از مدارک هویتی ایرانی استفاده می‌کنند، در دسترس نیست.
همزمان شماری از کاربران ایرانی در شبکه‌های اجتماعی تصاویری که به‌گفتهٔ آنان مربوط به از پیام‌های لغو آزمون تافل و نبود مرکز یا تاریخ آزمون در سامانه ثبت‌نام ETS (برگزارکنندهٔ آزمون تافل) است، منتشر کرده‌اند. رادیو فردا نمی‌تواند اصالت و منشأ این تصاویر را مستقلاً تأیید کند.
برخی داوطلبان نیز گفته‌اند آزمون‌های تافل تا همین روزهای اخیر در ایران برگزار می‌شده، اما پس از تصمیم تازه اوفک، پیام‌های لغو برای شماری از متقاضیان ارسال شده است.
تا زمان انتشار این گزارش، مؤسسهٔ برگزارکنندهٔ آزمون تافل اطلاعیه‌ای رسمی دربارهٔ توقف برگزاری این آزمون در ایران منتشر نکرده است.
در وب‌سایت این مؤسسه، ایران همچنان در فهرست کشورهای محل ارائهٔ آزمون اینترنتی تافل قرار دارد و اطلاعات تماس ویژهٔ متقاضیان ایرانی نیز در آن دیده می‌شود.
از این رو، هنوز مشخص نیست محدودیت‌های گزارش‌شده چه دامنه‌ای دارند و آیا مستقیماً ناشی از تصمیم اوفک هستند یا نه.
مجوز عمومی G که اوفک در مارس ۲۰۱۴ صادر کرد، از جمله به دانشگاه‌های معتبر آمریکایی اجازه می‌داد با دانشگاه‌های ایران برنامه‌های تبادل دانشگاهی داشته باشند و برخی خدمات آموزشی را به دانشجویان ایرانی ارائه کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78085" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uHmxaKX37bjPk5xmapHMQS71MxVulAG6ZqeNuOGhe4xGHeMiaZVzkHhcCSMir348FeN5M9fNtMsiE35cboD9jQ-NvZXCXR19zEnWxtThULdtj42-NLK9Hptc-e30CX2P9oMeJODcn9LEi7M-uO9dAqQhk5PPD9y9OrMOLBHQjXt0y6dWCqbU30ZFsNl0HuvL2_v8NXFOLixmNuxJmzRT8FHoMstBEZvJgOe5EXNjvKgQqueTJ9lT9HXTwhirLTEKwhWFk-490cGEobEOjVls-8DCFwOsLyq_O1hRkhuuxOwpzPHAg2czkq3RUG9sH3eSj0KT4dj5dCZu1AmPplzmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آخرین نرخ‌های ثبت‌شده در بازار آزاد در روز شنبه ۶ شهریور ۱۴۰۵، قیمت دلار آمریکا به حدود ۲۰۵ هزار و ۸۸۰ تومان رسیده است.
نرخ دلار در بازار هرات نیز حدود ۲۰۵ هزار و ۲۳۰ تومان ثبت شده است.
داده‌های لحظه‌ای بازار همچنین قیمت دلار را در ادامه معاملات بالاتر از ۲۰۶ هزار تومان نشان می‌دهد.
در همین حال، هر یورو حدود ۲۳۸ هزار و ۹۱۰ تومان و هر پوند بریتانیا حدود ۲۷۹ هزار و ۹۰ تومان معامله می‌شود.
قیمت دلار کانادا نیز به حدود ۱۴۸ هزار و ۶۵۰ تومان رسیده است.
در بازار طلا نیز هر گرم طلای ۱۸ عیار بر اساس تصویر ثبت‌شده از بازار به حدود ۲۱ میلیون و ۸۱۰ هزار و ۷۹۰ تومان رسیده است.
قیمت هر مثقال طلای آب‌شده نیز حدود ۹۴ میلیون و ۴۸۰ هزار تومان گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78084" target="_blank">📅 19:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=DiMCvIBwpeknAOoie5NHzcO9uG5SEEIXmPSbkU-WjPy_2h26XRPIYW9lo7pZG_85sHn22WsDliKy7po15RxCFGlotyrxFHOmqoGLym81Eus_I2f2D2ZBzSiCUtLrNAPJeyHDDbxxf417Nwy-9jGakhtRVym7QD5Rlk9hBZqSY4HqHiPqCb7VXDMjmoCoDZN5tT67RkMjnG2wKIgYDAJrZfopDjkjBnEJLo4fuxIZcJooCVU6GeUtb964rlPlo8CdQffMT2CbGYaDpQwEdJ85NSHBVcgfNJsCdkt0msZVEvIP1FiUA8RQvpo_jZ_K-GqmRAvXYFKsY8Qcvp5BYKwFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=DiMCvIBwpeknAOoie5NHzcO9uG5SEEIXmPSbkU-WjPy_2h26XRPIYW9lo7pZG_85sHn22WsDliKy7po15RxCFGlotyrxFHOmqoGLym81Eus_I2f2D2ZBzSiCUtLrNAPJeyHDDbxxf417Nwy-9jGakhtRVym7QD5Rlk9hBZqSY4HqHiPqCb7VXDMjmoCoDZN5tT67RkMjnG2wKIgYDAJrZfopDjkjBnEJLo4fuxIZcJooCVU6GeUtb964rlPlo8CdQffMT2CbGYaDpQwEdJ85NSHBVcgfNJsCdkt0msZVEvIP1FiUA8RQvpo_jZ_K-GqmRAvXYFKsY8Qcvp5BYKwFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی:
"اعزام نیروهای مردمی به تنگه هرمز در پاسخ به یاوه‌گویی‌های ترامپ"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78083" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or8Kk2kaAKxWAGVHgh7_7PEbqv-CtJOSFOItFOihkjRQcO0iGMifgX_X94qQNQs3E-Kg13jeSTrDz1t1ckYNmIzAHvGGQbwEGjUystJsfzZ59J-g_cC9CsTFlBna4qVgvM7Ur5zY0ANQ9dnPraAsZtKPd4FjsuRSLACisHu9ypXt8D1v0o4yBM0PddlmdBUzFIOmC1x_MRbcmlzF3YcEoffv4XWpNtHELsYUfWwc4yeaNvK_Qg1JxOizGK0rJ8YgAoofMaa8Xecb_0T3p6N7GXYEYVtkovt4tHNX_bQONJfXweki2HyDD-waAQh9q50GRBaRgtyrH9sk8j2UxCHV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از ابتدای سال ۲۰۲۶ تاکنون، بنیاد عبدالرحمن برومند ۹۵۰ مورد اعدام را در ایران مستند کرده است. دست‌کم ۲۰ زن و ۳۰ معترض در میان اعدام‌شدگان قرار دارند و تا این لحظه، ۴۵ مورد اعدام در ماه اوت به ثبت رسیده است.
🔸
در نظام قضایی جمهوری اسلامی که بر پایه روندهای ناعادلانه، عدم شفافیت و نفوذ انگیزه‌های سیاسی بنا شده و در آن اصول دادرسی عادلانه به‌طور سیستماتیک نقض می‌شود، استفاده از مجازات اعدام، بر اساس حقوق بین‌الملل، مصداق سلب خودسرانه حیات است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78082" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Me_lGYoKn_jEHkPxB9i6yPir20ywyiqgjFYCDb1dvkbzKgMKTa5F-Q15YX8XV-5r8YZUVFlIGuI0XJppirYCcsOcvfyRzBbl2Ha-GvEmK6WbtdPwOY80NrutYTmekc-mGkp29-tNw3q2R6FE_Vdfp64Y1V4Se8X2j3P1rOA3DUv_zEjElm4Ujjjw-LDdYHis2wN4CaBe7KZAUmrZBJC_HpWKGgWfn_PlTLvlBuxCE50WU9V37k9LGYIp1UWj36KdRYBgZyeVko9aOsjZj6xyvuQpVCjhvuCDe48TnXLsJD3rf9J6zmMjJ-az15kCMW_NQvCx2rZHpgAVHQArPglozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rywN0r1dfpP1bqmTooY8Vd3nevWrIeCDxj6dcAV8W54ynOp-DvsqMhqoR7xCpvvpCLoobOX9Sy8j9r5y7Z6pMJ-G88127pJgES3dGNizCjrU7GJzNFLlT83l6A-Ye_DS1xTe8JDxu25wMIgBmDzmysSiKwAjwg-JhQC7LACyDy03kPSfQCiH_PxsBNNTgHK9Q7hxTChbcfl2WOjN0BeFk2urvSD9OnrcH0S04qUFdg1nFGkl4nPr_Vqv21BKq7wVuVpt-x1I2BanoyhgLEy69f_HIflkgXv2z0eWOHcmotg7-9eqbZHzGahG8E1hD8BxZLgfjaWFydJvOY7tZ0V8gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در تروت سوشال اعلام کرد آمریکا با ونزوئلا به توافقی دست یافته که آن را «بزرگ‌ترین توافق نفتی در تاریخ جهان» خواند.
ترامپ گفت بر اساس این توافق و با مشارکت بخش خصوصی، آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه از ذخایر اثبات‌شده نفت ونزوئلا را بدون تحمیل هزینه به مالیات‌دهندگان آمریکایی در اختیار خواهد گرفت.
او افزود مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ آمریکا، با همکاری دلسی رودریگز، رییس‌جمهوری موقت ونزوئلا، در دستیابی به این توافق نقش داشته‌اند.
ترامپ گفت این توافق ذخایر نفت آمریکا را بیش از دو برابر می‌کند، عرضه نفت را به میزان قابل‌توجهی افزایش می‌دهد و در بلندمدت به کاهش قیمت بنزین برای آمریکایی‌ها کمک خواهد کرد.
@
VahidOOnLine
مارکو روبیو، وزیر امور خارجه ایالات متحده، روز جمعه با اشاره به توافق نفتی جدید میان واشنگتن و کاراکاس اعلام کرد که این توافق علاوه بر تضمین ذخایر پایدار و کاهش بهای بنزین در آمریکا، نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی را به ونزوئلا سرازیر خواهد کرد.
روبیو در اکس نوشت: «برای مردم ونزوئلا، این توافق نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی به همراه خواهد داشت، از هزاران شغل با دستمزد بالا حمایت می‌کند، و پیشران بازسازی اقتصاد ونزوئلا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78080" target="_blank">📅 04:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=rD29ZlwspLq1-d81bg_z1D-G4w2GSsMBqIdf08ODy1cyvh0Ddt3BUOAZZUSuCoa8peJf87QMDsCNbIMoS2_zrg4twYG9m1V2AMtO_6RXdhNbNdiLuKfS9iL_RFx_GwnhIo4O-XRZrJsH04k66Gmm6q1zBlx8Lb6orFedv1WmA620qA9CTwz0CkImB_5Ui2nrk5YJIClNLGcGpr0Um-7jTBO47jqpXMV-thCBKDHGIOzk61-wVvzu_NQoifeISiXzz7-u4XxktHgfzi4VU_ZWHpEOhC-VE6TjJyvS8RW3Qjk1qgWCAm6YDHBIrs-X0vDr9_d9vwtf7RNCZpl_B5OYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=rD29ZlwspLq1-d81bg_z1D-G4w2GSsMBqIdf08ODy1cyvh0Ddt3BUOAZZUSuCoa8peJf87QMDsCNbIMoS2_zrg4twYG9m1V2AMtO_6RXdhNbNdiLuKfS9iL_RFx_GwnhIo4O-XRZrJsH04k66Gmm6q1zBlx8Lb6orFedv1WmA620qA9CTwz0CkImB_5Ui2nrk5YJIClNLGcGpr0Um-7jTBO47jqpXMV-thCBKDHGIOzk61-wVvzu_NQoifeISiXzz7-u4XxktHgfzi4VU_ZWHpEOhC-VE6TjJyvS8RW3Qjk1qgWCAm6YDHBIrs-X0vDr9_d9vwtf7RNCZpl_B5OYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: نرخ سوم بنزین حدود ۱۰ هزار تومان خواهد شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78079" target="_blank">📅 22:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YG7vX8m8kOWHxDz-ugvpAjBV91vd0rFWArYipw2mWhvOdBmr0Ko10NZK1uPNIDf2yUcWY1o2CurKn1ohqKq84fzffOgkLKTIpQmSVzYAQ9cUK8txn-R7n-KJC4_mYO49p8xDGJ8xJUo2bsOdxFRV4CZRrgYsSrAbYDWAo6jeO-W77hWOpn23NVnHaclY6VuO0fotgUV_4hS6BwNgQ4_8tAb0bBcO5YIi12tchIjMN2zFLg9DDBmPICojRJuJJcaVM_kHmL8tJutCeUrPh9k7AXUp5fEqhznjt8Rh0YiUp7twJRhEPba16io8G0Jh5x6gUfc7MrJ0ywgya6Q2TgbiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.  به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم…</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78078" target="_blank">📅 21:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود که هر شریان اقتصادیِ باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید رژیم ایران پایان دهد.
همچنین هشدار دادیم که حامیان ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی برخوردار باشند.
بانک مصر امارات تصمیم گرفت این موضوع را به شیوه سخت بفهمد، و امروز نخستین گام را برای پاسخگو کردن آن به‌دلیل حمایت مستمر و فاحشش از رژیم ایران برمی‌داریم.
SecScottBessent
وزارت خزانه‌داری امریکا:
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)،  شبکه اجرای جرایم مالی (FinCEN) قاعده‌ای را پیشنهاد کرد که دسترسی بانک مصر امارات به خدمات بانکداری کارگزاریِ مؤسسات مالی آمریکا را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، را به همراه یک شرکت پوششی مستقر در هنگ‌کنگ که به پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی کمک کرده است، تحریم کرد.
«عملیات طرد اقتصادی» در حال قطع کردن آخرین شریان‌های مالی‌ای است که رژیم ایران را سرپا نگه می‌دارند.
USTreasury
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78077" target="_blank">📅 18:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LNKwUzFbDe0e_Y1F-rOOdC3oLXjcZ39S4dzhCoeenkzZjREnbHi28XI8UYtoubjf46xdWqvJE8isQT2iwOnR-dgviM5pKzkv3gu-OdoCqdu6Apf-TvmThliV4NDN55EqFKc3LG6r-prgklGqYRXJuiEYYcILDqBHxAn6i-E0hqXAnMqnLC7KDM12YZPiyf8F4FPrO9zX6YAvGDKPAemjOOPhrniD3cym2MmX7MOvBoFJzMzIEVZCcpahvmYai38XD8GzhQccnPy0Y7P0Uc-s08rXTDrQKj-KxNAj2ftWOAqN0KTfZtHqhY2RXs49CyNF9ZUz5sxP2B1dx3EU5QC2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا نوری، امام جمعه بجنورد، در خطبه‌های نماز جمعه این شهر گفت: فشار اقتصادی کمر خود آمریکا را هم دارد می‌شکند و با فشارهای مردم در آمریکا بر علیه خود ترامپ، او که رای اول را در آمریکا داشت امروز محبوبیتش به زیر ۳۰ درصد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78075" target="_blank">📅 16:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sWzNj4pkxMfddEZxHZmiEwgkrClbpQYZ_v7nQWVVYUJcjMQUSLhRAFFCvP3tPekYW0GzLgv4WmsbFXvPBVbAWu-YIc5qUX65UzXgAkHJ0r6dMPZTkMn2VqHkfJWvUZOHZ7FtgIrw-cIpZZ0WdYbmJtLCiM8v32EOB1qcgrOGCf1_hI11VMizXd4CYtc8DrP2jVOy8mKRBz9r-ApVfLYQAMp2UU2TGY9rzsT-U47wwurw2wE3QkTkVjNjEPvjL0fOAHAzQNUiRy_-Gfd0dx8PEXFQ-uYUitpnlOTKF0xwjwc4dkNex6vL9E0n3mf4bhGiZBZivbQAdAntyaUyOpNcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در واکنش به دور تازه فشارهای اقتصادی آمریکا، از کشورهای جهان خواست از اجرای تحریم‌های یک‌جانبه واشینگتن علیه ایران خودداری کنند.
این وزارتخانه روز جمعه، ششم شهریور، در بیانیه‌ای «عملیات طرد اقتصادی» آمریکا را «تروریسم دولتی» خواند و مدعی شد تحریم‌های جدید واشینگتن با منشور سازمان ملل و اصول حقوق بین‌الملل مغایرت دارد.
در این بیانیه، جمهوری اسلامی آمریکا را متهم کرده است که با استفاده از نقش دلار در نظام مالی بین‌المللی، کشورهای دیگر را برای قطع روابط اقتصادی با ایران تحت فشار قرار می‌دهد. وزارت خارجه جمهوری اسلامی این اقدام را نقض حاکمیت ملی کشورها و اصل برابری حاکمیتی دولت‌ها دانسته است.
وزارت خارجه جمهوری اسلامی همچنین به قطعنامه‌های مجمع عمومی سازمان ملل درباره منع مداخله در امور داخلی کشورها و اصول روابط دوستانه میان دولت‌ها استناد کرده و گفته است دولت‌ها نباید آثار تحریم‌های یک‌جانبه آمریکا را به رسمیت بشناسند یا در اجرای آنها مشارکت کنند.
در بخش دیگری از این بیانیه، تهران تحریم‌های تازه آمریکا را ادامه «جنگ اقتصادی» علیه جمهوری اسلامی دانسته و مدعی شده است این اقدامات با هدف تحمیل فشار و آسیب اقتصادی بر مردم ایران انجام می‌شود. وزارت خارجه جمهوری اسلامی همچنین از سازمان ملل و کشورهای عضو به دلیل آنچه «مماشات» در برابر اقدامات آمریکا و اسرائیل خوانده، انتقاد کرده است.
این موضع‌گیری پس از آن صورت گرفت که آمریکا در روز دوشنبه، دوم شهریور، از آغاز کارزار تازه‌ای با عنوان «عملیات طرد اقتصادی» علیه جمهوری اسلامی خبر داد. هدف اعلام‌شده این کارزار، تشدید فشار بر روابط اقتصادی ایران با دیگر کشورها از طریق تهدید به اعمال تحریم‌های ثانویه و محدودیت در دسترسی به نظام مالی آمریکا عنوان شده است.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز در نامه‌ای به آنتونیو گوترش، دبیرکل سازمان ملل، از این سازمان و کشورهای عضو خواسته است در برابر اقدام تازه آمریکا واکنش نشان دهند و واشینگتن را مسئول پیامدهای تحریم‌های یک‌جانبه دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78074" target="_blank">📅 16:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78073">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/693aecab40.mp4?token=kQXgmjQhm5SQIGSlLXmAkyS5pOHVzFkVY_2fG9M26dRCggvvrxooQYvSnZt59UIme-qXfyT8b8A5HZCnblxrGZn5cTaTxBEw9daZOEDuRYporICKRa1ggR6j9pTYWDXf1twfTCqPNenp-Ryhlkbj_uM4CXV2jN5nh6XGIUqtyaNMYPpKnKIeZ8myByAI7g1W_DvQKipw4lRgCHGYrh5ZgDf0bvtzP-doeWW4OYzyjWrVJUvC-uQcbytnVGnOwo36mOT2Yp4IBs6462LXeFd-pbLheVOPXsnCbF2r8LfxZdHULjtkMp5SPolQ67rPzql0axevA3NsyDcb9TvCYJi4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/693aecab40.mp4?token=kQXgmjQhm5SQIGSlLXmAkyS5pOHVzFkVY_2fG9M26dRCggvvrxooQYvSnZt59UIme-qXfyT8b8A5HZCnblxrGZn5cTaTxBEw9daZOEDuRYporICKRa1ggR6j9pTYWDXf1twfTCqPNenp-Ryhlkbj_uM4CXV2jN5nh6XGIUqtyaNMYPpKnKIeZ8myByAI7g1W_DvQKipw4lRgCHGYrh5ZgDf0bvtzP-doeWW4OYzyjWrVJUvC-uQcbytnVGnOwo36mOT2Yp4IBs6462LXeFd-pbLheVOPXsnCbF2r8LfxZdHULjtkMp5SPolQ67rPzql0axevA3NsyDcb9TvCYJi4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش ایالات متحده در ویدئویی که روز پنجشنبه پنجم شهریور منتشر شد اعلام کرد که نیروهای آمریکایی مین‌های دریایی را از تنگه هرمز پاکسازی کرده‌اند و مسیرهای بین‌المللی کشتیرانی باز هستند.
دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ارتش ایالات متحده، سنتکام در یک پیام ویدئویی که در رسانه‌های اجتماعی منتشر شد، تاکید کرد که «امروز، خطوط کشتیرانی بین‌المللی باز هستند و تردد در حال افزایش است.»
کوپر با اشاره به پاکسازی مین‌ها در تنگه هرمز گفت: «شرایط، می‌توان گفت، چالش‌برانگیز و خطرناک بود. اما ما کار را انجام دادیم.»
پیشتر دونالد ترامپ، رئیس‌جمهور آمریکا، هم از پاکسازی تنگه هرمز از مین‌های کار گذاشته‌شده‌ ایران در تنگه هرمز خبر داده بود. سپاه پاسداران اما با رد این اظهارات بارها تأکید کرده که تنگه هرمز همچنان مسدود است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78073" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/st63sg1IVsxn90is0TYsHgjvrx2Gh5gyIhHtkt0bCnSaVTXBexInHcKBeL1TtlEx5EuKFwtCLTEpOCD-c4q0xvaVZ06M6jSD4C9m0XMGa_kmm030Fww9hz_8LcCpW5RuHGARpLEu4p1SCfyrooDk85Qn2OPy7g7Wn4CS8TIAH9Jqj3fJ3d4KKoBF6TmX_VcJPUtYZW0w6-fkBI0fuHbFUa66ZcOoMOk3pbTztUkulM2tzuO-q9AcHtDkFjafh0HZKnGXaJGf4Onbwgeht3hw8czJQAb392jSJzUEm6c3DczF-DvQh5MLRpLSsaTBBuBQdX_NvGfIkpqStJe1QM5H5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oYYjd3UePgu7U3q55H_gnGUL2kCJPXvlxFdKsGfUDPKYj3Hi9TlhZGLa3WYZ9ssuklDkwtXpCnyrdWIWJlIqUYlymzW_U65YUuzGj571J0a5aCbAoBMYCdaey77dXU2Q3v2SuxIZ33qIIwlyu-EUit8v3TfI_r7o_87HRD1AFqMUvUIkHpkXgLZnKLU0ffD7vjk55oZXSxNPas12fUP6qM4Y9UnYg1SzLqzmuewkOqzv6Mqb8PunlcTOLG_VEvLPX5z5lBmo2tD7_OI3-Rn5jk8_Ndm6NjtdQaZbJymBX0-0bfpjy0P9iq0CR5xoXA9w7UDS_1ZD_YXrC6BDQzJRCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفت‌وگو با اکسیوس درباره تنگه هرمز تاکید کرد که این تنگه «باز است.»
او گفت: «پاسخ ایران بسیار ملایم است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم. تمام ماجرا همین است. بقیه چیزها اهمیتی ندارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78071" target="_blank">📅 16:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IQ7sjvn3X_x4vhOjpwYq1oYMKjEMslv51uL-grXfCUR5pg5uslwiVcNizynpo4nW-xZTH6eN_x834b8H7w45STuVDZMqaQCt33LrqWFUuJY-ZAHAbr2UiEFYSDAfJHm8JPoYF25CRt6RgzqWYxSMMBtD5zHMuk1sRi57qV6jMgkLthGsDkOB8_ZKIWi7RrEI_an0lilvOeG21P_MAZDar1bQtq9zr4CSGBJnyUAGCwX3EtV2geRO-sA7UzKfTLUq0xAxWjIhIZqcPiZmfLHhimp2AeekPDtqmo_Kf9jE6rDG2s66l78jNMABpg1swwrzdxVfQmqhc3T5tNW2BOwBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sKiEUX9hDYQBaxulNCKq-4NtYb4eEgw57CRH21KtxZrP2je7Q0qnWz437TkcnmNtZR0l4l40UYmIWpGHnBMwdfvxscFiiru0-5SvAHM9gUDB45F2NJdq2vOI0rH2OT6Ca68EQXMCF5WLPZ6MjPLQL6LR0iQCP97GBFjeQ5ieZjEtyKmmi-0RZcjhWGF12hOJOZ2eblLfbU6ViH5zsdKSB8AxYPCpNEVc0OC5X9eX-uEtqpQC15FFSKFuajA6oY5qNT93lCzMey-Ou02yQyua92A7H4QPHSRCcNjov53_0Jmd4nlGof3gEZXi2eBYswaQOTTIzF26gqWr2C4vVe4T4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع آگاه به رسانه‌های آمریکا گفته‌اند جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، در جریان سفر محرمانه خود به مسکو از مقام‌های اطلاعاتی روسیه خواسته است اطلاعاتی را که می‌تواند به ایران کمک کند، در اختیار تهران قرار ندهند. همچنین گفته می‌شود موضوع حمایت روسیه از ایران از محورهای گفت‌وگوهای او با طرف روس بوده است.
این دیدار در جریان نخستین سفر برملا شده یک رئیس سیا به مسکو از سال ۲۰۲۱ به شمار می‌رود. کرملین تایید کرده است که آقای رتکلیف با مقام‌های اطلاعاتی روسیه دیدار کرده، اما با ولادیمیر پوتین، رئیس‌جمهور روسیه، ملاقات نداشته است.
بر اساس گزارش‌ها، جان رتکلیف علاوه بر موضوع ایران، درباره نگرانی‌های آمریکا نسبت به امنیت کشورهای عضو ناتو نیز با مقام‌های روس گفت‌وگو کرده است. با این حال، مقام‌های آمریکایی و روسی جزئیات رسمی درباره محتوای مذاکرات منتشر نکرده‌اند و سازمان سیا نیز از اظهار نظر درباره این سفر خودداری کرده است.
@
VahidHeadline
وزیر خارجه روسیه می‌گوید مسکو با دریافت عوارض از کشتی‌های عبوری از تنگهٔ هرمز موافق نیست؛ با این همه به گفته او، این موضوع به مذاکرات بیشتر نیاز دارد.
به گزارش خبرگزاری اینترفکس، سرگئی لاوروف در گفت‌وگویی با تلویزیون «آربی‌سی» با اشاره به باز بودن تنگهٔ هرمز تا قبل از آغاز حملات اسرائیل و آمریکا به ایران در ۹ اسفند پارسال، گفت: ایرانی‌ها «تنها برای این‌که تنگه هرمز امروز کاملاً باز باشد، در حال بحث در مورد عوارض عبور هستند. تا زمانی که ایالات متحده و اسرائیل آن قمار را آغاز نکردند، هیچ عوارضی وجود نداشت».
لاوروف تصریح کرد: «آمریکایی‌ها اکنون از ایران می‌خواهند تنگهٔ هرمز را باز کند و ایران می‌گوید که در ازای آن باید تحریم‌ها کاهش یا لغو شوند. و آن‌ها این کار را خواهند کرد».
رئیس‌جمهور آمریکا روز پنجشنبه گفت که دیگر نمی‌خواهد با مقام‌های جمهوری اسلامی مذاکره کند.
ترامپ افزود: روسیه رفتار مناسبی در تنگهٔ هرمز داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78069" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtxeWZM9Z57oUNfAZo-koVpy3S5HXMchjGcnr-thRk70AxkzFFSFVD4C4m-Vb4iDtCcxd8avbWJ2Iyppud1-q4S0i6F1T8OwsPiG1upgN71JW6wSNTLzBdMx3cf0T3Kn8oD4-e4HqnTujLXbZ_R1IKOXzBK50h1pLG_oy9ku0bH-Z4rY__R5olUmqp7agqqb5uJCj_mAWEt760PHr0ibJf1CoymCpYB7DJDK4Mer2yGMpLDe2v3ZaCpgpIT1WFOsSG3UEs1J5GR5eSRuV4z-TDE2InvENPyzQHlVHd5cDzCeTZSIcz69EtLkMmlmeifxOEmJe9JqeHQd5p0BzesKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه جهان صنعت بر اساس آمار بانک مرکزی گزارش داد که تورم نقطه‌به‌نقطه در مرداد ۱۴۰۵ به ۸۴.۴ درصد رسید؛ رقمی که نسبت به ۸۳.۹ درصد در تیرماه افزایش نشان می‌دهد.
براساس این گزارش که صبح پنجشنبه ششم شهریورماه منتشر شده، تورم نقطه‌به‌نقطه در بخش کالا به ۱۲۱.۵ درصد رسیده و از افزایش چشمگیر قیمت اجناس طی یک سال گذشته حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78068" target="_blank">📅 16:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=lU2EL1GZwQ0BLef_SQ2fYdclCvSwNkfagucQZJPU9CGUU74e43Sz0XIqJ4BUee4svimBCLXviZxo0cTvUYU-KERadUm2EIRebTWgNSWPRdxhJNEbIBTCQaWtiEGjznkhOtQ7T34_jq4xYpTG1_IS4OcOLq87vywOr2Kjk3PkpgMlDEM5rNtrz91LUWLVqSbVYbmijmxWrDgRnxD4_JAL_Uty6ARyLpjxFtfF7guZ0iWYRKUSOiXAjHiXTgC4p5jAgLDsV8-nPGmnKJL4CniKdVabHZvhe-ziMzU8NXU8CerX_RWa5Nzh75zvEhYO-xqYY38C_oJzzT3mDFHupx6oFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=lU2EL1GZwQ0BLef_SQ2fYdclCvSwNkfagucQZJPU9CGUU74e43Sz0XIqJ4BUee4svimBCLXviZxo0cTvUYU-KERadUm2EIRebTWgNSWPRdxhJNEbIBTCQaWtiEGjznkhOtQ7T34_jq4xYpTG1_IS4OcOLq87vywOr2Kjk3PkpgMlDEM5rNtrz91LUWLVqSbVYbmijmxWrDgRnxD4_JAL_Uty6ARyLpjxFtfF7guZ0iWYRKUSOiXAjHiXTgC4p5jAgLDsV8-nPGmnKJL4CniKdVabHZvhe-ziMzU8NXU8CerX_RWa5Nzh75zvEhYO-xqYY38C_oJzzT3mDFHupx6oFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک زن شاغل در حرفه قصابی با انتشار ویدیویی از وضعیت کساد بازار و تشدید فشار معیشتی مردم می‌گوید مشتریانی به مغازه‌اش می‌آیند و می‌گویند شش ماه یا حتی یک سال است گوشت نخورده‌اند.
مرکز آمار ایران در تازه‌ترین گزارش خود از ادامه جهش قیمت مواد غذایی در مردادماه خبر داده است.
در میان گروه‌های خوراکی شیر، پنیر و تخم‌مرغ و همچنین گوشت و فرآورده‌های آن، از جمله گروه‌هایی هستند که در ماه‌های اخیر افزایش قیمت بالایی را تجربه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/78067" target="_blank">📅 16:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WU0xrcsNQcnlmRDFOeaCaTWBBM8CLiFbWIeV3ezXLbLLMqqjJcmM89w_QPcV7po40iKEnyQPxSqWa41bsVE4nRUghNPD0XmfzPumEGLPuFer-aFAy9WNKyaLjYAZsya0tfF6yy9o8r10W1wlEuBjtn5DoAQSv981B9ttu-0VhUth0_iw870xWsPMidYwd2di8_bltI6tGJQAsUkOz5xVo7NupWPHPGeebMT75oMd19Pupy0NU0qRdw9cuXxVRBGTIpOYYTbKvgcE-G_L-pNEreFBj2A10dMawFlzKYU29luQdoTp2_VPseYVyq9X3m7RsluZQs1YWfVVXSADMIkyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رضا زنگنه، جوان ۲۷ ساله اهل روستای کلیل‌آباد ملایر و ساکن کرج، با اتهام «محاربه» به اعدام محکوم شده است.
پرونده او اکنون برای رسیدگی به فرجام‌خواهی به دیوان عالی کشور ارسال شده و در صورت تأیید حکم، این زندانی با خطر اجرای اعدام روبه‌رو خواهد بود.
بر اساس اطلاعات رسیده، رضا زنگنه روز ۱۳ فروردین‌ماه از ملایر به کرج بازگشت و روز بعد، ۱۴ فروردین، هنگامی که مغازه خود را باز کرده بود، مأموران به محل کار او یورش بردند و او را بازداشت کردند. شماری از مغازه‌داران و کسبه اطراف شاهد بازداشت او بوده‌اند.
زنگنه تعمیرکار خودروهای لوکس و خارجی است و هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شود. او از ابتدای پرونده وکیل تسخیری داشته، اما خانواده‌اش در جریان رسیدگی قضایی، وکیل انتخابی نیز برای پیگیری پرونده معرفی کرده‌اند.
@
Tavaana_TavaanaTech
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78066" target="_blank">📅 16:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAUGR55r6hZs1JT57CZdi7au7sdbHwo6msqzLC-cowFR21G-7ZN4t0tfFQ6F6zkEbAaCAYkhIP_Kls8QSmbphoMguEzxf2nvR3ZgsGzmSgXs6LKkxT5opG0iwLXRdyKTtvw4YMgr_Mfct79op4gd0-VIEK0CpEDSLP_Su8twG694IPRZxPx75NCuex7HFXEL1zWTU0qjqcGfABm2UlHqbLdziYG8h6m2XFpv2vcSVaR0Ao2aZus1dJZ7ThFfaTCJUh4_lwZgGRlESuWc12ilQxlgiHkGNRiZCeoz0YM1U3ddeGPpW3eWl2mOE6OLLt8UkAQOH6gGnSV0sV6sbQOmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ به میانجی‌ها اعلام کرده است که تمایلی به بازگشت به مفاد توافق اولیه ماه ژوئن با جمهوری اسلامی ندارد.
این موضع تلاش‌های تازه قطر، عمان و پاکستان برای احیای مذاکرات میان واشنگتن و تهران را با مانع روبرو کرده است.
روزنامه وال‌استریت ژورنال روز پنجشنبه پنجم شهریورماه به نقل از افراد مطلع گزارش داد که دولت ترامپ این موضع را بارها به میانجی‌ها منتقل کرده است.
توافق اولیه که با میانجی‌گری پاکستان شکل گرفت، بازگشایی تنگه هرمز و آغاز گفتگو درباره برنامه هسته‌ای جمهوری اسلامی و پایان جنگ را دنبال می‌کرد. در مقابل، کاهش تحریم‌ها و دسترسی تهران به دارایی‌های مسدودشده در نظر گرفته شده بود.
به نوشته وال‌استریت ژورنال، ترامپ اکنون فشار اقتصادی بر جمهوری اسلامی را در اولویت قرار داده و آماده است برای مشخص شدن نتیجه این سیاست صبر کند. آنا کلی، سخنگوی کاخ سفید، نیز گفت هیچ مذاکره‌ای با جمهوری اسلامی در جریان نیست یا برنامه‌ریزی نشده و محاصره دریایی و «عملیات طرد اقتصادی» ادامه خواهد یافت.
این گزارش در حالی منتشر شد که عاصم منیر، فرمانده ارتش پاکستان، اوایل هفته جاری برای گفتگو به تهران سفر کرد. وزیر خارجه عمان نیز برای دستیابی به تفاهمی درباره مسیر عبور کشتی‌ها از تنگه هرمز با مقام‌های جمهوری اسلامی گفتگو کرده است. نخست‌وزیر قطر نیز پنجشنبه پنجم شهریورماه در تهران با مقام‌های جمهوری اسلامی دیدار کرد.
وال‌استریت ژورنال نوشت اختلاف بر سر نحوه تفسیر توافق ژوئن و شرایط بازگشایی تنگه هرمز، دستیابی به چارچوبی برای ازسرگیری مذاکرات را دشوار کرده است. هم‌زمان، تهران بر اجرای مفاد توافق پیشین تاکید دارد، در حالی که واشنگتن مسیر فشار اقتصادی را دنبال می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78065" target="_blank">📅 23:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=XRWYjGALPP_F_ALl0wA5NZ0jHicCtMM0_BHWl_A5xpA_k0QnhQXJNxikatFICOfxbfnHvNEWzWbz6iGitn0OOfjmEhBF0vRC0_2tTQk2kaouuxqbH2aUXG98pREIlEnCIg6YXC-BEqUlSQ-pR0yPNRbUh0B_bdNK-pSob2bDUDpdUj1q5LFgDF3nOy4VNPcPJwSvRc1xjApxyDKwK3y9AjYViv7R9FuZMl2xjMtNKWhrdlJIfhPFKBtzsgHVZgU7s0AThXBc76qHAP_yebhnr4-L8WKnIvttlzpJTcZJH7bDUKBSb3s7Jk1c2sBUEDBPRk-CEWFhPSSFzsYECazAOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=XRWYjGALPP_F_ALl0wA5NZ0jHicCtMM0_BHWl_A5xpA_k0QnhQXJNxikatFICOfxbfnHvNEWzWbz6iGitn0OOfjmEhBF0vRC0_2tTQk2kaouuxqbH2aUXG98pREIlEnCIg6YXC-BEqUlSQ-pR0yPNRbUh0B_bdNK-pSob2bDUDpdUj1q5LFgDF3nOy4VNPcPJwSvRc1xjApxyDKwK3y9AjYViv7R9FuZMl2xjMtNKWhrdlJIfhPFKBtzsgHVZgU7s0AThXBc76qHAP_yebhnr4-L8WKnIvttlzpJTcZJH7bDUKBSb3s7Jk1c2sBUEDBPRk-CEWFhPSSFzsYECazAOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در کاخ سفید و پس از امضای فرمان اجرایی تغییر نام «دریاچه اونتاریو» به «دریاچه آمریکا»، به پرسش‌های خبرنگاران درباره نحوه اعمال تحریم‌های ثانویه علیه کشورهایی که با جمهوری اسلامی ایران روابط اقتصادی داشته باشند، پاسخ داد.
ترامپ در واکنش به پرسشی درباره عملکرد روسیه در منطقه و برخورد احتمالی آمریکا در صورت تداوم معاملات با ایران گفت: «تا اینجا رفتار روسیه در رابطه با تنگه هرمز بسیار خوب بوده است.» او با تاکید بر تقابل پایاپای واشنگتن با سایر قدرت‌ها افزود: «باید در نظر داشته باشید در برابر هر کاری که آن‌ها انجام می‌دهند، ما هم انجام می‌دهیم.»
رئیس‌جمهوری آمریکا همچنین در پاسخ به نگران‌کننده‌بودن اقدامات پکن گفت: «یک نفر درباره چین می‌گفت شنیده‌ایم آن‌ها دارند جاسوسی می‌کنند؛ ما هم از آن‌ها جاسوسی می‌کنیم. وضعیت همین‌طور پیش می‌رود.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز پنجشنبه پنجم شهریورماه، فرمان اجرایی جدیدی را امضا کرد که به موجب آن دستور داده شده نام «دریاچه اونتاریو» فورا به «دریاچه آمریکا» تغییر یابد.
ترامپ پیش از امضای این فرمان در دفتر بیضی کاخ سفید اعلام کرد: «ما نام دریاچه اونتاریو را تغییر می‌دهیم و این تصمیم از همین لحظه لازم‌الاجراست.» بر اساس اعلام یکی از مقامات کاخ سفید، این فرمان وزارت کشور آمریکا را موظف می‌سازد پایگاه داده‌های جغرافیایی ایالات متحده را برای بازتاب این نام جدید به‌روزرسانی کند.
این اقدام نمادین پس از شکست مذاکرات تجاری میان واشنگتن و اوتاوا، وضع تعرفه‌های تلافی‌جویانه و تیرگی شدید روابط میان دو کشور همسایه رخ می‌دهد.
با این حال، مقامات کانادایی پیش‌تر صراحتا اعلام کرده‌اند که این تصمیم یک‌جانبه واشنگتن را به رسمیت نخواهند شناخت و نام این دریاچه مرزی مشترک در خاک کانادا همچنان «دریاچه اونتاریو» باقی خواهد ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78064" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78063">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dPjiEQsoZGFYsl0UfDbpHKHRZeKCSZI_RzGI_b5yfqQuXgo_ekasrqyAtGZvQlJWl5FWcqQtq_syj4SxjpZLk8Lporj2JzTs6uT28R0pZemE1D4jW3yApYU5V9svXooqKmbTDu8jcPjzug8ANB8MS96uQN3PreNZgmhyrsfHrWMaOHty3u5zDIn2Enl_iTpfObdTKWm4rLdTKUAMqOhxHtXxr5bzKMWifKxe0z-xo8AeNeDkY_vVqGOTfnmyJDTqkX23e4Fy7uXYxdckr2SiyUhQoWC05f_menXStsWieS1U5ikmlCsDT711nrVpdYUXpeDZPmVV8NP-hq9BjOvNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان اطلاعات سپاه روز پنجشنبه ۵شهریور۱۴۰۵ با انتشار بیانیه‌ای نسبت به تشدید نارضایتی‌های اجتماعی هشدار داد.
در این بیانیه به ناکامی «دشمنان ایران» در «تلاش برای تغییر حکومت ایران از طریق حملات نظامی» اشاره شده و آمده است: «مخالفان جمهوری اسلامی در حال تغییر راهبرد خود هستند.»
این نهاد نظامی و امنیتی مدعی شد که فعال کردن بحران‌های داخلی، جنگ روانی، فشار اقتصادی و عملیات‌های امنیتی از محورهای این تغییر رویکرد است.
سازمان اطلاعات سپاه در این بیانیه نسبت به افزایش نارضایتی‌های اجتماعی و احتمال اعتراضات خیابانی هشدار داد و گفت مخالفان جمهوری اسلامی بر «برهم زدن ثبات و کاهش تاب‌آوری ملی» از طریق «نبرد شناختی و تولید ترس و ابهام» تمرکز کرده‌اند.
این نهاد همچنین از شناسایی آن‌چه «ساختار محرمانه و اختصاصی» موساد، سازمان اطلاعات اسراییل برای اعمال فشار از داخل ایران خواند، خبر داد و مدعی شد این ساختار از طریق ارتباط با گروه‌های مخالف، انجام عملیات خرابکارانه و به‌کارگیری عوامل محلی فعالیت می‌کند.
در این بیانیه ادعا شده که جمهوری اسلامی از وضعیت «صرفاً پاسخ‌گویی» به حملات خارج شده و در پی افزایش نقش خود در تعیین روند جنگ و دیپلماسی است.
در بخشی از بیانیه منتشر شده آمده است: «ایران دیگر صرفاً در موقعیت پاسخ به حملات طرف مقابل قرار ندارد» و به سوی «افزایش ابتکار عمل راهبردی و اثرگذاری بر زمان، مکان و هزینه جنگ و دیپلماسی» حرکت می‌کند.
سازمان اطلاعات سپاه همچنین ادعای حاکمیت ایران بر تنگه هرمز را تکرار کرد و نوشت توانایی‌های نظامی و «نامتقارن» جمهوری اسلامی حفظ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78063" target="_blank">📅 23:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78062">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BheuMNycuqSs0UMNeUCbWoB5t1G-HHxGir1svPcYbbcCgHV9DTk8QXvme9DBtIozGczWZqSrcGVKTkesaeVLlVyW7MsRFA6uri0MpK3XQb5z6jIjpNam2DwcqQa-_17fCxXoWlD-LWlzZaEJ-3bolvZS6-cYr6h88x9_Vf767ck6LO3regQ4G5Q6MdvZuJe7c_ZBigBUJ-WRiTsIdKPd5GJqSFY81EYKuFRhE-fJfQta6nNVNtgfn1EVMFtcP-ebuluIwd2K3gVSK9oO8OY-A_FyUn3gGQLTRxqccqFdUXjWFrbFCfq_yEcIrtFHvnRmrPQrakgnnDerbjxstjqiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.
به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم خواند، و در توضیح دلیل آن گفت: «توزیع بنزین عادلانه نیست و تداوم این مسیر غیرممکن است. ضمن این‌که تولید بنزین کفایت نمی‌کند و با محاصرهٔ دریایی آمریکا نمی‌توانیم بنزین وارد کنیم.»
این مقام دولت ایران در عین حال گفت مشخص نیست این تغییرات به چه میزان و چه زمانی انجام می‌شود.
در روزهای اخیر، هم‌زمان با افزایش اظهارنظرهای مقام‌های جمهوری اسلامی دربارهٔ لزوم افزایش قیمت بنزین، گزارش‌های مختلفی از تعطیلی برخی جایگاه‌های عرضهٔ سوخت در تهران و تشکیل صف‌های طولانی مقابل آن‌ها منتشر شده است.
بر اساس آخرین آمار اعلام‌شده، تولید روزانهٔ بنزین در کشور حدود ۱۱۵ میلیون لیتر و مصرف آن حدود ۱۲۹ میلیون لیتر است. به این ترتیب، میزان تولید روزانه روزانه حدود ۱۴ میلیون لیتر کمتر از میزان مصرف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78062" target="_blank">📅 19:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78060">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz01YfO4vpnmnP5kD3ya5m3sTt8e1RZPz9KnN8VGGEJ_Pv4alkORj-pmc89Dim1LtBZJDK9Uh4LjQu5nVZrod6nxe9iUt1yp_fHvnjiITsr55gnlF14dfepTcaBWE5tm819-TH66-GIIXOF6ZTI_rCijmaqG93f4-NkTMc7c-n-d07KbcdTwdydErLLE-7ytr4ftCFqPfdbv5P66KXiDFm6DeaIBU_P1ol1XvByQDJO5UllA5Mh7qs_7pAzhcd3i_92KYeLuKkhgjCOCL0oEXCKAbxwdjyE-w2EfCxFDZbd91XTECi4NVzEkgF9Lhy_vlQ0ptlBRNNZOGFwLdDoOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OjGklJKCxty1I656FuTpKATHFH5-UYydZwImMCeVp0mA_FV_VKtPcy1hChulhS_xLhz0EQzlypyu3PNa15-v_AJYNoNSb7dsm0iuvzwPsuLiPaZRqjB1pwhEsBd9NT-JBIkbxRw18mPAwl6aw5NBMLE3qS1r-V1v7NTmgIUoLp2BQ7Bhn6Azgdhc5R-FrVGWnbbxMLE5ZfESviDkdKQ-_fxC0qBevT9N2bIkZ_2lqByqZbD2JZK_5fO7tQrNKPTSi8fD9KYuxH9hi08W2gWQf2_xxZwIePRh8qRX81Vp1eidp7bJwih5Sc0LwcmfVEjFocmQdf2SO7cM_tQAX3mAsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، در سفر به تهران با مسعود پزشکیان دیدار کرد.
وزیر خارجه قطر در این سفر با محمدباقر قالیباف، رییس مجلس شورای اسلامی نیز دیدار کرده و درباره راه‌حل برای از سرگیری مذاکرات میان واشینگتن و تهران گفت‌وگو کرده بود.
@
VahidOOnLine
وزیر خارجه قطر همچنین به قالیباف گفته است که گفت‌وگو بهترین راه برای حل اختلافات و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78060" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78059">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJysrigAorQsSGAoKdhaXGTYZuHyl3P8mhic8beDnymaa74DCsPY1IadRnQitXcvHR5Jr_vfd3P9b29Zgb3QSevLe6O1f-SzslcnPsX_AsquSAjMsyAdx0eCmO3rWNlDBiumT25mIUXwD1e9EBHjs-_Vr-i56wavsCVfqVohAKdPc96U57Ta1Sp9HMvMsxiQMp6Kp2X5GMeF1GYTMDVBr53XtO4_D60jCTHR8iD8wOmHASrO2HNx_Ev20WpD6KqsKHLPMSc7bnncWbvRK0dMzbvN0EO7iTlyKdmzjgpai_5TzxOvRm6mWh0e6pKqPaCFWycWMMpf1ibYI2mzuZTFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیه رمضانی، زن ۳۹ ساله و مادر دو فرزند، در جریان سرکوب اعتراضات دی‌ماه ۱۴۰۴ در تهران با شلیک مستقیم نیروهای جمهوری اسلامی کشته شد.
ماموران بامداد جمعه ۱۹ دی ۱۴۰۴، از فاصله‌ای نزدیک و از پشت به رمضانی شلیک کردند. گلوله پس از عبور از پشت و قفسه سینه، به قلب او رسید و جانش را گرفت.
آسیه رمضانی مادر یک دختر نوجوان و یک پسر دبستانی بود.
خانواده‌اش می‌گویند پس از تیراندازی، او را به یک درمانگاه منتقل کردند؛ اما بدون رسیدگی پزشکی موثر، برای حدود پنج ساعت در حال خون‌ریزی رها شد.
خانواده رمضانی پس از بی‌خبر ماندن از سرنوشت او، سه روز میان پزشکی قانونی کهریزک و بهشت زهرا در جست‌وجویش بودند تا سرانجام پیکرش را پیدا کردند.
خانواده، زمانی که پیکر رمضانی را یافتند، گونه‌اش کبود بود و از زیر کاوری که پیکر را در آن قرار داده بودند، همچنان خون دیده می‌شد. آن‌ها گفته‌اند پیکر او در شرایطی «ناشایست و دردناک» نگهداری شده بود.
خانواده رمضانی همچنین می‌گویند لباس‌ها، کفش‌ها و دیگر وسایل شخصی او برداشته شده و به آن‌ها تحویل داده نشده است.
آن‌ها پس از تحویل پیکر متوجه شدند قلب رمضانی که با گلوله شکافته شده بود، بدون اطلاعشان بخیه زده شده است. خانواده آسیه رمضانی در روایت خود نوشته‌اند: «ما آن سه روز را فراموش نمی‌کنیم. آن پنج ساعت، آن خون، آن کاور، آن قلب شکافته‌شده و وسایلی را که باید به خانواده‌اش بازگردانده می‌شدند، فراموش نمی‌کنیم.»
آن‌ها تاکید کرده‌اند که همه واقعیت‌های مربوط به کشته‌شدن او هنوز روشن نشده است و افزوده‌اند: «هزار سال هم که بگذرد، خون عزیزانمان پاک نمی‌شود. نامشان را تکرار می‌کنیم، روایتشان‌ را زنده نگه می‌داریم و دادخواه می‌مانیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78059" target="_blank">📅 17:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78058">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gaybNuwjfyqLjj-YomYW0xw2nT5RKnSwZtsBHzJACRxbB1pL75GPQMXUR2oqUn7LpDDsBMDlTPk8EqtqIUw8oXVJ2lLM0GW7x8fXLhTEFhYN9izBE6to-8E9qEYGglAoB3FAwvZST36gYzE1WsQYmfbR2wAN65fVZBxZIovGRFPYaga6i4SPZei4cXSiBxUYOkjUFV7D72qdK_dODSUo2gqZtg8ADCs32kJtmxfc2RvqeBTbSySVX8XeYqvgwiXYIAtoXpiuC__3Y86-rJ5FBhogNz3roRYZuKGkThOAK9ivA2gwSoKUDoIjycFrloQLdE0gJDwoDDOVDfdi10LJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با انتشار پیامی در شبکه اجتماعی ایکس، با انتقاد از سیاست‌های مالی جمهوری اسلامی، خواستار اختصاص منابع مالی کشور به مردم ایران شد.
بسنت در پیام خود نوشت: «در حالی که مردم ایران برای تامین نیازهای اولیه خود با مشکلات معیشتی دست‌وپنجه نرم می‌کنند، حکومت فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.»
وزیر خزانه‌داری آمریکا در ادامه افزود: «حکومت ایران به جای تزریق میلیاردها دلار به گروه‌های نیابتی تروریستی خود، باید این پول را صرف مردم کشورش کند.»
این اظهارات هم‌زمان با تشدید کارزار تحریم‌های مالی ایالات متحده برای محدود کردن دسترسی حکومت ایران به منابع ارز خارجی مطرح می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78058" target="_blank">📅 17:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78057">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hYNjZ7Aqf3wFl4gAUSRYcAstydYXDbRW6WdGzwJQpKF5fROeI3bzmSJOf8LOleZVpajZmMyz5O-7-WVlNgUdfr2ZMHZTCKvvznnWXx4TAPES8w0XD8D26HB9FqqY6k1g-D7q53cURiExqYF-KAx81aGgsDLjSWFJoCBxY32XOLGna5sP3bIWuvVRBpO7qf0XloNQrWike5dM9PebFLQLqUXnPfkK775P5tsjH9WjW2Vquky_zxQB-09OITjtIU_XbayjadVLFqExWun_WkI2X4VxHGgkRrI29mtnJpcoUftQTVjW_W19lni0Zlm2CZ9kBZvFvC9Pse082hRH6qbp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت شاخص برنت در پی بهبود وضعیت تردد کشتی‌ها از تنگه هرمز و انتظارها درباره مذاکرات مثبت میان ایران و قطر روند نزولی خود را ادامه داد و روز پنج‌شنبه به ۸۶ دلار و ۷۵ سنت رسید.
قیمت نفت طی روز جاری نسب به روز چهارشنبه بیش از یک دلار و نسبت به هفته گذشته حدود هشت دلار افت کرده است.
در پی سفر وزیر خارجه عمان و فرمانده ارتش پاکستان به تهران طی روزهای گذشته، اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، روز چهارشنبه اعلام کرد نخست‌وزیر قطر نیز قرار است به زودی به تهران سفر کند.
هم‌زمان وزیر خارجه قطر در تماس با همتای ایرانی خود بر حمایت دوحه از تمام تلاش‌های دیپلماتیک و اقداماتی تاکید کرد که هدف آن دستیابی به راه‌حلی برای تضمین آزادی کشتیرانی و فراهم کردن زمینه توافقی جامع برای برقراری صلح پایدار در منطقه باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78057" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78056">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTVHJbmUZIJJeWx1YgYNcPoBKpRHVUh-JQ6X8aUT1xFhkPnBiloaQRxrwLi11hm3gL4S9GgFdnHSvzVxYOwWKh8g5jBinlA62SFIDU2jUgJ9xTBlc6Bt06m-bkXX4ttJIhY8uWChKzwLbuXwrvgDIfyeIZmkNijjuZ4vkL1pOqpd-KdyGA2oo9ESaqj9xBjxd0w_VlRQfWa-Z66VYx-kZ1FIKPOiLiCOHPfDYuK1TZ8kvgxiFhOKeXA1W1hEX0wvT4xi8neA7jLRzRkL9qiTilOOd7pktmZUuAVGgWN3mFx0Kc4_mj5zL1NFBGGPgd5M7ZfkA-mi1Wftu3jg1__0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه مدنی، پژوهشگر و متخصص ایرانی حوزه آب و مدیر مؤسسه «آب، محیط‌زیست و سلامت» دانشگاه سازمان ملل در کانادا روز چهارشنبه چهارم شهریور جایزه آب استکهلم ۲۰۲۶، معروف به «نوبل آب»، را از کارل گوستاف شانزدهم، پادشاه سوئد، دریافت کرد.
این جایزه در مراسم رسمی هفته جهانی آب در استکهلم به پاس پژوهش‌ها و فعالیت‌های کاوه مدنی در زمینه مدیریت منابع آب، حکمرانی آب و ارائه دیدگاه‌های نوین برای مواجهه با بحران آب به او اهدا شده است.
کاوه مدنی پیش‌تر در ماه مارس به‌عنوان برنده این جایزه معرفی شده بود و کمیته جایزه، از پژوهش‌های او در مدیریت منابع آب و پیوند دادن علم با سیاست‌گذاری، دیپلماسی و ارتباطات عمومی تقدیر کرده بود.
جایزه آب استکهلم از سال ۱۹۹۱ به صورت سالانه اعطا می‌شود و مراسم آن را بنیاد آب استکهلم با همکاری آکادمی سلطنتی علوم سوئد برگزار می‌کند.
این جایزه که شامل یک میلیون کرون سوئد و یک تندیس کریستالی است به افراد یا سازمان‌هایی اهدا می‌شود که دستاوردهای برجسته‌ای در حفاظت، مدیریت و استفاده پایدار از منابع آب داشته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78056" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78055">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vEsyIbkenhYfrHpOSW-Dz6w83jjQkgvnB7C9XmdqqBDa67p2784GZa_x14oMjt9gHfnnNFYrQTaIJAbG7Tx_oul4gFUGD618Nng7BC4QScFUvQkV9Zak7xgudBJXEwTmW8r97sgvElHCUPe2IfCmaQLcI0YrfJjdFP2YkLxGdTnTuv0awvdnVENAqZ4Iso2aU6dl1IYz9gHlXYZHqv3bC4_XUC65WAinUaJjq38FYZSmv4dkQWNefAiQ446fFPgGgu1wckAgKLLlVUQQF5_9bfOh2gAbdUKLKpIX5u3FhrN08XrJKOz035BWPDEjsBWSGSJISFWHdCuxRN8YTaZ1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلا ابوالحسنی، از بازداشت‌شدگان اعتراضات دی۱۴۰۴، به اتهام «محاربه» به اعدام محکوم شده و پرونده او پس از اعتراض به حکم، اکنون در دیوان عالی کشور در حال بررسی است.
لیلا ابوالحسنی، حدودا ۴۳ ساله و مادر دو نوجوان، از ۱۸دی۱۴۰۴ در زندان دولت‌آباد اصفهان نگهداری می‌شود.
یک منبع گفته است که ابوالحسنی روز ۱۸دی در شاهین‌شهر و هنگامی بازداشت شد که در حال عکس گرفتن از آتش‌سوزی یکی از فروشگاه‌های «افق کوروش» بود.
به گفته این منبع، دستگاه قضایی او را به دست داشتن در آتش‌زدن این فروشگاه متهم کرده است؛ اتهامی که به صدور حکم اعدام علیه او منجر شده است.
در حال حاضر، دیوان عالی درباره اعتراض او به حکم اعدام در حال بررسی پرونده است.
لیلا ابوالحسنی از زمان بازداشت تاکنون، بیش از هفت ماه را در زندان دولت‌آباد اصفهان سپری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78055" target="_blank">📅 17:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gGaFiLEqbpcLMnfl9jxMzdbykZMT5-uXGoQSmAR4X8dXsClE9i4XfCXHp2RQnFXQhgGwJtoHbiSeyDgk3G158NrXq5okGnCMZFJbtiLR1yd7TVjfYs7FYihUhCXttUjo2pnrnzF350ilnnKk41gztI-Q6nWT9wBtFLMfTlwp80Lf9ZByjVpXdzgz4GPA3N_DPJ0gGucZ4bSSRW13jVztcIrDB2xnjHsLpra0XLJsMsDDYAjC8vAYqHf0GXfn3PdE4xLHKNB31djBRBqw6ybCHq-RF12Yf-XgjQBoY2U8yYfDba39pIA9t8Tl9t0eLywrXN4lGZxEe88xI_2Qg9eo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
مقامات محلی گزارش داده‌اند که یک نفتکش با پرتابه‌ای ناشناس هدف قرار گرفته و در پی آن کشتی دچار آتش‌سوزی شده است؛ آتش‌سوزی از آن زمان مهار شده است.
گزارش شده که همه اعضای خدمه سالم هستند و حضور همه آن‌ها تأیید شده و هیچ گزارشی از پیامدهای زیست‌محیطی دریافت نشده است.
مقامات در حال تحقیق درباره این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78054" target="_blank">📅 05:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=vfYCx2klO5fZ1rQAmSidGET_1rEJjvg1CTkVt3ThjxuraShpfRA4yy2YlFdSq8gE76hWdj67OJrDKJvS5fNoMPKDwQGpS1rkedkiRpIp3ajyVSs7TQGTt1rZ0t1HzZKS5k4O_jSZjOVmIViIvsewxNYtR152IAcsNcOuOWsFkVUnhTOr6umEbM0HWadAd6CeqtFzqfXuO0j32i6Jemuq4gY6PV-nYHKcQ-snKI5GCPikcxqx2BPA9ydDiVDibtJs9GMkBT2Y3ZfIWVfIuh3KIYJGJ7vLGRzklh5EIKEya9qn0nGlwMSTEDjiuBjHO9UYKk20JNbni3V4UWfdiva6xA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=vfYCx2klO5fZ1rQAmSidGET_1rEJjvg1CTkVt3ThjxuraShpfRA4yy2YlFdSq8gE76hWdj67OJrDKJvS5fNoMPKDwQGpS1rkedkiRpIp3ajyVSs7TQGTt1rZ0t1HzZKS5k4O_jSZjOVmIViIvsewxNYtR152IAcsNcOuOWsFkVUnhTOr6umEbM0HWadAd6CeqtFzqfXuO0j32i6Jemuq4gY6PV-nYHKcQ-snKI5GCPikcxqx2BPA9ydDiVDibtJs9GMkBT2Y3ZfIWVfIuh3KIYJGJ7vLGRzklh5EIKEya9qn0nGlwMSTEDjiuBjHO9UYKk20JNbni3V4UWfdiva6xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح: رسانه‌های فارسی‌زبان در بانک اهداف نظامی ما جای می‌گیرند
1:11
سخنگوی ارشد نیروهای مسلح جمهوری اسلامی،  در مصاحبهٔ تلویزیونی با خبرگزاری «دفاع مقدس» مدعی شد رسانه‌های فارسی‌زبان خارج از کشور مستقیماً به «موساد»، «سی‌آی‌ای» و «سازمان‌های اطلاعاتی دشمن متصل هستند».
به گفته ابوالفضل شکارچی  «نیرو‌های مسلح جمهوری اسلامی به این بنگاه‌های خبرپراکنی به‌عنوان رسانه نگاه نمی‌کنند» و کسانی که در این رسانه‌ها کار می‌کنند را به عنوان «سربازان صهیونیست و آمریکا می‌بینیم و حتی می‌شود آن‌ها را در بانک اهداف نظامی خود پیش‌بینی کنیم».
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78053" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CU2nBtyNbP2lbUet_EBNwK_Hvpy7HvE0478beYQfDN0GNqH66cHPs_lxXWmmlBpF4Yf2eKFGtKtnLAlE4WK8GIYNc6rJROB2_A2uDGtNfKkSEk7MvYt0Uu9mojK-fEUKTh7G73AKtygx7Qhu0ET5jsGHNRJ4IHuOOH83q-W5Y94RV_XB5PqU97r757GkeK9zlMUJF3DcJCYdhZhB6kEC-5_EeDA-Gn-pUWcfFP9bAgh-pn-KBl9V_YzdY4Ijfv8eclgZFFVdakgfa0B1ayTzN-ua7xCM_mrbnN8oua-X2yhUnt1T0XL7XJCP_YJ5QG-SCfNViOzjCjmxBFIQSjQ2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bqtj7yYetk-2xbbuDoxO-rrV6gB9b6AQakXS7wRKoVRTjYWg7HgXCUFsCdwz25ezeHZ5xT4EohCJgfyYosq4jpfP1vtAoanq7xgF0b-H-zvcl-y52F5-3yhQ0mUol3wgz7SSdfLheazuvO8_M0lGU5dDWIMA1n-khWZCgQcmZAKzVUMAf2us_8ULx6vUNjfR38xEdd-foauKJ9FlAcAaGra9Mca5trUdHEtgjpbQutzs8LBtCW3U-XtV4WrxAB-IkI4NvmYc4rLBdX9HZCc-6CdC5oEQ11Ho5XhcQBvggbCZVnM5h1-fRrDlL6Wgs0v2KROJns5ygeJowh8d3aZU9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ درباره اعتراضات در ایران اعلام کرد «فکر نمی‌کنم وقتی یک مسلسل روبه‌روی شما باشد، آنجا بایستید؛ تک‌تیراندازهایی واقعا بالای ساختمان‌ها هستند.»
او گفت: «مردم هنگام اعتراض هدف گلوله قرار می‌گیرند و جمهوری اسلامی برای ایجاد ترس در میان جمعیت، لزوما نیاز ندارد تعداد زیادی را هدف قرار دهد.»
او افزود: «وقتی می‌بینید پنج، شش یا ۱۰ نفر در میان جمعیت ۱۰۰ هزار یا ۲۰۰ هزار نفری به زمین می‌افتند، مردم محل را ترک می‌کنند. فرقی نمی‌کند چه کسی باشید، می‌روید. وقتی افرادی آماده‌اند به شما شلیک کنند و شما را بکشند، اعتراض کردن بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.»
ترامپ گفت: «نیروی دریایی‌شان همان‌طور که می‌دانید، کاملا از بین رفته است. نیروی هوایی‌شان کاملا از بین رفته است. بسیاری از سربازانشان حقوق دریافت نمی‌کنند. فکر می‌کنم تورمشان ۳۹۰ درصد است و پولشان تقریبا بی‌ارزش شده است؛ منظورم این است که وضعیت خوبی ندارند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه چهارم شهریورماه، در مصاحبه رادیویی با گلن بک اعلام کرد که وضعیت حمل و نقل انرژی در تنگه هرمز به حالت عملیاتی بازگشته و حجم بالایی از نفت از این آبراه در حال عبور است.
ترامپ با اشاره به اقدامات انجام‌شده برای پاک‌سازی مسیر گفت: «ما از شر مین‌ها خلاص شدیم و این تنگه اکنون فعال و در حال کار است.»
او با اذعان به وجود برخی تهدیدهای پراکنده افزود: «بله، هر از گاهی پهپاد، راکت یا چیزی شلیک می‌شود، اما تنگه کاملا فعال است و نفت زیادی از آن خارج می‌شود؛ به‌طوری که همین دیروز ۱۰ میلیون بشکه نفت از این آبراه عبور کرد.»
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، چهارشنبه چهارم شهریور در مصاحبه با برنامه رادیویی گلن بک گفت فکر نمی‌کند مجتبی خامنه‌ای، رهبر جمهوری اسلامی، کشته شده باشد.
رییس‌جمهوری آمریکا اعلام کرد: «او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دستش، پایش، همه این قسمت‌ها به‌شدت آسیب دیده بود.»
ترامپ همچنین افزود حتی اگر مجتبی خامنه‌ای مرده باشد، جمهوری اسلامی «نمایش خوبی» اجرا می‌کند.
ترامپ گفت: «جمهوری اسلامی همچنان درباره مراجعه به رهبرشان برای گرفتن تایید نهایی در امور مختلف صحبت می‌کند.»
رییس‌جمهوری آمریکا همچنین افزود توافق با جمهوری اسلامی آسان نیست و آن‌ها «چندان پایبند به اصول» نیستند.
@
VahidOOnLine
دونالد ترامپ روز چهارشنبه چهارم شهریورماه، در گفتگو با شبکه الجزیره اعلام کرد که هم اقدامات اقتصادی و هم گزینه‌های نظامی «اثربخش» هستند و او در رابطه با مذاکرات با ایران «عجله‌ای ندارد».
او در پاسخ به پرسش‌های تانیا نوری، خبرنگار این شبکه، افزود: «من هیچ جدول زمانی ندارم؛ هیچ عجله‌ای در کار نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78051" target="_blank">📅 17:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KB2dyQ7HVd9Cg4OOeNsOp9PXvrEvMf7VJs0u3q7Huh8-QVIBpWeyuemj_0qPOozmeLtMAx9YjlU1Yx1MrLZWJq0f_sgmyq-Jub9juAU735n-gJkJuo6jbVqJ_cpxajzLhnOWncU7dF5wk6-iF35txE9_9em7v_GEJ8Bv3eBT7QhTyISn7HY8uuOiQ4klsPyR6WIZreJTxudboPY8GEF2nShtMKgtwGSdkv6wP7Ly38coi4z5OdSzKhsJGXl9KB1EIzNXjlO5dM6tszr4j9_qVsVS5QpDj_cBHt6UxPtoMOc26tJZ6f9ZEPI7-dbQLeR9O6BVGXYTmFe0m9HQ3wJYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، بار دیگر موضع قبلی خود دربارهٔ ضرورت پایان دادن به جنگ با آمریکا را تکرار کرد و گفت: «جنگ همیشه راه‌حل نیست. گرهی را که می‌توان با دست باز کرد، نباید با دندان باز کرد.»
پزشکیان روز چهارشنبه چهارم شهریور در یک مراسم عمومی بار دیگر ایران را «پیروز میدان» خواند و در عین حال افزود می‌توان با «تدبیر و اندیشه» از این مسیر عبور کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78050" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CF46TO_CmmSm5PRn8sN9dJkuh2MhjTcCUEfwZA2Eec_t4m7xXnNMtcOEVnmb8EXEuoqfZxe9AOW610Q6w-0Nvy4HdEXzMXmdyH-p0DLkMMzBys8AC5XtNWR6rDeFEgUCIpE0unJ77tfX-akrWOjv7fy6woCJQbD3ffAy0LrPgakVnLjD0t21bjZZqwH97aO0ZGjukxpOT2zc0amxnDZHBcE_dgTmMZZ3dc4KDMqu7hwBJLNNJMs0iv1DSbOOYP3rlYdwKxOxyks-g9bm9LsKL5YZjz6792kobh3XahH22LHM1DKUYaz0gRbO31EZJ9sDPKV_ZvFzynP9Loy7TVxAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری هرانا گزارش داده است که حسین نظری، شهروند ۲۵ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه اول دادگاه انقلاب مشهد به اعدام محکوم شده است.
بر پایه این گزارش، دستگاه قضایی جمهوری اسلامی آقای نظری را با اتهام‌هایی همچون «ارتباط با دول و گروه‌های متخاصم» و «اجتماع و تبانی برای ارتکاب جرم علیه امنیت کشور» محاکمه و حکم اعدام او در تیرماه سال جاری صادر شده است.
نظری، متولد ۱۳۸۰، در جریان اعتراضات دی‌ماه توسط نیروهای امنیتی بازداشت و پس از طی مراحل بازجویی و قضایی به زندان وکیل‌آباد مشهد منتقل شد. او همچنان در این زندان نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78049" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAI78v3jCSr3zxZo3e4nV12leqemef9TJcyXjRDDripy473S32HQAV5HB71ITcojpiQRu5D_RBTYXVKoizt_Ussu2v2rKdvc4SQMeyJty7NaSx1C2Ehhmh3-mou2tuc01qNQva8UhWpP08ZOKzHJ82rQgiUcZBncJbiGp8swJviwqg9pH1gFiPbqkc2SZvXex8SLcngpckGONKRoMSKqiaW0vuwxlTvrcnXBRfYUQQY2yPYcv61E2CPYZqYcl3-TzWLef-BxcFzKu0-KvNK4qZ1eABbTE2b2nNYcacO-fGTgoJXZTfC_TjiIPERwvw0M8iNDma3SUepxT28LCJr10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش وب‌سایت‌های اعلام نرخ ارز و طلا در ایران نشان می‌‌دهد که قیمت دلار آمریکا روز چهارشنبه چهارم شهریور کاهش یافت و به زیر ۲۰۰ هزار تومان بازگشت.
در لحظه انتشار این خبر، قیمت دلار ۱۹۸ هزار و ۵۰۰ تومان و قیمت سکه طلای موسوم به «امامی» هم ۲۱۰ میلیون تومان گزارش شد.
این اتفاق پس از چند روز افزایش قابل توجه قیمت ارزهای خارجی و طلا در ایران رخ می‌دهد. قیمت دلار آمریکا در این روزها تا ۲۰۵ هزار تومان افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78048" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=ehFjG-pYUX-_IPC3_Lqn449RU9q_KzmgZ_as3gImw9YNeixW0tEfgdcYdog1b0DJtqcpUHmw9F-QU9orGmtJ9fnHl_1Xs3S7M15dzVI63I_bE_h0zSwi-65Pnrx-J24E2VojiiBBUfidR014R0SWT2FIYVKNK4YfeYtqH4CeIYiUW2Gc2fBVE0-38HG72ZOO2VvyByWe8okVGnPg88-StjDRhpVQKWGdMa1DWACKvtIRyucUQ3pvHuziHueBD5ukVxr_iFdXlCNycDXoqMarcQAaVYoDVQqAJOKMX3V1-okTHKr5isQh50mgwBs7WZFFZ8OtKAaj10FcR7NlqeevGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=ehFjG-pYUX-_IPC3_Lqn449RU9q_KzmgZ_as3gImw9YNeixW0tEfgdcYdog1b0DJtqcpUHmw9F-QU9orGmtJ9fnHl_1Xs3S7M15dzVI63I_bE_h0zSwi-65Pnrx-J24E2VojiiBBUfidR014R0SWT2FIYVKNK4YfeYtqH4CeIYiUW2Gc2fBVE0-38HG72ZOO2VvyByWe8okVGnPg88-StjDRhpVQKWGdMa1DWACKvtIRyucUQ3pvHuziHueBD5ukVxr_iFdXlCNycDXoqMarcQAaVYoDVQqAJOKMX3V1-okTHKr5isQh50mgwBs7WZFFZ8OtKAaj10FcR7NlqeevGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: با «وحشی‌های» حاکم بر ایران نمی‌توان به توافق دیپلماتیک رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل شامگاه سه‌شنبه سوم شهریورماه درباره احتمال دستیابی آمریکا به توافق دیپلماتیک با جمهوری اسلامی گفت اسرائیل در اصل مخالفتی با یک «توافق خوب» ندارد، اما نسبت به امکان رسیدن به چنین توافقی با حاکمان تهران تردید جدی دارد.
نتانیاهو در جریان یک سخنرانی با اشاره به گفتگو با دونالد ترامپ گفت: «به او گفتم یک گزینه، البته، رسیدن به یک توافق است؛ یک توافق خوب. ما مخالفتی با آن نداریم.» او سپس با لحنی تند افزود: «اما تردید دارم بتوان با آن گروه، با آن وحشی‌ها، به توافق رسید. به شما می‌گویم: نمی‌توان به توافق رسید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78047" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQUi7MyEP9tM85pZEewpvVLZ4OOoczOUaSqQWX_sQFo44R1Mod34jfPd3fJDvbXm0REC7UwUoWc_yV02kJiBbxOgls8Mu5NZmg3lTwQ3haugNjRxw2iDL7FB5kzJ7zNgqOEhzhGCUOnsW1DL4EanxNs5MlVhiLAQQBmyt4N_ptlvCdGJkqs_GowD654lIr6dfpSGkICsCj4TY_dV7wpMnV7azJ1FskHwKKYZUtZsQmLsUn52G0MdsW5tZ9Cp5mC4tnutZCMPTX_ia4f9YzFO5YQKZjPK-vZgkDeuIjVGctk63BMVmFm9wKaPpSJvBN8WWbBJLrfTpKZaO-G9A-gQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیح شاهوردی، بازیکن پیشین تیم‌های پایه باشگاه سپاهان، در جریان اعتراضات ۱۸دی۱۴۰۴ در منطقه «خانه اصفهان» هدف گلوله جنگی نیروهای حکومتی قرار گرفت و جان باخت.
او ۱۹ سال داشت و تنها دو ماه به پایان دوران سربازی‌اش باقی مانده بود.
مسیح شاهوردی شامگاه ۱۸دی در منطقه خانه اصفهان از ناحیه پهلوی راست و کلیه هدف گلوله قرار گرفت.
اصابت گلوله باعث خون‌ریزی شدید داخلی او شد.
به گفته یک منبع مطلع، فضای امنیتی حاکم بر منطقه و شرایط آن شب امکان انتقال فوری مسیح به مرکز درمانی را از دوستانش گرفت. آن‌ها پس از گذشت چند ساعت، او را با پای پیاده به منزل رساندند.
مسیح شاهوردی حدود ساعت یک بامداد در آغوش برادرش جان باخت.
خانواده او با وجود جان‌باختنش، مسیح را به بیمارستان منتقل کردند؛ چراکه هنوز امیدوار بودند بتوان او را نجات داد. براساس اطلاعات دریافتی، کادر درمان پس از معاینه اعلام کرد که هنگام انتقال به بیمارستان، خون‌ریزی فعالی وجود نداشته و مرگ او پیش‌تر رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78046" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrBM_Y3d7Xw1-5p0g5CTuYLiIXuqV0GL0OS3mbAVNwCe732M-_zEBr2wsH8ARKgOcCsnrBNbfkUIu8rfV2nEKlSQGKmWQ2S_iB8uIBqbydR0VkfKMxaxVBqddgl3m781erKRpsJ8JB1JGAlBOiaq3DVEQYoR1FrHEetR_4FuqPzhhdYnfmKg3WfkhsRIew4uMe_rcVoBijaWoX4_G5jJCjSQYgKFIXc7x4Dk6PPJiLq4veLS9b6PJZ_dqeUt5OjspFy1TZi2FkC1ADwseONdcVusXGIR681XS4gc-Keqia5ZzviVvvRj95mG7aBbDwGRtgHQbG9E_OuTtRm_EabIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ با بررسی واردات گاز ترکیه، ارزیابی کرد که هشدار جدید واشنگتن مبنی بر مجازات اقتصادی کشورهای طرف معامله با تهران، این کشور را که متحد کلیدی آمریکا و سومین شریک تجاری بزرگ ایران است، در برابر چالش قطع واردات گاز از ایران قرار داده است.
ترکیه در سال گذشته ۱۳ درصد از گاز وارداتی خود (۷.۷ میلیارد متر مکعب) را از ایران تامین کرد و ایران پس از روسیه، آذربایجان و آمریکا، چهارمین تامین‌کننده بزرگ انرژی آن بوده است. با وجود انقضای قرارداد ۲۵ ساله در پایان ژوئیه، دریافت گاز ایران همچنان ادامه داشته است.
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرده است هر کشوری که به روابط اقتصادی با جمهوری اسلامی ایران ادامه دهد هدف تحریم قرار می‌گیرد و دونالد ترامپ در حال رایزنی مستقیم با رهبران جهان است. این موضوع احتمالا شامل تماس واشنگتن با رجب طیب اردوغان نیز خواهد بود.
بلومبرگ ارزیابی کرد اردوغان که ماه آینده عازم واشنگتن است و برای خریدهای نظامی بزرگ از جمله جنگنده‌های F-35 و F-16 به چراغ سبز آمریکا نیاز دارد، بعید است به دنبال خشمگین کردن ترامپ باشد. به گفته کارشناسان، در صورت قطع گاز ایران، آنکارا می‌تواند این کمبود را با افزایش واردات گاز مایع (LNG) گران‌تر— به‌ویژه از مبدا آمریکا — و اتکا به ذخایر پر شده خود جبران کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78045" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNQkazFezZSYdvjtLydB_kXvfqxqMeR0DseZ58RvjhOA18eL9xtMIDkx-kiHy9XVPfkZR4HuaTVtO0pUEmzLvHUzHxi0KEPW7A3lw0uuLD1Fnt_n6kly8T8EILxVFHDeOiNx40ncP_ZHnp93S6igFbwVsroa4IHEwP6BnSlgOKGcSyMVAbQ5DWOCU8_e6ISKzFMMyIX0QkymGLss_iLs1W9By7HKZzcF4wiUQiWJH6-IFSDxy4N7qQA9C808s-oOBO4atOJN1UTS_q6nzdSEhyJ957sxvjn3RtyUaGIBMeDpjQ0khWVStCb6MmL4tzJA5kbpI0wDU0TZbChDbgvn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان هیلی، وزیر خزانه‌داری بریتانیا، اعلام کرد دولت این کشور در کنار آمریکا و دیگر شرکای خود به اعمال فشار اقتصادی بر جمهوری اسلامی ایران ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با «فعالیت‌های خطرناک ایران»، اقدام خواهد کرد.
هیلی، روز سوم شهریور ۱۴۰۵، در بیانیه‌ای گفت دولت بریتانیا از زمان آغاز به کار خود تاکنون بیش از ۲۴۰ تحریم علیه ایران وضع کرده است؛ تحریم‌هایی که به گفته او در واکنش به اقداماتی اعمال شده‌اند که امنیت مردم و بریتانیا را تهدید می‌کنند.
وزیر خزانه‌داری بریتانیا افزود لندن مصمم است مانع از آن شود که جمهوری اسلامی از اقتصاد جهانی یا نظام مالی بریتانیا برای پیشبرد برنامه هسته‌ای و فعالیت‌های بی‌ثبات‌کننده خود استفاده کند.
او همچنین از تلاش‌های آمریکا برای دستیابی به راه‌حل دیپلماتیک حمایت کرد و گفت بریتانیا از افزایش فشار بر جمهوری اسلامی، از جمله در قالب عملیات «طرد اقتصادی» آمریکا، استقبال می‌کند.
هیلی تاکید کرد بریتانیا به همکاری با شرکای خود برای حفاظت از منافعش ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با آنچه فعالیت‌های خطرناک ایران در منطقه خوانده شده، اقدامات لازم را انجام خواهد داد.
وزیر خزانه‌داری بریتانیا از جمهوری اسلامی خواست فعالیت‌های بی‌ثبات‌کننده خود در منطقه، از جمله در تنگه هرمز، را متوقف کند و وارد گفت‌وگوهای دیپلماتیک شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78044" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OOsXndQ40VezqBe-v_a2XbwwLvvxDu7FvN-gl7Ot333RObC7rvLcxDANBE0f2KDF7KcUC-cawfqNuEvOhtUIMpRuEf0Q75JfyZyzVrKGGMaAIrr7-7tbWkmOX9xhgjKPoNGqdWgzE5j4qd-z5S1EykfcA70nFgBg2hMQQm67Sq12nskHXORvT_8DzI6zPtkLT56qOyGEVQHDDGtDWLQ0-hYERmhkT_Zr4qjUPKrmrFL7vnveI4tO5pOkfsJ7nLqjK10SR-Qr0pI2RmVgB0BrZBgt04zVV0Tufdb9IGb9J7xUUScG7B8GHV3rGVyZH3TaXpkMwalOTV6mPWmE28GVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، سه‌شنبه سوم شهریور در شبکه ایکس با انتقاد از عملکرد وزیر خارجه جمهوری اسلامی نوشت عراقچی بر اساس کدام مجوز از دستور مجتبی خامنه‌ای مبنی بر «انحصار» مدیریت جمهوری اسلامی بر تنگه هرمز تخلف کرده است.
او افزود چرا وزیر خارجه بدون ملاحظات امنیتی اسباب محکومیت و اجماع سازی علیه جمهوری اسلامی، به سبب «اعمال مدیریت لازم و درست ایران در کریدور جنوبی» را فراهم می‌کند؟
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78043" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uC2CPNbRWI9QkkMbpMIfd7UFF4NoggPUw9JzJwCuA_ZTMrB5scN4tMSbh72zrJ6hokalV1uETeQPW9EOrgspX_nTj_pGN3KTN9jwS6B_iYTIWzFv6oFw2joMR1oa2illKlzRfpbMqMEiuiz3AbBZiuxk6uArDa7cAuZghemBRyKZTQmra8vk_WrTLe0T4_SXJampESYUR_PSGYF94Ys1WgPaZvzrtXhgY8XD7ajGEwuzhrKrN3wxNQRUuKXMTRYXt5edqHG9Ia5an9m-sTu0y71pE-WxJXCTP1IjY3UXVzSxsq31ibvqpamSo2_aLzdrb_Uu5y6bsVQl4T_3NiwmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با انتشار بخشی از ویدیوی نشست خبری اسکات بسنت، وزیر خزانه‌داری آمریکا، در شبکه اجتماعی ایکس، با کنایه از اظهارات او درباره تحریم‌های جدید علیه ایران انتقاد کرد.
در این ویدیو، خبرنگار با اشاره به ادعای بسنت مبنی بر آغاز «روز دی (D-Day) اقتصادی»، از او می‌پرسد چرا تحریم‌ها بلافاصله اعمال نمی‌شوند، و بسنت در پاسخ می‌گوید: «چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟»
قالیباف با طعنه به این تناقض در سخنان وزیر خزانه‌داری آمریکا نوشت: «او ابتدا می‌گوید روز دی اقتصادی! اما پنج ثانیه بعد می‌گوید چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟ جناب، اینجا ساحل نورماندی نیست؛ این یک نمایش کمدی است و شما فیلم‌نامه خودتان را هم فراموش کرده‌اید!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78042" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p6Asuu2z1X5kJ1r4lqSUnjVbf5-buPTaiV_tl8_Ixi-hQZXnfNWUttxNql2_Y-dRcmQbo_ksRwyPvJ-sQfKhw7nK65zaWdq_jDfFmT5OgqQV-MEq4oHspTzGHs2gpFCB5zIIYBF-DxbwuLkGp1ulhCAYuKViM4zN3KgPFlcx5-TqxSIjlBHhTzwWpwhV3qFvzXmyvlF5pl0IPMEW2glyeU5QcsDzwBr0MNW7T8Q-Ic7H38yNTiTm54STyba1QoFZebWjHZtYGSUnsUx7xsvCP7UmI0s33-go1jfX0a2WVv9MMZ3Zp_HB0JhB_9jK_CFvwtOxz_6GoPPHweM2QDVPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pQ4havTmdlCdZh5ZKYCejalWxAMAwo3JTm0TpB8LuOU_BJxTvSY2M8ubHP2j15fxp60n2cM_G4fnlX1POz3LLEoL1S1Lulqk07XFYEKk8p_UvBhtJYNeKK1pRILZkC1cUpCcj-zaMIUrCzwsg8iHAxvWNIcc3y6RKfTSM7Zo3EiSbyM6LFdj6YkcDrq12g9p7yQ4Djcz4Jg1naG1Hp5MWhLTX-M5oI81Wdpg307Caq3Ye64aAEbAaSh4XXg1KFskZtq4ix3UD3UfXHtArx4nRzAs0EbKu5alj2fyLehOEXR6T394TtWL34oO6LLrF3AOkBpAYkWycgJ88PHvIQmc6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو منبع آگاه به گفت‌وگوهای مارکو روبیو، وزیر خارجه آمریکا، با مقام‌های کشورهای مختلف، به کانال ۱۲ اسراییل گفته‌اند واشنگتن در حال حاضر انتظار ندارد حملات تهاجمی جدیدی علیه ایران انجام دهد و تمرکز دولت دونالد ترامپ به افزایش فشار اقتصادی بر تهران و تامین امنیت کشتیرانی در تنگه هرمز معطوف شده است.
به گفته این منابع، روبیو احتمال اقدام نظامی آمریکا را در صورت آغاز دوباره درگیری از سوی ایران رد نکرده است.
این تغییر رویکرد همزمان با اعمال تحریم‌های جدید علیه جمهوری اسلامی و ادعای دونالد ترامپ درباره پاک‌سازی تنگه هرمز از مین‌های دریایی صورت گرفته است.
بر اساس این گزارش، دولت ترامپ قصد دارد در مرحله کنونی فشارهای اقتصادی بر ایران را افزایش دهد و شرایط را برای عادی‌شدن عبور و مرور کشتی‌ها از تنگه هرمز فراهم کند.
منابع آگاه به کانال ۱۲ گفته‌اند انتظار می‌رود این رویکرد دست‌کم تا انتخابات میان‌دوره‌ای آمریکا در اوایل نوامبر ادامه داشته باشد و پس از آن، احتمال بررسی گزینه یک کارزار نظامی گسترده‌تر دوباره مطرح شود.
@
VahidHeadline
پیش‌تر:
پایگاه خبری اکسیوس به نقل از مقام‌های دولت آمریکا گزارش داد انتظار می‌رود تحریم‌های ثانویه گسترش‌یافته، دست‌کم تا پس از انتخابات میان‌دوره‌ای آبان‌ماه مسیر اصلی اقدام واشینگتن علیه جمهوری اسلامی باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78040" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjKag4E6Rt2RHUV38wtBSDjwacL3jb4cqacUXlGdLsH0fiyl93gSaLBX0By0YveMPBtVGJSoIB8Cxyrt736SrYAH6o7T453pBG6o7ypZdbgFIHn0v-Sll3owi59AIQLRZ91WyJTQIkjKbF7JFnYu-kHH0f0pRH3ia7SpFRWHbHTuylj5U7Cq83pD-EEZBaJPQdDOHGJKefoad_ycW5p5hsYVl0ve4_bGABSoRi62oRVo7zuD3Ya2BQETmWmKHSRfmVJwr7vRYxEtRb4sKfdsVokhzQTmJgqSZ5E5b45QVbg3gNtTOKCJ_mjnk4IRMgz6Iq68TiZ9PlifhY3BU_Azhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی نیکزاد، نایب رئیس مجلس شورای اسلامی، در گفتگویی با خبرگزاری ایسنا از کاهش دو سهمیه بنزین بر اساس آخرین تصمیمات مجلس، سخن گفته است.
به گفته او سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان محفوظ خواهد ماند اما سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا خواهد کرد.
همچنین سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان هم قرار است به ۱۵ لیتر برسد.
او البته گفته است: «براساس آخرین تصمیمی که درباره بنزین گرفته شد، مقرر شد که قیمت بنزین افزایش پیدا نکند.»
اشاره او به بنزین ۱۵۰۰ تومانی است.
آقای نیکزاد تعیین نرخ چهارم بنزین را رد کرده است.
دیروز رئیس دفتر مسعود پزشکیان، رئیس‌جمهور ایران، هم گفته بود سهمیه بنزین حتما کاهش پیدا می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78039" target="_blank">📅 22:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CdLZBqRSzY99xxvr-isV7zxw4RHHR8mjs_pAoWaNgvPgoS4qG3MPS7nK9PtPclmHHRuSd7H5fhSneRKWmUVACKMxEu1EVjkJS_2Q6iA4OCy7jE9omA2uNY0kjbzduw9n854P2M2-uXoR7m9Agt172vEW7OwF2hFZWHr3H59mvccNEvrAp5Og1M_ghv6A0u96l5_nMAJr7NSi2NrEMFjgmIExXlgt6BL4F28VNKImX4peXNJFfYSCVyjULhDb_BAJ8knAx5WVfXRA6ObotwyG3xiJSqdrNsulvtYpzvIgjzTTP1YEhJpFJJeSic0Qbi0-XIhDLyYnGYuRepXLm36TuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BqBaJThrb-0QW94uS7OaAZb5BIzti0gki_ShjZySUk_Pa0EanGgddoOLl2Zk51lSxltb_CftXtvjE8t0SBjt8zKecT5qH1UsKaM6qbVx_Y2WSjc8QgvZCyb2Gcj2-V8AQhI3F_57lnNy7Kq-Pyr8CjepLsvHMP-yWe9jj1VR4Bh63X_6jM9SfiR8vCN2nWuyAXN5XssqgbabumT-Dej8RXXrKiFFg4uEprJGoRorlBVljf_aOEBTOpByvAavqnN560kFWPH1Eg0FjOFdmk5uka7JoNmRFBwfMi4nzWKLPINnTiSRhyr1YHvDZ-hIgAfOLIvz9P0Thj3m5iqHS_2AWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iEDBv4WxYK7o8vX4oXdWxViFh50xfMWTCPM7gaSgB_xio85CMDoVDf_ObGiRvWU3RjVj4-KWAugWMbMcJVwNmaU7S2JC_r_WOcYKw72pyLvmGwlKyyXYgoYiQpZReRFKnKyQCDtVFtSw_7hBwZotxEjFk4eD8bIAKbGWYxegAkj7pAgbeFIBxgkLazXvrPqIBrmkpLDKQxLBi17yjMoJ5iXysGVuvF9pgJnRIJELJyPWeKPuMLEsIZf2OMIecdLYULudYZBoJxw7GO6K6jUW_3c57yCyunW2LqO3ZoYqIQWEAK9Z87Y1fW8cm7dM4Gx5fzM8MDUrl735UmYi0pVFSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست اسکات بسنت، وزیر خزانه‌داری آمریکا،
ترجمه ماشین:
رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78036" target="_blank">📅 20:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqFCxGinvH56i36-hViUPFNuym-mfpDYG8U0Z51hyDYDreC9VOlE4XkvD88mv8dAFRfaXCDj8TMz32dC_qsRUZBD3-0t3FrV9L3wYnX6ceFPQcYJMZ_SdL0nGulesvM6HFE8j7j8wh4oM6iX31bCCHkWyVfIlbaSY4OX5AAPAsfgNNP-xnaKNIgC_kECZMTHv1lgV4dQf9OJRP6pntnJxUI4QhKqfLgkcrlIbpUEtPVGCC1OuDzJ1CS9zQ5fZglHEzAVX6TnXlLwbYxefVb67ftHS6uiP7Jm-VbfnzUZSQ3Bf4voOavbOcohTWB2IvdOaxC2tV8yPK6dXaDiznuIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه
بیانیه
: گفت‌وگو کردیم که مذاکرات ادامه داشته باشد
در پی سفر بدر بن حمد البوسعیدی، وزیر امور خارجه عمان به تهران و رایزنی با عباس عراقچی، همتای ایرانی خود، دو کشور بیانیه مطبوعاتی مشترکی در خصوص از سرگیری دریانوردی ایمن از طریق تنگه هرمز منتشر کردند.
بر اساس این بیانیه، وزرای خارجه دو کشور با تاکید بر حفظ حاکمیت و حقوق حاکمیتی خود، درباره چارچوبی مرحله‌بندی‌شده و قابل اجرا برای مواجهه با وضعیت کنونی تنگه هرمز و پیامدهای ناشی از جنگ اخیر گفتگو کردند.
چارچوب پیشنهادی شامل ایجاد یک گذرگاه دریانوردی موقت مشترک از طریق تنگه هرمز و اجرای پروژه‌ای مشترک برای پاک‌سازی تنگه از مین است. طبق این توافق، مذاکرات فنی میان تهران و مسقط برای دست‌یابی به کریدور دائمی، مدیریت ترافیک، تبادل اطلاعات و ارائه خدمات دریانوردی و امنیتی ادامه خواهد داشت.
همچنین دو طرف بر اهمیت گفتگوهای مشترک با کشورهای هم‌مرز با خلیج فارس، رعایت حقوق بین‌الملل و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78035" target="_blank">📅 20:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4CsXLqte540m2C5EjRy1X3BOOj2DPtfGl3Ba91Po-X-pntVKq-VqznCsUlytJ90sDJQXCSI7vmcB1zdlNDxX8L6K276FA2dkjEa27qDdK3Di7bEL16j47rBmu6kfkKrmdxy5qodwCNCylWfHWw3nXL7ViIG6-g6rA4Xg_6-DbE1wOO-YotB9xMGPRKHYyFkkUcV8PLGuO78qXICRaJuYxS5_WZkA72idE6_2yB2-eTWJIs-NIwMjBK7Ss0Bhgg6O_zfzoAmfH-wO-iYZWk8vxhEKhXxfuPyiyJ3_BLhfNPTz7L1a_Y3EqVDaR3t3jYYEME0j-GDE44p4t3MS6qRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها و ویدئوهای مختلفی در شبکه‌های اجتماعی از «تعطیلی» تعدادی از جایگاه‌های عرضه سوخت در تهران و تشکیل صف‌های طولانی در مقابل پمپ بنزین‌ها منتشر شده است.
برخی رسانه‌های داخلی از جمله خبرآنلاین، خبرگزاری دانشجو و عصر ایران نیز تعطیلی چند پمپ بنزین در تهران را تأیید کرده‌اند.
در همین حال فریدون یاسمی، مدیر منطقه تهران شرکت ملی پخش فرآورده‌های نفتی با تأیید تعطیلی چند پمپ بنزین در تهران، «افزایش ناگهانی تقاضا و ترافیک مسیرهای مواصلاتی» را «منجر به تأخیر در ارسال محمولات و اتمام بنزین در تعداد محدودی جایگاه و بسته شدن چند ساعته آنها» عنوان کرد.
به گفته او، در روزهای اخیر توزیع بنزین در تهران «۳۰ درصد» افزایش داشت. یاسمی مدعی شد «تأمین سوخت تهران به‌صورت پایدار در حال انجام است.»
خبرگزاری فرانسه نیز روز سه‌شنبه، سوم شهریور در گزارشی از تهران، از تشکیل صف‌های طولانی مقابل پمپ‌بنزین‌ها خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78034" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8mqpOzGGSoZRrTFXaFBI3W7jl34mEujvb3nAqJX4UVXKzF94AGx3gKBJwLnoy080lVr-l1DvBkisNf_qZ4gYLDQy7F6XoOYp_Xkx6Mlr7o5cCTZj_S-0VdJzfwD0flvRGPv0vXxnFFcuCqthR_FIPl09nY0pF0RS1O7CtC-dktcRSbCsCyjdA4RaQF9U63qubmENuE7uy8dd37MZQNAnPv9RVLusbdDdMwiLAhPRTlvBk0BI6URj1AreJyp2ECt8o1101VbzexyvOZOCxiMxqWWmv8MdxBpCiTr6lfygkoea7xvkBjHxU3FKXKOTeh5mHEMLkly1ks8WcZTFqsKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، چند دقیقه پیش:
همین الان نیروی دریایی ایالات متحده به من اطلاع داد که همه مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدید کار بگذارد، فوراً و به‌طور نظام‌مند نابود خواهد شد.
از طریق نیروی فضایی، ما تک‌تک وجب‌های تنگه را زیر نظر داریم؛ همان‌طور که کوه پیک‌اکس و سه سایت هسته‌ای دیگر را که پیش‌تر نابود شده‌اند نیز زیر نظر داریم.
سیاست «تحمل صفر» در قبال مین‌گذاری به‌طور کامل برقرار و لازم‌الاجراست.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78033" target="_blank">📅 18:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHCL1Ax0LyRDbjkpHm9tykyUo_rZODJhORQhqrMGUWP-N_AYBI4oR61IpeWiI6BIjT8xc27QcLz6iATS0LNKNtWjrM1gRVC9qxB7NAGRgzXqMANscw0pznw9CyAmTmriENcamGNZedXS1YHuHKYUPfUWiRGzMJAsauX6YN9ZP8B49RQCkd0SjTfo2enKR5A_NK9WsgljbEAu3_9ki2m0Xkw6T7Ed5gTbqyMCR6EizxPW6SknDSOwT0CejK0Kl0mah4aI2HxtvNy1HHkoZbI0hxbTSbwGfLUCv17aLQTyrdPMen-EPM3MTm-AoOGshAjhgIVlJ936sJTrz4YFgfcInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند ساعت پیش:
جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78032" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibT3sv3J4ulEp9WsevYfGertnihHcLNYxZwvIeBdWgtpAdquYmE2MGWzn1ULkg2R72yVJGFmh60ucBHiLYh1K3XDQkYQx_1ZwdysTITiaAKqY5zsSCKhIrmy-UMIE7jRjh6WSq4FTTYoXEwB1u7JWW1I5JhyU7jMdI0zJLhIFYROaW-lHgXahCc5ETnYIg_D6F3eIiT1aEasEJ8d5FR2H3hDp7RYoee6lGccn6CU4phsjW3j1VST9bwaT3Dr1xRmhn7Kga1Ywamv2KYcddDDaqHWXI0k1L91WyRRcvjyNHQ-tYoydy-ZFdhw1QkOuWh7YMDKbP47wNoKRPweTcFACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز سه‌شنبه سوم شهریور ۱۴۰۵ به ۲۰۵ هزار تومان رسید و سکه امامی نیز با قیمت ۲۲۴ میلیون تومان معامله شد؛ رکوردهایی تازه که ادامه سقوط ارزش ریال و افزایش التهاب در بازارهای مالی ایران را نشان می‌دهند.
براساس قیمت‌های اعلام‌ شده، هر پوند بریتانیا نیز به ۲۷۹ هزار تومان رسیده است.
دلار در آغاز هفته حدود ۱۸۶ هزار و ۵۰۰ تومان قیمت داشت و روز یکشنبه برای نخستین بار از مرز ۲۰۰ هزار تومان عبور کرد. بر این اساس، بهای دلار طی چند روز نزدیک به ۱۰ درصد افزایش یافته است.
سکه امامی نیز که در ابتدای هفته حدود ۱۹۱ میلیون تومان معامله می‌شد، با افزایشی بیش از ۱۷ درصدی به ۲۲۴ میلیون تومان رسیده است.
جهش قیمت ارز و طلا یک روز پس از اعلام بسته تحریمی تازه ایالات متحده علیه جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78031" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HhMrUCdFzXxQFSSXBpDCHSiizvtkjEd_P2EsCI57A8kcLWWwjLTUyPYBZ51muj0zZgG0v2w-EHZvk0J-Ybghs9lxOy7rNXXj8F1fdkvOIZ4TjNPj8wIHXp-eE6BUYa1IPABx_e9-8KRciAQ-omrPqJFD6-yNN9Cb8nvo1AizY4cIStFXHa25hu3yz07bujBHCr41oZ0IK7V4bfY3gkbr-2bP1OQYBipa6eN32rtjUP2v4YRuqObxA9r8Td1yUI4810WpgN-h5evTOCrlmt25Vw882AZR_cBUni8UtpYHsZpVbB7XQ6wVKu5kafIlJqn9okYJob4QCtcEoHS8b2oipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتایون ریاحی، بازیگر پیشین سینما و تلویزیون ایران، از تشکیل پرونده‌ای برای خود و ارجاع آن به بازپرسی دادسرای فرهنگ و رسانه خبر داده است.
این بازیگر با انتشار تصویری در اکانت کاربری‌اش در شبکه اجتماعی اینستاگرام اعلام کرد که پرونده‌اش به شعبه بازپرسی دادسرای فرهنگ و رسانه ارجاع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78030" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g677o4P_h5eUpW7Gy9yUNRqVCd_EZ0GOCQAG9866WnnR4Gn9qZQOAI8CMNhjQM0jrHnpgwv6ogmeEVVWMoRhPDgwx-Drt12hvYdDmz7fnQNaQ_zCwsYqcgAKxylqHwINlwysT01NgHlK5ChlH5yuvk3MGyXD-0OguoSxX0_tsYK5i9TttWr0B8qpt0V6vrmwJ5Bnby0QwdjA-Ru91Gus3_6ZMkePwr08L4DVEoHDZ2rf-VjSzWVwlT9ewLMjs2uA9DA74G0AHfV_OcqjKYByRHYgl1oH5tuxrhVfqXLS8Jqn-cevvDfDxwqO_fbjg4rmDRHYloRFtR4GHvfIe-XBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ade157391.mp4?token=bnbUwOazA5m7tfgW9nOK8l4RI4AxmAb6wk2M3lvBlCD47HOaFBEbB663DKZ9m8njRWlAR1M07UUr3Asb3n57_9IJUUpPpZKsBf6HkFYEOelMwz3UYBmYte-GXpI2iZoP9NwvKYekO75u1XdK-Sed913uEiYOaH_BbSFsiVZ414ZUHvW0FzYVWdZeLDOXwafevqu0gRsKcphWjHuxdpL8VTfdP8VLUTgGM27AHrQA7Y6JpWAeujrIJ4fl5RzEti6TueFxO3K3RYPXgBAcAA-4gNmQCXz3a_wD_LWio8vcRA-L4pC46hD_R-R_VUUM7OTu5JVyTsivI71BZlBV3xNVXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ade157391.mp4?token=bnbUwOazA5m7tfgW9nOK8l4RI4AxmAb6wk2M3lvBlCD47HOaFBEbB663DKZ9m8njRWlAR1M07UUr3Asb3n57_9IJUUpPpZKsBf6HkFYEOelMwz3UYBmYte-GXpI2iZoP9NwvKYekO75u1XdK-Sed913uEiYOaH_BbSFsiVZ414ZUHvW0FzYVWdZeLDOXwafevqu0gRsKcphWjHuxdpL8VTfdP8VLUTgGM27AHrQA7Y6JpWAeujrIJ4fl5RzEti6TueFxO3K3RYPXgBAcAA-4gNmQCXz3a_wD_LWio8vcRA-L4pC46hD_R-R_VUUM7OTu5JVyTsivI71BZlBV3xNVXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس پلیس مخفی ایالات متحده که وظیفه حفاظت از شخصیت‌های سیاسی در این کشور را بر عهده دارد در بیانیه‌ای که روز سه‌شنبه منتشر شد اعلام کرد از وجود ویدئویی «که به نظر می‌رسد بارون ترامپ را تهدید می‌کند» آگاه است.
اشاره این بیانیه به ویدئویی است که گفته می‌شود در شبکه سه تلویزیونی حکومتی ایران نمایش داده شده و حاوی اطلاعاتی از محل اقامت و رفت‌وآمد بارون ترامپ، کوچک‌ترین پسر رئیس جمهور آمریکا، در شهر نیویورک است.
سخنگوی پلیس مخفی آمریکا در بیانیه‌ای که به شبکه سی‌ان‌ان ارائه کرده تأکید کرده است که این سرویس درباره هر تهدیدی علیه افراد تحت حفاظت خود تحقیق می‌کند.
شبکه خبری سی‌ان‌ان در خبری در این مورد نوشته است که از زمان کشته شدن علی خامنه‌ای، رهبر سابق جمهوری اسلامی، رسانه‌های حکومتی در ایران بارها مطالب و ویدئوهایی درباره طرح سوء قصد به جان ترامپ و خانواده‌اش منتشر کرده‌اند.
حدود یک ماه پیش نیز خبرگزاری تسنیم، نزدیک به سپاه، ویدئویی منتشر کرده بود که در آن شکاف‌های امنیتی پیرامون ملانیا ترامپ، همسر رئیس جمهور آمریکا، بررسی و درباره راه‌های هدف قرار دادن بانوی اول آمریکا بحث شده بود.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه دوم شهریور ماه، در جریان یک تماس تلفنی با برنامه زنده تلویزیونی در شبکه ۱۴ اسرائیل، در پاسخ به پرسشی درباره تدابیر امنیتی برای حفاظت از پسرانش گفت جمهوری اسلامی یکی از پسران او را هدف قرار داده و تلاش کرده است او را ترور کند.
به گزارش تایمز اسرائیل، نتانیاهو بدون ارائه جزئیات بیشتر گفت: «ایران یکی از پسرانم را هدف قرار داد. ایران سعی کرد یکی از پسرانم را بکشد، به قتل برساند.»
نخست‌وزیر اسرائیل در دفاع از توافق خود با شین‌بت برای تامین امنیت اعضای خانواده‌اش گفت: «بنابراین، امنیتی که آنها دریافت می‌کنند یک کالای لوکس نیست.»
تایمز اسرائیل نوشت، نتانیاهو با اشاره به توافقی که بر اساس آن امنیت پسرانش و همسرش، سارا، دست‌کم به مدت پنج سال، حتی در صورت شکست او در انتخابات آینده، تامین خواهد شد، از این تصمیم دفاع کرده است.
او با اشاره به مهاجمان احتمالی افزود: «بدون این امنیت، آنها موفق می‌شدند.»
مشخص نیست کدام‌یک از پسران نتانیاهو، یائیر یا آونر، هدف این سوءقصد بوده‌اند و این تلاش چه زمانی و چگونه انجام شده است.
آونر در اسرائیل زندگی می‌کند و یائیر که از برادرش شناخته‌شده‌تر است، بیشتر سال‌های گذشته را در میامی گذرانده و به اظهارنظرهای تندروانه شهرت دارد.
بر اساس گزارش تایمز اسرائیل این تلاش در زمانی رخ داده که یائیر نتانیاهو در اسرائیل حضور نداشته است، اما مشخص نیست که آیا او هدف این سوءقصد بوده است یا خیر.
در این گزارش تلویزیونی همچنین آمده است که طرح ترور ادعایی چندین ماه است که برای نهادهای امنیتی اسرائیل شناخته شده، اما مسائل امنیتی مانع از انتشار جزئیات آن شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78028" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKzW8jrMcjdMKd5XJDbaCb7YXi7gfbLW7NiuWTTqYWisD1-MU_7AkZuOPV-5x5-smFQr2GgZw4GEipz-gJyXIU_ptQtA7L6Cxa3Ew_TvfXWR01ZdyHoy2i2SIsHOY_1vkrOF-i4HTJyCA_8fNrZrbin0i5AxioHTJPnKkgBadP-ciBjUGVTeXCGKRbysLsIzQu6vSNq5sO3dQLdjBpFbkdl7Td2Lxrx8yOoKupEEehnlTaoM3vvr4Sxe3wzltlyXrRBaYOT9Nqg0qGXXsFNCwFxwNSCk8-Jl2aGTI6uGfVoxFXEtNaG4pj1p3Cr7X8k-ggXwjsf8V0U3X25Lj0jYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه چین در واکنش به تحریم‌های تازه آمریکا علیه ایران اعلام کرد همکاری پکن و تهران در چارچوب قوانین بین‌المللی انجام می‌شود و «نباید با دخالت یا اختلال روبه‌رو شود.»
لین جیان، سخنگوی این وزارتخانه، روز سه‌شنبه سوم شهریور گفت چین تحولات را از نزدیک دنبال می‌کند و برای دفاع از حقوق و منافع خود «تمام اقدامات لازم» را انجام خواهد داد.
او در ادامه تأکید کرد که چین همواره مخالفت خود با تحریم‌های یک‌جانبه آمریکا را ابراز کرده و آنها را غیرقانونی دانسته است. به گفته او، جنگ اقتصادی و فشار حداکثری «تنها به تنش و درگیری بیشتر دامن می‌زند».
آمریکا روز دوشنبه تحریم‌هایی علیه ۶۰ فرد، نهاد و کشتی مرتبط با ایران وضع کرد و هدف آن را قطع «راه نجات اقتصادی» جمهوری اسلامی خواند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی را که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
چین خریدار اصلی نفت ایران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78027" target="_blank">📅 17:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sn3QHV5X72ZG2UvE5m3xzvuogDGa0HWqMWUWj9IOirxMCjv9jgjJgc_TpuMiLeF6c-jndn8kLUDPRCF5YGgSejwdw96EyEOVNhLqZGtzHS3b5RqgONR1MehQaGdNbFj5kNVMSKJFiMaLWAyIB-NqMldsXiZWqVEBF8PRL-0QcTAQYJ7BUzpOEOg6Mm75t5YOFcTZiomjhpAJQH8vSd0CnwiNDtYs9fq4CE-tbqQinPuKPylzrMDFhiUBHVUYJWAUovlMO78dZXZCB8-tyyFmP2nhgRHqhOY-WL33cqbFch_SG_VZiDTsL3RWl9chQ5yqfCqko3wjJHt_F_0L7wZsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی پیشه‌ورزاده، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در رشت، از سوی دادگاه انقلاب این شهر به اعدام محکوم شده است.
کمیته پیگیری وضعیت بازداشت‌شدگان
خبر داد که شعبه دوم دادگاه انقلاب رشت به ریاست قاضی محمد‌علی درویش‌گفتار این حکم را در مرحله بدوی صادر کرده است. پیشه‌ورزاده در جریان اعتراضات روزهای ۱۸ و ۱۹ دی‌ماه بازداشت شد و اکنون در زندان لاکان رشت نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78026" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=J84zDtWoqvPvr00Xmu2QET25rsXu90JEgKZV3Rif5-oKi_ljgnEOUYsWjVwwSn4U8x1UMuJfM2et45oPlEYGzWgjwXTvd9m2tWWh0KbXvlx37XnxxS9i3TWbMxofwdcRAoyVrcSsr0XoDC2hECFpux_4_mmtbwIuK3iQnkz9Xf1HLsxFPsUwv3yBNIjThCy6Dt9klw5dMqeIm3csbVi-1eHDXVpvRLjAB98b0e3KQd4dJyQ16h8baTpv3SKnt2tbKKjTSb2_8X6oVTu3oHFK0xJkxQZkmac5oL_1uJNDw-nzNmGa2jgB7OkGYfxhBbuZnGGT5gm1oaeTDAUlp1bUNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=J84zDtWoqvPvr00Xmu2QET25rsXu90JEgKZV3Rif5-oKi_ljgnEOUYsWjVwwSn4U8x1UMuJfM2et45oPlEYGzWgjwXTvd9m2tWWh0KbXvlx37XnxxS9i3TWbMxofwdcRAoyVrcSsr0XoDC2hECFpux_4_mmtbwIuK3iQnkz9Xf1HLsxFPsUwv3yBNIjThCy6Dt9klw5dMqeIm3csbVi-1eHDXVpvRLjAB98b0e3KQd4dJyQ16h8baTpv3SKnt2tbKKjTSb2_8X6oVTu3oHFK0xJkxQZkmac5oL_1uJNDw-nzNmGa2jgB7OkGYfxhBbuZnGGT5gm1oaeTDAUlp1bUNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع آمریکا می‌گوید اعلام کارزار تازۀ اقتصادی علیه ایران، به‌ معنای حذف گزینۀ نظامی نیست.
پیت‌ هگست که شامگاه دوشنبه و پس از نشست خبری اسکات بسنت وزیر خزانه‌داری ایالات متحده صحبت می‌کرد، تأکید کرد که «به‌هیچ وجه گزینۀ استفاده از حملات نظامی در تنگۀ هرمز یا اطراف ایران را کنار نمی‌گذاریم».
وزیر دفاع ایالات متحده در عین حال ابراز نظر کرد که ایران نمی‌تواند فشار اقتصادی تازه را تحمل کند.
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78025" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CBPhG2bmbcOcGMUeGAjvDRHGp-XztYTBeR7CaTKgpc_LlZxCHk66XbKNwb3E85htlPP3xxFBCBX4AqMxBJTQQWO9YKKyzIFcn5NRiqkZ_6S1QJNWPmca21uIKMbKmZGyrOAeBkFH8sQhfkbwfA8TkCUIwOw6fWyB5x47hrryFtSIQJpa7cjS7KID4Di5LOVS6gA5AfguYaYQTXwZQo8FtZtZ-TydM5qT0Uel1QKIVNnv8a-1f5YHtYV1LcLo7nrXkRhHi9qjwc_TvFKtlkKbSPt1v6x600TQfOF-REQNuai4ZegWYU-uZeLyg0qpPYIVK9k-sjvFv_VVhrVJ1HANOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pIFLycWBkhiBer0vvGDBIKX6dbrzymHh-AcaF1pQQkwMshvhn0G05ewQiLBq0fZuaOAcKnwWQAinHMvbehh9c72ajYm6g6RO5mfdOktRQFGTgv2rXwsAldLrSb0PqHfaRfwy5cT5sRoWnJ-lGqzw0-eNI6Z3OhPCyOo7N7tn_k-KRLj4EslPjdOeoKh1CbKfi_lhi_pAnhn1hT-58eyxf6JO5SiekFv4KkqvNq1MPzjuapQmDdZ8zcj6S9HFjGxoaNQrxUJX1UivUxr4zByJ-7MAyg5ZzdhD7LG57k3d9xCiZtwOdoF46E204rRJ_vTKsfh9n8iSJ3TvsU16KyqHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dIxq_RR6GI1nvhhMNjHRj1CV3rdoPajL5SjOPUHujHHR3AzXNTxEGDtADajw5fGiOEqmb8rTZuTqxv-2Tqv1h_MWCyHM76wTmJnJwUdHNbv7zjRf4n6cm69adktsHrSJ57XMNn72PM-mVm7i6f23kAL0dZ5pAGzHlWELVi7zsUMaq2iopdFoDriAn0rKVgUQIiO-tMW_L9hmL2MQRowZIChv8d5SYvA-RNwQbmBUqic62HJl86m_vn4upgO7yoXjknXRGIxPUURF6yyMlZXyXehXCEuVKZ22RXrFXZPUacaWmvZPzTKbQ0fAW0tCrXXpFdJTkHIPmnwTdfrm3NhbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/asXZMp19wT8F7qb3QTnS8FHWOjZXlkZA8rVX8O1H4A4BFfb0q1k-CAzHrA4oyqCT8I2lj6SErHb0wzkghYl3EFXu84n280FoYfKVdWnrCC981S6KGMATYmWfOhjW4oT9_PQWKHDfYIm4bPbtUlHyGj0Hza-7z5uHZ_-2R4YXqktEHKJAVM0pQOvfqXSgShiTk1HMwMs9yak2BMUqWsocWh-hCq_69EwtXyz3v3zYepjIGIWeL1F-DDg3O2Yw9yeMLk-xIVk8JR3lveMlpO0YedZcRQfZzgAuqprxTEcvo9f8k_ZOIlNeSGTO-ipDWEw_Bg5xA2YIbQow1HIWPJ88Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IObQwsazNzpV26x_ZXX-vX7jnXlARt9d5WsPkNfVbKJSh2J9KULHCAxUx0lXLmQxuw17j4hpHdys4eaWiGPIR3_EfPSb_tbwCr2vnI0BNTyfmD01EA4IWrUM8SmMF7xasJq-Ss91Fi2dIzJTNC8Sm6TqxPv4CvM4F4TEXl0YyiKSK34zcC8BjvU2e1ReuApnd01a7R0WWbgSXcqaX1OdxCdFMzcVT6n_cIXZOu6reIdBneAYxrQs_SEVBY5kfTXYYrZ3O1o5xUy_H1M2QaQUXiHBf3j4OOH9RbDkFMOHxH0WbBvRBCnPO4sCu_lJElDG7ntkmXVxUw2Bt8ohT2WTlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OkDb9aRCBhT2wfnmb4rC5vNqQ2DWYEnjMbtHqnrH-P_BFx7SeyQ11bAhJVFyFnELi-6w180hgjPh6rEzZiPY9zJlzkzzywriaAAfduwRW-tqi2zX-541PJlEn242c9DvP6GZOafqoqhSxlm3GWZUZ4dudMCMESgetW6uw5RSX7az7gau12mRV6t2F5M_EFeoDx5c4HwojR3vddop3ndlJELnC3ZiuJlJr0-eJqkOGn6jNOaGPsZ9Bad5viAFQ4M0IrcL9AgZRCbF6gagfVP30-BoOsiYDYHyAti6OsuR4kq95M4BoBLBX5kXEeQc5sxrpQsa-kryi1NwTEmYtcyX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kd75Zo9YQeDNjN_3m7H0UuaeRDA2I6c_lAyFLc1shTv9NgcYxxeEWasSDTbrasc-Ztoq1mQnfNvw1QILofcYYxKQLo4zvsY8dCAngt3XARqklvxvnogkY7AMHvrhIn7kEpWqoe5vayoWQFQUPpepuZmvNfznQSLafhKfs02TPxSz3XH125MLiuLbkloL1IXerPXdKYc3cdGVgFd8c0W7Q-TqfIUd7eF_HFWmnjZjTrjV3wqGS9GH2Vqk9kLKZVCgsmMCCFIWw1xggEckd2C3KT-TwsIVHl1Xn1cm87qR_MTFLNgmaeevDU-vM36LQHhTwBxQMRIiSe5W5PN9iDsldA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=Aft58EgQYbS-l6CvsRtu-qiw7dOwe-zrMbuyaeZwtGwr7CEf_aCPgM-plaI0QdhIoQQHSwEX2v4vnpcd6CK5n2_kq40r7py3A0nhNFgWqaRH3DZzUeR2Aguw3bnZ95jPNTQM3FTlP9OwFAI7M4Qs33MzVIjVrMa7mkQL4ibaIn2Xn50TJQTOkIzAANpwlg3CA2gICCwPsdAokJS_sAHGjVzD1y3NG9vi4ZrxL09OSkvTNaUzFFpst63zCiG4doP_bzaAaUmrYN2D9bUBn-q71N9xB8ErBhoNcLlLlctC7oseHAP3zZyjKK7kgeeQHG_YQ60Q8j4V3eidRO2z-1Gejg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=Aft58EgQYbS-l6CvsRtu-qiw7dOwe-zrMbuyaeZwtGwr7CEf_aCPgM-plaI0QdhIoQQHSwEX2v4vnpcd6CK5n2_kq40r7py3A0nhNFgWqaRH3DZzUeR2Aguw3bnZ95jPNTQM3FTlP9OwFAI7M4Qs33MzVIjVrMa7mkQL4ibaIn2Xn50TJQTOkIzAANpwlg3CA2gICCwPsdAokJS_sAHGjVzD1y3NG9vi4ZrxL09OSkvTNaUzFFpst63zCiG4doP_bzaAaUmrYN2D9bUBn-q71N9xB8ErBhoNcLlLlctC7oseHAP3zZyjKK7kgeeQHG_YQ60Q8j4V3eidRO2z-1Gejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLqxVOahVUXoaaTqfIW6bQ_yD8ilVQJ_ZvtweYmt7rY62GaovNldTMQjBEh-oOkWt-VtRTdXuawS0XNkFzAB1jaGS3yCCBblwaZbOna3wja9LDPiXTzznOTuQwTGdpH0M3MXt4wlydeOKMoAJ1TaRjZe9g32rKGkdycSxuBVCVa6A2VZ8bwW3bUXhPhsapIxAGlKkZ_Y1Wq6Ms0DgYBYVHuTpV4YLAgYd6wrbrpuBluJ0DIh1mtEAaY1DlH3wNQ8Ry2jY0Z0Tws1A-0uHginpb0I9PJ8lXAD3Zg4p_CaOcS-IFAs8BTds2VAHTPl_os6vNizL4IRaC397peLUUEU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOrOfdke2_O5Tjwx6MrHOx9OTWO51JYhjclbKGf-8VXxlh4NkPRm8JuNDV-g9jb41qGTKSEe0ABPBTNP9L8Bgl9wptABJ64v7ZNsGxyLTHxpaoaXt0T-hyWIGgmISGQ21mThqWSg4-aStDgYLh2wn_tgTpPC3CscQ-_11VgyM7UONPKwGRD4YZ-B06jgeBfqkKMX7spVJEv4Zmeqn47rUVV3E2ZRRQGMFwekPHYXJDkTjW8ExS0hwtUSsKus8G_fJ6oNzZrXzs_1KOlKYmhecUuSRVd3XaoNBxQssLfyzcSqc62LOG5bxhNfa3L7aR4D6ayCtxA9Yg68cQLuOdYbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UchV_110D5qLglHnMGCK7UlIySf5-tWZtw6M5MBsFnuHP-NqXcO7B9wncLP-zg9Zkxtt8qXFbyZcG1UuP3XTPYeQTkYSnOEGL65lqaHUSEJfyKlf8K-NmRuvE0Wpi9nUAGwP_P1XRXNP2JtT7M66YXTvFC7J_kmmbOZ3woHhGnvftcgpULUQfPPRYjo6qk6nrJlXlBTkRr156UdEF6N6T0SE6Bvg7WMO11xTP3G4zVp2y_TrQcXpBSF5IU0J2DHJyBCDp-Csz8slTJG7PWoRlLf5QjSdX9Dpl8ZMC_lxFgGIG_0xjXhdexMJpxmxL7tq_wqnAKf_5aJKIkPeA07nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJrf5ebPl9PsuoA5MUerdns54P_7a9u_MC3Gb49wEmWxelCEmBHhUu5pT9h3lvE2l16g5KFxL4PzboAQqq_PRt8dnQPdhBWBoSyIErB_mK8lzMysVEbQp3pylJSDANR1pZhosnd9YYDSVHbpAhWaGiw6BWn2X354Yx19x0DXrmCGFfR5drkIGOOONenbkTZqhS6FOeE-7g5kV3mau7V3ignxvpReY1_m4etiUsopPeJgQOBMGy82hF8JvvnBKQAND98P5Bc5BKoNawscRpuQ6gOsvNVSKiN5LDJGQ9ENQ_2P9jMa8h_R8xr4cFy_Og15p8cKzIKZibYDzaK7Xwc3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WKct8z2h8Hzfw3Mp8Bg6ysd-t3_P_8FJMi38gpFKEWMHatROTDqTIF-RpB-nlp4KOEQPlQvr-EuqmjMifIsatFVDAXZgJExyqgk35hRWXkf9Uv2qRWHzt2keT6VbohmqIifnTTTnPTJJ7P3eh-dsoNrBcTuM5Yi4ziLE3VJKgLTG4eVYSv_XEhjujtUB5-L-Nx4nz_jgUWYXwiFdPmaKhys8KEfD9kbbg1IX7DoQQfzi1x984LO64JHipMT6ruJbe5yNoBr31MWGBwp55LH0JuJC-p6ht94P3VI-cWZzq5sae9WnBxRu8ONcK05rSLsjqUeESbo9D0_VPfRykkaOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BTtX6FQXEgooHn6x1rhuvXLbme6g7HlmrtFpaF0KpsNCRoWHBx_HNcy30y6wFjB69KEft89uBOARo7GlxxJWnDUjiwBUQ0zjf0ww32E_TmumCMVXAl77cYtUhInaj3BXP74c_FPxUU0OuIJd3nG-6Y_rsoi8oR_IAMKOxq7A7f6s8UHovJnj16ZpSorVGcih4qvVFlbDXgfa-oCJrTcM9fy2Uj_SqVuFhyZLmneDGW-X85OLM9uRxrXp1iQb1IVlCtqYCBbAmgoH_vWKrtyiuwjrBYm3JEKlj3JT7rrItc0RGsL3lzBvnPegHqRzYzE6PLxhtdr425vB2eNCUTEWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GcNQr_hePU3mjZ-_ztbl1hSp2zpKxnjDYK0FZ5eScH9ls-1y6d3MPkTmfQPUNYNi5W6taXShKLOipcw2oE12c8k3RjfCVmpkzojqmgcR-gnw0kwv4fSE33kUIZAVtqbLIp0So44_kjNp1tgT5zQcFxnlpGiM5wqApowidnw4vwWP90I2Xc5Ar0g6cGrWx3wjsh2QBYIZIHz2pPIgYKvUOZCp2OiDd_BYwLIl8zTp9FOmBMVAa3nCH6S7ibndmyshy6WjKAPE_rqA9hyKG5dLlUShun466Lw3wf51jxMVX_WLT7zBGkO1bXaoubohVRPwG5Nl846ZLgFXKlMaew6qaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/orqcQYyU-8x3CvsTs2XG1PmjOFx1hFJhWU6mjA4i09ZvK0rGWYohomyYG3aeqX0l-oVh39nioe62HRvaFiicon9FOkXnekKD6XmJZfpkStZ4M5vq3GmN9BKTBuAR8JK0uGAoc4VPXMJArfICupnhNddwfiyAa2_Pvu8fIcvlK5mYJ1QDrV_Ju8N49FyU_FHANUbLfMzoRvu51Us25Az4Cb-KEwbHPnu0bYcw11xCBV1STG6pG8lI0MQT2Uu860Gvzce40_h4Ewk7l4LeT76ee6HC7X_OT1Da9ko2Wr4tKy3NCK9I-Hc-9c5xLhMJWCnh8G0Km-3GqcCXGiqNykvRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uLCFL2nTrb6JxjmUeKNjGBRsPnrjDTHoCVSGAYZqG6s6w0WYPKp50e34IveL4tpKGnlUD3_ug_wUv-bs9syo1lENqCTooI82nOBvNJ-FM2zQOlTQCeJJu29RKCbjnmq-CadOr8HPs9PXMq-CHdgUUnCSBUq4E9zMT6KtcE0QFe4X4bUc1Otuj2iK2B_rOz54-V6iP19SZpakvP408dGkKpJf4pbsKtHPayvAps45lOSIM3IHfnTST27z84UPbfY96_K2rBPaFruzezEyIDscQ0Jk4TOVazHOumf84QC0cUIwKTP9DaRZ09bzyT80hEjwn5tsnkVHVu7i8DeU6Xcpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=mwqVeQFAjnRi3tzY8qq2di5Cw1iqnmXmgbXEYsLRicoNTVhzho5Zz2u7H-bwMCItBefHUxAf0QAvnqueeZE3uKhteFUVM3l8BMmXCFMy0wygbXSOHbLDA11ACSpwNcflqT1SNoC7ugpz67ISLxbA0EJR9PHUnBBALe5nB_I2m_pJ03SvLOy7ielQCXfvYfb1xnUaOzxouKEwB4dZa_eUGlQMCcXYY40LLGX_cYyFWestvxEKpDF3NZCQoj7zKSVSoB7gFi9P-WsARtr3hAAIFHGwx_iYFZ0ktQsgGYUj3NX_TPn9U-c-_SeCSE_fzQQFbQd0dSmiyt9gPk1JbslW-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=mwqVeQFAjnRi3tzY8qq2di5Cw1iqnmXmgbXEYsLRicoNTVhzho5Zz2u7H-bwMCItBefHUxAf0QAvnqueeZE3uKhteFUVM3l8BMmXCFMy0wygbXSOHbLDA11ACSpwNcflqT1SNoC7ugpz67ISLxbA0EJR9PHUnBBALe5nB_I2m_pJ03SvLOy7ielQCXfvYfb1xnUaOzxouKEwB4dZa_eUGlQMCcXYY40LLGX_cYyFWestvxEKpDF3NZCQoj7zKSVSoB7gFi9P-WsARtr3hAAIFHGwx_iYFZ0ktQsgGYUj3NX_TPn9U-c-_SeCSE_fzQQFbQd0dSmiyt9gPk1JbslW-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fyEcNiYzqAWTI7MY98gMdKCxvYeJs5WIVKvQCNLYUtFBprXx7-adkM2HxE_bIo7U8T3PB4SBnh7hEmZaX2W6YAmbvd4bx1aLKbIyqNdzWZpWayTQb5nTq9a9XRCd6awdLq0IoeYpx_MSPnffZjeJwJCNneF9WW5yjnRTdxNbRPbl0qz6lzNYATK22L4h41l62u6uf-4KpWs_YS4tuovGuBUgQ7oQkosVn4VqINB-7tdREmSg6aWwSvXN1qID5sTCrWoLFcCFa7DQviIMMLYccujgVFUVUBi4xYadMUFr4eLt2x_HhlHxjpqR9XYP20KiQfWBDxfRH0Un8RSvH91Oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5coJBjQ6MXSNK6IPSEinGWZAkXD3cbe4wHtkkwIuFBqGuYTtQvj2Co22T1WleRXxV6GHuV4biTuBCfR22S-eeoZ97-fMPwEbrh_M-OwtXMTU4fJFj-DW3fDkSRqIAkGukhK57HPlyPTyNuVbiKNyI4YIouxSSxr0879N5iyTo2Iaf5IbuxqQKT8Wdq45MzetPFOoXBPBO7gTPEYGKdsJIN9BI06S2buCm_uvkwgOw7ZPEoh8vkIHS42UY4W-Z3G3KJ0vDuSMFxn1jRjaV2-fKCm6pqJVUjkMX0l_sxebVo8xlCQlSvaiukQtnvbJq2e4fcGgZCbQ9fB3UrKSeE4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u3GBkgc-0xQCBAs9ut7w0uw3MtDi6U1rTBzDv2Iru2_BKZ_vkSm8nWIeJoO7caLRWENTm9dYNaHENA-mPNVRisPnDQgTB-BXpiyT3YrV2PH8EvG2BWn7fX-ncOLN5IyzdPuYBEYnTjQs5CurZOB3eVcdUXvgdRKsQaJ8lAr0FdXRkG3rXPODJqZJ7uYenmvnBqCWOr6fFCZN6nYNfx4VSOQsXcHHw4BWK_q78p6_Gj5h8tn5gvArWTjUHsouf6ibRk93i7Pq4wY74sDMFJB8lKFxEO7tJfe4DaPWdX_QS1qqVCnJZA56hRN3p033-3ABf2fCjMIdlmleNQABbeF9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/va85WEOsW5MQ6dsePNibwCXDgjKExdzES_uofpACHTgqPm4IrmuQokQJ6gs_vRB6V5qtHFgh5RRcm4pqAVSZOvjLhdWxrsWqjnvbEVxnIXZIgygIlTQMcvOgCP6wyd9HFdlL5v2I3GkIocmak-CR5Kd7jQVWJC0qR-KmAEiTFpNUYdQajtysRA4Ddlsl_5kh-8dMnGULNT9FvLHlCRKrqilBXuhKkrZEHH1I1vKMSwHiJhzxUqa6EfT0x9IF3kCk4FaX3-hoECFf2e_AyyiTIfHsovlwzGv7XMlwsdvlS3Y2kPlxN5lggs62Mp4IesleyoGwMcJFDNuCsURjR0MZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkTpYAG_tpyJQ3ABFz0yakoeEr2WaRifrv5UytgdTDbkiss3pqZGfTrVIBhk45_6NNA6I5trKXn-LtYb-07jJT5CmAv3MsafYGYlx0lHWCxbII81_BQNuS2-5gz2R0lfSz-JZySi54WcfEtm3u0xsLfUBGFVN14VufaAB7e8BDVENIzNpVa1feGRSuoqnWZPeOI7Bqp-mUhmcGQMTEGW-bvvwgzhYPjbmQLgiG_NiRYTYSU50hxre6G2EE8VSGmqA34G57EFroTBJFKMrVek4sLz4KYSh20ZyusiYWeMteygpKhV8cF6F0mIROH3TDVnt5KLA3LeyrluZQewsvCCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T4-X8k-aolJkGW-m_N8GVKKuyO9SlZMRoKBjxA_371UiXBxsfVBxkRB-6LRkHktG0ZAsu6D6er4thxCUXKqi7TcUI2WJBMn3GYLQnguWzuShsNR7hPPGmzJzOuUiQfycG-hlHn0weQ30tohjboek_ViMcnh-q-8BfY2jvacoAoadPqFYekPGiOpnkh_K24IqC_tr_Jno2Lp1R78zxdjbRcBIwXEZgSUlrFcRWBv66570pxhIh8nEQiTp2ntdUfEnAlqaNxgk_pkoT6dw0hFz14wSOvxGvrOF644kPdGcUSMkRhRcdLa_7tzPk4oI8e9I8uNaHXR3Jt8g09sy8c_BUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hb0VQ79tb5QPv3HwFaQcOQxz4nJcCMXeF2QIe-30ADxH1rmTGvO51yVR_RMhqIBKpRqEGAcQqd8nKoOzVAxJHrj_0Ykv-Ts6cN8yK1nTpWXKmTtKOinAaXArknuhmk45d1ksMn4YtS1buTz_mXJSNB3UKRuxsmshOAZaNq6Y2xaANSlUR5T5zlwuRmLeue-0IFRvcw3UzgFQPMJYXngiJTx12ZEC9sk0Rgm8q_yYbkFBH99DOFkyW0pJ5CqvvuVPhvbN2flApm7orItj9SD2sz0PUJkvrZiqMukKhmJgBFXQ5p0jQizTLMW7Ezh1Lt7iF0Aa7NmQ-4iytozkzEADRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ev2AnCjow4gG8_cP3cuN5KbN2g94CKwyjBtO_IwY9kd4VenKdNmfldAN5vos42K9G9KBx36dYb9O77pwWbHSU4_U_Et2ohbveIQQl4qCEyKkNNCmx4Al-L10YTUAmQCU7Kt3bVOhX_sliISv0MtMPUqWueR6YzqVC2lwAoyZUSUKaiUkdSp_nTrUXtA7ZZOqDZtQ42kp2Cpw1eqSMfz7ZjxCoBEATWJ53S2-zuLoBVyvMhVxjHC9B1LDFU5zm11z6qReFhyTiD0R2zUkf4Ye721_x78QNpNGmCr47dNoVm9T8Q_H9BFD9t_1OKCdLZZ8TaHeMCQhS2nSd7gOn3ze7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cntzUqFUISCX_lTePeG3gT-dEq0bdU-hxATQcH9xHp-oemC9zXj5-XPBPvJ4vB-PY5oEFVrF82eq3HDFhoNhM5JtVd-EzmdZ3rFennBFg8B9d3hybfuk_uaKkioF30zy7vUX8gqMySgtWma_tAvSAl3cjK2eYq7-wZN4AQSyPGeP8xGJ5kKXAx-I_OUbhi8M4Unvf5G536m13dXPe7Kgqo-TcO0JRTYH-s824bFLcf9LS9x8TwIt9EzGSNpJ_4b2GhTzDFJ1NPF33lJLSqIT-yOVgcRcaE3FXmekcdv5mxWFZ-XukcWPrQqX4JvQ-Ny6ZLM3lEeMQjDVzX9sMKrtwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u3-mJzswko4B7Uj9mcqAaGPZsTZys-owc9_GCj7bubEMwqstbnpf57HVa3yKHCM9NAg0P046XAPGdQOkl3_V_4vEWPk_BC8bOk2ct1yhMjYNf3v_AkzwGmRsscEaa0t5sZTmIPigzRY3xDVd2awy6ga2kwoXBYeh4PlWw5St6e8UhLBgj6JJw40__YSmchreoD0fW_QlhpkIOCurQq2CWla3OfCQFXFbquKPAPma0dWcO6xjV1SPGQmdJ54YzSsdzMH37aZYrtN_E9w0xUTXrlaXIaT5EhUESUW_S36N-Rtq8SPvXUMa3ua29zLo29rNsVZov3XyL3ZsTFevrj7Rmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PAA-qM9vdorps0fNsWuh20nOzqOp2jvqn0sDZUM7_cR2zCnPoghrEP_RHO07nKnpM6I8arig9SPTFg1HCrL-xjMxQtmXMIt0P1fn9vvmpg3RZaIsYWrf1k25ifOnAKKFrjcZz_BSYpjo9t0uxHUdf6MZGNstGMgHpzwY266UX3Wj5XpXIBjdzR_5fye2lgj5sTRIbANFfr94UBVzJupuPMH0K5LMTIEOKt9mQHjy6DfGZv1lU2fnDyInCvr2qL9yBxT8XkJWRQTAzWoQlJ__7oybfh7gj1X3a77XmXd0QO8A-kiDMfBY5IO3xVadVBAy_H68LKTSaJf51NAH6UQN-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=Rel_YeINfQjboELUrwwW0rq7qiFFwzcuwNyo-cy8IhHkIaSWWddW1MuqOjcAFCONc4beH9lYVH8-1dlel7FeXcx79Cf1R-DrU0MzYpZQcPx0Kmz6Lm3yIfXpXB5jvRc4ogDmn01urVohSrmG_iKeOab-1s0YhhyfYI_KNgt5d7qdaP83hPBhfE5rOuHyJCd_aueq0B99cDtl148EI1472l3uAhkNsPJnGVyf0Gg9Rxn8kOWODXcUAnPToBx9izi0xJs39n1CemAPPBBpVPR2TIaFna1P6LLY9nrl580m0WW15KOyOtuvYBi-eslxtTLFlk79kuc-maOv8JFemebElA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=Rel_YeINfQjboELUrwwW0rq7qiFFwzcuwNyo-cy8IhHkIaSWWddW1MuqOjcAFCONc4beH9lYVH8-1dlel7FeXcx79Cf1R-DrU0MzYpZQcPx0Kmz6Lm3yIfXpXB5jvRc4ogDmn01urVohSrmG_iKeOab-1s0YhhyfYI_KNgt5d7qdaP83hPBhfE5rOuHyJCd_aueq0B99cDtl148EI1472l3uAhkNsPJnGVyf0Gg9Rxn8kOWODXcUAnPToBx9izi0xJs39n1CemAPPBBpVPR2TIaFna1P6LLY9nrl580m0WW15KOyOtuvYBi-eslxtTLFlk79kuc-maOv8JFemebElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=mnUdR0vrQuVWzxwyAVkJ1uP2zsfMa97QROlzqvqfP1eGB9JnOP7uuIdZlb93dS4Qv3rJRrvYjPFIM25ZtuUDNKXwx56rQ99fqQ1MK6Wpha9TkcU8kshNqGticf2p6Y4-Iqs8Q5-Kc5KYCyk2hnUy9KwNnEJS4LQjjJYto4D9bIe2Wx3SZpd4Q1hzHVPC5YY-HL0Pfd1J27mVgfFw4HjG9YDiUhtAcYrWth5ZY1QWA5ocMc2uc-ogfPua3E35ALjbXSpFY8SjfufXX4KUzaM3I6H1djn4HyALwhN6guel1X2r4YPQu_Oi-NPRZoU4N3My5U1iQpqZq471ntDgZpICBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=mnUdR0vrQuVWzxwyAVkJ1uP2zsfMa97QROlzqvqfP1eGB9JnOP7uuIdZlb93dS4Qv3rJRrvYjPFIM25ZtuUDNKXwx56rQ99fqQ1MK6Wpha9TkcU8kshNqGticf2p6Y4-Iqs8Q5-Kc5KYCyk2hnUy9KwNnEJS4LQjjJYto4D9bIe2Wx3SZpd4Q1hzHVPC5YY-HL0Pfd1J27mVgfFw4HjG9YDiUhtAcYrWth5ZY1QWA5ocMc2uc-ogfPua3E35ALjbXSpFY8SjfufXX4KUzaM3I6H1djn4HyALwhN6guel1X2r4YPQu_Oi-NPRZoU4N3My5U1iQpqZq471ntDgZpICBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B2biQmlL9DvpOa__ooyUhFLRDC7mpGEEWITiEK7bEvQstYDSdeqjpaioeoatAIsUkAy7mCJdLi87vFpDWoE4fDAq6SJONOCZuCrhVMIlI0wEA2zKVo_-1Bv4Y-mWv4c1G0vFvwrXomDqFbDo8R6zT1dku15Amfdjv6_3_EcMGMPAOXEYO2ErQvblfunvDDJ4lNDHj7ncNTYnnNltmXm7dajPnsedzEEf-JiloYkOEDw-uKVz0ZkRleOXQZJGVF9FAvExYWtncOhvUvejMyI-c6e8LcYzKAcMkXJd6LBFs2QAiHzGE4VKpu2XH4qFkyIR1KujFYdZPIjij-3rMFt39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbQpOEht8Pwyj4smprS7XJ_EQ-MInh94Ecnzo93VMiLeLSbqNVVG87Bv28coTuNVy1EHq4KoSEEHwoaIgv8jzrW7R2mHxtEWqnoUCOV9J343_ihUB5izYJTVEGhxkIHkvWbnz-mN3M-efB5AqSV_tgc0Z0GlcfWIIOfVGeCQo_Mae1DeyllAErwpgb_i0AiCs8QNY9SXAubq0Pswk6pgQAU4YTdIiuTxPnOkydYbWwh2wmeukJmyL-DpuNe41K59vcHqKVuKEYdSFLe5Ce7eu8oykVVbqTUIn2qNm_1LL6t1sTipkAkYAIaKadgWL_mr2TZBgf1mkOUobXMMXATi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHxcYX_PtK8W-BYO3RQJs4KGolvk-WwUHeQxCYYuBkWSh2Cfamw4f6j61crtH3wiSmfeNIwJcMVo-cki8vym1u-vde6CmVD4syrF4mdpHk_w6Vakr2gy7mLDbte9uAnSNXY3vAX0KZ0UU88WprnBbQmeRRKLeHMkvcCbe5RMJ2HxWMLPBmQAYoZqL9OrxWqym8BN7ZOq-xY-isKK3NYzxwtaRqRt4NbFCVPBAqpLqSAzKZ3Ul-YY82o9KhblHbyULI47HLdAv5KgMRjt5COrWohm1oL84BjCx4x9-9SZHwZPevhsW1w75WZILpKzOZ-bJCTRhfqhbuv87gB8_Fnefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=Yrlyq1OyGbvXsHBV5aMbv-wTlwi1W5VstKNcXL_AsOcwV94YzgAsoZbGA5gj1ATH426eX6kbzJWeHTDIrKd5JHHE4UlxexTTaqxTQm3sapEfW7VWfIxvE5Wt2JDCH-FzUVXMURGdxHI-bl0dlrIkrPvZLflWa2F44QO9RYaR8PRDM_gd6BjeFrGPqPO07qdkbx3XE2AnGEQ7fmdjaHGbqu_Wh7r3CYQz5DtNSjQKvjNEeN6Q9WbLwFIMNlbdrESYZAdiVnxUztFTuPN8qK4OPxEHfFQsHje4duIV44PEf4ROdlz9HhA4NLGVDPctsxUW04kqt56cu8ZXyMXi5PmQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=Yrlyq1OyGbvXsHBV5aMbv-wTlwi1W5VstKNcXL_AsOcwV94YzgAsoZbGA5gj1ATH426eX6kbzJWeHTDIrKd5JHHE4UlxexTTaqxTQm3sapEfW7VWfIxvE5Wt2JDCH-FzUVXMURGdxHI-bl0dlrIkrPvZLflWa2F44QO9RYaR8PRDM_gd6BjeFrGPqPO07qdkbx3XE2AnGEQ7fmdjaHGbqu_Wh7r3CYQz5DtNSjQKvjNEeN6Q9WbLwFIMNlbdrESYZAdiVnxUztFTuPN8qK4OPxEHfFQsHje4duIV44PEf4ROdlz9HhA4NLGVDPctsxUW04kqt56cu8ZXyMXi5PmQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rsvc-ObOIQCGKVimsbbILtRbhGKOQqK89otco5KLoUW0Aae0kMSt3IztzRy7HQL3LB30zHEDDqhIC_ELzvAXBTwYOAhovAGp25aB7G1PKhokwNfMs8fyJjnugZ--gJJUO-4eB9aTzwXYsLLDDft1DaSLUKyCq_og07pItkEOe2C0_N0AiqEKyLMWiDCDE_kZReomvliwvsQ5K5lUYxrpqjsid--W0U8zfr2eOSGvXxShcvNcY76Jm8xrldRCV7DN262knm4fcBGA6n_S1tZVHsjles5iv2cNrMfGajn_ABXTi8F9H5KWC3xbpiNHvU8lfLC1QlwCbbVTFYu0faQFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cPuFwfHNsujBOUDgnbH5_WtDZSwbUJ73CImRaxVG7b6HXPeT7EnLT-i_lOe9j1HkRGrG5QlZ-wpBq5-VDOtdesD1kyIy_Zet6nG29Nm512Qmw_cCR-JnY2U_jvdsnp6O2iOrWKTFpUqJb07gTvjvylWbdjKFySnZUe-_ujiorbOYaHtU7KspH1wbxf5i85ALt-AF6vqwHEuLRjCDUM2SooMU_NZ-9YWRazFRARnS758V9X_EfGHVIH74WOcOUsFmSR-Ts6fOcUhrdyJJoKUBiK0sClDgNSAdMz6TQ9B_XIjX1UmifdjZYmEG9di5ljJQaEsIpzndfb2KW27VeNulzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3-J298_2mx9Nk8irpTVCYIh7FXl9064B6JzENJ35NkuvV0-vIPCJn121lR0B5gm99-7mCuCdDb4rukh5g9voqrMrwqQr57n80qgjjgbyTb6TAo6Bspbf07hFIr1I_AvWIH0NgeSvF3sILutEVHk5141-KKfLUHnQApo-4gwbdNx3q1s8IzOC4Zh4HkkTZ_6HAW_RJXua37zJ1Nz_Hg28rhumupBarXrWzNTX6jBqqms_ERwQyN2Uo11PXy7rzlAWsUXGTjS5WIrTQXMNgiHEhIPVFDjv7YTtz9CnnBJORmkwIKKixrl_h5icyzWDpC_60iqXoE_mXPKtBZLixtkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=mZ1yi5JUoSbsLmQXM39U1JjZ5hAWR2BNK342LSjx_pNeeoDJ2hr9_2abRy54qNYmtSb2bvpbHz4Rla9xHKTiTqXuaGSo98e1w3OSDACHafW2R1u5r4h67uimTWA2O9WnWS939i01g7zVqA37jeFC8H-a6efuBEWOt8foPPia-WMRB_xcSTc8Kov1zBjEd7gNY3HVQC7yX5jV5nhLyhHtV3Ogvp5xdNxa7eguSzec3KCokKE4X_3DtJmCzrXY6ojqZBlTQEnXfyQdDt6T4BZyUJagVs3ceTHuf24GQDjSaHcIErAKInl6bmuAaYIhwLUsS_IlItqbwJxEPQePNa6R2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=mZ1yi5JUoSbsLmQXM39U1JjZ5hAWR2BNK342LSjx_pNeeoDJ2hr9_2abRy54qNYmtSb2bvpbHz4Rla9xHKTiTqXuaGSo98e1w3OSDACHafW2R1u5r4h67uimTWA2O9WnWS939i01g7zVqA37jeFC8H-a6efuBEWOt8foPPia-WMRB_xcSTc8Kov1zBjEd7gNY3HVQC7yX5jV5nhLyhHtV3Ogvp5xdNxa7eguSzec3KCokKE4X_3DtJmCzrXY6ojqZBlTQEnXfyQdDt6T4BZyUJagVs3ceTHuf24GQDjSaHcIErAKInl6bmuAaYIhwLUsS_IlItqbwJxEPQePNa6R2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R2MKinNds0jxKhcGHyRV9CkLRf4EUq9zVffn04TLVQbEuyGywmfWB23Pa0rnV8Fjx7p-Xo-t4-YOQ4VYbj_8J198PYJ_P1LjBtJowcZKX3gr086Du3Ann6f9ghn0UXpiNEcLjv9EDTHAeSJEZ7eXQiS0rKox-DeXfiiiVHfcKNpRfb0i5Wxwt7YuebyTZAWg3JmenXOZGNNu7cRdchhVC06OKyGs8QuVmboHJ1DWpXNFW8x-svtANJiAilOQMUCVZrJ_k-jzvPjV-1UJPaacbbUrp6rEaAoDxxPiNT0HsKnzRUSQio6xNxW84WN4_pQKImuWHEFjsZUf8RNAHyzIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nfj9mOWCh3-40UlYiI0_0NaiH1egeJoT-iQGcar-536yEFMD-tsN7a4nrlMBeMYas1XBLnzV3NLcCr0ytWFr9daiJEh30EYUWhulU9CuTJ2kw3-2V8C1U2GGr8K0wAJIYB77NNRx2nEbLA_ZNawJacVgUd4cApo4683hYCUp85v4YvdSvTWTvgU27lWjTzrmVgGtfrDcNO_FxvYI4sOZmIHrJpmrTyjQE3a993pHfrWpH5p0rzQZ_dglojEL5jPshr57HBrEbs45P9x_s_sc6RpBVbZ_PAMmjV5P27pdqAPRHPpH1vwlbOFGDM12AqwmS4BOkM344LH6YaNv4BN3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=ll2ExNhbVZyxHR6I-Eg-Wg7MU9Jgli7KDg3qDenEr9IaWKxQZF9RBNVoFuVa8JJgGp_QwgWoSUhk5AC_BOklUnc8CVjd2UOtvEecrOojb0ts-AG048rvaAHN8gPc3G92uOIcA8HVyZVeMo0lsuucLI39tTXVh1jfYEp3--mL7ZuteHmw1V4AXM4fNqKcSaUso-QL87Ca2nql28wkfXRhdDsmcPFE-pycsr4EwllCd8jYN44HWqC2PB5uuqXfX2JKWu4B_nZKRWUv7Hr8mIoTJENf5dE1XRm0UMK75CZ09BAaoVnVMXN-x-GG4dwMrPlMLu81kc3Q4NPay-5EExts7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=ll2ExNhbVZyxHR6I-Eg-Wg7MU9Jgli7KDg3qDenEr9IaWKxQZF9RBNVoFuVa8JJgGp_QwgWoSUhk5AC_BOklUnc8CVjd2UOtvEecrOojb0ts-AG048rvaAHN8gPc3G92uOIcA8HVyZVeMo0lsuucLI39tTXVh1jfYEp3--mL7ZuteHmw1V4AXM4fNqKcSaUso-QL87Ca2nql28wkfXRhdDsmcPFE-pycsr4EwllCd8jYN44HWqC2PB5uuqXfX2JKWu4B_nZKRWUv7Hr8mIoTJENf5dE1XRm0UMK75CZ09BAaoVnVMXN-x-GG4dwMrPlMLu81kc3Q4NPay-5EExts7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNUW9MaUO2tz7UZEdcvlOMwJx7s_pmkRtZJ5onpelJi0WxRCpL6m0roIyuIyhDwL5OihQscZzKl0k3BjV-KYmowCy4fShS9_piPHREmLTbwST9qV-tLjK55XWQVeHC0KA8vYIVjjJUjaXv6AtUcAd482JMLSTX2oGdXzFJ8bfcYRxxtwz8-r-4hP0Aa6uC3CipyY1vAlXXWA4fR6nGj4ud4dwWY-sE6qPsAMaiG4wP4dFWzxQoXL5rdg_Vnt0M-FkraJdR7BqMfV4l70brJplLXiQIjAIzu-rctHuhMZvx-HMAwBfBcjptxnQAWR6kH6PVTer5mOCJvu1Nn2vE1OKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eVvp15qGaej0IexCRm-D2ERpIweeagmU4ZQeOSR5IRfd2_FrCpFuv0r6BwOBrRF4fOLpwI1Q88Q12SlWwZ03BYDl9O7Tb5jlnMz6-HqD5LJJEOxWFmWSv7L5zicwtTtoNSetSju_s6H2QwYe0dRiSZuWWaR88PcwCs5lg6CxyvLt0qGNSYhIile6t2TXNNRQqf_9rtvWis2LAwkodz-NILjsVkEBc5P3ACwZSUII-67rE-XWxSYJzQwEH1nFLIFktCYaxhSZxB3jNvIFmYFvl2_l02fQOHYh18Ihhg5s78TSeuHV-cWISl7e6lEAXLLxzHF9DMAP3W0jINUZpZGmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q49GpOaXwHSl65-S5kMk7LCbO3m-cCqhBb4TiWP6RXBF95RqB2EvySfWyDPglA44WcmR58hgGilnVGRX9EYadlGjA1MIS_N3EWFumNnejEyZ_Lkddy0KGS4ds_PBMOqGl-7CSxgRT5RsL0ePsYU_O6wnk5tJGh1LIGmJjAXZw5KS1D4mV8HuWGmqYYwblwbYzq6lLrgf2EC8xGg-c1l-hg4NmVcaKnqQYhf2T8n9iXQBD08bL7Pje-1ywRvzxTpCigoQIml647-s1_J-n0QdIB6YNPtVKGXMktUnh9r_HeMJrIFHZZzuOuSa-itdDttupmZWfYHWEwMxN0ULPqLpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M8gOhRvvXpPmEt0atjwVKyY-NKmxETrMToE-uYOcv0KXNYXXBQpf_vPtxjNBhuFbPHiWit0oaANp_7SdaPdCOCTPyrT9Lqda_63Tbq4Nb41IfixvNe8xSOVbgL33NRCQDNwRcbNGY4PkFXQq5PxMzKiYpm3Vx-Oz715THrMu9wrUdt3x5QcRL772tgYBBV3zCCJpo4r88bq4OGP8HC64GHJtVUTxHiRZpzlG8Dtav_x8XTTPJjKNUxYwHfXywPhkk4MqvL-z_Esw92HxN_HCMgiKa4QuLEdWjbsBjT2rcjisCSU9BZg1nD_qTIxQBZEr6ZVtjVPP21WmeuQr4qdFlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QIFhnSa7_pJlm73uPKMZL_M8GMh0MJwTKkld3rI5dJl4OYQd95XGqrltH-75Tht09TjmkceiaVPt6KNe3OgBSrTZr55Bg5T-nqdUbzQV8CTpa-3EpGeE98qnW5_QWEJmqT3A1KQ2AizMXMz46j_BWClgCujJSWGtqXkbPXhFjOMbWvZ4yeYH0RKIqNLR-XkbZJF06Oqr_3aTASJxR6ET9rwM87oCMHeH_p646pB8Jz1biovNRx_G0dLZ7oGnqe_p5VdGtrm0F1fsE96qFL9gzXXpPUmuDZLjtwq0riJoXUTHJG2Z4Mf9J3oPL2Ibh112O1upGFaGA7aw1kWj5cegjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tyxOB96-SGpj6Cfk_u1GkxdgkeyZOoGnxAHAnjoua9ieBgR_HUnSOkPoKol34sSC1goeTcolIkLl0gNhbJzBJQdtSgqnDMRvchS9Kw5FHa0LaeZBcQOmZ99LXsI3Ax1c3aRvStWEPUsjS0vYfnzJ0mIjd6DEO5FTU1W6_u3KFT_IcIxHssGZYsFBZpt9N4cPAaVgeuFd3h2EdDA1tITKLddPwZV187wZrtK3EYm2YRRhH-VZAZNDq8MCm8uy_UsTE_j3Iwio82wGEGrkPWRuydt8nlnjZFoXWTtC5F54cs7g1k_5CsJb8xFw7WyCUP5G7a7JaWKlaA0qYM13bauyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ElkLszSKyFTi5_5qGLyLqBgNYWJwH1C9VHBOkrq62a9zP4gi53W91gbA2Ppnc_AcLxYkSQQ-eTMk6iq6sLgqOnWa4MonXiCXAjtYPzTLEPoDS3HEMurT_mfdPCVHpJLKjxmJJYWE8IQl7J5s89VYQowIagG-Iq69UEp8GhugApL0N6hAQ3oC_AjyRHTcd8So44hNBJMyByzc4Fv2TG-1kvLRub0_sh22leJV5cpnfI58iYpElD_cqjoOiU3u6-9q4MIt5FPkD5av3PxECLCfeSPGzXNjTv7Uj9WpnFkwFNbAsoHmRs5Qwb_0Eeso3CQ9UopumupzBaUsZ37tehcIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ekAQZkGiJw1LrDx9BflH4lm6Ga2KhtIjoyKeIDzDj65auYDbzQy_HkYKt5zlmWLH5jrqYlI1dB96LtbEp3p2PsA7un-3Q6Otj_rATCCzmCXcrbDAWHrofyA94qah5-gxDW4SKju9eyWh5Rgb5TyYNujodXLDfei6ndhKz0LQho2qwCgfZT1wkuR7_PFYNwYMB2GB1iro9-Wpv6zgWl-1SFo1KgXkUkJFBe8qWQzgWlXmKyofnjrlPjVhS4PzZ-Nl0j5Fp-BUHpubY9ssMmN6R6gktbP3YU7QzfRsCBgTz58wUpw1BBdp22CNd-M8tCWMORzb7MY6pblk6AY84JeoVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=trS-Fdji6l5yguooNGNh0hdjBzw9i20sV7bgi4xXTgHPahLvhxHWKWdtGArwYYxDKlcznTfCdd6CbQyjSQEWsJ_3BoE6J63CqZoyz_wdnSBBBUNabZHSdFUpDEhbdTxYuufJ6lcyh_XRvyG9kMb4AizunK65yltumkThda4_oAimBfe_LlaBQQuRSBwyK_iA6G0Cr8zRKVWI2hyzepUNqQYKC6HOyEtkPAep2e8rbBKy6P3uwzE1uQtxI4x2fUE5VFqmG_RTHqK0E_AzAdz_uskJqFFx6IjHtlBPoTYaETiHJHyETCY5NlJimY2nLqwAEwrv5-G-1kytrp5Ec-hATg6j6X0INVQ8TCI3Iiozx-F2Dj2DBfbrL4DDQbyu6T9PNOVM0l5ynUOU5xhtbQtNEVVGFBLQ82DoyK3BgdY4C6Y3ZsMAnb3JcEZTmSUTdi3J1G7rdqRRz3a5qaOsoUQvKk2px1Jay7dk5Im7YlZ4RQiPJp8N-LV733aHy85WH0XHvaBPpHIkRfd-98OECMq-mDmnQCrgVfItoUEABoKFXgEy1AXq_oKFMVZ1nirFYjWsev5CBMw96RUZs9QTwEEjrzMX2n5z7FHVbMu0HuDIDaqkj1jFBtVu82ncaOt5xJTg41aigsruKS33oh-gNZAkU5s5Cs00mJqOaYSUIDVucGU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=trS-Fdji6l5yguooNGNh0hdjBzw9i20sV7bgi4xXTgHPahLvhxHWKWdtGArwYYxDKlcznTfCdd6CbQyjSQEWsJ_3BoE6J63CqZoyz_wdnSBBBUNabZHSdFUpDEhbdTxYuufJ6lcyh_XRvyG9kMb4AizunK65yltumkThda4_oAimBfe_LlaBQQuRSBwyK_iA6G0Cr8zRKVWI2hyzepUNqQYKC6HOyEtkPAep2e8rbBKy6P3uwzE1uQtxI4x2fUE5VFqmG_RTHqK0E_AzAdz_uskJqFFx6IjHtlBPoTYaETiHJHyETCY5NlJimY2nLqwAEwrv5-G-1kytrp5Ec-hATg6j6X0INVQ8TCI3Iiozx-F2Dj2DBfbrL4DDQbyu6T9PNOVM0l5ynUOU5xhtbQtNEVVGFBLQ82DoyK3BgdY4C6Y3ZsMAnb3JcEZTmSUTdi3J1G7rdqRRz3a5qaOsoUQvKk2px1Jay7dk5Im7YlZ4RQiPJp8N-LV733aHy85WH0XHvaBPpHIkRfd-98OECMq-mDmnQCrgVfItoUEABoKFXgEy1AXq_oKFMVZ1nirFYjWsev5CBMw96RUZs9QTwEEjrzMX2n5z7FHVbMu0HuDIDaqkj1jFBtVu82ncaOt5xJTg41aigsruKS33oh-gNZAkU5s5Cs00mJqOaYSUIDVucGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aK3UMyfZOOHL1GrDVDO5z3AqBHRRcgWTdA9h4IBs6EOJq1Snpw1NRBK1mkc2IChrue_F4nS4aAwDBd2vQwds1jA2dWvP9yVKmBr_iW8-cEur2Qj5LTyvOgh0i9dzM2Tb1M6GA6WZ7VyV6CN-GC3ieE2GVBiryAroWFD2K4XraGEiS7C9fh_5U5ogHffVjcMk4LF-LRmlX5S0R9-D0Uy04SibQTgXXspY6dB9itMmwKa88fJmTJ1vWp1OIutdAf-0GTf16783uoe6MOJxDGIhMBImUp0E14hvX47WFcrfs_jO9fGDwmbiUFseY_bvqCz6vHneGgnX2GZqRQpBAtp64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O5uPqO365FdbUNDnWHn_yz9YhcsX67uG-nmJ5Dlu2SliGjZsToT03dPPjfWtQqQKTLA7LJoRYnHN6ToqAyefS1iTPNqDPa3stxeOOqpbJNqcazof3zEoMO8zIyFtsnLPDDsZ0QCY-NmrR0qBFjCy239OeW3dLMzaMiEg-eaPcO6gNIWuTgnPtqL9zEOp-DrOZ8CpHLjsE75cQeOVul6w-dU1pLGohVIzaPQgVIsjugPzUjtuWeypy3KtGmDXJn9f2k0n7IqpDdrI6rsRRA07mrwzrR8NihBEgXwKj9k5pscLpFs6vrJ0IxV13eb4QX1gA1z6YXEmMU7FQzcBLdss-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
