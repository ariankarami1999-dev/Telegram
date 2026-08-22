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
<img src="https://cdn1.telesco.pe/file/Yciq1n9apje3vp5r2Rd9BOBlmlha7oFDi_TQYtR_wcfjgb5diJ9gpJIJwT6EifdvQ53k_wznUWeVbLuuhRkyIvqhnnwG6-xAj8vDubdwwB-hBzkV_wO7bxM8jzyH0tGqM1Co_GCkKyZP2_Mh-LYELysxw6rPRigdl4DbkItOhbKe3KeNZBzaZOlXXFrs4G0l8NMPs1yhFIXx30qRjSY840YP_6Q8lwoWvntUmVjZUpOIh2rb8YtC3Mlli34oy8a7-xHKzIt5IaIkaNVy-IFX32H4MElW2teXEU9ATsLe9E2Ez5K18AnsiqfoG3vMNoVyu-BlWwhHb0d4CBsz5X7ayA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 04:12:49</div>
<hr>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=IE24UzUhjnih_Q_osn4acm2Iadi7Kmxicu3uhVmN7mGoYNX4oPpTRnv-GLGY5o9wOMHc5WjE8doVnsSRV0Lo8SKWtXFgY_7XwI0M-T7ZgpgJKY22NbM6AtrBfbGpRFhqZVYY-QSYdsXVhz4aBcTKVyebBS-tCbrixJ6d-T2Y0VddGfrbSj_LJc6XVYkFIgfZY4zMzHxH9AhzykS8CHUwovfARlpSKFLhbagQJ5aWkUE5Vr16VL7StYhawFrAb1rvLeRdE-oBCj6-Ayb4CS8j_MtmYeFirORnLMCLIlVQO6UvQ9R4ymeObdAWEQWMTVTMVlubucKqX25C_1DN3taaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=IE24UzUhjnih_Q_osn4acm2Iadi7Kmxicu3uhVmN7mGoYNX4oPpTRnv-GLGY5o9wOMHc5WjE8doVnsSRV0Lo8SKWtXFgY_7XwI0M-T7ZgpgJKY22NbM6AtrBfbGpRFhqZVYY-QSYdsXVhz4aBcTKVyebBS-tCbrixJ6d-T2Y0VddGfrbSj_LJc6XVYkFIgfZY4zMzHxH9AhzykS8CHUwovfARlpSKFLhbagQJ5aWkUE5Vr16VL7StYhawFrAb1rvLeRdE-oBCj6-Ayb4CS8j_MtmYeFirORnLMCLIlVQO6UvQ9R4ymeObdAWEQWMTVTMVlubucKqX25C_1DN3taaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lj3PqaI6-8GSNgQbZx_qj3foxu9HsduOKlsEj1DuEncXMLMcAlbs0lak9exY2bev2MYE2kU0XzkDoommCHKdpVr0kMwDkFq8xeF_wO9O5mOZg1JHbUSSYTA0Jf5MuG-MjG-oLzTldOuJZ8zjXT7min9N9ZydNJpXMhHypimrSDITSyzYOpo91SfDQBB4dlvSqsxaDV8nciJuA5B0fY4sedv7EhnONIEVMHZmngwGpiYgpDDq7z3yVDm4Eyr59VS1f3onGt0gOQq-8N32L3txu1mtx49jOqkWygfumXF3vuBdK8zJ19Pu7WrVeWBn4sL8ChvCHC9r8lpierWDbpLnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SuBb5E6uAu_8vXyqzxdqNfoVs0mzVqqq1DFSMdyRhS_cMO6uMNLbh_YfdyJxfwdUkbHzwCl4eL2rz50YbbViB6WEBv1YHrCuB2JPQA93qnPScrev-5DBpUhR_v6y7Zg21oAQvgzsFbs2LzpwmFtt8s8UzB1v0X_WqKkefNV8tgBOnpMFCCy3P35Ot1nfe5khjEW1fW-TLn2DSau_YwMTnH_UvoAN0DsPkiCNjKhtKyDpiEHTezNglpTsYFwmLa90EQlyowZXGsnf6GjOYyN-F8_dvEYWu9045joDklJuW9e0NBDBLymp4IInBMeIWZtPWErdsQzuGugnv2fyJ-pplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iEH64_F-YjJ-oeLepekcmA7naBwhjUQhx4ZWc9pM7uU7QPmnCBrFx1lxKv9tpydQmSCoop-wP0nGNjYzxrnlSpLjlC5f0npVYnpjA5nCTwR_b7_WRU-8GIKKRyDbll1sobUAgA2DFW5HBSvp7Mw0kRmqgNDKqSXndCK9XSq5Iy6XSblJg_yjIEgpuJILNtbpOXukvCNlwgktLk00XoKYmEGhOQY277PZpcrC-TkzMYXVdit2z6-nMhomLoq2fX-DDOr8Nn_Z_9hHy7up7M_ZyRA6ucq94mWPB4iNzBNXo1PFraIFeP5-a5amApMBononWxPR90il-T5NxTdWUqICFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=FiZATupTJXeQiADtu0VDc3wqLvPBksuiX93zQwRYHfwL7EQ_gjgyGJVBq2FHnr0Sjn4qYCbCTBiBDLzo1VWs3nXaXUu8mFK2oABjlrj89v8iptGDukiEr64pYmsa847wqEnRgV3ZRXsnaKjUVeEEF7FNlOpXELJihYzz-Gcl_LF0fyW8MUonIg_CxyfVmX54-IgHOV5pMcBwyW5BnVWifWIGl12QK0owVyqjPGKCrfVZLK2mgtJZMgesSjSVXOsQT6Dvd8WLqq0feIxI1AnXvx2c6iA-8v582ehKCuDzNctbz3BYocjz3QwhrVAxTPWOAq_7ocN-1-5SBd3KUQJzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=FiZATupTJXeQiADtu0VDc3wqLvPBksuiX93zQwRYHfwL7EQ_gjgyGJVBq2FHnr0Sjn4qYCbCTBiBDLzo1VWs3nXaXUu8mFK2oABjlrj89v8iptGDukiEr64pYmsa847wqEnRgV3ZRXsnaKjUVeEEF7FNlOpXELJihYzz-Gcl_LF0fyW8MUonIg_CxyfVmX54-IgHOV5pMcBwyW5BnVWifWIGl12QK0owVyqjPGKCrfVZLK2mgtJZMgesSjSVXOsQT6Dvd8WLqq0feIxI1AnXvx2c6iA-8v582ehKCuDzNctbz3BYocjz3QwhrVAxTPWOAq_7ocN-1-5SBd3KUQJzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PB7VWFPNI9JzD7BcxReotwSOP48kXEOeiRXNR9FPQiG2u1A3DyIcDrHRdgCeo6uCSBYIbWceAT6VUwjmbKfmPOjb2djVKlIqA5uT7Emkw7lPA9xntoXPm34mMHX50tkJVT9MNC3h5lCSebCaYW3oS_uPoZhI0j0CMeIEdFlVON9PqmlqGKNxtAKO05KdwUJL5GadHtQjAE9Nt_ue-PJQVOOFU7sRVIEE9w_wnGg0LIbNpw1x1JZdx66LDAt69YZG6fUSK2LUTHbgpGIRmONDTPCLPD8tIztKYBWnkKu_hry3iXb7QkMwis0rcuKwe7Ilhy4STUiJyTxB78shIuKy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ex5V4zpj2OPE_m0E6GkSclxICp5jfccYq9Io-RFfCAC0FAYHbuBVqcrxA0gnCvxsH5sXNyLunsZfU19fd6WCUNEEn-kfqwhk1eLsBbEqeFfkhwvsDsZZfPouVXSCYOe_wU5LryeYCg4ha8o-D35-Jh52DQLcSdrRV4efwOCHblWba8tu27JBxc8Q0OwyU4RObDL-gatLY-l0dLbyG0SYebAgOLP9WjeiPfFVYy9SBES47D_0hKgtdj5qoEEBP_pwha-2bvklw_WRUmpxKf55Ku4POIfIO9rZdh1hEmpnaibNNDkydG0tvGxX9wNMtkz9NxVrmkLHy6M3uL-uLOQS7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKv1vKkLPxXxpcr0kNJEkrynJ7POTWPwaV2Tdv5m4VaKI7h4MU270lk3RMGkg3KCy8R43HcjeHlCqNoixmxJZRYjB5Z23i_Ql3ujOi7crMnLwehS26xXYFx9G7K9Kr77M5jKfL297Jb7lFbte_FbGT1wXmAst_I6mg9xw8Q5SimIQQP-nFnTCLs1x4OYiB3RiEyAfZiPFJOemmcAuKpYdOVgzr_TvggAp_a5GCtN7_N92HUrEeYcJwGEu3ddzjLI9_HhDm3K9FM_xx19r0c3eCH7I3K6wIcMLT2PRUrNrfTVn5Frd11iBey93BhFqKh0kfFFvKzL6_5l_jl8gafdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=ISKFb7U2qBhdYWyNkq4e8AOIQda_yHgyse5bFtBAv1CZq1Xsvg5cX-ZeydwWQ4t7v73fgPE-i1sJbHuBoYqynAGbR7CZoHYKyGQAcZv5bApfztS3ZZs9NlrVv-g1Fg2s8LTIaHP3YSUwgzenruvefTm1LKD3tEC1fGUHAvvGHD8jg93ml-IF5OFR-XItQI59XFlZ-QnMW4fXTEPeAD9WA9Zd2YVrfU2q_6rIQcm0GgOaAnYwdAVJlHpYq_R_XB0RUembl6EKC2V5_uSVwQrdgDc27dgFAiN0hbo8yzKGNNwl8_Y6t8l04y_M6_w0GeeBdctHkiLR9Pm-RCAbBMpjqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=ISKFb7U2qBhdYWyNkq4e8AOIQda_yHgyse5bFtBAv1CZq1Xsvg5cX-ZeydwWQ4t7v73fgPE-i1sJbHuBoYqynAGbR7CZoHYKyGQAcZv5bApfztS3ZZs9NlrVv-g1Fg2s8LTIaHP3YSUwgzenruvefTm1LKD3tEC1fGUHAvvGHD8jg93ml-IF5OFR-XItQI59XFlZ-QnMW4fXTEPeAD9WA9Zd2YVrfU2q_6rIQcm0GgOaAnYwdAVJlHpYq_R_XB0RUembl6EKC2V5_uSVwQrdgDc27dgFAiN0hbo8yzKGNNwl8_Y6t8l04y_M6_w0GeeBdctHkiLR9Pm-RCAbBMpjqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T1CfyaVGknb-8DHWURnUyqfGSpr-hN_Oqs8VIVfruZNAPHXxj-ZEmPBarEiA4KRoAlDMewzz1Bpnkl4mHa8SYYjqew5EESx_Ey_ORUTzWnPVetO1uuIBCYUmT7YGurD5Biha9ZeG9AfZqqo7xns_jrb5nYTTtF93ZCYA0Kqagy9Oqm37XIiobL34ZJh05nqMxe3Wx1LFd1669NbJ_BkJe7MfdI-RBkZJ1HdavhTbVBcIi7rigxjdMT71kjkoHG_RO0dpqWy7SIBsuiTnLGkUH1NZG1m8y34O-d-Yi0jsMYBADrGAN0DV8QmFEDR2bwXJ_XljRKZCPeE36uurdSZdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hi3lslHCoIB_5L50dP830phXK78Y8enlDzWgQT5SAfi_v5qvevXDG-t7iGFTJ9S8n24WKsbDb32qIKVWkSfys8KjvzxqbG5pdRr9mteGBwDkQVh5FCLVri0z6b4bcxcqO8lUm8j4MhV9LMQE_-lnhVMCIU3sgCsYgUNDMyTRgTAuz9_OD-XPVCXapEn_c38rIoriP7EaMgqQkVZpxkE6mUZXY3eWSms05FNO4fhb396N-1lq56AY9HfmB2YEOIPuzumhgxaqui83i_xuBB0mAk9KqMEKU0o4DNdoJ-_g1ygDiHnGDpXShyn-UqOyVCLLGY8vz1zHA8RATbzkYFo0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=EqL8xoV2jh0YGHqB-Ndrd8HvrKE3ImbZXxSW-xyTM5Tg24hrrjfddwULwAKfA4WbnJGetdFbt5I_5qNMnN_3wgTwgD6DxJs7j1NfQjr9K3QSWrx3DTJVPciNXic6FeSvVIbYG-6j-5XFkxFCafMHUS8Qw0q_t_XxRqo-zcqNvWWI1we4j0L5LueRKf1UwdQHZ4ZeHz9kiugbO7SZiC_ShKKOXNY8TCYtA-2FLEONfzwoC53Tn3OOxtEWIQStKiCqzVaswKKs0RECM5oUop_vuwSsQCV7fd1Jl8ECCMUKEWj-gmAK2NTU_xiy3RILHdWmdbTT9UU52R4bC0G9f35Jew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=EqL8xoV2jh0YGHqB-Ndrd8HvrKE3ImbZXxSW-xyTM5Tg24hrrjfddwULwAKfA4WbnJGetdFbt5I_5qNMnN_3wgTwgD6DxJs7j1NfQjr9K3QSWrx3DTJVPciNXic6FeSvVIbYG-6j-5XFkxFCafMHUS8Qw0q_t_XxRqo-zcqNvWWI1we4j0L5LueRKf1UwdQHZ4ZeHz9kiugbO7SZiC_ShKKOXNY8TCYtA-2FLEONfzwoC53Tn3OOxtEWIQStKiCqzVaswKKs0RECM5oUop_vuwSsQCV7fd1Jl8ECCMUKEWj-gmAK2NTU_xiy3RILHdWmdbTT9UU52R4bC0G9f35Jew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovOs2MFwBvdO-sGTUfQkGY1XllPGpfCTd6bh49DJCF9xmzlI0tZskfScxMItxwZ6srfySfL5UOEdFDTgsKpv1d83wynojPsvyjq-JghgVJEJUFhe_CgMDGMVn1EB7WgXEkrR2Q4TvimhrdATom_6T0j2E1bPD4sXK9xUn7Pn3IOKLRxsZqwAdaQO7DCoj4cbbwSYTSYqEIdJo5Qcqrh3EQoQG_RecWSoNXHghqAObqE1aHypweIFXUDXHHbFaJ4_y4uA9nE-3KfKsbPnypsY5X9SLesb6BFdrJYjjNhg-dWFTQwY4gDEj2XZJLMAV6I6ZRCKpl4U42SzWmA-MuMK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UTw_dzg0Kd9llg04OLL6ACutIsdsg9Eay51eGzcz9a-n7mEKx5awqmbIplog_XtvM6hbiRUhEnTsKQTmvN16x-Vxov2btPHZA_x4gjiC-Dz_eS7a6Eiuw9G91Dz3W8VcolCoOQOd3taqzxcTOlhYqSSUaO1FL2IbXH9E992wVzTzX_wA3cGws5aynUrE_fJOF6K2rvFFHRruhaJRWOV3zOX2YNYN8UyvT_SQ1ufhBfWvIpNpKSDETH0IUh2RvVcbUqNtM5vTfVqn_nlw9Sty9wr2OdNIStveFLtqgh4-GJWloXM-DtCdQwuuv0DPPquY2iBUHke4Xn_Y_Sr4ML8JFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-0k0ksGqfmAdLK5Y5PW85CBjqopB3iNz7xmO_7rBNL_HFU_cTsk8d4MQe_lELOBBSS35x1agUS7tNmubg3O6U1XrMaWgPIID_mvkV_1_QiHNZPm5F4096uzH89ZwNYk262L44fOBkWDgAFGncHBEajjbprHhgbW38Rq7800MTrlBKprgDLQ21GaYj4yoWh3MmhLsvlpubPG7No3gOEJ2DJSAYGj8Vn4p4A65uac-Na19O-keBwJzY7mxjB014w8bIt1eXtQ2Y6CCHn8Y5ugAR-jZbIOpksxBfjqIZzt3Pr-JowNx6gbdcfE4sw5Vw_ci50UhU-l94CnhTNKx7k68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jIzJmaOragJzVEjMF8LFiNE24_AcFYeDPC1LUovVH5C_kZFPFb_hT9uqK-LwNRThu4i73qfcIcWuyINXKtimJMvsC_Nt5gg3QyzsV7KXwMow2Lb4hVTs4Em0xBAWG578eAoZHCuxnO1xwS4qLOQD8hELaXdOL72sM848kf9X3Byy8loVy_dEvi2lMm54lTA_lyl2K05A9EnO71nDTCMgrLjlBlPCCj_MPxJxSEJgj6Migksj_JXHl4k1c59us6m55Qcbcm98S6l-cJ5lcxCDsnMH9oi3dJ2TqBY0DBpiWTgJay_F0OHSZCoCTIW9hbZjZgnmmv9sU-vVqcokIIXWeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aLYk1ixWEOouhH-3Mh0Fv5OzcMBsAUyglxnLNVn1DjlO-J-fxEpKq0m73CDMGl_kYD8dE7zhhyJyGuisyRqxmH2qdcehBfJ3sGbJWJF33-KlRsEnAVsRdFnFVQdMfwpRY7GfAcJU4KIoKEBOo7a00qnErxLi9Q5J66uXgej1XKmLUGHSYhstl0LMo3JsrWsd9rxALx9hVeZgYS4JIiy6uQv4QtN14gctZd9mVtw_xWjiFLUo4mOnzHsd4S5kaKz_OU2SJnbHYbsmnmziHOOfLcthmEiPipT3lb_jyRO4vXSaOGEsNawQ4olA_HAfeolg4VgFWDqUMVaMgTNqA6-GnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qy-l57LiDyapX0A_x_Wni8Ovp-zOzMl7c8hkOGpmHXABpMaUF9bLkaG_ToLhGfTGMxJL_4Kv75s1402sZP0aZbz8KDSBo8WtU461SNkY-NKu-l_843krWf0x9eeE19Ot3J5FgG-Dtu6ps3ZcKd931WRpMAnSaVmE4nuKyRSpGgGoLXDhS9yIKUwVN1aSeCE_PqNwgk7ZKVpqZfSkWHcllYWQOtfUo1pQRXAki51kTG3Qy3swli2rU55TCJTfQoAAtTHyicC-7HqcOmXXqBgbXFOh7znKlJ5BhQaX_cKosMfmaWJZ2JWndSbEHN7WXhvRMWeLjqBA6GY5_496Ozkbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DjLXfIQl1O26k5zgSNS2xyOLk7k7Hv8OQskXHfT81qm-ti7iOjhdakJPt87j7ox0Y3IwFApX6b2BFzcBVHYKsqkpSC6eicculWq3EezcKhKZi6m7SX5QuVpEbX6eUVdcrQTBd-6pbQ6Mni5A2L-sF3FRAAo4IQnyROjWtUlBOYwqFOs3GHOweFv2hv_FahiN6fybdnLhizzBN3dCpWMFf8t_4rjInT2Gk9RhkXv0kfWpbqmnCPnsmVz9YwoEJpZeaw3RfGmdLEtwrK7ml_uJZvxxpsV5PQNFBgqGF9OWvAejYpHI5wq4XxDJM1NysqeulCMEKaZy3FeGfNEPkAjUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/as5q7hD6B0jv62rZWLdRR5aQk9eRsAev_92ra9evFTAZiAS6oww9cjlCBfOYaDgPcmtJxiey_qP-l472ts-r6VPJRr0YLLAgieaSULsf89cTjyZEiMiESNrPr1yogNIKHS8pCyaWRXc7JPBjWKT7HZWYci3sr_xbWxaGdJ23MN_C6KE5KLbNZFzuYVRC-9IGDRcVjUb17eDT237Byd_umEFYJcJwx81jy2XQ2Jz827-RHWVitz9IQTiazfzTZqTSRgE9MUnQ5fYYG-P7z9O_H9wQivrz3jyQ_e49yw5uF8FiXCZ8o46K8g-MxrGzcgnCWeg_3J5wpyxVPAl5FvIReA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=EYRxFVHQZ23yP3uooTL9c_ELq_Fr9fSF6PEQJXG-zpZIk2Bu-dH5Liqa88iGlW-menqek0kETImuPq2U9gei8iTj1B7ABtKizpaCWzutG-qHhUbDMsz8ht_XZZs4NSfi_CZHyaenvfp-uJihHx-fjwBHza9CuM64YX44Q7ZDTA2P8Sy8N2JeCn5XvL3gN0ome_c-rhMsWxo0vXEbR-wSZ9rRbK2dIBRmnV5f6PHzSGV5GmisapDA6TWOtNcRpeJFOVAtYHZUmu9Pm-7LGKHVTmn_3bK7LMDVy6rxvac2UZLCag26cMKmUaKEIo31E3OcPCnSEqg7VHfZSn8iye91sZM1dG4CQyMcJHv6Sfk4ohp3o0F1yQhw3AxoIZMxUvnu6EgYlEI_Av6yC1lroq5NBOUKspxRSu1XdpFeVl-UNVNTVpqzE1VdSmHz7t78IULAMJ4luibNNvfoWA_3BUSL_GD_oqB9b4IjYyDEXPPby_TQfx_glydI0_4Wyeda4f5zpMmKYcD01XJy1IMfIGZ4v-Eq9tdinImNzKGkCsZoXV8_N3YVQmb3nUSHOArrPePj1dTpTMA2dtAH8tzwfmywYOxBIooAfGmmLSc7ukmb0kKUcUPDOpjjF1-ESF9itULQLnbbF9yCtC3_KcPb82dmXHKg4ELNZPzk14oFgeeMIgI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=EYRxFVHQZ23yP3uooTL9c_ELq_Fr9fSF6PEQJXG-zpZIk2Bu-dH5Liqa88iGlW-menqek0kETImuPq2U9gei8iTj1B7ABtKizpaCWzutG-qHhUbDMsz8ht_XZZs4NSfi_CZHyaenvfp-uJihHx-fjwBHza9CuM64YX44Q7ZDTA2P8Sy8N2JeCn5XvL3gN0ome_c-rhMsWxo0vXEbR-wSZ9rRbK2dIBRmnV5f6PHzSGV5GmisapDA6TWOtNcRpeJFOVAtYHZUmu9Pm-7LGKHVTmn_3bK7LMDVy6rxvac2UZLCag26cMKmUaKEIo31E3OcPCnSEqg7VHfZSn8iye91sZM1dG4CQyMcJHv6Sfk4ohp3o0F1yQhw3AxoIZMxUvnu6EgYlEI_Av6yC1lroq5NBOUKspxRSu1XdpFeVl-UNVNTVpqzE1VdSmHz7t78IULAMJ4luibNNvfoWA_3BUSL_GD_oqB9b4IjYyDEXPPby_TQfx_glydI0_4Wyeda4f5zpMmKYcD01XJy1IMfIGZ4v-Eq9tdinImNzKGkCsZoXV8_N3YVQmb3nUSHOArrPePj1dTpTMA2dtAH8tzwfmywYOxBIooAfGmmLSc7ukmb0kKUcUPDOpjjF1-ESF9itULQLnbbF9yCtC3_KcPb82dmXHKg4ELNZPzk14oFgeeMIgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F8Fpz_R-6Nq920KloBaYvqyI8nBWmo0xprPsHvTnRz_FFaWDMlUFNzvO4VCVPBGyUQrIRaRRBEMMQY-MNMdUY40zf69GsxeQ-yFXh7InuOoWhYzveQqzBrMSh2iNmTJDbrw7ZlGUBtFPNTLLGVkfbhtdodUaadva6k3PucDljcLYCOw5OM9EyLMGDuF8H_c5edlCGFlkgDgnec9eXFnhblv8F6wX9C0w09DpvQml0JvRklIo47P_6S-cRre_o9fUwN_goTPU1AoCRRDW4oIUO4Wyvyvy8G3vFnV5a0SwcpZFCpaPtmJB8xqYQjOnF3QFrZVwmmgDbOQiP82VXTBkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N7mA49qxmlMAoxDBvRXWE-6ShLkNxiPTwdsxq43x2QrNmKVEs8tj_3gBfbFMJa3O-C2-0sDrooZ5EUlrwh4T8hHvFh4VCvndJPwhUiBi2fef8zOthePKcP-lnbogTfgQESyIU5tmUSIoL5TLUyGlnJqQMnzNkVHfAW_X_EdBGy3hFem0SoRjMlDOKJFIlTW_g5BBvEq-tFiHuEwgAgjT7saPGBgXeZZkfyZmNw0OgLRenTQ9fTIuTN-XnyUomYPHZTYAZbPAOsImiDOXEDdiZUoyZDtu9kTD0eHSzyp57W7HwBTGFDvpBMayhQYY7-paVx2JgaZadztCyMa0X1vuDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=TL-8FuObYSYA8vlKeAZSVd3fK5etTm8CIBRvJOcmW4cvK04EciBF0-ecqbc5uUXAtT6BSO0jqi42kC45AlcCMhvjnDLnbvDfk0lxR8UmSOQ8rW0u0Mq7JDEZ-mo7b2Wmixaih3L6QUntsbi-zIVF1e7MRwor87p_hxO8xxy0Iu52B3iwUSCwDP-To2M73SYf8JxrkLsv3eU5hFGR0uGHCvJFeCG642CcGAMRzXGkm1dtlofwYR6b0La6lSmzjaLZoNn0NYouIfkbKuKjgDSfSF_ZXj4m_BqlpNgJwNK9x5pv8v9OSZx84n6aLphjZUrnY9QgyQTMoTBir3YePHIjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=TL-8FuObYSYA8vlKeAZSVd3fK5etTm8CIBRvJOcmW4cvK04EciBF0-ecqbc5uUXAtT6BSO0jqi42kC45AlcCMhvjnDLnbvDfk0lxR8UmSOQ8rW0u0Mq7JDEZ-mo7b2Wmixaih3L6QUntsbi-zIVF1e7MRwor87p_hxO8xxy0Iu52B3iwUSCwDP-To2M73SYf8JxrkLsv3eU5hFGR0uGHCvJFeCG642CcGAMRzXGkm1dtlofwYR6b0La6lSmzjaLZoNn0NYouIfkbKuKjgDSfSF_ZXj4m_BqlpNgJwNK9x5pv8v9OSZx84n6aLphjZUrnY9QgyQTMoTBir3YePHIjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Frsh3ywjpbrPouycIbgkkppQnTY0kqF5UaeKJBcj6sfXWkU-WGg4hu6rTZJmnFUFXhSp5NW7ZlVr7vr9jOAtkjr4wcS_Dx4AGqiU1smRubup6XfXFfoKvclvkLSufU593nt1Uv27MuUZ-TJCN5eGUM2hsTyF7_B00zJqAGZcXqqxCcTI5KMZ6X0VKBN_zOHwQkeZgLYjwYQzBKm2VgfiDkRppS9MoqJxzl0OdFlWbp16fbBWr42VvHmN4INRwwbAPKAJCO8IPkIE_RehZOC5l5mBY_mc2tne1offeFPhJdZ81IyfJproRgR2O_vrWpDf752slwh5ik5DKY0jh726tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3uDwAELdSQTgnmuhxUKwjqr62UNcaB2vL0CdLRx04xHBzULESNyG5UtC7JAi3bbU6mOpoj_cYT2ZNBLbak706J8FXsXocBzIjhgiq-dOeeYdXiMBR_eCjvRp_lqGiRNv9swRnqZlnBgLXY-xfqO7Siw2s5_cKjQ_beYbejZ0bS-fZaxtI7YoTIgpmnUoP6yg4Kr80O9cLV8ki38XU2y9Ig1jxxCFdpaw48uL-W-R2f1lEZamFliGGsfyGwrlQi6njj_PDBV128jMnwQeUUdlRfN8VT8gUFrY_2dzq1exMElYYVkfw59GmRjz0idqqOb5nmYWseBxf5q_DOpscui4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QJUq4KobjFbySbkXR8Vekypx11z9k7yFL7bTAIBfIIX1E7g3uZZh1188mQPfBzPTj37rX_AyNbkljJLuzZAQkVpw8V9CkwAn8962SDpA3165dv9FDZbOCcPtiYOUch2eSU5Q8MZ7Dsr70P2pa4rmg6g5BruhUs3RGGF0AINfmImXKIKa8-0qUBBuLNQWM5jNotTv1WpxPFKJmYPqXvm0gHDubyZbUTrfdnYWRFz23ynAPIsi2ineGXA8M_1objZlU5O9owIuQ9_IoEMlOkB8ZAciM9yW1S8Fp9odwdQslOEytds-q_DAhDtwn95nPmv-l_81mkynZv2V8e956lJ-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=IE5YdMqHVnHQZaPPXDdqHMdDhAwWS88CkF1RMjmmUNBIef64iiINo601QOwn8dUvqGAs2x3yp6_rM8h91bgiTl3mVNdkWMYMXd2BekBrS_X5w9lZY__eYgDjjDdAplTNlF-hvclsdODANXGMde8wGnKIXYKyIwiMwmu7uG83Xe5eMdhPgUF7uAYNhmy9fwHXTyYpMTbysSeGWt4vt6HizDO8_Qdr2KAQNDRhhXjw4dVjI0vatuZRALFZvCrqOkoaYDTHGvVk0kprG-7JOO-VLHUfo82O0Sk7qxkm2DvgFcHvns4p0RWlvh-aBgTej9L4zEFJo_SdB-H92nBxopBsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=IE5YdMqHVnHQZaPPXDdqHMdDhAwWS88CkF1RMjmmUNBIef64iiINo601QOwn8dUvqGAs2x3yp6_rM8h91bgiTl3mVNdkWMYMXd2BekBrS_X5w9lZY__eYgDjjDdAplTNlF-hvclsdODANXGMde8wGnKIXYKyIwiMwmu7uG83Xe5eMdhPgUF7uAYNhmy9fwHXTyYpMTbysSeGWt4vt6HizDO8_Qdr2KAQNDRhhXjw4dVjI0vatuZRALFZvCrqOkoaYDTHGvVk0kprG-7JOO-VLHUfo82O0Sk7qxkm2DvgFcHvns4p0RWlvh-aBgTej9L4zEFJo_SdB-H92nBxopBsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fl7C6lXPBg0CAKFDLIKPlprTpBDzc7j2SF8e64eaJB6gj3AK1ABwvR7HRD1pbsDB_GlaJg6iJHVPrE4peF9c882SldsMj-qQoyYt-dnx4cU70NwN3I2Cq4aSec-TvR-v5fJk0QE0rxPNYPU9xDyZqWkJQPboURhdMRdONk8cmZBQjF_ny1lvyMtkjKy60NDx51_o-762iUcuJt2tVL2JSokrGRufcSoUD-i1K0ugcrBySnR2dpfjeKLaXJMcSyv5XA6JbiV9qyE_qxNIgiFnN1Pyf13hmWC9QKpDHgUARPGqTvXjF7YDkV3QED46uOl_D0mSsu5CAUN42sw5LblM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=ZFCOqfLnUPx0Pmq2E8Dy0dwuW51rzbpKPgDMLW7Oxk0NdP6fbNWwzEhxr8mAWD_R5s0rrXratoHUtn4KgN7nlU570t2If9rJQO-9YQGeNvddCrOUbmnNeSsNqLWRyZ_v8EXuccBBbO61iDd8c4jpGh585Z7qP8A9q1HUILd2209Q_kzQ-djUrD3iTuHalnArOMZjlsbX8lGcze8HCPhRRdyxQUlNV_Fy7l7kgzx5tFJ45Eqyu3wUx4XgIopjA3srnYv2DDCxBYPCVQSTEDIijAvkyEPyMa6IKwreEVzObf-iR8IOI6ecgK2HlpkpBPLR0buQJPP6IhMU6N0qmRAM1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=ZFCOqfLnUPx0Pmq2E8Dy0dwuW51rzbpKPgDMLW7Oxk0NdP6fbNWwzEhxr8mAWD_R5s0rrXratoHUtn4KgN7nlU570t2If9rJQO-9YQGeNvddCrOUbmnNeSsNqLWRyZ_v8EXuccBBbO61iDd8c4jpGh585Z7qP8A9q1HUILd2209Q_kzQ-djUrD3iTuHalnArOMZjlsbX8lGcze8HCPhRRdyxQUlNV_Fy7l7kgzx5tFJ45Eqyu3wUx4XgIopjA3srnYv2DDCxBYPCVQSTEDIijAvkyEPyMa6IKwreEVzObf-iR8IOI6ecgK2HlpkpBPLR0buQJPP6IhMU6N0qmRAM1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qdq9wOCoEjwSO9B1FTA4gcDUMQRg42i5fDlQaYgu9mY2FA_dByWAjBjrshDjYOOX0ufN7eIQDwscTGGmL_z_2Rnl93d2xCNwW4BjU5OOLuKwAmnTANCdfOBNdW5VqBgCl2NWqPeqkhS0A3WQFcbsZdIwwcKDMVwlV3iZ_QvN-DsB2EIYt8SGxCaGW2bKNLseOdQ4hBZesBpQeH2BQ8q_GZPG98_EXsYOCFMqMpYVfjq32lYFy57489wTKa-olthmBJtbHWP3RO-TT6Ts8bDihkkghqfouGy-kfV71fyn2osmy3gQSaFPakyAcghfKTHucjOEBuWfu1LPO_02wFcgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I5hrRAUEuKZ7FEZuJl1Ew525HpZjxfRVGiBvHwVorSPGi_dpgsvhrtb77V2J4uCcXEoksxwRuv6lYKPZ3vJCNTcUV-CIA-SbR_0cQSh-OtH38hj7PM8ZKJCCcLLLQuoeNROPcuDxKqc0cjffvMXmc_7Ofal_tEW3RDYCibD7GPC0aHqDG8WL09NEVL4NvooNQJJOJnKIadIT_RyXQNUC5W_MhE7hlOhGqH4hgdb_Y-FUluN6j-IQSf6EoE_c_spiCFtRvCpWba2i5gNlttbavn3loN6qQyu3-9TH8giB2kbFqsImqHcO4r-LoXcYpnA7F2ZrflRkOyzlSFs1HMsMYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vcSDGZbEb2OWRKUSyWUfw3E3GXHUzBQyBeorVTonm0XUxlFHh2t_9zgl80KB6PZu_IsJeqOFHlOkNk8JPfvE0YzqXU_4WI6vsuamin4mxt6--OklIIJPQgNoTIcDM_1PVRT6ZVGK6jrFzRJj4GtU0S55rCt2LRx4e-nUdaPaLHnVEztiuaY8jXNTNg5ynuNytFmgqqDO2776rsUlJ60cUJfEgOA13638Vm-lCmsxK9A5D_VDRqoJA8rI4Xbsq8ANfFHMORBb2imBtVcLc33W30S6K_XMgbenvZpoeml7gTMazam4qZ0ClKGvf7gOfk8_90h7L3Sg2q2yq6kvp8gu9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h9yFCnn9T_dgIhJ89rrMGtA16zOZNgfxBmrP0Gn10-i1MtCNwP6QpGKvAY6i4zjLGmkVY4ssKMN0vrLt8AoTjKltDDm8HMw9MFvYqgpuiG885KBOkQVmgHVeBNnv58YUpu9bGS9Kqr2oXfIzE-gBBFo5dMeAQ1D8SYhBo8qEcr87s2BNFjW-TNo5bpPtlztmg_esJrM22tta8Nxa0TBhgZ6pGLt0wdx8Ut_JEIuz6rH6uGQ6IIIi8qxXCPAaFZD7M6wssW474IGMTAktDvhqUmysi9xxhL5i11kBOpDOkrFJZ7c_BqYW255azMYoKqtN0EldNxGqlanP5N7YhsPDyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WLmgzdxTCVlkc6TUZOXZEq7wG9HsnSyPi0JUyPewD43t2mZzOxAcrK47U6YWLLgf9nTpWLoLSMB44LWP-lxSjzK9mknEcbEqz-hSdREnCVge-KTBgzjE98A6pTnegCFE_Q9COjvjoBebKQiBYBUQd7v0VOYcK5ur0q3nCPk77TC8-Agj2jNlrAQyUeH_RqzpgNe0X-eIkahaJSzm1-OR_31AaWzFSodQLqCXIySsRdU2CF71ZV9QZzK8t8PTOS_GAf0y3pt-OeB9CH0w3GkIHC0qPjBi-2aRROPUTn0Q79xwzaiKYTUIGfV91vfSC46fcKKoqS-jpAJ_apr7k-kOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g08ySEVQLsPA3uj27JpjqU27-XK_vzGy7AdKErn3cxRKKWhMVFmPAkd3dMsuYpixJS5scfceVx2Lm8ZTm7uqnvNnQWcLNRqK_dSGEU673KSdeRXroGREWAdQQYRySvCnXAVrkglZT8R3da0MdBs1sWpi1VoOyVAgn19ekdEKEgso4AVmmFXLr9LixgWUFG0Skj5ZaurMBiJ8Kg3yGHM9CVlr3mn9YPloP_K7BwcLURqyQEcI_-Ng2jOZk1UicLtd2Cp8jRmm25O8QMcEcm1TaDVuxF6pkxntYmMHEd80QixbAyYvmrJw8yW9aN2GaDJIqXVa5GNl2TPz0sKicnek4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mXRs5OUzTVHJ1w0EardlTKS5kkZo9cGrmnzz5eWCgPftKTHUlKmjbb1sev01KAoN1apF0cFMXn7aPBlIbTMNoLBF0U0TwvXnHvPx8FMPaz0Aznd7MswJQqxjZQHK47Ykxz9dYk25hN4O53mUEBfGoMkYJevU1rujxzYDB26qo67fcyg5KdfczKvAwbgaQBoLMff94Jgb4dQP2ALE5ENUE1iqVqDomAnbQXnRa7UfojG0Keod-R6Omd6tPb9OgmDF_6RsX4tvpe7ZWfYjPG1GMYxDFTWmt_sax0M4xZMOj4i8_8K0bfy6OkY2pyWe6mhp8jmtI3Zql08W5KuBIR9VMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHCj1Obyc-xotH_2T8pUViYRxU_f0rO1rMnQiZ1SudyjrKBufokUVcjyJpmuPWmKKcUdFb2gmQ-1eXVDHAVBQb01JpAr9-Di7flBfqk4nL4j6T_U3ZD28w3GHwTmmGakS6WjZftWbqXPPZDAdJSu6syITsfrOJYldZpUqxB-nU-63bcGv-fOTeEnag9NaKsv19rStwF82kPmGave9bBugLpQy6rY7-i62bzEmjeS_uLxxdsQn2wnRMqp_O1GLScHmQD0QknF5VsVMgwbrcs7kU1KeumH56f4mF39-kt9HlsCRycpB1TOPz_O4gh_fYEFSrZgp_rDED1WlbzJP-Hbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=WtF004wXDpy1vV0LcTpiQBjbAyMWskEycPB0zKJ0Dj-AwYUD-D09Bo1YDNZZS4e0JBxWL_ow1B8LNoVHw3VrgpQMr30CT_3CXJSYQg77z9Kt6fkGh8RwAL5OmmGFgeaVvdzP_m2ARw4uwO78TTH0XaFb4DYep7kkEByy72yUT3vVyHhZX_1JTlFQ2Axu_ZgJPbfQZ0NOQks1cFYmSRxQkuzi3eMnmM8P6npvI0e1_A1YFvUuwVGV_sHvX2wsvMO1KadZaJYdC88YIHqnirZIloSBoBBylOCur8FsgUijM7RGlc8xpObu_3rSp4hpZuR4NmH2cphyMN_p0ZvjULYx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=WtF004wXDpy1vV0LcTpiQBjbAyMWskEycPB0zKJ0Dj-AwYUD-D09Bo1YDNZZS4e0JBxWL_ow1B8LNoVHw3VrgpQMr30CT_3CXJSYQg77z9Kt6fkGh8RwAL5OmmGFgeaVvdzP_m2ARw4uwO78TTH0XaFb4DYep7kkEByy72yUT3vVyHhZX_1JTlFQ2Axu_ZgJPbfQZ0NOQks1cFYmSRxQkuzi3eMnmM8P6npvI0e1_A1YFvUuwVGV_sHvX2wsvMO1KadZaJYdC88YIHqnirZIloSBoBBylOCur8FsgUijM7RGlc8xpObu_3rSp4hpZuR4NmH2cphyMN_p0ZvjULYx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjTWH-osWj6mIqJPRxm8WJSxeX-43gmu955-BPmZcz2DIliu7mC4vOaARTmrmbjFDvscSgC5_w268pUil2f4WeE1jifIegyMNJHjaaFAuMrWT5sxF4bstNZGN2a2Z6Edf6YP1Na2qDDRP7COf2K9aCx8OG2hzq87dhe8I-0kmGzWI-YS2oMVrh60lT7MSr2O6luhLjgR8xTjhB7NKTtt1K_QqVjNk3zmV2xj8GYOL6Zknjlwnvc4T49GRQnZrLwJC4HjUV5B18r2VodelfTe7_djvQQxVZ4Acko80piAAXp-A2-P-FBc_z8ZTIXyjf_BOmqshiwMqLJ3sqnLBMd5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nb310I2GFliwPmy-ssSR1W_-73Hagg7SdtHlC2F5zmkkOrmnTPGGfhv7ZGuJg7cROG5squ9AHAZ4CIAjkhxvERfuhu9zmblvNXSN127ncSQKFlXJZfU3AG-iV-yC8NLR3K7tRjd5jmaT2W-y2hRH4mfVl_VMrXyNmMEVRv-NMOaHctmnD0xdyvt5ZoO541Z7SpmNAqRelK_Q8JY9SUZEHaXnXN7srlrFvGvJTILJxDRuHK4gNBT6jgjV0WJlvxgU3JGP3-qlDU4QCFPi1_IJTx1gpna3zieVb2cwrEeEcHg8KD6q_2sUpT2CQ66FjtqY4eWcKWnP8LEFUbHO9Xmv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojzp8ED-7S9hN-wkKduQ-PrZKWvce2RsTvI6CWRhy9w2mqvv65c0CJEp41udOhOT8aLc_IfvijyiNFeGmfMYEEYZs9_Gw33YbFOcpd0J_tLDWftVjuJfsqG0FWuZ2EXrbM5vf8GHeHJxdVOO9RVE_aWfB6fDVXKLZCW7pDYHejuQsINNIK63L-DeAv93-WFs_tHJVTQSlzYHkRawA_8EX434WV1C5XYNdee9G28kVdAYqEh_f_yn4Soit4NvlL3olsce2DAmtdk50vR3dAQFd8dGR9-yW4fhOh-R4u4CSGcdn1h6ba9SQobJtlUJ05g_y7NEKz96qmYZU00eRv1enw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WwsSJbbwPuQmOitrHpUQTSyUUWEqCqtN2ijLyrURzPBX_9C7tdTwAtn953l0EmgYxzLZAKxXTWXDEZXw52uPughSInWzC6L0YxaMS3jnFt-KKVqoXSgy4av-a1SwJlf8v7d4VPxzzCQgguLoLr8qrS8DPjUdJ-dvcpzg2VcHbEmt7DqviKdGw3dYSdtdCTizlRjD5IaTey056agJnDaIXjXaff67Lcfm4lvyQO2b9cUCByRm1RjRuy3j9oMEm4M1RrIKNLr77npgoBfqo7PrvTUtk7wGJSAIyuraUhHIdEGD6ZMRUXuJrnC9VPXsX5nGIiyzC7f8dFZbhcKEEGQKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOLCNSn7zlJCFBXnG9Qfe_mIvZJhhq4yE--J9tiG8dg4iz87JaMf70k6vnIslf0grrG-4EAuyp-tPEpQj2ZDyYRs2Oc1YWVKrkS8X0iETXjTkvWBPaMpa8NXYazAY1oeVaMBHMrmr6OHUgJ9spLfle8z3EJ0dFPyIM9CnBmvvOMvLCIXOptS7j3InowqthOyVd2pjyy0Hq_2PsV_sfO-8iBfRS7SRRR-W2KZ2yZz43097vBsRiC8mWnUswAKlKzPM_oLbfwWqePA5XhlpwWkr0EqbPGrO8oJK-C0Rl8VCQy_miDgR102UCkwD169MhhTj8Naw9OtnM-jbEVAGdNtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vz7nRm4dKwBu2V9Ddsq59s-obQJuCB1O1AAs7r2jy8GyveIP5Q5KDsLj-yBUUqP6sABQs8Lg80lDWeMUcbepkXec5F6yaeX_WKp-jyk1eYqCKMfeJYiL13NZPkfjsR4dmNDyqbp1Jg2uyd3TrwcJmzEnJ354JMlZyB0qeoc0etNDuPasZEAz6yvSXOpMBBvURyQYusPuS3PoMlxz0kgHyWPSj_xdCJPGMxVknsUqbHJkfIAgSnk2hBb380Dsg4gHhYGeiCrRWB__bpdcDN0-ESQMsmPIRAkLblCKP6tVVxKLi-L8g243DgyAG7Qae_p1zdR4FI2ZPO4_hD0LnDn5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cN7LSeTVeHBAr9rdnoMj1CBVgdSzf_aiG7UHHIqSUhdJj0HFe_dXCyjStjzrFWbg1uW4fe9y2ON1p3oo_NNqK4ikJySZxlWLzETCThzJngrbBaoROh3Xq1u_FKOXJ-d7-6-zxSlxgGtVcXwYj7M_PH7SouGvfBp7mC--EsYOgEIyVS13PF2NoIUhAPlqrDH8vp7rC4TQVHSlsTmIV3cKi6bGMugMQ6CDxeMQwAc1huyIa2_j4b38NftnUIgEfBhUrYbrRl3bbRMwpU0BVjVxS44HVTO_HR5OvjNE4_Y4FImVwIH71PEdiDPJmlqoMIbC35l1JQ8qZyPljFug71CUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfJB_8sjHKcaMCcgZ5ys5OIYZpTJniKP6gcdX6EKhr40BNshBGBqjGuwoZH0waxoOUiW0S5KntH-DXAOCvwzoOxQ0ZB1S99HmQVTS26nV3qD_ohvPW97gceGmwPpddbymEI_anwGK5Pa6A3CxS9tbKU4nTKJJ5bgkiy8buIAjFLnr4zErKVtXhJyw3iOnGxkLoifq202uBoze2HYVU98FfqffygYZoVrCG_tx-DEQUQNE4iEd6DJHYyKE0Au4bIxzG4XlcyEL5y3QTX1DM85x7XG7X6FC-iC5rj9ozuIvGC8p8-DbNin30_hsBoROinGDRcnau_OE7uLx4-hDmA-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dSP0TQHPHWZbdUe00OMq9ZhsfLevSHjoalNWB69AMczsgQpIt32JzWGdbY0dzSzHHVujHYGBq6WChJr3seACdhn-7C-_J2fl2TU7jSKGz2eufVNMWr9QGXgX0rXm4qM49giJI5TqCwS-YvPQ58OkFDpAI3yYYwLgzZCNjosCatkHNaGYcaRgihqf7qbCPZs1xW-xoyAwuvmQ1t2vQoZcqiPGs4rNyiH0GUwDVRjm46dhM0iAm-p7J5t2TUyRkZUFhrpN65EOafoekqpZX3jeKtVWxnUKbCEfw5wnJV7WunQj3QGMboo6XQc_WbyW1XbUke7j0SNnTGRSPktsQspmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WhtUFg_Z1AnAbaBdDdGMLbIp7ce2NQof6IdpaYsq_7q1j4-oxD4Ak758u7uvfHMsbpvQ59aRAGeG-qT0hxXVsjkZYyysmxsRJ_IbZzFaKkleJYMd0jYFzvzjJrdzZQRAdeX7kJIewXjpbZKgbxfvo23Q8hkvrN9D3JQrxjSVzjvC1X48aMil9i21-jUoW3wDJSSRwlmtlrmnP_aN4jkv6jqreUtTcoyZrvOuFGt0weHyKgpkY10kx2C_Hk07OFEzkfsQ9TwVu1xXA2vNaf9wuzCC1qiSEtWPF_tF4NPZgrYCmFYAhAecCxKjnWsZ2Z90Z_lmvSMznejeJxC5aW-fpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=HFRcoH8D4-U93ljWsLiNffQBHQqwddLxh2BQmrHqFdx_AESHbEGcdvdeJLfnC4DpOBoYIOl7WkqEfnAG6OjuzqlB-AcqGEGZl2xa3jVGLDMKQbQ-5gKmmnjdNNZMxP7sAxFDgpssEqBslAVyj18h_QvWAvpt3VHBu0S-4TUc0kNZ-eS5TZklFf1I_xxlKyuLyVtpkHiicXee01EXogAQYsTmNaQYaj-UJHunQxLHKxAo7MoE-DcCQDiV5n6PLfJ9JRS2dCj8AAsx0dftBZulMTkhcAUxRFq5gltCOdV_DDX8eHl5EJ1MtsuV3iT8pCr7sfiPRlX56kK_tz5LlR7qsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=HFRcoH8D4-U93ljWsLiNffQBHQqwddLxh2BQmrHqFdx_AESHbEGcdvdeJLfnC4DpOBoYIOl7WkqEfnAG6OjuzqlB-AcqGEGZl2xa3jVGLDMKQbQ-5gKmmnjdNNZMxP7sAxFDgpssEqBslAVyj18h_QvWAvpt3VHBu0S-4TUc0kNZ-eS5TZklFf1I_xxlKyuLyVtpkHiicXee01EXogAQYsTmNaQYaj-UJHunQxLHKxAo7MoE-DcCQDiV5n6PLfJ9JRS2dCj8AAsx0dftBZulMTkhcAUxRFq5gltCOdV_DDX8eHl5EJ1MtsuV3iT8pCr7sfiPRlX56kK_tz5LlR7qsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IaIddYX-6EIzM3PnMXP3cj6h4d0DvwEvhYCQ35qE0G-JSuNO519iM8Iy5XVEg0IHDrtws8K4fKwwOHmqYIJzTxT_KDsaODJEV5MMdHTrHZHhdCqtmgTyclpS3D7Rpr-YBItocKeiQVgbDeUYux0erXbTwB5TfJDmwqeGpky6XINE00aRqWPS7PPE2M7TEw_FSi1mIgHIY-nvUCy6BbTmIB57wqC3t-RARhB3gV8ZEaYYToM7KT3tTgk-Pj2Gdc88fM80V0hVOgAReMtRuTQ_HOUuS7P_jBqHJq-blq4IjIl6tMBq9tGHhs2g-1aJkXVRZ1tqdiHfbFo5kQuij6WsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=tJkFVcOVZkkd7u7g6NIT7Bu9xai7t8nME0AXczfKpYTTjLZVD3GKE-nIv6B0vuUNGDl-MdOMc4z6SdgIeyHCFPIyUjsf71MjVqtCsfXsgS5yFOr45Xb-tCb21E3HhpQB_p-oiz9Qnl_sFjIhN1sw8-0lLAF8dQ-m6oRp5h1eDg_2ej-kgE-Gfon-Irh7ETboMPRXitvGBtW3ygNrSi3j2JaU6nu_Olf7IVZzqvui9oNUTttRpHCN-d7J1xG6PTjd2EOgUZ20vLLzmVHq_LBoWNVn4loCtRrHPnIXQinJv-_dQvJBoKLBeOeJUDQBljVuzJSIlCBf-2w4FA3RYsZ45g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=tJkFVcOVZkkd7u7g6NIT7Bu9xai7t8nME0AXczfKpYTTjLZVD3GKE-nIv6B0vuUNGDl-MdOMc4z6SdgIeyHCFPIyUjsf71MjVqtCsfXsgS5yFOr45Xb-tCb21E3HhpQB_p-oiz9Qnl_sFjIhN1sw8-0lLAF8dQ-m6oRp5h1eDg_2ej-kgE-Gfon-Irh7ETboMPRXitvGBtW3ygNrSi3j2JaU6nu_Olf7IVZzqvui9oNUTttRpHCN-d7J1xG6PTjd2EOgUZ20vLLzmVHq_LBoWNVn4loCtRrHPnIXQinJv-_dQvJBoKLBeOeJUDQBljVuzJSIlCBf-2w4FA3RYsZ45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRqXtNH1ufYEIRvgVjVbNMZy0LpzbfOyzrEJ86W77Bne8jWWqGkzam3EnUssvPP4gn20dwC4fuc4MOjho0hW_NuU3fmkb1Pc1ZfV7OTf96zjgV5uDsAXu5La5epNxLeJwE2Ed5-sriMGMOPaVMhhT0jKvfcuPg6aJ1j62e-tEuslKQbcFxETXjb0JmWw744W9kegM13KyUz3jKQrJl6wV8DPB421uklj1qclunMCKSMtVKH3qzFk2GSLAgd8JzZ6FlgdKoMKc7r-xl-nArNKFnzATewfaXyIIhmO3g4dVNU1Q3GxWQ3RDbIHE83c20xBdF9yXV7UTwSsQEBfwJqW-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STEPlx4qadXpZz_kT6mlqimVY2q670zjwVdLkMn5b2L_YwRIGay_X7UR2K-YWSUuIlgqNrk1lAjyzScaYOAfQzZbRt77kKR6Fs6s71vsVgLygTU1kDQJWg_HTiC5OW58BJFrdeDnko4wbLcKTfJOa3L43fz4qYWMyEDTWfkiGY8YrOMqBOO4VraRtfZkEZXzQiVOrr6jNv0NItwlxM12UpLby40JJymIKThFRJVaMvgtsr1oP76iWZEV0beDNoEHBzyozXvrUDgKOjRSsEbLWjK0K7qttOIGjOQ6H2liCwUL3k6cyOVhbQFbUeAr0Pgw-CGPlZSDLCuvXBTl8xeSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gp_ZPezl5Tb3dGct90Ot7s7I_KwvUxbit-eBkRwsySOnnqR2-rCP4KleXGVmii667tC8IlpSZ5c7gyV42bFxk3fnc9_6J4A0fWOJqTqoAzTL8EuBrSvErsWSKDgt56BSgqGVqgB6htce_pewfCbF_ArNkhL8p7wzaHZjifVW9gwKhUZFd_NoLoT-5czp5jeqGxUCrIlTLpLlkmHEuYg2-cEsW202Nhn8N4IrUbdeDRqRVkj39I3QnGu9DI4NZ3q7SHVwwp3d7-rizI6_riGiFjZfIhnzeitglxx_ABXhFojaPIPh-4XGz6bxJ_qoqYE5zu-LBNTVvwNRTvBt53AVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVxxBiLigoSAPytvkwG3-O2udB7CP7JmxayfzYQPwIYAV-RjRYjrC_eTlTDM8EVc4MO7jko_C-8LOk1GvOLOfHa3SlVIGsr-aJdjjMvfVWY4ci0PuBmuQcjV65L0b13zLRqZvdw-Nh3nGCc7phFg7M9XMwWXfFlIeH1FMncrkUqGSfByDqU3Z-NfS87yY4LMDLGFII2Dj1xWesywnzILZG-gxy_GXa-_j_caAqbMhZDqmqAhdzawOwyLY6E_d1w2jlYLGO95Rqpfoe183aa9-oyZ1eO7H1Q5bvlSZfvwHSF0uyclvBDt239FkK_BemzBbu5mrRpNQ69pgsJ2LmzP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=IHhR9IerdVnzNFUBEssfecpaRgo417YXxtgYMpJNlHNWTOeCKpV4c1oxBJwuiJt0zBBGuEICOzAYk0navBS2axWgeBpq0OGVYUTY93xLPXyOwP9JrrFKuC8PypZjaDLK_o2LiXRXKQ3w37gqeMY57Jbp2t0-iikSEf3mJzjGEu3QQOG1NdQhy7MFe0KUAZeboob5DRUg-o63T5EqMZShZYSfJ4dskf4j8NXvQ2kqc1_KEoEWsvNcJ31yjKqo1eRG0jsar2qlf_m6MCmJ5nsKIPtv3nOauEQI15sYJIHMEDCXOGMWhicbAf-uTvl8_jQDwpiVrSoSu2eqBfMQgv9wd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=IHhR9IerdVnzNFUBEssfecpaRgo417YXxtgYMpJNlHNWTOeCKpV4c1oxBJwuiJt0zBBGuEICOzAYk0navBS2axWgeBpq0OGVYUTY93xLPXyOwP9JrrFKuC8PypZjaDLK_o2LiXRXKQ3w37gqeMY57Jbp2t0-iikSEf3mJzjGEu3QQOG1NdQhy7MFe0KUAZeboob5DRUg-o63T5EqMZShZYSfJ4dskf4j8NXvQ2kqc1_KEoEWsvNcJ31yjKqo1eRG0jsar2qlf_m6MCmJ5nsKIPtv3nOauEQI15sYJIHMEDCXOGMWhicbAf-uTvl8_jQDwpiVrSoSu2eqBfMQgv9wd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gpron7fxl8ahVfLA1EHCxRUYKBPQAWcz83tAsDR2tHSVxMo3SN18yEK5mkiw4P5VtZkoAez9F7qxlf0gMv3TPQxcUgJidj2LzgcJ5rdRPIKU0DRsEvv1O9URgENUgYEMe638cu6_LUHN9hHM5H93FtF_-TPlztPiX6rG5ty7OB_4YAC0RkqDH1xiFvXY-PVVcZH_JvNtVzMYc3lJmMPXWZs2bK_6851SgE0l9skTSxHNReriTxWQoY2ESOfSkvp3ZjZJOU-l182LP14S470OQMQWCT_5ImxvCZZJ49L6ZYnur-xR59KpHQD-ryjxsa3a0UKyjw8D_N6vUVWWU1TtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=S5ftMRilnxKAH7T4Maqugp530yVdhgP3YRsgMYsVHmpGMGZjdd9BoHeHWLjcolpOztVXrAAlDnyvOqjX7h27zcY29Q5xhVyNJYENxIVYQ_ywc-hjxZRRbw1Onzob3NWjP_87_XfTEXfW0CWGrGSVCuwcbQzqalZjqOOuDcneB5SktG1DSqgyAp4sxxOlydF8c1q_p4_choJnu3Vfyy-jGP09dKhF2lUvoapJYw09iQYMUiEFDEENmf9nKHxv2J-wEexotqmyJjNLEMgqSRXprWVv4NK3puHVcWqOYHYMddT-e98zi87eqBzlgvIW290EwzjVq_YTn7hgvXz13PjHfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=S5ftMRilnxKAH7T4Maqugp530yVdhgP3YRsgMYsVHmpGMGZjdd9BoHeHWLjcolpOztVXrAAlDnyvOqjX7h27zcY29Q5xhVyNJYENxIVYQ_ywc-hjxZRRbw1Onzob3NWjP_87_XfTEXfW0CWGrGSVCuwcbQzqalZjqOOuDcneB5SktG1DSqgyAp4sxxOlydF8c1q_p4_choJnu3Vfyy-jGP09dKhF2lUvoapJYw09iQYMUiEFDEENmf9nKHxv2J-wEexotqmyJjNLEMgqSRXprWVv4NK3puHVcWqOYHYMddT-e98zi87eqBzlgvIW290EwzjVq_YTn7hgvXz13PjHfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vp87MlYfaTj13Z17Xw9wFLwooFeTAVEsLJaDH3_5eGxLA3Tnoa2MJpBjvSIOlYlz2kq9xWq8C0I39xz4qom7dOtghr1-h5ury_vVZr9iiqzU5pFQsXpoBotxAvwEBJM4VnxBbMu11oCdwSAQbGT6xTQbPmD8gc2PLbB9vIP3hEt1yuKEISpAczhtw1MGGAf1ufFhUtimOjBx3bzQt1PModqrwsg3CEz4fY1E870TIsWMGB_X8nwSUg6U7ztjyQydttMBLS_sasVq2RrvzDq5X5_9WtgTiP7EFJ5i3ufBCNXOMYZ93NLfaQFXn4LHDFaoo5YCbEKRiUEi9U9X2xeD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=gtMQOo4r1bcPAR0LLcJzNrQhyVEzlVGM5eNvyWnUa4Hx7625OQ5KrNXH-oh-4errT9Qy6HEbd2OpBzxFVLJ5PGM5npCILGlH0GFW5W6kEFcccfiCJ7hGCoKOM2U5wvKNi5L7VsEXK1N_6pSach5Cja3WufqTu0FMlYI5c6gZg9lHhNO72Ig9HbtoQnkfJGMN4VHbsk8L_lEKh2yaHa08RlARbtOQcoauRJq7hvnlfi4yYrlpVKPGzxtQKlNL4SirfhVMTQGDMJ9gDgF18bNh60cSMM4I5VqqmQkcyJ8vPxbWzO2OmgTSWjpOnVMVqOJiWQiP_An-BhK7vu1zcVaB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=gtMQOo4r1bcPAR0LLcJzNrQhyVEzlVGM5eNvyWnUa4Hx7625OQ5KrNXH-oh-4errT9Qy6HEbd2OpBzxFVLJ5PGM5npCILGlH0GFW5W6kEFcccfiCJ7hGCoKOM2U5wvKNi5L7VsEXK1N_6pSach5Cja3WufqTu0FMlYI5c6gZg9lHhNO72Ig9HbtoQnkfJGMN4VHbsk8L_lEKh2yaHa08RlARbtOQcoauRJq7hvnlfi4yYrlpVKPGzxtQKlNL4SirfhVMTQGDMJ9gDgF18bNh60cSMM4I5VqqmQkcyJ8vPxbWzO2OmgTSWjpOnVMVqOJiWQiP_An-BhK7vu1zcVaB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NTaSUPvNY75KTrl35y4ZWMWv7PWaP5ddFi4zupKhEDHeTokUzWfMTw-WztnK2w79ZXz5tmQaO9ODkJwcY7P4jSDW4TKhpx41Gc7yDM9418nJvz46JzIF_lzfQMFZsB-kcauBXUI7o72TgM42oYrIMgseweY7tR6SGBz9zq_TBK3Bd0y1lC142xZ0KK48vh0giCgcSAlsYmoA4yRT5MmxrvbMaMIDZi-ct6XXA-FZ7rxQ3TlvETxh4GaBcwGwQqr67MdkWmUpK8PySEYMkt9NLBESQDj-iREBCY9BsXqMa4ewp_ozZm27XVUIG-qquJZ41nj8CL4OCEWb3AHbLWoHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b8kcFygaZXhrtRAORVatjoi7JfFgV664tf1foDvrRRIcXFfGxg6GQztZw8lKheQsU6xJn7SQQM6cPHJzFccODmH8Jo3ZrxZ48Nr3Qy3W0OkQy5AY8ZZindyh5HjtEf2oD-Xi3E7Re4bbEfR0e6ihN0B5-OmJV64nkFHIp4RnSzR-7PC8e3XNbyxo5KNJJOyvH1q0jswzCltWUdBsFFv__RA3rP9MhbXcY_LusM_RpC2n6EhZEBSAek_-BZlZuSRqX4ioONPeN6gkD-QGeS1mv_Oc8-FHw6nwVPuEj1KfyomJmRMcHxJwJpoOOCXW3yEyL5fnFmCVbZ9MaDtzguIiLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WwXwff-Xe1PzE-ZikjaU8xFiTtJYCylTok7Dm14BibXn2pcUnghB65kl5r_Uu6x8K4rODonZq4WBHHkqa7JPNPf0tXtOqERVse_gefQzxgHiT5YBtfx16o_ZSVSfuFgTe7U_UehiTvwlyX8DVvJta9WXzXKotID0mtXgscM6OibAmQVb8eHou7v7BTv-zM6JZhurcYfyxeZJce8p9B5bsR6_Hc2S2yzvRvivVme11XBDOfPn69BNrRf6RDgycYYLwHPDtbjFAWD6WKHNy-h7Ugf6AAsphoGQitZQr7JkRwwtLq1jnvYmxufTj-mQ6yaz8OHftOxsM7kFGMxvngVwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=JuoZw-_NLvwQmO_gcNlpn9P_42jCKnSA7gAI8ZY14gY-aKivsupxpBjTpZyld32C9rG0VEg3tU_rdBiRb7TwtfontgbF8Eydyfs-1_-AcpzGjpjPQoFLv6KIXtbC-qZPF0D1fcq69ExoL5ghMJ0DHZAWZ8olWspt2uaC9p4YYpB6Lv9J3IZqIL_SvZ3CPzx_g-34Ksv_owvyqRlVSo6fUp_35Vbt5JLd_NSCMuwbK8sZB-NNShNVWnTJdi9m7OR7oatxT9N_e3Srbe-YvDM_sH5eztWv-goY5OxfHVLE_vXjNJxanMe7mdEmvQVSHvYgK4eJeLxDG9yBILPIzbFnpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=JuoZw-_NLvwQmO_gcNlpn9P_42jCKnSA7gAI8ZY14gY-aKivsupxpBjTpZyld32C9rG0VEg3tU_rdBiRb7TwtfontgbF8Eydyfs-1_-AcpzGjpjPQoFLv6KIXtbC-qZPF0D1fcq69ExoL5ghMJ0DHZAWZ8olWspt2uaC9p4YYpB6Lv9J3IZqIL_SvZ3CPzx_g-34Ksv_owvyqRlVSo6fUp_35Vbt5JLd_NSCMuwbK8sZB-NNShNVWnTJdi9m7OR7oatxT9N_e3Srbe-YvDM_sH5eztWv-goY5OxfHVLE_vXjNJxanMe7mdEmvQVSHvYgK4eJeLxDG9yBILPIzbFnpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNbpv1YxBhGwHxyTO17Gc147sYX4yCwHFH5Aupfd2jottAUly8h-UlJ0tRBt7bQYaQNMejDj7dCAQF8MLcDdeXP__Yn6wqbwpBJhP-02_ialvS6iiLziwWSekualRJGgHl8dWgj-9-h_MB77WMdQ2MFQhShywh18iNJb6OHrRZZC3yplMy8BjxLU40nPn7BSqU9gwZR-ubIK9lhU1ucqFkCLv_68mdCkmTETj4_T3CZin-mTVY6GqwvrPvqD7htsPfmqNZaSlZKOFGzciasDHzLVSAGHc_XchqPcJVuwabVGY4AQL7kt0jreWtifuaOsDJ8CVxWFbw-yIDJc5Y_loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JUvGxq3yF-o-XAtD_qfmdZGD5VCEeb0YSwA1ptDGMP-gR4qIqesMe5_XaNBAQ41Hpc97G20DBhTw3p74cikH8ceUm6ZM9hFEm_3YRhhNjFfSpadCljqBMm8gu1LHG88Trlz9HwmOjlhUXE5G7nTXm1qDRfWlnYh61dVbL9AFEf7x_EtZcRFxalSWo5R4V3t1uYnls7EMVucnml_sCUSavfiELtPqdqw8V9Ciwz3pHwqZ485lsv680FI7I6xMVuyEryDJp7rKmFdm1jZM4LQJG7hva2S5RUCUUB0W7kCPwmAMPU-igrhejtKACjzA1mWOm_RC3TZohUgsEStKpaepJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=QpI7tV_hmrHYpW-jpB_cTZKR2jEptbH_K7Yg3nUbex5X9YVhtHnEfCHgUWGmUI0wIyGL0gC40sRC3yu90PSKcnOLdYJzp92aWgGugH5FKO2NGKKFThao9ZyYRUgxrco0tFRusBzQhPTwayGimosbNl86-rraOREokwqmL75YUnDMxidLgcEa9JjM5_sc0foZZMkJJT-EBjMS5qB_TMGvSx3Spotc8YjFiKUBFNxJpE7T4txKjMpF_3QhltoryTFBsuyI2RN_Ngkd_pXsxEY-VqEvkx44BZGyGrJK2YclnrKN5n-Pq_wOhXy3OJlOJ7ibV0u_0ruKkqMcVGXUneNMWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=QpI7tV_hmrHYpW-jpB_cTZKR2jEptbH_K7Yg3nUbex5X9YVhtHnEfCHgUWGmUI0wIyGL0gC40sRC3yu90PSKcnOLdYJzp92aWgGugH5FKO2NGKKFThao9ZyYRUgxrco0tFRusBzQhPTwayGimosbNl86-rraOREokwqmL75YUnDMxidLgcEa9JjM5_sc0foZZMkJJT-EBjMS5qB_TMGvSx3Spotc8YjFiKUBFNxJpE7T4txKjMpF_3QhltoryTFBsuyI2RN_Ngkd_pXsxEY-VqEvkx44BZGyGrJK2YclnrKN5n-Pq_wOhXy3OJlOJ7ibV0u_0ruKkqMcVGXUneNMWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=V14_Nl_9NHWJNkFDk7PzpQCUuSY9GZktiCGQBc7Gn9IQtoV2mvr1So5iGN7RVwjHCiRpdVsD_6y2ykCGXuygg_dou6Jz638gKH9QoDv_HUbdV9rszF7CECxPlw9VhPGkO1F44IvGZhfpviYe-HadsAGD8EpHwo4S7K75bjnLKCiRCacQ4qmPH5wr1dnY1TpQtSVCn2jBou1kVSe6HoBTT9ngVK4WFgorbqg_LUVacElWWFwaorcQc2tAGWFiWyX28XDtoBJHusA4gWaQz1c19_5j41gCDH1Hb7SS2cheVvdB6Omi9qyWdpqiDUC8ljlf501PsW6BHjEVQU1GSDrEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=V14_Nl_9NHWJNkFDk7PzpQCUuSY9GZktiCGQBc7Gn9IQtoV2mvr1So5iGN7RVwjHCiRpdVsD_6y2ykCGXuygg_dou6Jz638gKH9QoDv_HUbdV9rszF7CECxPlw9VhPGkO1F44IvGZhfpviYe-HadsAGD8EpHwo4S7K75bjnLKCiRCacQ4qmPH5wr1dnY1TpQtSVCn2jBou1kVSe6HoBTT9ngVK4WFgorbqg_LUVacElWWFwaorcQc2tAGWFiWyX28XDtoBJHusA4gWaQz1c19_5j41gCDH1Hb7SS2cheVvdB6Omi9qyWdpqiDUC8ljlf501PsW6BHjEVQU1GSDrEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=I_E0ph6dabAQ3Nu1PjV1qRL76JoYyfq8XHspJes5--ANTbESqQ4gOCHYC0jaEZNcmG7xeMqr3xdhyk8hR4t1KLmXUwzBKapz2LZYbh7_RvwmVakydDfchAPn9SZPwnKNxsjX1zhBENEO6ugKMewa8c6iF5UxUnvHwHUqhEv-BBqZPz7c7imcn1SoBzO7v0DnD2lAHrRzGwhdVxx9uDYgrdia0LwAvHfjQvVgwSptEkbAIlpP4FdyKffeFaaPNugNHsdznH18QqtizhAseDkrr48IGS8n7AFpBkuiK2NpNzbVdxCGcjtwA5mfyHxPB1U2MZzN33WjRp_ZjDWVh4f7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=I_E0ph6dabAQ3Nu1PjV1qRL76JoYyfq8XHspJes5--ANTbESqQ4gOCHYC0jaEZNcmG7xeMqr3xdhyk8hR4t1KLmXUwzBKapz2LZYbh7_RvwmVakydDfchAPn9SZPwnKNxsjX1zhBENEO6ugKMewa8c6iF5UxUnvHwHUqhEv-BBqZPz7c7imcn1SoBzO7v0DnD2lAHrRzGwhdVxx9uDYgrdia0LwAvHfjQvVgwSptEkbAIlpP4FdyKffeFaaPNugNHsdznH18QqtizhAseDkrr48IGS8n7AFpBkuiK2NpNzbVdxCGcjtwA5mfyHxPB1U2MZzN33WjRp_ZjDWVh4f7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPrsHOFvN88rvoPpBWA9Qbrtrowpm2pVqFQ4E8-ELlunnk3zZtH2u8cmqS_j4iE-wFAs6Ygd-C2b9YVsVa6sAOLru7l_YJbihNwPueXSWjR_6YUYnm2cwW0PTtYzcvCTE9iYIBJr21V7tbqkEMyEDBExV8lX3M7paYa6H8_pyzGNSqidwzDSran_NbbmtuZBc3wiepGE-LgbqjH_Rq-sxTSaqV30DA2YfQX576tnF-DpgVrcym-TH1cVOWNkhvgKrrar3_uHiL-USy0Nfnk7VNKoe1yj7bduNr7-ctccmOaAy2SxwzrXR5uQ0asAoaYotBy0O52dqTvMRGr83uowUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMz-IJObGieeZp_gR42jvecJpjEIz-7vK4d5MhqiLGRmelixAC02pIwDri7UhOvpjQGKjmQThKiW-jLZhtEXq5SFxLrMjuv8QkbBCh_1oGsgIo1ES8WSzvh6xARRXjFFqCTAYiXAKN-6QuaHF8R8gNz_UA9fcIIQb0yTUFGiu1xbE_0BDyKBTJYgcqvQHgJH-xsiqEo2Hy_9imhWSr6sNwm5wVEP69S8X-4qFP6JF5QMZettaa88sMbTGqYErmZoLlWI-RuBVlUTlmAUil2yfqVpXIVOnlp5tG6eJGIQp8rdtbXkHEC1MwYpdwG5UruJNXr_WAnuOzaxCKXNFy2HsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0sYa3slFZnkxrQTUNnf-UD1CSGNWtJs3--JrmGUVqv1h6Gzqm9o3BMRjGMoqnCrCBDVJhhUSYL2cz_qhpw5W4w_2C3n7qbiynUm3yciviCedXbmFbOqr-kA7I2QogouTA0fRGtXWX3oXTXYSzl0KRcLaspv9UVAxGpPER9ylKd0yWNwidPndcLbi-GxjO99RKoVgNx_QFr2hWL0xYH2Ez300nWasD8rUui_Hu1BMQpJC9ckV_HNolCjOKGDEVuJJqALGECfRj_qxgQ8e5Zm3_rzUl4KNoi2fRMSJAwctWotSbFkya5hD6Szsq8YI6cw58PSekZvfddSVfneUj4ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrRv7D5dbUn-JEqSh-yxtSExh8vmclDGheg5tDszGSkC_z-SM42-Gm7xd5QZhUw8JHL4ZWgx91QOpD8QzaVBQD7G6MpA48DO3a0vfbIi6FwPipGNSp2C2mA8wDgwM3-iHwKU9eJpZuGjN-xXh6U-VPzQMHR9W2T0Hqny2MU5Sr3xD4Eub8bNkfIoMQ5OlILkUrFi0V-dwdP0CzL5TQlNDqmlCqNIQV2dBcnH1NLrNxkAOrEa3YW2h3r-skmXudhJe5UnnXbVwGYIt2so-JcKwViQYeuqTVIWWb1GtY00C4Iv9RdyQ1LQ2-rVykL-f3-o8Q3eZnWbOdPdkzEJfr5k3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgvCz-mynVSMXlFWawAktoCK3hu1vyU0Rab_oyj64v_Zy11TClTKStqMP_5cZDjzmmb6_4AG2xST8DtbuGhr6hRldraHqYE35HeIDbGvkun4F4EQLGSXZN9vzSFu3HDY8E--e56xq1r4t_AU2hLgN4ZQCL_zgbRnD0BedJORFp33N45XCM0tdXFdQNn_yZW3qYGf1mYIVdxpQ7ZP7vZ9NlckQcrjW_Ejen4UHU9UDlunG8FT4jDfLL-V0ZnAlCSq6eNI9Pg5nZlQy2bXJYYE-MB4zKUafZestO2cgoqwnCKONFYDnOmhNu8m4hBmrSsRMJQMKEKAr8j6wuR7PlakeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDoTp_00_XTlmMVN70YZMlDp2Cjp51Ajk6mvqBngzg7ZD4cJTQ1ohHt1d6gThNSohRcHrAm1dOutzPkR_0xAQDpAvud0nR2e3ikQNhuVbDFqqNg7IRREE2LP-LEi2aYSP6bA-aedw9tZOUjhvFTfJ6IsbQFzeFNUoRQsg2nDfnkBsMkEf_4bE4msLqkQjO5oBRnsSyXlbxqsgAXT1EGSjqxxwUaSBT3jm5N79Jdm1otHW9W9pXhpdlDzNk9WmDt_iqyuSnAHQh9lB36Ih9DTLDk8KftUKdgxTaGIc_-dQPDNF8NVASlPgyKpCitgOBM2-YaI31uZQGEvZqWgKkYK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGwhLyCOjyHoraw-nAavVg-T-YOIqrAjPfqlH51A9x57jr3bSJPMmgDoEHUWQaK8CtZq6JBFwTCNR-Cp8RgzsA4m20-_SHkkYDXLsJ4-rR1JZFEbOK6Mg5NL9lW5EEww4kCj3Yu9Nc8dXQSgfrt9SuaT2asZp2MGu96hGwQbs5tuHeVTpuV6ndVShKpL3P8h4Q3kuzmWnOX19PomKJ5Z8ot-aFociCBEGUlttw2CTvZl_KsUzCkARUdXrLXPoooIBcBS6FOxg-I1Xp-0YJudeaffE1Sngf8d9xUjVOiYnTs4bs7Va8gKDzN9SlkB62fq_JBRIfJTUz_j-AqdOJwrJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=E_JwesVWAkiyrnL9ISxeXZeXnFQCrrj0PhoRnGCaN-uh4fjwLN7hofpdIPtZ37ljzdxyhUvWl4MunRS69syXgAjwgxPMKrHfTJ57q0f2Me0-flai_UJi3ye4v-ApvqoUKLB4hegaZ9reHn23iHpfbXHFxRAA_52SCslTght6CKkh5kLVaiwroJnpaFBy5VygB8huHElMyruqQ2Rvdrr2iL9lKYIXIgVxjVlJKvLVRDAXsgNfsw1TnQ--dn5LTIvCvI1IrpCSbHUk53h35FV_kqpMI_wQCY2flRGFQZ-3HwHLAdf0Spy3JZkFAYyBjG4P3flJd6sTrMiRd9-_8bNsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=E_JwesVWAkiyrnL9ISxeXZeXnFQCrrj0PhoRnGCaN-uh4fjwLN7hofpdIPtZ37ljzdxyhUvWl4MunRS69syXgAjwgxPMKrHfTJ57q0f2Me0-flai_UJi3ye4v-ApvqoUKLB4hegaZ9reHn23iHpfbXHFxRAA_52SCslTght6CKkh5kLVaiwroJnpaFBy5VygB8huHElMyruqQ2Rvdrr2iL9lKYIXIgVxjVlJKvLVRDAXsgNfsw1TnQ--dn5LTIvCvI1IrpCSbHUk53h35FV_kqpMI_wQCY2flRGFQZ-3HwHLAdf0Spy3JZkFAYyBjG4P3flJd6sTrMiRd9-_8bNsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7DE0IJg4dldnE7RMai3UCyRD2NYK8VOFSInHrBabPuc5wabfuIWueCU4b3W4wMufY3cSKJEmSA7WwBT7UxlBVQ8zgGGHMyjUFFO_gKfq6X7SlCPwtH3WeuNMHxWmspaXXhmNUXfbnXUu-0RSY2QwEzdD232q12Zdx47pqeB9KkLRt-7YbYbh6-SMub5GkjY_ECUWmGI3xzrdzrm739D2ofgonK7pDZgFO20bNrK-yIvabROiMOYKrRrUvJqVfRkahzkm5Fzin8i4_RiOAX-tvhQ90hzKRFQQKA7qshNPve-0tOFFSNnWdBxDfkBilfHGpx-IjpWsRszAM5dve7n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5Jli9suH2g5n1Vs0FjCw7381LLa2__B2UgMs6_Y1eGzwLLUFg32vPpO_Ws30qqlj-HPSfa3UzAyyP03UZMNxPYM-jRepL07NAdx0g8bx114FGOMkalPE1HtRjMmZrJhdY_FgQmpehhn11wckRZkmF5EW-DksYZu_EPeKBYgwDB2UExawZJnmuooUX1I7IXDhzh6cY9yQwo4Mc7FC2YW4ihHpYVKbKOWDDe_0htAsNyLynw3iHKNPOgq5vE6QvEvTZW-f949XqukLvZlEVaBafsPWNHrj8MZkr4TKsQ75_Udof_V0eRablw5QfdO6OdiG9JJGW672JPmlSZa4jB97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzgXPhRRHHV5657RRCSPMAALXVcHjP0-YlRee3f9K1UEpNxA0xZ92r7OUQNZZcvqv59ZjQ4LxORTXGvhultU0HtNG5FUuDlkT292MihXp5tYxTMo4gKeQo9_9dKVCQBVwLDCLas5mHZTMIdVyfeaReuLoRntPSrsnoOPb02pICDX76vikFSnaBaHBUDHhn7QYoj1wDhJKccieon9Q--wOTQN58CQo6WxYnFaVT-rtVegCf-JA2SVsNzf-NfvhndYZKKm7P_F0AyU5iHmpjb4K1rOFZUVjDbPD0JBSgRWVInFMOamNMeaSYm12tNcKY31R-sZ1jx-LMs6VrP2BPM0bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=ddRA1Yni6Zt0jRNO_ZsZYYUmRshYe5jk8zPcafKib8S7p-Vq4Lr_pplqGC2DrnnIU0_7xGQ4isGuK30q_DehX7lGUGY-WjnLbpPAa9-odxFKdFKmuPSkQC4mOqcnotSeuGSVGs9sUP9YevcDSI5Af4u9qZxSYOeRRNRmUO-9fs6GwX1PBiDsmqyWNeRn4nceP4ov8b6vsfu_PaFsgzlZBG3nJCX3f8iJSjInRQ8y9VsV8JeqFejxgu-aVBDYCuSnY8UE7xeC5hDXRdErw6avSVY3ToN2Urk58xAcp4PdBdk4tjmxLBMQjAnS-ViIMvbNcBSPcCZIjggAW_VgctnMFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=ddRA1Yni6Zt0jRNO_ZsZYYUmRshYe5jk8zPcafKib8S7p-Vq4Lr_pplqGC2DrnnIU0_7xGQ4isGuK30q_DehX7lGUGY-WjnLbpPAa9-odxFKdFKmuPSkQC4mOqcnotSeuGSVGs9sUP9YevcDSI5Af4u9qZxSYOeRRNRmUO-9fs6GwX1PBiDsmqyWNeRn4nceP4ov8b6vsfu_PaFsgzlZBG3nJCX3f8iJSjInRQ8y9VsV8JeqFejxgu-aVBDYCuSnY8UE7xeC5hDXRdErw6avSVY3ToN2Urk58xAcp4PdBdk4tjmxLBMQjAnS-ViIMvbNcBSPcCZIjggAW_VgctnMFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZNjQ9WZFAc6sSi4nmfLpz0FpGZ_-OXboQb3hrPw8vyzEmBt2zQucVlRe9TN6EwikdZhMP7LqVq1v3JonuYnFw1Wsyd0b31cheQoSUydlWa9MjxdCADdENaleLB649KvOZhZmvTlMKfHeZ5MbVxchSVk22q5gNfkcC0zdK_HQLA45hz2XQ8YaeWcknPAsh_9Ij8U5iIGDC9TPI-n2Dey1BTbcs_Ghr18x194mzKUln6e8lnSyOeToFYUQNM5cbazTul7X91639gDqPDUjlOQdCd6t2W4FU5_1sgt8vvAay0bqDqHvvNsEhIGxKslsVJ_tq2U0pAPHM1kh0IFTM1oJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XrjcnfC5OU1OH3wSfsliuJfFJx2iQqBvEQGIz_seiqQks1VcGnn2jD4sVl8jZW8s48Adl75wXiWJQMC0AVs0_L_5nX9hYyaxfrxxEf5ZvonG1a2seguybVber3tl7orGNehkSMyQUPF9LSaLyZ6Qkiu9GLwYu8s7TzOMtQfbliR4Skw9zt7-knIDCEqa6ydL1qJ2wV-BF6RlbeRHWcf0dSuI1eAWJPdE3YaWpemkX5EdrjyYOPP7T7lU9MLXjRFlS7EQXrlGl36QEx8YqRZir-SY4gK-gVYUQsJnY-Kaz8QwjX2AjSNHvbSjummoGUk0mP1kXlftAG9OzSIEEmfx0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZnPJycI7L6WvA17mSeMXsmE7hmD9H4arplsEzapm0s2T6MxwZSffW2vlDZu3SuWqvrTbznE_jI4ojtA81ExCiGYVHtiJNOp9GZ0fVWxjvDx4ElFRao9gi_ro5-02eVQrW0fwrO3NBy-9hDpnLlz3lP-jcixG8dTNmhEymVF72zI9ajdaI5WjFwkMUji3GpD7Tw3mKThljx3ILVNSXNx3UwZfFv2sgJq-rWUd5c-PdtrXsTlsW3ULBqGx1uCEZLYZVxbFA3kWG63Yydlz51CSA1EOBpcV8uvVWWxOT9Nr2jc1N9QXuLrSlCv8cjUw9p-_jBDcfdqraoH-kvITG8ANQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qRuKminEsjmpQeuw6ufm6UkUpGlB3-3VgOEud8DiO8EaQ-6NiXhmScqQ97IQrzftpq5_WOxSgIdRJweWdus28fO45T_kWqVxMdv--R5z1_ebCAvtjwn0HjwRHuEUPF7BMI9Aq_QiILa9PjwP7rCKIA3-tiUmR_7uWrUX_7rGxNmvQ3r8TKbrWeViQ43C9uq2_BaZpuEVe51hSBtxHQAA88ZA93EynGLnj2jl1hX46Eb4syc-Tl3hoZT4RcDMkAmEtuKrZZSCTrYvqmHz9yXZyYpDTrkVsDSvR0KfHPs_7hKmyKpGKIJt8kz0UHeSJpN_jnlqBltq53vowNLcKU8n4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=IGNYUsVuWsWK1wspz8WSEhtCsb4rKZbcyKOSedbfaWuaKPwMjDs24ad37s9-HOQgXXKbNAwyQgAOi9zjJOhY6Wyf_L1UunPWuNWL7LExQMT1ND-R523iuSKrU0WeUWsEIQvnYDLzbo_GV4GrwBMG87pixfMiD7_BY9WDkhy_UEvs5HRYFY4rABUNlKH09o5xx3XRFcjsGEk-F62HLV8ERuXKhqJXP6ywt4DmkQBKfXZw5BLMWkG6-zj-mTXc-PESljYl9RM-YrijS2ZMwwL8108F15GYrG_br24Heo0P5YbzPbqWWn_PsHFcUmBDWtBrI2vzb3QmBatvof_6QYEnDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=IGNYUsVuWsWK1wspz8WSEhtCsb4rKZbcyKOSedbfaWuaKPwMjDs24ad37s9-HOQgXXKbNAwyQgAOi9zjJOhY6Wyf_L1UunPWuNWL7LExQMT1ND-R523iuSKrU0WeUWsEIQvnYDLzbo_GV4GrwBMG87pixfMiD7_BY9WDkhy_UEvs5HRYFY4rABUNlKH09o5xx3XRFcjsGEk-F62HLV8ERuXKhqJXP6ywt4DmkQBKfXZw5BLMWkG6-zj-mTXc-PESljYl9RM-YrijS2ZMwwL8108F15GYrG_br24Heo0P5YbzPbqWWn_PsHFcUmBDWtBrI2vzb3QmBatvof_6QYEnDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gTKTl-3kZyy8vR6bFPTnundljMD3txbVSqpvO6wFLoJDA9w50fKK6QBqPEnGkjPdDhgjkcpmn7TDBDJwG7cHzE8-bx3WL4RjlNP50lqCej33Z9CFrJYgF4-OhJBs3sGb9cb01J3EE3LhlI9Fv_nj3lF3tckX1rNiG2yqEXcDaY82fEfq-A6VHGpF7gqUDtXukxeoFH--F-WjWGI7QXHjZKteVvpasOSIhmBzCBM6W8G7kvp1GujpHnRTSTe79blAmiyOMYnBnyx-qzjit-QiDwF6K1ty_CUv9XS7ssJp8LxgkXidm3JrlBRFILQhtjMZ_DadCjKxda9l57HedEMgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dwnsesM1TRXNjX0d4JcA2o1WSuzVftvjLibyLz7EZQ3B9EBOy1rZU_oXsQPuzLU-7ZNezghbxLmuEi_UD38uUagJyYozy_rzj7tmzPvVl3dtCXHZlYhwg3XOwECJXLCEx9yXAZN4Pz1hAOn257FFnAjPS1cAEy339XZ8GlZGkzuEJX_shMbwR9wjwxFZv7To3SERoqNn8uXjMX57wpcMn8zOV7MnVKd0d_k2XAj-UN7eOKEsmUV7rAtdFbCbgSDSWRTMalMm262s4Prn42QR4yA5097YSLgOB7rxUgyrClroFiFjYLVJ6zwVDsAcdPNw81KgxwNe68n0lz6wMs1xcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZdwfPpYrNzye0RWK9tfBhL5CY2Qz5zqmN86IKPTD4g4_K6UGo4pgkFeX1uk19vKOBHrdamzOREXHno0OOvgMk_5njclC-mUFAjlAorMo_uReY-kY4tMSOrCRdcp-cPiXbwg9BOeO52OrRJ1TtfgmCvvGGP10Wv_Ou5qGTPleM42qwgRyel-6wAPdc152rgGJ_ZrrfTak8M68s_OdyyiatXVz8eBGgTICxJ2qoJmpagXzbnunVndnF4MdWx-9Q3vx1JE16qL7r-8salqidEgrpwdlpDfP5BFebqQ6m1EObbdmMGusl3BRueIzcrWc9hih6zDVqkCqxAWI8iu5yjuNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C-oxQATdxVXuD7jl-UHL6NoLuEtD2KNRG2QKz-YvH6zR0Kujjv280uhGe-H4vys7JqkRusiOBPPwmN0VpAlbKbMyMZobnPe_kq3sk3jeZ4ywCHr7akFTG36h93sz2EtywEqLQdlt5qFGM0otVgJYQve_6v4dKn9Mri10_Yf2a9UT3rGBtgxcPF3Utr9GGAhg6K0vp2g-fDudy_5GR8REIwdm0Jpotx3MHVE8yCDybsC0DR8RkQbAbdfudRWCagQb1XzrZ2l-7ftkyJeyNozjn5MMj5GR8T7jBFL7cttPflzsJl2_ibhZwwtRSBFD1NaUZJigeASSRvW0FrzGBhKVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aQ3FBpu_DyY-94BMbyjSXB31Vd4--FSW6aoa5OhjTUFr7XMz_l6V31kMD5WQ5njnvkQM4Ccod4yB7M7XLJglMMFxtag53Jypgc3ZBejOc_uBsqz2OCd_qNmNnJwOCLlhSp9c7mCYvtyp39UQbHSIgb6rF2VzpIXEcUyYEHC4frulixJ6V9KkjtHLWrT17pqeu21QitLEUeE2KlJA7AMJLPSMUMOE45NTUpI9OFPiC5P04_loT_ybH8HyeHpZPhHrB-qtk5eure0Pj_GHjCwVp_N_VpFy-Aic6lc_Q-cOHbLa_UY13n5QT-4s9rePXVoifi5ZqArkvP21IBy571oyuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rHNWmJjUxIVFX-Uhrg7fyDzRgthIUS-_r4Ao4GTV7jceWFd8EwPRgVstqf99pdKNJiLCewVsQMRHgAHCIq87G3qZ6hefMoGW2ScBdSuhWmj3i8qn600xx3Qm8Aq93KKGvh0PjOI6dn9m6i2w-BNEUpgoEcYbrxS5KkWK6rlCRFcab5uPYorrmlwbNrK0ii8MJDt8qOeXwFUlFHDMh7fKE5Ign4UXhK5Hxi_PPszJFbOpYKZLVN8-hl4fLVQ4U-yehmQuOt9QKGjkp_yhg_cS9CQyeYc5oThqwL4--YeVjui3DYaBVQNoAEOH1gLrUw2XnzXf97EdrAIs_pp_fmPMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DYnfFB72Kf-5VEaTsiylAvO_9IXUKTtQPNkjhy1yar9a-vCahkVjt1SQQ7--dBPWKPCC8OEI_nuv4T60xUxN5IGiL4-BOiQp0gqfIV3aY3hkyTt3UEC4_C7bxOXyVgWRXduVA50rp2jLac3Ai1MHQyg5_zzeeBGPiSWEweBmkfeTNki5EBz2B3Cy3RveFb4KCCNusga_TnZFrCcBRgaVsfRwmTWN2kAk1NI5SDTzd1h-T81knDukDVx4IniSdYgB2UA7FdZbrTgqaqQ60n6ACsrJ9t2NE6qu2w-OCt8XayWeviFV8rS8kq5cx5NBKUmj1gNBXnFyDc3e92Rpu9njuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FzC2NUKnmAR8GPlqWF6sQaBmvzsrVpwemX2XfdCn-EebDwnmbCI4FkedxHcY-QTgaWnhGOwD0kijouJqFjnsyt7hSzXdiZazj-N7fdGCPpnIoloc7Y_lQeKCBr0GPDWDgBOZvc1vXFRGjTl34ykXWcsASUSPoI7teMn8-oXNkQjhbuldM2hWDzrilpMjhALE1c0jrTQOAACGEvj2UR2tAc25nKP0UE4peSkAhrXut4GgJiM3dGlqOaj7IhG9KzQ6Uv0JixJi9ZJViBDN651GvoOHGckgmuRKxFNXQK5bk3nili02OuCbMimR2RJj_7cbXMwHDWg5cl_4dr-EIJd_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BTE4d7a1N4_piFv1QqoLXD9VBcHbEpxbyMKXLDMjiB0zkAHAR06CIGMC-9ZE_X_juEMgViIN7aSKYFjMRQQZWZRCipP4gm0LC-fN6h0VVMquPnIddfhGRcAtLPplU3PXaW16A-ec7zYibqg8JiRMfLvV5YwLPSb0bIe93sZ0pm4ZdnKx425o7bcwR9IWNM4dNghCNlGMVE58mjws4Yu5xvkybGKKMbYoglC2fOTc5I9IeavwoL4msKYqlbr8zRYV-CEvEmOAfsNU-Fu_25Y8A4tGVXh8bQ3vxn-ztvpqt6spmcBIwUXz4H8eo2YkT-roiAtmxs4I69c5eVNLyaXyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/trsau5JP89vWk8X1_0qHgHpwoulbgEi5-mMkgwAFnIdrqrP9QOj7HeQU6QgzAkzyoafZpSf7-n5EOx3iRZDmbF50WBwJ8_qcHsyvMebW6bqI84jsjZzybYVR_9QTwFVQRinARz3Shbst6vcjFHKTSx03EEhSr7ZwqtEe_irD5zAdpcliDvCMltZAHiJy3JiUACsgt-ro6qlV1chASvfn7NjJL2jMoqgx7A_LpQhxKjFsaqXoQUz4bCbNYymge23kARNghRfp8WtfHD61ZnmUm05-Q1evvwYGjMZLrL7l1DHkS_xjjwwr18uqeMQGPkIKbRe6yB5hUMaDP2nafYbVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nk8y_0nJDXLelTjX4VIDT3Xp6wviJMNtK9fqP8Jos3sYWIKPt5rRAlyjnL0NJ7JUbRfRNm_zg2XI1ZxV88KygWA_3CXqdIj99jvlmMcMgVt-Qr6vgBWZ__jXrPpRG8VfkR3X963fv8gAjrp8g5Tv2hX7zUJBEAEzvT951xkhKT6loOkoiP9OPwqwpDLb9wzJVb4Yqd2Q3hr--VWXmhBs0QJK-tnWCcI9Y6t163v027AmWMpSTcVlxaQ8tne5tvvgJb6EAO_tqmWDGmCkEOBiYAe_me610Y5VwKcYAX4Dvo0d8eR1rocbglsWtonWwTdzHqPOWs6cNLfGhr73iu7tXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=dx1LTGETKPVRMinbdNbTM07MOM3gYgKoXsAdrdHo1zzkp7Wi3VFNo_-cGBj2KbosdlUFtXvMlqCcw10gm5NH2AkUxVwUM0wpOL7I97KIBteOvrPycW8NZ9gp8fRObTliN6DKa3OyBxckK-mdkbA7a1wCE_yFLKsxL1-ca9rk1DXjGeLu9hGHUvI8DIKcxw3DBI87BeH-Mlt5vMP7Ekym7oevymNwkHNzZUcOtRmOtlo1V7WZ2phCHn_TSFYNNOedtxiJ6kBHQESmvFZY19PNVU_V5MOsoE69ZQJuqBd1gJfP808qJ3MFzEz_lTY2PT053gJWw2sch_1zyl88GDq4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=dx1LTGETKPVRMinbdNbTM07MOM3gYgKoXsAdrdHo1zzkp7Wi3VFNo_-cGBj2KbosdlUFtXvMlqCcw10gm5NH2AkUxVwUM0wpOL7I97KIBteOvrPycW8NZ9gp8fRObTliN6DKa3OyBxckK-mdkbA7a1wCE_yFLKsxL1-ca9rk1DXjGeLu9hGHUvI8DIKcxw3DBI87BeH-Mlt5vMP7Ekym7oevymNwkHNzZUcOtRmOtlo1V7WZ2phCHn_TSFYNNOedtxiJ6kBHQESmvFZY19PNVU_V5MOsoE69ZQJuqBd1gJfP808qJ3MFzEz_lTY2PT053gJWw2sch_1zyl88GDq4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTjEMpsvG5T0R9KTBIU9H_jl53xUePwI_K_kyAayzgbnm79ulS_pv-C56vUAJ4vXPtYTZEkxCSGiNxI0ZPQG7z1ARULkQLVyJQ-oE_2_u7_Hv_gN1Jg7aFrckdytYyd4k4pTiS4ax1eDFxXrl-0zl8Ggx6iTYzIVY_JXcoeSQJNdwz87dhY0i588R_6htJJ9edEqBludjey6cUOLjFGwtO76JXan-XZetgMmwO9swLH6E0lEhxzYmYsE_BBznvMFG5e6hqE1EIQEq_dq-Y0xdN-DGiPeIl43UVj3gF1UEthO2jibGsEBCewxj_lFaCluSmtcAXRJ0H66vL6n89ZzmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Av-0PcXKcS3dUFvoVIVsBXnxIRghXzMq8ddbvfAOap8YYfD2QC8v1jrT0rY4vPZhzY6a5Mmtu180ZI4XpfUtxU2VwZkdmHPVNlw1RaNiTSnbE6KyIWnjyZuMxdk-G5Lv_e5GHv8wOfHBzNoUUAI92MnNrO9m-dXsVIrzO_MbDJ1miL_TfQijdtmQpbkCuo0Hy_9xaPR7T_AealL6Kw2aAJY1P_ryKsJI2llQWzZYTesZ6cqu2TSMqiSSirIMg3OFg-0HIw9XTGP-XOrg8pIOFW4bIzSxApnfXh3sbKZ7LmZXqz_zDHuMYrlOupiq3R-IJ4JU0Q5b4ZGuplKR_avG9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G3P0Bl2JWlEa4Y0fxu7VQWYtLY03lDsM57q69sZQNK4VTLPtTQR4thOV8XCRybWhOZXaDxYc0pM2Vx9-FyP6GfhHo4adY-uytzzhO_3a9fl_lx_7nv7DSvQg_7_6LcpNjppeTZSk5sXwt2SOazOQnX8sbI_0b69VF1O_Z7zTXugvHIuSrqlEo8QVyKb5m_VKjojY7XQ3Ic1RTXuN0iLkUoPJ7vhtfvzcmCqLph4Kxo8wASodk0xGxhfA8CHJmcgPHdoLXKdQqdYvXgbsvgUdvj3t7s8-cmwlpeVd5mQpUf8yA4SHKbPVwE94klronbKxXZxOFzjW4Vw7rkfLhHLWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=ekR2U38obKyo9ZRD1JJTabkHe1gB0Jt6u_mHlM0AN6MSXRmJAaL_aCJZi-vVgjXjNRBBkaH8-uyYL9nC1LSW7YwKjMH7itTe-NjKGm_WQNtzTUvd0T8WmVfq9tA9m2O_SA_mnmZmqqcGPgKN06kgsGgzr0LhNW4nJMl6mm3gFWD1hDFyMDZlRtQxubyQeEx33n2XpRDs7VjG6tWF_dygUqYtKC2UNE3JW_cBsep53BQirs3lBE1YUCVpdKWQoyfFpfPzhPHbI7nTZbxG1cpEntW0kXfwA7QZD7leg_BClPEOY14Z0Xq7l9UnISXeBPbrBzio2K7wfo4zHjPJeruXvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=ekR2U38obKyo9ZRD1JJTabkHe1gB0Jt6u_mHlM0AN6MSXRmJAaL_aCJZi-vVgjXjNRBBkaH8-uyYL9nC1LSW7YwKjMH7itTe-NjKGm_WQNtzTUvd0T8WmVfq9tA9m2O_SA_mnmZmqqcGPgKN06kgsGgzr0LhNW4nJMl6mm3gFWD1hDFyMDZlRtQxubyQeEx33n2XpRDs7VjG6tWF_dygUqYtKC2UNE3JW_cBsep53BQirs3lBE1YUCVpdKWQoyfFpfPzhPHbI7nTZbxG1cpEntW0kXfwA7QZD7leg_BClPEOY14Z0Xq7l9UnISXeBPbrBzio2K7wfo4zHjPJeruXvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=WSD9ECpQmENyCTWRW568-uM0amnCbJEOfUtXwWpcJAMcEvc3gtWQSpcH5gRD3wPFsUq22L1dSoElfn0vg6j8ux4jLOztPb9AjNL9Clz8lCdYqX5Vxjn4Z18ty8bkBdXzRWciRG1T_VLfcL8Nu0obDDp-YsxHxMn4I6gIucn0eskINPllWr7AZslD1VZpVjdCLihpPtVDvNaSYdCxHKyDEOT449q0i10xmBg4mDdiSDbLaF79PyYctoGl30WiuBb5qdDxUHpyaf-B9xIC-xm8swQQ47DIhAVvpswcrcJOC6BEO0rrSJt8Jwny5bCNPRXMs3Of2_h6LpMuDYyzm5yweA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=WSD9ECpQmENyCTWRW568-uM0amnCbJEOfUtXwWpcJAMcEvc3gtWQSpcH5gRD3wPFsUq22L1dSoElfn0vg6j8ux4jLOztPb9AjNL9Clz8lCdYqX5Vxjn4Z18ty8bkBdXzRWciRG1T_VLfcL8Nu0obDDp-YsxHxMn4I6gIucn0eskINPllWr7AZslD1VZpVjdCLihpPtVDvNaSYdCxHKyDEOT449q0i10xmBg4mDdiSDbLaF79PyYctoGl30WiuBb5qdDxUHpyaf-B9xIC-xm8swQQ47DIhAVvpswcrcJOC6BEO0rrSJt8Jwny5bCNPRXMs3Of2_h6LpMuDYyzm5yweA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG--KV4Zk_-ruQh4vgZ5hS83gTAzB8yx9lBmnagiMvrJlaCLlybETDB3xlwUW52riDeLWLzDmSYWGqPg4OeuT6KaZKAJvPrziEjauSdF95ZLo6xi-uD7zqgR2trHFiiYgDnKKBUIVKkNQiv5DSP8J5o9LPdkMntk8y5zes6vsQzjGp3VnbaW1jj8CWWY2o7-De5WXhNI8ciJvCEnVGMYWLFmEE1WsOmWqZVkI8ngHQWpd1wrVQbk8HiHsic7EENiW7Jei6atp33w-o_6rQd8mFGfpFV_Ybp3Qpm9F9WRTDbk7xB5R7S69WmkYmBphz8JTRyeqX82NPsp3VsgMHO7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLvsMnqSI_3FuoN7Muyl8gHklh2cml7bg2HeySoIEdS7D1uHuSsxTzrp52N774VaN9N-8-Zc35timqH1pazm9UjDAQcS3g3-3O0hFRnH-25dvaSfqZ550f67X_V7TfUfXIln-7A6qdoz7f3P11eh1qDkwEvf9jxZMX68iChTx088rxp-QtlEcTIrfV2ZrYdXN0DK4FkECfWOB6t-DdILMuQxKllhhEsM7JO89G5cAaTiPHzheLIqXPCTSBoDYXeJreiPitlJjZhsH7K_Yw4biCjipobP2JCSFgaDqh3wQ7aS50h3npzeCz9wDENMNIatk9Zakt3VZp-iapxHuelXag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=dNjM9ECeUj8vy1sGK3sYF_XFKrDkgWH-wSc1R3uoBuBBlkGT_7YvAhOF8z0EUjSvd5jBXUWGOjHKBGT7rL8r7WnKjvjrKI4HTUqzLDAhHO-2IQgUOLNURN8mOkxvU-5CGjd3JyNgODlbG5839rEg1AV61QzqEt8dgQakCtHK83OvljmCMYCN0DQ7J7p9v_vWqBKzudBMNORmkFxQ1LQXSnbsytpA7TI0VdyZMmgZp-ThzbFptpF1uliR_Az-JzzTuYk5vIXcFuHACa_q9vQR9LjDH4AZ3v7WTssnfhEVQOShYcOgGI4iepCkntJ_JdPKjmQ8aCNOkI4qHGldT-FyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=dNjM9ECeUj8vy1sGK3sYF_XFKrDkgWH-wSc1R3uoBuBBlkGT_7YvAhOF8z0EUjSvd5jBXUWGOjHKBGT7rL8r7WnKjvjrKI4HTUqzLDAhHO-2IQgUOLNURN8mOkxvU-5CGjd3JyNgODlbG5839rEg1AV61QzqEt8dgQakCtHK83OvljmCMYCN0DQ7J7p9v_vWqBKzudBMNORmkFxQ1LQXSnbsytpA7TI0VdyZMmgZp-ThzbFptpF1uliR_Az-JzzTuYk5vIXcFuHACa_q9vQR9LjDH4AZ3v7WTssnfhEVQOShYcOgGI4iepCkntJ_JdPKjmQ8aCNOkI4qHGldT-FyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=nRr5XbIOa_ozXXRy3bH3dLY_a4ljZI7q6AIqjlK2GyCI4gn4nlLnrowdBDgRMmN32prouVs9W56xTZJbBWWDm8_Hm3GHWb_-8otzQsVS4IfuXT8w7_2Rdi1MbkDFU6zxAq8gmFtYyWKY2LN-Vw4VpRnQxZiItP4-NGB1rV4Qil3WA-FO3GgL0Hh0hVRszTatpSewYxbGjeKY9Fs-XakuBeEd_z29qzGBCj92P0g9N9QUR8MbORCVxkyqzakUBUYGjWmGtudy32ynr3XOoq_xinleZhFI8PgQ6iyLN9g3UhgRBlXwZ0BvwPz2GFYZEaZODq2-vPZgZxzPmripmMJdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=nRr5XbIOa_ozXXRy3bH3dLY_a4ljZI7q6AIqjlK2GyCI4gn4nlLnrowdBDgRMmN32prouVs9W56xTZJbBWWDm8_Hm3GHWb_-8otzQsVS4IfuXT8w7_2Rdi1MbkDFU6zxAq8gmFtYyWKY2LN-Vw4VpRnQxZiItP4-NGB1rV4Qil3WA-FO3GgL0Hh0hVRszTatpSewYxbGjeKY9Fs-XakuBeEd_z29qzGBCj92P0g9N9QUR8MbORCVxkyqzakUBUYGjWmGtudy32ynr3XOoq_xinleZhFI8PgQ6iyLN9g3UhgRBlXwZ0BvwPz2GFYZEaZODq2-vPZgZxzPmripmMJdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=RjZiP2x9cq-ppjj3ysyx6tZX804n1OlFVsz7c66usWId1pCLyjVCWXrnEinLLVqOAs4HmvRkETDImeId4SXWvtrLn3XZSWOC5MA9XZExZhbIdru_FOfkWmOnxYER4XIUmGoYzQdSXRWVquawbH_ZnJvh3HnXLK7DQ7W09D0iINkfd0y4zuyUDcKnM1D6x9ktbZ-QbdkB9xaSobjf8lKPqMmpWlqO3IU-8hHBnpam_wl3rUqlNkrwBQAJ-P5-jpOYB4vBBOIEkqn64Ma7vKi2dKyWpoCcJeXK7AW-ZpgCixkGOdDjGmqxf4tsoVakODKPaj8xXpWkaMZPmTL07tKyYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=RjZiP2x9cq-ppjj3ysyx6tZX804n1OlFVsz7c66usWId1pCLyjVCWXrnEinLLVqOAs4HmvRkETDImeId4SXWvtrLn3XZSWOC5MA9XZExZhbIdru_FOfkWmOnxYER4XIUmGoYzQdSXRWVquawbH_ZnJvh3HnXLK7DQ7W09D0iINkfd0y4zuyUDcKnM1D6x9ktbZ-QbdkB9xaSobjf8lKPqMmpWlqO3IU-8hHBnpam_wl3rUqlNkrwBQAJ-P5-jpOYB4vBBOIEkqn64Ma7vKi2dKyWpoCcJeXK7AW-ZpgCixkGOdDjGmqxf4tsoVakODKPaj8xXpWkaMZPmTL07tKyYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmMjighdfZF_ynqZcSxckblmzPpWuZW7M6vvXfMEt6EEP6C_2a6lZ6x5GS3oJtpnk3dk4nt3p-YQxYyzS7Eo5ztTUh3kuy082rNv8RzTboYo51Wk_Z1VeQRsYgKhyfCNzLtrAcmPbSvEGrx_wBav44xZWsPeC73XOzdWex7PG9tLx9bOXbdsL0Xljx3RSiih6hfKpHfajNRp4romHzob1begeylR0tJeUCvD42yAUZWwdYAnjBaBLcAwdB7ZN5PIMBguC6tR43KWHuPGaXR1YbFfxl8fsfwj0wxkkctehN1oon4HzvqcdtxUCjSRFLFFaMSLZqTc6ZyzCSGuuwSmTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpJ6dC415p79elUlYOdEP49olJUTIGqdQdXtDfIyf7r4xBte-IAoWv87QMEaZZfJgT98Mb71nv_eYKmruWEXAi7lStpRz3roWIACkW4X2yhqUP2HS8ApBGVsEAGlxJ0XuywYtpIkh9gfc2y2VFlapMElFWqOwErsMdFFjdhDSoENyDM8ctSNozzlPTFCtEU0ghVqbPLzeGEaPWnZDVnfUwzOWr_0rn3K3z5gtPMF7QCUahz97KONFcyPciP4O2eHeKxYWDPbHJum68P7nLe7f9EbBrmdhcd5k8LmA5YR6wzP7jIru5wlaIv5p2p_KM3_7wYqKJrAhb882jy9AIOfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=IwFdOGqTgc3Mj_w-c5NPUeMPsllquOIp-g7q5YvFBBnqBtne9Qf-tiHmuyLGraTah0f-QCW4MIUteWAr1bhCwQoRDHlhRAURemoP_U59ODXtGFR0TUmCLCfnuAkp19_LTApT6qXZI6YgAfk5I-Uk7OzRiLZA9zxGufxfsgSbdMocFxP2jZPZOcPPNlaQNxNFrEC686TLnMlZsRbVB1unY46b0cnVNkdee3GLwPOrLswrv_By0WSfGF1gQIJhgRzB6ndkpmb_h2H0Jm7cufCASfSsFqqRhGqIDFJVaDUEl4wVpVHno8tXd250nKWIqS0tOT-Dk3aiXyrB9ahNutmWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=IwFdOGqTgc3Mj_w-c5NPUeMPsllquOIp-g7q5YvFBBnqBtne9Qf-tiHmuyLGraTah0f-QCW4MIUteWAr1bhCwQoRDHlhRAURemoP_U59ODXtGFR0TUmCLCfnuAkp19_LTApT6qXZI6YgAfk5I-Uk7OzRiLZA9zxGufxfsgSbdMocFxP2jZPZOcPPNlaQNxNFrEC686TLnMlZsRbVB1unY46b0cnVNkdee3GLwPOrLswrv_By0WSfGF1gQIJhgRzB6ndkpmb_h2H0Jm7cufCASfSsFqqRhGqIDFJVaDUEl4wVpVHno8tXd250nKWIqS0tOT-Dk3aiXyrB9ahNutmWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MPjTQ4dct-8rVfm1VhKEQBtz79A1ZD-C2iiOv90ywELmVhnmEXbRI0ruw6zcUFSwia1S-OKRQcnpfwRdp1iuqEYugU1JV64Kxr8XdDIBe1b12adKu7hRxmTUg3Oi8YoUuIa9xhminJtuR67cFkQUiQx50jp9-Y25DBjF1tJLgUei_hs_OQlAtv9QNQncJhWYMdwJ2xEvZ2g3SVyPyNKFtBlWqyQcDuQ2Bv1-xTgnE5MBkXS38xpoCXWNJ-2Zdot3yyCjQ0ojkCeyVyYQ6QE6c4qT0wT0b-X5JX3HnF5eYKDl8k7dMDtEkN2_LrUXeVbL8EGjjRo3nh29USevcNqqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HtoqOZVJ84GSY08uyy4n1rcHZzLGOs7k2ZIn7MFBoXaCirn0465FILRdLxgo0g3PVLy4BLXZyDybdj4PMeaqGz5VSTSHZSBJeZt9hrdxuXty0N7DLZ6jeZiu9oXEbJnrif3oHHiquHG2MKcLEwIW2-LLJ68O9XMak3C44WblyGdyazM4jUSPHsxTZeNfD07-2Pxn3pIBnVcv3rnfOBP6djMHmFDZj9HT0kSFaSagMd_5WdRzmOpM7WlIQCLCuft4UzMtDmuEtLLUMsiM0D7-JAvA1oKgBmmWwgNWDFMa6QckkQ3jLaMupqIz5s9UfaASFjFaI5Xie80584I7L3Hf_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3NoncnqVXIY1XQcJlATfF4MyTOGABO6HXhjyO8MAuFWDQowrIOr5FvL4pLirnpau5gHABk-WUBBMkjGIP3EP1BD2qRRC2rO0UX9_7Bqh99o9chwzj6Cx5jW35GCHSRpCHEmGRgZ1MOjgCr9TNOWlqARfbK60FqwvLVSkmkL9Ufux3e7qhuGQy3tZlj6wxguXmj3h2xJ60Ty7mFoWRGafPQDmHQxltNIoL8ILhWPhDJQWslvtKyuYhAW42u8q53loIIjppvMgIoEFILVeVxjYJdBSVPU6UmiN4mBld0Ya2HW3umCcuWXqOw9od1UM9rcx9M011oxFy5kHCoJmnCCJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AY3jEFZ0F3eIiMIERh5VA2SXaql279So2xGfhjUAXuaL99X1n7ZU7wGb_HEYT1Is43dPvLWYkICMfqUz4dvpmagcX5VzuWqsenBR67Nnqpc6RuP_gdfnFEKpY51ieS_bCnCcEKIZTpJV5pNGLqKwKzAPB8KaPUG8iG9TKJ36rX7w_XU26y_90Wo9L49GJLAnfstky2PDwjkBP98GwX5KW36z04S6j9qW9SeCWAnxpwvU-DamSxAAnphBa0j6C3uIPr0cJEyKIXoopFlIWNp49nqNuIOrNSlyBh0XO712hMPdDLA91Am-4jqTUoXPRGdspCkDgurGBiUUcAswcblllA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WE5AbwWnP0DziK-k-KI2qcc8mP2EsZOmvNwimHCfKvkpx1s1Jj1TU_vVfjVmNMWG6dB_gwsE4vygtJkOz_JLaz3X_cq7d7slOfYAkhbizYx9MQiBbFBXwaoNQiiGXi_tq3vnoFi4d4Vi0SI3EP8_FwqD379mQYbh8crzp4h22BMSce7Ga8NnpyGAT_6y02mNoQ4fmKH7GEUOgDzUDm0l7EbuhFw1rxF5NK3PuH3y493r3fOydCOhkarZLRaywD_yd--CVSAgGyq9futaL_XOpoOGKsA2rwE5eF0ItuWg4hb9XfTLAa2UFOmNK924z1Uik3PtiDdLzM6xuU_ZcVQNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uoXr87YK26B6MvSKiFmgYG5Et3uvo5K9ovBU2U_k01h9Nw5-wWRJb77_ScfjRgKmapmRucB68lX78qty58oNEylTmWxPuMnUbCKIL1x7XgRc-1wbja22k8TaPSUv66Pu0KWevGbtCjT8b34rRrWoWbeD4UEhGxXU6KmQUXk68g19ckKJd8UE9nhGW9zV3JI_bbN9ASC29oSD7JFIQL2RbFdVaQaDhh57Jyyg2wUt4bPau4gdmHIhEOjSTSNNgTghHF_LSVEEGepmiDjxw9E2l108UwGOATg4j0VMMLH0wcwbFidLdQngLX5turxfDSf9AymzRtWlH6I5ZEH5gzpzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGqMKr3jiKoeYZ8IsGLHoeeh8d9wujIBbt1EldiC3pqS2CQDFJTSqR72XQBwwq1CCFeda6SXpeWEa4rW58KTgO2JEq0qsWOU993DLiPugO-z_vNKr3LK8Krchsxex46GgMgFxUTfLMDBKLf-OWKW3-A-CgXqr2r7fUtfWvIJCCRC1eRs0VMaA66RmbU3jiRRat9ea8ub5Uib3qzL-QGqXYq-mDnu-9yBJw3ZnMGJQBo2PnOr_GPpBD_QqvLefph4KCupqXD8TtVQRM-y9GtakfA4VI1Ow8MoMCONO2Clqm2D_pMbaE6Il2R9efzq9HI06xVXQUs9nL4bZMi7hgWOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tDR1UXhwBlIrPUJbBnig-qap-SvMuctQZkvHUTUw4CT5ymZcum9pF02BYFYRYr2uyeupmE4ZJ-crDAI8NL_FjVCz_2vvMoB-Sze98p4zLJnno0zSlp-gw-oCBEdHrT8ziRYcu9Bskw7P9Xa-TjBC6Sg0ICG7ebHCrLJhNMRCRnmuQP31OnOHaTEakTUk6RQnYxwnNqWzcKxwvTEflamx0eq8dDdlD0Ecpg37Lh9QrPyzDVyr4745TZIsJuh8DxJGQ1sDE3mqs83HENTxiL-_363iRD53d65ZQ6HNtSygPpAtcCTi2zVJyuvgpY2x1RNnEKWuD4rPvQ7GSOPu-5ns1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gfUCy0-tH2EbwP2fQ2DZpTCkf6p9dDiYEprtyYbGEslxlnLv4Bil-Om8Q5zraU2mncsgX2ReNLCwfZ8oGMlbLEzpy0whtk2Pj5yx0NJheZtLl_j60aAPE1dYgOT9n-OhSwwbSgHX31MO4_hPDogVRdsoWpHY11j-31kuOWqrLsenffsixQY2Gir43FHdrDJHbpE3UzqTQIio2P4bvj15-k4e0WstrC5NY5UZhrlGN7K-iTSiXHXtLabL_xc2SL8ul8U3aYuCwHGZhwJHzso0kXEQCV6-rg0rKJaRAnavGIQE55ZN0NnOQFlayOPRxf7qenHFCsGJTF2wojlkykGFJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYO8gkLVJ_jv7tPcUiRRGTCeRHjVOd8YISFarVpugpD-lFbKdHGBS5jMh0JYJoUN_Ch3iqXJonuIvrhc2fOJsn498B-tcZYMlyKBOaoACQHUmrV9CyHRvRXTSTL7Ds_IlwnOeWsNGUzI3iysCu5Fl2j0YpGawRzqDb62vxc2G1d-4HIaF8j9DNsOI6wdiTcvQPfh6I73KFgMKwGHjvFdD-npA8s0dR2nlXDROpZjajW0jljsGjASA5l2GZtRCMrQ_nHUIAVFs-KZ8PccrC2DZETQK3xH2Bhfux5BzJYklncezIxz47HYzS0Ayp_3W-Z9ViWaiA1zaP5hA_4q-MHfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=DlZtOaTq6Aa_xWNJLMKFNAHsEfABzUZXVjbhudHuzGaAaw1itvulGi_lPTwXbbM92G9VSHnXSRpGZaaj6SzArvprEZzrBPM_cRPHC5F2ozvJu2n8RGWKatEJoO80iMxgKH7HILb6B2Q1hYyJc7V13xzVXGJRzUwadYIxjiuxLLw37jjOQDOtxx0otS2yMuPXbS5CbgT_1CFX8OvN_LTMeVoFpwhnSPBWhOCi8-ElogylelSTOYCrz4LjreT8DZ8Vb6urZnfowPBWIn_bR6v8Gj9A19j1_nOBGQQHIxd1DWwAc6NDDTYvU-OVvyiWD_kPu_DVhUC9MVwM-1EqfS_SAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=DlZtOaTq6Aa_xWNJLMKFNAHsEfABzUZXVjbhudHuzGaAaw1itvulGi_lPTwXbbM92G9VSHnXSRpGZaaj6SzArvprEZzrBPM_cRPHC5F2ozvJu2n8RGWKatEJoO80iMxgKH7HILb6B2Q1hYyJc7V13xzVXGJRzUwadYIxjiuxLLw37jjOQDOtxx0otS2yMuPXbS5CbgT_1CFX8OvN_LTMeVoFpwhnSPBWhOCi8-ElogylelSTOYCrz4LjreT8DZ8Vb6urZnfowPBWIn_bR6v8Gj9A19j1_nOBGQQHIxd1DWwAc6NDDTYvU-OVvyiWD_kPu_DVhUC9MVwM-1EqfS_SAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qv5SjGKHcLk8GutXwzJNpiY30-H0W5fMuUo5Yyg-CkkreBLs4-tOgIwE1ZlvevDeRZyoiPwO7DUydLbQB27Sv8CnNQvGV6ncBPbXMI-7VjPVRb-6cXyCr477vKX3yQnICtzOcyKGNOBqBPnDw_fjAH8MFzV_SHZMWYZx2Cd4uUP960k8eZztle0MhYjhmjbKRfzjZy4nneoIlf7EjEIZl-U_Uuzs4JIDcH8E3todsmB60bjXoiFSvOcavz1EAfCSlqwU8xLVtPTxB3g3vBqIagXuDvGXSYjaPEyhFlRYLBiChxsUddT6ZPrn82sH6NcnoQOlfxYpwM9LW8tGxtD6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vvJm4RbYyqM4G8PokyJBls6PoEsv3IWATkmaeEa7C7-u93gr5MAAAGo2-zTffeGFLflb4lMVTuYZFXTUCCfJMq-3O5AR9ueVmU2rDnp7TrKiuq0v5X7xgdapOQ5qViz1MvUuTtofyyj7XTCtv7oRMMvxgevZkUcOXyxMTFqyAy6lXBvHPPdy-oNJrrxgdRMBeEiJpFDtwJo6TJgR4EGJTi38MnRxPF7if-nExrSAEPpcQeXivZDW_GdbTgkgljznnk3JAMJR-XcYDApxhFuwd6ZdwmmnMSiZznLCBn5bGPBAfEbe7iOvTr7rVXb9fHWCF3uZggxaFM9WGEHuTwz9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVapWgFpQn36dX7yDTmuFJWIGRQ9zmAT5MGem0IpmCjq8uNP63vdMgM6AWUolDqJu76JAJ6nV2es3n2Quw7GnvL5m6Ykb2NXrDtLTw6LZ48L2z9RqYtPXYRwAgyVnoYM9MQtLhI9PteNJGFyBMdWWmjowe3YmsxdftSPbwhfE8v00WpBg0WaXngI_5Uda44iJLyjEIHh4WO6GMOM0_3aIC5sS8NmgRMK1V_DeSxhzJjj33c1kRWOTpFBcAJRwhNSOIvls5rMcvJ6ZKUCjewXT9vwXiv2XZTY8L0CmhBuq-8MWxb_iujahdWmbuE1J2J0AxmblaPhG-qemVg7Sx3wKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QmAW63i2qC_j_VJDjdjoRkXpux52DxAgpNwMQirJb0JYCUNBwXfNCZ6hbtJrMIn1qqLgqzsci2VfGJfA7wx_-1GZdAzDC-qXtsAcUxt4pmknBTaCb255pMvO8fFOK-9vPK-M1T6DDosjsIKepWYR9gsb1BXIGDV-5vx8VESP3y4xAKicWqtPqo1YVCigXkeQuSjN6i_txhxt1vdNr4lzUVIIim-HpS2fzSH6r2komaYQP6d5WyogT4ztQURQ1raPGrecCpWOA86sLYBl1f1x9ulgLAxXKkmpvxntjtNwRYeuvLGk1veyy-HObi-E3LZG_5VKZWtIofU29tWL7WKDnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AljVHm-50JHUtCYYi2ghnfdrRIjw8Sj1hzXbLU1FYg4xBX8_yAtfu1Kv0gxqIohjkc4opp8IeUY7jXU-_ABexu-ATr-mjtr7x64w-NU5W5w4hvCLYgPVmUyX6-kdyNBqEH0UGgTLoIEiBz4AKVUsR3zqWjHblxH85c36W1ovxwQFYxgf_qw89Eq-w5Ja3WSsF0KZQEDbyUnFNxX3mDfbbexACYNdJ7N0GEckYGeNYE5mtTofoG9KQCm374oUwsQymnFaAgjAZ6O2zS1tTQt0P9XYkD2tiin6SOiw-C08H5tgSN8wSi4LlCuoZtKCjwSkHAFelW03ytUZt6AOoxAI9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ir-7AzB8FKUvl_MOWyFdtztzvN5zDDS6ijiK3ne6HykBcWJy_CBb0f-WxiTZm8OiSOZq0XZx0aEHJlT5pMs2yGrjXyY9gUG3muLKWMXJrDsffw0l_GBzswv3GEocycq7WsLOyImNSp3Awxx7oxiEYDMC2xHnRwGGK3Y-djU7J-F_2v4QnJcIZCZoQeKGBRXF8ZdDJzN_KQKjMQYXLyocY5TYBalm0kk-ivL7nBuwWt0pNcv8WZ5F3Djwp5reIigL17-DT4HW0gWhZyF8bJCVS-vh8BWc4q-L_CM-d6eB7523RX2yiHyqBDPyIcDO0ZRAOwej2yro62gJsYIttLt97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9SxWUJrFcetrY-SUOrnVqpli4u__sMLRfQHgytXCs6GzklBJh6FdAfvN-gd2HmSL12Dyubyh4OWT9fQywRPFkC7eOQsrWfY_lao6zGEn9UR5TeG7Pr5bUxtXCWx8LOTnMPO6EqTMn9--VMZb1_QhQKg9RFTo8G7rF4MxstqK_nXxBQO-rYam74RJZYAZQ6tIxXS-scqgZ5vvgjUcZXRmHN6JxeQkOmsdLyp5j42eoaG3_Kz2IMuG_8WxvS3Bn36QV7ztBBUDWaB9PkTuubFyOtf27wbA7P3-S8zGQ1U3RoUsjVF2w9U7sX0GSuOKmHrfkNe0gkhpBs90Kwk0cFahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1z3ZvwySnr1oVzX-KDl3aEK-p_IsBrNmvP2Zd6v1hXBoz_oVJkhkRxLAG80AzTl3nhhL4b3K9W490rcajWeRrmcWOCo5z4kCpGmr2E_by6dmJha6fo1PoNNV6kYxVKQ2N7HjBMJwAkU3vsKbDss6ZJ0Ed-5vg3H_ndZJcRlWCXJmXhhQ9unI3VqYl60f5ipXtWWNiAVlE5R1O6HM86aN2WeV2UA_-CQlZo9AxPGvVWtbZlhTh1fZj8hoRFlalstpqT07yzXNGPJAl0WZLzuxfbUcwZAlTEV_LFS9XHW_O3sWSZX0xcKwDvSNj5GqZoiRs1e0oWwN-fs03upTyYfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsD0lgnTtVV8j8PP_Pdex12kAUPmFV7c2TyoNvNrumLVQiJFqTI02Hkuttm1J08VeYO61vUWb0olk6feE61efZYjsv19t0Q7J0wfPBIDMPVPzr4vbSofqbjP20FrsCGnEWpE9c_z3zRY2wBQNp5DoxsU3BK3TIC0q4hvTeNF2Ha7p4pEibCO0nDb037fhJpSC_JeYQTKVCxzmDHmGfAxNqeO4_KhUF3jPpnZ4Ld0je_hza8-esSwab1A5hhtT99XiOGphU3lJaLMvGo7QYnWVTXJaqR2sMgTfjq3nrVbb3STBREBNEg_btgaoxlG2brrEEzlOrVi8r8N7V-G86U5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpthfIxfhxBnYIhIEzrRQ9XY-VTbv_9RAf1iOT3hw5hTYOb25NmMcqIynXX_AGbsEWSNyPIP6yOcd-qNP3nNjyAkVaXWdh-PXDCuj7LVfbgtGLs79efja-4m_1ceJo2jW91tncAgx28qVdF2i5u_V9tgFW4odZIzICwi0axtdOfDI7_44PqmvU4wP48levDmDbpjBQaXD7jyysGe1dlUb25UaH8Ih1iv3Si3YhAz-v0iuzYiZMfqW180s1xiWtU-fyAtAKWB7WyGHwfLLPPszZ4-pSbz7jFF2HAJ2f2JWxufpuLIZX4gT3E8VzZKtWkmGgr5GgOW7rNF2o5Au_E5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxEeXnOrojBuDun7g5b9N_ovDmAfu2hLv3LAXfF763EnFNZGSzY6BXL2Pqkt9rCxxVkUXRVBD69tYq3k4FtC6Zb8_EYRc25JkgQo4qxCYivIhqZ8pnngIsgqw_V2RcVya3VPr6KAIlUvYnBqE9nGE_aPDiDJVeAbQujD4WFS165F4eWp64DTPtVb2iq5FY0l-FtqOX9JDtFPoltsrevt-CqLOm1mruftkozG0M34JeTs587rC7ifSXxIuZ7ZuYjsk9O3yLGfsKmPDkE8L-9gOaty4MBnubaEv6XPgHg-kD4WDvwzfU6AWpGURPBqRtWcxy07fPp4gsvewicBO-_QZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjyOFUMJB2LCxXmygdJQMGDbB1h2Zj2Hq40L5ROiP-3UDp3hMIpjgqZwSRBVuJlH92XYab6IWhUFxrzuDpfmOCNFY_Xa6-r-zQ9wWO1WZ1VhG2TCYkgdqCTwAkBAXOihtG_QvMsIYcCu-fEnLYC5sa7wLLYgpXHsfurd4K-fyL77Ld-C9O4CUGyl0XUuV1jbinNoaI4_5V6Jhg-TE8cC53fyhSgb2gXHL5dd07tiC5JtbFBI62VeIy1eRw9LBHgoZCaXyQFgtXVt61uPPMHwYTORmMlANN_ExyHkg-WtJYzGBhxEO8D11ppAaRq_3UdFxf8GsZoCQaKOeSkPh4pAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/En0Y7uLnyAT1hhFdAzE9lYypa4doXDgAeA0KSbOdoKfa-17ecGv8dC8YmKqHzM8aj8PGVuR216VEEG0cJXsI64DHxtG7Uz5BgzeYjrYh_bhZRU_VEhgn7y7W0T4B8eNSBd2HK2NBPNENKT7g0SzBT8Lqxj8XIvfGUBAqrW3OnZ_DfaSu36axa-crWXegQiK2B_yVJmV9EqowNzii_DYZX91N5-rKihErk5_9xakz4g8ioeNiAWP0Ija9tMt_ca4-7MZhy-atNWoPWfkusyL2jIZk-jZp5GmVp-Cqet2T9-ExjatI9X-xPZzThDVgC5ugYlZ2YEJPFsVnQGjWaCxMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcSbsApribb3Iv49EQvUdnjrFUG4u_woP4I3zGMzO76n2w9bU1KE0gfs_XL_sIzI1So5gKB1QUnbVL0nZjUrbGqBPch86C-Ib3VL1XYigWq4on_yX5A_WA1kKnmaMVz-acLszxVDyXFF3YSDwG_bwRq9FrSGV0OjICwvvBf622C825rmXWZ7dQp8dj1ha9t1mrxMlAKs_OOHK4330t834n2oR8DjfuVvMedPOOZnX3F-P6ENBuF2FHlf_wsJwj6xGM4a7Au6zm3pi-1f-nkIUWlm3s2xFQXKT4N62m9e4ctx0vllzxb304Jy-3OAE3HlFW46Fz8KgBzzTYtnAiYy9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OzbSAal4iLVyW4bauakcAjvyM_3RI1o7Ubit6lSpWftXMVs90az0QG9QIwDEfPwUMzQZGhDQWPMzfSQBQyLkn8qIB3C4cERVES-3DoyvOOiEJkh9XpnWO3MOgTJMFMOl7SqPnBBmNZI9S3eBflC667JhGXtBCgjYgF96GRNd8-PgpY0KJTBIT1LHcA9wRyyVJ_qDB80F05FraK1D3r6tkcYBj9QGCN-5tYf0XBi7SuJBqaf2TNLtPrsAsSGXTqigItJ-QljJ3yfrkWHMA0o3zG26GNzhfiNaVUXYrGy0Mqluvtld5bzr5DHlzmWHy4FQDhS2NrPAXKe_XVMwIEHj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wb-CD0VSXuATUgVTA8yPJ3S5K6ZMaqB5j_cZSqF5pOpQiInWkH4golzCS2_s-O8TY2vM1vi-NcfYQKZ4CmvmW0daN_FfzSi7CpRkyu3GLtbrL26kZJybRMr9OdgXRjCA5yX_WbV78oOuu8l-rgi6zFBP7J4juorBJkbjza3KW62E2uGNryQs7r7ywCl-i794YJLYlQmDBzictWa4I5IU6kpC2mMfdROFYCPBvQbMzSenA6SUiM_0IM7si7NlY4YqXFG0bkOnE7PHgwrnRIVjsxxzpKM_Dd4onIr2dnj7BxSHnKpxqP-I7oyXsZw5ERouSFhHpz4U49ngxLwMtKjZig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NUsBrrElfgKr4k_PU7FPm-RhCbVf5O0-ayfW-tlIuJONwdRHRa_AwqVJUkv2O3cb43Gu9A164pOHj4Ikwjw1WSbNBQRpxP50_KOouHIBm6DZsDWMwKH8yGtH-1aQIzVxikobCXQoEIIu-GxSxxA-4D984pxMRp-9V17W2rlMqD4NDBNYakgIa3iVLOT2stXW-deLFNaru8rUXAUBk0HJJw45WqHSWp6Yw_EhY5Aidh4utQCfILqIyKChLiK5Z9OUAbBg9URS8wPYVNdWxJoyq5fpwmWssTX3O_2v5fg68fMSVqfub6SELDI91Pk_tftMlC3poVTxrnVXZDonSBLTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xf5B2EDiYNgQn3mXquET3ua2fnfy6Weq50Odut8bAjN6TcunAvf6fzKpRrvfk5RkGQJVS5KrtpL5Okh3NBTa6NBuAon1NodWj-QgHpdPlh1S5i9wc5GWfoteoONLlyLg2V2oSgZgGSjVNWExs0NqjJN75nKaJ_Tiqadqbbs7QrHqg0M2vRsNlDKGGfa7RtRd6pN_pKj3zbBMSV0aAZJsfDRgxW5JbdY1cM3_w1-WKOy9Ckr_4mje9z0pOlXw0ybjiscQ5XTVU8Nn8Xpz-2lSL6nyHojLBGXvPb9dMAoIwuXGDzI16Gpm2V9YGk_V_PO2d_TuOe6W89Ebcr8CQmu9tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j41LL6vzr-UvSJPCJaCuMDvYWwiGj8g0d_vZpB0JRxuLgiZlcff2GcwfuFUG15w4NGfxciUpb1xDdIV62Dy4lHYNt92YU0G2oO4tGm4ASIo6H9Bidh5XpGCzz_ggRIFbPiQqtCc0_x3f7DiDdh02_wfRnGCyB_ZSQOVFmKTYhXd2rzWY33PwphEbYdtvEyypT1sHZ4P2aYVgpC303s-FYGFifoF-7-ZeSFVByQWi1HYiz_SmZR557Qf6X9ijTOjmbeBxWUTdxR6ThsmGDSD4eaM4kxYNZ4Tu6GqgRRz_SaFF5yfSqg6PpAsVjRMbA65rSS_b4j5YYNM_42OYngY3rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
