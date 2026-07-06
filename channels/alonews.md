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
<img src="https://cdn4.telesco.pe/file/jigrrrwDjZa9CCsY8INFgSsd5VoVCqY0KWW-oI_N6bEfPoq1u178EHh1KQzwgjjh6G5qnJ-jfkUGG69mYopfagP6MXMlA_t7mrwS7AwiGFQSEwHzElO6SLvsHnSo9PMhntKUnpOXMlnPVa57uyTkg9InQLrvZalk1zfTT5TKhnpqBWv_XkIxbOUwdnwhYfE_tOkd3i5zWm8IOG0yv27pjbxGcn4djfRa1IRSSp-_VEl1h1dGfq0mXOXFuhymLlwlMuo8BR35XY-akRL9sBVm9w2-156ynKID0HXCyxfY72fMmOb_WNxPkBzqgwXwX-tXuOxz5DbFb1db8S7j8b1C-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 929K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-132044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/wBnld2Vq2ITDCAURniDe0cTyPYplQeb0l09VZ8oDkJC2O6VavtAn5JT4SOGI2Ii6KFsMi0jFtbSC1iR4S4MJxo4Yj6_0wO4lGhKGoR8W96QbkmJUcO_iUrS5rLIhsA60USISMc6dZKSWk0bVHnWvAzXBpVKGsFtWOzw-Vyeq7J3mppjgTqpRXxxtwpj3_Ojf7hiPhcjqprm3s1nH3LEmw05fLDF6hCL2jY0BYoEi8loQ3sjOiiZyP7FjpyaKoCT9mXM9rGaXAv2p04UMejwpb-zIac6o5CIMp6htNH3TJCDg58eimNWD-TjoGD_MaTI1GlDi5bylQwF-KwwN6A1BNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dyg7wt2cBZSEH_4oNrNazZvnkEB9WMoid2bUL4_pg8RujjNsddTYIrTGaGqWq8lisqgM9TQbYhDqOJoouIWh8FaOCOLAWwkiyLiq_ttUCzRLWNWjQDZNqBtPTfhj13KKSODqiZ0R4K-5jfOLNly_W2JlyyW12pLpDslwMEPY3DHtz4pMccj9zFwoZwrOayitXuAAOB2HPfwh-VXEYfQ3lTaYkFc0iRGnIy4W5oN3l_FSwWyes2yI5pndMRgQg5LPdJ1GyPOaPQgP8wvsEetJvmermy3Haduy28EQB58vY3OGHTqWTOfpMeog9XXIUE5AFQG8_e86_7zV0mX2uLO6QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین به پالایشگاه اومسک روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/132044" target="_blank">📅 15:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سازمان پخش اسرائیل: استعفای ظاهری دولت حماس چیزی جز یک فریب نیست
🔴
مقام ارشد اسرائیلی: حماس بیم آن دارد که اعلام شود این خود است که توافق را نقض می‌کند، به همین دلیل وقت‌کشی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/132043" target="_blank">📅 15:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نتانیاهو: آمریکا نباید به ترکیه اف-۳۵ بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/132042" target="_blank">📅 15:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نتانیاهو : از آمریکا تشکر میکنم
🔴
نیرو‌های قویِ داره اگه آمریکا نبود دموکراسی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132041" target="_blank">📅 15:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تایمز آو ایندیا: آمریکا مانع از حضور ۱۳ کشور در مراسم تشییع پیکر رهبر شهید ایران شد. حداقل ۱۳ کشور از جمله سه کشور از اروپای شرقی، پنج کشور از آفریقا، دو کشور عربی حوزه خلیج فارس و دو کشور بزرگ شرق آسیا یا از این مراسم انصراف یا سطح نمایندگی خود را در پی فشار ایالات متحده کاهش داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132040" target="_blank">📅 15:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
به گزارش اکونومیست، شارلوت هاوارد، سردبیر بخش آمریکا، نوشت میراث دونالد ترامپ هنوز در حال آشکار شدن است و شاید در نهایت او بیش از هر چیز به‌خاطر کسب ثروت از جایگاه ریاست‌جمهوری شناخته شود؛ منصبی که تنها ۴۵ نفر در تاریخ آمریکا آن را در اختیار داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/132039" target="_blank">📅 15:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132038">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فردا سه‌شنبه شهرستان‌های کاشان و آران و بیدگل تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/132038" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132037">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQsdEhbOQQZapaJIZZqbNBcfwjQm_9YczP-8LVdtQm4FmTe803eHmh0VIM6Vuth3Kh4oJbI0aJ-eYuIo9eiWA-kGFlGpA8IJW5vMQHyDvzCcbKM5DZCLZIMHUnAekZbhpYy6R0n2_UHJkLpx5cDq8P0_rUZkEBwxxPPUE1P8G7bS9P9KG0F4k98Ovdk0bcYq7OMsoeUA3s-Emf26lhBdddv9QJH0RT4-c8bWrPAXd9wFCmZeWfIw3a5_gBCJxrk3nunCoN41zuXqGTeDVSzhxCKy_jat3pxUW5jWBks9fO1d1Des0Ctb3c0XSUObBZvGvFDPHPR5rzl3kwuEHDyJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی واسه نتانیاهو و ترامپ ترامپ ۱۰۰ قطعه زمین ۲ هزار متری جایزه گذاشته،آیدیشم گذاشته کارو انجام دادید پیام بدید !
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/132037" target="_blank">📅 15:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132036">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RZpaoXdcP83f7npmOk5KJLX0s1YCMEzclkvsgnOL-CHCzdl9mz_ecyvewSAlnj8oAAKcyh6XxTGIMzedPpt5TV4YobHtMOmbr_3tTaguQqRib2nuP1j22Fjl-2gr1JBXaFDo1QcXP6vLp8RLjj3wpL0MmRS34m-KX4mdKZ1PXPbeXBonYMHSOE8QMQm3QRogyzS8OVBi2w7rlMbygXjMUno0LXMFfHbaPzcKjSqg7p6UEbglBpaHhTXVWZUhECWOA6XFQ3wdsCXqExqMY6sAuwLqPuYrxsRoTnFEJWgfTuoYuMhk8XSpA4JtAb-lhOihrmS2JJtZOg6lBEYSB4PRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵۰۰ کیلو طلا، جایزه برای کشتن ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/132036" target="_blank">📅 15:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بریتانیا تحریم‌های جدیدی را در ارتباط با روسیه اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132035" target="_blank">📅 15:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، معاون رئیس مجلس لهستان گفته است این کشور به‌طور محرمانه موشک‌های رهگیر پاتریوت ساخت آمریکا را به اوکراین منتقل کرده، در حالی که همزمان به‌صورت علنی درخواست‌های واشنگتن برای ارسال دوباره این موشک‌ها در جریان جنگ ایران را رد کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132034" target="_blank">📅 15:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ادعای عبدالرضا داوری: ۲۴ میلیون نفر در مراسم وداع و تشییع رهبر شرکت کردن و رکورد تمام تاریخ رو شکست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/132033" target="_blank">📅 14:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
استانداری هرمزگان: تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه تعطیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/132032" target="_blank">📅 14:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/132031" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بلومبرگ: اتحادیه اروپا در پی ایجاد ابرنهاد سیاست خارجی است
🔴
خبرگزاری بلومبرگ گزارش داد که اتحادیه اروپا در حال بررسی طرحی برای ادغام چندین واحد و اداره در قالب یک بخش متمرکز امور خارجی است؛ اقدامی که در صورت اجرا، می‌تواند توازن قدرت در سیاست خارجی اتحادیه اروپا را دستخوش تغییر کند.
🔴
به گزارش بلومبرگ به نقل از یک منبع آگاه در بروکسل، «ابرنهاد» جدید امور خارجی ممکن است به‌طور کامل یا جزئی وظایف اداره تجارت اتحادیه اروپا و همچنین اداره خاورمیانه، شمال آفریقا و خلیج فارس را که مسئول سیاست‌گذاری در این مناطق است، در خود ادغام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/132030" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
قوه قضائیه عراق: 25 میلیارد دینار دیگر در پرونده پالایشگاه‌های نفت کشف و ضبط شد. همچنین یک میلیون دلار و 5 کیلوگرم طلا در پرونده عدنان الجمیلی از منزل وی در تکریت کشف شد. مجموع اموال کشف‌شده تاکنون به 127 میلیارد دینار و 24 میلیون دلار رسیده و تحقیقات و پیگرد متهمان این پرونده همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/132029" target="_blank">📅 14:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2684c5fbb4.mp4?token=prcUmNe0LHctTjGA953k6ytoJ7sodBxvcN6vsDOtsoRM4SxD0UQG4u_CUlSvQxVhAmqFl4AM1fy6gnLBkVTpv7JJ4ywwzWb2tepPXNEzFoEPGiEG3GhCioBAKShI1GASfE0zlrbi_HSTafTkrBFxrcWBuzus_ZA0541sbzqVcgL5EreiQLVZ5QsM26NboNIo3n0YsJltyhf_IFigMTaJbhbY6Viap1vpRmXV2OSsrpw7-1o3TBXz0YY5SgZEAoxO2iyeqJi_gnOsjkAs2vJPPeGxMOaVl4ioHX13Fisl76FSjUb8q83kl0d8Vk6RxteCM6GJ7Uwh6sMIbbhwkyNbc2qVGQsW81xBOSIdRKaV8XqyGXKCZBU55aO6nUPmuLBxnayhXgVErs8akVSIDsQclMEb5-NJ7H0vuDReGPRVbj09oJqWh2AfmW0tmEIjrfBdg1lvI6GxWQQNgHJ28CyxVYZ34nykuvA1T7spljX6dOpPalCcDCvHlmKpb-1WqULLF7JQVGgHgEyW3Xg48ZIbLsC8q2yTl_XNYNgl_Z_tTPFJFpjCEQI8NuOm0dax1Y9HWwsQspQOhD0PPDQupo1cSPZySyyyhaAI8QrUceBE3VxdxcaHU8NJ_awgQn1myGPrYTwuIRr56s6zes6Uipx5mKAOMuUNDvU0a2TIVZQxjUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2684c5fbb4.mp4?token=prcUmNe0LHctTjGA953k6ytoJ7sodBxvcN6vsDOtsoRM4SxD0UQG4u_CUlSvQxVhAmqFl4AM1fy6gnLBkVTpv7JJ4ywwzWb2tepPXNEzFoEPGiEG3GhCioBAKShI1GASfE0zlrbi_HSTafTkrBFxrcWBuzus_ZA0541sbzqVcgL5EreiQLVZ5QsM26NboNIo3n0YsJltyhf_IFigMTaJbhbY6Viap1vpRmXV2OSsrpw7-1o3TBXz0YY5SgZEAoxO2iyeqJi_gnOsjkAs2vJPPeGxMOaVl4ioHX13Fisl76FSjUb8q83kl0d8Vk6RxteCM6GJ7Uwh6sMIbbhwkyNbc2qVGQsW81xBOSIdRKaV8XqyGXKCZBU55aO6nUPmuLBxnayhXgVErs8akVSIDsQclMEb5-NJ7H0vuDReGPRVbj09oJqWh2AfmW0tmEIjrfBdg1lvI6GxWQQNgHJ28CyxVYZ34nykuvA1T7spljX6dOpPalCcDCvHlmKpb-1WqULLF7JQVGgHgEyW3Xg48ZIbLsC8q2yTl_XNYNgl_Z_tTPFJFpjCEQI8NuOm0dax1Y9HWwsQspQOhD0PPDQupo1cSPZySyyyhaAI8QrUceBE3VxdxcaHU8NJ_awgQn1myGPrYTwuIRr56s6zes6Uipx5mKAOMuUNDvU0a2TIVZQxjUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری وایرال شده از برخورد موشک های هایپرسونیک روسیه به کی‌یف در حملات دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/132028" target="_blank">📅 14:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132027">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روزنامهٔ «پاکستان آبزرور» از احتمال برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132027" target="_blank">📅 14:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132026">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ویدیو هوایی از جمِعیتی که برای مراسم تشییع علی خامنه‌ای اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/132026" target="_blank">📅 14:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132025">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بانک مرکزی: اختلال جدیدی در خدمات بانکی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132025" target="_blank">📅 14:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132024">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فرمانده سنتکام، کوپر، این هفته به "بیروت" سفر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132024" target="_blank">📅 13:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132023">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ_--aCvGdk-bTsW4FMTcKqlQuxbC1jVZ9b2q5mbzaYNwmHbYoRt3yST0sCli527NWJfo0xNfQD5GHKit7dmkfodeatgpy0GRrnewsbsU72DCP1Bk52IM3N1eCi8HyfDD2IfoPs9B-nojC2zob1P5qcswdJIhyUuANeYPjOMV8GlgLalh7As0tRAG8_qoYEpgRr3SXZv_qT2Cmxg3ok7woFitwCsoD6wBfp46qdxIslcnJv92Lt7jI1x-btNi34iT-ISCB5H8tSQi_f68HRQhHzm1GDciIxwPIuhzyl-26zpHv2SEJywfk7Xxzy0fFS1eKydOtTMOiPV2EuR1TLWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
🔴
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
🔴
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
🔴
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132023" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132022">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کرملین : قراره پوتین با ترامپ تماس بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/132022" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132021">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHvQ5v4t3qt0d7TYbK-W25Z5hDw6C-Mwm1nZIXXW_AULcLOKhcXt_Xv-YDQELbptWx4m4vK-oMpLc6rkEnfpFILb7-ZxqkfwIk_jO6IhpRHY7Jwb2JBv8ZsSPPrpsvbsNT1OyO1ToYiymk5GyMS-Z1FOptrwlrcrntolma6rDOxrAjd40X0EarCta_rzWLESy41VaXYK5xxZTskX_V1_CKJfLl55ZO_lP2hZrknund8BeoZ0k4w8MZMgeRZ7ZgmmNTKCv4L_gUqF2zB-V8eKRe8vO6SzeoIkOWBQUk2FQFsN-7KH7a4MiDdlbTDthrsDtTpTOvVMVxH22QDF5L6zBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور سید عباس عراقچی وزیر امور خارجه در مراسم تشییع
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/132021" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132020">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M81HR4emsvnIA9clKIbuNzJZ7MkChXVVxHwnYvy5ZVdKrRi8OI_K51iJG5j79sroK2yBhIMlPukpk4XHXI93YuA5MPQ8yQSJpbPSJfKAdyD89pevyONCzznMNL8xNBJe-KTZJBwXH3B5LEI-awuYWWU5Da-_f_MwFniOgjWfqEJIhFqrVgCYueDdt9djUNnEB8ZPj_of3EwIjuC9P4ypjf8dlV-LdOIUVNOwpSIKCS3esvDJPIjSo16iCnHJtfLkBtPo_ez73G7M5X3PsGvfjZNu55HtLZjlaXYSqoLb_ueviyZKFgXX9r42V4-yWZy80UsKrC-wNVd-Ju_CF7RGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک بنر در مراسم : دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132020" target="_blank">📅 13:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132019">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نتانیاهو : اورشلیم پایتخت متحد ماست
🔴
هیچ‌وقتم قرار نیست دوباره بین کسی تقسیم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132019" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132018">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کره‌جنوبی: ایران در مراسم وداع رهبرش از ما دعوت کرد اما بعدا دعوتش را پس گرفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/132018" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132017">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnnEkSn_gznw5k9ygOzZW2-Kyy7KGQ7NK40AuQTEahdKfaM3YEAjqXIij9GcXBK9Vp8tD16VOMk7q3yU8jmFT7t0-eGa-MFHjQoSyFUWvXnORoUX-IfryEWwiMPxsrQor6q_jAiNIw0duEsdHV2rdjLZwxIDUbP-1cWS1MEKSzrjzNuegKHtik0AP1oUACDgrB1_gFtBK3LGl2WhLFV9TXpnPSGtnhFlWnqkZ--1Al2ljeoMWPk1p1LQM3kDidfw4Ajznzixt1DGZq_lwgUHwtMGqD5lZ5uhZtom0EcewNU08DUffpBVy3F8KYqv07dCoCLRAOTdat4DyYrNEfzA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان، نبطیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132017" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132016">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر  فردا در مراسم تشییع عراق شرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132016" target="_blank">📅 13:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132015">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc3c73d84.mp4?token=OHtiPnpa80DWtiZVewRFgTxIE8vNEoefPbs0N96bg4CY-m_ipDLQvAhQi6jFt7mBsWCylFKdQ2yKag7gCk2U5Ipyx4kw_hFZpDgJeYWrXgkRCiYtJx8wsOcDVv9cWYyfkTDS6ibTPLIaTv7l-ilYau-ZF3nl_CE2J8uMGn6obYio3XFmwz6A1UNs4xRjK77axerhkiSSoI5WdOqSd7b_dvKmcEwhgqmT7xzV0MQTI_5wnl8SaO2f8A8uSSnjVNDvpSUy6rKTBRTaAO6iPHj3ouNxV1Opk0nUF6sbvpzE-ugRRXPBdrD05QAM0IUZb8PC1kFypHS1OxlsQFeLZLWZBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc3c73d84.mp4?token=OHtiPnpa80DWtiZVewRFgTxIE8vNEoefPbs0N96bg4CY-m_ipDLQvAhQi6jFt7mBsWCylFKdQ2yKag7gCk2U5Ipyx4kw_hFZpDgJeYWrXgkRCiYtJx8wsOcDVv9cWYyfkTDS6ibTPLIaTv7l-ilYau-ZF3nl_CE2J8uMGn6obYio3XFmwz6A1UNs4xRjK77axerhkiSSoI5WdOqSd7b_dvKmcEwhgqmT7xzV0MQTI_5wnl8SaO2f8A8uSSnjVNDvpSUy6rKTBRTaAO6iPHj3ouNxV1Opk0nUF6sbvpzE-ugRRXPBdrD05QAM0IUZb8PC1kFypHS1OxlsQFeLZLWZBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132015" target="_blank">📅 13:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcsRzwhIsbLxCyximpNsVXL0cCbu9xaSWVWqoE1-hOiSEipXFyvTRGRn7LxYvtq89gqCTukZ-MSJsxOpMsgLwle9WHKqc9gPA8NEq92OJbeMVOwiOLycJ_ca0sEcjTFS_RltqqZ-h3nx5O1nqCWhucuQ8qS5AVUdVWZzmeTSqYbg38sFU0fUO3DdWy5sal_3SucMN9IYoNrDDVHsl3tBsYsaIAeA9juHItmhHbN2eoHT0std6Y_fgM8mcj7liroJPGbUOTAk2MdADNVJ81OKF6NKOhnDUvDvaE1o2bji5wJOXGutJ0kSepMqNljk-Z_Nc2mnYan5F-yCndFdsQ68YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در شهر بنت‌جبیل جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132014" target="_blank">📅 13:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات زیر :
🤖
@Team_express_bot</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/132013" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
سرویس های V2ray  Team Express
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
🤖
ربات خرید
@Team_express_bot
✅️
📞
پشتیبانی
@Expressuport
✅️
📢
کانال اطلاع‌رسانی
@Vpn_express_sup
✅️
😍
رضایت مشتریان
@vpn_express_supp
✅️
🌱
سپاس از اعتماد شما</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/132012" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مترو تهران: به‌ اطلاع شهروندان و مسافران گرامی می‌رساند، تمامی ایستگاه‌های مترو تهران و حومه در حال حاضر فعال و پذیرای مسافران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132011" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132010">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3Ur5xo7nzGU9FcJPSBtee6AznmRcio7heg3nj92jMdJ43AYsQ3h9Rq7UkVTFp1-fh46X6gFsDRqtqMJ3UaWOxIgxRIaqpLbVklkUPY3_Z7d5h4n1slz-EDv19_VHYZ6mc36GKWssBbpRDCYXWmT8spW4Vgwi5yEN6OO8LhTQravjc6n0n26Szju1pgvfDOOxWLgiAOsTectcwwovMP8mk8uP2xWRCaa96GNEoacx_twRjOnHNsSAasyyaaW8L6ZIvsoEClAW6719DfrpxIme0B5BTJNC-lNDSIKO2qx5HOiRDxE0r-9J_BVfrZW5Q1K8W5E77nyKpQMKirGCLicQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای تأییدنشده نجاح محمدعلی، خبرنگار : امروز  سید مجتبی خامنه‌ای نیز در میان تشییع‌کنندگان حضور داشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/132010" target="_blank">📅 12:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132009">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده/اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132009" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132008">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مجری فاکس: جناب رئیس جمهور به نظرتون کی قهرمان میشه؟
🔴
ترامپ: ایران نباید سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132008" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132007">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_JB59BVGnHvdX68aPmtsDugybVmFFSlFmhOy0Twh9QXzqzICLCe4mxqmwxuw2fQ1XEgxNyNwkLV9tfWWxpt1n0cEVudbHrTHpF3Jkvtfg-wvOfyHS4JDSoYHOn5FTSeY7A6B0bigMcBcuTKGa0Nawe15UUGDN9rJ58hiFixkx41Ku6gWzs8XZdI7qWMJT3ItCsUVXEeMNrtipkrznbWLAaoBSz-MqJIC-n2MI4SEm5QYWvOC_bQkhaNF6zAu5cXbsJuZSepDkwvFNnrJuZ8jiRjsv-U9pVXMXtjoZCA6Kda2WMJWLpzCtgkpYaDJSjYhC3tq6-_cP0uyOwkEym5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : هری کین یک بازیکن عالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132007" target="_blank">📅 12:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132006">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd089597a.mp4?token=RH8qQvQlIkc7BvMzaGDhTU13Pv7WQ8pJ0kvtRKtPXNHpZ5VHkZxEmTXf8nBTPBhCRE51ZEyRpd-DOPqBAE2SOUwx4X0g4FZXOcjkVZmm4rmR1JD0mAvNc_wKpQTm3bkvXcAlCETazPiooV2CVR4aKyMsVnlfbumg-RuPpfk03xMjkADdgiuawpo2ey6KSs8LpObX3N5G3Hnrkv8broacfCdXvRzj8dnYjNyliVYPXD6LU2qO17NAbl_HoISUIb2qFpGJZ_Nkr5B3tlK6oxvspenXan3ZMIHvqKbLoMN9jZAX5x6egBBEM7eYn878IYCw_6ISXPRJ-0Q0-LAbeS-5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd089597a.mp4?token=RH8qQvQlIkc7BvMzaGDhTU13Pv7WQ8pJ0kvtRKtPXNHpZ5VHkZxEmTXf8nBTPBhCRE51ZEyRpd-DOPqBAE2SOUwx4X0g4FZXOcjkVZmm4rmR1JD0mAvNc_wKpQTm3bkvXcAlCETazPiooV2CVR4aKyMsVnlfbumg-RuPpfk03xMjkADdgiuawpo2ey6KSs8LpObX3N5G3Hnrkv8broacfCdXvRzj8dnYjNyliVYPXD6LU2qO17NAbl_HoISUIb2qFpGJZ_Nkr5B3tlK6oxvspenXan3ZMIHvqKbLoMN9jZAX5x6egBBEM7eYn878IYCw_6ISXPRJ-0Q0-LAbeS-5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ترور هدفمند در غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/132006" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132005">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ارتش اسرائیل: طی ماه گذشته 20 فرد مسلح را در جنوب لبنان کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/132005" target="_blank">📅 12:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132004">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/شرق‌الاوسط: حماس قصد دارد طی روزهای آینده انحلال دولت خود را اعلام کند و حکومت غزه را به شورای صلح ترامپ بسپارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132004" target="_blank">📅 12:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132003">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449fab3a4d.mp4?token=PFaauVl_I5rXf-Gljfckj6BFaZOx80Hhaq4hlp04MPpg7mfLhWj3We-iOWnnmfISYvomFxLuPk8iS1fDiki3tSHG2XF9Wt_a7e1UawYGdpz6vf0tFp3Bg0fgv7gUrNWQDlpl4ag-YLj5YZYuzbNsok8hlzUfW5IWUVEC4fGSW9DllYWjv2wU_iw6yQmxdbvdPe82mua4Au1_OGlKugdJR7WtfQ6vRG_A0EQS_SfsXozAzDktN1rVx_dZCib9hEQFx1ZD0Hxfdb4wE5xH3APULE4JWwsDB-JQXKTrrWaX0qT-B-dpObC0AOGtaBKtm-JQdOZMwnVJah_Sgc9o1yAxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449fab3a4d.mp4?token=PFaauVl_I5rXf-Gljfckj6BFaZOx80Hhaq4hlp04MPpg7mfLhWj3We-iOWnnmfISYvomFxLuPk8iS1fDiki3tSHG2XF9Wt_a7e1UawYGdpz6vf0tFp3Bg0fgv7gUrNWQDlpl4ag-YLj5YZYuzbNsok8hlzUfW5IWUVEC4fGSW9DllYWjv2wU_iw6yQmxdbvdPe82mua4Au1_OGlKugdJR7WtfQ6vRG_A0EQS_SfsXozAzDktN1rVx_dZCib9hEQFx1ZD0Hxfdb4wE5xH3APULE4JWwsDB-JQXKTrrWaX0qT-B-dpObC0AOGtaBKtm-JQdOZMwnVJah_Sgc9o1yAxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو تقاطع خیابان انقلاب تهران، ترامپ رو یه گوشه گیر آوردن و دارن به سمتش بطری‌های آب معدنی پرت می‌کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132003" target="_blank">📅 11:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132002">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7oApJQYxqlqzDqf-SCHtqwSoVteJuFvN4xzE4fuMHXMIfhRjMwPGZAAhTgK_Ie-uLuusElVGiqZbF0ybih5la_ZTYINwf1x6iEZmthxo0tnyDNvwZysEvhQpgzF6-a05hghf19IElF-TzSpzVrkf6fmi0CfCR0b9-9FfIeEziTlXPkk9xzVMiFM9Y-b7ZSgkM6DDVl8FXMe6u9oDrF786G1ewc7zdSGx8dlSDQlHWmTFHzVM8g46rqM0VNYCBI7YMc_S80hOhX2r8P4VSKFA2sXuLb1D5KtQzJzRjKzObTm1iaFrOIWHg-q2rJP8Zx4KWwARjEo_dF63or-JGhm2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۰ میلیون دلار پاداش برای قصاص ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132002" target="_blank">📅 11:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132001">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b7e100ff.mp4?token=VLXS2QEIuX9r_hN6GByKcQ_0bA8NQGxmltM42B7Vush9rxAj2vbtFMMXZcv8l-grhXGDacqAc2OF4vNGImRfsmCAVXZXx1dMtBTqqyK_L-PF_6yW2V7V23-991V2G4454GVUUs7gx03pwhYA3tPSg869B6Puj5n1VOu4WXmsOV1KdNjDdsq_a-v0IkPHzMaUgmhQiDJpTQ31Wrcs-u0fLc_UMW3DlVsvnOcyGwZNE-eK25rjRBlsCtCwgYErmM5GXOi_7ry1h890GMAzuhVXYuxw62iYSRN-gxBLEkd2-_QwJWzJxKoOge88Mle_uPItL73g7woPDbhVNcPhS9W7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b7e100ff.mp4?token=VLXS2QEIuX9r_hN6GByKcQ_0bA8NQGxmltM42B7Vush9rxAj2vbtFMMXZcv8l-grhXGDacqAc2OF4vNGImRfsmCAVXZXx1dMtBTqqyK_L-PF_6yW2V7V23-991V2G4454GVUUs7gx03pwhYA3tPSg869B6Puj5n1VOu4WXmsOV1KdNjDdsq_a-v0IkPHzMaUgmhQiDJpTQ31Wrcs-u0fLc_UMW3DlVsvnOcyGwZNE-eK25rjRBlsCtCwgYErmM5GXOi_7ry1h890GMAzuhVXYuxw62iYSRN-gxBLEkd2-_QwJWzJxKoOge88Mle_uPItL73g7woPDbhVNcPhS9W7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار ها در مراسم تشییع: توافق نمیخوایم ، سر ترامپ رو میخوایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/132001" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132000">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی ارتش : تو مدت آتش‌بس از فرصت استفاده کردیم و توان و آمادگی رزمی‌مون رو بیشتر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/132000" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK0A4HOMukzD7SHFf0SNrQ3l9zwoYqAXOalkkFoKZ6d5mx-O8c4NlywhSDs6GZZa7vdQbS1rgJBSMoC-c2e7-27VA9KPwde5Xg9LVMckedqjHko5zCjK-FMF8fmCghlwjSXHMugXREFpsm2zQB7qlpc1vVkxh1B-7pX2RPCmS85dESo_WVNK9dUVpNG6Wa-al5-ufCZ9QDX8JvWeh5SyEKkdCXLKF4RWZog3hOefq_xBc5dFjnwCCI-_psPVHGqd_vaEWtRBc5Sabuk0-SvxqKOQvxGeLTnyubPaEov9cteGAXYcInIc4VOEq7VwpL0HUUuRQkhkjQm_IdH6WS6hNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوناتا ۲۰۱۷ قیمت در عمان ۸۵۰میلیون تومان
🔴
در ایران منطقه آزاد ایران ۲.۵ میلیارد تومان
🔴
در داخل ایران ۶.۵ میلیارد تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/131999" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131998">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74ab95ac3.mp4?token=AuxBiEXHA3hiEs-J9FHkoGQnwKgQSf_y0wRFXC7YGydhFyCgx3qXdyeMlLp9qYrqbt74WbNo0NnDh0oATcpJw353fk6NguHi5QizIXF8Wc5ZtamY61B64108r0eMHNAxjdd4UQstyKAU9z43TpzljrWaT3fFV5fJDVuAraYUwYaBUM3gYAVY5bJWH0nDKEIYJTz2l5DyszNSJhTY8BOmEkt5lNvPG-ixUDBfFC4Uj18Dd_yQLykx78g2DkZGMOGZhScyxnXorVqhV6uwtOz1oMJ4nzUQn1im-NySBlAQMeQgI2IpH5-zytlXcas8AvSzJaxrVcOi0zZdak838djy2jyE53re6iblxwcyPqMhKMvgkEAFZMR4f1RUkCG6wD40GRsmEbz0nghyCR4XEbvLAtRfuX7vESbQOzuCEmpG42HgDjYH35zg0sk2Ss80NmcufF008Jq8M6JufNq2_xC_MeUDbBiBgkJL3p2Ta4t0azm2FSUqV0YJWX4KTLTTNSCz0g6UD5InwwAqtPpC7QaEs4TwAV1Q2ATa68QgkRwe6AHUFM_Gb8U7rTbH0EAInJJ7GWsRP-z6Woc_OGNayqYh2MewCwKrpxiaoXy5zGVNvd47cYU_m2FydqioZm91-pxt4Ytb8yZ-QAWttd-CmGrlZGIsKycn4Ha6dSPEcyJ9FFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74ab95ac3.mp4?token=AuxBiEXHA3hiEs-J9FHkoGQnwKgQSf_y0wRFXC7YGydhFyCgx3qXdyeMlLp9qYrqbt74WbNo0NnDh0oATcpJw353fk6NguHi5QizIXF8Wc5ZtamY61B64108r0eMHNAxjdd4UQstyKAU9z43TpzljrWaT3fFV5fJDVuAraYUwYaBUM3gYAVY5bJWH0nDKEIYJTz2l5DyszNSJhTY8BOmEkt5lNvPG-ixUDBfFC4Uj18Dd_yQLykx78g2DkZGMOGZhScyxnXorVqhV6uwtOz1oMJ4nzUQn1im-NySBlAQMeQgI2IpH5-zytlXcas8AvSzJaxrVcOi0zZdak838djy2jyE53re6iblxwcyPqMhKMvgkEAFZMR4f1RUkCG6wD40GRsmEbz0nghyCR4XEbvLAtRfuX7vESbQOzuCEmpG42HgDjYH35zg0sk2Ss80NmcufF008Jq8M6JufNq2_xC_MeUDbBiBgkJL3p2Ta4t0azm2FSUqV0YJWX4KTLTTNSCz0g6UD5InwwAqtPpC7QaEs4TwAV1Q2ATa68QgkRwe6AHUFM_Gb8U7rTbH0EAInJJ7GWsRP-z6Woc_OGNayqYh2MewCwKrpxiaoXy5zGVNvd47cYU_m2FydqioZm91-pxt4Ytb8yZ-QAWttd-CmGrlZGIsKycn4Ha6dSPEcyJ9FFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنر چندمتری «ترامپ را می‌کشیم» در مراسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131998" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab849993e.mp4?token=J0ZDfsWpwbZqTR3s-Jqrm23X3W9bD90026_1sftzVKSNxsE5zH3DIaW6A3Q4pvZEYkLgWzmyDGierhjc3GxSig1FBgyBioUBnxdzFYfy3GwBc9Q1QOI8qHHSWpwAYexh5aYK72dBGeTI728KTZWAZKUoecBRx6MEkiSEEBjMGcBKbXNRdQyPyr8IK7w_M8uhSZrHGOLRYckcG3xrdUwoVkAw5ZgOmsG9P1KEeFEjo68nqpSnHp_AlgVst_bxHbkaArTQedM2rl6YmoCCMFDxHekTnPtMbFp4bNHLdU0Ga8ZpH-Hvh0xeQTaJXqhPvkFNw6nmnTrt82ikQdm-tYtEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab849993e.mp4?token=J0ZDfsWpwbZqTR3s-Jqrm23X3W9bD90026_1sftzVKSNxsE5zH3DIaW6A3Q4pvZEYkLgWzmyDGierhjc3GxSig1FBgyBioUBnxdzFYfy3GwBc9Q1QOI8qHHSWpwAYexh5aYK72dBGeTI728KTZWAZKUoecBRx6MEkiSEEBjMGcBKbXNRdQyPyr8IK7w_M8uhSZrHGOLRYckcG3xrdUwoVkAw5ZgOmsG9P1KEeFEjo68nqpSnHp_AlgVst_bxHbkaArTQedM2rl6YmoCCMFDxHekTnPtMbFp4bNHLdU0Ga8ZpH-Hvh0xeQTaJXqhPvkFNw6nmnTrt82ikQdm-tYtEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود سردار وحیدی به مراسم با موتور
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/131997" target="_blank">📅 11:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQuKPIo0yfHdR8aEhL0vIKILR5m7pt3LQ9SvMDy8md45orj-9iVAC1UsifywuzGxs1q57aLhjIJuqUrs1n4_xxq7VCgZ7i5y9YVz_iniQ3os6fVrpM75nhkCixXfaTOSxmBjjPT-8rlIz2sbwLppcszP7K8N5oYdobt4eNzF4yFyThl5hHYnzOD_NCENd6clnKX-t5fMCRcf5uYO2yNQkM9awKB_GNpwKhG27HLxYZRuWlSjF41zoIoL12pUcTsNhkS-bCpz2hlguGyNYjmHyn5s0K5X5LoV2KrwfLQbfO1Eg4LY5AQcz88VdDuKxkJTPiTbDD2xvwkZU4Vzq8OgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی نژاد، رئیس جمهور سابق ایران در مراسم تشییع امروز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131996" target="_blank">📅 11:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131995">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muiEMFU6OPPjHb6UhXC3toK3jZWl-7Vu9-REh0CwVFOMp4kRoNSzkVoQ95NpKawex4iOV6xgPxQgdAEa0od3Via-oK554-AiLUeN7TTg02R6fatUEVf0MO6WEjdoc7F_7d6E_irSdzyfcKRywwRFSsMPSt0093NAKBopPLvEgKd-UgxUBq2CygGbbpUp69gAZudnqOS2yYP8ShNAqoI2_igjGTX9zPlobDBmdtbHCFZezsOB9SvtLZW1uPPMesiyHDtadacicFqg98iFH6cIrprYN2qwxAEu8I62A5E30EcsHl7aPYpGqCrgDaiFocPbAm2Y9svTYqdgP6FbFhs9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور اسحاق جهانگیری در مراسم تشییع
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131995" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131994">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / هشدار یمن: باب‌المندب به روی کشتی‌های سعودی بسته می‌شود
🔴
در حالی که یمن منتظر دومین پرواز غیرنظامی‌شرکت هواپیمایی «ماهان» ایران در ساعات آینده است، روزنامه «الاخبار» به نقل از منابع آگاه خبر داد که «انصارالله در حال بررسی استفاده از اهرم تنگه باب‌المندب برای تحت فشار قرار دادن عربستان سعودی است»
🔴
این منابع خبر دادند یمن همچنین به سازمان ملل و عربستان سعودی مهلت داده همه محدودیت‌های اعمال شده بر تردد دریایی در بنادر یمن را لغو کنند.
🔴
به گفته این منابع، در صورتی که عربستان هشدار یمن را نادیده بگیرد، نیروهای مسلح این کشور مانع از تردد دریایی کشتیهای سعودی در دریای سرخ و تنگه باب‌المندب خواهند شد.
🔴
خالد الشائف، مدیر فرودگاه بین‌المللی صنعا، نیز وجود ترتیبات جدید برای ازسرگیری پروازها به فرودگاه صنعا را تأیید کرد گفت که این ترتیبات شامل مقاصد جدیدی برای فرودگاه است.
🔴
الشایف همچنین گفت که ازسرگیری پروازها بین صنعا و تهران قانونی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/131994" target="_blank">📅 10:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnS0O7l-0peXkRcskh6UTMliSXJt8GfOo7lJc-w-1lQzzHVU1Ven9T9h0DLUNhQUk-va_LPcqTgEtoJw1wlpDS-h3m0wNzP2uqQvJ7dTK-t8ApCY9h1xk8NqAStCqftwCghEM2WCO9Nog0-nhc0JgFDZ3aU-cp_HYRTKdh1cxs35CxNvWv0wvoanUmsCIVCO0jPQUDmvw5Kd9qhOuoH3vuCoTOsU5VWNMvDzHF_mxowZA-gBLxcspAGMb7yR_3jXXlE2DhkY7XDpQMrCXbVo4UNPEqSCY_V8Il9UAbvYFdDYe3QN_TzO9LahHTnMdaLMtdlgfPG9Lxnmfm3Tzm0Ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/filsq0jr8IXGUCXErLXJPQnZ2tBEb8m74BUTBk2vV5Bu9IlSIjrXoGEwfkEaXgWcfI5kVg6GMRP64n6vmP_welXqDdytkqYkYFbH_fPVmFYHWSxP8h9pnStZoMlMfl-Aqh0GHwVEJLv_i5-VofGdoTUKDVU4qFCpeABob5O-fFz8U83i-LnPgDAnAU5gA2dKE0DoS_oDfzYoQbBg1awp2PAsEdhZZP3DH3aeN4Acq82Hs2JvoseQV4SQ8cB_OwqjRTVJLjuQh9_IF1rHK8GAubYmgOaIgPG0irrOu7a5n9QvrkRRDJMJokjuGQnsqZqodlc1LxIXDpZ0ZF_YcX1pAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در یک نمایش قدرت در برابر ترکیه طی یک تمرین مشترک جنگنده‌های اف ۱۶ نیروی هوایی  یونان از سوخت رسان‌های اسرائیلی بر فراز مدیترانه سوخت‌گیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131992" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری هندی (ANI): حداقل ۱۵ کشور در اروپای شرقی، آفریقا، خلیج‌فارس و آسیای شرقی تحت فشار آمریکا، یا به طور کامل از شرکت در مراسم انصراف دادند یا سطح نمایندگی خود را برای حضور در مراسم رهبر شهید ایران کاهش دادند.
🔴
گفته شده دستورالعمل‌های محرمانه‌ای در این زمینه برای سفارت‌ها و مأموریت‌های دیپلماتیک آمریکا صادر شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/131991" target="_blank">📅 10:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بانک مرکزی: نامه‌ همتی به رهبر درباره کمبود ذخایر غذایی به هیچ‌وجه صحت نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131990" target="_blank">📅 10:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335c644043.mp4?token=V2eywBd3VuzWTegcSg-cZF1pjpzinJlIPhykYEiOOZhsJbxkIPH4kzj-rv7YZ-k2QsEDHJ7L0Rok_8WLrG9WUY0pAAJt7dh049krb9BYDw9Iw6rM8EMba5V-_tT1bLkHV2iTZrr1qLPuayTgkJlYjgQdDtn-cNMcL44R8zdDv1eqbPKCn5ZRiG5YOKRL6lXtSJgbAAEK9DfPV12R0zaUsYH1URNqWlXQEnU82zn6RXqnOXo-T0vVLGm38z5qGLCviWx4mqTI5YeZB15v5IaOnMv3zYbDySfYGR8p3m-gA5GvS6p0Xnkmflw9SZj039tCQLzBs4NhA2UhG9En3zsU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335c644043.mp4?token=V2eywBd3VuzWTegcSg-cZF1pjpzinJlIPhykYEiOOZhsJbxkIPH4kzj-rv7YZ-k2QsEDHJ7L0Rok_8WLrG9WUY0pAAJt7dh049krb9BYDw9Iw6rM8EMba5V-_tT1bLkHV2iTZrr1qLPuayTgkJlYjgQdDtn-cNMcL44R8zdDv1eqbPKCn5ZRiG5YOKRL6lXtSJgbAAEK9DfPV12R0zaUsYH1URNqWlXQEnU82zn6RXqnOXo-T0vVLGm38z5qGLCviWx4mqTI5YeZB15v5IaOnMv3zYbDySfYGR8p3m-gA5GvS6p0Xnkmflw9SZj039tCQLzBs4NhA2UhG9En3zsU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون وضعیت خیابان های تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/131989" target="_blank">📅 09:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / ادعای شبکه ۱۴ اسرائیل: سپاه قدس واحد جدیدی به نام « یگان مختار » تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131988" target="_blank">📅 09:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آتلانتیک: ترامپ با حفظ مشاور مسالمت‌جو (ونس) و وزیر جنگ‌طلب (روبیو) چاقوی سوئیسی خود را برای هر سناریویی آماده کرده
🔴
ظاهر متناقض سیاست‌های واشنگتن نباید کسی را گمراه کند. سند تفاهم پیوند مستقیمی با بازارهای جهانی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131987" target="_blank">📅 09:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37ce8846.mp4?token=HEFRL2PJopmULAzTajx7IAZNjsg1RTPVkqhyTlK9AU6W6nVTIu4sftzlA6d5YjfvF5CJfmCzf0cwl9ME5JJLkUwbB5i8A6e8ehrgHCi20QHDtge0ECTKSRcYbZKAO9FWYsSfSgDMCkkh7KcjFrMi_Bz69K-8ivwQywIlDlvxHG1OB-E6xMSPdUCL88tCEEXlloRAsWGOMgI6EzIoZE2196Vh3ZefSr1JbFDf4PJ5AhJ13-pJ1cYJambTmjMBGv9DmeDxxmClDxHGhqiv1YnkmN8KB2FDOJ6jV_CITswdHjk0mjMosAYiPLUD9TTieq3TPPGEzdpol4R-z9Rhgoi5Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37ce8846.mp4?token=HEFRL2PJopmULAzTajx7IAZNjsg1RTPVkqhyTlK9AU6W6nVTIu4sftzlA6d5YjfvF5CJfmCzf0cwl9ME5JJLkUwbB5i8A6e8ehrgHCi20QHDtge0ECTKSRcYbZKAO9FWYsSfSgDMCkkh7KcjFrMi_Bz69K-8ivwQywIlDlvxHG1OB-E6xMSPdUCL88tCEEXlloRAsWGOMgI6EzIoZE2196Vh3ZefSr1JbFDf4PJ5AhJ13-pJ1cYJambTmjMBGv9DmeDxxmClDxHGhqiv1YnkmN8KB2FDOJ6jV_CITswdHjk0mjMosAYiPLUD9TTieq3TPPGEzdpol4R-z9Rhgoi5Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حشد الشعبی و حزب‌الله وسط تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131986" target="_blank">📅 09:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فردا بورس تعطیل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131985" target="_blank">📅 09:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2888c102f.mp4?token=k66Dbl9RB7ruUpLaUvFSm0SmhldOB2f5fZpnxl-W0dHj-9l760ptZcbKxrd8EmPhCxc6mpqXjvZZWt0zYIcTLzMXvmmdPcttEwcrevGwAPO4RMvbrbYhgE0BrOYQUfXVrmdr4aO_e7JnBGJEa9ORMvqOFg7QhKDmmaVuijEf_t7VuwsNVCcGRo-PUzOvcRSrLKAGwbmoDaAD9wHb2KNMNpJa0yQ1miltBoOFav9mmMT7jR4JCOEkNBMwq5nZk_ytHY_AP3vMG3bMhxA6lQTw1PJ-cWSM3pUBn0__zYIQfPqm1AoDeXw5_etC8QPcdRf-xGaAvXI80b80h4OjW6lq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2888c102f.mp4?token=k66Dbl9RB7ruUpLaUvFSm0SmhldOB2f5fZpnxl-W0dHj-9l760ptZcbKxrd8EmPhCxc6mpqXjvZZWt0zYIcTLzMXvmmdPcttEwcrevGwAPO4RMvbrbYhgE0BrOYQUfXVrmdr4aO_e7JnBGJEa9ORMvqOFg7QhKDmmaVuijEf_t7VuwsNVCcGRo-PUzOvcRSrLKAGwbmoDaAD9wHb2KNMNpJa0yQ1miltBoOFav9mmMT7jR4JCOEkNBMwq5nZk_ytHY_AP3vMG3bMhxA6lQTw1PJ-cWSM3pUBn0__zYIQfPqm1AoDeXw5_etC8QPcdRf-xGaAvXI80b80h4OjW6lq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی سنگین روسیه به کیف در شب گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131984" target="_blank">📅 08:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqLzhSVHhTugROx6htRbGg68uvi97o7AP5iOvW9LkRaeaD_FXoHOiM9aTfKUJemVnWHgTv-9MQqJHi4pQwLi0-uGdFUoqDWNAB_KMmNjzVHbEZ1xr6fL6B5PlRQ92G0a-1XvVdQrMv57R9nnuP-8yq_yG1hXHiiZv1C9aKVUycSOrd-xFB8wpbPmSDLMT_K7HX6HR7DdHJjo_MENB7QegGk-sjG46zhIugJG5TnLAPQAta-lqiEHuK33LAV1zO2g7pd4tFgNjQXQrRnHABmUdOBXG4Lsg7u_CVOvKNbDM-pjdTJDyAOx4aK3UL8x7C0aGQtdKyD5Y9wR2GZXMoWEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی:  پیام روشن پرچم‌های سرخ انتقام است و بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/131983" target="_blank">📅 08:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ccd88a65.mp4?token=KT3nI5TGIPqUI09kEHAuKtCWEZwIBa2AmA-TfunyE80JuUkDh2gjSom8VzLQauW7LQy3BT0eo9v3P3qRGSzGyL8P6psKNHNEfp57LDf41NMh7AwWYjiT_MTGzBM7zuyzfGSUwAfZ2RibFA6rBeOKlLmSuTUOsApi6ObnqtOnTM6_YPNt6VvH-UbSmVfZT5D15R_YOOFiAsqTGVvBkTd7sfyNeGEkiMq2vOjq8YiNqT0OGIS9MQ6fCAFshGpRjgyV19vnu2T0BaD7-Fn4DJNwxVTg0W8UyJu1IZItQz_WxNfgHufj9GhHcClLeVbYSTh4p8PCoNoHHtlnFiyX_t6rCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ccd88a65.mp4?token=KT3nI5TGIPqUI09kEHAuKtCWEZwIBa2AmA-TfunyE80JuUkDh2gjSom8VzLQauW7LQy3BT0eo9v3P3qRGSzGyL8P6psKNHNEfp57LDf41NMh7AwWYjiT_MTGzBM7zuyzfGSUwAfZ2RibFA6rBeOKlLmSuTUOsApi6ObnqtOnTM6_YPNt6VvH-UbSmVfZT5D15R_YOOFiAsqTGVvBkTd7sfyNeGEkiMq2vOjq8YiNqT0OGIS9MQ6fCAFshGpRjgyV19vnu2T0BaD7-Fn4DJNwxVTg0W8UyJu1IZItQz_WxNfgHufj9GhHcClLeVbYSTh4p8PCoNoHHtlnFiyX_t6rCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریستیانو رونالدو تایید کرد: این آخرین جام جهانی من خواهد بود!
@AloSport</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/131982" target="_blank">📅 08:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqidyzzAnJygvDvZfS9svvjrEsX5tWLpZ9Tu8hnbHbNahiejye3k378_DjUPsWeuQ_4EhWIPns9McoV7CSJf8jnAhxRaHiTiCmTrzV5Czxz0KrWo91_lVEyoj0s0xhdkMoOC0xMP_byPfnLiv__324kRKdJ0MSUsnXql8vIgZCnZM_cftMS1K4V7tyngmF-xHPK93SkbDVeG_IO8qZMq3TEOXJ0wW1GVOu-DSDGix8b63KEvnd_YbGdxqrktgBsRdQw3BzNMihwXitlLCFxh07hLnWSfNAUUTs8FO0DCZ5IpwLR6561bquHvdUIQyKaBknWBa9AknRG5Hntl5_rl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی دبیر: آقا زورخونه‌ای بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/131981" target="_blank">📅 02:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-2V28pl7BUXPatZLj_jimb3LGlrX0MNtx-ShyEOIcXoOy1bfawRn-JvzhV9_B7XfiGzgCfw-sqpmPTY_UK9JPOsuGTaCJy60MiUwpFuLTv76sA8jdJXFaBLAzvk5eUcKjJhD8xFXqw-vlvaFhDlIxnGeE7ZpuYnaUcfNlT-lN1DjC2FuygbGqeFNGjAYWBPyV_tQ34_RK18zrvkHBBAxzQi8rNIodJvQUaaLnPef1FV17o7CpZpJQPNb16VWLWFzWP6yADUYSQ6iBqZevnd-fGru7mmCKBd3MbxqaV_lNfzaIA6YebFOhpMqXxFruSSBfHP_HTFmOXweih50hxKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ در Truth Social، نخست‌وزیر ایتالیا، جورجیا ملونی را تمسخر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/131980" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwYAgYdv0hv_RjlutScWsiiIz9Zh0yxbr-y6g1inWiVYHdI-ChRVkRyNGr0RPhbR8H51YffkqAHO8JSlGMazsKwK2Qsoc74VNNLw4--he-oTdZDBDzYzd21aQ5qCVpaj-GmL6dopxGLWpRv9vx_yDthhyQSFOHLfBma-acjjnRSqKAzlLHRH9MkgdhFy42tR1z020o-gzscXHptItTiGmmzOU-rJzbbJwIU_s_G2OzvRYky25kB5prtVmmZCvaqtzIgief6u7AQr2IYmrZg9sQb7q2wMZzII0_hQ0UcqWVug-52An0LXpK2s1e7KcLnP2xRd_1JNF4ravry9iBjxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
نروژ2-
1
برزیل
🇧🇷
‼️
ابرویی که بالا نرفت/ بچه‌غول حکم به حذف برزیل داد و نروژ را به یک‌چهارم فرستاد
@AloSport</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/131979" target="_blank">📅 01:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نتانیاهو: اسرائیل هرقدر لازم باشه تو لبنان می‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/131978" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de38c0981.mp4?token=TTAMbg1EADo0bSNx9R7n0uYAmPSmNTU_Ouyhk08ma0aNXtyvw2oAADlhsFk37g0W-NlNW9On6m4TsoMOSseQrXO8AcAW7i_gVTPd-W59_4HVn-f7mDbnm7mXuRAfgMlT7u9rRrjYWSNd-D-W6q8LV-sSVYIt9KZq2ppOjnfiZRyvW6_gzKoI2wq1n4vTyIiusq-CFSH_W7aHyzkvgqcO7KEMEpUUT-7FAzleUkQXgG3cxhPdE5HNvRdYELLDxl6bS6Ek0Cghj_6ilviA5RchbJa09aOwIr7QIHJcMw10Xhq5PLk1HHwRYMxKgaij-K2KV7Jc-6d-66wKAc2V2kVETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de38c0981.mp4?token=TTAMbg1EADo0bSNx9R7n0uYAmPSmNTU_Ouyhk08ma0aNXtyvw2oAADlhsFk37g0W-NlNW9On6m4TsoMOSseQrXO8AcAW7i_gVTPd-W59_4HVn-f7mDbnm7mXuRAfgMlT7u9rRrjYWSNd-D-W6q8LV-sSVYIt9KZq2ppOjnfiZRyvW6_gzKoI2wq1n4vTyIiusq-CFSH_W7aHyzkvgqcO7KEMEpUUT-7FAzleUkQXgG3cxhPdE5HNvRdYELLDxl6bS6Ek0Cghj_6ilviA5RchbJa09aOwIr7QIHJcMw10Xhq5PLk1HHwRYMxKgaij-K2KV7Jc-6d-66wKAc2V2kVETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بی اعتنایی عجیب پزشکیان به مسعود و میثم خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/131977" target="_blank">📅 00:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سه غایب بزرگ مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/131976" target="_blank">📅 00:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGyxKIytGtWbPn9kieT7PRQglBFMeM9lJIOo-k0EE9Rg9EoHjAyHHcOFiuXIb8REwZS4EVkjpNaCcW98kKayboPQAFuNU4g5jxJNpadaCvjywS8RsRFb4e0PAq1VT41tqtMIYYkzDVGcyVEuER0FuhmiNeT3nIWtIqPdqYNDCVt7tpiGoQmhJIeuMexCgWVArGxd_2s8tH8K_6Oprr57o6MOYTOnezehY45zcPe35Zkdja-SszM9lg-gotoYHSS05Nh0ew3yFnfGIX3lTWWuQaSZwG0nKqDM67VwivkVPn9ZmZdtpita7WiYpdxWy3stMTYly_zhb-sFAgvMgrjttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOmk34ReR1lKN2iqwV13niUCkSxuoTksI7sxRoqr7KW81mN6jYoSI-B8u2A1_Ai-IwPyChRQdQ69XXLjJjYDn8j24zt0vUM3Yk96JsWv7T_cgjYPjhsilJWn3Ul9l8OhNr7Tg4K9Yw7-sjryIrA9-bua2gsE-vN5qYhPqynXkx42_uoXg-8uV5Dc34R70Hqn3xpZRdgVBdknujdB1U7d6FNci3_AJ4YmWuZyktlQU7z3syoCMm8zLu3c1U4dSVH2Ee8gh0yf_2WHVAS0xYILUn-G8HXXVxMdQwYHpkjjFFamPZitK88rw8JKOlph-C2fw04zyfNrQBucvwhqZb6IqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwKeBgDdjV7Fh7NCjwzge2F4eM24_BHGWce4gSbR_rMWt8LzOzpaNOCeXZN1aFTaZIsfIhjJrByx5qgVY3yS_5sl4AnqBITyeHUvczoZwF3gyrEPB1hDnLa8u4mnVZ5e0PatzmyngmVJRoKmq8MT3DYV9h6_VVP4sYBb7rOYbCTY7MpVs-hBVYrfPOmJn2johAhwf144mM1XErprBwr4hT9RmUkYKL6FibKbm6Tx73ZL3ANNtmWyr2eYLgXqamq07VyZ2V6BP5w_BvpWXFRok3TlKC5oSu230Zs-H2xyUmPqp75A4g86QwYJ5HjvmWPv8RnPbZi1-oFENDID7jC2MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سه غایب بزرگ مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/131973" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131972">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55821e32c.mp4?token=KMGs-vqaxozLApibc0tZTaVRf1jHbvyA9sA_SgmlbMtUK3jl5ONLbsDgCTIxBAPwYelEK2oUsv3Tky8D-ivSArS64eH2I5dxtv4lddDMWFqQ2lFv9f3PNH6h-uLlpM8vl54R1DYW0mkgwDEEiRdt5c_xbROdokZeqZ2rGuzFiOEm8wJmRnz5Pm_Qnu938-KfqowSK8wXgWB_kIRJ-JJVaN-qLxN91ZyHU9QGgtlh-vu_vCQAUAd5-NhLQ0y65EUlhqWwICGrebg_cVxwpPaGUOpa8JZ_SwnOM8rquRWWsAOXLdKUlWv0ivbLC83g8H3AGkLxacVLGwNYnOajkBFcQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55821e32c.mp4?token=KMGs-vqaxozLApibc0tZTaVRf1jHbvyA9sA_SgmlbMtUK3jl5ONLbsDgCTIxBAPwYelEK2oUsv3Tky8D-ivSArS64eH2I5dxtv4lddDMWFqQ2lFv9f3PNH6h-uLlpM8vl54R1DYW0mkgwDEEiRdt5c_xbROdokZeqZ2rGuzFiOEm8wJmRnz5Pm_Qnu938-KfqowSK8wXgWB_kIRJ-JJVaN-qLxN91ZyHU9QGgtlh-vu_vCQAUAd5-NhLQ0y65EUlhqWwICGrebg_cVxwpPaGUOpa8JZ_SwnOM8rquRWWsAOXLdKUlWv0ivbLC83g8H3AGkLxacVLGwNYnOajkBFcQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسئولان برگزاری مراسم حتی به آیت الله حسن خمینی هم تیکه انداختن و هنگامی که با برادران و فرزندانشون اومدن ادای احترام کنن آیه زیر خوانده شد
مؤمنان خونه‌نشین که بدون هیچ دلیل و بیماری‌ای جهاد نمیکنن، با مجاهدانی که با جان و مال خودشون تو راه خدا تلاش می‌کنن مساوی نیستن و گروه دوم نسبت به گروه اول برتری دارن.
🔴
حسن خمینی هم همون اول گذاشت رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/131972" target="_blank">📅 00:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131971">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e716df92f8.mp4?token=e-OuIkDWvC16QfW8C49DprdiZyy-KApNXAfIYy2MG_h0QUu86_wmd7mFo6dTbn9dIFhXB-sZQ28-MkZ1ufKdx-Ei2GFcojZrCmeHopZjnxB6KD6zOFh98o_K0SC2yteUvFb0KEG0kQNAKe8g0GgXFpqhE5ur6HCXm9U5K9fIpwFY4IC4fYgjWDDiAswVCMjQrUVieZ9B9pdb4SLV84nhhv8S_hOC06g5ZnQthrEpcM6ALJRXJizkqKGA4MPFjGTcuAwpVRLLbLrxkbEAeDRKV9Ztwr8D_4GJbEHDwp3GSnUlUG1276H7xlIajt8YG3q6AML_as0sq0gJ0CRsgMrw5r_arhWSo8w-XdQrHtxypOFe6loJ2Al5EcAaaC4nu1Z_Y-kFWI_I-7BtOv7tbbi1Lvtp5AOp5STM8H_A_i7h3h_LUT2G1X3zBMat9iucG_nesxY7BPI2iMffyYzg77lFsbfOIwpHbWM04YUoWBSqi0Ht_TECNjbHCzbBxUsgKjv0W_--nh1BmPQp60S90keWk_xthZFf5lEGPDe2m3mtWEhD2eJCtl03DgPTAPgfWOGeUjjlREhWfQi3gSOK8Op6OA4Wj3lfIpS02pRsuX5QY-YKqRznD7HPXvO5tUY2qlIgpvbBTkZ7HklJLPfAzOYhgJhkMOwHOXqzVI_1wHiMIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e716df92f8.mp4?token=e-OuIkDWvC16QfW8C49DprdiZyy-KApNXAfIYy2MG_h0QUu86_wmd7mFo6dTbn9dIFhXB-sZQ28-MkZ1ufKdx-Ei2GFcojZrCmeHopZjnxB6KD6zOFh98o_K0SC2yteUvFb0KEG0kQNAKe8g0GgXFpqhE5ur6HCXm9U5K9fIpwFY4IC4fYgjWDDiAswVCMjQrUVieZ9B9pdb4SLV84nhhv8S_hOC06g5ZnQthrEpcM6ALJRXJizkqKGA4MPFjGTcuAwpVRLLbLrxkbEAeDRKV9Ztwr8D_4GJbEHDwp3GSnUlUG1276H7xlIajt8YG3q6AML_as0sq0gJ0CRsgMrw5r_arhWSo8w-XdQrHtxypOFe6loJ2Al5EcAaaC4nu1Z_Y-kFWI_I-7BtOv7tbbi1Lvtp5AOp5STM8H_A_i7h3h_LUT2G1X3zBMat9iucG_nesxY7BPI2iMffyYzg77lFsbfOIwpHbWM04YUoWBSqi0Ht_TECNjbHCzbBxUsgKjv0W_--nh1BmPQp60S90keWk_xthZFf5lEGPDe2m3mtWEhD2eJCtl03DgPTAPgfWOGeUjjlREhWfQi3gSOK8Op6OA4Wj3lfIpS02pRsuX5QY-YKqRznD7HPXvO5tUY2qlIgpvbBTkZ7HklJLPfAzOYhgJhkMOwHOXqzVI_1wHiMIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عربستان حسن نیت نشان داد اما جمهوری اسلامی بازهم نیش زد!
🔴
هنگام ورود هیئت عربستانی و ادای احترام، آیه مخصوص منافقین خوانده شد و به عربستان متلک انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/131971" target="_blank">📅 00:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131970">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnbImx_9MX8_5JNFmy_blqWvYX3Wa_KDllcxRZ682r45Unw1n2iP3An3cY6xoPAoAAd16sHyyQp2jvKd4YDSabPaXzLNV_y3NGvrjvmXF3_yFBCIT1zeGHSG9JxfHY7RmmgXLIztULJTJb0skv7HEcoP2iBK1Dmad9QuswLzYdGc0sF4uMN12dCubFsiZVFsg0M3IVsPv6tVAS4quGpd_JUCPT4Mf07NVr0uCMSBXNWuv9EEP9R2Yb_WeBZFYWxt-_RiAv-tcbESZDFmJMA5C8TSDhxuSspwM99EpeQa1qW-g4V8koRUn5Qgc2z8VK-LkqiGq3O8zOM6cvW7lHw5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی زرنج شهر افغانستان، یه کودک 8 ساله در حوزه علمیه مورد تجاوز گروهی معلمان دینی خودش قرار میگیره و متاسفانه جون خودشو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/131970" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131969">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/131969" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131968">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lD2I3PSCAc9VuMFd6A3gLw0j0iCnj1Mg0AbbWqLejr6ZcA5ijBhA_tWL1s2F9quBW1e5hYNX96j3DjEC76Ud_XU83ivLtI1NEjOOvf3jiDaFs40-jquoYjX6RG0QsCx4Cun3911HvivQP8yYk1OBchm1YXMAudNykvK34-pVhPwBGVFKIkusAR1udsSTQAxASG5YsQ0QXqSNqAMjoXYZsVHk_HtNwAo0Vf--W3zha240lQ_xcx1KB7r7mjJ4rFRiKGzYpTPENDt7pLTC0hCoBbI52TnMZy8RfynWfTe3F7u0asOhJAk6EWmQTeVbhrsYkZYGe1SBZu3HYGeOukkGcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین پهپادهایی را به کریمه و غرب روسیه پرتاب کرده است.
🔴
منابع نظارتی نشان می‌دهند که تاکنون تا ۳۱۰ پهپاد پرتاب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/131968" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131967">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCsmtlQ7HxSIW9pvPiODowz2-nHw5QShpWNd_oMhXf5Cy9sU-yoImH6j7W6IYaRtulqI3aIp-uwLLb2nAJeVvuuBvQbK6h4zbgKLp4PkV7DluHJswYt-zJGOt8cKrELJMycM_eV-tx8IIg3jgoZ1DDV6X9yuMefT16tFgc39J0hJuaodew4R3zHM3LDsD7YWuGqwQHrqherhuKaRXsL3DBMM5GAWfWPjY9GbtN5smVzidp5u63CdxLAXo7NeXlyIgIUOuNqSJZSjHNY0RiviS8OosSaCWM0aHkTcZkDjQll15HNgToqBp6Gturb54qxE_CBXA-c0vYkBD0AuFOlWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال
:
تجمع ساعت ۷:۰۵ عصر شامل ۴۲۲,۰۰۰ نفر بود! همه مجبور به ترک محل شدند زیرا به دلیل آب‌وهوا، رویداد لغو شد و همه به دلیل رعد و برق رفته بودند.
🔴
وقتی شنیدم که لغو شده، بلافاصله آن تصمیم را تغییر دادم و مدتی صبر کردم تا مردم برگردند. باورنکردنی است که حداقل ۱۵۰,۰۰۰ نفر بازگشتند و این شبی حتی باشکوه‌تر از چیزی شد که به صورت عادی می‌توانست باشد! این نشان‌دهنده کار تحت فشار بود.
🔴
تبریک به سرویس مخفی و نیروهای قانون‌گذاری بابت توانایی بازگرداندن این‌همه نفر به داخل استادیوم به این سرعت!
🔴
این شبی شگفت‌انگیز بود که حتی باورنکردنی‌تر شد با این واقعیت که بلافاصله پس از پایان آتش‌بازی بزرگ، باران‌ها با تمام شدت شروع به باریدن کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/131967" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
استان خوزستان سه‌شنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131966" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131965">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51d88b2c6.mp4?token=QtCJAAC0b6kXuVXBDe-kawocxUfJoPMtvQt1QblC-PS1C_3gIJu4qxqnoiVaFGZFTKJOEqnhi7mFxUCjn9seXXGV5O3wDuMUNU2rXvh_bRZcHNo6QMeDyt56jgQLBiQC4KWL4NHr0m2H6oD3GnK9hOsfZ_it7WYnNjQA0523Mndka1Km7iHo5xtxynnMCutgsWG44qb-r5m-NGgdY6-fYQxcrpRNyXQZNScLZjSL4Vz52xiLhseVAflIISywFNaKJSm7J-E-Xz2ZR-t3_DSuXntlmRFaogF-ATg60eNXcwwZNak6MGsSU5w2BJQz9C5fVCZfHy8_Ws5F2YcgdLxnty84u-zgJihQwso-o40WYgM8hPruaw3VY3VvJueyMy7Jlxv7R2BvsP7Oe0qCtwV2rYv-lmpf-xFgbC3ynN8KNPZoedxbDHwJZPDM-4FXI_595vinaoB9eyWA8NTuX8hmU8ucG3loT0xRjm6b7K5gcnZhGU5Wd2uIRFYapO-GNAG9hBp8FG5K8XFiiQs9ODs_6yo5ExrZ5zp9F5zmg1vhbUKeIEuVsRUI3J-LssjBmczwWpuPlhXhZBE1NZHWNx47ej1JtWotvlZRodaTBFlKeg3dnA8tdnPZLdHXP9vbqKjuq3kw8OWff2ALUgpFX2ayJxuW7G7J3TnJ8ivvWFUu_j0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51d88b2c6.mp4?token=QtCJAAC0b6kXuVXBDe-kawocxUfJoPMtvQt1QblC-PS1C_3gIJu4qxqnoiVaFGZFTKJOEqnhi7mFxUCjn9seXXGV5O3wDuMUNU2rXvh_bRZcHNo6QMeDyt56jgQLBiQC4KWL4NHr0m2H6oD3GnK9hOsfZ_it7WYnNjQA0523Mndka1Km7iHo5xtxynnMCutgsWG44qb-r5m-NGgdY6-fYQxcrpRNyXQZNScLZjSL4Vz52xiLhseVAflIISywFNaKJSm7J-E-Xz2ZR-t3_DSuXntlmRFaogF-ATg60eNXcwwZNak6MGsSU5w2BJQz9C5fVCZfHy8_Ws5F2YcgdLxnty84u-zgJihQwso-o40WYgM8hPruaw3VY3VvJueyMy7Jlxv7R2BvsP7Oe0qCtwV2rYv-lmpf-xFgbC3ynN8KNPZoedxbDHwJZPDM-4FXI_595vinaoB9eyWA8NTuX8hmU8ucG3loT0xRjm6b7K5gcnZhGU5Wd2uIRFYapO-GNAG9hBp8FG5K8XFiiQs9ODs_6yo5ExrZ5zp9F5zmg1vhbUKeIEuVsRUI3J-LssjBmczwWpuPlhXhZBE1NZHWNx47ej1JtWotvlZRodaTBFlKeg3dnA8tdnPZLdHXP9vbqKjuq3kw8OWff2ALUgpFX2ayJxuW7G7J3TnJ8ivvWFUu_j0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما به خبرنگار نشریه تایمز: برو به مردم دنیا واقعیت ایران رو بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/131965" target="_blank">📅 23:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9_zTx5orcpGEqJx4P16U2ETrz_qSQp1CRaaIyWmBBRJVN9gd9fLojYqaCgSwk7P7tEh2Mz0NCxsX2lF66rvsz7pNPne7EwvP9KlE8PRCcZMKzM9oSocs8xCqpoZijMiTT0Fvspt6TVRLabVCtutbgmfRhEGYvWS0mFCztRpsPmT_sPaNEBTFnbAC9LUWR3R2zcLBwQzHd2O2M0cXD_OJnRSqTrrQ7PRtwBAiDiKWowcFwOsxjnhOVJ9Ub_jtJYNTe7506tMnExVRyLmgYIKqpplteKEv9XesG80L0wXzmAHhT41sgVI96Bh2eWLVodo1n3rCHKXuNnnSgo9amqIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسوشیتدپرس: یک مجری (محمد رسولی) در مراسم تشییع رهبری ایران در برابر جمعیتی متشکل از صدها هزار نفر، خواستار کشتن ترامپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/131964" target="_blank">📅 23:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر  شرکت نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131963" target="_blank">📅 23:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
زلنسکی: طبق اطلاعات به دست آمده، روسیه در حال آماده‌سازی یک حمله گسترده دیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131962" target="_blank">📅 23:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
خبرگزاری رویترز می‌گوید احتمال زیادی وجود دارد صندوق ۳۰۰ میلیارد دلاری بازسازی ایران هرگز عملی نشود.
🔴
این گزارش می‌افزاید یکی از ارکان اصلی آتش‌بس ماه گذشته میان واشینگتن و تهران، ایجاد یک صندوق ۳۰۰ میلیارد دلاری بازسازی ایران بعد از جنگ بود.
🔴
رویترز به ذخایر ۲ تریلیون دلاری سازمان سرمایه‌گذاری ابوظبی و صندوق سرمایه‌گذاری عمومی عربستان سعودی به عنوان گزینه‌های محتمل تامین مالی صندوق بازسازی ایران اشاره کرده، اما می‌گوید با توجه به حملات گسترده جمهوری اسلامی به این کشورها طی ماه‌های گذشته بعید است آنها صرفاً به درخواست واشینگتن هزینه احیای اقتصاد جمهوری اسلامی را بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/131961" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: واشنگتن در حال آماده‌سازی ارائه درخواست‌های رسمی به اسرائیل است که شامل موارد زیر می‌شود:
🔴
کاهش تعداد ایستگاه‌های بازرسی نظامی در کرانه باختری.
🔴
انتقال وجوهی که به دولت فلسطین تعلق دارد.
🔴
اتخاذ تدابیر سخت‌گیرانه‌تر برای محدود کردن اقدامات خشونت‌آمیز و پاسخگو کردن مسئولان آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131960" target="_blank">📅 23:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c5bb8bd4.mp4?token=cB-LO_u7hZUnV0PDlmVqPuqjN-srNDgVWiJyCfAjqDvWwI45ub0OqKVsUb4ZSg4R_7zrDvPCZCGBQp5k7kiejakY4y95-bvMSPkSIrX2uX0qRotDRJlkCwmItFr3tgmdsYwhA1VtrGOL_kFPhobqLR8Brm6vLuFPYUbfXP3mv_ra_ZrgY_AUgP_TH2StKti5k4CSC-qmSXSPAzEMjJaVhwb_YBaAMK-9rtcGIcLKk_d_Pge01q4W8xFY9e7QY_YsyuWhLvQusEV-Q0svvW1AOYcqZ5ASLLer7FhQlnUVuowJDRQX4bfoXavfkjdFxXijA11XojvkkADj7pT0JNY91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c5bb8bd4.mp4?token=cB-LO_u7hZUnV0PDlmVqPuqjN-srNDgVWiJyCfAjqDvWwI45ub0OqKVsUb4ZSg4R_7zrDvPCZCGBQp5k7kiejakY4y95-bvMSPkSIrX2uX0qRotDRJlkCwmItFr3tgmdsYwhA1VtrGOL_kFPhobqLR8Brm6vLuFPYUbfXP3mv_ra_ZrgY_AUgP_TH2StKti5k4CSC-qmSXSPAzEMjJaVhwb_YBaAMK-9rtcGIcLKk_d_Pge01q4W8xFY9e7QY_YsyuWhLvQusEV-Q0svvW1AOYcqZ5ASLLer7FhQlnUVuowJDRQX4bfoXavfkjdFxXijA11XojvkkADj7pT0JNY91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف‌های چندین کیلومتری بنزین در روسیه در پی حملات اوکراین به زیرساخت های نفتی این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/131959" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGCRURfVEoE0w1_xOPLJMD1vxfMRKnCqAKQ5-sFNzOSqm7Xdu2R6sG9f_odV_99E5HnRJhLl2UUbh3Yj7GQGBoDJBktTLcrK48fevGsQwrG-c_0MZGERoInm50KV9dP67lNIrpP0w_rfIjTCY5N60G8WMd6HiD-07CHnVX6pmxzCzhY25OgFSZQUQjx6FPmTLvuzj-FcRZ91XG_m7OnvWh7imB03Q-c9yyY-8g46PLtlq40gRaKn4Cr4I6dw6wolfKMVd2lhdeW5QH42VvtWcK4WtXkf4X3w-iwObd6lemtbxfojS9mh4KaRr9Ztxd73ZJllNyFR4Yuo1Q6IFNsqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابلوهای جدید بزرگراه I-95 در جنوب فلوریدا اکنون مسافران را به سمت فرودگاه بین‌المللی رئیس‌جمهور دونالد جی. ترامپ هدایت می‌کنند، حتی پیش از تغییر نام رسمی فرودگاه بین‌المللی پالم بیچ که برای 9 ژوئیه برنامه‌ریزی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/131958" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEQ1lSeZM78TW7ZAmaMqltZs_0_DHdPKryGGio4Ozdi0LMCiwku_hab8OpXpTCzz48Uqb6SWfF0RuCsUyFu6aYxNg9ynSMqRNKbxhrFDis5bEU8Do5m_ORmCSwe2IsOv39F3CdtNErxn-hkjWq8qGEs3qgA6ZdQz8gp5nbsv82Rqi8sWJ6LAEOQSrbfuqwbMJGsRARxErLa5lw6itiaxbS0vONJ9d0SuMK2i426Fon4F-B3z4aXeKXbgtWjngZYO0Jly6bPRlH4oSXbBlhIKSjr3JdwA6bnGKrcGkwkJKdxYzDsT1Vm7qG798oQoe9gSr0ML8eOHPlm544l-2RvvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
⛔️
تصویری لو رفته از همسر سپهر حیدری و ساسی مانکن در ویلای شخصی ساسی
‼️
⛔️
گفته میشه دلیل طلاق اسطوره پرسپولیس هم همین عکس بوده!
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/131957" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
شمار قربانیان دو زلزله مرگبار هفته گذشته در ونزوئلا، بر اساس آمار رسمی منتشرشده در روز شنبه، به حدود 3 هزار کشته رسید. هم‌زمان، با کاهش امیدها برای یافتن بازماندگان، تیم‌های بین‌المللی امداد و نجات عملیات جست‌وجو در زیر آوار را محدود کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/131956" target="_blank">📅 22:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131955">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXNncOnrcqzYcD4fsjbFY62RHzl-RFKVJNna0_rNK0b-eHeqWQNWVwRY_ST6kdSkTTs_COT6KW9tyzje5SYQOLvO80HQGcMXHNu2BNhRRnf_W-Uh9mrx61xV2N1WGheA0pheAiSrAZQZeDxgy0OWd0gEqcKMODTNpSkpuTlgATpdklorIR6rzpXDQctCq8-cWfij72Nio355NCwuEw2q-yHzlhlFEf_oInh59WEFQNsNbN7W6REFVF1UTW-e78cx66cb0hBvE08GpOra-xMjhh0aP4MPIwxnqXhId7Ifvo9-dhX6jYsibztsS9Gzx-9qh7_BuXzdsPu-nG2Yy7M44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: هیچ کاری وجود ندارد که آمریکایی‌ها نتوانند انجام دهند به جز شناسنامه رای‌دهنده (شناسایی)، اثبات تابعیت یا، مهم‌تر از همه، لغو مانور پارلمانی (که دموکرات‌ها بلافاصله پس از به دست گرفتن قدرت انجام خواهند داد، و ۲ ایالت دیگر، ۴ سناتور دیگر، ۸ نماینده کنگره دیگر، حداقل ۲۰ رای الکترال اضافه خواهند کرد، و غیرممکن خواهد بود که یک جمهوری‌خواه هرگز دوباره به عنوان رئیس‌جمهور انتخاب شود. من نمی‌خواهم آخرین رئیس‌جمهور جمهوری‌خواه باشم!).
🔴
جمهوری‌خواهان، هوشمند شوید، اگر این کار را نکنید، مدت زیادی در قدرت نخواهید بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/131955" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سی‌ان‌ان: ایالات متحده انتظار دارد رهبران ناتو در اجلاس خود درباره امنیت تنگه هرمز گفت‌وگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131954" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بر اساس گزارش ها ،در درگیری های اخیر یمن حدود 50 عضو از حوثی ها کشته شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/131953" target="_blank">📅 22:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=DmJlz2WYFtqQ5FOVpwuWK2NoRiC3-HNU6GH85qrJRBgC-DyLjGbjO8V3aqXeulDeDpmW3K37gSfnPJl49EKhQDgscVzw1bFrnwLqlqfZorJHbmNt_iAC61o9mOUb04RPEWFk5UZCYLxo1TXE0sS9EYq14meJRJ-1ydhnaeg6o3SLcJjGG9OOBTCY5_P4AJ0wqnhvqOU5E-o2rFAVMgAykCppSPuN6dWwH_Ai7BKkFf4EySK26PfYVU1YfJZaDnz78j7H7FlkWoTGM8z-OIAMFw-OU4mLQW-EQvdPs6ZKphBkjxxIufUR-tpfwMGfJrT8sq5TpBare1VPLoFue4SEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=DmJlz2WYFtqQ5FOVpwuWK2NoRiC3-HNU6GH85qrJRBgC-DyLjGbjO8V3aqXeulDeDpmW3K37gSfnPJl49EKhQDgscVzw1bFrnwLqlqfZorJHbmNt_iAC61o9mOUb04RPEWFk5UZCYLxo1TXE0sS9EYq14meJRJ-1ydhnaeg6o3SLcJjGG9OOBTCY5_P4AJ0wqnhvqOU5E-o2rFAVMgAykCppSPuN6dWwH_Ai7BKkFf4EySK26PfYVU1YfJZaDnz78j7H7FlkWoTGM8z-OIAMFw-OU4mLQW-EQvdPs6ZKphBkjxxIufUR-tpfwMGfJrT8sq5TpBare1VPLoFue4SEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/131952" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بانک مرکزی: سامانه‌های سحاب، پل و پایا جهت انتقال وجه روز دوشنبه فعال هستند
🔴
با توجه به تعطیلی رسمی فردا، سامانه‌های ساتنا و چکاوک روز دوشنبه ۱۵ تیر در دسترس نخواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/131951" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دلار در تهران به 177هزار تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/131950" target="_blank">📅 21:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ6-838tm52Bl-XosomKAhN92iNLa1-ODwM-X_ZqWf5Y27GsAo-xbEGZ1pErggrrN-4zLQ3zcjvSC3CCxXzqoFFt89nm3QVFPVYdKXRjb_CvHwjJYRtAqXV5gpNu2K3cvzlackHVxLwzpHLH3G_Rz816XmYXomHiJeNAWrtLzSbVUMXrrX42-LA-MoY0savoxX-px074z75WrdsRIOxxp2PhnatjttsDUV7cyQByEVw5BFKCo1C7npdC5JGW1QAtQ7vwobzSvFFTxdxOUroWRjLCH1OduCP7nl7uXIu6mIr1bIPSrLMYHvv96tLoUCVu4ZHJTnQxxAQtGI532we4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه امیدِ صداوسیما:
برید تو بازی ماینکرفت، انتقامِ رهبر شهیدمون رو از آمریکا و اسرائیلِ جنایتکار بگيريد و فیلمش رو واسمون بفرستيد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/131949" target="_blank">📅 21:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131948">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نتانیاهو: فکر نمی‌کنم میان من و ترامپ شکافی وجود داشته باشد
🔴
در ۹۹ درصد موارد، من و رئیس‌جمهور آمریکا کاملاً هم‌نظر هستیم، اما مانند هر رابطه‌ای گاهی اختلاف نظر هم وجود دارد
🔴
کسانی که از اسرائیل نفرت دارند، در نهایت به آمریکا هم نفرت پیدا می‌کنند؛ وقتی تظاهرات می‌کنند، پرچم اسرائیل را آتش می‌زنند و خیلی وقت‌ها درست کنار آن، پرچم آمریکا را هم آتش می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131948" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131947">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/131947" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ادعای شبکه عبری کان: در روزهای اخیر، گفت‌وگویی میان ارتش اسرائیل و ارتش لبنان با میانجی‌گری آمریکا آغاز شده تا معیار روشنی برای مفهومِ “منطقه عاری از حزب‌الله” تعیین شود.
🔴
تنها پس از آن، ارتش اسرائیل مطابق یک طرح آزمایشی و بر اساس تفاهمات انجام‌شده در آمریکا، از مزرعة‌الغربیه و فرون عقب‌نشینی خواهد کرد.
🔴
همزمان، از سوی اسرائیل نام شماری از افسران لبنانی که با حزب‌الله همکاری می‌کنند، منتقل شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/131946" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الحدث: نتانیاهو در دیدار خود با ترامپ، تلاش خواهد کرد تا بر "توافق" بین واشنگتن و تهران تأثیر بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/131945" target="_blank">📅 21:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK624BmZ4gF_MF-RAv4MiR7IZ7DfsPInG26Wt4ozbS_PETHwJtnV_yp4iBi7AHGB24GEcyaiPeJoDmTOBEYXDjxF_KDk8o5XbE84AkUvwe2GKMs5JEgQdgnmrRH53iiyM9uqhMtt_BOF-N-dXFgTXWtr6kUltDNuV1ajL0as-3BjuVJ-9Ju0imJbsWqbJDy9vqkoxycyEzRTJmbI5ao2o9qwoyK6IsgVI0CE70r3tOTwcKk9HQyWZtViF3R1TuV8Mw5Bk_NpnW2YoYP2kvZxNObkcOBQWjiweAYdnoop51L4aXSYjl-qZHsxLFMhYkuuttRU6rOzAZzjj5Mt-gERjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/131944" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیدار کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131943" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e189569c76.mp4?token=RcIEJhqSRtuBMg2ge7T3IZR3_gtFmrJ6ZJlvJij7MwWzjBcECf1N54FA1Y7P-MK9epW37QNb0oXuHxJEhKC9XDrm_GL_66i75SsjWG9HVjrRgSOFy04GPIBMH6Mdz0LnNZls5VeKxnCGeLo3ns8VVSpssgSb_VaylmfT1Vx1tMDYkFhgoElEymX7cDBHooS-apy2it-JbxnCrP085a1N-Owhkkgs9l_-NbYM8-vOykH0OCdjwCo05dd25nVGIpBLrIp7IJPbbBwZ3yC4qAnVCNYrEO8wiGM0mF0dc_Aem9ugKCwN41uoKhNtAVPtb7g-0wSTF1_xROJTqN3cFXbgYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e189569c76.mp4?token=RcIEJhqSRtuBMg2ge7T3IZR3_gtFmrJ6ZJlvJij7MwWzjBcECf1N54FA1Y7P-MK9epW37QNb0oXuHxJEhKC9XDrm_GL_66i75SsjWG9HVjrRgSOFy04GPIBMH6Mdz0LnNZls5VeKxnCGeLo3ns8VVSpssgSb_VaylmfT1Vx1tMDYkFhgoElEymX7cDBHooS-apy2it-JbxnCrP085a1N-Owhkkgs9l_-NbYM8-vOykH0OCdjwCo05dd25nVGIpBLrIp7IJPbbBwZ3yC4qAnVCNYrEO8wiGM0mF0dc_Aem9ugKCwN41uoKhNtAVPtb7g-0wSTF1_xROJTqN3cFXbgYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزمایش موشک‌های ناوچه "جیانگ جیان" کره شمالی، دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/131942" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
